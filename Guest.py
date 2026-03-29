class Guest:
    def __init__(self, name="", start_date="", end_date="", budget=0, other=None):
        if isinstance(other, Guest):
            self.name=other.name
            self.start_date=other.start_date
            self.end_date= other.end_date
            self.budget= other.budget
        else:
            self.name=name
            self.start_date=start_date
            self.end_date= end_date
            self.budget=budget
    def read_line(self, line):
        name, start, end, budget = line.strip().split(",")
        self.name= name
        self.start_date= start
        self.end_date= end
        self.budget= int(budget)
    def __str__(self):
        return f"{self.name} ({self.start_date} - {self.end_date}), budget={self.budget}"