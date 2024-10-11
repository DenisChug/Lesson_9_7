def is_prime(func):
    def wrapper(*args, **kwargs):
        for i in range(2, int(func(*args, **kwargs) ** 0.5) + 1):
            if func(*args, **kwargs) % i == 0:
                print("Составное")
                break
            else:
                print('Простое')
            return func(*args, **kwargs)
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
