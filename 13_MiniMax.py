
game_tree = [3, 5, 2, 9, 12, 5, 23, 23]

def minimax(depth, node_index, is_maximizing_player, scores, height):
    if depth == height:
        return scores[node_index]
    
    if is_maximizing_player:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        )

def calculate_tree_height(scores):
    import math
    return math.log2(len(scores))

height = int(calculate_tree_height(game_tree))
optimal_value = minimax(0, 0, True, game_tree, height)
print("The optimal value is:", optimal_value)
