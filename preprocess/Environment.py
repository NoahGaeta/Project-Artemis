from kaggle_environments.envs.hungry_geese.hungry_geese import Action
from kaggle_environments import make
import gym
import numpy as np
from preprocess.ObservationPreprocessor import ObservationPreprocessor


class Environment(gym.Env):

    def __init__(self, opponent=['greedy','greedy','greedy'], action_offset=1, debug=False):
        super(Environment, self).__init__()
        self.num_envs = 1
        self.debug = debug
        self.actions = [action for action in Action]
        self.action_offset = action_offset
        self.env = make("hungry_geese", debug = self.debug)
        self.config = self.env.configuration
        self.action_space = gym.spaces.Discrete(len(self.actions))
        self.observation_space = gym.spaces.Box(low=-1, high=1, shape=(self.config.rows, self.config.columns), dtype=np.int8)
        self.step_num = 1
        self.observation_preprocessor = ObservationPreprocessor(self.config)
        self.trainer = self.env.train([None, *opponent])

    def step(self, action):
        action += self.action_offset
        action = Action(action)

        obs, reward, done, _ = self.trainer.step(action.name)
        self.observation = self.observation_preprocessor.get_custom_observation(obs)

        info = {}

        self.step_num += 1
        return self.observation, reward, done, info

    def reset(self):
        self.observation_preprocessor = ObservationPreprocessor(self.config)
        obs = self.trainer.reset()
        self.observation = self.observation_preprocessor.get_custom_observation(obs)
        print(self.observation_space)
        print(self.observation.shape)

        return self.observation

    def render(self, **kwargs):
        self.env.render(**kwargs)

    
