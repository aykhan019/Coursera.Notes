

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKCWX5KF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID30cRCur9yzrP8YwkYzf62C3HsstysrqOcrwpz1gEIrAiEA730KOgcPJrsHVTCNYqT3h2BH46o%2B4NefBv2k5dXAT5MqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDrbEQfgt4y0bPWYfSrcA57Huv%2B%2BwKCZnGLc93ffYdAGLLwXhArFvo2WRJfKqbLY618q%2FEUz4WH5MyZoygAOSdYAx9Hnd1TDeJoCJsql1cz%2FAOiAKkYlrOWWnH4DDjjmCiVKjY1F%2FNgcCLUr%2FPeA%2BT8wNy8jzYGSRi7Bn1RhmIogqNA2UouMu6TddTlCzIe%2FbQCTPzszfWSn%2Bah9NN9t0mr0D9jK2exOOaVHK6kClvci2yH7iXOov7rJA7gxPB7zhqhPlmE35ngSmSWLHUGpQwEWq2YUbimVugXtV86rWjcGzZj1iXY%2BBWw1cNZFSmO6HbNL%2Bx6e4xoS%2FP1RHmnLi58ALlmbG3H4BrBkQCMKbmrw1Drtl9SmdIu%2BoFPiuoMjtvDzk7JNzKxMidaRVqusY%2BiovIN7z2%2BtXta7ECMyeeUC%2B5Akp46vNhc5gVA3b0Vfa1O3szhdiwItC%2BnEhwM7CW3MyPa%2F06Q7IETW2fE3P5FCwift4Kwutf2Y4uxAL9sohdoJPrxH6ywwYZp7x0sTLO0OV6xUy%2FQ1GJuuEYoXRd92wXC8S%2Bagn0Thdyx25PGtJvhlTCmVG9Ie9Vyww0sj0kYXLM4x9gyIBAf8ZtLFlHF7fLzWgbjsCMM7djly%2BBOw5ZYEsreoLy2pX%2Bw0MI7z7rwGOqUBzhisAOv6CG2VTEjlcVLrtkizS7hht0lJY%2BIaCGbZBGaxTtnxaD6W1pXWk2g%2FgGhE5RlSGdpqOSlm%2BaxGTAXNzTBzJdmqrqwW3yLiY3FPFDuJTfYYyN09CxL9oooiDhSjdOaaX1TDrMPhszEpSfSBzHnMz6b5ZfaljrXoRkLpuad77HBkU7uV2jSjV6ZZFOXkMtlWESnL5kyhR9VvtwvbphjJvwNw&X-Amz-Signature=74199a1696ee5273afa3caf6c21842619b502397978765410fe3520bee441d72&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPLZG3N6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB4uwx%2FJ4nxgMIGKM2iHMxNqSZgD6%2BkpM%2FY%2BG5mCNduLAiA9ge7hyUTuQ7%2FxnmaS6E3%2FGh2mFYH6zY62tvkklaN6JSqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzfj3Sy3Zdslv7Vo7KtwD4A%2BloqSOM%2Bq9lPqQzQYe%2F9gM1w%2FykbuJ2le2dX8ymZEDCsAnpz425725uJGDbqOV9kHX3LS28cYeQzM3bhKiiCruq3%2BFnoVo6fNV2Vbx8l7wY0Ju7zhqtorADzQVswv2MdsK3vV%2Fs9x3gSKDXcxJcMd0FfIX0JbWID%2FfC9vKwVP3IQHirtVleS7Qy5uQ1KLzwKBiQP7Zo5ZmXX0wrQNj5yjoKNPFRbLWVulOZFf1uMfUVmWnr1E5jkvILv7%2FRiwd46fFMg25yi5qM6zKoSiyESzF8atPphzx18hy0fLINpaopGgs0LCGgWs4So96Yu%2BRa1yo2HkVJrCVNBaHZbkqUKa%2BFE64JZfPYOMutEHTBkpK9e18kgsWL70oCTiaiKjaEZoeplwoCql6CPy9b7G09ddwdcQm9gx0IRWaCp%2BDwxhRgXfO4dX1qeKGKzSqwZZGw8%2F3CnvudYhvNbPDJTwNi5tqUjFTLZIqzwDHfFurENOUsviqfG4LFX0F4SFGYZW%2FcaI7wN0p26bCFDLRYLg6x1rZvJX7vetxAzMmr%2FTpWVbl%2Fiz4OUvG1cVdUy%2B6OcGBsEB%2BQmDJEBdYQzaMbULwQNb%2Fg1RZJx3Mpyb5N5SkR3ObDl4Vf1M3agyHAhkwlPPuvAY6pgHcAGPSKoxvm%2BtTmSNWURw27t3ge51UaJzRLawvIJE6eQ01Yq145Z3AwuK9zBJdzVtpx6ID3QEVcVLXgI7ElOyUxhZE5B8gJ%2BqyGHSRNhcyOMSOd%2BdrK2zeGZa1JrT3LatEcoOGPFzJb2sWi8sXEGFq2Bmsh%2BfUlwPamBPJEOq7MF3spHZvUB%2Bhpki2NEYMiYeOXGcn5k5P7hy1KTV7dxxeVk5aLvhb&X-Amz-Signature=57076cef4f3d02247f6c789e3b5c470e2edcd378fa383432445592c5f3ed885c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NX5QSVS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD01yKhbm%2BNXcBMnE39QV8igYekkVQOhT7uE6SY2nGOVgIhAIxTIHIOKazgmc3ROG8rEULlbztfXQwOXiC3qwqpA9ViKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRg5ivFQmLcDdtPx8q3AMcFtkdMnNQbxWTGsDt7%2BrKHlWpWf%2Brk6amhshn42HETWpcCNkJRggt1PeXRpyNlyTWz1q9lhxzvvHFdGzrk%2FrpYC0%2BCzpgptQ8qg5svX4oK1N4r2tQ4kvYEEvCgVSnKFR%2Bad5XmXf0JEcBuVZUn3yfOaQwI9mL5L80zfLvh0K9nwtaO%2FMR8lsavwAbOIDcdWMoMEAqQYfY6z7NvY2w7LYjLNIR4vYGZNeRyRwN2y5wITalvlwVGiFdbD7WpsLBV6Lu2%2BHS6WlPOu73jEXHArvvK4BgWuGQPaCl1pv%2Boe2GBvlSb2zXLZbbTUfkul36XWUxFUPbEvub5OSKGOZNFnXyayI6i55aXg0X71jKV9mm3IjmaJJH9f4owWWnXiponQsLKrgy8OjCfjnUmTMaVQRjupdMtZVAWETmYh%2BHECEoZwdN2ygNe54CQfCkFMChhcQ7yRT0w1%2B9hHNsLBdykixzaRgd9cCKlJcO%2F0Zt6YWZWMSBALlo9A8YTfVfrnwlzNrrWsfZVn8v4w3u8OIyO8ncr5RqgMyEL2gp4q%2Flqpb8VFkXjy9JxlX2zZn7H7Dod3HuDIVFYKu%2FApBBw%2FOxvdGDl1VprsPTPgiy8tUgnQm1bCFZuAQJoMXpq6ElFTCU8%2B68BjqkAWenE27xG%2Fi1VL1GArZkqVO2LeptiUpsfRQgFyHqG%2Fhs3nBXdL6xYufKfLTYE1yrqnmwjECNnjR9g%2FHcN7riYIUV3Uy2gInuxxSrhIio7Ojtir%2FzXTJveJKp3vRMTynCCvqElvUDRJ%2BS7hSXey9dLnRwdDQ4HGe4HuCoeUzxGeJjnis1jBEMnhDfFRvR1n6KtRtto1nQoeuhn7s9WTVWXuFnpOMm&X-Amz-Signature=6593ee8c406605feff64f55ea5108cc7a5fa2130d6c3034bf1d8da5dc8890c12&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RL5VY7TE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCCdy6icjfBd1j9H%2FOvSS5OTBqcq00gLIN%2B1BCrx8O6bwIgeY%2FgQl8YA99pvNPhaKPhpO5XqNIPEN0u%2FeT2ZebLlDMqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDESLx54PJqOgp31tySrcAy54rFRcPPRTgIcXoCrRE1LsFSzf5CRKDFREo3JdhcIh3d%2BKFG65ERQoe9F9dCEDcvCQw3IoUFVHaqPzA1uuKvJaUNQoPaHvrwh2hYrZaHxjg8mLomFF1X9D0O%2Bt1zPSNh%2BI9uWp8VdMaKQQhaUdPaWrNHIRqCeRygWNFbLJXVda6t8XRQSZjAhQG7K%2BfU4GucVQHxQEjpqhogKDguJftYsCdsl5XaimkZZhBoP53SPdrlfeZIagBGsqazHNXTrg%2B%2BboWZfeBTmmeT6%2BBW3X9kGh9S%2Buo50xFOwiVvfij4uld%2Bn%2BXTOW%2BQvul52qmh7kyMb154305HxncXQfAP3%2BFDJXTOKoOHPkS0zq67%2BS4K%2Fq5ZVX7dGvWMw6TBchrjEQwqhQnNEjI6EW7z4FEE1WRQNZnhq6MEj3dKMPj%2FiRw680r3rQbz2W9wfS%2FCz4bLZXyqe493IMtEKsve9PGVTQ2Ovfdrpg0ylyB9c79V9w4bDPr%2BO41M5LBhL%2BGRGL69CQUh3ERUWPFp8FOSBYnwQ%2BJKpxo0yEPDS04J5dS1SXkEr3occeq8po4Tn%2BqFp%2BrG4nY7p2fZeX%2BK6pIXb1V%2F6ktr%2BmXCXX7mCS0AVAt%2Bw2IYo%2BUPhhNEJmyX1TcHuDMKvy7rwGOqUBUlg5CMzGdxRFLl9Zc0b%2Ffx7g7JEV0DE90H%2FjIA2FAa%2B9Rs7AcAHOdxPLVAw4Hck6l9vubAmWA3Cd3krLxtUC8sZi1NpFIplEF0%2FTAnow7x3ugoeu0WtJpIptoqPT20tzVdgc6eeZMU3agLNWh%2F%2BXHVWCFbXyOj6rWAfJZtwmC32eg6m4FWM2kDAh5IYiOCtBM94SAb%2BhX%2B3DM8oQK%2FpFvKNzHTFy&X-Amz-Signature=51a39a0330bf4f56542dda3708a34b5a15b0781a97c6f8efab7cbfe4434571c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNRQ7QTL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJTBs2jrW8P8qmOczAjOCh3mMezm33%2BUF4LEGgyruusAiBc%2Bkvnray5nBhfvluicpo7X6TDSPgsIswOIUdoajbA2iqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1ZMwDUp%2B94dgtglpKtwDJX5lx1zz2VxM4mJYuilg4Es99cvjb2sAfRzCj2qcVZaB3qVtjf2X5MlPiTScj%2FsgzLyKBUpz8cFhumtEr9BTD1%2F817l0t1EbKKK%2BsNd0K0gk09XKwGxuIPuGKPo9MRmEF2U15T5acMqt4nvJB2S0xoZRmKf4KxcVb3ipgxQF11%2FEJFoqqjXgnl6zmxMPR%2FzmFm3r%2FMRWWd3mEldL2UBkP4PYTMewbEBCFz3ecRFFtYjpbK8o3qSnxYrsdQRftbS7QlvGTPG5P5xSRUn4tlhFSORuMjfgPUBbUXyaR44XIHyYqsSPsVPJGHmndQGsY8fualbHVrhn9MzCClHvjnhn3vSS%2FH%2FEZPW3xDP34jsX2dRhQhjtdf7ZoJQkikdaCLqKCcUm6t4AfFAHOnWIHSFp3go0%2BoL94MDTiMXNcjTBWAIW7Ue1jEK2EVXc1gCQ%2FGNmDRTS%2BTPWDWCLyujkc2VUZA99QFhZy5Heg2QJ87Otq3tQgIcIkpTCxu2BVo8ao8TYIbxrL1F95MVljG2kyKnDWXHtr210fq6eZtb8HB%2BJpRpm%2FEqbfEaQBVArpBNPmub7yLtQ37iIWTcDTnQslkW2fRJNiQ41MbJD4mexe9%2BtI1EJciGKa%2F6llTaSufMwhfPuvAY6pgEExo11jjY7jfwuHQ05rmzuU%2F%2FrAHI%2Bpc5NVyn778pM91XuHQhvgTJXMmMhAExAXvj%2BDjLW1Ttxf4O0SeaGNUabZ2A%2B2QtMQwRIP5e7PyanQqA%2B3d63dwLHJc3wdgqgyMCFqf%2BnXSLPuwON1em1pOxWdjyO8why%2BQUJNJ1cVbPHwqeZ424FjfJ68alM3YoXEf%2F5huNGYhHxaVHXI7fFleFqllK7uJ2V&X-Amz-Signature=ff0b1072a383c988a3ef0abb6d8e5e88613689dedaa39608b291a3cb23ae1242&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVHYTYWX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCv3R3uMdraKC9RLRzyQsU74fXwNN0OHRgHiWx1Akh%2FrAIgXszRaEZVYFeV7PEf7Qj6rHVH3P0CJnOfBTQgQYLAI9EqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKqm%2BVXqR%2FGjf6l8BSrcA6UNMgctOMIFxZ59XE5H99Alg5%2BKtAZo6vIACk7sprQCLv8WvcHB%2B2pbj4fgA8RdPybCgwBO8eYKXLwe7BRO1OhCdZnVMksmS%2FBdXBetWV8DXpjYidNLcrmxvDQMM7%2FY4Z505MWGILZexgqP6pQNzRUdNxj%2FvMPJiZz5KMf3jbIs82LJbwzz01Xv4tXGGgpxX6KZlAV3m85D%2BZUgr5jXUyu9m%2BUg8PkW1bKKPdmz7LZiB4Gya6reR6S%2B7asj43ZCXRSHirnlZXeJliC0uB4GZa5hm%2F0Dol%2BGZnuEAgC8hNmI8M4eXGAyiWmHzq5%2F9ML6xtZVtdVPNMbyhIT%2BUMC3rvFZWbL6CLId5qeY2%2B4Yb7MxW%2FayCA7r%2BaRIcvaT3oDm1i4TyqvQorZw7V0DzuzjVsRwlDd0IZ4NK7CRKCvwweLTzgqW2V05upgWUpI5hw7rXl0pJa2D7oB1s9ddCVPasaoXXhIdIJugPg0qRs9Sl26jHmk0lFVfvqfwNDTKf4nk4ivDO%2BpCCTZtta6ZnKFbNAYGNutBOkv2TJaXk2QFCaEI8raLne%2BQCUtwbBjTnXv2kI3LS%2BFIxIQWzUCsATFCHlPaqmvSYSZV3h0arLN4JWG8Gy3tGi57n6qFmMA3MJby7rwGOqUBNPCKw2lU8ySiCcrVM64rn6TdUPKTcBYGNk54vd0jmC2%2B97Xwi6ckVjDKjxRRtl4XQ%2Fl%2FLcjrFVq1ZH75jVEtsXiuXZL8IeXzF6mCqWIawHE1byOX49LXcHNlJ6UWO9DIrtFcvdNzas85qMb5C%2F0EujbOAgArqKCkmaIUdGHNnb5djj%2FoAoyvDopre2pn340ju7W6Y53SHEtas47rVaZteD7UoK0w&X-Amz-Signature=39535c813fed0fcf3fb159d35ba8c9be1e6e765ea664f1a72cb9a84af75d9b20&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNC5U6CE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICA5faZFTVyrTdX8VJuzZoYGWH1tHpQO9QMROZ6704nQAiBU%2ByY2EwsiVcUioGES54Hv6BJ7yTSEDuQJXbqD9RtcJCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUnvGnK%2Bil3%2FCPgpUKtwDWT7OIx7M5fZtzQqY3%2BazLjzsHNwRHETpGEHFk4OAn%2BmJeoSDGIMJv89RVuDJ33WX11L4kO46xvgF%2BqK3cYQFj61ek1iUb3cuGvS7sH0kR8X%2BRhxKf3S3QY4FB8vh8bL7GDpn2ljzwSpc3wu6jRr8VFRRWzri33eYmQvyWQynIk22zL5tpd%2B%2BwRcOTzyw7Suyb7AF%2BCJ7eh8OqIWvtd2O%2Blz1Wxma29mc1J8xX1VY%2BstAyUxjv%2FjnnU05w7E0V3AjSzFYpijiguUcjk0%2FPNTrsPq30gNIfFvAQIhA6gktPQateBbq5CxYE7pUTwvsx7fUeVl4h2iBJrOB4138btfy85ayy8g%2FDwyLkE5fo98CQ%2ByAcen5XPH9nTTx6X2Q3s%2B0Qn3xSOawAOxv%2BkkcIqFJ4Xxj6gRsulmPg5MbiHMIz4CvzwsYSWucIcxAX1jcUNLCs6bKsqw6P%2Bux97ZtICH6O%2BtrKWa7D7D%2BLiXwvyVmu03A%2FMotJm9MmXrJR5B1Z7VYyicggAhVSC9kwkFiAhyTaHX3O%2BKNwkzLxs%2ByYvfR0XYZZ5qYmu5Z7vz3iMC09VX5UCmeLl9dYud%2BIe2rbt7dFEfOXfFH0si9MFpbtSq5TrMBy8RZ%2Bs2hS10uWV8wwPLuvAY6pgFgb4o5lxSBUL03VBiETvhFQYTZ6WNUByQNsBmgHyPp6qHtzycaTpgiyOBo5W7nczMoO724IcLg%2FYpMsqm3PeHvk0Lpl8H3rzafMtNVuByOAmEKKDGuqSDNGIJZekZX2KfUqmcXdIkChkmBQEOIodliaY1xNkRUKrzVr2Mz1frKBKSq2UgZ2cbxrAJyDMv8rN%2FfImWTCbAEWjSiArzy5TVgm6%2BAfOdA&X-Amz-Signature=c0bfd724c249bda5bd719b6590d3b01d552edb18c478b689a6858851b1839781&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3DFN4A3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGvWEHA%2BgpbpN1yueHqIURYe9Jmn2nuWV%2F5pXUAR8a%2BVAiB2PRIOnfpogBXXEyXHx2NLnQzW1tFStfc0DuQuALDP8iqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFeCujwRmKl7o%2B6N5KtwDTOHCgrPWLr8MxeU6mVltnU2%2BnfaBsfns1Ghll4J2NBYpXxYYnbDWVRHqBx%2BwwIcXztVj9%2Fcuecxlz9ZFaVdjUzSiElNEIVfav8%2FKYLMhDwSP7NfuGSbM1H82UpcRBhqNN9lyjB2tI%2FlyOvVS1cH21Tz%2Bkr2q7aX3DLs4o%2BFLIRpuc82nndG263owgCRzxkKh4kRsQ5Ez4X8UDngPo%2B6q1%2BPoXcR7cN9aZJb8UazLcDu61uTZ6Ybaqdb1%2FNGyg3zgGliKHYrBWZfXOStnmT2Mj%2FYD%2FMr4swPHcrj6VrYI7Ri8wntVUH1PDBpCmvdVwfSVJEcVj6WkP7C%2FxIK7QIJ0JM98l6jW5pVsFka7w5hpV0wnJ1qLkppkNQAj3La6yRpWmBaGzbOH3EzMiIGSEwr0ZPa4OOvbkmIRZr93xdlAEU7GVw4hTWFTgQHnSDGEETEs54SsUW%2FXFog65LGT4kidiGraTme26oJA0sIcO0LeJ%2BK71jvWmPirDzHkc7EMrWlaI1z2UnrDudMqrnz7xl8g1n%2B3NJMGHMajE7KX%2FEVSszqMy2v5jOp12%2FeQgDUgVU1I8OuUKEf0mAUH88T3hJOecppuzBcapa4cdSic%2BhnBnzRfO4vCY736K5vM8wQwwvLuvAY6pgEE5tm0dQuxSyYTJJfaH025aCox7Xg1tqHY5Aw%2Fuu4HZj8kz%2BGyWrUF8k6u8YuSwuQMejsgjYlf%2Bfy8q1WKi%2F5qb%2FYfh3zYLeaFCtn5r%2FXR2nCnu8CuHrXNfCxEFLp3MOM2kPfs2jev4xs2tZO8JQY3zb9rOqalpTM0ymmTendBJSoGqGEOC677auWxehrdC3Dkcz1McL8Js11ytNjjziuyuv1Wsdrq&X-Amz-Signature=f19ba70f7cc796e4feba89f1e2b51c3cd21b36e95476c8a6beb97e59e93e849d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNRQ7QTL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJTBs2jrW8P8qmOczAjOCh3mMezm33%2BUF4LEGgyruusAiBc%2Bkvnray5nBhfvluicpo7X6TDSPgsIswOIUdoajbA2iqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1ZMwDUp%2B94dgtglpKtwDJX5lx1zz2VxM4mJYuilg4Es99cvjb2sAfRzCj2qcVZaB3qVtjf2X5MlPiTScj%2FsgzLyKBUpz8cFhumtEr9BTD1%2F817l0t1EbKKK%2BsNd0K0gk09XKwGxuIPuGKPo9MRmEF2U15T5acMqt4nvJB2S0xoZRmKf4KxcVb3ipgxQF11%2FEJFoqqjXgnl6zmxMPR%2FzmFm3r%2FMRWWd3mEldL2UBkP4PYTMewbEBCFz3ecRFFtYjpbK8o3qSnxYrsdQRftbS7QlvGTPG5P5xSRUn4tlhFSORuMjfgPUBbUXyaR44XIHyYqsSPsVPJGHmndQGsY8fualbHVrhn9MzCClHvjnhn3vSS%2FH%2FEZPW3xDP34jsX2dRhQhjtdf7ZoJQkikdaCLqKCcUm6t4AfFAHOnWIHSFp3go0%2BoL94MDTiMXNcjTBWAIW7Ue1jEK2EVXc1gCQ%2FGNmDRTS%2BTPWDWCLyujkc2VUZA99QFhZy5Heg2QJ87Otq3tQgIcIkpTCxu2BVo8ao8TYIbxrL1F95MVljG2kyKnDWXHtr210fq6eZtb8HB%2BJpRpm%2FEqbfEaQBVArpBNPmub7yLtQ37iIWTcDTnQslkW2fRJNiQ41MbJD4mexe9%2BtI1EJciGKa%2F6llTaSufMwhfPuvAY6pgEExo11jjY7jfwuHQ05rmzuU%2F%2FrAHI%2Bpc5NVyn778pM91XuHQhvgTJXMmMhAExAXvj%2BDjLW1Ttxf4O0SeaGNUabZ2A%2B2QtMQwRIP5e7PyanQqA%2B3d63dwLHJc3wdgqgyMCFqf%2BnXSLPuwON1em1pOxWdjyO8why%2BQUJNJ1cVbPHwqeZ424FjfJ68alM3YoXEf%2F5huNGYhHxaVHXI7fFleFqllK7uJ2V&X-Amz-Signature=709b7cc8f2d6750bd5e97b6f5b09f6a34b61f8c2512967ddc7bdb1b0b5ef97ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAR7YAWL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFp4d1DNyYmSIwTzNWaOWmKQH%2BeTRTvWVDlJKonPqXSAAiEA9PhfZMBaeEC4pOlTS4S4W56G1%2BaTCb882jopYSSOmJsqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCicGPuarTAMiXmJNCrcA2D9LuL83GQ47qiiqhec8L3Pg59kAM80AJjGf%2BLXDknEEGD1S3aR3OAMhXWGnbLmWo1c1Xg85Y6sk%2BPCt7490LozkmA%2Fq1PVu0%2Fm65osdME2Dtrcy2edgMCM%2F2MX7mdYNykWXO6VnfQ9muS%2FXjehZtCaJF6QHxWxywITYPCZfGDn0jkx%2BY1Um9joqHHuSE%2FXI0OFQO95uw2PXKSEjOrvyIXh3hiC7DIj3x7zF6WJ%2BGQpjLe%2ByE42P%2FGLmN7FLgNVxz0t5B3aj8NTnsEdad5U2KdYeJkBQ8Axv%2FduC7xbuPn2kYB%2BAFmZWzCvOXflk7Zpa4z2xxJDrtL7BiTRIJong2quGzj2uZK0PDCYNE0MXhPLYObSrptUzYUOEHzO5pTTM7UUQKYaGheonBkmmTlxnq6H1oy%2BNVttED9JiweDTuKNGEPiepuYbFy9zZ%2Bjvk%2BL069zwqCzgMHUx23xKpIjlbRuFs00hhKxTLyh4sjfAZddPlg%2BR0jIktarrNtOpGa%2B%2FSNOpFHpcxdC9lNUT8i8DCmUtmvJshIf%2BmRuwWnjcoN8ZpjuRbYRRasmJS20B1Miz7zjEbvSkHLBFEZIwsa5Gems9Y8eQIacBJK%2FXjPuHqFWu3XqA%2FmG8fU6Etj8MMLy7rwGOqUBXWQ3VtwmgrStlfn4S4VUaS8N0YftwVpt5XFV5Yqk%2BrT7tu8jEOyeDYxV%2Fd6JYKOKoVKTyQuSxktC1bc%2FpVV9pjk%2BQZnev71urD8i%2FRcum6gDgNG5i72dDT4vrK0%2BL9GsxffI5S%2BTa8EQ9VHVYaSTLdW%2F%2BFDbM%2BOw4wGORYUtYqxOx4Xqj07KPHiNWxPAjA52Nryp0nJplQORNtb5uojEaCYuPZsF&X-Amz-Signature=9b50759da0f3202e0de6317d475087f2a9289d6d027e8eed33a0b07599a26fa2&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAR7YAWL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFp4d1DNyYmSIwTzNWaOWmKQH%2BeTRTvWVDlJKonPqXSAAiEA9PhfZMBaeEC4pOlTS4S4W56G1%2BaTCb882jopYSSOmJsqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCicGPuarTAMiXmJNCrcA2D9LuL83GQ47qiiqhec8L3Pg59kAM80AJjGf%2BLXDknEEGD1S3aR3OAMhXWGnbLmWo1c1Xg85Y6sk%2BPCt7490LozkmA%2Fq1PVu0%2Fm65osdME2Dtrcy2edgMCM%2F2MX7mdYNykWXO6VnfQ9muS%2FXjehZtCaJF6QHxWxywITYPCZfGDn0jkx%2BY1Um9joqHHuSE%2FXI0OFQO95uw2PXKSEjOrvyIXh3hiC7DIj3x7zF6WJ%2BGQpjLe%2ByE42P%2FGLmN7FLgNVxz0t5B3aj8NTnsEdad5U2KdYeJkBQ8Axv%2FduC7xbuPn2kYB%2BAFmZWzCvOXflk7Zpa4z2xxJDrtL7BiTRIJong2quGzj2uZK0PDCYNE0MXhPLYObSrptUzYUOEHzO5pTTM7UUQKYaGheonBkmmTlxnq6H1oy%2BNVttED9JiweDTuKNGEPiepuYbFy9zZ%2Bjvk%2BL069zwqCzgMHUx23xKpIjlbRuFs00hhKxTLyh4sjfAZddPlg%2BR0jIktarrNtOpGa%2B%2FSNOpFHpcxdC9lNUT8i8DCmUtmvJshIf%2BmRuwWnjcoN8ZpjuRbYRRasmJS20B1Miz7zjEbvSkHLBFEZIwsa5Gems9Y8eQIacBJK%2FXjPuHqFWu3XqA%2FmG8fU6Etj8MMLy7rwGOqUBXWQ3VtwmgrStlfn4S4VUaS8N0YftwVpt5XFV5Yqk%2BrT7tu8jEOyeDYxV%2Fd6JYKOKoVKTyQuSxktC1bc%2FpVV9pjk%2BQZnev71urD8i%2FRcum6gDgNG5i72dDT4vrK0%2BL9GsxffI5S%2BTa8EQ9VHVYaSTLdW%2F%2BFDbM%2BOw4wGORYUtYqxOx4Xqj07KPHiNWxPAjA52Nryp0nJplQORNtb5uojEaCYuPZsF&X-Amz-Signature=753a44ec80a2881892e13b88df33c419d4f8bc8f6eadca1a71e3fc696d051c19&X-Amz-SignedHeaders=host&x-id=GetObject)
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