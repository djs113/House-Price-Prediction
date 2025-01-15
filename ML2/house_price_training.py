
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib


# In[20]:


df = pd.read_csv("Bengaluru_House_Data.csv")
df.head()


# In[21]:


df.info()


# In[22]:


df['bath'].fillna(0, inplace=True)
df['price'].fillna(0, inplace=True)
df['balcony'].fillna(0, inplace=True)


# In[23]:


df.drop(['availability', 'society', 'location'], axis='columns', inplace=True)
df.head()


# In[24]:


df.info()


# In[25]:


maps = {}
def find_category_mappings(df, variable):
    return {k: i for i, k in enumerate(df[variable].unique())}

def integer_encode(df, variable, ordinal_mapping):
    df[variable] =  df[variable].map(ordinal_mapping)
    maps[variable] = mappings
    
for variable in df.columns:
    if df[variable].dtype == "object":
        mappings = find_category_mappings(df, variable)
        integer_encode(df, variable,  mappings)
        maps[variable] = mappings


# In[26]:


f=open('mapping.txt','w')
f.write(str(maps))
f.close()


# In[27]:


df1 = df
df1


# In[28]:


X = df1.iloc[:,:-1]
X.head()


# In[29]:


y = df1['price']
y.head()


# In[30]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)


# In[31]:


# X_train['society'].fillna(0, inplace=True)
X_train.head()
# why we choose machine learning, algorithm used for our problem, why regressor algorithm is implemented in this problem and existing system, proposed system, future scope, data visualization purposes


# In[32]:


r = DecisionTreeRegressor()
r.fit(X_train, y_train)


# In[33]:


y_pred = r.predict(X_test)
y_pred


# In[34]:


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('mean_squared_error = ' + str(mse))

print('r2_score=' + str(r2))


# In[35]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(15, 5))

plt.scatter(x=y_test, y=y_pred)
plt.title('Actual vs. Predicted')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')

plt.text(max(y_test), min(y_pred), f'MSE: {mse:.2f}', ha='right', va='bottom', color='red')
plt.text(max(y_test), min(y_pred), f'R2: {r2:.2f}', ha='right', va='top', color='blue')

plt.show()


# In[36]:



from sklearn.linear_model import LinearRegression


# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model on the training set
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model performance
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')
# Calculate R-squared
r2LR = r2_score(y_test, predictions)
print('R-squared score:', r2LR)

# Plot the data and the regression line
plt.scatter(X_test, y_test, color='blue', label='Actual data')
plt.plot(X_test, predictions, color='red', linewidth=3, label='Regression line')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()


# In[ ]:





# In[37]:



deviations = np.abs(y_pred - y_test)

labels = ['Correct Predictions', 'Overpredictions', 'Underpredictions']
sizes = [
    np.sum(deviations == 0),
    np.sum(y_pred > y_test),
    np.sum(y_pred < y_test)
]
colors = ['lightgreen', 'coral', 'lightblue']
plt.figure(figsize=(8, 8))

plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Pie Chart - Deviations')
plt.text(0, 0, f'MSE: {mse:.2f}\nR2: {r2:.2f}', ha='center', va='center', color='black', fontsize=12)
plt.show()
plt.savefig('deviations_pie_chart.png')


# In[38]:


from sklearn.model_selection import GridSearchCV

# Define the parameter grid
param_grid = {
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Create the GridSearchCV object
grid_search = GridSearchCV(DecisionTreeRegressor(), param_grid, cv=5, scoring='r2')

# Fit the grid search to the data
grid_search.fit(X_train, y_train)

# Print the best parameters and best R-squared score
print("Best Parameters: ", grid_search.best_params_)
print("Best R-squared Score: ", grid_search.best_score_)


# In[39]:


# Access feature importances from the best estimator
feature_importances = grid_search.best_estimator_.feature_importances_


# In[40]:


joblib.dump(r, 'houses.joblib')


# In[41]:


df.iloc[2:3].to_csv('house.csv')
df.iloc[4:5].to_csv('house1.csv')
df.iloc[5:6].to_csv('house2.csv')

