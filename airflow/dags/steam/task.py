from airflow.decorators import task

from src.airflow.scripts.extract.steam.owned_games import ExtractSteamOwnedGames
from src.airflow.scripts.load.steam.dim_owned_games import LoadDimOwnedGames
from src.airflow.scripts.load.steam.fact_owned_games_tags import LoadFactOwnedGamesTags
from src.airflow.scripts.transform.steam.owned_games import TransformSteamOwnedGames


# Extract
@task
def extract_steam_owned_games() -> None:
    ExtractSteamOwnedGames().run()


# Transform
@task
def transform_steam_owned_games() -> None:
    TransformSteamOwnedGames().run()


# Load
@task
def load_dim_owned_games() -> None:
    LoadDimOwnedGames().run()


@task
def load_fact_owned_games_tags() -> None:
    LoadFactOwnedGamesTags().run()
