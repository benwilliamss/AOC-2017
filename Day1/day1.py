
def part1(inputLine):
    sumOfCaptcha = 0

#used to check for matches incrementing up the string
    for index in range(0, len(inputLine)-1): #-1 as last value is considered outside loop

        currentNum = inputLine[index]
        if currentNum is inputLine[index+1]:
        #Match, thus, add to total captcha
            sumOfCaptcha += int(currentNum)

#circular condition to check the first and last are a match
    if inputLine[0] is inputLine[-1]:
        sumOfCaptcha += int(inputLine[0])
        
    print("Part 1 Captcha is", sumOfCaptcha)


def part2(inputLine):

    lengthOfString = len(inputLine)
    stepsAhead = lengthOfString//2
    sumOfCaptcha =0
    
    for index in range(0, lengthOfString):
        currentNum = inputLine[index]
        
        if (index+stepsAhead) > lengthOfString-1:
            #ensures that when the step ahead is greater than the length
            #the values wraparound as the sequence is circular
            indexAhead = index+stepsAhead-lengthOfString

        else:
            indexAhead = index + stepsAhead
                    
        
        if currentNum is inputLine[indexAhead]:
            #Match, thus add to total captcha
            sumOfCaptcha += int(currentNum)

            
    print("Part 2 Captcha is", sumOfCaptcha)




input = open("input.txt", "r")
inputLine =  input.read().strip() #input now a string with whitespace removed

part1(inputLine)
part2(inputLine)
