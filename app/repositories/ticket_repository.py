from typing import List
from app.models import Ticket
from app import db
from sqlalchemy.exc import NoResultFound

class TicketRepository:
    def save(self, ticket: Ticket) -> Ticket:
        db.session.add(ticket)
        return ticket
    
    def update(self, ticket: Ticket, id: int) -> Ticket:
        entity = self.find(id)
        entity.movie = ticket.movie
        entity.price = ticket.price
        entity.date = ticket.date
        entity.hour = ticket.hour
   
        return entity
    
    def delete(self, ticket: Ticket) -> None:
        db.session.delete(ticket)

    def all(self) -> List[Ticket]:
        return db.session.query(Ticket).all() 
    
    def find(self, id: int) -> Ticket:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Ticket).filter(Ticket.id == id).one()
        except NoResultFound:
            return None
        
    
