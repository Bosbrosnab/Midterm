#Midterm Exam
#Problem2.py
#Name: Alex Bowes
#Date: 10/23/24

def countvows(instr):
    
    vows = "AaEeIiOoUu"
    vowcount = 0
    
    for char in instr:
        for vow in vows:
            if char == vow:
                vowcount += 1
                break
    return vowcount

userin = input("Enter a word/sentence: ")
result = countvows(userin)
print("The number of vowels in word/sentence is:", result)
