import requests
import random

CONTESTID = 1750
r = requests.get(
  f'https://codeforces.com/api/contest.status?contestId={CONTESTID}&count=250')
file = r.json()

passed = []
i = 0
while len(passed) < 249:
  id = file['result'][i]['id']
  mem = file['result'][i]['memoryConsumedBytes']
  time = file['result'][i]['timeConsumedMillis']
  contest = file['result'][i]['contestId']
  i = +1
  temp = {"id": id, "mem": mem, "time": time, "contestId": contest}
  if (file['result'][i]['verdict'] == 'OK'):
    passed.append(temp)
passedstr = ""
with open(f"{CONTESTID}-passed.csv", "w") as f:
  passedstr = str(passed).replace("'", '"')
  res = f"contest-id,time,mem\n"
  for i in range(len(passed)):
    id = file['result'][i]['id']
    mem = file['result'][i]['memoryConsumedBytes']
    time = file['result'][i]['timeConsumedMillis']
    contest = file['result'][i]['contestId']
    res += (f"{contest}-{id},{time},{mem}\n")
  f.write(res)

for i in range(149):
  s = random.randint(0, 147)
  passed[i]
