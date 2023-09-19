from ..utils import db
from datetime import datetime

class Ticket(db.Model):
    __tablename__= 'tickets'
    id=db.Column(db.Integer(),primary_key=True)
    title=db.Column(db.String(45),nullable=False)
    description=db.Column(db.String(45),nullable=False)


    def __repr__(self):
        return f'<Ticket {self.id}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()