def week():
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        count = 0
        # print(len(days_of_week))
        while count <= len(days_of_week) - 1:
                yield days_of_week[count]
                count += 1
        raise StopIteration

days = week()

print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))

## A simpler solution
# def week():
#     days = [
#         "Monday",
#         "Tuesday",
#         "Wednesday",
#         "Thursday",
#         "Friday",
#         "Saturday",
#         "Sunday"
#     ]
#     for day in days:
#         yield day