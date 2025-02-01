

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664X6JD6MQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCstcB08TQ0edFacPyjGtBkO0tV94qdzNj54o8WWsxqnQIhAPVKuN%2FCDt42DajpE%2Bi1sjgrjNWmJ%2BRpIQ56kPddnCe%2FKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy8TZ0z1mtY%2Futl53Mq3ANq11dCbIatX4hRhD%2BzLhwdEJ7NSjZZO5hV%2B1z8IxD%2BLnRVzv%2BijKGnXEb074HOBCfrG1TuGRQ8jNdPp3ZCqVZyB6joCR2YP3d5OqOxVQyhQMKvOY63VKT3Ry6A8NXiW2KEzab3kWI1RqXMRn5xuNZENM8Z%2Bb0PeCSZ58uUAnDdYSltNUacloYJuIgeaQivAPPuX%2FJ%2FeiEFKLBy1jg6YamkHnKVqOoHjdaIHVYHGEtlpg3U778yzym3hY6p57GK5274dpLxz6zuK9zm2IlrX8Q7YjxXAMoRu1XUgsAHY93Er7cMFa%2Fvr568klmXi4MMp3wPRmsoK8vvH2K6ygPHdrHqAWIQk%2BVYi%2FnuX4TpYpWv64%2FkGBHFpsP6xE3MEhSbloVmOvhiz%2BLcfd821IuJXzJXRw4dYfwticju3Ij%2BeEVWw81UtN41PqNbntUTYT0wxPB%2FaCxf6%2FgMne%2B2M0myyOVJ3S9r0N1es2i0jQowpCBdwwk%2FxUFZi0QDibhOrqFMxAUqFc0Ky1cpBQlv1kAviaOzJ%2Bam0HHFemSkEdWO0L0etGu9q6nmzeZ%2BK%2FZ0KLn5gP43fEBR9FVi%2BdRlmCbbdmzfY1VaMRq0lxe7JeSnmcjsunPlkI0anOYY0fYDhjChpPe8BjqkAZSVlbATDLJkESLaenh89QtV2dl0FJxYxmvyOerZjvb4nvofTSRwmfokx1pjDaehg3zmLwggeOyGidSajzOVkt5kDN%2B%2FYXPKPWw82GUX5NGsULIvyyVAe82HxFMI64%2BC9SDRclX79wfPb2n5FDEERFa1CxjK50EFMK9l9Qgxm0n%2FIBfat7aReBfG8hNiE3KQSVCsIFhD2HsPk4%2BVkdJ2OZy3Dgnm&X-Amz-Signature=59d7f505b87d82862a88dc5e1d4dc895cd87489b3448e424a1a60b7e66d80349&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPVRUDZM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH98UY6o0MppDxen8K6dLy5Q1gFHh%2BbTMnHdjJP0xCBSAiEA1f%2Fmd1%2FpKnXVmCGEw1SuvIiF%2FmtxMqG%2BWCJ5NK6PIeMqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDgrXV8RN7IXAfeQLyrcA95GX%2FfwbG5714Ipc7AIgjiHvMrI5410YwZxbwreXtbojBwQTOXy62qbQpJTz90NBzHZ8%2B0pUnnArPtaEqEnIRMKAUiglijLH04YRKvfKlVdJMZVXRk7SZZ29X6OP4Ohg8xJEexMsMYvbEd%2BAA3DD1TLz0YtVxknZm7p9MUuQiOlpgtfFQAlV7qyRiOGc4KRaP43fOYEY%2BoAaFAm%2FUlFYhxSWeBeLm49u%2FpeMH0ekhqDmU5S5zn2E3sZ5c35S8zzy4ff%2Fo6EiDb3gmcYLQsYhtNkRO5eGYnsGJOkO94eF7RQSG8Xqyagzk7DWIHsgQW%2FeOZxZ%2F2ZniZoTDvc2Yg7xhWW%2FtrnnLhqCX4q87PFZjzqxEM0KQDtwxTggNoLz8MQ6DO4kMiMElfviOS4jcUM5Ii%2BI4wh2W1fb3xGSYPJZTdQ04riStNUQUDJZLp4pfWZCFn43vOvcdwu89j0ybIrZMpzn3Vdg1YWHDnVavf7H02aJKtvaF8cAJgjU0wNCoOThZTyCwagMujLDyEwOsdzQYXjSi3724plESkznu3Nc1hxE4q482lbPLzjmXkN0SJwvZ6q3hGGlrPNrGvhumF%2FcAVaSf1WKV36O6%2FzHnFbcHMJsDYHZAhGed%2BLebbCMKek97wGOqUB%2FeCygwLamlCRVCiGEb9adcBQCdNpcLecfljXBUZi71CPxy3z%2BR1B2xYTXm%2BUu3%2FFDNCuDq4qYeBw7%2Bn2%2BMdF2jbNfazFaiYg7WQ5b76CpAEph1G3T9WARqqFXCUOy0BqgNUXAa3FYorRw4UK2d1Rdyql%2F%2F2B1y1DIlTxgX0TmdrAf2VrGT8rz5t0iFbCO3XlYx2vXYNJ6WETwr5CNOFicHaM%2Fpv1&X-Amz-Signature=b7529a8358b4f18ebcdfac8e603df1b51eda290ca1b8391f8ad0a1a883a1e661&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EJVEU3E%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSwpGnYe5FW%2FOpoFfsDoZNS0VbK%2FVsZASIV9ctn2EFAAIgJaEFvmQo2kIt9nYnJtk6Dt1TCUPYSPYdqjiALBWa7jEqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCowBulIhaAJRN7DWyrcAwtXF07i%2FfKtNXq%2F9TMGyuS9QstEeKWMWjT%2FtDqRXAneqpSoV5y7UzIU48w3fg%2Fhnml7FjSN8aDIiH926JrYw6cLhZsudJmtyFJbKqOYNm7Ssef5lIjna36LizjEhrNJYmSPH93RXRC2D4y5kvHz1703%2FjEahISoO1LWGUl39YrFnLLSN7QVDfYO15ZqbT9H7xb4PvEeF8%2FoFcbJwdPiR1oSjw9UMIAnCwNJ3kX4JJitqQ%2F3OUWAbaHcKqMxBi6uKBgJGGNLyBMrLM49%2BaWybfxnn5zPosA8TtQjF%2B2%2B1XYgCSzjaR6C4d%2BZhbRDS72GwF9jOlGXleLpRmlrXGmNkON68UP%2FlT4u16tEiNc4ZYf6kuAz9LFTN7iGorXJubXjt8LgJ5%2B14p49eNU6apVtpQ%2B3hkHRSXCQZQTWgw16c%2B5U3APVshaKh80qt3jZ0ZsQKGKrq%2B%2FUOb8zYdlYzq2Dppx23ksdzivwo4B6WWojXVr9HZ0hpy8ESiHbJGq0wZrDsjozliWLqhSP%2FrNt416teswJ6PwWgyiYW3JYw4UJWfIKrwJUbbGzmmCOYjH41uPy3QsxAofdNYY5kmcDkdszpTGhTYywnL3%2F%2BXgK8H4%2BGIoAEVz2N6f%2BMbyCm127MKyk97wGOqUBaPGnw8Y%2FpGrLdZeVsbxYcyVFh7JJNrw5nwNLKpGmnVv25aijWRE7Rgshd7TKYjZCd%2Bi7n3NSFXCKD6mmbL2%2BFHiWOZQ8hUi2dfnhlDz4Eejwn6YUyzUNDe9x45yBcN1la%2BIhHionPER5w7AlJqnOBRv7BAJ%2BfypRaDr9YnfjfGcsR7eFFVkhkpAoiF%2B83anbowf4vqpuOd%2F5FmEnDvJ%2F9aewKwl5&X-Amz-Signature=7a407d1c266b8155c5fac9d49c0d2f45e83f7d20a4c41f47e041637bf12be882&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL6D4MZY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbppEbuGpo%2B1QXdeGX9JsREuaY2A28ARZQathECjcPFwIhALM1IY8T%2BJL33TR6KVSWExu18%2Br5P37hMEWhm%2B1K2cbCKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyjrjxaZG9OwSqxJPYq3ANXF46ncu3e0admmRO2cVzTgYgzuxJGnNKrE6wk6j4dJkkL%2BRHi3v7PxyqC8OsbAriAXXWnbg1%2F%2FISRpE1BDtnKwAWK0eLb0n6qzK1bFdO%2Bpu%2FC8Ku9mletZSa3%2FxMVTYYW1%2FuzgkY23VqxsK5NbzUo04%2BIHdLd6l8vOKMFUcXJA3d4xeSwIpGEDxruMhdgc1bCBWNQRQLmB06EUwfQ9kUpyPJ9%2Fx8xrqnkO9Ej3pluCi9odwHqAbeOeIi%2Bel%2BIRFAfE%2FaFHhDDXJ3SpjIS5uzl84GDvPMugPqCmTZU93MeWFWXFQH9QdEWG8kQe%2FYnTNGg665cf0MSmYxhFCkcVonDAYyyZ7W0bnD4tgnV%2F2N43McyLsKxWFhqOeDcOep15rRKkqNvszEJWD8SCrHQMhXRZaN3RrkNl8gPUIc1yKMh%2BqwCKIkrSevjYpUCEFMRswmf863uguTS2S7%2Brw0i2PH%2BkKjIDzPWBnnxEE45ti5fkYzIgdSdrWDZmWpTxZGhZ2S3ypXdiYS6QXL5PpZERolfEgwPANa8fAwEpkCXpRKbToq%2BG0Mio5wiPUBDEcKHzKDJg4PbgOwC0MdwCsBRNA8PBo%2Bu7E7YLrMc3Y%2BlW44owZy9mtpFXrt1KyvwSjCApfe8BjqkAQuL3kxSoU7ZddxKhNjwwCUx3T6mQN4lyD6hLU5GC1ogCpCH3CL9IF8G%2FSnMvywzEwrTYsrR83yqSwAAtGOgWAGRwQN6U8m7ybyIM4TnPZHxBzNP0ml1ncdPmAmzzQSAaS7LI%2FHRrbPyOhupZYNfzhGkuAYhpFLK4YbcRaRglx3ZOuvEeFauCeZL9UlhzEm2yKyA%2B%2F3I8yLPFKHKQjLaDX7UAJu7&X-Amz-Signature=dfc5d740b19ead5f46631deb2eb63fef7e22a33be69d168a976861d80e1a5fc6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKA7PELW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDAiGASD1P43E%2BsnIqSjDod1%2BU02OyY61FL6eIpsFFjtAiA%2B9x4Bkf3JYYNNHCxAGGiQM5fydzlsY0X%2Bd%2B5gR3uxayqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkD%2BuKaDzg%2BcHyED4KtwDTj1JW2N%2BrOfhqseN1m9FH4%2Blzrf%2FXCdAquFn0%2BpHuUd%2FzQsaWzsafVZSPGHzekuC4gDdDKYcG3uN9tkZviO2xFu9kQ7WjyrsPttoU8KNB1xfz6sBr982l6sBJZDJoD7%2F4%2Fv3Uz0VpncnJUGpW5zoD2l90NTH7c6Q5gch37iG4F44HKR6Ux7%2FQkU%2B4g1iZJeicGqdl5DdQVWURZbKgJu9PruTWBeIlETuieNGynld5Q1f%2BHBh4Dwf2E3NjLIpbxkXAGs6X6%2BslrBXy1QuUOhwjW7znu9xpNN7wKNZZr48inBtb8bpMkJMVE3oZFPOQJoHTTngcU2Dw%2F5gkkk3gjxg55KYx%2BrzCoNnfRBGAqJf8d7ufGiY4IEPZRwLC%2FMz%2B6jVrh0kU5rRSUDXyTwu7tVPl6abWunSxPpkbKsg2Nl3OMTAceXjjSv9AzyNjHazU59XmZQT%2FSe5SYCy3ppEJJz6IMj5sXPmRMRdhgIPPMeOrMJuUuJn8jT%2Fz1xS7qFbaTAecxMgXUW%2Ffpjhyn3S301qqJRSci%2BwExBCMDuqSCmHlrLVTpb0xsauKnDp18b5KqfkyhCRIBWKy4LAQ%2F5sTTSiG7h2h7rPGKCxWp6qCP0fSshlu0iqyuESPjWFAjkw36T3vAY6pgH13ldnWHRAPwHaYfknyqPXrGcBSpHNrDBlAyjGBQNN6NCAG2lyfG1RFdqFbUEFc8Wm0M8c%2F82TIzwsplDWdbrtSyCkd8o2hM9qELSFKjua22C3A3%2BP6xTEl6Ar6WoTrt7h8KWZcv6dd3S70pJVB5ZpxAOvVKJSK58L7Tc4kvWtW07s5W1UiIV6Sp%2B0KIwxkZ6uBjR5O3TiS6Sp7zCpa5PkIRsEC4La&X-Amz-Signature=f6bd1943b529d18d870da007c1a25f8c8492b6211fe758e72b57644218603142&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHIJIZHF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA0OxOGVSXlqxcYfOSXvFWFBS3RNL3l9tZlCNUkC3aR1AiBeYLSy2ncEQ30zmXZHAo5S3OvRvtmSOGvNYHL%2FC8oJnSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZU0OsbP60lyUK4QLKtwDaTQrDvVolhO30ulP3Ruun9SMIGSj62Ujqn23soeWa1vWpxSmFAp%2BwvppBlnuADMK7C6L0n8y%2FYSKyE%2FVATjjF7H7phwHtMa%2Bw3d8LmV6OD1pWbtB6xQD0czSzK9vr4yuTf%2FeI7yb8oFDQqmFu0zdCpLC0%2BOO2P0ecMGrlctjyB3V35U8YLjdwFDIK2Lhso%2FxdMz2difqZb7xH%2BwEn4R1x4Nu9Pte1S2eXtu2pc1D2LjKAdXH%2FXZ0nBgSS3yNSQ0H8KmORFFaasbm0y%2FrXNpttYqQmF05GeYTwlEAiSPLmhhv0Yj3bmvVIDz5aJivDXXv%2FHTEpPpQwVGZHwC1c%2B%2BdpJHTceq99oh6n%2B9Lg7ik7ZDeqNSxjv0NSEbzBCn7oGVGugXMYk6laZfzjUD0PCTF4VCnTGmVeZHNcJswJ1OKiU7q3dmq5Uiq6H82kyOBgTN6H%2BgWUbhX2auV3Ri6C33R6u%2FG3YGDg1L9kHW%2BVfi1lY3zAYLluohValYsvO4GUXrAPVHoXDOZdfQY%2BrhZoUlP8BjpGEQWRGbXcDlXEDkaZPZ0FhdXZHR2EL9VaE7m4WeweHaNZMoW27MRJjtPs5VHTCz19SDq7t6e7AGfMQf9x7z4k8FNq2gZFnivQQ8wt6T3vAY6pgGlMEdSW7RC2Yc7TVRoy%2BhoQZuPEXAyf6CnyRrk%2BMHdM%2BxNYxuX%2ByejZeDTOMePiata7VKRvrfrIxj7OQIJgE4KnwIWlISZmtku80bnUu%2BWhOQgvDtkxUhSMbtdbVki9yR%2FmMiYXO%2FKaGcfYPI6ghrfcpuVyjVqRUlL4AIJeMMvOobpELwPIXdFZUboLPfh1w0e11nFKTztuviwQmGpr%2FviRq29ft2X&X-Amz-Signature=b3dd30c2e432c9372ee0105b6d1f1fc2b80206d9bbfacbd5bec1039aef2b1d4b&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYLZPB3D%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDu3kLx3qVQMWz5MfSvY6RioHXMcif1eN1EhU71CI2%2FiAiEA4kXj%2FeqOlkykCUByshdfr0ZBdX1DEZic6ksquCfgzKIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHXUaqfROCM5CfqQByrcA3djosD1fVmdaAW6LmWXtojsk6PLl6mhaVdC5WbQO48xs7vHHkxel7Hj%2BH6d8kz1q3pipS9W5sjVwjIbuStGzhLobWOENrnWjn2VG24A0KGNAOD%2BcAA0MlpDhIW6mczb%2BeO3jIwni6DKaL5Iw6RKmgRh5QBCUVVFdC0d4jNCgDgavtWUnRKz%2BRMhIH1GfYlv2ASQm8vGDE%2FN4otrEyR%2F1O%2BSmk4%2B2grgmPdsjuieBJCrzzSqcMDa1aKUnzJjf5SLgDplwMyCcaeY6vJr810hpJbLaibS2M5B0AyCL3bGS8BedKhs26fPsvZRNJtZinpNa5KbP0N6wzSa57K15Wwc0TBum4X5O5r19VMkl7OtvJlhBiob0PI%2BoOAp0r%2Bh0Nw01xafba7veqTDkBM%2FxNaXPNKLrcFeCpJjY8dDy8Jf14fksYk6qlzNPXJzYa0UEE1y0dn2J8Kd7uaneFxlLvj20O7AYG2ZZDYhYyvtH6lgrwK4zH4Uu23FtCFrOcRBDg7%2FSaLCUDaw%2FGshmopi6R0lYuTOSkoCtItS22GXR8s1I%2BWazSnpVG%2Fb83CcZnyXjWnwwNRwGmp5TNhp5EE6yeO3DeG7qWNqJUy8bPpKf9e4lkSnkn0f30SUg3N50ufrMKOk97wGOqUBsW04QXPlaxc9dKZh%2B9lxWk9%2F67ftYqYAOanJB%2FXvylOeXnXHNh0BJOZE7Lt9Z3cw5hI0m%2FzRF5JWnnLlJFljX4q7JFRIlKTzEUjyJRxzPg1r1LQSOabZUSr6j6jSUnoTnvu9PGUv0%2BuX1cxECQ36jv0CGTIt7Os%2BTzxNXGCycsNzAN8n6LVqjOD7BOby8SSRG8I3uZsfzYrIgPhJmRN5Gi6mn2q8&X-Amz-Signature=e395a929543a1124a9e60adb08ec25dfb7da0ebd78c724979908c2fc3ac1ad5c&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VD4HJIWC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGCvTU7wLaFvyaoqxW5vybLVpQizRMtfu81%2FvtHGRUiTAiB5ULqTDwuDS6WpN0oNd6aFJoEVQj6d10LkVLJVufsGPCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiJNeaOWAjA%2BGx9zEKtwDvZCClo8RG2XuCZFCWGxis69DDN3MaBRB7Q3wWQ84W70PpasCkaVSRB1iWobKx%2F0FXlCl24bZYreWptM2shwQNhtYCF9ab%2FIL7Zlkqh7bUOfkVJjePtwTzG9uFCwKpfzevKxNcG5X74xtKpC0txz8U9y8voWemahRLJLgrE6VZWiapkE3Z3VfdZbTwTPsVbpv8fSRlRaEr7Q%2FHo6VnlF6PzoLNqdSrW3RlBHmJCfRsg1Zu%2Bz03vixcRa%2FQkPlTGXODHNq9WqJLXHXaipD9KXvkdaE95FzkTt2wgPPdTSI9y%2FZ2GpDoXnUBOS6zMcslB%2FG%2BWugy5VDn1Cosz8TT4%2BXhdRxZXca6F91%2BIutpOADcO1rQjqqKdjhuZMWFu0gXOCcaNKkL8Ucg2JtbSDxj%2FjiKUtzKIXqMiQ1iRNzyTlo%2FZlqV29BQ5sHIs5uD1Dq6ATuLu%2FDXu9Ve6OBppmUtvpj%2BwNNByQ5Pp8gySFrXPPBkCThrkwBya%2BOBc4qYIp3YLwwjFF4kWdvd%2Fi2Sp7UESHHDQ%2F61rtDV423TNQLlJDWYl9LER1WA%2BME9IwLSR9u2HVcdKvkC%2B4L2gRDjqcRO6YOUzTGgJySjkvKgIqbxOK3k3laHKCaJJA9EUzgX0cwoaT3vAY6pgHqyrjkIJZr5rTqQ4%2B4RC3n2d%2Bxq4Im7Wkcjl9iIJp7T73ZEfU9nIJRehuefm%2F%2F8ds10MxFcEgKaWIG%2B6RnO6JKe6%2FdxrrP4Aa6YlTJsv7ukcOuHPR2XyPcn2LcD57h6FlCYWNzHcodc9ktVjwM3XyavWo2r1FnCENBDUve9SExvjr10GvFZH1QUHRtX18e0dWGWrbpRObBdPpNoSVHWfQ9I%2FBFAM59&X-Amz-Signature=3e2dedbe642b2ebfe4fbb372c20cbe559651a7b211fdf9a227fed1717229996d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKA7PELW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDAiGASD1P43E%2BsnIqSjDod1%2BU02OyY61FL6eIpsFFjtAiA%2B9x4Bkf3JYYNNHCxAGGiQM5fydzlsY0X%2Bd%2B5gR3uxayqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkD%2BuKaDzg%2BcHyED4KtwDTj1JW2N%2BrOfhqseN1m9FH4%2Blzrf%2FXCdAquFn0%2BpHuUd%2FzQsaWzsafVZSPGHzekuC4gDdDKYcG3uN9tkZviO2xFu9kQ7WjyrsPttoU8KNB1xfz6sBr982l6sBJZDJoD7%2F4%2Fv3Uz0VpncnJUGpW5zoD2l90NTH7c6Q5gch37iG4F44HKR6Ux7%2FQkU%2B4g1iZJeicGqdl5DdQVWURZbKgJu9PruTWBeIlETuieNGynld5Q1f%2BHBh4Dwf2E3NjLIpbxkXAGs6X6%2BslrBXy1QuUOhwjW7znu9xpNN7wKNZZr48inBtb8bpMkJMVE3oZFPOQJoHTTngcU2Dw%2F5gkkk3gjxg55KYx%2BrzCoNnfRBGAqJf8d7ufGiY4IEPZRwLC%2FMz%2B6jVrh0kU5rRSUDXyTwu7tVPl6abWunSxPpkbKsg2Nl3OMTAceXjjSv9AzyNjHazU59XmZQT%2FSe5SYCy3ppEJJz6IMj5sXPmRMRdhgIPPMeOrMJuUuJn8jT%2Fz1xS7qFbaTAecxMgXUW%2Ffpjhyn3S301qqJRSci%2BwExBCMDuqSCmHlrLVTpb0xsauKnDp18b5KqfkyhCRIBWKy4LAQ%2F5sTTSiG7h2h7rPGKCxWp6qCP0fSshlu0iqyuESPjWFAjkw36T3vAY6pgH13ldnWHRAPwHaYfknyqPXrGcBSpHNrDBlAyjGBQNN6NCAG2lyfG1RFdqFbUEFc8Wm0M8c%2F82TIzwsplDWdbrtSyCkd8o2hM9qELSFKjua22C3A3%2BP6xTEl6Ar6WoTrt7h8KWZcv6dd3S70pJVB5ZpxAOvVKJSK58L7Tc4kvWtW07s5W1UiIV6Sp%2B0KIwxkZ6uBjR5O3TiS6Sp7zCpa5PkIRsEC4La&X-Amz-Signature=b37496a1cb04dda818780350046fe58bfc7be8c0e6098e28ef594dd7fa67b13c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UCQ3HS7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoH%2B3CITDH6MjrhOM%2BY946hogZZoni1eJQcrshI1pCaQIhAIqNquyzBcXvkODQzo%2BPjBrrfqXPuCrvl5GVayI1CUJgKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjpeiGGuXjJu80cL4q3ANI3VmxKmmsH73rL18KkQ5CPuaNIIgVQtxUeTNGWxY8sFdShuysaYggkMBa4cC1wTSIsUzRWnR6GeDgMTmE6PEuad25O4VuFPKYDJGbwn1ys8FKJy%2Fi18499vdrUR4Rc9I23c0FKJX7fZqSFrnJgSqW3vGCt5rTRtKkCxcAD75enCdknOc2a%2FmD1LCESdYR07MFCAScwSSEeJjBjHM07D7i%2FQaV4HNTCAqW2pH02tbPzq87GmOcTCEmCcvXmbu6MaUnP240UURhyI80iQwzmLmL4o5SX4ax%2FACNZgTxJOhlQrq76Y3EACWQIsGAFh%2FN1A90hBDv6l%2B45PigyKpvkYb9jzPESgldis0SNhs6pxP%2BmCnfs1j%2BHD8yuJF%2BlN94pFyTNFtVTfNhw93UAhdXlp1%2BpUVEjn1wW3GpP2ifOn%2Fww5u7qGIpDpfV1Y3%2B%2BSi8FM7Pir2Qzy%2FSiYJ6yLYvf6WMMBMOCKSFXk%2FiZXpRyY1i7VrJ2pa3JCKDO5NwnxS0SPMlS%2B6%2Br5lZQkSCCGvRVTnZNrZR2iyqz07gUqaIf0fCUDPnCk17kD8YJbslLHv1shu9PKIY1R14hx8BWHCbH581aDd4x1U5eqzWyqf4r026FtItDUPjDaUkOKGg8DCnpPe8BjqkAdpBC726%2FbKz5FtCaOFRpD0W83dJp7gi4i46BOdu6GodT%2BTbCI0Mn3kZPliPCa10vypRYfD4jHYY4EKkf1EcwHKoqiTO%2FZMa1sSrxm1BW%2FEmbcZVLbCupSCpiI3aZpJ4zVF5o9nEktJOhl8m3%2BlvNIUSsafAptuCKpnU5Pvxb0n9Ef%2FVuieRW4fyfhKXd4Fqyyw2sF0igItLEbOlMMTwzScJ8Zan&X-Amz-Signature=bafa239cb4bf1143f7b150e7ec6be5993b8acb96194e8ffbfdcea8c73f6e6b1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UCQ3HS7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoH%2B3CITDH6MjrhOM%2BY946hogZZoni1eJQcrshI1pCaQIhAIqNquyzBcXvkODQzo%2BPjBrrfqXPuCrvl5GVayI1CUJgKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjpeiGGuXjJu80cL4q3ANI3VmxKmmsH73rL18KkQ5CPuaNIIgVQtxUeTNGWxY8sFdShuysaYggkMBa4cC1wTSIsUzRWnR6GeDgMTmE6PEuad25O4VuFPKYDJGbwn1ys8FKJy%2Fi18499vdrUR4Rc9I23c0FKJX7fZqSFrnJgSqW3vGCt5rTRtKkCxcAD75enCdknOc2a%2FmD1LCESdYR07MFCAScwSSEeJjBjHM07D7i%2FQaV4HNTCAqW2pH02tbPzq87GmOcTCEmCcvXmbu6MaUnP240UURhyI80iQwzmLmL4o5SX4ax%2FACNZgTxJOhlQrq76Y3EACWQIsGAFh%2FN1A90hBDv6l%2B45PigyKpvkYb9jzPESgldis0SNhs6pxP%2BmCnfs1j%2BHD8yuJF%2BlN94pFyTNFtVTfNhw93UAhdXlp1%2BpUVEjn1wW3GpP2ifOn%2Fww5u7qGIpDpfV1Y3%2B%2BSi8FM7Pir2Qzy%2FSiYJ6yLYvf6WMMBMOCKSFXk%2FiZXpRyY1i7VrJ2pa3JCKDO5NwnxS0SPMlS%2B6%2Br5lZQkSCCGvRVTnZNrZR2iyqz07gUqaIf0fCUDPnCk17kD8YJbslLHv1shu9PKIY1R14hx8BWHCbH581aDd4x1U5eqzWyqf4r026FtItDUPjDaUkOKGg8DCnpPe8BjqkAdpBC726%2FbKz5FtCaOFRpD0W83dJp7gi4i46BOdu6GodT%2BTbCI0Mn3kZPliPCa10vypRYfD4jHYY4EKkf1EcwHKoqiTO%2FZMa1sSrxm1BW%2FEmbcZVLbCupSCpiI3aZpJ4zVF5o9nEktJOhl8m3%2BlvNIUSsafAptuCKpnU5Pvxb0n9Ef%2FVuieRW4fyfhKXd4Fqyyw2sF0igItLEbOlMMTwzScJ8Zan&X-Amz-Signature=be2856f6aaa2c3d5fd8b76d73155d7e6e5fa77b63655fbb16563b2b76d16865a&X-Amz-SignedHeaders=host&x-id=GetObject)
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