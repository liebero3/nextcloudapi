import requests
import credentials
import pprint
NEXTCLOUD_USERNAME = credentials.username
NEXTCLOUD_PASSWORD = credentials.password
NEXTCLOUD_URL = credentials.url4


class NextcloudFormsAPI:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.auth = (username, password)

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/ocs/v2.php/apps/forms/api/v2.1/{endpoint}"
        headers = {'OCS-APIRequest': 'true','Accept': 'application/json'}
        response = requests.request(method, url, auth=self.auth, headers=headers, **kwargs)
        response.raise_for_status()
        return response
    
    def get_forms(self):
        return self._request('GET', 'forms')

    def get_shared_forms(self):
        return self._request('GET', 'shared_forms')
    
    def getFormSubmissions(self, formshash: str):
        return self._request('GET', f'submissions/{formshash}')

    def getFormSubmissionsCSV(self, formshash: str):
        return self._request('GET', f'submissions/export/{formshash}')
    
if __name__ == '__main__':
    api = NextcloudFormsAPI(
        NEXTCLOUD_URL, NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD)
    # r = api.get_shared_forms()
    # print(credentials.elternaccounts)
    # r= api.getFormSubmissions(credentials.elternaccounts)
    r= api.getFormSubmissionsCSV(credentials.elternaccounts)
    print(r.text)
    # Erstellen Sie ein PrettyPrinter Objekt
    # pp = pprint.PrettyPrinter(indent=2)

    # pp.pprint(r.json())
    # print(r.json())
