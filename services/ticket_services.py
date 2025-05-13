from typing import List
from app.models import Ticket
from app.repositories import TicketRepository

repository = TicketRepository()

class TicketService:

    def save(self, ticket: Ticket) -> Ticket:
        return repository.save(ticket)
    
    def update(self, ticket: Ticket, id: int) -> Ticket:
        return repository.update(ticket, id)

    def delete(self, id: int) -> None:
        ticket = repository.find(id)
        repository.delete(ticket)

    def all(self) -> List[Ticket]:
        return repository.all()
    
    def find(self, id: int) -> Ticket:
        return repository.find(id)