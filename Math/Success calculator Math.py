dc = float(input("DC: ")) 
bonus = float(input("Skill bonus: ")) 

SuccessChance = max((21 + bonus - dc)/20, 0)
FailureChance = max(1 - SuccessChance, 0)

critSuccessChance = max(SuccessChance - 0.5, 0)
critFailureChance = max(FailureChance - 0.5, 0)

normalSuccessChance = max(SuccessChance - critSuccessChance, 0)
normalFailureChance = max(FailureChance - critFailureChance, 0)

probabilites = [SuccessChance, FailureChance, critSuccessChance, normalSuccessChance, normalFailureChance, critFailureChance]
probabilites = [str(round(min(max(x, 0), 1)*100, 2)) for x in probabilites]

print("Total chance to succeed: " + probabilites[0] + "%")
print("Total chance to fail: " + probabilites[1] + "%")
print("\n")
print("Chance to crit succeed: " + probabilites[2] + "%")
print("Chance to normal succeed: " + probabilites[3] + "%")
print("Chance to fail: " + probabilites[4] + "%")
print("Chance to crit fail: " + probabilites[5] + "%")

