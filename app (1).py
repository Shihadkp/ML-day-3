from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict')
def predict(# -*- coding: utf-8 -*-
"""breath1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ooc7IXuu6XFSP4lMuCKtu79bEQ-Tz9Hy

## Heart Disease Predictor

### Importing Numpy and Pandas module
"""


import numpy as np
import pandas as pd

file = "./heart.csv"
attributes = ['age', 'sex', 'chest_pain', 'BP', 'cholesterol', 'fasting_bloodsugar', 'rest_ecg', 'max_heartrate', 'exercise_angina', 'oldpeak', 'slope', 'ca', 'thal', 'target']
df = pd.read_csv(file, header = 1, names = attributes)

df

df.describe

df.head()

"""### Data Visualization

#### Importing required modules
"""


import matplotlib.pyplot as plt
import seaborn as sns

"""Few features of the dataset are further classified based on their values. Let's claasify them for better plotting."""

data = pd.read_csv(file, header = 1, names = attributes)

data['sex'][data['sex'] == 0] = 'Female'
data['sex'][data['sex'] == 1] = 'Male'

data['chest_pain'][data['chest_pain'] == 0] = 'typical angina'
data['chest_pain'][data['chest_pain'] == 1] = 'atypical angina'
data['chest_pain'][data['chest_pain'] == 2] = 'non-typical angina'
data['chest_pain'][data['chest_pain'] == 3] = 'asymptomatic'

data['rest_ecg'][data['rest_ecg'] == 0] = 'normal'
data['rest_ecg'][data['rest_ecg'] == 1] = 'abnormal in ST-T wave'
data['rest_ecg'][data['rest_ecg'] == 2] = 'left ventricular hypertrophy'

data['slope'][data['slope'] == 0] = 'up sloping'
data['slope'][data['slope'] == 1] = 'flat'
data['slope'][data['slope'] == 2] = 'down sloping'

data['thal'][data['thal'] == 0] = 'NULL'
data['thal'][data['thal'] == 1] = 'normal blood flow'
data['thal'][data['thal'] == 2] = 'fixed defect'
data['thal'][data['thal'] == 3] = 'reversible defect'

"""Checking the number of individuals with different features"""

data['sex'].value_counts()

data['rest_ecg'].value_counts()

data['chest_pain'].value_counts()

data['thal'].value_counts()

# number of individuals with and without heart disease

df['target'].value_counts().plot.pie(autopct = "%1.0f%%", labels=["Normal", "Heart Disease"], startangle = 0, colors = sns.color_palette("crest"))

# scatter plot of BP and cholesterol for individual with and without heart disease

sns.scatterplot(x = 'BP', y = 'cholesterol', hue = 'target', data = data)

# scatter plot of BP and age for individuals with and withour heart disease

sns.scatterplot(x = 'BP', y = 'age', hue = 'target', data = data)

# scatter plot of cholesterol and age for individuals with and without heart disease

sns.scatterplot(x = 'cholesterol', y = 'age', hue = 'target', data = data)

# relation between Blood pressure and Sex of the individual

sns.histplot(data=df,x='BP',kde=True,hue='sex')

# relation between cholesterol level and sex of an individual

sns.histplot(data = data, x = 'cholesterol', kde = True, hue = 'sex')

"""#### Data Cleaning

Replacing the null values with the mean of that column
"""

df = df.fillna(df.mean())

"""Dropping the target feature"""

x = df.drop('target', axis=1)
y = df['target']

x

x.shape

y

y.shape

"""Splitting the dataset into Training and Testing set"""



from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=0)

X_train.shape

"""#### Data Preprocessing"""

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

X_train

"""Trying various classifiers for checking which classifier is performing better."""

from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB

# Defining classifiers
classifiers = [
    ('Decision Tree', DecisionTreeClassifier()),
    ('K-Nearest Neighbors', KNeighborsClassifier()),
    ('Logistic Regression', LogisticRegression()),
    ('Gradient Boosting', GradientBoostingClassifier()),
    ('Naive Bayes', GaussianNB())
]

# Iterating through the classifiers
for name, clf in classifiers:
    # Training the classifier
    clf.fit(X_train, y_train)

    # Predicting on the test set
    y_pred = clf.predict(X_test)

    # Evaluating the classifier
    accuracy = accuracy_score(y_test, y_pred)
   # print(f'{name} Classifier:')
   # print(f'Accuracy: {accuracy:.3f}\n')

"""As we can see K-Nearest Neighbors Classifier has better evaluation score than other classifiers. We can use th KNN classifier.

Let's use the K-Nearest Neighbors Classifier
"""

# Initializing the classifier
KNN = KNeighborsClassifier()

# Training the classifier
KNN.fit(X_train, y_train)

# Predicting on the Testing set
y_pred = KNN.predict(X_test)

y_pred

"""generating the confusion matrix and calculating the accuracy score"""

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
#print("Confusion matrix :")
#print(cm)

#print("Accuracy = "+str(accuracy_score(y_test, y_pred)*100)[0:5] + "%")

import pickle

pickle.dump(clf,open('clf_saved','wb'))

clf_loaded = pickle.load(open('clf_saved','rb'))

clf_loaded.predict(X_test)

import joblib

joblib.dump(clf,'clf_saved2')

loaded_clf2 = joblib.load('clf_saved2')

loaded_clf2.predict(X_test)

import numpy as np

import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

# Load the saved KNN model
loaded_KNN = pickle.load(open('clf_saved.pkl', 'rb'))

# Assuming 'sc' is the StandardScaler object used for standardization
# and 'attributes' contains the names of features used for training

# Sample single data point (modify with your actual data)
single_data = np.array([45, 1, 2, 140, 200, 0, 1, 150, 1, 0.5, 1, 0, 3]).reshape(1, -1)

# Standardize the single data point
single_data_scaled = sc.transform(single_data)

# Predict using the loaded KNN model
single_output = loaded_KNN.predict(single_data_scaled)

print(single_output)):

    return 0

if __name__ == '__main__':
    app.run(debug=True)
