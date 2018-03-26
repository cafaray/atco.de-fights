def higherVersion(ver1, ver2):
    return map(int, ver1.split('.')) > map(int, ver2.split('.'))