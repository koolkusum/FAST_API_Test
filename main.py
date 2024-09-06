from fastapi import FastAPI
app = FastAPI()

# python -m uvicorn main:app --reload
@app.get("/")
async def root():
 return {"greeting":"Hello world"}
