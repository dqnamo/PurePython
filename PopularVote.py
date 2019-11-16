numberTestCases = input("How many testcases: ")

for testcases in range(numberTestCases):
    numberCanditates = input("How many canditates: ")

    votes = []
    popular = []
    total = 0
    highest = 0
    winner = 0

    for canditates in range(numberCanditates):
        votes.append(input("How many votes: "))

    for vote in votes:
        total += vote

    for x in range(len(votes)):
        if votes[x] > total/2:
            print("Majority Winner Canditate {}").format(x+1)
            winner = votes[x]
        elif votes[x] >= highest:
            highest = votes[x]
            popular.append(x)

    if len(popular) == 1:
        print("Minority Winner Canditate {}").format(popular[0] + 1)
    elif len(popular) > 1 and winner == 0:
        print("No Winner")
