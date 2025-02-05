

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DAKNWZ6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIDqL6VuC9SFknPayUCkda9F77EtTWD1ZIMIa9PWebrDcAiEAqUqtoM37IBo%2FsUtXlWAU%2FrmExErMosj4eCJvYGpvjRAq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDD3L2rPtCLxuTszoMircA0VOxBIEKWruiri6jhCdZh8u5iZfJg2Wjbf9fUY4yxRlTKJK02vhmUNk4luuxgXvbMMQvFSMO1GbSgPj9weMTcXXTKkmRUkYiVUhSPHj9z%2FgYiS0ml%2FGghYjToGi3LMiQz99u4H0qBxFkHodJrKog2oPzCjrsSjBFaw7NfPEe2t68KfuHm5CrIdK4JTuDN6S6StW6vJ5uCtRmhnEB%2B1QaOK4lBAxbBkAsvYMCbVYcQAWfbsSEZNjky1jROi1%2Bt%2FmXHvrj3pq8WY%2Faj8yCYlPXTQEi%2BGFbf%2FEEUSUeu8Euvj46IftotN%2FWCff1eyaYGRkWlmpot84SRN%2FI5zAHiUGU6dxuNH9lwgu%2Bl7HVLOlrl5%2BbswZef2B82nyEojUZlVYwOy5BlTCVi%2F8GGlK%2F%2FbFS6RTVw%2Fpy1RaD63DJHAwNh864kcp%2Ba%2FiBumNLSK%2BWQIgOsejvrSA0gHUaN%2BrsoePtYBSBTqpQw58Xb4GNiwQmRUGlJd5qKOePLz%2BrHWFAyzsm3Gif29NipabXcY20aJkcOuO3L0PfG8r9cWtCDalTzRh3ai9JXrcv0xEXlbXgO1sSp2bhYBLlyGY%2BCLIl%2BqdbHNBs5fS7HxaGxKqCDaVxOdJ3XedyIMXcES8Oy8OMK%2Bdjr0GOqUB0wJ2qQOxxCGsjii3StSJ2tDOWAINhrtBI%2BcVqv%2BSZimZ7sLZrxWqg5vCQbnR40AkKZRDfwTAtGhN2xlvHH6B7EOwFJm08jSUIKBm6B0j2kBF6tI4qHhaNaBBmPngVZogadWFWq6xZS2oWxldU5tXskk4%2BpJIYg6BWvJ1TBSJRDhEGDQXDDve8FmIcxSwezsg6eQ8IMEAGkhhlbwyiHKdPO2gh%2FJE&X-Amz-Signature=0fb3e1955d188699404025e4ebf1b606052bb51a0d0125ae89b9c193a75f2a68&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNEA6TL5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIBbdT1A%2FdAtWGhbT0N%2BGzFTnmaW5hhJJzWfsi0mWmAkWAiBvnlnkynh1SXJxDPAOyoO0JjFfhIgfmxDojIzL%2F4BKTyr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMZqL3Dx48a%2FVyYzHAKtwDDUxf0uCQpu6cdJ7RKvRceXPex0doUhWjRYm7DsVvx5zkVS6MC3DYPs%2B3wteXpf%2FWQwAigSD954Fz2c2ZvQblyZNfezpNEijeLaaeR3Yc3McQjNGxNJ7wDcZzOFJ4UiPpAOMUclqNBdCuQ58QvtzJfbkliGE%2FW%2BHfOcsx%2FbkTsnkNW8cit1p0q5Cx6mit8HxOZB%2F0T9a4XTmgB5RkROT5CPoN06Etu6xOIT3ZnPplGMDGh54hmqGhFCxi%2FKoBo%2BVONQ8YaPFdRB8aAlBXgBa1slnwkuSvBVxEWo8ELqD9y60ONYe17oAKXrcZxoHwNl%2BpftrOkmMY76L%2BgFOLKx6VAEhiKdKrg7mAIJ6iAPur0jr7MSx53h%2BPbs37il2ZLMpt6a2Jz5zgIqY7lRmOFrGidQ9Jdi%2F2ohagC0lQSGyGyD6haLBTiSYOtkbpqqQx42%2BJscd%2BOdB46hTWPWX5wfEK6LWR59SQDFOkYSShGteI4vH%2FaUN6MEplyQ9xY2e5UaI0anR5ScsKMC5u4NIQkzaMwTXK7us7rOfwupzsWqj60djJAwwlk47%2BRpw1d9MXoeibZRtJVFoOvF3ZbQkSpTVWZBFC%2F8WV%2FTocpVxXm2xzGt6YZZLzDZQPuSJdmpIwp52OvQY6pgGZa7vz1IFTGRUGC3lwCsEzjFLvY%2FH77w%2BjCTdr1DRQJFeAocMHySBog%2FQ1dkbfni1Ei7BAxE0RRca5T8DrndkodUH8H%2Fi5t0HxDqcvO1IYAByRV00KRqizo6Rgp7is1kZVUTiRXOr5rXgCNF2QER0VaVGNT5BnbFwHXl42FzyMJH4Tu2%2B%2BSuA6FacdFiswaf3jsOVPuUfb62B3J35tj46cROc53Aib&X-Amz-Signature=d6ff7b36f317366d0328c6dafd647aa88d7972754ed392b496a4fab4ce561d76&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625KJPGVC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIAkJjpIILdZAWLAJf5S1Exp72iV9lQ29x3%2BIZSDkjQtdAiAzlMKJg0WO1Z8KqaZFfZ9kD7HBGWKFVtW3NGJe8AZrUSr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMMzMD9iPINSUkYcyfKtwDdeQidIel1UJQnqRpNEAyfcxqjP%2BzTEip4g656XTzoPNz4Qx5yBVLD0dcxcJg9UtFEyGEQwroH4CeNOWn7J8%2F1YM8BvUIZLPFlmN3r3WSI4knLzekiloGB0NrCB0IVtdm8P%2Fj4a0%2BVafoOU5B49dPEFIZgN227mHNlahtoJNhWRCCMl%2FswlDWElE7%2FvX%2F%2BsBVdlzPqq30ZgxJ59b2B2M%2FFPu0aiLoVf7DbrWkKMw1TUl0zLsVAfF1s%2BfD%2BAIlyPGz3UNMMpamS4qn%2FlHou3qzVXnjBNZtdKXiP7FHAI8Yse21WNEzSIZhSjJ7Ioh6CB2WJFI91kG3nAYUOuaHhTlTGDdb7ZgOjBnQGacGfTw%2BXCbhkjeFk1so4WowOpTugGtzgY2oN7Y%2BBpXYiScmawov6UvUvU4ZQcWDhrBFe%2Fqv%2B5M3TVAGpB91bG598F%2BWoSIZgMiITAD9OsfPvxibrQBn4gEzFfE5RuG6GvwYOc%2BmFbY1kXrBLXbvsoU7XjLLEsAsB0bFRNHvaQnlhtVIAgwOv0kDEz6trDRqaPhSr9rZ5S07vbSXwaWA9dxP3C6ag6Xg4wonD%2BM1gLykAfBWyTyxWBj%2FGzGW2weijD%2BuUR514IHvqMmFRjkJoQGOOYQwwZ2OvQY6pgGrmf7kCgr98vsdQ8NCEXo7NSLvH53g0Y6h%2F6CmVe5OT%2BwCDUP9XK3j9Jt9d7fzD0mc01rWypF%2B8R6yJZL%2B%2FiS7eNqImCYVMRdAncku6%2Fax2PmRx5nah4ldR9YDfcCcnqzBCHQGPsHJS9PysP3aS1Uz22WPuXm6wnMhpkmqJhfGPWOgxvBKtdAY4aTefXtaG9Hl9DGJ5Bj91epyK1fhr0PB6vkDrJ7g&X-Amz-Signature=2414768bd601b902c91b516c2acb3810dc2b65e7beeef075a46f796a2957b1b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PB5YF6N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQCExMHdbFdh7uOv7l8xhdFY1kUj2grGm65QhgkYGbZ5IwIgCeQtP4a3Ag8wvR%2FWZaHhSaKu5Htim1BTqlg8EN8yuQIq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDBhTMBcQY6l8SBnmEircA%2FsgKkCWTQibhmC%2BCwWAjfYxqcz5TIo1sPo1%2FP7Ttak99WkbEMBmiJ2j%2BKZHtasgYe%2BQfAKwpKRsGy7Xfl4io9oIotaPNoIDYSzlYlXHNPXV051p2JFmhAnphXQazprM47CXQUvKLphFjKRjuc%2BU3Wxvho2iQ10BHn9X%2F%2BZLfCrgqltzw9pXwBMusGBOQlu4yPM4CwfEXEiyDUQOpPYyKjLo6uuavy7ROSdFIv%2B5o1zLacHjJ4n2K69bg0SX7TrR0J74%2Fid5R6QiippYjGgV2WjcKzFzgzx45lCf4rSzMV7kEz8iPTXhpKgQmRuNk1i29c6kzmK74BgRvFmigRgC4nBBxnzIbOz%2FcV2rEsJR3j2lric1Va1PA7yQN28L%2FZz7oLnqlr4%2FPybDRhOSSnGA8pRCXcuU%2FowZ1RhlFnTUbiBwFIv1vDON3%2BVSEb%2FKdBwLIEoJUqsJZdriVt07NszgjNVuBVovdS6xzg6KRR7B3lNnlIwDybbG5bprsk%2BbTTzC8Jr8NCV1dTHPg5iMGQzDc71YVf036L%2Bt8FH6i1T06hrJEOm0CkOkLdbgDf0wNYHU%2FbJOXn58Z%2BdwQS9%2Fqk3s%2FxUh4j%2BoJJO1WzxIrmiU2R4MRbTag%2B%2Ftp%2BHUF%2FZQMP%2Bdjr0GOqUBe1qjcl5rna4Bti6qx9v1SRnBPlHrA5IbL70zEtyKBShNsBgZ1n1vBE2ES9ok1FOOsFITVKGs8JoUeUq5jD2rSvLYZ%2BZl60zs0djbMhNkLzzf5bHd303sWRaofKozqYmytw1mSh2glVuhHSAUAaTIKw%2B3Vaug%2FZpmuY6V6k64Vhr5iPkSiE6MVNqYjkqI143yGEgdUFob%2Fs6kpm7ohO8ToQ29w%2FCX&X-Amz-Signature=a74e056cf5ffe51012c390b32168fc9335bcf66774755bc809d0a91ad8597091&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USM5IAIP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQCMMESLaK0LRmkqqWYAEyip%2BwW42fnNe38ImHVK2WULvwIgNdocLVaHeZs0LrX65YTmpDVnNTR0g5C9q7jlv8WU24gq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDAgytaRDtphBmDuaZircA8CF47NLBoYVpvybTUm1Z%2FpxAvQ1YEmFnJeOxy8MSz%2F4asu3jqzO0d8sFLqKmJSzYgOlf57PCCg%2BcuhiDHywCSKTB7PTxAQgSFWCHwb4DZRDfh2GJHmcUfIRF4RwgiNDSkZ6MkMXN%2BBTXMas5N2sTNmDlaJKUny4WNr5BS9gr7t983CnnxRGOAYW3JpwwoeliOkN1ci99xgS23tH8EndEyesMxweGXFJbcgyLqL7qpDJJH8b422SDpghz4MSSkwflR2fqhbWSeolY8ttWwRBaBfRoL%2Bf%2Bx%2BbtWMltJs5WIpXAmxWLebz5ckItTgaxNzFezG7tpOvVVkI3%2BQ%2B6%2B%2Bgj4CoshZBTDDMRq%2BM5l1ICvYMckV0RpV7SuDSSPXiUd87t44qrnfaEDQCGftRdDUM%2BTbvFzfTec9%2Bykh3mC7DHQU4nbK%2BjtYTXoS%2FW3yY3T0ao41Y5%2BPEM2IkFPjrI%2FzMahKuRgV7jxBJwMFKgHPypxRBp8ZtyzDy9klAF68cvuTE2WW%2FIQ9y58B%2FgsxKeMCgI9mrvr%2BpkLhAlvgHEvadOqjCsw96LLr%2Fw7bJrleZXcfy0BwFjGGDelrZCw1qQsiwMcQaeMbJswSeLHpTo%2FElElfBjteStLrQRJM5uNAfMIKejr0GOqUBSANkjjCI3uv9%2F0nZHQrbo0MAx6SXsEWirgjXXbaDTEN6YaWA8l4zijjn03qL3dNJX%2BKSuE5Fa2NJrcUgWTjmbV6nI%2BY3c0FmgaaNM6iJJCLlf4D%2F%2FWpSdeieQW7Qdrc5KsPgIKTkeidJuGCZyWt1RIXh3CujTMd1lB9nxgkMaC7af8O9nB%2B4l76K8NyQVLBDpi8NiLoW2lFHE0iLSYBel%2BkCm5oq&X-Amz-Signature=16ded96a2196d60ec676525bcd3425499e4c0a38ebde3118da5a6453f81cdb69&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DAKNWZ6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIDqL6VuC9SFknPayUCkda9F77EtTWD1ZIMIa9PWebrDcAiEAqUqtoM37IBo%2FsUtXlWAU%2FrmExErMosj4eCJvYGpvjRAq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDD3L2rPtCLxuTszoMircA0VOxBIEKWruiri6jhCdZh8u5iZfJg2Wjbf9fUY4yxRlTKJK02vhmUNk4luuxgXvbMMQvFSMO1GbSgPj9weMTcXXTKkmRUkYiVUhSPHj9z%2FgYiS0ml%2FGghYjToGi3LMiQz99u4H0qBxFkHodJrKog2oPzCjrsSjBFaw7NfPEe2t68KfuHm5CrIdK4JTuDN6S6StW6vJ5uCtRmhnEB%2B1QaOK4lBAxbBkAsvYMCbVYcQAWfbsSEZNjky1jROi1%2Bt%2FmXHvrj3pq8WY%2Faj8yCYlPXTQEi%2BGFbf%2FEEUSUeu8Euvj46IftotN%2FWCff1eyaYGRkWlmpot84SRN%2FI5zAHiUGU6dxuNH9lwgu%2Bl7HVLOlrl5%2BbswZef2B82nyEojUZlVYwOy5BlTCVi%2F8GGlK%2F%2FbFS6RTVw%2Fpy1RaD63DJHAwNh864kcp%2Ba%2FiBumNLSK%2BWQIgOsejvrSA0gHUaN%2BrsoePtYBSBTqpQw58Xb4GNiwQmRUGlJd5qKOePLz%2BrHWFAyzsm3Gif29NipabXcY20aJkcOuO3L0PfG8r9cWtCDalTzRh3ai9JXrcv0xEXlbXgO1sSp2bhYBLlyGY%2BCLIl%2BqdbHNBs5fS7HxaGxKqCDaVxOdJ3XedyIMXcES8Oy8OMK%2Bdjr0GOqUB0wJ2qQOxxCGsjii3StSJ2tDOWAINhrtBI%2BcVqv%2BSZimZ7sLZrxWqg5vCQbnR40AkKZRDfwTAtGhN2xlvHH6B7EOwFJm08jSUIKBm6B0j2kBF6tI4qHhaNaBBmPngVZogadWFWq6xZS2oWxldU5tXskk4%2BpJIYg6BWvJ1TBSJRDhEGDQXDDve8FmIcxSwezsg6eQ8IMEAGkhhlbwyiHKdPO2gh%2FJE&X-Amz-Signature=9d43f7580827fdfe05fa0778c20f275acf878c2923e1a0eb70d5dc26f229cd8f&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOTJ2575%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCF9A51NocoaOYLhb6OX9B82pbDY51pgaDwSfKke24%2BVwIhAKVM%2FuinE9X7VUTu6NOhXx8vFnVIjP9rCXB1jAP7c3Q2Kv8DCEkQABoMNjM3NDIzMTgzODA1IgwlaTfYlNAqD36fYfQq3AM74ke7NonCnKMMDV0iFr6dpU%2Bc6F8SP6%2BA9oMkLF2YqZHO54HW%2F64h54Psx%2B%2BFNkmQ9aFCoCUURCytEnmlwyiqEqu8AYUBmyzL9tfhEXPnMRWORXC5a8%2F9whLtlGry1sIlT0KKA2lw4tPffLRjfvMhQZzO1cgNVsuQ6L990E43J3yc%2FvK%2F2qPpUcryz7B%2FsK360WdPDKD4sFB1ETczQgIgUNyYJl2f%2BotxhZUZzYwgnklo4YX47V0mW9ehnfdIFez7G8fHR5fKzbeVoHIAcNgGdrFW%2F8IsRksROaJeYpNtbO4nSlH75i5RqPPiksSNrY3WbJbBmQmn1gP%2Bvn5XhL8F4PN%2FyFbNLdaFl9NjsjCstB2KwgkxkJHKsRyD5CzG7gIrWlaVwXDqwhA1oY8DMD1BcX8Qqfgy4liN9aAYoM4kf6zoRbqsEoQZsManGR1IKsfx%2FA%2Bn18kpiJ2zv93rAHFxNnFHBzZaOWSeGG6a%2Bu9u7z4kaWqKPV9jew%2FbTElK8mPjlzsE2bICmw7I3DLB5KvFvNfJXNo7kBwOByzyrsSz%2BbxQKe5GLpJSr5nbKk9wjT5aW4D84pkoT1HE2u5e8qJBLyvk4sWRzOPnheGkKyrOxh7eAkRFkSzOjljVJDDlnY69BjqkAceEv63cxix6TqhlEVSuuCffWa2pl73TuoCa59%2BnnhY9MdwiuNhH1%2F0BakDpEM89V4Thnvv6vGouK5B5n3w8BEhvnzijFn21L6TpO5ObIGVv31w6dP%2FbvwZ67laSMwGWW9RHFEXlF%2FTRo0dKZz9NRIXFfGUKrwIqx0fdwAbFGw4akZipR2NaeTpcHGpZYNdyEL3oB53p9d4ulHGIr4gtUjmHcQI%2B&X-Amz-Signature=f49be669626a7213f54d38a4636858fca0702b4212211b5d044cdce5cbca65a4&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDH2ZDDB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQDVHpKdijfEyyUYYqhDsP3TFTqUk28PI6KpumGlcJekJwIgPpS0gxs5GlHRBnuttc5Y%2By7iPGVQdbsskQ0h1qQiq6sq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDBV%2F9S2%2BsP5hbWX3CircA70xfFFQyZvEUMxwD4QDaPaPXEIPzes7tJaN961xVseeesy37jdq9yw6swutlmzpeRSIPq9SaqQ461nJSsIfkOaxR3XsJvA3mKfyY81%2FwiyDhD1HLs4Nst2LTiZoDz9yyqtgvR1O%2Fvdo31XxCJjRAd%2F0iSF4U0icsxmAne0lX11T1bAG60YjXCHo7QJcO%2FDrUfbfEa%2Bv7LRaDqTCTsvZhBlQpvUZEiNFuSTj1ZZF6jMmswniLvWfN3zvj%2BVXeHd9T2Fq3FoWlbh0NfbA%2Fv8bwxNQ71C8INKsLuTi0LWn6sSJ37GO8qsTmW%2FxvBEe8SyBIkBKWnpAeJm83%2FzPU%2F3reiYawb7Ypl8Fw744oYrXT5yzSL9iJVb8OTLm5e9NaLEKCFAXaZexTqWIiBE%2ByTRcb8zKhQwShGBkYKs8IageCw6FUdSXbHExDCcSMuiTUhHmGOKAWeNMbDGtXqVHnkaJCOL2Ol1t5qlUYZLvhnhDgTNwnc7iFbYzhOh%2BEjs0fNnOLVkB0e%2FcI4NpzcO0TDi07z6TL2rTHEYZrFtFEE9ObkcZz9%2F%2Fkl9eYlt5bv03Mv%2BWPK05JIQlC3BqwVl2svzwshQiU7lFNpXDLUvcMtLoPMNrW7xSxuY4d9fDLS%2FDMMmdjr0GOqUBQkMwPd0XWsDosY%2FMngEVOBH9XhkyGwJ5f8ppZUhrc9NxDL1ymf1PGai%2FFeFDUqIDRnqM1dJalC9SoDrfs%2BIDZwgZmokvGK8iH02hH%2F1l1ARRgbYpGdGqKcI1Y9G%2BQny7VQE4M5vDI%2BTqUxmRJBXkUUAbJIBQEVdnQ%2B%2BXNr1SYcvpAKr%2FG4Psu5Q%2B5VRS03LUTtiMmz%2Fi2y%2BcprFSU9rEvFELBN%2BS&X-Amz-Signature=7de9d57ba1468640b7b5b673c432db38fa79adc60abfbc174d876975b58a12f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USM5IAIP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQCMMESLaK0LRmkqqWYAEyip%2BwW42fnNe38ImHVK2WULvwIgNdocLVaHeZs0LrX65YTmpDVnNTR0g5C9q7jlv8WU24gq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDAgytaRDtphBmDuaZircA8CF47NLBoYVpvybTUm1Z%2FpxAvQ1YEmFnJeOxy8MSz%2F4asu3jqzO0d8sFLqKmJSzYgOlf57PCCg%2BcuhiDHywCSKTB7PTxAQgSFWCHwb4DZRDfh2GJHmcUfIRF4RwgiNDSkZ6MkMXN%2BBTXMas5N2sTNmDlaJKUny4WNr5BS9gr7t983CnnxRGOAYW3JpwwoeliOkN1ci99xgS23tH8EndEyesMxweGXFJbcgyLqL7qpDJJH8b422SDpghz4MSSkwflR2fqhbWSeolY8ttWwRBaBfRoL%2Bf%2Bx%2BbtWMltJs5WIpXAmxWLebz5ckItTgaxNzFezG7tpOvVVkI3%2BQ%2B6%2B%2Bgj4CoshZBTDDMRq%2BM5l1ICvYMckV0RpV7SuDSSPXiUd87t44qrnfaEDQCGftRdDUM%2BTbvFzfTec9%2Bykh3mC7DHQU4nbK%2BjtYTXoS%2FW3yY3T0ao41Y5%2BPEM2IkFPjrI%2FzMahKuRgV7jxBJwMFKgHPypxRBp8ZtyzDy9klAF68cvuTE2WW%2FIQ9y58B%2FgsxKeMCgI9mrvr%2BpkLhAlvgHEvadOqjCsw96LLr%2Fw7bJrleZXcfy0BwFjGGDelrZCw1qQsiwMcQaeMbJswSeLHpTo%2FElElfBjteStLrQRJM5uNAfMIKejr0GOqUBSANkjjCI3uv9%2F0nZHQrbo0MAx6SXsEWirgjXXbaDTEN6YaWA8l4zijjn03qL3dNJX%2BKSuE5Fa2NJrcUgWTjmbV6nI%2BY3c0FmgaaNM6iJJCLlf4D%2F%2FWpSdeieQW7Qdrc5KsPgIKTkeidJuGCZyWt1RIXh3CujTMd1lB9nxgkMaC7af8O9nB%2B4l76K8NyQVLBDpi8NiLoW2lFHE0iLSYBel%2BkCm5oq&X-Amz-Signature=c9a1376d1d8c9ae5985fed34dfdfd04ddc2089738f0d7379c6b3b909a3862a80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CQ3V2PK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQDFV4EQrOFG6dX4M6WrMPjwwK3Wx2OlMWtGdY7sMrQy3wIgAx5CweGzvaB7pXmriQiteznCXwG7Yo5OkO6R9brnV78q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDESTtfxDzx3dW2PMqSrcA11%2B569n3rs9R4Sn5FMn83BghuEBXLrFIdi1gIsIcSm4AapRz%2BvIcxTH2XlYYogc7jxPun%2FQbB4JfX%2FZVSMgYNX2o7LgzX2vxw02XFbSMic9lApLVnc4ocJQemd5tXX9h4CVTkM0NpSjux1O3uKOivWCJRIKLuQ1YtZBGL2z5UUMmaCrpQa89dsZgHCE%2BKPgx373bX9PyHq1AaStkCovdE6xxab8Ku5zseldyKcmq%2BVKcoFut6O4f869I6znwzv2eaU%2BISyPPyIjlLwvaHLCp1Fjxzm6n0hJbXVwoWmo%2B5RRxTqJbEGXz0x6ueEVnkRZOzp54lOHL9aydS%2Bpr9Z%2BnWPKUoB%2F3r3n7l%2FH9NKkSnqhlfWKrp1RjIhsOYxfHjghaAvrpQ4GCq7mt9W12mfhFou4xCltnmirU7MV75LM2RhYnEDrixsQmE9aTuhEmnfpA8zOp%2Brq%2Fg1DUWe9VySDr%2BYQKZZ4y5LUK5OzmdFQRWJR0cOOyQOQdFVVEanMxRO9o8GgnegXvDX2KEfKRxXBvcvACUDkyKCkmDNdoYT4Wid67mE%2B%2B7QIhkAuuiVzVJyDhH%2FkBy5P4w7B%2BTdESioWiiHyMyYGcjnsbblCi74L3NS6Qjn6Ei%2FQpmFx61QwMM%2Bdjr0GOqUBY25liRglN7dzloEuEqPtBJnzmGshUqQnb0wCsEk5ofwaV0zGypoYYwDj3oA9gya1gVhOR7Z8jWCOy39I0YsFrhPd8roTAWaKESPNsvFXChYWowcQ16NU8%2BvBdviWXsAoj7M%2FyklqZ8Ti%2Bt7kGJhmGT02gN%2FtM5fC5zJJgtWFzikDlMVIa0oy2niby1LLdz%2B8AIBqh3GEOz0MF6DYzoG%2BBYccVj4h&X-Amz-Signature=1b78c8c530eaa36055a30e5797a26186e08b84c4b186f4967bd3ce5398814916&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CQ3V2PK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQDFV4EQrOFG6dX4M6WrMPjwwK3Wx2OlMWtGdY7sMrQy3wIgAx5CweGzvaB7pXmriQiteznCXwG7Yo5OkO6R9brnV78q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDESTtfxDzx3dW2PMqSrcA11%2B569n3rs9R4Sn5FMn83BghuEBXLrFIdi1gIsIcSm4AapRz%2BvIcxTH2XlYYogc7jxPun%2FQbB4JfX%2FZVSMgYNX2o7LgzX2vxw02XFbSMic9lApLVnc4ocJQemd5tXX9h4CVTkM0NpSjux1O3uKOivWCJRIKLuQ1YtZBGL2z5UUMmaCrpQa89dsZgHCE%2BKPgx373bX9PyHq1AaStkCovdE6xxab8Ku5zseldyKcmq%2BVKcoFut6O4f869I6znwzv2eaU%2BISyPPyIjlLwvaHLCp1Fjxzm6n0hJbXVwoWmo%2B5RRxTqJbEGXz0x6ueEVnkRZOzp54lOHL9aydS%2Bpr9Z%2BnWPKUoB%2F3r3n7l%2FH9NKkSnqhlfWKrp1RjIhsOYxfHjghaAvrpQ4GCq7mt9W12mfhFou4xCltnmirU7MV75LM2RhYnEDrixsQmE9aTuhEmnfpA8zOp%2Brq%2Fg1DUWe9VySDr%2BYQKZZ4y5LUK5OzmdFQRWJR0cOOyQOQdFVVEanMxRO9o8GgnegXvDX2KEfKRxXBvcvACUDkyKCkmDNdoYT4Wid67mE%2B%2B7QIhkAuuiVzVJyDhH%2FkBy5P4w7B%2BTdESioWiiHyMyYGcjnsbblCi74L3NS6Qjn6Ei%2FQpmFx61QwMM%2Bdjr0GOqUBY25liRglN7dzloEuEqPtBJnzmGshUqQnb0wCsEk5ofwaV0zGypoYYwDj3oA9gya1gVhOR7Z8jWCOy39I0YsFrhPd8roTAWaKESPNsvFXChYWowcQ16NU8%2BvBdviWXsAoj7M%2FyklqZ8Ti%2Bt7kGJhmGT02gN%2FtM5fC5zJJgtWFzikDlMVIa0oy2niby1LLdz%2B8AIBqh3GEOz0MF6DYzoG%2BBYccVj4h&X-Amz-Signature=66766040ab9fbeda28766c6bb0abe9e31533745e8dc3be85c05a3c291fe9a925&X-Amz-SignedHeaders=host&x-id=GetObject)
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