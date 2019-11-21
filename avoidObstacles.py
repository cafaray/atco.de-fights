def avoidObstacles(inputArray):
    o=sorted(inputArray)
    c=2
    findYou=False
    while not findYou:
        if c in o:
            c+=1
            continue
        p=c
        while True:            
            p+=c
            if p in o:
                c+=1
                break
            if p>o[-1]:
                findYou=True
                break
              
    return c

inputArray=[5, 3, 6, 7, 9]
e=4
r=avoidObstacles(inputArray)
print("Assertion for test 1 is: ", e==r)

inputArray= [2, 3]
e=4
r=avoidObstacles(inputArray)
print("Assertion for test 2 is: ", e==r)

inputArray= [1, 4, 10, 6, 2]
e=7
r=avoidObstacles(inputArray)
print("Assertion for test 3 is: ", e==r)

inputArray= [1000, 999]
e=6
r=avoidObstacles(inputArray)
print("Assertion for test 3 is: ", e==r)

inputArray= [19, 32, 11, 23]
e=3
r=avoidObstacles(inputArray)
print("Assertion for test 3 is: ", e==r)

inputArray=[5, 8, 9, 13, 14]
e=6
r=avoidObstacles(inputArray)
print("Assertion for test 3 is: ", e==r)
