

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642XCK6EV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQDzL1IwzfvKGQFqxUm2Xr00U7WBWor1dGyg%2B1Ka8nsJrAIhAOA0WijJrsT6Q1l%2BnUS0FE%2BC2cnGvr45OxcKEsWS1EbBKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwJKKX48n4CJ5XX9ZAq3APxhDyHzWtzBjTG2MXlQtP%2FeAfL0LLa7kZKwjk8NfoUnQ00pzgmHk%2FC2OQfofLX41cWVhpMY38MGY%2BB4NYx6EfRv31YaViayE0rNdn%2BEcRokZ6hmJue78u6%2Bt9xOA0YnKJ%2BCB3Sv82Ryk9fMcqI8EE6Ad6xAnyYE%2BZJyoCzX7vLxUg9pYWv3k2MZ1gnt9W%2B7glVeqQ21kytcvQRJoFLnyBOTzBuASuJFQFR8Fv%2FtLpg2Rcovnmk34hT5U0X8HtGQ6Oii9orJVxcfYT7w2W638LxaPeK%2BEBBRNxcEWu%2FCQ%2FQq%2Bj%2Bh2AFQi4xiWgjVInhFoOGTZMhdGPnN32VsqGSchmNrlP%2B4wBTH7zPPf2rlk6XIiSq9Ka62wGakSlc4NyYpP5QKei9bXWTBCRIskXs5cftqfhPrB%2B6UdVH4sk0o2In%2F0O3hgiCinq8WBEpa7ib0bravUe2EwwuUrRn0XvwqEu9f7bVtMPXkALKOxRp7DJnXk8tsztL3K2OG9azt8TvNmW86ggGltiEp3OmrM5N4qTHTgNV3C2ATSuVnPA%2BTT8E7bjeinuUgtSsHCRa6d%2Fyou0yc0HOxA1G7R6XSEdb%2Fr5uhkIU%2F8R1h2xfVaHTuodC96ZT1kTj1IElyvQYWTDNn%2Ba8BjqkATBgFifmvsPFiKN8BnughHPeUn0yGMXWKvT0%2FtSSf8761JEPSS8UK39GuiF1jLgWFc8bBu2mifzEwmEQq7G39l8npriScVayqPwNxYGvtW%2Bx36O3U6DGnFNSEC9%2F6aPedfBqN9cmWTJUXlb3R0Xqg2mbRRynEcZLUvyVAbT19hyycK7GJ1ZHxW4p%2FAt9xB%2FnfpJ1%2BPkSYgY0Ek92J7VQHLx5XzU8&X-Amz-Signature=cbf77a79646fcf4dae498f446a7dd55d431161230811bab268017477df9e4e0a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFF3OHVZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICLvIdOTK%2B0yzynhmezrW%2FyAzVZicJeId0Celwd5NH9TAiAZgKkA4FN0sFqrS6BKRuonb4Qzl%2BiMatWtutnA10M9FSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKjD1MV0cyEOMgRQ1KtwDQHZeuFvugj1%2FgcSumEXoGUFvFQSyLAYTjGC99bMx3FBb%2FzwvpP5QZG9qfn6A4HpVwJApJwE7YnZAbXtouG%2FOjkONcsfTP0IMBG%2FxrKSxhGkALAJXReGvuOACB7CmQkulhBQ%2F50zeJYRbVMEg%2BxPi65DiQmnMx6wxaZbP4ymopclMU4CWK7thJwRqt9eD8dOvkpaug3VAXJ5nMWW0ude2XiAxc0gFJKffXAHEwtuQ0pzAwCsXVfeysESaI2tih3mBAQ3FO9p85MOvbHzyw7OHHJajuUTfdorWqzzTdOWIMCB2qhoWg3mRyZ5VTA9R4jplkNvYrK0b5dLaYQCJzL0pZV6IQa%2B5RsSbNcfNJHguuSIn46YTTXbHZAM4ovIhXyV%2B%2B%2BREfN3tC4AFsQuRpsmISyCWja9TJtQ7pdCozyzDHwP7h%2BdVazO%2FhJQdJLkWsRkh%2Bi9NPQedZBX%2BzmsytVGW4jhqdyPQB7NuKP8%2FU7avW83wsib9VtELdcqoX7eKGysUfeXPPGRnd2X%2BWBC8OzWsA9w1NJsOCKVIwOKQ5tL16G67ygrlfN%2BG7h0wie1YQeIlb8At2VO%2FwiPszHt13GjVJPp0nhc9w%2BZECCNMjJpYM2jligiqkIKr9u4rzNYw0Z%2FmvAY6pgGNePEFzMWGJr5aSk16U1F3LrkGBphKJuVL6OeHRi4VDzaSC21x2aL3%2FXno2BGncIBgcys6Qn831gAZFYOazbU2Q3HXusBtEONX5FCcAJlTG8f%2FQAQmFKZ2CfGaWJbu%2B%2BmzTV42riwk8liQbGtP%2BFT7wOyr5mODViikZLnEXlA0VzNPm10cDdcOvep5CACewFaCgOCxg2LwyK7XqOBWr6wC1XRTOQ2j&X-Amz-Signature=439f4f3e959e044efd7569f79c2d06d671865701893f8b391680d8ff82419b60&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EE267KP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIGvGq3FylNMBzzk%2BAKbYJ9jXp%2B8zaJXT99by9EE9h1n%2BAiEAxRtwKHTJzq9JsG7cogFMHZXAm%2F4iIPlt3wwkv6Meb1QqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNySaKNOl13SSZSrjCrcAwTUcEEeUugDW8cLHsE2utummmyTJlAKteqFpVsHstVIbQQQYdfOIwElDwe9bRptv6bDtOawm3LciyM01YMbt3iG%2Br%2FG7cOkD9oan0lZIvjCHVeGDDPGfBvvUZb8Qsmt20iDAh5fdWT8oJ%2BDODJKATUDKXHpaPsAtMlwNo6xAyposJrXIx3J7K2HkeurxDQLZh1qLUQpwMKeU4EuJIkoxjKhF0GfvlRXa7ViyAdzFZ04WN1GSmgHhd%2F1Vk4xN24HDYMSgYmZ7WoYqtrEu1iLRMhcUsjsjVR3UT7VVoy2YN5y6o1xcwnhwYIM6T8kCF0TmwDcOQbmrudp6DeE7Op3la4N4ziDxx6WAikEAXrmjKZv9HyMGYY1nPkNIiug3ABXt39%2FjSNPzILMORTFQDwHtVRvclg%2FcPGnJVf20jnfaD9BbekUvy5oVULVQT3UD%2B1ZBXM1x%2FDGvzfV%2F2EPzhdL1eS3UVYHS98rtsDyUEjGPVRNxK1TDJLoBHkdBXxQeAA0AmdrN8F6ad5bM1emgMN7ZoWyu62ECuaLgELoh%2BOaGCjxoMheLgDR21NPRjpT%2FgHwSCKb5WIhdBfFPCQTUc99qbPxFNTuaSY8HdzoR0lxIVGNvwj%2BJJ9wvJXHnSdoMLmf5rwGOqUBLuIpgk9nRtarpQneE0%2BGDGJ6IoylCeohGKliSZ4kCHhugZf2IUI1Fb5dq1umbg1zXDd%2BLsStglEb7Iz78TFhvmfBBCiN9Mnf%2F1XIGxWLHVYKlqiKvT3onAP6hOTZWPdYjz0RHSpwmwqFXN2h2AjXoxuLxDBEgP%2FgyDR6sKbdRx%2Fa7pN5L%2FW8VpSrW6X0rUV8RoSd12QB6kepwtm5ygt0lDxP9NLv&X-Amz-Signature=4b6208a265cd9c421e88c6536d8c1047e5fe567cad46d55a064c3f4c49bb1515&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NOBICTP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCmck8dQPtteC9vuRae7DoaZr1%2Bj2x9TtmRFln7XjGVBwIgCPiE5ntO%2B2IORaNeGYj7XVVBlzxDnm%2Fdo03vo0wH5zAqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIWujEvEY1qjOVo7CrcAwGQCK74AuzL%2F8HF1WAomsKJwnah1mESPIjcocfIn1bbcIXCgv75AGUamwRUMqSTMSLJlhX0C8qTHXeqyUyVgO5axzPGmnoFq1ZnjNvHG31G%2F%2BOIeSin3znwle5%2FZYg5g%2FqTilVDwi5P%2BEjvfzynjPhOQ2Zpd8R2vKVrcAYA%2FW%2B14%2FQ%2BXh1wYmU%2F2%2FNai8VK1NFd%2FTW0%2F%2BHNA5N54cJ2CsrJKTSaga9sKb6X9tE4hi61LNfUgM9ZrcA9zZswdeCW4uYTUxITH5fBehFmIOPqjidzib%2FPvDI6T9BNRwTBWSMyNPXkbbWzLBg5%2B0j5%2FtOzEQ0i18kbbKpXDCPCrq7g44Tffp%2B7G63hfxmomrgxCVt9I6qdYvn3UfWF5POUPO84zFxlVy2NRJypGLHRRXd1Ar1ocg6ohz0sG0DUKex879SfTQo587Q%2FknDUJEODA4kvL97O1Mg6FgJ%2FxNPJHw0yaGF8DvqRVCmDwwiD4zZX71Yz2pQ7zwOAifBv9Z3wlNNo5NymDMJERuevwp%2BEV0kYWDzB8M0Yh41XVBX9viJ9H4pbGbGUxBbJpqFo4JOyW92sPezGSc8P38KeBiIitJtoW3Vf7PIApsIvP4gbO6Dytw85UNPSsfJwFfGTqMWLMN%2Bf5rwGOqUBJkzoOXxMFSmv0JG2X3%2BrJApBp68EzzQ3ktQoFFgE%2BEY9lyBIj4Lh07YzHsG9kGW2cEhn2T1qPtYYeIdHrhH4TqrNjIBoxMf5loLHPAqkJ%2BYDc17bO2ytzyHBcPiLvjI7Tydhbqtx%2BNnC8caGSvALF6qGdneEYGtaBdBWskNy2sO1YRO8S%2BUr5irWO0n8i43y389SpG5BL117q4uVOI7Hg3BhivLf&X-Amz-Signature=314c672971b7717b7656eb5fd0b651b1308bbddce73bd85c8fdba4c23d62b835&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2KNBMMQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCUGdBRCK5mCQXFoqUoo%2BRJqgy17OcoNMk0%2Fuw4nnjJkQIgYiAwsR7S4zaxyZqQ6a%2BrMJAjFJ0CQJwwKluQEXAzSy4qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNylE3D7zuUh0U2peSrcA6XAx2zXHcpt2rZhxfk3%2BP1Kff1bEMuNTzySK0HEJoh31NFpttivlzwOJQJk3BoTrGpm1EseG6Fj2UyxfK20eYaqUyzCo%2BS1EHjkSP73zTbVn9ZhSCrGxPNNPWvn1egjpK6Zve8v079v6ygy749tP192EXU9Uhux%2BVSHXuKDjUlzfpjCIvFVhCInsh%2FN4SNN0R6Ao%2BGv%2B6ippsnp5b%2FbYsXNpEXmfsimy9wkGSAde%2FtXUeOYqBgGlnJ%2Bs1eRMq7NuBdBkMve%2FIPawVee10FrriTBqbjF6pcCvOsN6NfUGfEsbyXQnBs7pVpHoIGt0srci7%2FmS%2FGvlrBQWRhL7sMWkj%2FMhb2PUx9lBSRGmi3%2B%2FCdugbvRdirAhn2mHGrEpcqudNgYPaDvhMOFiholSsLi3yddTaMzS6zGh%2FiBU3WcjhmaaiwSwpk45h3LxXW2%2F5AA9XrsAiGKjqDWjD8dRcDK7i7VE%2F2196K5sJoRQgHty7HXX0m9JMQJXalku74s9EZ7O%2F7s%2Bj5ZFkDx698wW6H14q%2F1oBgzVcFUlqDOy%2Fldkyi9NCqjV0i%2FeYxJM3GCny0Ye%2Fb38BkOQ5f5UoHeO23c2%2Fq4XLfRHin37wu1pn8fgze7wjamcLQsC%2ByOvhzIMLmg5rwGOqUBUlU5KaWePvrf9dn2lW2IaBbxWPlVOlOpF1TRCzuYPp3ENnEBPSsre%2FFnOyBY6JNNNqIVcoYG2748E82rBFAeN6JjKqR22o5CmGUUBKtjUQERXhwc1tiGCmRk95h54a8y8EjUJGi%2BTuebYX7Q0vrAm8qNDrfxkcxx91B1iSEZx3gwQAPO2gxozkBOVUVEQi5R5xaqP2cRqL%2BNNehKDCXwEtu2eCNI&X-Amz-Signature=e3665e775c4a9108e58037b5c093145d8db61dd0d4462345cb7a4d5c14fc4814&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646Q22VFK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIDbDhqwY48qmwJkfLwTjeNbOOtv28PBTfTUoJ%2FXOSH2BAiEAiMUJs%2BI3CAlKxp15%2BlZS%2FhuaxbGnwZuvJiLUV%2BhUQf8qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDIUCsTYa4LVspK37CrcA15xx6bZy0SOL2DzSB0xf%2BudGczkPqoHyQ7dTkoy6ONUXx4xzeQG034Oa2YVCTlPeZKvs%2FZIq6XtOYzLqiCLzHnc18Fwl8N8TvMGMrsoXc3LQwxCcJutlcs5y6dWkAil0WmUDkwzSbrtX5A6Ea9xJSRNzWZGVGYM%2FzdvU970kBnlogjcP%2B2gjDXT7XL%2FJtNBYMeSIKTmAGN0lgsYaObkm%2BclYD56YhFmKfz5e8%2Bei2dJ2c8SM7vdLjVwcQLojMGIruj5srg1CSrH63bdNAJPB65PVTtJTqEg8KaiacG7qzyGHF9E1TR1E4gfZefaw1I0iA8ZIpWR%2BbO8BCNWdBdfaytn%2Fvf%2BYn2G%2BwEG90MZ8Mn%2FylEfdAYsBSEVZyTpwV7NJpvZzW8X7AbIVZo%2BHYipGrBhHkFxMph%2BBRqJgfaGxBIqs%2BMCtOciBzGHAkWD9gzTjRRtdlSWsBePqTyADWB%2BE0cAezWC2LhwkXu7usSSHfFjjiKt7VL3WNSbnxiRcV193Ceey1CovV9DMLeRUu6UfRYkHfD%2FRzQSXMFvDNDb%2B%2FTyt%2Fhb19U%2F2IhO5LnaRc%2FinEcNFrbiOy5C651N65EuTszM1DGK%2B9%2BCzQ1%2BCNWjnIdoQcEEYsE4EcHgMFE4MNaf5rwGOqUBD7ntTsKyeVoowyUPIf7aG8qDQXLS%2FxnW2Jcx5d2cXa8Ow9f2E%2BGUmYF1jTp1CuPvUbPjMZD3EZ4WkhfJlKQmoUrSE0iSHTJLsmMQ32vHHH713JZ4FPHxOpeo6y62L4V25AqPKejN23fPye%2BqRDRzcmHvsAGDB9ZczMvUfVepce0PDlnlrSCLGkPhw1msdzzcgUXTIeBpg%2FglMX8u9m5R%2Fxx0tucE&X-Amz-Signature=e514eca0e025cdfe7bf8d3fa80baff113b5cd46d492d092109a67cb2bdb0a1b5&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FNHONEE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCfrimaR%2Fq90lmlPAX4dmkIQeg59YDNyv%2B%2F2zV6D3npfgIhAN1SVn9NIRDCciWDYQO%2B%2FKUaVFANDKJ%2B0tlxxaxvlKk9KogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwv7ON6D8lXiqcUGyYq3AN1NRp7%2B8uuaJzckKurSM0SPhXdlZT20HfL6LQMtAR5yemtUAgZdsJX9OZ7XWtNhNTeOZFlF3mL4NOy2zYfSiaNqyjDX9QeezEpoaWTpABsYD14aoHO3FUDUwIUonNbvu1yrDpF8EjttlxtTMsZq0PPOgcF%2FLvtSFZlQ7f%2Fz2K4kaEutoIA%2BMpl1kdMmRnLrhKww0I4FYBmDEXv6K%2FZs3gKiUNERZ%2BrHJFKSe%2B13oU5eQjWoP7XLIDncgYJd8UBoqedzJXWitugrI1AgOyDDRB2cjkF7j2xZydOSgB5aeqJtsBMhReH80W3DMeOph5Y2HAW42iPrFc8cpgkdDy4wytSc3j3PifigTntslXV5wqnquSAaWiHYH1C6u8OTlx6EleofhbrU%2BEDGLAGChYFyCqfkqp46LuZfkz%2FHLlEESV3oJfnie2woOStPRFieFpodZkBMO3Rszi0k2sw1%2BW6nECb4Gw2l1YXJ%2Bjjg4fs5WdhMDf19ik5%2FLL%2Bgja89GTvnL5%2FeeEDwK4DvF1dPWecUal%2FO5BQdqLtbBpIB6rDaTgmF5INOQirIozCmMvH7MnEsIpU2hPBlSPvS%2F%2BkNptnqElguEK80TxLZrnnqmhNssPO29qHuzo4jPwBD4h2ljCOoOa8BjqkAex1P6QomBEXDK%2BaUZOGGrVyrTRyj36kWpomkvlf4O6r2cCi20%2Bxs0kyfkbobozYiYAxjb%2B4r%2B4YkDr3fBPFoQn6wqrX4PRoATrlSnyz0%2FIGc7EMqY3sH4OdPWFQFjCKWwJzz6HecU06KQ5TUNzLvTqQ0t%2ByCIvY7J1UTZIJWzSHcrX7uf58Wz%2F2QW75e%2Fubl3zMoVkGg44EyoRj88VF7QQYS%2Fei&X-Amz-Signature=90b7bc0d6755b3b4d6f805e144d8da6053924d092c10b8e542b976c7ff2fb3e6&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMV3OUPO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCID8VCLvvLBqkFMfP%2FPV39EcnHRgXduZR5plvVPvvfA3EAiAeOrwVce9S%2FjRddN3aioLiOtBwcDvU3LyyG0TUir%2Bs5yqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoewWBXPEOySEjUmHKtwDsQ0ebfcNbdxyErEsFw7rGQev0hImMlBtKqEgcRaasAQHCJVuP0yPfZY%2FBi7Fa0NDGNKAPx4qtFkUwW4tTxa6XjiUHN8nw8TbhL%2FuvPim7k9IJnOLQrh4gIetcG5C5ncMgvMnGik3at7FgahLCRcHSz7oSSte81NEj0a4q6OcxzPiBzeOAbsu22P5G%2BBSPFz%2F9%2BlB0NfLvaVjbiZo4ClOCA%2Bm9feHtbwOORgtmOkzJPphQnVDfrJi0fr%2FGggt5RCbX7GrA6SNf8oakRA1dA025DhypqK1qstsLLlc8ayRe28SOREvRgn7hTmZq4JgH26Zi%2FBKX2YTD0bnXR2LEisZz1u1ktc6CCQALNyUbIOpabZ7LlPSrwXwV8PigTXPctjns9xUiGN2VTH2Q32AmN9LOwCNlcBVSES%2BsPiN2pFoNGa7%2BGaDbKjKYfsW8YpS0vmHsbKYhtuY0czQN3MwFge3WCgAYBeOg0kgcJ%2FEoqX2NYB7qEKby%2FIbQMHu9TwfIFMZUPNYNd0q8ysUyt07A9au1UufF5vSZtKWjXoHUaOUuFwqHfpdlHNYZLazTxrL26eFuOwPYfYeRuEn7NYW5FsbBY8R1O%2Fa1ZUJxdoppuD1OMAK7yX4bLQnXxZDo0AwvaDmvAY6pgFkD1K%2FAvp4LMquxtdmwAMjPe%2F7lrhrQT6p8%2F7JfAct3Ls%2B1j9MUCiVr%2FowCFXvhlfG9x6g%2BLbekP2iEArG237aZTANe52k2xCYL7gujmXCxjb5bPJEZruriCqJTg1V4c%2B04bgNq%2BrGnKgl%2FqEgXpYO5KaWOTWD1aBr0iAfnelPWkJ4oHMnOWNQJoW3TWJzaMeDXbeBcPIArmNHPaEOoONPOI9ZxADW&X-Amz-Signature=dd0f5a0949415da233ee4dd2c77de1947d6360138fea7a1903f79bdf08c7454d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2KNBMMQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCUGdBRCK5mCQXFoqUoo%2BRJqgy17OcoNMk0%2Fuw4nnjJkQIgYiAwsR7S4zaxyZqQ6a%2BrMJAjFJ0CQJwwKluQEXAzSy4qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNylE3D7zuUh0U2peSrcA6XAx2zXHcpt2rZhxfk3%2BP1Kff1bEMuNTzySK0HEJoh31NFpttivlzwOJQJk3BoTrGpm1EseG6Fj2UyxfK20eYaqUyzCo%2BS1EHjkSP73zTbVn9ZhSCrGxPNNPWvn1egjpK6Zve8v079v6ygy749tP192EXU9Uhux%2BVSHXuKDjUlzfpjCIvFVhCInsh%2FN4SNN0R6Ao%2BGv%2B6ippsnp5b%2FbYsXNpEXmfsimy9wkGSAde%2FtXUeOYqBgGlnJ%2Bs1eRMq7NuBdBkMve%2FIPawVee10FrriTBqbjF6pcCvOsN6NfUGfEsbyXQnBs7pVpHoIGt0srci7%2FmS%2FGvlrBQWRhL7sMWkj%2FMhb2PUx9lBSRGmi3%2B%2FCdugbvRdirAhn2mHGrEpcqudNgYPaDvhMOFiholSsLi3yddTaMzS6zGh%2FiBU3WcjhmaaiwSwpk45h3LxXW2%2F5AA9XrsAiGKjqDWjD8dRcDK7i7VE%2F2196K5sJoRQgHty7HXX0m9JMQJXalku74s9EZ7O%2F7s%2Bj5ZFkDx698wW6H14q%2F1oBgzVcFUlqDOy%2Fldkyi9NCqjV0i%2FeYxJM3GCny0Ye%2Fb38BkOQ5f5UoHeO23c2%2Fq4XLfRHin37wu1pn8fgze7wjamcLQsC%2ByOvhzIMLmg5rwGOqUBUlU5KaWePvrf9dn2lW2IaBbxWPlVOlOpF1TRCzuYPp3ENnEBPSsre%2FFnOyBY6JNNNqIVcoYG2748E82rBFAeN6JjKqR22o5CmGUUBKtjUQERXhwc1tiGCmRk95h54a8y8EjUJGi%2BTuebYX7Q0vrAm8qNDrfxkcxx91B1iSEZx3gwQAPO2gxozkBOVUVEQi5R5xaqP2cRqL%2BNNehKDCXwEtu2eCNI&X-Amz-Signature=7c113d2db7321b25c2ecdbc84d33ba947b8d961802fdb04774ab110c95ba7d36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVBJU234%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCxJ1RXJ8YjzQyRohbrXkDHb7BVIluEAC8Tcm6CVMfKvwIgfXJFQszG64uifC0exPS3ztHPOSizrPFDdQkYWZEeM0sqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGS%2BCy5iBwf8q02oqyrcA1KkrIrizxaFXIJ2ch7V38wE8FINSS%2FcWs%2FlLPfGXeJlikisBFs29OOzjuKxHxnfY6r4YBor6NkT08F4Mi0vD63Pn9xi6BHaaz21B1lYzA25rb0XD1Id8UQaGhawyhqsLR1ZuUvQkPyYxZVbbCKd4L2UshnJHl8tkLhJ%2FN4VnDY%2Bi%2BZ8bQzRkwe%2BcqOAWGlI1Poznhfgv6z893CMJtVaOrR1fNsRtG1eXoNViY1oKV2r8201gmWx1RWl0KiGpSlBsFUZHnKjkU%2B3N41gsRK3Sg2cXxKBcOi8JAshaWVrHGTbpqYVgw9ReWgGztH%2BFfIlkKA%2F3mjQodZ%2FT4oeuNoMMRUGO3nrAFOvbqPFADoxJG4fHCk2q2QnHD3u9H6GncEefdRSMsKS7pUzKrXgXPkQWY2B00EbvseQc%2FRehbV9AC4e7AZkvK6NK9KUZ4oJzZOwEiz3jLuyLYQeGbztYTMWuApUisOASSlIYMNk%2BoT5EG2p412iD6G67BC04kEpEmbarmZK%2BbI254eoG3J4yqlkmZHJoEoH8yjvztc32C9JiWhT8%2FnDDZ732A0buimNWixvQQAJRCQV2kmZBayn8CIYCho5PZsnVNm99btgb4nUXiPV%2FOq03Nj8dV2JupDgMLGg5rwGOqUBG%2B2bTabP%2BPqSol3RZu0N2fI4fsi2S97cxAUNFQGeu58G5%2FUAI%2BAh4rFELTtPFQQGgT21t4pj9de5WLXqnqgY70VG20NONPqudqbFCARVH%2Ftptp76rbLbf5VKCsuBC4rtRyrmXPIDjkHzlzJLC1Gfm1lz3DdqMlT0VHZLa8QtnvmJ64rFEueJHFeiz1jB%2FOuEGJv4gnzhoSXAAahXpmxyywNU3uwK&X-Amz-Signature=edeeeb706211188a0ec9372f5215ac500e84a8f3477fac818e05d6f09fe9dcb6&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVBJU234%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCxJ1RXJ8YjzQyRohbrXkDHb7BVIluEAC8Tcm6CVMfKvwIgfXJFQszG64uifC0exPS3ztHPOSizrPFDdQkYWZEeM0sqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGS%2BCy5iBwf8q02oqyrcA1KkrIrizxaFXIJ2ch7V38wE8FINSS%2FcWs%2FlLPfGXeJlikisBFs29OOzjuKxHxnfY6r4YBor6NkT08F4Mi0vD63Pn9xi6BHaaz21B1lYzA25rb0XD1Id8UQaGhawyhqsLR1ZuUvQkPyYxZVbbCKd4L2UshnJHl8tkLhJ%2FN4VnDY%2Bi%2BZ8bQzRkwe%2BcqOAWGlI1Poznhfgv6z893CMJtVaOrR1fNsRtG1eXoNViY1oKV2r8201gmWx1RWl0KiGpSlBsFUZHnKjkU%2B3N41gsRK3Sg2cXxKBcOi8JAshaWVrHGTbpqYVgw9ReWgGztH%2BFfIlkKA%2F3mjQodZ%2FT4oeuNoMMRUGO3nrAFOvbqPFADoxJG4fHCk2q2QnHD3u9H6GncEefdRSMsKS7pUzKrXgXPkQWY2B00EbvseQc%2FRehbV9AC4e7AZkvK6NK9KUZ4oJzZOwEiz3jLuyLYQeGbztYTMWuApUisOASSlIYMNk%2BoT5EG2p412iD6G67BC04kEpEmbarmZK%2BbI254eoG3J4yqlkmZHJoEoH8yjvztc32C9JiWhT8%2FnDDZ732A0buimNWixvQQAJRCQV2kmZBayn8CIYCho5PZsnVNm99btgb4nUXiPV%2FOq03Nj8dV2JupDgMLGg5rwGOqUBG%2B2bTabP%2BPqSol3RZu0N2fI4fsi2S97cxAUNFQGeu58G5%2FUAI%2BAh4rFELTtPFQQGgT21t4pj9de5WLXqnqgY70VG20NONPqudqbFCARVH%2Ftptp76rbLbf5VKCsuBC4rtRyrmXPIDjkHzlzJLC1Gfm1lz3DdqMlT0VHZLa8QtnvmJ64rFEueJHFeiz1jB%2FOuEGJv4gnzhoSXAAahXpmxyywNU3uwK&X-Amz-Signature=60e4e6dc4e39a77f6b4c40c093f94d66228edda86007a395bb39bba1442b0b79&X-Amz-SignedHeaders=host&x-id=GetObject)
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