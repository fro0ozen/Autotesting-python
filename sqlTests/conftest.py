import pytest


from mysql_orm.client import MysqlORMClient


def pytest_addoption(parser):
    parser.addoption('--logpath', default="access.log")


def pytest_configure(config):
    mysql_orm_client = MysqlORMClient(user='root', password='pass', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_orm_client.create_db()
    mysql_orm_client.connect(db_created=True)

    config.mysql_orm_client = mysql_orm_client


@pytest.fixture(scope='session')
def mysql_orm_client(request) -> MysqlORMClient:
    client = request.config.mysql_orm_client
    yield client
    client.connection.close()


@pytest.fixture(scope='session')
def file_path(request):
    return request.config.getoption('--logpath')
