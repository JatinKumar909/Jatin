class AttendanceRegister:
    def __init__(self):
        self.attendance = {}

    def mark_attendance(self, student_name):
        if student_name in self.attendance:
            print(f"{student_name} ka attendance pehle hi mark kiya gaya hai.")
        else:
            self.attendance[student_name] = True
            print(f"{student_name} ka attendance mark kiya gaya hai.")

    def display_attendance(self):
        print("Attendance Register:")
        for student, present in self.attendance.items():
            status = "Present" if present else "Absent"
            print(f"{student}: {status}")

if __name__ == "__main__":
    register = AttendanceRegister()

    while True:
        print("\n1. Mark Attendance")