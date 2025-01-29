

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG7BGDW2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCh8uENPQFJ79J6rsS54MhJUmQIU962%2Fe0U2Ha6Wdb03gIgbDSLxhkd9UdKdBXVk4CdJKZvnYAa3%2FreQRwglwpaw1EqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP%2BjsL9wUZx43oQ7nSrcA1fzoeyB46CGaLVI29DNsG7cZaeIAS4%2FOiYy%2FbKCxqMMEwBbxbmITerk0LSF%2F5H0UJId8PkvXjDMk84lufF%2FTr4wSHel7wq8OpOuBkaj5bSzAypg7NSdNs2aH%2BAgmr5oggxggbtyinqDlAhUg0WJp99cNWpmGhhPGW9owDrIfibhNeTiJiXsuTD%2Fz0hJOFHlTtLv%2BYSmKwxIEiQPNq9wOIg4ERM0NUkCxWy4aw7ml%2BMh%2FxJpczhAknhTaaPMRV2SO3uMQlDylV7w0X%2FjmgOX%2BhfJmBSzv6CFv1W4YVTZUbYAmZrj2A2BSV648k8kkRP2j4HS6KFIO9DCIJhTqHuJ9rH65YBCXeibzMx3efFB1mVzmjStb5rmuAAYae%2FzIIyMHG1LjxzGHMVTP1tJCsx0XMLHs%2FtVXgwIhQfxCXTo%2FwNgPSgJn%2BYf7fleep43vY7w%2FfcZta%2FNFfXKIOZK8sT9NG%2BNwJ%2FE51GhmAMGK3OT7MrLV%2FruEdprkiGQXY%2BBFkF6eVuzcgQr6vtApWB7N1zdvnyNIqntikit4w8Mks1ylY4WfI6KhrIK6h6is%2BBq4GfP6MDnF6AU%2BtGWMoYjlWN72AmVqzszlBDyNa3Uoj7LBucu4RRk3T4xQMJtSyU5MKPj57wGOqUBr920a2k7jL7ur87LLbjd5JUnv0HZ4j0Yj6Pfbd%2FQ0%2FFrM%2BjvVEnQO2t69XbOLquoiLweMTuESsWhyVJasji2OVbtObcS9peUCbZwC9r%2FD14clwLS4nbdH9AkjsTAFUX11WcmF5oIdrdQwrfhxxfEGS%2F%2F%2BpWFW3WhpMt95GQYlb5MNUsGGY10BZlYjRlKjHXg463ZkQXSX%2F6TV%2FBMaZunM7lZdMUI&X-Amz-Signature=0b31a6d40b44f16868d599ac0a6fab7634fcd16d185f4a72b3fecbc05111c8b7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KHNTSCF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtIuGM33niCxbfvt3Fk9o0BcBrq06pqRbBpCtlj%2F6zCAIhAP7h3T3bqA%2F8yXFYIxWt7WwXwDeBvxUTU67pLfN50Rs8KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxUENJRbFDk5uHJDp8q3AO8Jj37sxfyiQl66wVJ8n469GZwGxgTBz%2FOIFBVpqGrgVmmjB9RwCy4gGi0Iriru5eALiHlXDHU4P0Ge3ZyD9K0yFPWSUlYFQYIZJxLsAQHJXHihU3R2uhruGK4J7JBHOt1NB1PKCp6Alrcbi0TAkiQgsBCYsUd9ldfcD5H900ygGoX4d1I18QS2FX2NOWvU9yMgOzmHuLs7fTKlnoBDizRTmJ12WmbC1LEHoekQlIcGyUyQ3b6nZbbhlfJRqXoE7gsol5MSL99LnxXQ3MW6LnG2dDhHXBsa%2Fa3hmLwvP%2FPnDDwMmwzMHZwXlKEEHFP8pNiDlX54iS%2FY%2BQnd7TwxLLagVxawU17ACnBStxVgdgUg%2B0maxEQ3ucycIZQHIuRxwBCpThg9jx9sA2kcaGRVQaGZ4TqCuoHK%2BVlXRFX%2FFbwLHGczcThu4uDI27gVaGprwJM65VuYQ1hK7Jx2hI9gMHBZGJBRaZl7U889mAvKVqL79mapiEaaS%2FnLWeXof4OeLjAhVlfN1tePwNPk8WAgsNJnsZKfUc3vJHyy0zmW0skBw6XUY49XqwWoZfu3N%2BeP3OZFbPNfXIysBoBbB%2BCJrePxJofLJXQNvLnIWjrFdoA5hV%2FmwYrBpslM3UC8TDA%2Fue8BjqkAftEce63P9d5Kr5rVFBOYzJ6MbrHaSVNwnH7vmr1AQyN%2Bf8EnqAMsUUIdFBxBf3sfbzpzg3aU3v%2FzKvf2yy59QUQbmU9njBRVZbCf5V3ACpG49FBvNaEvIhbeWaA6HdJkUDB%2FgsFJxbt2d0c7xCj3oKlntonUJ7I0TUDdC561X0EcqAuCZHMeN84x0tRsHQmNFcry7pImHhpPTRdHlNKlsEERDfE&X-Amz-Signature=45cc2e62ab90c9d143bc275be2b950e2d1542c273ce0688772aa6949c748251a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IU35TJR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2FSjk0p%2BIS2lHEst0r6XRDI1gfZAbxyzzqkmcnzz1xNAiEAyE5%2BS0JAm4CN0mXy2i%2BOI5N5%2BmermkbRJ6Yn%2B95nmeIqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBPuN3BYOk9QtlA%2BQircA4eJ1ykrZ0cibrG1JaaTK2%2ByfH2qoEEtlDYXqDxBCeqcaaoPnlqRStXiHUXT2DNdGpJECV21fmOuVYGyhsNtir1WpuzJWpKglejYYXje2UiIckr%2FxJhpE4sUDxm3lNNe2jWzhlgB6dXDnPTbvgSPxgbvR3EDr3CAEara2czfOLqV9dK%2FPW0xQmdBIR1komWvo0GPhuuJW0SE0aBrsZGbzg%2BO6OkNZOp%2BrSMAayoky4bhNZhHgRT0LcbSd52wZK5Hf5gnAu4geceUeANKRFzQorMOTm9%2BooK5Kr84VoigolfMPjWmeXaEy7M8tXJlOvEDWGVrb8KeaH8MhXoqrgZFf9KAgZQUIeJ20xwXypyAwNvZaQX8E3eNYeQTtFPnKIT%2FXrZ7oh5FkOkBeHAs%2BDDUXQPoQSqwyDzg6NjeK%2FRUXu9pE6kVKKbLVoX0ydEzrvVgWF5CBMlfqMohQmpeq%2BDQBnRAa%2FP5wOAuarneGPzLeAMxZs0tpoEMUlJ7qcSVA06Zi7HZQC5J4t0P%2BthseKgD5F0tM7Vmg%2BUa8BVG5b6deRD%2FSIgt8JuAH9IsP8A5Vo63VFHwIoiPZt6E3mA7D4wP4QrOA9mBhcsOXftxr49igf3f5QMsk2W7IbOBH1YeMOn%2B57wGOqUBW4mf%2F7RKVpMEGx9uSjwWNANY4XnWQ%2B4qEGE7s7wPW8U3I92cR6f217HehCd%2Bg9evHdhLs5CJaJBkVOh2ZKgnl6F9C1QTjrlaOdl4iNwx%2BTGILEaAdzN8w3mMgxtwnipaholcxZEPSZp45myEu9EQ8VcBHykz12R5pbyXNwKN4P2S6m%2Fx0q7%2BzgqDELuCyxpVWNw3OsrIzAzSB72pyS5Nv%2FYvCMCI&X-Amz-Signature=fbc1b917c0e13b6ce12065aa1edab4463c5f3004b616ebbb5d5599df8e218f28&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QSZF62T%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhv30fukzrC%2FtG878UF8yMV2rBzhu7%2F%2F%2FROznZyWY8xgIhAIanmW0EfCH6Q94fP9a9fAnIRs7exnkvr5jWYikRBl7fKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy3QKQNO5t20%2BFUulsq3AMJQ16b1HHf37eSQujQUY71e%2B2kjv1Z5wzPqdbpPu62ojkJ8WLsR1ylWqR0%2Bsd27M%2F0S4RT93%2F%2BGoaQEr2hzZz0hCFXtVsr%2FhZsm0GXlio%2BSRL5G5SbS7xLZFPPZYM90haQSiH82HL09lVWIjN2XinEb8ZxWJqd7ItTRDIangoLK1hA%2Fne2%2BuXG3XMEOeJdP3BcekEih5C4qnA0CxcJcsw5Ly7euiRqjxisCpj4hciIKalcgeEgPemxQAWCFGJswlwd97jnksFNyhvU3fjXWU9sb5F158RFoBqgbTl78D6%2BF6buP%2FyJ%2FZK7UuVHJD5IQSYj5w6OrhVN8BeVOMkj4Kb3Q8iKQ0FxORrSAkad0eizE0SysK6glxPg79wia8d0MmUCWyTOqiBaf3tjZYE5ZQk453FYWZPKQLB6%2B5lNZS8ktVOll7as8ZFYOPc5dYmcA3JwegDzPJbD%2F%2BgeQK5LEidbXOIB7uU4CvyamEXi5euFhX4KRhw25aadJnNfRHs5XZyEyDZlY1goagCwhROf7Z%2FYLnXB9%2FUgx1HR3gS52i8bPDHvNIeYgiTS56jBxd0XMHtfVVorK0Y3s905dUkkRMxEavY%2F3z%2FojQUryFfaIGIvOmEjr0ihJWuEcX2UxDDX%2Fue8BjqkAbmXhlQylBPc%2BS2m0nuxVnAWy0oEqYaU14UUwums5sDzs0Ffrld5%2FnefTU2GehS3QJZUhUi5MUomIAaC%2FQG6%2BEJhW8HFlqkZatbyRN48Jbvm6fOx%2BaAp1vhADFWiJ6UXwySILWrJy9LPCwFn8ZVJl1jcT0ZlaRQmYbmAw93rSA5tlQvMbzXCiMA%2Bxagve6XEHwM%2BDW8Q1F%2BMM0N7CZUzHGZLRSEr&X-Amz-Signature=fff23dda9c77357122fc972410b7a534c4c9c854b915cc08b2ea9cf59011a60c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FRNUEUY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH6lqY6tzBuG7N%2BL47B5bqEZkmmxDBOeonvN1wlQhYOWAiAUWC%2FYmQplRL9EbbPxbW54fHsn%2FtLtr5t%2F25VbbeMJnCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeBg%2FvZ0SxYrBY%2F6VKtwD6WExTw2d38eT8UsMakJFadIcKZsvQ63AaVxLkNumQcvqmjm0nLJQoj87xO9tBb7ZNAXuBfmO0NiQE%2FqszZizaxhwfHs%2F8ESiZ0UdJfJh5rQYW%2F1eqHSZ45LP2cnXMqfR2m3DxZMNYD5SKyKYNR59A6UNmMKHSeR9X7swOugTkxHR%2BLcA5B6VUdy5eT4WxV1u8n6uGbELbjyFkf3i5VFqJL8WYUFLb6gwBiMOvpCMlGRUwDSMYG8Do30YebKrVKBfxL8bz0zH54Z3ArgQAjgoJMtBbXti%2B8ExepktEL%2BFv3Pw%2BQXX0Vds4uFwcK3dnrptptMbD2aqcR2diELen9ZsaCQka%2Bmp7IvTu1qgRlbzlRpnIBJHrm0CxPWphE8mjBXlyPXsPkIlZJitAB8h61QdGj6N%2BdO1KQ%2F414Rw%2F4DdQbY%2FrqQeRUyZrIzVrVfWxaZzkdUfMEQlloTunuM7fsdscjB7VXNJ4AOgICj8RD8jCL%2FuSvoNMdY4rCLKK6Lbr%2FsJyc3TRww7Sx84NTGLCUSeBvXOMBLPN03%2Baz%2FK2j6euvU6zIDirG3GHmr5p0IoxbFgLYI0uz42fRq6ZGc5TpxoWu6BdX5G5dTCBNFHRgFbRrcEJGDHzgjiCrpDpW8wwP7nvAY6pgEkheii9%2B1FmlA%2BU3hR8mI%2FSHTYnnuEyiTZ%2BLxejawzQoMUKl4J4zq5UpN86sDHbxCNuQ3jV6BEsRkjCBVtV3FkpTAI34yN%2FQCwdnth0wdm6xevFWJ6AuC8%2F6jbbiXxAGK1zcoBfvUICNwZfDA3mEbOBhwqeB1yTiHTIm6haBc46JHHA%2BLaDa5JhyjtwdotEoUBu7HfBlQ7ZLC30myf3KMa0A5zY3YR&X-Amz-Signature=db11a1d6ad0e38b5614bdcc87a130f0072eb854fbe12f7d875008fc5cb7aad6c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USW6EKSG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF36i1%2B%2FltVsmdnCgdsDVpgpI0j5rRLHOjnW8g4bUfNEAiEA1gEqKzoPcb657O513yNWOQbG3YlOPjPq%2FT1HrgkCsuMqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF6apmi2pnS%2BnhrGmyrcAzFPpIlvKIgY2%2BrBHNtgAAdaDkD%2FoDWo8b7Gz%2BSvPgeAyOXYSKkpZK3ChQcogyqRrP4oHzGyOjq300uS6du2NhcbWbtdzt5yaE7Q3xI8c0K4ccgQ5aMkmaMT4YVr5h5zTXGEzFug6qAVqqLHQTkbEFt2KpTkQlm2TswkexuICIA3UVx0ut9sMqadZqyCHXRVOPG0S14Vw2sgOu7CVawbFgHfgvBTfxaBYCfcU%2FyQwflXlaLHpsytvBTeis3La58mKLNGYSUGCe%2B56lJCvGBKi2G9zUg7ZW0eag3k6IwP9JDJzxz%2Fupa2c5MVYDACsdT%2B5Dq6GTkLuB9GlDvDjoZE8tiXj%2BtbbqqJWmKV2Smvw9WCnmbajlHxGqDxfmGJPmqYN7LN%2Fl16MQxAXnzbRqOXeRMpnnzKxr2gm%2FlxJjenYyGyAwbBJeMQKjgyfavH7y0TTk4npsTQxabaA5%2BuVqdTnPChNQSAWjQPfjU0qNTNoiVemAklO2UcJBgsdrTecbuAGN6HhPx%2Fp85qOkCsH632SM6lBXYAW86uqo3AQ6dZcvQKMl6bnFdarlpUJitCpygx3UtQ0W5TSd%2BLef4fzcflsNsciAnwzwn3ac90b93t6Sq92j%2BoNLJS8GIhp4%2BcMM%2Fj57wGOqUB%2FxLYYBB9a4dzIyloPhQPABoGPeDQDCstycoGKM1lV41RQvTx123abkrBxdg5kEW3HZgQfrfODuCM0DOeHH5aH3i%2BNwIQYzVDr9UPAXPuaUmoSyYCt8nnyX2u8mSGxry1j75IVUkUQMScjDnaHo1cFFDW9E5mw6900YMfhaqMU28ebDPvs%2BbGgmR09c%2FysWeIrhASe8V1Ikd%2BJ4%2BH8OINr64U0gHr&X-Amz-Signature=606df07ff4cce366cb76af14b9009c548cc51b3ae41620b7b4ba8e82e84716f1&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJZV6EDA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2FJMSml7Ee8HXVkvD6KqZ1g0OK0xvDjWv%2FB1b0ezj2XAiBivDfhdLxqo52a4x78CZZK%2Fc6Yw8aaaz4tLgM8qTjrbyqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmnyLWUBpCqbcRDuVKtwDUvgeSs2NnOdiGfLHeM8XpTsiIDmpzfkrNDmEQXxE1TWF%2FX9mH6rc8d5IDaUbRgQCv8WaPn1tSJa0EDSJNpbnx9rCRxr4ULufLyYA8ZB%2B%2BtmckYpMV82lQuLX0rdEheSUmZIGDDUiQSFMjJY7FXHoIwVpuhQ8GjZ3maE5xGyscdch7nPmNvHrcAbIPLjFSWH1Vz%2BJA4GHmTMJoO9f227pO%2FKQTLg5hEWXXAaK8vFDZJe4tvXQKCA9GhcL%2Brui8hE%2FiyIxw7mvj%2FcMiNSMr17Iyo6o2INbOixtynM049vM2WE358OMRTWgKnG175N6zybJxKV56Dusit88fqnBsBlIedTkFduHZHNvVrzSkB8pzWE15CEXI%2Fo9e9x2B53zi%2FKUaTkGdcImQcUea6lKPDONspWLVmfEF70Y4v4h%2Funpsl95uJ15Y8xgeTo4voeAZ3pVs00177w5q4%2F%2BhtnOsJuMguCpL7Gr5FDgvdh8TAy2PykLvoQ9OS0zuRZZlhy3ZDsVYPg2U4rgz06yy5w7XoDe7aA4mnD%2Baf7Iuly8AuR0GR%2F17BGYlQ%2F2nM88b%2BDHS0KbJPUaGvBwt%2BCIUac%2Bfl6%2BIjVexp8bE1GQp48wy%2BE6aYa%2BoSA0%2BYbk4ttNfBYw1v7nvAY6pgHVgTYB9CyMze%2BjaBTkkqdj12x1kOXvRknyyB%2FCmCvOfnKr9Pt5NdPZ3LG8dQ%2BWlJytDiao1N0gkM7VPVgTP5AIrHdtbI4N5RaM78lXGyQ9z5ArBG5Th13xMGobbPQLFZIFmEHE0W2tNgBzNcmgRwbCFcanXnBVNcVqV252ijb2wjr7IQMw%2FtD%2BKl8n2Dl3ENFA%2BcSMCUdpg2LCc70lsOhefNy4o4jl&X-Amz-Signature=fe68d738d7d821d575cbf477d8a225acad8da999672a70264b38d3c94fffe450&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666K3LU3AP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqAw2hX0ZG8ytL5qoHeNaLX6gOzrmKdQCya6%2BTEr9IUwIgGa96nTA4290Yy0t0LhXxiHdinIqxkZEyOpTp5ZmIDDAqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBnEybXAo%2BYeaWrWryrcA%2BpntChrxlMhooiof5Ybh%2BHTa1bYWE2c0HF962samxnBLBwx5LR0NFy7FJ8PNseT%2BF5lz%2B%2F5BnypRU8OMXxyFa7PYrpJnuUV9xMuQgp7Hwkd043WiPYodObH1qaHPdSSXkhrarnjfF2qYABeSvCMnMYL6nXY%2Bm63l4%2Bm7Z3zz9Vox0XlFJeN0LVL4o1tJa6DjbbWx5qSCdaGRunC%2BvoD8mkdN1I7t2SfAnqLVMtJHbPd25Cu39s3r08QtAVuHWx8nHKxW9JudEDyQpyfYHvk3TEchhYMAJyeDK5nJ1Mx%2B1NvV03YotAfdwlTH54eMyIZsOYu6eePZTC1tqXh9XVcSYDEa%2FNj6U1mDtAbG84Nonhx1Pu8UbGA5lnt2FSHrS3FwmeBGBu5qFdO38xoraxHbt9pbwAJP3XgbA%2FafVItQ6tZdqdLJeDFx3KFGTQH6hIx3AwRwBtKyEHzVem00Qe51j85iQPoeUD2gvmE5v17m3OjXnYiXIhP8Mlpo5zvlssIbcMIrVIzThzAkrfAejZMtoESyLjVzMxAXBkQBLdsJgTPPlbx5r%2Buf5PnP7ZJ2u%2B4t3kiywNjbeK0sB33%2FdiuZpmuhnWtBfNqK0y35nMxL3Pz7QRiHvXwxr67VqdsMIvk57wGOqUB96mg7qwtfbFFS3EiU25zgnCXVuDRgzTZEHV2q5Rlw5m99A1mQjkSTOP1tEYtCav6H8hzFsLKu7Yoe9Yo9F79pjK8pWsNOA5AlvCGuu8T4MUjCUb7i5F1sf8i78E4oCGCV0%2BpH6N3xqYROSadEBJdlYxBo%2BUTowc2QKrdXMe0UUYo7Hq6s3swBuQXwTOmFaxyMxMEDbuXiFL67yibRok47bBptVjZ&X-Amz-Signature=63c9f4660ad27d1b356db8ca6db2d7a1e3db7fb4ce0ab50dc55b9d70596c2e12&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FRNUEUY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH6lqY6tzBuG7N%2BL47B5bqEZkmmxDBOeonvN1wlQhYOWAiAUWC%2FYmQplRL9EbbPxbW54fHsn%2FtLtr5t%2F25VbbeMJnCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeBg%2FvZ0SxYrBY%2F6VKtwD6WExTw2d38eT8UsMakJFadIcKZsvQ63AaVxLkNumQcvqmjm0nLJQoj87xO9tBb7ZNAXuBfmO0NiQE%2FqszZizaxhwfHs%2F8ESiZ0UdJfJh5rQYW%2F1eqHSZ45LP2cnXMqfR2m3DxZMNYD5SKyKYNR59A6UNmMKHSeR9X7swOugTkxHR%2BLcA5B6VUdy5eT4WxV1u8n6uGbELbjyFkf3i5VFqJL8WYUFLb6gwBiMOvpCMlGRUwDSMYG8Do30YebKrVKBfxL8bz0zH54Z3ArgQAjgoJMtBbXti%2B8ExepktEL%2BFv3Pw%2BQXX0Vds4uFwcK3dnrptptMbD2aqcR2diELen9ZsaCQka%2Bmp7IvTu1qgRlbzlRpnIBJHrm0CxPWphE8mjBXlyPXsPkIlZJitAB8h61QdGj6N%2BdO1KQ%2F414Rw%2F4DdQbY%2FrqQeRUyZrIzVrVfWxaZzkdUfMEQlloTunuM7fsdscjB7VXNJ4AOgICj8RD8jCL%2FuSvoNMdY4rCLKK6Lbr%2FsJyc3TRww7Sx84NTGLCUSeBvXOMBLPN03%2Baz%2FK2j6euvU6zIDirG3GHmr5p0IoxbFgLYI0uz42fRq6ZGc5TpxoWu6BdX5G5dTCBNFHRgFbRrcEJGDHzgjiCrpDpW8wwP7nvAY6pgEkheii9%2B1FmlA%2BU3hR8mI%2FSHTYnnuEyiTZ%2BLxejawzQoMUKl4J4zq5UpN86sDHbxCNuQ3jV6BEsRkjCBVtV3FkpTAI34yN%2FQCwdnth0wdm6xevFWJ6AuC8%2F6jbbiXxAGK1zcoBfvUICNwZfDA3mEbOBhwqeB1yTiHTIm6haBc46JHHA%2BLaDa5JhyjtwdotEoUBu7HfBlQ7ZLC30myf3KMa0A5zY3YR&X-Amz-Signature=5a2c0d7c5e62d9617f30192e95af9732d974843e8819c5a2979bf501c5eab627&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSRVLL3G%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEObfhGyfwo%2FzLpGlAG2j6P5tHbrybv1oUEV6G%2FYkltIAiBsbrlRenGmW%2BzEYUsAJ5jbCgRZL5ZLOsARzFp0yEelTiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjmJgbi0cS9d0ZTDRKtwDM6f1Nt1as1lOYtPD22CGgqULYhaaNYX7RrCijc%2FnRBjIjO6wV3u3Y2TId47xRlE3yWs%2Fi235ocFlMIbKiAoO45m2gZIHG%2FWGErZES27Iep1o4T4kiFJXRRo22COfn46c1mccInbUuj13ZTPU1WI1MZnxuTyWuSUvJAZOle1%2FuUWke%2B%2BN91ZoHEILaq4u%2B%2FoRUySBjcYBNvCce12MC%2Bh0Bz4XlFQz35vuIfpPsMX7w%2FfB2nH37Q57FwgKZRHFg14MLFzvSwq1XvJX1TvXRudU5cUuLrnxjKycw4oi36AMwbvUXjs%2BR4moYjgp1Sd4mvqx0A5Du3AWeF59iB92fX8dkFi%2FOaL%2FJggKIUnx4g1AIlFnSASkqDATOyQm8%2BTwTqjgF8WHau5ktCT9CcQeswD9%2Fp9fm%2FuM6OqHOn%2FcqQ28ew22uCk3S%2BcpuJeqJUdaF6OjhGhG1UgqE6sLeyP1BSUCZs9YH3KO8YF1mA50%2B90o4zwhT2nIRTglguYnNovYBsyCzND9TtuhOEqvukyhuJUNMkRkuDo7TUkXrSVeChYWYlavQHi4ph7f6QB08sHSKKc9c7OXnYmE%2F%2BP01P6T8XHGH2icjMpi54SMFcn3LZHq5AuHV6PzzPq5YCXQPwswv%2F7nvAY6pgE%2BklXWwwaQ%2FzY8nhmV%2BcwU0XoxKMFbZBYz7euSpprADMNuuMM6Mc32MyeLq9awczKGmodeyjud6tR%2BbNoQiDRyUCgl2jsHHCZ4T7C%2FdewD0j1MExnKvjBUrNc3zHQYihuxIQkh2qLLHfg61EW0MXsmpQV0QTMwM%2FvDIa%2FXIMhyQEsh9NFqzsvYMXQ654sUtJeshAOwMIL75IiOHk6z2J5a2mup3LSi&X-Amz-Signature=2296c93bbb4a70ba6e45a3fdfc08703be48b02fd321bef256febb0d2355a20bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSRVLL3G%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEObfhGyfwo%2FzLpGlAG2j6P5tHbrybv1oUEV6G%2FYkltIAiBsbrlRenGmW%2BzEYUsAJ5jbCgRZL5ZLOsARzFp0yEelTiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjmJgbi0cS9d0ZTDRKtwDM6f1Nt1as1lOYtPD22CGgqULYhaaNYX7RrCijc%2FnRBjIjO6wV3u3Y2TId47xRlE3yWs%2Fi235ocFlMIbKiAoO45m2gZIHG%2FWGErZES27Iep1o4T4kiFJXRRo22COfn46c1mccInbUuj13ZTPU1WI1MZnxuTyWuSUvJAZOle1%2FuUWke%2B%2BN91ZoHEILaq4u%2B%2FoRUySBjcYBNvCce12MC%2Bh0Bz4XlFQz35vuIfpPsMX7w%2FfB2nH37Q57FwgKZRHFg14MLFzvSwq1XvJX1TvXRudU5cUuLrnxjKycw4oi36AMwbvUXjs%2BR4moYjgp1Sd4mvqx0A5Du3AWeF59iB92fX8dkFi%2FOaL%2FJggKIUnx4g1AIlFnSASkqDATOyQm8%2BTwTqjgF8WHau5ktCT9CcQeswD9%2Fp9fm%2FuM6OqHOn%2FcqQ28ew22uCk3S%2BcpuJeqJUdaF6OjhGhG1UgqE6sLeyP1BSUCZs9YH3KO8YF1mA50%2B90o4zwhT2nIRTglguYnNovYBsyCzND9TtuhOEqvukyhuJUNMkRkuDo7TUkXrSVeChYWYlavQHi4ph7f6QB08sHSKKc9c7OXnYmE%2F%2BP01P6T8XHGH2icjMpi54SMFcn3LZHq5AuHV6PzzPq5YCXQPwswv%2F7nvAY6pgE%2BklXWwwaQ%2FzY8nhmV%2BcwU0XoxKMFbZBYz7euSpprADMNuuMM6Mc32MyeLq9awczKGmodeyjud6tR%2BbNoQiDRyUCgl2jsHHCZ4T7C%2FdewD0j1MExnKvjBUrNc3zHQYihuxIQkh2qLLHfg61EW0MXsmpQV0QTMwM%2FvDIa%2FXIMhyQEsh9NFqzsvYMXQ654sUtJeshAOwMIL75IiOHk6z2J5a2mup3LSi&X-Amz-Signature=5743a9ca059cf95636fd0f880d0ce39b597b9bdd62a1df8da01ba655942b5a38&X-Amz-SignedHeaders=host&x-id=GetObject)
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