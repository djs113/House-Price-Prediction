import pandas as pd
import numpy as np
import pickle

## For Prediction

def predict(location, sqft, bath, bhk):


# Assuming you have X dataframe defined somewhere in your code
# X = ...

# Load the saved model
    lr = pickle.load(open('ML/nextgenmodel.sav', 'rb'))
    X=pd.read_csv("ML/your_file_path.csv")

    loc_index = np.where(X.columns==location)[0][0]
    
    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    print (lr.predict([x])[0])

        
    return lr.predict([x])[0]

#predict("Chikka Tirupathi", 3200, 3,4)

