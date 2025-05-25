# GSoC Organization Scraper

A Python web scraper that extracts organization details from Google Summer of Code (GSoC) archives for the years 2018 to 2024. This tool fetches data from the GSoC API, processes it, and saves the results in both JSON and CSV formats for easy analysis of GSoC participation trends.

## Features
- **Data Extraction**: Retrieves organization names and their participation years from GSoC archives (2018–2024).
- **Rate Limiting**: Implements a respectful 1.5-second delay between API requests to avoid overwhelming the server.
- **Flexible Output**: Saves scraped data in both JSON and CSV formats for versatile use.
- **Error Handling**: Includes basic error checking for failed API requests.
- **Lightweight**: Simple and efficient, with minimal dependencies.

## Prerequisites
- Python 3.6 or higher
- Required Python packages:
  - `requests`
  - `json` (built-in)
  - `csv` (built-in)
  - `time` (built-in)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/webscraper.git
   cd webscraper
   ```
2. Install the required package:
   ```bash
   pip install requests
   ```

## Usage
1. Run the script to scrape GSoC organization data:
   ```bash
   python webscraper.py
   ```
2. The script will:
   - Fetch organization data for each year from 2018 to 2024.
   - Save the results to `gsoc_organizations_2018_to_2024.json` and `gsoc_organizations_2018_to_2024.csv` in the project directory.

## Output
- **JSON File** (`gsoc_organizations_2018_to_2024.json`): Contains a dictionary with organization names as keys and lists of participation years as values.
- **CSV File** (`gsoc_organizations_2018_to_2024.csv`): Lists organizations and their participation years in a tabular format.

Example JSON output:
```json
{
    "Apache Software Foundation": [2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Mozilla": [2018, 2019, 2020],
    ...
}
```

Example CSV output:
```csv
Organization,Years Participated
Apache Software Foundation,2018, 2019, 2020, 2021, 2022, 2023, 2024
Mozilla,2018, 2019, 2020
...
```

## Notes
- The scraper uses the GSoC API (`https://summerofcode.withgoogle.com/api/archive/programs/`). Ensure the API is accessible during execution.
- A `User-Agent` header is included to mimic a browser request and avoid potential blocking.
- The script includes a 1.5-second delay between requests to comply with API rate limits and ensure responsible scraping.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve functionality, add features, or fix bugs.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.


## Acknowledgments
- Thanks to Google Summer of Code for providing the API.
- Built with Python and the `requests` library.
