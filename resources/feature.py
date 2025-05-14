
from flask import Blueprint, request
from app.mapping import ResponseSchema, FeatureSchema
from app.services.response_message import ResponseBuilder
from app.services.feature_services import FeatureService

feature = Blueprint('feature', __name__)
feature_schema = FeatureSchema()
response_schema = ResponseSchema()
feature_service = FeatureService()
response_builder = ResponseBuilder()


# Mostrar todas las funciones
@feature.route('/features', methods=['GET'])
def index():
    return {"features": feature_schema.dump(feature_service.all(),many=True)}, 200 #, 200 es el código de respuesta si todo funciona bien

# Obtener funcion por ID
@feature.route('/features/<int:id>', methods=['GET'])
def find(id:int):
    response_builder.add_message("Funcion encontrada").add_status_code(100).add_data(feature_schema.dump(feature_service.find(id)))
    return response_schema.dump(response_builder.build()), 200

# Añadir Funcion
@feature.route('/features/add', methods=['POST'])
def post_feature():
    feature = feature_schema.load(request.json) 
    return {"feature": feature_schema.dump(feature_service.save(feature))}, 201


# Actualizar funcion
@feature.route('/features/<int:id>', methods=['PUT'])
def update_feature(id:int):
    feature = feature_schema.load(request.json)
    response_builder.add_message("Funcion actualizada").add_status_code(100).add_data(feature_schema.dump(feature_service.update(feature, id)))
    return response_schema.dump(response_builder.build()), 200


# Eliminar feature por id

@feature.route('/features/<int:id>', methods=['DELETE'])
def delete_feature(id):
    feature_service.delete(id)
    response_builder.add_message("Funcion borrada").add_status_code(100).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 200