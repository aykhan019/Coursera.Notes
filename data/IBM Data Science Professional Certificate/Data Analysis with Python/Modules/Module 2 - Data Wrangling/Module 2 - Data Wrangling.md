

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654T6LK4I%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCXSm3Y5EEeW2ni9hQazE7Mi0BYwI9xIpVeAhp%2Bg7pcBgIgDIYDML3YjJo7lcWZzkosX45xYf6JDz%2BlCswxFbwXNUoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDI8eONvdv%2BeUGtj31ircA8qxm%2FjHT9OoCG6wjhTNLYr%2Fe1IZ1Dwmoo6EhQOo42HrMghr1qBPlOgOPCX1%2Bco63QZjKHn19mWPNFH8cyHE7TdAeE1kYcD4vUpH3v%2BvC4woKlUoG5RfqacyzQgA%2BqPQeHWPgvMJmR48U3DpNvMOxb1PkEDtesWyQy7CFq3uoLgLn1zuuNSSe1uNVA2B5LEPFF1b4M0iehEFuMpgS475l4MNgH%2FkcIe0Y6CMH%2BMSxvyR2fSZLeQtAOmqOTNBT1%2BbbB4%2F6ktYHFgoPHp8QFJPudob8yZWEja5ZCp8MuneZHhENt8GRhvxLMKycQhMYaG5I7HlWkLGpdi4BPF0JfC03UuQ9qhUfAfitpEHUDEVJXC%2BSvUa9SjoU2rMLH4Oszvl9bArknu0UhWgh8HgcXE0kXRlFQzZtmki%2Bs8Jr8oLDDCQxdx9MTQWCQ1gGAtZXPVno0jIFBaPppRr9Mzg%2BCZVm6ZhbU06uRSaeAFY0GaXa3KfetPT9svWHJiFgmY%2BWNm5a82GrK%2FFnzrHPt8XeHXLtJcuuH4rrCxiyw5yIx3vYF56uP9X5yOjGcSZIlBADFnObfASZ7rMe%2BB5CI5dnbKrYWjQV1EzYOaSKRfXv1kP80csMtJGxWqVim5gNw1rMJHNir0GOqUBfjGSRhqSdXtpYyH7c6cTdWppWbe7yphEo207gqyEiWqVec%2FOFN0BU1MPqiS1kJkTVpxUHJKiekPLWRasibPKYBXvr%2F6eTHMdekGlfJ3EvzZg2oOQA0T6%2BR2pXW8a%2BCw5ER0GlH4rDtCminnmgVNrmNjpZjLD%2FAarq1TxiBzWkLFN2I7R1xR5X4fw1sKjdHbcco4dVbdcvj2Tfgv5MsqF%2FwSIskxI&X-Amz-Signature=e871d00e58f25796eb8aedbfbacf29bb2f5720732773b0ce12eb35e1f55ef8be&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QBXBWQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIE4W7uI3s1VV40LrWQDWK2gCUAoRwA5Mh56K%2Fnk2RvopAiEA%2FM8RO6wb7zFI67s6XKQ8Qizgv3UJgNBU6a%2FTY3B8VBUq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDE3zlR6L7pii5jLUEircA7IMsL%2F%2FvAkJ8t0iN7IHJ%2BUzH5MtoiRkOP3PQSI0tFg4N%2F1MCC4yHSSQEXJLgkb8njUN%2FEhEdwyjd0M3%2Fd1Vcq2wf9TyqwBJLbfgyjsLkDS6Un1zw9OaV4E1XLQDv%2BsTUkmb3nxG7vSbDBryKzk9i4%2FabxLk1YdjKJHY7ZpnJ5SrzcH2mIELh3HGB9yxU4znoz%2F6uAu%2F9T0DBzUey6AW6sMFMp6FhDWYLZB8iIFi9ZfQcHv894azlHYaZpDjsOAVGOgFpSIJPmiTl6zW2WHTiA1TOzIG1DjHw6edOtrNHm7KYJ4ZB5y3qd5aUlcg0jGwDoDxzjrXZqaKR2NGofKs0%2FKRQUd49HDdlO61tq7sVTUxhgwe%2FHBdnvLu4JHl51iQSmnVjWnUOikicJ0ujCqccwvRJT6p4pRuaL1YY0sEUczDBa04OOQDrRptXadYcMVDGUlc9llZW3YD52PAjqkDB9PgLHrB9jRx8m%2BDJKVG0rGZFu4N9rsUUPagxYkm6XneSEfmHT4MNeGiKsQ1u3Zfdtxq8PcrWz4ZVz4tLJEHUlIoEaZ6foA4JOfaF6esPnykUBX%2BqeKB6nLQUPH3mamgs6z4%2FaW40GlbDVr5II28xLCjyB5ey%2Bu%2FJ%2Fr4CeWwMPrMir0GOqUBqBrKHKhJv459wm0G9ABsdQhwZrgb3maabKIpiBRIjqJe%2BG3Z2y%2FNNsHysCp9Qym4N6rwXzjTIbozJqkB0zYQCCaikpPjWO7%2B9aKEmotHobnLqoXxiLkvi1xM%2Fy9w32I8MHROnFIq8Xh%2FkVDhJ0D3zTBO6CfRGBS6R3wLgMGLbCz%2B0fx0fKYrklVldH7zimWVLL%2BTKmu5vzboCUQOn9mulpT%2FeJmb&X-Amz-Signature=9e4c5e804998dfde744de6d51617015a762cf90f0463202d10fd69c50a1e4d36&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOIVGOUR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCRW0lW%2F41w%2BlRNCD9OfhQddIYhRQiaYRp8HrxtKdNjAgIgaIy9nIINmTPNVgAJp1dDCMMdYY7eZvVX0sLFsE6sBs0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDIMEDhD9j%2F%2B9NIWY%2FyrcA3lHTQVR36Vp4raEY%2F0oyzoJb4uFumewx3CZa1wBA8ROeslvH8SdPr9pF87pLoIESyTzJf2NMoNlgFnQPSqBhs%2Blfn%2FRMKJvEnPGImzMNyUInr4nLDXDxm6v6hE0LZzd%2Bv9Tv79K95yEoyfNPGBmZFARdipJHP%2BYGlZUUwUoqtC1cmCpREDEZOkiJYZbCAQoXVaQjKltnmBsuF1c6ylZazQ65OL71He%2FYrvA2yBGpMUhp8dkghFXB%2Fk8EYo9SQq2yopf5pj%2B7oYEkh7VhLNobFlVtGvjUUznKbisMFbeKXpkCMnMJtDBmqT%2F6LMSQ6NbxvtXlmuQH5uej4N7%2Bpq2SM88km89S8bZnmk%2F0i8Dm7C8rraVnse9znZ8nnggtQSYln2Q1Z26OLvuILXjK2Q4h0N910xZH7g4SMi62OGg8unuWFmzaIlQmAias8fv2K55BHXyWrbwoLF31FCdYvYvt7OvcpuuuUDf9PPUScxsgWjvs94rZ78Pv1w%2FIkVeWpHPMX9g5QUyCu%2FXs0l2sD%2FowKW7KcUnPaxY%2BvzHbv09DfPTnzvDKbWmmjiOAq8eIgD17bez0WNDTZAIWrURio6kMPPc3dyebVF7pXJV2%2BdcIyN9%2BT2DDuQnvrOZJplvMJPNir0GOqUBagfvAVfd5pZyDwLMTk%2B98hBMafMaIGmF4KvL8AJfzZsCuuOQDN4ab5xYv%2B6Jy4IM8ZWjbT08CRlTA97YFSZG3hM7BqcoAeAKzG4YwAxOZfrJpHJhTnvzgdVC2QpWp3%2FbLOS6E5RjrRkDmgXXekr5p08NpEcvaRFowGCqIoVrMhOz6yoZHD4Slm86ntyDBzxYRY0guH2H%2FC08DnajwueZDiU7qCCN&X-Amz-Signature=22afc7636f4a7a92851f60dea150fb80e4603ab47e88fb9114d208d15081a781&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNTPFITV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIGqzZN1y1aQmITDSx6cMiNkFXaX10grpmLw180WrHJFDAiEAqaHFyCKxM5ieq8PpMLqy5St8ZnrlMtkV64GN8Jk1GBwq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMnYdOjm9CE8GO0A%2FSrcA4qLzQrivgbTzibYjAZ0B%2BB0yllVKhjEqa1wpa0ZsOc3et463phXhADuEynRWqNHBjl9M%2FKlboP7vQfpTHpLzjWfnBi9%2FgbDludaBda%2Bk09rIEzzG%2Bg6nqf5lG5tPowXGvZ4AoJfJd257c3DvfxfqEOdoNQu7kCFmVXex5PkHt9UpytwQkzLaIwJi5vKX3MUQiWyFUOSCjmlyf9brHSDBv2C4xEQ%2FvBVcuvZunXaR%2BkMFGYPi2Dyyptjfl%2BhbNUTuq0pbmV0el%2FqCRxqNWgysj2QVHYao1vxvarea%2FX662Bbz9R3crRS8wQYnRy8HZ1r%2BrxIxeSIzVXByix5PKJueI393zgocyp5PnUb6DXh%2BX0A1Pf8hE%2BEp76sEwQj5jF33sOSgN5QJbBVyQUaDYolvpVzuyNuw%2BMrnc8whOpFAaKKFJX3TGP6s%2FPIK6M0Kkg9kKrpbYnUHFooXWFSVID%2BD3oIoS%2B3tt%2BTUQ588oAf4J03EJRQ8asY4EhB0xgm0o5cciPVpUHZt5a%2Bx5WMk%2FJd%2BZvAxcStqERIjnT4ZhDzHYlYcomqU6H9rLXWuF0l0LZPpDF5ns8tA70oT1TGNKx1LOg3%2BzSFcaihzW5I1p7PcIZsyF1n2HyldF4%2Fo2Q5MPPMir0GOqUBLOyCUjtZEwtdR%2FgRAODxPooJeTENg01VMJOGJ7G%2BKsWEDMNdRdyEORFTP6njDtCjjhB7mQt4L9DmrhubYb7YkYpcXWzZwCch%2B286%2BcNDQbKmxaVWtJISbu0LPh%2BL4QvgnJsvCqXEdcOB1av2gmxWEaGdn23jzlzbv1GphJGjjiMIWdVMAP3gVS8fWEEpRnyeD%2Bg1w3cV3onRAs5XLA1gzAJpKk72&X-Amz-Signature=0ae0eaf0a8548d3efe2d0800c334a3a1c2fc4fec53549d6a2d3f8436417e1855&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HT37J3X%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIGg3X45zJx5rqc1BYYe3qSYlMlVPto1hxjKAS0djK8EjAiEAgM%2FuWyTahI4obtxdpi9Tq2mrqYtHcdJNN7ZM%2FUPnqjEq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDDKnD2NKMg0c320i3ircA8FpF0CXG5%2BmJQ3xzr%2FyhocLNcZHbL1gn0z7Ck%2F%2B20xbjbzeeL6fXatfGsB9OgBSkBbhJCwlDSykcQ4p9rBbB2Rkdqz1vX%2BAX1RUsW7g0bWHRJBIULXfq4NKpGSQXb26fwT8yByogFdUai%2BipQN34gcr68NBcw5eKHPlBDncSwBBln109p08dyUtKR%2FRj7OVONF2xJPLF9IhPT%2FYaP0iDIvmLuQJZDX%2FEc1mG2rL1xdp9lHryvYevqKfmMlKTn3RY22JK8yks4boXGHv%2BVgz0mj7UfuL5a6qiAcHfxjcDz9XXORtCeq0ZO1%2F3p27jUlHOnP7gI2SgulKDL6OkNe0SAxX4LmjhWdBDCFPaDVeVFMc3qf9jY9%2BsFPV13u2z%2FNm1DKXc4DdWGc6hLnQunSSVtk1jh0erl6rJ2GCeMRR7E67VzfX1gpLLrpn2gDHS4qCnMbO%2FJItAc4rqk0dS%2BzmklF2%2FZAw%2F2RQ52Ajv5o3W4deLucmE7CzzKxs7UIQauCLJ1t9zHE1tljW8nN%2FYhQ3l7IxopbCvI0gMDaJCTFXYlWZTWtSIKiFfRf5ertHScEM0zO%2BSl2AYpT1TBrXJfyVLxy5ICHRx5GQOkDbbZPTOX%2BFkdKosIvgxES7rMTJMKLNir0GOqUB88vb5ROJLWTJZDhmjy23kUlRVmjNvDDVFLyi78HHdMC4XzsxzPTj4%2FCP5QcBqBssMy3YiOq%2FGzpemPkBOjFVr3QjHGoCHarJnlAoucuLZjTyXAFaUV9lztWFh6uquwtBwmQGd3jS50bMPs%2B7uk565nqSVYciW7IGEy60KmnMDNWYQSmamd89BofUnZVgH%2FqfE9dWzOURqqV3rq6VPPuhlpL48irA&X-Amz-Signature=187cc73ecdc8a0255f83ac1e8dd667fdf2e20b1b46739355eea11224d1a5d9eb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X55L2VF6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIDJ1GmKkA91Ddoth0%2FqMz7T%2FIbKGHjl0QRknPxCzEIIgAiEAn8YeoKV9PKSRhZeytj1glMl%2FZl4CJLjel6sQm8Z5rmwq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDEG8bCckzn8NXoDDECrcAxYrYg6E2vKHMXslV28uHCy%2FY2C8QfD2X7ItkD6KyzlGtdJw32O4AZjL94ibdHn9zf%2FF444EuQwwcEA0iE9PpE4C7PXRN%2BZutrBr2WhYVtV5YLSVU29pR7UKcJNWJQDXEflW4HnKD7ykSsWAZv6o0tRqy46LSNJBXOlSNX8nDOOI4iO1H%2Bo4m0Sb2N9EkBQRcmWB4J0JoF87hHitz7luIdqqI27ApBaZ6L1OEcneVxkjbfn1fbEdzryOVrCstohrbYTJF6Xgtca%2BwSBgSWo%2BWv0S2xL2fS%2FXiZbthEr8ydGlxEtWWHAr%2Fi4EZ0E4XJYzi07OW3HGWDutun9b88PcAcrLwUqt6YBPrM6LnDegqDSDaTNC%2FQ68D0ahgFZM1fJ4PnSI878LY%2F2qsRliyMfA5LFRPxrG1ICLhek0zyNNl4rKo0e7utAMjVZb7eqyJzxD9TpX%2FBnLySkbHVqU36xlXuT8liX53p5Nc5C6mqWzIHj7l11Jg169N%2Bk6UijQt93ntYyO5XIF8WcanBDTa%2BqzwPoUSBrnm9nfWYlL1lA%2BQwzsROxLIQBGABYQgeC7gt4dL19Nqq%2BVPEmNUuJ9dMotcu20foEAj3MFV8DT1tyUZvp7NkPXjJg9yNBlv0njMKHNir0GOqUB%2F0uX5wrfi%2B9v%2BBn9%2BNdri9MquOpI8XL6laE9tqayjKzcf0RoLloT7pXebo6%2Bk31di6RU6bPGnKBt0i6lhmFRg%2F2rupc58TkmaJflvTOYX%2BhT4gN4ZegtmxV4rNpwkYzg9Q02wLPDx9%2FKwZ366uIBkjfr2e9tb61ZSzr3hHmU%2BI7OHJS7sbEGVrcSyvRYUYIu8WzMm2a%2FUgB6aKZeWYuXvTXBD3N9&X-Amz-Signature=d41434b0a02e8be98c5f9bee6e39df640447105ad59a3065b35044ee7478e43f&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JZZC7L3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCFDTMIbb571o6Upe2woXChAd7aQjxebkvOMo9GMeWN6AIhAJe4lMgvupjicx%2BCNEybjmL3GKYLyVlW9%2BLvM8WyhIlAKv8DCDkQABoMNjM3NDIzMTgzODA1Igx4l2lSZIN1h%2BFS9Joq3APgv4MjnjfLqdHQ8wZMJnyCwE9rESksUy%2Favu%2FtSWpAs2YfohmQSwkRVknPX4sejLSdUMyUYhn%2F%2Fbk7oQD4%2F1CUdKgqHoasp6rIbFvLPHakQ%2Bk1gUrPEwhiy93PyBL1n6vR4THPBZox4EzF6XKrtHhah0KdsNS4KNyvp2Ophh%2FLTkXd0A72grsgM6j2pJAeoeVjIbCMl%2FJ97xO6F3CMEgTF5AtDXFkCKU7nL7yH7Wn%2Bui3slaRkPltWCbWmGDWVsRuRgSPYAw40tiTKIJV399DpJcpl2rwn%2BY2LDB2nSh6u%2FVgnlKvFg7gEt1sjCF2rhjxRrO6jN69oBRU2Q%2BlyuonlwPRzmHs5SCwtJtakHucM06pAlgGnYXn7jK3uYMwy2uDxxvEbFI4UTrnMyTY3dIna7LbEgTxMdczre2DPB7WmS5LNdoTOmJxHFNESERzffuXPA1VQIqjxP7LIvNuYhl2kASZQmwpDr8FS9j1pHo7umaptcVTeVdqVpOX5q8hsx8wxOfZkjxzRfn%2FaSuJJDYXevXz1hFXlF%2FpT6H2u%2BIUWJQ1inT6qa2QKlkMUB3jhqvyCyqO%2BwJ6vU46S4KyiP3fkoNm%2FIwTOa%2Fq0%2Bhv6MkiB0gVxvlG4wQmM73dcEDCgzYq9BjqkAaENV7EINnbNyOwHNKDyQ9zM%2BNmf6JeLoM5FULGvuSdkvhtalhnEXsaaKz8M0DwkG7VxLpYiOPtOBQvytwxvUn%2FgaachVkFiDcwR4jUjNo15MXR8Nl13zZqHBRqnHsvwQjgXtMda%2BC%2B3Bhn9ItBu8MBoX9pXrBKjB6xR3s4PpJB5N5rysjPZnqze4uUNvGqcZ7YW9B%2Bw0EiP6kYx7UF%2BE9hX%2BF19&X-Amz-Signature=ae97e94e07c6ec7282b9288dfa68491e19957e522dabae6752b9254850d292d5&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7ESJGW6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCV0cn1DoR%2BuuO9NlC5N7azgJfR9qJnYM%2BIuELsR5qtKgIhAJwflkbYRLtNGZ2JA7tvizoz7kFipUQ6uGjUFpmIQlRgKv8DCDkQABoMNjM3NDIzMTgzODA1Igz9BtgMlDX3q8KKoHYq3AN1A%2B19nLtBYE0pTkgORjfSVK%2F0qxpSZOdHA6IQG6%2Bz7FxsK0l7M2zc2J8n6T7jsuU9vvKYJAV%2BY6Mactsn1A%2FiIQmXfP%2FeOGfF%2BltbHAXnZbUDiXZOyZaJOFw4cnW35ZkgqvDhEcd4dz2l%2FeV21%2BBMmqycd09j%2BsQTX%2B%2B4Sp8gwjngoWh2G3V2fQjkSoLGdPdZCQPUcOZhw6qJj9VCbFvmUuoeJM%2BO6A3ujAZxuTzwuvghHZJhYSBsH5R7gXzwP6WqyfoHXjizeW%2FHjJtg%2BkHyU2v9U44IiURbt4ALmkq%2BTUKey02ZdTPjTlvkESC7JQiidD6tNbgbk0fFUWaiamUgt7s0eiMCbKe%2BtgZTJlb7r4UykHyqv6BYl18z5bsSv3%2ByO6Wdgavdxm5B8yDsurJWTnUXWuTrTqEplWnBK9c8%2FogS8n4Vv6BIKEdxjMvY%2FikbY2IKLYNh2NURyCPROEQjtU8dSpS%2FMk4%2BeHWXmH55YhS3dgKvYRPSl7%2BRNdF9TZPnVLLWkxf2DZJr4kM%2FnYRRhwlSaByLyIu%2FVCZ%2FXNBt9D1BHkp0Le2%2F%2F3d7xALplHaIr3g5102Uu8Kbt6Y4Nxhatr0DyzwdkxhW1vSmsVehrgA70OcL%2BiQtHQ8wxDC2zYq9BjqkASZam8706d%2Bvkj2Ym4H1Vban7LPUlwx128O1tK10zR0PbcdaqITw2NnjJ7FGhz%2BKXXLuH9iTiD%2BwFFdTvY8XZCQamNMfvZUebRTiQfo6zjkklLZaIIJ%2BNEw0dm2IohGvFgk%2BTcRSCinsc6qCCLzs%2B7B%2BUX5SDvR6z7sd8UbVodeoQcAnBgF0YuPAnCz8geTRXjVFRZTUWFWDVIzbQVbhoVMIbGeS&X-Amz-Signature=41ca330ce02be6343bd960bae265f9fdad1641959bf690f2b2f16e7910cc6978&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HT37J3X%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIGg3X45zJx5rqc1BYYe3qSYlMlVPto1hxjKAS0djK8EjAiEAgM%2FuWyTahI4obtxdpi9Tq2mrqYtHcdJNN7ZM%2FUPnqjEq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDDKnD2NKMg0c320i3ircA8FpF0CXG5%2BmJQ3xzr%2FyhocLNcZHbL1gn0z7Ck%2F%2B20xbjbzeeL6fXatfGsB9OgBSkBbhJCwlDSykcQ4p9rBbB2Rkdqz1vX%2BAX1RUsW7g0bWHRJBIULXfq4NKpGSQXb26fwT8yByogFdUai%2BipQN34gcr68NBcw5eKHPlBDncSwBBln109p08dyUtKR%2FRj7OVONF2xJPLF9IhPT%2FYaP0iDIvmLuQJZDX%2FEc1mG2rL1xdp9lHryvYevqKfmMlKTn3RY22JK8yks4boXGHv%2BVgz0mj7UfuL5a6qiAcHfxjcDz9XXORtCeq0ZO1%2F3p27jUlHOnP7gI2SgulKDL6OkNe0SAxX4LmjhWdBDCFPaDVeVFMc3qf9jY9%2BsFPV13u2z%2FNm1DKXc4DdWGc6hLnQunSSVtk1jh0erl6rJ2GCeMRR7E67VzfX1gpLLrpn2gDHS4qCnMbO%2FJItAc4rqk0dS%2BzmklF2%2FZAw%2F2RQ52Ajv5o3W4deLucmE7CzzKxs7UIQauCLJ1t9zHE1tljW8nN%2FYhQ3l7IxopbCvI0gMDaJCTFXYlWZTWtSIKiFfRf5ertHScEM0zO%2BSl2AYpT1TBrXJfyVLxy5ICHRx5GQOkDbbZPTOX%2BFkdKosIvgxES7rMTJMKLNir0GOqUB88vb5ROJLWTJZDhmjy23kUlRVmjNvDDVFLyi78HHdMC4XzsxzPTj4%2FCP5QcBqBssMy3YiOq%2FGzpemPkBOjFVr3QjHGoCHarJnlAoucuLZjTyXAFaUV9lztWFh6uquwtBwmQGd3jS50bMPs%2B7uk565nqSVYciW7IGEy60KmnMDNWYQSmamd89BofUnZVgH%2FqfE9dWzOURqqV3rq6VPPuhlpL48irA&X-Amz-Signature=28d107eadff40d3a31e442ee3f040afc1b5113fee836b131b5490b5764e1e53a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CPDJHJQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIDi3UqeaQars1Ln7V51JMgktNZuhtQ4%2BoeqoZxuNpyQbAiBFp5w3sQ3s7lferq7z6TGzgb%2FV0ybWJs4ywBM30aW9iir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMnL8k4CfRtQOq0i%2BwKtwDYNgD30gCo2okcx6k7zT8zUlDpc%2F%2BoQ0SxyboiMR2sxe8W7ALzGeoxAsWXjb2y2kc7JtGZs6OjlgpItk8guG0dGxZWMw2hCb9L1XhtoTKvfa71yNSUM%2F8V%2FGPavAnXae5YIqQt3swOGjl4SaFqItgX%2B7bDnQV5fXhMD45hy6Dt0tcfC9s57UFNVsxxauG%2FIzdc5SAtA3pWgUyzi9v41reUL%2FVPsNaT2iGnKqrGVyqMzQrfOJ%2B0NiaqVglNp3Blcz6RAWOHZdNWNuavgdxQ7HXh0Ft9uOZuDp4u00pKVfQdLW7AIAaGj%2BS5eDX%2B3N%2Ffm1A5O0%2FtD7o6oKEYmZs3CfkEmWv9JEbXL0950X5IvEmJKtdfiN6c2%2BJBzOq%2BJLD28DpfNbQjM4P%2F7BgEjzScMe4lwgbW%2BZf3x29vTTk%2F1y11iPPEcIM4%2Br3Wv%2F5vmLF5vN3djokaDX%2BOogGa4QXdGjC8qk1r5Z0xW%2BDQMTrlLEqzksRPZKxFwBoierjwjX9TKo81LIDzTtNrBFUa8PUuq9uPzccQVFAV2wgxvY%2FWlBzPhsOTvGuPqisMvOlaRnrVhUSoMHLL2ZqxMzyF4Fy3uuY3EeUSN03xhUhm%2FqVV8AefP3QDIqjKhVZzn6I4cIwr82KvQY6pgE24dNkgkAp0Wp554%2B2XVoYgGj53NfnudfZLcCJ3xfHqC6CYmmhVUbA3Srx2YO3Mca5l1qtmaSPJ7kbicEaF%2FT1xhn4aCAN2jTwH8h7SvPzhrFhvw6dxCsuWGMl2ONWSEdq0muc0e3q4bC6DtQlXmD%2BTig8YR2IxBnVMRYbl37wNviU3lmGrtSUvmvX%2FyjkOCFKPtJZclqOyYUOzUWe32fLrc3F7HnD&X-Amz-Signature=c123886fe889826f9c05c5f5c5131ccd6c69b27d40fa75d1bbe48a050a1801f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CPDJHJQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIDi3UqeaQars1Ln7V51JMgktNZuhtQ4%2BoeqoZxuNpyQbAiBFp5w3sQ3s7lferq7z6TGzgb%2FV0ybWJs4ywBM30aW9iir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMnL8k4CfRtQOq0i%2BwKtwDYNgD30gCo2okcx6k7zT8zUlDpc%2F%2BoQ0SxyboiMR2sxe8W7ALzGeoxAsWXjb2y2kc7JtGZs6OjlgpItk8guG0dGxZWMw2hCb9L1XhtoTKvfa71yNSUM%2F8V%2FGPavAnXae5YIqQt3swOGjl4SaFqItgX%2B7bDnQV5fXhMD45hy6Dt0tcfC9s57UFNVsxxauG%2FIzdc5SAtA3pWgUyzi9v41reUL%2FVPsNaT2iGnKqrGVyqMzQrfOJ%2B0NiaqVglNp3Blcz6RAWOHZdNWNuavgdxQ7HXh0Ft9uOZuDp4u00pKVfQdLW7AIAaGj%2BS5eDX%2B3N%2Ffm1A5O0%2FtD7o6oKEYmZs3CfkEmWv9JEbXL0950X5IvEmJKtdfiN6c2%2BJBzOq%2BJLD28DpfNbQjM4P%2F7BgEjzScMe4lwgbW%2BZf3x29vTTk%2F1y11iPPEcIM4%2Br3Wv%2F5vmLF5vN3djokaDX%2BOogGa4QXdGjC8qk1r5Z0xW%2BDQMTrlLEqzksRPZKxFwBoierjwjX9TKo81LIDzTtNrBFUa8PUuq9uPzccQVFAV2wgxvY%2FWlBzPhsOTvGuPqisMvOlaRnrVhUSoMHLL2ZqxMzyF4Fy3uuY3EeUSN03xhUhm%2FqVV8AefP3QDIqjKhVZzn6I4cIwr82KvQY6pgE24dNkgkAp0Wp554%2B2XVoYgGj53NfnudfZLcCJ3xfHqC6CYmmhVUbA3Srx2YO3Mca5l1qtmaSPJ7kbicEaF%2FT1xhn4aCAN2jTwH8h7SvPzhrFhvw6dxCsuWGMl2ONWSEdq0muc0e3q4bC6DtQlXmD%2BTig8YR2IxBnVMRYbl37wNviU3lmGrtSUvmvX%2FyjkOCFKPtJZclqOyYUOzUWe32fLrc3F7HnD&X-Amz-Signature=97885558378e8b93b80016b885db78db7b25fd605cb90b8f2478914272a3bb21&X-Amz-SignedHeaders=host&x-id=GetObject)
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