from fastapi import FastAPI
import redis

app = FastAPI()

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI with Redis!"}

@app.get("/cache/{key}")
async def read_cache(key: str):
    value = r.get(key)
    if value is None:
        return {"message": "Key not found"}
    return {"key": key, "value": value.decode('utf-8')}

@app.post("/cache/{key}/{value}")
async def write_cache(key: str, value: str):
    r.set(key, value)
    return {"message": "Value set", "key": key, "value": value}