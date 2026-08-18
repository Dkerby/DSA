class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.currentTime = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        # add the tweet to the list of tweets, with a global timestamp value
        self.tweets[userId].append((self.currentTime * -1, tweetId))
        self.currentTime += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # look at each of the people the user is currently following, and grab their posts,
        # plus their own posts, and throw them in a max-heap
        maxheap = []
        self.follows[userId].add(userId)
        for followee in self.follows[userId]:
            for tweet in self.tweets[followee]: 
                heapq.heappush(maxheap, tweet)
        
        smallest = heapq.nsmallest(10, maxheap)
        
        res = []
        for tweet in smallest:
            res.append(tweet[1])

        return res 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)