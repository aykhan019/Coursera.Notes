

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCNUXEG4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB2WJiAaChapkQ2MmqSWfVIgFhbZWWc%2FPoguqfV91bLcAiEAzgFkqlv%2BWuRowgYpKcgOQvx2PGOy%2FnUi2EDL%2B6M0RmEqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOwL5OQVnJZ7ks852SrcA%2FPITtqHpGF3%2BwWBVZUwYh598sQiGTZankC89R9keUHe54rErKU1P9cXsiKDDEbH7Ra911EFJc12YiMj04AtQDB3LNjmhz3jhNIQFaG1lDvQDv8BFrJzFL5mM78DNTxZqmPqN6oy9jvcNXRF94h0%2F6TNfAQei3z%2FDTTgPqcPG54%2Br%2BFiO%2FBnFDiQYQMySeAhIzmDB3rTPC3RL%2FRHas%2FqUUETBThhF10%2FB9BzDrXTDJ14EfFr5I6M0WRvEhye%2FCx%2FHfj3t%2FBFU7b%2Bqv9eDjyaD74sf%2FYCxMdeMycS10WOTofsD3dJfJ5I1A%2BkUpTpxG1ih55428l9YT1FdSh7OfDJMYrZle%2B%2F6AQM2nFTY4M7crvQqoZgXZ8TTWtOgui652RA07oZfcmeMA%2FLopXkTT4NupwgANxmSRDQBHP2ODJgeMZWfgUijB4ymvsMchaidxZ%2FcPiRi8pexYrQCEKMjUI9rKuFdVxMa8iCqd5XUPCgnvNPvAEmLf1EX2SxphDe4yoQ%2FIQ4XagkPGFzz6ec1eZhHB%2FdNPYUB4%2FNWecHQepCarCJQG0KVAZGuVH9ajUV6Zd%2FbSKZC0PKd829%2FtGdLz6GW%2FSjdZ7A18TR9ZGizz8kI0bh1Q%2Fp4T8Sz%2F5u%2BPCrMKq%2FgL0GOqUBo8UuESG%2B3PZpN7bYGcKGGR89Ii4TvzAvAOvi0hM5QhXYHseJB4l5ZgZdfuU6QgKhNWZa%2BgZa%2B3c3i3fY7BSfhyiF05GVc%2FYWWtXSyYtB2JyvJJ70%2B%2Bv1MAKM3B%2F1X4peaGd4ULymGsgabgXOse%2BhKG2Vi3jyyPgdtB5b0Z%2BBa19Tn2k9veoyBHWWdCCjqIuF05HfyDVg98byw0GWr%2F4AV9UtEe0x&X-Amz-Signature=0fa03a1118f768be3a18305b181167512ac9adb9f8cf99834bde77e8c17a1ab9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT66DBFV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEh%2BaVbDNtifDHMzUY6E1A%2FeFWagN2NxO%2F%2BkHxjl2%2FmqAiEA5mo96D1OPRRAWF6AhXcXhG5remILM%2FU3ggtw9IoCW%2B4qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNmdUesnDF1iZIge3SrcA2cCbDS0Ih9YYAlMMX6tuU%2FRzIliHdhntR%2BAql4X7UgzKZ9WSIjSiLR5jX6AC4QsI3MjBCRsNz3W6HPalGIrLOxxDhgWYgMScxPO0Q4qinQZZsQ0VwJCg9SWFiDGIfwr0ZTSpSYbzJRm%2BbiUPHbO75bfkMWgBX2X4sIyYJMAv0ytOKZbHf56analM%2B6huiZ%2FN584BU9oHU0hdjPTIjgHvlzRo5Po3QVC7bqt47E0BtkVO5qSTbCMwqIi0X29kxJJFSRgTb%2Bl%2BavwZRFdeXmmCMSF1ziDoNUgZJiZEK7HuTLLNXVpkhSJkB%2FVm7Q629Ov%2BpaV59qN6jCxy7p%2FbgyQSvSpYZr34xl7CmvddVbr5vZxQCzsvI2NujvoZXdy2YNnfQWn5IHmGf2t6C4FcHmo43XcLHnzTilKIovDJdEx5yntgPYfgfSwSCkPvW%2FgjissQnr4I9XLGx9lIQBoEwy3yPzGjD%2Bw1QzzD44qHPlz1hBQQigzlDUOpuvxDVNjODq7bJonjc21gtzlovBkawhBQvhQCLZ1%2FsgpPpdraa6o2sVG6v41k7rG8WrKexv49rzny4a5TrYRPOCUEAw7VakkY7JWYKo1J1gxdKnj3Gm3Ntgrlu4lz7s9KtTF7oVEMLzAgL0GOqUBtQhxEl7ihYhzFGIcebYZy4twXyTgybZpqZphQuvqndATqehhW4iGTTo1f%2Fm9REFiWYlwJgtvyTtu%2BkpswzghJO6MRUiukNTDdGmkoBymO56CvgJtgbSLMc5GX3hLfTttlFdlwcrYnXkxIiStAv29l0LHFJ6CCIN%2BlWvAYBFV4NuYK6eRgi9Z1KKd9eEHo2YTFWwfAdwihHp80iXLF2D%2FdvVLE5%2Fw&X-Amz-Signature=382af840a586b07a9e179828a1f592b8c2217eeff1661874bd31b464de97b07b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EMCRWAD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEr3dAgMy42zuKO65Pd1e6vGk8mHThWhrBTNLDzlDsaGAiBsgJ1bkitymhOJEwWmwWKXqV5jZy69WKzSmaXsAJN%2FQCqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJV3j32%2FInHZhdR01KtwDUlZ7R%2BD2fjsGtLkEtxPTi8Y9qAbSRdnHPaD9ZwQ67EaSZ5qi4AyHvrdlhUL%2BRQL9zuAZ7acscGDyfyQXzGPrTOVcwUcsLdqtUF%2B1SgpHCWWvZl%2F0p6Aa83v1fTCxM924ohfUDaDWqmlZAteroj62kTQhxgYoQEbdsXvVdDxaiXfLZtXeUCKt58cXJpKKz8Is1FBlkKU4uCO%2Bud2MvCA25WuXhjbef%2Fu8Ud5eyUJfLmjeY8NYHh9305iAWqeXeaQiOYaXr7Oo9XGGyzfxpgBE4HUn%2B%2BosOQdAx8NJ56SCebdxYf7f4niBxO88oVpKCwIV9x98guupXEYrdv%2F8%2Fvd1VSdiux%2FjJCP170lmeeePlMeT%2BzNBN8WaTspF3kKjOHLZLsRkMlTlmoCD6ft7EeW2N%2FqK7%2Fj0Mhu7Kjnev%2F%2BMRVqiq9IHoLHgG9kkLYkgTru3WMG6yt9EIGTZnfubJO7IOivvr%2FbbsVOQUtHxWNa2YEBUwFSjt576zE7wU838gY9LxwncpqrwYsBNu1hNncPYTG3aGvKFfwoEbuVEFDvn0X%2FlooNQ6zQ5Qz8dxSTfoAo0t14R0f%2FXiVtDJb55R9lJbmCnLfe2zkwNkkeo09BwV31Jkb%2BTILQYEr4UcZYwrb%2BAvQY6pgHbDzL7waJ%2FMdNVqMEhAr89ypwPyKSMaKGf0cqA3HLPtuN0WGiu12%2BuocONt8qn32J4LGYQmt1HpAsmT3JZPWoHZIhRk4qwaJ%2BANOQ8CunP%2FlnOMyRpKOnxynsanvFLw9hcNrmwIvW2OHJImDS1R3YRjePoT%2ByIdWADSxfutrSIzing5K0l8GS%2BC5ZhtCcEiO8a1PH6mpCEbPY9hZNVLLEmpjzdFlD8&X-Amz-Signature=998f2211ba638755121c051fbf6e49a81c04151f04f01d56230ad802b984750c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQNMAT4G%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEd7RQ5WaqqWi1dcXuEnCd723q9%2FE89Y4bhnclKgTzqQIgIPDhvYITTQvMzmcjEwGBq3swCG74asu9sSN29%2BkKROEqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLN9M05jQyL28vWQLCrcA8n3Rh3p3IPUj3xHR0jMmsxV2T%2Fw5Y%2BlF38qgORB8RW0NCsI93p2IPCRDIPXOKkrnVFkoZhEXruj0FSGLeXyJRaFResaBVPXoE4BslB%2Bobvmtm4xC85AhEjp6qg7rRt8UP6wBs3iuwLps%2BD%2FPWeWOrovaCZe00IGafYQ329%2FyCEzw44zj0NjEX%2B0GP%2BBK15qH5Mv6Lx1f53E9iEognvUxdvOfY7gWMreV5%2FaZaMMdgxG47aJTh2FokzQl4vVfkPYOZBa%2FEtpWSQP13MGzmnSlQfwrEtAcU9DMjSs3l%2BudTZOH%2BaDhGhHYypZ%2Bsms2DyOt5yopcYVqDVMB%2BC47W4UxCTlD1kcF11moC2VAURt7Hq7J9v1q2iSY3pmDBWM1yb0hEvQeegjM86fOjxuRvjVEQKjdi%2B%2BzZJuHPqMQfuBaQwDoomWcD1soMayQcobrWsXwt29tAObLp45d6pdBbO%2F0bkguIVWwbAsBzCMzcPX5CZIuzC8I6v8z%2BeKZJQhg7TH4a0GQY6Xbl5Hwv4gwB2l5XTiM1gJs%2FGC9U3UPAu0XcnfEdM9LakSnXkUkf7ElJZGXszxvGqMfr4JEXKJq6UrJPSPjF7h4fDgFLwDWKJtGvr6CXEsb2XbEpvrsnncMKa%2FgL0GOqUBIdRVZS%2BlvFwAYFncfZauD5AGm4n08anK0oySygHMs9yu20s8hWvzUpDXJzgjC5%2BssQOyd%2BbQ91nlJQT76XCq1kxIbIE6OQ9ALMxJOLiy%2FEiopS%2Fuk6hPQKVdcCHlBViYChU0XI8wEzu%2BnQRi5ckkAE9%2Fg6UKEUPVpTlRoeO5EMIvglKWqkKHrKN7UX2p5LuCY44SFvPI2MIDE1uHMYYQgLc6RDA9&X-Amz-Signature=4322a89492cb18e66006e7365f05f8f887993253751a1a58ab3c9b692d9a83cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGGVISHD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpZkZrUYOKMdMx5zMIwwFf7sO4NZZXyDIvpc7SJobobQIhALYqMqg%2FxSPU2QPdCA963Ol3vjX36AclTY6idnZUjBzTKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwPtrEV8jacq34TfYq3APhZTs6rWrvxQRflsQsEH1V7LycVFyYIGG7FjmQADAdK4u4ioKmhTmemA9T0uBYgA7QEFn73St1X5qdsta416q3Sgv0E%2FwoCyo9go6smX6FL87t6Ibx8i9F9gz881oWTdmOotOsnlgqhBX0K9ucW0Ktptma%2BREriZ6rOoeRRytx1l05xdD%2FQalBXpxUcNAAkM1AKQbQkhCiT5unQfw%2FGsQ02Lah5U9DpKfhR2WVCDXSenVUrdaGoribA3XHP0XsiXIjm%2Bq0AecJFN24L0HbsHfs0tWDOjHs5J55xPob7KM6vy%2Fcya14LZlwk13xFNshZQ5qj2MCKjU9DkeYu%2FfokUyuIK72XuFuIRXTP6c9bRyQwXlRWxfvn22aRMlKf9m%2B9D2JsimqHMfv2Cf96RHSf53snTGy0uWfzhpgfEX1PAXp8XXZ99bRquM0IzpvNjeC9OyZyupR1uX1ctDk%2BOt2ZPVN8LOCZyduV8kNhNaIMJa2AmgFBB3tuNtMi30SPlf%2F2MqkcK5naRSpwqev6%2BpcoBHLkvmAulXOl6COyEL%2BieJSdgqNMgoVotFjK5LrS1uPEwBfW5hy14tXuKhzrXZ3QwR3Rjax6IbBc%2F6I4hOypbajaH%2FAuzCSWvddUGcSzDC7v4C9BjqkAc7f76sbhoCvqheEZW0gYJbT772ogUWehlY77e%2BEL%2BU2SWMFEn0saaPHl2XuKModGVsprIpx8cKi0LDlUF6QusCZxgBnAbNkWGS8Dvav2EsjV%2Bd5g6piBAB65T5gcjoeqNKWpM8O8%2BEpv1lDLHg%2F%2FIxWFtc%2BcCzqykPpqXrQpP%2B5CsSjMnnnq8XMS2SCUKikb1eusTpSdeN9KLgUBsMo53rTxZHy&X-Amz-Signature=00da4df35802a8cde094de1db781c63f378ba20672b707eb86c6264bbb84ba21&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667U567PEC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGqxB%2BvQfpaRxRW7iH39VBm20gWLKfoCfKeFWZ2tpQQ2AiEAzhxVtq2VF8OijAJtLAZYKbogC%2FDUbsoJ2aHzjd4S2e0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP%2BYPVgOUlWhJeDlJyrcA52zOilGDqKOLgsRRHJrz7FLiP8P2w0G6k%2F6goq%2Fcxizfbw3oKYhhtv17%2BELbTlGyykUaYUO9IHT39rOi%2B%2ByS82vSODp1xbKpjEiSlZ647b14Go8WqV6sJMhETQWid%2B2Krh1%2F7UkkwmEcH0ObGJWC4oCz0qK8F%2BiTYVwdyWRBcX0ZN1oMmh621XzzznPBiaREF9eziS9pK4wYTiAE3FQpHZzBxUtpMyoc5X8AWZUN3aGug%2B77te6JCBqRuBx686vlxHY8CMSen7mBMKAeAg8bUc9rIUFX9Jm%2FtjB42sTmiNBBJj9%2B8I5bT%2BiwZJwn5tsFWFUZHTXp8%2Bxwn9OudIKGKB9RAfWqKex8aRwYdQ0z0SvCUyp%2FAUhIMbDb%2FYsGN1wPvpPkz%2BQo4grOauXzhiOU3y2V6vpa%2FJ5FsqkIM57QlhxUK%2BmKzPNze%2FICmgDmhokdphf9zkYmyVpd6XprWc8LHIPhFhPIU%2B%2FBnv69mGqwYiEk%2FynWasbRY2hCjIaay%2BFlmmtTEYU7ZWYQtx4NOBKBCZEerYJVCZT%2FVuUONfrxl32nRvuto7Tyzmb%2BsclBKAORgOLy%2FRLmMlhHBul0CJ4Bayy08dp18jWYm4Hc4rZ4f37owzHTrvLyPLK6HulMIq%2FgL0GOqUBd5hNz36DToYl%2FnxB5CTFwBhUxE%2BYqG9%2BlNCH3Sr%2F6P3YKhp8OiTf34NI7RdvCDodCk1yvRChUCfOr3IDBk5qeRofvx3EAJjdjHDNYyv8WkFe7xgb7QxnlwFwRxOYAFsIE%2FtMcF%2Blo9mS0G5sYSPyYz1y%2Fr%2B%2BuSChesgPjAldTKMXEjZqnrGcgvFLOIZChfdfLHWaHwuqOSLDwI9AsxsAE4UmZ54p&X-Amz-Signature=15def5e325e4a990af9b25e1c5b679f31ea517565dc35e80ac3a3dfd21ab15a9&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBNVQURH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2Bs0ZLfqse6TjbR28YwcfEy8xjIfYhUKRA72ve%2Fp8KDAiBBmOZIidtI2EA9ezjVJwvGYMpYxEw2tKXLJc%2Fz00AtpyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BddbPDlQR7wjLP%2BcKtwDr1ZLxIv7%2Bcg72k8ABhckvvfBAz6EIZ7hfvEcCiafjjhV5OKkLb3nfpB0zRSLbyiYzOuZxWRCG%2BaEu4bp9d2tfCnTPazoX5mptNHvFpRIYyaNnhaHHT1fs%2F4kcpwEjveqox7npVodyK89epNBXNb9keryx97dkInyqdJMS7F%2BuaXeIvw8y0XfcMU047sBhNC%2FxN25BykZTdlJRLK1jotoCexkRIjWjCIpnDevmhjvXeaNwaGaLfkiv4R81NzA6MeJI8VjWKDp8A%2FzOblfJHmbLsICZwsNk43U3rZLpHlDGI2Zj%2FORElZ8jPvheNey6GiYB7Xo15h2zqbdr1%2Fd0P6%2FOCkM0afHtueQn%2F4wYcENBEwuXYVkk2HqTwFx0N8wCRsB4rVz%2F3ongDh7NsBzhLaQL%2BE5tMplJO51gasg3qqwJOgnFx847F1XiWnaKHMs4VJH61dWUgZoMq%2FmN%2BB0jgIJsMLdX%2BSrGOUYiHy%2BTygK8hU0PTGBvlBzzE27epoyAGycCxhTKmrKhF3SHoep939NgOK1HuN%2BDuTd2zekwdJqs6VDnTn4Iihu6G9Bn7gYzRt3TsNR8Zunm7%2BlbVp5yzNEJpuh1cnFikAnANdF8adE01oRNkh%2FjP8UhbmoTZ0w%2Fr%2BAvQY6pgGv%2F5jM1DUlN7nZjY9D%2F4ovSfj70Otf3i9zJ9%2Bjjz7KLSFPkx5wfyeNjk94VNyLW4nNO6Pnqv8BkbKZ4g9Q3ee2VmT9%2FB8Ubpl41RpkDBYhFj8HUjiS%2Bza3zAMy5nk2C5rvF2KZBqWKd%2Bf2ySqcCcfHy62duqbLv%2FSMPiWCCjD136excCQQPIf%2BgOUu4Bah9h8twh08HRnpi31koBOvFhrCuTZRCIY%2F&X-Amz-Signature=801e1751d462a1289b884397f0c6a5f3ef69516f729558097ea1ea4d9c77d276&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXYTC4U5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHSK%2BLNqj%2BGkLu09G%2FS8TYQsqD0bh4TUisuLZT7jY3hYAiEAzJ6EATuwZMWpDQ7pQZM7Mq0bkeSycysDN%2BXEnUm0bxUqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKbXCEjo2J4ToG1%2FYyrcA%2BLIOn9hlRy1bdbuNxjccPjmZONJUQTGcm5uc0p%2BUZ0r3mpoJVpk4QjoWSD%2B0g5ZZ1NHDTOVte4HZ3OfbmJBtr6qVzLc3Yl9Ieom%2Fx1QnUXWeL8P6svXmq4GIeDxf3irjbXfpHuwnbvSzxVrXyQlQrhCbsWxSazoJ0kqgQhsIkGOiSStCrfdSi26fkIN6KzV9I10uYsuO0aFUf%2F7%2FqXVHjqxhkkiHXZlPlJ9HW3%2FuoxavtaRiGttzobgFa976%2BJryHfSDPS5zkUrodcOR2tveUK2LpicqsZIZ3o8lhLA6S4GUKY1DBygTbFXwktTKtZzoVRyatfobcC%2FEEec1LZzRi9HDWx8XrmIn86RE0tT6%2BIwNgiI3PIyTdep1SiJgAlR%2FttAuewaIhIMXtua1yt1Fx4HBmmMUTDmV2E6wfXecWcx7FSs7y5GVoYxuQvCoqHtbcWu%2F6qTBQqTBDc3xOnfZYiwJNqZZkE%2Bg3EfVPoeX2WXrLRUP1LJVlIzGJd2frAuO9KV5k2I3t%2BhEvLG7xEUPN%2FZHmjgeYgAhikczeYsitpd9e0Dq%2FGSRxFVyjs0WuAaDpqXa%2B4EMy3Z3kkvcDMJg5E9Lwz6GwBX3wzRUKmY7tZFJGQpCqFf3Cs4joz4MIzAgL0GOqUBSafK4Qr%2BgkX%2BSY1fisOk8z%2FANiMwMa7E4DBrvOBzgGG%2FzjMr3Bo4AXaBosT4YEeRf%2BKLKcEw7foqlMt%2Fb6WtsujR6rlLS9vPkUk%2Bef0l4GSblgy%2FdnMwwZicP%2FvzC8IodXk0qDVh7X%2BniWoIutH06iZIbK89U%2Fe0%2BsTF9aou%2Boejf0MKHqpg0cPwvsiYgpwb6eaSY2Jb9c5oGv67Mt3xe9P%2Fv%2F%2FC&X-Amz-Signature=fd3cd0e270065ae4ec108cde366dc309813fe905ffdf6830a15caf0e646ac383&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGGVISHD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpZkZrUYOKMdMx5zMIwwFf7sO4NZZXyDIvpc7SJobobQIhALYqMqg%2FxSPU2QPdCA963Ol3vjX36AclTY6idnZUjBzTKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwPtrEV8jacq34TfYq3APhZTs6rWrvxQRflsQsEH1V7LycVFyYIGG7FjmQADAdK4u4ioKmhTmemA9T0uBYgA7QEFn73St1X5qdsta416q3Sgv0E%2FwoCyo9go6smX6FL87t6Ibx8i9F9gz881oWTdmOotOsnlgqhBX0K9ucW0Ktptma%2BREriZ6rOoeRRytx1l05xdD%2FQalBXpxUcNAAkM1AKQbQkhCiT5unQfw%2FGsQ02Lah5U9DpKfhR2WVCDXSenVUrdaGoribA3XHP0XsiXIjm%2Bq0AecJFN24L0HbsHfs0tWDOjHs5J55xPob7KM6vy%2Fcya14LZlwk13xFNshZQ5qj2MCKjU9DkeYu%2FfokUyuIK72XuFuIRXTP6c9bRyQwXlRWxfvn22aRMlKf9m%2B9D2JsimqHMfv2Cf96RHSf53snTGy0uWfzhpgfEX1PAXp8XXZ99bRquM0IzpvNjeC9OyZyupR1uX1ctDk%2BOt2ZPVN8LOCZyduV8kNhNaIMJa2AmgFBB3tuNtMi30SPlf%2F2MqkcK5naRSpwqev6%2BpcoBHLkvmAulXOl6COyEL%2BieJSdgqNMgoVotFjK5LrS1uPEwBfW5hy14tXuKhzrXZ3QwR3Rjax6IbBc%2F6I4hOypbajaH%2FAuzCSWvddUGcSzDC7v4C9BjqkAc7f76sbhoCvqheEZW0gYJbT772ogUWehlY77e%2BEL%2BU2SWMFEn0saaPHl2XuKModGVsprIpx8cKi0LDlUF6QusCZxgBnAbNkWGS8Dvav2EsjV%2Bd5g6piBAB65T5gcjoeqNKWpM8O8%2BEpv1lDLHg%2F%2FIxWFtc%2BcCzqykPpqXrQpP%2B5CsSjMnnnq8XMS2SCUKikb1eusTpSdeN9KLgUBsMo53rTxZHy&X-Amz-Signature=8336a345655d839d1e667b9bf227ff4f9f7437f016fe116c5513a44cee0b141a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVEJ5XV2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBjOx%2BOrLTSCir%2B6cxsxE8hpIW34CII0JliXyE9%2BlCA3AiEArajwAkN9YevfJzT8uWUdvKmf5ZPqd92ptUMT1gFuXrsqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFj6Ukze16osNC4wayrcA%2FBmXIKjBXwF0kv0lKLS5KbbTslrbRL35R1vLlKPBv8BBMcFJk1yaGuQA0qkaHvNKi%2FF8q3pLwj7QQkvuPIh0Lyb%2FwOiNBcF5ay%2FJdxnQoClRub5cDWcJGIIamkAtq4U%2F7uZ5tLITY1nQLlE8xzoYG50JVlxCkw1rB%2F7MPlL%2FCbzVH5Lc1%2FmHuIWGK1vPeGaPCz%2BP7y9pD2%2BvPHypW75Xmqhx7f4%2FvQUthwJHiAo%2Bla3%2BkvI2aOL7%2F8dnZ6OXpke%2Bj7NvRt%2FD35rQz2%2F%2BxKmDBwLw1%2FA6as%2B9QgBzeDBmrbq90qW6oR3Q11FW9Y02yqSDjd2p%2FIn7Ogk8cDvTmN8%2F7h2Niw12ZXHGGvaPHuK67dSnw9sY8qtbytIYeMIXEQ3Z8XE47QxrkJQNtFse1gcuLGqYnUuOK%2Fftohf4W8%2FbEPTnfRwX7mJF1rav55XGZGZlydjFLnvg%2BM3KYgsZxe3FZKTBqK4jZNY4eyBN%2FlizulxEpDdhyKqfOMWH25CPYllAYnsXCgGkx5UJpekpPeISsP7AV1dko6j0GwiY5jO8FnlBxrV5KYe1Bcc9FJtKo9kE4iObTPqiY89%2BRP53AtnWgARlPAOcksdGXegmcNuIrklQLBejcrUF4Unhpf9MJ3AgL0GOqUBUGKnXYlZfer1fXc8Bcluqq7DsuP8OpIIhtdadY8GVzPftNbwAPcA36fRXPLT2rIG8y72Vkc3j23nWr7b1RuN9sEoCpO1JrIZ1mZamQ%2BnQYqfNgq%2BiEMC%2Bx1PoUaH5Gb6QadC3JQF5omXd32xNi4Vz2YyzQ%2FElPA2tZNKvid4tUHhUtkR%2BKZCCqN7hTRCIwl0IKhi4jsrMTtY%2FDINwxLcGhRD87Ww&X-Amz-Signature=80dcd422d883d3ab354af22f7e81fc07ac0cef482239b08c492d1db8b4778816&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVEJ5XV2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBjOx%2BOrLTSCir%2B6cxsxE8hpIW34CII0JliXyE9%2BlCA3AiEArajwAkN9YevfJzT8uWUdvKmf5ZPqd92ptUMT1gFuXrsqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFj6Ukze16osNC4wayrcA%2FBmXIKjBXwF0kv0lKLS5KbbTslrbRL35R1vLlKPBv8BBMcFJk1yaGuQA0qkaHvNKi%2FF8q3pLwj7QQkvuPIh0Lyb%2FwOiNBcF5ay%2FJdxnQoClRub5cDWcJGIIamkAtq4U%2F7uZ5tLITY1nQLlE8xzoYG50JVlxCkw1rB%2F7MPlL%2FCbzVH5Lc1%2FmHuIWGK1vPeGaPCz%2BP7y9pD2%2BvPHypW75Xmqhx7f4%2FvQUthwJHiAo%2Bla3%2BkvI2aOL7%2F8dnZ6OXpke%2Bj7NvRt%2FD35rQz2%2F%2BxKmDBwLw1%2FA6as%2B9QgBzeDBmrbq90qW6oR3Q11FW9Y02yqSDjd2p%2FIn7Ogk8cDvTmN8%2F7h2Niw12ZXHGGvaPHuK67dSnw9sY8qtbytIYeMIXEQ3Z8XE47QxrkJQNtFse1gcuLGqYnUuOK%2Fftohf4W8%2FbEPTnfRwX7mJF1rav55XGZGZlydjFLnvg%2BM3KYgsZxe3FZKTBqK4jZNY4eyBN%2FlizulxEpDdhyKqfOMWH25CPYllAYnsXCgGkx5UJpekpPeISsP7AV1dko6j0GwiY5jO8FnlBxrV5KYe1Bcc9FJtKo9kE4iObTPqiY89%2BRP53AtnWgARlPAOcksdGXegmcNuIrklQLBejcrUF4Unhpf9MJ3AgL0GOqUBUGKnXYlZfer1fXc8Bcluqq7DsuP8OpIIhtdadY8GVzPftNbwAPcA36fRXPLT2rIG8y72Vkc3j23nWr7b1RuN9sEoCpO1JrIZ1mZamQ%2BnQYqfNgq%2BiEMC%2Bx1PoUaH5Gb6QadC3JQF5omXd32xNi4Vz2YyzQ%2FElPA2tZNKvid4tUHhUtkR%2BKZCCqN7hTRCIwl0IKhi4jsrMTtY%2FDINwxLcGhRD87Ww&X-Amz-Signature=5cb97a632cd4a1b2aead89f3b335e4a45f5903979449738be1a20695cf43745a&X-Amz-SignedHeaders=host&x-id=GetObject)
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