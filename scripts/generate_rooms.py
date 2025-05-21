import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from faker import Faker
import logging
import random
from app import create_app, db
from app.models.room import Room

app = create_app()
app.app_context().push()
fake = Faker()
logger = logging.getLogger(__name__)

def run(n=10):
    logger.info(f"Creando {n} salas...")
    for _ in range(n):
        name = f"Sala {fake.word().capitalize()} {random.randint(1, 99)}"
        number = random.randint(1, 20)
        seats = random.choice([50, 100, 120, 150])
        room = Room(name=name, number=number, seatsnumber=seats)
        db.session.add(room)

    db.session.commit()
    logger.info(f"{n} salas creadas exitosamente.")

if __name__ == '__main__':
    run()
