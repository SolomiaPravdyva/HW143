from Hotel import Hotel
from Guest import Guest

hotel = Hotel()
hotel.read_file("data.txt")
g = Guest("Ivan", "2026-04-01", "2026-04-05", 3000)
room = hotel.check_in(g, g.start_date, g.end_date)
if room:
    print("Кімната:", room)
else:
    print("Немає вільної кімнати")

print("Вільні кімнати:", hotel.free_rooms_count("2026-04-02"))
free_room = hotel.find_free_room("2026-04-10", "2026-04-12")
if free_room:
    print("Пошук кімнати:", free_room.number)
else:
    print("Пошук кімнати: немає")

print("Прибуток:", hotel.hotel_income("2026-04-01", "2026-04-30"))
guests = hotel.find_guest("Ivan", "2026-04-01", "2026-04-30")

print("Пошук гостя:")
if guests:
    for g in guests:
        print("Кімната:", g[0],
              "Ім'я:", g[1],
              "з:", g[2],
              "по:", g[3])
else:
    print("Гостя не знайдено")