def rowDifference(listOfValues):
    
                           
            #presets/initialises the small and large vals comparision
            firstVal = int(listOfValues[0])

            smallVal = firstVal
            largeVal = firstVal
            
            for value in listOfValues[1:]: # [1:] as firstVal already checked
               
                currentVal = int(value)
                if currentVal < smallVal:
                    smallVal = currentVal

                elif currentVal > largeVal:
                    largeVal = currentVal
            
                        
            return  largeVal - smallVal #returns the difference
            


def rowEvenlyDivisibleValue(listOfValues):
    #return the quotient of the two divisible values in a row

    #Method: two for loops to isolate and divide each value
    #break/return when the function
    
    for intX in range(0,len(listOfValues)):
        
        #str to int
        val = int(listOfValues[intX])
    
        for intY in range(intX+1, len(listOfValues)): 
            #ensures the same value is not compared 
           
            valBeingComparedTo = int(listOfValues[intY])
            
            #if the value is divisible by the other to produce 0
            #hence evenly divisible and return the quotient
            if val % valBeingComparedTo == 0: 
                return  val // valBeingComparedTo
                                
            if valBeingComparedTo % val == 0:
                return valBeingComparedTo // val
                        



with open("input.txt","r") as f:
    linesOfInput = f.readlines()
    
    checkSum=0
    evenlyDivisibleTotal =0

    for line in linesOfInput: 
        listOfValues = line.split()

        #pass in the row into the function to get the returned value
        checkSum += rowDifference(listOfValues)
        evenlyDivisibleTotal += rowEvenlyDivisibleValue(listOfValues)

    print("check sum is", checkSum)
    print("\nEvenly Divisible quotients of all rows is", evenlyDivisibleTotal) 

    
