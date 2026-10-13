# Student Pass/Fail Prediction using LightGBM and FastAPI

A machine learning project that predicts student academic outcomes using academic and personal features such as study time, previous grades, past failures, and absences. The trained LightGBM classification model is integrated with FastAPI to provide predictions through a REST API.

## Project Overview

This project demonstrates an end-to-end machine learning workflow, including data preprocessing, model training, model persistence, API integration, and prediction serving.

### Workflow

```text
Student Dataset
      ↓
Data Preprocessing
      ↓
LightGBM Model Training
      ↓
Save Model using Joblib
      ↓
FastAPI Application
      ↓
Input Validation
      ↓
Prediction Response
```

## Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- LightGBM
- Joblib
- FastAPI
- Uvicorn
- Git and GitHub

## Project Structure

```text
student-pass-fail-api/
│
├── app.py
├── model.py
├── model.joblib
├── requirements.txt
├── README.md
└── .gitignore
```

- `model.py` — Preprocesses the dataset, trains the LightGBM pipeline, and saves the trained model.
- `app.py` — Loads the saved model and exposes the prediction endpoint through FastAPI.
- `model.joblib` — Stores the trained preprocessing and prediction pipeline.
- `requirements.txt` — Lists the Python dependencies.
- `README.md` — Documents the project and setup instructions.
- `.gitignore` — Specifies files Git should ignore.

## Machine Learning Model

The project uses **LightGBM (`LGBMClassifier`)**, a gradient-boosting algorithm based on decision trees.

The model is integrated into a Scikit-learn pipeline that combines:

- `ColumnTransformer` for categorical and numerical feature preprocessing.
- `OneHotEncoder` for categorical features.
- `StandardScaler` for numerical features.
- `LGBMClassifier` for model training and prediction.

### Model Configuration

```python
LGBMClassifier(
    n_estimators=100,
    max_depth=3,
    learning_rate=0.1,
    random_state=42
)
```

The complete pipeline is trained and saved using Joblib:

```python
pipeline.fit(X_train, y_train)
joblib.dump(pipeline, "model.joblib")
```

The saved pipeline is loaded by the FastAPI application:

```python
model = joblib.load("model.joblib")
```

## API Endpoint

**POST `/predict`**

Accepts student information as JSON and returns a prediction.

### Example Request

```json
{
    "school": "GP",
    "sex": "F",
    "pstatus": "T",
    "activities": "yes",
    "study_time": 2,
    "failures": 0,
    "absences": 3,
    "G1": 12,
    "G2": 13
}
```

*Ensure that the request fields and allowed values match the input schema defined in `app.py`.*

### Example Response

```json
{
    "prediction": "Pass"
}
```

The response may be `"Pass"` or `"Fail"`, according to the prediction logic implemented in the application.

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/kammarisrikar73/Student-P-F-status-using-FAST-API.git
```

### 2. Navigate to the project directory

```bash
cd Student-P-F-status-using-FAST-API
```

### 3. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the FastAPI server

```bash
python -m uvicorn app:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

## API Documentation and Testing

Open the interactive Swagger documentation:

`http://127.0.0.1:8000/docs`

You can use Swagger UI or Postman to submit student details to the `/predict` endpoint and inspect the response.

## Key Concepts Demonstrated

- Classification using LightGBM
- Categorical and numerical data preprocessing
- Scikit-learn pipelines
- Model training and inference
- Model serialization using Joblib
- FastAPI REST API development
- JSON requests and responses
- Pydantic input validation
- API testing and integration

## Live Demo

Try the deployed application:

[Student Pass/Fail Prediction — Streamlit](https://student-p-f-status-using-fast-api-kvscuemethz3r4ycyobgzu.streamlit.app/)

## Author

**Srikar Kammari**

GitHub: [kammarisrikar73](https://github.com/kammarisrikar73)

If you find this project useful, consider giving the repository a star.

