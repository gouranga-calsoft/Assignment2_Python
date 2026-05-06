# 🐉 Ice and Fire API Assignment (Python)

## 📌 Overview

This project uses **Python** to interact with the **An API of Ice and Fire** and perform data extraction, processing, and storage.

It consists of three independent scripts:

* 🏰 Houses Data Processing
* 📚 Books Data Processing
* 🧙 Characters Data Processing

Each script fetches data from the API, processes it, and stores it in different file formats.

---

## 📂 Project Structure

```
ASSIGNMENT_2(PYTHON CODES)/
│
├── houses.py              # Fetch and store houses data
├── houses.txt             # Output file (sorted houses)
├── houses_Output_Screenshot.png
│
├── books.py               # Fetch and store books data
├── books.csv              # Output file (books data)
├── books_Output_Screenshot.png
│
├── characters.py          # Fetch and store characters data
├── characters.xlsx        # Output file (characters data)
├── characters_Output_Screenshot.png
```

---

## ⚙️ Functionality

### 🏰 Q1: Houses of Ice and Fire

* Fetches all houses using API pagination
* Extracts:

  * House Name
  * Region
* Filters out empty names
* Sorts data alphabetically
* Saves output to `houses.txt`

---

### 📚 Q2: Books of Ice and Fire

* Fetches all books using API pagination
* Creates dictionary:

  ```
  {book_name: [pages, release_date, ISBN, publisher]}
  ```
* Writes structured data into `books.csv`

---

### 🧙 Q3: Characters of Ice and Fire

* Fetches all characters using API pagination
* Processes:

  * Character name
  * Number of TV series appearances
* Ignores unnamed characters
* Sorts by appearances (descending)
* Saves output into `characters.xlsx`

---

## 🔁 API Handling

All scripts implement **pagination** using:

* `page`
* `pageSize = 50`

Loop continues until:

```
No data is returned from API
```

---

## 🚀 How to Run

### 1️⃣ Install Dependencies

```bash
pip install requests openpyxl
```

---

### 2️⃣ Run Scripts

#### ▶ Houses

```bash
python houses.py
```

#### ▶ Books

```bash
python books.py
```

#### ▶ Characters

```bash
python characters.py
```

---

## 📊 Output Files

| Script        | Output File     | Description                       |
| ------------- | --------------- | --------------------------------- |
| houses.py     | houses.txt      | Sorted list of houses with region |
| books.py      | books.csv       | Books data in tabular format      |
| characters.py | characters.xlsx | Characters sorted by appearances  |

---

## 🖼️ Screenshots

Screenshots of outputs are included:

* houses_Output_Screenshot.png
* books_Output_Screenshot.png
* characters_Output_Screenshot.png

---

## ⚠️ Important Notes

* API errors are handled using status code checks
* Empty records (like missing names) are ignored
* Internet connection is required
* Pagination ensures all records are fetched

---

## 🧠 Technologies Used

* Python 3
* requests (API calls)
* csv module (CSV handling)
* openpyxl (Excel handling)

---

## 🎯 Key Learning Outcomes

* Working with REST APIs
* Handling pagination in real-world APIs
* Data cleaning and filtering
* Sorting and structuring data
* Writing data to multiple formats (TXT, CSV, Excel)

---

## 👨‍💻 Author

**Gouranga Ghosh**

---

## ⭐ Acknowledgement

Data provided by the **An API of Ice and Fire**.
