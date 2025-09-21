class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def prime_factors(n: int) -> set:
            factors = set()
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factors.add(d)
                    n //= d
                d += 1
            if n > 1:
                factors.add(n)
            return factors

        primes = set()
        for num in nums:
            primes |= prime_factors(num)   

        return len(primes)