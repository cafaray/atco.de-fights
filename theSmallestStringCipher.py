

A<B and A!=B

i >= 0 and i< min(len(A), len(B))
A[i] < B[i]  and j>=0 and j<i A[j] == B[j]

String A is lexicographically smaller than string B either
if A is a prefix of B (and A ≠ B), 
or if there exists such index i (0 ≤ i < min(A.length, B.length)), 
    that Ai < Bi, 
    and for any j (0 ≤ j < i) 
    Aj = Bj. 
    
The lexicographic comparison of strings is implemented by operator < in modern programming languages