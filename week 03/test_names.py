from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Andrea","Brenzink") == "Brenzink;Andrea"
    assert make_full_name("Tiago","Ferreira") == "Ferreira;Tiago"
    assert make_full_name("Abc","Def") == "Def;Abc"
    assert make_full_name("","") == ";"

def test_extract_family_name():
    assert extract_family_name("Brenzink; Andrea") == "Brenzink"
    assert extract_family_name("Ferreira; Tiago") == "Ferreira"
    assert extract_family_name("Def; Abc") == "Def"
    assert extract_family_name("; ") == ""


def test_extract_given_name():
    assert extract_given_name("Brenzink; Andrea") == "Andrea"
    assert extract_given_name("Ferreira; Tiago") == "Tiago"
    assert extract_given_name("Def; Abc") == "Abc"
    assert extract_given_name("; ") == ""

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])