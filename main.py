from art import text

alphabets = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
             'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
             'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
             's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
             'y': '-.--', 'z': '--..', ' ': '/', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
             'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
             'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
             'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
             'Y': '-.--', 'Z': '--..'}


# for getting key from dictionary using value
def key(val):
    for key, value in alphabets.items():
        if value == val:
            return key
    return "Key not found"


def to_morse():
    global start
    text = (input("What is your message? ")).lower()
    text_words = []
    for char in text:
        result = alphabets.get(char)
        text_words.append(result)

    morse = " ".join(text_words)
    print(morse)
    res = (input("Do you want to Continue?Yes/No ")).lower()
    if res == 'yes':
        start = True
    else:
        start = False
        print("Good Bye")


def to_word():
    global start
    code = input("What is your message? ")
    code_list = code.split(' ')
    code_words = []
    for _ in code_list:
        result = key(_)
        code_words.append(result)
        text = ''.join(code_words)
    print(text)
    res = (input("Do you want to Continue?Yes/No ")).lower()
    if res == 'yes':
        start = True
    else:
        start = False
        print("Good Bye")


start = True
print(text)
while start:
    response = input("For conversion from morse code to text press 'to text'\n"
                     "For conversion from text to morse code, press 'to morse'\n ")
    if response == 'to text':
        to_word()
    elif response == 'to morse':
        to_morse()
    else:
        print("Please Type Correctly!")
