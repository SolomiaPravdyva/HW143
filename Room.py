class Room:
    def __init__(self, number=0, price=0, bookings=None, other=None):
        if isinstance(other, Room):
            self.number= other.number
            self.price= other.price
            self.bookings= list(other.bookings)
        else:
            self.number = number
            self.price = price
            if bookings:
                self.bookings = bookings
            else:
                self.bookings = []

    def is_free(self, start, end):
        for b in self.bookings:
            if not (end < b["start"] or start > b["end"]):
                return False
        return True
    def book(self, guest, start, end):
        self.bookings.append({
            "guest": guest,
            "start": start,
            "end": end
        })
    def income(self, start, end):
        total = 0
        for b in self.bookings:
            if not (b["end"] < start or b["start"] > end):
                total += self.price
        return total
    def __str__(self):
        return f"Room {self.number}, price={self.price}"