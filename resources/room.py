from flask import Blueprint, request
from app.mapping import ResponseSchema, RoomSchema
from app.services.response_message import ResponseBuilder
from app.services.room_services import RoomService

room = Blueprint('room', __name__)
room_schema = RoomSchema()
response_schema = ResponseSchema()
room_service = RoomService()
response_builder = ResponseBuilder()

# Mostrar todas las salas
@room.route('/rooms', methods=['GET'])
def index():
    return {"rooms": room_schema.dump(room_service.all(),many=True)}, 200

# Obtener sala por ID
@room.route('/rooms/<int:id>', methods=['GET'])
def find(id:int):
    response_builder.add_message("Sala encontrada").add_status_code(100).add_data(room_schema.dump(room_service.find(id)))
    return response_schema.dump(response_builder.build()), 200

# Añadir sala
@room.route('/rooms/add', methods=['POST'])
def post_room():
    room = room_schema.load(request.json) 
    return {"room": room_schema.dump(room_service.save(room))}, 201

# Actualizar sala
@room.route('/rooms/<int:id>', methods=['PUT'])
def update_room(id:int):
    room = room_schema.load(request.json)
    response_builder.add_message("Sala actualizada").add_status_code(100).add_data(room_schema.dump(room_service.update(room, id)))
    return response_schema.dump(response_builder.build()), 200

# Encontrar sala por nombre
@room.route('/rooms/name/<name>', methods=['GET'])
def find_by_name(name:str):
    room = room_service.find_by_name(name)
    if room is not None:
        response_builder.add_message("Sala encontrada").add_status_code(100).add_data(room_schema.dump(room))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Sala no encontrada").add_status_code(300).add_data({'name': name})
        return response_schema.dump(response_builder.build()), 404
    
# Encontrar por número
@room.route('/rooms/number/<int:number>', methods=['GET'])
def find_by_number(number:int):
    room = room_service.find_by_number(number)
    if room is not None:
        response_builder.add_message("Sala encontrada").add_status_code(100).add_data(room_schema.dump(room_service.find_by_number(number)))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Sala no encontrada").add_status_code(300).add_data({'number': number})
        return response_schema.dump(response_builder.build()), 404
    
# Eliminar sala por id
@room.route('/rooms/<int:id>', methods=['DELETE'])
def delete_room(id):
    room_service.delete(id)
    response_builder.add_message("Sala borrada").add_status_code(100).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 200