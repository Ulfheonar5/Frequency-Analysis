letters = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0,
    "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
    "k": 0, "l": 0, "m": 0, "n": 0, "o": 0,
    "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
    "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
}


def isletter(character):
    if len(character) == 1:
        if (97 <= ord(character) <= 122) or (65 <= ord(character) <= 90):
            print("Yes,It is a letter.")
    else:
        print("Invalid input,Please enter a letter!")


def uppertolower(character):
    if len(character) == 1:
        if 65 <= ord(character) <= 90:
            character = chr(32 + ord(character))
            return character
    else:
        print("Invalid input,Please enter a letter!")


def info():
    print("""
    Name: Mert Töke
    Student Number: 211220041
    Note: Anni, amori e bicchieri di vino, non si contano mai...
    Yıllar, aşklar ve kadehlerce şarap; bunlar asla sayılmaması gereken şeylerdir...""")


def reset():
    global letters
    for letter in letters:
        letters[letter] = 0


def frequency_analysis(article_copy, part):
    global letters
    reset()

    for letter in article_copy[0:part:1]:
        if letter in letters.keys():
            letters[letter] += 1
    for letter, count in letters.items():
        if count != 0:
            print(f"{letter}: number of using: {count}, using rate: {(count / part) * 100:.2f}%")
