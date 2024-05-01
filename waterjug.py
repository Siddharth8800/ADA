def water_jug(jug1_size, jug2_size, target):
    visited = set()
    queue = [((0, 0), "Initial state")]

    while queue:

        state, action = queue.pop(0)

        
        if state not in visited:
            visited.add(state)
            print(f"{action}: Jug 1 = {state[0]}, Jug 2 = {state[1]}")

            if state[0] == target or state[1] == target:
                return True

            queue.append(((jug1_size, state[1]), f"Fill jug 1"))
            queue.append(((0, state[1]), f"Empty jug 1"))
            queue.append(((state[0], jug2_size), f"Fill jug 2"))
            queue.append(((state[0], 0), f"Empty jug 2"))

            amount = min(state[0], jug2_size - state[1])
            queue.append(((state[0] - amount, state[1] + amount), f"Pour {amount} from jug 1 to jug 2"))
            amount = min(state[1], jug1_size - state[0])
            queue.append(((state[0] + amount, state[1] - amount), f"Pour {amount} from jug 2 to jug 1"))

    return False

jug1_size = int(input("Enter the capacity of jug 1: "))
jug2_size = int(input("Enter the capacity of jug 2: "))
target = int(input("Enter the target amount of water: "))


print(water_jug(jug1_size, jug2_size, target))
