# type
```
env_runner
<class 'diffusion_policy.env_runner.pusht_keypoints_runner.PushTKeypointsRunner'>
policy
<class 'diffusion_policy.policy.diffusion_unet_lowdim_policy.DiffusionUnetLowdimPolicy'>
```

# data
```
obs:
dict_keys(['obs', 'obs_mask'])
obs:[56, 2, 20]
obs_mask:[56, 2, 20]

action_dict
dict_keys(['action', 'action_pred', 'action_obs_pred', 'obs_pred'])
action:[56,8,2]
action_pred:[56,16,2]
action_obs_pred:[56,8,20]
obs_pred:[56,16,20]

impainting
shape:[56, 16, 22]
To:2
Ta:2

```