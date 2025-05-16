from app.models.ticket import Ticket
from marshmallow import fields, Schema, post_load

class TicketSchema(Schema):
    id = fields.Integer(dump_only=True)
    movie = fields.String(required=True)
    price = fields.Integer(required=True)
    date = fields.String(required=True)
    hour = fields.Integer(required=True)
    feature_id = fields.Integer(required=True)

    @post_load
    def make_ticket(self, data, **kwargs):
        return Ticket(**data)