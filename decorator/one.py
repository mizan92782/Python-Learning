def argumentInfo(func):

    def wrapper(*args, **kwargs):
        print("Arguments in this function:")
        for arg in args:
            print(arg)

        print("Kwargs in this function:")
        for key, value in kwargs.items():
            print(f"{key} = {value}")

        return func(*args, **kwargs)

    return wrapper


@argumentInfo
def add(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


res = add(4, 5,c=6)
print("sum : ",res)