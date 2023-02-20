import numpy as np
import pandas as pd


def getNewVariables(data) -> object:
    data["was_previously_contacted"] = data["pdays"].apply(lambda x: 0 if x == 999 else 1)
    return data


def getPreprocessedData(data) -> object:
    # dane wyglądają na porządne pod względem nulli i zbędnych zer

    # podmieniamy unknown z najczęściej występującą wartością
    data["marital"] = data["marital"].replace("unknown", "married")
    data["education"] = data["education"].replace("unknown", "university.degree")
    data["loan"] = data["loan"].replace("unknown", "no")
    data["housing"] = data["housing"].replace("unknown", "yes")
    # w 'default' nie usuwamy "unknown", bo wyszłyby tylko odpowiedzi "nie"
    # w 'job' nie usuwamy "unknown", bo możemy to interpretować jako "inne"

    data = getNewVariables(data)
    return data

