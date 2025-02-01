

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWTU56IY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovA%2FCqvpmcUkJV0rKMNNYu3Mu9HJq0PEaW7i9UlooDAIhAJB3OtQlbP7XxYIiMj36BXlSmeeCX9%2F2V7%2BD2Ri%2FhWISKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHBk%2FbGSaZ5UC2lLMq3AMH8oS15eafIOm%2BjPB0aXK9i6%2Fzay2lEA3FmFI0Zxzi9YJUkkRxoYTIC%2Bqywa3Otjd2lWwZmTkDC3HOB0s%2BsKka1R%2FGwvP4AItXyOd%2B0R8bHVo%2FqbwP5O4CzEsNTNoS9A6lTAlDQ72njl2WJyCuPlqT6mOjQhRCzdAE9%2BtseBRuHDEOrG6n64yiCiOz4I1gEMYwFY6kjV0lv4KmiguZAixklLaiWp8YbbaMKU5KMjmE0VLvDuHx1lfWC%2FbwtAc416zb0TmGpGnX17w5A4KNv%2F73uX8FRRVRQB02gSgZjQIJFLGQBR6nbjdfuIR9%2Bsubaz95vnKf7qOuV59XSe0EBrGZezApsGz%2FuPLdSlCy%2BVGpEdsG7RIa7256tmWvmV5cc7XaFc4UnuUskq72Cgrq3qPw2t722%2FaDMVqEn8IOtmthbSbzXQ%2B%2Ffw%2F4yePCqM3joLvQ6SJLt3FuepRFuoFpLLCJJpAE6hJ7Kjkg0teTOA5fv9n3OfgCSy3xGgzdfeUkuWZKd93aDfFHp2ChLOC3HQUn2S2p0ii%2FpFsaRxqIi0vG79gDpkwXYNDKj5F2g7YJiwNd36Q4zfloR%2BL55sYEz%2BcQ2WFynd6qnA4jJQvKFOHboEVyfurtJzHk99mCpzCOyPi8BjqkAbyTss6BxJj%2Bad%2Bg5G5HfhreHhNlhzjY%2BMYR7R9lsNfZd0YFwIM47YUoS9oMFADzDEpEWnmJtJC62EPm2SiZgUOjO4pUearBV5cqMNxmsUInojXhLAKIP9E0kcfIjbJxLqk%2FPMPrfcT%2FDws39zy%2F0Y46cMeyOh5%2BM222QTTht25p5UxglMaF7lah%2BVfogitwwAXF50IZKHT%2BJc9nP%2FH%2BqOThP6C%2F&X-Amz-Signature=03cd6fc134f1f3cef8d47578651c954489e16271c473dc2b1280ba7a3da97a85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWTU56IY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovA%2FCqvpmcUkJV0rKMNNYu3Mu9HJq0PEaW7i9UlooDAIhAJB3OtQlbP7XxYIiMj36BXlSmeeCX9%2F2V7%2BD2Ri%2FhWISKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHBk%2FbGSaZ5UC2lLMq3AMH8oS15eafIOm%2BjPB0aXK9i6%2Fzay2lEA3FmFI0Zxzi9YJUkkRxoYTIC%2Bqywa3Otjd2lWwZmTkDC3HOB0s%2BsKka1R%2FGwvP4AItXyOd%2B0R8bHVo%2FqbwP5O4CzEsNTNoS9A6lTAlDQ72njl2WJyCuPlqT6mOjQhRCzdAE9%2BtseBRuHDEOrG6n64yiCiOz4I1gEMYwFY6kjV0lv4KmiguZAixklLaiWp8YbbaMKU5KMjmE0VLvDuHx1lfWC%2FbwtAc416zb0TmGpGnX17w5A4KNv%2F73uX8FRRVRQB02gSgZjQIJFLGQBR6nbjdfuIR9%2Bsubaz95vnKf7qOuV59XSe0EBrGZezApsGz%2FuPLdSlCy%2BVGpEdsG7RIa7256tmWvmV5cc7XaFc4UnuUskq72Cgrq3qPw2t722%2FaDMVqEn8IOtmthbSbzXQ%2B%2Ffw%2F4yePCqM3joLvQ6SJLt3FuepRFuoFpLLCJJpAE6hJ7Kjkg0teTOA5fv9n3OfgCSy3xGgzdfeUkuWZKd93aDfFHp2ChLOC3HQUn2S2p0ii%2FpFsaRxqIi0vG79gDpkwXYNDKj5F2g7YJiwNd36Q4zfloR%2BL55sYEz%2BcQ2WFynd6qnA4jJQvKFOHboEVyfurtJzHk99mCpzCOyPi8BjqkAbyTss6BxJj%2Bad%2Bg5G5HfhreHhNlhzjY%2BMYR7R9lsNfZd0YFwIM47YUoS9oMFADzDEpEWnmJtJC62EPm2SiZgUOjO4pUearBV5cqMNxmsUInojXhLAKIP9E0kcfIjbJxLqk%2FPMPrfcT%2FDws39zy%2F0Y46cMeyOh5%2BM222QTTht25p5UxglMaF7lah%2BVfogitwwAXF50IZKHT%2BJc9nP%2FH%2BqOThP6C%2F&X-Amz-Signature=3aed3ca29953d5571c2ec232b4d4d0f35fc613ee3e7bda03ff83bdd3a04db397&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWTU56IY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovA%2FCqvpmcUkJV0rKMNNYu3Mu9HJq0PEaW7i9UlooDAIhAJB3OtQlbP7XxYIiMj36BXlSmeeCX9%2F2V7%2BD2Ri%2FhWISKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHBk%2FbGSaZ5UC2lLMq3AMH8oS15eafIOm%2BjPB0aXK9i6%2Fzay2lEA3FmFI0Zxzi9YJUkkRxoYTIC%2Bqywa3Otjd2lWwZmTkDC3HOB0s%2BsKka1R%2FGwvP4AItXyOd%2B0R8bHVo%2FqbwP5O4CzEsNTNoS9A6lTAlDQ72njl2WJyCuPlqT6mOjQhRCzdAE9%2BtseBRuHDEOrG6n64yiCiOz4I1gEMYwFY6kjV0lv4KmiguZAixklLaiWp8YbbaMKU5KMjmE0VLvDuHx1lfWC%2FbwtAc416zb0TmGpGnX17w5A4KNv%2F73uX8FRRVRQB02gSgZjQIJFLGQBR6nbjdfuIR9%2Bsubaz95vnKf7qOuV59XSe0EBrGZezApsGz%2FuPLdSlCy%2BVGpEdsG7RIa7256tmWvmV5cc7XaFc4UnuUskq72Cgrq3qPw2t722%2FaDMVqEn8IOtmthbSbzXQ%2B%2Ffw%2F4yePCqM3joLvQ6SJLt3FuepRFuoFpLLCJJpAE6hJ7Kjkg0teTOA5fv9n3OfgCSy3xGgzdfeUkuWZKd93aDfFHp2ChLOC3HQUn2S2p0ii%2FpFsaRxqIi0vG79gDpkwXYNDKj5F2g7YJiwNd36Q4zfloR%2BL55sYEz%2BcQ2WFynd6qnA4jJQvKFOHboEVyfurtJzHk99mCpzCOyPi8BjqkAbyTss6BxJj%2Bad%2Bg5G5HfhreHhNlhzjY%2BMYR7R9lsNfZd0YFwIM47YUoS9oMFADzDEpEWnmJtJC62EPm2SiZgUOjO4pUearBV5cqMNxmsUInojXhLAKIP9E0kcfIjbJxLqk%2FPMPrfcT%2FDws39zy%2F0Y46cMeyOh5%2BM222QTTht25p5UxglMaF7lah%2BVfogitwwAXF50IZKHT%2BJc9nP%2FH%2BqOThP6C%2F&X-Amz-Signature=033fbc135c21e029683c88640df06afd22afa611fb522044ec09e9f4f37dd9e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWTU56IY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovA%2FCqvpmcUkJV0rKMNNYu3Mu9HJq0PEaW7i9UlooDAIhAJB3OtQlbP7XxYIiMj36BXlSmeeCX9%2F2V7%2BD2Ri%2FhWISKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHBk%2FbGSaZ5UC2lLMq3AMH8oS15eafIOm%2BjPB0aXK9i6%2Fzay2lEA3FmFI0Zxzi9YJUkkRxoYTIC%2Bqywa3Otjd2lWwZmTkDC3HOB0s%2BsKka1R%2FGwvP4AItXyOd%2B0R8bHVo%2FqbwP5O4CzEsNTNoS9A6lTAlDQ72njl2WJyCuPlqT6mOjQhRCzdAE9%2BtseBRuHDEOrG6n64yiCiOz4I1gEMYwFY6kjV0lv4KmiguZAixklLaiWp8YbbaMKU5KMjmE0VLvDuHx1lfWC%2FbwtAc416zb0TmGpGnX17w5A4KNv%2F73uX8FRRVRQB02gSgZjQIJFLGQBR6nbjdfuIR9%2Bsubaz95vnKf7qOuV59XSe0EBrGZezApsGz%2FuPLdSlCy%2BVGpEdsG7RIa7256tmWvmV5cc7XaFc4UnuUskq72Cgrq3qPw2t722%2FaDMVqEn8IOtmthbSbzXQ%2B%2Ffw%2F4yePCqM3joLvQ6SJLt3FuepRFuoFpLLCJJpAE6hJ7Kjkg0teTOA5fv9n3OfgCSy3xGgzdfeUkuWZKd93aDfFHp2ChLOC3HQUn2S2p0ii%2FpFsaRxqIi0vG79gDpkwXYNDKj5F2g7YJiwNd36Q4zfloR%2BL55sYEz%2BcQ2WFynd6qnA4jJQvKFOHboEVyfurtJzHk99mCpzCOyPi8BjqkAbyTss6BxJj%2Bad%2Bg5G5HfhreHhNlhzjY%2BMYR7R9lsNfZd0YFwIM47YUoS9oMFADzDEpEWnmJtJC62EPm2SiZgUOjO4pUearBV5cqMNxmsUInojXhLAKIP9E0kcfIjbJxLqk%2FPMPrfcT%2FDws39zy%2F0Y46cMeyOh5%2BM222QTTht25p5UxglMaF7lah%2BVfogitwwAXF50IZKHT%2BJc9nP%2FH%2BqOThP6C%2F&X-Amz-Signature=d8003128beb35103c2afaacc8746fe084b5a9f34ce0810868f93358f952100e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWTU56IY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovA%2FCqvpmcUkJV0rKMNNYu3Mu9HJq0PEaW7i9UlooDAIhAJB3OtQlbP7XxYIiMj36BXlSmeeCX9%2F2V7%2BD2Ri%2FhWISKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHBk%2FbGSaZ5UC2lLMq3AMH8oS15eafIOm%2BjPB0aXK9i6%2Fzay2lEA3FmFI0Zxzi9YJUkkRxoYTIC%2Bqywa3Otjd2lWwZmTkDC3HOB0s%2BsKka1R%2FGwvP4AItXyOd%2B0R8bHVo%2FqbwP5O4CzEsNTNoS9A6lTAlDQ72njl2WJyCuPlqT6mOjQhRCzdAE9%2BtseBRuHDEOrG6n64yiCiOz4I1gEMYwFY6kjV0lv4KmiguZAixklLaiWp8YbbaMKU5KMjmE0VLvDuHx1lfWC%2FbwtAc416zb0TmGpGnX17w5A4KNv%2F73uX8FRRVRQB02gSgZjQIJFLGQBR6nbjdfuIR9%2Bsubaz95vnKf7qOuV59XSe0EBrGZezApsGz%2FuPLdSlCy%2BVGpEdsG7RIa7256tmWvmV5cc7XaFc4UnuUskq72Cgrq3qPw2t722%2FaDMVqEn8IOtmthbSbzXQ%2B%2Ffw%2F4yePCqM3joLvQ6SJLt3FuepRFuoFpLLCJJpAE6hJ7Kjkg0teTOA5fv9n3OfgCSy3xGgzdfeUkuWZKd93aDfFHp2ChLOC3HQUn2S2p0ii%2FpFsaRxqIi0vG79gDpkwXYNDKj5F2g7YJiwNd36Q4zfloR%2BL55sYEz%2BcQ2WFynd6qnA4jJQvKFOHboEVyfurtJzHk99mCpzCOyPi8BjqkAbyTss6BxJj%2Bad%2Bg5G5HfhreHhNlhzjY%2BMYR7R9lsNfZd0YFwIM47YUoS9oMFADzDEpEWnmJtJC62EPm2SiZgUOjO4pUearBV5cqMNxmsUInojXhLAKIP9E0kcfIjbJxLqk%2FPMPrfcT%2FDws39zy%2F0Y46cMeyOh5%2BM222QTTht25p5UxglMaF7lah%2BVfogitwwAXF50IZKHT%2BJc9nP%2FH%2BqOThP6C%2F&X-Amz-Signature=306ae81ba8e4d5e3c894dacc2581a624f38680152e085ecc5617ec12edfe12d2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWTU56IY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovA%2FCqvpmcUkJV0rKMNNYu3Mu9HJq0PEaW7i9UlooDAIhAJB3OtQlbP7XxYIiMj36BXlSmeeCX9%2F2V7%2BD2Ri%2FhWISKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHBk%2FbGSaZ5UC2lLMq3AMH8oS15eafIOm%2BjPB0aXK9i6%2Fzay2lEA3FmFI0Zxzi9YJUkkRxoYTIC%2Bqywa3Otjd2lWwZmTkDC3HOB0s%2BsKka1R%2FGwvP4AItXyOd%2B0R8bHVo%2FqbwP5O4CzEsNTNoS9A6lTAlDQ72njl2WJyCuPlqT6mOjQhRCzdAE9%2BtseBRuHDEOrG6n64yiCiOz4I1gEMYwFY6kjV0lv4KmiguZAixklLaiWp8YbbaMKU5KMjmE0VLvDuHx1lfWC%2FbwtAc416zb0TmGpGnX17w5A4KNv%2F73uX8FRRVRQB02gSgZjQIJFLGQBR6nbjdfuIR9%2Bsubaz95vnKf7qOuV59XSe0EBrGZezApsGz%2FuPLdSlCy%2BVGpEdsG7RIa7256tmWvmV5cc7XaFc4UnuUskq72Cgrq3qPw2t722%2FaDMVqEn8IOtmthbSbzXQ%2B%2Ffw%2F4yePCqM3joLvQ6SJLt3FuepRFuoFpLLCJJpAE6hJ7Kjkg0teTOA5fv9n3OfgCSy3xGgzdfeUkuWZKd93aDfFHp2ChLOC3HQUn2S2p0ii%2FpFsaRxqIi0vG79gDpkwXYNDKj5F2g7YJiwNd36Q4zfloR%2BL55sYEz%2BcQ2WFynd6qnA4jJQvKFOHboEVyfurtJzHk99mCpzCOyPi8BjqkAbyTss6BxJj%2Bad%2Bg5G5HfhreHhNlhzjY%2BMYR7R9lsNfZd0YFwIM47YUoS9oMFADzDEpEWnmJtJC62EPm2SiZgUOjO4pUearBV5cqMNxmsUInojXhLAKIP9E0kcfIjbJxLqk%2FPMPrfcT%2FDws39zy%2F0Y46cMeyOh5%2BM222QTTht25p5UxglMaF7lah%2BVfogitwwAXF50IZKHT%2BJc9nP%2FH%2BqOThP6C%2F&X-Amz-Signature=8872a36cbe3e3520acbdac220ff647d4e330d3a4903fde45f5d80fbcedd7269c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWTU56IY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovA%2FCqvpmcUkJV0rKMNNYu3Mu9HJq0PEaW7i9UlooDAIhAJB3OtQlbP7XxYIiMj36BXlSmeeCX9%2F2V7%2BD2Ri%2FhWISKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHBk%2FbGSaZ5UC2lLMq3AMH8oS15eafIOm%2BjPB0aXK9i6%2Fzay2lEA3FmFI0Zxzi9YJUkkRxoYTIC%2Bqywa3Otjd2lWwZmTkDC3HOB0s%2BsKka1R%2FGwvP4AItXyOd%2B0R8bHVo%2FqbwP5O4CzEsNTNoS9A6lTAlDQ72njl2WJyCuPlqT6mOjQhRCzdAE9%2BtseBRuHDEOrG6n64yiCiOz4I1gEMYwFY6kjV0lv4KmiguZAixklLaiWp8YbbaMKU5KMjmE0VLvDuHx1lfWC%2FbwtAc416zb0TmGpGnX17w5A4KNv%2F73uX8FRRVRQB02gSgZjQIJFLGQBR6nbjdfuIR9%2Bsubaz95vnKf7qOuV59XSe0EBrGZezApsGz%2FuPLdSlCy%2BVGpEdsG7RIa7256tmWvmV5cc7XaFc4UnuUskq72Cgrq3qPw2t722%2FaDMVqEn8IOtmthbSbzXQ%2B%2Ffw%2F4yePCqM3joLvQ6SJLt3FuepRFuoFpLLCJJpAE6hJ7Kjkg0teTOA5fv9n3OfgCSy3xGgzdfeUkuWZKd93aDfFHp2ChLOC3HQUn2S2p0ii%2FpFsaRxqIi0vG79gDpkwXYNDKj5F2g7YJiwNd36Q4zfloR%2BL55sYEz%2BcQ2WFynd6qnA4jJQvKFOHboEVyfurtJzHk99mCpzCOyPi8BjqkAbyTss6BxJj%2Bad%2Bg5G5HfhreHhNlhzjY%2BMYR7R9lsNfZd0YFwIM47YUoS9oMFADzDEpEWnmJtJC62EPm2SiZgUOjO4pUearBV5cqMNxmsUInojXhLAKIP9E0kcfIjbJxLqk%2FPMPrfcT%2FDws39zy%2F0Y46cMeyOh5%2BM222QTTht25p5UxglMaF7lah%2BVfogitwwAXF50IZKHT%2BJc9nP%2FH%2BqOThP6C%2F&X-Amz-Signature=56775efbd4d2a4c2dd02c8f62a46f84cee003309f130445ad065fd31ce371c37&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWTU56IY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovA%2FCqvpmcUkJV0rKMNNYu3Mu9HJq0PEaW7i9UlooDAIhAJB3OtQlbP7XxYIiMj36BXlSmeeCX9%2F2V7%2BD2Ri%2FhWISKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHBk%2FbGSaZ5UC2lLMq3AMH8oS15eafIOm%2BjPB0aXK9i6%2Fzay2lEA3FmFI0Zxzi9YJUkkRxoYTIC%2Bqywa3Otjd2lWwZmTkDC3HOB0s%2BsKka1R%2FGwvP4AItXyOd%2B0R8bHVo%2FqbwP5O4CzEsNTNoS9A6lTAlDQ72njl2WJyCuPlqT6mOjQhRCzdAE9%2BtseBRuHDEOrG6n64yiCiOz4I1gEMYwFY6kjV0lv4KmiguZAixklLaiWp8YbbaMKU5KMjmE0VLvDuHx1lfWC%2FbwtAc416zb0TmGpGnX17w5A4KNv%2F73uX8FRRVRQB02gSgZjQIJFLGQBR6nbjdfuIR9%2Bsubaz95vnKf7qOuV59XSe0EBrGZezApsGz%2FuPLdSlCy%2BVGpEdsG7RIa7256tmWvmV5cc7XaFc4UnuUskq72Cgrq3qPw2t722%2FaDMVqEn8IOtmthbSbzXQ%2B%2Ffw%2F4yePCqM3joLvQ6SJLt3FuepRFuoFpLLCJJpAE6hJ7Kjkg0teTOA5fv9n3OfgCSy3xGgzdfeUkuWZKd93aDfFHp2ChLOC3HQUn2S2p0ii%2FpFsaRxqIi0vG79gDpkwXYNDKj5F2g7YJiwNd36Q4zfloR%2BL55sYEz%2BcQ2WFynd6qnA4jJQvKFOHboEVyfurtJzHk99mCpzCOyPi8BjqkAbyTss6BxJj%2Bad%2Bg5G5HfhreHhNlhzjY%2BMYR7R9lsNfZd0YFwIM47YUoS9oMFADzDEpEWnmJtJC62EPm2SiZgUOjO4pUearBV5cqMNxmsUInojXhLAKIP9E0kcfIjbJxLqk%2FPMPrfcT%2FDws39zy%2F0Y46cMeyOh5%2BM222QTTht25p5UxglMaF7lah%2BVfogitwwAXF50IZKHT%2BJc9nP%2FH%2BqOThP6C%2F&X-Amz-Signature=cd043a3f969af3436a768c86f82ab1e4597c699d786f0603e30cb881da4f02b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQJIEYDV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHodzJTI0GJPS0PEkzYiZIQQXLvMMmFkkYxZH2rvrQQ6AiA4T3Fxmyo3rHgfANrfSo%2BrK5OcnB2ybTpo%2FXQ5YnXGFiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcGOtEMfV9WtGdtpoKtwD1ljh4nkRy%2Bl%2FdBPzJ3Fwn020HW72zyVu65VteQ30ZnwzIPI2N2nUKnZDMaahdzjqqMz9y0cbuV2hbPeSvL%2Fo1AZ5v0U4Cnic5h0kpgSTOmhUijV4v%2F%2Bz3S7v2v28W%2B%2FRwM%2F%2BHyciNqsvUrYXHXVyDnHfmccNqJe6aqBIa33NwefX5dixqrL4I7lZAulNNP%2BQcR7d%2FUpxfKr8wn4wI0y5O79TLeNm4qGBjY5Li2NPQ%2Fb8tjDYnYa6X7HhruPN37DkXf%2FXfezSsCEcVLUyHHt4czKMSDiPGHvrrLJGZsWYcf8b2bBo97xS8mxzNQ2rENADWx99SsKC%2BolWFI7sK1H%2FLJE%2B8auXiWRSFN1qAn%2FAgDHb%2BXvIGXphjbJL6Y9jf6UkZxh4EailZKXWiXMShiRm3BTu4c4wjBKqvV0Kf0AeL19%2Bz%2BFGlIedaHxCUH%2BBC1kBMZ4cCblADZAv5Cj6BSgtHjC%2FrF5oX6ydPTgxCyEokcSisxXR4Xz%2FPY0z6YNEbcx%2Be%2BC7ACACpWaQUnKr471BTmeUlLUKUXcGr7zUF8XfEHcGrMsPnJsfioTV3NHr9RWWEX4i8IkAUMIke9g80ZoYdQtKLa27QfaqAwdfgk%2BVxIzUhTqPd3KPp6rCedcwgML4vAY6pgHRBSDpD0ILUdH2q43a%2B4HO9OMcBEMIsJdZwj4dgFEtCpiVuZCYW5oyoRoh4pewh1Sk2mg8FuCwaFytqjDopehkMZ9RPeSl%2Bk%2BsGlFeKUaMDGI4KzpW3ijrAzdxvpjgbfb4YmSCzoHOmQUZEW%2Bvl1VmmCD0Y0VBJ7F16qHHBttpaFj8kgpg266LfaXWNwxJ25vTnHPOxj5DnheUi6oKZac8pLAS%2BVeL&X-Amz-Signature=abf749ea13626cc4d8df29d6530f6203b3a4c6b24d7189828a5c094a302c58da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBJMCV6Q%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMcIC8bpDIXqp4G5Rsnph%2BESwOijcCM9MDce1ZDTP6ngIgXv%2BZZ2GYh3xRj%2Bf5x4hm6kVcfhaj%2BwP4l2SrGs1J9HUqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIw8EtIQiHTTbPL2YSrcA9JznmmIdmKZ3U6dLKbWFmyB31c5W%2FVvXwZYE0%2BhCAHCgDFDKR7XpzVVJVVmF4%2F3YdW0uyujEE%2FQwMz4lL3ckB1Eg3s7JFZgreZilCTa%2Be%2BfNyYbm18lcSWkjGe3sIWMSG4VBeSzVGcReGbebNMxHPCu%2F8pWH37RU9kOKZ%2BXYO2UJTdQLtl%2Fg2c3OKExsNpM%2B9gokSGnUDRfhZYWshN6U5tPdzN8tD6lTYB7vio55meuo4pCuODq19JOJsFBgkRgVtGz4K84wD30DsWKXF2cjG8B2M5plCzjHayMfDgkrZwkjBrc6Kjb40LnZW9pSoVQByQt5FnlBMgOQvf7h%2Bk7x9%2FonTUDOA63UkJ%2FNuc2JsVeOm87rpTCNzpwJwU29dC1uMEGXsKa6ZoYRqvvoMUy%2B4ZvV%2B1LMSi18AveCxQjHXncZI13quiHfq9RRbopU%2FcJWJQlvKVgYS%2B2AsgH5DKPYum6GToViPk%2F74WAE1cp5%2FdEcZqIuvt%2BQ1G49cyZ8jglOhqUPfxShswT1c6r%2FhMdQvwyXd8caMr4B%2FBg4VqgLFaL8pXgBeB6OVMrPme5iQXb2s%2FJ4m%2BCKab%2B5VOvvif4dWNpdc9C4hbPNiqvYMykKB9AVqMAUNNh2FZE8gbpMJDB%2BLwGOqUB00AhvrP8V2dCfRDaRMnvxhQ1sOEUexfcmE%2BkoH80SFEQ%2FqV9xdG8GlkRdqtIAEc%2BCe1Li8aOVCvnGnCLs4ljO3T6c3ujLnS58%2FH4kl6x2sIztYBXmwYsn%2FpIxErI21zG6pCPh%2FPcG%2FuYz31AChj9SR7ueC1LQ8xY66IIdFG6vgi0K73Nc7fq2CjpblGC1UewiUjHEiqD5ke2zJOttJ4crhdX1Acx&X-Amz-Signature=054b6d13b7c431965dab8f21f5748b6287710d2ae384a8322a325dfc7ddcea02&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYFKHI5Q%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG17DV5bNiTwDywpYaAx4KdzlR0a1AD84ZptJfjeP8RIAiEAiaCasVaL0%2B2icXSqcHVOJMnQ32PoBsW7DMczAbpYcnEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObGdKXl6por1cSkpSrcA62NNQnJ%2Bv06oVw7%2FqHjT%2Ba%2Bzsot38t8e%2FEcODv49xII9qwhk82XAcWHQq92vZcSxM5MNh%2BTT4Zer2pQZBsmwoPObj66HYaf6MJ7HDdRsbP10G9hWxI0pmSqyABLMPOA0e%2B8%2Fcq7lFe27N64%2BIy4bHzDZvemCTrLcg1R9OuX5aWYXjJ9d7dv%2FjypYJA3qtZOvZ%2BXvx0pQqakwoy3aeSfdOON6Oqg2B%2ByE4B1fymSZ8rgcwP6ZoUBH0JiXUjDG3yMkm6VSaikzo8EMc3REbPtmN%2BuA66obaw16HjAk5ZONN95m0keoPj0YIdouSBvB0AIIg%2BKl7AxCc9rFkziZ9RcKtsJfAA3IgU0cIJdJ5SIpKs0qdnfzuHB4DBdRYab0V7jpy9XNdGKhJ%2Fu9AUQhpGb48KY%2BNkIvUxiSq1g%2Buo%2BYiKjM1iNmSjcYXk6vgRrxONQTYgKxIOvSaZ%2BnNoHPjpB9Yfdp0ypbaIcbK7XyRxZJ%2Fu1JcYPVBb%2BrGSiTzblu9rGXZbNcJrAZ2cxUluh99U7vXi9%2BK9XUtwvnW4Q5RPkHHOV1tCVHiclCuNIXYD9Tu9EqGk7sbUe64cTxN05Gm3%2FnkvKCMJGey1nmvAkNH9mtHIPA%2BOa%2BPNkO%2FQl4ug9MLLI%2BLwGOqUBt6lDj%2FV0i4aMhD%2BVTjJRCHtst3u7Xl%2F8ek7tcwYidakjmv5A%2F43wPKm%2B7O%2BnG0JHycFhZ5Qm0FYdvCmpslr1gIPH1WfQaCqG6flP%2FurlqZNazTzgTNd5EfRhgiCbm8oA7pvyK%2FN3YN%2BiAQNKXqd2DyfmgTMP%2FBz%2BUnm%2ForQdxS3UbO83jlNKG%2F68klwEf7PA%2FV9cdrUZpihTfV3%2B0H3MU4bte7gw&X-Amz-Signature=4fd5967d3e5f7c61120e68ffe5e5c197b0a00c8cca82ea461b1414b46289cdcd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYFKHI5Q%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG17DV5bNiTwDywpYaAx4KdzlR0a1AD84ZptJfjeP8RIAiEAiaCasVaL0%2B2icXSqcHVOJMnQ32PoBsW7DMczAbpYcnEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObGdKXl6por1cSkpSrcA62NNQnJ%2Bv06oVw7%2FqHjT%2Ba%2Bzsot38t8e%2FEcODv49xII9qwhk82XAcWHQq92vZcSxM5MNh%2BTT4Zer2pQZBsmwoPObj66HYaf6MJ7HDdRsbP10G9hWxI0pmSqyABLMPOA0e%2B8%2Fcq7lFe27N64%2BIy4bHzDZvemCTrLcg1R9OuX5aWYXjJ9d7dv%2FjypYJA3qtZOvZ%2BXvx0pQqakwoy3aeSfdOON6Oqg2B%2ByE4B1fymSZ8rgcwP6ZoUBH0JiXUjDG3yMkm6VSaikzo8EMc3REbPtmN%2BuA66obaw16HjAk5ZONN95m0keoPj0YIdouSBvB0AIIg%2BKl7AxCc9rFkziZ9RcKtsJfAA3IgU0cIJdJ5SIpKs0qdnfzuHB4DBdRYab0V7jpy9XNdGKhJ%2Fu9AUQhpGb48KY%2BNkIvUxiSq1g%2Buo%2BYiKjM1iNmSjcYXk6vgRrxONQTYgKxIOvSaZ%2BnNoHPjpB9Yfdp0ypbaIcbK7XyRxZJ%2Fu1JcYPVBb%2BrGSiTzblu9rGXZbNcJrAZ2cxUluh99U7vXi9%2BK9XUtwvnW4Q5RPkHHOV1tCVHiclCuNIXYD9Tu9EqGk7sbUe64cTxN05Gm3%2FnkvKCMJGey1nmvAkNH9mtHIPA%2BOa%2BPNkO%2FQl4ug9MLLI%2BLwGOqUBt6lDj%2FV0i4aMhD%2BVTjJRCHtst3u7Xl%2F8ek7tcwYidakjmv5A%2F43wPKm%2B7O%2BnG0JHycFhZ5Qm0FYdvCmpslr1gIPH1WfQaCqG6flP%2FurlqZNazTzgTNd5EfRhgiCbm8oA7pvyK%2FN3YN%2BiAQNKXqd2DyfmgTMP%2FBz%2BUnm%2ForQdxS3UbO83jlNKG%2F68klwEf7PA%2FV9cdrUZpihTfV3%2B0H3MU4bte7gw&X-Amz-Signature=e8f304dbde379a15afb8b532ea482f0ff515c79ae4cd034db8b36efb441eb943&X-Amz-SignedHeaders=host&x-id=GetObject)
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
