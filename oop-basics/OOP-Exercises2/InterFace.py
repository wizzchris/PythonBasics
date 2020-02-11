import ExamClass as ec
from ExamSittingClass import ExamSitting
from SutdentMonster import StudentMonster

#Empty lists to act as fake DB.
exams = []
students = []

while True:
    answer = input('What would you like to do? Type HELP for commands or EXIT to exit\n').strip().lower()

    if answer == 'exit':
        break

    elif answer == 'help':
        print('Type exit to exit \n Type help for help \n Type add exam to add exam \n type add student to add a student to register \n type add student to exam to add student to an exam \n type get attendees to get attendees for an exam')

    elif answer == 'add exam':

        exam_name = input('What is the exams name?\n')
        exam_topic = input('What is the topic?\n')
        exam_time = input('What is the exams time? Mor, Noon, Night\n')
        exam_format = input('What is the format? Paper, Vocal, Online\n')
        exam_name = ec.Exam(exam_topic,exam_time,exam_format)
        exams.append(exam_name)


    elif answer == 'add student':
        student_name = input('What is the students name?\n')
        student_strength = input('What is the students strength?\n')
        student_skills = input('What is the students skill?\n')

        student_obj = StudentMonster(student_name, student_strength, student_skills)

        students.append(student_obj)

    elif answer == 'add student to exam':

        for student in students:
            print (student.name, student.uni_id, student.scary_skills)

        student_name = input('What is the students name? list above\n')
        for exam in exams:
            print (exam.topic)
        exam_name = input('What is the exam?\n')
        for student in students:
            if student_name == student.name:
                student_name = student
        for exam in exams:
            if exam_name == exam.topic:
                exam_name = exam
        exam_name.add_student(student_name)

    elif answer == 'get attendees':
        for exam in exams:
            print (exam.topic)
        exam_name = input('What is the exam name?\n')
        for exam in exams:
            if exam_name == exam.topic:
                exam_name = exam
            else:
                print('Sorry not a valid choice')
        print(exam_name.get_exam_attendie())

    elif answer == 'exam id':
        for exam in exams:
            print (exam.topic)
        exam_name = input('What is the exam name?\n')
        for exam in exams:
            if exam_name == exam.topic:
                exam_name = exam
            else:
                print('thats not a valid name')
        print(exam_name.get_exam_id())

    else:
        print('Sorry that is not a valid command')