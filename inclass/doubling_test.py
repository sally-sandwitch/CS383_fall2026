"""
Bonus Assignment -- Doubling Test
CS 383 Algorithms Analysis and Design

Fill in the TODO sections below with your own code, then run this
script to check your answers:

    python doubling_test.py

Submit this completed .py file on or before PA2 is due. Google classroom will have something. 
Bonus assignment: Submission is optional but if you submit then your points will count towards the assignment category (40% of your grade). 

"""

import math

# ---------------------------------------------------------------------------
# Given: experimental running-time data
# ---------------------------------------------------------------------------
n_values = [1000, 2000, 4000, 8000]
times = [0.5, 1.4, 4.0, 11.3]


# ---------------------------------------------------------------------------
# Part (a): Compute the ratio T(2n) / T(n) between consecutive rows
# ---------------------------------------------------------------------------
def compute_ratios(times):
    """
    Given a list of running times for doubling input sizes, return a
    list of ratios T(2n) / T(n) between each consecutive pair.

    Example:
        compute_ratios([0.5, 1.4, 4.0, 11.3])
        -> [1.4/0.5, 4.0/1.4, 11.3/4.0]
    """
    ratios = []
    # TODO: loop over `times` and append each ratio T(2n) / T(n)
    return ratios


# ---------------------------------------------------------------------------
# Part (b): Estimate the exponent b, assuming T(n) ~ a * n^b
# ---------------------------------------------------------------------------
def estimate_exponent(ratio):
    """
    Given a single ratio T(2n) / T(n), estimate the exponent b using
    b ~ log2(ratio).
    """
    # TODO: return the base-2 logarithm of `ratio`
    pass



# ---------------------------------------------------------------------------
# Driver code -- you shouldn't need to modify anything below this line
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    ratios = compute_ratios(times)
    print("Ratios T(2n) / T(n):", [round(r, 3) for r in ratios])

    exponents = [estimate_exponent(r) for r in ratios]
    print("Estimated exponents b:", [round(b, 3) for b in exponents])

    avg_b = sum(exponents) / len(exponents)
    print(f"Average estimated b: {avg_b:.3f}")

    """
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    # Part (c): Written response — order of growth
    # -----------------------------------------------------------------
    # Look at the `ratios` and `exponents` printed above, then answer
    # the following in 4-6 sentences (edit the `explanation` string
    # below):
    #
    #   1. Are the three ratios T(2n)/T(n) close to each other, or do
    #      they drift as n gets larger? What does that tell you about
    #      the nature of growth of T(n)?
    #
    #   2. Look at your average exponent b. It does not have to be a
    #      whole number. What does its value tell you about how fast
    #      this algorithm's running time grows as n gets large -- for
    #      example, is it closer to linear (b=1), linearithmic-ish,
    #      quadratic (b=2), or somewhere in between? Justify using the
    #      actual value of b you computed, not just a guess.
    # Written response: in your own words. (3-4 sentences)
    # -----------------------------------------------------------------
    explanation = """
    TODO: write your explanation here.
    """
    print("\nExplanation on order of growth:", explanation.strip())
