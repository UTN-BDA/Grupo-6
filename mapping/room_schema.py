from app.models.room import Room
from marshmallow import fields, Schema, post_load

class RoomSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    number = fields.Integer(required=True)
    seatsnumber = fields.Integer(required=True)

    @post_load
    def make_room(self, data, **kwargs):
        return Room(**data)