from declareAppApi import *

from logics.calc import calc
from numpy import real as Re
from numpy import imag as Im

@app.get("/calc")
def calc_by_your_model(independentVariables:str="x,y", yourModel:str="x+sin(y)", yourInputValues:str="1,2"):
    result = calc(independentVariables, yourModel, yourInputValues)
    res = {"result":{
        "real":Re(result),
        "imaginary":Im(result),
    }}
    print(res)
    return res