

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGSZ3ZJV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCID3pL1QYnTIStkifSrZGHdt0ZfKTYQbDdR7SgCFlI6PgAiApZjMKsEgxTF8sIdgQu%2BEd%2Fj2bUVFzvR0xMeBEXdbeeyr%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMhPzj0WRCzwcaXlY9KtwDvhgQJoIF5XiywuJD0Gg5eLxyTlius6izPXvyf8RrOdmUCO%2BKkVoK0QWwSSd06lnoMOUaalAtI7yE4xchT%2BJQ9Zh3OJ6rzCSvlitTtBF4uSvF8Eqi%2BzId777Cp1Jf%2BCAdp3uEMDwsuUoWZt5BvFgzK5oVU%2Fm8aDv4qpdMuwsQ4iEJR8qJtFeevSWiayCZkuPM0Ya7mMAxkWXK9IkaRRvcUBsOsZnqV2mLgsxHpQIQtzaCd1tDxONCkYnLfxBaSWg%2FPfVsPoNtthT6vkmjw%2FxI5n36%2BtSxMZH0YPRwxmSJm7oINz%2ByfvhLHvQPDEIgdRQ9lPUTsPHqZO4uQy0VYV4opEPO8p9y1B03PlClwHmky8bNM989moy07BLmWVnMfPLm1zizWS5IkwTX0MKZxdPOv9ZRlCdcsTLpq2ERNWkK3V2VvGhQrFM8h%2BZEqxiewdJxa7OkNvCbnrcZAq36w6U3yVvWJ3QI3vcLluQHKk0J%2BNIVWPz%2BUty5LQFUIS8WQfhOckcV9XjOXhe%2B15jCNaPkVJBJIIOrNevFnP6M9%2FafLXDTAmIhHDakycr2NuzfJS%2Fkzx6ZVN5nAkKvQlzz2E%2BdxLafhWFNKvPupzQUQm%2FqUhGYOvp5H1%2F17Gu4Thcwg9qEvQY6pgEZXBV0z3DDgKYh8FlMO6MEghGr8IAZhjlZEMc30Hn4RVhzIH7p92lcX7hoz6NW9v8tL48Vr%2F%2B26Gu%2BacbMOkjisJRo1teJTU4niqmgDqwBlgg1RjO%2Fea0To%2FmYaduwfcj6ROdLurzj27EhuJxV5GO%2BESfnCJthx8zkKc3ck1kuGdU45C1ZLfhdck7%2Bwb5xwA4z8FfbvW3daUQdFxz9ofcn7tle%2BDxD&X-Amz-Signature=3f29afef9c60006bc3dbb68af2a646a4679f10b671dc65c28139266b1d7eacc0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XODBZTLS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJIMEYCIQD9YXCDnV2Q13mqPN%2Bcwdfyj%2FvvkeulrY%2BQlNoUdGw5HwIhAI7Ns5QrIxEuOoSFzrB5%2BmtMqce2OMMPlvhp6OY3%2FOPgKv8DCB4QABoMNjM3NDIzMTgzODA1IgwjEjR7Z1KqmEvNnjIq3ANfeinty7HoJhslqa1RUqUYYju5bcRtqI3qMUGQlj4noWb%2FoPj53bgJ9F0nC8eb9Kas1TJ05irLXolNBuTTt8h5LlfmlySqUJ1jIAN3eo5qE5weg5j1FjD1tvuwuHfhO7ofQsLp1jNr9Mn0hi6tW5Eg3VGU1OiQPsvxRy0vFGukO9wiBk6uYmcROJRuLwinRJlgqtmzU%2BeODSIlvKbKXNdmHVVPKK5bKXkfGdqNfBWDS2ysqqHd5GV1A1j015A10KBElJzR%2F7mXzwhkdXuowd8T5VBm0H3KQ0fjr0aIuggndxzpkA7Ud%2F4uYrs93zrFyIlEp%2F9zFLR2SPZSL1ozzCX19hVrgQ0lLTPIfkjHRA%2B82RlTBEYKO5RBbIWnrJQqF1Y6zkd70Yw0s0xsSjWEdE07H03S8ILHCmfhe3vmZPdI2rsJCXpf%2BK336hPogI25W%2B%2FIgvoIbUrJl46dXLCwIbW1zWAWlWGeBU%2FXZcLauL6N3%2FNDn%2BBkx0Wa3C0NE0TuWN5A93o9GYdsUfdOBXvsJKs7U30cRG0FPrqeLI5oLNam%2BSOkI6Kske0wRQzoC%2BI5LF9nPmWeU8ntTEDTa6QKLGI5al3h6PbwCyQLJGFQCUf%2BVOOyN1UXFkge0%2FrquzDA2YS9BjqkATl0MiOTuT04lrQqY%2BXx825uOnnzQ%2F0NDNqp5ipwVUZ1CSk0YOMHk60j8mY6%2BuEgxsVQpiaqM1Hh134bK9j5ynVexaiu79beC5VK7MMLCAD4ts%2B9y9pClyrGnoNOghvCQi4giPGHJKtbJWmDc4ZB9uOXfHMxEfp1DP4Z72j%2BVjjrUVYm9lCuhmGUOBOEIX9Ul355DZ%2F91YvmNJUkQfoPjiGzjR%2Bu&X-Amz-Signature=66d4b16b3c43735cd56d400d91d735bc43b2eaaa87f619c781f4d897f242a1a6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRXVDJ6E%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQDkbgNd%2FGb%2FruBmYDIEDMgoGGC3xMmQit4Y%2BaO5pPi5CgIgbtRPYWeKCfnPe%2Bzc9XBYczYjabCcIzVaiyaFrjW1JgUq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDB29j3VRs7WeGe1F9CrcA4zOdfUWt%2FaND8UxO4%2B2eGQ9hlbM0tIllm5kQ9U%2BczCBn5wRiyhyy3buYT1oCbN8h985KWVZgsfMiVhd6Y8ydfVLkxhS8UBfrsr6HdGptV6x83FO4a%2FIC%2F1JPNtWzR9ubiSPuIiQAJsMotu34ZRDo2A8JVK41AyKTEwG%2FDmiiSiZO1V6SpN2TN2pjpN2OJH0B0x2VypZyWcjmBleOpj4fDvYvF4%2FU2NGwVkcr5krN9VGtWsYDOtbN55tcjl426vrwkozIhConQMRjUGrWqq3O8XasUSOIk0884JRXeTNllHEv8pr%2BTZIUi1gt6IYK4%2BnNLJnlFwN%2Bc14%2FydKWru4NSKV1pjDEjL91%2BvbJtfyUFtXdlMaWs2fD9MLyJSxER%2BvqrDDHbFdcNSFT0ZMNm%2B2ks68brH12hfvin93to52pWdxiWpMTZFyRzpSgkbTh0kIcd3Y2fLKPbVUGQCHo4OxMewTg9VXlRGucx4S%2Fyy3px1NJkJ06Y5qh4g4Qy4b3G9JHcBxhm8PL%2BwSeJ2eVl1f%2FX8NURmTnSf%2BFdKJ35TYC5S1WjbBoHawcv0q%2BKP%2B%2BcJbgPnRFi7ONEo4wXWqjYXQlsqgioGbwdkgsLcPg%2FbznLJURgyZsHf8zoqSfCtTMPfZhL0GOqUB%2BW3oX8LQM%2FUTX4cJ4J97yg5ZH9SWtgBu9naaZz02tPsvVZqpt9ZjSuQnApkyPK3wUrJqtxtHVMfQIXtUnYAcmo%2BVaHnPzDNv806zNvvGTOyRadGQPUhv8YigL6rg%2FIiWSN0mHB4bn1Io3xa4KowWZGOR4i5XpixvnQhjMhYDemMjvBG4FLtmDHruD1vrpUfwN4SvNxuqOTUDRi3vnSPxoXWSIoWK&X-Amz-Signature=8ac5ee3a107c1d29b16fa11176c2e83b8ee0b45572e0969bf5a20f960fb64e16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJHUGGJ4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIFmUssuCfjfMS8E2Ij7i77y9sf3HcDPbKGgN6U5wXbvvAiBkyKcx7VGElnzPACgSdHzByk%2Bsf3BTzs9NLPLwd49sNir%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMz7sf1sdcdFlEWN8SKtwDryauynoLv4wKfcLmUbXktvpOBNzJw51hcLFdhL0EDDF8PR%2Fwv29jCuKIj5rTncAn5yc63NgAPsrtCFP88uDwBnVyA%2FVF1hChmbQqKfPqYJL5hs7D0kk%2Fpc9PI8Flrplg5iUOS1AAOlzcPtru9P2nResmn%2BWEy%2FJm%2BP1vV7vhEGyOZOyz4tdO%2F7XSKEtD9vsXLEouE0BLD7%2Fv6k2bu9RA9dYtMovA0orf%2F4365oE45s5dmLDwFSHdH9TFEpXPSsdlB4Mia9Mh6%2B2xsDOC7Ovx7%2F4qC8CfT9Z1Rd8U6B2QSrBrCbt7QERVMpCRv0MKq7rE4%2BLjrbFwPAENO0wZ6zAQ7AhBtcqyuVkZYPfnHmlBAcRy2wWuZAU5uMnsOgfVtkFiAf%2Br%2BJ5V2hcybaVslHBxZTHzGUJoK2Cz106CV1sFhVqJpluViPOZgmvVfSc7aQnNfzk5hbu89LLF2TQAT6kkfCL5XYtKhpUqbTDRbU0rGBHQVfYTlKfyPmk7L%2FaoFy5H1Bx21EMEoA340XAdjkJBp5jOAgFbW2ipOGvCGpHQGw%2F0zpwjwo6w1w37NiYM6Jud29pAqx8XZi7NnIGamFRRRdpQX25sr54A2LxEUEK%2Bsmgz01Glma5btMofnEEw9NmEvQY6pgG91k22dyKvvmHzhwKr6MzymsyluDGZyFX0i4J7dORCflhjsS%2FPfs65MJ24mFg%2FMr5je%2BgrWdiFVCqdb43KmpOu5I950QzHHkTDY6oIMcidRVOZPMhZd%2Becz7bzb2AHG%2FYAniKD3Ol4TOwDXighlNzUpATLnWrm6Yk9I4oNVVW%2Br1DCs%2FeNkE57KjrVFay6T8r4L9TCgPopaOOG4h%2FVDY%2BkD4C2I331&X-Amz-Signature=f585b5d3f9ebda3fe4670660a5adaf1bc6e0cf864acf4e8ba7ef021fd177123c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKD6IOII%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIC3pH%2F0BqGy5qTz28AXKa9FCvtxrxq3XOEdmdC3MpnMfAiEAt6CPSE%2F3uvDwYMh989lK%2B8%2FOl7peRwb66Q%2FAJdx7d%2BUq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDDUPnZLMeGkpXnjbNSrcA5viJ5xfRGlpujJbtqFLWKPqZvSE1RtBXVfTUfJEfp6vkwkU%2BVwZOBUMsYYPjIWuoS3cAuN7blG7Z3KwheMKH9HvX2IPZ1kuBCrySpqFKjiOTa9cbOPmv8L1tFuLTQS%2BrbwTkVPOj%2F4BeqmNcNlzmCBQpiSlkk%2FZVTFqzTPqF%2BM4v92lhVABBQNVSNQYvXgF9DzKktgbWceLTle6kWJb18fbvmMJJDSsJxFlOOPsx9XcPm4LhA5byKf4kxU5vT6nZxVuhbSpNZSypdnAdn3x2R3vZKprHVIreKOsDiVrXlgX%2FFnFxOFK4LSOfxgW0uGyXbP3VoCYmbJujjeusrxRgrIlcbqZrJDvItdbL6MQIFBlX6R0zRDEMmMP3iNBcEABf1xbyfG8L5%2FeXzLwksy4NvwwLSNmKRET%2Bk0k4234%2BTUBSJPkA3vaMHuY2%2BAccjHIXn%2BqeK%2FdPVOuJtTHhJQEEsOHJYXPOCRy2zzFil4EgUC3fSZ7KTx%2B2dhdwa5%2BMaBObJnTZYkw8R%2FZO7PU7VvazDIy%2Fpt9jZCVdCepTSb6BZhxqDPpxAQeN2AGJnbZAPDRfWHTlipvCoAA6rj%2FZsvWYWHuOFJB6%2BsEXNSHSOdETJB2YSjCcDURvWwo0YJbMLXZhL0GOqUBF7YUCBF8tTcA4XlVqfCEV2EYzlGS7K9PLhHi%2BFkzGldXfe03oLsanRcnzY6ewHPI0kM1jd64s885jzPUUPkJMzx203U7xujtRgnGuvHOe8iOGb94EdYZpdCMQfSQY5N1lprMzEcdJa%2FCCPVJ4ybcnwkPShNVvcLoBC6hRV0OtZEGGCn0XDXF%2BfLJFbPKuqN3clMF7Bjp6iO4tEbBHkp5gFn5Oikn&X-Amz-Signature=156080be2dcdb28cd52be21a7b6ecffad46e2dfdf9637c1f1d2e707fd6407bc5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBINOIYS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIBJ0L0Kna9oZeVNm4QyAFAwR3CT0vtBn6kRvKlKkiUZuAiA%2BqB1WrYKEbOBTXK%2BcCfaYE2ibJ1GHdGCNHsKXWGJjLCr%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMLNKVJfwiNXz%2F5iDrKtwDIAv%2FM4%2Bu8nxoMagg3409wxDV98pnRyHsRD8W7v9CEiabL5VzdsT3hLBx6Ni%2BCUzlC8RsBHcG8TOYAlQteLFVYQorUMfhfbkObkB7HFVWFiWjJzU3V8K1bYJRLC5NGbrhAbNts6MVf7qtggdlpdjPhbg7MekF%2Ff5f1OCO1QcnOJYIBMWBWcoKpomr3nSkC4%2Bq06gxN%2BG%2FlkiefUflV3GTu86YV0CYdBgVnsaZjdCE3E0qz1fkAOTxNGiZcrQE%2FJuUdHvoenUBhAoktldopbLEzHToTvgpn8IPzToEgAq4tAJZ8%2BT01kGNjesCheiMSCxyAtaB4LbIqCXaFw07YMoqioVKoqpEXWIPWWYFMudXzc4UNlcpsuXR3%2FhtIzXFyqsvE96TLBQJdF1g81JfuVPS9jGPBJ0zKtoyQWMx64iQcqgIna73D7v93y2Tl06lpfCp7BfQT0ut5skd%2FWb1XbYMhh2EGxGYnqypLTK7nUuIS6ZGap%2Fi7rjYEStFz0QANtTWz8MkTf8klveZq536hFMJuyaPPw3rXE4fyXS5p6Bv1j%2FoeP4m7jSoGL5MKRI0tGxVQ7%2B5E3xQy6rGFu%2FO0lvc7yVVjsqUOs2pOfstAp8qPNqC0USj%2FQ3jEvLGkjIw%2FtmEvQY6pgG1pufJmpbMhZMpcqt6E%2F%2FsYlCbAMwFl%2FDkef79uxYW21II8ZMbTznPdIfYH0Guf7FjBXrE1kZ8D23krAwfbnWGRqm9Th2VDgPvfMj1SnhGX%2BTe0OZW8%2F4yfTryRVoATov03JeV4oDJSPqB4wui%2FnZp0YLiQy6Int1EyT3KStmPI2BPKzssboX8nsl3PuUxdzl0ZnhvkLIeLjwYhnmZDimzyKU5s2Uy&X-Amz-Signature=a770af3848d06dda45d8b2051aaa084f48f54a6a41b5d1ae3b24d433a68b003c&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VL7WT6TP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQDpYnFOlTmWMadVrt3Oy4FE9fNGPQ9lZ3dxtaFZjKaTpAIgASXAD2Ap1FGcwcp488noLcmEEu%2B3Px7r1gn%2F1UOn6PAq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDIvc27A2Rwsqekk25SrcA5F4ksLcO3ySeJBNvvj9ka1%2F4Qv6s4fHj6pYZmimrzT2%2BDW%2FrUdAP5n6eoi66BOdsI0X%2BTIxV3jzVADUB%2FqNVxQePVlfLBQAA%2F4hNJfqk%2BL2NIbKw%2F4iwOD8A0XefI4D%2BX%2FisesSyB066ZIaSdd5YZ6tqRm1goNhP2nFwUJpSOnsI7V0Jvoyk0rZuuFX%2BUJ4vVZgZS7duHwoN%2FFlDxtTZErUj4vkmbj7jMP%2Fv5QK8iaQRZD8hSjdtCdq7k62RP1qJ5fH1gAi2J9dnTpVVRpRWWPFVQnONrQpfXgDm%2FvnRgYc25SGD3kyqgZzEHWUQqE4dMVO%2FJx6WcTp3N%2FXH27ciqljV2h1oT3nV6xrnHsffzy1WfSq7blYR56Af0ZsVaNZBcOo%2BRV5XI1VQBBd1AHzYAe6h6PqSi5S4noGVYCZG3Bkh%2Fl08Mf3TTl9yPlPKMvrHBttXqAFA7WWtYUDGmJO1GEgFrg5pg4ugMa6pyDWESxD5v5w5ni9bd%2BUT6rsqMWn7W%2FYtiEFay0iKJJ8wVfgiy5RwmlAU5N3BtUL%2FKOQV4eolXTe1iYGJMN%2FD9aKNTfHAi79xdyNhbYEQwCkyoZJ9N%2BNdLI42sIPTpeCwHBC%2BQmwPTjlyik2mdIwBjJnMLfZhL0GOqUBP32ZkzdXApgK7nv%2FN9hyM3JBmSynI4FR6U0x7eOqfFIALlNdPgNx%2FqFgHt56nkXNMIN9j0TUiZ7HfkiXPJDDhcatMz6qCsGibED%2FQY5W37gFjPxYFjyWycq6oXS5g5FGmLIvUFJQWZ3juDf5Uldi3v%2FPEwrvbAhEH7ZSbdxqz095hpu367J1%2FsGLyLrYe%2BPFbYSvyzRsCce%2BVIpcY1HzxnFI3sot&X-Amz-Signature=1a4e8e6bc59a870acc5635804500e73e9eeee44327ba4a9f70a88d7d2f7650dd&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZSYTI3C%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIH%2FmgkIsWhcDC5vghFIvia8LkGkhHxTgzkQid0OYgtq9AiBp5NyfTopt%2BA%2BSMRZJK%2Bh1L1Ld1ibya%2BWf3%2BDGjbBUbir%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIM0lAs694egtbEEnlfKtwDICGwODh5Qoie18ZjXbr1I7xwoO3BiWmKtgHvrGK5nEReLFJ1l%2BD7iSf06BieOU14tljuVT84TNK5ItvBvJQ58ewMnHWB8n6T%2FIgU9Uf4GPzpaBxxE9gITXLZT75x9KMfx76OYhtNf2DxnlDR1p9jILy3o3D8KEwfXaA6y5odg2C9dSuDKnSWSwLnyzO5vqV5LR%2FnyvFjC1%2BA3UhVg6vIQpHUOFLrEEb9q2kiAi%2FHT%2B5EhGy1PJ2yL5LdzTtuc56y3yBKLiYfY0cdYppzkAzo0mXiORhGjyMoXJ0y1DIWepcwliM33O%2BoCv%2FFiiQi0B4YUmlHGedcGGm7Bf2AtvHe6nRtzA4xPSKgGlqPrLEuib0zBXqTDECLzXaSCSMj2B6QjZIWkTANaIGYTyTbEwl0e1o4plOQA0WnXDjEzLgcuqB8ovuF%2FSyDU8%2F5EzFq%2B1kKCs3X3UdoMX2EVv%2BKjzlPyfzdrt3Wdypx9Rg%2Bq3zruxvQb1YXteaInRUuAv3Kx5RODicYXQiJTOAguLEngIf%2Fqq1pUp4AIQO0z7eWaUXpIEZL58AP2KEFRcp27Nz1HTz7npZg8EXFfZugw89qucIcsPfUjZ5LLiq4lc2QBMeC40CWkdKrdrsygKW6F4EwvdmEvQY6pgE%2BE5gekEznr3tyutmlo1xWssXm9%2FAz%2FIBQ38SNnoGo%2B%2BgBXeeN2gJj%2FYZvTYHAiZ5gLvB243x%2BmABnNTLFYaJpI9cCnhpr5KJtlqiLzVQ9iX%2FXGr9fRfZkN6d1aKV824CYEcSmVChtBP%2F1nnYGypG9TguZTwIVnMy3A%2ByEptnNlLn1A2hXP1CQFEZWd4NofkVLWCyq5W%2BZkiMgEjjta6JbdFNjA22u&X-Amz-Signature=794b94ee7bf1d6233c59610e512a56ca398696ebd62c610e5ee27cd1b9dac79b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKD6IOII%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIC3pH%2F0BqGy5qTz28AXKa9FCvtxrxq3XOEdmdC3MpnMfAiEAt6CPSE%2F3uvDwYMh989lK%2B8%2FOl7peRwb66Q%2FAJdx7d%2BUq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDDUPnZLMeGkpXnjbNSrcA5viJ5xfRGlpujJbtqFLWKPqZvSE1RtBXVfTUfJEfp6vkwkU%2BVwZOBUMsYYPjIWuoS3cAuN7blG7Z3KwheMKH9HvX2IPZ1kuBCrySpqFKjiOTa9cbOPmv8L1tFuLTQS%2BrbwTkVPOj%2F4BeqmNcNlzmCBQpiSlkk%2FZVTFqzTPqF%2BM4v92lhVABBQNVSNQYvXgF9DzKktgbWceLTle6kWJb18fbvmMJJDSsJxFlOOPsx9XcPm4LhA5byKf4kxU5vT6nZxVuhbSpNZSypdnAdn3x2R3vZKprHVIreKOsDiVrXlgX%2FFnFxOFK4LSOfxgW0uGyXbP3VoCYmbJujjeusrxRgrIlcbqZrJDvItdbL6MQIFBlX6R0zRDEMmMP3iNBcEABf1xbyfG8L5%2FeXzLwksy4NvwwLSNmKRET%2Bk0k4234%2BTUBSJPkA3vaMHuY2%2BAccjHIXn%2BqeK%2FdPVOuJtTHhJQEEsOHJYXPOCRy2zzFil4EgUC3fSZ7KTx%2B2dhdwa5%2BMaBObJnTZYkw8R%2FZO7PU7VvazDIy%2Fpt9jZCVdCepTSb6BZhxqDPpxAQeN2AGJnbZAPDRfWHTlipvCoAA6rj%2FZsvWYWHuOFJB6%2BsEXNSHSOdETJB2YSjCcDURvWwo0YJbMLXZhL0GOqUBF7YUCBF8tTcA4XlVqfCEV2EYzlGS7K9PLhHi%2BFkzGldXfe03oLsanRcnzY6ewHPI0kM1jd64s885jzPUUPkJMzx203U7xujtRgnGuvHOe8iOGb94EdYZpdCMQfSQY5N1lprMzEcdJa%2FCCPVJ4ybcnwkPShNVvcLoBC6hRV0OtZEGGCn0XDXF%2BfLJFbPKuqN3clMF7Bjp6iO4tEbBHkp5gFn5Oikn&X-Amz-Signature=84798da37cfb816ffca7492f6d7f777272af5a8573f63fb965b926d8f9bf9f58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SSYKFLA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJFMEMCH1nXm76wBOxdwKiQAf5ml9DDnJX4fT%2FPfpGBWGEGmdcCIG3RNb5DTUeUbmfcCBZn6%2FzWl5DrR55FvRa3HVtyGaudKv8DCB4QABoMNjM3NDIzMTgzODA1IgyCYWqkbba%2B%2BZaGR5wq3APUc0ENjxewt%2B%2F%2BDC5PFisZRp0hbvbfQLHf3ValcrqAWCqd%2F9rkyEiXwQcc7iv1vaTomDDHX9h4lth4W2RrTc6ezycrJH6XW7sqwevp9mNkKS99LQX0hUnSwsAL9ZDSKkL4DK9aqWy56taVdjJhVPMosfavNktDgpjRnjmxjXUXR97ZECHWKiMJ1anCD4i4Qs7j%2BEWSS3FMPGrx4gRR5t%2FV0LDbsaPCLWFDrHBNp26wmpWjN48mXki34ulgkHsO3AvOeZexWYv41LBqP8wcZmirk7xZgZSN%2Ff%2FPqwTmts%2BS7hSMxm%2FYrg%2FVIfZoPWyKPrRlw0KAyYBEhX6CwgJf1%2BTYP213KZmYsa2NDPft3KaKSGE7fyBk3DB1gwl14140q7h7aoTNk2g%2FYWA001MYfB8ED4F5Gy7QuIUBIy%2BfDNFn0KSI7vkVzc%2B1IEQO4lAW36oPkWge69vKZ89v3TruEsbGC3P%2FBczRuTkIliEOVjNy%2FHK1ltF8tCQAkliwg7Bem4cjfyCoH%2BMPQVbPHrizzdagKMN5DIHDUrxs5mUVpbmZKNA48zmoQC3Qh8FkfMAZSgBuC2ERPKGXv%2BbBqvop7N33NtZwIGZh5P7jr98EpFE8%2F2Z8E9qYDg0rHCGRfjDR2YS9BjqnAanTfILW9e7xsjxGpgs4FR4Yv7jtcnxuFom%2B%2BtS3OzlcP3D%2Bsv2kU26qcKVa5Td64ys3bBfixpZk1OjrTmDElR7bUX4m1MnXkwSgZ6oo4Iy5SPPyHG13aG8rS7aR%2BbpLm7AA3R3ueYoo5iYi4bdc6PMmdKxYdbL9wR8a%2BymgHUfPmUXOCOQoeSycvUCeqJNNtJLxXjKUBM5pAkGaMIaoIU0J7FKyqeeH&X-Amz-Signature=f6e2cd88043d78c5e591a6372215b7a3ae5b760a99065f27c0a6151ff5ae9ac8&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SSYKFLA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJFMEMCH1nXm76wBOxdwKiQAf5ml9DDnJX4fT%2FPfpGBWGEGmdcCIG3RNb5DTUeUbmfcCBZn6%2FzWl5DrR55FvRa3HVtyGaudKv8DCB4QABoMNjM3NDIzMTgzODA1IgyCYWqkbba%2B%2BZaGR5wq3APUc0ENjxewt%2B%2F%2BDC5PFisZRp0hbvbfQLHf3ValcrqAWCqd%2F9rkyEiXwQcc7iv1vaTomDDHX9h4lth4W2RrTc6ezycrJH6XW7sqwevp9mNkKS99LQX0hUnSwsAL9ZDSKkL4DK9aqWy56taVdjJhVPMosfavNktDgpjRnjmxjXUXR97ZECHWKiMJ1anCD4i4Qs7j%2BEWSS3FMPGrx4gRR5t%2FV0LDbsaPCLWFDrHBNp26wmpWjN48mXki34ulgkHsO3AvOeZexWYv41LBqP8wcZmirk7xZgZSN%2Ff%2FPqwTmts%2BS7hSMxm%2FYrg%2FVIfZoPWyKPrRlw0KAyYBEhX6CwgJf1%2BTYP213KZmYsa2NDPft3KaKSGE7fyBk3DB1gwl14140q7h7aoTNk2g%2FYWA001MYfB8ED4F5Gy7QuIUBIy%2BfDNFn0KSI7vkVzc%2B1IEQO4lAW36oPkWge69vKZ89v3TruEsbGC3P%2FBczRuTkIliEOVjNy%2FHK1ltF8tCQAkliwg7Bem4cjfyCoH%2BMPQVbPHrizzdagKMN5DIHDUrxs5mUVpbmZKNA48zmoQC3Qh8FkfMAZSgBuC2ERPKGXv%2BbBqvop7N33NtZwIGZh5P7jr98EpFE8%2F2Z8E9qYDg0rHCGRfjDR2YS9BjqnAanTfILW9e7xsjxGpgs4FR4Yv7jtcnxuFom%2B%2BtS3OzlcP3D%2Bsv2kU26qcKVa5Td64ys3bBfixpZk1OjrTmDElR7bUX4m1MnXkwSgZ6oo4Iy5SPPyHG13aG8rS7aR%2BbpLm7AA3R3ueYoo5iYi4bdc6PMmdKxYdbL9wR8a%2BymgHUfPmUXOCOQoeSycvUCeqJNNtJLxXjKUBM5pAkGaMIaoIU0J7FKyqeeH&X-Amz-Signature=65ebe203c05d6d5f4ade91c6f4c0366d4b76b704bcc789fd9f50f4fbbd3a9e43&X-Amz-SignedHeaders=host&x-id=GetObject)
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