class Student:
    def __init__(self, name, s_number):
        self.name = name
        self.sNumber = s_number
        self.courses = []

    def register(self, course):
        if self.is_registered(course):
            print(f"You are already registered for : {course.name}")
        else:
            course.register_student(self)
            self.courses.append(course)
            print(f"add course : {course.name} to student : {self.name}")

    def is_registered(self, course):
        return course in self.courses


class Course:
    def __init__(self, name, value, capacity):
        self.name = name
        self.value = value
        self.capacity = capacity
        self.students = []

    def register_student(self, student):
        if self.is_full():
            print("course is full")
        else:
            self.students.append(student)

    def is_full(self):
        # print(f"students len : {len(self.students)} capacity is : {self.capacity}")
        # print(len(self.students) >= self.capacity)
        return len(self.students) >= self.capacity


# Create some students
student1 = Student("Alice", 1)
student2 = Student("Bob", 2)

# Create a course
course1 = Course("Math", 3, 1)

# Sign up students for the course
student1.register(course1)
student2.register(course1)
student1.register(course1)  # Trying to sign up again

# Output the course's student list
print(f"Students enrolled in {course1.name}:")
for student in course1.students:
    print(student.name)
