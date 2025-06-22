import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts import (
    generate_feature,
    generate_ticket,
    generate_users,
    generate_movies,
    generate_profile,
    generate_roles,
    generate_rooms
)

if __name__ == '__main__':
    generate_movies.run()
    generate_rooms.run()
    generate_feature.run()
    generate_ticket.run()
    generate_profile.run(),
    generate_roles.run(),
    generate_users.run()
