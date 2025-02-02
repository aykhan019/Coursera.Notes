

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEQIWBXO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAhHXKvnWWjS0bhIPkNSVHW%2FiOfwlhNXn4Vnr5oJKyS1AiEAwe2NmWT166v%2BbEkQZTkuDEmR0efwLE02gzNijg8enE8qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPw6CvFO6t%2FK7X1CySrcAxlIIz1Z3HIO%2BhbXTNFbO%2Bj6stpGlJoYtegumuBMgduraUSwYgmVIjiC6ydB948lh2PeHYETWa0IDoTv6Yl%2FYd3bzEPrkJglFyCAjF%2FSKVnoE0H8nJH%2BV6eeahthQ1NrkMnlri7M7vevfeesgaj2dL9FTLeVZwzimC4s2t%2FelhEDOcoDodQVZNMaDjjntc2ooz2sQWZG3L8dC2TJtxcYSC2gLP9fqgwC9O6BwxJDW4YwtwR2Bhcey96cdZDzskiksGQv0%2F4DUqSF%2B7%2BtixVxh8sB14hIcbsn1jHTaGN0muVMavpNFM3wXcHhYoAkAjqNUj6EsXbZAQyEeRObmsF7xgpP1MbG5NyVIo4y213y%2Fn44x8aCicyZlTa6Kkb4D4iumTXheW4UcWxvz3hHW31Jkvf55FBtwtnE9s%2Bvr3Exy7peTLDDbbwBsixM79Dus8IwQ1%2B%2F4Wkgq4eJytBRm%2B5gblr2bviO1uCIIta%2F1rDLucXPjgF2gVWACWT6UNUofDgoxie58XyLyVbD0mRsXmaHVKzkW34MhVpc10JZ1NWSza2k26USfEZNr%2FyfN09v%2BWpwJK7ST3XkN7HD7ZxvXyUWto6YJJNW0yPUlkZYtizY2%2FTw3LABoPG4bA%2BpamGAMLHh%2B7wGOqUB5fHyPepr51knvVO9PvESZ9j8dXGxivgoNm1FEOaVyIxNMo1dadINmzeRFNGbgG2nU2R64o5VdCvwTNQqrF9Z2cw0ha0uvYuIBoFtzYMS9LhL5e5JbZSFsJ4D9oUpRgpYqwMngbmbe3F9HvNuomhhxef4vk6Z1cFgCpFBXk4VDufFK4Kqq5uHrqQX%2FAVnYfxfst8ljV1gHy5VsDaOYEe3jYw%2Fm0aE&X-Amz-Signature=abe3a7b62262778159abcc1277591f34048f4e7ee7f94c4153aeb6ec170fd49f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TJ357ST%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDAA6EDljd6YiLnsUaf29oczhm5%2BQT6VJJ8OsNXVIlBeAiEA0U7iwDy0zQK5K89nvVaPj2zY7aT%2FxjJUpcsISczvec4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOyVspJ2AJNbRaEMvSrcAzCS4E75w9OtN161Dv3Ht%2BamzPy0sixZqe5UFbhVRpiQEnCeFxXlmI3Omn%2BoBWndLTKg4oRNxzpvS%2BR2vVooDR%2FXlvpUeA8RbhbVBZdA43JsdIJbcgjDGlmT%2Fp%2BWNflyMuPV09mRDHJdT7Har5K26Xw7c4vBoQh7uaKy6q2nKXjZ%2FvCv35ixAwRwzzYRM0dhhEh4LaWdkHY8LfJnesY6vAePO6qO3rDFSz02KZ%2BA63oZkWlplMtZAyormmliCRd825FcvVzAbZ0mMsXIjdAUGBOk%2BjncdsvWawLi0ZxLxSVXGvs1X%2FV6sMUESNxcrBahjsWF2mDBodwq266NeKtd%2F4pfX0Ja6J5bYOu%2FnxOoUifr1lwaobCKmGZ29gfxjeRfJqmjCEqbpDPoVAYBM3n7VUV0x2oPk0tKDya45dmJRNtTzLhF%2FqEyuzWZlv9g8Ya3XlI%2BuG1gNnrGhYI66fQGq4Yc6Xc7aEzGknc%2BQ6d288nF%2BvyqNnkcStri52000e4vKaQ8EfDGhhq%2FAtGKNDcOzgKErz4O1wsbBqXoM3T3eeco4bHevaxo%2B2RTC91DyUD9yl0S3mAd0aQF1SqwyHWqMRM%2Fdcw%2F6zFm3tlufZBXcqqJGvfF4x8lR5qx06SNMOjh%2B7wGOqUBsVYLYP%2FvMAj4f0kY22sGYNyQGfjRVVgtGm5RRDKNRW8qMgLlJULq%2B8O0faRF4Af11Xrr4GCX5Xu5CavicUZ7ddqR5W2ULLBLp%2BGlFUE2xMN5omq49TjPPCbhjiqYoDX3BLIowXqPQ6nW0MRGW4yVIf8iRiqEC%2B2zQcFDy5kyuP%2Fqm3iCYRiEcbvGPMd8YPluZOu7oJfvVEikxsPpQm%2BCXZvcVqrJ&X-Amz-Signature=dd57ea53c73acc433bbc44c69fd3f684671af015ed7bcf087ff2d1a5037042f3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3IAR4B%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID12pFeAIHHDu2HNFQePB5bF8mKmybEC%2F8UMgxt3%2Bjy6AiBd7loGif7cVhtPugtVon51%2BxlLhqPRNKX0h%2BEWerEnkCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9cWiLemTRsPTefRKKtwDpt2ccLm1QtfZ3Cm%2BRA8d8HRYTehAa4fMubg3rG8E6ULjiqJvj2qtoI10xV1lAFuH94RyWi32nCtA4C9FGBAEkCA98OIjW4RoHCG1eJ24rcVITBavm%2Bkt0w9CEy7D8nF9ps6ckV%2BvSJr%2BFW5azZaW%2BMBUGcqe8eJ6UC33bjDDOiv8lB%2BHiUSvZadovFHhd2dqsTkLNeHxm4DuoLNnxi4L0rEdaQSc2JAoFKYYkiMMcvgPuy%2BrNHQ4vQoBXuGaKGSDLKSLTelTcuf5zzzQkaBgTpMgJQn9%2B%2FMPil%2FpiR%2BSJymnRNw%2FJWk%2F3cGTb7ZqRbP4xFaG4hyBqbGl1oh41uHHPse8b1FBYZ2cSAkYgJCERX3emW7j0gDISwhabmiQXkADVRXPnZt%2FUZ%2FhOQvJ%2FXKDry7mlZBjl1%2Fii8KvCHhj%2B9CAXso%2FRCb25Uz62zYou8bxFx%2BE3%2BWb9Jcs1xD9tRn7DfD2bwcKxrDjvkY8%2B7BU4s%2BocihS%2BSJIp%2BylkHWKMP%2FVJH1TaTMxWKVUsIoacZKtFCqOe6XNP%2Fe71nliHn8YNO4ZcjpiwPhjPg1oLrHvRfDN1VJHoz4MCO0sv8Xm2DwiNeMiXpQ4A60EcwA99iVJg3Lgt5oh7g%2FhHHouvC8wleH7vAY6pgHMRjlqEx6uHCWJIEn0aaGGgoK1xs%2FrcG5nkbNhnCO0W9ygki5JZFBJlM996F5ytJSokfpVH%2F3Job9UFuOqKbMs4ZXRHdT%2Bh%2Bk%2BUhDHqiFvMYDb4MUHFl1GLpx0Xz2%2B2iq7cwNaGRn%2FcVUX7XX3vQGqZ4wIqTON1vvby%2BHUP72Ybv8QwNHZwXc4aRyhzAiUv2lbHwgVERqsA0hUKho2209H7o1EWGi9&X-Amz-Signature=71a23a44e6b6786ca1d7ee8e4a83aa9b2ef26f4f596c95427ce9dc3990e79126&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NYPHPTZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwyXHyJmEApkj8Sltuaoh2rzvSdQuO5kRiDaKU6BL1gAiBV816GxWZNkx%2F2wRO7IaQLCGwRN5IJyo%2B4%2FOVG3%2F8opyqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3VLMTxRCUlLP6c5KKtwD4AUS8lXWvQc8rZP1IpmC9WRoGf91Dfwfz8xA9QVGfmGsgpKLXUpBdFu4%2BWed%2FD96OCzeYj5ZN5qULY68zaKXRRl7xfAnDX8frlsFEdvrQUf6b23wFRDP8v3UqYO0HdQo1U6r2jfKL5qPDrOsyKUt0fzIzKSXaZuAD9yZzFMLA7mBRsDa4GWKoOAc8Lt7smbCBVkveI2%2BkeLwHc5Lms6vKbzATsjzTpguem%2B8vSdZ%2F0%2FxvMu2Cfv19e7YdzCcxaHxQRr37ydEKec6476NR%2FeBZiSUcikkSTmVntKBNjO1wv6Pa%2FFPdv3p1WHjZPyAzKcybiTbEQQBYjolImu9YL1MDXFCc9gKmYcEmHElZJBFLM%2BQRJZeVuW0TlMFAcrDh%2B%2BHL5MXDfPMcdFC1yE1CVwohezCp7uvuypx6nKHIJjYgSFZ0q50stHLNqOjxSiLNjU6AhazJM8fPxyjMkSiWm7Kj6rGX5lIx4UyfRXcC%2Bmir1ABmxs%2FWnT25j64B9Z%2FHYExFvxX0NausTp5OLL%2BpDMAnUixmR3kSiq4UNhUfchUd8qi0lU%2B9QYbYz4AzJpcMzoEiuQa2xZjefMxm6MJtWTzrbSlUoY%2FbUo1nCEWTT6aenur13JhQ2oAVSPBnZYwj%2BH7vAY6pgHOV%2FXo0eT8jhL0aLj9lbhTSRGeuYE%2FVgwmrcr%2FtcdLmD96lGHQrfLzlhzc0JilRCEsRUMeR1SxyetIqjkr3XlwFnOtKGhK3msdb6XuJihNPjYiyzRxLjh95B5uohzrwi30yqUrcU07sFjDf8BQvBVdgBucco%2FYpZSJBwtmmIG0AMcU5blseviLLr%2BTRkz8cjEgtP6alGc5Su78aNuOR7btRl7Bguh1&X-Amz-Signature=eb34856877af48a08b5f1c2e87fb5407f8322d96d41253ff54deaab6b208cb42&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFVXFV2C%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGmUu9yoxtnlJ7816jgHVdSr2wFtNx7K23pQ7R1DYlUmAiEArhNe4Ka1F0cQILjbtAInF%2Fdyhx1%2F6AA7rg1a6nnqHEQqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOev5j390OXMoDJjSCrcAxI3ciRB82qxEL2w%2Fu1Le%2F4eGqytk58nyV4tRgYa97PhhLSwWKm2h9SVMQ4rWL5CbGq83Qd2HvD87aEY1Q3vtB9BE2bJySy5tK4det4BB1h36wkVeUJJnJJZV5H2z8mG3vCmNdRqUAqaKECORcxQMrcxfSPUdE8plmTh7Qzw3FAXQrjDu1Nq0CmQS7GEYNFGZZEtDFLGP5smRZO1OLZ8XiNAuBNdNrdgIFDb1n0gFiWWZ76kmmqXWF9Lj7PCvTEQC0QrCFvmUvgfib%2FKgNMipZXCkXQERfYrTRFg0CQ5kBGIPo94ecJt1yK2HpjQQ7tUf%2FcYladFRKxe3jrwzZH7wGCLH9ZQLJboZdHYlswLRfTH0bR6ZtSodP1eRSUM%2F2IaIau0DOf%2BQwoPcMzYjwT4u3zNsq%2Ffz6x7jMrcLeb8rLmL2d9fdgv1jOmX94vVFLtf903yf6eq%2Fbb0bQlMpPlEo2d3eY5OEKAVFWQropQe8Vvb2kgSoOrNAkaGEnXrenjW%2FPszlQAJW0NdMypJgqqM72doNo%2FhMhM%2BNPJFXzsNFESVVhe4SxVWuI7Y83M1AF%2BayuVcuD7ZO7wjWy%2FB21YDjLkx0cWEYJYuZTlcUC55XY66%2F2T1P4ww36ijn5hVMMzh%2B7wGOqUBSnws66PseDBvDWSK9buzr6az1LJHT%2FQLTdp%2B8BoChXkilha1p6%2FKtMOgvyMIENjQAHkOt8RYQYmfhFOtzxoKrkLdIFp%2B06NpNrea9tMBkGjNiNxaUT2kC9YGsXQMAXgofJNEsnXp2a%2B1tfcHxHPQJSk3KjbnKPk9uDqjWwohARjONB5iEYrjYbZ%2FLdVFejzwjpKVgHPfOIwLcBid6qzBQ21qe%2Bgs&X-Amz-Signature=c40cd1c37fd7e91d54f1dbf34f953abcfc07c0eb1c7a2444d98fda906b33e9e2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVQZ2TS5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHKtY8TISKJgqCpaiIL0ft6h0qQZIHWlBRpLVzILimpHAiEA9qR%2FWMwBlX1a7ZnomHbK%2BJ4ewK3Ky3MuXxu3z%2FnhfdUqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCTnvFtZqaWsaKSB6ircA91t52MKXXr1A6RsTZLDcrluT7DlWSATHZJvErycjC1ePInmGLMnr6xbuj0rfr%2F2QSV94UYIsTnw31WkKhUYd7IWerNmAuiMf2KPZVEIvQFtGhLqT%2BJHY6vgiHPo4q3%2B1S%2Bt6tcLjWlRn0wbNet6NkVmu%2B2YE1LI%2FfjEVQVFZRYKvuSg2yLgKFiZxIXevqLPgnv%2BBDtlkigyrquNQTC7NtN%2BZsN%2BdUlRgiFk6zc2f4OPqhbBD2%2BB9kIwMohuhwrLi9L62zQzECZfpi5FZxreMBIr%2B7O7wjQrurxhADwI9yxGRcbeNp7Wh98cnZIsjfavm6KMLX156YEAbPqct67P6at5az3L5PEGrk7p%2FJ0AF5RXuz%2B6yRVNM8aewmhVf84V6GaTt3HQqQbJ1HeDleNmUOpbkBSswT%2F9FZUAaAUmYISsQkGugO6aSnTMi6Y%2FiLx8Sw9J5C020QFbXpZgc6FdTtUYiPVzWus3eExm9cMpowo55tF2SzB1C6WvMBPoztmpiY8vr3l5%2Bi10U0tJcXoM7inpZXPLaXSjrN98f2hO4C9Roj3ZD00FK9QwY56JKKwiY9G2ZfuQIPiEnJxmrFs2nDlNYN2kMxLPKofGVZ47Jv7u%2B3ynNfmEqr4XcMr0MNbh%2B7wGOqUBva00lwVuW%2BH9wzy3XNiEO%2FEySoL1FEVYQjHUVqC%2BcDUknnUvX%2B478oUtkI2VEFjgdYLnBge5%2F%2BZyVChBScN%2FldL%2Ft8xHLvPxDwde%2B3SerRypL1q%2BDsiWLF8WBoYhMCqhIStUNu47GUKHquOTxn3zP6SHmTr%2FJ1k7b5sMerbmhpSOxEBAdORQfLlZ%2BkO6FcAVBKfyNmIpwDvSRwpmQmdnJ0mhaekE&X-Amz-Signature=41443ad66bba1b2c89f7bf53244123531147b093d0338addb25d036f6d33a9b0&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVIM6R3Q%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK5WCpxKuFs3rIYkq1gZ4rfXAgl%2BDEj4rU%2FODngxf2CAIgFdIgOnCS0CIWIxNqnboatmMe9zY60EaqQ2HVI3WqTmgqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGad8SvSR6sVDWXdZyrcA%2Bk1Ey%2B2PgLGxaR3H2Enk5ja5rlNJYe4%2BCJr7HjJlTzof1dmjj5oaK7Habt3Sd776TA8VLrlPkPgg5c%2FYp6tr9ILHi9ervUaUd4dg5VoC56zVCQxM1v%2FtwqVaHj9Uvn4DInLmZjxsWkYSglL%2BZNrPYmSAlHI1jZuVtAHi4j0vquYmpwsxBZsZWSEU5BPZAe1eynQkrSgjLXGKRFJiK%2B87Yw3PNIlUI9yleskHVq0LahXVUp9QBJJXr2G2L3uX7i5fhEfUEZq1GyWUILLYspqu7yJLgphHdl%2FnsTnKATbtDiGPqhg9P5O1vNNUgWSMpfAMCX9ScyNVEmBvJv8uHrmo%2BYzlxsl09H3TGt1EO4cy4VUikMoPmJqKZRgM9XmLk%2FXanUJ48z3RHN6L7UQgx4zbE%2FMNXcnXxQY6VpGHFlhDq1mnFS6tBX1CpIxXxc%2F8w3fZh8N4ay3QylusTgYiHtvwQIr3I%2F%2FgBST4yGLcD%2FY8m1oL8wAxIGHfkcDj57Y5hQoSVoWbwnecoCmFsv%2BqR2yqeetVCrjHKD1qYyOKDpApTN50ypnYOyJg13ips1LwxPl0t5UAOxdmlmMWmSa5X0mZ2NZz5zOBzj8RyNduSR4tkhwkhUIlgEzH%2BCvYzZKMMHh%2B7wGOqUBXloSoWc9JSTUSpyjZchhfEsMhPfy7m8Xu5cBYJUz%2F4FcZZzVsrf1e2yv1gI%2Bjo9S6V5VfJqmFq0D36zFHzWJQq3nuwPHqXf%2FFgsxL%2F8OuajiVs%2F3VOe3y5XCiWznJFdyA%2Fir%2FGoH9tQlJgml795dvy59hUJIF8OA%2B2xIGC%2BMIQSORHgG09sMI0e%2F3qIvD%2FkG%2Bj5sU2%2FvxvjIV02%2BMQFd5hBMsRN2&X-Amz-Signature=a693de64fc7a8b5aac02a270d2b8555ce91369fe0f869e526a3f820fe391ddbe&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIA67P3X%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXWx9jBSYEO%2BXzbiaSiE0VGkOzbvw6br7UOpNyaKXLPAIhAI0CKDKnZ7nMlyEFp4Q0I1d9VOC2RUkrcKDJaJXOwrxHKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwxAWzH%2F%2BCCeIGmaIwq3ANTEZZKfWuF40gREjvj9BNKBP4xwUHO903imnoa1kFVI%2FNSY7b%2FnNb0TgfDuaJtnSmjH%2B5tD5W4CZCbkZNolfs59D1pxYchCpZQ60l%2Ffi2dY%2FQOZnk0Y2CFn8JhRHwFC6RJZptD4G1Z8MX2vwMjs4UYe%2B23NE89fDjKj7JSJDXSlK67Fsc1nym6V45zQ2LK4rna3d6hGlMZXPqm8N%2BhBMWH7V3WtiVUCg3tuEoHDbx3MPX5suSDs%2B6P42NFwGKQe19n6RotYE1x%2FJ4CLgi0otGNUMxHbHQEPzhC39GcJIRiAIewiA4iC78FPuYskF4XTywmLMO%2B3PcqEcQDgtD2ZNGcaw4gDxskNUTFOR85vopQSjG0wnucLuFo7ocAOWKKM2gkIcnaHRssvx2UIRztHDsTMzUVUzNQ3nDd8BQtRj1l0k7zfSq0NZ6Umz7VmJVLj5GM1Ku%2F3vjfN954Tg0zf5P%2FwwDJXkny0%2BJTnsOenRQ%2Fzq277aXAy3EKvLweXgeuyiScNUCvCK4m44zzsNcWH%2FUOtg%2FkB8uG80gQgShVcsSJSpk4h7iANyf445kOBmnL7DpON2%2BhNrzrErAcmCA5biCCnJPUHfyV2X9Phk1BvF6%2FNH5YpVRMCfiAMot8uzDD4fu8BjqkAXhTdNQpEwfy%2ByB9jG8ZefUZxlz4MN%2FaDC8c%2FevFWtq%2BBRbtt%2B%2FIfk1w2rnC4xw1gR%2FWlxuEALWwty2DfoyGLRmQBkiFjgfUiZNhHnDi9kykR7%2FJi7%2FLsHuIKhUsLy4bMGB%2BAFSRul5Fb1rRkrljSzxlm6vy3LKESjH2vqtSbiqb0MmEhVixwTrzIhMaUz6xRoAO%2FdDTcXi4gysjICduoK21QZt0&X-Amz-Signature=d8b1c439ad750b2bf17d8d3d015e22404b69e0795dd05917af9886e2034f2ae8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFVXFV2C%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGmUu9yoxtnlJ7816jgHVdSr2wFtNx7K23pQ7R1DYlUmAiEArhNe4Ka1F0cQILjbtAInF%2Fdyhx1%2F6AA7rg1a6nnqHEQqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOev5j390OXMoDJjSCrcAxI3ciRB82qxEL2w%2Fu1Le%2F4eGqytk58nyV4tRgYa97PhhLSwWKm2h9SVMQ4rWL5CbGq83Qd2HvD87aEY1Q3vtB9BE2bJySy5tK4det4BB1h36wkVeUJJnJJZV5H2z8mG3vCmNdRqUAqaKECORcxQMrcxfSPUdE8plmTh7Qzw3FAXQrjDu1Nq0CmQS7GEYNFGZZEtDFLGP5smRZO1OLZ8XiNAuBNdNrdgIFDb1n0gFiWWZ76kmmqXWF9Lj7PCvTEQC0QrCFvmUvgfib%2FKgNMipZXCkXQERfYrTRFg0CQ5kBGIPo94ecJt1yK2HpjQQ7tUf%2FcYladFRKxe3jrwzZH7wGCLH9ZQLJboZdHYlswLRfTH0bR6ZtSodP1eRSUM%2F2IaIau0DOf%2BQwoPcMzYjwT4u3zNsq%2Ffz6x7jMrcLeb8rLmL2d9fdgv1jOmX94vVFLtf903yf6eq%2Fbb0bQlMpPlEo2d3eY5OEKAVFWQropQe8Vvb2kgSoOrNAkaGEnXrenjW%2FPszlQAJW0NdMypJgqqM72doNo%2FhMhM%2BNPJFXzsNFESVVhe4SxVWuI7Y83M1AF%2BayuVcuD7ZO7wjWy%2FB21YDjLkx0cWEYJYuZTlcUC55XY66%2F2T1P4ww36ijn5hVMMzh%2B7wGOqUBSnws66PseDBvDWSK9buzr6az1LJHT%2FQLTdp%2B8BoChXkilha1p6%2FKtMOgvyMIENjQAHkOt8RYQYmfhFOtzxoKrkLdIFp%2B06NpNrea9tMBkGjNiNxaUT2kC9YGsXQMAXgofJNEsnXp2a%2B1tfcHxHPQJSk3KjbnKPk9uDqjWwohARjONB5iEYrjYbZ%2FLdVFejzwjpKVgHPfOIwLcBid6qzBQ21qe%2Bgs&X-Amz-Signature=0f41bc5a152bcba568d705dc6dcfc2c33f60fab7a3b149c242976a99ee1e9a4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VO5CMVI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDWxgrNJOAx9eCXDVy0nLEpWwEu%2FV8OmNFfxlHNJVG1IAiEAgs%2FnyZTVk1DepbHigJqMbw6xe%2FzYcNEoXOLvwTWPdP4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHGKWi7nxNWpkovmCyrcA9Ay4i9uq1kjdonDVyokuUrXXybLG0qYy%2F4tjtyrSiu0Wyz%2FE535v030vsB8kv40U5B0zMHJKyWEAJ1NFm0DIaSi70vtyecwl8F7UE6ur8ZN6lMBPqughrqEa7ceDALUXJ%2FoCOZ1kMUR8u6mjhJ%2BdMt96zIAVMuBR8PVbxWXjhAmUPjsd0wYiMRG5izJYm%2B%2FJZY85ry%2FioyZTc8LdoIopu0CS1o%2F%2F3HhZ78HGkuAbL1K%2FvxqEig4I%2F%2FavWIcubh1RPudgAHlVZE6qVr%2FDLye0YciXR%2BcX1oCCY5PybqzswMCYf%2FCDiynqXt3DhGv76E1KFUr699EdviD3zywz6Ou1jWa6DL7I0nc%2BnrRekMrVMoUlDicnmd%2F4V%2FcDs3gSzdgzmlERY113Sa2pxaZq54CmoCLW8UdtH5i%2BWoEZAHaPJgLXr6snySE5oVbYTHRsHAaYsSwEIzNzojtq02O0mCJw50Af4ZUZau9LxCN%2FJULc7%2FzYElbwNdynVvtkHqMeFeXRUjJlNDNzR5XQ%2B5ryy2%2FlrmR0HfFBaiE3XKCwUwAdT9bwxoy%2F2UmFPYeVJmdArK0eCFQCBcORcy6aUXPk2Z4FjkuAHCI7wE8pPkoqJDj07koJl6DI4ZZSVu0nTl4MM%2Fh%2B7wGOqUBLZfDXm34KR2LNtF6vppaojfAzHDloDtSu0TnWUtjnGeiKigxVDzPINpm8KVM0nn326EkIeH8abdCgBEMcAoT%2FE51tK%2FHjGj8V4NVnjS43G6fix6ZLyubo%2FJUdgJUpJ%2Fd5Of8P0s5ojtK3pMqLzBlEtyY2SyX4WUkZ5osz5iJM4FYSmDUHTgWFQOGs3yB58G7eaoG5UVaWlSmGZSwtyLqGZJOxfyI&X-Amz-Signature=4632511b78e3c13c4368ea00da0cb7b0d13a800b2a07d346e7eda37eab11c371&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VO5CMVI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDWxgrNJOAx9eCXDVy0nLEpWwEu%2FV8OmNFfxlHNJVG1IAiEAgs%2FnyZTVk1DepbHigJqMbw6xe%2FzYcNEoXOLvwTWPdP4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHGKWi7nxNWpkovmCyrcA9Ay4i9uq1kjdonDVyokuUrXXybLG0qYy%2F4tjtyrSiu0Wyz%2FE535v030vsB8kv40U5B0zMHJKyWEAJ1NFm0DIaSi70vtyecwl8F7UE6ur8ZN6lMBPqughrqEa7ceDALUXJ%2FoCOZ1kMUR8u6mjhJ%2BdMt96zIAVMuBR8PVbxWXjhAmUPjsd0wYiMRG5izJYm%2B%2FJZY85ry%2FioyZTc8LdoIopu0CS1o%2F%2F3HhZ78HGkuAbL1K%2FvxqEig4I%2F%2FavWIcubh1RPudgAHlVZE6qVr%2FDLye0YciXR%2BcX1oCCY5PybqzswMCYf%2FCDiynqXt3DhGv76E1KFUr699EdviD3zywz6Ou1jWa6DL7I0nc%2BnrRekMrVMoUlDicnmd%2F4V%2FcDs3gSzdgzmlERY113Sa2pxaZq54CmoCLW8UdtH5i%2BWoEZAHaPJgLXr6snySE5oVbYTHRsHAaYsSwEIzNzojtq02O0mCJw50Af4ZUZau9LxCN%2FJULc7%2FzYElbwNdynVvtkHqMeFeXRUjJlNDNzR5XQ%2B5ryy2%2FlrmR0HfFBaiE3XKCwUwAdT9bwxoy%2F2UmFPYeVJmdArK0eCFQCBcORcy6aUXPk2Z4FjkuAHCI7wE8pPkoqJDj07koJl6DI4ZZSVu0nTl4MM%2Fh%2B7wGOqUBLZfDXm34KR2LNtF6vppaojfAzHDloDtSu0TnWUtjnGeiKigxVDzPINpm8KVM0nn326EkIeH8abdCgBEMcAoT%2FE51tK%2FHjGj8V4NVnjS43G6fix6ZLyubo%2FJUdgJUpJ%2Fd5Of8P0s5ojtK3pMqLzBlEtyY2SyX4WUkZ5osz5iJM4FYSmDUHTgWFQOGs3yB58G7eaoG5UVaWlSmGZSwtyLqGZJOxfyI&X-Amz-Signature=99672c69bb79b85cdcc03204f30f71915d06a15d197e7dbea0e95e222f16a776&X-Amz-SignedHeaders=host&x-id=GetObject)
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