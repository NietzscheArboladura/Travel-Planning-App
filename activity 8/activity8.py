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
        choice = int(input('\n1.) User\n2.) Transportaion\n3.) Schedule\n0.) Exit\nEnter choice[0-3]: '))
        
        if (choice == 1):
            # User
            choice = int(input('\n=== User ===\n1.) Add New User\n2.) View all Users \n3.) Add Destination that user wants to go\n4.) Delete a User and Destination\n0.) Exit\nEnter choice[0-4]: '))
                
            if (choice == 1):
                # Add transportation
                id = id + 1
                name = input('\nEnter New User: ')
                student = Student(id, name)
                school_management.register_student(student)
                print('\nTransportation type successfuly added!!!\n')

            elif (choice == 2):
                # View transportaion type
                print('\n=== View all Users ===')
                print(school_management.registered_students())

            elif (choice == 3):

                print('\n=== Add Destination that user wants to go ===\n')

                try:
                    
                    if len(school_management.registered_students()) == 0:
                        raise Exception('No students registered')
                    students = school_management.students
                    select = int(input(f'Select User: {school_management.registered_students()}\n'))
                    selected_student = students[select-1]
                    section = int(input('Select a Destination: 3.) London 4.) Philippines: '))
                    if section == SectionEnum.London.value:
                        selected_student.set_section(SectionEnum.London)
                    elif section == SectionEnum.Philippines.value:
                        selected_student.set_section(SectionEnum.Philippines)
                    print('\nDestination successfuly added!!!\n')
                except Exception as e:
                    print(e)
                    # 
               
            elif (choice == 4):

                try:
                    if len(school_management.registered_students()) == 0:
                        raise Exception('No User registered')
                    select = int(input(f'Select User: {school_management.registered_students()}\n'))
                    selected_student = students[select-1]
                    
                    school_management.unregister_student(selected_student)
                    print('\nUser and Destination successfuly deleted!!!\n')
                except Exception as e:
                    print(e)
                
            elif (choice == 0):
                print('Exiting...')
                break


        elif (choice == 2):
            # Transportation
            choice = int(input('\n=== Transportation ===\n1.) Add transportation type\n2.) View all transportation type\n3.) add mode of payment\n4.) Delete a transportaion type and mode of payment\n0.) Exit\nEnter choice[0-4]: '))
                
            if (choice == 1):
                # Add transportation
                id = id + 1
                name = input('\nEnter Transportation type: ')
                student = Student(id, name)
                school_management.register_student(student)
                print('\nTransportation type successfuly added!!!\n')

            elif (choice == 2):
                # View transportaion type
                print('\n=== View registered tranportation ===')
                print(school_management.registered_students())

            elif (choice == 3):

                print('\n=== Add mode of payment ===\n')

                try:
                    
                    if len(school_management.registered_students()) == 0:
                        raise Exception('No Transportation registered')
                    students = school_management.students
                    select = int(input(f'Select student: {school_management.registered_students()}\n'))
                    selected_student = students[select-1]
                    section = int(input('Select mode of payment: 1.) Cash 2.) Credit: '))
                    if section == SectionEnum.Cash.value:
                        selected_student.set_section(SectionEnum.Cash)
                    elif section == SectionEnum.Credit.value:
                        selected_student.set_section(SectionEnum.Credit)
                    print('\nMode of payment successfuly added!!!\n')
                except Exception as e:
                    print(e)
                    # 
               
            elif (choice == 4):

                try:
                    if len(school_management.registered_students()) == 0:
                        raise Exception('No students registered')
                    select = int(input(f'Select student: {school_management.registered_students()}\n'))
                    selected_student = students[select-1]
                    
                    school_management.unregister_student(selected_student)
                    print('\nTranspor and Mode of payment successfuly deleted!!!\n')
                except Exception as e:
                    print(e)
                


            elif (choice == 0):
                print('Exiting...')
                break

        elif (choice == 3):
            # Schedule

            choice = int(input('\n=== Schedule ===\n1.) Add preferred schedule\n 2.) View all schedule \n3.) Morning or Evening\n4.) Delete a schedule \n0.) Exit\nEnter choice[0-4]: '))
                
            if (choice == 1):
                # Add transportation
                id = id + 1
                name = input('\nEnter preferred time: ')
                student = Student(id, name)
                school_management.register_student(student)
                print('\Schedule successfuly added!!!\n')

            elif (choice == 2):
                # View transportaion type
                print('\n=== View all schedule ===')
                print(school_management.registered_students())

            elif (choice == 3):

                print('\n===  Morning or Evening ===\n')

                try:
                    
                    if len(school_management.registered_students()) == 0:
                        raise Exception('No Schedule registered')
                    students = school_management.students
                    select = int(input(f'Select Schedule: {school_management.registered_students()}\n'))
                    selected_student = students[select-1]
                    section = int(input('Select choice: 5.) Morning 6.) Evening: '))
                    if section == SectionEnum.AM.value:
                        selected_student.set_section(SectionEnum.AM)
                    elif section == SectionEnum.PM.value:
                        selected_student.set_section(SectionEnum.PM)
                    print('\nSchedule successfuly added!!!\n')
                except Exception as e:
                    print(e)
                    # 
               
            elif (choice == 4):

                try:
                    if len(school_management.registered_students()) == 0:
                        raise Exception('No Schedule registered')
                    select = int(input(f'Select Schedule: {school_management.registered_students()}\n'))
                    selected_student = students[select-1]
                    
                    school_management.unregister_student(selected_student)
                    print('\nnSchedule successfuly deleted!!!\n')
                except Exception as e:
                    print(e)
                

            elif (choice == 0):
                print('Exiting...')
                break
        
        elif (choice == 0):
            print('Exiting...')
            break