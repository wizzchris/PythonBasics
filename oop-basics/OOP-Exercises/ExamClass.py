
from ExamSittingClass import ExamSitting
from SutdentMonster import StudentMonster

class Exam:

    __exam_id = 0

    def __init__(self,topic,time,format):
        self.topic = topic
        self.time = time
        self.format = format
        self.__exam_id = Exam.__exam_id
        Exam.__exam_id += 1
        self.examsitting = ExamSitting(self.__exam_id)


    def get_exam_id(self):
        return self.__exam_id

    def get_exam_attendie(self):
        return self.examsitting.get_attendee()

    def add_student(self,name):
        return self.examsitting.add_student(name)






