

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JTDGR2G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIE38Lph6D9HLYPVD6SsaFUb0%2F2kclvjQh0eTzuku96ThAiBd4Xf39k4aMr%2B6tW%2Fg2pjRrMDAL9qsGvZiZB1N4E8lwSqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1S3lF54NKYvTmzXMKtwDaGFuK%2Bv9Bxe6ElBPy1u%2BWU%2BAIsvu%2BvzS99ok43qXezVCTQ%2Bqri%2FkC4G6w99wok%2BLg5wLNtZKG2N3aZIr4kTA99cQ77GnNKuGjoGuPdMS5Tm%2FSqqzffPbh0sKbjm0cUBCg9vPzPxoTOr0EG8Mf8tnK7Wf41Z8OFV9W9WX2rcLyYifhXE6SXhjEXXJo0fiEr0oAB75l9oyupuJPTDvu7PjBQXW%2FHLg7odABedwOncMkRedMwaFHJ3rYl8XfrAUhONN9D0XwTDfmfhQh7mmEpECoflM2hiJ0%2BuicdBA%2FXZVO%2Bow170mwAFOTCy9kfxDvyEbFa%2BjacO5I0lwnKesei5GJrF94psZfEPyIhRhILB9OxQP1KxZTTmZZ6HMGv%2BJNmjXWRJrOmO8xcHP6KD%2B4onXpBwMb1naooht90c07yqk5jC4PJaCzaIdWVYanRjpaxlXIGToVaENZFioeBhbD6B3JWKFaY4M9LHXuSEtbYjbbVh93n5oGLqest%2BRWhCz8bCeo8ptmYZgG%2ByC3J4zmvJf3eM%2BD1zyoX8%2Bv3sAKVG3MTNitTHNHv25X7nVoI3N4VDBD9bCL3zp0GbbudntJR1YzPyvLaQOlPN%2FfY7zAiX550SLGzlbzPe9%2B%2FCeLHkwxr6avQY6pgF80j2%2B53YSfRDrShZ5QPBX8h0WXkaLQvQNvKjMVh2XQUjDyhRfcqGqqJKVHl6NqAcz81pGEpvK%2F3PB3bmSnX7ORv9UtXAJodoQIVwN4M5rGaS0SWqocpGuVg9qtiCWAlUeYlcZ0r3pdlIjZ%2BWk780pa6mYKqVyOArsI0oIhlh%2B3hjyL2K%2FE%2B2yxbWXchj8HMqw2vIFcIcsvlv70PC9CTjZQdoZ3iav&X-Amz-Signature=f873d885746db17a4457af0a4491d5ffd9701b480d07f1e81a551d949f84391e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCGTW3OW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCID9kKa4TUgHHTqEcphKT5tP5AbU7xxyfJwsL1bptdGCyAiEAhYh3hvIpCyKWTjSnTqD8HzRQdqkeOvHCtbY3NX6rpf4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOf887GVK%2FjHo5zXWyrcAyhH8%2FoOGzYtNiuEGjN%2BOlSumoRz7kmKIxppC%2BLR%2FqRI8PncgEsTTxjcP53nhzphpkGHMN8Ax0N9jBJ4gDHfsOYKobiQrWRF3Rt29Gvl1BVaA7rffezBrVHiL6q%2FNvyRs1WLu85sYoreJCAb2NowddiE0FCvl51BstdrpFYfmW0oN%2BYGdwiFnkrIwkdS0ooz9y4PaFp6DmaUtmARxp2rjn3R3W2Dq7W19WNocipygV5py6h5k45TVN0O8qQQPkrnfibb5ZLFqfAh7FuMSh4%2FXyQgnzeUWT7Oit%2F8iyRcdyqM2L77%2BqhObzZKahQrcM6LbwbYjMAaOv18Qo%2FuHsHxLcyNPIs%2FpeKAmyzl0wJRlcIaH%2Bsexae%2BOGkDzpJ5m%2BPE%2FNW8mLDH7WqGo142Nver5spRSU61cpW600zmrSmC3bTwDJW7gg5sVMGejgTplTVdUKkAid2L65Xhneo9luX%2BmPmhcLR%2BJqRjTWjAimlsjB%2FRxJLDneXNoV8X%2BhYcwRuhvv94xFkAX9%2Fy6tKEJIP1Pu2ny00mZcrCAgQNlw9lX6LH%2FSz157%2FTSii51IU1IStvKo2mW4REraQ3hqcXiXe30lLpgQB3figr7FeWLf%2FixGHZKQbAaxGWn%2BZlpTqLMOy%2Bmr0GOqUBezkWTljrie%2F1gdavi0eheiW9NruBpJAETMqIT29NL%2Fir85O9hDw1kK7tV6CRQpn%2BPX%2BXbHJsN4iyE89ILaVJmU%2BuOwwVuBvmIYyMdyjtdub0wM2t9NtlMXndFBbIJ5BjaBDGGbB3YAWieBj6OMySR6gSH9LQsDpbHY6mvWmvjrtIwjLLyR0NBI8TzNyJy9YtTqzlIVwKEfCnzgilqaqyVh%2FUP%2FYu&X-Amz-Signature=cfd52baee6668c07ba05139c53d54fc1e069a2d32102112ab80b73a6af9f2e98&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJSRIYVI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJIMEYCIQCJzFlV4hHXRPqVWu01bkNL%2B8BkCi%2FZEdwExprOpsURXgIhAN24XET75hNagBtmGqr8y4NnNnRSrEZ6XmQ5zzknK4%2B0KogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxE6%2BrtkSV9PTE0xOIq3ANZH053TpRwM31yta%2B2XS6%2Bvw5AK%2BNvTgNU09EUmCTXrhdbKrNE2dEOqVwSLfpMV6UmBYRXHjBqA5LaBcL4MTjfzFfq83btuwWOrpMXr2ON7zbC4bLE%2F1JRpDTk9cS4cCmyv7s8DTdwsFWMqStzfYsuYDszjglkAlJCRacxP7mzY9vFpIBwyb%2Br89dTZHL8hrXgVDz5ywKfceQcJfJ4R3neaVs04iPQIHVjQwz7%2BUUCS1mmL1OEuSkfoGggoicGeHcFafwG3OnZjYVtaL7t%2FW4ATR2un2FlZXwLWHT7fSuJ8wCoGE8XSerZuTG8ArCvEfHcSdP9IJFP7pSyXOIK%2BEDjWVCigKwthj67jHPD4at4t9mcm0D1EoS9Yxp51z7H4WWOD0NwSxAL8lgTBqc3PsoOqkVlzC8MKhXnkzBT6xAoEQ046Tgjen3hvvsBTh64fQ%2BGianjmv1XoG%2BewmkZc1ADc%2Bf%2F4u2y%2Fj2Ibf6V6%2FM89UkKpre4p1fJohbDbLoWcwlQG8dgeELbjoPmv9hNLTHW%2FMKUk4dkKzi5e7d1LzbFNfAKuh4Sv77pajedSk%2B%2Fu%2FPo2Li0APiX3ND2orsxpnj5OsPpSuQAVEe0DSn5l8HA3lraVuyinLin38FmBzDsvpq9BjqkAT0NEPwUrAMuxd42eUlM8rs45I1em0ne9wSjBS8F4jlhgyKuBkr8s9Ak1t1DhOCrcErztP8jfHK6XOoCAtDPcqne58HbaUdVyCcqswsc1IfXgj%2Bf9FYu1Tyra9irxgS0xcgubru5eqoQjOWYxGPa%2B7cgKH7WJdFlAGY3sO3OFAUpF3bQ9YMYx%2Fz2vf5aRRPZJ9ABngDqHLSvoP%2B5azeuVtdvf%2Fw8&X-Amz-Signature=298ba7bb680e52a3d72c545af6b20fd00f8b14b411effc826e67b54bccb285f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XQMEHC3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIQDA52YXEl0BDpBI0f%2BAN9QZj5UA5Nkdp%2Bb90jiv2xPqgwIgf%2BJgSYDJpGPEMbSUpNoMMm5HsftHlK2Gtyj%2FdF9N%2F1sqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPhqOpde5Wx7Pvh%2FdSrcA5u7SHdtlKGtGeaY5pkbtaPhnKeRC1qXCK29fG3G1oao7WZ6klzYINtj87VR%2BLLpm7PueSUOJn89ve%2BlZzGVWlMEgvgnH7oeOrSwNJMHZqSVDhQ%2BQeck%2BFUiOarcQJnuRn7q2JtDuo%2FB2SMDTPT5GKccYVoxaJP3H0x6gIv1lejPO09XvszLR0vJDeKR9TqtDNg661MKkJ44qclarsGqCJ%2FppxxogjpqYS7dSzoZrXm0atu4ADGFzhL4eQW1DA5mbdgtVuk38w7ErNfzAB4wUG8TRiUUI2fadOZ7EqjybUc2G8ltB9J1KUFcl%2FwAEMVPuaqWrAPAyZ6gX1%2BpuNBylKAmm6c3Jv%2BqUQvYejvb2AFtS0lnmWaPUG3a4J0JSM1A1CTlbLMYfvFCBR9UVXi2kqDpyuxbqDmC25a1jw%2B1ijAGF%2B2VxKvfEe6uuXUWi89kceJBE2by%2BHxzCUS85db65Bk6aaKvosWXsjfB2qn0y1DKw%2B8AWygbTIoMP1gdw8zPSCL3jRsfmDLRTjU%2BR%2Bu%2Fg3BXbEq8sPODaoPkaHH0BQO77%2BELumvlx0aRkRacDYfhREMUYaNs9hwK%2Bd7yl4diGTO75WRgNBOcz8XU41WWre3nOSTMkp45qZdvyapLMKm%2Bmr0GOqUBj60K2iYKLMwLd9G8YJTJvOOkJHUAd7p%2F2FAI%2BL63NNTUWe2ik3YrbcKJDB7BOrdTClPoDKo2PGYW%2BRcbbTx%2B9HxpVSMcfvLPZV2BOlep4r8%2FwyIWTZZP8I2Ijvkgmj%2FDmmfv7XIZq%2F%2FB6HK%2BtDMlxVP9IdyfnSmEx9OFCQfaEWllqqNbWvXx4w2wOAT%2F3wT8Idu6pBykXJskkhuo%2BnkJAk81%2BmNw&X-Amz-Signature=b65a62159469326026ebf71554e317dcccf8af20d85cc0d3ba08bd8b717c39b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSAWKXOC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIGIJOUE0POluvF%2Fs6ebO%2BSxu9MSzzu2rOg0ZaEkmpzkXAiEAwAfX0au7aKLCRqaiP4jR92cSb1yEXsyGQliBnamQs6sqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJO%2FSxvOp%2F6w62fn%2BircAyL0XfugXVIVbayeq2Rb5zOutmRcxwu3X85kknyEwNXPfBfkaseqd2xm8VRI75LMhRU47Po6kcQkwG4fBICr54HbQddEd8jLfnISIP%2FXBc%2FAYvRw%2BapnOtsnIfTIvC0vpbjONN916I2gyRC8Kd8fnGZ6Y5G4qaaV2of5POBP3I2bzahzq%2BoWtskifp143%2FHRp1kzyBr5VCrPZ5rliZTKWjiYbCXOlSBSj5oh9m28OxHbCZxImJ8R3u%2Ftfo9HSEFfNhUZucTt3cxPn2C7Mk8ykffvSSaiwnnwaf9OdD1HbpvOCp%2BBnW%2FrsXtncMDXk4SuXg9Ww4xowDl6hoWCQUszVKjid38%2FZp4%2BXnfKF2wcAsYjg4YpZeNNytzmyjcdiXnYbXErVKN4dKiQSR36xoqmkD6p1x2zHEpgRoI6ogzLhC%2FIJ6c3B%2FoW5RINfK2gNDpaI0Sa7OFFrdnO6zoT%2FSwjn0Fs3jVirLFaZzfdLUCEadx8dYJ4AHgnJ2RP29hVm1LcDxj%2Bs87T%2BStXTzH%2BjQeBRFKXPqhrOWngMeWENncHutjkNTKZFoH6Ap%2FdpQhQgUDvCDSceEhsjmI4PeE9SZYGEl6%2FXDOOWL0hketUZBGaFZjvvRGiRuyQeabRJGyuMJO%2Bmr0GOqUBKmVQGG2GKE%2FusMy%2Fi4j4IVx0OBTir4G6UPsbOECVc9mERQSZMIQAoBELG6YwuG8JlCIKnhrm5sCMzHJp%2Fj8SiAqwH%2BePLa5zpHMWV8JXhE5zHnOuRhzxf1oLUBKQwG8DkACd2bdNYxodbgHtopQ4aK2uOwL34YMOVQsMvwLYqzUiC3BY0n6q6pv8G2bb2zZIH2TFTmhvtD%2FLXIk%2Bq5RBOj%2BiqQHp&X-Amz-Signature=c8dfc5426d2cbe835843ffdee2672de908e5eb6070215cc424a72fb7866d26e7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWGGQYWM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJIMEYCIQDipsU8J%2FrhreAM41%2FEGvuvzE1SGAdctl%2BSUeNVXT3wWAIhAPan0k8ZGFd%2FcrOVK9YADtRKE0g6%2BmF%2FQpji3ba5uEpMKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWI5t1qEICaqC0evIq3AN85L5fAGXVEOZeZ2pzUtGhnB5mBc6mPqDY2znH6kS2DmOZzhB0IarbKLcK%2B9R7PdT9WWFT1e3kuTNDcEKliUHixgNyOweCg570KAqG0HgVd4Zfy1aF3jyjroOQpVoAOmKwUshftEZdGwo%2FagkHScuWEN1lpMQLO6SdJkgZg8c7nnsOPLg1jyHOdBds8VHcpI5arJSZNp0r86BoM6fd2C7UD6l%2BTd9rHaPwhxvppTF9QWYUaYPmiQEhNk4nc5RlAEboExY1E4YVMpAJ3f6nXo%2B4N0Xry9K1gacU%2FZpFRCoCtxxGL2kvBii44iFa2RDHWQCxY5row659%2BMuo2bLzUeWQ3HG%2BN3XXTSovLneUYPCSH877uoEKpz5cmwjL%2F7hoe46gKoKI%2F%2BCkSztwfz1nrRs0hoojXaGkKuyGGsVwZLw0In8YFBbd4ilUt4neDmmQBV%2FG5DQ2xOLfbHBgo0nu%2FJXi7DAsK%2FtRBliO1%2BM71%2FaDhuH71m2TpRmyLkguz2H9mKrQ6m1lLND%2FH06GHg%2BzTAo%2FVZqHKYCMVaYXAjjF56y0Zk2OH6%2FDWUmesMFgOUbnAfb276hnZlCM%2BBqAqznhabhSkFIPnjzxZMplY6SVRrh6ruUY4eR%2BbD0%2FQeTbGzCmvpq9BjqkAXekZ2tGAMLNkdgkWoWusV4Z4gLjAD8Ny%2F%2FK7cWEkCDpC9qJF%2Bok49h86N9ohdgeiNhTmO2iXHJQ9xU%2BBnuOgMyzAiKwMyeGsdXiuQN5Vc%2FtoiD7bhLFf7uFYYwwYfLnt2D0hTLnj%2FXTudgdUyZmtSCANZ6qrpdt8biFDVB9sXyYBwXxHYzHcFASDLwEtIlY%2BP85sD%2Bh9quTtPRjPTpgqXHJjQwP&X-Amz-Signature=e6aeed135738c7d95cdc85c6fea5a0421301f950b50b2b7c5274338cc2ae36c5&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFES3K6V%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIHxuMovH12vkI%2F3CzWOJ%2BJaTR3q%2F%2FcxvoC%2Fay5aVupH0AiEAgrcEUdPIXn5120HShhxpr%2Fx2t4EqYz6bi1e3m8skOGMqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDENqR%2BvkwT4783MF4CrcA12euOXUgs0rdyHdGz%2FudmCJXXJWv7pu3ym5CXG6uvE5MidJq8YH1V6STvI2JjXyI6a0IlfEm4aKhHy531qv9AOHG%2FvnUjvDqDiVQJe6GKfNVbWu%2B6GxFFjYgggGRZi9qCJjwtT45jLRDTeywYcGLY62avTNpUUUUOoIsraMbV4mPs5NFXjxXLACp9oyUYV7P3Bl4ZEZ%2FkN4b7TgvIl4%2BH7JJBwW3nR73ukD%2BitxPgkvDO7OAsqoLUsA32lh7QDc3PzlYJtGn72K6LTYMarQsMfnR4jksB8H7dkxK1AO6aeSlbw%2F19AkGfWB3fFmmX7JpVI3HW61xlqRBFoTaycMBFzeckcBuR5DqNAIbhjQAozUVQEcdVN3Vx%2Buuv0fF%2BaKadxYWKVH9OzN76w4VUWHRBaOQD2q8Qtt3qqkEgeVIWhlmMXjgL7%2BIyPzQhgy3B%2F%2FHhwb0NZHSY7D3iLjEWApRSyIYhX2ewn%2F%2BKKhewvQjjH8qLIs%2BOinqhMo1Qzj%2FSjZxJi%2FgczI1zd0ZOs9D%2FxFfGyRLMLHgmeT2ISP0DDluw4g4eIKoCYzf86Cm1aC8WFKAqdTnB78oyNnJ4SpO%2FR%2Fo3weH%2FlHpe9iTmTFcbiCekNg1i2DX%2FnWdU2QODzQMJq%2Fmr0GOqUBBAnZ14VVOJ9pPGUvl%2BK7jHEcLTHbLxJuBX%2FQ3vL%2FRY7tMagsf17Czz0VI7stPTjX2LkaebPedQMH3ltcsA4Tn%2B%2BKnzZx4MecF0iVGPsJb6DV89zcZmF4AJyyiX41rbRjRK6An%2FfEeNZO8%2B76aE65d94Ayxwwsx6qatkC2OBy9VwpJ1gh%2B7XeYxw1TIh2mUtlvn92agyeaqYeUV60rO0s%2FkCCjsSn&X-Amz-Signature=90b7cbb62818ea889453eef44e5edbf54d2f5719152d0570e6f533164f880cc8&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E4JG5L4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIEWNtEMaeZ4D%2FxfAwvJwEJyiW80sfp2LVRRGbYMFOeK%2FAiACeubTOU98AJeEAGfVrVw02zOwYAP6JsUypDv2jx3l7CqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr3SkMb%2FYJVHoFtqqKtwD0fjmiV9rl2wZe5DdOb38ZoWTCMDULm0wHvyopf9UrhKTD95G2pm3cdnxmrP1PO7Ma0Q9Z9PODXdqd7KoUbU%2B8BNhVfiQoaZgRtpcBMfuQlSiG29SwAGpjjrjZ4ZbNlNa8QKzJNdVWNvX3NBslkn4Un6qP3nNNbKec9F%2BPc6XtzhxBSwhhpuh3tUvGLjmZoSFjUlxMdz6I%2F1A6n2Ys67LF1PxubCImLq1I4RiBM%2BHoGZDs3kIlButZHoWfNqDcKHFdyIL%2FJdsZSdD7%2BSUDuGOhcyL8cnwd%2Bg%2B8tj8CYuS%2Fos1jIcp3aE40g45tPsq6PNDHDUDKSpGuW81G7ffdN5KTUPrecfpWG2aBG4E%2Ff5I%2FDp7LDdTwKlYPM1S5sdmUVfzLJeDb4UWDG%2BVb5C13NdSIMsZAHR%2B7p31bVSc8YXRYZb7nEx99vhJQDNqC3PZqxlDZ%2BO0rBnWMhW2vE2maaqSEwZvALGIR1OznULmG1vVDkNqZ%2BcNlZ31JRHSOdShI34%2BGOoXcJPOxeRXeXDwXn83pKiua%2FLzLKrEqr2vnQRZI6T1oDufgg3VGL1lyEGZ6LKTmQO3z%2BZ2m%2FvED1n6TxQzL%2By1ULtN3rKuUrx0hTL48JcwEul38JtXv%2FC0uWIwk76avQY6pgF%2F4N4lUKlLXC62IjImEqY3cOB%2FNz8ZEuyApF3166jgkaaGEGmvuwwy7KR04tLcr1m%2Bv11BRauTYeCEUXMSzFUmNNklO5AhxU8kWLZlcwedWlUK%2BZGXYzcC%2B60%2B7m1HatGMpQLcxzhatk2MGYzfNEizmKnbYwD%2Byn6nsGLljyVs%2B9Go%2FAI6K0cHE1VUAs%2B53mNRV2BQyuEANzFCkGEBBcjDz7RN9j99&X-Amz-Signature=5cf11809796c476193d85e4a927c48c416efcfb38637ca78fc35dc6021f5ba6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSAWKXOC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIGIJOUE0POluvF%2Fs6ebO%2BSxu9MSzzu2rOg0ZaEkmpzkXAiEAwAfX0au7aKLCRqaiP4jR92cSb1yEXsyGQliBnamQs6sqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJO%2FSxvOp%2F6w62fn%2BircAyL0XfugXVIVbayeq2Rb5zOutmRcxwu3X85kknyEwNXPfBfkaseqd2xm8VRI75LMhRU47Po6kcQkwG4fBICr54HbQddEd8jLfnISIP%2FXBc%2FAYvRw%2BapnOtsnIfTIvC0vpbjONN916I2gyRC8Kd8fnGZ6Y5G4qaaV2of5POBP3I2bzahzq%2BoWtskifp143%2FHRp1kzyBr5VCrPZ5rliZTKWjiYbCXOlSBSj5oh9m28OxHbCZxImJ8R3u%2Ftfo9HSEFfNhUZucTt3cxPn2C7Mk8ykffvSSaiwnnwaf9OdD1HbpvOCp%2BBnW%2FrsXtncMDXk4SuXg9Ww4xowDl6hoWCQUszVKjid38%2FZp4%2BXnfKF2wcAsYjg4YpZeNNytzmyjcdiXnYbXErVKN4dKiQSR36xoqmkD6p1x2zHEpgRoI6ogzLhC%2FIJ6c3B%2FoW5RINfK2gNDpaI0Sa7OFFrdnO6zoT%2FSwjn0Fs3jVirLFaZzfdLUCEadx8dYJ4AHgnJ2RP29hVm1LcDxj%2Bs87T%2BStXTzH%2BjQeBRFKXPqhrOWngMeWENncHutjkNTKZFoH6Ap%2FdpQhQgUDvCDSceEhsjmI4PeE9SZYGEl6%2FXDOOWL0hketUZBGaFZjvvRGiRuyQeabRJGyuMJO%2Bmr0GOqUBKmVQGG2GKE%2FusMy%2Fi4j4IVx0OBTir4G6UPsbOECVc9mERQSZMIQAoBELG6YwuG8JlCIKnhrm5sCMzHJp%2Fj8SiAqwH%2BePLa5zpHMWV8JXhE5zHnOuRhzxf1oLUBKQwG8DkACd2bdNYxodbgHtopQ4aK2uOwL34YMOVQsMvwLYqzUiC3BY0n6q6pv8G2bb2zZIH2TFTmhvtD%2FLXIk%2Bq5RBOj%2BiqQHp&X-Amz-Signature=c3946a6dc7fb7ed5b37b97c0fea9d5fea3e3195d8a5209429410b60d4ad47b9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UAQXJW6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJIMEYCIQDiIWTQZ%2Bd5bbE2Gs9Cuok%2FLmCbWmhCfqdRMWhLRUCJ3wIhAJTVBnw26DlRHCt7CaT5Z5xTb9IIW83W1gY25rHMcZoTKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwltKH71ZIBJFIEJM4q3AOEHbkb9Bo%2BWUSAjYUlmBQ4bHS%2BFbhUxafX%2F605zCV2q6QHhqVZh1MuPx0IH3JNxtPYBDAfBU3wwek1wtTXDYyozQ%2BsFWhqp7BKIN5NUibsWwrEb4qD8ukEhJGft%2BfuS0GzCeBTY%2FMiSsq7nGhkFEYzEBrC4s9hFFoBVZPel3HO1Lugs6wChuqS8zxenktSh%2B7SAWfs01HfDX65PcKBA1Agk7Yp3ybGJGXixjr52o7jNH%2F1OZQda4KliARENgSoj7ItUxspci0rx7fYVoTMToenQaFzqiNkPj8oYKPzKA5hXwmoTfxhKKJuYZ2Unximq0TdCJEFLRa7HJ2zXUDyXGofjbNLNW6yKwhu4j9%2FRXkHSNEvSYzHv8Zr5obX4kW2E9ZMkuWSc5lRINER1goNhIQI6yvHxmxyEFj4asbtM79A%2BgcYLrFPoIf7wbhN8e%2F8B3w9Zwh0OaL03SdVw805izOcEl2l5%2Fplr8Pgu%2FxSjD%2BPyWBa2A3wFH4YzAnGrPcEqQElhZig9%2FXLO6xzycLyPic6eSDy9jx4B%2B4XtG9ExkT%2Bb5HQX4I9Q6C9noMCa%2FqNaokGAWKyRTZLh%2FIR6xj2%2B%2FIgKLU5p%2Fs3yGkwkmeT%2Fmwem3quSFg4c2582mJGoTC5vpq9BjqkAeTo5SpGeB9T9Z%2BxtCocK5Y%2Fz%2Fz20kYR7pIoM3k%2BL8dOaYy%2Bnwb9k4t7dJ3GCHoj%2FOwuZB%2BjC0GhVhdxhBRiZqouUiGjeJsmWe%2Bd7sFUriFlcQjA3IyO52le1z2U9GQ1M%2FMdhXipsVbGkwQAQEiZNIc2AZd6fGkCpDGFap2JsADQrneL%2F32DhJ1p2%2BtShPIjiH5k7VsSdmJIjpUNHXbRx1jnWXX7&X-Amz-Signature=ddaea66dbc0dcb5a5b272095464ce1b4e8b93b57e3aee2e28634790c9cbff37b&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UAQXJW6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJIMEYCIQDiIWTQZ%2Bd5bbE2Gs9Cuok%2FLmCbWmhCfqdRMWhLRUCJ3wIhAJTVBnw26DlRHCt7CaT5Z5xTb9IIW83W1gY25rHMcZoTKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwltKH71ZIBJFIEJM4q3AOEHbkb9Bo%2BWUSAjYUlmBQ4bHS%2BFbhUxafX%2F605zCV2q6QHhqVZh1MuPx0IH3JNxtPYBDAfBU3wwek1wtTXDYyozQ%2BsFWhqp7BKIN5NUibsWwrEb4qD8ukEhJGft%2BfuS0GzCeBTY%2FMiSsq7nGhkFEYzEBrC4s9hFFoBVZPel3HO1Lugs6wChuqS8zxenktSh%2B7SAWfs01HfDX65PcKBA1Agk7Yp3ybGJGXixjr52o7jNH%2F1OZQda4KliARENgSoj7ItUxspci0rx7fYVoTMToenQaFzqiNkPj8oYKPzKA5hXwmoTfxhKKJuYZ2Unximq0TdCJEFLRa7HJ2zXUDyXGofjbNLNW6yKwhu4j9%2FRXkHSNEvSYzHv8Zr5obX4kW2E9ZMkuWSc5lRINER1goNhIQI6yvHxmxyEFj4asbtM79A%2BgcYLrFPoIf7wbhN8e%2F8B3w9Zwh0OaL03SdVw805izOcEl2l5%2Fplr8Pgu%2FxSjD%2BPyWBa2A3wFH4YzAnGrPcEqQElhZig9%2FXLO6xzycLyPic6eSDy9jx4B%2B4XtG9ExkT%2Bb5HQX4I9Q6C9noMCa%2FqNaokGAWKyRTZLh%2FIR6xj2%2B%2FIgKLU5p%2Fs3yGkwkmeT%2Fmwem3quSFg4c2582mJGoTC5vpq9BjqkAeTo5SpGeB9T9Z%2BxtCocK5Y%2Fz%2Fz20kYR7pIoM3k%2BL8dOaYy%2Bnwb9k4t7dJ3GCHoj%2FOwuZB%2BjC0GhVhdxhBRiZqouUiGjeJsmWe%2Bd7sFUriFlcQjA3IyO52le1z2U9GQ1M%2FMdhXipsVbGkwQAQEiZNIc2AZd6fGkCpDGFap2JsADQrneL%2F32DhJ1p2%2BtShPIjiH5k7VsSdmJIjpUNHXbRx1jnWXX7&X-Amz-Signature=9029e83ae0f61e345527987befd5a9c5728fb13b46281abc756435bda7af662f&X-Amz-SignedHeaders=host&x-id=GetObject)
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