"""Find duplicated, non-overlapping substrings."""


def find_dup_str(s, n):
    """Returns the first duplicated non-overlapping substring of length n."""
    if n <= 0 or 2 * n > len(s):
        return ""

    last_start = len(s) - n

    for first_start in range(last_start + 1):
        candidate = s[first_start:first_start + n]
        second_start_min = first_start + n

        for second_start in range(second_start_min, last_start + 1):
            if s[second_start:second_start + n] == candidate:
                return candidate

    return ""


def find_max_dup(s):
    """Returns the longest duplicated non-overlapping substring in s."""
    max_length = len(s) // 2

    for length in range(max_length, 0, -1):
        duplicate = find_dup_str(s, length)

        if duplicate != "":
            return duplicate

    return ""


def main():
    """Runs the required terminal tests for both functions."""
    s = input("Enter a string for find_dup_str: ")
    n = int(input("Enter substring length n: "))
    print(find_dup_str(s, n))

    s = input("Enter a string for find_max_dup: ")
    print(find_max_dup(s))


if __name__ == "__main__":
    main()