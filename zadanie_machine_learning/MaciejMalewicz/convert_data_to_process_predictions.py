import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

numerical = ["age", "duration", "campaign", "previous", "cons.conf.idx", "euribor3m"]
categorical = ["job", "marital", "education", "default", "housing", "loan", "contact", "month", "poutcome"]


def convertDataToProcessPredictions(data):
    data_copy = data.copy()
    data_copy["age"] = np.log(data_copy["age"])
    data_copy["duration"] = data_copy["duration"].apply(lambda x: np.log(x) if x > 0 else 0)
    # wywalamy day_of_week, bo raczej nie jest to znaczący czynnik predykcyjny
    # wywalamy pdays, bo numerycznie te wartości nie mają znaczenia (przez występowanie "999", które jest wbite na sztywno i nic szczególnego nie wnosi)
    # wywalamy emp.var.rate, bo ma bardzo dużą korelację z euribor3m (i nie chcemy w modelu zmiennych, które mówią praktycznie to samo)
    # dlatego w 'numerical' i 'categorical' nie ma nazw tych kolumn
    data_copy_dummies = pd.get_dummies(data_copy[numerical + categorical])
    scale = StandardScaler()
    # skalujemy: \mu = 0, \sigma = 1.
    data_copy_dummies[numerical] = scale.fit_transform(data_copy_dummies[numerical])
    return data_copy_dummies
