import twitter, time, json
import numpy
import csv

# Load config from JSON
with open('config.json') as data_file:
    json = json.load(data_file)

# Connect to Twitter API
api = twitter.Api(consumer_key=json['twitter']['consumer_key'],
                      consumer_secret=json['twitter']['consumer_secret'],
                      access_token_key=json['twitter']['access_token_key'],
                      access_token_secret=json['twitter']['access_token_secret'])
# Printing payload to verify Twitter access is working
#print(api.VerifyCredentials())


with open('C:\\Users\\teja\\Documents\\1.MS\\1.Masters\\RA\\screennames_1_300.json') as f:
    words = [word.strip() for word in f]

# Get all followers from users in array
followers = []
users = []
myfile1 = open("followers.csv", "a")
myfile2 = open("followersOnly.csv","a")
writer1 = csv.writer(myfile1, lineterminator="\n")
writer2 = csv.writer(myfile2, lineterminator="\n")
for name in words:
    sec = api.GetSleepTime('/followers/list') + 2 # Wait 2 seconds more to make sure rate-limit is avoided
    print 'Will wait {0} sec to avoid rate-limit'.format(sec)
    time.sleep(sec)
    print 'Fetching followers for {0}...'.format(name)
    # Uncomment the next line to instead fetch from the /followers/list API (takes much longer)
    #friends = api.GetFollowers(screen_name=name, skip_status=True, count=200, include_user_entities=False)
    try:
        followers = []
        followers = api.GetFollowerIDs(screen_name=name)
        users.append(followers)
        writer2.writerow(followers)
        followers.insert(0, name)
        writer1.writerow(followers)
    except:
        print 'Cant write the followers of'+name+' to file...(query failed)'
        lis = ["N/A"]
        users.append(lis)
        writer2.writerow(lis)
        followers.insert(0, name)
        followers.append("N/A")
        writer1.writerow(followers)
