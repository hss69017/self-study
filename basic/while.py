customer = "Tor"
index = 5
while index >= 1 :
    print("{0}, your coffee is ready. There's(re) {1} time(s) left.".format(customer, index))
    index -= 1
    if index == 0 :
        print("Your coffee is thrown away.")

# customer = "Ironman"
# index = 1
# while True :
#     print("{0}, your coffee is ready. I called you {1} time(s).".format(customer, index))
#     index += 1

customer = "Tor"
person = "Unknown"
while person != customer :
    print("{0}, your coffee is ready.".format(customer))
    person = input("What's your name? ")