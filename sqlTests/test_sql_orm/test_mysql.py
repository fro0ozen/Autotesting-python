import re

from test_sql_orm.base import MysqlBase


class TestAllReq(MysqlBase):

    def prepare(self, file_path):
        self.prep_all_req(file_path)

    def test_all_req(self):
        assert self.get_all_req()[0] == self.line_count


class TestAllReqByType(MysqlBase):

    def prepare(self, file_path):
        self.prep_all_req_by_type(file_path)

    def test_all_req_by_type(self):
        assert self.get_all_req_by_type() == self.all_req_by_type


class TestFrequentReq(MysqlBase):

    def prepare(self, file_path):
        self.prep_frequent_req(file_path)

    def test_frequent_req(self):
        assert self.get_frequent_req() == self.frequent_req


class TestLargestReq(MysqlBase):

    def prepare(self, file_path):
        self.prep_largest_req(file_path)

    def test_largest_req(self):
        assert self.get_largest_req() == self.largest_req


class TestUsersNumReq(MysqlBase):

    def prepare(self, file_path):
        self.prep_users_num_req(file_path)

    def test_users_num_req(self):
        assert self.get_users_num_req() == self.users_num_req
