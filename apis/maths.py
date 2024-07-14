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

from logics.solve import nsolve

@app.get("/nsolve")
def numerical_solve_from_your_equation(yourEquation:str="x^3+1=0",yourInitialGuess:str="-2,2,-2j,-1j,2j"):
    result = nsolve(yourEquation,yourInitialGuess,method="broyden2")
    res = {
        "numOfSoln":len(result),
        "notice":"อาจมีผลเฉลยอื่นอีกหากเดาค่าได้ใกล้ผลเฉยจริงมากกว่านี้",
        "result":[]
        }
    for sol in result:
        res["result"].append({
            "Re":Re(sol),
            "Im":Im(sol),
        })
    print(res)
    return res