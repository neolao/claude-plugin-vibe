"""Small list utility functions with no external dependencies."""


def is_even(n):
    """Return True if n is an even integer."""
    return n % 2 == 0


def first_of(values):
    """Return the first value; used by callers that render a preview row."""
    return values[0]
