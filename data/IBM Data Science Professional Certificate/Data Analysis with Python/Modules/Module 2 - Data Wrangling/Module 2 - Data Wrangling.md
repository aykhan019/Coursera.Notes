

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXVYX2C%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDwKpMY4tSQAVqpFGbGaUlo6KTJOvbyWrtyvIlaVNQzagIgaTNWN1SuntAuBT8eg9yZaEJ2FJ73whWdRTHp%2BZz1aE4q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDCBfpGdeFaaaX1vLzircA1UKxSwOHBKKKNr03houtOjdfx2uyQaMORL1EQrudabUvHokA1Z1R3acCzbu1oYoR59koDF%2BZZCs2MwFQ9NX%2Bv9%2BnGiHTaOOeoIZm6WhF3ypTiQLsL%2B7Olbx9%2BvPJkW9yj4wSZSTNO8GV%2FwwwkPuBXCmEv3Ion9JK9yWDJ3oX7%2BkRCFiMBxe1OcNMJDPev4CjhBD6NsBJ%2FmDLmhkyHkKUjGxdIWPGeIc4HOMLU5VfJ6g8K7uTematA%2F3AUa8tk%2B%2BIaTnkTtM9No7CvgHi%2F3sb%2BcVJNJ5LWUsqQwF%2FPwuMf1ds5hVtIVQRtDpD2ZYQmDC2MHosX%2FWOVe1ZMmqACkiMHkSBEpClgevjJCW9glJSL4U4OUALzu2UmDIqvLObuS7LwK9VgCxUyVVqcfk9AqAQEN5KmiJmPyFKAx3jeQDc609f7t8lbbDIIgGQv4hPJFImdzXzJKrjbkWqUI6vtsYaRLiLv46IYi4n%2BcjasAjEAjcPaRoCLD8kN2wwAc0GN2yposAAQgjN6%2BGi5T%2F1LvLEaIxqHBsT6LdaP8YdEjv%2FImw7bPJT%2FVpUfCMWOrS0P4JJenyFvicHTJ6IM6uDI3BT0UK2jdWmDyGzu15jej8t9vfGIGLgsfQt8Vlxa15MO%2FkxL0GOqUB%2Fcf0Ht8uSAWfht5MbEdEjw2Fb%2F70MsglN02keTU2VUVQrJSlcRN0mHHwQQcBNhu69LkbIbkd%2FuO16n1IJaVpUmuPlUbfaUXADNPTRlP3Sz1aG4pIx7juMQJ0I2xZj%2BgEeWhONVa%2Bu051zhf1TJTxbYDdvm32U4eewI3LTXHSdLpi0Q9igk0ZPb%2BAgAFVDF7fYIwoapoYaMTzgtPWIBzicKPhtiuT&X-Amz-Signature=e11feb38f47bb261b15e107711c0eed788daba80d57c7b19b32ada31f54296e6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVJOHVUX%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIFClWvgT0cfomZzfK3a5RERCN4YrvI1kZww6T7N3eq1qAiBAAJOkQOHN8XOUqMPT82SGgSrUPYapkh%2FhboLs7habPir%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMrAxcUZUl6DIV8JvJKtwDK9pnfZnWWzjGEsz%2FR2%2FfSlJ4zhY4goo3DHNDUD%2B%2Fpab7K497Pe6RUHK%2BfZ6bOVg873LeT3Zy6G6Lt%2BWMEwzakxzGyTyaTxuKKm2KdKubv3Tk2MkMgNOdclNACD4A3%2BGO81E%2BXzVljXfad9Ja4TqxY3DOqC%2B8QxOljH0%2BYQ7qj%2FbPS2r4dPyruNQihUA7huU4HN0vCWy6EfB9H04k1Vh8D8FLBMtAvxHt1FuBWHZ9rztm%2F1iw5kMx8t4yNuL1dfhX4JR5YB5sLhmD6yqFVZanPC1IjpJu03Vp5OPWTYot2eKhL4HZgC3l%2BezVI0lpk96gsmbA7TdSzzke7wKNv%2FVLl2ZM32MRYt8n19dqbzkilaev4k0QZdpOB15FW0nmvlRiqsOlqlvH1sSVL2zu3ysVOABYMFkQCeajqK5Hwl3QKOPEBCuCRTrUBwAEeWIZhWb%2FmAQFQ%2BPvK3Dx7TtJUyD0woSSIycmwwrUesp8U2DuZVLDw%2Bfcq1D89vopWJNeEcj7obfrnnaLFolt6FoW8M9uDUj172PbU%2BgeDqBEc9K7ftDEuy5tGHAWIaNN2uI50Ukp5zpGjwqLeGD5SCjDnwolCYU6bCfd%2F69Bvl8RL7H7jGuzUWJ3VmYJZeMV2S8w2eTEvQY6pgG4PH68XUbvaNrwD%2B6jpVXrMVU8hU8YWDTuFrHpJyCiNnPNB7jKKn4az8urWz9c7Jp%2BoG6nQCDmSvjl5IQAtGdqc%2BCdWpeP0yMBvMCReSZRgEX2sKvg3Q6F339upEaamt2UuoQ8H0zXd8HrfTZ4YIBqxVUO60Hx3dwqiR4UNw6YTbHOXh95t%2FFZexzRXAKTyGH%2FcHKn40g5MWa%2FgrsV%2BymBWgsN8CW%2F&X-Amz-Signature=ac0ad29592704c57afee4feac427b6ce6ae641f199b83b75eaf7cd7b6bfddb9e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662B4Q7DOH%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIE2sq6uBxA7%2Fu9N7izpfJ6%2FGUdWOsXzX85uzfjsMy5QWAiEAmZwsL25xtOzE03sBI8EEY%2FgXPEMRbFNNLjQilhNn11Eq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDGzaH%2FeLCYjfINfcNircAyEGaD54cm%2FRh0ZUEshjPhLNpbb1lCVyjiJjH9bEq2F5pc2Su69%2FJ1L9b6y0U7kPrCjfWw6LHraEGklEP8Q1YZsH0ttYcAaTAOWQlQ8DamhiMO0j18Xj3iCj241%2BH9rCkZnSa3FgnoGf2%2BLQHzk0yDDtgszVyB%2BIKwiG8z7aY0yteBKs1j8K1WHu0Tshp5onNJxAyZkita7Hw9sWlb65QNc490MhYHjm0n7CYZJbBYLgavndMN%2Bxj8NzIK1Wu1aIgTgJhbzbt8yJkTEyVpt2TUsjiRcIlMEVrtJU4ejnEWxL2n8BoxXY6yXCp2Y5Jv4L0XODwZZaLdl%2Bx32IJDhVR4hW0C4gbTzQZUxon0hQ4sl0cih4bzEgm%2B7nOhgc3Ogtd%2B%2BSaIRPbml7XYx4pOJQflvzx5AhdXOIzZjwzLMV2kokCedzt2iQGVfBeYSu8iU7ZEg9%2BweantQuDgFq91a7ZSt7fPLV7aTvvMAzegtDEzwnoo5ciEOJ2aETISscDLVm2%2BCWPhvAxSxMpl0OdUTasXz9aPOLVPorIThHAyXG7YXe1zhL2PerAeXOqKx0SKNFo8XwstNxLZm%2BVurRfjliS27pWcTwkop0u0pk5WViyfhyFrO1m7UaihahI7i7MNrkxL0GOqUBexxFA82ugRq31ipDll%2BcVAkL2jL0yO0s2Wr1DB8grQP5ynWTSRY19wBGpRsMYlXIQ0xDFRRy3xej%2FfBWnJzSl7Rf9G1fObINi2K9nUP0eSvzeU0DMWDlao5jma8Gkm7DQhbVqziSMN0gh%2Fp8H8DzBJHMVmbxspqezP%2FDp3Dnuv%2BKbRoQX1S8%2BAkZ9Sal%2B1TwMu7r8OuYxpHgl9DGr5Hk81ukuRj%2B&X-Amz-Signature=c3a55359cbc41bf268d955bc8ff8227927984eeadee777962b10b2c95fbee5a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RCM72WQ%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQC5aN%2BnErcb2FaIraHr3iGD0yZd0MxEW7d4prXshuZAvAIgB%2Fh4EQf0%2Fr%2Be9I1%2FcK1VFKBIG9RxEvKw839vygex%2Fjwq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDG%2Bt7SsEgKmR0tlmjCrcA%2BqS5IMR4vnqoa8JxPArfRHo2T7Sbv8reU5y0jSft0Maw9ycuUZhfqAZuSGgd4xoteJWo7JeL1Qs7Z6aQy5okHfjiA0kj6lfz2ZiEEZiyNhm9fElI%2Ffaf5CGNzJEo%2Bfv%2BuAWSHs73sB5etRXi5gc8S0mbjGsocgzcgAI8W%2FzD3wU%2FLGbIGqP5Cl8jUdS%2BAV1nivu7ZpnDVOwfQUC3WlutKo%2BV6%2FOurmgb8pEo8HwswluEKrhSNFax1iqt%2BquZQdneKK%2F9jI0o8bKwyqGjrEvzzrzbHIk0NGOZerAwdoKhOh%2FJZhcOhccR3W5E0qDnJk9j%2Frqdl0K0VxXr5NychmiI7zN3rvcr2gMLcmLYgjvymaTnkBSvjijsjwKZhYzdWsaS3ygtNAtLkdonwKIxbruU0ljE8%2FzI1yaX14ubXnkEfhF%2BpMJF9noktbzkJWuNbagGZj8%2BBT1nrT9cDTn1ugaa7748dceGHCZZHrJBJ6bCQkD7UaRgGcrCeCfKqZmPb3XsvEffFi83loq1xXjglszwhlGnKvCJy2HeuGDbfLg3U9ZE3wtUH2ajQwrda7jIRZT%2BTBPYl160W%2BvhezxOWs7RBCZcTSsSLFS9LtBbf2mKACNQZyzTzqnbk5I36oOMMLkxL0GOqUBcbWQXy1ghUEDk%2FunWnMtAw7JdCB7uQDoe8tq926s2GviuPOA9dz2biQmjt53n%2Fi%2FOlqutweETKnsWq0gsLXVJOTpZZhg6vWP0lKqm%2BZse0hugLHnmPR2nY13fnll36uWE0Zo%2FDKPyfFDiuADjR%2BbQsVya6TbP%2BPQ%2Bkc%2FxhPLUMQJZdkJk1uVbXjaJ9DdIZhnEE64IZIHCWQACtq2Kj%2FZ2mBUdDYp&X-Amz-Signature=5f955a090fbf4bb3410ece460332e3bc684562d51c02f6e85a8908659daf10c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WM3WMY47%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDjckIU9hwBM2GZ0b67WNnXWLlkWimo8vqd10Tgmz0zuQIgKT0CiMOKSmUsaNamIRh1%2Fq90EswQhwEzHlVBQsTpfTMq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNsUJf9JYY7524%2FvVCrcA6SVauSIWPDwuBAniyUYTeaYKGWl%2FeCgJE1d5kNOTiNvL1sWbuWUA3728FndLIpPaSQsne1D0IL2%2BdTNaXqsT654Nax6LXBhNpa9biqKkybTxlesKQ3emLYHIjE7AkwsefL51u6sMMSwjGBk1MTk5aiz5%2FgEROFmFM1E%2FVNc2lx5p89QUekMkyhWrtBdfDNzfX7iuZIia675B6wxd5RjJqXQCds1NN2%2BTtOvKMBevKkAEWkfd2hp0uAMw8QVZCmt%2FuxCPahTUFx9nX4zhhFgVHOnFOtXWjC2ok2PQvotuTF8kbD4w%2BT5L1%2FRJBPqKf4MggFkufqlBgoW416%2BtvZzbj6C8fzqc%2BIDhw%2FRjtk1geV%2F8vuFCaNW0dMyLu8VAdGHoy65zkT7mXrg9sJR%2B6GIUY6MS9jT0E0%2FjrTEhA7xRa%2FeWO8Gc9EvrktjGitKKKRPetqUqo3XrYVMUmdcB7gpFAd6ayrdEqcks7piK%2B3JN4R6AUxw1VjMse17RxzpeQ1dyX9gCoxjxdKV0h%2FAp1SQ1E7xS8gIw6QyamDEDlH71nyL5WAsCb4s6A0SVxqiZt9nq%2B5FD8JzJw13OGvJ53nBjZfSn0Sqy7xjab9tWNImForrXD%2BLEAa2b5Ls5nq3MNTkxL0GOqUBAkadChV41LEoy0zDqcJMdW1cy023dC8qKlZiSTVXILT8cxg%2FSHHvrJeju1GGp2g6rnEgg5%2FYZ6rumCmRzwG8gKySU%2FdBVGYVR%2FLFj8P%2Bp23WS4RJehrpsI4CeFA5yHrfTnaIcb6Qnk4U%2F6ZaNjMOIMAVT28nZYHv5Rarh6sjkDNH7gvNXfUhgWb%2B4Sq79I3CW0lSseob10nhabT6ztO%2B7rhHhiI8&X-Amz-Signature=671af6c5381c89a6d715944d626c7918098e976433016380b7af7dc6dc0c6834&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBKI7XRE%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCQgRhtiqKvTyh26c2GGmtZlouqDPLs4sdUH2XhFdHX5wIhAOwy2YoxeTxXuEEG9ODRnC%2B4ZL6AoczejmF2bRuaH1ORKv8DCFIQABoMNjM3NDIzMTgzODA1IgwHrVl48isgWn3Jph8q3AOwBY8GGyMGa%2FNlSKKYrrC%2F1F1WRqtHCeFVk1kAPh%2BDRAing%2BzRN7ym1bZJd%2BpeCR%2BNIV0rjwuo4LMBEP4BsVF8LeK7Z2v8142Qg0wIRMQRWiyeTRzfjWJtQ%2BAoLMSXeNZY7Tcbt4kgpN0zP6IGH1tCNzVIC6JuGoZ6bp1VMhpy%2BbbVz0rGgrzgrdS%2BumfdKoNYyL6BGYyrGP5odVJK7O%2B0E25o5mbCmOwf3XAXD9e247puSz2kRrZ5uRY%2FCMBJ%2Ft6IWnX%2FQMoVKPnOyJdsDTLDq5ky%2B4Kd3Pr2Wx9cbLov1MdSC%2BqpBhRGoGLCk%2FGkmyEiLUHAjy1ohDW94xOLs6Ji55Jom1VhqKR1i%2BZ0MNODKc%2FfIX27auYSc0FaavkoSo%2FPtu%2FMvacrTCPLLsdcsYc7fVTpuNJlH5k%2F00eXx%2BlHl1QoqrDEAFZ6SShvQSrtLvQZnzBUPWA0%2FD1ji98m26wgy0%2FA5dFII%2FeEmMa6Ku5c74KDSAJx6P6LDlfuiPjraGhZgtb8uUnkoVJLSt7%2BkAhjA6dlI89f9hspLlyLxtYurCVtVl%2FrySYqivWNnwWgLGWBD52nCMJgvPbMFjmx976q0jdY8o56C8RvPr8SUUUjHCM8kunHg%2BLX2dUagzDS5cS9BjqkAZh14IFllwJ1O6YPyQNS6yackmgVsVP%2FNEmh7J1DMh1BNjCxNCarhcvQ7z%2BqK77daI%2F5Y8GWiWbYJ8MN3QWeVgiNVi7fPVbVWAXfnAVK95SgmoALv0TLDN20HoxymvCE%2BytczDXqgkRpYLda0cVuLFqs%2BA9s5bRpZ%2FOAHpRLKzjpzBgNv5wKjUOtWSatM2zJO7yGVHKmVmpWgipk3IxkAN18QmIa&X-Amz-Signature=3c2a538c629ebce19dfe4ce4f36d7474a6fbc7aa6e6969c8505e87e547663d39&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQYVEENP%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIHs6OetlWDWzWytTn%2FKeKPfnhNamSwPbmVEe67%2FbCQENAiBRdzQkcYS0DitmWZZtsWRpD2rHhItHlc5K9pf0rW0Fvyr%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMLmpzAlJjmMZ2NNKhKtwDrCOf9lqi%2BhKCXmf1en8X9HZbOWao3Nwn113BXiIdZJVj7SJBkomvy2YPiHPKGKPJAlAvg2nd3sDq1pfXtS2YMMXDWy3OLHX2tCLYBkxz6vI8lMZvAiTtxbsZZVHAD6Ax%2FQs%2BZQ8qBIhyt7cQuV0%2BceFA6IA8lIsbOh7jwcamBMtUDdWJozyI0rL2qz3Iu8qa0aAQ11ebMRRAhpAR1uvU%2BJVZLFsiAigj3y%2FcgKvlybinpxAhsTs0RTouAhXvQMn5NWY5CdN1KBa3Zt7VQ59SOuwdEeZZ9QY53Ql2kvCmKqCW2hQFOfnaCMybYZtPTrvN%2BXgE94oCftBImsN%2BXsQyEnon7TyKqpkvjM5LzDlJ4uCUbS%2Bdw1QHLYT%2Fl%2FFmhVTgVWgc35ZtFLcLWN%2BOYSvzeOQzdjduun3VmICwEVLwcE9j1oR%2BZuuHBXY%2BTsljDrNANZG7ixlyUs%2FOM480dUwLtcUrwS9MpdbTf9prpItbudR3pvy5KYuoIX%2FToNMQXbbsjkvOP6cFuFv8HrEvQQ4cp0c7201QXuuWLHvDlFK0vgqyZcVyLsgNyL%2B3seu0Hbv6WVJjl7TYP8H45gX1nmmWAQnfbT378%2FVsilek7cIu4gMCIrboEVN6QdwI7I8w0uXEvQY6pgE%2B5c19s9ThFU5QR1a4dJrd9je1%2FwCgYcqkxvm%2BSsZLeOqLW5dIyI52HjSrkHgzLtOCxTsRitT4j9ShlrbmKV0V6eKU8P0%2B6nUR79IQOpuBFu0MbJqkCTtU3WWxKH5ecfS%2BekPEAWY7TvQRdzvYSiZjxB2zbEcaYhgVP6JAspbpHsRNm%2F%2Fz8GpNvIdQDB4tLYgTE4SXVA2DhNLQqeQcFuZfeoMTpKnf&X-Amz-Signature=90164348c7d0832ea4d0e8482497eac8b8bdec272a98fbc5ccbfe094d3b502e6&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M2IJLAW%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIGx7Fax8hB9vNTee6uaxWbkNr%2Bj2xHX%2F5t6CipR1jpsBAiA63HIwlS72kj3FEb6V6V2XHn%2Fo78TiO%2Fx9kqXJfa4UVyr%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMnbgMsB1dWM0Zw7IcKtwDMAKONsCsJmJ71s3RAmCvD5clcjy92iG%2BJiREmuQcdimSA5LIYuN0DEB7emjMnUB8uREx9k5bdHwfQU7mAmwR6el35bR7x0PMb59cKMp2nugp3JhIx1GMFSAWj%2BNzpZMussl%2FRpal0JNYEKAZrJpU%2BN8spxc6wmQbbe%2BeR8kKknbeIVpaHpMhVlCC%2BtdjnwaHXV2AT6y0QpXRyV045fX5FQ1jrYyOZdIuQ5ZV99j74%2FG9TdqE9g7L4EI0z8XcEm6r63C1TdVXiGNQbHHftKFTppmBklOygzYMB6YYgDCuCyLLnDgwggxcoUMbxjFirfPicj4stppO1yiZwFaCpy6%2BVvPh3R1%2BUM7IfK6tlVnYEhB2DaLltL89Fd5sxWfPG7VjOWLHuHq4jKqB6xFZ5Ixq0xgMGZd3IRHmYS73vv8q8YqNtNevhxMhvb1SJCBQbVoTXdJRXAPxJ%2Fiz9mVnQNwiRkNlj5R3bxwD25eSat%2BTvTqWp0FkIVLNyWoxPu3p4EKou2Wntk%2Fmupk5S5sOzZVXsYcZmVhkarPUyFdU7NmIKy4mzAo1La57IvzVuRBsF%2BOqUVk8KnWFW92Wu6LA9KI5%2B%2FSFmB%2F%2F6IC3OttMQIUtQG7BdEWIk0rGm%2BQFrqUwv%2BXEvQY6pgHt95vGa4B%2BY4F5ggddPpGCNtbVuKYV4efz%2FGyzhktFl8uFn1aFq449fhZ96KBDvoJZKtOdx9scZ%2ByoMR0i%2F9mBlx4lomJS4NjLwTG4Br3igOQVFIV3U5wCIZZr3SX9wYAPoAK7aFD9MX%2BmzYdkVq7KuPOHfo4NXuIoheLNnxRxA3IukXcYDS047R6BcxAsIBlycDNFE18O2UTSHa1OC7jcrF3ATriX&X-Amz-Signature=40775492da24977bf801c022556e17456a300a1911428d4d74e66c88739eb153&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WM3WMY47%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDjckIU9hwBM2GZ0b67WNnXWLlkWimo8vqd10Tgmz0zuQIgKT0CiMOKSmUsaNamIRh1%2Fq90EswQhwEzHlVBQsTpfTMq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNsUJf9JYY7524%2FvVCrcA6SVauSIWPDwuBAniyUYTeaYKGWl%2FeCgJE1d5kNOTiNvL1sWbuWUA3728FndLIpPaSQsne1D0IL2%2BdTNaXqsT654Nax6LXBhNpa9biqKkybTxlesKQ3emLYHIjE7AkwsefL51u6sMMSwjGBk1MTk5aiz5%2FgEROFmFM1E%2FVNc2lx5p89QUekMkyhWrtBdfDNzfX7iuZIia675B6wxd5RjJqXQCds1NN2%2BTtOvKMBevKkAEWkfd2hp0uAMw8QVZCmt%2FuxCPahTUFx9nX4zhhFgVHOnFOtXWjC2ok2PQvotuTF8kbD4w%2BT5L1%2FRJBPqKf4MggFkufqlBgoW416%2BtvZzbj6C8fzqc%2BIDhw%2FRjtk1geV%2F8vuFCaNW0dMyLu8VAdGHoy65zkT7mXrg9sJR%2B6GIUY6MS9jT0E0%2FjrTEhA7xRa%2FeWO8Gc9EvrktjGitKKKRPetqUqo3XrYVMUmdcB7gpFAd6ayrdEqcks7piK%2B3JN4R6AUxw1VjMse17RxzpeQ1dyX9gCoxjxdKV0h%2FAp1SQ1E7xS8gIw6QyamDEDlH71nyL5WAsCb4s6A0SVxqiZt9nq%2B5FD8JzJw13OGvJ53nBjZfSn0Sqy7xjab9tWNImForrXD%2BLEAa2b5Ls5nq3MNTkxL0GOqUBAkadChV41LEoy0zDqcJMdW1cy023dC8qKlZiSTVXILT8cxg%2FSHHvrJeju1GGp2g6rnEgg5%2FYZ6rumCmRzwG8gKySU%2FdBVGYVR%2FLFj8P%2Bp23WS4RJehrpsI4CeFA5yHrfTnaIcb6Qnk4U%2F6ZaNjMOIMAVT28nZYHv5Rarh6sjkDNH7gvNXfUhgWb%2B4Sq79I3CW0lSseob10nhabT6ztO%2B7rhHhiI8&X-Amz-Signature=e0e3febbe755499f6b1389396cc380b5822335e7b8f62e1b8766982c72418667&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDXVHVSR%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDWu9h58YVzvXM4X1QA8nWbP6P2R4sUbogXzw%2BSiAUg6AIgZoxLo63LJ%2BEmHVRV6rLxijW%2BxCK9xEyw%2BHHWqGcZ0UQq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJXeOJ1Wq09%2Fy0%2Fm7yrcA%2Fd5U77i3xYRtUXdsgWG0cR6H78ICLv%2FHHQpQBhW5jhCC1mYoPoX3gnJ8ahaMBBK%2Baj6lvlRp3wYWpfTsheyLffqHQCDA5Tv%2B6HEh9Iu9eP4puuSAdGzy85OkqEUfHTXq9bSLfxNPV4vNIuaclE3HehuCEKLRnkq4QdZksDWGEb0vA%2BS0Ibhfh2tAFWx%2FUkUUaPLs4gedytpTIZJ3DbadNzt40HJqigT937jeLb7UuMnrEUTDLcHsotuxnzsoJqLuoLkQEOW6Pk%2B%2Brig8nSIWIOusZwBk2fBAk9IZt7WqUsrwdQ2WURIWuR80byJjT5Rzt5x%2B%2BIka64kO59sI6OxVqUPzJx4a8F36bCkdfcBz%2FJckWT2dI5EdRuRXd5tV1efdHiXgC3tyX8r4FxdzOaHPi5c6s7gIGtWHfVA%2BZ2d9JbSQA6OF06D%2FKq0gtyXZeKMukGwgYZfpGggIyOabJJWUIylsMlMKOP0XV1Bsw7LRRNLenPY1UcHVPTb5ucElyIGv23MliOkH%2FpGZo3Q6VvW4BGZn5ZqwCsnasFP1sgRBr1vQYz%2FyVYFg2X18r2W6uVgVNvk%2FOanx3ZvcByO5Zf4ciKCOAsv35q1nlTHj3uP1YhqM8KhE93m582l3pmeMKXlxL0GOqUB5K5yI7DhZdk%2BD5VYJ2ERmevj3zzEp%2BGmev3wJIoVmhcFDdi63uA23FspxOtaFFvPVb3nyiSY23s6PgdMpOdwSVEk%2F16BCz99HOSe1vvgsSKGSb4FVoyN9NApfU6%2BgQxwd6M%2BiBYNozHGtUYk%2BlWb909XrB%2FiIFk%2FNfF8bNoahQvdRsl4Xu3F8CPYfjousdble8VS46lObDD22QMU4fJ55mFJtl5Q&X-Amz-Signature=587002db11a956352eab55fcd9bac31211c83ea1c757dab68bfec56f592aaaa3&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDXVHVSR%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDWu9h58YVzvXM4X1QA8nWbP6P2R4sUbogXzw%2BSiAUg6AIgZoxLo63LJ%2BEmHVRV6rLxijW%2BxCK9xEyw%2BHHWqGcZ0UQq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDJXeOJ1Wq09%2Fy0%2Fm7yrcA%2Fd5U77i3xYRtUXdsgWG0cR6H78ICLv%2FHHQpQBhW5jhCC1mYoPoX3gnJ8ahaMBBK%2Baj6lvlRp3wYWpfTsheyLffqHQCDA5Tv%2B6HEh9Iu9eP4puuSAdGzy85OkqEUfHTXq9bSLfxNPV4vNIuaclE3HehuCEKLRnkq4QdZksDWGEb0vA%2BS0Ibhfh2tAFWx%2FUkUUaPLs4gedytpTIZJ3DbadNzt40HJqigT937jeLb7UuMnrEUTDLcHsotuxnzsoJqLuoLkQEOW6Pk%2B%2Brig8nSIWIOusZwBk2fBAk9IZt7WqUsrwdQ2WURIWuR80byJjT5Rzt5x%2B%2BIka64kO59sI6OxVqUPzJx4a8F36bCkdfcBz%2FJckWT2dI5EdRuRXd5tV1efdHiXgC3tyX8r4FxdzOaHPi5c6s7gIGtWHfVA%2BZ2d9JbSQA6OF06D%2FKq0gtyXZeKMukGwgYZfpGggIyOabJJWUIylsMlMKOP0XV1Bsw7LRRNLenPY1UcHVPTb5ucElyIGv23MliOkH%2FpGZo3Q6VvW4BGZn5ZqwCsnasFP1sgRBr1vQYz%2FyVYFg2X18r2W6uVgVNvk%2FOanx3ZvcByO5Zf4ciKCOAsv35q1nlTHj3uP1YhqM8KhE93m582l3pmeMKXlxL0GOqUB5K5yI7DhZdk%2BD5VYJ2ERmevj3zzEp%2BGmev3wJIoVmhcFDdi63uA23FspxOtaFFvPVb3nyiSY23s6PgdMpOdwSVEk%2F16BCz99HOSe1vvgsSKGSb4FVoyN9NApfU6%2BgQxwd6M%2BiBYNozHGtUYk%2BlWb909XrB%2FiIFk%2FNfF8bNoahQvdRsl4Xu3F8CPYfjousdble8VS46lObDD22QMU4fJ55mFJtl5Q&X-Amz-Signature=6512dbe8f57d71b955d698a4dc9c20a1d7cbb9986d76013ad5502d39aa4b5e79&X-Amz-SignedHeaders=host&x-id=GetObject)
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