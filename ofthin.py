import gym
from kaggle_environments.envs.hungry_geese.hungry_geese import Observation, Configuration, Action, row_col
from kaggle_environments import make
import json
import os
from preprocess.Environment import Environment
from stable_baselines3.common.env_checker import check_env

HTML_RUN_FOLDER = 'runs_html'
JSON_RUN_FOLDER = 'runs_json'
JSON_RUN_COUNTER = 'run_counter.txt'
file = 'myfile.txt'

def main():
    env = Environment()


    check_env(env)

    return 0
#     clean_html()
#     initial_count = get_json_run_count()
#     for i in range(0, 5):
#         game = make('hungry_geese')
#         game.run(['greedy', 'random', 'greedy', 'random'])
#         write_game_replay(game, i)
#         write_data(game, initial_count + i)
#         set_count_file(initial_count + i)
    


# def get_json_run_count():
#     count = 0
#     counter_file_path = os.path.join(JSON_RUN_FOLDER, JSON_RUN_COUNTER)
#     if os.path.exists(counter_file_path):
#         counter_file = open(counter_file_path)
#         count = int(counter_file.readline())
#         print(count)
#     return count


# def set_count_file(count):
#     counter_file_path = os.path.join(JSON_RUN_FOLDER, JSON_RUN_COUNTER)
#     counter_file = open(counter_file_path, 'w')
#     counter_file.write(str(count))


# def write_data(game, count):
#     json_data = game.toJSON()
#     json_file = open(os.path.join(JSON_RUN_FOLDER, 'run_{0}.json'.format(count)), 'w')
#     json.dump(json_data, json_file, indent=4, ensure_ascii=True, sort_keys=True)


# def clean_html():
#     for html_file in os.listdir(HTML_RUN_FOLDER):
#         os.remove(os.path.join(HTML_RUN_FOLDER, html_file))


# def write_game_replay(game, idx):
#     """ Writes game replay to html file """
#     html_string = game.render(mode='html')
#     html_file = open(os.path.join(HTML_RUN_FOLDER, 'run_{0}.html'.format(idx)), 'w')
#     html_file.write(html_string)



if __name__ == '__main__':
    main()
