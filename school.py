class School():
    def __init__(self, name = None, roster = {}):
        self.name = name
        self.roster = roster
    def add_student(self,student_name, grade):
        self.roster.setdefault(grade,[]).append(student_name)
       # self.roster[grade].append(student_name)
        
    def grade(self, grade):
        return self.roster[grade]
    
    def sort_roster(self):
        roster_sorted = {x:sorted(self.roster[x]) for x in self.roster.keys()}
        return roster_sorted
        
