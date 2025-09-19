from distance import Distance

d1 = Distance(10, 'm')
d2 = Distance(2, 'km')
d3 = Distance(500, 'cm')

print("Дистанции:")
print(d1)
print(d2)
print(d3)

result1 = d1 + d3
print(f"10m + 500cm = {result1}")

result2 = d1 + d2
print(f"10m + 2km = {result2}")

result3 = d2 - d1
print(f"2km - 10m = {result3}")

print(f"100m == 100km? {Distance(100, 'm') == Distance(100, 'km')}")
print(f"1000m == 1km? {Distance(1000, 'm') == Distance(1, 'km')}")

try:
    result4 = d1 - d2
except ValueError as e:
    print(f"Ошибка: {e}")