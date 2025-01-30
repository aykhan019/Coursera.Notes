

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4IKJN7G%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMIRHov7MrhEGu7L1RcmmQG%2FlthXkNWl6qEuAI6aJr8gIhAPoE02wvcOHW9wxw%2Fz3Mj%2F2Byxa4ypGteS1TkfsJqCbhKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyoRlKIrpkpwr9Gh%2BEq3APF9Zsk7orDsYTrEh0yRuLkljgyo%2Fu8R%2F34IYtC3KNAzj1Im%2Fh74FutxnixXkb2QlMK047D6vpQ%2FLqJlrXOOm38LSwH184Mqss7ShqHtivFZathsKZejSG%2FrTRRA4uuWki618r70lb%2BGZbL1EtzasvOORNkYVBff15qPaCsJyrk7ePlFdxrjoKDLVa5PdwOtsLg5qFG%2FiSBoraBUy%2F4AU7xxN26%2BlGmJiIiw8BiLnDdz%2FkDdcY3T5TxBN2ep1vBAI%2FrnB9z4DA0ktuexLymVeNa6BtuaNbDYwzeqqOywLHfEJtXiNLhnGJUBKsx9yaA7s5aRIzQbQV%2B9Z4REy6WuDcwO5KEz8pUo4VjMUgrnqtAz324OJe9qC%2FhowdOEaBIRrWv7HVnZ8vSFuNJjCaNG4aR%2B3IbRRrmDy27pUXguzF3hoyKBIIs8K7H0K7%2BDiBEQCjm6SQcRn326A60NJVNNMcpIn2lovpG%2BxKtGI5AHHY5srRwHJ1So9PRcOKMCzHnsLzlFFSE%2FyMm%2B%2FiEm6e0jChsgmiA91qgWqVK0Y3gcK6y6%2F7W3FLfuiX6HJ5pZcsL87f51GhPuuDIBm2ajDcaP9lzrZ5kW0SdesBbVXwLHuLI6GuD46jZGakwIC2IwDC1huy8BjqkAfDDpPB1QZQZygoZvD8ePLypdxaORRRdffxm3Q69Wzh9SgATm2%2F4vSfqidvoY9PHsfWXGbeREVGkvnDfRBW%2BP0CTlUeE1x3DT5B%2BERp%2FKfQ%2BmYGLWbif4HM4akaH0ntQJbAS47Jt2tBVByVfsQ%2BcDfwxYsUHKKbTdA15y0xp%2FDEdrmnasbGPyjcrAfWQde1qrfEjaxwQwUC6VwCuLFVsG%2BHMAaXf&X-Amz-Signature=a7b4f214ce18691292f57434b327f091360c124fb7934522ce6860b11f91607a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHOSXK7J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1Bcd%2B0U%2F6JObgJIycMFYgEpixHkEmNGlUpmkf44iGXAiEA44OPU6TDyupg7WQ8Vd7SUWCxDB09htsa%2FJqkPXV778YqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAFXbrRpc82LFJmTXircAzVbfEhl8u%2BnE1BjSSMW4O7a5blKepZAfEtu15kU1NPchD%2BkchWX2P2xw8HYANKS40Sue6PMa4ukpFLDbYgDsv%2BaVGWrcOPvJA2kliWftS5v8Z1slrV8e8Wm5lUnV61%2FXQmgjCgibleVf5B3oZexUxnN4Q5PPub6FpsjaVukhabOwZ28BV7hHTUG%2B22tmQ0bv%2BXlx0mUNkstO5pd73e59olcaHsbQGEvaSa%2BapEGpZ6DK6e52R8MjaDmo6Nzt1dwzbQh4Y3233sp4nYwKKxUEv%2F1qXbIWsL7RSjF1zdj9GWqRa9fyZj87rozieEcTZYvFIBjwfByAnoJuvuSbdKaehPYMaGD978MxiDcXpUbYCR7mQak9DSPY79UT4SkbFLunv2F3j4W19LiW8ZD26sMpD8yr4cOCzcyVtNyOO%2BOp1oMagjErQ0xCck2j%2BAEGsUFomF%2FTXXxufgwkPOGRWvKhqjbBgpR%2B3%2FSFXwcU5SvVJUokcKsj0iCCwYlmfme8T%2B8mH8qVl5Tk7nRTLDftrFa2cOTdD8Y6XE4vzTkvyeS6ra14MOz0n6McE9l%2FZ9D86JUdKdHuZlajtJJu5VTbzgr9JGOrXjRcz6Ti6YKzhsBUMUFgVyYfb9RhX0px%2BE6MOOG7LwGOqUBl2m%2Bqpc7xEgnTyyT%2BNsGOO%2Facgdx1mCaewW2EKK0f0%2Bkgv29H61OoUFbAD%2BAiEhxdRmtSDgUUFSF%2BZ2WDSx8aHMqe7H15JPDcdOdRhyaIM1Xl%2BATFMQpGOeuIj4r9PCsPAUvj%2FzE4na83v4nHvDPMgrbFvpvwBDiwuhV75xbFXwloEx9sVwDrR71ewJolZYp6LkhTLHP8%2Bjdvi0Vosvg0LM0KE9Y&X-Amz-Signature=94291744d70bc7f3e56767a2de773f6058b54c9bcdaf08a5cd21f928fb6bf7a3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLQC6YQT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGwkxf3EpzxoZ2vgqf30OkMYPb0C7iWI40FTEU0bONduAiEArETqWMyA1862qi%2BoKe13PfE00Um1OYcOx0yBWbmxLuIqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO8nFq%2FUbOo10gaLHyrcA99dcRf7wNWPYMrLVM7%2BJB9naMytfQgdnlD3Db1HjGfTf9dlxcFLxT0hl94HeuKqKwbyNkD3nbfCChbxQDW2exIi3k3WMtOwmkXeRx1n9QDbIMRU1uCnHgu9H5OKlK4PZ0wFP6DPo6bOq6SVLMgeIeAJoIIkAxjwhoLg%2B7%2FL9UVnEjs1FgocdxLcmZq2C39Cjw1FAF8dZ8V8hoHmUrJtKjyX64aqh%2Fvf4ssWkoRCLsdmce7gYEXSXmvq9uUhQUYjbQXGQ%2Bvu%2FLR6CAhJaGxM8JK4WHbpQtQyqyTFFcR%2FGrJmA1JCP3G%2B3fmywB0sZww1tHrfnoKhYGSeYjWmoxBCLyJ2jWCsMWhCBJn%2BvDXCdKCb3R5jgcFxGqgUw3QSPg%2FfYJwiutJo9lvf6J8QB6gE1ygpmJ9xfN3LPqNrWwIn9HLba4WggU6SKfJYHNPwwGIFFGmk%2FObojTDFF2LLwd85g7%2FJWY0IRzwZW1EYeV60kN%2BN9vHGS%2FcSbmDip4L1M%2FImTGMViSyf07AwrKxY1EIJAfrcixHvzzFJ1ITav7Wtkjao5ftDDmy4VXTvmNc51PmfBDQlKjFASZLsu3rHMGf7dy%2FFAy3cw9H264jrQELUCgJo0YLrIluGO93EGssyMImH7LwGOqUBRPGvs9AQsIuBpMd42MhQS%2F6%2F52VzjMXBv1NxYM%2BuuVufxJy7r0TwqAqa6cxZLlyuguzaUHpAcZsqgKXQ7ej60DvGNyamimF6BjbvWKZ9rtvyDgM8KJ%2FHnSNULPplOtyzzSMN16qWpaBBBbTXOZbd7h6iuU%2BpVZOkygp1Pqr3ejBBQCY64cz04HqfkTMQZZWwXG2ig1yjO7qKyIs6XjgmCfCe7ZPA&X-Amz-Signature=59dae57a453084c2e23af2667c6311db74232a92cb20ab8032f1f08faaafc252&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QYG7K4F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTZf%2Bh%2BPg0XxA36PLE3UMjqfQRZTqEYtUZZF4BTavwCgIhAO9VuqBPCSQM9pMOHUp%2FacIsJYBdCUHBVFZ2BlFUYeqYKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5TNUtZU%2FSmnZ6P6wq3ANWoiGSco9iLLXUGRTz7Ffx9qe4Wl8g2QAEVxgtTOAHuoMf0ckoVYone7SA5Mln3UyhlIRIpc%2FWW5LTPt3QVc%2BEa%2BHjAI19TsaZ7HL21HHFhlj4%2F%2FK4JLOTWgu12fdywY2vYmwE5Gq6n7M1bqQOW0JcsisEm2PaWTJUH4bbHkCt9%2Fe1ngvaPvmS2BoGpAvidL9YgIB1jlfQxzGl35wkmIc%2F%2BGIGNfMKDt0plGaUPuttNS66njhAwDHYDohdb%2FNy5nOjIfMhsv1wgobW1QheH2jJFH%2BXCvKtWg0o%2B%2BkVZb3OP63YEX6A0vCOhXPHK3uVuYvdNj7p0409tVciXPXZQ01KmZq4BkTUXD2Ayf%2FRqg0bup7OXXdGCXFbSlHWcSXdMRW2OKPIlYVQ5PaoPMD5PHYl%2B%2BpoElcAZaT7oo011NmJPysADbZixxaR9SdvBrdAe5JZuW%2FCJvmRRiEm6obSynY68M0zkog3%2BIIVe5YQ9aWadz636z7xvImYKX8MBIP7sD5Hup2oMxQTdXMkEB69zmjYsxz3SXsdwy2BkDIyiMrNQAzAmoxa7s3atr%2F%2B0feYY7BRbNGm71huf9YFZRj%2B8YLvDTKbj8cSCixFuOc04EVxnz9db%2FhQxe0h7m7qUTDuhuy8BjqkAc2y%2BqSPIDUEOQ9ZqybMyeFZ2OQpgIr0L%2FLHEfRzVFB7KG5ugQQ1j0%2FI9QOr0XZxfMTNy40aAe%2FyiUzs%2B21lC43Zsn5xcGYROINE5X%2BBKgwTTb9qVhr5KrMQh38MhADBaYV2xLPTsMBdXXReY08kckTBhSmdGujv4pYxHLaA3sh2tM%2FJNvaXfMWjsZDH7AdWO3VaYR61GHRtZQRKT0aMEecOoZf2&X-Amz-Signature=583a65e0ef5978337da1272b5b2e6e8e5dbb2833e503a6b2d331693432b0b95d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZS6AXDTM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBG4tza%2FdHHeD6S8XOI1MQgZl2dLwf8kc5gPD7ac6CvCAiB9fmxKqPxnLqmN%2BKGiQFea3%2Bfs21G77vfxuM1jd7lAnyqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6U5tp7b5HIHS86UGKtwDAzsFcU5K21XQLihIBchlYQVF2%2FOBb%2FAoxt6FejRAIgHkUoHaLuwY4dTjeIa%2BaYTtMJE93Qw3w6WPulllLzl7yHN9HsLRxCnxfK7LZHd%2F%2BoiIbL2EplyPrikq304TtQmiM%2Fdy3YKRrtE8a7eieJWoH5JnUjgnmPCLY1IkBlOJU6XDdzG%2BwuzCsoz3wBwWcuJ3qPKW9lZ5YD6HtGtYaL3Eat1v6cwgVK0FKD0CPFPtHx4RGQeyFnK6KQ21IrY17qndD0sWvG6Lxic2D9Unhp0zCW8jYKGNnhYxSlJ%2FLvwejeZeQnkH8a7CKiNPaTerNx973VDkK76pFzhzlqbjfHXi%2FDtXssWdFC2zVmOI7r0Pebd33oNtsdrfmtwBABlzasvCnxTQJVc1mu8pUxperaA93a9HendgsN9HcozIP1YIp%2FAYN6RnNg7y1Q2PYGW115qgA%2F9zj2ExCsVQuvb5oaKpWsYEpXvyf7CM3OuPLobK3BqLiUEM4z8M86Z%2Fk1Mb6Pq%2FU0ZuJGfYzSykLi1p1kbjt7iwR4Ohzh9A33mcx0ThzZp%2BmqObIu3Oqt%2Foiz6xPwXUaHgM%2BWa%2FXnpNsInCzZa3A7XtfWGAHTNB3rvu6%2Fwtdrr8xBdOZVRe2PbmBN4wkYfsvAY6pgEmFFGK%2F38fQWabICKvknlR0xZIRiac2O4CW2DTqbqn6vjmXy27R3qS%2BhcAnwiFnEpPzZYYSvX2e7CImhThlDELQLgZ1SN%2Bjk63IZa7xrNDndteuteNNi7a0Bwmf%2Fxh4jjAZbjlz2Vw8kxQiaCx5foiYkT4zHsdboXB6yg828m2RYvrhQxdcQS4l4bTCuipVGuSKzoeNkawrikfvYgprYfyDKphg8KY&X-Amz-Signature=0c429b3bc584ab18374b4248b25bea75c8191525cae35160c3f379a3192a6416&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WTLI6AX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC19dUwLw%2BuJgws3pAkGJNx%2BT4NOjc6xpF0RMHNiUx%2BmQIhAJCVRUhEQbgwtysZnpsK9FFVP8nblMxw%2F%2BidsAJOwfdBKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3K2UoK%2BIlpiYfeBAq3AMe3egXCqqtBy%2BGM9Ti8UXt%2BOaT3wAvbD%2FIBJxenPWa%2FWSjs36jDHy5kiudHaZqmrWeJE0w5V1xImprQ%2BscLuogR3AzsoGSacbhBnkZdyhP7Onw4Ayibh0SJ7NI6bY0oUQuXIkg7RI2jG9mSwF25j8AcrZyj1UzK5v8dXemiEIXw%2FZLBvg4oXH1leA3a2N8AiaHd%2F%2BEe97huXVGfF6FwcmyEBY%2F0e0qlUUR%2FRP4HpOEopUaP0HR0Z3MuyoTeXQ930QqMB3g6NApOnbJZE%2FNpFUvpSaiA9Ui806gs1pJFEqQh7u1C5OBKwq4FBiwuTaDOeArJkvdB59w3WUMCHtoUGFs%2FJ2Ot6E9vO%2FT5FL1Wu3CrKQ7xEtqSaKS8lP2074rzc8pgAqILblmjdGrzvLpWREFSHL9dzFRBO4k7wkKq%2B6PGA3oMgOtvUCJmkgjXLCEptL%2FfZjZ4J%2Fri4k2mmB%2BadwpJbSogKKeGU%2FcsvjjopF5hku4ihud4QvCQWwp16dXFuT6pDqr%2BMPLuUA4aT5gyCXZBwyu2turvbYlz0kiT9Xb5kfzUGiDePo4oNCwcSYkuu0j4Gglz0LSM5%2F2es91YA76dIC0zpTiUe%2BwiCPMY8kglmjvIQ5BkkYVqOyRojCUh%2By8BjqkAUd9Ony4c0EWK3yNZlwLCG5M2OH9luDOHBHGQN8YNCV0%2BT5wg1HZ%2FLKNvaaxjXqtB%2BYYkn3tXZoit8blZSk0KKR2AEQFdfJWZgMAQ2rX1OUkI7HQZ9vw5XPUr5UFyXYIXrb6TN4jWaCkiTPdMIs3O%2BTqGbJ3PxahI90j3KEJ4FGfuEZ9HEowO7dYc%2Bb1PJWv46oBTZQbf6SbBdFEUXnz9cTWuXCh&X-Amz-Signature=cfa08d483e9f9d418253bf4b69f74c78d97fd671862c6fe252e2ee616fce291b&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJWFU4TJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjk32v8qA53i5HvlTup%2FfUQ9%2FztaRTMrgBdXdKrfp9IgIgbGEftJKJFlgZq6Htqm33q%2FfgfGJAwhqD%2BOl3OSB85v0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKjhCj3m%2F9OA9Fc9pyrcA1LWffYpeEeJHQ%2FStDmXPUE3BzivyelEa11w5JAEDc1Kwd42NLZDckGQkDiONwqviCBgpFsy1FBS%2BlluRscNxMQaBrCjZGpVGyd3NuvkKkRoy18PDo1TwxbOAA9WuN7tjbPQkk52DzFf8w8YwBQW0CpI8cdsHBCKPlj%2BIxeQKpToCmzl8XbwsvRjZBGARpJ6rM2w7va2lf8CVha9x2dV7DG0cXGgy5i0StRmSkOU4fsLoVsIwrioravUz5sAz7ygrH9T8YcM6NRNj9jG7%2F1ohs39Q6kU6rvDswt%2Fdu1U%2BGorVNII8JYTW2MfEd6JVNuCO4R9g%2Fjos09YQJzwscKy%2B2TnXPcK6Pf9uPQ%2BrnSnUzLkOnt%2BmzOAeMoH0LTB5TXCFLzPq53e54V7kCFn45%2F28Cjz2jRr%2BWYp4fEHAIMG1YdQ6c%2FgoJPvaq4%2FnnHhSRhwQWdNB7BB9P0HmP5otuhBRdugBA6Mo7d8V6N%2BmVXnlOZemFA%2FsCl5kgfJJb%2Fssltcs6SCPy1zfX1hDiY5FqSbA0CGPuzBn1j33oU9mZjyPRfCGLCf0GJzg%2FfLo%2BWJFmjewuA4aedkvOX6Y2Yf5ycc45tec%2FlJuxiv8AL%2BLAlR4ZugsbyDrP9IspQ9bSCxMMqG7LwGOqUBavuxbZFXYzmxYjJ1xlr5wmnyITognVsRHBSAiP2NpQBDZItNbk5%2BYt3brqZ9SEhNbfCWlLYyRy6gGayofsIBslHjdP9Y4FEMlARGq8sqkocv3h0uzVdzJMIHsCcCMaWpcHK7Mjbl0KlSntWa6oOyBPo6g0mfmO4tZzF%2FXH0On5vJoPa1cp9cmtwwrjquX8O%2F7w5R%2BRhxlUwckBl0ljqXDvXkX3Xb&X-Amz-Signature=455e38fb4118fc2bc386fe5341002bc025519bcbb32081414da4cc9bdc576919&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SNW5IQD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BUZJEQn7ji9aGIsmDSYBJKOQosXx48B3WMKdaVGaY%2BAIhAIoTv7YU5nnjHtpRPjDtxSFyn6Btpre7TMYh%2Ft28ObTdKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx53YU9iuaZzaWjDgIq3AO7YZyFW%2F1AWIIJmiw1TbDwjPkq%2FvCfr0WZE8EweA2yGd%2BW0znR7QmcnTiDEtToaGQvmfg0WUsOw%2BmFH5dsn0gOm%2FF1bZZbabQqiMcq6s9Ts9EY0hBMfNRJ7kR2BMwvPH%2FPM0ncat7cERwegbKYxQljGuYkFwyXJ2rEokhYp24jwmJsjL2N05ApdQxFApkjx24uI075nM7eTFtqDRA9F6f31PHQCUv214a2QpbGfv2TKr%2BIrtkrm6MaGz6Sni%2FljhfqOfOq6Vzd0m%2FW4qb4%2FSPxP1fts5aSBeIPhyIjaCk5qAiN6vVhP1VY76%2FD%2BlpEleWgNVH6A10qv9tQaK2Wg75udBvE0jI4f8m%2Bx92x%2BlVXD6BJ6H4PaHrqb9%2F2hjxruV2MgmJN%2FglLDabXWJoYf5hrvBySg9OGJjs%2BkfncSPnlqQAZZMNFH%2FuyzPg4s2WHKSMpWm6hqwRPXoJ95%2BX6LanoqVcyM5osvHp5zijpQjY6%2B9eW8%2FEa1PC4POoKyab2FDfe1V7cgcExhYUueLdm%2FTFOMVPMc72m8lI%2FKLlftBURfKqahU7JMBbwuJnRhjW%2Bz%2FMV8fqzraTVAS3aCaLtCBYUf1ufqR18CC3UoPvOQWIb%2BYBP1UDAZnoX4W%2Bc%2FzDThuy8BjqkAe5%2FZLa5Cr9rgJ3YICtmcUl%2B%2FcTTZaSF%2BLfAckAHb48krTsLWvwbL1LDpkymLojNfdPF2wFCaIdD%2BN1nVPTpv%2BitpDaroI%2FRcghcEMyqiOJh%2FTNQnylme3qJ5IHRGflYsPGxPybBcTYbyYR7MgFmX9RigVYifAMfmRr0035Zo2UTOPt9NLHYaEbLPPT%2BXCn1%2Fadq4As0v%2BRwSUkZ7LuWsXHT0eR9&X-Amz-Signature=a345b2aec37202491e1898998aeeda6cf5ccd5f245c0830f292ac46c33cee7e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZS6AXDTM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBG4tza%2FdHHeD6S8XOI1MQgZl2dLwf8kc5gPD7ac6CvCAiB9fmxKqPxnLqmN%2BKGiQFea3%2Bfs21G77vfxuM1jd7lAnyqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6U5tp7b5HIHS86UGKtwDAzsFcU5K21XQLihIBchlYQVF2%2FOBb%2FAoxt6FejRAIgHkUoHaLuwY4dTjeIa%2BaYTtMJE93Qw3w6WPulllLzl7yHN9HsLRxCnxfK7LZHd%2F%2BoiIbL2EplyPrikq304TtQmiM%2Fdy3YKRrtE8a7eieJWoH5JnUjgnmPCLY1IkBlOJU6XDdzG%2BwuzCsoz3wBwWcuJ3qPKW9lZ5YD6HtGtYaL3Eat1v6cwgVK0FKD0CPFPtHx4RGQeyFnK6KQ21IrY17qndD0sWvG6Lxic2D9Unhp0zCW8jYKGNnhYxSlJ%2FLvwejeZeQnkH8a7CKiNPaTerNx973VDkK76pFzhzlqbjfHXi%2FDtXssWdFC2zVmOI7r0Pebd33oNtsdrfmtwBABlzasvCnxTQJVc1mu8pUxperaA93a9HendgsN9HcozIP1YIp%2FAYN6RnNg7y1Q2PYGW115qgA%2F9zj2ExCsVQuvb5oaKpWsYEpXvyf7CM3OuPLobK3BqLiUEM4z8M86Z%2Fk1Mb6Pq%2FU0ZuJGfYzSykLi1p1kbjt7iwR4Ohzh9A33mcx0ThzZp%2BmqObIu3Oqt%2Foiz6xPwXUaHgM%2BWa%2FXnpNsInCzZa3A7XtfWGAHTNB3rvu6%2Fwtdrr8xBdOZVRe2PbmBN4wkYfsvAY6pgEmFFGK%2F38fQWabICKvknlR0xZIRiac2O4CW2DTqbqn6vjmXy27R3qS%2BhcAnwiFnEpPzZYYSvX2e7CImhThlDELQLgZ1SN%2Bjk63IZa7xrNDndteuteNNi7a0Bwmf%2Fxh4jjAZbjlz2Vw8kxQiaCx5foiYkT4zHsdboXB6yg828m2RYvrhQxdcQS4l4bTCuipVGuSKzoeNkawrikfvYgprYfyDKphg8KY&X-Amz-Signature=d319f6df9dbfe71d21aac9d181ec9187a3ee7be8470b4c3bacb4e083b0be56d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCHAVMHM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNLmEED46J1ElzZ05xTnfbp15s1vJnQk3Q9ATmh2vL3QIhAJOXLruRwF6CQHI4Ign%2B5nRb8JoUlw95CTH9uxo8PLANKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQuiP4520CE5lCux0q3AO1KX2Ua%2FycPbHo0zNdeV1Um6HQxym697zDo8lneCBxMvlVlAxriCF4AvKNSxHQxioxzFDfPJj%2BWyiIUwFXHB16PD2Ke1%2BfIGkC23KjFYf%2FA0htyGv1DTwyn3TCB7%2BzljegOcYLwvQ5HGR%2B2%2B7Dj%2FDvgkt4hnR7avpPfOnJBIKtRwpz%2FXkMJujNiBHF6fZcrUccWRIK%2BmWuRp5bfIpxTexaNaW567agpNslXJNtcjk0RQ6BHz0qPppEnw6nJcrE2SLL0%2FOgyrYNzeiHpkSZBW2ZPyhs5%2FS0E17xOeoNSYK%2BPYeCda0yVRRhsQMBexWecFiYe7TfAYpjpAvKtS8HJvZBGTqKdfTeC6A4eSD2bXSdJ7zCgQlndwR9oSSIZluoeNNlFXd24vgKmIJpioA%2FdX9XZmyn8a6ewrMiW6Pi8F2o7nDrxU0zrxvPd%2F%2BAuhF%2FRi0KX%2BhLq0Zu5w9NNapP9BCNA%2FRG2zSXnyazxhM0KOqMJRgcQGJEjmMjVrqde8znVDVOEYPBnC37JQwU1Z6bDyAMnd488z64M8AqUWzcpF3EWPqYvB9hB9sP2zE5dUrFmqKiaIXcZAbY99E%2BtUw7ULeWkAJ4JobN73xkm8i3Z2jZ%2FN86IuUBLHpucIufSDD0huy8BjqkAU9XH3TFrVj67yID6dCkkHDnw7g1ywlknnn5aveVyeB25oVBHTNvP4SjA7xoMxnmmmx6vsBzr5qdwS%2BI6vdv9Q3rGnN%2BpTkXUqOCCHzPDb%2FFQMwQNo%2FICHW0nW7mqcRtn9dvnb4dWSqQ2TcOUPYfYosLOqUNXwFRriMR7SLeDV2b8LKBy8O2lgxxJrd7dKAtpyuh1ALnlcMgVBmqy918zUNuQqnT&X-Amz-Signature=32a33362742234816c976dffec28a37197bbdf0e2996fbb554ae3179a57c3225&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCHAVMHM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNLmEED46J1ElzZ05xTnfbp15s1vJnQk3Q9ATmh2vL3QIhAJOXLruRwF6CQHI4Ign%2B5nRb8JoUlw95CTH9uxo8PLANKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQuiP4520CE5lCux0q3AO1KX2Ua%2FycPbHo0zNdeV1Um6HQxym697zDo8lneCBxMvlVlAxriCF4AvKNSxHQxioxzFDfPJj%2BWyiIUwFXHB16PD2Ke1%2BfIGkC23KjFYf%2FA0htyGv1DTwyn3TCB7%2BzljegOcYLwvQ5HGR%2B2%2B7Dj%2FDvgkt4hnR7avpPfOnJBIKtRwpz%2FXkMJujNiBHF6fZcrUccWRIK%2BmWuRp5bfIpxTexaNaW567agpNslXJNtcjk0RQ6BHz0qPppEnw6nJcrE2SLL0%2FOgyrYNzeiHpkSZBW2ZPyhs5%2FS0E17xOeoNSYK%2BPYeCda0yVRRhsQMBexWecFiYe7TfAYpjpAvKtS8HJvZBGTqKdfTeC6A4eSD2bXSdJ7zCgQlndwR9oSSIZluoeNNlFXd24vgKmIJpioA%2FdX9XZmyn8a6ewrMiW6Pi8F2o7nDrxU0zrxvPd%2F%2BAuhF%2FRi0KX%2BhLq0Zu5w9NNapP9BCNA%2FRG2zSXnyazxhM0KOqMJRgcQGJEjmMjVrqde8znVDVOEYPBnC37JQwU1Z6bDyAMnd488z64M8AqUWzcpF3EWPqYvB9hB9sP2zE5dUrFmqKiaIXcZAbY99E%2BtUw7ULeWkAJ4JobN73xkm8i3Z2jZ%2FN86IuUBLHpucIufSDD0huy8BjqkAU9XH3TFrVj67yID6dCkkHDnw7g1ywlknnn5aveVyeB25oVBHTNvP4SjA7xoMxnmmmx6vsBzr5qdwS%2BI6vdv9Q3rGnN%2BpTkXUqOCCHzPDb%2FFQMwQNo%2FICHW0nW7mqcRtn9dvnb4dWSqQ2TcOUPYfYosLOqUNXwFRriMR7SLeDV2b8LKBy8O2lgxxJrd7dKAtpyuh1ALnlcMgVBmqy918zUNuQqnT&X-Amz-Signature=956db1eb9ee290de9166154d22319b6bfb5662ab2d97f0ce210bea77de618167&X-Amz-SignedHeaders=host&x-id=GetObject)
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