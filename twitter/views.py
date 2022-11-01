from django.shortcuts import render
import tweepy
# Create your views here.

# API_KEY = HYhS1Hh84n3GgQnlg4oMf86hI
# API_Key_Secret = fwxJ7QgnfZjw9gp7k5TIzkXNjrccArrGsQ2h8Zf0tL8tNL0693
# Bearer_TOEKN = AAAAAAAAAAAAAAAAAAAAADkFhQEAAAAAS8fhBwcDiCma5GxROT%2Fld8gbFmU%3DnPzmsbVPQTzZrLZI45seGTDdNibssylLrbM5WtNiXxRnRYjE5U
# Access Token = 1569967691565355008-gvIjzhId7fNWcTJXueK9tbJfXQzIXW
# Access Token Secret = tq3uOe4UdUjuKeZ6jcHwjRkiaRqS7U9i9RU77GlQgETz3
# CLient ID = VVRfVk1GdTZGTGFVZmJhZjdHWkU6MTpjaQ
# Client Secret = g9ZTBsQJnk8W0giTpLcsQD4wflZl6LOuIzGyqUpJ-Tqj9JA_uB
#User id=2244994945

def TweepyView(request):
    Bearer_Token = 'AAAAAAAAAAAAAAAAAAAAADkFhQEAAAAAS8fhBwcDiCma5GxROT%2Fld8gbFmU%3DnPzmsbVPQTzZrLZI45seGTDdNibssylLrbM5WtNiXxRnRYjE5U'
    
    # getting more than 100 tweets : tweepy.paginator
    client = tweepy.Client(Bearer_Token)
    response = client.search_recent_tweets(
        query='mahsa -is:retweet',max_results = 10,tweet_fields=['lang','created_at'],
        user_fields=['profile_image_url'],expansions = ['author_id'])

    # for getting user id
    # user_name = client.get_users(usernames = ['TwitterDev'])
    # print(user_name)
    # for accessing all tweets of the user by id
    # tweets = client.get_users_tweets(2244994945)
    # print(tweets.meta)

    # Making a list of dictionries for users id and username
    users = {u['id']:u for u in response.includes['users']}
   
    # # for making a file with tweet id
    # with open('tweet.txt','+a') as file:
    #     for u in users.keys():
    #         file.write(f"{u}\n")

    #Counting recent tweet
    # tweet_counts = client.get_recent_tweets_count(query = 'mahsa -is:retweet',granularity = 'day')
    # for u in tweet_counts:
    #     print(u)

    # for accessing to place of user we need to have a academic bearer token
    # expansions = ['geo.place_id']
    # places = {r['id']:r for r in response.includes['places']}

    # get followers 
    # followers_image = []
    # q = client.get_users_followers(2244994945,user_fields = ['profile_image_url'])
    # for i in q.data:
    #     followers_image.append(i['profile_image_url'])


    liking_users = client.get_liking_users(1228393702244134912)
    for user in liking_users.data:
        print(user)
    
    users_list = {}

    for tweet in response.data:
        if users[tweet['author_id']]:
            user = users[tweet['author_id']]
            users_list.update({user['username']:tweet.text})
    
    

    context = {
        'response':response,
        'users':users_list,
        # 'followers_image':followers_image
    }
    return render(request,'twitter/index.html',context)