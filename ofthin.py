from kaggle_environments.envs.hungry_geese.hungry_geese import Observation, Configuration, Action, row_col
from kaggle_environments import make


def main():
    game = make('hungry_geese')
    game.run([agent, agent])
    write_game_replay(game)
    return 0


def write_game_replay(game):
    """ Writes game replay to html file """
    html_string = game.render(mode='html')
    html_file = open('./replay.html', 'w')
    html_file.write(html_string)


def agent(obs_dict, config_dict):
    """This agent always moves toward observation.food[0] but does not take advantage of board wrapping"""
    print(obs_dict)
    observation = Observation(obs_dict)
    configuration = Configuration(config_dict)
    player_index = observation.index
    player_goose = observation.geese[player_index]
    player_head = player_goose[0]
    player_row, player_column = row_col(player_head, configuration.columns)
    food = observation.food[0]
    food_row, food_column = row_col(food, configuration.columns)

    if food_row > player_row:
        return Action.SOUTH.name
    if food_row < player_row:
        return Action.NORTH.name
    if food_column > player_column:
        return Action.EAST.name
    return Action.WEST.name


if __name__ == '__main__':
    main()
