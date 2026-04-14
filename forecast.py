import random

conditions = ["Sunny", "Cloudy", "Rain", "Thunderstorm", "Windy"]

temp = random.randint(70, 100)
condition = random.choice(conditions)

print("Today's forecast:")
print(f"Condition: {condition}")
print(f"Temperature: {temp}°F")

