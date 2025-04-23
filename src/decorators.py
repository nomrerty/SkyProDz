def log(filename=""):
    """Этот декоратор автоматически логирует начало и конец выполнения функции,
     а также ее результаты или возникшие ошибки.
    Декоратор принимает необязательный аргумент "filename",
    который определяет, куда будут записываться логи (в файл или в консоль)."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as error:
                if filename == "":
                    return f"{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}"
                else:
                    file = open(filename, "w")
                    file.write(f"{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}")
                    file.close()
            else:
                if filename == "":
                    return f"{func.__name__} {result}"
                else:
                    file = open(filename, "w")
                    file.write(f"{func.__name__} {result}")
                    file.close()
            return ""

        return wrapper

    return decorator
