class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = {}
        for n in nums:
            arr[n] = arr.get(n, 0) + 1
        temp = dict(islice(sorted(arr.items(), key=lambda item:item[1], reverse=True), k))
        return list(temp.keys())
