from typing import List
from app import db
from app.models import Ticket, Feature
from sqlalchemy.exc import NoResultFound
from app.repositories import TicketRepository

repository = TicketRepository()

class TicketService:

    def save(self, ticket: Ticket) -> Ticket:
        with db.session.begin():
            # Verificar que la Feature existe
            feature = db.session.query(Feature).filter(Feature.id == ticket.feature_id).one_or_none()
            if not feature:
                raise ValueError("La función (feature) no existe")

            # Verificar si quedan asientos disponibles en la sala
            room = feature.room
            cantidad_tickets = db.session.query(Ticket).filter(Ticket.feature_id == feature.id).count()

            if cantidad_tickets >= room.seatsnumber:
                raise ValueError("No hay más asientos disponibles")

            # Guardar el ticket si todo está bien
            db.session.add(ticket)
        return ticket
    
    def update(self, ticket: Ticket, id: int) -> Ticket:
        with db.session.begin():
            # Buscar el ticket existente
            existing_ticket = db.session.query(Ticket).filter(Ticket.id == id).one_or_none()
            if not existing_ticket:
                raise ValueError(f"Ticket con id {id} no existe")

            # Verificar que la Feature existe (por si cambia feature_id)
            feature = db.session.query(Feature).filter(Feature.id == ticket.feature_id).one_or_none()
            if not feature:
                raise ValueError("La función (feature) no existe")

            # Verificar si quedan asientos disponibles en la sala
            room = feature.room
            cantidad_tickets = db.session.query(Ticket).filter(Ticket.feature_id == feature.id).count()

            # Al actualizar, descontamos el ticket actual para no contar dos veces
            if cantidad_tickets >= room.seatsnumber and existing_ticket.feature_id != ticket.feature_id:
                raise ValueError("No hay más asientos disponibles")

            # Actualizar campos
            existing_ticket.movie = ticket.movie
            existing_ticket.price = ticket.price
            existing_ticket.date = ticket.date
            existing_ticket.hour = ticket.hour
            existing_ticket.feature_id = ticket.feature_id

            db.session.add(existing_ticket)
        return existing_ticket


    def delete(self, id: int) -> None:
        with db.session.begin():
            ticket = db.session.query(Ticket).filter(Ticket.id == id).one_or_none()
            if not ticket:
                raise ValueError(f"Ticket con id {id} no existe")
            db.session.delete(ticket)


    def all(self) -> List[Ticket]:
        return repository.all()
    
    def find(self, id: int) -> Ticket:
        return repository.find(id)