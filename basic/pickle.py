# import pickle
# # profile_file = open("profile.pickle", "wb") #When I use "pickle", I should use binary type(b), which means "wb", I don't need "encoding."
# # profile = {"name": "a", "age": 30, "hobby": ["soccer", "golf", "coding"]}
# # print(profile)
# # pickle.dump(profile, profile_file) #The information in profile is saved in "profile.pickle".
# # profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #The information in "profile.pickle" is called to profile.
# print(profile)
# profile_file.close()