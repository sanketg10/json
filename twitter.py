import tweepy, json

consumer_key = '2xX7O8JmoKFrK6qlz0mYf3TRi' 
consumer_secret = 'tK9YqjgfXi38GVkXXalL0D5SMzGu2In5rsNtryBgGL7BXVJyvZ' 
access_token = '246323037-kf0NrAa9BgoQ0O7fnvLF5t9JYVF2NTBIMxy5JAky' 
access_token_secret = 'Q0cEnaypuZk6A6yTO7T6CGeX8pr3QxKObRJcTX2nNMJHb'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth) 

print api #Just to check connection if it is working 

public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text


# For India it is 23424848, US it is 23424977, and for world it is 1
world_trends = api.trends_place(23424848)

json_trends = json.dumps(world_trends, indent=1) #indent=1 gives a nice serial format
print json_trends  #Will print the string in JSON format

# print type(world_trends) --- List
# print type(json_trends)  --- String 

dict = world_trends[0]
print type(dict)   #Dict 

trenddata= dict['trends']  
for i in trenddata: 
    print i['name'] 

# From http://stackoverflow.com/questions/19483351/converting-json-string-to-dictionary-not-list-python
dict2 = json.loads(json_trends)[0]  
print type(dict2) #Dict if there is [0] in the end otherwise it is a list

trenddata2= dict2['trends'] 
for i in trenddata2: 
    print i['name']

# import json
# weather = urllib2.urlopen('url')
# wjson = weather.read()
# wjdata = json.loads(wjson)
# print wjdata['data']['current_condition'][0]['temp_C']

# world_trends is a list with only one element in it, which is a 
# dict which we'll put in data.
data = world_trends[0] 
# grab the trends
trends = data['trends'] 
# grab the name from each trend
names = [trend['name'] for trend in trends]
# put all the names together with a ' ' separating them
trendsName = ' , '.join(names) 
# print(trendsName) 

# print
# print us_trends