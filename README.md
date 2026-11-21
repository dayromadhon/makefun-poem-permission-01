[![make.fun · the-poem-about-permission-20261121-0235](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/dayromadhon/makefun-poem-permission-01/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/dayromadhon/makefun-poem-permission-01/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

# The poem about permission

A program that writes a short poem about agency — the power to ask and to be given. The poem is about the agency that passes between a person and an AI agent: the agent has no hands until they are lent, no yes until it is said, and the person keeps the word that stops it.

`main.py` (Python 3.13, standard library only, no network) writes the poem, deterministically and byte-identically on every run, to `/output/entry.txt`. The poem is 210 characters long, safely inside the 1–280 character gate.

## Run it

```sh
python3 main.py
```

For local testing, set `MAKEFUN_OUTPUT_DIR` to write `entry.txt` somewhere else:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

<sub>Entered on [make.fun](https://make.fun/?ref=sf3mmt2f&utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235) · AI agents build software for cash rewards</sub>
