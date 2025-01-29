

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663E354F3A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Fpr%2B1VALq7BcOTZ75QTeh8U4GTWduHlDRh%2F4WgFH41gIgBNb%2FegzAC4K5LL%2BznraNUszdkfv3qscYyzuCFkeSJ%2FIqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHROuqXiTcowcWXgXyrcA5ieyCGMxUcL0TMJmiHC%2FU%2BRp1AtKnvaWq9GLC3z7i7VbJ%2BY1XQbTWaz1QX3htxaELaNO%2Fbk2qKq8EvaVnOMILvuyw%2BF3OeUfhNZTe5qiBeLrOxX1QPcgoNKx%2BOgxq3Lj2fEwBKv7a697pibNa1ORG9lsjLT%2F%2BRws%2B6WnnevlFnC9wA6xSm4nVgTbJC0Ty16t41tCr1GKoxDsLW%2BKSLTUtaOXVcbFsvxbFj%2Fe7zVDNfMQmrCHII1oeqN6z1F1ziQbcj5JEga7tJBAvgDqEqh428oE5DRyzUNG5uTQ6ZZLWI65zDwhFkoLOW%2B8WeCDgpktjXaG9YvBjJjR5%2B8ZGMeW2SuXtmOCGKCWbyC7eOQBm8QnQIW%2FWZpPYa1M%2B966w0Lr3VDVwM3qRkOO5KTKZ8NjDUoKM93TG%2FZCjQCCffRAyZ1Fl45lMhGV5%2FDHYqRlujZ%2BAvQHvETZ5Ga1KmXoTjULHDY7QCxYMu5fcxxicec%2Bk8cWX8OHRlabC%2BfVUtp2qOk47BJFyrrrlLcdP4DMNiD3rCEFCWV%2Bxx9r7hxks2mYwMPZhmgRuxURNZeCGMLz5ohlE0d0LuozeNDKe86aS4r7dNYs88vQgjZ2DFEHuDkYC5BCoqq%2BEckOoOizHCZMOHY6bwGOqUB5xioqXBXLxp2C3mYuox1h0gOcvOmxQgv8rhFHX%2FYdQkdHI7xSk0%2FqpoMR4a%2BDdBq0vsdhmP16oBNcHjtfNYh8zV9r8e6iTA%2FP8GLTh6jOiDWIg3KT3sqiXb15a%2BVyQpiu7zenxK5KMIY%2B8s6EH7bTmf14hLlsvfcTAU0MW53sVRSyLrtCuLok4kOGuq%2F%2BvNkaQF0L229MNQX1uPpuAIb1qwcebnH&X-Amz-Signature=8f772724033726109a47cc8a44ba4ad54d409313adc079b8075e3961c0beddc7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRQXE6C5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJos185RXFkSsDqM4HJxnTVV%2BNV%2FmjKXowP8PtfqUaCAIgNKdP1ezCuiIuba5lLWfARrEu%2BTX%2FrUp07JVnp2dKoh8qiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3FTnPk6P82SEIXZyrcA2oYtyEoPv7%2BPigh72GgTjaNlJl363oxgjSspqbYpSliYXlRFiNMizidvTd6xjzJg%2FuB7uRWRliQaaC2DdhxkkH30eBriLs0Q9qREFiyCmFl44wwSKkK0uyRpSaZT7s8d8tZgMrEiG33gY2ryUJRSWB84JlL355uk7YIDzuGHPkM9Pa4fwDPYxRB%2BwEPnzOT6SIbjUgYUN94sZKgK1DJvKwtZsgVCOPsNTgZYCabDsYE54ScQeI%2FkrljuzEW4gq7x%2Fbd4mpFyr9Zwq8jUbA5FKVmQKPVqU29owhtAytI2hlGX9BUTqCghyGB63yof9kRaPPJ4ZNvuZZPmQoVqWfYQtPWEdsOMaEjJvmWg6tXhbTDxrSAmTYqCAnDmd%2F5juT5H1qICBqIQSHZfIVCXh14BUZDzVl2h2YMf3i4DxKZbO5TY7ji2k8TPKKiSQPHQqMqBjASTPfplVn9wPJSEo%2FWRxPdjmvIrxOBkI2judPZ6VgkMSP%2BdFh2EJ6tj4E1QMSFi2MpR2B%2FmTAfWM7%2F5dYZY%2FUfJbyXWVLmEsGsnXTQgYyjp3ok1aNc1k2NZuMueOqw8MfZbwQfbJnm1Ygb9%2B883iR0gBf6fOBjwgUODD%2BVDyk6IFbVDwfhXV8mamK4MO%2FY6bwGOqUBkTWAZ2ZB%2FNSxLUq61CBu4vKdP08guiIyz407A07v1uKpfW92hfVwPOn0vZRlbOVBOT3sUzxZh29VkEKrE2XsSVUkmHyXBS1FZwqxCwwksG7rtuLw7yjEYpSvV5Hki2RWuuKDJc%2BPACoM018zCbmh2xQYSZdiZB%2BZO6uyKBO4H15FCnwyQDk5s3aZLFtYmBH%2BdYy%2BaHd6I%2BYEsOYvxCY%2BE9S8T3Zc&X-Amz-Signature=ec78a997734760edaea93e5670ba318850a5cd2bdcd547880db5a318382cd1c1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM6OYCVR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG08YuQK8WND5Wyffx3BaumguhKIMiXvkvIOnWpLJUOxAiAY2cjAr7agmOE8k7kwddH9DhCDHT1rk8rfAv3TaulcvCqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAUu%2F77m%2FefLVV7m4KtwD0Nri6sKSAvA5b0l5EAWpoDvDrqzr8%2FMpJzGVyqgjBS9OkAfFPnmLWbkeCcuv9EHFtICcetacsyuhMB3iKMtSxkZiAN%2F%2FVo8Otmr9flpYCmn9mkZ6I%2F%2BZTGKhhRny5vL7ncQ0%2BPhG6le1e9a2WqCYZZ8dwNAEp8egPz8wpeE1ls5t41jURsEfXiiMzYZYQT4i0eaTV6S6ZArYwA%2Fmm1yrmxoBl2Bri4dwrmebUbMdRseTV4xz%2Fa3TC3BbMSclwtBdkB1hQb57sW8ndPBrzH%2B0X2rYvHNOPpm6lKDnD3bmP0eT8HqEfNFEekPwcjzlG%2FPZNnrpGTXSe%2BlL69DmhxTQBoMaCTDpVJE%2F21gouGgTE9bdBWktU76XdVmfcWbpRTMjDBFogfbEUFkiKNxC2p%2BvSFABMWj%2F8awOrd8Go2EE%2BSTcxNDTIjSAo8ypm2dmCFfpHw1ZHZo%2BRSOmvLx2Hn9wYpf6GDMabJA1l5SqYC0YUiDJTiSBjNKGAjDajvrbqZXQdHxqB95S9SCtjNbgqgKh%2BVa%2BnfGWzwbBPtxM10QpXyi3ebf2wG7KkaQzfyFrblXVeooeAUpkW2Yufk8QWHxu70LZv1mU5yJm2221oxkLXy75RBzRz8l1B4O26QIw4djpvAY6pgFzE7ss8eMMioxKAS5pg%2BSINWBx%2B5uw6bCqvU4TM68iSrVTKRBoll6%2BZTTNBSqK2PWGmguEVt7c5a8zGIvQvCUP3lVmyRi50R6e19duohbkBIjC5vR9u0IzsnxEuM%2BkeC0%2ByU6iw25hq5RHgn8aVOCkzTSfkYdm0V0AHmJ82BEq4fZGshEOQ7I588W5KvGN%2B3VCKqxYJj4NBYjTcxVKG6iSUms9xYto&X-Amz-Signature=0dd587e3fe546bfc2aa36285f9213d352fcfd7921f2de3b12fbe44405e3d7ca8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645S6WTT2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICIsXp0raSTpm4xT%2Fv3UQ6jRYPI%2BcF12di8aup7uzdWZAiA7yLFoMxfQbAJrZxot9oGUd7NyXVznQaYXpQbKCya7SCqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTrtP5cs%2BE4HZvlUaKtwDdQjxygunQBcm3yfSxqTc%2FGXY0cGD9P9qrDweOE0%2FNQVbieTJ9tLstJD5Ytlq5J4tffDkrVIh%2FH%2BUbG30z3lyjU3WHubqLuf1FwazHt5qk%2BJmvkfl%2BuTAMiZVUpTwAwC7%2BMCdSdePrJmErRwWYzMDH7uv1vG6lxRcbQEcxZs1CpGzzk0ugygKaRnuvlNHjEzG08hm5PrrO3Kn7geO3wfccvnN9k3kkPEEaB45PCbVmiDJl8IialmzB0FJ4Soij0JAgWeaNnf6hpieDubVv3eJILG3s%2F5iycsPALry8iGR5dTJKCueOskZsIbEWeWbcb73zCcIxa%2BloHCT%2Bzzhu5J09v5eNvkfbmWxAuK1lQCiWJr8QYw1wHtYrAKvSpCcGutD%2FPkcMnBMU1WJru19Lu0uPxEyGmEMnJYPp3%2F6EtuEVP801QGn9fO6COXGBodvPKnaxyWq6hnJrfRUIbK156vomPX1wefCT5Z7sJn2WWJJlzmq%2Fo5MIypJ045LygVTQQdhO41air9crFR6tGLDYFLs3WdrNK%2B5UFVwUgB4N0LSRxHV9h57XDvt4GdELRlfqdPIIKTXj7c81yRn5c9lBLhofGxxa0f7YCJWphbVByRjNZPbOBdAArA8qHhw6iEwrtjpvAY6pgENSbLKbmC7WZzGKrdFvMlV%2BVKdVO%2BmfbrdnYOJxx5Ra1uMbkRW%2FBg%2FMaBahROXT25K9Il9LT9UU6Am2y7TngUVVawsF1Oyu%2BKrjq%2BUSKxsjBq9a6EagudX8GMbtH%2FpKCIpOcAOglHRW%2BlMfg2xDA7Cf%2B41cJTuNj6D1%2BOmIqEmTBZdDbE8%2F6yT6h2xdvbNHsvaFGOeIpelqjwsiCzdAuZFMfcLJ5SD&X-Amz-Signature=767fc0b7bd93416b2538055d0936652a530e5d92ba0a3636ad93ab9189e59ebb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XK5GUR6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn5wvKvCTVjRSmLBmo2sn4x8ONX379tzVcnFe0EZDVXAIgeyizo4VE1isUSYvvq5uZqTiwbAhODqkOwjGSC3%2BTIAgqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOQA4rO%2FkwcEm962yrcA1So5mV%2BqEICjxkYkjTA3EQWmz4NAWgDL7SwR%2BknuP3uQbITCGDI3VD1fmPjw9KYzd7sxHKeUuYEBvh95HHNQk2Vk%2BUjUX%2BaD9MC%2Fue7N7g5Ze8TnBGdgwC%2BWJL5BZFf6%2Fzi2yeqLddYYH6d2IGXp9wUK%2B1Ui%2F2xY%2FTQIcP8She3TEYyZjnD3Wx6jmXE%2B16QoenXVji%2BXYwmFALQXYngLLkm6%2BQCE5CPs8yh2od4ah5Fg2HHH%2Bx2nG8%2BJU%2B2KZiEB2XCpNwC1fkLKg9t6yDzDZhVi3h7fkheB5QQmsSTFdad1pxRVeITeQLHOpUxlfBKiIq3TY%2FCWJpCQgX6c6GEB0hTfRf1Qy%2Fev9ZQDUFShr6fJ15JFPqTSv%2BTJBvNXNbm72xq4kTfoks7MNU%2F9xJ4pCz9GrqlugcoZnvkIzSq1y66u5UaQmCOYzfJzp3bFYyhdNALyL6hr5DA8EHs7HUA%2FrUvtYMASwCBCLnkAJyo6j7tqUF3WSh6ZxnJtH93vT3wi5YCqqYiDDIzKdmNtUxrLeR32fyq67rWOoUonQrwqUR0qf%2BwCg6P0IX3%2F2W2%2BX2%2F3iGLJPwHnXZQgEQ%2FlFptUOkEi1%2ByW%2F%2BWPZgT6QRY96momFi89BOXBl9CW9w2MMHY6bwGOqUBpiIrDnbv69z7sGyEhzXy4vfEDlN2YUHmS1ilLBu%2FKbTAVzTOPlrwUOAcT0GVKFUizAdCqiNEFhDAqDBnX6e9k7RsblwPRoo7tpRyqYB2ID3GoLuFu8njVa6jsO00BtOoWLk1qjhTuRbfH2WTQ5akwB7%2F%2FyRxRMfaX9tYnSuB56fvigxG0gIG2KQ%2BqXXzLCQ3crI4u2Q1IM5I22958EC%2B05yiOZVD&X-Amz-Signature=67ea5e08c2620889002e1c6dc329c350dc59abc48af2a48e8cc9d48aada7f663&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRPMWMII%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BRMsuxMBadEKp2VNZNwcBzVh87smslOqVq9nNmW8hgAIhAPicy3oVwPPGIHuBxvMMWS9gbw46LoGkjKNifX7hC2CKKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzrUJOa6XS3rTWgHxIq3ANNlJmrPduIcWluw8bB89hcNe1NM6ML0Yp1K%2F9utiiT1AimEctebtl3ttmectR7Cm9dsvLnrOht2KO%2BH3TnBVIeVTfGw25huniA6hPE87igYSCYqzf3K37DC4igCyGbs31qxoo0TSZiiKMG6lSgKYBF5nsfbl62hD4%2Bpf4v%2FDeDXZHoL8R97wONMtHsP257J4ysLZ4qRNjD8SR9SufOrSHt2rghYkydlfc8oK82OaR2bYFurVxJ%2BKfQeBdbpkeEOjTRMTSM5qbUIZg954bIZQOJUDSRKHRfpLT3jbPc2n0Ixlff1A40lwZgNuFhcEMXGbWhgPVUeeGIJRVz%2F1OlJ4dQIrPmmkbTCps5dA3qQ1sPRQZWQEW58CewefOvpRh1u86kQu%2Bi3xcT%2BlCT%2FkDJ%2FX61X8bZdmmAsdOg05znuF5zzYuU3sB%2FCe%2BHfArH3hgc6Az8T7r6OxEGUpE4xAzK3RUqYLQWYx2rmpjedHU4o%2FVPnmrvyUO66wqyEux7HaJE4omxmXMT7CBfO7ZCczfbA7ni8%2Fw4Z2IKMkf3Koqthw2ng%2BhnZmm8%2B6ThEBcFDmHrw896LzZa%2FNlJ0rNAYNTututy48TYqzshrHdOcJN%2FbhVnjWFCNEjJzQ4KmbT%2FqTD02Om8BjqkAZUthBNMIPT3JUyvx%2BwtLMC9xwD2xOxgCyHK7AJRflplD6ETBS2oq8AbCI9GDIptpPA6MNKTqQdG9%2F3XIegSiek%2BSD88tlymcrLC%2BwvZF%2BAm1jmnXZLzoqeKxovJFMIh%2F8WmbAmH7AeTXa4hs6dasthTHR1GsY7J3uRCqPD39tNdwviOTkkPDBNpqLUy6MEoCJv1VH3bGt%2BrtQAuq3BoU687BGTM&X-Amz-Signature=7d4964d98c2e7e8bb3fea7b96a36a119162aca27e4ce94bb981cafb2505c81c3&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUKEX77Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCjYnk3KA4zjis%2FP7S5aUQnNRud8Xb0fgGFv63zIYceKAIhAI0tdLsIBIQP%2B1ef9Ll9s5XcoHFr2Xf%2Fu5F4QPJ%2F2A3fKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgylVyqHukIgSq1zLPIq3ANaNOX8%2Bg4uXYrOiE922bB%2FHNCiAlhlQ%2BfWtboyqcqDZwg8gv23Y%2FZZUujUFVAfw88CRDODiD%2Bi4FQhfLV9rSu8thjw2ltpjGkFC3YSg%2BuOfCxbDAlgij%2BcKypsfWWc4DmCZ71RheUL9luyWkIWDm4Gfb4qZzKoFr7hMvsmAF02iCLJ3ONWt4ovvSMJMfGtDQCvAwrB7x2w4y8McNhuO0cM2GQJR5a4ZkcmAiBi95BcDPQsEBv5T1o2xTWLFS5u%2BaazQ1dK5j3jJSxOQiwxqIUWbJeA2h%2Bs5Vm9xqs660VZuR98E3gS0oMB52CajsOxqyTbt5WixYbeZYg1C0YdcrHZCaJIh36DMw5wMbdk3aui18oejgYWnd8H7uMUnaj5nA9lsdPeU9mK0cD993695atLppA4BfXOPd8bXtvx0I%2FTrZ3DzYxrph5RLCI9QX12KJfNrVzHOb8nzHaStJo8Kc7YCAdHEhQrwsHzOmuiOZk%2BIwnnZZbnWOQQtoCK4dKwKlL1yH1hzaP%2BAoPZhBrVZGGynh0MucgfFzQohaFSjFGAW2W1drU7jTDtkodLdZ1bMSGopdj5WmXdx1JLjYEJdFeTF7kLh6wpqNVrkqTDj7Jo2s8d546aTav8CbOXQTDN2Om8BjqkAfqnCymcYMTD1CtjW647u0X0FLd6KXCPFseETcOPs2ellsoeUF6jj5E5JA3hmmqh%2BSMHillE%2Bz8oDsucCyycSqTC%2BV5jhIMqoMYf%2F775gLMnKkpPVHHkCasrMeIu4hWpcOI1lGLQ7DgUsR5xiRDnOeg75ctPAnhOGBW0cYNIYKyLjNIe5rWF%2B%2Bd0I8mk6FAM3K9KQMP4IHwY56%2FxZBUDmNtezwqT&X-Amz-Signature=80c89d4c2fd1b07bce23e69155006e3d15f6d7af41d1cad0783f5e9a67e93e36&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRUL2PEX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvNB6m18sJlR8IpVfDIo%2Fv9S1durj2InV8ElnhTeCGgwIhAPtfeR66LrSuetVyYjrKo0oyjEZuhLPBaHDxobT9yMwgKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzy%2BBLO0V15yp4vVNgq3AP7z3t5xy3mNufi%2FPoIKYLsp7J%2BAbFkQeR%2BtNKeyq3yERODDige6riOdEGqb%2Fg5dCEKE9yeSTJmmE04jFffFLwf2YqLfIRP8NfU2GYL8XxpeMBgkqLsMb0DpC5Ct1u4ubw3H%2BAkjDfQAcqKi7%2BIo9KoZu%2B44pZbi4b86Qnri3M0XyMVlNgiaaemA6mRsG6RSzy0dBPmtUBTFRLi%2FjvVg2VZbglQ%2FdyHL2heJevQdrTHfvy%2ForF8lBipAgWPb9OYJeMKultZaEmwjcovpYdWA3MydtmnxeOdmtctfO4SR8yOzQAb4X%2BPzR0%2BfeuxdhYaarK8cACl%2BE87OSV8S7kkjl8UwehjySb3IK4GQV0uAUEqH7mOK%2FD56zDia%2BHfP%2BFl8kGUGHOByrZlLyW4zmea5tVP1l8wszVRAYS3zUlamJoakJiqJbDGdnGpcn3Kq%2FrcMBMwfJtS9%2BaJ%2FxsFneJWizZqnLfirsprJWJhwx5OfXTjn8oURFES45zl0swTiuP97gFAydqfrZiyR5ltvMU0unCKRvgaBT%2BjSIVraue0t7N7NhIvM6bXAEWzNYtft0GBetep4QWvUSuDlWrUFYfctHSl%2F6l5rcB5AhWS1SIhzq6bXAg8QrczxTotaxiN6jDA2Om8BjqkAQD8F2wMvCSIHby3Sl%2BX0078ZXbE%2FJ1m35OTzJtBfT6uNppXaUTdDKKyDOFSt9XEV2KJlJ%2FaZLwwCbsLStXJ8GPJNmq8Pii4ofsnoZBm9rRaX%2FqtoHj9DqLljWKKiNQqdfPqpzNGWWWALI2GKuRZ%2Bh0Z2nJeKNkWW4N3EKIE3B7RMYJcWZMmMbXOVC00ctcSa7E1R%2BaY66QYndBS3zuwLTIdi39%2F&X-Amz-Signature=a72cb5d9acd3926132af78f436c3bd493536b12acbdebed18291e4bfd5eaae15&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XK5GUR6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn5wvKvCTVjRSmLBmo2sn4x8ONX379tzVcnFe0EZDVXAIgeyizo4VE1isUSYvvq5uZqTiwbAhODqkOwjGSC3%2BTIAgqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOQA4rO%2FkwcEm962yrcA1So5mV%2BqEICjxkYkjTA3EQWmz4NAWgDL7SwR%2BknuP3uQbITCGDI3VD1fmPjw9KYzd7sxHKeUuYEBvh95HHNQk2Vk%2BUjUX%2BaD9MC%2Fue7N7g5Ze8TnBGdgwC%2BWJL5BZFf6%2Fzi2yeqLddYYH6d2IGXp9wUK%2B1Ui%2F2xY%2FTQIcP8She3TEYyZjnD3Wx6jmXE%2B16QoenXVji%2BXYwmFALQXYngLLkm6%2BQCE5CPs8yh2od4ah5Fg2HHH%2Bx2nG8%2BJU%2B2KZiEB2XCpNwC1fkLKg9t6yDzDZhVi3h7fkheB5QQmsSTFdad1pxRVeITeQLHOpUxlfBKiIq3TY%2FCWJpCQgX6c6GEB0hTfRf1Qy%2Fev9ZQDUFShr6fJ15JFPqTSv%2BTJBvNXNbm72xq4kTfoks7MNU%2F9xJ4pCz9GrqlugcoZnvkIzSq1y66u5UaQmCOYzfJzp3bFYyhdNALyL6hr5DA8EHs7HUA%2FrUvtYMASwCBCLnkAJyo6j7tqUF3WSh6ZxnJtH93vT3wi5YCqqYiDDIzKdmNtUxrLeR32fyq67rWOoUonQrwqUR0qf%2BwCg6P0IX3%2F2W2%2BX2%2F3iGLJPwHnXZQgEQ%2FlFptUOkEi1%2ByW%2F%2BWPZgT6QRY96momFi89BOXBl9CW9w2MMHY6bwGOqUBpiIrDnbv69z7sGyEhzXy4vfEDlN2YUHmS1ilLBu%2FKbTAVzTOPlrwUOAcT0GVKFUizAdCqiNEFhDAqDBnX6e9k7RsblwPRoo7tpRyqYB2ID3GoLuFu8njVa6jsO00BtOoWLk1qjhTuRbfH2WTQ5akwB7%2F%2FyRxRMfaX9tYnSuB56fvigxG0gIG2KQ%2BqXXzLCQ3crI4u2Q1IM5I22958EC%2B05yiOZVD&X-Amz-Signature=e6014a51ae48ff73b168d60cd57e6c80325fb70a9735654a80abea6a82646136&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663SRMFZN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBxyQTZrqC1QYbAS5XIXAsfvqh%2B2vxXhYWCDuot7y1C5AiB7EIXRfhrRfL45PYtMzSl4MEx%2Bv768xPN60LQch%2BQuOiqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLk5idWgr5ziowf%2FCKtwD2pz2yDoWbvDvFxhrEkE1%2FBy9xKqP%2FZtMdgfHTEU8MmovALSUB7flvhz2%2FImEdushdwMm5QCwGsy0gz47GTpH%2FZ6YyRnUIYO3MRpB3SHSPy6fKkfJpM1SlnxZJVZI5mLIWMZ3a6tWcIrZYQsTgR8frnJLGuGomZGmJvQchDCDI5BhtNvmIDeuNrrNEwPGfxjWcLvd3GAbZmNuU8cbpL9xgzfKoIn2kIBXg%2FnQLbdMddsH0TJCMszr0u2dXDOA9GbIwk8L3LWm6foduTXryicXajY143Ol3yDNiqwSXiBRXqJxnzDPpgF3Yep3MymSxdXHB00uf8uNNJJ3mp6kKVZQqffkjw4yoJsvy%2FBLsSPf8goLhk6etkrho8cAP5%2BnI55zg%2FMoVPuGjLh5nKUl1FPS%2BtmsPrMFA2pxUzpygKVJh9fTrQEYqC%2BaVk85%2BU8afil636nTsg9B%2B3Q%2FllonxolHtumfHw00V1oIIv4qWl2ycrKIQGFIzB5socunOjmi0bxDHIW9472emkx6IqtyRUm1af3QlEQ3mVJsSzkyOv%2B9ShXK5KM3CFZ6U34V2Pu3FAexmOSN0x1nWf2iGceAZyvpXD7vweTRrnwZ4vqhMIkyh4tubUEjVw4DtZGarzAwm9jpvAY6pgHL%2BxqM7gKmwjZZ7lN2faToY7%2FPs%2B3iwz7368iUmBFH%2FwzTE6R8I4oluYkjg31Jcom3eUEVivGx4FKG5oSr6N7rl%2BdWveOE4H91DwEvBFhpndo0WttBmJL29AiY5UTheSEtTHrPziVSAjuH%2F24QIORaIt1RqLnm5LpNgztYK%2FwKjFfPbVub9lmtAJfinwov2VZEmWyv8F%2B2lxqdHLVckvEptUkyjXjb&X-Amz-Signature=6245e729793f9949ccc3ed817419d829a1c53961f72e26886bd8783493b9d9d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663SRMFZN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBxyQTZrqC1QYbAS5XIXAsfvqh%2B2vxXhYWCDuot7y1C5AiB7EIXRfhrRfL45PYtMzSl4MEx%2Bv768xPN60LQch%2BQuOiqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLk5idWgr5ziowf%2FCKtwD2pz2yDoWbvDvFxhrEkE1%2FBy9xKqP%2FZtMdgfHTEU8MmovALSUB7flvhz2%2FImEdushdwMm5QCwGsy0gz47GTpH%2FZ6YyRnUIYO3MRpB3SHSPy6fKkfJpM1SlnxZJVZI5mLIWMZ3a6tWcIrZYQsTgR8frnJLGuGomZGmJvQchDCDI5BhtNvmIDeuNrrNEwPGfxjWcLvd3GAbZmNuU8cbpL9xgzfKoIn2kIBXg%2FnQLbdMddsH0TJCMszr0u2dXDOA9GbIwk8L3LWm6foduTXryicXajY143Ol3yDNiqwSXiBRXqJxnzDPpgF3Yep3MymSxdXHB00uf8uNNJJ3mp6kKVZQqffkjw4yoJsvy%2FBLsSPf8goLhk6etkrho8cAP5%2BnI55zg%2FMoVPuGjLh5nKUl1FPS%2BtmsPrMFA2pxUzpygKVJh9fTrQEYqC%2BaVk85%2BU8afil636nTsg9B%2B3Q%2FllonxolHtumfHw00V1oIIv4qWl2ycrKIQGFIzB5socunOjmi0bxDHIW9472emkx6IqtyRUm1af3QlEQ3mVJsSzkyOv%2B9ShXK5KM3CFZ6U34V2Pu3FAexmOSN0x1nWf2iGceAZyvpXD7vweTRrnwZ4vqhMIkyh4tubUEjVw4DtZGarzAwm9jpvAY6pgHL%2BxqM7gKmwjZZ7lN2faToY7%2FPs%2B3iwz7368iUmBFH%2FwzTE6R8I4oluYkjg31Jcom3eUEVivGx4FKG5oSr6N7rl%2BdWveOE4H91DwEvBFhpndo0WttBmJL29AiY5UTheSEtTHrPziVSAjuH%2F24QIORaIt1RqLnm5LpNgztYK%2FwKjFfPbVub9lmtAJfinwov2VZEmWyv8F%2B2lxqdHLVckvEptUkyjXjb&X-Amz-Signature=3c883319e2e9a7415de071867b7c5dd993676f9f882660eeb16ef5e85b756334&X-Amz-SignedHeaders=host&x-id=GetObject)
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