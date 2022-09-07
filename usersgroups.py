import requests
import credentials
from lxml import etree
import csv

NEXTCLOUD_URL = credentials.url3
NEXTCLOUD_USERNAME = credentials.username
NEXTCLOUD_PASSWORD = credentials.password

BASE_URL = f'https://{NEXTCLOUD_USERNAME}:{NEXTCLOUD_PASSWORD}@{NEXTCLOUD_URL.replace("https://", "")}'
# print(BASE_URL)


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
        'email': f'{f"{username}@example.com" if "" else email}',
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


def getGroups():
    '''
    Retrieves a list of groups from the Nextcloud server.
    Authentication is done by sending a Basic HTTP Authorization header.
    '''
    url = BASE_URL + f'/groups'
    headers = {
        'OCS-APIRequest': 'true',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.get(url, headers=headers)
    return r


def createGroups(listofgroups: list):
    '''
    create groups by passing list of groups. (also for a single group as list!)
    '''
    url = BASE_URL + f'/groups'
    headers = {
        'OCS-APIRequest': 'true',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    for group in listofgroups:
        data = {
            'groupid': group
        }
        r = requests.post(url, data=data, headers=headers)
        print(f"{group} wurde erstellt")
    return r


if __name__ == "__main__":
    response = getUsers().text
    root = etree.fromstring(response)
    ncusers = list(root[1][0])

    '''Allen Usern mit numerischem username eine Quota von 100 MB geben'''
    # for u in ncusers:
    #     if u.text.isnumeric():
    #         editUser(u.text, {'key':'quota', 'value':'104857600'})

    '''Alle kompletten details von usern ausgeben'''
    # for u in ncusers:
    #     print(getUser(u.text).text)
    '''Gruppen ausgeben:'''
    # print(getGroups().text)

    '''Gruppen anlegen'''
    # with open('gruppen_schild.csv', newline='') as f:
    #     reader = csv.reader(f)
    #     data = list(reader)
    # data = [item for sublist in data for item in sublist]
    # data = list(set(data))
    # print(data)
    # createGroups(data)
    # print(len(gruppenliste))

    '''User aus csv zu Gruppen hinzufuegen'''
    with open('testuser.csv', newline='') as f:
        reader = csv.reader(f, delimiter=';')
        data = list(reader)

    for user in data:
        if user[0] == "Vorname":
            continue
        # Zur Sicherheit Gruppe erstellen, in die eingefuegt werden soll
        groups = []
        groups.append(user[4])
        b = createGroups(groups)
        print(b.text)
        # User aus angegebener Gruppe loeschen
        liste = []
        liste.append(user[5])
        a = removeUserToGroups(user[2], liste)
        print(a.text)
        # zuerst versuchen den user zu erstellen. Sollte er schon existieren, gibt es Fehlermeldung
        a = addUser(user[2], f"{user[0]} {user[1]}",
                    user[3], "", [f"{user[4]}"], '104857600')
        print(a.text)
        # sollte er schon existieren, user zu Gruppen hinzufuegen.
        c = addUserToGroups(f"{user[2]}", groups)
