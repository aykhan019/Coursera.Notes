

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WCEUX7M%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1h6SYkXE%2FH4dNY34sj1%2FNJ0sAy12VhxW5CAPBBeveXAiEAx8qieayODvifv3b7WoVhEkARV6aQ%2FOIvuQHyQylD%2BJ0qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK3iw3a%2FCQ6H47mNQSrcA0YE5eUwF2RBZex1ENHhh4N%2BqJubJY14KMyfdAZVaW466daBDdezKRMEhDdDY2g7awROPLthO7GvOz47tU0z26bLiZXAa5bC1pdp0skZmYJRamuZ1%2F00cA5rGmHnt8tinzHNdgxoBQbxeFrC9QLzbiy5rODzKwFP%2BspooZUXvj5fTOOdluYK%2FNlqfKlUyp3rZkrTf0LpCTpbhIZZq10TurSDXjwgxd%2FzxEoW3hypGcUXklmTI%2FgkN72iTRGbJMgQppMryJzPyMekVB0LyFnnErAILDD2%2BTabddwGL8sx5rdJhEZVDCnmZ1fGPNfZ4aHZjV8YRbWU%2FyBLbnjRQ8z2FlDabp1u9u%2Bd31cVlfhfx%2FKBM9BIWsbu4rI%2F5%2FmnkGwrvgFvtjskzdBuU2oJSnUFgMabLqWl0zXVKQ%2FMYDCu%2BinZO0BVyE3wZRz1ReJb36aDoUdTJg2ZZdXv3PjOrZhQ%2FK3XyVHte6F%2FXHZVdGdrCYR8Fbrkdh6duzSUyblq%2Fk1CebvBckZpf4kWqRUlqaJNpWACUm3fKVPNor%2BFduWwIztbOcvDDndczlpahtpYaLdQ%2BysIjmanJxHOzlovu8zTdB1Y%2Bpt2GwZoq1DASQVYVVSBdlTiSDvGY6UVhZihMJ2x%2BrwGOqUBJi7qsKis5YjmhBJmmTFam0F5iuaWDXNmQ4YJW4qUdJ0J9vrNIAc79Re78dB53oIFraLLJqmc7G42s4ebfm0n0d9TRoRnR03Fb16HupqOOVgk9SQaovkg77WnB8WsWvuNuXOz6sXPI0oSiJJzNDb6KCa5CjWKtxH%2FlDvUHZruA8%2BSOUN7Cbtc41IXkAalS1BVSHSaiPzkqGhVg30i0Ey4ajO5Bssj&X-Amz-Signature=b3f7092bd4b2302c41438b3b5159c26aa7eb3812bc98e556f6e0f1fc49422b83&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNV2EZNL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHLmRUq3gsqImJE9SrDliOAK4nivlIbTjXmJHBggrWXGAiAp3IjcUAT0iaTnErA%2BB%2FUc87Wkn%2FkRzAt8Q7acidHLtSqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMn%2BbaMkck3hhpKTxOKtwDahpH3P6%2FK8JbFg3o0n%2FiCyXNvNap3zogPbdi4ZP54107zDcVZzP2jYwRuu4b%2BT%2FSiA6cgf1Pbmcng%2BlZ8RC7vpkp4Sgu20oDUyAni7m6CLv6xLsuR5gVPf6i1hDcOlubNpgYC3e6GMH9okuNUALxzJOyASE%2BPnrFyyHCiq8%2FXH6%2Fmx9mCZK6ev3h85%2BVrqKtBaqGbsXeD%2BFe5ckP%2BLc6oNt4LQU2XBA0okcE7RTvgy4hGd%2Fxixlh%2FbViA4JNw3cs2JWmb2t55gKnsWCH7YZvdQru7Ub0uGfs0Y0t4zN6%2BD1AWjLdIWIqEbZdoC%2FMcHS57jjtrHLEzlg1ifJgQ9CnICgxqtEymgk%2F%2BSttA7nES7tOZrUe5CkdUmZQ65GkrFEwgNjhlzPs6hZy2gK07EpeKTrj2Aa7gGY0mwf8DFalrSnVf3BJVDEPk4pOx8VC1Oeb3eCK%2FqS73BLRHn62WpWvnEpPsjpmYaZVk3FyAeAAbMKQeF84tk5E7KQ7dq7QZeLf9TcbPyujGGCJBQiNwUf1l8zPKTCP8F6PAU53Y7ceBHeBqKg3a%2BUGAIB5D%2BcCfLWSjPa50q3jG%2FyBNe65Y%2BbGmjL64kr3rhyqx22RPH0pRGyuBpoVTXw0aIXB%2BNUwxrH6vAY6pgE%2FlnFmalz36I0uYt%2FN3pnTVkNAVpXH1v%2BXIOUr5mCbHa63HfSPstdybpiC8cW8LQ9jwdV5y9XbgkAPVNMDOzvluzg7LNVF08sZgHU9dIgd1c9XSBL%2BEc8HujHerSE1refEcDKId739h8V0APKSXeCtj%2B4C0NvFD0O8ArtDz156Zt%2BVGLgw7ZzA8MYQWRnRH%2FtWlzivLHmyMXtFiBSqHkoAaqX4ypYo&X-Amz-Signature=04febfb23f223b2d775c124c5796a58160702bbe805775492960645f652bb6e1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5QUTPRD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXKJ4R1U7ZN5FSQVSr5m2rdBd6omVtXudpqs72sTLY8gIhAMWrPEUby9B4hoM9oYT0fEG7OuE9SPGCG%2FCo3e8IG4ZTKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwF9t%2Fp%2FOv7VXI9Q7Eq3AOh3nsk2nh%2FXTLLo7%2BrzWOzAVzGkNMY6fr33FtcIg%2FCljd8xISmHeS8gMDlvlq0bhaTlsttmjeq%2F7sivKwBy65Feonj%2F%2BiJqAHUrgyNv3ZvKjP75ap3tAzY0UpacGMGK6Oq6CoNXpvuMXYaD%2FUKWpJU05iay0zoHC8rrgHCyV5ewvhr9XRo4ItfO9cuKYF%2BR%2BVibrYds9TUrRlaROqDS%2F9Tlqqi7fgB9nGd%2FTQno8cLCCjdDyxoJ%2B7%2BC9HC2IzZCXxCb3bvzpd5tRWXfTfPmtw%2BXcV0WepIwdx85uIAFI%2FExOXJiwlz0UvbGEOuRC4P00G0JCczkfe0SfQwYEwBG2JEifdsNpIlSYf%2FEF02spkdp6dMB8DGUQ7CU7G81S9sMvc4EEw%2FFwqRwiy237rq25367r1KsNxQ88WGAVY2nt6Fzc0cXAz3Yk%2BzkCjH58n7Lvqg2NKnVlr60STEDQBAOQ%2BZ1VBnp1ayiP3%2FXEoK96iTyRNLtdlyHandGYXfr%2FwFgkfE%2BAZ%2BIwiQP4th9nJ9IIE%2F6Zkck4m1rVskI19xexuFT9kXxNYjoQKMtjx30e8WSL2fjOkpQ%2BUx02HEv9VJN1fyqQMmlrPRt%2BV5rhs1QNNP1vn6cOyCX%2FVn98swqTCrsfq8BjqkARoxWNxcMkj3yt5Z8BVSx1rj6fTNu%2Byr2z4dUfyeJad%2BSGH6L5usgirSZk%2Blq2KMhWwvXjybGkU9X%2FafvErGuQM0rbrktt2CEPCbX6GtTQYT6%2F4uTaXsm4zsLWKOLTiARV1fs3AVbIWL534uo8ONnnCJsg72%2F%2FWb8cgz2bJKhTN7htwyUTm69G3edkcBgpEksyxPfytHhV38NKD8cHb9RTlHLgI8&X-Amz-Signature=135fde4251ae81464a242ca11d51479772daf27b353991bbb2fa4d6ae7a488b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMFTEWFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDeGXWCgcUgKEwNuegvxnE5cpmv7WORpYAh0hPbqp01FgIhAOlRm6h2WUVJO1VA5KaVDmhHAWSVzrjlekO1NGJCT3liKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXSjkalLNGeWI5dScq3AN33BIX3BvljQ53mHHzxxU0Dvix5fACr5WultAb9qPNa%2F%2F1CSWJ4d6l5lC1sNJdlzjxC8vPFRw9XGOAtwoAN25Zv4WaQBFcKLf4gOUNsPN5sAailhsMSu%2F2MJ2ShOEFC0cpEFhnRzIBa8kdGnxk9khbek%2F5Ksd8n9fGp4mPhptH2xLkqonQFnZ%2BiDf7IV7zZQX3s%2F9CYQ%2Bj%2BPDL%2Fn3kpE1AqmPLpCaIr1l92LOrL8dJTIuKogzmMISoCooWDbQn47HVuaPRhLkdR5i6iQQZBLjKpxhYhZW4aS2Hm%2BJSdZH0fVcjo91B46%2BaWR%2FAI0K24rjSkp28CIHzAB%2BxWy1IoHGunjD2wEILelLKvg17%2FqJMAU8svGkDtg3kENl1AMRClS8D9ELrCUmsMF2akuPW4WCRAq1RnIrMPL%2F7xeSRlt0owus57QjauH23%2BYplS2EChRGXSs08Z%2BcCJbwtfZPGFRC7HaESRVHSDpSK%2BDkEdCykyWcknueOzSjGkqGOUtkbeGO5Epopn67LPvXBTO9eyTT5D6kRAdWAr6asogdFO%2Bx8yhUpNrmoRm48DMSmjdAPljxGbikMz5BQrqLplTMgK9xCGH8O6Kq3fftrzTpq2b5jYIpIXOYhJIHLt3RYkTCfsfq8BjqkAWpuxk6bOWTi2Ij122hvwXnQp8X%2Fo3CYdmzLA3rchHnEULqTe9%2FCLz3ZrjZR5P7XG59EecRAWKhbbmm59BCksop08HfLzdSyoWKXyG6oyezNBPfLlofUWG2CCFXDOb0AMv8V2jZb87lFKGRPJLcJzK9LgbbYkZ2Tgo2OL8OgLu5D5BNiGaxiU%2BLniwylcYR9IS7AswRHY4g1KhS0GZC2jRlJF0gM&X-Amz-Signature=e51f82927d2ebd4f33d8960d9ca71c96bb043d12dcc19851fad38c6f48f0fcf6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNPYKR7R%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqWQx4XJpa10ZizeQoKczDB%2B%2BBCNqrSyV1R65Ilz7QrAIgNm0bm7wvinKqyk2yNe5fKgAoDZoiZSlkUreGaPI38MkqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPi375zBOo%2BfWIc84yrcA0DATcVU5mRu3d%2FH1hz1ef8n1bz9Whl2%2F3EjUHXeo7OfBfrcGbz9a48PjE2u%2B2NfIMGA9esW5D9upSbDrPTpiMeKhzKSSKT3yOndrqf4FegAjv21D4Ne%2BJCy2lEs7%2BQl74D9Ezpm3gpN3OWRVuiesc%2FcW2UTcJGwqgrgMckbkkS5fjID2oOt%2BLegBp0Pe6G%2FQJsqCLmP10wGPK1OcNf5sy1Dtl9Vm4GfjmsSRdcWqdY2%2FT4FusqXMiQ5SmlGwJuWkbBN4hHoyC%2B7xhWo86Vl%2FV3EarWO6hvidCqTiTsRHsC9l7OrUES6epRILOK1O5MLLQJgK7befAKCok68tVgrNKN9a7PZux%2Blh6ISXGCEd%2FMaDNDUchWxJ6OV4A9KWlQClDJA6fJykomDUq6G0saZR6YhF5WwL4Sj%2FW4n%2BHXbz3QevkeainZFUXQS0fH9cyMCMzI7ImAkIK%2FHlqtQmoQw2uCXCFhX3E7yMjQ93euWRXJMlcBGWTdbNdwJNPkQjfMziMc98dwSyYcWd2obDCwwC5UEAJBb1o%2FyURkEZzMmXCWG%2Be%2FSBhtvmqLHzJhU%2FGZ3R%2BTJAHLXM2Qed125v2J6R8u%2BDpp10yhz%2B2ESU92HE3W34NBGaFjqszHVfmCAMKyx%2BrwGOqUBi2Pe5ArAXAbQryJKQ0Bdqzo4QLYDrIZNZpdGYHCw2%2Br8YZkoJ%2FaEL0AacR9o69S5l5EgUlO8Pbc59R2MAt4GKKmIv3xqkP5ut1QbO94HYu13vlhZuGE1ejUefMcsuDG9Jb232KzRpGntX2HNVvOIyFmf5oCxCYK3hQ5kfwqNMn%2BUmvE8d6hEWihuJssk6X5oiDhQj7kKQwCE0hO3ZPw%2B71lKTANl&X-Amz-Signature=e54897ee757c4806caaf8f94dc00bd532ee39b1f1415110ad4b882e96219d24c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLHKJAFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAv%2FtM0nbyt4Lsd0knR2SDwuE%2FCAhkbi9gwUwNDldwZRAiAfMp44NtbfqYtBJIBRo3wK6EfYhxr%2FBZAN2kU%2BZrOI7yqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5UDM9Xl%2B7os6zsINKtwDe8048cqhKG7Frn75mukSaFfa6oRKsU0UP%2BKQ0paz80wZxo8VRuwaBU7uiDV1UpjVkSYAQ5kRIClt5ec5W83T%2F6zXMSXCWbj4UKM5TpkRPpVimJ8IRhPQVARrRy2oXt73TnKUkYvl7tmVPKrDApmQAHVjkB4UAzn8BIzfchgQLyzc1v4CcdqxD7BvnbXXo4H1Mh35E2VYfNUoVBRTC%2BJJkDiBxgBzGURvmgpomk03Ky5mVTaNKqkOBquuCnR2vsYYbcVN1vEQHgrvrqWBdoZbbHqE69hjyp6XKgTXtUPi31eMtRsUEqJAH1qgDzXJDkR589EGsYrAxAxjnLzavZP5HHm4ga8NQcvcKIXGA4HTx6QUYdrw16d5e6FxEqX1XFlmhm3Ymf1OKb%2BI1yhEmFmknsyEZeMCV%2BHTWEyZxIsb7KJcfNHHybAjHHpAD5bRiNDofv%2BNWQqGm4FnMny9nc8Yb%2BpIUGPNMzw0yCcvaUiHxXfG9LNV3Nv6Lb4E4E6azjQlf3UdddZNrpftbL3bY%2BY8FvmprIAa5gd2lOKq4IWCFxowihoRujNI9yv6agpvCKlT6Qul%2B2eNlZY%2BWTQrLmc48I%2BS%2BZpRYgTpA8IyJK5kMQTQ0kCuV9cw%2BMQMGj0wprH6vAY6pgGl8iiyx7JL5Xm0MTfOjo0lcLcQX%2F4nEgIxDXYtid%2B15YLAdLvZkYqwd2L%2B0uE7cRVm1JxjQeT076%2BUv9OTOOiS%2FIsEwjcicuP2uSizn5Pu4L5kHUVduS8STipbbYE%2BTXr7s%2F%2FAzblT%2F9CkEX0FRIpaeHvLDyjsXLa7Yp%2BDZILEc1f5KrA5cyy0ZlVgaZrgcx2auvMoI8YsPXSNRxM8q0CXrBekTly3&X-Amz-Signature=c5e0376bd5867b5b41cf5cf6e60a1f0e11ff932e82877c80cfab3bf1e079efe8&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJ53RP4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHHfVOH%2Fnizn%2Fw8xLfCAHUrPLdnu5S8F7hAIQCiR9myqAiA%2BGbIMJeSt%2BtqwI0ib7IFznkzZzu%2FqvqEjchBONETVPCqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM53qQkUMZ6Iva6N0DKtwDsB4g96tlEx8a20EYfKKxqlx%2BMFlCCOEgnHAF56MWmW%2B20R2pSsV4jm9ZuuhPSrMdxLOFVs41w1ctp1g4H%2Barb32GlOpwCXUDD0HRWpQPICZ013GvcrOh5LArG7cg43ATjl3%2BzJ1srBzqae9PqCTRGhclMwaSClWVGFovNZ8SWZpTcY4Zc1pQDtYQpgj%2ByPkqtsedMIsHhauIJl0wemvJCHZ8dbmIBEfeuVixnSNrRlmnZkV8n1W1JdPj48D8bAMSnZdW3bQjHufHuCogwHFlLSQve0rdZndADqyhctLQtg0OU4nfsQRJ%2FHqCX0xal7CSjqA47l1sPrWmuKVsyRniWZtEcpHsMABnpymDe7khGrkIsVK%2FBKZDEH1bkYdDCJEPCLZ6H7ZpyHlLZ7c6uq0jgBPV6r27HYxtBC5glEcbsV5gWj9uY8v0IQKppVxk4fD3nXbXo74vZWh9Kgw5oG7oqDXVFeqWt9F0NaxFBYO%2BC2e1naCiJFYN%2BpJSNlof8fRcQBYszX3oMSqiNDNAPPt4LaP%2Fo7RYWV7HNESCkXQycOvfbKey%2BLkRqwvgFFiuOX6%2FSPWP86n%2FBexSSBbigIRmoAhqGB%2BgkJ11eiZLq5iJvhZybJdu0s%2BBoAF0qB4w77D6vAY6pgExbgwy2CKVeBZISkz7N1TotGDIjjx5ZuVjdVqK6emsUt8SGsUKvmoK6F7RIq%2B03BPlQvQVr%2FdtylyFpd1%2FgEz%2FKZMoIBIqWog71JjhQRoW7XgfsaOxppQRyNdRyWBQ1BYYvXKxZ%2B41oCPumUuJOlGlKLxDtZXWJSGIvCess%2F5bSYdD0TBgOW7tjjb%2FPydqg43OLE5YHxa%2FhoN%2BaXkcWiYzX2fVck4T&X-Amz-Signature=66450f7df15e8d4b22b575e458b8e8eb556098117004baebc5ce46091791fea3&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYLCGQN5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEM6Uuo4VXDDd38Sm5RCe1KlVxJ%2FZjdL%2F8KqEzQnfuAgAiAvItLjnxxdQGhIkh2e%2B0ej52L83Z2hFa2idDyCS0eTOCqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMh5XRi%2B4HDFK3lBigKtwD7zYonFSGwe0Ni85RfQH2GvclL%2BUXeqrLJ%2BqGBZU2HV5mxy7ubYPVIeYuhHGK5YPY4RVXEtUuwKfMts7ed%2BrHVwvR4xJFygyCDkzhXBeher8P2d%2BJ1txnPZhVku1G1tCehPLFjfH4u%2Fv5Ggpf9fWt38tUaVkFNYynv7MMJB4P%2BCInGoC3VCpbkGL0S5JIeAP%2F15KLlwJpRYHtD8zicCSwTizcLa8X3lOwDjMhIPfiizZseFbABK8Dv03TQsp%2FGQs1dmbGoofjd9ZU281Ta91Dl1MAyGdQkjS4f7YljAVEbKpB3g%2BrSCAOVlPzZb3E3Jwv2eZp4KtBhY2XdtpJ2%2FApAvQoYQQWm2QYZJoZga1tZ2%2FozTXnuNmhtwd3Hg%2BQu34wYvWbdPn4X8AraGPSvtk%2BajeyeaHrEH6q3T4HTZ7GeO2JB9t9RUsGFxshyLMeNSBsMlbBCicL4HPSvgYDljSpUcfj95cw6mEQEVMynEutjkeCKdMP%2FjLdZgAv0680q4lJkItnHYIuPdNzvI7xwjGoi%2B1N5r8HTUpcUgBjjGCRlu2ha39Wr4DDpXqDq%2FfxNcr26KQw5BT1H0CVipPn%2BkeQAsTH96G4oG1JMp10hpR4ZZcfLLnJ8r0rZI1FHhEwlrH6vAY6pgFjTNrkWzFIl%2BWsuVLj%2FnLhJt6doLPlpTQvziZetEw3J5vHO%2BdPWeoSNkdDCUR7rqhx36lZyv%2FQjWFEDFK%2By0y1CfpdVCA7ASyVf9CML5x6AWfFzupCK65nbFoeD0wQSbY5NvqEmHe4JElEZ5Nk03IRZCgCPYMxJJKkpvCwWcbA3z%2BQ%2BjMY9OuDuhk4vOd1QlGGwwkDLNG3ofH6jeZLLzICn3ofFKuc&X-Amz-Signature=00fde667ec0b6b232733066dd3bc7a3633c297143dc44f22bd2c2a5e2ff77b9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNPYKR7R%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqWQx4XJpa10ZizeQoKczDB%2B%2BBCNqrSyV1R65Ilz7QrAIgNm0bm7wvinKqyk2yNe5fKgAoDZoiZSlkUreGaPI38MkqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPi375zBOo%2BfWIc84yrcA0DATcVU5mRu3d%2FH1hz1ef8n1bz9Whl2%2F3EjUHXeo7OfBfrcGbz9a48PjE2u%2B2NfIMGA9esW5D9upSbDrPTpiMeKhzKSSKT3yOndrqf4FegAjv21D4Ne%2BJCy2lEs7%2BQl74D9Ezpm3gpN3OWRVuiesc%2FcW2UTcJGwqgrgMckbkkS5fjID2oOt%2BLegBp0Pe6G%2FQJsqCLmP10wGPK1OcNf5sy1Dtl9Vm4GfjmsSRdcWqdY2%2FT4FusqXMiQ5SmlGwJuWkbBN4hHoyC%2B7xhWo86Vl%2FV3EarWO6hvidCqTiTsRHsC9l7OrUES6epRILOK1O5MLLQJgK7befAKCok68tVgrNKN9a7PZux%2Blh6ISXGCEd%2FMaDNDUchWxJ6OV4A9KWlQClDJA6fJykomDUq6G0saZR6YhF5WwL4Sj%2FW4n%2BHXbz3QevkeainZFUXQS0fH9cyMCMzI7ImAkIK%2FHlqtQmoQw2uCXCFhX3E7yMjQ93euWRXJMlcBGWTdbNdwJNPkQjfMziMc98dwSyYcWd2obDCwwC5UEAJBb1o%2FyURkEZzMmXCWG%2Be%2FSBhtvmqLHzJhU%2FGZ3R%2BTJAHLXM2Qed125v2J6R8u%2BDpp10yhz%2B2ESU92HE3W34NBGaFjqszHVfmCAMKyx%2BrwGOqUBi2Pe5ArAXAbQryJKQ0Bdqzo4QLYDrIZNZpdGYHCw2%2Br8YZkoJ%2FaEL0AacR9o69S5l5EgUlO8Pbc59R2MAt4GKKmIv3xqkP5ut1QbO94HYu13vlhZuGE1ejUefMcsuDG9Jb232KzRpGntX2HNVvOIyFmf5oCxCYK3hQ5kfwqNMn%2BUmvE8d6hEWihuJssk6X5oiDhQj7kKQwCE0hO3ZPw%2B71lKTANl&X-Amz-Signature=a8d5fe14646894150eb2283b5ead3d5b8a509fd00d238a392bffc068cee74303&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZV4VAFD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBXh2p1FaE9eOM9F%2FG6qenpD%2FRtytvtwXF1euPEBBLZIAiBfQz4IKOxdqVjaMwkY4Z0ODtqjLs9zFEArbvDIKFJ8GCqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrh3V1ipt%2FrYO23G6KtwDGLxVV1iFJFzSIA2taLK0VEYEGPILBojEnY5l%2FA1xps%2FXcWc6cykdyVuS1TPdEGfRBkwsSXNpw1P071Ll0ShM5JOL1BDbtukQg6ffveCj9wGG9Y8EeuwEngxsFieaptYnzmXBRIPYTNes3%2BZ%2B8zqVSayteAGC628gy7hTh8VWn%2BAEGbcJEFZtsRsDkkCZ1024D2vHjZf88%2FJ26Gl9%2BwDm1LOzALOt%2BR5xffQuq4FudJoQiPwBLtxv3ifdZiDLi2Kje6SEPlS0QHzmwr%2FpVAsB78bV4JRf6vS0xW8v6xjzH3Lp9v1TLbioTCkIdZx8%2BGk7zUiNOC1OEgc6Gt%2FKN1g2ZcfbbWO6OBWXai4SbHbpiyGvTy296Qdzd76t7zmD0mVDDo2aALOO092uG%2BRHEmTpMzjrddWYkUX1csO5VTtCeBk8tLKMGxNH1TTjhz61XtqI9PG7Nbnjq2XNgohw9x9aalC1WQ1skMe8gAYxavWZyeAXBAkj9%2BbshvvWibpWy6dlWREVLcXn0QvM3fx4%2BJbIrgBlLvRPBWjRInU1KpXde2DHj8cg9DllfVeWDD4JsaZB2d%2FUpiyXxErPW4OvGC3s%2B1lU5IArxzlpFKYc%2FHJq%2FE0Gx4XaMW8saanfnzIw77D6vAY6pgG105UvCJ%2F7QWTSdCjdAUyO%2Bh7FmijQHyuWrosoVHh18cMojwexOxlsm7J%2F4GUODRqxfRgxE5H4DuDwPMM3BV5iTcwbMfrKjVpDnsyC8xVx1Xk%2BqozV9AWcnhZAJO0HgVggB9DMmEvPpAUphZWx6ggsISnse9KqUQQ%2FI8Ltz0bNzTRZr4%2FxeUcr2azdezaLzsp1BbsFTLl2YPH4ffE5Rigegllxi%2B4C&X-Amz-Signature=4b42aa890284284cb8dacb1b273ea4422f67bf30b3ea6eddd4a3b78f77bc69c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZV4VAFD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBXh2p1FaE9eOM9F%2FG6qenpD%2FRtytvtwXF1euPEBBLZIAiBfQz4IKOxdqVjaMwkY4Z0ODtqjLs9zFEArbvDIKFJ8GCqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrh3V1ipt%2FrYO23G6KtwDGLxVV1iFJFzSIA2taLK0VEYEGPILBojEnY5l%2FA1xps%2FXcWc6cykdyVuS1TPdEGfRBkwsSXNpw1P071Ll0ShM5JOL1BDbtukQg6ffveCj9wGG9Y8EeuwEngxsFieaptYnzmXBRIPYTNes3%2BZ%2B8zqVSayteAGC628gy7hTh8VWn%2BAEGbcJEFZtsRsDkkCZ1024D2vHjZf88%2FJ26Gl9%2BwDm1LOzALOt%2BR5xffQuq4FudJoQiPwBLtxv3ifdZiDLi2Kje6SEPlS0QHzmwr%2FpVAsB78bV4JRf6vS0xW8v6xjzH3Lp9v1TLbioTCkIdZx8%2BGk7zUiNOC1OEgc6Gt%2FKN1g2ZcfbbWO6OBWXai4SbHbpiyGvTy296Qdzd76t7zmD0mVDDo2aALOO092uG%2BRHEmTpMzjrddWYkUX1csO5VTtCeBk8tLKMGxNH1TTjhz61XtqI9PG7Nbnjq2XNgohw9x9aalC1WQ1skMe8gAYxavWZyeAXBAkj9%2BbshvvWibpWy6dlWREVLcXn0QvM3fx4%2BJbIrgBlLvRPBWjRInU1KpXde2DHj8cg9DllfVeWDD4JsaZB2d%2FUpiyXxErPW4OvGC3s%2B1lU5IArxzlpFKYc%2FHJq%2FE0Gx4XaMW8saanfnzIw77D6vAY6pgG105UvCJ%2F7QWTSdCjdAUyO%2Bh7FmijQHyuWrosoVHh18cMojwexOxlsm7J%2F4GUODRqxfRgxE5H4DuDwPMM3BV5iTcwbMfrKjVpDnsyC8xVx1Xk%2BqozV9AWcnhZAJO0HgVggB9DMmEvPpAUphZWx6ggsISnse9KqUQQ%2FI8Ltz0bNzTRZr4%2FxeUcr2azdezaLzsp1BbsFTLl2YPH4ffE5Rigegllxi%2B4C&X-Amz-Signature=51488c88195b6952e35563a9d53f0010949c04585d26e61527cfee2df35addae&X-Amz-SignedHeaders=host&x-id=GetObject)
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