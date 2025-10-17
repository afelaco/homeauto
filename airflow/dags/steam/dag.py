from datetime import datetime, UTC, timedelta

from airflow.decorators import dag

from dags.steam.task import (
    extract_steam_owned_games,
    transform_steam_owned_games,
    load_dim_owned_games,
    load_fact_owned_games_tags,
)


@dag(
    dag_id="steam",
    description="Steam Data ETL Pipeline",
    tags=["steam", "weekly"],
    start_date=datetime(2025, 9, 20, tzinfo=UTC),
    schedule="@weekly",
    catchup=False,
    max_active_runs=1,
    max_active_tasks=1,
    default_args={
        "owner": "alessandro.felaco",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
        "execution_timeout": timedelta(minutes=5),
    },
)
def steam() -> None:
    tsog = transform_steam_owned_games()

    extract_steam_owned_games() >> tsog
    tsog >> load_dim_owned_games()
    tsog >> load_fact_owned_games_tags()


steam()
