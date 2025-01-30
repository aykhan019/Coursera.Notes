

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNWPOK7W%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBS%2BfEozc8tjwmrGV3t6SzsjP45eDfiaMKM223vjBVHwIgZo%2F8b1fJgcFitTRecrnXD8miQb8aDkKjOSk2owiRkUsqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNwTaHBGV3lIaDkPEyrcA0XPKF812oAG8a4ULlzJv5u7akhPdUjwoIatHxmnHMnlaMtSyrv2pT0reZfJEjZxhsyUgwv31znq8yihuZKTIoz8cmCmkd5mBPhBvYMhs2Gq7%2BS5lkKDDonYm7sUVcLvJ0PnzmXdl%2F0F497tADVg9tvqXtYixH%2FNvBYbK2Qpn2eqigGkd1dIn7BMz%2FUfBQ3%2FHbi6XZsk1HGn9lBxfy0%2BS4hAli9fNtV9yocENwusJGBKrJ7DpZM35nFeCpa4tJiDa3ZYLbxtkUn%2BTyljQvMFDZlIgEVwtRhNIENnSgjEx%2BPwBIzy7yk1%2FgGByhyYqQ6tqEImu7cuoRcHgwEelIOQHeDcwIcuTXXYsTQvh1zf3OapgUvFdBL4FoPdAAwvE953WlXAzirr00dPI5S7P%2F6YJ1mvlM8393gzwiLZmuGul6dt1kTrrYIM4RIOm4gMHi2KxxjjmrpKJ6oHtU9t60hpvVvHAJKFi%2FFJaYnA3jpql1TJxd9sIDf0NyHCMM%2BPxwauripGSBHAmRyb0fH8WJkrVJE%2Bbcdfg%2FgWF%2FX%2BFN4fUj2VZXS2R%2FxqrDWs2uktJqgPD80iBrznhum%2BfDEovJcs352EzkdDXJe4%2FTxRjIBD5KphXrrphCTOey%2BBu1N0MMTr7LwGOqUBU6Y6P7Hc1bf0s7It%2BeYAsWa%2BHn5TTkC%2Fyaq%2BLnlc%2FB5HgYrex%2FfW8qlcKjw9UjKTA4vlwwaouXiiav%2Bzf3h3%2BiBKrJ1I6ZwBunApOS4OtYrgsmmbCpw%2BmGCyrQxImMXE%2FDXZvB3kEwogoQL6ClpuGFTg1kRY4bkPkn8RIWG3eomUh%2BaTnuOXihuvyjKTPTaxfUBhXsqhPAitef7W%2FAtJpJly1DLE&X-Amz-Signature=d671cb3041afc2f37d751e5552269048248a0558a075a0a19c400e24e817e518&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XMC4AHG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOzXJxNEvuzT5d0qIFW1OGte%2FiKKuq30%2B6aBI%2BeZdWIQIhAOD0BXvmCtMkkGEsbqna8E8Wc1yTgF%2Br5iylrwuNvH75KogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw1hPPXGJChtckSoT8q3APaloa0AfHY4RGpDIQoYVoYpA9qReq3Czfzb0jbTy6ENkuVB%2FALv%2F3KxFzZ7C8CQnX5X82WOVbFOHNItSnI6ArWllBBV%2B3PGx9fzZfDjYDiu0vqDKzsRASu3Ya%2F3UpfRoup7YlKwDWZHvmgFhMqX7WxgxLl9N7TMF4ZsMpN4U0gMwkc9cffm0qDW19aCZcDAavcs7GadpKIxm4eZXfE5YaLFMvLCMCrRN4VNciTV63V3SI%2FzmR9%2FNmbQR65EFxBgIxcNVvaWN4e2fu8b%2FHneTizkPgHTMfOOUOyXtSfqXKJiIpx0uJXIGiP9tN%2BRKXeU1lcKB0qr7DW8R7Mm1PxfAji5r2x6nChnrHV56raKkcrgy4TRACgVrtYbmN3ZGYgsCcz6pRbF9vdGcbBbDPfSW6aSmKr%2BO2UlPOAusMDa7NKTwY%2BBXeKsNG3eZfrdWukDIqMY8HoQPl2DtE6IfdrOiyWpj4DBdKiKgmwgdBLCdZLfEtQq6l7Fqzcltr4ylmGTeRzXVE1rAaH9Bn68iPTymGF2dMnX3UZU5Zs0HCmz6YWCJ%2FdiI10wf68NyaxXUPLt7jtDPrnlnfyu6CtaFiXe5Xasqlew8iIBrg1NCqMzyHFmcuPpvJ5TPFlN37arzCC7Oy8BjqkAfkXFZtin3S3JHyWUQfeS327UIljfAt7kbVxUj3r0jbDh6X5S3evcTw3hSfFsNw0X88u2Q4UVUUGNVOsCLgGpa1%2BTZdmklK7yyatEV8qG6QgC%2FWOdljWWCtca8q0s6MH3hfKhSlGPNK8yIXdbGfkO8vstUMYpYOnJm33QJe7DbQ%2FSSzRiEU2rVGF%2BrouZBQdGr39EYDoYkog%2B88aVtr4kjqJgRdF&X-Amz-Signature=34510332938110d1ed3a32eb7a093b595b6dd37cd8c94f2d90526b81db885c6c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664S6NKKOA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAX1F0wwfpLXUGrtV0as1beHwkeGuHKFCi4PRXcAveZGAiEAoLXy84PrIiTEfv9ycOnzeEnyE1grTtuRXchRrsnLyu4qiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLlPA%2F%2B3AnRCmQwl1ircA5Lbb9anyohQb91fmy1%2Bs%2FuUn2cfGcz%2FSL3Jmh7p%2BODcmoWncZpycGrtpB83DoL0K4baZzHjjUCp23Coir69CFk5kJL64HXmwzum365LYCFU7rdMLp5YZqWHSfW4X3lOz9CAXARKbMor3p6gJw2lZmG%2FMjsPgpteUhKFajcx8qk7Q%2BfQN51b6itWQH7i0iEMqz7D%2B3kZdUz25kHZ2XIMY714uiWkY0UYDAmqCyUxpIdBVZES%2FQU%2BDSUdRDfxmgC8AoUv0ZnZ5ntx83Bg96IuujDQ3BH0naUU5cqttq3tnGcWEixzHJ1%2Bw3rQAxlboJVTLBhxQUd%2BLXhn%2Fy%2BbO6%2BaNyfotUoA7HFLHhEzAf64bTvVDkW%2F2pdu58rpB1l58GIDSyExIHzf2jzgezJF4HJ%2FcJyWIQfeOShxfwrEqxtE5fsW%2BCmFR0ypVce%2FkHN9hI2oHRAhGTuxCKXAKoCBW6GwBUA%2F4C8HLY9sUoYEzgoj0MjPPK%2F7yJ2euxmxYW15iIsjEUxHMFuYb5jrUIBvuz3YhJRjHjKJSFbUFVqYbv7AVcb8%2FsyjfyBPze85Mo6GxaitU5KSYekYqWsZo6F2Tk3q89RRVgmwjNMHKQ8YDyZbor6rjFzTcEOiE7EO4wgEMKnr7LwGOqUBzR6DUQDCSwBB6iCHEULKRQvJZz9a8DqpaJDRmZFwc5r3jiyf427m9dEy364sCNMuADvYszcooifs04TDs17YkJw13nkw8JLIww7pbP2qQSFs9PerSHM3YWoDaWy629zlVti%2FV4EvkKl9mFEeVjGU7VNN5El7j9DNa8PGR5GHaZSO%2Fyw5vHWtRu38zBXxy7I8POgxsUSpW8gDUfQl45XXiqIi%2FeIM&X-Amz-Signature=cdc4ffe7e5e52565d6ba91871b7b7f2933b0121c139ecb85501f9755d7ff55e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWC3BY25%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDeplSa13m1U6I5kB3uhhE%2F5K5j0YRk8w5A1jLmucJCwIgGv8LcIumxF929EQx6usxLHLk%2FxJhdNb0P%2FsDIQpRZRoqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBnvkdDjjIN9o%2Be9uCrcA68dR2NhkuSrUUlPL7ogORqLwc31FAw2XpmymygeyERam2PEMAa0QIgQc5fFzO5SkxgazfCAzeC9Wc49xm07s7uzy3W8nGgdcgmmo2W9GJIPWuVbQ3b6LmjD2omiK8%2FA8MVt4AEtCN34Vm4EA6gfdcvCVHXvo4B39ziC0Eb6fIq6RnVK3XaRQbvPzSOWUWS5U6Z2B2Uby2yaPk5liN8PLC%2BIX1QXtBzgvaDY6Mjh0uw7u2mCIEILSVT7Sn7HyhOqb9bDflvxG66XtLqCquSpaHDY0x04hpzvZv2zXt%2FVupoJcSmaVGwGBc9TDwgtco2dX57zYf07NGyvB0%2BbvrhFQkLpfvjMileuBxLYt0P4f8uSvxhQOWnklp%2BNi%2BFxO8IMK2oHln0TZcunWwBLI0mWkSmNxugF0ucD0jdVWgy1YXLw7IIfIb%2BXW0tpkmXscl3v2X%2B0OhXbO2GmYzcXpDMO%2Beo9X9bCeA6nauuswaN1%2FAjivuSF%2FT8WKM2kfcOmA9fJmuNGkFKbtc1CNe2SOXG3bmJ6%2BqZHojuTaWjt9b%2FxpeddZ7r2Ms3mw0joVDS2Y0w1XK%2BBceA7fYepWwarVnFTdMMlYAqxpx4dm11vBC7WqDEVG%2FQFlAZXRjwMllUzMIjr7LwGOqUBfJFZy4Irm7p9xxjSOs3vbPq5pj30MonUdCnR4SC21bas%2FVITQJGILJNvllLGCYo2bBo2H7FXTOn%2Fq2V9Hav7rx5a7AGuJoBUVAoFp%2FRn%2BvHtK%2Fm3bMZc2QRUToAP4GRluIcBKXGd%2F3BtKUPEief3BHpjE1YE6PctAGjuBC2M7X%2FIlDFKbHu0Ghj7ZJaGBcbIRBMKHdfGytpVFPyPXTOCY7TQQeGf&X-Amz-Signature=b217a7ef17507149a9bb1ce71f20ae2cd067385d4bf4002061bd694623f51851&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z46CTOLK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICGfcN82B77lFMWROCjlMPSIvhCA55OMDQJi0jEBoi2QAiAETBfKy5tbdq0OK2qHA9hfwz2VHS6xC46mCLPHSPwNVCqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXfDXCJFu4de0ofimKtwDTPgYQkxMO9P6nXbIigafzljP41hMzqMARY03ZDB7WMYfiXQCfXWrKp2CJOLcA36FELTtLJfgj63jOvHZKVnJxt37sNR9Ut3dE7SpdXrDajNVXsVPnG5OBNqDtu0BYEEK7bw%2FJUjahHy0czk1SMZEX%2BMZp5fo88JS1AsTZHNV4jXbW4LTwJbem%2FtB0lccg%2BSqDlqniazaoqTSJUG9dzU%2BhHQ%2F%2FVvhJMLBmPvHS6reu80SneB0330zomfIMN9wG5vnmWGECxmk0hExgIqLeJS3SVr1sTfHymeQGzp1jk3ZltMEuIdahV2CY%2BQIELc9FZ0j4JFTPQb3Not9X3nOkgnhnoPM%2FhYxSzrrTL%2Fqm3i%2Fl5uULfxTo1VzhLYn6k7O6AQyZb3OyxWHaCw%2B6mWjq%2BDExNYfhya6EQ%2B16%2FyB8DRmrSAvJp4Fz4zhIdRAjOUyyC6G6p4IU1Ahl0PJKQdQBIvMKF5%2BhsxcuFNaEx2JfaZ%2Bm2mpoDLF5z6edWEx0tq4HvhXDcQY7eCwhXV%2B9CJ5J8jgPzCxEtg16l6QMa9UAnMP6UnPSp6LYucH1qfXQeqywWRsf7Xl2tdiebLgHRyqlnUhkvaw5ydhatmR5DepskpUJlGIyUpf1IFBibVd4%2B0wt%2BvsvAY6pgFy%2Fcy3IypTqKlqX0h6UeL7fIjFpdNLdKonl%2FaxsAQ2sMYk35WaxzIRQbD4XrUbvIGyPEGOYVqFtpS32PSj1l8BUJhntFFk6DKCo71qbXJ5%2FxZTHigsA6pUbFEPNmj0f29al%2FkTSOoyBqJ7kGX7U6Zii1UhJpWhjFNeDDLwfgBzwsIonBDkorn6HYy4CI7ZRfaqKWVYkF2VYWDgMcU0GeP5pvH%2BdaFK&X-Amz-Signature=d4d2f2ec1a8d73f8e22775304e83c71e14038c03fa432d5e1a0551cda0ad77c4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PIQ376K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIFM%2BdmwCHSUf8u5SygDeeY0UHU3qGYkkOvl0zErikJIzAh8%2FCTO%2BFJkcC5vecjrZ16%2FyrYgjBDvBpq7pkyBHJGurKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBDf5GM2QXQ8y35vgq3AOWxQWZZTvoabsVtyNileVxo6Pkre9Et0ZdbXhlFcBrG%2BCAo7IU4DPLbAvCR%2BCHaNco%2FSmaIpvm%2Ft4pSQnx%2BT8B9gpFJsVgY2Th8Y2jasodcuJBYfkx4bCoZEsQBGSYKi5qP7%2FlUQVTj5TkltozGhm6u2RQ6soRH61jRRB%2B%2Bjd441oT%2F1ZeQXimIjje15iy50Vb6olZCNyxt7EFqB0OZVGz37DgngDffhwX%2B8wTJgS6EH%2BVTvnN5x%2Bk3ulOcwNv4DA6A650uV4c%2BwbhUynhq%2FPDuI8EokOlIxxuBuODZJVF76fumGZuVaR3oEoHqF5%2FGGbW%2FP%2B7nUKmryIt0T%2B5dTlufGbTZg0JW%2B0UmjM5zVJEfZ5waRZltdiseUyimxHDATQfemuYsFNah2BqTyMn0kz5Rk%2F6Oy0k9US18tAKmTsVHwcIn8EeRLmAAfClGRu3NpM7JBxU73mboraLdBFv6Z%2B40DYvELMYkCLjb%2Bn9SI8B3s7lK0WMQd3VNvbtvJPcBhJxR4sjKcYpXhDy1zV%2FbzyjPhj3E3lVoRNc7lCRs%2F%2BAbyge4Za5lOndyzoL%2Ftv6eC3iuH%2BirCTGGHsHq695jCstPaA5BE87YvwcE%2FOW1TMI0c99MmINK549OteeyTCY6%2By8BjqnAcR2KWmkGwVYZ7PJu2CxJ%2BvFEQcs0Ko0Xf8%2F9Gdek9myEojwsct3bhs0YDeL3ITZEckLfV0dCLBk4Sy58lp3Zq4ZggLeRMs17fDnPo8pLpfRPZYRLqFwu%2BIimeqX2a0MzF4ds42Tuv3r54Hk9q48frxsSlIxSW%2B%2F%2F8iVdyDHLeeM4kJ2%2FZ3g6AxefLqa5y72CHnn7ATuqalqviG2C%2BmfcwTODTeFspW0&X-Amz-Signature=e42e8b9601df8af3300d3c664089b23c3b94b812008cc424e7668c87fb4ad3ad&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7EYLIOY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDJnB3P6nBcj3qIAoRzXLkkd2okW3Ye%2BH2JXkfjR%2BkLJAiEAl9fNe4i8GNURrl9g2Q5haUQcM6hAisDQOLDGoRuUZ4IqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAnGtiKtuha8DMXFpyrcA9VPO01SpMwQ%2F7s9bhFrdIDYcUNuVD4faLb78lqmfwxEQZ0eCZmexK%2FYlXx8G%2FsGtNRwfS2pi7b88ajTKRABulkQnyxcP1hFK5pxDLIhHe1c1sa2Y49qS3KCEYgbnV6ACZfFbvgo%2FE7msK1ae9k44uXfbgn8u5q5KFNocS2zd7y8BOYlcym8GGhjfugsMs9dMbjb1WkMa7U0vc057ITi4Qt3vRSM5s2gF0goQK9V2zN0uVvPp4xvY5yFWT3uJQgQyagREp%2Br%2FwCmaKF%2FBivsoiMxn0GmJd6ICvvW%2FTOYcFVh87KofxtFyq%2F%2FwGNvm7zCfigCn0g2symgvmDGsBcoUX%2Ft2eNXlwGmfok8pMZTTM0zSLqJdebkNpsMWspGeIHuWQHYUhOaFXjmpTf8tXI3FlKXgXXknZgJiWSDeeYqmO9b31jAeainBqLKp5gSolpt1mlfKVHAzizkmqYg0n4UNsim0mf0AEkyeBiQhymbejosCAUIwXi1Mjk%2FJEzMrzQH8TVdoPZGTN6rCxRmLejDdHkx%2FP6b30QtEMlTYSYngpnW0dmLdb4hHYTfLX3ZxluWBe2wJjEqkgreSNnWLgnv2I%2BNYkhuI7LDXLRxlvkRumuVWRKQPU7Wt2x%2FWE6ZMPfr7LwGOqUBhBvrgUGWJiux6h6JzqFULHl8XuasIWJeI5jguUEpNNjdT0LBGmGnPOAfhzY5al2bWGagxPNKdhjKpQ2UtrC41w0yIxMe8AsWW2ZH71lUBobOX3a2pbZ0BnZUjNeB34caFJ3r8cLfa79fkuJI4IfXwtL0T1WCgxzznrKKsZndddYrMyIcZOpHIY6MUdOTnIAMP6EUmTN0Y9Ctnn1XHvd%2BGpg%2B6Epl&X-Amz-Signature=9c64cdc97b326cea843b2a16080864fb594481c1538f20428243265150644b6a&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OCRGS2G%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDs2hvXsaK2ixnBVwPXn0lK5HXxQVI51tef5NdqLyHIkAIhAKh2VoOkyGmi1MrPNQ90QfcJD5%2F07zj%2BHZUrqpn9T%2BOUKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhWsAEa4Jt1%2BgcolEq3AMrWajJ4YMbiZXa9VZ%2FL5Q%2FiKvFl9JWsDVviS2HGa0eaS2uU0TpNaVYV1EMhlKL811B5BgF53DYLwuqGlMEr8Mv4VaGcCozHsO8Koa5vQ37tAIb5oZiV97w4lbftpv6tV%2FDdUn6TwXj3a0K%2B9ou49u6B9QB0I61eysqGJkLKujMntr1zvR2An%2BSKWPCcK2jQW8qZgdmgYzMipJ%2BNznnGDZfVXNfatUIeputL38%2FZvJzi%2FOrufCEQmmlu0aAxg%2FFhT1Ogd7s7f9z24jRXsqsvnMy5QgRWqHcMeKa20lBTc1UfiXqWQsh1ugrQ3V0xwCJoFVJdGJ7j3uALs3LcF7qrxKAyPONyJMEqY8Krpa9ssFKh5MMSLc2L4MP%2FVxOSBxYPdYFLJmfSsz9ibHf0g5CBUyz9viFtaNf05P4V13Loh28e20AtpN5Yw%2BVUNo06h4tPEZK0n8A1rBqHSeh8nbpMEuZtTqME1dfolpdlPAoRHdLOhEuTFaA8%2FK1cuv6JddQjR8uuafaEKXlZC9xqpG7quoEWJkVyLkZ6u8ahJSW2o2zwyGy9rkNc80AtYqBt0YTL0A7qIPYN4qhzFeWsqd8cK6sqxdVNPWlpSSrSXknmtVM3wPzz%2Bo7IChjMzEoqzCL7Oy8BjqkAQz1rJytd5uay0kSYfQSfxRyfbzpgZo0J5VlgMCpzvklf%2BZxOAbs%2FcXkmFo4t7mU4dOdD3Ap1mDtk0uSVCwWviaq2OKkJ0yBqOjzCzfkPHiJUD%2F5t1ZMoAgLAa9YFGayT6NHaF0teYmtp3pSn6lTDUX5lY7DsX6FG9FjIuHu2Vo61n9DX5P%2BmrooBM5JAQ8AKg1qAQ32k7p%2FTtsbF6tqwbz4EXiF&X-Amz-Signature=e2675c8334630181d730ba4584bbd81833db6e6256970ab6cdac1bc5256811c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z46CTOLK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICGfcN82B77lFMWROCjlMPSIvhCA55OMDQJi0jEBoi2QAiAETBfKy5tbdq0OK2qHA9hfwz2VHS6xC46mCLPHSPwNVCqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXfDXCJFu4de0ofimKtwDTPgYQkxMO9P6nXbIigafzljP41hMzqMARY03ZDB7WMYfiXQCfXWrKp2CJOLcA36FELTtLJfgj63jOvHZKVnJxt37sNR9Ut3dE7SpdXrDajNVXsVPnG5OBNqDtu0BYEEK7bw%2FJUjahHy0czk1SMZEX%2BMZp5fo88JS1AsTZHNV4jXbW4LTwJbem%2FtB0lccg%2BSqDlqniazaoqTSJUG9dzU%2BhHQ%2F%2FVvhJMLBmPvHS6reu80SneB0330zomfIMN9wG5vnmWGECxmk0hExgIqLeJS3SVr1sTfHymeQGzp1jk3ZltMEuIdahV2CY%2BQIELc9FZ0j4JFTPQb3Not9X3nOkgnhnoPM%2FhYxSzrrTL%2Fqm3i%2Fl5uULfxTo1VzhLYn6k7O6AQyZb3OyxWHaCw%2B6mWjq%2BDExNYfhya6EQ%2B16%2FyB8DRmrSAvJp4Fz4zhIdRAjOUyyC6G6p4IU1Ahl0PJKQdQBIvMKF5%2BhsxcuFNaEx2JfaZ%2Bm2mpoDLF5z6edWEx0tq4HvhXDcQY7eCwhXV%2B9CJ5J8jgPzCxEtg16l6QMa9UAnMP6UnPSp6LYucH1qfXQeqywWRsf7Xl2tdiebLgHRyqlnUhkvaw5ydhatmR5DepskpUJlGIyUpf1IFBibVd4%2B0wt%2BvsvAY6pgFy%2Fcy3IypTqKlqX0h6UeL7fIjFpdNLdKonl%2FaxsAQ2sMYk35WaxzIRQbD4XrUbvIGyPEGOYVqFtpS32PSj1l8BUJhntFFk6DKCo71qbXJ5%2FxZTHigsA6pUbFEPNmj0f29al%2FkTSOoyBqJ7kGX7U6Zii1UhJpWhjFNeDDLwfgBzwsIonBDkorn6HYy4CI7ZRfaqKWVYkF2VYWDgMcU0GeP5pvH%2BdaFK&X-Amz-Signature=b75d00cb02752c050bbd49ee6a680cecb383ff33620d9ed645d2c2fec3bf1856&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVXYPNH4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgoARpqlEXL2R%2FcViINDMxjmg6ZjTDL1auUUxnPYhMjwIhAJWnMZPVxzH7FWJOd7evAoEp0w%2B%2Fe%2FyGxq9XY9WMKzu1KogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZE3%2BJXqiV1%2BrLIFIq3AMue3SXNwFQMm30jdo0S9fszChovNTmS4DwJyFd6evh%2BiLz8lAzY5uFXG8ep7z4xz5ucWIS3WsMmHmimmb3uD6UkJj%2BqOp55alil1aLi7pOgBlhBLZTsEI6Pq2oG21YO0me7XKJORKjTnHSt6ge2kls836sOy37d5iOW%2FkRCsFn%2B%2Fbg1VG35fGzcX7FSaFvQrKTw%2FxRlKC87NMC7dMZOUa7kCesmgRmAY%2BAOOVPaEZHY8L95mshmm242%2FND3qCYrmRSQKhJU%2F0pEex04O6j7KWeHUIGAAhLvlWwZujJ0%2BoF8bapA9rhrw3gVkKUj8FsUORbUmUDFFeMsW0iHPygLcIlp%2BZvOIN2A0Rp4vkFc5bm6m2TyaBP3%2BFUaz0LACuyZ8FTufRi0VbSWvhfABDr15jaPBHyDSzP9Dxez1Rk%2B1czurnHViKnxHt3kI2AB5lIkt9wfCEKVnaaPEi7P34D6%2BkBglzRjG6EupZYX7vmo1f0QZB6cfBR1DA7Wb%2BwVX7aRd9rwKserwYrBP6M0ZT2QH9EfaMAp7w%2FykY3sCGrLp%2Fwxo31HyDYJGPdICOO%2BSS2foWxqPhH4ftAYgZEKCK4sg70KSiKIOnQhORQUVdoNWJuM3amdaknMOGKqTzOPjCG6%2By8BjqkAUYimes9jMvI3uEBu5%2BBpwraDjhziqsN39UIbcNxIXXQOt3m4nwcFLUbQ4F42j78jM2fOyB9YxNSOVs4Qok9YgJGfi4tfzJ1lRTZzs2EthSrijH7vN9MX6wTq98x6wvrJ8WBogsvcy0JbNMCmQhVH95CQudsURcq2kEklDDUX8lt3fLZ4J%2FYX%2By%2BjYHC64XZMNGcp1svihLZDLQccvZOLUGDV6VP&X-Amz-Signature=3b1b472f340945d115281f95fd9b37286c6173d82d60762154bd15d4ce07f259&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVXYPNH4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgoARpqlEXL2R%2FcViINDMxjmg6ZjTDL1auUUxnPYhMjwIhAJWnMZPVxzH7FWJOd7evAoEp0w%2B%2Fe%2FyGxq9XY9WMKzu1KogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZE3%2BJXqiV1%2BrLIFIq3AMue3SXNwFQMm30jdo0S9fszChovNTmS4DwJyFd6evh%2BiLz8lAzY5uFXG8ep7z4xz5ucWIS3WsMmHmimmb3uD6UkJj%2BqOp55alil1aLi7pOgBlhBLZTsEI6Pq2oG21YO0me7XKJORKjTnHSt6ge2kls836sOy37d5iOW%2FkRCsFn%2B%2Fbg1VG35fGzcX7FSaFvQrKTw%2FxRlKC87NMC7dMZOUa7kCesmgRmAY%2BAOOVPaEZHY8L95mshmm242%2FND3qCYrmRSQKhJU%2F0pEex04O6j7KWeHUIGAAhLvlWwZujJ0%2BoF8bapA9rhrw3gVkKUj8FsUORbUmUDFFeMsW0iHPygLcIlp%2BZvOIN2A0Rp4vkFc5bm6m2TyaBP3%2BFUaz0LACuyZ8FTufRi0VbSWvhfABDr15jaPBHyDSzP9Dxez1Rk%2B1czurnHViKnxHt3kI2AB5lIkt9wfCEKVnaaPEi7P34D6%2BkBglzRjG6EupZYX7vmo1f0QZB6cfBR1DA7Wb%2BwVX7aRd9rwKserwYrBP6M0ZT2QH9EfaMAp7w%2FykY3sCGrLp%2Fwxo31HyDYJGPdICOO%2BSS2foWxqPhH4ftAYgZEKCK4sg70KSiKIOnQhORQUVdoNWJuM3amdaknMOGKqTzOPjCG6%2By8BjqkAUYimes9jMvI3uEBu5%2BBpwraDjhziqsN39UIbcNxIXXQOt3m4nwcFLUbQ4F42j78jM2fOyB9YxNSOVs4Qok9YgJGfi4tfzJ1lRTZzs2EthSrijH7vN9MX6wTq98x6wvrJ8WBogsvcy0JbNMCmQhVH95CQudsURcq2kEklDDUX8lt3fLZ4J%2FYX%2By%2BjYHC64XZMNGcp1svihLZDLQccvZOLUGDV6VP&X-Amz-Signature=c0c69acf459c84e6284e44d5628d4fbc710ac6ef637c7569d318e1c62ebc2bcd&X-Amz-SignedHeaders=host&x-id=GetObject)
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