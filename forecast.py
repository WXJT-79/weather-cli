import random

conditions = ["Sunny", "Cloudy", "Rain", "Thunderstorm", "Windy"]

temp = random.randint(70, 100)
condition = random.choice(conditions)

print("Branch version forecast:")
print(f"Condition: {condition}")
print(f"Temperature: {temp}°F")

humidity = random.randint(40, 100)
print(f"Humidity: {humidity}%")
