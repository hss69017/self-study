def std_weight(height, gender):
    if gender == "man":
        standardweight = round(height * height * 22, 2)
        print("You are a {0} and your height is {1}m. Your standard weight is {2}kg.".format(gender, height, standardweight))
    elif gender == "woman":
        standardweight = round(height * height * 21, 2)
        print("You are a {0} and your height is {1}m. Your standard weight is {2}kg.".format(gender, height, standardweight))
    else:
        print("You typed the wrong gender.")

std_weight(1.77, "man")

#I can use "return" in definition. However, if I use "return", then the definition is done immediately.