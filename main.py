seconds_in_day = 24* 60 * 60
while True:
    input_seconds = int(input("Введіть час у секундах:"))
    if input_seconds <= 86400:
        break
    else:
        print("Час не може бути більшим за 86400 секунд")

remaining_seconds = seconds_in_day - input_seconds
remaining_hours = remaining_seconds // 3600
remaining_minutes = (remaining_seconds % 3600) // 60
remaining_seconds = remaining_seconds % 60

print(f"Залишилось до опівночі: {remaining_hours} годин, {remaining_minutes} хвилин, {remaining_seconds} секунд.")