

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ENE446%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6nHUb5qze18Yd9enJPj0JoJEC9shoY8pIGXxfDvWWwQIgf1l3JMfzYq9xoxEW67upd%2BPSKKufEjyfaTTkEr%2FGpo0qiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCLKg%2F4mPiAUDK53UircA2jXYQei%2FgHf%2Fx68k9WTIEll2CWnbHO75zgWWK196tK3JEiIeIoybXSrt0J%2F1Vef27MmFWFdwC7CdY4jUA4ToJpy9BhM36Vl%2Fi%2FjWlygC%2BTJbJp1%2F%2FnEtR2Shi4fdjZ1sEnM0rJnRh62xyWz%2FqDGIQwYekwtG5FOEBoGAEz9gmgyKlXLngwj5u%2F6sE5f7BPYL7LVWsKU7U%2BO5WyQXeIfCG7w3CDWjqkYuc1Q8O6TOMWIHmkpVzmtLHcc5rGZ8xui9LgT%2FM6DmEpCGcxwPxelXuJoA%2BaDvXB7OfbCVhQu0V%2FGtkFG2uZ9o3D%2F7SHqCRq9h784P22%2BfQYeaMVAjkr5oRRG4KQEhXPduHsPX9WZwuTDFFHPKWW31vxSa0Dl6cPH0ea6L0%2FsJDHu03PZ8jyEn69sbyL1NOYEoZKS2DG%2BY9cns4mbCk668Ph6bIthVZtPOPrw6R%2Frl8SZ6N578kTdYrpLl%2F9T9lbJg8lxDjmsh3VjCfs8NrD7WuMV1aDK7Q5SawZL%2F5s2gWaK7%2B5jJDXc%2F9xoB84V8bF2%2BVZC1FDtpGPVAjcrOkn9ipJ%2BAcMBheJhzvn0eW65UvsuXA43l7Hh7aOxWgWglV8rtyqu%2Fb2g3n4oXTQi6s428LwhJ1e3MOu08LwGOqUBvwwZh%2Bb%2F81pvaH1CfELv0v9jfe941%2B04rdhR%2BxhKLVTy5lnuF9edIXXTF%2BhZKmG7Uu%2BcZqlppAcnJll377DYjENQ2TKHDpTfD8RnZwS7BKN7RkxIhtqaF5mECDLc9Dc5yJ4ImZ7eympo10A0sLPZf53%2FNT%2Bwy%2FIm5ZV%2BA2fon%2FCW4yCCX2Y%2BKsydRFBlhSe7hz6izZIjghK4XEmfb4luAvREw6SI&X-Amz-Signature=78f81f95df78294c3391ba3a390076e16bfbcbb545dee457d02499e9adac701e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ENE446%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6nHUb5qze18Yd9enJPj0JoJEC9shoY8pIGXxfDvWWwQIgf1l3JMfzYq9xoxEW67upd%2BPSKKufEjyfaTTkEr%2FGpo0qiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCLKg%2F4mPiAUDK53UircA2jXYQei%2FgHf%2Fx68k9WTIEll2CWnbHO75zgWWK196tK3JEiIeIoybXSrt0J%2F1Vef27MmFWFdwC7CdY4jUA4ToJpy9BhM36Vl%2Fi%2FjWlygC%2BTJbJp1%2F%2FnEtR2Shi4fdjZ1sEnM0rJnRh62xyWz%2FqDGIQwYekwtG5FOEBoGAEz9gmgyKlXLngwj5u%2F6sE5f7BPYL7LVWsKU7U%2BO5WyQXeIfCG7w3CDWjqkYuc1Q8O6TOMWIHmkpVzmtLHcc5rGZ8xui9LgT%2FM6DmEpCGcxwPxelXuJoA%2BaDvXB7OfbCVhQu0V%2FGtkFG2uZ9o3D%2F7SHqCRq9h784P22%2BfQYeaMVAjkr5oRRG4KQEhXPduHsPX9WZwuTDFFHPKWW31vxSa0Dl6cPH0ea6L0%2FsJDHu03PZ8jyEn69sbyL1NOYEoZKS2DG%2BY9cns4mbCk668Ph6bIthVZtPOPrw6R%2Frl8SZ6N578kTdYrpLl%2F9T9lbJg8lxDjmsh3VjCfs8NrD7WuMV1aDK7Q5SawZL%2F5s2gWaK7%2B5jJDXc%2F9xoB84V8bF2%2BVZC1FDtpGPVAjcrOkn9ipJ%2BAcMBheJhzvn0eW65UvsuXA43l7Hh7aOxWgWglV8rtyqu%2Fb2g3n4oXTQi6s428LwhJ1e3MOu08LwGOqUBvwwZh%2Bb%2F81pvaH1CfELv0v9jfe941%2B04rdhR%2BxhKLVTy5lnuF9edIXXTF%2BhZKmG7Uu%2BcZqlppAcnJll377DYjENQ2TKHDpTfD8RnZwS7BKN7RkxIhtqaF5mECDLc9Dc5yJ4ImZ7eympo10A0sLPZf53%2FNT%2Bwy%2FIm5ZV%2BA2fon%2FCW4yCCX2Y%2BKsydRFBlhSe7hz6izZIjghK4XEmfb4luAvREw6SI&X-Amz-Signature=77e7b5b5dad01bfd39e5b3580f2f30bdf49648292fe0c93261bd6065e566eec5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ENE446%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6nHUb5qze18Yd9enJPj0JoJEC9shoY8pIGXxfDvWWwQIgf1l3JMfzYq9xoxEW67upd%2BPSKKufEjyfaTTkEr%2FGpo0qiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCLKg%2F4mPiAUDK53UircA2jXYQei%2FgHf%2Fx68k9WTIEll2CWnbHO75zgWWK196tK3JEiIeIoybXSrt0J%2F1Vef27MmFWFdwC7CdY4jUA4ToJpy9BhM36Vl%2Fi%2FjWlygC%2BTJbJp1%2F%2FnEtR2Shi4fdjZ1sEnM0rJnRh62xyWz%2FqDGIQwYekwtG5FOEBoGAEz9gmgyKlXLngwj5u%2F6sE5f7BPYL7LVWsKU7U%2BO5WyQXeIfCG7w3CDWjqkYuc1Q8O6TOMWIHmkpVzmtLHcc5rGZ8xui9LgT%2FM6DmEpCGcxwPxelXuJoA%2BaDvXB7OfbCVhQu0V%2FGtkFG2uZ9o3D%2F7SHqCRq9h784P22%2BfQYeaMVAjkr5oRRG4KQEhXPduHsPX9WZwuTDFFHPKWW31vxSa0Dl6cPH0ea6L0%2FsJDHu03PZ8jyEn69sbyL1NOYEoZKS2DG%2BY9cns4mbCk668Ph6bIthVZtPOPrw6R%2Frl8SZ6N578kTdYrpLl%2F9T9lbJg8lxDjmsh3VjCfs8NrD7WuMV1aDK7Q5SawZL%2F5s2gWaK7%2B5jJDXc%2F9xoB84V8bF2%2BVZC1FDtpGPVAjcrOkn9ipJ%2BAcMBheJhzvn0eW65UvsuXA43l7Hh7aOxWgWglV8rtyqu%2Fb2g3n4oXTQi6s428LwhJ1e3MOu08LwGOqUBvwwZh%2Bb%2F81pvaH1CfELv0v9jfe941%2B04rdhR%2BxhKLVTy5lnuF9edIXXTF%2BhZKmG7Uu%2BcZqlppAcnJll377DYjENQ2TKHDpTfD8RnZwS7BKN7RkxIhtqaF5mECDLc9Dc5yJ4ImZ7eympo10A0sLPZf53%2FNT%2Bwy%2FIm5ZV%2BA2fon%2FCW4yCCX2Y%2BKsydRFBlhSe7hz6izZIjghK4XEmfb4luAvREw6SI&X-Amz-Signature=6d54af6321feb1cd5d2fae8a3c755c5e8f283497083d63a4b5595d3c220c7724&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ENE446%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6nHUb5qze18Yd9enJPj0JoJEC9shoY8pIGXxfDvWWwQIgf1l3JMfzYq9xoxEW67upd%2BPSKKufEjyfaTTkEr%2FGpo0qiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCLKg%2F4mPiAUDK53UircA2jXYQei%2FgHf%2Fx68k9WTIEll2CWnbHO75zgWWK196tK3JEiIeIoybXSrt0J%2F1Vef27MmFWFdwC7CdY4jUA4ToJpy9BhM36Vl%2Fi%2FjWlygC%2BTJbJp1%2F%2FnEtR2Shi4fdjZ1sEnM0rJnRh62xyWz%2FqDGIQwYekwtG5FOEBoGAEz9gmgyKlXLngwj5u%2F6sE5f7BPYL7LVWsKU7U%2BO5WyQXeIfCG7w3CDWjqkYuc1Q8O6TOMWIHmkpVzmtLHcc5rGZ8xui9LgT%2FM6DmEpCGcxwPxelXuJoA%2BaDvXB7OfbCVhQu0V%2FGtkFG2uZ9o3D%2F7SHqCRq9h784P22%2BfQYeaMVAjkr5oRRG4KQEhXPduHsPX9WZwuTDFFHPKWW31vxSa0Dl6cPH0ea6L0%2FsJDHu03PZ8jyEn69sbyL1NOYEoZKS2DG%2BY9cns4mbCk668Ph6bIthVZtPOPrw6R%2Frl8SZ6N578kTdYrpLl%2F9T9lbJg8lxDjmsh3VjCfs8NrD7WuMV1aDK7Q5SawZL%2F5s2gWaK7%2B5jJDXc%2F9xoB84V8bF2%2BVZC1FDtpGPVAjcrOkn9ipJ%2BAcMBheJhzvn0eW65UvsuXA43l7Hh7aOxWgWglV8rtyqu%2Fb2g3n4oXTQi6s428LwhJ1e3MOu08LwGOqUBvwwZh%2Bb%2F81pvaH1CfELv0v9jfe941%2B04rdhR%2BxhKLVTy5lnuF9edIXXTF%2BhZKmG7Uu%2BcZqlppAcnJll377DYjENQ2TKHDpTfD8RnZwS7BKN7RkxIhtqaF5mECDLc9Dc5yJ4ImZ7eympo10A0sLPZf53%2FNT%2Bwy%2FIm5ZV%2BA2fon%2FCW4yCCX2Y%2BKsydRFBlhSe7hz6izZIjghK4XEmfb4luAvREw6SI&X-Amz-Signature=6545365b12608c9c19f8463d8bac2744efd9c63cb20671c6543f03c52032e6f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ENE446%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6nHUb5qze18Yd9enJPj0JoJEC9shoY8pIGXxfDvWWwQIgf1l3JMfzYq9xoxEW67upd%2BPSKKufEjyfaTTkEr%2FGpo0qiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCLKg%2F4mPiAUDK53UircA2jXYQei%2FgHf%2Fx68k9WTIEll2CWnbHO75zgWWK196tK3JEiIeIoybXSrt0J%2F1Vef27MmFWFdwC7CdY4jUA4ToJpy9BhM36Vl%2Fi%2FjWlygC%2BTJbJp1%2F%2FnEtR2Shi4fdjZ1sEnM0rJnRh62xyWz%2FqDGIQwYekwtG5FOEBoGAEz9gmgyKlXLngwj5u%2F6sE5f7BPYL7LVWsKU7U%2BO5WyQXeIfCG7w3CDWjqkYuc1Q8O6TOMWIHmkpVzmtLHcc5rGZ8xui9LgT%2FM6DmEpCGcxwPxelXuJoA%2BaDvXB7OfbCVhQu0V%2FGtkFG2uZ9o3D%2F7SHqCRq9h784P22%2BfQYeaMVAjkr5oRRG4KQEhXPduHsPX9WZwuTDFFHPKWW31vxSa0Dl6cPH0ea6L0%2FsJDHu03PZ8jyEn69sbyL1NOYEoZKS2DG%2BY9cns4mbCk668Ph6bIthVZtPOPrw6R%2Frl8SZ6N578kTdYrpLl%2F9T9lbJg8lxDjmsh3VjCfs8NrD7WuMV1aDK7Q5SawZL%2F5s2gWaK7%2B5jJDXc%2F9xoB84V8bF2%2BVZC1FDtpGPVAjcrOkn9ipJ%2BAcMBheJhzvn0eW65UvsuXA43l7Hh7aOxWgWglV8rtyqu%2Fb2g3n4oXTQi6s428LwhJ1e3MOu08LwGOqUBvwwZh%2Bb%2F81pvaH1CfELv0v9jfe941%2B04rdhR%2BxhKLVTy5lnuF9edIXXTF%2BhZKmG7Uu%2BcZqlppAcnJll377DYjENQ2TKHDpTfD8RnZwS7BKN7RkxIhtqaF5mECDLc9Dc5yJ4ImZ7eympo10A0sLPZf53%2FNT%2Bwy%2FIm5ZV%2BA2fon%2FCW4yCCX2Y%2BKsydRFBlhSe7hz6izZIjghK4XEmfb4luAvREw6SI&X-Amz-Signature=3b4d088923ed58c2a0182e1bdeb07d5f44256ac138da43b66855526830d387b1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ENE446%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6nHUb5qze18Yd9enJPj0JoJEC9shoY8pIGXxfDvWWwQIgf1l3JMfzYq9xoxEW67upd%2BPSKKufEjyfaTTkEr%2FGpo0qiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCLKg%2F4mPiAUDK53UircA2jXYQei%2FgHf%2Fx68k9WTIEll2CWnbHO75zgWWK196tK3JEiIeIoybXSrt0J%2F1Vef27MmFWFdwC7CdY4jUA4ToJpy9BhM36Vl%2Fi%2FjWlygC%2BTJbJp1%2F%2FnEtR2Shi4fdjZ1sEnM0rJnRh62xyWz%2FqDGIQwYekwtG5FOEBoGAEz9gmgyKlXLngwj5u%2F6sE5f7BPYL7LVWsKU7U%2BO5WyQXeIfCG7w3CDWjqkYuc1Q8O6TOMWIHmkpVzmtLHcc5rGZ8xui9LgT%2FM6DmEpCGcxwPxelXuJoA%2BaDvXB7OfbCVhQu0V%2FGtkFG2uZ9o3D%2F7SHqCRq9h784P22%2BfQYeaMVAjkr5oRRG4KQEhXPduHsPX9WZwuTDFFHPKWW31vxSa0Dl6cPH0ea6L0%2FsJDHu03PZ8jyEn69sbyL1NOYEoZKS2DG%2BY9cns4mbCk668Ph6bIthVZtPOPrw6R%2Frl8SZ6N578kTdYrpLl%2F9T9lbJg8lxDjmsh3VjCfs8NrD7WuMV1aDK7Q5SawZL%2F5s2gWaK7%2B5jJDXc%2F9xoB84V8bF2%2BVZC1FDtpGPVAjcrOkn9ipJ%2BAcMBheJhzvn0eW65UvsuXA43l7Hh7aOxWgWglV8rtyqu%2Fb2g3n4oXTQi6s428LwhJ1e3MOu08LwGOqUBvwwZh%2Bb%2F81pvaH1CfELv0v9jfe941%2B04rdhR%2BxhKLVTy5lnuF9edIXXTF%2BhZKmG7Uu%2BcZqlppAcnJll377DYjENQ2TKHDpTfD8RnZwS7BKN7RkxIhtqaF5mECDLc9Dc5yJ4ImZ7eympo10A0sLPZf53%2FNT%2Bwy%2FIm5ZV%2BA2fon%2FCW4yCCX2Y%2BKsydRFBlhSe7hz6izZIjghK4XEmfb4luAvREw6SI&X-Amz-Signature=7ebd5da9173a0ab699d045dceab62d0c76c9900e7054233770d1ad0bacbcc62a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ENE446%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6nHUb5qze18Yd9enJPj0JoJEC9shoY8pIGXxfDvWWwQIgf1l3JMfzYq9xoxEW67upd%2BPSKKufEjyfaTTkEr%2FGpo0qiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCLKg%2F4mPiAUDK53UircA2jXYQei%2FgHf%2Fx68k9WTIEll2CWnbHO75zgWWK196tK3JEiIeIoybXSrt0J%2F1Vef27MmFWFdwC7CdY4jUA4ToJpy9BhM36Vl%2Fi%2FjWlygC%2BTJbJp1%2F%2FnEtR2Shi4fdjZ1sEnM0rJnRh62xyWz%2FqDGIQwYekwtG5FOEBoGAEz9gmgyKlXLngwj5u%2F6sE5f7BPYL7LVWsKU7U%2BO5WyQXeIfCG7w3CDWjqkYuc1Q8O6TOMWIHmkpVzmtLHcc5rGZ8xui9LgT%2FM6DmEpCGcxwPxelXuJoA%2BaDvXB7OfbCVhQu0V%2FGtkFG2uZ9o3D%2F7SHqCRq9h784P22%2BfQYeaMVAjkr5oRRG4KQEhXPduHsPX9WZwuTDFFHPKWW31vxSa0Dl6cPH0ea6L0%2FsJDHu03PZ8jyEn69sbyL1NOYEoZKS2DG%2BY9cns4mbCk668Ph6bIthVZtPOPrw6R%2Frl8SZ6N578kTdYrpLl%2F9T9lbJg8lxDjmsh3VjCfs8NrD7WuMV1aDK7Q5SawZL%2F5s2gWaK7%2B5jJDXc%2F9xoB84V8bF2%2BVZC1FDtpGPVAjcrOkn9ipJ%2BAcMBheJhzvn0eW65UvsuXA43l7Hh7aOxWgWglV8rtyqu%2Fb2g3n4oXTQi6s428LwhJ1e3MOu08LwGOqUBvwwZh%2Bb%2F81pvaH1CfELv0v9jfe941%2B04rdhR%2BxhKLVTy5lnuF9edIXXTF%2BhZKmG7Uu%2BcZqlppAcnJll377DYjENQ2TKHDpTfD8RnZwS7BKN7RkxIhtqaF5mECDLc9Dc5yJ4ImZ7eympo10A0sLPZf53%2FNT%2Bwy%2FIm5ZV%2BA2fon%2FCW4yCCX2Y%2BKsydRFBlhSe7hz6izZIjghK4XEmfb4luAvREw6SI&X-Amz-Signature=58cd215b60d124e5d36f4370a7ef7c7f4f57b6529c4617998214d0311ea8af2c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ENE446%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6nHUb5qze18Yd9enJPj0JoJEC9shoY8pIGXxfDvWWwQIgf1l3JMfzYq9xoxEW67upd%2BPSKKufEjyfaTTkEr%2FGpo0qiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCLKg%2F4mPiAUDK53UircA2jXYQei%2FgHf%2Fx68k9WTIEll2CWnbHO75zgWWK196tK3JEiIeIoybXSrt0J%2F1Vef27MmFWFdwC7CdY4jUA4ToJpy9BhM36Vl%2Fi%2FjWlygC%2BTJbJp1%2F%2FnEtR2Shi4fdjZ1sEnM0rJnRh62xyWz%2FqDGIQwYekwtG5FOEBoGAEz9gmgyKlXLngwj5u%2F6sE5f7BPYL7LVWsKU7U%2BO5WyQXeIfCG7w3CDWjqkYuc1Q8O6TOMWIHmkpVzmtLHcc5rGZ8xui9LgT%2FM6DmEpCGcxwPxelXuJoA%2BaDvXB7OfbCVhQu0V%2FGtkFG2uZ9o3D%2F7SHqCRq9h784P22%2BfQYeaMVAjkr5oRRG4KQEhXPduHsPX9WZwuTDFFHPKWW31vxSa0Dl6cPH0ea6L0%2FsJDHu03PZ8jyEn69sbyL1NOYEoZKS2DG%2BY9cns4mbCk668Ph6bIthVZtPOPrw6R%2Frl8SZ6N578kTdYrpLl%2F9T9lbJg8lxDjmsh3VjCfs8NrD7WuMV1aDK7Q5SawZL%2F5s2gWaK7%2B5jJDXc%2F9xoB84V8bF2%2BVZC1FDtpGPVAjcrOkn9ipJ%2BAcMBheJhzvn0eW65UvsuXA43l7Hh7aOxWgWglV8rtyqu%2Fb2g3n4oXTQi6s428LwhJ1e3MOu08LwGOqUBvwwZh%2Bb%2F81pvaH1CfELv0v9jfe941%2B04rdhR%2BxhKLVTy5lnuF9edIXXTF%2BhZKmG7Uu%2BcZqlppAcnJll377DYjENQ2TKHDpTfD8RnZwS7BKN7RkxIhtqaF5mECDLc9Dc5yJ4ImZ7eympo10A0sLPZf53%2FNT%2Bwy%2FIm5ZV%2BA2fon%2FCW4yCCX2Y%2BKsydRFBlhSe7hz6izZIjghK4XEmfb4luAvREw6SI&X-Amz-Signature=f947fd3a57cf30603bc932bc24b066af7ad2a78c3659b59be2d6581f6585369c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDICUJ4D%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDD22b%2FwQKtNVWlMX9lWFggL%2FCgqDzGq36%2BoPYe0GBMtQIhANKdotREhS4lHUZbVtmPzv8wf9hjCYsdxWbnNbkymGSRKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb2v671Is2%2B%2BpouSkq3AMe6CWHyDqLumnrRJuQVLgPlBw%2FXSXLDMndyjDBB7gUZ5pECzNI7Vg4NqPBkX2eyyS4jo1QgmRYrZyWBGnB1HacvVv0LvQDqKB%2Bsavli6iakmboMdD8cUiMl1iOqxuwZYI%2BGEe36mdXc4T%2FJ8ljBankyyAB11ooug250wY5XX3O2vRYOoR1PBqsKcmP7e%2BkvVlO3Ql7D82%2BVSBEBGRuMoP%2FMUJwhxmDrE9xIpc95lszETYoNY7JXWty3hyeWSmIHa4XghOSzHdcQy0vjhXkvNUXyD1ITNcOuNfDzWyIwKXL1vQda9xVPZ4qbeCoJouCtBC7LxV07MmJiFbUoycsh139BHe%2B7MhaVI9dpBZ2cYTa1cVegj8Ocs5FFIkAfz1BPS0chV00iG0gXfw60nf3hWVwSBMfODICP%2BvZgqQXoNFBHWBG28bNDg1uAXCH2lFlEtx7EktlyTeQpFN7jctuwZ3gk6z%2FvvJzBqPghKILfHtcp1Gq9BahYN1NUSSYoBzFVqISQRv90l6xtlDPnTk9Hd8OWSHWKF7MbmPfygPZmhv639TnQ7U8NEVQnZTidVptaA1l8h9rszSLtpTjj1zUYpPObo2Fh0HIEAFv857IdEw1Eb4zQVl57o7Zepvs2TDrtPC8BjqkAffheWFaJLniOmp%2B36tuPqCpzKJTeFwoH1fG9MHtpckiWXZOpDfoo%2Fvewtm1DtULFqDMPPFyVHc7TXF0TCFsRrdQ1jFdNxGU8rnwbjiKCXlB9ObLsKe9vvDmUIJGfQRhRVlKeaDsm9vC68LnvIlTRSxhXZYq0k0QvyCO9EBSIdO5dK2bAkcqHBwntNKmXgOQD%2BkiOlmEn54mvpYF9liLrHjK2aT8&X-Amz-Signature=8321008ffaf2528beb2615723acfbebe127c5c47890b7125e09e18af5a9f9ea3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BS5IHNL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAFKPb8ls57HwdosCxnzf64v7kbg9SdwEPEBN%2B8N0wilAiBKhNS3Rqri%2Bjg51vb9%2B920BhZU6L1oBS9mIl8MC5hVlCqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAGRB7H%2F%2Bq2Aj1OG8KtwDUQ9wuIQ2lZVqRvKmtbAPTxFAZc5QCz80J4371nVXOsw4wXx6UoeeTV%2FBjqQ1ryQc7aDftxxXozTgo3KZqaSxoRUtZk5oPyrbYHZcowor%2FkmzcO%2Flhs%2FIKQ4SSKBab3bH%2BSPvYpejg4%2FvapqwumXHBUyWzQWjSrrvEsHbLIsi7LOC93%2F2Zma0YlVBUxTz30fZuqOd%2FhpKkYOWxKI%2FGbQGh0uB1VF5p%2F1mKjKmMtnxQPj%2B%2BBXwXz7bRQx8sjAGWn9FGmgNRX5uToGaC5QXHpM8ql9lmVhHiymYNcc8eIeBXh4yPqVMwBDV57zxN5KAVdvZSGVdRRI1YGfQ6OhStlOF%2FwIQYz4oPJl8y4QuAJWnirvzeSOF5WSLo9MhOdgymGwp%2B07SDFx9GyR5nhBAtHnrrpQlmBAbGhv%2BxhA0oSS3DWi4wKx4ZeXVVQcb2iL6PDCiY%2Buep%2F5ATn6cmrjgSyFkkxq6pJIrqVV28Gv28nMOpBSimQmQrj1BuU7hXSNP%2Bqid4VbyECCWURwYtgm1tVcPivdgEOfRRGo%2FhkOINqBXAOPIi%2FtfrvMIKKi7wU4ZwSIDgZmI4nBF4JiRUNNCKUW7gXcTmpAHETCeskV%2Bl9z%2BSgN6gVSKkNhUljnP%2FLQwqbXwvAY6pgGTGm8VUSEeVtsaSoX7HZlwceLFh51wqMeBSNXchoSw34%2BuOfLadUyAN1PktBTk4EjUltP0MBkGGIm%2Byr17r3SwrLqqMKvI4j7N%2BylXHQIvuZ7AZD%2FwpZUIlzk1%2B5chmg11Sc%2FdRdtwcI0UO5Dj136314Z2BB0xlW9AUJWfORMs0g0gjaBkufVDwAMtHrYWkO6bXfOVxjdIozRSRw%2FK%2BWlMktSI0k0h&X-Amz-Signature=5c45c6fdb43dce2f0f8673f3fc0115aeb95bd1abf5ec07e98c9d3963399ee275&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAQHIU6W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHjj4rRB11MmfDsAgap4tuC9ykAm%2FLwLu6YsjYpIiXEhAiBED%2FUYU62%2Fnez81bJ95i%2Fn5MFVz4NRjq0AtHN4W592aSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDdVHuI2f5TVXhwq3KtwD3biCLRck3%2B4dHeYL52pqLgFbM5vuewrT5juX8FaqlcYY7GLboIl%2BNyJ%2FM%2FcnaCmkA4jhzTHLkquJ48e0vU4Vww1m51rsUjNyMtjadZ%2F2mUmaybqS1%2FZCYe2mGj7ggnv198D78iTYqyEofX8eAO%2BMIUWriqrfwQsT8rLxoivVQhhBHxENwa1fjWQwiUEkjnlXbF6c3Xt9LgHv8YPvsY8YgyPitDtFlWyvXVMmO1%2B2MTGpWQKANRnjeY1ZsRpBaPmEPP%2BA84hht7yfYK2WgR2G%2BqufsOeUJ0tgbquaJ951Q9BZo4Sit4i1vQFF8wVA%2BOWhNZhOJDBUBPc9MD6b8ssEXcX%2Bqd9ynN%2BPS7BPc9MtuGlvScuZQgvdAXJdDsO%2B93OrgOnmOJSweN4P0SwQGe17H6pZF99cOZnY4U%2FY5BhXykbtpUJekjPiFHcjqe3SGkeSk3WEkRdiTAtHURLpq9EqOEBgej3lmKoBZxFSwhk06neCCFSQ%2FSEYBq%2BsPkS0lk2DjNCSxwCPBy9%2F38tZhfvw7GEKF2waWztPC3h%2FFQS8WuWkk3NZWWuN2rDQDDR0vwx97NSQ2J7ZB%2BoYo8FFxeJJ%2BDYpDw8g7mujlTdCHHJENR9RFJT1%2FfDZ1YLs5qMw4bTwvAY6pgFfamugIZO0jrVxAQU9tbzrnMNyhLl2PpdGPAadzTY%2Fl0Scu1I9WtYrngGBHm7HAp9EJowzycznBcSnYtSAB1llRziTpYgD1CCJjhL3qHGO1qGakfm2ONW6sqwbiwXJCeaIzlt6V4hTMvhFdPaMAM61x8ITr6mnM4MK72YXH6vfT51FisUbbjN5JQRmd21xSW7mn33MevL5vF9jeO%2FfKUAS5hw87YxK&X-Amz-Signature=6443da80ec792b50e40ea0cbaba37679b1d702ce3879d79a1025e2d2699e5876&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAQHIU6W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHjj4rRB11MmfDsAgap4tuC9ykAm%2FLwLu6YsjYpIiXEhAiBED%2FUYU62%2Fnez81bJ95i%2Fn5MFVz4NRjq0AtHN4W592aSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDdVHuI2f5TVXhwq3KtwD3biCLRck3%2B4dHeYL52pqLgFbM5vuewrT5juX8FaqlcYY7GLboIl%2BNyJ%2FM%2FcnaCmkA4jhzTHLkquJ48e0vU4Vww1m51rsUjNyMtjadZ%2F2mUmaybqS1%2FZCYe2mGj7ggnv198D78iTYqyEofX8eAO%2BMIUWriqrfwQsT8rLxoivVQhhBHxENwa1fjWQwiUEkjnlXbF6c3Xt9LgHv8YPvsY8YgyPitDtFlWyvXVMmO1%2B2MTGpWQKANRnjeY1ZsRpBaPmEPP%2BA84hht7yfYK2WgR2G%2BqufsOeUJ0tgbquaJ951Q9BZo4Sit4i1vQFF8wVA%2BOWhNZhOJDBUBPc9MD6b8ssEXcX%2Bqd9ynN%2BPS7BPc9MtuGlvScuZQgvdAXJdDsO%2B93OrgOnmOJSweN4P0SwQGe17H6pZF99cOZnY4U%2FY5BhXykbtpUJekjPiFHcjqe3SGkeSk3WEkRdiTAtHURLpq9EqOEBgej3lmKoBZxFSwhk06neCCFSQ%2FSEYBq%2BsPkS0lk2DjNCSxwCPBy9%2F38tZhfvw7GEKF2waWztPC3h%2FFQS8WuWkk3NZWWuN2rDQDDR0vwx97NSQ2J7ZB%2BoYo8FFxeJJ%2BDYpDw8g7mujlTdCHHJENR9RFJT1%2FfDZ1YLs5qMw4bTwvAY6pgFfamugIZO0jrVxAQU9tbzrnMNyhLl2PpdGPAadzTY%2Fl0Scu1I9WtYrngGBHm7HAp9EJowzycznBcSnYtSAB1llRziTpYgD1CCJjhL3qHGO1qGakfm2ONW6sqwbiwXJCeaIzlt6V4hTMvhFdPaMAM61x8ITr6mnM4MK72YXH6vfT51FisUbbjN5JQRmd21xSW7mn33MevL5vF9jeO%2FfKUAS5hw87YxK&X-Amz-Signature=cc24fc8bdc5727caf85c0fab1d328c31d4b799ee90708960e2ebb7d855a3274a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
