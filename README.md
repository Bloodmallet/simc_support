# simc_support
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
