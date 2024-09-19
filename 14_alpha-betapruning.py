
game_tree = [3, 5, 6, 9, 1, 2, 0, -1]

def alpha_beta_pruning(depth, node_index, is_maximizing_player, scores, alpha, beta):
    if depth == 3:  
        return scores[node_index]
    
    if is_maximizing_player:
        best = float('-inf')
        for i in range(2):  
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, scores, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            
            if beta <= alpha:
                break  
        return best
    else:
        best = float('inf')
        for i in range(2): 
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, scores, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            
            if beta <= alpha:
                break 
        return best

alpha = float('-inf')
beta = float('inf')
optimal_value = alpha_beta_pruning(0, 0, True, game_tree, alpha, beta)
print("The optimal value is:", optimal_value)
