def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    odds="13579"
    count = 0
    i=0
    while i < len(s):
        if s[i] in odds:
            count += 1
        i += 1
    return count