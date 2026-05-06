import requests
from openpyxl import Workbook

BASE_URL = "https://anapioficeandfire.com/api/characters"

def fetch_all_characters():
    characters = []
    page = 1
    page_size = 50

    while True:
        url = f"{BASE_URL}?page={page}&pageSize={page_size}"
        response = requests.get(url)

        if response.status_code != 200:
            print("Error fetching data")
            break

        data = response.json()

        if not data:
            break

        characters.extend(data)
        page += 1

    return characters


def process_characters(data):
    result = []

    for char in data:
        name = char.get("name", "").strip()
        tv_series = char.get("tvSeries", [])

        # Some characters have no name → skip
        if not name:
            continue

        season_count = len([s for s in tv_series if s])

        result.append((name, season_count))

    return result


def write_to_excel(data):
    wb = Workbook()
    ws = wb.active
    ws.title = "Characters"

    # Header
    ws.append(["Character Name", "Season Appearances"])

    # Data
    for row in data:
        ws.append(row)

    wb.save("characters.xlsx")


def main():
    print("Fetching characters...")

    data = fetch_all_characters()
    print("Total characters:", len(data))

    processed = process_characters(data)

    # Sort by season count (descending)
    sorted_data = sorted(processed, key=lambda x: x[1], reverse=True)

    write_to_excel(sorted_data)

    print("Excel file created successfully!")


if __name__ == "__main__":
    main()