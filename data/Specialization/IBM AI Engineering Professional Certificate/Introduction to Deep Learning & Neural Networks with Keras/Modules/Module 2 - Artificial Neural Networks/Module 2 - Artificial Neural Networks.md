

# Module 2: Artificial Neural Networks
## Gradient Descent and Optimization in Neural Networks
### Introduction
In this section, we will discuss the concept of gradient descent, a fundamental algorithm used for optimizing weights and biases in neural networks. Understanding gradient descent is crucial before diving into the mechanics of how neural networks learn through backpropagation. 
### Understanding the Problem
Suppose we have a dataset where $ z  $ is twice the value of $ x $. Our goal is to find the optimal weight $ w $ that generates a line best fitting this data. To achieve this, we define a cost or loss function, denoted as $ J $.
#### Cost Function
The cost function measures the difference between the actual values of $ z  $ and the values predicted by the model, i.e., $ wx $. It is given by:
$$ J(w) = \sum_{i=1}^{n} \left( z_i - w \cdot x_i \right)^2 $$
The objective is to find the value of $ w $ that minimizes this cost function, leading to the best fit line for the data.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bd20068e-2350-4c53-ba35-db137540515b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191203Z&X-Amz-Expires=3600&X-Amz-Signature=2df3d28591824541d35ad925a36e70b29e2ac9a64ed44301411ad11ccafcc7a1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example: Simple Linear Data
For simplicity, consider the case where $ z=2x $. The optimal value of $ w  $ that minimizes the cost function is $ w=2 $, as it perfectly fits the line $ z=2x $.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ce186573-efd7-45c0-81e8-d88b278d76c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191203Z&X-Amz-Expires=3600&X-Amz-Signature=c1cfadce08c7b001284d0641b8bdc319a5977d65e4a1107a1b7011dadac1014f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Introduction to Gradient Descent
Gradient descent is an iterative optimization algorithm used to find the minimum value of a function. It is particularly useful for minimizing the cost function in neural networks.
#### How Gradient Descent Works
1. **Initialization**: Start with a random initial value of $ w $, denoted as $ w_0 $.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3a4b2b9f-74fe-40ea-bd5f-b6da8e8a1b53/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191203Z&X-Amz-Expires=3600&X-Amz-Signature=2ffabe31cbe0cf8edd4680cc88f9cb090841252f27c3621285ee916a07a7f5d4&X-Amz-SignedHeaders=host&x-id=GetObject)
2. **Compute the Gradient**: Calculate the gradient (slope OR derivative) of the cost function at the current value of $ w $. The gradient indicates the direction in which the cost function is increasing.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8bba6cc9-bbcb-4ba7-a8b7-d5c36ae63437/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191203Z&X-Amz-Expires=3600&X-Amz-Signature=e71aa31aad4376b398a8ef3a7811670bc784a6c1b0ddc928c6a21298b5f4fa3b&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Update Rule**: Adjust the value of $ w  $ by moving in the direction opposite to the gradient. This is done using the formula:
$$ w_{i+1} = w_i - \alpha \cdot \text{gradient}(J(w_i)) $$
Here, $ \alpha $ is the learning rate, controlling the step size.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/42a2d642-6adb-46de-883a-9c979db13be1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191203Z&X-Amz-Expires=3600&X-Amz-Signature=5430bfe93f199dcb5b34ba0a6942c55f64df89593df4f01de5119e82377e9a22&X-Amz-SignedHeaders=host&x-id=GetObject)
4. **Iteration**: Repeat the process until the algorithm converges to the minimum value of the cost function or a value close to it.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/045d3977-5b07-4e2d-a476-fe683b0708a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191203Z&X-Amz-Expires=3600&X-Amz-Signature=d2e0c8a77097f0147e7df8941636a2ad1b72bf955ce828a70881852a2c9ffd81&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Choosing the Learning Rate
- **Large Learning Rate**: Can cause the algorithm to overshoot the minimum, leading to divergence.
- **Small Learning Rate**: Can result in slow convergence, making the algorithm take a long time to reach the minimum.
#### Example with Iterations
Assume we start with $ w_0=0.2  $ and use a learning rate $ \alpha = 0.4 $:
- **1st Iteration**: $ w_1  $ moves closer to the optimal value $ w=2 $, causing a significant drop in the cost function.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2ec0fa27-9d1b-46d9-9353-5593db897df3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191203Z&X-Amz-Expires=3600&X-Amz-Signature=c0a0d5c3261b1b504a247dadd7080694d1c59f20e64baa8ad3fe68ea9b569e38&X-Amz-SignedHeaders=host&x-id=GetObject)
- **2nd Iteration**: $ w_2  $ continues to move towards $ w=2 $, with a smaller step as the slope decreases.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3162cdb0-ddff-47b5-ada6-d09807f482dd/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191203Z&X-Amz-Expires=3600&X-Amz-Signature=31b18653add475f79cb1e2a479ffd0d30ddc016b072aa200673ad7ebee315ee2&X-Amz-SignedHeaders=host&x-id=GetObject)
- **Subsequent Iterations**: The steps become smaller as the algorithm approaches the minimum, with the cost function value decreasing steadily.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff65aa88-841b-4a86-8b66-352055ba85a8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191203Z&X-Amz-Expires=3600&X-Amz-Signature=af81f7a175bd9bafc34f1daa43680954ca2e5cf197a14e9664d1afc45883a7d9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Application in Neural Networks
In neural networks, gradient descent is used to optimize multiple weights and biases simultaneously. The algorithm updates each parameter in a way that minimizes the overall cost function, which measures how well the network's predictions match the actual data.
#### Forward Propagation and Gradient Descent
During training, neural networks use forward propagation to calculate the output and then apply gradient descent to adjust the weights and biases, improving the network's performance over time.
### Summary
Gradient descent is a powerful optimization algorithm that iteratively adjusts parameters to minimize a cost function. By understanding how to apply gradient descent to a simple linear problem, we are now equipped to explore more complex scenarios, such as optimizing weights in neural networks using backpropagation.
___
## Gradient Descent and Backpropagation in Neural Networks
#### Training Overview
Neural networks are trained using a supervised learning approach, where each data point has a corresponding label or ground truth. The goal of training is to minimize the difference (error) between the predicted value by the network and the ground truth. This error is calculated and then propagated back into the network to adjust the weights and biases.
#### Error Calculation and Cost Function
- **Error (E):** The error represents the cost or loss function. It measures how far the network's prediction is from the actual value.
- **Squared Error:** For a single neuron, the error is computed as the squared difference between the predicted value $ a_2  $ and the ground truth $ T $:
$$ E = \frac{1}{2} \sum (T - a_2)^2 $$
- In real-world scenarios, the network is trained using large datasets, and the error is calculated as the **Mean Squared Error (MSE)**.
#### Gradient Descent for Optimization
To minimize the error, gradient descent is used. It iteratively updates the weights and biases in the network:
5. **Starting Point:** Begin with random initial weights and biases.
6. **Gradient Calculation:** Compute the gradient (slope) of the cost function with respect to each weight and bias using calculus. This shows how much the error will change if we slightly change the weights or biases.
7. **Update Rule:** The weights and biases are updated using the formula:
$$ w_{\text{new}} = w_{\text{old}} - \text{learning rate} \times \text{gradient} $$
        The learning rate controls how big a step we take towards the minimum of the cost function.
#### Backpropagation
Backpropagation is the method used to calculate the gradients of the error with respect to the weights and biases. It applies the chain rule of calculus to compute how the error propagates back through the network:
- **Derivative Calculation:** Derivatives are taken at each layer to determine how the error affects the weights in that layer.
- **Weight Update:** Weights are adjusted by computing the gradient for each weight and applying the gradient descent rule.
#### Example with One Input and Two Neurons
Consider a network with two neurons:
- **Forward Propagation:** Compute the weighted sums $ z_1, z_2, $ and the outputs $ a_1, a_2 $.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a695635c-0446-4714-a226-718ac9577549/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191209Z&X-Amz-Expires=3600&X-Amz-Signature=12945f1fe5e13576d2b683f990595ec4fc232945f974ca2c532c859e1837282e&X-Amz-SignedHeaders=host&x-id=GetObject)
- **Backpropagation:** If the ground truth is known (e.g., 0.25), the error between the prediction and ground truth is calculated. The weights and biases are then updated using the gradients and a learning rate of 0.4.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd5117c8-af5b-46ec-857b-f6ad4622631f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191209Z&X-Amz-Expires=3600&X-Amz-Signature=23c85f08ad3d37fc7d5b75c84042e81401c54e0682bf67c193ee6ee504c9ebb6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Weight Update Equations
For the second neuron:
- **Derivative of Error (E) with Respect to Weight **$ w_2 $**:**
$$ \frac{\partial E}{\partial w_2} = -(T - a_2) \times a_2 \times (1 - a_2) \times a_1 $$
- **Update Rule for Weight **$ w_2 $**:**
$$ w_2 = w_2 - \text{learning rate} \times \frac{\partial E}{\partial w_2} $$
Similarly, the biases are updated using the derivatives with respect to the biases.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3ed6542e-ad49-481c-bce8-115e2cb8faf9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191209Z&X-Amz-Expires=3600&X-Amz-Signature=03ffb24e06a14f50658f3684fbaa75f6e484a3e8786aa1a5e2e0d79c8d1a482c&X-Amz-SignedHeaders=host&x-id=GetObject)
[NaQwXc72EemgrQ4z3gANog_5cdaec1e385342c1a8095e8b6c3eb7ad_Partial_Derivatives_Backpropagation.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/038b0865-3aac-462b-bab6-083877527b3b/NaQwXc72EemgrQ4z3gANog_5cdaec1e385342c1a8095e8b6c3eb7ad_Partial_Derivatives_Backpropagation.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191209Z&X-Amz-Expires=3600&X-Amz-Signature=2e4a008aa773fed7889618fa4378e39663b3f79f244620f4133557c24ce592bd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Iterative Training Process
Training involves repeatedly performing the following steps until the error is minimized:
8. **Forward Propagation:** Calculate the network output.
9. **Error Calculation:** Compute the error between the prediction and ground truth.
10. **Backpropagation:** Calculate gradients for each weight and bias using the chain rule.
11. **Update Weights and Biases:** Adjust parameters to reduce the error.
This process continues over multiple iterations or epochs until the error is sufficiently small or the maximum number of iterations is reached.
___
## Vanishing Gradient Problem in Neural Networks
### Overview
The **vanishing gradient problem** is a significant issue associated with using the sigmoid activation function in neural networks. It affects the training efficiency and prediction accuracy of the network.
### Problem Description
- **Sigmoid Activation Function**: The sigmoid function maps input values to a range between 0 and 1. While this can be useful, it leads to problems during backpropagation.
- **Gradients in Backpropagation**: During backpropagation, the gradients of the error with respect to the weights are computed. For the sigmoid function, the gradient (derivative) of the activation function is always between 0 and 1. This causes the gradients to become very small as they are propagated backward through the network.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1300f8d7-31e2-4054-a375-dd0677d27731/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191209Z&X-Amz-Expires=3600&X-Amz-Signature=fcff8018da3b189fd35a86ac22443fc4d00b882a7bc7459855177f74848c8d44&X-Amz-SignedHeaders=host&x-id=GetObject)
- **Effect on Learning**: In a neural network with multiple layers, gradients of weights in earlier layers become very small. This results in:
	- **Slow Learning**: Neurons in earlier layers learn very slowly compared to neurons in later layers.
	- **Long Training Time**: Training takes significantly longer.
	- **Compromised Accuracy**: The prediction accuracy of the network may be affected due to inefficient learning in earlier layers.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/5eeb41c8-279a-4556-a186-f41c06da54f6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191204Z&X-Amz-Expires=3600&X-Amz-Signature=4f95b179380f89ee0f0ee9b742b407f3334555993c6b50ab2c057d8af5401591&X-Amz-SignedHeaders=host&x-id=GetObject)
### Mathematical Insight
When using the sigmoid function, the derivatives of the activation function can be very small. During backpropagation, the gradient of the error with respect to the weights is calculated as a product of these derivatives. Thus, gradients tend to diminish as they propagate backward through the network:
$$ \text{Gradient} = \frac{\partial E}{\partial w_i} = \frac{\partial E}{\partial a_n} \cdot \frac{\partial a_n}{\partial z_n} \cdot \frac{\partial z_n}{\partial w_i} $$
where:
- $ \frac{\partial E}{\partial a_n} $ is the gradient of the error with respect to the output $ a_n $.
- $ \frac{\partial a_n}{\partial z_n} $ is the gradient of the sigmoid function, which is small.
- $ \frac{\partial z_n}{\partial w_i} $ depends on the inputs.
### Conclusion
Due to the vanishing gradient problem, sigmoid functions and similar activation functions are not ideal for deep networks. This problem has led to the development and use of alternative activation functions that mitigate this issue.
### Next Steps
In the following notes, alternative activation functions that address the vanishing gradient problem will be introduced. These functions are commonly used in hidden layers of modern neural networks to improve training efficiency and accuracy.
___
## Activation Functions in Neural Networks
### Types of Activation Functions
There are 7 types of most common activation functions:
12. **Sigmoid Function**
13. **Hyperbolic Tangent (tanh) Function**
14. **Rectified Linear Unit (ReLU) Function**
15. **Softmax Function**
16. **Binary Step Function**
17. **Linear Function**
18. **Leaky ReLU**
*Additional Note:* 5-6-7 are not popular functions.
### Introduction
Activation functions are crucial for the learning process of neural networks. They introduce non-linearity into the model, allowing it to learn complex patterns. While the sigmoid function was commonly used in the past, it has notable shortcomings, such as the vanishing gradient problem. This note explores several activation functions and their applications.
### 1. Sigmoid Function
#### Formula
$$ \sigma(z) = \frac{1}{1 + e^{-z}} $$
#### Range
$$ (0, 1) $$
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/20bb4bb6-02a5-4a68-8fe0-6a70da31ed6a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191207Z&X-Amz-Expires=3600&X-Amz-Signature=073c8ad1c19e11102851abe619e9faf3780975abde551bbb2672650fd4f3072b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Characteristics
- Outputs values between 0 and 1.
- Gradients become very small in the regions where $ z $ is very large or very small, leading to the vanishing gradient problem.
- Not symmetric around the origin; all outputs are positive.
#### Applications
Previously popular, but avoided in deep networks due to vanishing gradients.
### 2. Hyperbolic Tangent (tanh) Function
#### Formula
$$ \tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}} $$
#### Range
$$ (-1, 1) $$
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/db2f9c8f-51aa-4db6-aa8c-3855d0b93b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191207Z&X-Amz-Expires=3600&X-Amz-Signature=82c45d0be1ccc07959798e6c7b3e4048d4d338a296161d85218154aecb0b524d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Characteristics
- Similar to the sigmoid function but symmetric around the origin.
- Gradients can still become very small in deep networks, leading to the vanishing gradient problem.
#### Applications
Used in some applications but also limited by vanishing gradients in very deep networks.
### 3. Rectified Linear Unit (ReLU) Function
#### Formula
$$ \text{ReLU}(z) = \max(0, z) $$
#### Range
$$ [ 0, \infty) $$
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/5d06c921-b0fd-40ec-b681-15be7e883d76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191207Z&X-Amz-Expires=3600&X-Amz-Signature=a153986512209f82d86aaf4036663d99838f4229610564c1bcd28c9be17e605d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Characteristics
- Non-linear activation function that only activates neurons with positive input values.
- Helps overcome the vanishing gradient problem by ensuring that gradients are not zero for positive inputs.
- Results in sparse activation where only a few neurons are activated at a time.
#### Applications
Widely used in hidden layers of deep networks due to its efficiency and effectiveness.
### 4. Softmax Function
#### Formula
$$ \text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j} e^{z_j}} $$
#### Range
$$ (0, 1) \text{ (sums to 1 across the output layer)} $$
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7df121d3-29b2-4c62-801d-b1a78e0a433c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20241021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241021T191208Z&X-Amz-Expires=3600&X-Amz-Signature=bcef929561d44f29f214421bfd54203019757a9f9052e2823279f7ce20c800d5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Characteristics
- Converts raw output scores into probabilities that sum to 1.
- Useful for classification tasks where we need to determine the probability of each class.
#### Applications
Commonly used in the output layer of classification networks to handle multi-class problems..
### Conclusion
- **Sigmoid and tanh Functions**: Avoided in many modern applications due to the vanishing gradient problem.
- **ReLU Function**: Preferred activation function in hidden layers of deep networks due to its effectiveness and ability to mitigate vanishing gradients.
- **Softmax Function**: Useful for classification tasks to provide class probabilities.
This concludes the overview of activation functions. For deep learning applications, start with ReLU and consider other functions if necessary based on performance.
___
