

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z26JNRP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzRSACvZuJMDcRGi98SJY%2BfE2bzvBiirFa8SYVpJkdgAiEAnRoLV7jN%2Fz2b9EvDAKRYR4qRR7zT9E9iVCK8fy5Ob1YqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNA6MAZmKpWYl8t5xCrcA9XVXbnfFxEH4vVdHH4w3U1xNZcpfovbwhblKJ6rYiJcU%2FcdYc0NuyS3%2FrmU0eQ8ba8zKM9Y2EZSxXXP3BQqXgC9oQvEnIv1vGse6YwMEtcJZw7IIna9QbFKwwshVBNVkvD99yQVGL1wKvn3t9BcKmfkYgyVLsQxsAI79UI4vGSqM4aID%2BPWk4GWJv1Ifqss0cdgPwHFvpaFOCHPBjBFcWZkI04JIXxvMoTTBzYKoJPqGmaD0uiw5KGRlDK8OetXt30VY7zf9h9Z%2FApP4Y%2Bb5BnaYszaMHrpCZTwWs2mZqSdQB%2FTc6xSJ6jHAjmoa79nWVR3GqBLaCvPZKSVgXlH5ztv5pdHD28sajCIxzhA2Itgwd6biF0nfwQ7hz2LWLtqCWEKQd5mfATEypBjk9RplmylzRFjqrtJe3kgIZ2JrVvDkaLbM5RlvvSUS0Odc6eKBRDkV8rWDwK%2B%2BRMFgR5re7pQavzKjYH9fwmOEKJC1GSe0Tw19kQnEWFm%2F21W%2FqgNYgvHssE%2FaHx28gpLyfmlN0Tu%2FyGzzxP6taIqvWJczUusMY81%2Fvy3qCjTwZen2za%2BBqJD3pJmtUUQK5Kix%2BG%2Bo1tLURvukSS3cFgpvWFhYtCawQ0888HSPqOw2LXkMOLz8rwGOqUB0KSHRX4zDoU7LMVw9zbhiSUSNOFkO%2FIMQLg4HvyVsR%2F9pqtyGQWE9nWlM9yPlDhwCHaWObYUXtGpWt2c1dJc%2BkXe1AL%2BBb6tP0%2Bux6tl649DaxqDBS6EaR8KUZWc%2BWy%2B7I4KkUfGAsR17%2FcWeHzYAaeOf8ikYfOG1xxj6Z9g0o97QwM5mcV6dWb%2B%2BXP9AWzLp0w9TANUdZTKCVUVBQZ%2FL2n7vmFm&X-Amz-Signature=354f573431b3784993ad126c17a00144cd64142d4a5616566050fc41050536a5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665OHLFII%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICUWPR2mplZRSbFUAU4G7pXChVDpjgYsAs%2FgY9QEmMN1AiASMH02I4Y5%2BDckxCRALtS1Qjs9QhRFBnpdSut6C7eCXCqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyzAsYYhfZyDR3AifKtwD54bC446YiC83Ul21VZ6PV%2Ff93YdxmzQ5eoYtTX%2FvgDw3Id%2FXoP5pXoXuPEDerUoJ8budWcLe6IN9aZFFG%2BnosR7wxo9HvVo0kAiEgaDXwcMO76m3al%2F87AViRon508eD21nCfVujpEYSkZZXBj48oYr7qserWlA1q7KvXvgiPVuJACtDLhmxnoJ82IMj1%2BqjB1hVBvDZWQZNk3DWb2BAEnw8eDpf%2B7Cea%2BbGpVH2D4fYCLZiwTpQLAFqWvwNuAawkd3%2F0QiZoDXXD4mIjpB71xBA3ILo2R5aEQEwMsifS0CufEuZngcaMaMjvWc%2BfvstRUuZBOApsmQ0O3bl0CAPk21JSZ0VBW%2FGjdkAXkr2TxXMdC9rYQiwppttgCNzGNT9m3eDg36IoXkrlGYfwPpYeXCfg4DX8PJ2ksLJE5SRB%2F%2FCYu0ixK86ct9x5VKFLr47NQ6vOc6PfzdGGqMpY%2F0bqU0nXzVfKUFzfnh%2BO4CICVKgRkkYUjxAzCfDxA7mdSzwdNkrRyBWtuAxKGLzAlPHqTKe2CY19X0rPNUum2MyB1zcbs2W6PEpvh4cgSYbqTd3F830BQXy0EbdbSu34F7FQb3p5M5Pc2o6ZX%2FwRiGaAjIbov%2BexYcEs3LSI5Iw8PTyvAY6pgHkLTugjjr9KuZLNS6aSKcmM%2FL1iGlGWpsnVQWHocLscxbdL517xwOdtkUBw4KcaGkl9PRzTzBTHogt6HtLFR07c5PAKFZG0OFs5IxGdCGpBDQHEteBOxBJU34PGGo2liXaAAITbxX9PZrVskXCbdNk9FlceqIouRbFJwWZQAC1EPn9j2eIM6NLVNZe2%2FDSTbKBNeEs9fRxQgTXOjcd%2BXH0oLXVms%2FE&X-Amz-Signature=b6c1d353dbe600a1cee6ace23b8f18a4693a6776d055fbd17a7a669fab4adf64&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5GVWP6O%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuLZOWdT%2FlPiCSlRKQ%2Fw9jEGkkkheHkQ5%2B5ZkTY%2B%2BVbwIhAMLFAjUUZTRIFkmMUAPiR15wn31ybbgLR%2Fm07OdFrYgZKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgygcfCKzRcioXl953gq3AMnHdpW4dO7XEiOXIkrsshADKvo%2BPmQWzKWCCoJwZhZaRfyUEVQHEYo6%2BGBE9QonqKfkigobJ5%2BopOAQSrImDW7TYHX0g35yWzPK2UcOVJlAld1O15vOwkkUf%2BlCZ5A%2F%2FTQuzpnREWXDYV7MDIjBQRmj1EGCbLnuzxdrNk7tOOkzPL%2FVN78mlXCJT8Z1eHLQHjs2ECXP99WNU2C6ijGLI1rqb%2FU06xKOMmTp8GtsPI%2BbhlP9PQQgUnhZGxrW2uneMbtyZ8d9vXQAgeO6yoOmK2D7WdO8crUU7Zh2q%2B3znCtsn%2F8gcq4PNpEJkEPKQOzTrJ6SwE6zBI%2FFdPXqTZyknv8LbdJw7QkS%2FmyeaOF8Qs9CMOpd4t2ICGlAccM0eSREP1unaQZLdF5lfHFgMHRIyReqPLLcg0%2Fw47aAzGUFLr7%2B%2BY8nZipbs2WTSr6JnmdQB9zBVE%2BnLLI1pw%2FYpD26wde8evGUlwwFgrEA3yLp2wGTWY0lKkMZ0IHp5biXMcNgVeF0oytwkuCGxzMFe%2B0mF4ptgCUsM1VQ4cl2XT43X1LViHP01sUUklE3hVGVRZ7UFMfV2QWFv3fvwGkF%2BMx2%2Fp7vxLB3EQRsZqYfNCepa0l9FhBlCWis5k85FZXAzCd9PK8BjqkAT0xf1l%2FjKug0tb8bzWkdFOs2LdVZxPBtk9azA8x7UuGJyctWLEMgv%2FDcikSVB%2BLIe3xVeGEQTjQakabNQDlq%2FDMQwA5l7cbTLPXxljDOsUS9KqCy7tJk6vbrpgLRSmKXCJMkZ8T9%2B6JxGxj0QRvjpEFtdmzwBu6dEM1lGwXiXOHg2qwFBWe97r9aFLVgY%2BSmDVMwumWut8l%2BMyuv3xJDIPRmva1&X-Amz-Signature=06b57b16910a313ac19332a3647bca26d40fdb4132305fd42a2379e318107a84&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ7B57PX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGmrboK6in71hrQEvARfv%2BaBeMgnVXKfXQswMBgXvGP4AiEAjQGXwJlq7LKaIef8X%2BgnMBXDUvi6nQDC9LAV8FVzXVgqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHUtM64A2AjTAs0GJyrcA0oL8doyu1NN1OA2xFVPsZThSTmJwIHDa%2BlUN6%2FPPekibIzYIMT%2BjUSBFbfYLeKrAHZebhWf%2FpmMNIHHFiyGBSQvmEPChnFy3MkgsrVxK1YbnILC5A2kUKwYqYjuoU0tGnOKvBCwloWZMAYeZ1O4H5RdPB8n%2BP6IV8KZCqDkPK%2B9EFafk0hPM86cwYNX9alQqUZdnHolqmCV5X0p11q18n88q8pf4mLsZb1%2Bafdvgt6wQ%2BFioenNbkQZYc08S4%2FiJF1d1S%2BrbOSCnBF%2BcxahDUXrFdzWFy10qTrjGKLbNl6fp94gkzymyE7l21yvtbbeCeIi2ca70amzR8O9ffd4GyCsVPHwu1IL3i7qItr74WmC5Z9Vwqkp0wmA2Vkqqq0cmge0ZCMQufkDn7nrUw0wbGVvPhVNT%2F%2BOEsv8VbBfCXAHqlUXBkCVWmrgNkn393ybVoZ5SsrFJJXKFUlkkbINrDQwUUqEekXr0%2B2xLHfb9eeGcfFdzWryyAsVFofVQ30Po8HMNlEA%2BbDZb6Yh237gXJdkDXbl2MALV9%2F4r02gI7nXOjs0ga5vRJQmABdtMrmhtwLOPEZCO%2FUkIdjq0XV8OmFAFn%2Bb3znqgJKHpYsnWEsZt2eGM8T%2ByaLjFiw9MKP08rwGOqUBY8335zIqRAFa%2Buw0Fu755OPBsA2C8sQItITo0lHJ1gHMVJ9hXbWeICH%2BtG3lK18GyZmWWOzYUcJO9hTSPaxrzrtnXSARIYcR8460NoCWyODMW3rWpVx6wVLiN%2FvWhYpTkj6aguZ0mgcMMcZ1n%2B7uVxHPRi6AOxdpYJmeopKddTzQJxISn112yyK%2BNlc15Yt2mQ5u5ayvq9oi8wwMlq1UsNy07DD1&X-Amz-Signature=cdb408a51e7aae60865b08ee054f8584ca41229008f3de9cb895bf96433027ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD7DMADP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3Vf9pmPBd2%2FqlsTeXQ73XC1W6XpAawGjbn2iPYtm%2FfgIhAI0iEWhCHFQZiySrWdE%2FGf%2B%2FrFi%2F%2BbPoeMoLG8lJ1GgGKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNM9Q2PriCas1KsWsq3AMq4DnUXdBvTDTnpxtK2%2B9%2FSFg4T250giDf1KSkzSi8l6%2FkSrZCAekXG%2FkQAnEntlt5PYNhue1oYSBMdzT8Vcl2mYLRIjhzZg1FlrR1mlYVyuryDepwgfpqkeQLmYAv4l9juyzrnuVfVLFWD3te9i1Ko4cw7Mre04CflCoJ%2FRQDOUwIJS5suOMEgDMnpB1XPxXx6LZNPz2e1xgbDvvaAilYDpXVFFtEWg3x7VWsgLeZvUkatFvKyCabenCJeVBmTwDU6Z0qNwfTFExU18DGt%2FNDGHuy0a4t7fW0rX89oYUa79Knm0hvFqICVAy6816NHdzVsB4Tp%2Fztx9lD8h%2BFt%2FroDYQH%2BqZOs%2FC1gBE5%2Feg5fw5Nr9s7Awk9x%2Bi7XE9nYMMdWMFck%2FvvJK4z9jA%2Fe5MlFjFITNlcJbmHDprqEkdY7ZCNWJ6Q2VfyDvDc2yE%2FCheeZqXtYPIcDEbrfn4x8fFW5j3fs1gvr23bcb7TLpw%2BIsgkLGF0FJesRgpMNszfEZxjl5RPY9tPswQT%2FljWJMaAqaubd9PY8Vrn%2FgdNu0KIe0AN4KZp9TqmRWGuY4%2FUMysllPtGkvOKk%2BHWZspKzzBNZP5PlzjfnYMxyMUGz6%2BRrLV0OKqqlNgeOYiGITDM8%2FK8BjqkAZrHv1%2FmnCdh3WYv0cOXquxivhaMOHm1NipF6YSXPc3r8mC8n11C9%2BtfcBhmiNmodk4zHIE3%2FsvOKEUYTYDV9vAz7bhYHDIj%2FLxjnYtspMT6JXPh%2FFfLEV2O6Qyfws2Ipxt%2BkpxXjQFXKirrKArUfZlfzMZXpQb%2Bd9GIiKE6Sgsle0Ionx%2BSZ74JhTRnmjTRSxPgMRxgLHgRi5mVLXx%2FralFODxs&X-Amz-Signature=59134d5f02c5f816a5fd03e3232b6ce588e0788921353c60b3a3ceea37673d31&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HM5VLAR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhwJHLqpmGkgVwsRNa%2Fs7kvRqukE4kBvzdT6aiyJbE2wIhAJ%2FfMVj6EVXRH7tS05NIPPgrLcB9j37EgMit6soMeMbKKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDlICipTXuWi576YMq3AObNYNli%2F2WdykHyTdB4RVunwPuj3wEs%2Bk7%2BqVIVk4Pc3jjbNlkSyH5OJkIwRveyVMWs1s1Pm1rLPKsEdsg68rhOQ9bh1evEKrwsowGrDBcvwraL6XokrpOL84Uz%2BWY2onLUcAo4VXRqvO%2FD%2FkumqEUAcjhV4qgsRy1IT6kSpg2AvVhsOCP2oH8uffgqz1amxNifZ8ojCm9Kozm5nw7LYvlvwOG0ntxi8%2Fk898BdxxZvH3Fd60N9%2F88zEUhx0lsw%2BVkt0Z8ifiINoyyGfkCcSVjpj52F%2FXr8p0%2BSzC38j0viEKWmg1Snjd5w3MgvHPfoQe0kBv8sVKzHdbCSS3%2BLDlEy7wf5Cym6YhQmRFYbyUCrqO29U6u9Kt6cGNCEewfR33%2FtxbBOXMbUXifAi7ik9MteYY6U%2FkBPGAa%2BIML%2FHLjO3g4ivtwFVgQl6IkcCHxQTcjvdGWsPXGPGWo0aTXypgcu28UYP2LioygkMIzFjCi5DmtmNbXdJqRHW%2FYEfRyxlNz1oyJ4EaEBC9LNqQ%2FAKs418Epr4nNXqykzTrBeY4vFXLv%2BZxIQJAKSOqrXypZRSbHIat2CzpB0x0V4cmEHeHEUB2%2FAiPSUqify1wN%2FSA52ep5wL5Ks3CyleH2jTCL9PK8BjqkAVTVuxyzpDiua3L3omWcbQ0YLg4Awk1jkfTrL0vT5M0aW8DFGxrLeKf1AhiPYdXEBApYyYAbmC8qXXOflKSWqy%2FXOSxDVXYen5s9IJH3vn9Rhk9FbRPG5TICYrLJns4Z0LTCKrvlgKrfMSYsk%2F1sSzvSHAebnP3vFr2nNX%2FcvFKzSv5Bxb1Uwqr0gr9hoE%2B7a4LJ6wMn1XchDanXMTN0G4P7TeLv&X-Amz-Signature=e478654a2880cbf8ed1d2d50d28f80bea24552a1f60427966d06ee2ce6750b50&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3IUEMIN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCz%2B%2F%2Fau8Y2Yy%2FObUieKdYIk2E6oBb89je61sACmhZSTQIhAJ8YmHRWMy6XMzwdDnhcYOqYLBiO18s2sbZQ%2BXsqpaMdKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxySeJLsC5jZhvSmG0q3AMZWEy9ScBTVdVMmPS%2B31Q4IicXrTd4FBBghCXaFqX91RO0RTLSeU8vU1Efv%2Bgirq2Jg5aYxbaZY20BerZEtCrDpxpn4VuVQxCQjjtu%2Fax7mmKP%2FjHcqblcpaFqj411Epr4Rq3QVOzkyJnR7iqb5FxMrlvkSNkq27bUTEvGGSrC3KM862vZJJHIbnlwpX1UwLjtQM%2BEE81%2BI%2BEwHPODSD5AtDVahaUllTybgs0I1Q0WJG4RJETKHpz5ReyK4tqvXAYqtuKDPTlsA2yBC2Q7QwoC1sJX2F5qAC2DxuZVOxPHeHrs%2Fq%2BsGPJaztb6HiiFhPtGydDBORGce84L%2B0Ymy6ad2LBuekPFa%2B5ky00YAJRCxEok2pC04Xe%2B9Hqw5yjqA%2FgXGoKCwiJap8DkD1gtc7CMbuDPtH%2F8RBHMY7oa5lqQSYvbSmnYpFHppr6vyYWCFuWMa42jxVwPVykmwi%2FZT8zYTDFGFyoFX6Uh9pG9HqsE5v6PbSUs5A64k%2BYCyionT6lYgcsSzSG4y7kTVEnTMtG8Ojc5HhP93Yamk9Hku3Jzv85aaYaAijqgIXF08zc0ZyQnokmJxm6bx0MjQilrPe54F11wtt2tCglwowoZsI%2BLRfdWFRIqa0muDR%2B%2BbzDH8%2FK8BjqkAdtZqiPZtUa9lYhL%2BZjzgdiirfGtm%2Ffmgv6EZSj7K9vZkFv%2F0W83k5X8arvzKK4RhKNyVO%2F%2FpoeZKn%2B0j26m8QYeDPZ2OXElwPr78zb53qn4kUuo1HOWZw44Ghl40OyQygsUMoNbHAZslKBDByVHRa5EnOT7oJgK1nNi%2BqjDfdM9usOaoP4H6fpVlhk36QgjjgmPclNk75afDPhtdNu9Oq8FHlb%2B&X-Amz-Signature=0c9ebe032ef2ae65b1cbcee3c3aca40754511a1795489c18a10d764e0cd2b417&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZIB3WFS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHZiKgBnkvjuJds017sZZutgM%2BYBa%2Bl1GH4Yr3JUu07%2FAiEA3JJqwqprnu4YRDuzorhGwQfapQviu%2F6zQu3rFo04rtgqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCqi4kdF5K%2FFtUjpRCrcA%2FPQKGBjt%2BOdMJz95U0uWsjA42o5rPHHWgLgvRptPLHGmsYvtFKE19QTy0YCHhPnEzxbFH6nme8RuSQqSRy8tF6PZJ3%2BlFSLjn%2BNd0ws3CTBL%2FS1%2FkfrgXAG%2B1rDGXCOH9vVPSD5ON%2BZNoRURzagS8YIQ56xgHF%2FdKM4cDAMiJkR%2Fjvj%2B6wB%2Fet1AxiYDwrGg0LNiPIbsAFDSEWLLo%2BLQLc8H1nRpTE82d3KsFZl3R2x%2F3F%2BFMcTL0ko52BsegsVE%2B2R3oxj%2BTrO9sPIZdId5kvZEfH%2FcJahXcrukCIZgCvyFJXNowbMm0wosyFDxSCDWb39KZha5hkBqIlb4PNsxQ650EpD6iHBj6cFhNtZpCq7HWsvQ9SCx2y9gzcxZaomsL%2FVXQV6e%2Bblf5ap4sUutNUw8ymGBzZkSq%2BAKV3iU76Pu6f7R1AY%2F%2FWWIz2o4M2cclDp%2BdBJfQmSiSImFgCZh3EiDfl9zLi6dn4bRfLXDKwtQ0rrfOd4qlm4vhp6UKKdh6HoexJcn8KFDWrodmI%2BjE%2B%2FBAav%2BSdX4oW7n12Y9yq2XYSs4oGetiJ%2BS5Ae7Q07N4FUrjLqsux%2FAXxXqwyD8HeO0f862H3cZfR9HkxvItbxYDXjOko5mg8DBAooMPrz8rwGOqUBCcat5y3sjlgaTgNaTGRn357iWUOSrQ8gM6eMJd%2Bvqx5XwyEvuJ9tVxO0vXmZ8jykZ6ZK7%2BHniTyqXhouML0aQzWmo6fPZgtXExe45eaCMPw9RKBQWPUrWaBqFOBxTFm1ZylBMkHage64LYzw8YrzRGKLVIqnmWfRrJeWkj7lDw0FMGnXxaHuoEJKeIeCHTfKevu7xRLrWtYxaci2YiQ3DpFzDhDL&X-Amz-Signature=421127b719f0345629c339d707dfebdce9d9e5f71499c3ef29576e4a0fed5274&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD7DMADP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3Vf9pmPBd2%2FqlsTeXQ73XC1W6XpAawGjbn2iPYtm%2FfgIhAI0iEWhCHFQZiySrWdE%2FGf%2B%2FrFi%2F%2BbPoeMoLG8lJ1GgGKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNM9Q2PriCas1KsWsq3AMq4DnUXdBvTDTnpxtK2%2B9%2FSFg4T250giDf1KSkzSi8l6%2FkSrZCAekXG%2FkQAnEntlt5PYNhue1oYSBMdzT8Vcl2mYLRIjhzZg1FlrR1mlYVyuryDepwgfpqkeQLmYAv4l9juyzrnuVfVLFWD3te9i1Ko4cw7Mre04CflCoJ%2FRQDOUwIJS5suOMEgDMnpB1XPxXx6LZNPz2e1xgbDvvaAilYDpXVFFtEWg3x7VWsgLeZvUkatFvKyCabenCJeVBmTwDU6Z0qNwfTFExU18DGt%2FNDGHuy0a4t7fW0rX89oYUa79Knm0hvFqICVAy6816NHdzVsB4Tp%2Fztx9lD8h%2BFt%2FroDYQH%2BqZOs%2FC1gBE5%2Feg5fw5Nr9s7Awk9x%2Bi7XE9nYMMdWMFck%2FvvJK4z9jA%2Fe5MlFjFITNlcJbmHDprqEkdY7ZCNWJ6Q2VfyDvDc2yE%2FCheeZqXtYPIcDEbrfn4x8fFW5j3fs1gvr23bcb7TLpw%2BIsgkLGF0FJesRgpMNszfEZxjl5RPY9tPswQT%2FljWJMaAqaubd9PY8Vrn%2FgdNu0KIe0AN4KZp9TqmRWGuY4%2FUMysllPtGkvOKk%2BHWZspKzzBNZP5PlzjfnYMxyMUGz6%2BRrLV0OKqqlNgeOYiGITDM8%2FK8BjqkAZrHv1%2FmnCdh3WYv0cOXquxivhaMOHm1NipF6YSXPc3r8mC8n11C9%2BtfcBhmiNmodk4zHIE3%2FsvOKEUYTYDV9vAz7bhYHDIj%2FLxjnYtspMT6JXPh%2FFfLEV2O6Qyfws2Ipxt%2BkpxXjQFXKirrKArUfZlfzMZXpQb%2Bd9GIiKE6Sgsle0Ionx%2BSZ74JhTRnmjTRSxPgMRxgLHgRi5mVLXx%2FralFODxs&X-Amz-Signature=c7c219dc01324560032748a45cb7bcdb1edde68732d9cb62e57f29ef0bb78bd8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVTOYPBK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHHjSetd6umgarAaZfHL4%2BlwWXkQ6MTssEzy0Apj3MHCAiA2ZvF8QVlYEQHJe7B9AfmoGqTeI80ZTH9yBgflbF1WfiqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9XT8kHacAReo%2FkMnKtwDXpW49Jr3R9PfgLZaOskTdG3F4uEL%2BwrRDX1vxifdneu8AO2ZvvyypDygXCEbWp4Fj7BeafXaJYh5mTR1k9lA8o4urESqEtTt5nA9PYdkV99pfpF%2B7EvrHagNsB42qKZGeTQsRDVBC0JckeIPZoePCQGqPe9l9KpW%2F5lm%2B8mG1Msvsiwd6lZDR4DfYCIZpxwe%2Ft%2BFgSkGKgUejkmlWYW2Bfkb74sEnT2uqiHKt5C65KyQydwOZc31H3kVYHh6I%2BTnb7U66%2BhfO3FEmkWucOWFr%2FZ01LJhi6FMKEJkClyD6ptq0jJsVJdUpPMjycvSAP0TRO%2BJ8i0CmjrNmpA1f6HlV7CXvrxfsyQ6VUO999twriGw1Y7ty187%2FtTGEtbBEyDqHzoxlGCofNBDDvfMUHJetw8HEn64d6AyFPtFlvyA6Fm3%2BGwlkUFFANCkV0SwIV9xMLXUQgUXlVuaom6hMMiqB8sIE5ygIz2PHQjgGND8P6XVm%2BvIn8%2BSDoO1BfG3Fj79YwCi2bcmmpCQ5i3BONyspui78bSBTF9Ilc1p%2Fu4P7Q4JSF7QCyR%2FmpP2LbQO4Z18fGxsHUY%2BT2NnUkx8QGdxmaH%2FEKcr70W5AJgvsRU7a7Z90NqVGULd%2BGqZWd4w7vPyvAY6pgFpWC4mTgdVEtlXbm01S13i%2BOTl1Z2t1LM9x4ccKxgT5PAaGl7ETXW1bJthB0%2FhzqTK%2FM%2B90AmetO3w8MrQi7tHVKCik2BFW08VIBd%2BauWuV6IbgSwMMzCdYHtfV0SuMja3mioiGWZRORLexoT9zlKaK%2FoFVktCe%2BJ989eNORPOzN%2FySlvN%2BS4M1%2B94%2FJb3X93UGxRynb%2BjAnlDeAFAqrFNETa%2FWUb%2B&X-Amz-Signature=236075299e4008ca8bba36a90ccc71e24387f46ae4632149ca7b2ee28f59420b&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVTOYPBK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHHjSetd6umgarAaZfHL4%2BlwWXkQ6MTssEzy0Apj3MHCAiA2ZvF8QVlYEQHJe7B9AfmoGqTeI80ZTH9yBgflbF1WfiqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9XT8kHacAReo%2FkMnKtwDXpW49Jr3R9PfgLZaOskTdG3F4uEL%2BwrRDX1vxifdneu8AO2ZvvyypDygXCEbWp4Fj7BeafXaJYh5mTR1k9lA8o4urESqEtTt5nA9PYdkV99pfpF%2B7EvrHagNsB42qKZGeTQsRDVBC0JckeIPZoePCQGqPe9l9KpW%2F5lm%2B8mG1Msvsiwd6lZDR4DfYCIZpxwe%2Ft%2BFgSkGKgUejkmlWYW2Bfkb74sEnT2uqiHKt5C65KyQydwOZc31H3kVYHh6I%2BTnb7U66%2BhfO3FEmkWucOWFr%2FZ01LJhi6FMKEJkClyD6ptq0jJsVJdUpPMjycvSAP0TRO%2BJ8i0CmjrNmpA1f6HlV7CXvrxfsyQ6VUO999twriGw1Y7ty187%2FtTGEtbBEyDqHzoxlGCofNBDDvfMUHJetw8HEn64d6AyFPtFlvyA6Fm3%2BGwlkUFFANCkV0SwIV9xMLXUQgUXlVuaom6hMMiqB8sIE5ygIz2PHQjgGND8P6XVm%2BvIn8%2BSDoO1BfG3Fj79YwCi2bcmmpCQ5i3BONyspui78bSBTF9Ilc1p%2Fu4P7Q4JSF7QCyR%2FmpP2LbQO4Z18fGxsHUY%2BT2NnUkx8QGdxmaH%2FEKcr70W5AJgvsRU7a7Z90NqVGULd%2BGqZWd4w7vPyvAY6pgFpWC4mTgdVEtlXbm01S13i%2BOTl1Z2t1LM9x4ccKxgT5PAaGl7ETXW1bJthB0%2FhzqTK%2FM%2B90AmetO3w8MrQi7tHVKCik2BFW08VIBd%2BauWuV6IbgSwMMzCdYHtfV0SuMja3mioiGWZRORLexoT9zlKaK%2FoFVktCe%2BJ989eNORPOzN%2FySlvN%2BS4M1%2B94%2FJb3X93UGxRynb%2BjAnlDeAFAqrFNETa%2FWUb%2B&X-Amz-Signature=07631a28da41e1beb7bf2cccba9520f6979f773fae2452b2bac495f4df10ba67&X-Amz-SignedHeaders=host&x-id=GetObject)
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