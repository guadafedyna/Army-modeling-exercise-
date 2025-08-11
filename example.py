from army import *

army1 = create_army('chinese')
army2 = create_army('english')

print("initial amount of coins \n army1:", army1['coins'],"\n army2:", army2['coins'],"\n")


print("training units from army 1 \n")
train(army1,1,10)
train(army1,1,5)
train(army1,0,1)


print("training units from army 2 \n")
train(army2,0,4)
train(army2,1,5)
train(army2,2,7)

print("trasforming units from army 2 \n")
transform(army2,0,3)
transform(army2,1,4)

print("asking units years alive \n units from army 1:", ask_years_alive(army1,1,5),"years alive", "\n units from army 2:", ask_years_alive(army2,1,4),"years alive \n")

print(battle(army1,army2),"\n")

print("verifying coins\n army1:",army1['coins'],"\n army2:",army2['coins'])


