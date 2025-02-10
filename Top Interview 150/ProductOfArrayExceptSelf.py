class Solution:
    def productExceptSelf(self, nums):
        product = 1
        zeroCount = 0
        n = len(nums)
        result = [0] * n

        # Step 1: Calculate product of all non-zero elements and count zeros
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                product *= num

        # Step 2: Handle the cases based on zero count
        if zeroCount > 1:
            return result  # More than one zero, all elements will be zero
        if zeroCount == 1:
            # If there's exactly one zero, the product of all other elements is placed in that position
            for i in range(n):
                if nums[i] == 0:
                    result[i] = product
        else:
            # If there are no zeros, divide the total product by each element
            for i in range(n):
                result[i] = product // nums[i]

        return result
