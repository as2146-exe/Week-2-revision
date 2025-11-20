class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade
    
    def add_module(self, module, grade):
        self.module = module
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, grade: {self.grade}"
    
    def display(self):
        print(self)

    def update_name(self, new_name):
        self.name = new_name
    

s1 = Student("Alice", 94428923, 85)
s1.update_name("Alicia") 
s1.display()

        