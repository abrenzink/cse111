import random

def main():
    
    quantity = 1
    tense = "past"
    print_sentence(quantity, tense)

    quantity = 1
    tense = "present"
    print_sentence(quantity, tense)

    quantity = 1
    tense = "future"
    print_sentence(quantity, tense)

    quantity = 2
    tense = "past"
    print_sentence(quantity, tense)

    quantity = 2
    tense = "present"
    print_sentence(quantity, tense)

    quantity = 4
    tense = "future"
    print_sentence(quantity, tense)



def get_determiner(quantity):
   
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    word = random.choice(words)
    return word

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

def get_preposition():
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    word = random.choice(words)
    return word  

def get_prepositional_phrase():

    quantity = random.randint(1,2)

    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    space = " "

    prepositional_phrase = preposition + space + determiner + space + noun

    return prepositional_phrase

def print_sentence(quantity, tense):

    print("")
    print(f"---------------------Sentence-----------------------")
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prep_phrase1 = get_prepositional_phrase()
    prep_phrase2 = get_prepositional_phrase()
    print(f"{determiner.capitalize()} {noun} {prep_phrase1} {verb} {prep_phrase2}")
    print("----------------------------------------------------")
    print("")

main()