from cgitb import text
from mimetypes import init
from deck import *
from forms import *
import json
import csv
from datetime import datetime, timezone

NEXTCLOUD_URL_DECK = credentials.url2
NEXTCLOUD_URL_FORMS = credentials.url
NEXTCLOUD_USERNAME = credentials.username
NEXTCLOUD_PASSWORD = credentials.password
NEXTCLOUD_FORM = credentials.form
NEXTCLOUD_APP_DECK = 'apps/deck'
NEXTCLOUD_APP_FORMS = 'apps/forms'


class NewSubmission():

   def __init__(self, author, errtype, errtext, errlocation, timestamp):
        self.author = author
        self.type = errtype
        self.text = errtext
        self.location = errlocation
        self.timestamp = timestamp

    # def __repr__(self):
    #     return f'submission {self.text}'


def getAllSubmissions():
    ''' get all submissions and save them as python object'''
    # save json to variable
    data = getFormSubmissions('WgTCRZwyi6WfTEa2').json()
    return data


def getHash(file):
    with open(file, newline='') as f:
        reader = csv.reader(f)
        answers = list(reader)
    if len(answers) > 0:
        answers = answers[0]
    return answers


def setHash(file):
    ''' saves new hashes to file'''
    with open(file, "w", newline='') as f:
        spamwriter = csv.writer(f, delimiter=',')
        spamwriter.writerow(answers)


def getNewSubmissions(file, data):
    ''' Get all submissions'''
    for answer in data["ocs"]["data"]["submissions"]:
        # Check if submission is already in known answers
        if str(answer["id"]) in answers:
            print(f'{answer["id"]} ist schon in der Liste')
        else:
            # Submission is new, so it gets appended to known anwers and saved in file
            print(f'Beitrag mit id {answer["id"]} ist neu und wird hinzugefügt.')
            answers.append(answer["id"])
            setHash(file)
            # just debugging purposes
            print(answer["answers"][0]["text"])  # text
            print(answer["answers"][1]["text"])  # type
            print(answer["answers"][2]["text"])  # room
            print(answer["timestamp"])  # timestamp
            print(answer["userId"])  # userId
            # cast str to datetime
            utc_time = datetime.fromtimestamp(answer["timestamp"], timezone.utc)
            local_time = utc_time.astimezone().strftime("%Y-%m-%d %H:%M:%S")
            # append new submission to list of new submissions
            tickets.append(NewSubmission(
                answer["userId"], answer["answers"][1]["text"], answer["answers"][0]["text"], answer["answers"][2]["text"], local_time))
    for ticket in tickets:
        print(ticket.author, ticket.type, ticket.text, ticket.location, ticket.timestamp)


def returnDataForNewCard(sub: NewSubmission):
    carddata = {
        "title": f"{sub.type}: {sub.location}",
        "type": "plain",
        "order": 999,
        "description": f"{sub.text}\n{sub.author}",
        "duedate": f"{sub.timestamp}"
    }
    return carddata

if __name__ == '__main__':
    file = "answers.csv"
    answers = getHash(file)
    tickets = []
    data = getAllSubmissions()
    getNewSubmissions(file, data)
    for ticket in tickets:
        carddata = returnDataForNewCard(ticket)
        createANewCard(42, 121, carddata)

    # r = getAListOfBoards({"details":"true"}).json()
    # for item in r:
    #     print(json.dumps(item, indent=2))

    # board = getCardDetails(42,121,272).json()
    # print(json.dumps(board, indent=2))

    # for item in board:
    #     print(json.dumps(item, indent=2))
