

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFHUPX3U%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIFBC6Fbx7i7%2FLH4Mq6ilpdMZakgVFz2SkVTHDhQYRWGgAiBJVjRmMWDr7Db5fLQrqy82VIOtQYGBRr%2BuhMVICiWNAyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMabZimvGox%2Bh0mLRkKtwDofT8NGAcXhBlcCmRbFRgJTb90WiyOWHPamOyUr3GDgZefRSiYYVkZYe9QpJT%2FJUiTxL9Y1bTmdN2OkfrYx8%2B5WMbTkGsA5HUDCHDVM826b8Sv2nOvvs%2Fa6tWW8FwMtTEi691qERvrPGf9P%2ByVTWKLOk3cAR6FeL680UtTVaK3EuDud26cEk6ST6TVGj6zoCl%2BOTxFDd9xXrdEQKnlwJS6IhVWGznIsY3bIyHtqzDOWqqKyXWX4gjdPudpl83Qfe9BsqrE33%2FfZqI4khduuvdkxirZHokCtqZiVO6kfvbwSwtHHqXNCRsyCe6fymqSzqc0Ltg3jYe%2FsyndmdWpA6zJzig%2B1htMXoc%2FD2NMeuyMTJ%2B19%2Fo8acxv4ofG31vfasd80Fdgo2IrkrQPluDRyzj%2BtdjsG5cWHdQtbMWxD1h1qhTFMUOHXjUh%2BdudsqHme%2BcCFKgPBCN25ECxqKacrdZbdI2WgCWtpiR0cBAmEHtHVbXAdskWNv9U3bTwySqO2sOnV4IAmjZPsNXurKmJ6LfCfbAZ8KNiLzspmTu%2B4CWnicBthEMZhMReb56HFcM5MBBpx3IqNis35plgnMhYux9bzOrotnZD2iDMd8jR2hoiaAH3xvQlsOK15CHisUw9I2cvQY6pgEDAHsi9J7zVKli7q8k%2F0CvbfB%2BIrNDk%2BUR1DdlApEV6SnDEPF%2FVQVj7aCpivUb1BrsgbXxBrBXwOY%2FJS6cxX993%2BGYtG4OY7cdknYkt935RmaJXci9a79v9bkaqdFSWlZ3fWuNEyNk%2BMtZ5J9ii13KtBuVLK0FxjJekAwOfW%2BKSt968qIHVHfZiVDtJucOsXt10X4XrFLvM3RJS2FLA69DY5Id7kbe&X-Amz-Signature=5651b239a707416edc2de3892ff9b021901d7743633c16995881dfc4690fcef0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IGD4SAR%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIEmqgHtkOIsroImm0CtmXZ0N9nRWynfjjHlRKRW6p1vIAiEAkvjsK271aG13%2FSmzTl4Ge%2BIS8%2F8ovP6Fkgdfs1Oq5fIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKVOipbl1p0D%2F6TI%2FircA%2FFnB3bQeqRNIoZpfhoIYNEpqsFtvnyf6kGmZNsLNEcczwFkuU9PREG1SthS2vegekmFTy5Z7ryZzbHi0CJZNWW8CCy%2F4V8oeI3LuhRaw5Mt00XSGUnEiys7Ze%2BEw8vQCap2MmyNNf5WkQ6q0L1xJYQjzaQRbJd1ZJYta3gQFFuDlzwG%2B7dIVEqc68uaM49uni1z%2BOW6y9Mn%2BfwpPybUzNukzIekrXxOT%2BQJA4paPzaXT8%2FGT4BT56kJ4%2FsrsNGmo0Vm57KLHXPgOc6rAUEekrEhSfRHlJFzJvd5lu4DAmIzxXlcJp4v9mwHUkrj7hBAqqmuCG89C3LlWWi%2BuVMakDR0xLUs1aT8E0YSAaevz3lbPU5ZsEr0lOSdlTbqCj3cEcMZgALAGs8ydRPl4d7AE%2F6QRMA%2F8%2BtgBuZdvWdy5mqNEEag9fzKsSa6ti9zQ9m4usgEFboOvwUg1lZzC24Fja0siuc8IKmilgSvSipqQjTk103brYgeQ%2FB0czcOApuUZaZsi5wv%2FL07rOgyEvlJwmmNWJslTpikLdLllEqvhx9Ufb9wIZUgPbKnGUGb3KGQ2I%2FacgExsmvStRIxg7SCA1GDPv7D%2FL5zPJ6xRetk4lENJdMgXw%2FrkzwLJwdAMIqOnL0GOqUB5JF%2BT7jWyWVAsIT2eG4dWaajrXqpvNz5I8%2B2%2FoONyEQYqc%2FpTytRa5VsCNYlxpQuT5WfKW8uyAXKOo2pLIxYCE93uq6sKVVU3C1x2x9AG%2Fa8stApdFjOZa4ExKRHlA8ofXGqgTSlkCFP478jA0DRluUQJkd%2BQJdyNP8CG2o1vnpD0XkZT1q7AqzTMGrpInvuGPWhgTczoCRgNXyPWmfK6lD5IsgA&X-Amz-Signature=7a507965cd49c11ced2e2375fb09dad0453cbbf7e690613452073175eaf6b205&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L5HR3J5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDP7qdl0eU0sMmwpSVzmQCkqec8oeX1pxWGl0hm7EVyIgIgaSHSN4ud1mVWnwWV1sE17efeWaFpfoLVTFYWgEdBwZ4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOE6s%2FXOyzBPz0EuySrcA%2FUud2%2BhNSuowtdAz5yWxc6ko96XMJGKo%2FRA1N2l29oo0lONqOPu7oYKNMRPmLlSKx1zf2f0cR%2FHYk08zA3xqx4LgpWIumX%2BvL8isVOTTQrq8oqbOydW0ez9gKnaGPyzTa3WBY3qI3%2BLbShxAgR3IkfUvcRlYXugQAbEDgHlQ%2FV7hBFOhFILXvrU%2B53CnvAgL%2BIq9WrDIgzMhZ23ni6wuT%2FbY17YhHWNazMQlTJ5GZfpT7gAEuZlPoXG8Yj7xG0vwzNGPAPU7Q%2F4r9UGzDcTwGqSIBgxB9x7ZoIugOYkzbfkug8svCGlLgcAPSWI6IIzdhkcz6ki5uaZsDQ7H7DNPszOxaCt0c95bhhiWqgxWxlxjl6Hyz600dPkaaTnFoZX0Qd8NXM3Sw88wTV1oZLd%2F453ORID5nSbRqYT4GL9iDl2QELrBQrdRMax%2FpEkHgufJZTJxZPkKIeF1Yt4sLxyjNYNe83bALMACErtDapX7N38sBmppck%2BffM%2BiyWEJj3dT0iGV35jGkIspV8jEs9ovnYCNKXMmIXcUl5nVOHNWE6bmcow21yycWWxH9c0VIkcfGnT8cUfCM4HI4fQLkWSfJyQ%2BXKl6K18d6K2jwqVaUBR8Bd76dRpyjJda7EZMM6OnL0GOqUBHKUbZo2IxfXGhDC2Fl2AEByBzYoiiGn7nvKUVXPHFDKvLRO5UA8goRTSMN%2F33wSduRwGRDSaXZ%2Bt7R7TwmudfLkNZTvTLH%2FzlRGHXf2vB3j5AGJAfYxPRP%2B%2F2iWQgXxE6PYe%2BSYs%2FkGNrFnZsDmxM6rCRFHEvw%2FZ9cKHy96rD%2Fe4HWPoNNDWopboBSF4clMvJR%2F10Is20XpE%2B5a1lbwNV3B7GI51&X-Amz-Signature=bd53aba16bb8a236a091a0b0f676a35d26d76ca5ba94c18960bc92cff11a2df8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3XHEG3A%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIF7ASy0tSBVOS%2FWdCHneuZ2uTZWzyD935Ilaqg3UYfLvAiBrdTEoyQj1px%2BJNt6rFlD92S9dtlwDvF7meZAq7A9weyqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFcnO7xFRrJOkNKp4KtwDSqjpDyc0ohbQry%2BtJcm%2BVsZiFSJcB0i6zUv45CMDDoUgd5PJ5VSg68%2BLe8GVKAfxlhDiofVQxn6iiifilM0pxdI9SH4E3kb4rH92JyYg3X%2BNB%2BmDkelNeHDCbn3c2puoNLkbss6TmZoqOFgunLSjuHdqMkuGv6MJEdz%2FnHwI6gq1Ea9Yu1lFBRQm708cSdBTxBP%2BcdCHIKI0pLgssfwtrBAZe%2F0tbwoY%2Ft5mgvaRHOoLXFhLnLI4X0Uyg87oCyz3KCdAHc5ay%2BiOORJXyDINCbwhA0aAcuErUhGuklguokOI95zYR1cIWc9nybLKh8vKRiJ2aoPq3n%2BxcfccPSsb4P8wVwMsKk0tQSzsbdjAFBbVHlX0NuhMZQn2cwVdWXuLg0edDzcvUA2SQvGlpl24%2FEIlXEiy7pQOXnJrAs4MvaXHvwuA3cmzqLYeZU5nHWfWJltL8pQwUXuK%2FpFg41BcjrV97%2BWbv3zCAnElkjmyDMwKiEk1xmgYAk9YDqttQltUCP9%2FsFMiSNtK80oFx6A4cP5JqbLM0BJhKWZ1EgHw%2FXeQwiNe4viBSz%2B1cijKMlw1rUVn8vYKilPxbf2HnG11czUUPqxL%2BzsURmso23ivZzCd2gR90uwNj%2BIaigwwiY6cvQY6pgE3V2gIy5ycDpQXc58PqAv9O7WdTvc%2F1Oh5msDJdXKoPan7QYmjOnpYjehArZf%2FfecZET5EYlcxG8ocjTtErFlYUtUMJ%2BO2t%2FRn2vZy%2FKOBDPpOU3zK8NajMMX8GzaqgeHgicXHw6zEJLQ95KzDB3IBi%2Fu9C%2F%2BI3Gtuy8V9vI01Aiz8mR3BIfKwmX3LxIkJA5cckRQW9XJDW1qXTEQb%2F4IixMs6XNIW&X-Amz-Signature=a7194870bcdd526a4ca0ab6f35a9fe0043f170d420a37de70ec2dcc0743a9d59&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LHW6UGM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDAERFomktFLLDtTcXACf%2F2ATBccbnNQ2ReApuPBG0rLgIhANwfvRnwrpORPCoVy38bpxKdf9K14gWpsKEwAM3Le0rLKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyQFefFp8OOHB5zSVEq3APbI2y%2FduLea7akVHcySvBNzvuzTIdT9UGbVJ7ANhHX2svYIpu%2FJ6ay4JbtLY4qtu5F2QXRXsnoX3ZtUMmKpfAN3haUhK6nkcHwfaY1M02K1UAkGXTKqhIaKb%2F020X%2FE3XnpRfh%2B4svjcENpaDs4eL2uJ2Ac8xzY7E1qOyS4m2H%2FMCeWRcXnBESFQDWDsKasVFqVIQ2g9PvdnW4Iy10DvNlhT1I2hB9HxrEb98T4UXdB3lVVzWCI2K4sy6J4wWB%2Fvuy6jGmmCn5g%2BuC4k%2FNxg3yj8pg2%2Bo8N3m%2FDONGQltk1hE4sEd6SjMKtLMt2cz1eVrunXae%2Bt9LhVK7PrPXMTYgVZvUcupY5W1rBOqUvdD%2B%2FqLLVUf3Pqe8T6engk%2F6hrNn2KO0YPxZXmPSy3Eq%2BlKCRMfcbWTTsK%2FygO9aUVfRYQw56wfaLzPWVeZsqWahWGJwHg9TWgY%2FNoibDdQAAvDEyUak0YlDWZdg3%2FMdRVrYsJpmTGyRMTZnMTMknckAavcqPQrooxzE8LulOhDTMraH%2B8h%2Bqau5Wdw36NVDww%2FF8zTOO%2BGILe5CxruvfXoUb1TRTt8fLGt%2F401ps8560%2F7mIiN7FJRCF%2FSWxkg9LowlqsOWVsigThx2L509ZDCtjpy9BjqkAZQGAD6engltMuBG2wWYLdeKMuvtVRNLPoikfwhmC00Q1lIweqdLXmp5gvPMH8%2BndpDRbz%2FKBDDEoyBSVErtCUCKRV8DYF043nTNVUyT%2F5lF5vHijCgt0iNl582%2BOFjpiXZrqV0ggrYraxTQthx9V7FV6zTv2HpJFB5TR5nkTDiMz3GmW02J8z424iEKmoZ5GGCPP4Xje2v479qhVjV3Odzas%2F1p&X-Amz-Signature=5dae01149307363f55b9925f019961fa7f60a742307db4dd888bb7803893df08&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ORGHIVC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDS8lLHNzCiWUOdErgyPMSU0ba%2ByB0KtX1f8ksBgIfLwwIgInAxch4GQ0y96QYLX%2BHg%2Bp8PZNWEhuOn5DAHCwzNoEwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFTmt4GRhv0On7ejvircA8lPtvoWRrrb32qVoQn5GH7CoAkIiFjNEf4yi4%2FjnC4Hx%2BJzr3oAWQsuWfuH81k10Nw2kmDqrBZMwaMQDxLoEdC97gfEiVC%2Bw7rIRUIkYIGcgqFUb%2B9yVuaumyqNg45QnLn%2FPgs7kiNEiry19Jiyp5oVzeku9mtv1PLT%2FxxrLGdOihdyP53zllr0wBrU4pVliWGj3h%2BGlniOj%2FJKPe%2Fn14l39hNVNtHzVmFYsAI06TIU0gKGbbf%2FMrA25IDsu3rkoOo3KdAFnfS5g3s45aJrZL7HurkU%2BZERolb01miEjfRoz4uH4AdsivwMBWk%2BpYNQXtIn6EtJq%2FVDw1XpVe0kdsvTpiSO2PxUzfJES1poQ8ayZBxxKE%2BYXDVq7TUWvBH9zYrQzah2nuDej%2B6uIzaA0Ju6%2BqikMtjwlNSRw1M%2Bf23XAQzGeoNIy0F3oUesVszHOfvGzGrKqwIXrdKw5M0qIXTbAB7YVdBmIJwGOG8hcBrVuYzVmIHZt9bAc0pOVYJcGg0zRj9Vq88IZMgquVT1af6UUm%2FIDZ%2BY8LeuK8Yc8UwBgtezEU7wv3jK5%2B4OBbwTpOgxWYFxeELzhRLjC9SD6YFI2ixOWUnLmwIvpj%2F%2F23m5aHNocf5kAczTcYOEMNSOnL0GOqUB%2FoL2Xbeop7gNW%2Fd1oUxBiZ%2FGgUitMhosFnqDMX7wY0Mh1b4JOXjkbRTmeKtOdOBajfd%2FDq%2FhJCwb41VT5TUAylzwvpWOmYIOb2TSKnx3d%2B5Y%2F4rUS%2BDARf%2FzPmBAOy%2FtVgK2ywHlwTdEtWYZZnLKDxEFQP3FUha6CLoxMkw%2FD8mO9U4jZM38J8BcdDAN0Yb31M9ZpUCorYdOc6I8CUGkvR8cAfOW&X-Amz-Signature=e0b6d110039f64847a67c5386bf805b7e06b6aa85d9c1fce41bdae0d48f66b87&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSROAY3I%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIDjl0JVlde%2FgMW2KqWoMUd7EB0M3eAfc82GgngdJZpQkAiEAyaRdkwfnFSYrza4gd8GZtcCINToO2pC8%2BNIkCXGsP6cqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPtG%2F9XsWWEMeKgLGircA%2Fpld%2FkZ2REW3JzaUlYT2gSx9rXCQwa6izZltj01GmegZ1076i7YokvUVMjF1jNOWNN61FFFT%2BMY8CMqK4HGE4ypgLvgUi8wl3BzEFqPb7pVs2MDMhOTOQPz0nyltUNr4Fa5PpcPVCiXlBE0Ny7I7Uaqx%2BPWY19rkJwlohFcTZcxnD2wOTTCQvX%2FngSEGgAUws4AubW6x%2BA5hTQAO4azcEJGnjVlJ%2FcI7loOafLtTXyWAuhpyi47n14%2B5fkrS6rr90XOs6r1uBlOwTsxw2O%2B9ByLeaf%2BxoEYyxdvaUDxw%2FHv3Dybh%2BTgy%2FVOovTFpB%2FKeqz6Obj6AlTU8dEYttU8HSwDbBgZX7adbNd9QeHmQWPSV4EQzypmJgs%2BWY2nzqzDCOEivWRrxj5NVo3DVgFwJRYoumbz0kHZZ6fhCDv2%2FrYD%2FEfcMAJ%2FqEiJQ5mpaCLT7bKppBEDiEPmqTuvQUuzppcRRe48fPGiZHyryznGYs2e7%2BM%2F650EnyVXefFlcubUFDBhPwtLvktzTsQNZuGRwYaP%2F2UAcCICygig0j0IIro8MgbX2BHjzg55xLDQhPPdPvdH3Y%2FYdhV7q9zVxALcDcXf1CBUDy1NOJuIn3q05ezxOqmiRDhkUJoOclwGMM6OnL0GOqUBwcLI7c2WnlwBNY5V4Tper5iGlARGNdSOKeq%2FAlnyTZw1Cx4OveclBKnb9qCiioIji2Nl%2FVmNI1xt%2BvVch5m9QQmnxZFoBPoKuq1x2p8srAYKoZfJRFCj6F1JWNq4GfqJaf4ITVzVZxZyWVv9QpGXopr0VumXuz%2FYGWp%2B7k%2F%2B9QpWPzs5BDOJH%2BiNRGdQq0JWasVTGJWLogST28o0d2zRjJuaY43X&X-Amz-Signature=90c5d062bb887448e3520c00bfc2e01430a195bcad49849368693c14ec99fcc9&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7IAPZXJ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCCXhcDcJKDpj0M%2F7SRI7paM6APq9ELFlqeQ5zX%2FcaZYQIhAM5cMQFHUXtxRAjWlA6Lw1I2uhoMBSeuMewWAXoAA6NOKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2BcJFEr8SKkVSmPRcq3APfTQNromHM5ZlwNozBN3llB3I7EzMO6WNvgB5xDJeBsLCoINwhMe%2FfSn2ZKbBLIeLdNExQZHzz%2BbgPBRsyA0wi32kzvH6Y5r2smRzMVYeQkxb9MYgpMQt3IMkE9%2B9Bg1cR3LlXQNNK1tYJfQ40O2p64%2BHdqsmJEb8thxexRRjYDXtaWzbzy%2F2ZP94AWnte9pmgiMoOujBv%2FR%2BjIQl%2BduZkWK5pcxlA4oofQLeitOIkLnTJzU1io2fS0HaBzMtj0fA3dHA2vgjHZixLYc7qeIXOEHLAHVBqPLQPL1t%2BWs9nKgeIhtO2ZMwG7mq4Ou85hmfHhmToBBynN2DZmvZm%2BPhkjP6E1FvthUC7cnd8mlPWXp3VWGUuZtMIBf4W74XPZQ2zLxATYdlhybxehLAuFQDiQlNDL0%2BcYijIKrTUswbbo7PY1vim20eZ08tgrYGM8zNLE08VYWb3JBmb%2FgpkPyyoFRWLC%2BBkFNJ8LrwxdRNJ%2F2hxYJx9HkcwM1vVXyLEgFNFnQHJmKGXybYzobb1I3I2Y7iUnsWf6OC1DnXtsfgWdVUasrm1a1Sr3w13cD2Gt3BcJmBOaeRQJcpPI0E6TQ7QJtJNLFhGICQq0cQJpM86JL7lxZ6ACf4h91EtzzDbjpy9BjqkAYhOlUWhoss2A8qHZZQRT0BLsyDYGzECKvGb0w2jspOYPD%2FmjX0PgxsmTHkE71FjzqRmTTx8NCFovI2rhw6qUAhIj1nJ9LzsuVX3MpLmhxUtEs%2B1nQxBsAxlPlAClvIPMV9Axc0SiMc4Bd53Eu5rO43Y3Cqn5bRXdk9j%2B2W%2BW613hmvprXO9o7z8vj7lCHdTmtHI6D7pIXjyvMZRZG%2F9%2Fs8N0E0q&X-Amz-Signature=ca1dd9092f42ff23fb005b85e86ff05086e549cf210d4c461ef4c49ef582ff20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LHW6UGM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDAERFomktFLLDtTcXACf%2F2ATBccbnNQ2ReApuPBG0rLgIhANwfvRnwrpORPCoVy38bpxKdf9K14gWpsKEwAM3Le0rLKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyQFefFp8OOHB5zSVEq3APbI2y%2FduLea7akVHcySvBNzvuzTIdT9UGbVJ7ANhHX2svYIpu%2FJ6ay4JbtLY4qtu5F2QXRXsnoX3ZtUMmKpfAN3haUhK6nkcHwfaY1M02K1UAkGXTKqhIaKb%2F020X%2FE3XnpRfh%2B4svjcENpaDs4eL2uJ2Ac8xzY7E1qOyS4m2H%2FMCeWRcXnBESFQDWDsKasVFqVIQ2g9PvdnW4Iy10DvNlhT1I2hB9HxrEb98T4UXdB3lVVzWCI2K4sy6J4wWB%2Fvuy6jGmmCn5g%2BuC4k%2FNxg3yj8pg2%2Bo8N3m%2FDONGQltk1hE4sEd6SjMKtLMt2cz1eVrunXae%2Bt9LhVK7PrPXMTYgVZvUcupY5W1rBOqUvdD%2B%2FqLLVUf3Pqe8T6engk%2F6hrNn2KO0YPxZXmPSy3Eq%2BlKCRMfcbWTTsK%2FygO9aUVfRYQw56wfaLzPWVeZsqWahWGJwHg9TWgY%2FNoibDdQAAvDEyUak0YlDWZdg3%2FMdRVrYsJpmTGyRMTZnMTMknckAavcqPQrooxzE8LulOhDTMraH%2B8h%2Bqau5Wdw36NVDww%2FF8zTOO%2BGILe5CxruvfXoUb1TRTt8fLGt%2F401ps8560%2F7mIiN7FJRCF%2FSWxkg9LowlqsOWVsigThx2L509ZDCtjpy9BjqkAZQGAD6engltMuBG2wWYLdeKMuvtVRNLPoikfwhmC00Q1lIweqdLXmp5gvPMH8%2BndpDRbz%2FKBDDEoyBSVErtCUCKRV8DYF043nTNVUyT%2F5lF5vHijCgt0iNl582%2BOFjpiXZrqV0ggrYraxTQthx9V7FV6zTv2HpJFB5TR5nkTDiMz3GmW02J8z424iEKmoZ5GGCPP4Xje2v479qhVjV3Odzas%2F1p&X-Amz-Signature=3f6047fec1b02d76799b867d4947273e370e277adad8f69dd4619d1a34ad6e41&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKSKO36U%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIHpUfwLblTryMjBMIguqRAlF0y%2Fpd3iEnboy5KzAxk%2F9AiACW6jjBeYJWz7kNxf%2Ba%2FDpwwbyedcE1qlyBmUZaisexCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BfK7oVs7qhPUJkZ5KtwDrSbd51uYvYVP1t8778eFgLd7gMhtjoRy3FwV%2BQPu5eOLedWx0oc%2BL4XVTG1TeefNI%2FHdfVkmGSKmXxKpolJvlyZEAs2bPdOoJ%2FEPcnzRBwK5wXHcLjyV%2FgRmG5imzysEZHVlXOV8hQMocO8j6zC035qhXCJQRhbBF%2Bxup2cnTeV7QX4saG8ezCw8b6ntWh%2FUG8WyD9uUA85uELjx%2FEHK%2Fa8WWLfPF0K6y72tGlf0yTd8tZ4EsrJ0p%2FKKl7wfcdUh%2BR2qgBn9sx92D%2BkR8VwbauZYpUj0SiSKV4UdoF306qfSvhF2%2BrrFe9hNz%2BkMYknLEkno8reLXEFTJGu4vydKQgVExJ6DlttAJdBXz%2F5LeLlN6ucate80zkG5zKNzaEGxze3O1ltcEzhVp%2FlD3GUTMgKCWwbQoQs1dr%2BLUqidvoyj7r7eWygfDoAEmZP1GTmcU%2FjykITl0J2JekOS8vDLqWm7VuDGI2WQ%2BhVDf1vTC3b6WEHKCkNjU4APNnJnTGCtJw2yjKxCy6d6OA%2FQWjiIFAkXfdtKOSngfJz8NBZZL5COmTs3ZZytB08gHvEO3MilUHiSKPt%2F0pJTdAYw9g1CNGqpYSxxuIrlWRoDhnEXn3kh%2FBGQ%2FSVta20S4pcw6o2cvQY6pgEkLjvhCel%2BrfzszIpER6oTi4q%2Fp25KYpsjnlUIPVW9twq0Zkz85dBIGWtcIb37ZuvPt7S0HAAtV8DUZ88CS0x2LzXmSNvLrUDlpB9YR%2BvXIMTUfJdbNHn0XBGf7A3OIDPp116kchfqHOO3I%2FJi%2BS9873nM7YIFq9hRgLcWVMECV57xUaHTXBkEmBmsxLh5kqyPz%2BG5rkBaM8AXQsXYZYi33oZP9xHH&X-Amz-Signature=3412e82d840b69fca0e5fdb46de9e086c0d1243810947a4dadc0f48a32985584&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKSKO36U%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIHpUfwLblTryMjBMIguqRAlF0y%2Fpd3iEnboy5KzAxk%2F9AiACW6jjBeYJWz7kNxf%2Ba%2FDpwwbyedcE1qlyBmUZaisexCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BfK7oVs7qhPUJkZ5KtwDrSbd51uYvYVP1t8778eFgLd7gMhtjoRy3FwV%2BQPu5eOLedWx0oc%2BL4XVTG1TeefNI%2FHdfVkmGSKmXxKpolJvlyZEAs2bPdOoJ%2FEPcnzRBwK5wXHcLjyV%2FgRmG5imzysEZHVlXOV8hQMocO8j6zC035qhXCJQRhbBF%2Bxup2cnTeV7QX4saG8ezCw8b6ntWh%2FUG8WyD9uUA85uELjx%2FEHK%2Fa8WWLfPF0K6y72tGlf0yTd8tZ4EsrJ0p%2FKKl7wfcdUh%2BR2qgBn9sx92D%2BkR8VwbauZYpUj0SiSKV4UdoF306qfSvhF2%2BrrFe9hNz%2BkMYknLEkno8reLXEFTJGu4vydKQgVExJ6DlttAJdBXz%2F5LeLlN6ucate80zkG5zKNzaEGxze3O1ltcEzhVp%2FlD3GUTMgKCWwbQoQs1dr%2BLUqidvoyj7r7eWygfDoAEmZP1GTmcU%2FjykITl0J2JekOS8vDLqWm7VuDGI2WQ%2BhVDf1vTC3b6WEHKCkNjU4APNnJnTGCtJw2yjKxCy6d6OA%2FQWjiIFAkXfdtKOSngfJz8NBZZL5COmTs3ZZytB08gHvEO3MilUHiSKPt%2F0pJTdAYw9g1CNGqpYSxxuIrlWRoDhnEXn3kh%2FBGQ%2FSVta20S4pcw6o2cvQY6pgEkLjvhCel%2BrfzszIpER6oTi4q%2Fp25KYpsjnlUIPVW9twq0Zkz85dBIGWtcIb37ZuvPt7S0HAAtV8DUZ88CS0x2LzXmSNvLrUDlpB9YR%2BvXIMTUfJdbNHn0XBGf7A3OIDPp116kchfqHOO3I%2FJi%2BS9873nM7YIFq9hRgLcWVMECV57xUaHTXBkEmBmsxLh5kqyPz%2BG5rkBaM8AXQsXYZYi33oZP9xHH&X-Amz-Signature=14b01d5a0f3c838cd6786dee910ef16e96bc264c86c22f947ae2acdabb1779d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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