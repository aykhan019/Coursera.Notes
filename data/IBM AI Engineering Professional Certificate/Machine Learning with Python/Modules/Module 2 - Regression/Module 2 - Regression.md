

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJYDA3SY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQCE%2F5KOYzgoyl9Av%2BFnx4dy%2F6UYjxtEycMOr9a%2BTa5OawIgTaVOMnFfukYVsVMYSa%2Bbs44ZBe5D%2FMwFDZ89685m4pYq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDMuGvgKfo4OAPTgvdSrcA9qFjF4%2BfV5%2FqutVroOsJkg86z0MO%2F32nnb5aBtuewba8YLgR9tEo5Ls0ZhfJW3FL2oKYqenOorSyLuprI5sop8vRjzXzG9E47%2FkcQKnjXgBbxZ4zJUzCgaIe%2Fivjp%2FuO7B7RwPEhvsRZv1wtasqijC23EbWoo693vAwxTXLRmxR%2Bgy%2FLL9K2jHBz5e%2B8oS8Fb3dO4wXqEKHlT%2B1eFO1aFmWjQoCBeWiTsTkBAH1DqcKy8NDFBwFBiuXZgpDAn0elN8q2kTB6Xoccd98SpHqX6d72ntaDvmD5FznaC98iT0LzOy34Be8LXw%2B%2BWjz6clbXej%2BLPSuNOYTlfmkM876eZeYwrftD%2FTxAETg5yuSqcRHkq1zyAeGlzWutsO04nSPeDirOyGmDHjSsrNbNs0z9XpPUsmNmfP8%2BBjGLQbN0H1BgFUHajMKVaSNsKT24yyaYSN6%2B53SwiIRaWZQCJLTurIWZ0pGiK9W%2FR1IJeGQzoBzYFF%2FtQng9iVnss1bvnw9TAbbFNLOgicZNXQPUXdp9U6FsJL6Ygyz17pJbnNEQxZTbOb9TSTs3JOD32t8f54OngRISmvOK5daCjwTrzix0ZpWCzVvFTHy4QbMlM4CK3YeDS2hkSK6yhoBn3xWMJm9iL0GOqUBGoqxFUhqCzo7%2FuuJZch9Z2S2gyBbBpphHcwsNbWfJktuiwp1eIZYiAA%2B8XK63LGBBXc9uh5wy3w1Tag9YTUx9Q6g9XrcIk4UM7H%2FUFVUpCXNpl83eFuxa0ad359nFb5fj0njlTzDjeyDcl7Ui14NgT6pETMkE0k5WgGqB4cmyv4ebwlltfthyyhqA0%2BNd8LQKQaC1toA%2Fry3WGPobnJ7l6DZZJcx&X-Amz-Signature=c8c1a2380df4b627cc6fa5e99d800bc9031eb9269b9f89a27631f4178bdf7f4c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJYDA3SY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQCE%2F5KOYzgoyl9Av%2BFnx4dy%2F6UYjxtEycMOr9a%2BTa5OawIgTaVOMnFfukYVsVMYSa%2Bbs44ZBe5D%2FMwFDZ89685m4pYq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDMuGvgKfo4OAPTgvdSrcA9qFjF4%2BfV5%2FqutVroOsJkg86z0MO%2F32nnb5aBtuewba8YLgR9tEo5Ls0ZhfJW3FL2oKYqenOorSyLuprI5sop8vRjzXzG9E47%2FkcQKnjXgBbxZ4zJUzCgaIe%2Fivjp%2FuO7B7RwPEhvsRZv1wtasqijC23EbWoo693vAwxTXLRmxR%2Bgy%2FLL9K2jHBz5e%2B8oS8Fb3dO4wXqEKHlT%2B1eFO1aFmWjQoCBeWiTsTkBAH1DqcKy8NDFBwFBiuXZgpDAn0elN8q2kTB6Xoccd98SpHqX6d72ntaDvmD5FznaC98iT0LzOy34Be8LXw%2B%2BWjz6clbXej%2BLPSuNOYTlfmkM876eZeYwrftD%2FTxAETg5yuSqcRHkq1zyAeGlzWutsO04nSPeDirOyGmDHjSsrNbNs0z9XpPUsmNmfP8%2BBjGLQbN0H1BgFUHajMKVaSNsKT24yyaYSN6%2B53SwiIRaWZQCJLTurIWZ0pGiK9W%2FR1IJeGQzoBzYFF%2FtQng9iVnss1bvnw9TAbbFNLOgicZNXQPUXdp9U6FsJL6Ygyz17pJbnNEQxZTbOb9TSTs3JOD32t8f54OngRISmvOK5daCjwTrzix0ZpWCzVvFTHy4QbMlM4CK3YeDS2hkSK6yhoBn3xWMJm9iL0GOqUBGoqxFUhqCzo7%2FuuJZch9Z2S2gyBbBpphHcwsNbWfJktuiwp1eIZYiAA%2B8XK63LGBBXc9uh5wy3w1Tag9YTUx9Q6g9XrcIk4UM7H%2FUFVUpCXNpl83eFuxa0ad359nFb5fj0njlTzDjeyDcl7Ui14NgT6pETMkE0k5WgGqB4cmyv4ebwlltfthyyhqA0%2BNd8LQKQaC1toA%2Fry3WGPobnJ7l6DZZJcx&X-Amz-Signature=6bbda21f2dd5e8d998d0717443b8ed1437e32809a8313b27c535bc25ab30a3b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJYDA3SY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQCE%2F5KOYzgoyl9Av%2BFnx4dy%2F6UYjxtEycMOr9a%2BTa5OawIgTaVOMnFfukYVsVMYSa%2Bbs44ZBe5D%2FMwFDZ89685m4pYq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDMuGvgKfo4OAPTgvdSrcA9qFjF4%2BfV5%2FqutVroOsJkg86z0MO%2F32nnb5aBtuewba8YLgR9tEo5Ls0ZhfJW3FL2oKYqenOorSyLuprI5sop8vRjzXzG9E47%2FkcQKnjXgBbxZ4zJUzCgaIe%2Fivjp%2FuO7B7RwPEhvsRZv1wtasqijC23EbWoo693vAwxTXLRmxR%2Bgy%2FLL9K2jHBz5e%2B8oS8Fb3dO4wXqEKHlT%2B1eFO1aFmWjQoCBeWiTsTkBAH1DqcKy8NDFBwFBiuXZgpDAn0elN8q2kTB6Xoccd98SpHqX6d72ntaDvmD5FznaC98iT0LzOy34Be8LXw%2B%2BWjz6clbXej%2BLPSuNOYTlfmkM876eZeYwrftD%2FTxAETg5yuSqcRHkq1zyAeGlzWutsO04nSPeDirOyGmDHjSsrNbNs0z9XpPUsmNmfP8%2BBjGLQbN0H1BgFUHajMKVaSNsKT24yyaYSN6%2B53SwiIRaWZQCJLTurIWZ0pGiK9W%2FR1IJeGQzoBzYFF%2FtQng9iVnss1bvnw9TAbbFNLOgicZNXQPUXdp9U6FsJL6Ygyz17pJbnNEQxZTbOb9TSTs3JOD32t8f54OngRISmvOK5daCjwTrzix0ZpWCzVvFTHy4QbMlM4CK3YeDS2hkSK6yhoBn3xWMJm9iL0GOqUBGoqxFUhqCzo7%2FuuJZch9Z2S2gyBbBpphHcwsNbWfJktuiwp1eIZYiAA%2B8XK63LGBBXc9uh5wy3w1Tag9YTUx9Q6g9XrcIk4UM7H%2FUFVUpCXNpl83eFuxa0ad359nFb5fj0njlTzDjeyDcl7Ui14NgT6pETMkE0k5WgGqB4cmyv4ebwlltfthyyhqA0%2BNd8LQKQaC1toA%2Fry3WGPobnJ7l6DZZJcx&X-Amz-Signature=a39e631cf434962f9e710be67b00d132d41c4849b2cd039959f3868e37fcfd1d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJYDA3SY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQCE%2F5KOYzgoyl9Av%2BFnx4dy%2F6UYjxtEycMOr9a%2BTa5OawIgTaVOMnFfukYVsVMYSa%2Bbs44ZBe5D%2FMwFDZ89685m4pYq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDMuGvgKfo4OAPTgvdSrcA9qFjF4%2BfV5%2FqutVroOsJkg86z0MO%2F32nnb5aBtuewba8YLgR9tEo5Ls0ZhfJW3FL2oKYqenOorSyLuprI5sop8vRjzXzG9E47%2FkcQKnjXgBbxZ4zJUzCgaIe%2Fivjp%2FuO7B7RwPEhvsRZv1wtasqijC23EbWoo693vAwxTXLRmxR%2Bgy%2FLL9K2jHBz5e%2B8oS8Fb3dO4wXqEKHlT%2B1eFO1aFmWjQoCBeWiTsTkBAH1DqcKy8NDFBwFBiuXZgpDAn0elN8q2kTB6Xoccd98SpHqX6d72ntaDvmD5FznaC98iT0LzOy34Be8LXw%2B%2BWjz6clbXej%2BLPSuNOYTlfmkM876eZeYwrftD%2FTxAETg5yuSqcRHkq1zyAeGlzWutsO04nSPeDirOyGmDHjSsrNbNs0z9XpPUsmNmfP8%2BBjGLQbN0H1BgFUHajMKVaSNsKT24yyaYSN6%2B53SwiIRaWZQCJLTurIWZ0pGiK9W%2FR1IJeGQzoBzYFF%2FtQng9iVnss1bvnw9TAbbFNLOgicZNXQPUXdp9U6FsJL6Ygyz17pJbnNEQxZTbOb9TSTs3JOD32t8f54OngRISmvOK5daCjwTrzix0ZpWCzVvFTHy4QbMlM4CK3YeDS2hkSK6yhoBn3xWMJm9iL0GOqUBGoqxFUhqCzo7%2FuuJZch9Z2S2gyBbBpphHcwsNbWfJktuiwp1eIZYiAA%2B8XK63LGBBXc9uh5wy3w1Tag9YTUx9Q6g9XrcIk4UM7H%2FUFVUpCXNpl83eFuxa0ad359nFb5fj0njlTzDjeyDcl7Ui14NgT6pETMkE0k5WgGqB4cmyv4ebwlltfthyyhqA0%2BNd8LQKQaC1toA%2Fry3WGPobnJ7l6DZZJcx&X-Amz-Signature=fbc90478d4b77bf5bb8490fafd88c65fb486ef9006e71fea4fe9e127996f85fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJYDA3SY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQCE%2F5KOYzgoyl9Av%2BFnx4dy%2F6UYjxtEycMOr9a%2BTa5OawIgTaVOMnFfukYVsVMYSa%2Bbs44ZBe5D%2FMwFDZ89685m4pYq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDMuGvgKfo4OAPTgvdSrcA9qFjF4%2BfV5%2FqutVroOsJkg86z0MO%2F32nnb5aBtuewba8YLgR9tEo5Ls0ZhfJW3FL2oKYqenOorSyLuprI5sop8vRjzXzG9E47%2FkcQKnjXgBbxZ4zJUzCgaIe%2Fivjp%2FuO7B7RwPEhvsRZv1wtasqijC23EbWoo693vAwxTXLRmxR%2Bgy%2FLL9K2jHBz5e%2B8oS8Fb3dO4wXqEKHlT%2B1eFO1aFmWjQoCBeWiTsTkBAH1DqcKy8NDFBwFBiuXZgpDAn0elN8q2kTB6Xoccd98SpHqX6d72ntaDvmD5FznaC98iT0LzOy34Be8LXw%2B%2BWjz6clbXej%2BLPSuNOYTlfmkM876eZeYwrftD%2FTxAETg5yuSqcRHkq1zyAeGlzWutsO04nSPeDirOyGmDHjSsrNbNs0z9XpPUsmNmfP8%2BBjGLQbN0H1BgFUHajMKVaSNsKT24yyaYSN6%2B53SwiIRaWZQCJLTurIWZ0pGiK9W%2FR1IJeGQzoBzYFF%2FtQng9iVnss1bvnw9TAbbFNLOgicZNXQPUXdp9U6FsJL6Ygyz17pJbnNEQxZTbOb9TSTs3JOD32t8f54OngRISmvOK5daCjwTrzix0ZpWCzVvFTHy4QbMlM4CK3YeDS2hkSK6yhoBn3xWMJm9iL0GOqUBGoqxFUhqCzo7%2FuuJZch9Z2S2gyBbBpphHcwsNbWfJktuiwp1eIZYiAA%2B8XK63LGBBXc9uh5wy3w1Tag9YTUx9Q6g9XrcIk4UM7H%2FUFVUpCXNpl83eFuxa0ad359nFb5fj0njlTzDjeyDcl7Ui14NgT6pETMkE0k5WgGqB4cmyv4ebwlltfthyyhqA0%2BNd8LQKQaC1toA%2Fry3WGPobnJ7l6DZZJcx&X-Amz-Signature=8d4f1fc070e67425e2f65a14537bb336b903944534c4f93147dca1fc2c5ada32&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJYDA3SY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQCE%2F5KOYzgoyl9Av%2BFnx4dy%2F6UYjxtEycMOr9a%2BTa5OawIgTaVOMnFfukYVsVMYSa%2Bbs44ZBe5D%2FMwFDZ89685m4pYq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDMuGvgKfo4OAPTgvdSrcA9qFjF4%2BfV5%2FqutVroOsJkg86z0MO%2F32nnb5aBtuewba8YLgR9tEo5Ls0ZhfJW3FL2oKYqenOorSyLuprI5sop8vRjzXzG9E47%2FkcQKnjXgBbxZ4zJUzCgaIe%2Fivjp%2FuO7B7RwPEhvsRZv1wtasqijC23EbWoo693vAwxTXLRmxR%2Bgy%2FLL9K2jHBz5e%2B8oS8Fb3dO4wXqEKHlT%2B1eFO1aFmWjQoCBeWiTsTkBAH1DqcKy8NDFBwFBiuXZgpDAn0elN8q2kTB6Xoccd98SpHqX6d72ntaDvmD5FznaC98iT0LzOy34Be8LXw%2B%2BWjz6clbXej%2BLPSuNOYTlfmkM876eZeYwrftD%2FTxAETg5yuSqcRHkq1zyAeGlzWutsO04nSPeDirOyGmDHjSsrNbNs0z9XpPUsmNmfP8%2BBjGLQbN0H1BgFUHajMKVaSNsKT24yyaYSN6%2B53SwiIRaWZQCJLTurIWZ0pGiK9W%2FR1IJeGQzoBzYFF%2FtQng9iVnss1bvnw9TAbbFNLOgicZNXQPUXdp9U6FsJL6Ygyz17pJbnNEQxZTbOb9TSTs3JOD32t8f54OngRISmvOK5daCjwTrzix0ZpWCzVvFTHy4QbMlM4CK3YeDS2hkSK6yhoBn3xWMJm9iL0GOqUBGoqxFUhqCzo7%2FuuJZch9Z2S2gyBbBpphHcwsNbWfJktuiwp1eIZYiAA%2B8XK63LGBBXc9uh5wy3w1Tag9YTUx9Q6g9XrcIk4UM7H%2FUFVUpCXNpl83eFuxa0ad359nFb5fj0njlTzDjeyDcl7Ui14NgT6pETMkE0k5WgGqB4cmyv4ebwlltfthyyhqA0%2BNd8LQKQaC1toA%2Fry3WGPobnJ7l6DZZJcx&X-Amz-Signature=406e5b12e430d53f72231f73b98b25214d9aec29e5517d15542a9f86e1d667a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJYDA3SY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQCE%2F5KOYzgoyl9Av%2BFnx4dy%2F6UYjxtEycMOr9a%2BTa5OawIgTaVOMnFfukYVsVMYSa%2Bbs44ZBe5D%2FMwFDZ89685m4pYq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDMuGvgKfo4OAPTgvdSrcA9qFjF4%2BfV5%2FqutVroOsJkg86z0MO%2F32nnb5aBtuewba8YLgR9tEo5Ls0ZhfJW3FL2oKYqenOorSyLuprI5sop8vRjzXzG9E47%2FkcQKnjXgBbxZ4zJUzCgaIe%2Fivjp%2FuO7B7RwPEhvsRZv1wtasqijC23EbWoo693vAwxTXLRmxR%2Bgy%2FLL9K2jHBz5e%2B8oS8Fb3dO4wXqEKHlT%2B1eFO1aFmWjQoCBeWiTsTkBAH1DqcKy8NDFBwFBiuXZgpDAn0elN8q2kTB6Xoccd98SpHqX6d72ntaDvmD5FznaC98iT0LzOy34Be8LXw%2B%2BWjz6clbXej%2BLPSuNOYTlfmkM876eZeYwrftD%2FTxAETg5yuSqcRHkq1zyAeGlzWutsO04nSPeDirOyGmDHjSsrNbNs0z9XpPUsmNmfP8%2BBjGLQbN0H1BgFUHajMKVaSNsKT24yyaYSN6%2B53SwiIRaWZQCJLTurIWZ0pGiK9W%2FR1IJeGQzoBzYFF%2FtQng9iVnss1bvnw9TAbbFNLOgicZNXQPUXdp9U6FsJL6Ygyz17pJbnNEQxZTbOb9TSTs3JOD32t8f54OngRISmvOK5daCjwTrzix0ZpWCzVvFTHy4QbMlM4CK3YeDS2hkSK6yhoBn3xWMJm9iL0GOqUBGoqxFUhqCzo7%2FuuJZch9Z2S2gyBbBpphHcwsNbWfJktuiwp1eIZYiAA%2B8XK63LGBBXc9uh5wy3w1Tag9YTUx9Q6g9XrcIk4UM7H%2FUFVUpCXNpl83eFuxa0ad359nFb5fj0njlTzDjeyDcl7Ui14NgT6pETMkE0k5WgGqB4cmyv4ebwlltfthyyhqA0%2BNd8LQKQaC1toA%2Fry3WGPobnJ7l6DZZJcx&X-Amz-Signature=304044d697649a1eecc14fe3078770b21987c10295c90acd318b7b6e183cb9f5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJYDA3SY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQCE%2F5KOYzgoyl9Av%2BFnx4dy%2F6UYjxtEycMOr9a%2BTa5OawIgTaVOMnFfukYVsVMYSa%2Bbs44ZBe5D%2FMwFDZ89685m4pYq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDMuGvgKfo4OAPTgvdSrcA9qFjF4%2BfV5%2FqutVroOsJkg86z0MO%2F32nnb5aBtuewba8YLgR9tEo5Ls0ZhfJW3FL2oKYqenOorSyLuprI5sop8vRjzXzG9E47%2FkcQKnjXgBbxZ4zJUzCgaIe%2Fivjp%2FuO7B7RwPEhvsRZv1wtasqijC23EbWoo693vAwxTXLRmxR%2Bgy%2FLL9K2jHBz5e%2B8oS8Fb3dO4wXqEKHlT%2B1eFO1aFmWjQoCBeWiTsTkBAH1DqcKy8NDFBwFBiuXZgpDAn0elN8q2kTB6Xoccd98SpHqX6d72ntaDvmD5FznaC98iT0LzOy34Be8LXw%2B%2BWjz6clbXej%2BLPSuNOYTlfmkM876eZeYwrftD%2FTxAETg5yuSqcRHkq1zyAeGlzWutsO04nSPeDirOyGmDHjSsrNbNs0z9XpPUsmNmfP8%2BBjGLQbN0H1BgFUHajMKVaSNsKT24yyaYSN6%2B53SwiIRaWZQCJLTurIWZ0pGiK9W%2FR1IJeGQzoBzYFF%2FtQng9iVnss1bvnw9TAbbFNLOgicZNXQPUXdp9U6FsJL6Ygyz17pJbnNEQxZTbOb9TSTs3JOD32t8f54OngRISmvOK5daCjwTrzix0ZpWCzVvFTHy4QbMlM4CK3YeDS2hkSK6yhoBn3xWMJm9iL0GOqUBGoqxFUhqCzo7%2FuuJZch9Z2S2gyBbBpphHcwsNbWfJktuiwp1eIZYiAA%2B8XK63LGBBXc9uh5wy3w1Tag9YTUx9Q6g9XrcIk4UM7H%2FUFVUpCXNpl83eFuxa0ad359nFb5fj0njlTzDjeyDcl7Ui14NgT6pETMkE0k5WgGqB4cmyv4ebwlltfthyyhqA0%2BNd8LQKQaC1toA%2Fry3WGPobnJ7l6DZZJcx&X-Amz-Signature=d03fc9c24c052bc41031e9f13153402f60f219502d24ef054b9c88e420f14a32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKER5YXX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQDHD9fXB6R%2F%2B4cNugp0gG5tHYDnJD9SZlY%2BN0Zff4tGCQIgOQGKsmvykPcDfPqCcSBuhrO1axNqZ8Kof4H8l0br%2Bw4q%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDJtJqErroNtqW2bjVircA81sExugI%2FImbG7MFjAGIa0cOcYCP9JCSN50PsG1FkWRQ5EYAcY9KLhjgpvdYk7Eb4Wg5ZcDH4tSyzdTJ0D4ewqqqr7lQZHGr0B3SRP2viLdrWmiLUnk%2FozPzgOy1rvcmR4B%2FbThuwpD7h9SqeywXU6zYjssWZ3k%2Ff0Lt%2BWw1Iqmd6ccqblU5q1RA9SIYqbIHj%2BRWk%2BLFU8jhWgaB6hg6HnGyafhj%2Fu6OyM2Sv7NeCsoQ2KtEeU31yiJrxYJYyOQmiuhCZTxfQWdyEOjiZqPV00nVnklUzrbOpxCYOmDYLT488zvOtbZnhEuY0VQC30NLXbK3tBSqBotN0yUFi8emspBEJSV%2BgVMWj5K%2FhBiSXZPWcGtdvX4SkQ%2B8U62b5lPsnUSK48C753%2F63M46p%2F8VA%2BXC1wC75qDMl0ETcG4W8ORfkPRlrNDk%2BfrmGrUpw3YZxq1ik%2ByR%2FmsI9qPdaUBXEDuGnZtYDPODdMGfdNTd9N7og3kvcdOwIColB25Y0ZLvVB1Vj29GhC0dcK%2BRva1kOzgWWkvBQi14VjjiL%2FqbytFd1kVMZh4oK2WRcuH1qkYo4XgnYnmoiQX%2FNfgIOlIyvGov62uodmI5mOLzz1pZbE3wnYdcnfTocTZCYZJMJG9iL0GOqUByDCIKF%2BCyV%2FNqmBQybmlCSAvWTW%2B9aRpMDbPGWpSMC%2B5DFrWL2JuniGvlUntGF9u6YI4KuwZUXIs5IqzQU6zP2qUX6iL5bpftJiL80PyXfqJ79qJT1v%2FqYrYlJiVW6hRBKVn%2B23eyL8x50reat%2BtpFl47W3lWM8okGWU%2BY5qWwb%2BLkaUigGwqcd4Cgry0vDNp7kZqVDqxGGTNrrCWsp9zTexizKQ&X-Amz-Signature=bd528d2fdff81289ebbc958f331cd6847da1f64606b58e22d65f9c160c2f1943&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIY5LPTW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIFQ9OMeV4x0X%2F97d01FEW9cGARA9%2FGIXDpP%2FNOHWMN9%2BAiEApghRXvCoaLVDbCQ18OA%2FB3QWuzv94DaztjzSdDSr6J4q%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDLcDqbMXUFmWX7%2FsnCrcA3n4TeyqXT5JzWgqpuY8aPZTHK3Bap6Jz%2BRZowToMRewmOcExOAOjUP4VMDiNXcBc33ugGLa7cVBN9w%2FKIjup7BkONSUagbxKxy5HQCKY6DMaQs13liL98kU%2BhEgIJV4K8OScw9GZcX5NULqc28XgL8YzcIXVXqY%2FT0khXKF0omhhbc18MjjBoaQLqiIys5pbnScZkNdWk0703sWAvcJBocrZtU46aGLMOICx3VCVuSV5V7LtYxlyXr65DSyMt%2BZucYaqAlIYnVm4M8fe1CB9XS4hBr%2BxljsgT9HgjY4YNW191mMgAD5ZSBp0RYRSymOzTozNsl01rqdJ5KZRYP3RBxC%2FwM2am0%2B9ppYQYJ%2BF9UzrfhSLbsTbo4tiaizCkyohRZcD4qO2A%2B%2FfMX3a6wXUC29McIvlUMZ1Wu5HU3dvVsRncxLhIxWcVScDDJXqRwo%2Bz%2Fd%2FNxDCIYk8Rfpj2vNMSrseb61E2CMK75FefE5H8HRYm5LbevEsUSita2jpU4trulPavO7XPbAQMPEOs62EnQJ8dLVoW%2BzAzPf5eX%2B1ZWeJzs%2FJOJfNlLnWinTkBfKMfXXMf%2Finv38i%2FEVaDvJ3u8hS3ZJcN1zAq%2BEIn97cRu8xUpHdrzSDmweHkNSMN28iL0GOqUBgjjWLN4UbwM2O0MmMvGtl0Rz6H%2Byimb3OgH2JXiwLBktA82x2QRcu4x6xsP8030hOn5jJvBTplx5ekrHQ1pTzZP%2FjxDPsZks3wvJMhTckG59i0GLewdxGF36%2FhofGDFKokaDADQ0kb4%2F2uQFw646utGUr90GdY%2BElVDhnIjABQdVCQQ8wdt7OgBCOYCZAfNejNqPYzz%2Fs44GdHxJobe4e67%2BMN8J&X-Amz-Signature=adbc44944e79c8d6e07dc1423ff6e2a90751aa33fd692b273dc9a7ed71d502d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ETCGLZZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCICYMQqLlsZAZiEjloS7LzS5w5BtwlK2kleoX6CKFCmvWAiEAsYMb9A3Ce8%2FwHpNIYjCbBnHlJEL0K5e0E5p0aLbH9Bkq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDCEW3TwvkSrDpVgm1yrcAwInKB4salO7liNlSPMAI285qtQsDIFYUuwiF14Glayw%2FiHNFAYtdhPkHAbfAwqoJoQ6yTmjXlNyXhDpR4ejvD028lD01LYAVCjf%2BuCIbo8Qt3UOIX90%2B7sQR8wgriXdVm41YKESicy5cpT2CUAPkfie2BsJpc2x2JHQ4QgUUy1AvG%2B5ywtWXJDWtuCjD2QSbI2CuzvoM59xMCqRL9JgKFszmeNq0Tacb2R4%2BcaoJtACMxhqDfjAvLU5oLQZGlUON4YdP23%2B0Z%2FBI9QMGab33s7%2Fkx6qa1N9J7vFIrIDRr43kIWF%2BU3i2X4dv2x%2FmeTe8HZfzNpr22QtuH9SCulmDynU94%2FnmE9XI1BFESni%2BqAcC3UNMXetVeRO%2Fh63nPt5p8zJaCnQdjvLeVhYBhZL%2BVcnJ4X2Q4GqxxTP1d3NP%2BpYEllebgs7UAlOAjyEZ%2BT1QaMMsIv29dUZ1aSNJgNsozXZ%2BVhxkUiDv%2B%2Bm1cG1v4UI8QX0Anzn7uHd1MrOdL%2BaZ9%2FWe7gQMB9rMNWVaH6DTP3wifJ5Qb3tetEn8eiQBedq%2BPyQOU1MWBnjzu6agU1mC9%2FgvRxrsNxuP%2BB%2Fn4Y8CUxzCS12W3QyHq%2F8yXaOI9flw8QQzRXI1CW656rpMOy8iL0GOqUBOyEgbyEVZmV7UVtHGjsWzJSTw0mYHuH998R4fN%2FU8gePMyNNjba180%2Bgp5bkujFqEUmrbMzfvftFBHs1g7KHG9AgvCyV8sj9xOs2Hwg8rjSj6AIRHIDXJFrGhAyVTTz%2FAGOW0g4JZJo%2BlQOIdpAGxE4uoEA34MVr50dmLRdImwxMyaz7SNl8vL2Es47TFLfliMU%2BeQlR7v8mVJ9praM2ZhryZ5pO&X-Amz-Signature=eebbc9e5e056157e969123aff9c89960a2e632baf56ae3f53409765d302d89cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ETCGLZZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCICYMQqLlsZAZiEjloS7LzS5w5BtwlK2kleoX6CKFCmvWAiEAsYMb9A3Ce8%2FwHpNIYjCbBnHlJEL0K5e0E5p0aLbH9Bkq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDCEW3TwvkSrDpVgm1yrcAwInKB4salO7liNlSPMAI285qtQsDIFYUuwiF14Glayw%2FiHNFAYtdhPkHAbfAwqoJoQ6yTmjXlNyXhDpR4ejvD028lD01LYAVCjf%2BuCIbo8Qt3UOIX90%2B7sQR8wgriXdVm41YKESicy5cpT2CUAPkfie2BsJpc2x2JHQ4QgUUy1AvG%2B5ywtWXJDWtuCjD2QSbI2CuzvoM59xMCqRL9JgKFszmeNq0Tacb2R4%2BcaoJtACMxhqDfjAvLU5oLQZGlUON4YdP23%2B0Z%2FBI9QMGab33s7%2Fkx6qa1N9J7vFIrIDRr43kIWF%2BU3i2X4dv2x%2FmeTe8HZfzNpr22QtuH9SCulmDynU94%2FnmE9XI1BFESni%2BqAcC3UNMXetVeRO%2Fh63nPt5p8zJaCnQdjvLeVhYBhZL%2BVcnJ4X2Q4GqxxTP1d3NP%2BpYEllebgs7UAlOAjyEZ%2BT1QaMMsIv29dUZ1aSNJgNsozXZ%2BVhxkUiDv%2B%2Bm1cG1v4UI8QX0Anzn7uHd1MrOdL%2BaZ9%2FWe7gQMB9rMNWVaH6DTP3wifJ5Qb3tetEn8eiQBedq%2BPyQOU1MWBnjzu6agU1mC9%2FgvRxrsNxuP%2BB%2Fn4Y8CUxzCS12W3QyHq%2F8yXaOI9flw8QQzRXI1CW656rpMOy8iL0GOqUBOyEgbyEVZmV7UVtHGjsWzJSTw0mYHuH998R4fN%2FU8gePMyNNjba180%2Bgp5bkujFqEUmrbMzfvftFBHs1g7KHG9AgvCyV8sj9xOs2Hwg8rjSj6AIRHIDXJFrGhAyVTTz%2FAGOW0g4JZJo%2BlQOIdpAGxE4uoEA34MVr50dmLRdImwxMyaz7SNl8vL2Es47TFLfliMU%2BeQlR7v8mVJ9praM2ZhryZ5pO&X-Amz-Signature=c035e610b40a9d05fdc1920719ac24e19eea569df94fffb19b2aaee6fc1620a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
