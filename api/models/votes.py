from ..utils import db
from datetime import datetime

class Vote(db.Model):
    __tablename__= 'votes'
    vote_id=db.Column(db.Integer(),primary_key=True)
    vote_name=db.Column(db.String(45),nullable=False)
    vote_region=db.Column(db.String(45),nullable=False)


    def __repr__(self):
        return f'<Vote {self.vote_id}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()