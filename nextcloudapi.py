import requests
import credentials

NEXTCLOUD_URL = credentials.url
NEXTCLOUD_USERNAME = credentials.username
NEXTCLOUD_PASSWORD = credentials.password

BASE_URL = f'https://{NEXTCLOUD_USERNAME}:{NEXTCLOUD_PASSWORD}@{NEXTCLOUD_URL}'



def getUsers():
    '''
    List all users
    '''
    url = BASE_URL + f'/users'
    headers = {'OCS-APIRequest': 'true'}
    r = requests.get(url, headers=headers)
    return r


def getUser(username: str):
    '''
    Get information about a specific User by username
    '''
    url = BASE_URL + f'/users/{username}'
    headers = {'OCS-APIRequest': 'true'}
    r = requests.get(url, headers=headers)
    return r


def addUser(username: str, displayName: str, password: str, email: str, listofgroups: list, quota: str):
    '''
    listofgroups is a list of groups the user should be member of. Groups must exist before.
    '''
    url = BASE_URL + '/users'
    headers = {
        'OCS-APIRequest': 'true',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'userid': f'{username}',
        'displayName': f'{displayName}',
        'password': f'{password}',
        'email': f'{email}',
        'groups[]': listofgroups,
        'quota': f'{quota}'
    }
    r = requests.post(url, data=data, headers=headers)
    return r


def editUser(username: str, keyvaluepairs: dict):
    '''
    keyvaluepairs are like {key:blub, value:blub}. Possible keys are 
    email, quota, displayname, phone, address, website, twitter, password
    '''
    url = BASE_URL + f'/users/{username}'
    print(url)
    headers = {
        'OCS-APIRequest': 'true',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = keyvaluepairs
    print(type(data))
    r = requests.put(url, data=data, headers=headers)
    return r


def disableUser(username: str):
    '''
    disables user by username
    '''
    url = BASE_URL + f'/users/{username}/disable'
    headers = {
        'OCS-APIRequest': 'true',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.put(url, headers=headers)
    return r


def enableUser(username: str):
    '''
    enables user by username
    '''
    url = BASE_URL + f'/users/{username}/enable'
    headers = {
        'OCS-APIRequest': 'true',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.put(url, headers=headers)
    return r


def deleteUser(username: str):
    '''
    deletes user by username
    '''
    url = BASE_URL + f'/users/{username}'
    headers = {
        'OCS-APIRequest': 'true',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.delete(url, headers=headers)
    return r


def getUserGroups(username: str):
    '''
    Get Groups a specific user is member of by username
    '''
    url = BASE_URL + f'/users/{username}/groups'
    headers = {'OCS-APIRequest': 'true'}
    r = requests.get(url, headers=headers)
    return r


def addUserToGroups(username: str, listofgroups: list):
    '''
    Adds a user by username to one or many groups. 
    listofgroups is a list of groups as str
    '''
    url = BASE_URL + f'/users/{username}/groups'
    headers = {
        'OCS-APIRequest': 'true',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    for group in listofgroups:
        data = {
            'groupid': group
        }
        r = requests.post(url, data=data, headers=headers)
    return r


def removeUserToGroups(username: str, listofgroups: list):
    '''
    Removes a user by username to one or many groups. 
    listofgroups is a list of groups as str
    '''
    url = BASE_URL + f'/users/{username}/groups'
    headers = {
        'OCS-APIRequest': 'true',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    for group in listofgroups:
        data = {
            'groupid': group
        }
        r = requests.delete(url, data=data, headers=headers)
    return r


def promoteUserinGroup(username: str, listofgroups: list):
    '''
    Promotes a User to subadmin of one or many groups.
    listofgroups is a list of groups as str
    '''
    url = BASE_URL + f'/users/{username}/subadmins'
    headers = {
        'OCS-APIRequest': 'true',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    for group in listofgroups:
        data = {
            'groupid': group
        }
        r = requests.post(url, data=data, headers=headers)
    return r


def demoteUserinGroup(username: str, listofgroups: list):
    '''
    Promotes a User to subadmin of one or many groups.
    listofgroups is a list of groups as str
    '''
    url = BASE_URL + f'/users/{username}/subadmins'
    headers = {
        'OCS-APIRequest': 'true',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    for group in listofgroups:
        data = {
            'groupid': group
        }
        r = requests.delete(url, data=data, headers=headers)
    return r


def getUserSubadminGroups(username: str):
    '''
    Promotes a User to subadmin of one or many groups.
    listofgroups is a list of groups as str
    '''
    url = BASE_URL + f'/users/{username}/subadmins'
    headers = {
        'OCS-APIRequest': 'true',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    r = requests.get(url, headers=headers)
    return r


def resendWelcomeMail(username: str):
    '''
    Promotes a User to subadmin of one or many groups.
    listofgroups is a list of groups as str
    '''
    url = BASE_URL + f'/users/{username}/welcome'
    headers = {
        'OCS-APIRequest': 'true',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    r = requests.post(url, headers=headers)
    return r

if __name__=="__main__":
    # deleteUser("Testuser2")
    
    
    print(getUsers().text)