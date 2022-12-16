from sections import *

class Person:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

class Student(Person):
    def __init__(self, id: int, name: str) -> None:
        super().__init__(id, name)
        self.section: SectionEnum = None
        
    def set_section(self, section: SectionEnum) -> None:
        self.section = section
    
    def __str__(self) -> str:
        if self.section:
            return f'{self.id}.) {self.name} ({self.section.name})'
        return f'{self.id}.) {self.name}'
        