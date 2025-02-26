from uuid import uuid4,UUID
from enum import Enum
from my_app.models import db
class IDType(Enum):
    KENYAN_CITIZEN = "Kenyan Citizen"
    FOREIGN_RESIDENT = "Foreign Resident"
    REFUGEE = "Refugee"
    MANDATE_NUMBER = "Mandate Number"
    
class User(db.Model):
    __tablename__='user'
    id = db.Column(db.UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid4)
    id_type = db.Column(db.Enum(IDType), nullable=False, default=IDType.KENYAN_CITIZEN)
    email=db.Column(db.String(80),nullable=False)
    full_name=db.Column(db.String(80),nullable=False)
    phone=db.Column(db.String(12),nullable=False)
    national_id=db.Column(db.String(12),nullable=False)

    # relationship
    password = db.Relationship('Password',backref='user',uselist=False)
    
    def verify_password(self,password):
        print(password)
        print(self.password.password==password)
        return self.password.password==password
        

    @classmethod
    def add_user(cls, user):
     try:
         new_user = User(
             full_name=user["full_name"],
             id_type=IDType(user["id_type"]),
             national_id=user["national_id"],
             phone=user["phone"],
             email=user["email"]
         )
         

         db.session.add(new_user)
         db.session.commit()
         db.session.refresh(new_user)  
 
        
         if Password.save_password(new_user.id, user["password"]): 
             return True
 
         db.session.delete(new_user)
         db.session.commit() 
         return False
 
     except Exception as e:

         db.session.rollback()
         return False

    @classmethod
    def by_email(cls,email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def by_id(cls,id):
        return cls.query.filter_by(id=UUID(id)).first()
    
    @classmethod
    def by_national_id(cls,national_id):
        return cls.query.filter_by(national_id=national_id).first()

class Password(db.Model):
    __tablename__='password'
    user_id = db.Column(db.UUID,db.ForeignKey('user.id'),primary_key=True)
    password=db.Column(db.String(120),nullable=False)
    
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
        
