

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V643ZTDJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDlcBPqodn19dZ9l5M88gbdlEnIBdT0gAugF7SJ2GlmpQIhAK1RHc23%2FmA0rqfpCUSJVkvHs8%2BMW0i1OCU8XqhZUeTAKv8DCC8QABoMNjM3NDIzMTgzODA1IgyI5ZKvdnx0cFQH5QMq3AOIMlrWRv7LF%2FIo%2F5DsY8QxcteWEh9zjqTe1zndS61QklgBtNnao0aFdIr1rn4QiN3wbM2Iewa0X07mxlJU%2BLfk7%2FHA3MJsBHMjMfSIy1GXUV90RVnVWAGUTx28EId8d3huTwKFx7UVw2K4NGiXrpg5PnAVp1iuoYWEXTYojAH750WgE1LulyA53f8JeK8Emo4fOwSuhmeYaU8vD%2BtDdXUcbXdjOylE8h6DwOa0EeXa3yJIQCTIdRUaJPybD8zwLRUUyabfWqtK25GquTeWBdTMyq18RijkUYE4%2FCESvpyVH%2FjZYd1i2RsEDsEIks79u%2Bd2Py9nmt7432MBtTy1YrPVsp7sgVAqM6Fe3WscgYJTkNZSU%2BdshA9s1wv%2FmcVbHnVy%2Fs8LInXf7869qKYg4ZTBfKKVBxclpCN7leUshIQ3Ypj5y0ygRgAys3zc6huXQe5BdpkYsOfw3U1VpxfLDPaHOuAhbolfSzqt5RrhvqHDexCkLT8LMPeK6FwN6HuLVkpHxWjpL3Q69x%2FIQ49kxsvxp8pV31xgmLRqdKRNpd8VaoDOj%2BIzc%2Fa%2FlbluN%2BQ8W2UrISF%2FeKAd9hRDSvipUtP3j%2FBaWqsYna7p7p6%2FEG8C6wTF1kgTFsvmoCqMyTCZvYi9BjqkAVBGG4O9nTGpuO8U2vhWbUI6DU0%2FaAytb401H5TU5A2CIFdrRIHzkNs%2Foxf4nXfK4NH8ummEtRbziiXMgpi0AP7KFkXMPgMvormQM1o32jj4aGOmucvcsJm7sB%2BMOBZV4mJsogH5uap%2BScgnZtcIkKLLjnXFflnGfODtHBPm7zJBBRGSaEIg1j7QpRPXc%2FkFzYoi9N0ttyxf4IvNwqFHPnOaoFa0&X-Amz-Signature=3767c2899107588700857b6321fe60171b07fde673650fbcb4b4a8ee07757b4e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Q7YMHLI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIHX6mT0LaBTlfBlhZAJ9g%2FYvRfRwb3SlfuzVpEgS8PfUAiBtgQsMOlVAAzlEd5xV%2Bhd7ochyxzno4q2wSa%2BbO8mHUCr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMdGHWIpH58Dft7Wb8KtwDckfvEYiTAlXGT7TVNwVEIspDzIaaC6%2BTJRDWBh67PAHly1eiWVbMpA7nUf29dD8CwStOPaGZYJgYE%2F5logLJgf7gmUSlnIQ4uUatzfHLy%2FRZ2stqOGvqFoxY5OX7OcI%2F6FZcQeSkAepT7y2v98xo7TVp%2F%2BiFJzQwHjm8YGsWbgKltSOarzHA6uOJl%2FN6pq5FojQQ0sIW6mwS7O0MqOZ6IeWo6PnASSgOkKY8razqNjgM4VS9hScpOIioUo93w%2Fly9xT%2Beyyw5M7SivsiUY8xu810Nve%2FBDOOQTDw%2BNMCwecWRKx0T7hC0%2FhxwZ8coLt%2FgBTeAVskl9utTZQHBoW5%2FIQC7K4Cn0ezaAsL1PhCCpel5Np6i6MNftf4g1PUCAvXdsRstzCP%2BGj7J8IObkDY6f8hJ8AvI%2F3SdV0DwOrl2lzpInBr2gQ9W6foZvarzX2OSqVXTjIpWnKmlXTI%2B2Nk4QmNNABRDSAOdWLp2GTbTQ21pZnoqm3NAY%2BR1lE0QJqhwIzeXyUb8XfByvHvnRfi4ZVOAIIAgHimBPHNr6Obgt3%2FnhDEHzi3no8vp1nGP1tZsUDdmQ%2BHTZFZQAxqgkznZ6p5BAc7jYdVNsbSWAbK0TAPpnmnBliZOx%2FDy68wtbyIvQY6pgEeVnXqHPcjublWbxnLv1mOELo0iNWMjZHLGYM2BH6F22MyjllZKbZtcp122hL3jXvMMeYK4bM1Pw7a05vaHqP3ANzt0i0rgN7K98of0p%2Bv0padhmEp05HN%2BTFHKGHgIH18g8sBpK%2BuP96mTlpk4TyRjjfTxnlsz8S%2B6sSZ3N7J6pB906Lkch4FYARckOQURe3RA5I8Lch8%2B4ggZMXpF3fi2wijM0K%2B&X-Amz-Signature=544d94b7d8c8d42b70decd2c9f2a4e2dafdbce4a9c3e1c56e7ee3c0d10157117&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663FIV3SW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBbDcTmZ3oaqV96GUAYQpfJSmJ1pJRolwCo1YtCaoPGDAiEArkwI7yqRmAItK%2F8AxpUfFtz6g1zf8sLmH5sa9tvb9Ncq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDFMzAtfzTl1SO5XCjircA6%2BNU1pRiktG0BxmWmcVZ%2FxP4URaUDXKY0KQuWhpEMy%2BSEF74Q8SJ6OrqjuNDAy%2B0YkSdIaxnaFF5v%2Fta6x6ewGlrzJm%2FBw3UnPWJEyM3ARFGLqbVpPIWFZppLw9FAtC0On3PFBjFvrUxiZMNDYeHOxG0Y1kxNYLIFTJao9Qe2zFsfLMm2abZOD%2B0MUDwbw3tqFp69Oql19XxWWESEGITz2WqaYlMITiPHXCm1m9JKa87Q4OPdRvFp71rl8076gDlp29juZMnXCkMdkiJ5sDcmhQf7CMtnMPon30ue%2Fq83HjVhVVZ7EKieB0JrqeWXorY7SWbqyJsLU7fxh%2FbzI%2Be6rT5zvcYTUK2jN2%2FGHjmT9rGg6RFObrMhKIXVdhNDm88BmOGzQAvO0N3AKozT4jy50WLs8L5RgwXyB8qWGpefJ7vg1WQmBRCOfT80qI3Ucgbbra5OUp0Dl40ByUrECtpvloiIclEliPCF6UrEAxhkAJa%2FexXoFZtzo4f8K04k1Du4oYnvffiUXGvh9Y9KDOY%2F8%2BifN9Lkao7Ctrloy4lbC%2FWrxBNYmK7jQ7vpZBTplSSTMIC6IU3vx8T%2FYZRLrRY0UcRLSsdpePdPv6ndqMMr51MqNpWuHvFIkwl5nsMIO9iL0GOqUBy9gCZ%2B3ZTI%2BH3O4IP3Ejywp8u21tJCR9mMrSfTw4oo6CthsmDbugMO5WWNaGBxlubd00905Ms1ddcSIxAykRt%2FMlx2LxBcUHkpRYgxKTcIh%2F%2FQ9Qneo9XxEZzu3YUo1jslOcUHb2Dkhoaa80OZjBonPH%2Ff5pQO40fnSsZZf%2BUv%2FzcvyXhmeDAsETON25vpM39vqGpNSQXJ0Awzu4iHfljqyHODqM&X-Amz-Signature=2027c8eaeb3753db128c2cb0ee3f33c64d3e5614e6c88f36ebe4ac1e65fe1d49&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQWBBO64%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQDNf3bSC7FSWhrxQZVqFaIY8%2BvpIgaFvNQPk0fev8N9OwIgENyIO856x%2FwFEUgESecDfxAvyTzOuQ0Y6ukiRVMVPWkq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDMQ7ym%2FkO%2Fk0e%2BSNwCrcAwI%2FgxuTgwveIpTpHPoHBIWQZwqSY26zvgET1AQGBbZY8oyMLLCYZTpXP7yD30jOXOtB84s2sx4pjVCg%2FG84yHy4OJIw6wBupwf5oFaU%2B2GH3LTEso3JFmOt%2BJQ240py7GZNpFhPLSx7odBbcclivZfxfi8mc122q4O1U0TkzG3afBmV4YgFs%2Ffqqi9wclhzS7Ih%2FUAJngyiemjmocmt4CZpRSGMcOdgIX74l%2F4EWT0ytpQo520eSI0RALig7Gh0HBQJknCOraEsVOxhYaIR%2B0ud2J%2Fui2%2BPXl2OcfNcebNWWySEci0YAwMuoK9kxAaLVAysyF%2B5ByDjQ74Z7i1qE8PjTNLjJ3uIEi8B9pqVvr2kqPYkrPXwPCHFWszX2b5i%2FVMMxavlvQ318GXaFQWIdtcdu006O5uqchQjmhywPOSCQvqCPyQeZeBAe5mSg3fXRc9KF3kpnF5EEoobj6UpCo5LuJ73y4hzx5UgloYjV5JN7YqVcHgmPMQf8Na3XqSNdiT4xxpcIdZl6GIxlo%2FasmH9gCYNyi8B%2F2dvVRf3mBwszfwRwGKSGkQnXT8knNmLKlYvLK3UXsYO40Jdpz6xPuXxhjnQvVM%2FhSju0d3xUrTCEmTNvQoLWgGfXegpMPC8iL0GOqUB8dZ3rvSHD1wSiBiOy5oizO4iCn6el%2BpJ7DAanqlegmf1gr9q6fXLg4gAqG0Tp9Zz16%2BaAMm9mhobIoWb1hja7ss3PWe2VuWe%2FMpYfP%2Blo%2Fk8DWfg1Wmq8qRyyrKZjuEkes3jKhapvkmBTui0MPtQZyfkGN%2F0x5raaKX88KgL7SN3pAM7gDC6GMPDGPNkaxRghBeGfoO9EXOofYepkXk%2Fc2OVziYB&X-Amz-Signature=469b6b254d4da7e36f5ab921b5e9f9288f0c6620dc5e55e13fd7a4a9ec6ccf76&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHHOSBJ7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIHFy3MGDJPoD6z5uNrOHvmAtAAkFZVySw0rmyKleztK9AiArPTDMntbDcqB6507tf%2Bo72hbOuFhMjEysQgxm8OY9Myr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIM6f8k65ueqyouTSP%2FKtwDDqJj38%2FixKEucC7%2B02jUTo4zCT44L6DW%2FyAhgG0SNsVDpQ8qgLAAyn%2FaNuduC5pun5fmAWEMtpGH1y2eZdpSReIx6WUbljGzfDVoYVCOxXAUdWi%2BjlnwXpRZ2Y556cXaDz0gkshoPtNV6kBo18Ukck06rO%2BBcw7ZYafbDz%2B7vehYFNHF9X8hTHmGKV4LOWhqBljpE7aF0OK9zk%2Bm3oDE5UXHzF7fRr8cn3u14qCMcR0V1bBOz50eH6uGkLkeI8bfk2xSlW78JYwJ1U7VPY59B%2F0zcOKmBYpzLCWqjkZiVmtOreWP1iXbMjwDrm6sS8d4Ph9xc38zKa53fgy%2FSe%2FLHi%2FzkCcwJXlKvGoO5biZdOHreztR3Tb%2FNThZcsgHgn6%2FyV27E5X4b8FTnXEeiYUY9Jq6VA59ITRYNnS0f63yYJKwpIwI7tBs3NyqQzT8BOsUccG8FAPDw6hmU9gnoJ%2FAdW3llDu7T0hRf97lOPg2ZKWbhB30NsCFiCcKSEbDkQyMObLxAEy4wU3AsgVrcQXqaPUaHX%2BCiYdtDDTUYnQWFNEZsVKGUtwTMO4ykRm4ZvGmcjocBig6%2FqKNxcTI%2B8qyre%2FMwOOLJkTRB3rFgEvQgWL2mrpvnv%2BMplTV9xcwyryIvQY6pgHH0e%2FS18L6qkWTuqvEQrSFg9NwJ5Ro1wEG8IL0Bui8jNjL9FIx9OwW6y1sk1ePIQ8NgAJjEIhdcqC3o8VpQIQYDx5Rv51BIkNz3xZDJTIbtX1o%2Fy0m201zwkdCAE2Bz5Rq%2FYtwkz8LLed7pSqfL2QVY2T6ptctq3iNqCsaNMKH43Gmi0%2BEr5Soby7PcEhHIP2XlcGa6W8sgS9pkSCgB7ndPRe5AANt&X-Amz-Signature=044a41ce5804db70312a123d3a0c7dba489bf137d3bb8a11199cf572d9f01eb5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEAFRXO6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIHEpv5GUohTrIxYirBBjkDQ4qWpGIzmu2OKTYGZsRRpZAiEAnMCaeKwd%2Fk00jl0%2FUfm6TIT7Tba6%2F78mW7GJ%2FCk8Jmcq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDMnTQoiNblY0HIxAYircA%2FDJhN6TRCHIUy7Xsgli7TMlRSCeIk3NEYC0BqUW%2FpNXNJ8oh0XcYsiw5KzY1e46Lw0wCR5REzHyNZ9covOHpaFVAFK%2Fac3gn%2Frw3ny0PYn7mrgWxpjvfy5rqonxCugJ%2BbdphRUg8LYKK1FWXMAKS5U6reUo0%2FbDK30S2nfVMx6XaUdirlTSV4A9iy4e1o8TFiXaQ9wXmSvwV%2FHpBHU7lNRKYYH%2B%2Bkzwa%2FxTS4usBkKAUphKpZA%2BcCAlo5kwTxMxAwbqD%2F3Q41NpNBAxeKocG7WvUz6HKvgSrvuDDvHpn%2FTcYUm18kWwjZOpg0x2tQXq%2F%2Fuvs8Gm1U%2BtO%2B5Y43dOiw0h0ukMAIi0NpYOGEvvLMnb4%2FJ3YCu%2FS7A3qEBltQad7DAFicKXAHFgA3tPQeBGBrZ9dGDYvkx58Jwp8s7R%2FCHorQ3H0w43rCbLwYTGtTL%2BcLWhum6wMwyRu6p3v%2BMxtJ7g6zojduhVXhdu2Mlt0BeyAb6BfalCiDfkG2%2FAcZ346qTukrTr7SBKPOAj%2F24Nt5BrLt%2FINAEkB7LPJ7tQjZUittIgc%2BbP4rp9w%2FLGKLMZwNRpVvFJhDACFlPoRnN9IagNgwngn2pni6fbrYpCZCILZvUBeMmH4Y%2FSyScZMIq9iL0GOqUBOcHoBNfZdfrR4abI8QDmgrNbFnViVwF2K8o8PPXPUdPrp1USQq%2FnbkeSBs4Af%2BVlhcdDF733ewxRj1kKGqy0w7hbYdYIFZr3uqHbfpul3T7MVfge43WOVVI5PLKEgoDW4Tg0nhPHnYccgVRSth%2Bdl%2F033xQK55sd2GtfEQcUVn9xrQuv4CC%2FWE6lyhbi5%2BLBx4YzkjO1rSBtar8gYwyDgb2SBgTQ&X-Amz-Signature=5469c5206b1b16e9a07e8420f12895300500574391f727881f1835c203065840&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTN4CB6M%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQC9DgQNajkqgYz9Z0YoAkzvJ%2FPLaoQX2%2FVZf%2Biwts5nKgIgC4vT2WzN%2BVdd9bi8UQ5qGsAfoQCH1VBMnMfiw4gnu3gq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDPsLrAAgwTJ2QBHeICrcA99%2FETCxzPMAMp9jeUEyiBmgwRD1FmZPUF%2B5iYQIzNQmSVxjB9NgkldFo7eZwOGVNUz%2BR%2FmqCCMiRlvKCJdNibDJaOlFLUkCA6iUUyLdhWJ5s0rmgRJExquWoMpz%2BDtcAFydwFVa3CJh4dh6Cb40rh8QBJypTFR4nrbW6BiTy%2BuaGavpQy9S8GF%2F71NgolUq5FP2%2FxdwCY8JKlNAssk41WLdjFlqfye54UN%2BreTNR7YNMOHd6BK8OCjmH%2FAERT%2FOdU%2FbIUmHxOX%2BNR0WuB93jbW%2BF4LBS06RrpRa8SlALVwUrf%2FvBdmDzyua7A3SQ3Kxyz8n0fxs8RtoZtLy%2BCQY0vIXbEmdBCTDCTGCMjQUYfyODFMHJAvKYeUpzD9YJAwopdt5nF%2BkqgmOmVKH9p7ulXGtVKfbYLKJJ8Y9A6ClaKzqw7X7LukLxI8B6zVsoZ9eFA2izos1IJ9F7RQ5SQf2VwVbGCCtKooP3ht9Nm7RXC3HKnPtsSNGMiOAcslTLXRauY3QLLkag3tOW9FOT%2BZCHSlEfWX92Q5jUREotAfF4kefruWniEbOv4R8I%2FS7apIaSIQwzwya1%2B1A4FG5lT9GPXLi0VmF01XdS5DoRnJCG0t8SlLTACgiTPh7IDtgMNu8iL0GOqUBOgkkiem2C6kK0pMQLL5dC0hvp1fzPUuF5kUmRMlk6BKkGF%2Fh8BvaU8tx9TP%2Buih%2BN%2FW%2FoxLJFEnfvWV7hcwTddKxWj1OdV%2BhdpmnkO5VTtvX8eYBD3o5sHvd5LO%2Fa7qvBhb8bAOhn%2BWX7A90MaohFzHDYLiJ3nJAe7WQHDK4lzSY2N53A6IaflqzS72Ocdo6OmDEDc7x689t%2B6i0SAUuDm7kgyNt&X-Amz-Signature=94556b8e8c709f7c79f0530cfedcbe01e5021dcd41bfb7bc9b97b7b1b53c4af6&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QJ2FCKO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCGW1O46TzEVSv61scKY%2B73zap%2BRargO%2FxH1dbnRnk6AQIhAIpcSs8Dbdhfciih6Yz0d1ZN0xS4pSbTbZ7r%2FM0BYGQ%2FKv8DCC8QABoMNjM3NDIzMTgzODA1Igwduaoku6pdZkR07%2BAq3AOEHLD2G32OvI9WEVWRfwUmqaGpqdbdR%2FbgZYM%2BSZaimpiEh3Rn1hpHPX%2BlCHAK%2B9lOHi8RAwscnlAMTorrX6%2B437zDQSRfWoSDe5RveJ20aYw4gIUqdFJUfaAIvQPtNNTUhpn9KMJ7kO48VnLwkocZQkzSw9CiPHmCVgMgf7Ob8KWIwOBKOlix3UEYlvZyZrgBqlhkWC9%2BgCGHzbI5Pf3Yx30W53z%2FELhkuJcpSk1x6Jtm5uikXoaxmYpvqpwqaPXrwbTYDCwy7pGMR0KJgaLbXOQmrwxo0DU%2B9qTdbg6TgoxAXEgmQH8fSU%2Fyc1SGoRdji5eSCj1VzqQEAlRkS0mfu1gH7cE8RjGktGZxfrrIrHWr8%2BnW5LOnfClsgKyugUDzepz%2BaR7ZRA6N8veEp9RSMQl996uNrFARxf1J8TZyzBGTD7KrvKkexyQYT0iigSzmUDRj4G2Z5mQ5%2BhAWbRZTvPSxro%2FEcIN8LC7CV2JKUjlqI8HWg95pVNXyzItgAzqKL7ufsO6xPwss8LUnbL%2F48YB5KF01h%2BsemJ9MZQ2RJNIJa2U6W9oA3yRH%2Ft4xc9VqOICuAP9QTHQ5wXTah%2BSlvJzuvEqJ2%2FAJXdLATcychNLigRNOJdg3nLJDazCAvYi9BjqkAdN6jAr4oBeLEk95rkV9rOOGpxWXuYyiXwKbp3oPwTNilasugaAktA5QLjfrkGftJL98Jw5AyCuTw5GjzuwSSI1plGmztJknHu3vZuvh6EhFV3RpxZ0lhF%2FhQmM4ND%2FM6Eti4KmCkEhdmmo3FfAenPr9XRbhA1LSPiha%2FGi%2B4mCX3IDLK66HgINEr6Dzp%2BKAal8GhxjKTgCKv6CGrQ%2FvGvs5dTC%2B&X-Amz-Signature=d07b07e3e0f1f5f0676ae3a666bc11699d950e08af243d52e17bdc23847cc4a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHHOSBJ7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIHFy3MGDJPoD6z5uNrOHvmAtAAkFZVySw0rmyKleztK9AiArPTDMntbDcqB6507tf%2Bo72hbOuFhMjEysQgxm8OY9Myr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIM6f8k65ueqyouTSP%2FKtwDDqJj38%2FixKEucC7%2B02jUTo4zCT44L6DW%2FyAhgG0SNsVDpQ8qgLAAyn%2FaNuduC5pun5fmAWEMtpGH1y2eZdpSReIx6WUbljGzfDVoYVCOxXAUdWi%2BjlnwXpRZ2Y556cXaDz0gkshoPtNV6kBo18Ukck06rO%2BBcw7ZYafbDz%2B7vehYFNHF9X8hTHmGKV4LOWhqBljpE7aF0OK9zk%2Bm3oDE5UXHzF7fRr8cn3u14qCMcR0V1bBOz50eH6uGkLkeI8bfk2xSlW78JYwJ1U7VPY59B%2F0zcOKmBYpzLCWqjkZiVmtOreWP1iXbMjwDrm6sS8d4Ph9xc38zKa53fgy%2FSe%2FLHi%2FzkCcwJXlKvGoO5biZdOHreztR3Tb%2FNThZcsgHgn6%2FyV27E5X4b8FTnXEeiYUY9Jq6VA59ITRYNnS0f63yYJKwpIwI7tBs3NyqQzT8BOsUccG8FAPDw6hmU9gnoJ%2FAdW3llDu7T0hRf97lOPg2ZKWbhB30NsCFiCcKSEbDkQyMObLxAEy4wU3AsgVrcQXqaPUaHX%2BCiYdtDDTUYnQWFNEZsVKGUtwTMO4ykRm4ZvGmcjocBig6%2FqKNxcTI%2B8qyre%2FMwOOLJkTRB3rFgEvQgWL2mrpvnv%2BMplTV9xcwyryIvQY6pgHH0e%2FS18L6qkWTuqvEQrSFg9NwJ5Ro1wEG8IL0Bui8jNjL9FIx9OwW6y1sk1ePIQ8NgAJjEIhdcqC3o8VpQIQYDx5Rv51BIkNz3xZDJTIbtX1o%2Fy0m201zwkdCAE2Bz5Rq%2FYtwkz8LLed7pSqfL2QVY2T6ptctq3iNqCsaNMKH43Gmi0%2BEr5Soby7PcEhHIP2XlcGa6W8sgS9pkSCgB7ndPRe5AANt&X-Amz-Signature=f257d3d3eb52dc93fc2501fa8779265dfd060c68992c3b3960cec60dab17545f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKT3B5RB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIBM704z7z%2BAR33otjhwl9ElWXG4QvAe7HJVDaG0XOSA0AiAQI8H%2BUXGTeFVGgGZQ87zaP4iiFZ4pjpA7Lt2sfPnGlyr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMty6ktgUjwWyKej2QKtwD6VznaRK%2BR9BRx2DMN5bffLJIpUI%2BwcriwdHbW1GAF05BJ5hdmFycDV73jANCgEiEK8imB7237J9xEyoK232Ju92Naw01CLnxi8rvYpkXfSRBohOp7ZLwPu8QX6eQhkdfhBfNoPSIggAA3CaydLaKpDycHTyXbWtTnJiwQRofGnKuEhVMqnxbTs8a1OqsYxoRLQ3bJtIG%2FdYy%2FXC9EjmyCU8KFZF3ykrQomsRDDg01aO%2B5xhWg3UDQ0TTmf8lBg95n0jSHDenDaO7vuF5G5ydKIK9tkcu16oAxPgs7Q5JvrK%2FDuP5o5wPzJ%2BxdoSBuWMyUiwO6sukQH6VNk8JLlE153phvlMYvdt%2FMd2ZAda%2BDr5Q8XslgEjV2WYo9v6T9Ot7caToX3oemlbtmPoRdZThqzCEvAywQDuyTi%2BhtgStOwnVqb%2FU6obnhLoOYDg3xcf6zhBL9ImXD%2FxHVp2ZdRRpz52aGTYgN6L2m84uwqZ2P2bcGeLkMweSJecSb%2FhrEgeBUfZVxK%2B05jlFygi5x0AtXIzwg4ll80QI453rOiV6d4tqp32Wj%2Bptb7FPssjiqOE1Z6CUfG6i%2FRq4T8EeoUrArwC3z9sUP3kcpdIPDr0FRb1R%2F07YsJIPCfZNPa4w6byIvQY6pgFE%2F3cIRsJg9froz2FDVzB87uz7Zz83KMk3nBJu2iZmyJ%2Bo5wT5ZTpkRT2QD4%2Fkkr5AG7WTgBrtD4tgQctsrAz5oLCZoSn6%2FqA1AT3REPlzPqVJPG7ehcZ04gZyXixaIQOvr7BtNFk3SlhyQzrBVXZwspJB%2BuxyfPO20bKczV6bi%2BZ%2Fgu7Vb3GwioeP2oSbH%2FBlrdIUzC88n4t3FVIxofgmV7Xdx%2BJ%2B&X-Amz-Signature=40001adc9d7b83e310eaee6cb1be961b43933e69b8fe2bb46f9812d45d1aa9f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKT3B5RB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIBM704z7z%2BAR33otjhwl9ElWXG4QvAe7HJVDaG0XOSA0AiAQI8H%2BUXGTeFVGgGZQ87zaP4iiFZ4pjpA7Lt2sfPnGlyr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMty6ktgUjwWyKej2QKtwD6VznaRK%2BR9BRx2DMN5bffLJIpUI%2BwcriwdHbW1GAF05BJ5hdmFycDV73jANCgEiEK8imB7237J9xEyoK232Ju92Naw01CLnxi8rvYpkXfSRBohOp7ZLwPu8QX6eQhkdfhBfNoPSIggAA3CaydLaKpDycHTyXbWtTnJiwQRofGnKuEhVMqnxbTs8a1OqsYxoRLQ3bJtIG%2FdYy%2FXC9EjmyCU8KFZF3ykrQomsRDDg01aO%2B5xhWg3UDQ0TTmf8lBg95n0jSHDenDaO7vuF5G5ydKIK9tkcu16oAxPgs7Q5JvrK%2FDuP5o5wPzJ%2BxdoSBuWMyUiwO6sukQH6VNk8JLlE153phvlMYvdt%2FMd2ZAda%2BDr5Q8XslgEjV2WYo9v6T9Ot7caToX3oemlbtmPoRdZThqzCEvAywQDuyTi%2BhtgStOwnVqb%2FU6obnhLoOYDg3xcf6zhBL9ImXD%2FxHVp2ZdRRpz52aGTYgN6L2m84uwqZ2P2bcGeLkMweSJecSb%2FhrEgeBUfZVxK%2B05jlFygi5x0AtXIzwg4ll80QI453rOiV6d4tqp32Wj%2Bptb7FPssjiqOE1Z6CUfG6i%2FRq4T8EeoUrArwC3z9sUP3kcpdIPDr0FRb1R%2F07YsJIPCfZNPa4w6byIvQY6pgFE%2F3cIRsJg9froz2FDVzB87uz7Zz83KMk3nBJu2iZmyJ%2Bo5wT5ZTpkRT2QD4%2Fkkr5AG7WTgBrtD4tgQctsrAz5oLCZoSn6%2FqA1AT3REPlzPqVJPG7ehcZ04gZyXixaIQOvr7BtNFk3SlhyQzrBVXZwspJB%2BuxyfPO20bKczV6bi%2BZ%2Fgu7Vb3GwioeP2oSbH%2FBlrdIUzC88n4t3FVIxofgmV7Xdx%2BJ%2B&X-Amz-Signature=a1622eb2b6c447aab36daaec4c9e214ae9248446d53a5d58ccd04d9d9623ed5e&X-Amz-SignedHeaders=host&x-id=GetObject)
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