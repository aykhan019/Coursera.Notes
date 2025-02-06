

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AAIMEQU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFTm3A2kAxCBXymrIz9l0Nx%2BMa%2FRGtrnSTYEMBlknyuMAiBMjvmIdaZnWUFf%2FZ%2F025YTCEUsqroTjr%2F%2B7ixK1BUrLyr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMkmiYWCjJkjMOPabgKtwDw1c%2FF8r1uwgzlYwlVyJl%2F2CgjqPOonWYkYsWM%2BAPdjhRmk9rrRioiV5lN0hgw2NX%2BIs4LtEeZQeXbwWzqN01eLtA7yTLc%2FkneQuNN2zb0lsYIalg50T3Xbd8Foq2NaQipc8F%2BtZOr9YHdP0Pv4nayQll44%2FevCK13jFs6MG11d1hNtxsPigRqmp6epfM907FMFMOVCNUIWuF5hj%2BZ0iih4EdfTVoDbaP2t73rXCVgoF3kdZZDHg17Nv93L%2B1KDmv2EUe0veT0FEgid8pmiEhhkc5IPuG24VF9zLzrtdhpYeBl2o%2F3VaNDkeSRbQvhpv%2Bu5NLOYjbbENV9Rvv2ySIC5UigEK1AM5uGbrZpL5quCcG2ECjOyNXI6hHPMjx%2FhVQ68B3OHwsZD1F8i5IdM6mrRshwOy%2Bg2a0wmUg4b7HHXJthke4GmYFI4nlGQEiy%2FDpBsjWrsfM2Y7rTnFnXN9gr2CS0NOsOU9QsOqRW9kLsntYayrsphChlx0ZBRDrs2AtojiegLvbPGi9g7iWkhclp1o%2FjrgjIdJQ8r9oJZ3JoAwc3Gy9VnSWOezUn7sZ6nCJNhGqtjA8Nih5SdOSI0b2g5%2FpJZ7X6e58GmGocBJv0X8MUQueHY1TcxUEe2kwk%2FyQvQY6pgF56Yt3rz0aRswfDHaiw14A3bI74Was9CXJnFi%2BTj5MawBx7imOQYzVLwJu5OtNt7rHiP1H18EqeXRpMfXGnSfxtaFXejnYaoTxia30FztmDlgQKMvk02fOQZYdX%2BeivnEH2At1PvWFjsKMSlWKkWFFQkSbgHyrxNkubpKIEE75%2FkN%2BAEXcD05ixdWGGMX%2BCYSgGlpKE2DaYDnIu9RENuM6y9iO%2BNa5&X-Amz-Signature=4641c67f99b1d4b403adb24a5896ea6a9ec508c958d42df738ea337006bb3927&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZCF6O2I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIBjdohnfdovQcrhLE2wPMpOmt0Y85qKRc%2F2rfYyw13gtAiEAhrNW7z4MfY%2FR1KTo5LNAIcKkACoM1BBIjihsFjFAjdsq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDOEg%2Bb8h7qCu560JbSrcAxwSq%2FBBWoBb%2Bubn4%2FsSk3zA3CNXh1XG%2BLbOU7KVD9WxQ5AAdUH1wLLhxGQnvkDIccTXRgn4wBzXr0vk9hkh8L1%2FDPM5HtwNJVJDI39efnIG4Ua%2BkmRQUSdiyOpkTlu%2BXP6tarKyp4liFOil63j%2F9O0nh3Onb3LBX9eLwOCOsjdMnn3RsGClb8DNJiGyrsp0bX%2BaNgCvs40JgtGgPzSeIDX5m4gLXsk%2FN8tnzjIcx7Livxu%2BpsRQxylLjFXqf8iFcm%2BueAPOeC3WJcivJrhA9v41vPQBBnQDYugyb8voFRlyP99fvyt386Ck96H6qpkeIB%2F7alpLsVrIQtXDB98U%2FW2Puye%2FR4PcSOr7OaOO0m%2B9Xi5lzXi7Y0SHbowzaqsxP8kcMMTAmEQ9ZCF0iOqwtMVErKEW6orrc3d6iZaQPkBKMK7c4VbINyc4xTzvGUWs6caBD8%2ByDO1e7n7SiGiAo6q7Yxi%2FEVfs6hBQgk5N%2FlWb8f%2BxZLSOkyqRBg3i5nRbWMycHv7m3q%2BJxWCa3xT9JN8ujgSKW5SFX95ZFhyYU37sMQz2NrmEF%2Bd%2BX2YUg3QuLGyIZvOMB1fLprp6DezFeoMiOrbJ%2FqRd2ctRZirFpdFjKJxWY9zD324EUkS3MND7kL0GOqUBfhyzPZRO%2F4NaMSp04EvqOWgw0FD2ilnKI5VmY2%2B4b3QO4yP4IdABoNFjVf1XZIqaB6CZMyINgI6kKRW20%2Fdgy70BVHIU7m02tTRG9%2FiyvQVr0VFh6%2B6pbvt%2B1mETu21jRdQNQ9WU72sm6QkoqB88%2B81Z%2BefMG7SCrmq1XNooMGPpOxYSA1tLqlu8BCi8JKp6QuWbJd93Fm1t5cF%2FSymi4kxWsO0l&X-Amz-Signature=64ae527974d699be545869f02e82751df2ebcfaf02c8c90640af4df9927e8163&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3EYUFKU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIAgy7d%2FLIa1LFEvLzpdWO7Khi%2Fwqv9uyUU2TxCGvC9JcAiA1z7UoXflJJe7fNLfxUdkerwqiyoKC5mOJLVZZFWYNvir%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMfSn67fa9y3kQviVDKtwDIz7jLHlQh42teRJQ6x72RsxoKOwNMolCvHsIuJPdmPOcpvVxGwXE4tDJMx2dpODF8NNAAYrFeHW2pAraPStZ2GbFlS0hlEogyGWBqnlU79%2FFS%2Bt4Ubn0qsS2UpPczNMBB7r%2BFwH0nukoK7DNbffgxgbKaBexBzQ9qCNhtLS5YCJDmp%2BXwIMsypq9y5LXvNTFRMtqwXdsO8PZOG4tAC6rxMMKYl40gXo3CbJOAWK35aJPMxcULqoq%2BNcaHUSBDzsotAl2q8h5Zdkn5zzJ1J0itfCvcKn9DnKa2ifnir%2B7Rl6fXq6HDGgm58xgWPPTX4QASqBLaKIJg0itFC0niieIp4rBYYjQrgIE3CgQhMxNtGo6bcY%2BIAvM6Kx8%2F1LgHCY%2F2QAuh5tyoYS%2Fv%2FAJwUwb5UBQb6ML4RWEymkzaN0IN5HxmHFuAUeYIhWNHrUOe4hNbTE411c%2FJrwDFh6TAaXweYSkTQFUQ6DUcB9Nkh6Uylig85IjL9dEScjxtfkHbLWjF6jjjEGSQtnFJCOa49WbK59t0ld9aeCwz%2BBBd19tqJJbF3lklgTvNFcgKXPVzFiRHAw3AGXClruNEu%2BsMRI2sGFXczL8pwnLZRBDvtv7irNRvBvDJtJt9zN2kHowk%2FyQvQY6pgHQd4ak0kQnuFE5ZsDeDTCfkWKX6%2BUG1ZfIhURGWbUjYwNjT%2FtULlLXpcSnn%2B9%2Fec1GWqLY48THDNgo40pfd4B92MMl8J8yf5EE8yyOKL8VTzEwGyD9ZhBfHVp5g%2Fda2RRRHj6%2Bq1wq2PS5fPqh9iWeBXVO5m5gNp04KpRlvlkwhW8v5hSKDEGiclTdEpdeoPt%2FUQMfs%2FfZGvwozsQpT6WGzUoIJUv6&X-Amz-Signature=b362312519099e19b74cae5f11011abfa2fad0ddeb7a3ed2906c87df1769686a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSNI5EKG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQDWCcrclzf4ljM1S654jQtEk15bJYa%2FzhyQsF97Y35qXgIhAJYtnXULY5ELiDpHgpJhG%2FTNGrc%2FbxjiMeXTv9nd0AOQKv8DCFYQABoMNjM3NDIzMTgzODA1IgxSkDvEEOdN8TQq94Uq3AOWVWCTjmwcFw9P62clagGbkNGJBrXTg0KgjSf3AmjqyRtAI5IX%2B%2FDMRCWjq8%2BxiZYumkWnwtPY3Hg1sFV9gEDcuhimFNkqg62scdupEXQyHTR1s1lhw9XV7%2BYWyV6tg6h4Zh8wZexieeEnxreGEyNvm1eNX6psxtdSRkNgtRRl0bf6itUjIvmZzd1Km7DRfFpHU94DTW4bsz%2FIIAAw2AD0lsX85kjY1VXududZ1mHxohO9hd5vBS0l268fmQf1HmwQdv8lZfm5U4PEKflYV9NeV1maPcY9%2F9cWQRwdwkHEoa4z3M8%2FXd98Lscjga%2FgEecQQPw%2FK3cy1pVR7Y3LKvlzCtm2NAlg8xoSa%2BTGxWK9lIbF1b3fxcH7EAkOnKlmYO1jdyoey%2B%2FjJm54UiGaMyYneYZTxjsH0UH2SUfoEodfV1GjwdqMnTUugTvuVU5kXyvKTEPXV3Kj0kNmm5TDcpW2DlsEnaPMgagfpwZTdySzNPz09bPrMOoCOppmkffBpcC8yXKyCl6coHmHct4azFGPLJq13ZK%2Bj9etM2g8mCGf9Rmx31vh6fFp2aRJQspOjRUTomh67pK9wQo9uGgDj%2FA9m7RJNb4CttiOHlSLdzWTmfbskchWNZ4q01F%2F4zDZ%2B5C9BjqkAQX2TLyIghqR06bVemdzENKk7h9Tj2IOvDqexG%2FLnlV9EL5IMQ042138CcrnDeJHlkOY6CWkIOTgvR9Yvk4EduLp%2FymPqmOe0X91Jt3mXy7TkBC3OGmk4N4dkmrahc3sVTeOU1TWDOnjki0Y9NjvEB9NiXuGFjor1%2F40yOpcql8fRWJ9eVcS4o%2BhcTQ%2BKUwip1UDC4UVsWrseJU3kVqNoWDhrHu2&X-Amz-Signature=97c40b9d39f8eb473e3ab9e85b7b38f0cb279889d78ff4f64210c927a295c9cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UXP3Y5B%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQDiVbOHu6Ps3cXSc3brkeCzv0NVBfMSIyYmYmfcZpzd9wIhAPVTOAc2xP2Bw8aEs8B6t7FdQxdFRtibbb%2BNcWvCHIUbKv8DCFYQABoMNjM3NDIzMTgzODA1IgzoGqUc47aouiYXcvwq3AMGQA9djGedWbVrTYiKWWUjKTDGknTUg5%2B3MingbKlJTtneIQjIKglHNfwGXp%2B0OqrjfMApKexQgGH17V9W4GDlc1Ks0IgX1NtWx6yTqnD3o7bpwQ%2F0981cqxWykpEaJ7OYLeBkjtywtvq09nxrAJ%2BlXPcrGfpqMye%2FLfGhiFLDZ4ClzqwzcgnTrZcAbKbap3SrSpHGCJpcC0NBIGAONWgqzKH4vxpB6UdiPXmTHYvEr1OoT3ziyWpyByJifaZiTy%2F7j%2FBYdLD65LGJ8uUwtaQm5T2up%2F%2FinhJ3tH%2FYrW987ZqLbcPrXfmtTFJVLb9G5Z2xABiByVJr1wl1clwijRyY75meP%2BtlLN332TSAk6ciZVkY%2BevwlrgiydF%2Be76s7l4xqWn6%2F9kCHhPTPtJfQn9RuOD9DO0eDzBXc2zCjm7ZhOU5sW5SPCCxu9s2KfPgpqH6ny37IeoyaZ3%2BTP4rzdNzhWB4w8uWihiY5shG1SmfAJeMEcaI8%2BqwXDRgaIKSfy0SG6GA%2BpG1Wfa8t2qr5DtHdKQRcxCg4tPRIJx8%2FjotmcdgikSTeOsNf1xqI9tlTXfeoV4OqT%2BoGoQ8MHDZW2bqmKKVAm6zR5r5%2ByFIv5oAMjq1vucSgcXKc9kBYzDJ%2FJC9BjqkAenMDGLdvWljl%2BvCrJUoNz2YSr0b%2BS3a5BHGuesWv1%2Bsv%2BZul292voYErlSX7sYiZZlxBQJBo2IPmdJKUD5b6bHhOEFGYNjD8tMzy3v6pSXCFiXTsxf334JaNOJkhNNDlj%2FG7dcK6UTlEBVHK4a295pgwSafUDmP2Ar5ZUpo%2BlkL1RXWTeMcogFlh6nMsCLcSgxGDXMWdhO44Pi4Syz73Iqb5haX&X-Amz-Signature=2dd994ad85c88d97d24aebe21b5fe3bee0acc9db3f42f144738906e1ddf189c7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3JTJCAM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQDadmVizlsC221Pi2Tc6SCNTj7TD6yjxEl0lbS07Nm%2FiQIhANMP5NeJVFDSi%2BUTFNd0%2BvNOtXKnioOGUwqUQkx2ECsGKv8DCFYQABoMNjM3NDIzMTgzODA1Igz2ywr3CP1rsXkjn%2Fcq3AMgRVVm5MGg6yzfh4%2FqpcPs%2Fn4nY8shmzCr4%2FQ%2FSfgXjUW2hQhGpnRxMXotlYjUyyekyGSNzAK3RKo1rjb8PB4xdBAjU7eDhrMOxGo5XsCZtJ8%2FgAOgWN5goUwyy81CIT9vpdfuvS%2FTtVF%2FSMGnolnFc0Md%2BzawE%2BS6fOiaGxq1RISNDHKN8Xc4oFjU57eDSjyhD1ECqSdClU%2Fzkd2I9itGLNJB9uVjnnL7tjhUKqYqUJZ5Qj8UfbAUyO5lNy9t%2F3sEmUmpvR%2Bo4TfGmjQqVXdmEaCtV6U7l9e8rQRmfWqvu8EegKrT%2F2pHVBYBket9JgEtHzEDMWeAsUwFmX6CxNKfasSaHINok7V3TDJNPbV8coaYeUqtV%2BBifL0kx54Fu12mf5QfOULEZZXiddaQ9W9exwrdR2XfjGojvJWhjfccrFOqRaSSwA41n11L%2F%2Bql6NOwZ8ILDJQXNpTNtVd2wghAKEmU%2Bd1XZb%2B7k0lQvdj0oordfwMoV7uavko4H%2FXORY%2BswBOiBic9J1EWYRL6hqxO8k7HiyUchwsaxAI17dTHsLsCZRJDdI7NKJemnCJZzKp9PdPx2%2FAD9bvltKHy9waIxPvPoMUwQPVjVlIC1r0IY%2F5ZJxrlhTVtB6CWsDDt%2B5C9BjqkAWR8xhsMjz%2FvT5q91eG85hahhhkcs5wj86ISpGKOf1bNoxCOk7UutxnEoKUUBt8gZ7VY4omCmfEqo5k%2B5Mob1jWjsrd3M4Z0NTW3omWe9JqfQ6765Ql2x794N1QMZGkJouUWVYEUtar3ehKoBdwAI3fjWP9JPYVYQRbaxTEaDZepISzHNwoIgFEPvHR89Gcsn08kCMC2xTNKMfpVdAa8Cn9vws%2BT&X-Amz-Signature=91de89702682e45c69c828e095d510d4e69fba4dc98b5fda77c36d373e118b04&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA4SPW7O%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQCSqyFp9jRoMcZeHs7WpFgBgd0v4HLnEAC2gs5%2FItn9zgIge0NFBqlso5Msjv5Nth1E464LD61f0zgLrCE0apMXGJEq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDNJPOuY40KJh6sSd2SrcA7WmkmQLZi6lYCDpPEA80J%2FFwPjmVLbL8jzm35iksipyhsvxg2yivNlUWAvalDlIlMUfp%2F8bPqp28bMXVKtVa7oMaifsQ%2BrWpemAYcmpMXhi961Z2u7bcN%2FkuSUUqnBBtlH9VcohaN3JPT526T4%2BgUWVfH18C9578OmsD1beUEmuST6oidGRpez%2FRC8lq6v4NLMNVS5vWp4Iwpe393f5GOwIKufAVJrCS54A%2FsO6wdaWjriGyeJLsvv0YciOWW1tBHJJbOCy6RYjCsW7SdYuS2Zh2hPahrMYGDDm1DtweeBRK%2BgJ4UmHws%2BLWsRTgTGmGVdikm2dUnetuZJTtSWqtRkoCereR0qe95BRhyzFennPAoKUE5r66wrDBDkRFf9Vi%2BfkL3Ey2hFS2oWaNtB%2Bt%2BR247fzwHPFey%2Blo7knvr6YRI2eKySTaoc5EKHegPDMkyzMGa5gl%2BbMXw8BrNmqGm1p7mhdYyGaRpIVDVoIqWiVOZW%2Bf0rDci1v2IpPDcy%2Bab4twVErhkXKGZAqMc8aBmSsOkXTr59719Igi4h89A53H0Ay9bwPjaz%2FKIBg%2FGOJZIyBWPL%2BVvQB6B7v00DAwe%2BRIaQ4L5CqexWsaroyA9m31g%2FGmFmQiFvFcq%2FzMNL7kL0GOqUBPCIw%2BlA3n7dX3XPAGWECt04JrmmtAbeeeqBT2MSX4BSLWmwsGhWA%2B6ExH%2ByYOglEar3PvQBsKz9p2rpJzHmPlk0Ub8YOfjvthYgElOl43nAz%2Fjx5IzCviBpQru9smWe67FLizNhnoELBeGA8DHpLQpedmuRrX4l1TVnQFBMeqrukjM2LQLMpEDpwSS65nVXoowTIqf5GtkbzBoXsNV6zhPnJ2GZ2&X-Amz-Signature=e88442bb366b41bdf72493d456b8bad724be033f54b8262b80f804c46a0dc10d&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3NIWQ7M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQD%2BicAQ7xcHlSq13AZfHGkO0LWn7qD0e7Nb%2FAY3QHh9KwIgNsoMx%2BkKhlTVqRHS79psgZ1cXnbTPa%2FvHRPBOVbi7akq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDF8utGcfP0yNxKK%2B6SrcA3jTMNR9qxgn7elsypODItEUjecuOHXTHVuLrRLm6%2F5cQ8%2F0AXi7sIgEMdFt33z05D0wkRlbIRi8W0utVLm7bBlbWoPOtXjqyjkjmAwJ2LVqT4u1%2BDBds4VGxIHD3h9O4rC8Zk0PZ9nq68GrIeqJhaOq2uCW2ExAb6rIOJMdEAX2lDqJ%2FEwr4kkwtUzcN7P5Kmp4kAhULqhgFLrN5kXYNsn2CZrjyc4aPJDpTHF0Ou1pYlpZdMtJ5bt7N2Ib7oPrbdsD7PDBHx3YZkhEsV2v%2BW8glSl%2BKq%2FXIDc09YUjoDyFFdrD8bq2SfeLqiB5PoOTDNcT0GiAeNtlkjxJkExaYkBpkvhgHULdFuAIVyJNhM3Yg9TKhB8T9oRkq7U7yMHDA6IaqTo7DIHNskWrIdY09FUcL7p1YV9lydctXVgRXq8w1%2Bq3%2F0as8JxEQGoYqecq%2BvktIveOPuVVyEqUnRrWj5nmNOTXMT0v91W4fUBSWpMJT20MLNrP6o3bCF2obvNHXxazzlYjkbtjTaMEEWD%2F4qpkB0ls5E2vC1Y%2BPEq20yHFyC2XR3yVHK%2B6X06HhJvqSmqFo3wLZsi1rfs2eAZKvaw0GCN8EMQaaJAhSVcz%2Fft594r%2Fuy%2FMtiNjoMWVMMH8kL0GOqUBUz9ybug%2FQZZ188EdEF5dh%2F32eWlrvZHgHwY5339w%2BFzZcDPAZcXOLNi%2FjQ%2Bm%2BXUPh4H%2F6FJ6aL2dT%2BZKXjjO3Bj8APqLraDD82KbtzGWcUTrj06J2DF28yocGdLgvgCJMGocoqsioGBTy47ZWoWI43OHzG1gC%2BKCw0Nsjwl9MZwdjrnQ6vkKN9ZHETm4%2Fpziikb7eUzcGGOKrLBn7MuFvFL2NQu1&X-Amz-Signature=68cffe8be50b1cee1c6eff38c0aa51a35d0bd22bdd00dc722f660d38b465808c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UXP3Y5B%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQDiVbOHu6Ps3cXSc3brkeCzv0NVBfMSIyYmYmfcZpzd9wIhAPVTOAc2xP2Bw8aEs8B6t7FdQxdFRtibbb%2BNcWvCHIUbKv8DCFYQABoMNjM3NDIzMTgzODA1IgzoGqUc47aouiYXcvwq3AMGQA9djGedWbVrTYiKWWUjKTDGknTUg5%2B3MingbKlJTtneIQjIKglHNfwGXp%2B0OqrjfMApKexQgGH17V9W4GDlc1Ks0IgX1NtWx6yTqnD3o7bpwQ%2F0981cqxWykpEaJ7OYLeBkjtywtvq09nxrAJ%2BlXPcrGfpqMye%2FLfGhiFLDZ4ClzqwzcgnTrZcAbKbap3SrSpHGCJpcC0NBIGAONWgqzKH4vxpB6UdiPXmTHYvEr1OoT3ziyWpyByJifaZiTy%2F7j%2FBYdLD65LGJ8uUwtaQm5T2up%2F%2FinhJ3tH%2FYrW987ZqLbcPrXfmtTFJVLb9G5Z2xABiByVJr1wl1clwijRyY75meP%2BtlLN332TSAk6ciZVkY%2BevwlrgiydF%2Be76s7l4xqWn6%2F9kCHhPTPtJfQn9RuOD9DO0eDzBXc2zCjm7ZhOU5sW5SPCCxu9s2KfPgpqH6ny37IeoyaZ3%2BTP4rzdNzhWB4w8uWihiY5shG1SmfAJeMEcaI8%2BqwXDRgaIKSfy0SG6GA%2BpG1Wfa8t2qr5DtHdKQRcxCg4tPRIJx8%2FjotmcdgikSTeOsNf1xqI9tlTXfeoV4OqT%2BoGoQ8MHDZW2bqmKKVAm6zR5r5%2ByFIv5oAMjq1vucSgcXKc9kBYzDJ%2FJC9BjqkAenMDGLdvWljl%2BvCrJUoNz2YSr0b%2BS3a5BHGuesWv1%2Bsv%2BZul292voYErlSX7sYiZZlxBQJBo2IPmdJKUD5b6bHhOEFGYNjD8tMzy3v6pSXCFiXTsxf334JaNOJkhNNDlj%2FG7dcK6UTlEBVHK4a295pgwSafUDmP2Ar5ZUpo%2BlkL1RXWTeMcogFlh6nMsCLcSgxGDXMWdhO44Pi4Syz73Iqb5haX&X-Amz-Signature=e20bbf2dfe8ad421c62dc11fc24085f7a11f39b6588e5fadb227244e403f26c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JVIXREX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCICnqF3CFnmpESYOW9u1JcVj9N8spQZUurk%2FB3R1vN%2Fz%2BAiBBMmYKkgR%2BymQgOYhjCKVXXpQMqn6bGIEsvjGbhLE%2B%2FCr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMYrUef8tZ%2FZu6orvbKtwD0Wxak5X0G%2FjH4a3M9kHcf3gPY%2B3gYegkA9ZuKL7IIR3ut%2BXTcFWrKgeL64hQLgLqoh3twsdbmJ1QH472N9XD64wsMBcArMcUuQCCu3suME5rHOdsKQV7BhZH%2FlNcnV%2FfX4cPxC%2BVhkKwq8iTkFsx4K2sDoAU4%2FSHMPUQb9tBT7gkKSaPerdXPXHv4GjE%2FkyI3g4jWoyA5PW971pyOhIa7Y2XI9d06jXl9btmw5V%2FQu4RF%2BsSP7WaB4HXeCKJ2IiySxfHvs%2FmZJnpiIBIrQiCVmzu7Ch2Hvm0C8w06qw0lt7vIqpta1fhVohPitEjt2CbPDVh%2Frjs4kLtbFimYKf0GOU1%2Fxym6OMG2NtE04VTy9kx63osAUD13UKb1h%2F4186Ebl28VOH2eNhHRvsXrHqM4e703dp82hbYm40FslIOZCZBsJlGH2FmBrSwxGSbJrfKSIi0s2eaPghBrKgpVC3Lp6pkUyh5hTmt7B8jM%2BkwOXljMynh2z%2FBek9QgTdSE5u73zOhCBjhKTOBUhhNwgqOzBOHkpso7Mk7IBycVdKObdY%2FPPUgSxXcRGgISpBbkqAWaLGOsvx9v9FYzpcbxKgFDe8vhB6IsgkvfBVoW4nDQOTueqoaFE%2F8wIC0bjQw4%2FuQvQY6pgHh2Lkp97cjfI4C9U9%2BrdvGRMTC0i7poKknqy7VeAq53Mk3wSZ85QV1PPr1WeuMGO5wOjpUPSe1KRu%2FQfGpsmwVB7zQG9S3HaJ41Q5iB6eqZ%2Fj9dV4vcDZFIKvPLYMVQUMF50ZVUsrrlXxhHIjRIoLxp1YNFxRPbfPr9fVsH%2BtWqStJiWAwfBScqqR18e8D58aTBTKbYxJt6Z68m8fdrT3vMcD0Cx6K&X-Amz-Signature=0c41a7ad0010217b3d92985f2c7c6cbfda12598fb6729914d6d62314257fa5ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JVIXREX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCICnqF3CFnmpESYOW9u1JcVj9N8spQZUurk%2FB3R1vN%2Fz%2BAiBBMmYKkgR%2BymQgOYhjCKVXXpQMqn6bGIEsvjGbhLE%2B%2FCr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMYrUef8tZ%2FZu6orvbKtwD0Wxak5X0G%2FjH4a3M9kHcf3gPY%2B3gYegkA9ZuKL7IIR3ut%2BXTcFWrKgeL64hQLgLqoh3twsdbmJ1QH472N9XD64wsMBcArMcUuQCCu3suME5rHOdsKQV7BhZH%2FlNcnV%2FfX4cPxC%2BVhkKwq8iTkFsx4K2sDoAU4%2FSHMPUQb9tBT7gkKSaPerdXPXHv4GjE%2FkyI3g4jWoyA5PW971pyOhIa7Y2XI9d06jXl9btmw5V%2FQu4RF%2BsSP7WaB4HXeCKJ2IiySxfHvs%2FmZJnpiIBIrQiCVmzu7Ch2Hvm0C8w06qw0lt7vIqpta1fhVohPitEjt2CbPDVh%2Frjs4kLtbFimYKf0GOU1%2Fxym6OMG2NtE04VTy9kx63osAUD13UKb1h%2F4186Ebl28VOH2eNhHRvsXrHqM4e703dp82hbYm40FslIOZCZBsJlGH2FmBrSwxGSbJrfKSIi0s2eaPghBrKgpVC3Lp6pkUyh5hTmt7B8jM%2BkwOXljMynh2z%2FBek9QgTdSE5u73zOhCBjhKTOBUhhNwgqOzBOHkpso7Mk7IBycVdKObdY%2FPPUgSxXcRGgISpBbkqAWaLGOsvx9v9FYzpcbxKgFDe8vhB6IsgkvfBVoW4nDQOTueqoaFE%2F8wIC0bjQw4%2FuQvQY6pgHh2Lkp97cjfI4C9U9%2BrdvGRMTC0i7poKknqy7VeAq53Mk3wSZ85QV1PPr1WeuMGO5wOjpUPSe1KRu%2FQfGpsmwVB7zQG9S3HaJ41Q5iB6eqZ%2Fj9dV4vcDZFIKvPLYMVQUMF50ZVUsrrlXxhHIjRIoLxp1YNFxRPbfPr9fVsH%2BtWqStJiWAwfBScqqR18e8D58aTBTKbYxJt6Z68m8fdrT3vMcD0Cx6K&X-Amz-Signature=cbe65d6628f9bbe6496f7ab5c1e518b94a518ef16c50665625e71bf45d943472&X-Amz-SignedHeaders=host&x-id=GetObject)
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