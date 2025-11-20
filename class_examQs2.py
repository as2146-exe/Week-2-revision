class Student:
    def __init__(self, student_id, first_name, last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = ""
        self.modules = {}

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    
    def update_email(self, new_email):
        if "@" in new_email:
            self.email = new_email
        else:
            print("Invalid email Address")

    def add_module(self, module_name, grade):
        self.modules[module_name] = grade 

    def average_grade(self):
        total = sum(self.modules.values())
        count = len(self.modules)
        return total / count

s1 = Student(857463, "Alice", "Smith")
s1.update_email("alsj.silver@gmail.com")
s1.add_module("Maths", 84)
s1.add_module("Chemistry", 78)
s1.add_module("English", 87)

print(s1.email)
print(s1.modules)

print("Average", s1.average_grade())
    
        