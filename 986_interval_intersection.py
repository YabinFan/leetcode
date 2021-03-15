class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # [1,  3]
        #   [2,   4 ]
        # start = max(two starts)
        # end = min(two ends)
        result = []
        i = j = 0
        start, end = 0,1
        while i< len(firstList) and j < len(secondList):
            low = max(firstList[i][start], secondList[j][start])
            high = min(firstList[i][end], secondList[j][end])
            if low <= high:
                result.append([low, high])
            if firstList[i][end] <= secondList[j][end]: 
                 # Let's say the current range in A has end value smaller than to equal to end value of the current range in B, that essentially means that you have exhausted that range in A and you should move on to the next range. 
                i+=1
            else:
                j+=1
        return result

