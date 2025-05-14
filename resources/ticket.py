from flask import Blueprint, request
from app.mapping import ResponseSchema, TicketSchema
from app.services.response_message import ResponseBuilder
from app.services.ticket_services import TicketService

ticket = Blueprint('ticket', __name__)
ticket_schema = TicketSchema()
response_schema = ResponseSchema()
ticket_service = TicketService()
response_builder = ResponseBuilder()

# 5 métodos

# Mostrar todos los tickets
@ticket.route('/tickets', methods=['GET'])
def index():
    return {"tickets": ticket_schema.dump(ticket_service.all(),many=True)}, 200

# Guardar ticket
@ticket.route('/tickets/add', methods=['POST'])
def post_ticket():
    ticket = ticket_schema.load(request.json) 
    return {"ticket": ticket_schema.dump(ticket_service.save(ticket))}, 201

# Actualizar ticket por id
@ticket.route('/tickets/<int:id>', methods=['PUT'])
def update_ticket(id:int):
    ticket = ticket_schema.load(request.json)
    response_builder.add_message("Ticket actualizado").add_status_code(100).add_data(ticket_schema.dump(ticket_service.update(ticket, id)))
    return response_schema.dump(response_builder.build()), 200

# Obtener ticket por id
@ticket.route('/tickets/<int:id>', methods=['GET'])
def find(id:int):
    response_builder.add_message("Ticket encontrado").add_status_code(100).add_data(ticket_schema.dump(ticket_service.find(id)))
    return response_schema.dump(response_builder.build()), 200

# Borrar ticket
@ticket.route('/tickets/<int:id>', methods=['DELETE'])
def delete_ticket(id):
    ticket_service.delete(id)
    response_builder.add_message("Ticket borrado").add_status_code(100).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 200
