from fastapi import FastAPI
import random

app= FastAPI()

@app.get('/')
async def root():
    return {'example': 'this is an example', 'data':69}


# uvicorn main:app --reload     
# to write in terminal to start server and generate your own dns 



# to generate random number between 100
@app.get('/random')
async def get_random():
    rn: int = random.randint(0,100)
    return{'number':rn , 'limit':100}


# limit will be given by user
@app.get('/random/{limit}')
async def get_random(limit: int):
    rn: int = random.randint(0,limit)
    return{'number':rn , 'limit':limit}



