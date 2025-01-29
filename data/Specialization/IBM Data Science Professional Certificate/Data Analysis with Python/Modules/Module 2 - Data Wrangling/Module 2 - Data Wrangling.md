

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMPB72UF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYa2jHDunn61ju1lgjWTJrIkZanpor9AbFZ509K2FGhgIhAMQcurBatavvVr7R4E%2FlWrGmnP2yfNSNmBWqxFvTgRmoKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwEJNA6%2BUUFYlaqnrMq3AMay0NJKL%2B5ZggcEEON3LnCeEAsCDP%2BLOGQovVxspk6NtCHfe7Dfmlh8WT400%2F7q3QqmEpsGjsHB5MhfsU9mXWunIpbG%2FzQuJ%2BFaCoi0Lmnx0xMUV55w3mrAnKkN2kZOIYQLqpMU2d539L5Max5blJaSUFE2h4xPo6LUn6ODH42eIuVGDyGW4x%2BSJnrCfP0dmGyMcenqSoPntzat47LFkAFq0rw2y6Eu%2FfRPnDdzjzyc5Cp1a2qKr4w7jm4K0GImCcf6Fc%2BwP9Eic%2BArAvrRqm3xlT7MZdumDcF3tKbB282aeXuVL6336RBtSo%2B66Ql21HT9trvyiyoFClAi1GAC3VW6xUuBj3iMEn3MiwU%2FS%2FPGkgklUzcuJMJ8MholPMEmfD%2Fjsqy01jEVL8LDfRozfay1Hfp%2BZMwIG0A4NbLLilucil2%2B%2Fsx2gvQroumbF04VxZVG7t8tm4PjFIGpn7uGwmcsGwrXYxq8bn7mvWfGMlSV43PxLzq8ioBKvVCdTTd38FHD39cnF2Wvy3gDpoB%2FKMePM0r6sFaJJh1sbU5x8CHHX%2BrqAyeKbVEEUh3PEqsklUW0fL6y6gCVTyAkSZBTGOcXswOmSOy5sw%2BL4GA5mBGFk18mnnbhCBDkVQKWzCkx%2Be8BjqkAR22wAMScAZoxNifEoktn1i2kXiROP1AehzSEGujjZHf6SmnkkkSoHxJZTEuWzAljfja8B%2F4PmarC5qwMPhFxrmDW0fwag4uBMWWfl97%2F4v%2FGzU64lsbgSx1rRsclNcFungQVTdTJfghtMZFew87OTb5R1mSrCJTk6%2F2oL0sOjfvSM%2BCfugdrkQ1zktqcXMl4ui9VZ0PCbZ3M8A4pWcNYyxY%2FQXN&X-Amz-Signature=8279bf9380e47b412be89999064b75cae0d81f51ddbd13132f7f3c2f3f7bc1de&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIHIFONT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD39MnxHE%2FTXuuX1ADZXoTexM2IuNyBBL%2BPS2jaATFlSgIhAMS9CNBAjt3vzfxF8i706pKm9pgA%2FVrqmbUMJ%2B9I30wLKogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyImd2CqirU%2F1L2ev0q3AOFImGZpRrsUNhiLKun75KUFY2xDknY1%2FNoBHdhZb3mB2K54O8IydEltW%2B6v%2FjLAtosVwhmq6r7LTxF06At548wREmTf5YnmiLv7gGiRNK9ztq2MSO545hb0j2hkNaTBLYnalexob4Rh8GPJ7Sfyqfts5TPnwNi0E%2FZzN2S2vCW38yjBSKkP6%2BD3uZoRBbms6IJGjEh%2Bu%2BxGm5qQ6g2DgI7vQkgtAGkMaEPUuwcr9UQyyiPGV9%2BuirZhYdL5Uo4airwjMbwEpnhPqJzBG3AOtj5n0dX7w3D6O%2FK1JEkgTExoc093%2BjtPQ2O8oEUhK%2BSdFZy98oFdnR0%2FA%2FJH5PxTf%2Bk%2BsZIjyNrzyilgsCr3bRfgrN800xdE%2FW3yNIUAd%2FYAly%2FaEsTwjO0fg6gCb%2Fd%2FuJXjgINMa%2BPVnPpakdUS67msUyC4c%2BoJfdUP%2BTAfl9V%2FN3AaJ67hB6fVbxROgSbOlcaqEJXmO9B1yHCGYJyi2X0hms3BB64dYdLPdLy2A3NpOTuuCqmiiEmYjkjHtZu8SGTm5QaiPLfbXj9lGT1ElPyHlFNx9DdYJ876okJHTDcg%2B3jjXiYpNAgBDDujog8EUh7HpwlPOLdZYGLPvkGMeVkcmK3Im7BR0VXP4IVkDCyree8BjqkAXlGVRAo2f%2BR251oOx6zAf2Xl62hiPlfqxDFeVC31uvBOwKWu5dbkA2Ef7a%2FGq44u3WqVkleb3CoXlXdV5CdweMseXz3c8Kp9ytz%2FiU7ZhHKAZqfGMpbjyTzPT8ObN9TWsaGC3kATdWnHcQ5un8zsAj3Dqd44%2BkY0P79X8X5xMaLdTX3KMcrU2KN2jjhPOAD%2Bzd1ZnqVnOOmXtY7uc4xd6uYsPQ9&X-Amz-Signature=bd55cb36045893e50b4e6acbc63c2292dd31e20886b46062c74024a2ca9d051e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2MW4AQC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEaR7tlwKR9dhjNNT9y%2FvIQQMcWhGmhuwVKkNqJmwV%2FMAiEAwn902%2BLr5QoxyFdA%2BQYAzbv1aGhe96Zfr5GZLPc3mEMqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK8ZR3zU7MdREKiS8yrcA%2FgEvjkpViM0%2BTpD8T7q9BCWEieMUIkc2KfpbkABwDbn8sl9naGv2d7uj1kFUYxcFLm%2FmfCQQnPExelinDs4eGxOGgpDQhbn9A%2F%2BYWngRMMzNcrRrLjA%2BVBW2ntXx%2FsnP9pjHFP4ag27%2FrQjFM6HJTLXzUhQVNsMhyAl0FfewXd214DFbrTTjAisq8fuBr5CEVU7rUnFd1A%2BtiIh9S7UX0k8FTro9vgJloq37G52KX6IoODHQEkUQzZmANvz7LsHRbQsIDr5CFuGhWQCV9%2FBxYRMNEnQ4JU8F8IIYs8b%2BVxx4CK8PuWkz6ECZJDclmAyV85%2B06uFL55O%2B57iVNOYaLkOBeQSCugahiavi5Crg65hs%2FmVUJOtvlKM61NWg2qL9iGvYGA0Ilv3THxO15ZLOR4rWX0yzKSTW4S2tLWvits7j98QmK9TQbRyGAk7DwhiL5jRaT2zK5II2cS6hCjwOtUlRBQ8IL2G6RZ%2Fw6rNfn7WZeS78x0f5VcMdqcALJzqLhEOwHWKkuTT1WV7%2BovXeB4M%2B8V5J2aUSVVIwYmQ8saZSbnMBUUFdFu8nrBLUOL5meGmcwOt%2BXXiuRMs9ghMM2A3rKjrkchCIwpCN0K9JBn%2BNUu6o8Z0vvqhSLSBMPXH57wGOqUB9Qag8S5dxv1GEJ9Aif6og6l1bLN5XG8a%2F2aishyNEYhxSu2xT0Akycjr39bpJft%2BQwbrZMnMEfrq2nJHF7xkX4xnXYxEDI3a%2F4QzvugV92TnFWScyvf6uyof93TcZratm%2Fo%2FHL%2BS0lSPZXjqynhcKEOcifp2mLUn%2BQ%2FBjm5iKvSV5dtBncfOpMhEyyCD7sij214rKq%2BiG2oSez7A4fUKDcN4Bsei&X-Amz-Signature=67d4e92d18d11bb3453537116c755f74f329873ce73c1d17c5d2588269d9b188&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCMNAN5L%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqee5V72YrzOljJ7cmSPeM1tTEBGxy2Bbkd1p0AvhgYAIhAKcMC6KRQHoluExYSk1%2FLBZrEy5b1XGHgr7l%2BiqFwfONKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbZ8WvCNBqEH1a504q3AMSiYrvyqSDgeaRQX950JsncWHpDEikiFUapkirYElXU6ZU1PqkJQS7OCXpeFAXi%2FznkWi%2FKEns39w4NcUSPYX0QSNSr30TYiEi%2F9ZtebH5qYTv451xvvRnRIRjMEeNMbIHWVD7kxerqJEYEO2BtCMnulzcyY50xavX8ES3%2FZOPdLmtUkHCHhdPg4EdoVMR1iapGScFe5ieT7Bg%2BCXtRdSxV9IhtgUYuMXEL9DZ3uM4eccmGCBqzhO1GmqNrCkcc%2BymYjcNpjD7pAXsnLCNnWsdMQ9vkgvbVhyubXHKXDF8nVl%2FSRzgeNqSlWjEtZQ9kf2%2BvnESewnp03pxM7gIm8ZlDwa24YPNgHL5vvQ3AtmIR0heugnmGNOIYhb%2FZVXrNlkqyDq%2FqAF2KQfWTPzVT3Aky2owDpeBZRgBepVAGXkFhfPwUyBdd1d9HGtcsaV7RbTJXCrjMhZDnPqPaHA2xcLo%2B8UMSaGMJCBmMqXIYIzP963FE9Wd%2BetySy%2FBjPEVHKwkIFUao7JXEj2Xn1s%2F65kWW7TPTsdwMp88t%2FeqBcGM9pCRsz4Eyel5PoluKfU1W%2B9sIRsaioooQEJVUzlIM3%2F%2FpzNLZHa%2BCHvbFEZkFBYXZHQXg1CN1Ytl%2FsfVVDDNx%2Be8BjqkAVEFSmWBxBiJVVuAY5FYDe%2Fs49mYj95fupIH8JVc6nTTlShS8Y42GsY0tWhyksZaA6xj1jiOKCdXK%2B%2BLbKIwMcGhlky1So4Cc3AuNTHLMOiLtPr0A6dvEnH7eyT59yptWGvrxshLk%2Fsdo%2Fd5k5z2wUWOD81aWC3KhtXGdSOTCI%2FyaIT%2FME%2BaxSnv8ddpC3vGLcniWwQkwMWVjZ%2FFvAaUHNJL36xo&X-Amz-Signature=af8f57abe7936602e871fcfa6410fd505be9b0f4bcbf169b90200cc8a7b6c9d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBLFN5QH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQboEOIGel1nY9dsOc91qDtXJ22stOhEREe%2F6Fv6diHAiALUTmabRdZqt4GMYpPAhiRJPA0eGnWOYJLzN2pH6WskCqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvWofhOJJ%2BS5k%2BdPvKtwDezLhKNdSH42h%2Fx4S42UjFxNRpnAilYLQJXaOGilYM3EpYgn%2B8XaE9AmMMhRrGbi9YJn1RJp4YdD5zDjqsEV3uLpQ5%2FC3mRZZ03Fep%2B0vsX4jsd8%2FzMJIGEwsq0XBClGNgOAgr18d8r4HnVXUCglx2%2F%2BL1v%2B9jSAiJni3U7%2B8czDg1Tc7E6nOljVssyiXDX24b6nvX1J4rCl%2BjX%2BMQWJkrRvMKX7X8XDmhcp5eLUp5wkvSBtQQcuaWWPda2BAkfJlmZom%2F5uuQuyY6GwZAVdS93eXZ%2BxfRdqy0wtOu0I4Ev3yOTzR8i%2BsjPJ9sVa5zJjD9gqpMQYkymfG011GPHJmDdkcQJwOn%2FU2mqzswtTjvG2f89zIuz9YmHhrx8Zqk8B1Uff83j7CDZ6IP2ODEfHXwl7TWUiyQqMWdPUWOH6MqzdNYMoqAJiIvwMrraRamSwJuHU0S70Cw%2FIN4Dx1xY17%2FeDrwXz%2FEXHfHDh8pMcT7VwJGEBMQiEL0gPOFHH4%2F2E3k0f5rXG2nnTE00qc5Wk0UHYnkTW3AyGrFMGb21N27k3W%2F%2BzxBCBpxPZ%2BLyUvk4d7fk9ZgkocOtd7b8YArQ%2FsE6y1KRnEhwqMtQYzRB6huvk3jGpVdELVg5YMFO4w463nvAY6pgGvMY%2F28MYfbZrC7cxI%2F1HkhcEcvfa4ODwLP8n%2B53D9GUvJhE0eTrHU%2FHCc4DGI0EIpxIlLujzszfp76kBqKUdrACP1uEksWkLwJemV0z6caFn7S9Azh%2BoADwWOyBLlbtMfoGjGX1FL0eab7a%2BBvHPrKMHxwLRWkIOo8JBt6ylO51zd8L1vTOqKnSKoZVb%2BJwN65YN%2Fdo%2BzMjskqln%2BrhZXwd4AjSma&X-Amz-Signature=e9517de6125b91b50318e09e34961c9b60f798ad057ffa55d6cb5a0915e58b88&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HI4OVF3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfs6s%2FTHuRTZSrUM%2BwO%2BTkXjSpFCoiaBDLfOWa%2BU6Y4gIhAN8XYcZx8KO%2F%2Bqc8guumdEwMuUtOLNMj%2BMDnD88b%2BIl0KogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgznJiDpbpYxFlNimdgq3AO4%2F6DkjdHWreT02ncQ4Ni%2B2ds5%2B8laSIX149HMYPcrf5Jf92ilGUailPGhph1kvKZHANGsbq6ihVla7J7QIYPPVTZOl%2BclMVeuwWYW8HDrO7IqHB2mht%2BhU3SLPHJX0K40HV2fsoI%2FhDFOgcgFkUuTau%2BJsiuSBAitR%2B4EC1pB%2BpZxqUuA4GSidOPgKh0pxj%2F94VHXRy2FPTPlsNncw8Fgz%2BBNeFtXQxrEp8SHV83S1t2hWgdhrUfyIbphu%2F2XPbufA4oaWxWmC7BoC9iWUJGylu163950EL2PLMoKTzp1tgvqfp2%2BmMcBbABLocL9I%2FVzHTkGc0FSRRFooTuyK8OFzbuyPtAa6zm203n4FbjCMF73zWyvFuHBkL204iiTJkGCL9bYVXKSXMPSZYcp2LKZtRo9h321FV6e1JfWHhyBRINrc6FcvER8v4B0Ib3eEREqQ9OJXQQWp%2Fn2Cx3du1G7ua2HRczjczT2VT3o4piMFNlz1uQKk9pbYTOw7rQzdmnVs%2F2amVSLUuTT7LkGps%2B4OOZHiIG%2BDJF%2FnUfmEp1bqpXppCe3vBLuIRnaAeFDYkYcD6W9fyrsBFkj0LJWs2k1MSh5%2BlwCAeT38A2rkg%2B0wMRgtrPptM3PF4VnhzDNree8BjqkAbC3O1zot%2BoX715%2BdfHEQOJddlwnuLhfZ%2BqLCzz7Epq9Bfq8FyfGX%2BthdfgQnIGHs%2FnG4HRKP1vvZPUp13l1yvHnPK2oqQgeXQZe7ugeFcn6pUziWJKTwedeyPOcefajvUi2mscOhfx2CbO2ohC2RlSxRvdrT9FOUjPRWBvfFsLvxjdGKY%2BQPqlnXasYz2GBnaFhPEUmp2lgPGU7qTSDSd1x9UCV&X-Amz-Signature=d80d77618108dc34306e19237612b6d5af3b76f6f6a537fc821eb7aed15a4082&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664X5IUFLO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID7gROhGF1JGtyfHksDf1Ozj9%2FM4YRjPVPPXxhPutBxPAiAb0cDHDjFWwvhlYfIDs%2B3C8s1Wpa%2BH8b5XN2fa0gttnCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXsNoVsQ3eo1kQR0IKtwDaNG0PTcbJrOeYx0z09mEjEHn7MB4Lrqm0haZtwCeiwrLw7bDx8a2BCbzB%2FiPtWrjxubsPHHyWUlT%2BpWmhuHs4bEXHArOLLVAf2kOp1E55UiJwOIz5Wan2yaKOU4jETnt1XPdCt2KI6gGbtGzWjcRk84QCQp5q4zTV%2FOuyVobyM0b1%2BLAqC%2FJqoM4rKLpndW5u5JQmee3gobiQePv3AWlWNYj%2Bv615KkKGIUva%2BwDdjle9c4QWLlFs4Wy%2F%2FIlvzxAzEwoTcw2jIX8%2F4%2FX2z0uV1EEVYVX4EeREfpSJDOmzJHpO5Zuf74zKwfZ9npz%2FLIa7WGm7sQCtovBkCs22qIue%2FNQ%2BXGqvsUCUlfQ3bej1PIjZ9hst5mbYrVzMuM3FsBOtSqPCFODpGY97STB%2FTJnuX4w%2BreGA0XPgWAbAOKvufQ5DUf5tYelbD3KtL%2Bg5jmS2dMekL0UVZOw8WXzNuKjQcstrGKOwGyIwI1clrE6fCXEnDTffgIIOfM2HxxM%2Barhftimxl6OUXJv6hQJ8%2F3BDMzTcAhx2FIzNCuUDTwTFkMYA%2FV38NAbEOSusCdN3sr5g14XUWVwU61ha%2F4MkM9oOaxORvSNsGQT9CFj%2BFVOMlOrpo4DEQ%2Bss6ietXYwm8fnvAY6pgF0FfJ5IeueNp%2BufC30Y0XQUCShyGwVlN%2BK7zVUB8oJp5ATGdbrn7ZpWMNkQ%2FZLRPfTqxY6sEPirhfd1v5FLi%2BZI0ADx6Bum27Ib%2BEQhW5qKfsyd6H5vrefq0%2BJsGgN5rg0X7aVA%2BPKlW8jiH7sekXjt%2BEEe%2BiVKeqkbpt6cYXpEUnl%2FT0AgRIPKnpvESmUX3urv8Lc0eRvTNl%2FDc%2FB5Ck%2F4h1rm47l&X-Amz-Signature=d3f9c1ec07dd130fcb8d38d1af10b88b5f1dde09b177f9f13cf1149eefdb0c54&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673YPP2BX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEFTclHrqzRnQpY1zlABo256nObwiy%2FQsTZIUgUAxWy0AiB2u8pVVYLJ%2BlgnkTt76uBwlAHHhb3%2FjQk7qzJ8wh%2BLjyqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQpHeeerqvr6xYeVvKtwDB4nQo3ZfGCHcq06GyIiLPRv%2BxzLSwhSPusAe%2BCKoz2vZyGR7zorpLaEyXQirdJTsVf4jDHo9E30gqOqQREv%2Fd7zyhjREtx64HKHPYuDXP%2BhDO7a8ZHrrac98bUjf6OMlB3S80UGlGMNoSpk61FUIydJLXLv4lk9IIHoqzn9XPWy6kCS3RbdX7Lxx0QyEa%2BD4Q0F9e3B335JvlS9hRxWx4%2BMNr6vMwCUfmckZwXfQ9WlE5iYbqSVE0wv7eWAlEMQ7BsqAfR4cnI7Eif85%2FfojVCuK3YNCdtV%2B5f2uiymTMirnVdnM5yqoEyS2U3zGgfGaoU4fMGYl0A%2BhNT%2F2ZB2%2FuFwN3rVON%2BeujcZDogrqYBSUydxAYkXNLWLOM4VURYC8llWUHL%2BkMQNwku49HTiv19%2FvecZz8tigf%2Fn4GREMThIjyiATg1%2FU609ike7s72pD3%2FQQ1v%2BUNB6LO6GJl89PCemcPKo7thVJ16cfFA6j82KPanBhRhUClv%2B4r4eNw897a%2B7jzsthuhkfWXVKoZpTQSA9%2FW8LhjQtgEDlbtXKIkpjaBWQFQa8VdEZ3TNRM5ehfX7akanKwCcDPRcVAxmyHyy9wdu97xKaveO%2BiqqRmd02RJMEeKieWjrYRFkwja7nvAY6pgGNPEF2uS%2Fy7dms0HslrfcjJ5LlAdZIkScMyR%2FTClTYv7EAzSb%2BMzmrqk5EWQesaZuZrm2Ahs5gY5MrU7Wa9FS1rjI2mMYljoh4p22bDiRn8Cm2Dl8ZItnqNNU%2BmAz%2F3au0PclmcK4TRRQGqg%2B987YZ3L8HR%2FnEhPFYMRCcDd0cDT4z4YisipTDDDAF5%2BXwsmGgtqT9FdECYr%2FLmhlsX3QhK0sr%2F%2Bfv&X-Amz-Signature=80e7812c73f30daf1e5af3465f3352718021ebf10dcb57bdcaf952ccf87bc94f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBLFN5QH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQboEOIGel1nY9dsOc91qDtXJ22stOhEREe%2F6Fv6diHAiALUTmabRdZqt4GMYpPAhiRJPA0eGnWOYJLzN2pH6WskCqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvWofhOJJ%2BS5k%2BdPvKtwDezLhKNdSH42h%2Fx4S42UjFxNRpnAilYLQJXaOGilYM3EpYgn%2B8XaE9AmMMhRrGbi9YJn1RJp4YdD5zDjqsEV3uLpQ5%2FC3mRZZ03Fep%2B0vsX4jsd8%2FzMJIGEwsq0XBClGNgOAgr18d8r4HnVXUCglx2%2F%2BL1v%2B9jSAiJni3U7%2B8czDg1Tc7E6nOljVssyiXDX24b6nvX1J4rCl%2BjX%2BMQWJkrRvMKX7X8XDmhcp5eLUp5wkvSBtQQcuaWWPda2BAkfJlmZom%2F5uuQuyY6GwZAVdS93eXZ%2BxfRdqy0wtOu0I4Ev3yOTzR8i%2BsjPJ9sVa5zJjD9gqpMQYkymfG011GPHJmDdkcQJwOn%2FU2mqzswtTjvG2f89zIuz9YmHhrx8Zqk8B1Uff83j7CDZ6IP2ODEfHXwl7TWUiyQqMWdPUWOH6MqzdNYMoqAJiIvwMrraRamSwJuHU0S70Cw%2FIN4Dx1xY17%2FeDrwXz%2FEXHfHDh8pMcT7VwJGEBMQiEL0gPOFHH4%2F2E3k0f5rXG2nnTE00qc5Wk0UHYnkTW3AyGrFMGb21N27k3W%2F%2BzxBCBpxPZ%2BLyUvk4d7fk9ZgkocOtd7b8YArQ%2FsE6y1KRnEhwqMtQYzRB6huvk3jGpVdELVg5YMFO4w463nvAY6pgGvMY%2F28MYfbZrC7cxI%2F1HkhcEcvfa4ODwLP8n%2B53D9GUvJhE0eTrHU%2FHCc4DGI0EIpxIlLujzszfp76kBqKUdrACP1uEksWkLwJemV0z6caFn7S9Azh%2BoADwWOyBLlbtMfoGjGX1FL0eab7a%2BBvHPrKMHxwLRWkIOo8JBt6ylO51zd8L1vTOqKnSKoZVb%2BJwN65YN%2Fdo%2BzMjskqln%2BrhZXwd4AjSma&X-Amz-Signature=e7737cf7f8a464d1a473d5a734cddbfc0a7d06bfb14a0d912e11befcc78a2fe6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJ6Z2WZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkztH95laNxQG0H0OCxde5Ay2zwNZXoDwQQ2LmrB2pgAiEA20%2BtroqAN8lm30DfWbth%2Be6GoEsbReom0EQJdaReV5sqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2BUQcStanL343F33yrcA5FoA2WRKzK4R9mt9lYqmkQJb9FlxoeS2zZ9%2FC193vaNbTL0%2BEr6m1Q8iunR%2F3TBIBPFSqr4iFaWluIZssals5p%2BH718XVcZtHcpFzk5%2FQqJGArnQrSwoY0mv11qgjZRtp2ES2f1Hfk2PrSO%2BsFQF8DDLunl00aIjmDzEwNFg8to%2FaU06pSG2JEdPBJZiLitC%2B%2BTUi3gA6sthOmf0mRzoD50a5J%2B4KbQzPYmg%2FCNNIu9mYol4CjBYX9FYwEwSfkIIRPxL1uXX2ZGrM9A5onFGX1PXf7IE6NAg2HA0gXqdjlfz9avS1ErRuepsIi0ZFv48QDVx10WfgXeqaOp7m8Ekjtdfiz5u8E78twgEvBrd1KqSg6lEgZ59OJJuLg0FhL9NaiSQBR0RchLsZg49gnNggiF8ETX9GXr%2F5LBZFG8xeP7uWqO4wEH1cpwf9PzgFvf4oE1khqQu6R9A3657%2F%2BaP6cA40BPH%2B8Xm4sHft2N04wnKu33YqpZ5hCkXi0hiiuSaJTjWEe3gldAaQz2HAltRzayAVeCVNukjLaQ8cqNh5Fc%2F3X7pYAHR5BM8B7SzIpMh88RbIdg17zk%2FdUvdQ5TgT%2BFoMbkUT3fyVi9o3FVpCrf8M4H3GuCALCT6pwaMMDH57wGOqUBZt1aEiTwiAx4X%2FV%2BnZ7VvgNQAPGLjZt1aXcKm5yl2DCvd7G%2FdQ9L9EbxnWXR5Yn8N1MQWuGEMqFP14puDtUGRN287haYXvqbzeHk2VYTVO0a7cqH068%2BPL6bfrWIiL53uglwx00AqyzE3X0FpEGwCZzcpTiK9CH7cUZFPekcj84ED1DfxYzlINVl4IP%2FEORdqsip15McU64p3bCqFeiTX2bnO6Nv&X-Amz-Signature=7d5320d57236ebd5b1f879b8459604dc6cd59a9431031df4f9a784c06e8ba95c&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJ6Z2WZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkztH95laNxQG0H0OCxde5Ay2zwNZXoDwQQ2LmrB2pgAiEA20%2BtroqAN8lm30DfWbth%2Be6GoEsbReom0EQJdaReV5sqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2BUQcStanL343F33yrcA5FoA2WRKzK4R9mt9lYqmkQJb9FlxoeS2zZ9%2FC193vaNbTL0%2BEr6m1Q8iunR%2F3TBIBPFSqr4iFaWluIZssals5p%2BH718XVcZtHcpFzk5%2FQqJGArnQrSwoY0mv11qgjZRtp2ES2f1Hfk2PrSO%2BsFQF8DDLunl00aIjmDzEwNFg8to%2FaU06pSG2JEdPBJZiLitC%2B%2BTUi3gA6sthOmf0mRzoD50a5J%2B4KbQzPYmg%2FCNNIu9mYol4CjBYX9FYwEwSfkIIRPxL1uXX2ZGrM9A5onFGX1PXf7IE6NAg2HA0gXqdjlfz9avS1ErRuepsIi0ZFv48QDVx10WfgXeqaOp7m8Ekjtdfiz5u8E78twgEvBrd1KqSg6lEgZ59OJJuLg0FhL9NaiSQBR0RchLsZg49gnNggiF8ETX9GXr%2F5LBZFG8xeP7uWqO4wEH1cpwf9PzgFvf4oE1khqQu6R9A3657%2F%2BaP6cA40BPH%2B8Xm4sHft2N04wnKu33YqpZ5hCkXi0hiiuSaJTjWEe3gldAaQz2HAltRzayAVeCVNukjLaQ8cqNh5Fc%2F3X7pYAHR5BM8B7SzIpMh88RbIdg17zk%2FdUvdQ5TgT%2BFoMbkUT3fyVi9o3FVpCrf8M4H3GuCALCT6pwaMMDH57wGOqUBZt1aEiTwiAx4X%2FV%2BnZ7VvgNQAPGLjZt1aXcKm5yl2DCvd7G%2FdQ9L9EbxnWXR5Yn8N1MQWuGEMqFP14puDtUGRN287haYXvqbzeHk2VYTVO0a7cqH068%2BPL6bfrWIiL53uglwx00AqyzE3X0FpEGwCZzcpTiK9CH7cUZFPekcj84ED1DfxYzlINVl4IP%2FEORdqsip15McU64p3bCqFeiTX2bnO6Nv&X-Amz-Signature=a5720e34fd0b24ba2f50b88585e8ae36b1df58d8d7f3e580ccce1d024a087fa1&X-Amz-SignedHeaders=host&x-id=GetObject)
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