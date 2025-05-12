import unittest
from flask import current_app
from app.models import Ticket
from app import create_app, db
from app.services import TicketService

ticket_service = TicketService()

class TicketTestCase(unittest.TestCase):
    def setUp(self):
        self.MOVIE_PRUEBA = 'Kimi No Nawa'
        self.PRICE_PRUEBA = '150'
        self.DATE_PRUEBA = '28/05/2024'
        self.HOUR_PRUEBA = '2'
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

    def test_ticket(self):

        ticket = self.__get_ticket()

        self.assertTrue(ticket.movie, self.MOVIE_PRUEBA)
        self.assertTrue(ticket.price, self.PRICE_PRUEBA)
        self.assertTrue(ticket.date, self.DATE_PRUEBA)
        self.assertTrue(ticket.hour, self.HOUR_PRUEBA)

    def test_ticket_save(self):

        ticket = self.__get_ticket()

        ticket_service.save(ticket)

        self.assertGreaterEqual(ticket.id, 1)
        self.assertTrue(ticket.movie, self.MOVIE_PRUEBA)
        self.assertTrue(ticket.price, self.PRICE_PRUEBA)
        self.assertTrue(ticket.date, self.DATE_PRUEBA)
        self.assertTrue(ticket.hour, self.HOUR_PRUEBA)

    def test_ticket_delete(self):
        
        ticket = self.__get_ticket()

        ticket_service.save(ticket)

        ticket_service.delete(ticket.id)
        self.assertIsNone(ticket_service.find(ticket))

    def test_ticket_all(self):
        
        ticket = self.__get_ticket()
        ticket_service.save(ticket)

        tickets = ticket_service.all()
        self.assertGreaterEqual(len(tickets), 1)

    def test_ticket_find(self):
        
        ticket = self.__get_ticket()
        ticket_service.save(ticket)

        ticket_find = ticket_service.find(1)
        self.assertIsNotNone(ticket_find)
        self.assertEqual(ticket_find.id, ticket.id)
        self.assertEqual(ticket_find.movie, ticket.movie)
        # se puede usar el metodo movie_find.name ?????????????

    def __get_ticket(self):
        
        ticket = Ticket()
        ticket.movie = self.MOVIE_PRUEBA
        ticket.price = self.PRICE_PRUEBA
        ticket.date = self.DATE_PRUEBA
        ticket.hour = self.HOUR_PRUEBA
       
        return ticket

if __name__ == '__main__':
    unittest.main()
