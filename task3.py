import random
import pickle
import unittest

"""
Function used to sort students using python's inbuilt sorting class

"""


def sort_by(_class, order):
    if order == 1:
        return sorted(_class)
    elif order == 2:
        return sorted(list(_class.items()), key=lambda student: max(student[1]), reverse=True)
    else:
        return sorted(list(_class.items()), key=lambda student: max(student[1]) / float(len(student[1])),
                      reverse=True)


def get_class(class_number):
    if class_number == 1:
        try:
            _class = pickle.load(open("./class1.pkl", "rb"))
        except IOError:
            return None
    elif class_number == 2:
        try:
            _class = pickle.load(open("./class2.pkl", "rb"))
        except IOError:
            return None
    elif class_number == 3:
        try:
            _class = pickle.load(open("./class3.pkl", "rb"))
        except IOError:
            return None
    else:
        return None
    return _class


"""
Function used to implement task 3
"""

def task3():
    def display_grades(class_number, order):
        # store data in the appropriate file
        if class_number == 1 or class_number == 2 or class_number == 3:
            _class = get_class(class_number)
        else:
            print("No such class")
            return

        if _class is None:
            print("No students in class " + str(class_number))
            return

        if len(_class) == 0:
            print("No students in class " + str(class_number))
            return

        sorted_names = sort_by(_class,order)

        if order == 1:
            for name in sorted_names:
                print(name + ":" + str(max(_class[name])))
        elif order == 2:
            for name in sorted_names:
                student_name = name[0]
                scores = name[1]
                print(student_name + ":" + str(max(scores)))
        else:
            for name in sorted_names:
                student_name = name[0]
                scores = name[1]
                print(student_name + ":" + str(round(sum(scores) / float(len(scores)), 2)))

    option = input(
        "\nDisplay Class 1 Grades: 1\nDisplay Class 2 Grades: 2\nDisplay Class 3 Grades: 3\n\nEnter desired option:")
    order_option = input(
        "\nDisplay in alphabetical order: 1\nDisplay in descending order by highest grade: 2\nDisplay in descending order by average grade: 3\n\nEnter desired option:")

    try:
        display_grades(int(option), int(order_option))
    except ValueError:
        print("Incorrect type of input")
    print("\n")

if __name__ == "__main__":
    task3()