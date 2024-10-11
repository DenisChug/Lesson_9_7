

def is_prime(func):
    def wrapper(*args):
        if func(*args) % 2:
            print(f'Простое')
        else:
            print(f'Составное')
        return func(*args)
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
