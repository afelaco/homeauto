from time import sleep

import requests
from bs4 import BeautifulSoup


class CompletionistMeScraper:
    def find_next(self, app_id: str) -> dict[str, str | None]:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(
            url=self.get_url(app_id=app_id),
            headers=headers,
        )
        sleep(1)
        soup = BeautifulSoup(response.text, "html.parser")
        label = soup.find(string="Completion Playtime Avg.")
        if not label:
            completion_playtime_avg = None
        else:
            value_tag = label.find_next()
            completion_playtime_avg = value_tag.text.strip()
        return {
            "app_id": app_id,
            "completion_playtime_avg": completion_playtime_avg,
        }

    @staticmethod
    def get_url(app_id: str) -> str:
        return f"https://completionist.me/steam/app/{app_id}"
