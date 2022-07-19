from time import time
from typing import Callable, Any


def timeit(function: Callable) -> Callable:
    """Decorator to time a function

    Args:
        function (Callable): The function to execute and monitor

    Returns:
        Any: The result of `function` call
    """

    def timed(*args, **kwargs) -> Any:
        time_start = time()
        function_result = function(*args, **kwargs)
        time_end = time()

        print("Done in %2.2f sec" % (time_end - time_start))
        return function_result

    return timed
