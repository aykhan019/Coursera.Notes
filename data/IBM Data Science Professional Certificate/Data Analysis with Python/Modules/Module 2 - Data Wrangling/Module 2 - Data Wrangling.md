

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VM56YUZZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIEiIYK2AkU6myO2ubI%2B0pUTZdJ8xw3crtplbLY0ImfWNAiACcv%2Ftb4Qw01j1ppF%2BwS6Xb6QBqGV3bwQY3k8%2BDymMwir%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMfDFtEU7qEXiJzXWGKtwD2Fa5R6zgsj09tSHKgLcJL8RVTElpMEhs%2BoeX6Tm8bdjNxCT%2BHoIZqKhNaT2l1xkcEAcdRGnnmpkZ8pO35NHiMTtJUWFkY93t92jdNTH7y0EOZAwIPQ0qsuXxLwqBJvXSk5fK01gxm%2BX1mxS7BqMlqiwTnjWANOU4RIzdIN7seOMzviTRiKmDjrNH1V6KCgzm7OKtwKG%2FwmE%2B7R9IfSykUnVqxZrlMWFj6t96jO%2Foruh9gOtV5cVlgNRkoV6cIFdvz92INcC7l2xVpakt%2BHg%2FKwewBZIX76nO%2BGd7rItlpx3nrvqrkWH9N8wRA3AVEYhFZgPQfQzMQ1aOhOzGdwGpv3UFWwN2JjMpWyjxzfAdleiwkYe2EKedHVEeb3g1Kkuv2YGP%2BwytyY%2BcLGE3Op2CF6sgScP2nkr3nxNX6VBepPsJSYrlzQdGO%2FGtpoVILZZ%2B4l1SK9aPzU4hkVtRygX55UZtOdyTh0rndinCN5ujUc6%2B6CVB4pEx0o%2FoMVQSuOrD7WHa3UtMX1dOZOShJUcRhPrxMzZ%2B%2FB962q29SPlbyxUHmSiMxRXw%2BmwlyL%2FaOJHxPePhTS2I%2B1NFH5sDuXQxlfJ%2F6DHK%2FjoE0LNY6XgSR62QFVxSuLoLl4whQ8swsP2UvQY6pgGM6t6Z62jNPj%2BMxxFTj0TpeCAPB3YId9UURrd68E3Jop4B0R1PrJkFaIzhij5gTfoRg9845bkHaQZeCCCasVbmC98TizE1%2FbQVPf25QHLUfdyfG1xQ1cAJOBxZf0xeSq9BBhgdgaDYXiNwSDaNQw855DnNkGM3YFKmsCodH9hxdyasnmpj%2F1mGmWQ31Ws9vecRB06dWHkSpv5r1skRJ7Dt0I4DZtIm&X-Amz-Signature=00c3212870a03f0c3c2b7e50201240a1a5dd4860a39d30b3465cbd209f4d61cc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664S3QY5L2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQCSH7PX0RpEtzpKdmbX%2B62AcqdMXkM4omPKohYpjyU03gIgN3Zvordme1gymEEo%2Fnq0DsZMZTPdnuFzn63yOoqw4NIq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDKGA%2FwiFiNY4O8y4CSrcA6%2FQWVFPAxquZV8sHWMnzPs6BmBQBAoFTUFdIcLUZ80ufJC%2FRY%2Bdr1aKY8bqarHr8PTJfU%2FzlPSsLwIHag1dGNrkxp3W6V64CdkKX2Y%2FQSVwZa1PzgofOvv6KTKrjXT1IMl7zflMnHzF%2FFRYY%2Fd5r9Vx7KTTfuU1m%2BRBCIx6mDytvr1Do3coesaIuiqnGekUY2cZMLHH8a4I9DBeBAPA7bmMc9nDDZRkfZaEt0%2BSRR1wQ8OkRXsWMP%2F1rvYojv55DvGEBJ7EzKmD5WyRodFQC3adLDGaLWGp1TtVNDMm6CdTyGNzy%2FeE0MibIGhIHGHC%2FGiPdEQwUpJFaiqINY%2BJ%2FaFdgzv5N9v%2FmVk0mlww%2FjorPEjNZqrQ16JqpLVXDnsqawKnXY2OE10xEB%2FAtQf6C3F%2BDlZYei4VwnhdRshD2Ef9BaMjOJd%2FcYb3E%2BRGWdfmH5EjrTRL5gMejbrOSNgVoqFspE9NrRvXtiURZsNnQEYIRdQiogREbUpZUkbJbmlcbWyN6Rb5i%2Bszo5rociEF20BeMsuMD9paEeAnGk3VDsNBfuVmNr3sOClu5VYcL7dP9kg23UUhcZLS%2FRD6YVieRXi9xv2f%2BXLSESWdhvp6BGlQaQuq1UlU8ElqFd4yMPX9lL0GOqUBQmIupmX5HA6HNO6uQRVyx1cMnq3vAjpTVJjcXvshAsTkCQrSCQlelnpM4TAV8Y1j4IUtzYs3Xiv3pMLc%2FWALtoStfhcIt4Uryy5UUsV4v9LleWtVXCDNC5tPysPz8mi94XQKPSGUdvfk3NVWOuAHO%2BRn2VWcAxT8EYaASpMoUYPDdrKabJa3MX8VONd%2BpflodmPjCK%2F3cYm7%2BgRzI8FcmTr2BpkA&X-Amz-Signature=2b3863c6233ae865cff101b8a77f0a6190ba9e60c5870cb53acbbc8a1c8b3edf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG6S7N6U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIEMd6tSBQb9e3IJ2%2BTr0DstOLjnWCT7LclcxalLLSF4MAiBEvSoiS2uzTUAFv7R5v97fmsXUTsvbky1rA295IG4EOCr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMvMmIWQBfa%2Bb1i14TKtwD4k6%2F1VIOjLkBdG51CnvY%2F6dd5OimqqzfryJR5Yb28tDKcQ2rPx03%2B8%2BTJKT7k2FfGXRoArBH%2FPegpMql%2FVe%2BjbPnQ6BqpelA6zGb1DZ5KVPhsDYkDzjELaPBcwnZC16TyLutb3QTSJpqOsrH4lOhm34JlcjX2dbHJG2zVGbxmgagZN%2BD5e1nJ37%2Fri3Xux2IEPfHyiz3dIpg9iBYboGZaY3AzgY17iJ3HPY0P5pZ%2F%2BT%2BzNixK0RIeV1AVqoKGJ39qsNsq4BuftBn5YC6fNnDH%2BR7HmDdojLBhZtYvgd%2BSm0j%2FoEgWXwIarD%2B5Hj10M6bggG9vjjk5qUOI7dJK8CyV67WeAWXQMcTzp2W1L0GpfTWPWEoiyyVuNtGZUmiN%2FxqI5H%2B%2BzCKhpQoBxHvzxyrAhuepE18feimRO8gUk4HehfhOkgchYw0sw9qt5BnLh3jVghSKNELd3AVOnZRhIyiBbtABFjxd6GaWn72jPiTWINhezci9K0hTyH8%2BiyPllRjk0F%2FHIepj8kw2RHvCKfSamkPToXGNzlZsBdmZPBfNcTRrLPYsxBH%2B8zaRnk3mJJWznUglYAs%2BPwVKiPJ5ImtxtyrRZYO%2FoAQQEOAtIYZDP4cMOt1hr042VUwwjMw9P2UvQY6pgG6rFA%2FMhEKb3YxRV1uGys4RbAYB7BUAbgsLn7ItFYdAHFb28v7xOSwIM2UqNwaqODyNHVO%2FMZx9y%2Fk0%2F5%2FT%2FgZ82VNQktsZFrn%2FE5huOybfjRWvQdDubZq%2BkQ0qV6T0I3GELAp5lnsOIRGP3eBeX2yte2DAsET7i2FGplJ%2B4cXCuPiF2Lyksw3xPmcPxJMKvRn9Z4TmvHYZiJcSTud4WL7p3vmhDn2&X-Amz-Signature=73c7e1070ce1cb6977a4722497e1aafdb8307801be28eeeef6a65083d10e1ff2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QFMJYMR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDMYbxT6H827R%2Fupzfybhqfm2gXQwXiTeITd%2BNl1oiDEgIhANmocMsH%2F47QjgY6mUjmlhZ5uwlIaH07H5x9Qwx%2BCFdnKv8DCGgQABoMNjM3NDIzMTgzODA1IgwJ8nwL3tgTU5m%2F62sq3APJ%2B9oXG%2Fm9y%2Fk4HzmZ6MvXq9FBvy4jJaH1xhVB8MhxzEcOaIbpAsc%2FCss0WL5Qle7fd4eo6krZTs5Iu%2Boy1VNiVnQrcqI321lQqLO7hs6VGuNS1RhqyN5Eg%2FnG%2FRiWmDyNDJfPDMTCV3DskzSmRuCFFSNWkR32v7ZCkzJh427VgF2ATn91fd78eX%2BazJncp8UHRJhW1pjOZq1SpVTNPB%2B1C6WQ12VDuEOfkqLRK1DaT4JmOg%2Bjj4VbKmKmogTMnM24DDFj3xKazthUC8x%2FtphxejRJzcMqUFq25VhFEbQGa54bz1XcmFzMJEnWXxhuUN082ZwgMkxWqLEsoSIW%2F%2B9agDJh%2FTCmsWHIKOTzEZH1UjFXyNXR4ikKpv%2BkNPEEwrSkfIghCi9GIZknMO0hro9qqoJ%2Bqz9HnI0CgQOGAGAiu%2FaT%2BsTif1LtaBHCKClXPsvgYFFySZMNDhnQHJpUKRFsfbaWAsljGUOdj0GK1XD2h7sXZac1Jtlrnszw2U%2BBEfGZMDU4jTSNKAtcgYt3shJ%2BnW1yfPpCOaRLg3FdxQP9azeLiKjo3O7CVawQ%2FxgJEd1Nmo2D8cfdoRppUB8Q3oblbUiF5myZXel0gY6pj1ObWEoRA6frXFwOaqv2kzDc%2FZS9BjqkATcu36D5ZNaxJfab3Z%2FAsgzapombhgvo49M7GdsiadWmTWsS8rCLgBo%2F4%2F6r9aoTqSTVMY49FG1SmhmwfitriM4fsZwbstA75ECL744JJbtTrgZssPDgTeBD9bhDPMPBic6a4IhLxpEDBl4YODp93lBVLk7sTC%2FaJ4xFKrjma7PS0R%2BbgCCBlD34TPl36Hl2QT5vLgNRDzBtuUi0JDma6dRNNpol&X-Amz-Signature=9a950e731f880021f80e288521e8557901439358597f9188d2ae60c3fd834d70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TWMJTIX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIE9%2BJIy8fuCjRVpsTTWCcoX40TBBGm2JxdVtDSQ8ljDQAiB8emrnCkVmu2oveL1cfj50UAezaTUA1stp9r7fzloWCyr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMHfw15PSSboyYYwK%2FKtwDUHj3PBGpxRxIpSe0oM3edL6SRbaS71JrnmBAweZ%2F3UxAVl%2FntW6dk189%2BMZd2MTA8zKIcEkPf5DZbCLWLMKpRhbXGSZtZpwSlDuhsO09TW9ubQx210Ot7VvqWrlwsvgw6rxx3tFdwZIhCXujE8VGec98OqSc8EwSiXZp4GpL%2BSpcxeDZtp%2FLbM03qY4RPIXMsJOTw%2BgCs1yiL%2Bwao08PJHEJHK5EaPy%2BidCtflfUeU2se0zUN1djmPzvtt7qVGof%2BFXjgLfI9mbRLX63F6Oh8lX4opm66wRO%2BLz3etuuAwunFDkWL9iN9EX8c2UQDEChDyBEY6WAe71Ak3HHe%2FL6cHuFxp%2FVO4Ey4gGIM%2FOhEPL6J%2BFU14JQsKnUUhq1ODTBDZYq5XnTHWc6DqwiS%2BADcLiRtTtoUhBQVSjtSbimeq14TKf%2BeO2waZTl%2FeTtSqz5xuha2gl5k5K8eA50H6iU2CmZMQ7IQSgj4dPQSnP3Lxf4f4ELfkImOoUlYgocwmqX6VO6X6M9XbT%2FRiw21QRv9cf04wG3S2Lexqi7BjAfW4DsI%2FPjtWUWpUX2JapvexoKl4wrMLiA19ddG2MuxTrFf78ZbPfWAZAdOwdg3jwXlhOkymshHm5ncxIfy%2Fkwi%2F2UvQY6pgFy2DAbFp1%2BW88XHehwGFHBwchQK485MQ76kHRS9VBGUF7wgl95uc45h5d6oIyDLAptKpxUVIKi%2BHuO7FIx2t5CrExIRC%2FE0aEH%2F5JAjnG9b3bx0ohmZ%2F5c6yRs8aBZZUrq0KZhOJm%2FeKIUpPYsGMuyRAvDI8NdnXvKTH3nDk%2FZYNAw5cgQ6id2IilWOIXDmfYvhaQpdrWWwcV0GsF9xju9puATr0%2B8&X-Amz-Signature=4aadcc895f890008d7e8028ddc78b2148a898e6ce75c04bfc08f9adc2a15c272&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V67COZI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIDpbEQ%2BGGgXiOoLTqvyZH8v592rA%2F2IgozHJ1PFozyqYAiEAt1COhIckAEXNeWR089dYk2eqmve5XmLiCiMo%2BKK7iUQq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDG%2FCnkUyLVcD%2B3xzYCrcA4fiXoARf9QUveWsHDdXci8R9AaLr8lmTaH6f4Jhx6iiqJK%2BMtwmLqzvZsRKn7E%2F775%2FSn3BMNAJ1oXtt0XZtpdF3UgRM1aTNVM7cWN6HLK%2F0zh2IlgfCE%2Beq21d5ge8zYIKGwapSNRkZGQzPDmiRBae2OqPwQsDJE8ZG1f%2Fi%2Fcgdnv0Ne01dV3fr93esQLyku7kQ5hc0Bh2gKQtirKXMpAxP%2F69CXkrD%2FvXDX7AbU5lwTcJryP0k0hbH4BH6VpV42vEJbX%2B52F9F7f6DOrZBc6JrjqCBuWnN8v2Lq4wiQDhJG2HSF362x711LEw%2BYE6CrQGpJyzliqtPyUR9urKX8ac7lgyg%2FrDOfWMqyiBe2T7SpJGh%2FC9bD9HR3G6VGE5EwEqdVnaxi9zPkoLswpD%2FsB0UDjItx1UQDIdCBpbRTqXDJDIl%2FTa5zsQeDS%2BEaoXAcY6fAeKiC4D6%2BcV0BNDVpbddqaRHU0I12JscRbDnAHjEmsv5Df5mf2LYzkcogRY7y4INHVxqlGQm0Xm27TCGUB9TjRho6V0HtaLbE2yVKwnSfc%2BiGrdKlrKaNTP7q0VbY1EfNL3lGZh3aAMXRPyOuPR9eOZl%2BOIMMactLA5xw%2BztWKMjWbecbTqEXfXMLn9lL0GOqUBcXKxs7UBKQcZHsu6aFrvcPx%2Fuk%2B%2BKpailfQJ9Yn1p1hIYAcTLJYNzPU4LURTmK99bL%2Fe3t%2F%2FFHMQs1tlKK0KvuG1kZs8Mk3LojvaYAUCho%2FgJTBtR%2F6j%2BS0vPWM9j6MX0lKjcPU4xgm2CeKVoM44Oh1hQKR3in5EhG5%2BSZSQPHpmg%2Bg9ARDo9H1x1UzaFiCuQHMBbLS3QGxzhmvvALdPnsA0fbgF&X-Amz-Signature=6779db5cf5f1aa803b17da39707d2efb7f0dc04123bc4b932d33ff21505dd4fe&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKOEIFEX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQC5BrTdrLDo6Xh7vnDst76y9E4MsbnCRMhLfD1Q%2FWG%2BqwIgX6GLWUC7tbQ%2FUFizCOAx2NIddSTezAFnaTJAIuybGqEq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDFiNO6eSGTtbPqVDsyrcA8BflzUAnILxbOMHgzDSBeu19%2F%2BpWV8Y9dZiWlf5RNzdTyUXAbui1QnKQDO4heTNl7KBZ%2BSAAxONNvc8phYbYWYRXtAy7O7Pk5wjhn8Kup4Q4aoLrMEqx2AaZKckas%2FfWFYUIQGCqlK26MgMvLVcVvxUJMBb048olWuMhlTbrLhZYpkHEKgL95IyW8mtNs55LxgrPt9UT8GcNKbqtFN0SBSlfEWBBWJTh8LF7aG6zJoWyCBejdmBpaKCqWfNO3LNd2OSghpVl5LCvPjzRwmvltk%2FT8zi5%2BVcHKqIBef%2FAdJzc6j1%2FRHSJ%2F%2F3LCnHkO6277yEwrX7s1zV1SYTn3YExO%2B07w%2BvsOeiqJ0NdiWz%2Fju0n8lfO48OeVSfQWtxCrBWI4%2Fk%2F%2FUSgZQ6u008zSJfrPMgp8QXdioX8IHHpEbzph0%2FzKRA6I6zpkLp3DDf77wAG%2Fpxc%2Fyj%2FuCw154D6JYnqJrK4pi6RsvRhawZDiv%2BSsTe6yZlnpS1PyuB7x78hAF1yyNwBzIchhggp0uyS7uODe30lYHGt43zLfG2sXjwspAXO%2Fn8XS6Kv553EB%2FL9O8ELXaYsESz%2Bjs%2B%2FauE2z5kfQ5UqE34W7KqhQoGXucA3nUScC4Fx7wx%2FoguJsMLMKD9lL0GOqUBqWwv6SE1Fs13CiP6LQnVFUEyyzy0tX5fF8io2KfnTvBdLSQPXph%2Bnkm0oLFrNrDuK83oBCEfUuZNM%2FWiEVNe6MIQegP2feZYbRj%2BkHYbfTOm2PFlTolcpfGIt5mWgZllE3%2FyV91CG%2BLMU0Qhv53pUOEpO250hsdI1IDzhIZQyGz5li4%2BmR8tSgnbl7Y2lzq8F9plpKAGASQBr7%2BDvWTz5WVyZFWz&X-Amz-Signature=c269cb5c3d4fa9acd9bb55ac855923d17d4585ffbf2018485025f066fe2ce593&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642HJSKK6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIFSPuX%2Fx%2Bh9stzFz6qqBdd1J3%2F3Lq7%2Bp9LMP53t%2BBYPFAiEA4%2BOCNMBMKgBCTrx0XnCXGz0fbw2hmy%2Bxlif8NloT%2Bokq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDAK4y8mzfE2Gn9PXUSrcAzI0FWbXHCgxv0%2BFhbAE6Lq2kqURjgubR5G2FJkyIdgrR8d3%2BKuGHkymtbpoKqA2aESPQ1dREHuzK16sV0R9oCOpffUGdM6Yh1Mh61mPbeP09EWA4oV3AXYhK2RcMptIR1Ub3iLqyk8Z7jEu43YQYZQSr96kpPU5I%2FH8JeK3RFq7HDZEzQ0WsNe3rlreSHHryva%2FnjuMWlZ8ccjZBwPnf7xExvw8voGHvI6G3DNN6dAF2B%2BZHNPw9Td5X9iu%2FvjO7eWMen9zx4VLSzyhwNVYdQFqIEVNpyrr%2FKuJWmGeeOHVCmn%2FfudmwV%2B0sUHJajPEjDKde74QUpC0jP3zsgK2cW1NVqD2CiG5evISVIb5vQxi0U6ksuL1MGvrrFvLh8zP4kv1hA6Zx2Zhj4hWV7QwIySvaH65XMjQzIDJKvEP04QtEPzarXDbQ1WbcqNjYMDl0K7rU3agYj1COmOos7afV5UdQGKu2qBRjqbi4KfUsw%2FIFa8plLno5jBDfHw7ASbfvRpSOfWEKg%2FovqlltQhrMADV2vUF0wPHubDUkBY%2B8SQ%2BlSuLeO8ZNfaSdizPekaLZbGDTiKB5RGtM50HsJJGDmTH7RPmFzzIR2CqZ638QYP3w6ilKPX7q7jAC0vGMPP9lL0GOqUBiOIQyEETBoBCcBe7p2DHnMavQMfKQhoppBW8%2FiuXzrENGo4lGUZSxm%2BPClabocjXSscGgQR0SRxQB9P25MuBjTGBKEude9lWHPJT6iJ%2BKf%2Ba1XZl5NXqpzDrI1jBr5szkR6tHmixObEr2O3kvG3SeLGS8ImZPDdhH3MnXVXzvO0mZzKPv9HyMzxGUZcKVmvMtWTjXDa7Kcz0%2BSEsG0to%2FUcrR2P4&X-Amz-Signature=e134138c67c5da9ab95621c5b39ce7d00bb1e187e58be3474c8f21787cf20204&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TWMJTIX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIE9%2BJIy8fuCjRVpsTTWCcoX40TBBGm2JxdVtDSQ8ljDQAiB8emrnCkVmu2oveL1cfj50UAezaTUA1stp9r7fzloWCyr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMHfw15PSSboyYYwK%2FKtwDUHj3PBGpxRxIpSe0oM3edL6SRbaS71JrnmBAweZ%2F3UxAVl%2FntW6dk189%2BMZd2MTA8zKIcEkPf5DZbCLWLMKpRhbXGSZtZpwSlDuhsO09TW9ubQx210Ot7VvqWrlwsvgw6rxx3tFdwZIhCXujE8VGec98OqSc8EwSiXZp4GpL%2BSpcxeDZtp%2FLbM03qY4RPIXMsJOTw%2BgCs1yiL%2Bwao08PJHEJHK5EaPy%2BidCtflfUeU2se0zUN1djmPzvtt7qVGof%2BFXjgLfI9mbRLX63F6Oh8lX4opm66wRO%2BLz3etuuAwunFDkWL9iN9EX8c2UQDEChDyBEY6WAe71Ak3HHe%2FL6cHuFxp%2FVO4Ey4gGIM%2FOhEPL6J%2BFU14JQsKnUUhq1ODTBDZYq5XnTHWc6DqwiS%2BADcLiRtTtoUhBQVSjtSbimeq14TKf%2BeO2waZTl%2FeTtSqz5xuha2gl5k5K8eA50H6iU2CmZMQ7IQSgj4dPQSnP3Lxf4f4ELfkImOoUlYgocwmqX6VO6X6M9XbT%2FRiw21QRv9cf04wG3S2Lexqi7BjAfW4DsI%2FPjtWUWpUX2JapvexoKl4wrMLiA19ddG2MuxTrFf78ZbPfWAZAdOwdg3jwXlhOkymshHm5ncxIfy%2Fkwi%2F2UvQY6pgFy2DAbFp1%2BW88XHehwGFHBwchQK485MQ76kHRS9VBGUF7wgl95uc45h5d6oIyDLAptKpxUVIKi%2BHuO7FIx2t5CrExIRC%2FE0aEH%2F5JAjnG9b3bx0ohmZ%2F5c6yRs8aBZZUrq0KZhOJm%2FeKIUpPYsGMuyRAvDI8NdnXvKTH3nDk%2FZYNAw5cgQ6id2IilWOIXDmfYvhaQpdrWWwcV0GsF9xju9puATr0%2B8&X-Amz-Signature=0f82545f1cbe0d78043d51400c21145a0999f90958e9aec6590f7ee0bbd65498&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJGW6YNA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQChv37HMDx9JEzZzx8DFUFC9gz3VoUkXnU%2BE2TNWJ%2FcTQIgbZIq75PVJIHWYllp1ptHMM1XhvlUgdNnQrUGvMGLCsIq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDALbxdVxzgcdeEh0rSrcA9yIilZFDD8l8YJYpLvuxBkEWe03VpPVWgODydxeCLbBK4EfD7zpMWhT0jcIi9ieMi%2BVl5N31H3svV605E2ryjRZCldSZoThHXlR3k3EP2k5maEUZYEy%2BqRBsDvwfnOis0LH8C%2FkGmARgxBKixsrmeZSlrwmTR8GbTi9bqzFDE8MpidDtCX0TPt8Y2p6cdPO8Uk8gdGt1bP7jNmzFP65jHZYzjTsSf4pXw1YCZYMNNhwnUB6MhQsGkKna2TOIGEXsNM%2B8UAbCIWVepQ423zrE4JW9WizKtWy5HBt%2FhhGFCncXWysNWrwGVrtOFuGVWjs9x5GE6DufMw%2FPdNjGuFni6eIW1zT2okiojO%2BV958rw%2FpuvSF01VF8I%2BL9BmYmZ2KeuoL%2BNHEZb9kDI1hM%2BMOCdgELEmIeQ5P1oz2QkGeuVeKKNjFqKz7xj8pQKtjUhun2d3F%2FS3KZqUB3U5%2BK66b7pjTwZjaTHh4r7quK3YlS0hym2If7wyK%2F8MwMq5%2F0jR3MfwNLTW4fNw%2Fsm2YSg1wc3DLDh%2BHPTQMoaDj%2FZGleVY4RlEfeQr3xW%2Fegybx2UP7xDxJNuhhDROOf%2F%2FvBDw3xSKz9E01n8S0JG8G%2Fi0U%2B5Wl6IQ75lRYg2C%2Fso2CMNj9lL0GOqUBWesi1XCkgZxo0HxMH6nCy9kTG1YjhVsjiQuRPY8I0aIbZ4h78lqbKCR1JLhhKW81L78kYeX8aqx10JCF62QvXluGdLi18mdZokHGt%2FhbL3SmbxKZQ0Q2hFaic0oO%2F%2FMFsgmvxocHA%2B0EP6ra38ezESAhEiDyMSloWwyBvQ%2FYY3hihJQ8ffWmGKs9473PZeMQH9gZ8FcrQz6HI77EwRQGEOFdN8%2BH&X-Amz-Signature=582976657e67d5c5766636116e2e57e5c1c33c75a673106c472fba6ab8daa0bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJGW6YNA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQChv37HMDx9JEzZzx8DFUFC9gz3VoUkXnU%2BE2TNWJ%2FcTQIgbZIq75PVJIHWYllp1ptHMM1XhvlUgdNnQrUGvMGLCsIq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDALbxdVxzgcdeEh0rSrcA9yIilZFDD8l8YJYpLvuxBkEWe03VpPVWgODydxeCLbBK4EfD7zpMWhT0jcIi9ieMi%2BVl5N31H3svV605E2ryjRZCldSZoThHXlR3k3EP2k5maEUZYEy%2BqRBsDvwfnOis0LH8C%2FkGmARgxBKixsrmeZSlrwmTR8GbTi9bqzFDE8MpidDtCX0TPt8Y2p6cdPO8Uk8gdGt1bP7jNmzFP65jHZYzjTsSf4pXw1YCZYMNNhwnUB6MhQsGkKna2TOIGEXsNM%2B8UAbCIWVepQ423zrE4JW9WizKtWy5HBt%2FhhGFCncXWysNWrwGVrtOFuGVWjs9x5GE6DufMw%2FPdNjGuFni6eIW1zT2okiojO%2BV958rw%2FpuvSF01VF8I%2BL9BmYmZ2KeuoL%2BNHEZb9kDI1hM%2BMOCdgELEmIeQ5P1oz2QkGeuVeKKNjFqKz7xj8pQKtjUhun2d3F%2FS3KZqUB3U5%2BK66b7pjTwZjaTHh4r7quK3YlS0hym2If7wyK%2F8MwMq5%2F0jR3MfwNLTW4fNw%2Fsm2YSg1wc3DLDh%2BHPTQMoaDj%2FZGleVY4RlEfeQr3xW%2Fegybx2UP7xDxJNuhhDROOf%2F%2FvBDw3xSKz9E01n8S0JG8G%2Fi0U%2B5Wl6IQ75lRYg2C%2Fso2CMNj9lL0GOqUBWesi1XCkgZxo0HxMH6nCy9kTG1YjhVsjiQuRPY8I0aIbZ4h78lqbKCR1JLhhKW81L78kYeX8aqx10JCF62QvXluGdLi18mdZokHGt%2FhbL3SmbxKZQ0Q2hFaic0oO%2F%2FMFsgmvxocHA%2B0EP6ra38ezESAhEiDyMSloWwyBvQ%2FYY3hihJQ8ffWmGKs9473PZeMQH9gZ8FcrQz6HI77EwRQGEOFdN8%2BH&X-Amz-Signature=0ec450399d6a544f3ac3fe06b73f8d053085826acee01d6c02133f9173402922&X-Amz-SignedHeaders=host&x-id=GetObject)
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