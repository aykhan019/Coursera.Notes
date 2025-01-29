

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TODXZCK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTxLaxEwlaVU4wUcJoOyxO4M2yUOiyn2woLiPB1YtGmwIgSANW6JUlvJfDBbB%2B6VDvT3sf0HbdtdoeNdRy%2F5Bi%2BEAqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEIDE%2Fg%2BhT%2FZtWBWNyrcAwO%2BfrL4zEv55jiEDdnfmf4J4W4Lbq%2FhKmUvmjca%2FCSYN2RmyKvgWLJKVBMbioRS5nyIsLLLX5i1dng0k9ZCT2l9OU9TpRhoHpehTwoAEuiD%2FgZZQh4u5qM0W12rusyYuJbjMyAlTPIxzyMYUl5yv6P1OfPFadDdAQqgge1%2F%2FnDnpoeM1u8%2BY3vdw97P%2BYQf%2FrG9XsU20TUwwlYbkvMbVfczrCxgnbsPoRUbJb7ZL0pBCdmctVj5Mbu2%2F2Ge2Mlq0cxd1GZX2pPDZTkPuW1k8J18MlV8GHLm1nPMu%2FkBXOGUny3RTe5xVdDE1jKPx1NjlNEnkjidaRCscv6S2XBMVrOsafDAcPN1DpsSAHH%2BMTTJpJGfwfkMFYVm9wqGEFhoZ9huahmrsiDHjQaED3%2B4Kx4e6dqQ2PeHWdR5xdY1XVzP%2BJ9S71zMRU8W6rSXN86vfaSjfYTFOKg4M%2FWn9k75nGZdZil6O5FZJNqj2JAi4fVpz63kJYGAMEdLBSQmJjhOa4iWfJCUw8PSuo8zXb9ZLOhgzTDPXc989pghw5WcQB2jTeoIH3VN5bwTYuHJ0JPzqUDZ2ArE0JBpbF8usPufFufPBVjJq9OzpHahuqRXi58d3z9FAmxHZ4GiwMyUMOr06bwGOqUBMLZZ4KXd4WY0kMYmsRGy9YEmdBBGAj1Tk5hNHtaXYNCh4U8asB6YvaxeHWxvfEap73Q5UaLpzGO5URZNQxfdWsg28gElvQXfxgrVn9%2B9Dcn2c%2B2wZsWkFtTZ%2FboOfpH36A5IaOZAT%2BEx3K7ohNG7HXn0lgOuQ8Y1b9DyffcgVongVhPz0ilJSyZD9tsJtkzzo8285iRCINFw%2F9rS4QUNrpKVECBL&X-Amz-Signature=3f3b213c0e81d66008ecd96edab9c0fb537af2b922219682937226e218acf062&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SHPIHB4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCaKWrtxwIsmqVgWBnjfWI%2BtHxysEgSUe%2FnSA6nvCmLvAIhAKJltI4V2HRmP9vIIuYcD3Xd3e1MWMdN50Ymy%2BzzjfsUKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy8n6TtHBGhI6oEvJoq3AMFWL2e47hgADNBYK2jmio7EyXDdrTbppk6xLTaX3Vl3k9%2B%2BscVCaLS6S75Oqi8UdRFRKIgDjCQY%2BHJueElngYbSJfa7LCrH3XLpou9r3dF9Wz8AK9tdDIFtZghnFpFZVJzx1f5%2B%2FNkzPZ1jzBHyNsZOm2CR2UC%2BmtVYyL6foP%2B3mL0qmhIiY6%2BzBPH1I3Tk%2FfEPmCzArjflQDCYXnCHxdMJI6P6RgGdf0edUqKmUL%2B8Ikgswg8znMASXesCOeUaWfYJyWLuqvp5bDwr2PNoATkG5IiDRDqySru8DaELyu52H93qApdXkuGa35yupIA781ngrKqGJnr%2FMBa005PWFnKQ8vPeG%2FXHyNtgY3FHhB2CY50%2BRrfgOx1J5rmtKOtjra9qsTfVSC2WtRuMKSF8eqnQTWX0Ij8sbwhAQBaiT3Rh5mady9fuV7AkZsi9oJFf5ugIIo7%2B0%2Fradt4TTasR7DHNShd1y7MmRlJ702TyQDQo7rUE41f%2BN%2BfDYZkawcvXlt%2FfXEru0T87HHlr5aBTvuhE%2FMgypi3T0UUeZ1IU6y8TAAqFvMVnP7YVhV%2FniPZEYno75WJ0tompaIxeq79DRTo1UY6x%2FhsX%2B5i39kY63meuj8UVQOCRhOyLgKa7jDN9Om8BjqkAZ1pwPN3bOLY2IV5imiBr%2FRuyBeAh7f2LiivumiOJCnAmW5VjQK5Q7eoUS0oC7fQmFRimhAEehV2%2F%2BmL1VmqSSW1IMfjHZISvK%2BABijt8CenFcmGmSRrivy6jlsK0aBFTiyUKvgjOQ05AP6pUgONGOSQFT7rorjodVOtc5PrkR%2BQWJxGfSOE1J3pXxJZePjMPVe%2B01k0VAKxX9cwhNcOK2ueCLZo&X-Amz-Signature=026a84ae1f56c60e13f6c3a45236fa11ba7b19ff6425e115daedc00ebf088cd1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AFK6VQE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDHQo7c00EN8P68G%2BFyoQoYA6YdUd5oDHkQpff1Q2u%2BOAiBNeS%2Bm7WugWNkp4%2BOm9TooLXOlQaCjz9dB%2B9nAwIHkYCqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZUyJNZ3KxFGtLWbnKtwD%2B93zLnAyVMf0%2B01C%2BvfqpWFD0m6JhmRdWdWZqZM0v4ogz9wHXtf5TOJaqJjRB3sn%2F6lFepzJYygcbqbe5IKc8bEzMPPEyD5e8IczCbPZU6ojAL2yAybeLwNPWghV%2FuYyQdW4T%2FB7G6%2BEqOf3Ui0I8pwvg6uElyGYlskDeC%2BB8%2BcMTxx4%2FGfz4cvBAMsH2gThxcyj4owsEqB%2FPC5Q6e5TFUM%2BTDy1Qo2lu1MbjxaX3eRa%2FRLNSkSUiydnCvPWeA1zVe%2FF29cQgrO11rgMb%2BgMGUH3nKHsnYhkNyaO9VrKKWV%2BrlOqnAwVRMhv2Nhz%2B8QlPZ65CKOepCLCiF71VC%2F7eCVkQi8EYyxvvJh14hg9vFZdqM%2FUdeXspt%2BQO%2FjlQ4E%2FM0gvki87fx%2FGZS5aOefz1TKtHMX%2FzrzwtNoCA%2FNcPFs8mMib%2Fw42lsJrFO2IQnwRToAX%2FR5KAFOjRrcyMBvUaS19za1EXAMIs1tBCEO65GbpUnKF7zc2WYa3czM6EDSiXpc4zRd6n2gtHNzuyEHOM%2FiP7nW%2BYB2WZhailaKKREhJZfibl9fEaKL5X2FSNXQ%2BkMGRgdrYBOQ4BA85DW6ZEHPSfEC%2Brw95xmv1FLHiMGdSKSQR4PIIK8OpZLAwk%2FXpvAY6pgHDtgJF68mYZbCuMursHMkUo2ysC%2BAYbxMlRiTjnru8Nis%2F9%2BEWnfMl0ExH2M5ngarfnNelmKGFrE2CuacuR82ssPtFR0Y74qHOL6hHtV5Hve1dmnJ12XfVMRqrFKSJ7C5T1xeLYinbi83A788rhzHs2O3hyM%2FK7EFX%2FO6DtTolmQFDzlKn3eV8eS1O9Z%2B0FS14T2rT1%2FH2MFYvt0k5Ik9KHrxDrAqT&X-Amz-Signature=16f6d5e984966c0ec9be469d4a21ac8429ba9c4b0f622eb7274128113ccc0600&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYA6J4RZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBg4pzpZWcV5KN0YXBo4lVy%2BynxY7jYjfywa5gjYIVX2AiBXXmQMLo8whSQLQC4j5CPB32usqK45ZwZCTmUPxeABJyqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmKKrthX6Q2Q8Sl5HKtwDp64SJSt5Wn794R10bUAcxEGdI%2Fpvfn%2FEAPI0EZIYQykeiszhda89%2B1hLjqTQizLLARSGrFxRTWS%2BxI4GdaxgSwoUbRvc457E7Bu7dtBnr2odn5S8SH59Ur7wyeFdnZB06nX0rXin8b1Qit0peuIb719u1v2DU7zppmntrqwK%2B498wt8uOZv3mZzYnazKDn1zXJklxiQRUhBNnMB01%2B7zIU6Rb7PcAqLGDHk9l2yHp6kZ0q0Qlqw1yYSou6VD1ygSlrH681a3ckk951R6yYJ3twhiQbpmSna7nrgML8lFsAQO094MEiqgwaR3koUZuU3uin1PXEhF%2Fxp6zisAFDAb6rYrfbnQ4UvQPsWfiVUn%2BZrv1Zjegbq5zJwaxEzWo1zwTv5HVXrDvkF2JeggXUpzhzRwRyW0Cj22nmlpyhZqmkSlArDJgLQmcn3UPMxFyKngGD5pU9OJ0V4hP9TfCrEQlkA65y%2FIIiPPxvzy%2BK97c0wxP76%2Bu2SOMmLMeJ5o0ne7IXipLNpbDjIZFu64l2Sr%2BtS%2FGYX%2F7J1dRqiL0TO%2B%2BD35DZOl2X8v6F3DkYo109YG29GvnjCe4pUDICCZ7eUR1V%2F8WKgX1pgLyhjI85c47bh5xu28CerWmj87ITQw7vTpvAY6pgG%2FfdzbKTMAGQBW9jwB0%2B7tp%2Fr%2FetiIjfPcjvt5jzvK6BKQ40vhQmXRmKgY9TmpcgoNv%2BeLJFWn8C0f1ne9TKy8nPWH2zwjMvtT4L0Oywd5Oc6lMbxF1lfpgLAh%2BMNN%2BKqUQu90KG131zkJwHQjY1alGD5qE6aavCnmrcKYmVRIKMjTAwBRf6DiujcfyiMdUOPnHV1NJY7KdXTrrCulgrhpE%2FQvu5n7&X-Amz-Signature=35f84b0233395f3644488d66eb08f8c687c72f80cd541b4e92fd2468e0cddee8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MTOGOKK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfGSMLywre5XT3TiY5Uf66j1zGgxNlUQ5maWTWgxY5HgIgAOBa%2Fz%2BCKcEWxL7AOdtKMXYdL%2B6%2BWvwvj7yxC0utZEkqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJtIDQvkorjsU1Q0UCrcA%2B%2F7Jrl4vMUP9asGisr6BslarwxBV%2BNF14tNrHo08D3DHLiJE336ei%2BUa6OdeN%2Fz%2BGfLcmNLit0ICSGD8myB0tUlOUxzMMjIl0Gb39UIWQig%2BjB%2BJmaBHynDMtw2J9cNAsblreHZjr47jFT2JJQvB%2B8%2BodEYJhMm5cHNi67QLdZ1KYsx1D84fhVydOkUxyzMCrVVe6rtq%2FI9rpK%2By1mGPyyKWSpwmz0ZKpJEu53bk%2FG3ghHPeW1hd4DvF7WUocvAyB08lZq15IrPrPJ0mI3PdnBJQlcMGJdmNKjt%2FdtZ6hK0yGsK9aYWZ%2BXFdtBbE0%2FQx8Wys%2BKU2BCd2HYfC9jvOHbg8T0ZRDNCDPiE%2FZP3%2BaXqzK%2BVzfr0QWmGKJdddKg4DB6mX8D7m%2B8RvLTOW8gyRy0zzD%2BSmGU2rZ1lWlN6crXKJYRnWr5WP2XlfWrX40r921tEiQ71S1TI3PC%2Bj3ezYxvOp168OxwssRVgyv6i0QIE0M7sjN7wA7VBYSKuZrjH1%2FOYydQNnYVPUbSIbYCcgTrTfK2XpEYMkWh9nDbsYRtGegwsKMj9Cf2GDTUwwfXr4GEhlErc%2FAlfU45qQq7znioLCR4HuXK75d57lsV1e8KL1TBFtfhx%2B%2BEZqr5OMOH06bwGOqUB4KUHsYAy7Tgm38DUpK4hlkN%2FEWAUn%2FOqxkC4Y44f5e2VX21VN4SFkPr1MezbrrgW1yLVyHpdA9M4K69g2Sk0jFZ5n%2FEowxPPo%2FfL9lr2r0NAgd4Bk9MyJJiHbLHrixuLbAoDQeY7EXWG9Gbw9zuU%2FnSU6msGNcgJOw%2FOo%2FKsxkWIP724ZI%2B8hVPiSTpJIf6rdWneLQO2ivfKRD2VlT6aDjnr7POk&X-Amz-Signature=f7a9cb6b6ab3dfff56cf40b7110337fbe31dbb6af631c266a75e2b0998271342&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGRUIXNS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrXqUmUv4yLRUaA%2B2YUznF8gxSyV1K007GIunjYMJG8QIgb3OkiH%2FWPlZBJEQDv7WGeer9LREmMpia0bKMwdBY3KoqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBXWob0X3isrpBPECrcA%2B%2BNvESiEqHqzgh2SgjBLWBhiCMYtJchd0pc4XtmXyia3AMUrYFQt4S9YhXewqDwcPEIiFJKx5hv1rIqQqMW8c225m80974IV9vPF7wE9sDOJ0kqLHA%2BMC7RqGuArbRLoT776SBvccEQVRPvFwj%2FjhDv8XIgghLYzNaXWbhV437xM0vmI88CLgV4qEHddsNizDpMt53OWtUylNJCzHofjHQ4pEzXd9OFgQOs7khWbWaHCvUBfa9LzhcFB5bopfvVdb1H8pkVJI17zSnzSwmMng3pjcK%2Fu0SPXhDP%2BeKr5F3GCPFLLdKVoZvOAqAhjh81WkbsUZI90e3Agx4vUCOc%2Fyb4Pvwhsl%2BpaHkxc4LH1vQ0tqWS8bQHPXxChge4g2BJDEbEK1pJR38EEMx%2BrhvL7RPWhjFDxcORtZt7UowBXh6z%2FEtmM7AGfuyhaggPjRHMmqIimyWMac5QYCF3Xpdx4IIgVQ0134%2F%2B46ansYJr9hbK04xlgF62E3cn5ETNFswI40beilwtGB24o7WtWNK2gfQPCAca85pqHdWtpdpbmFjfrmGQZawiyTcRgOQL74BY83y95ckvQRS9nDIS4DOkNKLQa%2FuP8ptXFkNeRjUj7DTyZBY%2Bxilun912u3W9MNf06bwGOqUBHvgXRHCippRsUOG0SWGx%2FaSwrY2blT0FdDO6JM6LENMv4kCJyO%2BnQBhkUocS%2FWZWTjIVDBYIRgnWpB6tmBasj%2FydI%2B0KChymTdJOkSY16czbP7t0hbcsB%2Fat64lGedYHK7%2Bvnlm6Dt0%2FDl%2FZYCw5EIOItLWSPH2u88mg%2B2ApzIfo9IY%2FO052J4B4Hk%2FL9qUGH2O4jqGlmrLx8WxS4A5cv37dQXT%2F&X-Amz-Signature=2877c3785a9ee80c3d43dff43f576aeb9616dd4fd33780c1a713475a28486efd&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKOLZUWP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDpiu%2FTW3rMreDcQksw227MYnzuce6Vf7upjb39yl7AEwIhAO9S0ZWVMUypCBAvgRlIMuGPkF3Ylm5QaSHvNMNbSyD2KogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyaGwX8cqzaVso9a%2Bkq3AO%2F3MzrSo%2BjeNBlsMWE0FCu7PQpnSIPlqGLxUiD9svHDJ8Hgo%2FmPkyCQdlxjLC5sA%2FKHZm%2FJ3wVlwGyxncruo6LveLeuJ1G53wEsfPpsqe584QOGoS2jXV4zjiMcv9sVDPzUtpuspIFk%2FPQxwW04%2FKfFdfVAUlnyPrqjeNFty9wtRWVdKWQFn3srg0aeWQG%2FOqnQKdz6JXJSordhRqkJ8twXeZRnsIXBaoro6IkEwS36xtejVazl8uTlH0OiCVucDXATnniTAMnH%2BlJOIY98VrDVx6lGPBLW2CbQSVsn0Cf4zypJ%2FCvw6JbFGtwLHgW%2BFliT4yCPe7kV5qdG7g1UMF8wXV0efGU0%2BLybYNUfsVywkRj7AoRN%2FL2Uh1T%2FCuxaUUgS9JXfDyB5ow%2F7ox7vv%2BH3kwv6ctGW0ogO2h7J0KGAhDX8KQtGdocrnUiy5WJ21itN%2FQk%2BHf84M8TLYRkq6XjVqgGRs6OM0o53dqKopbhGrCoucw0zJfgDvSUhcy%2FIUd%2Bg%2BuHZK7yChS22koig3%2F2wwv4QK8CRv37XAZhhdi7LP6%2BwJ6e7vpvjuVlJRLlnNNda%2Fl8ezvZ6VuuhdG9KNLe%2B2LSw3uTkfQOd9dK5xLZOduatRGmeriE8w8YOzCr9em8BjqkAXEJFyP6lXds2jFmH7zy9Y9JmIsMKbN%2FlOt7DpfWMNQZ3g2U268N8hqUW1tm7%2BPkkKss1DblHpZhr3B9V3oEtRLjJRUHHwC5LY1gKOnjEh3j%2FTzPkpbp%2FzvTp%2FZ5W8Dd1kuAulDLXtODyVOKQkZWuzuZRLqK4VTsLexr7NLh0psQioLqNtWjtVmWP%2BXjaKtzfw2epV8yJLaHE5raG0Qq18gZpgYO&X-Amz-Signature=32f3eb921c826e19cc16b7cbdc3e53d22e560a6c4f9d1502c5fb28315c508b61&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4P7I7DU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIATDQyuA%2BswYhrGN9%2FNz%2FX1IdJaunP25ojgj%2B%2Buf6PYcAiAcP54f1IwE67oHuMONRnl%2FDEd0hYUqdVhBIGnTHkGr%2BSqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIScso1TT19gfW3eXKtwDPlg8oQOYff7%2FG4tT%2FKDcBTH5xZjzz304zZreeCg1e6%2BAjOokMLGUErIqxK7ZDDoik75fq0raYnEz0WhfLza6YXqVjBj7cl00mxDmcffiGDo0lP%2FB6WCAECzJZaW%2F6x63eHhlkjMGA5fLLAOY5EHY1kRhxkQtekjdUACvg7wiBBDlwEmk5jKSJ3DQWIsmI9SniiAjx0PqB4cgnIlTWhH72qvKAcU%2FyNIOMDK6ooBf2%2BAdJic4LRCsuLdRoe5ubE5IETutrSNPzN8LKbl0Fa07Ts27IjYSLbGm98ZRs57kDID3J2O%2BDQ%2BeoD9TpAIckF0ZVixHDQ6p3TZCn0ASBgQbAc8KT64btK8fzk%2Bnz9nBvv%2BBIL%2BdgTHqPAzdl6AGhpelnltriGzEfJ2lfSedxqWqE%2FJYvvjVdKSKhj%2FADXlGiJHwpxb%2F54hXl%2BcxL2BV1Dmbp%2Bgy48sUlDS%2FAk6apUl0vU65hWv6QR%2FHgz%2BI%2BosoUgU3ClMVc9tFfhvwF3Ys3U2iu14d3ZzH5mCnFXoMEHC6AGiqRgrOVzSOSOYWIaCYoTNXg%2FcitFV%2FehkQQCHsKJK0vGtGQaRNtdFEzrr%2BsZXySrfHqAUBYZxD2CyI0kABbvMzAZg%2BBTKCKrxMrogwwPXpvAY6pgEr7MZQIwaH27sD3cSSzOaJPTSGnTqqW74ShgBSuIU5diQbmIJO8Vq0k8Zu3%2BkeYKBsLcUei%2Bi1wKqhI1htmIpUJhpguWtRXmwhjk0jnNXkr%2FO9gNQXyg8CjRE5UdAPlNruS16FvNZ88fdj4K6u4jS%2BFrSgL%2FIRQ%2FR9BvCrA58HMe%2F44VYASgT6A0EwIl3kJTd9TmVpzEOJzhU%2Fr6CuXhH1n%2F9iBoNc&X-Amz-Signature=65377ee13780ebb4567ca0ccd090b1fc1aaed7705068779f372c781250c78333&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MTOGOKK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfGSMLywre5XT3TiY5Uf66j1zGgxNlUQ5maWTWgxY5HgIgAOBa%2Fz%2BCKcEWxL7AOdtKMXYdL%2B6%2BWvwvj7yxC0utZEkqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJtIDQvkorjsU1Q0UCrcA%2B%2F7Jrl4vMUP9asGisr6BslarwxBV%2BNF14tNrHo08D3DHLiJE336ei%2BUa6OdeN%2Fz%2BGfLcmNLit0ICSGD8myB0tUlOUxzMMjIl0Gb39UIWQig%2BjB%2BJmaBHynDMtw2J9cNAsblreHZjr47jFT2JJQvB%2B8%2BodEYJhMm5cHNi67QLdZ1KYsx1D84fhVydOkUxyzMCrVVe6rtq%2FI9rpK%2By1mGPyyKWSpwmz0ZKpJEu53bk%2FG3ghHPeW1hd4DvF7WUocvAyB08lZq15IrPrPJ0mI3PdnBJQlcMGJdmNKjt%2FdtZ6hK0yGsK9aYWZ%2BXFdtBbE0%2FQx8Wys%2BKU2BCd2HYfC9jvOHbg8T0ZRDNCDPiE%2FZP3%2BaXqzK%2BVzfr0QWmGKJdddKg4DB6mX8D7m%2B8RvLTOW8gyRy0zzD%2BSmGU2rZ1lWlN6crXKJYRnWr5WP2XlfWrX40r921tEiQ71S1TI3PC%2Bj3ezYxvOp168OxwssRVgyv6i0QIE0M7sjN7wA7VBYSKuZrjH1%2FOYydQNnYVPUbSIbYCcgTrTfK2XpEYMkWh9nDbsYRtGegwsKMj9Cf2GDTUwwfXr4GEhlErc%2FAlfU45qQq7znioLCR4HuXK75d57lsV1e8KL1TBFtfhx%2B%2BEZqr5OMOH06bwGOqUB4KUHsYAy7Tgm38DUpK4hlkN%2FEWAUn%2FOqxkC4Y44f5e2VX21VN4SFkPr1MezbrrgW1yLVyHpdA9M4K69g2Sk0jFZ5n%2FEowxPPo%2FfL9lr2r0NAgd4Bk9MyJJiHbLHrixuLbAoDQeY7EXWG9Gbw9zuU%2FnSU6msGNcgJOw%2FOo%2FKsxkWIP724ZI%2B8hVPiSTpJIf6rdWneLQO2ivfKRD2VlT6aDjnr7POk&X-Amz-Signature=72c17b7d7e01a754ca3580d68cef1aed53a61f6659ff720a4759e714364850c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UR6QEYL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrGLxhnIb3uRKIs2vPPrhUYAsjP%2Fcp3xeqxCjC37Q3xwIhAMENsHyOFbjzFgk90RQARa87zuCza%2FTXbCj5iIWrZ6LZKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQmAVDBMSH5W%2Bk8cMq3ANJrWPyOj%2F36SAPy5yekSzQD5vpqLJTi9XqZ%2BBgzqo2AlyhuhmfwaOe%2F9lVNJKCsvWpRiKC48M6nb5tm4NZ2TDu557SWYIfARxL6ai3az6ii5420DppC0j%2FqIlHvmxTLHjDSEnJDAJKtPA1Yc1xKAnnhHza0e97zZlraQqFw7S2LDkmE27amZspRdzBMK6qDq%2BPcDbeiKqqh6xcLAfQf3SSWV0hMrjrLeKw%2BERSTKPxOOGogY6NSfQqsdHuLYfnhFIMoIDlAbjSNLTrUeorlbZ8p20VClH2i2VmDkTADXDPChNB0gghA4tVGJ4TKROmh0EifAI7b0EP334ji00KNWgrrevVhvj3UggpTJNX27tQ4crsf9%2Bl79aB1Tlv7kkPzr%2BvVpZmA4ZNBPdyFvTYStbkI0v57h7H44PVkcNPGebLsRKd9cIH8kUu5sOfSZY%2Bj%2FgHQmuQ5cz2NFKLLVuUs6TJwQ%2F2%2BMTZvRw1aV76m4jX%2BpXBVbFbdH676ZBKkzfn1P4FgT5stP3KOahTYhWpD4eItT5BO%2BAQEK60%2FlYbcsgxR7InbGtvgoW0PhOdF%2B%2FGwL5n0T23idQAIckygdDZ4ybJ6UZH0nhmkeEiGwKBk4PoBKK60xG8I6iPjTz97DD29Om8BjqkAT9iOtstRpqVAy2ERYZflGWTEMoFxlOqGYMFJwwyiTaEwTCfzWCkBpgKTdiFxhIlxlBmpVwuZM3OAXEmBsUVFvHQ7mLuVr79sp95JXDfT%2FfWC205qvCdtJftVMQrJzwD8P0qOM%2BKqxuDEa6bg37WDHqcQpQj8B8IBe8oxiHMg5wXs9ZxHUNH%2BkCq7pQ2nBwrZTsyqZmy%2F2t2BuTnU4V8QHey6WSP&X-Amz-Signature=8d01932337ae2ead3b8216998b20bb1f275cc3475a747babf98e7bc3f97ac984&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UR6QEYL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrGLxhnIb3uRKIs2vPPrhUYAsjP%2Fcp3xeqxCjC37Q3xwIhAMENsHyOFbjzFgk90RQARa87zuCza%2FTXbCj5iIWrZ6LZKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQmAVDBMSH5W%2Bk8cMq3ANJrWPyOj%2F36SAPy5yekSzQD5vpqLJTi9XqZ%2BBgzqo2AlyhuhmfwaOe%2F9lVNJKCsvWpRiKC48M6nb5tm4NZ2TDu557SWYIfARxL6ai3az6ii5420DppC0j%2FqIlHvmxTLHjDSEnJDAJKtPA1Yc1xKAnnhHza0e97zZlraQqFw7S2LDkmE27amZspRdzBMK6qDq%2BPcDbeiKqqh6xcLAfQf3SSWV0hMrjrLeKw%2BERSTKPxOOGogY6NSfQqsdHuLYfnhFIMoIDlAbjSNLTrUeorlbZ8p20VClH2i2VmDkTADXDPChNB0gghA4tVGJ4TKROmh0EifAI7b0EP334ji00KNWgrrevVhvj3UggpTJNX27tQ4crsf9%2Bl79aB1Tlv7kkPzr%2BvVpZmA4ZNBPdyFvTYStbkI0v57h7H44PVkcNPGebLsRKd9cIH8kUu5sOfSZY%2Bj%2FgHQmuQ5cz2NFKLLVuUs6TJwQ%2F2%2BMTZvRw1aV76m4jX%2BpXBVbFbdH676ZBKkzfn1P4FgT5stP3KOahTYhWpD4eItT5BO%2BAQEK60%2FlYbcsgxR7InbGtvgoW0PhOdF%2B%2FGwL5n0T23idQAIckygdDZ4ybJ6UZH0nhmkeEiGwKBk4PoBKK60xG8I6iPjTz97DD29Om8BjqkAT9iOtstRpqVAy2ERYZflGWTEMoFxlOqGYMFJwwyiTaEwTCfzWCkBpgKTdiFxhIlxlBmpVwuZM3OAXEmBsUVFvHQ7mLuVr79sp95JXDfT%2FfWC205qvCdtJftVMQrJzwD8P0qOM%2BKqxuDEa6bg37WDHqcQpQj8B8IBe8oxiHMg5wXs9ZxHUNH%2BkCq7pQ2nBwrZTsyqZmy%2F2t2BuTnU4V8QHey6WSP&X-Amz-Signature=8670dc0ba4c3c31e79dd2366e0383aaf1e088343faaf273a772993b4981667ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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