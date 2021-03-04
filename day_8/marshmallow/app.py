from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", backref="books")


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
    books = ma.auto_field()


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        include_fk = True


db.create_all()

author_schema = AuthorSchema()
book_schema = BookSchema()

author = Author(name="Héctor García")
book1 = Book(title="Ikigai", author=author)
book2 = Book(title="idk", author=author)

db.session.add(author)
db.session.add(book1)
db.session.add(book2)
db.session.commit()

print(author_schema.dump(author))
print(book_schema.dump(book1))
print(book_schema.dump(book2))