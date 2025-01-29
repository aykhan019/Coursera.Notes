

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IJKTTPV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICxn5ilyOxtpRlVLl0dpL93cH8FT3mJ2hVB0vH26ngFMAiBnIIJ7KIReG7o0SgckIM%2FsLKAVDywkH0yweMcZbYNgYSqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9f7JGV%2BvsR04RJzxKtwDhbxS6MlRgnuGeqsyDGct7eB7PhLgA2XISfF2FWARTp0DBcUlrcKpscP%2Bc6gUkPSGoqVnL7x4G7JkBKdxDciGTqmMdkPnFuOqlW1zm7isooSVvRNzsM8BSg8pXOGnHwjIhYvMFMCH7mBnxM01uPxoNex%2F3AGsiq%2FzcbHn11h44S1OFjLpAjzDDqGWesMHULxaMZwGcspoY4Xa%2FiSvsOiaRHrNFX046xVwE3h2qMJFcLH4Jdx1AglakDZppBN4G9%2FKMOqmCLuKtetjX9PsghcC2UJuaVJ1itXRMrYYlG9o7CvFknDQUx5ief8K6XVkbqqfp9q98JZhbJaVyWiwVjiCdetFO%2BZZth56OhVJBW5luM8KzVCVuz1KJAIT2Z9hA6hbAhkBvTDiBNcXnESww0pDo5B6UIBpI%2BtT5En8lAclSfkbEgjpAANam0y136mIN49DsZ3qAmGbY%2BoDcMj0a4tcLRBepSZ4gK5%2Fkbpmt2WHhAjRxx60fRNgoElVJ1XFmbHPyvnPUiKK%2FH7tZHNW2D75HSQtLjrvadNbRiP8iSr0WfyKtA5bk%2B77JyVDS%2B4e%2FLsBTNAG5XA%2BzpnDvN7pmDGVM7Bp01lvuv7HnpkUZIKApqdJ%2BwljXRcv6DK8%2BsYwo8bqvAY6pgEi833NtAISRvnTL3JGtMxnLVtNRkLtQrF3WLCiVARtyiT%2BXtGqRNHz%2BSskflTsd8xaXleOi%2Fhy0lrz7mteJ4lh32jSTnyFL5tMlhJcD5FKPwxWSS%2FNMYSFGRf7JnUSai2wRJXYSwLhGbPLBQZOIt7YDnpF6O5A50A4BZv3vldiFsQuBfABg%2BNeUYtUDxzOPdr7C%2FxkEAIvSmezy6bLfOCs0OXu6QHi&X-Amz-Signature=72f5f41c02b64e920ccff62c15ded586b591f795acd796a832144435b9f088e9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDVYNK76%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtQPrlLMz1hx6CHTakKfVnaXUObbqBQKKgmQFLusixsQIhAM%2BsDk61moHEHmhnm%2Bm17LEXPPQQUvmTMMvIBkwLAZHUKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyT7Z3m8%2FpW51VlBKYq3AMQklMP3dVLJzY9YUTF8KGfT6h0KVTlWhtQsYvYfXSa3CD614hE7hoAiipFVLm5Hf3LpGQB%2Fg4Q86yTtFL3kWOM7uiZFnfzM8bc9xo4vCsVzS6bcNaZmTCPu1NaDVutEB%2FV6HdimEuo4DixTpHFOWKhwdzgAqqQv6V%2BsEMFfgOKJaAYTeRwQkxbP91ZjgIO2cbPKq4jcaLzMqUVmvjNntqKDqcaaUN2gwUGmQ0Utm9VV4mIo%2BG8%2BWSPurmvDQZ1wP%2BSi7%2BFMPfnWK4NoZyxlXQLU%2FaedJg6qTvW5TAucyZxuzNGDUm5b0qF9yX5CWgj6vs%2BPCXBicELH0jFxM1d88I0Wwn9MKUA4NDNmhSWTZHEh3HCk0%2BD3G9ySLBL1G1jqfgMXmomaPhUKfB%2FIP2wvjPWSEEAwz37YvJLgS2fYB2VDIzd%2B1zp7ofa%2FLYCRAqu8RC%2FpzJCdOheBUhk32RA%2FS1fgvU8R5loZ80yKAdoCHnO5vU7OUHDwyoQHgaB63dDaZwHTSNxvecQOkPypa5sKOTbJEozStw2JANkX5HJ2SE%2F44j4kVVl9CIa7ik%2Frc%2BX%2FWHN%2Fa7m0zGgKZngqzBqjvRmXf0kXYUEjBYQEY1KTYUMHw5cx%2BH2EkP9dK6LZjDVxeq8BjqkAUX8gO1FFFvyX35k1U3D937XWq2%2FsRj8HWAJOb32hIfQe62up0WItORdUa1dx0UBFnbsYF4j8o%2FAJpg%2B8YghEBw%2FHBLiRGlNWT0v%2F6rmAnP9oVnBl86PgvTtDbnlYlsT7eFk%2B2qWY7IVCITaXLb8V7vzD%2BNYeA8j1RZLvleeNcvZ1PMPTGgG%2Fvmpf4XSFac2fHNImiLH4R4ksMMHI4vKlX2%2FMSCf&X-Amz-Signature=b52d531b37ef570916798c3ff6e9063d9474bf30e2353aaec49ca95693b51e60&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV4IJAFT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGP1u50lJNNSwvfl19T%2FbmsSiyHIIbpYNBdyOfF9P2UtAiB4f2yke9gs4K6oTeuvmbCZhX5vs9%2FJBkwV9R0bN1%2Fl8yqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZgjWwOtopn493KSHKtwDfKGKlWjRaSxMLvHR1ICP%2FgBjmDBnTlqVQ63v6dSLloRCVudBFU%2BDrKMR0os%2Fo1txTNjXV0kJOD5ufSRGIVeOjJOyhAlq8stZtJwRRdU38txUOZ0%2Bhko2OvzGhk7ZlgI5MkG7ZCqdOQrAR9q4PXqnmabhdY%2FDGVf0IqIerST1CVaTc0euuhjNCPk8p3DGs9CVB2rb3NJbwUS3VpTwkQbAsfW08ko%2FfzT7fOc7Sfp9nbzPfrFq3GdKdXTj98gZimm73L71urkYTlHgnb29RzWt6wFaDQpyHBXVm6Vfv0RCIaHrqUndCNsO%2Bh6E69lv3RTl%2Fp%2BlPFKHC1V17tUJuBNmqZT2fHr62%2BDfEIw6y1GeCWwHYKh0FAPtaNwC8GaToXgA7hXGXGUED%2FBoNQoNsc2dn%2FgOC6mAUtMUPv8bfl4c1fuS%2BRK2WixQwDC%2F0JJQXbbpzt5AwsDrtOfqbtcJbKkvq%2BMFoSBMGghbF7FmXCpvEUxOLHgOWmqE2I5OrlPuQF6UR40yDUd8%2FMft7HojW43U0kMgMrkPpfbXYhlGMRmQOvsPNWZnP0d0AlbG9SaNN7PMz65cCydYufE3ALw7i%2Bj9z40affZIh0lg%2FzHxhuoIdkyReQXIB7Xi00qSNq4wzMbqvAY6pgFjx3%2BPTDieGE%2F%2BcErQN7TuCbCEqkM6Y91%2Bf1liQfG5Airabl7y4HMzcVDq02WCsAT1HOQVYiABe37k%2FypHlryQvWeGIFygvTvRlLvGdtv380U7UAHHJDZuqfdDaOVWCN1UjN8wlZXofUBhXhaHtD8xjpHZC0CKtTt8%2F9EReaNFd4m8XoZZShg41cxX%2FrkF6e7%2FIXmNz6gwU1VNUFcICmPSt7FhXb3l&X-Amz-Signature=018126ac266182be0de533b78429eabe36925c7262d736ead972e73b6b5a3bd6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TRF2Z7S%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETVOAhUIJFaxPS6hAy4Q2J8Xqu28KjGDxydwy7kTq4KAiEArx4FpPbSgkhGEAB1MDR%2BKRjS5oniinopdpRwt4YE7%2BAqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGM0%2Bum9%2B9N3qsUIeircA6wqhYRKD5RBbnKM%2BDE4HNAcrXBSFQKvnKIYmiXWq9jHEDU89srzYuNDcUNK6TNdnkC9qd5eyxyxn%2FqzDqn6IoSGL%2FZ3yh4fBZEJ4hUiXtQWhsid9viict8uhFr%2FYk5UETo16fL9akpRiAyqa5X%2By6mLiQiUXMFEPYhWP9RagGGSgrkev45m0IBFl35203EBcGicfZJLoPEUjjb%2FaPvg%2BEG8%2F5E8Pq9OQNw3sa%2FN9mChh6AhDTbzA%2F0FnQRAXQTP%2FHuC6x6TS4FM6n%2Fxdjt92N7UzuPQM35aXW%2BldexCvjmS4S6mS28ZS55egLKyIkSFAeyxc8iK5TzQ7AzXc2xTqRIY7k2ADmnxpdBbNZw4eUOltazpWi1%2FkPCAj2I0BlDgSsR5erkfj3p747c%2BqwOCV0J69TTcjvgQG8qxPKjOuYc32HiDJ6GJRqoz%2BKbzCvztnplGuMGEp%2Fc0QKiwF6jTdGSgZMmv3Td584se1XW55fe2eneQSHOJc1bonobxksmE99qLFpYNn0HxyF1Mjh4o1EVoK76CyUwpUTcQWaYWxWGoCcMm8%2B94CDYuQKBK0GWsPBML%2FlIsEUEXN2oFDdIA6QKglCc6ebQ8ceI3Y%2FGWzItRjT%2BIWGm%2Fl1l3xyFoMNfG6rwGOqUBETepmgOfCITZ9gZVhjrvlvhN0laULZoA1nwJ387qheisRzawAcQR%2Bxo%2BgxZHKmBSVqS2V6YEkmzeGriuzG3Y%2FvKbnVc92RmNqkd3mGgVLB1ya%2F1raCrsOQZb4FuCzQyY9F07gdPqExYNpDl7Is2JhlfiNRaBBlu6RIvsGu%2BrUCtwECe2B19rvHQwfntPQWQD1%2F9qLgg2%2Bs2lhdYt%2FeFgl%2FgpA6OS&X-Amz-Signature=04151852fa7e19e42c7e32d738c02f3872e15d3567154cff1a903808bb3a630a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRNMG57D%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDg7iD6S7vICAGRpYxixdZesHYZlf0tPl8KYK%2FQNALsIwIhAP4d%2BqP5ofDatZgw%2BwZTtpkjGQVPlk41Th4zO2ecltn1KogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxC7UHqt4u8p%2F4ncBcq3AO43DH0WW35i7Vjf6bLJVrbcycXHdi7TvgghwmdYM9ZI%2BMfj54UDgLP27iaY5v2zvgfa%2BeA5IaVld7b%2Fr%2FOj2w4lYoUMO9Z4CWPwEEBrmNHWKrjFEQBie9Vh84b%2F11suGUhH6FzWGQzL3hN1y1tYl51tb2Ibs1GVJtQ9t98ZU4j7mfH%2BHD2cCXuDnDhOhefFMe2%2BRYLetqPtXDDp4AB7PIwk8qA7eDlPH%2BFrNYeZXYPiINCXukbeji3VTd37okhqqp9IkrzCy6NywIJpXSvWB%2FPcofBQ1aWr07GG72h5xF222J0JdAb5zKEmIp%2FuQuDosa%2Braa60dGr8GP%2FBFsj2I2Hx7Xx18xd8hKptSFBgBZLB9Q0UJaqDUaYhSuP5Vzv%2BMRc6b%2Bgpfw97bkk1JEFUPzoCHL7yL6BDnEV9rItc%2BoFG2GUEnC7%2FazHGAmFl5uY5OnTUgVlDN44LrMZsOaCn8eCkPX12oWXZCzixw9fnz8bWtU0hKCYvMhDE9DcjxS4XcwJTAmh2xVjDZJBnp0HkBn2BDJq4C8Y%2FH41J7HCU9s3WUFpubu0ag9LdOa5YoIrwjuLDi5sE4UWzKoAn87S8RXx9xO8uDjoeZ5i2jWtrFOw6N8HqSFT%2FUCH%2FvBBzzDsxeq8BjqkAbwXzBCxgyQMVjOWLfQceI1sJVFNVLxIrtIDryma8nNWkC1AXKkNBtDL%2B%2BdSqsdRDfTUe29KqShKg4vzRMPSUBwhP9UOt4TDkIsvG%2BvDJaEoV44WQaVnWXjxDLiDGR7Z6rpp3zTVe%2BQz%2BxdOmL88qOXJAYLX5XOYCURc7FgxHJ7C%2B%2FeZSc1m%2BvYCBsOU3LHo4T1VMxVCJs9CV9%2Brf23duCd0NS%2F5&X-Amz-Signature=db362766e0a8d9d461b4be857fa2241c6d4d2d02e9a90d135f5e440f25b1ab0c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZRE7VYU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHnn8YLuw8EQ%2F4IVIRxx8LUyPgnjcWsyRiG3B1H94wXpAiAQFgYmCUHvlBjaD6k8RRjMV3VelZ8eqV9JWjoI%2FrfctCqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8yiP64rdeQuWwlCAKtwDM6wcO3zKq2T3JAVCCDMXLcA%2FqgfzixcqDb%2FB4wYcq%2F8FHQK5g5I9o5JRIYLb3HxQ1ydNcn6GFJS2H1p5IX8Qxk2Gdm94%2FhZNbTEnw30KkhOCEr1YPgvMRIhaWY7wPsvo1tIuuYB%2FHhf8OxL1lV6LKYcY4e%2FEtwRrS4HZllQcyeT227PBZGUofTF%2BQIXc60sFMqGAVQbJMxlhFWoYp2BrzrNWAtq5FVNoGu5cWpAS4tNoNO7%2BqohY4jOCNLCeUzZXuWA28uaRhsJcSvPwHPe3GPh7twneV%2Bya6f7WsNYd2qgqs9t4fcyzBs6SNMnwU%2Bu3NPOo6LooIG0J5f3%2FKrGfaED8oyj%2BqeJTGIqgE%2FrhjzlZK0y3oOMglzMKyZ4cyszh9u29JEq0NMswy%2FlBQ6yVk7vHefASk1RZ9nVfXGjSVlL0Xd61%2B713NgxF39wx5Or%2Fybh7a5Yddj0M7wZWnB1W964VG9jBqx5Qi4yYrC%2BkVaPVhNvSiwR2GViCplE1fCBPX5jIDpKexRM93YhR3vVH7Eo35G4l3LHwcYh7zqHncZ7%2BMoNYlwPWnEzqhvWiEQ3PtlBenyEb9R%2BxuUkL0xqxFbbhpqeqG6Ry627%2F99uRXpM9L7r6ZvguzYp3TPEw1cXqvAY6pgFQQq8juEU9tDZHggD2ZOdw%2F1unKBFFBCE%2Boab0FDoKL8Lq%2B8oMS1pn7dFmtYHNLGSeWOV5fD7%2F%2BFpuy1gclTUE%2Fzna%2BEJwgTw8p2cKUgC2cCFbOi2etClPwQvdcMm7bXr7xLfbldtEmWRU8C7bGmnIp%2FJ0iLIyt1KLB2NbIYOiMfrNnlq92WrUMdED5cUKpPFaxUkLEcZcLGw6FApKJwI9aSo4yd8J&X-Amz-Signature=e8c7e0abedc301ae9999733ac3fcc7a9b9bc882b4ae076ebc49fa6ffac95f1a0&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJSNLHZH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBg2TE%2B9SL5PN63tlRI5Y5kITpiOCyTYYXB9QnLiERhwIhAJovXorDqrT2T36rQmW31M0Z6iq%2B8KA7C%2BT0U7FPGf5MKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwn6eZuEBNopc3TVAsq3AMj77vSuCkArIFBNUUgsekA%2BHAKz3mnIFbs7GaxBMT6nHoNpPUJyfdMYhOYUCaSah4Hz2HYi36gYcRElvYqeIiU0u25nbWkItgcvj2msS0cYZp3EqdylW9UEZNyMv89CpHStmRcQoyB0eoLCyMgkN0L1RUIUJwVPVT08azPEdozGqec%2BMwypc4p2lSRIgh7tmzpZ4UdYMsE5cMrcL3YkKUXpW7u0%2FtSkReZzKM7B4fDQsHtRWvgvXlJuLtyQJnu9Miki6Pi9nwGBX%2BkI6TwlZAnaTx4Jn5Ocdhf5UAz2%2BmDsIOsh89MuMsP51Dqbj2KeM%2FOaIcgSgLxFIFs8Ale4MD7PXFbFuq70R%2Frr9LyR8YQuhf82o5YwdO7Tt2Io3f5zSHxZj21TWN436GLQ79gER4t3YVmqHAMxcpw7D0f1g8ycahC2CTyyb8Xpxh1iSJZ3W9AuKhStE7zExWw5zmdiNrkfv4EIuT3MOBnURAigoZ3PKysDGbcacFYcT6qeI2UR06qAUNcB2cIdtL4FucOt0C693jWKBLNmYeGJdF6w6tAogy0KuxTKhoDK36CB9G9Es07hnDgyE%2FCBlcMDDbNoBOslOSaSik1JX9lvcZYZwM0848vs%2FTUqkNLVufsSjCzxuq8BjqkAbvkEengDikgz0Kk8YYqL%2F0WfHO5bIHLq85Nn3LVknyYLIzRdTWtqCObDtysZ8dTA4lLSvPmYTNl3XKwCuiu%2BiRYTMwMQ0KEquPPnv4IM6Kges%2BDBqV%2Bt4YN5RNCSMI2uw3DbWgMaA8UjGrr6hTZ%2BPCpC3tSq8Ff8f2uF0FRjzFOVq%2FEyYSrjaS9OTKjE%2Fo1E1x6cY%2BSsu7%2BXekOG63AzjfMcBVy&X-Amz-Signature=82b4fa5e5cac670b3a117436e155fed4b5e3186633f28025936b74e52c23e9b6&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REGT2STV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICBxnhV3qZFUdn3a7%2BqqmB5CBayG%2B%2FP5944Chk15lO26AiA7D5VX6SxY%2F5yrvMbPOkZONhLvKyLIkZk%2BD8QvHWlqCyqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtt3OVF4%2B%2FDbXTXKmKtwDMmxTn%2Fq%2FUpVujanPX%2BXx7OtryCmPLdKI%2B885a9y0ZWBPp15GHiDBuWNCtMB3ugKR37iCTjZi30HSZq6Vz9Bh6oLjFlVlzfLNnh0QpglD%2BImH5Wq%2BHJhG%2FPqrDhdt9%2F6Gx4kk4ACcWoxb4Vh%2Bn2L%2FcTSsRDOVoiq61hqWMv%2BSl0jRbkrzywH0THVImaCL2mBd35oBqzDvGjE4GFbICQWhMyDmlx%2F7DG7b0myvbVt0q8I5afpEpms4wFdCIuxoFI5Obms1t%2BfzU%2FixI7TaGKjdMbHyrlMvRJmtMuKjehrvW7%2Fmw%2B3ljJl%2BSSN5LOtRZV8D%2BuESmONcE3DIubZ5y2ljkPjQ%2FxnQOKCiNuV1LaVM94bd5TnimoSSNDgnjaqyKGZPK2ITqp5lt1jr2tAGayshOd%2BYK16gCUkm0FoFCEahasTKlBzUx9tOSUtmAUpZD50nFXe0WcAYLnWhCJgE0GJJQWAEaufrqTMZTjgeBqakijAX50aXZI8pA3G2kx5frfninSuxEAnm2JKFEmnjacUf1gi3ouPAOaqQ3cXmpvUTfuVrM2osD0OG4B70cqpDGLkEW2eV7Sy9va7aYYQnj7xPZ5AG7FZ1kcxORkB2yqH5gMPawca389u6lA7BHU8wisbqvAY6pgGvbGyoRjuB1wlSEJ5ZF%2Fajgo4secIE%2FLjgX8dNn64JClqn9FNRXAFAmV%2BiMrhG2SKJoMIkrseWpdpeNmzANt3Oha6hgkicXK%2Bo35jGEJrThT7Tnrgj%2ByJzeY2pBXOD2%2Ff8UQtWbHNnevWPYP0U8dzIWIQk7VKDaAH%2F1bFqrEaoNg8%2BrlErdSTIhXePFGmerIEMafcs0jOmAwEbnNyasqO1ak9s9q4X&X-Amz-Signature=25670b0bcbe7e280b1d10b906a9efc0f20704319d6c0a99fd8993abfe3bf1687&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRNMG57D%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDg7iD6S7vICAGRpYxixdZesHYZlf0tPl8KYK%2FQNALsIwIhAP4d%2BqP5ofDatZgw%2BwZTtpkjGQVPlk41Th4zO2ecltn1KogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxC7UHqt4u8p%2F4ncBcq3AO43DH0WW35i7Vjf6bLJVrbcycXHdi7TvgghwmdYM9ZI%2BMfj54UDgLP27iaY5v2zvgfa%2BeA5IaVld7b%2Fr%2FOj2w4lYoUMO9Z4CWPwEEBrmNHWKrjFEQBie9Vh84b%2F11suGUhH6FzWGQzL3hN1y1tYl51tb2Ibs1GVJtQ9t98ZU4j7mfH%2BHD2cCXuDnDhOhefFMe2%2BRYLetqPtXDDp4AB7PIwk8qA7eDlPH%2BFrNYeZXYPiINCXukbeji3VTd37okhqqp9IkrzCy6NywIJpXSvWB%2FPcofBQ1aWr07GG72h5xF222J0JdAb5zKEmIp%2FuQuDosa%2Braa60dGr8GP%2FBFsj2I2Hx7Xx18xd8hKptSFBgBZLB9Q0UJaqDUaYhSuP5Vzv%2BMRc6b%2Bgpfw97bkk1JEFUPzoCHL7yL6BDnEV9rItc%2BoFG2GUEnC7%2FazHGAmFl5uY5OnTUgVlDN44LrMZsOaCn8eCkPX12oWXZCzixw9fnz8bWtU0hKCYvMhDE9DcjxS4XcwJTAmh2xVjDZJBnp0HkBn2BDJq4C8Y%2FH41J7HCU9s3WUFpubu0ag9LdOa5YoIrwjuLDi5sE4UWzKoAn87S8RXx9xO8uDjoeZ5i2jWtrFOw6N8HqSFT%2FUCH%2FvBBzzDsxeq8BjqkAbwXzBCxgyQMVjOWLfQceI1sJVFNVLxIrtIDryma8nNWkC1AXKkNBtDL%2B%2BdSqsdRDfTUe29KqShKg4vzRMPSUBwhP9UOt4TDkIsvG%2BvDJaEoV44WQaVnWXjxDLiDGR7Z6rpp3zTVe%2BQz%2BxdOmL88qOXJAYLX5XOYCURc7FgxHJ7C%2B%2FeZSc1m%2BvYCBsOU3LHo4T1VMxVCJs9CV9%2Brf23duCd0NS%2F5&X-Amz-Signature=da3990a8e78bb9644c7408a4522437fdb732eaa457b7396af530a74106cdfec8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BFKCECU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqiO9HfCrGpfIvY0o05E%2BqnSp9sfKO8MzVH5FTLeiiMQIhAIOYUyLpIT1Ui2o3H15Mc93FixzgxJmwoCImlQO24%2BxaKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxueG%2Bss0SzvmDCBU0q3ANOvwAthJNxcEzCXBmxzRpL8JDSDow3K1O3I%2BVa7dxQrK01KKR3EbOIbFSaZeTjuwrViPFscrmr7JdoQLU4PQXYSmhwfnEnXbGBCvFaxgfaT30%2BiyVz7tt%2FR8fFgxyyaGb9ulAM63eEEPoDQflOK8%2B1hr%2FflE%2Bn4clxuyTgMG80R6tBslzJ130j6I97pq%2BTZOzPPS7ULbjVPJzmuONYRMq28FuqMWWlf8MBRmfugewh5ygh0fDlCAysdnUX9vj8jaPHMdEBJFIMPq5F5ZM8vRzGrz4zuCjmhGQMzt%2FhMeAc9aPMUiQ8A%2F1vjKjOXZgi%2FjcApHzTlzwUTMOcSy%2F%2BHGki7enwBq4C2ajuD6RgFgXwAmVtPQ7z3cpkzv1B%2FO8z%2FojKbMP8j7o1KzeiJMtjPbcAtuaEPd0Wwrz0A75dqOIg95IFDBGYn6UcBP7m9Nb%2B%2B%2BrH%2Bi4JOwok9fHaPB99xTU1WRf91ix%2FiaXX7B%2BzvekKVRnX29YOlGXFWutq81LBULAafOZFV7B%2BEZm98MoUhCWnMez2sokubN8Rzwi0Zu04XiCSAUMBcMBgk%2BdpU72gHqsaUN3MiTw4WZLntGB%2FCIQPXz6YJ3bvmAfn%2FCTOL77Pdp%2BUDy6XuhH8QHcznTDqxeq8BjqkAdfVklN%2BzWOisTsI3d0u40PqKLH50oTQkzbtpLl8ajSPCi8RfDXB3oEhe11tCRV9z378P4hbITi4mzVHXmtT%2FDhNl88vTCxq5wQZIAUg4xli%2FVlizwYpLS0tZffxZRhBtzHJzxKdktkIJZah%2B0RGdg3fnk8fKgEZCUc1LaktZc4HVM62xXwFetHrdw%2F1%2FFiDCzZ2baVUuqbyaGy0Rp1VfcLft8mS&X-Amz-Signature=dbedd97002060997e6eb6dd12f27e8b7f6866ed52bd4eb8a5d01cf3d1013aeab&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BFKCECU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqiO9HfCrGpfIvY0o05E%2BqnSp9sfKO8MzVH5FTLeiiMQIhAIOYUyLpIT1Ui2o3H15Mc93FixzgxJmwoCImlQO24%2BxaKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxueG%2Bss0SzvmDCBU0q3ANOvwAthJNxcEzCXBmxzRpL8JDSDow3K1O3I%2BVa7dxQrK01KKR3EbOIbFSaZeTjuwrViPFscrmr7JdoQLU4PQXYSmhwfnEnXbGBCvFaxgfaT30%2BiyVz7tt%2FR8fFgxyyaGb9ulAM63eEEPoDQflOK8%2B1hr%2FflE%2Bn4clxuyTgMG80R6tBslzJ130j6I97pq%2BTZOzPPS7ULbjVPJzmuONYRMq28FuqMWWlf8MBRmfugewh5ygh0fDlCAysdnUX9vj8jaPHMdEBJFIMPq5F5ZM8vRzGrz4zuCjmhGQMzt%2FhMeAc9aPMUiQ8A%2F1vjKjOXZgi%2FjcApHzTlzwUTMOcSy%2F%2BHGki7enwBq4C2ajuD6RgFgXwAmVtPQ7z3cpkzv1B%2FO8z%2FojKbMP8j7o1KzeiJMtjPbcAtuaEPd0Wwrz0A75dqOIg95IFDBGYn6UcBP7m9Nb%2B%2B%2BrH%2Bi4JOwok9fHaPB99xTU1WRf91ix%2FiaXX7B%2BzvekKVRnX29YOlGXFWutq81LBULAafOZFV7B%2BEZm98MoUhCWnMez2sokubN8Rzwi0Zu04XiCSAUMBcMBgk%2BdpU72gHqsaUN3MiTw4WZLntGB%2FCIQPXz6YJ3bvmAfn%2FCTOL77Pdp%2BUDy6XuhH8QHcznTDqxeq8BjqkAdfVklN%2BzWOisTsI3d0u40PqKLH50oTQkzbtpLl8ajSPCi8RfDXB3oEhe11tCRV9z378P4hbITi4mzVHXmtT%2FDhNl88vTCxq5wQZIAUg4xli%2FVlizwYpLS0tZffxZRhBtzHJzxKdktkIJZah%2B0RGdg3fnk8fKgEZCUc1LaktZc4HVM62xXwFetHrdw%2F1%2FFiDCzZ2baVUuqbyaGy0Rp1VfcLft8mS&X-Amz-Signature=9f611ad309ae0a3b2696b8ed351eb3f7f12f7ae1cc7c2520d3d4945f0c08a7a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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