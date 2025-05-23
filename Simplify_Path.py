# Given an absolute path for a file (Unix-style), simplify it. For example, path = "/home/", => "/home" path = "/a/./b/../../c/", => "/c" click to show corner cases. Corner Cases: Did you consider the case where path = "/../"? In this case, you should return "/". Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/". In this case, you should ignore redundant slashes and return "/home/foo".


def simplify_path(path):
    # Time complexity: O(n), where n is the number of directories in the path
    # Space complexity: O(n), where n is the number of directories in the path
    stack = []
    components = path.split('/')
    
    for component in components:
        if component == '' or component == '.':
            continue
        elif component == '..':
            if stack:
                stack.pop()
        else:
            stack.append(component)
    
    simplified_path = '/' + '/'.join(stack)
    return simplified_path

# Test cases
print(simplify_path("/home/"))  # "/home"
print(simplify_path("/a/./b/../../c/"))  # "/c"
print(simplify_path("/../"))  # "/"
print(simplify_path("/home//foo/"))  # "/home/foo"
