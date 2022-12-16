from users import Users
from interfaces import *
from travelmanagement import *
from location import *

class ProcessType(Enum):
    EXIT = 0
    REGISTER_USER = 1
    VIEW_USER = 2
    ASSIGN_USER_TO_LOCATION = 3
    UNREGISTER_USER = 4
    
if __name__ == "__main__":
    travel_management = TravelManagement()
    
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
                user = Users(id, name)
                travel_management.register_user(user)
                print('\nTransportation type successfuly added!!!\n')

            elif (choice == 2):
                # View transportaion type
                print('\n=== View all Users ===')
                print(travel_management.registered_users())

            elif (choice == 3):

                print('\n=== Add Destination that user wants to go ===\n')

                try:
                    
                    if len(travel_management.registered_users()) == 0:
                        raise Exception('No users registered')
                    users = travel_management.users
                    select = int(input(f'Select User: {travel_management.registered_users()}\n'))
                    selected_user = users[select-1]
                    location = int(input('Select a Destination: 3.) London 4.) Philippines: '))
                    if location == LocationEnum.London.value:
                        selected_user.set_section(LocationEnum.London)
                    elif location == LocationEnum.Philippines.value:
                        selected_user.set_section(LocationEnum.Philippines)
                    print('\nDestination successfuly added!!!\n')
                except Exception as e:
                    print(e)
                    # 
               
            elif (choice == 4):

                try:
                    if len(travel_management.registered_users()) == 0:
                        raise Exception('No User registered')
                    select = int(input(f'Select User: {travel_management.registered_users()}\n'))
                    selected_user = users[select-1]
                    
                    travel_management.unregister_user(selected_user)
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
                user = Users(id, name)
                travel_management.register_user(user)
                print('\nTransportation type successfuly added!!!\n')

            elif (choice == 2):
                # View transportaion type
                print('\n=== View registered tranportation ===')
                print(travel_management.registered_users())

            elif (choice == 3):

                print('\n=== Add mode of payment ===\n')

                try:
                    
                    if len(travel_management.registered_users()) == 0:
                        raise Exception('No Transportation registered')
                    users = travel_management.users
                    select = int(input(f'Select user: {travel_management.registered_users()}\n'))
                    selected_user = users[select-1]
                    location = int(input('Select mode of payment: 1.) Cash 2.) Credit: '))
                    if location == LocationEnum.Cash.value:
                        selected_user.set_section(LocationEnum.Cash)
                    elif location == LocationEnum.Credit.value:
                        selected_user.set_section(LocationEnum.Credit)
                    print('\nMode of payment successfuly added!!!\n')
                except Exception as e:
                    print(e)
                    # 
               
            elif (choice == 4):

                try:
                    if len(travel_management.registered_users()) == 0:
                        raise Exception('No users registered')
                    select = int(input(f'Select user: {travel_management.registered_users()}\n'))
                    selected_user = users[select-1]
                    
                    travel_management.unregister_user(selected_user)
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
                user = Users(id, name)
                travel_management.register_user(user)
                print('\Schedule successfuly added!!!\n')

            elif (choice == 2):
                # View transportaion type
                print('\n=== View all schedule ===')
                print(travel_management.registered_users())

            elif (choice == 3):

                print('\n===  Morning or Evening ===\n')

                try:
                    
                    if len(travel_management.registered_users()) == 0:
                        raise Exception('No Schedule registered')
                    users = travel_management.users
                    select = int(input(f'Select Schedule: {travel_management.registered_users()}\n'))
                    selected_user = users[select-1]
                    location = int(input('Select choice: 5.) Morning 6.) Evening: '))
                    if location == LocationEnum.AM.value:
                        selected_user.set_section(LocationEnum.AM)
                    elif location == LocationEnum.PM.value:
                        selected_user.set_section(LocationEnum.PM)
                    print('\nSchedule successfuly added!!!\n')
                except Exception as e:
                    print(e)
                    # 
               
            elif (choice == 4):

                try:
                    if len(travel_management.registered_users()) == 0:
                        raise Exception('No Schedule registered')
                    select = int(input(f'Select Schedule: {travel_management.registered_users()}\n'))
                    selected_user = users[select-1]
                    
                    travel_management.unregister_user(selected_user)
                    print('\nnSchedule successfuly deleted!!!\n')
                except Exception as e:
                    print(e)
                

            elif (choice == 0):
                print('Exiting...')
                break
        
        elif (choice == 0):
            print('Exiting...')
            break