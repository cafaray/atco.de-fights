def rectangleRotation(a, b):
    # first, we need the radio for 4 triangles formed inside
    r = pow(a/2,2)+pow(b/2,2)
    r = int(math.ceil(pow(r,.5)))    
    #print(r)
    ## around the circle inside:
    p = 0
    for i in range(-r,r+1):
        for j in range(-r,r+1):
            # gain the position in cartesian draw
            x = i*math.cos(math.radians(-45)) - j*math.sin(math.radians(-45))
            y = i*math.sin(math.radians(-45)) + j*math.cos(math.radians(-45))
            #print('x, y', x, y)
            if -a/2<=x<=a/2 and -b/2<=y<=b/2:
                p += 1
    return p