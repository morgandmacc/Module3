"""
Author: Morgan McCarley

"""


def average():
    score1 = input("Enter your first grade:")
    score2 = input("Enter your second grade:")
    score3 = input("Enter your third grade:")
    return (int(score1) + int(score2) + int(score3))/3


if __name__ == '__main__':
    lastName = input("Enter your last Name:")
    firstName = input("Enter your first Name")
    age = input("Enter your age")
    average_scores = average()
    print("{}, {} age: {} average grade: {}".format(lastName, firstName, age, average_scores))


