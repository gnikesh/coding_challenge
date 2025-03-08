# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. Each number in C may only be used once in the combination. Note: All numbers (including target) will be positive integers. The solution set must not contain duplicate combinations. For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, A solution set is: [ [1, 7], [1, 2, 5], [2, 6], [1, 1, 6] ]


def combinationSum2(candidates, target):
    # Time Complexity: O(2^n) in the worst case where n is the number of candidates
    # Space Complexity: O(n) for the recursion stack and O(n) for the output

    def backtrack(start, path, target):
        if target < 0:
            return
        if target == 0:
            result.add(tuple(sorted(path)))
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            backtrack(i + 1, path + [candidates[i]], target - candidates[i])

    candidates.sort()
    result = set()
    backtrack(0, [], target)
    return [list(t) for t in result]

# Example usage
print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
