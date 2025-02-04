

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHTKQB5J%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQChT41o2JfLFXbRsNO%2Fllp%2F6Y8Qte9j473YKX2dd6kmIQIhAMcAX9E6VypsbgQHtPsTZfNHUjBf4pNIHO0yf6HcbIBBKv8DCCMQABoMNjM3NDIzMTgzODA1IgzAzJPIz6f9KEBYiTYq3ANby3Q8ny9fm3jOZcBNIYmTekwDmRZlgBwJGraJOkH%2Bcw9MoekXfuFrsJGVwyrrkVpAy33cPMvNWQsPoBT%2Fy2iDDoKC6O4icY7qEWG7DlV%2BIGC3mALWrVEvlIJ88CK64lRjkm85Ws9lCCN5%2B9z%2BujEwDGNGdbPWzk4PuKoKx5PLQJ5Z3Qcfp%2BOANHtIUf%2BsTufS6gE1p5Nw8nMsbwK2b2R5g7pmFK0B%2FqBMjOG6IKpvQcv2bl1Q8%2BrJdf4Srh4jXCg2teyCWUYUkGt7vor%2FpJLEyEvqFPWWaaYvQ3FEw9zF2M75K%2FWMdZRW94IZuOs4PWHWbfgu3ohMAKV3tpa9LXKWTVW1z3hUZfy1%2B1kkInGXiK2Cwls1k%2Fyv7t3WiTjRuPk8lIeysdCCMgIOPvpW9ZGdXK1JLSyyMSwoPJVv%2Bf7xk48t1TEg1UJQHFgyJhOW3bBGustlpTcCypuCb4hBJ8Z%2FcJBYRo%2BBP2c5I8w0KWw8uNQOR93QNW8iuD%2BqIaExkZwELwggyfqzoX34ukhWrxfP3lZQuH%2FjQ9ooo%2Fsr9R8YG%2Fe6xBqQcqqFIy%2B1vhqE%2BCiPAOYzaw2RRzXfml9puwm1gbG0tXFM8MNj%2BM2fnZedEWfeTsXBn71K0n3xbTCm6YW9BjqkAf75EyTKrMG8oOodgbQ3GlxockNK%2FEqfBW9O%2FzPBkYWXT3eDdxIQE4X29DEPMg3HzbVlF6jqevHDrB9bUapENo89a6Ktq2bxsknv0qrgiqtkTlGOG8fQh5n7WkFteyKUvY%2FGWZN%2BuvVRMR8nBtdd7xecb%2B2ACUQ0y3Wi78klmFQRUq9lxEy3Uexr7RWDjKUPHTalm4iDTUmShy0Yw2VkcC4hSF7m&X-Amz-Signature=00a6bdfcb9a901ffc4d4a2b8fabd413d6dba8bf51bb29322e28b5cf44d28765b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUUDPZ3S%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIE7Vwt4pyq2tiGLKaY7I%2F%2F73dpAUHW15zzlljF9Pgh0xAiBx2xLOVsibkQmZT53TZc%2BmUQ7HYQqb7jWrxkUr0Xda%2FSr%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIManKMWVN13LYESrRpKtwDl4MKNLP5LysqrEGLBjENEGmNvTKMTEudahrGsSO5y4sznMncm2FrA76kICdTcU5QthCWF%2BpBha9P4Bc0UKqI5FtrR%2BFfPUsdye0tXYdh6XmjNtEK3YUD8eiUz9JOWt7gSp4WLsSCui3XIk7zDv3lxIISVshikqFNBDux%2FyL4AXls84hBm%2BoEMbrr97ZP6h%2BNgut2CWQBSTBu3QDCmwcZIyfcaSc6AuZtFrEXnF0%2BbV7lPNl%2FRUNG2jp%2BAzNFb6zWnP7C2dfXS%2BSfvyINREZyeKyL7%2FT3QTALLlJb4HUSjeFfEa1B5go6Di%2Bcm4D48gXKmmXifAfRYawxhn68N%2BixslndI5nFB5hbMLwONguaHloOlVbb4RrfWhnlDjwgB5hNPe8DjIUdDI2BTaF060opmmfL9bUIAXI72RH4Mkvld%2FtfHnTcvityScuR6kCtUnD6qfVw2CxBQNSlAqLtGspEwz9pwiNRKKtw9xvFiaeu3W2%2BAZ2TWmuXfKQVT544tGaL7pSJkWPF3wgb81%2BLF%2BsDvE%2BkHYEvZo6w7QdSxU8M1%2F7Ajh3teqwjp5HXcsUnsxrwL4mF%2FS8%2BK4x2ZLAXaIgSSbs85AIMlpaZw7uSM%2BGr5IT2ViXezsgwcglUE34w5eqFvQY6pgGLvKVzOKZnnrZ9yqh%2Fu7s6aCr9Beb8RlpT91Px43TfFKUkJtkBz2xQL2hjTmTnZv2Yzx5QhRvzeusE2f5%2B3VE3xkSEphr5ucxTiBnJaFteT4350jSYfpwbPvE%2FRWNqiI%2BN9tE%2BFerhJmw%2BqyEB5SiPyGOKW6oOWsOvYQjV0Z%2BiXm9Yg%2F6wgpYYcj6KXCrfSZsvl15uL520pzP2Xur90kY4O%2BgSim5a&X-Amz-Signature=8e9b96ad85b7ac92c724c41400198a4a655f0304f3eb30cb568a2ce633b77443&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGSML3CZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQCvuEyZzISitNOLe7xR11GRFyJ7J6hG05jnOuwZVrFN2wIhAL4WNVK5meCUB69lIZYPy2MzJ%2BcY5OBUUbr%2BUwQzooeeKv8DCCMQABoMNjM3NDIzMTgzODA1IgwXOFnyMtncUl2aQ9wq3APAyyjBOlIJ3UujXZCC20CohIWnr8pNmtjM2VtIab3rlEoYUDnYu9flEqsCOt3KgoBGoCIMr%2FNvurIUwDlLgoZfC6Uy6ix2j%2F%2FQ7DIDCE66EVqtRLsOK%2BJbrTCYcn7wSMB3PJNDO%2B5Wt4muwo8M11U%2FixeamJwriErOQY5e9ot4xjKBCHdNeVOfa4Z4AEfTPxryuwuLjQzSA7T9x%2Bl3WJeQotPuMyKFfVGAJsS0IltjqGNczscJnEZwD3kGBSPClOwWykyoqfZg1xxCLNVPAozcp1oVhyIm5xcoCUOvC8MpBVs2juzwns2Lkwu6gXHZWrKsvabddseycZNctqJ%2FEgMGwDO9wyQmNli2CpqvJdDzkjNHg1x64ytojC%2BRIdcqfSR0WXNABE3GjpaRKi5j4kDTxeWPr7920gcXfMVukBY1sjjzF2KQUafSSFC0jvDnlJCuVOAG4cHWZH%2F3rQ32gTqfnjkkc3qpmDWnI0QoRxdww5tz1FOMGASneUGq8Z3cqBEcw4tXJrWNFnNi62VkFVcLIrBrX1TQzYd4XmxoN8ssFnCHpKOfgzu4kKpqxUU2zJt4Dt50%2FeiOJs4A3UVy33%2FYNEP6%2FLUBgPr%2Fu8oAeDbkLO47pcSC%2FhIBumG7QjC06YW9BjqkAfn%2F8sFzRKHQahe3Zs5QwUdyLfTeVxdCWv2xcPVsj8wwc3jjZXh2qJPshe3Q2PEyaLyGL9kjq6Jz%2BRLTxLk4Ejk1MpHeynUJqnRnwNlLTBMlq0xuprVnDWe6gPpMhuYEPodXfO0N2XCZnakpYAioqJXoALfPmlnQqgkSg0APgV9dzedS4eFBHuS9DeeKWunnpx3h5uf42DvjNIZIIEH5lPTMaLpz&X-Amz-Signature=a4224fd8962834c67941f892788f4e9e36e38b7d9cf4aaab24e780133b71f2e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGMBTXOF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIF1ueUPT88GnnJL%2B1PutMOhdVV4iPEWoTud1JVJy%2B2oSAiEAjQdT16I5y1Rl%2BMMpp9oeHHK6LfW0uMTIPyNQQvbIq6cq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDJnV6h%2BJXdSQKvfsUCrcAwAQr%2BL5UVqKtvFczMlNOcrwmiwAmxWs28%2BexskAxd27OjE6Ow3lvZeJRoUj2etJgU1tDz%2FEkicrJMNaSwYfJpmkNVaMIFu0yzRUYsdVhRe9gEV%2BfSZs1fCqu1htfP7DcCiVrX1kCW%2B8LeQ%2F7rCxLiPL1NX4CfeGBE5KxaRehM6%2ByEk5gWtwRiaecjdfjnX2P0JiI9ThbgVwfxAWA%2FFh31gZ%2BgvuHL5d1D7acvLXxsvx%2Bq%2ByOByRbi14sPkDn5MHyEvop4rpxBbC2HYSUChfgNcy%2F3ag16tvSfj%2Fp0KCDXRd4BKrfM%2BN29TIUQapmIyKsIi%2Fsn75s197v6%2BjnWQxVJhrder0lqvXVYsYA%2BQORmMoTxaNV6nRsN4ALgfmiuewRT%2Bxcd6i%2FBxZmm1HefRRJ%2B9KllNsjbBiHbGzP9Uew9JN7nTVPv91nQDAxsUeoLROs3IvbXna9IDO0J93q%2BN1NKnKHOODmi5VROyX0cXvwYPo48%2FbIZ%2BMi9oB7d7i4fEQ6D7wIJfrfKkQ8SD9AZO5svjUn8l%2B2nT84%2BpNIGv5N4LdwG5BNckH7MqPMfZw%2BYlkNfGIgsQ2CD0GwvR6h7DYVbZsMHg7R7Agp1MBJhdx3vE3g82iRCiGvjz%2Fam4GMM%2Fphb0GOqUBky7ci2G%2Bz1D2%2Fbc9YqVrHUxLkA1hDK7Qv7nZw8S%2FzQo5CMLCiUrwU7twD2X6NKLVzZ6BmHA9clNEQA9yeFUv9W7bx31vTM%2Btv3IhZLcCCoA8%2BfCYph3eEs%2BNlfip4gT4012D7VzRklPRCkWQFNn5XxxrolmSUvQrCHyfvwsMewObgWlEHQMWUMk1DPO7p1FiACEpPRXAeoVCLAN5Tbh2Vh76OKDu&X-Amz-Signature=ddf5b3fe72ba017108cf854666a55c0a3de112804ad3624f4b385af11218f597&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVE7TMDO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIGD%2BhfYmZTjBSbZswSHoYoZlHmOG%2Fhg1UmcF0Ms6cDZPAiEA1PTzEt8L6AtB5e52l9LlOW%2BFr2STjn%2FF37g4G1KKK8oq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDFO4hUOBtx3C9IHrKCrcAxDxScMVHUnqvTuBK2%2BYSZ0PoGHLqAQkGKC7ZpCp2uLa%2FgGL7tsycHLDD1cXinnBOZGpX6tSz5izcxo0uk1ELP258hbVyZMxjEcEw1WoswPniuEnFRdZCWSUTwm9hbUNrzzOh0xKttAfRWggfPm8Gj%2Bo39PqDK3oXGtoMR69PKa6f1uP3Je4NkYCu7CqgO17cje8NfQwLHmIv9hfMP%2B7TwHKNppdSV5%2B2NYlh18zDRHBS80x8xak0X4To7cGCa5dEstlRqS6GFfvfR1vFW%2BaMEg1nhg4Vsmldet9dCxv6P3xsuhUVKXwDCngbIMCLi0RH1ZfHMjMYAFbKbujNZvbtu55YdnWhC0Ai7CaWDb7cNpLLjlzdXYOw18AcIWY1EwFUyoOuWirB%2FxXQ5R2S%2BMOKVjmkYLozSwHFwDsDS7nax2kwAVw9jR0c37KAXF31hlfQI%2Bbvy6sTtEEaUnpg%2BPLC0xU8DbHL0ChkrDauPGB7jPP2DA%2BcbChWVz3iDcRqgM9JtziXolo3ao6yjHF1PhvrKM1N3U8WLL02LJXMZ4D81ktFtAjm0X%2BQGEV7obnzl7wdHVhMAcntoR%2BoM95VsVnG144UDZbIN2%2Fptr%2B7hiFQPaH6fuvQAR6ZKWxeBImMO%2Fohb0GOqUBVeIRKgMAa25hL4UI5ikqGSliVI4HjN8kzBY1kAKSLZpBw4CRDKREwjvgo1KI7XDPYJxhVRz4HEdzdmLZYEnnz5bIAFhJ43LPdYe%2FRcWfzn38CuQNQZqmAWGkO%2FUTaJSz%2FcSUumz7qJCCKrA%2FQfUdSJ755c143YNkDlCdvX1qwY8vUzmcQ0Ab%2Fn8uECAdk6IEcvlMHlK6a5h70vMhkbTUY0XmBJCn&X-Amz-Signature=1cf3a13cac21227ca23b355d00300d495a13a85e0f76b0b595ed1f8e89dc93ea&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H3NEX36%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDQ3nRDWGQ8mILLZl3ncTZekyv2J170gKLci9nrL0fYhwIgBw6G1oMBzwgPXMb94HAdzsqO%2BaZj4%2FcPjeLrpZ3E0yoq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDAF1Gruhnu8eGSnUQCrcA10mCtT076Ymrovi%2FrxIjXoTP83jiYqrguNW8fNDI3WUXABG0CDPzNbc7agVNUgZNrhlxjU7L0WsnK%2F0ouVzvpw1qRhEgrbQ35r9IRJbC3ZcDdqkdXD7M6N668kdNIw9KkyX4sWEi942WzlzUJ3m4r2bSWOpeTdXtoO6B%2BhY%2FjrVvHJntxzEQg0npxQtzaXrxiBcf1fQXGCA%2B8mj8uJzI2BsJ9zivZA1%2B4il04mW%2FCPmJ5bJVwKCt8vGM%2BJSjQRxZ922uU9eoN9NqTiNHtkpruN%2FU0UewtendB9lPjPeOIQgt1JMBp2RXoESeEU4xRKrKvq1JyFLdSwOdI0L4lQ7Zrc%2BVN4Em7q7rpweZJkgkPKpmTH6mcFkV3zjx5r1t7b76C6UpJyhvsTV8umduW82fCX3n6DVZJe0XzDXLfGhJ6D0y8%2BfKZ8nJwYDU6jqLIkXdCaY1liNyturFDNYtj36m2Ml2sG95gsl5iw3Vr4paxHk%2BZaFsvqy9eO9efxk9WInTd%2FFbcR%2Btx8neJwlAVHF32lSMbk4N2i%2B7Af2J4PZJoWNo%2BTA%2BpI4NpCojeqbcrDi4WkAHJH%2B9giiJSBaCkBgM8CTZ2UZFeaC8az1QfaaHblMkGyF1w3pgfV7UYRSMPDohb0GOqUBoaYUOlS0Tww9qrC0eWIeVXE9e6%2BkZqHJw3kTRKADYLZFc%2FfzTFXeg7XUQvadQ6zPQGe%2FJsxv5u0xCRre4Q9P934G47jmqHPbQo76DBxG06w0HSOdZUT2kmWVvnOb%2FYiS8dkkDzLZEKiQvPkTLtqrhhqnh1hVNKCvmbApQdLTdGU3gMMrwOV1swQJGySNZ6liLrv%2FBx4M5lk4367uFUVF0JcX7W71&X-Amz-Signature=ec4a92abfb3eec3dbe3baf2a3db917d1581b7246c9f2a3da48eb55389093c7b4&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3KC4HIA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIALc%2FXVEKkxVC1%2Bvji%2FbMauzggMqMhDeoS5Nk37Cvnk6AiEAj4YiDnk9JzlD8nuvi3PPdqmHP9mtPYVVGDxFOTyrMuYq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDGAPKZPUMcjuPk8I%2BircA7gIRgz2QxQRkqkrnWMRGE8JlP6xWeKgybkq4jVxWvGDfy1L56cFhJ21AI71Fy7x75nu7B3JZ1mvZvjDriZquoqGgtOzyfYs8gqnTJCBPE3bXW2hCqmbf0zkl6Sqd6wDj10rcHF1OO4izrPS9NE3bcscFK05FKsYszP0%2BZRGRXT2B32c3%2BQtWGXwaZRT3uGmx0pb22J%2BG02r5ZBVeUdqsV6PNCnI9M%2Biy%2Bm1gDyUUzLgqJ7I0vBnhJEwFE7qjaYSbuXSof3nfPrr034g7x5tAnXsYdwV0CjdWb%2F20xOeu9MvQOi%2BR9NJddED4cpB6tAJYHgWqEu4%2FkKUL59hNk4faFRHUlJ1zLyrCrSbEz2RPSGczIryMJ3cot%2F3IVpfpJCneWh9zY6toiy45xHL5x0n%2F0zBqf5J%2Bj2DDIQFABy%2FiKbfJWe0g1QNOzW4qor%2BE5vGjM6xYAaTJYBXxIZooOZvzIp%2FhQq5V69vpUiCi%2FHQzvW25iCzGN7OXMdWziniRPF%2FF18YfIDGHf8EVIiW1I7UnNMKMGZyCdaCc1JndwCehZHErlFyXTf8gOM9c%2BwaIG7d1CFeB1IxrIaAqKRKdAkqihWSC9XZW0kFQatvWDT%2BEe6qI1aOJel5DCvBVOBhMKTphb0GOqUBLN9K%2FrCwSYPPyGuts0Y4o7VtOjyhsPeglXRzvIPumWySFOz4Wga4KvY35MC8jJ6YBo4%2BeopWOrNJ5s9tz8akAI%2FcIK1SYs%2FVoXEshC1RQJ3oaaNxS0TlwWQwuOK3mTwW3vhbc9T2eUuprUay2o1B4uLcOGlLF%2Blf1qynzNJFeoGnVUaCwMK4DZPMJPGiZ%2BcZZIcU%2F%2FvZVitI1lmcGlkGQ9GeUxED&X-Amz-Signature=62ff872b9fb7708e7a436319d541a223dea457e84d6dd1198aa578bf2df979b2&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFFR2FZU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQC5IQTP%2B3p%2FOChTv8a%2F6SjXC%2Fke3EZcGpSjKJgAwlSyGAIgM2P%2BPDFZWVUVizlCkZ4X5ZZARVaDfzwrFfFphw%2FJ9SMq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDGZfp0zVo2ol%2FfXLCyrcA6oDjuLD0XEseV6A4ad2wTF0YGKh6t7UHwizk8I4gDoRLs82ZrO9Vx%2FJA6xw01Vsce0BZjjrdGzx8bqOZAVhlCo6byPFC6cVOBeBogbp2DjalYDkliOV1%2FOFKe%2BsST%2FRHzHeGaami5aecjE7JVIdpPEUqzfcx0eFjzmT3qkkASgRUmU8OwCfvhLVGiWWpSsJlsyYlrjXBHnXzQ7NjvSkHkthCcNawwqoLCbeuhHLYPa5h1xD51ImyHXmiSvkpvDyNU2vmzF1bVOipsD9eKPxfCyPFSzgbICMVE7z7N5EA6xJml5GF%2BwBnUKurvvLdZHLmhapKpVrvqAvyERJrr%2FhL%2BAOlYUya2WsvBXyl%2B4p1EEpM1d4%2FoNVVwJsQvdgj0KoO9dDIIo919dh7gXKzWMvphBJB6A52La%2FsdCJSzqpwOfeELcrmaR3ZpzJU7CPwOnqj5d7EjmrvU52KZwh4X0QSZgI56%2BKq9ImePv6alV86o2NLuY7uslfPEPFCEw08o4Y9PWoMCsoqVJNDQglN43i1kBOz3bndbYAsCKpgb1ijc0qw0saEff%2BN4n7w1uCLMYodQtXbmDA84FuvuNQMcmsUh7d2uCUDpktqSR2lzxNKeCe5jvmDrj1iU2VelVzMPjohb0GOqUBrqDKnvBYgjNUSgUyKDP1ASMW7ueNBxQ7KoeMiQXJEoTVC5Fo2QzXV7uRTjGp7QHC1l0unW36g19chd59P0zHHCHRTW61gzm4lWyRNdTzMJJPDQfYyZG8Go8JB45TwSP2nS7fsrgSpGqwNnaDhrZCAwO8xuA2KFU%2BEvQWfX7m4I6lUkepxqyrkPfLRVREnxJ0JxQtbGmBsO7BQk6wMoRbuRRk%2FDEg&X-Amz-Signature=94d67c03afe4bf347fc1a9aae8ddf88e164dc5b7a70c1ab5417cc584fdb4b351&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVE7TMDO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIGD%2BhfYmZTjBSbZswSHoYoZlHmOG%2Fhg1UmcF0Ms6cDZPAiEA1PTzEt8L6AtB5e52l9LlOW%2BFr2STjn%2FF37g4G1KKK8oq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDFO4hUOBtx3C9IHrKCrcAxDxScMVHUnqvTuBK2%2BYSZ0PoGHLqAQkGKC7ZpCp2uLa%2FgGL7tsycHLDD1cXinnBOZGpX6tSz5izcxo0uk1ELP258hbVyZMxjEcEw1WoswPniuEnFRdZCWSUTwm9hbUNrzzOh0xKttAfRWggfPm8Gj%2Bo39PqDK3oXGtoMR69PKa6f1uP3Je4NkYCu7CqgO17cje8NfQwLHmIv9hfMP%2B7TwHKNppdSV5%2B2NYlh18zDRHBS80x8xak0X4To7cGCa5dEstlRqS6GFfvfR1vFW%2BaMEg1nhg4Vsmldet9dCxv6P3xsuhUVKXwDCngbIMCLi0RH1ZfHMjMYAFbKbujNZvbtu55YdnWhC0Ai7CaWDb7cNpLLjlzdXYOw18AcIWY1EwFUyoOuWirB%2FxXQ5R2S%2BMOKVjmkYLozSwHFwDsDS7nax2kwAVw9jR0c37KAXF31hlfQI%2Bbvy6sTtEEaUnpg%2BPLC0xU8DbHL0ChkrDauPGB7jPP2DA%2BcbChWVz3iDcRqgM9JtziXolo3ao6yjHF1PhvrKM1N3U8WLL02LJXMZ4D81ktFtAjm0X%2BQGEV7obnzl7wdHVhMAcntoR%2BoM95VsVnG144UDZbIN2%2Fptr%2B7hiFQPaH6fuvQAR6ZKWxeBImMO%2Fohb0GOqUBVeIRKgMAa25hL4UI5ikqGSliVI4HjN8kzBY1kAKSLZpBw4CRDKREwjvgo1KI7XDPYJxhVRz4HEdzdmLZYEnnz5bIAFhJ43LPdYe%2FRcWfzn38CuQNQZqmAWGkO%2FUTaJSz%2FcSUumz7qJCCKrA%2FQfUdSJ755c143YNkDlCdvX1qwY8vUzmcQ0Ab%2Fn8uECAdk6IEcvlMHlK6a5h70vMhkbTUY0XmBJCn&X-Amz-Signature=efed735fc730cb929212233c00942efe641030f94e3c2fe0dfd612ed9a79fda6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YXP25UG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIGlpD%2FYCbBWMqeTGNGqrXr3o6K6dA4GyL5k8I7oq8OiKAiEAsrmdMhAUYjhklNgPlFeAGE209uZGYGYLA9N34JmC1csq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDODG8SVy2vsoAvuLtCrcA0vKjLGAyJP1pm9PKivUvNINgDGOxnWBCqwPSnA4hm4gpfThDyCWmgGs19uCPOokTpxTXf68U2jAiCOOmgV2m%2FWARfF9s7zvA8irsPuKLih7zXqg9EobP0R%2FO7OT1oEWZxpSTIkzKhMUMuRxg7VNQrFQ056NJsvG27E%2BZvC%2F7Jh%2B8i7L4XE%2BVCFxfSIZhxMF9iT0ZoAnfwil9JOrgpMezZamt3fmsSK1eZ41UUkr3F3awFk24xW%2Bv%2BFbwA%2FG0pa0DAbXjWPmGKdf3qzGbSo%2BTEc4dw1wehTR2Qq8O9xZQ90GIcEL2OZlbrMXWE3RkTrhBCGR1%2BCGQuAUgdweHT4QrTKJRQRTAhpf8QNNl0IqUP81ChHmTW7Oj%2BKddfUiBQZc0TXSZpQcf7gQk3zCbqhTpG87GMKhXLj2BDKjE6%2FJVasr6R3ljfcbsk80zJ%2BXVDCHJ150yn6QaCbBmmhGq3rzHvxrc8fcex0VQ5pK3iEwpPjtJrLXk%2FXSn3wEpcKzuW27u0231rXx6PdlYs6rNCjLzDQ09zGSTPaNP%2FKPuZpZNO2%2BPLP9odaOgYr3nCMQJl2%2FbhS35FF9VNcps7ZbLijq1cGlng0uq2aW9nt1nDDsty%2FbCIiiHp3fUI9AItbzMLDphb0GOqUBHC9yEO%2BwrfAWXG4Zi2ukdwxPOZca9iyzDn4%2FllyuTEnDCCOwP8Mi6IydPJieH7PVFuxyJJKzpSv1HOhzroJ8bmQ%2BQTXCuT2doTJ3vis7EICfq%2FSHmqDSBZd3jHf%2BY46eP5QpcU8YVWj%2BSRyE2mly94%2BbOg9BXFtMbKcqGKF%2BVNZQAZMK53AQ%2BZPfEVY2VUcfLHu48d1or9nZBhnWjBN4uaVxN6FG&X-Amz-Signature=7c49fa0938a77c6a049e43f7ecf888797ef4fe32b4ff0d916f889e53e7e82703&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YXP25UG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIGlpD%2FYCbBWMqeTGNGqrXr3o6K6dA4GyL5k8I7oq8OiKAiEAsrmdMhAUYjhklNgPlFeAGE209uZGYGYLA9N34JmC1csq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDODG8SVy2vsoAvuLtCrcA0vKjLGAyJP1pm9PKivUvNINgDGOxnWBCqwPSnA4hm4gpfThDyCWmgGs19uCPOokTpxTXf68U2jAiCOOmgV2m%2FWARfF9s7zvA8irsPuKLih7zXqg9EobP0R%2FO7OT1oEWZxpSTIkzKhMUMuRxg7VNQrFQ056NJsvG27E%2BZvC%2F7Jh%2B8i7L4XE%2BVCFxfSIZhxMF9iT0ZoAnfwil9JOrgpMezZamt3fmsSK1eZ41UUkr3F3awFk24xW%2Bv%2BFbwA%2FG0pa0DAbXjWPmGKdf3qzGbSo%2BTEc4dw1wehTR2Qq8O9xZQ90GIcEL2OZlbrMXWE3RkTrhBCGR1%2BCGQuAUgdweHT4QrTKJRQRTAhpf8QNNl0IqUP81ChHmTW7Oj%2BKddfUiBQZc0TXSZpQcf7gQk3zCbqhTpG87GMKhXLj2BDKjE6%2FJVasr6R3ljfcbsk80zJ%2BXVDCHJ150yn6QaCbBmmhGq3rzHvxrc8fcex0VQ5pK3iEwpPjtJrLXk%2FXSn3wEpcKzuW27u0231rXx6PdlYs6rNCjLzDQ09zGSTPaNP%2FKPuZpZNO2%2BPLP9odaOgYr3nCMQJl2%2FbhS35FF9VNcps7ZbLijq1cGlng0uq2aW9nt1nDDsty%2FbCIiiHp3fUI9AItbzMLDphb0GOqUBHC9yEO%2BwrfAWXG4Zi2ukdwxPOZca9iyzDn4%2FllyuTEnDCCOwP8Mi6IydPJieH7PVFuxyJJKzpSv1HOhzroJ8bmQ%2BQTXCuT2doTJ3vis7EICfq%2FSHmqDSBZd3jHf%2BY46eP5QpcU8YVWj%2BSRyE2mly94%2BbOg9BXFtMbKcqGKF%2BVNZQAZMK53AQ%2BZPfEVY2VUcfLHu48d1or9nZBhnWjBN4uaVxN6FG&X-Amz-Signature=86879b9094d10cf4c2d1528fb19c3a9dcf646aaa2ea11f23329e20ff6eaf63e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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