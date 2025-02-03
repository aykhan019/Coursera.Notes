

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QW6NBNE3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCthHQhgjaEFCVmCFnU9PAEfVN6zeTyTykzySazucyodgIgWINn27ZXMbWGUs4xpEe9MWjWDmZgL5VjHlm5Mn%2Bb7mQq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDNMlpzApHAtE4EQE2ircA8g%2F6IN3omvBa3CzT53YKY6goQjbTjjrmzPAK8aN%2BPIztny%2Bbpvy3Fj2ss%2BYm8FfJFNRbErXhndXvynJwpgKmi8aSi3ccEp%2Bl9gM%2B2NL1ptf5yisFLfukgDfy0veA6BRYnpTl7w2hcpdYCUI0ryLAE27M%2FUS3lR1LRTb7UWIHMEQYsJEQ0GGq5BvWhhc1thQCKth1O7BVRagEpc9mlc1NxEa4TClgYX2Aec%2Flg%2BU1trh%2FS%2BPWFhbgGCYSwp%2BtHvqqLjPwNh%2BTIDbuuk3rPkm%2FxHSXwBt%2BPKRQ8hopttzAC05v8MgMKzg7SWb9cHw3gUpgTPMbfnVKa7VFaE65pAWa9WghVcG2I3LcUXjUddDx0BqsW5U2XZPM583IIQ1Ztg3DXsuy3Q6Fkn%2BD5nL0wDqQMGCmb3Np6sgdLv5bWf%2FGcUz0uUn%2BR7YncfUgjyb2IQ7ZC4iY3TUx5G5v0u%2Foqyv8S2vgf%2F%2BoKV%2FDuOvhwmQv6%2Bz8exrxG2MKxdsDJQ6N58SxZ%2BRt6tG0wrABVN90LKh9SkL9J0B2d4kRUVXSVnA%2FhpbXAB0HhGJfF3WZer%2BxmoWkndqIYqqNNA7Se%2ByLaYLZ%2Fp5VKZKGqS%2BuCnQgncNxsmOmjR72faGJgZTyfAgMLHzgb0GOqUB5ZOnCYMylX7OBXpn90Mzgu1yq2SvGADoRP2R5hGgCfHT0%2Fgim6oS6cIcBOXfrBw2loeYku3MX57SeyjV9ElXmqvxQrkTnbVTEPSWYp5bCjPI9XPvvArXm1jknv7l%2BMlwrApfT%2BDwzruocs5fOBL9XJt%2BJqJY7%2B2NNwstVWxxne%2FBhad9QcqBpNsUw1epZcS28Jb%2B9qnVPuN1SwPHFM9%2FBxwlGll7&X-Amz-Signature=1e33804c44f5b63907df5de3ca112dd768e57d4c24c8f69852cabb5beff25e37&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQ4WGSON%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVBgfZL8zPHWoRba4KLp99mud1uQFFJuHJzpv6Cdx4OwIhALj46hFBBLf4C9914%2FYHZfWBN0gIfPAiL3gxapIpl03QKv8DCBEQABoMNjM3NDIzMTgzODA1IgxMCIncdsuenfKiKQsq3AMea13gEzQ820ngKMSz1lHY1nueORrC9yzQwKATFcibpheHPqD3pxABfNpNuMkUDIEMRdQZp20%2FBPoDBx7naxqjX%2Fnq0iCXKxd%2BE%2FyYfuKglou0m8G1P0tySHxmW2H4UgVB9bnLndz0%2BfKEYE43g2g3ugHyOvc8LuM10%2FnjcXwqW5w3ON3YMeJXEoFDbA36QUYqmBQjKuY5i5xZgL1XiN5WkCBLR%2FnSUGHizwk%2BPKAPjs5Gdz6EI4x62iQ4SVXYwUnjJQlSEqgB7AbdmvbgxW8lZcc2AeQYbMlI7h%2BrVqmSkwdLxZ%2BGkU7PWeqNMd9LrHCxpRIt0SH3woRv6UJ%2FI1XwmhMngMRWmhJHxrRtcOqd%2FNpMfEY%2FV4y6s1qGmCllkbp22mbtyqrW8B%2Fes%2Fbh%2FC4GNPuYdxWKaNszCeHElZDvVZ%2FL7rFHl8A0%2Fsh7%2FiqG7M3NlMJ8cq3lMd2nkoj3ToTFNiXUm88I9nEzfBACJEBwu3M8riQHAmqLActwwqGTygfCbjitPniW7ktf%2Feg0TD2JilwxYk8POyNnkJ04XJqRqCPHq6RDjNUjEWBNqKcS%2BjYMNSu5lAzssw2qP8XZYmdqOn8KJllbXccLyGQDripAtgfdwYVpXCS9taT2uTCv84G9BjqkAZnLMJUbokwER4iJ2pUtPFv8kZgRvKsbffKxmDquwY4LX8u4ON5dgfeYljBV5wl1MHTofeW5g8pRy5w2bm4I12D9zq%2B%2Bb%2FwaCUF%2FuQqC7%2BxHZBxGF9gRdrUBdDhwXTjkw9gubtJ46dnM4NNhonsieJ69VTlfdtdZTX1%2FreoXL1oaKU%2BXxNhCfS4apU8t%2BLz5%2BYB6941xbqIbkeitPY%2FY5mrqSt3w&X-Amz-Signature=724507a6763747d3a78e872579263fcf0c731af7b587c3cc113e8388ca862172&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSAHYVDB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWBhxOgqKsNFXIjkMwwUWONDlbE0mvYBNFKRHBs5W1pAIgXNtUuQ3oRBEULuIuDvNr3UL7ljiQ7qavlkzfdRGOdxcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDJli0QhrP7EDg2DTSSrcA1j2NhWiGPpHUBsVdt40yhlbTnhEvCV4aHZrywBKuX9rnwPVNBglU%2F6jngf%2BfJyhCJKVIH%2BEh0qQ46MgYqDVJLXfQ8JnBjZBBDAc1ZK3azSKO21wVbtW4kL32064wrX0BXkat30F8zD3fHM3apSLNtEX4zAxHiUYOraaOtsmyRcuIHjaEy%2Fmmmv88dX5IH%2FjqARaoPsgzfw%2F9r8IglYwZw2okhtPMmI%2FsHNTMCGyI8zVkQMsd2k0iPdAae0JxE5QukuBA0HtluPxlxlWTYJHu0Nn10CMF5WntGXaLlKljkWlhW7vQ9y%2BWm%2F4X58Rkm0nYyYT7vuaGhE6eVO8lhVR%2FqNteqMSVRhAB4lORkXT16zG4MOhXB6UBxLHcz7IipX%2Fm28%2Ba34ApFIz8zs216rnN6nxdjVAouDFV84jZNuh%2Fg29kkvyR4iLREJW3YaqzlnUcWuuyb97hrspxHjDldvKKUEhILH7iQgNUjmfPyGyJlQYCvJ0unK3m%2F4n3aIgPhExqN4pBsEXh%2BHNYwwzEq%2FGec7iPaeASqL16Ud1t9FS%2B6fWtV9LZE%2BJ3R7Ea%2FCB2HGfqmxRpef1tT0oThjAx3%2FLlpeT55EuP5DNsW6cCfiJw1LCsggnT4ihfWtiElw3MLnzgb0GOqUBtD6NQS1WBxtROlJ4qqtA9VvTPypuKVaP2lj%2Bxty00bwRoxMPHLTkj2XXXlQ8XuPj8yaFU61GKz2BczvPGxQ1oXipcMywyIo1SBTL6qEBQf5VOMbCH29iMZ7so12HL%2FaCFfHPzkLK9ngORc9nc%2BGtxftssWMo1OIS5pI0zLxrvJGy4k6Kh8U2mogcDc%2B4UfXhPQYaaFgGBM91U1%2FjtWLOgXHTsZC0&X-Amz-Signature=e8b0593b0c23cd01c89126df2a371f0d41aedf145021eb4277388ba95270ecde&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645G2CGUF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDCLe126lciBKcBC%2BLnm4xrwrYqL%2BvxnbRS9f8fIhZf9gIgHAT210QOIjObmQPgN3uaWZKjaNacIGnuGoOrSPl81Hcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDBgAafu9Po%2F2%2FLCJPCrcA4VHQrotByRPDXIgrpAfK5Lx%2FIqTwn41%2FviE%2FFVbsPZVSVU3URz%2FaQtL4AXd%2BbdWAyHABwTge%2BPxRBC7W%2BcsiHEhv60r%2Bu%2FTCL54qFt9c3jOxevCMJY3f0pn5CZokfQrtuPpZU9YQuT515Rw2cEfLeJ0e8RsPQAPfOARuDDrqMuRHd%2F1%2FMIUd8HWi1Wu5RjiX59jo9CfkPSezRFm8PcKDOokSJDTGHBQKFf2Z8ruWb%2FlHhUndjHAB3zIwvRSjzO2Td%2BMQRStJ%2BxerCZ%2FImszIVCpvWiwSRBONZSJYfW94jJDnldbM2h2p5KAIZttpQVpzO4sQILayziDknuubk0ayBjQXuhE5BEBFhGs5sxkNv0KFu0tgVoAArQXVIofHBJ0IQ9i6P87AD5sA3Fq9R%2BTBxO2fv75G0RJQBDBYS2B2ERacV6RLHu1zpfU95a%2Bxa%2FNqylhPKuPQX0S1QNXNV3deAUP%2BgSI4CC29ejRImH3ZURKMKz47cNbjXMeOArfjXS5SiBafHjwOe59TlI2IkN9xbP%2BW9ZfnG9itGsE1xWNZB8aILehHsWElB0s3kQiDhKJK1qHY3FwZMnKi2HSafSLI34LQp6NU9EuJqUUb0941wUebiRCy9XlvlHFdVLKMO%2Fygb0GOqUB2mkSgKXyI%2BeanjmIo4KJzCKUF8t1Ql%2F8bgVnOzkgAXGWZi60qnHf4SKx5sQ2B%2FEoB1tfX5FBM6MMcnP2lumBFjjjn6nFchfkbCgxeYF1wNfg2%2FB8QD6Wi7WGbC5TESAABKICF3hS0GSmiw15NhHZEUIN62EVAZGcXTApux7S9MSqiNS%2BGjzlDuxFE0BuA2Ws6AkTNlN0SBazz0Floags1JNu6h7p&X-Amz-Signature=1f0b56559bb5e80fcd879556b75db42ef4c2278633be1ae67c34d9bbbc3c5710&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIR7YBSQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDDDRY3Wykfs0hY0Khkj%2FOv2%2FaPffyzJnS1dIgq3lZ2OAiEAhRBElKaMp4hDV9l%2FPE4ag1roaEHpFzXW7Ouf4cd7Pcoq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDME%2BjAPQPi7npomqnCrcA816Izhlimo%2F8erTOmM9U1JPpSzwdRyrPyysZ5mKkhp6PXO%2BkZyE87J3qT3E1chWBii4bUmxmJ3FMURI7MoctYU%2FwrqG0dhYr9tLvycc8aTArMeoaIFubBWK0aJJwtG%2Bu1B9S9Eyy%2B8%2BmVyJ4PT%2FRhaPKIkuZOVkDjfPY9ily6azB3VLQIfIeu95utdCbvSoP2L0EaS%2BT4qNcSIVz36%2FLWtPfECf2nTN01BVgkmAS%2Fer3maw4VqwNoSiWJ%2B%2F2JlbP7ruwrmu5CwgxRVRl%2FVemFfDCD6jLai1txu%2BidKACvyPBDPJnDCT6liH0hBOb9VPFiTwnIz30%2BZ2jjMxYXgp%2FpJ7039mF8tEepdq79yFJpnwvvnDi6pt4bqr1qVbdtVzobgXgGBlhhZqTbET5kgGvNH9kVAcJDHEzQ8E8l%2F%2BWQfxiHBRp36Z6yCHUSDJrPx0exclfW4FuO24%2FDGXQ2lf4AUAQj4stwoMf36HjwpMQnkVrwmy82tlTP0r44BXMwZkaczkH1zeezhwVSkicFiJZ2slVrOb4tJZhcp5h4ZlbTo6jo39KWk57eFwlx4m%2BsEwNcG2ji2GaDqGC9KHapZmbQzbvAY1%2FAaL4xWF%2FXKhX6xLNcRrKyGDnygKXC%2FmMLfzgb0GOqUBnLraze%2FrbuuM2%2FKwe5Dj8EbUMO7KqtOukYqn43YnNw24IjpyB6EjYiFB2RaAYFam3lkBajh%2FsoILR%2FRBvqEQD4po0AZ0Sv9n7F1fEujtKglWuAalwpzT6NHQAYmgD8LllxCl%2FX2F%2FmQpLLOyZVbGeskVvkCBo3KPjX1Qpo1WhHT4d9arZdHSfMcQ76T0UhESf%2FmXrv8uKrDMIyT0NN8Uv3GeiNzp&X-Amz-Signature=a8f646e39c90d37479640406d2bd5b262c16e99f4a9aca0fc6e2ef2a4ea653a2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOZU3GCS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBEAMkQVambeHeq4SjOyaFi4gHEDwiKA5qJhIg4MmQmiAiEA9VXDPcuMn49Ow%2FWYz4sFi6Q7M2IeY3D9Pqw2vaVG%2FLcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDCXyCIs9mTS2BlfEwSrcA%2Fkxz1MNjFBVGlbT3B2mxPivHdW4zL1RmSJNqO8v1h5UdD7hr6ghyncmq2H%2B7GQ85k2mxTYg9kXdgR%2BucdclPHsRqfQK3RhVZIbU3RUEqOZxyZBVYStEeDcwjpxgoyKqeMKIqz2OvjDsLZ3xY%2BDWlqVnG%2F%2Fkdqt9%2FcVxrspe9T5IfORQdjkn6CXvtG0nYB7TH1xbz8zdGkwP%2FP6ltkMxNx6Dc%2Bkywcm2hNKerWRIXyzHAJ9X%2F%2Ft3Vv8FbV7XTe6SDsufWSj8T6Yqych9EMT0s71O69wqrWMQwwIk2Zi63tlJ65Y5ec0JyfpojlzINEaUcBdB0wySrloRrqFpfsvUcDTJotiK8pKsTfPs%2BMVJkf9XgcOY17GvJLN2IJhY4c518i%2BIYlVEv7UIHdq2WVU5h55csYznSn4uDgZszSVJcdWPeoIxkevA%2BDcshu0%2BTwcypc6lB3MaUBQeAi29Yx%2BvNbk5gIubfcL5GbrefGIYtMP8ytQpq8YfrIU7OmCjzKGaX2Ooqsox6y6D3lljnI0Sf788b0VfbKpbKzN9TK2ZYiz4b0ZVGLCEzP7zc8TAoi7i19ctlm2p3G134oeuiJyRROXccoHWyGNkd5h7%2BWt8Ou8Tx17Zvpt1XWvXBovvMLfzgb0GOqUB5oYdkN2biLJviqwWTxP5v76ZGeBc0WxIz2nEWmHjbVR1FBMtqlEqhSUHgSmobV8YBPsgxDqPPLduQzFna80g6vIFc39t%2ByA5foNIvPaM1bcg6yq5BJMMCuovlSaCnXsc6BQ1XmsLbDCRVk5HWF8Zyzp3P%2BLxcENpGbT%2B0cboGDf9u0hNRoFcaEknJnw2giP1WcZgYeJzY4k11Tzmnxnghb51zWoI&X-Amz-Signature=90aa877460d6915163ede140aa435546dc5f600451a5552a351bc65d5d911c1d&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPBLIBXW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaa9lvYLPI%2Fnb0IXSOOuVQKke5tE7Ykm3d%2B2hQqQPpCAIgPTs%2BCMzKzys9tFDwReeKY6GfRlrNg2v9Il15vPz%2BH1Aq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDFiH2fld%2FU3478LXhyrcA0rTxwk%2BSlpNBCcfrQk4w0tIWz2z7Dl3PATUMMu6iSUW3Mt9GgZMA1HiY5%2FhJpG6qHVuz5zTiWaZngjPqOPrDOuwZSCOy4fDkVl8pJ%2FqVacTdCZFw%2F6I2I6d%2BLe97b7CHXlyBWDWTQGLzg8WGNtpaSmEQTTeDf5gAyXqJoIaQ%2FzUxEGEISEP%2F1FJlo14y9en%2FGm9gjeM4n6Ypq8m%2FLbF8ZiRWucIzVrtdkeytcYCDaXSRYG7xHvErDdetL8o1Vch4tNamONouErUuRoGK394xgVypZH71mX98EVZoYIOSbQgeFE0UzPX5cIlSzf%2BO8uMpnhQOBZm6YuYoZv5C1EdurUValefBkf1zZaJ%2BJWEwQbHg55As%2Br2BB6Q%2FMZxqypko9n6iD8LD3L%2FqnVjz8e3gVEFExD%2BykFI3qg%2BD%2FrYtqK4JpOQWGIlM9GWd0rjfGyBi9%2BzF4UAYDPzoROoIPkz%2BPbsDN%2FuFstbIQOe%2BNgG9FHnxEa2SeNNzRsfv3c96NSQUZmInq3FCPJn1269iZ1bGW6kZi9nKceqCSp9BgmCxWrn0TMsDVZIUV6mVcLcllbBXtGMpco5QzZhKikHsul6e1R%2FUpzo0YCOilEyKjUmk09%2BcJ08AvSOBYR5d4g9MLbzgb0GOqUBM371rspsCMaxtLP%2Bmcd%2BYOTWQeLTJdmf0z3694ZxDZn845%2F3zU%2B5e7Hps6hrx1uQWyvzahld9agehG2mzhICDm7ea5tXEOXYCP8I1uljux3MZSYE3TULo4Z56QaudCC59TCP0OdJNYK8Y8QIKbPvJVz7h63QTsWaDtFKtKKtOJ0QSoA7YMtE5GA3oHaJ%2F%2FgX2%2BHL7xJBPeXVbuDt2JhtFK3aSMxe&X-Amz-Signature=c8fc162f9c82d56a7fc861f2595597609f0a98a5fb059cd38d7e77ac2d30a8d4&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKCEQD7T%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD67HhHBp2bQMIxbYtzXbjgTxXdmYgt3%2BzvqWOS1P908QIgbh9jGnuytwAKSYxKyEE6CSpufs6fRqhhbL%2BjkNZ6m3Iq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDF1cnLNNhIKr6FKGASrcA9i1ZWX89u4PHz1lC1vF8%2FMsIM%2FT3H5yt1B70DO56S5gWnflow7C5nz9lwLgW6kFP%2BSGZCpO2j%2Bfsjw8AhhjjsdkLt7owxf1FNQFRuNAc7DHgEoi3J9Kr3vzEM8H5Mo8Ve1sZZmYInBH8CW%2FWg1EHX%2BeEUsqAUp37MF%2FllbddBGmubR%2Fg5CpxrC1m8dodLS1GCHv%2Fu2qcTmunV28FZq%2B5H7sSXeJljpZgZPT6TGYPtEeByW80oqghklzFqGPIAqP3p1HVuMCKN8ZAR547XNaCMcvFJ%2FWS0uwX%2BR9Y6JZRgZsjELNG1NM2SzDSxJNsz0RHm6g0mY2vVH%2FhGW7nXLfwmCw337ouP6llsZvVshOUSvey0FpVl1nbl9nOC3cTJyzwppn7F7lfjww6SzcFLzgt1fMFfNhUmXvNOY%2B9WMU05uYABmrtm%2By8rWAb%2FzyzX68MtqW8DZlDAg%2B04MEGB3PvLB86SyOhA82%2F6wveU5Sp589VvQMQiIRXBegsFkaAtiATaiUoweZAxo%2BdSHEaQqNk3%2FoSjp4pmnwoaFEqCeYGST2Mp6w%2FaDeS0%2FCL3ZXgaba8UZAZN1g1Lac1HUDEeqYDteU%2BFdrWGkXeEtLyLrmCwRvLu%2Bn%2FLrYeF60azhkMObygb0GOqUB4INk25XMdR3BPjqleuaqwl1GfOAjI8hL%2BFE0BND3Cj%2BdhdSlKqU30VAq%2FaQ69h5Cr2ZwgfRvTAM012HXofg%2FXRFbdmX9GKZ0%2FqsJlHgq%2FYiDUZbJbeXGMegJGscWdEb9%2FVXGQNCr07A5uYXZ9I3L9PoELj8IciippvAtDvar90M28mRQksN0DKHYDexnffFzeddBlIAonCGiKT%2Bnpp3g1w3HGcLv&X-Amz-Signature=e20b7e2914b8f079ba642a6bd7dc615e402e73b2c78de53be42292f132f6753e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIR7YBSQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDDDRY3Wykfs0hY0Khkj%2FOv2%2FaPffyzJnS1dIgq3lZ2OAiEAhRBElKaMp4hDV9l%2FPE4ag1roaEHpFzXW7Ouf4cd7Pcoq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDME%2BjAPQPi7npomqnCrcA816Izhlimo%2F8erTOmM9U1JPpSzwdRyrPyysZ5mKkhp6PXO%2BkZyE87J3qT3E1chWBii4bUmxmJ3FMURI7MoctYU%2FwrqG0dhYr9tLvycc8aTArMeoaIFubBWK0aJJwtG%2Bu1B9S9Eyy%2B8%2BmVyJ4PT%2FRhaPKIkuZOVkDjfPY9ily6azB3VLQIfIeu95utdCbvSoP2L0EaS%2BT4qNcSIVz36%2FLWtPfECf2nTN01BVgkmAS%2Fer3maw4VqwNoSiWJ%2B%2F2JlbP7ruwrmu5CwgxRVRl%2FVemFfDCD6jLai1txu%2BidKACvyPBDPJnDCT6liH0hBOb9VPFiTwnIz30%2BZ2jjMxYXgp%2FpJ7039mF8tEepdq79yFJpnwvvnDi6pt4bqr1qVbdtVzobgXgGBlhhZqTbET5kgGvNH9kVAcJDHEzQ8E8l%2F%2BWQfxiHBRp36Z6yCHUSDJrPx0exclfW4FuO24%2FDGXQ2lf4AUAQj4stwoMf36HjwpMQnkVrwmy82tlTP0r44BXMwZkaczkH1zeezhwVSkicFiJZ2slVrOb4tJZhcp5h4ZlbTo6jo39KWk57eFwlx4m%2BsEwNcG2ji2GaDqGC9KHapZmbQzbvAY1%2FAaL4xWF%2FXKhX6xLNcRrKyGDnygKXC%2FmMLfzgb0GOqUBnLraze%2FrbuuM2%2FKwe5Dj8EbUMO7KqtOukYqn43YnNw24IjpyB6EjYiFB2RaAYFam3lkBajh%2FsoILR%2FRBvqEQD4po0AZ0Sv9n7F1fEujtKglWuAalwpzT6NHQAYmgD8LllxCl%2FX2F%2FmQpLLOyZVbGeskVvkCBo3KPjX1Qpo1WhHT4d9arZdHSfMcQ76T0UhESf%2FmXrv8uKrDMIyT0NN8Uv3GeiNzp&X-Amz-Signature=2d05af57bc509a2c977fb975efc962000f65463cf97e82aa67f0d8cd77f8b7c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6HKFDMS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDE0a%2FCq43IaleCj%2BdG%2Fd0iqgYq%2BLXrPtpk%2FwaV528CuAIhAIvNAaLlnEhM0a3VOXnu92E5mDyWvu%2BKtgzMMPUo3IfRKv8DCBEQABoMNjM3NDIzMTgzODA1IgxH%2BjJ9clFkOS8snQIq3APWo2spP5KNJTawFJ3uOKb92AJCuZjjPhtB6LttGYmOd0aaSmIMhSl%2FofJsDy989EUAlBymLQDjguS6bkFPwjC2RnC1QL7B7dZ2FGc8rVoVGDruuP0RnkUU9L7%2BFwmEN8kbQf607JuE4ejSXdhOljrm4UwUH95ioF2y2lWw%2FzFaxjcnjvTfczKGpvpTcXQA05793qLaOFPddUHrzCrAsu7CdpDZi%2Ff8BemJ0clT%2FkIanUvO21%2BgnVHqp5lvkCCymEmLOxpH1Z2fArDMKYtLUNLmGU9r5AfZhi6qJJbrFXY1vco7U9XjkfJAdFiTNiagHLdzpbCsNaigLcGNpIlGI%2B247NQL56%2FJs4NT%2FZenX3SbcubrpiDXrm1B%2FUWeKNjhiM0KkYey6V91qLvLRkNyf1%2B1kumZDAh58bhOR3WHyiIYI6WxlySJ555qnctmge1jWkeUROunfgjSnKVOgaBHlNxfoLt54X13PHY2o0iHr%2BuiRU%2FFf6s6ZuBUgJBumqFkhUqvxAC5VRJI1cXZl%2B46bLQgdNtbVNHAUF%2BhGzx3yhCIC2abEaHX2uXR64%2FZK0YJqfxVY0bt18hjy%2BdhXEGrTvHfDT9m%2B9od%2BabvUDmwjh5KZrHnuQDcPGSFbQd2ojCP84G9BjqkASjVdgtAircdBmlMN99XNz1uQCF3cMiAkgaTDZlbsmdPlGZXi9wJ5iAvYihnLrEPF2F4Czx7mQ6RaXtDfir3WyB4b%2FCF3882ywYeDxHMyFckFrF8TdjvIpoWQa7wLkqm6HKDSCkL6ayOnSMFI4kAyy3vG%2F5AYuCqJDBOybW2I4BfITGd1WPlTzWZNAZJgRXwYwglB%2BEQhsfI7PUJGqYM8dJ%2BUKR1&X-Amz-Signature=f8040cf6e32e4fe9d4664d01c793c0423915f15b1e5bf5c06bd11c0d9e686245&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6HKFDMS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDE0a%2FCq43IaleCj%2BdG%2Fd0iqgYq%2BLXrPtpk%2FwaV528CuAIhAIvNAaLlnEhM0a3VOXnu92E5mDyWvu%2BKtgzMMPUo3IfRKv8DCBEQABoMNjM3NDIzMTgzODA1IgxH%2BjJ9clFkOS8snQIq3APWo2spP5KNJTawFJ3uOKb92AJCuZjjPhtB6LttGYmOd0aaSmIMhSl%2FofJsDy989EUAlBymLQDjguS6bkFPwjC2RnC1QL7B7dZ2FGc8rVoVGDruuP0RnkUU9L7%2BFwmEN8kbQf607JuE4ejSXdhOljrm4UwUH95ioF2y2lWw%2FzFaxjcnjvTfczKGpvpTcXQA05793qLaOFPddUHrzCrAsu7CdpDZi%2Ff8BemJ0clT%2FkIanUvO21%2BgnVHqp5lvkCCymEmLOxpH1Z2fArDMKYtLUNLmGU9r5AfZhi6qJJbrFXY1vco7U9XjkfJAdFiTNiagHLdzpbCsNaigLcGNpIlGI%2B247NQL56%2FJs4NT%2FZenX3SbcubrpiDXrm1B%2FUWeKNjhiM0KkYey6V91qLvLRkNyf1%2B1kumZDAh58bhOR3WHyiIYI6WxlySJ555qnctmge1jWkeUROunfgjSnKVOgaBHlNxfoLt54X13PHY2o0iHr%2BuiRU%2FFf6s6ZuBUgJBumqFkhUqvxAC5VRJI1cXZl%2B46bLQgdNtbVNHAUF%2BhGzx3yhCIC2abEaHX2uXR64%2FZK0YJqfxVY0bt18hjy%2BdhXEGrTvHfDT9m%2B9od%2BabvUDmwjh5KZrHnuQDcPGSFbQd2ojCP84G9BjqkASjVdgtAircdBmlMN99XNz1uQCF3cMiAkgaTDZlbsmdPlGZXi9wJ5iAvYihnLrEPF2F4Czx7mQ6RaXtDfir3WyB4b%2FCF3882ywYeDxHMyFckFrF8TdjvIpoWQa7wLkqm6HKDSCkL6ayOnSMFI4kAyy3vG%2F5AYuCqJDBOybW2I4BfITGd1WPlTzWZNAZJgRXwYwglB%2BEQhsfI7PUJGqYM8dJ%2BUKR1&X-Amz-Signature=0e6190e108c25c3622b9a940a2f0e20925d5e01242973e81326d1d71da3fe34d&X-Amz-SignedHeaders=host&x-id=GetObject)
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