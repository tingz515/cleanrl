import gym
env = gym.make("CartPole-v1")
observation = env.reset()
total_reward = 0
while True:
    env.render()
    action = env.action_space.sample() # your agent here (this takes random actions)
    observation, reward, done, info = env.step(action)
    total_reward += reward
    if done:
        print(f"total_reward: {total_reward}")
        break
env.close()
