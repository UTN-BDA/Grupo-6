import unittest
from flask import current_app
from app.models import Room
from app import create_app, db
from app.services import RoomService

room_service = RoomService()

class RoomTestCase(unittest.TestCase):
  
    def setUp(self):
        self.NAME_PRUEBA = 'SALA AZUL'
        self.NUMBER_PRUEBA = "1"
        self.SEATSNUMBER_PRUEBA = "80"

        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_room(self):
        
        room = self.__get_room()

        self.assertTrue(room.name, self.NAME_PRUEBA)
        self.assertTrue(room.number, self.NUMBER_PRUEBA)
        self.assertTrue(room.seatsnumber, self.SEATSNUMBER_PRUEBA)

    def test_room_save(self):
        
        room = self.__get_room()
        room_service.save(room)
        
        self.assertGreaterEqual(room.id, 1)
        self.assertTrue(room.name, self.NAME_PRUEBA)
        self.assertTrue(room.number, self.NUMBER_PRUEBA)
        self.assertTrue(room.seatsnumber, self.SEATSNUMBER_PRUEBA)
    
    def test_room_delete(self):
        
        room = self.__get_room()
        room_service.save(room)

        room_service.delete(room.id)
        self.assertIsNone(room_service.find(room))

    def test_room_all(self):
        
        room = self.__get_room()
        room_service.save(room)

        rooms = room_service.all()
        self.assertGreaterEqual(len(rooms), 1)
    
    def test_room_find(self):
        
        room = self.__get_room()
        room_service.save(room)

        room_find = room_service.find(1)
        self.assertIsNotNone(room_find)
        self.assertEqual(room_find.id, room.id)
        self.assertEqual(room_find.name, room.name)

    def __get_room(self):
        
        room = Room()
        room.name = self.NAME_PRUEBA
        room.number = self.NUMBER_PRUEBA
        room.seatsnumber = self.SEATSNUMBER_PRUEBA

        return room

if __name__ == '__main__':
    unittest.main()