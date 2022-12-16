from interfaces import *
from sections import *
from students import Student

class SchoolManagement(IRegistrar, ISchoolRecords, ISectioning):
    
    def __init__(self) -> None:
        self.students: List[Student] = []
    def register_student(self, student: Student) -> None:
        self.students.append(student)
        
    def unregister_student(self, student: Student) -> None:
        self.students.remove(student)
    
    def assign_student_to_section(self, student: Student, section: SectionEnum) -> None:
        if section == SectionEnum.G1:
            student.set_section(SectionEnum.G1)
        elif section == SectionEnum.G2:
            student.set_section(SectionEnum.G2)
        
    def registered_students(self) -> str:
        
        res = ''
        for student in self.students:
            res = res + str(student) + ', '
        return res
        
        