class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        container: list = []
        for number in tokens:
            try:
                container.append(int(number))
            except ValueError:
                first_pop = container.pop()
                second_pop = container.pop()
                
                if number == "+":
                    container.append(int(second_pop + first_pop))
                
                elif number == "-":
                    container.append(int(second_pop - first_pop))
                    
                elif number == "*":
                    container.append(int(second_pop * first_pop))
                    
                elif number == "/":
                    container.append(int(second_pop / first_pop))
            
        return container[0]



# Test Case
Testing = Solution()
print("Test 1: ", Testing.evalRPN(["2","1","+","3","*"]))
# Expected Output: 9 

print("Test 2: ", Testing.evalRPN(["4","13","5","/","+"]))
# Expected Output: 6

print("Test 3: ", Testing.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# Expected Output: 22