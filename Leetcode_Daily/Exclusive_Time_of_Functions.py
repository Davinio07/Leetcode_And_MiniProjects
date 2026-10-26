class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """ 
        Times_Of_Functions: list = [0] * n
        stack: list = []
        current_time: int = 0
        time_passed: int = 0
        
        for log in logs:
            func_id, action, timestamp = log.split(":")
            func_id: int = int(func_id)
            timestamp: int = int(timestamp)
            
            if stack:
                time_passed = timestamp - current_time
                
                Times_Of_Functions[stack[-1]] += time_passed
            
            if action == "start":
                stack.append(func_id)
                current_time = timestamp
            elif action == "end":
                Times_Of_Functions[stack[-1]] += 1
                current_time = timestamp + 1
                stack.pop()
        return Times_Of_Functions

                  
            
            

# Test Case
Testing = Solution()
print("Test 1: ", Testing.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
# Expected Output: [3,4] 

print("Test 2: ", Testing.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))
# Expected Output: [8]

print("Test 3: ", Testing.exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))
# Expected Output: [7,1]