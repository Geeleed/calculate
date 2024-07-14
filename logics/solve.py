from scipy.optimize import root
from numpy import round
from logics.calc import text

def nsolve(
    yourEquation:str = "2*x+x^2=5",
    yourInitialGuess:str = "-5,2",
    method:str="broyden2" #  hybr, lm, broyden1, broyden2, anderson, linearmixing, diagbroyden, excitingmixing, krylov, df-sane 
):
    initialGuess = [complex(x) for x in yourInitialGuess.split(",")]
    t = text(yourEquation)
    t.rev("^","**")
    left,right = t.text.split("=")
    root_text = f"lambda x:{left}-({right})" # F(x) = 0
    root_func = eval(root_text)
    soln = set()
    for guess in initialGuess:
        sol = root(root_func,guess,method=method)
        if sol.success:
            print(sol)
            soln.add(complex(round(sol.x,4)))
            print("------------------------")

    return list(soln)
# print(nsolve(yourEquation="2*x^2+3*x+1=0",yourInitialGuess="-1,3"))