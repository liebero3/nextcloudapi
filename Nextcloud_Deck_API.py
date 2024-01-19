import requests
import credentials
NEXTCLOUD_USERNAME = credentials.username
NEXTCLOUD_PASSWORD = credentials.password
NEXTCLOUD_URL = credentials.url4


class NextcloudDeckAPI:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.auth = (username, password)

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/index.php/apps/deck/api/v1.1/{endpoint}"
        response = requests.request(method, url, auth=self.auth, **kwargs)
        response.raise_for_status()
        return response.json()

    def get_boards(self):
        return self._request('GET', 'boards')

    def get_board(self, board_id):
        return self._request('GET', f'boards/{board_id}')

    def get_stacks(self, board_id):
        return self._request('GET', f'boards/{board_id}/stacks')

    def get_stack(self, stack_id):
        return self._request('GET', f'stacks/{stack_id}')

    def get_cards(self, stack_id):
        return self._request('GET', f'stacks/{stack_id}/cards')

    def get_card(self, card_id):
        return self._request('GET', f'cards/{card_id}')

    def create_card(self, stack_id, title, description='', user_id=''):
        data = {
            'title': title,
            'description': description,
            'type': 'plain',
            'user_id': user_id,
        }
        return self._request('POST', f'stacks/{stack_id}/cards', json=data)

    def upload_attachment(self, card_id, file_path):
        with open(file_path, 'rb') as file:
            files = {'file': file}
            return self._request('POST', f'cards/{card_id}/attachments', files=files)


if __name__ == '__main__':
    api = NextcloudDeckAPI(
        NEXTCLOUD_URL, NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD)
    r = api.get_boards()
    print(r)
    # board_id = 42
    # stack_id = 121

    # # Create a card
    # title = "New card with attachment"
    # description = "This card has an attachment"
    # card = api.create_card(stack_id, title, description)
    # card_id = card['id']

    # # Upload an attachment to the card
    # attachment_file_path = "picture.jpg"  # Replace with the actual file path
    # api.upload_attachment(card_id, attachment_file_path)
