from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

model = joblib.load("model.joblib")

class new(BaseModel):
    school:str
    sex:str
    Pstatus:str
    activities:str
    studytime:int
    failures:int
    absences:int
    G1:int
    G2:int

@app.get("/")
def home():
    return {"message":"API is running"}

@app.post("/predict")
def predict(data:new):
    new_df = pd.DataFrame({"school":data.school,
            "sex":[data.sex],
            "Pstatus":[data.Pstatus],
            "activities":[data.activities],
            "studytime":[data.studytime],
            "failures":[data.failures],
            "absences":[data.absences],
            "G1":[data.G1],
            "G2":[data.G2]})

    
    prediction = model.predict(new_df)
    if prediction[0] == 1:
        res = "Pass"
    else:
        res = "Fail"

    return {
        "prediction":res 
        }