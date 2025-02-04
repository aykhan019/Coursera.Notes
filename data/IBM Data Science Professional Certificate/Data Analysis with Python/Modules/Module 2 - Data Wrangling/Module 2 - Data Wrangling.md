

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VY5OTBSC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIDUklkO3%2BZFQchnyz6L2hzu4ZIu0GuxH7nu7Sk86ReUUAiA19OTK9eKGhmKlGhkK9Rwo0x2sGmlD%2FuG8gpu7YMLKjyr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMnnO4IU%2Bg7rhNe41PKtwD15t3gC5wbYywg00KoJ9E0wWtDLI666Rkf%2B7EEnpGDAvf9fY8OxIphg64wJoE08%2FO%2FX4JIS1ax%2FO4Wde0zlHaB0rw0aUNjgb6symGD8R9qgZRw9dzF0wmzdtuLicIsxlcJJXtYv1PSOzrh%2FBpOB6%2BuQLViSu6S7zcMHHIzk0zBPfa6fDOa6wGNzeG9%2BQe3kWIFxyQhGrqRNcYDwuMBGHLCwmKYxvQ9PKaRO13p3ZfgX0%2FUtDZm7tA4qKPEc5N0LnXjRBh%2BX0LXfTOSnAlx92B3aqUMKBWSnPyejnvWcrp7Ex%2FktoHNpAY8ENrs8GqAT3U8nuZYWJQWQzVABPzN9elpngxy46Pr%2F5fowURoPgbDXNmogOWkP2UMZxdBa8Q9KBN3PukFB9qnHJ%2BU7TfrlBN8CUJQX0Zo38Em%2FmwFRlxapA%2Fw5R%2Bb5Ta1oBSi26pvnCUzUDmK81NCTTTp5MyDBWQj8wmLyi0H19VfN2kNFr4aLEXW%2FrBV4evP%2BufIANxWA47Ohf62JRWbkYx3gXVr0MGUq5zwDc63060dMmnmKyjV4MxmfXEGZ1OG3v7sBW%2Bd9Gb0VWDUV8GWuerr1gmh6OFWR%2ByFYVRDcODSprbnMNnk7QqwKfZT2wf1YPg7LIw8ZKHvQY6pgF0n28Xn5sq41q%2B33dHQAWqGLEfR9D3Kv%2B7X5KrXdiELCH7gdwTpeeJoEWb4zaWhlPzDRyx93kQwhAD3gBbCFINvSXtPdnv9YjQFYhw8A1mi1EbOQMdJabqnC8j%2FKJuQuMmP2kbzr7kYE2bA336rFVL2Sv7VL9SkE2JtaD%2FtAEncr4ap1tiYL88EyCSJ%2FfRCvOCSQA3QgwvihX0nX5yOZS0L6hXRI35&X-Amz-Signature=c292758d77f33d25f492c785c52a4bdca38225eca7ba5c210856fa80c79087e1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WIYLSN7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIQCK25QGK9Selse1P0S4Be9%2Fp29e340b1MGoq%2FWMOA4JQwIgDo%2FmmyUk73B4pGKBChQrfRFbabHz6MQfG%2B2L4AlF27oq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDALU3bMvBS8pdEzEKCrcA3HpZr9vDtski2%2FvQtsWcuyiziv%2BX%2Fzxm6Va98hd9Gp2Q2XEaDfoCjCIfrZg4%2BO4hoMNBubVGG5hyqkOnPqEgb8AqK2kB3P1LvGXQ9AJH5o6wQ7nlkgdrdS7Zr%2BXBUEQyRcwu3PgpJfc89GQrJ7XDegWZWEJ9B%2BisbklNgL8B%2FusF0MmkIVc%2FOSaHzPSuMIg7r%2B6eaW5QemfzgNUy2KGmujRBGTKgjXb56LHQ56KXKPZTlIfY7bgWk%2F%2F2RAO8aTSrjkzVAcjbGwZzg%2FlDbMjLTeOz1hYSaHiqU1WkkfXmGkxi0T4ygp5ILxfwVpMd%2FljqelBB7iYHrjRZmgANfy2QSO56wz%2Feqg6II9FsPNkiPo5vzwYJpqZ9k1Y7qFLsumrA3uIu6WGZOve6%2BpVYT5w%2FVO5BByD4g6XFu5bSojECfJc0GUmc9qO9h1LbXYC0CAseHaqYdSpg5C1RfN0Jks8311EPBArDItx2WLR60ORPU2dvB3FZQl3wpn4Iz%2BSf%2FEXMnR%2F3czV7cE31gJ79kawnG4arr0pEuQ7dfhlfOBW7O1XY6YaB37DmqPWpwr8t1pZtrM%2B2DJJJejNS6b3ODGQNi26nuFFIM%2FGlyxAUoG%2F07hdh%2BwVgkAG5rHoVQACMLyRh70GOqUBfaUq%2FIfvvmGszdnx4Xegi5t%2BJS%2FQIyEUn57kgKBrBxTj2QN8a%2FEhg5qDF1IXR1xcjNHDufB0%2Bj8SdBv4FZZCg9Ah0G83lSXzGXN7mHKp3wQZRYcjnYmEZI01kUyAOe64Z8sWRkE3GoGkAAdNNym8EUID8KgNZB6MB%2BMhsXnNeOAtxZcMK7pScv8AuXdEeLTy8i7TB8SozghGC4WTBWbxfuOqqD%2BS&X-Amz-Signature=8626dabb197b0e6c5ea6e6497fd74936c5e8adef5ddf5e2ef573c39d0336b00b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SAP6IAH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQDsuB6SCgQKFoQD5k3MQWogqGmc%2BtTyzX%2BNpfN9HaeBGAIhALzuzj%2B2%2B16GVuJTrIWqFdaqz3k8RTqFgZzqGS8pZwSbKv8DCCkQABoMNjM3NDIzMTgzODA1IgyE7bH7pJI8LyNoeKgq3AN91JSEoCmIEDAc%2BpVb2c2ysQKIpER%2FvaLesO11U5pN8hEoJX%2B6OXkOSTHjqclLc1Q7g2Jt5pYrQczw5ndjN26obEJ%2BwR68ooUP4XKL2lCfFmFurzPNS4GIhRUQtkr02rsWpbwVO1CYfu8EK81bgK6JRyfMJ8dQvlmw5dSaW9WxHNLciS60drQDVr3RckaBut2w5Xx3v53WYgdmuEbJq4NGCmMu1cAIMVU1t%2FqltKIyXDLjfUwlBUC7cuUcMvpgxsm3D0lrnBXmxPr1Byt%2FLfhR16IYQHDSuXCcRo4dqhwDaG2G9Z7n6tl5SZfqNFJYhw3Wu9YqMVBO0NVLAFfr1mH5wJFiwNCkfL3moGj%2BN6hMxJsx6Gpo2HosOAc6Lher7uwtedyo9PyyMMxDOyEULg%2BBpiRYptEIPJiyqYOAVl2sEOF18oAp3Kw7ot%2FfhvQ2gxFDM3Od5WNVDU3z44m7emzCoqSEVyUfZTJYd3qhYlOHWRhwCS22GRHmkMRtcJp2NSZee%2BIWmjseVdWvtQELaBQRlOCLJNGGE53KNKc4FaFGTyB3%2FApcssteWZkUhlD7PkQqJgYncPun%2Bh0Yh08GjRDsOGXBFT6vwn7qZteYbXoL4ZrHP%2B7zMreOi2AiNzC8kYe9BjqkAQODcTPD%2BUpPy%2BXq1KvCWpCqMnYwvD4VbnvH1JumDDauNc%2FV%2Fn%2FYT8L0QfDnpxriPLB5CDqXgVphIKoS5kg6EtcTEk8nta4l0ziEsXpoNAjY6%2F0vts9PDChIIpnNd6Lpen4Bo07RsJL%2FCoiSuRQohNa2bSDhrMKq%2Fx%2FKA1gEu%2BJUKmMFxDD3an9Ou9sv%2FuT%2FLloDEXVeXMlNQkyAF8QxzdZurBrw&X-Amz-Signature=dc4c8ce3b721be00f92d50f5a11fca4d04c7b1597ebfadb99572842b77b6664f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQ5SJCII%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCZxRCBekKHNLNu4I5jnaH1N3DOjinbaU84p971CnXMGAIhAJtWgwkgHZt%2BelSycKfHoPbp4H3QnUreMwwP2KV1aDlBKv8DCCkQABoMNjM3NDIzMTgzODA1IgwL4DVnRm5jMw3Mt1oq3APD%2BPAnh4qdrET9L%2FXFeMU%2Fnrcy962WHUhxEUXpz8FgSSgCkOmPHj42xF%2BvK2C8R9dkpepI3WuyCkIQDAhNfvQGFKodd2i%2B7aQzXtLGpAYAvwlGpBruiEttXJRGVyPwkXbBxk3ex7CHMFGoiTwgXKgnbhDiv98qs31mH3KugS1%2BJRl%2Fi0K4forVz%2FRWGLmPhcWD%2FsD19x%2BYZFgvFeNMjgsVEG3r0QxCnb1oCr01WYKvFSpE%2BRhkOvd8h%2Fc7u1zQ9c563tOkeTihP9Yt7wpqQQIB6mQ%2BHGusJJevJetPAbt8F4caZknVLtqbAaSgnSk4G6X6hfl%2FWA2BrM1nK4BAd4PcfyxVzuN8bi6WN3DL3QTvMyBjp1AWbXgwpvxFgmVtAbPo8Jte8YjG%2BJQSAfQ%2FtTuMa6t0UTo7MT4NXwhXeC4DgJCILRzZGlE5%2BRUwbHOuZlW%2F27HxIYG3ncSdklG5is0uh9pg32M%2FfZgJiI6K7%2B%2FSEoIt8fa9V22%2B%2B70c7XtijVLdDWiZlz2OgwoCAF1%2FRk7Ensg%2BzcmKm7CGSuw%2FpeQI7I4Q3E%2FhkqSOP0cDtGYp9qWOP0W8hdw%2Fxlb9gaA0DvwHA60detz70NfHn5NPZJG%2Bg9mVe5YRdRkhfV90CTDBkYe9BjqkARXKZqlFlWj6A3MbR6kolO56GyWAwWnTxTkKv14O7dvSiyNpYwpPdYjQItHxN890FtbGYfryPhiUWx%2BcPtkF36odotvqIsoqp2kDUVjpCQlw5fSYTT6E0nNvXMAx2eQ7o%2BHTkUtMJnuYzOATBr2GdCdjG6TZ%2Fu5WXvph2zz8n3%2B10N66EXoPgIVFDAHWNblUTEaTtk%2FafLMi%2FmIhzB94Hx0YaS3l&X-Amz-Signature=59394e053eb29470770695066174bcaf181eefd89610bce75ef6238f1b31ddf2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZKHZEL2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQClNis1728kgRfOJda4tVAMzlLwI2iJVgCIX44vbc4dfwIhALAu7aTRgmX9LKGB3KiIq4dQXHkD1CAS4%2Fs5eAR5XYA5Kv8DCCkQABoMNjM3NDIzMTgzODA1IgzhGV7QAKP8hSSdTTgq3ANyh%2F3XmZLCmsmebPM%2ByMNpbK9a7qK72wlSOS5nmxIr8hTRghiGTVklK0Xpg7Zv0WQOwbek6HU%2B7uCFNdao5xULQr7aXqclvnW%2F%2BCBoSV6SM4JmCb%2FsfSfwEGww1jMQozxTW%2BTmT%2F0YHG%2BjwiWZ6i1lra%2FU9H1hQNDi5wje2jBYxaMjgBwEHvO%2BI1KEq5j%2FEhWbvfCs72yH%2FRoH8fMReOb0Fx61%2B3Z1XV3n7rCrFbuor3Yp71L%2FM17vE3630oGDKG1YwobQuBiE0SHdJxSeWeUHw%2Bn7T%2FV86CXZvY8Ku426aF%2FsaLop%2BHcW8RZOM0wtDJQ8Lh10U3H0wmFmtFDGGTo6vBWILtygetnobKSoJ8zE%2BVT%2BG3NmQ5lgdCL41GZ985tyIllgz8QpnTN2vjmC3tUywMAJeL%2Bc8PBfyx7moqzD37LD%2BrD%2FfTUChd2q3wIS5YsJlWoA8gsH281JeL5P%2Fqo%2B%2B7t4r3l84LbVwHmwNveD3NiPbctlHmgV0VMkZP%2B67pOFXowhG8zgb16YGvOOIZu8B1hgxfUmMt93IUZe7SpXTmScGX%2B6x8EOVapl%2FXVxMgqikQstZoPX7MVYVz0Qk6QLcKfRtRBupkVKZv8CpE4A4dHywmpicoUjG461DDDFkYe9BjqkAdmOq46hMm0lyiqbQfSkL1l91BO%2FM1fm%2Fy0vYKGpMH60gs7hyx3bB5q3c%2F6MkE8HSkpGauh%2F%2BGI6rYRzilMHUPSHbj2Bfz0X6ZFb4sgXbGwrwS9FLy7QKSB30yUcVyVXUStIF1vQbqRZMTakQdpmOZfhLmYGjOu0Pq9BNSb2kHFKRNXucehtSPdCtwg1h%2F28vcQzKNGbp%2B9%2FPINLLD2DtewfWrWS&X-Amz-Signature=51541157a7fdfcea3648d00cf0ccedc1fc540b651745420714795a7f9da70c51&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM2AQT3W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCXk1XqJJf2GZ2Po2oTU1w8lfbv3FYWIsfx1Yatq25cwwIhANZ6kUE%2BC305D%2BtOFWi2OHuC3Y3ZUYG99rEo%2Bvyo5vJOKv8DCCkQABoMNjM3NDIzMTgzODA1Igw9yL9ynKj4%2FeLJnWkq3ANJZaSztwtubo3JHmwqvlLZSPV2POQcQpuUjbPXo%2FijUHF7H0FW8cct2WtNMEYcqB%2FNPeGUSRE0yIv2sNgx8QA0LqltsLnDQLbiHgV%2Beq3pazsp0h7zQugTpWakAmLYaDLfVpphryAMJ747XoeAg9mIi8FFfYfpy4E1bqgMOZ6%2FLDX5itwDdaYVbjwj22t0P66apdBpAytDfyD4oM7H7exxbqzlNtNZqJ93N%2FZoqpf3YAdAuXBofd39n71lw4wjypZSSLX1K%2FycfTaDk23DxST%2Fj%2BGC2PwL31Jobp%2F2sqKRxH0Nzif7L%2F3Rqn9Lu%2F%2F7%2BU9lStO%2Fr7mB7kwPYUyQSIFLOdQRA5GJH0HPWTk4dZ2Au6SMzlcMOLjDPH0fzPvWfEBQMkgEq4bHcOnm9MpXQuXylmh8aG%2FwxzmlH%2BToZ2C16Mb1EizoY2rh6vd%2Bzj3E9T7d7T5D3ugV4U2OCnNklOO5X217K5eqS8AbQ0x6MC998f%2B5GUrTVWmoq9Ex0FaigdJL5DXsQdfTAEsJq3FSrGw8rUKGx7CtYtznAfDCtMMqZiQqGApO2SCm5XobP%2Bv2kmoaMTwwtlnYvovXwGWChOY%2FJ8HCYmsmvOMTMZ37GXZyTmsVOMH93BXFFEVW0zDWkYe9BjqkASjEkcCKemkp8xStcLvAdHvL1Htf1HiECvXRW50QHmNZBEMZPTSrGuftm3UC9rT2cRWPRM3H1XC%2FvLgifMdC0V1yciBQIx%2FZZBPyh92VhtzgY5O2HXHEfxaGgdgCC1pC8%2ByBYMI%2FNkTDJQwzjk1bcR4NVnRnLVGu3aTJvJWfxezfvvqOHQG7BngI2B7oQ%2BCroOUkh4sPFKHW3gsr870dXI5ksVe7&X-Amz-Signature=29d29daad3fc6279ac8fac6646dd24f41655e9aa9e129aa36e146b361ab87e62&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7T2JOLN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCOJ7iexkJ3CqnF0EQc%2BEo51PZ3%2FccjvKZ%2BsQVqCs4mlwIhALmoPEcNikQujZuVPZZaaU9ZXTZaIiOy17nQvaGvpCuzKv8DCCkQABoMNjM3NDIzMTgzODA1IgzgllJv7MeQrIerSSMq3AO2iM21pY7JtX6TeivcvT%2BRw%2BiYmiSu%2FN7BjLCZJHsKIv2Cm8LfVNYgri%2Bs61ND9YwSR0bTtQ%2Fdspb7bqS9jpE3jZnRa%2BwFUUH7G5V0WxHVWvbR5OHCLlud1gATZzH4h9BsxTS2UmZUZHRd%2BTsUAn5y3VU5%2BpeafDB6QFCCYL%2FGLVH0vcim0v0dnRhmNYC%2F30174HWeVrBWsDBChBvBGZrY2FMxAY9tdhERniSI5HK28B9AATbstw0X7hZlAhgUBv1xhL803d4z5KOszsohsJ1fusGUmNxl3wQLNBek3mFFh3sq%2FzNMIiMiWRDtSyYJp5igROXXCEkrkyvZ0ModPry3ecfZiFcvn7Qtc%2B4eazMOXiEQG0e16C8t7b%2BwljbxfwzitAuWQ6XSCjCvgMrUwIp0rlvnvoXHMzefVS1P9qu4csIsUDnILSk9AxLFj8LAcNfBgs%2FWMz34An7GfpZN48cfwKXLvcsLQfbiDD0MQQHgFeb%2BFp5jutHCFSPbooQulq3GjVaDu%2F2mbUbEyt2SB22l6I5q3C3LT0L8wvhwS%2Fd0AiMUXaQKUwZFIGvm0mbM75iSX%2FxJ6O8%2BJYR3GEAJz%2FA1vMFho%2FOtavgHXOUMib5ISln9CzjFuegxveXSdDCZkYe9BjqkAWNHN8tC482pBgaew38gT6zaol4hKDy9L5HCzUShfxvO1o2YFk%2FEPvjMu0%2BwGqW49LFrUSHhkwE4Sfch7IxTGEPeShxdDNz0zwVPjTRpGuybbTdAWf6oVCT7%2FQZV9eZ9zeRLOT7yYUwBLDjOQzbkwJI4vvL%2BVSM1Ot4RishMq3OcheloiAXJdbrei3msgurbsAT6XW4WrP4KCdAIoNZXQy%2B8SAGs&X-Amz-Signature=a25361803e062fdc6b952cd477bfcd03c2b6a92632c5f806d2bfe4f76d0e03cb&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674DVNYIL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIFTx9BmbP%2B1ATSYu%2BjO3jO8YhpLPjI1Js55ZR9DP5E6wAiANtKyI%2BNaVbc0Ow2mNAjQVfx9Fk2l0DAM6BDRH5H%2BmSSr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIM82%2FVCnTF5INliSh%2BKtwD2%2FGW%2BszI60oIAvSKdqZ76cFTflcSoKEgPbU4CJOyG50tA40Y2UhuTQunEyI6xnBL%2FV2BjDl0BW8DagGnF%2F6umK6bTsjLGC0A%2F6zA77sIFG0uKtYSdAmwezKp6Qufda%2Bs4tqW92GuNYAUO3qDlZDpjBE1QJBCY0yq%2BTMfm32PWkShFPUaxRvb7kVPW2iHa%2FxwK%2BJxt0FWPV6ov84T6VFTo710yFs4tVONPN5xGqpT4NrrHiqKLFoeLqwe8RmY7VNDxlS1HisizPVLHbW%2BDTp1C%2BJmADC28ChuS3osi9slhmN2qaAyKxkovX2DfriJFv%2B3MfImik7FG0XW4B3bEz98uYiiEm56GqeUahE6t1kF6mAh8JnSUf5jbRHoBQ6%2BO%2Fb6xCBU2cF%2Be%2BeY8Owrc87Epm9sOFcA%2BWF%2B1ftcOTtcWrrmIdOSCXrGV2kIjReK1xGmO%2Fcwdp3ID45v92tdzwnXW%2BVPESQWSqT%2BXx9ll0J249uez8QZ2Jht%2BXTQsnpCHTg5B4nhywgT1pIhI%2FGwqY2On6LiSAoGl6yF97nE47XmBiqZuDs%2Fbh2MTIFlc0ZqFs7wdW8cVaZIGT5IbqW%2B3Pdy9KE01CjWbejacH9Hk8c2JERM%2BbHXeO4Ke0hfpaUw95GHvQY6pgEf0EMiZVCi3%2FbkoxTWw3jbUTfHirVPIkZSni1JkEyfPFmz6OpaQvuCIoVB18i%2FOcp7w%2Fhn50dZtBC5AQrJFikG11QWvn7e9GUCCsZ%2BKmEmexItVrxkHdSBrevpIeaYSRXW%2BMfzDdvmb9a9s%2BZYBTWFlIcWkT58znFwkS1z%2BSw2JUG9M3JoZZ9B6p9nMH0Fr4r1VUBQjJztRZ5p%2BRFcdRjqLoqwlKzg&X-Amz-Signature=ab12ebb28d2e566e43fac1aecc78e7366710ed4a82e69335248971cd1cd0f9b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZKHZEL2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQClNis1728kgRfOJda4tVAMzlLwI2iJVgCIX44vbc4dfwIhALAu7aTRgmX9LKGB3KiIq4dQXHkD1CAS4%2Fs5eAR5XYA5Kv8DCCkQABoMNjM3NDIzMTgzODA1IgzhGV7QAKP8hSSdTTgq3ANyh%2F3XmZLCmsmebPM%2ByMNpbK9a7qK72wlSOS5nmxIr8hTRghiGTVklK0Xpg7Zv0WQOwbek6HU%2B7uCFNdao5xULQr7aXqclvnW%2F%2BCBoSV6SM4JmCb%2FsfSfwEGww1jMQozxTW%2BTmT%2F0YHG%2BjwiWZ6i1lra%2FU9H1hQNDi5wje2jBYxaMjgBwEHvO%2BI1KEq5j%2FEhWbvfCs72yH%2FRoH8fMReOb0Fx61%2B3Z1XV3n7rCrFbuor3Yp71L%2FM17vE3630oGDKG1YwobQuBiE0SHdJxSeWeUHw%2Bn7T%2FV86CXZvY8Ku426aF%2FsaLop%2BHcW8RZOM0wtDJQ8Lh10U3H0wmFmtFDGGTo6vBWILtygetnobKSoJ8zE%2BVT%2BG3NmQ5lgdCL41GZ985tyIllgz8QpnTN2vjmC3tUywMAJeL%2Bc8PBfyx7moqzD37LD%2BrD%2FfTUChd2q3wIS5YsJlWoA8gsH281JeL5P%2Fqo%2B%2B7t4r3l84LbVwHmwNveD3NiPbctlHmgV0VMkZP%2B67pOFXowhG8zgb16YGvOOIZu8B1hgxfUmMt93IUZe7SpXTmScGX%2B6x8EOVapl%2FXVxMgqikQstZoPX7MVYVz0Qk6QLcKfRtRBupkVKZv8CpE4A4dHywmpicoUjG461DDDFkYe9BjqkAdmOq46hMm0lyiqbQfSkL1l91BO%2FM1fm%2Fy0vYKGpMH60gs7hyx3bB5q3c%2F6MkE8HSkpGauh%2F%2BGI6rYRzilMHUPSHbj2Bfz0X6ZFb4sgXbGwrwS9FLy7QKSB30yUcVyVXUStIF1vQbqRZMTakQdpmOZfhLmYGjOu0Pq9BNSb2kHFKRNXucehtSPdCtwg1h%2F28vcQzKNGbp%2B9%2FPINLLD2DtewfWrWS&X-Amz-Signature=a17cd87eef4a1aa1da0a72b018bf581d19857625b477fcde8c2fd677cf62ea6e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2W426RE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCj81RceZRK%2Bw2HttO0syG6ida6y74XXU3h%2B1KQQ5usxgIhAMAFRAUnNMSAhX92TVMNuROCzYyr18X8gjXUGRPrzAayKv8DCCkQABoMNjM3NDIzMTgzODA1IgwsDuXrv9%2BH4qzAVKYq3APZVJXw1NEPTpNf%2F64Glm2jW0AOko1portL6IOpLaLEcc7ycGOPuYRVLhhY9fcXB6MxRY1jybdOHEz0r%2BfYmIZWVGBlBqRYpEVSgV50Dw%2BoSTZsnV%2F5T%2Fjjv%2FH9ujAFcBHolmP9OJUlI6nuA0wI5rAb3JLah3vJoXEvB1VELI%2FXyR%2F0071PfT4dho%2BgHdE5Y4y5Cz8lbKN58tzUs280at4gsgWvMu40Cfq4Sd%2B%2BWMvStlgcvFdA8tBS9il1oOzHSqdq7pqZ2ujYa%2Ba9nICGWyreD9uM2ApGFfbvEC4EZS5le20mE%2FtaVJ%2Bvp9%2Bw14ovfKjrJKzeAQfX2XOgI%2BkIqsFRm6tQstj%2FPQ2ikpB%2BfuEOhm%2BE5Ddb9O8%2FCK1zScYluRCH9Ja7j5uj0p2PgK8iDcIHAAUJ59Y4BMzdDOZtVqXeNGdAXaBGbGGuUKpiY61jOpGuPcaBU1laNig8HraM01qC1YkH0yKTeVNvTvcVwXlswlG6XOBixOoHaqq0j%2FJz0sWs2gvHWkZrybM5vE5GyIRwPIirG6JveXm7ylBo%2FdpH%2F7FUr8rupNIP8LgtRSmMFnOT2bWX4pwjfLC%2FPIY3CxMRS4w6rdwLEoHeYI8XXXDhZw%2FXUbrdd0ABr6NrZzD%2FkYe9BjqkATIyTo%2F5694pThloSEI2MUvX%2B3a%2BCtvLfjTN2puVPJmqqTOSixkd2kd0%2BAuJi4qOnG5sAqEcua95UnUlkM6XbLeJ6pY%2ByJwWCR3khklf4ejf7xxvexGtFqHxjwJyh8Tg4Ark99dioQ0vyw79%2B%2F%2BaUHZ%2FLGvw8HCdme5rPC11HwL28y8tE67fJ24kXv9KF6jF792Cn4BUcru3JNv3M%2FRfJQd7Ko1I&X-Amz-Signature=dc96e841cdc73b23304daaeca94f800eb2160b6dc621b03e9fb56987be6b4b7d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2W426RE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCj81RceZRK%2Bw2HttO0syG6ida6y74XXU3h%2B1KQQ5usxgIhAMAFRAUnNMSAhX92TVMNuROCzYyr18X8gjXUGRPrzAayKv8DCCkQABoMNjM3NDIzMTgzODA1IgwsDuXrv9%2BH4qzAVKYq3APZVJXw1NEPTpNf%2F64Glm2jW0AOko1portL6IOpLaLEcc7ycGOPuYRVLhhY9fcXB6MxRY1jybdOHEz0r%2BfYmIZWVGBlBqRYpEVSgV50Dw%2BoSTZsnV%2F5T%2Fjjv%2FH9ujAFcBHolmP9OJUlI6nuA0wI5rAb3JLah3vJoXEvB1VELI%2FXyR%2F0071PfT4dho%2BgHdE5Y4y5Cz8lbKN58tzUs280at4gsgWvMu40Cfq4Sd%2B%2BWMvStlgcvFdA8tBS9il1oOzHSqdq7pqZ2ujYa%2Ba9nICGWyreD9uM2ApGFfbvEC4EZS5le20mE%2FtaVJ%2Bvp9%2Bw14ovfKjrJKzeAQfX2XOgI%2BkIqsFRm6tQstj%2FPQ2ikpB%2BfuEOhm%2BE5Ddb9O8%2FCK1zScYluRCH9Ja7j5uj0p2PgK8iDcIHAAUJ59Y4BMzdDOZtVqXeNGdAXaBGbGGuUKpiY61jOpGuPcaBU1laNig8HraM01qC1YkH0yKTeVNvTvcVwXlswlG6XOBixOoHaqq0j%2FJz0sWs2gvHWkZrybM5vE5GyIRwPIirG6JveXm7ylBo%2FdpH%2F7FUr8rupNIP8LgtRSmMFnOT2bWX4pwjfLC%2FPIY3CxMRS4w6rdwLEoHeYI8XXXDhZw%2FXUbrdd0ABr6NrZzD%2FkYe9BjqkATIyTo%2F5694pThloSEI2MUvX%2B3a%2BCtvLfjTN2puVPJmqqTOSixkd2kd0%2BAuJi4qOnG5sAqEcua95UnUlkM6XbLeJ6pY%2ByJwWCR3khklf4ejf7xxvexGtFqHxjwJyh8Tg4Ark99dioQ0vyw79%2B%2F%2BaUHZ%2FLGvw8HCdme5rPC11HwL28y8tE67fJ24kXv9KF6jF792Cn4BUcru3JNv3M%2FRfJQd7Ko1I&X-Amz-Signature=c31e0571efd0e9425e913ea9f18be44bea60cc5ebfded433eca2a991453082c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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