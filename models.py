from sqlalchemy import Column, Integer, String, DateTime


class User(object):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    iptype = Column(String(50), unique=True)
    qq = Column(String(50), unique=False, nullable=True)
    address = Column(String(200), unique=True)
    cell_phone = Column(String(50))
    email = Column(String(50))
    game = Column(String(50))
    login_id = Column(String(50))
    login_ip = Column(String(50))
    login_time = Column(DateTime)
    money = Column(Integer)
    nownum = Column(Integer)
    password = Column(String(50))
    region = Column(String(50))
    winnum = Column(Integer)
    expire_time = Column(DateTime)
    usedpppoenum = Column(String(50))
    higher_username = Column(String(50))
    higher_userid = Column(String(50))

    def __init__(self, name=None, iptype=None, qq=None, ):
        self.name = name


    def __repr__(self):
        return '<User %r>' % (self.name)
