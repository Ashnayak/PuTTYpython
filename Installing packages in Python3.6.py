## Step 1 : Choose the packages that needs to be installed
import sys
import numpy as np
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

## Step 2 : Check if the packages are already installed

## Step 3 : Set Python version to Python3.6
export PATH=/opt/Anaconda3-5.1.0/bin:$PATH
export SPARK_MAJOR_VERSION=2
export PYSPARK_PYTHON=python3.6

## Step 4: Trigger the Python3.6 terminal
python3.6

## Step 5 : Check if the package is already installed using import command
## Step 6 : Check the working of the packages using few examples

## Step 7 : Come out of the Python3.6 terminal
quit();

## Use the below steps for the packages that are not installed
## Step 8 : Fetch package URLS (below are Keras packages URLs)
https://files.pythonhosted.org/packages/64/01/878553a3af23d9a831edbe67889a61aad8b429409b38f5ac2604fba36e9f/Keras-2.2.2.tar.gz
https://files.pythonhosted.org/packages/60/27/a25dfc6e49a6ab3de2d5f23fdb851f18d45ea9867a0955906a5c488ebbe2/Keras_Applications-1.0.5.tar.gz
https://files.pythonhosted.org/packages/be/2c/c9bdd8fe3e2f7f4ea4d8f22f8f556bc38261e9f38b4d426b607e9d60996c/Keras_Preprocessing-1.0.3.tar.gz

## Step 9 : Set the proxy settings for download
export http_proxy="http://10.57.128.25:8080"; 
export https_proxy="http://10.57.128.25:8080";

## Step 10 : Set the path to /home/hdp_06/
cd /home/hdp_04/

## Step 11 : Download the Python packages using the URLs
wget <package-URL>

## Step 12 : Unzip the packages
tar -xvzf <package-name>

## Step 13 : Generate the command that will be used in Python3.6 to import the packages
sys.path.append("<path of the package>")

## Step 14 : Repeat the steps from 5 - 10 until all the packages are installed

## Step 15 : Go to Python3.6 and use the Generated commands
import sys ## To be used to set the path
sys.path.append("/home/hdp_04/Keras-2.2.2")
sys.path.append("/home/hdp_04/Keras_Applications-1.0.5")
sys.path.append("/home/hdp_04/Keras_Preprocessing-1.0.3")

## Step 16 : Import the rest of the required packages
## Step 17 : Start coding