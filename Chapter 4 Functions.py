def greet(lang):
    if lang == "English":
        print("Hello!")
    elif lang == "Spanish":
        print("Hola!")
    elif lang == "French":
        print("Bonjour!")

lang = input("Enter language:")
greet(lang)


