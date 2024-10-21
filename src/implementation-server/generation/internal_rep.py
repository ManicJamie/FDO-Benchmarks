from dataclasses import dataclass
from datetime import datetime, timedelta
import random

# Aliases to help keep track of types for when I make this a little tidier
CC = str
ISODate = str
RefUri = str
IANAType = str
RefPath = str
"""A path to be generated into a full URL based on the hostname."""

LICENSES = [
    "https://creativecommons.org/publicdomain/zero/1.0/"
]

def random_delta() -> timedelta:
    """A random delta between 1 day and 10 years."""
    return timedelta(days=random.randint(1, 3650))

def random_date() -> ISODate:
    return (datetime.now() - random_delta()).date().isoformat()

@dataclass
class Author():
    type: str
    id: str  # TODO: RefURI?
    name: str  # TODO: should probably be generic metadata

@dataclass
class Content():
    type: str
    id: RefPath
    """Permanent URL to this content's metadata (?)"""
    name: str
    fileFormat: str
    contentSize: int  # TODO: verify b/B and if other sizing schemes are used
    contentUrl: RefPath
    """Permanent URL to the content datastream"""

@dataclass
class FDO():
    """An internal structure holding data to generate all FDO implementations."""
    name: dict[CC, str]
    description: dict[CC, str]
    date_published: ISODate
    date_modified: ISODate
    is_free: bool
    license: RefUri
    author: list[Author]
    distribution: list[Content]
    
    @classmethod
    def generated(cls, i) -> 'FDO':
        out = FDO(
            name={"en": f"Test object {i}"},
            description={"en": f"Test object {i}'s description"},
            date_published=random_date(),
            date_modified=random_date(),
            is_free=bool(random.randint(0, 1)),
            license=random.choice(LICENSES),
            author=[
                Author(
                    type="Person",
                    id="https://orcid.org/0000-0002-1825-0097",
                    name="Josiah Carberry"
                )
            ],
            distribution=[
                Content(
                    type="DataDownload",  # TODO: add other types
                    id="",
                    name=f"TestContent{i}_0",
                    fileFormat="text/csv",  # TODO: add other types
                    contentSize=0,  # TODO: based on size of block
                    contentUrl=""
                )
            ]
        )
        return out
