class Student:
    def __init__(self, name: str, student_id: str) -> None:
        self.name = name
        self.student_id = student_id
        self.__grades = []
        print(f"Yangi talaba yaratildi: {self.name}, ID: {self.student_id}, boshlang'ich baholar ro'yxati bo'sh.")

    def add_grade(self, grade: int) -> None:
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(f"{grade} bahosi qo'shildi.")
        else:
            print("Xato: Noto'g'ri baho")

    def calculate_average(self) -> float:
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades)

    def get_status(self) -> str:
        average = self.calculate_average()
        if 90 <= average <= 100:
            return "A'lo"
        elif 80 <= average <= 89:
            return "Yaxshi"
        elif 70 <= average <= 79:
            return "Qoniqarli"
        else:
            return "Qoniqarsiz"



student = Student("Nodira", "S123")
student.add_grade(85)
student.add_grade(90)
print(student.calculate_average())  
print(student.get_status())         
student.add_grade(150)             
