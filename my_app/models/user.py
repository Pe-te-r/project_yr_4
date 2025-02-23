from uuid import uuid4,UUID
from my_app.models import db

class User(db.Model):
    __tablename__='user'
    id=db.Column(db.UUID,nullable=False,primary_key=True)
    email=db.Column(db.String(80),nullable=False)
    first_name=db.Column(db.String(80),nullable=False)
    last_name=db.Column(db.String(80),nullable=False)

    # relationship
    password = db.Relationship('Password',backref='user',uselist=False)

    @classmethod
    def add_user(cls,user):
        try:
            new_user=cls(id=uuid4(),email=user['email'],first_name=user['first_name'],last_name=user['last_name'])
            db.session.add(new_user)
            db.session.commit()
            db.session.refresh(new_user)
            if Password.save_password(new_user.id,user['password']):
                return True
            db.session.delete(new_user)
            return False

        except:
            db.session.rollback()
            return False

class Password(db.Model):
    __tablename__='password'
    user_id = db.Column(db.UUID,db.ForeignKey('user.id'),primary_key=True)
    password=db.Column(db.STring(120),nullable=False)
    
    @classmethod
    def save_password(cls,user_id,password):
        try:
            new=cls(user_id=user_id,password=password)
            db.session.add(new)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
        
