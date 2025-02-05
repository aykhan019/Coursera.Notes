

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LKLRXSP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIGeImVIjrX5w1ZONB1mQ40ZDBcLusyz71usbfSwTMCvFAiBf6i49EjmDIfUlgpehBVR27VFZ%2BHV%2B0DSXXwAnxKoN%2FSr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMTzXEQqaIek6E4y0TKtwD8bqOEMhlG73MnBP%2B2A5%2B8OaIzBbvdCrEiFld25YXCbM7b6sjAO9cFBHXxgO2okXgs3fqmOLLv1f72cXthanjEUeeSvsT4ne0Y8RbjAgFEOtvCmW7xgo13Fx8T9%2FQPwceMl49iVCMhJTLB5TvDaUTkASTAYTc9p6INqUB497w%2BPkIRnJxaD57EGvhZEVY32BR1C%2BwiS%2BCjyGOBc5KXuD03yk3xjOMLUkWZoGcazAD%2BjjEMuyxzdJfo%2B6a%2BHHxtTLH3YOEMMcSv2jB%2BG2dgQFn%2BZiVxs7D9X1QBLcOrr22PzDIpV8JtJT80LlADaDj2Rz3eI2T2XONQS8BbwhRjW5%2BH%2BYTGrkynog8TjYG%2BfucyWbxoGoWSCQeT9H4IXG%2ByzB9nr4GZZJFrGHIGtRhBBrjmdAH%2Fatz0SVdeJwK%2BR8LYboYVUkFmNLX4%2FE2NMGqH2%2FQqH4Dg0Q%2FF3bIpExdhWYEAG1Q09ftcMq4yMkdkDT7wnj2XqCawsDciqGTbdYPRd5%2BrxrIjZLp239h1shCy42tHmhtphj3GMtFpRb423XXaPQl9s9anIZXgoUpZkeqRYIamhjeIoEYTroWFP%2F%2F4Ke6tB8aYJJLK%2B7gkbS%2BfgKsjADTcr0mfLg26ZL6sK8w%2F9WPvQY6pgHhfzq28X2XjWamNA27DPfTmkq47sisOfsSL6kFiShOWFy753caxP96cC6g3G1XLr%2FdsdqIcVWKRSCKIdwnCv15nlEGPp3t6hEYloW2bznJCRha3O5F1elfUh67QakGQ7ZNPy%2FePVyRc1DFloRP4vlk44Bvcj3B5K3AlelG%2FHGHVEsTJ%2BYaERwRiRNoltQyoPoYVvQdC6%2F09OFXO%2BgexPja11Oo%2F83Z&X-Amz-Signature=646fa84ef1f707aec988609299038194c5e55759f41032daac3edb93f12e163e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5JMP5EP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQDVmtaEZJPF7YpvoYQS5CkO3fxaPjAfYOzzEfeVBdZOwwIhANqCx2uz6jWgmdnbGgAWTdNnh2VaQ5c1bfEG%2FaJ%2BNzCMKv8DCFAQABoMNjM3NDIzMTgzODA1IgzJPOMgOpWpiAIOMPgq3AMD7IlB%2BZd76Xw26Q972yCCJmI9ZWwpROnAa%2BCv1wo8x%2Fxuz6oqR9PQe2mZ6X6uPK6NROrC%2BKG4fIrCDG3ll%2Fw%2FPmijdP%2Ft9nuhrS7nARyZYYpazwUTYFFrWoV8w%2BCp9bkj2zlsEKjmf%2BK43RoUnOv017svPkVP6BtWWXfe1dgqFpXcm9gICACXtVC9U8WQiq4MI85Dn2Wr%2BNalrxY7d%2B08l9GI4VnIoVE%2FZF2aYSe9XpVXAn%2BhAl29EaV0kHbp8prhZram7pqy8TTC%2BSkYPC6g6mkUl55uGYf%2F%2FRbS%2FrR13jdGG%2BCpMsako2bEHBgOQYstVo5qLSvdB13ORP5NnrCuwHM0tNTTqh9%2Bn7ysJmJ91xWNoEVzXoZwftBO1%2Bl%2BH7N1ky9Kxz3UmAOL3GhhHaD%2BlsaVqnaPLJU29gRtWFkdpLqfmOtr3Cgns%2B1%2FJsr230n8vzTqbAUkzmlXmLZehLpScsvd%2BYWqBplq73r9kevmhehnjSVm0lTnY6D6vKlwi0QZPfwftH0oYVkDktoCVHURMnVK8f4%2Btup7zATqOfWB31ydor1KcN2DmYXcsG2IEDjhU4YlvlFrUjoDVybtSjaugmQppS%2FqL%2F89FAGpxWKg5YtgF9g4bGiaaigqLjCz3I%2B9BjqkAU4sgm%2BtYpq5oQMuJtXnr71Q7b8hVoONiBDUCGGJhVrSnm60iW1ASHYzgnnnfLkQt03onuZEfiyXW4XjEff4mGa4YCyxmilmjTAjwy6o4rZJ3rhnYWaTmxtD5i9pAK2DqFH%2B1JRheUQDGKquVLEO28YEwaiguX49MPTrkVivx7eS8OA%2FZXpVnQAT2xBp%2Bqs7fC6tnwOpShh0cAXF8jDNKwYaszhz&X-Amz-Signature=abe033b1df94b5af984c87ab658a04b8fdbe2e56ece1d1fb18c2f825267d6a69&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SPAPQR6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQCk%2FT4jOjDPk9kB%2B2tH%2FOp%2FQ%2FQecMkwQDtp8h39wSvvSwIhAPvi4dRV%2F0yq%2FF%2BHZvFlKXzmfqPJBeBUIdLLgXLXwGyDKv8DCFAQABoMNjM3NDIzMTgzODA1IgzwtQm3h3N411RAeQgq3AP%2FEl00F679rpW8KU1nc3CK2ZXZt3d3Z6A%2BV8pBHQjdrHsy%2BddzUoE6Tt%2BbKOlT%2B2n9HLT0AGiCZ0zIyOa6beJed9d7w%2BEJs2b1n4i82S4fQAT60IVykKGisYDn%2BIq68tJl1SotU27Yeger7bJQI8LdKWWsgFktOQAAwhfgTmMgI5O1tg3onWuIGNf8ThE92CoKOzVdd3iXOMc1koIT%2FauknqgveA%2B3wLKPctLhJ8JRWaryr3dfSnkcdgkqFA8r%2F2jDfYQP0C92yMP6%2Buf60p%2BJy%2Fi2KJ5Rpg4Khm2f%2FOIELbIoEfKk8hoaMQj3tXSEyupjglLnRFjyj%2FGFlu6eo4BAdfnXTaVorYmRNQpXh7ekfruJ%2BwI6ICpt6Gr1ghzZx2J4xlrIrpNZMHAnNpqYdW8wTjQ5ZQ2w8w7R8KV52ay%2F5r4yvtaP%2BFuVSSHH09SjaQ7B%2FRQoGr3xcHtnvZvEyWNm2M9r8wHbT%2FaQas9wXD4ejRSjm%2Bl7XFe72OjSRryb%2FEYT%2BkMiiR5rmm%2Ffa6%2FPzsYQz%2FLOcHQnHW8bWcOtVRrEM19d96aIzV%2FY847CgEpKsNggKDwS2iAN8dnAtRjZ6GoL%2BHC1pJ08EYq0m%2FnWFlCiWysW5DTssT1ZX2A6NjDG2I%2B9BjqkAUwg8F5VXVvHK0jyTNjfT9I1H0kt%2FBoAKSsTeva%2FPZqnb3Nmj4%2BcmsyqvUaSm9RT%2Byw418SgKeFa7f9iHwlmgQgoqSBERKdmcxg3VFOOBgrWX3x2I59LOAEz%2BHbM%2F4Ffuxw8WNsvfBFGgeLEw3GM8fJVBXwToUZ9bWd0dyxn1ZhT5GKhVf8oAIDvEka1FTSOfcuTXJQXC5J5gqNdxvlrHdHeuoTD&X-Amz-Signature=33297a85502e29c6d3efbdc5e518fa3a195314f21e583aeca48e0dbf292ac736&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBJCMSMD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD7amKvjQeLdqoYOfnjSXpuEXq3iVIsw13JEe%2Bn5cKZxQIgMjrDq5Bdk4UVx4HXpQT04tHUm9hEmcHBu55hiz2ZP9Aq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBO1dpcv6LP90ZrUDSrcA%2FvIdIciojaHDAFeG%2FLImIRq9IJvaSpTt1TWVaWE2TORXRL3Ko%2B%2BcR5pNfZOE8sqoefZgzNhPcpX%2FIYOmeTVWaWBlgjH%2BTddgrCuEY7RpTcOQ3rxhg0qh3yteG7D9X%2BI2f1iE9Sfn1cPVT7WNEbcCDG7ebzR33R7b0f7GKZh092E8bNvHDgrnXO9xdtBewH7TTeJcy3pDey0PjeBO4P62n74CtyQbXHcWIxqPMYpoN2RSl3EwQzgaNQr62eqADfN%2F1SS%2FGv9CkX6E9Y6ds77QhYYvFd08dJDV3skDMHeKNHgTM6ByX9ZEAY9a1tusxoaGLcgMcIQ5BXnZK8oFuuJQLrvhmkp5hKebi1pxREH8mvj67eBq2sXTm8HQloIYgLk5IhkRH8CLlSDD%2BtAl7n5qORDdIb%2BZOHz01QJOWY08%2BoX1besljgYfGRhFGN6ZGHBv6Lf2hFKc3CUPoUmK87gKkJCTX%2Fsmny%2FvdQ6%2B8mlx2u0q6lGnsRWL7d%2BosUXHtoZZ1UIPn7xDKKDsI%2B8DnokBnX0xvCIaWeu%2B%2BhevSZfljYfo1aE4KjrvIliZBLBtEfr6UUbQT3aIGUyYSt6XgeYUlxKbBSHET%2F5Re0M7epiMMoM2ek%2B2xfPRzs3hCkbMJ67jr0GOqUB4tmxVlKS1yLoFM67q36Et%2F3g0MHwY3B84%2BSdl%2FWaD7Ru%2B4JqdjUeY2DZMiMjRPGWmFEgTaUmNN6bSoUNJGI0jRZCe6CvBYZEb4awUnc%2BjFPG7P2tg4POEqr829JgH6L%2B64Yh5DwjYRe81aQ1fBgaRBtSxkEhL%2BPau3X2gfntC5%2BUR9pbwumewmbLR2WHGIgh6WA12H1H5zzDECZDae1MUBIeTHSX&X-Amz-Signature=6ac39f787847a09f701fbbb6111b0c752022de8a84348a8d94e9358c1dab04ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLJDEBW7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIQCMX0UqfOoH57PQgzpF8CWCeEd28%2Fh%2FBw%2Bv1zZCc1A7igIgFMznS%2B8McZiS51%2BHV4K1mpj%2FVFjXlIPALfpIGg0Zh4Eq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDLciP5PxKkFcW4toOCrcA2FIL5htsIwsZ4yNg7Arf4CS62PoEQXsMJ5efqb6VWn2cg26Av1Azwtt3PyUVaEtzRTPSFsKpO1romA3VNCkUljvmXQBOTQE0BQ7UCgxZKdp5bnm6Ebjr%2BBK9%2BX2duFpcuqFzakypr7RrvkDWcN3lyiaH1FS%2FIdEGi%2FMa9PQH34ZAueDA8VbnC%2BcjOwOvjlRX9C4BVJtDj%2Bz53KMawrc7Keckk%2BmcbVZH6l%2BbqhVgxRna%2BqP8y45W6MI9p9ztMYeEy45AEWgdnYq%2FokVDwK1DoXrLP%2FxmUQEqh2vKaH4n%2BLmq%2B1%2BuAwstxTWuu3b6ilhtoskEDqyPIajRn8%2BtC4KyZ9kbpgsRiZ5%2F2tzhykFQDfOB7yZj%2FA6H%2F8UWaJde06vTviyjIQuRbHll8jXJk6g7OiEam84b9BBOvokU57mekKtkE8l6jPKsa8mCQSz7ozjNNSpaiJvdddVWsC5pBq8pYfOX8C2BB%2Fkpw2H0f%2BIUO7Cjeyc5PPh2EXygLm4NHOT6%2FaXMvAfH8g8NyneJUEUMcl4THlAULP4sFHLYGDYZncKqVTNVrADt5biS4VRrsnX9VjMUsNjMDyIwFACkldpV6g%2F010W71t6ZEBdXu0PH0HkGH1FWurieUq%2B3A3KMKTfj70GOqUBn7vdULLAwcc1nMvdec0aXLLGPUbUIGgfwUTekRDoCHmkzNm1JO5KiTfnehYmruiY1evgGFGh%2B8wg%2FruDt6GO4Jx0%2Fh%2Fp01jQ3j1dWR6cOuh9f5Iu7nmmTCApeUr2Y22neUpA%2B4O8iOrzPT7Kguz4biclLF85bx4SCBFAKRkkp3pl98RVjvH55H3Q4zXZJzMPpPcfvrFKoFJwhvNjCPv7xYhHAXCa&X-Amz-Signature=220dba8970c33acabdc4b2e32aec830cc869f4dcd19ccd82396d9832f8fe24f6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645ESS3TD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIAfWGjFfxan9fdZgeuJLQXGdFHknwBaHw7VuHFV98vqdAiBV3ScDCGdKA9kHcbKkVRDYJsK%2FbdCJL4bPfk0ytUB%2FNyr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIM1J4Ospa70oNkhryaKtwDfz8JA73V5iuVgDoavjYLpZvO0bme%2FIsk6FjonaN44iVnNGK9DffPhrvv1ZPYRtVUKAYVQ4yI5xYwotwCXiPheHpubBEiqCgqNHW88eydaWy0RNJ92I0mKp4BVHZRUg2UouRYipB8M5QdUO8yTVzC%2Be2kNn4kyKzgUF9ALhRRK6s%2BNGCVLSzJy2ZR0dPvCSumSiZCDBKyuOhnPfHIa1zidqsvNG1q%2Fr%2FbvZoMvZG67ZKJNUmSK0%2B4CvFPBcLpF6m4SNBqjDEGYsUDZs9T9tAFxrNhxGmDtrYc3q4OiFZ40cj8NRFW8h3bjk7005hQzu%2FwG0F64RBB832%2FxJOWkVTFKBoR4uCtcmjOOHAIkGOmln1NRXW7dSPOmTFlwVCsZDYw6ZUir1ECCcNP85a3fq%2F90U1nz3%2BPMjnB1KZhlmSlpsybhOIlQZOX9oDd4gLI8MGO%2F8%2Bg7upIPtnaizT2OXrABwlMYK4%2BVDeJ9842JDzYpdZQKZ8LxyqQ3IUIrrhjTEwYAsbhMWpnzPYtiUGoIvqTZRYSMdBX%2BQxVihU5zbx9MFMoTwRrrZr386Lve%2BQKaPyTbrtnJaukod3PDINV8Y3uNPTM05MibaEQH0YEs%2BdLn9xdcl72fNJnNti7HlEwldSPvQY6pgFw%2F2GC%2B2Yl1l8pcfAiNmdBSDmHZwmZgqJdg8jYYxJAgXOmYSlsOInfs5ceon8IojXR0ne2CkoZf6tIzw%2BBIuEGGOMiEq95Y1mvp1htarIi0yCCnu%2FZsgpouE22kgD%2Fk%2FARfbKYRedTFUDPNYNXov3bPYaAARaIqnQ12apiRsHqao71hf%2B8bOhV8o1cFlIuMPBui%2BBpYbJ4GJN9APhPR%2B%2FsG5oSoWDq&X-Amz-Signature=f42c82bfb7ecee35962edb7f8b7906be39793db92d488ffb145075d739b5b6bd&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LBVBM2O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIEHyg2qBCMYzVcDhtPrQ%2FqytBDTHIq7hdyZyYzckRwsuAiAkyu%2Fjxl2WaqWqxfVcYZFSxWNV2o7ttsKglYD37sWx8Cr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMgD8T71CFCpS%2F36P1KtwDs3Yu8VEQAhk1P7OFTI5S8xCGeUDN6abzJ%2B8Rd1AxsXsqpG4p52Ro8kWO%2FfiZwjnOhvF5rPYIJcsG7m2QuAXZ1oiq%2FXkxg6IZVtFgecK2hp0yTgWnPi6BazAiL%2BfmJBWdEmxoCF6v0Vs9iSE32Fp89hcFOqHAd6kK8PetYgsCURjWgHPv2M9QkWW5fKuakMy6eMfNhbXrmXBvcm2J5o4PNX5qepxQWhxbonZSXz5HgsxxQa%2Bdc%2FM6qWUDjfCITUGfdCsGCXBv%2FG%2F2MAuNMUTm1QdcEgEBu%2BUaG5KWgOeRnvXX2Q8wh8jcwb4mV%2F15eMkPr7lkdssiif50SbsiopfscbgDB46iSI5%2FF2SzFZl3oSl7f0017ky243JDjA8YHdbz12plIfWhvSX0aTcz5w%2FJl%2B5J%2B0Y99CzHFWiVrufYJ1tth0aUi759oTbWWUVO09eb%2Bx8EbweOX%2BFG0l5rE06o9YkdENLnnOGBNgOV07SBQcA1b%2FVtz6j1skMe4UEfqxYJ9fSHBpuosjEVw%2F1nSKmuCWCIiVcTRF9TCKaii9gQ8Y%2BPeTJg%2BWtNfQ%2BbAiZTmPKR%2Fjfc4k9dgyNSAr60MXd%2BwSDmrJV0%2Bo6hPgNJWO4MF%2Fb0PUVFtged0LHji0QwgtWPvQY6pgH7zF5364TOi9GG7LjOAmyY3mk%2FYCqI2AbQ2jINhIF8dMy0oYeBKzVab4hB6Z1GexrbrSx3RlckHh8hTU40kJffOkN3RTxzknjVoQ5NTzDcHLzaBX4QXqGaAo%2BkjC4iZYba3g3ojvKU3Pd1UBYLwX0cHGOPN5FWb7y1yKazFBxsuVlgBSSc37D6sLgCdfbcx%2FS8Df72kwlEaEntH4DgSmVQ%2FuXBwRMX&X-Amz-Signature=07b0772fce52d334cb05ab9d833b99574ca7cae42e21214b42508fe9d5ccc5a0&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S26Z2TOM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIQDrJo%2FyzQM9374Zh%2B0k2FGmntwfF5u1gHYyhm5et4m7lQIgV5y3NeVm8POcK839VkcLCb0sWUT6U1nIiwzHmW%2BbHtgq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDKVZFPmwU4YTNsqe1yrcA%2Fs6e5YIT1tb0NgdK4lUmxZTROTRwui%2Fg%2Fu4POL30ne2wDuf1v6taT29f8I%2BmnwthfC70OqNYuwuKXW%2BiY2pBtwgDSQTDJznCA8z%2BTnfIVZEK8dBIdxjCcpoD41GBtUYMJNK4F2pCiDovhNHavuyyH5PhYkk%2BvZt%2BqiMKPx8alcPk7PFmO2jYWWlf0YiJjm4vyzx6FZn4Yc9qWiKowNT7CmR4rcygPi1Oot3LVQQK0lxPdk8YGSP5hL%2FDab3DLrXir%2Bay%2BoVLpnQhxArtiXKtCA3MiQda7X7DzY65y%2FNTTLnfo9TnBA%2FgJ0YlNdGKaqBfZbOQgrvLhcswSL2hik9hWCtzkqT7Qbbi1Wb1sFVFr4LynLaVqr5UAr1W8fkyeeCJ7pTaN49luPLocvesz31nN4YdF48B%2BCpnqevqKMcrv0vilmUpgTtyKtfUb7eS2C1UXD0ycpdYIH4I75crXabbkT%2B0nuQ4ch%2BF2TQKYmhRWrf%2Fsw0XbgNvMLCyKHGRMO2qsgVyRHUWOKx5N24P7%2F3MCvEy6pChO44qDCNAnODK09XcAzMrwEjgHlmkaxzkCl2HmDx4%2BXkz6lspAsDJqeWuKjxZZDEoxxa3KLGYyh8b2%2FvxqbHSLH4lKGW32RQMOPUj70GOqUB3t0yedB4FVhE%2B6sjuCHpcCxHjC%2FuKWx%2BVKQQMF55EI%2BzGAfYgpQmmjfYzaOzum1C%2BSwU03aRBbLcgF0MODaMjRIx1QupX5SxBohRWQaGGuh%2BlSnl96CA1%2BbqORsD4iy%2BF3JQ76%2BBqqBR7%2BbqcJH6sG5tRJFueKC4M%2F3kxbQdB3o%2F1fhDdh1zwRBBfnqf5MAWPMzVNLmTU2MyEmlr%2BzZqpFZsIULH&X-Amz-Signature=30f241ea9284b2d6b9afef737008791e05920cbc1da0945ecf8954369033ca97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLJDEBW7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIQCMX0UqfOoH57PQgzpF8CWCeEd28%2Fh%2FBw%2Bv1zZCc1A7igIgFMznS%2B8McZiS51%2BHV4K1mpj%2FVFjXlIPALfpIGg0Zh4Eq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDLciP5PxKkFcW4toOCrcA2FIL5htsIwsZ4yNg7Arf4CS62PoEQXsMJ5efqb6VWn2cg26Av1Azwtt3PyUVaEtzRTPSFsKpO1romA3VNCkUljvmXQBOTQE0BQ7UCgxZKdp5bnm6Ebjr%2BBK9%2BX2duFpcuqFzakypr7RrvkDWcN3lyiaH1FS%2FIdEGi%2FMa9PQH34ZAueDA8VbnC%2BcjOwOvjlRX9C4BVJtDj%2Bz53KMawrc7Keckk%2BmcbVZH6l%2BbqhVgxRna%2BqP8y45W6MI9p9ztMYeEy45AEWgdnYq%2FokVDwK1DoXrLP%2FxmUQEqh2vKaH4n%2BLmq%2B1%2BuAwstxTWuu3b6ilhtoskEDqyPIajRn8%2BtC4KyZ9kbpgsRiZ5%2F2tzhykFQDfOB7yZj%2FA6H%2F8UWaJde06vTviyjIQuRbHll8jXJk6g7OiEam84b9BBOvokU57mekKtkE8l6jPKsa8mCQSz7ozjNNSpaiJvdddVWsC5pBq8pYfOX8C2BB%2Fkpw2H0f%2BIUO7Cjeyc5PPh2EXygLm4NHOT6%2FaXMvAfH8g8NyneJUEUMcl4THlAULP4sFHLYGDYZncKqVTNVrADt5biS4VRrsnX9VjMUsNjMDyIwFACkldpV6g%2F010W71t6ZEBdXu0PH0HkGH1FWurieUq%2B3A3KMKTfj70GOqUBn7vdULLAwcc1nMvdec0aXLLGPUbUIGgfwUTekRDoCHmkzNm1JO5KiTfnehYmruiY1evgGFGh%2B8wg%2FruDt6GO4Jx0%2Fh%2Fp01jQ3j1dWR6cOuh9f5Iu7nmmTCApeUr2Y22neUpA%2B4O8iOrzPT7Kguz4biclLF85bx4SCBFAKRkkp3pl98RVjvH55H3Q4zXZJzMPpPcfvrFKoFJwhvNjCPv7xYhHAXCa&X-Amz-Signature=a93d81bf09dd27a091b0a5bbfd9fc024cbd87ffed1f685c5dd9bbb393c9ffc35&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YT53J5Y5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJFMEMCH3jb2uIVpPvBuPacH5tqQUc8ZnW8zVpjA%2BkHF%2FmHQ%2FQCIFspPBPzwWFTUYiM6tBJnC0sA6YFS7nNd4d8l7eMg9PgKv8DCFAQABoMNjM3NDIzMTgzODA1IgxwnvftYq7DifSMVrcq3APHGbmYeKnu6Ynug%2BkOo26rwrw6DngfiaX6Tv02Y5pWZ0DVHb%2Bvz8jGmJxMolH4Aus%2FL0M14kVN5U7xYUCX5Y27PBeyGbU%2B6CVgvF5AhqQFol8LbmoLFcy4kWz3%2B3kBHK1HlLCMEBNe6lc1Mfoiee8X0wyLIzKrkPhAAo8b9OMQGGqvzjMN4H%2FBhkLCBVR9m5GV8DS0ORxv8lB2nV3HyxVpkQWFi830NDz%2FXdcB1S5QH927Dbb7Ds%2Bu7iAyTfcTQNuGD5U7Wp8YA5tN%2F%2FMncj8VNfhS7ROD1nGWGRec7val8NFtcotK28FVWwx8gyP2JhzHSPepJco8lPuDAx%2FR1qTEXPUR7cID%2FvXPuMrqGmdw2sO2Sgv1D6vCz8MT7D44sc%2FIL14Iur528k7YfDO0KE3FU4TiciJ9hLHS4IgsOiQdOgVKoV0by70CkbmJygP%2BYfZlFLFtnxRHfdDiADXbir7A0z41gHhx5a3PM8g1mosc5633P5S1ojYbk8GsBKJb2MvIJm4n%2BxIf8obyNCgV9phUkQv%2BfyiY1t1DQdDeHDa4w%2BVdrLxXOus%2BRECv4yRcuQ2smYlpHfZuZGWpZM80N81B1HQS%2B7CDbC9Wcte%2Bh8gzbYDGWbkZYHbJDB%2BkKDDp2Y%2B9BjqnAfzpaUv1WHYDqkUTrCcLLfV1AMLrt9KcIBVwgn476LKBpsqCw1WR7GRFCxz3ioi3fY8FPzsIZGxYAAhUpsc2q4RuI4q%2BDD2KfdVyLWjfihEeVErln%2BZCPxqPqMXq2uHrlZXwUjTnM%2B%2Bp1b6Pfmfadv0wQOzNPPetkDLCMqUpSYJ8e%2FzYECIJu2AqdNeRTkjXu9%2BxsE3TVRWv8f4%2FHzLhpbo98X%2BHI%2F6s&X-Amz-Signature=72b2db0d4f3765f12b960ed68cb2d8d8b9f3288c553185b7d98359f35d073ecb&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YT53J5Y5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJFMEMCH3jb2uIVpPvBuPacH5tqQUc8ZnW8zVpjA%2BkHF%2FmHQ%2FQCIFspPBPzwWFTUYiM6tBJnC0sA6YFS7nNd4d8l7eMg9PgKv8DCFAQABoMNjM3NDIzMTgzODA1IgxwnvftYq7DifSMVrcq3APHGbmYeKnu6Ynug%2BkOo26rwrw6DngfiaX6Tv02Y5pWZ0DVHb%2Bvz8jGmJxMolH4Aus%2FL0M14kVN5U7xYUCX5Y27PBeyGbU%2B6CVgvF5AhqQFol8LbmoLFcy4kWz3%2B3kBHK1HlLCMEBNe6lc1Mfoiee8X0wyLIzKrkPhAAo8b9OMQGGqvzjMN4H%2FBhkLCBVR9m5GV8DS0ORxv8lB2nV3HyxVpkQWFi830NDz%2FXdcB1S5QH927Dbb7Ds%2Bu7iAyTfcTQNuGD5U7Wp8YA5tN%2F%2FMncj8VNfhS7ROD1nGWGRec7val8NFtcotK28FVWwx8gyP2JhzHSPepJco8lPuDAx%2FR1qTEXPUR7cID%2FvXPuMrqGmdw2sO2Sgv1D6vCz8MT7D44sc%2FIL14Iur528k7YfDO0KE3FU4TiciJ9hLHS4IgsOiQdOgVKoV0by70CkbmJygP%2BYfZlFLFtnxRHfdDiADXbir7A0z41gHhx5a3PM8g1mosc5633P5S1ojYbk8GsBKJb2MvIJm4n%2BxIf8obyNCgV9phUkQv%2BfyiY1t1DQdDeHDa4w%2BVdrLxXOus%2BRECv4yRcuQ2smYlpHfZuZGWpZM80N81B1HQS%2B7CDbC9Wcte%2Bh8gzbYDGWbkZYHbJDB%2BkKDDp2Y%2B9BjqnAfzpaUv1WHYDqkUTrCcLLfV1AMLrt9KcIBVwgn476LKBpsqCw1WR7GRFCxz3ioi3fY8FPzsIZGxYAAhUpsc2q4RuI4q%2BDD2KfdVyLWjfihEeVErln%2BZCPxqPqMXq2uHrlZXwUjTnM%2B%2Bp1b6Pfmfadv0wQOzNPPetkDLCMqUpSYJ8e%2FzYECIJu2AqdNeRTkjXu9%2BxsE3TVRWv8f4%2FHzLhpbo98X%2BHI%2F6s&X-Amz-Signature=dddfc1c25ba581c3e0631926cae4cff41ad8120ae06b1341877bedfe1388208d&X-Amz-SignedHeaders=host&x-id=GetObject)
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