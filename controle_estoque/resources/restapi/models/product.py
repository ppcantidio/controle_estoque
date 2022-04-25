from controle_estoque.extensions.database import db
from controle_estoque.extensions.serializer import ma


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.Numeric())
    description = db.Column(db.Text)


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
