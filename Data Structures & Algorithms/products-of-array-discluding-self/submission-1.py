class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        out = [1] * n

        # Prefix products: out[i] = product of nums[0..i-1]
        prefix = 1
        for i in range(n):
            out[i] = prefix
            prefix *= nums[i]

        # Suffix products: multiply in product of nums[i+1..n-1]
        suffix = 1
        for i in range(n - 1, -1, -1):
            out[i] *= suffix
            suffix *= nums[i]

        return out