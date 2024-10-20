def greet():
    print("hello")


def welcome(func):
    print("Welcome!")
    func()


welcome(greet)


def decorator_with_args(greeting):

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{greeting}Before the function.")
            result = func(*args, **kwargs)
            print("f'{greeting}After the function.")
            return result

        return wrapper

    return decorator


@decorator_with_args("Hi")
def greet(name=None):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello!")


greet()
greet("Gordon")


class Repeat:
    def times(self, n):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for i in range(n):
                    result = func(*args, **kwargs)
                return result

            return wrapper

        return decorator


repeat = Repeat()


@repeat.times(3)
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Gordon")
