import os
import sys
import logging
from faker import Faker
import random
from sqlalchemy import text
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models.user import User, UserData
from app.models.profile import Profile
from app.models.role import Role

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = create_app()
fake = Faker('es_ES')

def clear_users():
    logger.info("Eliminando usuarios anteriores...")
    try:
        db.session.query(UserData).delete(synchronize_session=False)
        db.session.query(User).delete(synchronize_session=False)
        db.session.execute(text('DELETE FROM users'))
        db.session.commit()
        logger.info("Usuarios eliminados correctamente.")
    except Exception as e:
        db.session.rollback()
        logger.error(f"Ocurrió un error al eliminar usuarios: {e}")

def generate_users(n=3000):
    logger.info(f"Generando {n} usuarios de prueba...")

    profiles = Profile.query.all()
    roles = Role.query.all()

    if not profiles or not roles:
        logger.warning("Debes cargar perfiles y roles antes de generar usuarios.")
        return
    
    existing_usernames = {u[0] for u in db.session.query(User.username).all()}

    for _ in range(n):
        for _ in range(10):  # Intentar hasta 10 veces encontrar un username único
            firstname = fake.first_name()
            lastname = fake.last_name()
            base_username = f"{firstname.lower()}.{lastname.lower()}"
            username = base_username

            counter = 1
            while username in existing_usernames:
                username = f"{base_username}{counter}"
                counter += 1

            if username not in existing_usernames:
                existing_usernames.add(username)
                break
        else:
            logger.warning("No se pudo generar un username único tras múltiples intentos.")
            continue
        email = fake.unique.email()
        password = "hashedpassword123"  # Simulación de password hasheado

        user_data = UserData(
            firstname=firstname,
            lastname=lastname,
            phone=fake.phone_number(),
            address=fake.address(),
            city=fake.city(),
            country=fake.country(),
            profile=random.choice(profiles)
        )

        user = User(
            username=username,
            password=password,
            email=email,
            data=user_data
        )

        # Asignar roles aleatorios
        assigned_roles = random.sample(roles, random.randint(1, len(roles)))
        for role in assigned_roles:
            user.add_role(role)

        db.session.add(user)

    db.session.commit()
    logger.info(f"Se generaron {n} usuarios correctamente.")

def run():
    with app.app_context():
        try:
            clear_users()
            generate_users(n=3000)
        except Exception as e:
            logger.error(f"Ocurrió un error al generar los usuarios: {e}")
            db.session.rollback()

if __name__ == '__main__':
    run()
