from typing import List
from app.models import Room
from app import db

class RoomRepository:

    def save(self, room: Room) -> Room:
        db.session.add(room) 
        db.session.commit()
        return room
    
    def update(self, room: Room, id: int) -> Room:
        entity = self.find(id)
        entity.name = room.name
        entity.number = room.number
        entity.seatsnumber = room.seatsnumber
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, room: Room) -> None:
        db.session.delete(room)
        db.session.commit()

    def all(self) -> List[Room]:
        rooms = db.session.query(Room).all()
        return rooms
    
    def find(self, id: int) -> Room:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Room).filter(Room.id == id).one()
        except:
            return None
    
    def find_by_name(self, name: str):
        return db.session.query(Room).filter(Room.name == name).one_or_none()
    
    def find_by_number(self, number: int) -> list[Room]:
        return db.session.query(Room).filter(Room.number == number).one_or_none()

    