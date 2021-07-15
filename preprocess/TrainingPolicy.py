from stable_baselines3 import DQN
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.torch_layers import BaseFeaturesExtractor

import torch as th
import torch.nn as nn
import torch.nn.functional as F

model_name = "dqn"
m_env = Monitor(env, model_name, allow_early_resets=True)

policy_kwargs = dict(
    net_arch = [2000, 1000, 500, 1000, 500, 100]
)

TRAIN_STEPS = 1e6
alpha_0 = 1e-6
alpha_end = 1e-9

def learning_rate_f(process_remaining):
    #default =  1e-4
    initial = alpha_0
    final = alpha_end
    interval = initial-final
    return final+interval*process_remaining

params ={
    'gamma': .9,
    'batch_size': 100,
     #'train_freq': 500,
    'target_update_interval': 10000,
    'learning_rate': learning_rate_f,
    'learning_starts': 1000,
    'exploration_fraction': .2,
    'exploration_initial_eps': .05,
    'tau': 1,
    'exploration_final_eps': .01,
    'buffer_size': 100000,
    #'verbose': 1,
}

#coment **params for default parameters
trainer = DQN('MlpPolicy', m_env, policy_kwargs=policy_kwargs, **params)
