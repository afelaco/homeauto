from homeauto.core.api.response_model.scryfall.cards import ScryfallCardsApiResponseModel
from homeauto.core.endpoint import Endpoint

cards = Endpoint(
    url="cards/search",
    response_model=ScryfallCardsApiResponseModel,
)
