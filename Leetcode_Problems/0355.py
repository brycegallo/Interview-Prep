# LeetCode 0355 - Design Twitter
# Medium - Heap / Priority Queue - (actually harder than many Hard problems)
# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.
# Implement the Twitter class:
#    Twitter() Initializes your twitter object.
#    void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
#    List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
#    void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
#    void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# Solution with Min Heap, and defaultdic builtins including Sets
# Complexities:
# Time : O(n * logn) for each getNewsFeed() call - O(1) for other functions
# Space: O(N∗m+N∗M+n) - Where n is the total number of followeeIds associated with the userId, m is the maximum number of tweets by any user, N is the total number of userIds and M is the maximum number of followees for any user. 
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.follow_map = defaultdict(set)  # userId -> set of followeeIds


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []  # ordered starting from recent
        min_heap = []

        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                count, tweetId = self.tweet_map[followeeId][index]
                min_heap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(min_heap)
        while min_heap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            result.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)

