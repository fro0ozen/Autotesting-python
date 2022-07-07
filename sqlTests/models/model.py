from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class AllReq(Base):
    __tablename__ = 'all_req'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    total_number_of_requests = Column(Integer, nullable=False)


class AllReqByType(Base):
    __tablename__ = 'all_req_by_type'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    request_type = Column(String(10), nullable=False)
    request_type_number = Column(Integer, nullable=False)


class FrequentReq(Base):
    __tablename__ = 'frequent_req'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(Text, nullable=False)
    requests_number_for_url = Column(Integer, nullable=False)


class LargestReq(Base):
    __tablename__ = 'largest_req'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(String(20), nullable=False)
    url = Column(Text, nullable=False)
    status_code = Column(Integer, nullable=False)
    request_size = Column(Integer, nullable=False)


class UsersNumReq(Base):
    __tablename__ = 'users_num_req'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(String(20), nullable=False)
    number_of_requests = Column(Integer, nullable=False)
