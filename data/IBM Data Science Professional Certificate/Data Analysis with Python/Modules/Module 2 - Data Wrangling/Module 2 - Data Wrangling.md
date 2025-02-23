

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIBHRGDD%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6GxnGqDrhbtJNWfVcRl3JDEq2tj%2BjGTTk6NJ3qmhUQgIhAONLZy1LT5YP73JakD%2FljasATNM5YHF7y8zawTrG18NpKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy0ogddtum6dvjBbBcq3AP%2BouW6Xd3cz4GDXUB7Q9vL75GDrycLM7h3qJ%2BlrMWOETfSgofbTJTvdDEamUbDEHkMZjYmhsl5P5KgEtklqxY6fpP1tgt1i53f04%2BmIIUrl1gngkFIbop%2F5xJbyhSgD9fUE8CCwulLKv9BtDjL7VxuUeajFCPjq8bTzQ72pnylG9ZJsYX%2B3mT7eYqUS1J1QagSBj2An7Df%2FXcCuojBPuL1c2DxmBmO0sjbtAv09te%2FwNPx9UBVbfIylVDHXfN49Wq1uJaYEiT7k0Bssdcdi2laoFJZfrXpvJUckylSc8nxKqvUp53TVP7hnrwHkTvK7bz4ZqqLyhXHQqGTFCmu53pJN%2FjYijybp2PRN2%2FWyJp44oyjCgN8QxXW5ULfg3FPh%2FYel6gUxHkb2ccM6Pu5Rtk1ZurbE4OmniXkAD0rbma74vYgUu%2BxPZEntZcnq%2BSDku%2BLI%2Fx5CiLXDbLJ6g56MHh2%2FLPtRoZTpTfgW35KE0RY4aWdz6vXopBecNDyafWLIrZ9UIQB9UYjag1unmIxu%2BfBle5y%2B1Qk9EX02QdGKblEMcHkqsENZ8mJsMylkoTqwt6nUZboKFc3eArKaE%2BFcg4FkMECCygG4d49vgESGzvq2YpoCwO1XbkxvqNL1zCpq%2Bm9BjqkAdm8sJUJsaTnX2c%2BW6T%2FruthXhWvOQ77Wr73ztNAtwNTwaIAd9rEaaF2EW7aXys%2FkqCsE89R2gUVXa81bamARnrJJCsTGvdszGCCFVh7OD6z2J3gRN5ONCZD%2BG8ugQ9tX5Dfw2sRdafbamBzAlecY63i9%2BuKLso3GJs%2F0xFJ0pJS83l7lsaUriL73BGM5zxxcMf7hHWthikAwFSv%2FptduJg52ock&X-Amz-Signature=efae75c3c2eabb778638e3d0fb56bca20a9c0c27d1d345f724e6d6d077d2053c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S26ZMA2R%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGDa5NfyX%2F4AdywW%2BvH2qvZgvv02Tku69ScajGlSZSAaAiEAnG1KeGG9e05YkyuUYpCN94SS%2F3BVStf1qmzEm70fXG0qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPvlRkhTz0h7E343ICrcA9noh9nE1FX7W5cRbuXP5QsdWkkElTmA4%2BsaaD39p9AYjy%2BuKpGED%2FbzwwVR1IQtrEZ8o%2BYqzn3FwlkbdJk2%2FdGXO4nOx0zwNExb%2FfDByEOnPpuFLYwPEoWXh%2BCcTePY0wHgD28CAHv4ttwUiy3C37fbcByfw9gP9Wcdnwut6dPlZc11ZXCRPUdwVhsbYIIJoxH7X9U2DJ1mLNE7wamoibiAlSw651Q9CrRUT51H5Y6xjkjFyGune3yEERBdPSZfxuVbDS%2FpCagR99Q4quHRebY2dM3bZCydubQGWaiw8mDOvz%2FGukVBLFQ%2F2B6vvn6YtZDy1wue4LuLQNp%2BHlvhX8PW1U3NaAsvA4ff9u1mkIhNZNz7mDM9JkDEb8XHW%2FyqXi1b6LdOVjD6VmGBiTpVJntgQEp2d%2Fu7qSvjGowljqFkV8fubzz3R6vIO75TDn1ou6OnHIJtYYQQEMWG%2FaJgzVEc7okGuMiVuqbTWyhq3CVbRtJMQQHKvr981cwuOD%2BrUKuMv6gHxB9pq9ran3W%2F15NEkIRrJz0mI%2FqKvUBqdTRdZ9fCKt8F5Wyfx2JxYpoJAAua%2BF4ZP1ccbqLGVGqXY0xyRKApuSakaHWH8%2F27470e30ftvMn9ptUcsWBBMMer6b0GOqUBhMlove223%2FCg1%2FWi7JiDhfsZTqdZyVDIorFv1aImsMipGkt52F%2B3k75FAZnuMg7XQbAo5pNinr5aYQxVwz%2B5Nq99tHpSyZ3C2qJ%2FuAKiOPkdK5WuoLxXEY2v0IWQ4gZx4W6%2BU333Ktc8frsKwDCPmszoJSElV09AQTmg%2F0kNYh083P6f9mGybEyv%2BNHA898vsu1zLlwveopuNgN1BS7mFCzUBbUd&X-Amz-Signature=f3797665e9ab617bdd3049c215c5a877878eb9c158902e27cbb3d016488c11b7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWP2N6LW%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4Kr0B9Bb3hwZJuH%2Bb8bGKm9btYc4SHZfgC5FBJXApmAiBg4BDytc3eY6sLWpJEBCsw3EsnYjaIIqwtSJNMqPKMjSqIBAj2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl6RTCIwwwb2pp9mTKtwDLDdn%2BsUIL09LfFZynJKVudnLo%2F%2BgXK2dZ%2F%2B3zWO%2BTFV2RyNfyi%2FE52bqoqOy3loSPxWrBzmeqbNCcxTxVedHf5bzIX%2BWR0HOBxKueicQRQiRzbR6WMWvKW4%2F4Kp2vOAxdyeEgFfjJtnDhtgtna%2BCwNzu7KCPoANw56ZbdVsa81MgaoCzCUD7pDHe0WHplHKbepZL56gj%2BxCSJiHSDcUzj3o6gb67w2%2FeuMOp%2BYzGSWbDQKrQY4NkZLwDRtsXHR82IdKz2O%2FFFEuCIuBz50ENs4XstbQjQpv6gTzkZQB9t18rETmYjDlFCL1n6G4ebkNrJrdX43DtgHdoVoVEOKXt9JYYVfyRq4LeuIH9dy4G8PT0mIQxewyLo6zUkRaslVtY7q9l2AUpkdIa7GXVlJjuvpVy5jE3pZr%2BcZ2LAqN3CYt%2BItyrVD01AxVe5JDmLgP%2FE0O2LxP7T%2FXKAqTh3aqhLsTL%2FLq91Q1mICENev5dKCYil2Vw%2FIB1mGnnZXlMnRDNJ1AnTbzF3ERcUbwzlVmhhUd3F%2Fb96lh0WNnaEz%2B7f4xjcYW%2BGBA%2F0QySbXRzFBMWuTa8TV8QsQ6Np07fxgJpleF5n7cdkOnrvG2ilLTatnDP75rTvWysr%2B%2B9VsYwh%2F7ovQY6pgF3LLvijNSkoe9RgyErdRJ6Yg6Hkx56OBehfJHy6P8PMsBw8hd2JS6mzB%2FuChHtcg2X6lxl5ourKLeP4wfTscT4SiZWm1vwT1DKYrxdJakjruab%2BCswgVOorelfq8bW2ecitM6WwQyMbRZZid26vGT0Y%2FkV1DnFenhtm6yJPiMcvMcp0WzJOJ6OD%2BjhRP5p5LHv8jJNMSuzXMyWUcY7cpZBBLNK6vOQ&X-Amz-Signature=6049f2e6320cdba7f753872569cdc321e65f290e00729e781eba011758c16807&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XO5QJHU4%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAO7oojzZ8TZdL1%2BlxjGz3sMhZr9f3jivksBSg1ky95iAiEA5Dealh9YOPW9wutaEfZrMXPLNGg14MAvmBBP99H7laUqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0PPszfWhth0GKGiyrcA6dxLvNPdAVuz%2FX%2Buv7SmvvTPOLuZF9M76mJuR9hC3ILLxQmyy3cM%2FMi7xnYr5Rrz7C%2FPXXmEWP7tLvUz%2Fmz13DGLIQvsaMiXHjbQjr71mEkQ11bV2F7WFp%2BBcStROHyfkmJZnQ22jNLJarEQSgqjuAjPOwrmH1TbdU9xYtFP6bkd%2FvnTRUb4wG%2F4BjIwHloxLbVaH1l%2FOXhSyacnwltWXRK4CVM7fWWr2%2FBJQasGftrHB78U0ElOm2Oxr6wNDZQ3l9O0wCaizOeTrXcNRmlqEMBY1oGv6ZZpbX5EdMw3Ex%2B35njXXx4GhFr5Me345ZNgmNGgmCGdqTXRUdNRPPrRrecOyEHFFaf0fQsgl0wVAMmy%2B0wuR2EHiGtaWYlUHluRNA0p0jyq0aTRhaGRX4ZG%2BO2XY%2FGTd6HjVSBwMrQSDyZPOTuPr3xux1i6BqwoJnA1BF1Q8TZMgEo8U%2FPsZUcakfqvsLG%2FfzGD1nchRIU1w3csSdXQ4fCsja%2FvD3NzvmOd1j0QU5zHpeQqu1uOVA2w%2Bf9W6wWjYqEer3qBzAamMXdfc38rpnaIMgHUO%2FTTUQntNZmkJs0hePDumefe6SOrEEM1XjmO82QLyr5dpp3hZAdzVdREQFJFZH33K2zMOSt6b0GOqUBychOMorx8AjPxMS%2F6H1fMH0tU5j5OWvS8IOd4nu76yuyqZtkVTN57YQ4WsmBqG4Fk5cUvXhSXLlgPmiSUKa493zRbVGwby%2BCUbSYNOkT0rpVx3HuGO2sf3JzwnrsfG4U%2FyzMoPB16afrjfEUDImieh6ypldGQkgYO0dB9PnC%2BC1JQC6lrt9pglguRjw36EveS%2FVljQs5iwS%2B1Lb8zmf5m%2BvTqTxT&X-Amz-Signature=0eb3c747956a22cf2d790c325d1e007a04d785e1ab42bbb78850b95c6902f889&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZXXT23A%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNxs1jx%2BJY5i6wH4YrIerfeaVXnNe2rdlnMiXYvPze9QIhAPpFCdDjCy2QY5QjM1rYTJl4vfuPwEg%2BlPom4er0IxDlKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPPPQUtiH2OtuqZZMq3AOdCn%2Fdk6jdY%2FcT42XwK22EPzgUBJp%2BHRqd%2FWU5YfxEVwqRr3IetEwhifYCBAM9n0%2Bdxu3pMsNDnmJXT0DvP%2F0lQL8Of6aqghV2cs4eaLE9vO8PCnZyCgZCFJb29uYxmte03wCm%2BlrsKya2O9VcQmFy4BwJ3AyAQfoHsYDcAw0AGMP3WlCj9%2BljxtJO5GjRHvSADTkOJCuRM%2Fk3FCCPuYmHM8EJUa8b9zObtPRbC3hmlxFVhnr%2F7d966mSTo%2BNPycmIEkU6OzZ%2FKbXgUGYpekOlHrwNkbtfOASaIKaMC%2B%2F47QP0peQwxk59nZ7oE4jP9w80p%2FHHBFSdUTli8QnXOriqM4xpK66AbFLiBz%2B0biHbRdFmRoqP2L2ouIS6hme80shZa8X1dso6o2AfEo%2BBvQEkyf60IkV01yNPgzlDeWO%2F%2Fc8IiUedx2W560vkqwPPU3jWJhHsPhmO6ozkE9S0PVcLMY6Rx3ih8gkTwIQ9hmcl1mGdCIYFndMIz7gBvbrh22mqB%2FOe8T%2FL6rjIuIfSAVUUBVcz%2BoZitQnhZasGohCyw7aupE3YJUprQ5Oabt%2BiNJYTYNPGbHc%2B98PM4DezlXlx%2FXcXjaRADgHLu62hrVYPen%2FXJdNMiYJfsdbGGDDOr%2Bm9BjqkAV4hdfIMMcjVXP03WBGbz0RlmevqPkBcUaWS6hnNret39RAs35n8%2BXRDU5uj25OoY6MFbmNLln7xac9VC1YDpCEivTrZ%2FsomBfzNVLG9GpRg4p3jyULiejvn5YzEKeASN4naYnVsnli%2B1%2F2gmnPerhMMvfPrsoj3wuwvhNn6JHyNi82U995SWre6hwwmdlzFzLiIhzCZXf4EATb0xJyJK%2BDNAvts&X-Amz-Signature=336b947f95ecabb406e52513bdfe66d1051d97e74c9534b3e92aa81b017e02b9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRQN2FIV%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBkr7ezehFW0lPlIxSTfWKOBov6QcUPrv%2Fnl71Z%2FjfpwIgDZuVWksN0hmw8%2BM1anKL9M6mTO7npbnIMsVfj5XZzwwqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHYT9X4%2FPX2qZDD6nyrcA1iNNoIRXE9SQvwFrrXTuKLkjjsNkoYozNJ0xHxpjBTP688i2qoln5QlCxYMiYzwPZjQOZmYfqYW9UJIoouHIXInaZ2HfUh0lq0JwAqlt8dvt2aAJVoam7EskVoTWeL1p28sQGZAfIlrAGCBNhfr9g1Wa2LHoXUSu6TN%2BQymLG%2F%2BWxN7e7AeU1D6ChEq8tCpAIV2tZgpWqxT%2FB55jqCLDIV8H29Fu9fSr8PBxFlHamfYpdqZsnaPLdfF1I%2B3yJFUZ6Sa3UCtkNPOPd1X95eZA8ZfjqCVXiIdcCuLGJWfxBZ0vUx46%2F7jj7jYyFg8Jli%2Felt%2Bs%2BcmsyQGIPa6iowd%2F%2BTCTrp%2BG08bIyECAwpu0C%2BFvMm5qylUGkFi2FpmG%2FmNr%2ByoZYzkwyPldbq%2Fqgj2pHGOWvVEGlqArM3JhqdkatWc%2FrMYFWVxvCkDVX8QsNJaX2KNIaqnclHWZbi3XoYkNz7yOuMlaxsktYbCPK61H26CugjdbKnXz2QlUGif1qI46eAos5ZCNe9QCEi2%2B18I%2BNQitq%2Bj2vcj9Pud2gTcPRmLOTSUB48ZDaRa3Qgu%2BJAb1F4TJcpgJeTuJWosN5IvNKjdcf0ckoIn9vzf1VHQNJzXxvTFi8X2ax9TIjS%2BMLyn6b0GOqUBzCUyemc1A0dHbF7tJdbfcXDdYxqLt8uvSlynuN19kV%2F8jZJaelfVQYWbSKVJ7RCVA%2Fzh2P%2FJDzxCOj%2FAM7329cuoET5sXFetnJC3Nw%2FQ11H6D7ld5N0tEW2C4mAJmlbrTw6goFkU4VAWjlRvGNAX%2BrmWVMJrY56gXYrbfedlaxcKAtOZ0nCdjKSx%2FF0rlOvQ5ba20tOHDrAp45BaKvENSLV0vKFI&X-Amz-Signature=ec918ca61d16730903727ed827bd250826b6738a216b79ab790c0489b9005796&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZXXT23A%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNxs1jx%2BJY5i6wH4YrIerfeaVXnNe2rdlnMiXYvPze9QIhAPpFCdDjCy2QY5QjM1rYTJl4vfuPwEg%2BlPom4er0IxDlKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPPPQUtiH2OtuqZZMq3AOdCn%2Fdk6jdY%2FcT42XwK22EPzgUBJp%2BHRqd%2FWU5YfxEVwqRr3IetEwhifYCBAM9n0%2Bdxu3pMsNDnmJXT0DvP%2F0lQL8Of6aqghV2cs4eaLE9vO8PCnZyCgZCFJb29uYxmte03wCm%2BlrsKya2O9VcQmFy4BwJ3AyAQfoHsYDcAw0AGMP3WlCj9%2BljxtJO5GjRHvSADTkOJCuRM%2Fk3FCCPuYmHM8EJUa8b9zObtPRbC3hmlxFVhnr%2F7d966mSTo%2BNPycmIEkU6OzZ%2FKbXgUGYpekOlHrwNkbtfOASaIKaMC%2B%2F47QP0peQwxk59nZ7oE4jP9w80p%2FHHBFSdUTli8QnXOriqM4xpK66AbFLiBz%2B0biHbRdFmRoqP2L2ouIS6hme80shZa8X1dso6o2AfEo%2BBvQEkyf60IkV01yNPgzlDeWO%2F%2Fc8IiUedx2W560vkqwPPU3jWJhHsPhmO6ozkE9S0PVcLMY6Rx3ih8gkTwIQ9hmcl1mGdCIYFndMIz7gBvbrh22mqB%2FOe8T%2FL6rjIuIfSAVUUBVcz%2BoZitQnhZasGohCyw7aupE3YJUprQ5Oabt%2BiNJYTYNPGbHc%2B98PM4DezlXlx%2FXcXjaRADgHLu62hrVYPen%2FXJdNMiYJfsdbGGDDOr%2Bm9BjqkAV4hdfIMMcjVXP03WBGbz0RlmevqPkBcUaWS6hnNret39RAs35n8%2BXRDU5uj25OoY6MFbmNLln7xac9VC1YDpCEivTrZ%2FsomBfzNVLG9GpRg4p3jyULiejvn5YzEKeASN4naYnVsnli%2B1%2F2gmnPerhMMvfPrsoj3wuwvhNn6JHyNi82U995SWre6hwwmdlzFzLiIhzCZXf4EATb0xJyJK%2BDNAvts&X-Amz-Signature=0555db5e20eaeb532edb561d95f84aa2071b1f4dad27e22121888b3c3ea920eb&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSJRPY3Y%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFtbnzfzQ%2Fg3toiNqBAbsuPlpaWxSpiyxeBnFThpkL2wAiEAtJyqCe65j9%2Fj3rr9cLCrFXVsrIWZOXiSm7EISBrua08qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDQlW9NC6xCjWTgk5ircA3SAzUHdTZSCCtIMCRE8yGRmmbj4J7tHsm4GzjK2SgQyYw2AUY%2BdBSeWg8ijWroOWX8vKZmPV06JPJUJrBuNqt%2BX%2FHjv90rfvu8l794O4P%2F3jrpUMTfwyK7Afrp82QYBGcKM5lLB89PHaYpQPfr72HDMzxO79xbkx7GrtONpJ3ZcgtyoRhV1CxNK3I0MHJWFdL1P9gl3mwN41G3sm4Pb5Q9ZzWB165PG2TOBPqeF7DWEOJrrYHhGSjMcyeFWmbU3lhO4D%2BCagjvZpJf37fM1guQheyPUvXNIs8V7x3leCAW%2BEupUDRW1EJ2iCuTtfGbZ2Mxfe3l2UpmsY6tDqgBOrxdTvGLFAlSe5V7VEJHukzDAv4g6TRXqsTgvQdu%2B8RwQaC7mtgSRGm1xDTVR4mRxK38LiyeKik9jyu8zmkWn2Dx4barLJ0DFumMJyKhlRlhrX7RC%2FvAqFhQswK3ZxoPPakQRWavgN9eTUybtvXUR%2BylTlpG7A2Hu5wRpVuwVcceAMLXmSdbcvdxyiS91yL50dYBsOiXEmCQX79MLsR9D4FWDg3wUIVBQoBFkFKDpYy0WESPvSyqLppyDK%2F9jKv9PXieyjWAoR9GJZeltULn5QSLG%2BtLfRh7%2BuFjXb6NCMNiv6b0GOqUBD%2FWz0B2Ww1Dnh0Orx1k6ZmnDz9j%2FXQ%2FYynlp0Bx01EMa7QmIj%2BUyvkIFWA21R%2BQ1%2FZiFBOWZm4bmSYhB%2B3M1X6zgt2JxsxubxuVZkPNzSFi%2FehF5QkkzOP9K22rxtTNVhMDnkNzTOcA%2FDUGPVI%2FbxX9DszVpfg2JJ2Slghy9ssiZwqV6cPSm0sL6cVeiQVagrK9czjwhykmwvRlmlF8%2FC%2Bb58gfN&X-Amz-Signature=fefd3ccc3367a7cf9ee0e0b41270d6a6e77e2d5dcc4f81601e9af97399f0c194&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZXXT23A%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNxs1jx%2BJY5i6wH4YrIerfeaVXnNe2rdlnMiXYvPze9QIhAPpFCdDjCy2QY5QjM1rYTJl4vfuPwEg%2BlPom4er0IxDlKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPPPQUtiH2OtuqZZMq3AOdCn%2Fdk6jdY%2FcT42XwK22EPzgUBJp%2BHRqd%2FWU5YfxEVwqRr3IetEwhifYCBAM9n0%2Bdxu3pMsNDnmJXT0DvP%2F0lQL8Of6aqghV2cs4eaLE9vO8PCnZyCgZCFJb29uYxmte03wCm%2BlrsKya2O9VcQmFy4BwJ3AyAQfoHsYDcAw0AGMP3WlCj9%2BljxtJO5GjRHvSADTkOJCuRM%2Fk3FCCPuYmHM8EJUa8b9zObtPRbC3hmlxFVhnr%2F7d966mSTo%2BNPycmIEkU6OzZ%2FKbXgUGYpekOlHrwNkbtfOASaIKaMC%2B%2F47QP0peQwxk59nZ7oE4jP9w80p%2FHHBFSdUTli8QnXOriqM4xpK66AbFLiBz%2B0biHbRdFmRoqP2L2ouIS6hme80shZa8X1dso6o2AfEo%2BBvQEkyf60IkV01yNPgzlDeWO%2F%2Fc8IiUedx2W560vkqwPPU3jWJhHsPhmO6ozkE9S0PVcLMY6Rx3ih8gkTwIQ9hmcl1mGdCIYFndMIz7gBvbrh22mqB%2FOe8T%2FL6rjIuIfSAVUUBVcz%2BoZitQnhZasGohCyw7aupE3YJUprQ5Oabt%2BiNJYTYNPGbHc%2B98PM4DezlXlx%2FXcXjaRADgHLu62hrVYPen%2FXJdNMiYJfsdbGGDDOr%2Bm9BjqkAV4hdfIMMcjVXP03WBGbz0RlmevqPkBcUaWS6hnNret39RAs35n8%2BXRDU5uj25OoY6MFbmNLln7xac9VC1YDpCEivTrZ%2FsomBfzNVLG9GpRg4p3jyULiejvn5YzEKeASN4naYnVsnli%2B1%2F2gmnPerhMMvfPrsoj3wuwvhNn6JHyNi82U995SWre6hwwmdlzFzLiIhzCZXf4EATb0xJyJK%2BDNAvts&X-Amz-Signature=9185cfbf10d42ec9c61c00fcfeb707ddb295d2c801ffc6ad20c4360fb58f013a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5LGZI6W%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FblTYzejZiXh5lvoBys1tUkPAqLF%2FrwZwSYmcPdwiPQIgSdrAXwXC9uLnVCklK0Iv9Y%2BzFC%2FG8fgBgJcqdhLwbUQqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI5ly2%2BXd4o%2F39FN8ircA%2FJYlAAAO8XK%2Fi8mEaAr%2BxzLpm740SOgb0zAWzvdgprnHMWQkkiuPhcZ6L7SAWcv888gZxEqjB2alsnqVX%2F6MkyV8jnQm6QXggtesuLyALlMcImVkKO4C2SodlgzPwqdRaePjjtdivACx4WOpvxVOm39Abr5021ndlXsgkW9g0gqOqEdv2033rE0NmnnnBS2LFhRSb6QbuOPMOhfFY8H%2FbqEZD9fJWy0iGzYCC2pcnYvg%2FXxICJx2mG2LSK6XbAmpulRAXCYXdxyVna%2F61UDyLmiKsM3F%2BNjv4Tl6wlMZUil2A3%2BDvkqE9pUz2vw3pW4ejIqshwOLF82diFBvsBWw09zLdwiPOya%2BDk5xauIqjeAm6OgRsYGoATcG%2B7yW5jVa2b5iAaRdJB8bpSSPjRiIFvFu15%2BsDi2Va7YWbotWgiguYM7evaMiVGkRR1Lv%2F9iCWA4MnfCrqU7iOWy2lAzbmA0mtoOKKprlhwWBfZ7sqDeNRPhHKACClK%2BKPthkHQoHLRyxhiXcSnq%2BsKkEaMJz6uU%2Bnt2PJ86UH6xbtmq47qg5iMCwcRND6EFQnE78uT%2BE6BEArUuULMw8AWIZaEY7fsmrui%2FrwATWXipBO1g0rQqJode42l%2BUkuNnMMeMOOx6b0GOqUBPXthIKxFpqirdxIQuq%2FHSnph4Q3Etm84jzi3wfA84nz4H%2F5aguXTwWLUUFvm9e%2F4QSoIHw5bWlRfiyjrzWQSGvcOXArvlKdLfvkZWiYDvpG0yLnadjmKSCcu35SWd59jZKSu7oTMlzGXcOzEZY3qex%2Fo6R0qVROcTKxFwKyKptODS6auGXCL1ntAQ%2B%2FRW6bZWiITj%2BgmN8i13m41H%2FCdtQMH%2FYm0&X-Amz-Signature=9d73db141b5d77c97c5a4847a03df29b0f3cbab7ed37ed3c30cfa57f9c261055&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5LGZI6W%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FblTYzejZiXh5lvoBys1tUkPAqLF%2FrwZwSYmcPdwiPQIgSdrAXwXC9uLnVCklK0Iv9Y%2BzFC%2FG8fgBgJcqdhLwbUQqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI5ly2%2BXd4o%2F39FN8ircA%2FJYlAAAO8XK%2Fi8mEaAr%2BxzLpm740SOgb0zAWzvdgprnHMWQkkiuPhcZ6L7SAWcv888gZxEqjB2alsnqVX%2F6MkyV8jnQm6QXggtesuLyALlMcImVkKO4C2SodlgzPwqdRaePjjtdivACx4WOpvxVOm39Abr5021ndlXsgkW9g0gqOqEdv2033rE0NmnnnBS2LFhRSb6QbuOPMOhfFY8H%2FbqEZD9fJWy0iGzYCC2pcnYvg%2FXxICJx2mG2LSK6XbAmpulRAXCYXdxyVna%2F61UDyLmiKsM3F%2BNjv4Tl6wlMZUil2A3%2BDvkqE9pUz2vw3pW4ejIqshwOLF82diFBvsBWw09zLdwiPOya%2BDk5xauIqjeAm6OgRsYGoATcG%2B7yW5jVa2b5iAaRdJB8bpSSPjRiIFvFu15%2BsDi2Va7YWbotWgiguYM7evaMiVGkRR1Lv%2F9iCWA4MnfCrqU7iOWy2lAzbmA0mtoOKKprlhwWBfZ7sqDeNRPhHKACClK%2BKPthkHQoHLRyxhiXcSnq%2BsKkEaMJz6uU%2Bnt2PJ86UH6xbtmq47qg5iMCwcRND6EFQnE78uT%2BE6BEArUuULMw8AWIZaEY7fsmrui%2FrwATWXipBO1g0rQqJode42l%2BUkuNnMMeMOOx6b0GOqUBPXthIKxFpqirdxIQuq%2FHSnph4Q3Etm84jzi3wfA84nz4H%2F5aguXTwWLUUFvm9e%2F4QSoIHw5bWlRfiyjrzWQSGvcOXArvlKdLfvkZWiYDvpG0yLnadjmKSCcu35SWd59jZKSu7oTMlzGXcOzEZY3qex%2Fo6R0qVROcTKxFwKyKptODS6auGXCL1ntAQ%2B%2FRW6bZWiITj%2BgmN8i13m41H%2FCdtQMH%2FYm0&X-Amz-Signature=f288d8cb421cb2748bbe2826dcaf21d29ae0d088ce4c3d52a3cb3a0d4d5b2766&X-Amz-SignedHeaders=host&x-id=GetObject)
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