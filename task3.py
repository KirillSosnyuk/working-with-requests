import requests
import datetime
from pprint import pprint

class StackOverflow:
    def __init__(self, params):
        self.questions = 'https://api.stackexchange.com/' + '2.3/questions'
        self.params = params
    def get_two_days_questions(self):
        response = requests.get(self.questions, params=self.params)
        pprint(response.json())


if __name__ == '__main__':
    now = int(datetime.datetime.timestamp(datetime.datetime.now()))
    past_date = int(datetime.datetime.timestamp(datetime.datetime.today() - datetime.timedelta(days=2)))
    params = {'fromdate' : past_date, 'todate' : now, 'tagged' : 'Python', 'sort': 'creation', 'order' : 'desc', 'site': 'stackoverflow'}
    questions = StackOverflow(params)
    questions.get_two_days_questions()

