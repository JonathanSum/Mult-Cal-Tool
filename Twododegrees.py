import math
num = math.tan((math.pi)*(1/4))
print(num)
list1=[]
list2=[]
def twodotsdeg2d(a, b, c, d):
    list = [a, b, c, d]
    num1 = math.degrees(math.atan(int(list[1])/int(list[0]))-math.atan(int(list[3])/int(list[2])))
    return abs(num1)
# thirddemsion for degree in two vectors
f=0
def magni(a, b):
    lista = a
    listb = b
    c = math.sqrt(lista[0]**2+lista[1]**2+lista[2]**2)
    d = math.sqrt(listb[0]**2 + listb[1]**2 + listb[2]**2)
    e = lista[0]**2 + lista[1]**2 + lista[2]**2
    f = listb[0]**2 + listb[1]**2 + listb[2]**2
    answer = {"len1": c, "len2": d, "nrlen1": e, "nrlen2": f}
    return answer
a = [6, 3, 2]
b = [4, 0, -1]
print("end")
answer = magni(a, b)
print(answer)

def twodotsdeg3d(a,b):
    answerf = magni(a, b)
    t1=(a[0]*b[0] + a[1]*b[1] + a[2]*b[2])/((math.sqrt(answerf["nrlen1"]*answerf["nrlen2"])))
    answerInt=math.degrees(math.acos(t1))
    return answerInt


a=[1,2,3] #17 of 13.3
b = [4,0,-1] #19
a = [0,1,1]
b = [1, 2, -3]
thd=twodotsdeg3d(a,b)
def checkdotsRTri(a,b):
    answerr = a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    return answerr
a1=checkdotsRTri([1,-3,-2],[2,0,-4])
print(a1)



print(thd)


def vectorMag(a,b,c):
    return (a**2+b**2+c**2)
print(vectorMag(3,4,5))
print(twodotsdeg3d([1,1,-1],[3,-4,5]))

#def crossProduct3d(a,b):
def vecCross3d(a,b):
    firstE = a[2]*b[3]-b[2]*a[3]
    secondE = a[1]*b[3]-b[1]*a[3]
    thirdE = a[1]*b[2]-b[1]*a[2]
    return "{}i + {}j + {}k".format(firstE, secondE, thirdE)
    print(vectCross3dd([2,-1,3],[3,2,1]))
