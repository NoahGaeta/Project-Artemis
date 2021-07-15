from kaggle_environments.envs.hungry_geese.hungry_geese import Observation, adjacent_positions, min_distance, row_col
import numpy as np
from enum import Enum


class SpaceValues(Enum):
    HEAD = 0
    TAIL = -0.8
    BODY = -0.5
    EMPTY = 0.4
    FOOD = 1
    OTHER_GOOSE = -1


class ObservationPreprocessor:

    def __init__(self, configuration):
        self.rows = configuration.rows
        self.cols = configuration.columns
        self.hunger_rate = configuration.hunger_rate
        self.min_food = configuration.min_food
        self.last_min_distance_to_food = self.rows * self.cols
    
    def get_custom_observation(self, obs):
        """ Gets custom observation from hungry geese observation """
        gym_observation = Observation(obs)
        custom_observation = self._init_empty_observation()
        agent_head, agent_body, agent_tail = self._get_agent(obs)
        other_geese = self._get_other_geese(obs)
        food = self._get_food(obs)
        if agent_head:
            custom_observation[agent_head['row']][agent_head['col']] = SpaceValues.HEAD.value
        for food_item in food:
            custom_observation[food_item['row']][food_item['col']] = SpaceValues.FOOD.value
        for other_goose_part in other_geese:
            custom_observation[other_goose_part['row']][other_goose_part['col']] = SpaceValues.OTHER_GOOSE.value
        if len(agent_body):
            for body_part in agent_body:
                custom_observation[body_part['row']][body_part['col']] = SpaceValues.BODY.value
        if agent_tail:
            custom_observation[agent_tail['row']][agent_tail['col']] = SpaceValues.TAIL.value
        return np.array(custom_observation, np.float16)

    def _get_agent(self, obs):
        """ Gets the current agent head, body, tail position from a observation """
        agent_idx = obs.index
        agent = obs.geese[agent_idx]
        agent_head = None
        agent_tail = None
        agent_body = []
        if len(agent) > 0:
            agent_head_row, agent_head_col = row_col(agent[0], self.cols)
            agent_head = { 'row': agent_head_row, 'col': agent_head_col }
        if len(agent) > 1:
            agent_tail_row, agent_tail_col = row_col(agent[-1], self.cols)
            agent_tail = { 'row': agent_tail_row, 'col': agent_head_col }
        if len(agent) > 2:
            for agent_body_part in agent[1: len(agent) - 1]:
                agent_body_part_row, agent_body_part_col = row_col(agent_body_part, self.cols) 
                agent_body.append({'row': agent_body_part_row, 'col': agent_body_part_col})
        
        return agent_head, agent_body, agent_tail
    
    def _get_other_geese(self, obs):
        """ Gets the other geese positions """
        other_geese = []
        for goose_idx in range(len(obs.geese)):
            if(goose_idx != obs.index):
                for other_goose_part in obs.geese[goose_idx]:
                    other_goose_part_row, other_goose_part_col = row_col(other_goose_part, self.cols)
                    other_geese.append({'row': other_goose_part_row, 'col': other_goose_part_col})
        
        return other_geese
    
    def _get_food(self, obs):
        """ Gets the food position from the observation """
        transformed_food = []
        for food_pos in obs.food:
            food_row, food_col = row_col(food_pos, self.cols)
            transformed_food.append({'row': food_row, 'col': food_col})
        
        return transformed_food

    def _init_empty_observation(self):
        """ Init an empty observation """
        new_observation = []
        for row in range(self.rows):
            new_observation.append([])
            for col in range(self.cols):
                new_observation[row].append(SpaceValues.EMPTY.value)
        return new_observation
    
    def get_rewards(self):
        pass
