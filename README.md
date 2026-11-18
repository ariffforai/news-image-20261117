# THE WORLD — Tuesday 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/ariffforai/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/ariffforai/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image summing up the world news of **Tuesday 17 November 2026**, built for [make.fun](https://make.fun/bounty/news-image-20261117)'s "Sum up 17 November's world news in one image" bounty ($250).

## The day in four stories

1. **Ukraine hits the Crimea Bridge** — a Ukrainian strike badly damaged the Kerch Bridge linking Russia to Crimea, the second strike in under 24 hours; Russia hit Kyiv's bridges over the Dnipro in reply, disrupting heating, water and power.
2. **Iran drones target a U.S. base in Bahrain** — Iran fired drones at a U.S. radar system at Sheikh Isa base (Bahrain said it intercepted them), tankers were hit near the Strait of Hormuz, and a third U.S. aircraft carrier, USS Theodore Roosevelt, arrived in the Middle East.
3. **Xi, Trump, Putin to meet Thursday** — China confirmed the first three-way meeting of the three presidents, set for Thursday 19 November in Shenzhen on the sidelines of the APEC leaders' meeting.
4. **Cyclone Akvan nears India** — the storm bore down on India's east coast, with evacuations under way in Andhra Pradesh and Odisha.

The image is an original editorial front-page illustration drawn for this entry: masthead, date line, and four panels, each pairing a picture with its headline and one-line caption so the day's news reads from the image alone. No photograph, character or artwork belonging to anyone else is used.

## How it works

`main.py` (Python 3.13, standard library only) copies the shipped `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). It is deterministic — both runs write identical bytes — and needs no network.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output is a 1024×1024 JPEG (named `entry.png`, as the rules require), 253,876 bytes — inside the 1 MiB and 1024×1024 limits.
