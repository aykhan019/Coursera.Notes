

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C6R6BGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTszrjm3D%2FEpsqeN7cH%2BYUH2evKYBTnwXXGvTbnhmvNgIhAKDsg3%2Fen7SV1QPl12DpQdAaBUYOj8Z4FC5SStIA85bPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfXyNdvcFI4hHEcicq3AM%2FmUwWB2t0Pwj4ivk69J5vprjUwec4tDCyFbC98xw%2B%2FGXslwQnqANcBtJ2tEUgyWd%2FjMTZq2nFwrwhUpZDVOowmByqIBiP3RwqwabmpjCiUAFvocwpPEE0VQHQRu1hzD8qbFUO74WXafQhPjAHB8cSEsBMZVnoOQA5Sj%2F1sd0XQpztM51bi0UwahdlzmpCTSUCHThmI3syRCtxHJA6JN%2FJIkvVw1ZN61r%2BC4rtFPjDD%2Bbg%2F5N5ARfIKslj4vzDOLuBfrN%2FMXOkFTcc%2F6ON9oQ1mx5uTRegt5uazkuhe8EYE%2B46FDjhvTvXfQ03EbA7q9qPP0age7eJLn0v4%2F0t9Uqjh2YbCkHVXuhY%2Fd5pWKMl19a%2B05deNGTEWmGoIRIZiAFevjIo5IL4nSfFQrqSNMNqe9CH7%2BYZD0MF3f75mGWPPkjjwZQgoA%2BDQr54skaZ8O%2FBY7hv5LB%2BDOLgWBTG2w05LzyJUjtl2TWe%2FJhAUnOLnMvmGadbYgJ8N2gJ26xLV%2BQLbxq12jm8ucq57wMnhUfaGj5X5HnfmBIywpVk%2Bfokhjapf5JL%2BkgZiislr%2FWCjS1ipakfXle%2BPWVScFKlR8Av8BJQG15ZqSdAiG1sNH5X%2BdtGAoYO0jWc454dzzD8u%2Bm8BjqkAf7QWkBYwxS2dCMfhQQlysBoF%2FXqYIKycu61cVh%2BjKZdu5tIHvh9n58N2nFo2NHPdRYxI7U%2BmNiI6qYx2yL9SJLUDvu%2Fy7qy1xal7Fin8HIBetIMJ0kmi0Z262qc8jyRj1cPVrMhepIFbJB%2BpnIzEvTIezSUZzDDWiJu%2Fn%2B2jcNX3urFZT%2B%2BWSNUUeNhpO7ypxgV6FDyrRq6zMww6o4D%2BDzEpCEd&X-Amz-Signature=800bf95e491e0ab786aab78603a164d316408bd9f894957ceec81ab509eea1ce&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOMFFCO4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoNTJApHpRz9d2PCf2j1%2FDaNyw10g5HiQkavqdUq2aUgIhAPQjMo5S%2FHBBvA96Di0GZhF5l2i2LAJF64GHMdyRo9X7KogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1cknB9%2BtSzAXt7Swq3AMmW%2FX1je49vB7bu9%2FVRd5CC%2FmpmLZcgWuK45wG5R%2BIfvA62Xl5CYtqYRJ15ExeZmFDyS6gBvP3U6tq0MNuboJHyH2roB6EyBTZgt5uo8wp4SfzVML7FzxJxaYKue2hIp0EiRnUDJrqDgbNvztpu22tz%2FqdMq%2FdoHZDjxpa%2FCPug9GDz3TWZT%2BfA%2FEsMPyEyQwLAfxw4q%2BBsXKkzNW7mijbbZqL4DCoumkVKBDKAMVA%2B45OWhtT0ByLdIUVTzFn6wCkcO%2FlW9bYtnTWrNYbb11pm3gLUL46WnZ%2B21b7BbK0HmkBmHI73P5REa5WgpOEnILOqXj0mMDztHhtd0T7bK5zoGgZS8NQBXk1pigyOWGMZcoClLBhdh0tmpEf7oHXucDGxiugFcst9tlT2z%2FxpbfhNyHQvkBSPOVf4dSs3htNe2xq9Y1pljUvK1mtbdV2YxvLMElbmzI71dRxk2k4z4dZROspHpz%2B9ZSYFMdvu%2F4ThVmYAvu2%2B7esMau7t1nW57CWpo3LGhTfImF2OIOxRdxD%2BzVSBIXq2IlaW%2Bj%2F4fR3%2BN0OSd8ze7ol5pb9IRj3D6BAOnUKw%2Bwe0rfABiOGx%2FAYhTnHtu7Mbv5bqYseHP97RA2PakqLuemZcwubVDCnvOm8BjqkAczTdkZYJfnNk5hLboWZVGFBHdqDngTjkJvQj%2BLrmS%2F3ljc%2Ba0mZ0FHfjhYTSWedegkf3iCV%2FYQ8QmbIU7IFbQe1OBRWXnLm7JhAafNq%2BfajgfG5RoMrorfSoPqIr%2FJij%2Bug4RqMFoB%2F7%2B1RR6ZdHloXpCmdjgoOghOZL7W3Kw4w4cVrJyfqOuNZ0Sr81LBE%2B6Gn5nwd2ndHYW0jtN%2BwazKJDCy1&X-Amz-Signature=b24a76ed91a8846aa29299d1f2738f5ff1f0616779972f1d6d25fb3038e98587&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BXGHWSE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEmi7Qb1hVcq4TgHSILfr0qCWPjYRLNASEnLEVym%2Fw4xAiABMt1nOYUJOhP9U34e2YwAHDyLPcG4cfHwO%2B2LcPHE%2BSqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEiF%2BlqlGIgq5FwP1KtwDWr8pIUGn9iZh2HoCAztCtTDg4H2HnueULWJ2JAhow3oN7LIWthM4VCnRXvNQrJDEe920GjKWp9NiWDknlvJLaV0PmkZ8rO3PQGIoFwlR%2FpEPOPbaOSvhjTjBhAlxADoXGN4dNAliGjXfRCytf5fvB2fnI1bbvbvnfWdE8y0TgHAlMvhcrI%2FXv9CZOdb031V2ZBxMNbQr9wGjqPuxJwjgHuSkgI6X7e1s%2F8ilII39RJQ6bM3ScUaC5%2BVy0BJ5%2FygedPOTzV7o7pp%2BfB%2Fu73%2Fb8hJQhVRu%2BleuXYHXFjZNV7fWGuVtKVeqJ0NGwzS9h9zF8ZcRLN1ouJfSEWvl8LuZGBe5lDIWuB2N9CFBNDVoekAHDvz%2F6hztiTRaIgYruS18YF6yA6Dh8W%2BwTDrMO%2B8v7TVbaJ%2BLw3ao4cyuq655dLm%2BZVXh4zhCZ1NPlI5u7GI5ctzls8zmDaL5hC9SAg4kviLoRLT81kDjUnVB49nSQSariBE20sTtnlskoZKc1eNsqgLiVvaQS2dJ5hf%2FdVG6efeOzLXL8YMKcbyU83kgVZlF9F0bVCTO9VNjx%2FKrOFb%2FzLu4KHfpXg6DOgTXCzvA08tZOZm4wKCmXeKyPABaoW4y9uo5bnoPRIxcMWIwobzpvAY6pgFbA39si1G6FHnh8N02mRdcc3Utg5OVSqxueFEPxg3etm%2BZXXLHJpKZ4w7PeFNNwhuvcybPqJTqRvd5jEdCR%2BcWWtLu2ynQIG9fphXjCrYztR%2FxPa1OnHJNAuL%2FNFWriCpF8I1%2BMVEBvUZKgk6FGlEQ8vtNnuB0UbTMZFJOXeLmZ9PPprfHD%2B7iGEbJQoOvzqbHDGejuHH%2BgeZQgazRruuYzwPaqKpu&X-Amz-Signature=1267b04cf71bf5c3c86d460cac1bda546c04f5695809560fd785a8738b144267&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFVKRVXM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG0%2BAT4YCeiYfiB9HVR5pxKgOlOaQjtOKsBQkepWVJ%2FMAiEAr62M%2FwjD%2FvA0fDiQOlWTFFXySb0ag4KBfFtkCKs7V5kqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM78WIJDVgaZ2t%2BaOCrcAzUncJVPUCHtru8mnyE2DnDJSDaaQl0aI1frvuIIb49TzF9ayKcvNsGKMGiVfuEmPIXoVPO76nB10iKFrpvibGsRQbcCh%2Bqf1tbmh7OK%2BGVVBwv6Q%2BP7dmc%2BdWe4JLkv8bYhGF86n3wGr9D6uEELSPfvpxq4ZWVp8ESvmhNpF%2BxepJuptNpZBJ%2FHevNsuQqIsruzIwOyqm7e5OkqnxMb5VQ1IpnAC75XRTOnkkFS9dePo5uSJWHmpvyB0i%2FXAYLK1gCwCdifGbsje8CNh8WprsvXCyN7x9rfI5AEK88EUeViADmfK9jzl38VMvmD6MEGKJBDsxt%2BhSF9a8YRLREprUm5jeGC0i%2BTAT5L%2FG5dj2Pr90QK5STVjM0VjO33Ucn0tt2mfAkftxene2%2B2cSyXW3nI%2BFgR7RTBjeWco4G5WSNs4qJrVJi08A222qw3qMRV2hGaW6mRM2y5Vb5o9bIKcQBHVug8JCjSVmy3mKyHdadGReK1YIatDsZJb0QtiAOp0D8UYt0niVIlQ78LsFP8z%2BtZEkq1uMOU8qBG3SN0UXJ11K4hRyXl9%2B0awnvXTM%2BBMh5nnzURQ3EhrY7nPHms4a9WfJl25El7nc2YsoJNQUJCuNlt159xax3BnzJJMPG76bwGOqUBHNvge4cln65BMWy594UN1qsZwC2Va6ObKhwxeVUojL3R1ALjU1yxxi8SywSy%2FYeT2CeyfR46WmfKwkX%2BDy7R%2FxZCJwMIcJVKvT0au4jVoqmVsLfoCmS9KyICmjpwWETCSjnqBlf3F5LybiVmoviWHoMw88Bk%2FNQrH9OTOvqrtEquERxADxhQdbjJfEVgZ3pHAoxFl8827jBPwUvU3RlIop7nr%2FwB&X-Amz-Signature=8f5fec9fdd296c37f57b7601466f9d0bd2bf77440bac5d0e4b69f5ab47cc4101&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DPZPTO5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGmI5jCd2Syk1sTzVrwxwE4hRjwVNPn8h15an5k9%2FhJDAiEAmCadqwpSYQzuPPEIVHvvav2xTFPgXLDzrChfXrURKGUqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKMKn9hR83CrbBKc0CrcAxEjHq1SI087iv%2FBmFSmC0bzuoNYuA02z3fRQ7U7bHA16K%2B4sr2jsJCz8sQKtUzmqVFxzpEie3yDdZiOldGfbTwZLHC411E19DO2CV40Rwy%2FzTETP4%2FLzMw3RvByI3VpQAgxmisC7Phre%2FrH5%2Fmwnq8nbETbCe6SYKa1wlkRQfK1B%2FvfKuAOPvUG5S27NUPli6bsWeFF12dY0lfVSrY%2BUbRriqnMiIICKdO8uJQscJMNklQFV7Lv4xwtXaziY4TxQnzolE7R%2BT8RNqkZh%2FhRj0Kv%2FufREw8Y%2FlTIJY6adlmndC5bae71rJBqUT962Zg47VhnYE1vIBMZswI49OL%2BEIr9FREX4r5rzyH00qXmEnNo9F8k9x4ydVU0y%2B3ueGdh2tGhyAPrlMBZgekedqaOJ3VDt5OgolJBv3HSg6SIgK4jj%2FRfSikE3zqaTUk9wEpdodYveTkkDSSKFaCKA81zJjEYOaqrrXUi1VdsJB%2Bg9ntIynbOddmWOhcR%2FVHPXPJ8jXj2A1%2FojCkkuaJwAqF9nbb53YSnzC15xB8gclLPgpa0LyLFscg1KicB2tbo5reUvfshuFYH0qw%2Fs%2BFcveTER%2FwL2dUG3yj8Oz%2Bw9RehN5hhYp6hc1oXTzf0nQxFMIK86bwGOqUBIAUrXYHsTABHmwkLb%2BaVTi9l74LcU0TO1xLx2qafqgZRabIASCRUUgP37X9No8xUbaLJ0ONegWohHbCn3pC9fnXPh1dP2k6X8ZC0y2kc8Qd6r%2FbbZFvUZWyIErnZR%2FJKWeACoCHS27oKxEl9MT3Hv6q7y%2Bmm3pfKaB7AvrJkVr53p4qB4l2SnRK322myx8ojNjmHtaJMqo8VN%2B1MPs15mK8RamZM&X-Amz-Signature=fc99347831f9819b64d0c5179fbbda321c2fcd11f2e71bd807cb85da41c5b029&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQWPRGAR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6m76RaWNVkUpiBdseqJfhKPu%2BmJn0FDxc81vRZN0WlAiBjq3BpSa6RM1RTPf5zGsclnY%2BivCfJa1gxNuohPWmrWCqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMADCte0QTvQWEfc6BKtwD9eKOnrprN6oPx7utXrdDc9p94s2lfzK8wzBoOYiF4ARTY2j16rOFtwdWweSDSASD1tj2cWnrZC%2B4G1aE%2FgfB9tUfO74O6HhW48L96nD2RvPKgdlkRg99S%2BEWAq%2Fv4HCEHp6mvi0ohE8yRLmhr58F%2B3Yf30yZ5iGzTVuedaBQBOCkmqudzfItPABXscXV0Rs079rTF7XSLNrA2iq5ZYKPgUKUR6KSXGeAS8ipy%2FdudIImdZuuZ4y2JMyGb%2BKgiOUG5cUGeT43mj8UvjufGQL%2FNZoAUnFpAxV1QJyngDmmejR9fl2O1ws%2B05Ytx%2Bwc7dPj3cycrXbOyMUCUfoeQ%2FQY0sx8NBBY1dyVRA2a3BGo7YhMztZ65EUVyBWjLRPUVl52U6Xx137wIufQ5OU98MlJzZnNZHJG7DnYTNBP7Z4om1UzJERuDr37F5zhOuCjF6OlNxcQHlWSo37sQrCGQ9Gz5e3DjjbbyOy8VUBtxK766qN%2Fi%2Bt68%2F1LI18EJrMfoQ9hchAORVkEtyyLuN4hRQwKB5ximZWfJW%2B3%2FOoWpAmXNU%2BnUYMfHtvH6prstu6hGnr4iggEoAGCTRyM2j3AGM8gQclgI%2FW0mIjS3Q893a79JeiURW9qoFBqGeeAw9EwqrzpvAY6pgFDmv9hermSq6rJKyMiQRbjepgmXhb0XwMTMKJJz13jloRgB4il4I0xH%2FQonXby6dGBfxPN23YYu4puWFy5H2Tj%2FkenfwBxNPc%2BX8bgkdEkUJj2b46SuBzeWPFro%2BJ64SDrrHYeDAKcgsAWVbWhnZ2pDr08CEbiMPLAiVN7JQrv5kTCldZUV%2B3WOQrjWyWR%2BvyhpaDZ5tXDvZ%2F29EalkB7IHc2Qhuk%2F&X-Amz-Signature=ef454a43e978a8d08417bbbd3bc2b0e222d195db3a4949acee3293bcaf671d37&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AD7OPQ6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcb2TTLwuA9qTQV4AZzzu08mOe1DQjvid6xqU50k93DAIhAPax%2B78rKawP2uBcon%2BFEhkQdwLKhLm%2BF4t9vc06LoyGKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxhr%2BnMP7z7%2FvTXBbcq3ANBdhcbr7uTFtDvqYct5KT9WvfjZGlsl6UgR6TpiUtiu5FypfsXt8hV4Jg0exJYG%2Bie3Qp22CF3fjLsN92MqG0FW4YiQ2GCYUldmphGelZPiVfz8ihq0xG%2FDc0LkwiOf0h3rKiB50no1PvF6YA6QCjTn31bhkD65sL73DxQhtmucwY%2BBFWAJAQh2NtWJALWSoRbFsYv%2FZ38bzdCCd2d6X%2BOyKlXa0ANor2SItpTVmSIpKzpBvRiGfuN6R5qUxq0p1kOUYQOB5vqcYJheFvaYc1lnpqg%2B6SqydwZIcJiH%2FB%2BeQZyx73CSvkc2MYI5h5qxVbtbzSrIDPdBjlFkOnkyZ8XnQ1t%2BfgE2%2Behp%2FOTQ%2BetdqHK5LYXbCXRe1zuf31Fx4v3XR6N1HbR5I4VmPUya3i8cvxWez4xxypWNnsaEG0KaDFBDch%2BPMHUVQU5cu4tERxvpl1Gk6XNQWc30DrDR1AY7TggSE%2Fna3P%2F1BZ99s3ij5%2FKy8upc18aeFosN8PmmD9Yweku683c7TOf8aGE9RHUt6HsFOv53hYqJ3f%2BKajMG5DhUK8SvGrK7py%2FOApJwKzjGJLuyZ09Z3h6cHz1iTbzmOW1JgTQQAij9LnHgrF4QBzMNE%2B3sQ3T6SeBuDCxvOm8BjqkARRPTd2DEtBD%2Bl0LgjkUAATh%2BBRoRu5EhKKc0QFYfS%2Bahc1mPhqwEN7cBkhRHyk7TF6FnGhuFsu65kDSztNTxhzoO0S9Dh71aMS%2Bp9z7Pa2VdXaz1ZDdCqAeJwPFUicryj9yoc9T3Hx%2FTrho%2B6U1LAYFir0MdzscLaWa7BCxDFDtq1DQjW3G2Rx1nQgdvs%2Bm7LpvU8PxO2fjQROxx%2B%2F9DFN02a38&X-Amz-Signature=3267d2f35b94f1aaacd4162222ee543bed97034788c7fd34780f53d57217fefe&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGA4DSTU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4J%2BWDLR8JZGvIta7uGhz%2FT%2Fcfrj2QNcmZIqSOaNuhQQIgRLI2skQrESxXCxunES0N5dghHOOLdN2SwEm1MI8rv98qiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPYxLjNAEY60mpvSySrcA7fW5nTpl2uXVY09NogW8wHoHcNrZLwT3pfYqeATDDEUTFcBVY0jm%2FeG7QnciO%2FtjjAHuu2wR95HUeo0hpboArj7ZKP6ZXcIRdLb%2BZxUn%2Fd9GViCs5mYpR5gVOWQuKn%2FwZHha5B2RXU5msW3I6xdFvGXuoBeLwWLleffKCQlEOqTJrjvKMApSP%2BuUiCLrwTeZJ7WgwpM0JYDm0ql%2BvYJDr2iY8lq9CCo%2BGe87MAXqKQEhIxXA0Vywe7dNo3vBQV3nkkguc6EPXSZBSV%2BjKSGYc2DMo%2F7gO7ijsHU3eAlDZvEu8pFzj9skHxxrBKgPR8lABgBpcxXGiQfeGKuxNP3F7t86nUwTbbds9ZdECHqLB%2FVXWp4Unahim%2FO2JW1YLQ2WeYr18DacwM%2BoBprhntnOb9y1jIZtpndr%2FyxrlWdYL6IdQRjEz7%2FAoR8cxR4SLJNo6h%2B3QpebVOyOY9gB8Ec%2B8AQ%2FkaYXdBSrJUw4tWGL6FhMVHgH4dTH9ahToF5CwjKDqFGtCEdDs8Bv6Mv86zmFpNNLFdOUCpfmyBck70zRlVWo7EKWG%2BuBYpWSLwrfFH99k%2FLnDmBA2IE58RBJkSJMBbtuLBOmwlbyQYagrVHjCciUCkyq84ZAiD1h%2BxSMNi76bwGOqUB16CDXvX2YfHGkqZ1MFQRU7fkMV8WaySDMwkWGXY7l3L4YmCvVzU3IMDieh%2F3Dtg0Lcgb29E%2BxXYxVxE5D6DuItVwzX6%2Fjhva82WGVRoluqPpRG4MpOB6N%2BQRZdZ6jiFOrZvCyTHRN%2BDGNsMzh4LWcy405DUHN%2BoI72H18wHbgGFb2x4W8Bzy%2FyVGQX47VV6ypcoHOvSjcDhDMwQQ9eWw%2FqOKfnoL&X-Amz-Signature=a4ca7d4a90880ff04ee809fdf50de27e15bd2419edc8d1f789ae5ed2c5690fd6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DPZPTO5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGmI5jCd2Syk1sTzVrwxwE4hRjwVNPn8h15an5k9%2FhJDAiEAmCadqwpSYQzuPPEIVHvvav2xTFPgXLDzrChfXrURKGUqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKMKn9hR83CrbBKc0CrcAxEjHq1SI087iv%2FBmFSmC0bzuoNYuA02z3fRQ7U7bHA16K%2B4sr2jsJCz8sQKtUzmqVFxzpEie3yDdZiOldGfbTwZLHC411E19DO2CV40Rwy%2FzTETP4%2FLzMw3RvByI3VpQAgxmisC7Phre%2FrH5%2Fmwnq8nbETbCe6SYKa1wlkRQfK1B%2FvfKuAOPvUG5S27NUPli6bsWeFF12dY0lfVSrY%2BUbRriqnMiIICKdO8uJQscJMNklQFV7Lv4xwtXaziY4TxQnzolE7R%2BT8RNqkZh%2FhRj0Kv%2FufREw8Y%2FlTIJY6adlmndC5bae71rJBqUT962Zg47VhnYE1vIBMZswI49OL%2BEIr9FREX4r5rzyH00qXmEnNo9F8k9x4ydVU0y%2B3ueGdh2tGhyAPrlMBZgekedqaOJ3VDt5OgolJBv3HSg6SIgK4jj%2FRfSikE3zqaTUk9wEpdodYveTkkDSSKFaCKA81zJjEYOaqrrXUi1VdsJB%2Bg9ntIynbOddmWOhcR%2FVHPXPJ8jXj2A1%2FojCkkuaJwAqF9nbb53YSnzC15xB8gclLPgpa0LyLFscg1KicB2tbo5reUvfshuFYH0qw%2Fs%2BFcveTER%2FwL2dUG3yj8Oz%2Bw9RehN5hhYp6hc1oXTzf0nQxFMIK86bwGOqUBIAUrXYHsTABHmwkLb%2BaVTi9l74LcU0TO1xLx2qafqgZRabIASCRUUgP37X9No8xUbaLJ0ONegWohHbCn3pC9fnXPh1dP2k6X8ZC0y2kc8Qd6r%2FbbZFvUZWyIErnZR%2FJKWeACoCHS27oKxEl9MT3Hv6q7y%2Bmm3pfKaB7AvrJkVr53p4qB4l2SnRK322myx8ojNjmHtaJMqo8VN%2B1MPs15mK8RamZM&X-Amz-Signature=e08824b4e1f9e16b6198060cbb61dfdfb21e89dc70f67633f1e0e74fb6db52cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBQOCDN4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOQn1CbdR9q2KJZV6BbknbzA6b1aHbml3pFivDPwmUgQIhAPsKreoIMqX3MLWAD8hmcaIoPWN7jSzSK5Dbx3kCEwr9KogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMu7OJatRl5CDlcgcq3APgrtuScBO0SzUGMRZCR%2BMN5tEPI8TqkSWEPVqoyDAECXnlFwXWQbhJ1OqQZDsOEYbbc6xyAEzmPgEFV2IY%2BfW3wXrSCIEBhiqPjmfrsOGncA7dUwDEIXf9TYeP%2F4r4g1wuaix%2FDazR%2Bm8QsoM8ilcqGvE9DmPmOJPsCYsPmNOKAlLkg49DA7kJBZoATsXld98utTQoVtDIX%2F3k0zN%2BWP%2F0A1SdPbr4jVclQYcNqfmgL9YLGzagQUHd4ZUdhP%2B1Wcu68ch8uq3djLgSc%2F%2BVS5ZS2AO7NtDDyi7rrcM5y6YbRoYDLebqdKIgjtFWAr7sgwsH2kDJax%2BbgkZ8hsej%2FUfTOTX95uqb399u2aY9Sf836Ipv8ivaG%2FI4%2FQFhXFcz1f2utet8cl%2FQPGcCdw%2BUfw8olEipAZzuq084EXn%2FUJlj6Yg%2FyvxjJeDJEnng1hGS%2FQmJwOcARfC3jJNLbhhQBmRSf2dxiQ%2BnJZLnSK1hToPCn7AYK1jqenGrESLp9Hiv62cTD461fJwFYDFw5oAFLuyX4J3t3bKVq6CT0fd9aXQlaoFM%2BLUPx9hJEOKPhCGicukHEf3hKliu3MILfmnR9DkZ%2BCJtOE9qjsNur92Vtz9CQrfm66MuaR0IyS6N5zD2u%2Bm8BjqkAY1H5qzneFLfdQbEh7oKobu76CBcARBvwTovyNX6BWmxBfbmgUnZdIQAJdrayCMTWiQbhnLFaENfQ0w4y7PJjV8eWXtbO0sy2WolofNeeW1yrAl3MjrrRvRtrkJu60v2TPwHjgsg9wpIxOARIyC0LoSBWTwg5hmkdld9mQFr%2BKK7WTGm9K36pyaJu%2F4VKnVlQp483WPiSzfxI9T5RJADpGb8izGk&X-Amz-Signature=da484e9d9d831f2fad6902bd96bf2a46728727829b63a3fc464a1136f1eb0214&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBQOCDN4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOQn1CbdR9q2KJZV6BbknbzA6b1aHbml3pFivDPwmUgQIhAPsKreoIMqX3MLWAD8hmcaIoPWN7jSzSK5Dbx3kCEwr9KogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMu7OJatRl5CDlcgcq3APgrtuScBO0SzUGMRZCR%2BMN5tEPI8TqkSWEPVqoyDAECXnlFwXWQbhJ1OqQZDsOEYbbc6xyAEzmPgEFV2IY%2BfW3wXrSCIEBhiqPjmfrsOGncA7dUwDEIXf9TYeP%2F4r4g1wuaix%2FDazR%2Bm8QsoM8ilcqGvE9DmPmOJPsCYsPmNOKAlLkg49DA7kJBZoATsXld98utTQoVtDIX%2F3k0zN%2BWP%2F0A1SdPbr4jVclQYcNqfmgL9YLGzagQUHd4ZUdhP%2B1Wcu68ch8uq3djLgSc%2F%2BVS5ZS2AO7NtDDyi7rrcM5y6YbRoYDLebqdKIgjtFWAr7sgwsH2kDJax%2BbgkZ8hsej%2FUfTOTX95uqb399u2aY9Sf836Ipv8ivaG%2FI4%2FQFhXFcz1f2utet8cl%2FQPGcCdw%2BUfw8olEipAZzuq084EXn%2FUJlj6Yg%2FyvxjJeDJEnng1hGS%2FQmJwOcARfC3jJNLbhhQBmRSf2dxiQ%2BnJZLnSK1hToPCn7AYK1jqenGrESLp9Hiv62cTD461fJwFYDFw5oAFLuyX4J3t3bKVq6CT0fd9aXQlaoFM%2BLUPx9hJEOKPhCGicukHEf3hKliu3MILfmnR9DkZ%2BCJtOE9qjsNur92Vtz9CQrfm66MuaR0IyS6N5zD2u%2Bm8BjqkAY1H5qzneFLfdQbEh7oKobu76CBcARBvwTovyNX6BWmxBfbmgUnZdIQAJdrayCMTWiQbhnLFaENfQ0w4y7PJjV8eWXtbO0sy2WolofNeeW1yrAl3MjrrRvRtrkJu60v2TPwHjgsg9wpIxOARIyC0LoSBWTwg5hmkdld9mQFr%2BKK7WTGm9K36pyaJu%2F4VKnVlQp483WPiSzfxI9T5RJADpGb8izGk&X-Amz-Signature=e7a9da9679324b23498049178054b0c5f48d79cc3b2fab6708b4efb23941a598&X-Amz-SignedHeaders=host&x-id=GetObject)
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