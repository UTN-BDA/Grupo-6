from app.models.feature import Feature
from marshmallow import fields, Schema, post_load

class FeatureSchema(Schema):
    id = fields.Integer(dump_only=True)
    date_from = fields.DateTime(required=True)
    date_to = fields.DateTime(required=True)
    movie_id = fields.Integer(required=True)
    room_id = fields.Integer(required=True)

    @post_load
    def make_feature(self, data, **kwargs):
        return Feature(**data)