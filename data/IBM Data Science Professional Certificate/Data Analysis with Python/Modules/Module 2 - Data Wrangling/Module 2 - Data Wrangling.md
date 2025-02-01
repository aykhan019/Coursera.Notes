

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOGSNVE6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCImMlnnD8DBatDNpzddmwh8z2mjNimJ6W2s%2BIOZX3e4QIgP%2BQSkGFZ1D0udmdgLCgUOxQHYT07BwICtb%2FjQrgab1wqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBrZtzNX6PiIVY54PSrcA%2BlKfHD%2BwzB7XWi8PvySyASe6B8d4nya5aX99HVr0eEaCmYuNBhbgz2KHzG6GwXEmBT4Mw%2BBsEm7%2FWp8suK2afYynWfyrLiscE96XjqEvmxmHOcFC3I%2FXdqQWYHe%2FB8ARzci45ACioEjmsvdWZNZSwqcIt5EeP5BZ6T801J%2FmEcc0UBzrADC770EtYRZKfqOIX8esZmXdBs9GuofvkqqHN9%2FhXFKx1z%2F3pO1JpJfoSHGUY0hxro2QEqS8qK64EG1YM53m6YR%2FmoSc635PyTzxHgNFfYP5R0rFeWrLm8Q1bPEX3cHl5J9i7vSyDcXs9Gi%2Fjrh%2BqE8rVz2B0Z8RTSnSoD8Px8UubBjjA7r5dKpIKFsrrti7uwzOfwStK8me6l%2FV%2FsIe8fvayw1xOATH8D74zrrcLeE5NByJrN4Dh%2B69P0AIhvMZk88FXFQuuf4X7hwEanJQm5fQlmh8M285fMMDCILsRjG0%2BzesLFvFvV560OHlCgc0WhDLFT8jTUT1fBTMgAbUL5AoZrogcQH18BM%2BmL8R6sCsFvegJFwtzKCnnNn0Jm3JbLBbsBHdSggSrCBHbAaYs7jtZLHMm7mRjlmczMEg0gFvtqtVT%2Bcx4q4pqw9nnii12f%2F44TLrDifMOik97wGOqUBoj475f6fztcF1AJuxrcLwmJTAt25QBqK2Q4orla9q3Bpa2t55VD05flFHNq4JifIXllc1zvtK0up1V5HKJHG3tmTY2Optv7jyeBNRQuWOvwMWj7dpVkL35DNm28ZA3Qpt%2FZfjvtGC3AyZmedSP1CBLrydywJrSILlf%2BirXavnhKNTp0FiFW9HWytMHxvcWKTG3nsC9BHUAenDU4Fo%2FSdVYCv%2FR8Q&X-Amz-Signature=5391d4207dc3311f6000bb4a84e2c8c5c4c053b20b28980747dd28190ad4dc92&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TD627PI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDf52H%2Fln714sX5sqllZnbxqzLPViXQA20VhPCL7ft4LwIgZg1KVUv%2BzB%2BDX6GjQhNesOWGEjTM6V9lEqjIJ9wt81kqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNf5%2FyDYy3O9HgcQVyrcA6NlJO5%2B1DCBKXWUdvaGFy3ELQY7DjkHPY7Zre%2FFk8zD2KV%2BosG3HyrQ7c26lKhzMqfcUGyXU35oh6v4vcREfI%2BKCPEcN6tLisgulmoxIIK0w%2F3%2BgPkMr6RSWa1gdWLXmi4Egns7SvB8Z9fQJzFhpwv58QEaAR9rAAceO7kaO1Ec5vXjslWLKSrgRyoh7t0ay%2F8Rscd0hw8yUbL%2ByMoPAGyXPJ7iJg%2FUt9Ip1p%2BYaLJbzh62TGuPgKnM%2BiRTIRPf5muyb4IxPB8f8EnvfzKPzYCor2wFYU5exGyzJcvxtOgyeQXj0ZrvX%2BEtiv%2Bn4VLYBRuBk%2B%2BBuNzRXXDfl1%2FVhaujfWUQEFvQN4LOeIUheQlw4eO1wGuwmuUYTAiJl3hJXSuaHbDXoHum%2FuY8UpKa5HMLfR4FKcZx%2FaDi8%2BETmAt3cOZg%2FqJmtlSlcRapzfOwS22O8iJtLkC30sa65GWFA1eLRFNG9%2FycBbLyrotk95Fg%2BleMS%2B%2FPklHRva5PflDWVwpjyTyjwRIctzeepxB1n2N1U4Kih7k10Vty6WuwiNIaOtzRa1kfeZmapNR8AZcraei8CLoWZBLCEO5l0HmHTofQ8nutXM2wCKIADvr4Cj8QI%2FaD3a9EctB9vFt9MNGk97wGOqUBY2e%2FT8c%2BuNBYnyTSrZ0h0IBkYNiC7fCSIV1Re0l4f%2BPQXVvKNWPCylwvalzg9dpHzuyo6fvUryF12kPF2TIWihK3qleEMpnaEnWnb5LrFWCMlUOeNeKW2a4XX2xuOmYqRH4p01xHe00r%2BRJse%2BAHY1Z%2BO%2B4Jxp%2BV01XVe0E7urRs122UDOnyimGAuKxE6%2BH3iNn6Bh3r5GXMCrtFATpcY3RX%2FdxZ&X-Amz-Signature=d34cc18a1392e79cc07db955c4c6510590e1a34668f056a97423e62501036e76&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2KH4FCN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIChQ6ojt4gVZ6gDJiIBk%2FP%2B8CLX8%2F0YpQbeRcAX23nPNAiAXpYg7XZCJ6mWax1zKOEDJS13tpVXPT2YhZuz3Nl3h6iqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMprU4Qr3VLFq6RndCKtwDdtndvYsE5lYRTrFowcbEGz%2FmdYSAKLuc7THpxxT8coruBA2Hb6Ls9CqkwrOKjYvjK9TVUYzDXflLFLpDtq4H%2FAqX3ynqU1MNYTfeIFXcf0Y1zHSeHUmhupFNVy0rqUQ7UO9lgtxVMFTmZJJwBXcW3F33Ytxug%2BTL9kPQ0hRiQejyx9tsch%2FmYVXD81y%2B6A9JAL%2B5MWoNP1MhacSzzYDe%2FWzkvfdPEWX24mSnK8%2B3MSrajOp6bEGrVrRvXA61%2BIUZzGXaEB3uAzEbD3LopjVZGqHPMl74EHCvzP1NGcieIwJeocy0NAlb9FBUfBjIbjrKAjKqBE2eFU0Dz9i1EamjgyAqwejiD0ioIKMq16r8mAsT4qRrl%2BhUPQ0t0wTZufJnFaYwoV2mT6MuBA8Fw%2FTPrEYrPatY%2BogYXcXwSAC%2BanFN9z%2BqcmfJRhPjN5jZGSQ%2FkwCljKy%2B0MmloOaFMcOMzpYJMWyIw6MDcoG%2F9hlXhxp%2F2LdjqDNAAop3KPyu0j2gDUVvmE7xg0URW1iTQYGxAOfi%2FYgfwOJmFqB16qmFjeJeRJfwmdyMqgVBYBM5JIW%2B73BOgKs3q58LY5ixdrvR%2B0W91zOhGK%2Bo8e%2F1PwXp0T30MuZ%2BVoY7MN7RefgwmaX3vAY6pgEggNM9d8QpP%2FjO%2BpXOM29FyZcqKQx6vtOE1mF8HViD2dh%2BUDM5WPt4XdIoDvIHkMS%2BlfRQ6OVL5bAy1DNSp23xzlvfn22AMmh1jbnPgSKCxzq1KERsJH9354Xk71gBQrHXB4mK9uZtKwxdzOUuoyUdXLqwriqqwtCVx1F1fGvZJaciZA4FaiEJSctn64OeMa%2Fb3lr%2F30UZ0rmrI3SWI%2FhjRnFAtbYl&X-Amz-Signature=acb63adcca8a1f7c34976eef97a665a45150d3639f0c6a58308a73e0472c96ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEGA3QRA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAk5u8Xl0uyctCRFCg2X6yp1bdHFUD8gBNtrY5yVJCnAAiBoskAbS5NkmUVJg8gT2zzMeii6tshM0hU2Ej5dNaFcdSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZhFnYZrCn%2FFhU5vOKtwDIes1u6%2F6un9PWLEtAR7nYJ59EelfDm8P1UuH6hqexl0EdrDhcYWMHbzX4IlQApamp75oeObQMbGpMECC%2Fg%2Fi06rUmPKXH0gZ4aC16vd5DgSHGsfeTiPQE3fSsjt0QwOiV%2B3TPJDi0WMYz%2B30L0GL7pQYa5TdIUfDQ5%2F4FzPkavj4XQD9ekytIGi7L9diZUPkGcvsE3s8aIGhkf8MZ2O9ybMgmtANffqBPNjYGBRJRlggeAdrLX1%2FyPmL1LkTrZDdBrKNvsHQTbxA5L1GEAvWwj76sgE9PTgMSXuGGAIm%2BNekYOMBV%2F1sDdzYcaRZzDSO9%2FQeISOxGV3nn69Icqxqb55150s9sd9B6HxDypgoZw9nZO0uPZN0XS2arC%2Bzbrb8%2B0JudjpAly0BPmAviUX3yHpM0pBYc%2B947mkMnHUjVlmsC7oBrDEwzbo5ul08uk%2F8umbfyqaYg7BqpeRfF5rvU3i42nLy9Z%2FVqx6fFhA%2FRVPVESeKcUp%2FJHWEz1Ll6jr%2BfrmYC%2BPKpyRMYQUmtseVXx2BdcLrTn9d9lQbn8XKkRAlruoyjl3iziVL0oDTYTLDa4BIhIDpyeo0am7SVnGyBV6tQmVIQxDjW6cCrNXmVL9jSy8mlWI7QLKzA%2B4ws6T3vAY6pgHunqPi00RyDNT1iLaNR4j9iDqQPaC3eUJG5HSEAgTLiUbEFmSaBILYk41eI6tGcuAKIxndat24v4c0GV9qkFr4RnAHEP10dELUT9k7oSzg02vHP0zrzL91QrNGIr%2FRGgKlQXxm%2B%2BLuF1zVFzr56ztGdqiT1LjSk59rekmlZVfkuM0QiwngfWnQ4SCubckWhGlsFpn%2BNwJmpWVWaZlywroWz%2BgdDnZR&X-Amz-Signature=48a615c627e409dac9bf06e925291f942ff35d89e2c68eb71ab8bbdab88a50bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FNG4ZCW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICeXe1X8g0BmNXgxxGM638J3C9Nsypr%2FLnOXh1Mg%2B2irAiEAqEYjRGIyNV%2Boyv5Cn8JiP0pVoXHuLgl8L0NhI6E1yZUqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBZ7vk2Oe%2FQWNV%2FqCrcA6QybI1Yxp3ooaaFW%2FTnOgLImn%2BgbLWVJDDXlb76jYUdVXos6t1UAbeQGLWuliyxbx4LiDUnBq%2FmseNZ3yeXXrfyQsk81XevIglIqZ0CY7SMmlkYcyKgqGj7YimJHrDvk64%2F2y3KYxU9Yu2E0SRr%2FMAbMcFxONOtrNdfv7rkoONvHNMRW4rKUDMloyzmvoFPuEcVI%2FdCVTpMrbC3zV0kf5bNUHU4qBRvh6eduOn2kddgm8IuuUhfQFrjyftrd3PbBNg%2B6bd8hIuNblwnLoaeVEI5j5jcNXMyn9VX7UpMNONJjv3RZH3nxnbswxybnSMftTYn03Y2xxutkhAZ%2B1YRHUEoEOk%2Fv9xJl303%2BOFenfWf%2BzB5oxEE8%2FXNaF9D18au3JnGZuXuDLqgmdeu3ZVJ7ELWBonj0RR9kdCV5bU7nLiuSq4eqAgiqbV8KVQM2Iy43VB8qBZNYjCVwrFYEs20XfdBe8sQC1Z9wmqT0r8N%2FlMJtLYSzly5VKGY2tnOWpFxn8nu7qcGMs2afkIjqNSEGf%2FA%2BAFnVb4sRQgqG%2FFuONxUpZqEZWVV0lgXhzZkihchzL0O3Z3lmiyW1v6PoyeWkYsc5nXSp%2BfFrdwE1g30uLWLfe%2Fvwnwz%2BMq1heA7MN2k97wGOqUBTJlqVTrxOE8lTq5ctvgc7QsfVl0UXNYScaK8FD2v8GIzX7BufIFEx%2Fte8B8Kau%2F5X19JoF8fhY1Oo9z2nxtWnhoClGAKAkDglvFGyjWxUvRMrLzgwNr%2FcYx20LmnBQofVtUvzF3kjrPXFjBlviwqW2XX8Wno8wW658JvFNFbCeIouqtm5Jo%2BRJ1JBrQmRxm9TzdrHYZQnoiMHdTvl5dRO20as9FG&X-Amz-Signature=aca737ae9447e22255c0b16bc729fec6392ef0c4fab30f11bd9c7e3e553ceed0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQY7IER%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEPJq%2F65Dv1JkAXYdbPMLKWrcKz%2FlmBrCK%2BXKXWfgR9FAiANLL7ULAtqXQA4NHQnaibdtZhACvXFBpiLAiNVWuyGoiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2bnq6BiwyDt8BfAuKtwDTZxeBi9h2es9DyjoRiCRfKcJg81Hj1Yzq4ZK9k1fPkdgbXuG1LSLGUbAuVp%2Ff0wa5AecFQaTLjcojwP0jeWlOrKo3yS0cVfd8uzcfW7bh73X5mqeR%2BFcVw5NfYh6tn10botTtAmSxqdihitlPZsS81WpcP65VPwEV1CMNX2BXSMeUXFQnz6CzbYoToiCbdvRkJii%2BMD6fxrvErTILgDAqMJHTVm%2BF%2FqsP34KAvIc0ZlO3iLZq4%2FB6LwfpYfcnRQ3VBU2JFkAwJv%2Fj%2F4Iso9XB0xkDTZ1BXm%2B%2FyXslyu0pE51%2FejBvbKoCP4fVzer2mIbE1NPlYO9QqoU0sRD8Gx7OtoehgXBGQ%2BXDZDYk1%2BoaPN3rV2iLu2jTi4WRz3UejuyhM8%2F80gJ6gER5SI03YoAtaDAAJ7LRh7Kv0wTeH%2BYzsT991eK5eidbULN4nFLM4nnnet6%2BwCx2Tm6cu%2Fwq0GD3XnKcEjl9VcHYkGQ0YrPv7Jvqj9nNlUbOIgt5fWhl%2F%2BDXt1XjfC3xNiuu8hsZk1ayKwK7eLZcYkKT2S9SripEBLftK4Vamj0MM%2FdHqWnRgCpvrxUUPC5KSjF07S3y9MWk8%2BWDhAZTK0wQGXNTlKbPb1FzxdhIZwAeimaRBAwyKT3vAY6pgGeHPd2588Nsr32b9lsloSHNeyxBm70H8sFtKaB2NvEKOk1KL4p1M0cAhk5nVmKX83iRNRxYgjRwJMWL9F7VdxoYLmtrhNTJ0Mx9oPyjt80Uf2cc2tnjgFlJ%2BEVfHpYeJPUNIXHZNS8DwfBbOqmthUUsdNKCBHTDmdJIdKBKkQkqmvx1BjyaVxPAKRmaaNXa1WI6ufaeHn%2FL8GFQw0H7Kj4Yk8sX6eE&X-Amz-Signature=a3e1e4b6d839a100db47907df12cd929026f03ddf15bd357ef41454a0e126a90&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYRZRNL3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeO5HSa3Kp0rQ%2BrA%2FA5A6%2B0WJAmSC%2BjcELnDjSvLaMwwIhAMMlItg0PgoXGHkXKbY9DVEUqAtTwWTIMpK88aOxZu1aKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxNAz9RmAB9IEmcDZAq3APViVhleqi62tMDkX5Sl0ttdSy2WUHBMaaWPFqttIjUmTvfkz%2B6tXCawuwH1Si6CYoiUiJsk0OWo04%2FoztcL%2B4vOqei7%2FCBQnHZzgDyW%2BUoSYuQelgipaRZyOxg4oLkPXOqK14pp%2B3LsGvVXzkb3uiTgUB1j%2BwPssenkQU0M2yvZOhcpTycjBdH%2BZSJHk5yjO9Un7yCr0bWxiWvzmngBHOjd%2FgClbjS74ZSxNQydE0xJZQcnuC4LRrLpOEQ%2FhfF2srr5zu7UIs1qQwdjDjjxuZRMxpcZWHnqkGCwkaMhP0dng5k%2BohfknNdWiuxfirZSsiyq9eVXcDs%2FaGvu%2FX1pqcKI3bp7DBhGi2trxkUOKW4BqGe37LtrLuXXC24ddeSVrTt4kwPxuvqhTOYl21aCmogfMiU4RBYG3r6L8Uw%2FzLwXBtQvpGgvDGBsl8WZHsdOxA3j9SBoRg6elTDiBA63WHQTtMpYtLHo3jhi8zxUCwIw4QOvihg3aupWHzoD%2BFcF%2BS5DnKGRR%2FDD4q5sJq4nvwUK4IUF9Tj6lf9r7mBESmb7Lic4pSf9l%2F%2FP33a%2FVR47Jo60il2f6i3MyrJYwpwSS8W47DyRf%2FdBca4QZ4mJZczb6E48NrPHgj1NjY6aDCspPe8BjqkATbM2uLz35Q3g%2FeCQH9ZUF45FrVmGTkCTGmRGuPHpkRuQ5NakCYSZC%2BPKFrEKe0OB6UuO6FNO%2BxhsKkIUMRxE18aHUPUyM6usUg5m14ZTci1d2KrxrHop3i0YvAB3gLOX0cusTiMNf64%2B6Tf5WuwqBPe%2FNT%2ByGi4KSQdYhcZYFHx5nx4kQhcvoKIlaLugiS0gnLTnTlxZ4N3%2BNBGyfbU3e8bfYJg&X-Amz-Signature=341f5173bc7bf68220f8899134b8beb41ef3265cd21e7561436225d1d9ab83c0&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3SPIOUO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8hEbBIpJhtAqOA5PSym92P0EUa%2FHVN%2FjWwYzfRZwVqQIgXglCHHeF%2F67y2vZP%2BxbEDVeFm7Mb5vVfxHf%2Bwo5oHDMqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKiv5xg2%2BT8j83k0yCrcA1a4ZJJs%2BChZsZtUiMEFdbrqXVbNbwYIDsv%2FAaKdYBIeON3cFLwmGIZPW2YpgUWkQ2dyaYCAgiSvMrkHeRIXgS%2B9ULT4nrmenJtTYlR7saoAgGPL80NC5LYacrlyVqEDF3grSwX%2BBe6qzEoPYgxXsLGvznhRprngGXMIpMrMwrEarEFl5I4ywoHW82fnwIg6mcoFRFmGiCd1MFSVYev1CdhaGjJ4DYki87V0cAFG9c0cPq9B4DlhavBP5%2FzSsooYT1jOV9TZcdXaGywQJhMeZlQP%2FAfeos3STVUKFGGG5fYHtX7C9KUxwZxvuyUWKUIrpodNZEgv9%2BKehbsy3R6XPql8MPpZL8SPsvPDcC%2BlleZzgjZQMh6IATqp932p%2FsSbdcOF8uUYn%2BEwIcTyNPmHYdM4UNHKQW3xcWEJeTGzxBw0Y7lZNBq%2BZocZPCks7eHAei5Irvf1twL5XGK%2BLMq9%2BOheoWV8c3tiPXThvHq5zrrLS%2FBT6Az9JHpyKeok0JxFIxNP5ZUB94aAki83FY%2Bl9Wfd6fecoomLwd0Y6dArjjReF7ZxF9jAdzqwr87AAFqwcLjvGk4QFJIR%2BriTD99pvbmz78GaMt0Mc9JN%2Fdi5VPWS2uiuZLVcvoS2qg0bMPak97wGOqUBST9KHNNNJa7ZSlEogMVUZGeW5jj4hgE1U3VHdTqvInpuzBP4d8gchwGyBnktNXkJJXKJERUaDwfRXuz225YtYTx%2BLJ07pHQ%2FCGzYRlSb8Ch4nSeDiZtp8ZCmJJ6C08p7L7RNo3nwAZhs6H0p%2FdXD4o1CdSqFVVVpOp88OzB7EaPfopZaZSL3xBzE3he9oC6im%2BrSVHiFTpxqhAV4rwN2q8ayCvXF&X-Amz-Signature=89e0863b9bff9f92a91650c1a646737be8740dc3349ea2881f42f3bec668c806&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FNG4ZCW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICeXe1X8g0BmNXgxxGM638J3C9Nsypr%2FLnOXh1Mg%2B2irAiEAqEYjRGIyNV%2Boyv5Cn8JiP0pVoXHuLgl8L0NhI6E1yZUqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBZ7vk2Oe%2FQWNV%2FqCrcA6QybI1Yxp3ooaaFW%2FTnOgLImn%2BgbLWVJDDXlb76jYUdVXos6t1UAbeQGLWuliyxbx4LiDUnBq%2FmseNZ3yeXXrfyQsk81XevIglIqZ0CY7SMmlkYcyKgqGj7YimJHrDvk64%2F2y3KYxU9Yu2E0SRr%2FMAbMcFxONOtrNdfv7rkoONvHNMRW4rKUDMloyzmvoFPuEcVI%2FdCVTpMrbC3zV0kf5bNUHU4qBRvh6eduOn2kddgm8IuuUhfQFrjyftrd3PbBNg%2B6bd8hIuNblwnLoaeVEI5j5jcNXMyn9VX7UpMNONJjv3RZH3nxnbswxybnSMftTYn03Y2xxutkhAZ%2B1YRHUEoEOk%2Fv9xJl303%2BOFenfWf%2BzB5oxEE8%2FXNaF9D18au3JnGZuXuDLqgmdeu3ZVJ7ELWBonj0RR9kdCV5bU7nLiuSq4eqAgiqbV8KVQM2Iy43VB8qBZNYjCVwrFYEs20XfdBe8sQC1Z9wmqT0r8N%2FlMJtLYSzly5VKGY2tnOWpFxn8nu7qcGMs2afkIjqNSEGf%2FA%2BAFnVb4sRQgqG%2FFuONxUpZqEZWVV0lgXhzZkihchzL0O3Z3lmiyW1v6PoyeWkYsc5nXSp%2BfFrdwE1g30uLWLfe%2Fvwnwz%2BMq1heA7MN2k97wGOqUBTJlqVTrxOE8lTq5ctvgc7QsfVl0UXNYScaK8FD2v8GIzX7BufIFEx%2Fte8B8Kau%2F5X19JoF8fhY1Oo9z2nxtWnhoClGAKAkDglvFGyjWxUvRMrLzgwNr%2FcYx20LmnBQofVtUvzF3kjrPXFjBlviwqW2XX8Wno8wW658JvFNFbCeIouqtm5Jo%2BRJ1JBrQmRxm9TzdrHYZQnoiMHdTvl5dRO20as9FG&X-Amz-Signature=c20274c25d3f89716a7f347ccdc5db57b8fd6eae7a48d41c8ffdcd4c1050c758&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TI2443T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA7mVMHqHM3wEdag11rDF2l%2FDXe7kAMbPRLKTOFpAWd2AiAA5Rhbfc9xUQwiz%2BOSTxpNR%2BGG0EmPpNqWtG%2FSMqto1SqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9pgTmyDfdedA0EA9KtwDSXfu%2BnScXBDep6SWW0xs7BMTNG9OFSmOyEph4zD7Plw6aGLmuHa1afP%2F78RbgZgPFwjUktv5pOsrTTgneaqZy%2FWTYYNm18yziXLVl0la6JqTvvL9jgcwufwPvU7VSwFgMseoMY3gVxg0l%2Brj52c8p%2BliL5lDRLTUTTIX588q%2BRpL%2Fcc3T8kR1nwHe85rNJV4m9iV5%2B4rkvnj7dIssY%2BjjjxZZhlWLN6wiZ7SzC5u68qXFoIafxxFtw7liWh4xI%2BIbDaVzSlKDv%2BQ45etW%2BKSjJhnmZo7o85ZffOA2RXJktxsv1mGqxh2bw%2FAr%2B8e43UgDwf668Ucan8U1ZW0BfbNoJF963k%2BjxvHJb9ijMCMhnV1jrQyVaaaSXv%2FU4GXjAZZKP0W3GZfNrDeL365ORHx0qZFTIJUTxYDnhTNfC%2FcnTkE%2BjTmB%2FEPAgFs471NOddn%2Bet75tRikjuIJAJccg52kc41%2B0SPp9w31PPXZDNeZXlT0fcJs5TbmP9%2FKkKUlshiA2i5mEW%2BGEgwQ%2F9637R8w9OzkuE0Rvu5F1JwBWjdM%2F8akY5q3kIBvJCEObYgU0fqcA9HiZmZFTdS7PdUjS4q8Y7WgzWVqcX7Eh5EMkCaNfZIK7DYZ4mLNwLWIvEw0aT3vAY6pgFQaYPxoyvtIkRXv34UIo%2Bj3E%2FO%2B6bRla0S3LGjj2wruJSvD8L2aygmPblArtMVmuq9i2DX4gZc0oanw9zitdLMZSw%2Fk3jFUZtgZM44NZPoiffh4ERL%2FOzwJSw4fMotUp%2BW%2FYtnWMSw15Q1DF4fJbgukPQe1wk%2FPpfFxjPdgu6aU0neEFqjsk2HbtybWciS%2BAufH8MkYD2PWRq1jV92uD4EPUgMJLXs&X-Amz-Signature=fa0f1f794137272055e5c4ed6823d919d65d9f1a73a485b975a4316b64e0e59a&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TI2443T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA7mVMHqHM3wEdag11rDF2l%2FDXe7kAMbPRLKTOFpAWd2AiAA5Rhbfc9xUQwiz%2BOSTxpNR%2BGG0EmPpNqWtG%2FSMqto1SqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9pgTmyDfdedA0EA9KtwDSXfu%2BnScXBDep6SWW0xs7BMTNG9OFSmOyEph4zD7Plw6aGLmuHa1afP%2F78RbgZgPFwjUktv5pOsrTTgneaqZy%2FWTYYNm18yziXLVl0la6JqTvvL9jgcwufwPvU7VSwFgMseoMY3gVxg0l%2Brj52c8p%2BliL5lDRLTUTTIX588q%2BRpL%2Fcc3T8kR1nwHe85rNJV4m9iV5%2B4rkvnj7dIssY%2BjjjxZZhlWLN6wiZ7SzC5u68qXFoIafxxFtw7liWh4xI%2BIbDaVzSlKDv%2BQ45etW%2BKSjJhnmZo7o85ZffOA2RXJktxsv1mGqxh2bw%2FAr%2B8e43UgDwf668Ucan8U1ZW0BfbNoJF963k%2BjxvHJb9ijMCMhnV1jrQyVaaaSXv%2FU4GXjAZZKP0W3GZfNrDeL365ORHx0qZFTIJUTxYDnhTNfC%2FcnTkE%2BjTmB%2FEPAgFs471NOddn%2Bet75tRikjuIJAJccg52kc41%2B0SPp9w31PPXZDNeZXlT0fcJs5TbmP9%2FKkKUlshiA2i5mEW%2BGEgwQ%2F9637R8w9OzkuE0Rvu5F1JwBWjdM%2F8akY5q3kIBvJCEObYgU0fqcA9HiZmZFTdS7PdUjS4q8Y7WgzWVqcX7Eh5EMkCaNfZIK7DYZ4mLNwLWIvEw0aT3vAY6pgFQaYPxoyvtIkRXv34UIo%2Bj3E%2FO%2B6bRla0S3LGjj2wruJSvD8L2aygmPblArtMVmuq9i2DX4gZc0oanw9zitdLMZSw%2Fk3jFUZtgZM44NZPoiffh4ERL%2FOzwJSw4fMotUp%2BW%2FYtnWMSw15Q1DF4fJbgukPQe1wk%2FPpfFxjPdgu6aU0neEFqjsk2HbtybWciS%2BAufH8MkYD2PWRq1jV92uD4EPUgMJLXs&X-Amz-Signature=b0d5fceda5ece5b943828f4f9748666487a12dc5653037053510840dc5e763b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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