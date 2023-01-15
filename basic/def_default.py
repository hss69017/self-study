# def profile(name, age, main_lang):
#     print("name: {0}\tage: {1}\tmain programming language: {2}".format(name, age, main_lang))
# profile("a", 20, "python")
# profile("b", 25, "java")

def profile(name, age=17, main_lang="python"):
    print("name: {0}\tage: {1}\tmain programming language: {2}".format(name, age, main_lang))
profile("a")
profile("b")
