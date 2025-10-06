import pytest
from fctListes import points
@pytest.mark.parametrize("vie,defense,attaque,resultat_attendu",[
    ("100","38","30","108"),
    ("350","105","145","410"),
    ("195","100","185","110"),
    ("67","38","29","76")
])

def test_points(vie,defense,attaque,resultat_attendu):
    #Act
    resultat = points(vie,defense,attaque,)
    #Assert
    assert resultat ==  resultat_attendu