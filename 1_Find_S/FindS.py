import pandas as pd
import numpy as np
 
#to read the data in the csv file
data = pd.read_csv('D:/engineering/sem6/ML/LAB/1_Find_S/enjoysport.csv')
print(data)
 
#making an array of all the attributes
d = np.array(data)[:,:-1]
print("The attributes are: ")
print(d)
 
#segragating the target that has positive and negative examples
target = np.array(data)[:,-1]
print("The target is: ")
print(target)
 
#training function to implement find-s algorithm
def train(c,t):
    for i, val in enumerate(t):
        if val == "yes":
            specific_hypothesis = c[i].copy()
            break        
    for i, val in enumerate(c):
        if t[i] == "yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass
                 
    return specific_hypothesis
 
#obtaining the final hypothesis
print("The final hypothesis is:")
print(train(d,target))