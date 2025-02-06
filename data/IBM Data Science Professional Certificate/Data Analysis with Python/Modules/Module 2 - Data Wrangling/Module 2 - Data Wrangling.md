

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAW3SH5D%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDEYe4H5wHenpVrHUVh7KqQG6v%2Bt2eE%2FiwS0GYVtz8O1QIhAL9QjpHYfar12OFtXiknvTYDXGFGiVLdAb7rzQB%2BSwAVKv8DCFEQABoMNjM3NDIzMTgzODA1Igw0PdJLMjCbp468Xt8q3AMA5iL%2BSDTPFUjR8z56vWyom1DNHi6Ju%2FFnsYwnsp21vUC90J0%2B4aQaDzUmD7zHVDSHUS2Cr2SKAhk0zFJVT1ZCsA8BMOmrrLmNeDut7sTT8jMORjlXn%2BEAP4cG6JhqqYYzUEzgkIaejr55DeGkONAaDpd5zPjXvqcucrNekoaKqUfe%2FzfKGh8UKFJcDnIGhXSicyPyWZzzRj%2FN8JbopXKOmrBdHRUhdRM%2BhsXDSbIGePOGXYMxrEW9ukiMGmq7sRaSJfhW0T709xksB4LNeFUpDSaYbTq61mq2a%2BQpuCe%2FlkBV2PbpeZ8naLs1ZPZYh%2B72jzO7sfNREav9NCL5o5ldRsemip9FUcXW0JxMNYXHaJ0PMYg1JK9bFQbammUEyM545cqWcWQD8Zx%2B2%2F7J4NiZ5Rx0AeiTaUawDG0CcjYNNvHLJpQGwvyBGLwLpO3h7U10BODCWC0yAqNo%2FyDtqFjuHRh13UJEiO2jH0zfFb8bJZxN%2FsjnS69G3Sq3DN2v5WF3wMlqlgyZfREu9sqMTZRTsukY9NeL8QI6igjKVsdcarVF0RJA05fgtwXL25t6ctYokWVDQEK8fEIKi3xEx82gFz2gtmCVBvVqpeHAov8jpq9a1UEPo9uuB%2BHWeTDa6o%2B9BjqkAfCjYomfjqPUnzfys8a7khrPKHWnhhDqHLRgoZdjXzN9Vnr7SMSSQ7IMqlTYw8BN0HtX%2FBpfvo5%2FQWyaKGKgxuTPJ0RRSsDcOupmjXac0sgBwHrczT4%2FaFlHhp6xIyntv9aL8pkWwtogPmuRU8QNJUK9WZzDbZe4%2BbESBjLeVjMbHuXY5HxOEMMzLz%2FteRnY6GbNOq8Q5u356P8qe23nS0X4skpc&X-Amz-Signature=193a8e36fb0060a8bda3c3842be4d385771cac82116654cdf6a9564dd9277b6f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCDMOD7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIClj11Q0hcjd65DHHDdw1Q2PevMrPQb4smHYj9K4vMHtAiA1aqJO%2F5h0bKPwLpURgajE5RzJV%2B%2BJryyRy9A725qnIyr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMdax0v3HtKFNDRMPPKtwDcPveK4US%2Fg%2B8%2FSoRmOPgqezFSVdlq3xKtQTGsPlIzq6tWkTroCxfOCTks1TznD8CJXLrkUI55Fk1YI%2F63XT31%2F%2Fg8rG%2BAyU7Rj9FpLuGUNsu8uXqevS9dkUDtweKoEzHW1gR2ys8gMDPYAo3ooodqn12yhUJGjc3Z0VIvvn59uFJHThB85xe%2Fm9k1nfEhuPcrxdjAr6D7LI3I5wuqzvHPmQe%2BSDSvXs1BSMHktjQg5ichcqoEKfRkkiPJdbBIOzY1Siq%2BeW1h1nU0Kq4ZUQMeQXQHqji%2BW0qGDqb5RGwBlrSLWgGypbM5j897TJPLa%2F4ZbHFQlnsAjN6WGr%2BrwPtlx4IjG1qUafAQGUV5Lc5L%2FmXxGwK7SCjyfxjfp8cfu4eM9f7c%2F77VE9CpR%2BwRiSSkzRFvvxqei3QYWXPy5dOu6Ego%2FQl4pPTOK4q271p9UArgVfYIk5onN2EawEpnFzQhvvTLbOOB2iZ85qIrV3lh5SxZ7dX5Gduve1NXM1o%2B9vfeiVD%2Bh40K9komLXEVL4eMDzCecsaOOKkG%2F03fDYhy6VyzLxkg6Mm4A6thknkq7%2FZtLV0pHN7YFdY18VTIOVVDTB%2BqCHaqvyfCwVcxbeBjiCuiDjkXiUz7GxJ50IwveqPvQY6pgHhwxD4G0uODoBrAzYG8nmAogrmO%2FE30rfOQEcAK7qrH2BoyQQibb3HAYchbXBkvCsae7rhL3p5KHVKZ33YfQvfpbMCXZ8F3C76BegxbDMtBNqlJtBpCHtucG6LHPCwpt%2FdWJ%2FnHACeoUwRzXoYui16sLiwlIxxujbALNOmZfyPbIBd%2Br69ZX2QvlA9YJXvj4Sh%2B5rGg2HG5ch1QaI%2FDPm42bYj8awF&X-Amz-Signature=c5b4c659be29030edc2fd2bc753b2ee77fcf643c7c04e83aee8cc73bcd260a03&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5NJQNWQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGmPilELLrCTEwqPnCjj3UnWFgnKZrQ86wTgKc1xSQKPAiEA14FQuyNZUBvjW2Hv%2F1HYmUCRz8fYDjC%2BSqjskYfN7Ccq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDAyzvZ5VVkwt7yNSiyrcA%2FDCUNXK6enfN465iURw5i9Knlbeuj4ovsYNukQ0m5VSTvgylNU0GIZVaOKYRq1PcQmCxCZpVc7ZGmvzMD9jRL%2FMeNvK8TGthwVXccl9P%2F8vx3ZTU%2Fd%2Fhf2%2FLq1Lfde6T229HExQ1jUDJQ4tYMMaEW%2FZagkpiacuXTpQSnBwFFQ9xpn5ySc8ug6lJGqyjnfszToq4KA6nijznykW69zjBo5rvFIR9br6PBlzmrz3uSl5s53HP%2FnFCCJpN16ZZ2iKqm70jw1fjImOBsPMp%2FKADflND9GYQ4kmWuJ2fzxCOCgNDS7sMfTyuWlDFU6OGJS2NzCZymKJATaFOM%2BwwoqabtJwwWAOCDO3OAQL9CFG10M0v6mFREsLkNWtAoi4ezlamqag4IZ5jgMkbh6RYkR1eHB%2BviaMvv7zp2bgFTnAreNoqa8kY%2BLF2MHQxVPPuzVyBWON%2F3Tk1UUrqsIcywxfIM%2FeXxHS0aiW4sNFCXfvlnzqEn1SP0EDEzR43U9EVGROg%2FuSCPHfpgx3DH3QRiJywKALA0W5uYv5i1b%2B1Yf4%2B0WAa4PhTucYnYPhMW8yYr3TwSoqjsjia2eMHZGBLJuPS4FMZMmjCaArF9SgF81Zmu4qrCjdwbOPTAVAm0sLMMzqj70GOqUBkeDihwtT%2FYi9VxTDF16nmplu%2BqMOSR4L3RASN5vfzQiwlwv5wqdnRC2UKQzxOdP7NDr5xBze0hCi4ytEUsA86ajcVH9rr5kGAc5lW%2BS7RGSs%2FXlPstPo0PLaIUBCnyfoGdUgHx9faizLjDdmamYqgsJer4m6avY8k4U31PJWpdLVrg8%2FMwIF9vnm3xynAMqSTATJ3LbfrKPHbqo4yIP%2Bei%2B3B3lK&X-Amz-Signature=17f45174f1c28cdd518e6f1f14709b14b6217d5049ee4d49df76ade718c571d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5BK6WEP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIFZvDgzGKAl1gbXP%2BfLPXqNhc121G4ufikRgFvnol74nAiBCBMz9H9pfLezvyqRcBykxCzMrvP1gTDlEYXZloyKVJyr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIM2O2TrJo53fxdCcGNKtwDPgtFjdNcwqc6Orp6uuG7X9s8vrKpNvfBSUmG8%2BqA27B7vYGp9NgypR940nEmTT%2BoSui1I%2FeBpL787er7Ku9btJtBBORRt5hOa7Ebea6C6L2jqg3SD%2FNQB84fuQuN4alMveTdxguCZl3rAIwWDNjqy0TBfzUQmbrnvZ%2BLOGKg3%2FkxLMv8gX%2FUpcejd3SmxYaVM3t7iNdMP2hbvZcpcjrtPTAzSvAQpQRJ0jyt4glacpjiy7R%2FijwQamyLSUyKSUIjEKd%2F%2BhU%2Fl3W%2B318aID65Dc3E41%2BTRCiyTjznkO711wr3WTGLbFdfroP2jNfAJiYaB3H%2B0teawKAxTXcj8RU%2FvHctIxNRiJLqLRQ8pQgG8KR%2FWFYfgVq0xHA5pbgWwm0dp1ILXQmxfQeaXYn%2FIqHYd2qPx8%2BA%2ByK%2BqO19yrQhrpMF3wD0jpf4r5tojZBMY7J4mPE1woruhO%2FgPPpa25acK7ToFzVsug0H8sYV9ZFGwXBrxKKCyBH3908vOWdpuEBLQlHSJb9bdd1hnpo6FMeUSjxXUl5RtTjhmGRc0QdC5aO%2FOoOVsOZ1vD%2Bn2H0%2BemP3%2BmEBwy12Bh%2Fpw4A18FiG3rC4e9WerzFTFJdJGf4FeE%2Fwfz0GoG3Y24pJgJww5eqPvQY6pgHd6DQhtv5V4vOo8wD%2FpI%2FaQ2QOaYzmwj8%2Bf3BfnAJLmj8s3KH95uges%2B3jFN1CaWB9wH%2FE%2BHe33ZlZmP0%2FLVqwD2c9FE2SPao7b0w3JHQJlxHCOf7WqtVAQp%2BTXIM9TYS9fI0ZqY1cfz6%2FkduZhZnZLxm7q9qgaON1GTDx0VQvLgHHTX4254ieWfvgWAjzD%2BncYN7OttDA6r2m8Z71UhY3pVg0wl6o&X-Amz-Signature=a910decf8544864fa1457c52d8c0127fe1c29faffb59ac5d11037cc514b78ecc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4YOXE7G%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIDdJ4qWcDFOHv0DLh0XeJM8IKo202ZxjcsKUvpFGwLUqAiBCM7tUneDWpBkD9k2%2BVbVNROyNDHx0REI5dE3hMF4RXyr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMM6EdEQ4ySutkwVGAKtwDmlehf7hcGXRdwXPHkUC3Sjwto%2Fj7wocdrWibxbXncnefKCnSs%2FmCqz6wc4l1zJJUiTgerb0bEK3IrZR0WJHMKLnOz9G0fwXqlkS38nlrOxLBnUV1nlDxdscWZg11naFufyiX6u5U%2FFE4VyZBxhced2G5rs06sqRKxOnk%2BztZO7%2BkhAAYRTDn4ZEc%2FB9D%2Bs%2FV%2FToIjBp0FvdmYJeGOx281SBZgG9zHF%2BpY%2F%2BqqH1%2Bf4KwUyg5xzYJWc47LVabweZ658uBUkwb%2Fq2UJUqQBtE0%2BBgTYAOqzLX94XByWdN%2F%2FLeZjpbcO44X3%2BtIzz%2BVYmtIt3k3nj9dCrucuOXXzsthR05egNwJlDPow2tWGPim9zptnJeeu6wAM5oUhW4Z2MtMHNhjOPlNz9nBp2dG3B4vPyCMjLzLvj16SF6OF5v0xwklNNGzyhhpR2xQU1XfNzSYRw2EK351%2FxDOrJoLrLPN3clh9tArP8fa8itPgytp2SGYuXMj%2FIWmOGSAgdOY0Vo8e%2B8Ze3nB7P1Jbxn3kiG4n8NpWmCPT46FOXOb4c5iQm%2FMKX6QaHKEgckJGrKwP0a538568UilumGPyYdcBUHFmK7j2FQ0iHxOMvMa%2FXndXU6f0MFg6r6URMpoLtUw0%2BqPvQY6pgHxlPDzJ36%2F6jTC4IVJwJ0dD611%2FH%2F6a3axtwAgRnBmcBLYmw8a3GZG2eGduRcdUcUHpQPh0XUtVTqiOSnSH4qoadMqPbJMHctpviOV%2Fq7iMUirsu7SSoZ5gdGip3mEEnzJHY66iiWlSdkEJCmFg9Lhz6k2mURTVyGoasWaSA6CD0SGOoqxaDWe5sU6OF7iU7%2Bwi6JdGmp7A%2B3muwd%2BDSNc9afk9rxQ&X-Amz-Signature=a759906658ec56118241f29097c04cba1c012fdcedd40a06a4607495a5b2b8a1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632RDVKML%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIBMgf4T2tnDW0HV1an%2BgRJw0XLYXdXTTn3LFK26p2CSJAiBMwy%2Fd1ur2uHRfiUaUwVcsNT%2F98za2wd0ONiam7%2FMWYSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIM%2BY4CnNzMs1FVOnTAKtwDxWbA8nkf7B%2FrMYcixLjPsyOAJqM9F0IX5QwqRO5iT8YKtL4W6q7mfn7HddIAAnTZmZxr9QvWQEpemclZx%2FBQjFH8kT0dIfURuX1maeDlxHWC64EOM7V%2BEsy%2F38aT7MxLIusT8Cu4ip6Ac5vIIERGsXIS5WjIWM62V2QDy7TmNHGeyOlwkS9rpL%2BZTssKpbYkRkftmLfbNqWJJf7T4%2BISwCeBTJfcdfCI7gLTeZmf4orouG0aAg4Ua9o8Jmot1YQ35Mk9YtIv5GbaXYFyx7ie6rwKDa%2BFATwOpv6FbVvoCuqnuhIxKlqeVmz0kgmFD9SHBBsOJ2OqwEpMhP2PX0%2FG%2BXngyB8hMfFBcMG7z%2FZNBB06pnpe%2BJWQYHa%2BcZUjtBMIICcx7miE1uv5mVS862FxVqcHigsIVlRukhe30sql3%2B1nxkLlMldZMyl7NAg3nNds8qSYcjBGqF0Ey8Eeiw1aNe2PK3LgS6RVlNOZYHbzmSJR5IJtDJVfc0p85IJYlBzQ5JDU6go%2Fcv0BFJYLpDRSo8cmj9XBqFwKx7k8tzYviQ2KyGfrjDLWcygSqBU%2BtWriV86tdqM1nxbyk9DwRgbnKCO5f6OEJz%2B2ybKJqCVQCok1uZPpz%2BvRN0GU1XQwteuPvQY6pgHlluD0IZcoiz4H6Yu0cMXFk4DR%2BHNp9oimuBh1N0gGSuX8cm%2FHB4QC2j0M1rarE4ue9bXWY%2F4U1U81AuvRi6oWgbcyPCW9CikJ653bmW%2FnLilu9e9H85%2Fj73PWZbzDP0e4A4PkhxVwVQdMmPC0niOQUh4QGrzu4bnD4tpockInfFcjXHZijWifpdKjhjX%2FFWbYeq4HbPmSHL4IS%2FFVNeSm3AVbZpWT&X-Amz-Signature=bdc15b9888769a61916ac285919cbce46e3a8a5fe2e588d9c3d29a780a3a40f9&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2QGL2AY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDXylFaSFnNdP0KMslQZdAivNbfAhfY8q8v5y7oe6kzlQIhAK2pqBnqheSo9Q%2B5j1wGYpIIgm2yb%2BVIuDOkzW0EhVBQKv8DCFEQABoMNjM3NDIzMTgzODA1IgxpikqBtoIoRmVqCCMq3APs4V7Wpub9ZMFYRS6vNdMBxtYTSobS1Nki7W139JOe3SBFWd%2BJ7C62rpLf0GC6qz1mb8kSuiMwBiDcmyHdnhy%2BCsvYC2KkDaznvqGkOS69Tmu97o7uBHk%2BRIKxaIVAcM4xAPU92M%2F3aw0Kob4u0L%2BSsC5If3v%2F3gKc33axnExQiqwO36dpQ5ZK9qCHJAlnXdqfiiRy7KiMkjUiVnLJAS3YF2grpfAi2CzLSO6T7QZQkVR58WemscIVnaznTfHhOQwmI3iaONnOOZ%2BI1BtN4K%2BLEzRNSXh%2Fr7PG1HENS0IrKd1ezQDvOtVTNOUiq3a7%2FM%2BqGAtWgRWc81klK6%2BUqq6AGsfjYCLzUhDJjzMIsUy5%2BfUMfA6izYPE3ADHJ%2FIXJcCsrR1UU8sgFcWFhGwzSHAlhD57%2F95ey3FssAXPpv9e8ezWTzZ25ps7Wi%2Bt%2FvEXlcL0LGGc8tcMXq%2BamJhH%2FUfZiNtjsYIb8lvZ5g541wWfTdYKKzzbuIkFy7h1Koq67bnib1qKWJ9tOGCXvDgI6Ev5YjZpmudQgFXD6B9tOXRTgcuoGzMRtUXCB%2Bn%2BI0FqQylyIJL8CMtHHYWbrqWdBrqdDutr8lOFkfcAavH%2BUsYC7xYXMO3S0wIMBQ%2BDtTDT6o%2B9BjqkAYCMGMyAsfxyI0TzgSIVXc8ZQteTBatJUMbuk%2FB%2FwWgjF6QjJZjQmxkP2tZ9xgawA%2FVvIPMNJBp7PUvo8CImJEHdcQxo4DLFUXu3M8nGNVUZWq9WhKeXtyKZgnzIK1iCRRxkPUhAvPD0auAstLnQgge7qAXhuWNFDNaGCM6tub1ZSri1bmvkqXsYQWPQib4xwfcN%2FVkAFLnYJNVkrujhBjbtCr%2Fa&X-Amz-Signature=280994e5e0d5cbfc57fd5f55d44979a628918555926d428e85087586084fc5ec&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SS5Z7A3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDENJ266vVFCt7bjc3DzlFK197CTRYINCfMHGiftT3rzwIgaJG%2FbJ90Kk0iyxPGM7nPAxkSaaFNwLQlJCh%2Fapdd0osq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDKNO8i1%2BVCNYevnjISrcA9FYwcQznyUGLKWwPIj7%2FKyBlvYXSFY27MT0kFeVUZT%2BYl9lmTsyY29bCyzJPQdqYyoCz2btHX53bf3a2DnSCjZVUoZVSg2EJk75jkZmNVclRrVF8AT%2Fzz6Cd4tHnOLe1rDgeXO1EZa7gsZU%2FMKGGlEeI7NMwCYjoUNT9XV0bFOe23SZ0uDegXQztACQkLV0%2FIjDKSyO0n5drcE4WsVdaGHGvJRU79s9huBTj6pDDxjcGdlzrwFX%2Fbr%2F9gEIwPwliuoOtt5I9sEvUjGLuTbmDPVOBoMP3rWwiGbWUzMvlFr%2Bd4EUqxe0ZNt8qNaOD0bnbaVzsf6RnNUxNHbYKCVzGUFeLnM%2FGV690nMgABg7gUv90XRZUDqk3Io00pQppMTLKh6LX3z%2BxqByKHqng7JvRZoke%2FkXFKcMCNWegxYlQoU%2F27LNB1lePiQmu%2FIihCfFORAu%2FyNG9mL6ms%2FKW%2FYN74D9jsSW1%2FcDlaVUE0QjN%2F3A4DvQZlsp7HbmIo4lcDOiAFYy%2B44Fi0n5b96BZP81fRC2EFCP6SWC2lXl7ksq2Un8L%2FABE70JsOa2cApdyZGWSxCTqbyILY%2BzNmmjJX7dNH%2FyyLWkZEJAWN9IH%2FNYblAZRAoCmUN3G9LKcl7iMMrqj70GOqUBojMYTQtSqKCnsPf%2B0yNBZ8cdVezopb82ZZK%2FW6bxHpw2yjh91FECoWHrNAIGgbmgFQi%2Br%2F0m61ooJYCMTxIOmbxRck4dxG0rnNlxQh80yft4a0vBU4uvhKghl4j1T5xRKXa0%2B3AV7CIK2m7GWNK1as86ECP71WJlzz%2F2KHUrhCBh1jnG8U5lurJS40F5%2FEBM%2F8NBk2FAmXKsoYc3Jf0Q7NMBSpUg&X-Amz-Signature=8c5b92dacc60052218a61074af612e4cdb976ea2783968c182a77efabc676eb9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4YOXE7G%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIDdJ4qWcDFOHv0DLh0XeJM8IKo202ZxjcsKUvpFGwLUqAiBCM7tUneDWpBkD9k2%2BVbVNROyNDHx0REI5dE3hMF4RXyr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMM6EdEQ4ySutkwVGAKtwDmlehf7hcGXRdwXPHkUC3Sjwto%2Fj7wocdrWibxbXncnefKCnSs%2FmCqz6wc4l1zJJUiTgerb0bEK3IrZR0WJHMKLnOz9G0fwXqlkS38nlrOxLBnUV1nlDxdscWZg11naFufyiX6u5U%2FFE4VyZBxhced2G5rs06sqRKxOnk%2BztZO7%2BkhAAYRTDn4ZEc%2FB9D%2Bs%2FV%2FToIjBp0FvdmYJeGOx281SBZgG9zHF%2BpY%2F%2BqqH1%2Bf4KwUyg5xzYJWc47LVabweZ658uBUkwb%2Fq2UJUqQBtE0%2BBgTYAOqzLX94XByWdN%2F%2FLeZjpbcO44X3%2BtIzz%2BVYmtIt3k3nj9dCrucuOXXzsthR05egNwJlDPow2tWGPim9zptnJeeu6wAM5oUhW4Z2MtMHNhjOPlNz9nBp2dG3B4vPyCMjLzLvj16SF6OF5v0xwklNNGzyhhpR2xQU1XfNzSYRw2EK351%2FxDOrJoLrLPN3clh9tArP8fa8itPgytp2SGYuXMj%2FIWmOGSAgdOY0Vo8e%2B8Ze3nB7P1Jbxn3kiG4n8NpWmCPT46FOXOb4c5iQm%2FMKX6QaHKEgckJGrKwP0a538568UilumGPyYdcBUHFmK7j2FQ0iHxOMvMa%2FXndXU6f0MFg6r6URMpoLtUw0%2BqPvQY6pgHxlPDzJ36%2F6jTC4IVJwJ0dD611%2FH%2F6a3axtwAgRnBmcBLYmw8a3GZG2eGduRcdUcUHpQPh0XUtVTqiOSnSH4qoadMqPbJMHctpviOV%2Fq7iMUirsu7SSoZ5gdGip3mEEnzJHY66iiWlSdkEJCmFg9Lhz6k2mURTVyGoasWaSA6CD0SGOoqxaDWe5sU6OF7iU7%2Bwi6JdGmp7A%2B3muwd%2BDSNc9afk9rxQ&X-Amz-Signature=968b04e43dc56e7dc5888e815c5ee78f57df18311c3d1bfd23e6ee19856e7dc4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AS3CPDP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBoNd8bXynNtdq1YrL8vY4lvudrdrEqOxhb3FJrc5ZQEAiEAx7DCv%2BTzZ63fd9RbbFQwYU45uG7U7Pi3iIxwKXkHyEoq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDLM4S9ZXTIhHTOJc5ircA1A6R9DmQWEOltAW3nJ1qSbQ%2BqZe7t511FJQa%2F5cywis28w8lLVrwgjSTgut0W4OP2LeQ55i4Sfg8%2B1IBpnaavd13wuS9jTcnxaEXDtrvcU6kl5mVh%2B22Vm5xCX3GzEyJ7bOB3Svrt3%2Fpd4ggZdyROahI3UpEp4VMKuCyB%2Bso17KA8peX%2FcOODpoTBnoKMBspzLhl%2BA24xPg%2BkoTVpukwmVenO3HPr5vi1hs0fqms8ixQGfCViikBDSBlTPZ8%2F%2F0EJdSL9Pq9NV5jZIKICbIL6PhxrbO2xxxz0vj30XZRNTsigueqvPmXm%2B6di6FnHh6as69ztaZVsiMhSWZFkQCQXm9MzOr1sRI3BmrQ0oKlnFB%2BsL1xFhhe%2BoVMB82kkkCOBlpgTaFg3BpDVquUnjiOiUgZ%2FesWZIW23jU1Wks%2BWSufgHW8jP6%2Bz2hgz%2FTEkzkNkg3os3FJqG3oBlLc1EHGIX6ev%2FzZ5DHOqkV0ZK20Aad7O9i6qg6LhvsIxT1xlvg3XS5xODNAs67%2BMNzkErbAmp71nlEMQE2MYqU0eEAkiGsTu3osNGmYFkF60wTtdCCcnZWDSJ6kCGSTAQI%2F%2BfXJgwehGt6NZb5MZKJR09LOla1ZDHCBXk469KLw2OiMPHqj70GOqUBKFXtkAzUMOBU9symTrNSHHzKFU92YEtzUH3MUJx%2FcCzBRfjwBx3wLFtknv27wCW99nSXJYnGn4%2B92BZj5Um6OnmWaNxCW5jLRdCGoQ207JvLK376%2BT0pz5x6DeYVPJHu7Jxb%2FsBpJ9XFH1UoEAZ0ETuPd7fzZWm9fWcUYwil4dbV7RxeTJsXyG4VINyTeX7rEfazwcSnFP1k4GTKGfMU4ce9BMOb&X-Amz-Signature=cbd248141f5955eb9b39a9eae452a8d20cf1cef9e172ae6658ace85d2da1efdd&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AS3CPDP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBoNd8bXynNtdq1YrL8vY4lvudrdrEqOxhb3FJrc5ZQEAiEAx7DCv%2BTzZ63fd9RbbFQwYU45uG7U7Pi3iIxwKXkHyEoq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDLM4S9ZXTIhHTOJc5ircA1A6R9DmQWEOltAW3nJ1qSbQ%2BqZe7t511FJQa%2F5cywis28w8lLVrwgjSTgut0W4OP2LeQ55i4Sfg8%2B1IBpnaavd13wuS9jTcnxaEXDtrvcU6kl5mVh%2B22Vm5xCX3GzEyJ7bOB3Svrt3%2Fpd4ggZdyROahI3UpEp4VMKuCyB%2Bso17KA8peX%2FcOODpoTBnoKMBspzLhl%2BA24xPg%2BkoTVpukwmVenO3HPr5vi1hs0fqms8ixQGfCViikBDSBlTPZ8%2F%2F0EJdSL9Pq9NV5jZIKICbIL6PhxrbO2xxxz0vj30XZRNTsigueqvPmXm%2B6di6FnHh6as69ztaZVsiMhSWZFkQCQXm9MzOr1sRI3BmrQ0oKlnFB%2BsL1xFhhe%2BoVMB82kkkCOBlpgTaFg3BpDVquUnjiOiUgZ%2FesWZIW23jU1Wks%2BWSufgHW8jP6%2Bz2hgz%2FTEkzkNkg3os3FJqG3oBlLc1EHGIX6ev%2FzZ5DHOqkV0ZK20Aad7O9i6qg6LhvsIxT1xlvg3XS5xODNAs67%2BMNzkErbAmp71nlEMQE2MYqU0eEAkiGsTu3osNGmYFkF60wTtdCCcnZWDSJ6kCGSTAQI%2F%2BfXJgwehGt6NZb5MZKJR09LOla1ZDHCBXk469KLw2OiMPHqj70GOqUBKFXtkAzUMOBU9symTrNSHHzKFU92YEtzUH3MUJx%2FcCzBRfjwBx3wLFtknv27wCW99nSXJYnGn4%2B92BZj5Um6OnmWaNxCW5jLRdCGoQ207JvLK376%2BT0pz5x6DeYVPJHu7Jxb%2FsBpJ9XFH1UoEAZ0ETuPd7fzZWm9fWcUYwil4dbV7RxeTJsXyG4VINyTeX7rEfazwcSnFP1k4GTKGfMU4ce9BMOb&X-Amz-Signature=f15f64fb82d341f4bae2e95cb182f7e60ebc3542ed126dc2f784e755dc177dbc&X-Amz-SignedHeaders=host&x-id=GetObject)
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