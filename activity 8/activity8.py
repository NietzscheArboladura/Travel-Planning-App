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
        choice = int(input('\n1.) User\n2.) Destination\n3.) Transportaion\n4.) Schedule\n5. Payment\n0.) Exit\nEnter choice[0-5]: '))
        
        if (choice == 1):
            # User
            id = id + 1
            name = input('Enter student name: ')
            student = Student(id, name)
            school_management.register_student(student)
            
        elif (choice == 2):
            # Destination
            print('=== View registered students ===')
            print(school_management.registered_students())
            
        elif (choice == 3):
            # Transportation
            choice = int(input('\n=== Transportation ===\n1.) Add transportation type\n2.) View all transportation type\n3.) Delete a transportaion type\n0.) Exit\nEnter choice[0-3]: '))
                
            if (choice == 1):
                # Add transportation
                id = id + 1
                name = input('Enter Transportation type: ')
                student = Student(id, name)
                school_management.register_student(student)

            elif (choice == 2):
                # View transportaion type
                print('=== View registered students ===')
                print(school_management.registered_students())

            elif (choice == 3):

                print('\n=== Delete ===\n')
               
            elif (choice == 0):
                print('Exiting...')
                break


        elif (choice == 4):

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
        
        elif (choice == 5):
            # Schedule
            try:
                if len(school_management.registered_students()) == 0:
                    raise Exception('No students registered')
                select = int(input(f'Select student: {school_management.registered_students()}\n'))
                selected_student = students[select-1]
                
                school_management.unregister_student(selected_student)
            except Exception as e:
                print(e)
        
        elif (choice == 6):
            print('Exiting...')
            break