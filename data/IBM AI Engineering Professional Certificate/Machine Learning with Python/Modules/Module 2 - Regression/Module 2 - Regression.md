

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GM37OZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCpZCobLd1ccc3ODJDBMyiuRqobjtiXEIhKcboSmtFmswIgLKf%2FBMhXtaJLOjQ95OmPqRB1QI%2FSMEIKTSo12WtAVt4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDP%2FRvpvA6LXv8%2Bbh8CrcA49x%2BOAC8xPgAqyhrK8xB5dnzADHUueqYx%2B18AW5agTJuXvVlBGCoyn9QrwqCQqy6laC2tTZaKx9FwSAIloW7QAatDdDux9GDkGQUQ4D7k0CjGRLuG2VYid9lq38M5X4yrijLUSJrYt0aPPWZwW%2F3yAWviM%2BqUqcALHP8qy85YGy%2BOw8VbbrKEda1qxRxoltwIi%2FNcoqYbb6q4iw97yEGR2mvaslnsY%2FKG3F%2FevDOlkUBg%2BLfTbSQJB4ad1oKGIyObcWR0HkZM6xxpMhii4H05HTphz%2BHRivp4pjkz%2B4MZ%2FORdxS5%2FTZzenRjg74B7RLBUlobR%2FJR4V4LsTzarfRP44%2Fv1zvifJ5KtK5yIkQaHl6OUS8hfDnlBWSpaFz7FRJwGv40WgqhR%2F%2FnERB0hqBd%2FNLZj4WdIlelURxhuxK67IoQvAmvhOnb5Zl7cvD7jSciPpb%2FITqHgLLsmpzz89JjzTlIF38P4OEiz9DfA8EfAqXoLUGteHp%2FeOnrdudgJLgolbB31VPo7x1UXnPd%2FqYr4OMLjpqLLO29WfyAlZsGl1ghorxMttVft6%2FrqO41JqGpDL1U1JMev145vPXc3%2BQ7Qsdcq%2F%2FhlXpizRkLc%2BnTIQijnmXGkNb2Bo%2BbuJFMLjRkb0GOqUBftD0ggjMJ5t17d18B46CiTTrNoaNR%2BheAcmx%2FCtxp%2Fb1DFDOQA%2BZUu1uN4Hnmghz3gqbnhU0rCbKPbd%2FmxhWtDdd%2BJ5JO%2BcAFQC%2BlUQN%2Bq0siWiMR6eLXEzoumRG7cwlFahcBRo9nVyM1KxmsiaW4TseQFAw3Md7K1PkR5kYH7dnZfxMbP51RBrgHeuiDYPB2bOHR%2Fojape%2FU8Vm2EVkELhLoOzh&X-Amz-Signature=edc1e0bc945b8ba1ae9f1ca125810f09a458754ec9ac647f8abed066cbf160b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GM37OZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCpZCobLd1ccc3ODJDBMyiuRqobjtiXEIhKcboSmtFmswIgLKf%2FBMhXtaJLOjQ95OmPqRB1QI%2FSMEIKTSo12WtAVt4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDP%2FRvpvA6LXv8%2Bbh8CrcA49x%2BOAC8xPgAqyhrK8xB5dnzADHUueqYx%2B18AW5agTJuXvVlBGCoyn9QrwqCQqy6laC2tTZaKx9FwSAIloW7QAatDdDux9GDkGQUQ4D7k0CjGRLuG2VYid9lq38M5X4yrijLUSJrYt0aPPWZwW%2F3yAWviM%2BqUqcALHP8qy85YGy%2BOw8VbbrKEda1qxRxoltwIi%2FNcoqYbb6q4iw97yEGR2mvaslnsY%2FKG3F%2FevDOlkUBg%2BLfTbSQJB4ad1oKGIyObcWR0HkZM6xxpMhii4H05HTphz%2BHRivp4pjkz%2B4MZ%2FORdxS5%2FTZzenRjg74B7RLBUlobR%2FJR4V4LsTzarfRP44%2Fv1zvifJ5KtK5yIkQaHl6OUS8hfDnlBWSpaFz7FRJwGv40WgqhR%2F%2FnERB0hqBd%2FNLZj4WdIlelURxhuxK67IoQvAmvhOnb5Zl7cvD7jSciPpb%2FITqHgLLsmpzz89JjzTlIF38P4OEiz9DfA8EfAqXoLUGteHp%2FeOnrdudgJLgolbB31VPo7x1UXnPd%2FqYr4OMLjpqLLO29WfyAlZsGl1ghorxMttVft6%2FrqO41JqGpDL1U1JMev145vPXc3%2BQ7Qsdcq%2F%2FhlXpizRkLc%2BnTIQijnmXGkNb2Bo%2BbuJFMLjRkb0GOqUBftD0ggjMJ5t17d18B46CiTTrNoaNR%2BheAcmx%2FCtxp%2Fb1DFDOQA%2BZUu1uN4Hnmghz3gqbnhU0rCbKPbd%2FmxhWtDdd%2BJ5JO%2BcAFQC%2BlUQN%2Bq0siWiMR6eLXEzoumRG7cwlFahcBRo9nVyM1KxmsiaW4TseQFAw3Md7K1PkR5kYH7dnZfxMbP51RBrgHeuiDYPB2bOHR%2Fojape%2FU8Vm2EVkELhLoOzh&X-Amz-Signature=9de6fc4959a063d725aab9ebcc2eedd1ec65c3bf13244cfd3d3078d50f9e9239&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GM37OZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCpZCobLd1ccc3ODJDBMyiuRqobjtiXEIhKcboSmtFmswIgLKf%2FBMhXtaJLOjQ95OmPqRB1QI%2FSMEIKTSo12WtAVt4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDP%2FRvpvA6LXv8%2Bbh8CrcA49x%2BOAC8xPgAqyhrK8xB5dnzADHUueqYx%2B18AW5agTJuXvVlBGCoyn9QrwqCQqy6laC2tTZaKx9FwSAIloW7QAatDdDux9GDkGQUQ4D7k0CjGRLuG2VYid9lq38M5X4yrijLUSJrYt0aPPWZwW%2F3yAWviM%2BqUqcALHP8qy85YGy%2BOw8VbbrKEda1qxRxoltwIi%2FNcoqYbb6q4iw97yEGR2mvaslnsY%2FKG3F%2FevDOlkUBg%2BLfTbSQJB4ad1oKGIyObcWR0HkZM6xxpMhii4H05HTphz%2BHRivp4pjkz%2B4MZ%2FORdxS5%2FTZzenRjg74B7RLBUlobR%2FJR4V4LsTzarfRP44%2Fv1zvifJ5KtK5yIkQaHl6OUS8hfDnlBWSpaFz7FRJwGv40WgqhR%2F%2FnERB0hqBd%2FNLZj4WdIlelURxhuxK67IoQvAmvhOnb5Zl7cvD7jSciPpb%2FITqHgLLsmpzz89JjzTlIF38P4OEiz9DfA8EfAqXoLUGteHp%2FeOnrdudgJLgolbB31VPo7x1UXnPd%2FqYr4OMLjpqLLO29WfyAlZsGl1ghorxMttVft6%2FrqO41JqGpDL1U1JMev145vPXc3%2BQ7Qsdcq%2F%2FhlXpizRkLc%2BnTIQijnmXGkNb2Bo%2BbuJFMLjRkb0GOqUBftD0ggjMJ5t17d18B46CiTTrNoaNR%2BheAcmx%2FCtxp%2Fb1DFDOQA%2BZUu1uN4Hnmghz3gqbnhU0rCbKPbd%2FmxhWtDdd%2BJ5JO%2BcAFQC%2BlUQN%2Bq0siWiMR6eLXEzoumRG7cwlFahcBRo9nVyM1KxmsiaW4TseQFAw3Md7K1PkR5kYH7dnZfxMbP51RBrgHeuiDYPB2bOHR%2Fojape%2FU8Vm2EVkELhLoOzh&X-Amz-Signature=b6fb5b5fb525363a3895d0098d844dda30cf8e57111e3cd362976344b48fd339&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GM37OZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCpZCobLd1ccc3ODJDBMyiuRqobjtiXEIhKcboSmtFmswIgLKf%2FBMhXtaJLOjQ95OmPqRB1QI%2FSMEIKTSo12WtAVt4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDP%2FRvpvA6LXv8%2Bbh8CrcA49x%2BOAC8xPgAqyhrK8xB5dnzADHUueqYx%2B18AW5agTJuXvVlBGCoyn9QrwqCQqy6laC2tTZaKx9FwSAIloW7QAatDdDux9GDkGQUQ4D7k0CjGRLuG2VYid9lq38M5X4yrijLUSJrYt0aPPWZwW%2F3yAWviM%2BqUqcALHP8qy85YGy%2BOw8VbbrKEda1qxRxoltwIi%2FNcoqYbb6q4iw97yEGR2mvaslnsY%2FKG3F%2FevDOlkUBg%2BLfTbSQJB4ad1oKGIyObcWR0HkZM6xxpMhii4H05HTphz%2BHRivp4pjkz%2B4MZ%2FORdxS5%2FTZzenRjg74B7RLBUlobR%2FJR4V4LsTzarfRP44%2Fv1zvifJ5KtK5yIkQaHl6OUS8hfDnlBWSpaFz7FRJwGv40WgqhR%2F%2FnERB0hqBd%2FNLZj4WdIlelURxhuxK67IoQvAmvhOnb5Zl7cvD7jSciPpb%2FITqHgLLsmpzz89JjzTlIF38P4OEiz9DfA8EfAqXoLUGteHp%2FeOnrdudgJLgolbB31VPo7x1UXnPd%2FqYr4OMLjpqLLO29WfyAlZsGl1ghorxMttVft6%2FrqO41JqGpDL1U1JMev145vPXc3%2BQ7Qsdcq%2F%2FhlXpizRkLc%2BnTIQijnmXGkNb2Bo%2BbuJFMLjRkb0GOqUBftD0ggjMJ5t17d18B46CiTTrNoaNR%2BheAcmx%2FCtxp%2Fb1DFDOQA%2BZUu1uN4Hnmghz3gqbnhU0rCbKPbd%2FmxhWtDdd%2BJ5JO%2BcAFQC%2BlUQN%2Bq0siWiMR6eLXEzoumRG7cwlFahcBRo9nVyM1KxmsiaW4TseQFAw3Md7K1PkR5kYH7dnZfxMbP51RBrgHeuiDYPB2bOHR%2Fojape%2FU8Vm2EVkELhLoOzh&X-Amz-Signature=75569270379fbd4670814bd480cc436b09019d069640be781e117fcf51b1f392&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GM37OZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCpZCobLd1ccc3ODJDBMyiuRqobjtiXEIhKcboSmtFmswIgLKf%2FBMhXtaJLOjQ95OmPqRB1QI%2FSMEIKTSo12WtAVt4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDP%2FRvpvA6LXv8%2Bbh8CrcA49x%2BOAC8xPgAqyhrK8xB5dnzADHUueqYx%2B18AW5agTJuXvVlBGCoyn9QrwqCQqy6laC2tTZaKx9FwSAIloW7QAatDdDux9GDkGQUQ4D7k0CjGRLuG2VYid9lq38M5X4yrijLUSJrYt0aPPWZwW%2F3yAWviM%2BqUqcALHP8qy85YGy%2BOw8VbbrKEda1qxRxoltwIi%2FNcoqYbb6q4iw97yEGR2mvaslnsY%2FKG3F%2FevDOlkUBg%2BLfTbSQJB4ad1oKGIyObcWR0HkZM6xxpMhii4H05HTphz%2BHRivp4pjkz%2B4MZ%2FORdxS5%2FTZzenRjg74B7RLBUlobR%2FJR4V4LsTzarfRP44%2Fv1zvifJ5KtK5yIkQaHl6OUS8hfDnlBWSpaFz7FRJwGv40WgqhR%2F%2FnERB0hqBd%2FNLZj4WdIlelURxhuxK67IoQvAmvhOnb5Zl7cvD7jSciPpb%2FITqHgLLsmpzz89JjzTlIF38P4OEiz9DfA8EfAqXoLUGteHp%2FeOnrdudgJLgolbB31VPo7x1UXnPd%2FqYr4OMLjpqLLO29WfyAlZsGl1ghorxMttVft6%2FrqO41JqGpDL1U1JMev145vPXc3%2BQ7Qsdcq%2F%2FhlXpizRkLc%2BnTIQijnmXGkNb2Bo%2BbuJFMLjRkb0GOqUBftD0ggjMJ5t17d18B46CiTTrNoaNR%2BheAcmx%2FCtxp%2Fb1DFDOQA%2BZUu1uN4Hnmghz3gqbnhU0rCbKPbd%2FmxhWtDdd%2BJ5JO%2BcAFQC%2BlUQN%2Bq0siWiMR6eLXEzoumRG7cwlFahcBRo9nVyM1KxmsiaW4TseQFAw3Md7K1PkR5kYH7dnZfxMbP51RBrgHeuiDYPB2bOHR%2Fojape%2FU8Vm2EVkELhLoOzh&X-Amz-Signature=3c05b21395731d2368d38f20e5fe7409f8ba024fdd8283f018ae694284d6b4cc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GM37OZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCpZCobLd1ccc3ODJDBMyiuRqobjtiXEIhKcboSmtFmswIgLKf%2FBMhXtaJLOjQ95OmPqRB1QI%2FSMEIKTSo12WtAVt4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDP%2FRvpvA6LXv8%2Bbh8CrcA49x%2BOAC8xPgAqyhrK8xB5dnzADHUueqYx%2B18AW5agTJuXvVlBGCoyn9QrwqCQqy6laC2tTZaKx9FwSAIloW7QAatDdDux9GDkGQUQ4D7k0CjGRLuG2VYid9lq38M5X4yrijLUSJrYt0aPPWZwW%2F3yAWviM%2BqUqcALHP8qy85YGy%2BOw8VbbrKEda1qxRxoltwIi%2FNcoqYbb6q4iw97yEGR2mvaslnsY%2FKG3F%2FevDOlkUBg%2BLfTbSQJB4ad1oKGIyObcWR0HkZM6xxpMhii4H05HTphz%2BHRivp4pjkz%2B4MZ%2FORdxS5%2FTZzenRjg74B7RLBUlobR%2FJR4V4LsTzarfRP44%2Fv1zvifJ5KtK5yIkQaHl6OUS8hfDnlBWSpaFz7FRJwGv40WgqhR%2F%2FnERB0hqBd%2FNLZj4WdIlelURxhuxK67IoQvAmvhOnb5Zl7cvD7jSciPpb%2FITqHgLLsmpzz89JjzTlIF38P4OEiz9DfA8EfAqXoLUGteHp%2FeOnrdudgJLgolbB31VPo7x1UXnPd%2FqYr4OMLjpqLLO29WfyAlZsGl1ghorxMttVft6%2FrqO41JqGpDL1U1JMev145vPXc3%2BQ7Qsdcq%2F%2FhlXpizRkLc%2BnTIQijnmXGkNb2Bo%2BbuJFMLjRkb0GOqUBftD0ggjMJ5t17d18B46CiTTrNoaNR%2BheAcmx%2FCtxp%2Fb1DFDOQA%2BZUu1uN4Hnmghz3gqbnhU0rCbKPbd%2FmxhWtDdd%2BJ5JO%2BcAFQC%2BlUQN%2Bq0siWiMR6eLXEzoumRG7cwlFahcBRo9nVyM1KxmsiaW4TseQFAw3Md7K1PkR5kYH7dnZfxMbP51RBrgHeuiDYPB2bOHR%2Fojape%2FU8Vm2EVkELhLoOzh&X-Amz-Signature=bd8f48d9fba520cac3ce78a1e9ee5fa535cc9b3e0ab439e2e12e794ffb936aeb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GM37OZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCpZCobLd1ccc3ODJDBMyiuRqobjtiXEIhKcboSmtFmswIgLKf%2FBMhXtaJLOjQ95OmPqRB1QI%2FSMEIKTSo12WtAVt4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDP%2FRvpvA6LXv8%2Bbh8CrcA49x%2BOAC8xPgAqyhrK8xB5dnzADHUueqYx%2B18AW5agTJuXvVlBGCoyn9QrwqCQqy6laC2tTZaKx9FwSAIloW7QAatDdDux9GDkGQUQ4D7k0CjGRLuG2VYid9lq38M5X4yrijLUSJrYt0aPPWZwW%2F3yAWviM%2BqUqcALHP8qy85YGy%2BOw8VbbrKEda1qxRxoltwIi%2FNcoqYbb6q4iw97yEGR2mvaslnsY%2FKG3F%2FevDOlkUBg%2BLfTbSQJB4ad1oKGIyObcWR0HkZM6xxpMhii4H05HTphz%2BHRivp4pjkz%2B4MZ%2FORdxS5%2FTZzenRjg74B7RLBUlobR%2FJR4V4LsTzarfRP44%2Fv1zvifJ5KtK5yIkQaHl6OUS8hfDnlBWSpaFz7FRJwGv40WgqhR%2F%2FnERB0hqBd%2FNLZj4WdIlelURxhuxK67IoQvAmvhOnb5Zl7cvD7jSciPpb%2FITqHgLLsmpzz89JjzTlIF38P4OEiz9DfA8EfAqXoLUGteHp%2FeOnrdudgJLgolbB31VPo7x1UXnPd%2FqYr4OMLjpqLLO29WfyAlZsGl1ghorxMttVft6%2FrqO41JqGpDL1U1JMev145vPXc3%2BQ7Qsdcq%2F%2FhlXpizRkLc%2BnTIQijnmXGkNb2Bo%2BbuJFMLjRkb0GOqUBftD0ggjMJ5t17d18B46CiTTrNoaNR%2BheAcmx%2FCtxp%2Fb1DFDOQA%2BZUu1uN4Hnmghz3gqbnhU0rCbKPbd%2FmxhWtDdd%2BJ5JO%2BcAFQC%2BlUQN%2Bq0siWiMR6eLXEzoumRG7cwlFahcBRo9nVyM1KxmsiaW4TseQFAw3Md7K1PkR5kYH7dnZfxMbP51RBrgHeuiDYPB2bOHR%2Fojape%2FU8Vm2EVkELhLoOzh&X-Amz-Signature=a1b33ab13c4f8dec0aff910b1bf04a9779fce675335ed67cb12fc6e2a239b6ba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GM37OZK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCpZCobLd1ccc3ODJDBMyiuRqobjtiXEIhKcboSmtFmswIgLKf%2FBMhXtaJLOjQ95OmPqRB1QI%2FSMEIKTSo12WtAVt4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDP%2FRvpvA6LXv8%2Bbh8CrcA49x%2BOAC8xPgAqyhrK8xB5dnzADHUueqYx%2B18AW5agTJuXvVlBGCoyn9QrwqCQqy6laC2tTZaKx9FwSAIloW7QAatDdDux9GDkGQUQ4D7k0CjGRLuG2VYid9lq38M5X4yrijLUSJrYt0aPPWZwW%2F3yAWviM%2BqUqcALHP8qy85YGy%2BOw8VbbrKEda1qxRxoltwIi%2FNcoqYbb6q4iw97yEGR2mvaslnsY%2FKG3F%2FevDOlkUBg%2BLfTbSQJB4ad1oKGIyObcWR0HkZM6xxpMhii4H05HTphz%2BHRivp4pjkz%2B4MZ%2FORdxS5%2FTZzenRjg74B7RLBUlobR%2FJR4V4LsTzarfRP44%2Fv1zvifJ5KtK5yIkQaHl6OUS8hfDnlBWSpaFz7FRJwGv40WgqhR%2F%2FnERB0hqBd%2FNLZj4WdIlelURxhuxK67IoQvAmvhOnb5Zl7cvD7jSciPpb%2FITqHgLLsmpzz89JjzTlIF38P4OEiz9DfA8EfAqXoLUGteHp%2FeOnrdudgJLgolbB31VPo7x1UXnPd%2FqYr4OMLjpqLLO29WfyAlZsGl1ghorxMttVft6%2FrqO41JqGpDL1U1JMev145vPXc3%2BQ7Qsdcq%2F%2FhlXpizRkLc%2BnTIQijnmXGkNb2Bo%2BbuJFMLjRkb0GOqUBftD0ggjMJ5t17d18B46CiTTrNoaNR%2BheAcmx%2FCtxp%2Fb1DFDOQA%2BZUu1uN4Hnmghz3gqbnhU0rCbKPbd%2FmxhWtDdd%2BJ5JO%2BcAFQC%2BlUQN%2Bq0siWiMR6eLXEzoumRG7cwlFahcBRo9nVyM1KxmsiaW4TseQFAw3Md7K1PkR5kYH7dnZfxMbP51RBrgHeuiDYPB2bOHR%2Fojape%2FU8Vm2EVkELhLoOzh&X-Amz-Signature=cd0ad6e89ce108b6b2c6bb90e63bcfb1521fecdf276bccc928c5ad2d565532ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YSU3ONA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIEcEl1Dn4JTzilxUGvYhOLWC65%2F69KREXdIknIThU%2B7qAiA5MaFBd1CAYEDDGX7P%2FsW0WytbG2SMoacryovd%2BPhGSir%2FAwhZEAAaDDYzNzQyMzE4MzgwNSIMEmwdgggAyGjp1ovyKtwD4esgGwZqSZxVQUyL08xmAz3ipjyqPm8nypO2w9XceZutLBOo4Nj7iFjg0EM8s%2FJrQDtVfH%2FIwPNaqTuLkiCOiYMD0T5JuojWLsX9oTRPtnqM7aFJ6zeCT5c5ioBKCVpuZZfK%2BSIRxpjMPrN9%2FXtzXxNUgQUKZvf2TgoifLakgfIs7%2BwiMOLikSsXyeW9yp9f09d%2FDtMl79frQIZXLQ1gjqkFIN5YPViAQ9bNBoxXmVDP8cE6MaX0CHETLUeIIkeEsGpkIB0pvUKzw%2BYh9Ot3QOqqElTaiV%2F7ju38eCjmgfFn%2FdZ6naQRjASn6dNYSz5V1IUWlFEFuUHNJx1bYDyPBR9RpsJZLSzbDw%2BOUV0GPyDd%2Bbri%2FywtSr%2Bhh8auqg5gfVH3y84XJgXFrfeuEnWzCROy%2FC69h3wZ2ZLK%2FbxchtNMDulTtoNQQzGpjeZJkgbGtTzp9EMARooTtmjev4w0vC7PZYfeTr6HWv9lsgtxrOvaMZxEALHqVX2z8j48I4B%2FH2MWNxXN1vAQz2PtyahaBKFU4Tif7tIsl3izKYlL2HV8CBIr9RcJO%2FQd48kaQnAI0aSlESj6dshSTjKwtR1vycdx5H%2BX%2Ff4DVSl6U1SRkO14WOsjXZRtzLnerNEw1NGRvQY6pgH5Oh43iSBrNIa3akxOJpNbc5Pk9sT8P92DViMCFxgTHo2RO2gqZC6KrP4LBVnnwYanMlxgdZZrIvi8Q6XguwkfkPyEAM3Szdslh48iN1w0gZkQxXn5fvxC3x5rTrwM3C9BoSU7rlufRbCYB2%2FQ%2BYRChsj6M5AlZy3%2FI7bDoWS0%2B5lI6GBFxr1wl3IztX6DChg3LoXbdka4bO1wiJcaKTLjpCLcK4s9&X-Amz-Signature=af2810c383173fee4ce34be61c7400aea835be763c48a4620777bbb508fd7167&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SLR325Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDeYkk9l5RZWUzJg6i0ZnXUPVEaqUQyIekvPTGXrxn26AIgHZr0rhKc0dZPTaYhSRRlDZ47XZ%2Bncj7Wg6jf1Y%2Fki4kq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDE6uSo3Juh03huiPZircA4dS%2FfgZ3uxQPwT0jr18uIjA6%2FEwT2wBRoQ0Y%2BKYhykGMN2e4%2FKAhTXWyKJo3Ob2WV9OMtfL%2BZtAgiHHKHRtEAmcBrjZE%2Ff4wYcqvzUDrz%2FpZfk76RtrrJzpZUpWl6CvXTcXHRz3wWQ%2BkPkLlki5IrE0DI97osF23cPU3TqWJfHE2%2Fqq%2BUfQrWc03oGfW62Tv%2FrsvgBXn3H76naKinOZWRNP8YPKazawBq63zr3e2FUnuwhFN4hV%2FMqiUakw0Vda0wv0vPKyL9Ui8%2BpZApSXtEFKGRdQHP8wnfjduzND6iOVl9kLkaL4X1553FX%2F2aCbIe4ZcoO8o85tZ%2FL6fFTOzRvSWYPqNq8IfJctUnDTKdS%2FFBzbha4sBj5GhGZz9yuSvsv41V55jOZeY56cyujxEvt8iVWAJPqdaVSAgdT1jMkqphdEJgi3hrsv8YA1s1IDDXcSPBw5cgxdceDF0nN7rbiS86M4Z71d8IbbotQ%2FCEg%2BE75OG8fVF3tUVpxgM19wPYadjTzu92yLAAl9%2FsHpR31QgL2STy5y0rIp4MEiJUwfcEJnEquXia0QQRZzm0SJHjWt%2FeAReH73%2BysG8w7w1u0Hs5DtOeylX%2BYufJu2aDRRSBJSnnAEGq1%2F1nvIMMjRkb0GOqUBhFnBQsrNNF03ccWpJydhojpRYFRYod98qhuNtc2DBuImnjcsJvbtHniFnbwv5gnT07Do8IDziNv5fAC89QI3HD%2BBAyHZbGepP%2FagHj5ScstfexAPcD0EeiklwMhhFokM7%2BtHbLk0cbZFzi%2F9UPetAy7NyR4FcunnSSgSoUW87AJrNNEwC%2FH3WMHi7uJi0I5%2FOI7B%2BKmQkYC6Q7zeyHvZgi%2Fue2P%2B&X-Amz-Signature=a93e7719ebf3d38284384fb8814f6a640d9f9f9efd00f83457cc11d11032f246&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YYHRVIC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCjbVGIEcNisemui9IOpwmLvwOLZ8Z4FQicd6HH1DOazAIgQmBLJ2uLItsODnvQcBtLI8pnCyWl7cwoDs%2BzF1znmfEq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDCD5VEHy9%2FA9vtKPkircA%2BTtfZqEjSvz%2FhpwoXw%2FHuXCGfeV23rNQOZESvLW5%2Bqb%2Bv5bpPX6Q2OyGOFmhOwKctRiDErLNCkO%2BmMITT0fnbXY2RAjMNfHPgilMXcEqMrkOy2wfvEScW0s8xGm2%2FRrPfT%2FinmO95g7fGo%2FGZaiTuhi9afS%2FBpgxdKV3Kf2Siq3DT7QTII0ejNE40Vsut49G3AMZ%2BbF2494fV6n3wvA2qZqiXAfBjuTW6i517uUs0IGWj31I7SkfV152OWplw9XQAWPCbOX7cq5TRvoeLAVf96Whrd4u%2F%2BQlgSkRE3ChPUSeqGZMRnNEmru%2FFRus%2FLEPoAIVB4YbxqpsC2sk6uSTjLJqsRFuXgfQ2XaKmtA8VIxY3MG3Vvy81QjlORn2uVk2BFJqeVjb%2FEC3tKEP%2ByYtto0iKtCCQYR7lFps8PIvKCtr7Cv7nZhZ%2FFcZ8m0e3RtJfFexBz9yGKrGoyD1j9ij5ldb%2B%2BJaPiSyqnUTnoHFoWZh7PFeZYjlafHz3XiRqIQ1FtItXQN%2B2YBVpaHLvgebWbiXv6fWnsTDtZ29q2NFad3zhdwtyqoNLvO9l6869fDyQqipfPa1Ux4v5twbba293%2BexQuOXKRsFwSNe8EyoW4Opwf2kNHDGChlb0%2F9MMjRkb0GOqUByQdFwqD1RWM2wQ6Nk%2FSU9xERHNep6GFNiihSM9pHl7LPzQHNkVs8rxDCgmlNIDC%2BxnGcMpjaGb4moox%2FuHwoFPwAi9SSG8vUWZz4ea531%2FbQpQe79eykY2CuYuCUwgAj7qSrixce4ft%2F%2Fa6cOGQrkY9QkJ2wRb5Di1gowdjBKfBRvnVsNwV0wKhqZWIFG7KN2ba4E7vGBb0BDl7fZ6hYDioNmi99&X-Amz-Signature=d23f521a407b868a65194bee195db0e1c400e0103a9c399aa4241ee934f74840&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YYHRVIC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCjbVGIEcNisemui9IOpwmLvwOLZ8Z4FQicd6HH1DOazAIgQmBLJ2uLItsODnvQcBtLI8pnCyWl7cwoDs%2BzF1znmfEq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDCD5VEHy9%2FA9vtKPkircA%2BTtfZqEjSvz%2FhpwoXw%2FHuXCGfeV23rNQOZESvLW5%2Bqb%2Bv5bpPX6Q2OyGOFmhOwKctRiDErLNCkO%2BmMITT0fnbXY2RAjMNfHPgilMXcEqMrkOy2wfvEScW0s8xGm2%2FRrPfT%2FinmO95g7fGo%2FGZaiTuhi9afS%2FBpgxdKV3Kf2Siq3DT7QTII0ejNE40Vsut49G3AMZ%2BbF2494fV6n3wvA2qZqiXAfBjuTW6i517uUs0IGWj31I7SkfV152OWplw9XQAWPCbOX7cq5TRvoeLAVf96Whrd4u%2F%2BQlgSkRE3ChPUSeqGZMRnNEmru%2FFRus%2FLEPoAIVB4YbxqpsC2sk6uSTjLJqsRFuXgfQ2XaKmtA8VIxY3MG3Vvy81QjlORn2uVk2BFJqeVjb%2FEC3tKEP%2ByYtto0iKtCCQYR7lFps8PIvKCtr7Cv7nZhZ%2FFcZ8m0e3RtJfFexBz9yGKrGoyD1j9ij5ldb%2B%2BJaPiSyqnUTnoHFoWZh7PFeZYjlafHz3XiRqIQ1FtItXQN%2B2YBVpaHLvgebWbiXv6fWnsTDtZ29q2NFad3zhdwtyqoNLvO9l6869fDyQqipfPa1Ux4v5twbba293%2BexQuOXKRsFwSNe8EyoW4Opwf2kNHDGChlb0%2F9MMjRkb0GOqUByQdFwqD1RWM2wQ6Nk%2FSU9xERHNep6GFNiihSM9pHl7LPzQHNkVs8rxDCgmlNIDC%2BxnGcMpjaGb4moox%2FuHwoFPwAi9SSG8vUWZz4ea531%2FbQpQe79eykY2CuYuCUwgAj7qSrixce4ft%2F%2Fa6cOGQrkY9QkJ2wRb5Di1gowdjBKfBRvnVsNwV0wKhqZWIFG7KN2ba4E7vGBb0BDl7fZ6hYDioNmi99&X-Amz-Signature=ce2fb5a70cfe8973f6e5c8bd14bc753705a0385ee1189442a64a39300eebe306&X-Amz-SignedHeaders=host&x-id=GetObject)
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
