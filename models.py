from app import def db 

class Announcement(db.Model):

    __tablename__ = "announcements"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description