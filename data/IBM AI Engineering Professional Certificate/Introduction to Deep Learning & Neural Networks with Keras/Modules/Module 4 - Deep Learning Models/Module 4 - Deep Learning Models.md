

# Module 4: Deep Learning Models
## Deep Neural Networks: An Introduction
### Overview
Neural networks have evolved significantly over time, transitioning from shallow networks to deep neural networks (DNNs) that handle complex tasks and data types. This note explores the distinctions between shallow and deep neural networks, and the reasons behind the recent advancements in deep learning.
### Shallow vs. Deep Neural Networks
#### Shallow Neural Networks
- **Definition**: A shallow neural network typically has only one hidden layer.
- **Characteristics**:
	- Simpler architectures
	- Limited ability to extract features from raw data
	- Often used for simpler tasks or as building blocks for deeper networks
#### Deep Neural Networks
- **Definition**: A deep neural network has multiple hidden layers and neurons.
- **Characteristics**:
	- Capable of learning hierarchical features from raw data such as images and text
	- Ability to extract features from raw data.
	- Handles more complex tasks and datasets
	- Example: Image recognition, natural language processing
### Factors Contributing to the Rise of Deep Learning
#### 1. Advancements in Neural Network Techniques
- **ReLU Activation Function**:
	- Addressed the vanishing gradient problem
	- Enabled the training of very deep networks
#### 2. Availability of Data
- **Importance**:
	- Deep neural networks excel with large datasets
	- Large data helps prevent overfitting
- **Current Trends**:
	- Access to vast amounts of data has become easier
	- Deep learning algorithms benefit significantly from increased data
#### 3. Computational Power
- **GPU Utilization**:
	- NVIDIA GPUs and other high-performance computing resources
	- Reduced training times from weeks to hours
- **Impact**:
	- Enables experimentation with different network architectures and prototypes in shorter periods
### Conclusion
The combination of advancements in neural network techniques, the availability of large datasets, and increased computational power has driven the recent boom in deep learning. The field continues to evolve, with deep neural networks becoming increasingly prevalent in various applications. Upcoming topics will delve into supervised deep learning algorithms and convolutional neural networks (CNNs).
___
## Introduction to Convolutional Neural Networks (CNNs) (Supervised Deep Learning Model)
### Overview
Convolutional Neural Networks (CNNs) are a specialized type of neural network designed for processing structured grid data such as images. This note covers the fundamental architecture of CNNs, their operational mechanisms, and how to build them using the Keras library.
#### Convolutional Neural Networks (CNNs)
### Architecture
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMY6NTAX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIHvhHI%2F%2BA8aiOHXMv%2FFapIzZTWQlWlf8K8empQbGGc3QAiA8Xuu41ANruha1KwfT5fSVDduRuIK084t3syV2wShgmSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfeMZAXue9U3bmyYoKtwDMUGhjzcvdAT2t1%2Bv6lVzNoKTO5UmZ%2BknPIRGVcL9fO4Rg5daIyVHiuqdt%2B10v7cjqvKcIHYJaOuDeAU%2B7%2BR4rRj0ZXIb%2ByVr4rqicmZ%2FD%2FUi4yeJ6pMJ7yV%2FesUlEPUH7NgtPbWYV34kpVQPSRtnsIcqbCqamYnVY3T66TQZCOEJuL8B4QhbL8Mjda1%2B0%2BUw8PcZp0NOuOY1C6bboED4GGHy7FYRzzX2pvHXu%2BVRO6TT2Ewsp%2Belo1LPj%2FF66Fhh3RFSxwHU0ALc%2FhauqHWCbEqwhfmj34jIbSxkL5cgnGj%2BUvLPvm5GocfU1WN4s8mT96HWcLbxb2KTuR9UfdxbvG9abgEIcjlq%2F67T98F3JERyWhlA0OP%2BzgVVGDfeWOEux4unygtE1liVY6N%2BnuBGHbXe%2F%2FJkBeWLay0SMA3t9iE4tA%2F%2BFOUxaQrUWS1Dbc%2BF%2BHkO9nA9ituTACXgOe6%2FhHPkw3MBK5Zc73ziIjGnzRJreW4cGWcpNJEF8KLMbUmBPWfpVod89aqiS%2FRQj0XfKsScd1CGpelN114SG%2B0LfpeAZ93Fnae%2FhLXrsqRJpoukEkHyEVNOele%2BtUJ5DQIPNjx2zuJsaFBSE6u9gn5P%2FNQh56a%2FY1WAyb%2Fz8C4wxI6cvQY6pgGje7KhSuJr%2Bb7YxAsDsYiYq0qkVQaF4jK21Xb0y5dRFgo6JVL%2BYOeSa7L2vEoIKHpQ%2BuUeweGFmC1qmoLMglLZNF9JZuGOS0RNg8x3Ku5lQfUKt6Pe7QujlWS9ZEuOP2sTqb5kKqLLVk2rFe9JkNjpmD8OCYdZfQuBsLnR8RigVxwzwsEouqx9a2mMh7lEiM1J8G1nkoDdxo7GGCcgw2EDy3a5Iw5a&X-Amz-Signature=ed0e7dedfb66babccea647267c33eac398d6a9eb63a1ed77f7395f210c0f891e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMY6NTAX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIHvhHI%2F%2BA8aiOHXMv%2FFapIzZTWQlWlf8K8empQbGGc3QAiA8Xuu41ANruha1KwfT5fSVDduRuIK084t3syV2wShgmSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfeMZAXue9U3bmyYoKtwDMUGhjzcvdAT2t1%2Bv6lVzNoKTO5UmZ%2BknPIRGVcL9fO4Rg5daIyVHiuqdt%2B10v7cjqvKcIHYJaOuDeAU%2B7%2BR4rRj0ZXIb%2ByVr4rqicmZ%2FD%2FUi4yeJ6pMJ7yV%2FesUlEPUH7NgtPbWYV34kpVQPSRtnsIcqbCqamYnVY3T66TQZCOEJuL8B4QhbL8Mjda1%2B0%2BUw8PcZp0NOuOY1C6bboED4GGHy7FYRzzX2pvHXu%2BVRO6TT2Ewsp%2Belo1LPj%2FF66Fhh3RFSxwHU0ALc%2FhauqHWCbEqwhfmj34jIbSxkL5cgnGj%2BUvLPvm5GocfU1WN4s8mT96HWcLbxb2KTuR9UfdxbvG9abgEIcjlq%2F67T98F3JERyWhlA0OP%2BzgVVGDfeWOEux4unygtE1liVY6N%2BnuBGHbXe%2F%2FJkBeWLay0SMA3t9iE4tA%2F%2BFOUxaQrUWS1Dbc%2BF%2BHkO9nA9ituTACXgOe6%2FhHPkw3MBK5Zc73ziIjGnzRJreW4cGWcpNJEF8KLMbUmBPWfpVod89aqiS%2FRQj0XfKsScd1CGpelN114SG%2B0LfpeAZ93Fnae%2FhLXrsqRJpoukEkHyEVNOele%2BtUJ5DQIPNjx2zuJsaFBSE6u9gn5P%2FNQh56a%2FY1WAyb%2Fz8C4wxI6cvQY6pgGje7KhSuJr%2Bb7YxAsDsYiYq0qkVQaF4jK21Xb0y5dRFgo6JVL%2BYOeSa7L2vEoIKHpQ%2BuUeweGFmC1qmoLMglLZNF9JZuGOS0RNg8x3Ku5lQfUKt6Pe7QujlWS9ZEuOP2sTqb5kKqLLVk2rFe9JkNjpmD8OCYdZfQuBsLnR8RigVxwzwsEouqx9a2mMh7lEiM1J8G1nkoDdxo7GGCcgw2EDy3a5Iw5a&X-Amz-Signature=db71ca22af5781f371a464b8c361451c797ab7998c50e7cc7d933634a8a6708e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMY6NTAX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIHvhHI%2F%2BA8aiOHXMv%2FFapIzZTWQlWlf8K8empQbGGc3QAiA8Xuu41ANruha1KwfT5fSVDduRuIK084t3syV2wShgmSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfeMZAXue9U3bmyYoKtwDMUGhjzcvdAT2t1%2Bv6lVzNoKTO5UmZ%2BknPIRGVcL9fO4Rg5daIyVHiuqdt%2B10v7cjqvKcIHYJaOuDeAU%2B7%2BR4rRj0ZXIb%2ByVr4rqicmZ%2FD%2FUi4yeJ6pMJ7yV%2FesUlEPUH7NgtPbWYV34kpVQPSRtnsIcqbCqamYnVY3T66TQZCOEJuL8B4QhbL8Mjda1%2B0%2BUw8PcZp0NOuOY1C6bboED4GGHy7FYRzzX2pvHXu%2BVRO6TT2Ewsp%2Belo1LPj%2FF66Fhh3RFSxwHU0ALc%2FhauqHWCbEqwhfmj34jIbSxkL5cgnGj%2BUvLPvm5GocfU1WN4s8mT96HWcLbxb2KTuR9UfdxbvG9abgEIcjlq%2F67T98F3JERyWhlA0OP%2BzgVVGDfeWOEux4unygtE1liVY6N%2BnuBGHbXe%2F%2FJkBeWLay0SMA3t9iE4tA%2F%2BFOUxaQrUWS1Dbc%2BF%2BHkO9nA9ituTACXgOe6%2FhHPkw3MBK5Zc73ziIjGnzRJreW4cGWcpNJEF8KLMbUmBPWfpVod89aqiS%2FRQj0XfKsScd1CGpelN114SG%2B0LfpeAZ93Fnae%2FhLXrsqRJpoukEkHyEVNOele%2BtUJ5DQIPNjx2zuJsaFBSE6u9gn5P%2FNQh56a%2FY1WAyb%2Fz8C4wxI6cvQY6pgGje7KhSuJr%2Bb7YxAsDsYiYq0qkVQaF4jK21Xb0y5dRFgo6JVL%2BYOeSa7L2vEoIKHpQ%2BuUeweGFmC1qmoLMglLZNF9JZuGOS0RNg8x3Ku5lQfUKt6Pe7QujlWS9ZEuOP2sTqb5kKqLLVk2rFe9JkNjpmD8OCYdZfQuBsLnR8RigVxwzwsEouqx9a2mMh7lEiM1J8G1nkoDdxo7GGCcgw2EDy3a5Iw5a&X-Amz-Signature=0afe29dc1f9962ff2c5c40539732cfff94ebb5f52a8d3e405b581bbe49dcdb5e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMY6NTAX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIHvhHI%2F%2BA8aiOHXMv%2FFapIzZTWQlWlf8K8empQbGGc3QAiA8Xuu41ANruha1KwfT5fSVDduRuIK084t3syV2wShgmSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfeMZAXue9U3bmyYoKtwDMUGhjzcvdAT2t1%2Bv6lVzNoKTO5UmZ%2BknPIRGVcL9fO4Rg5daIyVHiuqdt%2B10v7cjqvKcIHYJaOuDeAU%2B7%2BR4rRj0ZXIb%2ByVr4rqicmZ%2FD%2FUi4yeJ6pMJ7yV%2FesUlEPUH7NgtPbWYV34kpVQPSRtnsIcqbCqamYnVY3T66TQZCOEJuL8B4QhbL8Mjda1%2B0%2BUw8PcZp0NOuOY1C6bboED4GGHy7FYRzzX2pvHXu%2BVRO6TT2Ewsp%2Belo1LPj%2FF66Fhh3RFSxwHU0ALc%2FhauqHWCbEqwhfmj34jIbSxkL5cgnGj%2BUvLPvm5GocfU1WN4s8mT96HWcLbxb2KTuR9UfdxbvG9abgEIcjlq%2F67T98F3JERyWhlA0OP%2BzgVVGDfeWOEux4unygtE1liVY6N%2BnuBGHbXe%2F%2FJkBeWLay0SMA3t9iE4tA%2F%2BFOUxaQrUWS1Dbc%2BF%2BHkO9nA9ituTACXgOe6%2FhHPkw3MBK5Zc73ziIjGnzRJreW4cGWcpNJEF8KLMbUmBPWfpVod89aqiS%2FRQj0XfKsScd1CGpelN114SG%2B0LfpeAZ93Fnae%2FhLXrsqRJpoukEkHyEVNOele%2BtUJ5DQIPNjx2zuJsaFBSE6u9gn5P%2FNQh56a%2FY1WAyb%2Fz8C4wxI6cvQY6pgGje7KhSuJr%2Bb7YxAsDsYiYq0qkVQaF4jK21Xb0y5dRFgo6JVL%2BYOeSa7L2vEoIKHpQ%2BuUeweGFmC1qmoLMglLZNF9JZuGOS0RNg8x3Ku5lQfUKt6Pe7QujlWS9ZEuOP2sTqb5kKqLLVk2rFe9JkNjpmD8OCYdZfQuBsLnR8RigVxwzwsEouqx9a2mMh7lEiM1J8G1nkoDdxo7GGCcgw2EDy3a5Iw5a&X-Amz-Signature=0333ab4f81d234c40bc2974a3f1ae4a3a83cf4a577290c429a5d38b377e1a553&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMY6NTAX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIHvhHI%2F%2BA8aiOHXMv%2FFapIzZTWQlWlf8K8empQbGGc3QAiA8Xuu41ANruha1KwfT5fSVDduRuIK084t3syV2wShgmSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfeMZAXue9U3bmyYoKtwDMUGhjzcvdAT2t1%2Bv6lVzNoKTO5UmZ%2BknPIRGVcL9fO4Rg5daIyVHiuqdt%2B10v7cjqvKcIHYJaOuDeAU%2B7%2BR4rRj0ZXIb%2ByVr4rqicmZ%2FD%2FUi4yeJ6pMJ7yV%2FesUlEPUH7NgtPbWYV34kpVQPSRtnsIcqbCqamYnVY3T66TQZCOEJuL8B4QhbL8Mjda1%2B0%2BUw8PcZp0NOuOY1C6bboED4GGHy7FYRzzX2pvHXu%2BVRO6TT2Ewsp%2Belo1LPj%2FF66Fhh3RFSxwHU0ALc%2FhauqHWCbEqwhfmj34jIbSxkL5cgnGj%2BUvLPvm5GocfU1WN4s8mT96HWcLbxb2KTuR9UfdxbvG9abgEIcjlq%2F67T98F3JERyWhlA0OP%2BzgVVGDfeWOEux4unygtE1liVY6N%2BnuBGHbXe%2F%2FJkBeWLay0SMA3t9iE4tA%2F%2BFOUxaQrUWS1Dbc%2BF%2BHkO9nA9ituTACXgOe6%2FhHPkw3MBK5Zc73ziIjGnzRJreW4cGWcpNJEF8KLMbUmBPWfpVod89aqiS%2FRQj0XfKsScd1CGpelN114SG%2B0LfpeAZ93Fnae%2FhLXrsqRJpoukEkHyEVNOele%2BtUJ5DQIPNjx2zuJsaFBSE6u9gn5P%2FNQh56a%2FY1WAyb%2Fz8C4wxI6cvQY6pgGje7KhSuJr%2Bb7YxAsDsYiYq0qkVQaF4jK21Xb0y5dRFgo6JVL%2BYOeSa7L2vEoIKHpQ%2BuUeweGFmC1qmoLMglLZNF9JZuGOS0RNg8x3Ku5lQfUKt6Pe7QujlWS9ZEuOP2sTqb5kKqLLVk2rFe9JkNjpmD8OCYdZfQuBsLnR8RigVxwzwsEouqx9a2mMh7lEiM1J8G1nkoDdxo7GGCcgw2EDy3a5Iw5a&X-Amz-Signature=3071de5ffc0f7999705d90bb07a4ff84b76bc03849c76c02ea053b2ced4157e1&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMY6NTAX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIHvhHI%2F%2BA8aiOHXMv%2FFapIzZTWQlWlf8K8empQbGGc3QAiA8Xuu41ANruha1KwfT5fSVDduRuIK084t3syV2wShgmSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfeMZAXue9U3bmyYoKtwDMUGhjzcvdAT2t1%2Bv6lVzNoKTO5UmZ%2BknPIRGVcL9fO4Rg5daIyVHiuqdt%2B10v7cjqvKcIHYJaOuDeAU%2B7%2BR4rRj0ZXIb%2ByVr4rqicmZ%2FD%2FUi4yeJ6pMJ7yV%2FesUlEPUH7NgtPbWYV34kpVQPSRtnsIcqbCqamYnVY3T66TQZCOEJuL8B4QhbL8Mjda1%2B0%2BUw8PcZp0NOuOY1C6bboED4GGHy7FYRzzX2pvHXu%2BVRO6TT2Ewsp%2Belo1LPj%2FF66Fhh3RFSxwHU0ALc%2FhauqHWCbEqwhfmj34jIbSxkL5cgnGj%2BUvLPvm5GocfU1WN4s8mT96HWcLbxb2KTuR9UfdxbvG9abgEIcjlq%2F67T98F3JERyWhlA0OP%2BzgVVGDfeWOEux4unygtE1liVY6N%2BnuBGHbXe%2F%2FJkBeWLay0SMA3t9iE4tA%2F%2BFOUxaQrUWS1Dbc%2BF%2BHkO9nA9ituTACXgOe6%2FhHPkw3MBK5Zc73ziIjGnzRJreW4cGWcpNJEF8KLMbUmBPWfpVod89aqiS%2FRQj0XfKsScd1CGpelN114SG%2B0LfpeAZ93Fnae%2FhLXrsqRJpoukEkHyEVNOele%2BtUJ5DQIPNjx2zuJsaFBSE6u9gn5P%2FNQh56a%2FY1WAyb%2Fz8C4wxI6cvQY6pgGje7KhSuJr%2Bb7YxAsDsYiYq0qkVQaF4jK21Xb0y5dRFgo6JVL%2BYOeSa7L2vEoIKHpQ%2BuUeweGFmC1qmoLMglLZNF9JZuGOS0RNg8x3Ku5lQfUKt6Pe7QujlWS9ZEuOP2sTqb5kKqLLVk2rFe9JkNjpmD8OCYdZfQuBsLnR8RigVxwzwsEouqx9a2mMh7lEiM1J8G1nkoDdxo7GGCcgw2EDy3a5Iw5a&X-Amz-Signature=2716b119860e68a511ba08a4d8e25446d1e8f70eec0d1fecb9bfea87c9f0ee7b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMY6NTAX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIHvhHI%2F%2BA8aiOHXMv%2FFapIzZTWQlWlf8K8empQbGGc3QAiA8Xuu41ANruha1KwfT5fSVDduRuIK084t3syV2wShgmSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfeMZAXue9U3bmyYoKtwDMUGhjzcvdAT2t1%2Bv6lVzNoKTO5UmZ%2BknPIRGVcL9fO4Rg5daIyVHiuqdt%2B10v7cjqvKcIHYJaOuDeAU%2B7%2BR4rRj0ZXIb%2ByVr4rqicmZ%2FD%2FUi4yeJ6pMJ7yV%2FesUlEPUH7NgtPbWYV34kpVQPSRtnsIcqbCqamYnVY3T66TQZCOEJuL8B4QhbL8Mjda1%2B0%2BUw8PcZp0NOuOY1C6bboED4GGHy7FYRzzX2pvHXu%2BVRO6TT2Ewsp%2Belo1LPj%2FF66Fhh3RFSxwHU0ALc%2FhauqHWCbEqwhfmj34jIbSxkL5cgnGj%2BUvLPvm5GocfU1WN4s8mT96HWcLbxb2KTuR9UfdxbvG9abgEIcjlq%2F67T98F3JERyWhlA0OP%2BzgVVGDfeWOEux4unygtE1liVY6N%2BnuBGHbXe%2F%2FJkBeWLay0SMA3t9iE4tA%2F%2BFOUxaQrUWS1Dbc%2BF%2BHkO9nA9ituTACXgOe6%2FhHPkw3MBK5Zc73ziIjGnzRJreW4cGWcpNJEF8KLMbUmBPWfpVod89aqiS%2FRQj0XfKsScd1CGpelN114SG%2B0LfpeAZ93Fnae%2FhLXrsqRJpoukEkHyEVNOele%2BtUJ5DQIPNjx2zuJsaFBSE6u9gn5P%2FNQh56a%2FY1WAyb%2Fz8C4wxI6cvQY6pgGje7KhSuJr%2Bb7YxAsDsYiYq0qkVQaF4jK21Xb0y5dRFgo6JVL%2BYOeSa7L2vEoIKHpQ%2BuUeweGFmC1qmoLMglLZNF9JZuGOS0RNg8x3Ku5lQfUKt6Pe7QujlWS9ZEuOP2sTqb5kKqLLVk2rFe9JkNjpmD8OCYdZfQuBsLnR8RigVxwzwsEouqx9a2mMh7lEiM1J8G1nkoDdxo7GGCcgw2EDy3a5Iw5a&X-Amz-Signature=648f9a2c06c7ca3802c427927311f78236bd06039cb7305e42a2c7ecb21a7fe1&X-Amz-SignedHeaders=host&x-id=GetObject)
### CNN Architecture
- **Input Layer**: Defines the size of the input images (e.g., 128 x 128 x 3 for color images).
- **Convolutional Layers**: Apply multiple filters and include ReLU activation.
- **Pooling Layers**: Apply max-pooling or average-pooling.
- **Fully Connected Layers**: Flatten the data and produce output based on the number of classes.
- **Output Layer**: Produces the final class probabilities using the softmax activation function.
### Summary
- **Efficiency**: CNNs reduce the number of parameters compared to traditional neural networks, making them computationally efficient.
- **Applications**: Ideal for tasks involving image recognition, object detection, and other computer vision problems.
### Building CNNs with Keras
1. **Model Creation**:
	- Use the `Sequential` model to build the CNN.
2. **Defining Input Shape**:
	- For 128x128 color images: `input_shape=(128, 128, 3)`
3. **Adding Layers**:
	- **Convolutional Layer**:
```python
model.add(Conv2D(16, (2, 2), strides=(1, 1), activation='relu', input_shape=(128, 128, 3)))
```
		- **Parameters**:
			- `16`: Number of filters or kernels.
			- `(2, 2)`: Size of each filter.
			- `strides=(1, 1)`: The step size with which the filter moves across the image.
			- `activation='relu'`: Activation function applied after the convolution operation.
			- `input_shape=(128, 128, 3)`: Shape of the input images. For color images, the last dimension is 3 (RGB channels).
	- **Pooling Layer**:
```python
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
```
		- **Parameters**:
			- `pool_size=(2, 2)`: Size of the pooling window.
			- `strides=(2, 2)`: The step size with which the pooling window moves across the image.
	- **Additional Convolutional and Pooling Layers**:
```python
model.add(Conv2D(32, (2, 2), strides=(1, 1), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
```
		- **Parameters**:
			- `32`: Number of filters or kernels in this convolutional layer.
			- `(2, 2)`: Size of each filter.
			- `strides=(1, 1)`: The step size with which the filter moves across the image.
			- `activation='relu'`: Activation function applied after the convolution operation.
			- `pool_size=(2, 2)`: Size of the pooling window.
			- `strides=(2, 2)`: The step size with which the pooling window moves across the image.
4. **Flattening and Fully Connected Layers**:
	- **Flatten**: Converts 3D feature maps into 1D.
```python
model.add(Flatten())
```
	- **Dense Layers**:
```python
model.add(Dense(100, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
```
		- **Parameters**:
			- `100`: Number of neurons in the dense layer.
			- `activation='relu'`: Activation function applied to the neurons in the dense layer.
			- `num_classes`: Number of output neurons, typically equal to the number of classes in the classification problem.
			- `activation='softmax'`: Activation function applied to the output layer to convert raw scores into probabilities.
5. **Compilation**:
	- Define optimizer, loss function, and metrics:
```python
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```
		- **Parameters**:
			- `optimizer='adam'`: Optimization algorithm used for training.
			- `loss='categorical_crossentropy'`: Loss function used for classification tasks with multiple classes.
			- `metrics=['accuracy']`: Evaluation metric used to measure the performance of the model.
6. **Training and Validation**:
	- Train the model using the `fit` method and validate using a test set.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMY6NTAX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIHvhHI%2F%2BA8aiOHXMv%2FFapIzZTWQlWlf8K8empQbGGc3QAiA8Xuu41ANruha1KwfT5fSVDduRuIK084t3syV2wShgmSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfeMZAXue9U3bmyYoKtwDMUGhjzcvdAT2t1%2Bv6lVzNoKTO5UmZ%2BknPIRGVcL9fO4Rg5daIyVHiuqdt%2B10v7cjqvKcIHYJaOuDeAU%2B7%2BR4rRj0ZXIb%2ByVr4rqicmZ%2FD%2FUi4yeJ6pMJ7yV%2FesUlEPUH7NgtPbWYV34kpVQPSRtnsIcqbCqamYnVY3T66TQZCOEJuL8B4QhbL8Mjda1%2B0%2BUw8PcZp0NOuOY1C6bboED4GGHy7FYRzzX2pvHXu%2BVRO6TT2Ewsp%2Belo1LPj%2FF66Fhh3RFSxwHU0ALc%2FhauqHWCbEqwhfmj34jIbSxkL5cgnGj%2BUvLPvm5GocfU1WN4s8mT96HWcLbxb2KTuR9UfdxbvG9abgEIcjlq%2F67T98F3JERyWhlA0OP%2BzgVVGDfeWOEux4unygtE1liVY6N%2BnuBGHbXe%2F%2FJkBeWLay0SMA3t9iE4tA%2F%2BFOUxaQrUWS1Dbc%2BF%2BHkO9nA9ituTACXgOe6%2FhHPkw3MBK5Zc73ziIjGnzRJreW4cGWcpNJEF8KLMbUmBPWfpVod89aqiS%2FRQj0XfKsScd1CGpelN114SG%2B0LfpeAZ93Fnae%2FhLXrsqRJpoukEkHyEVNOele%2BtUJ5DQIPNjx2zuJsaFBSE6u9gn5P%2FNQh56a%2FY1WAyb%2Fz8C4wxI6cvQY6pgGje7KhSuJr%2Bb7YxAsDsYiYq0qkVQaF4jK21Xb0y5dRFgo6JVL%2BYOeSa7L2vEoIKHpQ%2BuUeweGFmC1qmoLMglLZNF9JZuGOS0RNg8x3Ku5lQfUKt6Pe7QujlWS9ZEuOP2sTqb5kKqLLVk2rFe9JkNjpmD8OCYdZfQuBsLnR8RigVxwzwsEouqx9a2mMh7lEiM1J8G1nkoDdxo7GGCcgw2EDy3a5Iw5a&X-Amz-Signature=7318d8404d181e65e13643e1c616f250763964e797cc05676d6c332fdc913e8c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Conclusion
CNNs are powerful for image processing tasks due to their ability to automatically extract and learn features from images. The architecture involves convolutional, activation, pooling, and fully connected layers, which collectively enable the network to perform tasks such as image recognition and object detection.
___
## Recurrent Neural Networks (RNNs) Overview (Unsupervised Deep Learning Model)
### Introduction to RNNs
- **Purpose**: RNNs are used to analyze sequences where data points are not independent but rather follow a temporal or sequential relationship.
- **Architecture**: RNNs include loops that allow them to take both the current input and the output from the previous data point into account.
### How RNNs Work
- **Input and Output at Each Time Step**:
	- At time `t = 0`, the network takes in input $ x_0 $ and outputs $ a_0 $.
	- At time `t = 1`, the network takes in input $ x_1 $` `and the previous output $ a_0 $, weighted by $ w_{1,2} $.
	- This process continues, incorporating previous outputs into the computation at each step.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMY6NTAX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIHvhHI%2F%2BA8aiOHXMv%2FFapIzZTWQlWlf8K8empQbGGc3QAiA8Xuu41ANruha1KwfT5fSVDduRuIK084t3syV2wShgmSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfeMZAXue9U3bmyYoKtwDMUGhjzcvdAT2t1%2Bv6lVzNoKTO5UmZ%2BknPIRGVcL9fO4Rg5daIyVHiuqdt%2B10v7cjqvKcIHYJaOuDeAU%2B7%2BR4rRj0ZXIb%2ByVr4rqicmZ%2FD%2FUi4yeJ6pMJ7yV%2FesUlEPUH7NgtPbWYV34kpVQPSRtnsIcqbCqamYnVY3T66TQZCOEJuL8B4QhbL8Mjda1%2B0%2BUw8PcZp0NOuOY1C6bboED4GGHy7FYRzzX2pvHXu%2BVRO6TT2Ewsp%2Belo1LPj%2FF66Fhh3RFSxwHU0ALc%2FhauqHWCbEqwhfmj34jIbSxkL5cgnGj%2BUvLPvm5GocfU1WN4s8mT96HWcLbxb2KTuR9UfdxbvG9abgEIcjlq%2F67T98F3JERyWhlA0OP%2BzgVVGDfeWOEux4unygtE1liVY6N%2BnuBGHbXe%2F%2FJkBeWLay0SMA3t9iE4tA%2F%2BFOUxaQrUWS1Dbc%2BF%2BHkO9nA9ituTACXgOe6%2FhHPkw3MBK5Zc73ziIjGnzRJreW4cGWcpNJEF8KLMbUmBPWfpVod89aqiS%2FRQj0XfKsScd1CGpelN114SG%2B0LfpeAZ93Fnae%2FhLXrsqRJpoukEkHyEVNOele%2BtUJ5DQIPNjx2zuJsaFBSE6u9gn5P%2FNQh56a%2FY1WAyb%2Fz8C4wxI6cvQY6pgGje7KhSuJr%2Bb7YxAsDsYiYq0qkVQaF4jK21Xb0y5dRFgo6JVL%2BYOeSa7L2vEoIKHpQ%2BuUeweGFmC1qmoLMglLZNF9JZuGOS0RNg8x3Ku5lQfUKt6Pe7QujlWS9ZEuOP2sTqb5kKqLLVk2rFe9JkNjpmD8OCYdZfQuBsLnR8RigVxwzwsEouqx9a2mMh7lEiM1J8G1nkoDdxo7GGCcgw2EDy3a5Iw5a&X-Amz-Signature=b33e49ce56e586a4fb85e1b3b0efff98d23ce2eaeef7f9de74fee30a972fd7a2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Applications of RNNs
- **Text Analysis**: Suitable for processing and modeling sequential text data.
- **Genomic Data**: Can analyze sequences in genetic information.
- **Handwriting**: Applied in handwriting generation and recognition.
- **Stock Markets**: Used for predicting stock prices based on historical data.
### Long Short-Term Memory (LSTM) Networks
- **Overview**: A specialized type of RNN designed to overcome some limitations of traditional RNNs.
- **Applications**:
	- **Image Generation**: Models trained on images to generate novel images.
	- **Handwriting Generation**: Creating handwritten text based on trained models.
	- **Image Description**: Automatically describing images.
	- **Video Streams**: Analyzing and describing video sequences.
### Summary
- **RNNs**: Effective for tasks involving sequences and temporal data.
- **LSTM Models**: A specific type of RNN that handles long-term dependencies and is used in advanced applications like image and video analysis.
___
### Autoencoders and Restricted Boltzmann Machines (RBMs)
### Introduction to Autoencoders
- **Definition**: Autoencoders are unsupervised deep learning models used for data compression. They learn to compress and decompress data automatically through neural networks.
- **Purpose**: They aim to learn a compressed representation of the input data and then reconstruct the original data from this representation.
- **Training**: Autoencoders use backpropagation with the target variable being the same as the input, effectively learning an approximation of an identity function.
### Architecture of an Autoencoder
- **Encoder**:
	- Compresses the input data into a lower-dimensional representation.
- **Decoder**:
	- Reconstructs the original data from the compressed representation.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4SNJ5S2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIA4OqOlxMmXW%2B%2BH3joS1ABpiKYmu9wq6wSwToO9CuDZFAiEAucGK1N8tvxxg4Kd9d38KYvea5yZ9MNaAXESlAfkJYMMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJo1q7bbCmg49ULvSSrcA6OoAJZsE%2BaFVSf%2BVRhipyNtjIeRsYeyT1kLc5yfm1%2FdBCnhytZuY6abTtmMtxVRW9PAg%2Fvb1%2BzVKsnnSBUf8LW1P4BwNolvK4hyA90Zi11brTAjIt441svehe2v1%2BVx8VtVmzU1X57Sm38dBlgDAc6J%2FfJHrrLFf9EB6b7uWZFZyLy3JvN5BAbJa1dSFRKOY6iSTUkJpkkeSnmlPjlsnI3mGYP7KXaibYyl9TUwh7xOt5eNOkYWDdveKqA2cKoO7pXHgi6Ma9Ui2cl3Vbf9PrDcQHlVGo8fWdO0BrWStABzync3VgOuqhUMqkcL462bQVjL8idsahOXi1NcuZoXTa49SlE6GW0qezFCn0n3bQXfaLmeZ%2F3p2WP7xLtH75IM3ljcolz6B4tMoT6EHAI4OM82M5s2eFsBobtXZ%2BM1Y%2FpS697QyRvYyZldY88y7nQMjlGJXBs86a5UV6LHL5pcOsZEe1FrDaFZuo5uWQZN%2FaH5b6NCfzsekYgAP2uZIu2Ah88Q%2FrYqZhJgd48V5R6PF0fJhLTMQH0wHrXG27V2EYMaGLSU1%2BW%2BtBhtJdaWrC%2BSvk0d8UMhi%2FtUDNKdbU3zxymIcGbLOb%2FH%2FDYpraXfXqhVmuPJuWFp6%2FYDIL%2FAMJCOnL0GOqUB8u9kom1eoghBmBGAmlL85WlLBp2bpL%2F6ToPUdi2i5rA9SB3%2Bj2sDI4%2FUD1l%2BQ7WsT21klxfEIRvTRPUEvZtuTHahVLXcVTVbuEIXPqrFt3jpw9sNrgCMzLWEBClW5vKzzvhKWZkE2Glgynm8XjTlFzacf0CZMEHds0WuztwbrJFBEpXxPx6HjMPlcuwLuGBEFi5z9lZD8%2Boml4EnxMue1kmKwMYH&X-Amz-Signature=2cb15c2a3ee6a04ce32682fd1fdb9d1c42f1d256ad80f31a5c860d989915c4c5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Applications of Autoencoders
- **Data Denoising**: Removing noise from data to recover the original signal.
- **Dimensionality Reduction**: Reducing the number of features in the data for visualization purposes.
### Advantages over Traditional Methods
- **Non-Linear Transformations**: Autoencoders, with their non-linear activation functions, can learn more complex projections compared to linear methods like Principal Component Analysis (PCA).
### Restricted Boltzmann Machines (RBMs)
- **Overview**: RBMs are a type of autoencoder that can learn the distribution of the input data to perform tasks such as:
	- **Fixing Imbalanced Datasets**: Generating more data points for minority classes to balance datasets.
	- **Estimating Missing Values**: Predicting missing feature values in datasets.
	- **Automatic Feature Extraction**: Learning features from unstructured data.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4SNJ5S2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIA4OqOlxMmXW%2B%2BH3joS1ABpiKYmu9wq6wSwToO9CuDZFAiEAucGK1N8tvxxg4Kd9d38KYvea5yZ9MNaAXESlAfkJYMMqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJo1q7bbCmg49ULvSSrcA6OoAJZsE%2BaFVSf%2BVRhipyNtjIeRsYeyT1kLc5yfm1%2FdBCnhytZuY6abTtmMtxVRW9PAg%2Fvb1%2BzVKsnnSBUf8LW1P4BwNolvK4hyA90Zi11brTAjIt441svehe2v1%2BVx8VtVmzU1X57Sm38dBlgDAc6J%2FfJHrrLFf9EB6b7uWZFZyLy3JvN5BAbJa1dSFRKOY6iSTUkJpkkeSnmlPjlsnI3mGYP7KXaibYyl9TUwh7xOt5eNOkYWDdveKqA2cKoO7pXHgi6Ma9Ui2cl3Vbf9PrDcQHlVGo8fWdO0BrWStABzync3VgOuqhUMqkcL462bQVjL8idsahOXi1NcuZoXTa49SlE6GW0qezFCn0n3bQXfaLmeZ%2F3p2WP7xLtH75IM3ljcolz6B4tMoT6EHAI4OM82M5s2eFsBobtXZ%2BM1Y%2FpS697QyRvYyZldY88y7nQMjlGJXBs86a5UV6LHL5pcOsZEe1FrDaFZuo5uWQZN%2FaH5b6NCfzsekYgAP2uZIu2Ah88Q%2FrYqZhJgd48V5R6PF0fJhLTMQH0wHrXG27V2EYMaGLSU1%2BW%2BtBhtJdaWrC%2BSvk0d8UMhi%2FtUDNKdbU3zxymIcGbLOb%2FH%2FDYpraXfXqhVmuPJuWFp6%2FYDIL%2FAMJCOnL0GOqUB8u9kom1eoghBmBGAmlL85WlLBp2bpL%2F6ToPUdi2i5rA9SB3%2Bj2sDI4%2FUD1l%2BQ7WsT21klxfEIRvTRPUEvZtuTHahVLXcVTVbuEIXPqrFt3jpw9sNrgCMzLWEBClW5vKzzvhKWZkE2Glgynm8XjTlFzacf0CZMEHds0WuztwbrJFBEpXxPx6HjMPlcuwLuGBEFi5z9lZD8%2Boml4EnxMue1kmKwMYH&X-Amz-Signature=2ad109813d1d01a9a33559ada0d99ac59add700278dce2588e302236660c8fe9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
