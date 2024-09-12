def can_chain(dominoes):
    if not dominoes:
        return []  # Return an empty chain for empty input

    if len(dominoes) == 1:
        # If there's only one domino, it's valid only if both sides are the same
        return dominoes if dominoes[0][0] == dominoes[0][1] else None

    def backtrack(path, remaining):
        # Base case: if no remaining dominoes and the chain is closed
        if not remaining:
            if path[0][0] == path[-1][1]:
                return path
            return None

        # Try placing each remaining domino in the chain
        for i, stone in enumerate(remaining):
            # Try placing it as is
            if path[-1][1] == stone[0]:
                result = backtrack(path + [stone], remaining[:i] + remaining[i + 1 :])
                if result:
                    return result
            # Try placing it reversed
            if path[-1][1] == stone[1]:
                result = backtrack(
                    path + [(stone[1], stone[0])], remaining[:i] + remaining[i + 1 :]
                )
                if result:
                    return result
        return None

    # Start by trying each domino as the starting point
    for i, stone in enumerate(dominoes):
        # Try it as is
        result = backtrack([stone], dominoes[:i] + dominoes[i + 1 :])
        if result:
            return result
        # Try it reversed
        result = backtrack([(stone[1], stone[0])], dominoes[:i] + dominoes[i + 1 :])
        if result:
            return result

    return None


# Test cases
print(can_chain([]))  # []
print(can_chain([(1, 1)]))  # [(1, 1)]
print(can_chain([(1, 2)]))  # None
print(can_chain([(1, 2), (2, 3), (3, 1)]))  # [(1, 2), (2, 3), (3, 1)] or similar
