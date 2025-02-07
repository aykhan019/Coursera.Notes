

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLB7O77O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIAmizZ8FKyAlmBElmXg5w3u%2F70mNSV0kEMvYV0U%2FG90nAiB1ASTtMfAzgZFCtYEaCjiX%2BxY7J3l637hNBFOhQCfevSr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMNCf5YJ6neEzk0MnhKtwDZZ6qJcvqlpZCbH%2Bfpcr%2FNEV0Qon8LtAlzM1jnmzuHsFhpnskklrl%2B8AiVIE1k8jndRbt4vVu%2B6pi2ABeNVEDRMxxBHvo3gfehfU24iVKXud2nkGWu0ha0plyzzsWlyALU4sNUWjRayok0UP0JbQGIctUIrWDioDzaE%2FFczk1ADX1KSwWFli%2BISL7OtwDV%2BkdOwvdU9GGAGQVgzgY4nxNb2K25on2QxPq4ZYR%2FPE3Z%2B1XD6Z3cfDNUKrtrboDY6kuyNrRZ6D2q%2F1Sk6TfEPdWksXvymdfJaN716KtInSFilW801q0Nzv4xYzbp4iyAEhevTpzfcabLfGlnLkA4IvTfWV5m9Q%2BNeJ%2FoBQoTQuLYOurA2Kixx36DxcEahL3acOV2RHsULjT8LbdWUm8FviIWmC%2Bz1bR%2FQ%2BNRbhzxkyqm1qATZUWdWG6s1mhL0uq5XBZcdbW2n1LwTVhz9U4MDMPagJnLq3YaMFk298ZbKpWFXjq7IRuDegf%2F%2B2Cw3RFEWgDZMJX4UZTV5qBPmPqCNmPgt%2BqvI76xBXIT%2BUA0xjygBBjffdLI6i4Qfsd6X9XQDLd3t8m3%2Bj3GnNSKNtbS0WVMjj6dxUQ8f5lHE1W7tLNmHL7hyhXmETqowpeHdwwlf6ZvQY6pgFhvfSrcwcaP76K%2BqdPhiYOK4M8sgZRCBJOs6T4FphCN73O2UfPWqzBn5%2BaBthkh6YsfQAQLt77B5XllaAi%2FeAJZa4WdV%2B6qv9Ia5v1hqMEmveGRggp5XqkZHm0HTtA%2B%2B4cI5VJeo5oUR8H%2FkTn2vBJqeaWOyD7E0QE1%2FNQ16xDXESTWuKPP2I22OdmKC8YKBvEVdpgnCVXxxdoRQL%2B0Iufj6yDLJDU&X-Amz-Signature=3a5f27a247b7d12ee3fa8ec28bec8bc6349b4aa0bc60260f595f8b850876e972&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZBXBFVS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIClYRpChwmYHvBFgoAu8mTicrLrzX3YcJxVWGoZ36CYnAiB5S35bot3vAbMUMhZTOKeW5rkgxtYomMuvUOmA5rQb4Sr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM4ekUrXT2C53TKTuyKtwD3gwi9Tv3htOoOj1dQRVwfi4bx5sTmhnjv5kkedv648HDDM4WcLxpKlapQw5xIgUMbP3YiO9uRoCqiRDPAK4lmIKy8XVg8D7%2FpM1vOSbDp5YXjsVZIY8MWpX2fPaY8Mzkl5lUp%2FFLas6yWYtdeUDak2jSHL8AkYzlL0hX92vXkBi6ETv8R0gukVZeYsknKvC%2BbQZCuvuK9gl76I%2BZolhptCG7L7s90Q6tdtPZvDgzHhn9fF3m5zBRs9J5hB4%2F8eAN7Xw774uRSV3%2Bb%2Fvsgv7%2FAbzvAxrZ6ZGMZH9PFEehpL6mK8BUaPjAw%2BtYpgMkwJOERgetTOiBvpAacT9wjbYXzM4Y4yHcM0R93gzOg%2BlgblQ%2F8z8kqhy9hCGbNG97ORkon1%2F10CV47VV39xCCo8L2R7w%2F%2BdN4LufGiUtdXQgvuWxoM09yqQEXPeJ9nTBBUzKKptlhLP9kItPesBkmaqDegHyMleFHtH83uUHw4UmZZMFdFc%2B4ECh9YoRjnI7G%2B8pqQLhD2cz7cqD6MUCxVi%2BTZr%2BnkXn%2Fnko%2BIxSwIdMqufcvGHUaoc9fwyJXsuZsVVUP2Q3SM5bJN8UZNgUbueDIhVwaEsn5xNcez%2FF6c9tIGK24ioPpzVxuiM36eDsw7v6ZvQY6pgGRWORcE%2B59NHPGlthK4WpNn1XYcrHzqd9Ou4xWaVT8txiU%2BHWrVSK%2Fj2pXAZ7OO%2FSM3ss0yb37yBD6Z5wbYFLj5LknfbK81ePBjP18J1q%2BKkn3Q11eQ%2BUt4P543DzLOVQ%2BQ0vX44rppJeUl5NTxdweq04aamWIK%2BFNZHCf6puzDrWXLJvGWdOC8CR21aAeZQuPTWWw2hAenwIIEcjNMmwmaqVHPGzp&X-Amz-Signature=8e1d04504d9b1be792f74657be0f74bd2017dcdfd62f8c108ae999166fdb146a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGDWVFUP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCICgTJn9iNR9SEv9S5NTy7gnhwCH%2F2HqFndwGLYcsqRAzAiEAzpGeHGLDS7ZtA38J0HW7PmoJCfS4vofw1tV4Djt%2FypMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGWItYtXEALbBewv3ircAx41Ta9OnZZ4D%2BtwYhzJX55V3ypW5aLaA2cCKiCiJClmm2XmpdtzhCjvM9Iqn6SO7Q8jg42LtPeNTktJXAmzYqfOMYFUSctpeUrvaYZP%2FGdUFPYsTM%2BoDQVd0EGvi%2BPSzYBcUMTUSDXBqOhOWX8eCduaR1arJP8NmptWXwJOihUY4kg5mYP7IDCZF900MXK%2B3CJwL3uK4lY%2FwVH%2Fc65o8FRiW1%2F31g4quOo2kGfnGtQElJNQ3ISU8Wx1EfV%2F3OrsGaVpf%2Fs8PlosR0YfCWcosLRpFV3xnNhD%2F5cAyeFTk%2FZw2aurFoo4iMWDt5R4Y08QYzI%2FdH8p5H8wR2kydMgphGF3DaZjA1%2F6MolsB6mGDbwKipBCN5lSPceNzwY5Bq8SZ56tXZ%2FjcdYRgiS%2Ba3%2BedZBxUhld0azXSLk0Zmdeo0ea3cvTMp3T%2F%2F4RoI0r1JnUXOufZovis0oSfl0b4soRtM5wZiE9dxDIR%2FP4XlOrpUqR450gYotb5IUSHNlEO9g04%2Bq1LTTI9EMGzLVtthCRw2liItcqjjEB46%2BdbgsgM1Wdh1g4ZkgDesTQ4vi9vvrSuPCJY1cwtv77rUhMZ8mH5pPgwU6GRZb24gSiK29MVKA4e1N5reLwrdICt%2BSoMOb%2Bmb0GOqUBVU6UL9cMGzujLsOnOjnBvUqav05MmWqwT3MDQiXKEzat2QCFAvc0V%2B37EfNuDaYl0VYdggKNtbVgu%2FA4aPYVgS7kfpfiByDhsDLfd8TId5gIf3Ozg74qMpc3Ef8O2YpcrNT%2Fd%2BBcrDijSjjxYWq0wlZn3icXutgooPLL5GDwot4%2F8Hk0VpQQ%2B3rGRcH1WsOxPxRaEI0RX%2F7wsBV4N5T95GIYM1h6&X-Amz-Signature=cb39a4a458180091286d566ea820d0c38fc9008b25c25d901158582fab5fc165&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667A5JWOSG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCiNLdsJo5YMux4JPFw4F85xiK4ZrhxUzSv0dzYDOdI8QIgS5x5YirQLJn5HMlm68UohRqFWseB0nKghMKDFVF9K60q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDFX96NtlP%2BGAjXqtkSrcA6hMZ2r1n7nLKXldfkGjwOlBxSyBCSy3sTJKIAw29O8lycIw2fcKGjhhNMuv2Xey7zgl1aSLV%2FcWWvPX5ENzJj5EAHPUag%2FIUcH9gtWGb%2B8XrNiltAe0sbRmlf34PGfeZs%2BRo3%2BldzJgj9pxM6JsaP2eKIBai0aOI70DktROxDbt%2FkOqbb6rrBzczPn7RMD8%2F34tF5quXGYoYP2uOYnEivkjpf5LDeIbAjaYtkF2gjb85zpM%2FDILNN5bx%2Bv9Ns9LONt2tDlwFA7X5wa3BkMdhqigR5M9dFYMR6d7XHtMPPFQ%2Fffw1lpM2Tct4qT4jgG4RnjpOSWFol41OmxRUtWyOWL0OLEtCtpMXIo3L1RgwXvnUhEWmfm6P9mA%2FTZE%2B8DHml1c%2BCAkwpxluQ%2Fq93rbHTvp1W3RTj40nQKs%2BRA9a8oMEjpi2GxMNTWGj8wrBPswgt9UBS%2FXvDvg7YVeRMyRixPDgtF2ceKU4DCkikNFGXxAnmp%2BKIK1h3Xq0gsNXyop67SzSfJNeuwFV2jUGrnBcZH0CCRkzXuMZz57OtVPQkTkl%2FFpDWSYzKrj4HxDx2IVIMyuv%2FH32k5Swa0XsM2xta5qLBj6fCusGp2MYAy1a8wK%2B7IS6v0zioDN8XS1MJ7%2Bmb0GOqUBL3zwJnQ0%2F1bFmSw5gOMXWVJAQEmTxq%2FoC%2BllDQWfpNhsh%2FvLpC5oau%2FHv%2Fqk8rN3LE7fEKtckK7dsb9Tw6JWdXLyVifvFocyMQhEwAOPi%2FUv0beXsVfWMVDZUsx9jn3%2FzdfMC5f41WNQDTfIsz29cVlwlK%2FdaVJ4WN7UQ8UyeT%2FwiwoCOPeiNJWa5TZmUngj3ng%2BPfjGmfEfs4GmQvV11%2FjWukOb&X-Amz-Signature=b5362dbe6c25e06b63b79221087f9cf0cd51ffd9b12823d2bf830a06910333f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDRBEAAO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFjvakxupXQ215LsvFhW1e9biX%2FVqPSLvSGHVmsg7jqLAiEArzfDldgtkMngYES0tqrBVhABKsRVuOlIUCzTGAjreQYq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDK5LW3DfY5jVzn7smircA3Mbb8BJ5J2PHaPA7i4dVvR3Ka8qcEbEck6RxSFMm1ji%2BZCV%2BGXYNqLKhIUzuVPuyvmJCSUKcX3YOw3UHGmSiDk%2Bt1n%2BNjIbvXT%2Ftger7L6QeQzP%2Bjb%2BuWRfZ%2B%2FdY%2BVKJgLeLc7mPbLwLdlT2a12s79ivUvFY79%2FHVI5u13pfI4CF0FLQjho2CZ0ImMDykwIcVJIxVOxoqYJtjAwpT8L9z9f3Y%2BZe9QRukdS0IOUuoxYNSZquL90MSmiauJijhsSJHjLjADbKx%2F%2F8Yv6E8K2uZw6bM6uDGo2O2gyxZkyXLnFNsux6wZk6AimaculvV%2BQge4sL9EjwAMx9ElMAXjQ83GlNmFISc0xaKo0jbJjQi9i%2F4eEeAfDE2P5V4uxVwOOlm6YfiEKsWj4nK2ewvJ0hOuoORacJmfiqrDbkJj0D%2ByIiKkwzx0lXlpX4wIJLqBiQxIrkQ3Zuwms0W5DMScg39DVOAEc05W27bLAKbAuzhMoho%2FAJ6ahvynqj8F7VFIXIDvYVdpZyYFwIgUWq1vMUmkUnmRPAfWT7e05NyepKTKQGvUGxQ0eIcMG3P8gHGvFY42QcOn4ZqLp1irXvnQk1z7Ko5ZTuRrKO%2FnnLPVfFVD4c9kj4ObJznzcJHgGMLH%2Bmb0GOqUBi4qEnsvy3rvJ1a%2BRQg2xkGL4ckvszl5RhPB74QaVs5SRRVj1f45jbzdNejsgQqzc%2Fl7OtLbPd1LCMhMpheK95RayGE0%2BesGpudqW%2Brj3H5bhK5L95NvcXf46V%2FGxucUCRBrwXC5HM2zv7f0s8nZGhg3VEDm7Uqp6OcaZiImvc5%2FGsh%2BImkMJ6l%2BZoR%2FZlt0htziK%2BKH8roTVOwv6xoBc9ki4UaKU&X-Amz-Signature=2e1765de6e35d2ef9c99c219581f6ddc6a126a832cf2008b61a17924ba9d0edb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FMHVUF4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFbolh23ygwnGe27HLKDwZyDL0wRHUPz2jIspRt4%2F4pPAiEArtk%2F2unwq%2FNy0OiXPP35Zx3Sp0Wi1tLs8S9XCBPHseAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPKp4pCwCRA7ubqc8yrcA1QXdCnznk9C%2By4nAM8s1Is9ohVXkqi36mEBDdpLE%2BeVBR6mb46w%2FK0QESR6tpw8B2AmprSUEJMNfT8PJ31pVajpwU%2BoD%2BwQ1cEjNYVNTmtNWrvRFMWpS55T9fMtomJVE4nCSZD%2FyNsNqYpOcCdoYFp9kCahNNL91eqjn2HdcBxeyLcoNGqq9qNqg8fX52lB5gTYPOAme0ayBgqZN4bdYy5%2Bov1KvPZvaYDqWVDsRwODQ3WXalvUI1ANKWD31HPzznA8LQeL8eKoQWksGOp1WWgqFe8lSMbxQX8SHNQ1NLOXqN79UXq9OOsU8VVvLGxrGJHYdGMafofTJz%2BwoG%2BvoRTrT7PHwE5944sAC0PfFFiIoduJT%2BPNyQMuo0yDtHcdbk12XrYgX%2BmSwH6A2DcpZJ3SYiEwg8fjeAWptZ9ncfcrIXd16fsk%2BI4jpaChsbYuP9YAvh13bl8pNn22jzLaiHTi49Q04431NxXl5mG7VDN26H2O8D2uVb%2Bgyd6jrbUya6C7xQfSGorZ1g4ynXUdWtF9SNJxYuy5qSKyVEDMbAl2U1OYwQ4Kqk6YomqQZ06ZJ3kCCwKfJQbeCVqDfpkQEOnMRgB7tpOzzXaSyoiQIbzX3hulkbi4G%2FLu%2BOFiMJL%2Bmb0GOqUBXZ4xLmgxUwn4cLRtQgF0UOV%2BfgvCJ3JYW%2BdmEURK%2B11oLG3hv5YZ5G8ubClMDwi1tTHcD%2BLkx%2B8Tfr9zCWTWbV3YEQuSMRUsE1oEVGYNGM2HM4TaG9q5MymjviVDI82J5rUellWhaPJoNzlNeizalwtwrz7nMAFppjCB9VEXosSxE5a1CTLWMNmlFPj102s%2FfHPa26JPd1PxKYem1tpc7c%2FWt7ZJ&X-Amz-Signature=929b99af552432a9d0813b6e89f3f16c08088f382395ec7dd5abf2137f37ce00&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RU6KDKAL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIC2DjdMlv9eVOQrX6hamO80xKAgjOooo1e1zX8rMgqWMAiEAqKiB2O4pCO%2BOtBzUHAFgcLR%2F6fVmGmbbniplqlsECPEq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDAmjYAWEfR3aatDziCrcA911ijfRYFOCq4LjgO6oG3OzEHSeNHg%2FosmfijnnIcFhkjJHtouz6CeLC9GEqk5pBYGxedA7hmy9yNB6n%2FneREE%2B8t5AwS3M4uVRec7rV%2FoWTFNQ8%2FLuq%2BxFxP3IZK3LzCzStwZboymEAwqzacdVhVwhMSgTW%2FtAaG79NJ57v9l9m96zMF9WjCbY4J5KJAz0gKZN%2F9zBn0qAK1KeT5tJBO8jrN4jTQoWJnov9lcsSMQvE1lQPVZhr45NAlul6O9DnTFKB8E1rD2lliqtospBJpXqIKSbPjy1FauzicN4s49OG7Az4k3wJtoWFIuBw9GuvloRfnJPhv0h1eaVapfsh1YlrzfhiYxsr6hg5SjzpgI847CyWIaPbwSJm%2FMV%2BzlGRTkuw%2BiIf0pEVoWQOvpeKiCBcVinA6WU1jSpl0K0%2FFJlWu9Q3FtTx1HdzHoSHKxoluoD7P7uLW4cHIehAHdkLNDAetQBovZI6LGRMC5RM6xCWO4e%2FHk4CERk0tvHNxTsTmu4cmeds%2Fq%2FLAyMJnqfPi9cZk2GBMW7NcwG48qkgBNTs%2FMfpdcaYoC%2FNpphaHC%2FHSnqQ9aYrdbQ16FUSXszUlMYEXayQXCvRNKWFeHXFM7XmEm920t%2F%2FEIIrTW3MJ7%2Bmb0GOqUBn4fOW398AoIxWEwdHhwuLgi%2BqB0HxxirzK60VIFxi2m1Po37%2BWKTV7gtEG6Lv4AFklvpeZMjMKy4hb4sqRw8xlW4TZjCnU6SsiqWvdjQrtLu00rt6Lg3ZFJ5CgqSJqPG8CI9YwAO215xpLyZ9Ia4CryCoxCksw31vtbw%2FtfCY44YI3kSB1QweKG4uV21LS%2B3n6qST%2BJcVLcfaXHl0yguIz5I83IV&X-Amz-Signature=9d177a5b83069e726478d7c63617fc4be86f18b13db5c4991a56fef03074cd45&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRLXY3EZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQDpR5AFyhyxNrSX%2B9qRElM1Y8M9t13gtwpIcT9m%2FYU7UgIhAJdGHauOtYzgULoq4DzBUqnhMvVfhAf1eh9OHO54%2FMtBKv8DCH8QABoMNjM3NDIzMTgzODA1Igw1vF24qZRT8hYgdxIq3AOWqJeoptgctl4ggP1XMtMZ%2BqAU%2FFwjaJgDkPmSI83JXFUjvY0uZtGuCNk0%2BnbKHzY%2BLBt12eD2dYyaoaPpDUgioROivESQd6DwpUDeSSxIMuoloB96N3UiG88L3NSoGc%2ByB7mphuhkonSvX9vbB%2FT9PKtutCdxPTHtEm3ceSpp769gkq64j8PEtUqzXXkiimc%2BPLf6Zqujz8kOyR8Jetanw%2FtkL7wk72TmhVZFrZ01RnpH4sT0NYmiu4r6yx0bNIeeXv70Wcq%2BFdiNI%2BsxsEMPU7dHW8SRQTc%2FU%2BWzD%2B%2BSRljXaG008sAcaDlH008SzQl441MUoeFW5V%2FgCNNbuvNpVfWXlPHY9pf1jAkZa9E8lOwJNoRlidmxDHHU7vOh5i1JYYOUKPROIghbUtkqV3%2B1mgNC4w326E32PwyjvUmFYSaBUg%2FtwSR5FQN3TgT8xkmvCeNXJ2OSBwjG4xEUAG6mA4cN0miEIwCSAkExqpY603pwjd9mlZyNY2fLk0jo%2BsFLyfCMANRll09Y9rmQk2sINP3KWk5jFZfjzUQfLwMO%2FtTxXPIqCSpKzD0S1HExSC7ZtvaXvSXydYYp8DInteKI73NVYyTzmNYO41z49bKK3McJyCMuxy3YWw0EyTCc%2F5m9BjqkAY8%2BWwfNsVZnvLE80uIGiZEyWheWg8h84wccTEubrjLuppSyw%2FyZujwgZyb%2B7pPdMDKu43FCVY4gy5OuucGWJtmAcDmbe10UkqRDvLv35fXqyDa3fLVVrofH546N1HpJQomYZ9cFAanMvsWygY78vua68w%2B141pvFSpn%2Fvm98WTtJDRAUMZiQ%2BSKcry99ze7w9eoNglqvSTxv%2B8PYc8pc2wyawd%2F&X-Amz-Signature=73c3eb77ce0b0e2176896ce8018f3d645c8f759f6fb662204ea9d7b91bfb4123&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDRBEAAO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFjvakxupXQ215LsvFhW1e9biX%2FVqPSLvSGHVmsg7jqLAiEArzfDldgtkMngYES0tqrBVhABKsRVuOlIUCzTGAjreQYq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDK5LW3DfY5jVzn7smircA3Mbb8BJ5J2PHaPA7i4dVvR3Ka8qcEbEck6RxSFMm1ji%2BZCV%2BGXYNqLKhIUzuVPuyvmJCSUKcX3YOw3UHGmSiDk%2Bt1n%2BNjIbvXT%2Ftger7L6QeQzP%2Bjb%2BuWRfZ%2B%2FdY%2BVKJgLeLc7mPbLwLdlT2a12s79ivUvFY79%2FHVI5u13pfI4CF0FLQjho2CZ0ImMDykwIcVJIxVOxoqYJtjAwpT8L9z9f3Y%2BZe9QRukdS0IOUuoxYNSZquL90MSmiauJijhsSJHjLjADbKx%2F%2F8Yv6E8K2uZw6bM6uDGo2O2gyxZkyXLnFNsux6wZk6AimaculvV%2BQge4sL9EjwAMx9ElMAXjQ83GlNmFISc0xaKo0jbJjQi9i%2F4eEeAfDE2P5V4uxVwOOlm6YfiEKsWj4nK2ewvJ0hOuoORacJmfiqrDbkJj0D%2ByIiKkwzx0lXlpX4wIJLqBiQxIrkQ3Zuwms0W5DMScg39DVOAEc05W27bLAKbAuzhMoho%2FAJ6ahvynqj8F7VFIXIDvYVdpZyYFwIgUWq1vMUmkUnmRPAfWT7e05NyepKTKQGvUGxQ0eIcMG3P8gHGvFY42QcOn4ZqLp1irXvnQk1z7Ko5ZTuRrKO%2FnnLPVfFVD4c9kj4ObJznzcJHgGMLH%2Bmb0GOqUBi4qEnsvy3rvJ1a%2BRQg2xkGL4ckvszl5RhPB74QaVs5SRRVj1f45jbzdNejsgQqzc%2Fl7OtLbPd1LCMhMpheK95RayGE0%2BesGpudqW%2Brj3H5bhK5L95NvcXf46V%2FGxucUCRBrwXC5HM2zv7f0s8nZGhg3VEDm7Uqp6OcaZiImvc5%2FGsh%2BImkMJ6l%2BZoR%2FZlt0htziK%2BKH8roTVOwv6xoBc9ki4UaKU&X-Amz-Signature=978066da63b75d20df0b27135445dda89e8b7702f1a21276a7b0645de06f731b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662N3AGPE6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIAQckCsYkX5pfVyW0MnsTSxyQXYkJOqLgXgG0nGftYtCAiEAy8A%2BX%2B%2BUO35L7RZAJQPAYBsXDNHsRwn%2F1VwvvJK0Zbcq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDCE3rtrndw9slBgs1SrcAxF4%2BxTMCKb8QkyqEi74S%2BFctyGyFAlSCT1lE0DkLgwX465%2BSRbyTgPEwRwDsdifLmbNJjzVqX8WISNNRcCwsSz46jq59cmkYiLeUOb%2FoqvvSgIY4lF7EXuiXwjqI%2B%2BLBCaebN0nNCV0KMO0Hefu1gcwDORsKEE%2Be5PvHe5KqulxQzu1Xt6h9WmOoXr%2FPbUVu38VMWy3ylou%2B8zcysrI23cPikqdktRHs%2BLZqKnOM3Ofe4MWGJ%2B9lIpEQ%2B0KNpkX153QXTMIVoqYstVRFmaWI7o6e0Yfj66%2BixhN0bVMrszAlt9zK8pN2aE0b7Nva9LBsF2JkkJSs6k8UL98dPcXa1KYvNhyg%2F4qTbaGuqQqR0jj3YlntG%2BpvW1JNfKp3xUBuUtVN12rk211XUGysAgHu0iLPyW%2BN5nkZMoWBkeuDnxS6MdzSG9V6fw1Y5%2FgV74eA%2FiVonfdadjhgVLPd0zTjTldTVX25hSHf9j%2FBf%2FK%2F9ueTnm9xRrCas2maZ%2FOHg6uaPPhD4OBB2eiuKQ4hm7Utn%2FR1Xi9DVLC9Ude4GCP3nDgHHpdOrNhtixYajxyYb7dk2gEI05wO%2FX%2Ft7JjsSX2KArUafaFvZ8dOEo3jdXlnP52t6UpZ0QPt6qIT2tFMND%2Bmb0GOqUBH%2FK4JCGb6YKwTt4ER3UjmnFNq8aFrPi0HkOxMy3T0l75r8gsqLeByqRwyB%2F1k82VnCwRoE9pNxn1%2BtwiZDwhAlKZsL%2FgIo1HH0LW3aRJJu9MJf%2Bg2obObF1jKPDoZd3068%2FXpKM%2FGV%2FoM%2FmgoJ8Ul9s6kVmsVHI6PFgjV28ZiqQjTYE0M%2BYKavQJTaJYCVb2MmzfFDEcE%2Fx7fZGq8%2BBFbtGcsyHj&X-Amz-Signature=93d1c7fc78d685e67e4689c45f68f8e621199dee2fb497bb22c3754e8fd1ccdd&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662N3AGPE6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIAQckCsYkX5pfVyW0MnsTSxyQXYkJOqLgXgG0nGftYtCAiEAy8A%2BX%2B%2BUO35L7RZAJQPAYBsXDNHsRwn%2F1VwvvJK0Zbcq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDCE3rtrndw9slBgs1SrcAxF4%2BxTMCKb8QkyqEi74S%2BFctyGyFAlSCT1lE0DkLgwX465%2BSRbyTgPEwRwDsdifLmbNJjzVqX8WISNNRcCwsSz46jq59cmkYiLeUOb%2FoqvvSgIY4lF7EXuiXwjqI%2B%2BLBCaebN0nNCV0KMO0Hefu1gcwDORsKEE%2Be5PvHe5KqulxQzu1Xt6h9WmOoXr%2FPbUVu38VMWy3ylou%2B8zcysrI23cPikqdktRHs%2BLZqKnOM3Ofe4MWGJ%2B9lIpEQ%2B0KNpkX153QXTMIVoqYstVRFmaWI7o6e0Yfj66%2BixhN0bVMrszAlt9zK8pN2aE0b7Nva9LBsF2JkkJSs6k8UL98dPcXa1KYvNhyg%2F4qTbaGuqQqR0jj3YlntG%2BpvW1JNfKp3xUBuUtVN12rk211XUGysAgHu0iLPyW%2BN5nkZMoWBkeuDnxS6MdzSG9V6fw1Y5%2FgV74eA%2FiVonfdadjhgVLPd0zTjTldTVX25hSHf9j%2FBf%2FK%2F9ueTnm9xRrCas2maZ%2FOHg6uaPPhD4OBB2eiuKQ4hm7Utn%2FR1Xi9DVLC9Ude4GCP3nDgHHpdOrNhtixYajxyYb7dk2gEI05wO%2FX%2Ft7JjsSX2KArUafaFvZ8dOEo3jdXlnP52t6UpZ0QPt6qIT2tFMND%2Bmb0GOqUBH%2FK4JCGb6YKwTt4ER3UjmnFNq8aFrPi0HkOxMy3T0l75r8gsqLeByqRwyB%2F1k82VnCwRoE9pNxn1%2BtwiZDwhAlKZsL%2FgIo1HH0LW3aRJJu9MJf%2Bg2obObF1jKPDoZd3068%2FXpKM%2FGV%2FoM%2FmgoJ8Ul9s6kVmsVHI6PFgjV28ZiqQjTYE0M%2BYKavQJTaJYCVb2MmzfFDEcE%2Fx7fZGq8%2BBFbtGcsyHj&X-Amz-Signature=21595c03948af1176b58d80fe7d7ef91db03345704db3ce775839d625d4aeb85&X-Amz-SignedHeaders=host&x-id=GetObject)
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