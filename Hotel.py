from Guest import Guest
from Room import Room

class Hotel:
    def __init__(self):
        self.rooms = []
    def read_file(self, filename):
        with open(filename, "r") as f:
            for line in f:
                data=line.strip().split(",")
                if data[0]=="ROOM":
                    self.rooms.append(Room(int(data[1]), int(data[2])))
                elif data[0]=="GUEST":
                    g=Guest()
                    g.name=data[1]
                    g.start_date=data[2]
                    g.end_date=data[3]
                    g.budget=int(data[4])
                    room_number=int(data[5])
                    for r in self.rooms:
                        if r.number== room_number:
                            r.book(g, g.start_date, g.end_date)
    def free_rooms_count(self, date):
        count=0
        for r in self.rooms:
            if r.is_free(date, date):
                count+= 1
        return count
    def find_free_room(self, start, end):
        for r in self.rooms:
            if r.is_free(start, end):
                return r
        return None
    def check_in(self, guest, start, end):
        room = self.find_free_room(start, end)
        if room:
            room.book(guest, start, end)
            return room.number
        return None
    def cost_of_stay(self, room):
        return room.price
    def hotel_income(self, start, end):
        total=0
        for r in self.rooms:
            total= total + r.income(start, end)
        return total
    def find_guest(self, name, start, end):
        result=[]
        for r in self.rooms:
            for b in r.bookings:
                if b["guest"].name == name:
                    if not (b["end"] < start or b["start"] > end):
                        result.append((r.number, b["guest"].name, b["start"], b["end"]))
        return result