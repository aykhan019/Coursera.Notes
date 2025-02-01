

# Module 2: Data Wrangling
## Introduction to Data Pre-processing Techniques
Data pre-processing, also known as data cleaning or data wrangling, is a crucial step in data analysis. It involves transforming raw data into a format suitable for analysis. Here are the key topics covered in data pre-processing:
#### Identifying and Handling Missing Values
- **Definition**: Missing values occur when data entries are left empty.
- **Techniques**:
	- Removing or imputing missing values.
#### Standardizing Data Formats
- **Issue**: Data from different sources may be in various formats, units, or conventions.
- **Solution**: Use methods to convert and standardize data formats.
#### Data Normalization
- **Purpose**: Bring all numerical data into a similar range for meaningful comparison.
- **Techniques**: Centering and scaling data values.
#### Data Binning
- **Purpose**: Create larger categories from numerical values for easier comparison between groups.
- **Technique**: Dividing data into bins.
#### Handling Categorical Variables
- **Issue**: Categorical values need to be converted to numerical values for statistical modeling.
- **Solution**: Label encoding and one-hot encoding.
#### Manipulating Data Frames in Python
In Python, we usually perform operations along columns. Each row represents a sample (e.g., a different used car in the database). Here’s a quick overview of basic data manipulation:
- **Accessing Columns**: Columns can be accessed using their names. For example, `df['symboling']` or `df['body_style']`.
- **Pandas Series**: Each column is a Pandas Series, a one-dimensional array-like object.
- **Example Operation**: Adding a value to each entry in a column.
```python
df['symboling'] = df['symboling'] + 1
```

These techniques ensure your data is clean, standardized, and ready for meaningful analysis and modeling.
___

### 1. Handling Missing Values in Data Pre-processing
Missing values are a common issue in datasets and occur when no data value is stored for a feature in a particular observation. These can appear as question marks, N/A, zeros, or blank cells. Effective handling of missing values is essential for accurate data analysis. Here are some strategies and techniques to deal with missing values:
#### Identification of Missing Values
- **Common Representations**: NaN, ?, N/A, 0, or blank cells.
- **Example**: The `normalized losses` feature has missing values represented as **NaN**.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ST5NUKYN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs3llUMZDxx8RQOxmkNCiZB7vlccoOlz0cwCr2LXkRBwIgeeZqz0a4CcqXrw75JQEu2yPxdjh6wtIUs0gwM7orNxoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDJBLCthgSb5zLuhkCrcAxZK8bLDOaqoSC7uXVevdZMnIGZUuMBV0iHoPad6sye0dk9J7y3ncC7pMISBjAuYRTbwfPOdlv7CNoSevGmrh78Va8ZiHxDQ83BD5nq%2B3QeJ880h180dPHf1F8RKA0QC%2FLLvoT2FXjgA0xVlnAsSYoP7wDZvHXJAEFjNyawMI%2FEruHbgw4jnhSYTj6wWjgVuWfyI4xdyGpCuF9BpqvNAWfxj3h01Zbb%2Bh7MEgqxqfAbN0LOHvkp6I2M1RU%2BqIKRet1NLohx7zBjcYfyqS5CfZfn701jtSsICQGZtcyZOj8k%2F0rq7NnGtiUTMPrcrMdyYd0N3HiKLnM2rIzNStXdqhNdjdwjFaYEaEKPoJltvHAVwvgIglDLBG%2B3O1qA%2Fpljht9RwM6VGFno6vyT%2FPrXq6sbQz67qy0N7yKzrsdWTTKxfdFxH3kZasp%2FkVHShBORuf2yqHzWgRuc%2FI6sIDXv38LjFeR%2FOFkQyhYhN1I2QKRCvwb3Erbk4taAbkopqYbWjbxOPBmfbwZ%2BdzH0D5X3W8%2FFO77LV9VGz%2FgK2UzT26%2BoCRUJjJnPgt2DON4X7Iyb3zzLRcO7UCRtMpoJfrCuRaRhGc0LqmWyMSLn00BbNmxHuumOCOo14zzViM2t4MMnG%2BLwGOqUBnaPup9Va6IEkdCIXM7MRjIOrO9mN4GlCdqoLeGAP2JMkfu3QQClKBH%2B1AzkaduZjoM14xw40gLZBYRdsVc8bwzVRuhHEH7S0sPqgABHTmCIrc880EjP4vCMwItFbPkieU23QQh1Ry5RMoeQMgyUrb%2FPVr1pTHr9TnDhqLNTR8Lmeh2Ms2N0hCfUz0tmFP7%2FF4wnIllq1Q6btrown4Wnw3FnHpolK&X-Amz-Signature=f359783da618ddf054476ad1647c6dd12a9c245d123a64e2234bf78fbbf1f0ed&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6UHTEFT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCYIevb9keSf3PTfRN1QMAMkoZEgL5q0b5SIx5zrd4SLgIhAKMJYz6Nm1KL73E0xf%2Brcs%2FF8mXr4IOD29AJyCdJhyLvKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwk4tCGN33Ux9tQxwUq3AO7Np7RqK25rYb%2FI9D1qKyYM%2B2IQI2521cSBkwEIMO3smxir4I7bfB%2FUvCuyTG0KIFg95Ny0vFC3RdezKyBuUV2aVVkKtkm6nfLxGjiq4tqXTxrQTUYsSqbTmuGJxBpC1i54s931Cb%2BQhkS2iyDVc%2FoCdQ5fGA4eFtNFsOrWYk3m%2BSBQTqJunBKbmZxR%2FfOo7TBJE7AaEeW5MxzzwrweniBFOVa6OfvZJikxSrt3qFoN%2Bg6tAbeUJ%2FAZ23w3iUxYrZie%2Fi6XXfjke%2B39sX05ngK11MZ6KHDm86ddHGayFfK26HES2Mx4A%2Fd%2FHVSYDexrcfzj6vJK0MzTKYnTMO5u2fr5Y5gkA48YT5pKXUd4ULHj9qlh2Ac%2BfRI4CvA%2Fndaen7OQ3AGGjW6Q8FLyhrRGJGugbQQ4%2Fppjn1YgCmFCnXxV6WsyTasoVQzrPOXaaJsB5E%2BK3NZTrObB2F67wvXYrEptBPSwvCH6oFjXmJfzjkxpa94PSj%2FqcJYBzTNjVcu8FhCjNnTHhenlfdS41k7ybcGp7DwDgQoI23WszfMwOFjSItHD%2BW5u4TebQ57zh4CG0KTLx8Wk2MjnG0TQkZH%2Bw07CypFuCF59uVNx1kzluwE7bJdsSKBKgwxJj%2BmYDCgx%2Fi8BjqkAfrBlpkMhts%2FYzkHDdBZt%2FWs5KPvZfgt3KDoF13ivhDLbdgsd5pjXcuU5Txtjh8Fm%2FaHntCopQ3rVuMkpE42JZH4YCou7rD9ISFGve1ra877hw9HK9C%2Bah%2F%2FOWlJMsjWKl2GTPB%2FEtwC%2BSVqoy%2BYBFv%2FWs4cRSxJhLYx44zdp6%2BzWJ9C6ufQ0L2mTeos3s6JFx61K0kdD8c%2FFuqBl9x9843ADBni&X-Amz-Signature=2f3d5cd4dfca405d0e9f6626393ebcf02ba05cc8fac216eded7523b5899683e9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWLISNLF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEYLqwfHhIf4jX5HDtQRaGPR%2F149d87bItVQhdlYII3FAiEA%2FUlTR886K1j%2B7Ugt1Fx%2B%2FqeuuNZDrQICaRpctIHda78qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLTRNrX4VuzQM5N5WircAzKF7OgMYblBSiTIteYutB%2F6xLMSHvPKCJrOZDUrOfavZ5hMgRueIv76l6aLkiL7m5AB82XNEyvx0oMZ8I9FtOsBJA1Hbg%2FTbZvquAYJYkgzePRGDPmxIHIYx5gTDgFS8CihlXE7OBQXrQCH9BzYTsAK3JwslGbewEmdQkE5a9yc2Al4FVwD6F9ehfm%2FG3i9%2FmcBFBiAEw65FajJMeXujqoXaAYnASxSRMKcDG%2FUZsZKiosvJbAZBPvhmm6R2K1y2c0D0qqhwT7h%2BS%2FHg9CDCJh13FySxnzRWJQdDC2IviuBBGGiES5eBSDKvlK15KDW9b8YS6CLL9aZQ%2BCTQtZ77MpMr4Paf2VK8bsgQP950rmir4z3Wc0MVzx6cUntSj5jYsUSeRgrci0x9S8RTE2L3AaJMAvF%2F5bBVSkARUF%2FDnnK38NzDa23x7eDLL0HY%2BuPvwGbC%2FMJA%2BH%2FSVXCTKB6eReKwaiXkVbj7kCgipWH9E5ETBK0kRr274DZjE91GmNefjBoAok1q1MtrqGsNEorzNF56AUP3Fe7fDlj1YfiuKHxm%2Ftz7sPQ6ws7nWhnpBKJkP5MNs8%2FNYBUz1GtOR99jvVSudN3ut31ONDkgibgb3lLFSA4Aonii5WwQCb%2BMK3G%2BLwGOqUB0kQf%2BHf3yJROkbrUFomHxeK2JR1wla3OhJ2ivvHP1abc8Qu7WIGRtzi9TBp0sMmu20FYVrB%2BpFtnwl6NBRK%2Fs5%2FFCDh31n5UK6ktdJ2MNW5DXHhTdAbv50DF65J%2Fn0XwMlchK5HVXnBT16UOzQB8Ax6vfW7%2F%2BUXsu0OARWWoxcHpDt5ACdHnpQAAYmJT0ChwrXdXmh0QCUs2N8K9JJ9dKNmiU%2Bm%2F&X-Amz-Signature=67802c93632b525cc6c1be0a25c17ac4e3d79098a9c62724fdac60f8b7e2c877&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Pandas Method**:
```python
mean_value = df['normalized_losses'].mean()
df['normalized_losses'].replace(np.nan, mean_value, inplace=True)
```
	- **Other Techniques**:
		- Use group-specific averages or other statistical methods to impute missing values.
		- Example: Replace missing values based on the average within a subgroup of data.
4. **Leaving Missing Data**:
	- In some cases, it might be beneficial to retain missing values for specific analysis needs.
#### Practical Implementation in Python
5. **Dropping Missing Values**:
	- Drop rows with missing values in the `price` column:
```python
df.dropna(subset=['price'], axis=0, inplace=True)
```
6. **Replacing Missing Values**:
	- Calculate the mean of a column and replace **NaN**s:
```python
mean_value = df['normalized_losses'].mean()
df['normalized_losses'].replace(np.nan, mean_value, inplace=True)
```
#### Conclusion
Handling missing values effectively is crucial for ensuring the accuracy and reliability of data analysis. The methods to handle missing values can vary based on the nature of the data and the analysis requirements. Using techniques like removing, replacing, or even retaining missing values with the right approach can significantly improve the quality of your data and the insights derived from it.
___

### 2. Handling Data with Different Formats, Units, and Conventions
Data collected from various sources often comes in different formats, units, and conventions. Data formatting is essential for ensuring consistency and facilitating meaningful comparisons. Let's explore how to address these issues using Pandas.
#### Importance of Data Formatting
- **Consistency**: Ensures that data is standardized for analysis.
- **Clarity**: Makes data easily understandable.
- **Examples**: Representing "New York City" consistently as "NY" or converting measurement units for uniformity.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CIWIBEX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFUJbjwAlFd6moUpLFVIAdJLLmvYZXXCSXBbxoKO30VAiEA%2BshZs3WCLAXyWeyB%2FCyXdnxUUDlMmF84doSYz77N1wEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLg%2BrD7bnbim6Mfd2ircA5m%2FAJbPWDrSzbqr4QXbE1upPwqD92wY2HqpeP%2BnLQKYSuU05e5iioQLeaYEUPsk%2FfSL18hZx%2BPh4AVdWBGpTPvU6uZv%2FMHwLcxOCmiSqNkDrYWHKAj3iCzgZtUyS8Uaxhg6xw08RcYJe8Gi9RReE5It%2B5GnL8ZG4Qo1qWNXeIOP8TPYBxbXLwTDJ0puaAPNTuy9vmhRdZ71FTt3ApAC4IZlHa1PSIXiCcMRjHPqT7h%2B6h7peZ4ZunymuEW7n0q73o7rcuqZMI%2B1NVtNiZGHSfjOJSKf2kJ0argxDHOtPPOM1whPrEQzxqd4ER179riIVksSjQmrOOWk5iabtof48bY0vb5frwSNudw3pxgB71sjhboiBZf9d0Dnp8Jecc9w4nCfnh11lsi8yIQ3j3UFXrOWlXhaX0uuKQ%2F7S6hpyHArU2AG5skkBMXfKvyhxWlr6%2BDM6dMz9CDtGCTvP7VWt8oPRMVTcUEzrm1%2FsM0vwYZFDNvqPwndHkUqTMrogFRniGug%2BCgtNN1Qe%2Bzz1F%2BG9A57stp5YJvkb%2F7BTWrglr1BBAILCHdpbrqEdNbwQ3ZThTNwDCI%2FH8YNqbxSnC9gnjYw3ZxzrehKdDDIgMUgjM1046kqFIETywFjL5hKMIDC%2BLwGOqUBUOyxaFBSHVRbSeY5SoUx80qBXhaXH0%2FWqxv5Aqh4oo9DmOREKZdxryE%2FuD6ogg8iWLtK1EW8M%2BUKVrQkUeMqNb68lM2sa%2BKqXn7NqDoed23xvXOGWP%2BkZbQ%2BKvKLbjlVkCiz%2BNmOWtT106RKUjy0ZI1CqIDe2iA7q9r%2BVw%2BQWtRYXNjh4LGaMZYmJC6NY0LV1PevdPTke7RcZL5Zq2WJsPc8ZEGP&X-Amz-Signature=6c241f6b55ed48d74941b33a87a01b02b9d0df90a736fba922aad5c012b8d273&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Common Issues and Solutions
7. **Inconsistent Naming Conventions**:
	- **Example**: Different representations of "New York City" such as "N.Y.", "Ny", "NY", "New York".
	- **Solution**: Standardize these entries to a single format for analysis.
	- **Pandas Method**:
```python
df['city'] = df['city'].replace({'N.Y.': 'NY', 'Ny': 'NY', 'New York': 'NY'})
```
8. **Different Measurement Units**:
	- **Example**: Converting miles per gallon (mpg) to liters per 100 kilometers (L/100km).
		- **Conversion Formula**: `235 / mpg`
	- **Implementation in Python**:
```python
df['city-mpg'] = 235 / df['city-mpg']
df.rename(columns={'city-mpg': 'city-L/100km'}, inplace=True))
```
9. **Incorrect Data Types**:
	- **Example**: A numeric column imported as a string (object) type.
	- **Identifying Data Types**: Use `dataframe.dtypes()` to check data types.
	- **Converting Data Types**: Use `dataframe.astype()` to change data types.
	- **Implementation in Python**:
```python
df['price'] = df['price'].astype('int')
```
#### Practical Implementation
10. **Standardizing Entries**:
	- **Scenario**: Different representations of "New York City".
	- **Code Example**:
```python
df['city'] = df['city'].replace({'N.Y.': 'NY', 'Ny': 'NY', 'New York': 'NY'})
```
11. **Converting Units**:
	- **Scenario**: Convert `city-mpg` to `city-L/100km`.
	- **Code Example**:
```python
df['city-mpg'] = 235 / df['city-mpg']
df.rename(columns={'city-mpg': 'city-L/100km'}, inplace=True))
```
12. **Fixing Data Types**:
	- **Scenario**: Convert the `price` column from string to integer.
	- **Code Example**:
```python
df['price'] = df['price'].astype('int')
```
#### Conclusion
Data formatting is a crucial step in data pre-processing, ensuring consistency and accuracy in data analysis. Using Pandas, you can standardize naming conventions, convert measurement units, and correct data types efficiently. These practices help in preparing the data for more meaningful and accurate analysis.
By addressing these common data issues, you can enhance the quality and reliability of your datasets, leading to better insights and decisions.
___

### 3. Data Normalization
Data normalization is an essential preprocessing technique used to standardize the range of independent variables or features of data. This ensures that each feature contributes equally to the analysis and is crucial for computational efficiency and fair comparison between variables.
#### Why Normalize Data?
13. **Consistency in Range**:
	- Features like length, width, and height might have different ranges (e.g., length: 150-250, width/height: 50-100).
	- Normalizing ensures consistent ranges, facilitating easier statistical analysis.
14. **Fair Comparison**:
	- Different features might have varying impacts due to their range differences (e.g., age: 0-100, income: 0-20,000).
	- Normalization ensures each feature has an equal influence on the model.
15. **Computational Efficiency**:
	- Prevents features with larger ranges from dominating the model (e.g., in linear regression, larger value ranges might bias the model).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6J5BVLB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAlumyRRSN06kLWrGhKhJtb4jF%2FPOBQr4EVHMvzNklCCAiEA6Z63OXpfNpSk9HFBHvbs%2BlzcadFJroHcGzwmEQWJwGYqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJvuBfZziRESmPfugSrcA%2Fz5WZaKS1%2Be79jIXgiqvETEsTlTRYZB6hs%2Bz1mYKNlzqbiUmHKd48N4rwD2p8jZCyOgeQNO2td2VvCdlRjL4tgIpzmO0rr1TUal1jqJyNlJHfkVtfiYOj9xEAs6eZFgUeU6s6VgkRuHqM6eQkYFvYkwhuXLOBrokMbOsN5Y1%2B2u%2Bv4xNjKMake6FSQKHUtLx%2Blh8Kg%2FnqEe5hoHzphRikEXA%2FWANcLJg1mJpU0hFdli7TMf0z2%2B8Tq0%2B3JKIwWoc%2BWTMvduKmiiuwP9xgU7Kxi6KJZwZEY2Gvvxa1W9DvwM3FzITylctD3u%2FPBDm0aDezDmj%2FEohOLh16spPZfE0aSGPOKm7h7VgPzexnfQXp%2FFKUUxllSVo2xvSmJSRYuUbPOLVlZ73jfVtyIi1uYCAbt4Az62%2F51f92qYOMZnU3pc7gW5zUKPXPWz8EM%2B75iMiUAgi0EqmhUG7VTa4eZo%2BxyoxK9N0ZNtr%2FhCmC7UsojHPWjvxRtej776S%2F1xN1zGKP4PocLhbqojA3ACPNrqYHgqRkLbARerrbE1Ir1Bi9HLv6oEulw3fqdtiVCsigdb0KFsVYzjVsxXnDGUcfHO4AMNEwiXNqVoivPgdj8UQ22rIy5WFMwt0KuTeodZMPrK%2BLwGOqUBdzloZu%2FOCYY%2BggLmdd5lJo%2FGBFTQ61bb8Vz3eoAQzVN1Ii6TwQ0mdkaN58CZXss6d2C7EELJbkQUhvveP2LmsPuY7H9SlaDzEBW5TavVn%2BJgHGmTpoJpHvmlX80jVRa0TsWxN3dHd9uf87FyO77GmMVRQAV9odsqTJzyS8UgViLqNQ2dTdYWZ4fCYole8b4bvqufxoJxw06Oqdc7J1mp%2FMQeMykS&X-Amz-Signature=d93aac4da102c040d1a58f3ff999a26b93b9022e83b6de91407f2ba3b9ad2586&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T26EVAM7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFbUEtoNLqtRiCYEEYf5Aymsj2ubV4sgpdqby%2B7GKCfEAiEA6JY8s3PBweUmrd6Xo16x5Kts9IT0r0JWOZLw%2BgFpkZoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGoBECWqAFE7L3%2Bc8CrcA6qDuBHvQEEeFYIikaGcRyoJUlC3jeejwxsNoYiVz4%2F0BQ%2FA7s0aAIo21YjXJqNbKN3qdd80kRYK%2B2SOPwL7%2FPtRcbLKIMoWl1lL89VlHdLN54VsHm%2F3%2FzXMrq92zHpZmxGTu5P4eqXwfZuAp3Vh5v8%2FgT7PNoWluYZF%2F4t8RsBvzO5TE0%2FsLHvjZaaJ53Nwp4pvIG93HEpMddIdq5NUMgrq8rEnI1kTd3iLSmq3nRfpQ%2FUSU5gfSrg62LFjWNkilmNE6olNQrx723nTtPun3JdpRXY9pY75lTe50Ufr%2BeLvJtURXrw9%2BU8wF1bBRkacJnkhyA7awRwEKiKvTKkR0GQjPWhp7J6Nfxsmc4gZnE20LzsdMYTGRKpzUP8%2BgtQ%2BvJuhD3WEPfjMHFc6%2BfCw6dCpAC9Ipt%2Fi%2Fc2ztI0Pc0Uty4cG5jikcm9n5OXLj1KE0BKw%2FUcP3luewxl8CunHLNyoB6CvmaAuLXxjQec8180yyjP7SCmOUx15NV1GifNf6WZ6vzhJUx9sIklhQhXQH8AptvuRlMTvZiaOgJfJoAggQ4jcVhkKjrDb4i0SoWiDbiDSIGT3XHd2unuxxqtFR151nO7m498r1uakgu8VI55C57StajoF7SQZXQavMKDH%2BLwGOqUBqsWcyhqCwy6vZfBLoyf6a%2FJW0zhaG7WGGHJpilSGbs%2BrZtw9Bu7TQLTSGbW%2BKyI7%2FOdXx5kuYlfN8no1G9trTfutLlK9NVnaKbDkf0alp8nLKRLLLwkXQmW4nS1ftuZ%2BBxoI%2BqYmXSI0nl6qaF04jl3SBET6R56oVZ%2BcFq3TVHQ6tJiKMcAOBslaPJMOoR%2FbST%2B1L%2FW3%2Ba07oPl%2FRSX%2FSiPoFBhu&X-Amz-Signature=d6a9d65404818571f5957c2c479c7235a3ac29287da6507ff81153b9cd732806&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVLNSMDO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEZwCWbVQ5GMEWkqlMsl6AeUHWHTtX%2FvwEyQ1N8wUf2wIgI6JBpPJ%2FR7x5slBCr3eZMC2hqWaXW36hTr2TRTFpr%2FIqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDJFYjPs2G24GJ00OSrcA7Ahse3wpuqIZrE0fBIe0eFok%2BxhccUfGpfoOthG8l71p4SqFefyuwskLFOYHk6%2FitSCrGcvKUGb%2BRGYiU6GL0LaEldWmZtEBjh8NGVmlJ5YofcJ4L08Ov%2FqlHYEzsN%2BOjuTHrfKrhgVxuK2bXBgP3A3%2B%2BYLIcRaVBpbx5bno8oAj5GimT7lRcdvv3tIM4UKjc0eXryRAyRNE1rXAgJvWm%2BjZGW0ixo0ESlYrOvUkyvZz5v%2BfvQqiFYfZnvaZ31%2FY%2B6g32Os5%2FXZxvhNo4mSbeJjtR2S4LNLyIIg5IrsiVcQuP4yuBrA73sZQYXUHCzbltjz2S3yTqLRGw8mawNe69mzExUedWfbq71tmzFKTMBmc67wG%2Fdlgr0UZubtdSZx40fm%2Bz7NXKo9YqRHxwrJjLORkM1UkZAHzm3P9rRVXtlGCz3JJTtIb8jR3PDTmGthkDjKUe7mEaBpsbnDKRfgRN7jqxNkbQu7fc5bDmSwNggc8cTCKpELiBT2vGWZKR7fjLCJy4rZ2rTQwpfw7FxBnmZ%2FvuNJW09vwSXsnUr4jGQODU84%2FYEJNJ39KcYvl6HW0XxPozVDJ8slNSL87GhLbgEKNLhDG0i4HmOTcGjW5Hixij4oNU%2B0mekFCkoyMNLK%2BLwGOqUBl8NMxteGSDH2wUvzwJ7C31JUatddot6iNzaUndIyNTIir4PEM6mCueiTgEA6z5t1NxizUAPL1eBDLolU2jBR7v0X2lflwhoJ3tdv9OGxjzG23mvh4%2BthPq8ExtUSGjIcf0gp3rZXPeiDt6o9jJdqoVihVfqDPzYAoh6omi0ptYkOJxg0asYFDYED9o97xalMNrG4hINLoAHOlXYjU2Kj4z7lgMlX&X-Amz-Signature=3001e36f0f1e00f908ff9bb75ef4317587c22da3e2709d1705d002bbe65fb7ee&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMQF5KAC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeZWo5f2vroMHRcaAwKmi2N3YYEz%2FFenfcRTtnUdf1IwIhAKgJ0aobB8j6OGdmNtksf%2BTVumUFaVIKLWUFhOO6k2byKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy56Z%2BXi0H4VJUZeUwq3AMV4Lo4ZAa0aKjz4tRsrLUynkHfTqqosm80BOivFifKLn5Eoh29JUSwrdBx%2Buh3ub%2BnXDbFzF1hc7hIMqAvV1Hj53e%2FgjSr5KAbcygpLRvIr5mzGC%2B4VzVvAZ2P532feAO5%2Fmml8Y8nORZMQ2W54s6cb%2BkR6MC7DkRIbS5RkbxnVKSyxfK3mpPgzTlRlYKUjqjh1HTVIBnNe1ugYdI7i1S1kGgMXPwEL1jKUrvfJ5wo67o07LsitRZ31Iqd%2BOfQjGrA86ZkAmD01TDOoVPlO6PNyIadoP%2FYlsKN1ao86ttexqf9x%2BHOrWQnpIHrvvqLwfEj05dcnEGeQToYuC8V15ydFrrT7Q96z3jXYBY6tVA4uTc25ZYuet3%2BIx3d6oRa3pkNc%2B2FGAuvJO%2FXINapAfbFCV5mgnYFOCpKp5Q46mAxN9oAFd95H%2FNydsg2LXpJcawlNo8xwViK1RP%2BmF9cKVOW1tsmoP%2F2cyl2HJ%2F4EFwSWfmzRV0%2FnQok10xBshbPcLDQxIoveYC8NxZfkpMedR%2FNmRgd6U2KWDt6WPMXSHXOsn1WMTp%2BGx%2F09Gn1yvg61LDBcdByOZf6%2FQGf6KkUj960MLzKEjh2HmATj03pW7qzlpSepC38QADJvikGBjCiyvi8BjqkASUjXhiCLLf2LR6%2BNg00zkp9jHa%2Bog90tLL6CZh%2B%2F9dLLXTxgdl46e601tpXbDImm1TvqO%2FK%2FDOA2Jg4jCvHhFLeUbmnDpnqbTjIGOMEoMkhW4PT7rvQ9Fl33Kc3AUxlpLhVFtrcdRzIUjj0o7rcRqNn%2BOfJtfdKaljRZdYgWE3FwdVsbFqYb3RyzcZF1HLC4QxLImAJkDGGYhexzUrOkW1YaKV1&X-Amz-Signature=e2ec5457f7c2fc55903a2d306c252c375fb3278a0787df36db2e15dcf174015c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example Implementation in Python
Given a dataset containing a feature `length`:
19. **Simple Feature Scaling**:
```python
df['length'] = df['length'] / df['length'].max()
```
20. **Min-Max Scaling**:
```python
df['length'] = (df['length'] - df['length'].min() /
				       (df['length'].max() - df['length'].min())
```
21. **Z-Score Normalization**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
#### Conclusion
Normalization is a crucial step in preparing your data for analysis, ensuring all features contribute equally and improving the performance of your models.
___

### 4. Data Binning
Binning is a data preprocessing technique where numerical values are grouped into bins or categories. This method can enhance the accuracy of predictive models and provide a better understanding of data distribution.
**Why Bin Data?**
22. **Improves Model Accuracy**: Grouping values can sometimes enhance the performance of predictive models.
23. **Simplifies Analysis**: Reducing the number of unique values can make data analysis more manageable and insightful.
**Example**:
- **Age Binning**: Grouping ages into bins like 0-5, 6-10, 11-15, etc.
- **Price Binning**: Categorizing car prices into low, medium, and high.
**Application on Car Price Data**:
- **Range**: The price ranges from $5,188 to $45,400 with 201 unique values.
- **Binning**: We categorize prices into three bins: low price, medium price, and high price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6J5BVLB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAlumyRRSN06kLWrGhKhJtb4jF%2FPOBQr4EVHMvzNklCCAiEA6Z63OXpfNpSk9HFBHvbs%2BlzcadFJroHcGzwmEQWJwGYqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJvuBfZziRESmPfugSrcA%2Fz5WZaKS1%2Be79jIXgiqvETEsTlTRYZB6hs%2Bz1mYKNlzqbiUmHKd48N4rwD2p8jZCyOgeQNO2td2VvCdlRjL4tgIpzmO0rr1TUal1jqJyNlJHfkVtfiYOj9xEAs6eZFgUeU6s6VgkRuHqM6eQkYFvYkwhuXLOBrokMbOsN5Y1%2B2u%2Bv4xNjKMake6FSQKHUtLx%2Blh8Kg%2FnqEe5hoHzphRikEXA%2FWANcLJg1mJpU0hFdli7TMf0z2%2B8Tq0%2B3JKIwWoc%2BWTMvduKmiiuwP9xgU7Kxi6KJZwZEY2Gvvxa1W9DvwM3FzITylctD3u%2FPBDm0aDezDmj%2FEohOLh16spPZfE0aSGPOKm7h7VgPzexnfQXp%2FFKUUxllSVo2xvSmJSRYuUbPOLVlZ73jfVtyIi1uYCAbt4Az62%2F51f92qYOMZnU3pc7gW5zUKPXPWz8EM%2B75iMiUAgi0EqmhUG7VTa4eZo%2BxyoxK9N0ZNtr%2FhCmC7UsojHPWjvxRtej776S%2F1xN1zGKP4PocLhbqojA3ACPNrqYHgqRkLbARerrbE1Ir1Bi9HLv6oEulw3fqdtiVCsigdb0KFsVYzjVsxXnDGUcfHO4AMNEwiXNqVoivPgdj8UQ22rIy5WFMwt0KuTeodZMPrK%2BLwGOqUBdzloZu%2FOCYY%2BggLmdd5lJo%2FGBFTQ61bb8Vz3eoAQzVN1Ii6TwQ0mdkaN58CZXss6d2C7EELJbkQUhvveP2LmsPuY7H9SlaDzEBW5TavVn%2BJgHGmTpoJpHvmlX80jVRa0TsWxN3dHd9uf87FyO77GmMVRQAV9odsqTJzyS8UgViLqNQ2dTdYWZ4fCYole8b4bvqufxoJxw06Oqdc7J1mp%2FMQeMykS&X-Amz-Signature=c22985459a4b2b5665294a4c2bb07703e9bd13c13e57fdc01e9f6519b1b6524d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Steps to Implement Binning in Python**:
24. **Determine Bin Dividers**:
	- Use NumPy's `linspace` function to create equally spaced bin dividers.
```python
import numpy as np
bins = np.linspace(min(df['price']), max(df['price']), 4)
```
25. **Create Bin Labels**:
	- Define the names of the bins.
```python
group_names = ['Low', 'Medium', 'High']
```
26. **Apply Binning**:
	- Use Pandas' `cut` function to bin the data.
```python
df['price_binned'] = pd.cut(df['price'],bins,labels=group_names,include_lowest=True)
```
27. **Visualize Binned Data**:
	- Use histograms to visualize the distribution of the binned data.
```python
import matplotlib.pyplot as plt
plt.hist(df['price_binned'], bins=3, edgecolor='k')
plt.xlabel('Price Bins')
plt.ylabel('Number of Cars')
plt.title('Histogram of Binned Car Prices')
plt.show()
```
#### Example Code:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
df = pd.DataFrame({'price': [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000]})

# Binning
bins = np.linspace(min(df['price']), max(df['price']), 4)
group_names = ['Low', 'Medium', 'High']
df['price_binned'] = pd.cut(df['price'], bins, labels=group_names, include_lowest=True)

# Visualization
plt.hist(df['price_binned'], bins=3, edgecolor='k')
plt.xlabel('Price Bins')
plt.ylabel('Number of Cars')
plt.title('Histogram of Binned Car Prices')
plt.show()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMZO2WIL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHh6B3NlgiWxIKEVymCMdmLG4WB6%2FWdrjMNcnA%2Fjc4sGAiEAtS2LeQ%2BNkGTjDpT%2BHPvaCO1QBgCrAc22y9wI20%2BMIUQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNm0dt03Jf%2BGF3qTCSrcA10b55vxi1eo%2BHxDe%2BgFl359b5dAF8NzrTJD4%2FcThxzWeK8wVIMugoY9mPmbC5Swec%2Fz%2BCGXpTjpuAv5Wjri0DG%2B8DheFf38B9uAXXWmjpQbyDjOhHmg53vyA5b2DUETV%2F8W7%2FhbexzsJBUwB3Ubd%2BytzlHZqWNB7LbCwFQHROiumj88j4HzhO6rdoyWbKklq05hsgnxX0Luek3q7s6tkk1Fj8IgjirMXiB3w0KMnHWR3XNPcvGCaq80xIjJR5FMhWiJEyAufCaEYaKmXXicfffZ%2BWoC%2BpdS8bMB65GqfWxL7DlS5L7teqMak0q%2B4x4DaxxYAul%2F27ZwptHP7cdaZFousw5dhZwzwO9LdfgvpKA05IZ%2FLM1SadvYdwI9AntjstHShy1as996yedA%2BuqdSqRL6vQIJ1kgHylKHpeAGwYJb4qjOPOoEzqcX2VEhYmtjHgjSPuHa9ybuwa65IRm5xFh%2F426FcQM4erNrv7mIMIjCrE128fMUm5i2HLIzNYafktsE1Tzl8TdbfZCec0FkdiuSH5zjRCW003ykC%2BY2%2FlKVGFcPli%2FqlPaPFXo0VCRBb%2FoMY2tKrYQdpjYfdskKfEokSmbSYJMXhxQm8xb0LsLyjAdykLRcYVCnJIOMPTH%2BLwGOqUBlGc595MffQJ8D9Mwp3bnrIDohbjD%2Fwn5j85wivOPmBcn63PMtTvA2ZzcZQ6xWxKUrYFI%2Fq2y%2B9i3ejtdJgTgn%2BVsR3zIPv0ky%2FpdvCIredh4wmFVAWNP5pr%2F45KqTFUi2Gqyj3OWJrADbt9VJDgq8M4LiCTALRqkkGNiLGFv%2BvrQfSh6AgCutSKkz25wL75FWc4SWS3WAxRmwcCpLqw1jQov2Vq4&X-Amz-Signature=bead990806cf07fee8848569c7687f95f9adaa179623fc7142543e6f19846621&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Conclusion
Binning is a powerful technique for simplifying data analysis and improving model performance. By categorizing continuous variables into discrete bins, we can gain clearer insights and more effectively leverage statistical methods.
___

### 5. Transforming Categorical Variables into Quantitative Variables
In data preprocessing, it's essential to convert categorical variables into a numeric format that statistical models can process. This process is often referred to as **one-hot encoding**.
#### Why Transform Categorical Variables?
- **Statistical Models Requirement**: Most models require numerical input.
- **Improved Analysis**: Converting strings to numbers allows for better analysis and model training.
#### Example: Fuel Type in Car Dataset
- **Categorical Variable**: The fuel type feature has values like "gas" and "diesel".
- **Goal**: Convert "gas" and "diesel" into numerical values for model training.
#### One-Hot Encoding
One-hot encoding involves creating new binary columns (features) for each unique category in the original feature. Each row is marked with a 1 or 0, indicating the presence or absence of the category.
**Steps**:
28. **Identify Unique Categories**: For the fuel type feature, identify unique values like "gas" and "diesel".
29. **Create Binary Columns**: Create new columns for each unique category.
30. **Assign Binary Values**: Set the value to 1 if the category is present, otherwise 0.
**Example**:
- **Original Data**:
	- Car A: gas
	- Car B: diesel
	- Car C: gas
- **One-Hot Encoded Data**:
	- Car A: gas = 1, diesel = 0
	- Car B: gas = 0, diesel = 1
	- Car C: gas = 1, diesel = 0
#### Implementing One-Hot Encoding in Python
Use the `pd.get_dummies` method from the Pandas library to perform one-hot encoding.
**Example Code**:
```python
import pandas as pd

# Sample data
df = pd.DataFrame({'fuel': ['gas', 'diesel', 'gas']})

# One-hot encoding
dummy_variable = pd.get_dummies(df['fuel'])

# Combine with original dataframe
df = pd.concat([df, dummy_variable], axis=1)

print(df)
```
**Output**:
```plain text
     fuel  diesel  gas
0     gas       0    1
1  diesel       1    0
2     gas       0    1
```

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMZO2WIL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHh6B3NlgiWxIKEVymCMdmLG4WB6%2FWdrjMNcnA%2Fjc4sGAiEAtS2LeQ%2BNkGTjDpT%2BHPvaCO1QBgCrAc22y9wI20%2BMIUQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNm0dt03Jf%2BGF3qTCSrcA10b55vxi1eo%2BHxDe%2BgFl359b5dAF8NzrTJD4%2FcThxzWeK8wVIMugoY9mPmbC5Swec%2Fz%2BCGXpTjpuAv5Wjri0DG%2B8DheFf38B9uAXXWmjpQbyDjOhHmg53vyA5b2DUETV%2F8W7%2FhbexzsJBUwB3Ubd%2BytzlHZqWNB7LbCwFQHROiumj88j4HzhO6rdoyWbKklq05hsgnxX0Luek3q7s6tkk1Fj8IgjirMXiB3w0KMnHWR3XNPcvGCaq80xIjJR5FMhWiJEyAufCaEYaKmXXicfffZ%2BWoC%2BpdS8bMB65GqfWxL7DlS5L7teqMak0q%2B4x4DaxxYAul%2F27ZwptHP7cdaZFousw5dhZwzwO9LdfgvpKA05IZ%2FLM1SadvYdwI9AntjstHShy1as996yedA%2BuqdSqRL6vQIJ1kgHylKHpeAGwYJb4qjOPOoEzqcX2VEhYmtjHgjSPuHa9ybuwa65IRm5xFh%2F426FcQM4erNrv7mIMIjCrE128fMUm5i2HLIzNYafktsE1Tzl8TdbfZCec0FkdiuSH5zjRCW003ykC%2BY2%2FlKVGFcPli%2FqlPaPFXo0VCRBb%2FoMY2tKrYQdpjYfdskKfEokSmbSYJMXhxQm8xb0LsLyjAdykLRcYVCnJIOMPTH%2BLwGOqUBlGc595MffQJ8D9Mwp3bnrIDohbjD%2Fwn5j85wivOPmBcn63PMtTvA2ZzcZQ6xWxKUrYFI%2Fq2y%2B9i3ejtdJgTgn%2BVsR3zIPv0ky%2FpdvCIredh4wmFVAWNP5pr%2F45KqTFUi2Gqyj3OWJrADbt9VJDgq8M4LiCTALRqkkGNiLGFv%2BvrQfSh6AgCutSKkz25wL75FWc4SWS3WAxRmwcCpLqw1jQov2Vq4&X-Amz-Signature=2b2b99b6f95adda26c8eb6778d156878eb8ecf35e8747b6ceccc09049a5ce6df&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Indicator Variable
**What is an indicator variable?**
An indicator variable (or dummy variable) is a numerical variable used to label categories. They are called 'dummies' because the numbers themselves don't have inherent meaning.
**Why use indicator variables?**
You use indicator variables so you can use categorical variables for regression analysis in later modules.
**Example**
The column "fuel-type" has two unique values: "gas" or "diesel". Regression doesn't understand words, only numbers. To use this attribute in regression analysis, you can convert "fuel-type" to indicator variables.
Use the Pandas method 'get_dummies' to assign numerical values to different categories of fuel type.
#### Conclusion
Converting categorical variables into quantitative variables is crucial for statistical analysis and model training. One-hot encoding is a simple yet effective method to achieve this transformation, allowing categorical data to be used in numerical computations.
___
## Cheat Sheet:** Data Wrangling**
### Replace missing data with frequency
Replace missing values with the mode (most frequent value) of the column.
```python
MostFrequentEntry = df['attribute_name'].value_counts().idxmax()
df['attribute_name'].replace(np.nan, MostFrequentEntry, inplace=True)
```
### Replace missing data with mean
Replace missing values with the mean of the column.
```python
AverageValue = df['attribute_name'].astype(data_type).mean(axis=0)
df['attribute_name'].replace(np.nan, AverageValue, inplace=True)
```
### Fix the data types
Convert columns to the specified data type (e.g., int, float, str).
```python
df[['attribute1_name', 'attribute2_name', ...]] = df[['attribute1_name', 'attribute2_name', ...]].astype('data_type')
```
### Data Normalization
Normalize values in a column between 0 and 1.
```python
df['attribute_name'] = df['attribute_name'] / df['attribute_name'].max()
```
### Binning
Group data into bins for better analysis and visualization.
```python
bins = np.linspace(min(df['attribute_name']), max(df['attribute_name']), n)
GroupNames = ['Group1', 'Group2', 'Group3', ...]
df['binned_attribute_name'] = pd.cut(df['attribute_name'], bins, labels=GroupNames, include_lowest=True)
```
### Change column name
Rename a column in the dataframe.
```python
df.rename(columns={'old_name': 'new_name'}, inplace=True)
```
### Indicator Variables
Create dummy variables for categorical data.
```python
dummy_variable = pd.get_dummies(df['attribute_name'])
df = pd.concat([df, dummy_variable], axis=1)
```
___