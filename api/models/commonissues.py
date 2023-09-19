from ..utils import db
from datetime import datetime

class CommonIssue(db.Model):
    __tablename__= 'commonissues'
    issue_id=db.Column(db.Integer(),primary_key=True)
    issue_name=db.Column(db.String(45),nullable=False)


    def __repr__(self):
        return f'<CommonIssue {self.issue_id}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()