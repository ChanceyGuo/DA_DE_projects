# Scenario

I need to compile the list of the top 10 largest banks in the world ranked by market capitalization in billion USD. Further, I need to transform the data and store it in USD, GBP, EUR, and INR per the exchange rate information made available as a CSV file. I should save the processed information table locally in a CSV format and as a database table. Managers from different countries will query the database table to extract the list and note the market capitalization value in their own currency.

## Data URL	
```
https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks
```

# Dependency

requests - The library used for accessing the information from the URL.

bs4 - The library containing the BeautifulSoup function used for webscraping.

pandas - The library used for processing the extracted data, storing it in required formats, and communicating with the databases.

numpy - The library required for the mathematical rounding operations.

datetime - The library containing the function datetime used for extracting the timestamp for logging purposes.

sqlite3 - The library required to create a database server connection.

```
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv
```