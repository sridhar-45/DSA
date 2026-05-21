class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        '''
        # Convert integers to strings
        str_arr1 = sorted([str(val) for val in arr1])
        str_arr2 = sorted([str(val) for val in arr2])

        max_length = 0  # Track the maximum length of the common prefix

        # Use two pointers to traverse the sorted arrays and compare adjacent elements
        i, j = 0, 0
        while i < len(str_arr1) and j < len(str_arr2):
            str1, str2 = str_arr1[i], str_arr2[j]
            common_prefix = 0

            # Compare characters until they differ or we reach the end of one of the strings
            for k in range(min(len(str1), len(str2))):
                if str1[k] == str2[k]:
                    common_prefix += 1
                else:
                    break

            # Update max_length with the longest common prefix found
            max_length = max(max_length, common_prefix)

            # Move to the next pair of numbers in the sorted arrays
            if str1 < str2:
                i += 1
            else:
                j += 1

        return max_length
        '''


        if len(arr1) > len(arr2):
            arr1 , arr2 = arr2 , arr1



        prefix_set = set()

        for n in arr1:
            while n and n not in prefix_set:
                prefix_set.add(n)
                n = n //10

        res = 0

        for n in arr2:
            while n and n not in prefix_set:
                n = n//10
            if n:
                res = max(res,len(str(n)))

        return res                        