class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # count = {1:1,2:2,3:3} {num:freq}
        n = len(nums) # 6
        bucket = [] #[0,1,2,3,4,5,6] 最多出現6次 (n) ,n+1 index, 出現的頻率==index
        for i in range(0,n+1):
            bucket.append([]) #[[],[1],[2],[3],[],[],[]]
        
        for num,freq in count.items():
            bucket[freq].append(num) #1,1 #2,2 #3,3

        res = []
        for i in range(n,0,-1):
            for val in bucket[i]:
                if len(res) == k:
                    return res
                res.append(val)
        
        return res

