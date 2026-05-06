import requests
import csv

BASE_URL = "https://anapioficeandfire.com/api/books"

def fetch_all_data(url):
    all_data = []
    page = 1
    page_size = 50

    while True:
        paginated_url = f"{url}?page={page}&pageSize={page_size}"
        response = requests.get(paginated_url)

        if response.status_code != 200:
            print("Error fetching data")
            break

        data = response.json()


        # If no more data
        if not data:
            break

        all_data.extend(data)
        page += 1

    return all_data


def create_books_dict(data):
    books_dict = {}

    for book in data:
        name = book.get("name", "").strip()
        pages = book.get("numberOfPages", "")
        release_date = book.get("released", "")
        isbn = book.get("isbn", "")
        publisher = book.get("publisher", "")

        if name:
            books_dict[name] = [pages, release_date, isbn, publisher]

    return books_dict


def write_to_csv(books_dict):
    with open("books.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Book Name", "Pages", "Release Date", "ISBN", "Publisher"])

        for name, details in books_dict.items():
            writer.writerow([name] + details)


def main():
    data = fetch_all_data(BASE_URL)
    print("Total records fetched:", len(data))

    books_dict = create_books_dict(data)

    write_to_csv(books_dict)

    print("CSV file created successfully!")


if __name__ == "__main__":
    main()