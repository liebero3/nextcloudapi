import requests
import credentials
import json

NEXTCLOUD_URL_DECK = credentials.url2
NEXTCLOUD_USERNAME = credentials.username
NEXTCLOUD_PASSWORD = credentials.password
NEXTCLOUD_FORM = credentials.form
NEXTCLOUD_APP_DECK = 'apps/deck'


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
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
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
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.post(url,
                      auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                      headers=headers,
                      json=data
                      )
    return r


def getBoardDetails(id: int):  # , data: dict
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
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.get(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     # json=data
                     )
    return r


def UpdateBoardDetails(id: int, data: dict):
    '''
    {
        "title": "Board title",
        "color": "ff0000",
        "archived": false
    }
    '''
    endpoint = f'/api/v1.1/boards/{id}'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.put(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     json=data
                     )
    return r

def deleteABoard(id: int):  # , data: dict
    '''
    response: 200 Sucess
    '''
    endpoint = f'/api/v1.1/boards/{id}'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.delete(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     # json=data
                     )
    return r

def restoreADeletedBoard(id: int):  # , data: dict
    '''
    response: 200 Sucess
    '''
    endpoint = f'/api/v1.1/boards/{id}/undo_delete'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.post(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     # json=data
                     )
    return r

# TODO: ACL-API
'''
POST /boards/{boardId}/acl - Add new acl rule
Request body
Parameter	Type	Description
type	Integer	Type of the participant
participant	String	The uid of the participant
permissionEdit	Bool	Setting if the participant has edit permissions
permissionShare	Bool	Setting if the participant has sharing permissions
permissionManage	Bool	Setting if the participant has management permissions
Supported participant types:
0 User
1 Group
7 Circle
Response
200 Success
[{
  "participant": {
    "primaryKey": "userid",
    "uid": "userid",
    "displayname": "User Name"
  },
  "type": 0,
  "boardId": 1,
  "permissionEdit": true,
  "permissionShare": false,
  "permissionManage": true,
  "owner": false,
  "id": 1
}]
PUT /boards/{boardId}/acl/{aclId} - Update an acl rule
Request parameters
Parameter	Type	Description
permissionEdit	Bool	Setting if the participant has edit permissions
permissionShare	Bool	Setting if the participant has sharing permissions
permissionManage	Bool	Setting if the participant has management permissions
Response
200 Success
DELETE /boards/{boardId}/acl/{aclId} - Delete an acl rule
Response
200 Success
'''

def getStacks(id: int):  # , data: dict
    '''
    response:
    [
    {
        "title": "ToDo",
        "boardId": 2,
        "deletedAt": 0,
        "lastModified": 1541426139,
        "cards": [...],
        "order": 999,
        "id": 4
    }
    ]
    '''
    endpoint = f'/api/v1.1/boards/{id}/stacks'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.get(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     # json=data
                     )
    return r

def getListOfArchivedStacks(id: int):  # , data: dict
    '''
    response:
    [
    {
        "title": "ToDo",
        "boardId": 2,
        "deletedAt": 0,
        "lastModified": 1541426139,
        "cards": [...],
        "order": 999,
        "id": 4
    }
    ]
    '''
    endpoint = f'/api/v1.1/boards/{id}/stacks/archived'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.get(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     # json=data
                     )
    return r

def getStackDetails(id: int, stackId: int):  # , data: dict
    '''
    response:
    [
    {
        "title": "ToDo",
        "boardId": 2,
        "deletedAt": 0,
        "lastModified": 1541426139,
        "cards": [...],
        "order": 999,
        "id": 4
    }
    ]
    '''
    endpoint = f'/api/v1.1/boards/{id}/stacks/{stackId}'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.get(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     # json=data
                     )
    return r

def createANewStack(id: int, data: dict):  # , data: dict
    '''
    {
        "title": "Board title",
        "order": Integer
    }
    '''
    endpoint = f'/api/v1.1/boards/{id}/stacks'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.post(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     json=data
                     )
    return r

def updateStackDetails(id: int, stackId: int, data: dict):  # , data: dict
    '''
    {
        "title": "Board title",
        "order": Integer
    }
    '''
    endpoint = f'/api/v1.1/boards/{id}/stacks/{stackId}'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.put(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     json=data
                     )
    return r


def deleteAStack(id: int, stackId: int):  # , data: dict
    '''
    response: 200 Success
    '''
    endpoint = f'/api/v1.1/boards/{id}/stacks/{stackId}'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.delete(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                    #  json=data
                     )
    return r

def getCardDetails(id: int, stackId: int, cardId: int):  # , data: dict
    '''
    response: 200 Success
    '''
    endpoint = f'/api/v1.1/boards/{id}/stacks/{stackId}/cards/{cardId}'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.get(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                    #  json=data
                     )
    return r

def createANewCard(id: int, stackId: int, data: dict):  # , data: dict
    '''
    {
        "title": "String: Board title, max 255 chars",
        "type": "String: Type of the card (later), for now: plain",
        "order": "Integer: number where to put",
        "description": "String: The Markdown description of the Card",
        "duedate": "timestamp: the duedate of the card or null. Format: '2019-12-24T19:29:30+00:00'"
    }
    '''
    endpoint = f'/api/v1.1/boards/{id}/stacks/{stackId}/cards'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.post(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     json=data
                     )
    return r


def updateCard(id: int, stackId: int, cardId: int, data: dict):  # , data: dict
    '''
    {
        "title": "String: Board title, max 255 chars",
        "type": "String: Type of the card (later), for now: plain",
        "order": "Integer: number where to put",
        "description": "String: The Markdown description of the Card",
        "duedate": "timestamp: the duedate of the card or null. Format: '2019-12-24T19:29:30+00:00'"
    }
    '''
    endpoint = f'/api/v1.1/boards/{id}/stacks/{stackId}/cards/{cardId}'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.put(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     json=data
                     )
    return r


def deleteCard(id: int, stackId: int, cardId: int):  # , data: dict
    '''
    {
        "title": "String: Board title, max 255 chars",
        "type": "String: Type of the card (later), for now: plain",
        "order": "Integer: number where to put",
        "description": "String: The Markdown description of the Card",
        "duedate": "timestamp: the duedate of the card or null. Format: '2019-12-24T19:29:30+00:00'"
    }
    '''
    endpoint = f'/api/v1.1/boards/{id}/stacks/{stackId}/cards/{cardId}'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.delete(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                    #  json=data
                     )
    return r

def assignALabelToACard(id: int, stackId: int, cardId: int, data: dict):  # , data: dict
    '''
    {
        "labelId": "Integer: Number of the label to put"
    }
    '''
    endpoint = f'/api/v1.1/boards/{id}/stacks/{stackId}/cards/{cardId}/assignLabel'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.put(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     json=data
                     )
    return r

def removeALabelFromACard(id: int, stackId: int, cardId: int, data: dict):  # , data: dict
    '''
    {
        "labelId": "Integer: Number of the label to put"
    }
    '''
    endpoint = f'/api/v1.1/boards/{id}/stacks/{stackId}/cards/{cardId}/removeLabel'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.put(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     json=data
                     )
    return r

def assignAUserToACard(id: int, stackId: int, cardId: int, data: dict):  # , data: dict
    '''
    {
        "userId": "Integer: userId to assign the card to"
    }
    '''
    endpoint = f'/api/v1.1/boards/{id}/stacks/{stackId}/cards/{cardId}/assignUser'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.put(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     json=data
                     )
    return r

def unassignAUserFromACard(id: int, stackId: int, cardId: int, data: dict):  # , data: dict
    '''
    {
        "userId": "Integer: userId to unassign the card from"
    }
    '''
    endpoint = f'/api/v1.1/boards/{id}/stacks/{stackId}/cards/{cardId}/unassignUser'
    url = NEXTCLOUD_URL_DECK + NEXTCLOUD_APP_DECK + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.put(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers,
                     json=data
                     )
    return r


if __name__ == "__main__":
    pass

    # '''list all boards'''
    # boards = getAListOfBoards({"details":"false"}).json()
    # for board in boards:
    #     print(board["title"], board["id"])

    # '''List all stacks in deck'''
    # stacks = getStacks(42).json()
    # for stack in stacks:
    #     print(stack["title"], stack["id"])

    # '''List all titles of cards in deck'''
    # stacks = getStacks(42).json()
    # for stack in stacks:
    #     try:
    #         cards = stack["cards"]
    #         for card in cards:
    #             print(card["title"], card["id"])
    #     except:
    #         pass
