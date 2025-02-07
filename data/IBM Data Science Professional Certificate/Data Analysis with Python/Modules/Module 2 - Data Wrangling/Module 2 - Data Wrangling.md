

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YZRO4Y5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCwbdqprQzrdxhiwjiovv20%2FmJhDQ8pQQY7rHE1QU3wEgIgVPWdNQtOy0TpzeqeR0F6RmfaGXOCofikja%2FAMqAjz80q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPRnd4ubuHf5emDUuircA0njnHumoBJCWOsPvAGqSa9eQoQUBR0ZIICLDwDFIRsWSbux538n7%2BY4f1QdkOYC%2BQceIRFmwa6ydtXx%2BOygAXyxB23fYehZJTm7A8dKpd8U1vMMhR2ycawh9mziVWvn6PD0uhoZnjtUPlhONj3Q%2FJqAwSqWfjGjADU%2B%2FijbyWcoxUhWg7l0Jxc3HRdYyEnRlXKVJ%2FvBHPy4c2r83x1NMKxVyk6HOlCs3EQepkR5OC2bMeD9QV4QXn%2BOcUjkNRRFaDcK9uXSbKsqXwYHHiMsMq7uRGlFB1TBrqAi47SO5mQGHK9TNOL3HfVfESNjCsOVZoAOqH2INJUMykDrl0pqpXRtHfk7qRqQIN9Z1OlmzHYgHfdiJysAO59KtgpNhl%2BC5WbE24qWIWLKYLtnTnUJitPSdiCW6AvmnkYMUL%2Bm02krzD%2BGwsrrE6tEBWzcFW%2FA9ZHAjV64EvjxNxBYpAeN%2BVbA%2FQFK8OSXmImrzK89sn673losPQcWtTIohbIYVwxl1XbDeCwOeFMHnP5VdCRe39WW7PNC%2Bv7fRTlMpMx%2FqA1QsO3FkrDy8WTqgJzJcI3OMSWHjDsFTZYOqN38Dsc%2FtuvM90kqhNGIsM8SvmoM9qxkitC%2FuuUC9DGOrW5DMI2blb0GOqUBUuOfbdyYRTtJL0Hk5tI9O5cxEnyUjB3QfonjEr4ealbJdhVqsJvC6Gi%2FgLMkwv8cVBLiGNXQwKK0stoLDtkX80nrqZgqHR%2B4bWy2TM46SJ9KBvC4My2ip3MNXPCyQkTuT0GX7WlE%2BVqQZ%2FqG4IEbCw23tnTfqYjSz8D15i4vho54uUI6SnECanvL5U9PjiRoXlQYDy7NtaakNDA6FMC3%2B1EHCJMG&X-Amz-Signature=53f23518857a133daeacf32dabd5533afff3f184ff026a7cd54e6f803b9f3cda&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQH5U4BB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCID790MD2meN15X8KT9D%2BB9jnLgyetu94i4OLkez70D%2FYAiEAi8OerYNqYkkqCjcgTd2rrOEhHbbiPNl8tGqCXb9%2BoXUq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDBUu9425Svpz8frxircAxhHEiNC73qMPlUDIKdwsHDrBTb2ODuvFU7Q6359keenf6bgqP09at2Jsh%2B2iWPRh8gtha70h9ZFLToz3DklbOQD9G7GR6kI9SgALTl%2FH%2FsiIQe4cDVfEM4rDnCWDofZ1EbVI2OeIEU81%2FpVOV0ZFpwurqBYXkV879y1JVa0eQJzvqA%2Fat7TZA1rTe09lK3v0jDQr5CrjbjjZz4kE1ONEpoxJA6hIaigDNrdiY%2BTCPe%2FxjwbdGY2L0Widv6MABoYp%2Bm1BqUeX4NcPd4SsIuQk9Xi6OLCb1GmhSRwvdF2FKoyB6Y4ch%2Bz5HwnTLST9r2NNK6eVH5UGimxBhgafiBFj2gRee1Mt0xs%2FmqfVduD0C8Aa7IXwhoLmRwlHfn2d3VRKk84Qc%2BEs%2BLX7fKHHPk79RZJYV9fMm4foFnknk%2BmuAdXvdxvW8X9uiYE0Nqk6l7YJ58ll%2FoPCUKcnme560Clflb3x4D7eYE4ndz597m%2BFsM1BTyJ4so1dHfvi850gcrbEbzPq7jqfBvtePxInc7zLDempiRxRUyTLYKQ8eBDEaupCElEPeUAw1wkL3EHkEo2Ssjjmp2oStUGsjY0OOy%2BaPI9YxgCzN0r66nPcI%2BYOsskM8mCPDHDmayQ13XOMI%2Balb0GOqUBb7rmCIbw09Al88BK9IZFAIVeEuFNdjAWOVsg%2FtC7mDzErNE19aW7nTXMr%2FdgU15fgU5KOMSW2qBanbTYV5m1sjQnFti7Dudu3Qti0%2FQfdLv6d3IBJSSEtOSJzwGYxccJ5C0yJ8vYITBAoN08HydmC%2B0dena2R7F1ZX81tI4u1GdsMrIOEgzTQ12CbIgVuDxWZ8K4L09TVTdZBc0c7e%2B%2ByZi5Mi0h&X-Amz-Signature=d36589480dc926e63a62a1e003ed053c1013b53f7a135118002d5f0aee99f583&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPZCFCBO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIE77m2BEanSx62FCuMBypDWsjzW3tPVU9SO5PHmBmg4DAiEA9v29dg2XmA7Y1ISAYhC%2FSYe%2BXQLeBL0jy5B2oesB2Q8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDIwW89gHqBEuytxSCrcA%2FNpNOB4Vnz9EvKvkXia5u2YXMQoPNnFulSrF5Kh%2BCIWwnBR9fay0p6I86wUPB64K5twLtuVfDWCco5L2xZ84aezFcvjCdx5wJj3crKdJ4r4n5eWAEQH%2BgT5t73nhgXFdwNvulWltfFi8%2FmIUkNvRvrifIJlFBfwukj5an5Rj9Dx97QUo%2B3Yu2Stvjap%2FmVuq2KMFEUWTHrL2IuGnPTYwfwYe1YZuQdGF2XOcijmPpA5XRdb5DRqKplRaAJMWhQ1CF%2BYpA5RMjOwszI%2B%2FJA%2BocB9BN7Ue5BWjjlHhznMgNGZpd1N0RSiGrw3Prkju4oC7%2BjgDpx0TkDuvQigGf%2B2hrLjWNkh1oYqDyrdfJPhiYsEkasM%2FTa66sDLRaO4%2BNiwLgKwzPJaWqOP7%2FkVftkF4sX2ryMXKI83jpmV9ss9HwwmkNMau2XKqv8LOmqOo5pYvFhJdsCVNUCPHbriMXpP%2FjorOUjXEgjGzsCiqccb34WaUlHxnHk8VVUkjqvUsJnJzZ39AgpUzFngAIUbVe0M%2BEfXtTEWamodWSi0iMrjHTjYNLkx99zBNZd%2BN2LqFm%2FbXFKBQlYvMYajK%2BzBxKbPhasaGrtNaYmFb6PHaj2SDGLhz9m%2FLggARYo0DBmiMOmalb0GOqUBJUT39PEBXLJs%2BIQ%2FrikGlgnMdlZUIC0zZoO3vrPcIFnZ%2FW1kzgGINAg6p%2B54cpSZF2rWdJq6ShpXZacBAegh0WbzyfgYE338XStN7zYALMC5DwgyqKW1rgNA4X%2Bgp6TjR2IWA2jcp9Dgu9hPN0MDgaorawgjhy0GSoIbMdM%2BdvMpdVrmnELI311andcRmvZWCxKNjNxIbya3etS%2FjdWZSI2raRKr&X-Amz-Signature=b54944d8e33d8b923264c9407d959c6a46a1be13b16cc266b541acfb09f17a28&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MKVEO3B%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCPAza%2F2Io8XRh2mjhfF5XJiXtxlS1u5PbRoRxXZjeSZQIgMKbR7Q4PbdyNNNUwVJ1%2BRvyyAlXX1pdiAffSvx%2Bl6Aoq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDIdWH8fuDWQz4YWftCrcA0NLcIOlhgKFWL7I1VMAPGGvIEPUR6VCmaOJfd%2BuLGwnwDdZVRr0a9ECcjCombAc%2B%2B0X1DzdOTJfuga8m%2Bp40lTV1Jbly0vToC1rqBzZDDDVDr2xGDmf3%2F%2FY3w3Ja0w9zS6GeD8s%2BrlfXiUWxd%2FrdsqpYKQDoUmQKcyBgFvNj%2BwL4XjcBinL5SvLltPEr23DhupI3BRY%2BVwePW4bWeRMwi6Yr1rwrytwSEfpsltnFTAbdl3njQZqckcbQiCSkKxAlCEJgW46%2BmYOhniLOl38IyoP9iQkzSKnnkBz7qjGH7yo52BZwOFwkCxIoMfPGyWzFQdanQqY9a01svRk3225xDHIpkXxz0g6Y26GOy01suEF8sdQ2YnBsaH8wP43bS74vtBkBZuGyDjv10OCw49G%2FK6H0t9DJJ%2FZAwokiMNPksSgyZJDTu4W0yuJkj7s%2BdwXNZ%2FIJXY0X9xaTtbCnbd0%2FDBntERaQ%2B%2Bzl5jYbv5%2BRzCFO8%2FTISZ2vo%2BHRc8OLKWcT3KKxtb%2BNYoHjkoD6TDKWETe1kTR7nUJZxsSHAYHFSlf74XRrX0aonPqWXc6Pd3rMykRfllH%2B8xGUtA0vneu%2BHBlMeS5385auKu8pgqD7pI321WROBp%2BC3Cz5ZgEMLWalb0GOqUBSTpnuNM0tVZCVHd8HDj5eYuUXW%2Bi1jHobkldEgcrZS6abjcFcUcftGg1Hf9E7wVg1HQdGMpideusiYVOxpVGooz8hxe%2FUkVdidTQfVOC81Sa%2BvKsDyU33QXrLkmDwGLMbJMD9raRjvWb6nrdXrL3niXKe5YwQkK1SbrufBBWmRI5arhZ5gfd5WYIZjrbcNvvNTikoWfCQW2M2Mpk7V48x8%2BFc88o&X-Amz-Signature=70d473b77e8591e7667ba0a5c166e9d08cd782e467f7b286a8c802288b6f0e57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6EGHNI3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCICNOCM3HQw%2B7oRCXxBmO97pWTbYgOC0reP2G4fmzGuKGAiAcZh0uewbgqTHOmmMFXa23I74rq%2FSyjuM8NN%2B5sTrRrCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMwOfympHHAHl%2BVEeVKtwDBkGjwl6WQqC%2B5bDarSQiEhjjZcUQnoFF9eGazby%2FonPGJBIJgwOh6dwpQFrtbRF4VDekHuB9x5GfwhtdQGWbU%2FGmIggO5KY%2FOYmBmYBefN0xETPs9viBpnnlgPMj%2B%2BGUAZiObNEu%2BEmbHOEeFu1yAa7cucGQITKLldE4VfyuMyokDo3xnEtAVhS0t4uNCDe8VCMN6aLRpgn%2FE2rNwRGtv9op9MCfLJ8crMegHuBe6YO0btr0occS6izqJUhTs%2BbRf0U2MFI%2B5OP5pAXEM79RaJFMK1LZTJmLc5c6LVzZ%2FOgYBnEo3itQgMf5vTnL5xNhXYTuXm2Hgae8oUkekkZBXpU4Kq7utnB62YeHYZpaxjtnurLAiSm39MIdyflMS9UCyOleGffxRKzFODgNAADzye8GKU8F940Fd8VM6QRpxiR8obXPt0C5n2Jh6WVykk1d1mWicz3aFZrr9Xj6hjE%2FxIBqMv6rCLEXOkGXuAmgr5SA4jEHzlOAgpb%2FyjOiRTFdT4kZVwqT%2FO5XnPcgAjrUBcGNnU2tovxBcyyB7ehzE4V73n88MmTkaUM2duEZONjb6x%2FdDyEa76soboo%2Bw4KOPcwPKM44og%2FBOZDAdgFEKDv9nJhjmNbWL6KhacYw2ZmVvQY6pgEhocjpyD7ZQDxdDXgEqxHYj38GxixB3Q%2FA6KgV2gHaFht9H2GWBC%2Fa8Ln4wBxgAVx6vYakeYsxQjICSbbr%2Fsv5Nq9B5aLrut8audKHnGobJ5yVeQcxJx0Tb83BVP0kWr1axOlnOhNKUNAHrp0g4gIjHNdDiK601IMywZ%2BEYC6PBOdN%2B%2FG4PxXsEmUgxelQMFw1Srw9TlGWBdzpT5MpT93v%2F97%2B7cPG&X-Amz-Signature=61698eaa50b5f25b5b3161c4f30c7757266520127b7c1db5bd264b4a45a9bf72&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO4PJPAE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD0odwqAHJX%2FHUfz0Bs6im8zNayUASr5SLqVTeCJNX2AwIgFBLvVSTDC8%2FqESk628DcQM1SdVyfOu66ogYcXhC2G60q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDE8pUT8wI1KeeXvLVyrcAzvlMthQ1nGBzgtU262cCf6mQb5fSWpuDp4aB8fDa6DWLDeRXn82qtBg0n6QyJVBvPSXwlFHKze7swv1zU1s9TCf3LsCh7gLbGe6xpd6gGDDqPRi%2FkO8bY%2B9VqdlK3%2F5V2M4holCsgW4UO9At8OG8lTrpTUYSbqzz6vED8Q4AT%2Fb%2B%2Bmqpna6tzxzhft4j2k%2FVGqGLwthAqx9Vlx2C7HBBCus7H6kTuEuYnAwnU%2BkQCMv9yVd45yk4TP3TxuZZScOxXQyYznU5yJqzxRZ372f389QLv%2FoIiDrLPpB4YMP5DueM3iojv9WwIdRBtEC7tpL4%2Bktd0kUWLCRXfBqq%2FuJjLYLU2Kr7sp%2FAD0RAw9%2FO7hUj%2Bmgw9UhI271TKN7skI5bcPyRKD3gePESUc6P8oRztiC9HuREg%2B58wAoffjiN86p0ffup4KFclInvzxbEJBS8%2BGuKom6sP16dO3YIec5ps1jgOnUkvfXW97%2BPJ%2Bdju0VbQA4aFwfs4dOmaZWToyfjV4tqiWIRqlb5ThRK4BWbum7ot%2Bin5Thv2pO7Sq4nEU6Uuk1LH%2BxA%2BM98XeM1ifYirnt8cka0HvlfNRYw8eYrXP6RXvGiSwMC1rQmjdLkmyTECoYil5Z4zcYyLBQMNqZlb0GOqUBC%2BAOwhxVYhVk4Y33t2yJ%2FUX7JY6k94I3GnqBqPGvYEPapvqOKXmYpJSD6lBpSxLNVtpO7ieRWPT3Qbtck7rh%2BdCHJVb%2BZavetFtPIRDiSuIVAAHUTWDcgNsgtKmQXoWEY8v14sliKpfx2STDhKvDczct9nvTT0ONCv8D66cE2q7O7DVKg2pISEzBrCJAzOi74K2L5gU3pL9ccPgpUUdpJ64PECxN&X-Amz-Signature=df7bf3935921cac6958fc08d9af0ee8028e752c7e39bdc17a9a790a2bd7c4bd0&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPN4NFGJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBCbOFnizS%2BGgh%2B7QwdNrIT1vfeRg5rDkshOQqyw4n%2BJAiEAjkimxqYdix%2BwY5mb%2B1cyi5AVJK2oZ%2B5JZXiw5o6pPB0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDP5CoDTKmxYYTAHw%2FircA2Vj5REiRDlzKS6bcJ%2BKHpI%2FVOVzCZUhL5%2BW4CH%2FtquT8LIWDlxIBMbyDP7jPum%2FJxDWAcaDh2jTWt%2Bj5IhU9LJgfhtVOLMOFKJ2kjbzk5D6asJfpna6MADdxIbjo8yVznUxoswo4y2Lz%2FlikJF2MQNPAwYh0diWkN2Ja2te5iKT1G4m8dsyw%2FaBIDQhF8KnJxVnJsHXWYw2f3MdIKCPihhfy%2BQPrl%2FKAS7ShSecPE0vPVmWFq4m%2FpaFWtfq54iOywJY3ELSW6%2FBNoOh1ISjbt%2B7T%2FLUEsEuRfivUSiXWzsgZxyC7IJEDDNlLk8HGP%2Bvh405s4QyAm8vL0eumZvbHPnbirWYaiMFUEmE5bA7%2FsXJv8wptOTZx5p2xjVU1O4dlu64kE82ZPclM6wNiK%2F4HROB4D2EgpgOcYZB6s5%2FhRGgzGphVwSA5Vbev1Cyn3fIkVszEdoFurCXeK%2FWronHE%2F8DTVbHhenUP3koMjoWaU%2BoBM6I%2BZQDnvO67phlSTlEAHHPBZpZM1AiSYk9k3GB6OqUBKP4DBz1Gy373wHvwm1zw19YNRb%2FJ20IGq3kj9Y8IMhUUhG7xmLehle2F4tpozNzoBO93yk2TghHZwa%2BiuE7yFN0jOKjQLZhU%2FZjMOmalb0GOqUBTb8VjLf%2FDEupQGlFPltZncBTSSeYMtAe28J41qGG8x29zwFZ2BmF5pU%2B%2BLdtE1Av15nM%2BR34fZEGOl8XvEoh00EklHXIE3KTvjCMBnjadYx%2FfDQVemqe1wmGG9ib7cGneluz4vUjB15XakbRCEIJMtGsfv0jraFBbvTvvYVJb6KXtPnonNL%2FCyuMqdTL7cv4LigIK66kMKkl5nf9Hp9vjIdxJYA1&X-Amz-Signature=e112c82b28b938d2658b99953d006712a27bc6bea741e082036e3ff4f1c00319&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCVKMVEZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDiVtsromDSBGyC38uDVy3OLK%2FpD%2FanseZMi%2BGTHep5SwIgS7NARmU4PRNz3wqKtoORgvQ86gvj7%2BGeleNywJGWjocq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDjuSCpb0BRp%2BxPWfSrcA4RqnJgvVBmxlqn66iIa8TkI50E3z0EU4UFBySbnFLdcuoPhkNemPN3VB6yaLCh5CrWmZTViePqP0tMYIijXOOGJjCsClzPX0QQmPaFxwr7BhTszdI%2BGYZshLJsyb67Xmxv5uzlbrzHTUnOkBAgI%2BbO%2BCZw99jFYb3QIP%2FEstLYGD7E9kAmxWWOiyQzAqHv4Lv%2FbqZHWm2OwTe9jQ81dxzG2HpMLvA6iJQPvbk3twg3I3vMB9YK4Pjdmf1CC4pn8D04nkukABvjHDF3Lis%2B9%2BTWQdFoKuPZHGRvLQARrKaLSUZ7tkFY%2Fwx5zaoiPmv68A7oPtoPD%2BBAoHiTu5I0gsf8uAoHMsLiPCMZDg3GU4bCgiwsfIzkCNYiDfs62pMIvpAZ%2FB1eicjlD5DMccoTibsMARY8ZUmXLGolsr7VlF6OhiXgHLUPBRNU04c81ixbN%2BzQNz2V12jCzRSKkRbqYtXx6JJ2hdQkdgO%2B0%2BnYBHI0kxmVzl%2BWUo2yOlqeShZJ7LRJ2q2ahUJx1ya%2FjQVW7Sg0TdIVgoDVYb8X0EVgXb4FBkD%2BbEicwuEdu2h1v7YpmwcS0RBydK0whCwX9JCGLFXIIccdAiqXfkwEA4zArls%2BzxoellfJwdM15z7ahMKKalb0GOqUBS7z9HY6PmkZHxAjH9ohT9P4%2FCDdWt1SToMiQzemQFdMfQgtv2O%2FEgzkiRbXHunbskvCxXvkVRbzyHBWoUeMoEapv%2FqFlg7WRMQ1uICEPJQ6MAQ8YBMjhE1dhDyo%2BTuYS1kJiCnLaitjz6uLrtjjj8Y%2BwGRq3FFF9TSTayZtJ4Yl%2BN0Phr0ZfUhirzpcgZo%2Fh77yv1clo7oTzMe9ZXjCSPfQe562e&X-Amz-Signature=c7f4618286bd58171e6c6c907ad228aab565dfce1f4e365d36278e965ceda46c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6EGHNI3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCICNOCM3HQw%2B7oRCXxBmO97pWTbYgOC0reP2G4fmzGuKGAiAcZh0uewbgqTHOmmMFXa23I74rq%2FSyjuM8NN%2B5sTrRrCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMwOfympHHAHl%2BVEeVKtwDBkGjwl6WQqC%2B5bDarSQiEhjjZcUQnoFF9eGazby%2FonPGJBIJgwOh6dwpQFrtbRF4VDekHuB9x5GfwhtdQGWbU%2FGmIggO5KY%2FOYmBmYBefN0xETPs9viBpnnlgPMj%2B%2BGUAZiObNEu%2BEmbHOEeFu1yAa7cucGQITKLldE4VfyuMyokDo3xnEtAVhS0t4uNCDe8VCMN6aLRpgn%2FE2rNwRGtv9op9MCfLJ8crMegHuBe6YO0btr0occS6izqJUhTs%2BbRf0U2MFI%2B5OP5pAXEM79RaJFMK1LZTJmLc5c6LVzZ%2FOgYBnEo3itQgMf5vTnL5xNhXYTuXm2Hgae8oUkekkZBXpU4Kq7utnB62YeHYZpaxjtnurLAiSm39MIdyflMS9UCyOleGffxRKzFODgNAADzye8GKU8F940Fd8VM6QRpxiR8obXPt0C5n2Jh6WVykk1d1mWicz3aFZrr9Xj6hjE%2FxIBqMv6rCLEXOkGXuAmgr5SA4jEHzlOAgpb%2FyjOiRTFdT4kZVwqT%2FO5XnPcgAjrUBcGNnU2tovxBcyyB7ehzE4V73n88MmTkaUM2duEZONjb6x%2FdDyEa76soboo%2Bw4KOPcwPKM44og%2FBOZDAdgFEKDv9nJhjmNbWL6KhacYw2ZmVvQY6pgEhocjpyD7ZQDxdDXgEqxHYj38GxixB3Q%2FA6KgV2gHaFht9H2GWBC%2Fa8Ln4wBxgAVx6vYakeYsxQjICSbbr%2Fsv5Nq9B5aLrut8audKHnGobJ5yVeQcxJx0Tb83BVP0kWr1axOlnOhNKUNAHrp0g4gIjHNdDiK601IMywZ%2BEYC6PBOdN%2B%2FG4PxXsEmUgxelQMFw1Srw9TlGWBdzpT5MpT93v%2F97%2B7cPG&X-Amz-Signature=873716aa6b09500aca91b3ff17823af45c4db2e71ce79533baf536fa100797f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VP552TOU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDbUfhOf57VzB0eynHDKUOZ6T06XTtyCFjVa%2B4tDtFxgQIgfH%2B1tuWJ%2BJhkCNRN5AcmlGRdQOVlI9c0uKGE7OpcRfgq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDMaIYaZPGt0LAq%2BdJircA4v4XEGestLlk%2FeKjP%2B%2FJl9%2B0xLxnQKNga156xUeEEqwpUaXQfhTwCcyvMuzAxhiDYfu01xzfdhnYszNvkzpW05%2BhtzdYcj7fzMrtzLdoHhR5KjN4VHwxm4g5tqOflvs8tc1HL6U0CUTUb39EOOPTBKcLi0Kg6FNpenMZ5h2dbBZFPszpOq8RV7JuzADMUeHIrbXUu4ztoYP3yITeyTaMqJaVMCGMtjV3zZBjKLcPQhNLFZg6AaB%2FMEIc0rtIrB0Pi1sa8sEZhaeVCo7gbQABIvJ2EorB8qy5CX%2FXfXz5mKjH6Yopi%2B0ubQe1MAqrMdzdwOj3WV3SCwXMkTcCRoS6Mq1jjn8yiYZlXB2c%2BG6EKM5lvd2GLPbmNGx7sUE0bLciRDRkVO3NY5n%2F4Ha5lBYuSEwniOgTIlsFu9mddxVD6F5aXGpRKObkYKYm3%2BQvTFVYasyyQEkkvM32ZstsKH9xTzP6wwxBIT%2BahQ3NU%2FcE0HgMovhMDrLPh4qBCi3KkYczZyFDcgxF0eYzulzpvGyu90jYw9mlrKW0hzL3CGxacYISe7epPoCs9z0bHuJvRirpmveXp%2F7WnF2D1P5p7s6fsuZBEgjcwwI8gv3en%2BHWgZorYMrqBObmnbZXp%2FOMOWZlb0GOqUBTwC4WBjFws4fx1VqPDlv0jv%2Fu7qApKKvpRJFanefUlC3%2FS6EwGu89ApU%2Fkw7t8JEYWEFUPHxFmNq0eq6RJl9Miw0XSe8Ojv0T7gpykpHSvt9Qua09CeIDxc0ylwDWIGOHKwshWm5DG5KbZIIpiqieM4%2FrO%2FJ3%2FoBZ%2BKJeXLEX2JC0pkJfzHUutKMr2khTs9dImwyf5Ahd8TWALw0WsQVQ4COv3gU&X-Amz-Signature=f403b001683aebd8e050cb8efdc2953d943a4aaa748765266dabf99a5e1c9086&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VP552TOU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDbUfhOf57VzB0eynHDKUOZ6T06XTtyCFjVa%2B4tDtFxgQIgfH%2B1tuWJ%2BJhkCNRN5AcmlGRdQOVlI9c0uKGE7OpcRfgq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDMaIYaZPGt0LAq%2BdJircA4v4XEGestLlk%2FeKjP%2B%2FJl9%2B0xLxnQKNga156xUeEEqwpUaXQfhTwCcyvMuzAxhiDYfu01xzfdhnYszNvkzpW05%2BhtzdYcj7fzMrtzLdoHhR5KjN4VHwxm4g5tqOflvs8tc1HL6U0CUTUb39EOOPTBKcLi0Kg6FNpenMZ5h2dbBZFPszpOq8RV7JuzADMUeHIrbXUu4ztoYP3yITeyTaMqJaVMCGMtjV3zZBjKLcPQhNLFZg6AaB%2FMEIc0rtIrB0Pi1sa8sEZhaeVCo7gbQABIvJ2EorB8qy5CX%2FXfXz5mKjH6Yopi%2B0ubQe1MAqrMdzdwOj3WV3SCwXMkTcCRoS6Mq1jjn8yiYZlXB2c%2BG6EKM5lvd2GLPbmNGx7sUE0bLciRDRkVO3NY5n%2F4Ha5lBYuSEwniOgTIlsFu9mddxVD6F5aXGpRKObkYKYm3%2BQvTFVYasyyQEkkvM32ZstsKH9xTzP6wwxBIT%2BahQ3NU%2FcE0HgMovhMDrLPh4qBCi3KkYczZyFDcgxF0eYzulzpvGyu90jYw9mlrKW0hzL3CGxacYISe7epPoCs9z0bHuJvRirpmveXp%2F7WnF2D1P5p7s6fsuZBEgjcwwI8gv3en%2BHWgZorYMrqBObmnbZXp%2FOMOWZlb0GOqUBTwC4WBjFws4fx1VqPDlv0jv%2Fu7qApKKvpRJFanefUlC3%2FS6EwGu89ApU%2Fkw7t8JEYWEFUPHxFmNq0eq6RJl9Miw0XSe8Ojv0T7gpykpHSvt9Qua09CeIDxc0ylwDWIGOHKwshWm5DG5KbZIIpiqieM4%2FrO%2FJ3%2FoBZ%2BKJeXLEX2JC0pkJfzHUutKMr2khTs9dImwyf5Ahd8TWALw0WsQVQ4COv3gU&X-Amz-Signature=dcf5729daf32acceeb62fab09693f037f1c113482b52b63bab32d5651a076e3f&X-Amz-SignedHeaders=host&x-id=GetObject)
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