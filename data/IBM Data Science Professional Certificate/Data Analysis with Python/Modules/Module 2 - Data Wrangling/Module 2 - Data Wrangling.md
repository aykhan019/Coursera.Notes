

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYBQ565K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQD5jDw3aA%2F42aHRXUqvuVQfUh7DrGhjrdhRA1KWWolcawIhAN9lVol4g8YmYeecmt5fIZKpL%2BN7VI5gqikJXw7gJqHiKv8DCGAQABoMNjM3NDIzMTgzODA1Igx6rFgsTUznZVxvAN8q3APfhO6xnZCW%2FIpMu0354JQ8WswGo0TDpqsHHsyx7%2B4n2slJcya6h%2Fi2B01kSsyLlkPZ1tg2mpmInuU0TIyaxDtSRqvEsFDiGR0NxgHRvUwr0%2F7dLLZqxZVEIyUNPtlm3v5RuRWYo%2BpGUTp%2FfiF9F2V%2BGI1wbkJ8V2MP%2FmaUIwf9T2d334qXmFaJWzio%2FqrOPgSoTfdXtQIUOy%2FAvpHAC8%2Fo1Ru10x79bi31JcIyC%2FQWHwdWPVabFkbjxBrkqh5hufceico6IvAcX6j1ZPk3F0b8oWYz8F4YjtbkYdGSkZrl9gP7wWyL%2Bb8mbZCvxkaCNt6GJkI1YvCxYpH59JXAg%2F%2B1eHIfIHefN25Y6Da7IJfWmYzlfvwWLiTPLSpkIok5a1GfjQ5IusL0v71PBsBKZPp%2FtdwcGC8A1ozqI6L5d1XxAzqSHnNNIEqF1xNP%2FFFAC1aoBWL2l8rqqYQHQcLkgSXR13fZmtXGVD8n0k4boFp%2FbnfYG2LyV38%2FRd3VHvWpZ9BVdEI3F471JQ2zpHPaE%2Bh%2BOuANNftFK1dgGj3a%2B0S7zN8nr1YDjTIMxuTGmeR0AJMjSRnQ1Xm4c%2FGkQl9W51nc5j8oman0o2v6c1f%2BhBGVL%2F%2BHcczi5wxmRqcAdzD5m5O9BjqkAaHX3Tf2UgB4q8qAd9OK8yl9ai0zBKoDxxzzJmncq8yxJM4wSNbmVFuIdRq1VpJskT%2FzFMr%2BNyl%2BKs22SbOrh%2FUkSeV9Uma8iFzb%2FYoV90lkXV2fP9D%2BKG%2F28t7sD6Xu64uk%2FCgtFS6P9wuQwZwWDWIw7tBwTXgSe%2FTqol7V8odooKy5G1dOsByS7HY7F0gSTnGCjp3HsvFii7JIBbzxpd9V1VnW&X-Amz-Signature=149a492c721bdceea0ecca1812a5551a38686fd8680baee5a666b1f1a75bbcda&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDLCBEF6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQD%2FG%2BQu9HOcAQkpBLlZUQFQax%2Bc6C4hJGxCNXe9tqxsawIhAO9lCtGr0XeeVTgWHTR5on2yJnTghFPxvfzFmZoAeiCEKv8DCGAQABoMNjM3NDIzMTgzODA1IgwYJvdWvmzoRoe%2BTgAq3AMYYXKLlZb%2BZQcx07T5zbo9C04mG7wSqgvLSSMTlc8qv73PVBEH8kOcfodeS9bXkly2IPiPDhGmbcSuOkVCXnyNq6vBWDt%2BzV5fqT0PCIBdbt7Rurz6ZUFUopPMMQooIL6ljejlahWboLannrnA5r%2Fgj326KuuMi0056tjuE3xvDUXF8ZVM3vLJrZzr2CisR8%2BB8qOEJRKKzujcNcAFOlCj9SnJiRI1DPEY6xGHHNF7KaTVdfzQUc%2BAKcEGHhk%2BC%2BGxGVACijZXNljBVnYbHXajfSS8X9ow3cUsCyn7SOWAUqXMxybRcMEEO54PTEEtf1yEw6Kk12zG1KEzJOq5H1hNz30fZGSValWfQaFKKfHeX4GLMDZzdzOrmr4%2FeuhvOQsA7SAi6uZzeuFhjRUPbSmYjAR%2Fs5sBaeBUbX5yyvsCsIdxyYMQMH1AvCaJXbWDYxFvArMHCfS5E0%2BAxOKwdNDgElJQOBbTRX2yZnrKj4ldeafhfBIHqRHdhdTZwpxCzY9YirImH1mUp3O2GmvuYr09lVYZSOCV4dyMGmyLCSao2cqKJQEC5c2xdFwgYYwbioSCrMABswggeBNkWRHDHllYUXUqS50I6UZ3avmBgQdhbqZzlBSy9z54HtTsazDrm5O9BjqkAXJn6IadavrWrxtP95hju71XYWJtZ6RA7bDQ8WjTNwIpPYGjZgNgih%2B7tLutMR9c3XnFRnqiRyIY1SGACYPHBtIlMvYXGLy%2F8O4WyZMFy5iF5Ts3%2BtLojDslQxExrOWEa9GK04vBh%2FiYDBVLt%2B2qBdnfjFeGmpv3x3GCHT%2Bnin0hh%2FQ6lOIPALKxjDeMU4iz2sY0aEwrl6dRMcBJciZIqCnc%2F2sO&X-Amz-Signature=ca7bfa9021d806ce3c832186234574e0ac3e7a3c53a954e11a3ec778ec0fe4b0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FVCEM6G%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIAJsnDY7LrD1JI%2B%2F2Hm%2BLv1RrYG0NTNAfYnPWjWoeTyIAiEAlfTu3arM0Z16icMbGEFwSzixoSCOgE4YDZj%2Fguj4C8Aq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDOlc6KPxGhfklRTHkircA8L1BPvtVqanp4uT7%2Fhv4J0oJgj6doLUpXmgSm6L3DSB7jQBFQBrXLKvVPJk2rOgWNHBaP%2BYicowkg%2FU3uWI4jhZzH7HJMUKGurwhTnwp4xIuAfd1q%2B09j8piOO64EfmcZzOv79WwClpAMNmcqrR3Faw6n1I7GyPp4xncaxYQssjmzbdnUiYdB1TLL6qh6y07i01lqxX7ifjha95d4M3ldVsUwzWy9Jp9LOEhjTFMwT3yqMb03%2BdCnGhcB4rjmrC2tULNVTnsli2arGQH2NdEd9zsIgVByiwbt9bkS5cupKhuCrIdVMmhTDHcDgi5C8hcIy4F3qXwL9tX%2BgdiXWHWAoGLYg1yw%2BtAYMDKIKRybKufBkmX2fliQIIEghaABKUvXMBl%2BpWiA2T%2BdDbxQn77gBYdIm9qsAVh2%2F9%2Fs7LGXobcOLzdpleWoUjCEUDSKn%2BrQh2QaLKH8Zpbit%2BRUb6%2FhP704t2EKcM0BjNDN7bbNpKzBZIqARjsVggAf2%2FosfVRQslmgyKVQ8Y3mSAljKC%2FnbKbBGrKyp45vQMUZkWB24OefB6vodYH3KX8XUo4wygyYGIxF89nSJxEe7Wo51YjAEsAtkFmhMLN3tIzFqx1nRDkToBC3djSPkBanhiMNOck70GOqUBa8sV4SMwpaAOJFjEvWIzurUbGU6DSumZ4POKRykGZnsw7f%2BB5u30wTSgEBDarEp6%2BwJluCJu9dKsT5bZy5aq7WrOMJ0ak86IkAZcf1g3Nxl5At0br6KwfT106WoZmUwLLCMGe1NZhNb5vQIrdiFRJTTDpxfguSJxY97J2I%2ByTVPXVZMgXCDw85hf%2B%2FuYgCfbwYXlevVuD5YdEfoZqUXOBwDIa%2BCQ&X-Amz-Signature=4ebc9a33fb0a5267dc4b712e7354d9f5b938f8c4bf06d4d8bc13bddd778d2cc2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OQ2JACK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIFoTJ6kFTsVfvHB18CIeUVmiUwthN2ahWPVVy%2FkJ3bqJAiBmkX5mXfgDSUQmhDHgWJdlDNdebsy2SvtJioV5HDSRSCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMkFrOo1EO%2BKBJE0cZKtwDws9v%2B%2F0iZtu1UWvylvtduhp5uMf3inqkK9INV0BL%2BwmxJ0aQfYSonDwxrUM59KHZkOghywGqodAsWFpHGNpXi8wi10RrnMYw5HC1suwH8PxUnksfrZdxq2LTJ5j3ikRVLjzitJ0%2B8BMJv179KyhXfRn%2BjGj3jkr6B3wWWQHZKjmNIWxU1p3Lht%2BLsdh9WGKqivo1LXEIqQf%2Fw72wP6CBKedMBqQuBA4MOo2rSprLqmTYFoyAE85f6BGltWMmTRVkMMbS6BYG1mdzTtUlb4SJNOD0%2FXqOjssRe0PlpIEeYuf47IDIVAYIukQtOeuEqYWOyHOWNEngZrni5XBhQEwjBUYmKK5p29LKF01LPFSiezmh0WyFqgCy2jeqZ%2Bf4VkMLMc3pASFhK%2FdA16hzGfHDrQh85HXG2aRr1suoTOIwgeLTApqx9xH0q%2BSnZXk8OXZI0lASlytVwVHvXpelON7x6OCSouJQFyYJFt%2B0PNqqH2m8POmonmAmmuhkVCDoxnrX%2Bek%2BlkgRZxwtmeBCQWTjDlqLiml5TEfLwgfYWAYRYeMikWHd6gWptfc0ppVmEb%2FmgMTdPIoMRfzkhtMhZRTLRVgJqLDGw08PIiclYXUBoFv3Mwtn264UCVQHuW4w7ZuTvQY6pgGqAx4bOdigmjJTbEiqa5Ns3Hjk%2BCbs6ImRIxxPmkwfYVCYx8iRQQ5xe%2BElTEfQBOcWgQRQPJ5tC6XWr850jGawVCoCAescEXhZ7eQeJcV%2FDLJkQQCKrFGAdCYEOZA5jY8rkQSzAWwEhcYv23qXDruUIC14VW5bP4iEbORUsz8YyPBoCPuowJbuc5i6klqwVTuUQg%2FCKtoChoTAkMJXzIGkiKIRvjh9&X-Amz-Signature=0b3c1695473dac693ae048b4a37b066cb525b90a7b4232fd377b168f21662f14&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FAPS4NC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIGGS7On59gGBVw07gyLKQ%2BB0DylIp%2FTXF1lz6IsXyflIAiB8kLO%2B3dwQmLb7nUsm%2FBmTdH7sJ%2BfGSVCAz6hbHxeHFCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIM7qZP0cV61JzO4DoNKtwDzJcvCe03LiRK3BNYplJtIzHKs5jp6lBgWmXtobka4ymGXYh7SWNPjwD0Ehq9%2BxZNyjCm%2FelHsA5ILLxBWUquCf%2F53jbPTloY4EVDmOcPWhFuoTTV3ISEswVcKufrRmzm0b0uVGLCGoXU7NsLpZZVBd2QwQCo%2FcH%2BHxCCAHeGgIjtIA1BFCcAVD14oSTxzCpyIyfYW%2BjF5Hy8CWDIp5IFGIMLpigHqy%2By56bK4cDAGHBFjnKt2%2B4dGvbBDUeVZBcG4z3MxCp8tNWmwEYH8sQKj%2B7jZEJAPJUpW2hsriUUfJfKxFZahEsEsy5Ldf4nInCSW7t6guEIaLi4ubOveKmTbuPXaXlPI9JR9S%2BIdVnYP2qTzk6by3449DQnBbvoZY0TPauT6LbChx0gK5YX%2FFzV44hdiqO4pXH5Uwi%2FNgi61VaKsnhKGBK0zjr%2FzG8hVAIDTpbHG1LK7nr7QiP1WBkAi%2BtOsZdCXqrU%2B5Y%2FlfhVVIBsiG5VHh3y9Sy5MSVduTxi1iQZERQ71Zj7Ai8Jo%2FLOQKGErNmbb4LOhRGnVQ%2FZ6k8kJbM6xAGnpb%2BbT1MSoIfS6ZiCwZrNperU4HMte3zxCD8WPX4sHH%2BLrPY2U49SgFTKMMK%2F1t%2BuBGHRpXgw65uTvQY6pgEBDPCeLohmqNrQDXjjSc%2BYk1Fo1HSRrmMLuIzuUzHJLlQTHQBkc%2BnyjBqfqG394pV6I%2BczO%2FdcpLvB9v%2B7Qp%2BNPZ0fZfLLWUJYIOxkXHkz8xjDloZkhfazd7rXczPuEuaH0nDege9MQ%2F6vVEK87uXnEB4Xh%2BoSW%2F3p74xPW%2B1Kq91r77PgHslNQK%2FtcHD9lIlRpWX4fbpJH6LfCUdUTmhYC%2FSav4zk&X-Amz-Signature=b5b1148d3a8a86c46f4dc8c7431353a1a5ddc8ee548ac0c93ada553330d66ef0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4V7675O%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDQFXiAOlRacCA%2FCkCR5FU9hF6kTXKoP1ty8ebL4089fQIhAJ2cIsuSRjFPOLAid73h8q5y4fyIQ5Db9hZUP%2B9z%2FZ5FKv8DCGAQABoMNjM3NDIzMTgzODA1IgzfqqdcExikbTeeI2cq3AOIcLBTYnO7NxtLefwHFb%2Bqz2fQt0tVfAjSS36J8uEGMjWqlGjmeBQF893rXSnHW8L0kHahKdFo%2FAJIT%2BpcmBdiTrK4kgiNDBL32PxXjG4w9ReA65otdiJRPfL2HKUMU59skKfXyUX8EKYu5GryuDPWLu%2BD2IxfkVM0tXWXXokoY%2FrxPSiIDogOyCqDt3hj3Y2zp86n9ZCU4PRJkGbe%2BD8DvZfO6rqrMrKk2Q52%2F7zD6YboFG9nK20pgRmZ2BI9HhNuWzcgTTFpXFKwT1D5bV%2FOOPM6nHqMWiv%2B59%2FuDgmXmMG0Z65dj7q1P9QNlCwCBq%2BP5J4KutrlqaAusJf1VZmsWlz%2FeoigMsO3y37S6lA%2BCjZRlEiAQ7MfZPfB%2FHuyRfESwhPWQk49wptajP8sEFK%2FzwrvYRiwttDCJ8YRgPOANO%2FF1KLFbgirVKZacGwq0bLdMB7R4dl9P7H%2FJRL9M5bP51PjGEVkBOnHecQ7kwqko8uFhb3INy04%2FOH98nNwoMEbWK7ylofBhbyv%2BJ%2BkQwf9Z%2Bh48vrfexYapiJNFlc28kg6ihlk5aNCBEySKjw03XLnSFkR0fFN8p9%2FZO7I%2Bb%2F0AUn55NIIQgACdJunyDtX0AmAVj9GT7GpsDPrBzD5m5O9BjqkAf8XDWUQupgpJup4dWYmo4auUIBc%2F86%2F04voooFEcjOSHbcg8k6F5x5qn0c6KyvtEx1AvICJv%2BVvkg2WPNb%2FLiahIg6HuxVA7mQ%2Fh2N3Nfhjs%2Bv8To%2F%2FHHA1EPk53aJpbLWTKHbcGr9sbcifWLh%2BF1qvpNL5iVpi1rlT4COEuT4DkM1ydNLjdfJIU2FYYw4nOpJeVZlklpzpPAvnkys0nw9Tbyx6&X-Amz-Signature=23812221a6c76b6f3f281546728914d3752e27d3d0593e705ec5b974bac9bc22&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQO34U56%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQCgXlyRj6exjQrv5wdgI%2BvpMRFxIvKL8zOLkPYaBvYJXgIgOXJ02FDGlpY0yowg1%2B%2Fj4%2FGTYx2ZE7%2BuPXM5TDtSkxYq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDMieSn4v%2B6bEZxaCKSrcA261qZTD1M2BwE%2FvOgKvlOp5Ar0vw%2Fp6QPZrTRAeU0Zzfb3RzibPuFRDoHqj2Dipi9S1bFa4NrqCtvJTPTMXQ9T4KdgizcjgUZCFu%2B%2FhahKIaSazuMatwKwKJt%2FQSPb2%2FL51iVjr0KrHS23nlY2cs%2BOqrZlxLW2SIde6LVVD4828a9H8VvI7RmtOLLB4JntTHgnafsnYz1KwFagENc6x%2BreZkv68iAt00JCdZWXPnG0L1ulTS7oL9xJnDxZTDkDspNVqm%2FRdfCgT%2FU0FHjpO1Tm821G3nPgM2UPzSMJtPKXrL5WJ6b8ZC9Sk3V1oex2N1nR%2FEJ6tWH2B80iuvNV8oUSWNn9g3yDZHyGB931ByocI4aVAWMGGluzCykMweWEGk8Upr4cFuCtAeMPbsNZ24wKkB4TjK%2FHFrv%2BUlPpqHi7NfHQJHJ7S%2Bn%2FHbxgG3LDIUZoiswmmGNXh9i5THvI2gwVXVMhMVNoOF90XZUsbxaoUtXI2OMkNp5vkeK%2BvlRKhbTX3j15zL9nq1hIrBs6ptzMvNHtpTomcva2cylCVJHjoAOjScCM%2Fc61QMYRa4Jj7kZQzU9WZ3cQWLaat2FBvQH5PR7F9TfI23gtFmN7xNH%2FvVVApOuYsYbE%2B%2FwyRMNSck70GOqUBuQgCmMYb3bsSYViKi7TdnTeauf6joo0G9g5SsfXjcMKDj510K7yT6TkWb7%2Bk2SeywJIKtBgeisx%2FZcvMTKuWf0Ts%2BMigasoVZgkHRMGhrF9qD%2BY08DgBOMchi7vDmvddUMJLWyuVM5urtRezUku943uBFxfHMLgQqsBPx2j0tIgiSCGZCkO6Q2RIQPt2WLpW4YPguedZdx%2F5Pphw5uYK12lnuOz3&X-Amz-Signature=d4666795920a1a786ee96d57cac361c0b9d46fedf1272bfaf1619203afe512a3&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEDDS4FK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQC2cuTMotD%2BrG%2FoKHUZCsNcUL7V8VukCr2UjmhBFXDmgwIhAKrrLHfdaBxa5XoCSBD95xXG2V5A1YFTN412YWn%2BFMbjKv8DCGAQABoMNjM3NDIzMTgzODA1IgyiEkk2XsQN%2B9BVwrUq3AObL0PqVrNb1wnGiojgE8TRPKz7ZjOPBxFFfR1stPar2gaAlR7C1aTHAyBft6cB5NmOORY6r9kLDHfhNsNLNYFIbniBj5FU6fxBcnhrM2vwRSth3FiSqkMNNH90G8nvpC86zIQ7TmQewKhiwDGfykJBvKvZpUgYTRXYqiINPsW%2Bc2dfHhQArG0VjqxlYYesf0JqdJ0xshYp0peWhwJjI8H5MAL6rTJ4xMKImUgbqzUwkRSGkGUx5tu%2BLXVrFyBuaKL7z6UwXGZk8kqrxW05EMb2L8bQWjCdWzcumqzc0W%2FzRfxEbMPDGO0a2mQOjNlBea0JJAYcffga6YCDnd2DtzGBLzLB3ofR7odIvVVIhNOT9w3WqrCW8X%2FLALpCdnAGYn0wf20xfMv9dL1vZaT2ubBEWFCleWWYv6AvH%2FffuwpfEZbmQRzp9iajkYSJ2qBSuqUTTO6QCwKAJqctlDigUQzake3NwBERBJ4ddtIkdRUJMYGG0AYKVQhkdZj9JGb5LASWfrSMOUnjN5ug0nQjleIgg2oEWLXpzNHVqmCAXgek0xGa4QwioRO3lH7%2F8O9kGUU3L37%2Bbm%2FbChOyc0vKjeE0sxTTds04eL2YfkG0PNaTFWqGmCf1xWM7ZF8ekTDTnJO9BjqkAR392odfMFr7TRyEG3Bph708po2uE00dEciQ8hyhcCahIY3MqwJubxiopLXWq8HwHwY2c7VG1oIXN43UFwC9Ooqaa%2F48rI1gtpguuQ%2BJNRtqIHnnOk4e%2B4in9f3bonYO5XyrnHraTZLqBCHtWaovbZVPtK3UZJyuJFNRFUtFMzOWB0ti0JMJHll4cpDvyn3V9ml3Quix8qAhDxmIo00vy5E4Wvsn&X-Amz-Signature=c0a3988a311fe0daf148db3bc79ddd338df55dd5aa3378c50a72dca06956e440&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FAPS4NC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIGGS7On59gGBVw07gyLKQ%2BB0DylIp%2FTXF1lz6IsXyflIAiB8kLO%2B3dwQmLb7nUsm%2FBmTdH7sJ%2BfGSVCAz6hbHxeHFCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIM7qZP0cV61JzO4DoNKtwDzJcvCe03LiRK3BNYplJtIzHKs5jp6lBgWmXtobka4ymGXYh7SWNPjwD0Ehq9%2BxZNyjCm%2FelHsA5ILLxBWUquCf%2F53jbPTloY4EVDmOcPWhFuoTTV3ISEswVcKufrRmzm0b0uVGLCGoXU7NsLpZZVBd2QwQCo%2FcH%2BHxCCAHeGgIjtIA1BFCcAVD14oSTxzCpyIyfYW%2BjF5Hy8CWDIp5IFGIMLpigHqy%2By56bK4cDAGHBFjnKt2%2B4dGvbBDUeVZBcG4z3MxCp8tNWmwEYH8sQKj%2B7jZEJAPJUpW2hsriUUfJfKxFZahEsEsy5Ldf4nInCSW7t6guEIaLi4ubOveKmTbuPXaXlPI9JR9S%2BIdVnYP2qTzk6by3449DQnBbvoZY0TPauT6LbChx0gK5YX%2FFzV44hdiqO4pXH5Uwi%2FNgi61VaKsnhKGBK0zjr%2FzG8hVAIDTpbHG1LK7nr7QiP1WBkAi%2BtOsZdCXqrU%2B5Y%2FlfhVVIBsiG5VHh3y9Sy5MSVduTxi1iQZERQ71Zj7Ai8Jo%2FLOQKGErNmbb4LOhRGnVQ%2FZ6k8kJbM6xAGnpb%2BbT1MSoIfS6ZiCwZrNperU4HMte3zxCD8WPX4sHH%2BLrPY2U49SgFTKMMK%2F1t%2BuBGHRpXgw65uTvQY6pgEBDPCeLohmqNrQDXjjSc%2BYk1Fo1HSRrmMLuIzuUzHJLlQTHQBkc%2BnyjBqfqG394pV6I%2BczO%2FdcpLvB9v%2B7Qp%2BNPZ0fZfLLWUJYIOxkXHkz8xjDloZkhfazd7rXczPuEuaH0nDege9MQ%2F6vVEK87uXnEB4Xh%2BoSW%2F3p74xPW%2B1Kq91r77PgHslNQK%2FtcHD9lIlRpWX4fbpJH6LfCUdUTmhYC%2FSav4zk&X-Amz-Signature=f21c35983319d4e513287b9011d9c88c049f4b3579ca733114045eb26384422d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3Z2B3MD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHNg3TATBQgqPMrVSUKc9TzKUPCsncxW0ToYetJ65H7ZAiAoF0q1SbpmTj1Q4RazjsWBTjtDuKsrsdB%2BEBRrVfUdoCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIM842pvvFZXlBKc7gPKtwDycFQLaf1eKDJJVxtNBm0AWGxHUFdeaEIHxanD0TFliBIP9G9pVfvKeCwnceWiakHueJsu4jHlbjhzb2idItSwPwXwXCDZ2suyXtQMwyo1iWnqhhDNw%2BGVwDcmeyfe%2FjGptDkdCYtt2g1u3pB943MOqDVizYKHNPdRqbtJgydEc6U29vLgz5FOabJ8524P1O%2FlkcEj7L9NBdV1vHdyHluStMvWbMoxaRAKqouLjAD0VWAz5V54Z6wvKpLBPDHtab9YEyegN2xFjQtkFrhoHW2e0l%2F9FROnSSb9OSSLY2IkRvSeMUXQyCWFukrF%2Bt9%2FaU8kAEOxzE7Ht9Spw1tntaf%2Byolvm6bSRTAzD0C0SW5C%2Bf3%2BchDKXoDBlP4HvCgCAOtiqF%2FJ7yV5o8Pkt%2BjXnvVli6e0xI6YqaFbYAwNuDaMZSseoNwkZLzl0a6qJ6Rg3LWtYfw3WYZqWLVsLBmPF0lykJuMwoiNOOzZ86a1LNcR%2BMoR7UFWXQ1eaXF2CHbTyjrbGwkg08Ya8RRz3JKjPA584RlP%2FyULuw8dVhehMcWBsoxAiMFRtnhISCkZl9BEW16zwyMP%2FivbF%2FgrslugU8nVKbybWFiJy7qrcOpvi2tDiVqa%2FdQN2CJJlDygRMwxJyTvQY6pgEJOpxsgjW3OOqUS1bHMi6GjwKrsnVFING4Syey3Kkuzr6pe3fTewqYE1c2%2FGwrTmrlNYPH8vzxVm53k2aa%2B7UORaPYZ8h%2FQNSXZ4QGRbjFkycLWXySo1Xy3oo4XdHFoXSgGT%2FwuhbF3h2y3KFibPBtYzrFemEGcGo1VX4l9NJkgrfY2Tc5qUZr6CrOMrMgOFL8AsP2jwioXDdrLj%2FkxotzaFwkQ03A&X-Amz-Signature=c3c24df7d6239b092a08c02ce83e6571ef8462379b44a00ff99c11028fe3a9e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3Z2B3MD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHNg3TATBQgqPMrVSUKc9TzKUPCsncxW0ToYetJ65H7ZAiAoF0q1SbpmTj1Q4RazjsWBTjtDuKsrsdB%2BEBRrVfUdoCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIM842pvvFZXlBKc7gPKtwDycFQLaf1eKDJJVxtNBm0AWGxHUFdeaEIHxanD0TFliBIP9G9pVfvKeCwnceWiakHueJsu4jHlbjhzb2idItSwPwXwXCDZ2suyXtQMwyo1iWnqhhDNw%2BGVwDcmeyfe%2FjGptDkdCYtt2g1u3pB943MOqDVizYKHNPdRqbtJgydEc6U29vLgz5FOabJ8524P1O%2FlkcEj7L9NBdV1vHdyHluStMvWbMoxaRAKqouLjAD0VWAz5V54Z6wvKpLBPDHtab9YEyegN2xFjQtkFrhoHW2e0l%2F9FROnSSb9OSSLY2IkRvSeMUXQyCWFukrF%2Bt9%2FaU8kAEOxzE7Ht9Spw1tntaf%2Byolvm6bSRTAzD0C0SW5C%2Bf3%2BchDKXoDBlP4HvCgCAOtiqF%2FJ7yV5o8Pkt%2BjXnvVli6e0xI6YqaFbYAwNuDaMZSseoNwkZLzl0a6qJ6Rg3LWtYfw3WYZqWLVsLBmPF0lykJuMwoiNOOzZ86a1LNcR%2BMoR7UFWXQ1eaXF2CHbTyjrbGwkg08Ya8RRz3JKjPA584RlP%2FyULuw8dVhehMcWBsoxAiMFRtnhISCkZl9BEW16zwyMP%2FivbF%2FgrslugU8nVKbybWFiJy7qrcOpvi2tDiVqa%2FdQN2CJJlDygRMwxJyTvQY6pgEJOpxsgjW3OOqUS1bHMi6GjwKrsnVFING4Syey3Kkuzr6pe3fTewqYE1c2%2FGwrTmrlNYPH8vzxVm53k2aa%2B7UORaPYZ8h%2FQNSXZ4QGRbjFkycLWXySo1Xy3oo4XdHFoXSgGT%2FwuhbF3h2y3KFibPBtYzrFemEGcGo1VX4l9NJkgrfY2Tc5qUZr6CrOMrMgOFL8AsP2jwioXDdrLj%2FkxotzaFwkQ03A&X-Amz-Signature=4fd7d2b638312dd9fef449a5ffb153f036c0e7e86706539bc613b5b45c380188&X-Amz-SignedHeaders=host&x-id=GetObject)
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