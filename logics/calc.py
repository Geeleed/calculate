from numpy import \
    pi,\
    sin,cos,tan,\
    arcsin,arccos,arctan,\
    sinh,cosh,tanh,\
    arcsinh,arccosh,arctanh,\
    sinc,sign,abs,\
    log,log10,\
    exp,\
    sqrt,\
    ceil,floor,round

class text:
    def __init__(self, text:str):
        self.text = text
    def rev(self,FROM:str,TO:str):
        self.text = self.text.replace(FROM,TO)

def calc(independentVariables:str, yourModel:str, yourInputValues:str)->complex:
    # independentVariables = input("independentVariables (example x,y,z) ")
    # yourModel = input("your function (example x^2+y*log(z)) ")
    f = text(yourModel)
    f.rev("^","**")
    text_func = f"lambda {independentVariables}:{f.text}"
    func = eval(text_func)
    # yourInputValues = input("yourInputValues (example 2,4,5) ")
    inputParam = [complex(x) for x in yourInputValues.split(",")]
    output = func(*inputParam)
    return output

# if __name__=='__main__':
    # print(cal("x,y,z","x^2+y*log(z)","2,4,5")+5)
    