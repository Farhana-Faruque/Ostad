def count_toy_cars(wheels, bodies, figures):
    return min(wheels // 4, bodies // 1, figures // 2) 


wheels, bodies, figures = map(int, input().split())
print(count_toy_cars(wheels, bodies, figures))
