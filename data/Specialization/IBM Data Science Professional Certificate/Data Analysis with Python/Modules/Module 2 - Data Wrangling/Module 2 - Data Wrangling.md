

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3Z62UKR%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDBTX9b9Sm5oGh9XD1bpaO500sEQ%2F3UlaNO%2BoKgGoTyuwIhAOfDpjv%2BCq5UWOJws3FHXkugTDuUJjZriv9f%2Bl8PMLZKKv8DCH0QABoMNjM3NDIzMTgzODA1IgxTP7ZaY%2F1SjGG%2FRaUq3AOVI3nqlP%2FLEYiTfnvr4FhjNjkPHZRbyGYSOjE2lYY47FrCXzRL7QCHraiBwTX9wHYhBulwhKuajkK2i8ReXpZXOed7Miu%2BLbdE21vx37gStrmyBmol7rEU17mzYa8%2BOwkPGHfbIDK5MqtkhoJ2r4wwvCNxQwL1wsJ5F%2BG0zyiu4m2k6nDcYkCD72UPLXridbB9%2BCyzv%2FYzQHxYax%2Fhn2y093%2BC0%2FLoaNvqnlSgFhrRJralqELyt1bD%2BtKFcWll1CCZ9tjhQ9fhk3mKRxyxjC96cByNzfSdQVxiZdgg%2FK34j0v1Sqp5rc77DjHKlfbdm%2FS6C5er%2Fzj8HfoVlYJPt%2BHa2GmPZMkiT%2Boa1XSEPohGHnWn7VPK38rMlsXNh%2FyfVp828DupUM2DcuPDOa86Hb1aT0jKtpGVa2v%2BYZf3eeS1PuUOJMpmnQuyHvCEdOE2fYEiJutaiiUAFI78fZperJnhtfx30Ze8Gc98IO8ThX21p3FRY%2F%2FGiVLrSOgpqof56gpxi7TaNTTBf0SskiIMvsfFS863hLUB3O5yuNSDUejgrgyHKNsSlp6J0zA3xSl5w5fRLYASmgBhv49YV%2BRYTNmwRLMpCZn7EKDHm%2BmZE7MWY05fwlb%2B8lz0HH8YlTDO4%2BS8BjqkAcA2WSwTQK%2B0833lQl1iSsw2Lo38%2B7BLu74iWLyPqbqL5TI7l3PRtYtwgPrEXiP4O2NhAZCt4JsyFes8wuNOKjV7p6mzGEb9UjGaj8ZYrRGDdoIdTRWJJsJ51SeHDO0Tl1IBdA%2B%2BmN%2FvKFso09j1dkTAN%2FkzErcU7pdg1dWV1AXSpHpia1M0UKeQB9j7nAyIWL9NpWUrqpxm3M2Rx0%2FK08KlKj%2Be&X-Amz-Signature=520e6927696c9e6191bfae418e642df134179230708efb6b342f50848aebc434&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMWHBSUR%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCDkiPjvLpCv5s5M7monghFs4WSqSqgJgDwq1OUdyLsBwIgR2iMkXWKICgCrCTA1ySJjk0H3GLjWpCuu8lGmsNtmUgq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDMwX7T6EYK6F4LuUqircAyDY5LQbSDyO3G5nkeHWufB0QemwZ3B3eTU%2FLLd%2BqxGpFCNNqPJ27pKhMsdYzFU566OfBBcStWxatDa6R4UX14jaNFyz%2By3vngR10wFaXfGZY42rq6SMRMYsh64tiaY8a7qWqSOP%2Bb%2B3xUVapPnhR%2FfPw4F12CjC8jtw%2FJV3wevPiJjET6EmZtPkBUwkiJbvDVp6E2A7brLW86a4Kll9mcULYy0ir8saDU1a2bVSyqJCzSzuN5EDuTihThIdbie0cqUER4LpTvWhfx0zkUTg1vyFBDEOILJoP7WwMqqXFJZku9o61pfqCrlnIVFeT88ugqB%2BmVt0bck8QbpssG8cEwk68PB8zZcH%2F0MGohQdgSzfIgNLmPLBoeX3rPgq%2FW7QWLM8aZmsOvna6Y1fU5%2BbgYQ0rJIV2WgYTNKkrp4TWIZGvAwRbHtqExazDmFVkSjlV4i6uV0YpVi8a9DiBZ7kXmBNM6fagYDJT3%2FiSlgjQLI0K0CnYS0LtoXkEoUOi8CSqFOdz7A9Z6JeV0yEKZLjzVFIGXnLeHMOyCFwsmP65%2BohY86elF3liME09YFPgHJ3bGfXH2bjlMT2nWPjEXhWvS8mOUuszcSpSLzOySF7DIeGI3PQkWNE41B7vTDDMIvr5LwGOqUBFHK4gHXKCGN6M17LOcntasDQBZGbdwbWX96iVlsFztN1kxUBEUJ91AF%2FoHHWi%2F1TNEsqS%2BT29fncMgTGfi0Dt0BTN0XurPrCxuyF%2Bin4Sblc5zC%2BNOhPdyJ6MBZ6kxHCddFwkyKAIxU%2BkDRhsFY64yYfsVNSWxLtZJ3h%2BpJ0RqwKSaltJlttNXgG6BWKwpaa%2FYxKgya7JfuHRNY9nB6JongTgy7H&X-Amz-Signature=da54963d9bdc295e74b043b84a629e4dfae222968c5a0bc16f1d1acf2d645a61&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPEKG2V7%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCP%2BLnsFCVgTmoXwFIp3y1aDJcZH%2FW1h9lFhitpPQm%2ByAIhAKJ%2Fku8%2FqxJKix0FsPvcumqHa5%2FzV65Lzwqq6zKE5LEMKv8DCH0QABoMNjM3NDIzMTgzODA1Igx9vVG1vM8j60pi75oq3APKPVyBtmDQXe1jUTpcuXFssB3XVhr%2FCS7WULQuCTZN9YUfxo02n5M9DKbyam8OcKMaeKYiiIptnIEyeDN9yHB2ypxx0%2B2GIaPm9PEM4q4ygmqywLqMGDSewO4QpgeAmuwL4t%2B5b4%2FmdB%2FfCiRhkG2tgQbxechaEXL0rSqo5GMgaF%2FTzPc%2BCgqbdo9P4Bj%2Fh8J4XtqxecnchjOXkSS3AG6BP1Q94Sk0V%2FVtUXk1tVMNmIyvdRvoqmTvlH5Hy1FnlbL90ZssXEIUM%2FNHUMSmJ6gPgjipMl6XPws%2B68z%2F1JJoPZjATVBArM84ZzFim4w16P1WNSFgspRHdMHrHxPRiDfzOl2GsiJJK30%2FCOS7tJp6yN2PFwO8wlYIGIKY1cut7kMOdqaSS%2Fn3Wlv8gHkBuqwx4vz2MG3WVhDntUoe8mWd3Fk7jURJwJFUDBdvdjj0TXLh8tDT09PMMFh59pK9eRZ0VnniUeMu3%2FJ8UYteq3%2F26AVJwG05M04N0LZJNEIGJSDBj%2BngBemAzNKm4ivcDzHB5DZcyZuxa5fNgqGLi9qUzjiA0bMCjw7gW81KNKi%2FTn1F7GyEOR4Xt2ohXsaodmgLacd4OuolfM%2F%2B7eEFxQW8q6za0rWZyTZ0nq5Z9zCm5uS8BjqkAYKwEDdhM3yvVa%2BzG39m0u3ShV5JLxhk0IoFGpcyo%2F99xEvSBcZr%2FWacdh7pDWFArqkkleg5bSszUOXgGJRZPmTXawpHnAQ%2BjSpIPlP5Ghg1VumksW2jAYNCVIbZucpuZj53XSGEStcdAvKpHcRiuiOczhJ3w68k7OG%2BcIefLixFWX9ERw4q%2FldjsZi6jweO7Jbrn%2FaBFO0eLJy3RRhAVoMmlTgo&X-Amz-Signature=3dfe27629b073aedabc6d105c82b4ca1ba20fbdf051c3c084b668682853a5049&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NWFEICW%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQD7gZkhKIlz9%2F%2FDuxhveoebEwMD3i6R3tA5PToMBJcwQwIhAM4ZGfsMxD7XGcMvnNKS2AEhN%2FPLedM7SGuHvuxNF6v0Kv8DCH0QABoMNjM3NDIzMTgzODA1IgxjOpa03Dm0FQ5pvCgq3AM77UJwwDpihkfKYLZC7E1czSnnbPm3%2FDB0bhllZ0aCN8RXG9ltLVTKfh8f3xAfCRmLY2mJEKzSx%2BfMVMicyGpQKHSW2jv237XAL6WTq5qhNKnC%2Fb7uKUTlPnTjq4cVAd11DbRKWsuJaQlO81zRjChzueM%2FofvOOA7sKOaHi3xHwV2NQotp3oDd63zv86fawXjF3MjHxp2gpUbE6wUplP25CBZFHF286iT4PJd3HhtTprEmYwaWXpmcXKDkc3RbnyaXuS04BjiWZ45Sw7b1HjNY0s9t8%2BocrLg0AGV2hdeCXKr44mZadOfxDb5i7OakHxlxyzGFXdBind5aY8K8HBh7C5Pau%2BFqaHez%2FncdmyEN3lAFHh5IRxpv5jUqTAQ6H7wePBlAd5gNfLByMHmq6%2BU9LIlI0EY0dr84hltAU%2BLKbg%2FEgDeFUO6Q9qqWfvW2D2YDEZKR84uQbRe2%2BncHdaSJ8WQx8rUNcOkvgt2IzalUqhitFM8PnTj99rHe1r%2BTpsdVFip%2FQaJPO3GEddH5FQgSoE7cAWNa3v7JHFnprkwLBgvNJuBk0jOlsN%2FNUv4HNVLLXcszS%2BlfMnp3%2FVxC7oqe0Mkz0yJrZcB9r6KJyXa837IgyKVC4JUfDXvrqzDn6eS8BjqkAYRoXhmaixurhNu73gG6UnsUClQhmrvTIqWoWAB4CstMvs%2FU97y1UoiU5H%2FThRGE1%2F1PntJ%2FcerIfquwWmtKazlTtTCTAc9lohMXW0eujYrkT4f%2FP%2FPSfpWbNHXRUzrE9jVd6%2FlC0Pk0c7dSsSvhNPD1Reaz3Uw%2Bp2IIof7ZNZAw%2FC8OvvMmVORoJNT5b9lmjf2kRN6f50BrR3CzrnwdIe4oS7ba&X-Amz-Signature=024580bfac0f718dd492dd78d6a119f80fe5e2b05a2db63b13e52af038fc91df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJRC4K42%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDhSAIIS5oLG48WwKMLU0FT7xiGN142yOFoVALs61RkpQIgQZLFbNxwunaQVroutgcVvjNFvb4rcxeqFkhHdvx3qBkq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEPUCWL6%2F2SvFiuM3yrcA3MpA5jaswBg8aRSYu%2Bmh0dPdBuCsE8LFuLAHQFd48Jr3vNkp9%2Bzv%2FUk51pIBH8OO0%2BXUA0WwTPkOfOV%2FTLn%2BrTL%2FmRs5mPNrcApEG2coAnt%2FZ%2FcC96dFFUEPcX%2FoC6M%2FauYVn1rzbVQgCqBDdto%2F9k2uF2KVcVJYJS85u9vxYb%2BFTMp0%2FW%2BANPcZhOTpd78b4CKRMN4RsO7UtI9KYJnznwqL56OvweqcJpnT7Tz3jhxvRDqnBVNfH76NDQY57boUr6eFqTlUS8wXIeNNCMfFqscpGZyxDgI0GAnDroBtgdAzgF7LTEVM7uwibaWQlB1s1jYMzib9%2FmMW06END4oZ8jnrGq6vP163Y%2BQruQlzgDXhFt8vQo294zSBi2%2FTXIfimXNQqaSKYvFXFnnphSYuP%2FVEVcWmmZhutPvlamlwh9wdv97X%2BUMReKmQzQWvXK2htiwOUk1%2BCi928kfdVDXAI0xfPg60J79J0QypWEo4RmaW66lHaxNypPIeIwzLth%2FGOXOITyy%2BwyA1pKTPa9ytvi%2BCfNeYw8zNznpVNOa2qPKFF8Osivsc1vIuZ6c97qVh2%2BZU2MCmeDFWytk%2BraXUyqd9i1mpaOGWvCDZGQUTcujpT%2BIk8cCnnA%2FpS88MMnd5LwGOqUB7iwMbJDurBljiNcHp8DMSnRHpMjrRJCeZCSqaAoLHDh6k6kRDpjHtHUAh722m97FWcAvItVq1XKkUJZ7L%2FkPDY48f4CMfXVKcx1rZWw53ZRMMBuyGvIOQQ81741IYfGCbJmhr5t1Mx3D7Oz0z5DJh81fgPxrm%2FNdMrqiJXMjPZd9d8u3DJNzoMrmNp6vBF1AJLgL3zEUkoyKoa4b6Uyo8IYBCuni&X-Amz-Signature=e0fb137c4edf1e0b9bdb46e45919a603d6794a8ffa0e34e806a212b91924cf05&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROGHNAES%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDFBYikdAyiuYkL2bbJterEYpHPK4RmeQ0KnifXqX3mywIgSp%2F9zaKZtRZEFx9Gl5GfGsiKoyPvFIcgUPA7mYzkJj4q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDCcStDNs3odFLiN%2BUircAxLlmOn2waWbgAMx7%2FKzkslf%2B6vIznC9aqJOGrI65ZynpVOR7vYDIA6JCKMjJmT1waNfN2glxPOYJV52VSitUbOZ0p4LodLw1Cj6AVz4z8K1Jc5Wuq%2BfftMLv2Iogj6KwSYx6RhKHaqIwHCt6ZwmcHq8jQb3FYL7CG6pluFzOV2hh6fvYADACGpJLKS5wX4W3rC612ZjzYE%2F0bs9Ch0WVjUqSQIGNwP7NP0koca056bap3QqDFY94CfxOx0GtNPqsjasKpKUqsXlIlRoVWr2%2BK1i4YzugA3551cFCqS32UD4RoZYeDW5Glst5Eukx9yIQ7OUr7tCDiPTJsDThJcAQ%2FPf%2FgKj1NhdDJP%2BbJTjUO3X7LEQswqEljvB1vXd0lzsvTuOPG34mdOzZ9pajO45eBVji4kEzpqf9op4CE4IWqIkjALX%2F3jXoYJFppuKlxk5U0yHz%2Bz9urqzUBwDNEoJK9UqV13JbCIJ9x2mroCJxEi6RH%2FTVDo5HXWlrw%2BycaIEsWJv4z5jZ2e5jCUMhp2T9C%2B7bMr4hCs5cZS3nqresZ3nFw2aTTYlaKoK8x6TOBS3205%2BQb4k%2FUSTwCtyR%2BvZOjgU0nBy%2BYumvoe9WvGt0CoztZ%2FrdzqUYSDBC0j8MLjo5LwGOqUB88F7eCW4hD11ye2WaCUVRpH1j8BQyeeWIRvkcBqRgwjbMMCzNKuwYiRynBY9kJXoo%2FP3SYeIkhqz85wwW87PiTRPlavZhXtP4oe7G1%2BkF9YtGmsvXPA8zA597a505PqfmAzCFlGscak1i1krV%2BZW9HbmOvYY80GOPfcd%2BBUE4OBco0%2BjKqGKDGz1gMc0vchzcj7awkuUD%2FMKWk4Ho2U8ndpwVU6I&X-Amz-Signature=45eacb73fd997ff9ccdf83dbcc8a5ea54fc5f365ffac5ff1e6c121559c81ca0a&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GD6NDSN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCbsXkco4KUgxkVU%2BftAS53sMZo3Rx2%2B9WxjkJDrRk6ggIgWasCTCdScKNJ5VoFnVZSo5Qo73u7Hd0j%2Bkowj9ad1nQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDGfHwn%2FnOyq018vsVCrcA3GNW7JKo6n5Fw1Kfmuggj3hHMnKm6ibgcrSLDwBTvqhhjD%2B008xYmmTsTSjQlnXOeoOlaT8ssOJ%2B0ZLaSRBoLAX6Qhch0DmajYaQ3hVA08C2DphsTLi6XOINPynqWYRrb27V8lx%2BDnElmwfE4sZzBYMeqOaC8SsPeZEthMNY6ITLF4Mk6sJhnTmQ7BLc07wUjORjExna88msl8I%2FlJBlRlMZn6uemNucgGQmJEa6%2B3NIpv%2BacqF0t0TTWKEaAo4M4vJ%2BxI9NXs2mzXHpgAoJs0dLnw5LE%2BKoIplH1PBjsBxfuLd8YqI2Blvi%2FvaPuigPI%2BEBHi6Lp%2Fy1PXipH%2FCSMtN9GxC4sR7dNhXHczJLMlUSeIi05bIIRFQUZTIVgH5HibzXRYk2AlN96lhje%2FbzIw2J%2BF%2B%2FSi0YZSq3amV5d%2F1CKBolAdJ%2BvmiTRDkqcLZUsDS2OH2z0tTmYJgk4JEvBII6sffKYtqAyk55XpsllTCUU4WX1cT6IG4VHnUG%2BaDHy8vMl0bLXETeS%2BMPqnFK2oQBEQtFeK8zgbfa7rOdqTS20SzOW0KblGqFEDDvIwV2dfk5%2BiKCbAQNAoNWuqGONG2%2BrMDT8S8xheakR2Nu27fAng%2BDjqUZCFtVKE4MPze5LwGOqUBRRLVWlS98jQFgVNgcORjb5txCcBEUOglbHNdmkXjY3Tx6rneRZA9XnT6SBYWXLdMAQznORAITgjQqIY3SZQ6tZhF73E1%2B75grtZ5eGQwJLR3CQnh5wwSGFitDK4d7%2BmRPbMU1Zvyo6r4LHuD80Xkhft%2BatEx%2FnpSUlWsj3IXNuu3daMN0nNaHQgiJuFbJJuuH6EJnbWQiP9eDH%2FFGZsTJNSNYXwa&X-Amz-Signature=960052ca1f9339f0a5e718c58f0e0d67f34b5e833c6566a0541763dc6750800b&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JLBOREE%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIH5GI3QyEpKNbwLPoBmILVRgoozFPLUbESDfEOGAU9bdAiEA%2FuwsaGgdU3PHuwoKCYJn88uznhmQv5hoDHw%2FKDnpE%2Fwq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDFwP7CljlSvBCnByOircA4N3ztQiM%2FxNAcMehX6dLiZygEjmZk7EckDTbEvBRky6kntIYffrwB0rOOodBWaLZYJ9J4bXqOFE%2F6zMdaNH1AsVjBcFMQulqfn3rx72PTQghIQmnzzqivCKr4v5WfxtYMYAC3c%2BMMfrtwR1%2FIHH%2FDRPKBBbydjrClMXbrAggysc3K%2BlgFoGVkKad11znAPkStmgap9DT4qcda%2BKNBG8sZDeXOOcHUSYadExwqNHAm1q9qiIaVhIAHO4vGVfWxZumUW7Fw09I0LfKXrV1y9oqXhJC3VVJoD7veEBqK4U%2BhdtD%2BJPghpyjomSmjCY8de2IcLobTymJglmzvPLzD7heHSfnlfRBF5Lh%2FEcQ80b68g2fTJfNJAWqRbnGyo4WHEAG1%2BHxlW91TFi%2FNpOBGi7yoIEvpUFw5TW2wX1oFdSo%2BtwT8C1XosKoWcm8OZ7H6Fv1mz%2F9XYx0DJ983SPU225q%2FSqP7gfBpStYPGQYwua3c%2FaOyvUGtiNe%2F%2Be919edkNGd6hRnQGHm0Mk4sGgsixL1gkGpDRFQjaWWjd5TRnqgYGkTUxxsvpA8RsHNKE%2F77fmJ1QJvLWCOPr2sIkTmUxup%2Bxt1VpnEASHR6u%2FpXgs6e%2BBjbd%2FvoDwBxUoapUcMIrn5LwGOqUBVMuXw4X11cBVlvyR%2BQ5ywJAOSs1cyFI2ExeEECGKPI1wd0nVk3aCJQXuYHC4v5tO2uA0G4RMMOy83I9Kbv%2Fikm%2BWEnNIql1KPcbPf6fTyTPVojSQgzFuqwhVGjJg1H63gbEIWKjcSF0zNw5ryHGY%2BC5X44rZpzNzru0XDgk2Jx6yUXV7PsrXLZwvoS%2F%2FsDKc6dZdQFKSOfc%2B%2FSFfDumzmAnjTWhI&X-Amz-Signature=7f905dffbd8b5b7f98d2e7cdc09e5121f63cb637f06bcbb634ecf5499d56c951&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJRC4K42%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDhSAIIS5oLG48WwKMLU0FT7xiGN142yOFoVALs61RkpQIgQZLFbNxwunaQVroutgcVvjNFvb4rcxeqFkhHdvx3qBkq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEPUCWL6%2F2SvFiuM3yrcA3MpA5jaswBg8aRSYu%2Bmh0dPdBuCsE8LFuLAHQFd48Jr3vNkp9%2Bzv%2FUk51pIBH8OO0%2BXUA0WwTPkOfOV%2FTLn%2BrTL%2FmRs5mPNrcApEG2coAnt%2FZ%2FcC96dFFUEPcX%2FoC6M%2FauYVn1rzbVQgCqBDdto%2F9k2uF2KVcVJYJS85u9vxYb%2BFTMp0%2FW%2BANPcZhOTpd78b4CKRMN4RsO7UtI9KYJnznwqL56OvweqcJpnT7Tz3jhxvRDqnBVNfH76NDQY57boUr6eFqTlUS8wXIeNNCMfFqscpGZyxDgI0GAnDroBtgdAzgF7LTEVM7uwibaWQlB1s1jYMzib9%2FmMW06END4oZ8jnrGq6vP163Y%2BQruQlzgDXhFt8vQo294zSBi2%2FTXIfimXNQqaSKYvFXFnnphSYuP%2FVEVcWmmZhutPvlamlwh9wdv97X%2BUMReKmQzQWvXK2htiwOUk1%2BCi928kfdVDXAI0xfPg60J79J0QypWEo4RmaW66lHaxNypPIeIwzLth%2FGOXOITyy%2BwyA1pKTPa9ytvi%2BCfNeYw8zNznpVNOa2qPKFF8Osivsc1vIuZ6c97qVh2%2BZU2MCmeDFWytk%2BraXUyqd9i1mpaOGWvCDZGQUTcujpT%2BIk8cCnnA%2FpS88MMnd5LwGOqUB7iwMbJDurBljiNcHp8DMSnRHpMjrRJCeZCSqaAoLHDh6k6kRDpjHtHUAh722m97FWcAvItVq1XKkUJZ7L%2FkPDY48f4CMfXVKcx1rZWw53ZRMMBuyGvIOQQ81741IYfGCbJmhr5t1Mx3D7Oz0z5DJh81fgPxrm%2FNdMrqiJXMjPZd9d8u3DJNzoMrmNp6vBF1AJLgL3zEUkoyKoa4b6Uyo8IYBCuni&X-Amz-Signature=a7d691e02a0938928dd87389cd29bbd351b6454c83d276dd4b585a029b1e3c0e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3Y3LXA3%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCiMP%2FTVHvGaAeHpTjyn7pY%2BPphM5XKFA9GxGz2JDea7AIgb6i72QEA2lVifhBRZnPLlVFMVU8HDMffJugD0TBIkgYq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDIpY8JTVBomalOmmvyrcA2DR%2FjuCgV73veEGqbdkG73HOKaLZx38WKKTLWtforRdC8r8QMhZv4zIE9jkEsqc0PHSJkXWVmvFlFjqyNFSjq2zrczEZIG25XC0qMRz3DrVmovgPNCZ6fQb3pQqQBJXUsZ8kfnfIXEbeMRcOwnyhnP4Ln6eDcoiOB0aiYR4yW2IeOp6pWlrhMY%2Bd3Ext3dixsP27i5uptMyA3lF01kVq0AqiYJ0rc47STJBa3CGeCI0qz9ZLMKOZgx7e%2BARifVmKil4r7zGSIo%2FFSJk2Q6RuRnSc4NRCe7avXUXHL46ouVCycM%2B8pj4W%2Fx9Z4XXT2v6HAaJjN8YU0cqpUkugBMm%2FScQT%2BP5BuQzDUr22by0YHhP8RHpEqXwWxu8kV%2FlEtKIW47sb8mEngU4PHkHP9UuMsn4LvVaQe4wysq3CaE6seiaBggEezqkb7ITf0kqagJAYFQL3Ux%2F9qnffDl1H4ZCzwpKjzgxWqlFg%2Brk02naaEplreSnMuoQp6HmVzW7x5ygtuvh13DQMKp5GYhpZQcacDEvETa4zbKzOt5ZgjlQc0ZjoRXEQVM5B1VmkHw4T2TVFlMQYLtplsMVRVZ9H66pxS%2BaX3Gmyr7UJZa4l4gE2RGm3nZqfV%2FQG4I7Dhz%2FMJ7n5LwGOqUBmNzCsT84xV5Mul%2FRd85WE623HNTi%2FYJIKk5dPVhQwvESMiHdF0ou34vf8xsBS6gP4ea3f%2BHNyKuNf4R0AM6veDxYi16I4q82%2FbrQEM9xmHy5QqGpJ64mSnCVei79WhRxeuTMe%2BOgXVy%2FjfTVaBDkCg7gGTgV0nBkYwrrkzSBDi0uRjcsVaS9lpsuRrgoLQcTN5sc8bUfub5qx5O3fPw%2Frqd8rqzT&X-Amz-Signature=0cc570ff3f80df37b1f02dfbbfe1bf1f3a0e3d8bc8bdf4a41a26d6968700b2b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3Y3LXA3%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCiMP%2FTVHvGaAeHpTjyn7pY%2BPphM5XKFA9GxGz2JDea7AIgb6i72QEA2lVifhBRZnPLlVFMVU8HDMffJugD0TBIkgYq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDIpY8JTVBomalOmmvyrcA2DR%2FjuCgV73veEGqbdkG73HOKaLZx38WKKTLWtforRdC8r8QMhZv4zIE9jkEsqc0PHSJkXWVmvFlFjqyNFSjq2zrczEZIG25XC0qMRz3DrVmovgPNCZ6fQb3pQqQBJXUsZ8kfnfIXEbeMRcOwnyhnP4Ln6eDcoiOB0aiYR4yW2IeOp6pWlrhMY%2Bd3Ext3dixsP27i5uptMyA3lF01kVq0AqiYJ0rc47STJBa3CGeCI0qz9ZLMKOZgx7e%2BARifVmKil4r7zGSIo%2FFSJk2Q6RuRnSc4NRCe7avXUXHL46ouVCycM%2B8pj4W%2Fx9Z4XXT2v6HAaJjN8YU0cqpUkugBMm%2FScQT%2BP5BuQzDUr22by0YHhP8RHpEqXwWxu8kV%2FlEtKIW47sb8mEngU4PHkHP9UuMsn4LvVaQe4wysq3CaE6seiaBggEezqkb7ITf0kqagJAYFQL3Ux%2F9qnffDl1H4ZCzwpKjzgxWqlFg%2Brk02naaEplreSnMuoQp6HmVzW7x5ygtuvh13DQMKp5GYhpZQcacDEvETa4zbKzOt5ZgjlQc0ZjoRXEQVM5B1VmkHw4T2TVFlMQYLtplsMVRVZ9H66pxS%2BaX3Gmyr7UJZa4l4gE2RGm3nZqfV%2FQG4I7Dhz%2FMJ7n5LwGOqUBmNzCsT84xV5Mul%2FRd85WE623HNTi%2FYJIKk5dPVhQwvESMiHdF0ou34vf8xsBS6gP4ea3f%2BHNyKuNf4R0AM6veDxYi16I4q82%2FbrQEM9xmHy5QqGpJ64mSnCVei79WhRxeuTMe%2BOgXVy%2FjfTVaBDkCg7gGTgV0nBkYwrrkzSBDi0uRjcsVaS9lpsuRrgoLQcTN5sc8bUfub5qx5O3fPw%2Frqd8rqzT&X-Amz-Signature=49503f6f84b543df92ae010b899ccab3ba6ec3ecec4b3e150c06734d64a5dc19&X-Amz-SignedHeaders=host&x-id=GetObject)
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