import json
import csv
from typing import Optional


class DataSaver:
    @staticmethod
    def save_to_csv(data: dict, filename: Optional[str] = "results.csv") -> None:
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Rating"])
                for name, rating in data.items():
                    writer.writerow([name, rating])
        except Exception as e:
            print(f"Failed to save in a csv file: {e}")

    @staticmethod
    def save_to_json(data: dict, filename: Optional[str] = "results.json") -> None:
        try:
            with open(filename, mode='w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Failed to save in a json file: {e}")