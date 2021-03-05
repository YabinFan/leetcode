class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # What is the length of longest subarray that contains up to two distinct integers?
        d = {}
        longest = 0
        window_start = 0
        for window_end in range(len(tree)):
            curr_num = tree[window_end]
            d[curr_num] = d.get(curr_num,0)+1
            while len(d) > 2:
                left_num = tree[window_start]
                d[left_num] -=1
                if d[left_num] == 0:
                    del d[left_num]
                window_start +=1
            longest = max(longest, window_end-window_start+1)
        return longest
