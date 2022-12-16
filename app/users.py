from location import *

class Person:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

class Users(Person):
    def __init__(self, id: int, name: str) -> None:
        super().__init__(id, name)
        self.location: LocationEnum = None
        
    def set_section(self, location: LocationEnum) -> None:
        self.location = location
    
    def __str__(self) -> str:
        if self.location:
            return f'{self.id}.) {self.name} ({self.location.name})'
        return f'{self.id}.) {self.name}'
        