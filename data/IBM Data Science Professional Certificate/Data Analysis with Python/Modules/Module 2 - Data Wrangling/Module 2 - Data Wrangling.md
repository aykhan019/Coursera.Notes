

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7PW3YE6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQCwuNXSMWPSzcwJ0gI8T%2Bv6c1Tmv0IT7xE4KylFfsc%2FmAIgG6bKIcz7aZE6TpM2JEgWa0B0kefD7ycpYSuWnCFaIZQq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDHg%2F8W5rp%2F1G%2BTikqSrcA9ABL2CXbbyZ2yaCvC1Akham8tru7ZqGXSOy9RXmVmDgzAz%2FK3rzLQIJ8IlS7SLDvr44lkGlvssHCGSt0dU7gGSEOjoTAkF7Ob6uq395fhTfWttDwT1m9CRP2%2F89v6JoUuc0NaSCmjK2rToySl1zYMUD8o4dO7%2FocIrNpH76uilVDRJ0X0gpSrr8BKvHPraAd3cUZtzzBEueQXxnO6GQIdTdmCjtcPDsaIY%2BiXWP%2Bru57VxBPk8njNO%2BBg2ITylz5nt7EtdDqj%2FtFlkaY%2F05Y5Co2nVcHBAdvgHcPlwxp0CWIpfqHybcwcOkt7MdBfQHkW6N92dTXnMN0u%2BLQ0yfNo%2F4MJHzau9sObbwL9Moy6%2F0f5bTsVa%2F75UqyUx1ShWzycxv1YkIQNA8NBoPGCKpWcaMwPemt9a4u7DnshrDBq6J1WHlu0ZkAsF%2FmW4ECOf7cZhKtDE%2FAsJMJjpCzs1F%2FYBYP9vRJszbqnUKMYJaFwhis065y0KoCwrmr%2BQIW7NcgNIYvGSbRpI2eVAtYSwXXyVc03HjU06f9JLVPqGyVWyWSt3hMUhjdwH8u2l90jEwe8ylKkcKt7qj6erhO3LOlK9mfilLj0TmioE2jZL0Oc1bAuXZ%2BcX5de9X2e%2BoMNz7k70GOqUBObv%2Fi5%2FcaCu2OfbbN8rlKwPZ9TDnwfPGePEF4OO0Ir7V0WhG8VbFbas%2BvSJEdy7%2FIRD6g2w9J9BSLHDjVxyXzf606J0zBrskbUyfosEN6COezcbqNlSAxcWzwUzj4ztbpzyBAA2MX7COFDTShIYcFiFGqSNwoNMhJpctMRokSwpb3wsuEZ3T8g3yqERTDisW36XzYo4tRsfjGtt50Q11hR2eb4Uj&X-Amz-Signature=8cdc097dbe57a3b19db17b62dde57bae3d061ce3a6900c04eeb54971d301b0b3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TGR67MZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIHpTcesFZYx4CRBkwHo2qlIpXPN1CU78iAZAxXPNjOm%2FAiAy81D5ihmfsEBjjVnjVq7wYm8IF4DtuZ3A6HySB9ke4ir%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMx%2FuW2T80YGZm5QLzKtwDk%2FvIzUwEbgo2nJVfLh4lNqaa2CIFaUCDvnK771qdmMgulTZhNZt7Pce6b6%2FVA%2FS9FTTknvHrmaWs3HXBImaWzLndtV9%2BCbbVVlXtLnDI3oBfEP6wcBserS4j1lYHik1nlj0%2F0hLKErnvofnN6RvxJglsQF5EBPcWwjFDRrZWoZg7jTxCfcZuU5X86kLOxu%2Bd8cG%2F65HtHlfc%2BO2SZe5CgY2tB%2BV0O1dEkFte4Lr14SHMg4S8MLkWLI0aOLGVET%2FBwKvAzmxJFo%2FD8C4sc%2BOzmZ9wAyEr8Hi3ywpBm5m6%2ForSXKWiAcElgrv0GiHOVPUSds5mX1zoNmpbzg%2FLMS6pHMmPoIf5EWjud4iQObBJno%2BqE%2BJIa49%2BXBnxUW%2BhC8kM5IhQ7F6JH2g653Z2sFd%2ByAT0IRCzb5maMSWTNsNagmEIOFc4ccfU1rO0CjvX44Dt9xY7Nnq7jC9D4r00plneO7VPTr%2BaX9b6Wjxkb2nRgJFdEUuSN5DcNO9jkSXQEMTXtG9RI5ikIbDV2Xb7PMs7Z7Hh57DzGbLF6TjNaW8WB3rpwyF5NPLD1lABFLJz51obV%2FhL66L1GjX0msJJ54cBbieECYmNIn6pAwIb06Uo2ZgRQt1BVJiZnX6sy8MwivyTvQY6pgHzKagAkhOOI01rUTH7e0r%2BQgsKJlPw55wTcDrY9GtrZYg64nD35mJhBuMKi6Xau7fkyRfaJ7SY75Jdg9VAU%2FYtZ5pRpVl8IPGdzUsPAWC%2Bzn2jEw6csAfYUMEiRvc88roZUvavIosT0ENstsEVEkL43yVZTJ5pUoNKxwzlZ4CKJJsaAc4gGFD5EmI12wXNasa2g%2BASaNW9p67v4noUXkX6DWPuDtNC&X-Amz-Signature=bc837ce1636702d0220b1f94c650e34f270760e5864faa776132d3b00dd6a92b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA3VXAAY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDpcnkWXl5wp%2FpJwzBCyUpaIhzFjdJmiQpjnFXKC9WQFAIgCM4WzqxD75oYbg5IIp9YHmtnl6BkV5k1qw6%2Fu1TVjvcq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDCwJXqYcsWpOwaGFpyrcAyBEXS154KhG7p6QcS%2Fi78%2BRo2yxFEmwr%2BsMyhv3PjumH2Jgiy9yZh2YnthYTgCegKQTvQb9uViYsC9nfsyh1azjfJNEJqgUWijLc1H9MSVcv9QOglScJhNxfyPWO7Tud9B5OUpKrmM0QHrmXYC6BMbqeBIje4y0VxY0T2ljrguudLTjNOBhl4Vfh3kQS8eBmgKTgHvXxI19ruNFo38939t4Kt5mPCKOeeSYrHbhc47zx6bTYLnOY%2B91yAsZ929C3kKR9%2F7inRX7Xps04wCHuC3TL3u%2FNO5so8GmdCMpLntGmXCmwLt4L36cA52YR95pIVI%2FPE719mo%2Bwhsu0bqcKx%2FSG3XVzUToUb7s5VIdP3Wea9ObsHKcLmdhf9qQ5s0qgPPh1UhANqH5KYhwksNnBMre2tIp227RFAhgalVtwKXUwqMl8jh6sJ%2FBsOIDvln%2FFoHEqcW3l7G2VlIHILivcj5yTzP0O33WAMdyQp%2BEO3dMdLNqav0yq1nxgPh21QCujOQrGcCp7TAwZ8Dnz95MTTBpbH2fo2ftyGn2786P5GY%2BVL9yiBzQhHkdxCFyixYkr6ZKplNPhlCSGWmL9aHaMfV%2FUTSi%2FqwAa%2BjeXKG2ZybcH0C6ZoImhs%2FQdl7wMPX7k70GOqUBraJeCeODrYP0asFAMmn36xXE50cPv27ExQ8eYx9aLX1tiDMuICPImBwMHJPu43OT2vVpjVdNGa69yJL2xD%2FHuF4cihfJCTSQa5VQI4Ogf5FR%2FXpAH29LK4P805n33420ZaxM95DHcgVUiJeksKub9pCei6tgcK8znzEz94CiVZzZ09kkeu%2FZPwxoItSxo8SUbThQt56zBW5E9qYLs0IQNWoJcqDL&X-Amz-Signature=2157dbf00f5a6fe0bc99a2a69f43f332ec2fcbb66bf031255f65042d629f61b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664T4DVEDK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDgA4rQndKCCI6V4Es90ezqOrUDrVpMPirhZ60pN%2FbQWgIgVWetqhyp0SU1kxYExSy5EkFGmqTBshg6s4p%2FddLk0LUq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDBpAOVoJJnvkxM5V4ircA53hzFbRO9o9wmqhZFTB2svrwy6U265Fm8XHvehk89ckXuWK4N6wCMj%2F1YcWe2EAH0ze6iubbQKMk29h6TFHGo8ZwMdNcWifcWtCcTdJz6uRA0KFG4mmJUTvbPH%2Bft9U9OQUF8z%2Bn%2F5NDYtNnN65DQxVPUZ1lXMv3d52BH%2BEU4uU9gxl2gYE6LS4lEjfCm77o0BPvUVRt0FwDDyorB%2B23KMhYV4hv62fe%2BqQoWPoU2SBSoiYhxRGlTie0G1O26qHolyurz2%2F3RAyH1%2FeHm3xRK%2BUu1vYdKO5rFO5zXtqqq8jd30OeCOHOjN%2BMotEuyA27Z2RfKaD94L5oS1kzcEETGC4hOd%2F3sLrnEQ5jo5Mf%2FajxukyMf0Surbf8hpRmR5RN2FVPRhzChPBnPqBEP7NCjLrvsWew61gv30Gkt%2FFyk6pe1iyslqY2MVTC1ARZzDMzon%2BzHRmDUf0ljuQ0zTdiPmF7LyuKaztingXxqxZMQdyCACq4E%2BJkTXrcNHVfmL%2Fr8oDkjucfodOy4RPiQUeeaXCSW9Kuko7KHwOArPt%2Bo7B2nEetcVyWdNqEXTF7dICQuWK8mWOPQrGext6JRXJqcTfoy0wdm7szKVx84N2tZFpoma9pKijJLUcOf1EMPP7k70GOqUBEeikXTZaA8SA7i2ynzzujb0KHeNRYzzOXZjRwXRWXTOg47R0we%2B1vlT05C%2BluE92PckopBNFXYduKkueD96jWkMvJaGeUgM5UFydIFP5uuQdeAjPjgCz89%2BCCbZ3NobhgYx496Z3nM%2Ftyxuj5yFUb6vOLIQbwY0TCIFDijpq3Nk5JiBIymgCdLCLYU0d1c0YnkNhqtKEgorJ0nXDDwp9EvjApvpU&X-Amz-Signature=34a23429c6d835c7047002561edede8510f9006d8de64cc00e0372b7bea330b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJTKX54T%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIDr5dW%2FEIgPZWLv8KHtqPd386l%2F3QHlvl6eMnTNBQHkcAiEA%2BbqBRidogCzvau9NJRrPZZdSfVwmdQ98OFzGFTWDosIq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDPSZTsNSqIRmc9ncICrcA7HYU4bY0%2FqwdBpB8v1U%2BTRBELA8S78b1mNJLD5NBXBKRlSNUWvzLubqQOT8bmbNOEcM8enuRrGzkeqymgTNcVFi6%2FpCQIk%2BxA%2BFT4MPkV9u%2FSvrmZbHZnIJLySWOVDlu8BsuLgVsPqX1W3LsXPHpyrytxSe2MPb7tWZnfoun6Bejl9VUxwhlnqoSMmsi2lUiX%2FldKzs7VeeAUP0rApN%2F70JIGjeYjLp9UWi4V8d3cMH20rpgmOebzKGN%2FLFHMOCOapPnI0lofmS6bbS5ShcYrtu8zaFfCfBmI992NoFipAHZu7ARSnSvn4H1GcHx2Ch5THFRe%2F2Iwa9xSV4YwNFD8CfvhV8NtJWYWayupVd64ExheSgWdeO0OJUBafRPg6MYhEPFhvehEkRucgtCQsOzri3rXOqSfJS2XMojlct8oL%2FB%2BsR9IivYhPHRkhZOnw7AVeH6sw9fdvX2W1EEREfUERfVF8xOzwB2YIc69zK54JznPtQWsY7mI0B5geIAB3CsE2vAbg8NzciUiYfKkI9ElT1GvTgORBo9%2FHIeem4xBOJ0Qiwynh3hqdKASf735MucY2Lj4KFxpCkraHW3q%2FFLlq5JM2ZjOja12EWlumyERCYCNTM8W6uNIhTDgKAMNz7k70GOqUB4AO7q9gAG7S1tWoeHigP3cgzTGZ9JW%2FiIqllGK8WTmA3lprywYnzIQuUrozIWdVAbz%2FgoHSdFWHwiuHisGUlLos2gNKyxADVdr7G15qWc2mZ%2F5vsZY0bx1%2B0DG3V7oe8f7GEoemdngfn6eDPnrwdAbleIulHeCobS2wwFcA%2BTQ62d2H2kU6pxLCb0z4G%2BgeioDTWsfJcLNbjpMLKhNzLfSgLPSw3&X-Amz-Signature=d4a840da03dbc552f2ab4b4b4bad50f1641eec25e0d139797b4961cb4a41d869&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HY4GVXG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIH4DLEnq2r0VFNRp3Fk78fChDjDUt69RGmXSI9amoKH3AiAE%2Blt%2B65SLdKMWkJ70Uv1VQXyYp4ZdZdMO0IsatP0nJyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMwmJ1kkhB47Q3xS9qKtwD0dyHJAduevLRE6Gf5VQE%2FkFKiPjYtMzTF6%2BxZ3FvmIsKGSWZ1AS75p6czX4im2c51KzDJIX026qUww3IqncD2r6fdZwfluQZuchrIuaXveV772PMZ9kZPzDqDmFDjsijU7LYl776rCLOORFBDYb5pTpG7lFgMBS4MydDrO%2FeEH4DE%2BYdXguYtwom%2BTMqHyAAgwjtCJgX7Ktua7wUigrjsVenufz6R6%2FbhdtXpsWij4rfPlLleaYvdPTPKPmuy1y816X4FPV3MhtjjKXD0HKXGhAaVNBPKGrEFs9WBj0MdOQYFFjm7utDAuqykCIIMNGfIcgt0tmdp6QHDGsb%2BnGBUiPl%2F6FsXJPpL7nuy%2BX0pRVTCL3vp%2BtUqvsTNABS9SdKIRsgffe4rdR6RHVaJ7qxclgL%2B14smuYiXXnvA7aiQeFteM82CZaf7sWiDDt3WRXUzSSaW8wmsmgotZiaaERwtJRPigqbh0RzpZx9Y%2B%2FZzWYwIVGpMlkEx6Yqg4FW8j5hEkVmRn98Me%2FjZsjry68KJR2sdNNujEwI9qMPOPSNgr58EGMFiLtMv0r3Vm2adoEYpw5zTXaGczAaAPV5VfVtG9GbA6PswtjLHIq61eH5jDbzguDCyaYT6fgFru4ww%2FuTvQY6pgEKvjFDNaYq5WOr8k2adatzhXLV6oyqjrIFwmQ%2FRCSLYYPJW5dNFYbPPgfYu754kut4aFw0EvgyC7tYk6N604VMiVe5gBcTSsimNIkuKvR0KB6SIo3%2BnkhLErQgOGNPdH5FbOL7tFOgRHgXDdmKRndm5qTwECIK%2F5HNmWfpIbWRrHXeKyK3bvWrC31Vfh43dV9QCl0tw9ACTZAnPH4r8HSAXu8qi9IA&X-Amz-Signature=4ef1bf5297979a83755d5f87cd019f42306b0a69d58cf2e92be180d240551911&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIP66T5V%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIGt7qLsgVeDN2AJcZrZr%2Ff2aQb9XBRIM26hX4YBdKReSAiEAlb4bS8Hac9ZS5imDz%2FzvhooEbSHHffojTehmHPrt5tMq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDBYKefq6rM4BwDKgxyrcA1Bth5eCdv5yxvS%2FV45iguLZn%2Bp1G1s7%2FqhRaeyQKHqoHs4%2BRxucpJny6pafv3F9XbaeeRMVkdTOfhh%2FXjsfwFH23KMbRAnyY9WfQ4LQQO9K50xMB4xtPNROpkWRNLtUj3%2BqrjPjLGYJfDTjeqQgEdycEfdSGUOqWwGxFWA6GKxCVAD2zs2v8TgkfRKmgmN4jLysAFMcqdYUJpSerYA8QpXb1PmZR3bJWX6diouKzWSxIEQSxAlUNAs54wQH904vPBx1lUnp043lewz1OMKiGS%2FSx%2Ba5yI6Pd31z7soqsLKsN8heEcvP4uISZXd6X0EkzNV2BeecOtvJzs8v6bCRE4jGIcZ5a7ocrpGqukanHfBjUhdC1ACwPYo8f5L%2BPTWOEaFnxQY0xn24oBqHu73B86DnpBzAEjRxWUKLGtnsJeNmVYxE6v%2FRfROY%2BUhHHJoIV9534GhRhFoCY2wZ4vmhW0%2BrPBmElX6mfLcdwwxanCoTBZdUTujjsTU%2FWXZ1d8OSh3vkuhQ8miHWyB7danpkVlcTquChZLEfGl%2FqIE%2FbGO2%2BxO3csESnwR5dR0FkpA3EylyRiPLN5tj%2BvRPK3J6aMRM6XZHofG66qf73kZO4R%2FwJbSilnIgI3Zrs96pnMOr7k70GOqUB%2BdTN5idYJNu5B2HXBNMllK2JyzYXMtjDJzv%2BdMR2FVomimuPTakq9x4K%2BoQTWkCRPpkKCL2WaE3w5hpajbijgu4tGT3GZ1cqr%2BBvtG3RDIQRAANOvFp0gABnX2F%2BmTUaaxNdVQQKaFanWYqrlMRvIXyy9tqRYWDzJWUpVdVpJ%2F9%2FsCCUjAhRIiceh0XWkh1dFL0ED4eMvBjAwEpnJxViv%2F5uNSea&X-Amz-Signature=45b24c220b5af4accfc844485505aa345d2112291f401b74e82c5a5cabd93585&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X72ZFWLL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIA%2FuRmS9xiLA2IhgmQGBZ%2FFzLa2xSngf%2BIa%2F1x8t%2FOiHAiA1AYHzPxMp9XARRwJJkrwHHlmE%2BovlTHXRRBNCPKl5cir%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMCP4S8UZfTwhXPhwxKtwDWXMx0FuJemH3GObaC1KK0uTr%2FKn3iI6IiBV9XBRmGQ%2BV2pyubdqNd85Mx9mOraJXvZ73r1Qu%2Fh5OWlUkcHsFOxMdGrTjhwrYwNlvcXV%2Fq6mMzdArBPXr9yGTQhuMwwTt9zERNU1NHqAraRwjUO8iOdvQ5Q72BtQfxnWelWW5EySFhWt0XaKu3eUq2DyuwvVQ%2FBeEdN6WljV0IcCKQkVcq6cXLohObE7QEXjBjsR3l6DLdjTbzFv5iV46WFpTT17exh21QnB%2FG7ITSrWMZvsbdd%2FBKG5PL%2BMsUhcoccj36QzEsUuB0lC7zV%2Bo3wrGV%2Bj8bLNDvEdICkWiOBfeRCD2banNXgOq3Lv5VwewaHk5t3TEaOZFqNI1yBBcc%2BdluEPsYdPzqF7%2BrOFYhHWwTgF8AK%2B24tAjjW%2FSTQ0ZXoIwhsq0aEyR68LE35ONthEosB0eQhvcEp4dDB6yUl9oG%2BAGZtJ57cNKRCXHZAeMPzLEyWTK%2BSmStxoYyuPZDUZKH3a7R2ZE7P%2BiK8mQHaoHo7dF4IT0ne0N8rypAZx1psEAiJcPZpdc1PavpzMQ7MTeJ4xInKi2x%2FAxJuito1vlgl0TlSb1iWyVj2eG5rcZa1pHDwNdOabGfD8XSoL43sYw8vuTvQY6pgGnNL8Ft4nkmg%2FPOe0XJlCi5SeX6gCzJEKID8m0kLmI%2BZfH95Vi3%2FAYZVOmbdPh8Zhkxo5rldCPr02qTnREL7KbuYzaDBOY2Zt3AUS26vi4iVWY%2F02flOCFw%2BTDrzD56vIHEvSc3setlIM7LD3XjfPNsuB48x62BtbS676jZ7mm99mHrA%2BEF5Z0aeD4XDdUGdRQvxi%2FjUoyCEEy4Z%2BkK%2BLdtw2Vtl7s&X-Amz-Signature=4ee211e0d9246d481ebc6622487a6f666050ed94146f023ecc980ae633a9da9a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJTKX54T%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIDr5dW%2FEIgPZWLv8KHtqPd386l%2F3QHlvl6eMnTNBQHkcAiEA%2BbqBRidogCzvau9NJRrPZZdSfVwmdQ98OFzGFTWDosIq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDPSZTsNSqIRmc9ncICrcA7HYU4bY0%2FqwdBpB8v1U%2BTRBELA8S78b1mNJLD5NBXBKRlSNUWvzLubqQOT8bmbNOEcM8enuRrGzkeqymgTNcVFi6%2FpCQIk%2BxA%2BFT4MPkV9u%2FSvrmZbHZnIJLySWOVDlu8BsuLgVsPqX1W3LsXPHpyrytxSe2MPb7tWZnfoun6Bejl9VUxwhlnqoSMmsi2lUiX%2FldKzs7VeeAUP0rApN%2F70JIGjeYjLp9UWi4V8d3cMH20rpgmOebzKGN%2FLFHMOCOapPnI0lofmS6bbS5ShcYrtu8zaFfCfBmI992NoFipAHZu7ARSnSvn4H1GcHx2Ch5THFRe%2F2Iwa9xSV4YwNFD8CfvhV8NtJWYWayupVd64ExheSgWdeO0OJUBafRPg6MYhEPFhvehEkRucgtCQsOzri3rXOqSfJS2XMojlct8oL%2FB%2BsR9IivYhPHRkhZOnw7AVeH6sw9fdvX2W1EEREfUERfVF8xOzwB2YIc69zK54JznPtQWsY7mI0B5geIAB3CsE2vAbg8NzciUiYfKkI9ElT1GvTgORBo9%2FHIeem4xBOJ0Qiwynh3hqdKASf735MucY2Lj4KFxpCkraHW3q%2FFLlq5JM2ZjOja12EWlumyERCYCNTM8W6uNIhTDgKAMNz7k70GOqUB4AO7q9gAG7S1tWoeHigP3cgzTGZ9JW%2FiIqllGK8WTmA3lprywYnzIQuUrozIWdVAbz%2FgoHSdFWHwiuHisGUlLos2gNKyxADVdr7G15qWc2mZ%2F5vsZY0bx1%2B0DG3V7oe8f7GEoemdngfn6eDPnrwdAbleIulHeCobS2wwFcA%2BTQ62d2H2kU6pxLCb0z4G%2BgeioDTWsfJcLNbjpMLKhNzLfSgLPSw3&X-Amz-Signature=17779a52e796f2430a654aa8bb5b0ccdc0b26f94d96ff6d712a22c9a400fddde&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEI2YVFF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDVbg9ZcqOx4TyApcvTvgPPj44wmU3iezyxV3Honh43nQIgB9JvIXOSySTvnKPmUUquecJ9Jkm53NbzR7mXp3p4Xmwq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDHwdxHWMEzejXbhuJyrcA0t74qhaaZaIzqWC8mcJBgH%2BEKlzoW1DukvckwosvYGvWH95EY%2FKQlZnLWl6wD4JdgPqnBLdjfd%2F2bnISevcx6oRB78ZavUDFDrK2D%2Fm7FGas62JHy9a81fYVXatq9F5yeqExqmDle9cJccOCfJtFNfxpD8g9o1k80Tqis%2F%2BNBwCui5fme7l3L0669xbzBtUsBjZdWiLTd2cFl1b7g%2FtZnZI2F%2FIFhGCWJZ3V56vTAaTyGg5m3%2FYPCfEHX7w23y%2FSC4NUNXkjRFHjNF4TS68JJOVB4b6zKO5faPbsnOJfVs5%2BUr9F3F08w1kjy%2BE78oYBojenuKjP4MZisQjNGu3qIMaGQKS%2FUfLMTrdTrahsSHUkRIrTUVc8n7TQ7N2%2Fg1O%2BilVJPOEDYYMjiZfyPFLvc8kBA606h%2Blsxq7k0foLop0Kdxf%2Bk696FMhNHO10uhWBEE9DrwCa85mEmXeYekO21aEvLJD7fLhTV%2B7QmezrJA8E7PgmFM%2FJNASjIyhveC9kjA9AkWb8I2It9jJr5s5WRrRcOs3nTvW%2BuuP7pe5sRx2P8oIf54yC79WWMHYA4vaxL9b3W0SbtOy8vclRgXEiKVn0UhfaotGhoEHy9Os%2FV6NNY%2B68uoM1YwWFRhsMJj7k70GOqUBBb22hpELCcVovywP509SUlc%2BN%2BlYWbMRQ2Jyp1v2NVvfXp1F9Bn7PGq7bf8xwYwU%2BUt2X9rjDCNB7TxvOPTJAxLjwnH8ytGz1HD7jG%2B3ZQ9m3XxEqJppRqKM6hKR0ymXvuosz8IzcGFIgh%2BldQfEh8IX1DxArxl1e7lth74A2GI1keUIF2Vvm%2BQwUEZcD3uZxn5HtBxRnboVZB4Dk3DqGAz3w9fD&X-Amz-Signature=a782290860a364c3525235d01a227be71ab222bc97eb31df478d70b590091fce&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEI2YVFF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDVbg9ZcqOx4TyApcvTvgPPj44wmU3iezyxV3Honh43nQIgB9JvIXOSySTvnKPmUUquecJ9Jkm53NbzR7mXp3p4Xmwq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDHwdxHWMEzejXbhuJyrcA0t74qhaaZaIzqWC8mcJBgH%2BEKlzoW1DukvckwosvYGvWH95EY%2FKQlZnLWl6wD4JdgPqnBLdjfd%2F2bnISevcx6oRB78ZavUDFDrK2D%2Fm7FGas62JHy9a81fYVXatq9F5yeqExqmDle9cJccOCfJtFNfxpD8g9o1k80Tqis%2F%2BNBwCui5fme7l3L0669xbzBtUsBjZdWiLTd2cFl1b7g%2FtZnZI2F%2FIFhGCWJZ3V56vTAaTyGg5m3%2FYPCfEHX7w23y%2FSC4NUNXkjRFHjNF4TS68JJOVB4b6zKO5faPbsnOJfVs5%2BUr9F3F08w1kjy%2BE78oYBojenuKjP4MZisQjNGu3qIMaGQKS%2FUfLMTrdTrahsSHUkRIrTUVc8n7TQ7N2%2Fg1O%2BilVJPOEDYYMjiZfyPFLvc8kBA606h%2Blsxq7k0foLop0Kdxf%2Bk696FMhNHO10uhWBEE9DrwCa85mEmXeYekO21aEvLJD7fLhTV%2B7QmezrJA8E7PgmFM%2FJNASjIyhveC9kjA9AkWb8I2It9jJr5s5WRrRcOs3nTvW%2BuuP7pe5sRx2P8oIf54yC79WWMHYA4vaxL9b3W0SbtOy8vclRgXEiKVn0UhfaotGhoEHy9Os%2FV6NNY%2B68uoM1YwWFRhsMJj7k70GOqUBBb22hpELCcVovywP509SUlc%2BN%2BlYWbMRQ2Jyp1v2NVvfXp1F9Bn7PGq7bf8xwYwU%2BUt2X9rjDCNB7TxvOPTJAxLjwnH8ytGz1HD7jG%2B3ZQ9m3XxEqJppRqKM6hKR0ymXvuosz8IzcGFIgh%2BldQfEh8IX1DxArxl1e7lth74A2GI1keUIF2Vvm%2BQwUEZcD3uZxn5HtBxRnboVZB4Dk3DqGAz3w9fD&X-Amz-Signature=18b243209d2344f09b8d3dccd449e6e0dbcceb96d02883931c44ec9774476150&X-Amz-SignedHeaders=host&x-id=GetObject)
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