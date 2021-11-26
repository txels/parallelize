import os
from collections.abc import Iterable
from concurrent import futures
from functools import wraps
from typing import Any

WORKERS = int(os.getenv("FRESHNESS_WORKERS", 5))


def listify(mapping: dict[Any, int]):
    results = sorted((index, val) for index, val in mapping.items())
    indices, values = zip(*results)
    # size = max(index for index, _ in results)
    return values


def parallelize(fn):

    @wraps(fn)
    def wrapper(*args):
        # figure out if this is a direct call or not... not 100% reliable,
        # should use `inspect` methods instead?
        parallel = len(args) == 1 and isinstance(args[0], Iterable)
        if parallel:
            args_list = args[0]
        else:
            return fn(*args)

        results = {}

        with futures.ThreadPoolExecutor(max_workers=WORKERS) as executor:
            mapping = {
                executor.submit(fn, *args): index
                for index, args in enumerate(args_list)
            }

            for future in futures.as_completed(mapping):
                index = mapping[future]
                try:
                    data = future.result()
                except Exception as exc:
                    results[index] = exc
                else:
                    results[index] = data

        return listify(results)
    return wrapper
