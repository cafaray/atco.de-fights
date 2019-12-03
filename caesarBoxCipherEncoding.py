def caesarBoxCipherEncoding(inputString):
    l=len(inputString)
    q=int(pow(l,.5))
    x,y,r=0,0,''
    while y<q:
        x=0            
        while x<q:
            r+=inputString[y+(x*q)]
            x+=1
        y+=1
    return r

inputString="a message"
e="aea sgmse"
r=caesarBoxCipherEncoding(inputString)
print("Assertion 1: ", e==r)