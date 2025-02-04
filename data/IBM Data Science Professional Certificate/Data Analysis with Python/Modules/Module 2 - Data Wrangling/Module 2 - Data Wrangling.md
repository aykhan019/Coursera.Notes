

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FA7QE5S%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCICdRv0NH%2BeQG9l5whu51PPkdn6D29nloAwAALo%2BpXjrAAiEA42HAKWQ914JC42QqV5OOvU7LJd%2FT2%2FEPNmq4D09xO9Yq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDBUqEAm0cvmbJf2%2FFSrcA6IgxicYR%2BLNPLmg70t5bFg1z1f0gAB6EM1JxWjnAXUIWcpeEg%2BzReYgHKh%2F8eQ7Z4FkY7DJIQ2e0MWrGyHHr1ccDTd3Gq6hA8aVTLNMSqODeoAvOsToKmcTv7%2FSqcZxollgLdRFfoZDmCO5Rh5ZNdnVJd7dO5yFjnYFTS9XH1xVP5GgiNn90s62etSgy%2FmqlqI2L1lecxnWR1GJPv%2F%2Ft0v5MgVNBnxHob2CXi%2Be2AIDECea0rviZqxlX%2BrtedmvcLajygneGMKqTfESWgr2UtiexVjYxC6aHMr2fwvWgC9T%2B4fOaDJ9vdfy8oZYZ6h2LtCYa0u6NgkzyG2hBaOlCt73VsgnZZT1pE0jg1Xd%2BlOcQTciWEqhMfSha7qVh14gJ5rdW4hK3TkU7wPafplIAP45K5Qo%2BVmlTaXjnCS41QfGsmynq4ICoNee5MSADJVDF0zhDovKFkGDvXclFnUNR%2BqeV%2F1WB9%2Fd%2B%2FpQJloO%2BmI4hge%2B2C0CaZUitgkkuOYpZiU3UJbMe3HXIxACleo4zHe3fiCx1GCBQGmdb8rneCv1lOIcMcAgE716X%2FIpnNYJLC9PAt5qT%2B4uUtKkFDrza5fpOVagzw6qLoyZssKjJLcZwbhXtjtLJRCT7xEGMMu8iL0GOqUBZGVy9wYd4TXbryR%2Bl2S4B6JA3k6r5nw2EpUYrLmdjFNMfSmfIg1d5hLrzu1Wpf57woFL7liQY7lt%2Fv0mLAickh7eHKjsBECjZcSdrDzksXmZiqYJO5Mbl8MFycmTNvyjEYkD0X1qtcya3%2FKGlWtk0KORYwbj7AiKIKLjr4%2B23FOGh7%2FzqPVrxHnozzNZlTqurkv7V29sf5B%2FLRoR49NEcqZ63FGH&X-Amz-Signature=3596a55f72da7cf2f73fdfa43cde560dc712b91c5f44646a15746e7d4215055c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFATVDFM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIHP%2FmryDvvQ6%2FGWanaogjuZMxsg0zYZTrgmbv%2BVPSdIdAiBNyXnek%2FldXnZx3d6EGR9dTZCtdIXcaNNUIscDBDngzSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMNnQWkwEaTJm0pNb6KtwDHS8c672m0RT2b4VA9jh7vVOQhqDMEcRi7vcgeZIum6ytX2ZDs8ipjo01ydT5O6eRqFadUUc%2FiYsP%2F04jmaA207CYNdUb%2BRcXoINOjytg0FlmSlGogBu6joPOzl0xDSAo62Rr9gZrgf0F9gdah2ikVbIU8vFF9n3Z0uN4VLmsQwBWR80ciwCb9MeDJG4FOsBRvubdu1uUR%2FKHpt%2BM%2FPRi2%2BDXfsUGDXEx2xiYMpG2of16c9%2FCdxCx89KO8ZsjRU%2FYF7YmAp30GX6WUIWoTq9qvcWINhfAFu3Z3T8hL1T5j5%2FK7g86jLOEvlIH%2FUeZBufF2XIwqwtESqL0UaG5HdxByFW8K3Wphu9NIcHvfs2WAzoXkazQxO%2B%2FbZEJKJA1BNJ029Xu32h%2FeDtLnFa6x2Egl5%2Bt%2B3EDT9g4ErRVM19D%2BKs3KQ8%2BqondxyudgQYNKyiL3gR3b4aueAA5R1GXNMIlvnOWjVb2Zoo67SRP%2FUgBSve8CgINRZpeprtDVvvlp99cnQlymdhRPFjbNwgEstFn4RUe%2FhwUfwByCU8ZU%2BNbDcNOS%2BowuIzWg67WqrFy6eXJz06ZfGzqi550x333auUjlKEV6Btj5CVZM3pp34Scg%2BqC1q7imyIWDopTYtowkb2IvQY6pgHUN2044pXK8frabnu6GUU7rboInesbga62nBD9GtIMfMUslrN6APa3MugEz%2BFrMhD4wDC8I5UvQegv0bh1I256ZMa5PoHqYJAPJLFkSWRbHGx0bqGsPURUcG1WAOArwqxkdsPRaOiixb5279MPjthLAg6%2FNCc5%2BWH0VhIHZfmHGQa1W1d1YbnXW%2F%2BfBGZoFVdr%2FmeQvX7DUtGdWMHB8mTie28SsOXT&X-Amz-Signature=24879b57351e8b47dc379e1a6b402ded2c2b6c4037225c70935a0fca12e569f5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQET7FYX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIBufsVo2EnCgrDPBOMezng7eOhMRd9UpNrl%2BIluqqotEAiB1om0tVCaE48%2F2M8dZHry8XCBzNXLb4x8o1jW4gA%2BfIir%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMnYh9Tk2PtOXaFSTPKtwDcqttWqBceggkJ24fC23Bq7T7il%2B3eAOv9hD9q%2FbCxUaDAeqFMhvSD%2BOa0SmfXQA%2Bge7lk%2FMM5pMYqdtSPawrx69Tifp%2FuklujmZm4JAHqtJzqRsj3zLfLJzDGakpZt9vsjB5ReS1hgwQu3xwDStb2frxrs7hM9lcnH%2F2f9XA4JiqvL4jPPROl%2F1lOXLCD8J%2F%2BJM1k0%2FCQkuTyC1uB7f6VMBtscddJHZbDXRGG3hOaxeH%2BzzLe45ah3ICAHVpquf7FYeq1CBFnHKcc2pchtMS4%2FxPxuqpdxsKNzcBpnFMoFXSWRShEh3BfvIiZHKx90sEdvMHlJOrJE7na%2B8R1zhkWeDvIW4zLVsEPCQpAfNwG%2FfWpNcilEmvkvsbbfSAKBOtqCtzhFhkY0rrVffLgV2ORX9YBT45KOc56piTTtNZN%2Fnjhduqo2ZCGyONQZBgzprqV22VBOqbL9c5dKAt%2BJQ%2FjCZ%2B5N3wjlt%2FqOzCE9k6Y5HRBM%2Fek2o7NrQyTAPAsgxozQJpbsTMCkVS6LatbPN77a3mISaJu9LJnxjT56k17rvEADjsAIDYs9nfuHoJp0PMGFEoFCz%2FJ2SBdhhfv%2F1Pl7jUb6HrEk0GM%2B%2BTIJCSS%2BeimpJPU38GiSX9Fxcw27yIvQY6pgFzUAqSs%2BIMi%2FyWbTrdBprKh6yMdJ2zPhGR6awKajEIIXOF50kM2oWWM05ty8KEcyRb3k4LtLcoeJtqIo8hyCLtxjNgckr%2BQWza2o6GSqE3tz1d%2FiLe3EIFpWr05EFi8r8pAipl9tEuzps8ZPR42QZkI6CrulAocWfahBj8Z74TwwHTPRIZMCDMwZeGGJXmCx6%2FI5XUn%2BNAMCGMObPuAUlStLOsEIqC&X-Amz-Signature=2b51ab1af5c182b5fec22f4fcfaff9ada92bf24f68ea70c4969818179804744a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNYCOQIH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCF7Rhv%2BJiTSj9afdc65jaFxl1gjtnfWhJQx%2BYEzQOU1wIhAKGIExICJRMvepnnD6GXXxl6d92%2B9%2FrDa%2F5xvhCFog11Kv8DCC8QABoMNjM3NDIzMTgzODA1IgwVzpGbAXsE0H7Mng4q3APtTrZg%2B0VkhRsJdzPcOx6Hh5kcmBcH27lrGvdz6PtdL8fH8XHeeV6ndO1F%2F9cKJy%2BwxDwF8s6SlUjTPgmel23KVd7TOy71gQJgnv1V2zyEgY9w%2BmDDbK%2FQ3MQrQvNIE8az5NJIFPPswYDoJoVZNqZTFQx%2F3IDl2Rp2TLc%2BfThUGfUrXP8TytZeaUzY9tOotkcL%2FM5PS6NKE8MjNCqlKpBIbp7yCHk%2BSdJ6fXs69Fev7jip5B2M%2Bb6dT7mTy%2BasAflYEh0NDg3HgCjiU2zuFd3BVjjZlgfzu5D74jAy%2BPccS6oo5%2Bsla8Fm80Wc0ZIglI40r2IcxBucm0RsY5SE5NRtcQ%2FPhvOJO4IOKPSoTJOcxCbXhUaMRX4jAdkiQvuvqKfozfQrS3e2Rp9DSzSAqq5%2BLDCnce8p3p8CW8h0WalsLOHnxBmfyBX%2BLTynxSacsJVPuGp6n8%2BjIHpPIyqxq64TaB5r2cGzbvEhNtUhZ8y9ce8ENSYwVj4K7cW7sVwifJQd2L838%2B6IiP8pWx03pcU10w1Hgodqg%2BOLnfQKRC1HJvkV38olM3yZWxChqs%2FEW5WP4lKLD7wBPk2VlOOKZv46CHtBXWjW64vdMi3qGztzSK5VP8pxYAdOVg1KuDDAvYi9BjqkATvEvaupqNbAkvEZZAOLLzrtWyPmBEGr9OD%2FaFbCSz%2FcOnQlqpqjhpN%2Fm3wgxO2DUjFuYmIGIM%2BdSyZh9HO0HB%2BXcoYymZ5HohmSGO5D5oEkL0TcMq1EfHm0zO7ITQAwnMqZT9PlgqnPfX4qoz27wkZNlrFlzPkIjOiFrsnjHSEOKaVtaBmcmSD7CeS2ca6baDBsfwcpUtpcady1x3N6XBbfnBlt&X-Amz-Signature=76d734f59aa810b9a4e390b79460cfaa4ed46ccdacd0f81bb31224b4188f7b13&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CVAEK6H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIAY%2FL4HXLnrFkvN%2FR4PuaFhl37OnpEWkSgSRLnNmMqjUAiEAs4vC42te7oyFXD7%2F6Zz5qVp6pbRyn6MBFjqf1dCNjvsq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDN%2BHBdZ6RBgudLOLEircA1biN6bkxmt%2BZgDQ1%2FHfskY9BFIfskvlBxdAnJSdBiGEJ6tiwSoIAGA%2B7DNy%2BMLzBxcyDSf85t3WOYMCybfFfXl8t%2BKJGN9wxMPrBXLuGQby1LCuIcAEUIvIhaCRm9hlndSwvl4Srwv%2BYT9lZy0OeNQ8EI%2BzWpAaCnzxqzyYREeHreGG%2FndZjCTP35YqHmEF96nnUDQ%2BMTuFQeUQX69lAYHOO%2FvRsok5ExXYJYnJxdv6FEfKypzItjLTAEWgyxBjSyAuUoZldLLwHZDW9joZsqdq6UJ9HRv8ftnShiVckxOviXflS%2F%2Br9T93k7a%2B2L7cajslIocujGammjp02vbuPna%2BdVq1qkQP2CXQ9h%2F%2Bt5EoJPFMv3eBA7bKieterWV0f%2BMyBpcZj18vSBgEJiPbIPxqJvqRsb2H6mwX1IGgHH%2BT2qbc89fi3MyHh5GRy%2B5LGKWlzx2icz3spfFHzTdOD8qaNMDJjWDlAtgKFvhLM0zRGEUXW3hsG%2BmbI3URX%2Bpxy6exZLowNkElRcQ54DLnxg9WjeT3cHvms%2F34o1%2Fzsnti02kygQ9PnfNRWwu8muQuMFPKTMYECPpM0SNM3mXpGmcQTEMJK6bmLUilObmb%2FxtUB7CxxHyT4aYMFaVWMJi9iL0GOqUBrvjevemcck3Ti8NCjKLHjdWQIMEQZnWR4qdnM1Nj4DMRRlswpUDvZ2czWlzz8A3oWso3Zdaurt2lAmHNvPxI1yMnTUlSUy8WaenIkPlXBCCEZFyCIa%2BPUYjSo0HMiX77GRmkysGnJD9k9E0yTKCHEyLE91WpWZhITD8c7NwRkSR4h3vE%2FLr8Ix8RWinMNeAyinHgbwcIGnmjW3RWwJ85HVxdEEfU&X-Amz-Signature=52728e0d69b102aba2f6313b871a2399a7bb8cd6e8c8ceb926ad5508c003448f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPKCIKHK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQCpciVkbpP%2BNcRlGtSesJEjEEFB29gkPHQyDFwNnHv7swIgRTspCQi7RZZxr3hnPx%2BJi9bGh70p5PDHKUdU5SuuFkUq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDC%2FXkCAsOhCkBQ6B7ircA%2FY5ggNLPDdKIDjUkEgPP9wW6GJBIcLNKVUIFHPVzwfHs2Pe%2FhSmEz6qI1JIXVU%2Bk1tnScaVfVwumDiYfjVIakV%2FoVGvYBl68C1DtLn9EZc2aT1zhYLqGqF2Cwzt0shvCzDvEIIlX5T7mzzI8mi3G92V35bLYuvD3ywjOaCPousPfBB5OK8ir6cnSjKXKy8O2Ql0Ut8ExeXNJoEJAHdhHqVmSQKTWicTVEoSlZYNbFA9lgk3S1rlgmG79HiQXt4yMr4JelU9QalOwGtsNnDnmhhN3PoTau1yOePpOvOYJwb2JSxqzI%2BVe34og2bxahVR3nx0G6ZUbf7tmg0EwHINHEP2nfRAggLv7cT%2FaO9J9KWwDfkosS5qqG1VNPid7DQNyFO05aphNUdknmHZREods%2FqZjjV%2B8rQymhNmPH6Rh0f5qh%2Bl5H5ESxFX0hzq91tTfAh3tgif4JpctsnO9J%2BqGtCTpQAQfhWpDzAnWu9vIEg3XpYzsLwpTV2knkdeF7qj3yjpMTJctPLsy4gfrbLMyV0qrOBuS7EVWp8%2FV9MOaS2Hgrv%2BPuV1X05CekgBIzJPS9KkvXSo0A5GFKy73P2b4YsXmhvNN5DnsVtd8f69kXq7hnULLLrnunHD2l7VMJC9iL0GOqUBRxGc7DBbg6UJlRp0t%2BgtMYx%2BNDeEzZJL%2B6D%2BfbP%2Bvl2tKAjWcL9XickWEKeEkRcVwVei0uKjgTEW0BXh075cjZDdv9ZiFNpjE2kuheLm0TvIsZlag2UOfi1fqrgwIqyL2iiRhourcga1vp4wOjcKfNAwq0AHD%2BZQ%2Bc6pEzLIK4pBa%2B0vIJQZQ3dYWwCPFgSwdvwMhbMfC8ZM1JziHBKKGONI8XwQ&X-Amz-Signature=bff1c0d9e306dee10f318c4802b49611631b8b23e57cb6551489c0ab7190c507&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HXKDSBH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDbs5qS6GeGzHxbhgewjJm1tBDCq%2BvzSxInKZTrwylcmgIhAJ0eDWzxjxhtRMliG%2F30eZFn%2BbNEilPLcuiTGgU%2FHKQyKv8DCC8QABoMNjM3NDIzMTgzODA1IgyeUED9KOC9iJppjAIq3APQrSP2kv3qZjew67c0dnpoe7b6zAZ6gStk5HAOSA4AvXehTELu%2B9yIk1N22zMo2mKluWXCfJegYzRYDJpPSkV%2FPwRW8d79n9%2BM8BrHcXHNJdTCyKHjbasxTZeL3j0f13y%2FCgUFeVgzMcEmZxUMRAreHF1Uls5UFuK47FC%2FRiB1YBzCIcaTWx8lwyFuMawEtE02tLzuR8rVYpTtcglkQpV9zMk4j3FyoED%2B0em4jdjYmtF4H2Mbz3Fq202J7aalVhGmUuQbPiT2Vv6cX0E18p73f%2FiFUlIipNnaDWCs8VAJiHKULMmqsRbeYD5bBdpjyLG2Ntfbf%2B9B9aPflWRXsB8rjCK7KmyqUP1HI3VQOd7uU5eRNVZjzJAb4%2FjcSR4Tlgxfa9gB69vxm5d6KOQEWk%2F7xcVxS0kAXdIK6A9hr6nrdcgNJiDgiG11Ckau3UncvxcC2gC0RkrPCPEu37dqrFtbX2upnrPFScY5Hq%2BvP5cvWm840DHQS2lQLXlu8Xyd4khBvoBtIPtftHOtberQ%2FDjkINkaXb9dlT0JvhWnBoLzVWNTpP2Y70mz3kCw85E6gOEyuo5IEx808%2BnIUsaXHXWP66tG5dVklauml9tFMxDxDSFu2mxyRg1GGwycuDCCvYi9BjqkAUdpzlwOLFcEVjcQPmhO%2BFccPEdP81%2Blzs5q%2B16pa%2FwBi8hiFYlSeatyminP8zLRm4f3ddcdWnENnU%2BnYcaYgegQ%2Bs7jLgXmzO69TONWvZ4Klu81xzlp%2BLA%2F3SygdFx85Su6fih6JGsFXDsquhgYdpmKj6OI00akKNI9DlKZDJfZP0eX1Q30WDBEfF5OvYRjFJuQxsiA6dEWhohJM2upY%2FrhMovr&X-Amz-Signature=26bdf87082567f9b14dd7841bec34c58a9f71b87e9fb3696fe43fe6a190c36b7&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDQITL5R%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBQ5N5q7h8xFVRGH2f4BxZTK6h4JDFTGWDmpii0jn0znAiEAj4JYxzCSXQrF%2BeFs0VwbjELuJOq2TO%2FwV%2FIn6x8%2BSqwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDEzVUd7Iwb3H61G%2BpSrcAy4XI5gbLN510%2F292YJOI4w%2BZp7aqvSOmSl%2FfwoDJiiqQcgJD8WPivChH1W%2FHTQlZVfKBypNkPTSFW%2FiW7mS9D82I1F2FzhTigwoQsrBLItbgad6AeDhW%2BsOJllHNSN2o0RYkLhscAAE90CXVbHAL8BphoplYiMlK%2FOq08B5obBWRHHeIHAZe8%2FoMuqkrGGIF%2BWjA7BwGyIuyNcPPc8bJY%2FWhunCjbTNdQ1gnSzZmcz9YgFAPP7DzePujzFrCfAMR%2B%2FACrccETKhm45GNkYLi3gACB0PNP0yQor%2BWDleksx7xsUFDSjton70V9KqwNw%2B50rjHOwwNu9pPQgz9SIztSt9vkW9P3Fd6mX0i0%2BdyoXCVi3vjauVYebvIky%2BN2SH6pt7Hoa%2BK1NFgDYMvvcbun%2B%2F%2BgKmSwyM9wdBHE9JGM9CqcyQYcRBt6v2IPKFofiD4d9LwB1HE4YpV2K0WEJaQYV4%2BEFLlS4%2F0voKdXM2p2jg3K9eABRcp1CpfVYKaQdQ4ULHgCGzl4hFhVxrepyiKAatHP9ciOpNnTeaLNSTIpP62Diyr1tNCFOR%2BVmKncVgLzku78mLSUClZ7O1k3ShFryWUKoYaDhMm4lUBGC%2B%2BHFPiKkkv93wYztQvQVGMIG9iL0GOqUBaeyplKSF5zbr93Pm2ds1pSZawoBYaPrHEID1EertKGstCoJdcJy2MXPCK1%2BSyEgMcVq8x%2FYvzQKwlyKk4S9f6nzBtTS7yZ%2FhdFltF1MpadMTLCB2VSCrO6FvBZ4%2FZz%2BDbhwwbx2UfysYH4n4%2F3j4BnKPnT5IUCLJFv34cdOe1NJPSm7pupKz3fxTwVAmQ0KEKUVzfKuw9KrFFQZBNufZLMFrmFBq&X-Amz-Signature=dbdd9891b06ea4d5e093eea21de353fb6561b671b620e41fc4a4f144d6878c8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CVAEK6H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIAY%2FL4HXLnrFkvN%2FR4PuaFhl37OnpEWkSgSRLnNmMqjUAiEAs4vC42te7oyFXD7%2F6Zz5qVp6pbRyn6MBFjqf1dCNjvsq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDN%2BHBdZ6RBgudLOLEircA1biN6bkxmt%2BZgDQ1%2FHfskY9BFIfskvlBxdAnJSdBiGEJ6tiwSoIAGA%2B7DNy%2BMLzBxcyDSf85t3WOYMCybfFfXl8t%2BKJGN9wxMPrBXLuGQby1LCuIcAEUIvIhaCRm9hlndSwvl4Srwv%2BYT9lZy0OeNQ8EI%2BzWpAaCnzxqzyYREeHreGG%2FndZjCTP35YqHmEF96nnUDQ%2BMTuFQeUQX69lAYHOO%2FvRsok5ExXYJYnJxdv6FEfKypzItjLTAEWgyxBjSyAuUoZldLLwHZDW9joZsqdq6UJ9HRv8ftnShiVckxOviXflS%2F%2Br9T93k7a%2B2L7cajslIocujGammjp02vbuPna%2BdVq1qkQP2CXQ9h%2F%2Bt5EoJPFMv3eBA7bKieterWV0f%2BMyBpcZj18vSBgEJiPbIPxqJvqRsb2H6mwX1IGgHH%2BT2qbc89fi3MyHh5GRy%2B5LGKWlzx2icz3spfFHzTdOD8qaNMDJjWDlAtgKFvhLM0zRGEUXW3hsG%2BmbI3URX%2Bpxy6exZLowNkElRcQ54DLnxg9WjeT3cHvms%2F34o1%2Fzsnti02kygQ9PnfNRWwu8muQuMFPKTMYECPpM0SNM3mXpGmcQTEMJK6bmLUilObmb%2FxtUB7CxxHyT4aYMFaVWMJi9iL0GOqUBrvjevemcck3Ti8NCjKLHjdWQIMEQZnWR4qdnM1Nj4DMRRlswpUDvZ2czWlzz8A3oWso3Zdaurt2lAmHNvPxI1yMnTUlSUy8WaenIkPlXBCCEZFyCIa%2BPUYjSo0HMiX77GRmkysGnJD9k9E0yTKCHEyLE91WpWZhITD8c7NwRkSR4h3vE%2FLr8Ix8RWinMNeAyinHgbwcIGnmjW3RWwJ85HVxdEEfU&X-Amz-Signature=6d7d16c03b3b953c924557a22335a760232606d8a99e76f387310e034385763c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRHGZGQP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIFVXnqlvdKMC6hKPSMSwzacjQEGKFfQC9fjgmBX8e9AjAiBViSPGJzDGoNNRvbdzG8K9TFpdqjEzKGzcwNe%2BcN3HJSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMTgy0lMbPnNM6RsQhKtwDnm6GORvWNzWpxO96sWDKVp5lrvCl4vCgnLIX2Z9ypoAfQxezATh97ZzIDlsn4b4Su2lkNM1mYE526INcvAy%2F2EdwMf5mQ1ERnhr%2Bml7FDqdEU25ARkNp%2FqBaRSLW%2B6ilKBypc22GjLlzBRRjr0fRZeczUzJvm4MrqE7V2WeWvadmZrgSNgNquUM6q4o1dY2SpF56F16e%2BQbh%2Fz4sFPHe8SM6drqIYykOQS2Pqz6ESdthydKzZCPZzaTkGuwx1%2BeHOYVL%2Fj6Y6%2Ft8oqnjy%2B0WZYq8%2FdqqGW2i5Uux%2FavPGfb827dc2YA%2BpvGlxugmxLIRgdmSQ53oUy4xRK2LW0Q%2BIyFvto8rSLrRPm%2FzmPym3M%2F%2Besr5LluimdByZ7L5y3lO6IP463U1j7AAJ%2Bphu7NLep%2FucDNcfM8Nn%2B02a2Ig%2BRmXVtXycJESVu5GgzzUs8NJg9oagAOvvK5Qqtl8JZorljze8T%2B262reqcUbsFc2hdnCDSWlHoF5jKAu1YUlRplChhHzr8waisbpwfeS%2FvbA9PZ1J7Lw4lF3n4Jf0Tg0r5Yxa2akWPwY7gvyi3Za9FBbYjohYw5RT%2FE2%2BbrDdq9PL%2BZocVP1hS9yBrghAMLLVzq%2B77ZUmvoaSD13%2FCswo72IvQY6pgGhtdCAy7tTKXrEpO2kty7sEM50esxtx0yzK0rRU4MqxuP4y21cc2CU0Q9bx4qO%2FHljPjlS1Dg0hFWOPWwhY1nUm%2BstsJAfpIoowbvt7l7R7Mav5OETV3Y7uz8Ue7ohAvlpXfwjhh0UuA62exAq2lhP6syw%2B73evNgMt%2FHyXxnJmedE2P1De1cgturhTQ0QZ0onKDhAaMv7RZCI0uKj1A1vIzQw7bZ5&X-Amz-Signature=de35642ea97374e37d29f8db32707154c30b054838138d2308a0e0d2eabe2e2f&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRHGZGQP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIFVXnqlvdKMC6hKPSMSwzacjQEGKFfQC9fjgmBX8e9AjAiBViSPGJzDGoNNRvbdzG8K9TFpdqjEzKGzcwNe%2BcN3HJSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMTgy0lMbPnNM6RsQhKtwDnm6GORvWNzWpxO96sWDKVp5lrvCl4vCgnLIX2Z9ypoAfQxezATh97ZzIDlsn4b4Su2lkNM1mYE526INcvAy%2F2EdwMf5mQ1ERnhr%2Bml7FDqdEU25ARkNp%2FqBaRSLW%2B6ilKBypc22GjLlzBRRjr0fRZeczUzJvm4MrqE7V2WeWvadmZrgSNgNquUM6q4o1dY2SpF56F16e%2BQbh%2Fz4sFPHe8SM6drqIYykOQS2Pqz6ESdthydKzZCPZzaTkGuwx1%2BeHOYVL%2Fj6Y6%2Ft8oqnjy%2B0WZYq8%2FdqqGW2i5Uux%2FavPGfb827dc2YA%2BpvGlxugmxLIRgdmSQ53oUy4xRK2LW0Q%2BIyFvto8rSLrRPm%2FzmPym3M%2F%2Besr5LluimdByZ7L5y3lO6IP463U1j7AAJ%2Bphu7NLep%2FucDNcfM8Nn%2B02a2Ig%2BRmXVtXycJESVu5GgzzUs8NJg9oagAOvvK5Qqtl8JZorljze8T%2B262reqcUbsFc2hdnCDSWlHoF5jKAu1YUlRplChhHzr8waisbpwfeS%2FvbA9PZ1J7Lw4lF3n4Jf0Tg0r5Yxa2akWPwY7gvyi3Za9FBbYjohYw5RT%2FE2%2BbrDdq9PL%2BZocVP1hS9yBrghAMLLVzq%2B77ZUmvoaSD13%2FCswo72IvQY6pgGhtdCAy7tTKXrEpO2kty7sEM50esxtx0yzK0rRU4MqxuP4y21cc2CU0Q9bx4qO%2FHljPjlS1Dg0hFWOPWwhY1nUm%2BstsJAfpIoowbvt7l7R7Mav5OETV3Y7uz8Ue7ohAvlpXfwjhh0UuA62exAq2lhP6syw%2B73evNgMt%2FHyXxnJmedE2P1De1cgturhTQ0QZ0onKDhAaMv7RZCI0uKj1A1vIzQw7bZ5&X-Amz-Signature=82896fb722e54bb5a1624d118e6226577a8f7290aa069c5171946bf47fdf3d2f&X-Amz-SignedHeaders=host&x-id=GetObject)
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