from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from passlib.hash import pbkdf2_sha256 as sha256


from api.utils.database import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    isVerified = db.Column(db.Boolean,  nullable=False, default=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True

    id = auto_field()
    username = auto_field()
    password = auto_field()
    email = auto_field()
