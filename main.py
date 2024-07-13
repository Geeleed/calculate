# uvicorn main:app --port 8000 --reload --host 0.0.0.0

from declareAppApi import *

@app.get("/")
def root():
    # return "connection ok. You can use api in /docs page."
    return FileResponse("index.html")

from apis.calc import *

if __name__ == '__main__':
    import uvicorn
    # uvicorn.run(app)
    uvicorn.run(app,host="0.0.0.0")