import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import copy

dataset = pd.read_csv('dataset.csv')
X = dataset.iloc[:, 1:].values
# print(X)
attribute = ['Outlook', 'Temp', 'Humidity', 'Wind']

class Node(object):
    def __init__(self):
        self.value = None
        self.decision = None
        self.childs = None

def findEntropy(data, rows):
    yes = 0
    no = 0
    ans = -1
    idx = len(data[0]) - 1
    entropy = 0
    for i in rows:
        if data[i][idx] == 'Yes':
            yes = yes + 1
        else:
            no = no + 1

    x = yes/(yes+no)
    y = no/(yes+no)
    if x != 0 and y != 0:
        entropy = -1 * (x*math.log2(x) + y*math.log2(y))
    if x == 1:#just one value for attribute having answer yes
        ans = 1
    if y == 1:# just one value for attribute having answer no
        ans = 0
    return entropy, ans

def findMaxGain(data, rows, columns):
    maxGain = 0
    retidx = -1
    entropy, ans = findEntropy(data, rows)
    if entropy == 0:
        
        return maxGain, retidx, ans

    for j in columns:
        mydict = {}
        idx = j
        for i in rows:
            key = data[i][idx]
            if key not in mydict:
                mydict[key] = 1
            else:
                mydict[key] = mydict[key] + 1
        gain = entropy

        # print(mydict)
        for key in mydict:
            yes = 0
            no = 0
            for k in rows:
                if data[k][j] == key:
                    if data[k][-1] == 'Yes':
                        yes = yes + 1
                    else:
                        no = no + 1
            # print(yes, no)
            x = yes/(yes+no)
            y = no/(yes+no)
            # print(x, y)
            if x != 0 and y != 0:
                gain += (mydict[key] * (x*math.log2(x) + y*math.log2(y)))/18
        # print(gain)
        if gain > maxGain:
            
            maxGain = gain
            retidx = j

    return maxGain, retidx, ans

def buildTree(data, rows, columns):

    maxGain, idx, ans = findMaxGain(X, rows, columns)
    root = Node()
    root.childs = []
  
    if maxGain == 0: #No further need of splitting
        if ans == 1:
            root.value = 'Yes'
        else:
            root.value = 'No'
        return root

    root.value = attribute[idx] 
    mydict = {}
    for i in rows:
        key = data[i][idx]
        if key not in mydict:
            mydict[key] = 1
        else:
            mydict[key] += 1

    newcolumns = copy.deepcopy(columns)
    newcolumns.remove(idx) #Removng the selected attribute
    for key in mydict:
        newrows = []
        for i in rows:
            if data[i][idx] == key:
                newrows.append(i) #finding all rows having selected attribute
       
        temp = buildTree(data, newrows, newcolumns)
        temp.decision = key
        root.childs.append(temp)
    return root

def traverse(root):
    
    dataset.append(root.decision)
    dataset.append(root.value)
    print(root.decision)
    print(root.value)
    n = len(root.childs)
    if n > 0:
        for i in range(0, n):
            traverse(root.childs[i])
              

def calculate():
    rows = [i for i in range(0, 18)]
    columns = [i for i in range(0, 4)]
    root = buildTree(X, rows, columns)
    print('*********--Path--**********')
    root.decision = 'Start'
    traverse(root)

dataset=list()
calculate()

#print(dataset)
print('-------------------------')
predict=['Sunny', 'Hot','High',False]
print(predict)
print('Results:')
print('-------------------------')

var1=dataset[1]
k=0
m=-1
if var1=='Outlook':
  
    

  for i in dataset:
    m=m+1
   
    if dataset[m]==predict[0]:
      k=m
      if dataset[m]=='Overcast':
        print('Predicted:')
        print(dataset[m+1])
        break
      for j in range(k,len(dataset)):
        
        if dataset[j]=='Humidity':
          var2=predict[2]
          
          for n in range(j,len(dataset)):
            
            if dataset[n]==predict[2]:
              
              print('Predicted:')
              print(dataset[n+1])
              break
          break
        elif dataset[j]=='Wind':
         
          var2=predict[3]
          
          for n in range(j,len(dataset)):
            
            if dataset[n]==predict[3]:
              
              print('Predicted:')
              print(dataset[n+1])
              break
          break
            

