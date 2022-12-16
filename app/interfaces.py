from abc import ABC, abstractmethod
from users import Users
from location import *
from typing import List

class IRegistrar(ABC):
    
    @abstractmethod
    def register_user(self, user: Users) -> None: pass
    
    @abstractmethod
    def unregister_user(self, user: Users) -> None: pass

class ITravelRecords(ABC):
    @abstractmethod
    def registered_users(self) -> List: pass

        
class ITraveling(ABC):
   @abstractmethod
   def assign_user_to_location(self, user: Users, location: LocationEnum) -> None: pass