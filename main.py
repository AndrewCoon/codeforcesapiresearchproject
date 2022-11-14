import requests
import random

sample = []
c = []
CONTESTID = [1750, 1747, 1754]

for i in range(len(CONTESTID)):
  c = []
  r = requests.get(
    f'https://codeforces.com/api/contest.status?contestId={CONTESTID[i]}')

  file = r.json()

  passed = []
  j = 0
  while len(passed) < 249:
    print(f'loggin passed submission iteration: {j}')
    id = file['result'][j]['id']
    mem = file['result'][j]['memoryConsumedBytes']
    time = file['result'][j]['timeConsumedMillis']
    contest = file['result'][j]['contestId']
    j += 1
    temp = {"id": id, "mem": mem, "time": time, "contestId": contest}
    if (file['result'][j]['verdict'] == 'OK'):
      passed.append(temp)
  passedstr = ""
  with open(f"{CONTESTID[i]}-passed.csv", "w") as f:
    passedstr = str(passed).replace("'", '"')
    res = f"contest-id,time,mem\n"
    for j in range(len(passed)):
      id = file['result'][j]['id']
      mem = file['result'][j]['memoryConsumedBytes']
      time = file['result'][j]['timeConsumedMillis']
      contest = file['result'][j]['contestId']
      res += (f"{contest}-{id},{time},{mem}\n")
    f.write(res)

  while len(sample) < 149 * (i + 1):
    s = random.randint(0, len(passed) - 1)
    if s not in c:
      sample.append(passed[s])
      c.append(s)

print(sample)
with open(f"fullsample.csv", "w") as f:
  samplestr = str(sample).replace("'", '"')
  res = f"contest-id,time,mem\n"
  for i in range(len(sample)):
    id = sample[i]['id']
    mem = sample[i]['mem']
    time = sample[i]['time']
    contest = sample[i]['contestId']
    res += (f"{contest}-{id},{time},{mem}\n")
  f.write(res)
