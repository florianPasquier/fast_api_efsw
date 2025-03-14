from fastapi import FastAPI
import pickle


app = FastAPI()

@app.get("/home")
def read_root():
    return {"Hello": "World"}


@app.get("/predict")
def predict():
    model = pickle.load(open("models/forest_model.pkl", "rb"))        
    prediction = model.predict()
    return {"prediction": prediction}
