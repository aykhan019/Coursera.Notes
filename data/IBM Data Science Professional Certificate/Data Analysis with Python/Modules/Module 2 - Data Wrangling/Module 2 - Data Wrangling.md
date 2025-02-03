

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQRERWKQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIHzgTKUd3jg%2FKxjEmcZw91qPur9zCOp%2FFCRgNCnx3%2FQOAiEAypjz%2BoQJYTkqG1y7zWmWjzL3Q3KpLirrqAxuxpB7Ymwq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDDVZ31qNHDLK9%2FO61CrcA413m7cygCBgb6HmdaH5xdXEe3NBSeAOjclsnLlvED3r4p21nktoJZHE1h4P7jKIzy6JDWREvqbFistE69W0Ru9gex11y3nyuw48v9McrmBAPDeK0qU%2FPl3a86RdZvYB8NYPS%2BuX%2BrQXvF%2FrN2Tb5PcJ0q83GGFvGbXQCryTM%2BkXhB1GrGa%2FgKjbtaSehw8yycMBH8%2FKVC625HkDGdlai%2BaUrmxkNS6Yn%2F7wluOUSo4gCs8PGh2o5SlF%2BlvnZx%2FlReqVBacfDCBAClsvzO2Cxnguix4DBLIVfAqG%2BmGiYzoCM8KcHcRH32ZSrD0kW4SqvoIJ%2FcFeHp0q7w4XyWYG5DTSKV8AOLnaPfGV20kWEFoHM8IyOc1HMWK%2FCBZRmZiUNpkqE4XTsjUJd5l0JPze%2FAa7YLvPzYm3Qx%2FBveDa2nh9BNYJNwZlhc7mVAeyp%2BH5hEemkQILbWU5crqqYdi1pcX%2BYQVoNr%2BdOHL5wUSuTfv4ATUNHGRne2wFND4EGYLYiYEPFCkVPOraG2h1ITRDfTCeyFltMNEloulLrXA5cNmqnFa7yFg0%2B9NBIdTqBXG1IRZqu5D4DZjSUDmoIjGpP%2FYLwJsZ2i64Ag%2BvnU7UpfdLaTXHnXKyyWq1GceaMIj3hL0GOqUBKePUUspzK0Zc3dFfCzLciEF%2B23I%2B3vLysCqu95Ppg3UuELjtRL9i7au7RcoCKswDpv4ebCoS2KvmYdSwxzbVbGxTPwKxE5ZQwOwiifRQT4q7O7%2FewCgjbWW6truATcVliB6nCJkMsore1D7niTNqizcRCYFzkOwbMtRpWPeCRr7jved6Hb7N4o%2BNok1W36urZXGHzUyeVu7hO%2F1zsisp2EChB68e&X-Amz-Signature=9ae6d9796e73321dd3a2cca3b9a956682fc8bf76c243a865259ff2c8c967cc99&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B2HGP35%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIE3%2FsUG5x737vpMPY0QYyAFYLwdOwWZYQJlZvHscZuJlAiBt%2FXn8KPWMRBfFjh753jYaUBA4Q%2FU3RcwPydMQq1%2B4WCr%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIMQRVBftlNjn4AKHSSKtwDmuiRLE7dwgkvmUfWRq%2BLDiFOnaAAouKkLn95%2FqrhqWbUQSXADEB47OdEtlAJmJluHza05J2TjM0J7OOtcXuLpDU%2BMiwZaczzvO0oEPi5VFnwYcUFcx4KxjYB6NZocvp5L9JKelu1MoHxV%2F8tZMfkLhRLvBE9ijE%2FTJzzIUcXViEoKarW7HIxC2JWWSYeOs5pmitgTs4Z2CA%2Fnp7O8oKWODsmrAqQQmLQph1N8%2FxxOMSwObLYDwwG4tPr5KQr0ZOScQGcH3EKw9IOBBpUKj3h93q3kRtMRkKxccrI29bXAcV45lJJFozbQh9y2MNhuqyQ40o9kvOoeWgd%2BVxflDxmj%2BUvH4DYQXymeprU2qopNUj3F4YK48pkzUJV3V0%2Ba9yVzITP5Zj2aSh%2FH26jvRsVwETkMVsPre0wN8fvgXjv3XeubuJAtYwDNii6L6QLfxomDn%2F2Q0CzpydCWNFB%2BDNNIdG99USNexp25jfNBVYH4EgGT4sm6dmn5RblNtBubGkNc7EErpK7oJWSwGxC91slo%2F7vdfex7LhtjGvjgtJQk2QNRT50X3hA2p6ESF2%2BvnHlnvQINsMlAXMzFf7JctEciyCTdn%2BzhqqBSI%2BzGHjpPUcc2D1A1Mm3orQavLQwsfeEvQY6pgHPUgSOTDIfmCfuYTxl2iHBslgz6wUNC1dfmboDwsG1rvvVs9qJdLQE6BpqcvsJMdGUmUfYDQ6ODFQGxkBMMhj6sjX%2FCXSQnOF4EeIGrx3DtiB9o%2F8nV4eavLhlbSGoDUnIb%2Bm%2Ft8G4iaH785TmThY4HAtfke4F23jHSGPEjrc2clX1OnTC90IVgzW1ClM%2FJKPapmWNGU9MIDqwoIQJWVhBXGFDg3bO&X-Amz-Signature=c3c4f05cd92a3f2c34de97ac3d5130d5a553a97f0d78708b671080d1763ecfc7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VJSKDOE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCLKiTFfm8F%2FuxnGY11fQuEbOEQ4osLDZ6bG%2FunnhVS7AIgZyajJNmWsMAcdgapJhHvm6ZMUl3wxxSk7QlAnMikhkYq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDKk%2B44IY2tOtZiP5JCrcA7UVwb0v9zlBPq9unXSf1p0DpWBLsosAlr8ploQ3L0BmqAViieRXD9AagxuAZOdTLZp%2BVEvwlGplRG82sw%2FkNRnrOltqPcZcezpSzMiv2b%2BL7qXbc5qcpb64baiGLUKLwXMPD1%2BxlPou71usKChAoVBHVdmFwV6VZOnMSsf91jLged%2FuAw9dS02ivf7%2FyrBvzlxb71oWzLqdUzqcEKZQm6kUqVJgblqdTgUPr5biZcRd6lf4YNIoR9r3IqDqbBZ%2BvOKikh0aEyQX3SHgM9zKW7qXhlgBFvqSppk%2FH8R15ry2Ns3rqNClxfdY0a8D81oMmB0BJDTTr32mFY%2FOlx598M1FsGSdOY6a47SrZe3IVSujkB0BkCHYYLaJSWeooWethnXX1WVfxarHHWW0DKn1bMhBgbrbq8VaOZBAUC5ARpXhNbcT0Lf6LvaNOsqzyDGPxSg174y4btX3%2FyYUtiIffmp1D8hxARga9bEvqDmvMO%2F%2FF6zeSUFsNlMj83DArEKOoiXB15yiTV8UIryB2KnqAXTg70BjQdNkyRviYeIMBoCs10lC%2BcySuYG4m5YZZ48HQhw0mjjfzKc4NyfXbE3SOwvZHYrYARTRTI5p8mMS044qDia2pIp0kLt4IYlsMIn3hL0GOqUB8sKa%2FJt6S%2FMuNNv6ncKRaQFJTw1h8WkBbVjRoJn39iIoNOn2IiD3d7BfW7sEwIqt1mMNMQi4xf3D9ivy8%2FTA2yrP%2F3%2FjGWwu4Bnz6Nf7sI6c9dcys345dq%2FWcYTUBokl3euv50BoWJgk3yzxaF7aw2b6g0Tfffu%2FtrA3MZKRORCrZcocKQmvsRAhYR4D%2BZfJg1A5gra5S%2FkWD0tI%2FAG4dJumcCE2&X-Amz-Signature=e88b8263beb74b9cce07499221039ca907f311442ef27da08c6faebbd25be0e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677JKK4XV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDzSe5JlWkOFOds%2BvdTcjdvb1%2BM4oe6vLYjGD9V0AnRegIgRAzGRIfLbQcpn3Yw9FIZ%2FhR8P5EiW9uAlWOqlvtE5B0q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDLXrp%2BIQ0bqoe63IBCrcA2NGyYRmfMhuJfA2uymZ8EQXN1oK58dIIdVuqHRIO6vGngujQJYPzd0kKb6Lo8R0PeWXu5h1WTPdUmQ7JkUzQGVF6Ia73o8NKKw0Bu61XQ2SPcsP%2BdhrzQRadOq50EUNKzkMu8powfsIQE0skrJxZCTxahHWWE89SiJVGcGUXBKda0TDQE9Uak2xsgcihSy7xGkbRMssVHfDVNVDOhAaa%2F5IbVOI1%2Bh9O1NYWGeMgDI%2F8uixXHYhLtCuHnWPyRl4gM6ETHfWDuM7vK2iYOoIKaoBrqBR6RklOGLxgV46HxQ2i2CgPpV98nRoQVJeaPWY7kCNZ5GgDVyFlOA8ASuFk3QZoMCY4kMzytvOP7Bn4QYaBSDCTBdhvEg6fOlUOXvSCEd7UMaQr2zMpwdgV2QMpHYD070zYBzZooHfAiXpxUQQMNhx8%2FKYQUM3%2FJ9Kx2Xs7eqRovkNNF7DJpXNGa4bIOsLfqU3je47YfLH%2B6ovSWG5SB3fEWHVCPETAY0kQWG6d5ABCyxplhPrXwsonWwZWV97SN%2FfWuAnBK7cQcmdWXKNP%2FQLrCbFsZalb9kERVUH62ExcGghds3PEq9af0LibGZztt4VpyiRX9OoDGRqWp5rXp44d6PtdmKG1Kg8MPH2hL0GOqUBy%2BcBAr12oy1k518SdMz5QPNLCoz%2BNyOBJAjNakuML6qd3yzRhOeiuv7jRdpI%2FNrRPGWM8C9MlNMvEYPLzNU3Wj0SlaJtjswdPoDi0TspFMqI6ppvA2y68rsaiuoHXYnpkIRnoQkWsLSNuIlQei%2BQLTJ44GThHjDLkBis5%2FAow8vqHwLH4b5r6A7XJWJB4rBeliKGBRDLPpwBBZhy9p5OWyRPXhLr&X-Amz-Signature=41531ea0c2b1532c2fce09c48ab42a6c4616299a046aa6140ad1b17706cb18f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QXEWXB5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCrKJBdA7GyGnLqjkdQoYn6rJhjqx5B4iAdW%2Bvh04tQ9wIhAJ9J%2F6jgouJA%2FdIbwhkgGZ4tmv00mrulxdS4a6fuE1i5Kv8DCB8QABoMNjM3NDIzMTgzODA1IgysAigDlWAYxK3KYjIq3AOB2QUC3FExDYAjbn0MZkyKT4NbTVjJcGE%2FHvUc%2FXClKz99dajuOWHlAknxJ%2FWa1COCmfuXveSlNz0Gz9R1jDm6YCmgYxfhC%2B%2B%2FSSE0U753gES1esincRUcSDB4Fgn8i95jKf4I3rcUFiVMnNvcVhqV8X%2BpcX%2FyOue8Tmehr1mUcPDfghQ6Qi%2BiDxfhKYz1QOLRs1X98MTRJZaPGeUXa%2BsdxuOu2fAwy%2BB3YmG8e10LBTzaetVYu0iwxTXSXbNpeTHOehr4%2BHknnZagAzvUr%2BGTflhPBcrmRedgEjq3e68xNc3IOFvRGDXr%2Fzf6qq0G3wcnoM0zT0rrQ5a3OeWe2%2BWYt9UhVb9tQwxPdhiUB6Pn0EWr2jMeVyyaw%2Fv8cSqiOhI158w5vqyroUCIkr9J8AQsvtRQQ%2Fol%2BIzNr8sFRZstp6nXCaluE4hOqjcujNDcQcTjxYCn9RC4jU2iu3PQaWLbXLpxmMg3TrdKyPwxDSryaJJ0iRPr9DmW55G93O8tbPKXaPhOWDz5vmsEqjOtbbXXTCpr%2FYwidq0ac6IUWzDl7knT7y4WumISXYcvvc1AAkesBG8vCe4gjhevsBt8R9qCMlmTVuL5xklKRWmoJ06%2FBPoQvnmOvAjk49hx8TCG94S9BjqkAV9Jq8dyRe4kKffMn1YOpq4Sha6yCH5EYU5wP35Qk4t2xAiEFZA84leOdnQz09J%2FgnVoQxkBun5ihTWBvVMaQmk8Ao8iLzzdobKNZzNhcVW%2FC8bo1HLSLruK4zgjfCNTY5Y%2FaIDR%2BsMW4S8A3kuXqRG5WDzxKl0bWlyiKwqsehxTYRKSLA%2FoEF2MpVHDMKu3abdFzPOHJT02WhE3yXn2KzzmZQIo&X-Amz-Signature=ebddfa970e933687f028602038dc85755391b30841127577b7822e5a93450a50&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBVRZQSS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQD7l84MDQcMLOsdE6yI7GFK4IT3bgRktgaSd1xKRg1TMQIhANJYquJ%2FqbAT7zFDHJ3%2BAh8dQ0%2BcHRLKBnhLoY%2FQvl50Kv8DCB8QABoMNjM3NDIzMTgzODA1IgzyD5G5u%2FZ23%2BbPFaIq3AN%2Bz2X56Y8tSZGgitqQ3kV77BgZTzOJSrBilBavHcl7%2FdlbcLfR80UB5%2F9HGs0P3Wd5DHhjJwGG0Qd4UB4Pk4FYiojPktSbYK9VBL%2FX1hWh3I59vhB2R5YlrjCw9%2FBTam1emfRcqZh6Ah%2BS2UQEd7N60Zsqy%2BO%2FrsdJ9abfod09aiJs%2BSoOZs6E9w7RxcWAhMDfKvjCCS93Hf8j9jYp1XfgPpdunbNIhtQVS3SjSWPClR%2Fl23lKSPuqCGUZjcwpbt9tnzypV4x6RnitMeRNGcBX0vtzZcQvqs4AsJr3thWqSSI%2B39FYZfwJ3ezSd98bQiIFexHxaC%2FvPqmVNUSO3l8vWACVoy4FpuZX0fqy%2F%2BrOIvUnP8Xuq6OlUI2yv7ofDP8bmoy19WvzxqGBVo20hXISe949FIPLoVFQLGROVQ2Y%2Fa0hVs62nBUNnVHYC765dX9jcOgf2hQbNMIol4aFXRqIvzUXChHA2U5utsoLc%2FS3yk9ZaEWuDN390BisN0QAmed6f3LTWtATWlCNomloQ41AmpTQ5rQ1CsfnXpI2%2FaD0oFCTvn6T7ShQGK7Vzs2DGSkmFXZHNss4Nh%2FHadUYPMmM3vB0YAjs1SZiN9fENB0JuULnH0vjTt6lMmpjXTCc94S9BjqkAQyhvueoIPICtxhjjx1nHaNhkyrol2efgCAZJ12juV7bb4Hkqk%2Flyu9SPjLAUVGjsOXmJn41Q%2BO02FZPPDEd33IWDPCUoaxErh7%2BZE1C%2FrrpBHgnuzgwX3bq5wUjJIzRKzaRoNjEWxrB%2Fhbin60unvn7yjwXFKN6re0Ob4N7JPl%2FH70BMc4pOGmkodELbof11mcU4h1M0O5EBkNCCeMzpXNDek2g&X-Amz-Signature=61c60d687aa48efecfeda6ea415440022127828539e67234fe64c2f49c44f470&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623P5ZWC6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDdYllXRJRZTOSsfiTNjiLYCb5xUasxDEAluyAs3%2Ftu%2FAIhALoBpMkw7SmjokWtHkHDO2GO9CfleYHKCwrGAzGrggwoKv8DCB8QABoMNjM3NDIzMTgzODA1Igwq4o4cj92zXUcwoXIq3AOfScTZsHrAmkzxQXCan2iNGBrt1nZ7HtGovAu1VkSvm8AmBWm4Lx6GDzw%2FLRapoQPtgbKc%2B9Uu5li%2BqsbCm3lNDoljcyzLTH9%2FNjsQk57ihM1nu1PIZFI4WarqJfNgq%2FIJu%2Fi3Xn4AHFLLdQM2cfR25YQ2AUqFfMvyHyAIhREBMOr0Z46%2FdBheP0FNfrgFhdF%2FOIa%2FTRJA8zYb44ejS3jng1c9unTwsk1M0LTp0%2B2Eb6WnCjmNfEHx0oY2W4NEm7xqsYsYzd%2BJyCYFmP0afuqhTkjCi48yygSV7wRX8D0BEFuW6DwiJK09ZUXT6%2B%2BxR0jzku1yjPCnGzlGbubG9CJavXzO7OaoX7U7OjrHNzOo0HUctyCsjb%2FxmY0QH4rRAlJRCJfcigZ53kq0w167VoY3enZZXOz3eJpGI5%2Fywo%2B%2BCr20XszAYe%2FyuRqmta%2FRrfo8LAiY2bgUXrQIORyracbeTKWMyR%2BmvUDw6jm%2BZ1PLVgaLK%2Ff6uyH1filNXXv%2BX0M4nv4Qqz4E6YAQe8hwwr6Ue0UUvlXZGq9uvPp2usWTL75lUGPs3UmhsSAPLKSPfgDXekVUw9J6CCvVtsnJUIl6EDbUOuVZml%2FSFrarFmbRwfSHR17kTHmquX8wbTD09oS9BjqkAYkPjk0EGF7bQGirSnTA84Uu7wPVuPXjvZ8WhEvO273HlKg3aCDA7L9r3NLSOTJeSwCE3eFKCDR1w67xfkHDa%2FYSrFzblITq1FTTjXQUWSLgjy7px510JMXHaOzN35Ef7OoUe48tqCfS5GG22WQmUVXLjBJaQxSY9lALKGdeL2HQMFOSuPz7843fvnv%2FxEygaLlWfIJ2ivvpW76YEnAf%2FANjrsVq&X-Amz-Signature=47124b53d5cfcab55cc11e4421c71f71cd9f05142ab631e13d9c851b519ed6b0&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YGFNWPV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIDmlkyV8vmPgyyH%2Bc2wDkbhtus7wEICwzfdAbIWZq2d6AiEAr5NJ0wK%2Bl3Pco6Ijbna0y%2FYr%2F9DZ4i%2F%2F%2FM3v5V5lmKgq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDCh8ebbo8w%2F4UerHaCrcA4XRKnwIyWhP0o%2BjwA651%2FV1RYOdmwcGMsnSTPzY39b0Q7K9iSumF5vg6eeuC3uumt0UdYyl5vEc2Eu9SYj2zoqp6xLYWwUk95NXY8SQDSXrLiid5Wip5QPdBe0iFiNpQacKWphqyh4kTWPkbsr0OMawj1W3g3yXphPJQ3zaHXeg2nE5iOeYDVyrNrXggE3BKQ%2Ff73h9O4sialSwTS7TEmrnpxKU8xyw%2BidQACj14AZN0nbnIFtcYSADoGsKwiy%2FgK8JnmGRIw3yO94rZBB%2FRgbtDzgJNo4M6%2BHpEclPadt3zxYe3wQuM9ujWqsPapbCJZj8CiWdzQtyVxhSncB6yNCWb3R6TUzd1EB5jp2hodUsFrdYcSDeUacXVO21sWDDVEwxZHfVDN%2FfINVp1aONSAaRK9Auy%2FI9s0SFfCHEj2FKmqsqfq1Zl%2FmYUysBze6IzIJUclC%2BEElIKe4BPg6vJvJ0X2V4N5dmmU1O0eEOh0U1W85n7GKMTTHgu8p5VHg7UHydjyFmZQJkYpTCrpEekiT2lwxY2WaPysJEMJGoNed8eHPxQAKnmCmpE86zSJ9N1CpWrMbxSht489pRr5f63WoZzsY1DO%2FS0lENZBatyh%2FoKU8eePCEXdlStiIFMMj3hL0GOqUBTA5cC1SnUlSBEAeCZDrk%2Fhht41T6Hfqat7q2bvJ%2BKfKrTlCD5KpgbFcQoQWUb6oE15crkJsN4RSSMoKZkqNvepv2230J66diXjn1svVB7O0n%2FV%2BbFCa7E%2Flgx1hCi2EPnlH7%2FObFc1dLbdXc2ipqyemzDFDnxNUc%2BNkWi%2BHfJCqhov8oRqUpKJgvcUTbnbyZnYbUj0M7QQnLtD%2Fg7NfNaqTv9LFm&X-Amz-Signature=ab18287c898086b4de4ed9632c1173b537b48db4b0535980d8432531f0f576fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QXEWXB5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCrKJBdA7GyGnLqjkdQoYn6rJhjqx5B4iAdW%2Bvh04tQ9wIhAJ9J%2F6jgouJA%2FdIbwhkgGZ4tmv00mrulxdS4a6fuE1i5Kv8DCB8QABoMNjM3NDIzMTgzODA1IgysAigDlWAYxK3KYjIq3AOB2QUC3FExDYAjbn0MZkyKT4NbTVjJcGE%2FHvUc%2FXClKz99dajuOWHlAknxJ%2FWa1COCmfuXveSlNz0Gz9R1jDm6YCmgYxfhC%2B%2B%2FSSE0U753gES1esincRUcSDB4Fgn8i95jKf4I3rcUFiVMnNvcVhqV8X%2BpcX%2FyOue8Tmehr1mUcPDfghQ6Qi%2BiDxfhKYz1QOLRs1X98MTRJZaPGeUXa%2BsdxuOu2fAwy%2BB3YmG8e10LBTzaetVYu0iwxTXSXbNpeTHOehr4%2BHknnZagAzvUr%2BGTflhPBcrmRedgEjq3e68xNc3IOFvRGDXr%2Fzf6qq0G3wcnoM0zT0rrQ5a3OeWe2%2BWYt9UhVb9tQwxPdhiUB6Pn0EWr2jMeVyyaw%2Fv8cSqiOhI158w5vqyroUCIkr9J8AQsvtRQQ%2Fol%2BIzNr8sFRZstp6nXCaluE4hOqjcujNDcQcTjxYCn9RC4jU2iu3PQaWLbXLpxmMg3TrdKyPwxDSryaJJ0iRPr9DmW55G93O8tbPKXaPhOWDz5vmsEqjOtbbXXTCpr%2FYwidq0ac6IUWzDl7knT7y4WumISXYcvvc1AAkesBG8vCe4gjhevsBt8R9qCMlmTVuL5xklKRWmoJ06%2FBPoQvnmOvAjk49hx8TCG94S9BjqkAV9Jq8dyRe4kKffMn1YOpq4Sha6yCH5EYU5wP35Qk4t2xAiEFZA84leOdnQz09J%2FgnVoQxkBun5ihTWBvVMaQmk8Ao8iLzzdobKNZzNhcVW%2FC8bo1HLSLruK4zgjfCNTY5Y%2FaIDR%2BsMW4S8A3kuXqRG5WDzxKl0bWlyiKwqsehxTYRKSLA%2FoEF2MpVHDMKu3abdFzPOHJT02WhE3yXn2KzzmZQIo&X-Amz-Signature=f7895e00fab41232cad57b1fa9cb126808a8f1ac0f8d7f681059a9ecb2686a9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QO3FHZ7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCuY9rpXIM9kTXoy0p%2BCDkX%2Be56z0BJ1wyk9Otff%2BIJ1gIhAPQz4fjsDnL2xZWLwLT8vWX%2FG%2F%2Bbd016JNoLM5SsBUFuKv8DCB8QABoMNjM3NDIzMTgzODA1IgxEH3FK%2F8UPW%2BP22pQq3ANibdx3QG2Jm7KMJttAm5yb0v8ZBZZBorwqmtmGQhc6IBPckIKd6Wn0V4xOvMjE0gVG8YsNnQwuB1nso%2F1DICZuDr1lUpPVKF0VuhhGOMoxuhD0jzZqherfbRiE9YmnbuLrS3QezD8q7Ko6hY3ziMwJFTpF7Bx9hAMvcdAs22GJpCosx9DYJK6N07wBe8SP0PT%2BvPd5e0QNASpXFllnhoGm%2BwR3L2ERI13Ue88LbuNh4giNdRDw77JMaQYdhjuUQrYfjfcZZkGZtIOZ5bfi2VDNb27Z9US%2F8qpqPQEwgXuGdOb4GfLu%2BgEaIXooP5zMx7dqVFhX2%2BhETzXxC%2FQYKOxwwYhe3YsyUWEUm6DNjwR6QaedVIctQbAiAvXrTFdsziWYBCyJLMJwB2FOj8Jw4JkrsaJtpixI5u%2ByqcYeLVbDni7w6usRzjuli60V%2BOne5Vl8QxsmUsg3nWrPYBshTHpnBXSx%2BmHXWsToOBWYtV1hDBkl9F3%2BP4FwMoqVcFnRG7iTx2vX9JykSyn5Qc6Z93Xo107c7iiJ8KegwPsicOpuyP1WaE2AVaMOG5e1QKiNCE85tVPD3Flq6p5Qdfxy5%2BrskwUCg9Wn5eQZOW86Oa4y2AU3n917qFtQbB9zcDCc94S9BjqkATQGNjfIFzjPiM6FjMMbPBfuudK%2FFlO55pztIMt%2BjJppq1TW5gpCbt7dTnAtYneXXuqMdURIzc1VvxsfcCTNklfhiudV7p93kMKPBqz7yQ%2B6p5%2Fc0i0C3pYpo4C9VPvsMzYkurpixX2e5ktDDDmcc9He%2BQKLFXJN%2FrHFPf2Lr5OQ%2Btn7bpbmIzyZEzpDMDRlCTXBrSPlrBLGjSt4LlcNvtzQihdr&X-Amz-Signature=979f0d0c1f0a6ae30a80bed6cd44f3e506c02c12197526811c924f0727c693a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QO3FHZ7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCuY9rpXIM9kTXoy0p%2BCDkX%2Be56z0BJ1wyk9Otff%2BIJ1gIhAPQz4fjsDnL2xZWLwLT8vWX%2FG%2F%2Bbd016JNoLM5SsBUFuKv8DCB8QABoMNjM3NDIzMTgzODA1IgxEH3FK%2F8UPW%2BP22pQq3ANibdx3QG2Jm7KMJttAm5yb0v8ZBZZBorwqmtmGQhc6IBPckIKd6Wn0V4xOvMjE0gVG8YsNnQwuB1nso%2F1DICZuDr1lUpPVKF0VuhhGOMoxuhD0jzZqherfbRiE9YmnbuLrS3QezD8q7Ko6hY3ziMwJFTpF7Bx9hAMvcdAs22GJpCosx9DYJK6N07wBe8SP0PT%2BvPd5e0QNASpXFllnhoGm%2BwR3L2ERI13Ue88LbuNh4giNdRDw77JMaQYdhjuUQrYfjfcZZkGZtIOZ5bfi2VDNb27Z9US%2F8qpqPQEwgXuGdOb4GfLu%2BgEaIXooP5zMx7dqVFhX2%2BhETzXxC%2FQYKOxwwYhe3YsyUWEUm6DNjwR6QaedVIctQbAiAvXrTFdsziWYBCyJLMJwB2FOj8Jw4JkrsaJtpixI5u%2ByqcYeLVbDni7w6usRzjuli60V%2BOne5Vl8QxsmUsg3nWrPYBshTHpnBXSx%2BmHXWsToOBWYtV1hDBkl9F3%2BP4FwMoqVcFnRG7iTx2vX9JykSyn5Qc6Z93Xo107c7iiJ8KegwPsicOpuyP1WaE2AVaMOG5e1QKiNCE85tVPD3Flq6p5Qdfxy5%2BrskwUCg9Wn5eQZOW86Oa4y2AU3n917qFtQbB9zcDCc94S9BjqkATQGNjfIFzjPiM6FjMMbPBfuudK%2FFlO55pztIMt%2BjJppq1TW5gpCbt7dTnAtYneXXuqMdURIzc1VvxsfcCTNklfhiudV7p93kMKPBqz7yQ%2B6p5%2Fc0i0C3pYpo4C9VPvsMzYkurpixX2e5ktDDDmcc9He%2BQKLFXJN%2FrHFPf2Lr5OQ%2Btn7bpbmIzyZEzpDMDRlCTXBrSPlrBLGjSt4LlcNvtzQihdr&X-Amz-Signature=9b51cbf2c986516d3357f93a4eb3d363a037eb6f903ad9aba9b9560a2ab27b68&X-Amz-SignedHeaders=host&x-id=GetObject)
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