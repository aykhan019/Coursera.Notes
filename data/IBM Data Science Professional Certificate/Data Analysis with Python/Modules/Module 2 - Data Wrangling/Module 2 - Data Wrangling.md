

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNPZJWRM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQD3ch6jCWv16z5ICvuG%2F2NaAIzpeQAsBIUiiX7BRAPDGgIhAIQ9fM3o1urpjsPwAHxTbmE9Vvxxa3%2FMmeuzF5GX1ufYKv8DCH8QABoMNjM3NDIzMTgzODA1Igzva8Y9OJsw1%2FXcyfEq3APQRHkmDIoWQNZLio5VuDTuCcztmaWHZH5tz61wWCePf4Deie%2FRDDWRMHZDGKr4rTcJFug9wkyUfvZoTpoNJJQJF7ZbTQb46UCLFFiXPU6YiSNyD%2B0lbvJaA9KBJOEpm5rBA%2FlpNGLLK3svLaqTxs375gS18MmcCQBBSxvUE%2FCATijc20EhSTvFx2dCNablG6JpxhmkYeCWr2LYw9nsJJPuIlFpnZUQpSHdhGIkD9BBT7fWJtCilegRzKAZGBdm%2BcTLk%2BgAD4wizoZZSxsMf0axO5M%2FTrVhd2T3fH2i3hiFDUmz%2BdncOv%2BqUD25A0ZQwE%2BWd%2Bnj5ho2PL5r9eQLey67iamkv4%2BxmuGlSb5l0f4yVtjO%2B94RqQtaXULU%2BD19UV8F2k9Qf5t7IwDqTQ9YfJJ2g4zPXC%2FDaakhmFeSC%2FcE93kOZhQ%2FuvBxCyAkV%2BYxS6ToP1moh8XMraxVOETZ4vA4KXg3Qypfs1D6yQh5i8PVVjqPzMiq92dtVPLp0bycEo%2BZPziMt1iyK36YKpYtvGCg95zK5aQ0em%2ByLkKkg5RSRE7DWeVEh4IpSVRLg%2BVQRN7uJ95x2lCUJ5%2FT1edEGtLFPVnncRR4COanZ8VlZxgKsCdZ8QueycYTDnYYMzCy%2Fpm9BjqkAda2wfX8HxG1RK3HxkXKcGI6IE%2Bo%2FZqBX%2FvnScoYCnpXoQQGYL3njYlUTvzMq7I5H2dHw07MZVXOyUg9o8QxtllqMgDmnf2TDyrk4N6h7sIqIQQ2Smj67x7%2Bm7db5%2FOQBhR92H9FS9OJAZJa0V7Tz1%2FG01gG%2F52OJpHLZvoU5WkNSoDCjlu%2FRoAG%2FHdf8ghyA%2F%2FqEpmh9sif6RndTTZz1cJfovDw&X-Amz-Signature=ea43ef914ecf4f0481aeb15de62f8fa2bbe0e91af416b45b9aa17042c14a312d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666R7AKGIO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCp%2B8BEQRC0H%2BhH08sNq8wOJYJr3nhG4wqv4H%2B76HfgyAIgA3yakoWQJ%2BBEJfqAyto8SlMAJT1tqnd%2FtzIFEuLV21cq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDJDlK%2F4t2fxhU%2BHNySrcA8mldbY5Y%2Bhd2gR%2FMarD%2BbzWwNgoL%2F8pWHp5DmTEjedtP4qvvQPhyXw9EueKs4c9FTp6%2BvOCcb48ma4QiU7cAY7znmddTfLfvbwPmTy5Yl0T6WRaw%2FZ3dSRxNrZZ%2FimbmrFIc1J%2BCgf1OhR%2FMZjvolT16E99kMEqJgES2cU3shDQ60n3bjOWWksy6bBwfaZNuGRjgLzjjoeHfcXEvkY046KIVoXM6OlQj1PGr2CE9SGbJcPgwPKfy30Eyw2FHRpgaHX5QV3XNDqSVKQUHE39H3qeEbZRZS8sr%2F%2F6E2zdvQibdXHRGP3lXd77ObrtjaOxADxyhxmDvh2osW2dUxJlbsT7qutdF9D19im2YiyaciEyqJ9ihP6NfghkNv1C9ITgscsidWnHI6urmEQ6K3Glg5gGUjSAIRUWGGF0ZWj3v8eU63%2FE5IoXV0i6zC54LOwckSdshghN%2FcYBvtAkmmdZ4XBWAUG03NN7LyGde1nzWYKnqL6oiAaYTrWzesJdWAKhe5oMl8lHy89mjR3lk0wHKrYZY5NXEmlR9ciUjnvUbHen50RhZPcBknBABfrPuP67lZHAcidhFYppIbYd0Nne5WNl7mid9xTr7mXDDG7L%2FwhC%2BdVGnA%2FJ8TiIL5vNMMj%2Bmb0GOqUBG9c1tH5B3cT8yGo9h3hQNtB5G8tzi8PtC1teQU5GejFqJ2kyZhnGS1k0t1FitgsQlOoEWeAtGxkwlWP7SisppFyydeRJJD1bKFrxBkupypbUk0mcjd4nmCMQoOe6MgKt%2BDxOao6fsuv2zyFuetel90O8Euaorm%2B50Ngq7iS2ECxSPAq12cvHCBZcMNJdp%2BGP%2F6lfEfa0wsflyP9%2Br4UWn8tpXh32&X-Amz-Signature=58066b47caf8c33d34c8b3b58b271fecc7afbd9903a62a226694be41ea8ce6cf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEYBZ3H7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQCrH1jLDE6ZUrndV4n3ewaGeRW71RnRwfQ7Rj7VjsuyEQIhAL5UXI2TIk8dG4HbDsT2TvdDno1r%2Fkkrys93%2Bp6ZaxWGKv8DCH8QABoMNjM3NDIzMTgzODA1IgxDcqtX00T87wqQOYkq3APVEJqHlvp8KMqq1%2BkRfvxyt5Kb3VohCRShYXSZfiP4EbjYBS%2FMHUm9vTY%2BM3W%2FiqoW7MvwBnDY7E4bGL%2BwrKOjJDzeNAJrr5XtUYhjOXJgD3v6arN1eU3uIPrxnlVJt6x88eRGQv6KkvOsYVnoyyCQ3cFEphOc3F5NnnsPXIQcguSCEFlt9OLYyAX0tH21sgpMGfX0oSrC5dn7hI2o%2FkUd4ewMAxEkRzNMo9WjOCVQ5VdQTPuUex5416MFubGNAc0AAxpnoVWh9OvaW7O5mAOvTfLNdf5v9jmsO6NekOwAuMK48hbh09tTSFvGIqc%2F3HWBXe6XAV1uuw29woHXKCl2elN%2BkO6u%2Blt3dUVV3pCOygnhcLmt7%2FG6tNdiD57jSaWQF6dWWvvDU7FKI2JehrmyJvqzq7VTZyVDmXGJP6TckHWgmOWLEAtj5ZyB%2Bl1woW18VpMKgTr2tluabCOi2RAPB8Cz1bekz8Ird4O7G7T9wowBWzG8z%2B7nkMw34wZuDkd02XJIgPu5RMDhbvmgW6A7iVV%2BRDHixrk%2FGzo42oLaC0bmB7usbo11OuJO%2Bl7BHIeXXxsqEGOJvFesJH58jywZTyBKQHAE84rWsgZZ41degSoJFhe2e3b0IbusWjDl%2Fpm9BjqkAUS60C%2Fw7UOlDKEIOsvCluzceKmO%2BEjDdRCOMkgCLt3TDTP7GqGrTxONRsf4Ik6BflGrHSTfHbl8hqH%2BafV3ZTNyyJj9T7WaE0V2NmWXCfl8bkCmJVRXRnkQ5vA2TXJKELmKKMy2201s7mSv3CwTnMtxq%2F3%2BHtvuVDim6winzOv4HhljlRZQMQWKL9yZml7yDEEmav7RqyOgD4qsjO2RBSLHgn1M&X-Amz-Signature=89f27320cebbdd5781e7deff0756a19898fbb6ff3a6b6ab42db34febf199de92&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DRMM7SR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCDaJm6dMj5qU1iGUsrUqYUGYGeupDxIFsOiy6vR8%2BbsgIgQkG0wRcC716rvsr8OW2jaPQ%2BJst2Zn8rMRr0CJ73uIoq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPGtp5p0YapsIgd2hyrcA1G1ekNygCalkSV9aNGPQYwVuzGfi%2B6WxijrtypjxkRSOXXUGjo1EXZWPvy%2B05LPMRlZzGeOfWVDqsD5Rm4IHVwawkkpb8ta1qj70dEfbNHwxuIuUgaRpZWINzmJZaYRAs%2BUUTUo9wdTfceRooqfTpgN9v7IGZfOMXJpJjXEAzQdc9kepU0crYoJiHMDyUKvpXpoiOYJGsE1aD%2F0ELjxmbfUsPiOofQ2MDMg%2FvndksepAP5%2FdARDtmeCaRzI5iMtj3bQJ4IZzgSrozV5WliQ7qyfs16Klm3z%2FFK%2BjZFzLbdqFdfigMFa6VEK%2Bc3iShgWy8nG8l9UUPfaHr%2FAkxtrc6xkH%2F0ucFVCcM38MGyXNfG8iyWB3H6ntAtanF9OegwajWN9nkMscWtC8l35vlJLHwkF66QFC4AIcwHHWZRnY4BNX8RksI4irwW5rVGTXaLQfmt8lwP9FvlYkHe2esYGu9Ec7j0xmYPgbubA4ovDdD%2BeMFOR1Sh%2BdrlNzaHX2si8fLH%2BbYGbP1UC%2FSBNI%2FDpgorIXZa69kfQdEr%2FQEiWUE7RRhPKf%2BVQDWU45IRdImQw08no0zdzlWrUar%2BVcS5fvHyPaQyx2IQnQ6femGhX7acZYwEqH2CX3HgKgDCeMLz%2Bmb0GOqUBqaR4%2FYkAkU2jfN3zCC%2B0kIVh04lZhHTS5ZVQF2qt4vcJuGRXELsDty0FNcnDzkZnU4lFANnnRTXrcL6LCjhsGDHo2r2s6jil9px6NTyUHbNd1lfqgf4wazk%2FCkJCz5pSQthmn22KRSj6TD2%2FpBC%2Bg1sD2pT2%2BfI7Tq4AvaI5ffQp4KfWhngEueMrSS%2FUde8w4VCEi4RLgR2T%2FPt1dKrhVCQicU0b&X-Amz-Signature=6dd7b872ceb22816d1dbf42de1dcf230bd5c5b3ba65123866208db8008a8ae26&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RS64P5I%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCsfgCQHUWWo7KVeocvFLESvjZJIvdtFjLQMFIm6h%2BKbwIgGBvkO3RXI8C6attrBaSIQIPlIySQZHv78%2FvX1EChmJAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDLk1t%2BqsKxqyQskF%2FyrcA%2BulosWNJYvAxY3a2y4Ulo2wKjNlqJxW2aoGongu5%2BfZTTzWYkQPFJEU9I5YRKuoIIADbsk2Nxau7a5yWkIStbCPzhB7rcaoMUdPwn8fn7Poz3QYighP%2BAk7m54andD6%2BIPvHWvqeK%2FLwwYN4k5IbO88SVRXXZKQ1woSxy6B%2B16iO59oKi%2BVZ9s8m9lcGJ%2FfFQElIivetZgEBFI%2FEQx3XrzH1SPMK2yE52MvWO0QaoAYL8pRnsQ7P%2FR1av3YcB7%2F71MLmgklDj8Miu1lmNxv8yOIQq9y9mDsVJwdOe4efqgXgbgs0PU8VAjeLszLv1MXuRyRSUVwyOFkPhWGq4NRsZddlx4nxUVTImZulhazke%2BodWge2rr8QAHv4COb52wNMBh1ATLFeJyN4qBvcHZmpyKnrBkdDgNX2y48b5w5DqInozX%2BcTH2gdZ%2BtpeSC7y%2FK1Zrp1WUv58ojfFu4n7fGoPx6YS3VO%2FWrCiLiYn%2F6Jj3uE3Y3AfuLlDLVCox8cF9bu%2FbNqfwiajQ5aAff1oKgKOoi12RDZXLqfpLwCXR9%2BQvCznV0PTuDXUzia0LK8KsGpmzAH13LAraRoP1yynwBX1KIS8uTJRVURwA4cM6oqCrbGXCWTYJb3RM9qHQML%2F%2Bmb0GOqUBpKFIEOoMdWM9KKi6JVUnGmGkLaCj0EsY5Nrn6Ae3UI9iJMpQ%2BONzQ2kenBcvadYm9PV6b%2FIA4wtVNQRdidJXbypINWXanAgLij9MEbXsHoiUqQd4vciMHsJG1CJepAE%2B0uyJQgfQnymxUCVjQYkii%2FF3QrigbhyAWLohrbsVW6Lz3KhmSsLC5gky%2FlOLhB0WHl4E0Ztu02WZ8EUCE1kfgiQq7IaE&X-Amz-Signature=c4d70b04f85368eddad50b4418d14a6b1dff00f5f08fda7e2aba1458c542ac52&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664REGV3QO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQDIcUxg4CaEPgf8%2BCen5j6z9D4wdaErAT3%2FR4iEjcGUvAIhAK1R37muug2zrXrxsnxpcFfRayYiyTm%2BRkm71vwbOTyGKv8DCH8QABoMNjM3NDIzMTgzODA1Igxrm8BM5INIm1AlYBQq3AOswiATA9P%2BV1irzcx%2BXmsEYrnNPtf2CqGDzlc3p%2BQI9WPI5EX7BDN3XR1TitImuJ0qlzsmutpaACW9d1taCB98fbzjKQWusWPEMo5IJVMR%2BCL%2FM5SIJcWItyFNnGz7DWZWxgnT3dRNFiEzj%2FZj0Kgv554fqS2gQpzdQFw1JhScHPz%2BIKtOyqmtAzt%2F6ZEmLKIRUaZipqdogxzAPlgK3E%2Fcsj9IvCE18JK21XlgoJUHQGay79S77ZKzHLIDnaTqRva9icg7VSY4A2ZO1nDt1gRbuWQE9U6vmRr3yNxung8afvv66hKR6Ym1%2B%2BhNGuHIlW431VQgfQIj45mWcWsODkVdDQo4mD6w%2Fx4sqc%2F3FP%2FTaMugxupk9%2FT07BqmzOW1u5ZJVHA0G%2FzBENAS5CtCVswACnv8FToobfsPd1g9uyucpKhh%2FMiFxHKGUZv1nNDlX0GDK2a%2FsPdyndAAkDWIdW7RBm6tCH%2BURyl2gf85iazlWNoZjMvS0BRcC2YQq%2B2cyF3ABy93Y2dh2J81laBwic%2F0riP1Jv0gzTnNFUFmVKnZy4hg1KbRlBAvvxxoXdE4PyMuyi3y5jM9luDTFFr9OxRDkcqlSOww%2BtsNdQWkF3okeVQea72%2FBJjO3hU0MDCp%2Fpm9BjqkAVTE5AOZZ6KeOQV%2FO%2BjsHuEtVtlBKGxwom%2Fz1bWqDXpGJFtdeCDU%2BfHFVLPyVukwfUzAV8nrnhiu9j8E3cXGAmBIK4Escaj3VR6LKxpr%2BH25JC7I760oc0ptlJFbCAMEajz6Pchy3WeBk3hRYqC3nLODA1MIP9g8JtIPM69YoBRk15JeSjhlG0YoQ0VrbQEQ4xdwZPT2w6xzeX7ia7ube6VsIm3B&X-Amz-Signature=f86bf133938a9fcc73c583c8cd81f5b214e41852d188c9146fb0263c15d955d7&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBVPPTZZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEKDeT4AHK3%2FnyV%2BKvVZfLIncpk%2F9we7hY2%2B06btcnDUAiEAjCjWQmKkamJ9LlVGCjwG8meBjpF3hU5uOZfr9xn0P%2BUq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDKCsCGLWcDbxqwR6ESrcA%2BlU40J4oJzsfbaE4XZNLxpUWmazvwSygIjaPoIUVhS4lb4VXlkCUBu3y6md6hKY6pn9pZkPgh1yxsk0b%2BWVEWoWaYIrSATYFjL2kSJHnlJqwn47M83Y%2B258TGC8Pm1n%2Fmc71hSsbntsXrOOmMKLHc%2Bl6wZAWTn8UIJ6Dz25l18oD8CFO7nol0YU%2Ba7WPV1wvzm7WgQh7hx9QRQMvZEQmLeW0b3vjmTKDG%2BykH%2BTKSWElK6Nkl51Ih0KBcW6CYq3Bifv81jclSMbVo%2BGldLKgrDGv00K9znYch8SYycGyMwfyv44pwlmfdD3KQL9%2BImO5d154hnerEJLqHMdZvdMr0G9bqIom%2BpVE%2FwESI3FyhJt0jX53bOqWuFj5NQwA%2FS278SgbB%2FrRvEIeS8wXZpwsuxWUw5PfAZPMrJxS7%2BfHFvl%2B5RRmlj2fHuGYemlcGOUi8LHhlO5a6FtkkMFybn1mSZYSER04XTKbq%2BcZ1jv6Wf5EjM%2F9Ea%2FHk3%2Fp8w1c5r0KuypF%2FiBRZhfDNivYwIG1m8KWw6WnsNuW2J1Vg6PxHUJaONP1FTQ8GmfVsnB6H%2FfCPyHtz7sGerJTNLyISfqWIAgKAespq8Nvzznuffg6Ck8KvIwOkkZyPAf9PBdMPH%2Bmb0GOqUB%2FI6KoDIoyg2zY0vDE%2F5XiPQP0u9%2FELu4zas0c9q74pmKqXUWW4xV5%2B6yZZBsLiop8vZ79jZLkMWFnY7xWpn04gO0wXGG0QftL8M%2Bf7IzuLIXPoOAZQ%2BZJrHxql%2BY8gPTfcXWG8pWOB0AHl9fWeJR3kP22cmipF7vUJEmXesHl8gnCUB8K%2FP%2BEhhc4Qx7kI0mxuIulcQRzmIvIsMirikC7xMcEJ9G&X-Amz-Signature=17425581230579aba4f56e55a718a8815e379d59171bde2d744abeea11757a09&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662O3QLSQO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQC4h7fXOjzEShP1BnEP9MGd6A8L%2BtpjmJd6GKKPEYGy2QIhAJ3%2B1A97%2F94e8mmmsUPkBek%2FE6Sm1InufLQpLkyYnmfdKv8DCH8QABoMNjM3NDIzMTgzODA1IgymDzvwoJerohC%2FgZEq3AMzL0lPeN%2BZf9GHAmVkWJrB7lXdtIndlrZWhYvaWQZvcuChdFsKU2VDZnpug90q6%2FKPcKNeonKr57d7G%2BmdjiW7h3JxdY6QtvtNzhdwgwPLK9zP411rpm5i73i6YopPtzh9n4r8%2FXbjVxYoqC6k2kSIm2AeHWysXH60ZUONCbQGwE%2BGan4%2FT47ZpR5YBYYQUK6M8tc4ujPjoDug5TmWEThdEH6zg4brh4vh5PV3%2FPXhbbmAzh47L%2BOsbdFCICOYoHof0g4pvJflSHdxlX1%2F%2BNFaQ85FhhxV7Dj2CGFC2WcbCXNSZlbJYiFiIuzrPdqbnAV%2F7sz54GnTgtX3%2Fba3ck1crSI8iFBb1ipUC3C9Hr%2FpYXSjSTE0IcI1ItOun1E%2BXM8zRVDgZubaL%2BZFIcs9Q9Rda5eO2Tnza88JfF6xpXnwpvQg%2FZmk2nD2uIeF70AIDrSMPo9tLQOdyY251u9x%2FO8P5XY0oO8Iz0bHbfSTsiGYBqWo49WgiTwmnTGb3U0h97MNBTPEPE1RRedbuXpJZnODF3yCob1LqsZU6RSvyW6MmMRcU85SeGw4SXUAno0GWblj8MBfyq%2BkOtvevcfU7SAcTXNVdMZnaf%2BWKAJ%2FfMrtGbfkMNWJCmVK5WvmezCy%2Fpm9BjqkAW2DOPfTULd9uaJ0Q%2B4kmDSTj4qlPXRthJHxDowAT1ZWtzZNwLctSgkn9ae56zXNEQq9ULeeRCA2YU%2Felp%2ByKLQ4afx4gYyJW8AILQxw%2BCsfRg8fz6hF6nDgDrwTiV1algfB0pbYHqOBtkWo4n%2BV93wtE2oLXBL0eBYPamipMMOFQuTVPIcm6KMcAmnOqlgJxqEsbsG8JbDbeYLS67TW0YYbLGkT&X-Amz-Signature=30e0449006eab008797b9b8555e7615d4af021d4d3e06b8c1d30ed5de7565f67&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RS64P5I%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCsfgCQHUWWo7KVeocvFLESvjZJIvdtFjLQMFIm6h%2BKbwIgGBvkO3RXI8C6attrBaSIQIPlIySQZHv78%2FvX1EChmJAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDLk1t%2BqsKxqyQskF%2FyrcA%2BulosWNJYvAxY3a2y4Ulo2wKjNlqJxW2aoGongu5%2BfZTTzWYkQPFJEU9I5YRKuoIIADbsk2Nxau7a5yWkIStbCPzhB7rcaoMUdPwn8fn7Poz3QYighP%2BAk7m54andD6%2BIPvHWvqeK%2FLwwYN4k5IbO88SVRXXZKQ1woSxy6B%2B16iO59oKi%2BVZ9s8m9lcGJ%2FfFQElIivetZgEBFI%2FEQx3XrzH1SPMK2yE52MvWO0QaoAYL8pRnsQ7P%2FR1av3YcB7%2F71MLmgklDj8Miu1lmNxv8yOIQq9y9mDsVJwdOe4efqgXgbgs0PU8VAjeLszLv1MXuRyRSUVwyOFkPhWGq4NRsZddlx4nxUVTImZulhazke%2BodWge2rr8QAHv4COb52wNMBh1ATLFeJyN4qBvcHZmpyKnrBkdDgNX2y48b5w5DqInozX%2BcTH2gdZ%2BtpeSC7y%2FK1Zrp1WUv58ojfFu4n7fGoPx6YS3VO%2FWrCiLiYn%2F6Jj3uE3Y3AfuLlDLVCox8cF9bu%2FbNqfwiajQ5aAff1oKgKOoi12RDZXLqfpLwCXR9%2BQvCznV0PTuDXUzia0LK8KsGpmzAH13LAraRoP1yynwBX1KIS8uTJRVURwA4cM6oqCrbGXCWTYJb3RM9qHQML%2F%2Bmb0GOqUBpKFIEOoMdWM9KKi6JVUnGmGkLaCj0EsY5Nrn6Ae3UI9iJMpQ%2BONzQ2kenBcvadYm9PV6b%2FIA4wtVNQRdidJXbypINWXanAgLij9MEbXsHoiUqQd4vciMHsJG1CJepAE%2B0uyJQgfQnymxUCVjQYkii%2FF3QrigbhyAWLohrbsVW6Lz3KhmSsLC5gky%2FlOLhB0WHl4E0Ztu02WZ8EUCE1kfgiQq7IaE&X-Amz-Signature=7978a62d3285aedbbd8ec4f4514f8f0a4e987138e127d0cf72651c1574fd81a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOCJGD77%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQD5K1b%2FbsXFStyOn1mtt1kjz4QgNoI%2BptB00eMZI8R2JAIhAPRcrPhxo8m8GpeSrfpDSeBdy8dNtsYFjEqiSjWPUufBKv8DCH8QABoMNjM3NDIzMTgzODA1IgwM3U0IqGYJrVYJjLkq3AMtwCBaj%2B%2BJva%2FEeKbKa%2FlJsAUSlyppI0fstaJK%2By1vj5vzq94s90iNQdzmZj1VSFNHqeKIDtSbVvO7JE4XKcNeHrZvi5gELn%2Fx7%2F4YEBownSYi0MjTewEV%2Bxx2a2cPmKjT%2F9y%2FEGdKuSOIvrRM6UNMMzfpZc9z9er3Vd7RaW33slQUwnEZQmORfvYDGTGw9mcQiZoWcG%2B0bNEQ9GvaKEPrbwDIW0cuP8ZN4gZWXBUtGoq%2FWvsdRlyyKme3q0MSOCLjtCKwwy74XIpfoEVaLwa7ponTOJJKuCsOENwnsBKuDqJ9LWFvd1Yb6vCNqApdN6%2B0YZ8%2FgKLu9w4eKBSK89yIqgam65SvQ4DzQitUKP8NKUs4YEzcuy3EXGxRxingVsQq7wGsw%2BbQLBe1eRR9EGMFifdx%2FmjtY4WN4youHgCR5Vx13NzppEeE3IrSS6TTrmCIlo%2BG8Ri%2Fs56f2YcN0TZZTZZyGbp7UsJl4qkgFiDLUbAVsAF7DH6jHAr1u7Gl8Yv0fHLu4xZtIP6WOph2wAkEt%2B2fda1dDD6CA4uvViYrl8OFGIejXlGo3%2ByN5A6ZlYPsa74PiWMXxw6nuDQMbRf3zgWXYC8%2FVkrWzZ7hNvL%2FZ%2ByD9o8H27D8qjjMtDCe%2Fpm9BjqkAUnkYOYbYWIdZ88AwFcapFarp0yAXZQcHAIhkJsxv6j%2BgzvE1qQ16OcE4I8xD1%2BbQy3y%2F4vCFx7QaMFjjiIcqMxr16iI2j7pxTNfuIEWrcEQdpkVOzn09luCus3AIXeN8qXxq%2BCbtRlT2FKflG7%2B30vsXWPUPlULzHfaXplkEy4PsMKhvprwmIWQh3SMeTRF1uH1fRiw%2BYGOu%2FosnIRB%2BMMYY%2FoE&X-Amz-Signature=760c15bdc5c4be5583a23106766a0101d52b2b6723eda074cd74c8563caab336&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOCJGD77%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQD5K1b%2FbsXFStyOn1mtt1kjz4QgNoI%2BptB00eMZI8R2JAIhAPRcrPhxo8m8GpeSrfpDSeBdy8dNtsYFjEqiSjWPUufBKv8DCH8QABoMNjM3NDIzMTgzODA1IgwM3U0IqGYJrVYJjLkq3AMtwCBaj%2B%2BJva%2FEeKbKa%2FlJsAUSlyppI0fstaJK%2By1vj5vzq94s90iNQdzmZj1VSFNHqeKIDtSbVvO7JE4XKcNeHrZvi5gELn%2Fx7%2F4YEBownSYi0MjTewEV%2Bxx2a2cPmKjT%2F9y%2FEGdKuSOIvrRM6UNMMzfpZc9z9er3Vd7RaW33slQUwnEZQmORfvYDGTGw9mcQiZoWcG%2B0bNEQ9GvaKEPrbwDIW0cuP8ZN4gZWXBUtGoq%2FWvsdRlyyKme3q0MSOCLjtCKwwy74XIpfoEVaLwa7ponTOJJKuCsOENwnsBKuDqJ9LWFvd1Yb6vCNqApdN6%2B0YZ8%2FgKLu9w4eKBSK89yIqgam65SvQ4DzQitUKP8NKUs4YEzcuy3EXGxRxingVsQq7wGsw%2BbQLBe1eRR9EGMFifdx%2FmjtY4WN4youHgCR5Vx13NzppEeE3IrSS6TTrmCIlo%2BG8Ri%2Fs56f2YcN0TZZTZZyGbp7UsJl4qkgFiDLUbAVsAF7DH6jHAr1u7Gl8Yv0fHLu4xZtIP6WOph2wAkEt%2B2fda1dDD6CA4uvViYrl8OFGIejXlGo3%2ByN5A6ZlYPsa74PiWMXxw6nuDQMbRf3zgWXYC8%2FVkrWzZ7hNvL%2FZ%2ByD9o8H27D8qjjMtDCe%2Fpm9BjqkAUnkYOYbYWIdZ88AwFcapFarp0yAXZQcHAIhkJsxv6j%2BgzvE1qQ16OcE4I8xD1%2BbQy3y%2F4vCFx7QaMFjjiIcqMxr16iI2j7pxTNfuIEWrcEQdpkVOzn09luCus3AIXeN8qXxq%2BCbtRlT2FKflG7%2B30vsXWPUPlULzHfaXplkEy4PsMKhvprwmIWQh3SMeTRF1uH1fRiw%2BYGOu%2FosnIRB%2BMMYY%2FoE&X-Amz-Signature=408b4e073ffbb07c07b51398cd9ca714d01e805b04722ca5f75cc7f1b9caae4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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