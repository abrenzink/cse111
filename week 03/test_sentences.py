# test_sentences.py

from sentences import get_determiner, get_noun, get_verb
import random
import pytest

def test_get_determiner():

    # 1. Test the single determiners.
    single_determiners = ["a", "one", "the"]

    for _ in range(4):
        word = get_determiner(1)
        
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    for _ in range(4):
        quantity = random.randint(2, 5)
        word = get_determiner(quantity)
        

        assert word in plural_determiners

def test_get_noun():
    # 1. Test the single nouns.
    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):
        word = get_noun(1)
        
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):
        quantity = random.randint(2, 11)
        word = get_noun(quantity)

        assert word in plural_nouns

def test_get_verb():
   
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
        word = get_verb(1, "past")
        assert word in past_verbs

    present_singular_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):
        word = get_verb(1, "present")
        assert word in present_singular_verbs
    
    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    for _ in range(4):
        word = get_verb(5, "present")
        assert word in present_plural_verbs

    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(4):
        word = get_verb(5, "future")
        assert word in future_verbs
    

pytest.main(["-v", "--tb=line", "-rN", __file__])
