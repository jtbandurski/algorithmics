def compute_high_scores(n, m, k, level, time_limit, stamina):
    # Create a memoization table to store computed scores
    memo = [[None] * n for _ in range(m)]

    # Define a recursive helper function to compute the high score
    def helper(hero, field):
        # Check if the score is already computed for this hero and field
        if memo[hero][field] is not None:
            return memo[hero][field]

        # Base case: If the hero is on the last field
        if field == n - 1:
            if level[field] == 0:
                memo[hero][field] = -1
            else:
                memo[hero][field] = time_limit[hero] - field
            return memo[hero][field]

        # Check if the hero has enough time to reach the last field
        if field + time_limit[hero] >= n:
            max_score = -1
            if level[field] > 0 and stamina[hero] > 0:
                for jump in range(1, min(k + 1, n - field)):
                    if field + jump < n:
                        next_field = field + jump
                        if memo[hero][next_field] is None:
                            memo[hero][next_field] = helper(hero, next_field)
                        if memo[hero][next_field] != -1:
                            max_score = max(max_score, memo[hero][next_field])

            if field + 1 < n:
                next_field = field + 1
                if memo[hero][next_field] is None:
                    memo[hero][next_field] = helper(hero, next_field)
                if memo[hero][next_field] != -1:
                    max_score = max(max_score, memo[hero][next_field])

            # Adjust the maximum score based on the hero's time limit and remaining stamina
            if max_score != -1:
                remaining_time = time_limit[hero] - field - 1
                remaining_stamina = min(stamina[hero], remaining_time)
                memo[hero][field] = max_score + remaining_stamina
            else:
                memo[hero][field] = -1

        else:
            memo[hero][field] = -1

        return memo[hero][field]

    # Compute the high score for each hero starting from the first field
    high_scores = [helper(i, 0) for i in range(m)]
    return high_scores


# input
n = 11
m = 4
k = 4

level =[4, 1, 4, 1, 0, 0, 4, 1, 1, 1, 1]

time_limit = [5, 9, 2, 9]

stamina = [3, 1, 2, 0]

print(compute_high_scores(n, m, k, level, time_limit, stamina))





