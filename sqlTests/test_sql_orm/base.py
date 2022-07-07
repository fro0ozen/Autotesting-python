import pytest
import re

from models.model import AllReq, AllReqByType, FrequentReq, LargestReq, UsersNumReq
from mysql_orm.client import MysqlORMClient
from utils.builder_orm import MysqlORMBuilder


class MysqlBase:

    def prepare(self, file_path):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client, file_path):
        self.mysql: MysqlORMClient = mysql_orm_client
        self.mysql_builder: MysqlORMBuilder = MysqlORMBuilder(self.mysql)
        self.prepare(file_path)

    def prep_all_req(self, file_path):
        self.mysql.create_all_req()
        with open(file_path) as f:
            line_count = 0
            for _ in f:
                line_count += 1
        self.line_count = self.mysql_builder.create_all_req(line_count)

    def prep_all_req_by_type(self, file_path):
        self.mysql.create_all_req_by_type()
        dct = {}
        with open(file_path) as f:
            for i in f:
                lst = i.split()
                if dct.get(lst[5][1:], False):
                    dct[lst[5][1:]] += 1
                else:
                    dct[lst[5][1:]] = 1
        self.all_req_by_type = self.mysql_builder.create_all_req_by_type(dct)

    def prep_frequent_req(self, file_path, limits=10):
        self.mysql.create_frequent_req()
        dct = {}
        sorted_dict = {}
        with open(file_path) as f:
            lst = [i.split()[6] for i in f]
            for i in lst:
                if dct.get(i, False):
                    dct[i] += 1
                else:
                    dct[i] = 1

            sorted_values = sorted(dct.values(), reverse=True)
            for i in sorted_values:
                for k in dct.keys():
                    if dct[k] == i:
                        sorted_dict[k] = dct[k]
                        dct.pop(k)
                        break
        ret_dict = {}
        for i in list(sorted_dict.keys())[:limits]:
            ret_dict[i] = sorted_dict[i]
        self.frequent_req = self.mysql_builder.create_frequent_req(ret_dict)

    def prep_largest_req(self, file_path, limits=5):
        self.mysql.create_largest_req()
        lst = []
        with open(file_path) as f:
            for i in f:
                if re.match(r"4[0-9][0-9]", i.split()[8]):
                    lst.append(i.split())
            lst.sort(key=lambda x: int(x[9]), reverse=True)
        largest_req = []
        for i in lst[:limits]:
            largest_req.append([i[0], i[6], i[8], i[9]])
        self.largest_req = self.mysql_builder.create_largest_req(largest_req)

    def prep_users_num_req(self, file_path, limits=5):
        self.mysql.create_users_num_req()
        dct = {}
        sorted_dict = {}
        with open(file_path) as f:
            for i in f:
                if re.match(r"5[0-9][0-9]", i.split()[8]):
                    if i.split()[0] in dct.keys():
                        dct[i.split()[0]] += 1
                    else:
                        dct[i.split()[0]] = 1

        sorted_values = sorted(dct.values(), reverse=True)
        for i in sorted_values:
            for k in dct.keys():
                if dct[k] == i:
                    sorted_dict[k] = dct[k]
                    dct.pop(k)
                    break
        users_num_req = {}
        for i in list(sorted_dict.keys())[:limits]:
            users_num_req[i] = sorted_dict[i]
        self.users_num_req = self.mysql_builder.create_users_num_req(users_num_req)

    def get_all_req(self):
        self.mysql.session.commit()
        return self.mysql.session.query(AllReq).all()

    def get_all_req_by_type(self):
        self.mysql.session.commit()
        return self.mysql.session.query(AllReqByType).all()

    def get_frequent_req(self):
        self.mysql.session.commit()
        return self.mysql.session.query(FrequentReq).all()

    def get_largest_req(self):
        self.mysql.session.commit()
        return self.mysql.session.query(LargestReq).all()

    def get_users_num_req(self):
        self.mysql.session.commit()
        return self.mysql.session.query(UsersNumReq).all()
