

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMDPDVVK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFA%2F03or33C0bwCwvcuKi%2F6j%2BQOv7TAZtF3q46yEcH64AiAq%2Fsec7hSinzbGCgreoztetIct8xzHTSbjIFltdyYoeSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUIPxZLUSqFlo7wf6KtwDjpTD9WIBIUhuOxZwODZRfPkWHJ1Suc4dYX%2BqVmBbYBn5OYVJXrazHk5EFgPPPo0DC4j9PBRoWDYjfzYCBgeiOXS2TIDTxkj5ULpf2xzph0jGtzP2hzLyL3gkhk2N5byAediXG94rBejIbw9nThdznlL2b7zOkOZdTcKoBtDSYdL9qV61hPdDH4tA5QyR8naN3dz14Ykw1nOm5FTlsBLO8Dp%2FKhxPgFwPNK1g8Tlku7Tmnp7o1PiLtUkZeYcSatStfvS2XvX8YEouHEx5ab22RBOxQ%2F02JL%2BxEEci96btp5wgGVSq3gtnmF%2BMzh9Kdz%2Biw1ACyB3E%2BjcyvW49F%2B37%2B1XihV0ZVod7liJ3b%2ByC%2F0A43D3A8anEPF3xy1jrS5BO%2B4H6%2B0VwMXkX6uF55SgJjdpaU30g045YGFwfL31HicI%2FJ7U2pQNvQZzeBnTw8PnyErpWU4vdhDAa4jk1iNw8UAnXArS9VJ6Ts%2F%2F4ClgnLLihJgxCcYkAQSKuAqrd6lu6Fk9YRrE1ETEIaBXkRhSwBfMnDmrD0eF9Ur5G8JWl6Vkwko7oqgM%2BRP5wauIw6tU%2B20E124cybrJP5m%2FEVqvdog5Qkk%2FfHRhI8qjpvtfYTdspe6BSjEgdEbWbeg4w0r%2BAvQY6pgGlaxC%2FzWzIUf6yhZxHrV5WRwQAlqOpwd5XibA3jBozOAebMDjKDmnFtJbOzhB6vBoDmS8B8P9NCWP2Ogjx7In49%2FhVe64zWSOYc%2F1t8ZBm34nox%2Bxy6bjxTX20XoSqgbNliriYjP2xS2UDFEJY301uxVUZOHcWBDOSLsZUQC6Xh%2FC09Pr1P7JfF2HlZx4wugl6LXgW2AB2cxZnXx13cM3tAHH6ddJG&X-Amz-Signature=2e39649c4e4bc20359f0df10b64b245c495229967750206b9f494434f7d9733e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHCXALMP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCN%2FSKx9DwNlfbZAo%2BR6pThve1zZE%2FkvuAX3XWYz%2B%2BhiAIhANlTvxXngJWQrmPPQqoBKXD%2FiOJY%2BHmS%2FqsFhwrdndO9KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcfZsdebglpyFvAX8q3AOOLzb6YvfAyyrCyEUobb%2BrDsFdDcbA6gHJRQkMNMBb8sc9vAhyZondOd6tWdMFUBHbhbDtJGshE%2FAnlGPdIO1m8tD4NiA4tHhrzAi7KMAu3vNlFmyt3cSpPnu52OkbYJxwoXdJQV8RCcmpQDZuuz29T5EbiVJNGdwKjrRUdFHC9a10d0H0IZ2dthxmBrWeTFmkKHI1dRCl7LLewfj9iqaIyNOyOFXrwYLS786o8O34QqRb9aQH4gw6SungQ%2BzYPLEM4SKlGHHhwI6X7XV%2F%2FByzGQ9C4SKhneIQgBAP9um2QonqqReJHkdG%2FkhOpPfYhbzZKtge%2F1p2h6tt%2FgoFPAEcP4JRO1jxrN%2F0PDNR%2FlExpPFkZZ%2Fiu5zlAgnJ4pUHelW3%2BsHpaDNeerdpCAezutnYWHr3eOVf3GmaLss4ZU2KNwX6h32JTa5JVAfMG%2Bmo5BAW6vNh5qAxhIkQLIncseSkCAI7cylFwBRoo81nLU%2B6ovm7y%2F5SCqrN7YO2MXNuE03XqPFgJprbF%2FLAURrUALbZTlvo%2FaIpviw7av0%2B4p3Lf8GzO13Ng6hcAETC9L4uS1IOGlXHNJ7Av3UrmdjqgtVkzRGX7iwhHPoM3bmkdU%2BCII2F4sCskVqdudSoHjC4v4C9BjqkAeIyUK%2B7zizWGzzDe%2BbS%2F%2Bnv%2BHiS08gSjoELXC%2FFD4q0%2Fz5E3wuQHjkMnNkH02KmJg8gRH9r5j0RUGI8WtoL71kzk1lb2U23nl3wzfK5nDSJ3kd8V4ktBLIYdBbzQT3eTWsvRedQq%2BTSpL2fAtsl%2BUGCaUK1nA5t53gmMoZMrb9ycae5rxCD1DEcOYkL%2FFPMLq2du8KZp9fI%2FEeENuNqC96hTiId&X-Amz-Signature=5f943f6c3532f966ec56fcd2a9b7ce47d9fbd69725022fac915bf69c87dd4343&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TZ7AR4N%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBqHJknQifVR4XeS7cV7ocRN4Elzh7TZU19jqHGwBw8nAiEA0J8Uw0b62kKL%2BklEI%2FPt4xLhiPG1a7Gz1QmIdPhcUfEqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM3Rjks9RifLE0dLxircA7nK41IrmSYSD8%2Fg3y7xIInz5QsERfGR905DSuQaG7OBmUjwTeBQfxOPOGcN2OrSK12uN17ZGUkGQ%2FWzqPfdyhf7Aep3YS1O1Ox0Gv3DKaSzUpKrPTsDi4FLzXvcHo9v410j1ST50bWirefaxLT16OfU78lbgotXlIT2vDzN35bYJ9ByxvHgNRSvplLwNWaaAez0m4SiM5%2FpILzKv87v2chgmEn4vzB5Ud9N7KZEz5q3cJsH1SOXhwpJggJU25BnNylms8VTddJdWR8uqERt%2F5GE1j%2Bcb700Lb%2FlXwNBFgamT5Z90vRdfnHYyRQb7NYJXfigmc1vZeZgnfygJ9H3EIArEx3dKZEvklrJcZ6yQ1YUzlp2681uePCDFDVmVckJgWCuC0xUjf9gpUMtsYcNBfm95VTkomaFjUZZ8yIqkviPIsZUjA%2FqBeZHr44uwHlu7wbwrQnkuow3DkyPBSkAxFoivmRtNxL%2B7DRn%2BEb8i0vvI7MgQbblA51LAD4PHowbhUF6VV%2BF8ltQlAjKecUtvjylEU8wfptrSkSJkEqeLnMZ8L46Uguis10ojx%2B0EqwbbMGg3e%2B21r6LrZtP9b8L1oL0AEARtE6mBQCdgVVyUZlS7otxvyBu6mXD9CcJMIi%2FgL0GOqUBUW5oI4k58ci0xiScRfz8y2dcCQ8sZVn9DmnDPPhGCRMToUdUA9IE88i%2FlFuTXLKOdixuBmqGQBNL5ATS9%2FxYYjDvk203Gji9ZgyML7mkgIg4KYInqCZPLG%2FqL92JoxsiKhXnsUDGToGsdnu5kFZtJ6UptvMQw44qnrRWWukrtDEccGjnIHON1%2Fim9QBeKHKvZhLJtDqU2sgKZhGKYy4Nt4%2By9m3B&X-Amz-Signature=00c4770d12aa64a6b68f703c1bf98b5935095ec82d497b1ed63267f411d50961&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPMM45VV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBUhdpN4eu%2FSSIy7oTjgTQVWiWPTHIwd2RRIfeLbecUZAiAuFD0XNfY9X54ej9U%2FcNnmaN8jNWdKZUdor%2F21YA14liqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfFfpw8dF6fHdzPaDKtwDYivss0FgSCqkW0Utml%2BHH6rwZ8ubmdAPRZhyfK9Rpc36QXNlHyw%2BvOfy%2B1WQ7QzEQxOGYebKvbAuJwwIVxjD00DkN0w4PS488w4KF4y4Mifjgsu%2BxnSP%2B5N2ltXhgrxDkz7FXX428%2FNB6WnGEY%2Brjl23w3W0V9%2FJmnRNxoLLRctszt%2BXlfoBFCpKaAFnXJZ2OadwhOvD8IeuINZT1YEV%2FY6KjcoGSlWo9mKw%2BxYODsrM5uu46IWxcweHpZi8%2BcNktZg6ht%2FZnUe4P3rBfGZpUWLeL9CK6N8A1twX6HnLBHMeTuRGFU4yba9vR6lm7TqFb0wT0s21SvrSFE3km%2B1s%2B0V336dvv5OgBC3RN9gia9%2BJJX%2FALpNhFIhOcTeeErb7kVrQLhj9qKHIMZncnGQCuQiLbAzf3J6I3fIUV7jmhF8L4sbYYEZaKoKFDsfEqI0WzmmpzCNsT9S1ks18znrX6gmK7xbVbTj6WtEgybzp2CPgjkbD0e0AMUZWEGF6fhcjlyvyWsxiI7Ro8dGlz525Q51ZMcSFG5oQlTVNrNzNXXlHR385k4NC9ZOeAFoJRydN4aDS3K3wLAX0kYoDR9%2BybJTyr0LycrX7kYd%2FafubI9XnkOqzgUiPwkTRdJEwv7%2BAvQY6pgGRDSEN%2BUGOPAOlFVQ68PHKcJbLx81A52HHxntqWy%2Bitemz0hJYb%2FQ%2FrPSZIv0nB3MhO2HsvELFsBx5sWQN6mZiOv71ao2ExzPgCxRiPGQkOgDY1p1OfXdYkgM39hZPg5oy0VhNKAe5iScoOQvYIHDYtZLP28SRtbV6aaTvc6skHfzRabLAaVXZBKXUTWhBc7xoJgB6iHmci1mFO8WYi6S%2F%2B5ZFLDbU&X-Amz-Signature=c84a27a9a6b13b045708a7f5944a57a8691536fff4c49b600e32e855a6293419&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6AH63AD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICgrpUeIhLtPrpTSzDl0%2FDOxLEn41iFevN81iJt54rY1AiEAmq5sP%2BkYpBBr8fO7z%2FTR36KS%2BF1a3fENwg5WcnE%2FMoIqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCjI%2BKuupEjeAyaxPircA0j8D%2Bbjt8%2FxvSmg4DFvlTDuDbUDU6fLO%2BD%2BEmqusFEyMnqe55NsyrYRr9%2FC1pkxPuU7hWjLvjdn1HmmvskBVT8eVHbvNs09CcaZVQ8KzeDXfFoms0SACVwyuYyVk7ZPXbh3dtKek66pXGpuw%2BGWDZ3iCppbetP4Nba3vd4tedWuO3epP0Oy11MmSqKKcB6mBXG2KKKfs%2FrFagYmBrgPEWYwoNRN4NtETVncrakn%2Bx2tFAG3f9l7TJAuXX7c96dhKkkPyTLLO771n0b1L1aejwcOyPds5O9JDy2Of%2FfZ0Zyr99HP0XgCnS5hsJs2Ln98lf3us4udHsKB%2Fir08FnG%2Fn4MRHKtCzWUf1tQF1bj%2Bwf8ESREpM%2Fh1jg22vvg4epGq0mBv7dv4A%2FS5zAdcOekt7Cq60qXZcxWi%2BmusOrb6fgD%2BNjoSvaHFyU7gwPCtlEUJYJAz%2FCOw3UW8%2FodYCbLnDvmundPh3eqrKYyGHhmnq3tgoT2UcR6Oc1StkDnsu7np%2BEJJ9Ca4XeeEdo6c2hoOl9RItZkRb%2FYQ%2BGjVfYo8IvVazXKHqq2vuB448R4yVlQDSU9Xi1lPDO2Mbvc9aMsRquYZCCDpxxCAQuqAuijAkLqfc3q1niVsfsFFwrnMMC%2FgL0GOqUBhwEqZ0GWHyOLkENOLEKX4G1UzBScdSg76odbPCvHztzziGzG1yDG%2FZVwOzVheEZCLQV672x8cWYAsczcqA6gjlLCNGecKxvc2o756H6WNd%2FZBuribj%2Fw7wDQ6qcI8lgpAUzHyfmSPtC7Px5bKLYojInZ3k9QhJf8luH66ysd72HKuvedYHQ7gVia8F4BvSkUyIx5QYbL266zMeU%2FteZ%2BXR%2FnIiiy&X-Amz-Signature=2cd81aebb2e88f41161ffb6900023d9a0e72f1bc33985ed71ef04e3c26231bc0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLVT3EC5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIBzE0sQmDfKdHlK1c0ZQoEVA0n0OEapmjs2cmVxd8cLBAh9Md2980DSjwhDeY3pQ%2FGVGkrvjFm8iHxyl4HkNw4z9KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBr6lEB9Etj9oA%2FrQq3AMsWGMoKVPxrnoWZFV2Y1KWCpFupBx3jDSnW8tGUbMAcZe19T6Tu2%2Fr0nqyaJcHmhHBVfq4o4Lq1uRlKhsuNEhhkUh5PpVRYTzJF1hjDZwMjid1yPQv5hPIQ3Qm%2FP4DG0jYY6QkOB4WqTaea%2Frl4y2WXkz4ex6c70ULPs4dVEwHtDrQ59xoTR8IqTLTVh73LkqNtG3Slfm7ssLMoTMKCGzSlhUATCKiZRm5AAq0YOg%2B%2FrjCawUJv7D4CKDIXjv1i6GYPIEuBg7PsBSHDhpdITqtwIfg7ZZNxENoYK9Hr9QV766zsOuYsyFMYwLExpfta0eBvKGHQp5y1Nzvwg%2B8hJmNzgnbXdblkP9A%2BLUwt0ETvku2tZds52IImH%2BJ34tn84wb9w1REQJF%2Formz0FxKTzLs6jdVNutzsnbfTCI8DLQbvtSPcLkyDOs8%2F7OfociE5pIrkmXCGUgJp9B526aXfIgkVKOxtczLUGW%2FNvR6GfuZKtcWvP0OTl8OKXSkd0iYeoXLvrU5HSJb6RC%2FuoBqFH7uzDhWKFERKPSO00gePkG%2BlJV1j5aQV2%2FW2Kep34Lk0wPoQjOHhF48tv9sEh5O1cjo7uYe6%2FDBK%2BkCIaPO1p6COKrlinGPu7Ujj82ijCbwIC9BjqnASQ%2BLyiCZt%2FEn5%2FfZNBwuicmXNkeiOteGu46kldAwTpMFTsmDa2K6BiDutwGK8QAkhbdYoSYHHmHOS%2B7DH7n125fqnh3i78gpya8ABS4Bq9l0mvhruEywndw5bktbfaTsIbRy0XSKeqxYl9Q1ktMjyFxPDZSX6dA%2B7Gu%2BZB3e3FqIyci6gWj4osOy6LgBewonkxhQa6qJ7Zxloe8eHlAwCrAVkRde%2BD6&X-Amz-Signature=3d3108175c34edfac25698cfebf307b3493b861c5d7e029e980a2408ed493c85&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5QD244V%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAZ7C12njFUaPkvJCKGYWKsgVIpHVo0%2F1Irt4ST4N8IMAiEAsvgJD%2F5cRUGMMxROLwjC6I0jctOm%2F8ocJUbVc3lUa7EqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLP23Y5kAIId8AL%2FvSrcA8V764r3sDqdtOn2FNwLl3ngM91%2F5Y4kqFIrWGW5lMvb0guXlf%2FJjU8LQd0zBee6TJaxrMjWjKCzLQZiUuvJEryNcWoTZ5gYcyGDk4yEN1nY3kUeFwULQrWS9wYLxC42CFSUh4VaX%2FDiB7B10P%2FI4u6fljfe7q5m1uQvOpKNQasln3lRXsLiYgCX3QX%2FAVLWw0cUj0m0adCA7UKI2MLFExx0C2LOwa%2BXrfYoK0zFocDQqmIuRB1z5Hhl2gZDOE5%2BI9IRSwxsO5dt1wu%2BLPn9%2FbHdK2%2Bw4N2AN%2BOGkZTqlukM%2F7LkM6ly3h0qDibqNgMnyyL7FE%2BLtWEaks2B30l72FCWb8Ah4N83%2BmE39E6TDswbBrQzjuQhEQ3OrjLfbcd6T%2BMfUnTRCjY6Z6fIPro2nFD2tbHDXbHLfgIoiq6y4rZHa9SyL65wjF2WUHbs6DvXOI0HM3mX5yYkSJ3TsrR7QEMuvkycCa%2FcOilUjclGvbIafKeolh6uEjnuQVtVDRjIyzIBSwjKPxA20vBzydP9%2F55i4PGmKr8N572abGF740uhXxxY6WTc6j3AJrvEaMPq3cjzHOkT%2BZDdGfOiWwl7srHpVr7UuBNqGHF%2BXvI6UPfWjtIIQ%2FDTa26EveCGMJe%2FgL0GOqUB5p2%2BlPJQmHUeJByL3qHTJwRnD1cvdihMg5L6F6E4nIAuapWvDm98gPfSZ347Rdw9j9dSMbaIqfR8SiyYvkxj8DpvlGZIDaOvH%2BwVZJqemaVQliBrSZjHTuOVottU7I17Pk98261U9SzinK89wPhCGr6ZCMDpTL1jZLYJtENj0azxCoYlTLKf5dFwLkjaLHzvxrmx%2BurS2Mmuz%2F9t2f%2FCK782O66E&X-Amz-Signature=de80d276e062ee7c5b91a1971885a481122bb9f6d17eeaff104465d5613ba082&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOCIWME6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC2kzvMZgzyUTMLePBqhFXRF82dU5iIt0ZblnGlK8p2kAiEA3%2BQiEADkvg96fVfbVd9NIFJ1VOz%2BA%2Fy4HnU5ksw4RmcqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEApgplZwta3l%2Fl1ASrcAwmAOb7c0T60k0XR0ola%2BPkohDjhrhEyoWZQsf3MxX1Et6v0rYBlXVcSd1SmTVeuEHaAZQUERAdhwueHtYCAYq2pH%2FhEYe2Pf0ySsOVl1Q9TM1PCqsGmzNApCwxzliWMr04ko50Bxp3gj3ropVhTOwSqUBriUbL4z7Zosds%2BmEhzW%2BLDecOLt6ESaf5cTvIgoJde9%2FLBHSRA%2BDu5phUno1VWfyVeqH%2B3p7Wa%2Fh3oMF8uaCc2%2FYcg%2BggvhVP4Rc9Ops3lN1pxM218dvyEHNcWnADC6k1ABzn%2Fwi9O8es%2FGPHnO7KjXpTblCdz29yKE0zBunlWfLzRxzihvRDT4CwZ3jvIQ8BbRvQZOSfX8n8GNvll6rvDWQJ%2FPKhHGVTLI5EeB4dbA5bcDkTQeo3s9cW2JW9eE2t6aeQREN%2Bg4qTU8tXSRh8Oi5Nk9iaYyahUB9%2FVA8gDR2CzFk3sjJSJAXx8V3DnPxo4EZeOD0faYbpMhBov8P9ICYcfxsjGejtHEU9xxFwJsfqHjLwXrxDURHHYXLoZaKi72AWdiFUV9OZvXqcbLjhDvVE3LxHmRLnBy9q0naZ9I%2F%2F2kEW6M3E7GZ4M2bktLlkmB5g1kF%2BSJbidlZSAHTL6mAUpbfqWwQn%2FMIy%2FgL0GOqUBQ%2FbCdmo5RhR%2BF459lXg2CKdGBnSpOLKADeYvVuuHU%2FwtVoHhrIZOVhTCaNZwfEakyTJlJz%2ByxioIS4%2FAB5amsmrd7MQa5Verd2SlFG8be0w0DKTh%2F%2FoT%2FvyF0JqGqEehukSrlWLVI2vddQfmWVaFOyxax0bRuChucbqTfZAAzNBHjffFAgDfOumMM56tiN1ZiF%2FviPTIaKc4IqviOD1DML7Rg%2BcP&X-Amz-Signature=98b02316a2f5f6e8bcfae372aaf82a3796c235b38348535e4d829903829a3aa4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6AH63AD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICgrpUeIhLtPrpTSzDl0%2FDOxLEn41iFevN81iJt54rY1AiEAmq5sP%2BkYpBBr8fO7z%2FTR36KS%2BF1a3fENwg5WcnE%2FMoIqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCjI%2BKuupEjeAyaxPircA0j8D%2Bbjt8%2FxvSmg4DFvlTDuDbUDU6fLO%2BD%2BEmqusFEyMnqe55NsyrYRr9%2FC1pkxPuU7hWjLvjdn1HmmvskBVT8eVHbvNs09CcaZVQ8KzeDXfFoms0SACVwyuYyVk7ZPXbh3dtKek66pXGpuw%2BGWDZ3iCppbetP4Nba3vd4tedWuO3epP0Oy11MmSqKKcB6mBXG2KKKfs%2FrFagYmBrgPEWYwoNRN4NtETVncrakn%2Bx2tFAG3f9l7TJAuXX7c96dhKkkPyTLLO771n0b1L1aejwcOyPds5O9JDy2Of%2FfZ0Zyr99HP0XgCnS5hsJs2Ln98lf3us4udHsKB%2Fir08FnG%2Fn4MRHKtCzWUf1tQF1bj%2Bwf8ESREpM%2Fh1jg22vvg4epGq0mBv7dv4A%2FS5zAdcOekt7Cq60qXZcxWi%2BmusOrb6fgD%2BNjoSvaHFyU7gwPCtlEUJYJAz%2FCOw3UW8%2FodYCbLnDvmundPh3eqrKYyGHhmnq3tgoT2UcR6Oc1StkDnsu7np%2BEJJ9Ca4XeeEdo6c2hoOl9RItZkRb%2FYQ%2BGjVfYo8IvVazXKHqq2vuB448R4yVlQDSU9Xi1lPDO2Mbvc9aMsRquYZCCDpxxCAQuqAuijAkLqfc3q1niVsfsFFwrnMMC%2FgL0GOqUBhwEqZ0GWHyOLkENOLEKX4G1UzBScdSg76odbPCvHztzziGzG1yDG%2FZVwOzVheEZCLQV672x8cWYAsczcqA6gjlLCNGecKxvc2o756H6WNd%2FZBuribj%2Fw7wDQ6qcI8lgpAUzHyfmSPtC7Px5bKLYojInZ3k9QhJf8luH66ysd72HKuvedYHQ7gVia8F4BvSkUyIx5QYbL266zMeU%2FteZ%2BXR%2FnIiiy&X-Amz-Signature=3742cd52d6f44e09b9265bd1fad06aa830e0ea2af4b16b14bc35071d05cfccd9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGH5LXLH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxN%2Bwjtl5kPlPUeGyWiUMzHFWfrIhNOofIS3Nnyh6ZqAIhAPFI6IWmOntUbL8i%2Fp9p%2Ftf7TPcWUJ%2F1zg5EmZiBfNZnKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwwFKo9HdLzhguFUXoq3ANBKGYauFhw7YvTaBtEcXfPFmfXT99PlXtiEG2OGzt9IW5GBOq76jAcjI31zimarhQ%2F%2BTiUfr222e9Qou3uOMzK7ksx242vbR45DNgwx%2FSfjeL2DYdw0PPlAKQpnxllzQN4kzN%2BAMtUoEJkQf%2FTuHEIFhsK0tjkJiaYpf1Wm0yWoJ3XG082nbXPiRzBNJTf3Yy13YpRh9PBN7%2Bo7CRNNcfv3l9RynMZqsQYEg1VoQ8hvDFQRj9Oii9cF3LciNp6mhE5mxYH%2FHH6jZOPvmniZoFVQRaaUjG9ISCRrhIy8GYx0VZVNVwjJHjzB3AZaZavbK5Oj3Y4dUKeENMrUQKOGIgxORXD0MpJFrlYk3Es4HxyMyqs9vgY4TGpINrQRr1pQlhNeezwwt0JU%2BvXrWjfUb2mELjepx%2B9IdKkMei0rWV2CqE5%2BxHC%2F8i%2BNsnwWCL%2FVyXUe4%2Bapgo%2Bxw3ZcgHlYNsAqujnj%2F3Ybp2yx34bu4QapPMwOxLFnJdFYKqXgdef7bq1e34M1ujsgF2TlXnEn7X0kgzFUV1kWw8hk5Xzx4rmhDd1tsd7zODK%2BCIepfzaNI80aWQjFt66RAh7tw0XyyYnapea%2BYotRkPFmAXMQyBoNzS6SUnJ2ci7zkwgtzCRv4C9BjqkAR%2Fl4GLXGn9Qys5NKL8K5ayz2K2NP9%2Fo0M9nxLaBbtqY4Ftq9n7NYbj6ImHpPquQdbQqocWCqYLp78SQp%2FC%2FOtwY6vSli4Ax6z41V4Cp%2FBW8yiKdFl7VMAA0Wlf2avUwm7I58936r90zaEEeIQcRyiZ7LgJ3YeSKhJTQaOFGBwXsgEt7%2Fs76lflpz4xfbmTUKaCKUuSCosLS%2Fi19N5EnBoUxlfi8&X-Amz-Signature=b5d42d9b5165a3aba7e1e9eeb7c186d8f847bf7caad974ecfa5f5f0f8b41aae4&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGH5LXLH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxN%2Bwjtl5kPlPUeGyWiUMzHFWfrIhNOofIS3Nnyh6ZqAIhAPFI6IWmOntUbL8i%2Fp9p%2Ftf7TPcWUJ%2F1zg5EmZiBfNZnKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwwFKo9HdLzhguFUXoq3ANBKGYauFhw7YvTaBtEcXfPFmfXT99PlXtiEG2OGzt9IW5GBOq76jAcjI31zimarhQ%2F%2BTiUfr222e9Qou3uOMzK7ksx242vbR45DNgwx%2FSfjeL2DYdw0PPlAKQpnxllzQN4kzN%2BAMtUoEJkQf%2FTuHEIFhsK0tjkJiaYpf1Wm0yWoJ3XG082nbXPiRzBNJTf3Yy13YpRh9PBN7%2Bo7CRNNcfv3l9RynMZqsQYEg1VoQ8hvDFQRj9Oii9cF3LciNp6mhE5mxYH%2FHH6jZOPvmniZoFVQRaaUjG9ISCRrhIy8GYx0VZVNVwjJHjzB3AZaZavbK5Oj3Y4dUKeENMrUQKOGIgxORXD0MpJFrlYk3Es4HxyMyqs9vgY4TGpINrQRr1pQlhNeezwwt0JU%2BvXrWjfUb2mELjepx%2B9IdKkMei0rWV2CqE5%2BxHC%2F8i%2BNsnwWCL%2FVyXUe4%2Bapgo%2Bxw3ZcgHlYNsAqujnj%2F3Ybp2yx34bu4QapPMwOxLFnJdFYKqXgdef7bq1e34M1ujsgF2TlXnEn7X0kgzFUV1kWw8hk5Xzx4rmhDd1tsd7zODK%2BCIepfzaNI80aWQjFt66RAh7tw0XyyYnapea%2BYotRkPFmAXMQyBoNzS6SUnJ2ci7zkwgtzCRv4C9BjqkAR%2Fl4GLXGn9Qys5NKL8K5ayz2K2NP9%2Fo0M9nxLaBbtqY4Ftq9n7NYbj6ImHpPquQdbQqocWCqYLp78SQp%2FC%2FOtwY6vSli4Ax6z41V4Cp%2FBW8yiKdFl7VMAA0Wlf2avUwm7I58936r90zaEEeIQcRyiZ7LgJ3YeSKhJTQaOFGBwXsgEt7%2Fs76lflpz4xfbmTUKaCKUuSCosLS%2Fi19N5EnBoUxlfi8&X-Amz-Signature=b8fb93c514ab389d9df6edc07578bd6a95ecc1e3d1f07dadd8f6bd51936517f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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