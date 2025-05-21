import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from faker import Faker
import logging
from datetime import datetime, timedelta
import random
from app import create_app, db
from app.models.feature import Feature
from app.models.movie import Movie
from app.models.room import Room

app = create_app()
app.app_context().push()
fake = Faker()
logger = logging.getLogger(__name__)

def run(n=30):
    logger.info(f"Creando {n} funciones...")
    
    movies = Movie.query.all()
    rooms = Room.query.all()

    if not movies:
        logger.warning("No hay películas en la base de datos. Aborta la creación de funciones.")
        return
    if not rooms:
        logger.warning("No hay salas en la base de datos. Aborta la creación de funciones.")
        return

    for _ in range(n):
        start = fake.date_time_between(start_date='-30d', end_date='now')
        end = start + timedelta(hours=2)

        movie = random.choice(movies)
        room = random.choice(rooms)

        feature = Feature(date_from=start, date_to=end, movie_id=movie.id, room_id=room.id)
        db.session.add(feature)

    db.session.commit()
    logger.info(f"{n} funciones creadas exitosamente.")

if __name__ == '__main__':
    run()
