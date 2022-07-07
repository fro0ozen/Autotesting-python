from models.model import AllReq, AllReqByType, FrequentReq, LargestReq, UsersNumReq


class MysqlORMBuilder:

    def __init__(self, client):
        self.client = client

    def create_all_req(self, total_number_of_requests):
        writing = AllReq(
            total_number_of_requests=total_number_of_requests
        )
        self.client.session.add(writing)
        self.client.session.commit()
        return writing

    def create_all_req_by_type(self, all_req_by_type):
        ret_lst = []
        for i in all_req_by_type.keys():
            if len(i) > 10:
                continue
            writing = AllReqByType(
                request_type=i,
                request_type_number=all_req_by_type[i]
            )
            ret_lst.append(writing)
            self.client.session.add(writing)

        self.client.session.commit()
        return ret_lst

    def create_frequent_req(self, frequent_req):
        ret_lst = []
        for i in frequent_req.keys():
            writing = FrequentReq(
                url=i,
                requests_number_for_url=frequent_req[i]
            )
            ret_lst.append(writing)
            self.client.session.add(writing)

        self.client.session.commit()
        return ret_lst

    def create_largest_req(self, largest_req):
        ret_lst = []
        for i in largest_req:
            writing = LargestReq(
                ip_address=i[0],
                url=i[1],
                status_code=i[2],
                request_size=i[3]
            )
            ret_lst.append(writing)
            self.client.session.add(writing)

        self.client.session.commit()
        return ret_lst

    def create_users_num_req(self, users_num_req):
        ret_lst = []
        for i in users_num_req.keys():
            writing = UsersNumReq(
                ip_address=i,
                number_of_requests=users_num_req[i]
            )
            ret_lst.append(writing)
            self.client.session.add(writing)

        self.client.session.commit()
        return ret_lst
