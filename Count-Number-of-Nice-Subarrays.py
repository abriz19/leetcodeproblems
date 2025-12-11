class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = 0                    # Running count of odd numbers
        count = {0: 1}                # prefix sum frequency map
        result = 0
        
        for num in nums:
            if num % 2 == 1:          # It's odd
                prefix += 1
            
            # Count how many previous prefix sums make: prefix - prev = k
            if prefix - k in count:
                result += count[prefix - k]
            
            # Store current prefix sum
            count[prefix] = count.get(prefix, 0) + 1
        
        return result
