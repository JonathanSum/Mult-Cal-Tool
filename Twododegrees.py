import math
num = math.tan((math.pi)*(1/4))
print(num)
list1=[]
list2=[]
def twododegrees(a, b, c, d):
    list = [a, b, c, d]
    num1 = math.degrees(math.atan(int(list[1])/int(list[0]))-math.atan(int(list[3])/int(list[2])))
    return abs(num1)
print(twododegrees(3,4,5,12))



