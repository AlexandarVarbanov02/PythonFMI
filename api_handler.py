import requests
from api_key import API_KEY


class TMDbAPI:
    BASE_URL = "https://api.themoviedb.org/3"
    HEADERS = {"accept": "application/json",
               "Authorization": API_KEY}

    def __init__(self, api_key: str) -> None:
        self.__headers = {"accept": "application/json"}
        self.__api_key = self.__validate_api_key(api_key)
        # self.__guest_session_id = self.__generate_guest_session()

    def __validate_api_key(self, api_key: str) -> str:
        authentication_url = f"{self.BASE_URL}/authentication"
        temp_headers = {
            **self.__headers,
            "Authorization": f"Bearer {api_key}"
        }

        response = requests.get(authentication_url, headers=temp_headers)
        if response.status_code == 200:
            self.__headers = temp_headers
            return api_key
        else:
            raise ValueError(f"Invalid API key: {response.json()}")

    def __generate_guest_session(self) -> str:
        guest_session_url = f"{self.BASE_URL}/authentication/guest_session/new"
        response = requests.get(guest_session_url, headers=self.__headers)
        if response.status_code == 200:
            response_data = response.json()
            return response_data["guest_session_id"]
        else:
            raise RuntimeError(f"Failed to create a guest session: {response.json()}")

    def get_trending(self, content_type: str, time_window: str) -> dict:
        content_types = {"movie", "tv", "all"}
        time_windows = {"day", "week"}
        if content_type not in content_types:
            raise ValueError(f"Invalid content type. Should be one of {content_types}.")
        if time_window not in time_windows:
            raise ValueError(f"Invalid time window. Should be one of {time_windows}.")

        trending_url = f"{self.BASE_URL}/trending/{content_type}/{time_window}"
        all_results = []
        page = 1
        while True:
            response = requests.get(f"{trending_url}?page={page}", headers=self.__headers)
            if response.status_code == 200:
                trending_data = response.json()
                all_results.extend(trending_data.get("results", []))
                # Hard limit for page count
                if page < trending_data["total_pages"] and page < 3:
                    page += 1
                else:
                    break
            else:
                raise RuntimeError(f"Failed to fetch trending {content_type} for {time_window}: {response.json()}")

        sorted_results = sorted(all_results, key=lambda x: x.get('vote_average', 0), reverse=True)
        trending_dict = {item['title'] if 'title' in item else item['name']: item.get('vote_average', 'N/A')
                         for item in sorted_results}

        return trending_dict
