import requests
import credentials
import json

NEXTCLOUD_URL = credentials.url2
NEXTCLOUD_USERNAME = credentials.username
NEXTCLOUD_PASSWORD = credentials.password
NEXTCLOUD_FORM = credentials.form
NEXTCLOUD_APP = 'apps/deck'


def getAListOfBoards(data: dict):
    '''
    Headers
    The board list endpoint supports setting an If-Modified-Since header to limit the results to entities that are changed after the provided time.

    Request parameters
    Parameter	Type	Description
    details	    Bool	Optional Enhance boards with details about labels, stacks and users
    Response
    200 Success
    Returns an array of board items

    [
        {
            "title": "Board title",
            "owner": {
                "primaryKey": "admin",
                "uid": "admin",
                "displayname": "Administrator"
            },
            "color": "ff0000",
            "archived": false,
            "labels": [],
            "acl": [],
            "permissions": {
                "PERMISSION_READ": true,
                "PERMISSION_EDIT": true,
                "PERMISSION_MANAGE": true,
                "PERMISSION_SHARE": true
            },
            "users": [],
            "shared": 0,
            "deletedAt": 0,
            "id": 10,
            "lastModified": 1586269585,
            "settings": {
                "notify-due": "off",
                "calendar": true
            }
        }
    ]
    '''
    endpoint = '/api/v1.1/boards'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.get(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     json=data
                     )
    return r


def createANewBoard(data: dict):
    '''
    Request body
    Parameter	Type	Description
    title	    String	The title of the new board, maximum length is limited to 100 characters
    color	    String	The hexadecimal color of the new board (e.g. FF0000)
    {
        "title": "Board title",
        "color": "ff0000"
    }
    Response
    200 Success
    {
        "title": "Board title",
        "owner": {
            "primaryKey": "admin",
            "uid": "admin",
            "displayname": "Administrator"
        },
        "color": "ff0000",
        "archived": false,
        "labels": [
            {
                "title": "Finished",
                "color": "31CC7C",
                "boardId": 10,
                "cardId": null,
                "id": 37
            },
            {
                "title": "To review",
                "color": "317CCC",
                "boardId": 10,
                "cardId": null,
                "id": 38
            },
            {
                "title": "Action needed",
                "color": "FF7A66",
                "boardId": 10,
                "cardId": null,
                "id": 39
            },
            {
                "title": "Later",
                "color": "F1DB50",
                "boardId": 10,
                "cardId": null,
                "id": 40
            }
        ],
        "acl": [],
        "permissions": {
            "PERMISSION_READ": true,
            "PERMISSION_EDIT": true,
            "PERMISSION_MANAGE": true,
            "PERMISSION_SHARE": true
        },
        "users": [],
        "deletedAt": 0,
        "id": 10,
        "lastModified": 1586269585
    }
    '''
    endpoint = '/api/v1.1/boards'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.post(url,
                      auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                      headers=headers,
                      json=data
                      )
    return r


def getBoardDetails(id: int, data: dict):
    '''
    Request parameters
    Parameter	Type	Description
    boardId	    Integer	The id of the board to fetch
    Response
    200 Success
    {
        "title": "Board title",
        "owner": {
            "primaryKey": "admin",
            "uid": "admin",
            "displayname": "Administrator"
        },
        "color": "ff0000",
        "archived": false,
        "labels": [
            {
                "title": "Finished",
                "color": "31CC7C",
                "boardId": "10",
                "cardId": null,
                "id": 37
            },
            {
                "title": "To review",
                "color": "317CCC",
                "boardId": "10",
                "cardId": null,
                "id": 38
            },
            {
                "title": "Action needed",
                "color": "FF7A66",
                "boardId": "10",
                "cardId": null,
                "id": 39
            },
            {
                "title": "Later",
                "color": "F1DB50",
                "boardId": "10",
                "cardId": null,
                "id": 40
            }
        ],
        "acl": [],
        "permissions": {
            "PERMISSION_READ": true,
            "PERMISSION_EDIT": true,
            "PERMISSION_MANAGE": true,
            "PERMISSION_SHARE": true
        },
        "users": [
            {
                "primaryKey": "admin",
                "uid": "admin",
                "displayname": "Administrator"
            }
        ],
        "deletedAt": 0,
        "id": 10
    }
    '''
    endpoint = f'/api/v1.1/boards/{id}'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.get(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     json=data
                     )
    return r


if __name__ == "__main__":
    # createANewBoard({"title":"Board mit API", "color":"ff0000"})
    # r = getAListOfBoards({"details":"true"})
    # r = getBoardDetails(2{"boardId": 2})
    r = getBoardDetails(2, {"boardId":2})
    print(r.text)
    # print(f"Status Code: {r.status_code}, \nResponse: \n{r.text}")
    # print(f"Status Code: {r.status_code}, \nResponse: \n{r.json()}")
