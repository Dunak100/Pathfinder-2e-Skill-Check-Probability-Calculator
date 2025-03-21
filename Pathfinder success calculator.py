import random

ac = float(input("AC: ")) 
hit = float(input("Hit Bonus: ")) 

hitChance =(21 + hit - ac)/20
missChance = 1 - hitChance

critHitChance = hitChance - 0.5
critMissChance = missChance - 0.5

normalHitChance = hitChance - critMissChance
normalMissChance = missChance - critHitChance

chances = [hitChance, missChance, critHitChance, normalHitChance, normalMissChance, critMissChance]
chances = [str(round(x*100, 2)) for x in chances]

print("Total chance to succeed: " + chances[0] + "%")
print("Total chance to fail: " + chances[1] + "%")
print("\n")
print("Chance to crit succeed: " + chances[2] + "%")
print("Chance to normal succeed: " + chances[3] + "%")
print("Chance to fail: " + chances[4] + "%")
print("Chance to crit fail: " + chances[5] + "%")
