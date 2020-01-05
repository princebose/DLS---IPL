import yaml
from DLS import DLS_predict
import json

teamNames = {'Chennai Super Kings':'CSK','Delhi Capitals':'DCaps','Royal Challengers Bangalore':'RCB', 'Deccan Chargers':'DC', 'Delhi Daredevils':'DD','Kings XI Punjab':'KXIP', 'Kolkata Knight Riders':'KKR','Rajasthan Royals':'RR','Mumbai Indians':'MI','Sunrisers Hyderabad':'SRH','Gujarat Lions':'GL','Rising Pune Supergiant':'RPS','Rising Pune Supergiants':'RPS', 'Pune Warriors':'PW','Kochi Tuskers Kerala':'KTK'}
def getTeamNames(arr):
    tempL = []
    for every in arr:
        tempL.append(teamNames[every])
    return tempL

import os
from pathlib import Path

pathlist = Path('Data').glob('**/*.yaml')
matches_per_team = []
for path in pathlist:
    path_in_str = str(path)
    with open(path_in_str,'r') as f:
        data = yaml.load_all(f, Loader=yaml.FullLoader)
        for everyDoc in data:
            t_info = everyDoc['info']['teams']
            teams = getTeamNames(t_info)
            matches_per_team.append(teams[0])
            matches_per_team.append(teams[1])
    print(path_in_str)
finalDict = {i:matches_per_team.count(i) for i in set(matches_per_team)}
with open('matchesPerTeam_json.txt', 'w') as file:
     file.write(json.dumps(finalDict))
