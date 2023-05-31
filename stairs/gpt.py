def compute_output(n, position, operation):
    heights = [0] * len(position)  # Initialize heights list with zeros
    output = []

    def is_step(pos):
        return pos >= 0 and pos < len(heights) and heights[pos] > 0

    def find_same_height_step(pos, direction):
        step_height = heights[pos]
        while True:
            pos += direction
            if not is_step(pos):
                return False
            if heights[pos] == step_height:
                return True

    def remove_blocks(pos):
        if heights[pos] > 0:
            heights[pos] = 0
            return 1
        return 0

    def walk_to_left(pos):
        steps = 0
        while pos >= 0 and heights[pos] > 0:
            pos -= 1
            steps += 1
        return steps

    for i in range(n):
        pos = position[i]
        op = operation[i]

        if op >= 1:
            if not is_step(pos + 1) and find_same_height_step(pos, 1):
                heights[pos] = op
                output.append(heights[pos])
            else:
                output.append(0)
        elif op == 0:
            output.append(remove_blocks(pos))
        elif op == -1:
            if is_step(pos) and find_same_height_step(pos, -1):
                output.append(1)
            else:
                output.append(0)
        elif op == -2:
            output.append(walk_to_left(pos))

    return output


# Example 1
n = 12
n = 12 
position  = [1, 5, 2, 6, 2, 3, 0, 2, 3, 2, 4, 7] 
operation = [2, 2, 1, 3, 4, 5, 1, 1, 1, 1, 1, 3]
output = compute_output(n, position, operation)
print(output)
# Output: [2, 2, 0, 3, 4, 5, 0, 0, 6, 0, 0, 0]

# Example 2
n = 35 
position  = [1, 5, 2, 6, 2, 3, 0, 2, 3, 2, 4, 7,  3, 6,  3, 3,  6,  6,  3,  2,  1, 1, 2, 3, 2,  3,  3, 1, 2,  2,  2, 0, 0, 8,  2]
operation = [2, 2, 1, 3, 4, 5, 1, 1, 1, 1, 1, 3, -1, 3, -1, 1, -1, -2, -2, -2, -2, 0, 0, 0, 0, -1, -2, 0, 1, -2, -1, 0, 1, 1, -1]
output = compute_output(n, position, operation)
print(output)
# Output: [2, 2, 0,

# Example 3
# n = 200 
# position  = [-50, -50, -49, -49, ..., 48, 48,  49, 49]
# operation = [  1, -2 ,   2,  -2, ..., 99, -2, 100, -2]
# output = compute_output(n, position, operation)
# print(output)
# Output: [2, 2, 0,
