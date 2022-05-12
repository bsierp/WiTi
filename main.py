from classes.Machine import *
import timeit
import tracemalloc


filename = "dane2.txt"


def pd():
    m = Machine(filename)
    print("Liczba zadań:", m.task_num)
    start = timeit.default_timer()
    print("Minimalna suma, programowanie dynamiczne:", m.calculate_states())
    end = timeit.default_timer()
    print("Czas:", str(end - start).replace('.', ','))


def bf():
    m = Machine(filename)
    start = timeit.default_timer()
    print("Minimalna suma, przegląd zupełny:", m.permutation_penalty())
    end = timeit.default_timer()
    print("Czas:", str(end - start).replace('.', ','))


if __name__ == "__main__":
    tracemalloc.start()
    pd()
    print("Zużyta pamięć:", tracemalloc.get_traced_memory()[1], "Bajtów")
    tracemalloc.stop()
    tracemalloc.start()
    bf()
    print("Zużyta pamięć:", tracemalloc.get_traced_memory()[1], "Bajtów")
    tracemalloc.stop()
