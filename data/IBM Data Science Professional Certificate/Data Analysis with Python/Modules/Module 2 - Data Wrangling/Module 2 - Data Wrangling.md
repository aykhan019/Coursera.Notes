

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOAYYC43%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGpbWS61Fzq5bxGFSMSOT7bfQn1rigRSqmHZKF8XnJSCAiEAprZN6cGQlKo7c9EK87vQtwKoWcV7ZS3toCJGldRW1ogqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEnZTaUj6B2LXfjFxCrcA0n9e8HSLq%2BOk1%2BEUOWOL18aLr7%2F26dDdSamEcWitWX9xERPfvlntoeGimfKfxJpdbOQb9B7BKUAOzlvyKpiBgogz7g2Znd1E0RAJAAsLlWSjAVOsdFVuiMOpXlvACE2Q2%2BylJuBVHNuz0RYOnRgh4PH%2B52%2F%2F%2FPFzEONtm5jvvL%2B7Ez7%2Fqy%2BsxYe9Ywrfcqxss15%2FhctOkQGrHjNFpN1jRWezmK64bE9B354ooghWr0SfS8y4oa3w0dPT2%2FnT9p4T5aKpEenvgLVQYezLE0zUyCEF7WFYwuGanBraxAUgW7VthdRzgOyirE93KWH7jzMUXoJlsLFwWHCOcQle0mCSD3U7njo5M%2BqImRCgjWvPpdwfbW%2B3EWg2BhBL9uiU7xwivmudNXr4WvDeKsRTcwSJJLPUiM9d9zlVvpT4zbzkeP6%2FBX6RAYcXny36bFdicsZvR2Zahucb6ExlATOpP%2BdV81p9PapDbC%2FWxinN4CnvfB4L5cuUMDUcYr66%2BjQbF25CymZmzyAJDjZUCP44OwUoCQtJoDiPQEYL5WvT7TUiuZajYiw49E6Vjp1cLvJf5D%2BXKEmkt13eg8AqBswyv%2Fw3cI1BFnUV1QBGv%2FvkHxzHHfMcdlnhcDbFmqmQn%2BbMM%2Fh%2B7wGOqUB1tdJg16PAjrn8vBGpQmZKY1KkPxXeiH7R8i%2F560UXFOiMx8Lp3UK14l9D2xXexCh7%2B5VHQTXysGy06sL9PjVTt9j3ibxIkiemeazxiT7mjPpxdv321cNluDRDSGI0SHRKxLF%2FjOHtLGfjgA3c7W4PZIRWkPuvi6h5fhNl2CBOgCxYdzeTY6qbzBrM0Fu9W%2B0dafh1XzepGArZJxGEqyjIuDNX2QV&X-Amz-Signature=3e7c156045024c4b07864492c872bf1c7b3c55aa462c554ffcec8a540700eac2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIZHBQXI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTyi8SkzlZXk%2BhNsiFVF4Er2BOcw3GrtbEuzCA6Mbm%2FAIhAJXJH7rxK1l%2F500ERBWjvL8ax6lA1nEP3FSnlo%2FxtrdyKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxa2o0qUlT5UDp7ikQq3AOcRb4ueDYOWrigDfQ8H9FZ9%2F8jqH7Ihp5jmW3ioLkRgFhXXl9Q7D6X2%2BduYaEk2RiGxyW4MLNlYg6AsA0trtns%2BtbDlmMLkYC%2B0XxO2fUpVVYUvwjFUjdyQJ70BazcMZLOd1s39UdLB%2FmqzWpNN8Sc2WwYRqCSbeLXs8hglRzdjOxbfG%2BtHKZFxAhYqxWh3Kou9lp39lrm%2FjGdG8cFajskI7IxkKBgDXfPnFasdeU0Szmi5FGYDcsBRkzc%2FzK608Vw6R9NfqRF9wU%2By4%2FEVk70O3iWXK0yOtB%2FjRkMuspVelJkScohf2mJWm1ff8qp17Sbb3Yk9AqcAkmQ%2BWmH9104u3jMphI%2BOPnij1chLQbXXHE745KBDq4qg4Ntx9bdhk7WlrXQ4e6ACywabFMYS0zXsS15P5AaBlBW1NUUfiJTX5gtSZGcNhHM43IZw5O4Njz0hrXLKCTD73qGgmPsJ3XWmHxNDv1b55ESHmkw0b2BNBUxDLOB%2BjKSYcPM33oJ0HF1JJx%2FWyuH3di2ZiH6E4AVZaxDnRy%2B05im1gvJbYYk4pb5wKB1snAXOeO0ngKO6YPJdzD2Rj4E9F69DM9B0TrauJ1hNKFIUQvTRClCsJaDL0XVnZvOR7TgYAi%2F8DC64fu8BjqkAWFahOUOQFmrOnt904xazGPUsAnrq6I5vA%2BswVRWBz4vivvPJh2e5KRGqmHv8FOck0JTwUHCleOTugyrhOOAkyycmH%2F9tcUgd3%2Fx8F4D9T2mpTjNKSLcJkukgGma%2BZW1ctZe2EZTb1c23SgmjSdp69TnjuviOe3wpzyyE9YEbOzd1uFZ5rIhWjc3cIgj5Ivv1yjjKCNR4fzVVGqaUFDtTSLjqe5N&X-Amz-Signature=7d4dba663edc418b14a124488dfeb3bc7ae6d590ff9f2befa2ff6d41ff5a529a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QGHLVY5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGP1cBxTb6dyNaDjrXr%2B6GaAUDW7Niq3ePCSdiAtXPN%2BAiEAjEkRCNUXUYf1T2ttFFHPOdKj3J5jrULbxgAznQqKHbMqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDr%2FUDLDrmRG9g%2FOhyrcA3Y9nLqjXyATGt0fu1%2BDWXYbtISlCX595z8ZT93tueAiQvmPKL3P0xpUPl7P2g%2BMADYbg0CtBynCzeOKeBwHPlYIu2ehVwMTw%2F5jdDf2GKpPtwTvsFV3R0MVu0AiZXyGvmfXlFjg6Gtl3TkeP6r4Po%2Fzqu8NQ%2F6vNv8Ea%2F%2BPijYiELOcXjDiCDZnSVRdCL%2BLbFZsVSMotFYYFyCLw2JiBmVOJsN0Uae9P8ojY%2F5S%2FGpkNMt0KLoL22hrGLuAx3CSfRj9MGHeEg0bi6LxqMegZ5yJKczxOiBsIMuZ7KLDoSa%2B14J6uU5hJbactXrXG3UpDJ6GMFREkf%2Fj7N2mBTW%2BOXhxASGHCEPSJYnJ0aComdVRmpPqRH1v%2BCoq4Cbbz1VCg5JoNx%2B9e096g8HupMgdiXQ1VD2tiMHWttlc5UszmD0RsqsycYV5m76N%2FXQWQdNb%2BztWKMvsI%2F%2Bp4F5rg5JLeI5PwOO2si0yh3V5jbZVftuDYp9%2BtkYydBSsT9Kv73xilX9FIlRItBzq5vR6%2FHH9lZL979C%2BSeMUHGkNXMHmMe7iELCLrjv%2BbQC75Wj1zIbpNFmQHbtXtH1INE62GnQZpEWSZHX7wfdKZ79QGmqTvl0JosFXz1mrjFYYV4GbMI%2Fh%2B7wGOqUB2oBv67sSfW5KQsLTIy4l%2F4w9vXO3B54Sji%2BRVDcW%2BA8v7Pp0h%2FeYjKBA5JK0HMbJ22pAzKMUx4lClo0Yc%2BD7IZK4cOUujszeAzA3d%2F1r8nzITcL9kkml%2BuiS5a6WeNvkiFZGZkl6WFZISO%2FWFlznZ0M%2BubGQ3Pr6%2BRNPDTAbCEm3IA0oNPE3p1vf2%2Fg2fbEYgYVQz7ljGhkIc04Gkol3E19B36nc&X-Amz-Signature=d851022c5f0755238c86d8d0e7e7f4f8861e8cd38921df458d96bb01045895a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6PO4A6K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEo22CFLXRija1d65q5ZCIhy%2FBhQdFBOgJsSaLg0DtdUAiBQi4kw%2BEFyOQ3lSRnVIReVkByWwuKVcF3tOHJn4gaC1iqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFvZLhb0gOjPDdNZLKtwDomL7EbLpgkh9Hvzr5Md%2FE04bca7VjtLqhKIevgIPEXqUVudxpoiS%2Bdq4NmaVZTgyVKFwysfhyUCpZdaZBYyDm5qJWtOu3TjMk7uFLbz95b8N9Mqs4KqGN7SOk0kudpknDy9X6%2BL8QOjTrRTYY1YxRUGxDmezbRHHCUA78y7gzKj3gPPu6tfMXN2DATJKzYtIYZqlTnWi0XwwXWObEOPtHBOvDHAtMgolL2wslQgniReuV%2BrTyY6BjGPBjOZYPL3Ztt6tmnBXMmPOrYJMR0k%2FKOFm6XPfTWvpV4cIBiFSEDilX78MPyP1aBADtS7kPRRzgIKSO%2BwnXVC1g7gJAa05FWGnILFyRYvFc2M%2B2wgMDHgNI8pE8OMYnz5A5PMVbSlOKBY8PWvUqVdgHGkhwsel3N6pDHqIBeRRtwndFvIa6jvQ%2F9VSJ9x9evHpcYPAAE%2BgxvO5ahdEev7D5I9bCcOmprbrNmPI91EPoCJl0u44fjeGchUToRyBNouFGI%2FqR%2FwxMA1JhT6H2I2PLXuxe%2BVu1%2F4FB%2FuvvNLI3XuL0DuRUg1MCiNCDGvgDyQSdV5KK9WicNq1gvBiQTeRTy8hMGTFVvv34aBcciuxr0kgqFkbJEkgHVSzQVzqOapzmnww4OH7vAY6pgHjxwzOFW3QNccB2lw9BK2DlJfAm9bUo%2FvftZ8BVuYEhHEMlq421ckA55J5nrjeM7VcTKuaCODLWt8xuXzvmryPCJ35bI124C1iIjP0ZaoIKOAKDKCDbhlR52v6DAY51R7Har6lNo3cGx4GcUjnIj47qdrSH7Ad%2BGMyujlEl12hSye9oNdCeNVEfnobFYjnfpGZpvZAHgDv6LG6RaMOylIAexmMpuhA&X-Amz-Signature=886986f22282c17fe177dc93bc6f0eb7a7846a80b3ae7a27a0c1413da2a9415d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSQHYFST%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCdqf68KZYuiS05Jsq2HVJMWJ30uf5CWeLpHTUgZxSvGQIhALj2d34z3ihj92dQ3tuzkrzBEWBxVSffav%2B%2FVLx5LontKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzI5P%2F1djrL27PL2tYq3APcU9ML6oRCXOZqrMZ9WOu23ACJk79JeDcH8N%2FCCq%2FOrVAivzqKtdbVGH0WbRELUezEu2UvKajSynOHeSEBNzorxcp2q4xwc7TQCzmM2bnmpUvUej9vNrwifynz7o2QiDWIuAA0xai96ndmNigVqiEzZ8cCQp7eVEBtvQQn1suPEFrM%2B6c%2FWHM%2FPqlDxhEpGI7VHERXov8Bwr%2By08%2FciQeGEZaUytyZ82%2FF1UykrI6nin%2FeLVfTNatjItOt6woIyhgYlpu1NnST9qugynxbpD%2F%2By0nvZqvA8T%2BfR%2B7R6%2BZcE6z55TZdKSXqilGJtaMc611eBA%2BmXfR6EZP8t%2BRZv72btLtuZOFbpvGYG4zbQKWLDIZ11DxSCNytF90ApBiyPVpEHm%2F2jePFSQxuu%2FTXAUsfrwzcMeSXbFItO7rF0hf%2BfhhUpUfHBnVrqP4KzVbeTd9MNqmdqmHc6p7KcEWM0AoJXj9wYn4QRktcBqR9nEdagvYweuy68DMOzErlKdOrRSTmXnnkXTvXuo1ROonaImVE1EVsjZmb3eoDhOLoIJUv85YFu%2B1D7k1197rL3mJbFiEVqjV6Xb3UD0AHvA7Y9y1pBk9fmpMyT7GLgZUhVHUWdIN3maX9kRE56bWnLDCA4fu8BjqkAbU5Hw8TemGNJgXtxxlfwf%2FUtoYsQjI8wd44UPrNLVR%2BgpncNwxddc0grAn04ezRhkc6dh6FH3TBeAwd6Nk8gTClz1E4oGBtIHBKRhQB3MUuS8V%2FWNycGqmlZX%2FrwsgtG%2BSCn4GT9aT67zcy3TLJKWpLC3aTbX4wbhJYZ8VJxGOLNv6OKs6D8q53Wn1QJZTiNnhZY%2FCvz7Jc3Sqh0jQK651jr8Yz&X-Amz-Signature=3a13dc4b97c5a12929a0682e3524ef1cb90e380c1408102d5c66e0e9dec87a4e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635N3D73A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBxyEBSDwamIFRGo%2BDz3xIGFpj4fTogimNy%2BQG0VHSG2AiEAnqcM%2BUH1c8PjdYqJdlqTBf1V0%2BZoItqCc4eH%2F5oODXoqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG8vzgOW3yfFGRiMWSrcAw9r00koZQGznTNILninC5WLMJK9xh0LAUsjDhE0ot7Hs50%2B7arIrUV6x7ufu%2F3vwuQAW3t48RWg53BIfEmnPj83teMySr9TagPUiCOgW3bl58XpO9PQxqLp3XT7JeUanbRsp3LvVQaxOWb3n5iMvFpAbMHdI1xeAYGtyzLcn9%2BxjQNXZh1SVhCcEHRH55SehefK75xAPfE4jEYa2tSNDYLXKvN9nfuzBzQjH2qAWiocx%2BcftneGyyad%2F6dWrmKQK3oQlo%2FgDF38zcgdJ5aLpZdwjoV%2BJL8EvdXyGWReYaaJAr6VGJNBTQzSNFH3aSsPfKdZIwRPaBgbBLr6%2BRN4BpfI%2BHuhL5qOOGjG%2B8uinRbxYO7wqzehXB3B6pM0ZoUKO6z8nMJ1i3mmisJOwXtK8Byq4PHcimqV86luncit9CitQGRsQIQBG1nBqXbrTbIOJFqy53ITb67FefEGMkhjtXbDdnFheatrb50ZwQ9Map8g6dwLajNsyW8RVxhfOE5E4vJamEjQqQWq3zRRmIf2TIzzKUFWxwlgllTJNXmAiZGbYm296jAB6aBwtMZVHTYhtzx3azQ6l%2ByMdALGLmQhl8DBXXzyq%2BpAnd1p03v%2FU6dzHo09NikpNW1G8UnhMJjh%2B7wGOqUBCzmYIRdG3Yh%2F3WwG1QcGpPCW19fZqGBSeV0wWvQdrmDMTilj%2B75f0rKzL%2FMmqZiZDuPbxoXnpBeJOgq4UCi5Mw2SUy53QbYiK9Tj2wT0Ng34Yp5rJv7Pw9N%2B%2FPjumkLlZD8lBdNDfVX1ZqHP7HLGnDCRcV%2FqNH6Sbxhg4fxmOnHRom6jvqSSXbB5VqPFzd3iYIXpFVe%2Btva7gU3gmTKr1NUeiq%2B6&X-Amz-Signature=042fad166e661fd9c67fb314fd4a7e4ae2be327725a066d14341eb86104123a7&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AVDFAED%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICoW6Szunb632EQ9GyxlHNJ11M9Yoyn15O9KvQOQki6cAiEAnYAChlDiC36mEn88nEmK%2FYX5dc%2FWxgQku%2FFPxm1OcdoqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJtOmCNZ1ndU5xD3lCrcA1%2B3%2Bte49aCFZEpA08ysQVyYmpjDXHxt%2F7uIp4N8NMI8sn%2FQ7AD9n%2FCJi0CTEX%2Fu%2FkxgGWJ8bX49bMub5KoP5Q7v8yLtFEVXgKWOjATH5IP0eUZJZRM4%2FmbOtEAB4AAxCk2yQpN563mUKrLlW0UmCRXHGAuwfSPkJp2TeDAUSDGNK11btUd2vUEO9Am3F5vYDY0GQp50ErdGKtRBP86LWcqZOUb7U5sMDe635QhZsQeeYnf93ovNJyY9qmWlTbxYl0zYCduO3NWEHejaXWBKi5LxJYkkf%2Fg6KcKTzAyNM0GMzGshv4k5VtRVBe9fxv30B8olSM6AhFqMqQr35Hw3rlTN3Z17RLZebnGdJJulTJtzMnzJkuJIlhRwFK0b2GZI10vKgM%2Fo94ekB2OCNCZ9Pq3qjhAGZfuOyjX%2FUNCkeMKWKbFsG%2Bvr8GqgVXbQ9tYlh2yB5oX52Rmb7nsHMtAwuRXpH4ad7aWvNWG78N5LDII6lhjKUTbBeozWLU7tVrx4wu6sL0vmRS8DkGpBg3zSzz8dS1lw12N9qqx0pZH%2BaYSIFAKnGnq5vgc6q1C%2Bfw353Wx1ecCtufYCLngD3%2BvbCZqlXJe1L67ePR%2BZMFaZjrZin8c3WZDTixqxDeB%2FMMzh%2B7wGOqUBWdQYiCHS4%2BK4zgNRejcWBWoqxNV1zQ9eQmYL0JhU1hty0TLqBmzF3LnZwkmdEIF5mM5l740LH2tAeLcENeudOaZbMnkC%2FL%2FzkQOoYoRkltRRchDYpe5BzDOKkCrpQ0TwfDbkqpsW%2BFZOG%2Fle3tFcFMlbrlFENz0HarpHHCrYkTNI%2Bdj0E80M5KdarEcs3RDdHsHfYwlKCMTDEzCee4QVvJSryQQn&X-Amz-Signature=f0220f32e47cfea2451a7eccb6493316e6852563110f2dfed4c1340c03b265da&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QYGE4SG%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpQCJ3SoDEo4k96WSEUzVrSTqt3M%2BGIhCw9j%2F9HGWWPAiEA0%2F9Cbh32VUZBdghO%2FVSB8KXpSSrW178dsHtbpIbxp64qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD0gOLs6QQiIN9XtoCrcA0XSdaLTrX3rB8vObZR%2F4jK7GWBQ9zl%2B1VV8TzImkRT4jbc6dv3v2o7H4ZJBnl8Fy7RKtFxY2tsnPWvs%2F%2FlBoz6hBH%2BTXK38QLrT9Z6NbWlYy6RH9b7DgeGOZz%2BOBU%2Fkm4SlkCnSkIVAgzDjFDYBcmTsDkbxSxrg986YqVJqsCArMaOab6nNNu%2BBjwK%2BwdC1oNP1mDtxRoUSCnZwC9lcYHYn1VOaZVqlWKK8CM3%2FUmtoZj57SKJmuDoIeZWJ2PuNW12VD9FYn0NdY38QfbETNo4%2BHK6CmN2mD%2BXbUW4wQ%2FYlwadseXovMNSYD3RVsJTaxahqRfNkx3ePfeK5OQQd29MC6qykQal3%2BhIkSRrMfdfaVwPeqDpJ%2BfeXMrtADORdvaCWAwQQAq%2Bgw%2F24vEUeZPYLo9Ouq40%2BP1q82SO7Rw87c5diIjRfvmMZUAXEe2O2hba5jMMySL3cBjT%2FBJrtR4BDaysumocMQBn4akTewZkpU8JTcDIBTZJoNS0PbuYrLsvI9dp6oqu3OIBHDrKtA9eck%2BvW9R41RlQaSJ%2F1pABhaG4gErRUyR1OcKY7BUda3F5J2ktb3%2BWuMuM75KSdjqC%2FdMLeKJQRG3NSWbxkvc4ek%2FPUvpsfRz8wyRynMLfh%2B7wGOqUBvX83k%2FYtbBM0wCt3PgtGcCTymO9Gcf99PVcWDgHGzNKmgrI9i2Te8enNzhqlI5XEfqRuORPkw%2FIK1gK5b8%2B3is2tvCcoLzXuiQSl4IJy%2FRNiVSt3IlP5DuF3oCq5Edr1G9IuN2ps%2BPagwBgCDj87eR3sYe8NUALh14paUJFW0g8kTaoUCJK%2FZlFcJdQ9YlYGkyr9kNlrfstlgzmc4MkmfpYRpsS%2B&X-Amz-Signature=8d69e77bd269073ebb0bcf2f87e825c4320473ff55a4d01ef63f0f5ddcedae8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSQHYFST%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCdqf68KZYuiS05Jsq2HVJMWJ30uf5CWeLpHTUgZxSvGQIhALj2d34z3ihj92dQ3tuzkrzBEWBxVSffav%2B%2FVLx5LontKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzI5P%2F1djrL27PL2tYq3APcU9ML6oRCXOZqrMZ9WOu23ACJk79JeDcH8N%2FCCq%2FOrVAivzqKtdbVGH0WbRELUezEu2UvKajSynOHeSEBNzorxcp2q4xwc7TQCzmM2bnmpUvUej9vNrwifynz7o2QiDWIuAA0xai96ndmNigVqiEzZ8cCQp7eVEBtvQQn1suPEFrM%2B6c%2FWHM%2FPqlDxhEpGI7VHERXov8Bwr%2By08%2FciQeGEZaUytyZ82%2FF1UykrI6nin%2FeLVfTNatjItOt6woIyhgYlpu1NnST9qugynxbpD%2F%2By0nvZqvA8T%2BfR%2B7R6%2BZcE6z55TZdKSXqilGJtaMc611eBA%2BmXfR6EZP8t%2BRZv72btLtuZOFbpvGYG4zbQKWLDIZ11DxSCNytF90ApBiyPVpEHm%2F2jePFSQxuu%2FTXAUsfrwzcMeSXbFItO7rF0hf%2BfhhUpUfHBnVrqP4KzVbeTd9MNqmdqmHc6p7KcEWM0AoJXj9wYn4QRktcBqR9nEdagvYweuy68DMOzErlKdOrRSTmXnnkXTvXuo1ROonaImVE1EVsjZmb3eoDhOLoIJUv85YFu%2B1D7k1197rL3mJbFiEVqjV6Xb3UD0AHvA7Y9y1pBk9fmpMyT7GLgZUhVHUWdIN3maX9kRE56bWnLDCA4fu8BjqkAbU5Hw8TemGNJgXtxxlfwf%2FUtoYsQjI8wd44UPrNLVR%2BgpncNwxddc0grAn04ezRhkc6dh6FH3TBeAwd6Nk8gTClz1E4oGBtIHBKRhQB3MUuS8V%2FWNycGqmlZX%2FrwsgtG%2BSCn4GT9aT67zcy3TLJKWpLC3aTbX4wbhJYZ8VJxGOLNv6OKs6D8q53Wn1QJZTiNnhZY%2FCvz7Jc3Sqh0jQK651jr8Yz&X-Amz-Signature=a538c849829b3061a3a848b70a634c40008d66c0fde9a781d70d3f5123b073b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IL5UICF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2LoETs7%2BexVcDq7J5hXp5w3KMELwCbT4N2RxR1%2Bhx3wIgTQno48diIb80hXJjIGOoq%2BMwmszSAkwjeamv7CjbW6UqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFTVXdvqISTv3RrEYyrcA9JvRN03b6hZdPofkr8yxjHzGufQAI5RCxGZ%2BHwFQMU09xI3uHITPZUkMSLhDWViY8TQIoD33e%2BnrWzjI28XCCd9UJ7gg1cg90e9WTmPhdvLnh1IGDGXA4BGieUysK%2F80lmckAeWjUYKw6cdReNYnlkbPqg5c0sg5gZK1fUEGfYvsGuCFyKBHi93buvaDOILhQOVVqZEkBkcntCdS3GL6tE2DkpbSbFoLINc8XiGnZ7Wc6qxcWuSeJ93KcagluoM1SzW03j3a5makWyhQyQB9Vs%2BzENq8LVfyYU7uJdiUDqA%2F89wHijuvNNAE3pQzp%2FQaO6urh00cvcRgiCAZR0QnX2X6%2FUDk3tRDp0Pfm0hqVyuAkJRD84qc35EXWNJKuJZr0N0DxwvBReHQetVLiXXpa9W3STTJNvShseY%2BCMzYXpKDnLcjmRCpNGQvBvgX8PdYr%2FzhPU8ARDSbCjQQDznoXjiZ%2BFnFDAXpHsOl1hvJZqZog6Ige9fwuku%2FfdKtZ9WPJHW0HQALE53FKIpRRvcSASZT39L0Rjo5Xz%2FscMgIf9BxqaQMOvgAflawsPnZ1AiOBx1w8v43kOtG8bZpFZ5KqGNhw0L04Z50p1squg4KN49rxKIEOLbtQ7AaqcdMNjh%2B7wGOqUBLu0HDITMtTVQx8chwDRYJgE4jNpf5KKuw%2FdXtGmMIgnJoCEBBJIVBVTM3EHUemR6aSr2zBKoTONSrAZBZYsatXILzpdY%2FpyaYQR4hgxBY3i49DqMPfsLemq%2B%2BiBNEGjIDx%2FnC%2FKC4QrAf0uRbgE5VDETWLhhiZmysrXrzs6OGtCkI3U2DCR%2FxVqlBypO1xiqnEExhGy1jeCj9CpRFyMRFS%2FkT9tq&X-Amz-Signature=866d8f2944fc571f1da3154de3ff338e2461a153b597330402b6c275fccb6b38&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IL5UICF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2LoETs7%2BexVcDq7J5hXp5w3KMELwCbT4N2RxR1%2Bhx3wIgTQno48diIb80hXJjIGOoq%2BMwmszSAkwjeamv7CjbW6UqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFTVXdvqISTv3RrEYyrcA9JvRN03b6hZdPofkr8yxjHzGufQAI5RCxGZ%2BHwFQMU09xI3uHITPZUkMSLhDWViY8TQIoD33e%2BnrWzjI28XCCd9UJ7gg1cg90e9WTmPhdvLnh1IGDGXA4BGieUysK%2F80lmckAeWjUYKw6cdReNYnlkbPqg5c0sg5gZK1fUEGfYvsGuCFyKBHi93buvaDOILhQOVVqZEkBkcntCdS3GL6tE2DkpbSbFoLINc8XiGnZ7Wc6qxcWuSeJ93KcagluoM1SzW03j3a5makWyhQyQB9Vs%2BzENq8LVfyYU7uJdiUDqA%2F89wHijuvNNAE3pQzp%2FQaO6urh00cvcRgiCAZR0QnX2X6%2FUDk3tRDp0Pfm0hqVyuAkJRD84qc35EXWNJKuJZr0N0DxwvBReHQetVLiXXpa9W3STTJNvShseY%2BCMzYXpKDnLcjmRCpNGQvBvgX8PdYr%2FzhPU8ARDSbCjQQDznoXjiZ%2BFnFDAXpHsOl1hvJZqZog6Ige9fwuku%2FfdKtZ9WPJHW0HQALE53FKIpRRvcSASZT39L0Rjo5Xz%2FscMgIf9BxqaQMOvgAflawsPnZ1AiOBx1w8v43kOtG8bZpFZ5KqGNhw0L04Z50p1squg4KN49rxKIEOLbtQ7AaqcdMNjh%2B7wGOqUBLu0HDITMtTVQx8chwDRYJgE4jNpf5KKuw%2FdXtGmMIgnJoCEBBJIVBVTM3EHUemR6aSr2zBKoTONSrAZBZYsatXILzpdY%2FpyaYQR4hgxBY3i49DqMPfsLemq%2B%2BiBNEGjIDx%2FnC%2FKC4QrAf0uRbgE5VDETWLhhiZmysrXrzs6OGtCkI3U2DCR%2FxVqlBypO1xiqnEExhGy1jeCj9CpRFyMRFS%2FkT9tq&X-Amz-Signature=cee0bcf70aa729eeb521df2d92ce00b647f96fdd63f80cbff9d8daac459c168e&X-Amz-SignedHeaders=host&x-id=GetObject)
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