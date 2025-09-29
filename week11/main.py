import sys
import os
import sqlite3
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "student.db")
UI_PATH = os.path.join(BASE_DIR, "student_from.ui")

def init_db():
    """Create DB and table if not exists."""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS profile (
                    id_student TEXT PRIMARY KEY NOT NULL,
                    first_name TEXT,
                    last_name TEXT,
                    major TEXT)""")
        conn.commit()
    finally:
        conn.close()

class StudentForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_PATH, self)

        init_db()

        self.pushButton.clicked.connect(self.saveData)

    def saveData(self):
        student_ID = self.lineEdit.text().strip()
        first_name = self.lineEdit_2.text().strip()
        last_name = self.lineEdit_3.text().strip()
        major = self.lineEdit_4.text().strip()

        if not all([student_ID, first_name, last_name, major]):
            QMessageBox.warning(self, "ข้อมูลไม่ครบถ้วน", "กรุณากรอกข้อมูลให้ครบทุกช่อง")
            return

        try:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO profile (id_student, first_name, last_name, major) VALUES (?, ?, ?, ?)",
                (student_ID, first_name, last_name, major)
            )
            conn.commit()
        except sqlite3.IntegrityError as e:
            QMessageBox.critical(self, "บันทึกข้อมูลล้มเหลว", f"ไม่สามารถบันทึกได้: {e}")
            return
        except Exception as e:
            QMessageBox.critical(self, "บันทึกข้อมูลล้มเหลว", f"เกิดข้อผิดพลาด:\n{e}")
            return
        finally:
            conn.close()

        QMessageBox.information(
            self,
            "ข้อมูลนักศึกษา",
            f"รหัสนักศึกษา : {student_ID}\n"
            f"ชื่อ : {first_name}\n"
            f"นามสกุล : {last_name}\n"
            f"สาขาวิชา : {major}\n"
        )

        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = StudentForm()
    window.show()
    sys.exit(app.exec_())