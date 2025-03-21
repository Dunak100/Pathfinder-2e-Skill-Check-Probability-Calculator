ac = float(input("DC: ")) 
hit = float(input("Skil bonus: ")) 

hitChance = max((21 + hit - ac)/20, 0)
missChance = max(1 - hitChance, 0)

critHitChance = max(hitChance - 0.5, 0)
critMissChance = max(missChance - 0.5, 0)

normalHitChance = max(hitChance - critHitChance, 0)
normalMissChance = max(missChance - critMissChance, 0)

chances = [hitChance, missChance, critHitChance, normalHitChance, normalMissChance, critMissChance]
chances = [str(round(min(max(x, 0), 1)*100, 2)) for x in chances]

print("Total chance to succeed: " + chances[0] + "%")
print("Total chance to fail: " + chances[1] + "%")
print("\n")
print("Chance to crit succeed: " + chances[2] + "%")
print("Chance to normal succeed: " + chances[3] + "%")
print("Chance to fail: " + chances[4] + "%")
print("Chance to crit fail: " + chances[5] + "%")

