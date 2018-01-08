import requests
import json

from requests_oauthlib import OAuth1

# >>> import twitter
# >>> api = twitter.Api(consumer_key='consumer_key',
#                       consumer_secret='consumer_secret',
#                       access_token_key='access_token',
#                       access_token_secret='access_token_secret')

class Api:
    def __init__(self,                  
                 consumer_key=None,
                 consumer_secret=None,
                 access_token_key=None,
                 access_token_secret=None):

        self.__url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
        self.__auth = OAuth1(consumer_key, consumer_secret,
                           access_token_key, access_token_secret)

    def GetHomeTimeline(self):
        r = requests.get('https://api.twitter.com/1.1/statuses/home_timeline.json', 
                          auth=self.__auth)
        
        timeline = json.loads(r.text)
        for t in timeline:
            print(t['text'] + '\n')

    def GetUserTimeline(self, username):
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=' + username + '&count=20&tweet_mode=extended'
        r = requests.get(url, auth=self.__auth)
        timeline = json.loads(r.text)
        # print(timeline)
        for t in timeline:
            if 'retweeted_status' not in t:
                print(t['full_text'])
            else:
                print('RT: ' + t['retweeted_status']['full_text'])
    
    # returns list names with list ids
    def GetLists(self):
        url = 'https://api.twitter.com/1.1/lists/list.json'
        r = requests.get(url, auth=self.__auth)
        lists = json.loads(r.text)

        return [(l['name'], l['id_str']) for l in lists]

    def GetListStatuses(self, list_id):
        url = 'https://api.twitter.com/1.1/lists/statuses.json?list_id='+list_id+'&cursor=-1&tweet_mode=extended'
        r = requests.get(url, auth=self.__auth)
        timeline = json.loads(r.text)
        # print(timeline)
        for t in timeline:
            if 'retweeted_status' not in t:
                print(t['full_text'])
            else:
                print('RT: ' + t['retweeted_status']['full_text'])

    def GetListMembers(self, list_id):
        url = 'https://api.twitter.com/1.1/lists/members.json?list_id='+list_id+'&cursor=-1'
        r = requests.get(url, auth=self.__auth)
        members = json.loads(r.text)
        # print(json.dumps(members, indent=2, sort_keys=True))
        return [(u['name'], u['screen_name']) for u in members['users']]

    def AddListMembers(self, list_id, members): 
        s = ""

        if type(members) is list:
            s = reduce( (lambda x, y: x + y), members )  

        if type(members) is str:
            s = members
        
        url = 'https://api.twitter.com/1.1/lists/members/create_all.json?screen_name='+members+'&list_id='+list_id

        r = requests.post(url, auth=self.__auth)
        return json.loads(r.text)


    def CreateList(self, list_name):
        url = 'https://api.twitter.com/1.1/lists/create.json?name='+list_name+'&mode=private&description=description'
        return requests.post(url, auth=self.__auth)
        
    def RemoveListMember(self, list_id, name):
        url = 'https://api.twitter.com/1.1/lists/members/destroy?screen_name='+name+'&list_id='+list_id
        return requests.post(url, auth=self.__auth)