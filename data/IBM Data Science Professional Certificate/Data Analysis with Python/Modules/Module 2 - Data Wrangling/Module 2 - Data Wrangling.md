

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QOJ4BCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIGrpzd63HXHEnF3F1EOydzqV4xidwY9OO09HHvu0kw7fAiBoF3%2BJ2e5CzFAxfmnNvuEmUWo%2Fj5QgF3VzKQrOyWezqSr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIM%2F9Hqt3IC8yc9O%2FkVKtwDWR%2BMi5JlJa0gbJ3QCYSxzkQpF0XPxIXx%2B5c6pfJYWygtZM3gqW%2FAIHUM7yygKowuqf%2BNxcX8yMi9k5FAdSRUCzcU3CNxR0INB7PopUWhf4Po6mk%2BCoPl%2Fc%2Fv0HycrYeQAHUF06P4h8mb9636jrpeNWx%2Flx0bIkW0l9H1vAXHNge3jjeqC64DGpkwS%2BukvoUsaLcBXPuBFSrkAsXxmoAgGktCMEdN%2Bjxxxm7CGfUx%2BNDTEKQMMyOozaKRV9x6XUaD0CK%2FlUb5ZYupyvHvWZ2LKvEBvRzjm3%2BPBu%2FuOD8T%2FJpP7cRcAyEyZIyB7RPCQev%2FhbtMUNUNERa6i4s%2FCIhVQvqafbwd6lDazQ%2FA4XRPH3ckDEBeA1L93%2FqmkmtICjCEq2xrMlztwYEzTFoe8rMO4g5xu1UoQudzTw2ovnq1etJM4zjz8ssBBoQqK1T7ebJBSv8y8%2FGn%2BYpHyO%2F4QWiZEoS7idlJJgkWjhoxVUeS%2BbJ6uFWPtbzX%2BTZdzwJZZrKNK0vcj24A3XKSrcyXrAmlopEGrOBECxxDMQz3A0wSg6S6%2BA1EGmI1p96RVOTK0tZI1Ia0bGAn2NtPh3PSAbXvhxH%2BXGdPEO2bkZt0h4gnJ1HBOZ9AsXR9nZ4b2SYwzoOEvQY6pgEHepZ1QuyU%2Bt9XDctJ%2FBsYo9ifTJ5vvGQnuIiTJayb1Xez9eetMyHzfA5yKsZFPQTRMCk0eG6YgdIuKyhtYBG%2BT4BtSVgyObrLzYAANz8lRgA%2Bw%2F3R9Urzg0JCyqNKOP1eobK1m0Vw0V3ZRfFFwaJWtqOxOIdZqDijEkRGAL56FNux2hKizaUb%2FNnlYbWv2srzpFNN%2Fc%2FOwNsAtfveJobWjJQD8zkB&X-Amz-Signature=eeb049bee84292c4d0c7b49950694ff20b45ae2a46fa7ebb8798b863ba7e924e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624QKEY63%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCnKgfO0ESl5RO5IK4JbNRhfqTeEvbMZ6CeZtrkSFAZhAIhAPQGLoiPvS8BuwUCg3iEo59c7UoLbSDunrTlD2sj9hmOKv8DCBsQABoMNjM3NDIzMTgzODA1IgzABRb5ypFOAUcp%2BUgq3APtKRdTArjSiRqiCpjH73psBcItkQ9lfxnoTWJekWXvE6IIa90AwXfESBtq8%2FEDATwdzSHVfnVUPOjDN1Le7VXCLs4w5yZq6i89vCOYg7E%2FdVk%2BZ5SPPfofkwOQJzqnQJcz4gx6EqAQ6fZmCg85fAFMqb7d6SQuEt%2BeP6pSBvSvJZwIc%2FGu0A0bCN8pXrBtksNhi78W5p35vj3Lp%2F1ddx6TdjTC3%2BPdlH0GGhgJ7Wa%2B95R5uOhJCyYNnR%2B9srgq0GiReO2hYw1D7KBiPgzQfhtJFamVbxgxsQmCnB8wZojMoWNIRWC%2Bcd1UMJMFQrB2tPVDeSHdqNPuZY8dD5RZSubjxVk6UyRd483dth5P%2Bg36GpWa5d%2BOAk4q8CG8n3gt%2BxVCV5EyWq9GBjCf1Hl89MLCnqfn5Xx5ra7lmPaAwrDIa0D9No8KTji%2F5Wnr5i9vnBkhbeez%2BZtz%2FwTVH5n%2BBo4FqSiJlnhg%2BmH7q5R4YFdzwRgfHYTBSu4o7qDEenIthPnjZD3FQKMK3OWxn4cGiDkuIhcu3lrpf9DRGx5Alxgx%2Fjzbxd2QTW%2BKGJlSNAhtBk9FRaXWQ%2Bi%2BT5QbRU%2BUYKeyDwos5rqvtR7yhY96urf32q9T5EjJM1kWkK3WjzC4g4S9BjqkASjDW%2FVbfeb5Sz5gjVJWdHGGo2v34k0Oqd4Auu0FpfrxYYbYu4zium54VzKbIbroaSsn5bLFaVoUeD1HZ%2FszaSzmh1KCnadbXvtvEWSd9H%2FKhQqW7X8u0mSzm%2BW%2BJS17cFec%2BMn2S7Bqrh3Ln0MjVOt1CFu8VEUDoET8BXC8XOscufSXuKLAOWWodXLk8MbgdWDNyHx4Rn3mMTZLVdy6AqMrRq1S&X-Amz-Signature=35f0f87bc1416e62a7a575515d9b68285eb03d2e1214bd687c719582b265094f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2HYJUMR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIBsuci8guSlrGWr83q4kkzmnzAzdy4RLD%2FgqT2Jj0ystAiAbjeDMx8Ss8oy72XMMcmJ1TopjYIJmqm%2BLTD0OAeBRhSr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMwaiz7JNu15gdGHNQKtwDp%2B34Z684JcqjTPONicJyjFRlEomLUnf086qp8NolqmX5rduwcKjRke6hN5oBJs4QO9kXjCSnwHfex6XE9WaWtk9gjEi4b4YgZyuGARyeT%2FYoOnGiVFMiAxy1wiJJ2xcDKxx2c4Qbf%2BIzeyRaAQ6e5leQS4YPwaVBnq%2BTFHikU8FAKzUt0kBdhvkMnRvpH9FqERbkkP2vL1%2FWfweskuj%2Bz0n2kZnKprvbDAZy6IhSYCirIY07k6hEj5vp3mEV6wdjZ%2BJzmVPyJWsZ8d6jPgBBCrqUqlUFe9aBKEVS1zUOGqXVcfxfUUKJADPUeX0gfRB1kSzW881kyfaKTyqcY8OTyK2XOUQ%2FI3cFZ6oLdQvvsH3EHRswKu%2BdbolhfY%2FYFebkIK16dq%2FH1xPbSRh95h1vjySIBQoiyFFTL%2Bsp8dHTMxoRwLLCKlS8Des0CD7jMxJ9Dz0Ck23pBkjMojGH6tzwnOhQT%2BneWTbmwLWq0QshS%2FFsjcHZaj%2BN2BG4qZz3vwaFe8p6wi%2BpDdbgE9zhZz4DW4p8EcEsBxSAGUOf9XQTdYWj7fN5icSKoymqNno0I%2FKu4e1ryCuIxCSa9v4ZpjbLksl2mRuIKIL8Q%2B8cxhJtrmU9CkD8mXXxASFC%2BWIwnYOEvQY6pgEulj%2BVFBcOdD1Bqt3HzLUYVj0uULOGpSV5W5seIZMWVcnxLbR%2Fj8VvGhjBSMExuwKlYLs3FIrk2rIb4H5kUGmJupxkRatKArHcWc41%2BREbS4RCLqUIixnFOz%2BtwKn8UyxdFMJk7G0IlfY99JRaPpGWBiiu89upr9zc9ThLcykNlLtTNNjb2Xk%2BKPjCdwCpqQytpvAPrTL%2FnxxjmTQhY%2FGjvsVIyhlu&X-Amz-Signature=c9715c059db40f4e3ff4f6421c74167e20e3a814fe2868b09ead13e397b31fd9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KOV54OV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCc%2ByWgbAYYVMmV4QRtS%2BbMyLTycdgFySXnN%2BqwCIETFwIgIAxRPGkiM1ZekIfoKC4PZo9dJl16rI2ymTSwtZCKnQMq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDPvxUF9HB%2Bv2K4q%2FHSrcA1AOWC0GnR6nZifXc3Xo6IHKU%2FQqi1zlRlCtHzLIrCWH7CMlK%2FFSPI7rYQweLXvzL%2BNbjMbAbWQeCRPwxchGYX8baDF20LIkPp30h0buyKYjmtRSxU7fRyN%2BaFpsPmUrgoAkkTf821BGVAdKNss2485DcxXYeD2nLZSdgavbfPFuYxfL1PglGSb8Wa%2B68Ah%2FAPWQX0tenolv7nrf3yIvehRMO3dHJBckc76FWcm3I94%2Fj9NyhCd3FSWOn1qyMbJVD0m4XZACdcKKTjXrg2xq0%2Bme%2BFGssrvUfel4qVEf%2F5zLNTQKfhH%2BaC0ooEbl0C5bDzeQIVLT6LPAAvYiLt0ZMKt2AzVr1crpyKNE%2FGuWTLrPy%2B2DdeYjoPCEy62RBRIUzOo%2FiIIjxPhSMFnH8rTpQR50MX%2FCRI5iSpHXgahqIENShyvT9aab6Kf4zkIkQjNRSS0BHRXF6S0I%2Frb9Q8ZFEGUIfj15PEs9rGv8wzVJuxkoIMKx5n%2FUjmWxjgy8bC4MuYMhYjrFhOA9m%2FcsO%2BvhGlykIucTJHszMkI8dBThiZYbEgt6MzhMCk0cRod5O%2F5k7zp3vHfEZcl4o5sJgSJRUE3FShbljbGkQTEEp7xo1H0Q%2B6Mr3f434qdlJx9BMPSDhL0GOqUBdCW3SBV4RuB8RZrn%2BPqEKZEllZHiPu6RJlOWAeDJbwhnMhnan36BqQdo%2FQD4Sieqg97itcs4ZSwvzGBM7Q%2BXyz8DsM93d7FCYXVSjV8zWpo4vSN4YPWWiYe90GxkglXgneiGGiEfMsGYQheYPUdHPo5RqfYuHEowLmhYa8%2FWgWe%2F9jzTclLZha8huQboURg%2FXaTeyayJMCvf6kW4ZK8E9BodnqaQ&X-Amz-Signature=01177a298e4f38ee1c37163a74abee79c509f8ae3be5908dd4f478fefe80033e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GJ4MJVV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIF2m6FEjVdTEcOjt4FLdSYyx%2BrLRirfdfM%2FQbxR%2B40BAAiEA9zRsaD2XEwReN4L1E2EWMfQhiMEjaYqc4S9%2BX7Rh404q%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDFwsUOOCMYwSJx%2BM4ircA8gxVq%2FkIAY8yBQ1jM283Jo9efcH%2FwvZc%2BGykb8gZJmw4KmifiIz5%2BkxS0IpBvfayhhKiHDNZETyoJsUxIs4GhxerWpsUMsF%2FybUFp%2F5ILMk5KEd%2FpMvSFpgVSv1imWIhEe91uV%2FcKHEarZ3lkA2nksobPmBgzHcytwhD78JKXSTMAyH1cRrs%2BLJ1TFZVfcjnQDVTwQoIzl2JI%2B6ZXrdNTUeEmMGFwEYFFCgtmpNTRX%2BF%2FHUhjW9qo56PRizS4ZJIfE%2FBW7In3QLH4J%2Bddqpjmv%2BUvEzLSMr3xL86ULyipWe%2B4jfRLxw9zVj5tjh43a7nkW63VcnjKGtcLZq644c3nrWKHD9IsYiNcc9hHeFCAuRPCVegjMb2MSR9o7EIdpzA6jK7xVLDCbATeuEhAJkJULuf5awj7uw3j6maU0UJCjjMfnN4IZmPbLq5e8PzcbSPyERjB91LpRVGGyMPnofjAUYONIrPj%2BqI%2BmYxXq%2FgdpGY2CYiQLO1TH5GYXr3qgJuo2QP7ELFJNh2%2FnnX67wxan3hQqmOPgnWlcxN16bm%2B4Yg2HESjcjGGidaqhZEjpwlZPe0w3jb1oA4EOOV4ZdMYbU6szgEFEDikaC76BLMulJYISwkss4ojXEnEvnMLGDhL0GOqUBKL%2BbRcg52r2XRXl65ObKsnR4Wv82LCzmkG%2BKDlbtCw4uhEn9Dy2%2FaaxlS4R7dlsKzUVEd1QFrPryt%2BvV5Zft2GyBCSVGIjqsdurVZBBCmIOxEnMJVxmSaP0SshYhi5XhCQimXP3UXLEbKyd6YbCakVPPyyzI%2F6%2FVHcihnOMq8g6G9FIqhRCx0oErSnQDuFlqvv7xqGNHG5CsXpmF1GT2Yqm7gK44&X-Amz-Signature=7c58781468c3a4fda83c04acb392626d20e105790e75919879ffa60a99e33cbf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663F7V3OZG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQC%2B39zvi7eKwS6g%2BR8Wo%2FCND7X%2Bk4e2eS%2BM6Zpqyww6pQIhAMV%2FIIKoCQ31HGdlP0dkrBGMl7MZ3uuuR%2Bl7goGh80oEKv8DCBsQABoMNjM3NDIzMTgzODA1Igyk4Ejkl89ZWX%2FTXS0q3AMcdajp7Us4RHlw5BW9sCcA5UV0dJkQfEDPuXyn7%2BbUXJIg9ChjR3FdMYP8yKEeb3SZBzK0cczFHuy9agUoqoubkebnik8jEjoxcr%2BiExWtWAsoa7kcdGgqcWrDvYuR0F0VZMANesv1k0iDKDfBooYa%2B8uRABD1KLrebm9MDmQ8uJE%2BUDwa%2FgADuJykklaWFVR3SaOrw%2B6bMWht3wBhGczQY9KvzttgVsiwRIqosW1BrgfcZBKVNWj751JGKxyCB04wMZvSMmf5fkXE%2BdFxichUrN0Uqj%2FBlupceFHZ9F4hJMtb05jqtLpS3ay%2FTo2XEUdP96pnS8%2FqQxLsOhGdtux8m2pLjFzS%2F7Meimf46I1wVaZRH5ns8FgPThHND2oGt7ncDqhn7emwzYPxlKIhRZV7VSFuGm1w%2FoJcq%2Fle%2F3qICYCRlxZCL1LIi4ZAZ6kGtJIEFw0N2Q777VxPQVWNW6UL5DYeX%2BGquIlQpV98%2FeQTLuW2%2F24jYVUC%2BKqRjbjkPPIkWjTKFn3dBtH3m%2B0GfjBij9VLKwLttIDh36B%2BsY6nmhcRwa0fIqTNCiVo4rw9JGPsY2DvlpImX85ozb%2FJSzY1pXfLc5diH4SD00B%2Bq1UC8LeQUOyzJcAZ4IAVnjCmg4S9BjqkATl3xvBaZNIKfHH8I9rEiJsoXyHcQU9%2FzobDZjCDjqq2%2BOCaf4dLOA7Gs7zte%2BSKxfONryEjeEq%2BQK5huk96YWLdOvL6GeUEgQCDVnnx7boGM9CvqR8ZhYimmNdPBdRxb6JMWuY9OhObpeA0LB9Eaj22Hc8upZxaVUWos6uuV1RKghgmXsAjQZY7YWOWC%2Frh6b5cienzTTEAhR373IEXbGes9Iqz&X-Amz-Signature=2354ec5b47e8a8a07216e4b686969d53bd2d1ccb1471d8df7bd39be0e3aa938c&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQIWUS7S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIBy5Igb762QPGpGuGMph7IGytogDDC6FjWhZBtDmnZlbAiAskbjHkAMyaG2DVFm%2BcmQ3J2%2FuvFpkEsOUjG0ZJUTS9ir%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMguX8iKNDtxpZmcxkKtwDkwOoA3vu8pez5e37xuu8ellKgGAL2ci88BiEGnGh4iZGuqOMy%2FkrjiSSyzUmpAiBSKnIdi5gBx7sl%2BM2DmpM%2FPVG16NXFCPpCJjwnpvjsm47Q8YV7DfZiHZ8sqA8d3ptGX8%2Ba9DGCRMOlS%2BK4xOvsNywVIH3FFtR%2BHLDZrkx6Fl0PX89F10%2BZDwibgRWaW8Z8Rr5sVoNiQhQ9ZxOLMPhBrP6jJb223tfHXuYs609zs%2BR7dBXA1O7OyISvgRVMzia%2FKK%2BdBEm%2F4jkXHpS6FnARGHNrrMl%2F6tDPtmmzlYAFnXkrJi8u%2BzbITT%2FCFiCq6TckRAWCSWawpA7Voc0vSOVcq5o7ac7g6Yd%2BA%2BcXroSirMu4JuShBFwogWQLCUjXPch8RCD3TCb4aiFTYKa7CjMDraCyjfIWgyt3sRti4i2Un%2FVO%2B8Q0bXYhX9Ybu%2BP7rFCoYkHrC3SvQwNCTdL%2BGCj5EdVx8DIsthRJro%2B4HnNgLHV1g4EyPFUbnuyIZsPUKsFbNW%2BhlL4nQOej63w8R90BVEsb8ASegf9mtQQMh0jd9tthRDe3jlkK5MXP5D0BndR6Gy5NFOnVEhTslFzZePWroU0v7lJ1ToKErqsHXJLUB0whrrCNGSYYddhr5Mw%2BYOEvQY6pgFGX%2BgAowSZWLt4Ni%2BoAPCpAgx%2F1B%2BDO7Pubp4aT7SZ%2FeDY%2Fl5KGxgLqko8n3MPxQBq0pSikLoGYEGM0ekY%2FTP%2F3nggW1cmeid0rO%2FKUOq%2FOPOCny3RsqS6%2FiHaTB%2BJL1%2FzKJBN86j7xDdo2har9RjO8clrnzlHVgAKAxovEagZquRz3q0M4vTlz14a6KxG8PLDw169m%2B23by16fC749B1Aj4JXWxNL&X-Amz-Signature=e2ebcbdd60190268999fdca10756a4a4e9d056d0ce9ad4d7f05d75201b195e86&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YXOBFW5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIEGijxMIn3%2FBgspDNiIyuI4csKyeDUOG2kJEV0ARRXcmAiEAp2zjMXNWjjHv8RAJ8zdBAO3lwduP99xMHWJfGNzMV2wq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDBheg1%2FyGglMVvW15ircA3QWYrDxJVL3sI16HwMekiwJJWtkHjrN%2FBjA80PLAui%2FD29gH7qp%2F0OOAw4nCmuG7nUhc4QRcqyKOz0dFC8edqKxxwsZlLZpyGW7PyB2fhkAejxzxwVpNf7Fc8P5j8DgJT5yBxm2OGE4FtFtTLjbWcLhWXzezWIwEWjBeYuMQpF1vwgZHyADGhFzrBcmKXKrCJ82rE5TjhaZA3Rr2yEV8aroAfVPsLzvJqRAh4rXXLR8IFQzO8%2Biqjc%2Ft1st1TGjrOpdtIS%2BYpPPgpvjZI2FnACfJqz2awTbBAVDb1GkC7czAwr6SlYFauDyp13XV5I2rmXtd0rO7Wca9YB7PFTe7YBJ3A6aAy%2BNwJTMGDCr0Ivwlsu3vXy3rC1X3u2nK9hhlyRzCLPH0mNdHBJ6nwl0xUvjDiAjo9QGwKiCe8HKZ3W1a5shFciwfSx08zQ9gJLFaJEGmzs%2B45NK%2F%2BVu%2Fe5yMWi6fchJnOHwpoLxdZb5XWYJG1DizQ3jehzVZ4TEOVXY3HHz86erfXprNsieyGmOE6X2MbHS3Wegdv3VlzJdQOsiX6YpRe7jzbPddOgvNCACb3yIsbHdP94Mkoyir86ddf23Mqh3Bb4uKU5CxQ7idAmhN%2B8bVUoE3QK5q1UnMJ2DhL0GOqUBjpEiGo0X37uy5Ss%2BRcStYS2KmvtHSS8ULYH8KPgUOIL%2B4iPD8MRJpEW1RypGPG8yc3M8CwrAXkR6LdnG5RCPDEhheEMRc%2BYgObLSstOFE%2F72Zw%2BZddiMlgE%2ByqZYNqS0HriHYjQpRU11GmlfC12EaQgJhsErkD3dbwiASuumf6UyZvmIwGYZwGAWMSXFk7L1QLKaQPCsHQJuaa4Fq%2FRfENPrGYy4&X-Amz-Signature=78b9a07e234ae519da0615458f28426005b5acf80b53a13ba6e642aa5f1a6a9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GJ4MJVV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIF2m6FEjVdTEcOjt4FLdSYyx%2BrLRirfdfM%2FQbxR%2B40BAAiEA9zRsaD2XEwReN4L1E2EWMfQhiMEjaYqc4S9%2BX7Rh404q%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDFwsUOOCMYwSJx%2BM4ircA8gxVq%2FkIAY8yBQ1jM283Jo9efcH%2FwvZc%2BGykb8gZJmw4KmifiIz5%2BkxS0IpBvfayhhKiHDNZETyoJsUxIs4GhxerWpsUMsF%2FybUFp%2F5ILMk5KEd%2FpMvSFpgVSv1imWIhEe91uV%2FcKHEarZ3lkA2nksobPmBgzHcytwhD78JKXSTMAyH1cRrs%2BLJ1TFZVfcjnQDVTwQoIzl2JI%2B6ZXrdNTUeEmMGFwEYFFCgtmpNTRX%2BF%2FHUhjW9qo56PRizS4ZJIfE%2FBW7In3QLH4J%2Bddqpjmv%2BUvEzLSMr3xL86ULyipWe%2B4jfRLxw9zVj5tjh43a7nkW63VcnjKGtcLZq644c3nrWKHD9IsYiNcc9hHeFCAuRPCVegjMb2MSR9o7EIdpzA6jK7xVLDCbATeuEhAJkJULuf5awj7uw3j6maU0UJCjjMfnN4IZmPbLq5e8PzcbSPyERjB91LpRVGGyMPnofjAUYONIrPj%2BqI%2BmYxXq%2FgdpGY2CYiQLO1TH5GYXr3qgJuo2QP7ELFJNh2%2FnnX67wxan3hQqmOPgnWlcxN16bm%2B4Yg2HESjcjGGidaqhZEjpwlZPe0w3jb1oA4EOOV4ZdMYbU6szgEFEDikaC76BLMulJYISwkss4ojXEnEvnMLGDhL0GOqUBKL%2BbRcg52r2XRXl65ObKsnR4Wv82LCzmkG%2BKDlbtCw4uhEn9Dy2%2FaaxlS4R7dlsKzUVEd1QFrPryt%2BvV5Zft2GyBCSVGIjqsdurVZBBCmIOxEnMJVxmSaP0SshYhi5XhCQimXP3UXLEbKyd6YbCakVPPyyzI%2F6%2FVHcihnOMq8g6G9FIqhRCx0oErSnQDuFlqvv7xqGNHG5CsXpmF1GT2Yqm7gK44&X-Amz-Signature=d56183fca517505b76780afca84a7f488b656694cca6d12b152d5bdc7b07b1d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHDQZC7M%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIEWa3VLbTypnLq%2FI0MZS7dUL8Qdjm4fbOnzTmohJNhKkAiBxVPv%2BjLDh7J83oJNNH2lUFN6CTTuPSR9a2ZsCPmvsNSr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMIRwrB01aU9HOJArxKtwDQQARzE48HT4edFEMNi05dQWUTB01%2B%2Fu1vQkWUwxwfn%2Fj5bsm79Y7Q8aF6yA0jJ%2BCKy%2BB%2B2pWm4L%2FhB8%2F2KdvpZRWnD0bm9l1wVWQ25U85jvRJixVVjS8AEEMjbKYHDDgaUXLYUYr3g5zzOfmyWsgIvZNq78bOOlDuy54QAVBV%2BADjXONp5e8VclvL6c0ptRUizeYgeUX53qwasRDX6aaRg8BazsvGa9BWW5ApiNu8JbIyTrr0krVD4z7y2E3GWLkzJkat8iWpQplsx5TA%2BdT3qY5b6e2P6uWemdgLAWMhlN1MsuFgPj%2BLUcxGFk5LE%2BQJgw2YxtcHisaecNTyPC7YPX1qTRBitRYwRdld01%2Fl%2FUKAkEPqbaNJBsTSMriNViwpo3AXVWbkGhG5agISl2HWj5DbxK4histYchGVsghTJ7IOI9sDK31lchjFLdlzK41KbZafUkplnpgq65YaHWDlXQKNaffUx%2FUtiWuhzwTn0R6sj%2FZbteHK3i1x5zZuKKAbIEaUGcQ87U1jnDA1Hb6BIefgE%2FHDeu5OQndTK%2FfA%2B5lzgNtBPHpAPN3Hnfp7o9rYyL4yPDtXDQ15Id%2BYnDXkXObFTGMI03zA37vjx3mksl3Kvhyla8YwMpdi1MwpYOEvQY6pgHpLC0q4KOZC%2FTklQEl3hWCIQ6%2B2x1U6Y5Wep8%2BbNBNqhuFgUmaTdMIwfcof%2BxlvfngmSXeHtUCNjkVsKge2oaupBj2Z5Ns7IPyekgAEwBTOtG36HK%2BTRjWzeDiu%2BxFjCiaTM86aX6uCpLDyIJ3TwRQRzB7dwByjfwyQ4QpSPPjhkCadD%2Fec%2FgNmn2p5BxSF8ZMsx1iZjeMseDP9msicaQ2kJW1VWW%2F&X-Amz-Signature=273695e31cb379cfb5abe239e9a72406eec71550891442ce773f8d3c1a7d5c2c&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHDQZC7M%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIEWa3VLbTypnLq%2FI0MZS7dUL8Qdjm4fbOnzTmohJNhKkAiBxVPv%2BjLDh7J83oJNNH2lUFN6CTTuPSR9a2ZsCPmvsNSr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMIRwrB01aU9HOJArxKtwDQQARzE48HT4edFEMNi05dQWUTB01%2B%2Fu1vQkWUwxwfn%2Fj5bsm79Y7Q8aF6yA0jJ%2BCKy%2BB%2B2pWm4L%2FhB8%2F2KdvpZRWnD0bm9l1wVWQ25U85jvRJixVVjS8AEEMjbKYHDDgaUXLYUYr3g5zzOfmyWsgIvZNq78bOOlDuy54QAVBV%2BADjXONp5e8VclvL6c0ptRUizeYgeUX53qwasRDX6aaRg8BazsvGa9BWW5ApiNu8JbIyTrr0krVD4z7y2E3GWLkzJkat8iWpQplsx5TA%2BdT3qY5b6e2P6uWemdgLAWMhlN1MsuFgPj%2BLUcxGFk5LE%2BQJgw2YxtcHisaecNTyPC7YPX1qTRBitRYwRdld01%2Fl%2FUKAkEPqbaNJBsTSMriNViwpo3AXVWbkGhG5agISl2HWj5DbxK4histYchGVsghTJ7IOI9sDK31lchjFLdlzK41KbZafUkplnpgq65YaHWDlXQKNaffUx%2FUtiWuhzwTn0R6sj%2FZbteHK3i1x5zZuKKAbIEaUGcQ87U1jnDA1Hb6BIefgE%2FHDeu5OQndTK%2FfA%2B5lzgNtBPHpAPN3Hnfp7o9rYyL4yPDtXDQ15Id%2BYnDXkXObFTGMI03zA37vjx3mksl3Kvhyla8YwMpdi1MwpYOEvQY6pgHpLC0q4KOZC%2FTklQEl3hWCIQ6%2B2x1U6Y5Wep8%2BbNBNqhuFgUmaTdMIwfcof%2BxlvfngmSXeHtUCNjkVsKge2oaupBj2Z5Ns7IPyekgAEwBTOtG36HK%2BTRjWzeDiu%2BxFjCiaTM86aX6uCpLDyIJ3TwRQRzB7dwByjfwyQ4QpSPPjhkCadD%2Fec%2FgNmn2p5BxSF8ZMsx1iZjeMseDP9msicaQ2kJW1VWW%2F&X-Amz-Signature=ec00ee226221d82ec9ca6d09b6e95189c9780ea3bd3b9af22a973d3ade5b0023&X-Amz-SignedHeaders=host&x-id=GetObject)
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