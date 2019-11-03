import torch


class BaseAgent:

    def __init__(self):
        self.env = None
        self.device = None
        self.shared_memory = None
        self.shared_weights = dict()
        self.memory = None

    def run(self):
        raise Exception('You need to implement run method.')

    def act(self, state):
        raise Exception('You need to implement act method.')

    def explore(self, state):
        raise Exception('You need to implement explore method.')

    def exploit(self, state):
        raise Exception('You need to implement explore method.')

    def interval(self):
        raise Exception('You need to implement interval method.')

    def calc_current_q(self, states, actions, rewards, next_states, dones):
        raise Exception('You need to implement calc_current_q method.')

    def calc_target_q(self, states, actions, rewards, next_states, dones):
        raise Exception('You need to implement calc_current_q method.')

    def load_weights(self):
        raise Exception('You need to implement load_weights method.')

    def save_weights(self):
        raise Exception('You need to implement save_weights method.')

    def load_memory(self):
        while not self.shared_memory.empty():
            batch = self.shared_memory.get()
            self.memory.load_memory(batch)

    def save_memory(self):
        self.shared_memory.put(self.memory.get())
        self.memory.reset()