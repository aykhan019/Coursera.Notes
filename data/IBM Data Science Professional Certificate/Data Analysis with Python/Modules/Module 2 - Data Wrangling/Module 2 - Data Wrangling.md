

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FFBTRI7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCGke7Ec8ACrz%2FxYXAsZMGfUqsVa%2Fp4SjNsI8RLbq1wQwIgWETuKfGOGLEoJUQ4sJI1kWnksiBA4kJSz%2FaSLrGUZ%2Bwq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDDv5Awm%2FqXoyFLysESrcA51f%2BtxKGnuMQ9WQZtAX0ZDenzY8KagWsxYkPmokQJDoy%2BUuP%2BWeigdCK3T8p1puKRpPWzYeLRhXupypAzoB1T6Q59rAH5DkgG2OWeku3tjuadx%2B7XOWLBB5frpS1RGfYxpou5OOZ%2FocjwKnAu%2B%2B%2F%2FEU%2BBhJ4BeVkhcjHdsmQaSW2J5gAiFlrrAACVYdfZZUkPbwQ6VHNRNcdC%2FKQff6wM1iOfO7vzfikJK1wHVaNU3ppuEFv%2BhH8946ezTqKqzQSPc6G4TVRVjrVpRV0pWZ%2BwZDmophngPXgW5vwbft3sKstFadtFLEwGUAu9wgqPnwi2f2KWoqQVM7VFqwBWAcGsLWFmHuAvbaGmrlQTFpQERr3mpOuqNIG5P1drBmQVKWeesN1dRD20U2wx0L4U1DCI%2BndSb9i2nAenXHUlN%2BRE%2BKHpJDDGZTr1GC%2BPUQtLFVCfK4UhGDvqGoWzFp4d%2Bvt5tXpSwxJUt1nQ0DNIzkC7UlK0btmikZQ1u2xM%2FPl%2FvmNICkS8aaNbWPoVbRiLBpCA50fyAw289hFnevxJMuDz12%2F03NhoVgzj38ewVTQ8LqHQVDMMicByO6dHKVJ058y44o5dWuYTHL7xKsKnYmB9wiRpthVvarHvGsD7AkMIL6lr0GOqUBxzdlNzp3pNmDFtcwapXWAaPuiXW5mpANb1pxQsGGZ06xDnt0UARM1y%2FrMnIm3uZ9X0hIE1ffZ8tvZ%2FpWu0uwNcLwTgNs%2F8fY2jLipC3iQW8sY0Rodz1%2B6F7d4nTocmffpMpql6%2BD3s16vyefOjt03XuX1AaZ1aew54GrcTr9KWC8rtS1XWqSGfzYQEybPR9Ja4dwUXXGzfDh8QeKfG1fU3RcsnZ7&X-Amz-Signature=e3fdf913ba0f4c217a33f3bd33002a8a4d75f2a08589297d67c9af88797ed0a7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXUXMP2O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCpVf8wMl0OKrOelJVXITf7Z6QF49B5lb3QezCgPpTlagIhAKsyaBFquXGz8ugs7kZOhWkJCV0vxmUPNGKFabe77AE9Kv8DCHEQABoMNjM3NDIzMTgzODA1Igx6R8CIfIFn7eo%2Bwe8q3AMCxvlh3K0scWPuJ9sGbUgfsKBmIKjxUDNy34pbYKlv8ZJ6bOPhQa4tZRGQ4EDfpp0JDRZhWNv2axyrRymrQZ6I1ssHUvDPMrl3l3Iptaxg%2FhuB%2FIgPuns3DtmFKpYmDXBNEjHwqjf4DaspNUbJnKfumDbORkxraQQqcITeWt0Egy1o%2BmjIUe8DRz9vFm9879J37DF1Wr72fEqW%2Fr5CKj7MHTlk6104TB99hePQmGpdO7Wtn8k9KVulkuhFBCH6KPHSJG1wJNOZ82Kd5FoZJDIyNJsQ04ZwX7ypYWyUqCASf0c%2BQWI5PyhLjH3T9Qtcowx5pdAQ32uzqc7rKChNMzcaXHmrIvFTbM0G3GGDGfvlMaib5m0bbyVmVKe%2BXHCgOVxGW56%2FOtjf5S8sT6IJP8IKZev8G00SHRbWngfZjbbcZ1cAnIpJ1Y5y5GBdYhGVst7Q8xBDK3G6GVBWyu7vyCDHaNL6AqFxGBKoZSSqSuE9F%2FAA3s5FgvyJINW7jbElnY%2BMksELSnws%2BJ5h7inUX%2FvWj7oj898ta5tJZaaFsePBenOXB9%2BxopirX4TFKSu4f3avI11zFBrjp5S%2B4QZ2ZDhHAYgHq7taEUwTwyKaOLCFU7Dpgysf1IQpu3kS0zC5%2BZa9BjqkAdYZhnghO5o0CE5rPkdh5YFD9FdesjnbjW%2Fr5%2BLvf2bbDCTJbqaHHcw9oEs8uWXFdzeJIBknVExoki6SySQ1SrRyIqdf9DHF1TPexIYWXUa8tw%2BlRJ7sokPIaJU8yh8KMp9K%2FaFN9oUnZBqjB6E9Km%2FP0tNyp7BsJUdIcXdO%2FfeyyB6hTZynUTe2GPnGPvLiLu11xSWsK4ZRR7K2QcXM%2Fj9bcM7G&X-Amz-Signature=e2850a9a588b14afdffa4d9d116bea97f2589d68a26817ca48766b6c79abfb7d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5GEA3PL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCHpFmNYmfuE9ofberOxiPnB9XqqOF8aCMPAvTD%2FYVy4QIgCztabi2ay1qWG49hCI38SGNMk7hmPPNtwcpPC0XVCgIq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDKszb9RiMA4lbclBaircA45jNGzzffqyIuqnDES9pxVbB025qHOitLVR72jqqoaLogRs6Lw4YfX0PggMtLagl2WVbgk07EBC1BA27yFJ5Ihfvo2N43g%2FNm8jKhN8xAHgRUBgjVBKAH%2Fwlr5m27NdDH2q6sxzWmPamUQBDqCPXApmDNYiqEKOav3Q%2BM%2F9L3k6relSRC5mlSN7k2Fv79r8sx41UyYMeTgUb1wBwq47qF6pkpf0vWIRrBWycKDqVC%2BDFXtLHNDtp1qxBG2ntfCL6tS6Q2zqcicNoPmmjHd2AalbOeNXfInFSmhMLhoqfNednnMDW9douaB8ZIdr%2F0j2DmYT6xTuiPnjO0m1A7QynS775IHAZoMAecCFKwV4L43a1h670Eush5sgzRZK8dRWWQBy%2BFLd3Is7nS4O4JLz%2BWRyW8%2BtLlpBYPHwaTKokFarNDwLraQH9in77sHiNfcsV1aT%2FHgN8h9%2B9KmgQ35Dd%2FT%2FS87QNHA3VspJ2C6Yh6kSyRYKYNhRynqQg73LHrwUPjZAOCduKRxuA4ye6hLGSD6dYB%2B9J248mfnv06Us0xLd53J0rLELknkRJj7U%2FgaQRANE1SYnKJEXRl66MfQG%2BfN8uIZp0jWIOrC8icGRo1AOf8%2FoCm%2FFNk%2B0eGvMMPf5lr0GOqUBKB2sTjR56mEvJNZeTbvrIJ8mLF4%2BLx1DzMQfGjYjTFZao0cfc9FOi%2B2ZMVIL1ylatdiXuu4W3qPieCXNG%2BHtHGZbuk6bsEqj3IG3FGIIH7iaoc4PThohftRWCL4n3FkSF7YoqJlXr8lO98UP6dwOaAG%2BpK%2BSrianmR9whb3hzzwf4ghlqoAF5FFWC0sVcH7X%2F63UtuerRXPOSIEVuU8Qzgq7nTOw&X-Amz-Signature=92940df07fbbbaacef47248385d243f80d3492325a5589e92820b9e47c9d6386&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLFHWTIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDWmOseN%2BNhnzf9mlvCzBrkGptdNLU5r89reJ0n%2Bm7IegIgeXAyMJ7KBQgWqOpmntzkA%2FLsL8eDssZnpcmHPZHXJLUq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDAB0%2FXb%2BVfEEstxd%2BSrcA06dohy0JB8x40cc9RPGq%2F6GAIFxW%2BWVCCZfUC4kZtixSaXliU%2B7iZ%2B6m86HW0uWiFoW37N8p8DJjPP%2BWbCGmWg6t32Tq%2BvE3udrL6zF6QLds3ZN1Bo2phSVmks2jZZQC%2FCbl2iySwFoVq0WiznhiWHW11YqzlmiAMHSwRBPcYbAAQry038mJpRlu3rKKi2cKUD%2FAAG8rdb7G0BAek9CM4gb9SMouQZbK%2BtZPzO9fLf08xCEZZf9SsWMUpft39xLZlo3ZRasQV9KamZ9npRRKcm4laGtUsU47rgBPzLzcVGIC5Zr7fBj94NChDTesVZIpYUb5BOFMdMnPGACOtOCINX70u4NnoO7aIOMHH8zuXi9Uh5Iafom5%2B8YYcAE8p0Mh%2BLkKriTxg%2FmkqO8dqCWSzIa%2F747NFnec%2BNRwAOu5fD0VUD0ZFty2bvDZgHQ%2BFl1BzYhCbBfCyWFJO5s3pNarOw5jDMLuIfAKOqlTDhF9I8Opp6kykq2DGfzn1q0WciPz9O8SX7GP%2BJ4IA8AAZu8Wn%2FivZCmlr5zolTZUZzgBXaIgXColRht7jBVlYWdaY7IMNKQabB9vJtO8%2FnLnAYA4bD6kmJy6DuZsn4pLkGta3TS3%2B4CEJqNfYs0g4f9MPj5lr0GOqUBd8zQ7qusmEvHyXe5EH9BTR%2Fry3ZSUma8aR5aubYLdycSAJakePgvPygv8QRYwYrEjnY%2FoNNaTmg0vcrKj2mi7phxANf0K8N2lF8hGu5wj7jyAvgi7hLorFtXTZT9CGSNaSA7nkkDQaJVgRroXtYEVeV48etoauazU5i1T3y7GOqIwDYn04X9jAlrcvCH%2FteE6BTGwIlyfvclrxMpPaZeVolYFMIH&X-Amz-Signature=2933411ac58067acf0b8c29716eb10ac94fc7665ae751738db58a6d286baee70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNLXTXIW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDRD9R53wx2nGgrA2NM3vfckLC3QwPPGIw24yT%2Fg%2FMIcQIgcDNwtvqtjus4p8i9rfIK%2Fl6ptRTaO3yvGHuT5DadAo0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDMNPagXRg5NtCLce0CrcA7EheIDmj4Ekw%2Fp%2B0Jq7GafUEoVTHm%2FLL3j%2FzpEoKDeuuhMDw8JMVeWPWJYRlbgRcNByXY5xkV7BPSGBl2qUhtAHWy941Gwwcuja6bwPkmdkpnViFLjhhyczHHgNl8FCi8ZUkrUrSwPpH6g49ZcT2GI9iICwuf0rY1QXC%2BumBE%2BzuSEN79NnQYBAfi4CZtwpGgK3y801KqEqp5eJwlAAk4p4MhM2SsdQIT3hnFXBNAuHsJoBbxf9veYuxVJckeGvGItVHvhuAkytG251NAHXerrGwHlmkgdctsCVOtOAtwFlN%2FG6FBmPNsF7%2BJZuYwSLe%2BLOBG3Ll3vaozaZoNfpQ98FvCnyWzcVKB4TW8mjy6j89No09MARBp%2BtbGaiO4ea%2BC3vf7kVbgYaLg6hiZftAOrd28lvYh1L9qCmGwOEJ4pKnv3XOPc7VzJpTafbCN7xDFqq6Eqw8LkJ%2BCbuq%2B%2FdWREviJJPKQ9EcJXW0hrMkL6xK92ate4T4c%2BZ%2F0UVtLlaKXBSAUDdNzreaDV%2FFhFClMCSUBbVMocUqvTZ5nN0YArq2ThMpKclfRY6a4QPl2LNZe99x%2FAOqCPbcSY4EhXVM1%2BuBae6tlXTLzolgKCZNYGANDDhOySxau0i6MjtMOD5lr0GOqUByQRirrC59e0z9e1ehBcfRC2%2B3LqDUfWs5VlNzncJrOYpoCYDSPs4xz%2F9ooWW6gZaN8vZNHHA0%2BJec16vlmeWKcGghtl1mDkoMLiKdvjma4RUXupSFZeqKBvfo812J6QleuL2UrEGYaSfTOT%2F80%2FDCJrkpz1XSP9cEXBRbYk7IEQiDEsJENiUWRGI7E5YhlaG0rOVUyJW96598JFDnGwBfuNmvUJY&X-Amz-Signature=0f847e876e9790a52d3d041cf3a5c877769064c5375a33300de32e1269c8987b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WD6FQTRX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDfzNzVzuJavlddtUYNnxI4Vtkl3YaVQCOuP0Pd5s19UAIgcttReQ9R6gFi%2B0oxx4sw7PUKe%2BZskhoToNNdfDH%2B26Aq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDK3x4VcJcjBmT99brircA7KNpfRRi0y9Wt8kEq6ge00SNA20B053suGkZmwVEQpoWvek9tCQu0qfI0WU9mdNEBjd0Q%2FUWEimwy7mFWPVIa0nV0mpM3033rB1P12ais8otTNrxSiWuFBgoX1E7jxP6NZ7HT2rkFCZN5ZFoSdZJPnlpV6diCXdmmZlNSd77qxDQmmM3BXghJpVNKJtCv7KUQf6yas0G%2FGpclL4QxztCs9%2FS5eHuDWdiNYuNBAV9hA%2BJqf94BRGOAt1rtoJHf2WtQP1WlM9QtBNXFbdnxYEw7fji9r%2BFyuYcaDHLnN2aHwkppH4sO4Jy8EACwySfwFtqWl0wDwDTYCzt1yDBP37vhQsNk0sCluCmYHnOaEZZutkLIb0poEf%2FkHS2u2mEDyI8NHFtheuyqWUJWKyfKeWfLW7FkFT3ABjkaMraEqN9IlvaG%2Frw9CSDQHI3Ac84g07CMTWQSnKOr%2Bx9d2SHhSmBjRbB6%2BGHsKOW7Q%2FjGKzfUZtpyRPJSmQpLOF85ke1VU1AMvVMbrbz4uulwo7LEUsMUAFhcnjFwZ2GGqwS9enhHkCnpaJYKmG%2BjcTwCfBJcF73Nhj3oToljb9CPRVbD%2FWZPgKhrePsYxNrARnX4P7PNpOJdYRmLAPvSBgZphjMIP7lr0GOqUBBiBBmEyYJCCpcozSIS40J0NN%2BfYEOrSIuxUlXmB7O3lQdh0GjBAoSMKcf9H2XjtjKKH0LHZoR2lPaHi47XfeZdmQ14Z%2FLSu%2B85bOh%2BsEecQmoQPJUYsSUKa1Yi37WdL57VCm7Fvjzjo6EdWregprZmpVqQAaRg210UfyVZk8hfIfIo0z%2BmgIz5eEjPjSleTwBV2ur%2BNgssX1Cl%2F%2B%2BrGwzFSs58a%2B&X-Amz-Signature=4dea7ba132efcbe0980afad68184209dcfeddf95776e2118522dc7719bd587cd&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U5NLIV5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIHkAdOd7%2FsW84FEpfBdjwQbHCS8NR1hCqNWlt4SowDg3AiEA7DDfdHpftPnWixHqrB5oOG29OL0Sp3qk35FA6JchtNgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDB3wj9S5eyGS1FQ3QircA50P8DwVkAiY5Kj%2ByJO1b8hnBQAfbXxKD1HyVskc3MWwGJZk3xe%2FDaLaLZivP5yQRIi8wpn4shcjSzZa7m20wz8cUrFiI1saKcbSY0JtA0kVcYRAnmrL%2FyFvRqpoxmy3oXncAjwCBhAEw710GY%2BL1qF9xzEauW%2FhV46sYMMVS8x3YMlCqqILKEGGCkfRO9nY4WjrR85AYw4AJWC46juJScS8XGrNUmpp7PUb0WiBABf1vyBJYelZ5ns03J4UTq5xwFtmHOy59h7FTNHe%2FZMxJcSNkaIMZmmbeIGnCw4vE%2B%2BSTNO4cnkCVQ695nhrCN5ilhXbfbw9vK%2Bd7zg9cfaZboA%2BGtAD7%2FHqqPtufjkAPQQJV8jPdz1%2BYHc2AGw91wsiJAJrtCzJmr6fK6v%2FhYAo2LRgWepOF16NwuAGlsOXyfHX0jXHjYXQMFpEkUPhqu8oPuAHPtvQujQSAVJ2eGfjcFVxhNjdqdwkw3njYo9ml4GB3pRt0LPqizBBfdc3IErIWsE%2B6xfSbPI9SbQn63hchEpQtp%2Bj%2BflaOD7kkI%2FlfmdevghLzsBJEbHwgBLzO4vPGuvlCagy416HsL4HanfFsMm9I3JqzSsNR2OZPKEYWKTlrhqZwAvf1p6gWJHwMKb7lr0GOqUBbSB0ggdUAEW1eYJDpKOZeZaUxkirRu637BVZBBmQMG%2FM8fswbvupU0L67Rm%2BsWUMokuoNH%2FodzRjnFQHWwN5MHHxV8Gv%2BKMFAb5gNz9nBX%2Ba%2B3PvILBV79AfKUBjgFY5yDg%2FeA629ACosSXuJ0GemVoX9cPznfBP2X8wrFxyOEkN2hjaRbCcOjtBwNo4copiQnnYM6k%2FpVg0c%2Fmg0s2tsykqS%2Fzf&X-Amz-Signature=66c5952ca88f270c2835f72ed574e247fe9eed73b8e3ed0cedee284073bcba02&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TDV63FT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQC7oV6qnb%2BkbIyWkK1B%2BreWLjbt5pY40hJCvJdsaPEgFgIhAOaR5bGrPROIvi%2B7SC0dhnLNZlV9ZRSnG6G%2BCohKWX6dKv8DCHEQABoMNjM3NDIzMTgzODA1IgzC2qb0McmgmNghX2wq3AOw9AJ9326qJaypXa4bewK764KJrkfxzrj8qXra%2Br%2F9fyCPF36WIsD4vMRk9FpVrDXvtz9HL7NR0rQQFvzlW91uQAXqt4BSkWhzzpenTcR1hlr23frMTF%2BO0IijOXtrmvBwjyaB1z0L5EHiyDwNK8Pc19yNCgvHUlASYc0YaWsVmMUiOvnKR6EH5chtuxCu5QiXAPcrVYze3c6JSiHDdZcljihTFRfzSKiMblZjMWrAzu2mKRFrNevAfOXEU9lKjlcZmbOg04IYAKJWhHUij1rITDwCOxZVy04A203xdWlnkefatL5R2aGh8Mf1TGzyMkVl3893MvkszSU2UHtEoRy%2B1as87Mqdh538h%2BRAEd4Av%2BAAwzdeb7MNZnEI%2BnnP79LP7OVCufgcbewXFPrlXNP2oMNxQdkZpwdok9VQ5uJDagKZWKKdPJTMYC2zOsg1oTWI3mQa7w2NNUp%2BSFbJjeZEupukP37G9qlGLNBqmqVunOiCi1n%2BKhl7blxRoTDiV3SAspw8wQGGAexgJVheTzX2p7%2B8%2Fe1E96f7wIgs6B9wCbGlsh7N560V%2BjFAh2vqZO5JWm0hezcsdRTL56aQjExszJyYc1xMWIknC8VPz63QU%2FE325JmpKmeUv%2ByETC5%2BZa9BjqkAYDZJHENloqkFhNE%2FTAbPvDtVvZs8U62QoOKSMdW0lpBDSuXgFRtAcYO%2Fc7uOPTU4cnsjfgPQUFkT093wb4Pqg8ges6pOePx1BRZ9C0lUrS4GGU0B0GPdkYldcVTwQe15cC3QZOMw9nau5SsgDVOPKPil5Sk8zzQN%2FZjUg9AFxEsUyQ3h3xHohGWt3WXY0QEu829X8AQB6evK3gcZ%2BaWCF5Y4wUT&X-Amz-Signature=50c94395a219bfa6ca73b72accbe713c53e1957e596052a834f59d1b8b7a4b6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNLXTXIW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDRD9R53wx2nGgrA2NM3vfckLC3QwPPGIw24yT%2Fg%2FMIcQIgcDNwtvqtjus4p8i9rfIK%2Fl6ptRTaO3yvGHuT5DadAo0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDMNPagXRg5NtCLce0CrcA7EheIDmj4Ekw%2Fp%2B0Jq7GafUEoVTHm%2FLL3j%2FzpEoKDeuuhMDw8JMVeWPWJYRlbgRcNByXY5xkV7BPSGBl2qUhtAHWy941Gwwcuja6bwPkmdkpnViFLjhhyczHHgNl8FCi8ZUkrUrSwPpH6g49ZcT2GI9iICwuf0rY1QXC%2BumBE%2BzuSEN79NnQYBAfi4CZtwpGgK3y801KqEqp5eJwlAAk4p4MhM2SsdQIT3hnFXBNAuHsJoBbxf9veYuxVJckeGvGItVHvhuAkytG251NAHXerrGwHlmkgdctsCVOtOAtwFlN%2FG6FBmPNsF7%2BJZuYwSLe%2BLOBG3Ll3vaozaZoNfpQ98FvCnyWzcVKB4TW8mjy6j89No09MARBp%2BtbGaiO4ea%2BC3vf7kVbgYaLg6hiZftAOrd28lvYh1L9qCmGwOEJ4pKnv3XOPc7VzJpTafbCN7xDFqq6Eqw8LkJ%2BCbuq%2B%2FdWREviJJPKQ9EcJXW0hrMkL6xK92ate4T4c%2BZ%2F0UVtLlaKXBSAUDdNzreaDV%2FFhFClMCSUBbVMocUqvTZ5nN0YArq2ThMpKclfRY6a4QPl2LNZe99x%2FAOqCPbcSY4EhXVM1%2BuBae6tlXTLzolgKCZNYGANDDhOySxau0i6MjtMOD5lr0GOqUByQRirrC59e0z9e1ehBcfRC2%2B3LqDUfWs5VlNzncJrOYpoCYDSPs4xz%2F9ooWW6gZaN8vZNHHA0%2BJec16vlmeWKcGghtl1mDkoMLiKdvjma4RUXupSFZeqKBvfo812J6QleuL2UrEGYaSfTOT%2F80%2FDCJrkpz1XSP9cEXBRbYk7IEQiDEsJENiUWRGI7E5YhlaG0rOVUyJW96598JFDnGwBfuNmvUJY&X-Amz-Signature=7f48595865020e487180925dcaef2916476a2b89de5a4d769d4d67ba0b84b82b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666H24APU7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDHcJelIwZYkeKeSF22nF6N2JfUo034xWrgRB70%2BhnrgAiA%2FGQVkS5t9335zIEB66ebpNXdo4hB5L6EHxdvoRLGcMyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM%2Fh3RRL%2FBXY5Xghx0KtwDfYEKdlP9pxgv%2F%2FU4kJFi%2BR1RiFJeAC7ovL0wC2ydFhdMYaPF30jZjI6oWS5Yks8FLQruuAGWaerWO%2B4SPS9kIdonDP%2FT%2F1SIRjfAI%2FWlYUgMZLKsRiMumtGydBAH6vJ6nyYPLA3HKBDDJsHQOdH0caoHiBiGUANUtscxABcpnDTYwHX3hmr%2F3AQA19NYiIRdkoVF0J7LoJdNXybL9fo538dII%2FXP1EXukZHHI%2FbhLMgVOS4JI%2F2NXXSs3h8D5L91c2SSAweT0XIeF%2FW6uFjiQMqX%2BKqyJP1xjm0zB4pEWuHiOkelNHBiQM9kmz2VhXUPdo7vU4WVMx4lK2AKqiEk0oufLiS9VKojodkRvndE%2Bn0u3fdM%2FjqRzJJW6L9RVQcqzsH%2FDHmoEOyPg5pruX1jJDVu57L31maNjqTE8ZM6rIjOIZNx%2B8OPlN6ni8%2FtzGsPE957k8NFOW35kq1FVudoEw4SP3KKwjh27qcvR%2BR0GgniQaJODhohlbcGQVJKhuszY2dpePT1WYy4GVjMJzoZy8YNmlsujo46CUF40te2mjGHpAj9Lq7krWbHcyHcLpauoSZgaHrvepFrR9pT5cLSp%2B04XYwr3XU6FG%2B1hJEgmJ1KhhfD9yd8bRExraAwgvqWvQY6pgFRpU9YOd7%2BvXw%2FDDCXknL8do7ZlcFuJFA6XOPa4yrqHJL3SeG04ZiRB24Mz0w4z52i8xac7JycZ%2B2cv5Lz2Qb%2Bh7XuvYwD8PtdrvvIJ7160xKRFKsHHcm%2Fsdf9vfueiXpVVavrBHD9AATuu70s7Nz5fs041Ggow9FYdCAcR31SxODAZsBHY2f6DKL95ehwSLbr093GiRPZGbiKjkhEYpTE27bNXGWC&X-Amz-Signature=3d53901afa2f9fc6fb08b7232e128b1ac55a5a66030924032c4457074bdbe1eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666H24APU7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDHcJelIwZYkeKeSF22nF6N2JfUo034xWrgRB70%2BhnrgAiA%2FGQVkS5t9335zIEB66ebpNXdo4hB5L6EHxdvoRLGcMyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM%2Fh3RRL%2FBXY5Xghx0KtwDfYEKdlP9pxgv%2F%2FU4kJFi%2BR1RiFJeAC7ovL0wC2ydFhdMYaPF30jZjI6oWS5Yks8FLQruuAGWaerWO%2B4SPS9kIdonDP%2FT%2F1SIRjfAI%2FWlYUgMZLKsRiMumtGydBAH6vJ6nyYPLA3HKBDDJsHQOdH0caoHiBiGUANUtscxABcpnDTYwHX3hmr%2F3AQA19NYiIRdkoVF0J7LoJdNXybL9fo538dII%2FXP1EXukZHHI%2FbhLMgVOS4JI%2F2NXXSs3h8D5L91c2SSAweT0XIeF%2FW6uFjiQMqX%2BKqyJP1xjm0zB4pEWuHiOkelNHBiQM9kmz2VhXUPdo7vU4WVMx4lK2AKqiEk0oufLiS9VKojodkRvndE%2Bn0u3fdM%2FjqRzJJW6L9RVQcqzsH%2FDHmoEOyPg5pruX1jJDVu57L31maNjqTE8ZM6rIjOIZNx%2B8OPlN6ni8%2FtzGsPE957k8NFOW35kq1FVudoEw4SP3KKwjh27qcvR%2BR0GgniQaJODhohlbcGQVJKhuszY2dpePT1WYy4GVjMJzoZy8YNmlsujo46CUF40te2mjGHpAj9Lq7krWbHcyHcLpauoSZgaHrvepFrR9pT5cLSp%2B04XYwr3XU6FG%2B1hJEgmJ1KhhfD9yd8bRExraAwgvqWvQY6pgFRpU9YOd7%2BvXw%2FDDCXknL8do7ZlcFuJFA6XOPa4yrqHJL3SeG04ZiRB24Mz0w4z52i8xac7JycZ%2B2cv5Lz2Qb%2Bh7XuvYwD8PtdrvvIJ7160xKRFKsHHcm%2Fsdf9vfueiXpVVavrBHD9AATuu70s7Nz5fs041Ggow9FYdCAcR31SxODAZsBHY2f6DKL95ehwSLbr093GiRPZGbiKjkhEYpTE27bNXGWC&X-Amz-Signature=87f40e6b4c9974462e74064e38f16ab42e1e1da8861e00b5cd1b29dc658945fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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