import requests
import credentials

NEXTCLOUD_URL = credentials.url
NEXTCLOUD_USERNAME = credentials.username
NEXTCLOUD_PASSWORD = credentials.password
NEXTCLOUD_FORM = credentials.form
NEXTCLOUD_APP = 'apps/forms'


def listOwnedForms():
    '''
    Returns condensed objects of all Forms beeing owned by the authenticated user.

    Endpoint: /api/v1.1/forms
    Method: GET
    Parameters: None
    Response: Array of condensed Form Objects, sorted as newest first.
    "data": [
    {
        "id": 6,
        "hash": "yWeMwcwCwoqRs8T2",
        "title": "Form 2",
        "expires": 0,
        "partial": true
    },
    {
        "id": 3,
        "hash": "em4djk8B9BpXnkYG",
        "title": "Form 1",
        "expires": 0,
        "partial": true
    }
    ]
    '''
    endpoint = '/api/v1.1/forms'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.get(url, auth=(NEXTCLOUD_USERNAME,
                     NEXTCLOUD_PASSWORD), headers=headers)
    return r


def listSharedForms():
    '''
    Returns condensed objects of all Forms, that are shared to the authenticated user
    via instance (access-type registered or selected) and have not expired yet.

    Endpoint: /api/v1.1/shared_forms
    Method: GET
    Parameters: None
    Response: Array of condensed Form Objects, sorted as newest first, similar to List owned Forms.
    See above, 'List owned forms'
    '''
    endpoint = '/api/v1.1/shared_forms'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.get(url, auth=(NEXTCLOUD_USERNAME,
                     NEXTCLOUD_PASSWORD), headers=headers)
    return r


def createNewForm():
    '''
    Endpoint: /api/v1.1/form
    Method: POST
    Parameters: None
    Response: The new form object.
    "data": {
    "id": 7,
    "hash": "L2HWf8ixX9rNzKnX",
    "title": "",
    "description": "",
    "ownerId": "jonas",
    "created": 1611257716,
    "access": {
        "type": "public"
    },
    "expires": null,
    "isAnonymous": null,
    "submitOnce": true,
    "questions": [],
    "canSubmit": true
    }
    '''
    endpoint = '/api/v1.1/form'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.post(url, auth=(NEXTCLOUD_USERNAME,
                      NEXTCLOUD_PASSWORD), headers=headers)
    return r


def requestFullDataOfAForm(id: int):
    '''
    Returns the full-depth object of the requested form (without submissions).

    Endpoint: /api/v1.1/form/{id}
    Url-Parameter:
    Parameter	Type	Description
    id	Integer	ID of the form to request
    Method: GET
    Response: A full object of the form, including access, questions and options in full depth.
    "data": {
    "id": 3,
    "hash": "em4djk8B9BpXnkYG",
    "title": "Form 1",
    "description": "Description Text",
    "ownerId": "jonas",
    "created": 1611240961,
    "access": {
        "users": [],
        "groups": [],
        "type": "public"
    },
    "expires": 0,
    "isAnonymous": false,
    "submitOnce": false,
    "canSubmit": true,
    "questions": [
        {
        "id": 1,
        "formId": 3,
        "order": 1,
        "type": "dropdown",
        "mandatory": false, // deprecated, will be removed in API v2
        "isRequired": false,
        "text": "Question 1",
        "options": [
            {
            "id": 1,
            "questionId": 1,
            "text": "Option 1"
            },
            {
            "id": 2,
            "questionId": 1,
            "text": "Option 2"
            }
        ]
        },
        {
        "id": 2,
        "formId": 3,
        "order": 2,
        "type": "short",
        "mandatory": true, // deprecated, will be removed in API v2
        "isRequired": true,
        "text": "Question 2",
        "options": []
        }
    ]
    }
    '''
    endpoint = '/api/v1.1/form'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint + f'/{id}'
    headers = {'OCS-APIRequest': 'true'}
    r = requests.get(url, auth=(NEXTCLOUD_USERNAME,
                     NEXTCLOUD_PASSWORD), headers=headers)
    return r


def cloneAForm(id: int):
    '''
    Creates a clone of a form (without submissions).

    Endpoint: /api/v1.1/form/clone/{id}
    Url-Parameter:
    Parameter	Type	Description
    id	Integer	ID of the form to clone
    Method: POST
    Response: Returns the full object of the new form. See Request full data of a Form
    See section 'Request full data of a form'.

    '''
    endpoint = '/api/v1.1/form/clone'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint + f'/{id}'
    headers = {'OCS-APIRequest': 'true'}
    r = requests.post(url, auth=(NEXTCLOUD_USERNAME,
                      NEXTCLOUD_PASSWORD), headers=headers)
    return r


def updateFormProperties(data: dict):
    '''
    TODO: need to be checked, how the array has to look and
    how to pass it.
    Update a single or multiple properties of a form-object.
    Concerns only the Form-Object, properties of Questions,
    Options and Submissions, as well as their creation or
    deletion, are handled separately.

    Endpoint: /api/v1.1/form/update
    Method: POST
    Parameters:
    Parameter	    Type	Description
    id	            Integer	ID of the form to update
    keyValuePairs	Array	Array of key-value pairs to update
    Restrictions: It is not allowed to update one of the following key-value pairs: id, hash, ownerId, created
    Response: Status-Code OK, as well as the id of the updated form.
    "data": 3
    '''
    endpoint = '/api/v1.1/form/update'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint
    headers = {
        'OCS-APIRequest': 'true',
        # 'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(url, auth=(NEXTCLOUD_USERNAME,
                      NEXTCLOUD_PASSWORD), headers=headers, json=data)
    return r


def deleteAForm(id: int, keyValuePairs: dict):
    '''
    Endpoint: /api/v1.1/form/{id}
    Url-Parameter:
    Parameter	Type	Description
    id	Integer	ID of the form to delete
    Method: DELETE
    Response: Status-Code OK, as well as the id of the deleted form.
    "data": 3
    '''
    endpoint = '/api/v1.1/form'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint + f'/{id}'
    headers = {'OCS-APIRequest': 'true'}
    r = requests.delete(url, auth=(NEXTCLOUD_USERNAME,
                                   NEXTCLOUD_PASSWORD), headers=headers)
    return r


def getSubmissionsAsCSV(formshash: str):
    '''
    Returns all submissions to the form in form of a csv-file.

    Endpoint: /api/v1.1/submissions/export/{hash}
    Url-Parameter:
    Parameter	Type	Description
    hash	    String	Hash of the form to get the submissions for
    Method: GET
    Response: A Data Download Response containg the headers Content-Disposition:
    attachment; filename="Form 1 (responses).csv" and Content-Type: text/csv;charset=UTF-8. 
    The actual data contains all submissions to the referred form, formatted as 
    comma separated and escaped csv.
    '''
    endpoint = '/api/v1.1/submissions/export'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint + f'/{formshash}'
    headers = {'OCS-APIRequest': 'true'}
    r = requests.get(url, auth=(NEXTCLOUD_USERNAME,
                     NEXTCLOUD_PASSWORD), headers=headers)
    return r


def exportSubmissionsToCloud(formshash: str, path: str):
    '''
    Creates a csv file and stores it to the cloud, resp. Files-App.

    Endpoint: /api/v1.1/submissions/export
    Method: POST
    Parameters:
    Parameter	Type	Description
    hash	    String	Hash of the form to get the submissions for
    path	    String	Path within User-Dir, to store the file to
    Response: Stores the file to the given path and returns the fileName.
    "data": "Form 2 (responses).csv"
    '''
    endpoint = '/api/v1.1/submissions/export'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint
    data = {
        "hash": formshash,
        "path": path
    }
    headers = {'OCS-APIRequest': 'true'}
    r = requests.post(url, auth=(NEXTCLOUD_USERNAME,
                                 NEXTCLOUD_PASSWORD), headers=headers, json=data)
    return r


if __name__ == "__main__":
    # print(getFormData(NEXTCLOUD_FORM).text)
    # print(getFormsOfUser().text)
    print(requestFullDataOfAForm(9).text)
    # print(createNewForm().text)
    # data={
    #     "id":9,
    #     "keyValuePairs":
    #         {
    #         "title":"Testtitel",
    #         "description":"Dies ist eine Testform"
    #         }
    #     }
    # print(updateFormProperties(data).text)

    pass
