import requests
import time


def measure_load_time(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        return end_time - start_time

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return None


# 👇 THIS PART IS REQUIRED
if __name__ == "__main__":
    sites = [
        "https://www.google.com",
        "https://www.ynet.co.il",
        "https://www.imdb.com"
    ]

    for site in sites:
        time_taken = measure_load_time(site)

        if time_taken:
            print(f"{site} loaded in {time_taken:.4f} seconds")