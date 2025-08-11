initial_units = {
    'chinese': {'pikemen':2,'archers':25,'knights':2},
    'english':{'pikemen':10,'archers':10,'knights':10},
    'byzantines':{'pikemen':5,'archers':8,'knights':15},
}


def create_army(civilization: str) -> dict:
    army = {}
    pikemen = []
    archers = []
    knights = []

    number_pikemen = initial_units

