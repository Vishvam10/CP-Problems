def pretty_args(args):
    """pretty prints the arguments in a string
    """
    return ", ".join([repr(arg) for arg in args])
def pretty_kwargs(kwargs):
    """pretty prints the keyword arguments in a string
    """
    return ", ".join([
        f"{key}={repr(value)}"
        for key, value in kwargs.items()
    ])
def pretty_func(fn, args, kwargs):
    # Pretty print args in a string
    args_str = pretty_args(args)

    # Pretty print kwargs in a string
    kwargs_str = pretty_args(kwargs)

    # Format the function string and return
    if args_str and kwargs_str:
        return f"{fn.__name__}({args_str, kwargs_str})"
    return f"{fn.__name__}({args_str or kwargs_str})"
# Use as a decorator
def recviz(fn):
    """Decorator that pretty prints the recursion tree with
       args, kwargs, and return values.
    """

    # holds the current recursion level
    recursion_level = 1

    def wrapper(*args, **kwargs):

        # we register a nonlocal recursion_level so that
        # it binds with the recursion_level variable.
        # in this case, it will bind to the one defined
        # in recviz function.
        nonlocal recursion_level

        # Generate the pretty printed function string
        fn_str = pretty_func(fn, args, kwargs)

        # Generate the whitespaces as per the recursion level
        whitespace = "   " * (recursion_level - 1)

        # Pretty print the function with the whitespace
        print(f"{whitespace} -> {fn_str}")

        # increment the recursion level
        recursion_level += 1

        # Invoke the wrapped function and hold the return value
        return_value = fn(*args, **kwargs)

        # Post function evaluation we decrease the recursion
        # level by 1
        recursion_level -= 1

        # Pretty print the return value
        print(f"{whitespace} <- {repr(return_value)}")

        # Return the return value of the wrapped function
        return return_value

    return wrapper

class Solution:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        # @recviz
        def generate(arr, start, n, pref, acc) :
            if(len(pref) == n) :
                acc.append(pref)
                return
            
            for i in range(start, len(arr)) :
                temp = pref + [arr[i]]
                generate(arr, i+1, n, temp, acc)
            
            return acc
        
        ans = [[]]
        for i in range(1, len(arr)+1) :
            ss = generate(arr, 0, i, [], [])
            ans.extend(ss)
        
        return ans
    
# Using bit manipulation

class Solution:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        p = 1 << n      # cardinality of power set : 2**n
        ans = []
        
        for i in range(p) :
            subset = []
            for j in range(n) :
                # If the jth bit of i is set, then include
                if((i >> j) & 1) :
                    subset.append(arr[j])
            ans.append(subset)
        
        return ans
