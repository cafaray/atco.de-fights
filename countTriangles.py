# Elegant solution for codefighters
# ---------------------------------
# P=eval(dir()[0])
# r,n=0,len(P[0])
# for i in range(n): 
#     for j in range(i + 1, n): 
#         for k in range(j + 1, n):             
#             ax = P[0][j] - P[0][i]
#             ay = P[1][j] - P[1][i]
#             bx = P[0][k] - P[0][i]
#             by = P[1][k] - P[1][i]        
#             if (ax * by - ay * bx != 0):
#                 r+=1
# return r
# ---------------------------------

def countTriangles(x, y):
    c = 0
    for i in range (len(x)):
        for j in range(i+1, len(x)):
            for k in range(j+1, len(x)):
                ax = x[j] - x[i]
                ay = y[j] - y[i]
                bx = x[k] - x[i]
                by = y[k] - y[i]        
                if (ax * by - ay * bx != 0):
                    c+=1;        
    return c

# samples to test the code for execution : 
x=[0, 0, 1, 1]
y=[0, 1, 1, 0]
e=4
r=countTriangles(x, y)
print("Assertion 1 is: ", r, "==", e, e==r)

x=[0, -1, -2]
y=[0, -2, -4]
e=0
r=countTriangles(x, y)
print("Assertion 2 is: ", r, "==", e, e==r)

x=[0, 0, 0, 0]
y=[1, 2, 3, 4]
e=0
r=countTriangles(x, y)
print("Assertion 3 is: ", r, "==", e, e==r)

x=[0, 0, 0, 0, 10]
y=[1, 2, 3, 4, -10]
e=6
r=countTriangles(x, y)
print("Assertion 4 is: ", r, "==", e, e==r)

x=[10, 5, 7, 8, 9]
y=[-2, -3, 5, 6, 8]
e=10
r=countTriangles(x, y)
print("Assertion 5 is: ", r, "==", e, e==r)