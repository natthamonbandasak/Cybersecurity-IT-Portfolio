# Python Automation & Data Management

This repository contains a comprehensive collection of Python scripts developed to handle data processing, web scraping, API interactions, and relational database management. These projects demonstrate my ability to programmatically automate IT operations tasks, extract value from raw logs, and manage data effectively.

## 🛠️ Core Skills Demonstrated

* **Database Management (SQLite):** Designing and populating relational databases (One-to-Many, Many-to-Many) from raw CSV and JSON files.
* **Web Scraping & Networking:** Establishing low-level TCP socket connections, parsing HTML Document Object Models (DOM) using BeautifulSoup, and building automated web crawlers.
* **API & Multi-Format Processing:** Retrieving, processing, and formatting nested data from external REST APIs across various formats (JSON, XML).
* **Log Analysis & Regex:** Extracting and cleaning specific data points (e.g., IPs, email domains) from raw server text and log files using Regular Expressions.
* **Process Automation:** Utilizing advanced data structures (Lists, Dictionaries, Tuples) and conditional loops to automate repetitive data-handling tasks.

## 📂 Repository Contents

### 1. Database Management (SQLite)

Scripts demonstrating data migration and relational database architecture.

* `domain_activity_db.py` - Parses email logs to extract sender domains and tracks their frequency in an SQLite database.
* `csv_to_relational_db.py` - Migrates raw CSV music data into a normalized One-to-Many relational database (Artist, Genre, Album, Track).
* `json_m2m_database.py` - Parses a JSON roster file and populates a Many-to-Many relational database structure (User, Course, Member).

### 2. Web Scraping, API & Network Protocols

Tools for interacting with external servers and extracting web data.

* `network_socket_client.py` - Establishes a low-level TCP socket connection and sends raw HTTP GET requests.
* `web_data_scraper.py` - Bypasses SSL to scrape and parse HTML data using BeautifulSoup.
* `recursive_link_crawler.py` - An automated spider that recursively crawls web pages by extracting and following anchor tags.
* `xml_data_extractor.py` - Fetches XML data from a URL and parses the XML tree to extract specific node values.
* `json_api_fetcher.py` - Fetches and parses JSON data from a REST API endpoint.
* `geo_api_query_handler.py` - Queries a location API with URL parameters and securely extracts deeply nested JSON geographical data.

### 3. Log Analysis & Data Parsing

Scripts designed for IT Support and SysAdmin log monitoring tasks.

* `regex_data_extractor.py` - Extracts numeric values from unstructured text files using Regular Expressions.
* `log_confidence_analyzer.py` - Scans log files to extract and compute the average spam confidence score.
* `email_log_extractor.py` - Filters log files to extract and count unique sender email addresses.
* `top_sender_analyzer.py` - Uses Python Dictionaries to identify the most frequent email sender in a server log.
* `hourly_activity_analyzer.py` - Parses timestamps from logs and sorts data to analyze peak system activity hours.
* `file_log_reader.py` - Safely opens files with error handling and processes text content line-by-line.
* `log_string_parser.py` - Dynamically slices strings to extract specific floating-point data from log entries.

### 4. Core Logic & Computation

Foundational algorithms for data validation and mathematical operations.

* `overtime_calculator.py` - Computes gross pay with condition-based overtime rates.
* `score_evaluator.py` - Evaluates numerical inputs against a multi-tier grading matrix.
* `number_accumulator.py` - Uses while-loops to continuously accept user input, validating and accumulating totals.
* `min_max_tracker.py` - Algorithm that tracks and returns the maximum and minimum values from a dynamic stream of user inputs.

---

*(Note: These projects build upon the foundational concepts from the University of Michigan's "Python for Everybody" coursework, adapted and expanded to showcase production-ready IT operations and data management skills.)*
