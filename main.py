import csv
from scraper import fetch_data, find_table

url = "https://en.wikipedia.org/wiki/ISO_4217"
file_csv = "file.csv"

def main():
    tags = fetch_data(url)
    save_t = find_table(tags)
    with open(file_csv, 'w', newline='', encoding='utf-8') as file:
        w = csv.writer(file)
        w.writerow(['Code', 'Nums', 'Currency'])
        w.writerows(save_t)

if __name__ == "__main__":
    main()
