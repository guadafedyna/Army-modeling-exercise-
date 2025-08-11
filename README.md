Army modeling exercise 

This exercise simulates armies of a certain civilization, they can be 'chinese', 'english' or 'byzantines'. 
Each army is representated by a dictionary that contains keys like: 
'civilization' is the type of civilization ( chinese, english or byzantines)
'coins' is the amount of coins that the army has available. the initial amount is 1000. they can be spent in training or transforming a unit, or can be earned if a battle is won.
'battle_history' is a list of dictionaries containing a history of the battles and their result. 
'units' is a list of 3 lists: [[pikemen],[archers],[knights]] each one representing a type of unit. 

Class Unit : 
represents a sigle combat unit in the army. 
a Unit has a type(pikeman,archer,knight), strength points and years alive. 
a Unit can be acceced specifically by using the key and index from its army disctionary.
ex. army_name['units'][unit_type][unit_id]  =  army_name['units][1][3]
methods: training(), training_cost(), transformation(), transformation_cost()

Years alive: 
training or transforming a unit increases its years alive. The years alive of a unit can be asked using ask_years_alive(army,unit_type,unit_id)

Battles: 
the army with the highest strength points wins the battle and earns 100 coins. 
the losing army loses its two units with the highest strength points.
in case of a TIE, both armies lose their units with the highest strength points. 
the results and opponents are always saved to their battle history. 

In order to maintain code clarity, I leave an example provided in the example.py file to visualize the development of the game.
