days = ["Thursday", "Friday", "Saturday",
        "Sunday", "Monday", "Tuesday", "Wednesday",]
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

current_date, current_month = [int(x) for x in input().split()]
for i in range(current_month):
    current_date += months[i]

total_days = current_date

print(days[(total_days-1) % 7], end=" ")
