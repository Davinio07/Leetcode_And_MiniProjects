import os

Leetcode_Name: str = input("Whats the Leetcode Name?")
Leetcode_Name = Leetcode_Name.replace(" ", "_")
filename: str = f'{Leetcode_Name}.py'

targetFolder: str = r'/home/cruzd/School/Python/Leetcode_Daily'
folder_Plus_File = os.path.join(targetFolder, filename)

with open(folder_Plus_File, "w") as file:
    file.write('\n\n\n\n# Test Case\nTesting = Solution()\nprint("Test 1: ", ... )\n# Expected Output: ... \n\nprint("Test 2: ", ... )\n# Expected Output: ...\n\nprint("Test 3: ", ... )\n# Expected Output: ...')
    
print(f'Successfully created {filename}!')

os.system(f'code {folder_Plus_File}')
