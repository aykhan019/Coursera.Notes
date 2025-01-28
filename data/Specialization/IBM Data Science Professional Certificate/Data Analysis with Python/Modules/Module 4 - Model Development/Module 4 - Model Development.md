

# Module 4: Model Development
## Introduction to Model Development
This module delves into the process of model development, focusing on predictive modeling using datasets. It covers various regression techniques, model evaluation methods, and the importance of accurate data in making predictions.
### Key Concepts
#### **1. Simple and Multiple Linear Regression**:
- Use linear regression to predict outcomes based on one or more independent variables.
#### **2. Model Evaluation Using Visualization**:
- Visually assess the performance of models.
#### **3. Polynomial Regression and Pipelines**:
- Employ polynomial regression to capture non-linear relationships and implement pipelines for streamlined model building.
#### **4. R-squared and Mean Squared Error (MSE)**:
- Evaluate model performance using metrics such as R-squared and MSE to determine prediction accuracy.
#### **5. Prediction and Decision Making**:
- Utilize models to make informed predictions and decisions based on the data.
### Importance of Data
A model, or estimator, is essentially a mathematical equation that predicts a value based on one or more other values. It relates one or more independent variables (features) to dependent variables (outcomes). The accuracy of the model often improves with the relevance and quantity of data. Including multiple independent variables can lead to more precise predictions.
For instance, consider a scenario where predicting an outcome is based on several features. If the model's independent variables do not include a crucial feature, predictions may be inaccurate. Therefore, gathering more relevant data and exploring different types of models is cru1cial for robust model development.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SVEMADN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIC0TT3d5C07EPojnvBZEkG4faEujS%2BgvUSdnJYDuF4GqAiAhfNdbSc6hL9MEAQSbIX7eJ7HeGZLQtTDx7dNl9G97eyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMJVAZA8R9%2F0h3BZ5bKtwDBKf0S6Dg718eIGpdrTQ8GiGozhWRtzQ9MjAK0DocsftWvwuefVoW0cuRwg7LmNlbgUaA39xHpNHUVhKCv8HYGn4caAlambkwxz%2FWKX9DBmXaSSHjWNSrOLD%2BpKTdGqr%2BZw6fE9GFTM8GOy%2BZmQzE4Bh1QPam0ykhrfLXfr09qpONIKSvjbMBXMMRou4gQJ%2BZp1RxOgnuYzW1Mv4DVaSPFLBYVtX67ce6fvo%2BHNnuaJD5MxgMUpZlqSVHIT7Gk%2FkXORwPklejKhzvsDjPjuWdOTfwxtjXCv5FG3xnXsFo34xmSr0z8KzxzrDdwUnndWa3AC1heP1ADKyO2NQyehdBic%2Bc53j0f%2BUFZekAp%2BENTPfuQbDXs8bvJWVfb3rOHl%2FYU9n%2BFeXAN4vkE1XFlhlhQkfoI91kQRbFNOAEDr7N%2FIn2uwR6manwc%2BtpUFHSovEZHElJviqU1%2F8B4qKrC2ssEhJXAFkM0KkGKtvirslPF590OtQInxFlY4mTkAEx4AOxB%2F7yrLMTBZohjzmVtNTNXp6oUw6COA6CYfvBk8Jl2ZOEYvosoUedqqUb9YLyYnk4R9MMfwVhJdbqAmEL%2FHKTqJ%2BRkyTesCE6czy8BmUiWvNI%2BaNYpYfni3xAaH0w5rDlvAY6pgHPiDQAfrGibuy1nc0UPW1UpjucX9pluzEry1xETyWLxzbTANHx8fjmTEzVrhFSuXAwEzH4MR0IycaacbpieuCwY%2Bl64FPE6%2BVmVRkr%2BtXoRdJ4B0JQf3Sny8%2BCfmD%2Bb1AKK8DC6JMb4kt330dDAWSMHTISvzrOAA9QCqbeP%2FXMpoxP8%2B5rpScIySZcnHUl%2B%2Ffjr4ugys7HxRIxxPPcDPfgrmRbKxmf&X-Amz-Signature=4c44ffef9e0bf505d8edab373858edde522ae90c859ddd58c161fb0019057544&X-Amz-SignedHeaders=host&x-id=GetObject)
___

## **1. Simple and Multiple Linear Regression**
### Linear Regression
Linear regression predicts a target value using one or more independent variables.
### 1.1 Simple Linear Regression (SLR)
SLR examines the relationship between two variables:
- Predictor (independent variable $ x $)
- Target (dependent variable $ y $)
The relationship is defined as:
$ y = b_0 + b_1 x $
- $ b_0 $: Intercept
- $ b_1  $: Slope
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SVEMADN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIC0TT3d5C07EPojnvBZEkG4faEujS%2BgvUSdnJYDuF4GqAiAhfNdbSc6hL9MEAQSbIX7eJ7HeGZLQtTDx7dNl9G97eyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMJVAZA8R9%2F0h3BZ5bKtwDBKf0S6Dg718eIGpdrTQ8GiGozhWRtzQ9MjAK0DocsftWvwuefVoW0cuRwg7LmNlbgUaA39xHpNHUVhKCv8HYGn4caAlambkwxz%2FWKX9DBmXaSSHjWNSrOLD%2BpKTdGqr%2BZw6fE9GFTM8GOy%2BZmQzE4Bh1QPam0ykhrfLXfr09qpONIKSvjbMBXMMRou4gQJ%2BZp1RxOgnuYzW1Mv4DVaSPFLBYVtX67ce6fvo%2BHNnuaJD5MxgMUpZlqSVHIT7Gk%2FkXORwPklejKhzvsDjPjuWdOTfwxtjXCv5FG3xnXsFo34xmSr0z8KzxzrDdwUnndWa3AC1heP1ADKyO2NQyehdBic%2Bc53j0f%2BUFZekAp%2BENTPfuQbDXs8bvJWVfb3rOHl%2FYU9n%2BFeXAN4vkE1XFlhlhQkfoI91kQRbFNOAEDr7N%2FIn2uwR6manwc%2BtpUFHSovEZHElJviqU1%2F8B4qKrC2ssEhJXAFkM0KkGKtvirslPF590OtQInxFlY4mTkAEx4AOxB%2F7yrLMTBZohjzmVtNTNXp6oUw6COA6CYfvBk8Jl2ZOEYvosoUedqqUb9YLyYnk4R9MMfwVhJdbqAmEL%2FHKTqJ%2BRkyTesCE6czy8BmUiWvNI%2BaNYpYfni3xAaH0w5rDlvAY6pgHPiDQAfrGibuy1nc0UPW1UpjucX9pluzEry1xETyWLxzbTANHx8fjmTEzVrhFSuXAwEzH4MR0IycaacbpieuCwY%2Bl64FPE6%2BVmVRkr%2BtXoRdJ4B0JQf3Sny8%2BCfmD%2Bb1AKK8DC6JMb4kt330dDAWSMHTISvzrOAA9QCqbeP%2FXMpoxP8%2B5rpScIySZcnHUl%2B%2Ffjr4ugys7HxRIxxPPcDPfgrmRbKxmf&X-Amz-Signature=7b1d06b869b5187885e8fa65849b891daad383a5761067ee45e9fc76d2e9a69c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Step
If highway miles per gallon is 20, a linear model might predict the car price as $22,000, assuming a linear relationship.
#### Training the Model
Data points are stored in data frames or NumPy arrays. The predictor values ($ x $) and target values    ($ y $) are stored separately. The model is trained using these data points to determine the parameters $ b_0 $ and .
#### Handling Uncertainty
Factors like car make and age influence car prices. Uncertainty in the model is addressed by adding a small random value (noise) to the line. The noise is usually a small positive or negative value.
#### Python Implementation
```python
from sklearn.linear_model import LinearRegression

# Create a linear regression object
lm = LinearRegression()

# Define predictor (x) and target (y) variables
x = ...
y = ...

# Fit the model
lm.fit(x, y)

# Make predictions
predicted_values = lm.predict(x)

# Model parameters
intercept = lm.intercept_
slope = lm.coef_
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SVEMADN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIC0TT3d5C07EPojnvBZEkG4faEujS%2BgvUSdnJYDuF4GqAiAhfNdbSc6hL9MEAQSbIX7eJ7HeGZLQtTDx7dNl9G97eyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMJVAZA8R9%2F0h3BZ5bKtwDBKf0S6Dg718eIGpdrTQ8GiGozhWRtzQ9MjAK0DocsftWvwuefVoW0cuRwg7LmNlbgUaA39xHpNHUVhKCv8HYGn4caAlambkwxz%2FWKX9DBmXaSSHjWNSrOLD%2BpKTdGqr%2BZw6fE9GFTM8GOy%2BZmQzE4Bh1QPam0ykhrfLXfr09qpONIKSvjbMBXMMRou4gQJ%2BZp1RxOgnuYzW1Mv4DVaSPFLBYVtX67ce6fvo%2BHNnuaJD5MxgMUpZlqSVHIT7Gk%2FkXORwPklejKhzvsDjPjuWdOTfwxtjXCv5FG3xnXsFo34xmSr0z8KzxzrDdwUnndWa3AC1heP1ADKyO2NQyehdBic%2Bc53j0f%2BUFZekAp%2BENTPfuQbDXs8bvJWVfb3rOHl%2FYU9n%2BFeXAN4vkE1XFlhlhQkfoI91kQRbFNOAEDr7N%2FIn2uwR6manwc%2BtpUFHSovEZHElJviqU1%2F8B4qKrC2ssEhJXAFkM0KkGKtvirslPF590OtQInxFlY4mTkAEx4AOxB%2F7yrLMTBZohjzmVtNTNXp6oUw6COA6CYfvBk8Jl2ZOEYvosoUedqqUb9YLyYnk4R9MMfwVhJdbqAmEL%2FHKTqJ%2BRkyTesCE6czy8BmUiWvNI%2BaNYpYfni3xAaH0w5rDlvAY6pgHPiDQAfrGibuy1nc0UPW1UpjucX9pluzEry1xETyWLxzbTANHx8fjmTEzVrhFSuXAwEzH4MR0IycaacbpieuCwY%2Bl64FPE6%2BVmVRkr%2BtXoRdJ4B0JQf3Sny8%2BCfmD%2Bb1AKK8DC6JMb4kt330dDAWSMHTISvzrOAA9QCqbeP%2FXMpoxP8%2B5rpScIySZcnHUl%2B%2Ffjr4ugys7HxRIxxPPcDPfgrmRbKxmf&X-Amz-Signature=fc0001faf022ccb024001088d1f0f307263f64d92ada30caaff0fb703a0d4b3e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SVEMADN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIC0TT3d5C07EPojnvBZEkG4faEujS%2BgvUSdnJYDuF4GqAiAhfNdbSc6hL9MEAQSbIX7eJ7HeGZLQtTDx7dNl9G97eyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMJVAZA8R9%2F0h3BZ5bKtwDBKf0S6Dg718eIGpdrTQ8GiGozhWRtzQ9MjAK0DocsftWvwuefVoW0cuRwg7LmNlbgUaA39xHpNHUVhKCv8HYGn4caAlambkwxz%2FWKX9DBmXaSSHjWNSrOLD%2BpKTdGqr%2BZw6fE9GFTM8GOy%2BZmQzE4Bh1QPam0ykhrfLXfr09qpONIKSvjbMBXMMRou4gQJ%2BZp1RxOgnuYzW1Mv4DVaSPFLBYVtX67ce6fvo%2BHNnuaJD5MxgMUpZlqSVHIT7Gk%2FkXORwPklejKhzvsDjPjuWdOTfwxtjXCv5FG3xnXsFo34xmSr0z8KzxzrDdwUnndWa3AC1heP1ADKyO2NQyehdBic%2Bc53j0f%2BUFZekAp%2BENTPfuQbDXs8bvJWVfb3rOHl%2FYU9n%2BFeXAN4vkE1XFlhlhQkfoI91kQRbFNOAEDr7N%2FIn2uwR6manwc%2BtpUFHSovEZHElJviqU1%2F8B4qKrC2ssEhJXAFkM0KkGKtvirslPF590OtQInxFlY4mTkAEx4AOxB%2F7yrLMTBZohjzmVtNTNXp6oUw6COA6CYfvBk8Jl2ZOEYvosoUedqqUb9YLyYnk4R9MMfwVhJdbqAmEL%2FHKTqJ%2BRkyTesCE6czy8BmUiWvNI%2BaNYpYfni3xAaH0w5rDlvAY6pgHPiDQAfrGibuy1nc0UPW1UpjucX9pluzEry1xETyWLxzbTANHx8fjmTEzVrhFSuXAwEzH4MR0IycaacbpieuCwY%2Bl64FPE6%2BVmVRkr%2BtXoRdJ4B0JQf3Sny8%2BCfmD%2Bb1AKK8DC6JMb4kt330dDAWSMHTISvzrOAA9QCqbeP%2FXMpoxP8%2B5rpScIySZcnHUl%2B%2Ffjr4ugys7HxRIxxPPcDPfgrmRbKxmf&X-Amz-Signature=a135c550735e0f4e0aa1bb6d334b39467062c34258ae8a89ab2a672470e7da17&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Visualization and Training
With two predictor variables ($ x_1 $ and ), data points are mapped on a 2D plane, and () values are mapped vertically.
#### Python Implementation
```python
from sklearn.linear_model import LinearRegression

# Create a linear regression object
lm = LinearRegression()

# Define predictor variables (z) and target (y)
z = ...
y = ...

# Fit the model
lm.fit(z, y)

# Make predictions
predicted_values = lm.predict(z)

# Model parameters
intercept = lm.intercept_
coefficients = lm.coef_
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SVEMADN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIC0TT3d5C07EPojnvBZEkG4faEujS%2BgvUSdnJYDuF4GqAiAhfNdbSc6hL9MEAQSbIX7eJ7HeGZLQtTDx7dNl9G97eyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMJVAZA8R9%2F0h3BZ5bKtwDBKf0S6Dg718eIGpdrTQ8GiGozhWRtzQ9MjAK0DocsftWvwuefVoW0cuRwg7LmNlbgUaA39xHpNHUVhKCv8HYGn4caAlambkwxz%2FWKX9DBmXaSSHjWNSrOLD%2BpKTdGqr%2BZw6fE9GFTM8GOy%2BZmQzE4Bh1QPam0ykhrfLXfr09qpONIKSvjbMBXMMRou4gQJ%2BZp1RxOgnuYzW1Mv4DVaSPFLBYVtX67ce6fvo%2BHNnuaJD5MxgMUpZlqSVHIT7Gk%2FkXORwPklejKhzvsDjPjuWdOTfwxtjXCv5FG3xnXsFo34xmSr0z8KzxzrDdwUnndWa3AC1heP1ADKyO2NQyehdBic%2Bc53j0f%2BUFZekAp%2BENTPfuQbDXs8bvJWVfb3rOHl%2FYU9n%2BFeXAN4vkE1XFlhlhQkfoI91kQRbFNOAEDr7N%2FIn2uwR6manwc%2BtpUFHSovEZHElJviqU1%2F8B4qKrC2ssEhJXAFkM0KkGKtvirslPF590OtQInxFlY4mTkAEx4AOxB%2F7yrLMTBZohjzmVtNTNXp6oUw6COA6CYfvBk8Jl2ZOEYvosoUedqqUb9YLyYnk4R9MMfwVhJdbqAmEL%2FHKTqJ%2BRkyTesCE6czy8BmUiWvNI%2BaNYpYfni3xAaH0w5rDlvAY6pgHPiDQAfrGibuy1nc0UPW1UpjucX9pluzEry1xETyWLxzbTANHx8fjmTEzVrhFSuXAwEzH4MR0IycaacbpieuCwY%2Bl64FPE6%2BVmVRkr%2BtXoRdJ4B0JQf3Sny8%2BCfmD%2Bb1AKK8DC6JMb4kt330dDAWSMHTISvzrOAA9QCqbeP%2FXMpoxP8%2B5rpScIySZcnHUl%2B%2Ffjr4ugys7HxRIxxPPcDPfgrmRbKxmf&X-Amz-Signature=4058fe326ee5f9ad5515ae4b385788eb176e5296ee2de6680cecb8b5515efe04&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SVEMADN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIC0TT3d5C07EPojnvBZEkG4faEujS%2BgvUSdnJYDuF4GqAiAhfNdbSc6hL9MEAQSbIX7eJ7HeGZLQtTDx7dNl9G97eyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMJVAZA8R9%2F0h3BZ5bKtwDBKf0S6Dg718eIGpdrTQ8GiGozhWRtzQ9MjAK0DocsftWvwuefVoW0cuRwg7LmNlbgUaA39xHpNHUVhKCv8HYGn4caAlambkwxz%2FWKX9DBmXaSSHjWNSrOLD%2BpKTdGqr%2BZw6fE9GFTM8GOy%2BZmQzE4Bh1QPam0ykhrfLXfr09qpONIKSvjbMBXMMRou4gQJ%2BZp1RxOgnuYzW1Mv4DVaSPFLBYVtX67ce6fvo%2BHNnuaJD5MxgMUpZlqSVHIT7Gk%2FkXORwPklejKhzvsDjPjuWdOTfwxtjXCv5FG3xnXsFo34xmSr0z8KzxzrDdwUnndWa3AC1heP1ADKyO2NQyehdBic%2Bc53j0f%2BUFZekAp%2BENTPfuQbDXs8bvJWVfb3rOHl%2FYU9n%2BFeXAN4vkE1XFlhlhQkfoI91kQRbFNOAEDr7N%2FIn2uwR6manwc%2BtpUFHSovEZHElJviqU1%2F8B4qKrC2ssEhJXAFkM0KkGKtvirslPF590OtQInxFlY4mTkAEx4AOxB%2F7yrLMTBZohjzmVtNTNXp6oUw6COA6CYfvBk8Jl2ZOEYvosoUedqqUb9YLyYnk4R9MMfwVhJdbqAmEL%2FHKTqJ%2BRkyTesCE6czy8BmUiWvNI%2BaNYpYfni3xAaH0w5rDlvAY6pgHPiDQAfrGibuy1nc0UPW1UpjucX9pluzEry1xETyWLxzbTANHx8fjmTEzVrhFSuXAwEzH4MR0IycaacbpieuCwY%2Bl64FPE6%2BVmVRkr%2BtXoRdJ4B0JQf3Sny8%2BCfmD%2Bb1AKK8DC6JMb4kt330dDAWSMHTISvzrOAA9QCqbeP%2FXMpoxP8%2B5rpScIySZcnHUl%2B%2Ffjr4ugys7HxRIxxPPcDPfgrmRbKxmf&X-Amz-Signature=03a16f8654d5450830e702080b9c08b18890f394747f09d1bbb2a81ad86afb95&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 2. Model Evaluation Using Visualization
### 1. Regression Plots
Regression plots estimate the relationship between two variables, showing the strength and direction of the correlation.
- **Horizontal Axis**: Independent variable.
- **Vertical Axis**: Dependent variable.
- **Points**: Represent different target points.
- **Fitted Line**: Represents predicted values.
#### Creating a Regression Plot
1. **Import Seaborn**:
```python
import seaborn as sns
```
2. **Use **`**regplot**`** Function**:
	- **Parameters**:
		- `x`: Independent variable column.
		- `y`: Dependent variable column.
		- `data`: Name of the DataFrame.
```python
sns.regplot(x='feature', y='target', data=df)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SVEMADN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIC0TT3d5C07EPojnvBZEkG4faEujS%2BgvUSdnJYDuF4GqAiAhfNdbSc6hL9MEAQSbIX7eJ7HeGZLQtTDx7dNl9G97eyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMJVAZA8R9%2F0h3BZ5bKtwDBKf0S6Dg718eIGpdrTQ8GiGozhWRtzQ9MjAK0DocsftWvwuefVoW0cuRwg7LmNlbgUaA39xHpNHUVhKCv8HYGn4caAlambkwxz%2FWKX9DBmXaSSHjWNSrOLD%2BpKTdGqr%2BZw6fE9GFTM8GOy%2BZmQzE4Bh1QPam0ykhrfLXfr09qpONIKSvjbMBXMMRou4gQJ%2BZp1RxOgnuYzW1Mv4DVaSPFLBYVtX67ce6fvo%2BHNnuaJD5MxgMUpZlqSVHIT7Gk%2FkXORwPklejKhzvsDjPjuWdOTfwxtjXCv5FG3xnXsFo34xmSr0z8KzxzrDdwUnndWa3AC1heP1ADKyO2NQyehdBic%2Bc53j0f%2BUFZekAp%2BENTPfuQbDXs8bvJWVfb3rOHl%2FYU9n%2BFeXAN4vkE1XFlhlhQkfoI91kQRbFNOAEDr7N%2FIn2uwR6manwc%2BtpUFHSovEZHElJviqU1%2F8B4qKrC2ssEhJXAFkM0KkGKtvirslPF590OtQInxFlY4mTkAEx4AOxB%2F7yrLMTBZohjzmVtNTNXp6oUw6COA6CYfvBk8Jl2ZOEYvosoUedqqUb9YLyYnk4R9MMfwVhJdbqAmEL%2FHKTqJ%2BRkyTesCE6czy8BmUiWvNI%2BaNYpYfni3xAaH0w5rDlvAY6pgHPiDQAfrGibuy1nc0UPW1UpjucX9pluzEry1xETyWLxzbTANHx8fjmTEzVrhFSuXAwEzH4MR0IycaacbpieuCwY%2Bl64FPE6%2BVmVRkr%2BtXoRdJ4B0JQf3Sny8%2BCfmD%2Bb1AKK8DC6JMb4kt330dDAWSMHTISvzrOAA9QCqbeP%2FXMpoxP8%2B5rpScIySZcnHUl%2B%2Ffjr4ugys7HxRIxxPPcDPfgrmRbKxmf&X-Amz-Signature=7941c357b52094a47e3100d5c8948962e6a6e680a234cafb062961a0f059b662&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. Residual Plots
Residual plots represent the error between actual and predicted values.
- **Process**:
	- Subtract predicted value from actual target value.
	- Plot the error on the vertical axis, dependent variable on the horizontal axis.
- **Insights**:
	- Zero mean distributed evenly around the x-axis indicates a linear model.
	- Curvature in residuals suggests a nonlinear model.
#### Creating a Residual Plot
3. **Import Seaborn**:
```python
import seaborn as sns
```
4. **Use **`**residplot**`** Function**:
	- **Parameters**:
		- Series of dependent variable (feature).
		- Series of target variable.
```python
sns.residplot(x='feature', y='target', data=df)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SVEMADN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIC0TT3d5C07EPojnvBZEkG4faEujS%2BgvUSdnJYDuF4GqAiAhfNdbSc6hL9MEAQSbIX7eJ7HeGZLQtTDx7dNl9G97eyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMJVAZA8R9%2F0h3BZ5bKtwDBKf0S6Dg718eIGpdrTQ8GiGozhWRtzQ9MjAK0DocsftWvwuefVoW0cuRwg7LmNlbgUaA39xHpNHUVhKCv8HYGn4caAlambkwxz%2FWKX9DBmXaSSHjWNSrOLD%2BpKTdGqr%2BZw6fE9GFTM8GOy%2BZmQzE4Bh1QPam0ykhrfLXfr09qpONIKSvjbMBXMMRou4gQJ%2BZp1RxOgnuYzW1Mv4DVaSPFLBYVtX67ce6fvo%2BHNnuaJD5MxgMUpZlqSVHIT7Gk%2FkXORwPklejKhzvsDjPjuWdOTfwxtjXCv5FG3xnXsFo34xmSr0z8KzxzrDdwUnndWa3AC1heP1ADKyO2NQyehdBic%2Bc53j0f%2BUFZekAp%2BENTPfuQbDXs8bvJWVfb3rOHl%2FYU9n%2BFeXAN4vkE1XFlhlhQkfoI91kQRbFNOAEDr7N%2FIn2uwR6manwc%2BtpUFHSovEZHElJviqU1%2F8B4qKrC2ssEhJXAFkM0KkGKtvirslPF590OtQInxFlY4mTkAEx4AOxB%2F7yrLMTBZohjzmVtNTNXp6oUw6COA6CYfvBk8Jl2ZOEYvosoUedqqUb9YLyYnk4R9MMfwVhJdbqAmEL%2FHKTqJ%2BRkyTesCE6czy8BmUiWvNI%2BaNYpYfni3xAaH0w5rDlvAY6pgHPiDQAfrGibuy1nc0UPW1UpjucX9pluzEry1xETyWLxzbTANHx8fjmTEzVrhFSuXAwEzH4MR0IycaacbpieuCwY%2Bl64FPE6%2BVmVRkr%2BtXoRdJ4B0JQf3Sny8%2BCfmD%2Bb1AKK8DC6JMb4kt330dDAWSMHTISvzrOAA9QCqbeP%2FXMpoxP8%2B5rpScIySZcnHUl%2B%2Ffjr4ugys7HxRIxxPPcDPfgrmRbKxmf&X-Amz-Signature=defbdbf726487f31e3e94582fae9e8c214dc6b8b69b32f0b601ed4b0fa045100&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SVEMADN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIC0TT3d5C07EPojnvBZEkG4faEujS%2BgvUSdnJYDuF4GqAiAhfNdbSc6hL9MEAQSbIX7eJ7HeGZLQtTDx7dNl9G97eyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMJVAZA8R9%2F0h3BZ5bKtwDBKf0S6Dg718eIGpdrTQ8GiGozhWRtzQ9MjAK0DocsftWvwuefVoW0cuRwg7LmNlbgUaA39xHpNHUVhKCv8HYGn4caAlambkwxz%2FWKX9DBmXaSSHjWNSrOLD%2BpKTdGqr%2BZw6fE9GFTM8GOy%2BZmQzE4Bh1QPam0ykhrfLXfr09qpONIKSvjbMBXMMRou4gQJ%2BZp1RxOgnuYzW1Mv4DVaSPFLBYVtX67ce6fvo%2BHNnuaJD5MxgMUpZlqSVHIT7Gk%2FkXORwPklejKhzvsDjPjuWdOTfwxtjXCv5FG3xnXsFo34xmSr0z8KzxzrDdwUnndWa3AC1heP1ADKyO2NQyehdBic%2Bc53j0f%2BUFZekAp%2BENTPfuQbDXs8bvJWVfb3rOHl%2FYU9n%2BFeXAN4vkE1XFlhlhQkfoI91kQRbFNOAEDr7N%2FIn2uwR6manwc%2BtpUFHSovEZHElJviqU1%2F8B4qKrC2ssEhJXAFkM0KkGKtvirslPF590OtQInxFlY4mTkAEx4AOxB%2F7yrLMTBZohjzmVtNTNXp6oUw6COA6CYfvBk8Jl2ZOEYvosoUedqqUb9YLyYnk4R9MMfwVhJdbqAmEL%2FHKTqJ%2BRkyTesCE6czy8BmUiWvNI%2BaNYpYfni3xAaH0w5rDlvAY6pgHPiDQAfrGibuy1nc0UPW1UpjucX9pluzEry1xETyWLxzbTANHx8fjmTEzVrhFSuXAwEzH4MR0IycaacbpieuCwY%2Bl64FPE6%2BVmVRkr%2BtXoRdJ4B0JQf3Sny8%2BCfmD%2Bb1AKK8DC6JMb4kt330dDAWSMHTISvzrOAA9QCqbeP%2FXMpoxP8%2B5rpScIySZcnHUl%2B%2Ffjr4ugys7HxRIxxPPcDPfgrmRbKxmf&X-Amz-Signature=37989e2948725bebe3c4c8184795e6c7f2266a8bf8c4b20959a4e4ecb646bf0c&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Distribution Plots
Distribution plots visualize predicted versus actual values.
- **Use**: Helpful for models with multiple independent variables.
#### Process
- Count and plot the predicted points approximately equal to a target value.
- Repeat for various target values.
#### Creating a Distribution Plot
5. **Import Pandas** and **Seaborn**:
```python
import pandas as pd
import seaborn as sns
```
6. **Use Seaborn's Distribution Plot**:
	- **Parameters**:
		- `hist`: Set to `False` for a distribution.
		- `color`: Set to desired color.
		- `label`: Include label for legend.
```python
sns.kdeplot(predicted_values, color='blue', label='Predicted')
sns.kdeplot(actual_values, color='red', label='Actual')
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SVEMADN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIC0TT3d5C07EPojnvBZEkG4faEujS%2BgvUSdnJYDuF4GqAiAhfNdbSc6hL9MEAQSbIX7eJ7HeGZLQtTDx7dNl9G97eyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMJVAZA8R9%2F0h3BZ5bKtwDBKf0S6Dg718eIGpdrTQ8GiGozhWRtzQ9MjAK0DocsftWvwuefVoW0cuRwg7LmNlbgUaA39xHpNHUVhKCv8HYGn4caAlambkwxz%2FWKX9DBmXaSSHjWNSrOLD%2BpKTdGqr%2BZw6fE9GFTM8GOy%2BZmQzE4Bh1QPam0ykhrfLXfr09qpONIKSvjbMBXMMRou4gQJ%2BZp1RxOgnuYzW1Mv4DVaSPFLBYVtX67ce6fvo%2BHNnuaJD5MxgMUpZlqSVHIT7Gk%2FkXORwPklejKhzvsDjPjuWdOTfwxtjXCv5FG3xnXsFo34xmSr0z8KzxzrDdwUnndWa3AC1heP1ADKyO2NQyehdBic%2Bc53j0f%2BUFZekAp%2BENTPfuQbDXs8bvJWVfb3rOHl%2FYU9n%2BFeXAN4vkE1XFlhlhQkfoI91kQRbFNOAEDr7N%2FIn2uwR6manwc%2BtpUFHSovEZHElJviqU1%2F8B4qKrC2ssEhJXAFkM0KkGKtvirslPF590OtQInxFlY4mTkAEx4AOxB%2F7yrLMTBZohjzmVtNTNXp6oUw6COA6CYfvBk8Jl2ZOEYvosoUedqqUb9YLyYnk4R9MMfwVhJdbqAmEL%2FHKTqJ%2BRkyTesCE6czy8BmUiWvNI%2BaNYpYfni3xAaH0w5rDlvAY6pgHPiDQAfrGibuy1nc0UPW1UpjucX9pluzEry1xETyWLxzbTANHx8fjmTEzVrhFSuXAwEzH4MR0IycaacbpieuCwY%2Bl64FPE6%2BVmVRkr%2BtXoRdJ4B0JQf3Sny8%2BCfmD%2Bb1AKK8DC6JMb4kt330dDAWSMHTISvzrOAA9QCqbeP%2FXMpoxP8%2B5rpScIySZcnHUl%2B%2Ffjr4ugys7HxRIxxPPcDPfgrmRbKxmf&X-Amz-Signature=f73f43bb40a5fc66e09223c8d7235c67523807c725eca9a3dfdf9f16296ff916&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SVEMADN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIC0TT3d5C07EPojnvBZEkG4faEujS%2BgvUSdnJYDuF4GqAiAhfNdbSc6hL9MEAQSbIX7eJ7HeGZLQtTDx7dNl9G97eyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMJVAZA8R9%2F0h3BZ5bKtwDBKf0S6Dg718eIGpdrTQ8GiGozhWRtzQ9MjAK0DocsftWvwuefVoW0cuRwg7LmNlbgUaA39xHpNHUVhKCv8HYGn4caAlambkwxz%2FWKX9DBmXaSSHjWNSrOLD%2BpKTdGqr%2BZw6fE9GFTM8GOy%2BZmQzE4Bh1QPam0ykhrfLXfr09qpONIKSvjbMBXMMRou4gQJ%2BZp1RxOgnuYzW1Mv4DVaSPFLBYVtX67ce6fvo%2BHNnuaJD5MxgMUpZlqSVHIT7Gk%2FkXORwPklejKhzvsDjPjuWdOTfwxtjXCv5FG3xnXsFo34xmSr0z8KzxzrDdwUnndWa3AC1heP1ADKyO2NQyehdBic%2Bc53j0f%2BUFZekAp%2BENTPfuQbDXs8bvJWVfb3rOHl%2FYU9n%2BFeXAN4vkE1XFlhlhQkfoI91kQRbFNOAEDr7N%2FIn2uwR6manwc%2BtpUFHSovEZHElJviqU1%2F8B4qKrC2ssEhJXAFkM0KkGKtvirslPF590OtQInxFlY4mTkAEx4AOxB%2F7yrLMTBZohjzmVtNTNXp6oUw6COA6CYfvBk8Jl2ZOEYvosoUedqqUb9YLyYnk4R9MMfwVhJdbqAmEL%2FHKTqJ%2BRkyTesCE6czy8BmUiWvNI%2BaNYpYfni3xAaH0w5rDlvAY6pgHPiDQAfrGibuy1nc0UPW1UpjucX9pluzEry1xETyWLxzbTANHx8fjmTEzVrhFSuXAwEzH4MR0IycaacbpieuCwY%2Bl64FPE6%2BVmVRkr%2BtXoRdJ4B0JQf3Sny8%2BCfmD%2Bb1AKK8DC6JMb4kt330dDAWSMHTISvzrOAA9QCqbeP%2FXMpoxP8%2B5rpScIySZcnHUl%2B%2Ffjr4ugys7HxRIxxPPcDPfgrmRbKxmf&X-Amz-Signature=e6a8a77ffe94f7d57ce5fcdf16059be8ca16db4438ce1c55584dc8db87232455&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Types of Polynomial Models
- **Quadratic (2nd Order)**: Includes squared terms.
- **Cubic (3rd Order)**: Includes cubed terms.
- **Higher-Order**: Used for complex relationships.
#### Example Model
- **3rd Order Polynomial**:
$$ −1.557x^3+204.8x^2+8965x+1.37×105 $$
#### Implementation in Python
- **Using NumPy**:
```python
import numpy as np
coefficients = np.polyfit(x, y, 3)
```
- **For Multidimensional**:
Use `scikit-learn` for more complex models.
#### Polynomial Features with Scikit-learn
7. **Import the Library**:
```python
from sklearn.preprocessing import PolynomialFeatures
```
8. **Create Polynomial Features**:
```python
from sklearn.linear_model import LinearRegression

# Create a PolynomialFeatures object with the desired degree
poly = PolynomialFeatures(degree=3)

# Fit and transform your data
X_poly = poly.fit_transform(X)

# Create LinearRegression model
model = LinearRegression()

# Fit the model with the polynomial features
model.fit(X_poly, y)
```
In this code:
- `degree=3` specifies the degree of the polynomial features.
- `fit_transform(X)` generates the polynomial features for your dataset `X`.
### Normalization
#### Why Normalize?
- **Purpose**: Standardize data for better model performance.
#### How to Normalize
- **Using StandardScaler**:
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
```
### Pipelines
#### What are Pipelines?
- **Purpose**: Efficiently automate data preprocessing and model training.
- **Benefit**: Simplifies complex workflows by chaining multiple steps into a single process.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UH7JSDL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQDlgI3YKGxVHBUdqMPSNcg53AcgZp0zARP2v5Etfj1WAwIhAP9Bh4v3gveHTEHW%2Fq2AZQ9iZ9g%2FtcFAsnDUeKi%2FvSdZKv8DCH8QABoMNjM3NDIzMTgzODA1Igy8c8KQf1ynPv%2FOQiYq3AOgB%2BObqCpXHgjqjjOWcbG4ib5WEyApvahFNxC8UgT9dU8ffmJ%2FK44TZyZ9gmZ9R%2FcjxKbF89%2FlwtrFeI5sMxS39YmCl0juP6g5lHt0UBbC%2FguZ1gTkPFU90O%2Bd4i2fg9IdtQQJu1Yzh9e1DvjVzQ7w0QcpflRX4VFX1fhB9D4LNu%2B5BtqTfgSt%2F0HzSM%2FrHUcFPezC%2FDgpur3vEJlmd0XCf01fi9TctrUEipTuCYJszfou3qxOF4r1g30ce368nus6MOpi5659gbz0VvA3xgukJs7shZ8aBHIWZlUlCv52NDlzCcrPt9cDIj6GQTnn1FNAtUph3L51ds%2Bu42%2FBDVFJzwJTKE%2FiNZUwu5VFrCNWT46gxkBrBB4mizyy54gf39tFWOIGZvsWJap4UIqVgSEB%2BB86KFlG2%2B5mRxLOhXMRh7u7FR13ZjFnEYRos0IA4B%2BwvGAVds%2BMWvX6iH5G8hwfOaMsNK06S3UakVhICQBrXmRdq0H7JBAU52%2FPUguogUqxPE6uHH%2Fvqr%2Bh9xkuz%2B0BJMhZqOJ0eZYqn%2FI4485FuC4fZt6lnwsYwko3pXcQWIyovY8e7TOeb7TlfFe2rXKspfxvhBGB21UDxiSEKdgwUIYuDabpLlRfSNCglTDrsOW8BjqkAbVKHT5PpqeIzc76YwZHJs3mJbouC2%2F1DKz4cApB%2B4y69%2BH07kq5xywb75y5ds0nRr5JlQwHbMN6tPPeKRR0BwFR8tO9hGkG%2BdzFrpX4FQa4uNiIMifPv4q3Aot9wln8Z8GriRKaWIeb3Wl6tb61QC4PG1k5ioeTeIoa8CFidbV9l17nEidR8IAba%2Fxe%2Bg%2FSu7FcYk9WGC5qRFVwNa2Q8tKdf1Lm&X-Amz-Signature=0df164a9e9b9ffc4310399374ce6111ceccc1ff293afc2231272023723dd06e8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Benefits
- **Efficiency**: Simplifies code by chaining steps.
- **Maintainability**: Makes workflow clearer.
#### Creating a Pipeline
9. **Import Pipeline**:
```python
from sklearn.pipeline import Pipeline
```
10. **Define Steps**:
```python
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('poly', PolynomialFeatures(degree=3)),
    ('model', LinearRegression())
])
```
11. **Train and Predict**:
```python
pipeline.fit(x_train, y_train)
y_pred = pipeline.predict(x_test)
```
#### Key Points
- **Sequential Processing**: Automates the flow from preprocessing to prediction.
- **Versatile**: Easily adjust steps and parameters.
Use polynomial regression and pipelines to enhance model accuracy and streamline your machine learning workflow.

### Note:
#### Simple Linear Regression (SLR)
- **Definition**: Models the relationship between two variables by fitting a linear equation.
- **Equation**: $ y = b_0 + b_1x $
- **Use Case**: One independent variable predicts a dependent variable.
#### Multiple Linear Regression (MLR)
- **Definition**: Extends SLR to include multiple independent variables.
- **Equation**: $ y=b_0+b_1x_1+b_2x_2+…+b_nx_n $
- **Use Case**: Accounts for multiple factors affecting the outcome.
#### Polynomial Regression
- **Definition**: A form of regression where the relationship is modeled as an nth degree polynomial.
- **Equation**: $ y = b_0 + b_1x + b_2x^2 + \ldots + b_nx^n $
- **Use Case**: Captures non-linear relationships by transforming features.
#### Key Differences
- **SLR**: Linear relationship with one predictor.
- **MLR**: Linear relationships with multiple predictors.
- **Polynomial Regression**: Non-linear relationships using polynomial terms.
#### Example Code
```python
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Simple Linear Regression
X_slr = np.array([[20], [30], [40]])
y_slr = np.array([15000, 13000, 12000])

model_slr = LinearRegression()
model_slr.fit(X_slr, y_slr)
predicted_slr = model_slr.predict([[30]])
print("SLR Predicted Price:", predicted_slr[0])

# Multiple Linear Regression
X_mlr = np.array([[20, 5], [30, 4], [40, 6]])
y_mlr = np.array([15000, 13000, 12000])

model_mlr = LinearRegression()
model_mlr.fit(X_mlr, y_mlr)
predicted_mlr = model_mlr.predict([[30, 5]])
print("MLR Predicted Price:", predicted_mlr[0])

# Polynomial Regression
X_poly = np.array([[20], [30], [40]])
y_poly = np.array([15000, 13000, 12000])

poly = PolynomialFeatures(degree=2)
X_poly_transformed = poly.fit_transform(X_poly)

model_poly = LinearRegression()
model_poly.fit(X_poly_transformed, y_poly)
predicted_poly = model_poly.predict(poly.transform([[30]]))
print("Polynomial Predicted Price:", predicted_poly[0])
```
___
## 4. Model Evaluation Metrics
### Mean Squared Error (MSE)
- **Definition**: Measures the average squared difference between actual and predicted values. It indicates how close predictions are to the actual values.
- **Formula**: $  \text{MSE} = \frac{1}{n} \sum (y - \hat{y})^2 $
- **Python**: Use `mean_squared_error` from `sklearn.metrics`.
#### Example
**Scenario**: Predicting house prices based on size.
- **Actual Prices**: [200, 250, 300]
- **Predicted Prices**: [210, 240, 310]
**Calculation**:
$ \text{MSE} = \frac{1}{3} ((200-210)^2 + (250-240)^2 + (300-310)^2) = \frac{1}{3} (100 + 100 + 100) = 100
 $
**Python Code**:
```python
from sklearn.metrics import mean_squared_error

actual = [200, 250, 300]
predicted = [210, 240, 310]
mse = mean_squared_error(actual, predicted)
print("MSE:", mse)  # Output: MSE: 100.0
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UH7JSDL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQDlgI3YKGxVHBUdqMPSNcg53AcgZp0zARP2v5Etfj1WAwIhAP9Bh4v3gveHTEHW%2Fq2AZQ9iZ9g%2FtcFAsnDUeKi%2FvSdZKv8DCH8QABoMNjM3NDIzMTgzODA1Igy8c8KQf1ynPv%2FOQiYq3AOgB%2BObqCpXHgjqjjOWcbG4ib5WEyApvahFNxC8UgT9dU8ffmJ%2FK44TZyZ9gmZ9R%2FcjxKbF89%2FlwtrFeI5sMxS39YmCl0juP6g5lHt0UBbC%2FguZ1gTkPFU90O%2Bd4i2fg9IdtQQJu1Yzh9e1DvjVzQ7w0QcpflRX4VFX1fhB9D4LNu%2B5BtqTfgSt%2F0HzSM%2FrHUcFPezC%2FDgpur3vEJlmd0XCf01fi9TctrUEipTuCYJszfou3qxOF4r1g30ce368nus6MOpi5659gbz0VvA3xgukJs7shZ8aBHIWZlUlCv52NDlzCcrPt9cDIj6GQTnn1FNAtUph3L51ds%2Bu42%2FBDVFJzwJTKE%2FiNZUwu5VFrCNWT46gxkBrBB4mizyy54gf39tFWOIGZvsWJap4UIqVgSEB%2BB86KFlG2%2B5mRxLOhXMRh7u7FR13ZjFnEYRos0IA4B%2BwvGAVds%2BMWvX6iH5G8hwfOaMsNK06S3UakVhICQBrXmRdq0H7JBAU52%2FPUguogUqxPE6uHH%2Fvqr%2Bh9xkuz%2B0BJMhZqOJ0eZYqn%2FI4485FuC4fZt6lnwsYwko3pXcQWIyovY8e7TOeb7TlfFe2rXKspfxvhBGB21UDxiSEKdgwUIYuDabpLlRfSNCglTDrsOW8BjqkAbVKHT5PpqeIzc76YwZHJs3mJbouC2%2F1DKz4cApB%2B4y69%2BH07kq5xywb75y5ds0nRr5JlQwHbMN6tPPeKRR0BwFR8tO9hGkG%2BdzFrpX4FQa4uNiIMifPv4q3Aot9wln8Z8GriRKaWIeb3Wl6tb61QC4PG1k5ioeTeIoa8CFidbV9l17nEidR8IAba%2Fxe%2Bg%2FSu7FcYk9WGC5qRFVwNa2Q8tKdf1Lm&X-Amz-Signature=80a959b8979712087c5562f04464d5dfc29ab2dadc62f5612ff0b5ead19d0887&X-Amz-SignedHeaders=host&x-id=GetObject)
### R-squared (Coefficient of Determination)
- **Definition**: Indicates how well the data fits the regression line. Values range from 0 to 1, with values closer to 1 indicating a better fit.
- **Formula**: $ R^2 = 1 - \frac{\text{MSE of regression}}{\text{MSE of mean}} $
- **Python**: Use `score` method in the linear regression object.
#### Example
**Scenario**: Predicting test scores based on study hours.
**Interpretation**:
- **Good Fit**: R² = 0.9 (90% of variance explained)
- **Poor Fit**: R² = 0.2 (20% of variance explained)
**Python Code**:
```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([2, 3, 5])
model = LinearRegression()
model.fit(X, y)

r_squared = model.score(X, y)
print("R-squared:", r_squared)  # Output: R-squared: 0.9642857142857143
```
#### Example Interpretation
- **Good Fit**: Small MSE for regression, larger for mean → $ R^2 $ near 1.
- **Poor Fit**: Similar MSE for regression and mean → $ R^2 $ near 0.
- **Negative **$ R^2 $: Possible overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UH7JSDL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQDlgI3YKGxVHBUdqMPSNcg53AcgZp0zARP2v5Etfj1WAwIhAP9Bh4v3gveHTEHW%2Fq2AZQ9iZ9g%2FtcFAsnDUeKi%2FvSdZKv8DCH8QABoMNjM3NDIzMTgzODA1Igy8c8KQf1ynPv%2FOQiYq3AOgB%2BObqCpXHgjqjjOWcbG4ib5WEyApvahFNxC8UgT9dU8ffmJ%2FK44TZyZ9gmZ9R%2FcjxKbF89%2FlwtrFeI5sMxS39YmCl0juP6g5lHt0UBbC%2FguZ1gTkPFU90O%2Bd4i2fg9IdtQQJu1Yzh9e1DvjVzQ7w0QcpflRX4VFX1fhB9D4LNu%2B5BtqTfgSt%2F0HzSM%2FrHUcFPezC%2FDgpur3vEJlmd0XCf01fi9TctrUEipTuCYJszfou3qxOF4r1g30ce368nus6MOpi5659gbz0VvA3xgukJs7shZ8aBHIWZlUlCv52NDlzCcrPt9cDIj6GQTnn1FNAtUph3L51ds%2Bu42%2FBDVFJzwJTKE%2FiNZUwu5VFrCNWT46gxkBrBB4mizyy54gf39tFWOIGZvsWJap4UIqVgSEB%2BB86KFlG2%2B5mRxLOhXMRh7u7FR13ZjFnEYRos0IA4B%2BwvGAVds%2BMWvX6iH5G8hwfOaMsNK06S3UakVhICQBrXmRdq0H7JBAU52%2FPUguogUqxPE6uHH%2Fvqr%2Bh9xkuz%2B0BJMhZqOJ0eZYqn%2FI4485FuC4fZt6lnwsYwko3pXcQWIyovY8e7TOeb7TlfFe2rXKspfxvhBGB21UDxiSEKdgwUIYuDabpLlRfSNCglTDrsOW8BjqkAbVKHT5PpqeIzc76YwZHJs3mJbouC2%2F1DKz4cApB%2B4y69%2BH07kq5xywb75y5ds0nRr5JlQwHbMN6tPPeKRR0BwFR8tO9hGkG%2BdzFrpX4FQa4uNiIMifPv4q3Aot9wln8Z8GriRKaWIeb3Wl6tb61QC4PG1k5ioeTeIoa8CFidbV9l17nEidR8IAba%2Fxe%2Bg%2FSu7FcYk9WGC5qRFVwNa2Q8tKdf1Lm&X-Amz-Signature=b2dfc4ac72346a16a221582642aad729fecfbe4a26a51e0d3e142ddebebdcdce&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UH7JSDL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQDlgI3YKGxVHBUdqMPSNcg53AcgZp0zARP2v5Etfj1WAwIhAP9Bh4v3gveHTEHW%2Fq2AZQ9iZ9g%2FtcFAsnDUeKi%2FvSdZKv8DCH8QABoMNjM3NDIzMTgzODA1Igy8c8KQf1ynPv%2FOQiYq3AOgB%2BObqCpXHgjqjjOWcbG4ib5WEyApvahFNxC8UgT9dU8ffmJ%2FK44TZyZ9gmZ9R%2FcjxKbF89%2FlwtrFeI5sMxS39YmCl0juP6g5lHt0UBbC%2FguZ1gTkPFU90O%2Bd4i2fg9IdtQQJu1Yzh9e1DvjVzQ7w0QcpflRX4VFX1fhB9D4LNu%2B5BtqTfgSt%2F0HzSM%2FrHUcFPezC%2FDgpur3vEJlmd0XCf01fi9TctrUEipTuCYJszfou3qxOF4r1g30ce368nus6MOpi5659gbz0VvA3xgukJs7shZ8aBHIWZlUlCv52NDlzCcrPt9cDIj6GQTnn1FNAtUph3L51ds%2Bu42%2FBDVFJzwJTKE%2FiNZUwu5VFrCNWT46gxkBrBB4mizyy54gf39tFWOIGZvsWJap4UIqVgSEB%2BB86KFlG2%2B5mRxLOhXMRh7u7FR13ZjFnEYRos0IA4B%2BwvGAVds%2BMWvX6iH5G8hwfOaMsNK06S3UakVhICQBrXmRdq0H7JBAU52%2FPUguogUqxPE6uHH%2Fvqr%2Bh9xkuz%2B0BJMhZqOJ0eZYqn%2FI4485FuC4fZt6lnwsYwko3pXcQWIyovY8e7TOeb7TlfFe2rXKspfxvhBGB21UDxiSEKdgwUIYuDabpLlRfSNCglTDrsOW8BjqkAbVKHT5PpqeIzc76YwZHJs3mJbouC2%2F1DKz4cApB%2B4y69%2BH07kq5xywb75y5ds0nRr5JlQwHbMN6tPPeKRR0BwFR8tO9hGkG%2BdzFrpX4FQa4uNiIMifPv4q3Aot9wln8Z8GriRKaWIeb3Wl6tb61QC4PG1k5ioeTeIoa8CFidbV9l17nEidR8IAba%2Fxe%2Bg%2FSu7FcYk9WGC5qRFVwNa2Q8tKdf1Lm&X-Amz-Signature=9de93a553b0eb401fd7eed22050be1142481cc86ab4fff0cf27b6834eaf380cf&X-Amz-SignedHeaders=host&x-id=GetObject)
### Example: Predicting Car Price
- **Scenario**: Predict price for a car with 30 highway mpg.
- **Result**: Price = $13,771.30 (reasonable value).
#### Coefficient Interpretation
An increase of 1 mpg decreases price by $821.
#### Potential Issues
Unrealistic predictions may indicate:
- Incorrect assumptions
- Lack of data in certain ranges
### Generating Predictions
- Use NumPy's `arange` to create sequences for prediction.
```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([[20], [30], [40]])
y = np.array([15000, 13000, 12000])

# Model training
model = LinearRegression()
model.fit(X, y)

# Generating a sequence for prediction
mpg_values = np.arange(1, 101, 1)  # From 1 to 100 with step 1
predicted_prices = model.predict(mpg_values.reshape(-1, 1))

# Example prediction for 30 mpg
predicted_price = model.predict([[30]])
print("Predicted Price:", predicted_price[0])
```
#### Explanation
- `**np.arange(1, 101, 1)**`: Creates an array from 1 to 100 with a step of 1.
- `**reshape(-1, 1)**`: Reshapes the array for prediction.
### Visualization Techniques
- **Regression Plot**: Shows data trend and potential non-linear behavior.
- **Residual Plot**: Curvature indicates non-linear relationships.
- **Distribution Plot**: Highlights prediction accuracy in certain ranges.
### Evaluating Models
#### Mean Squared Error (MSE)
- **Interpretation**: Average squared difference between actual and predicted values.
**Example MSEs:**
- 495 (good fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MXVICXD%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIQDj%2FbAn60LejUAMh2DFyDlrv07leh1k%2F0VgNXYo%2FDYRcQIgJqCWNbRgcOzsupeqorcAyVXqR3VCqUCtsyeXDGIv0owq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDCz29rRwRCdB0xVBoCrcAxEX0nDRVTmw9Slqyiettj4HJ0SNxaJySg%2Fbw5iNF6zOXBuTXz4jyCYMdf6A2oOyYBvSqMXQuazV2nMxrntMi1DjkBaMpiCiEkROtg1O%2FzDt2%2B%2BwTMRojfmXbXXnE66OGRZ0JPGCvvrMrE4a1WKJDWZC%2BtLXhj4R%2Bf6HNccZmCoXM2KDY2wFioMJVURnG11k%2FItlahRDFg9BBVLmEbIhyNQLbzMhosqvFGXlBoNVhU1kG78%2FWkZd1oDuQyjRdAPkffGNzYhaL9WWFZpEql4mQ67P3pEtFezvoZvXUS8KbZVFiUwQMHmiNp2gfYt6wbP42IFTrFt4BJRK7hVR2wuCHiCJc1LfHPMsYbjLJAdH3xxWFlWR7rJzgNHF71ije9g%2Feu9PBGUpqrZireLkxARBqJKrEz%2FLiAN6MZ4qTd%2B1QmPTP1O9Ji17cno%2FHzZ0BkbJmoIP7eUw6Bs94GejrdhA%2FvQI4q9Zgeefi3rSaLzim%2FhLVZaO43NfC17vwIOJC667BNAy4F7RgfheeaPhE8JP1X7woXGZeEf6218ynyameBxH23AWE%2BasBptXzBWAVISsWoi7CHO0XTEB0%2FDfwULYlQjD1flEWnTXusntrBZ9pz4%2F5jRpFfXJrube8fJxMKuw5bwGOqUByH8hfP6E0LZbgtet39i7H%2FD%2Fgi%2BmgkLtO86G%2FgxO58TnqTzDO%2BwGGTMH5bXypHwsFxe1bogOXVhhIfLiVpahHDffBQf%2Fr4ZAM6mkKjLQIKQs4Ker92TKN%2BBAGYozi%2FMH5gXvJnq6oRngFXVqynFvTT2Eu7F0m9hz2pPP9190%2B05IOlOVvoP0KwWeDENjEKQuXywuYBeOy3NBXHae2mKlXTJ7bvNc&X-Amz-Signature=10bd49b95836e31a7257169262ed5f3f539505c08433ee3d223fa8f75ee9ef09&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MXVICXD%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIQDj%2FbAn60LejUAMh2DFyDlrv07leh1k%2F0VgNXYo%2FDYRcQIgJqCWNbRgcOzsupeqorcAyVXqR3VCqUCtsyeXDGIv0owq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDCz29rRwRCdB0xVBoCrcAxEX0nDRVTmw9Slqyiettj4HJ0SNxaJySg%2Fbw5iNF6zOXBuTXz4jyCYMdf6A2oOyYBvSqMXQuazV2nMxrntMi1DjkBaMpiCiEkROtg1O%2FzDt2%2B%2BwTMRojfmXbXXnE66OGRZ0JPGCvvrMrE4a1WKJDWZC%2BtLXhj4R%2Bf6HNccZmCoXM2KDY2wFioMJVURnG11k%2FItlahRDFg9BBVLmEbIhyNQLbzMhosqvFGXlBoNVhU1kG78%2FWkZd1oDuQyjRdAPkffGNzYhaL9WWFZpEql4mQ67P3pEtFezvoZvXUS8KbZVFiUwQMHmiNp2gfYt6wbP42IFTrFt4BJRK7hVR2wuCHiCJc1LfHPMsYbjLJAdH3xxWFlWR7rJzgNHF71ije9g%2Feu9PBGUpqrZireLkxARBqJKrEz%2FLiAN6MZ4qTd%2B1QmPTP1O9Ji17cno%2FHzZ0BkbJmoIP7eUw6Bs94GejrdhA%2FvQI4q9Zgeefi3rSaLzim%2FhLVZaO43NfC17vwIOJC667BNAy4F7RgfheeaPhE8JP1X7woXGZeEf6218ynyameBxH23AWE%2BasBptXzBWAVISsWoi7CHO0XTEB0%2FDfwULYlQjD1flEWnTXusntrBZ9pz4%2F5jRpFfXJrube8fJxMKuw5bwGOqUByH8hfP6E0LZbgtet39i7H%2FD%2Fgi%2BmgkLtO86G%2FgxO58TnqTzDO%2BwGGTMH5bXypHwsFxe1bogOXVhhIfLiVpahHDffBQf%2Fr4ZAM6mkKjLQIKQs4Ker92TKN%2BBAGYozi%2FMH5gXvJnq6oRngFXVqynFvTT2Eu7F0m9hz2pPP9190%2B05IOlOVvoP0KwWeDENjEKQuXywuYBeOy3NBXHae2mKlXTJ7bvNc&X-Amz-Signature=8867ab6ff8ac5e0a8403c1cc478aba43f7cb879b9037bb9fd8bfdfa50a701c9f&X-Amz-SignedHeaders=host&x-id=GetObject)

**Code Example:**
```python
from sklearn.metrics import mean_squared_error

# Actual and predicted values
actual = [15000, 13000, 12000]
predicted = model.predict(X)

# Calculate MSE
mse = mean_squared_error(actual, predicted)
print("MSE:", mse)
```

#### R-squared (R²)
- **Definition**: Indicates how well data fits the regression line.
Example R² Values:
- 0.9986 (excellent fit)
- 0.61 (weak linear relation)
```python
# Calculate R-squared
r_squared = model.score(X, y)
print("R-squared:", r_squared) 
```
### Model Comparison
- **MLR vs. SLR**: More variables can lower MSE, but not always a better fit.
- **Polynomial Regression**: Generally has lower MSE compared to linear regression.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MXVICXD%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIQDj%2FbAn60LejUAMh2DFyDlrv07leh1k%2F0VgNXYo%2FDYRcQIgJqCWNbRgcOzsupeqorcAyVXqR3VCqUCtsyeXDGIv0owq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDCz29rRwRCdB0xVBoCrcAxEX0nDRVTmw9Slqyiettj4HJ0SNxaJySg%2Fbw5iNF6zOXBuTXz4jyCYMdf6A2oOyYBvSqMXQuazV2nMxrntMi1DjkBaMpiCiEkROtg1O%2FzDt2%2B%2BwTMRojfmXbXXnE66OGRZ0JPGCvvrMrE4a1WKJDWZC%2BtLXhj4R%2Bf6HNccZmCoXM2KDY2wFioMJVURnG11k%2FItlahRDFg9BBVLmEbIhyNQLbzMhosqvFGXlBoNVhU1kG78%2FWkZd1oDuQyjRdAPkffGNzYhaL9WWFZpEql4mQ67P3pEtFezvoZvXUS8KbZVFiUwQMHmiNp2gfYt6wbP42IFTrFt4BJRK7hVR2wuCHiCJc1LfHPMsYbjLJAdH3xxWFlWR7rJzgNHF71ije9g%2Feu9PBGUpqrZireLkxARBqJKrEz%2FLiAN6MZ4qTd%2B1QmPTP1O9Ji17cno%2FHzZ0BkbJmoIP7eUw6Bs94GejrdhA%2FvQI4q9Zgeefi3rSaLzim%2FhLVZaO43NfC17vwIOJC667BNAy4F7RgfheeaPhE8JP1X7woXGZeEf6218ynyameBxH23AWE%2BasBptXzBWAVISsWoi7CHO0XTEB0%2FDfwULYlQjD1flEWnTXusntrBZ9pz4%2F5jRpFfXJrube8fJxMKuw5bwGOqUByH8hfP6E0LZbgtet39i7H%2FD%2Fgi%2BmgkLtO86G%2FgxO58TnqTzDO%2BwGGTMH5bXypHwsFxe1bogOXVhhIfLiVpahHDffBQf%2Fr4ZAM6mkKjLQIKQs4Ker92TKN%2BBAGYozi%2FMH5gXvJnq6oRngFXVqynFvTT2Eu7F0m9hz2pPP9190%2B05IOlOVvoP0KwWeDENjEKQuXywuYBeOy3NBXHae2mKlXTJ7bvNc&X-Amz-Signature=aef84de3c98541104d752c005204a8bb9a54686f62bc3604a3147f81aef933d6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Conclusion
- Evaluate models using both visualization and numerical metrics.
- Consider context and domain for interpreting R² and MSE values.
___

## Notes
### Regression Plot
When it comes to simple linear regression, an excellent way to visualize the fit of our model is by using **regression plots**.
This plot will show a combination of scattered data points (a **scatterplot**), as well as the fitted **linear regression** line going through the data. This will give us a reasonable estimate of the relationship between the two variables, the strength of the correlation, as well as the direction (positive or negative correlation).
### Residual Plot
A good way to visualize the variance of the data is to use a residual plot.
What is a **residual**?
The difference between the observed value (y) and the predicted value (ŷ) is called the residual (e). When we look at a regression plot, the residual is the distance from the data point to the fitted regression line.
So what is a **residual plot**?
A residual plot is a graph that shows the residuals on the vertical y-axis and the independent variable on the horizontal x-axis.
What do we pay attention to when looking at a residual plot?
We look at the spread of the residuals:
- If the points in a residual plot are **randomly spread out around the x-axis**, then a **linear model is appropriate** for the data.
Why is that? Randomly spread out residuals mean that the variance is constant, and thus the linear model is a good fit for this data.
### **Simple Linear Regression**
One example of a Data Model that we will be using is **Simple Linear Regression**.
Simple Linear Regression is a method to help us understand the relationship between two variables:
- The predictor/independent variable (X)
- The response/dependent variable (that we want to predict) (Y)
The result of Linear Regression is a **linear function** that predicts the response (dependent) variable as a function of the predictor (independent) variable.
### **Multiple Linear Regression**
What if we want to predict car price using more than one variable?
If we want to use more variables in our model to predict car price, we can use **Multiple Linear Regression**. Multiple Linear Regression is very similar to Simple Linear Regression, but this method is used to explain the relationship between one continuous response (dependent) variable and **two or more** predictor (independent) variables. Most of the real-world regression models involve multiple predictors. We will illustrate the structure by using four predictor variables, but these results can generalize to any number.
### **Polynomial Regression**
**Polynomial regression** is a particular case of the general linear regression model or multiple linear regression models.
We get non-linear relationships by squaring or setting higher-order terms of the predictor variables.
### Measures for In-Sample Evaluation
When evaluating our models, not only do we want to visualize the results, but we also need a quantitative measure to determine how accurate the model is.
Two very important measures that are often used in statistics to assess the accuracy of a model are:
- **R² / R-squared (The Coefficient of Determination)**
- **Mean Squared Error (MSE)**
#### R-squared
R-squared, also known as the coefficient of determination, measures how closely the data aligns with the fitted regression line.
The R-squared value represents the percentage of variation in the response variable (y) that is explained by the linear model.
#### Mean Squared Error (MSE)
The Mean Squared Error (MSE) measures the average of the squares of the errors. In other words, it calculates the difference between the actual values (y) and the estimated values (ŷ).
___
## **Cheat Sheet: Model Development**
### Linear Regression
- **Process**: Create a Linear Regression model object
- **Description**: Create an instance of the `LinearRegression` model.
- **Code Example**:
```python
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
```
### Train Linear Regression Model
- **Process**: Train the Linear Regression model
- **Description**: Fit the model on the input and output data. If there’s only one input attribute, it’s simple linear regression. If there are multiple attributes, it’s multiple linear regression.
- **Code Example**:
```python
X = df[['attribute_1', 'attribute_2', ...]]
Y = df['target_attribute']

lr.fit(X, Y)
```
### Generate Output Predictions
- **Process**: Predict the output for given input attributes
- **Description**: Use the trained model to predict the output values based on the input attributes.
- **Code Example**:
```python
Y_hat = lr.predict(X)
```
### Identify the Coefficient and Intercept
- **Process**: Retrieve the model’s coefficient and intercept
- **Description**: Access the slope coefficient and intercept values of the linear regression model.
- **Code Example**:
```python
coeff = lr.coef_
intercept = lr.intercept_
```
### Residual Plot
- **Process**: Create a Residual Plot
- **Description**: Plot the residuals (the differences between observed and predicted values) to assess the goodness of fit.
- **Code Example**:
```python
import seaborn as sns

sns.residplot(x=df['attribute_1'], y=df['attribute_2'])
```
### Distribution Plot
- **Process**: Create a Distribution Plot
- **Description**: Plot the distribution of a given attribute’s data.
- **Code Example**:
```python
import seaborn as sns

sns.distplot(df['attribute_name'], hist=False)
```
### Polynomial Regression
- **Process**: Perform Polynomial Regression
- **Description**: Fit a polynomial model to the data using NumPy.
- **Code Example**:
```python
import numpy as np

f = np.polyfit(x, y, n)
p = np.poly1d(f)
Y_hat = p(x)
```
### Multi-variate Polynomial Regression
- **Process**: Create Polynomial Features
- **Description**: Generate polynomial combinations of features up to a specified degree.
- **Code Example**:
```python
from sklearn.preprocessing import PolynomialFeatures

Z = df[['attribute_1', 'attribute_2', ...]]
pr = PolynomialFeatures(degree=n)
Z_pr = pr.fit_transform(Z)
```
### Pipeline
- **Process**: Create a Data Pipeline
- **Description**: Simplify the steps of processing data by creating a pipeline with a sequence of steps.
- **Code Example**:
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

Input = [
    ('scale', StandardScaler()),
    ('polynomial', PolynomialFeatures(include_bias=False)),
    ('model', LinearRegression())
]
pipe = Pipeline(Input)
Z = Z.astype(float)
pipe.fit(Z, y)
ypipe = pipe.predict(Z)
```
### R² Value
- **Process**: Calculate R² Value
- **Description**: Measure how well the model’s predictions fit the data. This is the proportion of variance explained by the model.
- **Code Example**:
	- For Linear Regression:
```python
from sklearn.metrics import r2_score

R2_score = lr.score(X, Y)
```
	- For Polynomial Regression:
```python
from sklearn.metrics import r2_score
import numpy as np

f = np.polyfit(x, y, n)
p = np.poly1d(f)
R2_score = r2_score(y, p(x))
```
### Mean Squared Error (MSE) Value
- **Process**: Calculate Mean Squared Error (MSE)
- **Description**: Measure the average of the squares of the errors, which are the differences between actual values and the estimated values.
- **Code Example**:
```python
from sklearn.metrics import mean_squared_error

MSE = mean_squared_error(Y, Y_hat)
```
___

