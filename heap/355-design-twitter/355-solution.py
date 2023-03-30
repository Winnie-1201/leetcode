from ast import List
from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        # self.tweets.append([userId, tweetId])
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followerMap[userId]:
            # check if the followee has any tweet
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                # get the last element in the followee tweetMap
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(
                    minHeap, [count, tweetId, followeeId, index - 1])
        return res
        # feed = []
        # heapq.heapify(feed)
        # followers = self.followMap[userId]
        # for f in followers:
        #     tweets = self.tweetMap[f]
        #     for t in tweets:
        #         heapq.heappush(t[1])

    def follow(self, followerId: int, followeeId: int) -> None:
        # self.followers.add((followerId, followeeId))
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # self.followers.remove((followerId, followeeId))
        if followerId in self.followMap:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
