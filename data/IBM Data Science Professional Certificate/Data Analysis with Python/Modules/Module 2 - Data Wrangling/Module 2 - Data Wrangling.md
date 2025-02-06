

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EVMOQ6K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIHyHF3THV6QMMgCFcpM9nLkdOQLx%2FMKJxNV0EQKuekmjAiAXV%2B7yGUv6lFHOZE1t%2FluUFCQw6XBGcMBkNrBljhsCHir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMrWKnURBY9R0NNB28KtwD6UI1fO2VYe19gMWyu7slpsm3OgnsSoTdwUIyCgrqJZy%2FvaX3RpvjBLY7JraeW6Kfs%2BG67bsB9O2sPVCNNVxjFGJ0J%2B23mN6VMMCKOidZ7mN6nXJv5zA3HOhmeq1Wl%2B4j3ZlDjLRYVRq2ycO%2FmypUXIr2iIcVB1Ye%2BAq9tIWPgj%2FTsYNHSZurhCK%2FUM6QoIsxR8d20fA9ykq3LeMZZl7w3BSjjnFe1i1S4NfaXJDfBej5ejgRCEzERIofW2ydbPGfV1ZbXhcIs8nKyQmvGHFIMP8A5uoZu5maQ9XqSA2Y6Pm25jjnq7QrJMIxs9nfwRuUJYg8dbgT3E4GYAghfNRmoJ6k%2FfIOd6DgtvqYBd3VpOgKrsawMIWLvWpgRbT2LhIDmmLe0nMNO%2F1w%2BourLYTds4u5kg6W1oJoPDC7vNY5pb7KwOVEKx9XlcFF2CbyD6UbL5%2F7YF%2FAsTwTIlwDUy0m9gQl2EiHwxfj1Q2CsA56XilbF%2BESAhqdQzeR%2FzXFD%2B4yDBZ8Pgm%2BpU8LbGVjttqRMc6jjgdB%2B9sp0jqgc4h3hIY5%2BARKlw7lSmQsidr5MqCwRFNXlnW65gmUbteYJSNvM%2F99%2FUirF9J8d1VQPcNEXmcVbXdLdeHB%2FHQo98sw%2BcOSvQY6pgEtNNOvRXagOOM6lFDcpTIrHQvVpuXg0LXJ4l4Mo86DysZk2zHEoWQOLoWcv9hUbcSXbEH2VDDCz1ItM0BrpHJNObmPlusWaR18fWWr4gtTC0%2FCQ9qfiClz%2B2TuJBDib4rHTcrBtpPQQ1JGH9KdLUYhQHFKbdIshja3JsOC%2Fh745X%2BDhQN3kwiM0jdYa5rZ4MOlHvLp8iDiDsekME685Wv82bHneZCA&X-Amz-Signature=4bea8f5cee1d77fcc08c39a39f5dc4ee335326af56e7628e226f742bf1a0dc61&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTLE3KZH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIH%2B5S205ccTOIc5DklPzPe%2FU8RnWTwWhCLUKcUIwMaBNAiEAqq8FdKM3FeAUUV0KScFZyoLCaU7FPzZB9u3MEd2UM2wq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDL29Rs4gMSoyqRuC%2BircA%2FDb4xWN4P%2BqgC9%2FSzyhXrLGeJWo7ONXnpoxJxBq1ixV3uT%2B8KrxxqKFLVm82%2FN6reWII7pv1pJU57LL42qKKF2Ke8gs8T2OT4%2FekVXzCLD22UHvR%2BnzEwFlZ12qdzf5Aes9JNQwKN6IWCYkaHoYiPP%2BnjfaHfxv1FYw6itaFEdFartlRVey0S3YJ%2FqkDfPuILjQSNTD%2FO6FrX%2F7wJpaH4C1pkRzPY6RX9quS23ii%2FQDgjMX2ahDia%2FMJr98PiFBsixm5d9pGlR%2BELClK9VGDXr5K3u8hrLLQBNCBEQvybNsdEWCClXeU%2BZ32BzEyjlnu5%2FQKUCewc4OjaHkiYNkHL3ccUkya3FZc5iqAqv2%2BQYhMcGD9%2BZ3StGoqwEG5r5cyumvJ3sw4rh54dOndiEsZo5vd7paRa0PIYrWnZwo0oOOwHXRtvGz4kMuO18okeomzbzMsduTxmXzrxpJYxFdwLBg8W5fLiG0ANZt30rcr6frF4ATBPVFPcIXcY8SfXHLWrRrEJGorg5RJntAkrvfp3nHVxFr9yutKjCqoFNs%2B98Rz%2FMv4a110Uaz5mopzfvwhpdYQ7RIoUznmg%2FC3t4V13ZUPp9EYvc0V%2FQpzilbt1voR8WBsLBw43UEJxUPMI%2FEkr0GOqUBlAd0XzxDBSa%2Fbcik8FC7v0toGsA03yKBiDJ5kjjk%2FCBGk%2B1FbYJKh3IUP382pZSnPCSywlstK7NdTy8sd1tLVfQMt%2BF2CY34KNR72KIehAZrr75bOHRrLRnP2Up7GkPk%2BRnkBjEgMhX0w0Q9Wso71vWGp4PKI70zJ65IlyqdivP5TYy1zYno9340%2FJhNp8yhcbncQ1Xw%2FYoOX1LDBE2iONrergee&X-Amz-Signature=d935860d7973a8a72fb7d49a5dd490483c52fc582baa59609fa4fc8ac7a3a051&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBR7SYQ4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIE3stjOgX3eYS%2BSqxBFE4J1Y1JqYnyF5%2FkETPOtwhnh3AiEAyTuwXHD6V%2BMADXoXg%2BYFAacx73gEI7%2Bz0MSE7Ogm3B8q%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNJcYYnPePW3KUIhiyrcA2%2F0%2B4yhOCdOTQd0PFcqaT7A%2FAsJodkpLG%2BhMNNuFER89UlX3zNp0znTjrAPRc%2FMcUIC1jwQWBv%2BzCahUtjX393hyLgX1PSKeawy7z3Om70p5j9vCcAUwal%2FNCA9ZtkPx0NfXV%2FNOUGWnGlqxdUuNQ9ff1z1pTUZAIZchNXAPBu8morG0MfTK2YQfMNwf%2FyEUsuFfSXYcPxNK2Vysoq94DrT6Zhi07evClfQekmXxycc%2FFcaP%2FZK8raYBafdnbUMZ8nHkjzcngrWdfGFADyjaJ2kIVzsnkEeq3Xu3VC0wt9wn8y3K1kC%2BAmO%2Bdhv6PGPkwkd8VavoDjDkrGygmQXhcxwGhHCWOFecvKGbLjj%2FuqPoRT5eUPKSDgDQO02XAqxxNHsErEFyTVnaNYjJpjoA8tprFZo9jj0GRKFZMdeDqLfF4Prwl4LHYKkc9vS8GjB9ISug78olFqqKsvqIQMD7yLQCR7HsHntWXjVdgdLhEpQlcwP9%2BFprRFMuWuC64X6v5cNhlwPxNQ1l8QmOgekyVZi%2B0ZnH00oIohGxqQWu14%2FHNIsNHwK3vcj2z7%2B%2BPZf3AqzaMlUyxl3bLf4saxlnMo1PGosbYaj%2FaUKqXoJTnVzAuajX%2BRLbOxVl4EEMOHDkr0GOqUB%2BKITEMur5acs4%2BPgXu98tl3nZgA8Nht8FwStyO%2BBy9H2pfFgNxiOUPVcbIA8bV66PgJWm8B0VO17A%2FOrc68MnIdJTfroC5bs96nrsqot5dxhouHQoKsw7Zm6MEp3Xyit2iuGgaMXooKDs42jP70M%2Fsp375TAU6WZ0KkKF4rtSfloSrpRWmlLGUoWJfKuiPjvTRLjfHdkxyuJNepQaypKZ7ENR3N2&X-Amz-Signature=e14302c31026be137db9e96b024f66b9c25d0bfa72311baccf20a4000d026b8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAG6NOBC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCr%2FufU6VrG3FprFOLyRYDnbh0rxnUQ7kSEijUcA8mrpgIgEcB2ID0tlhOMIFWL5P%2FEW9W6f3c%2FKmV4ZIRgOPtJ3sMq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDDgV0Ml9Kc%2FD2zdSRSrcA%2BnpKDf5cOc7NjVJ9uaxZ5PKirWDApvMqpfs8wrBQJpoiEJea02l6d29hPCtpSb2Hw3ffxpg%2BRHcrVxKP%2B24VptrHErWb2YVnayX3otj6W8woq5jD5pFx8ySPKksfWlshtbr1ScAnEZG9NGlr%2BgxMEv2WtrtHLkhqfF1QXudDWP6%2B%2B021sDPWRq0aF6k%2FdCyhNox8NNrPzTYtxLQs3iB7hGIOd6z2qvBQTECyBIETlQ331D3frRWpyXp6NF8TtSErSQwX%2FIhTDMfQRXvV%2FUZr78F4bi8XqdkuI3JYk5VY8xc3za8g%2F%2BD%2FjwG9%2BQ3J%2F1ErZTguf98%2BTZGodIpYXJq63ErFFPDfjTC0nlUwq8ocwycUYQ1p6tqai89JAHMLWmjOFtOM4aoWTltfeCTHk3ooMhJ%2BhUSGTFmuIMaxPkRI0lLHDABNliUNxRFmS6qDqpN%2B4W1jUCbYqMZCgoOWbufjcHrAWAyL1EYdNiLsQbYGLJoHz4Al3xMKrq%2BXgcxK25GYBrMq%2FnwO3qQsrvMiSDxHwg%2BGj6wchJ%2FVCj70P2SW3AFaMbvftX77wfTLqcLCS4Z3Xhw%2FSdTEFH%2FfHiDEYEAZ6YW71VJIF6tzUK9AvFfO1rQVq8r9EHBBKs2UIXuMLnDkr0GOqUBonZZEx85RaGrfRoYtkq8KXsgIyK9cN2xcKjNpRUUI0qTckgUVkLw8gTGu2TGfxypxgpI4oJZWOCcbMkrjMmWcL2qqyjIrYjmfRdA%2FhEptaMIEGmRrwV%2FZeLORb8VfE9lToKttRWhpw1pLHfUeKvmQfFPi5iPUUVpn5cJviOYP%2FuiRiptI9MKj3Phk3S5hCfoy6oecW%2FskjbqgdCTqUkNBAhkON4z&X-Amz-Signature=a3e45af54c6a4b7d5b1c4d57a4fd002cf4d981725dd4101bdd713b9b40304210&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZLZBMRS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQCQEWrH1LZcBA%2BdPmW8d%2F71KjKiVCNGD9JEE6sd6F7DUwIhAPDbjvzTh6fW%2Bx3AG1sL%2FivijHQqhJ07Tmki9QkH6dkVKv8DCF0QABoMNjM3NDIzMTgzODA1Igz0yImv%2Bc6M7wVoLbkq3ANn5NwHsvmyKfF4obb4Zj%2FtbB3PD462ED4m%2FyDohen2aaySBx9Q0uAStILT794tYenqPyVZffoKynmatz6Xtx1VWZRUkOfpjjihQ2Ff3XoXqkA%2BuAjm1Z3Sz9xOVGKfBoXpXehzlVbWUC8Us0kEVgLF5rdOTYZXLCaA61YcYF20OXJfFcQiAvCTkrShh00cBZ2oFwRBPaTbfvt5mUt9QRl0Q6eKzRXUSBcy3OL3aMO1QUltx%2FtmI67xwpIpkg5IrPLRUaqnkhwpEyielI1Zlu4Kt3T4CZLpfVWhXjHX4j8IhSc4hoVTEx4ZZoj1Aaz61k7GSnxhUd9Ly%2FYSL3KzcCZuCrmUp8h36NX0mDO6%2Bsb6XM3DQnmndBrKNn5f8zDT1sfXQYzu7etketD1bqzgTEhaSoJBU7YG83ipWSO%2BEEVC%2FMMqmqQGSbsr63cOR%2BJxZZ0X0%2F%2FJ5ieDnNukm%2FqFaXsH9OexcRhZMPep3R8%2F%2BkGyvmm3aTRNrZi37u81FtjkvXG%2Fc0qswjBwCfJQkuiXyTKGCbbD7cpVCuSD2sAWhBVxaj1rAxtqvJv7m3czk%2F%2FbxXLf3%2Bo8cfWBzZEvMP2dwaU5e%2BWa3t%2Bu7%2BxdcJnJtOusr8oa9vf521hbyAa9CTCExJK9BjqkAYA4pAKdP5xuZo5r2p4zDdzHTUF5kfnRW1xUgNkDgxCrwHkrDZ1NIKsv8APcuUb05bK7haQoOZn8ZrF6Yup1x6hjkvq6vStLBNgK%2BDHHhGl3wTsQbCFI9EakZYclIdRLrsB1Lv8FoyxjCJH6qlH%2BakvyzOY8OJkgb%2BynLxoa3WaoVGZskG0hcuMsMBzyFtGufSiklaqWeS%2FrvoOTQWCdEHqvRjP5&X-Amz-Signature=fbf9e50d2f13987407875bfb7c666a53330a18f29998c863f4700a5c2cee82ed&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQSMEX4X%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIC8w61GIVh7yaIGikkat0t1YpVxd5qHMM%2B%2BJ9DwUxFihAiBHO5nFS9igczCZJUjpRT1%2BmAHECGO3tWjewXvws%2FA8Vir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMiyDlY7YPJV8tbAusKtwDx7X1EqmjZNnftl3pmx5g5DudkGDVkPZ8Tg1vfq%2B3WIWg%2FmwLDDY4coHnzVU3PDjJrA%2B4lyGkKDqr5%2FZ1r2YWdWx7SlWPbh9AqntC1nqCZopQk%2FNEgJqYoJ9qH%2B4bssMSGIVaxuDHGOYVsMeG%2FeLCZ79kJVmOBxI91cA%2F4qt%2BgOEVQOnoUaBdW8e1MFD4PLjt4mBZ9tCobMwbgzw6G2M5QPiQr742cVSSLqXH%2F%2Bh6TiFe4tGEAgd7bWqCnaK5FLG3tX9xQqUEGhbRGcZqY2asMSK5Ovvnl7CTxUufjcAxCKeqdnDDmTIMVRa87XcE4uOQ73p65dDZ40eun2L7l8wrNlNXRXS2dUwPcny5aCPCKN9evvnKrudwl5Mu325z8IGn1KxSJf8QxqLaAKSngwmRYvSb9zFub%2FwrpMT97HrNGd77dRvIiu2hFCP88XbAL0yibeaDJZ3GnddFofycmybzCcYRdU3A1wGOltIWu8NNqsNlaXcThKNEriOkyCkZ9l9vrkZlyM7P%2BOz%2F7UazOaMycaEEDsWOgeYtNGTL0safGS7biHIdnz8jq1XgbW%2BQYwXA1%2FLgaEqEfz3Xs3J8NliuvEvXSkI7bVsCoK4MfDQR6W61o3GedaMXpf7coP0wuMOSvQY6pgFKmqhjsv5LXFCGbr216iEAeKixnEokp5yB58ue%2FM0DaUhTZeBCyxqyYZSbapDzfNhPT0ckgIx9Ih0KjDzmaOfLhjAvVAz33Kl3P3EYlHdNFYuMP0WexF%2BLWndmw1YiPU5QWxrCF0LtxpKv3hebhEF%2BmJaAI%2FAgHGjIW7WLlhXRDRSw7%2FKA%2BUERJjKn7PekkzcWrEsm%2FFABjzNdKYbb7nEUfGY12Luw&X-Amz-Signature=3602bc5a44348eaaea7f1518b5a8b7a0c80afd746ab9e2519277f4cac6a8846a&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6NBOGK7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIEu9UiWk7yGV%2BUa9JpjdaebUyPgoVD1jMqGvz2IC0FAdAiEAiDxlYXFUefVfVRmuomEYWk4WY1vFUkzfc%2F9bM05j830q%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDPSmjipvaWofFw8L3yrcA8JdaMb4paarHpFv%2BAYjOlxv5k5Awsr1U9vBpRGn1AUY5DUdhZTaNzivH5ZI8JPXk410BSuaCLogkJFWrkbEmVze4VIqm7NmzaeymTIuPdSQ44s7FPYcWaZQtOnYa7X%2BrYmrGafiQrDv8m3B%2BqWP3geQuQqtJytuSgOSBQZqu4iRsDKhsGiGhPJFk2WayydOQVve563wVtcs4sz0WmFqQwvdPS7olxdlzAT4pg0s7dWCjC1LUgJ4mgwG9KSEiup4bY%2Fml9UthL4A8qvYLy3EeqmzBHMG%2Fw4oz%2BmlpR404lGZ9YpdNJg8M9w8ksCgEjGwtMrjkerIHgs7IkeBdkRtx135mJ5WJpT6jthafcC0J9ylf%2FKDoEG4Uym5fXaLjV%2BVmFHJjhwMPbKOlN%2BG3MRljy4yj6sFkgIQIZjUD84wsl5z8UtXcVmZaR9qCrXFdlblU1pxam1hWIoyKz%2BJQ9jUdjCEA1P4u8wCgECTthCPrPZl39%2F9uDAKRTi7DYilfV%2FK8nIx2zdIGyJcEetN8J%2Fvc2XZhNEZ2lynG1tHCEJT0aRcwB8te6dFG0AbvXMpFxqhWy58oA24A6ElHoWhf4lZIuqx4JyDue39rxUxpTC5JQ8ZEzD5HQ0W8zTrHxFHMIzEkr0GOqUBkgWXwO%2FIAycnb4Iuc87KiRPhoLtk9gVIyJjFq1yYYhGsNT0l%2BvMwXEgB0mL0yGcbQovpN82gToGOCa5KA7sVG%2Fs%2B8SXRmIlrOXgsXx7TIYcKQiaV%2FWQ4QI%2FSTJyXvRPjGKZbMoR7fht%2FentWhetdA%2FGx%2FOo%2BQb52xt4fPCkEV7%2Bn6QiNGoemPhedmgcWWUItYVgST86G0u7jANzpLi0efMyuLBtR&X-Amz-Signature=f4e2bf5d0acbb0a1e6bffcecb2f09eeaa337326465cf039d3d00e098aa41ba51&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IO7ZZRF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIDAwsEHRnOnqHH6rhOQphjcj%2BArzE6iZqFo9yM0wfBGgAiEApUZHr5P%2FfkJI88LvgSe3owfg%2Fi86cuivoEH5WIZl5f8q%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDInE7N5FgTa83jJ2CircA8ocoJmmKDmQtRsFBiCuBJZEHSwfhXxuhz4xIXe5RzqzEUxnjJ3btpWmMNWyV7i6I7gleBUjW5quvZCAs7jX9inycz2okBIozCX5%2Bd1MdSNw%2F8hGQ5OfE6SnKpyVeaViyI6goguMg0oCyxBXyTDbGxYXNZh55QAquq05yw21nLSlAEMq0h9QVn%2BYtf3vQ7D%2BsUH5uDi4qymYbCUdY7hdQ5NXatyw%2FmH7g%2FkWHzYq0W%2BtzVNBlqCO%2BTVywScm2%2Fh3qQzbZWVIkCVSivsVNqMeYdDRpTfYGsEfgNC0dHg%2Fr3MRaiEQINvXpWnZHHmeG44Lck%2FhYpq%2BeG0odvGOZMlvYYd906i7b6NyN7EtL%2FLMywQdJdGhyBIJBQnztF4o6z4%2Ff%2B7Ws%2F9R%2FMxHX6UlC2CjocrsdH1iG15IRQzYhkNcPFkZdU7ZrMRduRtdE4XVmzEZuSrO1OoW1Ja%2FB751d2hNktkqvafOB01mhn3Gf%2BEM4siU%2Bcz%2FPFqUacY1%2FUQDMHaVQARraBtZib5A0oGYpR6WfFtFWi5PeJE7JZD9yXDmuKD0y0V4TgfrKUyvlaLvNn4FdaVKJA7bpPQdXFeOZkTXHMNV2MbYf2YRbPG4ybOWK30hf5rB1xuKy136sznJMIzEkr0GOqUBJ8m4SMIlJbkIDwlDiDwkc1cL6o8nsbmLw6idNrEQXpXwZKa4aUf%2BQF0El%2F%2FtKtaqna2lREU3yiZlrMcGVgwIg%2F3doF5cwitAheGbQF4kaEJWikC6MWwZlLCsk59wlodiXtgHnuIasKJ77%2BF3aA%2F4CaK%2BLhgk5H%2B0XRcDPeaCed2MISCrNg1VZ6%2B%2BGIA2DIAPfyrfENhHtNjKzhC0LXOqO%2FK11SY7&X-Amz-Signature=e799178a04514947393ac8843c255d3948ace85313e8c328ae934ca3c6016331&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZLZBMRS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQCQEWrH1LZcBA%2BdPmW8d%2F71KjKiVCNGD9JEE6sd6F7DUwIhAPDbjvzTh6fW%2Bx3AG1sL%2FivijHQqhJ07Tmki9QkH6dkVKv8DCF0QABoMNjM3NDIzMTgzODA1Igz0yImv%2Bc6M7wVoLbkq3ANn5NwHsvmyKfF4obb4Zj%2FtbB3PD462ED4m%2FyDohen2aaySBx9Q0uAStILT794tYenqPyVZffoKynmatz6Xtx1VWZRUkOfpjjihQ2Ff3XoXqkA%2BuAjm1Z3Sz9xOVGKfBoXpXehzlVbWUC8Us0kEVgLF5rdOTYZXLCaA61YcYF20OXJfFcQiAvCTkrShh00cBZ2oFwRBPaTbfvt5mUt9QRl0Q6eKzRXUSBcy3OL3aMO1QUltx%2FtmI67xwpIpkg5IrPLRUaqnkhwpEyielI1Zlu4Kt3T4CZLpfVWhXjHX4j8IhSc4hoVTEx4ZZoj1Aaz61k7GSnxhUd9Ly%2FYSL3KzcCZuCrmUp8h36NX0mDO6%2Bsb6XM3DQnmndBrKNn5f8zDT1sfXQYzu7etketD1bqzgTEhaSoJBU7YG83ipWSO%2BEEVC%2FMMqmqQGSbsr63cOR%2BJxZZ0X0%2F%2FJ5ieDnNukm%2FqFaXsH9OexcRhZMPep3R8%2F%2BkGyvmm3aTRNrZi37u81FtjkvXG%2Fc0qswjBwCfJQkuiXyTKGCbbD7cpVCuSD2sAWhBVxaj1rAxtqvJv7m3czk%2F%2FbxXLf3%2Bo8cfWBzZEvMP2dwaU5e%2BWa3t%2Bu7%2BxdcJnJtOusr8oa9vf521hbyAa9CTCExJK9BjqkAYA4pAKdP5xuZo5r2p4zDdzHTUF5kfnRW1xUgNkDgxCrwHkrDZ1NIKsv8APcuUb05bK7haQoOZn8ZrF6Yup1x6hjkvq6vStLBNgK%2BDHHhGl3wTsQbCFI9EakZYclIdRLrsB1Lv8FoyxjCJH6qlH%2BakvyzOY8OJkgb%2BynLxoa3WaoVGZskG0hcuMsMBzyFtGufSiklaqWeS%2FrvoOTQWCdEHqvRjP5&X-Amz-Signature=0da7b1132e9fa01f9c25f1f58f1e9906dfc50d0b31b87ed832448d5e05a88279&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MNAYOXO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQCxxewFhgR39JesNXrzzjMhXH06b%2BL1KsNXxMRiR4ObpQIhAJDmf84JKhEUyhTibExxMgWNkgMROH94CwdI2qCFridDKv8DCF0QABoMNjM3NDIzMTgzODA1Igy%2FcWQKV9kNzEnlBX0q3APel6PYuHcP3KiGVipIR6OLHV5Z4q%2BWi0qkbUoRl07dU2qPZ53Elxjk6ZwM7ahYop%2FVKA%2BDGZY87TxNHy0PU1ZtO1ND72q%2BTNxcQTw9qojs4veWDWJuOhXHPdVxKCmuxb2Ns51P00iYXLa1PbfNXOjzwZ%2F0t5%2FclIwP2A%2FMFqteuQrBovYC%2BoMHU%2FFaGuX0tOiLpiOw798j06odObQekrYdHwRH9QJnFsOBA%2BOebr%2BbI1viM8Ntyny0DNgKHzinsqi3Gvpun%2B6CqVP7BkKeprAQj%2FerbpY4aE9%2FeaE4oHVubqMFEBcYnJwnhoaSN9zg4Oyp2qtZCjWW7qFFLsL0%2FqvEVfRLKi5RVGM8JN7XqV6S2U8jYEgMEjRHja7ar3f1xjiy1yIRCBbiUfYafOgmZjFtNCAh9BuPb9Yk5dRS4YRK%2BDjNHTm1oS8PxjEmFuz0nN28sfeyOt%2Bil633Ahxky%2FK%2F6tLJk5KfL%2BjhQ7roFiP8qOzDhffZcqhvzUpiIeFBYtMoVrAWI8OkiyG1oYqXCMVfVjxbdS%2FMdoeeqp8Uwz7eolzMxhyQgtzGxI%2Fkcves66UMvXx%2Fo6Z2DnKPxUm5TFZATJZFO1pq%2FNacSg9tbyA%2FNKVN%2FKp751FtPTbCYzDDxJK9BjqkAYvMnOUYogoHFTpzTamVoyI6VJyBn4uXkkwDC22t62dXNWWhjJYkK3wgSUDy7nMoPYJwgaHzZRW9FiWwEJcuqidsKrCTXfK8k4Z7jLbwpF7J77EAv2XNtWwo7beqQzLZahFbECJumLJAWBOmzONZQtqusDmz6ZLWmQAlZ4xu5NXmgloiBRcsovB5ahb41GG2gwayCpxkUfTEJe%2BOFCryJ26ODlQf&X-Amz-Signature=8b3ae14953ceb77088a208f15b9ad2849fb92353e655be143e70c48815ec4610&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MNAYOXO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQCxxewFhgR39JesNXrzzjMhXH06b%2BL1KsNXxMRiR4ObpQIhAJDmf84JKhEUyhTibExxMgWNkgMROH94CwdI2qCFridDKv8DCF0QABoMNjM3NDIzMTgzODA1Igy%2FcWQKV9kNzEnlBX0q3APel6PYuHcP3KiGVipIR6OLHV5Z4q%2BWi0qkbUoRl07dU2qPZ53Elxjk6ZwM7ahYop%2FVKA%2BDGZY87TxNHy0PU1ZtO1ND72q%2BTNxcQTw9qojs4veWDWJuOhXHPdVxKCmuxb2Ns51P00iYXLa1PbfNXOjzwZ%2F0t5%2FclIwP2A%2FMFqteuQrBovYC%2BoMHU%2FFaGuX0tOiLpiOw798j06odObQekrYdHwRH9QJnFsOBA%2BOebr%2BbI1viM8Ntyny0DNgKHzinsqi3Gvpun%2B6CqVP7BkKeprAQj%2FerbpY4aE9%2FeaE4oHVubqMFEBcYnJwnhoaSN9zg4Oyp2qtZCjWW7qFFLsL0%2FqvEVfRLKi5RVGM8JN7XqV6S2U8jYEgMEjRHja7ar3f1xjiy1yIRCBbiUfYafOgmZjFtNCAh9BuPb9Yk5dRS4YRK%2BDjNHTm1oS8PxjEmFuz0nN28sfeyOt%2Bil633Ahxky%2FK%2F6tLJk5KfL%2BjhQ7roFiP8qOzDhffZcqhvzUpiIeFBYtMoVrAWI8OkiyG1oYqXCMVfVjxbdS%2FMdoeeqp8Uwz7eolzMxhyQgtzGxI%2Fkcves66UMvXx%2Fo6Z2DnKPxUm5TFZATJZFO1pq%2FNacSg9tbyA%2FNKVN%2FKp751FtPTbCYzDDxJK9BjqkAYvMnOUYogoHFTpzTamVoyI6VJyBn4uXkkwDC22t62dXNWWhjJYkK3wgSUDy7nMoPYJwgaHzZRW9FiWwEJcuqidsKrCTXfK8k4Z7jLbwpF7J77EAv2XNtWwo7beqQzLZahFbECJumLJAWBOmzONZQtqusDmz6ZLWmQAlZ4xu5NXmgloiBRcsovB5ahb41GG2gwayCpxkUfTEJe%2BOFCryJ26ODlQf&X-Amz-Signature=380eb2fcb14bf2363bf13846458fbdf5475ee6cd039de4a05d804a4f12dc1419&X-Amz-SignedHeaders=host&x-id=GetObject)
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