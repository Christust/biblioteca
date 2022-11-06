from django_seed import Seed
from apps.libro.models import Autor

def seed_autor():
    seeder = Seed.seeder()
    seeder.add_entity(Autor, 5)
    print(seeder.execute())