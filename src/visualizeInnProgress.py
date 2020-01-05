from matplotlib import pyplot as plt
import json

file = "InningsProgressionData.txt"
with open(file,'r') as f:
    data = json.load(f)
print(data)

overs = [i for i in range(20)]
runs_1 = data['1']
wickets_1 = data['2']
runs_2 = data['3']
wickets_2 = data['4']
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(overs,runs_1,color = 'green',linestyle='dashdot',label = 'RUNS' )
plt.plot(overs,wickets_1,color = 'red',linestyle='dotted',label='WICKETS' )
plt.title("1st Innings")
plt.legend()

plt.subplot(2,1,2)
plt.plot(overs,runs_2,color = 'green',linestyle='dashdot',label = 'RUNS' )
plt.plot(overs,wickets_2,color = 'red',linestyle='dotted',label='WICKETS' )
plt.title("2nd Innings")
plt.legend()
plt.show()
