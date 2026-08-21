import pandas as pd
import joblib
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

df = pd.read_csv("data/student-por.csv")

df["G1"] = (df["G1"]>10).astype(int)
df["G2"] = (df["G2"]>10).astype(int)
df["G3"] = (df["G3"]>10).astype(int)


categorical = ["school","sex","Pstatus","activities"]
numerical = ["studytime","failures","absences","G1","G2"]
preprocess = ColumnTransformer([("cat",OneHotEncoder(handle_unknown="ignore"),categorical),
                                ("num",StandardScaler(),numerical)])
pipeline = Pipeline([("preprocess",preprocess),
                     ("model",LogisticRegression())])

print(df.dtypes)

X = df[["school","sex","Pstatus","activities","studytime","failures","absences","G1","G2"]]
y = df["G3"]
X_train, X_test, y_train,y_test = train_test_split(X,y,random_state=42,test_size=0.2)

pipeline.fit(X_train,y_train)

joblib.dump(pipeline,"model.joblib")