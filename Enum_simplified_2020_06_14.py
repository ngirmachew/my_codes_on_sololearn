from enum import Enum
class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

print(Weekday.MONDAY)
print(Weekday.TUESDAY)
print(Weekday.WEDNESDAY)
print(Weekday.THURSDAY)
print(Weekday.FRIDAY)
print(Weekday.SATURDAY)
print(Weekday.SUNDAY)
print(Weekday(0))
print(Weekday(1))
print(Weekday(2))
print(Weekday(3))
print(Weekday(4))
print(Weekday(5))
print(Weekday(6))

for day in Weekday:
  print(f"'{day.name}'\t{day.value}")