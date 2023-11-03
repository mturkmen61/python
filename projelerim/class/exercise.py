class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def show_school_info(self):
        print('school name:', self.name)
        print('school city:', self.city)



school_1 = School('itü', 'istanbul')
school_2 = School('odtü', 'ankara')


class Student:
    def __init__(self, name, birth_year, school):
        self.name = name
        self.birth_year = birth_year
        self.school = school

    def show_student_info(self):
        print('student name:', self.name)
        print('student birth year:', self.birth_year)
        self.school.show_school_info()

    

student_1 = Student("Harun",1998,school_1)
student_2 = Student("Mustafa",2001,school_2)

student_1.show_student_info()
print()
student_2.show_student_info()
       


# Student: name(string), birth_year(int), school(School)

