# Decision-Trees-Implementation
Implementation of Decision Trees in python from scratch
	The first step is to convert the .csv file which contains the dataset into a data structure. I am using pandas library to read csv file.
	Next, I made a class Node which contain three things for an object (value, decision, childs). Decision are the decision nodes on which we have to split further, Childs are the nodes of attributes titles 
	Since I am using ID3 algorithm, entropy is calculated in the function findEntropy( ) . the formula for calculating entropy is:
 
The entropy is calculated for each attribute. 

	The next step is to calculate the information gain. The formula for calculating information gain is:
 
Where Entropy(T) is the entropy of the target attribute and Entropy (T,X) is entropy using frequency table of two attributes (target and predictor). 

	Next, the attribute with largest information gain is selected and is calculated in the function findMaxGain( ). 
	The algorithm runs recursively until all data is classified
