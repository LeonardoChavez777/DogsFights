from fastapi import FastAPI
import routers.dogs
import routers.fights


app = FastAPI()

app.include_router(routers.dogs.router)
app.include_router(routers.fights.router)

@app.get("/")
def read_root():
    return {"Hello": "pelea de perros application!"}

