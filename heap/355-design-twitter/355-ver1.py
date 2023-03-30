from ast import List
from collections import deque


class Twitter:
    # does not work
    # but the data structure is right
    def __init__(self):
        self.tweets = {}
        self.followers = set()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = deque()
        # heapq.heapify(feed)
        for t in self.tweets:
            # heapq.heappush(feed, t[1])
            feed.appendleft(t[1])

        while len(feed) > 10:
            # heapq.heappop(feed)
            feed.popright()
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers.add((followerId, followeeId))

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers.remove((followerId, followeeId))


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
