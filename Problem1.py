#Midterm Exam
#Problem1.py
#Name: Alex Bowes
#Date: 10/23/24

def listSum(myList):
    total = 0
    for number in myList:
        total += number
    return total

def listMax(myList):
    for number in myList:
        max_value = number
    return number

def listMin(myList):
    min_value = myList[0]
    for number in myList:
        if number < min_value:
            min_value = number
    return min_value

def listAverage(myList):
    total = listSum(myList)
    return total / len(myList)

def listAverageDropLowest(myList):
    min_value = listMin(myList)
    total = 0
    count = 0
    for number in myList:
        if number != min_value:
            total += number
            count += 1
    return total / count


def main():
    testList = [1, 2, 3, 4]
    total = listSum(testList)
    ave = listAverage(testList)

    print("The total of the list is %d and the average is %.2f" % (total, ave))

    totalDropLow = listAverageDropLowest(testList)

    print("The average is %.2f if we drop the lowest value." % (totalDropLow))


if __name__ == '__main__':
    main()
