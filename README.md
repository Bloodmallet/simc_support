# simc_support [![CI](https://github.com/Bloodmallet/simc_support/workflows/CI/badge.svg)](https://github.com/Bloodmallet/simc_support/actions?query=workflow%3A%22CI%22)

Data to support simulations for World of Warcraft with SimulationCraft for each current expansion. First three versioning numbers match World of Warcrafts' build version.

## Installation

```sh
pip install simc-support
```

## Usage

Get a list of all trinkets
```python
from simc_support.game_data.Trinket import TRINKETS

for trinket in TRINKETS:
    print(f"{trinket.item_id} {trinket.name}")
```

Get a list of all trinkets available to a specific spec
```python
from simc_support.game_data.WowSpec import get_wow_spec
from simc_support.game_data.Trinket import get_trinkets_for_spec

elemental_shaman = get_wow_spec("shaman", "elemental")
trinkets = get_trinkets_for_spec(elemental_shaman)

for trinket in TRINKETS:
    print(f"{trinket.item_id} {trinket.name}")
```

## Data Origin
- Data in `.py` files was written by hand.
- Data in `.json` files is automatically generated with the help of SimulationCrafts casc and dbc scripts. See `./simc_support/self_update.py` in the repository for more informtion.

**Exception**: Dragonflight Talent data (also `.json` files) is being prepared by [raidbots.com](https://www.raidbots.com/simbot). Permission was granted to use it here.
