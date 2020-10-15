## Sample ANN Code in Python3.6

## Set the path for Keras Packages 
import sys
sys.path.append("/home/hdp_04/Keras-2.2.2")
sys.path.append("/home/hdp_04/Keras_Applications-1.0.5")
sys.path.append("/home/hdp_04/Keras_Preprocessing-1.0.3")

## Import all the required packages
import numpy as np
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

## Import the dataset
dataset = pd.read_csv("lapsed_all.csv")

## Set the Independent and Dependent variables
X=dataset.drop("atrisk_flag",axis=1).values
y=dataset["atrisk_flag"].values

#Splitting into Train/Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 10)

#Scaling features
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Build neural network classifier
classifier = Sequential()
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu', input_dim = 37))

#Adding the second hidden layer
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu'))

#Adding the output layer
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

#Compiling Neural Network
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#Fitting the model 
classifier.fit(X_train, y_train, batch_size = 100, nb_epoch = 100)

#Predicting the Test set results
y_true, y_pred = y_test, classifier.predict(X_test)

#Putting probability cutoff
y_pred = (y_pred > 0.5)

#Creating the Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
print(cm)
print(accuracy_score(y_true, y_pred))
