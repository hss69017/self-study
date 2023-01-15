weather = input("How's the weather today? ")
if weather == "rain" or weather == "snow":
    print("Take your umbrella.")
elif weather == "fine dust":
    print("Take your mask.")
else:
    print("You don't need to take anything.")

temp = int(input("What's the temperature? "))
if 30 <= temp:
    print("It's too hot. Don't go outside.")
elif 10 <= temp and temp < 30:
    print("It's nice weather.")
elif 0 <= temp < 10:
    print("Take your coat.")
else:
    print("It's too cold. Don't go ouside.")