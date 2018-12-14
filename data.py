# Written By Joynul Islam

import random, pandas as pd                             #For random seeds and DataFrames.
from sklearn.model_selection import train_test_split    #Splits data into training and testing data sets.
from sklearn.tree import DecisionTreeClassifier         #Runs algorithm to make decision.

#Reading data file with responses and converting into pandas DataFrame.
optionData = pd.read_csv('./training_data.csv')

#Y Variable - Self assigned personality from users.
Y = optionData[['Personality']].copy()

#X Variable - The data from IoT devices for the model to train from.
features = ['Alexa', 'Sonos', 'Phue', 'Arduino']
X = optionData[features].copy()

#Whole data set used for training.
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0, random_state=324)

#Create ML model.
personality_classifier = DecisionTreeClassifier(max_leaf_nodes=30, random_state=0)

#Train model with data.
personality_classifier.fit(X_train, Y_train)

data_points = pd.read_csv('./responses.txt')

#Guess users personality.
predictions = personality_classifier.predict(data_points)

with open('./data.txt', 'w') as final:
    final.write("{}".format(predictions[0]))