# Scenario

I take on the role of a Junior Data Analyst working in a local government office. My task is to work with real-world fleet inventory data and demonstrate my ability to clean, prepare, and analyze it using Excel for the web.

In Part 1, I focus on data cleaning and preparation, making sure the dataset is accurate, complete, and well-formatted for analysis. This includes identifying and fixing common data quality issues such as missing values, duplicates, and inconsistent formatting.

In Part 2, I use the cleaned data to perform data analysis with pivot tables, uncovering insights about equipment usage and departmental distribution. These analyses form the foundation for future data visualizations and reporting.

# Dataset 
- Part1
```

https://data.montgomerycountymd.gov/Government/Fleet-Equipment-Inventory/93vc-wpdr/about_data

```

- Part2
```

https://data.montgomerycountymd.gov/Government/Fleet-Equipment-Inventory/93vc-wpdr

```

# Operations

- Part1

This task involved cleaning and preparing the fleet inventory dataset in Excel for the web. First, the original CSV file was converted and saved as an XLSX file. Next, all column widths were adjusted so that the data was clearly visible. Empty rows were identified with filters and removed, and duplicate records were checked and deleted using Conditional Formatting or Remove Duplicates. The dataset was then reviewed for spelling errors and corrected where needed. Extra whitespace, including double spaces, was removed using Find and Replace. Finally, department names that had been split across two columns were combined into a single correct department column using Flash Fill, and the unnecessary extra column was removed.

- Part2

In this part of the task, the cleaned dataset was first formatted as an Excel table. AutoSum was then used on column C to calculate the sum, average, minimum, maximum, and count values. After that, three pivot tables were created in separate worksheets named Pivot Table 1, Pivot Table 2, and Pivot Table 3. Pivot Table 1 summarized the total equipment count by department and was sorted in descending order by total count. Pivot Table 2 was modified by placing Equipment Class below Department to show vehicle types under each department, then all groups were collapsed except Transportation. Pivot Table 3 was modified by placing Equipment Class above Department to show vehicle types first and departments underneath, then all groups were collapsed except CUV. Finally, the worksheets were arranged in the required order and the completed workbook was downloaded as the final XLSX file.
