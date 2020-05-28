import uvicorn
from fastapi import FastAPI
from fastapi.params import Form
from pydantic import BaseModel

#创建一个fastApi实例
app=FastAPI()


#接收参数
class Item(BaseModel):
    username:str
    password:str



@app.post("/login")
def login(username:str=Form("userName"),password:str=Form("passWord")):
    return {"userName":username, "passWord": password}


@app.get("/")
async def index():
    return "helloworld!"

if __name__ == '__main__':
    uvicorn.run(app,host="0.0.0.0", port=8000)