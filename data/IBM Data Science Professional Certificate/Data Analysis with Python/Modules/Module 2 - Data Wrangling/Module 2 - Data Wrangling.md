

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGLXSLCK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCadDb39IAsa0G%2F7kz9tb5%2BOJxYeEqJlGeMKzBnaqj10QIhALX9u7xsX1XnLY1vkaJ6AzwnneA%2Bc%2BfsOvJCkIl3GupAKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FBM22oB6KM6zUOooq3AMV5VOqsb94vD1YC7ICK8ZF2mG8XZr1V0jUPlFdxsqR2NDCouMZdw8gs%2BN7gUJPmDRzIQruINI%2BcfHHDRonIEq%2BNM8VyxGyF%2BwqRzImoejALfmqvEYv%2BcLYNkcmtn5kZifHQIPCAWvxiBdW5ttsKNI3tje0bdEXLcqN35L5HBHbqEiHTY7OjfgwsWsN46Nian1R30wyaqPtXK75MbHBeTF%2BArU5yN6%2BAIsfMzugB3b1O4QzijfNBmSyn0Zu2CJ1w%2BQej77oMefVV4hafhyYYxrUp8AhUVoIyrUD54yQHkDLDGCl%2BRtMV%2FW14sTCgqGnlT0HuKky8p6XgFoS9GVEUKhFjXkeVGlOASKmwT9gSg%2B9PY9XGQm1DmqmFz0wAKr%2FeK8Nl1zunxwuTCpbiCedla5R3P8Ams7t0yDGIhm9CTIqe%2BkUQ3IA9y4OGlX%2BLWMbikRIn9d%2BNonhfJKcK9zchxZtBKsi6GSJJlVzZs92jmUAqiAoY9t9fyagxVz1cLmIG%2FDwdnwjT%2FtEKchdj0RjSmbrdrY4KpNOe9VjcLcMLhmIqFS1IOOq%2FtTaBTam1%2FJpC%2FIlYhWVL%2BStu793rRb0yjgVmEBX9kgMGLa7ASJ%2BNh0s%2B9uPGqxM5vxMBHT1xjDk6vO8BjqkAfudAiAbCbINJ3qBA0nMumswVRo2vELacUljYV2rz26M7TjqvFf90A0JRd3PyUn7NyH05CTmnrYSHOAprlp54agm8n%2FvjAbK3A9sm3%2Bv1fV8jUv%2Bj5DCmESsxJVKX6nOLRNLN38jssHMePT6Shf2diy1n3fVTVWRrjXHiBijWddMDbpc8UCaD2CMYFpWdllLVXSWw2RDuNCpomt2CJdxNVZY44s8&X-Amz-Signature=028e03524cb3e47c13fdda62b8e28c9f6ba6c2ed36aaaeb7ea0da8357c43c9d9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR6UQSJ3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFXbnTXKwpoepsU0BkMJ0AkryYLZFmkbghWfRGXV1mQ7AiEA6M%2FqS1hfMIx3Lph2UE0lxwhLlvEN2BGUIW7kZuUJuNsqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO3GtnUNpKlz%2BePHtyrcA9wWzH%2FCiPVKJEFxuXB2%2Fum7ZDXYS7zhg64FVQVSawGtB8B%2FO2uGNUhDidcF5LsWow6plvUAH7XlHaDVfWAwANKwcpFFbYoInDESG6d5Fy4hmEBJDCY7MF8y00idcZjHiOOIC5Yx4UDlSKXDo8efcIPFNf984hiXa3CZG0qluzcku8dMRrNBcfqgArPNppbSNXAOHLcVHxi2oQ%2FI1rIiwYutoiAU1URyZzcT%2BHFEFGokNYPMaXAJzVqTp4qgYgXsn3MJA66B3DfYFwokEmgLe5MrYay4xEAZ88kD%2BUlDUUo7h5U3v%2Bm9iy568YF%2FY3QYxYzOX5W693L%2FHOFR7K0vvpql26ySmwThC7qwjoSY1Yypq4lSOjdPBIDWM1r%2FYyNpawSU6R7vu2oxfLZbktEuWYVjNp36rA693haKQHHtQUylNlev1Vhvm8Fz3l5BJOSmTgT0HDkzw%2B0kFgx0mTS4WP%2F9wfAJ4FJGcg1miOqe8j6ckPUBWE1y%2BdciiODtWviswks519431uiW9CrqTFJDI8Ak8lpuOCMSdi%2F5wfTLL7%2FgEakDrXMhTwHyB%2Fe7RbllwMSFb8Cd%2B31B3ecjaeyekm5yYYmHC6P6W8FU4aj%2BThG2Yyv%2B8qnFkOjzyuq2MLTr87wGOqUBUbO6iBntVLl9EInfZ4Reg%2FvCxSgADtTiXVJChyNl2oRF3Hame5cxyIaou5ryIczx0bzYy5WBmEPGjDRmK%2F3TYg8D3cPapcv1hF12dK6b2%2BtWsvf6PtlRNZy4YA51K%2BDQ1xF3SBV8QCFGCgc0RkFxU2BDel%2FncF3saOsDScNxZN%2FjDA92YlpA3MCwY9pfO9oK9V%2BSlriAa%2BjDWKpa%2FLxppFIBJQJp&X-Amz-Signature=e6154d063fd3cdef28f11bb9f5348cd84cac2cf6f6d0407f692bde776efc6329&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF5TQZSH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGkujAUJgb%2Bq%2BV3ZatfCu30XM0KrTWiGbXj4Wt37unBSAiEA%2F9xOZREdyD0jZPIu%2B8Xi7gwSKLrMXF%2FN%2F%2B4RnLbkzg8qiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtqFxawZp5Rj2EreSrcA0w2deGxCcmrkzRVGomEU7VxpSPNZSQqun%2FSxPfXHZG0Cr5hdODeV1g8GWdb4Ql4B55HP%2ByzFsIq4BxX%2FtH745q5SVHxIigwJqQhha8raA9%2BnT2tWpxh7FtznQtYfE5PQH5NutBUiHFBHf43uGA9dl4UjNUiIi%2BogfQT5XaMa1vjQzDgPJGjsZU2Dv9fmT9hcP7QosaeQHofDLG0bHQb9NLneDcR0S8ChYBP6I17%2B%2FxXcmKJ%2B%2FwjzDZ1utCWghwGs2cvorZtL2GnAPfq372rX7ZLxv%2FWrfraDExg5xC7B0MtHUO5ecKRfQ3YJXenTg06WoucMHn%2BaJJNlkfWpPPUwzNuzdCw68IANSnETOLyJXMU2Dg%2FTwIgvi8bPh9BdIDULp%2BegOzsSUvzqqXxr%2BZZETVDLrHFZ32AcYjFpj%2BNjuBcKwFudzcpMaZ0nUpJ4b6uhKDsHqt8560CE5Yr4iSJcCxKdzBaJej6HpoZBgNWjVtepN3m%2FU6CGFzRLmptzARVfBMIv2ryLd5kL3epQeCU1dqY%2BnpURh3w5RHCH9W6ahC8sscyl3CQDM7vB7U805fZzv%2BEvd9SYHpGOD%2Bcz%2FrJ449%2BbOCguSG%2BUi804Vndon6pL3CI9bg2vFMKQSkFMPHq87wGOqUBOzYpYShXCQ42l4Q6kTWykJY6lPp88%2BAY02g%2FKy%2Fum%2BHbOJBGM0XwyYGWJ7wycJrz4Un2BEPDYmYr%2BqD%2BetvKROgyg1MeODHj%2BZ0634mDspSxS1W5wRAl0l4gGGF0GlG%2BRT2nWnnFiy8cYPJMbfgpmf3JLMyETWgi8fF0muop1knMjr8C2Wcvcxmm%2FIiK34N1gr5cqe9%2F1wl9sT8R9kM0v0dUoMUT&X-Amz-Signature=5b1142ea1cae79df5c99f3c2b5db66d954d1d6553bec5d579c133ccd68ba0e94&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGT46QFF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9q1NBH%2BgK%2FUKZv9VxuAfh8eMu7FIzBUsPB%2FrkgF9oFQIgEovXkseNQ%2BJkB4uWcEBGcsDPHsZFl92PqobuBggUI5sqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCfRw1vobT0UXbI4yCrcAy637i4B8WJjt9qSGJK9d%2F4UeLA9mwjvKGW8ObdVz8yDpXHtH7BIR8VM9COjhxbiU1KTKhEfKYB5Eyen9KyuOPgSTPPIJRAtXTE%2ByKRm4xw83QTzDLuc3L4C6gsirgTvd4lDs%2F8SmU8Lkyl20UVsDcOxL24rT%2BoaglcGENxLyOx7ZSkxFnlImbQX5E1LSiCL61yJI7MdBJard6dMrVOcRKjEgr4m1cqMgSL6XfHHkmIaca665ewxje58IUVvZTZmZ2BEymNYQ3cx7GrWJLKaJV8hepQ0iSL2pU65LKQYVP%2FkY%2B6nkhMbNhhgIp4Jp4%2FuooFemaCjBMOcor3RPZsAqM8b0s26U6ZUKRQnJeVUjXACZeshvBCCQP3zku0ho92yJxkuBj3s2KsfBprx%2B42gM6CBTxADCTUkHCcSorxnV%2BJbQhV0sTMj3spmLbDW3Rt97ub%2BnRveNu1HBl%2Bnc9LHX9V0eo0oGSY16P%2BuWkjM%2F%2FeaGrZ%2Bt%2Bax3NrgYUPfV%2F05UUDtJh2UXN9dRFGZyqLZlS4Zcq1JF1PTkEwCADjIG6mhWII91uSmVuFUnpclt24WHDQHVgVVCxdux5%2F1QyJwCxTw1DUS9OSNuXIBbXg8%2B9%2F%2B3q5yks31vLLVa%2FcbMOTq87wGOqUBuUvzBr2fGsORuGtu00O6G0xwcw0TUv2fz14ESkn0%2BXbWDFgauGynxtGngqXE5d7zCb%2FGByh8ibiUcAptbS8I0lzP6uO5Vi0EUE57w2pJWRYtTIdQ3Ga2IHRsL6n%2Blkdb64U3OoY2RyedUdkVihBIQht17ePye%2BGV1sRZ39jcf7ivaSIUWZ%2BOI3LCrFG9zfRKM63rhkixDgx4yDQpKG%2FHaaq1hOxv&X-Amz-Signature=d7a32ac5da7d122d9bdcab9070a5f35877486f680ecd55a917adaaae2a1338f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRMVOE46%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcVPyfh1cv3m3BprrBYcPrI32PYoUgHwJJBeeWffxwHwIhAK5xQMGfugZy3bdfSb1O3Hz1YShoDqhP5wzlDO6HC9MaKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPnUykD9P5ufhgwvQq3AOpKU3pqf9X46xo6Ec%2FNZNgfYBVwJBWSiTjJv8rdsCgg%2FaJ0WcfIeG%2FRHIdGISvz%2FYfM0OWXRBTo2t9SoaPZNV2mS5lg6EqGbOh02Aqg2%2Fk85cHb1CiIsXmDqRo2mFhobcjXX%2FIzKSuZUdfStnttxh0kbAsHkPihsQDEZxfIkCy5eU89FRXqqDjwWFVP6RygcGu7jSwFn1ectRrNeFrxqz21fKRnyY1lcdkrZ8%2F4spLyuFfxPtOEqNHmVpQIw7oXi1CPDq%2Bx%2FUFK2qmd3MP9gf%2F1vyj%2BD1bOmCtSAGA5l4MzOiKmsYWyHTLGAvY2WuL5gVrt9%2B%2BO9XMvYyHrIPBrnB6M9bQuaoo6tMS5cAMcxu7i5cT8e3fRDlQ3L5cPEKImX6BsfCwO%2BT4Tmt%2F3FnNWCr%2BGHub%2FH8gquWx3AGa0KYcVoPZdVSq0hU6UKm%2FD%2F%2BANYsEMeLUUG8QsXDtRmhYvNkTwgfVb6SkMZdI38ovWfhuEmjYwLt3b8DZKcfcPUJKUck9%2Fv6QDU4dS3TbOZkNbINoMcf52blPxPnGIQvCqBW%2BP8VW5OJPgGcC%2FQIURWcUkTFdf7UAwm1eVhny0cmv9fF2NRMVvJ5J8YT2GLCfBeLnF%2BxvTHjuxX5N0laJrzCG6%2FO8BjqkAZH9dahJ1IhLj5cJsq1JEC4IQzkQJkhbd4RUpo71Fy0WUjXKxlI4FLD%2B8uxM7UUrFeI49on80JwOIR%2BbnytkArpiLP1BapoPf5Q7%2FFUd6aLD7ELxUwYvzhwHWiWlasm%2FSy3ipwbEQBlEfGhV6XB%2Bck%2FYAUXgshckyH747iqic7fsQeYmm80aJf6IlsfoxGmudW7oZnbkGCY2uNLjG0sNMwnV4wsY&X-Amz-Signature=9587568c1ad49d9c0a7a13e7994c90b1df6a7af825626a5a7a93e5bd8cfac4d7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBFVNWBF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICXGPF3EC4rZgbzlZpG2r08VPCmO9I%2FMG0t5U1ON%2BreoAiEA%2BVdSveofsVoIktR5pqPTnCuOflns4rl6lyBZJqZDFPQqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFfFRB8YefuWn9EIwSrcA6fxuRbyuJweQ6GQErBckPmM0%2Bae7yM9yZA48fCJ55npYv1mjVsWcUL01auaPUh%2FEr%2BesiMUmaA7qQQoBXc4iaWkZlydTCKRY3XdSwDaVuTpDbJIdwHxHmYcKLHBOHVXK3Jup25%2B9ljj7c8Fgu6UynzJfPNSowO5hJF%2FB12%2BlY2mFCGCuQHtoMcbLy8sUk0fJEDS4y0dvqrlAA0UusmIS044S1t0ZWbDZzKRWY9dgHPiN9qXDQLFIQU2KQrxjSeVakE%2BaDHr8TXI%2BbINJwmsuzNbyi4DYR%2B%2F8DH5PmBtpVRBIRF%2FgltsoJ7pyTL%2BCikwSTfdQTqidVrYvkUTziaw8ez2bkpM2i1VRw%2BQs6VHlLKpndAeIudb05kGuymSB1gJOazssXQHWLWJ8lhDRdAFFNHui7ZGZS64lWQirSMFYh1sSd4BB%2Fx1cP9PLW6oqEGhV4RWR3nWwJIwpmTifE1XZwbVYPsK39f3PATtaMZYYVLxjqkYBBeXfN9UE5LLQt9XZgkScLJJOVWcMUl1iE7YmzkqW1Ua1dQqCahQ4DM8y9vCAvaHZYub0VBO54Y0%2B8oIBwhky%2BQDXaxSwQD5%2F4PuVanpTI0cki8pAUopEmiJmC2hqHYvRynZwEUDXmlNMPHq87wGOqUBz32Ukn3AAByzaGNdRvODiSJh6%2FPsHOgkkxJhhoaJxpgba2adv63BVzW16g5Qyi5fLpbIIqr4O5nP95RsNz1XrTjpqaSJfhmRILnp2SGaSrMEWYRK5tovtzh6v1DSQKIUO4PPnSamsx%2BoyI0BSLdzquqwzYcIPRhZhlMirsY%2BYgBwXYT7EF0b10cJ0wtoaxzTRYQAwRPP%2BdMQ7PtF2wD%2FGx31nqI8&X-Amz-Signature=89c1c62d88062ae5e0daae982b5ff29a295aea8542cbf48d1ad3dbd349d4dd5c&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XQ5ODFG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG0KqgxAaHivtFEkwNEvaM08K8Lb0CbDJbDzhj8XMs%2BgAiEArSnmZfd2bsIwbTO7Th2RuVmP0U%2FH%2FwI1MBFmAu8ej2IqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCGoT2rYVnN9oI00ZyrcAztJBBIrYNmbKZJnUpXRv9tgP9sZ0JnN22NQaTUGGrQcCtKHBNUQclt7cGIeuAubGgsHmDPo957E48PvsJYwJNXMCCmtyUjXdDJfVAsqkCvjJwImohGOIc%2FLtIGdsAyF6An4wWrJZ3SwGeuiEgYx%2BuVLM8dWuiWbDWsY4nrqNsjq%2BzNCjD%2BmekmxWWP7UTor4yjkfCcedVnKCOU8zWkQ7YVmFAPYAGUl9b3NCm5AXJTNsIAjCYgIyVp6lpY1pe6dcZ7IUOPCETI119UR3pi3bM7N7ooFp30xaHY50QO9C2PhSwPgVDONcuII7Ex6KOY6Tfb%2FgbWt%2B3rE6ZnKxZHwkKkYtdQYPiK4I2Gc7%2Bq7lkCHXctQ8wqulhMrN8yEXBxw65L%2Foq3nx39JwAzsYOBKzf1gd%2F04Dj1RQNkgx7WwpvxqP55W1T7I8mfWeFu%2B9MmrrqD6YnQOcleqE2%2BV1tvcmn3FhLvdqpA2rY1SfAfvmleiPn3SLPQSp5XWTPiNzdFmth%2Fj0jSK9q3x9CCnapREucgCUFLfsyDGio5pPsuuLSyz0o3kBiEyAuqA73TzifOK%2FOrgc8qbXSILjWZBzqOkX1UKTCu5crlJT3nZ0Jobcjla600GrAPOnBjFrOCiMOPq87wGOqUBkN0Gyi4%2BkplYvScruZrobyQPJsHyGyRRvNXEX5%2F4pfOr4uTqN3ESBfpalb%2FuygM16FpRdLKOoisrPpbbV20YG0QYt8KtT6VFlcypKo32RZXDoCy4o4PTAzRGLeJOc1n33h16%2B%2Bc1s%2BV6ijSCfwq6rN6YLcYNTBWDDpI1qm6Fnlhe1%2BmfkGh%2FSoYhiWW%2FrGS5EmSHx2675fFtO70FJn2U9M8DFcWu&X-Amz-Signature=56f38a71f154b8c7dce0b7078c4749ddc6cc74f999a3fc5daeb3cada1cdc11dd&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TLVSY4Z%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQwFbuWpBKenjcst62Te3j6L3qhoiU84kOs1RbTktTwgIgfvXcDBeOQ%2FNTh%2BOpSKxHllDMhb%2B0d28R2InuaxbvLrAqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAXAIomNGic6l2Z6XCrcA1jeO0pzEQk1YJJONcxwRTUTo8mXe7slhYYnU%2ByZ0hbVFA1l85NVbb1UPjccTzkqdzLex2OfGDbbOIeNxAO0cXZgEzWuPgqCgFf0SOlDUdxIv9MfAD2THzPZJoGKjBEVh7L0%2BR0LgU6IeW7nl545j9D6Km7ycWXDihy7oTdNKzxMTbRxJKmtAtJrrz9CFLrFakxTi16l5K1%2FXv7hbCer2Bbh6x5QAC6XMhuCzL54qBUuu%2BWscI8u5jEJ7StyldfePEKUAsBhlBRShTlQA0CA%2B0fVwa6lqClneRgIjkh2TE0put0reSnATy2dtNe7yftg4v4ZYEH2xM3G6UGPQyXhZInZOPMYoayS%2F1VrMpPhppYrw17E0WBH8XnPby5AW9sVpkJssBsyRmrf9%2F6ePsGgratZ2eqorx4qR8Y4FPA90YusJWIPuELhGLnjK4EPDHXFg1STmeXgkKSnGvrRFn19meCGkBIE%2BvhdUg0qOiG8UEoEED9DO0BFhzyDC3lBn5WcXQZf8%2FTAFFIVf5b4m%2FMpqdwjGEt%2BqSmtl2gLI0Lh3sgzy8GRAInNugWyYlARAAbdA1SHaE8YTaibJIxKB1IqIAllO1VAupJguRfBs7b3rZb8CLHaf4P%2FIcKBeIvzMPzq87wGOqUB%2Fre8o5nUwcWA5qZwl9Re2aq95khEsfLgSbBjwVyyvFf6wEZ4hOb6IYLnhHDGveBQRDDphbV9evQZzvILqqABqu2HHmHK0V3uLw3Hzrg7TJuLXl9shliL5K5oOFEsXObEM3nn9dnBUmKE011T9OqBFHDdQd0MSC3g0I%2Bl4HXF2JmOdoMEXh0XFxP%2BoGB2ci1zp%2B6%2Bv1t%2FHA41EwlbXCm%2BgigHwq29&X-Amz-Signature=bce5086521900e063bb836efbf5d1f9baf43e6b51851cc5a58c1a28df3ba8348&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRMVOE46%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcVPyfh1cv3m3BprrBYcPrI32PYoUgHwJJBeeWffxwHwIhAK5xQMGfugZy3bdfSb1O3Hz1YShoDqhP5wzlDO6HC9MaKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPnUykD9P5ufhgwvQq3AOpKU3pqf9X46xo6Ec%2FNZNgfYBVwJBWSiTjJv8rdsCgg%2FaJ0WcfIeG%2FRHIdGISvz%2FYfM0OWXRBTo2t9SoaPZNV2mS5lg6EqGbOh02Aqg2%2Fk85cHb1CiIsXmDqRo2mFhobcjXX%2FIzKSuZUdfStnttxh0kbAsHkPihsQDEZxfIkCy5eU89FRXqqDjwWFVP6RygcGu7jSwFn1ectRrNeFrxqz21fKRnyY1lcdkrZ8%2F4spLyuFfxPtOEqNHmVpQIw7oXi1CPDq%2Bx%2FUFK2qmd3MP9gf%2F1vyj%2BD1bOmCtSAGA5l4MzOiKmsYWyHTLGAvY2WuL5gVrt9%2B%2BO9XMvYyHrIPBrnB6M9bQuaoo6tMS5cAMcxu7i5cT8e3fRDlQ3L5cPEKImX6BsfCwO%2BT4Tmt%2F3FnNWCr%2BGHub%2FH8gquWx3AGa0KYcVoPZdVSq0hU6UKm%2FD%2F%2BANYsEMeLUUG8QsXDtRmhYvNkTwgfVb6SkMZdI38ovWfhuEmjYwLt3b8DZKcfcPUJKUck9%2Fv6QDU4dS3TbOZkNbINoMcf52blPxPnGIQvCqBW%2BP8VW5OJPgGcC%2FQIURWcUkTFdf7UAwm1eVhny0cmv9fF2NRMVvJ5J8YT2GLCfBeLnF%2BxvTHjuxX5N0laJrzCG6%2FO8BjqkAZH9dahJ1IhLj5cJsq1JEC4IQzkQJkhbd4RUpo71Fy0WUjXKxlI4FLD%2B8uxM7UUrFeI49on80JwOIR%2BbnytkArpiLP1BapoPf5Q7%2FFUd6aLD7ELxUwYvzhwHWiWlasm%2FSy3ipwbEQBlEfGhV6XB%2Bck%2FYAUXgshckyH747iqic7fsQeYmm80aJf6IlsfoxGmudW7oZnbkGCY2uNLjG0sNMwnV4wsY&X-Amz-Signature=0c83156834ece1068f35c0c2da8909ffb6033d0c521f159d83b293dbc9790581&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7AC2VMH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqTSWqc2%2FPa8Z3GpCeBRtqeGS%2B7GOaG9KD65F3cY6nQAiA81tOZLufkkcIiHA4KL0Q00jFC3beCGnEfKlaaw2jpDiqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMA%2F0PkH%2BNv2W7FCNTKtwD5LAnsYgQR4UqymkUJGnkXygEw2zTb%2BUUsAYyEKxCvZMvawfrspBe8wa1%2BXO5dhRfv3jfZr2ioWZn8Sl%2FoclgjV0HhNbppSvXihkm5SWVqnm9t4yyjpeVgolKqYcQ5douC9lCPSzT%2BlpcuYno5h2uYApyKr4ATvk5tApCpOGxt5AWvTCshPoyZm%2BVje78mKwd42ZH8WK%2F802FROehXx0cDRSBAUZ6Tw7iTTUNNYcs%2B3TEBeT1C4LBn2Vp%2FL4MI5S6KetMsQ8ZCkAbg4cpIi%2Bung06QCUaKPQo%2B7Y9m1rMjPf1gWL5lNVTM4QV%2BBa3dRjFqP%2F0uRly33Izikk226JTHFmBo0uH8sEDzF5sM9l74DMHo1mnqK0jvstdwlfdXeW1MjpHkQ9cEEBDONJx%2FtX9SMYNUd9bJKwQ6EEdWrFS5Hlr1nhrxp9yp%2FS90osG1XVI4RQY6NbmGQfEEYydOsgXFaAdevSwVOxFPXvyFLuohhQ%2FQWeTxdG0Py6A%2BaMzYkliJy3Wb7YUtlJgJzyFriCvoEINbGLNg%2BWnXc8pDmUPeclEINyQCBnEuA%2BrznZtF6o2r%2FKgZ7Y%2BLXmXzuXCmX1pHhE6lwb8Fl7ltGcYs2AqUbXq0BMt2Wc%2Fh4iCD5kw4OrzvAY6pgG6SEtNMvgxy3UXfjSyxQ85pPXU3e1Wv0SovADmWZQNyBB9Lm7tLLA2QMveqvFxt8m1briuRQ5PGuqx15e%2BFr0mCoeu3IINEyx0quBZ472T%2FcRDkQQMoJHuuHAiz9n91n6%2FLNDsd3E%2B7kSiq5rFmU9znhtnGnGv6B4inyXQ%2FmJ%2BYJq9j2FoAefvu1pCXc6lT%2FKkw6omdo%2BdLQD8EqgT7UiJ0tj6ELNg&X-Amz-Signature=b6fc9305c905ff21066f535aeb5e00e0a5eaae7f0e220c0003a99316b8731e1d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7AC2VMH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqTSWqc2%2FPa8Z3GpCeBRtqeGS%2B7GOaG9KD65F3cY6nQAiA81tOZLufkkcIiHA4KL0Q00jFC3beCGnEfKlaaw2jpDiqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMA%2F0PkH%2BNv2W7FCNTKtwD5LAnsYgQR4UqymkUJGnkXygEw2zTb%2BUUsAYyEKxCvZMvawfrspBe8wa1%2BXO5dhRfv3jfZr2ioWZn8Sl%2FoclgjV0HhNbppSvXihkm5SWVqnm9t4yyjpeVgolKqYcQ5douC9lCPSzT%2BlpcuYno5h2uYApyKr4ATvk5tApCpOGxt5AWvTCshPoyZm%2BVje78mKwd42ZH8WK%2F802FROehXx0cDRSBAUZ6Tw7iTTUNNYcs%2B3TEBeT1C4LBn2Vp%2FL4MI5S6KetMsQ8ZCkAbg4cpIi%2Bung06QCUaKPQo%2B7Y9m1rMjPf1gWL5lNVTM4QV%2BBa3dRjFqP%2F0uRly33Izikk226JTHFmBo0uH8sEDzF5sM9l74DMHo1mnqK0jvstdwlfdXeW1MjpHkQ9cEEBDONJx%2FtX9SMYNUd9bJKwQ6EEdWrFS5Hlr1nhrxp9yp%2FS90osG1XVI4RQY6NbmGQfEEYydOsgXFaAdevSwVOxFPXvyFLuohhQ%2FQWeTxdG0Py6A%2BaMzYkliJy3Wb7YUtlJgJzyFriCvoEINbGLNg%2BWnXc8pDmUPeclEINyQCBnEuA%2BrznZtF6o2r%2FKgZ7Y%2BLXmXzuXCmX1pHhE6lwb8Fl7ltGcYs2AqUbXq0BMt2Wc%2Fh4iCD5kw4OrzvAY6pgG6SEtNMvgxy3UXfjSyxQ85pPXU3e1Wv0SovADmWZQNyBB9Lm7tLLA2QMveqvFxt8m1briuRQ5PGuqx15e%2BFr0mCoeu3IINEyx0quBZ472T%2FcRDkQQMoJHuuHAiz9n91n6%2FLNDsd3E%2B7kSiq5rFmU9znhtnGnGv6B4inyXQ%2FmJ%2BYJq9j2FoAefvu1pCXc6lT%2FKkw6omdo%2BdLQD8EqgT7UiJ0tj6ELNg&X-Amz-Signature=a15b42cc341b35c49f7a40d15e6ac7acf87cb5c35bb830936370ae70089ba9a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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