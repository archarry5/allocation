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

def rearrange(vector, numOfDutiesLeftOnDayi, dutyCount):
    n = -1*dutyCount
    idxOfMaxDutiesLeft = np.argpartition(numOfDutiesLeftOnDayi, n)[n:]
    for idx in idxOfMaxDutiesLeft:
        vector[idx] = 1
    return vector


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

for i in range(employeeCount):    
    threshold = employeeCount - dutyPerDay  #we can allow only threshold values to be set randomly without hurting column count (if all are set to 0 randomly). 
    if i < threshold:
        #a = np.random.choice([1, 0], numOfDays, p=[employeesDutyCount[i]/float(numOfDays), (numOfDays - employeesDutyCount[i])/float(numOfDays)])
        a = [1]*employeesDutyCount[i] + [0]*(numOfDays - employeesDutyCount[i])
        np.random.shuffle(a)
        employees = np.vstack([employees, a])
    else:
        col_sums = calculateColumnSum(employees)
        numOfDutiesLeftOnDayi = [(dutyPerDay - col_sum) for col_sum in col_sums]
        a = [0] * numOfDays
        a = rearrange(a, numOfDutiesLeftOnDayi, employeesDutyCount[i])
        employees = np.vstack([employees, a])

headers = ["Day "+str(d+1) for d in range(numOfDays)]
outFileName = 'allocation_'+str(month)+'_' + str(year)+'.csv'
np.savetxt(outFileName, employees, delimiter=',', fmt='%s', header=','.join(headers))



#temp:: if in doubt on count uncomment this and run code. U wud get each row and column count with row number.
##count = 0
##for emp in employees:
##    print(count,list(emp), sum(emp))
##    count+=1
##print(calculateColumnSum(employees))
                     
