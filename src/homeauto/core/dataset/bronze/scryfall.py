from pandera.polars import Column, DataFrameSchema
from polars import Boolean, Float64, Int64, List, Null, String, Struct

from homeauto.core.dataset.bronze import BronzeDataset

cards = BronzeDataset(
    container="scryfall",
    name="cards",
    schema=DataFrameSchema(
        columns={
            "object": Column(String),
            "id": Column(String, unique=True),
            "oracle_id": Column(String),
            "multiverse_ids": Column(List(Int64)),
            "mtgo_id": Column(Int64, nullable=True),
            "mtgo_foil_id": Column(Int64, nullable=True),
            "arena_id": Column(Int64, nullable=True),
            "tcgplayer_id": Column(Int64, nullable=True),
            "cardmarket_id": Column(Int64, nullable=True),
            "name": Column(String),
            "lang": Column(String),
            "released_at": Column(String),
            "uri": Column(String),
            "scryfall_uri": Column(String),
            "layout": Column(String),
            "highres_image": Column(Boolean),
            "image_status": Column(String),
            "image_uris": Column(
                Struct(
                    {
                        "small": String,
                        "normal": String,
                        "large": String,
                        "png": String,
                        "art_crop": String,
                        "border_crop": String,
                    }
                ),
                nullable=True,
            ),
            "mana_cost": Column(String, nullable=True),
            "cmc": Column(Float64),
            "type_line": Column(String),
            "oracle_text": Column(String, nullable=True),
            "power": Column(String, nullable=True),
            "toughness": Column(String, nullable=True),
            "colors": Column(List(String), nullable=True),
            "color_identity": Column(List(String)),
            "keywords": Column(List(String)),
            "all_parts": Column(
                List(
                    Struct(
                        {
                            "object": String,
                            "id": String,
                            "component": String,
                            "name": String,
                            "type_line": String,
                            "uri": String,
                        }
                    )
                ),
                nullable=True,
            ),
            "legalities": Column(
                Struct(
                    {
                        "standard": String,
                        "future": String,
                        "historic": String,
                        "timeless": String,
                        "gladiator": String,
                        "pioneer": String,
                        "modern": String,
                        "legacy": String,
                        "pauper": String,
                        "vintage": String,
                        "penny": String,
                        "commander": String,
                        "oathbreaker": String,
                        "standardbrawl": String,
                        "brawl": String,
                        "alchemy": String,
                        "paupercommander": String,
                        "duel": String,
                        "oldschool": String,
                        "premodern": String,
                        "predh": String,
                    }
                )
            ),
            "games": Column(List(String)),
            "reserved": Column(Boolean),
            "game_changer": Column(Boolean),
            "foil": Column(Boolean),
            "nonfoil": Column(Boolean),
            "finishes": Column(List(String)),
            "oversized": Column(Boolean),
            "promo": Column(Boolean),
            "reprint": Column(Boolean),
            "variation": Column(Boolean),
            "set_id": Column(String),
            "set": Column(String),
            "set_name": Column(String),
            "set_type": Column(String),
            "set_uri": Column(String),
            "set_search_uri": Column(String),
            "scryfall_set_uri": Column(String),
            "rulings_uri": Column(String),
            "prints_search_uri": Column(String),
            "collector_number": Column(String),
            "digital": Column(Boolean),
            "rarity": Column(String),
            "watermark": Column(String, nullable=True),
            "card_back_id": Column(String, nullable=True),
            "artist": Column(String),
            "artist_ids": Column(List(String)),
            "illustration_id": Column(String, nullable=True),
            "border_color": Column(String),
            "frame": Column(String),
            "full_art": Column(Boolean),
            "textless": Column(Boolean),
            "booster": Column(Boolean),
            "story_spotlight": Column(Boolean),
            "edhrec_rank": Column(Int64, nullable=True),
            "penny_rank": Column(Int64, nullable=True),
            "prices": Column(
                Struct(
                    {
                        "usd": String,
                        "usd_foil": String,
                        "usd_etched": Null,
                        "eur": String,
                        "eur_foil": String,
                        "tix": String,
                    }
                )
            ),
            "related_uris": Column(
                Struct(
                    {
                        "gatherer": String,
                        "tcgplayer_infinite_articles": String,
                        "tcgplayer_infinite_decks": String,
                        "edhrec": String,
                    }
                )
            ),
            "purchase_uris": Column(
                Struct(
                    {
                        "tcgplayer": String,
                        "cardmarket": String,
                        "cardhoarder": String,
                    }
                ),
                nullable=True,
            ),
        },
        strict=True,
    ),
)
