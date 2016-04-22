import random
import pickle
import unittest

"""
Function used for Task 1
Accepts an integer representing the number of parameters as the parameter
makes use of python's random library for generating random numbers
Returns the name and score to be used by Task 2
"""


def task1(number_of_questions):
    name = input("Please enter your name:")
    try:
        name = int(name)
        print("Not a valid name\n")
        return "", -1
    except ValueError:
        pass
    question_counter = 1
    score = 0
    operations = [" + ", " - ", " * "]  # a list to store the operations that can be used
    while question_counter <= number_of_questions:
        # generate random numbers
        number1, number2 = random.randint(1, 10), random.randint(1, 10)

        # choose a random operation
        operation = random.choice(operations)

        # assemble question
        question = "Question " + str(question_counter) + ":" + str(number1) + operation + str(number2) + "\n"

        # read answer from user
        answer = input(question)

        """
        Python's raw_input function will read in input as a String
        We must change it into an integer in order to compare it to
        the correct answer
        """
        try:
            answer = int(answer)
        except ValueError:
            print("Invalid type of input")
            return "", -1

        # decide appropriate operation to apply
        if operation == operations[0]:
            correct_answer = number1 + number2
        elif operation == operations[1]:
            correct_answer = number1 - number2
        else:
            correct_answer = number1 * number2

        # check if the user's answer was correct
        if answer == correct_answer:
            print("Correct\n")

            # increment score by 1
            score += 1

        else:
            print("Incorrect\n")

        # move on to the next question
        question_counter += 1

    print(name + "\'s score out of " + str(number_of_questions) + " is " + str(score))
    return name, score


def get_operation():
    evaluations = {"+": lambda num1, num2, ans: (num1 + num2) == ans,
                   "-": lambda num1, num2, ans: (num1 - num2) == ans,
                   "*": lambda num1, num2, ans: (num1 * num2) == ans}
    operation = random.choice(list(evaluations.keys()))
    return operation


""""
A more advanced implementation of the function used for task 1 using the python dictionary data structure
Accepts an integer representing the number of parameters as the parameter
makes use of python's random library for generating random numbers
"""


def task1_advanced(number_of_questions):
    name = input("What is your name?")
    
    try:
        while int(name):
            print("Not a valid name\n")
            name = input("What is your name?")
            
    except ValueError:
        print("Hello "+name)
        pass

    score = 0

    evaluations = {"+": lambda num1, num2, ans: (num1 + num2) == ans,
                   "-": lambda num1, num2, ans: (num1 - num2) == ans,
                   "*": lambda num1, num2, ans: (
                                                num1 * num2) == ans}  # a dictionary used to link an operation to an evaluation

    for question_counter in range(1, number_of_questions + 1):
        # generate random numbers and a random choice for operation
        number1, number2 = random.randint(1, 10), random.randint(1, 10)

        # choose a random operation
        operation = get_operation()

        # assemble question
        question = "Question number " + str(question_counter) + ": " + str(number1) + " " + operation + " " + str(
            number2) + "\nAnswer:"

        # read answer from user
        answer = input(question)

        """
        Python's raw_input function will read in input as a String
        We must change it into an integer in order to compare it to
        the correct answer
        """
        try:
            answer = int(answer)
        except ValueError:
            print("Proposed answer was not a number, answer will be counted as incorrect\n")
            continue

        # check if the user's answer was correct using the appropriate function from evaluate
        if evaluations[operation](number1, number2, answer):
            print("Correct\n")

            # increment score by 1
            score += 1
        else:
            print("Incorrect\n")

    print(name + "\'s score out of " + str(number_of_questions) + " is " + str(score))
    return name, score

if __name__ == "__main__":
    task1_advanced(10)