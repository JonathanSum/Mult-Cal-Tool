def vecCross3d(a,b):
    firstE = a[1]*b[2]-b[1]*a[2]
    secondE = a[0]*b[2]-b[0]*a[2]
    secondE = secondE*-1
    thirdE = a[0]*b[1]-b[0]*a[1]
    return "{}i + {}j + {}k".format(firstE, secondE, thirdE)
