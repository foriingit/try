class OOP:
    def __init__(self, grade, date, name, group, subject):
        self.subject=subject
        self.grade=grade
        self.date=date
        self.name=name
        self.group=group

    def Diary(self):
        self.grade
    def Student(self):
        return self.name
    def Subject(self):
        return self.subject
op=OOP(grade='5', date='14/12/3', name='Aaar', group='class1', subject='asdas')
print(op.Subject())
