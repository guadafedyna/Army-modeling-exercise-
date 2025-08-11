

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
    unit = army['units '][unit_type][unit_id]
    years_alive = unit.years_alive
    return years_alive

def strength_points(army: dict):
    points = 0

    for types in army['units']:
        for unit in types:
            points += unit.strength
    return points 

def lose_unit(army:dict):
    highest = army['units'][0][0]
    highest_type = 0
    highest_unit = 0

    for t in range(len(army['units'])):
        for u in range(len(army['units'][t])):
            if army['units'][t][u].strength > highest.strength:
                highest = army['units'][t][u]
                highest_type = t 
                highest_unit = u 

    del army['units'][highest_type][highest_unit]



def battle(army1: dict, army2: dict):

    points1 = strength_points(army1)
    points2 = strength_points(army2)

    name1 = army1['civilization']
    name2 = army2['civilization']

    if points1 > points2:
        wallet(army1,100)
        history1 = {'opponent': name2, 'result': 'winner'}
        army1['battle_history'].append(history1)
        print("¡army 1 is the winner!")

        history2 = {'opponent': name1, 'result':'loser'}
        army2['battle_history'].append(history2)
        lose_unit(army2)
        lose_unit(army2)

    elif points2 > points1:
        wallet(army2,100)
        history2 = {'opponent': name1, 'result':'winner'}
        army2['battle_history'].append(history2)
        print("¡army 2 is the winner!")

        lose_unit(army1)
        lose_unit(army1)

        history1= {'opponent': name2,'result':'loser'}
        army1['battle_history'].append(history1)

    elif points1 == points2:
        lose_unit(army1)
        lose_unit(army2)
        print("it's a tie")

        history1 = {'opponent': name2,'result': 'tie'}
        army1['battle_history'].append(history1)

        history2 = {'opponent': name1, 'result':'tie'}
        army2['battle_history'].append(history2)


        




    
 
