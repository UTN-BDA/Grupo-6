
from flask import Blueprint, request
from app.mapping import ResponseSchema, MovieSchema
from app.services.response_message import ResponseBuilder
from app.services.movie_services import MovieService

movie = Blueprint('movie', __name__)
movie_schema = MovieSchema()
response_schema = ResponseSchema()
movie_service = MovieService()
response_builder = ResponseBuilder()

# Mostrar todas las peliculas
@movie.route('/movies', methods=['GET'])
def index():
    return {"movies": movie_schema.dump(movie_service.all(),many=True)}, 200 #, 200 es el código de respuesta si todo funciona bien

# Obtener película por ID
@movie.route('/movies/<int:id>', methods=['GET'])
def find(id:int):
    response_builder.add_message("Pelicula encontrada").add_status_code(100).add_data(movie_schema.dump(movie_service.find(id)))
    return response_schema.dump(response_builder.build()), 200

# Añadir pelicula
@movie.route('/movies/add', methods=['POST'])
def post_movie():
    movie = movie_schema.load(request.json) 
    return {"movie": movie_schema.dump(movie_service.save(movie))}, 201

# Actualizar película
@movie.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id:int):
    movie = movie_schema.load(request.json)
    response_builder.add_message("Película actualizada").add_status_code(100).add_data(movie_schema.dump(movie_service.update(movie, id)))
    return response_schema.dump(response_builder.build()), 200

 # Encontrar por nombre
 # los espacios en las url se escriben como '%20'
@movie.route('/movies/name/<name>', methods=['GET'])
def find_by_name(name:str):
    movie = movie_service.find_by_name(name)
    if movie is not None:
        response_builder.add_message("Película encontrada").add_status_code(100).add_data(movie_schema.dump(movie))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Película no encontrada").add_status_code(300).add_data({'name': name})
        return response_schema.dump(response_builder.build()), 404
    
# Eliminar película por id

@movie.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie_service.delete(id)
    response_builder.add_message("Película borrada").add_status_code(100).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 200