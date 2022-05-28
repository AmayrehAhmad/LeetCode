import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        freq, Q = {}, []
        for char in s:
            if char not in freq:
                freq[char] = 1
            else: freq[char] += 1
                
        
        for key, value in freq.items():
            Q.append((value,key))
            heapq._heapify_max(Q)
        
        ans = ""
        while len(Q) > 0:
            freq, char = heapq.heappop(Q)
            heapq._heapify_max(Q)
            ans += char*freq
            
        return ans
            