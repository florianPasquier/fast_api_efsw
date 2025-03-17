from fastapi import FastAPI
import pickle


app = FastAPI()

@app.get("/home")
def read_root():
    return {"Hello": "World"}


@app.get("/predict")
def predict(pickup_time: str
            , dropoff_time: str
            # , petal_width: float
            # , sepal_length: float
            # , sepal_width: float
            ):
    
    
    model = pickle.load(open("models/forest_model.pkl", "rb"))
    # prediction = model.predict([[petal_length, petal_width, sepal_length, sepal_width]])
    prediction = model.predict(pickup_time, dropoff_time)
    return {"prediction": prediction[0]}
