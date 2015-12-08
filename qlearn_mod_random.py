import random


class QLearn:
    def __init__(self, actions, epsilon=0.3, alpha=0.8, gamma=0.9):
        self.q = {}
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.actions = actions

    def getQ(self, state, action):
        return self.q.get((state, action), 0.0) # q.get(key,default=0)

    def chooseAction(self, state, return_q=False):
        q = [self.getQ(state, a) for a in self.actions]
        maxQ = max(q)

        if random.random() < self.epsilon:
            #action = random.choice(self.actions)
            minQ = min(q); mag = max(abs(minQ), abs(maxQ))
            q = [q[i] + random.random() * mag - .5 * mag for i in range(len(self.actions))] # add random values to all the actions, recalculate maxQ
            maxQ = max(q)

        count = q.count(maxQ)
        if count > 1:
            best = [i for i in range(len(self.actions)) if q[i] == maxQ]
            i = random.choice(best)
        else:
            i = q.index(maxQ)

        action = self.actions[i]

        if return_q:
            return action, q
        return action

    def learn(self, state1, action1, reward, state2):
        maxqnew = max([self.getQ(state2, a) for a in self.actions])

        oldv = self.q.get((state1, action1), None)
        if oldv is None:
            self.q[(state1, action1)] = reward
        else:
            self.q[(state1, action1)] = oldv + self.alpha * (reward + self.gamma*maxqnew - oldv)

    def printQTable(self):
        print self.q
