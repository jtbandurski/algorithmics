from collections import deque

def calculate_high_scores(n, m, level, start, target, time_limit):
    high_scores = []
    
    for h in range(m):
        visited = set()
        score = time_limit[h]
        current_field = start[h]
        
        queue = deque([(current_field, score)])
        
        while queue:
            current_field, score = queue.popleft()
            
            if current_field == target[h]:
                break
            
            if current_field in visited:
                continue
            
            visited.add(current_field)
            
            if level[current_field] > 0:
                next_field = min(current_field + 1, n - 1)
                queue.append((next_field, score - 1))
            
            if level[current_field] < 0:
                next_field = max(current_field - 1, 0)
                queue.append((next_field, score - 1))
            
            jump_field = current_field + level[current_field]
            if 0 <= jump_field < n:
                queue.append((jump_field, score - 1))
        
        high_scores.append(score)
    
    return high_scores
