def short_number(n) -> str:
    """
    Reduce a significant number by utilizing the SI prefixes (k, M, B, T).

    :param n: the number to shorten
    :return: the shortened number in String literal
    """
    if n < 1000:
        return str(n)
    prefixes = {3: 'k', 6: 'M', 9: 'B', 12: 'T'}
    for i in prefixes:
        if n < 10 ** (i + 3):
            return f"{n / 10 ** i:.1f}{prefixes[i]}"
    return str(n)
