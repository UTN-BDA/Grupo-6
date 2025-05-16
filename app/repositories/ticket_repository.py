from typing import List
from app.models import Ticket
from app import db

class TicketRepository:
    def save(self, ticket: Ticket) -> Ticket:
        db.session.add(ticket)
        db.session.commit()
        return ticket
    
    def update(self, ticket: Ticket, id: int) -> Ticket:
        entity = self.find(id)
        entity.movie = ticket.movie
        entity.price = ticket.price
        entity.date = ticket.date
        entity.hour = ticket.hour
   
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, ticket: Ticket) -> None:
        db.session.delete(ticket)
        db.session.commit()

    def all(self) -> List[Ticket]:
        tickets = db.session.query(Ticket).all()
        return tickets
    
    def find(self, id: int) -> Ticket:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Ticket).filter(Ticket.id == id).one()
        except:
            return None
        
    
