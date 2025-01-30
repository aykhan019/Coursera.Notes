

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVAHH7YW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQyGcuPVS9QcrJO8QNOZ2a8vDeKP34Ts2KAIDMTqgLNAiA4VOXMx7DnqP7tIonxWUpQSNi85N%2B%2BbwT9yGuOoqMo7CqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRvYLtXFzcxP4nkIiKtwD36zJNGCEwNFCw4NgBeBgnL45rpY%2BCD74AlwXE3Wy4bSAzRJ7BVjsajbBfqqv%2FlP%2FORS8%2FP%2BDHtSong62OnBqiltKisdvQ8nXmzIQ%2F58ILAXeNlVl4tUOQgcgmunv%2FyPqBTF1XCLxjFU8ovoZnvGWDky1HrXq6TCrL4vYg%2FqBjoZ%2Fomv6WPTQBTloLc4r9J96idioYR03h8PHXWJrzi3sBhQOCnKh2LHz%2BGuQbLHMg6BKBixU1zVME2jc4zOVECofY6rn3Ix9%2Frv03rzgvtMOUnsBdAKU7SV%2FN51UB5akUfWLNHhZz3y9PB42U9gvGrk8YSZ8XED%2FHnDs1n8%2FzVbP9JcKyR40ukC8srdeURKuX8t4cGfjG%2BoEIbtmKvOBdjL2rMVG5cm9YIgrMGrQQDNUL0ewnV%2B4hfynjk%2FCBjBouIueoqgN0DxzoUMxsmVB0AXN4khI2xfOYS%2FcXaqDvjxDqocY68uFgD8%2FYyYF%2Fzm8opQP5RgfbKi1jLmb%2BFg2UDEqZykA9d13l0eWOYrgD8HvM219udKO%2BBVF8TbhJOYOZWkz2numr0FYhw2Q93HHzxa1iLvXWX48hQ5BhpvIlfBdsQZLORE55aS7GjydKdIYKZivcl%2B9c9PHywEEIq8w06LsvAY6pgGGG9PWihh8HDteTIDKlb6rIMgjKg1u2lZ3Gr88pJxm%2F3dEbGnano668VWm52Df75XJHf0DFdRTkiMeXntmuroEGzvRjesQWKBQk986UKDdK01EZ3qb8V8djeM37eWsu78VHEV%2BdUBdTGRt6TNC0Km2m9rz0xlTNkqc6AdR2mZenBvLPHgmHll228viMPHtmRbUINdv2Iu1owaNholTj%2FRQ5h3mFJo1&X-Amz-Signature=5a9cfe5337b3f97ead6fe5a9688a784504ead22027580fd5db8e586237cfbc10&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IMOWLMF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHTQxXuvDkEUW6sd8JexJBCzwL6KKbFWIDdrnZTHGSvIAiEA1YrmFT4nKUWUra1A2EIhMaB%2B9BFYSDBMWAD6Q4ZVbn4qiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNpGieVBAzMSyIs0eyrcA%2BZk8KrT21TDRfsMXZ7CRLjIIAva5ZG%2Fqt1ncB1kbcO1UdsJKWu4UyjcC7b2HCTPQ3imxV7ff5FwY%2FzKfFK%2FmWP33eFlokwciczDvU1fa%2FO9f0CoEgYfE5s7qY1IVVwa85XD18G21FmROiH%2BNpvLV2EEPvjux4U3bPr8jN9t%2FnEByRskg5QzmjyoqBztFf9UfzddYDJtecMyu8n%2F5KiT9Y%2F5KBbXKxaChGXpbg9IcsTEBAqZksEN%2FFUqBKgst3agniaMqPpYQvEVeetTlHt%2FQ8nSy2HA8WrHRQKSM8PT11m4jWJUsgdcekpYseJF%2BjG13Y%2BbaKdHQx8WvCl4ZMR9%2FnMWwBxABSgqf%2BovFvmBTtyp5wDyktXwGfPqp9NXm28vQpU8Q4XifvOpCNbtbxQKoT4WDJuLM0g4nNO%2Fmw6MuCIWn68KrY1Q6i39A2wzNzg%2FBF%2BQes%2BclaiWCIgWcurdazKVsxxome6r2rxLUOfc6VHRK8dmhdkJ1t2xtzeyOCDZSP5xhNrJBfBTzL%2FQ3ybh0ity7MqMzNtgf8B3RT1%2BuvFyLJjiKhfChmoZ5%2FDfoD8ifVCqVcrSZN6dmAdjAeVUSP3zzchf3KBhIW9vjiVnzw933%2F6gSQtBuEP2l5JBMIjr7LwGOqUBAgMlSRGQGqt2dwHUqOhmwgo%2FiTqBhLdBDAiy1gxrgcOWYIXEr%2BO5iu04LShNQyI3gmgmMR8bGUAEOVmcyD3SzYqzaiQ6SHjtpj9dBStu0eEFevKz7VI%2BEhRljmihJOjLduQrpV2dq%2FmRHQLEIl2ifOiEPT6dA2jzZXAj3eMt%2BtBOKTOeA2p7MXC%2BFSVrb0g%2Bn8zmD2qbu%2B7xfU%2B6uRk3ElfinD5S&X-Amz-Signature=953ee25ed8571351c4f67351c1743802a23ad08810b7a7c5225654d166e8fa04&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWHTU45L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3DnfYKDC0WSu6jL1TeYCJUWLN4LPZy2IIdt0SFp9txgIgXtRXJoHRvDJyoXqr6%2BBxUNnvswrLyQfJCbLSBVNpmJEqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIQ2bz1aznLDiSNutyrcA%2BDGhvJQygG1TR7W4Yecuf9dsi4Zz4S2HikpGhX1Ye4wxf2XAYe%2BKvOp4fYRSX31HxVaVlCwapjnSn79nGXDuiFwJL0AQjHN00LNdwcvuIyjwjvHmMxCvQ9H2JV8WZFU5fpQUUecpTcJSSNPn1LIi5rpzJLj9MpuiuEj5%2Ba8fOta2jzTid0cDEXRY%2Bu2m1ax7klaMcOb7dnRPAnYut3J%2FkjtlQyST3CGytv47qcFfcZ9gj3wZKxE4YSTGwdJBzCpvEflVCKnDluwdBu8CZbzWjJRVam07DeWZeVRfb%2F7odnOt30SKJEX1VVoxx55Pdc3yttPGaz0HASx76M%2FegPLfSfokibudP%2Fr2l1MJAKHiMXxqOZIiZBme%2F9wjHyXzyBM1xotXhhu6xOV3x0JshisoAY%2BZ2moKWRFEbRe66E6YfWPE2A8Xq3q7Sgrb%2Ba9dPpmTN2fs2b4RL2yETyUtCpqOlBCqj5QKBUl1ErUqQ7yVNx7huZTWhqtSTOeLGn35AzMjd2Pr0Y4Pmzibr5ZLfnH6u%2BZ7jka470r2LT2hchZqf0IarfTJmWYW4oSZ3tOKZd0ky4zgVhf3ob8D7T7XYMt%2F3qg6pt2iNyhc4yqE2hfULgdSMzW2OyeuF21QOIlMI2j7LwGOqUBeezXti9sAl4FW4OkYGnd7fJnTCmIsrX6EuvevvMNTEID8BuEjK%2F93EoXoQsPz5mLVsC49PFVyudeoDbORxZlrMtRvGRYuo6U%2BsNraH3fmphEdtdYS8rSMST8JTMNcSS1xycGVrTyKZHxQB7fhmTAXULalzWsHEiPsa6avMDzkK6v9OmmYbLY0dUvEttOcNSwvDzClRWI%2FOdhoofcXDpVbFFToveW&X-Amz-Signature=8441b6270ae5e5f200451a11027deeecb160149b15288c664b1977079405aa1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJIEQAKO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAZBgyZiR4mnuDcxFfy1fBVCBh%2Fc2xXyWPwJ1FB9k0P3AiEAyLBRB1RsjA1aV5WvLsYGqFBlyuMIamTS6%2FS3GUS3g68qiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFa4V4qNYFZS1MV16ircA5hH%2B%2F7XzrgBIJMz9wS2Ah0wylvcMeyiFVgLNAWZSTHIWAhBMpxQ4hcdrZwcqc4xATs8ozDRS7uV%2BSRNM1e2nnK%2BD8KGmJCly03GSYkSa%2FyFp4bpPHmlo8v%2Fuftu2I4LkEFOyVJ91PkWQulgGhmGf1gZ4AIj%2BA2UN4CCb6ed4d37ejrzsD3kyNN4%2F1lY%2BTNrmCQxrvP2MrPc6SqnAKwBRscLNlp5jXnJy2tXhFVB0EValFwMecihpc4Jso4Xouk28Kzy6nic5d1UoB5C3xSywBRbteDoZB%2FLdMw269mMo64QvEjI8H%2B455lKoCMC2PwGne0lkpYgCV9bU62GdXxoILk1VSXU9dw4uyL6pcJwkM02PnXbhL6YrEfvvh1M3U1S0rkftFMdwC4f7ATK0hFXczyATUahNngNHfHtD%2BXHidwCuZasxCAQ52IoR7o5pOhEqoknLXCKsymDplvdESmJ%2Bcv8JggOJHBWZMjGL9y3KXEYiu7xd27p7GkHscAxFNPW6s0Mau2Dd9pEdBW7HCI8MrkFhWYoWY5QXKkA4ECwlfmwGYfntlstqStoa%2BxSNc1UGpWMYH%2BmCYzNF8qWcFKIXVuZWjDELJojLhy0iR7ost2GXn9cJPbZbuVzxpYSMPGi7LwGOqUBHBwWqeqoTuIJ%2Bf3PaCkV8Up%2BBDlQw%2FOpPqqNp2VRxWznwmgSuTTThRvruLch67FaFradZ6suNnWgAWctA2pg6qW0Vfux8MRMpUmWxr7QWBLKCcgEBn1L2tTj6dndchyxHVCcc8%2BB1aRd8fqCg143DMk7RJZGFybFvss2dlSsFMoARm4HSbDeAymzZo4pRksTZWI9bV2NxRQcFXTFpmymfKFkDAh5&X-Amz-Signature=0532de89522c4797467be48eab4a2e0834f591edae90ee8d66a87b37fbc7799b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRPEA7VC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDX%2FyecZ9QkIkYI7SFMibpp9dwCcP6ki8MlOo07S9AckgIhAPB8vulQPXb4VzqzIYof03mP2EDxoSH5frJ6P6PjS3V2KogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9NjD%2Fn02S9h7GhNEq3AOskcn7qBJ%2FK%2BF0fEbgT8RcEbrt5mhPEm%2FFQBDBi2PBIVqa4ShwhgaOVGjpRUIqxVYG78DrCQlLMXhoX4tKs0GZph5OKf46ZhmPwl3OwHbdUeYrsb%2BD9L8ZaJ3X1bXFLgSuZx6ix7JnZODEtDYQ2LZrA8AAIa0uYOdVIx%2Bhbkgyvs8dzHFFjEXqF497ITumrQrvUArpazAZwImJQIidSyrgeNrk6UfO5yinmRQ8pMb%2FU5pnZAiuVQfOcu1b4t485SWuBJtR9bWmGLws4IwzuMUAG44NjREUoGhGr0E980ONoaU1DQDiqE8IvWOb4U1LTqCCNaWuhty%2FHKzy13P2RH4wKY9v1wfBnZ5EPnEMaVJH6R0KN3e1iWM7dSTS8zH3ZgSLDtfopJ4OVzp8XyDqhnMlXwE%2FvXbgjY%2Fx5lYnHsQYpXg7c89gXwzHvXKLkUldfxsVXCzKzLKS2FYUjIVfyeik%2FeA0lVjM%2BqyAiNu%2FjY%2F%2BiFkodlmTwDvYiPRYqqdGPLalaW1GdiO7xe7MZGgL456fK6UPb8HNqR7083lySHGE1BOT43kHF0dntdL8eToqyN6vtEkCeD3meFsek80vNsotHjS3MNwCzP6gw701xj4i5lW0HaEKNRQBjiRXvzCOo%2By8BjqkAZAAjSxDpfEphtTSKd9F9abeHP87ZlsmAZ8RhCcrZxWcX%2FUXGS1aoeFIb%2FXfDHd7P0yQUpBmeciODVAQB9a6lXtAVPF%2BlSkfvTLCjs89jsSFwGjdRv7olZMxOX4pi%2BTDw6Umw80niAKHLCa66HdcSGxOmnd%2BEZXxu8XruBRDLwljVJqMO2kP%2BdtfcOaVO1nqsPIVLu%2B%2BzlutAGzBIvUVNIRDdu2I&X-Amz-Signature=0eb5129d94245b3669634104bc7a11e569394b365a0ffa2e12e2413b205ad7ac&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBODICIL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3mJEu7%2FWHLVYFHp7rAtpluPK6ANFltvNC%2FVuGM%2FokWgIgHlMYY17UG6ZDITmqZPFS2GlknJFszSb6QmO%2Bt0lkk3gqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHuRm4OPVDxh3feyaCrcA1HO%2FxhEH2C3pyUinp8H%2Fp4J6oiOpx7yu2gW6w%2BEwHCZA9j%2BSh4idwkQH9lddq%2FGjAecXCEBD0bbDgskHO3%2BCApCZ5s3I%2FdtONUTvGFXUyQ79lSQXk2Emf4dppj%2BBlsqFMpJocyKOKQX06X9x%2FZO%2FjSP9E1S%2FHfm9tIHHee61xeDj8QfD75oD1jiK8Rkm0unhYvXSIFOALwCFuiSze5FqhBeQsxdt05HANSr2IJv%2BmcPWJXg06RQyKuZRZxIkbCGPrj5Ymn5JLvntAW3JlMKS5G2pMcOLMY7Kq29Jg4nKpyQP7T0TRsWGoNq8Tk965vyWJ%2B%2BJRrF7gugQM6gexYOujHM0fno%2FT%2F0zrTrb%2BIhvPiTjQ8htVhKOh4T0YIsqwnF3%2FQz7nlrOXm30tEAtdxZr%2F2%2BX3fysYPoyJOnKsXkQD7OyIItbispO0DvzFAGX5QK8BRcTP5P%2BrsJAm3TZ%2Fxu%2BS7BE10WuN00eIXQQY2T9SJ%2FQGP1aAl8SViWYe7plPSbRmvyuwCAcjrc9%2BRI83A9wfyPuumUbDzrKxbgOUPM%2BnvQfz55mMNrbVkHgLt9iWXCUbbEMsg4Ua0wC%2FR7Cg%2BSJVldw6kdc358rPk521F56vF8qI7LkZaF85QrX7hwMKfr7LwGOqUBW6K29V2ZmEhaLTkW%2FUELGLLHRNCiXNEnoPAVmQX9y99d1dRSTG1BX%2Fgl1KbwwnWDw99tnYesOhUKA6u50Klwu3VLrtsrZRYKP9zNi1FfBQ3Bld%2B5U1dQCAEnB1znZwKfoNfGVkxTVQJPUd%2BIfyqhCoR%2BT2DTRfO45G6hM19rRGBwM7%2FcnMAydbxfA8JAqLwYKsnWZh46Xyx%2BWEXZ5wfehsDMwA%2BB&X-Amz-Signature=92a0785793d29d67d024536e9d70d1a623dd0b796065e1ab3288ae5eb9c3142f&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TLOVMSL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDifNI9s9J17AyGp8dQt7v4lb2RsvBu%2BL4JqiFat7l0qgIhAPkrGTOXm%2FF00SKX7I5%2FPRk3ogrhOJ4AmMa0TPm9PIfKKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz6lk1%2BHZPlTbKdiNAq3AN%2Fg6py9i9m45J5RxQqzXXApHnCtgKxLeeI1POSkO2jiAehIO9hSgaihvBNrlMiNoVK%2Fa1tNwbdnaq3MTA7zFvat1RHJ7%2BU3V6FC%2BHXGhniHVKbXrMDFCnY8wyVFHf9Pqmvhwn%2FKKYxqQoIsMCDYphBq33BuGX0fTZ%2BrqcNSx%2BnTCzxgeQnJBd0wBVrQW6B9F5T0WoKIs1QJKY27ixA9TfCCoCzqFies1WeNiQQFHzwpbYOTQJUcX%2B45DvWke2mwRh%2F2A%2FntqRsDulw%2FCVQqCey2V43QtL6A0UMeH4MH02FYHUbpAOhvxqURqQg9dwjcmPz1yKAWF87teBC3dz1HTvXKOnmyXsxIARLBLSQfSyZ8qGjblDyNPC9iUyAun3ClwXHJFuLh2Km3aTxCt4GA0WMH1sfHQHOLZecMXmDtrtlFFwKcAfUTXPWwmd3jqdzu7oF1xRfDkseJAnVA7WdUs0je7vDwuiVSa7GBNX9k90aHeGwNrkpHbWIKFNmTtCuJRj4vq8HnxbriTDxr4%2FZ%2BjEmjt1LllFIk%2Bl8agTIZDTrtC%2FkO%2BjXvGN5tT28914ddRiMZjGIFAvagNoQUQ5QM74dkHWq5Um1ZhrNnbtOQSIC%2FbnV1HShUo5B1e2yJTDxouy8BjqkAaT8tvbnXdh3xfwBG1qUwHilwydXKG3CzFcQre5w1tX%2B8wkFFJkmu%2BtF48Pecs%2FMT9GGv0OFIfqB8NzGUi9VG5VgmQzZg8Pc3Px6xkL9Sz6hFxt2SQNXh5%2BF4yjUMpLng8xldUTT32ONIZp0%2Bm%2BDmAOV5C8R%2BlZMQTzB5%2FwvXFw2A3wnc96I3qN%2F4Cd5S9nywlK8SE2wl3IOwISFo2PlqHkkyFWR&X-Amz-Signature=31b18989e71b3cc1fe6e815951905cf53c94b6c75468d485bafd3f305170ff4b&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3QS6M6Y%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6Ct4CMcvaneZmp8oGYlBQ0THj8tHpm40tMk6EPuyxfQIgWJm41ym9AmwwOnsI44%2FxhcYREGVCG66ZrhHvVB24JpYqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN0astF1SvydGLXBASrcA6C3WgPN9x9bs42Hwj2S7FimKOvX3PYiCJYYNUSEAQDaAyG3UBqPA5QvtbNjqi6am9%2Fct2TWhvXetuxkifN2nO%2Fc8IVRI6W1SQEULdwxqfssYyDwCyFrtjWllKjqRMzNUGljDtsxQfWybRAQeJVOA%2F989pZlLxcq7yKggsPqdTJIXfbe2FizIRHVCig4zzWDxgdsEe6jfXmvxN3FhULclbzb3V8wohHe5HKgg0%2BjOLbz2ozTjqc0JOUPKX%2Fng8ZPqMUEmjaj7AegSrrlFQKdXPnBXAbcs5jwA8%2FKZV0j7%2FXpuUYzWKEKjDPL%2Bl3oADhmnzSDLTLVCv7ZHQzRk8c2FD%2FbS719u6h5SxKZxBM6XEdty0ITZlJzkUni5jYBjj1apEPgoHulJGjILm5a%2FpAJu9G89CRoVgo6UNHf7JGq7MCkXlghfgT5aomS1jD89qOwnRbiWtFOVpJpOj7fqBRZT5kV3bVA8zUkNxrclyeFuugJMzmrX93kJIO7B4uiglqkY55dtFi6XXeqgAsjaizXy7pQQeKHmhJ%2BmclyO7qgyrLyMcCtAqQ9XEeZfoq9VbTa%2BH5LtIYPTy1bC3EqUGjYhJTe6s3joIlRQCXViBMhlle%2FvCGx3xN9CrYCc3AQMJXr7LwGOqUBQIHMSEqkeIwwwl2bN2uNkgLmO39GMFDVSXXEP%2Fg3AGlL7gSu0qaS1mb8R1flJ4Kt2gnVfjGmbDuPrPyTGwPvhyMNsekabS7Fej5HYrC7rXUPNKQ8aE6Jhl3ME0qildNfycR8uAJ%2BeEuCEFSFmoqfzzR24%2FJ578HoC7%2BO3HB6UjN3Nh5EFFERLehUY%2B9T4QXy0I1co5oM84SgGZVTIJW7Dl1NtVPE&X-Amz-Signature=0d0f395bf67bb76299da698531f5feb36374e9a67fcbf29b60d024674c4f4de5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRPEA7VC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDX%2FyecZ9QkIkYI7SFMibpp9dwCcP6ki8MlOo07S9AckgIhAPB8vulQPXb4VzqzIYof03mP2EDxoSH5frJ6P6PjS3V2KogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9NjD%2Fn02S9h7GhNEq3AOskcn7qBJ%2FK%2BF0fEbgT8RcEbrt5mhPEm%2FFQBDBi2PBIVqa4ShwhgaOVGjpRUIqxVYG78DrCQlLMXhoX4tKs0GZph5OKf46ZhmPwl3OwHbdUeYrsb%2BD9L8ZaJ3X1bXFLgSuZx6ix7JnZODEtDYQ2LZrA8AAIa0uYOdVIx%2Bhbkgyvs8dzHFFjEXqF497ITumrQrvUArpazAZwImJQIidSyrgeNrk6UfO5yinmRQ8pMb%2FU5pnZAiuVQfOcu1b4t485SWuBJtR9bWmGLws4IwzuMUAG44NjREUoGhGr0E980ONoaU1DQDiqE8IvWOb4U1LTqCCNaWuhty%2FHKzy13P2RH4wKY9v1wfBnZ5EPnEMaVJH6R0KN3e1iWM7dSTS8zH3ZgSLDtfopJ4OVzp8XyDqhnMlXwE%2FvXbgjY%2Fx5lYnHsQYpXg7c89gXwzHvXKLkUldfxsVXCzKzLKS2FYUjIVfyeik%2FeA0lVjM%2BqyAiNu%2FjY%2F%2BiFkodlmTwDvYiPRYqqdGPLalaW1GdiO7xe7MZGgL456fK6UPb8HNqR7083lySHGE1BOT43kHF0dntdL8eToqyN6vtEkCeD3meFsek80vNsotHjS3MNwCzP6gw701xj4i5lW0HaEKNRQBjiRXvzCOo%2By8BjqkAZAAjSxDpfEphtTSKd9F9abeHP87ZlsmAZ8RhCcrZxWcX%2FUXGS1aoeFIb%2FXfDHd7P0yQUpBmeciODVAQB9a6lXtAVPF%2BlSkfvTLCjs89jsSFwGjdRv7olZMxOX4pi%2BTDw6Umw80niAKHLCa66HdcSGxOmnd%2BEZXxu8XruBRDLwljVJqMO2kP%2BdtfcOaVO1nqsPIVLu%2B%2BzlutAGzBIvUVNIRDdu2I&X-Amz-Signature=ffb73434519605d0f776e7bf2ace1fef731bba24e4d9581f17dcf88932729821&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R54AI66U%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDY9V2Isn0%2B42xeyd1SfDRomUCPSIVsLfi4icSEE96i0QIhAL5YD4SoOMm6t4T0LG3uawYR4GzwB0QGvK9TM7mE6mYKKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzEMdbSN1QUeunYZ0Uq3AOuZZjobtfKkFJr4uIhLBqw7j0gt1eBqC%2FiRs0AXEUai7lMsL4cQnKQVMRQFx2Bqta5ntvrq%2FPJdwLG5DMDxNZTF1OFrvMb85R7LKnB3v3jg38no%2BphL9%2BQEdg5%2FY%2Fo2aU9X9DeMTydorXXdSq3P%2FxYCqiEDhUKJB6LLHR9HA%2BQyCP4IwBfFfR73BYV6NBI1%2F8aJpCE4G%2BacRZ1bnkeEjZGlDywlfIJfURnidbjDeTCEfLxvgf7bAZzxJ65LIYpwd2lKDxSWGCU3FRzMnyjJBJpndyvJa33T6m33lspREsFShusmWgY5Hye0DXfu2ihInM1R4yMCHOE%2FCPVAcMRzjvlSnSLuZrlQJ1DDDOs6HimyEKcsoHvatOWzIICpM1sKcqzowjpOH8OaKgSHQtTNI0Dy1mZcvFgBare%2FFza9zeAa%2BOpwODv%2F8UwNqs8DalRRxCV1nUJHbz7uTHosrl%2FaOCsLTFBzsFsk0yVx6G1wGKEqMd6C0bTwggHZ3pYfBsgtPnbO6yw9jRFSB%2FU%2Fpeyz5P4LWpyCMMdTr939d3iFDEe8LObt8CKR%2Bn4m%2BSQx%2FquHj%2F49DyNAD%2BUtv1gAigCKsHYjTyPfi8JfS8qWdK43mMyE3o7ovwr8dfLFxx7nzD7ouy8BjqkAQY4OVG3VjdwsUM8O3mK2AwNkvC4AoLRo5JS8uXsRP58CL%2FuO9b6uMFVQXXUtnIDb5%2FnPsa%2FUEjY%2B%2Bnqm%2B2uDn%2F%2Bw%2Fh19esHt%2Bd%2BaCy8kh3Hxancxh6E9AcyMWOv7B%2FggHBm5%2B6sY715fTzp7QmbsKs8thuU9MjpeRYTGubLr%2BwwYaeIk0OpCxRsOQyJo6CwVwyauQfzW9NDkJjXocprwY6DmNtU&X-Amz-Signature=d6e4573d0eebe961f95a75bc1daf9cfe14666ba83462cc51f74581a895874d6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R54AI66U%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDY9V2Isn0%2B42xeyd1SfDRomUCPSIVsLfi4icSEE96i0QIhAL5YD4SoOMm6t4T0LG3uawYR4GzwB0QGvK9TM7mE6mYKKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzEMdbSN1QUeunYZ0Uq3AOuZZjobtfKkFJr4uIhLBqw7j0gt1eBqC%2FiRs0AXEUai7lMsL4cQnKQVMRQFx2Bqta5ntvrq%2FPJdwLG5DMDxNZTF1OFrvMb85R7LKnB3v3jg38no%2BphL9%2BQEdg5%2FY%2Fo2aU9X9DeMTydorXXdSq3P%2FxYCqiEDhUKJB6LLHR9HA%2BQyCP4IwBfFfR73BYV6NBI1%2F8aJpCE4G%2BacRZ1bnkeEjZGlDywlfIJfURnidbjDeTCEfLxvgf7bAZzxJ65LIYpwd2lKDxSWGCU3FRzMnyjJBJpndyvJa33T6m33lspREsFShusmWgY5Hye0DXfu2ihInM1R4yMCHOE%2FCPVAcMRzjvlSnSLuZrlQJ1DDDOs6HimyEKcsoHvatOWzIICpM1sKcqzowjpOH8OaKgSHQtTNI0Dy1mZcvFgBare%2FFza9zeAa%2BOpwODv%2F8UwNqs8DalRRxCV1nUJHbz7uTHosrl%2FaOCsLTFBzsFsk0yVx6G1wGKEqMd6C0bTwggHZ3pYfBsgtPnbO6yw9jRFSB%2FU%2Fpeyz5P4LWpyCMMdTr939d3iFDEe8LObt8CKR%2Bn4m%2BSQx%2FquHj%2F49DyNAD%2BUtv1gAigCKsHYjTyPfi8JfS8qWdK43mMyE3o7ovwr8dfLFxx7nzD7ouy8BjqkAQY4OVG3VjdwsUM8O3mK2AwNkvC4AoLRo5JS8uXsRP58CL%2FuO9b6uMFVQXXUtnIDb5%2FnPsa%2FUEjY%2B%2Bnqm%2B2uDn%2F%2Bw%2Fh19esHt%2Bd%2BaCy8kh3Hxancxh6E9AcyMWOv7B%2FggHBm5%2B6sY715fTzp7QmbsKs8thuU9MjpeRYTGubLr%2BwwYaeIk0OpCxRsOQyJo6CwVwyauQfzW9NDkJjXocprwY6DmNtU&X-Amz-Signature=965e9336486f92dd9664f670e08782fd4e8ef125aa836eb975363436b1b39630&X-Amz-SignedHeaders=host&x-id=GetObject)
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