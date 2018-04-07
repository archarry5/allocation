import sys
import  numpy as np
     
def calculateNumOfDays(month, year):
    daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31,30, 31]
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        daysInMonth[1] += 1
    return daysInMonth[month]

def calculateColumnSum(matrix):
    m,n = matrix.shape
    return [sum([matrix[j][i] for j in range(m)]) for i in range(n)]

def rearrange(debug_i, vector, col_sums, numOfDutiesLeftOnDayi, dutyCount):
    n = -1*dutyCount
    #print("for "+ str(debug_i) + " " +str(n))
    idxOfMoreDutiesLeft = np.argpartition(numOfDutiesLeftOnDayi, n)[n:]
    #print(col_sums)
    #print(idxOfMoreDutiesLeft)
    for idx in idxOfMoreDutiesLeft:
        vector[idx] = 1
    return vector
##    idxOfConstraintFailed = np.where(colConstraintFailed)[0]
##    flipBitsCount = 0
##    idxOfZeroes = np.where([x == 0 for x in vector])[0]
##    viableOptionforFlipping = []
##    print("for " + str(debug_i))
##    print(vector)
##    print(idxOfZeroes)
##    print(col_sums)
##    print(colConstraintFailed)
##    for idx in idxOfConstraintFailed:
##        print('1')
##        vector[idx] = 0
##        flipBitsCount += 1
##    for idx in idxOfZeroes:
##        if flipBitsCount > 0 and col_sums[idx] < colConstraint:
##            print("in")
##            vector[idx] = 1
##            flipBitsCount -= 1
##    print(str(flipBitsCount)+ "while signing off") 
    
        

dutyPerDay = int(input().strip())
month, year = map(int, input().strip().split(' '))
numOfDays = calculateNumOfDays(month, year)
employeeCount = 30
employees = np.empty((0, numOfDays), int)
employeesDutyCount = []
for _ in range(employeeCount):
    employeesDutyCount.append(int(input().strip()))
correcInputCondition = (dutyPerDay < employeeCount) and (dutyPerDay*numOfDays == sum(employeesDutyCount))
if not correcInputCondition:
    print("Incorrect input.. Aborting program!!!")
    print("constraint - duty per day * number of days in month should be equal to sum of employees duty count and duty per day should be less than total employees")
    sys.exit()
#constraint - dutyPerDay * numOfDays = sum of employees dutycount and dutyCount < employeeCount

#employeesDutyCount = sorted(employeesDutyCount,reverse=True)
for i in range(employeeCount):
    
    safeValue = employeeCount - dutyPerDay
    if i < safeValue:
        #a = np.random.choice([1, 0], numOfDays, p=[employeesDutyCount[i]/float(numOfDays), (numOfDays - employeesDutyCount[i])/float(numOfDays)])
        a = [1]*employeesDutyCount[i] + [0]*(numOfDays - employeesDutyCount[i])
        np.random.shuffle(a)
        employees = np.vstack([employees, a])
    else:
        col_sums = calculateColumnSum(employees)
        numOfDutiesLeftOnDayi = [(dutyPerDay - col_sum) for col_sum in col_sums]
        #colConstraintFailed = [col_sum > dutyPerDay for col_sum in col_sums]
        #if True in colConstraintFailed:
        a = [0] * numOfDays
        a = rearrange(i, a, col_sums, numOfDutiesLeftOnDayi, (employeesDutyCount[i]))
        employees = np.vstack([employees, a])

headers = ["Day "+str(d+1) for d in range(numOfDays)]
outFileName = 'allocation_'+str(month)+'_' + str(year)+'.csv'
np.savetxt(outFileName, employees, delimiter=',', fmt='%s', header=','.join(headers))


#temp:: if in doubt on count uncomment this and run code. U wud get each row count.
#column count always satisfied..
count = 0
for emp in employees:
    print(count,list(emp), sum(emp))
    count+=1
print(calculateColumnSum(employees))
                        
