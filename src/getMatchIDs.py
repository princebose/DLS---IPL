import yaml
import pandas
df = pandas.read_csv("ipl.csv")

def getMatchID(n_input):
    i = df[df['Team1'] == n_input]
    j = df[df['Team2'] == n_input]

    ID1 = i.ID
    ID2 = j.ID
    ID3=[]


    for everyID in  ID1:
        ID3.append(everyID)
    for everyID in  ID2:
        ID3.append(everyID)

    for ID in ID3:
        path_in_str = "Data/" + str(ID) + ".yaml"
        with open(path_in_str, 'r') as f:
            data = yaml.load_all(f, Loader=yaml.FullLoader)
            for everyDoc in data:
                if 'winner' not in everyDoc['info']['outcome'].keys():
                    ID3.remove(ID)
    return (ID3)
print(getMatchID("KTK"))