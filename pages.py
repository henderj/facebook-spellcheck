from enum import Enum
from secrets import (
    pageToken_santiago,
    pageToken_la_vega,
    pageToken_navarrete,
    pageToken_puerto_plata,
)

pages = {
    "santiago": {"id": 112473910504378, "token": pageToken_santiago},
    "la_vega": {"id": 107755494333905, "token": pageToken_la_vega},
    "navarrete": {"id": 107764137669344, "token": pageToken_navarrete},
    "puerto_plata": {"id": 101398454989145, "token": pageToken_puerto_plata},
}


class Page(Enum):
    SANTIAGO = "santiago"
    LA_VEGA = "la_vega"
    NAVARRETE = "navarrete"
    PUERTO_PLATA = "puerto_plata"
