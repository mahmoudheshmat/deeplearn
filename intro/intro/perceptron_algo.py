##### perceptron algorithm trick

### how to modify line for a misclassified point?
'''
if false positive, subtract the point values and bias from the line equation to get a new line to correctly classify point
if false negative, add the ponit values and bias

better to increment line manipulations in case other points become incorrectly classified:
multiply the point values and bias (1) of the data point by 0.10
this is the learning rate (0.10)
substract (if false positive) or add (if false negative) the learning rate from the line weight and bias and re-attempt with these new values
repeat
'''

### pseudocode for perception algorithm
'''
Start with random weights

for every misclassified point(x1... xn):
	if prediction = 0: # if false negative
		for i = 1 .. n:
			change w(i) + ax(i) # where a is the learning rate ex. 0.1
		change b to b + a
	if prediction = 1:
		for i = 1 ..n:
			change w(i) - ax(i)
		change b to b - a