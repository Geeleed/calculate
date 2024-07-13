# uvicorn main:app --port 8000 --reload

from declareAppApi import *

@app.get("/")
def root():
    return "connection ok. You can use api in /docs page."

from apis.calc import *

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)