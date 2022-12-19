class Student():
    university="Uek Krakow"
    id_number=100000
    def __init__(self,name,surname,field):
        self.name=name
        self.surname=surname
        self.id=Student.id_number
        self.field=field
        Student.id_number+=1
    def __str__(self):
        return f"{self.name} {self.surname},{self.id}, {self.field} ({Student.university})"

student1=Student("Anna","Maj","Applied Informatics")
student2=Student("Maria","Kowalska", "Applied Informatics")
student3=Student("Małgorzata","Kowalczyk","Marketing")
print(student1)
print(student2)
print(student3)