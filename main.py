import requests
import random

sample = []
c = []
for i in range(3):
  CONTESTID = 1750
  r = requests.get(
    f'https://codeforces.com/api/contest.status?contestId={CONTESTID}&count=250'
  )

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
    if s not in c:
      sample.append(passed[s])
      c.append(s)
    else:
      i -= 1

print(sample)
#with open(f"fullsample.csv", "w") as f:
#  samplestr = str(sample).replace("'", '"')
#  res = f"contest-id,time,mem\n"
#  for i in range(len(sample)):
#    id = sample[i]
#    mem = file['result'][i]['memoryConsumedBytes']
#    time = file['result'][i]['timeConsumedMillis']
#    contest = file['result'][i]['contestId']
#    res += (f"{contest}-{id},{time},{mem}\n")
#  f.write(res)
