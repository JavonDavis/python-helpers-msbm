import random
import pickle
import unittest
"""
    Function used for task two takes the student's class nam
    makes use of python's pickle library for storing data
"""


def task2(class_number, name, score):
    class1 = {}
    class2 = {}
    class3 = {}

    # initial set up and loading any data already present
    try:
        class1 = pickle.load(open("./class1.pkl", "rb"))
    except IOError:
        pickle.dump(class1, open("./class1.pkl", "wb"))

    try:
        class2 = pickle.load(open("./class2.pkl", "rb"))
    except IOError:
        pickle.dump(class2, open("./class2.pkl", "wb"))

    try:
        class3 = pickle.load(open("./class3.pkl", "rb"))
    except IOError:
        pickle.dump(class3, open("./class3.pkl", "wb"))

    # store data in the appropriate file
    if class_number == 1:
        if name in class1:
            class1[name].append(score)
        else:
            class1[name] = [score]
        pickle.dump(class1, open("./class1.pkl", "wb"))
    elif class_number == 2:
        if name in class2:
            class2[name].append(score)
        else:
            class2[name] = [score]
        pickle.dump(class2, open("./class2.pkl", "wb"))
    else:
        if name in class3:
            class3[name].append(score)
        else:
            class3[name] = [score]
        pickle.dump(class3, open("./class3.pkl", "wb"))


"""Function for task 2 modified to fit specifications in Task 3"""


def task2_modified(class_number, name, score):
    class1 = {}
    class2 = {}
    class3 = {}

    # initial set up and loading any data already present
    try:
        class1 = pickle.load(open("./class1.pkl", "rb"))
    except IOError:
        pickle.dump(class1, open("./class1.pkl", "wb"))

    try:
        class2 = pickle.load(open("./class2.pkl", "rb"))
    except IOError:
        pickle.dump(class2, open("./class2.pkl", "wb"))

    try:
        class3 = pickle.load(open("./class3.pkl", "rb"))
    except IOError:
        pickle.dump(class3, open("./class3.pkl", "wb"))

    # store data in the appropriate file
    if class_number == 1:
        if name in class1:
            class1[name].append(score)
            total_number_of_scores = len(class1[name])

            # check to ensure only last 3 grades are kept recorded
            if total_number_of_scores > 3:
                class1[name] = class1[name][total_number_of_scores - 3:]
        else:
            class1[name] = [score]
        pickle.dump(class1, open("./class1.pkl", "wb"))
    elif class_number == 2:
        if name in class2:
            class2[name].append(score)
            total_number_of_scores = len(class2[name])
            if total_number_of_scores > 3:
                class2[name] = class2[name][total_number_of_scores - 3:]
        else:
            class2[name] = [score]
        pickle.dump(class2, open("./class2.pkl", "wb"))
    else:
        if name in class3:
            class3[name].append(score)
            total_number_of_scores = len(class3[name])
            if total_number_of_scores > 3:
                class3[name] = class3[name][total_number_of_scores - 3:]
        else:
            class3[name] = [score]
        pickle.dump(class3, open("./class3.pkl", "wb"))