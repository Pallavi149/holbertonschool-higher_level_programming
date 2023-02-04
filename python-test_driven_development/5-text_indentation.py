#!/usr/bin/python3
"""
This is the "5-text_indentation" module with one function:
text_indentation(text)
"""


def text_indentation(text):
    """
    Prints supplied text with two new lines following
    any instance of '.', '?', and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    periods = text.split(".")
    if len(periods) == 0:
        periods = [text]
    l1 = len(periods)
    for i in range(l1):
        period = periods[i].strip()
        if i < (l1 - 1):
            questions = (period + ".").split("?")
        else:
            questions = period.split("?")
        if len(questions) == 0:
            questions = [period]
        l2 = len(questions)
        for j in range(l2):
            question = questions[j].strip()
            if j < (l2 - 1):
                colons = (question + "?").split(":")
            else:
                colons = question.split(":")
            if len(colons) == 0:
                colons = [question]
            l3 = len(colons)
            for k in range(l3):
                colon = colons[k].strip()
                if k < (l3 - 1):
                    print(colon + ":\n")
                else:
                    print(colon, end="")

            if j < (l2 - 1):
                print("\n")
        if i < (l1 - 1):
            print("\n")
