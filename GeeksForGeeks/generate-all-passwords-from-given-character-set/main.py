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


def fn(arr, n):
    ans = []
    '''
    [a, b] => a, b, aa, ab, ba, bb
    '''
    # IN AN INCREMENTAL FASHION
    # def helper(arr, n, msize, pre, ans) :
    #     print('pre, ans : ', pre, ans)
    #     if(n == msize) :
    #         return

    #     for ele in arr :
    #         temp = pre + ele
    #         ans.append(temp)
    #         helper(arr, n+1, msize, temp, ans)

    #     return ans

    # return helper(arr, 0, n, "", [])

    # IN A DECREMENTAL FASHION

    # @recviz
    def generate(arr, level, pre, acc):
        if (level == 0):
            return

        for ele in arr:
            temp = pre + ele
            acc.append(temp)
            generate(arr, level-1, temp, acc)

        return acc

    # Generate for all sizes
    for i in range(1, n+1):
        temp = generate(arr, i, "", [])
        ans.append(temp)

    return ans


arr = ['a', 'b', 'c']
print('ans : ', fn(arr, len(arr)))
