import docclass
from subprocess import check_output

import numpy as np



def compareSample(file, pred):

    with open(file, 'r') as filename:
        result = cl.classify(filename.read())
        if result == 'spam':
            pred.append(1)
        else:
            pred.append(0)   
        
def emailTest(cl):

    outcome = [] 
    standard = np.array([1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0])
            
    # testing spam
    try: 
        for i in range(1, 11):
            filename = 'Testing/spam' + str(i) + '.txt'
            
            compareSample(filename, outcome)
                
    # testing non-spam
        for i in range(1, 11):
            filename = 'Testing/notspam' + str(i) + '.txt'
            compareSample(filename, outcome)
            
    except:
        print (filename)
        
    print ('STANDARD is:')
    print(standard)    
    outcome = np.array(outcome)

    print ('OUTCOME  after Comparison is:')
    print(outcome)
   
    truePositive = len(np.where(outcome[np.where(standard == 1)] == 1)[0])
    trueNegative = len(np.where(outcome[np.where(standard == 0)] == 0)[0])
    falsePositive = len(np.where(standard == 1)[0]) - truePositive
    falseNegative = len(np.where(standard == 1)[0]) - trueNegative
   
    confusionMatrix = [[truePositive, falsePositive], [falseNegative, trueNegative]]
    print('CONFUSION MATRIX is :')
    print (confusionMatrix)

    precision = float(truePositive) / (truePositive + trueNegative)
    accuracy = float(truePositive + falsePositive)/(truePositive + trueNegative + falsePositive + falseNegative)
    print('PRECISION',float(precision))
    print('ACCURACY',float(accuracy))

    
cl = docclass.naivebayes(docclass.getwords)
check_output(['rm', 'spamCheck.db'])
cl.setdb('spamCheck.db')
docclass.testEmail(cl)
emailTest(cl)
