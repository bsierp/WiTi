

class Task:
    def __init__(self, i, p, w, d):
        self.i = i  # nr zadania
        self.p = p  # czas trwania zadania
        self.w = w  # waga zadania
        self.d = d  # pożądany termin zakończenia
        self.is_active = True  # czy zadanie jest sprawdzane w permutacji
