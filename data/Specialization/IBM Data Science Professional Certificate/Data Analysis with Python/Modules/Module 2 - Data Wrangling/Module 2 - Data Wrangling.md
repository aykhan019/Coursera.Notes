

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BODH35S%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHBndZSxAdsxe6hSnIYlEfgmqWusAI8YqtoxVSR6vfvhAiBAHl%2B1waQUtBwzB9c6lhad7F8L5RwNnEG3oiqWbpKW7iqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlJTzxNI0GwgiY4M7KtwDLARwxyQsEQq5ml0jxd9n7Blq%2FJggD%2BIgZRwVX3vhXdr5lvHAt5CfCHBENVLLgYvbnt5FMDTlw4xwfMZ6xr9G6gz9zG7b%2FFpeYHYme%2F0dZ%2Buek5oj0%2F1qy2YEg%2FV%2F4YnZjd%2Bd1IFq%2FoEGw6tf7E7naIFusZFhc2kG6JjvEKCZRwMhY2XPZ7ghQlwMrjF4DMVzLmRrNfh83SwKzkgvrq1cKOP5t3PsF0JvwtpgNNnMW4MDhh5F9wbdYmCw7qtApf0uSBcbzZ5htIeJH%2Bs2MUaTt%2FQEoMD%2FxpDQUWZrY2PiheE1FehEh4E6%2FJwjqifEmGpZL3cYdEt3OgrqpgzNGcf9Me%2BCZ8RmrzMaSyJyqI%2B0vtzxwb%2BKfL6vudOrRbaBeh%2F2C5DkoKmds1YZIPFM1aur%2Bwe0KfwrVPJCLTW27KKfjHWxn7NjQjDC4myxTg2dwYiXgLLqANo%2BM4qO9MndGX1slzyuPwSyX%2BKQSQJvBDzgi8hsPvP37adhbP9wf1uTXBg7Xq0mufIk%2B8x5oAtZcmlPrlS1CV6GSm1cfCAlb2fowwJshIIQpmzIj2xKJmo4c0g4sPf4%2FHbqIAGHsf0a6Sa88wfB72ocIOOazPujzTg10OJaRZOYIZubxjrn2BUw0qnqvAY6pgFa16pNq04wj1Ij5YDRT%2FkHcclNv%2FsVHUYOeVyMSohEMjnnsgXbUToJU5z3Bt58RHnWvY11CGxSj5LKXAnuWQHm8UL5vT7kKQ6fVrDoTHIiCMV3ZU6DLcJCj91JtgOD7IBkKP7lACbbvFi89MAU%2F4FuVe8G%2F%2FOd7wNfTZ%2FINN4JQyOzhj5p%2BL%2Fgu7nndzRbBTa2GvWLJ8Z8OqzyWFrRhnxEr4UL4Sd%2B&X-Amz-Signature=c2a89b8bd85ffbfca2ddd4b7a8056cc229e99ce0287645e46d205730ca054306&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ROXNT37%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEnTefsyubkxqNzPSEM%2FsehIZCAYyCY1UDh6yrpYry12AiEApuL6DEJp0NnHvElSKncdIQ7hwAmwptcIspspaIccRA0qiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaWwFYEYOL9q2f2gCrcA%2FxZHt1RzEVztP1XquEotB%2BrAi0uE382ZIjqFZ45G%2F5M%2BZdV2Qd8qmGCc%2BHEQICeMhMlQiLFKEdobeqBjQUBMhjH3k0ro3nKY6EC01Hy3ryr1GP9teVevBkPzHDkideEtiUx8mY9kNCGS7ahZp3%2FnBSk5eeEJWzICr0dkQbd6iHh1eOiooeNQm18kAtxL7CJ6CgIlyXhtO4as7k8DeTh7%2FZepo8Hp%2Fawr0wncfDvpuiEyXUFcP5gi5rK2j0zngGEPLGXZ3l5wmIqcugNxH%2FBKSgeLzpCiT60AIAdMhcDXioGpZQj%2F6tCgmOs6SSU2jBv5sN72LGfr%2F%2F3UQTz7sMITBALww%2BW1z7sXnBaSlaY2sK%2FNYGLfFlDVEF6Gr9hzP2CGCZt1wtIxTxZHmrS1BOM3DwIeGD4U0bgNZLo6IXOE7gfoRJMC8XPKbgirWaXNb7uNSEYx1rclIkZrWCHskI2%2BghWEBMbWGrFt%2FFJBiEqS%2FWhdnaEnD%2FgQIwKj3LxL6tRbU%2BrjWQN63Ys%2BUXdajInurYHAvShKIyLYnNq0maTb1IkL1hRnjxS0t4I%2FnKcMaoGNyAsi5brDsyts6%2B3JUcECHQuzvbYAK3h%2BIWfz3Z1yxUoAbDmXleBhMcuOb2tMKCp6rwGOqUB1uiImwirM4g3lAqZAOf9svRCfS4BSa4%2FqOaLTPNA7zhrbC0C4%2BCi8T0t87MTAdV8OdXbeRtt7xobbA3ZJRSUIw8wrAUGhy%2FzVugHoySMocpZ7TSy1HinChDb0Bmw%2B1yLTJLtDlUa7LJzwKyypuwV64y1fk3Xgzh5l12vY7wBs9KFC5UrprenibRHrjUxhbWqjl7ShOrE5JdRKYhy5vSNlkSlOO%2FU&X-Amz-Signature=6f3d407f66603beecc9b6b2d5797b0db4378aa6e6b6c3f1f6bb333598f9e2b49&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF623QBK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJoJzyNfX4XW6E2GFfN0loy8oMifq9YMIOKVtriADZfgIgMKSdPGPjfdzsk1cpT7jLhpn5UnlvtbObi7YFc1AlB1IqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKTYNSn0dWEs859WYCrcA97FuPQYUSsAp9lhCIrTE5CuLCgREZNrvZ4GhzFtDf8eu4zKKcLvZxj1QaJMatg%2By5NGAnC5YFM2keLKCaze2CSKQCYX6QRTNob%2F4U8CVE9%2Fcbfj2nUR7iyE2NCAD3pstL7HhkT1qIdqRtU4uT3zpYrQiMrgLxZORMTItRkZMV9fRNhq20DdgxRSL22vAGRz7K%2FS7HF0jXg5VA6LHO3hIh2tqKCejV7BsRtumg9BaSKOV48YyoCQVs6Z9w5omBYObACGZofkvfplvAo4IbfA6k01FFSPPywL94VBWUgNkA65JzbFc1CllBEViDcF1Q9swpLB3onaN4kfTE3sh%2BB2fyNIpwNuoeavSJqnfuuGXVdG5mf0Q4PN0Gy9aCcwn3fBt%2B97OCcJM%2BBv1s0vDDi%2FjIH3ssgHf%2FvvmH7elUT3NJlOdzN1nvkW8y1Na7kBxOPY7PAW7AAPjfGBHFTVILC9TQPi2bDvYhu4EeXGdYkaIOkN4KYpPRFm9jisbRnkHmvJr4eDSVlbU0sy5c4mw%2F0y%2FsMHuWQqMXMnGEAE43Tb6UmC2V2KaoqFPlrrMRtlJPgAniv8GUeuYMw8l4zZjrEjzxljqGsDsayxtQCNOnuWNNYTJJVB%2FCpqBOgr8tqCMP6o6rwGOqUBuC8YlMLDiSA5FazbHdDbvLbsqN9l%2BcgJl7tggDVBV9mRKhxLWE8kYDoMX%2FFXLC4uMjqM6C7UeK27SLeVBRKA1xt%2FlINFKaDTAazMxPfc2%2B9GwUQkQaAgYk9P8mbhUA98uLSETIn8wMLNor9jx4Fw%2FxMrIs%2FXPyyBxQ%2ByUFYUDPUHkNEEjP%2BlwxoUC75aK9WbgXk1lr1jrQhema8phvYJLECj%2BVW1&X-Amz-Signature=323035c70234f51693e1eba5b08f1309749c79f5d2e18a0785a01a1fef5a756a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HONXN2K%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlhdTIntWx7UZlnwhDlu0oHONAYp78P2hfVmSN4sh0ZwIgZvsEqFRgmNNcrY9rBd%2Fx3ow7gAqxB0iaz6SCUBnrR60qiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYa8Yg3SThyVHStHCrcA7RyKAFqENWfpTiSrjv7oZl14%2FGFG7vyP6BceWJbPMCjFopZeuk4MS0LbrtgNJmpENzQG%2FdW0MzKNf2IogPtkFiLyv%2BUCutvn2KvDj5gGIXKFbzXavmt2H%2FV3JMbh3mOspAiI46iYkqUP8Wa1vshthUprrxEk%2BLUkJdvjSqcNOdLJ4fEESS6BjSdusxJkXf8gIMAzAKgHFupq8uELNc%2B%2FlfCSOOfXki9l05%2FrLJt6m5MA9AS6ti4Z5hLcRNpBxZnIrBghYIfV66OYCZyABDTy5w1%2BqUueV%2BAvm%2FsUDGbMA2GKAU8lY24iv3vXtQi%2FCbZRzmkPHH6RdfZM5mHNWA9X84MKro5Fex%2FwN%2Fl4L1kym7A88oJgy7SZTSC20tdWXykdXdpoVa4Cnh9U27riFlZBl%2BE2%2BRZcFiWCWF9WcUO2iKn1A9kRh%2FA%2FPX099bOOjoUgNWGEO0OE6PlXn6OgNZp7KCZidtRzQfjbfXhWcq1oc8CYUvHhW1MoGde16BEs58WZHzhGU7JL9TQm4IobNhOJwSy2TiR%2BIV34em2knV30yHritXJ29Rj2r32vX73NaVsWHqu1YDS1Tgt%2Fn3Euz1PJiaNyW4WaJBXSbFJwos638%2BbDwSDnL6aP3ajCVBuMP2o6rwGOqUBedrUYLX%2Bawcv%2FOaSOkgfL7%2FWwrWDqSV5hPi7AucWRM8wTC3d4ajUKOAGxZwtiaX1F3%2BS%2BmI7NH6bjN1I5ccNzzSMiHXwb07p5%2B6cjLBFWYW2GVV%2BcgDTe%2FzJEJc206Ko%2BbLzLJjUHOX6dTZWLlPp3gL39DQEXw9TwKZiB91x4Andb8G9cKk%2FOWEmbfhUgVU72MKRQ3ZRd%2Fs9HH25yRTb0zIL56ws&X-Amz-Signature=7d2d5e56ebb9f696c5893f3f11bfe3b8f059e5ae238eed05f5766b7e165d2e97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUJXRTJY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2F2JkMt5TcAh%2BsjQOeUevMIc8EHKsnBRzn2F%2BDeNvNVgIhAItaE7AZebQwzeUcXrPI9v%2BkfjNf4PGQlqmubFnYh%2BDBKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwCc0kByMN%2Brg6jZ58q3ANq3Gult7ekE7383mqIGW%2Bf19MjK3t940HX7RlSoMY26sKN6PunBB1BSIP227%2BscNAx2jpiVmWKubjVb3fPsx190hNiCos0sWjRVAobEy2jvdNmpo4YIEhcxAgMbt7loclSLPO1fO%2BlVByGHOlAlILscRBE%2FwGR2Bd5TW4891%2B%2FLgm4hMvred8pwT3E%2FS0fQBJdgUa62kTAnwW%2Boi1OB5rCgfN13HxPeKv45zmSyOQeT4HETA123hI1u0wRhTe%2BDDzy4FI3koeVZ0D1fHv4LH%2BCBZc0evsAuyBEqYiCkYglbVueIK8vfY2Z9eas8N7rTfeVHHzH9Tv7yu2L2cYm%2BaSJeAUBjUJEMoXRXsWhxQv%2FADpZdb%2Fkna8WYgJrunVtQRoyHs1rREvOqzMYnKqC9qUuOmt%2FzmowpGdGDPKOZzS5V4KOWjRD%2FR2QjqHPpxwBdUp2J72%2B68wBv9kY%2BozfgwxmUfQlIO8m7XhGJWZukLi9J8fsS1GBE9EPlrDvYZevFzKZXhica3lVoW2FcxyHGlZTyg6MVb7UUkYIvBxRPv4XJtr35qBaap69QEm8Eb1dSoPooiZgh0WA3Tg5rAgBlTm%2BtwiPqTmca2%2FAy6RODt0OxDcak8%2FAlJBYxwpaLzD2qOq8BjqkATVcTLf%2B%2B%2F73Mtcdvi3BEnl9JRtcM0deB6zEtg3nBgR8zkhmcB33Xvc1xnfR1ep0E%2BQjphuctDVutwp%2BSHDsr0cCfewz1IkN%2BbAXfun83seb6aK0vx9snPQ05LGfPFoSKbNQxx%2BqmJZGcniTI30s5KGiFbFzF%2BDMLmwYznTL3wYqvV1eB%2FRdhYYfaeubwBNwODSFdfoFAGq3sJ10lY61IFhr3ncX&X-Amz-Signature=501434cb355eca875472b91058b791cf7733ef0d03b0506f6fc7296f8ad4c139&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKL5CSQ2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERQe0QkEa9pJ0R%2BcFuJkYJzw76TSO9pmSpNGzMJTcRbAiAKU4kaGm23cgNGS8W0e8IuEh06uFWlIcVcca5%2FKnbpPiqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYb1rsSjXmGhXkQatKtwDECz9aknkzaXfPAooPFuq8ZmzvFObFYwflQFdIBNE3gWeGgcNuidyGjxasJ6NU%2FOpW5%2FBhtN%2B3o1iqVfbG7kG6AmJlvHmVx9uBiJZ42B2ZHTIH0CGfGZaBznhR64CIUnXjH%2BrzNN67dWruecrWMXLhgzANQHMLfaCNAQsy0DdbAmHNiyGUfUYx%2B7zrM3TlfK6maMYExTtyUV6gBPoqb5TYHnszTO8oB4zKDU0wrH%2F7Lq%2FkU95QSTO0PZCEfFCAw3ys3agwp9TRit9jgytxIH8%2B8SxbQeWhoEm1N09EwhpCRwRqKS0yB8KOFSSRI9bx3mmvWEkaCX0B11rTWjsZ9nujYhZ1NxloFBwrmUykdmGeQ38la8oH3gprs46C8TPdJBgpY2IICHCZLUWm15t7G%2B7b%2BlTaIkAon2s%2F9UgEgyZ%2B%2FZWaF5eUOBDjEFbJT8YlLQLjK73SvPr%2BXPpNp7VwGHHkF4rpf8ixPviLVlcJZ3oc0RjzYKSu27RXcbld40LWvNCRMiy4Wh10dTcgLyNnHJ3zEJgarboy2ep2Qw94dTYvYA6F2WlP9FiHH7UKe6aDhz%2FLkomCtXDJGYOX5OEw1DbVFhO51wFMSmRndqRtnzhY39a47jNlwIqakmrhX0wmKnqvAY6pgErHXz%2BJ2LguL%2BiFUZlN8akOsZrfBjPT9wBzfeM55WvnNmeVLpQ%2BZF1NLh3n3EbnGpfDemgtctF7vjvLpQGcRj%2FcMjOGMAiB3oXMKuDaqxX%2F4lyr7y1i3pz8E8jlt9vTv4hj8VuZZfA2Kkzs6EbQ2k5TedWLSxEkLaFCzmJQdkCdaXiA9ZriPW%2BZ3yT49g%2BDe9MP0Qkn7x4TrJ%2FjZvKXVPZfQhhQW2i&X-Amz-Signature=5295918a7be02cb6d22549d38c5545ac1d7fc5eada292f9ecc90e814bd0cd260&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDHCMLLD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICiM1%2F06g0ocznpjZHNJNd4CA2GLqLwsvVdn%2B1UH9%2FK8AiEA6l5XmVo8Z8bjo6yBwBXrQPAE9AuCH1Q1U2WnJGyTHIoqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLgSDH9q7R6Tqz5ADircA072lto%2B3BNQW7tbgMfIfF99uqzC7tzn87FN9FowaEJvFa2c6QbZSbsWFv85kXsCUdq82GIXKOc4FBB3YHh%2FEPgh6Uy%2F2ERlCGVmah6MqpBhWz1RRg1lW8nF7XEdmETH72%2Bh%2BsyQVAp3qPKhQSwbkpy9BWhQX1ZQkwK%2BflylLTGqkKjBwRrQrIOWXCuW28QeZCnaM9e%2FJLLN2YCJuKbbh%2F7ekR5AJk7YsxERi6zse0kEz6oYHdCr7lLkqM4fQEyOxyGL561%2F8kcbt%2BhWpGmupV6D7Rsde%2FL%2FoKqvTl6JboCyatATVW1Ae8D3VZAyt3ycCk8xqld8vaFH3PF49GGnP57FVv2TTEUkXGeDVc7U9YaBjHHbj5YK6ns1%2Bl34q%2B%2F7y7ZIxm28J38oWjrjAfBy95Y5DBr86b%2FJTn6lkE1NGktyKxhOlSe2azxseuDOdMhegw4gF4KyBPN3Z9fCZN3b4WkLCfAWW9NjbS7v6Hv7sfYYe4HbWZc94ztd2cEtvigmGodAMOmqLSuI75qWd4%2F6%2FDxCGkZke%2FB2%2FWx%2FXQ3h6u8bkD8K20s2b28MqFwbJ2s73Ud4Aef6iusUpOYkzfvF5sZVu%2BaoMRtA83ILWCIP6e7gj9jgX1lWN5YtmnssMJCp6rwGOqUB7hhJkAICiMrl24QE%2B7FAeFIG6LT1cdsk0G%2BeMKVJUKgb8xfcvnTZW%2BAR5ywoQPCNnKp5auzSe8pSV2%2BOB535gG1CuTBTeq45f2Y0Pv6m7I0cjuJESkq7ec%2BrbkddlJmuXW7pUmHxq4FHyjV3VFG0MrvlOYfIF31Jbdu6utYlZlGF%2BQbD82pz1muSdLIswaGUgdSbfki52wrMJm8Hv18kSqPo5Kyw&X-Amz-Signature=bb58374cc5151989110ec1a1c9039733e1fa460d4b257810d3ec134fba1c069e&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QF36DOSX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE7qJzebS8L8S1SxHpjY%2FL5YZnKeA1LnLBKWpYBzznEoAiEA9CA6Ne2A8JcM4pQMJTgG5D%2FS4jJ%2FrALaJCCHniShUkYqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKLAFIDOgfVxY45VWCrcAwxlW1%2BSjPemUBnPykoN8volCN9JA5XRKnml%2BuX%2BpoEmUFfDbRtBua0iBzHTQV1mLJAs2wxMGGqr2GqpmPBK7T5PlDHjW2GiyITD3fblPQRUykDvN5XPpT8iOCQtdgV3i4ghtg4M0EeGVnS4dnt7UJ5hL1PYntOy5hZzqhUUTA09QJSCvEoOIWXDrwPnMMClb3F7GO%2ByTLptrW%2FOFjHIXl2zN7xyHQKX1wpraCQ5zvqGklwDXyQwIP5YerUGqrQpuir%2BjWV6kt8BaCSrNx1%2FX9%2BlnPLrGy2vvF2u0MiHLTQxbROat5AG84cw1JobvURkVNZT8%2BBbOTJtCPb7H7tXig7wGSVpPQLW20kLYzVGBCZHHTmx2NcRSsUewyqeF4846t1BZ%2FApk%2B3BZAOoBmb9gg%2F4r9qDP%2BBnZ8xgzCa1D%2FrHT%2BV%2Fw9jttHVRX0RkcqRVfeg1U%2BPSxLOws7sPYF0ScpI1HY%2BM9iE6BHfF8S0d%2BKBBUbUnYnuWmwMfQ42fpwFd9bHg7OdcSuUIeF%2BVPsr2kZYoZepg4cgaK%2BntEntFv3XwYLqo9Fa8Yuz8DZNXmNxEflgpXGTNdPZjuXA6fx4JhIScjtVIE9JZftjRQZ91Ks8GU9auJSPjHH1aPzu2MPKo6rwGOqUBQpIvjgMONnt61rgG3jUlOgOwQLOjK9PDfbY2sJRUG2%2BNkn7EgHHvnZ5rSCvfoFb2IdtVR5i7J8XnKuoiTQaiapmQcFvxPx5T1bL5xyO6i7HCDoYsXJVuPzdHt2k0ps%2FbeX9LfTSc8YAL1OYcglKvhn7ahqrM0Oau0z%2F8Dl6jT1VFrfqwLLWrhZf89ZlQTCgLsw2Ie9X%2Bab1XjkH29lT4wZyukyAZ&X-Amz-Signature=8c1f87445bbb7d41bc769541808b55d5432ae447c27db351b60e5d9ddd4e53e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUJXRTJY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2F2JkMt5TcAh%2BsjQOeUevMIc8EHKsnBRzn2F%2BDeNvNVgIhAItaE7AZebQwzeUcXrPI9v%2BkfjNf4PGQlqmubFnYh%2BDBKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwCc0kByMN%2Brg6jZ58q3ANq3Gult7ekE7383mqIGW%2Bf19MjK3t940HX7RlSoMY26sKN6PunBB1BSIP227%2BscNAx2jpiVmWKubjVb3fPsx190hNiCos0sWjRVAobEy2jvdNmpo4YIEhcxAgMbt7loclSLPO1fO%2BlVByGHOlAlILscRBE%2FwGR2Bd5TW4891%2B%2FLgm4hMvred8pwT3E%2FS0fQBJdgUa62kTAnwW%2Boi1OB5rCgfN13HxPeKv45zmSyOQeT4HETA123hI1u0wRhTe%2BDDzy4FI3koeVZ0D1fHv4LH%2BCBZc0evsAuyBEqYiCkYglbVueIK8vfY2Z9eas8N7rTfeVHHzH9Tv7yu2L2cYm%2BaSJeAUBjUJEMoXRXsWhxQv%2FADpZdb%2Fkna8WYgJrunVtQRoyHs1rREvOqzMYnKqC9qUuOmt%2FzmowpGdGDPKOZzS5V4KOWjRD%2FR2QjqHPpxwBdUp2J72%2B68wBv9kY%2BozfgwxmUfQlIO8m7XhGJWZukLi9J8fsS1GBE9EPlrDvYZevFzKZXhica3lVoW2FcxyHGlZTyg6MVb7UUkYIvBxRPv4XJtr35qBaap69QEm8Eb1dSoPooiZgh0WA3Tg5rAgBlTm%2BtwiPqTmca2%2FAy6RODt0OxDcak8%2FAlJBYxwpaLzD2qOq8BjqkATVcTLf%2B%2B%2F73Mtcdvi3BEnl9JRtcM0deB6zEtg3nBgR8zkhmcB33Xvc1xnfR1ep0E%2BQjphuctDVutwp%2BSHDsr0cCfewz1IkN%2BbAXfun83seb6aK0vx9snPQ05LGfPFoSKbNQxx%2BqmJZGcniTI30s5KGiFbFzF%2BDMLmwYznTL3wYqvV1eB%2FRdhYYfaeubwBNwODSFdfoFAGq3sJ10lY61IFhr3ncX&X-Amz-Signature=e1a4a77bd47ef7298d44c464a38bc399a0a907d8314d04947bbf3995380948a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MITKUVV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9EflfirHKqwYQBNxiJNSzrKkuutNWHvhAa5SvYPJjpAiAJE47Vjj%2F%2BDJfpgnLNqP46TBEb80nbWWUtrwr1LOBTuCqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe0410FAJjlbitympKtwDR5wz6JPulpn4JM4K5QLXeEk8hfRVpEcMvo6ZlCWKhYB1TeOHaLXQiIihGSY%2FH5lIJEwBoosBGZbS5pk4SQahzxMLlIoVAkmpKr8QnTgkpnWZejbLHaVhkUmWN%2FdMlwW4ug3DLOrDXsMu%2Bz7DJ9CCgW7cbYOGGEwnfIr2Y2YXdfciJXmmRYmDtDuT0X60gzugyeIBGnS80wwFBijuii%2FxikfLc1MBYV5KldQYAooYM9n3eizLWuX7XXtyzw%2FKnyh24hyTHHbgN9J5LJU10u0iDPGFhQiu2%2FfY3W2O9ydOroRL2MZOTm0o9LeF9MJEMdoxtonOyl8JEYdf%2BBdFEjH7fX1KzanIfCLgDnsxpKr%2FzaIrVZik%2FQQT%2FcNc%2Fj3%2FDSk0a%2BLLC%2BI3Qu9VdfGA%2Bf1aqExaOselJQqGW6Fdsx4a%2FO8XdjoFPgvmGfiPHVUV511cuL2aqZKnhLf6v5iSkjEbuGwp2XivxaO9cHd79hTg0a%2FxiwQ4WtFyaLFixAh1JsUrq5kyyEvpNPC6AKrTihIlaYNOPnlmHu19JdwbJQrJn7a8ikjhDrPps2HqSv%2BZ7wcKH8Bd%2BqhG1uKVIFKq2v7zP7b2cuDbpw8a50feLAzrsRn3JbSQn1PBQltAoSAw6ajqvAY6pgGN35HscN4dF%2BrdF1X3HJxEVFESqqKXSDX4T3Hi9j4eEbN6EC%2BeZRDvIThAqcr0AV3gKk8VNHqTuEkmg%2FWI17EpMR0usITFjIptcVuAmRrr0%2F3m%2FAQwdmtOAEKh3OCTL8LG2SrZr3s6vSfSz2Aw%2FAT%2FoCgDr2wGglnBBNPLaJmdwmB4IWPLkzwXpHlXQwRVFlO0HROzVf1xnE5d%2Fz75zjWLeRNx6HpH&X-Amz-Signature=330b9dd6b7d548b3a77745e5a115e3ebe6416f646e8ef9bcffa001f477b34b4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MITKUVV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9EflfirHKqwYQBNxiJNSzrKkuutNWHvhAa5SvYPJjpAiAJE47Vjj%2F%2BDJfpgnLNqP46TBEb80nbWWUtrwr1LOBTuCqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe0410FAJjlbitympKtwDR5wz6JPulpn4JM4K5QLXeEk8hfRVpEcMvo6ZlCWKhYB1TeOHaLXQiIihGSY%2FH5lIJEwBoosBGZbS5pk4SQahzxMLlIoVAkmpKr8QnTgkpnWZejbLHaVhkUmWN%2FdMlwW4ug3DLOrDXsMu%2Bz7DJ9CCgW7cbYOGGEwnfIr2Y2YXdfciJXmmRYmDtDuT0X60gzugyeIBGnS80wwFBijuii%2FxikfLc1MBYV5KldQYAooYM9n3eizLWuX7XXtyzw%2FKnyh24hyTHHbgN9J5LJU10u0iDPGFhQiu2%2FfY3W2O9ydOroRL2MZOTm0o9LeF9MJEMdoxtonOyl8JEYdf%2BBdFEjH7fX1KzanIfCLgDnsxpKr%2FzaIrVZik%2FQQT%2FcNc%2Fj3%2FDSk0a%2BLLC%2BI3Qu9VdfGA%2Bf1aqExaOselJQqGW6Fdsx4a%2FO8XdjoFPgvmGfiPHVUV511cuL2aqZKnhLf6v5iSkjEbuGwp2XivxaO9cHd79hTg0a%2FxiwQ4WtFyaLFixAh1JsUrq5kyyEvpNPC6AKrTihIlaYNOPnlmHu19JdwbJQrJn7a8ikjhDrPps2HqSv%2BZ7wcKH8Bd%2BqhG1uKVIFKq2v7zP7b2cuDbpw8a50feLAzrsRn3JbSQn1PBQltAoSAw6ajqvAY6pgGN35HscN4dF%2BrdF1X3HJxEVFESqqKXSDX4T3Hi9j4eEbN6EC%2BeZRDvIThAqcr0AV3gKk8VNHqTuEkmg%2FWI17EpMR0usITFjIptcVuAmRrr0%2F3m%2FAQwdmtOAEKh3OCTL8LG2SrZr3s6vSfSz2Aw%2FAT%2FoCgDr2wGglnBBNPLaJmdwmB4IWPLkzwXpHlXQwRVFlO0HROzVf1xnE5d%2Fz75zjWLeRNx6HpH&X-Amz-Signature=dfc14b846769703ae0843a84c7a483a8c59cb17e5c13b98d4e3290ad1014b82b&X-Amz-SignedHeaders=host&x-id=GetObject)
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