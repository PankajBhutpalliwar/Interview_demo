
from fastapi import FastAPI
from app import models
from app.db import engine
from app.db import SessionLocal
from fastapi import Depends
from app import crud
import logging


# Create and configure logger
logging.basicConfig(filename="data.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

#create the database tables on app startup or reload
models.Base.metadata.create_all(bind=engine)
logger.info("Database created")

app = FastAPI()
@app.get("/")
def home():
    return {"Hello": "FastAPI_TEST"}

#database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#define endpoint
@app.post("/create_address")
def create_address(latitude:int, longitude:int, db:Session = Depends(get_db)):
    address = crud.create_friend(db=db, latitude=latitude, longitude=longitude)
##return object created
    return {"address": address}

#get/retrieve friend 
@app.get("/get_address/{id}/") #id is a path parameter
def get_address(id:int, db:Session = Depends(get_db)):
    address = crud.get_address(db=db, id=id)
    return address

@app.get("/retrieve_address")
def retrieve_address(latitude:int, longitude:int, db:Session = Depends(get_db)):
    address_list = crud.retrieve_address(db=db)
    return address_list

@app.put("/update_address/{id}/") #id is a path parameter
def update_address(id:int, latitude:str, longitude:str, age:int, db:Session=Depends(get_db)):
    #get Place object from database
    db_address = crud.get_address(db=db, id=id)
    #check if Place object exists
    if db_address:
        updated_address = crud.update_address(db=db, id=id, latitude=latitude, longitude=longitude)
        return updated_address
    else:
        logger.error("address doesnt exist")
        return {"error": f"address with id {id} does not exist"}

@app.delete("/delete_address/{id}/") #id is a path parameter
def delete_address(id:int, db:Session=Depends(get_db)):
    #get Place object from database
    db_address = crud.get_address(db=db, id=id)
    #check if Place object exists
    if db_address:
        return crud.delete_address(db=db, id=id)
    else:
        logger.error("address doesnt exist")
        return {"error": f"address with id {id} does not exist"}