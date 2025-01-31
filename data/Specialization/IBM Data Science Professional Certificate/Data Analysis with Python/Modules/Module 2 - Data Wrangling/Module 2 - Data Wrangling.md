

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM722Y66%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIADZ%2BiidxFDoM%2F5al7rjSDC3wymyeCc2q71R%2BGhMzw6MAiARWHFi6zkPpeicxhSXxsjtK6oGFaMzM%2BBT%2Fz3uD6gpdCqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZkHybkPM3rjATZ8DKtwDEf5HnJmvSqIe5g3lKRCiF3X8xdj20uVI96z2vkix53S3Cp5wkx%2F2MnYHANe566Ap6PkhGZWaUaA6sLXf46%2Fq9mcnrRdrgsTTBzPlKigmlnDScj7eSRKs1l9eMgkeyPs7G%2F%2B0A%2B4Kkb%2Bso9r%2Fe9X%2FZswowXkd4h600ssihmsd%2BbzMmyKMOu054%2FZO37bu2K%2BHUfblqSXpMpHm9vS2Tjx4RoTo4ANCfPnU%2FM7F6U6L5Uinguhkpca0KE16Rv1j%2BBDyCsjatCq5dOI46UKHISp33rMaJVInsOaX6kYp3z5gQbvUhDlaFj%2BBPIaHCDHjRtHuc2954afj7zwXkVg5fL676OXURXZ43dsgNf5%2FZYchzE9YNpEKriZCKVoxMuIJyJqQUbWmGlnJmncYyAj%2BSkG8e7gA1ssYidyv8fCDtVpLxnLDl60GnUw529Q4KwajBoJLl3Op4CFDgPb%2FuRdDVFMEHX%2FdXbayN9nB9GK1mJDU5dOLuAPRJUmPtPrDQR0pV2zlz97Bsrh14OS8QYu1tgEuwTOVgAAcHqC23necd3oNV0Uesqs%2BBYGr9wQk42gntiHZoelBs8sQ5WDnGfO0xEL8XWelurnl92WGCBssK9Jq1uVcX%2BE2bUBgFmYFYOMww7byvAY6pgHmhTGV17XZvf0oQw7SGl6iHjMkyO17cZu9D8qfzibg025T9NWA7LH%2Frf5zdHHiaq5d5et%2FqlUYXKhNUcdO0mCYpIfbAvTam%2BCBn9qFlC5pYE1iLL1D6tz4Cb0r6a1WE%2BhMADfo6tly4jlcyOZeJzUmysWv6ymtG7AkIWOGPMZTSt69GrfMHHiszrJateWC5n9cWIU%2FPDcCw1%2BtFVHwYDpbn0Ahdi3v&X-Amz-Signature=a75b378b8df6067d4fa126b59d85adbddcdf5d77e452a9e3dde5654d6fda7cea&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z5RRMQI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWMWnftA9ZxLN1iQYr6%2Bea%2ByKjkFjuVEzEXXXSluA6HAIhAOII67fBWaGwmP9EmpW%2BxBKmjiuLr%2F1O3ylarq6EA8aQKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxeuZTxGrXfG%2BtatFoq3APgHqq2IRn0qXUKNHANv2lNiXjKdM3A%2FT%2Bhe1Qoat6%2FfU5Eqe3vu5h%2BjRe7VlgCKBJPToyc0RNnDJwCPmC7Qd2Kb%2Bl%2FnqCokjEhfj6%2BoCPE1AtHlcMrPOl862I63HG04DzLdFxsxrHzMaEW4m33A1xef4hz5ssdoxRBA7NGjNgo1BmooOuGUM6FcML924uNvcUTYS%2FNL4WIjB4MwEmQHdEebZxoTpKM5QESdAjfHyPVcuWh2evMUeRWy5zi6QrNtMRIwFPZ%2BD5EFYVaMZz9%2FBijXOvK7YwG7ljheXl2PCu57IQKr%2FtDmVBMXGvw%2FfLkE5ENoTV6DozTyO23FLPLasjz62DqGdUgaKjrUZkBWFnFZ7rxkbORG3b3LsUl34kaMSGR39r%2BqxMwCapYD%2FSqE5r161MwZ7BLnX4qHxzzr%2Fl4dJUrh660Jh%2BO%2Bj6z3y2SQzfNckmi6jY1jwImUjmeai98lyBXbqrncP7S2FMprHEiSZpgwtVyeSABycbesyxyhCLsUtf53ZC9o%2BoPxNRhd0OpQastyAfZHX%2Fx9nGmg0nUgdbuBdoshIKopUSmnZ0nknbULtXoxltsild8KwSzP87PpW8MpYCsNcZKHK9fqR0plTG9ljF650IhThdhzDDvtvK8BjqkAXbs4hEtSvKqoj99DKZcsEdKQHPUnJI5ftn8bDQJPq6Mq7CFKr78oF0p68Vn2xvJrP9SFLb1GcfyVXq1Ip6L3Tbwx2ZcBU5%2FPA2203DeeE9NVV4Zk%2FDr46SkqVQhl%2Fko2eyV2c9cnejPZ7H25eJadGYus%2F7PW%2Fjb5x%2F2FJ5DAWKf%2BDwbVy0GUXaKAn6iUjb6cZ3mRwXPI1Vk0JfRXBHpTmLOk3SB&X-Amz-Signature=cb680104b30e9e9b27201482efd8404c0047445cf2bbc8247a4c9e46015d0242&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LMAWQHV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE07m20nbelzuD%2Fk91kJHr8cY1G3OipBoCpF2p54pmZ4AiADZCPy4GCBqVRmn%2FHmbJjt19qghla24axrQf8ZstP5eiqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmA09xfpBWNUH%2BW9sKtwDetdFLIcDCwHhDbAQmOF2uL0b267QzIDZyuZm07yUJft%2F1EanHQBdcxHIZn4nrLKA%2B%2BUgmXf8NlTmdRQ0BSpcfbnQEtIuVh%2FOPs%2BRtP17PFkq4BEyMHpUuOQUL%2Bj5iiRxRH9LaN7T0Y3%2BZyLWw%2BYJ6l2HGz1Qjh739bLAR%2BOgnIjLKS6jmL3Buzg09xJgKmLQg82X9PG%2B38jhc3Bj9i9NJNF0VcKOMucIN989495j4Nfc0D83Ph%2BWcLdMvnsb2twy6iQnqyyzT9Hi8%2FHRZIWyYdSi%2BUA9qXdLKZoUBLuBkxYAkXtcZ9f8LgLSeqZ2RFOEgR1ubfOAC8qvxs0OW1vP%2BX2B2d2R881e4hJCGPbXVAPEDlQAy7nYdAUQvTzeiCsYNAtb9GTYuwAJ2aOe%2BZfdzI%2B%2BpLVEoPfEAKZyWhGvY85H0vz%2BfMnQWyf8g%2BjROZprs3S0TJJWvpx2PowxC6M8bjHthoRte5s7szG7OfJe2ZlzuebpYuj5i%2FWIoDZxGm00ibGHkL0OaV8leiq8HB0wjhCRLpDj5uYxdX6SgEPS7Ct0%2F4Pw2CLNIP%2FnKs9z0MDpSKcT1X6bivdYwJsHvpRYIwUyhrrAVT8wNxaWcCP9ndH%2BbDHUYZpBld6W7TkwzrbyvAY6pgFaJhdYWPNoimK1hgn3gQvxwiYJSkiDR5E7wLO07QbtDjwWXRJc2n54mF6REGPYuOi3WX0Kxhcm79MMoPdPBE1ZJKMQCFq3eeBs1Uk%2FjnJhYiY605wzGftA5Udf8COMK0lF%2FjaozMXqM6STzFhPpKIJfWfuatXLmpfA1wXLaBNO72zony7z2UqFsl4xsW7pJyo37x2YM4aU%2Buf0I2ozfyHDD9Sqv%2Fdt&X-Amz-Signature=843b2780ed6c60e85408697f3fd2e98d85d8f2773fe08e41385d99a6f53031c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBEZISIJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH2vDJGrp2G8tXF6x4mE6%2FBQRzhyqfZvAeYvc3samXQ1AiBy0liUYmWixSfZhJuiVRUTfPPRbrOITJx6LhY1nv3UWyqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjUMtyn7ttiREG1WdKtwDUZ3by7ndQoaoljDYo42zjaw%2BD0tQazPR3uIBtDQreyDmcIXlBmGuetP50tWM02QQfujaRIw7SlqhbqPN4yrcwIuQfxArZ9BLMPBNvrx8Gg9rt6a%2BCzO8wVyxDYI0UWCHvN4Iz7%2FReiJKvaiDI3%2BqwBdl1mNMf2GdePds5kX7fmIQDzvDpExpqkFQV07ZBZmm%2BboWgArSU%2FF8qdw7cn4t1StgPmmprBEn5jX3MnpzMBGgWFaN8ohvxy7nJ2DI%2Fa%2FDdj6IiidhVyvgRCVQIur5HVXrJlkhCarBkDtlCv6f0TZFM1UYJLDVTj3KQqDrxE06W3kvjSHRXSLnXF5kkxIxpSxsOqM9u30bX4QBrJCuSGEUI%2F8M3zpiRqeylEaZmymLrQCJ8vMnE3TIqENN%2B8QWK2rnqH%2BxZyj2V4%2BOdsOU0YlwObbG12x0Egdb45VoqYADcArcBnIEn6uZkfGBjxtql%2FbaUIdpWPqkmFFlR46dJ0gBahFQJzDhSbcSDDjjN7c1%2Fsbi4r%2B2Grwh2UBjLXzl%2BPFW0tvT113MEI%2Blri%2FG49LevcBjYqvsPpYxmcwtcXR%2Bay%2FZ%2FluE%2BIf0Kvt0ooLPYMEx9sVtMS%2BEo3YjqVTd0ouhRDHlhpXl47rXsUEwwLfyvAY6pgHgF%2FBGUXv7qRxwdFVZi4Szp%2FSlG7fNRCZalMo338BPpXyQFRMxlIjLrcgLqJmRrqge4uaUuliQRr70CpoN884k%2B%2FV0fP6n%2BLgpOtY0pvxzKQ8PGlH6jtrikbwnC1ATkLjgXKbXZwha9dDtb%2BVpqrOH1dNH%2B7h1oUOsXVIIdGqjbyNdj9Xz7uhhTgWSziZ0R0GNP669aLSYzxQgMpuFGHelRPYw4mMm&X-Amz-Signature=4005e3aa292c0d5a8bb56d9c2704ce541df5e9fd4bcf6d8edbad4d82f82e5b5f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVMOABVK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9a68pwtFhpcilVVpw4urxxAZEKJpeTwHk%2BuSbrTPGTAiB6blnO8qPFwW7NGU5ySXd%2FdnsL1BzjaqHyDJooirYhJCqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FFd2wKLiVTOFn2KtwD33e%2F8BvwViERcjsQbj4usYoCzkJdYDOzVunqUZbKEEgk62uqvPHyf2O7Q0vNHvUQmz9Hc9gE%2BPeJMU05yD9WqilPgUqBbrNGtGm1DncLBpUcRrKyhAK5PnxPUZuy80n8ghKUW%2F9pT0ceOa%2BxLv%2FEF8n08ZJkhboAByqid6SPboXNS7r9WKoMjUbwXaEo8V1oNgLq2Vvev8atW8N%2B097XQK0mzqfC0sRUU%2BXZyp1an9DovwGMkje34mEeLajXinTx3%2BQBZ0za2MvN0%2Fb%2Fh0ec4t7gXOPe7IJUVEBeCHx5xSscm43dNBywK7vdX%2BDgNhBelvHOaw698gFX4w2gpGKNglr0zdguQekpQ2l57JZSPw96oFTRKYz%2FXvcCFbKZCNMXDj5JHeDxwGOsh21KfBBQpibqe19MTJgiFV7XFs3kXD56ytCFjBjaYp96kykaef6MgSQJ9w0Q6WLVnqlEVlKja1purnchsuMrQKYtDtwoWqGEgwncSfrzrtyxTDwhRqb%2FApPRYRa97Ra%2BBQt7oyoEDpanrJPpA79J2XSkaTGb1NSvjt7SO%2BBus2xrZKqDApDKhPCXRdUR2zSFFx68gTjjEjYPXw9p%2BwdGVaFNn%2FdFqe%2F%2FtdZ4I5sGo20fm4swr7byvAY6pgEKz34G%2FGhxNbBHLxxVkar7iijNLcJ8nSDhBz8mxEoK8Irch%2F3dX6178vIrd1ksHhrC5HpioNxTo9fL58yAAPn%2B6hF1JrBYHU4%2B5Frhtb5z0VZ5RHusuAN5b%2FT0fsZJJ81Rg%2BkNtm%2FOiI2ltnPQh3FZ7moVa2MPvLpdlV5sEh2bk%2FykmlDzZiZ7HpQD5SYhJe1njllv1bCWxOGUMqmW7UO0mHZZUged&X-Amz-Signature=8da3ef9476956fcf7d30a2e1b80b49592ccf92449f0025993c599be0e809bf48&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6OSYGD2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEnUDc%2F5T2eVAmUjNzSbxIKOKvs8dgAPWCl28eB%2BwErSAiAEP%2BIw5Q6jkz3HsJUoNA4QUhcBYOzHh6Uy7LFGGYIeSSqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrJAAQznDwyOwF%2FjuKtwDBUlZ3G58puHJgYtfi7tHLtQHLCQCzJg3L%2FA8lLVkteyJeekh0Rtbie8VnN0hFKijQKdbaRrjfBSagDqc07b4di4HtmNbjLHGXPJQ1ncRzqd4c49RLrO6e304lrvES4zVyvM0H1K%2BbeMGoja57IY26qTYWBR4gmfbg9CREzNAvJDf6UNMY%2FFG1oaVneVckiuWTF1KCF1smWXWAb8MrRSYsISy67YYCtOljISFH7nHt%2FQd2%2Fwin6leNZRROgI5hJcjj%2BbheaRojOf8O%2B3rdnMyX1GBaaSMJWVEQSM1JKfsgzwDulUm4SdB%2FMjz9qoBt%2FXk%2Balk%2Fk0mddg7gDP3WqI4CdMv5iRMx7ctZsL%2Fk05fP8lrm3gqxlkTcHFLP6%2FPP7aCAie%2Bfpi4q%2FxXVXQcllMtOA8uGZm6VeOy%2BcsMDTa6DrlGSANYf42npTw3e45f0eiHEPhaNEyLh89L3%2FojEE2W%2F8W93uKqbDiIb3qovu95eBgehgqttMjOmshsDjdpsLMWXI66C2xQNlTTqbxbBMZKuo5JsEgrmxd29ueEi9hdRXlma7Qfd9a%2Fn%2FZWwQAwf6Oe1EDxWuLPQv1WOOBCo9XOY5yJu6IQrqdiPYTCj%2FMHyhG78QH6AxlGfN4K54Ew77byvAY6pgGeIHexo67P5fKjPEP%2Ffl1yuO%2FMDqX0TaOhucqA%2FKSZ36cbhof%2Bu1KpsQiQQiusVc%2Bg2ergqrBEbnWHjK9iOQjiezhh9z9J20lt0En9l0nSGTV4Ga03F7q3AlDm8jGCDxIUQ0vQ5MxSmrRXLMfIPciAr0J2ZHq0w95e4XtCMs5j4%2Fohfk5wplxAC6aAW9tLsNvCSkX86Jv9nnZVkBbDQfqt6aYNZvwU&X-Amz-Signature=e7aa891c634a2ea98006316c791d3118c795fb1bbc65e9b33390273f6e46818b&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIHQIDSD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlR%2B6DGnBORzzg9Q4kVPUD891TsmmgyDm1OZa6LSgEFQIgdnxHvzCavYghdlMZ8RnjXuwyLBvtdMLT%2Fgz8Wb1yuToqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL2zaNczr1BvtT6H2ircA0myL%2BmxUvS1YrSxO1SejoianFZ4BIQ0I0QWZh7CEnWr%2BJDQm6oJY8zO60AEXznpP%2F2qRlmXoZYhXDviDF%2BAxOFQHs7vctRzHYi2BRcJF9VQu2EcseLeb1V9fTmEKg82cjQKTzp1KGC9dTr1q6fxaVRnB7VptZ6LXJvwAUT%2Fhc0GZesEk3hZ9MamSNY0m%2FDIPLV3X3mTlxFw%2Fyac2cNWoGtEu3JBVErUZrIUKSShN7Oky8HnGXjlYblFFGHMpPbb0xkrCPlo0E6nhHl1GIRoNZ6%2FkWdcNUwT9kK3qfcQG1GSkeZ5iW%2FT7U6ptoZB%2FA6QQzlKa%2BcOH8XdtQheiixPGLd55WQZLMvuu4m6TBEQg%2Fdg%2FrJ5lNPCD4I6c6x0FclEtZDSDoXUoUMY42wp4tt4bBfUYnrvbH2G1d4W1HzNOzctxlUfyp7pJadKAGu5hdHpkfNXBVerI3eVwrQyaVvHeM8qLf29EUGAh2%2ByJiJ96FWqq7ieaJTW6oh3KSvyj%2FPnrZSBDtQFmazThAB1cUCv9cvTHF3Ro3vDEx5KIwajrR72cLhsJMHEJwJLpsebksOLKMXzExNFOwLJBx5SiVXtidoC1ElNesybqAFGLPrtQQacbeaZq54xfAvN1uhhMMa38rwGOqUBlJJIG8Jvjc%2FPnjpKBUPtU9FmrGQW6RFH9Mn1%2BuMiTRAjVhIJtaTpiCAvPuP5B0CNXyjz9ZPygsy7ZVCuWpzRlNYbXFiVoQ1Bd0GAv1jcnDhw%2FEDQay0uJJ9m3cv%2FVt3bDLGNegu1ahGixEFsRoDDz2vGfWq4Fch2cXxKdF7%2F0aD4ldarZR8CvJbyNv8EfzbBUuTlr5Tr98RNeyHdn1%2BtBBYnfBCG&X-Amz-Signature=ef8b2f12945875d2dd374ea975e1984fe774ae9d49bbc2e3409427c5e841e324&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWYD6TYQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZs4BBx4ECmpOIn0zrmdQJbqZrU%2FHVw%2Bhd%2BEuq0PzoKAiB8yTQDGigxTFPT9z3D%2FHtw0kg%2BpCvS4e8sw3sgQ3OPfiqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFbUbZUrm4Aj2xjyPKtwDuzJUdPnaJjklCzgZQ9%2BmbS1%2FxbpDpgf7lfUrKRyBo0mX7tY3%2B1zrj%2F12Jz6h2v6tYCVKJInj5rkEJWgEQyr6Okxpa140S3xtz0mDvpDgE24zOjrZOVdArYVdqsNPPDConO0YYFwKGuyXPBIlHZgjHJt8GHSZ%2FQD4v3drKolPM%2B%2BTjMjQQueZuZb7iI8YSfxgk6meB4RtS%2FulKJicxxqPcaLg9gl7sXscBNZIJ3%2BwlXhZPhsM%2Bco279xlDswkL0J7eIpyX%2Fn8qmHUZBzUNcIp5X8QkoHc8HjuzaX8olHrUL%2Bu6zWvZNUNUUvgRQRt6nbYq6YS84O2BFm9qcpGnVa6085jpGN8ZuUq94eFPdwt6GHnuQ9LhOALMZadI2Rph2alPFfQ08dQf6zaNFrEIrzZBInxMgkV4TskVAiPCUcx1TbPHH9ezew33JOSbtL0teeWAjd9zEd7J9Iu7yi4Z8LnpesjusbX2aEFe8vBBVTl3IfaD0TvK0fFMJ6xZNeG4VgFvUQc7LQwlaz%2B%2Bx3ErWZPNkd3U%2Bxx3S83enNAPSzIeBcQwLo3ikYZHuP1w5ayP71nNkqXDECIY8%2FEJQBzRRpvSK0nnIUhGrD3WdesV%2F%2BdLZfp3kuPLm9DOTLpNRIw77byvAY6pgEyhsK%2Fo%2FyP2LwVzkOmalFU5g91QqBdMGdNjRFibVpNIRIjqsMpUraJdrFzk5kliyJogx4ISoTQQk6u%2B51hhaGCDlhSLgpyqDcpp9p7n%2BQdoog4CJ6bMa13NMHmyJpBR4aVepV%2BgTKHxYDPBGVy42v2%2F3KbamI90c24DptdaE5y7tChjjECEDKiiexA%2FmLFIT2Ew733mrN3pPNS1eb9z8v%2F3QfJ%2Bq4S&X-Amz-Signature=5b58bca219ca9e1ec6ee8b265814d38e263aa38f3e6f5de2b6000f3e674f85dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVMOABVK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9a68pwtFhpcilVVpw4urxxAZEKJpeTwHk%2BuSbrTPGTAiB6blnO8qPFwW7NGU5ySXd%2FdnsL1BzjaqHyDJooirYhJCqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FFd2wKLiVTOFn2KtwD33e%2F8BvwViERcjsQbj4usYoCzkJdYDOzVunqUZbKEEgk62uqvPHyf2O7Q0vNHvUQmz9Hc9gE%2BPeJMU05yD9WqilPgUqBbrNGtGm1DncLBpUcRrKyhAK5PnxPUZuy80n8ghKUW%2F9pT0ceOa%2BxLv%2FEF8n08ZJkhboAByqid6SPboXNS7r9WKoMjUbwXaEo8V1oNgLq2Vvev8atW8N%2B097XQK0mzqfC0sRUU%2BXZyp1an9DovwGMkje34mEeLajXinTx3%2BQBZ0za2MvN0%2Fb%2Fh0ec4t7gXOPe7IJUVEBeCHx5xSscm43dNBywK7vdX%2BDgNhBelvHOaw698gFX4w2gpGKNglr0zdguQekpQ2l57JZSPw96oFTRKYz%2FXvcCFbKZCNMXDj5JHeDxwGOsh21KfBBQpibqe19MTJgiFV7XFs3kXD56ytCFjBjaYp96kykaef6MgSQJ9w0Q6WLVnqlEVlKja1purnchsuMrQKYtDtwoWqGEgwncSfrzrtyxTDwhRqb%2FApPRYRa97Ra%2BBQt7oyoEDpanrJPpA79J2XSkaTGb1NSvjt7SO%2BBus2xrZKqDApDKhPCXRdUR2zSFFx68gTjjEjYPXw9p%2BwdGVaFNn%2FdFqe%2F%2FtdZ4I5sGo20fm4swr7byvAY6pgEKz34G%2FGhxNbBHLxxVkar7iijNLcJ8nSDhBz8mxEoK8Irch%2F3dX6178vIrd1ksHhrC5HpioNxTo9fL58yAAPn%2B6hF1JrBYHU4%2B5Frhtb5z0VZ5RHusuAN5b%2FT0fsZJJ81Rg%2BkNtm%2FOiI2ltnPQh3FZ7moVa2MPvLpdlV5sEh2bk%2FykmlDzZiZ7HpQD5SYhJe1njllv1bCWxOGUMqmW7UO0mHZZUged&X-Amz-Signature=8280f62455c896c86f6aded698321dcd01d736916933f5fb60caa297c7995b9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDRO52FK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGE4%2FJ73dj4YnzMJkSuM74CiuoZeWvFz66OFuo5Q5qWxAiBq7LlYnKewoQ4xNLhLU9u8IggYfiWy8VJ4aJdswgi8VSqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcazih6Gze4k7t0q3KtwD4lIvXbt9OURA4r53ubGC6XWdZN1XD1kIXBMxMcYT5JFnz9bRECkgdaAWFAND0TAnb1N3LhfHdsu%2Biqe9HwdMp3zSwuAaBVylJJ7Z0gI8mag1a8FolJvEmBxEJMDNdOgcjZlvEMqpu0KXvqdojY4aSdtq6yD%2FGgoOKdVumESkFgZO0%2FDC78hQmqg2vW8nEPuno%2FAnSlXYYoahXe57xrDPdRaRGKGo0QFKmpd9PkubE7Otn3ycbEml5g522w9ZU9xk4s9gVGcSBFjawl%2Fkl9t3TDuDKGPDRiMkVvV7xprV4L28cyezFo3u6MqXMlXtgfUX128gx8Rhv0X8yjZhNrS%2BdDghtmDJbyKkf3awldx05Z69fyUN3HVzsGd4IF%2BNyRqJCubqkHHcCuKRlYASOTikgIUBxiF9ORoSnWw74UVrBF%2Bi1R0yIPTpfl5FN7bbP%2BJCzk9E%2F9XGWHP5vHcHHdtHeIqC2yzBzD4BZnPGYuPcDyVEUkz%2BLeGD39WkrtPj7XfShpIL6urGoHEmV8xlSHustU9LBTxPs1Op74gJHYynNwOmdFUQwLKgAFVhClMd07QEtO2YZBsmZnjvdxcD4GMmL7ryg8QLQ9OHB3H46cNqB6bgiyKcTokQjjL9DM8w%2FrbyvAY6pgE4BjF5L6P01rOT2a%2B3S%2BeZJz3TMy9vl6sFllPVbdOOlxj%2Fs5BKo97P2QIIhN6Yxvnr%2Bh8OwTCZNmxVQPuxX92ohg2utKGxnwpIsEVUKnTcdpVgBhxGa0pvZ6RaTx2B6j3%2BHjdsCCFIcCQkGmw6J3oYPYYrGz5EEBK6UfHqUQ8xN9xwpl1DSlO3WGp3I2OdaZsrUvu%2BWyBnu544JIb1pYjVArYwz05%2F&X-Amz-Signature=da2fa522c4397c8252a11327b14e3648f90947f5679509648362e43f2cde79a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDRO52FK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGE4%2FJ73dj4YnzMJkSuM74CiuoZeWvFz66OFuo5Q5qWxAiBq7LlYnKewoQ4xNLhLU9u8IggYfiWy8VJ4aJdswgi8VSqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcazih6Gze4k7t0q3KtwD4lIvXbt9OURA4r53ubGC6XWdZN1XD1kIXBMxMcYT5JFnz9bRECkgdaAWFAND0TAnb1N3LhfHdsu%2Biqe9HwdMp3zSwuAaBVylJJ7Z0gI8mag1a8FolJvEmBxEJMDNdOgcjZlvEMqpu0KXvqdojY4aSdtq6yD%2FGgoOKdVumESkFgZO0%2FDC78hQmqg2vW8nEPuno%2FAnSlXYYoahXe57xrDPdRaRGKGo0QFKmpd9PkubE7Otn3ycbEml5g522w9ZU9xk4s9gVGcSBFjawl%2Fkl9t3TDuDKGPDRiMkVvV7xprV4L28cyezFo3u6MqXMlXtgfUX128gx8Rhv0X8yjZhNrS%2BdDghtmDJbyKkf3awldx05Z69fyUN3HVzsGd4IF%2BNyRqJCubqkHHcCuKRlYASOTikgIUBxiF9ORoSnWw74UVrBF%2Bi1R0yIPTpfl5FN7bbP%2BJCzk9E%2F9XGWHP5vHcHHdtHeIqC2yzBzD4BZnPGYuPcDyVEUkz%2BLeGD39WkrtPj7XfShpIL6urGoHEmV8xlSHustU9LBTxPs1Op74gJHYynNwOmdFUQwLKgAFVhClMd07QEtO2YZBsmZnjvdxcD4GMmL7ryg8QLQ9OHB3H46cNqB6bgiyKcTokQjjL9DM8w%2FrbyvAY6pgE4BjF5L6P01rOT2a%2B3S%2BeZJz3TMy9vl6sFllPVbdOOlxj%2Fs5BKo97P2QIIhN6Yxvnr%2Bh8OwTCZNmxVQPuxX92ohg2utKGxnwpIsEVUKnTcdpVgBhxGa0pvZ6RaTx2B6j3%2BHjdsCCFIcCQkGmw6J3oYPYYrGz5EEBK6UfHqUQ8xN9xwpl1DSlO3WGp3I2OdaZsrUvu%2BWyBnu544JIb1pYjVArYwz05%2F&X-Amz-Signature=adc64d72322801d5ece7b90e2275c400e595d9d1da5dd1aca635394eec6f420c&X-Amz-SignedHeaders=host&x-id=GetObject)
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