import random

def main():
  
    print("-----------Sentence 01-------------")
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "past")
    print(f"{determiner} {noun} {verb}")
    print("-----------------------------------")
    print("")
    print("")
    print("-----------Sentence 02-------------")
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "present")
    print(f"{determiner} {noun} {verb}")
    print("-----------------------------------")
    print("")
    print("")
    print("-----------Sentence 03-------------")
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "future")
    print(f"{determiner} {noun} {verb}")
    print("-----------------------------------")
    print("")
    print("")
    print("-----------Sentence 04-------------")
    determiner = get_determiner(2)
    noun = get_noun(2)
    verb = get_verb(2, "past")
    print(f"{determiner} {noun} {verb}")
    print("-----------------------------------")
    print("")
    print("")
    print("-----------Sentence 05-------------")
    determiner = get_determiner(2)
    noun = get_noun(2)
    verb = get_verb(2, "present")
    print(f"{determiner} {noun} {verb}")
    print("-----------------------------------")
    print("")
    print("")
    print("-----------Sentence 06-------------")
    determiner = get_determiner(2)
    noun = get_noun(2)
    verb = get_verb(2, "future")
    print(f"{determiner} {noun} {verb}")
    print("-----------------------------------")


def get_determiner(quantity):
   
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    word = random.choice(words)
    cap_word = word.capitalize()
    return cap_word

def get_noun(quantity):
  
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    word = random.choice(words)
    return word

main()