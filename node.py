class Node:
    nextMap={} #next level's all nodes
    id=""
    text=""
    def __init__(self,id,t):
        self.text = t
        self.nextMap = {}
        self.id = id

    def addNode(self,newNode):
        self.nextMap[newNode.id] = newNode

    def hasNext(self): #whether have next level node
        return bool(self.nextMap) #Empty dictionaries evaluate to False in Python

    def isNext(self,i): #whether next level have id i in the node
        if bool(self.nextMap) == False:
            return False
        elif i in self.nextMap:
            return True
        else:
            return False

    # def writeId(self,i): #write ID
    #     if self.id == "":
    #         self.id+=i
    #     else:
    #         temp = " "+i
    #         self.id+=temp

    # def clearId(self): # clear ID
    #     self.id = ""

    def getNextId(self): #get ID
    	l=[]
        for k in self.nextMap.keys():
        	l.append(k)
        return l

    def goNext(self,i): #get next level node which's text is t
        # return list(self.nextMap.keys())[list(self.nextMap.values()).index(t)]
        # print ( self.nextMap[i])
        return  self.nextMap[i]

    # def getAllId(self, idset): #get this node's all child node's ID

    def getText(self): #get node's text
        print(self.text)
        return self.text

    def setText(self,newText): #set node's text
        if self.text == "":
            self.text+=newText
        else:
            temp =newText
            self.text+=temp

    # def getNextSet(self): #get next level all Node set

    def remove(self,i): #remove node t
        self.nextMap.pop(i, None)
    # def getCode(self): #change code