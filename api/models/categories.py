from ..utils import db
from datetime import datetime

class Category(db.Model):
    __tablename__= 'categories'
    category_id=db.Column(db.Integer(),primary_key=True)
    category_name=db.Column(db.String(45),nullable=False)
   


    def __repr__(self):
        return f'<Category {self.category_id}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()