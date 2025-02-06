

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTKZL2O6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIGtAGZ%2BxQf38tA9SDgM7RjVjQzqPhUCoRldmVIwnttS7AiEAuTZSv29R%2FrSqGF87B9INx1cp5yyS6%2FOYv3uVt%2B8vRrwq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDLchjkG0DRbYAZamNyrcA7zMMYwfBYiu%2FMPpdlTHsY%2FGdjhmsZgkX%2FDqnpRJX3n%2B24xnx9068U9uzZJn3H0Fb5xKTef1FHnE9S6pUVWZV6Nush2TonntrkToxpnHKO%2F2c%2FqXFcHCzJDHGZ%2FFSj6N%2BiPvj5uU98QhkSdSrGEnwplKkzGrMZcRHNFoahiFjFJsHOyQqjWOKmVYE2jZHdXQhu3R3nWDfjFuOS6ish53rQr6kbt1nRrNpe8s4ORi7QATZv79Uwczz0Evy%2Bfi08mTbgy%2BZUIKBB23pMoXvNes2n2FX1tLE6aaXNnTNlsrlHj5jkge0un8flw8yqCjz5Kd2BJQc7dyJ%2B%2BJVjhLW8yE4z2kd89AFPj3konP5C2aHFUCcy24eOtXQ3XyZmOd5ehrwST3Gk7Wm4ce0qF6W7WAT3Qf92d3kB%2BY9NFqZd0m4Wnf4Gf%2FnXgc2hg6h%2Fi70%2Fi5qGMfqlUCbo8qyRI2%2BxsA7qodT36ZSiPHBwOLnsg6kAkqZO5fN6oohTzEpADkvQFoaXm%2BGquWF7Oj0%2BeBpXzW4xxIu8249c7CoJAotzjQ3emDz%2FwKeYaQZte6ftCx%2BAt5C7%2Bw4V%2BPURZnn5ax%2BmkKbfw%2FggmHkFucnObbhkWboez3zHmszFELy%2BRnutQWMPnDkr0GOqUBcapFbrPfleZsOe4PbX7C7o8oF%2BY0d9Ye9duYARvuFMygzeHiXiqvqT3CPtp9Nig%2FoCxTbTkL8Je2pOP1pXtU6jqJq4gBBt3JAjgdDAhFOBuEgIpCJ5DOYnQ2%2BHPugU1FkNuIXJe7o31M81IskwnORFGPmiNtnuJXTYzRjs3stAdM1SbZ9nX4bVCnr%2FH%2FuYlSStfZyc6jiwk5Qs4QcfPM41esoCaF&X-Amz-Signature=5467739c53cd59fd93c487e0cfc0098adfbdc3c01c4432679f96a46f4c6bd48d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5DU3OIK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQD2npDELF4hVmPYVwkxX2HUZA57Z2PGQ5lHTUxwTD%2BcFgIgVYfZHPq0eiHnXHjWoFGWWeEc7Y9tQUJUjz%2BNij3J83Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDCk7iteCR8ukgAfS5CrcA7EirZWjAU4ttkfPL6wl3SD%2BbOVdp1a559akoeCiY%2BUvUeBWkkJrpGGcyonRtxCyQ%2FVPqoA0bve7qaYsziM8%2FI32ndteSCkiaZQftQ5j8qc5hA%2BKD8JVGHd3BMGTfJsyS59JJOOSywsdWjs0imbHkN%2FH4DjuU8T9jneRlnaTkg6Vln5xNj8d6lBpI6oA4reqDuBefJAarOzGCpGgodFRUFb9SdSWvz3KlMbhfLPu7xul%2FW%2BmQaNV2%2FeDS%2BJq11PFIqJy7%2F13SKHCPziFKVqNAHJnIt5Y7oq2b9OtdcyLMa1%2Fy7%2FSjIrFFuBqZfdfwaFOipJzFWxpP%2FcP5GmKs%2BjikLJLBln43%2FNEezGJfTOr%2F6RCEyF2j50yYLxyvU%2BcVreBOzCiFvv5VQL1WscczRBj5h%2FmnEyDTPhdlFo6iOBagzc%2FaTUJbXgao3ta1hrAqVQYxTWN%2BBSw1ouJDs13rm%2FF4jKAaCxi%2FyJymPYUg4Qthl7fHpGLgeUXiE44ERHNWHXQrZ1U5%2FhNqY6CyWB%2F8LL5Q4drGqMGdmndZsroV89JGQ%2F3yBbRa%2BnXVL8%2BkAuF9ZcgtWTQo6bnN11fkSCGDI%2BYoEgyX01OnUsZNIwuC8qbFaPP4K9rPyFan3BYb9tWMNTDkr0GOqUBjbw64zpH%2FrPR82ZENEhSeIetX0E%2F6GsjsJMBAOXu%2F3nQghBKcapuXo6oS3BqKnOSTDM4jCbZFcaSUBURvUVQaMEZ8RwM%2FEZ5I1vZkKhyZFzVLkIJlFn5tClZZoeR%2BHSUEPH0%2FWLhBF3uhVVQVF6kidO8KwL8DlmXzU8bi3yzzfBGRROiPhfWptTemhUnmDFpNadDJ2%2Bo9tKC5V%2BkCDIGDfx%2FhjWO&X-Amz-Signature=faad32ae36ebd8608ecf24490ee5361191e9af43916ae305ecdcccd4dd428772&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LIZ6F7W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIEZ4F9UXIFXUd%2FDWRxnbvUbRLwV%2FUtftFuEQ6%2FGy8YF1AiEA3FZO0qqyYhObdL9%2FCKFn3W6iwxHkSJErepMvuuTsdWsq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOnT32l9X2GSEtE7qircAxemPp7uk06W1d42HZM0AVNUoMXIU5I%2BPFmouXUdYiCPpNOxBLxGkkj81qmGY0EVy%2BcLmaf3ApQGOL%2FrTuSiScQSpkLlDcPmKyiKG3aVOj8vxkQlZWey7cjbHgMEtFGcpOW7%2FmknFqgT9%2BAOGgiVoNlI4cGhFR31fAvl0XADZalIWSkMasItPyfNTVbM7IGtcU710%2BDEmcG%2FqOo89sSryUAOQ%2BttorEm37gxmrC9Iyo8VEawyIEhoMdALHxsjRr8cDyN3qWgvwL4Xw45JRuZio2umbruVTWUHeEQySi%2BTT4KgMIBJ3U7PI7GUfSdJ1r9gGRDRf7bnc1nX6gXVB9dZxVzkofzeIkftBpAvXUUaeg93gGUrdRMSArVkWuFQjyMzc%2BH7y%2FB%2F6oGtxWgYv9f10JXCBFhxUMXlr7G%2B2%2BFSgfALNherCLqd%2FBva%2F8DBnGil%2FZSi7yklHn42g4woFd5BDS3uRKZPlXKS9KgR2L2%2BibKJQ91xBJx%2F2N5GJbxqT1SBfZfIzeTC2lgs2W3r%2BYnEPay4lr1mLgXLS7iHIjLKkhrW0Iv79j9ta%2FCxiucF2LsXW8w%2FI45f7%2F95Bxa1Hd%2FVZHlEMkFCM2cN7BHBhtu%2BhZ64PbkhdOK8QcPKKXbMLnDkr0GOqUBG%2BGLbNf9N0fJgTBNO1MFPVej9xdeRGDYYHQAjbc2Rmdre%2Fw56u65ua7G6%2F%2BM8%2BpSo6LDZSaFRX35KB6NlXLmnQ0he6NpDAa%2BBHzv9rSmJegz7e94r%2BMSjprfrqhMJodJKuDaWiIDs5heD%2FpaOPMqbZ0MFGvjBXXhQV06pJphncqplDV7P8ca%2FH7KiSNWKIgdJCbVPVwcPwdyjuRwKilZxGXIjW5e&X-Amz-Signature=8a419850c1e7ba64a0ab71098253d274e590dac0233c765916fd32ef784726b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYCSTIJY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIHsuJv8MZWfuajA09pg373xqRE7GgIf49DKkcRkRBQBjAiEAomeZSwf%2FsVV7keeAWb54tTTaWlzGr6uaFW1AVXaIREUq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNxy3eA6zNwmRjk9YSrcAzk8A5LNE6tNJbKQWwrOOrKDdXH1tXeWqiaRHFqN%2BlhE5480vXhh4IXEW4jLpLWDs7bPuEH8qn5axGGiQYOAfm758uE1UQ3Do9eoRg2gq84DsPjvVl7Zg%2FdvbSleG1RG71AwVHVNeCe6v852OQK5niLawpYF%2FvlBs2r8PX75dyPj3cQUM4Y6bOuS0V04arCKUazPGGIUa%2FVgeWgILEoC22ydHiY%2BryRyRN1hAbkJzYfgCwrcfDwFFNprOIqeVY5pwpvCVMHAumvByWLMyZ%2FesOgahMzyytEohyM5crIbNqm%2BO0GqQZUJLcEGUCgrYCK%2F%2Fx7JT%2B%2BI8phG%2F2GMdpTI%2BZ1Z4kgvivzTl%2F1K0Hgsh83uotWtsfaq6RDde08CZ7fjIvQp5csgKNiCUnIgug4r7mLn51pzDIR7%2F0AVUZmlOPwWA6cX%2FUi%2BZ%2FjYhSeLxP5B9sR4OmOHa61q2JKXFkvvBaFvzY3caWvJGOOaUw2SuJRliV3M2%2FCZuuMKP1sCTRXPu809iz7Kr3lz0T2bQhicHsrcCec6VX0ceaJ156LHNLaBO0lM8sIEe2IYMYeGHm8wvuOAR6IZNtTdnZLRwjrMOLhoXN2j3lM9T6QW7fVEgxeRwRmoRPTQaI55GtquMO%2FDkr0GOqUB02vJpDQlHuDmZnEiEGftfC9QR9FC6kMAcGeJ8SSKNSKkANcHbU0FhUJhauA%2BSUeQXs8UBq7TAmoO3CqYlSLLHCyiLJUWr2mvQybrfbF7XQVtQTDJQIZpstJlrd6RHf4rrBKNTR4JOIy9z9bcm6n4fmxtQeR6sLu8jKfQvta2s%2FkdQPkuDe8p%2F6%2BiNZ2zTv5pgygXQCsL6t4d2VqaDi%2Bo7fks0%2Fqk&X-Amz-Signature=66993d1fe7c6b322c39b1a3882154334ecb3a42856f56f4811af8f807cd7220f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VR2STT2Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQDLheLvgvZvM51ap%2FIYq4jPDcd1pYEwgbZlgYP7c4MT6AIhAOB%2Bc2cRb2MY%2BmSgudlPTYZXG3UCsrAY1J3L1g6YsdCiKv8DCF0QABoMNjM3NDIzMTgzODA1Igw%2F0WJ4WEK7Vc9%2Bf%2B8q3ANHjiEPsWXPyvxHPU5TwMDjhbc6VF5mZBCp1iSV1tZ8LoyTmY2jt4B7VoCr2RBWujS%2BVwfn0YkoX02TxN%2F8pnT1pnAtlkboYJdxjZgPnjajP1vW0bSCEdeLExETzDHqqNDu2iQQ21%2B37bt57qvpHTpmHallEVd0KEjNzvPluWQ%2BRR2E7EsE7hZ1ssMAuZmnYDJ%2B5NZfDM1p%2BlAL0%2BNrZ6QTSoHkJzAoWrszjBSCRVijDSIElcdaU6sDAqSeRgjmK6oY1j55nJcMEvGXGn5dieol%2BVzbb0xGzCW5aiGCeQyiucbU4%2FCwtmmtr9%2BPhNRxcp0UpNISqw8MFrUcEukJjKITvlxxFjT7DLm2KIVJ6ad1hElaz09nJ7lHYe730LTyFi3P3jEN9pkhiFsP7rYI2zibbx7Ja9xoKnVaz6IkUdVGZUD8Cdt1U1jp%2BLouQs3fvMfqt%2BqyfgkMYNjC6fp6rftuQqGIB6iGv1oYtRYnKKdxOvkEb3ANLJTCcPd19pnha3h481C9l2RWEmnVUOc0FxHqMoDyd59odg1J9qVy7KyDX5OSf6JZNCgRNrj67zCBYsf3Qt5Ol%2BGwAXBjqiM7ENkIj%2B%2BSsPfWtv8g%2FgsKFsPK2BAEv65LgqO%2BHAQ9YDD8w5K9BjqkASv1atpk6cwVdD12dAEOQwRqOlZOJpgc43KuN%2Fs2JythE4GC%2BDODVKXcV%2Fj4Rn%2BK2vAcIIErF77Ew%2Bhx3d2igH%2FG0cEb4UQ7LE5Xd8Mw5JdzSA2LY78GixjVBcMvY%2BwPuxzocA2vgYjLr9nvuHykoWMLYqIJXBFJ8jQmahWij2JGVAdYZd6IJyOQu%2F0WKL0ewhGl7VhV4A69TloBziTxgUaNr9GQ&X-Amz-Signature=1c67824ee586c163ae7a0299a188163267a740e5656817e4493a46a79bdcc89e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622UCH65I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQCJTXvf8vRes7sS9puEvruIpy3pO43UvHLTQVOLmZLprwIhAOjc4UEkL5De0EeiACoeTHIEjKKNugILo79KGtjaEcF6Kv8DCF0QABoMNjM3NDIzMTgzODA1Igy9FHDrkKvZT2t%2FVjAq3AN%2FZlo%2FQeSOYdCc%2FeNNiacRsSSLodvbSHupydXqYIPR%2FW0YPlwQTiaYL7M0P0jDWDT%2FzhDHrdsI5lPqMgF2%2FtDramP1iH03ObhxxS7L3%2BimMzwyLF1Dy7RiV6ANaCjwfZ5opv9dlQmMaA%2FTtnD71kNVeawIyVHNlJahcxY2j4sl2mbasLXm9yvy%2F%2FJyHsUZGom7cBLoYDG2FYDe5erEVywqiKG0PEkTSSqdV%2B8bWfJfe4AF8%2B%2FGPZCpQcx98cODxYNw9wpXSefX8o0Kmuk7IHCc4UT0Dypso%2FgMvkIzU%2Br65RbVnwiHXAGJor9Tx5WWXfEp%2BsgHI4wZEEFBnzAhwdFKjOWDzi4voSrvKlJ9xRlW5J4FXgySdsugXOg%2BrAG0ofxJrDH09gRD6%2FGFjgEacnlvM1u4BCuiD2DVLTipV8iEZNdmP5Gbb9O6ABYutjrKWtWnVfVQ9wyl5gM%2BQd8EdZC%2B1pAd49mVlTgGStYwtroksMR40FjP09TJ9N4AZbWJs65hYY%2BjwCkf5FMs7TFFkTHYyjqxxmhwUQGlBEDDBREP2FupMo7lrDgZzoEsSvN8qEaO9B1o96FncgLoJsXsVOCaDovvJcUeFb%2Fc84XoUkcAOCco6vRqIhTC1G6KRTDiw5K9BjqkAQHk4q4aFth9xtXrAtTU3eOkiyhTBRupfIFGShdfO6ZwVJWZLXOq4GTds8ax374Eql5Y9En4odY%2BBJUWQHWf6dFxe5%2B0kgmuy3y1zTUUl%2FdpELyrARXQRYOuzXibSXKNqviOdcfIeoNjGl36mid8v%2FlVVmmrBpxKPR96fCXLa5rI8ShpuYeQBupR9VNft8UtJAyIVr%2Fjs186zPCKNuei0FXxyfns&X-Amz-Signature=cfbebe752e26af8392d3aca1d0e05fb3eb0c781e910709e85366ed7a76d03774&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKH23TDG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDZnamu8efwE2G0rNCSYpjzMGW7O2H3HdtJ9XUYHsp6agIgckKVXGyPG9cfFl8UdYIaWEPS18WkWb2piXfFQOTVHegq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDLprr05tME41HTFt0CrcA0piB7pTLi3gG8bCC3XCTDDjGq6Z4D7MPSo0fe4YL5ScjTs1xLTUCsyPNOoPqdHHzf8kQngLG0IEd3rXeM8ykDOQKJi3OpeEmbfd7X3eAMgNwMAvX1MicTkjI9iIjpEhojBtXgDXtwe%2FeicK34U86Ddkvc5V7PH4FmiV5SwTLN1Q9ny%2Bk6rcEdhR%2Fk4rennijCOac5m4YB3rqHfj%2F%2BP%2BWUrib1DefJKY4zZxVzR6mIaRTkjMx1%2F1ic2Md7yox94wu%2FnTlkBkKVb4B46Nr4ZEGPt%2Fux5BVf2dKmEhAvCqebYiNX68V7%2FjsRKP4nh5dpjuxDb8oy1VLdA0%2FlLSj7PTqsNmHvlZ7%2BZ2awwWQjMSHvb16eKp6FMRQRmw%2BNLYZwqtd0nnfqHIbKVKYCVF2X8OYn5o%2FVuX85eoZ4k513eGF517TOOMjjZBP0eRAHp1HAVU1UY5haNC8dFBs%2F9HB4tO96i3wYDlcxnj%2BYG56M%2FgjN%2BsSTTcOeMcnu%2B%2F7Xmx1yd14%2BtEL32t2NpDFYCHKyfz5sORM%2Fd52fp6s2jf20Hk2wVE5GXxWz0FNzG47yspEER0JFAccTu56%2BXJEPd2qVjxWaCW1XO%2BfTsHPEotfRWqWL3ffT0Yqwx1SmY4mGy7MLnDkr0GOqUBGSCtptywV7V7Pvos4NrhM4zXF3LkRAZfWW1Z1PbJeQAjSQ1lW82CLUEuvly%2FTBuWBgYP5GlbldoF%2FVRNQaISBr1ruaprDC5g06zNlJHDSzy6jG9Ba9yUPkG9oZn5TK6ScAFlhC%2BDPEtnaej9QwkB8DU%2BQ3SCGRfYaXZNfiuxQZ4AE%2F%2BO%2BNiqoF8kNbO%2Fx%2FX0HtLNNX%2BMLrSLQyrBMSIpeqXJ2MFF&X-Amz-Signature=b01eacaa082a3687f19762f17921fb54812d42795de83490873cb2d1cfdb1c96&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7CMMYXE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIC14e7lzCNJvkkM9E98TbYSOYZhS362vidyL2UvLPaMZAiAIjqe8XWKSZgSEql2i1DDjP0PxmLrhDdp8fRjLxGAG6Cr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMN9uQ9v2S8Ec8GtU3KtwDzcz%2BMjaRmeBSgTp2YmL6rC4d9DjOb2HDr2J8l%2BV%2FdVewHfmD8cNiC0WEVYew98KdjMJ0Gy2tbjyJTPmsSSELrD%2BqTJXgNkYWOpYUm%2BjBZCzzg2HeUyAraf8JtPVGPaCQViJ8OaGt3rHllrhFFganzSVsVIu%2F5vi7iaiVyhRV0beDtp4M9hGzQA61Jly71tKuobSgR7VzVJGTjwQ36lO4c5ivmqeZdCrP7usXs28RU0lXP8gElN%2BXZjXzvYh1AnuhEPTHlj2byByzBAPOEoDeOx6%2F90m7kZUcDfl70%2ByUYaLTFNfP2z7eur4HRwB%2BMEYwshrn6oTd9qnY6xV1pJo0l57t6AEVvuyZa0%2BgegQFm4Ov1a3NdtcivUf4ZLxKxu2YxIFX2lGR6WsJcV35gM9I%2BAIhEefqpx5zB0K5MNGqsONcrlb1pSj%2FTxvPUBXf1ZrnnhMwPBeSfprb7nLr4eMQ2INr4AD40hoL6nNXIwgsLYpHmD8NQ0KCifpAgRhMmz8DGVb44kqGkRbAGyBTZOfipTtyoSp7sYKfj7JevOwm5iHX%2FwotcfkiY3AsXcgzdOqI2w%2B3hTt6oVRXOTzzy7dqDlU1VB18Ebhndv04p6dx%2Fi2Vrr2gTQunBTBZlv0wusOSvQY6pgGzRgnOfIiwX6favuMhKxDrlxXt7OAI%2FGbCpgq23qt1WpKAbzq2HLrhmXeKyMbtsZcb4SPPjt6jIBNAlZVvU84c7SmG6FujYY1E%2ByyMCM03jHBcBoVoFqClHv2Alk30Ex3DbseUDBQDiwox4U4vS%2FN%2Bh3WzEyGcqcrR8fAVlPcE1Ts5uRMEV4BrlRs9x%2Bva%2BT7Qt93dBPn3HkuwYJz3OO4X5YxhJkbc&X-Amz-Signature=9c17c767771ceaf7401dd6a10e7bad92fc4cdf1d2fcee0386b42481e71b76b4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VR2STT2Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQDLheLvgvZvM51ap%2FIYq4jPDcd1pYEwgbZlgYP7c4MT6AIhAOB%2Bc2cRb2MY%2BmSgudlPTYZXG3UCsrAY1J3L1g6YsdCiKv8DCF0QABoMNjM3NDIzMTgzODA1Igw%2F0WJ4WEK7Vc9%2Bf%2B8q3ANHjiEPsWXPyvxHPU5TwMDjhbc6VF5mZBCp1iSV1tZ8LoyTmY2jt4B7VoCr2RBWujS%2BVwfn0YkoX02TxN%2F8pnT1pnAtlkboYJdxjZgPnjajP1vW0bSCEdeLExETzDHqqNDu2iQQ21%2B37bt57qvpHTpmHallEVd0KEjNzvPluWQ%2BRR2E7EsE7hZ1ssMAuZmnYDJ%2B5NZfDM1p%2BlAL0%2BNrZ6QTSoHkJzAoWrszjBSCRVijDSIElcdaU6sDAqSeRgjmK6oY1j55nJcMEvGXGn5dieol%2BVzbb0xGzCW5aiGCeQyiucbU4%2FCwtmmtr9%2BPhNRxcp0UpNISqw8MFrUcEukJjKITvlxxFjT7DLm2KIVJ6ad1hElaz09nJ7lHYe730LTyFi3P3jEN9pkhiFsP7rYI2zibbx7Ja9xoKnVaz6IkUdVGZUD8Cdt1U1jp%2BLouQs3fvMfqt%2BqyfgkMYNjC6fp6rftuQqGIB6iGv1oYtRYnKKdxOvkEb3ANLJTCcPd19pnha3h481C9l2RWEmnVUOc0FxHqMoDyd59odg1J9qVy7KyDX5OSf6JZNCgRNrj67zCBYsf3Qt5Ol%2BGwAXBjqiM7ENkIj%2B%2BSsPfWtv8g%2FgsKFsPK2BAEv65LgqO%2BHAQ9YDD8w5K9BjqkASv1atpk6cwVdD12dAEOQwRqOlZOJpgc43KuN%2Fs2JythE4GC%2BDODVKXcV%2Fj4Rn%2BK2vAcIIErF77Ew%2Bhx3d2igH%2FG0cEb4UQ7LE5Xd8Mw5JdzSA2LY78GixjVBcMvY%2BwPuxzocA2vgYjLr9nvuHykoWMLYqIJXBFJ8jQmahWij2JGVAdYZd6IJyOQu%2F0WKL0ewhGl7VhV4A69TloBziTxgUaNr9GQ&X-Amz-Signature=450ec0a0d40cd65133e5afbb28721f248dd6b4807f176c210cfc0476956c5293&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWCM7ASO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCID4kwyYfeXTEVGUkM97V0z8Yp%2FiQ%2BaprhBC15IEhcFcIAiBGY7bYyiw%2BEP3CluEhirVNuBBqRKUZyJDPKvZPpJo9VSr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMZ1cW1qAUM%2B1HzNNNKtwD4XqVSlt8AwRTj%2FIy2LfVJcfJV1OH3nkUKRVT6EaENUjDhlWsmvM3hiEnzHemQ9pVB8rH7S37K7aMImIZC2vhAslQ3StoshlRNUWi4VOEFXD13CjSoITT0PMS3rb7ZwexxkiTbdHXUApStz6xzjhDZvMdlkr%2BbM2lDpggH1ZuDNRNwdOPecWC5gCjSwgOliArZdrNIn3Fn3jwLd%2BgD5RVfqM4XHHfh32s9LpMX4OHifDZphQR%2F2WgejojmtrYfxlSUZYSN72f9GAuIbZyGOv5Q5zQ%2Fp6vN%2Fw0ImhyUHfexrC0UE9%2FXIYUvlnPBhQQ7eN1xvnt1B%2FjJyQZeYWMcgcf%2Fpj90QXPgV4c%2Ftcods5%2F%2BWdQwNI2rLbWJFyHOliO9SgjKAZZx4UAWSZHxhI%2FT5PtQl2USTgQcg%2FjFoPyPjUDh9AXNfwYPjLaQ0bx3BwPL0Y%2BW5g2ELQ0lsPOpKVixqLm81heUBERRfBvasLjH2NwZRdMdI53cDQniTPHZuUCF0mMShuFGQDCQD%2B0Gm%2F0KhqM5nnLyII4gd0tVoo%2FPMwEtHamvsw%2BoGZZfBcxH%2BfXsEia4505nQSoIbn07vAICKQvl2ydLNiDg0MRGflq4OlAk0fadO51TDL1rf6XUV4wmMSSvQY6pgHdLAdvM1SB%2FdR6%2BZ1c%2FZLvW5k1bUmkLtlJelh4hIR6X%2BnqIC97DgBrki%2B6EmZlD%2FkNwvsAs6t2RBHnneo6KbQrusedA%2FO7rEn21y9J0V8%2FqlmSoUdjED9RIHObRdlqytV7S2TtB2pNwzyUIeIS9JeWflLRsyHcnJ6LlQLMNVkGDUyfQ5YH9IoIrfVpsAQMEDF%2BaqHdS9ppqOtQrt09iT72POkt%2FsMt&X-Amz-Signature=866e8616492de57081a77ebdddbd9e23c1c30f17d5100feecb3e5cd4a4a0c08e&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWCM7ASO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCID4kwyYfeXTEVGUkM97V0z8Yp%2FiQ%2BaprhBC15IEhcFcIAiBGY7bYyiw%2BEP3CluEhirVNuBBqRKUZyJDPKvZPpJo9VSr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMZ1cW1qAUM%2B1HzNNNKtwD4XqVSlt8AwRTj%2FIy2LfVJcfJV1OH3nkUKRVT6EaENUjDhlWsmvM3hiEnzHemQ9pVB8rH7S37K7aMImIZC2vhAslQ3StoshlRNUWi4VOEFXD13CjSoITT0PMS3rb7ZwexxkiTbdHXUApStz6xzjhDZvMdlkr%2BbM2lDpggH1ZuDNRNwdOPecWC5gCjSwgOliArZdrNIn3Fn3jwLd%2BgD5RVfqM4XHHfh32s9LpMX4OHifDZphQR%2F2WgejojmtrYfxlSUZYSN72f9GAuIbZyGOv5Q5zQ%2Fp6vN%2Fw0ImhyUHfexrC0UE9%2FXIYUvlnPBhQQ7eN1xvnt1B%2FjJyQZeYWMcgcf%2Fpj90QXPgV4c%2Ftcods5%2F%2BWdQwNI2rLbWJFyHOliO9SgjKAZZx4UAWSZHxhI%2FT5PtQl2USTgQcg%2FjFoPyPjUDh9AXNfwYPjLaQ0bx3BwPL0Y%2BW5g2ELQ0lsPOpKVixqLm81heUBERRfBvasLjH2NwZRdMdI53cDQniTPHZuUCF0mMShuFGQDCQD%2B0Gm%2F0KhqM5nnLyII4gd0tVoo%2FPMwEtHamvsw%2BoGZZfBcxH%2BfXsEia4505nQSoIbn07vAICKQvl2ydLNiDg0MRGflq4OlAk0fadO51TDL1rf6XUV4wmMSSvQY6pgHdLAdvM1SB%2FdR6%2BZ1c%2FZLvW5k1bUmkLtlJelh4hIR6X%2BnqIC97DgBrki%2B6EmZlD%2FkNwvsAs6t2RBHnneo6KbQrusedA%2FO7rEn21y9J0V8%2FqlmSoUdjED9RIHObRdlqytV7S2TtB2pNwzyUIeIS9JeWflLRsyHcnJ6LlQLMNVkGDUyfQ5YH9IoIrfVpsAQMEDF%2BaqHdS9ppqOtQrt09iT72POkt%2FsMt&X-Amz-Signature=0aa592846376e7efdf136df15aac385608a318e51fa75ee09053aa26eaef9b0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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