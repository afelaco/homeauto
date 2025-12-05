from typing import List, Optional

from pydantic import BaseModel

from homeauto.core.api.response_model.scryfall import ScryfallApiResponseModel


class ImageUris(BaseModel):
    small: Optional[str]
    normal: Optional[str]
    large: Optional[str]
    png: Optional[str]
    art_crop: Optional[str]
    border_crop: Optional[str]


class AllPart(BaseModel):
    object: str
    id: str
    component: str
    name: str
    type_line: str
    uri: str


class Legalities(BaseModel):
    standard: str
    future: str
    historic: str
    timeless: str
    gladiator: str
    pioneer: str
    modern: str
    legacy: str
    pauper: str
    vintage: str
    penny: str
    commander: str
    oathbreaker: str
    standardbrawl: str
    brawl: str
    alchemy: str
    paupercommander: str
    duel: str
    oldschool: str
    premodern: str
    predh: str


class Prices(BaseModel):
    usd: Optional[str]
    usd_foil: Optional[str]
    usd_etched: Optional[str]
    eur: Optional[str]
    eur_foil: Optional[str]
    tix: Optional[str]


class RelatedUris(BaseModel):
    gatherer: Optional[str] = None
    tcgplayer_infinite_articles: Optional[str]
    tcgplayer_infinite_decks: Optional[str]
    edhrec: Optional[str]


class PurchaseUris(BaseModel):
    tcgplayer: Optional[str]
    cardmarket: Optional[str]
    cardhoarder: Optional[str]


class Card(BaseModel):
    object: str
    id: str
    oracle_id: str
    multiverse_ids: Optional[List[int]]
    mtgo_id: Optional[int] = None
    mtgo_foil_id: Optional[int] = None
    arena_id: Optional[int] = None
    tcgplayer_id: Optional[int] = None
    cardmarket_id: Optional[int] = None
    name: str
    lang: str
    released_at: str
    uri: str
    scryfall_uri: str
    layout: str
    highres_image: bool
    image_status: str
    image_uris: Optional[ImageUris] = None
    mana_cost: Optional[str] = None
    cmc: float
    type_line: str
    oracle_text: Optional[str] = None
    power: Optional[str] = None
    toughness: Optional[str] = None
    colors: Optional[List[str]] = None
    color_identity: Optional[List[str]]
    keywords: Optional[List[str]]
    all_parts: Optional[List[AllPart]] = None
    legalities: Legalities
    games: List[str]
    reserved: bool
    game_changer: bool
    foil: bool
    nonfoil: bool
    finishes: List[str]
    oversized: bool
    promo: bool
    reprint: bool
    variation: bool
    set_id: str
    set: str
    set_name: str
    set_type: str
    set_uri: str
    set_search_uri: str
    scryfall_set_uri: str
    rulings_uri: str
    prints_search_uri: str
    collector_number: str
    digital: bool
    rarity: str
    watermark: Optional[str] = None
    card_back_id: Optional[str] = None
    artist: str
    artist_ids: List[str]
    illustration_id: Optional[str] = None
    border_color: str
    frame: str
    full_art: bool
    textless: bool
    booster: bool
    story_spotlight: bool
    edhrec_rank: Optional[int] = None
    penny_rank: Optional[int] = None
    prices: Prices
    related_uris: RelatedUris
    purchase_uris: Optional[PurchaseUris] = None


ScryfallCardsApiResponseModel = ScryfallApiResponseModel[Card]
