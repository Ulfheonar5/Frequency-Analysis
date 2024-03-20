import module

while True:
    selection = input("""
Select 1 for frequency analysis,
Select 2 for letter control,
Select 3 for uppercase to lower case,
Select 4 for information about me,
Select 5 for quit:""")
    if selection == "1":

        con1, con2, con3 = 100, 1000, 10000
        article = input("Enter the article(max 10000 words):")
        length = len(article)
        if length > 10000:
            print("The article has more than 10000 words!")
            continue
        elif 0 < length <= 100:
            con1 = con2 = con3 = length
        elif 100 < length <= 1000:
            con2 = con3 = length
        print("--------------------------------------------")
        print("             First 100 words                ")
        print("--------------------------------------------")
        module.frequency_analysis(article.lower(), con1)
        print("--------------------------------------------")
        print("            First 1000 words                ")
        print("--------------------------------------------")
        module.frequency_analysis(article.lower(), con2)
        print("--------------------------------------------")
        print("           First 10000 words                ")
        print("--------------------------------------------")
        module.frequency_analysis(article.lower(), con3)
        print("--------------------------------------------")
        print("--------------------------------------------")

    elif selection == "2":
        letter = input("Enter the letter:")
        module.isletter(letter)
    elif selection == "3":
        character = input("Enter the character:")
        module.uppertolower(character)
    elif selection == "4":
        module.info()
    elif selection == "5":
        break
    else:
        print("Please enter a valid selection!")
