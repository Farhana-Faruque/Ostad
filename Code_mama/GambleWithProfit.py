def gamble_with_profit(F, N, M):
    return "true" if F * N > M else "false"

inputs = input().split()
F = float(inputs[0])
N = int(inputs[1])
M = int(inputs[2])

print(gamble_with_profit(F, N, M))
