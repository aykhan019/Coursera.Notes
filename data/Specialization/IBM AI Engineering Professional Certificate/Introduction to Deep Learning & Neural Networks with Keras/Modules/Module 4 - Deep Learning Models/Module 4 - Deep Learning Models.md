

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIF7PV3T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICvNEwUaS5AwGXyZguOOhYckkH%2B2OiX73ZICV8ES0XIiAiBGKKCCvt9JgZGcNQBjPd%2BfvWA71%2FsoYNrVkzgZ3LoOySqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzl9Qm8tmL%2BimYzWhKtwD%2BUGvG6aq8wHFu8NHG1gvOHJZwnqgUb9B48nTNqEeK%2B6YpDrakZl7sWZ923%2FTd0yZsj8H8Db3BpyYLAzY0b%2BMtwUH7bdvFGle8n%2Fm28AgFOnOcfA7KazaUzshMT4R9O1p0CSjpvH6Sc%2BptV2tljc1VZuBtpTWfNOun%2FttIkp5ooRf7%2F9eV0n%2Fo9MEaijX4nwIv9TB6b8rAGTrmEy%2F797FdXnKyhVMix4ntliNyX9xs1ShRGH65CuJHGaWK87LT9PQl%2FrGEL1okX4ioBhn4W%2FnKghuOwVBDyX64Oh3FAtGQZ5wZSJJUJ3F%2Bv%2BhlO32%2FJbEj8MAe3l45HR1MMaUO0p0OWURLTcMHEU8JydeEvWU7s9fNqI543oMXunejKZ0bFoXoN281VtoClDNQE3cjcQE7et59%2BoS6bCoqJVmw8oMCAMP8KTiR3Xxc5ry%2BoXxc9pkFvNuz%2B9usXdEFhTP1gpB4ZkZKezmp%2BrUUx7OwkX9WxDX%2FPhqepCL4R%2FBKtUZ%2Fymkt7TO8ovK0HCKB34SMRse4aUMbMdqowwZgSOoibs7bW%2BA4VwuwYtkZUx1sgnrUypB79Db7IV3416Wkmzs3EwIxjUEDDFm7L6r7G4GMHmHbYzDjSNi8ZGhHhK5dZUw%2B9byvAY6pgFsiKU9TZobi3hhlCMH7Mo90R%2F1WOasEb2DNckwPYI3UmQil2VLm66A0zu17QJ2g%2Bkc4A%2BniRUGiZbdRWYPprtC4JM6jrC1F%2BIM%2BdEYXWxqZvXnGi6VJbSQA6XQXEe65QN1yKoIZDARf%2FMy3MtoTe0ef9D4cvbposFjUhbkjteDmMdYCPWnc07o%2F8LMqH9c3NjI2YxUvZv5NtusdyOQN53fSGTa312X&X-Amz-Signature=6d097e9e9475da102ce2f43bcad1affe5bf2487ba4c8838e36928123fbb60a75&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIF7PV3T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICvNEwUaS5AwGXyZguOOhYckkH%2B2OiX73ZICV8ES0XIiAiBGKKCCvt9JgZGcNQBjPd%2BfvWA71%2FsoYNrVkzgZ3LoOySqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzl9Qm8tmL%2BimYzWhKtwD%2BUGvG6aq8wHFu8NHG1gvOHJZwnqgUb9B48nTNqEeK%2B6YpDrakZl7sWZ923%2FTd0yZsj8H8Db3BpyYLAzY0b%2BMtwUH7bdvFGle8n%2Fm28AgFOnOcfA7KazaUzshMT4R9O1p0CSjpvH6Sc%2BptV2tljc1VZuBtpTWfNOun%2FttIkp5ooRf7%2F9eV0n%2Fo9MEaijX4nwIv9TB6b8rAGTrmEy%2F797FdXnKyhVMix4ntliNyX9xs1ShRGH65CuJHGaWK87LT9PQl%2FrGEL1okX4ioBhn4W%2FnKghuOwVBDyX64Oh3FAtGQZ5wZSJJUJ3F%2Bv%2BhlO32%2FJbEj8MAe3l45HR1MMaUO0p0OWURLTcMHEU8JydeEvWU7s9fNqI543oMXunejKZ0bFoXoN281VtoClDNQE3cjcQE7et59%2BoS6bCoqJVmw8oMCAMP8KTiR3Xxc5ry%2BoXxc9pkFvNuz%2B9usXdEFhTP1gpB4ZkZKezmp%2BrUUx7OwkX9WxDX%2FPhqepCL4R%2FBKtUZ%2Fymkt7TO8ovK0HCKB34SMRse4aUMbMdqowwZgSOoibs7bW%2BA4VwuwYtkZUx1sgnrUypB79Db7IV3416Wkmzs3EwIxjUEDDFm7L6r7G4GMHmHbYzDjSNi8ZGhHhK5dZUw%2B9byvAY6pgFsiKU9TZobi3hhlCMH7Mo90R%2F1WOasEb2DNckwPYI3UmQil2VLm66A0zu17QJ2g%2Bkc4A%2BniRUGiZbdRWYPprtC4JM6jrC1F%2BIM%2BdEYXWxqZvXnGi6VJbSQA6XQXEe65QN1yKoIZDARf%2FMy3MtoTe0ef9D4cvbposFjUhbkjteDmMdYCPWnc07o%2F8LMqH9c3NjI2YxUvZv5NtusdyOQN53fSGTa312X&X-Amz-Signature=37786285c640e3d398e92409611f72f5ac9a70ebac1a21fd6039947299d656cd&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIF7PV3T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICvNEwUaS5AwGXyZguOOhYckkH%2B2OiX73ZICV8ES0XIiAiBGKKCCvt9JgZGcNQBjPd%2BfvWA71%2FsoYNrVkzgZ3LoOySqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzl9Qm8tmL%2BimYzWhKtwD%2BUGvG6aq8wHFu8NHG1gvOHJZwnqgUb9B48nTNqEeK%2B6YpDrakZl7sWZ923%2FTd0yZsj8H8Db3BpyYLAzY0b%2BMtwUH7bdvFGle8n%2Fm28AgFOnOcfA7KazaUzshMT4R9O1p0CSjpvH6Sc%2BptV2tljc1VZuBtpTWfNOun%2FttIkp5ooRf7%2F9eV0n%2Fo9MEaijX4nwIv9TB6b8rAGTrmEy%2F797FdXnKyhVMix4ntliNyX9xs1ShRGH65CuJHGaWK87LT9PQl%2FrGEL1okX4ioBhn4W%2FnKghuOwVBDyX64Oh3FAtGQZ5wZSJJUJ3F%2Bv%2BhlO32%2FJbEj8MAe3l45HR1MMaUO0p0OWURLTcMHEU8JydeEvWU7s9fNqI543oMXunejKZ0bFoXoN281VtoClDNQE3cjcQE7et59%2BoS6bCoqJVmw8oMCAMP8KTiR3Xxc5ry%2BoXxc9pkFvNuz%2B9usXdEFhTP1gpB4ZkZKezmp%2BrUUx7OwkX9WxDX%2FPhqepCL4R%2FBKtUZ%2Fymkt7TO8ovK0HCKB34SMRse4aUMbMdqowwZgSOoibs7bW%2BA4VwuwYtkZUx1sgnrUypB79Db7IV3416Wkmzs3EwIxjUEDDFm7L6r7G4GMHmHbYzDjSNi8ZGhHhK5dZUw%2B9byvAY6pgFsiKU9TZobi3hhlCMH7Mo90R%2F1WOasEb2DNckwPYI3UmQil2VLm66A0zu17QJ2g%2Bkc4A%2BniRUGiZbdRWYPprtC4JM6jrC1F%2BIM%2BdEYXWxqZvXnGi6VJbSQA6XQXEe65QN1yKoIZDARf%2FMy3MtoTe0ef9D4cvbposFjUhbkjteDmMdYCPWnc07o%2F8LMqH9c3NjI2YxUvZv5NtusdyOQN53fSGTa312X&X-Amz-Signature=46223ed516107b500780d1de89ccb81125b8e72a8ee69bd753840cb5b3e2abba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIF7PV3T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICvNEwUaS5AwGXyZguOOhYckkH%2B2OiX73ZICV8ES0XIiAiBGKKCCvt9JgZGcNQBjPd%2BfvWA71%2FsoYNrVkzgZ3LoOySqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzl9Qm8tmL%2BimYzWhKtwD%2BUGvG6aq8wHFu8NHG1gvOHJZwnqgUb9B48nTNqEeK%2B6YpDrakZl7sWZ923%2FTd0yZsj8H8Db3BpyYLAzY0b%2BMtwUH7bdvFGle8n%2Fm28AgFOnOcfA7KazaUzshMT4R9O1p0CSjpvH6Sc%2BptV2tljc1VZuBtpTWfNOun%2FttIkp5ooRf7%2F9eV0n%2Fo9MEaijX4nwIv9TB6b8rAGTrmEy%2F797FdXnKyhVMix4ntliNyX9xs1ShRGH65CuJHGaWK87LT9PQl%2FrGEL1okX4ioBhn4W%2FnKghuOwVBDyX64Oh3FAtGQZ5wZSJJUJ3F%2Bv%2BhlO32%2FJbEj8MAe3l45HR1MMaUO0p0OWURLTcMHEU8JydeEvWU7s9fNqI543oMXunejKZ0bFoXoN281VtoClDNQE3cjcQE7et59%2BoS6bCoqJVmw8oMCAMP8KTiR3Xxc5ry%2BoXxc9pkFvNuz%2B9usXdEFhTP1gpB4ZkZKezmp%2BrUUx7OwkX9WxDX%2FPhqepCL4R%2FBKtUZ%2Fymkt7TO8ovK0HCKB34SMRse4aUMbMdqowwZgSOoibs7bW%2BA4VwuwYtkZUx1sgnrUypB79Db7IV3416Wkmzs3EwIxjUEDDFm7L6r7G4GMHmHbYzDjSNi8ZGhHhK5dZUw%2B9byvAY6pgFsiKU9TZobi3hhlCMH7Mo90R%2F1WOasEb2DNckwPYI3UmQil2VLm66A0zu17QJ2g%2Bkc4A%2BniRUGiZbdRWYPprtC4JM6jrC1F%2BIM%2BdEYXWxqZvXnGi6VJbSQA6XQXEe65QN1yKoIZDARf%2FMy3MtoTe0ef9D4cvbposFjUhbkjteDmMdYCPWnc07o%2F8LMqH9c3NjI2YxUvZv5NtusdyOQN53fSGTa312X&X-Amz-Signature=0ff1ed404962685361caa71748d007f3c3493b441626f1d47faadca82055dc00&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIF7PV3T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICvNEwUaS5AwGXyZguOOhYckkH%2B2OiX73ZICV8ES0XIiAiBGKKCCvt9JgZGcNQBjPd%2BfvWA71%2FsoYNrVkzgZ3LoOySqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzl9Qm8tmL%2BimYzWhKtwD%2BUGvG6aq8wHFu8NHG1gvOHJZwnqgUb9B48nTNqEeK%2B6YpDrakZl7sWZ923%2FTd0yZsj8H8Db3BpyYLAzY0b%2BMtwUH7bdvFGle8n%2Fm28AgFOnOcfA7KazaUzshMT4R9O1p0CSjpvH6Sc%2BptV2tljc1VZuBtpTWfNOun%2FttIkp5ooRf7%2F9eV0n%2Fo9MEaijX4nwIv9TB6b8rAGTrmEy%2F797FdXnKyhVMix4ntliNyX9xs1ShRGH65CuJHGaWK87LT9PQl%2FrGEL1okX4ioBhn4W%2FnKghuOwVBDyX64Oh3FAtGQZ5wZSJJUJ3F%2Bv%2BhlO32%2FJbEj8MAe3l45HR1MMaUO0p0OWURLTcMHEU8JydeEvWU7s9fNqI543oMXunejKZ0bFoXoN281VtoClDNQE3cjcQE7et59%2BoS6bCoqJVmw8oMCAMP8KTiR3Xxc5ry%2BoXxc9pkFvNuz%2B9usXdEFhTP1gpB4ZkZKezmp%2BrUUx7OwkX9WxDX%2FPhqepCL4R%2FBKtUZ%2Fymkt7TO8ovK0HCKB34SMRse4aUMbMdqowwZgSOoibs7bW%2BA4VwuwYtkZUx1sgnrUypB79Db7IV3416Wkmzs3EwIxjUEDDFm7L6r7G4GMHmHbYzDjSNi8ZGhHhK5dZUw%2B9byvAY6pgFsiKU9TZobi3hhlCMH7Mo90R%2F1WOasEb2DNckwPYI3UmQil2VLm66A0zu17QJ2g%2Bkc4A%2BniRUGiZbdRWYPprtC4JM6jrC1F%2BIM%2BdEYXWxqZvXnGi6VJbSQA6XQXEe65QN1yKoIZDARf%2FMy3MtoTe0ef9D4cvbposFjUhbkjteDmMdYCPWnc07o%2F8LMqH9c3NjI2YxUvZv5NtusdyOQN53fSGTa312X&X-Amz-Signature=22da014a494d1027b61736623e52ecfe84dd433fcc91f17c6642ace5597e10b7&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIF7PV3T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICvNEwUaS5AwGXyZguOOhYckkH%2B2OiX73ZICV8ES0XIiAiBGKKCCvt9JgZGcNQBjPd%2BfvWA71%2FsoYNrVkzgZ3LoOySqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzl9Qm8tmL%2BimYzWhKtwD%2BUGvG6aq8wHFu8NHG1gvOHJZwnqgUb9B48nTNqEeK%2B6YpDrakZl7sWZ923%2FTd0yZsj8H8Db3BpyYLAzY0b%2BMtwUH7bdvFGle8n%2Fm28AgFOnOcfA7KazaUzshMT4R9O1p0CSjpvH6Sc%2BptV2tljc1VZuBtpTWfNOun%2FttIkp5ooRf7%2F9eV0n%2Fo9MEaijX4nwIv9TB6b8rAGTrmEy%2F797FdXnKyhVMix4ntliNyX9xs1ShRGH65CuJHGaWK87LT9PQl%2FrGEL1okX4ioBhn4W%2FnKghuOwVBDyX64Oh3FAtGQZ5wZSJJUJ3F%2Bv%2BhlO32%2FJbEj8MAe3l45HR1MMaUO0p0OWURLTcMHEU8JydeEvWU7s9fNqI543oMXunejKZ0bFoXoN281VtoClDNQE3cjcQE7et59%2BoS6bCoqJVmw8oMCAMP8KTiR3Xxc5ry%2BoXxc9pkFvNuz%2B9usXdEFhTP1gpB4ZkZKezmp%2BrUUx7OwkX9WxDX%2FPhqepCL4R%2FBKtUZ%2Fymkt7TO8ovK0HCKB34SMRse4aUMbMdqowwZgSOoibs7bW%2BA4VwuwYtkZUx1sgnrUypB79Db7IV3416Wkmzs3EwIxjUEDDFm7L6r7G4GMHmHbYzDjSNi8ZGhHhK5dZUw%2B9byvAY6pgFsiKU9TZobi3hhlCMH7Mo90R%2F1WOasEb2DNckwPYI3UmQil2VLm66A0zu17QJ2g%2Bkc4A%2BniRUGiZbdRWYPprtC4JM6jrC1F%2BIM%2BdEYXWxqZvXnGi6VJbSQA6XQXEe65QN1yKoIZDARf%2FMy3MtoTe0ef9D4cvbposFjUhbkjteDmMdYCPWnc07o%2F8LMqH9c3NjI2YxUvZv5NtusdyOQN53fSGTa312X&X-Amz-Signature=cc75d31e635ae26617d4e9c619597af0c67963315ea39b41688d0addd8d9c324&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIF7PV3T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICvNEwUaS5AwGXyZguOOhYckkH%2B2OiX73ZICV8ES0XIiAiBGKKCCvt9JgZGcNQBjPd%2BfvWA71%2FsoYNrVkzgZ3LoOySqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzl9Qm8tmL%2BimYzWhKtwD%2BUGvG6aq8wHFu8NHG1gvOHJZwnqgUb9B48nTNqEeK%2B6YpDrakZl7sWZ923%2FTd0yZsj8H8Db3BpyYLAzY0b%2BMtwUH7bdvFGle8n%2Fm28AgFOnOcfA7KazaUzshMT4R9O1p0CSjpvH6Sc%2BptV2tljc1VZuBtpTWfNOun%2FttIkp5ooRf7%2F9eV0n%2Fo9MEaijX4nwIv9TB6b8rAGTrmEy%2F797FdXnKyhVMix4ntliNyX9xs1ShRGH65CuJHGaWK87LT9PQl%2FrGEL1okX4ioBhn4W%2FnKghuOwVBDyX64Oh3FAtGQZ5wZSJJUJ3F%2Bv%2BhlO32%2FJbEj8MAe3l45HR1MMaUO0p0OWURLTcMHEU8JydeEvWU7s9fNqI543oMXunejKZ0bFoXoN281VtoClDNQE3cjcQE7et59%2BoS6bCoqJVmw8oMCAMP8KTiR3Xxc5ry%2BoXxc9pkFvNuz%2B9usXdEFhTP1gpB4ZkZKezmp%2BrUUx7OwkX9WxDX%2FPhqepCL4R%2FBKtUZ%2Fymkt7TO8ovK0HCKB34SMRse4aUMbMdqowwZgSOoibs7bW%2BA4VwuwYtkZUx1sgnrUypB79Db7IV3416Wkmzs3EwIxjUEDDFm7L6r7G4GMHmHbYzDjSNi8ZGhHhK5dZUw%2B9byvAY6pgFsiKU9TZobi3hhlCMH7Mo90R%2F1WOasEb2DNckwPYI3UmQil2VLm66A0zu17QJ2g%2Bkc4A%2BniRUGiZbdRWYPprtC4JM6jrC1F%2BIM%2BdEYXWxqZvXnGi6VJbSQA6XQXEe65QN1yKoIZDARf%2FMy3MtoTe0ef9D4cvbposFjUhbkjteDmMdYCPWnc07o%2F8LMqH9c3NjI2YxUvZv5NtusdyOQN53fSGTa312X&X-Amz-Signature=32daa1c8c3d85c516d0b8b106777f6dc14755d7d04e93f8854551de96b412bc3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIF7PV3T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICvNEwUaS5AwGXyZguOOhYckkH%2B2OiX73ZICV8ES0XIiAiBGKKCCvt9JgZGcNQBjPd%2BfvWA71%2FsoYNrVkzgZ3LoOySqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzl9Qm8tmL%2BimYzWhKtwD%2BUGvG6aq8wHFu8NHG1gvOHJZwnqgUb9B48nTNqEeK%2B6YpDrakZl7sWZ923%2FTd0yZsj8H8Db3BpyYLAzY0b%2BMtwUH7bdvFGle8n%2Fm28AgFOnOcfA7KazaUzshMT4R9O1p0CSjpvH6Sc%2BptV2tljc1VZuBtpTWfNOun%2FttIkp5ooRf7%2F9eV0n%2Fo9MEaijX4nwIv9TB6b8rAGTrmEy%2F797FdXnKyhVMix4ntliNyX9xs1ShRGH65CuJHGaWK87LT9PQl%2FrGEL1okX4ioBhn4W%2FnKghuOwVBDyX64Oh3FAtGQZ5wZSJJUJ3F%2Bv%2BhlO32%2FJbEj8MAe3l45HR1MMaUO0p0OWURLTcMHEU8JydeEvWU7s9fNqI543oMXunejKZ0bFoXoN281VtoClDNQE3cjcQE7et59%2BoS6bCoqJVmw8oMCAMP8KTiR3Xxc5ry%2BoXxc9pkFvNuz%2B9usXdEFhTP1gpB4ZkZKezmp%2BrUUx7OwkX9WxDX%2FPhqepCL4R%2FBKtUZ%2Fymkt7TO8ovK0HCKB34SMRse4aUMbMdqowwZgSOoibs7bW%2BA4VwuwYtkZUx1sgnrUypB79Db7IV3416Wkmzs3EwIxjUEDDFm7L6r7G4GMHmHbYzDjSNi8ZGhHhK5dZUw%2B9byvAY6pgFsiKU9TZobi3hhlCMH7Mo90R%2F1WOasEb2DNckwPYI3UmQil2VLm66A0zu17QJ2g%2Bkc4A%2BniRUGiZbdRWYPprtC4JM6jrC1F%2BIM%2BdEYXWxqZvXnGi6VJbSQA6XQXEe65QN1yKoIZDARf%2FMy3MtoTe0ef9D4cvbposFjUhbkjteDmMdYCPWnc07o%2F8LMqH9c3NjI2YxUvZv5NtusdyOQN53fSGTa312X&X-Amz-Signature=942b7a7cbab54b1d7bb35a38f0425b3bf56541521b1fb485385cfbd631dcb1f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIF7PV3T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICvNEwUaS5AwGXyZguOOhYckkH%2B2OiX73ZICV8ES0XIiAiBGKKCCvt9JgZGcNQBjPd%2BfvWA71%2FsoYNrVkzgZ3LoOySqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzl9Qm8tmL%2BimYzWhKtwD%2BUGvG6aq8wHFu8NHG1gvOHJZwnqgUb9B48nTNqEeK%2B6YpDrakZl7sWZ923%2FTd0yZsj8H8Db3BpyYLAzY0b%2BMtwUH7bdvFGle8n%2Fm28AgFOnOcfA7KazaUzshMT4R9O1p0CSjpvH6Sc%2BptV2tljc1VZuBtpTWfNOun%2FttIkp5ooRf7%2F9eV0n%2Fo9MEaijX4nwIv9TB6b8rAGTrmEy%2F797FdXnKyhVMix4ntliNyX9xs1ShRGH65CuJHGaWK87LT9PQl%2FrGEL1okX4ioBhn4W%2FnKghuOwVBDyX64Oh3FAtGQZ5wZSJJUJ3F%2Bv%2BhlO32%2FJbEj8MAe3l45HR1MMaUO0p0OWURLTcMHEU8JydeEvWU7s9fNqI543oMXunejKZ0bFoXoN281VtoClDNQE3cjcQE7et59%2BoS6bCoqJVmw8oMCAMP8KTiR3Xxc5ry%2BoXxc9pkFvNuz%2B9usXdEFhTP1gpB4ZkZKezmp%2BrUUx7OwkX9WxDX%2FPhqepCL4R%2FBKtUZ%2Fymkt7TO8ovK0HCKB34SMRse4aUMbMdqowwZgSOoibs7bW%2BA4VwuwYtkZUx1sgnrUypB79Db7IV3416Wkmzs3EwIxjUEDDFm7L6r7G4GMHmHbYzDjSNi8ZGhHhK5dZUw%2B9byvAY6pgFsiKU9TZobi3hhlCMH7Mo90R%2F1WOasEb2DNckwPYI3UmQil2VLm66A0zu17QJ2g%2Bkc4A%2BniRUGiZbdRWYPprtC4JM6jrC1F%2BIM%2BdEYXWxqZvXnGi6VJbSQA6XQXEe65QN1yKoIZDARf%2FMy3MtoTe0ef9D4cvbposFjUhbkjteDmMdYCPWnc07o%2F8LMqH9c3NjI2YxUvZv5NtusdyOQN53fSGTa312X&X-Amz-Signature=67bfe76365397808e77ddde9c18b7c6f8ace990cb6ebee52056710eaf951a479&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666XTPRLQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICGtd4Pmo102iKjnZEcHC%2FaqwkZWS58w5qDCQZSVSHl0AiAdDVwvCtRvztOdshiYiIlxJeGsahLv11jXwOdtzIzTQSqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FeolDn49JwDKYnIsKtwD6xuUoq278IL5MRsXb6j4fHSWjIHunH%2Fd7wnAg3fnzWzUD9WUkmCLqg0tHBFbXGEJbKda%2Bj69%2F2ZAe5pcilSlRiFzU1AkRF%2BrRtx7vo8XldGNUZOvcpGDjlWFQOJsH00KPI31YksU4r1c1ZB6hWV86d9ocJWmOa%2BOHmm5Zt21tBHGoSePuTSwXoDfMI5M0rgaa4U6ZuNtK74rGrfRWc7q33xXuP3yFPMtOzbYFvBinGPhLG0KdApbK2veazHJ557hfQtpDz5GdIgqjGZrE5MtzLAjulbSKYhrJAX6QBOLIuTWNlazC%2BA62of1Rf%2B9M%2BLrzL6IbVTyIcF9erBwy5c3WppGBjAXUItgHzNPFCgbjjwEJhwYDaN%2FPbRXbnCJEvzOv65KY9LW56J4V8X%2FmE5QKMJUyA7vvaQpX1tmvsj98jw9Hhg3NSGcv3NzsylvcmF7qD3KI%2FlGv3Xq7tW11okcLeARCqXPhoJxR1Ot7%2B4BFd2t0sUzln4zP%2BM%2Bn6RnuqfJ43bFQz4wZWYt0ahM%2Be1GaovXBUijrqAwQo1djXxxKVFXJYbXMAJF2ih3FSyMY8Msfsu9THCSw%2B88umdEdQ3B7sh2IzsX1YVFdrD87c%2Bd%2Fc8DfZEtvuP4jWNfG%2F4wldfyvAY6pgH98HIhKLLT2rqxujq7UdW2v2bTAYVSXXs5maHdHjaQT2jjQzfnNTmx1CQiiR9URUx4JK9cc23WBdj8ILiZ0%2B89D%2BDEPKb0daxMmfm1xZAUm%2Bs6AGDY4EQTMjGxKdBftEDhZV7NKe53KDqbJPKBn4nnk4ZUjYiydwrgDOxkUndmxtlu4aGS9MPPzfNK0VB8U46dusItQRWfQDUFXVDBnJKCwLCBTFCo&X-Amz-Signature=463f21bf4c70d299d1647f8ca34d302cb142ed09398b1d7a919ce2bd256d596e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666XTPRLQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICGtd4Pmo102iKjnZEcHC%2FaqwkZWS58w5qDCQZSVSHl0AiAdDVwvCtRvztOdshiYiIlxJeGsahLv11jXwOdtzIzTQSqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FeolDn49JwDKYnIsKtwD6xuUoq278IL5MRsXb6j4fHSWjIHunH%2Fd7wnAg3fnzWzUD9WUkmCLqg0tHBFbXGEJbKda%2Bj69%2F2ZAe5pcilSlRiFzU1AkRF%2BrRtx7vo8XldGNUZOvcpGDjlWFQOJsH00KPI31YksU4r1c1ZB6hWV86d9ocJWmOa%2BOHmm5Zt21tBHGoSePuTSwXoDfMI5M0rgaa4U6ZuNtK74rGrfRWc7q33xXuP3yFPMtOzbYFvBinGPhLG0KdApbK2veazHJ557hfQtpDz5GdIgqjGZrE5MtzLAjulbSKYhrJAX6QBOLIuTWNlazC%2BA62of1Rf%2B9M%2BLrzL6IbVTyIcF9erBwy5c3WppGBjAXUItgHzNPFCgbjjwEJhwYDaN%2FPbRXbnCJEvzOv65KY9LW56J4V8X%2FmE5QKMJUyA7vvaQpX1tmvsj98jw9Hhg3NSGcv3NzsylvcmF7qD3KI%2FlGv3Xq7tW11okcLeARCqXPhoJxR1Ot7%2B4BFd2t0sUzln4zP%2BM%2Bn6RnuqfJ43bFQz4wZWYt0ahM%2Be1GaovXBUijrqAwQo1djXxxKVFXJYbXMAJF2ih3FSyMY8Msfsu9THCSw%2B88umdEdQ3B7sh2IzsX1YVFdrD87c%2Bd%2Fc8DfZEtvuP4jWNfG%2F4wldfyvAY6pgH98HIhKLLT2rqxujq7UdW2v2bTAYVSXXs5maHdHjaQT2jjQzfnNTmx1CQiiR9URUx4JK9cc23WBdj8ILiZ0%2B89D%2BDEPKb0daxMmfm1xZAUm%2Bs6AGDY4EQTMjGxKdBftEDhZV7NKe53KDqbJPKBn4nnk4ZUjYiydwrgDOxkUndmxtlu4aGS9MPPzfNK0VB8U46dusItQRWfQDUFXVDBnJKCwLCBTFCo&X-Amz-Signature=8b827ec670d811ebfca1368e58b18d00a484293cc705b0ce9c9586105313174a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
