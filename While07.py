def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    evens="02468"
    count = 0
    i=0
    while i < len(s):
        if s[i] in evens:
            count += 1
        i += 1
    return count