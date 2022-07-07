import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

from models.model import Base


class MysqlORMClient:

    def __init__(self, user, password, db_name, host='127.0.0.1', port=3306):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = host
        self.port = port

        self.engine = None
        self.connection = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'

        self.engine = sqlalchemy.create_engine(url, encoding='utf8')
        self.connection = self.engine.connect()
        self.session = sessionmaker(bind=self.connection.engine)()

    def create_db(self):
        self.connect(db_created=False)

        self.connection.execute(f'DROP database if exists {self.db_name}')
        self.connection.execute(f'CREATE database {self.db_name}')

        self.connection.close()

    def create_all_tables(self):
        self.create_all_req()
        self.create_all_req_by_type()
        self.create_frequent_req()
        self.create_largest_req()
        self.create_users_num_req()

    def create_all_req(self):
        if not inspect(self.engine).has_table('all_req'):
            Base.metadata.tables['all_req'].create(self.engine)

    def create_all_req_by_type(self):
        if not inspect(self.engine).has_table('all_req_by_type'):
            Base.metadata.tables['all_req_by_type'].create(self.engine)

    def create_frequent_req(self):
        if not inspect(self.engine).has_table('frequent_req'):
            Base.metadata.tables['frequent_req'].create(self.engine)

    def create_largest_req(self):
        if not inspect(self.engine).has_table('largest_req'):
            Base.metadata.tables['largest_req'].create(self.engine)

    def create_users_num_req(self):
        if not inspect(self.engine).has_table('users_num_req'):
            Base.metadata.tables['users_num_req'].create(self.engine)
