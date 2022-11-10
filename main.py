import requests
import random
CONTESTID = 1750
r = requests.get(f'https://codeforces.com/api/contest.status?contestId={CONTESTID}&count=250')
file = r.json()

passed = []
for i in range(len(file['result'])):
    id = file['result'][i]['id']
    mem = file['result'][i]['memoryConsumedBytes']
    time = file['result'][i]['timeConsumedMillis']
    contest = file['result'][i]['contestId']

    temp = {
        "id": id,
        "mem": mem,
        "time": time,
        "contestId": contest
    }
    if(file['result'][i]['verdict'] == 'OK'):
        passed.append(temp)

with open(f"contest-{CONTESTID}.json", "w") as f:
    f.write(str(passed).replace("'", '"'))