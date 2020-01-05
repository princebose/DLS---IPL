import yaml
import os
import json
import io
from DLS import DLS_predict
from getMatchIDs import getMatchID
from getInningsScore import getAllData

file = "matchesPerTeam_json.txt"
with open(file,'r') as f:
    matches_per_team = json.load(f)
teamList = matches_per_team.keys()
teamwiseAccuracy = {}

for team_name in teamList:
    print("Team Name: ",team_name)
    getAllData(team_name)
    file = "InningsProgressionData_{}.txt".format(team_name)
    with open(file,'r') as f:
        innProgress = json.load(f)
    Accurate =0
    InAccurate = 0
    matchlist = getMatchID(team_name)
    for everyID in matchlist:

        final_score_1st_Inn = innProgress[str(everyID)]['1'][-1]
        wickets_each_over = innProgress[str(everyID)]['4']
        scores_each_over = innProgress[str(everyID)]['3']
        firstTeam = innProgress[str(everyID)]['5']
        secTeam = innProgress[str(everyID)]['6']
        ActualWinner = firstTeam = innProgress[str(everyID)]['7']
        if ActualWinner == 'tie':
            print("Outlier - Tied Match between ",firstTeam," vs ",secTeam)
        # print("WICKETS per over\n",wickets_each_over,"\nRUNS per over\n",scores_each_over)
        pred = []
        for i in range(len(innProgress[str(everyID)]['3'])):
            # print("OVER ",i+1)
            oversleft = 20-i
            wicketslost = wickets_each_over[i]
            scoreatInterrupt = scores_each_over[i]
            pred.append(DLS_predict(oversleft,wicketslost,scoreatInterrupt,final_score_1st_Inn))
        predFreq = {}
        for prediction in pred:
           predFreq[prediction] = pred.count(prediction)
        for key, value in predFreq.items():
           print("% r -> % d" % (key, value))
        print(predFreq)
        WinPercent = (float(predFreq[True])/float(predFreq[True]+predFreq[False]) )*100
        LossPercent = (float(predFreq[False])/float(predFreq[True]+predFreq[False]))*100
        print("Win = ",WinPercent,"%\tLoss = ",LossPercent,"%\n")
        predictionValue = [WinPercent,LossPercent]
        if WinPercent>LossPercent and secTeam ==  ActualWinner:
            print("Accurate")
            Accurate += 1
        elif LossPercent>WinPercent and firstTeam == ActualWinner:
            print("Accurate")
            Accurate += 1
        else:
            print("Not Accurate")
            InAccurate += 1
    Accuracy = 100 * float(Accurate /(InAccurate+Accurate))
    print("-------------------------------\n\nAccuracy of DLS is = ",Accuracy)
    teamwiseAccuracy.update({team_name:Accuracy})
print(teamwiseAccuracy)
