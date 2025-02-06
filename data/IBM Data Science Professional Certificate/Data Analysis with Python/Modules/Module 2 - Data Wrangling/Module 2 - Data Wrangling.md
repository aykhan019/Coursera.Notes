

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FHOXGCU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDcTcAoLhqTEGep0IcXyy3SUc5oHDfyoPBSUOeUa3HyQgIgOiYytpUV6IcB0i5LXfT7lpbUo%2Bw7HkOSrOXVCr%2FDvskq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDNsuwDYv9%2BtEd93smircA1gAv8RhylPKsYXulRVJ%2B%2FcP5dlwqRQACKiftDbWG%2Bepu%2BAWFhQe0ppTx%2BLIwepAR1Qtppy5FMdrfvWB47V976k5YwsqP4ruM7UOkFn2CtY%2B0HTwq6T%2Bmv2zAYfB5c%2BZvdBke0T65kFl9Mw69mBCNzqhw%2BJiGaV9%2BED7yAfdhdfGGHijNg6iMw4MumgGRAj1XBT02x%2Bzsbr5uYD0ZmT60RL6Z4jTX2h%2BJlvuci8zGRAC2OohNwQW0tzXulQ29khm1dk9ETbBeVddC5AAcemMWmbS537JLvgwIMRXBwKxhZ9xzLQQ8IZ5cq%2Bea9rRKjv0nbO4V7xuGSmf4pTwXwnZB4cYYcixYYsJuTLbyTl%2BkYKVfhcIpwbksv7%2Bix%2FO6JoR6i5jkay7bSzBCUiGRwgTcd4PwCbWg07BN5csmOCVmozcYXVzI5JxSJv4rRH%2B2nDCI%2FVwNCRNP%2F5P9vDjWOzO0DDjyU6ie5z3oQ1oN2X9M0l126HSd%2F6qIaCuMIQSNS0hae97mlQr5AWQ8eO0f8P0Q%2FLKRhL%2FDUTm51glfOcxgTw%2BQef0gzMzZMxKwur%2FtszCIy59%2FYHVoPJi899yHw6yHb2HbGr0y289mz0hdAKtumtkKxg%2BD7mhD%2BtFERj6MOeYkb0GOqUB6uLLGHQyf6wcqvyHBEgg12n0ytHWUFQ3HmVjpE2IMOAuuC79PcqYhGcbq29scTdaTiYbKbDvr4W1CP8BEuMEUIdYXymfvjLflS19PQK1O5OIngznbjHsfgsfWO1y3BNgn8dWm4UK8mHkYoTguEb5YM6Ry3RtLCINX7Ok87rrbVlOpfyf3h5%2BdchWN8DMBMRr0lhds3lpG2v98VKQAydvde5bqBVr&X-Amz-Signature=53955c62e0ba8a58f0d2b5f35167f595f0d4b9d4d3b5e8806b790f3ba04b4fbd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SZ7KHOB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQCfncX3niza3ovqQjjx8GQCoejCnCULVSjTPcakdPtO5QIhANEYGHFXu%2BGGp%2FcNQIMDN1UlfpfNWnkT%2Fx7V%2B0OsOqR9Kv8DCFcQABoMNjM3NDIzMTgzODA1IgwR5BxSXXD%2FnQmCyn4q3AMrtu57QxsKkwiwNwrc2v1VkLKT6G%2BGWQsgqblioZ7oCv37ozZaPy%2BzIFFRn1hpClb5bc4R4jhuAxklPb91AtoGoCSrIXGI0dKWldRNlRRkceH7R2IdqZDPKl16g4lKI4KwF0fzakvfjLkWdEF8smbGksCJ3fiu5XQRoX3sA1VhG%2BqfyKkHFFWfh0La6%2BGgGT%2B8sek2v2bDW5499V3usXHwRI0KAsZegToYPYrErXx%2FMuz7PxZ7%2B9AlMyYgjyGeuT%2FimJrHAnEIgdI02OrmfiuZ47SCTB1OwtCCBUdjSBsWq23RanaD3Gj1UjajjKactHa2Go5sdgSBWgy44mJiPqKnnKlqeGti1iR34SwqF62JB99ujoSv7HrKBmaif%2FWNwQXcbOM%2BqipzNa4ECgDu3AvLMhIrnzAGlRzb1vPMixpvUymgZBmWSw%2FirWck5SXQxUnqZQeC3KQ0HUYuyaAMvKEd4sCkHtgL36S77W7CFM%2B8zHHdyNoQrAP17B58WCLh7xGYWJEj2pwiaT0dajdJx3fCdt8XirYv3pTmtvWe5OnJYESsa4r5MzCK4%2Fbr%2BuUiLCXw%2FSAxNT3WxYtuhjiNA4cKuWyQe%2F7IATmamkqsZcKfEGG74FyznV4vKZGQIjCzmZG9BjqkAZdoI2wRkeXzxb8BGsHB6Vxa77vQGRKtPXwY1bGkoFN8fIRBt5nBdbYrGdvGCZpC2afefLEdCzArtS5UTi43sRIZF4POb3me8FR1EsY9lIoLE8kau7QlCBGHHVofYybBfJnd6JrxTCGiOwQsTT3q7c8Jj3fdY3RO4D0smB%2BQN65Guy5eqSdiCZlFsAGFVDm%2Fyi1mx4QVZc6RR%2FH9DcJe9rtiIQmL&X-Amz-Signature=637255a624a723b8b19fae09831abaa6e7ff2dec99e1320e7b058d2944239ffa&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAGIPXXI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIEWV9NexWH5w6DdRHP4BNdPCT6sIBPj3%2Bfwqw%2B8Bxo%2FcAiEA5HsbaaOBrRYUTwA4%2BZeJ%2FlXogtuE9YKJQqC%2FJdvv%2FKgq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDERv5hTaYS6Gxk45mircA1rgiirjInb1wx9eY15rd1dZMQCno%2Fa0hApI9rwmEQ9MnY%2FN3L5tc%2Bg2NIhO7yo6iSEHHaunGh64a4qLulmiIpUN1j4ZoltdN1mTkEOJiuXN84fORBfKv%2BDMLRxiYtVhIGE2y%2Bjx1rReIBvQoY5HS3gt%2BitbxTmYVHKeqHJCkxGgZEKwNMQNNCkppWJvJZiZwMf9Ap6ZHImLsIKcaeJ4LFFggfCZwXVr7oSOW8vwOlmoUqCUIcC8qmJQg0gvclKHXUgDMkpbb%2FXZ7GAqi0CLrsf3mM8tVGgbWxpan0XOYexGOD76%2BzpPgK1glRspYtpTjvBfxi%2F7%2Fn5%2FYe5voaQRHisUE8EJjuU9RZmi1pn7P9FYKp7P4uq1mLt6UhfNF0kPr5geTwB0CaKYKyASPIy9dIU54LIJ%2Fe1RmMVq5ITlZjL254lsz7Fzr8hDaKJ4rUAFlq9Cg7XB3m%2FxZ7nInGcJHzdwC8yD8N03ntbk6nqMR7mO9y4S8a%2BjhDpm2dOAq8Rc6k%2BlMPaPBXggJNZmglbDEQBKAuwlEcflmhXAPJBycn%2BboV86TIP8LNB2w4y8gBDfRGyGrQlq%2FajU6y6NXceA34WOuhAM%2Fae%2BwgujhGUQTiLoW15AGY4Iy3MRfv7VMOiYkb0GOqUBbmcJ62E7mRWYuK1QTFRBUGRPUsqhCNa09bdZbqRwvBJcGiLTlxNaXlVVEphYhR%2FVGfI9W%2FfqHNoSvgplOwlt6dZtSeG7DcWolXsqOBQENgOAcjG3qbsbJ94D8RYeSy1JC4JTFT3zN%2Bf7bN0FzGWxyvp6nZh7nUSMzVltVLw%2FvZu2Zh69d7pnPBLIRyNHc0B7ddc3yD1QS3DW1Y0XbASBSY4oUk2v&X-Amz-Signature=209b10d1c8513dd7717f7bf4dedd1e12c0e0579e3bacc5c832a5f1080e230f4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFKGXJUF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQDz8lGTFj2Zqq0uNxSIZkIN0Nfs%2Bpmg7pMiw4fqpbQgHAIhANmpkuKZ8lxZRTSPGN%2FSWUvBKRa9FS1xvhxJ6Cv49g%2BaKv8DCFcQABoMNjM3NDIzMTgzODA1Igx%2F5O8MpLyD%2Fa%2BwbRkq3APXdA2nZNpo%2Bu55vv5bJ5lYNJxSW%2Byd%2FfNr30ufW0FK8OcFeW95VwZJbTFtKn5TW8JC6lIP1TiXjGvLjADZz%2B%2Bzkvu6FRmm8YIB4c0NW%2FdMaIYJTj5qj0Ao2Yy1lJ9dq9TwB9RsMVzylpVRzLbzeLURY0sHyanDY6gc%2Fb3Ipd6%2F2SDyI8aMlKHKACJwltroVESWWc8%2BtyA%2FXXhhpRVpFMe6Dq7f97qUCIy2uSTokwLQeHpjjrfLv7FbM2gXSTsptpE5arhv%2BpuEgV3hoe9GecR8CHJKsaDibYz0zRjBrNtbsqI4NxzpbaZq4G2gOEfYJZ0lmuIrmbR2uh%2BFw48P8ruE1WdTciNy2lg0Lu9b98u2Trda%2F5cOSsgpYF9An1aBJmXbhMWh75Q5BPArlr1KoO3W2xoX3WGJ8K994MFub3Oy96aj9lrAklb8K1%2F%2FV0E7s6XIB8KKASSyJnjcNkyYhU3ZF4l7NBsGbGzo4g2GMO8N%2F6IBzbFcLiQYTkiLLPssCUL9AwTgDiPvF%2FTqb%2FdOmz2KW%2BHElTAA1N73scrxg7FlnfJBj4nriSbx%2FwWCKD%2FU%2Ba1JsuxX7AZbAUlgLtwINmai618VCNMHOZc%2BXhu4JsBhJLrNzruezHi2y3RnEDCFmZG9BjqkAW2vo8wme7GiIa2KRbZSZQYGUnqv%2FKeVTJOxFnz%2BKHj3LIVQxXD1pGjtrEDsY9LIWrCAd8AiCPzC7IazgY4kix8I%2B%2FUKe0uhu6YYLDWpFK2YFsev%2BowwnI92We8rxRv5cLN9NrrVtBShl13ixP%2FUZAIdbQ9fdr2rEU7xopfz6wl5Mp0sdqkvIbe1ZiVy7TOfmSiYIPixhsD7prE0a%2BbJgrFdwa9p&X-Amz-Signature=2266f32c1a01b5266dab5a96e1c116981185232676e3babf3af61380b0da8c6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677S3VWPE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQCEQmdE57ZRRK6nQuT%2BfsqE2H17VxD%2BouQeZ4EXO3mc%2BgIhAJEPok%2FeUpfLnpUzsNJYme%2BLavtbQJ95OLQCqCWPnDfHKv8DCFcQABoMNjM3NDIzMTgzODA1Igzv%2FtU4pnDL5Q9gh0Aq3ANJZjp5u5wokBT3kQILQ9MU2Ixc4LlgZgGqBXc8wzp7jl1uIdbwf9ql7pnS3dBj3TJd6lzo4mflq82J2glvd85rDS0XEIp1kG2qkolbWKecmnVW5JscnoRuQN%2FyvEmliFRn2gNgxMIqEnXOVmeOCot8IevUAY1kOvA4VoYgFHBRLYWAEIJU9m8hp%2FHkBm4s22PHMNOG0lIbY%2B7C7zFWEOCfRv6d3z8dsvSnItwOor07BJr80%2FtCEmSLqGXwjAXCTlG3yGnPq4p%2FXGkrK6tl1gqHs1Z6VzxsA%2B980QLKc8ghTjdbh%2Fouekpj%2BQ%2BRn3JCP1JoyS8tIJNulfMx7We1YuKviYUZefdeVbFipCuSmR4RpngV8Eek3F0mXwVZkTFOF%2F959jdiXQrQoKSLeuAoJ%2B4lHda1o8SMbpPXoz%2F80reRXm95rsq6nLwGXUbLJ9YmP5ZGKi%2FvJLBD96BPakmMuHykX2h550BGry%2F0C1MITceDeIflW%2Brf1XNJwEqQrDdF2ljw1GdwkhgrwzJh9%2FQcug6I8Hf3boSk%2F5RRWm5kfZ4IrCoKMOz2kiCDlehu62L%2FAalweabmmo85hkjKXvg9jaVG772M1AHrd77UtdApUIcAzhuV5Hw6xAs2UsaLajDdmJG9BjqkASWWROsCVryxAjDIH4QZUX%2Fs71YkXHQItGvEkpNICif%2FFpb%2FByDmQ6z9PNr%2F7FHSvjv2pM5Z6dU7Ni%2B5VW1NVQAvJyjhQckCpadjMXEMZFbPDRXJ4Vo1jKeVAGe0RH%2BNqUSym5slrnxx2L30VivAsJ2aWtkhtg%2FbC2504GjsYDNM1IkUtFnygeTxmIx8AXlU1ckc7juMfTNXzJ2VQA1s%2FSYa1CXC&X-Amz-Signature=7449b041a83f42115f37949da41c931b060b092a50b795400d7fb71254d73605&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STGTWMBM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIGf83lDAOD59ggzQaGriAShYPQZ8uLQqP5e2%2FycX9XL8AiEAlO%2FKEkFiAeKAZ%2BQrJ16kLgiL%2BgtXQdKf%2BD7Gub9S8Rkq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDOKUpB0ICn3XNIe%2B8SrcA1DKxDsYIIVOftAOaIt3eOmM1118EI9To9d4NDwXN0HSpH4KNgePN6qOUCgsZZLc4onwpq9YnwFKeV90Zqq8fXValCJcu%2FqRJv0ps3rTQMg5fc32SV%2F6HHtr3M2HVJE2bcrIsm0gw1jZVQrrMX6aYasX9Y0mE3EFCsySJKwCQtEj439NHAh8zscS7rDVUAVYxdjTQf%2F29arBbWz9ovkktsOEs3RdMU6y1O1Q8sGnrNrtPqvdt9rR17UgcteidM2JQu3PXTcCmORY4Lw6ieL7PKA1OTTnd5EmJyo9zDhIvnBQNsXx1FFX8ih4RuQexgZcG%2BenVSiCuBkuoQlIKHtlaE%2BzB1L%2FmIzDdjim6H%2F7dDY1c2RJsLVxsY19dzKWWe9yHHrMlliZgp2TRmNPsLNryNLMOcxMlrf%2BmYkGP%2BK6DOirFLJ7hSSY%2FwxItLRRSZVbbmsd5ClqtIDQkG6cKrd9iQSUhGqylcvlPdrH2Zouc0H1L30XV%2FXwj%2BnLlesoKIPf8sSBG%2BsR9y2ODKJ89HsByg%2Fxfbim14HA0RDxExFt1ZAS1W4Tij%2FiNltU1cXSDUoMj1fpw%2Feh3vaaFjAxdoa%2BgBEeqlnCLq5gIsHCtYmRCfSG9gKBPwKrWrWy2mwOMJ2Zkb0GOqUBnfc7tgTa0986Gv3VPMTQsBR8RyWdUJGIujSJbERXQbfeNthgx%2F6rJb7Ve7dH22rF0UDmCm6r9sTbkS4qqXrN2oKYtZ9lvKKTjfKY%2F0LrufoDH5O%2FfCbwq55ui8ZIdt5lD2buoUVylFqE2d6fFApXHL58Z1giMETiW2XRo5zIxV1me1AJVkLodkiHVle6WS7cBtMVJhbcVXRdWNLRDUiQfgP4IMPj&X-Amz-Signature=4c0547b7666ded6755acbe5a6d92d3285145004b6249bfbe23c9bf93bf67a484&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4Q5P2UJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQC0YO9wUvMxOc7GQG7G4dtw9RBBu1rJc93%2FNN3BzoGZ6gIhAK3gK4vpEV6R6QdT69r9wug3qpdllQPfHJljTmxffYTrKv8DCFcQABoMNjM3NDIzMTgzODA1Igypkla7h4eGvkmAY%2Bwq3AMCaVRdOvuwZZhQB5QKoc7wZuR9ef1jUysIPRKbQyksK8cTHWf9iQ7NAnWVbl9FX3T8Z3EYOo1G6wky4%2B7b0xaVC1bPg8wx3pEAX30rzWyQIc6JzRU14IxMpWeY3iPm6a9zWrZoQAKh047VIJmbj5EtySP1bO3KGeUGsEkJcD%2BcmZjBpHgxPeRNrm7efr9dLjoDASH7GeqR%2B4BEi3McYu5qdc%2BSk3WNGw05Px9hYH5AtSF%2BEjZapMcf5iL%2FeLMZYTseEbMnBfVmTvVSPL%2FS9e0qoFDLpOE2EfEdxgBM6bfuvO%2Ffj8j4QLGtUzV4gTJJRLt7zP3u%2BMFOjK6ugOESpAJsHjYhWB8Mxby5EPdjy7%2FYiq6Uk9lLly%2FfR7G0OZlsOkFO%2F%2Bt21SWpl8LfSS8JRpDKQxljDyYQ5grCUsyrdohtvyXVmpsio1ll7tW61SGYlXVGsGyO0DfC7YeHSPDDqzSqkAti3qbcbTxBckT4aWe9Bl2n2J2cvy%2FjFxELCn29v2D%2BlMFEiLZu0zlXVKMSpfS9IkoBkfmtxNx09xrXFPWgjfDM8wRMAR5RVIW3OlNR4OvgydKNyFATMcLVc0H6JCkTjzfK3vP5FCSoi9OvsbXuIhnLgZgkny8rvqdlqDCbmZG9BjqkAcdGyrRO48bYwR8%2Biq%2BZcWiynmkt4pUCAN94E42bzWf4iXS%2FhziQgc5weg9AWPvxXB3j4eophtPVzfAgZswP12FHRDRRtQPj0l2AP%2FWpU3pxyxz0XK4aYuNoKa%2BwTSpKiFPSolmyX5lKJi3pi5OM74UxNPr08xDWOZtRBf107MfT45ARJw59%2BNuW4VjgpwUtrvJf7nXRe7j%2BdXxUxv1NOSbHd4HZ&X-Amz-Signature=a044e6d3b1d2bf2b889a6f936053e29e5f242f9cfdb54648435f975fee459d9b&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLG5Y4BA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQCVBR6eZLukQd7OdZrALiRnEBWAzfAuzCWbUdoBDrHwPQIhAKrXJaYO8wvep0q3OPZtWY7x4KJE9aIwp%2BWiqr56jQQmKv8DCFcQABoMNjM3NDIzMTgzODA1IgxSjSZ%2BrOLLx%2BTL%2FVcq3AOBn1w4%2F9BMCcH%2FXztr95Lq%2BYJkcW5T5RE%2BaWBCGPZ%2Fmjdpk4akmaqXncY78sezYQN9QAXxu%2BCERxSkGwtCQ73WLV3XnfQxqJ%2B2Om1%2BEs9%2BpdlkJ6qXF4ChICqakBIb9UoQFsAfNbGgxSchmU0OLN7gW8yodCtiQAmQukjQWwH5haBFFGRTIgLjNfseUqjoPXv3tc%2BtbP2FUuzMKOthjpYI%2BTsoP0DQ7F6aK0yhhou7fbZH6lIfThqLMcJ38K%2BxOWoVbzLrjQQiPuUm0btt84I9wSrORiRfCt18H%2B5N2hhpbEWJEY0J6uery%2B6afD1rUrwJsO4hP3g2xDos80U2tP8m0xmVZ2zcqIesWiafZbFq60DUWsB4EuA7P5h%2FQuCQDj9tCfBWLT0sad0ftGeWAP8Env28McHQagc94cEWZkGIKCKkM8zBctKiJRFT63JkjVZp6rCTB3qEW4qUTaxhKwedeEiAUNjge9%2F%2BKe1NcOCIN7ZTtcZ24tLpCtWrZf8qmO0qcdW6bUKTji3DdcM7S6x2gzXYNgLx8Yqcz%2FUMHlpGSy%2F8Hrv4KOAesAzVCfNobnN%2FXZvjmslFla1%2BPBcpk9m%2BaRGJ%2FWypcjnLPs8d%2FTJL4g7l7bUttZiDfPTXzDDBqZG9BjqkARifkdSq%2BNu65wlnD6LcHnXHoFFoJ8pTN%2FV6v4iXFbCCANRyDORPIcJ4okyBs2j3wRWHiSimShgY9ewIJJR5QRP9AZ5Xbxv0HP5pOkVaTwCfiFtR9amhHHYleIy0O%2B0xJRY0bRz9HVwEn4k7JtDknruYImxMmYV2DzbKzFX4PObYSo4VJKlBbcS0Egv9kaKzXEqLSaYc9OmFrRX3sRePCrsp2M5n&X-Amz-Signature=578f1a36f70191e917c20c26a954f0410ca2a1019760029d478055af1f5e33f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677S3VWPE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQCEQmdE57ZRRK6nQuT%2BfsqE2H17VxD%2BouQeZ4EXO3mc%2BgIhAJEPok%2FeUpfLnpUzsNJYme%2BLavtbQJ95OLQCqCWPnDfHKv8DCFcQABoMNjM3NDIzMTgzODA1Igzv%2FtU4pnDL5Q9gh0Aq3ANJZjp5u5wokBT3kQILQ9MU2Ixc4LlgZgGqBXc8wzp7jl1uIdbwf9ql7pnS3dBj3TJd6lzo4mflq82J2glvd85rDS0XEIp1kG2qkolbWKecmnVW5JscnoRuQN%2FyvEmliFRn2gNgxMIqEnXOVmeOCot8IevUAY1kOvA4VoYgFHBRLYWAEIJU9m8hp%2FHkBm4s22PHMNOG0lIbY%2B7C7zFWEOCfRv6d3z8dsvSnItwOor07BJr80%2FtCEmSLqGXwjAXCTlG3yGnPq4p%2FXGkrK6tl1gqHs1Z6VzxsA%2B980QLKc8ghTjdbh%2Fouekpj%2BQ%2BRn3JCP1JoyS8tIJNulfMx7We1YuKviYUZefdeVbFipCuSmR4RpngV8Eek3F0mXwVZkTFOF%2F959jdiXQrQoKSLeuAoJ%2B4lHda1o8SMbpPXoz%2F80reRXm95rsq6nLwGXUbLJ9YmP5ZGKi%2FvJLBD96BPakmMuHykX2h550BGry%2F0C1MITceDeIflW%2Brf1XNJwEqQrDdF2ljw1GdwkhgrwzJh9%2FQcug6I8Hf3boSk%2F5RRWm5kfZ4IrCoKMOz2kiCDlehu62L%2FAalweabmmo85hkjKXvg9jaVG772M1AHrd77UtdApUIcAzhuV5Hw6xAs2UsaLajDdmJG9BjqkASWWROsCVryxAjDIH4QZUX%2Fs71YkXHQItGvEkpNICif%2FFpb%2FByDmQ6z9PNr%2F7FHSvjv2pM5Z6dU7Ni%2B5VW1NVQAvJyjhQckCpadjMXEMZFbPDRXJ4Vo1jKeVAGe0RH%2BNqUSym5slrnxx2L30VivAsJ2aWtkhtg%2FbC2504GjsYDNM1IkUtFnygeTxmIx8AXlU1ckc7juMfTNXzJ2VQA1s%2FSYa1CXC&X-Amz-Signature=b542e957ff332bc58f8cfc1abe95507faa7e165d9060096bf67d7ad61166fb8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6LKGODE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIFDHb9a7altAdmxrkLNP%2FLvkLjlnnOJD3%2Fz5MCjL9zaPAiEA4f7xtzF7HBUwdv3bm80F9GGEJalyK1LldIHqBCS8Xwoq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDMZpYgIpWSJCXQeJJircA6mD%2BkNTvH%2FB5oeoukZm%2Fmhe01zFmY0IC0vb5%2Fu%2FUL%2BVChUF0AB3mf39WUGs%2FrFZUEgQscim3zdxFeVnamJUcl%2FK0omkmsEkCOS4LiiKpWbHHyElgdZI7n9o5nfK9POQQyIHOo8HmFgzJZaNHK%2BNEBIbQnbnrWH18DBylBU%2BDKDCdCguG6qVXI%2FvT7f5CBd%2FQsU28KolCDk4sHGOS9C7CwdJ1cWi9snfANYONgrN%2FqLtZvsgHJYYifYk0I5ElftMbf7WWVlPT4v2tYlnNxwmvXyrVh6m1nytz7QIeAdt0YyIfnkGxVFSkN0kisUdDXDon0Uo60WtOLbXYAHeOXj4M2STatsfp%2BSZ8wQBLJsXzHN4kBFdJuM1zlet2RXVV6T%2FKZXdSi8%2BZV6no3ZPSUUsjPH40PINdzXkVd0DbL6MTtXKGQKte0QUZXo0ssExIx%2B%2FfTx2lYAlxmitY2wnVk%2F4DJ1KqO%2BmQyfoKLPCcqmc%2FZEBpzELhsAnKR70vCjDUUyNMIGiQOlGAFY3ckfjC0YeY1EOf5Pm8augDdz4aFxXGTXtghFTdmOFAF0sOuomohenBL32dxsaR0azvef3PZWal24HD8u41%2Bk1g6lXKJqwBUf1ed9TrlUnIBSgMUn2MOqYkb0GOqUBiJscpanVM7z4RPVs7%2BNmWHxnhaASuo2z3zplxB6dhYCu75%2BiuDQ4YsquBIOwKT4LZtDoenvEIvVwpfYtbntyh4jyB2pxUGID9B9UHMFAOhZilztfuejwaNajLnOh0MKZPvClK%2FDzrS5w9vvNRcp2Zj1x1X%2BB2EhUi9GlQtfIcROw86vZ3JDFENc83nX8KeZZEmt2EtqjR5KpOTuqD9r5Xa0xHSqA&X-Amz-Signature=b21ca2ffa8b813f554a81d21532186b666dc4ab151cf3c9b8b7bb32b726094da&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6LKGODE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIFDHb9a7altAdmxrkLNP%2FLvkLjlnnOJD3%2Fz5MCjL9zaPAiEA4f7xtzF7HBUwdv3bm80F9GGEJalyK1LldIHqBCS8Xwoq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDMZpYgIpWSJCXQeJJircA6mD%2BkNTvH%2FB5oeoukZm%2Fmhe01zFmY0IC0vb5%2Fu%2FUL%2BVChUF0AB3mf39WUGs%2FrFZUEgQscim3zdxFeVnamJUcl%2FK0omkmsEkCOS4LiiKpWbHHyElgdZI7n9o5nfK9POQQyIHOo8HmFgzJZaNHK%2BNEBIbQnbnrWH18DBylBU%2BDKDCdCguG6qVXI%2FvT7f5CBd%2FQsU28KolCDk4sHGOS9C7CwdJ1cWi9snfANYONgrN%2FqLtZvsgHJYYifYk0I5ElftMbf7WWVlPT4v2tYlnNxwmvXyrVh6m1nytz7QIeAdt0YyIfnkGxVFSkN0kisUdDXDon0Uo60WtOLbXYAHeOXj4M2STatsfp%2BSZ8wQBLJsXzHN4kBFdJuM1zlet2RXVV6T%2FKZXdSi8%2BZV6no3ZPSUUsjPH40PINdzXkVd0DbL6MTtXKGQKte0QUZXo0ssExIx%2B%2FfTx2lYAlxmitY2wnVk%2F4DJ1KqO%2BmQyfoKLPCcqmc%2FZEBpzELhsAnKR70vCjDUUyNMIGiQOlGAFY3ckfjC0YeY1EOf5Pm8augDdz4aFxXGTXtghFTdmOFAF0sOuomohenBL32dxsaR0azvef3PZWal24HD8u41%2Bk1g6lXKJqwBUf1ed9TrlUnIBSgMUn2MOqYkb0GOqUBiJscpanVM7z4RPVs7%2BNmWHxnhaASuo2z3zplxB6dhYCu75%2BiuDQ4YsquBIOwKT4LZtDoenvEIvVwpfYtbntyh4jyB2pxUGID9B9UHMFAOhZilztfuejwaNajLnOh0MKZPvClK%2FDzrS5w9vvNRcp2Zj1x1X%2BB2EhUi9GlQtfIcROw86vZ3JDFENc83nX8KeZZEmt2EtqjR5KpOTuqD9r5Xa0xHSqA&X-Amz-Signature=121cf82262ce8c05d74236d97e1ca0045464b86dea481d5a7bfb7b0751369dad&X-Amz-SignedHeaders=host&x-id=GetObject)
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