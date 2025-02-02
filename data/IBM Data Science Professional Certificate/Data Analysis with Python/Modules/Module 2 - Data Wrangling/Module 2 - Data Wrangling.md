

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDPRSVE4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNd4tWm6Ew1tovBpEocvaG3f%2F0nnmL0NSY3pksZKDR3AiBxDKbgM4cNRPTRI0TSQIwQ9%2FThfNv5s0nDRgQ9bPq8DCqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZTcRJ4iTT3zRlmHCKtwDpNbG7DcTFI7hlp%2BF25nnAYsO2uBjyu3cUGbcuAT3VsNBnQQXaf%2B7vWAKbjnaRF4ZoJvAdmBZR%2FYOss3TMaAy5%2FrAWSeXGiZAMVAaA7HbvhwJF3PHhHafW9mhog6EdI3540h0%2Fxz7imA1olSeov%2BpJefJpg34w0%2FiAg9SgnLZnxcHvSTOI0G3iKe9JrR5QkCj0c46W2mOFXrjMZ9FKAjYgvqjbyN2nM2DdKVeQ99t8slFVDAE5wlnbsgkvYOjbUr%2BJiiaqqcLbg%2BlBKMeNGb%2FuJsEwPamiciuhfRCnjRP8Z3Pk6Qhb7Jm5zPlGLhSLNKDII2XreyzWLnngexwV68BLW68avKZRbB6V%2BHa8VAAgm4ujrSGjZl2Memau9HlmN7GgeXEM%2BnDQ3YSC8%2FCBch8FxaaZO15%2Fwndod8Ms4Whdz4OJscgsytdjXlGH1Z%2BxmYdlQPvPm54P%2BF%2FMRzu%2FI1flOosDP0lM3u4QuW6BViHt9H4neXZ3qBngR7vABYFP3QxgNFdbSMt0rmISOTKA7tzN%2BaQGSiKnTeRcW1QalIj7IpV2yaqtahBnwm5KzUtg4EnCZNcfGRIU8sHBqZ9IYOIASIPe%2BsR5vnaLOLi70VLvte5Xl2QziKwL2M26EEwxOT%2FvAY6pgFVat5Lb0JQ3PasmGc0BLvCianxcQpXXX2LvuvU8CYGfWGzZwZu%2Ff9a9ArarSFSvjURu4spD1Zuti0Zz6ro3uaAL9MguqpRDSQV8jiP4XAWgL%2BW8SBKdux7U%2B9o0eaKow1L7rScaocz0gNNJsSC26rHTuPv%2F%2FZpKnWooFtBD0g7XQBIgAFCpMySe3F44woRyJmEBS78LX9vENRwYdE0FR6kEw5EMERc&X-Amz-Signature=baee99a25a1384884ae98445470c3c64c72e56bd4943c4684c6738e2c1351236&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZML6R2D%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmnXGYDHB2uSGMJwejsGJ9i020euRGFNRBdeTuwvxiQgIgHXxW8Km29usM%2BU6RLqxjMj5H278767QMNLh5bt7rUKwqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIdU8ngMtqyJn%2FNHSCrcA7PyRU5mwkH%2F6vS7zdZ7PIdA8y4%2FVFXjz5mPd%2BLIkj4UPwPKprOI1hELifCJWPutLh0ni3%2Br%2Bf331zj1iYoV96%2Fh86jfC2F3FOFh%2BrGUFdaSoNEyrXVe6qrBOZsPpxv0yPwlFIGsEBi6Pe7%2Fblp1YHj%2B9JIdQhcWM2ayFG3YmLabZ%2FFT53nwnqsEUQfDCVx9WPNvWJXk8PCpUR6P0VHjRCC6P778RWSPTD7dnw50I2VT6A%2BqMPKPFtb8NBCg85YyNNPnnh7GWAhsbvSiP6hpEhQxtfDblNHUDiMPVmDzT1vbkbgaONOnWqW0bYxQQVQwxVItCFTROI2GvPO84jo%2BpRkLy1%2BwokRwa7v%2FT8972Oewl0ao2c0Gq13PrKfN0syYm%2FBEbeYbKamWtR%2FWx3HDAlsKFI%2F8pV7SeaagGn9KyFs0PMyl1IR2xBcfMkBKmEb68Adwa1BEy49wLicW%2BbSmpcQTk1lfO%2BVzr5VdhL8NBjJcIGlGZvAIdvfCgELXSKLFvzjy4Um9n6K1VzWUO4s9iXi4F8EXf7PK7sG9J7lnFkNxni29TjnveBQ3EfBJERfb2s%2FJxS80D8pjmZMHbwfBtZ7C2UsSlKigIBSnz5h8lHNqQu2bsCq766jTeretMJvl%2F7wGOqUBnKpKW3GPAgq4IvrT2flhy8jcuKJts65WcghfeIbbUd8O%2BELAL5%2FzU7bB8ARx%2Fw4SP2dYG4%2BfwkqTvaMZ1OD%2FRZ2GlVm9xYDPao8DkWFsDeiP286a07FYcWusVOOMkojfmpV7ytp%2B1X6nxNqkZvGrzHcxcSuNywE%2FT2FH%2BM%2Bes%2Fh4Wjbxq1blzZjjXudkhHdkRxTNDStuWpH2gw8T5WscrTa3Ic3H&X-Amz-Signature=e944cfd77c647b88478a4254748a82284b46dee4a6708b1943dc49f55c6c869e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OTSKNS3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDU59P43RNX1T%2Buj2VnSEG%2BK1TpoiH%2BGjAowHDNZHLNEAIhAKWer%2FVu5br%2FIi7x8G%2F7Qr6shLF1VjR%2Fcha%2BqkCxwXIMKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCSisB97p2POjjBVgq3AP5SG01JEcHp6XfUFayf7I9mRoLKX4D6d%2BMX6PSGUtq8BHY23rFCVQePPo35IqhgtkDA0FYNpJjlCCX%2B8CwFtqA0TP8wLd4oTS1mVgSBKJS4IVCOkhqxyMt9YYKGMvHBnDOODhIBY%2FRndYi0zdVLMfPVSn7bs%2BXXrV0IEP3O%2FDCAOemynPCAcIvxqBICG19pXLb0jpxQ5CE2FcZClAJFENs3cWuLUdgPYTYCARt7ofEj8bxXqWSxE1Qh0ZSJqwNv%2FtDeXNv8fWKPrL3rsXvHBFeXz20Y4U2AUEq69i3fzrLhB1rj5x4jBMVK4rl0T1KAxcpXv8AY1wQQXo5xVx4MIB7KS9X2UgOaHf%2BBtzQB2RprJoEYnDChNHasEcWoPiJI%2Fdr6oX0V2vvqL4OCKA%2F79hMYhEkaaatn7otFqUNrS04y5TrLH98oxkvHbedofUGcXqgssrTYOZrkl0%2BpmOycOK3dra69hut2ZPcEraIxBt6%2BekaVFD2pO6xVXSm5aUjCgPdFsg93h9SvEgwjTtUmue9hdrmOICjIqws8G9%2FIHtwmIGBmBqkea0o23YJWk85OIwDsTVbMTaLCfODCM%2ByFHxbAQX%2BxddYnEurwHzYvVmGf6aYXMuEQx7unKUV8TCy5P%2B8BjqkAZKZUqF1T3IXXmQwcAHMxvYwCDYaOXIopR1t7EkWgoA3QLHhnedtV%2FaccMhh%2FV%2FWcn0%2FKhrJFbgmv7z34Vl9cO34OTUIG61pBOmcNu5Lb7W8V%2F35aeePEjwVIMSRHTvr7h1YJnPecihwo0uZwtIeYBwsC0Rr4ff97jJ4s%2FBa%2BPVJHX%2FPX8tP1BCFhBEhI%2BlyOfc1viHrTTLdemysE24y6%2BbBBXoK&X-Amz-Signature=5624593cc07485ecf0f63896f38fc1ffc668a96485040ff3baec6e8b0f245587&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OTUR4ZI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBNIJFR%2F%2FBDzUTpSnWzAlkT5BPMJ4bDbQe%2BFS4Nku%2Bs6AiBblLb7Ritwjqkt1jAM2sf%2BLms7%2FO8uWMOietonacDnNCqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuY2afv4ZDiwirhq9KtwDwWfHiQCHKTBwR53OAU2Qpod04zPq5cOeG0f5SR%2BUUVL0NFHRQDKJw55mTC42%2FbIg5W0Mbnr6cW0Epu2vRgSBs8YXsxZqYVHgR980PsD%2FbDuUq9PKf0rVgsnQCNammuPKzzdcHAfZ8EYpJHdql%2Foi7zbDAPfQ1wX7F42F1goqQc5WsN%2BInePsxUXX9rBcZztUp3cvyfy8pazCwTuErznd%2Bp%2FLJL7HUKJYeg%2B9EjhoigyJihuQKZ8QFcrZdqhQhKibWh3CkAG%2BHN4qJgUmVcEf3tv%2FkMwARENqAXR527aVegXzCjCB1GJUGfiya0nk%2FeEdpHDKD1p1pKugR4Y59L%2BRAHhINL%2F9lljUrwpE4Ghf%2FEce%2FdAWvGs64OtBC4LnVTcQ8hp64WxmdNFAD2X6C%2BCJIkSnQ7p9vRJuja39nRwYk7Dh%2FJF4Kniw5HJcHU20ID7v9VEyJdr6Fnhi78ZkhPBRyoRss%2BMyU%2BDaO%2FI9jfdaMzvAFIKvQBo7w%2FWJYgk6ue2y9S3QhjngnqaAGMA4TtJUSF9c0B3XBYy3wkLKHvZWm8dC0Bwwlv%2FK0WTYNh6efwBv%2BbOlyiCqbOUWNzkT5HWWTsUyPVxv5C5FbzHyQ7r4a%2BuW2HgRMPTmQPi%2BY48wp%2BT%2FvAY6pgGsfk9By4IpHATs6z3RrJZ3bsBN9TMbmcDjUPfBxDhdykw2SKZl%2Fdpak6Ohu8zCER2%2BYLxJEL0CFgIGiqJ%2BL6tDLPH4h78Aev7zWkLgYXH8%2BY5gtz%2B0Cwy3IzPU0HXJsoBFHSkTmtUbg2nvommBwCtor9170vxm5TI8LITmwbkYR%2BgOaLz1S8JSM%2FFvn1hwezcWqyBSEEWJ7VlsIIFSOSQ%2Bm5bipvsP&X-Amz-Signature=24091b93c1b233a90ac5a94c979523c38a385226c91eddde97bd3a2af204939a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DXD6AVJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYXP6vC3HZg3eyZWUM1Jhdz8IFrWjpSIuXD8S%2F1lzbSgIhAJbCUuNvzAIgomcwBfjoqWjSbmxCOkcZxzNa8bZgamF0KogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwdThEpVLkqYzUvQs0q3AMtlwGw5EwpDo%2FQEV4k13NMFeqDAKNRXS8%2B6Rv9gLDPe46C53Zh7%2FsUxwM9qpGvX97wkI6vbErTi2hofXOTOPjhr1mVIIJW%2FuHhIdYIXAYKNQYiZYU16wy4cXZOEh3Y3dQ3hCp29yaJBWxA9my75jAfQX3fJy15sHWSPSDWp4mCO2ycwiZKo9XumjJQLfb59EY4drxOrOmrMv0vZZVEdl7rH08IHlsgW53f11OIeOqbsowDkYrDhDsXrGYXdGVIjGFn6K48fE%2Ft%2BgjNgbw9Xx1eIo1EmfZupzBfTDc%2BdsFabHOn9q5YNBxNr98RkQV9d43PDhCquNJXTSAyvh6N%2FpVZn3nap%2Bn1tc2U9bGPGjR7nKwCQXQfZ2xYCI63wPQBFq3%2FI45INAJhgvdoK2%2BWco32NU1HwHXPzuObq5XyAkl8dRSUVoV6RKgNzakk0zQnEZOPK%2Byos31FN1MA9CP5OTK%2B9m%2Fv2%2F3CG%2F0YR6jyUgsC5hNyg%2F2Ak6Hv5yVsek86ZsC5DjAFhyVUyh2nz%2FU7xEPG9x6b6fMmg7e7zxbgJq0mge7IgA7kmQXseWrbcL1rgNfp86xf69ybJrFXEjjC8Ek03HWZQ6k%2BtTTsuQf8pxjkIPTz7KnbfZXs5DJA5DDM5P%2B8BjqkAUsg8e4Pj9UzySFUUme7Heied5bBgoAzW6pp9jcZLcL86NUKqbZim9YL0lHLQfDTcVwegmb995r7%2BlGHxIwi%2BzOaqUBjk4zY8%2BdnfTRbAe3iZdyf1Z9%2BTSKh3JH7S%2BBXcQh3ynqM%2FasDWznU8ErDNQqlVQwvFBExLxCywfvuTLM0TfYFvXx5SePTQJMKJIs68JJ67LHg7tr1T%2FyZBe%2BnK5XE%2FBRL&X-Amz-Signature=f8551130aefe06761a7734e785a40649367d36f348dbf440a237ea7011a1795e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6PI7ETC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAfX1Wlyc8duihRih10egkt%2FByE%2FNMJTPpLTMK9X6WHAIgR09eHig5PcqksbX2dWKI2%2BXnIKEbifWIMBLgqwUsOWgqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMGuLMobCGikeHitBCrcA2lW%2FRJ3om98qokBg3iwl0cAy0ZRHx8k6Dj2SSTX%2FKh8va0jISm7Yo114UgymSHP3MoHpbSOd1Y3WTMoYN92B0jsVQO73olbpOlAbkLKmBOgBm6KqqWoCw%2BULrmKuXwDw5n9%2Fl5f6dJ9BO%2FD3ou%2BLI1bMuaqmE3IrqeUgvEhTv7YP9MlZDQZH4c39N1GyhF5rIrkj9B5uRXWF0Kz5dsjrA1w%2FeGb3qwIJqFaXDWbYigOioFsMwvaVvzWrK6xt8FQskUnuEiCV1gc98kVaqXOZ7XMZ%2F0xsHkD9C3cltT29CeY7wF7ENTXOQKIZmIuIvsPcxierhLzm3l57Zrl7JG%2FWbp2bduBB%2BYGA7S1%2BfbkMf2yzUtx6ueKvkeDXwnNIaTNJU1x5e41iv4ZUXoUQ%2FAfU%2FRabmEyqVptDyCSkea1c5QocsddjKeF5a1YF7ubMw9dIxbBAM8dRBwWKleG6jOUKuRUSUTcNvqmV2Addt6RL3ILrCaTtIY7tf%2Br7Gz%2FTUcNKjKar5ylEpC66vrN7D0vUJlEAA4ToYCH%2B9L3N0BzOPXKvuO4ZzC6ZE6Tb668oW2PNF15usmvzJIv0UCapWQZuaeXn%2FD%2BwxHiBzST9sVCie7BOjxgy3Q2gUYHR9tZMKfk%2F7wGOqUB5%2FmmYNjUxWAcpkETymfstMAcXD1lbThGJGm2ZdfDrHfyRht%2BauaUv9WmdxB%2BwvbWEWLxZJg%2FnmG0k0AU3llTaulj0zqVtybguTortIHp%2FSwa0E%2BE2u82RZSBdGOTCn8TI5RN7hvdx4dVUUJZiETLo46z3j%2F%2FZ765tb46qiCaHeeqe0F2FkCoVl1AUDCJGR9HzkvwY5vWar%2Ba%2F3ic5vLgy4GTnIe6&X-Amz-Signature=bb4e83e7b84d95704b37ebbf92a425a33cf18a32463798a0a91a1ea339d45a4d&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BML7FWT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBDER6a8%2F%2F32BnGwvWxr8QoYP5G5QkHjXnJlxAhqYtYVAiEAy4y9vuxxDrwGwc0fK2QqUO7R%2Fyp9d1%2BR6WLiWEXeBm4qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGLVl5yMNn%2Bt1gvQ9CrcA%2FptDz1M48DzGIY10sx%2FBIUEUX0jIGpQCD94snfeIW5MhL2ABBWJ9mW%2FUN3Fz1owpeXQ3JUfy554OWKOLzIsM4XrrSJpEbp%2BNuwGnvo0WEK8od3i7%2FCoh2VEvah77eqYfm41U0PkBDK7dKenYAKOLkMfsY5GpgSNPAZZhhNI%2BiwrAYbsF59O0%2B1%2FfVz9zIWnR2DRSYiGoMXYD7EiFo9rbccxdGVTA20KEcnWsCfKXAGj%2FBMzW%2Fedw6wFNP9HaOBnSXX2LbD5%2B1CO6WeJ17lTIQAyKFnhULh1z6V6Vq5ooCwf9HvAxL0rYJyBhbuC6SyRco6V5Bdsn3XAw0IXc9%2BiEGkHWqw8ORMm0AEatMt3e6nRb9RamEd%2F%2BNJOeFsAhxzQ2RmdYiW5FA4CouO77WSohsHJkZfqaKikYw4p5bKXshc%2B2YH31WEGTTzUr%2BImmzjQLD7cq%2F0D9s%2FddEng1EXyp5uUwKqqG2n6bKcQ8gOpa9jAffQ%2FmR18Z9JY29w0s7Zk%2FEJLWbqJ0dLLIwUKcOw8loBigGylTdDgXDHP1Nq5d4rUyw1JbYE6rdgfPA8q6HGYq7e1vphfT5DGoUeCqwgnyeeo0MHpJwxPVmO5%2F4GzoaTmkf%2F24qwfe1hj7g3lMMHl%2F7wGOqUBamgY2%2BS%2BrZrAsQbY6%2BiSWHuDX1h3inKgfwN8FdIR9DEPDOLBskYeSD9MjqRoHWqt5VvfhyH6wo7AQJ9kjFaM7Dgx4QoD9Qj%2BJ5Xn4Rd5bPngjoDiLnp1FRH5hfWbHdRmlqnc0RV4spgKWkhbBJuyko11N0naFVDxAkqIJY6d54cqTOFxBD21kM%2FhfPgOUPUps5eGttShGLAIlXg98X7EbPgPBbwY&X-Amz-Signature=0388756a44656d185f8d1e0351115b00a6336b60542bd071e3fd1d030d25311f&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466244LOF5U%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDVKVdSW%2F6TOEfWw4ux2HUjpZsMxyq2oW%2F2d6D2FT%2FzXQIhAN%2FyPHcwOlPWI6pDHTwyJ18Tr47Vpn9kQpentTZW5MfUKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwCzqPchBhJb6WmPbkq3AOWxLGtQa9aySX9PZwxQNz1addFtAEPU4PUKAonCzoivPgbKyUMesDqhmv09SvGn8KBXdyVKKTBhJm1QdpyeKqC3CHguxE4ZeXGW4%2BYwRTplMLt0HJTmDDGXyiR83voasI%2FQSP4UOTf0%2BHpsko20vycxZS2js0beL1ILkgs%2FRkll%2BNoJy36mIoOUPjB8aac8lIaVqg60RINkM6Im5XVYL3v%2FlK7jEywag2k2AZ7lgR6hJbiOJrjYNi1xHl%2FaHlzAU5qA8%2FI8SBF9CYCK%2FoUJ6XL6wrxFjhl4ADFsLivrNeaANWwhddvPc4GvffFG06gia5bAxAqHdXDBBcYp1esQTP8mE3HvlkJXqD4bBNAUFgS4T6gAqpkPYKm6H2JPRHMYCQrB1U0MrahJeT8aI1Y84EcKwxzv63Zc9tz8%2FoB0qnKD0OVWLXxWCyNZhsUbduhwpWNOhJA%2FMduuiqH11wlD%2F1UxNs%2Fbkc0IRIqVrfXjw%2BgOE2o5UAbK4LeJ5ooM77%2BB8c1K5bsju0BCkVGtkJLNrranJwhjXLM0qaw8H3f2Ffo7PtTL5FFviMLVo0tRp7B5p12cB%2B%2BtSDlcHzvjHOLCQh78qp%2Fbn%2B%2BaLubIMEVeRcw6jGSgyBqWFbaIx9gkzCn5P%2B8BjqkAU1kdoUS81REME3V%2BVrI5m%2BgcsFdwb8X9dHE4TOvLGy406QhAfAOSYwod22OAOf%2BH5y%2Bt9qyvK4BFE4r6W3wE%2Bcc2qv%2F7b4diuJdxzr70SjTjP7AJnRT7ff%2Bgbm0xOtEwcPCNs%2Fu%2F%2Fd%2BhgrILpQUy%2FVt7%2BBPzI8wRDv2XPX0N9p%2B9%2BRaxRnaklYeK7Vp84HrPOkuDjaIzU4c7rmp%2FH%2Bn33Qr4h9y&X-Amz-Signature=eeb38c0dbf69ecfd10b6474a88301c0decd2e8e54be214ea3a94df802857bd2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DXD6AVJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYXP6vC3HZg3eyZWUM1Jhdz8IFrWjpSIuXD8S%2F1lzbSgIhAJbCUuNvzAIgomcwBfjoqWjSbmxCOkcZxzNa8bZgamF0KogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwdThEpVLkqYzUvQs0q3AMtlwGw5EwpDo%2FQEV4k13NMFeqDAKNRXS8%2B6Rv9gLDPe46C53Zh7%2FsUxwM9qpGvX97wkI6vbErTi2hofXOTOPjhr1mVIIJW%2FuHhIdYIXAYKNQYiZYU16wy4cXZOEh3Y3dQ3hCp29yaJBWxA9my75jAfQX3fJy15sHWSPSDWp4mCO2ycwiZKo9XumjJQLfb59EY4drxOrOmrMv0vZZVEdl7rH08IHlsgW53f11OIeOqbsowDkYrDhDsXrGYXdGVIjGFn6K48fE%2Ft%2BgjNgbw9Xx1eIo1EmfZupzBfTDc%2BdsFabHOn9q5YNBxNr98RkQV9d43PDhCquNJXTSAyvh6N%2FpVZn3nap%2Bn1tc2U9bGPGjR7nKwCQXQfZ2xYCI63wPQBFq3%2FI45INAJhgvdoK2%2BWco32NU1HwHXPzuObq5XyAkl8dRSUVoV6RKgNzakk0zQnEZOPK%2Byos31FN1MA9CP5OTK%2B9m%2Fv2%2F3CG%2F0YR6jyUgsC5hNyg%2F2Ak6Hv5yVsek86ZsC5DjAFhyVUyh2nz%2FU7xEPG9x6b6fMmg7e7zxbgJq0mge7IgA7kmQXseWrbcL1rgNfp86xf69ybJrFXEjjC8Ek03HWZQ6k%2BtTTsuQf8pxjkIPTz7KnbfZXs5DJA5DDM5P%2B8BjqkAUsg8e4Pj9UzySFUUme7Heied5bBgoAzW6pp9jcZLcL86NUKqbZim9YL0lHLQfDTcVwegmb995r7%2BlGHxIwi%2BzOaqUBjk4zY8%2BdnfTRbAe3iZdyf1Z9%2BTSKh3JH7S%2BBXcQh3ynqM%2FasDWznU8ErDNQqlVQwvFBExLxCywfvuTLM0TfYFvXx5SePTQJMKJIs68JJ67LHg7tr1T%2FyZBe%2BnK5XE%2FBRL&X-Amz-Signature=1402ac9321ca74cf5051e4368ebbe1891665d6333f7dc2fd6f7a7006a2801fa2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CNRZNEW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDHg9eATutWpk76u0VoZiQwu%2Bz7eDsiidWpU1BLpLHGiAiBxpctI%2BAjRjl1CKF51o9I5q55ImGFHzhVRacBn7RQacSqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqNKX8f76EiGx3OhQKtwDg3P7IDGD%2B9auodiBSlT6vRFnh8zA%2BqQKHcBqMKelvdoufi96y0hvWF1I95A7CjlWofXxKXok8Wp9qW%2F8Bo9l7VdY2pk8T2%2FfVIXW%2F1vn2K9079JKf5Wvsqny62r%2FDy5IQflFFsh4QmRHEo5EhMmWI3p1%2FQe%2BVc3vSTlUotxRqa%2BkYDd%2F5GiRJkCYTx2f8TDhyvfRz5NUjg8o0QbEan6LOyN0LPWTKsT9OaG06OCM0wLB9p6A4VGYZYdYQlnwQGzyAC9cwDz%2FdrqFyoE7RZg3NgYCbziHCcZLwAKrtGUAh3Ga9ekolVT%2FqckQDG7%2Bkg1PZlqhmYSpySZxZrO2K6TMoYSt0cZjWt5%2BX%2FFReXEK8Xam8jgEELu6T%2BMvFVnjJ48mJc419T7qDxOUhartjQr0oAsCCL5xilHzcMNYShY2KaMESgydQu2xyDBJ9HXcqsn9EKCfXIs1IypFJBe5Zdxm1rfPOWYZKmo2ZIdE0R7HHN2ONIzJQJSmbSOiqW%2BYj5F3EZh7nZe%2Fq%2FRlq0CBcSJdvfvxyftBnk%2BBXObCbp89dPkVK1UitdVy7bVpS%2Bfd%2BkFRHpUEf3NSrE%2Ff4K7ZdLW%2FqKsLEpJ1FrwH07pckmNMn51SCNagfVmqpB%2FovR4wpOT%2FvAY6pgFDQjzE%2B9OwQdlG%2F5J8VPJoMaiBN13UoGJC5jiPz8%2FpytI0%2BD1HT62aKPBe7La%2BX%2BUB83hqABhhhJEw9yTaQgqxQnsDnr7bHTDkF1BOrxz5bys8chwsC%2BwRT%2FDGGruNPxuFUt7JYNhgx1KO%2FPxHQ040lhRVTY1rtjRZB4N8MHp7qysGeLK0ivoKpvbXb5Z9HXhnyD9YJLwWXwP5YrjE6huNCfXSa716&X-Amz-Signature=8cd5bd396cebb75bd0d8757cf92830cf01f06375ba09028adf135a019f6ad526&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CNRZNEW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDHg9eATutWpk76u0VoZiQwu%2Bz7eDsiidWpU1BLpLHGiAiBxpctI%2BAjRjl1CKF51o9I5q55ImGFHzhVRacBn7RQacSqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqNKX8f76EiGx3OhQKtwDg3P7IDGD%2B9auodiBSlT6vRFnh8zA%2BqQKHcBqMKelvdoufi96y0hvWF1I95A7CjlWofXxKXok8Wp9qW%2F8Bo9l7VdY2pk8T2%2FfVIXW%2F1vn2K9079JKf5Wvsqny62r%2FDy5IQflFFsh4QmRHEo5EhMmWI3p1%2FQe%2BVc3vSTlUotxRqa%2BkYDd%2F5GiRJkCYTx2f8TDhyvfRz5NUjg8o0QbEan6LOyN0LPWTKsT9OaG06OCM0wLB9p6A4VGYZYdYQlnwQGzyAC9cwDz%2FdrqFyoE7RZg3NgYCbziHCcZLwAKrtGUAh3Ga9ekolVT%2FqckQDG7%2Bkg1PZlqhmYSpySZxZrO2K6TMoYSt0cZjWt5%2BX%2FFReXEK8Xam8jgEELu6T%2BMvFVnjJ48mJc419T7qDxOUhartjQr0oAsCCL5xilHzcMNYShY2KaMESgydQu2xyDBJ9HXcqsn9EKCfXIs1IypFJBe5Zdxm1rfPOWYZKmo2ZIdE0R7HHN2ONIzJQJSmbSOiqW%2BYj5F3EZh7nZe%2Fq%2FRlq0CBcSJdvfvxyftBnk%2BBXObCbp89dPkVK1UitdVy7bVpS%2Bfd%2BkFRHpUEf3NSrE%2Ff4K7ZdLW%2FqKsLEpJ1FrwH07pckmNMn51SCNagfVmqpB%2FovR4wpOT%2FvAY6pgFDQjzE%2B9OwQdlG%2F5J8VPJoMaiBN13UoGJC5jiPz8%2FpytI0%2BD1HT62aKPBe7La%2BX%2BUB83hqABhhhJEw9yTaQgqxQnsDnr7bHTDkF1BOrxz5bys8chwsC%2BwRT%2FDGGruNPxuFUt7JYNhgx1KO%2FPxHQ040lhRVTY1rtjRZB4N8MHp7qysGeLK0ivoKpvbXb5Z9HXhnyD9YJLwWXwP5YrjE6huNCfXSa716&X-Amz-Signature=e697c5907b7d82694d9692e54835ca9fde89667829c0b97a6cc62776c3699469&X-Amz-SignedHeaders=host&x-id=GetObject)
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