from interfaces import *
from location import *
from users import Users

class TravelManagement(IRegistrar, ITravelRecords, ITraveling):
    
    def __init__(self) -> None:
        self.users: List[Users] = []
    def register_user(self, user: Users) -> None:
        self.users.append(user)
        
    def unregister_user(self, user: Users) -> None:
        self.users.remove(user)
    
    def assign_user_to_location(self, user: Users, location: LocationEnum) -> None:
        if location == LocationEnum.G1:
            user.set_location(LocationEnum.G1)
        elif location == LocationEnum.G2:
            user.set_location(LocationEnum.G2)
        
    def registered_users(self) -> str:
        
        res = ''
        for user in self.users:
            res = res + str(user) + ', '
        return res
        
        