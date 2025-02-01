

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QLXBGDA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtLldZnG9SEQEHLCbJKADXELt5V4muREhvB7c3tGRlNQIgV72u0Jv0SxTFUuWD0xsxpe%2FDT9JHfvHD13nkUTDl0%2BsqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHnrC7Ct4mMVtAzWxircAzy9qSTho119J6rGvDcIOprXYx%2FPYndoAgqFpsB5lMIOIL8sFyX4LU3LjPiqGSjfQPn0p1eNaRrugud5YNK5OhngBZwsTUL%2FcZh4rsF4nE4idm0wTmzMlA3NimSb8hEz6hBUhOpR9Gf115%2FArvyduduxOktfZovlil3jH7sHJvOjTyf7iis2%2Bij8x08F7QEK9PFMsCoed0sjhKVLFp95%2B4IHMCjYftEtxgidpwL6cL31zsotS%2B%2FbtzArw0wy99w1Aj%2BvTB%2FncmbqCa5gfNrSH0LXNHBFUUM0ose5mdHnb8fUBDRbADTQ7ZkGLSe96EKK1Lj7zWiF8PVSxlHXGhh7s5CiHS2vQTfbDGxr%2Fv4pWfIj9YkF0oQ65yL4MzvInlOvgWXJhzsF6jS8fhiWAbv%2BkFElwjTHReoTfI6jkvwkImJEvoh9LGijqtm5DCEEHjz%2FQ6AKU1iYQ%2BVzQcdVrcg7g3XXfrH5l9%2FRAj7oH08vyLuCVuUKRYh4X2GuEBidroeacwlymM7de5nshc4PGThl%2BkmTxcXXLqGUKH2TGxYFkafefECdBuIcEqd30UZK1azI%2Bd2bgPHjuLCfb6mBWOpkuffZWPizhyGiYbZmq6bMb%2BIaesWf9GQEx%2BT5dLYFMMb2%2BbwGOqUBun7aKd13iMAMhiwj7y1GBVv%2FRvy42Hlmqmc%2BUwQPkz43%2FvKE1C%2FVY0vmLOj0OTfg1RsgsFhqq5qsxR%2FTJTZ%2BKv7NdwEsuZ55R0RE3kcqZc2ZeV2qUGbpfBkoPd4klE3MDlxuOBw%2FNbB6S%2BJg7SPBc335JCetIzLlXE8yMpsbRE%2B9Bs%2Bia1TRtA7y76vGuRd5MmbeL9NEcXb%2BAUqSPvQY4qf7Zaev&X-Amz-Signature=daf4020e812e46da9c3af05a9b340f96695cac611a6508e7996cf2d740076685&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LDCQBWC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIrpOW7vAHJ7DblHzM%2Bmdyz8QL7rImIOyVxv48s8hcCQIhAJIxLIEv0d8fzFVrzgD5I1IWZgFWBU2NYxB28340bO62KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwOthj2MAKl92qpapwq3AN0qLiYMiOGsyTAUEc28CNyirvWM17ogZsUtft0VgQeswH2tl3RPK10Io3ZvYKzGD%2B%2FYFK%2FJBHMsGKAOxsJa07w1pfWBCm2khnz7Mo1G2fCl98IyD7w1SB1Wrz1EWTcVc1qYnen3SKi6LHvxULFElLVa3K6Tlz%2Fzrmz3HZIOCgIxAJ0B5wYzparzGdqLcIfHZiSfxddpWNcjCVWQm69B2tNVI0ACRqKChKRyjNwRvWryDM%2F%2FLB6a4Dw6yhwFjZBDSltpguXGel3slu7gJ56RX0xnjsweggqMTQMv2S2h0AVzQ6Xgs%2FnKbnTtwMw2fC3n0iPfHWSDmUrOU8Oy2d%2B4eOWCW5FhA0M4sqWQ13DfQ8p0nYnO3KP2xH4Kmsr1AYhbIRN5Kx1F%2FWuD0k6dBrSpQkKhqg%2FU6xqHTS2CJorr5l5ed4W7pHhxONGDMA3mr7l7TIs5Ca7PYkNttAiYPFD%2Bi5zLpUIwwbFd%2Fg0v0N%2B3KbRWsJXUQfOo3v2vtRr6NcXdk%2BTcTHo5izEZSLwCOhmXUNlBWX5i8vrZywfGg3Mbn11K6nswpUejS08xx%2F4WZR5bHuR5aYnA1pOyFxC%2FtAldjrZ4Rf9AZ%2FiSbSxG0dKuSW%2FZ5wT6f0Y%2B%2BviGL5F4DCt9vm8BjqkAQAR1e5kb6yNRBRIDbDLDtm87qCr%2FiTOsYtlEaopFF8kgNstn1bLRa9%2Fl7SlWQHpn2xwSHQpDC0%2FKte5Be%2Bni1vgDl4f1%2Fc7pahhFektwWG9ii%2FcWYapvi7TqziVARpzO37yFYP%2BErRW3nVLlKGL5yHd2uEeLLssamtUU9PVNLza27CciLcsfEolEsXM1o24SZVS55H6Py%2BtDhbQDnsuPJDmhkDa&X-Amz-Signature=86775c02f1cf8057df06b458431d756da97a0711f8f2e1184b871b96633cabdb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJO7BFKJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHWYsPNPUXgK83R0IyIMh1re9%2FnZpA1Hj8ggl9e7sOTfAiEA5u42m3IScJ%2FwWGEJml3%2BB6u96tuW1zYWz%2Bv4iA5pM6sqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDr9Sxb6oeGtXFEkcSrcA9XGGEAPZwtLFeQ2ICRKHwd1yW94xcdp5pTZ%2FL%2FseFXEKf4aVBegXxB9KqMH2dCxEqfnL7%2FQnA9VJOs5QRuBkHfm1t00Xi8j6ojQkZ0va6TFMy9und466TFOchz%2FednR9q56GRM%2FVfkOV407IaFEC%2FKoh2V1q%2FSsWSHr%2BWzoG4AFtaiFRqlFn3Fsp%2BIGa3rSiHMel%2FS92q9%2BsI94SCZ%2BCNxYbKrizwg2MbezkdWNhKofXHcwCKvDUlRP8oaS5GwU4BBXI4z0vz8nW25S%2BTFZgbcj4v1bPLUtxspbbM9i%2F7CKIkO0SoAiXnXyrOeL5WPPmTWNn1LVuiWXaTVHQmqD3gNxUPBudvDVsaidQ1w21iJDv5VuFiFTd%2BgTuAQuEmTZE8ChbvopMjNSgzMdF1mzs8tVcWhL%2F3IdqQVfdWAT2J4DkgVuQavtJn081jCQ90Utw74jrvM0kAB8YFF7yU6MOTT83gOdhp171Cn35FYjhGltO7Y86QgHwVhvk%2FFxT44Z%2BKedhYzJBhpMDJizumUk%2FG7wABLEbx%2FSLoPusIGlVchCqZGJ0Hg7odtBkJMCpQgHy7bjvuLxQC61Gxkg2JWuQtC%2Fz2HlSgBCTJeEh1ab5UHUo8e6mfSLJaTpPytmMMX2%2BbwGOqUBfPg8bmC8Z6l4gx6giEOreR8MOAcEzr92mBVI4yBxn2WEtepsQSffMNKOU5c%2FjrjMjVygIWBEOtm6r7e2W5ZEHvXAno6RnRr0RrpjlNWxuT9qW3V19rW%2F9M7kxQ5VQSkS%2BHWvb0X9g8GuyITjUYq9ebGRIa9KOF2Sm5ZKwc07TuJ%2FTP5fX300LeLw%2BoxD7xfKvNteKrTyoL7Rj%2Bc7opQtjRRviIgk&X-Amz-Signature=d056b62be4eeedfb78827f082e9b3114f57897c1e9711253cb7124b3c1b8fea2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLVQRJT4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7UL4%2FvQ20vKYR%2BKEkHVKWT2FWSKPVvg%2FA4C0BXQhZYQIgHrY3nngYLUKjXJ%2FVxDFlbtY6N2EGLzsZShaY3sl8JgwqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMH0AGP%2Fsd1l0AhaOCrcA%2BIUcncECCBUPIu%2BleZhw%2F4Os4oS4%2FsDr%2F7XfB4Zz7KTLBZ5cTBi4FS%2Bk6nVpxy%2FItX%2BvpWauveLjwjobzahUJ0Ml1%2FH%2FJqQksgupyTBLTh9Md6NqKO6jYETvYBFuuCmLEWR39E%2B1pX92Nv3Xpbf5pCVnC8%2B%2B4XrpCFVwFenxcjg7aNIR1xmd7iawf0R7cAns%2F4vmmAJ5kUVtrz9Sd4btjEhLCRdzko0gJ50hEHZ4O4yE3XTlgC1sPej3Ez0xKhunkoLmztjaRjjsmfHoX4Z8jCr%2FZDD28vG0JHCqERpxTQTbyJqXAXoKY5y8BT0JmBSF7DIhTYpQsVf2kVwQosKCNKUwsabPAucMFN0Trx73rPOKk%2FtBsAApH1CLiOFze9kPWpgRqxBXhxVBzrJYckvtAFNPNn4%2FLSdbMkMzW4LE9Qbh3nhVWW%2Bnwwe07wDvLITTapQiBmZ2AX%2FJFbyCnpk3BloDOL33ylRiw9LG%2F07FUAbaBK%2FVC9hmxrgItKPLA24rPyPqvLFYk9%2Bt4b7%2F%2BTTmjjTypf07AOu16eh7GQ1mHJD02UcybAutbPxoi6o13oeCTa%2BHZMYVMcNv%2BLq6x4mMSxMbOdNO%2Bb8p5NfwEzReMisQt6uI47Er5azY8h1MLD2%2BbwGOqUBg50qHpK1nxzCKudYr5qNTYxrc9Ate%2Fs8G54VWggyh8IaN9DK9c6s9Vfr2uMyNZotgGGEHyD5W%2FecQdfCOObsnjX53RPWFNqGk8dco5y%2F4y%2F8JwCd8U9kYobmA27RlONjhucpJafDB664xHF3vQ%2BchhbLAWc4kKW897dxm7yeQzzAZfDSvQiV6lza%2FJ5YG5DZdTBHyfsBuTSuaGsLxSVSA7ZHg2zn&X-Amz-Signature=807163f705b762f1c3af892276efb1ae29e4fea2374c07bcd860402e4bc8a313&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672HNOPWT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBxG51B75yK5D23S7uBvMiVoTk7omM42qDhvXCWK5ODpAiEA3OXPXAqoxnd7iyvOfrhhMtuBJ1K4lvWaUm3r2jVYh%2BEqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE8Cqk1fqg8WU%2FSoZSrcAxxYvymeggUitSLc8rsQH%2FD%2B%2Fkln7kgKMWIc76A9qUW06GVlK5X%2BHsX76Nty%2FZuGcIeiIwgOY9VqnlWcFHkq53Ji%2FZ0OW9iH4Xirx0u51VAQATNHu4GO1UHEjgHrKJAVqVO3WTNbLmx31dqDLeyNhPWEQlPzcR9lUQ4p%2FJ37VOb6pQU6fgr4SPprq1jOB6SWkZyIjiEtnN3iFQbqI18DGW%2B2sdg9okkkoghW1KNxmeQ7Dfd9gNAGMPRNIa%2FbJ5a6nGAoCbEF3cMtovhv1XxROVSjVRmc223sC9zqnbphMJgqNmlufFfej6kG5sliBh7dzXAj63UmxJG3LACqj33aUXLPpLJ55sijJnznN8PMHVWnv%2B5yUk4MAF%2F6bTBySm5gNfQuy9AG8jHDvFo%2BuqMU0X65YJff%2B3Y0riJ4LH%2F820PvFrRohE86KVYuJQxR9wamA6%2F1Sx7qptly0h%2FyMHzbHQMTsiqBdyZ%2FypY5o5rpsX75w66v9gFn%2FbBF0VcSP%2B2rJQ%2BBM%2BpJzwewFB%2F7K8w9cak1KbqSZbPv99TspRDpUUnkgFIlCvbbDxWFUaxpn7TdgFau8HzMKH8brNDfJ7i6gT%2BxnJz6Rwa5VbD%2FmI6c8k6ywaQ57TYDij3gbEU%2FMLn2%2BbwGOqUBdB0LTcDRG3o4U%2FqCVOH3oFIEkiRTPUq2btEth9onvyTs%2BOuGPq%2FjLyFvVZC4DXe%2FfVDfdcLRM0VFJBT7d4gJ9GV4Qx3fLph1RkND5OhnyXZs%2Fs0bTVFxM0sp4eC4H6yLIpRnb8i4XZZbXfWCv4Bum3NXR2q7otYvGZHBclu7WaiPh1BDbheNFWFp6xf1IA4%2FXV7tj108ImLNpsWZCIH10g2WbflU&X-Amz-Signature=feee0d29d2045ebc6796a0b75d86596cf6f08231912ed60c224b35b0936c6048&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRYVQJ4M%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDDl5kJncBNoisGYN68gwEP3TJWyXfvgTcCy26nlKLCNAiAL76DBNXGhUQT5vBbXZ0ngNmNeYnXBIJ%2Fa8fmGgi8IdCqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAr%2F2XBIUk9g4tSHHKtwD2afdfTPFjMCGHLeYQ4pzhbvnButC1PWgvfhC6jb7OcxCSOecgCTiO1FAd17tO5MbNQGyYKfku%2Frj1gCda4CRmFVW%2FyAKjhQ2d68U9IBUd2b372kuYkFPJz3bI%2B5KSgOkte7%2FCw9xHn284YrLnz3IvEkpA127PffYmziXcKR6jX0dTF4rMW68cgKOSMQgC6NAfbVtGq4iJO79K%2By6Z9%2F35w3VNfUigiTR%2BxlC6qO3tX9ohMm79yPnYfe3JhfVU3lH36IEvexSJw28u4AMOZFbkXQD1Ow2UF05vRHwclaYQ3P1fOkFgyH%2FQxJpMVG3ML7%2BwRfVE4sm2Z6WpnyErLvV3TtUwxZCWI9jwVVBLScYFEFMKPnkMCw6FyVnNQ7f7dDnnUT66S3l7XDsKUJ6qlAnnHZfopfCJwK4eTfW5URLpMxfKFInDDL9RBzhIbbY%2FWowKfAhyHnlilr1pnSWYcVLQOz2sJzc%2BFwGKjWhWkMyin%2BB2qOBAbLx0xuK9lkvGvs4qq3gkItteFCMieLeSDZsoyHgUpoOSC8WB8kM8MfDV9HE3j9rjTNOFkz5oFpd7VHUX6VkfE0zEF%2BiQ5mFO%2FVFp580uPDcF6763NZDDkvEF%2BPCTbd%2BdRcEzl3S%2Bugwu%2Fb5vAY6pgFqOiaGyhLMcumiEHoQO916sT2kyKtuCcAGXf8Yjo8xeuCehCXrjp7EmcS2soGDkUfRqYbJ06lY5zFMT6%2FkVk0bbUv1TpbxyPe05u%2Bpzl6DGdfdGLHPkPAYP3JcSTzO2V%2FapHnSEMoyslJ%2F4gw5oYGiCHoYd5PNAc3Ye43RtJCCQlNCz53u6UaBupPXLKim1Km5JofAx8l4o6SfQkjlXGhdvUw%2FTr6t&X-Amz-Signature=5ff9056259fd89a1fbafef55c0e9e98fe3a00bcd2ec81dc8f61563d75141191a&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FDW2S2L%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCoVpC1oDTtfU7MwFLelKO9PUw5%2BzDNZIPrF4xb06alGAIgbCrAny2eulwkKMAv2zDDZPl4g2qNctSqbVkNaHs0VIMqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMCnkmeUo6G57XwdzSrcA1A%2BZNsOAejPZ9MjNoXAH38XV9BoBO5wFkNr0VdCy11C4X4usT4EGmjol9GZdOLPz%2FPnQpoTvEqasOdEDt7eB%2FgC7F%2Bit%2FtrQry7aIH9ip%2Fkw4RLNvOQBiqUwjG%2FgdYc4Z9ocMpNbQ5QcDo2f6URTGFZaEu3726KZhmbEdey8Kg3QDL45AP8IDvRdOc880osJeZ%2BNe%2BnNZ7HPTENP4xwcU69hHTrf6MpvsUOUj20f2RDpd3K9zW5sSsuhBRUIlp7xfXDKcZFvPqdTeIucYGri4NWPHGgS8E6ZLovTy6q7QPCie%2BiOZVqtLCQ12ps5srj39aOCp0GUvBNxQkDwcvOSU%2BW4kCB4S41KhcNbFTVq6cCwsDXDBwzCGuHbLXFSNNqCwq1v41aCWncLCb7RW3cdA1PzqH9GLGq%2BH1shAQhugcBMJjxokEZkiOpv73C%2F%2FI6eXgyA3ol5q8N5iTbebX0zILIm%2BQaKGR%2Fyea4rgyofLi9e0BVCPHE9DGtHG%2F32q2puv%2BZYhLQvLAKI0PrCTm%2B33RctolOg%2F%2F6kSqAlwB5%2B2JpQfRgIgNt1vlxXWXl8VeZMuJvGnuiaG7nPREyUg8dFP%2FJnYjMl7QeAGgBH7KDUh8mdd5PHrarTs6IGDw9MJn2%2BbwGOqUBIOxd2Vn%2B287YOxX7SsaJubRSYqfKG1Q0iRvz0R9xuUsz2kUW%2Ft8qMCPlTCOB1DN%2BRywwD%2FO2oqsuTE6ve9suaoFWfLK1s7PpmCsJ2NaTCIqe%2Fe%2B6RyVvaUOh2MPOKQOCRQ9OCiz0xxZYDY%2FKlKmdCaY62Yu%2FoG1i9ELQ2OF7QDU04%2BD4fubObL%2F5%2BJYn1tfCNO8Z%2BTQCOE74frZFk4h3fCmyZB08&X-Amz-Signature=d1cb4574c9d183e5d136c5252e4afcb72a89638acf57391f9ab3d79e7b3def73&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664I6PIAHA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAVisr1C5n8EoUrnHOnG14%2FANDy4F51wTwZ1wmMJ%2BeZwIhAJFU9yCJUBFue29i8rb%2B30Ix3uSmngi6qToLJVNNvQwfKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzARudlO%2FKi2AWQB5oq3ANFLIxonkOF956ZGUSy5N7ShVsUsqCMZkNQpOKglBy1l7ZC4i8d%2FK228IEgv9g8oRZwa9cd71K1VRdPUrAfvl8gg7LCrU5vWlbehVkHfQG4dn8uU%2FUEXZlszkJubLsAt2zwRYE%2BGgfvKMmZwO84vtSRtShSB778aDnK0%2B88ZzYg2et1hABcEtfmyVjyWgYmECD6ZIy6jZTG2M2PdNoJdQ4LfoPuBfL2tQ9s68LV6fsaurkPhTGYhqL%2F9qpptgxA3AAsII59CZ4dqmTAAa9UU82OgMCW8mpCsosEXRY1AdLTFoTHi4CedLh%2Fn%2FWAjFjm9%2FEDiAtk5JvHXVcXinWqJ59bTWF3WvY50a3HX0ZuYDXn3r4mY%2FkLlhLc89B6Ep2X%2BaaGshODQnjIHMAmcZbssmBnXFETN%2BQKHVsw70YCIcHAK56UBTEr09mWa97%2BaB9SQBT%2Bcpm9mwQZ5QFSPRYxQxUkmc8MnT%2BAoFLgKeytBn1ufP55ffsG9VPN2WfKknpEI3bv%2BYiFmkUJk8fUfYDfocJaN9%2BHsK1rslf6TIhmefuMOC2d3LWsHqYC17TD63jpni%2BTRnYaNtuHkFJ3uCDb7MYQHO5RnTGD6oxiYR9LL8YE5Tt9W%2BBS3ek9gwaMxzDC9vm8BjqkAdcd953%2BqPP3cIVpHJJHeEQ5%2BEdMaqAoaE2mulvaHMhfxBMSwNyY4Mfn1%2B88eb3kTyh%2B6JlzoiGH%2B79mSeu3BqD1aqeLJ1p3iuGbAlu3LBJMZn3%2B4WoAzbkJQu5%2B6tOhAFDoTjn63dDnsaAL0oDzJmaSmEE3Ltr2vmN2GR9Tf0%2BdcTn%2F5wjsUpNRy5WjTQJ8HK9n0kguHdyq17lp791dqsYVvT4H&X-Amz-Signature=5b9870c22bad7e0b0b02fc7b1be18a847b639bee5621c733c07fcf711b166e11&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672HNOPWT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBxG51B75yK5D23S7uBvMiVoTk7omM42qDhvXCWK5ODpAiEA3OXPXAqoxnd7iyvOfrhhMtuBJ1K4lvWaUm3r2jVYh%2BEqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE8Cqk1fqg8WU%2FSoZSrcAxxYvymeggUitSLc8rsQH%2FD%2B%2Fkln7kgKMWIc76A9qUW06GVlK5X%2BHsX76Nty%2FZuGcIeiIwgOY9VqnlWcFHkq53Ji%2FZ0OW9iH4Xirx0u51VAQATNHu4GO1UHEjgHrKJAVqVO3WTNbLmx31dqDLeyNhPWEQlPzcR9lUQ4p%2FJ37VOb6pQU6fgr4SPprq1jOB6SWkZyIjiEtnN3iFQbqI18DGW%2B2sdg9okkkoghW1KNxmeQ7Dfd9gNAGMPRNIa%2FbJ5a6nGAoCbEF3cMtovhv1XxROVSjVRmc223sC9zqnbphMJgqNmlufFfej6kG5sliBh7dzXAj63UmxJG3LACqj33aUXLPpLJ55sijJnznN8PMHVWnv%2B5yUk4MAF%2F6bTBySm5gNfQuy9AG8jHDvFo%2BuqMU0X65YJff%2B3Y0riJ4LH%2F820PvFrRohE86KVYuJQxR9wamA6%2F1Sx7qptly0h%2FyMHzbHQMTsiqBdyZ%2FypY5o5rpsX75w66v9gFn%2FbBF0VcSP%2B2rJQ%2BBM%2BpJzwewFB%2F7K8w9cak1KbqSZbPv99TspRDpUUnkgFIlCvbbDxWFUaxpn7TdgFau8HzMKH8brNDfJ7i6gT%2BxnJz6Rwa5VbD%2FmI6c8k6ywaQ57TYDij3gbEU%2FMLn2%2BbwGOqUBdB0LTcDRG3o4U%2FqCVOH3oFIEkiRTPUq2btEth9onvyTs%2BOuGPq%2FjLyFvVZC4DXe%2FfVDfdcLRM0VFJBT7d4gJ9GV4Qx3fLph1RkND5OhnyXZs%2Fs0bTVFxM0sp4eC4H6yLIpRnb8i4XZZbXfWCv4Bum3NXR2q7otYvGZHBclu7WaiPh1BDbheNFWFp6xf1IA4%2FXV7tj108ImLNpsWZCIH10g2WbflU&X-Amz-Signature=8c996a750b4c73aab5bbb2a35ea5d782bf3408ed23675b820f8f85431493b8af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPV7JGYN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BjIRxr3TNTKfqoenQOHzscDzcO%2B5moBiAtKrl0%2F0gAiEA5kPtLD9I3V7fWDoXXAUlWcMGEh0xR75hx%2FVtO1U%2F8JcqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiug9fIvomu7z6igSrcA6m%2Br3Sxs6DpfRfqtu13%2B2%2FsfQhDF13At1BkNpGJEYjqbGTA7FqsnRAfDrp4JcEXgWA9IwOgwilZf1%2BLTAzaYbUujwzEQQf%2FQ%2B4tWTuMiYHjjqP3JNmN%2BmD8ZmQusmXEHgPCsO5XEGS4FFIKcL26kf8iBCxPMS2h6Jvu%2FttjaHoyqUOHAVyQgQ%2BMeb%2FOGlW8D%2BjtqZBqSv3P5eT%2Fus5khoA8EAqM%2BxzoAug1hlvShp4xfKbdykI%2FK1npsgku8SfeDLfjM0d7N1aXFkY%2FQAlGwc5nNxM%2BclkLdnAJpO9RriFKsGG5RZoyMbsN4K%2FSFVF37pam2LQUeFJ0BAv1sD9%2FOEAVEFZNv1zQ7FsSDtNWGA%2BcdzOmSYc1UXTfBPb6gZpth%2F08z9K6Y2ZfWC2NNtY6yIojMlfkaA7xH8O%2BvR7g3BXHSySdE3m2tOZiwjAzYPq7Cy4HjFdZhP1BI1oDnYMe5s8HOMnxI8ECvZ5%2FPLWa2ZKdgFPYIW%2BeYq%2FietbvXesg6ecmuo5v1PNrrZGl4IL7MZmRmAQV362oqWvunqJkZLSPTEw%2BT%2FA%2Bnj%2BROoASaVA7B1pgzcipY%2Fj6B8a2Un9WKinvxNaKs%2BqqBx7lYZNGZt7WC8KnyRnT5rIO8861MJz2%2BbwGOqUBOengyyZaYi%2BQK6F4wTs3SmoAaVipCl0DQQzjAM7tK7imQEc%2B5VZ0rBAxQbmoswJ7vRtnqRGSK1VVmNtSbMIQgPAatmT8x9dKIkuBeivcKwTO9hU9dVNi0Z%2BoOuh%2BNLVO4wQHCZCYL0osJGtCI9F92TL1RS7Vbd4JFDNtE6cFvj8wUVGcqgQz1rb98NBrMrWstFg%2BtJCVZgrHNhiDYTKRPBrA2qNu&X-Amz-Signature=2a1f757b4656cff76b6816324d88e9a75b1939e881d31c0395accd911b9f4740&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPV7JGYN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY%2BjIRxr3TNTKfqoenQOHzscDzcO%2B5moBiAtKrl0%2F0gAiEA5kPtLD9I3V7fWDoXXAUlWcMGEh0xR75hx%2FVtO1U%2F8JcqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiug9fIvomu7z6igSrcA6m%2Br3Sxs6DpfRfqtu13%2B2%2FsfQhDF13At1BkNpGJEYjqbGTA7FqsnRAfDrp4JcEXgWA9IwOgwilZf1%2BLTAzaYbUujwzEQQf%2FQ%2B4tWTuMiYHjjqP3JNmN%2BmD8ZmQusmXEHgPCsO5XEGS4FFIKcL26kf8iBCxPMS2h6Jvu%2FttjaHoyqUOHAVyQgQ%2BMeb%2FOGlW8D%2BjtqZBqSv3P5eT%2Fus5khoA8EAqM%2BxzoAug1hlvShp4xfKbdykI%2FK1npsgku8SfeDLfjM0d7N1aXFkY%2FQAlGwc5nNxM%2BclkLdnAJpO9RriFKsGG5RZoyMbsN4K%2FSFVF37pam2LQUeFJ0BAv1sD9%2FOEAVEFZNv1zQ7FsSDtNWGA%2BcdzOmSYc1UXTfBPb6gZpth%2F08z9K6Y2ZfWC2NNtY6yIojMlfkaA7xH8O%2BvR7g3BXHSySdE3m2tOZiwjAzYPq7Cy4HjFdZhP1BI1oDnYMe5s8HOMnxI8ECvZ5%2FPLWa2ZKdgFPYIW%2BeYq%2FietbvXesg6ecmuo5v1PNrrZGl4IL7MZmRmAQV362oqWvunqJkZLSPTEw%2BT%2FA%2Bnj%2BROoASaVA7B1pgzcipY%2Fj6B8a2Un9WKinvxNaKs%2BqqBx7lYZNGZt7WC8KnyRnT5rIO8861MJz2%2BbwGOqUBOengyyZaYi%2BQK6F4wTs3SmoAaVipCl0DQQzjAM7tK7imQEc%2B5VZ0rBAxQbmoswJ7vRtnqRGSK1VVmNtSbMIQgPAatmT8x9dKIkuBeivcKwTO9hU9dVNi0Z%2BoOuh%2BNLVO4wQHCZCYL0osJGtCI9F92TL1RS7Vbd4JFDNtE6cFvj8wUVGcqgQz1rb98NBrMrWstFg%2BtJCVZgrHNhiDYTKRPBrA2qNu&X-Amz-Signature=099629720d63437e8cc7872e5e46aac61ff83905dca412fc2e5eb9773dc3b9af&X-Amz-SignedHeaders=host&x-id=GetObject)
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