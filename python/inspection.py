import inspect

def print_local_variables():
    frame = inspect.currentframe()
    print("\nfunction:\t", frame.f_back.f_code.co_name)
    for key in frame.f_back.f_code.co_varnames:
        print("{:<20}{:<5}{:<30}".format(key,":", str(frame.f_back.f_locals.get(key))))