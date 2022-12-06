import random
import os

questions = [
    "What is the college board syntax for accessing an element of aList at index i?",
    "What is the college board syntax for assigning an element of aList to variable 'x'?",
    "What is the college board syntax for assigning the value of a variable 'x' to the element of aList at index i?",
    "What is the college board syntax for assigning the value of aList[j] to aList [i]?",
    "What is the college board syntax for placing a value at index i in aList?",
    "What is the college board syntax for adding a value to the end of aList?",
    "What is the college board syntax for removing a value from aList at index i?",
    "What are the two different types of loops?",
    "Recursive loops involve [   ?   ]."
]
answers = [
    "aList[i]",
    "x <- aList[i]",
    "aList[i] <- x",
    "aList[i] <- aList[j]",
    "INSERT(aList, i, value)",
    "APPEND(aList, value)",
    "REMOVE(aList, i)",
    "For and While",
    "incrementing a variable until it reaches a certain break point"
]

def questionloop():
    index=0
    totalCorrect = 0
    while index < len(questions):
        numbers=random.sample(range(0, 9), 4)
        question = questions[index]
        print(question)
        answer_place=random.randint(0,3)
        if answer_place == 0:
            print(f"""
A: {answers[index]}
B: {answers[numbers[1]]}
C: {answers[numbers[2]]}
D: {answers[numbers[3]]}
""")
            answer = input()
            if answer.lower() == "a":
                print("correct!")
                totalCorrect += 1
            else:
                print("wrong")
            os.system("clear")
        elif answer_place == 1:
            print(f"""
A: {answers[numbers[0]]}
B: {answers[index]}
C: {answers[numbers[2]]}
D: {answers[numbers[3]]}
""")
            answer = input()
            if answer.lower() == "b":
                print("correct!")
                totalCorrect += 1
            else:
                print("wrong")
            os.system("clear")
        elif answer_place == 2:
            print(f"""
A: {answers[numbers[0]]}
B: {answers[numbers[1]]}
C: {answers[index]}
D: {answers[numbers[3]]}
""")
            answer = input()
            if answer.lower() == "c":
                print("correct!")
                totalCorrect += 1
            else:
                print("wrong")
            os.system("clear")
        elif answer_place == 3:
            print(f"""
A: {answers[numbers[0]]}
B: {answers[numbers[1]]}
C: {answers[numbers[2]]}
D: {answers[index]}
""")
            answer = input()
            if answer.lower() == "d":
                print("correct!")
                totalCorrect += 1
            else:
                print("wrong")
            os.system("clear")
        index += 1
    return totalCorrect

total=questionloop()
print(f"You got: {total}/{len(questions)}")