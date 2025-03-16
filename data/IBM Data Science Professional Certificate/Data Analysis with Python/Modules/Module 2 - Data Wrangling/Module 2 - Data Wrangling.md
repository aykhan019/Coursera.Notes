

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGODIRZI%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPXjNFyxc7V4jb0bm6Rj71mb4acbXBKDasvsrRhLbFKAIgILBN9LqnOzpCyFazWYPNheqIdVI3Inc3rztHC0GRUbQq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDN2E4el0n5h2RZjQWircAxO34eLdfHXDABbendVzBTNVLwo4rV6AobVdQeiHJSO0yBGQgd19VuTc%2BNJmPrD%2FT3k3plNenGcrqkuYFNnZRj4AUbmbu3qOlrxIMmWhbG98TAqrZsAtnPo5KgOtgZv0itaQQF2KbuSjZWG%2BJ0lCJPv4XDeeBb1tMGx6XgwYw7XTvYfA4z%2BH7K38%2FUJAREma4xfG7YqSSLSQawg9AXpaKWBvhajOjff0%2FN7cx4e%2FW0nE61QSVoCXL08aezvjRzQvbeiY0zF4cIvO%2BOz0myQ5zgyYMY6ppRl7NcVFxoF2V6XHh6icsC1bct9uPhuFzy790J%2BAfQNFhdVxXdHW0j1%2BkVJGZzSyrtb9pM%2Bv4j1uu1nbJz4AbG4xA2k0gs9QcMZbMN0SdpTQ%2BpC5m9j384Kfv%2FrLyRw74RCVlEPcrle62G6AoTr61l1yWRqQyYa3ECHureUZMsHZzI2XnDf3Zg9Wgx8OaIk6hqZOu%2B8f1wb4R0wcVjR9vM2%2ByCj9wvHP5EAM7RehiAh7ZZIy3oOVW9TvpEtvF942MEVTrdyYjs5%2BtW6OTzY%2BSa0rU%2BODvi0pEG2vtUFM2Cxzerts4GdCsz%2B055Coe48YrlIOpR1FS2EHxUA1s2xoB%2Fz5FlHm1Z4EML7%2F174GOqUBcTtt0gFk4Otu3iWXR%2FCyWtzO0YvbIWMmpi2i6Qy1rfoNXXY%2ByGLn6%2FI%2BLed4V16vPD1UgVRR1tmNWEtLPknsqyQtgXAmZVn%2BgKddf6eszgDfagI6BsidH0lnEboA1hdwmMpj5NbosBv1P4IGYjpf%2B61aftij3i3SxL52JuNWQB6EFmW4TOD9%2FBTJwhrdQ0ukZf9uTv4yXAJPIxubjXs6DB%2FGzn29&X-Amz-Signature=0596658dc646d43e410cec3218db35f852207a4e8f979170b29a561a5befafd2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RACDE4NZ%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICX4v6MW0RmmGcPSgcmUgRogkEnQbZCBz9JZHrtfNYtRAiEAhmHnL5v6RHTKQBdtGL%2BiFQeXhSeKSEBKuOsZMdTSdtgq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDMtJ2U6d4zlLThieayrcAz9xtLmUN6YgYUtIBagtnrOKp4QfgeE18wv%2F3UThfjIeMK0F7dRMR83fjz4LdvW%2FBQDnUX9V2KErxXdUzbmzRWuV%2FzX54cU%2BBpiXH%2B9JDX65ajzhWd5qKEH860%2F9R4cbJREJrMxvVEql9uniRPcxXhpZ57mjXFp%2BuNJKRhp%2BGVNkhTTHvi%2FM8ty26m0rv3ypyj8cJpPccB3byqZDIgTByAhVdxeTQWeh6qp2lNUpJa9FApYO1%2FljDUFu88OPZd7GUvIrFvKcaaQ9g2k52WpqoNYdKQx7WN1yBxNDgyKAYBuLvc0NvfNtva9kIeGYowORGciBiKDqYhSXkglfdXJjrZb78V%2Fyw0vbR%2FXK%2B1M21hURQH%2BeIS4KhqG8bUGxW6Yq8CY9N2339lWbvgfq1mh9DaG%2B%2BlNinfMFh1QwwpHjn0bqxtyUb5KY%2BKFGi%2FHxuCdzwMIVzQOkZH9hzN85227Zch1Zi0x%2BQRgPio6QlKxC4mftuXZdoRPafb9Abwq5wxOVE0wrGaoX7mmqEC9Dnbf1w3q6i6waR%2B0t3DqrLXO4RGee8WJt%2BMGuRhT62rA6yp912EW1nxCsBYKlofIBRtRY4XQOccqYCHaSGBwmFBqyIHALcLgRUSABNTVpfCz%2FMOL%2F174GOqUBC83Yh5KPdmsKRUIWZI1gstD2aF%2BsleAUos6H0sR2%2BsbFluHe1GKx%2F4vxWxcQcJ2c5%2Fdr%2B1aLBwVD3lW5odw7S7oOuTVUqEEQyhougmVMg5aN2pP4f9L%2BE8lBM5jYOZ8ZrMALdZBTSYJBLe33EtSX%2BqLLcUflcH9ZlqDZ8S5WMOAaRb9%2FKDth2eYvYNjSEjszE7fBR6iZQE6FCiG79DPNa%2FjHfDZ5&X-Amz-Signature=e0279bc0da25e867d2fd929ca5d9bcdd4ada4c9d22e16dca38ff14a9f3920b91&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQL7YRDW%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2FX8JP%2FONKifWGApwOpFs5ZV1qdJb3Mq%2FidfmVyDoIiAiEAtzVQiZlCCz0ujaAdRtPNtgLPeCZbmnrO2%2Fojxwfx6uwq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDDyuOpK7k48mNi3xfircA3afGgV15QRmbMvf%2F0U3T2XvbIgw1ZE0Lu6cCl%2B7vjWjtALjWvVBaxzIYvEHoobg8agxjHChuLuTt%2F%2FsQZEypVUQe8DSJ40wlorNvIX0rzWrrvvuTgw6irn1Kp7CHkbn84VJYnHFO385T6q4tFSbqOeWg%2BwPvebsOcZHkkX3KD6cakpO%2FLyoncoNfTmhc7okYgniVze3FrUx3aWDWbQsVkhOfmtFm7Jvss4n3qPh9e%2FTwHvv00DY54kHJ9dmlSlrRYreE8fNRFRVvK%2BOmQRfuCXBnhFyRcgKUABiQlGuTMC8SbQyEnCg5B1JiiNyNNdYpUGPQo6%2FLbTbs5WDlIqZgxSnVRekdrbj%2BpTDYK6rr4nEqkVK4IB2ZuabLKnbUKSmbfQ5ggwKMlukDeMVc6f3tWB0%2FpyX%2FfATSS7liYCecqFNCGc31oYkh%2BNtV6qQcRBpEAiwTU5f7QhjDGKQB7CSKqAE6kYWNSEhtvyP%2FP8kTiGLCRSYQNquQoq9bGT8iD%2F6B5CEmsRltxE6tyqyLpR4FjlAIC2X87d3%2F%2FFxw7yOAVnYEttHd5pA%2BqUh706h2u3LKtJ8%2FZsYMngcP0Aquy9W0%2FcqSrAYk2lBa%2FkYzk385efNvD85ur%2FYuz29B3jlMI7%2F174GOqUBlYM45raAHA42SF4yhai5oAJfK%2BMZG%2BEe%2B3DoejDIP6FbelAAOJ4cMy8drdJ%2BiRb7B2OCVNP9ZmnaOpZA4fZ8xX0kylFnHgeHkn6AbYyReXmnjg92J%2B3%2BlloegAkyM%2BZ5OOVmtX53dxVFJAzcaCatg9rESO1ka%2BplnDE3DyzBOOmeieEopSeinHugUh3TxV8R%2BEGUOPQ5kgg3B7lOuahykl5I%2FIC6&X-Amz-Signature=0142ce2094802426aa18486771566c630952eb2c7ee4de1d3cc302afe644135d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SJBGSDI%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBaZlOkCbBh%2Fxjp%2Fl4Kp1ABbZu63Bf0OjDZWMg2gCtcGAiEA2ryzdnc3MAufdFwJFcqSzHxtGWb%2FK79Lp7aQm%2BJ0Adsq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDNHB2mY%2FiTDIdavA0SrcA3TxZDBAzxoEehhSh7X3kDcxt4Kv3JgMzaLCzFUkMcH%2FuxUFlXykckAqN7AoZzh54r6Fh72wOWLGkULge%2FtQg4qmRhpY4yZBdUc6tp92OpoP6sVPKzXkJG%2FCJkJUFuRdoWN9q41ZKZrih2LqvsV6MsXc%2ByT5kXqvMs89OpnKMNKbSPyS%2F3AZ8VQGSX7qYQSowAA5P%2B6O%2BJCdJLhN%2FarJt7JDpoZEGc%2FPWVJjXsfMudi%2BhR2TIpmgvuTVQvPnTnVBrK%2F5pDKIjNUe4rTfi1lj4eS%2B5RFolHeC%2Fqf8x12Cy30N5dQvnkcJ9aFpbtOc2Px2qB7TDMvZLz1kOtzC5CDnMWaV5NykW6ZWLyDJgLzuobn705AKQ3Vx%2BDG%2B0XY8pmYmT8%2FJx3aeEaFwy7f8h%2Flvc3XdsJ8zStvUa8x9NSuEGS3xn2xkNFfceLcj9u59YeOprLDIeD1NKDjjzqVz57rFlDK1FXxI%2FRbMNC%2FTgKnrNt6rBTcIapjIPmfNkQrVgg6oc8u%2BqrvBqf302cmPw3RwIxfgwxGoVXMAOcMQRaAYl%2Bdm2dhX4aMACklRBd9G3Z1WLkCei9rmFyCkZz3uOj6Lc5Jf0TYS%2FtSvZrhi%2FXiYL%2FpkDNq35rszb8WqyYqTMMz%2F174GOqUB%2BD3piyhD4eFg%2Br7lO0pLhcNm5YoEb52gM1nybXPd0U%2BFDsn8FESAnoTXHLZJCVGRaUmydPQXVwaTfEoOwSQx26myyIr%2FsT3hPqZa3BArdmV%2BWClQUsctDUc4t0bfzLTv%2BOG%2BDXWi2ahleorbuuztIzFyTSA%2FW9enm7spwq8L42sfm%2BPE1kbmK9pA%2BZWHhqCYhTOfQYac8UNLp6BccSObd3tDklzV&X-Amz-Signature=e596aabc815a36fb4587f312309f5b3e2c282dc5e85a5ca2e9d85222c01597a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZPKQ3N4%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxdpM%2B3M4RDcYTQ9xItO1iY2%2BOP1u5gkeevJl45y150AIgbxZgNaO7YHUYwlXhDU8K1YwXldUTKZLqp%2BmQPliIXx8q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDEKmXn39UUj2%2BGuLqyrcAzkJ%2F%2B%2FvLBO%2FAh4OZ98eL6jmIEcOgAwSZRWZDC5tsv2IdPvO%2BMS9R9na1pqJI%2F%2BaeF8sfY3LUVJFm1yjRclby%2FX9GGd2z07BhvQrELhpOG9vXdUKaQaoIDwOgnpt3B8RskbQX%2FXqIP3Q2xkQWsGQouzyiuQBxOB%2BkSFFXPX6PFRGWrnaIor0akmyXns4wWO3YaP8ZRxYahU9LgZG1j%2FqnEIURy4i0ujGbaBKpjwFEZL0OoCiAwrEgQx5wRMui4KTCYJ%2BTe8H3hTxxHXqBThqbhEA0H4naT7gZVyb6W%2BtElLfm2X%2BUnWNdsOG1qkmG%2FUQjbi93DVz08oY5LCqO05HF1Ohaqm6LQQBH32a1AdA1Cp6c94xu708jhUf9LxTbRJQNq2W6b6Kk1oUpD%2BpzHoXlWdr88lUEW20bWpuRiY0QK0kP3RH6rdN3t9PpMQLxiMFvpIDjHe6Iii8zJLOETKaAvVFGU01nnGq6qZTu2hOjqqrrhUgGE98aODjphbB0CsMyvCab5mygujv8PvxZlHRSWN58Nu8TljHgiiHuaIjrBTn6nT8RpQcn4B0zoQNTbwkKTVZ76ZsoaS%2FMeebaVzuS8Tk3YA2Qs0Zay9FMR0mcvk8mGqPtoxCk3pQWcSaMPn%2F174GOqUB4SsVBlKkGK1mwBVeuY9ploqGMHBTq1fsqHtnNSBws8OygvCyapt%2FWHpfLPYIIx8TbFRppIZhM1aaVNel4f6TZc%2FtK1Ke9WeVmwz2wudZshD53GxsR1fnIdJ03piDlrLwxJQ16NMfrve9h0Pg5s8RVCMLSixeh2kiRka29erdWJaRRalyftxgPm8hgFUDXsrq%2FtGKm4XQhSlLSwXrnIQD%2BYtbNANN&X-Amz-Signature=67b8088b253def28cb83b148057ab2d507b17a4ff076a87476158ae285798cd1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622YD6URB%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9ws%2F6uwaPHuDxKeOc3%2F9hugQRsOEKDEjzT33AUxhARAiEA3EB76C1llVJorrwjADf0%2Ff2UR73WT59IdNpOKcQ7Pugq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDHysc0WfIhk5YQMssSrcA8Ks0Jw6CsBdkGv394Wigfl6T%2B535Uvxu1fy2c1GgZmB4WOz9uRCNNNvZzzqt%2FWWBWZf7yoltJ4NiX68pEOkvZsquGN4Fjecm96GhsRceEuGsCrYRHHC8TW8jlDM9DpMuTipx7F9W93bKyOloIvdnlcJxi0OwJsLPj9TRh9P8wMmPKXNg6x%2B77VPTd4UrJ1VabXvVRwXE4HPuVgcEJ2OoqcqJ82WlnwCU5aOjvdxo1%2FTvFDZ1l7FmR5kb%2FbD%2FWNYDFPVpKniKibgfvHls41uLtrywprqGtcnd9ENrBUsAx4aL%2F8LfT%2FCsMDgveA%2FwPTTXzH109qY%2FlILULiqbVnyEmjDcSU3Km9bKlr4fSbvgcb1T3Kwsdb7DFBzEhuKn0INMmVOiwWV5Ji3Is24R8%2Bi88TrwhYGZ42xh8JLVGM%2BhuzQWsw3plf4paQGB8KLXz6ycEZpqLY4gzgBqbR5v3eBOHzJBMpDC%2BXRtItP2oBeKj7OaVuZMoWVtc3qpKewhIyJD1%2BO%2FduYKDRci3g9mMXURiY50sB4TRxQOg2Qv%2BtZX7A43oKvRerQ4au6z19kuqtyZKBJE7vjossvz7oSVe0EVXgpjdvwLhM%2FSM1TMfOFB94YndHrEY78MHVhOMDvMIGA2L4GOqUBazsmwoQHeffeasbOPtVk3sE6QE8o5UOrK3KLijGZQdNDSQG%2FR5YvC37eHpkpr2v6D7VYz1CBGwRnypgur2Xu9nXsvwUVBcxsScGr36j0rF6DPuE7dF5NC39fjJVr%2BEijp1p8AjyO6ZyljrUl89T0qSkG06hBPB6h740zCVRyPisgVY6V0ZND%2BJjS907gHTQpKDpYXX3IHeId0DtkTx1tPTg2x1f4&X-Amz-Signature=4ebfc032dd15c507af868603ba0b28911a5b32ee27e163c4516c61f59f83ccff&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEPT66XD%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLK1JKVaz1WHwzdsJj1gfOxvhBCQHqSVzmY8jpLDPFpgIhAMKZizmMw8tlsTM%2BvdMccuKRAngSSLh1w7ZswRcTJLDpKv8DCCAQABoMNjM3NDIzMTgzODA1IgwEl34EFX3S%2BH%2Fp6dsq3AOFiOharRa5kW7oBVzpi%2FXAfMRjyjdk5YIqia%2BWL4Pa55s6SLBKWoaDfhvZhOpeQXnbMQQZS4OCFFrYDwQD3iFAH%2BTXjyAgWVFN29QfNkeOXYYCJ9LEofaxN3sWJNEZlQUIxpbyV9dty0SwUkTTxzlbLE8eCocR5pZz342sTBR%2BJVXX1EyUAV9SgynHOjRQEnfErwCEu61YrDusbFIqdL%2FjNDTKXK2K%2F2yZHEFI30GEx9JchhsqQJmq8LXTHrpolYTon3bRddSrvpoawAW4TOPZbU6dW%2Bq8yPPJO5PzXkfLlWcrTxZ36x86cWbR049f6mCm86x6i4MMKeD%2FGFCWu%2FirmU3S4SPr9PwPOsWt%2B9yEbLzQvkHAIo8S56i259KMVx4yLmHxAxPFn5nh1AWVF0ogjq%2FJv3M5Dwtxq8CbLJFP%2FvkxZIQazdD2E57tcNlAvdr1D7r%2BEf2GmK4az7%2BYIRnQay3ynbKHwtTgS%2BHl5KU6n7v51mk2BAhtRn%2FklLkByIp31iZnbGo5Mtrb53auoKFZCyKqN%2Bwk5q5XRAJfedxETp0K6Z8N5J%2BajZsxcb2USUmSelELHyW9q7Yd9Q9vda%2B2WqmRPFJsjhBvbHcRGCVL6NOcxkjwfhR7mgGc2DDj%2F9e%2BBjqkAfNwvUuU5Cp%2BdPC5oc8zscbwN1NPROk22vNxWGKlB1is4b9RoS9QbhFgzsntm1W%2FTDvdbowO7DQ45SCYaIahod456O0Nu7aEB5tc1vFZsMngbej6tVKwCXEREgIFkl62K51b4Gy3hOqgv7GWuVTKzSWVSyU1Gu50Kk%2B1A2eiP7wjC%2B15Thlpzr14MShXhirbBZj1A1mjVdrRCF2bzEGeDCCMBsYJ&X-Amz-Signature=2197b48711ae96993b35fd874d50be737f0513e5b43d2f5356094c2c7c8db711&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQK5WNJ7%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDIYk7BJU8XHJuNpvkcKexxLQny%2BYpoRhYA69vFM1osTAiEAmB6lu55OytQNtYrZ89mN70xJb%2B90Qg8hh54ayl%2FfnLIq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDMdJ4ii%2F5M%2FprbifnCrcA75xxbthpP60%2BhxcBRndYrD3Xl%2FhXyw%2BpV93Ldd8kZsJrx3Z7YfL88o2DCbfTrnY2cYbODo53X3DbuOs7oHGGxcmzDwaVk66N08TkmMnyq2SKodcdbJ8WjTB%2BTUWbBvMNBJglmega%2FS4d7LvX%2FCerT1Ghyh9KIezFWSJXrBfntdh97tjYzQ4iEKyRaedsB5hgGYXbRx70d9XfHMqL2CDsbDgbcv8JBQQrjSUHvWQqcCqi4DK0K%2FWbv8Q%2B%2BQ8Mv%2B5lVt97FMZ21HbSZbez51ER3EDG%2BLD5u08cvYR8yf8ahHFmpYfp20xEAb0Uixe2LbULTjUzRs6tRr20r8Byfz%2FYBHKRMiDUij1y5WV%2BPShamlbFENhEXV3gNXLlDY8EF7i5ueV7Nof0NQnMZjcSchjanCR9c90HkjJyVQLTOls2SaEo4j6B1XXo4trEV4pig%2BDobQIfOuJODedknOTwYdFNi4Gz8A%2FLZESR%2BskoIwgi5t8rGhKn68SKjZsTKVc7JgYnI%2BXavFhb%2BMxYzz0OVuCVHGhXXI6Mp5m4GqhtRDPnAuCq2nfxjJYce3tBZx0WwFX2loWxH6m4veYuxx%2FkP6ab%2FED70zXQYAGOvrg46cs%2BkDsqe5wurOsMqhEmwB1MLP%2F174GOqUBNBw%2FP5avSubI929WAEDYkm7sh2KdyFkDuaI3EF08PSUMkRX6c9NsERgZSF%2F%2BppwSvK2CV649I9il3nnCpfSHvPSLMZRzFxYbxgBKdNLgzGm2JF7QFZQbnCNraCzefXWXfwP3ZARnvFtygGKvMAAOP7kAPfx5UoK7JGK4YWRzZNkGXQnpndegYhPMVzBDLk1JFMshzFw8mJ8vGtQeIpA7rdsq9mwj&X-Amz-Signature=b9a7bfe4fbe931f3eb09181a4d46608b58350bdf9834579f9804c2d2eceb6051&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZPKQ3N4%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxdpM%2B3M4RDcYTQ9xItO1iY2%2BOP1u5gkeevJl45y150AIgbxZgNaO7YHUYwlXhDU8K1YwXldUTKZLqp%2BmQPliIXx8q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDEKmXn39UUj2%2BGuLqyrcAzkJ%2F%2B%2FvLBO%2FAh4OZ98eL6jmIEcOgAwSZRWZDC5tsv2IdPvO%2BMS9R9na1pqJI%2F%2BaeF8sfY3LUVJFm1yjRclby%2FX9GGd2z07BhvQrELhpOG9vXdUKaQaoIDwOgnpt3B8RskbQX%2FXqIP3Q2xkQWsGQouzyiuQBxOB%2BkSFFXPX6PFRGWrnaIor0akmyXns4wWO3YaP8ZRxYahU9LgZG1j%2FqnEIURy4i0ujGbaBKpjwFEZL0OoCiAwrEgQx5wRMui4KTCYJ%2BTe8H3hTxxHXqBThqbhEA0H4naT7gZVyb6W%2BtElLfm2X%2BUnWNdsOG1qkmG%2FUQjbi93DVz08oY5LCqO05HF1Ohaqm6LQQBH32a1AdA1Cp6c94xu708jhUf9LxTbRJQNq2W6b6Kk1oUpD%2BpzHoXlWdr88lUEW20bWpuRiY0QK0kP3RH6rdN3t9PpMQLxiMFvpIDjHe6Iii8zJLOETKaAvVFGU01nnGq6qZTu2hOjqqrrhUgGE98aODjphbB0CsMyvCab5mygujv8PvxZlHRSWN58Nu8TljHgiiHuaIjrBTn6nT8RpQcn4B0zoQNTbwkKTVZ76ZsoaS%2FMeebaVzuS8Tk3YA2Qs0Zay9FMR0mcvk8mGqPtoxCk3pQWcSaMPn%2F174GOqUB4SsVBlKkGK1mwBVeuY9ploqGMHBTq1fsqHtnNSBws8OygvCyapt%2FWHpfLPYIIx8TbFRppIZhM1aaVNel4f6TZc%2FtK1Ke9WeVmwz2wudZshD53GxsR1fnIdJ03piDlrLwxJQ16NMfrve9h0Pg5s8RVCMLSixeh2kiRka29erdWJaRRalyftxgPm8hgFUDXsrq%2FtGKm4XQhSlLSwXrnIQD%2BYtbNANN&X-Amz-Signature=4274ca4b70ae92a23fe0e12776d856f11638456c39f1c636fe0096fc93aa6454&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXJ4U4CL%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDDqvhjDD9JYsveGWCMUTSV65bwJO9hTIqJsxpUUKABeAiEA84Al26LmcaiC9xJ1XIwArcnnU5myAUb905OHFzXiIkQq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDPtEltpaxU0XHW8teSrcA8FTgsssM0lzr8T6RY5KHGfSIT7jBaCBS4XcsasRBV4aNwZxyv%2BqxSbWM6HHjohtKb9AmYegV72p13r5LQPW%2FobaD6Nkv7aqHuTTQ%2BAMaS9hoNkrCNTkGpVrJjjMRyZVPGff32O3VtTyJMJJARDfjorCymCBwx1hx1h%2Bmbq5F5gMuIbZhkdUeHbrCo6g1U9nc2qMZtGuw5XgOnsdDZBiSu5ZFU%2BLCAe2W2AYUewX0np%2FJCsvjKLNvXUaOumU1wiarQS3xViMZEouGbOcCGUiD2hrPMoiFz1vgXRLScyTjDhqcyfF0kp0tr%2BmdWEGBjWdM4D5XbuQ3p%2BhloHnql%2FbMzkwsDPVaoCo42AIaMMXzhAOoyHzxXoFsgUz2tyi8KcqQsZmZV0zbZnmiBOg5erSFyoMmZts6%2BNeUx45bi7jyHmJwyCHat5IE6C5cVwozITCsdCiViqPWuEFbelVyWIU0Dar0sHbsDdADakCs8I%2BnbS3Y86aXVOruR3NU3rvNokHye4YYpDPLBFSaUf9blITIzS84unNWgZIlhFn%2BV5BrM4f3HwxyxvzhUkPiM1PUC3JB2Icoo1kAChgwOrYKLUcWNoX5QoQxiPGnnLl%2FUueMFWN%2Fv8Q4bqGzvTPKH1vMMf%2F174GOqUBOLpeOdCU85owS0xYUVox2R2vibgmBstZzeEoCecp5IEsGouH2GtH%2BM6RJmwCg8CWhZ%2B5iCbhW31ISgHIDiGbt3h2HrovEAGRMK3RbavNfUCaB5gCQtgnme%2FDXY3bm2ldfBdeKu53FByer56usPNEv3gVdmmizrlOov7zKcgEGJQpcOil8N34Jor2Ut5qMvAAnp3M6NqA1HXCRy3L8cpmj2mmOT3w&X-Amz-Signature=e84da8a46b7d3cf22de0a678ed3cd60b9930be72cdd868b87133eeabb4fef5d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXJ4U4CL%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDDqvhjDD9JYsveGWCMUTSV65bwJO9hTIqJsxpUUKABeAiEA84Al26LmcaiC9xJ1XIwArcnnU5myAUb905OHFzXiIkQq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDPtEltpaxU0XHW8teSrcA8FTgsssM0lzr8T6RY5KHGfSIT7jBaCBS4XcsasRBV4aNwZxyv%2BqxSbWM6HHjohtKb9AmYegV72p13r5LQPW%2FobaD6Nkv7aqHuTTQ%2BAMaS9hoNkrCNTkGpVrJjjMRyZVPGff32O3VtTyJMJJARDfjorCymCBwx1hx1h%2Bmbq5F5gMuIbZhkdUeHbrCo6g1U9nc2qMZtGuw5XgOnsdDZBiSu5ZFU%2BLCAe2W2AYUewX0np%2FJCsvjKLNvXUaOumU1wiarQS3xViMZEouGbOcCGUiD2hrPMoiFz1vgXRLScyTjDhqcyfF0kp0tr%2BmdWEGBjWdM4D5XbuQ3p%2BhloHnql%2FbMzkwsDPVaoCo42AIaMMXzhAOoyHzxXoFsgUz2tyi8KcqQsZmZV0zbZnmiBOg5erSFyoMmZts6%2BNeUx45bi7jyHmJwyCHat5IE6C5cVwozITCsdCiViqPWuEFbelVyWIU0Dar0sHbsDdADakCs8I%2BnbS3Y86aXVOruR3NU3rvNokHye4YYpDPLBFSaUf9blITIzS84unNWgZIlhFn%2BV5BrM4f3HwxyxvzhUkPiM1PUC3JB2Icoo1kAChgwOrYKLUcWNoX5QoQxiPGnnLl%2FUueMFWN%2Fv8Q4bqGzvTPKH1vMMf%2F174GOqUBOLpeOdCU85owS0xYUVox2R2vibgmBstZzeEoCecp5IEsGouH2GtH%2BM6RJmwCg8CWhZ%2B5iCbhW31ISgHIDiGbt3h2HrovEAGRMK3RbavNfUCaB5gCQtgnme%2FDXY3bm2ldfBdeKu53FByer56usPNEv3gVdmmizrlOov7zKcgEGJQpcOil8N34Jor2Ut5qMvAAnp3M6NqA1HXCRy3L8cpmj2mmOT3w&X-Amz-Signature=8cd20b32e9b6a9e39ca192e4360815d2c5ef623fb44ad96abb1be0b5034d4243&X-Amz-SignedHeaders=host&x-id=GetObject)
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