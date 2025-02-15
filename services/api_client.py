import requests
from config import STRACT_API_BASE_URL, STRACT_AUTH_TOKEN


class StractAPIClient:
    def __init__(self):
        self.base_url = STRACT_API_BASE_URL
        self.headers = {"Authorization": f"Bearer {STRACT_AUTH_TOKEN}"}

    def get_platforms(self):
        url = f"{self.base_url}/platforms"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        platforms_data = response.json()
        # Retorna um dicionário
        return {item['value']: item['text'] for item in platforms_data['platforms']}

    def get_accounts(self, platform):
        all_accounts = []
        page = 1
        while True:
            url = f"{self.base_url}/accounts?platform={platform}&page={page}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            if "accounts" in data:
                all_accounts.extend(data["accounts"])
            pagination = data.get("pagination", {})
            current_page = pagination.get("current", 1)
            total_pages = pagination.get("total", 1)
            if current_page >= total_pages:
                break
            page += 1
        return all_accounts

    def get_fields(self, platform):
        url = f"{self.base_url}/fields?platform={platform}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_insights(self, platform, account, fields):
        fields_list = fields.get('fields', [])
        fields_str = ",".join([field["value"] for field in fields_list])
        url = f"{self.base_url}/insights?platform={platform}&account={account['id']}&token={account['token']}&fields={fields_str}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
