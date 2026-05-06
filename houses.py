import requests

BASE_URL = "https://anapioficeandfire.com/api/houses"

def fetch_all_houses():
    houses_list = []
    page = 1
    page_size = 50

    while True:
        url = f"{BASE_URL}?page={page}&pageSize={page_size}"
        response = requests.get(url)

        if response.status_code != 200:
            print("Error fetching data")
            break

        data = response.json()

        # Stop when no more data
        if not data:
            break

        for house in data:
            name = house.get("name", "").strip()
            region = house.get("region", "").strip()

            # Only include if name exists
            if name:
                houses_list.append((name, region))

        page += 1

    return houses_list


def main():
    # Step 1: Fetch data
    houses = fetch_all_houses()

    # Step 2: Sort alphabetically by house name
    houses_sorted = sorted(houses, key=lambda x: x[0])

    # Step 3: Write to file
    with open("houses.txt", "w", encoding="utf-8") as file:
        for name, region in houses_sorted:
            file.write(f"{name} - {region}\n")

    print("Data written to houses.txt successfully!")


if __name__ == "__main__":
    main()