from typing import List
from app.models import Room
from app.repositories import RoomRepository

repository = RoomRepository()

class RoomService:

    def save(self, room: Room) -> Room:
        return repository.save(room)
    
    def update(self, room: Room, id: int) -> Room:
        return repository.update(room, id)
    
    def delete(self, id: int) -> None:
        room = repository.find(id)
        repository.delete(room)
    
    def all(self) -> List[Room]:
        return repository.all()
    
    def find(self, id: int) -> Room:
        return repository.find(id)
    
    def find_by_name(self, name: str):
        return repository.find_by_name(name)
    
    def find_by_number(self, number: int):
        return repository.find_by_number(number)