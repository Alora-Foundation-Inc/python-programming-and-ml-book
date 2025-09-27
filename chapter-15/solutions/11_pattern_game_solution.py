import numpy as np

seqs = [
    {"name":"Even Numbers",    "data":[2,4,6,8,np.nan],   "rule":"+2 each time"},
    {"name":"Perfect Squares", "data":[1,4,9,16,np.nan],  "rule":"n^2 (1,4,9,16,25,...)"},
    {"name":"Fibonacci",       "data":[1,1,2,3,5,np.nan], "rule":"next = sum of last two"},
    {"name":"Subtract Three",  "data":[10,7,4,1,np.nan],  "rule":"-3 each time"},
]

score = 0
for s in seqs:
    known = [v for v in s["data"] if not np.isnan(v)]
    if s["name"]=="Even Numbers":
        answer = known[-1] + 2
    elif s["name"]=="Perfect Squares":
        n = int(np.sqrt(known[-1])) + 1
        answer = n*n
    elif s["name"]=="Fibonacci":
        answer = known[-1] + known[-2]
    else:
        answer = known[-1] - 3

    print(f"{s['name']} — Next number should be {answer}. ({s['rule']})")
    score += 1

print(f"Your perfect score would be {score}/{len(seqs)} if all guessed right!")
