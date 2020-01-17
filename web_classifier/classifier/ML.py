from sklearn import svm
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import csv
import numpy as np

def trainCSV(csv_file, knn, svc, tree, ts=0.33, precision = 3):
    labels = []
    scores = []
    file_path = os.path.join('uploads/', csv_file)
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        csv_list = list(reader)
    
    X = []
    Y = []
    for element in csv_list:
        xs = element[:-1]
        X.append([float(i) for i in xs])
        Y.append(float(element[-1]))

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=ts)

    if knn:
        labels.append('KNN')
        clf = KNeighborsClassifier()
        clf.fit(x_train, y_train)
        scores.append(round(clf.score(x_test, y_test), precision))
        
    if svc:
        labels.append('SVC')
        clf = svm.SVC()
        clf.fit(x_train, y_train)
        scores.append(round(clf.score(x_test, y_test), precision))
    
    if tree:
        labels.append('Decision Trees')
        clf = DecisionTreeClassifier()
        clf.fit(x_train, y_train)
        scores.append(round(clf.score(x_test, y_test), precision))
    
    locations = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots()
    rects = ax.bar(locations, scores, width)
    ax.set_ylabel('Scores')
    ax.set_title('Scores by classifiers')
    ax.set_xticks(locations)
    ax.set_xticklabels(labels)
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height), xy=(rect.get_x() + rect.get_width() / 2, height),
        xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
    fig.tight_layout()
    name = csv_file.split('.')[0]
    path = os.path.join('classifier', 'static', 'classifier',name)
    plt.savefig(path)
    return name + '.png'

if __name__ == "__main__":
    trainCSV('PhishingData.csv', True, True, True)