import random
def commonLetters(asked, secret):
    return len(set(asked) & set(secret))

FILE = "sowpods.txt";

allWords = [line.upper().strip() for line in open(FILE)]

easyWords = [word for word in allWords if len(set(word)) == 4 and len(word) == 4]
medmWords = [word for word in allWords if len(set(word)) == 5 and len(word) == 5]
hardWords = [word for word in allWords if len(set(word)) == 6 and len(word) == 6]

PLAYING = True
while PLAYING:
    level = ""
    while level not in ["E", "M", "H"]:
        level = input("(E)asy, (M)edium, (H)ard? ").upper()
    if level == "E":
        words = easyWords[:]
    elif level == "M":
        words = medmWords[:]
    else:
        words = hardWords[:]
    WORD_NOT_FOUND = True
    while WORD_NOT_FOUND:
        if (len(words) == 0):
            print("\nI don't know that word :-(")
            print("Or .. you are cheating :-)\n")
            break
        guess = random.choice(words)
        print("I have to narrow down from", len(words))
        print("I am guessing: " + guess)
        response = input("Tell me how right I am ").upper()
        if response == "WIN":
            WORD_NOT_FOUND = False
        else:
            common = int(response)
            words = [w for w in words if commonLetters(guess, w) == common]
            if guess in words: words.remove(guess)
    PLAYING = input("\n\n Play Once  More? ").upper()[0] == "Y"
