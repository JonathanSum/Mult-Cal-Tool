#lista=[-1, 4, 0, 1, 2, -1, -1, 1, 2]
lista=[5,1,3,7,9,-1,1,-15,11]

def dis3(a1,b1,c1,d1,e1,f1):
    return (a1 - d1) ** 2 + (b1 - e1) ** 2 + (c1 - f1) ** 2
def dis2(list1):
    l1=dis3(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5])
    l2=dis3(list1[3],list1[4],list1[5],list1[6],list1[7],list1[8])
    l3=dis3(list1[0], list1[1], list1[2], list1[6], list1[7], list1[8])
    print([l1,l2,l3])
list3=[0,3,-4,1,2,-2,3,0,1]
dis2(list3)
