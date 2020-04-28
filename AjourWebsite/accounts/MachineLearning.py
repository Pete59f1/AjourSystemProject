from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Add data here
# In X the data means weight, height and length
# In y 0 means cat, 1 means dog
X = [[5, 15, 30], [30, 50, 100], [9.5, 15, 35], [20, 20, 40], [10.9, 20, 15],
     [35, 60, 70], [7, 12, 30], [15, 20, 20], [9, 30, 50], [50, 100, 150]]
y = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

# Turning our data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=4)

# Creating and training model
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Getting model score
predictions = classifier.predict(X_test)
print(accuracy_score(y_test, predictions))


class ML:

     @staticmethod
     def predict(x):
          return classifier.predict(x)
