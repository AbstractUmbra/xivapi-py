# xivapi.py
An asynchronous Python client for XIVAPI

[![PyPI version](https://badge.fury.io/py/xivapi.py.svg)](https://badge.fury.io/py/xivapi.py)
[![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/downloads/release/python-360/)

## Requirements
```
python>=3.6.0
asyncio
aiohttp
```

## Installation
```
pip install xivapi.py
```

## Supported API end points

* /character/search
* /character/id
* /character/verify
* /character/update
* /freecompany/search
* /freecompany/id
* /linkshell/search
* /linkshell/id
* /pvpteam/search
* /pvpteam/id
* /index/search (e.g. recipe, item, action, pvpaction, mount, e.t.c.)
* /index/id
* /lore/search
* /market/item/id?servers=["Phoenix"]
* /market/item/id?dc=Chaos

## Documentation
https://xivapi.com/docs/

## Example
```python
import asyncio
import logging

import aiohttp
import xivapi


async def fetch_example_results(session):
    client = xivapi.Client(session=session, api_key="your_key_here")

    # Search Lodestone for a character
    character = await client.character_search(
        world="phoenix", 
        forename="lethys", 
        surname="luculentus"
    )

    # Get a character by Lodestone ID with extended data & include their Free Company information, if it has been synced.
    character = await client.character_by_id(
        lodestone_id=8255311, 
        extended=True,
        include_freecompany=True
    )

    # Search Lodestone for a free company
    freecompany = await client.freecompany_search(
        world="gilgamesh", 
        name="Elysium"
    )

    # Fuzzy search XIVAPI game data for a recipe by name. Results will be in English.
    recipe = await client.index_search(
        name="Crimson Cider", 
        indexes=["Recipe"], 
        columns=["ID", "Name", "Icon", "ItemResult.Description"], 
        string_algo="fuzzy"
    )

    # Fuzzy search XIVAPI game data for a recipe by name. Results will be in French.
    recipe = await client.index_search(
        name="Cidre carmin", 
        indexes=["Recipe"], 
        columns=["ID", "Name", "Icon", "ItemResult.Description"], 
        string_algo="fuzzy", 
        language="fr"
    )

    # Get an item by its ID (Omega Rod) and return the data in German
    item = await client.index_by_id(
        index="Item", 
        content_id=23575, 
        columns=["ID", "Name", "Icon", "ItemUICategory.Name"], 
        language="de"
    )


    # Get non-npc actions matching a given term (Defiance)
    action = await client.index_search(
        name="Defiance", 
        indexes=["Action", "PvPAction", "CraftAction"], 
        columns=["ID", "Name", "Icon", "Description", "ClassJobCategory.Name", "ClassJobLevel", "ActionCategory.Name"], 
        filters=["ClassJobLevel>=0", "ClassJobCategory.ID>0"],
        string_algo="fuzzy"
    )

    # Search ingame data for matches against a given query. Includes item, minion, mount & achievement descriptions, quest dialog & more.
    lore = await client.lore_search(
        query="Shiva",
        language="fr"
    )

    # Get current sales & sale history of an item (Shakshouka) on Phoenix & Odin
    market = await client.market_by_worlds(
        item_id=24280, 
        worlds=["Phoenix", "Odin"]
    )

    # Get current sales & sale history of an item (Shakshouka) on all worlds on the Chaos datacenter with a
    # maximum history of 10
    market = await client.market_by_datacenter(
        item_id=24280, 
        datacenter="Chaos", 
        max_history=10
    )

    await session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='%H:%M')

    loop = asyncio.get_event_loop()
    session = aiohttp.ClientSession(loop=loop)
    loop.run_until_complete(fetch_example_results(session))
```
