from gym.envs.registration import register
import diffusion_policy.env.qf_push_square

register(
    id='qf_push_square-keypoints-v0',
    entry_point='envs.qf_push_square.qf_push_square_keypoints_env:QfPushSquareKeypointsEnv',
    max_episode_steps=200,
    reward_threshold=1.0
)