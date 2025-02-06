

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UA4CTH5V%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQD0Um7QJUiJ9ySsuDeyN0H4kbhsIEGD%2BtWMGBMbqW1kuQIhAO%2FfjKlxwYsDjpL2ahUTnIgQeHH2MUIGeoMJJlSvPXbKKv8DCGIQABoMNjM3NDIzMTgzODA1IgyTosISAFJ2A1nqTI4q3AP1RNnMuwmdFM9TAlWPIkoorEp4B7oz9H7DoJFq7DwXlKNglIV1HEboZ5MFZ%2BaxC263%2F6OIOVPWF3uzw4qb9XbKY672BzgmZEk2j%2FtRYMLPv4CeGBzZZW5MKco9lpwGsmEFiXCt7l8rah6J22A5MoECeesXI%2FRdjjTwnYhmAXdMj70uVa0xb531WhxBiOCXJh%2F%2FVffbyTlNGhwdtvzS9WYjPnvtSzKKqN5VMqJimRwui3HhuEkpZtRT8eAIIvA2uhy1igaFs8u1cvuRvOZoVNdwFVL9nrGQDDc5Ks68KiMsGOZ8NYWLA30oWwKCwO%2FWB9nlgYuDL0Bm1rd%2Fq5VNJ3oqRvsk9eiSkWhZ1njNpC%2Fp8GK8J1dPmfUfyZI0fmVjis5xC8%2BhzwFVrhTjMHsFyfhip%2BKjWsMQ60U1q9M9lcCzpTqL4ZamIOJQ6TdE2tbqC07Ab7FKOehEj%2BLQveY0VBcTS1ok7ug8tRs4QSzVNrseHSA2WQNYzyyWK9z%2F6rntwo722J78Z49SxreO%2FxoS5fxtVhzmJmt3a5dUHF7VDduc3K3jxtkAcoYTvtoVsFAQnvEN2xY663j0l%2BSMSRQwky5FFL2lY%2FqThp4fCiHCIYEGrqc%2FsnIMKX1oS%2FX2wzDT0ZO9BjqkASwncnV1Fxke1Zh%2BNT88sWTSAfkwsY%2F5W6Q9fpA%2BdRy%2BvNUKCL4rpi6w43relDEFGoKk7dVsQ%2BTtfbL0YwDAD98fBdXslWMdaG2w1GTEitV6VELqSm%2FU%2FXaMklQadqqnmnmFki9KmFE7Tjnz17QzbrKPb%2FdoDL3Bv5S1P1XE9zLj%2FaF3eUkQz4J2YgIP1BZeAnZzg%2Bqlprq%2BThAUMNPl6z4CHCG5&X-Amz-Signature=dfa6c5e1a828ed37985b1e7409191fc56c0b38b8f2457a8b17b531bdee4a0d93&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPIPLXRO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIBVoUQxLv6fl0pTpAt%2Fr6X%2FZLzhZZcgzIwUXCMNwgwasAiEA3T12r6HrLSvpS0AbXdpRn0r64aqvFZa6R%2BwAfRuG2f8q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDJxo%2B1l3M9JJpzp8fSrcAxvneBFR5xyml3xVR1qF2BazLL3fkxfInjGGLvPQa4R1MOTIPJ9J1KH0nh9W%2FmbOCFv5rykz1Ikp01pUAEUByQVYfWCxBLDPF2gbcY9zDAGvFh%2FoZDWk8h%2FdZpLxU6Do6JW85QdiHS0csJoylnwyuclDONV2MTTo%2F8pOElCGLXJhq89kTYJWe%2BZxgikl9mmD%2BtmOj%2BoVTTiWi5ZbbnQT8rIzHLtyMUvnQYDfcbVJ3XteR1I8PYy%2FP6%2BBc3se8ZfGJU%2F4IGY8YQcfpstZOsUlfvatk7gpkH2DUcUJ60BuK73639o%2F0UC3MJ4a3N9vxXhSjCsKzwiQ3mZusNop6IqL9u4y9TzR7j5c4qOQF0ykp%2Ftolnws9QH51JTUWvsT0Aq8RunfqVmAQ1QL60AjmJMmUBp%2FzKV%2F2MxLuzcXzptMrb%2FCclCN%2BOiRHiWplMNC8%2BPpmnine1HmGdD3qOjsWYrrjRBoVmQ3ogxOu%2FEm1GgI3%2FBZn3ITJ5y4bNkk86UZHxJsPG17I1ImwD7Y6%2B9BUkA%2B%2FWBwnGyu%2BW80RkAh5fTzS%2FUYmTu9hPheB%2BKYN7vOHwDU5wEpvI5Ag0yL806f4k7fDCbzP8TLUgMFzWfbpaVyaG7nNRm822f5M7yIRXRSMKDRk70GOqUBVFaE8BM7eSW9OT7WiQ%2B9Te3ucMqLN02Ch4EzB6BRGuQHx%2BY8vn9zbTXmAnmGAWDg4%2BcF65I5O0XId4coi8sHejjNRSD2RGhRwugyr7JKLgVrhATatupfjJI4cjZBfSa%2BOmlTeKqFz51I7K%2BC8MoKXBxc822yYLE4lKZHlfjkEt6fo6toRQsV5KJzK%2BWx9ILfhE3rWJl79v%2FSFKKx8LCNmcygeVwh&X-Amz-Signature=5f12cf76e34a4a87319bdc213182b5aca4d07b259f48320a9a8b44588225e966&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJODJTZ7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQD4HRM6dG8J9mtQvSLo%2BUea%2FeKXUgesWpyWSJ%2FOoIwOngIhAMPflhzjf5Uw4uGOOcbDdLVDhusP%2BLzlVkENmZrIEdD2Kv8DCGIQABoMNjM3NDIzMTgzODA1IgwtchI%2F%2B4GphBIhNhwq3AMSq5dxCkwfveTEPvETkGaiBEvU0bXsRd2tLCukfJ3ycZ4Sl3SLmZ3KD6axxYwC19JymdDIeQDwbkuYCoghRu%2BbykRmDnkpGiao0e9ciwGZ%2F%2FsLnyqdqeAycSxNJqqpoGE8%2FVsqUO7%2BGp%2BzWbIVfoEs%2FWYNaYbQg330HxC7dOXW7h46bROR04ibwKpX3YNaucaXeFWZ%2FtfVpdF6Kc%2FecTzVJyTJ77aycBPn0fz2dXQieTzYqw17V%2F1uy3DUOmu5RZAB7QW7k2DbeW9x675xsRFJiUHEJqoKej2CDAOw46%2FZxZNia8XVtS5Wn%2FyppiaslHmidBaj6nSrIrdrTF4RSeJq%2FGs6blUFlm1FWrYA8TzmmdbXAzYPfRulnAggnFF3g2L0dwm4oHq46s9fs1jNmMEoOnq8De%2BogGbA2WrVC%2FwwOW%2FFZLRmoyJzWmHwCIMcAtHsIBwgb5Z6PK7XBwPVVFXRyNOGdrtW6Z7SXSyIgOmy8ZfqG6ng%2BSVnMVM4ufFjOR5pKn92WB5bIgfUwuLplOTLsLf4nJ7TD941ec3%2Bi4BXzGKdgaFQNBE5r0jpMeAjE1K1nCJv%2BvveVwTXx5k0D5VO7NqzioF1F9xguiKwGj%2BNuczTix4gpvpfGWYADzCL0ZO9BjqkAUEIwRCfofv7%2ByUU5PCzWuxaPc99nRXtVoRZe2W%2B7%2BmT5dFSVZeFMT5el1sWFrv%2B94mMNbsul8sBDoT9MPr%2B8tCG3ARqpYARPFhGG1Jctn8DwjYb4tsfleL8z9uoMz2sD%2F9yzetqVK%2FjRwa5BylTlK75qfhxx%2Bj%2BELYqYiwZ5cDFZOODeM23ACs0RaBgqSsMUWaMVYq29sXGrNWNXQlvyX%2FPCs5U&X-Amz-Signature=df81e0c6ed6a1ce1cb703831be96cca71508b35fe58da854263bd5e854078673&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HLRQOFD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIAnmf04soUt2k4d%2F6JPj8oxQf4quLe%2F%2BPHpyIx1M9oS5AiBvYnkiUABBVlkMJeKPhLhC0InUE7wu7La52xGKZjtmhyr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMSS4OTG7sUZBdFkK1KtwDeVzYrnNuAZicAwlOnH5uSgadKZ0h9SURnoIwvYSDZMKGKfve1sjxFI5PS295w2X%2FojQ9MJNg2ksOaPOI%2FKuawBwxYpRZJ2JgYqRGakEL4ZhrFgopV2khSoIsBlo%2Fq0tFDBkkCGyzbNZfxU8e%2Btk0v%2FZyKNd%2BXQVCK3kEvB6qWhZ7Tdx%2FW1nVN0EBd18zGLCOS0qUjDKuhQP4FJG65qyxPPKWQUdWnYrxlvAaWc3KvPQ43zC%2FTXEzS23AxXvppL6%2BxfHV4O34UEfL%2BFtqenHlwK%2FMF2zix868yfsOFfrMtbJ%2BwOiRvK4rpSeIYQjZH6LI%2BAJrVq4WBRsoeeEdpLFCsh0SrTV7GmS%2BG3H97rP5zRgqrByJRBPmqV1Trrm4pwepEeqrJZb%2BBA8h2Z3j885MagrqKNvLr66yccHf7v9B6j9PZgR1iO0UOGSAgtfC2c2x5F3yg4KUUgA6v%2BpHRXWQuj3hCRuwnq5G9Dn%2FZ7ajdrvln4lKUiI%2FfB85gbnHwdMHfc%2F%2BSZAEPW7YIwuiyzsvgFvJoLJj%2BzIb%2BH1jgJYkUKzG0FFaMqaHy%2B31ba9KeOTcWZsQHbcuxcXEFrrzL6s29xsVo2UyeV3oLsZ9TNr5auHuDbCSDx2HYav9QhAwk9GTvQY6pgFIMl5%2F%2BtF6TvrRvZ2gpqH0US67SNEIIMTDALOcZri%2F3FKDQgBHQIBz8HIuGv3zwSGGS%2Fm7IVhSCgnwe%2FDyqDGdyUVPtL35UlC5Qo0EkzHWTnJeEtVswY%2Fp52y2FiC0fPHmuC9glpPCa3SLv5ptGN28D7c9Aco2OZjW0W6UFdP0vIoV9mTERGfjauwALXS3J%2FoR0Io%2FwkkmAmSFW5bSIEASAhGshWZI&X-Amz-Signature=83fc6181b67d8ae3ef8a32a3d6a7e639f0f851372e96767158de3b34d493a978&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VP52GC6B%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQD%2F42OGekunYNDUzbdJE9t5%2BHmxR4pJQC5v5TgY9MBSHQIgG%2BUz0rCjm0%2B0XH%2B6MYex3BHStEqGXu1TcRwiSO3RNv8q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOBh1pTkd6jrw9w3LircA1LxUQ%2Bs8zl%2B4a0Vz61yP%2FFUuixYrnsVDCa2NB6nB6gsQWJ7s8L1U2Lm4mI1UGKaKB1RB7NOO9Ar%2BQ0ybTK6zTkNmL%2F4azXIpMfe8PXpVJo1EGO4Y%2BSxPGgyuAZlvCrdQCmlTl8FKPCS%2FXYQFUgVrSfWHboyVv1jqAzJ6eXV4ZQH5cfseCgsOkhjWULjEXcMnedeWZnqF0b5%2BPpnCVOD6fO54YUNcKxP0ETdFhpdoZAguPyi5sswKFNj4gcWEmiYlwjA0B8rT4Vz82v3JJF6Nb7SMOBa7xhGj43Y6ta5kjwruXd7HSPwB5jxsqpd%2BOrh8ti%2F7oUfDujkGi1jihxkh1ahlh7CyQ%2BOQDlqcdh8EHC5U3U%2BnEo2gAdcgAwYVKVsGooocUBEeJZLP5isP41ANvso%2Ff%2FlL5qYsZuC8oGMlqhUW4ytmHW51BQsMIRWoKIBHISnEVykwv1GF3%2FoO2uzobdbVhk8ief6Fgk8hocTK%2B9PzFn7dTPJzyrcrb4lwb2Yk0GG6A2Pc0hIX7olXKHtGxwf52TPnB16vjEl7q%2B8V06WiJOVe%2FVE1V8A1AmeG08a6GZhKdqLJGouypWhodmZLYz2PnYr%2FdNmzyddCyiX5A6klNkvwLOrAKRyykOzMOXSk70GOqUBkwvdDDufy6GB%2FbME9eOgmz%2FgCZpWg%2BvLzZ40%2B%2B0srhIrmhdb%2Bcm%2BQ8FjSu5wBd5JnrclnNQuCN4b34pVuK0NFgIr7kz%2FcJTbvUxYbPpQ9MqCPOj0EphBZNEEDlUbEspUVF9%2F8UQShPpZT9tZnhot12U8R5w7MGmecguK7j2m310%2B1kG3IrdQ6teVuTz0w5cmEILY7fBwgwu5KbTBKLXhp9jNMY95&X-Amz-Signature=8b4ffd657b7c814d8919e55cc9af005dc3e9afb54da8bc8c825029d3f06f5b8b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOGIITDU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQC4pUv3CuXcZKpuZLoSogqrjtaBU1h8niSyWOohBaWq%2BgIhAP3V5uYqwzaNckeOgfAP3EoCkZmTsOCH97HeON1GxCIRKv8DCGIQABoMNjM3NDIzMTgzODA1IgxVmJJ2at2CHtqA5jgq3APRCrWM%2Fi7CzZOGEUUhv2Ehf%2ByBOaPVwG8MNqHUA9SNT2NBB0ws%2BMONwconMZlhB7tXBLtX%2FS9FyjqZonJ280tpqE98I4X11GRMwqk6c6eS1aksU0b%2BYye%2F5J8UtVbt2Xwdexp3mtMXUreQGFwYn4AYdylynMlI5UW%2Fb0nquJwSNJ99gdM5XBqJDNxPMFUyM3edUOT5Ljsfu4MlKESVbyXQvZVfbek9yimTdv09mfJbH0YyAXWsnGGmZyo3RrZkWaQzlTju0gAd5Vs%2F%2FEXAcbAzN%2BfyP9IHcknfdXinA%2BRknjTvEmN%2FCxS6KHb8PADbvrOTK8sMGwmTHU3KwafmtQ2EkDuaEOKEbzC%2BdEdiyfxcdOq8GLaV5A9o9YZx7wnQfBRbocN6Sk%2BYm5Cot1DUOdJOLnrn7UAu8jty4R3YpoW32DfHa8DTf%2F10uXTW6%2B8sMxlJb5Fo%2BXkmk5xEAnLGglNaNrTGCcLZkPQe8Me0mTvIeqrrmlbeVxl7LAXjx1vssKV%2F8fFv%2FlTIK8Z%2FAQGm7onv94fjK%2FmJmgn2La2FeVAxZCgGo%2F7mr2hSQejhuNiUoVUkbicJdiTSAjq38k06kBwfmjPOnZTalyjINTAJVsjAitbx0Jn3x%2BKHis%2FsVzCH0ZO9BjqkARfFFeVSbmrrxIXretT9BQArS90SYjlP09%2FQmzMhPxn290pWq8GfvOO%2FcFgHxz9rPrBFA8cKgPhGn4brO11Wc4ai2OLeh%2F08tffM%2FfjB1ymdpbmuByHO%2B0ELG36rN1iV4NNpvrFXPyOtmAdBZEVCu9P4Ap%2B%2BsTy2FS69IQeJ7%2BSOqDLp9adtZrSK%2Fm%2FUVl3M%2BmiYQPKi7Tgl5lSJr0oQH6qfREED&X-Amz-Signature=2dedbbab5b4b40cb9e48d2d3f905e733f9c0a16aeb40d78c6ecf5f199fcd32f3&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSYYFJ24%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIHQ8X5VsQm%2FhZzptMbWkaDJBSsIrgj%2FtAda0mUF5m6VfAiEAxY%2FS3Km0iDGKpFOb4ELw%2FA4ktgX8LlzY%2ByazHEaZTrgq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDEMFtd7cIkLfQfX%2BuyrcA3d7b5PSI%2BtmBnouwqrgneF7j%2F1lNx%2BSr56wWg6FVchC8o84dyegXVowmJFkUAldgbUuNet3RzSyTJamp7%2FVb5ERhUZk9Yo7aw%2F4HKgtc8SommlNgPc6PU%2FVZRuWwW%2B6Wzgt%2F22UG5c6kCrVFID69W0qdIwdPfq5JMMOVp07RfEmGVwKo2dE2QrB3HsLJUohIGlLL%2BAyGcLr6koHvEEDU%2B2pioB11U8WBRoRWI5a5T1ZmiOT9FnfS5OHZAgqTZcyDDI8ekb3A27uvMh%2F5AxKsYVVpC5qD1oKqfXc4334MY3d8CYq3uvSV%2Fw82qDP%2BDMW6uUtaT8BknYJxMxpvCc02Cblyeq8l6HPsV2e%2Bza8tp%2BVzq0kiCOH9EGcY40ZuBaCAjPJsv07S63Yj4OvNU2Po%2FbXpC5kab23LRrcZGfXqN%2BD8wzJSVJEzvk2lKBfO2H1h92DtNuHFAPWsQFuj352CW2aIvTyI5mlHEY4Z8Q9TL5qD6i4urLnODC6XRn0Jwex6TraD9e7btrzvDwkDOKaIRgh1JxRAVX3iHY70JuEATFiPi7d1VtsbpZjxSxrRC8NHZNcp2lc8T%2BIFmdP6qrGX3DqeV4Qngip%2BdrAlh%2BYCcT%2BYYfoJ2ZBmQTSD4BtMNXRk70GOqUBpP5T6FZO6pvLn3r%2Ft8IRxlJ%2FMUWejPNe5HDgNQaEnmgSguK8cJj7%2Fxd1WmYmw%2BYTHBNjO3qK2t99lwK87Rbxg%2Fg0NeLdbKAKhWY%2BxWLHXRqDIlR7wAjd61jld1jp0Y0%2B%2BJMWFIqPuxwgilvv2mIIfEZD0puZnS5eTQdSOb9IZrL68DFNyyyFDTooKWjHg%2BEvDXQ5DtkhVw2O8ASbRhVs5ryEQbl7&X-Amz-Signature=1050b0b04d859dbd0a2bb0c2f75e14e60d393c28b65d52866f75e96fa69cafe0&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FLGDZ3E%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIEcl23v9iNbSWw8NDLeh91kP%2B%2FOXMiUnjzfjZWCfhED7AiEAv2YxnIFsfCk88HToVIXS%2BuBjQoi9NAdREwfL5G0db6oq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDO5rz3rMzjcXj%2B11oCrcAz67zZhnqGHtA%2FCG%2BP3uYHFu9HDSxJGKEhMtuEmn%2Fi%2FGx4LVYkynNVmK7qJXNyQWXLfBxfLOOoS4q%2BnVf0SiUasV9frfMxQEg%2FhEbKQRY1WDUPVt5HeLFDXGAsfjwNvPZcwRck%2Fbxb1DMgN271xRXMUfOSFBcVa%2B%2FgrXrI7UuXA11P5zoRaYkDk0GPj1GCKg%2BqDgbc1zHRcGRGG0nXDlXswIX35DBQ%2B0JV2NQLeRIpJ5TrYWRMBmTQe0vSum0fLFH3ZATdMoQNjaDqvammXxVsStMXJ1zqGB%2BfZhgOcJxEdtOxXn1luoSttjZQvaOtb09WS8z4s9siJyAoJyf7CkLHa4vNr3Gqaeip4e3DcOcYhJKbVnTHuF3K0agXY9UvwRiJ3Nzz7PQ%2BrFPB%2F7W7V%2BVbCSZoc3lE1r8NbDwK5q4UDDKgvTD%2BhY4vcqDz0gC6mn%2B1r%2BkMlK9QSYL%2FGwwMAfh2mwQiEtK0uEq%2BNo7yo%2FjXKTh7uKeAOnjHQGgWJnAHP%2FrNoSTLF8sjIL%2BkttNSfpZvZ%2FEYhQMvG%2FhxZ8xvsoH4YdheZ%2Bt5QR5dDuab4iO4kZJEfLZl%2BCDAg2Ye%2FurAX6%2FCEZ%2B7UUnrXLHF8TyMhYuOglihZNt%2F5prCDJwtH5MMnRk70GOqUBdrK20VWxMZbWOdQJS82Yr8CHXZuQB3UmQ646efLLbAGcVb3l0rfHRkSjKpt1HkRyJzdRqiqjipYSpA24N%2B3Glf3IYpZzODOkOut%2FvLTvdFyypkBmWQwna2FfbY4%2BoBiyM16lWs2LiR0eZmgWGc%2F%2FufkuGCdHbRDPx0gcH9xHecCxk86zrciICODLtevm8JrL28zjWOgtnEoZYO%2BFbZCQ7o6JznDv&X-Amz-Signature=7fc2ec0121725100b1729e392c694deb690730855f9620f2ec55db5542ffe574&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VP52GC6B%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQD%2F42OGekunYNDUzbdJE9t5%2BHmxR4pJQC5v5TgY9MBSHQIgG%2BUz0rCjm0%2B0XH%2B6MYex3BHStEqGXu1TcRwiSO3RNv8q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOBh1pTkd6jrw9w3LircA1LxUQ%2Bs8zl%2B4a0Vz61yP%2FFUuixYrnsVDCa2NB6nB6gsQWJ7s8L1U2Lm4mI1UGKaKB1RB7NOO9Ar%2BQ0ybTK6zTkNmL%2F4azXIpMfe8PXpVJo1EGO4Y%2BSxPGgyuAZlvCrdQCmlTl8FKPCS%2FXYQFUgVrSfWHboyVv1jqAzJ6eXV4ZQH5cfseCgsOkhjWULjEXcMnedeWZnqF0b5%2BPpnCVOD6fO54YUNcKxP0ETdFhpdoZAguPyi5sswKFNj4gcWEmiYlwjA0B8rT4Vz82v3JJF6Nb7SMOBa7xhGj43Y6ta5kjwruXd7HSPwB5jxsqpd%2BOrh8ti%2F7oUfDujkGi1jihxkh1ahlh7CyQ%2BOQDlqcdh8EHC5U3U%2BnEo2gAdcgAwYVKVsGooocUBEeJZLP5isP41ANvso%2Ff%2FlL5qYsZuC8oGMlqhUW4ytmHW51BQsMIRWoKIBHISnEVykwv1GF3%2FoO2uzobdbVhk8ief6Fgk8hocTK%2B9PzFn7dTPJzyrcrb4lwb2Yk0GG6A2Pc0hIX7olXKHtGxwf52TPnB16vjEl7q%2B8V06WiJOVe%2FVE1V8A1AmeG08a6GZhKdqLJGouypWhodmZLYz2PnYr%2FdNmzyddCyiX5A6klNkvwLOrAKRyykOzMOXSk70GOqUBkwvdDDufy6GB%2FbME9eOgmz%2FgCZpWg%2BvLzZ40%2B%2B0srhIrmhdb%2Bcm%2BQ8FjSu5wBd5JnrclnNQuCN4b34pVuK0NFgIr7kz%2FcJTbvUxYbPpQ9MqCPOj0EphBZNEEDlUbEspUVF9%2F8UQShPpZT9tZnhot12U8R5w7MGmecguK7j2m310%2B1kG3IrdQ6teVuTz0w5cmEILY7fBwgwu5KbTBKLXhp9jNMY95&X-Amz-Signature=e67cb4c30b947681a28289390edb723841f8b166b4173bbb62f5e8638e49b542&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIBUN554%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDIrambmyN4ssRAeUrnK1qkZUEPIs980QdhDIs7aberWgIhAMRwzgHYL2CYRbFzW%2BBgBQvTIMCDKGLvqpgeCkAmUB4rKv8DCGIQABoMNjM3NDIzMTgzODA1IgzRuB5kTWjnsj7FK8Eq3AOUyjjUn9%2FmdH1NFwrCOrU9Zmz%2FUB5AE3CsTBeT57a7A9EOUubYhsAXcpvXY5BFNjeq6VbwkSJsGhsNNhRXg%2FNzRFI%2BOPyWTtSTNT1fgQxx7AFHIGgqSVJwEFMtr7P%2FB02IAZd47PsiIiJLWaobOAyFEzSQQ0IKRgI3nBl7W6A1OkuGnsEgt8eEwGR823g1m4Z89apCsExZ%2BOqVSsukS%2FJSMvOP7kvjcuFqFr3jy7KOsQPhb%2FSXNZ06yjlJf%2BtpAxvmF4xUOEnfjJ%2F6pq7nEJJb4j2aRkHptLmQJ3oQ5D4jHm1jqR5ey6H18TtxPatBWwokjrfl%2FMEar97drqSLPILPDsG76k7%2BCWXSy4RQIt6tns4Foni5WzNfWyppuFjGBPzWyqvRDgdwoe6HfVUKUylQyBk61VdTjIkKCs84piDyNgmmkSBR8jcvC13ZQw8G7J%2BGZy0pKhrsuV4GgaJbzHNdgQwbv62Z0Yp3bxXVzjtZG99%2B1e5bZD2cr%2FT0QNjDPcc3eN6eJXd2Js1yINRplJnP2NoWMBCjDXBRNDWaAQKHPv5Yjq8iBQpPabk%2BUyZDgF%2BGlpU62qckIYjwVEi7ezIkZ0JLw5Q26WOVUkT1KKxWMib5jUMtniH8SI3bpzC00ZO9BjqkAQaNb1rxkWMV8Xkw4%2B6UeWgTpExXq8tVN8Xkl%2BoJfvgTSGnBAkuzLwTtWyMdwHm7OC83UXZXWy0HoyYED5y4Cy4Vfg5MylXCOYpl%2BedoOEln6U9Sh0CHwI%2BuP8YEV1ueWhkI%2FMl%2BRH92EcRYqbMWEurn0Q5NVDVyw33yH6nZP%2B1BKqZ6xaziFS5AkF4JzlAagCn9v3PYGTgGV7IelIL7Qsqo2v%2B4&X-Amz-Signature=1e6b15edf288354d2451879c619d54415c8400621cab38e81ef8fa0d34f24b9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIBUN554%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDIrambmyN4ssRAeUrnK1qkZUEPIs980QdhDIs7aberWgIhAMRwzgHYL2CYRbFzW%2BBgBQvTIMCDKGLvqpgeCkAmUB4rKv8DCGIQABoMNjM3NDIzMTgzODA1IgzRuB5kTWjnsj7FK8Eq3AOUyjjUn9%2FmdH1NFwrCOrU9Zmz%2FUB5AE3CsTBeT57a7A9EOUubYhsAXcpvXY5BFNjeq6VbwkSJsGhsNNhRXg%2FNzRFI%2BOPyWTtSTNT1fgQxx7AFHIGgqSVJwEFMtr7P%2FB02IAZd47PsiIiJLWaobOAyFEzSQQ0IKRgI3nBl7W6A1OkuGnsEgt8eEwGR823g1m4Z89apCsExZ%2BOqVSsukS%2FJSMvOP7kvjcuFqFr3jy7KOsQPhb%2FSXNZ06yjlJf%2BtpAxvmF4xUOEnfjJ%2F6pq7nEJJb4j2aRkHptLmQJ3oQ5D4jHm1jqR5ey6H18TtxPatBWwokjrfl%2FMEar97drqSLPILPDsG76k7%2BCWXSy4RQIt6tns4Foni5WzNfWyppuFjGBPzWyqvRDgdwoe6HfVUKUylQyBk61VdTjIkKCs84piDyNgmmkSBR8jcvC13ZQw8G7J%2BGZy0pKhrsuV4GgaJbzHNdgQwbv62Z0Yp3bxXVzjtZG99%2B1e5bZD2cr%2FT0QNjDPcc3eN6eJXd2Js1yINRplJnP2NoWMBCjDXBRNDWaAQKHPv5Yjq8iBQpPabk%2BUyZDgF%2BGlpU62qckIYjwVEi7ezIkZ0JLw5Q26WOVUkT1KKxWMib5jUMtniH8SI3bpzC00ZO9BjqkAQaNb1rxkWMV8Xkw4%2B6UeWgTpExXq8tVN8Xkl%2BoJfvgTSGnBAkuzLwTtWyMdwHm7OC83UXZXWy0HoyYED5y4Cy4Vfg5MylXCOYpl%2BedoOEln6U9Sh0CHwI%2BuP8YEV1ueWhkI%2FMl%2BRH92EcRYqbMWEurn0Q5NVDVyw33yH6nZP%2B1BKqZ6xaziFS5AkF4JzlAagCn9v3PYGTgGV7IelIL7Qsqo2v%2B4&X-Amz-Signature=b262d666f47f4ec949fd52801b3a588830cc212c7e9cb55f530e7d988e0f7c56&X-Amz-SignedHeaders=host&x-id=GetObject)
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