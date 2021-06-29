from kaggle_environments.envs.hungry_geese.hungry_geese import Action


def get_opposite_action(action):
    """ Get the opposite direction for a given action """
    action_switch = { 
        Action.NORTH: Action.SOUTH,
        Action.WEST: Action.EAST,
        Action.SOUTH: Action.NORTH,
        Action.EAST: Action.WEST
    }

    return action_switch[action]
