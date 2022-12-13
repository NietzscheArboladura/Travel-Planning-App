from abc import ABC, abstractmethod
from students import Student
from sections import *
from typing import List

class IRegistrar(ABC):
    
    @abstractmethod
    def register_student(self, student: Student) -> None: pass
    
    @abstractmethod
    def unregister_student(self, student: Student) -> None: pass

class ISchoolRecords(ABC):
    @abstractmethod
    def registered_students(self) -> List: pass

        
class ISectioning(ABC):
   @abstractmethod
   def assign_student_to_section(self, student: Student, section: SectionEnum) -> None: pass