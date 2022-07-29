import string


def get_frequent_id(filename="input.txt"):
    _file = open(filename)
    line = _file.readline().split()
    n, C, D = int(line[0]), line[1], line[2]
    keywords = set()
    for _ in range(n):
        keywords.add(_file.readline().strip())

    code = _file.read()
    valid_symbols = set(string.ascii_letters + string.digits + "_")
    identifiers = ''.join(ch if ch in valid_symbols else ' ' for ch in code)
    if C == "no":
        keywords = set(map(lambda x: x.lower(), keywords))
        identifiers = identifiers.lower().split()
    else:
        identifiers = identifiers.split()

    identifiers = filter(
        lambda x: x not in keywords and not x.isdigit(), identifiers
        )
    if D == "no":
        identifiers = filter(lambda x: not x[0].isdigit(), identifiers)

    identifiers = tuple(identifiers)
    match_dict = dict()

    for identifier in identifiers:
        match_dict[identifier] = match_dict.setdefault(identifier, 0) + 1

    max_match = max(match_dict.values())

    for identifier in identifiers:
        if match_dict[identifier] == max_match:
            return identifier

print(get_frequent_id())
