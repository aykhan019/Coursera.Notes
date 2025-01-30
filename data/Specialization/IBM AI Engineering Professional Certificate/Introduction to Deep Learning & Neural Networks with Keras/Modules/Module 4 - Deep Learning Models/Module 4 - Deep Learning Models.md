

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623376QA3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKfD%2FOQXt29azGBOTEABS%2BlEZGUY2V0V3EBS%2BK%2F4u9kAIgczPjlP09wt0UmfsfkT3CyRoPIUwk9vCBn7sg473KVUkqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3DCFwgWyNiz0ra4CrcAz3YC9xy3Smp5TgHfaKdAJ7G3SyP0Rw4L91Zbs1BUoerkVjXq%2BtnhOz0MvvDMi8haU6172PcvF7mxZxnnbj51sV7zA98UQW33bfb4UFK6qg1rjQ2FDAFxbt1g4HT%2BV2Mplffl1T1ZML27OCX0kUQZwl794n%2F5MfjS41x0oh8yZrTppbuMvXQ%2F9gHV81Nj%2FOTa8vbvBu9KAkT%2FGFAoKmm5shL9s5r0w9sa5cT86OwOq9iEGxxOyokWIjet95XNfFK7rHyuvubgIDynOyjALm0ToSvrjhh6ddr8QrJ5WTIrgJ1J0WX7wmzreT1dEz339ptvDQJ%2BOJkwbA4gV32LBcMvvEydZWcDmgRXKcNG3Ti5KmYz0vYufJBNcHHhAQd1QqpGmG3yFfWUSWgKZdx7lyHu%2F7pNZhm7sKII0BCTZjB0O3bbyh5LNQN%2BcWrvlaBOrL45lvu8FrrgvCUKJBd4yShXLP%2FOvijztNb2StPEbRipBzAU00y6VfMwR2v2oAV1fnLENxPP58Ie%2Fw%2FrPrEjE933YPsj46IlQlxer7o5k2tyP7GdMgXcIeRTK7TsTCBXbJUpQ6Rc3HTdkDssVrcr%2BaLUHgl1SNCQBHROlB9pXiRckR60MYxzL12NW9gmKFkMOL877wGOqUB7PeAsV%2BaBTwCVpqx%2FtYaW40Ch%2BUcvWIksfC1E2zBp2cF7LbhJcOImobldlL986k%2B8rg0ovQwlDDLu0bvMpEq62vy%2BCyvi%2FZ4nNi5AyVTLX4kzTgQutsf3kPa1R78yeFw4Z1tmsx7DdxB3G9EJh5fFQYLm1I4hj1AXfvv3JCXtYei2UmBQ8kbVP8%2Fuc6a4cEwNXOqoWtE4kQVhPx3431plIedlxXS&X-Amz-Signature=b611984eeb967613c49b50a1ec8b2174c82b190a25afcea26c3fc16cbcc2bdd4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623376QA3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKfD%2FOQXt29azGBOTEABS%2BlEZGUY2V0V3EBS%2BK%2F4u9kAIgczPjlP09wt0UmfsfkT3CyRoPIUwk9vCBn7sg473KVUkqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3DCFwgWyNiz0ra4CrcAz3YC9xy3Smp5TgHfaKdAJ7G3SyP0Rw4L91Zbs1BUoerkVjXq%2BtnhOz0MvvDMi8haU6172PcvF7mxZxnnbj51sV7zA98UQW33bfb4UFK6qg1rjQ2FDAFxbt1g4HT%2BV2Mplffl1T1ZML27OCX0kUQZwl794n%2F5MfjS41x0oh8yZrTppbuMvXQ%2F9gHV81Nj%2FOTa8vbvBu9KAkT%2FGFAoKmm5shL9s5r0w9sa5cT86OwOq9iEGxxOyokWIjet95XNfFK7rHyuvubgIDynOyjALm0ToSvrjhh6ddr8QrJ5WTIrgJ1J0WX7wmzreT1dEz339ptvDQJ%2BOJkwbA4gV32LBcMvvEydZWcDmgRXKcNG3Ti5KmYz0vYufJBNcHHhAQd1QqpGmG3yFfWUSWgKZdx7lyHu%2F7pNZhm7sKII0BCTZjB0O3bbyh5LNQN%2BcWrvlaBOrL45lvu8FrrgvCUKJBd4yShXLP%2FOvijztNb2StPEbRipBzAU00y6VfMwR2v2oAV1fnLENxPP58Ie%2Fw%2FrPrEjE933YPsj46IlQlxer7o5k2tyP7GdMgXcIeRTK7TsTCBXbJUpQ6Rc3HTdkDssVrcr%2BaLUHgl1SNCQBHROlB9pXiRckR60MYxzL12NW9gmKFkMOL877wGOqUB7PeAsV%2BaBTwCVpqx%2FtYaW40Ch%2BUcvWIksfC1E2zBp2cF7LbhJcOImobldlL986k%2B8rg0ovQwlDDLu0bvMpEq62vy%2BCyvi%2FZ4nNi5AyVTLX4kzTgQutsf3kPa1R78yeFw4Z1tmsx7DdxB3G9EJh5fFQYLm1I4hj1AXfvv3JCXtYei2UmBQ8kbVP8%2Fuc6a4cEwNXOqoWtE4kQVhPx3431plIedlxXS&X-Amz-Signature=bd6dd78b11fa97ad96cefb2dd8d03ac63e9dcc6db2fbe4b940d27d8638ae3cae&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623376QA3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKfD%2FOQXt29azGBOTEABS%2BlEZGUY2V0V3EBS%2BK%2F4u9kAIgczPjlP09wt0UmfsfkT3CyRoPIUwk9vCBn7sg473KVUkqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3DCFwgWyNiz0ra4CrcAz3YC9xy3Smp5TgHfaKdAJ7G3SyP0Rw4L91Zbs1BUoerkVjXq%2BtnhOz0MvvDMi8haU6172PcvF7mxZxnnbj51sV7zA98UQW33bfb4UFK6qg1rjQ2FDAFxbt1g4HT%2BV2Mplffl1T1ZML27OCX0kUQZwl794n%2F5MfjS41x0oh8yZrTppbuMvXQ%2F9gHV81Nj%2FOTa8vbvBu9KAkT%2FGFAoKmm5shL9s5r0w9sa5cT86OwOq9iEGxxOyokWIjet95XNfFK7rHyuvubgIDynOyjALm0ToSvrjhh6ddr8QrJ5WTIrgJ1J0WX7wmzreT1dEz339ptvDQJ%2BOJkwbA4gV32LBcMvvEydZWcDmgRXKcNG3Ti5KmYz0vYufJBNcHHhAQd1QqpGmG3yFfWUSWgKZdx7lyHu%2F7pNZhm7sKII0BCTZjB0O3bbyh5LNQN%2BcWrvlaBOrL45lvu8FrrgvCUKJBd4yShXLP%2FOvijztNb2StPEbRipBzAU00y6VfMwR2v2oAV1fnLENxPP58Ie%2Fw%2FrPrEjE933YPsj46IlQlxer7o5k2tyP7GdMgXcIeRTK7TsTCBXbJUpQ6Rc3HTdkDssVrcr%2BaLUHgl1SNCQBHROlB9pXiRckR60MYxzL12NW9gmKFkMOL877wGOqUB7PeAsV%2BaBTwCVpqx%2FtYaW40Ch%2BUcvWIksfC1E2zBp2cF7LbhJcOImobldlL986k%2B8rg0ovQwlDDLu0bvMpEq62vy%2BCyvi%2FZ4nNi5AyVTLX4kzTgQutsf3kPa1R78yeFw4Z1tmsx7DdxB3G9EJh5fFQYLm1I4hj1AXfvv3JCXtYei2UmBQ8kbVP8%2Fuc6a4cEwNXOqoWtE4kQVhPx3431plIedlxXS&X-Amz-Signature=75c9c311e1f0acb6eca9c8cec366553531d4193427942299faf1bb7677d70e49&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623376QA3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKfD%2FOQXt29azGBOTEABS%2BlEZGUY2V0V3EBS%2BK%2F4u9kAIgczPjlP09wt0UmfsfkT3CyRoPIUwk9vCBn7sg473KVUkqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3DCFwgWyNiz0ra4CrcAz3YC9xy3Smp5TgHfaKdAJ7G3SyP0Rw4L91Zbs1BUoerkVjXq%2BtnhOz0MvvDMi8haU6172PcvF7mxZxnnbj51sV7zA98UQW33bfb4UFK6qg1rjQ2FDAFxbt1g4HT%2BV2Mplffl1T1ZML27OCX0kUQZwl794n%2F5MfjS41x0oh8yZrTppbuMvXQ%2F9gHV81Nj%2FOTa8vbvBu9KAkT%2FGFAoKmm5shL9s5r0w9sa5cT86OwOq9iEGxxOyokWIjet95XNfFK7rHyuvubgIDynOyjALm0ToSvrjhh6ddr8QrJ5WTIrgJ1J0WX7wmzreT1dEz339ptvDQJ%2BOJkwbA4gV32LBcMvvEydZWcDmgRXKcNG3Ti5KmYz0vYufJBNcHHhAQd1QqpGmG3yFfWUSWgKZdx7lyHu%2F7pNZhm7sKII0BCTZjB0O3bbyh5LNQN%2BcWrvlaBOrL45lvu8FrrgvCUKJBd4yShXLP%2FOvijztNb2StPEbRipBzAU00y6VfMwR2v2oAV1fnLENxPP58Ie%2Fw%2FrPrEjE933YPsj46IlQlxer7o5k2tyP7GdMgXcIeRTK7TsTCBXbJUpQ6Rc3HTdkDssVrcr%2BaLUHgl1SNCQBHROlB9pXiRckR60MYxzL12NW9gmKFkMOL877wGOqUB7PeAsV%2BaBTwCVpqx%2FtYaW40Ch%2BUcvWIksfC1E2zBp2cF7LbhJcOImobldlL986k%2B8rg0ovQwlDDLu0bvMpEq62vy%2BCyvi%2FZ4nNi5AyVTLX4kzTgQutsf3kPa1R78yeFw4Z1tmsx7DdxB3G9EJh5fFQYLm1I4hj1AXfvv3JCXtYei2UmBQ8kbVP8%2Fuc6a4cEwNXOqoWtE4kQVhPx3431plIedlxXS&X-Amz-Signature=a820e26d815464c95aa0f18779d38ee9b678f7c47e711b794315755a9671147a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623376QA3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKfD%2FOQXt29azGBOTEABS%2BlEZGUY2V0V3EBS%2BK%2F4u9kAIgczPjlP09wt0UmfsfkT3CyRoPIUwk9vCBn7sg473KVUkqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3DCFwgWyNiz0ra4CrcAz3YC9xy3Smp5TgHfaKdAJ7G3SyP0Rw4L91Zbs1BUoerkVjXq%2BtnhOz0MvvDMi8haU6172PcvF7mxZxnnbj51sV7zA98UQW33bfb4UFK6qg1rjQ2FDAFxbt1g4HT%2BV2Mplffl1T1ZML27OCX0kUQZwl794n%2F5MfjS41x0oh8yZrTppbuMvXQ%2F9gHV81Nj%2FOTa8vbvBu9KAkT%2FGFAoKmm5shL9s5r0w9sa5cT86OwOq9iEGxxOyokWIjet95XNfFK7rHyuvubgIDynOyjALm0ToSvrjhh6ddr8QrJ5WTIrgJ1J0WX7wmzreT1dEz339ptvDQJ%2BOJkwbA4gV32LBcMvvEydZWcDmgRXKcNG3Ti5KmYz0vYufJBNcHHhAQd1QqpGmG3yFfWUSWgKZdx7lyHu%2F7pNZhm7sKII0BCTZjB0O3bbyh5LNQN%2BcWrvlaBOrL45lvu8FrrgvCUKJBd4yShXLP%2FOvijztNb2StPEbRipBzAU00y6VfMwR2v2oAV1fnLENxPP58Ie%2Fw%2FrPrEjE933YPsj46IlQlxer7o5k2tyP7GdMgXcIeRTK7TsTCBXbJUpQ6Rc3HTdkDssVrcr%2BaLUHgl1SNCQBHROlB9pXiRckR60MYxzL12NW9gmKFkMOL877wGOqUB7PeAsV%2BaBTwCVpqx%2FtYaW40Ch%2BUcvWIksfC1E2zBp2cF7LbhJcOImobldlL986k%2B8rg0ovQwlDDLu0bvMpEq62vy%2BCyvi%2FZ4nNi5AyVTLX4kzTgQutsf3kPa1R78yeFw4Z1tmsx7DdxB3G9EJh5fFQYLm1I4hj1AXfvv3JCXtYei2UmBQ8kbVP8%2Fuc6a4cEwNXOqoWtE4kQVhPx3431plIedlxXS&X-Amz-Signature=3c2bc01edf77fa9a08bb8a0ff7f9ab16598eb76314a3d7e1fb1edddf2988f120&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623376QA3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKfD%2FOQXt29azGBOTEABS%2BlEZGUY2V0V3EBS%2BK%2F4u9kAIgczPjlP09wt0UmfsfkT3CyRoPIUwk9vCBn7sg473KVUkqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3DCFwgWyNiz0ra4CrcAz3YC9xy3Smp5TgHfaKdAJ7G3SyP0Rw4L91Zbs1BUoerkVjXq%2BtnhOz0MvvDMi8haU6172PcvF7mxZxnnbj51sV7zA98UQW33bfb4UFK6qg1rjQ2FDAFxbt1g4HT%2BV2Mplffl1T1ZML27OCX0kUQZwl794n%2F5MfjS41x0oh8yZrTppbuMvXQ%2F9gHV81Nj%2FOTa8vbvBu9KAkT%2FGFAoKmm5shL9s5r0w9sa5cT86OwOq9iEGxxOyokWIjet95XNfFK7rHyuvubgIDynOyjALm0ToSvrjhh6ddr8QrJ5WTIrgJ1J0WX7wmzreT1dEz339ptvDQJ%2BOJkwbA4gV32LBcMvvEydZWcDmgRXKcNG3Ti5KmYz0vYufJBNcHHhAQd1QqpGmG3yFfWUSWgKZdx7lyHu%2F7pNZhm7sKII0BCTZjB0O3bbyh5LNQN%2BcWrvlaBOrL45lvu8FrrgvCUKJBd4yShXLP%2FOvijztNb2StPEbRipBzAU00y6VfMwR2v2oAV1fnLENxPP58Ie%2Fw%2FrPrEjE933YPsj46IlQlxer7o5k2tyP7GdMgXcIeRTK7TsTCBXbJUpQ6Rc3HTdkDssVrcr%2BaLUHgl1SNCQBHROlB9pXiRckR60MYxzL12NW9gmKFkMOL877wGOqUB7PeAsV%2BaBTwCVpqx%2FtYaW40Ch%2BUcvWIksfC1E2zBp2cF7LbhJcOImobldlL986k%2B8rg0ovQwlDDLu0bvMpEq62vy%2BCyvi%2FZ4nNi5AyVTLX4kzTgQutsf3kPa1R78yeFw4Z1tmsx7DdxB3G9EJh5fFQYLm1I4hj1AXfvv3JCXtYei2UmBQ8kbVP8%2Fuc6a4cEwNXOqoWtE4kQVhPx3431plIedlxXS&X-Amz-Signature=468557929520673a529a5d9c9d8f5c3ac61c5c2d3fc3e74fdd632d89c94f88fd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623376QA3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKfD%2FOQXt29azGBOTEABS%2BlEZGUY2V0V3EBS%2BK%2F4u9kAIgczPjlP09wt0UmfsfkT3CyRoPIUwk9vCBn7sg473KVUkqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3DCFwgWyNiz0ra4CrcAz3YC9xy3Smp5TgHfaKdAJ7G3SyP0Rw4L91Zbs1BUoerkVjXq%2BtnhOz0MvvDMi8haU6172PcvF7mxZxnnbj51sV7zA98UQW33bfb4UFK6qg1rjQ2FDAFxbt1g4HT%2BV2Mplffl1T1ZML27OCX0kUQZwl794n%2F5MfjS41x0oh8yZrTppbuMvXQ%2F9gHV81Nj%2FOTa8vbvBu9KAkT%2FGFAoKmm5shL9s5r0w9sa5cT86OwOq9iEGxxOyokWIjet95XNfFK7rHyuvubgIDynOyjALm0ToSvrjhh6ddr8QrJ5WTIrgJ1J0WX7wmzreT1dEz339ptvDQJ%2BOJkwbA4gV32LBcMvvEydZWcDmgRXKcNG3Ti5KmYz0vYufJBNcHHhAQd1QqpGmG3yFfWUSWgKZdx7lyHu%2F7pNZhm7sKII0BCTZjB0O3bbyh5LNQN%2BcWrvlaBOrL45lvu8FrrgvCUKJBd4yShXLP%2FOvijztNb2StPEbRipBzAU00y6VfMwR2v2oAV1fnLENxPP58Ie%2Fw%2FrPrEjE933YPsj46IlQlxer7o5k2tyP7GdMgXcIeRTK7TsTCBXbJUpQ6Rc3HTdkDssVrcr%2BaLUHgl1SNCQBHROlB9pXiRckR60MYxzL12NW9gmKFkMOL877wGOqUB7PeAsV%2BaBTwCVpqx%2FtYaW40Ch%2BUcvWIksfC1E2zBp2cF7LbhJcOImobldlL986k%2B8rg0ovQwlDDLu0bvMpEq62vy%2BCyvi%2FZ4nNi5AyVTLX4kzTgQutsf3kPa1R78yeFw4Z1tmsx7DdxB3G9EJh5fFQYLm1I4hj1AXfvv3JCXtYei2UmBQ8kbVP8%2Fuc6a4cEwNXOqoWtE4kQVhPx3431plIedlxXS&X-Amz-Signature=be4993ad0e08ce824b8c13a0115a8e9971d8712f0f3f1e889ef689d65e62c17b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623376QA3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKfD%2FOQXt29azGBOTEABS%2BlEZGUY2V0V3EBS%2BK%2F4u9kAIgczPjlP09wt0UmfsfkT3CyRoPIUwk9vCBn7sg473KVUkqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3DCFwgWyNiz0ra4CrcAz3YC9xy3Smp5TgHfaKdAJ7G3SyP0Rw4L91Zbs1BUoerkVjXq%2BtnhOz0MvvDMi8haU6172PcvF7mxZxnnbj51sV7zA98UQW33bfb4UFK6qg1rjQ2FDAFxbt1g4HT%2BV2Mplffl1T1ZML27OCX0kUQZwl794n%2F5MfjS41x0oh8yZrTppbuMvXQ%2F9gHV81Nj%2FOTa8vbvBu9KAkT%2FGFAoKmm5shL9s5r0w9sa5cT86OwOq9iEGxxOyokWIjet95XNfFK7rHyuvubgIDynOyjALm0ToSvrjhh6ddr8QrJ5WTIrgJ1J0WX7wmzreT1dEz339ptvDQJ%2BOJkwbA4gV32LBcMvvEydZWcDmgRXKcNG3Ti5KmYz0vYufJBNcHHhAQd1QqpGmG3yFfWUSWgKZdx7lyHu%2F7pNZhm7sKII0BCTZjB0O3bbyh5LNQN%2BcWrvlaBOrL45lvu8FrrgvCUKJBd4yShXLP%2FOvijztNb2StPEbRipBzAU00y6VfMwR2v2oAV1fnLENxPP58Ie%2Fw%2FrPrEjE933YPsj46IlQlxer7o5k2tyP7GdMgXcIeRTK7TsTCBXbJUpQ6Rc3HTdkDssVrcr%2BaLUHgl1SNCQBHROlB9pXiRckR60MYxzL12NW9gmKFkMOL877wGOqUB7PeAsV%2BaBTwCVpqx%2FtYaW40Ch%2BUcvWIksfC1E2zBp2cF7LbhJcOImobldlL986k%2B8rg0ovQwlDDLu0bvMpEq62vy%2BCyvi%2FZ4nNi5AyVTLX4kzTgQutsf3kPa1R78yeFw4Z1tmsx7DdxB3G9EJh5fFQYLm1I4hj1AXfvv3JCXtYei2UmBQ8kbVP8%2Fuc6a4cEwNXOqoWtE4kQVhPx3431plIedlxXS&X-Amz-Signature=bd9ac341c255cc1776bea058a9bbc87dbc454843d0333c365047859abe4ea44c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623376QA3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKfD%2FOQXt29azGBOTEABS%2BlEZGUY2V0V3EBS%2BK%2F4u9kAIgczPjlP09wt0UmfsfkT3CyRoPIUwk9vCBn7sg473KVUkqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3DCFwgWyNiz0ra4CrcAz3YC9xy3Smp5TgHfaKdAJ7G3SyP0Rw4L91Zbs1BUoerkVjXq%2BtnhOz0MvvDMi8haU6172PcvF7mxZxnnbj51sV7zA98UQW33bfb4UFK6qg1rjQ2FDAFxbt1g4HT%2BV2Mplffl1T1ZML27OCX0kUQZwl794n%2F5MfjS41x0oh8yZrTppbuMvXQ%2F9gHV81Nj%2FOTa8vbvBu9KAkT%2FGFAoKmm5shL9s5r0w9sa5cT86OwOq9iEGxxOyokWIjet95XNfFK7rHyuvubgIDynOyjALm0ToSvrjhh6ddr8QrJ5WTIrgJ1J0WX7wmzreT1dEz339ptvDQJ%2BOJkwbA4gV32LBcMvvEydZWcDmgRXKcNG3Ti5KmYz0vYufJBNcHHhAQd1QqpGmG3yFfWUSWgKZdx7lyHu%2F7pNZhm7sKII0BCTZjB0O3bbyh5LNQN%2BcWrvlaBOrL45lvu8FrrgvCUKJBd4yShXLP%2FOvijztNb2StPEbRipBzAU00y6VfMwR2v2oAV1fnLENxPP58Ie%2Fw%2FrPrEjE933YPsj46IlQlxer7o5k2tyP7GdMgXcIeRTK7TsTCBXbJUpQ6Rc3HTdkDssVrcr%2BaLUHgl1SNCQBHROlB9pXiRckR60MYxzL12NW9gmKFkMOL877wGOqUB7PeAsV%2BaBTwCVpqx%2FtYaW40Ch%2BUcvWIksfC1E2zBp2cF7LbhJcOImobldlL986k%2B8rg0ovQwlDDLu0bvMpEq62vy%2BCyvi%2FZ4nNi5AyVTLX4kzTgQutsf3kPa1R78yeFw4Z1tmsx7DdxB3G9EJh5fFQYLm1I4hj1AXfvv3JCXtYei2UmBQ8kbVP8%2Fuc6a4cEwNXOqoWtE4kQVhPx3431plIedlxXS&X-Amz-Signature=96e376e7b11e4fbbfd01762ecc9cdd71d88c38257ad8928497a3611c0c7e8c21&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637IC6LSX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGZVvzeHUDc4oI5Z9geLY7N1lDTfJc2m0Xhskqn2lICOAiEApcUugNm6NOWS5l7yrNL5E%2B921H0ZtZ5pHn2Xx%2BWboH0qiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIfao6Uj5eLODy1GWSrcA1D%2BBs0%2FsQgjriyN8kBAOItlC7VtspFf3n%2F4b0WX0O1Bf2rSsMo%2FGyp%2Bdpem5RvGNhyDGIGX0oeSZLbCgW1ctbOR2i6pdQ3UYp1FuSu29aO6dyoQ3BgR9rPNqn5fAgRT5zHVTRSZT8hAnkYY0gaWpWHEj%2FpPHExRXEjo8CmFV2XpcZjPMOpt2i5fPpzVBvNmYsAkFChHSyK282EjiFfArR7UiFTUykKaoK2PGKAUPwpLPkdGAjNy11lk7jb7H1Napk%2Bv%2B8qa%2Fce0oEx1fkoFOtzS84mbxgHPEoXAY%2Bf2GPXuvSKM%2FmG5CI9ADH9Xwh5RMO9dr%2BfWZ%2FY8glNKwxvm9vbkURaMkP1DaGxZAYNOTlLN8XrWOEGrwQ%2BHeD9KOi7UampOUsy8tdJbEp%2BRkFeYgEMZP8Bj0%2ByimYAq2mp5%2BkGN%2Fmbj0UKohTY17VZ8QQeVb15BoaVbNlRawyjcKFuqZBwOBOi9InJ8BkJf5g5RjiANld2zu6CdjtaEiUa7KuDTi%2FI6elsJzReaY2Kn5Hn0IVH%2FWVynSMX%2Bw5sY4z0New0vOKauzZx98Vcy0eNLsnrrclegpbIdWX73gpgg5f%2Fh9ujpOAnBwWD4g4nDFHVviRlxYdjVuLG1oAQgVlBPMJ3977wGOqUBqtM9eddwThQr3YH07TfNLTEdEmszOFowSm6qPaKpJucA4djdNqyZeU84ZX963hoTsNAdnUSaOwR%2FJyanp5TO6fAIr0M4yU5dVZHkW6D7Uf8spyRFr%2Bi5oWXiZnV0yhJkCRKcQJi%2Bd5DX8Y6%2Fof6dWk5a5nM5%2B0YRl4flztbvHdnPLUaUtudzhqvRMavJlE9FbgxsYiABGm01Kl2KWzl%2F%2BHg6CRsr&X-Amz-Signature=cfe03040d2cdd685b5ced37fbf570bb4a4016f08c3ac0a052e975ee73ba200b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637IC6LSX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGZVvzeHUDc4oI5Z9geLY7N1lDTfJc2m0Xhskqn2lICOAiEApcUugNm6NOWS5l7yrNL5E%2B921H0ZtZ5pHn2Xx%2BWboH0qiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIfao6Uj5eLODy1GWSrcA1D%2BBs0%2FsQgjriyN8kBAOItlC7VtspFf3n%2F4b0WX0O1Bf2rSsMo%2FGyp%2Bdpem5RvGNhyDGIGX0oeSZLbCgW1ctbOR2i6pdQ3UYp1FuSu29aO6dyoQ3BgR9rPNqn5fAgRT5zHVTRSZT8hAnkYY0gaWpWHEj%2FpPHExRXEjo8CmFV2XpcZjPMOpt2i5fPpzVBvNmYsAkFChHSyK282EjiFfArR7UiFTUykKaoK2PGKAUPwpLPkdGAjNy11lk7jb7H1Napk%2Bv%2B8qa%2Fce0oEx1fkoFOtzS84mbxgHPEoXAY%2Bf2GPXuvSKM%2FmG5CI9ADH9Xwh5RMO9dr%2BfWZ%2FY8glNKwxvm9vbkURaMkP1DaGxZAYNOTlLN8XrWOEGrwQ%2BHeD9KOi7UampOUsy8tdJbEp%2BRkFeYgEMZP8Bj0%2ByimYAq2mp5%2BkGN%2Fmbj0UKohTY17VZ8QQeVb15BoaVbNlRawyjcKFuqZBwOBOi9InJ8BkJf5g5RjiANld2zu6CdjtaEiUa7KuDTi%2FI6elsJzReaY2Kn5Hn0IVH%2FWVynSMX%2Bw5sY4z0New0vOKauzZx98Vcy0eNLsnrrclegpbIdWX73gpgg5f%2Fh9ujpOAnBwWD4g4nDFHVviRlxYdjVuLG1oAQgVlBPMJ3977wGOqUBqtM9eddwThQr3YH07TfNLTEdEmszOFowSm6qPaKpJucA4djdNqyZeU84ZX963hoTsNAdnUSaOwR%2FJyanp5TO6fAIr0M4yU5dVZHkW6D7Uf8spyRFr%2Bi5oWXiZnV0yhJkCRKcQJi%2Bd5DX8Y6%2Fof6dWk5a5nM5%2B0YRl4flztbvHdnPLUaUtudzhqvRMavJlE9FbgxsYiABGm01Kl2KWzl%2F%2BHg6CRsr&X-Amz-Signature=6dd2b851ed71b82e80a0e4cda080b5080937837ac2c11830abd878b52c85e36e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
