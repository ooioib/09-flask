# pip install flask
# pip install numpy
from datetime import datetime
from flask import Flask, request
import numpy as np

in_memory_db = []

app = Flask(__name__)
@app.get("/api/health" )
def health_handle() :

    return {"status" : True}

@app.post("/api/fruit")
def fruit_post_handle() :
    # print(request.json, type(request.json))
    one = {"name": request.json["name"], "create_at": datetime.now()}
    in_memory_db.append(one)
    return one, 201

@app.get("/api/fruit")
def fruit_get_handle() :
    return in_memory_db

@app.post("/api/numpy")
def numpy_handle() :
    a = np.array(request.json["data"])
    # return {"mean": np.mean(a), "max": np.max(a), "min": np.min(a) }
    return {"mean" : float(np.mean(a)), "max" : float(np.max(a)) , "min" : float(np.min(a)) }



