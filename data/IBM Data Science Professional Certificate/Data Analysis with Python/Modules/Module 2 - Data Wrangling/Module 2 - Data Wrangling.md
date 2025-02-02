

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6PFYQKX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHVje0nuwbWb9WblDpkWvlO8a6X8b2OYEbBfrGqsFdBTAiAJqogrClYtABJimPumq5qGJwNk5snNET8fDwsuB%2BPxjSqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcyDIYgKk43dtOuHjKtwDTnWewUBQ9OF5S5qk2lMJCOkICvTEYSr%2BCFDOxPdd8VEwO8GJIrornmBrxX8d8dJm63Wl5qaRO2ErJt0HiTUhFA%2FCKGPmeuWENax%2F5V1hyOD82zBxdcE%2B%2F6icrQxDShkrS4F65U3PyElLTCPqJZ%2FuoGAXfW62sgQG6C9U4098cAsBILhCvq28dOWkFwkrYigkGFqANcdGU6s0Hw76aVzR7FlXRxjCqZyRYbq8efwWu2yczu1XGAF2gUtOSyd%2FzefQBzd5f3tW%2BU2x5wHAOoD0qjBD5%2FN0RWtxVwVl4p080%2BTkP2uEIK7CF9%2B80NHC3YP14ygN2c%2BHpu8AaMWCsQ6reuSW6C0W0bm%2BrJhk6EcAW1yT5emdo98HMC%2F3YA72bza9AZOLSOO6AzaAfEuFjdLAWWZrzBY%2BretSTIyvv7Q2vDOB51gKl86VC9%2BMmmWK8a9Ann4RsFP1lsBdr6veCoQ9vVX4qwj6OoYMhwUy3RM3YIeU%2FI4OvZ5zk35D8mbxlvJJ3OiwyvGgoY6vevyPMg6ehu0UUMRD4UrawGOArfe63ETvyrU%2B3FyWclnqHd4bfbUTAmFjXU2Jt7p%2FWo1thWxRSAJuyVaBCvkQ0%2FK26j8t2qF8PaBG3YuJy49lXHww9br7vAY6pgFOIHgs030ljsizNbJhlNRT2AXMX%2FttoD22pDf9Zj4b9ScrePkT5BSFuVtyxco45xXGHFZcEhvCH%2BYQrNrC5lpicEtuC6refrdYqI%2Bnu8bGzg2hmpm6lDm7er4pm%2FIasUC6pfEbrUBrQ5rGQTAWLw1CEnS5x8J8gSz%2BD%2BnsWrPVe%2FBeTWT40dMql6D4QPXYT6kb3jabHhc8Ro87fu9sKfNmWm%2FRJz3c&X-Amz-Signature=0003ce9c7908ef4c4eba11c4305012d885cc71b302bd1b9efb1e351c7a8066ae&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXYS6KMX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSnGQQYeHlliUHbaraGt4Sg%2BKO5jUfwBsxFnzNhrpyVwIgB4uQ6NpM39Voja%2FYIXuGBxOKLzsjFDn6ZLaisFforMgqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPlQW9bjUgQH8gFVdCrcA8y8IB0q2uNhJsHEHv69JbDTSzZTxxAUzp%2F76N7xKzud37vhZUgqRoN1vva9lRugHPDuSuXqO3QnbCQnTxRkMdDba8RZfaU7DeiA57a7OOlw2sJZME3jAU12EdmxgZvTkHVu6yzv5IrBS1shKt6w95ucN4rbI9jk4qmOOhpERoZ1WfJv36ElTRPrEa%2FVTBgSdw9ogJTvYiQSF0zpdno0TSCR3FQx2l6p4x0MH515L7R4Lo%2FyWglaNXyq8%2Bd8ktNC9NSH9Kp28If1YSWbLkGg4ydCVzaV0asD1JIpYgDlS9E%2B%2FW0GlhPpJ7KBXuOuBJAd2WDsh0ZG7ODMINVe9jpwHAXeNxcPIfGHg7Szz4UbKfnqYM7j24mKwvcdOa3lY5mRYPgVpD1yCUqad6ona%2BMZ71oHf8rHT9E%2F3kDE8KSqN%2FIZq6TgCBsCafrPrOEY33V2qpCtsDVifzt3NBCCCfDtRms3FPdKq1DbZSrfLTXT9JvJxluEmYQW5xJ1ArAIlHnKsS5gyb%2BN0k6PNT%2FnR%2B6j%2BsEClxRoYPFpBek1Wutb9iAjX4PoKDN1WpLVUDt55aeJ%2BTnj%2BhSlP2Q4Ye9BQCTzXNdf9SgVjYriaT93vXOfLokBCLEzUoBywzFlWfRpMJu7%2B7wGOqUB8T1ctrMgYX2dZgJFb1LmKRAgSeqlM9vdOC%2FukS%2BWupcvag8MOz9xkusvfZQfd0aOX7BmNhTsFWkw2q1H4%2FvX01DjGUSdSSU6kjM1QYcOvR9t%2FgkTq4E4gGkUY9zJs36%2FBskPUgK4smXa4aS%2Be4V%2FXdM9h8bFyio4Z3A4I8hpL8tpPUNfK6oPLaaXoPHx8HtDWng1e72S3T%2Fj9dnuukJXHordQQQD&X-Amz-Signature=cbab7e7728ba425fe6c6ae4e91ea862d4c0a5b42b4b7c6cf08a7fb2071213d61&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SLWXT2X%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIENF5PBfNVGUntTP1QizZAir%2FYbNxhg7vIMJQznzAolxAiEAiYICloUuHtPtIDgMMAGtRNNjWIarQBFs2gJb0HP%2BXgIqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMFMYuN0kgmj7G8UyrcA%2BoSpuYs5EPatJeaGSoCIha%2BIKrvttrsdF0hOwqeE3bfZXLNFT6toxd7fCUc9GWrNhaC5uivK%2Byws8fVykxpRdu2PVZUhkOQp8Gu9rrX11I1KlsnDuhAhNh8wxybTJ7JDv6Q1RYnElX1bBZFey8vpBaN7DRxyANCUqEh%2BPFI4zFyH80AgwJJx17a94legZOcyqSmYM%2FUhemBxtc07mn55Ynt9pG7hW%2FTXBD21ytwdqS%2FrkBusJrXKdKfAY3geJjTO4dAE2jhtl%2BntY6K8Wk636o%2B0IMEueorGqiXFi3qsGxN1Cdbt7QdLS%2FQJX6kf5hPzWxSDTi85AcuziToI2EHe457KPcvRDYD5t%2FGO4URO5565VwWXX8FlbkHOu%2FmVuAXwlOLTS91W%2BDmEe3vFODTOzvYOQddw1nYId6vlfbFFV1IGk0LWqAvuWUyNldL2bdqGWfJTz8ww14T6RMsTkmWgAuXkldXNFQ0O4OiLMkSnkUdQLihSuZrWhwAOnmP%2BV0qvAJsvxJPsQ9fSYier2s0sJmfwvhQYPANocD%2FPcG8axjOldW%2BuTnPfQtOkVzai4EaJVO8cJM5ObTFf9ICnYqx%2FlH%2BY1casIK4TcCugh98CIwZbJpcS%2BsdZ6%2Ft3SWAMOq6%2B7wGOqUBJLVUMDL7uaptYTpYIEA1OlvdzsW%2FG3CwvtdH6gmhp1TbzVzZnEfjz42ZqIVB8DaCW3uSm5N29axCO4rIe7fZjdqDz1pVr8DpBrMQXpGqzavDiHcQfUs6IuNdMiUvwSJIvt88S6Yzs5yaFg1EjGQIsKp9XhGd9XPBljsYhecIM4jLmOS%2FLZ5MY%2FF%2FeR3vdEQUtVjcyoH%2B9qnQk4mMEkcGg3HrkaVX&X-Amz-Signature=2cc9883c5db8e9a6680e82311de6ee923124d9391b55fd9ed335f187d399f3f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PCQZPPS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEIvUhI%2FG5ijua16BXoXZBrTbBDOJ%2BraCtJbRproNoFBAiBn3WDOCAwr1OU%2BciU3To%2FejfskcTURpmOG0KjzEgjvHyqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhzBl%2BSbHBBtbB6%2BpKtwDvRSG1ivbvJ5%2FZQdrThN%2FM7qcxGS1AvRFXMTi8B%2FXsiyDexxWapMqN30ccvCyWkvz0Eu7eYS6mDNn%2FnHlemPLy%2B%2Bj4l7islbjJkMLAfAeuLgKFweOclxa%2BXk3y2Mh0docpobZEmLZUhKy%2FIcSUNHcoCxamokWi0OflLpHlFZJ%2BtagcbHJpB6qckvYlFx4ljdwY1ter5r1DIZRvMRFHe7H3Z8zDO2soIS8v3R%2B%2FlxryWxdKrRkaIMVUguzR6q4Zt5vC%2FHwt64uv83vHQzyr%2BdJtyuBeI4zXAj%2B4sNX8wVcXuW5Pgq8Py2hRPFn74Oag7FCruRjrGnNqhs7nhX%2FlBamnXZAqCqAZ5SDLQ1sDhmK%2F4rB0CdW66dHQCNc8bsow2BmdsvgxGRaCa7eLmjjUkVPHPOD50Ei76eVubtae1PyPYa0Xr6wD45yTodjcdCXgtHu8LdgEOXsMcprWbZ0%2F9VhJ%2Fy0xhOK6sIAybiYNgMx2CfQIWAHXtz9W9SO%2F13Fzih4xDhvVu8MsjR0RQ83Fus61SUi2XrO2TKWeGTjm4SF88rbaelPlDle0KPWRQURRe4vRVlhYLTPSR%2B%2FEAkG9I6yt%2BYz3teTlpleCnKkjIbnl4xexF91GFfnao8RiAwwpbv7vAY6pgFGx0o5T3VjuxexU3Uq3WsKaCpDFKXEOJ4gust%2ByhEOczbgDGCe5w%2B8VP2w7R%2BcRAfrVxArvKBV7z0%2FeKGVPsBrZYB4RTRjt8uEdMCGdTIsqp97ly6OtuXpQvKzcPpROFpWyDub74wjd5l33hQAacqhhasoh6wFCWCBlWbEpzXlK1Xe63d0fWox5UMQ%2FqD1MIKlTzoGrZp3Ql%2F4yYiY2Pt2yZUxo3W8&X-Amz-Signature=5601db3a5b75e62ff4be711a14e5af99f9472653947e78a34d6a35c6cb35de82&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWDHUO6Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjcuW1QHWcNEJWmYhBHQezubN4l84Y1e5W%2FrcNPi60MAiEA5Yz71GHOquDePAoZVyuUWP5Y%2F4zqQe5NLGq9piKAm18qiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJUiqOXnHkIzN8rk2ircAzlVLb%2BsZpMs2KT2hQmIbT7BUw%2F5uX2zoQ2hTSrPSUekTMbokqOAavo3jTd%2FmPtDeHBUomlv3uOxvC7FzqV6XqjcnzXGKC8%2BBvot8CDoB1VsQIBBrRv7wdk3DFzlqHfOFFP0nErWoPx5VU4JEDozElJiG6F1mpvp7dnWs%2FyRwRzqH8E7dts5efPrl7yidqudREJMz%2BZKKXaM8gBNWVBuzYDZ7Fhfqhz64nkIonzM3F3RJli6WrJ9NYxeMKU7GhQIZSW5dI3l1yY6H67CbCOXbtAwTLGRvtxfMs81aVqXmmRSXYZNzj5%2BxKbD4mpq3Kn1lRFFT4OJX3gt1SudNkDoF69MC0UnkecgqJwDKPZanGIkajZHsittcg6W%2B6xanHdIbccHCQPx7ayARt9bTTDYDqeomz%2F%2FJVbbBjFK59XrKG6KW9EBCfKjdM4Ahu77jcelVWkriUjQhJjPc%2BE19%2BnZqfM6lBPLXFBxZPEMVTLYYWb1YZ0rnAUaNiHzW56NQaSx2EruS3JyrqL7xEQ6uY4Qdat35R78IUJxB0SNm9BZrOSKprfj9OqplIWoi2BfKv0ov2K%2BZGlVnnQ1hnkCaaK9vpKLrQGjB2sMTWMDDjDVWVhtxfJm3dIv4CoTFxTbMNy6%2B7wGOqUBrmqZni6PSEAFEZUrHsDS0dUcdqrSyDkhnrpUdus7q%2Fpu8EKUyKm5geMZZWUb5z1tZgG1KAB5GMQ0HDh1UnWfaYhXpFP9GZhu3EzV4%2BjvZC2prYu%2BBcnjaYsf20v6yBMSSwN3Ht7IXNQJOsCrY2SuPrBe3f%2FMzGdzYJ5Xgr1Z48BcJzUyvyZI6KgJfK5OT5fB%2B1bToNaA1lzfk6m3xfrEcU6%2FxNIL&X-Amz-Signature=cba4897eb54176a917e3d7b4207d44a57bb98d23add675ce2642dc210096371c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DX6YSUI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBUltq%2BoLclCGt4WcPGZJ3WvMAJoGFM4DtnEojuAgUoGAiA4jrl96mJL3BRfdzgbVh6gHW0%2FR85l1OYa8kGA5AEpxiqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7MEMR%2FIpJqNMAQrDKtwDH4lIDx24V19laNdTG1Z%2Bz8blOp5dcUoYAsn5WIqG5z5xW66zMUcwmQSoAnjvql9t38nhHHIhAwy8860el%2B8O4moV%2F3Q%2F1z7ca1Ilj9sEPu5orIJ8%2Fltdey9FKsK7gV0RoAOuO6MDz5Qa%2FE5LJdbrxmoCqNgDbHXVpjmj1sklbcwwcl1cTw2jALC5%2F%2BFOkgRmDv7FllNxUKQnPff3f8GfzLa9euyP6wo8mXxxQD8WCZaKj47F9kpLbiEkyan4MsXfiX8lqFjvB%2F7mxHjJ2FlHmGsneAC0qSlaRERIDQApDkZEU2rxlOischYdv4XPRiQiTYda9HIjnOS6s%2BsO4F4%2F2qXCPORwyhtEHpGavaqN5Am%2BtA3FULs73mkOeNbC9h5Af%2FLaZOR%2FrpanWfPFWvCHu8Icp6Czw4tkPj2CWynZNcdPj4NCqOB50%2BTqeJOo9jcZ2b52uXahDjHPQLoRxU6E3VeNGLOz%2F%2FiGVPaXI6FERiWxIr2jXZjAfdCWwKCVdcc%2Bg%2FHdoRei6S5P4tkzyeFxFkdKcOIJ%2BR7G45PQ9edhXLp1o7yJZGQuxXML0UGyOBj5BU1w4dxL9LCYYzuRTRRCzgn9szgYRWBmSTecyDJgEGZeAbL2WRVXVzYRqzEwhrv7vAY6pgG9Fu9EH8AnOLgkHhC57vrUi4CsAgDMUXtgqVErjKeaMjvf%2BvAeU52wsfq7DmotYfMHsdUCeduQE%2FWTZ%2BKHZgoKUzFv0H4hJuwDEOxrOLy2w%2BRu8SaOrG1Xf8E60YoK8scDUVFX15kHfQUKMMYkhtb0PtNgbQqMxdIsRzwhSJAG18CdUfxiD%2FSQAhvLYkhQgkpuPg3uN6ioEplNJKYQ0YYobRv8XUYp&X-Amz-Signature=753844777e5e1151de766de09a6a9005682c96bcbc87e7deff4d6445c8ba2e84&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652JZEB2P%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmoW5nkyrZY495h1g2Tfa5NhJR7qkn%2Fk5DA5Skj7BjlAIhAIE99NrRAcv%2Ft%2FygQ9TqyfvCQGlh3kCehsGIgDE6QV5sKogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw1nchYsGX6xlsY%2FHYq3APe%2FeG%2FR44v3TnMTENRA21trOtvFV5mXw6eQTwhsyQtU82eE8uplwq1aCE9unNV%2FrrpX6xt%2F2uHcDqBpCtHZdvBdeZAQGJ4mBoV79RnlMeL6sKwEoF6ChBKUS80R8WHnYndiwetdYBTUkPuihmGvLF6eXRVxFlp6Pun9Nfelc4Kl8ThNxRXTrHvGA%2F7pufdmLbIe3nC2d24S9CigOuAxNrSvaSk%2FgHvX3cplnSBTLVoMDqMxHtJxPfnW5NsE36aWetDBEsmzJFcgMOxmMUfr6sqjOEiA%2FHuH9wkXMx7txFcEBYfVYA%2F9fgMSakIg1l2RssOBuuY%2BeA%2FqeljsPFEMFTbUsYV0eEDzIw8rKuOvfMYVEi05tfvyBagW5M7Pk7HytmBxb7%2FaDr5MsJ16OSU0Eh36YZQFVxdfuvLZ58JBBs0Cxt2HO7Am%2BO%2F0HXyWN%2FsUSWMCC2HPcuZBD6mwnYOHvzIkWm9OwwREagGG%2B4SBdTNk%2FB4lzQF13veXqK%2F64rpwDdRAOJ6KMWIWpldOpNbab2XKV07d7BbxtqzXmktU99Zc1CJ8bCzQ3dc2JzeVkHIOy4Jd%2F%2BBdKRCzmh7V0UMgeMQhJdHAkNccNvPW4MTBpF%2Boou4J%2FqWO2%2BovfdF%2BzD%2Fuvu8BjqkAQYq8RQgmRZDoTrx%2F16QBVX8VZAPkgrLMZPjWHGvc76%2BFAfUvBJM1NB6kku%2BDVSq7fjp3eD6D%2BJNXWfI%2Bx2A3wBaYBxY6ElrYqE57FWNU00JIfqHYJKtcP8DppOQhOIL%2F8voHU8Ng8kJdH65FABW%2F6zgJdwUPmFvssBXed56WwsOInCryfOF7ycZqYkuNsXJZ9dXt7yhPZ0bY25BJkLrPdqHCf6R&X-Amz-Signature=d4723429c7f69ae16927ddc9379995ed7c3301e7abe0bf74e085a4bb5a0ff3f7&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB4R7YSR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsv8QuxPmS4XD1EUfUjHIpWQRP8pzVoqwVQdBAZ%2Fzz4AIgBJkv0sPlevljEjeOBagqSbU%2BXmp%2BUFqB6OufeyFOuL8qiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9qVOSRLryX76DAoyrcAxwm%2FC5EBqHBX%2BzUrJ3ux2WoBuB0HDOlLvjBPDhu9BxZNIlAjSKe%2Fqdiuo1d2iK%2FcyzlbYPlfWsKDGwOHsix0T3d60RZJxsJWBPknESXXdbrmBcHWqKADeCO0WDb6sD8LcUwkd0HGWMy4Ylf29uLv0lXLgg0S2HDB2TM9FgZBl4hjQmIxYzYq6FcoJMPSWBdp0v3TJHzZS3hLChkJV1HbjttPE3%2FGKD20PBEC1rvYxZSK1KsQ%2F%2FVWFBxIgk14jDdweMlNfQAKoCyM%2BWV2GM1o8ZbjIrs7N5OKd0S0g1hbim7VzDPUtRJw9ixpEPoAYI8B0CeT38Y0He3yIq0ySyIQsjzLoh6bd02F4xw2FCiXyb2UinsMKhCE4fhd0I4pZuyFZDyPviHhHN%2BLS0gWgP1C5jtD8iX8bRO08RhEv7EE45FsMTY1x6lrqKJFhocfGfPZk8E2FckHDxitjiByeYAQwZRRDfyiz5qPR3xuvPLjKtoEwGy%2FRgzfVtasdPSMoNRWstqYV%2Bgz7fJ39UXNo8J%2BvkQ9d23bwKrxyfrOjO6XdmJvYbkxH7Iw5Fn49ZmjzQrs9C2W1dqvvwY%2FWIgu1gnwCNDVoX7neaYmPpRSSbYecvbppFUiI7T1DfUH4WbMKS7%2B7wGOqUBobvnnH1%2F8atTnkRYjttXU%2FoT9XmIL4vz79DKfIe4UFGIzDjKNwiM6%2B27ETbINqRJqOMKXykoKp1T3EcHWgc1l9CE0XT5m8UYxPl6WPZLAIAZ32XSM9B%2B1yFN5Xe2IVbOGHWdhhlkZnvFcfQOxLk4t7T8NUKplyWOcFJq4n4U%2BHb%2B00NMlbz0mtN3YbqHce389DWVsTWg5A0G6GIg8JoBFtqh%2B2lG&X-Amz-Signature=e3130dee2e99b78fc6cfeec7032f948668a447b35950194abc70323aacdffa8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWDHUO6Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjcuW1QHWcNEJWmYhBHQezubN4l84Y1e5W%2FrcNPi60MAiEA5Yz71GHOquDePAoZVyuUWP5Y%2F4zqQe5NLGq9piKAm18qiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJUiqOXnHkIzN8rk2ircAzlVLb%2BsZpMs2KT2hQmIbT7BUw%2F5uX2zoQ2hTSrPSUekTMbokqOAavo3jTd%2FmPtDeHBUomlv3uOxvC7FzqV6XqjcnzXGKC8%2BBvot8CDoB1VsQIBBrRv7wdk3DFzlqHfOFFP0nErWoPx5VU4JEDozElJiG6F1mpvp7dnWs%2FyRwRzqH8E7dts5efPrl7yidqudREJMz%2BZKKXaM8gBNWVBuzYDZ7Fhfqhz64nkIonzM3F3RJli6WrJ9NYxeMKU7GhQIZSW5dI3l1yY6H67CbCOXbtAwTLGRvtxfMs81aVqXmmRSXYZNzj5%2BxKbD4mpq3Kn1lRFFT4OJX3gt1SudNkDoF69MC0UnkecgqJwDKPZanGIkajZHsittcg6W%2B6xanHdIbccHCQPx7ayARt9bTTDYDqeomz%2F%2FJVbbBjFK59XrKG6KW9EBCfKjdM4Ahu77jcelVWkriUjQhJjPc%2BE19%2BnZqfM6lBPLXFBxZPEMVTLYYWb1YZ0rnAUaNiHzW56NQaSx2EruS3JyrqL7xEQ6uY4Qdat35R78IUJxB0SNm9BZrOSKprfj9OqplIWoi2BfKv0ov2K%2BZGlVnnQ1hnkCaaK9vpKLrQGjB2sMTWMDDjDVWVhtxfJm3dIv4CoTFxTbMNy6%2B7wGOqUBrmqZni6PSEAFEZUrHsDS0dUcdqrSyDkhnrpUdus7q%2Fpu8EKUyKm5geMZZWUb5z1tZgG1KAB5GMQ0HDh1UnWfaYhXpFP9GZhu3EzV4%2BjvZC2prYu%2BBcnjaYsf20v6yBMSSwN3Ht7IXNQJOsCrY2SuPrBe3f%2FMzGdzYJ5Xgr1Z48BcJzUyvyZI6KgJfK5OT5fB%2B1bToNaA1lzfk6m3xfrEcU6%2FxNIL&X-Amz-Signature=4fdb2ca5701f7544ad495dfe3f27215567ec0770729f5d05640e75856d6b8dca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPSMIJ36%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3scF38jF3uApKEzrRsAJs2EBIopbWovSpFv2VwRMFkwIgbSZY0pM05QTnuTYO8qsQbsF%2Bl2Suehjiz78sQhc4lmsqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJJDeGLSPmcqtnITwCrcA2rxRFLcoFkWEkltLA8lqgPoXdWu1hr6rkiL7rye8qUnVgOrJYzJgHUFV%2FT23Vbrz5zZduK7nMbWbwdqeULT8DbFxVRAMYLof48JYOZxB6zYlhLjlU7NUjyvXibS2G9WRC%2FIcl6N%2FbBw8sCc8ClXhZ7WtkwzUCuin0ElQLS0wsE%2BTLPJjOXGfaggSNOBIWvx3ADIKv6rO%2FYCkKwOjBsesadyrkf%2BFZCXHupTrbwvzFh5yJAB4StdDvW8dS8ucYe8blTY2Rj1gJABvXzXUzv9gOBEDplOOeBV%2Bu%2F4Jilu1OcLfoaSjC4Sl6VWYg1RMLs07RFHDUgT2J%2FJIPebtruRlQ73QcNSw%2FkTztxfsQ6Q%2BeC1mXKqbxsG82Zh27DeoGHpkUXbg7b7ptgQzd3uYpn7sJdqYEFhDKzl4qItqMqU5gIGH3KFf298GXPy3m59NXAGow5SbWaSp2CLGLfgLe750ee1i%2BPUkFryIvNCxkaUbRcjUSSeBfxVvuL6mz2mA1G8gq49YHB9nZl8T4GbV6OlV11kRXywwlAtHlMdn0t1ne5BwobofmrzK7Kqu6ZfpMhWGbcQ4KlvdcFmES2xfE8F2sDTD1Zw1eIhhpRYtIZqVSgmo66eqI1usRup1j%2FrMIm7%2B7wGOqUB2NgS9YB7SFw0XfqfpcCnDlTO4%2BRzoFEkJCae0%2BF51%2F3N0iurhY8GRkUqJ5B%2FUN2XfAodSsGy3cG0kja5zSyiFbd4cSFdX8iiDvjPA0hiiP%2FiJQTzdcJoH1QfWypet83ZeeE4EbEZyZKA02nMQYFTKl1NFxrHkUr2zI2AZwd2Yap5DcNkF%2F6%2BWSB5NFv2Mcli9S2vA0cKrZWax4liVHHoulseAvvh&X-Amz-Signature=d0ef0936cdf0b725227a999aea63698fb4f7ec6c0dfbfd54adc2b54b3037c889&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPSMIJ36%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3scF38jF3uApKEzrRsAJs2EBIopbWovSpFv2VwRMFkwIgbSZY0pM05QTnuTYO8qsQbsF%2Bl2Suehjiz78sQhc4lmsqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJJDeGLSPmcqtnITwCrcA2rxRFLcoFkWEkltLA8lqgPoXdWu1hr6rkiL7rye8qUnVgOrJYzJgHUFV%2FT23Vbrz5zZduK7nMbWbwdqeULT8DbFxVRAMYLof48JYOZxB6zYlhLjlU7NUjyvXibS2G9WRC%2FIcl6N%2FbBw8sCc8ClXhZ7WtkwzUCuin0ElQLS0wsE%2BTLPJjOXGfaggSNOBIWvx3ADIKv6rO%2FYCkKwOjBsesadyrkf%2BFZCXHupTrbwvzFh5yJAB4StdDvW8dS8ucYe8blTY2Rj1gJABvXzXUzv9gOBEDplOOeBV%2Bu%2F4Jilu1OcLfoaSjC4Sl6VWYg1RMLs07RFHDUgT2J%2FJIPebtruRlQ73QcNSw%2FkTztxfsQ6Q%2BeC1mXKqbxsG82Zh27DeoGHpkUXbg7b7ptgQzd3uYpn7sJdqYEFhDKzl4qItqMqU5gIGH3KFf298GXPy3m59NXAGow5SbWaSp2CLGLfgLe750ee1i%2BPUkFryIvNCxkaUbRcjUSSeBfxVvuL6mz2mA1G8gq49YHB9nZl8T4GbV6OlV11kRXywwlAtHlMdn0t1ne5BwobofmrzK7Kqu6ZfpMhWGbcQ4KlvdcFmES2xfE8F2sDTD1Zw1eIhhpRYtIZqVSgmo66eqI1usRup1j%2FrMIm7%2B7wGOqUB2NgS9YB7SFw0XfqfpcCnDlTO4%2BRzoFEkJCae0%2BF51%2F3N0iurhY8GRkUqJ5B%2FUN2XfAodSsGy3cG0kja5zSyiFbd4cSFdX8iiDvjPA0hiiP%2FiJQTzdcJoH1QfWypet83ZeeE4EbEZyZKA02nMQYFTKl1NFxrHkUr2zI2AZwd2Yap5DcNkF%2F6%2BWSB5NFv2Mcli9S2vA0cKrZWax4liVHHoulseAvvh&X-Amz-Signature=067a2ca6446e8b8c5f65d703f382383f42e0b1ea3610e81f89d62ea8b537b70b&X-Amz-SignedHeaders=host&x-id=GetObject)
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