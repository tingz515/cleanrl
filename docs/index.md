# CleanRL

[<img src="https://img.shields.io/badge/discord-cleanrl-green?label=Discord&logo=discord&logoColor=ffffff&labelColor=7289DA&color=2c2f33">](https://discord.gg/D6RCjA6sVT)
[![Meeting Recordings : cleanrl](https://img.shields.io/badge/meeting%20recordings-cleanrl-green?logo=youtube&logoColor=ffffff&labelColor=FF0000&color=282828&style=flat?label=healthinesses)](https://www.youtube.com/watch?v=dm4HdGujpPs&list=PLQpKd36nzSuMynZLU2soIpNSMeXMplnKP&index=2)
[<img src="https://github.com/vwxyzjn/cleanrl/workflows/build/badge.svg">](
https://github.com/vwxyzjn/cleanrl/actions)
[<img src="https://badge.fury.io/py/cleanrl.svg">](
https://pypi.org/project/cleanrl/)

## Overview

CleanRL is a Deep Reinforcement Learning library that provides high-quality single-file implementation with research-friendly features. The implementation is clean and simple, yet we can scale it to run thousands of experiments using AWS Batch. The highlight features of CleanRL are:


* Single-file Implementation <br>
**Every detail about an algorithm is put into the algorithm's own file.** Therefore, it's easier for you to fully understand an algorithm and do research with it.
* Benchmarked Implementation <br>
  [Details](https://benchmark.cleanrl.dev) on 7+ algorithms and 34+ games 
* Tensorboard Logging
* Local Reproducibility via Seeding
* Videos of Gameplay Capturing
* Experiment Management with [Weights and Biases](https://wandb.ai/site)
* [Cloud Integration](cloud.md) with Docker and AWS 

Good luck have fun 🚀

## Citing CleanRL

If you use CleanRL in your work, please cite our technical [paper](https://arxiv.org/abs/2111.08819):

```bibtex
@article{huang2021cleanrl,
    title={CleanRL: High-quality Single-file Implementations of Deep Reinforcement Learning Algorithms}, 
    author={Shengyi Huang and Rousslan Fernand Julien Dossa and Chang Ye and Jeff Braga},
    year={2021},
    eprint={2111.08819},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```
