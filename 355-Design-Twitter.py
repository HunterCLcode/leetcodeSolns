class Twitter:

    def __init__(self):
        # User -> Following Users
        self.followMap = defaultdict(set)
        # User -> Posts Made
        self.postMap = defaultdict(list)
        # Timer
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append([self.time,tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap = []
        
        self.followMap[userId].add(userId)
        for user in self.followMap[userId]:
            if user in self.postMap:
                index = len(self.postMap[user]) - 1
                t, pid = self.postMap[user][index]
                maxheap.append([t, pid, user, index - 1])
        heapq.heapify(maxheap)
        res = []
        
        for i in range(10):
            if maxheap:
                _, pid, uid, index = heapq.heappop(maxheap)
                res.append(pid)

                if index >= 0:
                    t, pid = self.postMap[uid][index]
                    heapq.heappush(maxheap,[t, pid, uid, index - 1])
            else:
                break
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.followMap[followerId]: self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
