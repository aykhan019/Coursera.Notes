

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AL6HIOJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDWwD2PwMzlEpZg0qCC0uygFAFiFFXoVg4XjeA1j52ZoQIgVzuzJE0xuW4LDsffC7zaF9Wj4GS6nALmdIR7NZLBN%2F0q%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDK%2FaS4Nn3fw8fmMaVyrcAxqTNDuRCV9WGV9BvBoEHM%2F8UZTSmZSm8xmumI8MUQicnoy1VHQJg8hBBgRNKSlSQk%2Fmb1HDFAudK0FwHJUaGJyJyuRuqiQu54gEjFASV6kEa0YUBoC4lrPxWkKOkvTasE0tGiMqnVkay0eubmiFmDivPCURjnkh8X2UEmfIQwhINk%2FyfUVt1J%2BOvuIwm5D1EUKghpXWy5FtDoA7Hi71Kkd3w5PFnEFGsRbvabjZlw8W%2FeEaz1F0ntIHZnBre4oCwy7Eljioyn%2FWFZk5TEo5lFLDjNeTdiP%2F%2BuKAO8VEPZ1iU3dRFkxTVyfcUvh2FkObOHJu1ZryBbIAZqeuD%2FaexsGJRAqcCOzh%2BapNY9RvWQdgdEUxOZXnKwCfbgVgsAPbKnyqVWLWXRfx8oj7FCkQm2cOSWbkW9PGKed4s2xFlpwH2XpqMWTh4ezqnPQOfsIez4Qw%2Bt1dVejLwYfYdSCNecSXtLxVydU617NkpMHzz5rMktUljsZGS%2BPNBM2%2BmkpU59S1jOBqTp%2Bf0I8bX6mjyN5FkW0sDWxasnmDhz%2BDpF8k4cTLqL2EL8zauDgOG9Jbk%2FrHrNTE%2FI7YETrFLYTBepejTLr0%2FaYKXihiqGBtobR%2BQGYCOW8B8VoIirduMMKZmb0GOqUBHzIB7wKicZ0Ek0sVPBem3XUR44BPMqisufv%2BWrGynjJvPWyN0z7Ih2A6CvDebbP%2ByZpqiNrDGkgVW81t%2FyIhVkdg%2FGlYHrzLXfsDDa%2B7vpcrRjHz8%2FwUBNLESI%2FTRdhOcT9hy0qGDUQk0xymPcjARWh7x5LnIWUUHr%2Fz7R8m0pZzEqWIZfRHOAmkVGQBp2%2F7YYB0orCq9nd9qWNazn4iFE8W0L1p&X-Amz-Signature=3c145004dc9c01aa250017691ed356be8b82b63f21bb054da91af8537b4a7143&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZFPCU22%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDlK5aihU4lXsh5UU0oQUQgh5MR3alhJ%2FGyYlZC%2FC25OAIhALBfZwG3nenP0Nm1xiBTl3CISqAztQ4DnIAiQSHr6DR1Kv8DCHsQABoMNjM3NDIzMTgzODA1IgxT2MPapi6lX81shVUq3AN3iWVrhj5q24NauPbeUrD0dlmI4yUqvtsiIlDVW0IxI%2BmtPFDW5sed50NxYtWtH0I2btFm6%2Fn9c6Syxo4xmycyH3cop42%2BEeRzi0lARD4egkNLRGsEDL70nHcIelZ%2BBOhFq%2BCsEJdUWEcawP73Plhkpfnvkma9Jxbcib51bsDklWEW6mOMvesNSeLx%2FB8eGua8TJlnHW%2FSYhGEErzujdaYGgsodZvaXnSeYzunfzMFzrwcBXedqxS%2BXGrtmtT5KfJ6fgHeVzQxaou02QPddVx%2F%2Bom%2B7IjX72f0YLzYBmgMEsdIKW8xmE7EpZ5alL8%2B9Fhh4jXhwbB3CgT%2F3shiVl%2FmVilY1vII%2FkGGt2YBmVzGSNcnai9wrW6ULLcOLFTHPz0uAGPTNR7YtNNdZL7%2B2ksO10v5Wv9lLRapKiysg4Br54n9oSdGhL5Hhi7E4rSP7JMW4o%2FHc8l0FSaJ%2Bifw4xqgmw0OKvYVBJE505xjeVjz1hFf2w8FbfIqXuO7fG9bTq6MxVzqJF%2FO3Jjwc6EtqfjYEdaAtMmAWVJ9UodAVuXOp6Gy9jGYoPJ1vXdo0TffzZFp8idj4eXCL83IxXJxsHpourTmjEAGZoULXWAiwEL3TjzaR1Q%2FJUQPc55pIDCVmZm9BjqkAfXOnG88cftisYqApW6yWmn%2B0qydq5GgHS5%2ByBcRVHU0yMQfo3yvXdYIBke6Gq1OmS9lM5kpoQ5XIgynhzqzQu1QFzo46Sh4huDvvJDM39zJUhtIezVSLGa8W1cfyhrJuNdznFwN8r3iYnetr4hTVZ9hypgFyzrBV8CmQm26Tp%2BkbW%2Ffz0UnBK9nuh1LaoPeMZgedGvPxuV%2FGSFg9WG5QeISzMSH&X-Amz-Signature=9a8a949594e0edba10b5d98d29e8fed17f739fd64729a4b9d641127b280df791&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V65YRFXV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCH5QsBa%2BQ%2FGpBeoByHMqZBk15xxgYT%2BQF8DpNH1GgUMgIgWnIkJsU3unN2soofeR27YDzn4CBeatn8O9ersSEzFFcq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDJfLvsWHHVl3mgwIjyrcA7QYe8Jo5X9GSgJ%2FLUrfinIwuNNSvs6xHwOtmZLDC%2B4Dw41ZDQ2yN%2B9KZUW%2F5dDXMh%2F2e1yieYh%2FFDEQtB0vzjuhcT62G5GdwcIHaVeb2qOSHzBNnf%2Bw%2Fao8fBsCahXLiPD2l1Mi0CWTGES7d40RK%2BCHaLuSgxfJrrsVVbXvYuQfpRh0fhAJsw%2BJSvk%2BsMkUwrA0fCPs6tTYX3ynVSIa8XwaueDPUsXseCOTMtCCRNCR%2Fu32j8t9OKQ%2BXQMHOU37wFhFZ7RlHy2pm2hRDy7NVfmr6d6LJphV47nY8beJ%2FXrSjYULBKq7qL1apvcsdSVLxqGQsDQbOyatDZUqZSMBoVaDZWHKNMTBVDnGgw4ewcpsq%2FpZ0%2FGsVolsiVk1GeDRvnj2Eb3XG00IY%2F9VWcf1ZbVvZ0tdPS7xlvQcP8dnVCFcMHzyGQl608J%2BNd4AACMuc3WbkDVMQlb%2FaR5dZI45eLTmIKZMeAsdvZT3%2F%2Fl5IIoRvMBZMYwtak30UPbkCKIjqRvzc9iEg3nsYDJtyBX8JPbQp8izMtA2BElOAQ61fOWptSkwapjrQIto%2FHKHoI8dObdnzqfFMsAhG5ibPSrMIwvrYUKxn6a3QBxs3JtIPMSs95xvZQxQi46BppUXMOaZmb0GOqUBKzT1fj1NUjvlKjra%2FAae7TwjeS3K%2FMn%2Fvf96ToXP1g%2B5jJ2kJ%2BwsMQ%2FC6xuLhVyqARup%2FUW1RIZeM8gT4VQqC0p2CEkj6d%2FMlXwzprLeHcLNvlZ4Q5qnIPGlVBWimLEI0D7JHr3UsKEy86NuLa7u0xB1fIpFzHp%2FqkqCdEm%2FliEsbj7mOJBtwJjwQwesXgQif8Yrqeh3r6%2BQ1r%2BzfYoUgpEiL4o8&X-Amz-Signature=e2becc484736a0792b64fee19aa0f7ee464a08e35b5907e84e154b9a14f85e20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664447UVXM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDngSxtXLtGLTh1Up33NlsWdfRSjCddYG10umh64IPVfQIhAO6ZH17npq%2FcQZQoHmz5SDqAhl3Dxio4sSfBGSDWTZVlKv8DCHsQABoMNjM3NDIzMTgzODA1IgxSulYvAM6rVi7pWSoq3AMuQAMCJhT9pjtlfZl7u4MfKkaCyZduMnpvOMl0HK5WaqXWYzz9iLnGoh35nblulqdlPlov7fyEp5sWwFLv%2FjcJ2hXgYfo2rmCVlJEWbkTPsMCaXbCfc8Uz7J3XoWa34u8UdlzKtcE9qY6JQIeEjmm3WFQ6blcO3tiCpxWag33e7%2BK8hFsnuKCQPN48irWsrTXh%2FrQTXhsyb81kcsCRJblRps3Mkd4H3D5iGJ35RaAdNDncEP1bKv4Tu9BObT1XkK6MWVBejCjx7mKMn0l0iLg0kjfU1MoBsSXyac2zG%2BM2LnzxGaSGWpiIlrHBJyLS18o0t%2BiILq3hgRtsonf5sTQkxZok%2BVUM31w7KXmgjkXu3rdTjjQ2IdRtdndL%2BjvuXoVSui8e1RPCQEPr3otV9%2F1Uj0sE3aA9li2zZ0ybfeGj%2BMYYVBFjw7RAo9KWzH7vKan4mwkZ1854Cnriqh7jIRcSwms%2FoTIfHAM734WmHEbGsFX5142P7%2B%2BKTyI%2FIWDLHEF1ZP6N3rbtltvxrIuiWrX9D4Alg4HsuaUU3%2F9H%2BT%2BlpZ9L%2F6wM%2BzTvO5gtaumNiwzflFzXblRpxieYatcaoFzaWS9%2B7WM7zmSj%2FsAXmA8wcN6aco6tLwJ7TDGeazDBmZm9BjqkAVci%2FgmbCPtr3V%2BIFKJgJPfwFQSfXwHhCobwCiecAUVAcOscm7MrP6QvXfYigQe2OYBJ9GJ3a7XdUKvnKCKnEe2wIEWyMSemCxmNcMrbDThFq8XgfnJFWqlJkBb%2FkawE6dGwe0p6qV%2Bg8z8nZ0KxThvZZTPc42LUA9ZyW1qcJJRtq%2BD3%2FxeHVZ1MMLPOPPTGN0QcxhcfjzB3uew9CexoLY%2BKobbw&X-Amz-Signature=a56199710b74ae7d2c3a1ea7f37d47a8bbbd30f9af6a3998899208261f0ba1bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666J5BZGDR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIDuL36Je%2BwKns6ibfLMNX0RgvBfBChQcM4lWAHWfypDiAiEAlO1KRKHTDUhu4F5XvfmNJS3NF3SpFp7tQDqDAMrD2gAq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDP1sBFzJcbsZ1ZVBHyrcAwkoUWaeCln29JSSNcl3184cVK7R9H0puJTeSfaYUxsLRYlpEPuGLFsUES53p4yVJ%2FpX%2B9S9fmrcVJ2GBvZ8Hpyn7Surf1VEeSsDcbb8%2B8PceD%2F5uMHVOPpIcIitjj02lZSTEY0WDTSv2s%2FmGoDRVt%2B9ApH1CQEe5hB78fmG8DeIJP2tMqOxIynkc%2FWNPKZ4D7DKzd%2B0fw8xYUQtE8ACjil3VgDbZ%2FHkUSDuHf4fl%2Bk9sXDpoLsh4lI0X40597PwXN42v9lrfhNQ%2BVGDr7xeDoDNWxqf%2FOk2QogYVLVras6B14fr1l%2FRB2J7dNzTSiFJRYNer5NR%2F8gyhLWCjqJfyG5PemF2ynvT4pswuHOaA8T6MLSbb6Vem1AgQyJvPdzsaXEDSSWHOvaYNGK78FCo%2BsK%2FaqATKhDW%2BSCwz3Z7GVhb8TjG4kD3iNRU%2Fq4wZpDtZ9kub1TUIxShLDIbpUpGn8MzuwyELAFChAaK7JIAxQuvLhRsYXiQfXJH%2Fv%2BU25dCYXdtwG3dI0NsOeyBqMM9TDTI7tg60jITi4nJmnMXRmDfojpKT3dIocjA4J6%2F8eTaCainM7zARbqVBNlGQrGYYRY9R5v%2BAMeyvsKYNsLQ%2FGlQbWf1TEf8BibjQgHnMMGZmb0GOqUBswnRXNc1zdUyDow3ZjumeKErLHoEP3nZyILD1KsbS8GbYGwZhp2o9c16DVf5NQqiDmT4OoG2Df447%2F4sLF0M1UCeMSBK5WSFhWAVUMfGBs3BfgFbVsSxkmUO9gb8SGmr%2B6tf50MxwLbaLdLzHCP%2BUkaJL4c%2ByJOo8NuL134123sVqHm9vUf3s2e3aN3dadRvFjpDlmAv%2FRFizwoeWMsAciLJ%2BOkW&X-Amz-Signature=2d379ba423bc22598a5b967f4183b8ebbcac9e78225d1f0d651e683905dc2717&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Q52RQN7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIGiBpKcq4uDxl1gSKVuvBG8xkguqnSONzmQZ%2FUU1fupEAiAlZ1fPw1WUqdx6GcHxJgo6Wbgktz7k5CYykqOzWKkRWSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMLT2ezMHLauyAiDzlKtwDL7tt2sekTyXE%2BdL2hfBho70lB9TlnmZ8T69gYMQl%2FujFl59i6MwCKoPXt0h3cnudOvT9SQkUhf6MVmcLidpCrW3vACc5FSY3qVCsSMokHc5u68KLGRxTaFe3tqqSXi0jedcAkU9pvkummjrqxJddx0usEVdB8KdneSFaSYToej3FwNgpbQfs6tycCZf3S0wk8lJONZPEbIG23H6zwY4jNQi7wVseLnBx%2F3eE%2B4Oco1vIENj%2Bt9hWuVO9YNcemWK%2BiqlO2YPc77%2F3gRE1N%2Fry%2FmqftjrGvqtXQWFKvVI63sBn32kKCiCxi0dGBM%2Fqp%2BTSTrZt5n7iFQu60Og%2B9wqTkfrz%2FDJqXN3l4Vf%2FWshKEV%2BiCuVMGC4L%2BvH7o89Kn8Ywx206YQY3EFhWNSEzngYa4ckLbtsig1i9R%2FfMcNlAxBvcJ1PCRJvjBpchtViTviwjQWr7Yiecv7Iv2So%2FhWvRTYBv1H7%2FLGWKql4t53OJ%2F3U3APU8LRP6qpghvHJc6CEUnm%2FyTtZ%2Bi8sXyO4PEG2P4jgo10cVlNYTicskEixr39EpsdA3MHCarBcF72Hd6CY6RvbHQeyIzcnre72qSXvtS4saYIGEWB%2B0wJqRDXBatTTYeUHFGIwnO2xWLOwwpJqZvQY6pgFF8F0svqb%2FdhLeCz%2BCLmm4U%2FUFwvnJpCQENm7PaU21nEEeLjk5GFtGpZyF4CWLLTE%2Be%2FvMWn8KGAgRjBWVmf%2FGbpSZJw9KEf8CND2hwmfQcadnWfjnm6BQ73hTKIDSZIVjEQzEsKs8vpi9Uo7xHeTSF8EkyMh6Ffxl92lhRWaHSn68UBP7Ha89FD%2B8SSzwW12A5sc5jbLJTaYRatBWy4mYmNK%2BXnOT&X-Amz-Signature=2e0a4e4b25bd2dcdfed85c30d020472c1ff0f75a0a4dd6632e4d4edc816c5027&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627YOCMQT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIHiLf48%2F2xkg0maTLDmTmMcP944WGqlXd7QESKS4uvfnAiEAzh%2BQgd3DZIDeziBR%2Bo7oCD8EZnwM2AUm5hu3sGZ6Ih4q%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDG%2BzVXAD93AxGlIoHCrcAwDfN4vYV66XE2Uzr124h%2FZsHPmBhboNJHKmugt%2BKhNL1%2FfcDeXCzsa7s2dIVdDjjE4S%2B6AItVOdIlKvTZnRoXatL8D1W06wPjNnWxLbWyC4WdfAixCMtLANhn33LFwIDhnNgUSvDhqAzBUQy84UsXlI%2FQB7bNuqFC50gQ2ppCwj%2BqzaPTQRUe%2FTAvKec3dyURu8x1kNVQEDPJsdUP2lsimq7ZQcNHB0KqIZ27645cevA58K0wdtxM2%2B1LoP4aWVMPCttPp7DQ1E9cLy6irFn5coEOCFEuTeHkNJr2AbCSl1R8H8gW%2Fv2z5WcujFJG0LCCtUrbXoeRejlWvKITrbmFS4a%2FGb3ZORBR2KgZk432J2dH7ftqku088I%2Fkq1d3gx8gQO%2FZ%2FKXl7dzYk1dpPrWNvVqQ7GD9sr9Fi%2BJAcuYcV5tUy3yY4qUd%2BtOaJpIJhO5H3ulK%2BnM6Rf47HuntL4BvDcZYcQKCNvKdOnOTCBr%2FYCoKTEBhWTnzA9xkfSS8nm%2BnkmOuwxvv07MhFdezwhOA%2FvvY3jQa%2F7RNZ7woDUS%2FLvTr7RwCPC9KM0M8MxcaEgKjGhVjw8ynVX4u6lpRY37fXJuSCAoEq95gTa1zjJ1aqBqzLCsmqpo6vR3gfQMNeZmb0GOqUBcJNE0S7zrzaiRMjzBDst%2BkhsjzycdMDKjkkD%2FyKcX%2BRL5a4k%2BZUN0VvCZSvtMvwOWpPP%2BJJu581ignvc36lWQQgn2X%2B5aH%2FX%2FYCtxEw45W%2F0oNsNqTU878ftL3AoSj7XouxAMNnYk8kKUo7Gd6hgFFfPZx6PDuf%2F6E4%2BE5sUuIDvmKdI10wEaMuPs11eCV7mmGsGPGnfImH7ugH3LLgdDYaBzlpN&X-Amz-Signature=ede1d249542692c5fd408b44e953e1f307ebe73dca819e7f93bf1562c75f2985&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLP2KDWA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIGyzKz2J4byRcJt7D8661LepfKCpmR553bN4SIeZfBFXAiEA0KBjETV0h70VfTNZCupmJIs3xDJ1lhilC4nMpP5TKzIq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDDloaU1qlS1GX%2Bc8dyrcA2rZsczV8WaOQ5cwgKi4d1L9XHuIS7M2%2B67PKheou9Mb%2FBzjaqenykJaXm2nUE8GGWhccy3K22UHakvdiHznVQo9IvzVY3OWS%2FVIIbipPC2BYONAZQGgvbJU33BTOFkslEnj%2F9%2FpJpAXTfBUS9i%2BfFxmWdRbbUeFW42s9l79Lv6oVwQKlJDLpkmmWD2%2B68yOjXn6l%2FV%2F%2B0DhWCsuVDjZadzlFFQAXBI%2BX8Eh2qboow8Y4QVO464w0f3mqguJX52M9D%2F81T8x98IGZ36AqHpkMECyOHs8CFskwlyYC8lIHSJ4JpnhiZ1GqElne6kAvmmllMNeNzK3l4AR7sWxnCZliWf6ykKvX0VAqIiwi9xm0DHQiLufcfEdVpdkifR7lGmKbCEV9f6VCJMCOHeLsBtIsFGhmCQO7S7VmVuW278986zXTsFCWoY9hG6z7egljZDTQEI26mbwSq%2B%2F75qUGU%2F0sdU8KYVbV0af9Skp8CSW2JXySLB%2B4TMAQCU8CmHu3Ej3jZMtd0UKfd7eNE1IxB4brDwflgIdTVwkBwLFkg5Mayk9XCAGDoCXyyV1DD3WW2HYaxbA8A3aTB8fuMlgtz7Du2nwmg8iWesmgFQcllLN8%2BVbXk%2BFpOw4f3gYKuIJMKWZmb0GOqUBtmhpI87%2FDjC8nbFRuL94w5pGiDnl%2BL2nWv1xYpBJSJKnfuUCP0OHeZC%2BxxZDj%2BBKVWn14MOcui6PQgh7voo2blOhT5pdwSrulljXMMuF0hsdGAm%2FL0c619ktVwaIU6CH4Ww3d%2BxlsrnqJ4GPlN%2Bk8w81EB9raihotkgvr0XKDkF41NX2L3%2FiMQgMk1sK0%2F0LQZr7IPKL0rSCS6GfNCnZYIbnD%2Bvo&X-Amz-Signature=4fbb5e525ef84f2f47d99d896aece1da5b5510f1e1ac04c39cf0d8c17a99123b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666J5BZGDR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIDuL36Je%2BwKns6ibfLMNX0RgvBfBChQcM4lWAHWfypDiAiEAlO1KRKHTDUhu4F5XvfmNJS3NF3SpFp7tQDqDAMrD2gAq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDP1sBFzJcbsZ1ZVBHyrcAwkoUWaeCln29JSSNcl3184cVK7R9H0puJTeSfaYUxsLRYlpEPuGLFsUES53p4yVJ%2FpX%2B9S9fmrcVJ2GBvZ8Hpyn7Surf1VEeSsDcbb8%2B8PceD%2F5uMHVOPpIcIitjj02lZSTEY0WDTSv2s%2FmGoDRVt%2B9ApH1CQEe5hB78fmG8DeIJP2tMqOxIynkc%2FWNPKZ4D7DKzd%2B0fw8xYUQtE8ACjil3VgDbZ%2FHkUSDuHf4fl%2Bk9sXDpoLsh4lI0X40597PwXN42v9lrfhNQ%2BVGDr7xeDoDNWxqf%2FOk2QogYVLVras6B14fr1l%2FRB2J7dNzTSiFJRYNer5NR%2F8gyhLWCjqJfyG5PemF2ynvT4pswuHOaA8T6MLSbb6Vem1AgQyJvPdzsaXEDSSWHOvaYNGK78FCo%2BsK%2FaqATKhDW%2BSCwz3Z7GVhb8TjG4kD3iNRU%2Fq4wZpDtZ9kub1TUIxShLDIbpUpGn8MzuwyELAFChAaK7JIAxQuvLhRsYXiQfXJH%2Fv%2BU25dCYXdtwG3dI0NsOeyBqMM9TDTI7tg60jITi4nJmnMXRmDfojpKT3dIocjA4J6%2F8eTaCainM7zARbqVBNlGQrGYYRY9R5v%2BAMeyvsKYNsLQ%2FGlQbWf1TEf8BibjQgHnMMGZmb0GOqUBswnRXNc1zdUyDow3ZjumeKErLHoEP3nZyILD1KsbS8GbYGwZhp2o9c16DVf5NQqiDmT4OoG2Df447%2F4sLF0M1UCeMSBK5WSFhWAVUMfGBs3BfgFbVsSxkmUO9gb8SGmr%2B6tf50MxwLbaLdLzHCP%2BUkaJL4c%2ByJOo8NuL134123sVqHm9vUf3s2e3aN3dadRvFjpDlmAv%2FRFizwoeWMsAciLJ%2BOkW&X-Amz-Signature=ef016d010b3e301ab8ab66b1800dd75616b733c4cbf7e65f839513147eb76a38&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GFVFAZG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDBE1on3bF5G7g1axKFuRLzuce%2FcpSSNrnoWXfIjN11zAIhAPvFurKgopsJbzyS7mhYqaBEigSMsm5nY7IKXSdh6mjDKv8DCHsQABoMNjM3NDIzMTgzODA1Igy1PN73McYgpNusThoq3AM7mRoS3JkuzMG%2FWe66pLqqhvCSOiMk2%2Fkdw7Lm7wX8%2B1jynMCyI%2BPTHr5TzSmpQ4wAwvljfhAyKlI2pyFaHzHSxbfHPzVd1Ez5P288xcJg2gbMiXjHe0JSdrqdmBD8U7ZFYXkjzD2IND4goDvdNlS7RNkWh%2FeHuLHd3V443bJqAExydNPFW95eBN0MeLPLJvbvTQNYS76SAdZdKEdlbkV4OOKryT6%2Bp1vigqD4R55PjPZtRSU0qQuIeyMPnMr9RLuBN9sP2qs0pzg0tM4VeTGzdWKp3TqyfQ5st%2FcOEsDClnkdMpOrebXtb5WyBMvpPciJ7teqrQvHaEy7MCvrvteg3Kf65tiA%2BjZR%2F8cxK%2BUAbRgclZYggJXe6ZtWaxYP1PUEZWiwpZ7z1zgkWeDrldaeCdtTXU8Kf4keOSEoOAI%2FPqS%2BfzAgvPEfIu5RBaseLbQR4YrhQ0csYdqh%2B8VHv0UDxXBAEUxGWRF4iJy2NGHvkwyr3NOBnBQJL6aS8yKe1aOd4tkQjGnbEd3%2BqcISpbA1si2moYbs3ZN%2FN%2BziV8f0HozrwKd77jgFvLisvJY5gTAnnQbc6E1QuAI76IQkZnLGMscdEMRjN%2FnL1WYqQCwjuR7492b304X%2FFtziKTDmmZm9BjqkAXQK2NZ4dRf878D9Dtv%2BwpLsV%2B88FZ1rrBhTpsnkKyCPlqF4CMhlJ6wMyZdk2DOeBNaMLlwxFb8MXXdBykEZLHD6NZ1YJ5HMSfZy5sF2r5B9FCb1XmETQoxNP%2BWSGKr7eEI%2BHJVkvlcpX0Awn7s2scQgzZWv6RDF%2FGq2iVsPDYmM8HvlIs%2BzViNtXEQ0Nf%2FshoNuhy0b8FMbFTcOre09Rn6s%2BUKa&X-Amz-Signature=94a9fcf3af12cb5ca438c9c69682760da8e582ed374f9fc4f25ba24a64b388fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GFVFAZG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDBE1on3bF5G7g1axKFuRLzuce%2FcpSSNrnoWXfIjN11zAIhAPvFurKgopsJbzyS7mhYqaBEigSMsm5nY7IKXSdh6mjDKv8DCHsQABoMNjM3NDIzMTgzODA1Igy1PN73McYgpNusThoq3AM7mRoS3JkuzMG%2FWe66pLqqhvCSOiMk2%2Fkdw7Lm7wX8%2B1jynMCyI%2BPTHr5TzSmpQ4wAwvljfhAyKlI2pyFaHzHSxbfHPzVd1Ez5P288xcJg2gbMiXjHe0JSdrqdmBD8U7ZFYXkjzD2IND4goDvdNlS7RNkWh%2FeHuLHd3V443bJqAExydNPFW95eBN0MeLPLJvbvTQNYS76SAdZdKEdlbkV4OOKryT6%2Bp1vigqD4R55PjPZtRSU0qQuIeyMPnMr9RLuBN9sP2qs0pzg0tM4VeTGzdWKp3TqyfQ5st%2FcOEsDClnkdMpOrebXtb5WyBMvpPciJ7teqrQvHaEy7MCvrvteg3Kf65tiA%2BjZR%2F8cxK%2BUAbRgclZYggJXe6ZtWaxYP1PUEZWiwpZ7z1zgkWeDrldaeCdtTXU8Kf4keOSEoOAI%2FPqS%2BfzAgvPEfIu5RBaseLbQR4YrhQ0csYdqh%2B8VHv0UDxXBAEUxGWRF4iJy2NGHvkwyr3NOBnBQJL6aS8yKe1aOd4tkQjGnbEd3%2BqcISpbA1si2moYbs3ZN%2FN%2BziV8f0HozrwKd77jgFvLisvJY5gTAnnQbc6E1QuAI76IQkZnLGMscdEMRjN%2FnL1WYqQCwjuR7492b304X%2FFtziKTDmmZm9BjqkAXQK2NZ4dRf878D9Dtv%2BwpLsV%2B88FZ1rrBhTpsnkKyCPlqF4CMhlJ6wMyZdk2DOeBNaMLlwxFb8MXXdBykEZLHD6NZ1YJ5HMSfZy5sF2r5B9FCb1XmETQoxNP%2BWSGKr7eEI%2BHJVkvlcpX0Awn7s2scQgzZWv6RDF%2FGq2iVsPDYmM8HvlIs%2BzViNtXEQ0Nf%2FshoNuhy0b8FMbFTcOre09Rn6s%2BUKa&X-Amz-Signature=55fc83acaef44a84e4922ebea2104c59dacb85764dc1829c94d47a8b2497abff&X-Amz-SignedHeaders=host&x-id=GetObject)
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