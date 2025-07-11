# ETL-Pipeline-for-Country-GDP-Bank-Market-Capitalization-Data

This project showcases a Python-based ETL (Extract, Transform, Load) pipeline that processes financial data related to the world’s largest banks. The pipeline extracts bank market capitalization data from a public webpage, transforms it into multiple currencies using live exchange rates, and loads the final dataset into both a CSV file and a SQLite database. A series of queries are then executed on the database to derive insights.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [ETL Pipeline Flow](#etl-pipeline-flow)
- [How to Run](#how-to-run)
- [Sample Output](#sample-output)
- [Author](#author)

---

## 🧠 About the Project

This project was developed as part of a **Python for Data Engineering** course. The goal was to simulate a real-world ETL task by:

- Extracting structured financial data from a Wikipedia page
- Enhancing the data using exchange rate conversion
- Loading the transformed data into persistent storage formats
- Executing SQL queries for quick analytics

---

## 🗂️ Project Structure

- ├── **exchange_rate.csv** — Exchange rates for currency conversion
- ├── **ETL_script.py** — Main ETL logic in Python
- ├── **Largest_banks_data.csv** — Final transformed dataset
- ├── **World_Economies.db** — SQLite database with loaded data
- └── **code_log.txt** — Log file tracking ETL process execution

---

## 💻 Technologies Used

- **Python** 🐍
- **Pandas & NumPy** — For data wrangling and numeric operations
- **Requests & BeautifulSoup** — For web scraping HTML content
- **SQLite3** — Lightweight SQL database for data persistence
- **datetime** — For timestamp logging

---

## 🔁 ETL Pipeline Flow

| Step         | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| **Extract**  | Bank data is scraped from an archived Wikipedia page listing the largest banks by market cap. |
| **Transform**| Market capitalization in USD is converted into GBP, EUR, and INR using exchange rates from a local CSV. |
| **Load**     | The final dataset is saved to both a `.csv` file and a SQLite database.     |
| **Query**    | SQL queries are executed to inspect data and derive summaries (e.g., average market cap in GBP). |
| **Logging**  | Each ETL stage is logged into `code_log.txt` with a timestamp.              |

---

## 🔁 Sample Output Queries

- **SELECT * FROM Largest_banks**

- Get average market cap in GBP:
**SELECT AVG(MC_GBP_Billion) FROM Largest_banks**

- Get names of first 5 banks:
**SELECT Name FROM Largest_banks LIMIT 5**

---

## ▶️ How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/Banks_project.git
   cd your-etl-project

---

## ▶️ Ensures dependencies are installed
- pip install pandas numpy requests beautifulsoup4
- pip install numpy
- import requests
- import BeautifulSoup
- from datetime import datetime
- import Sqlite3

---
## 🙋 Author
- **PhD Candidate in Applied Mathematics Gael Dimitri Tekam Fongouo**
- **Feel free to connect with me on LinkedIn or explore more of my projects on GitHub**
