

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466345UHODU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwRYRDQgJSBVFDNkl%2B7g0sgBV1yNOqAlQNHI6Wl2p3iAIhAPO0vtGD9jY3K%2BxD1%2FxMSCwyUStQuHe2B%2F%2FQzP%2FrzO%2F8KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBErDd2GT%2B0RLM9i0q3ANT15MoX%2F4Wp3X1PNZjsNTCRaiV28otHmgE0VtjeQIDxUylfI5YTn3IoLD%2B5LZK%2BkUSzB5t58gdv2pQEQ8t91NUN6px91GlvKOuhS9Nye7k2SdA2KfDqJ5HiWH8XoFGnQsPBiuJJ9T8OWLmOdWJTwxcK6H63qbKq3v2V%2Bk%2FMdR2Al87cCKD5iplV2LC1ncrDl7yBfD7ScPz3m5sPvhybHrIasXwa1ENb3Pr3C3TUdCj70NXT0JB%2FbUANZyECh5Gui02LKr%2FA4Pm7f7YsU3iu287uo48Zzh25u84OSZjnas%2BRTPyU2LozWrKUhzRugE8Zr92rcqX0JF6QrMs7KI2h1WIVd4I1K6nIzXBCLtmHFE2mBS4zPyyC99%2F%2BhebjP3pUhnE0%2B9gze0os5mOJiQ1PYFLwJa%2B5gsxnx%2Bt1owyZqnjvWU9v8YmeGTomsZy9E8fL3FBPtr8%2FruPclA%2F6RUsxhkLVyAQF4sZqc6KIdKte5r9yyQRF9matbYp%2BRwaS53ImGinYJDDGVfMS2nSxoc2oEqndhfNpPljHeifpgce3f%2B22glJc%2BLYI0l0f82MuoEI9u18eVcvGBUiH9UR1Gyiq%2BqqgoN%2B%2B6k%2BSji6NbXonqsX7pwRf6j%2FGHHLJsYwyDCqwf28BjqkARFQZJqAJytG6rJhNWUKCzUWojodVomK905h%2FLb4o220bsDhfrKcuTof%2Ffc2B4ar2x2LWqPnq82ggDtAlNcrh229Syj%2B8fxFOfya2k03tyrljElizYyiaqSM%2BZfsz55jzlBCqD2%2B2kKaNv8ZEbE7XdOfGpQF8gcG2Pc4Xq1J6f0r9oYbtxo5OiBW%2FR76apBcL8MOcwjwzAbHm6FKopSaw53wwlo7&X-Amz-Signature=c31ce578eb681bc74a04870d0aa64fe30241d4603526887bd97506dea36f97bf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHIKOWEL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBi2afpEJT8wE9vkPefhVjvJ%2BxPFe%2FUmpIIp3q2MdztrAiEAq%2Bonb4fyMCmAB9uWKASDG50mQFDXNRy94W8H60aMT5gqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPPnM%2BWm43nSo2dWLCrcA7zRbugHCTRSr0i0txEND8WeDf1eXFBLzSa3wc6FPq8bx7b1lLMPadxQAjccL7k3HHEFr0iDh%2BK1q%2FnNzaN7M0b87H21AHsyGrIUu5gRn6ETNU3UP%2B%2FP0BpBmZq%2FAydNJ4HZSkJLq7Ani%2BOUqy4ChSEt1GtIS1KvK%2FpG8zjGfe3pVqdu5ExIaeD0rdJq2fh4yK1hnH%2FVRIH%2FUTf8ho%2Bi4QP5H1oiO2rsX4%2BYchc4M3pB2xO7cY9rZUsN%2F7%2BNDNB0Wso5UfKeHiwpLNSW%2FVaw9RM17GQiWhK9xYf0eX2K%2FxoeOQTz1dP1WYbTTSUHwzj%2FJsXpcrHF2wvM19H9UaOFhhM%2BmASM8naM%2F8a%2BoqQ0LsokdcDlYLoU4nDudxhnE5KH7Ub1V8ojRO%2FXfY9tA8jwUtjq06k%2Fi6RoRX7ZYV9gGiAmJHgUP8K1YNb1E%2FPLoicO7%2BRfzgNhtE6N3cTaUYKUAldo2yeTXGK9l1OJr93UK4d4XvkUcKT%2BeE3EgLEBkYlriCR8Tua%2FPLwm99q9Ul5%2BMO3Eu%2BpPKgEWj3bPxR1utK7Qj%2BH3WTmIQm6VMUZwmKHn%2BkIWZQ9wM4fqnS2i8AxI7UNJm676RrMR8atTToZXHPI20V55vEeTU2%2BcVNiKMNjB%2FbwGOqUBQeuzunI1iCLlTLvlqUd9%2BMagKkj8I20FN42Inrj%2FSRn2rnDOzAXIziKyLaZw4kpPDswOxW1dmgG5It6d2EDB2X3sfjaxxb2QkgcZl9BbBZYtI7Xmh9sbbOiG51ibI1DfaAdM0kD4n7M2htIOUpYyVSNtb7UgDLFN3qnp7yuomnek3fIDKQqb4ZIzMBjvyytya4wjrrPAbEBtVjoXAKsDhxUKVd6V&X-Amz-Signature=f5ec8a71c477e19e9e9c894195485808683695326a14291e43c34494a97ba1aa&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JA76SNZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOigqPXilujOB1it7k3JuBdUuMyvFtALhqfMv1n0GNqAiByVyg9zu4FN0wmjb3SZduyf1wpTrUPdjkyiEP8VrzDLSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8AChFU%2FnFTXlvkxbKtwD2OSmTTeYW3Rc6NZRaJRPzHFJYTtl0OYAH6YRYtXfEda7nHUL6F47K8d9uHFGIBuTLIYcO9FqZ6s15SRzF%2ByVRFFyL34KPZU0MJG%2FklThmdp39Qpz014LvljoTdVMWZZG2Hjzk3Of0OX%2FqpownSwRvGIPWR8Z0g6vXQJ%2BrytH%2BuxokQG4Yh2JS1zhadk6EYVzeHDi2TITKKU79F2ec2Rz4M6stPOH2%2BSJluyy80nxu6pJ3ztLTrNvfhHknbpkLZFzoKUFBDUR20YxcNbeOp2%2FYigNaRVWC3A4zQmQEhQlM6GQvxIqjv1WGNxtnB9nAZ9TDRhpLWGkFPzXiBFWBdWV3s3TD8JpQfusT9LGrHBoeupFucRKQdWHn%2F6%2F2zbOHBVGm7A9UoDLxl%2FqCs8jF4IyLP1FTbcPg0nsnhFJP2DRGWDTqdvtD8cjrHmEki4wopmveabvIWlSrdDabfcNU1hkOfLYOYXOUbHTEkFusSgkKcp4UvDeqjpNTIp%2FhIxFK177h9DW7MEi8FiCq5i6ixkWp8RLlgQ9%2FEhH9vM2hxpe6oUJjYW62529PivtODgtDUjiUEy13FlkN%2F5lMVCd5dDe2z%2BFbrQdsfij5BbmNZH1u%2FO%2Fdtuk86AH9SLY%2FAgw%2FLj9vAY6pgGaTTYamKH5I%2BKOFEG4rqLpvmau5qrBuaPjzrnoSDYfrn6L8QBItG9yTCasfEPciboMef8GhuVwlLvOEj1%2BKdv6G1nBEwLb0oAPkisorwZ%2FOjIjuQrleUi%2FYSAJ1VqwneG5C1VDdBqkCYDq%2FU10zuLBQDb9UT8NM%2Bzt4RNCtAKzSQ1kZQ%2FX4szWm2LVEuLjYCbWme%2Bcsje91vMh103YDxeRZMlbf0%2BW&X-Amz-Signature=0b1cd82615f537d9e9b2a5be53f12a9e9b3df31176eda407233db5e1d26427ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5GL4LPT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXi2K2E2zYGMvxLXlEfiNymljhCFcMfQkQhDpDhHZtcAIhAOfdPN2aotilyY1c6UVTxocc7Om4VokEkSWaFzsC1l%2FRKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjSosiSQgfTasyBCYq3AMN%2F4wn325%2BjvQI%2BC5TzF4iMrlnbMPBeTXGyFj8A5G5h4DvGDeBA%2BYlgUnbwFkYNAz2NQeaeuAkpSY1DeFD5MYPL4FgeVEc7npRMFlnbsBhF0Xfhx6aXHvNFlpem5H%2BuPt9vf1pmccUZvJDTuTGFxSOq2Cuyhy1Xv2GO0Ty%2F161YlT8%2FtKnbrOJWPf0rKmw6ab%2BM9JI5tNVb77Hw2CCCdYvgnvFjfye%2Frmv%2FgTdzUb7bgEoUTyLQLKEx%2BsqMC%2BOoV1wZzmUYPDJBMkQR8HGydOYnouRiEiAAnAZiTUg7BtCtDWZwUG5JD6%2FP36XqAhWX3MdaTNciqiPhLirHIR9Z5ujFsHVzC0VJv%2F9go0ihVUzmfDHh7XTfBgYGZgs3NuRXioTz977WHBQ91WyX4c1W31ZhfluO%2FXox1qHp9zfGGLCvm0cz9lTsV%2BPCQguVEjPDTlIl1vouHsrl7nc7E2xrwy73vLs25%2BZja2BeFucAa5QUr2saIr8EH43lSmKlOQQm2uy%2B013cvKMkmhPuvI0Okq1tn4ps%2B37BnDFZWBhmL6pkDNvcIsYPk7dT2%2F2BFVyVzfW16pFTs8hxP8jPx4JZYTt0WskNdFdHljqLv914i37c5vME9Xbr%2FFI25fOJjD8uP28BjqkAfPfUg6dYZ%2FA8kMazGkTAroNyNkknL8IeLjUOO8JBKFOmWpobn7Z5Zw1qQTQMhLatcK6q9Ysw3D43xtULGsjPWwa2ymeMbXJ6v9Z8kjPSSRhCfh2Hs7ncvl7IblfjxKddlhfgwhEOipzfr2U5Hiu0YR3AvRGlg5nOU7gUtlg8tMOIypc1BPrIgWLZ1Xi50MuJEyPoXvRd39OesKMBK3P5Rfbgejc&X-Amz-Signature=1060184d471f1fb181b096dc7c064159713ce6cac6c5932726287d14027143b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA7M2MWV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYzbak%2FcsaQE4CrvDZpHfG1B1vMiYVp2mrZ4o0%2BVIVIAIgSin%2Bg59h78p93D9LwS9YwzM4mm4QIT6cFtisksxrIWcqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGW%2B1iozCjdzGyKrVCrcAwCdkfBF0nyPOTIRgbJ5PhUiuzmWaIE4xuxqdEjoAAKbR2vPhgLL00UFcitdtYYzvyKRRcUzUF9LuNcscFP2mp8d7RPmorltnYH9sKr%2BqPHx%2BwJ5nB3eK0ruoC6ZZytLOiVd09NkuTAl7OqWHriH1N6EWJYXUQP6fITPUlsvptSR3HvdA4lAD4PKlHYS0RQmyssGKST4b2xXOHFSbkcfdmH7cPX5VwrK%2BgVPUctzA%2Ft1ssBb9KhCav9%2FeDWdoK3qwHY1gvdzsdrtIWKRGzzFxzS4HkPBs08GM%2BBrKPPw2fxLnhahoWsyl8h0uesj4CLiDh2LrgICN9Cr5k61kuaXdssBeCTuX5SE2GxfR0syfdRc5CL5HxKLeIDVcsAEhE639Gt2IgKokNIfurj03amIAv0Ws9xGCBjcZBhFl02UL3irjpK3gmyWlBQXpspNOHxqiJXvR4MctNZc4Y7JaiBnavOqN0qLN9PIXD6x4Yd2Y2lWDlVJMQZ0d6h%2Bh1%2BbC6u3Eae%2FdfMM9gNXEBSjxVEpHeORUhSNJA94o4ZqT5cxi%2FgToAArnsazRmzc2MAy9oPdZyjxPCCuJeykpB%2BKfrcUWrCmHsB%2BXIZAxyNXjs0sdBJs6uCKTtpwiecbPEDZMJq5%2FbwGOqUBLl%2FpsIW2K1yMGeEqNTFNpwNoRvCNS9FuYuyxKrI6LeuObRZi6%2BXBHq3T8f%2FX5S3p2UMsR%2BABpNzL5vRZ%2F28xHOAOEep2hkYq%2B%2FJA%2BxDdJ%2FhDKCpbbRh75VdxHcc5eRMbnHZl3MA1Tp433hW6fVcQA6lnoXYgoNZ5HqKdOCdFYkbY2N4IOAnjAsT37oW5zLvjkzOBi%2FuxwHOmHBDNbpSmYOjk5dyc&X-Amz-Signature=e6e4b85630d86449c333393cac638cc8f1c23ff17c354d3fb86f8ca1779da85f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PD3LXCM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAFzHbIc7lMv%2B62uK%2B5OMvRYyz7J5Jo0%2FWuxdf0bN1ITAiEA3tHalQMoMZcP9wgHmU6J8dUJhJUa3sMCX0G1zfpO6%2BEqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGvoBgiqeWQx6vVm5ircA%2FvKtYuMn0XH6BG8Pynw6JWYccGIjci0K6WQggVaQyugGNnW3IBMe8uCXjDL2k%2F8tTZ2IfuKKKSuRSEasWzr5NZhcsi9vYHKSR9DFN%2BJYtr089YAEmu4MO5fPysRdKHo88Oiu5soMnnPmJxlBhUqId5vh0%2F0h%2FzVvVcIcETmz3C6GqsOB%2BRXVUqj1OrzGFqre8I%2Fr%2FZoXQZCVWcZm1m6UKyaAuxLK3qw1sDZlY%2ForfFBU6tALyjfwMMOPKzZFZD6KuT0hjCiNraS9cnjtR1FCGc%2FDNfk9MlKlwIJp6UqWk4rbfdRFiQvMFtsaBdiykDPA4EYProUaHP1Dd9EZqKy0yuZlaTcW1WDa22dQXN3FATHfYk51aNklRJDwUqHEft%2BLT%2BIWfeqTvLKkub7Rb74urjiYGCMwZ1XgTq%2B6Q%2Fi4BsTAuvWlllElpTUOOcVVXf2EX3rKlm5WD89sNZZcMJU1tS1A2CUVAWsLkXUIotyx5oPCo58CR7JTX51818Pg5xPOGPoO8W4nNgP9VCsbUh0h56mbblls0jrNp8%2Bi8FgWOsDlxoz3sxI%2BTySc8AwmY7kTWX3a4okP5PeIgBzFZBKtyo8UTbi2h4l6JMO%2FNWUtu3Wz7IkBDyB4I%2FDtcUIMJC5%2FbwGOqUBoyakf0DkojA4n9LO1a5gvpoGagBJP2VdfZuhn5Me9bWewKJuz%2BRWtqaa2qcXGtKCobLVQCi8HFG7JUpc6DccEHq7V0d3aY5UgOZEoj7R47ym8Hv2iGZ2GV7Fl%2BV57o84d6KJU8SJQZ4RXtxxWDjEFE4lWA0cl%2FLSj4wAxW0jm2ndmJZsfFFXshQEhtMTdkJO0z8dkecb7zjAw%2FLt2SivUrpq6OgO&X-Amz-Signature=e278671c02cc4cac5462b40308dc6a8a0030b3997ad20c2f434e6776740cd1f6&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DK23EO3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCfMliPzoHm9ay3MCYqhoDEzfPpvTE7O5q2%2Fy2MTJWYQIhAJlyiforAk4cO3NRkNLi4YE%2F%2BUaE5xyGgtEC5EWgdDr6KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyIYJty2sFT1V2HwDYq3APHxLLjIUpkbAwTmHBNJR%2FWKhRov2bkI%2BezNVzvAJhBjGf%2B5MBXXZ6YtnsPRQMXSO2o05KdkpRrqAXo8CXDWA4ZFrVsTdxYglg2tNMgYCnNrG2aki%2BD6ffUmR7%2BaXLLQpCauKJd%2FmyeYiIQLmBKIpjYsuujvHk0MdHRqZqlZkeCqHGaQ8IPR0vWPyEmYcLoRrGTc7BZ2ZhVcsXgjfhKyga9yUS3EJSKo1oT5DvP5G7G9TQqDgLznKHO3TUAbOq3Du%2FbKoeTNUWAQhkR9wNigp%2Bl06gOWHPCPYzcew1ckeeqdQ8r%2FcpSIUcaTi7XEt2mBZo6mx0jsnsJ%2BYkYZrsBVjLqMlJoMywU5WHxWuMeMYhHP%2FVF56jha%2Bt5hm51dhBVtgxwwt6%2FsOX4peyvBMjeLPOxYY7zrrs7PSewzB7%2FCj6%2FUE64hqWTXlb57WA0Z7QjR1LHmJiDrB8L8BdeKZVD53%2FVMAKF1S4VnZSWU9vclMViozARI8PG91bD1pyD%2Fi8VLuqP0nedG1gbYjMH%2BGK2nuM%2F0kZboKFPLqUS7Fpzgukupks1FuNEOXYOkWimGxEfnpTHATxqTF5Z76cXgQkdmHumKWN9UduaFXAtBaoHH7lki7Lt4dmFAlgA%2BhWe7DC%2Fwf28BjqkAQcdBjhgMGACdGGP%2FhZQhJJJpCf4DImz7NbLUgqJfkcBq4LOP31rK%2FdC%2Btq9qrO%2BuufBjVXf3SE6aIFiUMxYvs0%2BloSZ9kgGQOjIeMpynm3CLytlclJnTtkhOudtGmheVxZTGhR2FuFYb9rqJ2E0FMS6fUl%2FLeuFe%2FSENevonQUyi6lyx6SSNhfKzk6nQrLEW8TNhD1%2FsSOISY36D9FVUkjS5rF%2B&X-Amz-Signature=e847f49c71761b82fd741fe07cfc40a72efdc462804f853ab80085f475563a16&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THK3GKUH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhs6lS9GKkaY5JywGAplJVtZPuOIMw37W6vMwppVbkbAIhAPIzIhvsA15GtirHVHMBTLmjv8RBHDgnY0wm9eJ%2BTsdwKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxd52YM2mZrbOPtVDkq3AOEC7LXPL0IWnhf8DvFHt3F9Wjz9rAYMPp2AEw4LExo4%2FMttKjI2XbzWNtgCDvwvyTGeDhzqIUi%2BfmIo%2Fdu8P9ECVAGVzK36y71z7zRiACXyFwcPlBofWWnnQGtoO%2BRnoIBcBatpQoORFosV%2FFLyvN20DZkhddjdHq4Ncbv24n7y7dU4hyxDQHJCRKvxWVREnTqsdzMFf9rQL%2FlRACfw5kE68co462b0TzrYCXUN4c8jUKCJmQpi3FPeYuKiZO3FADxGN9gZOl7fEeeZOvMm99OJoT43lydqxjLS4FDplMaeXHI7xiZ4K3InFZt54DnkB7wMbgZwozELBHeeWfVPx8VJ%2BGwu3LzPRfKRg4cd8NDJZKeaIBdWOKNoIDYar5Ib01BND%2F%2FMDDPKYFKgy5lKK%2BnzKhq8qI5mPAS2CHMLSwPw1BVQfer%2BaKcw8ky%2B6TF%2F6J5D9yDsQ6q8M0HQ%2BQ23egjJKz%2F8dVK%2FEeLB3sBHAF%2FVrYfupj%2Fw%2BaIa%2BvTkONBhRna2CtQoXapMU7mnhayWTXz5IHhQqkPKDsWPB8LnmdXSMJgedz1AgE2Gyj%2FjiXrz5LbKvvEB2ozed6xngSvrS5tdhEm4kfA9jcKbzxBwN1fw353OHW8dROaf6CNDTDYwf28BjqkAdBwg8MqeeX29xeApkVsdnFraE7%2FATryYUCFdRsL0%2Bxx%2FQlXz1xzo%2B%2FIMT01%2FscFwNGcFKp%2FoEsbrhUpHxs%2FLi17t2a7I9uw4PxSFrUVtsdmmRu0AUC7J%2FacqIjwGeNcxbMiX%2BeLqvoPkCXC%2BwucTbRhgMsgyW2zqZ66cSF6785ECTZEFkkx2d6eJXdNxTTFYBJFA4kHPOhesBTz9bG6%2FIv0u50X&X-Amz-Signature=ac40456c5c58f30704282128798bd9a520acf9928bc36ad5463ce5d9faf622b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA7M2MWV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYzbak%2FcsaQE4CrvDZpHfG1B1vMiYVp2mrZ4o0%2BVIVIAIgSin%2Bg59h78p93D9LwS9YwzM4mm4QIT6cFtisksxrIWcqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGW%2B1iozCjdzGyKrVCrcAwCdkfBF0nyPOTIRgbJ5PhUiuzmWaIE4xuxqdEjoAAKbR2vPhgLL00UFcitdtYYzvyKRRcUzUF9LuNcscFP2mp8d7RPmorltnYH9sKr%2BqPHx%2BwJ5nB3eK0ruoC6ZZytLOiVd09NkuTAl7OqWHriH1N6EWJYXUQP6fITPUlsvptSR3HvdA4lAD4PKlHYS0RQmyssGKST4b2xXOHFSbkcfdmH7cPX5VwrK%2BgVPUctzA%2Ft1ssBb9KhCav9%2FeDWdoK3qwHY1gvdzsdrtIWKRGzzFxzS4HkPBs08GM%2BBrKPPw2fxLnhahoWsyl8h0uesj4CLiDh2LrgICN9Cr5k61kuaXdssBeCTuX5SE2GxfR0syfdRc5CL5HxKLeIDVcsAEhE639Gt2IgKokNIfurj03amIAv0Ws9xGCBjcZBhFl02UL3irjpK3gmyWlBQXpspNOHxqiJXvR4MctNZc4Y7JaiBnavOqN0qLN9PIXD6x4Yd2Y2lWDlVJMQZ0d6h%2Bh1%2BbC6u3Eae%2FdfMM9gNXEBSjxVEpHeORUhSNJA94o4ZqT5cxi%2FgToAArnsazRmzc2MAy9oPdZyjxPCCuJeykpB%2BKfrcUWrCmHsB%2BXIZAxyNXjs0sdBJs6uCKTtpwiecbPEDZMJq5%2FbwGOqUBLl%2FpsIW2K1yMGeEqNTFNpwNoRvCNS9FuYuyxKrI6LeuObRZi6%2BXBHq3T8f%2FX5S3p2UMsR%2BABpNzL5vRZ%2F28xHOAOEep2hkYq%2B%2FJA%2BxDdJ%2FhDKCpbbRh75VdxHcc5eRMbnHZl3MA1Tp433hW6fVcQA6lnoXYgoNZ5HqKdOCdFYkbY2N4IOAnjAsT37oW5zLvjkzOBi%2FuxwHOmHBDNbpSmYOjk5dyc&X-Amz-Signature=fed7f1eb05e081970269bd9609628229d0e271c00b334d87c415fe0624e938d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW3TTWNI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD59bTOm22lkToJ%2F6wOT%2Bw7HeN%2Fj9%2FcohfLZxn%2F0fvJUAIgG%2B7fBLobOXj9oMIxeVmluAIAUPf2UgIbsEWYb%2FDnyBsqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPr6L3qgIyBqKkyOlyrcA%2BvalQ1w1dlunzf%2B1xth9q8kO2K8vtFHPl1mY7vt0nIMG%2FKRZGlICZaTpGvTsJ47OYgmY51DEQdPl5P4NMiHWHehCYi6tn4dfhvD%2Fu5o5StlYns9g27JMiEzfDskp%2BCP%2FyBgk8fr4AZ6bnNVirlMRnZX2IuXa1S00Wt6pYvIw85yfbh%2F6Q%2BYhrT4%2B08%2BijJkhL4VKi0tMf5Ryer7Qims4uiArODWqS40MiTeHTFVTVmdNX5itV2KEkvWCxGFGMri%2F0oMBsFjnaIp%2FuhGCXeh%2BxlNWkos2sdtItNOa6yWXr6VIXYpf5yTUfDJaqF8GPUyT0ESvNkuorcJUFAWWF3ZUKNWob2IArd%2BdiuzIRnG4b7cGW5Hgi98NGz4g2C8ZG%2Bu9n9KtNi9KTKO792LaBwD7GyCBX%2FBq9NbzkHB9Bk1ACqjU58WHWtM9HV2lhYKFj8nZrTO1vDKM1FheqDwrScNlqDFZapk184pBAtL7hp2DLF3%2BKBEj6GOyrMZJRo%2BKEp8pgZn4vQHIZs%2BSPiv10fTXT87C6%2BmqeSespxkXN1cpfxDp1%2FMX8bONz2G2I2wSxQgthygCzGBqdtRm7mUbOuLMxOe176dKETQpYMsIJEpQdrnJsDqu9ejH3ojeeWnMN%2B6%2FbwGOqUBT%2FEU55kFJf6qBigHReZs8s0e4G7gP%2B2BMmT1nzmZPCHXr4VoLqsc0LpnKq9qOOR9hFiN6uV6ZyvQhjep8HrtoMk0vYstextdS%2B0ej%2FewnryTHOl5nuDhIchHZzPWGLl9Rvs60pP2JiQ6b%2FgAlM6kFlj%2BtyVUqHrla6OCTZmx5Ezc4Hz%2Bb5agUSYkipXveO%2FU2yXr6OJePhzl6RAHtyYO4f2VYOT8&X-Amz-Signature=673c38a5ac34630fe057e63c5b619c7a472f6f065e20c948acca23c53abf840d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW3TTWNI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD59bTOm22lkToJ%2F6wOT%2Bw7HeN%2Fj9%2FcohfLZxn%2F0fvJUAIgG%2B7fBLobOXj9oMIxeVmluAIAUPf2UgIbsEWYb%2FDnyBsqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPr6L3qgIyBqKkyOlyrcA%2BvalQ1w1dlunzf%2B1xth9q8kO2K8vtFHPl1mY7vt0nIMG%2FKRZGlICZaTpGvTsJ47OYgmY51DEQdPl5P4NMiHWHehCYi6tn4dfhvD%2Fu5o5StlYns9g27JMiEzfDskp%2BCP%2FyBgk8fr4AZ6bnNVirlMRnZX2IuXa1S00Wt6pYvIw85yfbh%2F6Q%2BYhrT4%2B08%2BijJkhL4VKi0tMf5Ryer7Qims4uiArODWqS40MiTeHTFVTVmdNX5itV2KEkvWCxGFGMri%2F0oMBsFjnaIp%2FuhGCXeh%2BxlNWkos2sdtItNOa6yWXr6VIXYpf5yTUfDJaqF8GPUyT0ESvNkuorcJUFAWWF3ZUKNWob2IArd%2BdiuzIRnG4b7cGW5Hgi98NGz4g2C8ZG%2Bu9n9KtNi9KTKO792LaBwD7GyCBX%2FBq9NbzkHB9Bk1ACqjU58WHWtM9HV2lhYKFj8nZrTO1vDKM1FheqDwrScNlqDFZapk184pBAtL7hp2DLF3%2BKBEj6GOyrMZJRo%2BKEp8pgZn4vQHIZs%2BSPiv10fTXT87C6%2BmqeSespxkXN1cpfxDp1%2FMX8bONz2G2I2wSxQgthygCzGBqdtRm7mUbOuLMxOe176dKETQpYMsIJEpQdrnJsDqu9ejH3ojeeWnMN%2B6%2FbwGOqUBT%2FEU55kFJf6qBigHReZs8s0e4G7gP%2B2BMmT1nzmZPCHXr4VoLqsc0LpnKq9qOOR9hFiN6uV6ZyvQhjep8HrtoMk0vYstextdS%2B0ej%2FewnryTHOl5nuDhIchHZzPWGLl9Rvs60pP2JiQ6b%2FgAlM6kFlj%2BtyVUqHrla6OCTZmx5Ezc4Hz%2Bb5agUSYkipXveO%2FU2yXr6OJePhzl6RAHtyYO4f2VYOT8&X-Amz-Signature=4f5b6170f40bbaa09495c0c91ec4d1a7ef4076b8d4f6636e5dc219c4bc5246a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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