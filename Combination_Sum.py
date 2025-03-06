# Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. The same repeated number may be chosen from C unlimited number of times. Note: All numbers (including target) will be positive integers. The solution set must not contain duplicate combinations. For example, given candidate set [2, 3, 6, 7] and target 7, A solution set is: [ [7], [2, 2, 3] ]


def combinationSum(candidates, target):
    # Time Complexity: O(N^(T/M + 1)) where N is the size of the candidates list and M is the minimum number in the list
    # Space Complexity: O(T/M + 1)
    def backtrack(remain, comb, start):
        if remain == 0:
            result.append(list(comb))
            return
        elif remain < 0:
            return
        for i in range(start, len(candidates)):
            comb.append(candidates[i])
            backtrack(remain - candidates[i], comb, i)
            comb.pop()

    result = []
    backtrack(target, [], 0)
    return result

# Example:
candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))  # Output: [[7], [2, 2, 3]]
