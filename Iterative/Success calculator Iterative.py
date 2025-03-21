dc = float(input("DC: ")) 
bonus = float(input("Skill bonus: ")) 

CritSuccess, Success, Failure, CritFailure = 0, 0, 0, 0
CS, S, F, CF = 0, 1, 2, 3
occurance = [CritSuccess, Success, Failure, CritFailure]


for roll in range (1, 21):
    if roll + bonus >= dc + 10:
        if roll == 1:
            occurance[S] += 1 
        else:
            occurance[CS] += 1

    elif roll + bonus >= dc and roll + bonus < dc + 10:
        if roll == 20:
            occurance[CS] += 1 
        elif roll == 1:
            occurance[F] += 1 
        else:
            occurance[S] += 1

    elif roll + bonus <= dc and roll + bonus > dc - 10:
        if roll == 20:
            occurance[S] += 1 
        elif roll == 1:
            occurance[CF] += 1 
        else:
            occurance[F] += 1

    elif roll + bonus <= dc - 10:
        if roll == 20:
            occurance[F] += 1 
        else:
            occurance[CF] += 1


TotalSuccess = occurance[CS] + occurance[S]
TotalFailure = occurance[CF] + occurance[F]
TotalStats = [TotalSuccess, TotalFailure]
occurance.extend(TotalStats)

probabilites = [(x/20)*100 for x in occurance]



if probabilites[4] == 100:
    lowestSuccessfulRoll = "Always success" 
elif probabilites[5] == 100:
    lowestSuccessfulRoll = "Always failure" 
else:
    lowestSuccessfulRoll = int(dc - bonus)


print(f"Total chance to succeed: {probabilites[4]}% (Lowest successful roll: {lowestSuccessfulRoll})")
print(f"Total chance to fail: {probabilites[5]}%")
print("\n", end = "")
print(f"Chance to crit succeed: {probabilites[0]}%")
print(f"Chance to normal succeed: {probabilites[1]}%")
print(f"Chance to fail: {probabilites[2]}%")
print(f"Chance to crit fail: {probabilites[3]}%")

