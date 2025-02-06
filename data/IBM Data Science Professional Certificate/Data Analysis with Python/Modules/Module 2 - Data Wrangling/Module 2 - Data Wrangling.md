

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTUHIOVH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDwd5YLwIyiEn06dXNup3VAjhYh3YAZcdat0VaJ7drKnQIhAMWLguKw1k8HqMtD6sIj4VkVPFeh%2B6ya7m0TyCEFH0p9Kv8DCFoQABoMNjM3NDIzMTgzODA1IgzRp%2BRe1VMwNeP74Hsq3AP9xdJxIe4uUWUtY3QTFt7ifk%2B4Zx0rR03BLChWCb9rxvCJo6MKwUiPK3Q2Lr9%2Bfo%2BiqIJkKLHi0J48AoOmS%2FBqETI5d9EvaatSOWBSOmYxZ5yBbFzFFQ0LRgGad0fPid%2BeyCf5Bk8r3bwM1mNbkqeWAc8JwJ3vEe2Vw93e2YU5xOGpzytXxOpjA6aoeVZPct8Jmi6qQZJNshPswkeS%2BMI9eBVtWFt0H89KFEi%2FtLuupaWW57aQMJ8WgyoTHOOh41rYMjasuB4qsXubvQr5iNECpQmMtalfD6nEqgsacAYq2j6RXTE0wv5c%2F0Skxax1e7mcCAmMZVAg97LyBnca9ZwuGqIjSn74HFaFTOjLk9%2FET%2Bh3M60eUH8RkltwIOTwnMErUZGVgrjJ%2BsGjBFcqbpHFt%2FidsNgyyXfuDXTwhlONdVU2gxxMI9iK3s%2Fdrxo0QFEqjgVQPcPatzc%2FEnYVPBktTb%2BnZdj6rP62vTKD6%2BmJsCcyo%2F36v1%2FJfoPt7q0mugbc%2BGNWqwosxxeXQY7k6pW4K7eATHIvVxei2n9H0AWxYFZZ0Nz6xr3rlHkeoZqIH6Va0Vtoc7U0uuoGqpP4FnGwiAu%2Fc8BcX1jBEix4TjwShcv5L7x0MRRU62DBkzCa7JG9BjqkAUJQYz9%2BSlJfUTy5UqfyEvEpBBhqqKQh16gUhfSu9JWeVk6Rkzs7QmB4Glf%2Bm7%2B6SEkfpIIcw%2BapONRjsO2RIAOGP9z0rZIlRI%2BvZ%2F5neI9LE0reQjDmIwH5P2RsTlYZDytN1c3Z9rKcRR1zR2sJ%2FVGu434sVXgvdUi%2FwSN6k02xnLBhVl2mv8AbFOnpJBGYgNJImdb5whRu3vEaU5zm8r1isV%2Bb&X-Amz-Signature=ef080f90a84a661001fe311fae70a5d081370927356f5be8cfee61eed56d76c6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DXHRJGE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIG4szt6uBI6xOSRaRZH%2BaGPIYthJmEK4DddHnBojEMf2AiEAhJKWYFtXDrw93n1QsOl6T4GoO%2BuKF5NCzTdcBhQb%2B58q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDCtRkSuoMNV%2BAxpg2CrcAz9vq6oArcCAg1gH6XBRU%2Bhqb74xBeaBxdCNV2nV%2BQqnC742OghUQMTWTW58slENI%2B3wE0SoZ75PW1EOx%2Bu6LyFb4iJKEGZdebswsEAABtAOVqhOMXkb6b749YR%2FTV0G2rFR%2B5Onz4x2phSurSlQZhodviNQQH0OwXHTOE31bkylxy8ZDi%2BLBnesKX5TSWlmQ7nqevs0ClLsdGdWS5ZKo6C6jnDt4yy3HlssQknjB%2FGXUu178Z%2FvXbnkbK0N%2BkChQ2%2BmdildIXj0onh9ohv30SDTuwP28D62CdvvXmRJHXMd86E1kZ0R8x2vRKmSRyXLgLoPTjPviTNURGhPLokPG%2BKYbHzF6Cj1Ofg%2B8Q2Ztyu44BOqsiTbD88thdhgDYFuslH38lZ2QyXmcfzNCLbe5gGtdSd9%2B9GxnN9CIyRhiEs5fW4xpNmS6buK2wjiRX6jPJebbKKTEuK7VpJgmsfWeDAgwhygbboPTmnOYkMjLZvOZY3XUJEjSUNA7WPlAwfKoHfMJMy6AG2RJak1MLupCVBjmizh5GtFliVmA3vAE8qquwsvov%2BLmH9mkq3QUIuQsssZTYsO525YenktGyDY8S2DFbeBw6HOR1fS0tE3d8ncxC8zKQyPhNmfkGxzMI7skb0GOqUBwye2DCBzpDLeqdq%2FMayYMeXTWT8SQCP9lkgxo9%2Fd2PAExYJRiYLA0QTRDx95dk%2FKrwP59TcaVZh81AAhPQ6wa%2BueA8aNkndIeqXiXbUaCwodAHF78A6mkZvVw%2FmrmEHwVBBe5Rh5upxZQKtnCPlyT11tMGcAGtm8bBRa0Ae2KkKhXdoaXvnp%2B%2FvOUYHUXYApPDzQbCESeKVSommH2eRrDIfBfAt4&X-Amz-Signature=1c481480d95e228d3610b40fd3ad123b937098864f58fd235ca7bf13af8ed441&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZU2SVQE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIA6qSmuwvdMoVtI8UO9HyjC3%2BjOKZQ0D1O9O0K5pRXciAiAekKRLmSVgxohTFFkm%2B0xGfWSIFpjPBsweMI807GxB6yr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIM3v7LJbuQWM3nFuleKtwDziWrfRtFziEEavSat4B07ujeYbhhVDwCIs%2Bdee%2B9IqsGLoeZxTQBH6w9sknv5WU2vhAiRJFotObMoEf1wQEIujYf3iK6pJsz1%2B0JjrzVB61EqtX9NVze0cDDBK4hDAmQCRRnrOL%2Bpobxp2S623ZJ0zWkKjZaplxclXfnBt%2Fsg0SOnI1yQT8sYdadoPIyXyawRk243ttTuNJf%2BZdxOvmrzTSZTQu5MyWDgFv%2FW0gfdXNS7QbeGEiiPo3ddQ%2BG3J8xqEnpEqZW8n5orwNBiLqT3TE39iPKK%2BcnPGFSgZulFZlq%2FrOqANmje5vafPVDsVr8NP1TDoHzR8p6ONLyjTwpl6KEmRM3a6KiqtGMxO0DocL5%2B2AIs0smqz75%2F4gqDd6XrQ1x%2Fq1NuFWQvT3V7M4YPvBMkXMS4LUAl%2BLnnCcgKU0C2%2Bs6BB1PamIneP9JS7HRj8p%2B9lQqe2X21bIdkp07sVhZiEjPZ4h4CL7cuxJMr4Umibh7N7fzF48bk3%2BwXrTxELOx%2B1gQAgU0dsnTwknLADrAMl%2FE13BtL5JuhNRgWHcJZU941n3iX1567n05GB8%2BZDFFUpP5Ak6SWbeTlDvfBgzZkzyXn%2B6y4Pz5mUjkA45jkbk07HHwsBiSa4Mw2eyRvQY6pgG8CPm84HuI9oA1%2B7HSSycnNP52uxghCwVfVqmJq7C%2Fg3QLn%2B1DekSlp8OIwI7FbQ3FNO0cp9SwxYSDHqP3kNMO8MkjzjH8Wn8IVjgWeEZQ%2Bs%2ByM8TMvwfSisY9seQYDe0%2FD%2FdOzw5bfOJ5UvxAP0LLWzqvqiA8m7RJGpwkJLvPgy2bdX996kpF892myNf0z4uY67dUj%2BEuUOBLNu3sZzskKqckVceG&X-Amz-Signature=a8d9c860ff8fcafa6663e7dec4caf4f7e593d245da9ec3f96bbd0d7fe7263a85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJ2XCHLE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIA%2BsAq6YsmIQAXTOA0Fk6%2BDupxk7bwlttidDMAi9hNEnAiAh%2F%2B%2BxLYxAUNFETr7EDi3AzYGRaJEvWmgy05safw7mvir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIML%2BYIbpQSjVNoMuqnKtwD8A5YN3GAhEyw2dCTStj6W1sdIyG9M0kcdLjXRbKHsQr6q87Z8hlJk2K5Lngo6myVjIT8urWkvkHqSfixHMrIMq9fXnpKsZEKjSSflPOfW4uMAsRO6gjQ5iAb2NMPnRLI%2Fqt%2Fuj7%2F23JSzRw7SeDaHyWfpvplRIQ30QnEoAkgqmvzJmQtRR4%2B7cjuNIPuyRjDchp6awHyQR7VuSxqFFDetaa%2BBYfAq92JfwhuGxB78moQszUpAN0xwmhCMZPoHw1m0fqnnyEaxI3tVO8dZdcvDRbXJrsj1m1g5AA7MxV87uHnXjWoPrspx8psy01jsxwISxHPJUgySkllIzoSYDCA3bKfhavnQ5MMWPyizs9x8IR8Y2nDkXXhbWcnBFdc3KBa%2F%2FmdVbIiKefVjrYA%2FaHLt9xrHRp%2B8t%2BeSFLtIqCdVjkgIKisn5LJss0%2FQtMwF0AkyUwQd3JEpJnNMSmId9LRkaOANOf2o605jWIxLtZ0LGD1wpzDdqVbY99Vto040JiS0di4Ndvoi7gP9kgklGQzULCKQHIR7drHFwyK7EKQ3VkAjw%2FIdjQXBXPvlEXqbFoYnhTfQ2VVCQH5iKOIt606DOJ1G9aayRwrJvvLsAqXnQTBWsth%2FtI6hRs759cwoeyRvQY6pgEBHwH0XJeDX6JmJcX%2Fng2vvlYq8%2FWun3Poni9Vh7ZMK2LvTWpcxZ1prbC2JgzA5uYb%2F4go2PNsn8IAgNc%2B96QN5yiHolrSq7fWAfoW20AkMrJ2SznSbaWh96lW3VoCLA2%2FqBnNzLgnCdVA0sVPpWyjjHUnO9998PLFw6pzyJDXDFKj4pRoESPBC8RXqMUOlaug6dvTP46I80TnQrd%2Fw4Kb8qp%2BUMk0&X-Amz-Signature=de9b138362ac0be6b980abb270c7dc5bd017371f12daaa3bbacfcb67a215ae13&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNMDWQ3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIB8XfZhzOF0uap7sxqqZlF%2F%2BtHaBpkrQ72WEdhyEmqmqAiAVSHdm5CqEKnhIO9l%2FDVSJrL2ajzB9jOghGA3tALLMUir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMcVzDLGgbuWzAoYgqKtwDvb5mrrRnzsyXFr0yOy09zk9YeXMeYnltoPJI%2F%2BWb1LBcSCX%2FYejK5K1Sijw8h40sl8sppGcQbtGj%2F07d3lLUZZcsK0Z6Rgf7208udG4kkC5cCmzBEkggHn%2BMHCpe1bwbMIYnbdAlSi0njtpez11118F5qbjMt45oap43Gb4QM9OVdZAjitg5dgxVIeMFtWirDriQlQXlw1Ip1sT%2F%2BLrPztOSUL0L2CIYCK7XA5DNiSgxHoBy4QxtemtcpEXH99nn6HQkANjZYqTF8PrVffhaWYXGVJfGXwdDN8X2Tw9EGrcQwUoNplDflfyA1iO8xVCRKq8jH6XMNcPBdkj73ErsBTTMhmJM7JGpX77j8k8aqVLEXp6p7z8Ukz57xZxv%2Bz71Ms7WltoicUfrAP0WmFo5YemFO59tOyj3qAWye%2FGrp4AgC0tnu%2F51%2BD3H%2BsjNx9JP%2B9Kf7F8mbz46KphxoekOksrvbuk71vUW6VCEpUw0BkgfyV9XwF%2BjxzZTtd0EZ4oNx2n94yExMOjYt4%2BfxhqT0hikeshA6unzZyYM27a%2BE1X0K%2FVwdxcaKTZkYasoIjJDp3Dy5TDcAzRY6s85STbRgnamLs5muJFPiRTWb9qOeEcLCU2OYsrGdSIfvdswq%2ByRvQY6pgFHS8RkTUdasLKnGfb9nuT6JplhTJPVzwKMRm6wdPXCd0o7WZlVvgpSkPfTF6yFtOrMynHmEkS3VNTxWHMgvdgD2xxC0KdP5br7QkaOLtBqaW6CIEXbkmnLQnzq8Y9oMi7PuhxtJsrRcJfQ5bYIqnGncI7QHgeZx7pVosyDuREVTAHC9nNQK%2B54%2FQFHeJ4cI0m9t4UP9npOd%2BZmEfD0jz%2FMb6%2FsrjxG&X-Amz-Signature=887b1405216d047bfa7fb86abf2a301b5a8843bb1596d02676f912c6e7c0c87f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PSFANAM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCCc6G9fIMe8lptFhrCsOhrqxSUqp7RiJGEeeE1yM%2F07wIgMLxCCQeEkPCbHB13B2AlK9wnBH%2BGt1h%2FTW2C2RDjYfUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDIKAg563HtBfVOuutyrcAxHzsOEhStL1ZA6noNUwbd%2BmvZTynhcGRTY8kNLmG9IUvLff8Ah3lfHc0ASGyoEMEtKwV7%2FBdmf87ptGv5M9YwNpMlMNudEdxQ%2FZABuJ%2Fwhvj4bI96pcqrwP7b7JVK74OPLU6fZuL0buamZ%2Bs4%2FyPqbBObjOshQeP5lvjIucyhXkycPSh3jzbZdkc%2FaYUqgMh5veUqEBxOOfEVAlXrlUyfAeU57znzbOZjDIy0mNAbsLkLB574Dc6ioGTElLY8ijlUMSWutrSJVpu5Hr2sPEACTw7yQjdOCFngalaSwNgDmgDN0R7kKsxcwRTZjvML3LoZ3vjIyjl4jYQG%2FCigkWlBGFqM6gIey%2B5rW70v5DgTvqn%2BUyJDCnsnxkUOpTJYGe0A2WZpggDLxQDSP8RWPpTyyH0zplSjDyB6djwqpNOsrbU4Tm5QHm2nPSKvMw2XKW0VQd9IrsKQyQFVWO7AtsoeOapM5UYWrV41PV7gGt9eJKOElvdVUcEdkWvklkmtSYioMJBmTD9tdl7Igoy0byP%2B%2Fu5N1lvP9jHkFoWnEWqFD3F5oxngsXxfSfGuAFfs%2F0ewaKQK94PcMfy%2FO3mGv9HPOF4DB0MBrC9vEraX3FU63iE2TN75%2FZoUWYh%2B48MK3skb0GOqUBor1mrXbTysR%2FvFmcIqYSZwdlK3B4pdcexb7qXkhM2oAdXG%2Bq5x9XJ6ikCXmKcZhHZ3WNuvWZpLa9VozQT8CjkX6WqeTo6Swk9re8f65%2FMOXIeuWHuT8EX%2BsFJGsGAtEZXWyVfQSvU33KZV%2FRo3uyuQgSMBxprmPuMUDc6nKbm1jCeur6oNjPBF%2B0uaVrm6cD5DnppVxPP79BpRvFzlgh3cSBg2aG&X-Amz-Signature=7741c262f36eb080a76a142e96858131e6d1881de2016cc5829f3492a74b0e22&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XX7SQZV6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCnCHOUosE3Rk%2Fg5521jqrMI8II7W1jjMErVnqt2VDsAwIgDEJWFb8%2BdPnndzJeUdABZcZcwvszqKCrWGKjFp4XJ0wq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBcQbeMqWQnBTVIqHircA3YKfGVXgCw2Kg5IQyeeE0OZf5YfZXGcHE90XKZMga6VcEU%2FFw3%2FwmUTyMJYECQFevIOMapdf%2FSY2toQZQcj459DSIV%2FbOTAowKnN%2F61CK4Mojqtj%2BEKNNdO8fqNtCR9lqpuVExXi%2BsyUlZstGhERXzFJRzjf0h4EkgX1bh%2FN%2FLX9KoEm41IMNBRAOaZr20jgYCPrUjUyV%2F%2BVob05KGIxjnlZdTo%2FlRjFX5oHd15R4XMD4jOUbZG33UoquhGgEirDLtuxQC%2BvYCt1sQypbKGfdzCn%2BqM%2B6IUmvybbkRPXdCy3fBj2o%2FGQ7Z0H6C7jD4hPVo3tJdRpK2%2BqaCx2gD6kkuoTMxcmDxW%2BepCbqlrQi8xKBOxpoFANf9CKwvfmSPx%2F%2BtH8MVwu2hGx19KtYE%2F92UQ8ekJ8j%2B5OoFwlWUEUUv%2FA3E2GbZ4TclzJlLmdCkrkNw0xZt0gjR%2FO7hppW4g4%2B7Y8qqnGXWD%2FLpvffg%2F47SYT%2F9GP3sfuB3ggm%2BPrTmpsyYbA3oXcUDohoEdLKew348sIQgANz%2BPZzVhd8A8YlXuSZ5dzvlkDGJgQr1DtGZ5%2F97L3Gto3wAbNeJK5qiUJM9IOzqVVV2UWmvh7TFsPwIhxHy192D7NZnxYqsiMM3skb0GOqUBtwAUnYVm0ttn2NuZnFweF0n749cfyUREAfCTGF0CRiS7VN0walFMTPXUZiC2GP%2Fk9fFyr5jQ5gUM8%2Bk9wMIK%2B0%2B7BidGyz5haPVHhcZsGPqrIU%2B%2FPPYbSowpTHvDFWNe1EzovaBk2KZlWnJqCZ2Zpwl8g%2FTxQvvLXJIrbEsOmaERQp8mrO%2FkA2M8tqywNCe9%2BXUT2M4IiSTbPtwaBlkNRxQa2VZv&X-Amz-Signature=7563ec81e714d6baa417c6cac25438f387a16784caba3a36cbf1574f18439b44&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPELPQNP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIC3xQzEw6g3IQ0RIyo12FlI5dGdHsA7%2Frp1qo6tsGyP7AiEAh%2F3eSN42F6S%2FRuFnE%2BXs24LczJ7LEKVTf1AdrC0OUvUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDA5gzAIgps2XLxjr5CrcAzCILSdDTpUE3%2B%2BzzcAuSuB06O8HmYW5arIkybV9xt55ogqJR0t3s7rQo1N4SGPaOo1p%2BRCWjJT3jZPm8LAiiZwB386QJUKCioJ0KXS2G182gY0%2B3rDA5ajkiJRDpgcoiZ2GvN7Mxnm1WfWzzqTUZZBtHpD9j1RlR8g20%2FhE%2Bk9GLEuC%2BhK0HNzDwrQDBgrvx0RCFZLHLD2r%2BH9qMz2dQhwrtVnBb8WiQku1kSxZIsjL6UlcH8zZTFaoy5xcYtaUbFneFG%2BOHMCIZ73RMLXdU9R3%2Bp53D5xc6%2FXZsUjiZptS4UphNQCzAMotlAT%2BvZiYMVYqeMxqGsZG33zohaX%2F9k1VWgtGb8fW3Z%2F4bGBwVgB621aCWfNG4tFVf7o%2Frd70aeiM%2FP1K%2FMd0ihdeA75bIuS2RLmJLmbPZ2usV9K9r%2BOYshzbuqSPVILrmQ9WluwpRlRUT3Uo2F7ofvl6wviBJtb4hXlAjSHxIxWsMTpoIJS2xZrV5%2BfaMkJYqytiPDVMAJZfG%2FkyaX18xaC3obujG0yBmFHKb7kOtXJRrwbKLOGsj%2F0a0EvzpPn1fzR3q4Nj8dW%2F0ccNa3j%2Fe5mq7bXGU6NdZC3%2FdgYTewfXnJD2riuazKcfA5REsJtzV0cmMJ3skb0GOqUBxBzQV%2FCjtzr8LFTk6xfAyOutA9izNyzkxZvtclCZYKMRe%2Bd5QkQgeFoIcRJkctT0wAa8X8tkzkq6Xsw2P7tfj5LMQlvVa3F0r5H3RWiqKYCVmtLrqrsJWD%2FNNnZLiJfkg%2FOCXrSvzLUqXSb5P4EJPrmTyPZWrEeeZ4DKejD2j85GWjcwSTVWEt9jfYdPVFHoHJMR0guxjkg3LA9R%2B%2FKfedVoiDG3&X-Amz-Signature=c82797be8940bd30420bde15d11a87852875048c0309bd720770dc0890cc8b1a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNMDWQ3Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIB8XfZhzOF0uap7sxqqZlF%2F%2BtHaBpkrQ72WEdhyEmqmqAiAVSHdm5CqEKnhIO9l%2FDVSJrL2ajzB9jOghGA3tALLMUir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMcVzDLGgbuWzAoYgqKtwDvb5mrrRnzsyXFr0yOy09zk9YeXMeYnltoPJI%2F%2BWb1LBcSCX%2FYejK5K1Sijw8h40sl8sppGcQbtGj%2F07d3lLUZZcsK0Z6Rgf7208udG4kkC5cCmzBEkggHn%2BMHCpe1bwbMIYnbdAlSi0njtpez11118F5qbjMt45oap43Gb4QM9OVdZAjitg5dgxVIeMFtWirDriQlQXlw1Ip1sT%2F%2BLrPztOSUL0L2CIYCK7XA5DNiSgxHoBy4QxtemtcpEXH99nn6HQkANjZYqTF8PrVffhaWYXGVJfGXwdDN8X2Tw9EGrcQwUoNplDflfyA1iO8xVCRKq8jH6XMNcPBdkj73ErsBTTMhmJM7JGpX77j8k8aqVLEXp6p7z8Ukz57xZxv%2Bz71Ms7WltoicUfrAP0WmFo5YemFO59tOyj3qAWye%2FGrp4AgC0tnu%2F51%2BD3H%2BsjNx9JP%2B9Kf7F8mbz46KphxoekOksrvbuk71vUW6VCEpUw0BkgfyV9XwF%2BjxzZTtd0EZ4oNx2n94yExMOjYt4%2BfxhqT0hikeshA6unzZyYM27a%2BE1X0K%2FVwdxcaKTZkYasoIjJDp3Dy5TDcAzRY6s85STbRgnamLs5muJFPiRTWb9qOeEcLCU2OYsrGdSIfvdswq%2ByRvQY6pgFHS8RkTUdasLKnGfb9nuT6JplhTJPVzwKMRm6wdPXCd0o7WZlVvgpSkPfTF6yFtOrMynHmEkS3VNTxWHMgvdgD2xxC0KdP5br7QkaOLtBqaW6CIEXbkmnLQnzq8Y9oMi7PuhxtJsrRcJfQ5bYIqnGncI7QHgeZx7pVosyDuREVTAHC9nNQK%2B54%2FQFHeJ4cI0m9t4UP9npOd%2BZmEfD0jz%2FMb6%2FsrjxG&X-Amz-Signature=1ad5de6a8bc22f492a98b6a12da6d22ad11ecae03c928572325c02a9675314b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YN7JHEXU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCEDjJKjqbaDspVg7eBCgn20sgHqMxQMcNGqhaJtfpTFwIhAP02gKSsXCdk3RIIFHQUO9VuDxWZuEeN8IlwPZMo8IGHKv8DCFoQABoMNjM3NDIzMTgzODA1IgwnzWW1k%2FgRNPiiT4Qq3APTbXhXujyLTH8lEioeG7dtrcEklHwC1BgHJ%2Bh3io8lVgoSbiJ2mqOs%2FDxRcZjlliOZlmvu8GBPRnY%2F1onMou2ZkYnvTb3OzYsoZoiT1ZfYfLjr71v6QieeEDlghtEIz4BdtGK6n0zE719jBXXy%2BP5yJ74sLGnYFM5M%2Bht9Fp%2B2TK0iyXQQPs5oBQeVQyFRoKUhPbIsrvshR5uI94Tb0EqSiQIYvHEgZ3%2F1Mls0jilpjExJBNRHr%2FTUWibijjOweNyI5FDHXzHo2ECSirbORnowwItqu8U5Hhk0HESJAnwvTDvzcDckC2apW2vUpy1nnOyG1dsoFI8uHu3qHHyUo1stTQeQBl8RQKaAeI8GPboz6u7jGg5%2FxdOfifKqzf8FThXu3kZzIvGbFsc1POfOq0V%2BWW%2FbthkdbKonYijtjKSoBrYpkUa%2Bcp3f77KQPgPq4CtFopHPEt0Cn9NI607Q%2FEHG4mdvr%2BKdySQVnAz25Ih41Mt%2BegiKnrn9%2Fi5K8qb3Z9wupb5hmPNoxiCRldE75GU5OXAAC754GtO%2FM5r7A4uIzhXBrRhtgcAWAKgp2NfmCoN645ofAtjX8iwcAEi0Rl5hxh3ndWBQ1P6wleZXktuMiZZpsMMidiPKiSc0nzC07JG9BjqkAVwoY9ynWa0jz7Y2p7Tz8fScQkv%2F3grN2jWpOzSRqGIqQf5WMySBMMTKNFL%2BsDjDVby4vIrgWzmznrY9h3GECmebCQ37eUQ0tgIPj8L6fHtO3e9ooTOk7uUEHKHOHNtkwbqT25IaaQXZe22rPECgU%2BChW8UXsb%2BXRAjfs1Yz5GvAQLDDyWn6z14xBCID0CWOYUBTfx%2B%2FejlMUydzXgoLGyIQDhlG&X-Amz-Signature=a853810879032c25d3fc4b12e030c9f38afa465c8267a87c27e5aa322a2dedc4&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YN7JHEXU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCEDjJKjqbaDspVg7eBCgn20sgHqMxQMcNGqhaJtfpTFwIhAP02gKSsXCdk3RIIFHQUO9VuDxWZuEeN8IlwPZMo8IGHKv8DCFoQABoMNjM3NDIzMTgzODA1IgwnzWW1k%2FgRNPiiT4Qq3APTbXhXujyLTH8lEioeG7dtrcEklHwC1BgHJ%2Bh3io8lVgoSbiJ2mqOs%2FDxRcZjlliOZlmvu8GBPRnY%2F1onMou2ZkYnvTb3OzYsoZoiT1ZfYfLjr71v6QieeEDlghtEIz4BdtGK6n0zE719jBXXy%2BP5yJ74sLGnYFM5M%2Bht9Fp%2B2TK0iyXQQPs5oBQeVQyFRoKUhPbIsrvshR5uI94Tb0EqSiQIYvHEgZ3%2F1Mls0jilpjExJBNRHr%2FTUWibijjOweNyI5FDHXzHo2ECSirbORnowwItqu8U5Hhk0HESJAnwvTDvzcDckC2apW2vUpy1nnOyG1dsoFI8uHu3qHHyUo1stTQeQBl8RQKaAeI8GPboz6u7jGg5%2FxdOfifKqzf8FThXu3kZzIvGbFsc1POfOq0V%2BWW%2FbthkdbKonYijtjKSoBrYpkUa%2Bcp3f77KQPgPq4CtFopHPEt0Cn9NI607Q%2FEHG4mdvr%2BKdySQVnAz25Ih41Mt%2BegiKnrn9%2Fi5K8qb3Z9wupb5hmPNoxiCRldE75GU5OXAAC754GtO%2FM5r7A4uIzhXBrRhtgcAWAKgp2NfmCoN645ofAtjX8iwcAEi0Rl5hxh3ndWBQ1P6wleZXktuMiZZpsMMidiPKiSc0nzC07JG9BjqkAVwoY9ynWa0jz7Y2p7Tz8fScQkv%2F3grN2jWpOzSRqGIqQf5WMySBMMTKNFL%2BsDjDVby4vIrgWzmznrY9h3GECmebCQ37eUQ0tgIPj8L6fHtO3e9ooTOk7uUEHKHOHNtkwbqT25IaaQXZe22rPECgU%2BChW8UXsb%2BXRAjfs1Yz5GvAQLDDyWn6z14xBCID0CWOYUBTfx%2B%2FejlMUydzXgoLGyIQDhlG&X-Amz-Signature=dcba524ee353494534bbf38570f2c37e63165f7b914c28f4cd771207d2d20384&X-Amz-SignedHeaders=host&x-id=GetObject)
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