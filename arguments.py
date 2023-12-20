def print_args_and_kwargs(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)


print_args_and_kwargs(1, 2, 3)
print_args_and_kwargs(a=10, b=20, c=30)
print_args_and_kwargs(4, 5, 6, x=40, y=50, z=60)
