# Project 2: Rock vs Mine Classification

## Description
This project uses **Logistic Regression** to classify a given sample as either a **rock** or a **mine**. It demonstrates a simple binary classification workflow including data preparation, training, and prediction.

## Purpose
- Apply Logistic Regression for binary classification.
- Understand how feature values influence the classification outcome.
- Practice splitting datasets into training and testing sets, training a model, and evaluating predictions.

## Usage
1. Prepare your dataset with features and labels (`R` for Rock, `M` for Mine).  
2. Split the dataset into training and testing sets using `train_test_split`.  
3. Train the Logistic Regression model:
    ```python
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    ```
4. Make predictions:
    ```python
    prediction = model.predict(sample_features)
    if prediction[0] == 'R':
        print('The object is a rock')
    else:
        print('The object is a mine')
    ```

## Example Output
The object is a rock


## Dependencies
- Python 3.x
- scikit-learn
- numpy
