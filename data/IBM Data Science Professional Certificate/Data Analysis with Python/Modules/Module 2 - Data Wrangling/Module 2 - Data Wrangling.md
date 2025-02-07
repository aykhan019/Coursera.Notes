

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GZTRW5H%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDhBrkpP%2BJlF1qI4I8SyH2zuaqvmFlKPNfNRDFz7r2e%2BQIhANCik%2FqigS%2B07FkAgm2JAexRVuBq%2F5Bz1aPZVhf082pIKv8DCG8QABoMNjM3NDIzMTgzODA1IgwZPeoVtmHURxS4V7Eq3APIxzanBGJOyf0h7QJoZzkz4peA%2FAiTiJm6GeTEL28nEuBlSbarhiBq4NAgY6VdxpLzGLv4M5BdUrj0Pco8I%2BEYIZc44AZUIjDXVXsR7hORyFyyeoJ4lwkduGEfB%2BUvd2V24EsVOpuH8c4R7NQ3KZNMdD47oS9uI24QA0G6wJO8HQVkaOcNKfK4zy3GQ%2B3DpU%2B47ndD6D751bLcTHSUWRHvnD87x9bRsonSxaPqD17mcq7OmbeZmaPTZiDTpKnglL0aOHP8DjJZarOI4wHD%2BeU5CzfkJ1opOyCLAUZvJKH8RclJ467H6lGmiITkgFGTU2h9NLisWWz1MLFgbHk5hZrEnIhOoBr6SVZarPxseDB81OFxKA91VuuBhiBGDXq8KuWF%2FxsnEBrsXxiDioSfNsFtfISsEnMS3ukj3jZgy0prJsmvBGN7A1k%2FWx59pKCHoYkRO8suLUjwUTrWPWquTax0ljWw2XC3tF56V2eghUS1BNrKQPdVOWK91FeeLDBqDcLWDZ3M7tx1gCDeOU9YqMbAElefed%2BjE7ZsQB8X0fAh1%2B%2B2spnWK9w1SKCcSK58HFUGYAwBGcA72A9RdNorGffTKeGTKjBB35JpXumSGqRcPVgf%2BgJa5badylgQlTDQv5a9BjqkAVJs6KO855ruY1QI8wMT651eGrSWfEW9m%2BP9hVDgcHPKPTWUJTM8RIiP6w8ChdKxNXatiWp6ZAquaRjeKsJ7cvYh5gnyMOeKA4nYyIKL87fKbH2cWznoKpm6A1HXmDry%2BkhNfi2TLIChHP1tU8t86zT2O7ExsPLtYzjUr6HDHsoM6wS5w227DB7P0pqLlSVIkkgUBTLzj4rL3dbfpx8ifEoEhMr0&X-Amz-Signature=d1554cdbf87cfc501bd553857879bd3dc376b633e21255f0e5f5cb05fad5edb4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663K2TW5C3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQCW1oM%2BH1FJHbdXoucdOHGFNNcKQ%2B%2BjsIGJoOw%2B13APWwIgTc%2FSqXxiIIRw6CegEP9jSzNvHKsKX40KJqPF%2BEOdpooq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDDwo36UJTO1OL4rQzyrcAzVYv%2BZk51IPBVwhdcpIeZWw544lfH2TcWYcjIkUxGRCHTD6GooQ3KFrXsUKiB8Bxc05PAkr2DjTCX8JyywPk0EMj41APSsxHrGuwPmWfE%2FLKbImbLfxhg0DxHDt4dZmFxKFO1pXWe9%2BPuiYv%2BKRDMyzr2I74fLOaIUzh9iYGsggxg4YrQTne6GtiVdrg6sLexjV28deFU3WWlL4oNMwZ%2FNiFipBAzU6xHdfmkKpNJ8IdNoaWQjkBsv%2B9rbYB1CIIuUuel2XbXwfnkHKNmKK3VSvjtvIx9V%2FScUtq2DM0MIZzDf0gJDL6g9mpgQRJXo4q1Om3veaKpbGhFa4id0JWHdu7dkINBCVeyfyV1eSJh0gk7uEcBAJCo8bvycsTPdNWaMde9iL%2BeVjhsAok5BOQ%2FB78A3deqPoUgw51c2ogNYkTNA69QtUn4U6CY8f9X7p25wagkMmwARWex2J5V9rTAkxmS9lltr6M%2BMiRgc0QeDMfHqPecJpkMLvoylPKr%2B0iH9GvY1frwYwl%2FsVMf7awtNn1orMg0I0mvqZLdO4u0XXJmz6Z%2FCij%2FBQQnqB6tOWia8y9nBWQ8hZD2wOmSgNPOsDT9hhU7sQJRjaPFeHRj4gAAYYlSWIuKln0dr7MM%2B%2Flr0GOqUBbWoqeMzAFq7CmPZBGfx%2FWKKVMEzNSJ0y0A3FqbCZQ7Sm4aainXHuDi0sU4eTUqHK4E5LsOpF94A20c8zWg0IZoYvC5PSQBGSQXqZxLUsDAUTRad5PbkAWbrgk0GEmIsyEHAk%2FcMbOYbwWBuTUmFtPVG9u73s%2FiEoY6hNueS1TncnWxrw%2FyD2OuBewR9zsfMZAW0cW1KG6GDk5nBiBJNRgLBkvO3v&X-Amz-Signature=ed46b3b46f668f963b7c267e3a4566823da3b546bbeb89ea93b80d6fbe54d26f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VQYAFV5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIDgXdqtblO6ZWS79%2FjHQQkIARiZN1c2nWTaAztl24WZ0AiEApq0ERKkLYPGs7Dkwk5d%2Bl8LgaVmiUz0CYfAZhhI4sAAq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDGELBVeZAcPton9%2BPSrcA%2Fv6GopNxZPo6kBvomIMDkpIbgiDbSisU8dQ303XL6elWkm0PKn6H9lbwhejQ%2B%2BN84nDgn6YJlY3MmhJQYDjn9QEPdaKGVLI%2FNPyqnaMoQNyrCVSu0CLZbjSaycnrU3SLbHVNX4l%2BRJ%2FspLhC9mbQTl3IgcBguOiJdOckWPEWc2fAu23Of4NKeP%2BRqFYTCl1hmKICUX52pjW4nsrVtvfPQTg4u7UNc0DPmTeOulBKAnX%2Fj2g4FYJhcezXy1n%2FPxPfP090LFYo09XfkV234tYF%2BqTcUZrE7X7d8tnQo%2F7mNQghBr2V3k6ZT3HBHUHH4Coi0rN1PZYXS3ZY6zqg4c8EeJdbSz0X5vbADtLr8lQdBPTtvsDesyYvAoRCUYPcseuJ75ALNWNQUUOoxXquVv497tVVEl%2FCRZgyEYcOo4BORYxFwgRi9eZT8z6WjWFdO6gxWgb8UNUsBx6tynyDlKSGbw6e%2Fgr4Ba4RokbtnzIFdTD3MHh%2B62GW8lZuZJYuTg%2BjqhdHXKZZS6sJz7npACbFCT%2BMUgvwK%2Fr0tRTqoTaxNZB0pKX1DXDYpUZFKNpk7Vk4Mm%2FGS8nYlrghrBpBhF0HyTxYgdf1mMf0DpqLcpNVFo4SD2pE33hNL300uGQMLW%2Flr0GOqUBg5WEDPlEdVqg%2F0eQtkniAyFBOfMccVc07NQxuYXhrjjl1smz5p1Jf1%2BknbgHp6oxsKPQykgKAKGrRJwGpFasD3YObfKmNxl3AH8KFCHKy8EWEGg734NAKiuTb0TUBaaCAUVl56035esz%2BtFlbVGXDPIItPD%2B3RZewg2VK8YwwtY1S%2BZBQ8UZin3jjFawNHcx%2BFVWLZyZb0Py7nEO9bXNCS1CscEw&X-Amz-Signature=5d8cb9d0b06340ad30118e3b1f793258e120b21772800cdc0e747e4ef04e5e5e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NJXMNMC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIGll74j6uAUmCiGb5CQ53D56IuC47V24TJyTnZ1Jmf6cAiAbf%2BJ4TMajA06hO%2FLHqmFGDPcDDTUGqo7432XSyOikwir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMSS%2Bnnk6pwmLkiq1qKtwDt9lzwnD1AwodRZnkAKlM0Ymgaheua7UHnQbphTwD1K5IWtnZF81W0NrDsLfHqnyfzm2ozE4dsAkDQA24qwicz2iT8feWmNuwjt5EXPUrzbFVFNHjCJA%2FN6jf8g8JxTfU6hGPulxYemEKK%2FXiMAdzLvR8OkmBjqS9%2FWxI3NRw9j4ORdAR7P9GPbdLAzS3PV%2FPU70yXYiQQ8xG1iCUjf%2BnBaTw8btB9HRD1FOxQ4Z%2BQ9pNg3ZFxr6BZg%2FOFanJbdpCJfR%2BbXHNkcCSGV6NTm7w%2FfSkBVekeQt2wQK82fb%2BSKi4%2FZMcpxsPwdWmSsbScKUr1IEuBfBgcTqk9YfVBWlSEBJAXM3oUHr1jJoM2te7olGbzetNsjK0OLm5QrR%2BnRn20HiY%2Bax0CDLJAkivM%2FO4g0SvoDAUxAWQDbLkMQ9jWauaXjRLjLSeou2xXI%2BG0yQMhoPdyvZTO%2B8tohYdiTdygjdt%2Bwjpx7DFZnsMldhCffbvoTwBR2PHnSUcf99Yu5pSEmqjUdReOf2oQ78CeAeDJs5LEaaAkYIpvnnXKWPYpOE8NiTzR6DN2cieGeBTTkt9n7WkWhc2sCYqCNivwZJFgqSYmD%2FThPPa4Ko6u1GLVzGU%2BOmUsw7953hz36IwgL%2BWvQY6pgGNr3gUCBWA0bPX1T%2BRj4jkP6MXQNI3rQvIKwuQcz9ImkKuYprvY%2BpJT7rxaCJDfl4eawoKcEZIB2y%2BWIzlrIRc7azmLGqRcWHV2SE%2BZr%2Fax7t%2BuTtHz2UFMP5tVN52dS7XfSFhfBCBiEg3FGWN8A5nVxoMw13UcT0rAolFAYt%2B%2BXvVtFicnpRcaQT7H%2FeNs9i%2FHLlf%2Brse%2FcDpHuXtnG6U2HpFXvQ%2F&X-Amz-Signature=df5c070ee8f5235549ea1e2fb912779d9014085b1896f68867fe72d6eb9c3adf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKRCBPVT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIDeD9MuCSwIfZ3tpP3Fay9mzqBDu17wv5DoyAFlAzfidAiBApwUKG7U%2Bs6VT0nHdIeniD%2FxoaoMQRxJnIZll48%2BH3ir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMr4eyq0IyVK%2F8vNApKtwDE0UGMDWH7iPhQ%2BaLirLITTPnYUPkEfrH4nZPH%2FS3r4lMcslFXob3AyoBGi5fP9JQ34k%2Ftg1grk%2ByDTObuKH2IadWUFFniWiI596Cfz7IKiLD94y6GygrZRWr6eSJ0XsyvOWODZh9VHr5kIdX16GPcS6NK%2BXoJA2xgO6%2FoA7XZ77ojPIuoHB3FlWTGZEYVkgQmXHlxQQ79%2By359BW%2FEOduN%2Fol2AlOZDOE5yDCW9MtGwpqBkYZ5fflM2wzX7OG9uMFIMtf15xZl5Jt%2BlAlz%2Bup%2F8PQdpjfYTQI40MV6Uvh90BJpXqnaKt%2FcoqQPDD%2BeykT7WnYdfx8bo2A0mdOvSM5VvlQUi3Yhv2vufhIE7kdnAvOsnZWgNteIJ5O9wWWSShV8JzM0qIP9XLw9Kfa6HpdrfPKmMYLXskboy1AmGhdA%2B0z0Jk7gC9r9XeqEFfLCIgyPby%2FzF2KtykpDnIRI3bzq57DYGSsND0x1g2P3QD936M5uTmjp9WmcuoLsAylJQJDJvKhmzh8rvXvhboxCtdspddhlhsu6W0Hgyrg10rst2i8dj1lvBYNeG15sNoWYO1S%2BrC7asiGzFD3u6Aj2n4TlGz9uBhDGgwnZXEh90Dk9l7grHdn%2FqqitxB7GQw9r%2BWvQY6pgENh7yUluBOXO1G997aPuDarhVGnFm81GW2Mz%2F%2FaKq7ntoQi2k1TJ7wTSJ9VbzNd1H5IHuyszU%2FoKrL%2FQLqx5G5fgZqMa%2Fjm20at57GNnKUqJ5PhfiwRUUYFj0uHPkKxehRTFLG525c7e221AwlSLZLo14rZkgMb3Ae3QmrZEzsMb0ktw48r2PGRxRxiuLzKIiERjD2EUNFPV7R6LsiyRvAQosLW5VR&X-Amz-Signature=40799ae799912b307fec751f1a5daffcdc86330d16f5b927ceb04c50d11c5949&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPFVIRKL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQC0ZWh7KWUWkjATS2RI6ZhNO8r%2FSUc%2BvnbjvQ8%2FK%2BA%2B5gIgZzGrEXTlkhznlRcRCbzbWqjsH28urM1L0OhwialY7uYq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDEfB7Y4Sf%2BMMX1DyFircA%2BYkPlbG7vVPEyDLxzqtZrZg%2FV%2Bgi4vGBTWTJYBspqrTLNLDArXSIK9BM%2B74FSfuWiPxA9gtv71PmmnUBgY5Ns8Rl%2FXnvC3VmXCzvZSsNNujatGciU4%2B3iJRoq%2FAYM%2FIoBOOLZtNlOXUT29mTeGZ3OtF9nJeryBN0i7hmG8roB07iS4S0GiWZLILKGTJ4dGLyIcV9BqJjDKJfJxsUG6pHLtb22e1rtz4%2FAPFTHxTksZx2sTmt%2Fqn%2FRHlXQIibm0SXGUb61OJ1Nled6XmeEmxJT3%2FHbv%2BjpaWNefhrBcTjYwHSclPUgoroAYH0WbrRN40%2BPa90%2B7iAU%2B0j7%2BH2sH51ZDpm%2Fu4OceZW0TfJT8B0F%2FCZHm1hiL3bDYyzFPf%2B4oQQDcrYhrALnw787OY9EyCT23ubVTlyVYIBgATvgU9gVQyUIEMu5nj7iJtncjLf1k%2BNfHviAw3k1y1VEOPKc%2FJZsHzJd6eeyFp4KtZsn6ixuM1yFgYaLjx1T8TIBAMLb%2BDGgEOQoFvp75sJ%2FMqyv1614wDjQVoiRWqhiJ4d38HP8clEqipSzM3Ukd1lxL3i4F27mo1570duL9x8FqyvKooayTIKGxxzgAWEWkK0eEFSLDATPTpq2BJAmqkgrgrMNq%2Flr0GOqUBSMcVEAC0dk8NWgimWWOOKVn%2BdIL4utgbdPwiYEeN5qjGvDbz%2FV9u8lBJMBzmu8xxcXJXH9VmeB%2BXn9EpyExHuZ1OoHVQQCDZgzuOHeVjZFlgBC1vDLX%2BOKbfwfYEl%2FErB5GUGCnpvabEik%2BXSXrsn6CP8R7cxj1mEtil6ocae8FEm1kSo1lim49DMWN8qSTB5RQ%2F%2BVja4r98Rz9w6rnUz5N0ClBw&X-Amz-Signature=0c04fd620546fb7472954b92c7f624296ab4507f04cb81fb34a955e99c0d9c66&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ6BLPNW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIDPQDkwsA%2F%2Bzr14iUeni2hGIVCtrQkL5fBGgnjJ%2FVz6OAiEA28ZViyf%2BBTUu7iCmH5UXlMpAwa6Q3Yzi1SIXwCjcjPMq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDHVp3G9JRjgYnajlISrcA99NFT8dDO3SWvoowdRW3JsUKLEUUcTGmoaKk7uBlBtx4Hxl4UThC4UWCKvzUT%2BfxuZroflnW9PBH309i%2BNPhTuakhe1WMs531rd71vtx7a3jyeZVejO855z48i1w5hbyi2a1kPl7zKSe%2Bm99B8Mf2i6ID1L8dRScNpsBsZghgPM%2FN7j%2BnKIeIQMoAw9sl3%2FB72iiMGAlB6AGX8rkZs7N8Wkj%2BG8Qb5ya7PDJbyP1z%2Frn1Lkq1XKLvpYtFSl%2FquRN7r%2FmPy8bveeFazTUe9gniFo2bWDwcytuTKP0AALq1M3OgRjxJ4MvAxwK%2B0PI8wxkL74CkECKvqJH%2Bonr6t4z8iY8dpL1muVjYaN0VgLgd%2Bn09GDtucB3Obc5GtCEQMCzVGd29Hl0CrWtZQkhZoZFCrKVBBUDcuimtudfwlDWWzL%2FiFC8iOfs8fpk4tbgbW4KFJD01Ty0sMO0V5JLbIrOEARoheKt4NWADTBjjQiTXzOhmXIv%2FjU2ZYDpso57G%2B66NTVMcMfOhYY9UjjhuviSQZOYUPfbssSiM61QzHjWr%2BuX9gNMdCcYn8O5i4mjnPEXaDQTLh%2F0RSh5G0CF5WJmwgLj0pCAUgk6hk1neHWxDy3vPRMIfk1HTL1%2BjMNMM6%2Flr0GOqUB3CmISNGzXJ9ii4H3Pap8rsKQRXmXhLu0b6JC8XbcPDPB3lPO3rLiwU4juI1aIDtUFLpOHjqRwJ3Q6%2BwaJvFO3iUOc%2B7VCQYP0gBvBVU9kK0ikKFGVOa0n4gpEvwBxdeG8yKXJTFVzMKszIVq2JSAa%2FYux%2BMhG6JxVr7oYBIdkLgVu4kjvOqK7bH8OSoxBW93NBMnBu6Keuu1B%2BM%2BDINFm2RntomM&X-Amz-Signature=3f9203aee3f1f14fa8cf3b624ad510d0aa8286425bd66269a7fecc547c287883&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662U275EHD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIHS%2B0wWUe88N8fRy1UIfxAHDU67H4A%2BfXMDolsENTJTzAiB2VkVFwvw%2FVnQn%2FEsvOCWUlrWnuNyXfSOg5myf1vQscir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIML8onhFHL0aYkv7WkKtwDUgmKyIB1CBsYtJBSdIH4gNJCKxBBbynSUJXaYN9JkQHzoKjmEozE9kCQvB3oT%2FS966xrjzvRzcyrgMMw8N7keZl%2FtB5OQv%2Fm6V6S3eOa0dD%2BhiU5%2BhkSnW7Uw5rk9rb6%2Bly2%2BZ1v8AM48ALkX3Ok%2Bg%2B3Zo9QQBquGxWSZDHh7QgeqGfEj3gHlWdiAqBrjdJHMBRYquhpIzpY%2BSYRjzdZ21T%2FrqZWg2WHvzWPIjOkETdbvVEEw5WIrTQpCBHH9ZesV2DZdo1TNYCnD1nAonUrm5OBwizyqKQZnQZBwATJFHUqe%2Fo8u0hq%2B%2F6Nthi2W%2BLAIFw98tddynCuzDBsHvyveRjGPzevfnx4Q1qdbEMzMXTwJVOFEw6Q1VwxSQIii0EhSGmNW49k8uX0yL44pPoo2Wz8DkfrcOAzArc0Bqui%2B25nCHousv%2B87tq9NF4X8Shtntt3ZYiErdU0VkjxTH7bYl4Ov06jWCnEuFbMUkWLyWokXBjucIpNjKCbVfQf4X8Ut%2FeAGD%2BVDpbCX%2FtVkq%2FvBjDK2fiTGa4lce73FUryQK55xtXJzvqoWai8YZxUhJs0nkUR3TOyhFt3aC91QEPvlKtE3zd%2FGZoL5iV3QaYiNkg%2Fo1FdpmOH9m4gRmIwmb%2BWvQY6pgGX4pU%2FJmCBVxnmt102g7jW9%2BlRivq5F6z9GzbpmtO9mVQt0Qrpt90evp6plJ005Jc0pvK4BplSmM2KthSyxR%2Fly9J2jPijRtd6CGzy6CVJ%2BHPLE3PVcMabCqqAgNtgmNMfeNCY8sGX2UYBY3jl9TRXXKJqfKMJSHOhebtYM%2BHysn13et%2F45jRkkqxtfU5R1nmWPYF%2BRWH%2Fqkeo2x3oyKRskvoVHWr4&X-Amz-Signature=999c5d80fb29295595069b8364bfa2fa5525374f31a5eda9a32d0baf3d6e101c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKRCBPVT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIDeD9MuCSwIfZ3tpP3Fay9mzqBDu17wv5DoyAFlAzfidAiBApwUKG7U%2Bs6VT0nHdIeniD%2FxoaoMQRxJnIZll48%2BH3ir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMr4eyq0IyVK%2F8vNApKtwDE0UGMDWH7iPhQ%2BaLirLITTPnYUPkEfrH4nZPH%2FS3r4lMcslFXob3AyoBGi5fP9JQ34k%2Ftg1grk%2ByDTObuKH2IadWUFFniWiI596Cfz7IKiLD94y6GygrZRWr6eSJ0XsyvOWODZh9VHr5kIdX16GPcS6NK%2BXoJA2xgO6%2FoA7XZ77ojPIuoHB3FlWTGZEYVkgQmXHlxQQ79%2By359BW%2FEOduN%2Fol2AlOZDOE5yDCW9MtGwpqBkYZ5fflM2wzX7OG9uMFIMtf15xZl5Jt%2BlAlz%2Bup%2F8PQdpjfYTQI40MV6Uvh90BJpXqnaKt%2FcoqQPDD%2BeykT7WnYdfx8bo2A0mdOvSM5VvlQUi3Yhv2vufhIE7kdnAvOsnZWgNteIJ5O9wWWSShV8JzM0qIP9XLw9Kfa6HpdrfPKmMYLXskboy1AmGhdA%2B0z0Jk7gC9r9XeqEFfLCIgyPby%2FzF2KtykpDnIRI3bzq57DYGSsND0x1g2P3QD936M5uTmjp9WmcuoLsAylJQJDJvKhmzh8rvXvhboxCtdspddhlhsu6W0Hgyrg10rst2i8dj1lvBYNeG15sNoWYO1S%2BrC7asiGzFD3u6Aj2n4TlGz9uBhDGgwnZXEh90Dk9l7grHdn%2FqqitxB7GQw9r%2BWvQY6pgENh7yUluBOXO1G997aPuDarhVGnFm81GW2Mz%2F%2FaKq7ntoQi2k1TJ7wTSJ9VbzNd1H5IHuyszU%2FoKrL%2FQLqx5G5fgZqMa%2Fjm20at57GNnKUqJ5PhfiwRUUYFj0uHPkKxehRTFLG525c7e221AwlSLZLo14rZkgMb3Ae3QmrZEzsMb0ktw48r2PGRxRxiuLzKIiERjD2EUNFPV7R6LsiyRvAQosLW5VR&X-Amz-Signature=7abdd74388bb11eaac0a9da51af03bc4d36ee5a822d43969e74428cbe95c8088&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663PHTYL3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIF0GTeU0tdBNzcuKrRN7khURXuSJWlrW9%2BeY71XGZzc9AiAw%2BixX9grPzeTiVxJZRvqaL3YMyq9rM7IMxDuMTosLJyr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMXbCm%2BplzvQMwxtZDKtwDiOJ3yDmJy%2BTJK8MN6w5qvcjXdHbphG9y99dpG%2FwOLNuhKLAMpeQw%2BnVR6w5koA0ev66lDtjVFl%2BjbrRcg7Ycv%2BGoTCLBSE%2B3piy%2F6fPskcRTapYat0qx4Aj5f%2BqOgCqBJTjL8%2FdtsugtwhPdvvC%2BQpTGoJFKuaaLirMt2y8Fm0QTYJvgqkhQw6CsM7bP8rGnzePfnnScCE953AkJFJAA1pZEaIggSAxj%2B3aJ0NRmmcxpBALWr3X1aEbHQW4FbY0w%2FGkyRN3MSHxIrE%2Fu3jnzffrPI6V9j%2BiopIQHdS4MJHvzWdTbDJ15RRFJqGybY1u3cQ1QbXrKY6ItlEQjxYdUjcm%2FZdchyypAIWmaGgrB2xyDjUasIJpfWHTkFkAhhfaU89Gd%2FSyvpirqoPexoXf%2Bh6xbkj3vbnPVOEuT8%2F0TCGmuiH5DpFDlpOfO5ShmQPEbwTBm%2FOclNkdoMB11xef6mt%2FRMYEiSBqwmIOJII4c%2F7YMTru1ksXKrdCXJy9qU71dHIZrhWPttwKa3uAZ52t8BP6qedjZkqgYJA3YdYp2jJdsO1AQaTT0f0Z729N3Rqr57wPXPsRum0IRmwSRlMI2UrGIFtvTut7989k7sC6i0fklz6lvEU6nmLAZ0bQwxr%2BWvQY6pgFomVuoehRNOCOy9w2ChFuL6kIm3WzduSeb8Rgri0qhqZ9AZr49WoXwUn1Sremmf%2BNrRFN3z3ePm3yYjPmxRLn1W7CYfPhQOrfJjJHCfHBr1fnhCmp%2B9SE6S9PFgCALILyx2bkFpopF4mONvC8kzqn4h3N1QQJ8WHD6CZtgVZMDOrLcy6xZ1P21lzweVpcTtCevOkoVxGOYd%2FGFk9ysP8%2FlMPlazk9Q&X-Amz-Signature=175b0dc3a2227538279abbc575566654f28dbed05dba64635dda9b0001ac7a2e&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663PHTYL3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIF0GTeU0tdBNzcuKrRN7khURXuSJWlrW9%2BeY71XGZzc9AiAw%2BixX9grPzeTiVxJZRvqaL3YMyq9rM7IMxDuMTosLJyr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMXbCm%2BplzvQMwxtZDKtwDiOJ3yDmJy%2BTJK8MN6w5qvcjXdHbphG9y99dpG%2FwOLNuhKLAMpeQw%2BnVR6w5koA0ev66lDtjVFl%2BjbrRcg7Ycv%2BGoTCLBSE%2B3piy%2F6fPskcRTapYat0qx4Aj5f%2BqOgCqBJTjL8%2FdtsugtwhPdvvC%2BQpTGoJFKuaaLirMt2y8Fm0QTYJvgqkhQw6CsM7bP8rGnzePfnnScCE953AkJFJAA1pZEaIggSAxj%2B3aJ0NRmmcxpBALWr3X1aEbHQW4FbY0w%2FGkyRN3MSHxIrE%2Fu3jnzffrPI6V9j%2BiopIQHdS4MJHvzWdTbDJ15RRFJqGybY1u3cQ1QbXrKY6ItlEQjxYdUjcm%2FZdchyypAIWmaGgrB2xyDjUasIJpfWHTkFkAhhfaU89Gd%2FSyvpirqoPexoXf%2Bh6xbkj3vbnPVOEuT8%2F0TCGmuiH5DpFDlpOfO5ShmQPEbwTBm%2FOclNkdoMB11xef6mt%2FRMYEiSBqwmIOJII4c%2F7YMTru1ksXKrdCXJy9qU71dHIZrhWPttwKa3uAZ52t8BP6qedjZkqgYJA3YdYp2jJdsO1AQaTT0f0Z729N3Rqr57wPXPsRum0IRmwSRlMI2UrGIFtvTut7989k7sC6i0fklz6lvEU6nmLAZ0bQwxr%2BWvQY6pgFomVuoehRNOCOy9w2ChFuL6kIm3WzduSeb8Rgri0qhqZ9AZr49WoXwUn1Sremmf%2BNrRFN3z3ePm3yYjPmxRLn1W7CYfPhQOrfJjJHCfHBr1fnhCmp%2B9SE6S9PFgCALILyx2bkFpopF4mONvC8kzqn4h3N1QQJ8WHD6CZtgVZMDOrLcy6xZ1P21lzweVpcTtCevOkoVxGOYd%2FGFk9ysP8%2FlMPlazk9Q&X-Amz-Signature=7529279f38779c99ab1710816837d10df443ca971ff18d1be6235cd7e35b3d24&X-Amz-SignedHeaders=host&x-id=GetObject)
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