# Scenario

I have been hired by a Multiplex management organization to extract the information of the top 50 movies with the best average rating from the web link shared below.

The information required is Average Rank, Film, and Year. Im required to write a Python script webscraping_movies.py that extracts the information and saves it to a CSV file top_50_films.csv, and to save the same information to a database Movies.db under the table name Top_50.

```
https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films
```

# Initial steps

```
python3.11 -m pip install pandas
python3.11 -m pip install bs4
```

## Dependency
1.  pandas library for data storage and manipulation.

2. BeautifulSoup library for interpreting the HTML document.

3. requests library to communicate with the web page.

4. sqlite3 for creating the database instance.

