class Student:
      marks = "67%"
      name = 'Ed sheeran'

person = Student()

name = getattr(person, 'name')
print(name)

marks = getattr(person, 'marks')
print(marks)
