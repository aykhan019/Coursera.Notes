

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y374AUO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCwQiHSJfB3qc%2BS5%2Bw%2B8lxFxnmkaucOAkhZOEDW1bHgAiA6EVaL2JBcgSA%2F0PjJc%2By2NrU2Qn06biY5hqdVRADdziqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAv%2FWcC8SthW7xlxnKtwD4IALRE%2FhXuP%2ByPxxszAPHKDjcigdeiFWddMblwOAevZfL48d%2BWz1DYiJYJ46XXt%2BUB%2FXvl573AgJKZRwGfNTU0nk2dkuXul5XXiI5ga3owThfRUfuwrKhEqEc4hKATnglbU3V0fIDlVzeZYxhYRekhcIAltyrMJhP0desspxz6iMP7pFfiOcM%2FAXjqKAwR6%2BsYwk77EmZzJiyhiWQwXDI6156sYnYUMqFpdgkdtrJg2WC%2FBYHCHHlicd4OHT%2BZPz3VWU080Hlyy5XP6NXNidRcHhfFm1ntnd9XqV0lIT01zQPobWQlzHLalrBN5jAuImxvy7gWGRj9eBr48xmsxYzjBwCaXPbnLpE16V8r1SOCHIy%2BAl5jg6GWbclRcfqcgzr6zLhYoOlxgsCxTjQFVzNb%2BYT6VCUqg9eAmm4NlBf%2Bnx02iMd2aYGQa6XBtb9RcAf6cKBdTv37FdAzxr4f40FBgexncPv9L%2BoLubPqahTydrnlU2V9RxVhaoHNjLnREZ2FnEbdV06TA5g%2BVynZM7w%2FsF6mGFm9oE0edT%2FHvddSJlF7mGa%2FAHcMy8drgjgiyLBAnahlojiQ4yuZLGNh5ie1ABFN4A5EaMpCh9qwAoUkXzYZBHG5pAzPxKPHowq5T6vAY6pgFX3cR1hjKf%2FV1YEBd60JumsCYAhllDx5ax3D51oiX4sqrSPKr8%2Fo1Yqzm0m39BbUj6Z2WQKYFXHNwZv63DiRkoLcoXu4%2Fb%2BYLOGA0GOPqAM%2B%2FEp631tNn8KNAS%2BWhC%2Ft9cvANMkBnfUGsnrt0CKdBONh98BWrw7JXOUnmwd2%2BXwdolBiU50XUk3EBl9yBPQc%2Bh%2BSmB%2BkP7XkgrOykAgRdrlo%2FLy3HY&X-Amz-Signature=1ff96d668ab0fa9f7771db6a84b310b97721ccbb2b4f35db3ae66a59589f3f60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y374AUO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCwQiHSJfB3qc%2BS5%2Bw%2B8lxFxnmkaucOAkhZOEDW1bHgAiA6EVaL2JBcgSA%2F0PjJc%2By2NrU2Qn06biY5hqdVRADdziqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAv%2FWcC8SthW7xlxnKtwD4IALRE%2FhXuP%2ByPxxszAPHKDjcigdeiFWddMblwOAevZfL48d%2BWz1DYiJYJ46XXt%2BUB%2FXvl573AgJKZRwGfNTU0nk2dkuXul5XXiI5ga3owThfRUfuwrKhEqEc4hKATnglbU3V0fIDlVzeZYxhYRekhcIAltyrMJhP0desspxz6iMP7pFfiOcM%2FAXjqKAwR6%2BsYwk77EmZzJiyhiWQwXDI6156sYnYUMqFpdgkdtrJg2WC%2FBYHCHHlicd4OHT%2BZPz3VWU080Hlyy5XP6NXNidRcHhfFm1ntnd9XqV0lIT01zQPobWQlzHLalrBN5jAuImxvy7gWGRj9eBr48xmsxYzjBwCaXPbnLpE16V8r1SOCHIy%2BAl5jg6GWbclRcfqcgzr6zLhYoOlxgsCxTjQFVzNb%2BYT6VCUqg9eAmm4NlBf%2Bnx02iMd2aYGQa6XBtb9RcAf6cKBdTv37FdAzxr4f40FBgexncPv9L%2BoLubPqahTydrnlU2V9RxVhaoHNjLnREZ2FnEbdV06TA5g%2BVynZM7w%2FsF6mGFm9oE0edT%2FHvddSJlF7mGa%2FAHcMy8drgjgiyLBAnahlojiQ4yuZLGNh5ie1ABFN4A5EaMpCh9qwAoUkXzYZBHG5pAzPxKPHowq5T6vAY6pgFX3cR1hjKf%2FV1YEBd60JumsCYAhllDx5ax3D51oiX4sqrSPKr8%2Fo1Yqzm0m39BbUj6Z2WQKYFXHNwZv63DiRkoLcoXu4%2Fb%2BYLOGA0GOPqAM%2B%2FEp631tNn8KNAS%2BWhC%2Ft9cvANMkBnfUGsnrt0CKdBONh98BWrw7JXOUnmwd2%2BXwdolBiU50XUk3EBl9yBPQc%2Bh%2BSmB%2BkP7XkgrOykAgRdrlo%2FLy3HY&X-Amz-Signature=3bb6733c062e7df6f37ab3d0d7dfb80b47888e87dca1f48be3563a42a60dd2ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y374AUO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCwQiHSJfB3qc%2BS5%2Bw%2B8lxFxnmkaucOAkhZOEDW1bHgAiA6EVaL2JBcgSA%2F0PjJc%2By2NrU2Qn06biY5hqdVRADdziqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAv%2FWcC8SthW7xlxnKtwD4IALRE%2FhXuP%2ByPxxszAPHKDjcigdeiFWddMblwOAevZfL48d%2BWz1DYiJYJ46XXt%2BUB%2FXvl573AgJKZRwGfNTU0nk2dkuXul5XXiI5ga3owThfRUfuwrKhEqEc4hKATnglbU3V0fIDlVzeZYxhYRekhcIAltyrMJhP0desspxz6iMP7pFfiOcM%2FAXjqKAwR6%2BsYwk77EmZzJiyhiWQwXDI6156sYnYUMqFpdgkdtrJg2WC%2FBYHCHHlicd4OHT%2BZPz3VWU080Hlyy5XP6NXNidRcHhfFm1ntnd9XqV0lIT01zQPobWQlzHLalrBN5jAuImxvy7gWGRj9eBr48xmsxYzjBwCaXPbnLpE16V8r1SOCHIy%2BAl5jg6GWbclRcfqcgzr6zLhYoOlxgsCxTjQFVzNb%2BYT6VCUqg9eAmm4NlBf%2Bnx02iMd2aYGQa6XBtb9RcAf6cKBdTv37FdAzxr4f40FBgexncPv9L%2BoLubPqahTydrnlU2V9RxVhaoHNjLnREZ2FnEbdV06TA5g%2BVynZM7w%2FsF6mGFm9oE0edT%2FHvddSJlF7mGa%2FAHcMy8drgjgiyLBAnahlojiQ4yuZLGNh5ie1ABFN4A5EaMpCh9qwAoUkXzYZBHG5pAzPxKPHowq5T6vAY6pgFX3cR1hjKf%2FV1YEBd60JumsCYAhllDx5ax3D51oiX4sqrSPKr8%2Fo1Yqzm0m39BbUj6Z2WQKYFXHNwZv63DiRkoLcoXu4%2Fb%2BYLOGA0GOPqAM%2B%2FEp631tNn8KNAS%2BWhC%2Ft9cvANMkBnfUGsnrt0CKdBONh98BWrw7JXOUnmwd2%2BXwdolBiU50XUk3EBl9yBPQc%2Bh%2BSmB%2BkP7XkgrOykAgRdrlo%2FLy3HY&X-Amz-Signature=931c420a7bc345c4717ceacce3586a28b0615da4e1a6d76e172b2ec17c1c27a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y374AUO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCwQiHSJfB3qc%2BS5%2Bw%2B8lxFxnmkaucOAkhZOEDW1bHgAiA6EVaL2JBcgSA%2F0PjJc%2By2NrU2Qn06biY5hqdVRADdziqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAv%2FWcC8SthW7xlxnKtwD4IALRE%2FhXuP%2ByPxxszAPHKDjcigdeiFWddMblwOAevZfL48d%2BWz1DYiJYJ46XXt%2BUB%2FXvl573AgJKZRwGfNTU0nk2dkuXul5XXiI5ga3owThfRUfuwrKhEqEc4hKATnglbU3V0fIDlVzeZYxhYRekhcIAltyrMJhP0desspxz6iMP7pFfiOcM%2FAXjqKAwR6%2BsYwk77EmZzJiyhiWQwXDI6156sYnYUMqFpdgkdtrJg2WC%2FBYHCHHlicd4OHT%2BZPz3VWU080Hlyy5XP6NXNidRcHhfFm1ntnd9XqV0lIT01zQPobWQlzHLalrBN5jAuImxvy7gWGRj9eBr48xmsxYzjBwCaXPbnLpE16V8r1SOCHIy%2BAl5jg6GWbclRcfqcgzr6zLhYoOlxgsCxTjQFVzNb%2BYT6VCUqg9eAmm4NlBf%2Bnx02iMd2aYGQa6XBtb9RcAf6cKBdTv37FdAzxr4f40FBgexncPv9L%2BoLubPqahTydrnlU2V9RxVhaoHNjLnREZ2FnEbdV06TA5g%2BVynZM7w%2FsF6mGFm9oE0edT%2FHvddSJlF7mGa%2FAHcMy8drgjgiyLBAnahlojiQ4yuZLGNh5ie1ABFN4A5EaMpCh9qwAoUkXzYZBHG5pAzPxKPHowq5T6vAY6pgFX3cR1hjKf%2FV1YEBd60JumsCYAhllDx5ax3D51oiX4sqrSPKr8%2Fo1Yqzm0m39BbUj6Z2WQKYFXHNwZv63DiRkoLcoXu4%2Fb%2BYLOGA0GOPqAM%2B%2FEp631tNn8KNAS%2BWhC%2Ft9cvANMkBnfUGsnrt0CKdBONh98BWrw7JXOUnmwd2%2BXwdolBiU50XUk3EBl9yBPQc%2Bh%2BSmB%2BkP7XkgrOykAgRdrlo%2FLy3HY&X-Amz-Signature=4a4721cc9c6f0322ab9b7dbee8e309f9c04cc8226baf7582e3b0106cde0cb0fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y374AUO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCwQiHSJfB3qc%2BS5%2Bw%2B8lxFxnmkaucOAkhZOEDW1bHgAiA6EVaL2JBcgSA%2F0PjJc%2By2NrU2Qn06biY5hqdVRADdziqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAv%2FWcC8SthW7xlxnKtwD4IALRE%2FhXuP%2ByPxxszAPHKDjcigdeiFWddMblwOAevZfL48d%2BWz1DYiJYJ46XXt%2BUB%2FXvl573AgJKZRwGfNTU0nk2dkuXul5XXiI5ga3owThfRUfuwrKhEqEc4hKATnglbU3V0fIDlVzeZYxhYRekhcIAltyrMJhP0desspxz6iMP7pFfiOcM%2FAXjqKAwR6%2BsYwk77EmZzJiyhiWQwXDI6156sYnYUMqFpdgkdtrJg2WC%2FBYHCHHlicd4OHT%2BZPz3VWU080Hlyy5XP6NXNidRcHhfFm1ntnd9XqV0lIT01zQPobWQlzHLalrBN5jAuImxvy7gWGRj9eBr48xmsxYzjBwCaXPbnLpE16V8r1SOCHIy%2BAl5jg6GWbclRcfqcgzr6zLhYoOlxgsCxTjQFVzNb%2BYT6VCUqg9eAmm4NlBf%2Bnx02iMd2aYGQa6XBtb9RcAf6cKBdTv37FdAzxr4f40FBgexncPv9L%2BoLubPqahTydrnlU2V9RxVhaoHNjLnREZ2FnEbdV06TA5g%2BVynZM7w%2FsF6mGFm9oE0edT%2FHvddSJlF7mGa%2FAHcMy8drgjgiyLBAnahlojiQ4yuZLGNh5ie1ABFN4A5EaMpCh9qwAoUkXzYZBHG5pAzPxKPHowq5T6vAY6pgFX3cR1hjKf%2FV1YEBd60JumsCYAhllDx5ax3D51oiX4sqrSPKr8%2Fo1Yqzm0m39BbUj6Z2WQKYFXHNwZv63DiRkoLcoXu4%2Fb%2BYLOGA0GOPqAM%2B%2FEp631tNn8KNAS%2BWhC%2Ft9cvANMkBnfUGsnrt0CKdBONh98BWrw7JXOUnmwd2%2BXwdolBiU50XUk3EBl9yBPQc%2Bh%2BSmB%2BkP7XkgrOykAgRdrlo%2FLy3HY&X-Amz-Signature=3b82044fb3fe1ed6f7af1837c65246ce2c1ce3925f2d66acbace05243fcddba9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y374AUO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCwQiHSJfB3qc%2BS5%2Bw%2B8lxFxnmkaucOAkhZOEDW1bHgAiA6EVaL2JBcgSA%2F0PjJc%2By2NrU2Qn06biY5hqdVRADdziqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAv%2FWcC8SthW7xlxnKtwD4IALRE%2FhXuP%2ByPxxszAPHKDjcigdeiFWddMblwOAevZfL48d%2BWz1DYiJYJ46XXt%2BUB%2FXvl573AgJKZRwGfNTU0nk2dkuXul5XXiI5ga3owThfRUfuwrKhEqEc4hKATnglbU3V0fIDlVzeZYxhYRekhcIAltyrMJhP0desspxz6iMP7pFfiOcM%2FAXjqKAwR6%2BsYwk77EmZzJiyhiWQwXDI6156sYnYUMqFpdgkdtrJg2WC%2FBYHCHHlicd4OHT%2BZPz3VWU080Hlyy5XP6NXNidRcHhfFm1ntnd9XqV0lIT01zQPobWQlzHLalrBN5jAuImxvy7gWGRj9eBr48xmsxYzjBwCaXPbnLpE16V8r1SOCHIy%2BAl5jg6GWbclRcfqcgzr6zLhYoOlxgsCxTjQFVzNb%2BYT6VCUqg9eAmm4NlBf%2Bnx02iMd2aYGQa6XBtb9RcAf6cKBdTv37FdAzxr4f40FBgexncPv9L%2BoLubPqahTydrnlU2V9RxVhaoHNjLnREZ2FnEbdV06TA5g%2BVynZM7w%2FsF6mGFm9oE0edT%2FHvddSJlF7mGa%2FAHcMy8drgjgiyLBAnahlojiQ4yuZLGNh5ie1ABFN4A5EaMpCh9qwAoUkXzYZBHG5pAzPxKPHowq5T6vAY6pgFX3cR1hjKf%2FV1YEBd60JumsCYAhllDx5ax3D51oiX4sqrSPKr8%2Fo1Yqzm0m39BbUj6Z2WQKYFXHNwZv63DiRkoLcoXu4%2Fb%2BYLOGA0GOPqAM%2B%2FEp631tNn8KNAS%2BWhC%2Ft9cvANMkBnfUGsnrt0CKdBONh98BWrw7JXOUnmwd2%2BXwdolBiU50XUk3EBl9yBPQc%2Bh%2BSmB%2BkP7XkgrOykAgRdrlo%2FLy3HY&X-Amz-Signature=2d6bfb6c184a761e05440e5db5795cfbd7c2cfc5f6f2b7d21b02c60561e1b455&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y374AUO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCwQiHSJfB3qc%2BS5%2Bw%2B8lxFxnmkaucOAkhZOEDW1bHgAiA6EVaL2JBcgSA%2F0PjJc%2By2NrU2Qn06biY5hqdVRADdziqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAv%2FWcC8SthW7xlxnKtwD4IALRE%2FhXuP%2ByPxxszAPHKDjcigdeiFWddMblwOAevZfL48d%2BWz1DYiJYJ46XXt%2BUB%2FXvl573AgJKZRwGfNTU0nk2dkuXul5XXiI5ga3owThfRUfuwrKhEqEc4hKATnglbU3V0fIDlVzeZYxhYRekhcIAltyrMJhP0desspxz6iMP7pFfiOcM%2FAXjqKAwR6%2BsYwk77EmZzJiyhiWQwXDI6156sYnYUMqFpdgkdtrJg2WC%2FBYHCHHlicd4OHT%2BZPz3VWU080Hlyy5XP6NXNidRcHhfFm1ntnd9XqV0lIT01zQPobWQlzHLalrBN5jAuImxvy7gWGRj9eBr48xmsxYzjBwCaXPbnLpE16V8r1SOCHIy%2BAl5jg6GWbclRcfqcgzr6zLhYoOlxgsCxTjQFVzNb%2BYT6VCUqg9eAmm4NlBf%2Bnx02iMd2aYGQa6XBtb9RcAf6cKBdTv37FdAzxr4f40FBgexncPv9L%2BoLubPqahTydrnlU2V9RxVhaoHNjLnREZ2FnEbdV06TA5g%2BVynZM7w%2FsF6mGFm9oE0edT%2FHvddSJlF7mGa%2FAHcMy8drgjgiyLBAnahlojiQ4yuZLGNh5ie1ABFN4A5EaMpCh9qwAoUkXzYZBHG5pAzPxKPHowq5T6vAY6pgFX3cR1hjKf%2FV1YEBd60JumsCYAhllDx5ax3D51oiX4sqrSPKr8%2Fo1Yqzm0m39BbUj6Z2WQKYFXHNwZv63DiRkoLcoXu4%2Fb%2BYLOGA0GOPqAM%2B%2FEp631tNn8KNAS%2BWhC%2Ft9cvANMkBnfUGsnrt0CKdBONh98BWrw7JXOUnmwd2%2BXwdolBiU50XUk3EBl9yBPQc%2Bh%2BSmB%2BkP7XkgrOykAgRdrlo%2FLy3HY&X-Amz-Signature=13af0c7810018a29ed384ab3f81362fbbe91e7254a8fc95cecaa9b33ebb8fec4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y374AUO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCwQiHSJfB3qc%2BS5%2Bw%2B8lxFxnmkaucOAkhZOEDW1bHgAiA6EVaL2JBcgSA%2F0PjJc%2By2NrU2Qn06biY5hqdVRADdziqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAv%2FWcC8SthW7xlxnKtwD4IALRE%2FhXuP%2ByPxxszAPHKDjcigdeiFWddMblwOAevZfL48d%2BWz1DYiJYJ46XXt%2BUB%2FXvl573AgJKZRwGfNTU0nk2dkuXul5XXiI5ga3owThfRUfuwrKhEqEc4hKATnglbU3V0fIDlVzeZYxhYRekhcIAltyrMJhP0desspxz6iMP7pFfiOcM%2FAXjqKAwR6%2BsYwk77EmZzJiyhiWQwXDI6156sYnYUMqFpdgkdtrJg2WC%2FBYHCHHlicd4OHT%2BZPz3VWU080Hlyy5XP6NXNidRcHhfFm1ntnd9XqV0lIT01zQPobWQlzHLalrBN5jAuImxvy7gWGRj9eBr48xmsxYzjBwCaXPbnLpE16V8r1SOCHIy%2BAl5jg6GWbclRcfqcgzr6zLhYoOlxgsCxTjQFVzNb%2BYT6VCUqg9eAmm4NlBf%2Bnx02iMd2aYGQa6XBtb9RcAf6cKBdTv37FdAzxr4f40FBgexncPv9L%2BoLubPqahTydrnlU2V9RxVhaoHNjLnREZ2FnEbdV06TA5g%2BVynZM7w%2FsF6mGFm9oE0edT%2FHvddSJlF7mGa%2FAHcMy8drgjgiyLBAnahlojiQ4yuZLGNh5ie1ABFN4A5EaMpCh9qwAoUkXzYZBHG5pAzPxKPHowq5T6vAY6pgFX3cR1hjKf%2FV1YEBd60JumsCYAhllDx5ax3D51oiX4sqrSPKr8%2Fo1Yqzm0m39BbUj6Z2WQKYFXHNwZv63DiRkoLcoXu4%2Fb%2BYLOGA0GOPqAM%2B%2FEp631tNn8KNAS%2BWhC%2Ft9cvANMkBnfUGsnrt0CKdBONh98BWrw7JXOUnmwd2%2BXwdolBiU50XUk3EBl9yBPQc%2Bh%2BSmB%2BkP7XkgrOykAgRdrlo%2FLy3HY&X-Amz-Signature=b5a2e601e9188bbd085eceabbd1e1e0c32e025e81f078fbddaab6dc6f1a043eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LWQXFLQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGS07mdXy5JQKfRSUV%2BOQv1w2CL5sc5JRSoafa4AxrKQIgc1MsAL%2FXsNNZBcvlNOyClQ3t7it%2BuB1jBtG02dUVkLoqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEygp%2FCkmadoPPDO0yrcA0tJ1GZxb7rsRujnvOIIRc9lNIe3ZbVn9kuX%2BacdEAIqz09PVx9vXW56oiQS6pBlGCQKrvKlHmMrf091mNtz%2Bcpk6n2N%2FT7MfeCrLqdHBx3Mwscaffz5Ea83rGViN8Zo8HU03yHxe7IOyTmT9wiBd353%2FkkTYPj4IrzvaBwF7f3JA5l%2FqnUOywFT%2BpT33dS1zbKzJjslz7jUpUpaxMGa4TKfjT3EfmZMuBMC4xiVr4iCXGkEKTdjOwx2snTamHO9LFBHOiem8yxw9PiAuTVngfESG2D90ZqSHNKq25Z0xHPHvwq5oc7D6agzqTLkWUUIcGOkgKjqLaq7WKfnD2vmQ2EpUyjxODLn5yaPSiPhFXl9CO4eiESCJOCkUYePkSojFSmwxu9NGpR9kzh4OfqyNe2W1ToFSDp0i3rIM5CdCDy3mVxp50GVwgBN%2BDXZEwNgWDbBrUkUKYkHDLaNgF%2BEHh6gOwcI7P9BuQKY3i0N%2FhoqTxUiuKP0kVN0yg6GvzfVf9lwGcvCJda1vxxJH%2FareKYdcF%2B1hVDZ0Z7rAmzRC89Zf1fhGNdT9KiQ8EbLPqLT3K%2Bw925PzDw3FI6DgQj%2FqwiXsAVv1Nao9cFCw1QJ8bX5AxBtk5U6UhCz%2B3s0MJ2U%2BrwGOqUB34uEUka3GKYMFLSZliX%2FhSr5Nn7pbEyW1a4RfQQpk4lSUWb24Je8V7572kCSRHV2c9%2FTwcDN2rcK3YpaP20uH7KygqhpRDRRpe5APl5RblqlrvlP6HVkYlmwrsYeEIyGFY00Rd6ojiTJB7hT94hWeE47qDmVPQboXGUVmPBRUovMKTIkRwSOpqN8sqEnYZoCln85%2BsxNa4e94yJMrTA5Tgn0H7tV&X-Amz-Signature=60a06c29d98f538ea01a9c6414105db1f1f1bd9a92ed309ff8ae3041b06d6880&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PDQLIDO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFS000n06uVzPIN7O8TGzPkQ6pRhXguP7%2Btp6txaSHgHAiEAjp1HE6l3D5Rnks4pYlInNZQDfVF3Q%2BwQBGFx8e1OqroqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJa1VJLih56j9xZirircA97F1nDFx7SILcgpB%2FgqMgHBgiNhKeN0C08w2t3P1Afhc%2ByoL9AxzWOqD8CKl5l8PFECLaFCaxlihk98bttXnRAuZqZOoRZKcnAlK%2BHz3gtHqsSahP5iW7zHiFvy161eh1B2U%2FC51EKxJ95bHcKaRgh9B6WsQh4C%2BJsBkcXH3CbqFUn2qUFoCun9YnlJUccHHi%2FAEUqV6vdIAk%2BqGt7qLzrqmL1ew5nvtOxhmUw0wQ%2FlaFsLGY%2BZa0w4puKrAv6HGzdSwEjkO2CpAmBCiYqcUdt8mOP%2FBN2a4Pt2aScEQqSHzmzl4DMQpTnQ7P2axDfwZMiDlaFJZHR5YTsBfLEaGNZR1nJTULqRPh2UYVjvT98eZvtxsFpOJjkGKbEjw6WiS7bwSN7o9TIXJ7n1pAApBqi2ClWZwaudXOTySpSkH0jwbYIq5xfMQG85LgdmMW0zGEWbLhLzEitd6SoWr2vfhjOEpk3OpGoWVdP8BhGGqUVVeP60qKkPvYaaDE2oz7Ugchoy5MbM0XJlsg%2BApjAXZdSyffLIhIZgqjtQqT5juvw0HNzfr4osnhuv342Ox%2FEQi3pQF2sVbUHq2LjZdNfAZ4oGwCa4q1v05ytYI%2FWGyreJjYBDnjjsCl0dml6FMJOU%2BrwGOqUBenVXVhP0Q9zUo1xRiyBnzM%2Fu1yOWJv40doPhM5EbX181Wn%2BuLX3QJsB%2FuyB3t0dQGMMGqwpeuCpFTeGo%2FYaZwv9t3jqUGaoyL99XZR9M5KizbnzyKV4uaCCraaiMQ2AUmJ0h82xYPevao%2BQ13pqFazQ8%2BoXqNIftg7ieVcniTgFPUKCv6JDws%2BED8PnMbQnsZsge3j%2F3FOcv0kv39f8z3041qXXo&X-Amz-Signature=37865b0031497cef1a4670cade1e77d0fba89d560c724cb4009f394dfbee3aef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ4W5MBA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEgYXPqGukyDaFy8MxaKjwZXuAhoBrK6jOP8enfqRkvkAiAX5vHFRugvBGpayfp0qCE0Q53oJG2siGiwfsBwbV9CNCqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlif5KjkZf3EEziJNKtwDY56MWce3EgkG4CWsbMRf2tlVxud%2Fm5wMVpENhChxDoLt5tG5%2BBbmyttSx1CAPUfd18QOh1n4OymoMg%2FJSF%2FcVKI8xdwA7UKw%2B%2Brbv9ZLGGz4nZ4HOJsThPomgI%2FCOTb8Ne94VMK4kQz%2B6l3suZFjHK0%2FR%2FvrYOQL2PzmxG%2BMPamZ8LcVL%2Fkpu5rFBxG6%2BO%2FGsIhARxviXMZQdPlQdQ0SqqTm3KZAkVW3ZVmaPsZLGuNhYGDhFhYJr%2BzfHaIV0rO4Z394VgZqYfo17xl%2Fgyea4lzl5UuhuwloYASSsvV%2BwP8NdO5lFVzUepVgH8wDHmBV7xNtp9LMOEH9xyVToHmiKaQRDxC88Ok7PHrOsukmClX6eSWtK4bbDGa39fbaNd%2B87q%2FgJQG3WPZp4OpcE8M3u9xjjfVrSjaQ3KqdzLVcxVNFBdJ0h%2Fz0jQAlGpCDlBimekoxVoF6626d%2Fu1ZbQPBTMVtCeO%2BdWWF%2FcYbq%2B%2FjGGndVV0zeSQAriHC%2FXsjXgQ0hz0XWZEifnobkYTxUze8GQk1GeZydBSbWHBpHtfpJryrT7l1gIIUw%2Fo3nAM%2Bjrcs2pwv4Lg2OWqBOIUwpZTa5v4rSLBqhITFtmpkIzpcBva%2BvyadrHl5KiJKe9swnZT6vAY6pgEVjCyDvZj1ieJLqsE6YC79r4VomdofBn%2B0%2Fihr6kgKzO7sqB2tcXPQZmLA8ys7DCG95MRGfQFF1a%2ByCQ4KT3Ez4cO6q3mRgTYDVrKYA1JvqwEm2oA5p9MxnDFCzhCN7Fw%2BulPPTjAfFMF0%2BNTLHwPQ%2FgPx1l70d%2FyIKNfDQViW5%2F9Ewu1WpeqDW6LEVuu%2FQTXUS982yvLTUaf45jds2ZGxh%2Bz5X2Q0&X-Amz-Signature=c3ceaec0bdb2cb506905ca6ad50c76a505795af0917f5a7e9b52fd40b5834028&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ4W5MBA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEgYXPqGukyDaFy8MxaKjwZXuAhoBrK6jOP8enfqRkvkAiAX5vHFRugvBGpayfp0qCE0Q53oJG2siGiwfsBwbV9CNCqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlif5KjkZf3EEziJNKtwDY56MWce3EgkG4CWsbMRf2tlVxud%2Fm5wMVpENhChxDoLt5tG5%2BBbmyttSx1CAPUfd18QOh1n4OymoMg%2FJSF%2FcVKI8xdwA7UKw%2B%2Brbv9ZLGGz4nZ4HOJsThPomgI%2FCOTb8Ne94VMK4kQz%2B6l3suZFjHK0%2FR%2FvrYOQL2PzmxG%2BMPamZ8LcVL%2Fkpu5rFBxG6%2BO%2FGsIhARxviXMZQdPlQdQ0SqqTm3KZAkVW3ZVmaPsZLGuNhYGDhFhYJr%2BzfHaIV0rO4Z394VgZqYfo17xl%2Fgyea4lzl5UuhuwloYASSsvV%2BwP8NdO5lFVzUepVgH8wDHmBV7xNtp9LMOEH9xyVToHmiKaQRDxC88Ok7PHrOsukmClX6eSWtK4bbDGa39fbaNd%2B87q%2FgJQG3WPZp4OpcE8M3u9xjjfVrSjaQ3KqdzLVcxVNFBdJ0h%2Fz0jQAlGpCDlBimekoxVoF6626d%2Fu1ZbQPBTMVtCeO%2BdWWF%2FcYbq%2B%2FjGGndVV0zeSQAriHC%2FXsjXgQ0hz0XWZEifnobkYTxUze8GQk1GeZydBSbWHBpHtfpJryrT7l1gIIUw%2Fo3nAM%2Bjrcs2pwv4Lg2OWqBOIUwpZTa5v4rSLBqhITFtmpkIzpcBva%2BvyadrHl5KiJKe9swnZT6vAY6pgEVjCyDvZj1ieJLqsE6YC79r4VomdofBn%2B0%2Fihr6kgKzO7sqB2tcXPQZmLA8ys7DCG95MRGfQFF1a%2ByCQ4KT3Ez4cO6q3mRgTYDVrKYA1JvqwEm2oA5p9MxnDFCzhCN7Fw%2BulPPTjAfFMF0%2BNTLHwPQ%2FgPx1l70d%2FyIKNfDQViW5%2F9Ewu1WpeqDW6LEVuu%2FQTXUS982yvLTUaf45jds2ZGxh%2Bz5X2Q0&X-Amz-Signature=9b6dc1f9f70f912f8d06f254165f145a20ab39577b589d1adb267c1c91d56e77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
