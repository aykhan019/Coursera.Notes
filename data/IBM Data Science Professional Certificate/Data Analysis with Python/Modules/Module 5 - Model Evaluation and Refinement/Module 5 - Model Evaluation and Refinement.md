

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW7RNK3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDg1ootHERDB3DLABC8jyE4UfUbAcEfcqlC058FaXN9zAiEA9XkyoJeRbGW1vN0TY0DJqNKHrGmZjlBNzdBPVqY6z88q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDIJjifdClLco7uxKECrcA9WsrLIHMuqJeSwYcsTiKFM9b20dASaexKQSCjL9JVAkhmXj%2BuO5ziwspQiKZ2AKMLa8eqrjF1ggLpr%2BXNJFb7%2BZiqXNnqKG%2FGgsR%2Fsrg1E8gvaNowQF8%2Fa4MfmFnmBn%2FXKzbm2k2wsXBDouXqRGSEYIkzl1kVRVY6inmafTkMRDjv%2FryLUP4VF%2BuDfQWUOqS2KviBOIqlaGrO3C%2FjivLypRzR9TRfQm%2BctUKOF1H%2BRLUeEolkctxGph36va%2Fauxw3nzEqqO2IXiTPYs3lwdGWxweDDyYfIRu1mSaQfAWej9gbyatB%2BDdrnPcVj4aJ8P0N9WlzRIPL5dDLliBkXZ7hpBT6r2lvJvzxPfEIOZ93bIhbq7g%2B%2BifTsvIcbSG5T5NYXoBmcrgMMHCE9Em0Aj39w1wLz1sjS2xufYiAG0JA39RtS%2B2TGapNWW2pzLfN%2Bgcy5VfeZg%2F7ZTD2xLgpGuq6IjhqbQ4f6xqBPT4UkshTIBB5S0AFeU6oL60IEtmGTvlbe75G7DHn%2BxDCVo0IfN4ObaSPgRr9sLi9cie10htLlS7ghHatdhuQGbuYn01LhTyJXNfa8lCyHp9Z1r%2FbCFNwZu%2BQvn96Xcd63WCyRceRo5%2FsepbXlU2VjALz9vML3Wgb0GOqUBFZKyi2hIR9M9Gr59O7KvygSVQd3%2Bdz6MYGh3wYKmnuXIPFlrh5S7ubPDGNW2RvZozZ7rLFDGr0NOk%2FTpoe4KoRK%2BRYlifx0SP39uOQqMCvmpdbPmAmsaYGX4EbE2IbUhb3e85W51fQvwmXa3%2BqF95pR9I%2BrCyFJ%2BCLwiHk%2FoGGp9SDALdBagqnWGbAJ37%2Bg7STilla98qxZnqZC2TiMaSeLNr%2FdV&X-Amz-Signature=ea29bd701e352b393bd738a3c202fea9657cb47675047e51f95e587a0974b895&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW7RNK3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDg1ootHERDB3DLABC8jyE4UfUbAcEfcqlC058FaXN9zAiEA9XkyoJeRbGW1vN0TY0DJqNKHrGmZjlBNzdBPVqY6z88q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDIJjifdClLco7uxKECrcA9WsrLIHMuqJeSwYcsTiKFM9b20dASaexKQSCjL9JVAkhmXj%2BuO5ziwspQiKZ2AKMLa8eqrjF1ggLpr%2BXNJFb7%2BZiqXNnqKG%2FGgsR%2Fsrg1E8gvaNowQF8%2Fa4MfmFnmBn%2FXKzbm2k2wsXBDouXqRGSEYIkzl1kVRVY6inmafTkMRDjv%2FryLUP4VF%2BuDfQWUOqS2KviBOIqlaGrO3C%2FjivLypRzR9TRfQm%2BctUKOF1H%2BRLUeEolkctxGph36va%2Fauxw3nzEqqO2IXiTPYs3lwdGWxweDDyYfIRu1mSaQfAWej9gbyatB%2BDdrnPcVj4aJ8P0N9WlzRIPL5dDLliBkXZ7hpBT6r2lvJvzxPfEIOZ93bIhbq7g%2B%2BifTsvIcbSG5T5NYXoBmcrgMMHCE9Em0Aj39w1wLz1sjS2xufYiAG0JA39RtS%2B2TGapNWW2pzLfN%2Bgcy5VfeZg%2F7ZTD2xLgpGuq6IjhqbQ4f6xqBPT4UkshTIBB5S0AFeU6oL60IEtmGTvlbe75G7DHn%2BxDCVo0IfN4ObaSPgRr9sLi9cie10htLlS7ghHatdhuQGbuYn01LhTyJXNfa8lCyHp9Z1r%2FbCFNwZu%2BQvn96Xcd63WCyRceRo5%2FsepbXlU2VjALz9vML3Wgb0GOqUBFZKyi2hIR9M9Gr59O7KvygSVQd3%2Bdz6MYGh3wYKmnuXIPFlrh5S7ubPDGNW2RvZozZ7rLFDGr0NOk%2FTpoe4KoRK%2BRYlifx0SP39uOQqMCvmpdbPmAmsaYGX4EbE2IbUhb3e85W51fQvwmXa3%2BqF95pR9I%2BrCyFJ%2BCLwiHk%2FoGGp9SDALdBagqnWGbAJ37%2Bg7STilla98qxZnqZC2TiMaSeLNr%2FdV&X-Amz-Signature=0a6a811dfdc8728cc8483011debd34fd36ac882e3a907b132b63dbb3cfd76373&X-Amz-SignedHeaders=host&x-id=GetObject)
**Example Code**:
```python
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# X_train: Training data for the predictors
# X_test: Testing data for the predictors
# y_train: Training data for the target variable
# y_test: Testing data for the target variable
# test_size=0.3: 30% of the data will be used for testing, and 70% will be used for training
# random_state=42:Ensures reproducibility of the split. Using the same random state will produce the same split every time
```
### Generalization Error
- **Generalization Error**: Measures how well the model predicts new data. The error obtained using testing data approximates this error.
### Cross-Validation
**Cross-Validation**: A technique to assess the model's performance and estimate generalization error by splitting the data into multiple folds.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW7RNK3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDg1ootHERDB3DLABC8jyE4UfUbAcEfcqlC058FaXN9zAiEA9XkyoJeRbGW1vN0TY0DJqNKHrGmZjlBNzdBPVqY6z88q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDIJjifdClLco7uxKECrcA9WsrLIHMuqJeSwYcsTiKFM9b20dASaexKQSCjL9JVAkhmXj%2BuO5ziwspQiKZ2AKMLa8eqrjF1ggLpr%2BXNJFb7%2BZiqXNnqKG%2FGgsR%2Fsrg1E8gvaNowQF8%2Fa4MfmFnmBn%2FXKzbm2k2wsXBDouXqRGSEYIkzl1kVRVY6inmafTkMRDjv%2FryLUP4VF%2BuDfQWUOqS2KviBOIqlaGrO3C%2FjivLypRzR9TRfQm%2BctUKOF1H%2BRLUeEolkctxGph36va%2Fauxw3nzEqqO2IXiTPYs3lwdGWxweDDyYfIRu1mSaQfAWej9gbyatB%2BDdrnPcVj4aJ8P0N9WlzRIPL5dDLliBkXZ7hpBT6r2lvJvzxPfEIOZ93bIhbq7g%2B%2BifTsvIcbSG5T5NYXoBmcrgMMHCE9Em0Aj39w1wLz1sjS2xufYiAG0JA39RtS%2B2TGapNWW2pzLfN%2Bgcy5VfeZg%2F7ZTD2xLgpGuq6IjhqbQ4f6xqBPT4UkshTIBB5S0AFeU6oL60IEtmGTvlbe75G7DHn%2BxDCVo0IfN4ObaSPgRr9sLi9cie10htLlS7ghHatdhuQGbuYn01LhTyJXNfa8lCyHp9Z1r%2FbCFNwZu%2BQvn96Xcd63WCyRceRo5%2FsepbXlU2VjALz9vML3Wgb0GOqUBFZKyi2hIR9M9Gr59O7KvygSVQd3%2Bdz6MYGh3wYKmnuXIPFlrh5S7ubPDGNW2RvZozZ7rLFDGr0NOk%2FTpoe4KoRK%2BRYlifx0SP39uOQqMCvmpdbPmAmsaYGX4EbE2IbUhb3e85W51fQvwmXa3%2BqF95pR9I%2BrCyFJ%2BCLwiHk%2FoGGp9SDALdBagqnWGbAJ37%2Bg7STilla98qxZnqZC2TiMaSeLNr%2FdV&X-Amz-Signature=547320a5e2ee90f819cafa507e9ca102f944f95f5172c4f644ab5c9fb48e998a&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW7RNK3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDg1ootHERDB3DLABC8jyE4UfUbAcEfcqlC058FaXN9zAiEA9XkyoJeRbGW1vN0TY0DJqNKHrGmZjlBNzdBPVqY6z88q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDIJjifdClLco7uxKECrcA9WsrLIHMuqJeSwYcsTiKFM9b20dASaexKQSCjL9JVAkhmXj%2BuO5ziwspQiKZ2AKMLa8eqrjF1ggLpr%2BXNJFb7%2BZiqXNnqKG%2FGgsR%2Fsrg1E8gvaNowQF8%2Fa4MfmFnmBn%2FXKzbm2k2wsXBDouXqRGSEYIkzl1kVRVY6inmafTkMRDjv%2FryLUP4VF%2BuDfQWUOqS2KviBOIqlaGrO3C%2FjivLypRzR9TRfQm%2BctUKOF1H%2BRLUeEolkctxGph36va%2Fauxw3nzEqqO2IXiTPYs3lwdGWxweDDyYfIRu1mSaQfAWej9gbyatB%2BDdrnPcVj4aJ8P0N9WlzRIPL5dDLliBkXZ7hpBT6r2lvJvzxPfEIOZ93bIhbq7g%2B%2BifTsvIcbSG5T5NYXoBmcrgMMHCE9Em0Aj39w1wLz1sjS2xufYiAG0JA39RtS%2B2TGapNWW2pzLfN%2Bgcy5VfeZg%2F7ZTD2xLgpGuq6IjhqbQ4f6xqBPT4UkshTIBB5S0AFeU6oL60IEtmGTvlbe75G7DHn%2BxDCVo0IfN4ObaSPgRr9sLi9cie10htLlS7ghHatdhuQGbuYn01LhTyJXNfa8lCyHp9Z1r%2FbCFNwZu%2BQvn96Xcd63WCyRceRo5%2FsepbXlU2VjALz9vML3Wgb0GOqUBFZKyi2hIR9M9Gr59O7KvygSVQd3%2Bdz6MYGh3wYKmnuXIPFlrh5S7ubPDGNW2RvZozZ7rLFDGr0NOk%2FTpoe4KoRK%2BRYlifx0SP39uOQqMCvmpdbPmAmsaYGX4EbE2IbUhb3e85W51fQvwmXa3%2BqF95pR9I%2BrCyFJ%2BCLwiHk%2FoGGp9SDALdBagqnWGbAJ37%2Bg7STilla98qxZnqZC2TiMaSeLNr%2FdV&X-Amz-Signature=7c71859b2cbc48075c04aa1c5b30aa4b8532ccea6da56d0ae2ba05226340c3a0&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW7RNK3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDg1ootHERDB3DLABC8jyE4UfUbAcEfcqlC058FaXN9zAiEA9XkyoJeRbGW1vN0TY0DJqNKHrGmZjlBNzdBPVqY6z88q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDIJjifdClLco7uxKECrcA9WsrLIHMuqJeSwYcsTiKFM9b20dASaexKQSCjL9JVAkhmXj%2BuO5ziwspQiKZ2AKMLa8eqrjF1ggLpr%2BXNJFb7%2BZiqXNnqKG%2FGgsR%2Fsrg1E8gvaNowQF8%2Fa4MfmFnmBn%2FXKzbm2k2wsXBDouXqRGSEYIkzl1kVRVY6inmafTkMRDjv%2FryLUP4VF%2BuDfQWUOqS2KviBOIqlaGrO3C%2FjivLypRzR9TRfQm%2BctUKOF1H%2BRLUeEolkctxGph36va%2Fauxw3nzEqqO2IXiTPYs3lwdGWxweDDyYfIRu1mSaQfAWej9gbyatB%2BDdrnPcVj4aJ8P0N9WlzRIPL5dDLliBkXZ7hpBT6r2lvJvzxPfEIOZ93bIhbq7g%2B%2BifTsvIcbSG5T5NYXoBmcrgMMHCE9Em0Aj39w1wLz1sjS2xufYiAG0JA39RtS%2B2TGapNWW2pzLfN%2Bgcy5VfeZg%2F7ZTD2xLgpGuq6IjhqbQ4f6xqBPT4UkshTIBB5S0AFeU6oL60IEtmGTvlbe75G7DHn%2BxDCVo0IfN4ObaSPgRr9sLi9cie10htLlS7ghHatdhuQGbuYn01LhTyJXNfa8lCyHp9Z1r%2FbCFNwZu%2BQvn96Xcd63WCyRceRo5%2FsepbXlU2VjALz9vML3Wgb0GOqUBFZKyi2hIR9M9Gr59O7KvygSVQd3%2Bdz6MYGh3wYKmnuXIPFlrh5S7ubPDGNW2RvZozZ7rLFDGr0NOk%2FTpoe4KoRK%2BRYlifx0SP39uOQqMCvmpdbPmAmsaYGX4EbE2IbUhb3e85W51fQvwmXa3%2BqF95pR9I%2BrCyFJ%2BCLwiHk%2FoGGp9SDALdBagqnWGbAJ37%2Bg7STilla98qxZnqZC2TiMaSeLNr%2FdV&X-Amz-Signature=7532fd576efb8cc9d0928a0895519efc045e9602b864afd31325543b3505b540&X-Amz-SignedHeaders=host&x-id=GetObject)
### Cross-Val Predict
**cross_val_predict** is used when you want to obtain the predicted values for each test fold during the cross-validation process. It returns the prediction for each data point when it was in the test set. This is useful for:
5. **Visualizing Predictions**: You can plot the predicted values against the actual values to see how well the model performs across the entire dataset.
6. **Diagnostics**: It helps in analyzing the residuals (differences between actual and predicted values) to diagnose model performance.
#### Example in Python
Here's an example using `cross_val_predict`:
```python
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Example dataset
X = np.random.rand(100, 5)
y = np.random.rand(100)

# Initialize the model
model = LinearRegression()

# Get cross-validated predictions
y_pred = cross_val_predict(model, X, y, cv=5)

# Plot actual vs. predicted values
plt.scatter(y, y_pred)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Cross-Validated Predictions')
plt.show()
```
In this example:
- `cross_val_predict` returns the predicted values for each test fold during the 5-fold cross-validation.
- A scatter plot is created to visualize the actual vs. predicted values.
#### Summary
- **Training Set**: Used to build the model.
- **Testing Set**: Used to evaluate model performance.
- **Cross-Validation**: Provides a robust estimate of model performance by averaging results across multiple folds.
___
## Model Selection and Polynomial Regression
When selecting the best polynomial order, our goal is to provide the best estimate of the
function $ y(x) $.
### Noise in Data
**Noise** in data refers to random variations or errors that obscure the true underlying patterns or relationships. It can come from various sources and affects the accuracy of models.
### **Underfitting** 
**Underfitting** occurs when the model is too simple to fit the data:
- Example: Fitting a linear function to data generated from a higher-order polynomial plus noise results in many errors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW7RNK3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDg1ootHERDB3DLABC8jyE4UfUbAcEfcqlC058FaXN9zAiEA9XkyoJeRbGW1vN0TY0DJqNKHrGmZjlBNzdBPVqY6z88q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDIJjifdClLco7uxKECrcA9WsrLIHMuqJeSwYcsTiKFM9b20dASaexKQSCjL9JVAkhmXj%2BuO5ziwspQiKZ2AKMLa8eqrjF1ggLpr%2BXNJFb7%2BZiqXNnqKG%2FGgsR%2Fsrg1E8gvaNowQF8%2Fa4MfmFnmBn%2FXKzbm2k2wsXBDouXqRGSEYIkzl1kVRVY6inmafTkMRDjv%2FryLUP4VF%2BuDfQWUOqS2KviBOIqlaGrO3C%2FjivLypRzR9TRfQm%2BctUKOF1H%2BRLUeEolkctxGph36va%2Fauxw3nzEqqO2IXiTPYs3lwdGWxweDDyYfIRu1mSaQfAWej9gbyatB%2BDdrnPcVj4aJ8P0N9WlzRIPL5dDLliBkXZ7hpBT6r2lvJvzxPfEIOZ93bIhbq7g%2B%2BifTsvIcbSG5T5NYXoBmcrgMMHCE9Em0Aj39w1wLz1sjS2xufYiAG0JA39RtS%2B2TGapNWW2pzLfN%2Bgcy5VfeZg%2F7ZTD2xLgpGuq6IjhqbQ4f6xqBPT4UkshTIBB5S0AFeU6oL60IEtmGTvlbe75G7DHn%2BxDCVo0IfN4ObaSPgRr9sLi9cie10htLlS7ghHatdhuQGbuYn01LhTyJXNfa8lCyHp9Z1r%2FbCFNwZu%2BQvn96Xcd63WCyRceRo5%2FsepbXlU2VjALz9vML3Wgb0GOqUBFZKyi2hIR9M9Gr59O7KvygSVQd3%2Bdz6MYGh3wYKmnuXIPFlrh5S7ubPDGNW2RvZozZ7rLFDGr0NOk%2FTpoe4KoRK%2BRYlifx0SP39uOQqMCvmpdbPmAmsaYGX4EbE2IbUhb3e85W51fQvwmXa3%2BqF95pR9I%2BrCyFJ%2BCLwiHk%2FoGGp9SDALdBagqnWGbAJ37%2Bg7STilla98qxZnqZC2TiMaSeLNr%2FdV&X-Amz-Signature=c44eb666abb64483f5507928342b4cbcb553488c865c8c7308ddde7fafbf17e0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW7RNK3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDg1ootHERDB3DLABC8jyE4UfUbAcEfcqlC058FaXN9zAiEA9XkyoJeRbGW1vN0TY0DJqNKHrGmZjlBNzdBPVqY6z88q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDIJjifdClLco7uxKECrcA9WsrLIHMuqJeSwYcsTiKFM9b20dASaexKQSCjL9JVAkhmXj%2BuO5ziwspQiKZ2AKMLa8eqrjF1ggLpr%2BXNJFb7%2BZiqXNnqKG%2FGgsR%2Fsrg1E8gvaNowQF8%2Fa4MfmFnmBn%2FXKzbm2k2wsXBDouXqRGSEYIkzl1kVRVY6inmafTkMRDjv%2FryLUP4VF%2BuDfQWUOqS2KviBOIqlaGrO3C%2FjivLypRzR9TRfQm%2BctUKOF1H%2BRLUeEolkctxGph36va%2Fauxw3nzEqqO2IXiTPYs3lwdGWxweDDyYfIRu1mSaQfAWej9gbyatB%2BDdrnPcVj4aJ8P0N9WlzRIPL5dDLliBkXZ7hpBT6r2lvJvzxPfEIOZ93bIhbq7g%2B%2BifTsvIcbSG5T5NYXoBmcrgMMHCE9Em0Aj39w1wLz1sjS2xufYiAG0JA39RtS%2B2TGapNWW2pzLfN%2Bgcy5VfeZg%2F7ZTD2xLgpGuq6IjhqbQ4f6xqBPT4UkshTIBB5S0AFeU6oL60IEtmGTvlbe75G7DHn%2BxDCVo0IfN4ObaSPgRr9sLi9cie10htLlS7ghHatdhuQGbuYn01LhTyJXNfa8lCyHp9Z1r%2FbCFNwZu%2BQvn96Xcd63WCyRceRo5%2FsepbXlU2VjALz9vML3Wgb0GOqUBFZKyi2hIR9M9Gr59O7KvygSVQd3%2Bdz6MYGh3wYKmnuXIPFlrh5S7ubPDGNW2RvZozZ7rLFDGr0NOk%2FTpoe4KoRK%2BRYlifx0SP39uOQqMCvmpdbPmAmsaYGX4EbE2IbUhb3e85W51fQvwmXa3%2BqF95pR9I%2BrCyFJ%2BCLwiHk%2FoGGp9SDALdBagqnWGbAJ37%2Bg7STilla98qxZnqZC2TiMaSeLNr%2FdV&X-Amz-Signature=102f3958fd623956c77c364a665e4773324de956ae8f13d5c8bb772a786ecebd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW7RNK3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDg1ootHERDB3DLABC8jyE4UfUbAcEfcqlC058FaXN9zAiEA9XkyoJeRbGW1vN0TY0DJqNKHrGmZjlBNzdBPVqY6z88q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDIJjifdClLco7uxKECrcA9WsrLIHMuqJeSwYcsTiKFM9b20dASaexKQSCjL9JVAkhmXj%2BuO5ziwspQiKZ2AKMLa8eqrjF1ggLpr%2BXNJFb7%2BZiqXNnqKG%2FGgsR%2Fsrg1E8gvaNowQF8%2Fa4MfmFnmBn%2FXKzbm2k2wsXBDouXqRGSEYIkzl1kVRVY6inmafTkMRDjv%2FryLUP4VF%2BuDfQWUOqS2KviBOIqlaGrO3C%2FjivLypRzR9TRfQm%2BctUKOF1H%2BRLUeEolkctxGph36va%2Fauxw3nzEqqO2IXiTPYs3lwdGWxweDDyYfIRu1mSaQfAWej9gbyatB%2BDdrnPcVj4aJ8P0N9WlzRIPL5dDLliBkXZ7hpBT6r2lvJvzxPfEIOZ93bIhbq7g%2B%2BifTsvIcbSG5T5NYXoBmcrgMMHCE9Em0Aj39w1wLz1sjS2xufYiAG0JA39RtS%2B2TGapNWW2pzLfN%2Bgcy5VfeZg%2F7ZTD2xLgpGuq6IjhqbQ4f6xqBPT4UkshTIBB5S0AFeU6oL60IEtmGTvlbe75G7DHn%2BxDCVo0IfN4ObaSPgRr9sLi9cie10htLlS7ghHatdhuQGbuYn01LhTyJXNfa8lCyHp9Z1r%2FbCFNwZu%2BQvn96Xcd63WCyRceRo5%2FsepbXlU2VjALz9vML3Wgb0GOqUBFZKyi2hIR9M9Gr59O7KvygSVQd3%2Bdz6MYGh3wYKmnuXIPFlrh5S7ubPDGNW2RvZozZ7rLFDGr0NOk%2FTpoe4KoRK%2BRYlifx0SP39uOQqMCvmpdbPmAmsaYGX4EbE2IbUhb3e85W51fQvwmXa3%2BqF95pR9I%2BrCyFJ%2BCLwiHk%2FoGGp9SDALdBagqnWGbAJ37%2Bg7STilla98qxZnqZC2TiMaSeLNr%2FdV&X-Amz-Signature=d53e7aa4a9d3e2dbe7ec1ea5e8b76a91975ab410c68b10ac29a475fd074d1942&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW7RNK3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDg1ootHERDB3DLABC8jyE4UfUbAcEfcqlC058FaXN9zAiEA9XkyoJeRbGW1vN0TY0DJqNKHrGmZjlBNzdBPVqY6z88q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDIJjifdClLco7uxKECrcA9WsrLIHMuqJeSwYcsTiKFM9b20dASaexKQSCjL9JVAkhmXj%2BuO5ziwspQiKZ2AKMLa8eqrjF1ggLpr%2BXNJFb7%2BZiqXNnqKG%2FGgsR%2Fsrg1E8gvaNowQF8%2Fa4MfmFnmBn%2FXKzbm2k2wsXBDouXqRGSEYIkzl1kVRVY6inmafTkMRDjv%2FryLUP4VF%2BuDfQWUOqS2KviBOIqlaGrO3C%2FjivLypRzR9TRfQm%2BctUKOF1H%2BRLUeEolkctxGph36va%2Fauxw3nzEqqO2IXiTPYs3lwdGWxweDDyYfIRu1mSaQfAWej9gbyatB%2BDdrnPcVj4aJ8P0N9WlzRIPL5dDLliBkXZ7hpBT6r2lvJvzxPfEIOZ93bIhbq7g%2B%2BifTsvIcbSG5T5NYXoBmcrgMMHCE9Em0Aj39w1wLz1sjS2xufYiAG0JA39RtS%2B2TGapNWW2pzLfN%2Bgcy5VfeZg%2F7ZTD2xLgpGuq6IjhqbQ4f6xqBPT4UkshTIBB5S0AFeU6oL60IEtmGTvlbe75G7DHn%2BxDCVo0IfN4ObaSPgRr9sLi9cie10htLlS7ghHatdhuQGbuYn01LhTyJXNfa8lCyHp9Z1r%2FbCFNwZu%2BQvn96Xcd63WCyRceRo5%2FsepbXlU2VjALz9vML3Wgb0GOqUBFZKyi2hIR9M9Gr59O7KvygSVQd3%2Bdz6MYGh3wYKmnuXIPFlrh5S7ubPDGNW2RvZozZ7rLFDGr0NOk%2FTpoe4KoRK%2BRYlifx0SP39uOQqMCvmpdbPmAmsaYGX4EbE2IbUhb3e85W51fQvwmXa3%2BqF95pR9I%2BrCyFJ%2BCLwiHk%2FoGGp9SDALdBagqnWGbAJ37%2Bg7STilla98qxZnqZC2TiMaSeLNr%2FdV&X-Amz-Signature=3e65ac402230cea9667042530650d37ce2bb2c3c247ccd80e24db4910bcde00f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JBV4EYF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFTlHJRJuL9Xu3MxSe3SwQ7kT%2F%2FJXpMD054jRGOK%2BwQxAiAIn07sbGBpJPwKJzP%2Fg%2BY77ESD8PskVlzhVRgWZAcHgyr%2FAwgQEAAaDDYzNzQyMzE4MzgwNSIMDj2b6ZJ2%2FWjSIQT7KtwD61F1Q4zdTOCP%2B40tHshvqmD8PCcG4l3fTwxtlLp9%2BpWMA%2FWAj4lIAem6wQH%2BT3A40RSesSe85hzTuNqN%2Bo0LhgFiNwP%2FCUAfIvdThfgfuJ09Z4WM%2FpDYUDgPssHyF%2FaUzMC%2BMBeGaW1kzsOCTZIost4U5V3gPxWvzpF99FrZaj1hbUhDj0d8V4Z4wjVAqWBCR6R%2FiSqNDabh%2FiXXMHjSUuTp0cjizxhcPdZ4X4MoKsLKPgY%2FCGDp%2FwADwDOwGO61W5q9n4se7Yb7vmgOdPFEt9bKzKCYeCN7LSGFHLyzoPUeDggJhnHRnInKeBtP4BtP6z1KQXcWIia%2B7ypL5HrRqKiQ%2BIPSozmM0oBOzIvzLY8bAegnbMe%2BywohGnr0xsK7B0Es6yEQLONPfWc8t27KIOTruCsXKGyhepOaM3c%2BNHm4gbQvdmiOnXmzl21vmlDSclthLMw6JAVO4evctsfxpaMzE7YubZUtH2rgFFzv2oyR99vU8qXB5U%2F%2BfGZ8rgFAcO1dfMYBJUYlG8yDA4VMF6gX4Rl4%2FcTCMbDM15XIX9NAVFji2EYadK2ip%2BGRJ5mSUKzNaIsv9i8IXbJouUJTHtqdEMP3zzAfO4LKKvnPHIUdduADnIG3%2BajS2a8whtaBvQY6pgGb0I8Ur0gsv%2BuCuKtjuEr%2BoADDbvGOWW91FShraRZjPrpDUuGELzinbCpQ65RJl7K%2BWcxm2vdjp3bXym2M5v72OdOCqYh6FXSuyFWK6pRCd8t8HYu7AWPFg7E0PsoXreUpjd9wL21ZH6ITmTtI4DpC%2FzEQbkARv%2FFIIAQP9UF1YxL%2F43u%2Bl6zH5AjYPAQdEmFYKBUdJOEm27l%2Fr3mWNa8WULsGdVfV&X-Amz-Signature=c8e13e762af5dfa1a966865290f75c0ebbed4f881b9f6f71a2ad0a162360da8e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JBV4EYF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFTlHJRJuL9Xu3MxSe3SwQ7kT%2F%2FJXpMD054jRGOK%2BwQxAiAIn07sbGBpJPwKJzP%2Fg%2BY77ESD8PskVlzhVRgWZAcHgyr%2FAwgQEAAaDDYzNzQyMzE4MzgwNSIMDj2b6ZJ2%2FWjSIQT7KtwD61F1Q4zdTOCP%2B40tHshvqmD8PCcG4l3fTwxtlLp9%2BpWMA%2FWAj4lIAem6wQH%2BT3A40RSesSe85hzTuNqN%2Bo0LhgFiNwP%2FCUAfIvdThfgfuJ09Z4WM%2FpDYUDgPssHyF%2FaUzMC%2BMBeGaW1kzsOCTZIost4U5V3gPxWvzpF99FrZaj1hbUhDj0d8V4Z4wjVAqWBCR6R%2FiSqNDabh%2FiXXMHjSUuTp0cjizxhcPdZ4X4MoKsLKPgY%2FCGDp%2FwADwDOwGO61W5q9n4se7Yb7vmgOdPFEt9bKzKCYeCN7LSGFHLyzoPUeDggJhnHRnInKeBtP4BtP6z1KQXcWIia%2B7ypL5HrRqKiQ%2BIPSozmM0oBOzIvzLY8bAegnbMe%2BywohGnr0xsK7B0Es6yEQLONPfWc8t27KIOTruCsXKGyhepOaM3c%2BNHm4gbQvdmiOnXmzl21vmlDSclthLMw6JAVO4evctsfxpaMzE7YubZUtH2rgFFzv2oyR99vU8qXB5U%2F%2BfGZ8rgFAcO1dfMYBJUYlG8yDA4VMF6gX4Rl4%2FcTCMbDM15XIX9NAVFji2EYadK2ip%2BGRJ5mSUKzNaIsv9i8IXbJouUJTHtqdEMP3zzAfO4LKKvnPHIUdduADnIG3%2BajS2a8whtaBvQY6pgGb0I8Ur0gsv%2BuCuKtjuEr%2BoADDbvGOWW91FShraRZjPrpDUuGELzinbCpQ65RJl7K%2BWcxm2vdjp3bXym2M5v72OdOCqYh6FXSuyFWK6pRCd8t8HYu7AWPFg7E0PsoXreUpjd9wL21ZH6ITmTtI4DpC%2FzEQbkARv%2FFIIAQP9UF1YxL%2F43u%2Bl6zH5AjYPAQdEmFYKBUdJOEm27l%2Fr3mWNa8WULsGdVfV&X-Amz-Signature=97e0b5b42468c2bfd8104c5761c580aa8d6c906e859af28eac35c4fd8f33c6fd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JBV4EYF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFTlHJRJuL9Xu3MxSe3SwQ7kT%2F%2FJXpMD054jRGOK%2BwQxAiAIn07sbGBpJPwKJzP%2Fg%2BY77ESD8PskVlzhVRgWZAcHgyr%2FAwgQEAAaDDYzNzQyMzE4MzgwNSIMDj2b6ZJ2%2FWjSIQT7KtwD61F1Q4zdTOCP%2B40tHshvqmD8PCcG4l3fTwxtlLp9%2BpWMA%2FWAj4lIAem6wQH%2BT3A40RSesSe85hzTuNqN%2Bo0LhgFiNwP%2FCUAfIvdThfgfuJ09Z4WM%2FpDYUDgPssHyF%2FaUzMC%2BMBeGaW1kzsOCTZIost4U5V3gPxWvzpF99FrZaj1hbUhDj0d8V4Z4wjVAqWBCR6R%2FiSqNDabh%2FiXXMHjSUuTp0cjizxhcPdZ4X4MoKsLKPgY%2FCGDp%2FwADwDOwGO61W5q9n4se7Yb7vmgOdPFEt9bKzKCYeCN7LSGFHLyzoPUeDggJhnHRnInKeBtP4BtP6z1KQXcWIia%2B7ypL5HrRqKiQ%2BIPSozmM0oBOzIvzLY8bAegnbMe%2BywohGnr0xsK7B0Es6yEQLONPfWc8t27KIOTruCsXKGyhepOaM3c%2BNHm4gbQvdmiOnXmzl21vmlDSclthLMw6JAVO4evctsfxpaMzE7YubZUtH2rgFFzv2oyR99vU8qXB5U%2F%2BfGZ8rgFAcO1dfMYBJUYlG8yDA4VMF6gX4Rl4%2FcTCMbDM15XIX9NAVFji2EYadK2ip%2BGRJ5mSUKzNaIsv9i8IXbJouUJTHtqdEMP3zzAfO4LKKvnPHIUdduADnIG3%2BajS2a8whtaBvQY6pgGb0I8Ur0gsv%2BuCuKtjuEr%2BoADDbvGOWW91FShraRZjPrpDUuGELzinbCpQ65RJl7K%2BWcxm2vdjp3bXym2M5v72OdOCqYh6FXSuyFWK6pRCd8t8HYu7AWPFg7E0PsoXreUpjd9wL21ZH6ITmTtI4DpC%2FzEQbkARv%2FFIIAQP9UF1YxL%2F43u%2Bl6zH5AjYPAQdEmFYKBUdJOEm27l%2Fr3mWNa8WULsGdVfV&X-Amz-Signature=210a68d2f376f41ebee5a440375cc16a604ba59451009bb6b4f3e154800138bd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW7RNK3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDg1ootHERDB3DLABC8jyE4UfUbAcEfcqlC058FaXN9zAiEA9XkyoJeRbGW1vN0TY0DJqNKHrGmZjlBNzdBPVqY6z88q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDIJjifdClLco7uxKECrcA9WsrLIHMuqJeSwYcsTiKFM9b20dASaexKQSCjL9JVAkhmXj%2BuO5ziwspQiKZ2AKMLa8eqrjF1ggLpr%2BXNJFb7%2BZiqXNnqKG%2FGgsR%2Fsrg1E8gvaNowQF8%2Fa4MfmFnmBn%2FXKzbm2k2wsXBDouXqRGSEYIkzl1kVRVY6inmafTkMRDjv%2FryLUP4VF%2BuDfQWUOqS2KviBOIqlaGrO3C%2FjivLypRzR9TRfQm%2BctUKOF1H%2BRLUeEolkctxGph36va%2Fauxw3nzEqqO2IXiTPYs3lwdGWxweDDyYfIRu1mSaQfAWej9gbyatB%2BDdrnPcVj4aJ8P0N9WlzRIPL5dDLliBkXZ7hpBT6r2lvJvzxPfEIOZ93bIhbq7g%2B%2BifTsvIcbSG5T5NYXoBmcrgMMHCE9Em0Aj39w1wLz1sjS2xufYiAG0JA39RtS%2B2TGapNWW2pzLfN%2Bgcy5VfeZg%2F7ZTD2xLgpGuq6IjhqbQ4f6xqBPT4UkshTIBB5S0AFeU6oL60IEtmGTvlbe75G7DHn%2BxDCVo0IfN4ObaSPgRr9sLi9cie10htLlS7ghHatdhuQGbuYn01LhTyJXNfa8lCyHp9Z1r%2FbCFNwZu%2BQvn96Xcd63WCyRceRo5%2FsepbXlU2VjALz9vML3Wgb0GOqUBFZKyi2hIR9M9Gr59O7KvygSVQd3%2Bdz6MYGh3wYKmnuXIPFlrh5S7ubPDGNW2RvZozZ7rLFDGr0NOk%2FTpoe4KoRK%2BRYlifx0SP39uOQqMCvmpdbPmAmsaYGX4EbE2IbUhb3e85W51fQvwmXa3%2BqF95pR9I%2BrCyFJ%2BCLwiHk%2FoGGp9SDALdBagqnWGbAJ37%2Bg7STilla98qxZnqZC2TiMaSeLNr%2FdV&X-Amz-Signature=703e91a3f6743a71125fa40a2ea72caeb35e8266ece9e13672482e7e5f3ad917&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Calculating R-squared Values**
7. Create an empty list to store R^2 values.
8. Create a list of different polynomial orders.
9. Iterate through the list using a loop:
	- Create a polynomial feature object with the order as a parameter.
	- Transform the training and test data into polynomial features using the `fit_transform` method.
	- Fit the regression model using the transformed data.
	- Calculate the R^2 value using the test data and store it in the list.
Here's an example of how you can implement this in Python:
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

# Store R^2 values
r2_values = []

# List of polynomial orders
orders = [1, 2, 3, 4]

# Iterate through polynomial orders
for order in orders:
    # Create polynomial features
    poly = PolynomialFeatures(degree=order)
    x_poly = poly.fit_transform(x.reshape(-1, 1))

    # Fit the model
    model = LinearRegression()
    model.fit(x_poly, y)

    # Predict and calculate R^2
    y_pred = model.predict(x_poly)
    r2 = r2_score(y, y_pred)
    r2_values.append(r2)

# Plot R^2 values
plt.plot(orders, r2_values, marker='o')
plt.xlabel('Order of Polynomial')
plt.ylabel('R^2 Value')
plt.title('R^2 Value vs. Polynomial Order')
plt.show()
```
Output:
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW7RNK3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDg1ootHERDB3DLABC8jyE4UfUbAcEfcqlC058FaXN9zAiEA9XkyoJeRbGW1vN0TY0DJqNKHrGmZjlBNzdBPVqY6z88q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDIJjifdClLco7uxKECrcA9WsrLIHMuqJeSwYcsTiKFM9b20dASaexKQSCjL9JVAkhmXj%2BuO5ziwspQiKZ2AKMLa8eqrjF1ggLpr%2BXNJFb7%2BZiqXNnqKG%2FGgsR%2Fsrg1E8gvaNowQF8%2Fa4MfmFnmBn%2FXKzbm2k2wsXBDouXqRGSEYIkzl1kVRVY6inmafTkMRDjv%2FryLUP4VF%2BuDfQWUOqS2KviBOIqlaGrO3C%2FjivLypRzR9TRfQm%2BctUKOF1H%2BRLUeEolkctxGph36va%2Fauxw3nzEqqO2IXiTPYs3lwdGWxweDDyYfIRu1mSaQfAWej9gbyatB%2BDdrnPcVj4aJ8P0N9WlzRIPL5dDLliBkXZ7hpBT6r2lvJvzxPfEIOZ93bIhbq7g%2B%2BifTsvIcbSG5T5NYXoBmcrgMMHCE9Em0Aj39w1wLz1sjS2xufYiAG0JA39RtS%2B2TGapNWW2pzLfN%2Bgcy5VfeZg%2F7ZTD2xLgpGuq6IjhqbQ4f6xqBPT4UkshTIBB5S0AFeU6oL60IEtmGTvlbe75G7DHn%2BxDCVo0IfN4ObaSPgRr9sLi9cie10htLlS7ghHatdhuQGbuYn01LhTyJXNfa8lCyHp9Z1r%2FbCFNwZu%2BQvn96Xcd63WCyRceRo5%2FsepbXlU2VjALz9vML3Wgb0GOqUBFZKyi2hIR9M9Gr59O7KvygSVQd3%2Bdz6MYGh3wYKmnuXIPFlrh5S7ubPDGNW2RvZozZ7rLFDGr0NOk%2FTpoe4KoRK%2BRYlifx0SP39uOQqMCvmpdbPmAmsaYGX4EbE2IbUhb3e85W51fQvwmXa3%2BqF95pR9I%2BrCyFJ%2BCLwiHk%2FoGGp9SDALdBagqnWGbAJ37%2Bg7STilla98qxZnqZC2TiMaSeLNr%2FdV&X-Amz-Signature=97940c98248443d207f3cf2b3a2d989d45512e04af8dbc244e9a74e6e63918ce&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW7RNK3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDg1ootHERDB3DLABC8jyE4UfUbAcEfcqlC058FaXN9zAiEA9XkyoJeRbGW1vN0TY0DJqNKHrGmZjlBNzdBPVqY6z88q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDIJjifdClLco7uxKECrcA9WsrLIHMuqJeSwYcsTiKFM9b20dASaexKQSCjL9JVAkhmXj%2BuO5ziwspQiKZ2AKMLa8eqrjF1ggLpr%2BXNJFb7%2BZiqXNnqKG%2FGgsR%2Fsrg1E8gvaNowQF8%2Fa4MfmFnmBn%2FXKzbm2k2wsXBDouXqRGSEYIkzl1kVRVY6inmafTkMRDjv%2FryLUP4VF%2BuDfQWUOqS2KviBOIqlaGrO3C%2FjivLypRzR9TRfQm%2BctUKOF1H%2BRLUeEolkctxGph36va%2Fauxw3nzEqqO2IXiTPYs3lwdGWxweDDyYfIRu1mSaQfAWej9gbyatB%2BDdrnPcVj4aJ8P0N9WlzRIPL5dDLliBkXZ7hpBT6r2lvJvzxPfEIOZ93bIhbq7g%2B%2BifTsvIcbSG5T5NYXoBmcrgMMHCE9Em0Aj39w1wLz1sjS2xufYiAG0JA39RtS%2B2TGapNWW2pzLfN%2Bgcy5VfeZg%2F7ZTD2xLgpGuq6IjhqbQ4f6xqBPT4UkshTIBB5S0AFeU6oL60IEtmGTvlbe75G7DHn%2BxDCVo0IfN4ObaSPgRr9sLi9cie10htLlS7ghHatdhuQGbuYn01LhTyJXNfa8lCyHp9Z1r%2FbCFNwZu%2BQvn96Xcd63WCyRceRo5%2FsepbXlU2VjALz9vML3Wgb0GOqUBFZKyi2hIR9M9Gr59O7KvygSVQd3%2Bdz6MYGh3wYKmnuXIPFlrh5S7ubPDGNW2RvZozZ7rLFDGr0NOk%2FTpoe4KoRK%2BRYlifx0SP39uOQqMCvmpdbPmAmsaYGX4EbE2IbUhb3e85W51fQvwmXa3%2BqF95pR9I%2BrCyFJ%2BCLwiHk%2FoGGp9SDALdBagqnWGbAJ37%2Bg7STilla98qxZnqZC2TiMaSeLNr%2FdV&X-Amz-Signature=6050133aa4dd55af69268477692e4b14a9af37059c9a1f905ca5ecb0eeb4cf39&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW7RNK3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDg1ootHERDB3DLABC8jyE4UfUbAcEfcqlC058FaXN9zAiEA9XkyoJeRbGW1vN0TY0DJqNKHrGmZjlBNzdBPVqY6z88q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDIJjifdClLco7uxKECrcA9WsrLIHMuqJeSwYcsTiKFM9b20dASaexKQSCjL9JVAkhmXj%2BuO5ziwspQiKZ2AKMLa8eqrjF1ggLpr%2BXNJFb7%2BZiqXNnqKG%2FGgsR%2Fsrg1E8gvaNowQF8%2Fa4MfmFnmBn%2FXKzbm2k2wsXBDouXqRGSEYIkzl1kVRVY6inmafTkMRDjv%2FryLUP4VF%2BuDfQWUOqS2KviBOIqlaGrO3C%2FjivLypRzR9TRfQm%2BctUKOF1H%2BRLUeEolkctxGph36va%2Fauxw3nzEqqO2IXiTPYs3lwdGWxweDDyYfIRu1mSaQfAWej9gbyatB%2BDdrnPcVj4aJ8P0N9WlzRIPL5dDLliBkXZ7hpBT6r2lvJvzxPfEIOZ93bIhbq7g%2B%2BifTsvIcbSG5T5NYXoBmcrgMMHCE9Em0Aj39w1wLz1sjS2xufYiAG0JA39RtS%2B2TGapNWW2pzLfN%2Bgcy5VfeZg%2F7ZTD2xLgpGuq6IjhqbQ4f6xqBPT4UkshTIBB5S0AFeU6oL60IEtmGTvlbe75G7DHn%2BxDCVo0IfN4ObaSPgRr9sLi9cie10htLlS7ghHatdhuQGbuYn01LhTyJXNfa8lCyHp9Z1r%2FbCFNwZu%2BQvn96Xcd63WCyRceRo5%2FsepbXlU2VjALz9vML3Wgb0GOqUBFZKyi2hIR9M9Gr59O7KvygSVQd3%2Bdz6MYGh3wYKmnuXIPFlrh5S7ubPDGNW2RvZozZ7rLFDGr0NOk%2FTpoe4KoRK%2BRYlifx0SP39uOQqMCvmpdbPmAmsaYGX4EbE2IbUhb3e85W51fQvwmXa3%2BqF95pR9I%2BrCyFJ%2BCLwiHk%2FoGGp9SDALdBagqnWGbAJ37%2Bg7STilla98qxZnqZC2TiMaSeLNr%2FdV&X-Amz-Signature=e30edeb3c47114ee1c77162c6ca1e9c8e7357920c9326f7ef3eed2b22af26ede&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW7RNK3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDg1ootHERDB3DLABC8jyE4UfUbAcEfcqlC058FaXN9zAiEA9XkyoJeRbGW1vN0TY0DJqNKHrGmZjlBNzdBPVqY6z88q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDIJjifdClLco7uxKECrcA9WsrLIHMuqJeSwYcsTiKFM9b20dASaexKQSCjL9JVAkhmXj%2BuO5ziwspQiKZ2AKMLa8eqrjF1ggLpr%2BXNJFb7%2BZiqXNnqKG%2FGgsR%2Fsrg1E8gvaNowQF8%2Fa4MfmFnmBn%2FXKzbm2k2wsXBDouXqRGSEYIkzl1kVRVY6inmafTkMRDjv%2FryLUP4VF%2BuDfQWUOqS2KviBOIqlaGrO3C%2FjivLypRzR9TRfQm%2BctUKOF1H%2BRLUeEolkctxGph36va%2Fauxw3nzEqqO2IXiTPYs3lwdGWxweDDyYfIRu1mSaQfAWej9gbyatB%2BDdrnPcVj4aJ8P0N9WlzRIPL5dDLliBkXZ7hpBT6r2lvJvzxPfEIOZ93bIhbq7g%2B%2BifTsvIcbSG5T5NYXoBmcrgMMHCE9Em0Aj39w1wLz1sjS2xufYiAG0JA39RtS%2B2TGapNWW2pzLfN%2Bgcy5VfeZg%2F7ZTD2xLgpGuq6IjhqbQ4f6xqBPT4UkshTIBB5S0AFeU6oL60IEtmGTvlbe75G7DHn%2BxDCVo0IfN4ObaSPgRr9sLi9cie10htLlS7ghHatdhuQGbuYn01LhTyJXNfa8lCyHp9Z1r%2FbCFNwZu%2BQvn96Xcd63WCyRceRo5%2FsepbXlU2VjALz9vML3Wgb0GOqUBFZKyi2hIR9M9Gr59O7KvygSVQd3%2Bdz6MYGh3wYKmnuXIPFlrh5S7ubPDGNW2RvZozZ7rLFDGr0NOk%2FTpoe4KoRK%2BRYlifx0SP39uOQqMCvmpdbPmAmsaYGX4EbE2IbUhb3e85W51fQvwmXa3%2BqF95pR9I%2BrCyFJ%2BCLwiHk%2FoGGp9SDALdBagqnWGbAJ37%2Bg7STilla98qxZnqZC2TiMaSeLNr%2FdV&X-Amz-Signature=09af10350d801bfbadbaa58e500ac02d64190c6e1141a5735b8de7bac25ef496&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQZ325O4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCqsc0TETsCX8KUZ6CEI3M6uHfQRlEDWQ6B96WMT%2BYg5gIgeNYazyutjLsXdPpsqwdornzG6C9wtfbSBORZ1NEjlzIq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDNp9TVeI8P0G6HdS2CrcAxyTAod2UAQcc8ZOiuPqSOgvZm%2BG5FdnrvR1IMnZpHrbA5MHH4hrn%2BYoumR151YECWv93NeU7jRT7EkxNtoSNugkdQWLp8GhhWWH4s9tC3JWOeTkpyKjUqnfPF1vWIfAUMoSZF8c13hfS%2FSZ%2BgKXzKX2zhhBnHmx%2Bc9cQ7y6P%2Bi9aBbibDBYbhQMTZORmEiO58WHgVkBHUe%2B1j8Jupj3H0WwtTnxHFhtGuzeKJy4R%2BB7j5CrpKutSaFib4vQnfp7sU0Vrg5gqxXG6%2FyhAR1qZ006WKYo0CE2PvVlZ2uxy%2BetltlGmzP4SZtdjEStJsr8YU3rTpE5Fwy1xlMmHAoMyxa7S26Mt2pwAssvghdBF0oTOjhLFp09EURKXLOIgOuZTtQ4yQ3enkRnwtvWGDLQEkod4iRNFnadQ4GEqjixHd7zXQTao6%2BUu5pbUTH1xNkEMFTKbiKkeSnGikbUH7pBF2Wm5uaWAz7pvF4O5VS5jNeBocimGR%2BoqjTVOBN6LbFIExyOlr1aPlWNs5rg4ltQ%2FdnYhYn4bcnJuNTtYRLH5gEGgy0L5bLVxQdSrreHYN8PF8BjppUxaiGGMyj760puZ59SoNUYFBEQFL635Qej4fcfMk%2FbuiF56lY1wmXdMJ%2FWgb0GOqUB0NKi6StNva1rbrXF0s44VOkDrZCgyB%2F73vtw1UaUJYJvyH8RsC4z6K%2FFT2oZ6yIHBmCpd42cSjnyD6aYhcG7w3JLwKSBh%2FYzSiPSTMcShbfJHz0q9d1EDyPTMcl%2F%2FZQuyaFyVyE%2FbLTJuxIg%2FUVJDPobuDxfr1cPCwUJwDSi9ctc%2BmSZelnIrGsSN97i6%2FbXygMdzkGkEXV8AjB4AGgx3gmiI617&X-Amz-Signature=753ccff33c90ea0911bb2c25ba048fcece7bbe3d7b6e5112721e3233e2808569&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL3SJKZM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA9tn77sKfH2OPMVmQ%2B13qNOjwt5KYw0H62nx8lH2rDYAiEA1bYfKnBTlSq3EVvvTf1%2BE73SVgMiovoaG7RUCm%2Fi%2Fzgq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDHnfF84JLLAG7SkKQyrcAy1i%2B7IHfNdro7Tr9ULaAJ6ZDt%2FI3QUXSb2%2FBOypfn7EXZVhR0oWg8KIWRaCYdPy2UGF47D0UK%2BMAFDP2TFzexmGRwKlLoadLekj84MyUVUc9Y3G9S73n75SGUFOQ0Xij4JMHe5k2ofTbHoliFrfYnk2oBKlJc6XlRlGn3x6SKve%2Bw2mnWFu84muFm10TXIVi%2F%2Fu2pxeOUBpz23IfEhmzS3r6Nx1olScWFhfXYduo3Pr5QNBfSiltbIm3eJ2xMLlus1C6AZDHLiQElKgRD5lvC94G9w0vE5WG3aPJnVJjHytmOR6gfsQs0KabyyoGb5SJPBSAmqUQW0Rw%2FKLDF%2B443bAq%2B1PIfhQFCLc%2BP44dUsuoUmUHCxRTQeQG0dxauo1rYRqOXWAk%2BVtpmOgLBuAjWJ5s8x0xt4QuVnfqDTZhPWfjjaVakJIDqEJ8ON4ziOoJQt%2FqfXuqEAJOZ%2BL%2F1ma5UWspFy%2Bs2ee1hHYUBNk1eQJ7%2FRotNEQ5EgfzgjfKz7MQUyUFac238cA%2BOzuX%2Fo1tI3w1nfePj0Z5b7vSnLQnvCbirkCIiQbJLZgUGYKRQ6DdZJmaRlGFwA1nP1Oh%2ByFLz%2F%2FsXO1WhrO2yZZ25RvgSjtYEGkTZeodXY%2FPuLbMPTVgb0GOqUBLS359yX1NVp%2FjaOO2N2uh4Zu3v59rNRspma9YfGAn6qlFG5Ttw5tuaEIukaEFf4Fq9CH9d9c0d0FUe757Bhy52bLCkoBqOQ2bhWYH%2BIkyDjhUsOgFDVhY0%2BbQFk6HatP07iMQU93heYVVrkCp9D8RgxbT6zxMUcJmwQsnFMX9VO5LmbpeUsj5iZGBKFPbptCO1MJAku9S9kfXhCLl3F%2FPNJDd9Sh&X-Amz-Signature=3f79a1f47fa1f4ffde19c21784ccd8cc82561247b4685b798833344463073aca&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL3SJKZM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA9tn77sKfH2OPMVmQ%2B13qNOjwt5KYw0H62nx8lH2rDYAiEA1bYfKnBTlSq3EVvvTf1%2BE73SVgMiovoaG7RUCm%2Fi%2Fzgq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDHnfF84JLLAG7SkKQyrcAy1i%2B7IHfNdro7Tr9ULaAJ6ZDt%2FI3QUXSb2%2FBOypfn7EXZVhR0oWg8KIWRaCYdPy2UGF47D0UK%2BMAFDP2TFzexmGRwKlLoadLekj84MyUVUc9Y3G9S73n75SGUFOQ0Xij4JMHe5k2ofTbHoliFrfYnk2oBKlJc6XlRlGn3x6SKve%2Bw2mnWFu84muFm10TXIVi%2F%2Fu2pxeOUBpz23IfEhmzS3r6Nx1olScWFhfXYduo3Pr5QNBfSiltbIm3eJ2xMLlus1C6AZDHLiQElKgRD5lvC94G9w0vE5WG3aPJnVJjHytmOR6gfsQs0KabyyoGb5SJPBSAmqUQW0Rw%2FKLDF%2B443bAq%2B1PIfhQFCLc%2BP44dUsuoUmUHCxRTQeQG0dxauo1rYRqOXWAk%2BVtpmOgLBuAjWJ5s8x0xt4QuVnfqDTZhPWfjjaVakJIDqEJ8ON4ziOoJQt%2FqfXuqEAJOZ%2BL%2F1ma5UWspFy%2Bs2ee1hHYUBNk1eQJ7%2FRotNEQ5EgfzgjfKz7MQUyUFac238cA%2BOzuX%2Fo1tI3w1nfePj0Z5b7vSnLQnvCbirkCIiQbJLZgUGYKRQ6DdZJmaRlGFwA1nP1Oh%2ByFLz%2F%2FsXO1WhrO2yZZ25RvgSjtYEGkTZeodXY%2FPuLbMPTVgb0GOqUBLS359yX1NVp%2FjaOO2N2uh4Zu3v59rNRspma9YfGAn6qlFG5Ttw5tuaEIukaEFf4Fq9CH9d9c0d0FUe757Bhy52bLCkoBqOQ2bhWYH%2BIkyDjhUsOgFDVhY0%2BbQFk6HatP07iMQU93heYVVrkCp9D8RgxbT6zxMUcJmwQsnFMX9VO5LmbpeUsj5iZGBKFPbptCO1MJAku9S9kfXhCLl3F%2FPNJDd9Sh&X-Amz-Signature=f451398137e7a09b72f60f25b1845382918e934dba0542a0d492f1a01b07b6cd&X-Amz-SignedHeaders=host&x-id=GetObject)
12. **Model Training**:
	- **Procedure**: Use cross-validation to select the optimal Alpha. Split the data into training and validation sets.
	- **Steps**:
		1. **Train Model**: Fit the model using different values of Alpha.
		2. **Predict & Evaluate**: Use validation data to make predictions and calculate the R^2 or other metrics.
		3. **Select Alpha**: Choose the Alpha that maximizes the R^2 on validation data.
13. **Implementation in Python**:
	- **Import**:
```python
from sklearn.linear_model import Ridge
```
	- **Create & Fit Model**:
```python
ridge = Ridge(alpha=1.0)  # Set the desired alpha value
ridge.fit(X_train, y_train)
```
	- **Predict**:
```python
y_pred = ridge.predict(X_test)
```
14. **Cross-Validation**:
	- **Purpose**: Used to determine the best Alpha by comparing performance metrics (e.g., R^2) across different Alpha values.
	- **Process**: Train with various Alpha values, evaluate with validation data, and select the best-performing Alpha.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYDTN6WI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBFaiPYRcwEOaRlOq1AQ1XwqOrinChD%2FN%2BJ1WstKahxAiA0At3jm96BfabcsqIGdu%2FCvKFK0dtmtwm%2BQ0%2B7VK7TeSr%2FAwgQEAAaDDYzNzQyMzE4MzgwNSIMt69UCd3OLqvCV0EpKtwDKYfGZ8LyHS6q1KzWSUYOk1OPlgriTl5%2FGI%2BB52VCcM9IqYFGjyvETCebozXQCXhkgcEkQggX7iopd%2FSwS5C3EDqc4K3XFRi5vOG4H4IwgWyi%2FB3I7pzlvEBYAtI5mMZKPMHz1l34MWCRnkAhCWijriPOwjlxt%2BiT3sDcV8WscMrxh%2FPzSApEQwfba6Dn4o%2FVwiMNfETv4M%2F2TYggaPGK%2BFv4zKbTL6%2BmNsKNq8x6jl0m%2BwWBROXD%2B56rmAvwRGTSYpG0YxtqTZH%2FaYLr0GQoiYekMF%2FvvwpYmXgJ0jW%2F7QHhhf4Jnk6kP4zV5%2BQGwSZ9jOr7ngWJWRrLFdXpbdJsXgX4EKeY2rJ8giCSTs%2Bidx52atU%2B22beC%2Fw4fB0wprfVIYIgolZmxXTGueeQ5cw4sewUaNm7lUUxgUHHWNmMy2AscvALD4YU80R32aQXsoI89MZ3eBn3KDBIViCBQx%2BoWa526%2BEK5ELMlvPwxHEp%2B21SAzI3bio4CgM%2FV%2B52DU908qjEGmc%2BHc%2FCcxWKoV9wZjEH6hUfUysUBkM%2BhobQEa%2FDY%2FujxIU1I8qBzjdu0U3kE6BjhARCFKwu2svwMwcK8sGyCH9uUgT3k8exoTfzwRCsI2TVG9GT7fkBx3IwqteBvQY6pgHDOtEB0OXocfCEK3LPRE%2FYop4EyjIUcf33di0hX2VB4vsBeo1fObsqloyetndeWyikgrEG5ncG1hX%2BabrIgdNK9qSBU0aXVjIdU1h4bk1tmYqdg6SFNIXcRcerEO49NqnwlIvTo8QM%2BQxR1ivuQFI%2BkQr9RnalfJDqnEpK%2FDs6MxfIGmOnEHx9rAg8d8f0Lqhdh3aX7MGkCU%2F2U%2Foz5VY8XOzziIUF&X-Amz-Signature=9216d47a1e7d1b32713643c255a81bf6c916bab03449ac14d1591aeb6acabc4d&X-Amz-SignedHeaders=host&x-id=GetObject)
15. **Example Visualization**:
	- **Plot**: Shows R^2 values vs. different Alpha values for training and validation data.
	- **Interpretation**:
		- **Training Data**: R^2 might increase with Alpha but eventually converge.
		- **Validation Data**: R^2 may decrease with high Alpha due to reduced model flexibility.
___
## Grid Search for Hyperparameter Tuning
### **Grid Search**
A method for finding the best hyperparameters for a model by systematically evaluating different combinations.
- **Hyperparameters**: Values like Alpha in Ridge Regression that are not learned from the data but set before the training process.
- **Process**:
	1. **Define Hyperparameters**: Set up a grid of hyperparameter values to test. For Ridge Regression, this might include values for Alpha and normalization options.
	2. **Train and Evaluate**: Train the model using each combination of hyperparameters. Evaluate each model using cross-validation, typically using metrics like R² or Mean Squared Error (MSE).
	3. **Select Best Parameters**: Choose the hyperparameters that give the best performance based on the evaluation metric.
### **Implementation in Scikit-learn**
```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 4, 9, 16, 25])

# Define parameter grid
param_grid = {
    'alpha': [0.1, 1, 10],
    'normalize': [True, False]
}

# Initialize Ridge model
ridge = Ridge()

# Initialize GridSearchCV
grid_search = GridSearchCV(estimator=ridge, param_grid=param_grid, scoring='r2', cv=5)

# Fit GridSearchCV
grid_search.fit(X, y)

# Get best parameters
best_params = grid_search.best_params_
best_score = grid_search.best_score_
best_estimator = grid_search.best_estimator_
cv_results = grid_search.cv_results_

# Results
print("Best Parameters:", best_params)
print("Best Score:", best_score)
print("Best Estimator:", best_estimator)
print("CV Results:", cv_results)
```
**Example Result:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW7RNK3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDg1ootHERDB3DLABC8jyE4UfUbAcEfcqlC058FaXN9zAiEA9XkyoJeRbGW1vN0TY0DJqNKHrGmZjlBNzdBPVqY6z88q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDIJjifdClLco7uxKECrcA9WsrLIHMuqJeSwYcsTiKFM9b20dASaexKQSCjL9JVAkhmXj%2BuO5ziwspQiKZ2AKMLa8eqrjF1ggLpr%2BXNJFb7%2BZiqXNnqKG%2FGgsR%2Fsrg1E8gvaNowQF8%2Fa4MfmFnmBn%2FXKzbm2k2wsXBDouXqRGSEYIkzl1kVRVY6inmafTkMRDjv%2FryLUP4VF%2BuDfQWUOqS2KviBOIqlaGrO3C%2FjivLypRzR9TRfQm%2BctUKOF1H%2BRLUeEolkctxGph36va%2Fauxw3nzEqqO2IXiTPYs3lwdGWxweDDyYfIRu1mSaQfAWej9gbyatB%2BDdrnPcVj4aJ8P0N9WlzRIPL5dDLliBkXZ7hpBT6r2lvJvzxPfEIOZ93bIhbq7g%2B%2BifTsvIcbSG5T5NYXoBmcrgMMHCE9Em0Aj39w1wLz1sjS2xufYiAG0JA39RtS%2B2TGapNWW2pzLfN%2Bgcy5VfeZg%2F7ZTD2xLgpGuq6IjhqbQ4f6xqBPT4UkshTIBB5S0AFeU6oL60IEtmGTvlbe75G7DHn%2BxDCVo0IfN4ObaSPgRr9sLi9cie10htLlS7ghHatdhuQGbuYn01LhTyJXNfa8lCyHp9Z1r%2FbCFNwZu%2BQvn96Xcd63WCyRceRo5%2FsepbXlU2VjALz9vML3Wgb0GOqUBFZKyi2hIR9M9Gr59O7KvygSVQd3%2Bdz6MYGh3wYKmnuXIPFlrh5S7ubPDGNW2RvZozZ7rLFDGr0NOk%2FTpoe4KoRK%2BRYlifx0SP39uOQqMCvmpdbPmAmsaYGX4EbE2IbUhb3e85W51fQvwmXa3%2BqF95pR9I%2BrCyFJ%2BCLwiHk%2FoGGp9SDALdBagqnWGbAJ37%2Bg7STilla98qxZnqZC2TiMaSeLNr%2FdV&X-Amz-Signature=7b2ee0939eacedb1a953b0f635420fd659a6d284e892011974c50935552c34a3&X-Amz-SignedHeaders=host&x-id=GetObject)
- **Key Attributes**:
	- `**best_estimator_**`: Best model found.
	- `**cv_results_**`: Detailed results for each hyperparameter combination, including scores and parameters.
- **Advantages**: Efficiently explores multiple hyperparameter values to find the best combination, reducing the manual effort required for model tuning.
___
## Cheat Sheet: Model Evaluation and Refinement
### Splitting Data for Training and Testing
The process involves separating the target attribute from the rest of the data, treating it as the output, and the rest as input. Then, split these into training and testing subsets.
```python
from sklearn.model_selection import train_test_split

# Define target and features
y_data = df['target_attribute']
x_data = df.drop('target_attribute', axis=1)

# Split into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.10, random_state=1)
```
### Cross Validation Score
Cross-validation involves creating multiple subsets of training and testing data to evaluate the model’s performance using the R² value.
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# Initialize the model
lre = LinearRegression()

# Perform cross-validation
Rcross = cross_val_score(lre, x_data[['attribute_1']], y_data, cv=n)

# Calculate mean and standard deviation of scores
Mean = Rcross.mean()
Std_dev = Rcross.std()
```
### Cross Validation Prediction
Generate predictions using a cross-validated model.
```python
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression

# Initialize the model
lre = LinearRegression()

# Perform cross-validation prediction
yhat = cross_val_predict(lre, x_data[['attribute_1']], y_data, cv=4)
```
### Ridge Regression and Prediction
Use Ridge regression to create a model that avoids overfitting by adjusting the alpha parameter and making predictions.
```python
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures

# Initialize polynomial features
pr = PolynomialFeatures(degree=2)

# Transform features
x_train_pr = pr.fit_transform(x_train[['attribute_1', 'attribute_2']])
x_test_pr = pr.transform(x_test[['attribute_1', 'attribute_2']])

# Initialize Ridge model
RigeModel = Ridge(alpha=1)

# Fit the model
RigeModel.fit(x_train_pr, y_train)

# Make predictions
yhat = RigeModel.predict(x_test_pr)
```
### Grid Search
Use Grid Search to find the optimal alpha value for Ridge regression by performing cross-validation.
```python
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge

# Define parameter grid
parameters = [{'alpha': [0.001, 0.1, 1, 10, 100, 1000, 10000]}]

# Initialize Ridge model
RR = Ridge()

# Initialize GridSearchCV
Grid1 = GridSearchCV(RR, parameters, cv=4)

# Fit GridSearchCV
Grid1.fit(x_data[['attribute_1', 'attribute_2']], y_data)

# Get the best model
BestRR = Grid1.best_estimator_

# Evaluate the model
score = BestRR.score(x_test[['attribute_1', 'attribute_2']], y_test)
```
___