from functools import lru_cache
import json
from pathlib import Path
import os
import logging

from pydantic import BaseModel

CREDENTIALS_JSON = 'credentials.json'

class BridgeConfig(BaseModel):
    client_id: str
    client_secret: str
    server_token: str
    browser_token: str


@lru_cache
def make_config() -> BridgeConfig:
    """ cache a config for pulling bridge real estate data

    Returns:
        BridgeConfig: The needed config
    """
    # reads from the top of the project
    p = Path(__file__).parents[2]
    logging.debug(f"Path is {p} for {CREDENTIALS_JSON}")

    with open(os.path.join(p,CREDENTIALS_JSON), 'r') as f:
        data = json.load(f)
    return BridgeConfig(**data)
