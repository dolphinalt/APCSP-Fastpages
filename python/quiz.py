import getpass

def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg


prompts=["What command would you use to display text into the terminal?", "What command would you use to ask the user for information?", "What is the keyword used in Python to define a function?", "How would you write a print statement to concatenate a string containing variable A with string 'Hello'? (include print() and use '' instead of \"\"", "How do we add a pre-made library to our code?", "We use _______ to store information for later use.", "Given the code, {variable = 1} what type of variable is this?", "Given the code, {variable = 1.1} what type of variable is this?", "Given the code, {variable = 'Hello'} what type of variable is this?"]
answers=["print", "input", "def", "print('Hello' + A)", "import", "variables", "integer", "float", "string"]

correct = 0
questions = len(prompts)

def gradeResponse(response, answer):
    global correct
    if response == answer:
        print(f"{response} is correct!\nGood job :D")
        correct += 1
    else:
        print(f"{response} is incorrect!\nBetter luck next time :(")

print(f"Hello {getpass.getuser()}!")
print(f"You will be asked {str(questions)} questions.")
rsp = question_with_response("Are you ready to take a quiz? [Y/n]")
if rsp == "y" or rsp == "Y":
    print("Lets get started!")
else:
    print("Bye :(")
    exit()

for i in range(0, questions):
    rsp = question_with_response(prompts[i])
    gradeResponse(rsp, answers[i])

print(f"You got a total of {correct} out of {questions}!")