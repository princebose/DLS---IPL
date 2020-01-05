import yaml
import os
from pathlib import Path
from getMatchIDs import getMatchID
import json

def getAllData(team_name):
    matchlist = getMatchID(team_name)
    InningProgress = {}
    for ID in matchlist:

        path_in_str = "Data/"+str(ID)+".yaml"
        matches_per_team = []
        #seperate first and seconf innings data
        print(path_in_str)
        with open(path_in_str,'r') as f:
            data = yaml.load_all(f, Loader=yaml.FullLoader)
            for everyDoc in data:
                firstInningsData = everyDoc['innings'][0]['1st innings']['deliveries']
                firstInnTeam = everyDoc['innings'][0]['1st innings']['team']
                secInningsData = everyDoc['innings'][1]['2nd innings']['deliveries']
                secondInnTeam = everyDoc['innings'][1]['2nd innings']['team']
                if 'winner' not in everyDoc['info']['outcome'].keys():
                    actualWinner = 'tie'
                else:
                    actualWinner = everyDoc['info']['outcome']['winner']
        delivery = 0
        firstInnTotal = []
        wickets = 0
        firstInnDelivery = []
        secInnDelivery = []
        total = 0
        overno = 0
        ###Make a list of each delivery number in both innings
        for everyBall in firstInningsData:
            for key in everyBall.keys():
                firstInnDelivery.append(key)
        for everyBall in secInningsData:
            for key in everyBall.keys():
                secInnDelivery.append(key)

        wickets_1 = []
        print("\n\tFIRST INNINGS")
        for ballno in range(len(firstInnDelivery)):
            if ('wicket' in firstInningsData[ballno][firstInnDelivery[ballno]].keys()):
                print("Fall Of Wicket at ball no. ",firstInnDelivery[ballno])
                wickets += 1
            total += firstInningsData[ballno][firstInnDelivery[ballno]]['runs']['total']
            firstInnTotal.append(total)
            wickets_1.append(wickets)
        total = 0
        secInnTotal = []
        wickets_2 = []
        wickets = 0
        print("\n\tSECOND INNINGS")
        for ballno in range(len(secInnDelivery)):
            if ('wicket' in secInningsData[ballno][secInnDelivery[ballno]].keys()):
                print("Fall Of Wicket at ball no. ",secInnDelivery[ballno])
                wickets += 1
            total += secInningsData[ballno][secInnDelivery[ballno]]['runs']['total']
            secInnTotal.append(total)
            wickets_2.append(wickets)
        # print(secInnTotal)
        # print(total)
        scoreAfterEachOver_1 = [0 for _ in range(20)]
        scoreAfterEachOver_2 = [0 for _ in range(20)]
        wicketsAfterEachOver_1 = [0 for _ in range(20)]
        wicketsAfterEachOver_2 = [0 for _ in range(20)]
        overNo = 0

        for ballno in range(len(firstInnDelivery)):
            if ((firstInnDelivery[ballno]) < overNo+1):
                scoreAfterEachOver_1[overNo] = firstInnTotal[ballno]
                wicketsAfterEachOver_1[overNo] = wickets_1[ballno]
            else:
                overNo += 1

        overNo = 0

        for ballno in range(len(secInnDelivery)):
            if ((secInnDelivery[ballno]) < overNo+1):
                scoreAfterEachOver_2[overNo] = secInnTotal[ballno]
                wicketsAfterEachOver_2[overNo] = wickets_2[ballno]
            else:
                overNo += 1

        InningProgress.update({ID:{1:scoreAfterEachOver_1,2:wicketsAfterEachOver_1,3:scoreAfterEachOver_2,4:wicketsAfterEachOver_2,5:firstInnTeam,6:secondInnTeam,7:actualWinner}})
        # print(InningProgress)
    with open('InningsProgressionData_{}.txt'.format(team_name), 'w') as file:
        file.write(json.dumps(InningProgress))

#getAllData('DCaps')