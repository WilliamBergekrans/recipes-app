from server import db
from server.models import Recipe

db.drop_all()
db.create_all()

lasagne = Recipe(
    name="Lasagne",
    description="En god och smörig lasagne för alla åldrar. Godare kan det inte bli!"
)

db.session.add(lasagne)
db.session.commit()
