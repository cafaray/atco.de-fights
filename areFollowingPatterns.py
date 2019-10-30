from collections import defaultdict
def areFollowingPatterns(strings, patterns):
    pats = defaultdict(set)
    strs = defaultdict(set)
    for w, p in zip(strings, patterns):
        pats[p].add(w)
        strs[w].add(p)

    for p in pats:
        if len(pats[p]) != 1:
            return False

    for w in strs:
        if len(strs[w]) != 1:
            return False

    return True

strings= ["cat", 
 "dog", 
 "dog"]
patterns= ["a", 
 "b", 
 "b"]

expected = True
#response = areFollowingPatterns(strings, patterns)
#print("Assertion: ", response==expected)

strings=["cat", "dog", "doggy"]
patterns=["a", "b", "b"]
expected = False
response = areFollowingPatterns(strings, patterns)
print("Assertion: ", response==expected)
