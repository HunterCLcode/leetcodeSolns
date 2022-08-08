class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue, maxHeap, hmap = deque([[1, 'X'] for i in range(n)]), [], defaultdict(int)
        
        # Init hmap with vals and then add count to minheap tied to key
        for task in tasks:
            hmap[task] += 1
        for key, value in hmap.items():
            maxHeap.append([-1 * value,key])
        heapq.heapify(maxHeap)

        res = 0
        # While we have values in hmap
        while hmap:
            res += 1
            
            num, curTask = heapq.heappop(maxHeap)
            num += 1

            if num == 0:
                hmap.pop(curTask)
                queue.append([1, 'X'])
            else:
                queue.append([num, curTask])

            heapq.heappush(maxHeap, queue.popleft())
        return res
