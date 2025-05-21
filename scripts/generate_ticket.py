import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from faker import Faker
from app import create_app, db
from app.models.ticket import Ticket
from app.models.feature import Feature
import logging
import random
from datetime import datetime

app = create_app()
app.app_context().push()
fake = Faker()
logger = logging.getLogger(__name__)

def run(n=3000):
    logger.info(f"Creando {n} tickets...")
    
    features = Feature.query.all()
    if not features:
        logger.warning("No hay funciones en la base de datos. Aborta la creación de tickets.")
        return

    for _ in range(n):
        feature = random.choice(features)
        movie_title = feature.movie.name if feature.movie else fake.sentence(nb_words=3)
        price = random.choice([1200, 1500, 2000, 2500])
        date = feature.date_from.strftime("%Y-%m-%d")
        hour = feature.date_from.hour

        ticket = Ticket(
            movie=movie_title,
            price=price,
            date=date,
            hour=hour,
            feature_id=feature.id
        )

        db.session.add(ticket)

    db.session.commit()
    logger.info(f"{n} tickets creados exitosamente.")

if __name__ == '__main__':
    run()
