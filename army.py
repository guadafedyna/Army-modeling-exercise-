

class Unit:
    def __init__(self, type, strength, years_alive):
        self.type = type
        self.strength = strength
        self.years_alive = years_alive

    def __repr__(self):
        return f'Unit type = {self.type}, strength= {self.strength}, years_alive={self.years_alive}'
    
    def training(self):
        if self.type == "pikeman":
            self.years_alive += 1
            benefit = 3
        
        elif self.type == "archer":
            self.years_alive += 2
            benefit = 7
        
        elif self.type == "knight":
            self.years_alive += 5
            benefit = 10
        
        else:
            benefit = 0

        self.strength += benefit 

    
    def training_cost(self):
        if self.type == "pikeman":
            cost = 10
        elif self.type == "archer":
            cost = 20
        elif self.type == "knight" :
            cost= 30
        else:
            cost = 0
        return cost 
    
    def transformation(self):
        if self.type == "pikeman":
            self.type = "archer"
            self.strength = 10
            self.years_alive += 5
        
        elif self.type == "archer":
            self.type = "knight" 
            self.strength = 20
            self.years_alive += 5

    
    def transformation_cost(self):
        if self.type == "pikeman":
            t_cost = 30
        elif self.type == "archer":
            t_cost = 40 
        else :
            t_cost = 0
        return t_cost
    



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

    number_pikemen = initial_units[civilization]['pikemen']
    number_archers = initial_units[civilization]['archers']
    number_knights = initial_units[civilization]['knights']

    for i in range(number_pikemen):
        pikemen.append(Unit(type = 'pikeman', strength =5, years_alive=0))

    for j in range(number_archers):
        archers.append(Unit(type = 'archer', strength =10, years_alive=1))

    for k in range(number_knights):
        knights.append(Unit(type = 'knight', strength = 20, years_alive=2))

    army['civilization'] = civilization
    army['coins'] = 1000
    army['battle_history'] = []
    army['units'] = [pikemen,archers,knights]

    return army 


def train(army:dict, unit_type: int, unit_id: int):
    unit = army['units'][unit_type][unit_id]
    cost = unit.training_cost()

    if army['coins'] >= cost :
        unit.training()
        wallet(army,-cost)

    else:
        print("not enough coins")


def transform(army:dict, unit_type:int, unit_id: int):
    unit = army['units'][unit_type][unit_id]
    transf_cost = unit.transformation_cost()

    if army['coins'] >= transf_cost:
        unit.transformation()
        wallet(army,-transf_cost)
    
    else:
        print("not enough coins")


def wallet(army:dict, amount: int):
    army['coins'] += amount 


def ask_years_alive(army:dict, unit_type:int, unit_id:int):
    unit = army['units ']
 
