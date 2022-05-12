from classes.Task import Task
import itertools


def boolList2BinString(lst):
    return ''.join(['1' if x else '0' for x in lst])


class Machine:
    def __init__(self, filename):
        f = open(filename, "r")
        self.task_num = int(f.readline())
        self.current_time = 0
        self.task_array = []
        i = 0
        for line in f:
            i += 1
            r_p = [int(s) for s in line.split() if s.isdigit()]
            self.task_array.append(Task(i, r_p[0], r_p[1], r_p[2]))
        f.close()

    def active_tasks_duration(self):
        c = 0
        for task in self.task_array:
            if task.is_active:
                c += task.p
        return c

    def task_penalty(self, task):
        if task.d < self.active_tasks_duration():
            return task.w * (self.active_tasks_duration() - task.d)
        else:
            return 0

    def permutation_penalty(self):
        if not [task for task in self.task_array if task.is_active]:
            return 0
        else:
            penalties = []
            for task in self.task_array:
                if task.is_active:
                    k = self.task_penalty(task)
                    task.is_active = False
                    penalties.append(self.permutation_penalty() + k)
                    task.is_active = True
            return min(penalties)

    # DO NOT USE / IT WILL EAT ALL YOUR MEMORY
    def calculate_states(self):
        states = [{}, {}]
        for task in self.task_array:
            task.is_active = False
        for task in self.task_array:
            task.is_active = True
            states[0][int(boolList2BinString([t.is_active for t in self.task_array]), 2)] = self.task_penalty(task)
            task.is_active = False
        for k in range(2, self.task_num + 1):
            states[(k + 1) % 2] = {}
            result_list = list(map(dict, itertools.combinations(states[k % 2].items(), k)))
            for i in result_list:
                key = 0
                for elem in i:
                    key |= elem
                if k == sum(list(map(bool, [int(x) for x in bin(key)[2:]]))):
                    b_list = list(map(bool, [int(x) for x in bin(key)[2:]]))
                    while len(b_list) < self.task_num:
                        b_list.insert(0, False)
                    for j in range(self.task_num):
                        self.task_array[j].is_active = b_list[j]
                    penalties = []
                    for task in self.task_array:
                        if task.is_active:
                            k_p = self.task_penalty(task)
                            task.is_active = False
                            dict_key = int(boolList2BinString([t.is_active for t in self.task_array]), 2)
                            penalties.append(
                                states[k % 2][dict_key] + k_p)
                            task.is_active = True
                    states[(k+1) % 2][key] = min(penalties)
        return list(states[1].values())[0] if len(states[1]) < len(states[0]) else list(states[0].values())[0]
