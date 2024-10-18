def is_prime(func):
    def wrapper(*args, **kwargs):
        prov = 0
        if func(*args, **kwargs) !=0:
            for div in range(1, func(*args, **kwargs)):
                if func(*args, **kwargs) % div == 0 and func(*args, **kwargs) != div:
                    prov += 1
                    if prov > 1:
                        print(f'Составное')
                        break
            if prov < 2:
                print(f'Простое')
        return func(*args, **kwargs)
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)
