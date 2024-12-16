import sys
import api_handler
from data_saver import DataSaver
from api_key import API_KEY


def main():
    if len(sys.argv) < 3:
        print("Not enough parameters provided.")
        sys.exit(1)

    content_type = sys.argv[1]
    time_window = sys.argv[2]
    file_format = sys.argv[3]

    if file_format not in ["json", "csv"]:
        print("Invalid file format.")
        sys.exit(1)

    try:
        api = api_handler.TMDbAPI(API_KEY)
        trending_data = api.get_trending(content_type, time_window)
        if file_format == "json":
            DataSaver.save_to_json(trending_data)
        elif file_format == "csv":
            DataSaver.save_to_csv(trending_data)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
