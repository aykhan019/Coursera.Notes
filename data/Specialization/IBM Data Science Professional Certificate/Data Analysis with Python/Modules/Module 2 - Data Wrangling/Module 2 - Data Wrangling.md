

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MQFMG45%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEv2uslDJdoiyLPONTX1FEdlGrFk3mnih3YsBIVWTO9qAiBJiRmBFTz0LyrxbtF5NLb6VQG6rHZXW4eqxr2uXMs%2FZSqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZWjIygVjnM%2FsNtfBKtwDuacHw1ZOBf8hK6py8S8MTDmya3XpZ8Y65yIKMjeir%2F9%2BPUst%2FzU2l5D4CM0fQtQjSHtvMBGSGLA309RD55euahVDU5f%2BbTQFLahQVJ4IQtHMGSWDDL%2BPz79Mk%2Fij%2BqcsKbYx4uOmvRqJTw7uGKnIDNa00JHIdKXuQ%2B%2BZ2xWnyIzE196kTTY4QvxMqgpeSfwP%2B1l5RcJrwSAlon841kGTBO3pB0XC1Vva24Avhrwg5nMzS2uA%2F2eKVusQVQKkHJUfRKJvvH5bCy3oK3XwWacXSHSdYF03orWDWOZoaboIomk99KojJbBq2%2BmyZnFSo4I5LlakIdbOUIURhtNG91FFIYD1ihtlJYgEDRpHW78ChGwQjEdc7dnJ7M7Bdf8R1jCsHv%2FoYaBYe8qVHXXJxc4MZAUFu2XpTM%2Flxibt3MSqplcInxT%2FK3EbCugcpDguv32lZgGp53B5%2BAMaaqfDDfjx0pcjOzaVxy5QbCj6jo7PFzLpMaYu3UsyJJEg%2BB2FYxw5BjwOn4lWW%2FQYhhkmoLf3pVF4KIu6Om3pcHtET7sBiAmbKdhz1%2F9Oif2548099RocO0TixRUXFAR3ShL2sn56XkQEweG%2F3JxgmcgqN9GlEc5pIZVsSAzwRQJZIZ4w9vzvvAY6pgEOXH6iUPalSVZFgMZzVXJXszuPo0GK3uTFy0a2OBk6XU85uy8OoA7kT00wlRMezfxtswGb1GKY6D2mvUgpMcSaKGkTOfdag0%2B%2Bzltky5%2BwY4SWLld7VPEm2R4K577%2BsRGxYwGFuLK3vLmiKmHDnOADZq%2BsKQmicN4Lhghx9f%2Bz0dd5IatrtbDGrz56CjOp85CQizn5yWFawJAL8v6%2FQHmuUJa2vqHY&X-Amz-Signature=44c05f9211685dc137977a6e27b3b64030f0e0836949746e25c5e064e771d534&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T6KVENO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBWdql8MCquR7dYtHImUrwefLIZdQtkVknjbM2KOolgwAiEAzezO2GCUUY46aMwYOZCXovw24PWTRTCwZjyFtytr0ZoqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDq9HwkpcdxiPFqpBCrcA%2BnjqJ6%2F2nS%2BT3297E6md0QHek%2FoahrA3cVlX2JS4m0B5amwN8NeXfAnjJ%2BluSJy9yQv9KtZy9YRXpjv5GykFYPxNMl%2BGnKvys7APuT63Nq4GP5AYEPy%2F6JEqCtwrgCjlX%2BAMjysFxzqu44zzKTcgBgedArNQSuKb08vp7x6eW4tK3oMRRop2eWcQttCHqgToS%2FbxBLPTcEm0Lh4ixPSPoojXC%2FehJbf628IiHXuML21FcRPPL5QXzMK9vlMy7%2B7OZiR%2FLAiqcj0JImAiY2qbAQcZMEANDsAeikCfxXZpSTRGJWnSKk%2F6QioeZqZne91nJjP8HMemFylGTYx3FFEmy9PQA7jHghObrkBqDOTfz%2BMlio0i7ZW7Tp24n2Mf89yq9CpDgtd5oM7ylhfw%2Fodz5quVOaB8mn5%2BmkuaiJEltTfhNy%2BlKnEJE2IYurinHX1AhV2XTGIG0rtkRJT4DvLx5LUU4h3Z149qaz%2BffSZfOpwOAVwrcIHF86ot%2FJ%2Fa3ruwe6%2F0iyROVMddTtqrPMm3pj52qm6gTxoP%2BtmC%2BCaP8dp3PhWOmkZ2dO8yUqKPHTJEjJSPcg7nPVh9lUq1sSriIBZrfhEV3iw%2B0iK1QcPGDjSBb8QlcF%2FwSCfoj7tMKT977wGOqUBRrAy6qwcNDceXGRY9Si33xXJRFsoh9RsjzwKyl2bO6UPumda7vrPyMivcV60L%2FDTPV9MUCXZQhFgNxn6sRHATOat76bP8yhYprqL7fx6bQI5SOKIXSmfmxeqj5KhbjmkIFnBe9b4RZH7NQVKBiJWdi%2F4IbZVXy9KEU5sgKdUYnc0Pndmp7%2BPjIR3ek3bmq54m%2BYKVKpWmknzNjmCfKO06N12aAPJ&X-Amz-Signature=431c9bbd2410e3c7ed826e38cbc24dd5ae15d82b4bbd6312f594a77d367e11f1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Z4WCYYW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAhEqcqhVtZS17ce9q3hCRP9%2BFznDr10I41S%2BoIPdjeDAiEA%2FRo0dV%2FnBZQtJUuEqtXoOCb8idJW0Cy2%2FE6%2B8IZK9dQqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDfxvqBtQaZPdtWm5ircA0%2Fsc1Jn684EH635GRTbtJW%2FVe58lCeEfSOc3vetb3kYqD3GWT3USF23YT9s1W0KH13L3wVNVw59jKShawF2JO20dR6R%2FOgswQnrXSwRlCXT1DCGYkMCmStxywfHLsWyi8aCY9V0KZXoArMhmAgUIFMEQxTkhbDHN%2FSGZwQurMdoGuHPsE3S%2Blo5TAr37BRF0FhlUt2kqrG52H%2FAnaA3NyxEFiT3gTsgZkSp%2BxjQi7OQk77JYVL38uM29qAwAZlUnAO0WHOnFmqox0ZB1HlisdIggEPSdFfhIxfAd3WtV36boLCEexDXOc9eQbli0nxQ%2F0ZVLMRUBK6e7Gc0CXmCmYrtGPqtQmHwcAvfudtQ%2BB%2FwSHqLir6Jnab5enMEd%2B18f%2FRMPtVSUC9WeKtMCLmPmgF5I8Ecka2rRo2ukyFC%2FFzEKageKpaD8XbGbkbLCmSs1glhq7eQjoCzkT0kQAHyk2n7JeAXfLgFfVl6vxwHSfXDSt%2FSQqwxaBUimURYmPEiYg3aCi9gVN8oFMBqAXx0WIMxL9siCU4Kob1ukcKXy4vhUAkfc%2BpJuR1I2U6rikZIFJGfaMXIyHFBCsRhInsE%2FoxSXTgn84RRP2Rqe7ytPFjq9I0n6oCiI2OEOOZuMJr977wGOqUBq6LKR8rL0sZLW1Ad%2FPDixAL%2F0j2MXvOuzFlHp3jaSYqFVcg8P5eAGL4pq1pLjAwpfHll2vuqeeUuy3LJO4Lf6k7%2BT8caKr3fmzYb2MVgTHru5geiU%2BqWNbogqETy5CwXUOgRePLYbzofk9RuRd2twMTO1ZuIhSECqT8BsmgNUP9hN5pw6k390r4Mo4J9pI6tQf7h5%2FnZ9AQ4pSebmICqDt6xBasm&X-Amz-Signature=8cea0455c7bd883dd51954dae15986169be1c413bc5d1ddfd25181c81be325d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ROF7DMJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1M5yHDe2hsM1336EftyDeYxtFhGWqfTldJa%2BX7u5OngIhAOXWo1By%2F1ruCEzThEuOlxhw0jj7D0BPz3jHJ55lw5pyKogECLD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs2s6z1gRL4kiLca4q3ANMianQABEKCikgJ6OIlqFQ2D5V4EbHbRaXL9JzoTVkbpItos5O0nWkj2%2F1dItV5xjeqDcEKljZpS136QHZtt5%2BkIAbknhgkJY3dQmr2NUGnKGs8vyxLGPLHqwko%2B%2BdhSu1aBKTR00RSPmcG99Jt1rrwbUPrghRfI74fREslgSDYiA4txJifqtSYdSQBIktY6PXvu%2FZ5UJx8RTHmkoAV9JX7DDD5JYVpnjHPWsPHNSTfP%2B3bGZWygSeFAlEWf0Qo%2BNZnlkI1Ilr2z3867hpfMepv151RLfkdZ%2B2G5x9nv2juN9%2FEPB9hIBuJNoxi5ZiRVyUAYk2hO2UCNgpXraEJSUihB2QY5dQdrW9vG9YY83lonyr73JQ128h%2BG9tQ4fcK2x3uk7dZKlIQnnzK5pqWzwl5BrAd49bWee1MlB8L6ZYsVubYUvfDQ2cn6EACNVUid5WSyK2mJ6jxFXnbNG4mROeZMpU2St1vXfXIMu4U1KEdu2YZ4TLtcmKQzvwcvAkUFwKDFchkYwBor%2Bz61ORAmDbJvFmUoAxVPZ0zbVcJcXNjitgYUClyGJ%2FaOVmwjrtZtZVZGFAoBvdHLiFx5RYLuUlJhl84YYAQKnrb0PW37LINiqBlYyPkPj54QJT0jDT%2FO%2B8BjqkAe%2Bzzr%2BTHShpqTOToCQEB5dUCVVsjWBjMlWJOG7fne3rJegmydF1PNiWwyj3XfIYvOUbg98K4G%2FkyMMG%2BJg8o3FKX0T%2F2H%2BsR17iQXvSmdMiberoIjUn2jrXFgrSo6UV7R8iKVoLEnF04U%2FcvcvCF%2F1VuhO9x7nKDiIw7%2FXlBAVTSay7OFKT3Ab67rns%2FPQHz84yWSBpjAIQak0gNu72JkwYaDNp&X-Amz-Signature=7a6420ffb4453fe2a551a83e25073d42530255ee05ff7fdc0a7f66ff875ad6f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSBHMEVI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdVQK2fum7LYTBkkIV6LOiTh4cv2oZf59zhssf2fm1wQIgP9rLhEBZkUCmAvOLV4hj2s0dFVN%2BUBFS245uVbOmkvIqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGztEZP4SPyUeKwkvircA4gEmSSf3w2bHm59DiqoUo%2B%2FMa%2B8xyhLbGiqMD8qHCwZOcjDdMIls8LIQ8SmQuJnZZlm%2FPp6H77kjrjchNprnjGPCqu4z30PdPXjrYb%2FYXX5OHmKxM%2Bx479%2B74sxIoPhXgE%2F6Tm9miXn8pSflMsXf7NWmo5zcXriT4XyWSHqr5prA4Bnawk1YDctfQSqhneQrYZ8%2Fow2eonXtTQ2y0OZ%2F8Nq%2BqhI4KeXzG2Jn4varyF8qlk97jEP9OvltbafONG0amB%2FNihi20RXVbTqWJcK9e8s%2Bml03u5PVSCWqQJVdm8Z2noEPsA1XQYCFJHbcP2QqWwocFS15vXU0KLdKo1YytHmJDsNrT2peNrIEhGPO%2BLo4hYUac6wMOrkrbMgEZ5lUwm7ks8G10RWdgHTuKQXd0IxdZlFSTWwC8pIjvAHB2f2LAXIe8G43eE7e0JzHMd4RM%2F%2FpWE%2FwaJpGpRxsFXgY7ITeOoHpGo6VeoFGh0QGoJNOjB9lA%2BtAOHxLCqJ5uejyjSWC2wt%2FQ5LRAMEN9Z60zs71QTG3d%2BUKyN9qmdRRF6GAldQ%2F7ZEsPZgHqtCygJEysjv%2B3f%2FgVBLWbkPn1k4yLA7FFKnLyup1mDm9GG%2F62SXZA4iVQg8SqSekVx6MOL877wGOqUBERlwvrA2X%2Bh%2BJbkLrfsooIHcTO0UPx%2BUdU4oaX3ieoXE6OMguaX%2FA0v3P6JP9lCB1OXLN1b1mPKta7dV5Pv0fB34sjb%2FavrM9v2UHMQBFzTkmb%2BbfkKOuQtdRtfN1mRe2r9UAs6Fnpl3MqSpA%2B4TDz%2FKJXvlDgU1q0WaJjmpuvmk6jYlrhNrXs7KWbq0hkVW7CY5BRe%2FtcBEvU4CrUm%2FLQUkvwxo&X-Amz-Signature=8dfc5ee15fc132450450f37a4f8034b7264fba97bce2e19721144c7bc25c0435&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6TGABVD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB7B1YzTfP6hl6maPMsQjqJkDjXynY79hIyCM0gxWSoGAiA1LCd4IdH5kt%2Fy5zb4opnSn1DoScEiY7Dpvhfxmhe1qCqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMut2wVmL%2BMhnbGl5aKtwDOyIVjjyU654Bk0cWzhP6g%2Bb6ncNsRTCl4U9Uu9m0dkIKnf%2Bt82gLPIYek0509rW2LpGTksMTM2ee2pDGscXvvkOrWtUA%2FRF4YIuZcRLiYVMQvnfo%2Fu2uRoNmbTGQaEHJ6MdNWMLrW2rWDsjFqCDz%2BiTOMbuUQwP1OXAyo3tJPf1EczR%2F%2Bpro8VZucwbsndGsuyum3YDn58L7AZUEaD3uUEk5yV29sYhpVBPXfzwm4sakwV7t63z6u%2FaBkY%2Bai4Na3W9ld2epJa9Dy%2Bqw97DKwF77WywqeCPclij%2FovXodlxoNn6odImrym9pDwU6clO4atSC7jDZlSFqEMEs5Et7UOPJrzmq%2Fw6nQJM0b9bu3pvoBH8QD9yRCViUnMWOGjODbCBghUHs6bnaKF4G8m1aE2CyXvD4W4m978CG4S7b%2FJeNQkKW8Deago05nNSZ7KWHFlXdMzdCV1fCzN2woP09C9um1K14GSl0ISx2b8tN0yiSsKZR%2FC3cCfffOA1MTGK5JY0qbMh10OFaMR%2FYn9Oukal8TH%2Bct2eS7ufYDVUPA8Bi0wHcPVLPZGFCtV8XLl6AVX%2F%2Bp9L9HbKA5UFF59YvB%2BPpjieBuIeqxC2tUPZwj1R%2Fnus3Akd5IHKSWrEwyPzvvAY6pgEH4xRuam%2FjRtXUiZEPRQ2J5ls4pRjhXSPi2ceEqBGAsRKlkCy2%2B6lF70fWPdrY7EBbh4u3gCv4%2BvsyAvgsca5TpBc6OpVRzpLKy2mZE%2Fgzfc1nM48uH8v316EPG8SUYLbgQ3u4crmjW6WGogcGiPrhklg1OLQOJ99OVePQ5q3L7fKug%2BjiMLnxBzKFtqpIqGBOnsMY9dqtztVVEDcAa2A0loyOG6g3&X-Amz-Signature=42457df239eabc8f018612c878010de326ee950a9524b546acac786fd62fc4fd&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYDQCY3J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChtSQ4Ku3y2lf5fYFLn1mJJsA00wdgCu66FhPRi809nwIhAJPsZscc3xHdhndJEaSOajhAb9D6b3zeyENJvRPYZOrYKogECLD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2FWql%2FvKeYbvrcFhAq3AOaGOJQbUoSbbQ8M4o5bwDegFyQ7c8U6J8M41RpgL2%2BHybV4NM4H8G%2B%2BrbKUfkh0OozKJBGn4pRGX9BY8SQznGKRnCJ0PWnSn52WPZaKgqOGPoROn6OJPPcFIUOgGpABHhrLt0Z%2BgjvQhRmvwtgibkApq9zEwpTWvTxKAlYVern5JIO4yF38W8OC8ACH%2FxjNYgw%2FIsW2xm6mkAC56SpHX8Wflw8lbUoRII2PGW9LJp5Iht%2FXegEzC8GMYa%2F2AVdsW4GN2wHLwpWN2W8BHCgPXEzeYtA80ueMuLPnNytEN%2FEH1v5eFU92d51XAhrICqf6dlaWiMzLbdz5j%2BNdWkA92OTgbhwrUKnqaj6V%2BTVLq5%2BVqDx41eZLfM5aLNJD4FjlDouRVuI%2BYhVQFEkUc1ZN5oD8inoEAnkUl0omd0HBJnS6yQUwWA4hfRlszsOuHUBUE0nCA3LHi%2BFEtmTBh7Ux5Cn54tdQ0CjzVEV8PfJ%2BdSD3CPkEGonfgyVOYA%2B1dz3jN%2BjrMqVeW1A4k6%2FcefK3za9PdXN%2B6FIXAMHc34ltMU5zW2vRuWWRxDMbdiMzDhf2zkgYcVRXp8ZsOGjBZTNJM2KXBJaFpwM%2BY76xDzkowU0NLc3mpp%2Fin3%2BrfCM4DCw%2Fe%2B8BjqkAaHLRKP%2BwogkDTJgtLg46Sa%2BiYijohFoAJl0OWiIJkfxcTAqurRVvUrDXPl7q3yX0nKzKLD3zhRszwQ5vdDh5%2FmrI6QoWFIeye1Yiq%2B3bDn4D5qoMYjgeuZVbfIuqhUz6IDUrAFWsGi3IOH3qZ6kzFfNN%2BFrsYDGa%2F7Dbn9kmptZJjaY56TG2YDQp6kBgOdHLd7z8Pq6re1vwfNJHtJZ6aKPvpoF&X-Amz-Signature=8041caa7a9321b1b4062bf57e4f514f9235edd9369eff9211891721864af47fb&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7M6ZC2C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCxQbAXLGZom9cPegKoaUSafM969d642y9GFu6P89dcjAIhAKCI991HkiolsRqd7Ml1970EOYTaCBbE1ndP3IeZ7BiDKogECLD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxotKJS1pL6GMeLR5sq3AM2GqdKxjRMcVIirE4wvEmXcyRg21loJ38wKdbbTb6B0nFM9ecUsvuxW1s1yvRpr2fPNI9EDj4ytNJZxeYKmABNseCsqh8lpGuh%2FkSvj0xi3PZD2PQSMlMaqiOmaLfj%2By2Er4Rh9gVyuXrWPm7GXTYfDohynNl7al2%2B6Cfay4mXcvG3l9IMUaIM7CddJYxAE35WDF4r5gijJe9nHPjgC0EapCXO8ZJ4dQHKH6ui30hchFJs3b94I326XwyUGUqLf0gflMR7vBoKzl1bpSJtCwxbm7%2Ft45r2UVtuilz4Nr2B1XD%2F31dnqKLP9NeuC%2F%2FkOX5krzuITyX3YdNTWLRlmsnZLxSl4wmwaL%2BcqxtF4nqXe588iS2QufxTUgLCCLTdQUg5FOE5%2F99rtoPYjWFxugaJgatzK3rRi8ar8apZ%2Fi9S6zkBCld5yRaV4CwsCUwqvhTDcww8yJE%2F%2FvmQ5tsZ6qEbsxVMvGlBCkryRSR%2Fq5Rq0Xezbm1TgjYWGWBS0Xkb%2Bavn8Wl6Zkdz91CaRqGaYlhPzWvR6uQr%2B%2BL%2B5bVLdYabaxXPe%2FqPGDId3v%2F7%2B%2FNmKedsho5reVZyqaOLcwFxezNHxqEYesasCWHheZe1HCKuTPS07qxC3l%2BZYlAhazCi%2Fe%2B8BjqkATMJ5j1Vo1lVcAhj3Kdzf32Ljy7DgZHwMWfyQsAdc0BoMH1G0c1TKAH7SJX1N3tXeNwK%2FzCqapKtc7FllldnfegXI%2FutlIZUgkMfHGbHwg6BSW3b4tdZMHEC60Fhs0hXIDSkLbjt0yjy5bKd9sSzmsNwwEOvVPXvlVWsevy5R0O6ICN7KH%2B0MGzmHNVCkjR5qh2WBbMpPbMnecfHN7asNQGZLNWE&X-Amz-Signature=d0c9e5b3b71d7bb1f86689b03435bf0fe6d2184d81c7860afbf4039a22c02cf1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSBHMEVI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdVQK2fum7LYTBkkIV6LOiTh4cv2oZf59zhssf2fm1wQIgP9rLhEBZkUCmAvOLV4hj2s0dFVN%2BUBFS245uVbOmkvIqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGztEZP4SPyUeKwkvircA4gEmSSf3w2bHm59DiqoUo%2B%2FMa%2B8xyhLbGiqMD8qHCwZOcjDdMIls8LIQ8SmQuJnZZlm%2FPp6H77kjrjchNprnjGPCqu4z30PdPXjrYb%2FYXX5OHmKxM%2Bx479%2B74sxIoPhXgE%2F6Tm9miXn8pSflMsXf7NWmo5zcXriT4XyWSHqr5prA4Bnawk1YDctfQSqhneQrYZ8%2Fow2eonXtTQ2y0OZ%2F8Nq%2BqhI4KeXzG2Jn4varyF8qlk97jEP9OvltbafONG0amB%2FNihi20RXVbTqWJcK9e8s%2Bml03u5PVSCWqQJVdm8Z2noEPsA1XQYCFJHbcP2QqWwocFS15vXU0KLdKo1YytHmJDsNrT2peNrIEhGPO%2BLo4hYUac6wMOrkrbMgEZ5lUwm7ks8G10RWdgHTuKQXd0IxdZlFSTWwC8pIjvAHB2f2LAXIe8G43eE7e0JzHMd4RM%2F%2FpWE%2FwaJpGpRxsFXgY7ITeOoHpGo6VeoFGh0QGoJNOjB9lA%2BtAOHxLCqJ5uejyjSWC2wt%2FQ5LRAMEN9Z60zs71QTG3d%2BUKyN9qmdRRF6GAldQ%2F7ZEsPZgHqtCygJEysjv%2B3f%2FgVBLWbkPn1k4yLA7FFKnLyup1mDm9GG%2F62SXZA4iVQg8SqSekVx6MOL877wGOqUBERlwvrA2X%2Bh%2BJbkLrfsooIHcTO0UPx%2BUdU4oaX3ieoXE6OMguaX%2FA0v3P6JP9lCB1OXLN1b1mPKta7dV5Pv0fB34sjb%2FavrM9v2UHMQBFzTkmb%2BbfkKOuQtdRtfN1mRe2r9UAs6Fnpl3MqSpA%2B4TDz%2FKJXvlDgU1q0WaJjmpuvmk6jYlrhNrXs7KWbq0hkVW7CY5BRe%2FtcBEvU4CrUm%2FLQUkvwxo&X-Amz-Signature=526cf0df87597386a85888e18a41addc89e0ad7cf704f0202043b32705d9d921&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GONZI5J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGMDSp%2FboLzTA7LJ%2BEIN540QDd8%2Bk2dp5y0geWsBocLwIgHTmcu4AngpddR%2FJV34%2BWETbfBs5psP5zVvx4HauZFI0qiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNKY2pVI8UBzLdRgSCrcA5pOOJ%2Fbo8Gi%2B9f5kC1kqWiLKXXE%2BHPjoXrKcdsykKBvRqN3Cub4cTemsGpZt%2FrKXT7nhrEVOTpKh5tI4mdwtCdf1qWY02a%2BBcQYHelXtR9sVUeXtkVl%2FF8nu9FU0TcHRwfrciql06bhsL5HXDgTT2gxVCO1%2F5aZRKgGFE1A%2FSt7cKm8QNoS0PJknfydqpxSuVTAcqJoUX6SNVFPmyCCGsIeamOXhanx44ro1ZGPkGUGKkRqOLEVX1XeF2qX%2Bn%2BYvtAa9QxDYPfiDKmf6KlJeg2GA%2Fbbipbf6N2yzNIPZVEenvE%2B8jQtH6IYlaoEfglvMd8%2BuO3earpWbqc6KQ5DPO3VGSPSCzMNu9g511egLg4bSsDLbtPBKAbMEY%2BtRx5ThfQn78P5ZHJuSr7fGrLHJKTiO5gxVUAEdu6ylbqzlpBdwMUBwULfGyBeiuH0vQfUs7lUlvdGhUzyFLur5qS8ZqG1EfHuM%2Bv0nOxqSuB%2BB5s81JahL9yMzOKFywX4%2BNBmrBHpSNNDyPmG%2Fmg218N04z0pxkxolT29xI7HOG%2FjSxUR%2BCQmqL%2FjzfSd81gxcBWzQA2I63RAV8Y%2FzH%2BZrfsYFizXPxhGVeswn7pdAZQAW%2Fe53q%2FjSIihCd65NlNHMJn977wGOqUBSLgsj%2B5T1%2B38r%2FO7YVoYtAugbCt8u0L2E7ALu%2FJz%2BcuVvfQVJhlkogbKSf0Na3ph3ho1CmIXaHDyZzwnqashjY1swq6cNryPGjHyCwxEH8ZzxJ36vh1OCxrpVphVG5%2FI4XBOSXuES%2B5FbHonm4ziu0C4Od1k8v2vbSARdlu7Dly4aXdH2ydx9RLI1ovItUfDBb8s%2B5hHhjQ2aFqFujLyMVElymtj&X-Amz-Signature=fb09bbf606becccb22338f91d4922d2c64f5f439116d0e22c03268bda6c00a44&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GONZI5J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGMDSp%2FboLzTA7LJ%2BEIN540QDd8%2Bk2dp5y0geWsBocLwIgHTmcu4AngpddR%2FJV34%2BWETbfBs5psP5zVvx4HauZFI0qiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNKY2pVI8UBzLdRgSCrcA5pOOJ%2Fbo8Gi%2B9f5kC1kqWiLKXXE%2BHPjoXrKcdsykKBvRqN3Cub4cTemsGpZt%2FrKXT7nhrEVOTpKh5tI4mdwtCdf1qWY02a%2BBcQYHelXtR9sVUeXtkVl%2FF8nu9FU0TcHRwfrciql06bhsL5HXDgTT2gxVCO1%2F5aZRKgGFE1A%2FSt7cKm8QNoS0PJknfydqpxSuVTAcqJoUX6SNVFPmyCCGsIeamOXhanx44ro1ZGPkGUGKkRqOLEVX1XeF2qX%2Bn%2BYvtAa9QxDYPfiDKmf6KlJeg2GA%2Fbbipbf6N2yzNIPZVEenvE%2B8jQtH6IYlaoEfglvMd8%2BuO3earpWbqc6KQ5DPO3VGSPSCzMNu9g511egLg4bSsDLbtPBKAbMEY%2BtRx5ThfQn78P5ZHJuSr7fGrLHJKTiO5gxVUAEdu6ylbqzlpBdwMUBwULfGyBeiuH0vQfUs7lUlvdGhUzyFLur5qS8ZqG1EfHuM%2Bv0nOxqSuB%2BB5s81JahL9yMzOKFywX4%2BNBmrBHpSNNDyPmG%2Fmg218N04z0pxkxolT29xI7HOG%2FjSxUR%2BCQmqL%2FjzfSd81gxcBWzQA2I63RAV8Y%2FzH%2BZrfsYFizXPxhGVeswn7pdAZQAW%2Fe53q%2FjSIihCd65NlNHMJn977wGOqUBSLgsj%2B5T1%2B38r%2FO7YVoYtAugbCt8u0L2E7ALu%2FJz%2BcuVvfQVJhlkogbKSf0Na3ph3ho1CmIXaHDyZzwnqashjY1swq6cNryPGjHyCwxEH8ZzxJ36vh1OCxrpVphVG5%2FI4XBOSXuES%2B5FbHonm4ziu0C4Od1k8v2vbSARdlu7Dly4aXdH2ydx9RLI1ovItUfDBb8s%2B5hHhjQ2aFqFujLyMVElymtj&X-Amz-Signature=8be91f749a4c3224821d73afbc4396137be67a9cb98cf1b5baa8c24a703d4053&X-Amz-SignedHeaders=host&x-id=GetObject)
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