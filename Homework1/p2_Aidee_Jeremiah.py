"""Find Pythagorean triples up to a user-supplied limit."""


def find_Pythagorean(n):  # pylint: disable=invalid-name
    """Returns all unique Pythagorean triples with values from 1 through n."""
    triples = []

    for a in range(1, n + 1):
        for b in range(a, n + 1):
            for c in range(b, n + 1):
                if a**2 + b**2 == c**2:
                    triples.append((a, b, c))

    return triples


def main():
    """Reads n and displays all Pythagorean triples up to n."""
    n = int(input("Enter a positive integer n: "))
    triples = find_Pythagorean(n)

    for triple in triples:
        print(triple)


if __name__ == "__main__":
    main()