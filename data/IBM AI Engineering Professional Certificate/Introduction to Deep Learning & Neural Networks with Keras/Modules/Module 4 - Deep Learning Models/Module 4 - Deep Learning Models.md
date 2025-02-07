

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXVXAK3B%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCbflhbdvfNiasx2eGPczSXQ63h83tUd%2Bzwlo3am%2BTS1wIhAMNw5VVjWEHEw%2BhLfk7TtGgsXmTVuy9JqcEBLfDzT1Z%2BKv8DCH0QABoMNjM3NDIzMTgzODA1IgxOwzMkIdUKECGvOYYq3ANRK7Y174o7avwqUSEoqjtp1hL%2B0vLnFe6P3LmBymVIWHwY3C8AHUTwsD8pUpDZ1xkoGZFWU7r0Y57w%2B52saCcY%2BFKRB9KXyaPRvCGKR1Pd053%2FA1SU0z%2BhvUWIFSezo1BcXKGM%2Bnt7XxYx9%2BpeonklPslWbhRJwSx6zTprThPnDRX6Y5aIbPsdD7XyEfjKnxArVssrqNDq56%2BDZpgpJjH0nbkD6T2xaSbDkH21s%2F9fl7aC%2BiRnKGh%2BxBA2oDo9AD%2Br4vJAMg4Ne7Kyv5be0bWRqxakegFcYuTd6I3SjasWmJ2p8NLSNOeVh6ssBMHl8ex6SiRlIy8L6jtes8OEvqet3X5GjOKp69cy%2BKU4WfFdxOVu96zu2Ib0d8CuVhpvDEY75nlK2AlWodvy08BAStrvsTPm71ec9Bm1d6KgY85vTFAJ8KYarqG1tALdnWlNzs3VFiHvsyy73JdkldruZf1awUKmry3%2FD%2FQxLveUacSXqy8tTsjCgM1yESrT4IZf9spjlGUz%2BTXW0SdUfCezB4Mys%2FZQbrNE17XEqOz8e9ny7S5POAZOtc8EVEVIhcMf8v5v%2FgGl7pIovs5Kv77820I6N8ScvYKfEhjFqyodFa%2BpV2syouWfQbwfQfqgdTC10pm9BjqkAeWGSWvkEQ1k8dtlUCT%2FA2WL4jUQ8QQuZ4aCseRpowW0HPwICUsxBqcpMy%2BW7ChLADWueH1vvTijKPOsb3veLN0Oj%2FLOTuwZ8bqIirMD3OOs2Yz9pmhPJW4SR9HGMKecnSfw1qeeXbvs1GndYRpNccvmG8B5Z9bs9LJSF6310oJBCutB6A66FjDmxnW8Ybkljb5KICwmO0IWU86Tyj%2FnPde1dMUC&X-Amz-Signature=8a74cbb3bb6808e5023239f17fac5ae6178d970ddc912218d474a5c053444fac&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXVXAK3B%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCbflhbdvfNiasx2eGPczSXQ63h83tUd%2Bzwlo3am%2BTS1wIhAMNw5VVjWEHEw%2BhLfk7TtGgsXmTVuy9JqcEBLfDzT1Z%2BKv8DCH0QABoMNjM3NDIzMTgzODA1IgxOwzMkIdUKECGvOYYq3ANRK7Y174o7avwqUSEoqjtp1hL%2B0vLnFe6P3LmBymVIWHwY3C8AHUTwsD8pUpDZ1xkoGZFWU7r0Y57w%2B52saCcY%2BFKRB9KXyaPRvCGKR1Pd053%2FA1SU0z%2BhvUWIFSezo1BcXKGM%2Bnt7XxYx9%2BpeonklPslWbhRJwSx6zTprThPnDRX6Y5aIbPsdD7XyEfjKnxArVssrqNDq56%2BDZpgpJjH0nbkD6T2xaSbDkH21s%2F9fl7aC%2BiRnKGh%2BxBA2oDo9AD%2Br4vJAMg4Ne7Kyv5be0bWRqxakegFcYuTd6I3SjasWmJ2p8NLSNOeVh6ssBMHl8ex6SiRlIy8L6jtes8OEvqet3X5GjOKp69cy%2BKU4WfFdxOVu96zu2Ib0d8CuVhpvDEY75nlK2AlWodvy08BAStrvsTPm71ec9Bm1d6KgY85vTFAJ8KYarqG1tALdnWlNzs3VFiHvsyy73JdkldruZf1awUKmry3%2FD%2FQxLveUacSXqy8tTsjCgM1yESrT4IZf9spjlGUz%2BTXW0SdUfCezB4Mys%2FZQbrNE17XEqOz8e9ny7S5POAZOtc8EVEVIhcMf8v5v%2FgGl7pIovs5Kv77820I6N8ScvYKfEhjFqyodFa%2BpV2syouWfQbwfQfqgdTC10pm9BjqkAeWGSWvkEQ1k8dtlUCT%2FA2WL4jUQ8QQuZ4aCseRpowW0HPwICUsxBqcpMy%2BW7ChLADWueH1vvTijKPOsb3veLN0Oj%2FLOTuwZ8bqIirMD3OOs2Yz9pmhPJW4SR9HGMKecnSfw1qeeXbvs1GndYRpNccvmG8B5Z9bs9LJSF6310oJBCutB6A66FjDmxnW8Ybkljb5KICwmO0IWU86Tyj%2FnPde1dMUC&X-Amz-Signature=57e9105febebdf69f0156b32ba08b238392c9806a74ebfff4f96e51836d21d39&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXVXAK3B%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCbflhbdvfNiasx2eGPczSXQ63h83tUd%2Bzwlo3am%2BTS1wIhAMNw5VVjWEHEw%2BhLfk7TtGgsXmTVuy9JqcEBLfDzT1Z%2BKv8DCH0QABoMNjM3NDIzMTgzODA1IgxOwzMkIdUKECGvOYYq3ANRK7Y174o7avwqUSEoqjtp1hL%2B0vLnFe6P3LmBymVIWHwY3C8AHUTwsD8pUpDZ1xkoGZFWU7r0Y57w%2B52saCcY%2BFKRB9KXyaPRvCGKR1Pd053%2FA1SU0z%2BhvUWIFSezo1BcXKGM%2Bnt7XxYx9%2BpeonklPslWbhRJwSx6zTprThPnDRX6Y5aIbPsdD7XyEfjKnxArVssrqNDq56%2BDZpgpJjH0nbkD6T2xaSbDkH21s%2F9fl7aC%2BiRnKGh%2BxBA2oDo9AD%2Br4vJAMg4Ne7Kyv5be0bWRqxakegFcYuTd6I3SjasWmJ2p8NLSNOeVh6ssBMHl8ex6SiRlIy8L6jtes8OEvqet3X5GjOKp69cy%2BKU4WfFdxOVu96zu2Ib0d8CuVhpvDEY75nlK2AlWodvy08BAStrvsTPm71ec9Bm1d6KgY85vTFAJ8KYarqG1tALdnWlNzs3VFiHvsyy73JdkldruZf1awUKmry3%2FD%2FQxLveUacSXqy8tTsjCgM1yESrT4IZf9spjlGUz%2BTXW0SdUfCezB4Mys%2FZQbrNE17XEqOz8e9ny7S5POAZOtc8EVEVIhcMf8v5v%2FgGl7pIovs5Kv77820I6N8ScvYKfEhjFqyodFa%2BpV2syouWfQbwfQfqgdTC10pm9BjqkAeWGSWvkEQ1k8dtlUCT%2FA2WL4jUQ8QQuZ4aCseRpowW0HPwICUsxBqcpMy%2BW7ChLADWueH1vvTijKPOsb3veLN0Oj%2FLOTuwZ8bqIirMD3OOs2Yz9pmhPJW4SR9HGMKecnSfw1qeeXbvs1GndYRpNccvmG8B5Z9bs9LJSF6310oJBCutB6A66FjDmxnW8Ybkljb5KICwmO0IWU86Tyj%2FnPde1dMUC&X-Amz-Signature=360cc1217dfb7357f04ba4989060b4e2b0ddc4710dd2b180bab8fe7b2a63be7c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXVXAK3B%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCbflhbdvfNiasx2eGPczSXQ63h83tUd%2Bzwlo3am%2BTS1wIhAMNw5VVjWEHEw%2BhLfk7TtGgsXmTVuy9JqcEBLfDzT1Z%2BKv8DCH0QABoMNjM3NDIzMTgzODA1IgxOwzMkIdUKECGvOYYq3ANRK7Y174o7avwqUSEoqjtp1hL%2B0vLnFe6P3LmBymVIWHwY3C8AHUTwsD8pUpDZ1xkoGZFWU7r0Y57w%2B52saCcY%2BFKRB9KXyaPRvCGKR1Pd053%2FA1SU0z%2BhvUWIFSezo1BcXKGM%2Bnt7XxYx9%2BpeonklPslWbhRJwSx6zTprThPnDRX6Y5aIbPsdD7XyEfjKnxArVssrqNDq56%2BDZpgpJjH0nbkD6T2xaSbDkH21s%2F9fl7aC%2BiRnKGh%2BxBA2oDo9AD%2Br4vJAMg4Ne7Kyv5be0bWRqxakegFcYuTd6I3SjasWmJ2p8NLSNOeVh6ssBMHl8ex6SiRlIy8L6jtes8OEvqet3X5GjOKp69cy%2BKU4WfFdxOVu96zu2Ib0d8CuVhpvDEY75nlK2AlWodvy08BAStrvsTPm71ec9Bm1d6KgY85vTFAJ8KYarqG1tALdnWlNzs3VFiHvsyy73JdkldruZf1awUKmry3%2FD%2FQxLveUacSXqy8tTsjCgM1yESrT4IZf9spjlGUz%2BTXW0SdUfCezB4Mys%2FZQbrNE17XEqOz8e9ny7S5POAZOtc8EVEVIhcMf8v5v%2FgGl7pIovs5Kv77820I6N8ScvYKfEhjFqyodFa%2BpV2syouWfQbwfQfqgdTC10pm9BjqkAeWGSWvkEQ1k8dtlUCT%2FA2WL4jUQ8QQuZ4aCseRpowW0HPwICUsxBqcpMy%2BW7ChLADWueH1vvTijKPOsb3veLN0Oj%2FLOTuwZ8bqIirMD3OOs2Yz9pmhPJW4SR9HGMKecnSfw1qeeXbvs1GndYRpNccvmG8B5Z9bs9LJSF6310oJBCutB6A66FjDmxnW8Ybkljb5KICwmO0IWU86Tyj%2FnPde1dMUC&X-Amz-Signature=7b96ba11020b5fe3425d832eaab03e27cf54d7a47f25f7e8ae7653e241d5c263&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXVXAK3B%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCbflhbdvfNiasx2eGPczSXQ63h83tUd%2Bzwlo3am%2BTS1wIhAMNw5VVjWEHEw%2BhLfk7TtGgsXmTVuy9JqcEBLfDzT1Z%2BKv8DCH0QABoMNjM3NDIzMTgzODA1IgxOwzMkIdUKECGvOYYq3ANRK7Y174o7avwqUSEoqjtp1hL%2B0vLnFe6P3LmBymVIWHwY3C8AHUTwsD8pUpDZ1xkoGZFWU7r0Y57w%2B52saCcY%2BFKRB9KXyaPRvCGKR1Pd053%2FA1SU0z%2BhvUWIFSezo1BcXKGM%2Bnt7XxYx9%2BpeonklPslWbhRJwSx6zTprThPnDRX6Y5aIbPsdD7XyEfjKnxArVssrqNDq56%2BDZpgpJjH0nbkD6T2xaSbDkH21s%2F9fl7aC%2BiRnKGh%2BxBA2oDo9AD%2Br4vJAMg4Ne7Kyv5be0bWRqxakegFcYuTd6I3SjasWmJ2p8NLSNOeVh6ssBMHl8ex6SiRlIy8L6jtes8OEvqet3X5GjOKp69cy%2BKU4WfFdxOVu96zu2Ib0d8CuVhpvDEY75nlK2AlWodvy08BAStrvsTPm71ec9Bm1d6KgY85vTFAJ8KYarqG1tALdnWlNzs3VFiHvsyy73JdkldruZf1awUKmry3%2FD%2FQxLveUacSXqy8tTsjCgM1yESrT4IZf9spjlGUz%2BTXW0SdUfCezB4Mys%2FZQbrNE17XEqOz8e9ny7S5POAZOtc8EVEVIhcMf8v5v%2FgGl7pIovs5Kv77820I6N8ScvYKfEhjFqyodFa%2BpV2syouWfQbwfQfqgdTC10pm9BjqkAeWGSWvkEQ1k8dtlUCT%2FA2WL4jUQ8QQuZ4aCseRpowW0HPwICUsxBqcpMy%2BW7ChLADWueH1vvTijKPOsb3veLN0Oj%2FLOTuwZ8bqIirMD3OOs2Yz9pmhPJW4SR9HGMKecnSfw1qeeXbvs1GndYRpNccvmG8B5Z9bs9LJSF6310oJBCutB6A66FjDmxnW8Ybkljb5KICwmO0IWU86Tyj%2FnPde1dMUC&X-Amz-Signature=7170d20a672fbdd5957befed31ac578c1344415221b3349e88ca168dbedddf52&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXVXAK3B%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCbflhbdvfNiasx2eGPczSXQ63h83tUd%2Bzwlo3am%2BTS1wIhAMNw5VVjWEHEw%2BhLfk7TtGgsXmTVuy9JqcEBLfDzT1Z%2BKv8DCH0QABoMNjM3NDIzMTgzODA1IgxOwzMkIdUKECGvOYYq3ANRK7Y174o7avwqUSEoqjtp1hL%2B0vLnFe6P3LmBymVIWHwY3C8AHUTwsD8pUpDZ1xkoGZFWU7r0Y57w%2B52saCcY%2BFKRB9KXyaPRvCGKR1Pd053%2FA1SU0z%2BhvUWIFSezo1BcXKGM%2Bnt7XxYx9%2BpeonklPslWbhRJwSx6zTprThPnDRX6Y5aIbPsdD7XyEfjKnxArVssrqNDq56%2BDZpgpJjH0nbkD6T2xaSbDkH21s%2F9fl7aC%2BiRnKGh%2BxBA2oDo9AD%2Br4vJAMg4Ne7Kyv5be0bWRqxakegFcYuTd6I3SjasWmJ2p8NLSNOeVh6ssBMHl8ex6SiRlIy8L6jtes8OEvqet3X5GjOKp69cy%2BKU4WfFdxOVu96zu2Ib0d8CuVhpvDEY75nlK2AlWodvy08BAStrvsTPm71ec9Bm1d6KgY85vTFAJ8KYarqG1tALdnWlNzs3VFiHvsyy73JdkldruZf1awUKmry3%2FD%2FQxLveUacSXqy8tTsjCgM1yESrT4IZf9spjlGUz%2BTXW0SdUfCezB4Mys%2FZQbrNE17XEqOz8e9ny7S5POAZOtc8EVEVIhcMf8v5v%2FgGl7pIovs5Kv77820I6N8ScvYKfEhjFqyodFa%2BpV2syouWfQbwfQfqgdTC10pm9BjqkAeWGSWvkEQ1k8dtlUCT%2FA2WL4jUQ8QQuZ4aCseRpowW0HPwICUsxBqcpMy%2BW7ChLADWueH1vvTijKPOsb3veLN0Oj%2FLOTuwZ8bqIirMD3OOs2Yz9pmhPJW4SR9HGMKecnSfw1qeeXbvs1GndYRpNccvmG8B5Z9bs9LJSF6310oJBCutB6A66FjDmxnW8Ybkljb5KICwmO0IWU86Tyj%2FnPde1dMUC&X-Amz-Signature=2223f5d22411d2e1742518d03a9629d8d2674e312e68283cc6bb4e869a900eb9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXVXAK3B%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCbflhbdvfNiasx2eGPczSXQ63h83tUd%2Bzwlo3am%2BTS1wIhAMNw5VVjWEHEw%2BhLfk7TtGgsXmTVuy9JqcEBLfDzT1Z%2BKv8DCH0QABoMNjM3NDIzMTgzODA1IgxOwzMkIdUKECGvOYYq3ANRK7Y174o7avwqUSEoqjtp1hL%2B0vLnFe6P3LmBymVIWHwY3C8AHUTwsD8pUpDZ1xkoGZFWU7r0Y57w%2B52saCcY%2BFKRB9KXyaPRvCGKR1Pd053%2FA1SU0z%2BhvUWIFSezo1BcXKGM%2Bnt7XxYx9%2BpeonklPslWbhRJwSx6zTprThPnDRX6Y5aIbPsdD7XyEfjKnxArVssrqNDq56%2BDZpgpJjH0nbkD6T2xaSbDkH21s%2F9fl7aC%2BiRnKGh%2BxBA2oDo9AD%2Br4vJAMg4Ne7Kyv5be0bWRqxakegFcYuTd6I3SjasWmJ2p8NLSNOeVh6ssBMHl8ex6SiRlIy8L6jtes8OEvqet3X5GjOKp69cy%2BKU4WfFdxOVu96zu2Ib0d8CuVhpvDEY75nlK2AlWodvy08BAStrvsTPm71ec9Bm1d6KgY85vTFAJ8KYarqG1tALdnWlNzs3VFiHvsyy73JdkldruZf1awUKmry3%2FD%2FQxLveUacSXqy8tTsjCgM1yESrT4IZf9spjlGUz%2BTXW0SdUfCezB4Mys%2FZQbrNE17XEqOz8e9ny7S5POAZOtc8EVEVIhcMf8v5v%2FgGl7pIovs5Kv77820I6N8ScvYKfEhjFqyodFa%2BpV2syouWfQbwfQfqgdTC10pm9BjqkAeWGSWvkEQ1k8dtlUCT%2FA2WL4jUQ8QQuZ4aCseRpowW0HPwICUsxBqcpMy%2BW7ChLADWueH1vvTijKPOsb3veLN0Oj%2FLOTuwZ8bqIirMD3OOs2Yz9pmhPJW4SR9HGMKecnSfw1qeeXbvs1GndYRpNccvmG8B5Z9bs9LJSF6310oJBCutB6A66FjDmxnW8Ybkljb5KICwmO0IWU86Tyj%2FnPde1dMUC&X-Amz-Signature=20d187aeab8c331d71c809394b5c844d671444e819ed5e8a338dc95a8bf5951b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXVXAK3B%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCbflhbdvfNiasx2eGPczSXQ63h83tUd%2Bzwlo3am%2BTS1wIhAMNw5VVjWEHEw%2BhLfk7TtGgsXmTVuy9JqcEBLfDzT1Z%2BKv8DCH0QABoMNjM3NDIzMTgzODA1IgxOwzMkIdUKECGvOYYq3ANRK7Y174o7avwqUSEoqjtp1hL%2B0vLnFe6P3LmBymVIWHwY3C8AHUTwsD8pUpDZ1xkoGZFWU7r0Y57w%2B52saCcY%2BFKRB9KXyaPRvCGKR1Pd053%2FA1SU0z%2BhvUWIFSezo1BcXKGM%2Bnt7XxYx9%2BpeonklPslWbhRJwSx6zTprThPnDRX6Y5aIbPsdD7XyEfjKnxArVssrqNDq56%2BDZpgpJjH0nbkD6T2xaSbDkH21s%2F9fl7aC%2BiRnKGh%2BxBA2oDo9AD%2Br4vJAMg4Ne7Kyv5be0bWRqxakegFcYuTd6I3SjasWmJ2p8NLSNOeVh6ssBMHl8ex6SiRlIy8L6jtes8OEvqet3X5GjOKp69cy%2BKU4WfFdxOVu96zu2Ib0d8CuVhpvDEY75nlK2AlWodvy08BAStrvsTPm71ec9Bm1d6KgY85vTFAJ8KYarqG1tALdnWlNzs3VFiHvsyy73JdkldruZf1awUKmry3%2FD%2FQxLveUacSXqy8tTsjCgM1yESrT4IZf9spjlGUz%2BTXW0SdUfCezB4Mys%2FZQbrNE17XEqOz8e9ny7S5POAZOtc8EVEVIhcMf8v5v%2FgGl7pIovs5Kv77820I6N8ScvYKfEhjFqyodFa%2BpV2syouWfQbwfQfqgdTC10pm9BjqkAeWGSWvkEQ1k8dtlUCT%2FA2WL4jUQ8QQuZ4aCseRpowW0HPwICUsxBqcpMy%2BW7ChLADWueH1vvTijKPOsb3veLN0Oj%2FLOTuwZ8bqIirMD3OOs2Yz9pmhPJW4SR9HGMKecnSfw1qeeXbvs1GndYRpNccvmG8B5Z9bs9LJSF6310oJBCutB6A66FjDmxnW8Ybkljb5KICwmO0IWU86Tyj%2FnPde1dMUC&X-Amz-Signature=9d030158400fef87587957590881e699107bd39bfc1d8f6bfde1edc79173a81d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXVXAK3B%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCbflhbdvfNiasx2eGPczSXQ63h83tUd%2Bzwlo3am%2BTS1wIhAMNw5VVjWEHEw%2BhLfk7TtGgsXmTVuy9JqcEBLfDzT1Z%2BKv8DCH0QABoMNjM3NDIzMTgzODA1IgxOwzMkIdUKECGvOYYq3ANRK7Y174o7avwqUSEoqjtp1hL%2B0vLnFe6P3LmBymVIWHwY3C8AHUTwsD8pUpDZ1xkoGZFWU7r0Y57w%2B52saCcY%2BFKRB9KXyaPRvCGKR1Pd053%2FA1SU0z%2BhvUWIFSezo1BcXKGM%2Bnt7XxYx9%2BpeonklPslWbhRJwSx6zTprThPnDRX6Y5aIbPsdD7XyEfjKnxArVssrqNDq56%2BDZpgpJjH0nbkD6T2xaSbDkH21s%2F9fl7aC%2BiRnKGh%2BxBA2oDo9AD%2Br4vJAMg4Ne7Kyv5be0bWRqxakegFcYuTd6I3SjasWmJ2p8NLSNOeVh6ssBMHl8ex6SiRlIy8L6jtes8OEvqet3X5GjOKp69cy%2BKU4WfFdxOVu96zu2Ib0d8CuVhpvDEY75nlK2AlWodvy08BAStrvsTPm71ec9Bm1d6KgY85vTFAJ8KYarqG1tALdnWlNzs3VFiHvsyy73JdkldruZf1awUKmry3%2FD%2FQxLveUacSXqy8tTsjCgM1yESrT4IZf9spjlGUz%2BTXW0SdUfCezB4Mys%2FZQbrNE17XEqOz8e9ny7S5POAZOtc8EVEVIhcMf8v5v%2FgGl7pIovs5Kv77820I6N8ScvYKfEhjFqyodFa%2BpV2syouWfQbwfQfqgdTC10pm9BjqkAeWGSWvkEQ1k8dtlUCT%2FA2WL4jUQ8QQuZ4aCseRpowW0HPwICUsxBqcpMy%2BW7ChLADWueH1vvTijKPOsb3veLN0Oj%2FLOTuwZ8bqIirMD3OOs2Yz9pmhPJW4SR9HGMKecnSfw1qeeXbvs1GndYRpNccvmG8B5Z9bs9LJSF6310oJBCutB6A66FjDmxnW8Ybkljb5KICwmO0IWU86Tyj%2FnPde1dMUC&X-Amz-Signature=2f77cd0a86b5660b2235ac2c3e00e4bcd06ea6e819e30bfebaf10c72f6f15b11&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677MSWQRT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIFofV%2FeU%2FXsrdA57UaYdz5tUk8BZB3UmvByhDNy%2FgZVfAiEA%2BYPC7kaqym0PRH5N33B4UzHI1wtc83gI7nRP8bQqKVsq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDPiPOFGL%2BUsxd%2BrugCrcA3wgfM99NxGnyxsZr0vdceyIBVxuannBf4e3rWr9RyssFzj63OZu2IWHCcwUcPP6ptUClDZC5%2FIyYnW1WLFp28R84kshSiL60tZBKw%2BSH569ecGQ3WLs5M0hMrTUv6rLw6i2r4ugc3pXH5sQhv4oKhqOkHcu1SC1CwEQkRPIqx3CyzU5orEus4k2AYlqcMHMFgISFpKQWzSlrTuKq1T5X2Ls7a%2F4eq8Is2Nc6fKAW%2FGMWOVMHHFESFBl40qzMrIhzfKZWpkMJ5bAISmN5xP%2BfRsW2XL%2BywpVUPMZ5udGFNjPWn3OKas8WHHnYjdTTcs2BL057Q7LImdgo0kMWKcQhWSlbA6EcFWuEZB0vcTaaFnbGLwUm2iopouqjhy1kCzSICAZYMN4o6Ne7Qs47ETb%2BJTaTSsbxaL4uPxEtCFQvDbCtgU6ieJDhkiiTRIrFuw4xFfeSA%2BbCf4EJRNzwmhutpi5AYdtdGE9GKS5UXNZNzG5eB11qx%2B%2F2my8mLoIfIWT3f3y94KhmBj10UcqTTEXKchO2fr%2Bj3uWEIH6reI3N8zQsEI58Ipmj%2B9UDZ35kw%2B7I29SKxZ3VgtuRtF0CebkjtxxEnOQTauvl6iJFcG51OmAwOn39YNLtTgsdMeWMMDSmb0GOqUBWQhhiJo9hWS%2BWY93HU8YjBl1iFC8eRGVy4UQBSYQZ73Ilo8Ainh7jiM0zSPqbvMQ3eiXOlePmV%2FV%2Bx8L05mk2LNzy72hmCt0WMSt6QlVUtR5qZ5alw1IX9OY2N%2BwunRifETDikhsU13lk8dPP1cvGoVGszFSlYii6eVhVVMVFXcSjMndpwqs1j%2BhdvvRbOgM4IjofO4ABB7k9DqsEmdsJaOGwaUe&X-Amz-Signature=7c9d7660eea06faaca988f361f3ed85aef78b4fe000c60627e8eb9bd3f382a05&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677MSWQRT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIFofV%2FeU%2FXsrdA57UaYdz5tUk8BZB3UmvByhDNy%2FgZVfAiEA%2BYPC7kaqym0PRH5N33B4UzHI1wtc83gI7nRP8bQqKVsq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDPiPOFGL%2BUsxd%2BrugCrcA3wgfM99NxGnyxsZr0vdceyIBVxuannBf4e3rWr9RyssFzj63OZu2IWHCcwUcPP6ptUClDZC5%2FIyYnW1WLFp28R84kshSiL60tZBKw%2BSH569ecGQ3WLs5M0hMrTUv6rLw6i2r4ugc3pXH5sQhv4oKhqOkHcu1SC1CwEQkRPIqx3CyzU5orEus4k2AYlqcMHMFgISFpKQWzSlrTuKq1T5X2Ls7a%2F4eq8Is2Nc6fKAW%2FGMWOVMHHFESFBl40qzMrIhzfKZWpkMJ5bAISmN5xP%2BfRsW2XL%2BywpVUPMZ5udGFNjPWn3OKas8WHHnYjdTTcs2BL057Q7LImdgo0kMWKcQhWSlbA6EcFWuEZB0vcTaaFnbGLwUm2iopouqjhy1kCzSICAZYMN4o6Ne7Qs47ETb%2BJTaTSsbxaL4uPxEtCFQvDbCtgU6ieJDhkiiTRIrFuw4xFfeSA%2BbCf4EJRNzwmhutpi5AYdtdGE9GKS5UXNZNzG5eB11qx%2B%2F2my8mLoIfIWT3f3y94KhmBj10UcqTTEXKchO2fr%2Bj3uWEIH6reI3N8zQsEI58Ipmj%2B9UDZ35kw%2B7I29SKxZ3VgtuRtF0CebkjtxxEnOQTauvl6iJFcG51OmAwOn39YNLtTgsdMeWMMDSmb0GOqUBWQhhiJo9hWS%2BWY93HU8YjBl1iFC8eRGVy4UQBSYQZ73Ilo8Ainh7jiM0zSPqbvMQ3eiXOlePmV%2FV%2Bx8L05mk2LNzy72hmCt0WMSt6QlVUtR5qZ5alw1IX9OY2N%2BwunRifETDikhsU13lk8dPP1cvGoVGszFSlYii6eVhVVMVFXcSjMndpwqs1j%2BhdvvRbOgM4IjofO4ABB7k9DqsEmdsJaOGwaUe&X-Amz-Signature=1aabaadf20ef23a88633151c784a3d7ab03b426659239251fba0cdb0bc7d4867&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
