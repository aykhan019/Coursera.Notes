

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=8acf8ef225d267341b65eb72766b76fb521e143bdcdbbaf281e11c11f12b483b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Example Dataset
Consider a dataset related to CO2 emissions from different cars. The dataset includes:
- Engine size
- Number of cylinders
- Fuel consumption
- CO2 emission
#### Predictive Question
Given this dataset, is it possible to predict the CO2 emission of a car using other fields such as engine size or cylinders? → Yes
### Historical Data and Prediction
Assume there is historical data from different cars. The goal is to estimate the CO2 emission of a new or unknown car, such as the one in row 9, which hasn't been manufactured yet. Regression methods can be used to make this prediction.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=9bbc25257c05c0464f00d6003b4a48068637ab97eeffd71e4694cf674c5dac14&X-Amz-SignedHeaders=host&x-id=GetObject)
### Types of Variables in Regression
- **Dependent Variable (Y):** The state, target, or final goal to be predicted.
- **Independent Variables (X):** The causes or explanatory variables.
### Types of Regression Models
#### Simple Regression
- **Definition:** Uses one independent variable to estimate a dependent variable.
- **Example:** Predicting CO2 emission using the variable of engine size.
- **Nature:** Can be linear or non-linear based on the relationship between the independent and dependent variables.
#### Multiple Regression
- **Definition:** Uses more than one independent variable to estimate a dependent variable.
- **Example:** Predicting CO2 emission using engine size and the number of cylinders.
- **Nature:** Can be linear or non-linear depending on the relationship between the dependent and independent variables.
### Applications of Regression
#### Sales Forecasting
Predicting a salesperson's total yearly sales using independent variables such as age, education, and years of experience.
#### Psychology
Determining individual satisfaction based on demographic and psychological factors.
#### Real Estate
Predicting the price of a house based on its size, number of bedrooms, and other features.
#### Employment Income
Predicting employment income using variables such as hours of work, education, occupation, age, and years of experience.
#### Other Fields
Regression analysis is also useful in finance, healthcare, retail, and more.
### Conclusion
Regression analysis has numerous applications across various fields. It helps in estimating continuous values using historical data and independent variables. Various regression algorithms exist, each suited to specific conditions, providing a foundation for exploring different regression techniques.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=a965c5e7684a225cde33e44b9007299cca27b159498c3cdd8260ffe3df712df6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## Introduction to Linear Regression
Linear regression is an effective method for predicting a continuous value using other variables. This introduction provides the necessary background to use linear regression effectively.
### Dataset Overview
Consider a dataset related to CO2 emissions of different cars. The dataset includes:
- Engine size
- Number of cylinders
- Fuel consumption
- CO2 emissions
The goal is to predict the CO2 emission of a car using another field, such as engine size. Linear regression can be used for this purpose.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=76161cbd8c9fe147be12975cd7af8e82e9f411019115d20e3bfc846d4411646e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Linear Regression Basics
Linear regression is the approximation of a linear model to describe the relationship between two or more variables.
#### Variables in Linear Regression
- **Dependent Variable (Y):** The continuous value being predicted.
- **Independent Variable (X):** The explanatory variable(s), which can be categorical or continuous.
#### Types of Linear Regression
1. **Simple Linear Regression:**
	- Uses one independent variable to estimate a dependent variable.
	- Example: Predicting CO2 emission using engine size.
2. **Multiple Linear Regression:**
	- Uses more than one independent variable to estimate a dependent variable.
	- Example: Predicting CO2 emission using engine size and number of cylinders.
### How Linear Regression Works
#### Scatter Plot
A scatter plot can be used to visualize the relationship between variables, such as engine size (independent variable) and CO2 emission (dependent variable). The plot helps to identify if the variables are linearly related.
#### Fitting a Line
Linear regression fits a line through the data points. For example, as the engine size increases, the CO2 emissions also increase. The objective is to find a line that best fits the data, which can be used to predict CO2 emissions.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=c8b0ab6a32c7e2aea7cdf280041bdbc0c3fb1b2890b0fec87ec800559f58d728&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=f5d51047b827f1a54990b2c150c34efbe30f8b79c3239b4f46355ea12864f71f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Mathematical Representation
The fitted line in linear regression is represented as a polynomial. For a simple linear regression with one independent variable , the model is:
$ \hat{y} = \theta_0 + \theta_1 x_1 $
- $ \hat{y} $: Predicted value (dependent variable)
- $ x_1 $: Independent variable
- $ \theta_0 $: Intercept
- $ \theta_1 $: Slope or gradient of the line
#### Estimating Coefficients
- $ \theta_0 $ (intercept) and $ θ_1 $ (slope) are the parameters of the line that need to be adjusted to minimize the error.
- The goal is to minimize the mean squared error (MSE), which is the mean of all residual errors (the distance from data points to the fitted line).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=cf1c6df7aa63cb62511627f3be830f924ebd74967531e92b8c56734a43afde6a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKG3TRJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCtjfddh1LpR%2BRkAhbxmcc3SKAcMiJzSjci3DT0QaEzHgIhANE1ZDX50zoOiYexGhkUOpBMwBXqGTZhYOhoIR6TtZqNKv8DCGMQABoMNjM3NDIzMTgzODA1Igz8YpULU8CGIJB4Sacq3AMaaHRUX46LRvqtiQKMoG3zix6xlKtVXZKDWuekk3QGsjgmidnDPaOPnC%2BHqhNS8O4hzEgkmvAls401qGMWrWGDcsEqggD3U1sLtXJ8RXyGbBGixOChc9I7Wj5Pll70%2BjsPva7OMOamolxt9oG%2FvYnC2NYhJRNIfIaVghavlPeMHDknu52T000aj5YOxpeXzuyiTsCQXINYGW1L%2BlEIqUgpIMT%2Bwcml%2FIYDcjyrrUqWX%2B9IvXb4OoO%2BUfDWCANjPOTIW5Rs%2BQg55OekvwxJW82OV4A3%2FiX8sKjZmDv0I45HLNyqWC%2BCp%2BnuwDg67aK3uK0lhoeATbrPsq%2BUlaxmPt5Rd81yjrxssWICfl5aiCIOXC9uZSUkH6wfLNdAiGtaj%2BSJGrpI5DhPob39ByV7PsvIiNHS6cPklArq3yZ8YRUC5dlF5dsDMAtLUbExgvKGKn8i02tHqW0Uget5WuCwCLZBSuMp4hp%2BLTjtdl2Plw2sWkcJwl93QxUjV1w83ZQzosKbkeMvvTgOj7v88jhEt6fOSDm6vGN9iB%2FbEafvl2DjJwf8ToahjrYZZw8MAdsM4ffD%2BnXyafhFhS%2FiJbJtyK52ESqXEUs560t7WlbKFdcleGIQ%2F30mzvtoIa5PEzC%2F%2B5O9BjqkARnVH82KNZvO1ZZ0fUjs3zecfF%2BaS4SY%2FDOa3P1z9uIsaO1zQ4RmsSC5fsmpZXUIUPpvy5NC9kl0PKTeVGBauZu9mqFE4ms2MHnFHPjaong3%2FCtP2yX6iDVgB7UnNKp1O3cE3Fq5Rw2XANryWIz%2F1F7nOESn4bzYda7P1VeSPMdTCyt9k%2B%2Ft9pLDgZj0fQZyirULt%2FLVCHrObEhM7XqD713SGkWv&X-Amz-Signature=d050b824abf2df97f100a9035e1c3b2943cffd20b05bc9410f41c4986fc012b6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example Calculation
For a dataset with known values:
- If $ θ_1 $= 43.98 and $  θ_0 $ = 92.94, the linear model is:
$$ CO2Emission=92.94+43.98×EngineSize $$
#### Prediction Example
For a car with an engine size of 2.4:
$$ CO2Emission=92.94+43.98×2.4=198.492 $$
### Why Linear Regression is Useful
- **Simplicity:** Easy to use and understand.
- **Speed:** Fast and efficient.
- **No Parameter Tuning:** Does not require parameter tuning like other algorithms (e.g., k-nearest neighbors, neural networks).
- **Interpretability:** Highly interpretable and provides clear insights into relationships between variables.
___

## Model Evaluation in Regression
Model evaluation in regression aims to assess how well a model can predict unknown data. Two main evaluation approaches are commonly used: train and test on the same dataset, and train/test split. Additionally, K-fold cross-validation is introduced as a more advanced method to address some limitations of the other two approaches.
### Evaluation Approaches
6. **Train and Test on the Same Dataset:**
	- **Process:**
		- Use the entire dataset to train the model.
		- Select a portion of the dataset as the test set (without labels during prediction).
		- Predict target values using the model.
		- Compare predicted values with actual values to calculate accuracy.
	- **Metrics:**
		- Compare actual values y with predicted values $ \hat{y} $.
		- Calculate the error as the average difference between predicted and actual values.
	- **Advantages:**
		- Simple and straightforward.
	- **Disadvantages:**
		- High training accuracy but low out-of-sample accuracy due to overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QCR5QLS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIGbeUeJyYdgHbrv%2B6yye%2B%2FZmdrlLvNn5diN9wYV78qWWAiAyjvAS0qkr41VHb5Rjckr46VN3UwUYStQc4r4j1uVtjyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMG0PaSQkAJ8nNLuPdKtwDTdtErEAKt%2BDqlWaYXqT%2B%2BCgxy%2FlDzKfPqkswqvrgfxihzLyXijwbbjdnqfnthiIjSutYvwN3A9mMzDANw482pGoCvJhOsLNz2wF%2FNA%2B9VuTOXxfwXyZvlJV1NTJH8ZP8VGX5GjLv2e%2F3JnQ7S33AmEaiJyeEVuwPnUhfI%2FmHapa39xbb9vpr%2FG%2F5Q9qtRV9qSzKdvGA8BcshxBrMMBoJCGe7Pt27TliXxlb%2FpMMDfh56dzkYzl3sxt7VD1MOGw6W3xj%2F3WGiIX4aimnPHjOi5QBfhpcNEz%2BuSEf7cuyFPCDhgg%2FBwcf8YW0Dr4M5NJSG0PKlpxHkE71HwG55u5bgjTl1YO38pkQuVhpeXdevyTVviK8rl6YfCpx%2BVb4NP2RJn5A1%2BQyrJyEq6C%2BVU0jWSeRjtvDKeYvGByB16B02CehlffP4oB0TBS9S5knN2A1y2CF8RiBKHVT8JLS2BoRFgTagWGPYvNv6E0zkVhKCpI%2FSIJ339C3EeLlUzKrc15XUTKOcKe3xQpRDlZ0%2BTNmDGw4ztaFX2s2L64muPzRQG3TWO59ibYPfCFQSjnGKF3MKf%2Fc6p00TVQUcJjPLQl48Dlx4KnBvh7odSrTW9zJ3mhHmAW90tnKKgQRHikUwmvuTvQY6pgGtPMD523SluV47HLHfiZseYs4%2Boq7jFhoiilLa0QjMz8I2S6bcAXr9eVISRXp8GnPigDunRa6jORPAL9uwj0w9Iwe4RAWgUAjrxDma5PYSRUH9qM21SIY8JkQABjGccdLPBm5RwYbzJX53QZxnL3%2BX3Et5CxT1WzW0TGh2MrrQ50YdLOF%2F%2FBMJdC8QJgj%2FQzovjHA0qW4TQTn1OJmuzRxZD1oCyX1f&X-Amz-Signature=da33bade1e001c80e52e10d31f9ce029ae5ee4255c219d19249f96f22e269328&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# Predict on the same dataset
predictions = model.predict(X)

# Calculate training accuracy (MSE)
mse = mean_squared_error(y, predictions)
print(f'Mean Squared Error: {mse}')
```
7. **Train/Test Split:**
	- **Process:**
		- Split the dataset into training and testing sets (mutually exclusive).
		- Train the model on the training set.
		- Test the model on the test set by predicting target values.
		- Compare predicted values with actual values to calculate accuracy.
	- **Advantages:**
		- Provides a better evaluation of out-of-sample accuracy.
		- More realistic for real-world problems.
	- **Disadvantages:**
		- Dependent on the specific split of the dataset, which can introduce variation.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJPPDDXH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIFSFc64BVSp8b6Ae23WBjXXWAJFr%2BqFUFH6hhQId8%2FlhAiEA1YXwUQlAVjVBMkcvhs41mBsgafFZVoQ1vMGE0T0iuz4q%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDIigFAHBLa2Plh0BxircA%2Fh3uQNWjX0CvHX%2Fz5qmsZe%2BNvNLUIUlU2hH1alFGPj5EhdPHJ%2Fd7oBwRrlobU4Kfwfk4ezXCmAtby5qySa765oIFaLypxKOyCONr7XFNQYSyEMfAxfs2ujpCFMbhbCNtvT00x%2BrQ2efk3KfAOXpO6F4QgnROPAudCbj5lIip4aNZJ1tqp3z8DMlT1ZHN5bfhCriStP9Pzq%2BTz7G9ipWCideMTRBvWe5u80OdaKG1tf6Y%2F%2BZAP80OjFvy%2BoA0vn2knhYBw98FCPul%2Bmr4mmn%2F3pmfi2fMLeV3B3z1JNA5mSpVSbPSMmatYy4fooD55rvsuGSVcz%2BIAFuZiRRmMoXOB%2BSaaIZf%2BxRWf%2B51LKrxoaCkQJlrXRxs9Vx7CGkPdcgF18BJ%2BEW%2FkDHtXbNKO%2FIsZTnfdEGtwTjPznY0etOiLvCxC0LSeoAdUBinthqjbqUiX5W3fg2x7qpSLZeamj%2BSxNMMJwHdWsnM0bCuYmZ46R0vVpM5IWqMabHb1PArZR01Maem1QT3FEMhKCbUCCMbPqaB2s%2FkWTyxIlwy6jN3It8h8pEagat1kM8VWW7QGwhELtFL7MQQL4ZUtAg7%2F8UNv1P1RK4ASiQGyK%2BRGleiF80KRlPNKGvg9OCb42DMKP7k70GOqUBAsPkSnNXxjbBGgTf3OfWIl6mFUwTAzGAT63Ejb62AV3YxI21N3RnFCiMy9Se6twRe7JCdn8uAH6LulcvY3pLxWECUWXDjJ8PvLt3M7x0Cuaz%2Fc%2BpRIB%2FLNoP6z8%2BPoWKg%2F1E5LhiB6ZHWxtl4P0iVYvjLC%2By1nPdWhQ0U3V%2FMTCrdcKTAz4v9XpGp9ACU8M4a78RVOH6yxN4JE3kW197K26m0GSc&X-Amz-Signature=f197ae50e93ccbcc6a800a575fba73be901ac93df969c0d3fe5583a0ffa4b51e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.model_selection import train_test_split

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Test the model on the test set
predictions = model.predict(X_test)

# Calculate out-of-sample accuracy (MSE)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error on Test Set: {mse}')
```
### Key Concepts
- **Training Accuracy:** The percentage of correct predictions the model makes on the training dataset. High training accuracy may indicate overfitting.
- **Out-of-Sample Accuracy:** The percentage of correct predictions the model makes on data it has not been trained on. High out-of-sample accuracy indicates better generalization to new data.
### K-Fold Cross-Validation
K-fold cross-validation is a method to address the dependency and variation issues in the train/test split approach. It provides a more consistent measure of out-of-sample accuracy by performing multiple train/test splits.
- **Process:**
	- Divide the dataset into  equal folds.
	- For each fold:
		- Use one fold as the test set and the remaining $ K−1 $ folds as the training set.
		- Train the model on the training set and evaluate it on the test set.
	- Repeat the process for each fold.
	- Average the accuracy results from all folds to obtain a final evaluation metric.
**Example with **$ K=4 $
- Split the dataset into 4 equal parts.
- In each iteration, use a different part as the test set and the rest as the training set.
- Compute accuracy for each fold and average the results.
**Advantages of K-Fold Cross-Validation:**
- Reduces the dependency on a specific train/test split.
- Provides a more reliable estimate of out-of-sample accuracy.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVOYMA5K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQC%2BAR9sslzThxH77Tx8tOR6Zq67zqgv%2BAbfV8Yc7AeW3AIhAI0dXCqfSiyeLnncg78OboBft9PBqs3oefkZPyYBxuy%2FKv8DCGMQABoMNjM3NDIzMTgzODA1IgxonY%2FyfejWG6ckBToq3ANrpvGk%2F53MWs0tmZEvv6htMWZofnwv2%2FSAvnEyFojrQR%2F7%2BeoLoEKYmkpgzEEiJcE4txOwl5BVDg3WzU5C8ZjTQO1Wp7sFeELK7sz4Jt4%2BdQYOOH4Kskc07jrarmUhHlGaimFu9hxZ%2FmmRxmgZnHMOl0zFvXEPa1io6LHev2uGuBnlWgnmFmJYsdzS5A81PwaIYWTbWzm%2B6NyCqDUP0%2F1dYx%2Ft4iiuNUGrSBvdRnp7E6FbkDlL8bRSA8t5sDb4y%2F0McJ2pSzC7%2FFR5CDhNbc5m4fzoHZjm%2BlynnpMOgvnNP0qBGIxuX1hzaxPX6scCY4DQ8nIF1oisk9F9lK0AHrfp1oYWrpa1v6blpeMDbvSRUjHcOf9lgMSg722rseBrPAsjIRYvuLcVtX%2BQZEJxZwIUTQJdouHJYx%2F1nZDP561aGFxIUauf%2Fr0pyiYpw4J0chAaamw49BXEVGtiUa2nps1dgr4eLFiOJaIbcjclv60UD86kV%2BdC3U32pCSE3TwtBf51PhtgN3U5e511IpqS%2F36muz05%2FTRM3ob4ehQIissAnuGyCYV9xawOPnVMSkzCe6WTLBiwNW6bxj1mTk6SD6hhBaozsa5sxGgrA1UMl%2BFsWktdUg%2B%2BxtMUzP2eRTCi%2B5O9BjqkAbKZOescaT92JIBmQcbnAY9iBM0g8%2F0vkBicQRFcLpsZjiYfveWoZ0X6ZoaV42byInBh5YcT34BIZyaZXilm%2FyL8bBAVzwVucOO5joKyuHwdMzHiMq%2BDngRMg7cbMOfL0i0T6Hx0Q1dkOKGyqPlSVK2u36vR9Bq9uhppWtnBJQJIWOCLn%2FgZT%2FCzMB2W5ny%2Bl6sPPaHqnZTev%2BpRdLn9XI0AnyGo&X-Amz-Signature=8fc19213eb19e9e58faf4125c4ce64fbdb22766e0778a4ce8c0275e7b59d34b4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.model_selection import cross_val_score

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Perform K-Fold Cross-Validation
scores = cross_val_score(model, X, y, cv=4, scoring='neg_mean_squared_error')
mse_scores = -scores
print(f'Mean Squared Error for each fold: {mse_scores}')
print(f'Average Mean Squared Error: {mse_scores.mean()}')
```
### **Formula for Mean Squared Error (MSE):**
$$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
 $$
Where $ y_i  $ are the actual values, $ \hat{y}_i  $ are the predicted values, and $ n  $ is the number of observations.
### Summary
- **Train and Test on the Same Dataset:** Simple but prone to overfitting with high training accuracy and low out-of-sample accuracy.
- **Train/Test Split:** Provides better out-of-sample accuracy but can still be affected by dataset dependency.
- **K-Fold Cross-Validation:** Mitigates issues of train/test split by averaging results over multiple splits, offering a more consistent evaluation metric.
___
## Model Evaluation Metrics for Regression
### Introduction
Evaluation metrics are essential for assessing the performance of a regression model. These metrics compare actual values to predicted values, providing insights into areas needing improvement. Several key metrics are used to evaluate regression models, including Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Relative Absolute Error (RAE), Relative Squared Error (RSE), and R-squared ($ R^2 $).
### Error Definition
In regression, the error is the difference between the actual data points and the predicted values from the model. This difference can be measured in various ways.
### Mean Absolute Error (MAE)
Mean Absolute Error is the average of the absolute differences between actual and predicted values. It is easy to understand and represents the average error in the same units as the data.
$$ \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
 $$
#### Code Example
```python
from sklearn.metrics import mean_absolute_error

# Example data
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

# Calculate MAE
mae = mean_absolute_error(y_true, y_pred)
print(f"Mean Absolute Error: {mae}")
```
### Mean Squared Error (MSE)
Mean Squared Error is the average of the squared differences between actual and predicted values. It emphasizes larger errors more than smaller ones due to the squaring term, making it more sensitive to outliers.
$$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \frac{RSS}{n} $$
#### Code Example
```python
from sklearn.metrics import mean_squared_error

# Calculate MSE
mse = mean_squared_error(y_true, y_pred)
print(f"Mean Squared Error: {mse}")
```
### Root Mean Squared Error (RMSE)
Root Mean Squared Error is the square root of the mean squared error. It is popular because it is in the same units as the response variable, making it easier to interpret.
$$ \text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
 $$
#### Code Example
```python
import numpy as np

# Calculate RMSE
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")
```
### Relative Absolute Error (RAE)
Relative Absolute Error (RAE) is a metric expressed as a ratio normalizing the absolute error. It measures the average absolute difference between the actual and predicted values relative to the average absolute difference between the actual values and their mean.
$$ \text{RAE} = \frac{\sum_{i=1}^{n} |y_i - \hat{y}_i|}{\sum_{i=1}^{n} |y_i - \bar{y}|}
 $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
# Calculate RAE
rae = np.sum(np.abs(y_true - y_pred)) / np.sum(np.abs(y_true - np.mean(y_true)))
print(f"Relative Absolute Error: {rae}")
```
### Relative Squared Error (RSE)
Relative Squared Error is similar to RAE but uses squared differences. It is widely adopted for calculating $ R^2 $.
$$ \text{RSE} = \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
# Calculate RSE
rse = np.sum((y_true - y_pred) ** 2) / np.sum((y_true - np.mean(y_true)) ** 2)
print(f"Relative Squared Error: {rse}")
```
### R-squared ($ R^2 $)
R-squared is not an error metric per se (by itself), but it is a popular measure of model accuracy. It indicates how close the data points are to the fitted regression line. A higher $ R^2 $ value indicates a better fit.
$$ R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} = 1 - RSE $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
from sklearn.metrics import r2_score

# Calculate R-squared
r2 = r2_score(y_true, y_pred)
print(f"R-squared: {r2}")
```
### Residual Sum of Squares (RSS)
The Residual Sum of Squares (RSS) is a measure of the discrepancy between the data and an estimation model. It is calculated as the sum of the squared differences between the observed actual outcomes and the outcomes predicted by the model.
$$ \text{RSS} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = MSE * n $$
#### Code Example
```python
# Calculate RSS
rss = np.sum((y_true - y_pred) ** 2)
print(f"Residual Sum of Squares: {rss}")
```
### Summary
Each of these metrics quantifies different aspects of model performance. The choice of metric depends on the specific model, data type, and domain knowledge. Understanding and selecting the appropriate metric is crucial for evaluating and improving regression models.
___
## Multiple Linear Regression
### **Linear Regression Models**
- **Simple Linear Regression**: Utilizes one independent variable to estimate a dependent variable (e.g., predicting CO₂ emissions based on engine size).
- **Multiple Linear Regression**: Involves multiple independent variables to predict a dependent variable (e.g., predicting CO₂ emissions using engine size and the number of cylinders).
### **Applications of Multiple Linear Regression**
8. **Identifying Effect Strength**: Determines how independent variables affect the dependent variable. For instance, assessing how revision time, test anxiety, lecture attendance, and gender influence student exam performance.
9. **Predicting Impact of Changes**: Evaluates how changes in independent variables affect the dependent variable. For example, predicting how a patient's blood pressure changes with variations in body mass index, keeping other factors constant.
### **Model Representation**
- **Equation**: The model can be expressed as $ \hat{y}=θ_0+θ_1x_1+θ_2x_2+…+θ_nx_n $.
- **Vector Form**: In multidimensional space, the model is represented as $ \theta^T x $, where $ θ $ is the vector of parameters and $ x $ is the feature set. The first element of $ x $ is set to one to account for the intercept ($ \theta_0 $).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVOYMA5K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQC%2BAR9sslzThxH77Tx8tOR6Zq67zqgv%2BAbfV8Yc7AeW3AIhAI0dXCqfSiyeLnncg78OboBft9PBqs3oefkZPyYBxuy%2FKv8DCGMQABoMNjM3NDIzMTgzODA1IgxonY%2FyfejWG6ckBToq3ANrpvGk%2F53MWs0tmZEvv6htMWZofnwv2%2FSAvnEyFojrQR%2F7%2BeoLoEKYmkpgzEEiJcE4txOwl5BVDg3WzU5C8ZjTQO1Wp7sFeELK7sz4Jt4%2BdQYOOH4Kskc07jrarmUhHlGaimFu9hxZ%2FmmRxmgZnHMOl0zFvXEPa1io6LHev2uGuBnlWgnmFmJYsdzS5A81PwaIYWTbWzm%2B6NyCqDUP0%2F1dYx%2Ft4iiuNUGrSBvdRnp7E6FbkDlL8bRSA8t5sDb4y%2F0McJ2pSzC7%2FFR5CDhNbc5m4fzoHZjm%2BlynnpMOgvnNP0qBGIxuX1hzaxPX6scCY4DQ8nIF1oisk9F9lK0AHrfp1oYWrpa1v6blpeMDbvSRUjHcOf9lgMSg722rseBrPAsjIRYvuLcVtX%2BQZEJxZwIUTQJdouHJYx%2F1nZDP561aGFxIUauf%2Fr0pyiYpw4J0chAaamw49BXEVGtiUa2nps1dgr4eLFiOJaIbcjclv60UD86kV%2BdC3U32pCSE3TwtBf51PhtgN3U5e511IpqS%2F36muz05%2FTRM3ob4ehQIissAnuGyCYV9xawOPnVMSkzCe6WTLBiwNW6bxj1mTk6SD6hhBaozsa5sxGgrA1UMl%2BFsWktdUg%2B%2BxtMUzP2eRTCi%2B5O9BjqkAbKZOescaT92JIBmQcbnAY9iBM0g8%2F0vkBicQRFcLpsZjiYfveWoZ0X6ZoaV42byInBh5YcT34BIZyaZXilm%2FyL8bBAVzwVucOO5joKyuHwdMzHiMq%2BDngRMg7cbMOfL0i0T6Hx0Q1dkOKGyqPlSVK2u36vR9Bq9uhppWtnBJQJIWOCLn%2FgZT%2FCzMB2W5ny%2Bl6sPPaHqnZTev%2BpRdLn9XI0AnyGo&X-Amz-Signature=7dabfe9870b8b24e790ab012e41512e5ca92563d9581e2516115abc3c0a78fec&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
Here’s an example of implementing Multiple Linear Regression in Python using `scikit-learn`:
```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Example data
X = np.array([[1, 2], [2, 3], [4, 5], [3, 6]])  # Independent variables
y = np.array([2, 3, 5, 7])                      # Dependent variable

# Initialize and fit the model
model = LinearRegression()
model.fit(X, y)

# Coefficients and intercept
print(f'Intercept: {model.intercept_}')
print(f'Coefficients: {model.coef_}')

# Making predictions
predictions = model.predict(X)
print(f'Predictions: {predictions}')
```
### **Error and Optimization**
- **Error Calculation**: The error for a prediction is the difference between the actual and predicted values. For example, if the actual value $  y $ is 196 and the predicted value $ \hat{y} $ is 140, the error is $ 196−140=56 $.
- **Mean Squared Error (MSE)**: The average of the squared errors across all predictions. The objective is to minimize MSE to find the best parameters.
### **Parameter Estimation Methods**
10. **Ordinary Least Squares (OLS)**: Estimates coefficients by minimizing MSE using matrix operations. Suitable for smaller datasets but can be slow for larger ones.
11. **Optimization Algorithms**: Methods like `Gradient Descent` iteratively adjust coefficients to minimize error. Suitable for large datasets. Some Optimization Algorithms:` Gradient Descent, Stochastic Gradient Descent, Newton’s Metho`
#### **Code Example:**
Here's a simple implementation of Gradient Descent for linear regression:
```python
import numpy as np

def gradient_descent(X, y, learning_rate=0.01, iterations=1000):
    m, n = X.shape
    theta = np.zeros(n)
    for _ in range(iterations):
        gradient = X.T @ (X @ theta - y) / m
        theta -= learning_rate * gradient
    return theta

# Example data
X = np.array([[1, 2], [2, 3], [4, 5], [3, 6]])  # Independent variables
y = np.array([2, 3, 5, 7])                      # Dependent variable

# Adding intercept term (column of ones)
X_b = np.c_[np.ones((X.shape[0], 1)), X]

# Apply gradient descent
theta = gradient_descent(X_b, y)
print(f'Optimized coefficients: {theta}')
```
### **Prediction Phase**
- **Using Parameters**: Once parameters are found, predictions are made by plugging input values into the model equation. For instance, with $ \theta_0 = 125 $, $ \theta_1 = 6.2 $, $ \theta_2 = 14 $, and input values, CO₂ emissions for a car can be predicted.
### **Concerns in Multiple Linear Regression**
- **Number of Variables**: Adding too many variables without justification can lead to overfitting, where the model becomes too complex and less generalizable.
- **Variable Types**: Categorical variables can be included by converting them to numerical values (e.g., coding car type as 0 or 1).
- **Linearity**: Ensure a linear relationship between the dependent variable and independent variables (maybe scatterplot). Non-linear relationships may require non-linear regression.
___
