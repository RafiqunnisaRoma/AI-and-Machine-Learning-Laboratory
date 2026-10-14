#Knn best k selection
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler



# 1. Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split dataset: 70% training, 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y)

# 3. Test different k values without scaling
result= {}
print('Accuracy  without Scaling : ')
for k in [1,3,5,7]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train,y_train)
    predictions = model.predict (X_test)
    accuracy = accuracy_score(y_test, predictions)
    result[k]= accuracy
    print(f"k={k} : {accuracy: 4f}")
#4. Select the best
best_k= max (result, key=result.get)
print("\nBest k:", best_k)
#5. Confusion matrix
best_model = KNeighborsClassifier(n_neighbors=best_k)
best_model.fit(X_train,y_train)
predictions = best_model.predict (X_test)

print("\nConfusion Matrix without scaling:")
print(confusion_matrix(y_test, predictions))

#6. Standarize
scaler= StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#7.Train and evaluate the best k
scaled_model= KNeighborsClassifier(n_neighbors=best_k)
scaled_model.fit(X_train_scaled, y_train)
scaled_predictions = scaled_model.predict (X_test_scaled)
scaled_accuracy = accuracy_score(y_test, scaled_predictions)

print('\nBest k after scaling: ',best_k)
print(f"Accuracy after scaling: {scaled_accuracy:.4f}")
print('\nConfusion Matrix After scaling:')
print(confusion_matrix(y_test, scaled_predictions))


