

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663I46NRGL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIALXekpAJrdPfo3h2iCxl2Q8inokMkrg7kZFH55NvDENAiAJukyntx91CO9L4c2VXhmsSPXdxr4GOshGuYtyQuIkcyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxB6ykQumBKZYr36fKtwDw8IksH7ESD3HTVJDW%2BuIStPIaLGSDpq%2FtmO4O508oEKextVEbf5e93Z3LwvWJFjnoq3Llfyyre3kptnwVYka4K5qQcnjD59DXFjx6hPy37kWRGUP8sutxHxxJfceAmcDwMb3wXyel609khOxwwzw25Bw5c0mfn20KsXzSOBAXSN%2Bq7jhsuYCVVqe7x8ZE75uqdKW6eLwYxxzFOroFNndHfAq23zZShyYrgbpQTHKPmgFgRmKzZOAulrfyFvjOjg%2BdcZaluK96MZWRyH3WAfF5snaeDjCM2CbQATQgkVTYjpNP7t5xa%2BHpXjPiZCA4x0YD7tcMZU0v5VRaxNSU%2Fy3dP4CXp09EaWA6p0zGlaFbbsBxwB8euukNfp%2BrJBwqb3w9kwxlywerfMMcDk3nRuEoJsOlDpmfgT9lZ%2F1eFIDdtMV3vc9fiMP2LDjH6MDH8akgGyQGYxRPUzLNXrkBntQf7Q97PrSiIq9JXvip%2F44jf5Eo1XrhdQwvWoekoWKfTiIvkTI%2BM8C8w8%2BMN2ZNJowXcV3NOgSihM6PAhXGb%2B%2BJZCnCV0Fcyb8ogXiDwGByrFOpepG9aIcj7CfkxwLQTDVZqc7Hho16nO4RkIR3FIo0rtsqJAWrQSC0Y13PRYwkI6cvQY6pgEJ7dSl%2BP%2FoVE35A1UdATPgPdEbmdRFk%2FrnIs7kUWLsEGZ47S0Ctu6mTnesi6%2BZacfZkPmvtWEyHkhPn7uoUJ8IoAMzFhn3sTHKsKfTB08ERQpJ5VbKWGSA%2BZyxHaNJZ6NtEiV50e8sa7Aj9I0M4woJLvAmHV1IsFgIh1W1yMI94PrZDnmtngK0xN4NVVYZdCjD2WefFcaMN3hN8DpOxTBaJqpPzhgj&X-Amz-Signature=431cf97df628edc6ced7f00f9ab24b75a72544a5982a03939cd698429021dfe7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AFYDH5E%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGrxMZSYGZ7jlwHj8ZKPWiX59j4b1ARDxiqDVP%2BZCvczAiEA9il23UAo8cMqrBOmvw4tb8fmZnCdTGIi5%2FJzSWHVseAqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFVZFnsB3wGIA2CZkircAwF1YcG5oicuquvQq0pjJIBfXON4FpUh4siKATYnru5e1%2BIlggiLIT3oTF%2Fca8TQFboqoDTbhPXQhToVd6mqQmFzl8nATnN5An14uqCe7nU9XnOwEZoogedjDXCH%2FupN4ZBEJBrSCIZcjzE6%2Bte%2Bh1LV%2BOgiG4CHtCXAlH%2BuSDzBuZHQghKRH%2FKTgMiBaRTH1N2T6Oom0EDZKdzXixJRN6tvDIaBYQIlIAzKjtKkcXh5yoq7f53%2BBj%2BwnfeVLCmNUjFusa%2BzrXvScLYDS6Va61e72s0aozX%2F7V7fN426yqQbQcm2xEZ9eGrIMu%2BCK%2FxUMHa%2Bjpj9FbK91wxefaioVgKLhjTtDidJbHtfhO07l9Fd2N8ceFB85Ef%2FZT%2F7BEFggrn1ne3EBCZ5SPk18PJI9rb3Nr8z0SR5ZZNS%2Bl6VyprWeqF6UXC6tz19dkBCv6Kq6N6ZMdwsIIw%2BvutqN8G2uM%2BzamJjucTJOS9JWZdmO0ZIm%2FTwERWVUWHLW27kaxQJVCJ861NjgTuXAxjflnl0XJp8HNXcAEK40cPwLRLt0LPRdCbwD%2BCNozZCitPKh70Amv3tejxRsPYRpS1h1XIAdTNPM0iL%2Bz2AszehpqJKy0mj5hTcgyxjiPvZU07uMIiOnL0GOqUBs8aJq%2FnqPwgTAixPWrxDeyU%2FrBd48itE7RWqSjgCVC7nXmjS4NlBYtJkM2ZQsLnzmXbdhbYHTUEyTVQj2YFQT6dgY8hyl%2FdMbyIdnCLxXQVD2nN3BYdzaWqA5sV7oLk2U5bITZXEMJI2jjLBs3or5cwprYHQNJHG2dKSG8XbskMdd6GcW8hqK1ZMZCjc8MQCM2uyDc%2BjuVi0h7JlTlc7HwEC1nyV&X-Amz-Signature=cddc056e3bcf36f0a642f4a9a14b41c8a44f46acd02ce9458c2308cc441022f8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IE4AEAD%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDiUTqxThFKqwAoMCSdsGBliAAtS1SUTEFNrckfuGdB1gIgZZsnEQTifOdzALJjbkzQXEfcbnr1Nu8xl7NRIEuEwEsqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5B8sY3lnILSAXDMircA97gog35OSbdDRJopl7rbZroIPnjuDan3kz86JFohWpGnoG3DipdUH286ZrzwVE1Q5wC0HBodh7Xv8p8hKDq9ccp8hQPd1AxDOhE%2BN%2FO3vqGMQWHq0yBJLjrTzvK1rhxAVsig8zkspLh56dxXAn0%2BPgFuJBjnI%2FjgOw%2BcliVQ0IXDmmkD3ukCVDo4i4QpAJ9JbLZUthDZ8SD5YKlvTDCfhBFI9C4ce%2FC1aEw0c0HtfPCQFw%2B8tGgDE%2BRE31RFs10EghCw9zeDwMGzLnau%2Bo%2Fppt9g3dymwmZ8PQOspuo2SUA1dC5n9%2FPChXM6WxUXMSy7sL5%2B%2BmgI86PKsx7ffP1z0skxC1kUB6fIMB2YaZzg%2Fc4%2F%2FfuqBVV%2BLWk2xfE4hgmOLlS8wlxzrqadk7WMCXPYzJMHfrfwvvk1NFWWqsfZscIeeu2NkndHjziQ2TnLmCIT9IsY%2BSehisUrprqvptg9FqpvzGQ1ABLk2u6A2ztcIFuwz6UrkL9xoGLRlVChI1Q05Fc4BVJeI6J9Qqnc5vD2w7eLrZjDjV52%2BN1LHeC8tRlIs3yNed76uyqDrJLFXtnBS79McEnJCGIv6txLKAIPwgLHNOaVQ33oj8eSlgH71DqNeJmq8Hz2uJEWYfYMLmOnL0GOqUBMsreZ9eNvuMmLTl2hVat5IY0rwXrKKqTsg8zmwcWILCjhHZxtju6p%2BhlsPh0ijEB4gSXbefLYjFYY%2FpqlbA1DVK%2B4941H%2FMk9HoBpt7lcONHTzWabV5gB1SOdMiICQxUvFfJusXGRf00iDi6VPR4GhfnmhN%2BtYoigy6%2FvbjLbVrJNGHkIJTdP6xcNa6L8yGxBznU%2B%2BEB1QKtcrLJSpwLAzAe8H5N&X-Amz-Signature=4ddb31d52c9fbc908ac5a4f5403a35c63049e5d6037e848f3589226db004d35c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMKAXYLU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIB%2B2bRigQ5bEnxKZGUr0QikjRIbSBs%2FCwRHfMfpddFjcAiAtWR7x3NUeOA5%2FHHxEkZ2GLJYohKS7OCRaWpZzkczfKyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7j8B2NdahVdNAKJfKtwDxtyUUAIYWE9XGGCvhfkft4AsWzRHeq9ffxcAozxVLk4hwM9gT69YG1Hce9Oe5qw%2FMP%2FqrfzR5u9bp0s896UVQX7nVx%2F4RhWd9hbXwC0OhceY%2FBKPWyxek%2FCpLSP%2Fb92msWx79uyYUd06pyhG%2FXNrz4Hx7awsT%2FSy1y7is79b%2Boa%2BFWKVNbfwTbm6c6j3n363CbVZcXydLxSBNO0i5girYx3dcHeokbFNHe8o%2FnmBvZliI%2BQ2HZUCCIcCSEWkBskkkiXv%2FwvqUM8RFNq%2BgOkea%2BaOKQMp0ziv2zB1st4mqGuqMDe%2B5SIPQqQ%2F45LOvVlXIc53PWyO52uz6DjMORmKnkWbfz%2BnQ7ZJLaYQa3CQe7iCb2uAiIc9dNFVA%2FB%2BffdmgBsdRvTn9z9v0zSSP9DQMmApWcphOAAl19UJ3t%2BSvN8Jv5OXVFcSfgxvTADblF235A5VbTrDZjvmDvOIk9n8IQhPsYM2Z5QZHmyIX1DnPTIfVAYue1zqnd%2Bezvlo9jk14V0P3YG4zOjnm0FiH55HKI8EXIsCvvzVXb6a4dmJtiUxzHDG4GcjL06V2fRsArKtEQ7EMV4v8aV9%2Bdi9ONdOCi%2FX%2FEW%2FZRC4x8%2BJptHt3KqL2oPIYk3IXmyEsCEww46cvQY6pgFwv8QC%2BmZAYHJUEWJBFY0CwOyVuKoTIccDVznkY6oBCOt6P2%2FLQ2ZsixfQDfXcNiODhyvbeubmTWDGO1p0Youy6b2%2BF0to9n%2F3Sk8kEhepP0gZdvvYaTT9bviTv%2BiSl6e8gg2oQaomeLKK0f8lw14PYsi3ZKIRvcbvyu11g4mznpdqHL6siZy8iqqOP4SMjKmqteVBPKBZdT0AF0vnztRJ0BtdYlw7&X-Amz-Signature=8043302feb8571979d6e51254493518527f9e552730fdfa7b3446d484cf59ae3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAP26VE4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCv8oq7kIzS0yhEQwfSTU2yzlEMfCXTUnIowecXdFBK5QIhANV7S%2FRPHsz97LkcHJBv%2FuDJC2T8mMdabW%2Bj%2BGRCEdQCKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw3ySx1IU19y9JqZPUq3AMvPzEMeeoFZv86FOS1DBtSB%2FU6U5xk7Z%2BaHFZU9qVb0TSs2NimEMaywgfVi9a5wMdbQtij1KjNhRQfAqELQb87NOeh4gQD6OCGVY58YOEtv0ySbKm79GMNWe3wwWdxoFTeTrrH%2Fb8eg%2FrBErCp57dMkMRc%2FukCreo2JUJVUTqIqRuUZk2xz6IaM85g8QU8ALBg8AQeaD5rsqC%2FKU3iYK3cqKxOE%2Bx8y5Ki9m%2Fw3Wx6x%2FLfBrakcq0KTdKKniYZfxb%2FxfpF52n6SOvkL6mtuW%2FP7xbnLqT2Bz1SzvXA3rfwQ%2B2gGqqEPGhCGucn0cwzr25qgqtr0mtRD9oyQ898ltYiPZr6z%2B%2B%2F9zRGkRXNvgRH8mBdrppbpFwg9niQ83KmY5n%2FbBCJTrlUD1vLMNkv119AwCS%2FohmKMfsQs5QBQD6fXFSkqncfuq4%2Bf6bo%2BhmOCWDB5lXZBHnXePEEQajmI%2BQxGUZ80Pc2q3BdGPKSU5R4%2Fg4iL2dnZ3phqLXI1p0aB7EpltYhXHWNh6Dynhqur5uxNkFlhGrOV7Vxk15rovD4e11xCNPEDEhFqqunODJAb5ZmzuUMRcT42gsKkaM4Q1cknlaC8P%2BCdcEt7XgOtNV7IAE9rOgh7XznjEyOHDDRjpy9BjqkAbpU%2B195jz6Y8bzKTriNMeLzXaiyi%2FkEyT7%2Fon27KZDoApq%2BmhlrsLSNY7mSSH828VVtBcSK7z19%2BWXnB6ooxFoY8QvB0B5vM8v8SPAh%2BuB7Lt2u2LUxW%2BiXuzvEZddDzn9tU2hDane13EvOfq%2Bp5u98Y4kJc30JYT7qQSdq8GrOartksaYHH8s8i7NmD%2FDu8xw%2BF1ICrQnwl%2FhkJe%2FHPLZXR2jr&X-Amz-Signature=3e89829cadcd605ba6ab6e59110aaadcfe859c5d6c12e5f89f2523dc973ccf97&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3N7TVTW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIFHr%2BfZUPZwLv8Yyp%2Fa5vtvA%2Ftdq0EpWxU8LIBk0GLv6AiEAqDGRW%2B3ABT4ugqb0TO3ht325FJslz1po0YXY8jm%2BaboqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIDJepfAZGsrWahJJSrcAz216VKOdCt9T66giRmmAUCBcutW2tbPur%2FGy5%2BYzuwq3OnAScHRc6ZLaPhjY8yrEun2ettiUuV7c3k%2BeApVnSTJ1CBnqJif7z0Vx1tj7Hpo9dDozM8UKAtlzpapLT5HUEvOyYYVpwi4SxUiz06iLbPlK%2FCzOkjMEDiBXDIYpCxGAO9zvL3n9C4BhiCela9RYS%2BexM9GPrN9WKtbVvW5m503sPuOqIQNU9ntvB2VRACvtA9oKXh9avqS%2Bqjk7K%2Fh9jnIfJG8J1gDIK%2B45djftIFHEglPyfeyVaBlAJk0imi2RCyZIDnj9oBxJVvsTN0v7krg3j3CBYtySiDBK%2BDrB%2Bquwfzom8f7V6rjxru2HDKzNn7luKVKWalSo8Ui3l5q%2FBuIEpo90ep5SV5LlE67WKm8cYIctCJsiplJHmmFguogfjKEjapCVGmYfVNF7u%2BXeivI8U3uEBD29lB7ioiVGu4T2L1Ps83Lxj0qqXZ2lxm8gSf%2BlhF6%2FjbSEvOu8TIlMGOk7RVQtf%2B0DocSenFhyo%2Be2%2BYO3K8KLA08BteqazZnUVPfj3Vbwmg7hGsP0sU%2FI4ycht%2BdhPAIBor%2FtpIuwGvyt2f%2FWv%2B%2B9PnPKri7IdqERLnVxopDBrxPT8baMMSOnL0GOqUBduBdZtcD%2FFkD%2BG1wJ67PKGzxw2HQmaYumUgbPIu0WxqUQp5iCMeJrR5s7a11OlcFlLdVbIXqHJ6dxBfoIOZBIWRHZMfBHX2%2Ba7JGldE5ea0hmli1m%2Fx3Dty7d%2FI%2F8hVMQ6SLpKLz87BizSiGdOBWMjAZgZcHoOZ3%2BXVAB7qGoqhwSJ936hxCovhs0T7hyBCJbdqGbGoE67NKt13xI6iPPhXrv8R9&X-Amz-Signature=f5bf23e233165e744397352323f8963adfc724e90bf799ad992a008eb136a8da&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTU65EGS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIBGsLQiZKvD2DnVQ%2BJkv%2FPWQJ%2FuMdXeG5ljW42IXUzH0AiEAh4VztrxmvrhY30tIV%2BCdKAeRyEo5BKJZrVYVnoSjZ4cqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF9%2B6rr0vdxF%2FcItiSrcAxPTqdR%2F%2FTHg22UGRhDCuAoHknOE1o6gDcudC7o45vv0vBVQzO8pysWa6VJgBGhXsyxRBSALNUySvrQA3o1ZMM0TqXc1iFt6vypLeGKP9juk5D3cxaBPt7%2BejEWtxCUxq%2FiLdZoUY7L%2FCF7m8AoPIhn0F4X3n6SLU%2Bo1Wy1W4CkligkLKOlnRskJw776wM8ufkKBsUp3JI3gR1rrZPuCX6T9wqqsfdb18X2tlUXCLI7rdBx9too7RqRLGXs11Y%2F72%2BFUPps2Wd7evB9ll8fVnPApjLBqiq%2BDwuHDM38Fjw93%2Bi7g7V80yromgStGr8YVdlN8azpx4ystpJOkpNp83fiV6%2BJ6Kuhshd70RPl%2Fb6Z9JAz8AFF3%2FaarSRwLlbH2rdH9jtPGGOZv9qzrcYCADbjT%2F2Fu%2BoaqVEM55OZqFKVWuvHYWt4kJL7g51PQ3TE4ufC46wcr25BbZEFTwK7gRLhwpG4GsJWdY%2FxLnHTqqXa6%2BPSu68kM%2FCRPeMx9iADJls9mijixZeJwQ47rCRpFOJn8%2FcWRcMzMOvn3AYROXch0rpxV6vaO1WcPePoMFIXJV%2F7RWrQJDoNOoQtEzmGTbF7gFX2wYYortqyIw2xZPkdLeeySjNKOOasgYiTsMKOOnL0GOqUBPm9RuR1aoQEvqJ0vZce1v%2Fr%2Bhsvkh13e0faApiAR0jfeCbg7NjA4NYNbO9QqfUjtm99FlLefiOqQJkrb4C%2BCgXHhUB9MI76I%2FeoiMjkRjcJuoBo3cVPFRQUVg%2Brlmn4Ifurvl%2F7FItekCHVckQhKL8Eoxd1HAHcZa8ZUV4wYonylP3ng3BNDjCt1gStR8znx1nKL28zWWuOAWMLt77oZI2Y4W59R&X-Amz-Signature=ccd068d15792f1bdc9af8e15dd0c66a9206e0e62e21de02f487c16304cdd137c&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T36QAYEN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIEXQ4rkA2EEVySp2K8RpzPEbrA6UC26%2BSF%2BVJqBEzIi6AiEAlWiORZr6p2VScABXGj4oZx9kFlrZhF%2BOgJqfHX8cAI0qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHMhbaXjZc3B3SHeHSrcA9rCnUbxjE05cLV8r2ATijSV1Px6Jf9wXYzD5GMmdxZ2g1vVt%2B9It9I%2BYnTPK1W3Fk3kv1dCuUArdU8IndcN9xUTg7kBZKTAi%2B1qTUvS5OvOOnZAu%2FHNsfd9FMkpaWS3zELNMO0P0JTQTufzLfyhy08tKW%2FqTs3xISxHRAlDzUOjw9ABtkhoPa45I%2B4c00%2FNa9Inxeu5bgb3LkIRtiuI3rkO76f%2FQoZL5edpVrP9EWDtZBeXaK%2BeHQmMc%2BS7cXEBW3vcYjSGBo8qlfKasEUmymUuNfemiaiSkeIvMgwmQXzfkN85gqr8SBzo2QWgp%2Bd9mY22uhjSNOnE1SVR9OV70NsILVKhgBK0s%2FqqfnDlD4bInvOz36fdPEyDt03Jf8WbSGdDos8k5s5jS9XYupXupdw3V2cmuBhprzebRRtTQU6gNzvl%2FKsPLKAX%2Buh7ng%2FhuTIbLc65rasE0m9KiR0mNwqHdB5pCpd8sKuAHgqHSX54euXCA%2B8%2FKWrAR%2BJR5RyzXZuuyAv38Qep8eSDBM9MWwX6Z1NnL9X%2FWwTduS7T8wM2JD1tsyjXR4TJMPrev%2FI7%2Bt7kWubGH04ZQzHPZqjkB32vvQP2vLPYs9GgBt95Jo3JdRuVG3LJX9iZN2SSMK2OnL0GOqUBtRAVntVMOiuYVsFcKmoWpck%2BN9%2FG9%2BdlnPjcqVFl%2B3%2FaW9izwIl%2Bel2lR8OCSu6iQaLIWtAF%2BtxkFsWHmCsiqmxMchScvQczcRuYLoENvCCpbqt9QeAPidWbVtMUe1z5TaOP10zCA7pFywbgSCNtRVkiLftA3d88g9J4Wzy1Rhhe8RLDKJrXBvli2%2FiQ4sw9l7Jl%2BFxHNsC808tADNKLbbNFRgHR&X-Amz-Signature=b39f7b32bbd66953cddcd366928bb3ad447612cfbb716a903b33bcb708d44782&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAP26VE4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCv8oq7kIzS0yhEQwfSTU2yzlEMfCXTUnIowecXdFBK5QIhANV7S%2FRPHsz97LkcHJBv%2FuDJC2T8mMdabW%2Bj%2BGRCEdQCKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw3ySx1IU19y9JqZPUq3AMvPzEMeeoFZv86FOS1DBtSB%2FU6U5xk7Z%2BaHFZU9qVb0TSs2NimEMaywgfVi9a5wMdbQtij1KjNhRQfAqELQb87NOeh4gQD6OCGVY58YOEtv0ySbKm79GMNWe3wwWdxoFTeTrrH%2Fb8eg%2FrBErCp57dMkMRc%2FukCreo2JUJVUTqIqRuUZk2xz6IaM85g8QU8ALBg8AQeaD5rsqC%2FKU3iYK3cqKxOE%2Bx8y5Ki9m%2Fw3Wx6x%2FLfBrakcq0KTdKKniYZfxb%2FxfpF52n6SOvkL6mtuW%2FP7xbnLqT2Bz1SzvXA3rfwQ%2B2gGqqEPGhCGucn0cwzr25qgqtr0mtRD9oyQ898ltYiPZr6z%2B%2B%2F9zRGkRXNvgRH8mBdrppbpFwg9niQ83KmY5n%2FbBCJTrlUD1vLMNkv119AwCS%2FohmKMfsQs5QBQD6fXFSkqncfuq4%2Bf6bo%2BhmOCWDB5lXZBHnXePEEQajmI%2BQxGUZ80Pc2q3BdGPKSU5R4%2Fg4iL2dnZ3phqLXI1p0aB7EpltYhXHWNh6Dynhqur5uxNkFlhGrOV7Vxk15rovD4e11xCNPEDEhFqqunODJAb5ZmzuUMRcT42gsKkaM4Q1cknlaC8P%2BCdcEt7XgOtNV7IAE9rOgh7XznjEyOHDDRjpy9BjqkAbpU%2B195jz6Y8bzKTriNMeLzXaiyi%2FkEyT7%2Fon27KZDoApq%2BmhlrsLSNY7mSSH828VVtBcSK7z19%2BWXnB6ooxFoY8QvB0B5vM8v8SPAh%2BuB7Lt2u2LUxW%2BiXuzvEZddDzn9tU2hDane13EvOfq%2Bp5u98Y4kJc30JYT7qQSdq8GrOartksaYHH8s8i7NmD%2FDu8xw%2BF1ICrQnwl%2FhkJe%2FHPLZXR2jr&X-Amz-Signature=a3fb15c81265d82589f389f522207fb1e74527a2bb1bfb58419f29d68b488d7c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HRAP2WQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIC%2FYxsKsSTI9EZbd3vcetKJcCsZLC92UQVh9b48Zj3dvAiBOxl62mGqDbkhDc%2BJQOQKvQBNf9U9v9m%2Fn77h0AbPxVyqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFvS8tMpomhTtVAS6KtwDEZtl1Jyi6gNkbceu8ZkniLy9co8%2FQDOChMMKRIGSuxHk322P4xVVmbXmsQ8OcIACHeuknott0N0szAFn3UAb4H0JwmpTEZbTO58eV31OZ2THaHLyqR3Zz2Ohm%2ByPyFgFrFkYdEMNoFP1jP%2BoWrqyR9B3SeDOP6PmcGaELQw9IaJlWqaLR1IMltvupSGz1eP%2FWGCMLNYP0SFsI%2Blw90qDMGdSZVV8hxp%2FpgFULMVnFh%2FVJJ%2F65z4eigstbU8fGx34UukF8aPGCS0441DpNGL4K4XjugibWf5syUMGLu3WANxVLUoVpmtCye%2BnnHsmoZ3sRKmkX6Ojj9W6c%2BVpOCPoKiu4Q4iUMKmzKLZJa%2FUbr11bb%2B5M1zKPDa%2BkTHQ2E4hYCKL%2BeSlF8%2BDdzKRikp9LFvmG4DPJoVRJrStwcE%2F98eanJ%2BHwiQtocP0Kk7IHoNO1Pd6XbXgrnyFhXKzXl8qEY4hDIZBL5cizD9QKnWNI1bfJ6SVNw6SH5gBTnRsVGnyFFNQPc0YYzY368sqk7J960BNs%2FPBPoZzZXHq6l3wfKxHGMgXlonP2eQcZCxcr3ACaLxchxwabFYQtwO4hM781Zlt7St3gXjDDTPT6ezwORsaGFfq8C8wYJotKlUQw1o6cvQY6pgHXKIM6xTvUdBD9lSexsT%2BC9RbQeC9nS4i8Re2GxB5JAOI0AyKInOopzKxQjakrf%2FSSVQrwPf47qKsy431BiehX2iOxb4R7UNSnI4bArmbIcCHWo8CeTt0yfUc27HeLkm%2BOqsYm76%2Bh5siu7xkQrXm6VdQ%2BcdgUcOYbfs9kVZwNZKLZusJwQjQwd2bKhm5PlGGMbk4bt%2ByGu6z0VdP2wJpeiQ2ZugQ7&X-Amz-Signature=9dd6bf387acf32eb6e337ab4fc0230aad74e5a17cf9c063baaae656a4153644f&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HRAP2WQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIC%2FYxsKsSTI9EZbd3vcetKJcCsZLC92UQVh9b48Zj3dvAiBOxl62mGqDbkhDc%2BJQOQKvQBNf9U9v9m%2Fn77h0AbPxVyqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFvS8tMpomhTtVAS6KtwDEZtl1Jyi6gNkbceu8ZkniLy9co8%2FQDOChMMKRIGSuxHk322P4xVVmbXmsQ8OcIACHeuknott0N0szAFn3UAb4H0JwmpTEZbTO58eV31OZ2THaHLyqR3Zz2Ohm%2ByPyFgFrFkYdEMNoFP1jP%2BoWrqyR9B3SeDOP6PmcGaELQw9IaJlWqaLR1IMltvupSGz1eP%2FWGCMLNYP0SFsI%2Blw90qDMGdSZVV8hxp%2FpgFULMVnFh%2FVJJ%2F65z4eigstbU8fGx34UukF8aPGCS0441DpNGL4K4XjugibWf5syUMGLu3WANxVLUoVpmtCye%2BnnHsmoZ3sRKmkX6Ojj9W6c%2BVpOCPoKiu4Q4iUMKmzKLZJa%2FUbr11bb%2B5M1zKPDa%2BkTHQ2E4hYCKL%2BeSlF8%2BDdzKRikp9LFvmG4DPJoVRJrStwcE%2F98eanJ%2BHwiQtocP0Kk7IHoNO1Pd6XbXgrnyFhXKzXl8qEY4hDIZBL5cizD9QKnWNI1bfJ6SVNw6SH5gBTnRsVGnyFFNQPc0YYzY368sqk7J960BNs%2FPBPoZzZXHq6l3wfKxHGMgXlonP2eQcZCxcr3ACaLxchxwabFYQtwO4hM781Zlt7St3gXjDDTPT6ezwORsaGFfq8C8wYJotKlUQw1o6cvQY6pgHXKIM6xTvUdBD9lSexsT%2BC9RbQeC9nS4i8Re2GxB5JAOI0AyKInOopzKxQjakrf%2FSSVQrwPf47qKsy431BiehX2iOxb4R7UNSnI4bArmbIcCHWo8CeTt0yfUc27HeLkm%2BOqsYm76%2Bh5siu7xkQrXm6VdQ%2BcdgUcOYbfs9kVZwNZKLZusJwQjQwd2bKhm5PlGGMbk4bt%2ByGu6z0VdP2wJpeiQ2ZugQ7&X-Amz-Signature=63b6648b8df19be246081fd9069869662ae8ae1a0f37109de8a322ffbef750ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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