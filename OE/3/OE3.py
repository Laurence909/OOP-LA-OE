#OE3
class SocialMideaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def login (self):
        print(f"{self.username} login succesfully")
    def post (self):
        print(f"{self.username} has posted a content")

class InstagramAccount(SocialMideaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers
    def share_story(self):
        print(f"INSTAGRAM: {self.username} posted a story")
    def followers(self):
        print(f"{self.username} has a number of followers of: {self.number_of_followers}")
    
class TwitterAccount(SocialMideaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets
    def post_tweet(self):
        print(f"TWITTER: {self.username} posted a tweet")
    def numOfTweets(self):
        print(f"{self.username} has a number of followers of: {self.number_of_tweets}")
    
instaUser = SocialMideaAccount("Laurence", "laurence123")
instaUser.login()
instaUser.post()
print()
instaUser = InstagramAccount("Laurence", "laurence123", 500)
instaUser.share_story()
instaUser.followers()
print()
TwtUser =TwitterAccount("Laurence", "laurence123", 1000)
TwtUser.post_tweet()
TwtUser.numOfTweets()
