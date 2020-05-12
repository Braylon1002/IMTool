# 需要点集数据graph.txt，放在本代码同目录下；不需要第三方依赖库
# 使用方法：更改本代码最底部if __name__ == '__main__'里的test_seed_set；
#   未更改的test_seed_set是使用模拟爆发求得的得分Top 5点集，可作为必须超过的baseline以评估你的算法的表现

import random
import sys
import os

# 请勿更改
NUM_MC_ROUNDS = 10000  # （Monte Carlo）模拟爆发的次数，在执行NUM_MC_ROUNDS次模拟后取均值作为可感染点数即得分
NUM_SEEDS = 5  # 限制取Top 5的点集进行评分（因为点数越多肯定能够覆盖的范围越大）
BASELINE_SEED_SET = [3, 18, 13, 30, 6]  # 使用模拟爆发求得的得分Top 5点集
##########


class SeedSetGrader:
    def __init__(self, test_seed_set):
        with open("graph.txt", "r") as file:
            self.graph = [[float(x) for x in line.split()] for line in file]
        self.test_seed_set = test_seed_set
        if len(test_seed_set) > 5:
            print('The number of testing seeds exceeds the limit({0}): {1}'.format(NUM_SEEDS, len(test_seed_set)),
                  file=sys.stderr)
            os._exit(1)

        self.num_vert = len(self.graph)
        self.status = [0 for _ in range(self.num_vert)]  # 0 for inactive, 1 for active
        for test_seed in test_seed_set:
            self.status[test_seed] = 1
        print('Graph with {0} vertices has been loaded.'.format(self.num_vert))
        print('Number of rounds in Monte-Carlo simulation: {0}'.format(NUM_MC_ROUNDS))

    def get_score(self):
        return self.simulate_influence()

    def simulate_influence(self):
        cnt = 0
        for _ in range(NUM_MC_ROUNDS):
            live_set = [seed for seed in self.test_seed_set]
            newly_influenced_set = []
            temp_status = [s for s in self.status]
            cnt += len(self.test_seed_set)
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
    test_seed_set = BASELINE_SEED_SET  # 更改为你的点集

    grader = SeedSetGrader(test_seed_set)
    print('------Test Report------')
    print('Test Seed Set: {0}'.format(test_seed_set))
    print('Please wait...')
    print('Score (avg. #influenced after {0} simulation): {1}'.format(NUM_MC_ROUNDS, grader.get_score()))
