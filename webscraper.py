import requests
import json
import time
import csv
# API endpoint for GSoC 2025 organizations
BaseUrl = 'https://summerofcode.withgoogle.com/api/archive/programs/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json',
}

def fetch_gsoc_organizations():
    organizations = {}
    for year in range(2018,2025):
        time.sleep(1.5)  # Respectful delay to avoid overwhelming the server
        url = f"{BaseUrl}{year}/organizations/"
        # Fetch the data
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to fetch data: {response.status_code}")
            exit()
        else:
            print(f"Successfully fetched data for {year}")
        # Parse the JSON response
        data = response.json()

        # Extract organization names
        for org in data:
            org_name = org.get('name')
            if org_name and org_name not in set(organizations.keys()):
                organizations[org_name] = [year]
            else:
                organizations[org_name].append(year)
    return organizations
    
# Save to a file
def save_to_json(data, filename="gsoc_organizations_2018_to_2024.json"):
    """Save the scraped data to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, sort_keys=True)
    print(f"Data saved to {filename}")

def save_to_csv(data, filename="gsoc_organizations_2018_to_2024.csv"):
    """Save data to CSV file."""
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Organization', 'Years Participated'])
        for org, years in sorted(data.items()):
            writer.writerow([org, ', '.join(map(str, years))])
    print(f"Data saved to {filename}")

def main():
    orgs = fetch_gsoc_organizations()
    save_to_json(orgs)
    save_to_csv(orgs)

if __name__ == "__main__":
    main()