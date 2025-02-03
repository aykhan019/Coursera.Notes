

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OCWKG6O%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCJ5XAi6IZBI3w%2F1CMB6t3AoMfbQBb6wfnPJpujIKdymgIhAJZgB6cl82heRz%2BOfQk5HEA6x9GJGUBdo6t5x92qjfWWKv8DCBwQABoMNjM3NDIzMTgzODA1Igy8APphk6lN0b3Ge8sq3ANyqkc31c6qru8UnThkBKSr4MDF6Q4A6Ce5MOeYo1AD08i%2Fdp01I%2Bl2T%2FRjtAxdq3cUkxI36BolEKnUOA7PcsNZ6lASLGWiUORXLKWBD%2FYLp6YVcX2Rfg%2B%2BYk9FJ1fuYjGaXfTolVq6zeK%2FvKaFTDnYTul4leGfd8zKde7SGdhGPsgPJs%2FS37ANNamxOTkeRC5M7LXu39Ow60vG%2FgMv88NsBE2Z5is0iDf7d7PkiEeHbNj3cabURzDwlKQcICklawJWPe72klE0qcVZUTr5FZ1nRgGVPhs05A0UQydVDIEFtJKO8gSM8WoCyIg3EJ24Ih%2FsY5nO2b5S%2BzT3tn4PeOK%2FeWLx26JuZXYkRwne8uGZHRlAQm0k9LO%2BPoCyuq9Tkp49ANp3Y%2FYTy00szJq7WVdh9M4Tix7pXDZ%2BJ1XME%2FQQj%2FLebVCIBxtlqvw5tQnTwAIT3J%2FMJCx7vihVV%2BiSye%2FUOi07raeZOVQ%2BS%2BKDJ0sANoHtDXNvMCKkUmpVAQ9xj9QvkU%2FI7yVU8nWof2rO%2FwczRf2fjwoa%2BRjfwkrfo5h%2B0fn%2FMUKH5rjaVG7J%2Bpk9Xe7p7%2Ff3a1yC3gJsLnxhdJiJNpNvXkxxP%2FmEY9YrZDBqB0OPTg8z6h9QspZxOTCIoYS9BjqkAS8RPdwtW%2FJcxy6lvx77wM3Jeg4%2FgrfRimSHcf%2BnbVqErUc001k%2F%2BMWFspMEYbFwzNkNs8dtASksbVrUfwe9SV4hKUk5jRiZSr2ZlegcQcYv5Vu%2Bm%2FttsW7Pp4GJDtjAlW6IMD4o5URQ1axS5rBxN5PLZ6nNi6gc4Ty0vAIpeFwdPqpIcq1fWW89GpSf177pSNgUEatRpUhpQfPCWLpY7XPzqh%2Ff&X-Amz-Signature=855a3a321b15bdf667325cdc32bf099ff5348a2c2d351b743462aefea3f0a5d8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KZOBGKK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIFwwHLwMiQU0294%2FHDbDB4D2T626g9hMne8Vp51tqavJAiBLwwInVLmWfZKfcqwcp9NtK5HC3wSMQM40GntNcUNVUir%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMucW9jSnztxfcX3KzKtwD1acTjKU%2FyffD04eQ%2Fl5c1X7OToZOcAMa7JukZFflYyxjC83l2wG0jO9IAFCKhLsBXpS0lnJckaKUj%2FHGIN1wBpfSJKbC0UiT9Z%2BYQO7BN%2BZANHAS4wAXqvx92Ovp5tLguY7ihskdhYVFDaCMRxoxBaPAMpyQ5aMWBizdN1%2FXqhHwzgcmyMqMJ%2Fm%2FnfFwL1n2laURDzl2RlKWMIqV%2FV01OCmQXC%2BcTTWPLPRQXowF7ik1J9RdVLk2VBgUljtNn%2BXoX9Z7xHvrkYT8aOhsk8YT%2F5eIFz3Cwi7bJpxg6X0sDZDb1%2BnNJjx%2BTMPUGnYeMoPL5gYuH0fJ5FT6PPVy0%2FqPocLdVUs7BYNEwlntpspSrDT%2BcKc7b8R5HZRcnlLtgT896DsEmiSuU50wuDszIa7X0y%2B9DQMNa8PzPRx2IBY3f8KekUHRfBvvnBBt9sQxYtEDSMjpwpuIkzI3Wv5FmBuDbssG78F0NCMvFWhdpKKlDygdFS3GCyvcjKPJVQPqAdr42nBVxSnfi%2BxM4SbBnnxy5hOhwdo2TIblUkI1YcUA0lqtLKDFuwlhwxasaBPBDjcKIolTJ3G%2FDCgr35VbgzUXP6kDAR1sozJFxZNJ%2FwKc2pc4YcnaETel4%2BCnlCAwrKGEvQY6pgGtLO%2FbGHg1d5oKbJcVamig%2BbVkCE6Cj5rFya24SRFdf1Hf4P26niuXXTQpAXPnanrNVEnMjJNqgF5fE%2F4e2%2FGbZka1%2F3ECeAE3qms3t7r1OtzXKifG8zwZpWk8Ijll7Xy40DQ7WytUWQHPWDT%2B9TzZSA6ifwAet7EF3PCuHNN%2BJyKkjWMQc0I5e%2BlVgoH8KRJPLNP8jU6GNB7sR9OuFT5BnJFN2%2FkE&X-Amz-Signature=fc65e181fa51278123265f1bfc989529ca84105564b902301a722c92fa04e7ea&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F54XQ6C%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIFHK7561ZnnlanT0IuNEUl4SmQdp8NPgegeB5L4oAbFXAiEAwCock9SVNWRVekv7FsBGOSahcZPkrfizx98ehwC6l9Aq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDFRblSrkMOOz58w8vyrcA8zXs3IX5yYrBriNaiOh0Ib9uiWW%2BjRleH%2BkeXi4n3PwKB5ww9lItgzv8HkqY%2F%2BndLJyBONNqIt1iXv6gcK3QpnhmAmBPxcxLjZERuFiP8DA%2FC51eZjl%2Bs9Qvv145SQLosp6M96v6kzNyUtSO4aVgnGeD%2FX6QLz7NJPSmPGo315DkEEXTIVybsrEWTWMEzeJ2yoD57f5M1gpqvTU98WUm%2BU1ibhYWTqSLN9iCfGBi5T4txC39mA0lVWqL%2FgH%2B7oQW346w1JfEWpdvUDPYdvKwtWF7Tmpf7gPIbqccuuTPKivJNjjxfTVkiFLTo0lICm3eatxFcax8KXzMZrey6UIkRsh%2FRkrHD2NYv1BOq%2FdhDSYSpe%2FqxcWKOOoNWuBNnLs4HyQO4LNgduRPDf2FP%2Bk8qz7W71DXVcVB%2Bg1ApgQOkBvNG2Tb4ordvmaG6yiNpacRpUKhDIxVYm5tVkzgM3F5TNw44SaLKhMPqCSNAvEGRslvr7DrI10NfRztqynsXPyynat9rvTrZgPmJ7YGzQTSMBzaQwtDe%2F6SRkdzfR3Lbj28M7Mamcqmylg1fVAqKdGEiuF5H2YQ9ROAKRzn36pfhNW%2Foogufo%2FQIrOR%2FMyXoz5MzeVKPqkf8wjojoDMLuihL0GOqUB5m2h%2BSIVfn3gHd%2Fv0%2F8YEPyfhFzv5R6SGZlAhd2hGXUdMl3zq0JtyCq2RkWGT0%2B4MizmbYeuItj5hTAOgZkJsQLmx7xq4Gh7PDm8Bs2h1%2FRvZjgLrwcW0C2Zc77mw2r9BaNzB%2F2oAInpG91VzYH6bqUzMUMQhdY5N%2FqL8oDb5z1AnOSjQd%2F1p%2FCGa%2BMN%2Bij5cD5%2B1D3WHr63jJ1kbLlH0AVzC6CX&X-Amz-Signature=0e28eb907de003134881d72850171ba6084cdc0b781a0d890e5d797e219eac09&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAVCMKZM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCICSx499QggDHyIkEzDfX0YtGVW3R9mzPi577EoUIR%2BM4AiBxCjVesqHQg4c%2B5Mt9W%2FBvHnqVE0hXX%2F91Ja2DRiErTSr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMoE%2B7cGdfsMRwX6rwKtwDGHLEBAUBKWnI%2BLU9Z9B5QpRkZrrfEFz6nuQFGbxqMjgUWpLuP%2FICjHN94E%2BaRwT5SOW%2F9t8ZO2L3Cq27Qz4tYnMfEgI3Xa9o6YkxAhS%2B9f4s5a3ymRakNwvs%2BA60B5JxuLd41wqMjo25HCFwcKr9focHoPOAPONoK0JKHQlKHm9VNBeb1wijOya9EkJAPKwECzNKo%2BhArMWtMtofY0EducJrWvi4J%2FRmxYdBpdyuBBQoLi%2F8HqBcAsToR%2B041P3uBUkelzKdLCYLbA4H%2B2yeC575VOBIzAWSfTYQT1oWkENAxUmAtios%2FgTfQjNMMjM62ic3p351syK%2FI6iKGCYS5DYcvSwrlaHHiVeqfFGk%2FGHlkMjZ3sM4nwqWMda41RCbqwdvESzaNHG2J6HF2bVgbyk74qe5WzmCvwOCwHStSZXCGhWjS9Dj8KI%2BD0oaKyo%2BgBsiuetrClMbZhhowC5HXwpSWJf3l%2B%2BO8BAjVPwFt4F08plD2KHGnW68E67DlPVMXfXcpKKKIBCYXFKTOcmlWB52yZaAEOnRdgIGw7XMc5Ciznh8t0np5vPS%2FdJv0%2BXAO8rdvuk4EtNCi9G%2BSTgVgiAf6WRsqUWphLXRUfHyqs8OZH47gBXQIXOG1UMwzqCEvQY6pgElpCXz76KVEsjb2gTg9ORZ%2Bxe3HukX7HMY%2FF3tiSqlObdSNVyrizv8FsL05i59FUYbUkpf7RBVNyC8N8OSlJtXvprWB%2B8cLmJ%2BaCoEV%2BRGpkAZedc0ixOWoYQxz2phEWeK6doFSzWyE%2BP3bo4E1038N8iIV4ZqApr6V7faOpQf2SeV0ojlHWOT7p0IX%2FCwoLWo6euEoMVRVABkLl8mrdoPPbdboYNz&X-Amz-Signature=8386edfc92a56b12f423b9139fc166b6992cf2f3fceddc85d505e21ba88b633a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634KVNVDI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDrT2IFVol0OTH9xi8mheCLCzaE%2FbcKXmuziGD3JFrtLwIhAJ5K7APscfV5xQJq0dL4zD4EGXWq9Gyo0sINffinwMVdKv8DCBwQABoMNjM3NDIzMTgzODA1Igx4yINC0PPnZt757vkq3AMGqsvuaD91IOQcIioywTU5JV5rQJluMdBBWGl0NGcBOfJmyGZPpwps4zoZ6VyVqBXgiLKAFw4C0OpzMUJR46S%2BFOvxG8st7vAQr%2BIEQ9pVYsm5Z7z9Cu1DJDVkeL5pbIYJgcNJ8JMJwJgh4ztPkR976aVM36n9i787qduyWxkpum7oAfXaITd9n3eB66nuec6tHkD%2BRo1r8Wudv%2BOWvRh%2B7fBHMdDVFPg2vTdqZJxLHW9xdRF29bxK9ZcnEWqgUrLMWuvD4letHw6nG2f8rPKveRdY%2BtS2PXo2PSqughjwYtkTa%2FTSIyzPNOu%2Fhx4wlvcgaCu5AHyC9BGvapq%2FaQdVerWy3TkWzvXJjMV%2FWUCVy3CEYu%2BJYm9piYXi0VHiHkzQ81W5%2F1GWYhVDubu7IPpBGxHOc31u5UCuPtc54vtQEYovtylV8%2BIgw5ir4LHd3m5q58Hi0zGlUPNhX1LwQkZUjW0IvVm798G54cn6vVtlEbOenaxq8k1ikSqkUT8knjhKaleI%2Fp0c4nT0tDC8oVpilS%2Fw6m%2BEa1%2FId079RDlubSiPcncz2qDHpbuukY7f3yVrcg%2FwYhsvEmrnJXareEmaofbk%2Fc68rRtcHWU2PufpCCCi%2F8Mf1BBUedeVTTDYoIS9BjqkAa1FCoEMd2wVcvBefdqbE9L0H68L5WsaWLpEW8HVzKg%2FPWH8L4BZC%2F9x6tYuG%2Bxa%2FUrN869ESSKZnxJoLMNJnBc5iGr6%2FG9Q6MKrqgaC1bDLZwwN9RbxoO5cNMS29DZcNuL%2BCIEAd2EUZQYDCW4wrGCbDmS1prCXSTee7vw2uIbcSxCJ6Frep9KEKg32G3SM%2Bx4e%2BTyKnaZdkcP%2BYDP6Bkw%2Fl30i&X-Amz-Signature=e7af38b2e37516654244473e7b62c131d4487b6a03d79701c7e2a5d8e8bea3cc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK5AHQDO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCzT9p0fo8U%2FTRl5CeaK1wzcCVrfKa6sMPnvQ6CJS15RgIhAJ32wujaQV30A6SB1T6drFCJBmJsQElaomEGGi3TfnVkKv8DCBwQABoMNjM3NDIzMTgzODA1IgyahTU%2B4DWu3UYLZvYq3ANZPlYBexen%2BW08HBfN%2BSiqx8%2BK%2BhbWwT%2B4cV%2B39NeR3WqgWkHyRGIEPWt3zALWpfpEhZPufiMrOJ0FNSVxaOIehSBqpj5AlL1Bn7gEo6aVpW1ys%2BTnj46zRGKtl5l8UQFlvID0RGYHaplpHNl1wvFk9d2FW2M%2BfyjZvo%2BXyXTMSa6VApFDuHcH0CCFcM3Pu38wqVIkPEbP8Tz0Jt4L4zDxcMfgRJuINrk21edb%2BpSQlvXjh9rm8p%2BJ9ZFHACWb7R2JgqQKh8cR30l6Zsj%2BgX9BhWbjVUuyBPJ7uhd2E5fGUSKbh67RHFCUud8eD7D6fIaERpn2GqJnZPnKcFGJBFExM6A5LQFbz2eo7mjotoUg4u86WhMKuUYsgV%2FX7ypaANWr6xT0Sfg%2BonYLNZkQJMBmJcacTMt3udPBA94Oc%2BKsvK8E374mSWQU4vJG3NTsRP0tdD%2Fs8UJ8Pxe61yO%2B%2Fz5UeRmGtrbH5DjCy8s8pmIw1ufDF6fs1kW57z26ySPpudTB2XrDspi8UkwFOTdeL%2FyowTVf%2BRMbufyAdmjAeQdum2BBsS8vycXyEuRY8e62eSNxgKCLLWyM3r64%2FR%2BcEMnYripn%2FuUtBqM%2FvhfDctL2YXfXPYvNtwSvy3sNtDCloYS9BjqkAeT7WG2%2FhNs6WJFBzHCmvsxBZmig2VJpODVS39RYXjQproSdtLNGDV63JJYfsgOPRynQKDEId54nb3aLY7XVA7KrIcEK8H4iDUzevfg5Gw8U6IKO0oZUC%2FeaBtS8b%2BAVZN9yn57t8bcQq9eQ%2B5W5MS7K7EDYdQ7JDcM2Wzbs82eP4KzWKtHynpf2TZDTvQYLjq%2F3mGYhqwsS6a3wjFTiVXO05SHt&X-Amz-Signature=7120497d3aa2a0335e91a35ba37958797500601521d2b5474590186aad87a2e4&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QT6BD7QH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQDGsXVSH79%2F4FvwC%2FIs%2BrwNGMke2%2BuK0PMETdvbRN7rvQIgeTO7i1jSVgjv%2FrSewvkip3QgJRhMlzXrT%2FmErJdXquYq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDPParPj%2FPS2wXHSB8yrcA6lM02NLgxepnHeztc8gdCjt994ocKW9iRhPKlZKUHApLNMJMBp7Mi%2FZzVkDVQsRJwovJjFaAVEykPzaRqEU5HKDwQYGx9E64eaVuTdRsq0gMVneA40j0uBrPnulCkrLiEX5iN6qeG1YAxoR5LlG6SfHg%2BA8WMl9IgoKU1wpl810JPoUoDmc8mQU193Xcal%2B%2FiOycdXuBDz%2BglaacUaC%2FWDlLGigKHcF2ffGPgLxoVZQtT7Of6v8M%2BO4NZZKQI4JNBeW3CY4yy3cV1r0lvv0CDZbJm9%2FKALkow0BOzWVdebRCq5jDd18lMJMkvDtOAY89ppLu2R1qW96ZdS%2BCszS9oqxsbeeSmQOwYVu%2BVhh7DzCOGJC%2B2HghH809QREpACc9vwH8aEnl95hm4%2FyOGKmTKkqXfMY6PuCmX%2F85GSiqTYgq4PQh6nf3HBDWXhEKYABf6RzFrVHlAXWbQlzosDWD%2Br1UIyZ6NjqWThlKSbTJeDEhmoBH3IoQyFDFHxWizKhsA4kYiKsZ0pKPsqeODMPJ6RoGh8l3YK6ISGMoyWf9f5V7mPrG7CzRbTPvnPI6smyGHnlINqDfyMJTahCrQPKsb5j9aKvU45ArEHzXdRGxC%2FnqRKK4RxzVRppQ8WSMKahhL0GOqUB5AIpwoEzV5EvAm5BDrkcuFV%2B%2FtFpjHRv%2BmpSpHk0a6aW50GIZ1xDqpxQzzJFAotMhZgDFo0FrPnYdb0rWH8p%2B8%2BA%2FxPs06pP9WOYVxA8qI5e4h%2BaFcJiD6TFOI4Vlo96zj4%2F7oJ6qdkgEUxHXBg7Y3Tpdw7HrTfBQbEowSKwlHB1mdHeluYI%2B7j%2Bu2BmRtuqevgxFzHfa7xiywAF3OsFPxr0fP6X&X-Amz-Signature=b1a7aed074a8510d7f1b2f92b375ed10b3457c7f2dbf84994aacb6d7519e0939&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOSSC6BX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCH%2BOPmzajPdg0Aq%2B4F%2B7fEbxPcHZXtBZtC5NiJxxb2WgIgGPNVwM5KjPu7UVa%2F3Q2OqpIAp9TH2ru%2BXZK7zMo6Ep0q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDCHWTRnihJu%2Fa7Im2ircAyCdRkITbn6sFg4xVyNHI%2B69PRu3quB51FKL%2BdgrCQ6NwSPkeh%2F6cJfFBsj6UIrrJ3FM8PO8Yz8%2BCMK%2BcMBbxs62nNwFMakdBLJMYfEnTsvGKKnxvMJvQzr%2Fu40U51S9KbaVrWP7z9mQChZPM9UIlPTHhVrzorffLoYsPFxG9rVdQHils%2F2pG6wscNwdAKY%2FxFNX5ygv9O25Py2s1dDxtIYSZzlUjdtycpzed2NiEaOl9FQA4HHDKbyZzJRnhCLQ0H21TuKPxf5LBWGb9bYu%2FddD7b54XZcUmY%2BzHB41ipRWXD0az%2BXbiYcPDFylUiGVzSZSntg9oSbDF9ytDgygXsq02s01njjHphrCUdaMVbdekw1V5bI6SCEProti8wFXfIyU6OXQMHLAu18mlFaPrQzgmXfDXtIVbQttjnGo4%2B68%2Fqisu2avATNyR4u8wATDBSTnaLB5rYFqxxD4E%2BQqifNVtJgtEwXQ6anx5%2F1UulsLf28ZFXb%2FRbSqWoGGvaggA5FFqz0mw%2FsqcKjppG6IIfrVLxHws%2FbJ7%2FhZwZm60iaeG74YyeCMNoZxAEGaezqlYc258rqaaR8wetgBd%2Bxezv5BY18OgQk1cxiJC4%2Ff9WP7xsw37QxBRFRm1NQ5MK2ihL0GOqUB%2FyBH%2Bv%2BG3qEFu%2F80jZanlLo9I%2B8tofn%2BbMsF7X0%2FnxLRW8XSdDFnblnytMVx5hGZSUMw2GEYJ4ueVp7bbyOnUKLwzdvvnsDKoWnimVW5R0DaZAesr407DPPsQ2PIAoIr8cUl%2Bk6rZj63itRYB0zF2MfLgHcFic9M9IbSKglsKCrx%2F1oLP41pEHKulqXockNo5z%2BkJ4HVl2qB1zgo3oIw6CX6j2Po&X-Amz-Signature=83403c6285ff63e3ab97ab8f57520e74ad3a814f274ed6b48132444a6dd90c2f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634KVNVDI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDrT2IFVol0OTH9xi8mheCLCzaE%2FbcKXmuziGD3JFrtLwIhAJ5K7APscfV5xQJq0dL4zD4EGXWq9Gyo0sINffinwMVdKv8DCBwQABoMNjM3NDIzMTgzODA1Igx4yINC0PPnZt757vkq3AMGqsvuaD91IOQcIioywTU5JV5rQJluMdBBWGl0NGcBOfJmyGZPpwps4zoZ6VyVqBXgiLKAFw4C0OpzMUJR46S%2BFOvxG8st7vAQr%2BIEQ9pVYsm5Z7z9Cu1DJDVkeL5pbIYJgcNJ8JMJwJgh4ztPkR976aVM36n9i787qduyWxkpum7oAfXaITd9n3eB66nuec6tHkD%2BRo1r8Wudv%2BOWvRh%2B7fBHMdDVFPg2vTdqZJxLHW9xdRF29bxK9ZcnEWqgUrLMWuvD4letHw6nG2f8rPKveRdY%2BtS2PXo2PSqughjwYtkTa%2FTSIyzPNOu%2Fhx4wlvcgaCu5AHyC9BGvapq%2FaQdVerWy3TkWzvXJjMV%2FWUCVy3CEYu%2BJYm9piYXi0VHiHkzQ81W5%2F1GWYhVDubu7IPpBGxHOc31u5UCuPtc54vtQEYovtylV8%2BIgw5ir4LHd3m5q58Hi0zGlUPNhX1LwQkZUjW0IvVm798G54cn6vVtlEbOenaxq8k1ikSqkUT8knjhKaleI%2Fp0c4nT0tDC8oVpilS%2Fw6m%2BEa1%2FId079RDlubSiPcncz2qDHpbuukY7f3yVrcg%2FwYhsvEmrnJXareEmaofbk%2Fc68rRtcHWU2PufpCCCi%2F8Mf1BBUedeVTTDYoIS9BjqkAa1FCoEMd2wVcvBefdqbE9L0H68L5WsaWLpEW8HVzKg%2FPWH8L4BZC%2F9x6tYuG%2Bxa%2FUrN869ESSKZnxJoLMNJnBc5iGr6%2FG9Q6MKrqgaC1bDLZwwN9RbxoO5cNMS29DZcNuL%2BCIEAd2EUZQYDCW4wrGCbDmS1prCXSTee7vw2uIbcSxCJ6Frep9KEKg32G3SM%2Bx4e%2BTyKnaZdkcP%2BYDP6Bkw%2Fl30i&X-Amz-Signature=0573d085579e87a55491375e12648a5363c828337537a6a1a476984b5e185a26&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MS47S45%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQClYm9a7OlSCuO1vKupMHDqzYHb4wx862MZhjctAZYaQAIgORDFovy33bbEoU1ItYVOJYe1Cwv8V0Yy5XxXUiIZEW4q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDPcNdkZK8wgsfyA5fyrcA2EaH3KdlfnzEeuLSMyjj7VOtwmT0dKXZMFERMkKzlC100R28M0zojnKItTSk4H6FQsame2krDf3zpOz1DEEBYRoarGrXiDpu7%2BxtU628Sj%2FtSHesPcybHkoSehZJ7HEgHTmbShmIrT%2F8pFuU0eIGVO%2BZ8PR7pXuW%2BDRASGzXA43FfCpkY9QQU4gukkK%2FWm%2BmmSXLJhvuZOKEUN0CHO5rNnKfC%2BfagPxiYEWTRh%2BMiIPrvmVB%2BMiZmAGN0lrP%2B6yB2sMsznPucUGgMV2xJTD29srEzgYYXI1%2FPAyZb1%2BHf79XH2R%2BoBZ4P0bvjJHYyAei%2Bb%2Fw8ITcq3s989jfPdJzcVv4IrMsAGX9aK1YJ3w9t75Td%2FCq85CBGb7dNk3Jz%2B9BBTuNH9PgtEISwiy%2BhT%2BbpnKuS6IhsU5qNdjUQ79%2BLy2mLYnlDi3Mm2xeKlxKap3ifFlDaZsRDmn59AColvQH2rlRO%2FOFimZlqwLxLpEcs4gTf%2FTEIWP%2FqDP77XDgBe%2FO7BMHYk3gn7ZbtPhaT8q3dmIWOjhnOC4JZv8Elv6FhaKEQJV2tkn7xmQIAmPKBZnxEHCtNWaDCYsy5WFm2UEMrlRLFNOCpzW4rc15jNkejBq7VBtiGDDv1yYd7mUMKqhhL0GOqUBQc83%2FjDEawvH7B3GZlwxRxdY430hkE0I%2BO4LP3Fmb2UMD4OJFPoln9LdLcdrN3qhSh7t8FmarN7SycRW75VLf%2BGJRGqwOhGmkTGoe%2BlRVygEPcVyMLxjdLWOf7WRyn0DTlmnXQrOegwdbTWN9L4iJBzzhwN8ITZmQtp7T1jG0ehS70x86LBRLMcykC8f88xax%2FgGMLEVZy%2BmL4w3x6uvlFMTpVuG&X-Amz-Signature=f44650c8dc65adb2fb85aa8efe03ce75413080b28e6e7f36480991756067ca2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MS47S45%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQClYm9a7OlSCuO1vKupMHDqzYHb4wx862MZhjctAZYaQAIgORDFovy33bbEoU1ItYVOJYe1Cwv8V0Yy5XxXUiIZEW4q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDPcNdkZK8wgsfyA5fyrcA2EaH3KdlfnzEeuLSMyjj7VOtwmT0dKXZMFERMkKzlC100R28M0zojnKItTSk4H6FQsame2krDf3zpOz1DEEBYRoarGrXiDpu7%2BxtU628Sj%2FtSHesPcybHkoSehZJ7HEgHTmbShmIrT%2F8pFuU0eIGVO%2BZ8PR7pXuW%2BDRASGzXA43FfCpkY9QQU4gukkK%2FWm%2BmmSXLJhvuZOKEUN0CHO5rNnKfC%2BfagPxiYEWTRh%2BMiIPrvmVB%2BMiZmAGN0lrP%2B6yB2sMsznPucUGgMV2xJTD29srEzgYYXI1%2FPAyZb1%2BHf79XH2R%2BoBZ4P0bvjJHYyAei%2Bb%2Fw8ITcq3s989jfPdJzcVv4IrMsAGX9aK1YJ3w9t75Td%2FCq85CBGb7dNk3Jz%2B9BBTuNH9PgtEISwiy%2BhT%2BbpnKuS6IhsU5qNdjUQ79%2BLy2mLYnlDi3Mm2xeKlxKap3ifFlDaZsRDmn59AColvQH2rlRO%2FOFimZlqwLxLpEcs4gTf%2FTEIWP%2FqDP77XDgBe%2FO7BMHYk3gn7ZbtPhaT8q3dmIWOjhnOC4JZv8Elv6FhaKEQJV2tkn7xmQIAmPKBZnxEHCtNWaDCYsy5WFm2UEMrlRLFNOCpzW4rc15jNkejBq7VBtiGDDv1yYd7mUMKqhhL0GOqUBQc83%2FjDEawvH7B3GZlwxRxdY430hkE0I%2BO4LP3Fmb2UMD4OJFPoln9LdLcdrN3qhSh7t8FmarN7SycRW75VLf%2BGJRGqwOhGmkTGoe%2BlRVygEPcVyMLxjdLWOf7WRyn0DTlmnXQrOegwdbTWN9L4iJBzzhwN8ITZmQtp7T1jG0ehS70x86LBRLMcykC8f88xax%2FgGMLEVZy%2BmL4w3x6uvlFMTpVuG&X-Amz-Signature=b7e297d7ad650b28d4d6b9530e853c128b7bbec349334aaa08ba814282a99fc4&X-Amz-SignedHeaders=host&x-id=GetObject)
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