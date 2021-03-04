from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self,name):
        self.name=name
    def json(self):
        return {"id":self.id,"name":self.name,"books":self.books}


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", backref="books")
    
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def json(self):
        return {"id":self.id,"title":self.title,"author":self.author.id}
    
db.create_all()

author = Author(name="Barney Stinson")
book1 = Book(title="Bro Code", author=author)
book2 = Book(title="Bro on the go", author=author)

db.session.add(author)
db.session.add(book1)
db.session.add(book2)
db.session.commit()

print(Author.query.first().json())
get_book = (book.json() for book in Book.query.all())
print(next(get_book))
print(next(get_book))