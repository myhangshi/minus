class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):
        # Write your code here
        
        withInt = []
        withStr = []
        
        for i in logs:
            if i.split(' ')[-1].isdigit():
                withInt.append(i)
            else:
                withStr.append(i)
        
        return sorted(withStr, key = Solution.mykey) + withInt
    
    @staticmethod    
    def mykey(x):
        pos = x.index(' ')
        return (x[pos+1:], x[:pos])
