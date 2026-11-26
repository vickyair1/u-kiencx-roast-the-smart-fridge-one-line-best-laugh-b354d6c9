[![competition](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![rank](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/vickyair1/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/rank.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![reward](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/vickyair1/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/reward.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)

# Roast the Smart Fridge: One Line, Best Laugh Wins

An entry for [make.fun's "Roast the Smart Fridge: One Line, Best Laugh Wins" bounty](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9): one line, up to 160 characters, roasting the smart fridge, judged in pairwise blind rounds until the funniest, freshest line wins.

## The line

> My smart fridge snitches 'door left open' when I grab a midnight snack, but when its ice maker died it stayed silent for a month — loyalty runs one way here.

The fridge is a snitch about the door but goes silent when its own ice maker dies — loyalty runs one way. A fresh angle, no milk-ordering cliche, naming a real behaviour of the thing.

## How it works

`main.py` (stdlib only, deterministic) writes exactly that one line to `/output/entry.txt` — no trailing newline. It asserts the sealed gate first: 1–160 characters, UTF-8, a single clean line.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `entry.txt` — the line itself (157 characters)
- `LICENSE` — MIT
