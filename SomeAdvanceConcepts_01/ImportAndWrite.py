# Store the multiplication tables generated in problem 3 in a file named Tables.txt.
from MultiplicationTableUsingComprehensionFunction import mulList
with open ('table.txt','w') as f:
    for i in range(0,10):
        elem = str(mulList[i])
        element = elem + " "
        f.write(element) 
    
           
        