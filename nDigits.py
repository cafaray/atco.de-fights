import math
def logSome(x, n):
    return 1 + n*(math.log10(x))//1

# return (n!=1e3) + n*(math.log10(a))//1

for x in range(1000, 10001, 1000):
    print(x, logSome(x, 3))


# CREATE USER 'ftcdrvtrck'@'localhost' identified by 'wh4t4#r0cK.ro!!';
# GRANT SELECT, INSERT, UPDATE, DELETE, EXECUTE ON drivetrack.* to 'ftcdrvtrck'@'localhost';
# mysql -u ftcdrvtrck -p -h 35.196.159.170