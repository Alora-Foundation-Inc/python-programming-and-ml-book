# Demonstrate the four common range patterns:
# range(stop), range(start, stop), range(start, stop, step), and reverse counting
for i in range(3):      # 0,1,2
    print("range(3):", i)

for i in range(2, 5):   # 2,3,4
    print("range(2,5):", i)

for i in range(10, 21, 5):  # 10,15,20
    print("range(10,21,5):", i)

for i in range(5, 0, -1):   # 5,4,3,2,1
    print("range(5,0,-1):", i)
