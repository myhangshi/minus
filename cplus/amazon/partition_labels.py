class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        mp = {c:i for i, c in enumerate(S)}
        
        result = []
        last = 0 
        anchor = 0
        for i, c in enumerate(S):  
            last = max(last, mp[S[i]])
            if i == last: 
                result.append(i-anchor + 1)
                anchor = last + 1 
        
        return result 
