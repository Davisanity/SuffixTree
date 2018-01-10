import time
from node import Node
class Suffix:
	rootNode = Node("","")

	def __init__(self):	
		now = self.rootNode
		
		# T001: 20,13,87,20,87,14....
		# in Tree Node's id is '20','13'... '20's text is 'T001'
	def addTree(self,text,element):
		for j in range(len(element)):
			self.now = self.rootNode
			for i in range(j,len(element)):
				t = str(i)
				e = str(element[i])
				#if id 'e' in nextMap means e is in the tree
				#text would be = 'T001:1,2,3;T002:2,4,5'
				#so is not in text , means T00x is not labeled
				if bool(self.now.isNext(e)):
					self.now = self.now.goNext(e)	
					if text not in self.now.text:
						t=";"+str(text)+":"+str(i)
						self.now.setText(t)
					else:
						self.now.setText(","+t)
					# print self.now.id
					# print self.now.text 
				#if e isn't in nextMap, you need to addNode
				else:
					t=str(text)+":"+str(i)
					tempNode = Node(e,t)
					self.now.addNode(tempNode)
					self.now = tempNode
					# print self.now.id
					# print self.now.text 
			# print(" ")
	#query is '1 2 3'
	#input is [1,2,3] so input[0]=1  (type is string)
	def inputQuery(self):
		string = raw_input("Enter your query(seperated by space) :")
		input = string.split(" ")
		return input

	def queryTree(self,input):
		tS = time.time()
		self.now = self.rootNode
		#if i (type string) is in nextMap keep traverse
		#until the end, that is input[-1]
		for i in input:	
			if bool(self.now.isNext(i)):	
				self.now = self.now.goNext(i)
				if i==input[-1]:
					output = self.outputProcess(self.now.text,len(input))
					tE = time.time()
					print "Query costs %f sec" % (tE-tS)
					return output
				        		
        	else:
				print ("sorry your query is not in the Suffix tree")
				return None
	#T001:1,T001:4,T001:7
	#split this string:T001:1,4,7;T002:4
	# a[0] = 'T001:1,4,7' a[1] = 'T002:4'
	# b[0] = 'T001' b[1] = '1,4,7'
	# c[0] = '1' c[1] = '4' c[2]='7'
	# d = 'T001'+':'+'0,3,6'
	# output = T001:0,3,6;T002:3
	def outputProcess(self,string,leng):
		d=""
		output = ""
		count = 0
		a = string.split(";")
		for i in range(len(a)):
			b = a[i].split(":")
			c = b[1].split(",")
			count+=len(c)
			d=""
			for j in c:
				if j==c[-1]:
					j = int(j)-(leng-1)
					d+=str(j)
				else:
					j = int(j)-(leng-1)
					d+=str(j)+","
			if i==(len(a)-1):
				d = b[0]+":"+d
				output+=d
			else:
				d = b[0]+":"+d+'\n'
				output+=d
		print output +'\nFucking count:',count
		
		return output
