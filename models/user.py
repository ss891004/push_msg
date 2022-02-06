from main.ext import dbs

class User(dbs.Model):
    __tablename__ = 'user'

    id = dbs.Column(dbs.Integer, primary_key=True)
    UserCode = dbs.Column(dbs.String(64), unique=True, index=True)
    Password = dbs.Column(dbs.String(128))

    def __init__(self, UserCode=None, Password=None):
        self.UserCode = UserCode
        self.Password = Password

    def __repr__(self):
        return '<User %r>' % self.UserName
