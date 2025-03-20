import os
import platform
#creating quetions
quetions = ['1️⃣ What is the correct way to print "Hello, World!" in Python?', '2️⃣ Which data type is mutable in Python?', '3️⃣ What does == do in Python?','4️⃣ What will 5 // 2 return in Python?','5️⃣ Which of the following is NOT a programming language?']
#creating options
options = [['A) echo "Hello, World!"', 'B) print("Hello, World!")' , 'C) Console.WriteLine("Hello, World!")', 'D) System.out.println("Hello, World!")'], ['A) tuple','B) string', 'C) list','D) int'],['A) Assigns a value','B) Compares two values for equality', 'C) Checks if two variables refer to the same object ','D) None of the above'], ['A) 2.5','B) 2','C) 3','D) Error'], ['A) Python','B) HTML','C) Java','D) C++']]
#correct answer shortcuts
correctAnswers = ['b', 'c','b','b','b']
#creating answers
correctAns = ['B) print("Hello, World!")' , 'C) list','B) Compares two values for equality','B) 2','B) HTML']


terminal_width = os.get_terminal_size().columns
right_answer = 0
wrong_answer = 0
expected_user_input = ['a','b','c','d']
loop_count = 0
wrong_answer_index = []
wrong_answer_user_input = []


def space():
    for i in range(2):
        print()
def welcome(a="Welcome to Koun banega corrorpati"):
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    header = a
    border = "~"*terminal_width
    print(border)
    print(border)
    print(header.center(terminal_width))
    print(border)
    print(border)



for quetion in quetions:
    welcome()
    space()
    print(quetion)
    print()
    for option in options[loop_count]:
        print(option)
        print()
    while True:
        userInput = input("Enter your answer: ").lower()
        if userInput in expected_user_input:
            break
        else:
            print("Please enter a valid Choice")
    if userInput == correctAnswers[loop_count]:
        right_answer+=1
    else:
        wrong_answer+=1
        wrong_answer_index.append(loop_count)
        if userInput == "a":
            wrong_answer_user_input.append(0)
        elif userInput =="b":
             wrong_answer_user_input.append(1)
        elif userInput=="c":
             wrong_answer_user_input.append(2)
        else:
             wrong_answer_user_input.append(4)

    loop_count+=1


welcome("Your Result")
space()
print(wrong_answer_user_input)
print(f"Correct ans: {right_answer}".rjust(terminal_width))
print(f"Wrong ans: {wrong_answer}".rjust(terminal_width))
if right_answer <=2 and right_answer>=1:
    print("Aap jitte hai 1 corror".center(terminal_width))
elif right_answer>=3 and right_answer<=4:
    print('aap jitte hai 3 corror'.center(terminal_width))
elif right_answer==5:
    print("Aap jitte haii 7 corrorrrrrrrrrrr".center(terminal_width))
else:
    print("Beta tumse na ho payega!".center(terminal_width))
    space()
if wrong_answer>0 :
    print("Correct answers of quetions that you did wrong are:")
    for index in wrong_answer_index:
        space()
        print(quetions[index])
        count = 0
        a = options[index]
        print("Your ans: ❌",a[wrong_answer_user_input[count]])
        count+=1
        print("Correct ans: ✅", correctAns[index])