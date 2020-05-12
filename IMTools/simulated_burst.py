import random
from time import time


NUM_MC_ROUNDS = 100  # 可修改


class SimuGreedy:
    def __init__(self):
        with open("graph.txt", "r") as file:
            self.graph = [[float(x) for x in line.split()] for line in file]
        self.num_vert = len(self.graph)
        self.status = [0 for _ in range(self.num_vert)]
        self.seed_set = []
        print('Graph with {0} vertices has been loaded.'.format(self.num_vert))
        print('Number of rounds in single Monte Carlo simulation: {0}'.format(NUM_MC_ROUNDS))

    def get_seed_set(self):
        tic = time()
        while True:
            max_val = max_id = 0
            for idx, state in enumerate(self.status):
                if state == 0:
                    # print('evaluating V{0}'.format(idx))
                    val = self.simulate_influence(idx)
                    # print('V{0}: {0}'.format(idx, val))
                    if val > max_val:
                        max_val = val
                        max_id = idx
            self.seed_set.append(max_id)
            self.status[max_id] = 1

            # if max_val >= self.num_vert:
            if len(self.seed_set) == 5:
                break
            else:
                print('Current expected #influenced: {0}, {1}-element seed set: {2}'.format(
                    max_val, len(self.seed_set), self.seed_set
                ))
        return self.seed_set, time() - tic

    def simulate_influence(self, vert_id):
        test_seed_set = [seed for seed in self.seed_set]
        test_seed_set.append(vert_id)

        cnt = 0
        for _ in range(NUM_MC_ROUNDS):
            live_set = [seed for seed in test_seed_set]
            newly_influenced_set = []
            temp_status = [s for s in self.status]
            temp_status[vert_id] = 1
            cnt += len(test_seed_set)
            while True:
                for idx, state in enumerate(temp_status):
                    if state == 0:
                        prob_not_influenced = 1.
                        for live in live_set:
                            prob_not_influenced *= 1 - self.graph[live][idx]
                        prob_influenced = 1 - prob_not_influenced
                        if prob_influenced >= self.get_rand():
                            temp_status[idx] = 1
                            newly_influenced_set.append(idx)
                if len(newly_influenced_set) == 0:
                    break
                cnt += len(newly_influenced_set)
                live_set = [inf for inf in newly_influenced_set]
                newly_influenced_set = []
        return cnt / NUM_MC_ROUNDS

    @staticmethod
    def get_rand():
        return random.uniform(0, 1)

if __name__ == '__main__':
    seed_set, time_cost = SimuGreedy().get_seed_set()

    print('--------------')
    print('Time cost: {0} s'.format(time_cost))
    print('Final indexes of vertices in {0}-element seed set:'.format(len(seed_set)))
    print(seed_set)
