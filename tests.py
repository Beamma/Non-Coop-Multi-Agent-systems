from main import max_value, min_value, max_action_value, min_action_value


def test1():
    game_tree = 3

    print("Root utility for minimiser:", min_value(game_tree))
    print("Root utility for maximiser:", max_value(game_tree))

    game_tree = [1, 2, 3]

    print("Root utility for minimiser:", min_value(game_tree))
    print("Root utility for maximiser:", max_value(game_tree))

    game_tree = [1, 2, [3]]

    print(min_value(game_tree))
    print(max_value(game_tree))

    game_tree = [[1, 2], [3]]

    print(min_value(game_tree))
    print(max_value(game_tree))

    game_tree = [[2, 3, 4], [1, 100, -100]]

    print(min_value(game_tree))
    print(max_value(game_tree))

def test2():

    game_tree = [2, [-3, 1], 4, 1]

    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)

    game_tree = 3

    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)

    game_tree = [1, 2, [3]]

    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)


def main():
    # test1()
    test2()

main()