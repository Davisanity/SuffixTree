import time
from node import Node
from SuffixTree import Suffix

def main():
    testsuffix()
    # readFile()

def readFile():
    testDataId=[]
    testDataSet=[]
    # f = open('t1.txt','r')
    f = open('t2.txt','r')
    for line in f.readlines():
        a=line.split(":")
        testDataId.append(a[0])
        testDataSet.append(map(int,a[1].split(",")))
    return testDataId,testDataSet

def testsuffix():
    str1 = [20,13,87,20,13,28,20,13,87,20]
    str2 = [20,62,12,20,13,23]
    str3 = [13,20,13,87,28,12]
    tStart = time.time()
    s = Suffix()
    id,set = readFile()
    for i in range(len(id)):
        s.addTree(id[i],set[i])
    # s.addTree('T001',str1)
    # s.addTree('T002',str2)
    tEnd = time.time()
    print "it costs %f sec" % (tEnd-tStart)
    s.queryTree(s.inputQuery())

if __name__ == "__main__":
    main()

# def testNode():
#     n = Node("10","text0")
#     n1 = Node("11","text1")
#     n.addNode(n1)
#     n2 = Node("12","text2")
#     n.addNode(n2)
#     n3=Node("21","text3")
#     n4=Node("22","text4")
#     n1.addNode(n3)
#     n1.addNode(n4)
    # print(n.nextMap['11'].text)
    # print(n.hasNext())
    # print(n1.hasNext())
    # id = '21'
    # print type(n1.id) # id is type string
    # print(n.isNext(id))
    # print(n1.isNext('12'))
    # n.getId()
    # n=n.goNext('11')
    # print(n.nextMap)
    # l = n.getNextId()
    # print(l[0])
    # n.remove('12')
    # print(n.isNext('12'))