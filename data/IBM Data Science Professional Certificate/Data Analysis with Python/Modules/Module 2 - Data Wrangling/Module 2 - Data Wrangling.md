

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCM263CX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIAFWQ3snAvDxb1OUEclcfXlVDLjIDTXU4S09hBlHGBxUAiEArMDVoAaDaYxsyoUHxU0g6hnZaJqmx3F8Y5WiAIhAk1Mq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDCptFm40KviiaGhneCrcA1Cwkkc1dAxv8zxFXp%2Fsj48JwLf3EiS3ukiJmWzCeMCEpguamsdj%2BHKultgYnc%2B1pf1QgIQIrHuFQZd%2FUY7CYKkFitYrYPxpUFNFIXmpb6XPimlYpepckTYcGo%2BHMU2uzLYfWS3jPtx9IZ507Gw6UB9y6ows94ZtJF51WARS7KHkgioZlZvghS7kTnlqN7C0E8SsDRzrcLJZNj%2FZ4nuB50x3WCNuepa22kKNz0X%2BK%2Fl38eYzU0rtMf5Qti%2BafSZ2WUjNdWCaHAJ99Sm7Zs967tRpafxaaaj%2FZWNZTvM%2FS93jGek0KC0zIrfnrVTOH8wSZXH2QynlVbYZx5m9fj7mYTKgmiXTiQ1Jh2mlKRJTkHm9mkZCNyaQjICTdwL9dwuQ3GVdDwJZFcpm4C%2FN2%2BOm1uRj6%2FeS%2F1o2SWwudADnnXBOOZ95arDUeY2xeBdFxP9wRkmEqSiBoyDGfHRnpcAnWmO3KOpkAFc4utYI7hQegmOVw3IqPSyNf6QKaQxg82bjckb27dbW7goLlrPjbyv%2FRipsxjlUoS82eVv4PMw23sKgCVHSDP%2B5ju4Nsp1mJ84MtHQJEEtu7vpbMZ3Q2UVGOc%2Fm0E4aE4DAxMAVU3HD%2B4pId8JWRKy5ETQB3%2FkMMK%2B6jr0GOqUBjJ0AvZiNExmA%2FoabtFn%2BowmPZgnwBrWLx1rr9gWX06liQhpEpp1aqho1j8NXxzAzy8xJ0SSbMtsrOf9Da3pnu1DIBipfkIehXweZzb0AvfmIkRQZH0tzti0PvJ9PX7hyVnW4yB7vhkvVUhbXsvQ3FME%2BBGdAr9gUh2cY0GZOfX2H6bzaNMdCaRCmHGGRQLsuw6WQo3L2s%2Ba1pH5g9TMFKfhN0NBs&X-Amz-Signature=1812775e348a88b175c19b8c5ece7dad2a30bc9c3247aaec2db94bafd1d75228&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPQTRJAJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQClo1cuZnJtPXe9yyzaWCddbK8UffGuRiMWs%2BfpB5hl5QIhAOg%2F5F6rPnjeUAsKx1ChRBQMFwS2lL2eqz8Bb7ONPQ0yKv8DCEoQABoMNjM3NDIzMTgzODA1IgwQCUFl%2BPjS%2Fa%2B7q0Mq3AOdaW8z0oUQbgYU7d1R%2B18DH76zISaRtGGHXXRbkQ26aBiE9Q7OD96J5K%2F6Ttpjnh3pSxnkP6g8X%2F43xJtjxzvbDWfysuHrQYZTjW2%2BfZE4nx8E0WyEnWx1WgXSzbIJU26p%2B%2F69xV8N%2FW1Ml8ovFeyH%2FUgf2hBIIMshm2N60gPPcPeaClb%2FYKzwnKC%2FikplwOx4m8nONo5ncf4bAYr437%2FG7QFcAcYeIdF9vW3AUqtiUL%2Bs08M6UcukIiTGtmd9jJWpWuMGEs09QtTo3REi9R6ZeBYIrqbVsMYOGag2ELTsUlhThc0D6IMDyEgz70V22kPIzHTgy2q6JGngDaVM32WD%2F%2B30oSJ63bEYNobVmmjqH%2B%2BbfBniVhLF3TPGPM0SwRSvEHVX3omJ25w5PJZZgqChJT5VIFIEZKptXUiA9BVYoOftpLRU7ZhXxNVIvNIFIaVbusfqHrajF1R7nhSSwIAOMMJPBayFGGcdR2Ma4KrolvbyQnJkxaLBRklKGXIdw2oHnrpMaUfp3rTke58nWs9utXG1e6XD%2BrWunCorBbMMTrMOnQWQyJRFc%2F5X%2BPFq4y9fag71S8H2k4vM%2FgGuYk%2B2NNcRng%2Bb1E26YRAjuSu8DhSSjZroejXD%2FN9z4DDKuo69BjqkAefWqNRBSFXWu9AUpXi0acJLBzf1q19OfNQzVISEQ2yALss36%2BQMQRU5mhorqF3IpFGVcR3rtL8bGdp8A7ee%2FcSK0nXXwujPravPAKKiMDrxzUGVa2PxUfqZ2K4Ssgbpa53eiqb%2FXiKxYgnsQ7l1jWSkZu%2Fy%2B6fvOxSs3dBf8nkvnZPsMn8oJ38IhflUS8t%2B367kOtH4ZhzVu3x86fj17b9Da5u%2F&X-Amz-Signature=d9408e96be0ee42e069601423f6fe31da69d477e19492215f640344579bb79f9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWNEILIG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQDlK6D6mD1NZzQ6S5R1UI%2FN9sgoTaCQ49DgEP5Z%2B4ldrQIhAJzavRCnUdFu3bmMHogWOOQDgGcnZKRoAgALz4Qhz86HKv8DCEoQABoMNjM3NDIzMTgzODA1IgzGKWRm2hfDkrLRdI8q3AN2JzC3tjPB4c4WyyBgKirdSawZRqmwwNapEsr70vPRRAPwsLh1uHkIKYw%2FFaokyRJrn8SQ8yyU5g0C7P8YaVjmOo%2FrN3B%2FWmSoayHW2f5p3GgU6XTh3WGHVAqNZIFfAJOu1Wsvlud2FrbtgpTsL2kTlEzSYCYQeryXydfe%2BNQtJFe77yr1K%2BPKmjbCpQ6CjuMJ7VwTFI04RMG8wgDDpvGN0Zvz2dsGawAPYw1A2sEYF3OFdix9lYWgZGlMniGyBN8ebTYUjqf2OWDMoSxACvNmJEVz%2FZKILc4NHUNt0oznTFGUnC%2BPd2exymqg57usRgfb4Y0mlEmMZNNpPP%2Fw7q5qZDO1R103PF4zS9i4M%2BNXofns9%2BL1Y8rRpqtokJyL2zHxA3IzEBwzLYHMEcp0r0cdqdn3F7tQax15HowUzZelVkaOFTmrxTUuBMztR3Xf7mWf0DVyZH7xqKocjOqCVCxJPMYnwUWV3TI4i6VhGNgEsY0UIOL3%2Bfjs3zDrKW42uYZbmgCt0HvBNibLrWGhycBVkoMgAW9%2FwZ97VsQdQ%2Fz%2B%2FMo2mNxqRc7ElXhSq9TB0F4qOZEV8iCXCCmAfFM978EMWceCg4PP7yQkLd26%2F8tV6nqjazRnE%2BuS7uOI1TCruo69BjqkAXGmVtVOmjdvrJOSHZywseQQeeuf0J4tYN%2BMUy3Jfym1iHuFT2AFUKeaPyOCD0Lxp1gwZeqnb478GbTPx2CcLNbBYsWK1AgLeYP9NgM1AYfLFBhLZhEh3bQHK7EUglIoo6aDjmAXteMDJfxrrw5Oi12wOL65cZVeyan4TYvBov%2BHd7U3ROXw8mOxtE6mtNVFvY1fI4XmqKMrmpBQcbYxwvjedh4L&X-Amz-Signature=6d101d9996e594ef0beba45402136483abe32a075310e41ab078f82445317e35&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSDGMCWQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCFkcpymR4RB3i9PEYOxUe112DMakw2cR%2Fb0piR2ZdEMgIgRz1z7gzzuW8pka8C9FGT%2FfKBE59FBtASxTvC217yMO0q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAhnqIHEXGLOTWoD9ircA%2Fe3hshEtV9tmqFsFrhx18nKPW6qlJrEhT1Yjyk4Czz2KQwJ22xFJfjq7LDuNGEgjE33k333r1ZQYfEJv1%2FARaj48nVz1E%2BXK5SE%2FNCcU7AUUIRokWTjTZ6sQsLp7bS9wOppdYtJYWn5GWreHM8QgfJsfKxSg74bm5ZNU08Oi%2BFBUP3z4TMKJEpClpi1zg%2BE%2BxMkZAyek3e%2BSoWUdn%2B1reosmjxXL8mz1p4b38MOKxEn80u9R%2BFh5YSFLGwQujbnMqebilNNdyahjBqR%2FlBhEX0Ud60NYsC54lLQkkP7ElG17iBS%2Fd%2FF6M%2B2BLv%2B4u%2FsmU9pcIZu5Yr5ogh42%2BCRAaYljigBcbiPRrwUzB%2BjnAICbiNZX%2BbwQZvTAIuv2LogCMxk%2BwjccDZ%2F%2F08H6VrFf831pVv4RUxDcKmISGKyBemI2yIxkYE9fZxULnd95KN%2F2idFqoSXRNYDJ4WweVJpUqbbL6NvlhwWMK2EObvvn5eUbiu%2FtCznPdex9XMKkxaOshr%2Ftfz2TsyhiJYaAaVh0Acg3FgeVLcTektj7t1ug7p5XjXVdaBwN0%2Fk%2B3GhbqnTTD0PRVzIuEkuu%2F7lvwQQqASWcUIJsNsm8EV5HhV0qtTmJZD5Kx1CKuzBlL2cMJK7jr0GOqUBnuyGSrkX4QFRj3EC4dZib1h7k5kv0VmjD9cauzy53Kz3a54FIgEnUYiNOKJ500BQEdQTEGFGAo5Bngu4h2vx6Ur78VuxGdjCW0frByOzZty%2Fdfv4AFfXM%2B%2BxX8Qozyir1HvtqdUndH6MeHBLVMYuT9%2FMNp0UlsF6U1WevqWgjO%2Fl6g%2B4CGzMaU2Od%2Ba2YBx82vd5IjANtMx2D9NmuM6nbwYwout7&X-Amz-Signature=81cb07c06793dce6f62dfef53886b7ad659e671936f534d275e8e9e818fb5364&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYUNMUOD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIGbuTKNmc5FkbtLOUqbJM4rSVA5NSitIjHv%2B0Y8bZvGsAiEAzikFe3aPZ5glkNq6n%2FZ6SptppwBis2X5ErIjbrHYqjQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDC61kyxoK213ZH6dpSrcA8C7dvLv797%2FZ%2BwgpmvWhIgTfU%2FR4yHPIe3FEdcnnMY7h%2FbdDZVTOyIY2gpxznGw195bk%2BWpEimHSAVFLah%2FEhuTQe8bv%2FN1lMZYonRxqoN%2BfqEQTjqzpHUDSoBLLiWhfooPgTPB0WyKhjYhmqSnZlUi1xXQYb5Dvz%2FuoNG03M16zYPKP4alQupvz4zYusSvlL3ySMv1iTAnDlrfBo8JDPa5Z3RP8OBdnSC%2BdZlRTL5i%2F9uQMowPgPn8NVoxLplogttgTEgq2kvIBOEk8xYGDucKoco%2BOze7pODRGlQpd1trOgK44HJGDLRBwzaIJPnV6uThYNB0FrMJpCpwDZc8phJlt%2Bo4BzfeIqyJjts7uIy18EtqmuunxeFeRMCWG1y%2B5tHKxAX8ULvRlvyjbZRopT%2Bh6q9Vh%2BeI%2FN8wcYdOWwV8TdaFiZ4BQUZHrODT30%2Bq%2FfhScuz8kwuq354aZGE8oDC%2BcnfugrycTw9UF1uOne2hiquKLcG4K6XoUsAIjjEYHwBzEuXg6mBaLFNlV%2FEnbjt%2Fy71cIM5MSeJX5lRFUx0a2k1cE%2FpH9qGADsLrE%2BmVvjmB7sysPBXTu6slQr%2FLPZVfwCokBG7Q3wgRqs7%2F9iBu5GXqgPxX0sf4lCvGMNC6jr0GOqUBZl0TfZB%2BVyuestJHxzOs%2BecsRPPsJb0i1Ff9n6eAuG1Vc6guRM%2B6TYNX3AlDM5KbJ3IjhCEfWpA3SGTrjPTE%2BOI%2FwoKGHeQqIllUQo3qOk8teU0DCT7W6xy%2Fcniw%2FZhXNTaKt3kiQQLHOSfOW%2B77MZoQ1KHxJ1oP02CwuS%2BpoxE%2BkTqgRdopoikmj0alzzfEKYDZtnKt1hOUg%2FIodHaK5IAaSVMI&X-Amz-Signature=2bacdac0000720396230995f163785ab92187434325fb22cb67ea2cc269f5178&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPWNR4WB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDKt8xJzHIIG%2BQJchWntLagXDhfoJ%2FoAQ5aDoENXx76EQIgCwnag1PSeEaiekDkKyLsK%2F3WDw1SQzSi6%2B5i0phUeyMq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDEhTFQjPn0Aqr78sXyrcA%2Bx8au7RZ3BR%2FsEN4G%2FvRZptBzMfbGwK7XSzxsjMWmgjNgSskL%2FJgU%2BpnHHsuv9mzUdFx2JYzjKaE03MRQHyLljdUKv7Gx3XbQpt5J5AFEVx91gR4jR3EFpPrPrG0%2FTrrSSA%2F5LQ9Cl2a1j4Q2YfRScZVBBmfTnP%2FewK0XUCZB18AM3ZyL1ntM1c4ymbqJaBn6SwFwt%2B3YwLYaVLjQMnSsEr6Q6bXcvQBPeklNNwUiOYcJ2WAqkDs463rUKkoiLhSfdffsu1Oz97n5uO27n14UXcuqTJQiX0nhWRxebZq1idowF0HXO0JoQkhYIurS%2Btd%2Bc2lwg2xmh%2FzMNaw7NtozC%2BkE2roih4DuUY0cHLkbLdM5FXEGJGjsTh5AhabJCRG%2FRm%2BR1IpF5qBFWhG1UMYaOd55Q2fN5qj8jQXeDV%2F3N3tpEGgzVTirJ%2Fc2ujhiKUJ3f7ITBvXYWnCQVZe3b82wNYgaEMsoQfL4pHu3GFVfG%2FBMmuo0KE7iOWwYlb%2BXlCHOJtH8rvyj6oxfWZHlRW%2FkluqhJxtRs2bTVIPjXAdUuSyEGSoplmA8JGSs00YoukIbB9JpCKQoaqCob7vekvkiBYCTYY6lmN65nKjjjMcInNOVhmMQ8vMP3ceqnMMNC6jr0GOqUBpwhhjOZBCC2PYuHnyKOnuyujAVpTooZRN7vVwc%2FzRgsbcaaI0EacYtjDZC8aSV7mUbzw9y2D3SeWUKeXMNxbsyOJGWVJXsCCP1U%2Bs11eUWma2oA5Y0YAk22bKu0biM58fTrQOZsN4G06qwL0fp56vt05sMKvPeUVjIg%2F9T52Gb7GYFflQbDBA9QjLGO1p1DKcuuIYB%2FsT%2BsTEoCWh06YvHwc70Gk&X-Amz-Signature=4818014f26675b7cf1ccc9f368db77d294993f4d021dd1f1ed481a59e2723d1f&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466727UBEID%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDbEbmBIxgqbVz%2FmdRxX1KqOZug89Jg0b4UX7GXZqwGtAIhAOAA%2ByK77uxkb41tpA9t7r0A83dZlx%2BgYwbvia%2B6rfYgKv8DCEoQABoMNjM3NDIzMTgzODA1IgyYJq4SUmPMVVoghQAq3APk1WAClbjBW%2FHUDcx%2FU1hP9vj0uyOXIEifwiPG0cyQHpjT9OiM%2BUzZoLYjkFftv%2Bdmyr1OieHJQL0CrsmJrPCtpn0RrufO0T1FBptOVczWC2bJcoMtFGS3zfX5A8sKsuJF2%2FGsy0t%2FJKzdJpvtSqiYqMkh5EuKDA1kcvQh4Bwds7UJ%2BJnWwHSkqIQcY%2FgmaEqc2FB%2B6h2e1cX6rVfy1diamoh6nEFqzaRfJ4Gv7x%2BiPN%2BK%2Fgwlpvq9FMRVa6p1%2BnkxyzDyPBIFkaNlscX5E%2FQ%2F78rOjr0WZDTtbfOO4qZIC2CNLadosOi%2BXyWQoZVvlWGVrTU2FWTpG2sIcHAxAm7CvLpk61JBEq4V9YlFcyWPOgKAjURs2AlZPBtSI8jntFXrUYRAsLk2%2Bl4SlNYPJ%2BcSFjcW3VUaPBVmv%2BI6Vp7GObXJkr7gB9y7JUb3TFyNvzXbFezO8UWUVTEDq1wuLSgsIcU2MrokiJvaH5N4f%2Bj8wBL8qMoUCRE4mL6JsZ0DwhnesWa5pkFCvEviliSJQX%2BrFthK8xBE4jERBjuCozrtAN%2FdkzSJtpecUwgePZBX9zrI4yl5n%2FFVpVHwcEh2VKeCOfs17Q3bKov0r6hHWsIRwlZ2e2B7YsOXpB0TqjDtuo69BjqkAb4ETEJ6yper%2FN3Q6aVO%2Fg4pyBrj7WtJ5Zk5GDsCWgiURLD6SweriFGszInh6Ngcl78rPaqQhnsweSf4UkMmU5Y6qswEx2lsSWeli3U7q32ONeUfFNxlGI1DmaiH38ePtFxHg%2F3WAPG4nhW8o7m7Sc6ckMwAJ3H%2B6COoWMi5a4U7uqtjEekdIdQshRiqhylpvJdtEHfwmCF6uARr6hY8ieKtvkli&X-Amz-Signature=e0132538a96b71841c46b218a0c044f7d11a01417ede2f0323c1f4e79f0548e4&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QXAA4MZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDoz0PLetmDZ%2F3JGOxhMk0WGhaPm9HPK5RESTr5kF31UgIgDaiuxug567CSzdPxgoNX3Es3%2B3bSvBvjfmkTxD19RL0q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFGqiGg2QEiMSl8p%2FyrcA61QuwJ1CFxHoeGhpVpxkGk4PfSW96Ikb9K0gEnGLx4ZpfzLaFieAZyXnaqs4DLLRU0B17i0hyERathYvlVLkHqp1pu5W1k1x1Jzb9BARhcTivvoJeTDZBDU9YUdF9ja6HE1vYX4ZZQEYNKpD6LzSDsS9AtXhz3gg0IU37ZaMHp4xtQBrU0H8GPgoD7p0GKmVmtYgXGcovYAxo7qcR0wy4%2F%2FN84YitLdA3GDoiFrXMcSV387MIFaQDzpGR%2BrHtLFJ97UxZYkvh6X41StJj8bAq3lS1rllZacOTaK2lsN9odnQJ7Gc9qskEKTQ2oOUrlO6pGRcOupaWVA1WqUCTYI9PS%2FUnowTyFh%2Fo8x1Ac7Yi17%2FWFmslQX4vrHdlOWW3UrxP19ZSOBOrux4zw2Xk0zKcFyHaiQkkYuh%2F5gUMVSQntAZcIlZWL57Hg0f9z78elyFr2SX4mQZ51eA7LQ3sGspvIwOpHZOApwbtjCc24WhEF%2Fox3R2gzLQ09LNesUsVC60ykdMmXK0ZA0yweI61ZREvZUKedJz4oiu67%2BxvtPSCqcH5of5XQ3MtJ5ZM9yK7BmbevKsGO6GpbWHUPHLtigvxcCIu%2B6vGeS5CXsLBr%2BDDxkdjmgL318nGpTMj%2FqMMq6jr0GOqUBgt5%2BsBghJSK95F%2Bi0Pus3v6bbIt4lXgCCNyPUNAQI1X1IFtx7BitzSxm2HB6hrBJ7QhhNWqRTV7WiXmfW2ZlRc97aGN%2FYO%2BfSTGRv9Cv6Bgb%2Fb37bhEpoO8w7ZidScz2wieTBkmlEiWR%2BST590p%2B95wpHB3mO7vp6CYfDbg5qU1oh2sQPnwrnQffzXhfApqZQ2mXq9kZDsjxKSs4nYDI4cXKLDWt&X-Amz-Signature=452cb0670068699557e1be10c28a4d240c77decee31b96a2f513e79016292636&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYUNMUOD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIGbuTKNmc5FkbtLOUqbJM4rSVA5NSitIjHv%2B0Y8bZvGsAiEAzikFe3aPZ5glkNq6n%2FZ6SptppwBis2X5ErIjbrHYqjQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDC61kyxoK213ZH6dpSrcA8C7dvLv797%2FZ%2BwgpmvWhIgTfU%2FR4yHPIe3FEdcnnMY7h%2FbdDZVTOyIY2gpxznGw195bk%2BWpEimHSAVFLah%2FEhuTQe8bv%2FN1lMZYonRxqoN%2BfqEQTjqzpHUDSoBLLiWhfooPgTPB0WyKhjYhmqSnZlUi1xXQYb5Dvz%2FuoNG03M16zYPKP4alQupvz4zYusSvlL3ySMv1iTAnDlrfBo8JDPa5Z3RP8OBdnSC%2BdZlRTL5i%2F9uQMowPgPn8NVoxLplogttgTEgq2kvIBOEk8xYGDucKoco%2BOze7pODRGlQpd1trOgK44HJGDLRBwzaIJPnV6uThYNB0FrMJpCpwDZc8phJlt%2Bo4BzfeIqyJjts7uIy18EtqmuunxeFeRMCWG1y%2B5tHKxAX8ULvRlvyjbZRopT%2Bh6q9Vh%2BeI%2FN8wcYdOWwV8TdaFiZ4BQUZHrODT30%2Bq%2FfhScuz8kwuq354aZGE8oDC%2BcnfugrycTw9UF1uOne2hiquKLcG4K6XoUsAIjjEYHwBzEuXg6mBaLFNlV%2FEnbjt%2Fy71cIM5MSeJX5lRFUx0a2k1cE%2FpH9qGADsLrE%2BmVvjmB7sysPBXTu6slQr%2FLPZVfwCokBG7Q3wgRqs7%2F9iBu5GXqgPxX0sf4lCvGMNC6jr0GOqUBZl0TfZB%2BVyuestJHxzOs%2BecsRPPsJb0i1Ff9n6eAuG1Vc6guRM%2B6TYNX3AlDM5KbJ3IjhCEfWpA3SGTrjPTE%2BOI%2FwoKGHeQqIllUQo3qOk8teU0DCT7W6xy%2Fcniw%2FZhXNTaKt3kiQQLHOSfOW%2B77MZoQ1KHxJ1oP02CwuS%2BpoxE%2BkTqgRdopoikmj0alzzfEKYDZtnKt1hOUg%2FIodHaK5IAaSVMI&X-Amz-Signature=bf6fafce46a434fdd77ecf81cfa564d77eb7af69406ef2cd9f73b9467c3930eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YH7UQZU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDL2KC40gMPNF5d2IriMgsnG8uq5mAdCoweq00B%2Bnv6QAIgfggZt%2BVA8bAJOZIzqt%2BpPI5ZCI71P%2B4Ucv9FHM%2BuucUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDDD5eEEieUKZohtbNircA3lJWYhQ1dQiv%2FNhP2mfOriZXzu%2FKp%2ByfagPH%2FxMDXu9iZerdVw63BM0r3M%2FEo4G2jslG8lg23PgDnfqBy8Gt56usoShiFzJTwfgiEmCDVoSelmKagTom6zxAhJ%2BWuUK0QhybxJ068N1k6Aj%2BxbK4byrkyhaH4ImQ9l9PF0SON8FzzqWbdJdouB346qx%2FHuHdGnoSm1vHigtsKan43Dep8GEbsTXFdS4PkG5jT9bv1IVtPtzitnpF1W6ew1KQAUKf3IPd9Y%2BNyl4YGgwibA3ucb583DDCTyd2TEMtB%2FSNneJ2ACHmRtO3dVh%2FcH6gaCltC1R26husNFGlJ88TGvyq%2FG6em%2FM7U6YZ8Ibck8aLH8NBYZMZJWRm3hE5qd8Nmnl4HTwkdiBhNeQWmcSTlKG6M2oBDTOGMvL3aolrT7UjDB0k7TySHFZs8ssgXVIffzKt%2FvcV176os5Ea6JDyUzw8U3%2BoSlft%2FtM6UOICBVz%2BJV2nmIKVgYI4vrZD0GNajenm09JlWi5Woe00rt0SET9A9zC8GnZUzso6eZrJJKLYixrdszfgUkW0LzNGHbuK0j52leStSp3yJ0mwbP8LvSR%2BKCyFubFYnlFGlk4LutODa0mXfGwk0Zr5Nd1T121MJe6jr0GOqUBVK90c3aiNof08OGncy7leXng6HL1hwbBlZ87d3p%2FeX%2Ba8zwc%2BSEaSH50wPQVZpaFv8jDYs2kqgc%2FlQlbgJpTMI8zOwE4UDesEecv7uKiWlRbL0kBd%2FGef3fU4VieQ%2FHXnHMEmdbBjeHjqX8DIxf%2FK8qMdz3UuQFrBp2Jvkk2DsGEPPqd60rzr0YW11kFzVtnfzQH8R%2BQ4quf%2Fxkxa1nbsHAejnWD&X-Amz-Signature=5dc5727438d78f7d31106225e19f4256a402cb9c6dfa719e8ac658e78964a8ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YH7UQZU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDL2KC40gMPNF5d2IriMgsnG8uq5mAdCoweq00B%2Bnv6QAIgfggZt%2BVA8bAJOZIzqt%2BpPI5ZCI71P%2B4Ucv9FHM%2BuucUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDDD5eEEieUKZohtbNircA3lJWYhQ1dQiv%2FNhP2mfOriZXzu%2FKp%2ByfagPH%2FxMDXu9iZerdVw63BM0r3M%2FEo4G2jslG8lg23PgDnfqBy8Gt56usoShiFzJTwfgiEmCDVoSelmKagTom6zxAhJ%2BWuUK0QhybxJ068N1k6Aj%2BxbK4byrkyhaH4ImQ9l9PF0SON8FzzqWbdJdouB346qx%2FHuHdGnoSm1vHigtsKan43Dep8GEbsTXFdS4PkG5jT9bv1IVtPtzitnpF1W6ew1KQAUKf3IPd9Y%2BNyl4YGgwibA3ucb583DDCTyd2TEMtB%2FSNneJ2ACHmRtO3dVh%2FcH6gaCltC1R26husNFGlJ88TGvyq%2FG6em%2FM7U6YZ8Ibck8aLH8NBYZMZJWRm3hE5qd8Nmnl4HTwkdiBhNeQWmcSTlKG6M2oBDTOGMvL3aolrT7UjDB0k7TySHFZs8ssgXVIffzKt%2FvcV176os5Ea6JDyUzw8U3%2BoSlft%2FtM6UOICBVz%2BJV2nmIKVgYI4vrZD0GNajenm09JlWi5Woe00rt0SET9A9zC8GnZUzso6eZrJJKLYixrdszfgUkW0LzNGHbuK0j52leStSp3yJ0mwbP8LvSR%2BKCyFubFYnlFGlk4LutODa0mXfGwk0Zr5Nd1T121MJe6jr0GOqUBVK90c3aiNof08OGncy7leXng6HL1hwbBlZ87d3p%2FeX%2Ba8zwc%2BSEaSH50wPQVZpaFv8jDYs2kqgc%2FlQlbgJpTMI8zOwE4UDesEecv7uKiWlRbL0kBd%2FGef3fU4VieQ%2FHXnHMEmdbBjeHjqX8DIxf%2FK8qMdz3UuQFrBp2Jvkk2DsGEPPqd60rzr0YW11kFzVtnfzQH8R%2BQ4quf%2Fxkxa1nbsHAejnWD&X-Amz-Signature=1c6cf85c781a85f0e359ca04dcf3c77310bb1e10a89244dceba28190cd5f5686&X-Amz-SignedHeaders=host&x-id=GetObject)
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