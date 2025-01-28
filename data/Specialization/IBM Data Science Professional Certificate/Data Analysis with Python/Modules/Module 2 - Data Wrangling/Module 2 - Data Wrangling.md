

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H7AIEPI%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDykYD0VIMvJ3XTEO4CnoM2VuORlSt1Lon6AjM4jK6%2B9QIgH0c5t4yy4U1gpttUQajOWZ%2BcISc%2BnqbG4VylIMchXcgq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDAL3PnnIQrucj2xJOyrcAzWu9N1TvNfHSox0EA8BHGC38DwDmxWZL0T%2FyoKy44jKN%2B3emkMV%2BuIepu0FJ2SCikHfo67j723n4wTYWtDwEvffMzpskmAY31MA16%2BfEhf3JDrzdd17SZxq8aa9Q%2BVeZZKWo3UNysZckDHaonWp%2BSL9lKJx%2F7Pa%2BsqbKqOwom8FyWFrh01p0M37QPsa5TCMcVRbh8DhIRQAQJYHjaRlCcLog7x1aPPZuZoY8BaqLoSjOjKfWlzgWCL8eyaEsDASTntP8xVNtF5Z9C%2BMjMBx04k%2FeXV8dRkxTx0jicWdzn2Kt4dwoByp7p1qocBJM5F4%2BGeNkJktg9QNxIKd62%2FvqPb1Rkgr%2FgXz92sphVZ7jL%2FEeC14VVxETy8ro0wOasI1YCs9PvC8KqIA87qT0GM26wJIp6Ev%2Bju%2FYZKbO46C5aY3%2Bot5YdHBcFomFInDgALqv29qumkQkh8pzBCypsZmWdjjlRSX5pMUZQYg8t3202r4VylkAmPMMzlFZDeFnpubfWzTdXIU2ft2MqK83BhFjTvhf%2FmnTguaNo1RxXB4k6S6TiPl%2F2zDN4M%2FT1hHwJ51U1YVcNJ%2B7MNAZi0%2FsLYB6HuO6LTw3%2BysgGpTg%2BQj3I6%2F4gzr5rZRCbJ3Ga0yMPSU5bwGOqUBZDOvFvFgOdpBlnejKL2sEkfi28y0sQ43AbsAL3HNYinKl3rRnAyxU%2FKg29YNs9oY7RwZmhJUbw9%2Bjeo%2BsSEqa8%2BckkaYFnJCHbyZWFsDf%2FM4oD%2BHtodfyYE%2F2i3G6KWEM%2B2l03M8THwNccW6rs96IkWQZCCVPu1KgiZtOOQN9wZii6%2BAEPrSkk%2BuOMlvPUCLDymEyASMzh304awlfAluH2ds4KiV&X-Amz-Signature=b2cbaac49cb4da736fc1dc0533f337dda514cfb7dcab082afdb15ff0cb124640&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSFQQWJF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIGgwGpnDVsgVljBzRM%2BjrnnpI%2BiGywny1PdVGF1TbWNiAiEA6%2BzxYAf0OiU55eBXAqWcUILeRyGjzGVJUWOHmwQxDCEq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDI3fqne8fNnurRhAQCrcA%2B8B4DmgSgbTNsqZYYX8az076e6FUFSnsoaEkitSuo6PcGhCoeJUFAhe4VR7ez8jLX9jiMBLqlXwcgWV8rQbPznjivG55yqe1IsZ906%2F5%2Fxr0vIu7sYzV3ZiGi%2BY%2FRy%2BYR7yOGDfwRukWcicMKa6feIOFPlgEmgSpWpZDBIqu8cbvYM7jHKoJcDOPMqJnJRY%2BHazGKvGrdBNm7eKWykTuBh8OTxVChZ8JLAIVfgxLigyyVQ%2FavY5QU0Go0Sem7GiYWn4BxUbBiAgGDtqB4utcIQhJCfad2C2uFF9CHb5LkC2Yg1ClTE2ccGiQdMAWwHx8OSyiKwu3iqy3LXtcZRQpJtteqwNm6Rh2DI13WF3BkFzoi43QKH%2Fi3FczEiMn4kQf8yHnDy8%2F5KwwuXr0IBx1wk31j3Vi9z4lNOQoWK4owaleUbTgSFrQrtEqQhKC6GAUN2ooVgt6%2FCh9PgIFuFZyost3turVS8UYlf8ytu4PiD5Stiy2%2BvBKArtlIgy1oq45Rn7nHRsFtSR7gPxH%2FWWKestzAIe1uIKBYFARsKv5Az5HFJ%2FStLUAwQaF0suvZIgVZFH0PcsgmOskJzgUWtrJmGK4cUYrG4e55W38pcqm82MOhpb1hJ4TS7MnPjgMPqU5bwGOqUBeFKFmiUVDN0V0cb%2BeU6PZdqvlqVQ91xlvoFp2%2FR0RYFRG0Tvh3cCsQzJvELVXWNQrHmcIFiHk5Jps1ZhwcHR1AD%2Bb%2FKiQHGuJH2Pq7SGKos9amqilX3mKnlV4stJRJxLmsoV8n%2BROwZhymzldxWWhasMCLJth2vL5WJIRwy9djVAHltg6%2F0%2FRLKqUQTYLJI6Z8vWGez9ua1%2BI2fL8wxjDv6NAyue&X-Amz-Signature=e627b5e73e20b79ed009f0895716795049cc61950959c17454b1cdedcae51c60&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUIDFYIE%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIHjCSPLPcFM9l99PlNVnFQijv3sqbWnCHrExxlQGjasRAiAB6sebdBN9Y18GrYbdWF5Wneex9UB25KxurpkuulcA2Cr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMlWeAh1YflOa84Gu7KtwDD3xlzCieT5ZjE56frBT8mBvGFbAm00RAtkvek%2B3oTSeZuY6%2BzKvLjzvB3Vv4XgpgFNwjlNY1Yr6tffMFI3qUUKadkjFaTfbATYpCqO%2BarLGYznihugWBW%2BVxjBcLwKnxLDillcOkmSPe15culXaD39lyPAhE5744IlMb0fc7026WAFMsNeUfhy3rQYpug6aSo4BRWTULI3xAYXa8g8bxXCLOge1lxa%2BYOA4goF54zQeS2QKW42Gh%2FJJv49rCsZphRaPsYb1%2Fslqyl8ZeqLyE6qvYY2QJi34XS325KGrZZB4Y3ZgSy8tHqdVK13KBOuirii9Yn5%2B8rNrmKTVovCBKrMRPwr3%2Bsn4ZWAE4d24gfzg5U3bEEq7wLRBwdVnSCSFkNgSrD0E5WTjwb6OTLAJCBRUURW%2BD17AOd%2F%2BCrRpEcJvmzvYQpnx3IklqF4%2BiSf%2FA%2BNU6uOWaYG%2Bo2i%2BA%2BvL%2B1YrTwuw7%2FDslwvZjS7J6fGXNodXrMoiBGKbOT5X7VOYENZyf%2BSLQDRu73vHFBQZetITdaWVD8NkL%2BoyD3e9lQG3iZKg4qSLX%2Bde9Zi0XBywgN5qYGImFlMuezpcPnpfOz%2BgzgSl%2Fm5BW8OOHMsFz%2Ba22AIXJXgEfF3ZzHSgw7ZTlvAY6pgGtkBc5oblD2MOJVRIhkOI1i6ZYm0XlE7hPceJsD%2B1d93Q4NHh4hRJuRhFL5Lq4hLlqh9f0xSbPW0r%2FvYtDOcGPein6YmPrvwnLgMWYFzRufT87FYj8hZvOBwNGf1pDRHbdnAdIutEIvfuugC4LAAiVzYagxvHb%2BXUmMqgRzMfcsfveRyuNVV9UpX4fGAqnb%2B9PwPbe0OJg50VfHaO7IiwcrBBupQGR&X-Amz-Signature=b4c18f76cdf90e9151ad382ef47b148b88b38558523361019214d36030268a55&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKJZ2SNR%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCICRfSV3rWlLbmvGLfmKqlmZU2hQT8LxHUEY1OCEONY6vAiEA90RpvbzPNGEhqfisVPh%2FFJOSQ5Qkh2p2VZ%2FPoYjrXe8q%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDK2PDR9fVBci4pb7PircAw8f6Tva7FReqFzkg8Cz6Shho7Yh4wU%2FErORn%2FamMnjhf4rSx4Cwwnq7ydBOTWznrJgvAcSEcPqF1C1%2FZKnY4Q5FmNjT33vcaxdkrevxak2nRuHiiHFEmrf7bVAqh3vym3vXFCZ8gIF7%2BD3fIr6QzqycmMHHVt8QLWBp%2BKsl%2BUPGGb93b14O2LWdjAdfznJrZQqeysxYhCBiGyc810uBslI33K17OBEnvWdgvsu8VpyoCLw6qg6daWY2SmOFTmyhRBkK98s6As7JMEpqZFJcs6FSIeILAITr5AzHXetHZ%2BSrK2F2slU4F8KSwi8dTL%2FNaPGHX%2B7J8rczGVtj9twHbewOifdZWXxj6juRmCIQCh%2BO%2Bc%2Fe6JvqQpx7BQw3997hjZV0vhNdpxPQIRkR4jFbUwGNxzzA0EYwGycn6aflPQJLjlb2VepEyg20hAYLhy5S1ov4Jh9Em%2BHfTVlgyUUwliGM7%2Fb2vw112O1LYTFtoDdfCBsaU%2BwZdRBBtEbF1WA43OlPFeZM4DKch%2Fd4g6pKm12xJNIt0GwoW6YzJK2W1VGiNiI3VASRatxLSdnHUAtgeMT82Tph0gcAYUODn4HMCvgcSVPVf4NsoV6nmjKpE3VR9hHA7ZznBk2c8MNEMP6U5bwGOqUBfSAjymbuQj9qSYiHLWMr5hlWUiDi2W8JHpe8PZxuJTiAPWdiKv9lIUL%2BqiRMV%2BF0R5W5g5iXbgeBuqbqDWp7gpgbgmIBdRQB1v%2Fsbq4umdrsVBpr1YA8SpWg7ST5QSWw4Uo15TdG7fLyJg5Z9ccDsS5POAYBPjnWPSOpPfRti1KcEzG9eh1ObvbNIj7mT8KyffaGZ5mJHNk600OxGbpY%2BtxCSgC7&X-Amz-Signature=09344a0e606049e34356436b450bbc80aa829fdd7a75c0275dbecd272e08e3f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMAP27KX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIHZzxwBAeXvRDjYyoPk66uxU4QNgcYmukZ9ieCh85jqPAiAIQH8miF%2BJRiZRlJTWqGVRxBA1d0MoIcUPMScgRThZoSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMmy8jaaAjrunPIzzOKtwD16pdeSv9xmB6bmZWsrSEdwMnI2hjDAsW3il%2F0sMLIn58NmbGeeQcFw93QdGZXkmbMLapsVym8iYQmMvCbrNh6RezaRjrJosauXSTx0xUJJC62JWq%2BTekNuxSVkpFQoUh2rPpc6lYue8aKOKg5EZ2g8lSubOVc25zqvncWHgRJ3wGWhv1t%2FPVf5ihn96oDfgMOte2bOZdE9TI1ey0GbjO5SfhUxgnkqtFsmbtqfIq8dT8jjYa%2FrGGETFxraNe69XMlY%2F7%2BlJhecXOlT7ANTIIpg0R%2FV1CTyFmX65IS7xRNxys5DhV0k0J4e7C6eV1tF70V2e0%2BsUHmLeP%2BOqzQICZzy7gwTDafvkZRb6giMJOGZv8gD%2FVd%2BxPNuVDz01OEJdZRLtNPSlCnMgc5EjmRmoqRyB8j3JFG3rm%2BOsSUk4JWtYz%2BvRIq3nu16ffxjQkrci2vOyUovDvnVcRjVDq%2FL0cnNBfW1%2FGV%2FP%2F%2FuLN8up5FV7Xg1NAhj5oCSSfBE9AhyrFe%2FaIRFF%2FzlN9lgdSGxUh3RTFpUPKORgbAmJPMHBsdee7%2Bp%2FnkAuYpN%2BFqJy0CumCc0B%2BUXZoSOhA8bpcCYBaIuR6L56w01zuLwyXpAKFXz9fJyNFu0Q%2B%2F8kYj1sw6pTlvAY6pgFjn0uJUnm%2Bar4qURz2irZJUou4wDK%2FCcKdl6aKTxswOx5gpTUKU8wX57rwwfze8jTVHASxEqhSlRnjBn%2BQ618uBtQvcT4hjZaOI%2FJJR%2BPBDpKXNQidk0%2B2tNi6F6L7WWglkNcw6%2FP9R9Hh%2BobvKJYyCVK3KEob0YpPSNCb1RyoHaRFytkrZxQJmmFHDSDz12Wb4Vj3iUXUl0AwUnxdWBbgrNR3dFf2&X-Amz-Signature=d65a2d3f579d84c2d4a1a84f5c47739f0d63a2644b0f5c96eae4ccb2075cf4f9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YE7G6JZT%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQCxrJhxD9QMxdC8Y%2Bi5JKjoVnDjnDdnNdNiQKUbInJQGgIhAIFYV7OULFe76jvkb6zBUhwtCjrNIVd8fZJnh8%2FW8FHjKv8DCH4QABoMNjM3NDIzMTgzODA1Igy0T7cUIEGYTNrJGdUq3AP5pUp0aO1A1P9I4%2Bq2ifEvptL4uBrk4UEfZXUkaP5L%2FO%2FD8jEALyZPUQfWmd%2FchnBDUPENzvKu50NDLMgnB%2BqgxZfcf%2B6Z2reMrGWEq9qCpQLjCyy2LSIZJvcNqHFxKFa0FZK1Vn8CCltX99NQs3tG7GNgFJVsVjLdpGF7OMCUHfkdFzQBncf10oiqln0OclyKjNx3Taopr3Lmm4Tpxfh2M0uMieppUyBKAakE226I9gcGlLjLGlyIstbJObq%2BiBC4dg%2BZV1qIyjiPitMddQhY8TnvP7jb0OJfRLiptWF9QC79o9yvOu70nZKUQRY716Ch2THagyvbiQ9k5n4CT4hPMjinPHQAPDMly7lO9V72i4550i40q7zEsEMaYWfSalqGvNHFFaPEDEAUVpEU%2BABXGRmMSrz5%2Btb%2FhPI8iWMO%2FGKPGqtJRFUm3tIxuDI981IVj1oqPrSHwMv33VSgcFrB67q2UYDM%2F7gqK9q7aSbfWpqaliZ6sTFsqpJhh3xBmcVfYEtCgUo4BOAnMYPloS62iRpekL%2BUObyOeWVCdFIYchZ1g4EKrwnUFSu6HCxK6EOf7jGFPjwVnLRpBfick94qZ%2BzGRcSCARH38sZzDQEwy2LsrsBAybrbOC4UhTD%2BlOW8BjqkASRw2oQ9sGk4RlOOz4lVd1AGyVJ0JZJIuSilxM%2BNvH5jA%2Fb49qs%2Fi%2BlVKXZL4SynhR1hYceMiUHYxO%2FzhRecFu%2FRisrR80Wkd0yIlpVDPZmdWvPq7cb35s3tXTG%2Fg1evU9Xk3ViB5Cgw5pVeZKB2AVdh8IffRlVLK4ELbZAwwTz8rGayjFI3wh%2BlAUNuF9Up0yEk7Susj23lKNOwcyKJXjOiJjci&X-Amz-Signature=20922a8bf0c14179177c52634c86d318bf5ad76427cbe34b8c35c9d1eec9bdfb&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YX7BX77V%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIEBB6Bnx64mnX3XTeGJ8rMXlBkL%2Bc9w%2FL6myN87bpmDjAiArjJ06LHYuySMfLYuMhnhimvGpCGdVqDOZRqlyy0UEfCr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM%2FYnESmKWppdgvgnfKtwDnpfnzQVTThsLLoAGZ%2BZ2YBnByeuDE%2BEUlFphxGJafDlYihuYROk1B3R0iGYVAVfyfBpqzFKGYTKIcv73SJjmF3I8eE6%2BPrSY2NQbci8HhKl4B6w6LZsT%2FlvAeBjGbuLZnpGI%2BzvJJVss3L52%2FJhFIc3AHQkiJ%2BTIFBjkJkeescQO5yry%2FGoaDWh74QOwkncNpslRx%2F8I%2BwWM2w6LjyBI%2BDi%2BfvufJ4VcMtDmPqbLKKYPOZ3LfOADIyUkaNrDLn51xr70Sg1vqbRvDjSR5Vu6FOYGvVqsVzBToTN31pRJ4UQ1e1NICaCdvxdwYYxYlyEjzCZkOeMdKD42m7vPF8weFjAs5gV4Fwk0q9WrX3lC5y6EsopMY3nD8paaOzuzZuGmmIqfGLrSaDsLniw2cJFW6l22NoXDlWWDAZ8%2BZ3lMfIdz5GdnwVy7iaMH%2F9beY86oaqgFj3%2FqCkecWLe2DQ1BGG5nGJq8FAvQSAa7LkodmxudJOlCEa1S85ycBVUF6fXQWamXjhIIhYz7uRRwscg7RZwD%2BJgsDy0i8ThAFFF1Xn%2B37IGCTZOrQOTXuu9byl7XZ0GzhVj%2F9Umu2YY3ft5txIv7HGwrPLMmJG2Pp9updUutOS9E0JUFtyX6d1Qw%2BZTlvAY6pgFWP%2BcTR679HmP2k5t8GTtfTUvDp87TKP5MLCtBFQxb%2FRJ%2BFaKaVmvAboHNfPg%2FXm5hIBAl0hnpkgTizMZ8npkrqIDEXbZr4K%2B0gemj6k0MO9xM1lkFhZHRr3Bf4FsH0pI%2FyRq7dOfCbUMY%2BxZ5QBYLNFzLQYfe0q7GHaSWAKQ1LqNNqYzYuKujMoWB%2Fe%2FuOVDdNKxNSeQ8Yu6pqcpGyF%2FE0iJjG45o&X-Amz-Signature=f91910562fb167d12de75af75d244bddd6a8420ebff9415023472a41623a43df&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDEEH5GC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIAeX4nQdIC%2FySn3ZP5Lnf66EBPGVQnbk0aPUjT3Ql9qjAiEAtKoha%2F1r375JP034O2oaHDdw2BtzCQ6WGKTnheLpG4kq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDPr8bPq1vPoUT9JrbCrcA6B7StzK6IuKzoh8beeUExD7L9tIKRXCWKEwOhEQGki1vWK4D0HlbCBplDGDpHtAj9wsSDPbXjDYgOxNbptO%2FuO9gRpPrExzk59r%2BDlAqCo2rhfoY9bXkbGSaRqGobjhbO5S6KgKpyGVd4AYXNeOt0Kkql2U86YYxiG4S8BtkYK7kq8QNNw59F8hFsdRh%2F8fryWnn8eqP6G0cvoEjIMZAhthmdjjpMp7HjVjq2R1yhQD9ticL8HW0mQpfxusD3de5kap8NsMIuFLjsvu8xQ91BU2DkLcuQpWdUl9DuPkhF3SHbNf31nM7bypwLASTE%2FMr5Hz02XvnTBRXy%2BeaVSjGhVgKTdNqvj42P8FjNFPIm6dr%2FpJOHpoaZpKcXBVrULzt0TEl3J5OrPeOB0jpbwzAeDuKpbDuMLTPtjY5CBs%2BIskuBWYc00lYeTiFovluqyizxD4mglMtm5ofWSqitu5yXNch5sIGHZTa6i1m3gxAY2hgVZ1sAAIWOOfzSfLUXhuLCY8fNaRQCgNIs8hcM%2BbBby3eFzJS0A1pv3AG0VK5e%2BqOnkpjGFj1QZ5CLNRPyt1fS4GyOnbP%2BfY4Gxdq7%2BiVeOxEWWzUpvhpCSNsYo4XlGXCmYA9uitSl3vHMJUMKqU5bwGOqUBS7%2Bjodpd4sHFCGkdm7hWOQZXDr0buCnZw5VQuIB2mVp3fT92r15PLHsYzULhlfOrlUxi2m13zEjIxBWpbOVMeMVuflEPdGRA6teAVXmpEMiL5MB%2F3FyAv2L87wq%2FoVequOvWhHoh6q4nLsSFAMvCueQNjLISZrAwymSD%2FtH%2BQWjyIJKnl7Nd1mmmDrYkt6WZCK8WGW041XEeXaY%2BDyH%2FyUFu%2B1jB&X-Amz-Signature=a4cf9979c1fe08191d8de6527bd8fcae690c53bd34d85dbf2ea78ec96fc9935f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMAP27KX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIHZzxwBAeXvRDjYyoPk66uxU4QNgcYmukZ9ieCh85jqPAiAIQH8miF%2BJRiZRlJTWqGVRxBA1d0MoIcUPMScgRThZoSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMmy8jaaAjrunPIzzOKtwD16pdeSv9xmB6bmZWsrSEdwMnI2hjDAsW3il%2F0sMLIn58NmbGeeQcFw93QdGZXkmbMLapsVym8iYQmMvCbrNh6RezaRjrJosauXSTx0xUJJC62JWq%2BTekNuxSVkpFQoUh2rPpc6lYue8aKOKg5EZ2g8lSubOVc25zqvncWHgRJ3wGWhv1t%2FPVf5ihn96oDfgMOte2bOZdE9TI1ey0GbjO5SfhUxgnkqtFsmbtqfIq8dT8jjYa%2FrGGETFxraNe69XMlY%2F7%2BlJhecXOlT7ANTIIpg0R%2FV1CTyFmX65IS7xRNxys5DhV0k0J4e7C6eV1tF70V2e0%2BsUHmLeP%2BOqzQICZzy7gwTDafvkZRb6giMJOGZv8gD%2FVd%2BxPNuVDz01OEJdZRLtNPSlCnMgc5EjmRmoqRyB8j3JFG3rm%2BOsSUk4JWtYz%2BvRIq3nu16ffxjQkrci2vOyUovDvnVcRjVDq%2FL0cnNBfW1%2FGV%2FP%2F%2FuLN8up5FV7Xg1NAhj5oCSSfBE9AhyrFe%2FaIRFF%2FzlN9lgdSGxUh3RTFpUPKORgbAmJPMHBsdee7%2Bp%2FnkAuYpN%2BFqJy0CumCc0B%2BUXZoSOhA8bpcCYBaIuR6L56w01zuLwyXpAKFXz9fJyNFu0Q%2B%2F8kYj1sw6pTlvAY6pgFjn0uJUnm%2Bar4qURz2irZJUou4wDK%2FCcKdl6aKTxswOx5gpTUKU8wX57rwwfze8jTVHASxEqhSlRnjBn%2BQ618uBtQvcT4hjZaOI%2FJJR%2BPBDpKXNQidk0%2B2tNi6F6L7WWglkNcw6%2FP9R9Hh%2BobvKJYyCVK3KEob0YpPSNCb1RyoHaRFytkrZxQJmmFHDSDz12Wb4Vj3iUXUl0AwUnxdWBbgrNR3dFf2&X-Amz-Signature=a725988607fee098da640fbebb011e9b604f541688f82a06097557ab5e1c98ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYHWS5CZ%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIBo0yXwcjOzTE4Y3VCcTVSzVXU3TMeCDsXfXqqcftWLYAiEA7yoKmnXmjwHwCdQs6o4Js%2B1cBIC8SE3JfAy60r5B10Aq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDNJEQwLDMtY2UIfLKCrcA2C1dVGp6NDxd4wZ6gDCh2Nabu13kfJuMW57L0pebzM1ztNkhVVFTU9qElBYELpv5BncMxZNwYJB2VmDMPIWwyFVPjyRFO644rtPgbylLYgyE2YsEeYIZyHbGeCUkgZyMMVwmn7m3zveC3Qms0a62PEq83cdWt%2B1tXHuy%2FnRqQvahEcLiHugmJGbcl%2B5uOoWkNRYCQPxQ%2BxfZCRwKSqTMi8DRFJCoYfyJMEaS8qaaLTbkPkWnIfK5OrppektsfmqoO0iV0aFiDaLHJi12hZnoO58Ncyk3gam3xx6LM5oFYqz%2FEoruw04dzvwGuj9shEZh3NRg9kDfm5Ifi1aURj1vaJ3o7hQy8woagyPZArsiPsZnEwWrxqngSXZcp9jnS%2F%2BnRJ9ZJKDhDHoq5ac8oL3YK%2BWpkzJ13sb5%2BXOftgaPfXsnd3tkw%2F%2BoeIBeVo1OaQE2p4s49kG4XL05cpwB%2BV%2FhETi8pptsddY3Mdm5VYsNFVylX2zP11O7lt6H7H9lqGnMuJuW2i5VbLGuzxBbl1cffnC6cx1H8jZospopM%2FgpgQ6nHOBdGKA%2F%2BDnXZKhofLdDEtlXH60UrW9sBc2A%2F68GhYpzO0ly7cdkyQ%2BoTtEOMtRMsaGp6zVoTvCm17TMJiU5bwGOqUB73Rg4fCdA0LvBbuZS0Aji%2BD2L8tBGVVCqdiw3LJopuFYnr6u1ER5z3Y6Yg8F0fAPblR4ZE%2BneLkP5P1CP6UcxGo7MaKDm%2BG0VsFNlpLl42m4il9Lo9AylLWpA%2BDglHHXn4VwFF1goutXUEklGRm7mPC9%2Bv4YGahpepL9z4PhuB4PvnznjJc%2BEFaQKrial9Sym3ofHgaqgKo%2B7PwJeMOFiW67R%2Fms&X-Amz-Signature=e3bad2321b9edd7bdd87add547b3982c751e5870255edc8208754c04ef44e39c&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYHWS5CZ%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIBo0yXwcjOzTE4Y3VCcTVSzVXU3TMeCDsXfXqqcftWLYAiEA7yoKmnXmjwHwCdQs6o4Js%2B1cBIC8SE3JfAy60r5B10Aq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDNJEQwLDMtY2UIfLKCrcA2C1dVGp6NDxd4wZ6gDCh2Nabu13kfJuMW57L0pebzM1ztNkhVVFTU9qElBYELpv5BncMxZNwYJB2VmDMPIWwyFVPjyRFO644rtPgbylLYgyE2YsEeYIZyHbGeCUkgZyMMVwmn7m3zveC3Qms0a62PEq83cdWt%2B1tXHuy%2FnRqQvahEcLiHugmJGbcl%2B5uOoWkNRYCQPxQ%2BxfZCRwKSqTMi8DRFJCoYfyJMEaS8qaaLTbkPkWnIfK5OrppektsfmqoO0iV0aFiDaLHJi12hZnoO58Ncyk3gam3xx6LM5oFYqz%2FEoruw04dzvwGuj9shEZh3NRg9kDfm5Ifi1aURj1vaJ3o7hQy8woagyPZArsiPsZnEwWrxqngSXZcp9jnS%2F%2BnRJ9ZJKDhDHoq5ac8oL3YK%2BWpkzJ13sb5%2BXOftgaPfXsnd3tkw%2F%2BoeIBeVo1OaQE2p4s49kG4XL05cpwB%2BV%2FhETi8pptsddY3Mdm5VYsNFVylX2zP11O7lt6H7H9lqGnMuJuW2i5VbLGuzxBbl1cffnC6cx1H8jZospopM%2FgpgQ6nHOBdGKA%2F%2BDnXZKhofLdDEtlXH60UrW9sBc2A%2F68GhYpzO0ly7cdkyQ%2BoTtEOMtRMsaGp6zVoTvCm17TMJiU5bwGOqUB73Rg4fCdA0LvBbuZS0Aji%2BD2L8tBGVVCqdiw3LJopuFYnr6u1ER5z3Y6Yg8F0fAPblR4ZE%2BneLkP5P1CP6UcxGo7MaKDm%2BG0VsFNlpLl42m4il9Lo9AylLWpA%2BDglHHXn4VwFF1goutXUEklGRm7mPC9%2Bv4YGahpepL9z4PhuB4PvnznjJc%2BEFaQKrial9Sym3ofHgaqgKo%2B7PwJeMOFiW67R%2Fms&X-Amz-Signature=1477287ec19138b80151408e09e98d0185367de72938c95892cf962a645cab58&X-Amz-SignedHeaders=host&x-id=GetObject)
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