from students import Student
from interfaces import *
from schoolmanagement import *
from sections import *

class ProcessType(Enum):
    EXIT = 0
    REGISTER_STUDENT = 1
    VIEW_STUDENTS = 2
    ASSIGN_STUDENT_TO_SECTION = 3
    UNREGISTER_STUDENT = 4
    
if __name__ == "__main__":
    school_management = SchoolManagement()
    
    choice = -1
    id = 0
    while (choice != 0):
        choice = int(input('What would you like to do? 1.) Register a student 2.) View all registered students 3.) Assign a section to a student 4.) Un-register a student 0.) Exit\n'))
        
        if choice == ProcessType.REGISTER_STUDENT.value:
            id = id + 1
            name = input('Enter student name: ')
            student = Student(id, name)
            school_management.register_student(student)
            
        elif choice == ProcessType.VIEW_STUDENTS.value:
            print(school_management.registered_students())
            
        elif choice == ProcessType.ASSIGN_STUDENT_TO_SECTION.value:
            try:
                
                if len(school_management.registered_students()) == 0:
                    raise Exception('No students registered')
                students = school_management.students
                select = int(input(f'Select student: {school_management.registered_students()}\n'))
                selected_student = students[select-1]
                section = int(input('Select section: 1.) G1 2.) G2: \n'))
                if section == SectionEnum.G1.value:
                    selected_student.set_section(SectionEnum.G1)
                elif section == SectionEnum.G2.value:
                    selected_student.set_section(SectionEnum.G2)
            except Exception as e:
                print(e)
        
        elif choice == ProcessType.UNREGISTER_STUDENT.value:
            try:
                if len(school_management.registered_students()) == 0:
                    raise Exception('No students registered')
                select = int(input(f'Select student: {school_management.registered_students()}\n'))
                selected_student = students[select-1]
                
                school_management.unregister_student(selected_student)
            except Exception as e:
                print(e)
        
        elif choice == ProcessType.EXIT.value:
            print('Exiting...')
            break