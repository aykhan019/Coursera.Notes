

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IJAAM4X%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIBpBva3qxjUw1luaE0yAz3NU88aiLmt%2BuUKkf%2FJwwZPNAiBhigW3HfwZ6cx%2BbYd2pTxZOmArxHiripVViRoFzmvGICqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM24NfBnH5NIzv%2FQKIKtwDr9463gIfbm9G984U4RzEmvROvjjOHZQCcb3Kb7ecwMfFUn8h%2FwnVSLyjph6RmiJNgKd8e6FYX%2FrrR%2B%2B47hOGHS9nu3TIv%2F6bQSn%2B%2FzkLYZUVKXCV%2FE6eMjzAnlHJobXS8fiAv1smF4MoyqtCxHcaTh8TkT4FnEoQKU8SX6vKxjVa8ouoE7xzEQ0y8phcUnYeI2g4PcBR1fiuPh6IPY9jyHxrww5qOCyOn8qnnFOjl6oTt6fT1fHdSs%2BMoiTzdiiUj2B5A00jgz8wojXm340nsISkc5LptfWH8oByTiFI8JuKds8izyCKIe%2B4VbyXK4Ld11xBp2KraL3hgptK8bU8ws%2FZLNZwwOl2OgGSFcmiWt8G4j4vaQy4dMvLlJ%2FzmCQNv0%2B111AXHVzmMluMF7Q01t%2BK4EnTXB1c66kkCfFevc9uhv%2FAehg2yzvhh0E6cEb3w1ISg4kHyIpeh4FLW1jcZBcIoUyrcymoDTL%2BWCBtzVP%2F1Qxm2hSpCjbxenmDbybUCfupDs%2Foz3uY6ookOvx3BG0Kwi74VEbDF0mGVRclS5I5fdnSYwnfj7lldzlozBhNqFpsV%2BM0CPZAbKXtIybT0Ng9mELXWGRnOs5N1Wcx6Chc9WTHCdz%2BKJrQer8w15DnvAY6pgGeuRupBDnBcunjDLG%2BSYqZ%2FsvZOsMVdTkz9vw%2BQi7g76V2TxVldy6DrlMrd10shKi4zm2nOFN%2BzM7uurFwgac47lEk%2Fc8mF4dseC8328R9VlDefTX1b6o7BbUPXFCOweILtvIfoIPtarXgeKC1Iu3FVHMU9WzajIexjfY%2BilpfCZdwA4F%2BKnLRz5frsRVzyOZS6lsIkd1M0EKC5mbFh4%2BN4NSJy4CL&X-Amz-Signature=1daa480c2d6cbe5eea4f4d3ae2b59ff38c3ec4e1af596d9cf1b6d91f7a3e1a6b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6Y2PQMT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIBpxAB8s3qPXqxKr%2BXvn8%2Fa0ZLyidOEzmhf9Mm8kfAvAAiEAzobk%2FJLHvn7mhUeX3oxCToUrBxyEId30OEbRvcXzhToqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMgW1eiU3bwY2KfXvCrcA9VRRpjfoMJ1dKS9B2sFxxOTtgDOD6BNqZpaQ0HHUaz4DK8LGgC4vs4olsn3nMMACbdFmDNLOsShNxIg6CTi94isFa%2BUgvPRPpfFtgqoeZgUTWL8NjAfXHMwrjMFmYzvuhuHN4YwV1G3D7gCYfiPa3%2FRdzHeAt6403RwEGB2bayVLFE0SG6XY3LXQL6pBOCET08TFIUJb8FzBsOjinCXRw2EMM%2FYASkD%2BWJJXLSaHqQfM0fa%2FSu7wUnTHi6xwsjNeR5myYBOuHOETZ2BisuGZd1OtflONgNZ7OJx50dqomrVj1ngUK6neblIAewpYQRbmiDM0WJe34s4QyAwfYxSZgyp33ng%2BpvbMHvkDOnzoyZzsNEVWt725EQ%2BfzXkhMtVBwNRKEF%2BT%2FjwHdyiqGbrwjx2h%2BJ34Jk2w1U%2FFMGmmaH4YA1IOtxLqQ8S9fRtPNWJTI8JWke2EKBUTtkLoVWUrcRNDYqU%2BovJHVBDYTDgyeA4yHgTg8RB%2Fj14bPnmthk7ruK8edTN6KeomRU6e92cFxLlebJQcbcexps3d02Fq3%2Fecw8JM1ChMqIFDhc63e%2FtRFSx0xWFT8PKal54oeMd9SUeWEw0HROLru1YR8wBiFsZgZXWp5oWSgKI7j9ZMLiQ57wGOqUBnSeTjP84pXJqDsa8Bk%2B3I%2BUAToEosRP83MrQqF8VQD9PTIsdNv3rUoFL1wQ9K3tW6UN%2FI4IETJcO7DywFOYg2wsLHR2hFpMRg0Qzv9BFvKBr7Y6YIMWjUr%2FSYAq5M%2FBXkO9PVAbDLJfCIknVVrdol9t3Aw%2FhcWZSHv3bHI9byOJEStjtOZxz4auMOYgN%2F4UJ4Kr0v5cCjNzl1kuH1BjQPKIfMOYf&X-Amz-Signature=8486bb27f6625e4ae8ef25eb6753a78a14ddb1a0c026ab12c0cc07508b49c2ca&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXMTS66%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFpVE8HmnuX4VOSatepFJvBLTy8YU%2Btxpuq4x5uiTUl0AiEAyU1F69wwSduQYO4FpbVM%2BcFaOnifctdQ7cZZ9729BBAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOgtrx1kBY7Pw%2B%2BtZyrcA8P9MCMX2RTe7AxwtgBoTQ4lXHtNCeeqINtGDi6KAglm3tPF%2FN%2FPYmPk7akXxcTC2PuZqN6OHYA7fVwYeGtlfdSBCSAkM724emDKGyGODXFDl1bmSINnwY9tlxQo7ovDNnhgAiwzH2Evbh1fxVx%2Fy62edGAC5L78sdHz2ld7aumXV79w9B8IV7017B3jrCYvZJdHmRZxr5YaRJ1ymI7TwGgXehCqmbid5ZGU8tRcqeU44pKBIsY%2Ffxma8K71lAKhzNYixPzfgLYZQkflgizH28afdPT%2BZLEFHZajS%2BuflhFuTNX830NGccWemviYV5G9D69QOR3gMRnhIP1ocCUL8lCpI1i2H0jW90weg51RE4vgu2F4Mi9Al7r7iMQ%2Bmp2Jj3TTnukb32e%2FQ7U5KCdU7%2FvwO5fQuTOnyU95%2FC91o94OM5WpcHlVNv2NOOy6SuwnQQYPBp3kDpTY1b5kgVx%2FcNovRf%2BrDvfjBTZmILHEA02Zk77p%2FozpyigMd9W15pajXj8cET3kDeJn%2FpyBSe114542N8iZU70ED%2FICv1wKSeLbvSoZh7ImzdB2h%2BIlk95jZgX9eQdu9abowf6%2FbrAT12cgjTFwOUU5whV0y0dhekYeisduwr7lME2U6sPCMKW75rwGOqUBYgKwA4r9Kyzs5zMtXwzEP2NygybLprRsUBBCWtAgagGM%2B1LBHmXTn6C9tjzgCz9PvFua0H8Vim2Kb6yZJNabzCwnidljB92ThIx78AK5Wcv0KiaGd2ArgSKPgfGIZ7iPKdfgzZVDP2dQkB2ycD474Vs56RFUPh40br%2Fbzv00vdnqJ3%2Fye4pOdPN%2Ba3%2FLdKNleA%2FRSHdBE7V%2BQFjsnR3gM4phu2GN&X-Amz-Signature=21094ea21c5ac874df6a5b49be66b2aa384c208fc87c87243f4d80080c79d831&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQERJYH4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHBDSCrRXdHgW3Fz5Se2Jbf7GR3Emg%2BLYhiFmI7W1NVsAiEA4t8xgm1rDHt8BW8ZhbbMUUR7ckpMCQzbU6BfoLEBCd4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHHU7tp1nsJ%2BmPSHCrcA9LxBqRSmHe%2BNxqDTEDQ0YN8%2FsHd9cooV9CPXhzVjZVxZRf5sHd%2Fs4FA2S0DAME0Z0QqnyeIHcrHmCEDpBpvHWwmKBH9goDFGG2SPhLCBXu3AoSC82z9uAWFcckQLDgXFbtltAKs0zOUMl8A%2BpoPCoca1iv1ljdJAOYBsh2zPH9hFgLsdptB9yhgwwOM7Li05ZYpAnR3KkMGKIhu6YSunI2XzV%2FAwgscIIeazJ8c6R9WgvG3XT649OwHBtSo%2FCHNReBfi%2FwG5cu8VRizwtox9Zztuhw9g%2FBL6X2t4gKmkiL4Bi3G2%2FrCrB5gCOumRuLs6USWTPwVcJc7gXMoOWs9%2BhyjVrRG9vQ9Anafh4O5eYBxdwknfKzJlmkSqMX7XhzmK05TLPSwpBjdlADvfhT9hu8kKWhfSqKFqaAqZ6q0eMIuu9XFKpO1rCl%2Fnx0jA1wwzodMNtMOK4LlGD%2F7rHc0g1H8mIslFBOg0iN%2B8cr%2FpUM3VCjI3MbPxXLBn73bMMedmeZD6827sIKgBWhAKG%2FD%2BuAJdECtCz%2F6V5fdGNr0s2hjB2UZ3VVgN7YnuodFFlOHxgBikN06NV3ezs8leMognPkA67qA%2FB9L95xN%2Fl51tomJSwvDy24GDSidjT0UMIS75rwGOqUBTYoJ0y3Rg8zmhqhd9Js84JPRLK9NgSbFrbx9CguzhS3AIMCouI0JrpsWk7feMnNPby3kJq1vd%2FC0cTGonsAmukiqQM%2BG5wEWDkO2g0Tcaz5LoU%2FiO1uGnEi8IQf%2FYFrXrsEtezvju%2FEG3j0QPuIRNowG4JU9hhrbEOYlAOmyzZzNc8d7R7khH1eiocrzQNLoiquAcrR3zMcRwfQaLg1Ay%2FOm%2F1Bu&X-Amz-Signature=4086cba9fc442fa1b4fae72c1c8b12e7519f5c37fd5fdd3613840d8d693b3023&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4RTGF4I%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCXxFMP8y7gnKA9Zc0ZoiKARTpTSpq8wtCq1bn9P6s8kAIgLTb6KDCxsPlXbmFbubA5E22vogK50RgRAcRgcLIpCvgqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7ZUzeLN9kjfAytMyrcA01XZhFpqqOIuqBGpXdRZLz9ygS%2FVZFRNg%2BTib2OJ3d46Cqv22VhU67cMdgkrnskq5rcw9QMGVy%2BBM7nRFzpVCsupj7jNNbAy%2BREkyopYVieERtC%2BQSMVy1Gj4stb%2FoEcFRYWd0mEyH5Q%2Fi740o5eDWZDNh7Qk5jInms5%2BNKkvSCWuTRb%2F5BeIZAT%2FKQJcmi4%2Foh6D1V%2BZibSXDOSfN%2BCnZbNe5dSKHHchtvSxdiViR4K8ZHYw8mLkgeoulFZUdlzob9F11xqlZgGflgVvahTzPrlGEKXpJEurW3ioFQ06QtWDd7BM69jMakuiPMluKLZlhRPNgEMDjourP30sz1sW3OhBVbRNj%2Bm8QfUgDxrhOvWa4VQmZgZlfNugHBDaX1CpN2XGa4rbHkqSYLvc%2FcUkb1jhdB%2Fj%2BiulxkpDQKOKY0v4awxokAP9TfWEgJXs8Zymp3MqBpsgdHzo5s5CF83zaNuMQaTcKjwRtgrUg7yWMkKXmXIdCAqBHwnDTcD2L58zsMDV5cv002pQY%2FfYBXnRoueWZauj2a1m1wAIJAibexIrKrvIJAxO1cTUO8ntkU2%2BAuP1CQKVDfMNulIxYUlIgCnmRyb%2BRWiwJImoua6H2Qk%2FGbcJFDyQVLBswGMJqQ57wGOqUBoiA3I7dyG9d5bXWBqosQbDRhTy4h6tZuft9OaQraYJlov%2FYTXdMDbrMQIJgv0YsUcGYCLzV5GKeGotFULYa%2FtXEmQhczukayR47ngmyPl5w4pCmjbGsBl1a6CRuE9mJ1L9kvgbGJZNMKclPniy%2B%2Bdl8uFwIeWRGG0nD%2FYN%2BF%2BF1UUd9YhnBjZCGWAdQnZMD%2BkG6gLjmDVaaeFHLiArgDzxLpOovG&X-Amz-Signature=fc68c80df891f5eba42f726ef9c77415b0d3f858a314b0fe963c865489f85f6f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HFD4XFM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIEYbNDIWSRpS2tA%2BXz3otkJ21PRsxlAHXyu1qw26LEvqAiAesMA73zhMaQOvMlpUSHnbALZ3z2Id%2B24ia7dGnI3uXyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIDGmMa8g%2Bd86leu9KtwDrffxmICIbBGcIAX2u3msf7tCdAs3vcnEmFFRDeqfX6jktlWrFn6XHJ5Al9H8poE24WvA2hnZSN1hm76RCldqKKOnpLzQoqE8yhWzoaQiaUzGmA1K7V1bOS%2Fr%2FkTZUNt2297mVa51H7g1MTGDlpnot42kIzdSrzDo6FoBgF5qfflYdxEdRf3L%2BDY%2FrEPxe5hgPaEkdD30pennc5oZ767WCtKSgv3KmAd8KN3x6SkjhF%2BkQhd2auQPT79tNB9GqEEyyZ%2FdegBNzcBa%2Bt3%2BKnpM4OwVtBnuzbJPsP5wEx2Fr5Lnhu1gfvwwsVT3UcjTKgAMapz9GZSECGEjgMbEi4ZpSJP%2BaUy%2B%2FASSO4pbPl%2FtmfSu3RuyfUe8%2FoP%2Buxh01f%2B%2B7Wihl9TCTxeKgTyeA8vkXnu20oicp%2FTKWW1ETaqgr4XRt9VE%2BZSesERy0HMyuMIf8kW8mw%2FEhBiy3RlG1DygHyKzkG%2BLnZcmTab8gRhZFHWkW8r9Nu%2FoN24ez5g83LGf%2BR4p7vjmdOIQqZ61WBX4Ey4txT9XbybH5oWnluY1t4mpq7zVPvQJxRwT7xKRslmfJ5vjagTBrvVjBYKm14ofprY1aP6CD73DQo6VPeGkuGb7K0B7sAOqXPmXKPUwm5DnvAY6pgGGvjO6F9hOGfthJW3L8EPvXzjcY%2FilBuc3mWGmUGViwFYWyYVffIutZAftHWelNoxeQgSt5dGrN%2Byn0CKQjeD2figW5Oa8AuPoe6%2Fp79ByX6RVfqVXbXp44SRn69O5GPvrDyg%2B6Hns2QmowtbKJUXuyMeoeDtThiMROnD8meIGslC67yDmazlgIMzMkbDspTfFkIQustzw5BrlL7w5sCMAUHDdzD3G&X-Amz-Signature=4e89bc3a8454a4f4985f990bf9073606449b201f3a93ea8a631a90635baabfad&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CGZ4TVM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDz2KO%2FRmNnL03bjU%2Fob9VMrHvbv%2FK6HLLiQI6d9emwSAIgOPxrSBfGeMl93NnZbMKryN45LyF%2BpjeWZU1h3loSYd4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF56%2BucLOzKYbcB9RCrcA9%2BDK00ONu9rpK7lp2T7qswN9ZyeqEjvc64JnvdoET7pnWhcQNev0Lu8UaVjA48gayZuj9KCKEKjISszPoDjPpN%2FaDdSPBT%2FpttqmKYKsxK2aRt6r3DfxI3pwg6i2zhKZbEwihA7xLoWyYPw3aLf0FbS8V8LynVS5TjX39a17fsj0WOGlpuxeSaHAIftgqtWsQ3fIMd1BTAMe47fn3xNDW7RSfLRBYkQmKNDaeXjaKMqDfq8%2FIYvjrdDtegX1A6vCFCt%2B8qbyudHNn9wNl3VR0dOyo0UmbhoFcOnFyg9w5cAlg6eBB8pPKreMEQ4w9wRYuTEXgQ2UhVqhGyUksdx3KE7YPwWIA3g2VnxVuxNkom8aM6KqY0yUMfFOowg1DGGx30xe6i0U3MXufaiB2jGvvYsOnsvivAqJI6SDijrl1v6R13VKbO3T9yUjJHyynV4FTlNyQN1gAL8Dt3JatcDED2cGdfG8hYJeFLtcNI3ciAm45CsCVu2qN9FjEjpEwbeKnrrl6MxJfZT2y9Zdy%2FXHqihVmYwAfxokbXq7NgV%2BfVXoFjp4AbIpODugJsuGSbKQG4gW0RYW79EcoDkDPMr1%2FAcSNsYW39xCSgkr3AVbfweE%2FSn%2Fl74i7Vc1lEoMPK65rwGOqUBzmSWRbOIX3sjwa8JyeQ33aYVwhwS4Ep611nWiEr63J5QgJrXwERhthLUyCjVdO%2Be1QeAm%2F64xFytMgINvIiNlHobLc9h%2BP74x54CObd3FB4mxwm5JteROQK%2BUKng4gkgwGx67Qvb4MDLDOP6b5PN9NhDcMxVywNDr%2FekphL%2F%2FVQaoGPiNQODoZAx%2BCAQASJs7dK4HmUUk5lhhzzEN%2FBUnLEWY8be&X-Amz-Signature=2a7ea6b2fed9caa0cdb281709e7a1280e7a74de8e43d15f65a3fe8a0910492a8&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFPFV3B7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCICzzWFSldD9ALiScE0GNUBb25OLv8TUT6n3M4YsIKH0pAiEAwvE8QR8xJ16qf0wkz5ljau1PHqCPuFmnld5zHES%2FA9gqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN9mMejg3%2Bz2IVaAPircA%2FN3qvBSkwnKyAvSlbSLc8qHJt7uSDvsGnJa3Jf0o4vnCVVXQ4FuEVBKrLgpFM821PMpdWI5N4sjxhcehckNm34kKdMxEGmKpiLOCiVDKH1Z7fYoGwl5mYpzq2GarYHr0HDj7YFSvou2Jm6YQAcIv7PekDjRq2DHSKZXf8Fkz5EtKX625tA4UAQLQiDG9EiuA4TlWV%2FYrMcoAfmopQ3w4eron2gXSs8mzBcYHfjimDjq3gu3g93RlBjGRhBL1H1l%2Bu3tf0tKUzNpAN7gE9D%2FOSCTt51ib3bS2rEultbTkXF1s1%2FUGIzifs3%2BgGSbnCKDKMir6NVLogC7E6R95QVsnmmxipQcFk9dPYnVH0x1X8U4OL2AeTDgPTEdNf%2FxqtheLsDgaHB3nggBkJpScLG5rDonBMNL2HaIHkn4%2F26VGhKgdOdFcPoougyN2NTNBV33i8C6x%2F5ndwbSkWMWF96tg8eTfjtl6HWrGJroVA%2BD54eQg%2BPOoAur36fsIzKasfcD65EF0I4TWKXTBRljfAaQBVD0%2FwircqZc2EWtL9p%2FIElxH8YMY8vBXtByQnH%2Fnp4SsxZ2Bbmx%2BuJzKtNoQ%2F%2FdPLUz1LAnGkYKuMr%2BLA2irB61o2NCAkjr0rIjWcN%2BMISQ57wGOqUBQLRkv4JoShTzCpESM9tcoOO4ybLnBotQaNGyGi%2B4HrO2cvGekjhrrbOBuhVwAERMZbdWoZFgbXsxULc7Hu4noQGy0HZ81IdNaqraysFfhOTDva0QlGWQPfZohphadty5g1Ixaz4cijJ7x%2FB6%2FrJm7SLO%2BEjw40oPpgZuGDN%2BHDyIBpDZJYQnpN0Wq1J%2B0E9hVPV9DgOB2pLawES7Rtvff%2Birtzv3&X-Amz-Signature=3149e31ef3ac53ed373f3a82f44bcc7e5861ee87ec92b4fdfcfd28654da372b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4RTGF4I%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCXxFMP8y7gnKA9Zc0ZoiKARTpTSpq8wtCq1bn9P6s8kAIgLTb6KDCxsPlXbmFbubA5E22vogK50RgRAcRgcLIpCvgqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7ZUzeLN9kjfAytMyrcA01XZhFpqqOIuqBGpXdRZLz9ygS%2FVZFRNg%2BTib2OJ3d46Cqv22VhU67cMdgkrnskq5rcw9QMGVy%2BBM7nRFzpVCsupj7jNNbAy%2BREkyopYVieERtC%2BQSMVy1Gj4stb%2FoEcFRYWd0mEyH5Q%2Fi740o5eDWZDNh7Qk5jInms5%2BNKkvSCWuTRb%2F5BeIZAT%2FKQJcmi4%2Foh6D1V%2BZibSXDOSfN%2BCnZbNe5dSKHHchtvSxdiViR4K8ZHYw8mLkgeoulFZUdlzob9F11xqlZgGflgVvahTzPrlGEKXpJEurW3ioFQ06QtWDd7BM69jMakuiPMluKLZlhRPNgEMDjourP30sz1sW3OhBVbRNj%2Bm8QfUgDxrhOvWa4VQmZgZlfNugHBDaX1CpN2XGa4rbHkqSYLvc%2FcUkb1jhdB%2Fj%2BiulxkpDQKOKY0v4awxokAP9TfWEgJXs8Zymp3MqBpsgdHzo5s5CF83zaNuMQaTcKjwRtgrUg7yWMkKXmXIdCAqBHwnDTcD2L58zsMDV5cv002pQY%2FfYBXnRoueWZauj2a1m1wAIJAibexIrKrvIJAxO1cTUO8ntkU2%2BAuP1CQKVDfMNulIxYUlIgCnmRyb%2BRWiwJImoua6H2Qk%2FGbcJFDyQVLBswGMJqQ57wGOqUBoiA3I7dyG9d5bXWBqosQbDRhTy4h6tZuft9OaQraYJlov%2FYTXdMDbrMQIJgv0YsUcGYCLzV5GKeGotFULYa%2FtXEmQhczukayR47ngmyPl5w4pCmjbGsBl1a6CRuE9mJ1L9kvgbGJZNMKclPniy%2B%2Bdl8uFwIeWRGG0nD%2FYN%2BF%2BF1UUd9YhnBjZCGWAdQnZMD%2BkG6gLjmDVaaeFHLiArgDzxLpOovG&X-Amz-Signature=62e4848e7aba7b904606cc3dc495783d87b3c15eee221b883df852455c303084&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BRMX4FJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIEHH2BxCEL3hEHx6zmxKJNIxmfxrvMX70oKFVmB919XdAiAslhblc7xz2H27ZOZjprOkYXPHUQyKNuV%2F9HdGXym8PiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0OlJduGWpsaqOXRbKtwDeGiFdNbHiUeZwI2hOfi6lhcqhPxFDJ46fIGMXEdxyWMIgL2eLI6VW2t3FxHJLsXI5lQ3Qxv%2FxakAZoaUfw6mducpEOY8sxIUMBvLPPYsZXQiv418NrHVLURHLn5nGTMbKv8%2BdIjBmIe2pv%2BGkAiPOMPs2W7Ce3Jly%2FdlBGWRZtKzAqxZp0IVmHi8vpFqIM7oYWJh%2FAoio56e8qCzgG%2F7Z2XtlsxDvJ0h4rNyQ5y8wq1SosjHNogwAj3%2F8O4uDV6PEYVG7luwswvwDJ%2BAHuKi01BpVBZUetVniBIl7tMMxIhkULmLMBu8zYZ5kNmcB7KDrNGabzycRh9eUKYyAZ3a39eVw1N24hN6ZoMWou%2B2%2B6RF6lpWVvh9wlMdifQBjgu6U0%2Bq4TmopHQ8E3EhecoJcas0CFpn%2F7Pkpr26kYCmNkGYCn2bdQiuLUkibrM5nT%2FJZe6zmTiX1yH5UCsWPp2XL7gcnyu2pmx14f7Juxz7gVycHPKYTHnVODy4InXsX7ckItJ%2FHlrjSdgPQHfAt78feq5Zes20eR0m%2BmAkwB0dl4pdySeQxUpoqX1JWR0%2BsIdTXbI9SI09ZEqgOkcyqC3LPbPT4hsZvSTirqJB2SuLBgBufRrf2b1KwD6qSt4w3rrmvAY6pgEEzIqYWCLZgXDDvoeKWERHvo8fJjja3TWDzC%2B4mNkn46Um179WhMlYeFxSqREm7IYjBxQiE%2BczNf%2BLZEBsL8%2BRxiX5TA2yDZlZgz85h8QrGrmlNpGRMRMTv8WLKAfgFG%2BSo%2BTRuZA8V2gIbk9vtnfkkykOLKS%2FSOXGFQHsjO1RfyMlAq1aIY3Y51YCLGWocIoQg0yGprfhgoKLpKPqYgljSi0BRAAD&X-Amz-Signature=e779532b7d487b18ce0c6f8d9674fd60c74890d1801ff327fde84a1738a2f372&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BRMX4FJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIEHH2BxCEL3hEHx6zmxKJNIxmfxrvMX70oKFVmB919XdAiAslhblc7xz2H27ZOZjprOkYXPHUQyKNuV%2F9HdGXym8PiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0OlJduGWpsaqOXRbKtwDeGiFdNbHiUeZwI2hOfi6lhcqhPxFDJ46fIGMXEdxyWMIgL2eLI6VW2t3FxHJLsXI5lQ3Qxv%2FxakAZoaUfw6mducpEOY8sxIUMBvLPPYsZXQiv418NrHVLURHLn5nGTMbKv8%2BdIjBmIe2pv%2BGkAiPOMPs2W7Ce3Jly%2FdlBGWRZtKzAqxZp0IVmHi8vpFqIM7oYWJh%2FAoio56e8qCzgG%2F7Z2XtlsxDvJ0h4rNyQ5y8wq1SosjHNogwAj3%2F8O4uDV6PEYVG7luwswvwDJ%2BAHuKi01BpVBZUetVniBIl7tMMxIhkULmLMBu8zYZ5kNmcB7KDrNGabzycRh9eUKYyAZ3a39eVw1N24hN6ZoMWou%2B2%2B6RF6lpWVvh9wlMdifQBjgu6U0%2Bq4TmopHQ8E3EhecoJcas0CFpn%2F7Pkpr26kYCmNkGYCn2bdQiuLUkibrM5nT%2FJZe6zmTiX1yH5UCsWPp2XL7gcnyu2pmx14f7Juxz7gVycHPKYTHnVODy4InXsX7ckItJ%2FHlrjSdgPQHfAt78feq5Zes20eR0m%2BmAkwB0dl4pdySeQxUpoqX1JWR0%2BsIdTXbI9SI09ZEqgOkcyqC3LPbPT4hsZvSTirqJB2SuLBgBufRrf2b1KwD6qSt4w3rrmvAY6pgEEzIqYWCLZgXDDvoeKWERHvo8fJjja3TWDzC%2B4mNkn46Um179WhMlYeFxSqREm7IYjBxQiE%2BczNf%2BLZEBsL8%2BRxiX5TA2yDZlZgz85h8QrGrmlNpGRMRMTv8WLKAfgFG%2BSo%2BTRuZA8V2gIbk9vtnfkkykOLKS%2FSOXGFQHsjO1RfyMlAq1aIY3Y51YCLGWocIoQg0yGprfhgoKLpKPqYgljSi0BRAAD&X-Amz-Signature=3ad4df2168fd860717c39b87aae9a85069dfa3b8430e47614d0bb8e86a3b1afe&X-Amz-SignedHeaders=host&x-id=GetObject)
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