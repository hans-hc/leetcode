class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] #the numbers of empty arrays is the size of the input + 1

        for n in nums:
            count[n] = 1 + count.get(n,0) #if n doesnt already exist, default number to 0

        for n, c in count.items(): #return key value pair
            freq[c].append(n) #this value n occurs c number of times
        
        result = [] #we want the top k elements
        for i in range(len(freq)-1, 0, -1): #descending order
            for n in freq[i]: #anything in i is a sublist
                result.append(n) #we're getting the n value that occurs the most frequently
                if len(result) == k:
                    return result


        


