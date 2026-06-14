import os, zipfile, glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve, confusion_matrix, ConfusionMatrixDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from xgboost import XGBClassifier

RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# Exercise 1 - Exploratory Data Analysis

zip_path = r"C:\Users\gabri\Downloads\Heart Disease Prediction Dataset.zip"
extract_dir = r"C:\Users\gabri\Downloads\heart_dataset"

zipfile.ZipFile(zip_path).extractall(extract_dir)

csv_files = []

for root, dirs, files in os.walk(extract_dir):
    for file in files:
        if file.endswith(".csv"):
            csv_files.append(os.path.join(root, file))

print("CSV files found:")
for file in csv_files:
    print(file)

# Choose the first CSV file
csv_path = csv_files[0]

df = pd.read_csv(csv_path)

target = 'heart disease'
df.columns = df.columns.str.strip()

x = df.drop(columns=[target])
y = df[target]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

categorical_cols = x.select_dtypes(include='object').columns
numerical_cols = x.select_dtypes(include=['int64', 'float64']).columns

df[numerical_cols].hist(figsize=(15,10), bins=20)
plt.show()

df[target].value_counts().plot(kind='bar')
plt.title('Class Distribution (Heart Disease)')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()

pre = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ]
)

def eval_and_report(name, model, x, y_test):
    """Compute metrics and draw confusion matrix and ROC if available."""

    # Predictions
    y_pred = model.predict(x_test)

    # Metrics
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='weighted'),
        'recall': recall_score(y_test, y_pred, average='weighted'),
        'f1': f1_score(y_test, y_pred, average='weighted'),
    }

    print(name, metrics)

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.title(f"{name} - Confusion Matrix")
    plt.show()

    # ROC Curve (only if model supports probabilities)
    if hasattr(model, "predict_proba"):
        y_proba = model.predict_proba(x_test)[:, 1]

        fpr, tpr, _ = roc_curve(y_test, y_proba)
        auc_score = roc_auc_score(y_test, y_proba)

        plt.plot(fpr, tpr, label=f"AUC = {auc_score:.2f}")
        plt.plot([0, 1], [0, 1], "--")

        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title(f"{name} - ROC Curve")
        plt.legend()
        plt.show()

    return metrics

# Exercise 2 - Logistic Regression without Grid Search
pipe_lr = Pipeline(steps=[
    ('preprocessor', pre),
    ('model', LogisticRegression(solver='liblinear', max_iter=1000))
])

pipe_lr.fit(x_train, y_train)

lr_no_gs_metrics = eval_and_report(
    "Logistic Regression",
    pipe_lr,
    x_test,
    y_test
)

# Exercise 3 - Logistic Regression with Grid Search
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

pipe_lr_cv = Pipeline(steps=[
    ('preprocessor', pre),
    ('lr', LogisticRegression(solver='liblinear', max_iter=1000))
])

param_grid = {
    'lr__C': [0.01, 0.1, 1, 10, 100],
    'lr__penalty': ['l1', 'l2']
}

from sklearn.model_selection import GridSearchCV

grid_lr = GridSearchCV(
    estimator=pipe_lr_cv,
    param_grid=param_grid,
    cv=5,
    scoring='f1'
)

grid_lr.fit(X_train, y_train)

print("Best params:", grid_lr.best_params_)
best_lr = grid_lr.best_estimator_

lr_gs_metrics = eval_and_report(
    "LR GridSearch",
    best_lr,
    X_test,
    y_test
)

# Exercise 4 - SVM without Grid Search
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

pipe_svm = Pipeline(steps=[
    ('preprocessor', pre),
    ('svm', SVC(kernel='rbf', C=1.0, gamma='scale', probability=True))
])

pipe_svm.fit(X_train, y_train)

svm_metrics = eval_and_report(
    "SVM (RBF)",
    pipe_svm,
    X_test,
    y_test
)

# Exercise 5 - SVM with Grid Search
pipe_svm_cv = Pipeline(steps=[
    ('preprocessor', pre),
    ('svm', SVC(probability=True))
])

svm_param_grid = {
    'svm__kernel': ['rbf', 'linear'],
    'svm__C': [0.1, 1, 10, 100],
    'svm__gamma': ['scale', 'auto']
}

grid_svm = GridSearchCV(
    estimator=pipe_svm_cv,
    param_grid=svm_param_grid,
    cv=5,
    scoring='f1'
)

grid_svm.fit(X_train, y_train)

print("Best params:", grid_svm.best_params_)

best_svm = grid_svm.best_estimator_

svm_gs_metrics = eval_and_report(
    'SVM GridSearch',
    best_svm,
    X_test,
    y_test
)

# Exercise 6 : XGBoost without Grid Search
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier

pipe_xgb = Pipeline(steps=[
    ('preprocessor', pre),
    ('xgb', XGBClassifier(
        n_estimators=300,
        learning_rate=0.1,
        max_depth=4,
        random_state=RANDOM_STATE
    ))
])

pipe_xgb.fit(X_train, y_train)

xgb_no_metrics = eval_and_report(
    'XGB no grid',
    pipe_xgb,
    X_test,
    y_test
)

#  Exercise 7 : XGBoost with Grid Search
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier

pipe_xgb_cv = Pipeline([
    ('preprocessor', pre),
    ('xgb', XGBClassifier(
        random_state=RANDOM_STATE
    ))
])

xgb_param_grid = {
    'xgb__n_estimators': [100, 300, 500],
    'xgb__learning_rate': [0.01, 0.05, 0.1],
    'xgb__max_depth': [3, 4, 5]
}

grid_xgb = GridSearchCV(
    estimator=pipe_xgb_cv,
    param_grid=xgb_param_grid,
    cv=5,
    scoring='f1'
)

grid_xgb.fit(X_train, y_train)

print("Best params:", grid_xgb.best_params_)

best_xgb = grid_xgb.best_estimator_

xgb_gs_metrics = eval_and_report(
    'XGB Grid',
    best_xgb,
    X_test,
    y_test
)