"""
Benchmark: merge sort vs. quicksort (two pivot strategies)
=============================================================
Run this AFTER you've implemented all four functions in
sorting_template.py.

    python sorting_benchmark.py

This times all three sorts on RANDOM and ALREADY-SORTED input, at
several sizes, and prints a table. Use this output for Part 3 of the
assignment -- don't just cite Big-O from memory, look at what actually
happens.

A WARNING ABOUT SIZE: quicksort_first_pivot on already-sorted input
recurses once per element. Python's default recursion limit is around
1000, so this benchmark deliberately keeps sizes well under that for
the sorted-input case -- otherwise quicksort_first_pivot will crash
with a RecursionError. If you see that crash, that IS a real result
worth reporting, not a bug in your code.
"""

import random
import time

from sorting_template import merge_sort, quicksort_first_pivot, quicksort_random_pivot


def timed(sort_fn, arr):
    """Run sort_fn on arr, return (elapsed_seconds, crashed)."""
    try:
        start = time.perf_counter()
        sort_fn(arr)
        return time.perf_counter() - start, False
    except RecursionError:
        return None, True


def run_experiment():
    sizes = [200, 400, 600, 800]
    random.seed(42)

    print(f"{'n':>6} {'input':>10} {'merge sort':>12} {'qsort (first)':>15} {'qsort (random)':>16}")
    print("-" * 64)

    for n in sizes:
        datasets = {
            "random": [random.randint(0, 1_000_000) for _ in range(n)],
            "sorted": list(range(n)),
        }
        for label, data in datasets.items():
            merge_time, _ = timed(merge_sort, data)
            first_time, first_crashed = timed(quicksort_first_pivot, data)
            random_time, _ = timed(quicksort_random_pivot, data)

            first_str = "CRASHED" if first_crashed else f"{first_time:.4f}"
            print(f"{n:>6} {label:>10} {merge_time:>12.4f} {first_str:>15} {random_time:>16.4f}")
        print("-" * 64)


if __name__ == "__main__":
    run_experiment()
