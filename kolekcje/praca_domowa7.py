import time


def czas_wykonania(dekorowana_funkcja):

    def wrapper(*args,**kwargs):
        start = time.time()
        dekorowana_funkcja(*args,**kwargs)
        stop = time.time()
        print(f"Czas wykonania funkcji {dekorowana_funkcja.___name___} z argumentami {args}, {kwargs} wynosi {stop-start} s")
    return wrapper

liczba_doskonala
