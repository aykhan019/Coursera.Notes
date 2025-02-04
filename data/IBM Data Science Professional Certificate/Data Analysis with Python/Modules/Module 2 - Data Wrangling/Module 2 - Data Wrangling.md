

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQVZDHUF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDWtKSwOqiw7iBDHyQE7wFc9fBODggbmOOT0eRrUHIquAiEA%2FAKP0vK1%2FQhPU8Gu5hfPbcgL7RSeqwgXTzEjZn3CNlUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDBYx0XtxPuZ7ANMsXircA3XpCISWJoqY4eFb0RY5nrwNuh%2Bsfr%2B8aaEAtmfVIdtAX1oEf14XY43mkpaZreRLa%2FB0ttI%2Fx%2BJuGO8pKANpgvM%2FY%2FPLNUkKmrxgD%2FrdPFNZQYc1fFLrOUU27fVk9bSLDMIyRz8QqOIgACWVsuAGnisHL1vqUay%2Bd4AucP9eeboTezfucvUxFhQG%2FsWD3uO8Yf%2FH2hwwiBgdF%2F1Dc%2FjubP%2FGMN9WKH30TUUG7r%2BP2nqGdVOmibCnmQkYPbYhPzC7llEvB5QLze63ievNvokwTzgnULzzCi87KsunbpfUwzzDaN19CJaxPlgKlTdfZgnsdgdiLbg6SFU%2BhNNQWLz51K1UOwco8TEF3xvT0GVi3VXNydC%2FPNBEB0qqY4%2FMW2vd0ayUiqn9T0t%2FqJnTbfGTHwtiOqqjzra%2FxgrnqIqSwjdc2itRw5ZRGEBBDT90%2B4iQdouqFXlnRN0l3qg0P%2F9BFgDhnunURspJIwaRv%2BuDjENwwaTlY8TOH8oV46XhJKfd8rLvwSggzDV3ncK7ef3lZ8W9SLnjvMA8O9sDDMzn4o0ugAeDWYdQGinmQt7SIkGwGSRRSr9p4KwxxDbBQ%2FzyF8sncGBoEfJW1mix11nF0CtUcWhT3Bg4QqLi%2Fs9VMLS%2Bhr0GOqUBSICwsvnK%2Fut0U43Vo1I3lZkBHo2OS22HM%2Fv5cDq2c6GNLaF88Yu9AiDCyH3xmPkshr631runGhKDC9J0u%2BHGXh42edTgFMJdc62SbSZrSI%2FFoOBBhbXcwcpwSkm%2BdTzylpLTO5ZDjQMd9%2BFd1f7V0AEXaAUTVhvQaxqCJh968RwmjGkfpmsGslOmQFo0rxr8EG9alahpQ%2BxkjK7OFfpQHt%2BjfE9S&X-Amz-Signature=277aabd317d50397f4402168c62c15cfbfdad8d0a5ef442ecd4490456a5a0fab&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZS6CDIB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIAFKjOCYx7FXLGUVCQZdbtZNSa6nt08pCQ3O0zYrwkw%2BAiEAvJZ5ODjHtv%2B5i3jBBnOkeR7TEqHCwOMabHlwXk%2Fhugsq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJdnlZZw8Ncb2xh6dyrcA9mgxdW%2BAtFHa%2B6zhXIyzhmpaLSYavixdxLn4CVeDjvN4pxCXRO00R2YItMNcexHAtJk7HK4OAjHxe3bxcTpTvfvlqG5lTBEkiBEuAUhJc3LT97CTR%2FBPv%2BPCJP%2BNLoYxRjyZpvtmsoM9qqOyot%2BKgWNnaBm7X4y95LR4kvu5BpL1dCM1z8pAt6PN4H8%2F4ZjSYpSqaz%2FtUnt3C88ds66RP7ZlAeTavrlVSQ%2FJkEC3E0O12kf2PMdBxsDjZ8UpIQngziAjxIhBq5jcTVYhD7HKBaWS1tkF1vZW1Ksj7LOkvpFM7jeaoC3fBYgHf6HoZt0o5jNgPlw7B7u8H3aeTyYWIdxinGH8FieLBcB6BZruuzGDDJquUrMY9F2ZE5J1mI5scvb5IXKDdpyMM9rjysYkPdNPv7oXxqCePZIoaudjF%2BYyPgDXAiEG144c68jnhMfecrfxIxGZUQ%2FShPxqr2nUQGx3BTIdwcIRnLahY4l0hps4Xe70W9NMWr4krw4K%2BHRydAre8F1xY3GFomyhuBW4HI0MGatE3IRSAWGv1LLCYanhJlGIcAsSCpl4xJVhF1pVx48gReX%2Fkz%2BiWadIWXbQ6Fa3L4niHur%2F5XsQCtZgUhor%2FXD19GWfB5%2FDitHMMS%2Fhr0GOqUBg1UyGWoR6iEXTBW%2FS9NG7BX%2Bl2yHhHPKIkMKf4toObPAE7gedfcsa8%2BqvIKYIn7PiP%2BJDvhtRmM4jzztYEjQGDyUdnvOxvQIZaga%2BLGoY0jJJuIHKSyblyT9z%2Fx3bfTNVH429Es05oGWJ%2FFvg%2F4Sd7JxGSjFUaLqXtJ6lL2y3RDRydCJfBnnmDktY22YZX9%2F%2F1YHtuf1ZH89fnPB2jE52FMyVWm%2B&X-Amz-Signature=e0a00277e3f1b48f510a42e04f1794e59dbaf283247b607c1d13ae4f78bbbc7f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6SAIOHT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCKIl8dIg5ApL1yXPt0POywCYvHnr0UyjTJyW1eHXuhWAIhAMR1K%2FxPxgQBbuuHdy%2B4dcI2Z3saS9Zn0mtcmjflk%2B9gKv8DCCYQABoMNjM3NDIzMTgzODA1Igz53OAzFa%2Fy4B5NjK0q3APyyenyb4ub3UktplmmCLGD2yF%2FQhOmyDdFfPT1wbtn%2BP%2BxD8SkHvRVJtI1w1O%2B8Q4Zv20JWzt2aLWdn6B3NrLCgGECwGq%2BUJQ8Q5V586prc2DIv5%2BJAQc%2BBUVc1xvIDE%2Bapu9IQR%2F3arhRUL%2BY8GvgjaVxnwBltzR4PfACAdDOsjnGoVRb%2FJQFvBpc9Ya8oBomtMlB8SqPpLu%2BAYTB00m%2BfGO8tbVhFNCzdwEOyI5OEHNaceuocbBVUSVIB0SDDuAYDHikezaewbC5uHsM5N5JQd1H3N58mPFjzMeq7odw9x18mBVqglXZq65oIIqRUg2%2FnIm6M%2B%2BqVFeWaxThszM2HnWXM2pwc7QN1BLhOKfLjfHXWo4lshJ%2BgO0TEwM4J8beeCe0jcZa6U%2BhBJOi7IBeJmNl3pZKUkGdvD8cKb34VT4jGKGtK6J8Mg9V3IWMQfgeQzO7DMzZ32N4%2FhARXyN7P2zF%2BujxDsEHEB0s5zoZ7cjUGIMLWNIwuD05%2ByQRiZ%2BHIxstKmx%2B%2FYqxgZLflFJyvJrd%2FbnF2uC5%2FLwN46wiibHGSfsmkb4vhMtjZxkrKRrAc%2BeSLbIYacvvg%2F5zoQiX1ElwSCyCWz9thWS6ZgprhuQW0w%2Fuj8%2Bt7yJ0%2FjDsvoa9BjqkAY7hM%2B%2FCmXvCc3DYfRsve7Kqs85W8H8GDMWKvDifBbv7Mvto82ZkRU%2BusaxacCZPiN3NMy6xPcepgGwq7m6FvjDcCxJ8g3sbOTnhHsFYoROTiwyH%2BUSmioYxDWI2HNRk8bVjQTKUSi9ssJoy3mXCHZTKoDLMV3%2FsO98JAPIErG5vi8rHCJJeaTXd7z%2FtcMIXfs7QoeOLIU2R%2BHaTbXxRb7cgOd2r&X-Amz-Signature=ba1344950015606ab57f01fc156c41971bb3a428b813546443f1d42e72f75562&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677LABLLI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCeL2DbgHXYdbLyb3WEhbht3%2Fn0M7VACdKqYcdFAuSaewIhANdvPeBy2I7DG4f%2FtUG2gANJwwm5rEtaUrRQ6JQB4f01Kv8DCCYQABoMNjM3NDIzMTgzODA1IgxmT50wQkPHul7GMzYq3APYgytU53s3yZaLeopuMplwD1WemEvjr4ZOrIGbPvtf3NyxoADGYx9CE%2BTiUZ%2F9pBwB6%2BsYYP6K71fWu8lu6GQhQ%2B2Zw822tsmEnoGqW0AF7dWPjY5coA7%2BeABGz6SwLlqjDganfEto6Y74OufvsHRmTpRa%2FBAgM1oeuhloY3MUC0qfj%2BSX%2B3I3WlhDVWS6viBrmd1wm8V6SRnsE%2FfPoPng2EidlaR%2FwdYGQn5ZxtZ0iADmkH74HCnTy%2FDGg1v0Dq%2BTg4Zga%2FEfD3frgVAqz9xb%2Fd4Hu%2B3AgHBRm5lY%2BIc97j3rEj%2BUazmBKeU1kY88UUMA6OV%2FV8bucaTmGUDfRgIlDpUIp82WDkBnaZc5s2A%2Bi7Y3Urexc3r7gJSI%2BEVlSTN1YBX3K57PPn0uPnUZ1ovI2Z0ps76Ie%2BXZg0PExP%2FwjlqWkWiGwCRKVOJSgo0BOxmgk4FsihvgA%2FU4k6DxYxLIbOMhh0YGONzQ9oTTRYEi2bKSm97yrwrG%2F0WuJvJOTPVIvcjSIJCLj6FHUEenh2S7KeUdLA75pWC%2Bd%2FeGlFCHAHlFuJApax2EXFq83YCJswpwT97SrUMB7GgHQvXyAQXHE1MelzS25MYnmY4%2F%2BsNh%2FyGyx6cgccpj0aWYVDC9voa9BjqkAdM1nEj2ck3mi12pBufC%2B4i7gRs37%2FHpHaqRn62Lj9oBG5OB%2FvqJXai2yGQN7VzFpXRHu%2FLX6XKVbidDTaDaDLOZsyqLrFad166ipuCxKH2vuX8GOkfihicMx1wL4KStfqdJe4rcEURBcURzyYRhFwlYMD0M4itCaopis78ex68Z5eO8XM4EZEW9ZKCAluI6b%2BIBhSvBRN0X284r8S%2F55LoN%2F3pi&X-Amz-Signature=3237ffb99bdb3cececa0d877eaa0ac160e2519f57129ee28608768df213ee271&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S474A7C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDQ5t46OYHGhEmuIkRuRk4MVmwjqPmrPKCmWuETUkwt0wIgKclkUpi7RH%2BwK7LKOhdV0XsfYqcwM37uo6Iz5nXAcYIq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDFvuoggW5CtQq3LsMyrcA1l8MebcpoXUbKyb06GZUflqdddjEJ6BBi6%2F55OOjDy%2BXzOJr6O0rEiZjh8Ve1TWMbLlErXHbcsZLBgBsOhGs2mh6Ui0ZxJx2z%2Bzg6x7EylzZXXSQPXaEyV4uT4HSYCC2GFkzavQzpLbrK6qeNWJjG3Zp9wARwRN1BbqlKlkOMkLCr0gTZj4Mai%2FX9DRHgzGIkx1NjeriIvJ%2BgKncj46%2BvK6IRRpXPXk%2FoA0IF2XZ1Au%2BQrT%2BKv%2FzZccR2Vmc1mG2owK1V2iEYGIM8XyPXC5Ztcuj%2BQIL6U0dWwQ2vQOnAQ4GucxZmUGYkBcBj5SGccTSHRNY9Cjhh3R5A4hKF1%2FqEOE14rqujZeTWfe6jrdsANr0EerJsKy1jnHiM94zA6FV4veU74Uoj6mm8RD9q5ZW2cN0mYBSFPr7MQMXS3CLUrD%2BFTaZTHDsEhq3xMm57d0IutzxVUB0tq1%2F6q8g3zz21hrOXPiYK33Iwb40sdaN5CYUNKBRFdAexb7tmTBVXr8E%2FTpFhfbKbNIPJHPB6vQ7A4dXWB31ZKd%2Fi9pgMTxfCSvYDg87QiYPl5eV7pLuVOSbMIqqyFSCdKuuA6seA0OOQ4XdvQ2n6fjB3W4P5UpP75UY%2BCm5oa4bzxnmgdAMLW%2Bhr0GOqUB95XTJiXw%2BOCKKuu2oQ7lYkH%2BzIYFZLSiKc0a7%2BK%2BuM%2FKQFwMW9ml09m1eu6mXhWsyW055H%2BMdoJw4uv7t8Sp12GXz5SGJzZ640peYkOyBER3kzKoqScvY4M6rpzKvpUyYZa14g%2Fn8aH%2FGOClbgGhODyEyrS7YjC3Dccmv%2FJrmQVOoS0osawVaDAL2Ptv3e1guH%2BM5oHw0uu%2Bf7HQ3jrrrWSEnDJ9&X-Amz-Signature=aa8d6c17b980df1965b20014a5ce99b776eab6825e3cffd2d75528038006784e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VSL5Y5I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDPeNlB7RHqYaw7nc8xnfjyThuC9VHOa5zY5Lmb8okS9AiEAzdxtNiRkKJryKQIUhLFg3AdZdU3jBkztj6591iT1nhsq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAfTtKx6xj%2B%2F20hOPircAybkQ7iZt16vJ9lNoci%2Ffxl3p3UkRa2qW%2B6jCduf0%2F7BzwzFucFtCFpmwhjFBfMh8WllME382k%2BjrGrHFCX40KXwZMHeXg5vmyFgwOCdyQxVHoj68JmpVu0rqheuRkQ0yHTdkP5U%2Fj4nbKCYWkLn8AO4gXom9cWRA8v%2FXyNcBIxV%2F8UkhYJNwWdAqLRL8FbQ%2BCx6XYd39OM5bzUG3DxmZ%2BM2SZkaI%2FbCY9AengLJuapEFQ7Dq27FCLbx4qcUpRI8hicYNe2wIi2RBf3yDoKkczBwXqo4dCRVZja%2BuSP8mK%2BjUBMGc1wsB9xGYsa9wXgamDuY9NgksmgeXtXlLgB4nRP%2B3Hzz1yK7FEwMtbmy8Ld7VkrVDhYE%2F6L9I%2B6lFK4LkBoFSkmzT908LS6%2Fq6N6i8QH%2Byu8IxF05fVnxAlGvkuWAF4kkQ0SyhQVGMDwoii%2FCSlAdqb4iEqDp5gJJBcQMPl5jxOsUSHYbG8F4q5gWMLlnOa213E0Qp18yFI9bdUWptdvTiS04h7Tk0fjowMX%2FjK8GM0Fu7KW5zAp9gqXozStGZbW7pGu%2BLxU8Xu27uYohsfU3XFCY19eaul4Wmtorexk58cbPCW5rRnU1b7bqYB4miJUOwSb1QoFgDlSMNy%2Bhr0GOqUBbVoMXglv6JJdQnOJaPwPZ6KTfvT8LzMlVlHyG%2Bpb3T1Xhmmjqp8R4h6YeaGaskANwsNcwFHILl%2F1LWSAIVSN1BPWjzJH4CFtLTZt%2B9rwiTfFoGsoMEIhM3k7YXl7kscJ2bt%2FG18JSW5PLhnfitvn60EocTkTk0qnQh%2F8BM5%2FMmvBJXxWdHBLFSZ1znCY5Zk%2F9iVOvqL3ksX4e%2FL1kxY6VSyB10hw&X-Amz-Signature=5475ae8d9f3cb3fbbd760f4c0daee5865a457eb1fee02043d942a70731c5dc57&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRSJYLO5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIGMjLqNg23Mn8iYuHqCBjfxTUYUVxcmd33%2BcjZW5nV%2FJAiA1nFKAU4HadHuUWYWmq11Ar7Q4rm7d3tYZ4BEvIzVP%2FSr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIM9%2FpsbqWKGqXX%2FrIbKtwD1z0xlTUJNZwHeKkcjI6EIy4Vrjkihf8mR73%2FZkWIx8BJUAf4ogGS%2BMrMWKhizNZS6sXpjz0V8blr4gs28dTzlcKjv%2F7BBdwZIB9xCl5rfIZEXSg%2BfgrpCN6WWBPTMnh2yel97SxaWwN0BbJ7i1%2F8wGU%2FfNTTq6GuRZQo58%2F%2F5ag5nzTdRoxrC%2FiWKiB6kom7pV4mE2eQTrLLVp6GAhcxFyL2yRk33YI8i%2FJgqzEjKYdYH%2BHdApelGBLF%2FfZWhA4P6iD4itzM8hn3aSW%2FZWQdCibCOODTGrhOzYKbyfOy9FA4szKr0r6rryMSvf0R3UQlDZkBQtHe1mqTDB6pby4jUoWsYt%2BGHMtQMi14l1Ik68fFRFUDCXBpgMaSlQFSH4Pog5p8R7aes%2BCqorse3ds7zYAhHVAJOqrNrHYX91zl8NgcrFn%2BlYO0vPBmQDfixzSK19xj%2BNi956hZQ0Pk%2FN2QU5039EBv4XGErOkNCyJYwSH1fb4rzhB4AjwSdrY2%2FnmfiFiT%2FljGNwBHm7D%2ByTRPQ3fAixhasBbaS%2FNef7ZKx34m95%2FLNsZaLn%2BiG21XaeNuiC7lez3eDjTni3FocvQBhtnENeWOx%2FwoT8%2Bxv0PSfSZbD914NtRFgrjwfbww%2Fb6GvQY6pgFnzuqFuFxom0qScm9%2FLH3tIdZ%2BfmQIbCoGOAYOgo%2FQJBAVdZGgPS7aZNZ0ZmPsy9AmF6EJZkH%2F0%2FxahYp7wiavOKMQAyv2KAnBF68tJ9PsGW46mjTK6CQnu%2BuvAjF44nwGYJTi6PAjUxnYcCgMPHEl%2Bnq3Pp20ZQv4nVE8Q86drEOc4t1lomz9Y2aW7QEiAnjfJGIBhuyKyQjm%2BsaE%2FeKy7u%2BSG3B9&X-Amz-Signature=49fd6df557b759e337fffcba1f82e7661e6984809f224e4fa03c58d7260876af&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGCP3CEF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQCgB0UCp4vpQqJruvNLnbg2AsLZs2i%2BJRsIdZaWdxPtHwIgTBPmb2XTHvaGnTVEldCcMnvHqFZsC1tL%2F3poG2WKUWAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGMwWhpZTQErQvtBoircA7otbHtYm95b%2BniE%2Fv5U96Nm1Pa5VbcQq8im3n%2BV3M4bLJIjlaffNOcBc9uPUBHRMlf8aYv7pd1jJ%2BOcyZIxJFuNwUYcaifWUbgfopd%2FPfLOZ4bcbv4NgtPMOyFcWWLl7hw8pZUTnUxZtcnRjOIKxbkbZi8F171t7rYULnRdukV5g0SoanAttk6qEtdLUwiagNWis55s3JanxGR6vcQ6KJFUPNuvGdZG9q7WSK881kHR%2BjKv36RpuYsQvTuzrB8mYnXiOQ3lpjxQjVWgsOwg8bgcrZV%2FF6U%2Feas5FUVUtAWUYTiEkRz6bhrlADBlTtI%2B8Z5ojKUD%2BtM3%2By%2F3C%2BdSiJFRzLhbD2nalz0g3%2Fj7p26YagQPmCFPeI3WLCN0KSCJMPgurUpyBvnaZZBq2ROISyFMbjbvF132HQlzq5MZ9hJ9HkQ7SSgdCoc8NqYsWBmSGrW9TgojcXpHsAc6Iei8y3x42v59Khgagu7mPlKj%2FwWW21phWBiV3o%2FcJsWe6JIaaHQqqzA0ZSBcgiHAO3qMHKta1C3EdfLu3ZcrX6RFuVn4gPM1uCwfts%2BMrhQYxJrjN2NYwtgaWiG33Sr9Gb4mfII%2FU9w5ESITHbM1YV1IvwCM7kYTtYM6o9gbzYCKMPu%2Bhr0GOqUBJcxBeFYWUYz%2BVj%2FDnDV2KP94bf045qqPZ%2FUzesz9B2u8G7EJVCi0nuwEGur9gY2UfwKIYP%2B86OmWZJQY3%2FEd20Fjg%2BfT0922qnRZRNaaBPEJxP0P0lkdFwoPTQ8NLKvz9yTVnvZw54ggfxwVMQMjMaUIdyRsmU5eQfCHaUpnHDbAYaEVjOs8JNG8VpH3M84BeKcZbXiHLz9a86DnPBa%2FgnUnhfzy&X-Amz-Signature=ef2d6766ba58f351685708fa3dd588473f3d2c3a9064bab264d605954ff85bb5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S474A7C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDQ5t46OYHGhEmuIkRuRk4MVmwjqPmrPKCmWuETUkwt0wIgKclkUpi7RH%2BwK7LKOhdV0XsfYqcwM37uo6Iz5nXAcYIq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDFvuoggW5CtQq3LsMyrcA1l8MebcpoXUbKyb06GZUflqdddjEJ6BBi6%2F55OOjDy%2BXzOJr6O0rEiZjh8Ve1TWMbLlErXHbcsZLBgBsOhGs2mh6Ui0ZxJx2z%2Bzg6x7EylzZXXSQPXaEyV4uT4HSYCC2GFkzavQzpLbrK6qeNWJjG3Zp9wARwRN1BbqlKlkOMkLCr0gTZj4Mai%2FX9DRHgzGIkx1NjeriIvJ%2BgKncj46%2BvK6IRRpXPXk%2FoA0IF2XZ1Au%2BQrT%2BKv%2FzZccR2Vmc1mG2owK1V2iEYGIM8XyPXC5Ztcuj%2BQIL6U0dWwQ2vQOnAQ4GucxZmUGYkBcBj5SGccTSHRNY9Cjhh3R5A4hKF1%2FqEOE14rqujZeTWfe6jrdsANr0EerJsKy1jnHiM94zA6FV4veU74Uoj6mm8RD9q5ZW2cN0mYBSFPr7MQMXS3CLUrD%2BFTaZTHDsEhq3xMm57d0IutzxVUB0tq1%2F6q8g3zz21hrOXPiYK33Iwb40sdaN5CYUNKBRFdAexb7tmTBVXr8E%2FTpFhfbKbNIPJHPB6vQ7A4dXWB31ZKd%2Fi9pgMTxfCSvYDg87QiYPl5eV7pLuVOSbMIqqyFSCdKuuA6seA0OOQ4XdvQ2n6fjB3W4P5UpP75UY%2BCm5oa4bzxnmgdAMLW%2Bhr0GOqUB95XTJiXw%2BOCKKuu2oQ7lYkH%2BzIYFZLSiKc0a7%2BK%2BuM%2FKQFwMW9ml09m1eu6mXhWsyW055H%2BMdoJw4uv7t8Sp12GXz5SGJzZ640peYkOyBER3kzKoqScvY4M6rpzKvpUyYZa14g%2Fn8aH%2FGOClbgGhODyEyrS7YjC3Dccmv%2FJrmQVOoS0osawVaDAL2Ptv3e1guH%2BM5oHw0uu%2Bf7HQ3jrrrWSEnDJ9&X-Amz-Signature=307e454d88f8eb0558c3cfeb147e5067420e3e3f7d423815e432345be993f77f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYFUTF6Y%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQD4G9h0KBgwDg9lrGI8iVxGjnRLahj349ociXPvId%2FnTgIhANDPqvx5EskG%2FKXsS11GdwPVM5v%2BcdZT1XpeOgZPlLIDKv8DCCYQABoMNjM3NDIzMTgzODA1IgyrDLNY%2BSJZFLHw4XIq3ANjVYh2Ktrjq2A%2FF2QpUthdq7NotdzPBCxhWQ2p0x4C2nIJDTCBYd1fHA8oUyduEg0NaSWnq51ZgriLWKmSXeFHoVg%2FEvEDUKgk%2BeG4HyYwGiTYCKtNJ4ablCkl8R%2BoMgqZACaFkGduN7nXMlCd%2BmWYiUNt716GlxgSnXVpLJN43lZ8SgTV2bvqmeGyLei8uyoBt60Ly9pPASZN4slk0UF61cI9fwPfzVYNG3JujXxRybqR6l4jxEP2dj94ISynyzHsvyqMhJVeucqM6Jj1CC6NuClxEAavDBJZe2lVrToqAT7bv7zNIdpywVAIQQjCnm2vraH8ZmOCqbDat3WP7kuOTJRb7NAI9PgXBgwJCxu1EDjyMMbsuKJMYFr74kzpxI0QbmHW8pAbArYMuAh9vop7ND8W86u2VNz3KsSWZte%2BbbPl9JCaW7rVIRW0M23JJCsVpztCCuQEtJk0dPWv2tvFCo%2FoMIfLD9WCo3aQJ93AsCFsGRqVZKXf5U2dpRJgsA7UXj6hW0%2BRNLhLuKxC%2FTotYzVjoSquKLcIEw0j20wajpMp8yllVcGgmZ7XgFGLJVS13K%2BR2wX7XUwQiZqb0h0jskq0x5nT61dMBAizOpJIawLpHbw1E3rMXu7fcTDUvoa9BjqkAezgkR5IfhU3N7e6GnEPU64xmpyGfLpF04qvrkSPdZdsc8Ylm4gucytmPFmJVDLtuOsPfxIl5%2FCJyLwojT5YqYVsk8THZu6CP0dEhYmUCLFBV1uQCTC1NE68RWYpSSzF%2BM7ZMo6KetpN3IBIm4hhp3OO%2BdejCJKxM4ScKZmMqQVrMLorSWY29JjLihVZDIolsbJrmzep1sptswETyONrTG2pVxrG&X-Amz-Signature=d73aaa3ded1d1aadf84f529303cf2f6d8ccfe5f4c256351b478c7facf0cb59c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYFUTF6Y%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQD4G9h0KBgwDg9lrGI8iVxGjnRLahj349ociXPvId%2FnTgIhANDPqvx5EskG%2FKXsS11GdwPVM5v%2BcdZT1XpeOgZPlLIDKv8DCCYQABoMNjM3NDIzMTgzODA1IgyrDLNY%2BSJZFLHw4XIq3ANjVYh2Ktrjq2A%2FF2QpUthdq7NotdzPBCxhWQ2p0x4C2nIJDTCBYd1fHA8oUyduEg0NaSWnq51ZgriLWKmSXeFHoVg%2FEvEDUKgk%2BeG4HyYwGiTYCKtNJ4ablCkl8R%2BoMgqZACaFkGduN7nXMlCd%2BmWYiUNt716GlxgSnXVpLJN43lZ8SgTV2bvqmeGyLei8uyoBt60Ly9pPASZN4slk0UF61cI9fwPfzVYNG3JujXxRybqR6l4jxEP2dj94ISynyzHsvyqMhJVeucqM6Jj1CC6NuClxEAavDBJZe2lVrToqAT7bv7zNIdpywVAIQQjCnm2vraH8ZmOCqbDat3WP7kuOTJRb7NAI9PgXBgwJCxu1EDjyMMbsuKJMYFr74kzpxI0QbmHW8pAbArYMuAh9vop7ND8W86u2VNz3KsSWZte%2BbbPl9JCaW7rVIRW0M23JJCsVpztCCuQEtJk0dPWv2tvFCo%2FoMIfLD9WCo3aQJ93AsCFsGRqVZKXf5U2dpRJgsA7UXj6hW0%2BRNLhLuKxC%2FTotYzVjoSquKLcIEw0j20wajpMp8yllVcGgmZ7XgFGLJVS13K%2BR2wX7XUwQiZqb0h0jskq0x5nT61dMBAizOpJIawLpHbw1E3rMXu7fcTDUvoa9BjqkAezgkR5IfhU3N7e6GnEPU64xmpyGfLpF04qvrkSPdZdsc8Ylm4gucytmPFmJVDLtuOsPfxIl5%2FCJyLwojT5YqYVsk8THZu6CP0dEhYmUCLFBV1uQCTC1NE68RWYpSSzF%2BM7ZMo6KetpN3IBIm4hhp3OO%2BdejCJKxM4ScKZmMqQVrMLorSWY29JjLihVZDIolsbJrmzep1sptswETyONrTG2pVxrG&X-Amz-Signature=22777c0c0a659ca413f7bd893b3ceb5c2fb8c6bf5f25fe156d65afc640b3371e&X-Amz-SignedHeaders=host&x-id=GetObject)
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