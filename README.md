# Student Pass/Fail Detection using FastAPI

A machine learning project that predicts whether a student will **Pass or Fail** based on academic and personal factors such as study time, failures, absences, and previous grades.

The trained machine learning model is integrated with **FastAPI** to provide predictions through a REST API.

## Project Overview

This project demonstrates how a machine learning model can be trained, saved, loaded, and deployed as an API.

### Workflow

```text
User Input
    ↓
FastAPI
    ↓
Input Validation
    ↓
Trained ML Model
    ↓
Prediction
    ↓
Pass / Fail Response
```

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* FastAPI
* Uvicorn
* Git & GitHub

## Project Structure

```text
student-pass-fail-api/
│
├── app.py
├── model.joblib
├── requirements.txt
├── README.md
└── .gitignore
```

### Files Description

| File               | Purpose                                         |
| ------------------ | ----------------------------------------------- |
| `app.py`           | FastAPI application and prediction endpoint     |
| `model.joblib`     | Saved trained machine learning model            |
| `requirements.txt` | Python dependencies required to run the project |
| `README.md`        | Project documentation                           |
| `.gitignore`       | Files that should not be uploaded to GitHub     |

## Machine Learning Model

The project uses a classification model to predict the student's result.

The model is trained using student-related features such as:

* Student pass/fail-related academic information
* Study time
* Number of failures
* Number of absences
* Previous grades

The trained model is saved using **Joblib**:

```python
joblib.dump(model, "model.joblib")
```

The saved model is loaded by the FastAPI application:

```python
model = joblib.load("model.joblib")
```

## API Endpoint

### POST `/predict`

This endpoint receives student information and returns the predicted result.

### Example Request

```json
{
    "school": "GP",
    "sex": "F",
    "pstatus": "T",
    "activities": "yes",
    "study_time": 0,
    "failures": 0,
    "absences": 0,
    "G1": 0,
    "G2": 0
}
```

### Example Response

```json
{
    "prediction": "Pass"
}
```

The prediction may be either:

```text
Pass
```

or

```text
Fail
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/kammarisrikar73/Student-P-F-status-using-FAST-API
```

### 2. Navigate to the project folder

```bash
cd student-pass-fail-api
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the FastAPI server

...bash
uvicorn app:app --reload
...

The API will run at:

'''text
http://127.0.0.1:8000
'''

## API Documentation

FastAPI automatically provides interactive API documentation.

Open:

--- text
http://127.0.0.1:8000/docs
--

From the Swagger UI, you can:

1. Open the `/predict` endpoint.
2. Click **Try it out**.
3. Enter student details.
4. Click **Execute**.
5. View the prediction.

## Testing

The API can be tested using:

* FastAPI Swagger UI
* Postman
* Python `requests`

Example using Python:

```python
import requests

data = {
    "school": "GP",
    "sex": "F",
    "pstatus": "T",
    "activities": "yes",
    "study_time": 0,
    "failures": 0,
    "absences": 0,
    "G1": 0,
    "G2": 0
}

response = requests.post(
    "http://127.0.0.1:8000/predict",
    json=data
)

print(response.json())
```

## Key Concepts Demonstrated

This project demonstrates:

- Machine Learning classification
- Data preprocessing
- Model training
- Model persistence using Joblib
- Loading a trained model
- FastAPI
- REST API
- HTTP POST requests
- JSON request and response
- Pydantic input validation
- API testing with Swagger/Postman

## Future Improvements

* Add a frontend using Streamlit or HTML/CSS/JavaScript
* Deploy the FastAPI application online
* Add model performance metrics
* Add more student features
* Improve prediction accuracy
* Add automated testing

## Author

**Srikar Kammari**

GitHub: `https://github.com/kammarisrikar73/Student-P-F-status-using-FAST-API`

---

If you found this project useful, consider giving the repository a star.
