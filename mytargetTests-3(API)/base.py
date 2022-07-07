import pytest
import allure
from utils import utils


class ApiBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, logger):
        self.api_client = api_client
        self.logger = logger
        self.api_client.post_login()

    @allure.step("Create section")
    def create_section(self):
        segment_name = utils.name_generator()
        self.api_client.post_segment(segment_name)
        return utils.in_list("name", segment_name, self.api_client.get_segments(), ret_param="id")

    @allure.step("Delete section")
    def delete_section(self, segment_id):
        self.api_client.delete_segment(segment_id)
        return utils.in_list("id", segment_id, self.api_client.get_segments(), in_lst=False)[0]

    @allure.step("Create campaign")
    def create_campaign(self, file_path):
        pac_id = utils.in_list("description", "Баннер 240х400", self.api_client.get_packages(), ret_param="id")[1]
        url_id = self.api_client.post_urls("https://mail.ru")
        static_id = self.api_client.post_static(file_path)
        campaign_id = self.api_client.post_campaigns(pac_id, url_id, static_id, utils.name_generator())
        return utils.in_list("id", campaign_id, self.api_client.get_active_campaigns(), ret_param="id")
