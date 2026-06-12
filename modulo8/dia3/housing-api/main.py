import joblib
import numpy as np
import sklearn
from fastapi import FastAPI
from pydantic import BaseModel, Field

model = joblib.load('./model/model.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

app = FastAPI()

#schema validador
class Housing(BaseModel):
    rooms: int
    
@app.get("/")
def home():
    return {"message":"Housing API"}

@app.post("/housing_price")
def housing_price(housing: Housing):
    rooms = housing.rooms
    rooms_sc = sc_x.transform(np.array([[rooms]]))
    prediction_sc = model.predict(rooms_sc)
    prediction = sc_y.inverse_transform(prediction_sc) * 10000 
    price = round(prediction[0][0],2)
    
    return{
        "rooms": rooms,
        "price": price
    }
    
