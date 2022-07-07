from urllib.parse import urljoin
import logging
import requests
import allure
from api import requests_data


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:

    MAX_RESPONSE_LENGTH = 150

    def __init__(self, base_url, user, password):
        self.base_url = base_url
        self.user = user
        self.password = password
        self.session = requests.Session()
        self.csrf_token = None
        self.logger = logging.getLogger("test")

    def headers(self):
        return {"X-CSRFToken": f'{self.csrf_token}'}

    def log_pre(self, url, headers, data, json_data, files, expected_status):
        self.logger.info(f'Performing request:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'DATA: {data}\n\n'
                    f'JSON: {json_data}\n\n'
                    f'Files: {files}\n\n'
                    f'expected status: {expected_status}\n\n')

    def log_post(self, response):
        log_str = 'Got response:\n' \
                  f'RESPONSE STATUS: {response.status_code}\n'

        if len(response.text) > self.MAX_RESPONSE_LENGTH:
            if self.logger.level == logging.INFO:
                self.logger.info(f'{log_str}\n'
                            f'RESPONSE CONTENT: COLLAPSED due to response size > {self.MAX_RESPONSE_LENGTH}. '
                            f'Use DEBUG logging.\n\n'
                            f'{response.text[:self.MAX_RESPONSE_LENGTH]}\n\n')
            elif self.logger.level == logging.DEBUG:
                self.logger.info(f'{log_str}\n'
                            f'RESPONSE CONTENT: {response.text}\n\n')
        else:
            self.logger.info(f'{log_str}\n'
                        f'RESPONSE CONTENT: {response.text}\n\n')

    def _request(self, method, location=None, full_url=None, headers=None, data=None, json_data=None, files=None,
                 expected_status=200, jsonify=False):
        url = urljoin(self.base_url, location) if full_url is None else full_url
        headers = self.headers() if headers is None else headers
        self.log_pre(url, headers, data, json_data, files, expected_status)
        response = self.session.request(method, url, data=data, json=json_data, files=files, headers=headers)
        self.log_post(response)
        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.request} for URL "{url}"')
        if jsonify:
            return response.json()
        return response

    @allure.step("POST login")
    def post_login(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": self.base_url
        }
        data = {
            "email": f"{self.user}",
            "password": f"{self.password}",
            "continue": "https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email",
            "failure": "https://account.my.com/login/"
        }
        self._request("POST", full_url="https://auth-ac.my.com/auth?lang=ru&nosavelogin=0", headers=headers, data=data)
        self.csrf_token = self._request("GET", "/csrf").cookies.get_dict()["csrftoken"]

    @allure.step("GET segments list")
    def get_segments(self):
        return self._request("GET", "/api/v2/remarketing/segments.json", jsonify=True)["items"]

    @allure.step("POST segment")
    def post_segment(self, segment_name):
        return self._request("POST", "/api/v2/remarketing/segments.json",
                             json_data=requests_data.segment_data(segment_name))

    @allure.step("DELETE segment")
    def delete_segment(self, segment_id):
        return self._request("DELETE", f"/api/v2/remarketing/segments/{segment_id}.json", expected_status=204)

    @allure.step("POST static image")
    def post_static(self, file_path):
        data = {
            "file": ("banner_image.jpg", open(file_path, "rb")),
        }
        return self._request("POST", "/api/v2/content/static.json", files=data, jsonify=True)["id"]

    @allure.step("GET packages list")
    def get_packages(self):
        return self._request("GET", "/api/v2/packages.json", jsonify=True)["items"]

    @allure.step("POST url for campaign")
    def post_urls(self, url):
        data = {
            "url": url
        }
        return self._request("POST", "/api/v2/urls.json", json_data=data, expected_status=201, jsonify=True)["id"]

    @allure.step("POST campaign")
    def post_campaigns(self, package_id, url_id, image_id, campaign_name):
        return self._request("POST", "/api/v2/campaigns.json",  jsonify=True,
                             json_data=requests_data.campaign_data(campaign_name, package_id, url_id, image_id))["id"]

    @allure.step("POST delete campaign")
    def post_delete_campaign(self, campaign_id):
        data = {"status": "deleted"}
        return self._request("POST", f"/api/v2/campaigns/{campaign_id}.json", json_data=data, expected_status=204)

    @allure.step("GET active campaigns list")
    def get_active_campaigns(self):
        return self._request("GET", "/api/v2/campaigns.json?_status=active", jsonify=True)["items"]
