from kaggle_environments.envs.hungry_geese.hungry_geese import Observation, adjacent_positions, min_distance, row_col
import np


class SpaceValues(Enum):
    HEAD = 0
    TAIL = -0.8
    BODY = -0.5
    EMPTY = 0.4


class ObservationPreprocessor:

    def __init__(self, configuration):
        self.rows = configuration.rows
        self.cols = configuration.cols
        self.hunger_rate = configuration.hunger_rate
        self.min_food = configuration.min_food
        self.last_min_distance_to_food = self.rows * self.cols
    
    def get_observation(self, obs):
        gym_observation = Observation(obs)
        custom_observation = self._init_empty_observation()
        agent_head, agent_body, agent_tail = self._get_agent(obs)
        other_geese = self._get_other_geese(obs)
        print(obs)

    def _get_agent(self, obs):
        agent_idx = obs.index
        agent = obs.geese[agent_idx]
        agent_head = None
        agent_tail = None
        agent_body = []
        if goose.length > 0:
            agent_head = row_col(agent[0], this.cols)
        if goose.length > 1:
            agent_tail = row_col(agent[-1], this.cols)
        if goose.length > 2:
            agent_body = [row_col(agent_body_part) for agent_body_part in agent[1: agent.length - 1]]
        
        return agent_head, agent_body, agent_tail
    
    def _get_other_geese(self, obs):
        other_geese = []
        for goose_idx in range(obs.geese.length):
            if(goose_idx != obs.index):
                other_geese.extend([row_col(pos) for pos in other_geese])
        
        return other_geese

    def _init_empty_observation():
        new_observation = []
        for col in range(self.cols):
            for row in range(self.rows):
                new_observation[col][row] = SpaceValues.EMPTY

    def get_rewards(self):
        pass
