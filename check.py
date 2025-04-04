from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

def check_mongo_connection():
    try:
        client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=1000)
        db = client["userlogs"]  # Connect to the database named "FAS"
        
        # Check if the collection exists
        print(db.list_collection_names())
        if db.list_collection_names():
            return True
        else:
            return False
    except Exception:
        return False

@app.get("/check-mongo")
def check_mongo():
    if check_mongo_connection():
        return {"status": "MongoDB is running"}
    else:
        return {"status": "MongoDB is down"}, 500  # FastAPI handles status codes differently

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)