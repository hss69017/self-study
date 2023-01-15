#가변인자(*args)

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("name: {0}\tage: {1}\t".format(name, age), end=" ")
#     # print에 end를 사용하면 print가 끝날 때 줄바꿈을 하지 않고, end를 출력하고 그대로 이어서 실행됨
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("name: {0}\tage: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("a", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("b", 25, "Kotlin", "Swift")