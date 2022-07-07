import pytest
from base import ApiBase
from utils import utils
import allure


@allure.feature("API tests")
@allure.story("Tests by section")
class TestTargetApi(ApiBase):

    @allure.testcase("Create segment")
    @allure.description("Creating a new segment")
    @pytest.mark.API
    def test_create_segment(self):
        created_segment, segment_id = self.create_section()
        assert created_segment
        self.delete_section(segment_id)

    @allure.testcase("Delete campaign")
    @allure.description("Creating a new segment and deleting it")
    @pytest.mark.API
    def test_delete_segment(self):
        section_id = self.create_section()[1]
        assert self.delete_section(section_id)

    @allure.testcase("Create and delete campaign")
    @allure.description("Creating a new advertising campaign and deleting it")
    @pytest.mark.API
    def test_create_campaign(self, file_path):
        created_campaign, campaign_id = self.create_campaign(file_path)
        assert created_campaign
        self.api_client.post_delete_campaign(campaign_id)
        assert utils.in_list("id", campaign_id, self.api_client.get_active_campaigns(), in_lst=False)[0]
