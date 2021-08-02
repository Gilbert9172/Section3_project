from gstore import db
from sqlalchemy.orm import relationship

class Question(db.Model):
    __tablename__ = "question"

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))
    # ======= 게시물 수정 & 삭제 기능 추가 ======= #
    modify_date = db.Column(db.DateTime(), nullable=True)


class Answer(db.Model):
    __tablename__ = "answer"

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'),
                        nullable=False)
    
    user = db.relationship('User', backref=db.backref('answer_set'))
    question = db.relationship('Question',  backref=db.backref('answer_set', cascade='all, delete-orphan'))
    # ======= 게시물 수정 & 삭제 기능 추가 ======= #
    modify_date = db.Column(db.DateTime(), nullable=True)
    
class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    orders1 = relationship("Order", backref= db.backref("users"))

class Order(db.Model):
    __tablename__ = "order"

    order_id = db.Column(db.Integer, nullable=False, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id') ,nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer(), primary_key=True,nullable=False)
    product_name = db.Column(db.String(10),nullable=False)
    product_price = db.Column(db.Integer(),nullable=False)
    
    orders2 = relationship("Order",backref=db.backref('products'))
