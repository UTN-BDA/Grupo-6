import os
import sys
# Path para que Flask pueda importar
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 

import logging
from faker import Faker
from random import randint, choice
from datetime import datetime, timedelta
from app import create_app, db
from app.models.movie import Movie

app = create_app()
logger = logging.getLogger(__name__)

faker = Faker()

def limitar(texto, max_len):
    return texto[:max_len]

def generar_peliculas(n=3000):
    with app.app_context():
        logger.info(f"Generando {n} películas...")
        peliculas = []
        for i in range(n):
            start_date = faker.date_time_between(start_date='-1y', end_date='now')
            final_date = start_date + timedelta(weeks=randint(1, 6))

            pelicula = Movie(
                name=limitar(faker.sentence(nb_words=3), 80),
                director=limitar(faker.name(), 80),
                year=randint(1980, datetime.now().year),
                start_date=start_date,
                final_date=final_date,
                duration=randint(80, 180),
                description=limitar(faker.text(max_nb_chars=180), 200),
                genre=limitar(choice(['Drama', 'Comedia', 'Acción', 'Terror', 'Romance', 'Ciencia Ficción']), 80),
                classification=limitar(choice(['ATP', '13+', '16+', '18+']), 80),
                cast=limitar(', '.join(faker.name() for _ in range(randint(2, 4))), 80),
                language=limitar(choice(['Español', 'Inglés', 'Francés', 'Alemán', 'Japonés']), 80)
            )
            peliculas.append(pelicula)

            if i % 500 == 0:
                logger.info(f"{i} películas generadas...")

        db.session.bulk_save_objects(peliculas)
        db.session.commit()
        logger.info(f"{n} películas insertadas correctamente.")

def run():
    generar_peliculas()

if __name__ == "__main__":
    run()
