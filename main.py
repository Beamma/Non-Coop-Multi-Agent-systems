def max_value(tree):
    if type(tree) == int:
        return tree
    

    results = []
    for i in range(len(tree)):
        results.append(min_value(tree[i]))
    
    return max(results)


def min_value(tree):
    if type(tree) == int:
        return tree
    
    results = []
    for i in range(len(tree)):
        results.append(max_value(tree[i]))
    return min(results)


def max_action_value(game_tree):
    if type(game_tree) == int:
        return [None, game_tree]
    

    result = []
    for i in range(len(game_tree)):
        result.append((min_value(game_tree[i]), i))

    value, index = max(result)

    return (index, value)

def min_action_value(game_tree):
    if type(game_tree) == int:
        return [None, game_tree]
    

    result = []
    for i in range(len(game_tree)):
        result.append((max_value(game_tree[i]), i))

    value, index = min(result)

    return (index, value)
