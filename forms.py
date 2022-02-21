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
    r = requests.get(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers
                     )
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
    r = requests.get(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers
                     )
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
    r = requests.post(url,
                      auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                      headers=headers
                      )
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
    r = requests.get(url,
                     auth=(NEXTCLOUD_USERNAME,  NEXTCLOUD_PASSWORD),
                     headers=headers
                     )
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
    r = requests.post(url,
                      auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                      headers=headers
                      )
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
    r = requests.post(url,
                      auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                      headers=headers,
                      json=data
                      )
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
    r = requests.delete(url,
                        auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                        headers=headers
                        )
    return r


def createANewQuestion(data: dict):
    '''
    Endpoint: /api/v1.1/question
    Method: POST
    Parameters:
    Parameter	Type	       Optional	Description
    formId	    Integer		            ID of the form, the new question will belong to
    type	    QuestionType		    The question-type of the new question
    text	    String	       yes	    Optional The text of the new question.
    Response: The new question object.
    "data": {
    "id": 3,
    "formId": 3,
    "order": 3,
    "type": "short",
    "mandatory": false, // deprecated, will be removed in API v2
    "isRequired": false,
    "text": "",
    "options": []
    }

    Question Types
    Currently supported Question-Types are:

    Type-ID	            Description
    multiple	        Typically known as 'Checkboxes'. Using pre-defined options, the user can select one or multiple from. Needs at least one option available.
    multiple_unique	    Typically known as 'Radio Buttons'. Using pre-defined options, the user can select exactly one from. Needs at least one option available.
    dropdown	        Similar to multiple_unique, but rendered as dropdown field.
    short	            A short text answer. Single text line
    long	            A long text answer. Multi-line supported
    date	            Showing a dropdown calendar to select a date.
    datetime	        Showing a dropdown calendar to select a date and a time.
    '''
    endpoint = '/api/v1.1/question'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint
    headers = {
        'OCS-APIRequest': 'true',
        # 'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(url,
                      auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                      headers=headers,
                      json=data
                      )
    return r


def updateQuestionProperties(data: dict):
    '''
    Update a single or multiple properties of a question-object.

    Endpoint: /api/v1.1/question/update
    Method: POST
    Parameters:
    Parameter	Type	Description
    id	Integer	ID of the question to update
    keyValuePairs	Array	Array of key-value pairs to update
    Restrictions: It is not allowed to update one of the following 
    key-value pairs: id, formId, order.
    Response: Status-Code OK, as well as the id of the updated question.
    "data": 1
    '''
    endpoint = '/api/v1.1/question/update'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint
    headers = {
        'OCS-APIRequest': 'true',
        # 'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(url,
                      auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                      headers=headers,
                      json=data
                      )
    return r


def reorderQuestions(data: dict):
    '''
    Reorders all Questions of a single form

    Endpoint: /api/v1.1/question/reorder
    Method: POST
    Parameters:
    Parameter	Type	Description
    formId	    Integer	ID of the form, the questions belong to
    newOrder	Array	Array of all Question-IDs, ordered in the desired order
    Restrictions: The Array must contain all Question-IDs corresponding to the specified form and must not contain any duplicates.
    Response: Array of questionIDs and their corresponding order.
    "data": {
    "1": {
        "order": 1
    },
    "2": {
        "order": 3
    },
    "3": {
        "order": 2
    }
    }
    '''
    endpoint = '/api/v1.1/question/reorder'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint
    headers = {
        'OCS-APIRequest': 'true',
        # 'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(url,
                      auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                      headers=headers,
                      json=data
                      )
    return r


def deleteAQuestion(id: int):
    '''
    Endpoint: /api/v1.1/question/{id}
    Url-Parameter:
    Parameter	Type	Description
    id	        Integer	ID of the question to delete
    Method: DELETE
    Response: Status-Code OK, as well as the id of the deleted question.
    "data": 4
    '''
    endpoint = '/api/v1.1/question'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint + f'/{id}'
    headers = {
        'OCS-APIRequest': 'true',
        # 'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.delete(url,
                        auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                        headers=headers
                        )
    return r


def createANewOption(data: dict):
    '''
    Contains only manipulative question-endpoints. To retrieve options, request the full form data.

    Create a new Option
    Endpoint: /api/v1.1/option
    Method: POST
    Parameters:
    Parameter	Type	Description
    questionId	Integer	ID of the question, the new option will belong to
    text	    String	The text of the new option
    Response: The new option object
    "data": {
    "id": 7,
    "questionId": 1,
    "text": "test"
    }
    '''
    endpoint = '/api/v1.1/option'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.post(url,
                      auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                      headers=headers,
                      json=data
                      )
    return r


def updateOptionProperties(data: dict):
    '''
    Endpoint: /api/v1.1/option/update
    Method: POST
    Parameters:
    Parameter	    Type	Description
    id	            Integer	ID of the option to update
    keyValuePairs	Array	Array of key-value pairs to update
    Restrictions: It is not allowed to update one of the following key-value pairs: id, questionId.
    Response: Status-Code OK, as well as the id of the updated option.
    "data": 7
    '''
    endpoint = '/api/v1.1/option/update'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.post(url,
                      auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                      headers=headers,
                      json=data
                      )
    return r


def deleteAnOption(id: int):
    '''
    Endpoint: /api/v1.1/option/{id}
    Url-Parameter:
    Parameter	Type	Description
    id	        Integer	ID of the option to delete
    Method: DELETE
    Response: Status-Code OK, as well as the id of the deleted option.
    "data": 7
    '''
    endpoint = '/api/v1.1/option'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint + f'/{id}'
    headers = {'OCS-APIRequest': 'true'}
    r = requests.delete(url,
                        auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                        headers=headers
                        )
    return r


def getFormSubmissions(formshash: str):
    '''
    Get all Submissions to a Form

    Endpoint: /api/v1.1/submissions/{hash}
    Url-Parameter:
    Parameter	Type	Description
    hash	    String	Hash of the form to get the submissions for
    Method: GET
    Response: An Array of all submissions, sorted as newest first, as well as an array of the corresponding questions.
    "data": {
    "submissions": [
        {
        "id": 6,
        "formId": 3,
        "userId": "jonas",
        "timestamp": 1611274453,
        "answers": [
            {
            "id": 8,
            "submissionId": 6,
            "questionId": 1,
            "text": "Option 3"
            },
            {
            "id": 9,
            "submissionId": 6,
            "questionId": 2,
            "text": "One more."
            },
        ],
        "userDisplayName": "jonas"
        },
        {
        "id": 5,
        "formId": 3,
        "userId": "jonas",
        "timestamp": 1611274433,
        "answers": [
            {
            "id": 5,
            "submissionId": 5,
            "questionId": 1,
            "text": "Option 2"
            },
            {
            "id": 6,
            "submissionId": 5,
            "questionId": 2,
            "text": "This is an answer."
            },
        ],
        "userDisplayName": "jonas"
        }
    ],
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
            "id": 27,
            "questionId": 1,
            "text": "Option 2"
            },
            {
            "id": 30,
            "questionId": 1,
            "text": "Option 3"
            }
        ]
        },
        {
        "id": 2,
        "formId": 3,
        "order": 2,
        "type": "short",
        "mandatory": true, // deprecated will be removed in API v2
        "isRequired": true,
        "text": "Question 2",
        "options": []
        }
    ]
    }
    '''
    endpoint = '/api/v1.1/submissions'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint + f'/{formshash}'
    headers = {'OCS-APIRequest': 'true'}
    r = requests.get(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers
                     )
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
    r = requests.get(url,
                     auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                     headers=headers
                     )
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


def deleteSubmissions(id: int):
    '''
    Delete all Submissions to a form

    Endpoint: /api/v1.1/submissions/{formId}
    Url-Parameter:
    Parameter	Type	Description
    formId	    Integer	ID of the form to delete the submissions for
    Method: DELETE
    Response: Status-Code OK, as well as the id of the corresponding form.
    "data": 3
    '''
    endpoint = '/api/v1.1/submissions'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint + f'/{id}'
    headers = {'OCS-APIRequest': 'true'}
    r = requests.delete(url,
                        auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                        headers=headers
                        )
    return r


def insertASubmission(data: dict):
    '''
    Store Submission to Database

    Endpoint: /api/v1.1/submission/insert
    Method: POST
    Parameters:
    Parameter	Type	Description
    formId	    Integer	ID of the form to submit into
    answers	    Array	Array of Answers
    The Array of Answers has the following structure:		
    QuestionID as key
    An array of values as value --> Even for short Text Answers, wrapped into Array.
    For Question-Types with pre-defined answers (multiple, multiple_unique, dropdown), the array contains the corresponding option-IDs.
    {
    "1":[27,32],              // dropdown or multiple
    "2":["ShortTextAnswer"],  // All Text-Based Question-Types
    }
    Response: Status-Code OK.
    '''
    endpoint = '/api/v1.1/submission/insert'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint
    headers = {'OCS-APIRequest': 'true'}
    r = requests.post(url,
                      auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                      headers=headers,
                      json=data
                      )
    return r


def deleteASingleSubmission(id: int):
    '''
    Endpoint: /api/v1.1/submission/{id}
    Url-Parameter:
    Parameter	Type	Description
    id	        Integer	ID of the submission to delete
    Method: DELETE
    Response: Status-Code OK, as well as the id of the deleted submission.
    "data": 5
    '''
    endpoint = '/api/v1.1/submission'
    url = NEXTCLOUD_URL + NEXTCLOUD_APP + endpoint + f'/{id}'
    headers = {'OCS-APIRequest': 'true'}
    r = requests.delete(url,
                        auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                        headers=headers
                        )
    return r


if __name__ == "__main__":
    # listOwnedForms()
    # listSharedForms()
    # createNewForm()
    # requestFullDataOfAForm()
    # cloneAForm()
    # updateFormProperties()
    # deleteAForm()
    # createANewQuestion()
    # updateQuestionProperties()
    # reorderQuestions()
    # deleteAQuestion()
    # createANewOption()
    # updateOptionProperties()
    # deleteAnOption()
    # getSubmissionsAsCSV()
    # exportSubmissionsToCloud()
    pass
