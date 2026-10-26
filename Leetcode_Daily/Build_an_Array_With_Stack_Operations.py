class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        Container: list = []
        TurnToSet: set = set(target)
        for box in range(1, n + 1):
            if box in TurnToSet:
                Container.append("Push")
            else:
                Container.append("Push")
                Container.append("Pop")
            if box == target[-1]:
                break

        return Container


        
#TestCase

testing = Solution()

print("test1: ", testing.buildArray([1,3], 3)) #["Push","Push","Pop","Push"]
print("test2: ", testing.buildArray([1,2,3], 3))#["Push","Push","Push"]
print("test3: ", testing.buildArray([1,2], 4))#["Push","Push"]