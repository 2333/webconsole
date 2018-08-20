from sqlalchemy import Column, Integer, String


class User(object):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, )
    iptype
    qq
    address
    cell_phone
    email
    game
    login_id
    login_ip
    login_time
    money
    nownum
    password
    region
    winnum
    expire_time
    usedpppoenum
    higher_username
    higher_userid

    def __init__(self, name=None, ):
        self.

    def __repr__(self):
        return '<User %r>' % (self.name)
