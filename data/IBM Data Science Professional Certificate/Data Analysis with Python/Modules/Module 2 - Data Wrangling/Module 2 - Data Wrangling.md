

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657TTZBUN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0QyEg%2Fb%2Bpk%2F1bWXS%2BjrxWlt06syHxsddrW34mWa4W3QIgJTDHNWocCLo%2BKY4%2FwYWZ%2FEAQg5UZD5Tpv0btKdcF7%2B0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2FvDN4YDITZJOPwhCrcA4RVnZ9mNOgXxvPJ9koCosPXzcLGHWPfkbV52iVpiSaxFICfhOFMFA0n3QQyA7%2FRUPLHpzGA2X4t4dPZnLTkpspBnui%2F%2B%2FXkZ6eCHMfMiH4L88Dtkyb%2FuQ2MvlnKyReFd5IEac1BWxej%2B2J08OLrlpDjULHbjXPcQS8L5Olnz35P2irc%2FbmYhNRs0UEncZeIkHchB8iqabpjgtyB9dEVOYfkX5iTiGhSwKy4yYJWFVG%2FYiwW74o4l45qklKxdvrxLjqBM%2B4yN3tnlkWUahMiKuQwjupj1%2FzBltj4GFZtbZzO8D%2BXBmDUzcpLbIbwQOCWksSgUGHSeR2Oep58mH4DPhXSY8XOcKQNxQtrYay8Yk8b%2BJ%2FezGqjKINLq3T6%2FGFUDCdhOGyQdiDRiM10rjov2Qvo9LDjEpGdNCr%2Fs8uHXZnTvEOANCYAQI%2FdFvI5%2BPTSc5aUSbzIcf4zQQ2vDPs60LOquOmUfxGja91OBav6kLjeG8kfNWJTXPX%2FqiVSPUnJSsgzkveRgRXJufIcGoKUDOvGG0MVU1VCslqOeHfGOUax43A6WzPXU56QQGqGC%2Fsf6VxJ9TRkS70HGvSlBH%2FpHaLi6OO5NVVv9odu8J9%2B01zdMsF6wK5Y5XpCvfDzMM%2Bb%2FLwGOqUBMk%2FpZt%2BoDSxNu8J9XQM9%2Fkevv0Y5xqO2su%2FsbK%2BPODanAIKvvLTIKoUVUO5C5LSnYKIAh3ja29%2BT9iDpkKWMJtPvRsxWaauUH2PWHvtD6ny9SE0wuROZrY4ERpSSVH5yyo21qui3VxrVVlNW6r6kSSgeJU2gFzhaMKCb%2BoMRrNJEvf%2Fa39rK1fKKbUqzj5gv1ozVq0LKVXopr643fvfZJpFDSGJj&X-Amz-Signature=4fac3ccaf57c530615b8699e0afdae2e30ba3c10be6c1e902dc45d1bd0332c86&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5NFIPB2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHqWk605x6iiw8qVbkmJqNiNpKKFMOhCvXbDUtntDPrrAiB%2BUQ0AmG7oBl44V2CRIHfb00v0rbpQbkwrqiN0A8dTRiqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFRKW%2Fj42EViZ4Hx3KtwDxBH4oFTQVw3TrZW8Rr9Tyiril4wC%2BotZmNFUlqd1Jyw1KZSkCaP5Tjww5sWmWvNQLpm1Ii0s8GVin8r5R4gZkR4bk7DlDrE3UIqQh6xfL5nEqaWN2uyj6aoM42p59b81wXzzQHV%2FlPfeQQbsUdUlIbWeIjLnY3lhJIT%2Bn1Bvo6OTIBQ5hFZHfoJRlxr4PeheCNcv4pMoas%2B59PFKV4oyPDSBaBBDkqnu0U871HdASH9NGnmfiSxoxc7t9%2FPYA8NOpAI8J2QRLwrVDxCgP55f9rstMuklgcIbfECZ9OBhStNaeDQ4y7MEXoJdppNd29B7VBWOHBfwvFo6pqszPLmPGwzAUZgKpC%2FKMuA%2F1%2B4i55VTPX5c5jTU6kS%2Bsu%2BmuTXi648hW9CXIaQzvG2mOW54krWmb3weOgDv56Mor0%2B1GKk8zAYK19Xr9%2F3ltTRvmI%2BbAGlMVePBO0Ey%2BTIZfA%2F6pFIIYMxMtBBAkf77cSOY7je5sNSPLh329vlcNjYYrrq9bEOiJo5CcFBH%2Bsj663qp%2FwxPujrFZYdx1ZdRVHzX25JakaN4Y%2FVib%2FDxXYtEbRKuwolV8Adve5S%2BORN4zIR4Ycxgdd%2FK%2Fl4QP%2FW%2FNFlymm4NPea6VamCBml0CJEwoZz8vAY6pgGeN%2FEPX31wOso7w%2FFi6yCk6OP8Q2ZQWi8msdRIetAgPyFxBvROmZ2YcUuO5y7FhPO9m7TtNgg18qgK1MQKKNxvIGNNUQh9GjpdmV2bQ7vLFO9VyF164HTts816Do6nw5hbWindOcTdxqT1xUqzCcN%2FZaBWO6oziil7yz3uzeXQw9REHYNNPe9MJ6E7rHtm62q80Tw%2FZ35fAlMFGHblYj208Qbui%2Bj9&X-Amz-Signature=e2cc9b8a677243c103ae760bd23850201947213edb1fb0a8018e7fd64eff2729&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIROMWBG%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7zz6mSK9X30QMlP80nPIbk8S8HhouWonCaNORYJQbEQIgUq05lUbdisA6hqqYYqe4zobZwgjZ3IClaLPXszjpeygqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNoNBAEEISDO9fBLyrcA5RCKSlUEL7ggc19glQiFepHgM64xTHNOQwRW0JCdNocTtxLxGtJ0BrResakJ7Xm2u%2FejILajTmG8lsjXiq%2BMzpC9RzY8jAVVBLjt8IRSH3PcwEOiPppEArM4g%2Bp%2Bs7wG2do4MU%2FGDKLrh7Sj%2FuSJ5%2Bn%2FddYSdGUDaRcuQu8KGRJ0m%2FaxVeq3%2FrGvnscWk0WaCiwwseJicKjtqE%2BkiFb%2FGVj22hgypkze6FsqZKG318ukMNQpUzJJ%2FbAKCTV7Suxyw7OVPxwvxvIXQ5yyyVNkIXvrY0ddXeSBQuX9uWDUhUdzxUcvQAZoBTe5qQN7y50MTYJG6iq%2B8q4M83b8xfYa3tJ%2FMty3lUXvcD9fEfrcYFPofj%2BewwL5fHJh%2F62KuRRTca7rFlDLlw%2FkywiN%2BCPJpRpdCZKA%2BkoAniGImyXm5s2RSdKLHThjGzU8M7VijxIsl9lP4txVWqh09NhqC7DL%2FpIKonrkLcVdqgrK%2B8wEZ2UoZgxyMIFf8gTqd%2Fc8lf4eD4miMKMcFT1fjAaZzLpA%2Fsg07ovOr%2BkAWzjq8Fms1GL1cJVFzS6idmvSbfpPO8eIBhrD5NqC2mrw7qi5EbiOHa%2BEvOMfKeKYM1T3BgRCyOQ%2F8ehtZ8Rp6EC91hBMNqb%2FLwGOqUBp6SIo5p%2BaRTLGmmwjIbyIX0Ungh6LEkG7K7DLuk4F%2FBQ4zKnpYloe%2BnDrShBemk%2F8LC3UGYQtKoc9YV92YrRfbRIwCCmscw2EbPZmIa4bpVqTWQbisoWghinQwnVCR7HTyl42eK%2BS7I2D1aYqc641J49RSh0K4c832IM2kFqbzi63erHrB7CW64eyodcHh6WoqqIVJ5FlAquluxoAFNV2ivOI88a&X-Amz-Signature=aee861ddc4911b5be7bcac77fdd6640bb11cdb1294bd324d02517947c727fceb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBDZCBII%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzmTjkC7QevT6H%2Bl0hjXvz0cfSP6LA%2BGWi8XfMNNiWqwIhAOneKyWiAONmQgynpCYdpxNwTFPhrzx6y9HCBxepQUFVKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwCZ%2FS2oeIbSwFbNRwq3APi%2F0l9S26yOKIC31uVmupcXyMiaIpoaYFusDqm2nd2lIzHitpZhsXdeB5k7Sxvrh14C9E9WM%2FXlegIg5nussKf2ZNmOGEzInVBCL%2FIAkcwCddOHQus8Wzi0x4E%2BFjZrQcbVZLGs57bR9w4YlrB%2F7nVcqBG0qWsJmlvYsSay6d7UXttvgIDxN3EuQQUVCxsdXswCPXioi0DXDAhjUBj5NYQr8odiD21J%2BzMddwAQQw%2B4sEtRd%2BajKt%2FcStBCynkIkgoYtPcbiPM4%2FvP%2FfieYooSImb4Hh06PUNhEM2m6DrbLYr0j3sJDl7rgl2seBbBO1Wdq5FiUowjVrYGvYt%2FBQD95cD5IyHyosFcoIqGkTPuJGdF8OZxWkQpuOW2fdrecu3yPe%2BoFaPHdEEp4al6VMomMQZhwaBitBiCPMC0gJ1Mp%2BxPodbwquKTRrXC7ibGvusDlbCqj9dSYCBV7hH78ufJHzcsLNOElnzkQPNQmAB4G76Zy%2BEHDSHz2I4NhSjM6e3say8MW%2BFVVm6NoATUdAst4NwjlrSJuZMxVLaQNNVxYGreGYdXlHPZMt15gDx%2F%2FM1hJhj48%2F7oOZm9wWjylHTHng%2FnuR%2B0qA3g9mJFWl1gJxZZb2kY4hU4amAiFDCjnPy8BjqkAWL8EGCvTlT5s%2BxxPfpifMadKqmgWDtCM5zCC9%2FkPt5WnzNUUMZ0MrdHs04EJFfpHqk%2BqoAOYMBy0VrvWBz5HZ9tjlwwL2TZtsO20ABjJ4vbMHp9t8g2o3%2Bd%2BwRYCTiezYbSkPAhxCxXSqex8SCp%2B1yzjhXlydH7e1i15sPHEk6AQnvyq35U52trp5jXb%2BkWcjtuR0a68E1FTIFU%2Byie%2FGQzcORt&X-Amz-Signature=0b813c055b9466c700623fd3ec4182b5b3fac0f195814d8ba6d1119f46ecfb49&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GDPIJVA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG%2BbPFK30%2FLVVwA360RopfTE6qNBj3WttQ1C%2FAzsRcBvAiEAk63M6O2kiEr2RuYz5op3j1R2DQ6ZibK%2B43XV%2B2W6h6cqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPFtUpK%2FvlPaUqR0oCrcA9BvxB14wUbqHOpQYTdDQ21h18pSZzmNFf7F758f10o%2F25P8WI48NF3ai%2FMi2Vir0BFh9yokHt1ddSwfP25Ugv8JSgl15qlxyoT%2F9e6Bb6E5Pd%2FNcblPUJJRTL6OSlxYtH2G7fGodoeUdg7jIFG7ay043H2pb8Sw7M%2BjirKwBGsxBDFQGNEDOeEXrIWLREjWmHkVb%2Bma7t7hKbD0U3lmPaZMIAxxHgpG7aPx5QuW0Zo4coeb9K3Ro62pZTdDXnD1OVSrQKaKamc6EX3Kq8%2FAEJk4zgW%2Bnf9rpnsvIN3wCWzyAr8TRB3FJO7yWIKFxRwLAWF0rUXjq9W3A2k%2FXaUmgqdfNl1%2BZene%2BhRs2WMO6vjAJs%2FI8tPqryNcvmGX6rrxBc4%2F%2FrB20stPGVpI4et%2FdpYIM5mXpBaa%2B0kFtwv%2F9oymhIJmnLLNG6TJxBWPDojOs0%2BMwV1Yurw8L0L4y3v9v7axzQ3q4jZL7UIr1tY7LIhxnPubQ4K7dXeEjZbOvh8FbknEyM3aWGwetOsAYvVGXvyagQU1X%2ByLbgPrXlOn%2BsQybEZwOYppwDpRmzR5B5GwBH95P87O9cv0m1GzdpNSJ0jdMH7LSEWmBz4toaM9osnkKlJZQN8Uaw0l%2F2gWMOub%2FLwGOqUBx1D98lCOlkcqGUCDortWvPf5%2F4KS8j9C5jpRIBxiU1O0j28f%2B14ruOqXoEA%2B90TtBiSM1pM9JCNffqe2WVFEirgrgCiEwCKZUNyISscMAzl0hb7z8go%2FW%2BYgCO59QsyzRtEso4tCSDm0aLmPb0DFx0qxexN0thqrsJ0DZjhyfqxKSsQtFcXsh7LVfQ1sn6%2Fn3x1WTAgaYW2zMqCy7x3mx%2FMqMQQc&X-Amz-Signature=73d26d2b4715ed2ab1f631b95160846ddf078fbae58be0d9bef8b98729da7418&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WZHLAIX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC8hTwLQDqEHAVINO4p6WRxUEQPfsrA3p3gAOZIynez8AiBlNDO7M%2B2xYq3TzDGJVdHec1k7qTq7GdVBozndUTsSJyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxvgACmHVOZjxrNLjKtwDKG43m9DNv8hYzhbrRtKWdDiUcrszkdeXNtL%2BTTicSAWqxyDch72yrZEI020aXTBRcBWAAtPRBC9HFbkTJeQemDuy6CLsReB1EqsOGp2A2X9M1gJ54GBe22oyW%2BwJQjWXVM%2BZ8ygmjrWoL9y35YnPpD6EaQzg4UoXKPpDlm6Ht06NutTyLCnd%2FuRvl9Y7in3kbjKhhsh3Cr%2FQklguzYNe%2BlkPWDw1plj7ew11m6FmSGg%2F6F07JPmEHylyy6mSaUxspkAq9pX89ZYamFiw3i0sT11lzRLvTpDGzLH6LcaN6o8QAvU6ImZTuuT6PyppoUV9BirsIuiSjKAGnjttPWFbnyrbDGarwwMFRyEAYYIFGeKzrLFIMuBBSC5MK%2B1aLmLi3R%2Fre2rTgfoNTPg7H18dpq9c8DAKy4HC8sRNiFovM%2FlWi7fqKNyBKyM%2BJ2gky2KwNpdcFkfZAQwkT4SnPq0q9hX1wYZRCdvGnAySKO6b5oaP%2B%2B8YHn3imwz%2FmfKVGrOShjUHVqA4eL0KWdJMQ%2BpvJucS%2BVKGjA2Z8lPoqxBfsRCprUaJUKzsrtd34tPJRRhGyGmM5rPeYFCi%2FcXLUo4EoC4Pxf6tUnmm8muWIAku4dTcqJGnNIFWWhAmBpUw75v8vAY6pgH3z36zG3rUYfg6RL0bZK%2FrQ6inHr71LMvKbpEo3g2ZUpTryEb1Q4LHVQksNcC0zFQJXVAPmo39Zg%2FqKoYmXyxNXy65VGgiOgbug%2Fe7nsApA4g34ODRD%2BLaLiguTI9uGmAwkwNMHzTsMv2EQ1og5q0JU%2F4Bm0Vbo0voLcwgZyMzpUdWcBTYji95%2BLVB2%2BjbDGh3nQSsesPQ5XINfOrlV6QKrhYvcvcI&X-Amz-Signature=e9103a0a0b8217c7e938ee09989e87fd33403cb4e2b8105e250bbc70c3fba05d&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWGUSMIF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKvN3W7S%2Bno6AZKPQCUu4Pczzs9qUsh2Ak6FUrOmhInAiEA70djCM73NPBhmDBWSny6CT7bsJtg%2B5Bcm%2Beb9HuzRVYqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEcT%2BVr9iNzbx3rsICrcAzWZnUBqa%2BBtJ8RN1a1xzGFaay9ixAY7dTH2D8K9mB2JA5wgQ2Kwe9zJ3LQl6%2Fr5zLG7%2FQvD9YApYeLVhM6%2BG79wXR3eomfqKe1s2dfu2ljjqSp%2FCYbEpBWxaeowK0TffTrzCvsr3Cu4LMRi3QBKSAM9pEuwhj%2FxsWLTsWHgn2hz30HJVncqmVmVLZHR7RVJWOkRw67ux5jowUPux%2F7r%2BdqeAfdMoYckUi4rH7KWRVBkW4H88qcr2dWfnchLgfgqG2p5BpY%2BtFPaooP0vT99q7ERIIN7OfAIjQh21ROEqCAxHFNZS5xU79Z9VV02qemY63l%2FRLlAT3HdppeByHDhjVNOy%2Fr5o34QoAhIE3mCnVkFJpV9XYzOTF6pDGJJsCL1jRhLehfqu6GFY052IsszR3U%2Bq6rEtPkCgf%2FJsGZtlZGJNf6YhEtWOpsR2SI3%2FdPLQYaAEnTqi2IrrCGuhF9JT7tMaHrOjd34zDTFGYSolb6uvAGXuWCl9VB3xh7Kg2tsb2DLhuEYCsBApTf3%2FZPVjneJwoAL0uox4zEggbfNTXa4E08CmJojoSB7kw7pZfav7IZaoI1l9fDnfZ3sqyaTpM25W8v203K%2B7gxGut2zvkdMu1nDZRMKjCf6UprlMJqc%2FLwGOqUBj0ZScq3JY%2FJDv5F0peeixb%2FtidyWEfj9NctbxXh1s64BZXQCWOBCpTTVMYABx%2FzxMuLX9Vd958Dbuz9Vzt8XyMKvAErVg%2BNj3KtzsMbBef1U%2FqdO%2BBXUltKUVhRdzyZZMdOwrOb5bIl%2BGuYGNzJ2Uaxh9im%2BbluVE1Dq2BZCLAjmn3cNCwp%2B1HSKqIV9MnRXxcfbMKz2tG5l7r2dBYtvYPXA%2Bvff&X-Amz-Signature=bbc25fb9b83eab26b175065f5fed72757ebf0e53c259df4e6c9600d2b93776d5&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666H4ASU72%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOOf3QgRiRbSw5OHFCO7jYihArdJktvqkGaqx37n07gAIhAJ6RvWJLxbwqH6gVSu8cf55ReewSHQJYJXffdJlZPG12KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxzhN%2BJZCsGz7%2FlJLcq3ANMbZgZ5m2%2FO8YCawpPo12OcVxb97VJS4pPI%2BCGZEmq4tsEexUBlBshmArJDJsmC25kpJNKiiysO1oJ0Nnw3mnzCOlm5dv34D0MUDWyJn3kP9PKQZy1P%2BHsvs14kQmX87aXtN6jZ1nOmraEFLdMp5Tf8MAuNsagpewCtmMeIlGvMyS1eKXkaNrxyDz7qsO58yayr%2BV49oBQ97eo%2FxGNzXdXs08eEsV%2BAN9vIZlLg2%2F%2FGiOYIueH5j85CH3rokRFh56ROhWXmjWYcbveBWSeFrzfp0tWZmiznLeY%2BqLPdrH07KLvtcnMNo4Sk3H9cgKys1s0yqloetK5paETnAJBWXHN3SgXq%2FTkHFik7Bx3z0Ir3k5p%2FHe4zf%2B5vASXHdTi%2BtKNJCGEWOFFz7ssuraCc3AifOTTIkznMYKxbfgx3dNH%2FURcnC56eyjPQVsn%2F%2BzIFoLlk5J8YD6bb5fXHEbBNiKZeVRkXuHQBNfRvpd%2B8e7fnSr9EkfRzZx%2FypHRrGOCcMYDHWWC%2BybV%2Fo1vt8TlDPl79%2Brvpcr4IZc%2FGD9XqAcpCeTcPslx2lAXY5W2nCOtrEqwtJSwVK0689jEwARRnKDd6Wsj0qo9mi3xdd3XsfY4Fp4dAPgj6dw1D6Lj8DCYnPy8BjqkAQBa3P8U9OIvLZpk2e1rFxEzrmNjXJW7GVS7byo%2BeGmR2oSOk22VGJNjmrQRnbJkcCmsDZMfy30%2FWYIKgbjxPih1du%2FDEGQdQaspUb0ftjVl7eXP%2BCrFDYCrimwxh6U9nQJ1OQsJl7SwSbI9HKhaIdf2FK9%2FT21cu2uFNO0UozsZ2W5NhLbnlvrxPS4JT0BaLJwq9yoSLzw%2Fy2LRW4Mon3%2BVRBsZ&X-Amz-Signature=c3db8c38b25ad5e2b8a99477c5040d18cc1b90a008e275ad326b4c453fd60ba6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GDPIJVA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG%2BbPFK30%2FLVVwA360RopfTE6qNBj3WttQ1C%2FAzsRcBvAiEAk63M6O2kiEr2RuYz5op3j1R2DQ6ZibK%2B43XV%2B2W6h6cqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPFtUpK%2FvlPaUqR0oCrcA9BvxB14wUbqHOpQYTdDQ21h18pSZzmNFf7F758f10o%2F25P8WI48NF3ai%2FMi2Vir0BFh9yokHt1ddSwfP25Ugv8JSgl15qlxyoT%2F9e6Bb6E5Pd%2FNcblPUJJRTL6OSlxYtH2G7fGodoeUdg7jIFG7ay043H2pb8Sw7M%2BjirKwBGsxBDFQGNEDOeEXrIWLREjWmHkVb%2Bma7t7hKbD0U3lmPaZMIAxxHgpG7aPx5QuW0Zo4coeb9K3Ro62pZTdDXnD1OVSrQKaKamc6EX3Kq8%2FAEJk4zgW%2Bnf9rpnsvIN3wCWzyAr8TRB3FJO7yWIKFxRwLAWF0rUXjq9W3A2k%2FXaUmgqdfNl1%2BZene%2BhRs2WMO6vjAJs%2FI8tPqryNcvmGX6rrxBc4%2F%2FrB20stPGVpI4et%2FdpYIM5mXpBaa%2B0kFtwv%2F9oymhIJmnLLNG6TJxBWPDojOs0%2BMwV1Yurw8L0L4y3v9v7axzQ3q4jZL7UIr1tY7LIhxnPubQ4K7dXeEjZbOvh8FbknEyM3aWGwetOsAYvVGXvyagQU1X%2ByLbgPrXlOn%2BsQybEZwOYppwDpRmzR5B5GwBH95P87O9cv0m1GzdpNSJ0jdMH7LSEWmBz4toaM9osnkKlJZQN8Uaw0l%2F2gWMOub%2FLwGOqUBx1D98lCOlkcqGUCDortWvPf5%2F4KS8j9C5jpRIBxiU1O0j28f%2B14ruOqXoEA%2B90TtBiSM1pM9JCNffqe2WVFEirgrgCiEwCKZUNyISscMAzl0hb7z8go%2FW%2BYgCO59QsyzRtEso4tCSDm0aLmPb0DFx0qxexN0thqrsJ0DZjhyfqxKSsQtFcXsh7LVfQ1sn6%2Fn3x1WTAgaYW2zMqCy7x3mx%2FMqMQQc&X-Amz-Signature=1c65b571e90c8d078203d69c58a68b74791ba66b163fd3ffb77165a20d4ce47c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXYIP7HW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3MIS4NqY5iJwf7YiD%2FtrCMZh8PnPyxIPPbw0tOvtjNAIgRyWAd%2FAtft%2F1sPe4tc1v8YJZg%2BPu2K4fhBt4roZIF3kqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELKi0OCHJKI5boWdCrcA1fo2RHW8UMM55bBz5NxFA5ip%2BFcCQLcUOvZr2%2BIqQPotLorOaquST5J3JdYZqtt2aHoIIbZIV3VUEkKw5wL3gzBnEl2kOlZdOefewiw%2BC0PHTc1kfFlhxOvLukd84SsXpokxeMOQUJwSVSZM6FGd%2BiC5xCj0k%2BKDH7TKVvwP%2BpO5zfIHqVDLhUNO7z%2BUAaTLiNTor830%2F1ZHIC50Sv458hCDgDln9mMGuEnnevZLzqr%2Fn7Ga71yrXJq%2F0zjYNnri5v2UYZJDJJeTapO7diCBkzyCPIKd0zbt%2FykHJHj%2B5ImWzELQB5f7Xbbey0O8tyMNMRmvoXXQsV5hN0MAF3%2FgnX%2BvLnhy94WIoMHnd642VSlp2yJEdshd5ZVKM1uN4Pj6OBRs1fCwHIC278IYzvdA34NX88QPyKcmzTLNNM%2BZN8JbFcL1YWSJQdTR1%2BasTvePOYH1JuiRjjQ%2FYfqXSF3U58Nwzmn%2FKOD6R3abW3ywxelwJUtmu9gh5wm7e4nHsdr23B2fG0fydlrIX%2Fvh1wGWNyS284MLlmEbep%2BD%2ByybrD4MXn3CFzivyREA6EC0UbRZa%2Fplmct8lhKi3lGRjfesSzSOTrs6JocbxgJ98UoPENLPEXy5PKWNRyUARaWMJac%2FLwGOqUBafQnDKI5lrKKe68tB%2FfAP8wakOmByVUZ9YCYdoGhKEneYNdecdtO1l%2FQ81fkXvnnVER2mTevW764RRgFKI3SmQcueh5SGGlSrsIhT6RNnEqQwKGmJKsN3Kl0ONvNMDO5Hi8Mt5izYJLaL%2BE%2FMXxy2RYNeW0zMrnL1sB4CGTfG3gLFKWHKb%2Fw4qa%2FxC34iEgUsY5rc9B1tCsH8ouQH6Sceiy4yaUQ&X-Amz-Signature=c0a6e38be4945cc74ba85ca80c02df200907d9309717b8f07917cff8e047e044&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXYIP7HW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3MIS4NqY5iJwf7YiD%2FtrCMZh8PnPyxIPPbw0tOvtjNAIgRyWAd%2FAtft%2F1sPe4tc1v8YJZg%2BPu2K4fhBt4roZIF3kqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELKi0OCHJKI5boWdCrcA1fo2RHW8UMM55bBz5NxFA5ip%2BFcCQLcUOvZr2%2BIqQPotLorOaquST5J3JdYZqtt2aHoIIbZIV3VUEkKw5wL3gzBnEl2kOlZdOefewiw%2BC0PHTc1kfFlhxOvLukd84SsXpokxeMOQUJwSVSZM6FGd%2BiC5xCj0k%2BKDH7TKVvwP%2BpO5zfIHqVDLhUNO7z%2BUAaTLiNTor830%2F1ZHIC50Sv458hCDgDln9mMGuEnnevZLzqr%2Fn7Ga71yrXJq%2F0zjYNnri5v2UYZJDJJeTapO7diCBkzyCPIKd0zbt%2FykHJHj%2B5ImWzELQB5f7Xbbey0O8tyMNMRmvoXXQsV5hN0MAF3%2FgnX%2BvLnhy94WIoMHnd642VSlp2yJEdshd5ZVKM1uN4Pj6OBRs1fCwHIC278IYzvdA34NX88QPyKcmzTLNNM%2BZN8JbFcL1YWSJQdTR1%2BasTvePOYH1JuiRjjQ%2FYfqXSF3U58Nwzmn%2FKOD6R3abW3ywxelwJUtmu9gh5wm7e4nHsdr23B2fG0fydlrIX%2Fvh1wGWNyS284MLlmEbep%2BD%2ByybrD4MXn3CFzivyREA6EC0UbRZa%2Fplmct8lhKi3lGRjfesSzSOTrs6JocbxgJ98UoPENLPEXy5PKWNRyUARaWMJac%2FLwGOqUBafQnDKI5lrKKe68tB%2FfAP8wakOmByVUZ9YCYdoGhKEneYNdecdtO1l%2FQ81fkXvnnVER2mTevW764RRgFKI3SmQcueh5SGGlSrsIhT6RNnEqQwKGmJKsN3Kl0ONvNMDO5Hi8Mt5izYJLaL%2BE%2FMXxy2RYNeW0zMrnL1sB4CGTfG3gLFKWHKb%2Fw4qa%2FxC34iEgUsY5rc9B1tCsH8ouQH6Sceiy4yaUQ&X-Amz-Signature=feb99e31a72ea259f5afddb1cfd465d9fec6d3fe2377e30ed1f56311612e640e&X-Amz-SignedHeaders=host&x-id=GetObject)
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