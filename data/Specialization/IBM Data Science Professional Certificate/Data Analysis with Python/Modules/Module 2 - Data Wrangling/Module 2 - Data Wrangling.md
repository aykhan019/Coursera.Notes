

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IRUX7RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIDzAreKOo0%2BrdUNt4NSs6WFXQC%2BUVtk6DOfGe5o3UbQ8AiEAtTmXsasByST2wZWJAtMCcsGqwOLqRE8XFkbpwY93jXYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDENXFUzkQUt133y%2B9CrcA%2BdSu2CnkduXN%2F5V8IUeOtJrM4L6RIz5eH2Etegdkqaq6zg5ZzK6ATHI8%2FMRLzkV9vOQUZtRtlj0GHaWXXveg0eFXAwjrdHW3SBW%2Bp%2FF%2B%2BiGVQm81hlH%2BMwj2Kp%2F4%2BKtmrNKztU56iEPaKGdLAVPdLppdDPwZQch2eEk4lFsAJjwRHX%2F3QNwtpdiJs9ghjumMx3QLU%2FCV1l3SHeXlP6sgN4WCQsBvvzECdVRUC%2BU58yzg4AJx0QJILfTLSe3iPJ%2BxYhje9TZjj71Kh%2BNsD1gbDze3zOxYFhtjyH7znvK7gCTq52%2BXkZcaeCylCy0Q34aaiyfX78%2Bsz9vTirmZKeaw2chRNzeCCf1JM3hKEV%2BLf%2BrqfxUhz%2B1xPkACzMCvA%2BDJlssaGx6veDWdTVNyRgG%2B23UoFhxOiku%2BvYz4m4xBAlrtBITM9qv2ZslM7GEYdvvZ%2FF%2FGvBwD9x4IfXmOTGjww%2BLHOzkj3g%2BB4jWbkYTlT6%2BAnVePgiJcp8t230O%2Fd2hUT4h8FssAtR1vCG9eIzFyk3ero7jvALFar3T7rsZw46MyWLhxbciVePg6T6UpBEvCwSDL95wzuwlP3cOqpCmMSdYvIf4yDTHlsef7AZF9jR5dgiIUHv9QzTeCLnqMIW75rwGOqUBYQd%2BP0XCl83%2BQofkp1gw%2FI6DgljNGOHubQTmk%2F8Kimisy%2BNM2UiNpEe%2BMNu%2BrBZpTJ1meaEi2M1OcbVAlJAjZ2Z2pQO5RlVftshfdjrcno18dcp5WOHsOgnAAkRiQjvS%2FOdaueJx3F7rxO8cK0c9oR2jTak2w2zCtbiINfzo7sABy%2BVRQ0Ue%2FlWl9Kz7Br0vRb%2F6dwWWEZDA233xwht28guHEWfY&X-Amz-Signature=53cdd1170958fb04d85ce70dd7bffc85fd88b5755f29533d980e1b606cd2bf4a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ5XHRPG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFBAVa%2Ft9OXuA%2F%2FiOLisF%2FV1HMlH%2FZIouEXdMzrpT56dAiB%2FmXPCs%2ByCmMbjjDYMrs%2BkvkClBxsq0l7%2B2dCSTTfrlSqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC4w8KRAHrSjdHibrKtwDjO3MocJ%2Fe9eloRjYoHk9t6KlHeuCAxkNj91TcMrwGK18rlbIlmehlwWXgUqknTZBx3S1ce0YPRglniXKXbVzn5j7PatdDCGLM7f8tkH5wjXol6ABkIpwZP3tBX77Qax2X%2BzP%2ByoeDNktT7CuSz22a13gJ5HpcLsiI8JVj7RQwVpjUetjcdEhfEAjpVaI3XukADKHGSGIdk%2B9itcDqtOMQG1xcXn4%2By4n0hMDDXs7wf%2FBfkeaUCCtGItoftinWFTfDTULW53GWuPSqcBnPi4YN326hEpb1FdNKdlJofYKeCJPH7ONne7SGJ%2FA6h2pnVPBqPw6npfZa9gjnn5o3xUfh5Zdl001NW9QO6dtq3ViqDQ5cVHqBmZ9RY%2B7126%2BQz8ToB6hxyzlwzetHV%2BMGUxpOnm8%2F%2B9UCJe2sRWaeBiN%2FCYDgyapOSHEksG6j47D8gNg4RRLPBGD4QvuScaToNPpqHwt2qwfneMQl0l27%2B2ajFTpUc6WQ3S0pJ9JcdFWYL1FaX%2BjiC0lqm5jFRwXr5tsuCzzIeE1BO0K%2FofH5kYm3N%2BhlKhRp93xcU6%2FHeBu0kA57Ul91MSUCog0KO6C8IyXx%2Bft%2Fk%2FpaK4NHL6bju7B7Oqv5QHjbvpMMGYShOIwh7vmvAY6pgFYxKuqFmnPkQK5GODh2sIpiWBiqjkwTVAGqP5NrvPCrN3%2FYo%2FOhgnYvGCp5XZFJRr%2FHw6ZBvlv0ID%2F9keq76Qu3patuRckGkeDea%2FmLfdn%2FHXO16UGwUhCS8ZIG8NK0kfaqYD66uuFQOFakbYgYaTzSelY4VcA58bfBEnL0SXzOekqC1dyQlWZyJ0ix3PGBA9L0lugp9wSH23hP8bL%2BVYJrwr%2BrtzY&X-Amz-Signature=6a7943ac001c3a9afa8618c85e9439dea2578b518833e8f86ac216de1f8deb1d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVHQCCXJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHY1xa%2BG0zyrvvM8app6dPrlktGFBEfl%2BeFiA2bHSKZxAiEA0l2PE0y%2FRvykUamM8dZPR98F3p4cpd543f%2FZnHOFpbQqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDY5sLUXRCzlre9jYCrcA%2BK3x4QMRYm95aNFJ7kk7wkARC9bzx9DaUOhQgjahzsRLRI98N%2F3vphIfY42R0syuM6%2FQH87QWtkTh%2BejrGkMaUK8glkuOmex%2BrnyxWzezUBCkoQ2EXjde6cO9nLNLg9jfjLtFIwvwd2BmLbFbX97RnmPkl%2BcjyMLWoGs2F2W%2BZENO1NP0U5a%2BNXxJAP%2BtaPIfIBFJFpklnEjXRXF716KMd5dBl%2FkA7Z2E7oshA73kMzbC3YrN4n44PQ36%2FHbW5mrNVXMi3uyHvU91YnIRnji0yApQ00w76eWoFa6iPkXDM7ejJtHZourhxvzVeXdY49iRovwm9tGPiEHeNU%2Fn%2BY3PQNOYAJ29EdJMBl7jd0lk%2BKjAQN3CnZ0q2FdcbcwSTq0GI6vkj6FElHGbJQeHTT8BZphCpATCADUTzjtz4yDRS4SwSD7ErgTL7tn3N%2BQ6xszdylbmwQNgOcbwzMiVdvAPveLSjj7RFHar1l6f3hHKbEkLqO5qXSA5Rh4tD9sYtetKKXwDOOA6ga4nT5%2B1j8rELF3tHyS45OpqMV0%2BR%2Bf7T75swrs5yGawJoCcG6aIuPDw3GM4MxgLIE2n%2FZvdiExZPgR%2FNkgHOww%2Bc1tkQwLanJEjKPM9O%2Fpsm2EknYMKC75rwGOqUB6KVteiK6lz3uman0%2FzzSebnR%2BEKYPrHLBfl7MSQKBi0nadpo4MQdxf6osWjM3GAKrPCHXvmHpWdXTlH5sk%2BMJ1oqlqwPfxodTt6cHE%2BCCJea2ctavzSxtGDSQ5gAehzpm5b6P9Bhd6sOzk8a27eAa37EkDaUvCrPGhpt5nNOIL4dw%2BDuzooVUwbfTjv3E063%2BiEhBxBHwJhlr8K3Y970bd2H4sPw&X-Amz-Signature=11d71a19a9bbe1c48e997a4b500d417a839414a954d67f14ff37e4081f73fb89&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQTNUHJB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIESjOnojhWQlNm9jHnbY5cjKrgdITG7FXpRI%2Fq4wFEN6AiBP8IFi%2FU1ttNoEg%2B5kIDlDpKoMXOeiS%2Bth6D1l3trVkiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIhkFJMXDojT2l3VkKtwD3Ft7C51PnwSHe31S0z%2B%2F8RQXbiFwe7iLhIlswja%2FSfK9udbbfWVVgXfS%2F%2BqF9cnYFdRGJIR2t9Lhivb2Hqz%2FoXF2In%2FY6huZ1O%2F%2BOJExNRf79MPPdfO4bjWerJyx7VpmAqmElFG0XJ76GKkVOFLyAxVt%2BgV4VqUnVd8LqPaPpKr8g8ajugkWv4fqWWc9rx1VJgi7V1PJtlZ10BGyKOZqcOouz1qYmcmyhoQMJbGUv%2FFcsiYedq8Uu8oPa9WYVzGusYdXgikKt3N%2BnNj%2F44AxN9mii%2FQoFoROzdkVBsMDPqSw5U51NZJliuaDENP2isJA7RbPzfZ7MfuIYVEZGBOe3Smdu9kGsSSsaycetxw7DtYUc1QmZ6L9Zw3UpBZQSYFoV2wdXp25a%2FNblQjtw71itl4dnn0QIvtSAicAeI43U%2FpE5fOEt2Y%2BUZ0QBz4hz15mZBI0e9JVRZ39BbdL17Fkkxvy7kKbPti6Spbqorxx2b7GC32EitqX8ZyRtpMPhGAN4hXZDemd3YH9SkZl%2BUdmMbjrJ7jV5QP5ZDzl%2ByAFijaJw%2FESqEefDQhUN8hGXpK8uAp2uqksxZ1xMT9MCy0TvMGTuOhSilqMEu%2BoOcrRZiEy2Lj9D8UTI4zUlg4wkLvmvAY6pgGzTtNTcqmJrxfkmFpoPI9i9os2xHwviNrxHKIJtaxz3d0eLQMxI6UZn8Wg5LWVNKq8gZ0R9yq0hXK0ATkse%2BBrdlZBsEyX9ztrT7YTLQB4O0EpSJc%2BDiLbKQXuA%2BRtPDCRW%2BPINEQn%2FufKcasvdTS1rIaMXoSxYKBSRzxQSW72tb2PUHb54hvZ6%2Fx1YxFX%2B9Idj9BBJYNjgTNFYsKGMuwIDQP1obEq&X-Amz-Signature=9eec3735ced51ebe4a82d748a0dfcc29774f7fb62dfcb2bfd3791bf46819b5ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CQN6CHE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFioteqqEj%2FfOvktcfwsTfSojQUS8tauLfIklpE%2Fyi%2BnAiEAqRe6ea1kM%2F6dqn19ERIi9CMWLsWASOfgi5XWhrwhWlcqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIJSJ0US2wdvZPcmdSrcAy4XAHK6kk4sPIXQLgHQxACEwVy8qgNDiG%2FpwQtQm6H2e%2BJ6KiGiHHdOu0dRqRNtGSJX4iBr69L0jSDz%2BoPYr8RGIyEWeo6sbF%2F0Su9Uw1KzvC8X7HAaRBOyW%2BTphehZjuSCxbcH0MV8HjB2YjnE32HWxt51RMJ%2Bqu%2BJlfWo%2BgLpYu8ZcccLJgi5KZtRsv3iWes7U3igVFDqlyCgMj3SGQmJqM%2FwksB%2BGCse64yRUXzBgVryhp2B1PwWjwIFGYAzzpc%2FDIIPL%2FO5293l4UVQOal0Rdx80Z7wm2hHgKKmiAT0vUM0DhCh%2Bwxipn0dnmFABOHtV4z1FyCqQREc%2BoCakYhSaM%2F4i%2By3IxJpblxXkErhAXQoK2lUZzZ2UzMQxAlu4a3zz1WvDAx0ZIwd%2B2dIzd924M62bX1JRbrUOKtL%2F0vrttErsBblOHekNobaD3Ysa7tu6HqoL5ma34uXrsu5NW9mIuNCPw31hM5pLkRVowpmxQIwatTDNr7C2SV2JSenjym5%2B4sT9NFol6CzshhGnKmDcfphjFv0rZnQoIMOzooPNc8kRJlvb49uoDHVsTcR25juas8DowUrIqRTwmEwkfj8380fgo1VyVBv7HcTom2eNX1AQltw82WJUo4GMKC75rwGOqUBzGW5zawnyO8dvIg95d4LDtgu%2FAZxUCFBtnoMQ4A4Y78SfZC6A6LRY%2F%2BUh3Pejjop24c4CH01UU5vyQh%2B7fY6KCjRkEb8FOKiZD3GhGYAV2EH1mLeXnashFVESTarWRUtxyf8VcKlaLI%2FQiwbtsUvpIBPPwsKlucMxVzBkU55Xrbf7x8geo3GXacNqCf%2BzHgEsak8CR1wfQrpiuV9Gol3cduUzAxd&X-Amz-Signature=97a86d4b2a766bec7a1ecdb0700966f458a88b3e835d24efce1a27884080abe1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WKCU7WB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFI4XErb46l9k2wJa1ps4Pw51dyco6GVQlJ7sk97gPedAiAu1L0tN2RBJ3SN7q0gEoAnVdKTMXnOMMMuQX1bpfVvFCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUUxnUhQpcpkNVv0nKtwDpWbARzPsHPFWCXeIDpgtIF45%2Bzpp7XTKUeysfoR60URXo%2Bm9OY5EXC9Fooj%2FKc6jafBnPAor%2FHTv9N%2Fy55kkTiG42rak4u3vjjmBVmzVcs5LkBIpPnR32Qva6groKawRixE939Cq9FjWmOeAdCTDZZ6hwAZxY16rxQNLDH%2FlRSC%2Fh1Du1yJd3UfDmfektJTYmBMfUHr8G1jO7K0JdQW6cAgsCGIJSpHUCL0pdKmWNwQ%2B08gATTBIobWRj32kHN%2Bo1cgIbbMUaYcaP7Z5VFJFZXMhsGktxjVPuoIzebuj2XxkF7%2FEvQs4ZIu2FY872kPnT0YlJjGFXqsTOYIGa6F7SAzekYFxfVG9sgzF9p0oHOQwuIohhMPJ7HEWGTClphUly%2Bzels9U8lLbAQFsMJeH%2F7V8gwRIr8PkjCjlQso%2BlHjDMpBerajOMhaMGixAEQHT7Ji7vTLzdZavJ64Wed76FJevUT5DRcCZylKQMsfLQ9FudYv9SCYjI6YM1lMCfRY54vfqEdw7095MC%2BWCsKyVMNL%2FpUX4H1SXe5mohw5Rd2kBj3YnYmsaMblzvM9%2FYWX6UmbHg%2F7GN7cb%2FL%2Fxu2sqlxm%2FOvt%2BoWuOztAXEqrwYvP37y%2ByzEjbigoY6qgwm7vmvAY6pgGoITtmeJloa8YlkCNdc8olNfsFCpRYTBY0yQU61pNcA23wSFcj3yxN%2BXMxU5JRtREISrrHdkj1CN2PxKNYod1w3pbpKTLzqipVoUyI%2B7rWTs5o1dGkxlZJu2E1i6yT%2Bh3L%2FtGvyb2pQiIF7IYToMxtqXYD12rLsxz136mqGFBPhQhaEDJcUWbEuPtjqSOpBV3w1bEom8dEfbS%2BfsA92p2D8KGYvsrD&X-Amz-Signature=21805b25b98505de8a4a10cd4b249092b9a307f8ee0027136174f1faa43c6b75&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMC6AYSR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHmqrSkaz2YIC3FmRVRRImSFiZxBAv8qNxypBFGDcB6FAiEAyFW0vr7Ytvx3Ex5vCPasQ9kDI8RN2UciYwypZNjV0WcqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLjlScARsHVC0JzmQSrcAydOvr8rlS2YJG8wY1eUfAHRfwjnPA5j%2F5dxWJoeCsi1H667Rc3a0hyYnnfoGTaMrCfbR1M4i4gDWP%2BBNOYH0Uhvm89eTIG%2FZx%2FYAmPt0nkllupN8a3OP96n7M7aBqs5sG5%2BR89h6MUp2fDjFhw5Ton9W2N4XXIsEdfjFnSiejH7YYgRqvYKcvvo%2FpbRlVn9W9spYczQFOdw07kPiiiWmIJ3Nbf8oSOxrrStpDxbappQpp0VAa8g9DmhGBic1NVwvJmMiOYSb%2BsUOkeBN6ztvn7LiG%2FYYGs9rYmd0xaBNCrmmN2o9N9STJa6kcGs3MOLGiTYtKhFlkzWVvFv8FyHdXAgb3N7GziF5rL1d%2FLEYZVOzJRRvRUZWTsetZapr%2FDTdi%2Bf8zIYquVfUOA0NEkmL%2BBauAaq5sDnd88TGPrRaTG1ysKXH2TriYnOc2bS7%2BWGQlYjz9HRE%2FTvmvvPQuJiduY2fNJNFhVdiJ9FPrVRTI890FVN6SyZl97Ko0rZn8LjmLfnoCHsvkfUoNcBF2kO49DWl2UUADWHDwjS%2BlM1GeldketW65j3%2F6Mx6P3flOSDkY4RAc06AyKUdqVTeWabY%2BX2cS8R3EED4EO5VfTHTp7tsxkKuneC9VHhBB9LMO665rwGOqUBSo9YHnUyzy244G%2FnplnlUgSPlUBsxqEDo9MWpFXdlJpqpOXJ5W5j9x0ORiOZGgzoVzWEHnF6XNnB3s1N9I6u92ZIXQlVqNTWaR7FCYQmv5fvK5BwZqJzUEoVRBiAUPWVogrrf1cquNAvi%2B%2BaX5XvRXjejOu8L4J4zpsMYo7QHYVx8%2FVhl6m1tgn7Qq2cV%2B1ydTHN7EQb1MammKUQBhUoIcZ6L%2B1n&X-Amz-Signature=c5dfe032f69079ba0dcf1e1d07dae3bb76214fa087d4a0677034383a294b01ff&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C36I2TE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDWaxSYlkW3qDnQ7K4rVOp8h7O8yFDibNAzF1FNYQMN8gIhAKnf4N3JYgVN%2FTbZgfTIz0vfHtwsPAvtvBXxUgB2tA1UKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwtU7ke0I9958oXuXcq3AOcCD6KSDK1svU%2BG%2BU4tC4jkDo6rw0oq8Z79q2VzlL%2BSpAScA10CD5XNExtpcPZh0uP%2F%2BRzhmUM%2FfQbYI1p7299SSnGq%2BB1qH%2FiL42icbprMDdS%2FT0MW37t0EED34ENZHMOyk5y80ysQyOL5Qx%2FEM7C73iazXzp73v47ZS9wF%2FiTrlV4lNXaxEXGI2D8GZopLXK6Xl0FCjRMnYzIMseEKm4hlerUi48kPJJHI1zcqY9htkuV6XRtkwCElrq9LS0vDFcHZWG%2BPzdW0gKYwLdw0hkinBQF69zTwIFhbOneNLAAFTnhIjmhPLQlAiZQUh4tB5hsK%2FE%2BiHx0i8b01EV9WSqP5iPt%2B7okcKd4ui5Q2W3aaeuQ0WTM%2FzZcTfLDa%2BiJLMR07PZll80vjtlgmxlGOxYpmLNm2CJuXQWQ1xUSVjsbD9ByH0Np7anYV2tx2xrWfCKr99rvyUxYXR%2F39EszC%2BAP82hBL%2F%2FXWSU9doHuvd3nldM4MDMPqp1mtwTE%2FwGC%2FsbOnN3iC9yhlcCdYFfLctYx2Qe3CgBvEOjq%2FqEZFTHrsdJRq5%2B3taH9boa5mxJeZj4afTWdbVaWHv5pYdKekIbp%2FwiDP2TiXt%2Bg3iGn1A9IuGX7cAki2FSNzCDQjDzuua8BjqkAY7QOajD3YphwwAUWvzo9zovWh%2Bpcs7D34ICAuPg6hfuyIwx2y2lwHgRLin0KXrWCiI0sIbNSATVZddbT558Iz%2FO0onP5TIfnbn30KKqxja3RBoFwS%2FAMwLVjA3OS9tzYlJ9blVedugUAf%2BmpVCzYS3RuNV7oNyCEvnCHbFuIX2dqm%2Flipj0r3C4nh2Dyl91hdv0NvU4EEZGnTE6B03pHZNKB2RJ&X-Amz-Signature=c0f93437e659c9cabffa3ffb3bc63315d604206ed6003cd7d3814fc24ae5e16d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CQN6CHE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFioteqqEj%2FfOvktcfwsTfSojQUS8tauLfIklpE%2Fyi%2BnAiEAqRe6ea1kM%2F6dqn19ERIi9CMWLsWASOfgi5XWhrwhWlcqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIJSJ0US2wdvZPcmdSrcAy4XAHK6kk4sPIXQLgHQxACEwVy8qgNDiG%2FpwQtQm6H2e%2BJ6KiGiHHdOu0dRqRNtGSJX4iBr69L0jSDz%2BoPYr8RGIyEWeo6sbF%2F0Su9Uw1KzvC8X7HAaRBOyW%2BTphehZjuSCxbcH0MV8HjB2YjnE32HWxt51RMJ%2Bqu%2BJlfWo%2BgLpYu8ZcccLJgi5KZtRsv3iWes7U3igVFDqlyCgMj3SGQmJqM%2FwksB%2BGCse64yRUXzBgVryhp2B1PwWjwIFGYAzzpc%2FDIIPL%2FO5293l4UVQOal0Rdx80Z7wm2hHgKKmiAT0vUM0DhCh%2Bwxipn0dnmFABOHtV4z1FyCqQREc%2BoCakYhSaM%2F4i%2By3IxJpblxXkErhAXQoK2lUZzZ2UzMQxAlu4a3zz1WvDAx0ZIwd%2B2dIzd924M62bX1JRbrUOKtL%2F0vrttErsBblOHekNobaD3Ysa7tu6HqoL5ma34uXrsu5NW9mIuNCPw31hM5pLkRVowpmxQIwatTDNr7C2SV2JSenjym5%2B4sT9NFol6CzshhGnKmDcfphjFv0rZnQoIMOzooPNc8kRJlvb49uoDHVsTcR25juas8DowUrIqRTwmEwkfj8380fgo1VyVBv7HcTom2eNX1AQltw82WJUo4GMKC75rwGOqUBzGW5zawnyO8dvIg95d4LDtgu%2FAZxUCFBtnoMQ4A4Y78SfZC6A6LRY%2F%2BUh3Pejjop24c4CH01UU5vyQh%2B7fY6KCjRkEb8FOKiZD3GhGYAV2EH1mLeXnashFVESTarWRUtxyf8VcKlaLI%2FQiwbtsUvpIBPPwsKlucMxVzBkU55Xrbf7x8geo3GXacNqCf%2BzHgEsak8CR1wfQrpiuV9Gol3cduUzAxd&X-Amz-Signature=f3d5b4e88d63338651c3c1e355a2182822600ef1fd94703c1e74f1bbfb04b624&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEIK4HX2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDw4ZMVq5Ffw%2Bi9E3sWvPVUojNFHOoDlrBltE8%2FimSUZAIhAPfy%2FRmeM8urv9%2BQFXsANp5Vde9rThKdNNrwiLJOHsssKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxy9Isqh6Wrl2NSbaAq3ANHqXOeYbP9eoEnus77DogY%2BqgbCk4qIxUUSr%2FhERM4tWYmnN0LBVs%2FDmt9AHUdFrSMT2sbvv73qY3VoITdrhR94f16WH5iXcbWJd8ZU0ADsJ0Q0RBnNuDlLAo%2BLhf%2FWXFQW7uDYfcx%2BzndU%2FFdDbTHkjZic%2F65z5DUFd7GMeMOMPmVWUdN%2F1RoF6j4z5ladxZcMYJiTkO90%2FSMAiKoOqmMTxuO9czI%2B1G%2B92sKkY0lHVMJf%2BzTRKMIUPMgOO7TqqsKt%2FCUS6bsTsFVZt6%2BEeSI7nx0B%2FQQUwTx%2BQLBcqglKCTz%2FexQblaqyGmsvE5H1%2Fodh%2FgDTmtUM70jDFduEGPnr8TAKg6uBsHF3wZ6tjzDAxpYJTVgMejwTWqOXOE%2BQLcBsHxjSij8fwLoE0e8iQBgTK660FqRj8NnXP2mvLu5FxhZEv8Gvu0eRVl6LfrOSWihurGVF%2BlJHvHQBPmUqpOCftThCYU8EX%2Fd9Mei6snVnsZ2bjiF4V0sVFNsUfD38VlBrh%2FOIOxwe2T6bXWm9yK6bV9JD9bQRSXRM2lmh6MpyQoMoCGOAw1pzQIKAsEaHbJI2OLQpm6Uxq1C4wskOoPc9UfXPsfFKigl5Zvf9iWxXtEqpfzlskkxG7W7lzDvuua8BjqkAZ9sat%2BG2iqdTXr7XkfAXJLAE7SB3itr9BAVc4CHqcUOVsB5CtkCkeT9SjCmknNSCkA2GygZ5xTdabISYXJ6BydSMyDMe5kN%2FuPLZEfx33v%2F6w1VH1R3IJEdl9AK3ojzXfoE9cpzmMqnwp3BcS08nh4IkCvmr6%2F5YAl8j3BTlOH76PJGI2GYUru0G9tc5pXiK%2FkVRxFR9COJbzh8D1Fbwqx5hjzt&X-Amz-Signature=d95f42ca8703be44d9af77ed1deb55ca552989624346957246779504eabbafb9&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEIK4HX2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDw4ZMVq5Ffw%2Bi9E3sWvPVUojNFHOoDlrBltE8%2FimSUZAIhAPfy%2FRmeM8urv9%2BQFXsANp5Vde9rThKdNNrwiLJOHsssKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxy9Isqh6Wrl2NSbaAq3ANHqXOeYbP9eoEnus77DogY%2BqgbCk4qIxUUSr%2FhERM4tWYmnN0LBVs%2FDmt9AHUdFrSMT2sbvv73qY3VoITdrhR94f16WH5iXcbWJd8ZU0ADsJ0Q0RBnNuDlLAo%2BLhf%2FWXFQW7uDYfcx%2BzndU%2FFdDbTHkjZic%2F65z5DUFd7GMeMOMPmVWUdN%2F1RoF6j4z5ladxZcMYJiTkO90%2FSMAiKoOqmMTxuO9czI%2B1G%2B92sKkY0lHVMJf%2BzTRKMIUPMgOO7TqqsKt%2FCUS6bsTsFVZt6%2BEeSI7nx0B%2FQQUwTx%2BQLBcqglKCTz%2FexQblaqyGmsvE5H1%2Fodh%2FgDTmtUM70jDFduEGPnr8TAKg6uBsHF3wZ6tjzDAxpYJTVgMejwTWqOXOE%2BQLcBsHxjSij8fwLoE0e8iQBgTK660FqRj8NnXP2mvLu5FxhZEv8Gvu0eRVl6LfrOSWihurGVF%2BlJHvHQBPmUqpOCftThCYU8EX%2Fd9Mei6snVnsZ2bjiF4V0sVFNsUfD38VlBrh%2FOIOxwe2T6bXWm9yK6bV9JD9bQRSXRM2lmh6MpyQoMoCGOAw1pzQIKAsEaHbJI2OLQpm6Uxq1C4wskOoPc9UfXPsfFKigl5Zvf9iWxXtEqpfzlskkxG7W7lzDvuua8BjqkAZ9sat%2BG2iqdTXr7XkfAXJLAE7SB3itr9BAVc4CHqcUOVsB5CtkCkeT9SjCmknNSCkA2GygZ5xTdabISYXJ6BydSMyDMe5kN%2FuPLZEfx33v%2F6w1VH1R3IJEdl9AK3ojzXfoE9cpzmMqnwp3BcS08nh4IkCvmr6%2F5YAl8j3BTlOH76PJGI2GYUru0G9tc5pXiK%2FkVRxFR9COJbzh8D1Fbwqx5hjzt&X-Amz-Signature=84dd0982534618e607bdf22d07b288cc760570d5bcda023c91cb6c6cdc0f5a77&X-Amz-SignedHeaders=host&x-id=GetObject)
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