from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "RubinOT Bazaar Tracker API online"}


@app.get("/health")
def health_check():
    return {"status": "ok"}