

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMIRN4IR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHCQ0geaeKVljwTaGlq9zK9JZiJZa1KgIvNXGw7p2y7KAiEAqu4KobozjgLGp9ZMtSt0TTnPxiPKwn0%2Bt3%2F%2Fzh7keU8qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPYBypoFHv9AB1ZMqyrcA%2Fx4IoYWOTg9%2BFttcjAfvtGwTib8q0DU54z8CT69RDRV89H71Uyw5N%2ByDhd8dsMtizAB5tZIl1IRcvR0tDNl%2FhQG2wPYP9LOBoX%2BqhEHWzPgeXmEGIbXrgXlzeIW58VVGay97oVVTqKoBc6RuRdBMvb6n7AkTQZo26tgI65mgtph8TYFXutPko3Li72NXo39LkkewPTGIvigRGnnyoyQbda8vpYjgQLQbMsMBzVPqqMDaH%2Fy%2Fy7sdeqsIDzZYzIZ6RG37RpAtaIe8ZArbzIExrFe2JPlk9DE0C%2BsNhVqAMRJFTyuTFljjej%2BgLm8IFamCW6zUjLYdr847zySS1Mu7E2%2Bnzg1CTgmOR7pXqcDUG0wGGtvVZ05zfvMozfj%2Fu4A%2BEVMx1oYP6WC5HM6kthaNVXCgm7D37R9UCerqVFN03xcfWa3enBTNdRwquzm9sbDfIdo9JZP%2FfL%2B2frmtLrC8yOhppaWzhvNWQGSE1etNK0PBN3CloPp2IdGkB3ICqFufy2PbIDEV1s47pTPztscHeRqf1p0UXzVHWs6fwTB3Q82t%2FgEUp%2FuVkHLcSn8zgJFaBDlzIn0XEjdziGGuzWAsGrr07qsTM5AwNM8MROmxYJcL14GOqMqhQ9HGZTKMNeE6bwGOqUBipfBJsXEiAhPsvb91FTgi7h7a0V%2Fx0WoxjlaLTuzcF1kA3ilcp5Vtm7L%2BN2jYXdK37Xgw2x6xou0V1J3VzbYHZhE75d%2BpaYwkrfCICDQ2sg4plU8rws8buQ0605286A9xkZWVhIyU8aUfVdbAnuRQJu5BaKHEBXA8SBhABmv%2FAU4nx75ZKxrLt9tGqCZ4wOanUUN5UHKLAivRrOqQsSEcnasgHSv&X-Amz-Signature=9c6a2e2bb56fbb468809ea5ec7ce5e776b2f2d8dd1975f2ed5ba8e355ea5704f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667R56P7WL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDlaGWoNG%2Bmz7yXm7rjijA5mIqgDOYqr2udXAa8%2F564nAiEAv3BAOMuYzC1BP%2BKrhxpcnI7MqLaDyUn57tqa3LKkVfwqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOtWObG7ECbkymCWsCrcA1XZ771zuneuBgUAnxOEGoypN4ec3NWFpsZqObg3mglnlGo1hbtybOVJIDyCmR1NkRfp0dU0qMfk49VleYfarrBX5vt1yas4FrIXTNCKqy7OLsiOcnlBPBs9vs3ZSyCV0%2Fwq7UUhkk%2F5PU47Vf3W5Y4U%2FM2%2Bb4QDUsFE95oRkpCoRRoRxa%2Fc9ntEdrZn30cUX4EPdJ5egKJnsoZAeJKV6euEWk57ijVb0eJbSvNTyu1%2FsjobYQuq7fAbgo0HSiLjM3JxnUOoksPou7namsX49HM6OVUjjcnb0oUMHdFnpQ3yXi1JIQYV22GorZSUqcqIWVtffhgPrsmBucIE5%2FCBbYiQJqx6JUeNeo7eDInFajI0PkSiAJNfRef8rntguN8z7HMQVygPokMy990VcPAtDE1nUbp%2BgEASc9EmwvQCiN0dxn9NjFN0xENm5SjT0YD8mnmtGI87yClLP9%2FKcbsDENZi%2FknZWIaT1dDjV%2BEUhf0h%2B%2FFlzk9KoqcYWNLuXIrUzOnl95IiPHav5s%2F5k6JX2fcT8eucSeQtKfMyJxzGDfO7%2FVJhWbwpMHFCwGC52CqqIPu%2BtY9F397%2Bp6cX7C4ixtnli1Ak2XcUaFEoJEMUZnmcwA7D1Qu%2B9hEkZ6b%2FMLSD6bwGOqUBGC6vdiAn6qks8cdUrGW9Eqdt0tbj5VeRupP3MOdOtH8rYpaM4R1rNvnmJVYw%2Fn5neXwfp8ZUq%2B05L1wDHMdtlF6fytT7H%2ByQLs2DRK276B9pejniKL69uDVYSkIXE0%2Fpa%2FQ4k%2Fw4ALQAMzOhIwk9uCtC1MwoW0C3cq0pxCP0%2BAWe5FcSrmgoZOGUDCGihInRlCZ%2Bhr5dLzglTb3u%2FYWtHcadQrm%2B&X-Amz-Signature=08e1f72ff566c2fa0370cb0ffc500f6969e20893306b0a321bf21c303b6bdd43&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YMGCFIK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFOKOYGzzXVHGI57CClf96Ka21pXVsCeSrZeRyEEDjjVAiBLVmaa7NQbKd3xy6MVs%2FTCM8MdcsVQ%2FVXx%2BhQUean0ASqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCm1RtZoEc67G89cTKtwDuK%2BtmdOGgGSPn1VCjQYVAG2YdL0Uik7k0P1sYi%2FwkyBprtzL3wbEMBP2%2B0XhNEuvNiK0GtxbePJmOmqX0%2BeC4%2BCuK%2FjtBM%2BAbOSMkBHibxKQQD9bPwR6thMVI31PhzANkDReTzavG%2B2ou3uh6nqEspvCL66N4KkxxTBSbC1H5O8dVuVs9cVjjjYE0CVApHaZmc3jJJXDFemgxoMGOla3ke06MDU1sqqZCywyKLBJ6Y6d23kltNGt3Lv1Lv362mTtp03xBzlBx%2Fs9%2BsWtqWWZFLH8MF4lSFB7ogQoiha7WjK6aW5YNALgbrYGNdRhVu4whrZXom3MbwvVsXeI%2Bz3GwLWF5Li2dGkSU9l5mDzHLsK5ObytcfzxxzEDyhcvPJHPxLAhVauW9x%2BHpD8Iy6ZYczxa%2B6tk%2FQLhj%2FsX2fwc0X%2B75xi9b4JfFZdiNz3XHRmBTuJLuWLGARwvKp41zRe%2BYDiRFNAPYSd%2BH58qDBLWq6hl8rxHhWVnRr97vvOIc6o%2FSFAZ2QHFb0nXuUKEPpGDOiCX%2BJBmq4560nGI9XL6cZumPxb%2Bajh96RCYTyBLS5y0CIDDjeQr11inWq1qLMD9zj8XBgxPlQH5DTyQP5MQQCpnDlWP8%2FDMUDpe5Gcw7IPpvAY6pgEh%2FjRkJAJxt00DwiMnp%2BdZV5qBBwaRR0pqU8AZzqrijfQ%2BWOujwQMgSF3hX7oBN5g3s14GtRyIafDK6b4MBtxEUWOa2mxFgvy5eQRhw5OsBdhm1vUcbHuvTKQdGrZjn6n2E4AieSkuPY1DfkeSm1oLjRaU3D%2FXwh5x%2F1AcoBPj859ozEPSOZ%2B32pQP2OZChw57Pra5%2FDOycOVoLhPckoREYB2XCRZi&X-Amz-Signature=714794a921e541a20cb39331be06426c3b334dd1c2be6d7e9265bf125ae6eeed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEBKC53S%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4arEddJVa5j5m8RG%2F%2B0WpKIL2PoKvgirLewM3vLJmuQIgdPqGwxpD9gsrQJElnnwuXapPZMlMPd59X65rXIyocPcqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPq4cMQLB%2BrDKvY0KyrcA3J5T3XhN4JvkH0iT2iKdPi7CjmRG4sj2BscrbEj6v8HvZEwi8xhv5Q%2Bg1258fOsKeQzhowZSW0tdt1uKJxFsaKB3PLZlDoHhfx87OgluOvdfaAGBEunWHSKJBA13sH5WS0AZngZrlQP5GI1z9B0nUR%2F3EOxIEpAN80S8%2BLotXkeyl2KawSjBIV%2BXEFgoXJ5nsUjPzNJoBg5FvzJbOzQXS5fJk7i2yaX27dMYTlP5LFfKZuTAP6hka6qIajNAMlbE1WJlmoW8MxxOnZ%2F6F%2FNmS309hyC6fFwrCddaMKASbSoJ3YjDRTkbbmr7iGsoa1B90GKvyV5%2BbIEWG2u%2FDcEFUGtaa34Mq%2F1vzt0xe2ERQhJ04sGc1h99TCRP7D7OL9zQ%2BzUQKnnFm7kUuQRp5rIeg%2Fe2LGOn6VWiGHKIwsXAKaFZVjMz1b%2BlU4i4plE5SIyFNmonQzOXznX7l2qimc5MKibJeohazCKUeeaD%2FfMnNld5mVGafZMANR42%2BzlpOUt5Rva2v%2F7fiMXiHgUqsov71nyBHb4mkCZVyHgUZc1a90rJUYH4cz9aPdxYunCI6tLg53OAMPt6%2Fmdd0D5gPTo5UUFMZofgzzmHjxZog4sV0xy2o8NtcCrIVwygwg5MIGE6bwGOqUBbZXUmLpcJ7OQQErbc%2F4bBFQyOAHnIno5rL8n3jjmZFNuPV81YxETTL88EWq8A%2BXgpu2NXIbzvu7CZTOHzqfROos6ypkqw4dCTqP13xAa0%2BBwlZunmTSLmZU9IdHKo5H1NsgRQ6m6R7bYO1E3WAxNBbTVWSJoTydWpDqC4kB6g%2F6GXrnGyKQaDS%2FDw3ufD9VqVNXdbiMx%2BlX7dpLNGq%2FtiBex2R7B&X-Amz-Signature=9c68305652bbe05fc1234815cc1314110b29a362bd9756ecdac2dd2c1e2fd0f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PZSOLID%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbjMoJixFQIbuIh6jDj8FyPvSsOW%2F1w498jhgTzeVnkgIgbH2XCG0gJHXbKn1gONdkqDj9RROyBtVVRot1PRxs43oqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL3buazDWokJRBhuCSrcA3GTeuwx%2BbYH%2Bc0sjqr5C2kjctcQkmIu5oUPJb3X4h71VTfHdsjCGc2psi9j%2Fsm4yfiXWZQYTq%2B0hhUQYi72VSMrmn7v4NydYkgDLiBD42zwy7D4nve73b73Vg0fS6JghQGHo0xsXaMPnZXf7zhDyv7ufeyF6esDHP0B%2FU1yppn7stS2ute8dsZL8LLlYDLUbgRZ%2B3sRbdIjo1WAEpcErKytiJ0BkyEhogRZaVqqxRNznnoLHySilnRmvVJOFtRQRp4xzNlPsGL3HYStF0u692D48PDb7R5TaUDxm33LI%2FJEi7J69iHzTR6kdOsbelNwMNSYPWnyV6afNL0aHmTKboaBcb1lDK3JnYNe4d2p%2B5wqc56QlSvhbE667IFXps9Rf6JsPKS7uitpm76j29%2BhQTSOCfx2BjvScZC8inqFu0XzFXPGdduPC7PFfAG2D%2FQCKyOmMf5TyMfsxH94orlzn2VCgnzpfOloB1n5%2FzTa9cOBJlzA1Cb3TuhafdMmVs7k5MQEg%2F1fokoVj2dsdD83FteP%2Fk1WcCbQ4peH27Aq97ccwRQO6KEowI9A9jdLaeYa6o%2B0YhFi%2BklaEumGbB4ybmuxy86VA1WBuRPthkBHXuj37izI0Edln7jvTzhBMPOD6bwGOqUBVYWUj3AgMzGt72NIi96UDJWSQnopXFAB0MwIrTtIGqWQzgsZuJHM6dwhru%2Ff9d%2B1uFFmELHfaE6%2Fz5KXq50p7rfFdJRUWOTuz4emUzlfCvg0C27LI846eWl8sR2bQhTFL4UUvYFn1jr43hL6g0d1Ot75b3mVV7bMsII8eEbJcW%2FM5ECFLbreawiLJ2Nl0tRofmF%2BKd%2FzzCwP6siNJBR8NgRrb6UO&X-Amz-Signature=f7898c87716a49eade83b0bea27a87dedcca65a65029a857caf102d17d1a5ab1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTW7RLC3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjZGAY5bxqcLtmEGS5Wzay1RgCVWwrr%2B8fVxUSMHRHUAiEA3Fs7SKPlCXDZsCxxxFUWG9ry5nphoUr0rIiQMWsZ7%2B4qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPoLC%2BqhoNdPB9vENSrcA2QVLRdakrQzzqSNOXyPxikSvusnGzjHGcL%2FVyUTZNrlL1fjz%2BEyh23qoukyHoaW%2BUWUJLe1bnUx7dvcIBCM9n6Vj%2Fme6PhCGvscCDfH5BZp10%2BFpq9VVCl3v64rIwFvdzKM2SSht%2Bzwv6WhF7jlwZjdIvUthXH8TtMOO%2F7v798XgGlP5Ty77Z5Ya49YMOK%2BKGzt9pIHj%2B1g0ywmIud9Ni5tvOBe%2FWlCuc2mokgiQ%2ByxFvJRpmFjgFb%2Fa%2F7TOgfotwRKcwYrGb%2BYaAVj4Rdf1dcRY5QhAZzqnUH1YpIUdAdJE4JJr5%2BaVrlL%2FUR76Z0SJZvLNb355Bz%2BKWP5eVZulQ73xioVJ0Sop8WQnXCJ80RBeDlMlksgxZ69qoI37qMCxNYV5X6HAMnssENJ3jiniyurixwaBMyO793S0gndKFo90FQDr7io44MJc4RALXh0Zjxh3AmTvznMvPgIwjSR4iDUOIUZB2%2Bs8yeEVvcjFZg4irHM%2FG2PQErYQhgaLpGVVEkqd945FutFpr4Atxe3z2m84lgoNbK63QxwosYuVtjUxjGPVsiA8nlEHLOF69I%2B%2Fbx%2FfwO8SeuS7aDCGyRUhe4BgdLZ6u9RpwTkuhpOc6DMFaYj7D118FV8g8n%2BMMWD6bwGOqUBb2Y%2BR3Bnfx%2B5kxBw1ZAlUCL4jfCQcebatnpP%2FnIvz6Rkdq6Q0iOlZOkgDLNAFAIkR2t0h0Z8zqteWHdEkuRC5Bz59qeV80tJ7WW3hNMVGCkzknh6FStePaUCsazOq7Tu8oaoDPUIhz6kjRxJeLSxOnCYWSgvmyLk%2BBsOGiJmzD5oNsuurGx7gs8I%2FjCn%2FXprmoLpfeWohKG%2BGaGeq8MeWLf0fI0G&X-Amz-Signature=c339975248ae0ca9ed2ec400e86d34cd238b428fe4a69bd44307f48d83edab5b&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667F2C7NFZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGmM%2BVyPvCAhYXwG5PmRe9ZtqfIty4avJivi95KpscEZAiBbH9mwFU0T%2FZu1mQ2JoWZJhUXcaur8xBF5dVXWJ6S7jCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMU9u8%2BQ1%2B6JSqXjG2KtwDZ1jRcvhvajWWxOCr6Rjsw9q0o6bb75Tioc7I6sFXI2Pq%2BRIBf3c%2BKhD9VC6xL%2BOLzbnYdBzakADxH0y9QORSI6cmKB0o0LTbspJP0ucUJdq8oPOoUNPLN%2BJe6G8GqeQGk5RKd22gzZIvJiMUIAvIGtxrsZhXzSIU9ctaikKm7QzoJTVfHPQ%2Btm%2B%2FBSPWi2iI07Eq3HGkYjkA1jaePrqCgqWkqf9le9F5N%2FG23bE6Zf0WzgcVUGZiEIAol9URh%2FjsXdDDLiuhKUZ%2B%2BbGx%2FMRKS9WuNamyYpf8b2P5d4ph%2BYqDeejJ4rPS6excABZF9zsX8dJvMYYkhr%2FsX7Lue6YaOnPcJAUNDLiJfDwMgvFhXri%2BP3MDtMqM3DjRtwJORnTAMKUhac44MuMnAVAsjo9IptLpOcuY67NNNx96m2j%2FNmT3KmSEBCJ%2Br2OrgLB3HhfkHFKuidcqBjAwd2PNQbh939M9v9EQ1hHz4L2bj03a6ZixWww%2BExQTHEUzUJKSFFkBw87YupFVpphi7jz6dlnmIlQUOwBYJJZ7NkPdTGwhZsVRt%2FnAHxNf3%2BwQZH6%2BfhnHHbwYe9kgN%2F5IpsSAbViOUKwB52%2FqpsUt8VFnGj0xlCbhFOZaX%2F%2BBYFJ5eAAwuoPpvAY6pgEbQuWQCT%2FD7oBQTJFGZaARDNCXa%2FUeHbkf2di9rfl6l9yjmLYMI2xSdlnadYDeSVXWng3WbZEDO9ZpwOEtXHSGckyzGx7lueexIehgAkzIeJGROHFuU%2BpSobkENMW%2BPTLvQybgQFIWEtPgfswL9%2FSjGMnnnHO4toJCdnT8FhpIq1NOLMtA2p2qGxzB%2Badqul6315Ga5XfTFmodgPhvVGa7ikUd4nPa&X-Amz-Signature=7f64f266c9e0114b9cf524f153a391affe2801763015cdfbbe0773e80a9d19db&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VJJU5F4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHdZrFepiAjBNOQxLzMoYTKA%2BMPxP4h3Y4aF9LPNEsrIAiEAizCZRNhpTz%2BkU%2BukY%2FLKKrfdOt0ASgA50v5jm8LxyjMqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBYOEWBRr0OUO9mevyrcA0kNwm6zeywECgvRGrwV6Ullsvqo353vkwF25tTMIvkTNvtef%2Fp%2BsvGCdkCHS8njMtdbMJK7heQHxKZG9HPDexXqM8izuoEPJVGEAbnf0JZQi%2B19RyBvzoLmsztwRR0OuRirRTkmEtp%2FB%2BlBuAGBA3UlKOa4fLaHRg863xF5n61dN5hT5bS3bYaf5m6ohCJOqabx%2BGF6wuX7OwL3hsf9zWgg3kjackfFx5N0fc6ClAiLa0eCyulkeIbpy775DZY98OleoA3at5%2BG4FpdSxAhoiVdySjn8MHS81g5yrVDorUbRzA6IlqIfFg6j0V5n1NFtnXjbNo8E3lW%2FXQ%2Fc8HUq%2Bel52NpDlPxdJ4ucOgCaKbnXwljYIxM6zwKqPzLgtQh3PmRDUDXqY5U1BD7HspoFPXoBVfC5uJPOeUf4XI1sAw6daT4k6N%2Bd3W%2BDk%2ByBm7ygaCsAJWp9ZYMkJRvRk7Q2hSD8xdsGecW3dqaIZX3VRY2N4NOzkqrVpaNaLGD8vB5kZoJDldC7bebUjectrM84KjlEDUb3wsi9cnQyTnoRLLhVzyrQuEQEPDs9shfsuLr2hhMd%2BfjCUSVgucyN%2Fr9ThnXC3sX6qN8KtjBDrRA2vQUpnIhxtm7dV6jaj2HMNeD6bwGOqUBeILoWocI4z8effbeNY06ZD%2FUj7TXUxOgkOktNFPrDhaUKDMcEMN2%2BvD01pbqKNRaibudf44dWE7gGNglbKd4TTJD%2F9VuHtySLQw4aj1p%2B811H%2B%2B52QyrZNrSNmcujYmLjx3inM10jU4h7KgOTLxgxBk5VSIO6zrqrAGrvaw46fSqzHG%2FJyYoX36ntE0aBukivolkYvbPPAtOj6pwfnhiMEf9jck2&X-Amz-Signature=bdc99f1292fc9529167cb10ac2d51f911e74eded1dadb1dc53a44b73f818593e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PZSOLID%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbjMoJixFQIbuIh6jDj8FyPvSsOW%2F1w498jhgTzeVnkgIgbH2XCG0gJHXbKn1gONdkqDj9RROyBtVVRot1PRxs43oqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL3buazDWokJRBhuCSrcA3GTeuwx%2BbYH%2Bc0sjqr5C2kjctcQkmIu5oUPJb3X4h71VTfHdsjCGc2psi9j%2Fsm4yfiXWZQYTq%2B0hhUQYi72VSMrmn7v4NydYkgDLiBD42zwy7D4nve73b73Vg0fS6JghQGHo0xsXaMPnZXf7zhDyv7ufeyF6esDHP0B%2FU1yppn7stS2ute8dsZL8LLlYDLUbgRZ%2B3sRbdIjo1WAEpcErKytiJ0BkyEhogRZaVqqxRNznnoLHySilnRmvVJOFtRQRp4xzNlPsGL3HYStF0u692D48PDb7R5TaUDxm33LI%2FJEi7J69iHzTR6kdOsbelNwMNSYPWnyV6afNL0aHmTKboaBcb1lDK3JnYNe4d2p%2B5wqc56QlSvhbE667IFXps9Rf6JsPKS7uitpm76j29%2BhQTSOCfx2BjvScZC8inqFu0XzFXPGdduPC7PFfAG2D%2FQCKyOmMf5TyMfsxH94orlzn2VCgnzpfOloB1n5%2FzTa9cOBJlzA1Cb3TuhafdMmVs7k5MQEg%2F1fokoVj2dsdD83FteP%2Fk1WcCbQ4peH27Aq97ccwRQO6KEowI9A9jdLaeYa6o%2B0YhFi%2BklaEumGbB4ybmuxy86VA1WBuRPthkBHXuj37izI0Edln7jvTzhBMPOD6bwGOqUBVYWUj3AgMzGt72NIi96UDJWSQnopXFAB0MwIrTtIGqWQzgsZuJHM6dwhru%2Ff9d%2B1uFFmELHfaE6%2Fz5KXq50p7rfFdJRUWOTuz4emUzlfCvg0C27LI846eWl8sR2bQhTFL4UUvYFn1jr43hL6g0d1Ot75b3mVV7bMsII8eEbJcW%2FM5ECFLbreawiLJ2Nl0tRofmF%2BKd%2FzzCwP6siNJBR8NgRrb6UO&X-Amz-Signature=10f9cf6b5682e70e89b0caf79656c307f387d42bf02e719fc2fa722a0e495f08&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NA3MFYI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfg%2FNJJTuZiR68UlA0BLW%2BOZuXhLHzQb1KtQZJozks4AiALk2BnZUZPzERAl751k8iSjVstcrWsJDYa9MuAarxSbyqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNDKzt3sTmoYeIW2WKtwDqG7KuOUVnZWSqnmRNU3KH9o3xNg5wTQIpqxa8WCZCEGGAYtjzOPkyhQOvmJQm8zVelS%2BT33P2Kha1scDN%2FKOIONI3%2Bbo8HWYD074z3xySVN5R7bYvgiVqeIzD0w2WOkS0tdJmSFEtxo6bFqgfhSC0d4lTGUCo1ruDJbJtgfytwu9FQGWCiJLLjaYrq2UUegm%2BWNkzWqBWDgkkoY%2F%2BW5F%2BmB%2B8Si3CeRez2MEb%2B5KjrLcDJfC%2FwXJY%2B%2BT3BupbF5EcFZY4DDqelHFzULcdmkfG2r4qLAZFXHImHI2qL605JGq07woNioFkiTNybqTW3s2FyZ13OmAd8cYHDu%2FzMkqKUvWoOX7apHLr0xWz4kTl2aqiqw0lbIhDgB20evsaJLi1o034AOjxP3jZmfRoA9QGen%2F5vDAZ9gtW1NHo3VP4OhXMXYrnE0a4nQONdMj3VTNf%2BE4njQuEZDIM9VPpFeaaRAUc70dg2Gh0PE9NehLDS105L0jl7S6o994F8DVM%2BABxcRJ9quxEEuxCioVoYf0%2BUF35%2FYqLqVNYbhzeo4iNAXo66uPideLEG47sKjiXV%2B5Y5eUcAK%2BILR7ZPQX0v9mudoWrJf1OvvqBfTErRcJIBpwy5o%2B8LfjcUq2diYwwoPpvAY6pgEU0Rq9OnMVzQQm4IBpUwTWSaK1syh2YTyZ91yO5ArUB8ASPswqcqVzM2uSMKd0N4Gl6gVmrUCwPAxJgNyT4R1sKCPRUoCay7lpOsYOC6API%2FyIWvKwmTKbYH0Jn%2FBTHF6n5AwDPUttjZsWvqqwt%2BUcEv%2F%2B7JpEmmOPuRlnMSf%2BGUuYIsL9pqN%2BkAkEI1wqEzHqh4RyqTohX%2BZQnn1su%2BLTBnbgP4Hq&X-Amz-Signature=f4a13412e1cf00800ace1c32d03b2a6c9f49b8c9b2707943df5ee6aaab057674&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NA3MFYI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfg%2FNJJTuZiR68UlA0BLW%2BOZuXhLHzQb1KtQZJozks4AiALk2BnZUZPzERAl751k8iSjVstcrWsJDYa9MuAarxSbyqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNDKzt3sTmoYeIW2WKtwDqG7KuOUVnZWSqnmRNU3KH9o3xNg5wTQIpqxa8WCZCEGGAYtjzOPkyhQOvmJQm8zVelS%2BT33P2Kha1scDN%2FKOIONI3%2Bbo8HWYD074z3xySVN5R7bYvgiVqeIzD0w2WOkS0tdJmSFEtxo6bFqgfhSC0d4lTGUCo1ruDJbJtgfytwu9FQGWCiJLLjaYrq2UUegm%2BWNkzWqBWDgkkoY%2F%2BW5F%2BmB%2B8Si3CeRez2MEb%2B5KjrLcDJfC%2FwXJY%2B%2BT3BupbF5EcFZY4DDqelHFzULcdmkfG2r4qLAZFXHImHI2qL605JGq07woNioFkiTNybqTW3s2FyZ13OmAd8cYHDu%2FzMkqKUvWoOX7apHLr0xWz4kTl2aqiqw0lbIhDgB20evsaJLi1o034AOjxP3jZmfRoA9QGen%2F5vDAZ9gtW1NHo3VP4OhXMXYrnE0a4nQONdMj3VTNf%2BE4njQuEZDIM9VPpFeaaRAUc70dg2Gh0PE9NehLDS105L0jl7S6o994F8DVM%2BABxcRJ9quxEEuxCioVoYf0%2BUF35%2FYqLqVNYbhzeo4iNAXo66uPideLEG47sKjiXV%2B5Y5eUcAK%2BILR7ZPQX0v9mudoWrJf1OvvqBfTErRcJIBpwy5o%2B8LfjcUq2diYwwoPpvAY6pgEU0Rq9OnMVzQQm4IBpUwTWSaK1syh2YTyZ91yO5ArUB8ASPswqcqVzM2uSMKd0N4Gl6gVmrUCwPAxJgNyT4R1sKCPRUoCay7lpOsYOC6API%2FyIWvKwmTKbYH0Jn%2FBTHF6n5AwDPUttjZsWvqqwt%2BUcEv%2F%2B7JpEmmOPuRlnMSf%2BGUuYIsL9pqN%2BkAkEI1wqEzHqh4RyqTohX%2BZQnn1su%2BLTBnbgP4Hq&X-Amz-Signature=c67cbab464c1e08b7f2c5e8283eed3a2cf645d4f3b9412750918d38b5a723e41&X-Amz-SignedHeaders=host&x-id=GetObject)
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