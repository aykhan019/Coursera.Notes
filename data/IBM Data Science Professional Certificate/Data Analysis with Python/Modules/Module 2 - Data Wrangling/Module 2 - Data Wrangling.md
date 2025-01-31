

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOMC552U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF0i1yf55MO%2B%2BA3XAqwDJwdpGWcx8yyvfTdrrTpqBCnkAiASi4egovF9sQi7x1m2gWES0Etu%2BtBRpsZgnrfgBRisVSqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH44hiLRgFZdcpL0uKtwDOdbRgzjnaInQhHnNzDPgIT5KHqgIhcvDoz9RtgP52j%2FwvUObrz7d4HbdS50BXfHrbpQyR1lOts7C0EDb6LTqELa0G4pArEGQYZ429ythc150lSRZEK%2B1et%2Fn2VKGE7jdSC8xN2EN8EL15dHmKBiz55C4Vr4PaBsR8YuATNn2KveP1049cqtexl0Bgh%2BznOu%2Ba1g4KY%2FZPSNwAZBLHERdDm33Eo0b8aiDHrQhMSgOGvD7NofIQUYYTdBfJ0ruTomLFoz6G7CT1%2B8pkR0GuoyKf8Kohee9ZaWE8Dr08bW6p0uAqmYKV0PNdxfLcAmpRoK6edkYOHUafLtMr64Dvl8HeTCdFkeTdHIqTE6lcICruUu%2BvLNZDYGDR8P3mosW1E9aGYUKlYaD%2FdDgdmQoUJolB4xu4M2enG9ChIfnlntraG7MiOQENrOzgys67fA2UIVxBly7MeXCUofkWCLj0I4xT8GATpwrF4%2B5NlFN3z%2BAhTQJtja77M0az80Bd9weXebJzFQi98XrnMrcswZIyx6PNK0uyaAQOKO%2FTI69J0e0r7KgIb2ntAz%2FmP3EEPfS86g7uzFwS3ffJKzmDgs32A2h0LMVbORf5vw0%2FaTcET5GAPsCKizsgkTf3NkqXIEw%2F9r0vAY6pgGFq6wGdYs9GEs%2BaXZTyTcMMPa5u2zoGMVAkdgqD6YChVI51YL46I7CPUnxfRLRelncviKFC4jeCLy7Uj7pyUy0K%2FxIBmb7yasYmk1bFtawb0dTJ42aKDXY6EsQ7tovH7Zwz34B8PIHdtbnHhjYs%2BgzlXqJPMXXE3RmDUba5PEtyOINAv1Myf%2BFeutESupydg%2FH2Jg0M9HbbJSZvYuFIUxHe%2F2OnJau&X-Amz-Signature=229d6260973b2af17d30c23270c80861a2d496bdec22d75bb7ce06a955525c5d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Y4L3LNR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBw%2BREIBM3AwzOopEApYR6oEUWCAfmbxSzHJVWPOMzjJAiBjtuw3gqNyjduN3yf2MndddH%2FymP%2BKexxfkxUpGfsooyqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMalEIMAJDIjPx7oVTKtwDvBLxpz%2FZHPb2LizcGEFgWWBqkTGUSOO90QNn8RelQqxEKx2OmTJLPFybR1b95XnDjw6NHN7OowWIUqFq%2FDEuDX5bE%2Fozvky9QsVfDg%2BJZNlMGCiC6jdP%2F8xY2YYMrzz5Q6nYEFKdEWurHJ8Ik6HNKCq4ZLTaTimlvScZNblL%2F5uJhLyE4yb4gBKfMYz8aKJohts4Mx2JP9rN%2FJRIfHAJLM3LeofozjJgeKcYv4OP09ISc7r4Dj8QZHF5REoqI0RKy22i1zRHXsEh42Sa4PKnFdK%2FKxgr1p2n8jc6DDVwZGvsBtYvo%2BtGTpCDxYmMGD%2BpPtmCEMDbzedZEQnb5HLcwycpowiyrOFoRl3D3BESl025VrWVCZDRC80X62yf5GbHIl%2BhFTL59L1lhOeYOPWtJ4D4honsY9QOvCnrHVR6%2F8YiZsPfIte4B3YP1XVrZraB2Vlv1n4oTB8gNUPqaISCOGTUHLEIjc6Cw3iI5SC3bEsGtH2vRfnOpuiUjFnTiaxL0mDhMVnfdbMJ9EoF31fA8xD9svKfjaKZSWQcNsQagVU9P5Xb4VfT%2BV2mHRWV%2BAb%2BPT5nNIwLJeF4vCn3tjVLnE6%2F9Qw5hKJ0m6hcw%2Bu6JiHE1gNtx0o7zhitGC8wm9v0vAY6pgFvsLPAQYAcKNK%2BwOJ1Tw9RA2EwZdPPQg1fZlKtftDxNXpcFRcxjTJKDvjCgFaBcqvfSEVZT%2BhTmsLmGilf4UMzQOCxPcfe2I0gHQkMSiIyYzsS4ksywXozoxUdIhgc%2F5THoK31eNMp3tkusThhqEjU%2B2dV1mSqSNMtb7z%2BikEneuDMY0nbebE2K4LjigBVFjkysbya2F49PXZmA61X5MN9qbw4Jkfr&X-Amz-Signature=05a457d99b2d01bfc6abc47c341f0c2ec44e22d983c2f29b2a3ca3d8960d8f2d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWP5XQM5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCjXcszSEvCWsFuHnN%2Bt4qMU4HDQikznAMS1xmuT9zqXwIhAKDYVg%2FffAK4xqQrYPP7gZ9GKikWwy4eeK6BP%2FulvwBAKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwft5sodfIf3c8awCIq3ANp40pXu3gnZqlw5xDGNAXaLsKuSUZn5%2BQ9kK22IGk3N0PdpkCIgnEa5i2RVKJoT6G5T1T2NVzxtrd4pZVlJquVEfGzDIZOqmE63MngsZbDZyKRbucjgQw%2BrrdblOhjx3jb9yRE6g1sGPOps4%2Fluw6TFQv3b%2FtP3GqEw7AlEkgASm3HlJxsMcbIlSBoJ%2B2erv5d5hfYu0NmceeQIpM55jT8eQMp%2B0Z1UmD3jp7kDn1JoS8D2AskM569K7EPtWgIWWfD6uagcB%2BLNRlCLILevjVmIXURsSUdOqEvzwYiG1W%2FGRisokJ88fTHwP3rpqOtQ%2BrGQ5uxnsoXuwCfddkDXqlqVjKB0vE2ycssfe57SaWRfppyie7OjJNmvBUXbGi6C6m4mikiI6641SVq51sb5QUHzeIFvs%2Be0ODvClsvrs4rWnrsotwtTOQ2SLZiJWiKwRY8dUf66LGOn45Gj291ldoFLz3FS1lwcX9kTZ0JsnXxD8E2Qykp1FSBZiyCpCNqyhrkuctjNSc2hl8OiJFH9rs3%2BIgIiXaLJaRHwpl%2BAJrk9yF6avZ1t3KgVLxK4cqD3PNWFdCf8n4rObK6%2F4f4ef0uUPTUiY0vyb7zop6P5ML6mtDI7NZu4vkP3n2u0zCB2%2FS8BjqkAdQ7bKTAohyucX7mjpIcEyJ2%2FPgviuPAi9xBMipqmI4vglmM3FQx693GvVDa56wH1Sh5Tk7lJ5yLcd04OHVBC78%2BGvD4MNSdW4psFMZQTf4X1PZ%2FndB3vyBc51rLd0pWZFBgf%2BUgax4Id7sFhLG0OTRxwndUChXKHpZ7O63Z2Ll7i3LM3G%2FhQyerPvLtzlejR5hUe47qo3xqkxpoTOrDHKdXB2Cy&X-Amz-Signature=e387b539d202b2a56208136945561683420076020e1cabfd3b78c836116ee2b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY6B7KBQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCElZpVxaiRtmN6ZufAV1PaVPNumnJ%2FInyUg7TVr99TEQIgdrzDvN7sd4ZFwvDFnlAkqMzP9Mqp0GmZZUqAJDSN%2B08qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK6L%2BGX4tSAzJM6JyyrcA07MHxvO8yJE8ZtkJ4vUSFPVDsIGUQojTCM0nhXwOmjk%2FAvWrcc0lGV8PkfIX3Af3qrOIOSZWOUOkj1EhanbtK11Uo8d8EV%2FHifUGdn9%2Bs%2FoNiID1U1nHr2HYFSyIYn6LkqRfyeAImUjdqYa45iBnOvJId58%2FqKil9eFwcY3ELWQhXoXsHoNm%2BBJcT0cLtWt81vP9GgtmfWVgnT%2FxDQ1AWWemx5jQYFK1n9FhJ6BQ79hwf1icNbSNTeg%2Bf%2F%2F95K4M1SFWTB4L4H5wqo%2BE0AFd0MgndxUaOk3YheQN%2BiWlJ7rpntNkF6pCLRAb74KAUx9tVOILNhoF5VZkWMlDr6eyb1VOCR5yrO53FxmZgXIg%2FarnWYsPJK814vdn0YdvrnOm55kc69EYTWf72KSuoThZfzZBvTbJMbZjbfhAhlXfSsu%2F%2BLN4tpALaKHypqg8fEu2rBJOBJv2GEQgUv%2FFdafgdPhx81wbdmbIdE108VsGPz4Dibww%2FBT8cyD6fhQkxsA7aX6%2BbPFdsuy1Y7WW0GhsdJ7%2FjC6CgBACHoYCy11ezMT0ps6J3prQDnuaj2eOEYky%2BwodsbL3neXl9pH7TS2tP5okHTt7dTFAw0YWEJUFk0pRqb%2FxJ05pa7mPu67MLXb9LwGOqUBqh76vBj2H8D5VjUa%2FPLMVSe2fCNt1y%2FXSqP%2BtD%2BAHLs5dTw5NnBOSubupHIkXbUWYL2F2JlffDdnKZYOeDrtHELwUfJ01b4VS2%2Bp2xTDb6D5hiBDgwpRQm0K9ueX5%2BkBgP2yF43miTay04%2Bz%2FBi%2FWZQLkVVDV4JuLdb3cI9UtvV%2BOFtJulJYZurhbW6Q1887vbmC9v5ORfjVUA7nNjhkQ0phzXBp&X-Amz-Signature=3b8c242f1cb274661d4ca3db825149f4f9715f94660a0ecc69154e994cd860bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW26S6IE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjBbE3%2FyV%2BlRhc20bOqPvi4SEHq7Kw3BYkFXZimyP0nAiEAv7HMb27y967mnPvK%2BqPv7prMf16W3UHkVjLTMis2HK0qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH%2FsCtKVYyWIOHfPuCrcA1WxPiO63vJxPZQ0FozF4Ubl5n8KAcHOd8VBxgAZgpbdaR7wJVz4FM6ga7VAJ0LmEOqoe6Zy2HkaEfE3Y3IMMh4thnp5nUkp0eH0X7nJR8OwET1pokKad9hzYIzvzkjwXA9sRca4ea74jp%2ByGgxk0geN%2FxG3qdb%2FMTAhBK2kTb%2FxeuLKKycfzYikc4G9N0mFctVPp%2FTUXV5x%2BbvN1F4cAUsOZ1D5AbBq4kASM%2B9PdjSVrSlObZGpg5TXHBdPIomuXXkFIllns3Ew1cWTGCNlwXirabydQayrJIjOTE8LMXWqObIwX273GEbVcWTpc4REinX%2BrXdImJXqSlNGKucwrv2k1osGj42VLWUNxhdgR%2By5Sb6wGeJu6zqVbohLzm5cWs1cHjZRaeusk%2FcLEIFuWy79Ia%2BErh%2FpYBxjj2jzdHj0omL0MYj5tibqxMG9D7tcL3UCLNeyRYmMHBPKYC9zMPsCx1Gx6IGGrn6DIetc0dOnHkqb6xCzC5M3ua%2BKyXLDa9zWQbeOu9DPgbyhYv7EymHVER3lSrpxM3XVW5tJrJUx466Xft1kkF%2FU4%2FuaA3BVXj67ofbvvVBnTGTUGJddlaXtD%2F%2B%2BvwAL8zmg%2BmSvBK6VN6HJiGkfEt7q%2FHxjMN%2Fb9LwGOqUBPn4oynkKf6GPWhxcbcBXDb1LgM2vnBRVEwhoIILpDH6RFfBIxq%2Fd4OadoyxPqBdhHsYQqdtC6HrxrGHykUEWwXLS8HUaosTEgcTrbdVp%2BTjSP6%2FYEEhnWg90VGY68lSGkyUzm5fPAWoRDWEConMykU9Oiz5RWKBW%2BeJohHurGp8E0dgY4HjhlS7OtbPqdW8dQb96jRUP4rwR3oJqtvdFlICvyMPz&X-Amz-Signature=5549e9f1375cfa40cbd90c04d1d31e8a313553f76e62b3a7725431d9ec368a01&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB6ACQP6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmvhCe2SLwFbbzpWajDDT7dAVSrEo0NYevWJY6MBLFbAiBOT5PsIDvCf8oWLy3tTpcmwTjGtLyu8Od2bp%2B49kwvQSqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCUsxtUUNJvWmXGH9KtwDI%2F3kHnQD16yI26KiwDwe%2Bj6GrHeJh7yeojTQjWJfFR32KBQB4f7ZCVQHT%2BpxU5gVE9pS%2B4QzO0iPmWKcDby2LHqFjrGhSFMJgWhsiVVrm8VECz12%2Fn4VR8tzqZdAOv7uH7MZO869U%2BReaXuA2Zt7a1WIsS3TWXLXlM9VjZgDN%2BZ5xe1SfxhH%2BzeMACGTkHk8GbC9NCrXhulLttQNPj0jVd3NRsFeEwB9EElezJpcGQO38aMSr94KsbCcYLYUj2ZejjhoSQ0xsz6pIJK6vkxXEH2r3LbACv3KlBCOGfR428Ahyyz1gz08hSM87MOdc3vG0%2FF1SeQEGHcpCPu0Zx3iecfwuCKA6dYFTlcCLTsOgMYzRFfAwu3EfuTl%2F5e6rqwi4XuV8Ogu1aMppiDDkmnMuqr%2Fk5M%2FoXTyU3TxfZ8TG0oMLNvMskU%2BvxfR0l8Xn5lggqi9mzGJUcs%2B5hP2MyVmbeocrQ74RAdJ9h7f6qhxiJPsmKEsOiHt52u%2BWw4oqaZe2PGJ0v2TQ9%2FmZBil8Htt5jTPjmHvkc9tYaWTnEfBvs4iMl3sLShGE56AkJyBWMZs%2FG6rcil%2BF3XkYPiQxpMOuCnqc5k%2BhVrBnqhaYPJY5%2BTd2jWOpyWu1S4tSzswv9v0vAY6pgGgj1ea3XEN%2BS6GSjJ7uwWLCqtlKKOO%2BzBHBVkhHeVQyk4bex%2FwX1zR10RcezS56ELSaAg%2Bh%2BHNp9Ypfi11y6F3ej2kGBxLhaYQrGGZAzyOR%2F4vIHG8had9xMaBGGw2bIxNNaC%2BAdMNIlrQaHo6LCM25qNNrjxu1Dea6K0iupycHxEHBUKAbFGHjkorDnoJI4K81io8ZFuCVHQ7Q8JASx3TpuvPVPNl&X-Amz-Signature=41223579f85d216b9280e0c91daac637684dac6de368003b9430072498cc782b&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VI5IBGFN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrVmJn%2BPLOLhrXXuJIjzkNXPipBo0GZcdYLvygIz8g5wIhAM8vX%2BQoGasGd%2BDFTCOqP4JAn3WiKIdeLWMbAIpYWDF6KogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw1%2FxQkqXsMXVMmcJ0q3APP6sJYCPV0GlsQLUf3e7fdXSpB9d859WV2DaOta4uOsi%2Fq2eTn7dPpR30IB33MisHPmsd8oTeU28wkCpd%2FrY%2F9VWXEsUMrTCNc9iY4f87N55DtfPyMrotDSmuZK7QHmUeKlZ5H21sYSpaDkE2RE%2BwlM6eHv4OSRKb57sKYLAA6dejul4ei0tnRkQNafuBOhkoM6wkORtR4FrrI3iBPUnYEEtwK1vdO16dYglrOM%2BOd0PkWJkNe1cwOhG9BqZcn6owwLnwHioB2Ti3Pxo4lz11r5FfXQxpjxA3n5qgzKcLk13hRa8ycnXYPJV%2FW0NtVXH%2FT7c%2BDu6UI77NO2J0OLFp7B0Gz%2B75lW7idSuosIDWgLnaOI28yXJ7xO%2FaSILNguRIX8%2FtuhA4p8gW4RVC1nJz7eqR8u4N4bs%2FMJip0XCLxxtuBY9ZXk%2F0DBKr5uJGL1IPYyTZwk4O9MDmSl%2F6WiavxE1d6Xd9L4S3o65ZuSvW5%2Bu5OXdpTVFv1nCYlOk8JzW7bj8ORQ7PVyumYdK9RQaRqZLauieT53MLTPGwnhOIuQMcSUq%2BGMtExdvH1JhREK41L%2BqpyM13ZH2I0t4kvDgM3M4%2BofIusYNDZ50CG7wk3z46ltWmfDlBJhRu3pTD%2B2vS8BjqkASxY2YN4LSaiR0wNM%2BIkzBVPP%2FzZmssB8SJjNFur1l1JbmiPHsSi%2BTegFbcUxJF6DPXG58MLZyVrgkH%2BFqWHf%2BoBVVFRChfOIoL1EuPPMIlK3gdC1NS0Cl8hPnyzEvY%2F9YhS2B79yd4glXgqmBAqbDAe4%2Bn6qlprTN8rhfADGkkIeOGDKU%2BdfuwdVT%2FhsKk%2F3EKHE7gnVfUiWpiNnVUwKWUPAIDI&X-Amz-Signature=aa92df2727d4b1346c3ecaae44378979c73c48056859307107f82e1a10b24efc&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDYL5CNH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvC%2BYigYzD7aknnqfn13O9SKyVtE1of1BVqz6D26tGVwIgDpZ1ZeEcKFKnxzFl5wEgegAieOVNGsIh2jI9rs%2FhlkIqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJm%2B1y7%2BVxG1HWwSpyrcA1XmNsOcIzcLZqsyb0x%2FEKsFGS%2BDxQonfSzZoExTW3XWwZiV288%2BvFe15qxWSjh03n3nnov%2BlG8HwOoVTUYATVwdKkBbfESyaC%2B8Sy1XcjOmtXdPCsPJb0mye1g%2FY8D5Ar%2BvaDGhk7QrxGfFsZ4YHAjFFgvxoSjcuPKNO5JbVp8BQLw9aPgCOFrSiSmAWMCnFRGyC31AZb346uleSF%2B0uvDUt2Te2web4Xd4zUTE0tHWIs%2FnIo%2BIe5gq1X5g%2BVcJHnUDG%2B7NmHjp7qLysYWpB2n9qU%2FZTHpZps4d8N7dYGaknvgeZz8LMdR2eobgXvjuTb4prmcz8o9TyQNtytTxUp%2FNA8nG2jR0whna5zH9G%2B1glML9tWNmvLLZ31hG5ZFmPRNhfl5L0EliWU%2B0qQ%2BC6SJggp6dBeEnlSnEB4P%2BbZ79jqzCJVcmfJrDBdTGTAOlUehky2qq%2B8FN6kryi4WvjukxnWYpQI8kq93iEkjXn5RxehHDda1im9fW4nwkWpbTn9NZAk6PvuCqpu%2FBvejZsh9eWivofo5%2B4gDf58QrUIsh30oyBZexFdevp1Rs5tVM9Qjurr5cZXW4u75cHzsgQaru%2FWos4f61RRA1DU7KmdZz7kZTLNP8s%2B9xoju2MJ%2Fb9LwGOqUBdSa9vWP3YA0aKDu1Y9B%2FjtKlgIQDKIqTRAsKSc027qiQlICeZNOYumRSdOvdcNF3FjP6na7NMEaAepFdmeiV64xLFCR%2BMPnMEt8coFu4iSZKxSWrAS%2FeDCl17a0BrkZca25s0wwYFUIEM8t%2B8EwlRZJpkePSmtOb0GeSWDR1wBD5gmdFFkX%2FlS9BRfEh%2Fp4LpSR6kz5D9TaFQQ8uw9CsS0C9aZub&X-Amz-Signature=bb57b7852061488b4232d92ce689c331284b92351051f6624c67487b5056e97b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW26S6IE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjBbE3%2FyV%2BlRhc20bOqPvi4SEHq7Kw3BYkFXZimyP0nAiEAv7HMb27y967mnPvK%2BqPv7prMf16W3UHkVjLTMis2HK0qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH%2FsCtKVYyWIOHfPuCrcA1WxPiO63vJxPZQ0FozF4Ubl5n8KAcHOd8VBxgAZgpbdaR7wJVz4FM6ga7VAJ0LmEOqoe6Zy2HkaEfE3Y3IMMh4thnp5nUkp0eH0X7nJR8OwET1pokKad9hzYIzvzkjwXA9sRca4ea74jp%2ByGgxk0geN%2FxG3qdb%2FMTAhBK2kTb%2FxeuLKKycfzYikc4G9N0mFctVPp%2FTUXV5x%2BbvN1F4cAUsOZ1D5AbBq4kASM%2B9PdjSVrSlObZGpg5TXHBdPIomuXXkFIllns3Ew1cWTGCNlwXirabydQayrJIjOTE8LMXWqObIwX273GEbVcWTpc4REinX%2BrXdImJXqSlNGKucwrv2k1osGj42VLWUNxhdgR%2By5Sb6wGeJu6zqVbohLzm5cWs1cHjZRaeusk%2FcLEIFuWy79Ia%2BErh%2FpYBxjj2jzdHj0omL0MYj5tibqxMG9D7tcL3UCLNeyRYmMHBPKYC9zMPsCx1Gx6IGGrn6DIetc0dOnHkqb6xCzC5M3ua%2BKyXLDa9zWQbeOu9DPgbyhYv7EymHVER3lSrpxM3XVW5tJrJUx466Xft1kkF%2FU4%2FuaA3BVXj67ofbvvVBnTGTUGJddlaXtD%2F%2B%2BvwAL8zmg%2BmSvBK6VN6HJiGkfEt7q%2FHxjMN%2Fb9LwGOqUBPn4oynkKf6GPWhxcbcBXDb1LgM2vnBRVEwhoIILpDH6RFfBIxq%2Fd4OadoyxPqBdhHsYQqdtC6HrxrGHykUEWwXLS8HUaosTEgcTrbdVp%2BTjSP6%2FYEEhnWg90VGY68lSGkyUzm5fPAWoRDWEConMykU9Oiz5RWKBW%2BeJohHurGp8E0dgY4HjhlS7OtbPqdW8dQb96jRUP4rwR3oJqtvdFlICvyMPz&X-Amz-Signature=5f2e2a3a313a21084e336352dc0ef9ebaac73e27070e56e930d530cb5db939bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ANVEZOO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZVPYUOVXo3u6UFLt8VBJSn0PvTNkQaxgxRI3HKfNdjwIgHsq8sKyVWI1gfDwLync8UjomjgfKaYbgB9Kz0%2Fm7TyoqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIwWq6bu3fwjVgEAkCrcA2cdM%2B2E4OgebgTrJXeafSiqlF5C78l8AftsyDGvqVBzUu2xA87XYN7jDcK3oWLuAaq1NJozZ%2BtCcsIPuSdOXc606ltrJlaDw%2BVgXnYk1hom7%2FAxoEnqBOA%2FeeklVkFu3%2FHPtw177WmOLYxcqONaw5b5nDtPH6IJFVIi3RbOOrQSiUgNZLcbd4bC%2BK1rEwhLqTpqAq7dVJqvd7bLuVxAyrKW9WLihR7RmB6O47pydi%2FEqmfvRHvcXmzfxkT%2Bm0UJZtn5SS%2FAmXUYWBvxoARovWAgRf%2FZDo5I7gWJhmHTJRoJVBrzfLgdVh7oYEzMFcvXehivgP4cET4iT14jt8ZWVXscPm65AfdhZRv%2FmD%2Fiah8OZsa9ninLWe4dBykgfiZE6N%2FrsaVnPQX9l3tlggYpAATcmRSLr6tAe%2F4mj8kkT7nDcXU21box2Y0eqOlqyWC1q32u4PYS9JV%2FExdLRc20btt1BC7qqc5xAHKShtZracShuWu8W7MNGl422wYl%2FbK01C0f5rr%2F3gkBaG5D%2BIvHRCXK9rAX7Y9KwjEhwBEujjN%2B5btDzWhCzJkV%2FIPGjhm8OyyRlUguU2%2FyKT9OPbb2o3%2BYeJSXrrYNpI1Cd7fExXJOsJXB8NLh2krleNA0MLbb9LwGOqUBrHvSYn5zKjqOUczwhXemJAnxI01fwA3pk53%2BL3YF425fnPREamPTDC1pWh70VqZkVMiyPWGv%2B%2F6%2B5miecN6Fl3YktuuA7eAY3869%2BjDuyWhVBvNB3YEyglvSKpEoLXKLw4HuIsnOgJxBcV%2FdgZPC9GBubgMMbww28v9sMexcKUpoLblIa14M8uwv%2FlGzcS1F1bE1p2eBlqLctxqri4uJRMuW46ya&X-Amz-Signature=e3d49c7ccb404d46f6ac8c7297f7341ed06c19b9c9ae411c384d09c3b0f70815&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ANVEZOO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZVPYUOVXo3u6UFLt8VBJSn0PvTNkQaxgxRI3HKfNdjwIgHsq8sKyVWI1gfDwLync8UjomjgfKaYbgB9Kz0%2Fm7TyoqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIwWq6bu3fwjVgEAkCrcA2cdM%2B2E4OgebgTrJXeafSiqlF5C78l8AftsyDGvqVBzUu2xA87XYN7jDcK3oWLuAaq1NJozZ%2BtCcsIPuSdOXc606ltrJlaDw%2BVgXnYk1hom7%2FAxoEnqBOA%2FeeklVkFu3%2FHPtw177WmOLYxcqONaw5b5nDtPH6IJFVIi3RbOOrQSiUgNZLcbd4bC%2BK1rEwhLqTpqAq7dVJqvd7bLuVxAyrKW9WLihR7RmB6O47pydi%2FEqmfvRHvcXmzfxkT%2Bm0UJZtn5SS%2FAmXUYWBvxoARovWAgRf%2FZDo5I7gWJhmHTJRoJVBrzfLgdVh7oYEzMFcvXehivgP4cET4iT14jt8ZWVXscPm65AfdhZRv%2FmD%2Fiah8OZsa9ninLWe4dBykgfiZE6N%2FrsaVnPQX9l3tlggYpAATcmRSLr6tAe%2F4mj8kkT7nDcXU21box2Y0eqOlqyWC1q32u4PYS9JV%2FExdLRc20btt1BC7qqc5xAHKShtZracShuWu8W7MNGl422wYl%2FbK01C0f5rr%2F3gkBaG5D%2BIvHRCXK9rAX7Y9KwjEhwBEujjN%2B5btDzWhCzJkV%2FIPGjhm8OyyRlUguU2%2FyKT9OPbb2o3%2BYeJSXrrYNpI1Cd7fExXJOsJXB8NLh2krleNA0MLbb9LwGOqUBrHvSYn5zKjqOUczwhXemJAnxI01fwA3pk53%2BL3YF425fnPREamPTDC1pWh70VqZkVMiyPWGv%2B%2F6%2B5miecN6Fl3YktuuA7eAY3869%2BjDuyWhVBvNB3YEyglvSKpEoLXKLw4HuIsnOgJxBcV%2FdgZPC9GBubgMMbww28v9sMexcKUpoLblIa14M8uwv%2FlGzcS1F1bE1p2eBlqLctxqri4uJRMuW46ya&X-Amz-Signature=5d875bcc43c180f5ead90746d4d8ab915fbff1aec9b4a2e3ea6f3b14a30d9fbb&X-Amz-SignedHeaders=host&x-id=GetObject)
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