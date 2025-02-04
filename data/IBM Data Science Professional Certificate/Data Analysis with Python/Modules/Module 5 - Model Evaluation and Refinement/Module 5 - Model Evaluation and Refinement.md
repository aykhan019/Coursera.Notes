

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIR2BYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDjSv6RwDzdUzOUCNmkJVrzuI2LQA1zpMX8R6pgqKk6cAiAPIEVd%2Fup9J31N5sY9780LqRVntKfN9LTFTJZF3Cnd3Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMXFxM2%2B8BsdQte7COKtwDXB2f0Rmo%2BkjtFbjXEFaOmNyyPb2Ej75%2BEXQ3qjHaCBbNjhu6NiLkJR36VJ45CRPnLUzOHGMm10HHerL89QW2ehXCpj107Cef1P3H7aYCZeAdwe2Kw5BNwA8Fm8orgzNCh2LbZsx0FlGnwXwgpx9x%2FFQU10pxfEoAfFALFtPhntj8Wus9BMEpRoVRtzSfImxOXzoLHCymnQ%2ByU%2FzwFH3WsiNGxvwMy%2B1VHLGCSJvY%2BHK7EzjuufYXzVuPZaP5ViHHUVEF9%2Be%2BGDjoBCVUOoHO1DPgF3b4jEVAb5qlHqMuonlgTwMtpR7Mo%2FKxP6HZzRURcWzAm3%2F6bp9Nt%2F1B5KpWUAzXZlP1XEGveUBZeObE%2BSYCU1DMGpKh95KwovRNfDbPydHhhdw2BRphTBkJ1ROXHiQD4gjFwh4kWNjVvsFAehQb5l540N8E4kMlWtMb2Qh6bBOyygU%2F68TX0oILIhExe3SkkOCVYtaIrbj9diN%2BtLBbLeJefy%2FS8T%2FEN527N72jOFH%2FMvaGT%2FMsy3DtV8xB%2FSDoGoDuh2%2F1fcb3GidXAipH9bOOFEhsVaxDQwGTN4uPSjEUUC4ArcC%2FeGSg%2FX5Y0n%2BonsHj9GLGpLDNxhKB8OtE8V%2BRssqH8MhuRm8wusqHvQY6pgE4CeS63yt46GdgCAFI3dQUxQ7x6aDJbQPqaZwQ2KEKiJnJT%2BLaViD05SqPMDkSvUBeg2FnEdoZ8CWCwGz4G94tblALYcRelhfNpQVFH697yusz0ykjaB4qL4Q4ws6tkYYUbAUwHv4XtembCGollGM6%2BOgvgjPf9H3qHjv56nJGQO2%2BdTOUbI73VF4kGq5nQHEAYRFrudhFOC4VJ2wFWbB50Rm2D8CZ&X-Amz-Signature=52400fc6a8285c1e9b5b88252f82dfd33861ba1f513b569f056c5ed454739bad&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIR2BYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDjSv6RwDzdUzOUCNmkJVrzuI2LQA1zpMX8R6pgqKk6cAiAPIEVd%2Fup9J31N5sY9780LqRVntKfN9LTFTJZF3Cnd3Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMXFxM2%2B8BsdQte7COKtwDXB2f0Rmo%2BkjtFbjXEFaOmNyyPb2Ej75%2BEXQ3qjHaCBbNjhu6NiLkJR36VJ45CRPnLUzOHGMm10HHerL89QW2ehXCpj107Cef1P3H7aYCZeAdwe2Kw5BNwA8Fm8orgzNCh2LbZsx0FlGnwXwgpx9x%2FFQU10pxfEoAfFALFtPhntj8Wus9BMEpRoVRtzSfImxOXzoLHCymnQ%2ByU%2FzwFH3WsiNGxvwMy%2B1VHLGCSJvY%2BHK7EzjuufYXzVuPZaP5ViHHUVEF9%2Be%2BGDjoBCVUOoHO1DPgF3b4jEVAb5qlHqMuonlgTwMtpR7Mo%2FKxP6HZzRURcWzAm3%2F6bp9Nt%2F1B5KpWUAzXZlP1XEGveUBZeObE%2BSYCU1DMGpKh95KwovRNfDbPydHhhdw2BRphTBkJ1ROXHiQD4gjFwh4kWNjVvsFAehQb5l540N8E4kMlWtMb2Qh6bBOyygU%2F68TX0oILIhExe3SkkOCVYtaIrbj9diN%2BtLBbLeJefy%2FS8T%2FEN527N72jOFH%2FMvaGT%2FMsy3DtV8xB%2FSDoGoDuh2%2F1fcb3GidXAipH9bOOFEhsVaxDQwGTN4uPSjEUUC4ArcC%2FeGSg%2FX5Y0n%2BonsHj9GLGpLDNxhKB8OtE8V%2BRssqH8MhuRm8wusqHvQY6pgE4CeS63yt46GdgCAFI3dQUxQ7x6aDJbQPqaZwQ2KEKiJnJT%2BLaViD05SqPMDkSvUBeg2FnEdoZ8CWCwGz4G94tblALYcRelhfNpQVFH697yusz0ykjaB4qL4Q4ws6tkYYUbAUwHv4XtembCGollGM6%2BOgvgjPf9H3qHjv56nJGQO2%2BdTOUbI73VF4kGq5nQHEAYRFrudhFOC4VJ2wFWbB50Rm2D8CZ&X-Amz-Signature=71a1286722b409a0f80d4f8d5b6f593698d5ae8b949c3bcb3d8867f584d18274&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIR2BYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDjSv6RwDzdUzOUCNmkJVrzuI2LQA1zpMX8R6pgqKk6cAiAPIEVd%2Fup9J31N5sY9780LqRVntKfN9LTFTJZF3Cnd3Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMXFxM2%2B8BsdQte7COKtwDXB2f0Rmo%2BkjtFbjXEFaOmNyyPb2Ej75%2BEXQ3qjHaCBbNjhu6NiLkJR36VJ45CRPnLUzOHGMm10HHerL89QW2ehXCpj107Cef1P3H7aYCZeAdwe2Kw5BNwA8Fm8orgzNCh2LbZsx0FlGnwXwgpx9x%2FFQU10pxfEoAfFALFtPhntj8Wus9BMEpRoVRtzSfImxOXzoLHCymnQ%2ByU%2FzwFH3WsiNGxvwMy%2B1VHLGCSJvY%2BHK7EzjuufYXzVuPZaP5ViHHUVEF9%2Be%2BGDjoBCVUOoHO1DPgF3b4jEVAb5qlHqMuonlgTwMtpR7Mo%2FKxP6HZzRURcWzAm3%2F6bp9Nt%2F1B5KpWUAzXZlP1XEGveUBZeObE%2BSYCU1DMGpKh95KwovRNfDbPydHhhdw2BRphTBkJ1ROXHiQD4gjFwh4kWNjVvsFAehQb5l540N8E4kMlWtMb2Qh6bBOyygU%2F68TX0oILIhExe3SkkOCVYtaIrbj9diN%2BtLBbLeJefy%2FS8T%2FEN527N72jOFH%2FMvaGT%2FMsy3DtV8xB%2FSDoGoDuh2%2F1fcb3GidXAipH9bOOFEhsVaxDQwGTN4uPSjEUUC4ArcC%2FeGSg%2FX5Y0n%2BonsHj9GLGpLDNxhKB8OtE8V%2BRssqH8MhuRm8wusqHvQY6pgE4CeS63yt46GdgCAFI3dQUxQ7x6aDJbQPqaZwQ2KEKiJnJT%2BLaViD05SqPMDkSvUBeg2FnEdoZ8CWCwGz4G94tblALYcRelhfNpQVFH697yusz0ykjaB4qL4Q4ws6tkYYUbAUwHv4XtembCGollGM6%2BOgvgjPf9H3qHjv56nJGQO2%2BdTOUbI73VF4kGq5nQHEAYRFrudhFOC4VJ2wFWbB50Rm2D8CZ&X-Amz-Signature=f3fab3dfcfe380ddd50df1857c3be27470bbb056d15e88870baec998b96337bc&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIR2BYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDjSv6RwDzdUzOUCNmkJVrzuI2LQA1zpMX8R6pgqKk6cAiAPIEVd%2Fup9J31N5sY9780LqRVntKfN9LTFTJZF3Cnd3Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMXFxM2%2B8BsdQte7COKtwDXB2f0Rmo%2BkjtFbjXEFaOmNyyPb2Ej75%2BEXQ3qjHaCBbNjhu6NiLkJR36VJ45CRPnLUzOHGMm10HHerL89QW2ehXCpj107Cef1P3H7aYCZeAdwe2Kw5BNwA8Fm8orgzNCh2LbZsx0FlGnwXwgpx9x%2FFQU10pxfEoAfFALFtPhntj8Wus9BMEpRoVRtzSfImxOXzoLHCymnQ%2ByU%2FzwFH3WsiNGxvwMy%2B1VHLGCSJvY%2BHK7EzjuufYXzVuPZaP5ViHHUVEF9%2Be%2BGDjoBCVUOoHO1DPgF3b4jEVAb5qlHqMuonlgTwMtpR7Mo%2FKxP6HZzRURcWzAm3%2F6bp9Nt%2F1B5KpWUAzXZlP1XEGveUBZeObE%2BSYCU1DMGpKh95KwovRNfDbPydHhhdw2BRphTBkJ1ROXHiQD4gjFwh4kWNjVvsFAehQb5l540N8E4kMlWtMb2Qh6bBOyygU%2F68TX0oILIhExe3SkkOCVYtaIrbj9diN%2BtLBbLeJefy%2FS8T%2FEN527N72jOFH%2FMvaGT%2FMsy3DtV8xB%2FSDoGoDuh2%2F1fcb3GidXAipH9bOOFEhsVaxDQwGTN4uPSjEUUC4ArcC%2FeGSg%2FX5Y0n%2BonsHj9GLGpLDNxhKB8OtE8V%2BRssqH8MhuRm8wusqHvQY6pgE4CeS63yt46GdgCAFI3dQUxQ7x6aDJbQPqaZwQ2KEKiJnJT%2BLaViD05SqPMDkSvUBeg2FnEdoZ8CWCwGz4G94tblALYcRelhfNpQVFH697yusz0ykjaB4qL4Q4ws6tkYYUbAUwHv4XtembCGollGM6%2BOgvgjPf9H3qHjv56nJGQO2%2BdTOUbI73VF4kGq5nQHEAYRFrudhFOC4VJ2wFWbB50Rm2D8CZ&X-Amz-Signature=e5dae6e8341c340d7539ea4b82427421d499221311b866f2416af10995af6598&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIR2BYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDjSv6RwDzdUzOUCNmkJVrzuI2LQA1zpMX8R6pgqKk6cAiAPIEVd%2Fup9J31N5sY9780LqRVntKfN9LTFTJZF3Cnd3Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMXFxM2%2B8BsdQte7COKtwDXB2f0Rmo%2BkjtFbjXEFaOmNyyPb2Ej75%2BEXQ3qjHaCBbNjhu6NiLkJR36VJ45CRPnLUzOHGMm10HHerL89QW2ehXCpj107Cef1P3H7aYCZeAdwe2Kw5BNwA8Fm8orgzNCh2LbZsx0FlGnwXwgpx9x%2FFQU10pxfEoAfFALFtPhntj8Wus9BMEpRoVRtzSfImxOXzoLHCymnQ%2ByU%2FzwFH3WsiNGxvwMy%2B1VHLGCSJvY%2BHK7EzjuufYXzVuPZaP5ViHHUVEF9%2Be%2BGDjoBCVUOoHO1DPgF3b4jEVAb5qlHqMuonlgTwMtpR7Mo%2FKxP6HZzRURcWzAm3%2F6bp9Nt%2F1B5KpWUAzXZlP1XEGveUBZeObE%2BSYCU1DMGpKh95KwovRNfDbPydHhhdw2BRphTBkJ1ROXHiQD4gjFwh4kWNjVvsFAehQb5l540N8E4kMlWtMb2Qh6bBOyygU%2F68TX0oILIhExe3SkkOCVYtaIrbj9diN%2BtLBbLeJefy%2FS8T%2FEN527N72jOFH%2FMvaGT%2FMsy3DtV8xB%2FSDoGoDuh2%2F1fcb3GidXAipH9bOOFEhsVaxDQwGTN4uPSjEUUC4ArcC%2FeGSg%2FX5Y0n%2BonsHj9GLGpLDNxhKB8OtE8V%2BRssqH8MhuRm8wusqHvQY6pgE4CeS63yt46GdgCAFI3dQUxQ7x6aDJbQPqaZwQ2KEKiJnJT%2BLaViD05SqPMDkSvUBeg2FnEdoZ8CWCwGz4G94tblALYcRelhfNpQVFH697yusz0ykjaB4qL4Q4ws6tkYYUbAUwHv4XtembCGollGM6%2BOgvgjPf9H3qHjv56nJGQO2%2BdTOUbI73VF4kGq5nQHEAYRFrudhFOC4VJ2wFWbB50Rm2D8CZ&X-Amz-Signature=52a55acbeb7f664ed7b6dbffca5c473068b2d7fb47cd3c9e7b849e7edc39e199&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIR2BYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDjSv6RwDzdUzOUCNmkJVrzuI2LQA1zpMX8R6pgqKk6cAiAPIEVd%2Fup9J31N5sY9780LqRVntKfN9LTFTJZF3Cnd3Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMXFxM2%2B8BsdQte7COKtwDXB2f0Rmo%2BkjtFbjXEFaOmNyyPb2Ej75%2BEXQ3qjHaCBbNjhu6NiLkJR36VJ45CRPnLUzOHGMm10HHerL89QW2ehXCpj107Cef1P3H7aYCZeAdwe2Kw5BNwA8Fm8orgzNCh2LbZsx0FlGnwXwgpx9x%2FFQU10pxfEoAfFALFtPhntj8Wus9BMEpRoVRtzSfImxOXzoLHCymnQ%2ByU%2FzwFH3WsiNGxvwMy%2B1VHLGCSJvY%2BHK7EzjuufYXzVuPZaP5ViHHUVEF9%2Be%2BGDjoBCVUOoHO1DPgF3b4jEVAb5qlHqMuonlgTwMtpR7Mo%2FKxP6HZzRURcWzAm3%2F6bp9Nt%2F1B5KpWUAzXZlP1XEGveUBZeObE%2BSYCU1DMGpKh95KwovRNfDbPydHhhdw2BRphTBkJ1ROXHiQD4gjFwh4kWNjVvsFAehQb5l540N8E4kMlWtMb2Qh6bBOyygU%2F68TX0oILIhExe3SkkOCVYtaIrbj9diN%2BtLBbLeJefy%2FS8T%2FEN527N72jOFH%2FMvaGT%2FMsy3DtV8xB%2FSDoGoDuh2%2F1fcb3GidXAipH9bOOFEhsVaxDQwGTN4uPSjEUUC4ArcC%2FeGSg%2FX5Y0n%2BonsHj9GLGpLDNxhKB8OtE8V%2BRssqH8MhuRm8wusqHvQY6pgE4CeS63yt46GdgCAFI3dQUxQ7x6aDJbQPqaZwQ2KEKiJnJT%2BLaViD05SqPMDkSvUBeg2FnEdoZ8CWCwGz4G94tblALYcRelhfNpQVFH697yusz0ykjaB4qL4Q4ws6tkYYUbAUwHv4XtembCGollGM6%2BOgvgjPf9H3qHjv56nJGQO2%2BdTOUbI73VF4kGq5nQHEAYRFrudhFOC4VJ2wFWbB50Rm2D8CZ&X-Amz-Signature=018d410018b9edee94ca5215a405e29b9d59da290d1d244c09efbfc2561fc4e2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIR2BYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDjSv6RwDzdUzOUCNmkJVrzuI2LQA1zpMX8R6pgqKk6cAiAPIEVd%2Fup9J31N5sY9780LqRVntKfN9LTFTJZF3Cnd3Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMXFxM2%2B8BsdQte7COKtwDXB2f0Rmo%2BkjtFbjXEFaOmNyyPb2Ej75%2BEXQ3qjHaCBbNjhu6NiLkJR36VJ45CRPnLUzOHGMm10HHerL89QW2ehXCpj107Cef1P3H7aYCZeAdwe2Kw5BNwA8Fm8orgzNCh2LbZsx0FlGnwXwgpx9x%2FFQU10pxfEoAfFALFtPhntj8Wus9BMEpRoVRtzSfImxOXzoLHCymnQ%2ByU%2FzwFH3WsiNGxvwMy%2B1VHLGCSJvY%2BHK7EzjuufYXzVuPZaP5ViHHUVEF9%2Be%2BGDjoBCVUOoHO1DPgF3b4jEVAb5qlHqMuonlgTwMtpR7Mo%2FKxP6HZzRURcWzAm3%2F6bp9Nt%2F1B5KpWUAzXZlP1XEGveUBZeObE%2BSYCU1DMGpKh95KwovRNfDbPydHhhdw2BRphTBkJ1ROXHiQD4gjFwh4kWNjVvsFAehQb5l540N8E4kMlWtMb2Qh6bBOyygU%2F68TX0oILIhExe3SkkOCVYtaIrbj9diN%2BtLBbLeJefy%2FS8T%2FEN527N72jOFH%2FMvaGT%2FMsy3DtV8xB%2FSDoGoDuh2%2F1fcb3GidXAipH9bOOFEhsVaxDQwGTN4uPSjEUUC4ArcC%2FeGSg%2FX5Y0n%2BonsHj9GLGpLDNxhKB8OtE8V%2BRssqH8MhuRm8wusqHvQY6pgE4CeS63yt46GdgCAFI3dQUxQ7x6aDJbQPqaZwQ2KEKiJnJT%2BLaViD05SqPMDkSvUBeg2FnEdoZ8CWCwGz4G94tblALYcRelhfNpQVFH697yusz0ykjaB4qL4Q4ws6tkYYUbAUwHv4XtembCGollGM6%2BOgvgjPf9H3qHjv56nJGQO2%2BdTOUbI73VF4kGq5nQHEAYRFrudhFOC4VJ2wFWbB50Rm2D8CZ&X-Amz-Signature=3414ef73ddcdfdd11768979860ecdc36b34e8ee9d33e8f29088f4d387052675f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIR2BYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDjSv6RwDzdUzOUCNmkJVrzuI2LQA1zpMX8R6pgqKk6cAiAPIEVd%2Fup9J31N5sY9780LqRVntKfN9LTFTJZF3Cnd3Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMXFxM2%2B8BsdQte7COKtwDXB2f0Rmo%2BkjtFbjXEFaOmNyyPb2Ej75%2BEXQ3qjHaCBbNjhu6NiLkJR36VJ45CRPnLUzOHGMm10HHerL89QW2ehXCpj107Cef1P3H7aYCZeAdwe2Kw5BNwA8Fm8orgzNCh2LbZsx0FlGnwXwgpx9x%2FFQU10pxfEoAfFALFtPhntj8Wus9BMEpRoVRtzSfImxOXzoLHCymnQ%2ByU%2FzwFH3WsiNGxvwMy%2B1VHLGCSJvY%2BHK7EzjuufYXzVuPZaP5ViHHUVEF9%2Be%2BGDjoBCVUOoHO1DPgF3b4jEVAb5qlHqMuonlgTwMtpR7Mo%2FKxP6HZzRURcWzAm3%2F6bp9Nt%2F1B5KpWUAzXZlP1XEGveUBZeObE%2BSYCU1DMGpKh95KwovRNfDbPydHhhdw2BRphTBkJ1ROXHiQD4gjFwh4kWNjVvsFAehQb5l540N8E4kMlWtMb2Qh6bBOyygU%2F68TX0oILIhExe3SkkOCVYtaIrbj9diN%2BtLBbLeJefy%2FS8T%2FEN527N72jOFH%2FMvaGT%2FMsy3DtV8xB%2FSDoGoDuh2%2F1fcb3GidXAipH9bOOFEhsVaxDQwGTN4uPSjEUUC4ArcC%2FeGSg%2FX5Y0n%2BonsHj9GLGpLDNxhKB8OtE8V%2BRssqH8MhuRm8wusqHvQY6pgE4CeS63yt46GdgCAFI3dQUxQ7x6aDJbQPqaZwQ2KEKiJnJT%2BLaViD05SqPMDkSvUBeg2FnEdoZ8CWCwGz4G94tblALYcRelhfNpQVFH697yusz0ykjaB4qL4Q4ws6tkYYUbAUwHv4XtembCGollGM6%2BOgvgjPf9H3qHjv56nJGQO2%2BdTOUbI73VF4kGq5nQHEAYRFrudhFOC4VJ2wFWbB50Rm2D8CZ&X-Amz-Signature=15d23e8361f09d29a0564a2958dd5ce6b7cae28d899e49287b3c79b47aaa9586&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIR2BYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDjSv6RwDzdUzOUCNmkJVrzuI2LQA1zpMX8R6pgqKk6cAiAPIEVd%2Fup9J31N5sY9780LqRVntKfN9LTFTJZF3Cnd3Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMXFxM2%2B8BsdQte7COKtwDXB2f0Rmo%2BkjtFbjXEFaOmNyyPb2Ej75%2BEXQ3qjHaCBbNjhu6NiLkJR36VJ45CRPnLUzOHGMm10HHerL89QW2ehXCpj107Cef1P3H7aYCZeAdwe2Kw5BNwA8Fm8orgzNCh2LbZsx0FlGnwXwgpx9x%2FFQU10pxfEoAfFALFtPhntj8Wus9BMEpRoVRtzSfImxOXzoLHCymnQ%2ByU%2FzwFH3WsiNGxvwMy%2B1VHLGCSJvY%2BHK7EzjuufYXzVuPZaP5ViHHUVEF9%2Be%2BGDjoBCVUOoHO1DPgF3b4jEVAb5qlHqMuonlgTwMtpR7Mo%2FKxP6HZzRURcWzAm3%2F6bp9Nt%2F1B5KpWUAzXZlP1XEGveUBZeObE%2BSYCU1DMGpKh95KwovRNfDbPydHhhdw2BRphTBkJ1ROXHiQD4gjFwh4kWNjVvsFAehQb5l540N8E4kMlWtMb2Qh6bBOyygU%2F68TX0oILIhExe3SkkOCVYtaIrbj9diN%2BtLBbLeJefy%2FS8T%2FEN527N72jOFH%2FMvaGT%2FMsy3DtV8xB%2FSDoGoDuh2%2F1fcb3GidXAipH9bOOFEhsVaxDQwGTN4uPSjEUUC4ArcC%2FeGSg%2FX5Y0n%2BonsHj9GLGpLDNxhKB8OtE8V%2BRssqH8MhuRm8wusqHvQY6pgE4CeS63yt46GdgCAFI3dQUxQ7x6aDJbQPqaZwQ2KEKiJnJT%2BLaViD05SqPMDkSvUBeg2FnEdoZ8CWCwGz4G94tblALYcRelhfNpQVFH697yusz0ykjaB4qL4Q4ws6tkYYUbAUwHv4XtembCGollGM6%2BOgvgjPf9H3qHjv56nJGQO2%2BdTOUbI73VF4kGq5nQHEAYRFrudhFOC4VJ2wFWbB50Rm2D8CZ&X-Amz-Signature=5ae51016ebf5c72f41bf1b5fdc509f8bf7cad33ed6620ce235982f361cd9e28b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UICJQSGZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDMtk478qyxp9DzvdQNarau0S5OejRr21YxR8Zwy8nexwIhALSPcWSy5zTdpW%2FU%2FtdvoDVzObKau09f5u5VWCOjnHtWKv8DCCsQABoMNjM3NDIzMTgzODA1IgzZK50bXQ5%2BvC1dVbsq3ANtFtMvEMilkljMghKKZzX1ukWZ8J%2BqWJpV8JLrnu7HuT4NZhcGSIEGSnpTC%2FQ65%2FI%2F6VUsrz7SxK1IF1zb1PBIKuUFT2kIH1zpp1idgxodqwS1gjpFRbJdtWJhO3hEm0tSRucI50PUp9DBoIfLItiOtDurQn2fIi58r3KpXX%2B1e5w1M%2B4vOyV2wntVe%2FiQxog4PbNG%2FYeSYJTBxhcJATlvFDjm06hPkteBKoXJ8S9FFLTe2IZy0UCF1mtY2PsB0lOMu%2BaRocnHb%2FW8GZnO32F8K%2Bw%2FawE4XVCJzwXQMVtAjyvlx4Ey2eH4kCwU%2BNRJwL%2BzajBXSBgmjE9LdK2s2KrTs%2BH2sw97cP084YnrSqpXMRlxTNeYeDgSIZdp2xTT0VOW%2BOxb4anPnIZq%2FoihLycAHFOSG3f5iFmpntknZ5Zfl%2F4kWAJgikGhURQaN9wjOWw7VTN0rD2hX7eMsSn7xB%2BhworNHdfc2xm6EXt4kghCYr4PqvA3YAVewtNng3JootFyX2d99WLkKNQJoWlqYh%2FmjDGHjRhTkatvTyefS8kqUcMVQ77R%2Bgy3I3tsLMDkk6VlkG%2BB4AvAlQRjczMoBs3xuxwVlAXlb0reENgX0yo%2FIFKjQWS%2FkeruI0iowTCQyoe9BjqkAXG5%2BfRyKJOdIPNSKqyZgh1wszMhP3IZq1JwuGeIXC1qc9ECBctnSwH5eX81cz8rTosvXW3VD1mqxRvfuausKkQZjAXopMmyfuveshB3BKEyHed23HOuMKoXk9u%2FKt1hpyPHvkHpPIzhuFgjIpsqReUJ8k9padn%2FcQ1JXD5a%2Bf2Q2O0y0y0I67PMfvN6Jd7eEH9DV1AsCjM9de4n7hTh3sxGbhyC&X-Amz-Signature=45923896c4f7f782ded3381d90adb7db6da1e3ddfa859ee7d82de3cfec0b7cb6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UICJQSGZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDMtk478qyxp9DzvdQNarau0S5OejRr21YxR8Zwy8nexwIhALSPcWSy5zTdpW%2FU%2FtdvoDVzObKau09f5u5VWCOjnHtWKv8DCCsQABoMNjM3NDIzMTgzODA1IgzZK50bXQ5%2BvC1dVbsq3ANtFtMvEMilkljMghKKZzX1ukWZ8J%2BqWJpV8JLrnu7HuT4NZhcGSIEGSnpTC%2FQ65%2FI%2F6VUsrz7SxK1IF1zb1PBIKuUFT2kIH1zpp1idgxodqwS1gjpFRbJdtWJhO3hEm0tSRucI50PUp9DBoIfLItiOtDurQn2fIi58r3KpXX%2B1e5w1M%2B4vOyV2wntVe%2FiQxog4PbNG%2FYeSYJTBxhcJATlvFDjm06hPkteBKoXJ8S9FFLTe2IZy0UCF1mtY2PsB0lOMu%2BaRocnHb%2FW8GZnO32F8K%2Bw%2FawE4XVCJzwXQMVtAjyvlx4Ey2eH4kCwU%2BNRJwL%2BzajBXSBgmjE9LdK2s2KrTs%2BH2sw97cP084YnrSqpXMRlxTNeYeDgSIZdp2xTT0VOW%2BOxb4anPnIZq%2FoihLycAHFOSG3f5iFmpntknZ5Zfl%2F4kWAJgikGhURQaN9wjOWw7VTN0rD2hX7eMsSn7xB%2BhworNHdfc2xm6EXt4kghCYr4PqvA3YAVewtNng3JootFyX2d99WLkKNQJoWlqYh%2FmjDGHjRhTkatvTyefS8kqUcMVQ77R%2Bgy3I3tsLMDkk6VlkG%2BB4AvAlQRjczMoBs3xuxwVlAXlb0reENgX0yo%2FIFKjQWS%2FkeruI0iowTCQyoe9BjqkAXG5%2BfRyKJOdIPNSKqyZgh1wszMhP3IZq1JwuGeIXC1qc9ECBctnSwH5eX81cz8rTosvXW3VD1mqxRvfuausKkQZjAXopMmyfuveshB3BKEyHed23HOuMKoXk9u%2FKt1hpyPHvkHpPIzhuFgjIpsqReUJ8k9padn%2FcQ1JXD5a%2Bf2Q2O0y0y0I67PMfvN6Jd7eEH9DV1AsCjM9de4n7hTh3sxGbhyC&X-Amz-Signature=73f81eeeca5556d277acbe6754fc597b24a2d0795a73b9b18e3f483635d00c4c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UICJQSGZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDMtk478qyxp9DzvdQNarau0S5OejRr21YxR8Zwy8nexwIhALSPcWSy5zTdpW%2FU%2FtdvoDVzObKau09f5u5VWCOjnHtWKv8DCCsQABoMNjM3NDIzMTgzODA1IgzZK50bXQ5%2BvC1dVbsq3ANtFtMvEMilkljMghKKZzX1ukWZ8J%2BqWJpV8JLrnu7HuT4NZhcGSIEGSnpTC%2FQ65%2FI%2F6VUsrz7SxK1IF1zb1PBIKuUFT2kIH1zpp1idgxodqwS1gjpFRbJdtWJhO3hEm0tSRucI50PUp9DBoIfLItiOtDurQn2fIi58r3KpXX%2B1e5w1M%2B4vOyV2wntVe%2FiQxog4PbNG%2FYeSYJTBxhcJATlvFDjm06hPkteBKoXJ8S9FFLTe2IZy0UCF1mtY2PsB0lOMu%2BaRocnHb%2FW8GZnO32F8K%2Bw%2FawE4XVCJzwXQMVtAjyvlx4Ey2eH4kCwU%2BNRJwL%2BzajBXSBgmjE9LdK2s2KrTs%2BH2sw97cP084YnrSqpXMRlxTNeYeDgSIZdp2xTT0VOW%2BOxb4anPnIZq%2FoihLycAHFOSG3f5iFmpntknZ5Zfl%2F4kWAJgikGhURQaN9wjOWw7VTN0rD2hX7eMsSn7xB%2BhworNHdfc2xm6EXt4kghCYr4PqvA3YAVewtNng3JootFyX2d99WLkKNQJoWlqYh%2FmjDGHjRhTkatvTyefS8kqUcMVQ77R%2Bgy3I3tsLMDkk6VlkG%2BB4AvAlQRjczMoBs3xuxwVlAXlb0reENgX0yo%2FIFKjQWS%2FkeruI0iowTCQyoe9BjqkAXG5%2BfRyKJOdIPNSKqyZgh1wszMhP3IZq1JwuGeIXC1qc9ECBctnSwH5eX81cz8rTosvXW3VD1mqxRvfuausKkQZjAXopMmyfuveshB3BKEyHed23HOuMKoXk9u%2FKt1hpyPHvkHpPIzhuFgjIpsqReUJ8k9padn%2FcQ1JXD5a%2Bf2Q2O0y0y0I67PMfvN6Jd7eEH9DV1AsCjM9de4n7hTh3sxGbhyC&X-Amz-Signature=5646c27dfddb78ecbf626ec115be8420d91d5943c7f78560262729f8f7497cd6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIR2BYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDjSv6RwDzdUzOUCNmkJVrzuI2LQA1zpMX8R6pgqKk6cAiAPIEVd%2Fup9J31N5sY9780LqRVntKfN9LTFTJZF3Cnd3Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMXFxM2%2B8BsdQte7COKtwDXB2f0Rmo%2BkjtFbjXEFaOmNyyPb2Ej75%2BEXQ3qjHaCBbNjhu6NiLkJR36VJ45CRPnLUzOHGMm10HHerL89QW2ehXCpj107Cef1P3H7aYCZeAdwe2Kw5BNwA8Fm8orgzNCh2LbZsx0FlGnwXwgpx9x%2FFQU10pxfEoAfFALFtPhntj8Wus9BMEpRoVRtzSfImxOXzoLHCymnQ%2ByU%2FzwFH3WsiNGxvwMy%2B1VHLGCSJvY%2BHK7EzjuufYXzVuPZaP5ViHHUVEF9%2Be%2BGDjoBCVUOoHO1DPgF3b4jEVAb5qlHqMuonlgTwMtpR7Mo%2FKxP6HZzRURcWzAm3%2F6bp9Nt%2F1B5KpWUAzXZlP1XEGveUBZeObE%2BSYCU1DMGpKh95KwovRNfDbPydHhhdw2BRphTBkJ1ROXHiQD4gjFwh4kWNjVvsFAehQb5l540N8E4kMlWtMb2Qh6bBOyygU%2F68TX0oILIhExe3SkkOCVYtaIrbj9diN%2BtLBbLeJefy%2FS8T%2FEN527N72jOFH%2FMvaGT%2FMsy3DtV8xB%2FSDoGoDuh2%2F1fcb3GidXAipH9bOOFEhsVaxDQwGTN4uPSjEUUC4ArcC%2FeGSg%2FX5Y0n%2BonsHj9GLGpLDNxhKB8OtE8V%2BRssqH8MhuRm8wusqHvQY6pgE4CeS63yt46GdgCAFI3dQUxQ7x6aDJbQPqaZwQ2KEKiJnJT%2BLaViD05SqPMDkSvUBeg2FnEdoZ8CWCwGz4G94tblALYcRelhfNpQVFH697yusz0ykjaB4qL4Q4ws6tkYYUbAUwHv4XtembCGollGM6%2BOgvgjPf9H3qHjv56nJGQO2%2BdTOUbI73VF4kGq5nQHEAYRFrudhFOC4VJ2wFWbB50Rm2D8CZ&X-Amz-Signature=67b51f9870ff1cb323835199bd7ef8fa9c3c3bbaedd93a5dba9518bbb218a034&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIR2BYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDjSv6RwDzdUzOUCNmkJVrzuI2LQA1zpMX8R6pgqKk6cAiAPIEVd%2Fup9J31N5sY9780LqRVntKfN9LTFTJZF3Cnd3Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMXFxM2%2B8BsdQte7COKtwDXB2f0Rmo%2BkjtFbjXEFaOmNyyPb2Ej75%2BEXQ3qjHaCBbNjhu6NiLkJR36VJ45CRPnLUzOHGMm10HHerL89QW2ehXCpj107Cef1P3H7aYCZeAdwe2Kw5BNwA8Fm8orgzNCh2LbZsx0FlGnwXwgpx9x%2FFQU10pxfEoAfFALFtPhntj8Wus9BMEpRoVRtzSfImxOXzoLHCymnQ%2ByU%2FzwFH3WsiNGxvwMy%2B1VHLGCSJvY%2BHK7EzjuufYXzVuPZaP5ViHHUVEF9%2Be%2BGDjoBCVUOoHO1DPgF3b4jEVAb5qlHqMuonlgTwMtpR7Mo%2FKxP6HZzRURcWzAm3%2F6bp9Nt%2F1B5KpWUAzXZlP1XEGveUBZeObE%2BSYCU1DMGpKh95KwovRNfDbPydHhhdw2BRphTBkJ1ROXHiQD4gjFwh4kWNjVvsFAehQb5l540N8E4kMlWtMb2Qh6bBOyygU%2F68TX0oILIhExe3SkkOCVYtaIrbj9diN%2BtLBbLeJefy%2FS8T%2FEN527N72jOFH%2FMvaGT%2FMsy3DtV8xB%2FSDoGoDuh2%2F1fcb3GidXAipH9bOOFEhsVaxDQwGTN4uPSjEUUC4ArcC%2FeGSg%2FX5Y0n%2BonsHj9GLGpLDNxhKB8OtE8V%2BRssqH8MhuRm8wusqHvQY6pgE4CeS63yt46GdgCAFI3dQUxQ7x6aDJbQPqaZwQ2KEKiJnJT%2BLaViD05SqPMDkSvUBeg2FnEdoZ8CWCwGz4G94tblALYcRelhfNpQVFH697yusz0ykjaB4qL4Q4ws6tkYYUbAUwHv4XtembCGollGM6%2BOgvgjPf9H3qHjv56nJGQO2%2BdTOUbI73VF4kGq5nQHEAYRFrudhFOC4VJ2wFWbB50Rm2D8CZ&X-Amz-Signature=b4ba8470bb23c81f9dd7fc82530b4b08dbc4dcc87f9614f53d62d5944aef35a6&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIR2BYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDjSv6RwDzdUzOUCNmkJVrzuI2LQA1zpMX8R6pgqKk6cAiAPIEVd%2Fup9J31N5sY9780LqRVntKfN9LTFTJZF3Cnd3Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMXFxM2%2B8BsdQte7COKtwDXB2f0Rmo%2BkjtFbjXEFaOmNyyPb2Ej75%2BEXQ3qjHaCBbNjhu6NiLkJR36VJ45CRPnLUzOHGMm10HHerL89QW2ehXCpj107Cef1P3H7aYCZeAdwe2Kw5BNwA8Fm8orgzNCh2LbZsx0FlGnwXwgpx9x%2FFQU10pxfEoAfFALFtPhntj8Wus9BMEpRoVRtzSfImxOXzoLHCymnQ%2ByU%2FzwFH3WsiNGxvwMy%2B1VHLGCSJvY%2BHK7EzjuufYXzVuPZaP5ViHHUVEF9%2Be%2BGDjoBCVUOoHO1DPgF3b4jEVAb5qlHqMuonlgTwMtpR7Mo%2FKxP6HZzRURcWzAm3%2F6bp9Nt%2F1B5KpWUAzXZlP1XEGveUBZeObE%2BSYCU1DMGpKh95KwovRNfDbPydHhhdw2BRphTBkJ1ROXHiQD4gjFwh4kWNjVvsFAehQb5l540N8E4kMlWtMb2Qh6bBOyygU%2F68TX0oILIhExe3SkkOCVYtaIrbj9diN%2BtLBbLeJefy%2FS8T%2FEN527N72jOFH%2FMvaGT%2FMsy3DtV8xB%2FSDoGoDuh2%2F1fcb3GidXAipH9bOOFEhsVaxDQwGTN4uPSjEUUC4ArcC%2FeGSg%2FX5Y0n%2BonsHj9GLGpLDNxhKB8OtE8V%2BRssqH8MhuRm8wusqHvQY6pgE4CeS63yt46GdgCAFI3dQUxQ7x6aDJbQPqaZwQ2KEKiJnJT%2BLaViD05SqPMDkSvUBeg2FnEdoZ8CWCwGz4G94tblALYcRelhfNpQVFH697yusz0ykjaB4qL4Q4ws6tkYYUbAUwHv4XtembCGollGM6%2BOgvgjPf9H3qHjv56nJGQO2%2BdTOUbI73VF4kGq5nQHEAYRFrudhFOC4VJ2wFWbB50Rm2D8CZ&X-Amz-Signature=155eb680be4db113691bca01040b9e43be65b205a6469610926ed41f5c647a7c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIR2BYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDjSv6RwDzdUzOUCNmkJVrzuI2LQA1zpMX8R6pgqKk6cAiAPIEVd%2Fup9J31N5sY9780LqRVntKfN9LTFTJZF3Cnd3Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMXFxM2%2B8BsdQte7COKtwDXB2f0Rmo%2BkjtFbjXEFaOmNyyPb2Ej75%2BEXQ3qjHaCBbNjhu6NiLkJR36VJ45CRPnLUzOHGMm10HHerL89QW2ehXCpj107Cef1P3H7aYCZeAdwe2Kw5BNwA8Fm8orgzNCh2LbZsx0FlGnwXwgpx9x%2FFQU10pxfEoAfFALFtPhntj8Wus9BMEpRoVRtzSfImxOXzoLHCymnQ%2ByU%2FzwFH3WsiNGxvwMy%2B1VHLGCSJvY%2BHK7EzjuufYXzVuPZaP5ViHHUVEF9%2Be%2BGDjoBCVUOoHO1DPgF3b4jEVAb5qlHqMuonlgTwMtpR7Mo%2FKxP6HZzRURcWzAm3%2F6bp9Nt%2F1B5KpWUAzXZlP1XEGveUBZeObE%2BSYCU1DMGpKh95KwovRNfDbPydHhhdw2BRphTBkJ1ROXHiQD4gjFwh4kWNjVvsFAehQb5l540N8E4kMlWtMb2Qh6bBOyygU%2F68TX0oILIhExe3SkkOCVYtaIrbj9diN%2BtLBbLeJefy%2FS8T%2FEN527N72jOFH%2FMvaGT%2FMsy3DtV8xB%2FSDoGoDuh2%2F1fcb3GidXAipH9bOOFEhsVaxDQwGTN4uPSjEUUC4ArcC%2FeGSg%2FX5Y0n%2BonsHj9GLGpLDNxhKB8OtE8V%2BRssqH8MhuRm8wusqHvQY6pgE4CeS63yt46GdgCAFI3dQUxQ7x6aDJbQPqaZwQ2KEKiJnJT%2BLaViD05SqPMDkSvUBeg2FnEdoZ8CWCwGz4G94tblALYcRelhfNpQVFH697yusz0ykjaB4qL4Q4ws6tkYYUbAUwHv4XtembCGollGM6%2BOgvgjPf9H3qHjv56nJGQO2%2BdTOUbI73VF4kGq5nQHEAYRFrudhFOC4VJ2wFWbB50Rm2D8CZ&X-Amz-Signature=2f196feddd57f72483e3010582814fe7cd74d51ddceda9e5d604bca8b0782684&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIR2BYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDjSv6RwDzdUzOUCNmkJVrzuI2LQA1zpMX8R6pgqKk6cAiAPIEVd%2Fup9J31N5sY9780LqRVntKfN9LTFTJZF3Cnd3Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMXFxM2%2B8BsdQte7COKtwDXB2f0Rmo%2BkjtFbjXEFaOmNyyPb2Ej75%2BEXQ3qjHaCBbNjhu6NiLkJR36VJ45CRPnLUzOHGMm10HHerL89QW2ehXCpj107Cef1P3H7aYCZeAdwe2Kw5BNwA8Fm8orgzNCh2LbZsx0FlGnwXwgpx9x%2FFQU10pxfEoAfFALFtPhntj8Wus9BMEpRoVRtzSfImxOXzoLHCymnQ%2ByU%2FzwFH3WsiNGxvwMy%2B1VHLGCSJvY%2BHK7EzjuufYXzVuPZaP5ViHHUVEF9%2Be%2BGDjoBCVUOoHO1DPgF3b4jEVAb5qlHqMuonlgTwMtpR7Mo%2FKxP6HZzRURcWzAm3%2F6bp9Nt%2F1B5KpWUAzXZlP1XEGveUBZeObE%2BSYCU1DMGpKh95KwovRNfDbPydHhhdw2BRphTBkJ1ROXHiQD4gjFwh4kWNjVvsFAehQb5l540N8E4kMlWtMb2Qh6bBOyygU%2F68TX0oILIhExe3SkkOCVYtaIrbj9diN%2BtLBbLeJefy%2FS8T%2FEN527N72jOFH%2FMvaGT%2FMsy3DtV8xB%2FSDoGoDuh2%2F1fcb3GidXAipH9bOOFEhsVaxDQwGTN4uPSjEUUC4ArcC%2FeGSg%2FX5Y0n%2BonsHj9GLGpLDNxhKB8OtE8V%2BRssqH8MhuRm8wusqHvQY6pgE4CeS63yt46GdgCAFI3dQUxQ7x6aDJbQPqaZwQ2KEKiJnJT%2BLaViD05SqPMDkSvUBeg2FnEdoZ8CWCwGz4G94tblALYcRelhfNpQVFH697yusz0ykjaB4qL4Q4ws6tkYYUbAUwHv4XtembCGollGM6%2BOgvgjPf9H3qHjv56nJGQO2%2BdTOUbI73VF4kGq5nQHEAYRFrudhFOC4VJ2wFWbB50Rm2D8CZ&X-Amz-Signature=561ddd116073745f2a7df6ada86148c0cd7ddcfcdc90e82db565c2a99820d1d5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UICJQSGZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDMtk478qyxp9DzvdQNarau0S5OejRr21YxR8Zwy8nexwIhALSPcWSy5zTdpW%2FU%2FtdvoDVzObKau09f5u5VWCOjnHtWKv8DCCsQABoMNjM3NDIzMTgzODA1IgzZK50bXQ5%2BvC1dVbsq3ANtFtMvEMilkljMghKKZzX1ukWZ8J%2BqWJpV8JLrnu7HuT4NZhcGSIEGSnpTC%2FQ65%2FI%2F6VUsrz7SxK1IF1zb1PBIKuUFT2kIH1zpp1idgxodqwS1gjpFRbJdtWJhO3hEm0tSRucI50PUp9DBoIfLItiOtDurQn2fIi58r3KpXX%2B1e5w1M%2B4vOyV2wntVe%2FiQxog4PbNG%2FYeSYJTBxhcJATlvFDjm06hPkteBKoXJ8S9FFLTe2IZy0UCF1mtY2PsB0lOMu%2BaRocnHb%2FW8GZnO32F8K%2Bw%2FawE4XVCJzwXQMVtAjyvlx4Ey2eH4kCwU%2BNRJwL%2BzajBXSBgmjE9LdK2s2KrTs%2BH2sw97cP084YnrSqpXMRlxTNeYeDgSIZdp2xTT0VOW%2BOxb4anPnIZq%2FoihLycAHFOSG3f5iFmpntknZ5Zfl%2F4kWAJgikGhURQaN9wjOWw7VTN0rD2hX7eMsSn7xB%2BhworNHdfc2xm6EXt4kghCYr4PqvA3YAVewtNng3JootFyX2d99WLkKNQJoWlqYh%2FmjDGHjRhTkatvTyefS8kqUcMVQ77R%2Bgy3I3tsLMDkk6VlkG%2BB4AvAlQRjczMoBs3xuxwVlAXlb0reENgX0yo%2FIFKjQWS%2FkeruI0iowTCQyoe9BjqkAXG5%2BfRyKJOdIPNSKqyZgh1wszMhP3IZq1JwuGeIXC1qc9ECBctnSwH5eX81cz8rTosvXW3VD1mqxRvfuausKkQZjAXopMmyfuveshB3BKEyHed23HOuMKoXk9u%2FKt1hpyPHvkHpPIzhuFgjIpsqReUJ8k9padn%2FcQ1JXD5a%2Bf2Q2O0y0y0I67PMfvN6Jd7eEH9DV1AsCjM9de4n7hTh3sxGbhyC&X-Amz-Signature=8822c6447dcc984203ec691136836fe4ab0c16fc1107f565cc83fcd37f18979e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XC2SBRTG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIAf4CuVkLYB4ADAkFtj%2FhCHeLPwfdcC%2BS8q5WszfRzj2AiBSjZLlGGq9RllMVNC366Kq7LT0Q6diztBQg9TNw0R02Sr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMq4GKHdq%2BzBzWitc4KtwDlneX0zpojYqBKBNwKfT2KlTw3VqSV8WWSfBN8rhPKjWkrAddyWqpKMoYhoixEqTkT%2B1GmfKI%2F9nCL666sV5bCsuLkuFx6NEDgZgYQuFL0uDmLEHX3OKY%2BrZ%2FV1Dtxuy5mP0pU6BrbmD61sUIHOc8U%2BexKFtY92nr6Bt%2FAVxPlz5hJO5sax0MrcbDLB4w175Jnoz0uHZ9XZqa%2BPsa1SBK4ivs%2FOVK2jJRt7k%2BsupfArMPVaCDiAzoWSj18VqgZv%2BUG12X6Ai44AqS34EAwHdJwCP29NloKTpXnJR0MaC%2FAUi%2BHRN5x8Gfcd7yfKNz5pc5s5BqvOd2uWm7pGi1CTnxG1bx85i6Vh%2Fud4kFLp%2FefbbH7jQPmvipr0Nv2d0gPFqGN%2FSpMyE8i6Ox3S5XcX4MzdcxTzd3um%2Fu1j4%2Bc10lOCw%2BaQCXfkKVxcJaxIkLJCjJuIIplCmm%2FdG886pwSgfbVvo4GL3pzdWvrdkdnYNpOmLAmf4r339kETyiK9%2BRTrUaYy%2FJ38Ri%2FesWKBPrH9a5fDmsTKmCz%2B4fIsg7%2BVCm7txGtvj75g%2FMYtgqM2sF0EE%2FpZu9HWqZGeXp%2F3vW3jrOy3a%2Fe%2BhsiUijTokjN4MQVDz%2FwDA5qPN8eC%2B3Q%2FMwjcuHvQY6pgGwXz%2Bvxcydn0bNJ4otoxgsXJZS3l9DyNZjiU9u6WQddTzoNIkQNV9VTNRiPHyYRbkW3dqeVxufzOw%2BIO8meRjbmm%2BbXhWWzYfbSn%2FQjCVdvuGYyQ3BaXsU7usASD6i%2BI31RVP%2Fp1Aru%2B1EDFUX7m%2BJIcbBJANOoPC%2Bl9c8%2F4BU3g8pSD6qpj98s%2FfGs6C5%2Fsb7pZKqLeXJHbOa9rrSzijYEefONYiT&X-Amz-Signature=1fb3f7da7f838d7eb67a235fb47c8e1254d61a631b20569a34f9265de7446cd8&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XC2SBRTG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIAf4CuVkLYB4ADAkFtj%2FhCHeLPwfdcC%2BS8q5WszfRzj2AiBSjZLlGGq9RllMVNC366Kq7LT0Q6diztBQg9TNw0R02Sr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMq4GKHdq%2BzBzWitc4KtwDlneX0zpojYqBKBNwKfT2KlTw3VqSV8WWSfBN8rhPKjWkrAddyWqpKMoYhoixEqTkT%2B1GmfKI%2F9nCL666sV5bCsuLkuFx6NEDgZgYQuFL0uDmLEHX3OKY%2BrZ%2FV1Dtxuy5mP0pU6BrbmD61sUIHOc8U%2BexKFtY92nr6Bt%2FAVxPlz5hJO5sax0MrcbDLB4w175Jnoz0uHZ9XZqa%2BPsa1SBK4ivs%2FOVK2jJRt7k%2BsupfArMPVaCDiAzoWSj18VqgZv%2BUG12X6Ai44AqS34EAwHdJwCP29NloKTpXnJR0MaC%2FAUi%2BHRN5x8Gfcd7yfKNz5pc5s5BqvOd2uWm7pGi1CTnxG1bx85i6Vh%2Fud4kFLp%2FefbbH7jQPmvipr0Nv2d0gPFqGN%2FSpMyE8i6Ox3S5XcX4MzdcxTzd3um%2Fu1j4%2Bc10lOCw%2BaQCXfkKVxcJaxIkLJCjJuIIplCmm%2FdG886pwSgfbVvo4GL3pzdWvrdkdnYNpOmLAmf4r339kETyiK9%2BRTrUaYy%2FJ38Ri%2FesWKBPrH9a5fDmsTKmCz%2B4fIsg7%2BVCm7txGtvj75g%2FMYtgqM2sF0EE%2FpZu9HWqZGeXp%2F3vW3jrOy3a%2Fe%2BhsiUijTokjN4MQVDz%2FwDA5qPN8eC%2B3Q%2FMwjcuHvQY6pgGwXz%2Bvxcydn0bNJ4otoxgsXJZS3l9DyNZjiU9u6WQddTzoNIkQNV9VTNRiPHyYRbkW3dqeVxufzOw%2BIO8meRjbmm%2BbXhWWzYfbSn%2FQjCVdvuGYyQ3BaXsU7usASD6i%2BI31RVP%2Fp1Aru%2B1EDFUX7m%2BJIcbBJANOoPC%2Bl9c8%2F4BU3g8pSD6qpj98s%2FfGs6C5%2Fsb7pZKqLeXJHbOa9rrSzijYEefONYiT&X-Amz-Signature=78c79ef7904c1bb78439181dfa318eff88a8b42501c7b8c9e36f6a6388f04bd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BEC2NXR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDdaSLjBkwm38232I34T%2Fepym3NhU0IG6zVGbI5%2FkKI7gIhAKe8esYkeTXaO16eBFb4jkpCAUvfWUtTInycZ49nrs5jKv8DCCsQABoMNjM3NDIzMTgzODA1IgwdCa41dqbPQE36amkq3AOQZGm5w18BC%2Fehpbux2jopaxKxyhzoLNouxyEt392JcUFrBzndooy9AbRxbWhsM%2FN49zPE88dkkODt78KQN9Wzog7KV5hEZDBxnihCo7wBC95ulxaLLAh7TWCQQyHGYKcPCXTui0vDUXxue8q7fNw8o5Ui6L5N8EoCTWMWzK7CPdYw%2FLRYxM5c7KJEb6yXmtZ8buWCzp4%2FsltIh9%2F%2FfCp7xOwf5p06qsUJMKXtZFMqemqsuQ0tBDjdJSomCL35wPNKf%2FPERRIn6B4pwsCCdOOH31V9CLZtAYMuN2y0vY25atcUwbE3RdVdzn4nZ16bKPso8yZu0CiuEIgwdaQa4wZyUQwMsxt2NxMhiOHTlnjP5KSqJUNOgKpneAO3oZeEH7FhGYaFLu682tP%2FNQFsVUOt91O4136FJvxKldE40MY5frN9qFvQ8rlhFWPjiaNiM8eRLUUYiM0GfATWqxIaIRk1WrGy8q35%2FZqOc3c4Bi94NBwBYjh0cLxOOjAl7QpuhApMcKdD1e1qOs7B4Z90xBQyhsUfDTnEVlf1J0t2n%2BSfXrSiFhyVdRE%2BZeTi4kgY3r04ICQZhOY209lWzAu2NACmoPyFsCTGHVzKOUx5ht2MBRJtXhWzPRlQw7XriTDNyoe9BjqkAaydFd28T5eOS67yl5Z8JZDiFb4gtlMH7K1tsMrmFFPeQ9ay5jEVuLZU%2FXrqShtYEE1Bvwz1ObBsg23xLjngzXphnuCC5lg%2BVt2PIMmeQf7jhC8WpFgVZIRvLc4C9OafRqwC5J7SFV0s%2F8HHpjWbyHB2QcnbCrgHj1z%2FHkvkFTTpjho87Dz95vJQSo8vRMOEuT9CfiH62g0Y%2BlmO0bjFgfVzxohK&X-Amz-Signature=21f3bcc501b7c486e8bb04142f48be2979d73092b13947390c23a7c79df47f7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIR2BYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDjSv6RwDzdUzOUCNmkJVrzuI2LQA1zpMX8R6pgqKk6cAiAPIEVd%2Fup9J31N5sY9780LqRVntKfN9LTFTJZF3Cnd3Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMXFxM2%2B8BsdQte7COKtwDXB2f0Rmo%2BkjtFbjXEFaOmNyyPb2Ej75%2BEXQ3qjHaCBbNjhu6NiLkJR36VJ45CRPnLUzOHGMm10HHerL89QW2ehXCpj107Cef1P3H7aYCZeAdwe2Kw5BNwA8Fm8orgzNCh2LbZsx0FlGnwXwgpx9x%2FFQU10pxfEoAfFALFtPhntj8Wus9BMEpRoVRtzSfImxOXzoLHCymnQ%2ByU%2FzwFH3WsiNGxvwMy%2B1VHLGCSJvY%2BHK7EzjuufYXzVuPZaP5ViHHUVEF9%2Be%2BGDjoBCVUOoHO1DPgF3b4jEVAb5qlHqMuonlgTwMtpR7Mo%2FKxP6HZzRURcWzAm3%2F6bp9Nt%2F1B5KpWUAzXZlP1XEGveUBZeObE%2BSYCU1DMGpKh95KwovRNfDbPydHhhdw2BRphTBkJ1ROXHiQD4gjFwh4kWNjVvsFAehQb5l540N8E4kMlWtMb2Qh6bBOyygU%2F68TX0oILIhExe3SkkOCVYtaIrbj9diN%2BtLBbLeJefy%2FS8T%2FEN527N72jOFH%2FMvaGT%2FMsy3DtV8xB%2FSDoGoDuh2%2F1fcb3GidXAipH9bOOFEhsVaxDQwGTN4uPSjEUUC4ArcC%2FeGSg%2FX5Y0n%2BonsHj9GLGpLDNxhKB8OtE8V%2BRssqH8MhuRm8wusqHvQY6pgE4CeS63yt46GdgCAFI3dQUxQ7x6aDJbQPqaZwQ2KEKiJnJT%2BLaViD05SqPMDkSvUBeg2FnEdoZ8CWCwGz4G94tblALYcRelhfNpQVFH697yusz0ykjaB4qL4Q4ws6tkYYUbAUwHv4XtembCGollGM6%2BOgvgjPf9H3qHjv56nJGQO2%2BdTOUbI73VF4kGq5nQHEAYRFrudhFOC4VJ2wFWbB50Rm2D8CZ&X-Amz-Signature=3e9699721c07e54b79084da3ecba4f2739c4f1e7bd37e3728913899b20de2481&X-Amz-SignedHeaders=host&x-id=GetObject)
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