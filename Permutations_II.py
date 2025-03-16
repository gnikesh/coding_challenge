# Given a collection of numbers that might contain duplicates, return all possible unique permutations. For example, [1,1,2] have the following unique permutations: [ [1,1,2], [1,2,1], [2,1,1] ]


def permuteUnique(nums):
    # Time complexity: O(N*N!/N) or O(N!/N) where N is the length of the input list
    # Space complexity: O(N*N!/N) for the space used by the recursion stack and to store the result
    nums.sort()
    result = []
    visited = [False] * len(nums)

    def backtrack(current_path, visited):
        if len(current_path) == len(nums):
            result.append(current_path[:])
            return
        for i in range(len(nums)):
            if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                continue
            visited[i] = True
            current_path.append(nums[i])
            backtrack(current_path, visited)
            visited[i] = False
            current_path.pop()

    backtrack([], visited)
    return result
