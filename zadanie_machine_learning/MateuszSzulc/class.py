import pandas
from sklearn import preprocessing
from sklearn.decomposition import KernelPCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

DATA_PATH = "Data.csv"

dataset = pandas.read_csv(DATA_PATH)
pandas.set_option('display.max_columns', None)
print(dataset.head())
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

standard_scaler = preprocessing.StandardScaler()
x_train = standard_scaler.fit_transform(x_train)
x_test = standard_scaler.transform(x_test)

parameters = [{"n_estimators": [x for x in range(5, 101, 5)], "criterion": ["gini", "entropy"]}]

results = []
params = []

for x in range(1, 10):
    kpca = KernelPCA(n_components=x, kernel='rbf')
    X_train = kpca.fit_transform(x_train)
    X_test = kpca.transform(x_test)

    classifier = RandomForestClassifier()
    classifier.fit(X_train, y_train)

    grid_search = GridSearchCV(estimator=classifier,
                               param_grid=parameters,
                               scoring="accuracy",
                               cv=10,
                               n_jobs=-1
                               )
    grid_search.fit(X_train, y_train)
    results.append(grid_search.best_score_)
    params.append(grid_search.best_params_ | {"n_components": x})
    print(x)

best_accuracy_index = results.index(max(results))
print(params[best_accuracy_index])

kpca = KernelPCA(n_components=params[best_accuracy_index]["n_components"], kernel='rbf')
X_train = kpca.fit_transform(x_train)
X_test = kpca.transform(x_test)

classifier = RandomForestClassifier(n_estimators=params[best_accuracy_index]["n_estimators"],
                                    criterion=params[best_accuracy_index]["criterion"])
classifier.fit(X_train, y_train)

expected_result = 2
new_sample = [3, 2, 1, 1, 1, 1, 2, 1, 1]

new_sample = standard_scaler.transform([new_sample])
new_sample = kpca.transform(new_sample)

predicted_result = classifier.predict(new_sample)

print(f"Expected result: {expected_result}, predicted result: {predicted_result[0]}")
