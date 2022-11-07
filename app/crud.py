from sqlalchemy.orm import Session
from app.models import Place


def create_address(db:Session, latitude, longitude):
    """
    function to create a address model object
    """
    # create Place instance 
    new_address = Place(latitude=latitude, longitude=longitude)
    #place object in the database session
    db.add(new_address)
    #commit your instance to the database
    db.commit()
    #reefresh the attributes of the given instance
    db.refresh(new_address)
    return new_address


def get_address(db:Session, id:int):
    """
    get the first record with a given id, if no such record exists, will return null
    """
    db_address = db.query(Place).filter(Place.id==id).first()
    return db_address

def retrieve_address(db:Session, latitude, longitude):
    """
    get the first record with a given latitude and longitude, if no such record exists, will return null
    """
    db_address = db.query(Place).filter(Place.latitude==latitude,Place.longitude==longitude).all()
    return db_address




def update_address(db:Session, id:int, latitude: int, longitude: int):
    """
    Update a Place object's attributes
    """
    db_address = get_address(db=db, id=id)
    db_address.latitude = latitude
    db_address.longitude = longitude
    db.commit()
    db.refresh(db_address) #refresh the attribute of the given instance
    return db_address

def delete_address(db:Session, id:int):
    """
    Delete a Place object
    """
    db_address = get_address(db=db, id=id)
    db.delete(db_address)
    db.commit() #save changes to db