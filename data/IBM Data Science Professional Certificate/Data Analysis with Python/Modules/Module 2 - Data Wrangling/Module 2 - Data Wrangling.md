

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCRQUL4L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQD59K38CM7MqDBKmVOMx99CPx3NGAScyGuTZLilPJsGGwIhAK3ozpmZlSY6N6DHzbmFkf%2FFO9KEAQuC5jXofQZP5DfEKv8DCFoQABoMNjM3NDIzMTgzODA1IgxaECbfC72AX3Bv52gq3AP0ep%2Brjzs51TEHuYj8XLeE7zxpN9fqNvisSkNqoTAzK%2FtYIZJzYJ5%2F0IOmciHyBSkXpro0s4oR9qp7E4nO4v1YlutLH1pjmkvay7bXg9PFds6j3%2BQTPnFidV2Vr65Ag2EREc6KrCj94dESvqhqg0P4YS600TczkqeLeyw%2BF9kkHqAeYebyfjOkYXfXbYzLHAJAlGLWKxi23yng2HgoWfQP4ywPXX3i31ZMqMxGUzFYczstzp9X%2FHy4jMLMHefKf9%2FpHP%2FKW8v3p%2F8%2Fq0R7sB4Y91L4OFHITSSsBCZanvfv%2B7vhUxeBJwtjNcXC3uatAIlB6UmGO9f%2F4gCVUatrS5skZuOPIo7cD15ysLJnQypwne2JiX9OIVFnygJmS9iyYKistebij2BhN8XARiI%2BGTr5w7UPWWmOoHuJ33u6KqrI0RYXO9aFfH9yDh6kIy5t%2BxB4G4df01v7zEM7ndmwO69lWPFo%2BcduLBOTWb5rGDIDT%2BB3of2Rae07OkpToNAF3JituZ3YOZNh8LUKsjC6A9m4kgdviCfAUHL0wkuX1EB4mQPk2Th3zpRJnHbAJMQoZfvEwynx0Gw1eEANQBXD1l51fxDInTiHgRdSjNpsXu3KRcoheZkrZMdXrX%2FNzzDf65G9BjqkAeh7X8rGNkJBYzSGUGJLo0YtK2Pi8IS9%2BHKczYtZH1cbVCKM%2FXSM%2FlrvhSPUfIUshKc54uAoKl4FXigcbIqwW92kxiBd2dXi5mvcrTdG2ZsPl58DX%2BZCmMe9VEtTQFhVT83bgZOTw3lvVdYiOOElsZYYCbkg6wE7ckR4%2FFJbU5HXg3MAbIDxB2%2Bwf1pexSMNIl5SqP%2BKZ%2Ff8bp%2FKQvVEMJ7AqluD&X-Amz-Signature=83c44fb22d7c6ab6948993cf0a24c0a986269e3d36b57327b68fc8b09124e781&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QL7GS4M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIFuUwblTCkyfr1TAoX2f6oROCDvyhUdo494tE1LuEuhLAiBSm1dcTEOoNRC9FSTep4kURUGga0tfioj986iJMspCfyr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMltjDTv6txoRszjR8KtwD5B%2FsSWk6b7PJWF%2B5L3XNDYZ8aKexN%2BTYM1vgdswr6jj0ZjPrCRfkVqR0urCoXWQrx1CG8%2BPJoaR1QpRgGmC8euaBeSCIRuto6mQjCuYWWTz1Nx8rTg5aSKCf4UgDVILAj5Nox27tlofAylj0YwRqFO%2BrjTMlqeBRlcnLMV2b7m%2FnhakE%2FF%2BhHKkg302rxmcZoEs14kvPKpHyBpyB0spRHibBJ1pUWWayXTQ7DbYaLn%2FH9xAZs6cHvVdVnB%2FK0FcS1XrcfTG9HqfIL%2F7Jr2vg4MKAV%2BOBYoPt9NdEQ%2BXLTyd63DTsk8jLZE7MgSEL%2BfP4%2FKw7FW8qbirJLpkefUSiwJuJ2o7Qc50iZ3BGNy5HmJ6Y9oYquUpUnupDIBlFWFxO%2BSRkkdgfWZTaKxBHUj89a4I2z52cqTEKmOqpxL%2FD3oNiPA3XzUt0jxn4LDUXwwrWKBddvSZSNH0ezVPXoe1OIeZwLKwUDWgnt9f7ntoqX7THYiaUAdabWHETwwfdLpND4T0m%2BrrukBjkIYq2kqEqJchfizlu%2F9LfTUROzaz2IqiL3Y%2Fw8WFRcY5bnZxHYlx%2BS03GkbIxEoy2xQlHaoGJ1xzn5%2FsYN1TH9ekEjlCWb7Ubr5tORulvv1e%2FRKgw0%2BuRvQY6pgEh0dMpops647L14N4RbHtP7fxZ8DrxzV3CcJbEugOQlw6pBmsKwAKU7IzEyH6M6q8xCUSbndlYyQKV9dKAzSwuoRtw7lFgG0laVQUHfHL4G6O6mRlcRq97DNwbHATqzCnrg0gPCQjpsIhTwdnEiMlT4EwVKYQNiCz0OcdMY1N1ioIbrZc4FnfvE1voOA7tf0iOoZWglv3UwMyi0AyRGzrulUFFSYng&X-Amz-Signature=ffd8d480c8a358b4841f36c296827f28715bbb13b72122c0d9eeabd150bb80f7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633GEL3KJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQD6sUDfn4VEmj0tfBqeLdFoW7ZnYDZ4dnAm%2Fj027iKIKgIhAPiRATy2xOisRGtgchnw7d8eSG4QRLz9yVc%2BPySGNn0oKv8DCFoQABoMNjM3NDIzMTgzODA1IgzUlFBbZRw7LGDtKoYq3ANIIFPdyxjrNYel%2FneqtMnxbxwtFSxON%2BP9NjXhLEYIUWgM68Hskbt7CsET%2BSHBpyhvc7NnTC9p6k1ZbT3Q2EFuf7pGoZ1cWYTh9%2Bbb0zUSTGyKNiM4J1WjmZJ92NrDoPrzvohH1hWIRbJf3iZrBNUPOOejWGau7wEinBFBTtI8GsK4oD27RCUsnDHffqPIG8GCopVp6vEBEVhUq0KRVoNynd%2FbGMojUPQ3k0wmip0C4sCTsNqJpWcWSthigkUKzgRGhm5tPXML%2BLOY7WWlIceV4cBELdFxBRy%2BY5x1pvXyfWtUSE81Xt8n8tmsGeVQsUeiH6OXB%2Fe9V6MdWQEItvV8byMNXKrN38GUcR8bP2EJHXGdt6zMyzRpTovxvvDCtNRqfZawhv5miyl5izr6F3tWDEiTbEd6G6RRrNzked9at3F5uDHAjbteDaaOw4l%2BazOQRs%2Fper8FHjznNKsJdUEpNkhY9MeznuGHdH4IH5zhTLqfTi4tOPtn4vmwoIrGLCfkCZnLkeOEWAZuLki3GmYurGaft5ieiQwyAGZ%2BDtyrY2152qw%2F1cNZfVXm%2BbJA8C9AP7sP%2FS%2FN12IisXuiNppXQC7CfFewvh%2FhxQqxvQ0Ajs1OXQJKbXLn7Cq3CDDZ7JG9BjqkAQMnzKLIbSSYd6DXbNYTu43afL7FoiyratcyUWWlXCG9v9nxHJxUsekhxEFKHtEmwEQD0CzJeP3EjuYXO8cLZCDk22Y2rsgNMj6N28dsU0KvF2m2NHsyGA11xF7UgvKPSgHqeefaqMGafvRwnrY7hZDmP3DmGavVZBVfnBLXhxwrSnpJup3WlpIodU7MbCjXIDWTNfU8iN%2FuFqa%2BS8o7rRYkzmHs&X-Amz-Signature=df8ca63aff6caf36193133ea8288a83abaebd048c4e8d770dff0398d62d1431f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHQ6YGO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCtdvKSk2hftzb1xnginH6%2FmiTfyYWkefGKRsLo3zxZrgIgA5tPGQQzAddQdaKfzzRoFu5AyySwBRJXRJ83WDwv99gq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDI8lx%2BjIZa601yylySrcA2Hi4kdkIm%2Bj4ah4aRZ8acgUdYzwZImaH94GI8yOkde5ZU3FpV1TtM1ax843Kb9MzjBFq4cbz6x46%2BYq%2F01%2FzvP01LgKT52WDysiEgwpR5x9dnHh30q2rWFoLTd9IT7LTzdg%2FiEKgAU5CF6z2bJ5%2FxX95yPImMnzeP30qgUoKdUZgFQ0A%2F3ue1q3q3ZH3IuMcrncy2juXB%2FMe8Id6vt8622b7zVHIVPysZU%2BZhsQcKKcDKbyXzepm3Aq1URYgFUOeTsEIEbeYxBt8krA5xPf%2F27AX%2BJbZ90d9uyu56dJCgO0t7eK6WgWPpLxNBSqyw8uGJSh%2FQoUGzB1xz%2FH37xBTkL9bRJbEVeqCVwV1dpFBcRtf9PLiLvR5T8qp2qFeqVta46BmYTDN6iF3bMaauZRwthQkB5DtAfLUdkvLvAKdsQa89jMWX%2BCLuvbeHklwBiGu73JIyRRR3gtfS4BpWiTrB%2FSuwwAQ8KmfR3eW3iVfH2p%2BPAMDQ%2BB2UcBFqz6c4jygTGU4xM%2FIOkDVKNBjedG03%2FHSOxqBoiknrQlC1KTk%2Bsz8cSy2MyhZwbKIRT%2BSTcptpWN0N7d%2BqkR4IFI5dp8IuZv0NcMHVGRa3D9sSEU0QG8cjR7fRdpWOPgF7N8MIrskb0GOqUBp7vwpz9hYXIPmnMPM%2BaV28%2BEgwZbRAlOSMZ6Dg02Ds4YEX86IvOpk92yFnDITuUyouUs6DIawowV7dddSe7DZWqIPDfm1jflfHz6ePbb9iCCdsnA8ov8hRFqA5TupoS%2F1Myhsmk%2B4kkq7%2BRBwol%2BGFE1H5roHEzaoVp%2BGTRakBbfT2diULpTfhWAX8XhHRIfKFdb61YdLusPSVTlTmpee%2BJ8lgRN&X-Amz-Signature=e2bfbcdf04d19da264af7c4ed13719faa0ea39aa3f67bf485043fe5c7e02dd53&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGHOSWLS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDYvV0909bmy2umHo4qUFQUtusPD1m%2B8AYByhb4gS8tgwIhAKyB4CxePwgI4xlX6j2XnwRHLxqEthOEcPOWxRTqa9r0Kv8DCFoQABoMNjM3NDIzMTgzODA1IgzRwgIGWb%2FywT7e%2F7Qq3AMQ3%2FJZj3p5UJt0DkcsezQfbK0MR3MBljbCCTo5LT7fGL5OeyLkCWQtAawHrGmAdXqIRaTwHCOALA5dPaVnLKknjrWEp%2FEveSEeVU%2BRcaH83j8ECztVU7nNMjKX%2FWjxobXM4JCsMJwVBgW%2B2ItJI0vwV8jpIeS7u9bjAEWypOrriKtVlJ5n2ViFk1IP6N7U7EnJTUXOWCy8vk46q7hahSq3qE0YLlAO%2BSnyUs7EuYKEDRYz%2BWM%2FlLYsy4AVGP%2BD8FaltsbgkLtn8aR3u5XHidmeNB4f3ieAsOPkDWm758N2UiC7G5C9gi%2FMr%2F9sXHQx4cTX53ZuCRDA%2BxTSzsqK%2BSdVD8X6iW7Yt16abIkSMUZLQ92BhYYsrO8cdlnxE8h4u%2Btb0VZBa78ZLaqn7N2ffUdxWIN75YIqotzajPTRJk9UxdO432KlFBrXgtWf52lyAMb0c4HjIau%2Bb%2B0RcgK%2BpesBtLsGwBdVlCweSBHo8ewHPB1PNa%2FLm0w1fSVI0cttEyJ4zzW9mwytHwAunhss55Yopcy5Q%2FAQ0fTUeIKUrGUGO1Bp2xXLmfkvLZWgKMHOMg887v5gcW7uOLTS7xs5MFh%2FGpfJBIS%2BhuVyzVRmoJFVXCXytRD8xfMuorVfnDCm7JG9BjqkAbXJKFnRUOLCzs4f0rVuWr3HArpkKEv1OB6GY%2BDMEED8VSAeujszLVg8POTOXQTFAZA%2Bldu5z5%2BEgi3YawaS4Iv9oRMNibbi%2BokEogERvryXIPMW513U2geKd%2F0%2B2vZ4lmL0ALqN86WFICWNbDZs%2FGaei4bgXeMyiwB3BuwOnEf%2FRpC0fZQIsEeEnUM6Ufs1b7rCKnq1ITD13DANJ2P4HPEcDVnt&X-Amz-Signature=f55693ff3524a5670e62b97c64661994c7c9721a3f85c9a4c5a9d662f890f8cf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVKVIWH4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIEi9Oe9c9IosLp354pmuMVZnHsbm0z4A1Pbok06hRRHoAiAnqMBJ8Rhog4R5MNJPxgI9%2BNWAlTQLf9%2BtP3%2FM92BvIir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMIbd6NrESdFZWWtc9KtwDFPwv1tKVnqZLUDsVoSW2tmaHcUsF3m%2FuFU%2FKmxStM6EvCTRGrsoIXhJk%2FtVgL%2BwCH9MUQIXJVEgZ3S8waOIxghBeziVH5Gpo0IjyKB%2BoeAaCmH8g%2Fe0pPMonskdDQPFPr3xDJoJCOQRzhyMwd6gB4ahq6vjq9oC1xSHfHyCvztjqKqDrcEP%2BPZrrjlBeqSE7JdJmNELXyd84xYMOiKWvuw%2BzUQ2P0kUS48a0J6i0c7MVIpEXWPhdDNT9NevaavkxKoL200jl3lvXINvXI%2B4mLqR%2BhnBVsvdRN7qcm361nD0TcUP3B799t5S9r8q82HUO4JmTCCEmPzxKKCZ%2BOQN88QtW7jgXGLCFnlNJxOTM273q8NoSCAmq3%2BNya8TVwjhbVvwdue83ZrlXa6ffgZUgonAjp%2BaIrf6Kz7eORgE98DRKdtK84D8NlpWPdxCAdstHDehEY8pOFsxPOdUrnc8HrQvi3VJ1hOWnovpBfNR53NZJ8A%2Fe5Xyj3Qig2VKaAFAc%2Bs6yEdo5dwCPFcZAfO%2B2MRZ1DXCB1jvuKZ2CcbWwOCW2NsRVaWxMIm4bsNIuSieltKl1LalLvF%2FLXax6UzJLBRf%2FnXq0ymIYEnNi4wkK1ZikEckLBl3z5vvvmHUw1eyRvQY6pgGHf%2Fke00J4MzRGspxUkzI0X78pW2Wfd9V3cgMYwi9lZ8%2B8kwfOGDnoO8CWbOKmKnSCmyh36ygX4BB93fIjQGVVg0cz31asLfGd8H2HB7SeT3ZowTh3lbDIA06uHGontuifMYvD%2BVhZwXYWYSj%2Fkb81yYVXJjAMzY8hhaK3kbsd6YvoDBdSSjBDyLZsh1aZ8IbrNteEUvz65QcEyljT7HSyyvL6PB9G&X-Amz-Signature=81ac8d045456143ded7a79be49a820af2cba6f52bbe45f06aaadd62cd1ac3afe&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YKJYFTN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCICDxEF0B1Jrc9p7KRjG8I%2Bzy3JHzHCBzB%2BUpAq%2BQr65nAiEAo%2FZIl4I82v5gaVnv2Yl%2Fy10JUM4qhd3HZjTad4k6m04q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDNpUR981SggF7fNU0yrcA3xMMtb7pahvt3y%2BfG5DgdZdhMABacHTneU%2Bj60bDBpWUdrkfRkGrQtAFQGfyEqrklbQ%2Bgl57uk6qS%2BHmqItWZ7vJhzC5aenttdePl7iXupd7LZNl3GVY9rgnzr4N7%2BDwpC1h8XuhHPHj9rXmxwSc%2BLRlJdl4IcPFQAMAnMuNwShH9FZ6hod8ttqcWLJhW39YetXEjGPrBpOXuJdcFIhnslv1JBxY1h%2FCvP%2F1%2BdEwxQJXEtyJcN0fhiyZ%2FeUo%2Fnau2jnyyXIpXX0B8LNoE4XydF3QTHH9yeZMq9uE8MG0uAgg1gX8sTwbr34XtFsaM8ty9EemPuaoAgbnSkfl2vbDKzOGBlb1Hf%2FErblaQiC96w7P6aVA7T0Vve%2FXd2%2FdlgqMyd5xAToOwr7T0K7aAe3DLvVdXDXkIukK64SMahSPOk9F%2F6czABdMG%2F0PpRmIHw5TtHV4%2B5bSLqY13oiU2XpqWgM7nRd4hVqiXk6TDb1bK2QX4BsjD200psMR9%2BooEFxFRW%2BLb91ph72VWTRpW33GUiG9SA6NPs%2FhZEiOaNIHMykIghkNKdOsZvmExucOvgKqfzBy27hRd1iALSfrX5xdO3gd0kJ3iJgjMvWLHBV%2FGK4c%2BZF4bNJ1Y8QYQM3MNfskb0GOqUBhyia6PS%2FcHVo9Z%2B3GDxepX5Dal7H1GPQ%2FXrplErkk3kKG3800LNqWN8zIEboz6%2FQsqAbJ7BJgZDmXSWJDBypyJS2MIhA%2BWL2h%2BrIsZCzG8WFKtPP%2FXmh%2Fy4h4rJhFevnVnQZg5Yo7exXE0V760eRv7rpgLuTgXsZc0Y4VfI2pnpGxUtjUwStIM1dpLLOB5ssyfTvpnZeNftxFAEg%2BXuctUGC0Ma6&X-Amz-Signature=66550a8a71381c75ee50a36c2b0f889914e0dd1fd493e0f74c49a7cad3818f74&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS363UYY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDGv4dVxcrlXnfLKrcX0zbx3Ui4TVCWxVVAQ1GgiKcKpwIhAIqe0bM%2F%2FfbVzBWqrdWch7TbG1oYmnlDPLqs89ewR2eGKv8DCFoQABoMNjM3NDIzMTgzODA1Igw4RGnM2eD0%2F296iB0q3ANxYLzfwGyIn0wNHb0Y5PGJfBOsxqenVmfODoRy5dsxVJaW2C4sAGeVIAzwr9bBsr47YvbG6d65Wh%2F2%2BNjwUHZv2E5OijJjYw6YdxB49BYCCk08I66nK4QA2xkYt%2B0QKfxJOI9y7Ty9aCJ0fMsaJEfOen7gjUpf4HybploifKYvSDKy4ZhNI2Pr8F58l2B3KYVVWpox5%2FDF3qn1TCvB9bnAsMZk9h2P7LqWpdr357QP9lB%2FbEFDblR7GHBehNpbOEWwfBwv5ZmLWiStrRSNbaYUUOIAKIFntLE8r8jifBna0kZCUH%2BhltG%2Bqw4UJuM1ATRD5JCpK0Sv%2BpbdNEspsu03gNjCm%2FXpifJHm%2FfB%2B%2BYROyPf6paMwn5kkkb6LprHC2j%2BfHguoDjb30DZJXCboo3jwu2qKoMZocCxtmKdlqNpocdYlabU9ZpXONbocYbU3xV68YNnnnfLHraceyqs5L%2FqjXEMQLPT2G%2FpZM%2FRaiQRZxHv7or%2BMmbu8bN50sEkpPN5gPIQSRtGWFVM5HRRDh2bXsdrF5atCFfIoMH%2FZLkg3rXiyYw0UMhTpeY1CZxipqtTn0yr0JZWQrOg%2FKKAaCGtqB0jSFUS0Qkuym5nJslWj9NzK5q3j3l8R3iL1jCH7JG9BjqkAdU7pf9AJXlGVIStmHL0LXtBHUZT9VAPA1kPvAYtp7cPUY8RXP8XXQ1%2B2tMVeI88W%2FWMqZlrKHDKXZLcoNSBS2lcYWx370VK%2F0kqFoiTN4I60SLAqz%2FMpSxksxeu7KgE3FXDJz5akre1yEGioeFkrTNFLp%2BeRN6OucZtKDn5FX6SCWBFL4rV8fzZBhplqpu3Sv7IoJyJOn2FjQB33pl%2FnsuBuZ8B&X-Amz-Signature=2ae79a1f53ab502352a6fd8eec785e46dbfe0611fdafc55b1c76ae3f03930580&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGHOSWLS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDYvV0909bmy2umHo4qUFQUtusPD1m%2B8AYByhb4gS8tgwIhAKyB4CxePwgI4xlX6j2XnwRHLxqEthOEcPOWxRTqa9r0Kv8DCFoQABoMNjM3NDIzMTgzODA1IgzRwgIGWb%2FywT7e%2F7Qq3AMQ3%2FJZj3p5UJt0DkcsezQfbK0MR3MBljbCCTo5LT7fGL5OeyLkCWQtAawHrGmAdXqIRaTwHCOALA5dPaVnLKknjrWEp%2FEveSEeVU%2BRcaH83j8ECztVU7nNMjKX%2FWjxobXM4JCsMJwVBgW%2B2ItJI0vwV8jpIeS7u9bjAEWypOrriKtVlJ5n2ViFk1IP6N7U7EnJTUXOWCy8vk46q7hahSq3qE0YLlAO%2BSnyUs7EuYKEDRYz%2BWM%2FlLYsy4AVGP%2BD8FaltsbgkLtn8aR3u5XHidmeNB4f3ieAsOPkDWm758N2UiC7G5C9gi%2FMr%2F9sXHQx4cTX53ZuCRDA%2BxTSzsqK%2BSdVD8X6iW7Yt16abIkSMUZLQ92BhYYsrO8cdlnxE8h4u%2Btb0VZBa78ZLaqn7N2ffUdxWIN75YIqotzajPTRJk9UxdO432KlFBrXgtWf52lyAMb0c4HjIau%2Bb%2B0RcgK%2BpesBtLsGwBdVlCweSBHo8ewHPB1PNa%2FLm0w1fSVI0cttEyJ4zzW9mwytHwAunhss55Yopcy5Q%2FAQ0fTUeIKUrGUGO1Bp2xXLmfkvLZWgKMHOMg887v5gcW7uOLTS7xs5MFh%2FGpfJBIS%2BhuVyzVRmoJFVXCXytRD8xfMuorVfnDCm7JG9BjqkAbXJKFnRUOLCzs4f0rVuWr3HArpkKEv1OB6GY%2BDMEED8VSAeujszLVg8POTOXQTFAZA%2Bldu5z5%2BEgi3YawaS4Iv9oRMNibbi%2BokEogERvryXIPMW513U2geKd%2F0%2B2vZ4lmL0ALqN86WFICWNbDZs%2FGaei4bgXeMyiwB3BuwOnEf%2FRpC0fZQIsEeEnUM6Ufs1b7rCKnq1ITD13DANJ2P4HPEcDVnt&X-Amz-Signature=1e7b1434d12de02ff1138e9f493308cc436e4889dce61ed1170effe00fcaa0ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI3JLNZQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCxZOJctQE%2BvCTXDD6N0GLPrY1ADrFv9BWekU9xJMPUYgIhAJ2Yh3JswM4ZxU9pECcP9i2slkBAltPfyy0nPtDPGCNAKv8DCFoQABoMNjM3NDIzMTgzODA1IgxtL6QEUNTkwr5MLGsq3APbgB9OK7ZPVg7JVevAXp4gPIyeXKAOGryh4KzvWsKe7TGDnS1x9C95U3tMz5diufZCX47klOu1BrN0pv6Iz6UPO5ZxhHkT0%2BNIgrAqilR3wmjCXBJO3%2BhrO0TK%2BsuxnGzg%2FProEp4yk4j%2FnEv1hLa8%2FDSlzm2vhEGOj3bJm9lp1bLg4%2BAnLJiK5RqiFWgdtE3IM4xCwDqqZeNTs2PEukI%2BUOzO3gx1W97OFtOmUJDSmtBo0TwuUxGWPHp9i7QZO%2BTHmV%2BSYsEdO0s8oc4M1PDsMyopXPgBRGPVPDb%2B6jBQNj6Izsj%2FoKitdXa%2FJ35Jpp7M1WoRxhot220edEs13TARxeB9Az7IH8qkAcb%2FMjSzLX9OzGbGUhHzHycOH%2F%2BF9hIHIX%2FI8ZddNlUmwj87Rhjz34CojSFt%2FpYyvpENh9XxFav3yTVZvkkFUXMuIfNyiwesoMVfCvrnSsiC87mpmgWChKNkZI1WXIjlhKCnWQrXx1MT9LF70RygfhJ8N%2FXEnVWctiPiYgMfLkB07hNlaTRgOLxYDXiUned9VPWYKzhIog5kMqqniy4Gb0i3kHXnuX6qaCvTc82I2epmmIUr07EfiicsaUp3OClSK1%2B2mU9rI7mTUV%2Boi8wZhTgnTjCe7JG9BjqkAftQYO%2Bphm2b7Uio6rb66%2FH8%2FK%2FHwOYTxmiGsiP4PgmwvI3TAxIn7hEgvE8MBBCuzevkoQaV911ES9nHOmpCc0NpzjYo8FwuU6Mgmg692T45uJckH1uDuUvz7BGkU5VYpPD2udkZVR4Xogybvuuv9whRPrt%2BSJLBjagms8GxHMxWOS%2BySbFKTuwRkZEF9B3%2FqtFI181qd7uVtFSvtLzk45DXkuHI&X-Amz-Signature=ac4dd5fc9b39477f9c4be56eb442fdfbdb5f86c1533b26340e47d2b83a521a80&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI3JLNZQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCxZOJctQE%2BvCTXDD6N0GLPrY1ADrFv9BWekU9xJMPUYgIhAJ2Yh3JswM4ZxU9pECcP9i2slkBAltPfyy0nPtDPGCNAKv8DCFoQABoMNjM3NDIzMTgzODA1IgxtL6QEUNTkwr5MLGsq3APbgB9OK7ZPVg7JVevAXp4gPIyeXKAOGryh4KzvWsKe7TGDnS1x9C95U3tMz5diufZCX47klOu1BrN0pv6Iz6UPO5ZxhHkT0%2BNIgrAqilR3wmjCXBJO3%2BhrO0TK%2BsuxnGzg%2FProEp4yk4j%2FnEv1hLa8%2FDSlzm2vhEGOj3bJm9lp1bLg4%2BAnLJiK5RqiFWgdtE3IM4xCwDqqZeNTs2PEukI%2BUOzO3gx1W97OFtOmUJDSmtBo0TwuUxGWPHp9i7QZO%2BTHmV%2BSYsEdO0s8oc4M1PDsMyopXPgBRGPVPDb%2B6jBQNj6Izsj%2FoKitdXa%2FJ35Jpp7M1WoRxhot220edEs13TARxeB9Az7IH8qkAcb%2FMjSzLX9OzGbGUhHzHycOH%2F%2BF9hIHIX%2FI8ZddNlUmwj87Rhjz34CojSFt%2FpYyvpENh9XxFav3yTVZvkkFUXMuIfNyiwesoMVfCvrnSsiC87mpmgWChKNkZI1WXIjlhKCnWQrXx1MT9LF70RygfhJ8N%2FXEnVWctiPiYgMfLkB07hNlaTRgOLxYDXiUned9VPWYKzhIog5kMqqniy4Gb0i3kHXnuX6qaCvTc82I2epmmIUr07EfiicsaUp3OClSK1%2B2mU9rI7mTUV%2Boi8wZhTgnTjCe7JG9BjqkAftQYO%2Bphm2b7Uio6rb66%2FH8%2FK%2FHwOYTxmiGsiP4PgmwvI3TAxIn7hEgvE8MBBCuzevkoQaV911ES9nHOmpCc0NpzjYo8FwuU6Mgmg692T45uJckH1uDuUvz7BGkU5VYpPD2udkZVR4Xogybvuuv9whRPrt%2BSJLBjagms8GxHMxWOS%2BySbFKTuwRkZEF9B3%2FqtFI181qd7uVtFSvtLzk45DXkuHI&X-Amz-Signature=6a1958266d9c5e7a255270fe43b0e5ba33f6743e470091a32e55964572f790dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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