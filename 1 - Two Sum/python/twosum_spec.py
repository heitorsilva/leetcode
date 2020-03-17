from mamba import description, context, it
from expects import expect, equal

from twosum import Solution

with description('Two Sum') as self:
    with description('when two numbers in a list sums to a target'):
        with it('should return the indices of these two numbers'):
            numbers = [2,7,11,15]
            target = 9

            solution = Solution()

            expect(solution.twoSum(numbers, target)).to(equal([0, 1]))
