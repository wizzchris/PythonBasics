

class ExamSitting:
    def __init__(self, exam_id):
        self.exam_id = exam_id
        self.__attendee = []

    def add_student(self,student):
        self.__attendee.append(student)

    def get_attendee(self):
        num_of_students = 0
        print ('Index \\ Student id \\ Student name')
        for student in self.__attendee:
            num_of_students += 1
            return str(num_of_students) + ' - ' + str(student.uni_id) + ' - ' + str(student.name)
