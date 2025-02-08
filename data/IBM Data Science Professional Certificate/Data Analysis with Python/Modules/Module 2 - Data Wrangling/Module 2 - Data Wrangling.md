

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWJKGCQ3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDB2D4fsR6RN8iVgGbZvJejRcjaCChGZNGQF5y8UewLoAIhALxcZsSDSryTcCBCsXMbyGqS2QGFi6s8vrwKAjGR%2F3%2BDKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzFf%2Bm4t9YJmOLZUWUq3ANVASLBxWQTkTx6xgoHcDXuo9sB9%2BWsmboDqFRkc2kRd0f%2BPYRLH5mYCSnM4%2BdikjQVN%2FGN%2FFfx5Q1Ro8dU09KsbIAPWF3piUnZW86n5nFra2wPasr3WSwiuuzI7EOUXz9PWuZrFd0swIMmZfJQ%2FJBw7Rc%2FMhEcU3F5BQ3bGayRyJoVFRYSz%2FbXe4fokYQGJGF2W53EWRq70l66PMIMx55SQGQgWu5HbrrM6jZW6OdXXCDAAEf0sYHGtt4wyH9vdli8B57ppEdH99tOwL85%2FOM6c093lgsNv8I1OyXare9q2HVjqHpGc%2BVPqPMp4j8lDwHCfscEpvG13%2BnaVnMgb5Jp0o%2FPqMIKcgHnaVNv%2BKTwyfEc9PU1OHtzLVkvBKIt1UIlWCrwGSK2lKGwG9e4y8sJkCqDReVZ3ZkQGu34EMkK3vWvtCq0ze2HRuRZ1Ql5MXXuTo%2FHv1vPfU2rw%2FYK6p2wo5j0r0fWLYWr%2FB8tOzXq2skqrGoPmozHgGd3pyEvaS5toUmNh40ZBFdhWRFyjGbS%2B2I2DjOvJeQBopB6rKtIk1au1blKegFJ9D7cCowbkr8tSlIUJ4H3mzAo%2BHYGgmH%2FsQnqT8LqkZ5Q%2BmK1GCqsA6QGsaD6xX%2BG0B1pXzCAlpu9BjqkATKJH2x3%2Fac%2B4P8HCAB%2BDKkgWAiaEKjf2kHzV7mqVrnnFk3uiZwIGip2Zv%2FknSOh9LnS0GUEhveIdLkMNWpTtsWWm3xddcyfIOMg%2F6GCvrLTYGD2Lb%2F%2Fd5T9y90YUIV1%2FtuMY0HgcDN74%2B5PeC4OQonz9WbOk2aEfJjGm%2BmUNijeK62z0oN53TIRXl9uj3LvEbrSY91JgHM8lZ52xq7gPMQnz8Dg&X-Amz-Signature=c9871b0b4ada4bb780e670205fbdd6f09e39ee35fbdadde2aad40adb4001701c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FDYKFHQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIG5zwlAU30iBszye7RLGyZfE5TVJRQR348YqHTxdKDWXAiBX39ooEN6U7wIhJ4NyEt2ZxtW1PLlHypj7NV81fPGsHyqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmkarI90bPHdg7VGwKtwDQRTfo9mVqTCF5FYDIrb6QUZkxt347%2BxeTBxyeSXAa8yQKL0D7JdhYFkWDmQEC8tbE6NFDF4AI2GPF11SKVU940hZxwA8nwUSzeY%2BtL5xWi3TCFiadVZI5XuYCYumJ1HODFOT5qj4ynfmsY1GGINSnwUdcvbNjh1KMh0d822L%2F9SUu7pbaVBB2SzEpxX9sv185HAGPisS95HFqgzW%2BWC1S2zFUw4%2B2IfPNJlCP88TOgnK5mfWwR7i7ihOm2NWsOvrqKOXwYRhThljRAG3nv4rKqfN153cN9QKHJbBqMn37HpHMnOOddnXM4n5SwfdYUQhiQxdtAbt0lOpFMsWbhf%2BVtm%2FJnmZ9X%2BSBQv6FyZDOq49XhxJYSC0afr%2FoL2ThZEhQc1Yn7iJWfK8Ejm5VW8peAPO5ahhJH6Ddh5GQTPg8jbyeJgvoxZ57Y1xcPX4z7nIqfUeEFGbssuXmtjBLMCYTrrp5mOghkjfUGd8UTqMnYGy8N7aoYv5vFK8zb4hSVqrBW7Mw0o%2FJSnr3u1NjDUfxmOnkLfJkegwDkfYNKjuo07tfm9UTVZYhj6Nem0wrnOaYw5TKIcn6yjkE3iHRF4XoadrXENIaZS4MlPNMSP%2FVkzX9MHG64PfcoDbnzMwupabvQY6pgGZY7pJp2w5U%2B77jj41VuOCvw2Z6LqffKTsXdVFrkc7eO7%2Fv7bugFBtcKoNciqPqtwL3Bn2Ax1D9%2FqiZr8qsYsEEhoxS6RzgYRqwi6cSsFNYEI2tOip0DsBna34HWOmO6J9cOjSSsadSjDUKtSSgQn2%2Bm%2F8ivOZkynl%2BXERXoY35x%2BlhfMYZKP%2BEHpWrtSPEvpKqo%2FY73uxqD1I2wk6s9rJVvYaUABl&X-Amz-Signature=15e9fdb4a58c337d79304739dc64ed4523c3b85f012ab4ac58d718e652b63e12&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6WDBM53%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDmU071ZKghww1DOkj1oCcP1NfFpsfwV8NRyNO26%2FF8HwIhAP7o%2F0zIDYKshkwAa6U9Q35KF2A46BNNRY%2BX3sz2dpCHKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfGdWkYTeCleyD2H0q3ANoSTUCs3dgoqgBm0F6roNPawLzOrQpuYAjrHlLln1%2F7XnMLEYBLNrjLEKwM0ZyRGLgQnjdmh33aC8sHLxolzMRsTGgYxOgcZWtXDutyj6gjXcCK0VPl7ZQdzugQIrH0QaXejCM02cX94ao2S8GeOvIEwO8lZ9qTcKfhg524pv1JJt4BDg8TXuYCdhv9Ffh37XlEYPsiAYSlUv2dZyH3y0nqEK%2BVlEw%2FQY8CNTfMpQtumrrJgXcMRS4D2BhbFU22MayrS9yjisXO4fVcaPz55PH56x6Mg%2BeaQv%2F%2FxB9YBEb8qYVLBBXdI1p1rFDosFh2MLgIYSRtCbFm0hr6Qs35KAQYFP6Cjp0DGCv%2FxY9dTOMLVEBswZvhUUiLN%2FEqrS%2BX%2BxsiSWpbTOlh%2FbOhzliXLb5AoXDIQfCNZ%2Fhl%2Fmd582xf3%2Fu9AFFS3yX4otF58nLaSWGkmY0jgqje8b%2BiP7ABgjVCAuuHdKOPeDNR8Wa8Ks4uJIOFT0ehO%2FgvQEAEOiY9ZwDtFN9FfxaIid4ut%2BEbRora1Bnhmb6jSBYbrK49iWqzhqxdM6SUhCyr9FOrAcDlbClwvNTqTTCMVT%2BMxMcwu1LGNkXy6%2BMUHC66Pl5nYBf0tITbtqPNp0nJHxQrzC6lpu9BjqkAfk8TfCMi6vnhFB02o8Z5HJlcFwv%2FK6v7JXu44W5dYzXylerLuF0xWBcV%2FKKi4PCY0cPaNBrTvn2DiqXRnS4to4EnM%2BaLnBuLCKLvR6E8vlp579T85NNl8k6DAJfoLv5lDO%2FJxwE%2FywcMr%2BS%2BnNTpyPNGD0Wk5gqZ%2FkOkOdqb80wXhAXmZZbg4gk04M4i0s1DQmfVhMTxqWi0GiW9i9SBMYQG0PD&X-Amz-Signature=46c4eddd53334945460332b1a28fe8c66516559733865beaa7a233583d05849b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q54UFV57%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDu48lRznFqM9NxihWIvUajtrmrHwI7yJsaY1RCwWwiXgIhAI8kgmLKa3CR8iJl4tCuYhvlw5EbOtzmYiz05DfHJ1v8KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhVoN4793x479b%2BuUq3ANPaeVqi82JZxBkzfGUt3Nc6kWKVtIR4U8yd5ck3aFesIGVl3djhiJTtw%2BVy7sUyrIjfCYrIOcTZt8CarqTYRVoccvhQTFq3XNimHwmcJ%2BP4ew3EpxjDj%2BFZ9gANwxwxASpdP0pir3O9Edolst%2FFJirAVH%2Fd6xjPYrjpswtMnE%2FXSN%2Fc5AkcLF%2BWpWdRe2J7zpUgGKqxz1SSmZd9LIC62W8o78vHYb56Rt55nzeVEKhGCdxOtlcvBpXxjFZtkWApZjej01NzO%2B2W11g7DOtRwqeg2Es%2FBIx3Z83jM%2BtJOh4%2FuIYcvlVbsDF5T6RqlLI1Ag1j4bsBkxALrfLrJsFUv%2FbIF%2FaeEhzXj9ZRbvd0XkARvDiumuKEJ0eD5GvONgHr77R%2BpsouoBpBfPA0g%2Fo0ZIEVvjKJsHSLpAuWKGKyhOTHcG0FbDaNm0G1ECcKDSS0R9vVjrpUtlGEajobRRZk2RRDJvgGyFkUUIPAAJUASJTbDages2HMK1dl%2F%2FGhzB%2BzKQm%2BCl%2F8HoUAXn1IY4FN2236R3AxVARFe13zaDrqBpT4qHcBR%2Fhw2JFpprjGHyHpEJt8Qxio7Xo7cGU3VQFmP5Rk94dYssWH4nmd23AzLA%2Fi24IebVpjmbldwVPaTCilpu9BjqkAWUOQy4S%2BRz02uuq4YFIzwsPoYWSjRplJsjPt1O7epqtN6rcCWpEMdhiI6pGOAXqp5qQ3FZFTpxTMLVvv%2Fa7yXTXMTSik%2Bk%2FYbgnABsNhiuIGXdLnVSazoSkHlLb%2FVLIKYP56JuBNy2LeZ1ZWND2jZkuDAmo92cXORoV6w%2FwspBxAa%2FSeYtMWpBRcKFAHcr6zNTBRjJbr5gKwdndcp62bD6qeAV%2F&X-Amz-Signature=f1617fe4e1b2f046d375308c4f7073163fd3f45acdc24a1e52e12f4e0c00883e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FMOWT2S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIF2lkNgAu1vD0RIw3YsNnnvj%2F9tY%2Fv%2B8cD9m9k6xQa5qAiBkNISA%2BKCROyagKY%2Fuin4H8rnZJEAUndgyAzTz%2BGkSrCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeG4abixJDgxzd4S2KtwDx19RI4wfDfIIdy9kfn532XESZ4ceNJ3uuRe1LbNemd%2FTK6GJmAFZHRF7Y5Z6%2BdWr3VHS%2BgtH9G3PmqA27PPzzB80eDJT1oQfZgLb61%2BlQR3d%2FPaQGFWHuMLFZuZp8mVdpVc2N8YsLEDlhiaaKGIYotP3sHACI3p%2Fq9nL8fpwyPSdMCitMKTDNH0AtvuJaAR8%2B8X3Qe2OmEfRfobBv0Zn%2BEwTxfp5uTzdonNyPSMkDPq7Ap8zIAkTN%2Fgvrje9TXbU9KEQ6%2BrmXPxIU%2B4av1RzY7jRH4RihInP9FOjX6dqpwc1Tr7FxIrxm3I7j9VLJFtqlhkziX4oFaHlyQpLaa82xJ4V4utDqa%2Bp3VQvHjyrAbRTEfSGn1at4cDhFvtGXwZg5UtfSiAl%2Byl24y8nS7U59rEPIY8QUESX3%2BvGZKnwFj1z3idRsmmO7S7qkmlZqH0FHXlCTbI9kQRS7pFKXDnsVY2txYlNKZDMbfkr20eSgPUIp3VeIWGJl3zM4flGIM4t9mrWpiCVmNkteDyyC8NgZovVVIy5grQCSy9cb8%2FTeaJwpvPHHb9dBgRoJ52YH4sRbKtGf04zZcyzpIfco2wGlq2ixxEnAKh%2FTOGgiVnGqkviturMFmiVmQho1Lowq5abvQY6pgFy6sxCXXZH%2BHVqXqzKhcD2wsNT1%2BmIcrX0tA40mah5MmCCwulJcnZTeccyP1baOfz4ImvaAjmlUHFypo4wNrmBrQQrGDeYOeNN3yFUYzjbCSGUmiVToscXmo70EfYRzpuZyNzPZ8kwI%2FMnOER6D3tF2DpJjiF34WbjXAQc%2Fg99%2FAN%2B0CN6yhf7H3qUEfzOMKb%2BVSDw0HVLZTyq5DAnH0vwo7%2Bla%2F%2BB&X-Amz-Signature=c8af5a254ed739e9a4e6c2a5a51511bb22b77a07d9c2e08a397897c32279dd56&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7G3WNKI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCICS6CbkDrKXERjwubEdm51Sv6P4Xd%2BomSjwwL2aU2GUBAiEAth7aWfqV07hlred5qo1AW247sr3DuEgSb76XvxJBS%2FsqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEYtYXK3PTBicgJiyircAxpTp2qksGe89IT8FGf3nXJuzG29rs4BFZfOrz6M6DmYnLuRDQ3qJiPXa7GDd0PbfynEf%2BERTXESiPqqqhNAnoTwSEwBypx9DgRnJF2qeyYrwRV0JedDwlstpfVMhIITBDQRzPOs5kWVGZU09%2BuSnVGOmlD%2B9GpTkeOudWfIWFLNINCquCrvxzqf9uRjwEXbeunhwSsMjuNXS1kq%2Fhf3Vpp6DvMxFcn2o6W3hj10HGp3cgQ7xo2rNJiDqPgAQSgGQhOLa%2BiqxSmv%2FiB%2FPYUk%2BOGzpRoIE1493q1pwUMl%2FqE8oQrBJG%2FnEE2WxZpR0PVqncGLNKDcsnAeAix2wW8Nd5qSKY%2BJR7nTNe3sFVXeOh4aajz19LyvO980pzVwu8cxVfxWKj083pSXpBMH9hzTC5lXQG7PPYCSEGlspgzcP6Q1td5gUONksE5Wx6ng0FDMCYLvdHxRGmFsk2Q2%2B9EQrgCAONQI9yvcsjG5GGBacKnH%2BpX%2B578L%2BPN56mCnWlsWeD1%2BF%2FT3eA6jSLDi6jYSEEdwPZsqZXLBI7bG%2Fto5i7ffyiN%2FCA6HgILgTpJLTb1LijValqATQnj6A1hsVkIYayoPyafFht8l3hLYGfyUkvuRNIrIXsqmQA4NB5rTMKqWm70GOqUBHqE5U4V%2B7CI%2FqDLrQlosdOrOKgI5vkFCaatL%2BvDhJnKbcIwgkx1hzVk3BfFtAnNTs6AInXV%2BTrEa1KwBPJ3jtO7qdRDrI30aEZqoVq6QfZmAjDtJVQnTZRmhow%2FbxmgA7VY7XDfucbDLJ8PphJFtioGnPVph7gnyZrYkGefY6UvODiuAuL7cT8SFTPA3GvsP%2FcsENyYXmPFS6MGeq74XOcPgqrFj&X-Amz-Signature=7879c47b6595e737423b17117065cc0c223a5db817bea89a81a0454942bbf8f6&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673GHESGU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIGv9%2FoKQDF6AeJ3ng4Nt1lgEMgnYGKBvACSk84lMOy2xAiEAsOaMEog1UaBrj1W8FJWrpUFiEE0yJ0u6zaZUEoQt42YqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOHPQNzijmjaE1hioircA%2F39PRLC6qQTyFXEn2jrlaQd56MVsCyGg1zbLRy0PA7wQ7xF1Q8qugg7ZgiRN%2FOxLCvRHH6U%2BB7sMdCj6Ig%2B5baHfDP%2FyX7vMFMRdgM%2FrdZKA28%2FZppUssRhk%2BIb1pm5iySs1vK%2BQtGGVCJjI12UjbR06I33XK3uAAWoObJuaTB9xXDES8ZlyXeOjJzohWXQ3Q3uXTcIzJYkML3C0IHmrMp1fkQU%2FkE%2Bq%2B1OLoenGXWOwkZnBVNbepUxvR%2FzqLJsAkyk9UOuBkEYY9bWbqdi0Qi7hPDAl1i3Y7siAumKW%2FCkQV2XNgO1XqggUWiUA2dCsshynnKwR5Tgelxj3zmQLjTrGiqqU1swyW0Bbhn2cDlF2dp5nyR5DotCn2VG0ULcL3MQCf1ZDRCQ1H97DDgBbOqfg6wvTAHYnSrvV%2F%2FNMFfSHZk0l9fW7ewlniAycC6wIi3FdCEL709jf93vzNt0DUmmh%2Fxq401c1lZfeyDXDwEU7a1bsi0l0F3z%2Bfx3pIt0c7mUCOUc%2F4nG8CyWczufurtfjs87ieOBGmKqe7qUHmga4%2FTGxpb7SuG7mBu8lxBPQ%2BiZkK%2FPMpErULFXXUOeqKM7xpjDLG8c7mqVE6zfQzO0pDt20i7iJW6wE2%2FgMI2Wm70GOqUBA1OS5KzYqaeHzX5e9CStB9lPH2bllgBKWaHH094kBBQx66kg6hDTyIxYMVIlH%2BbgLqaOras4cIyjD6LP5ptClA0dr%2F%2FBj%2F6CREjh9kpvOGF7atWnRttXM8X2VzVwLVaYc3peeUD6fMnrqIVTCPdb%2FTt2FJ%2BSWHqP2oYl5b8KIET%2F%2BBajYZVSX0bBTdZG9nORPOArMbM46ZtLMIwE%2Fkw2V8ZMAPf%2F&X-Amz-Signature=dfd4b7f036d707a2898c5c3345192c7f504b381445a5dfd5d8ca5ffd05b73009&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWBVVAQO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIDQcERLzV%2B8ovqXgJltRui9YMCu6KWS0nJbUQwbL7kSRAiBHlu6fTCRGLD2UHEEYbjda3elcHMxpoAJQBP7OAfLlZyqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNeC%2FSBeYtE6EMTH3KtwDVzgB4FpgEZyViV2I6f1vvm%2BCD8P8ZKIzU2u%2BhsEtPDvdvkxUyNOOvkz%2FYwhWRdf8otjkCnMjWLgPsmPVPWQxVwer2vlj9HvcDxqckMK66eKBLn1vfVmu7t%2FUKdUh0g9PciAaMo3IPzakRQEQOc3iiY2vSVRRmcwzsPLkkNaFCfgHc2mqiD%2Bku3CIlq8I%2BhI69bB1JxhkvI9wUoIg1EYreI4Utz9xIWa3ZXWHyEVYP2wf6Yv%2Bv7QNpz4UNP3EmBDkbrKKsiPd817hkPcEbLyOzvTPgSVb9wgbaR4YBxpI4E68o18uqRo12%2FKf6I%2B2l2F62ldAi7XqrXVqaslcqxks1WKvkiUIVw56yuurnw7RoJUrWE1uqCad3QOcbZ5%2Fc1ZR6T9VwDmO9ViXQlXaGF4d6bklIaebBPODUWw11JS9dEj%2BjoBQrm1zTvd%2FJ30gI9eyqpyYgQROUp9F9UY4gTJyCPsU6ZR7Tx4GxvT%2BnvQWmjM1N60w65oxZTtiApdgkhd82RFiPupEpCSEM%2FmfeL9QF6Vn9MZQhuNnxwn58YGIe9ECwmiSjqliVMhQUlJrsG5PpZmtbqXtfyQ4S8YDoIRn0Ohu8MVJZiGnk716NSSkYnb6MrBxtIGBV%2BIU%2B%2FIw6pWbvQY6pgEqdYwUPtaZExLQ3Blmzw28%2BIJeLLOfqvxzxb0dcmagfEAF%2Bek9%2Faghw7iWDLdeGPxKGFCm5J4hlU2JipxANnJu32huOw%2BmW4x94gUsrd0BYNjtyumUTcqn1%2F4wPqE7pIqcmOj6doCHifLEAwU%2FJyRAh6b4k2JephjE8Ik3CLo0O75MCoS5Hi0%2B0%2FEhBZ8Kf7ftB36cDKQ7tjUgzaixHaTDChEdAEXA&X-Amz-Signature=67cf1b3fed5e0213098edf134ea4d1c016bcf70faa980498f1c5b8cfbab71807&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FMOWT2S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIF2lkNgAu1vD0RIw3YsNnnvj%2F9tY%2Fv%2B8cD9m9k6xQa5qAiBkNISA%2BKCROyagKY%2Fuin4H8rnZJEAUndgyAzTz%2BGkSrCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeG4abixJDgxzd4S2KtwDx19RI4wfDfIIdy9kfn532XESZ4ceNJ3uuRe1LbNemd%2FTK6GJmAFZHRF7Y5Z6%2BdWr3VHS%2BgtH9G3PmqA27PPzzB80eDJT1oQfZgLb61%2BlQR3d%2FPaQGFWHuMLFZuZp8mVdpVc2N8YsLEDlhiaaKGIYotP3sHACI3p%2Fq9nL8fpwyPSdMCitMKTDNH0AtvuJaAR8%2B8X3Qe2OmEfRfobBv0Zn%2BEwTxfp5uTzdonNyPSMkDPq7Ap8zIAkTN%2Fgvrje9TXbU9KEQ6%2BrmXPxIU%2B4av1RzY7jRH4RihInP9FOjX6dqpwc1Tr7FxIrxm3I7j9VLJFtqlhkziX4oFaHlyQpLaa82xJ4V4utDqa%2Bp3VQvHjyrAbRTEfSGn1at4cDhFvtGXwZg5UtfSiAl%2Byl24y8nS7U59rEPIY8QUESX3%2BvGZKnwFj1z3idRsmmO7S7qkmlZqH0FHXlCTbI9kQRS7pFKXDnsVY2txYlNKZDMbfkr20eSgPUIp3VeIWGJl3zM4flGIM4t9mrWpiCVmNkteDyyC8NgZovVVIy5grQCSy9cb8%2FTeaJwpvPHHb9dBgRoJ52YH4sRbKtGf04zZcyzpIfco2wGlq2ixxEnAKh%2FTOGgiVnGqkviturMFmiVmQho1Lowq5abvQY6pgFy6sxCXXZH%2BHVqXqzKhcD2wsNT1%2BmIcrX0tA40mah5MmCCwulJcnZTeccyP1baOfz4ImvaAjmlUHFypo4wNrmBrQQrGDeYOeNN3yFUYzjbCSGUmiVToscXmo70EfYRzpuZyNzPZ8kwI%2FMnOER6D3tF2DpJjiF34WbjXAQc%2Fg99%2FAN%2B0CN6yhf7H3qUEfzOMKb%2BVSDw0HVLZTyq5DAnH0vwo7%2Bla%2F%2BB&X-Amz-Signature=f6af2d2199ed17b6775ab3e6725e8979a57a6a927cb7e09328737d5995f6a804&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WR4PKU34%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQDR%2FFhq0V2MVGDqTUhIfNKC4cpu8%2FziW5yUKeB6te9uEgIgb0ZZB3Xths1uCyJtVovaJ5s3ldPNSVGyo2bwimn4UyYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL50GzlcjCAjWE%2FfGyrcA2F0qJZvHekXFa6P4e7wH8EmeqUvchBN2HEHdLC5F680VNwdeWauM3zaIwmFEXbRNlIFd9rxiPkQ2QkCxI9D4s%2BZBLpqXq%2BLk%2FcboOuurk46cWgTQJm3Bcn9KOtBpo2Gw1KIjTSQK%2FqeAI9924MY25YiS2oBQEE80tlJdi0Ro5odpi9nO4ArGyY0DkW8iQzrcEiE%2B0BZxHsXvaXwLBwNP%2BghTn0vU9b1HyitYwS0LESDHaOelLNizYLZOQf4P%2BMPy0Dm%2FJzHO10jnqOpGVSXjw5b2Oghs8OZpaRx%2Bi7YFkg3iqn3jYNYvpN4kOPE%2FMzlNdN681QfgASckIUqTuFRTWxrS9glqCXfMCTISRVCf0BezM9wVqUkbL5jDHErWyByTlKZ5mkxWeomtdfnuvtyMaNp10JxRuOBT8phkLnTs%2FHJxI88lB7UyUTYbzsawb%2BmI6XoxAcuO%2FxXiK4LMkJdFAJ2f253MhvLF%2BFdYf4cuelvkiV8YJLsBfO0rb47LCNiV053%2Fri0Gnw8YqKF3QbEWXXukd4Ztfkm5M88YwwaGK1ZTEV4eoGLUKQ7I0YzGiCl2DbwWyIlW%2BOm5jXzvZBFNaeHhWaEsb6GrzIZsjWoYDvTv4JS1Cevh1mbrc5wMKKWm70GOqUB6WFudA6OIbzleNUdbKzJExUfKsLkCSVv8yMw2ULHTB4vXKYLI1M4CZgf9iUg4RWOXOsvypVOxrYT2kgPzgdhrNnOmoMm%2BMaV%2BS9LBlWBzQBU0o9i1lXbeFuWNKDjiUKE9K6rR0Cdp4BuWO0mSXGena2YTu%2BKMfj2DCWF5AXNshDjyWSyZu1TWz%2Bh5LWbZBDWKG8mzbw5rLfzriZB4qX9wzd5%2FbLY&X-Amz-Signature=61b7a0814b343a7223e46d494d5c4d059073ce93d5f551675f2f5a11412f1cb0&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WR4PKU34%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQDR%2FFhq0V2MVGDqTUhIfNKC4cpu8%2FziW5yUKeB6te9uEgIgb0ZZB3Xths1uCyJtVovaJ5s3ldPNSVGyo2bwimn4UyYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL50GzlcjCAjWE%2FfGyrcA2F0qJZvHekXFa6P4e7wH8EmeqUvchBN2HEHdLC5F680VNwdeWauM3zaIwmFEXbRNlIFd9rxiPkQ2QkCxI9D4s%2BZBLpqXq%2BLk%2FcboOuurk46cWgTQJm3Bcn9KOtBpo2Gw1KIjTSQK%2FqeAI9924MY25YiS2oBQEE80tlJdi0Ro5odpi9nO4ArGyY0DkW8iQzrcEiE%2B0BZxHsXvaXwLBwNP%2BghTn0vU9b1HyitYwS0LESDHaOelLNizYLZOQf4P%2BMPy0Dm%2FJzHO10jnqOpGVSXjw5b2Oghs8OZpaRx%2Bi7YFkg3iqn3jYNYvpN4kOPE%2FMzlNdN681QfgASckIUqTuFRTWxrS9glqCXfMCTISRVCf0BezM9wVqUkbL5jDHErWyByTlKZ5mkxWeomtdfnuvtyMaNp10JxRuOBT8phkLnTs%2FHJxI88lB7UyUTYbzsawb%2BmI6XoxAcuO%2FxXiK4LMkJdFAJ2f253MhvLF%2BFdYf4cuelvkiV8YJLsBfO0rb47LCNiV053%2Fri0Gnw8YqKF3QbEWXXukd4Ztfkm5M88YwwaGK1ZTEV4eoGLUKQ7I0YzGiCl2DbwWyIlW%2BOm5jXzvZBFNaeHhWaEsb6GrzIZsjWoYDvTv4JS1Cevh1mbrc5wMKKWm70GOqUB6WFudA6OIbzleNUdbKzJExUfKsLkCSVv8yMw2ULHTB4vXKYLI1M4CZgf9iUg4RWOXOsvypVOxrYT2kgPzgdhrNnOmoMm%2BMaV%2BS9LBlWBzQBU0o9i1lXbeFuWNKDjiUKE9K6rR0Cdp4BuWO0mSXGena2YTu%2BKMfj2DCWF5AXNshDjyWSyZu1TWz%2Bh5LWbZBDWKG8mzbw5rLfzriZB4qX9wzd5%2FbLY&X-Amz-Signature=ea87bd5ff9f46d6b02a9eeeb0e6ee1de99658c319055e3cc696098eed3bfa3ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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