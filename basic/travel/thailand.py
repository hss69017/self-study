class ThailandPackage:
    def detail(self):
        print("[Thailand Package 3 Nights 5 Days] Bangkok, Pataya Travel (Night Market Tour) $500")

if __name__ == "__main__": # If I execute this file directly, this will be executed.
    print("Execute the module 'Thailand' directly.")
    print("This sentence is printed only when you execute the module directly.")
    trip_to = ThailandPackage()
    trip_to.detail()
else: # if I called this module from outside, this will be executed.
    print("The module is called from outside.")