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

## ▶️ How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/your-etl-project.git
   cd your-etl-project
