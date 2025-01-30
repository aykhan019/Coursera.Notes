

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DN5P6S4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FVZD9eMHpX7gIb1Qaac97sP0OtG5HEP0XDfwmdGN0%2FgIgGic3iJbeXgJ%2BX4cPbiByEmtu4dmyPFr92WA%2FHL40HUEqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGG0zc3fvVXqtvFZ3SrcAx3GXpO7CT0YUkDxI%2BeZXI%2F%2F0VKvZgC5%2FKd14jVxDMrD65svkHKvHA7armr97SaOtA8J01Jsx8mY%2FLhs6J52Q6txr917rTkNbT1O1yhbL4L%2Fr5p7GK1fY6GzcVfpCIpWfwm%2FFt6g4ZtzM%2F6upXrx9v97Qj7UwyaRqi7Y7dNIHFmyDLLxnAcn%2F%2BuwzjB%2BPK1LcJ%2FaM%2FaP1PEzHqBmHYbX1RDKJyDaZKtm2xC8s8mcbRJHIAv8a21mlaK%2F9OPRj3mWWMW96zb5cCO0xNrR8rp4yT9VsRwNeA8GB%2Boo%2Bp3jVXslUv%2FR0N%2BEjPSvKEY0%2FFoQJT%2Ft4sNZqI8SeB7gY8aTh7jWc%2BDrhInY4KcslaWyc4ueGoBjvB8Rxd3nUpgHksipIiIBZ5xtG2ZiKXe7zOfcz56K4ChEHSpttwt5q70IOVt3SKjvAoouqnyMtOKtErCCXqGCQYwwJAP%2FG228wa55v88h%2B20RiRqzQUDc%2FEer0%2FH9S7pXbsa3tNOrR7WsVcltm7kkeW73SU%2B8n%2FdoAsS7ixLRNpnWVHXWgkxtlR4z%2FacrouT54ttePQZnSTkZxH7kpHhHq5IF7a9PCv2RZ%2BcWzfcndS1uCtkg0mg7EUabbq7eSDyP4FK4kOaKcftCMIj77bwGOqUBwGQ6WRRpULHU1kj1tWf3OKjMuwevier7yDbv9nqc6kBnKWXD1Lt2x%2Fd%2F%2BgZ8h9oXOq%2BIw5lJ%2BHrWOspsNwtnKQGlflSZ%2FHZ05Ook9e4fsDFuwBJtCulfTi%2FaJKqhIkjg4I79U90JA%2B3uCh%2BCB7D45GGMISMjhFUfIG8tUm4kK9SIJa2NI8vseiul9D1JXGRqYvsYd7lhfFt7Plg%2BO67DIRNxmKKE&X-Amz-Signature=80a74d2e09602c31a58620a7d83435d375a2d852548d3982c22fef8ba9fffa94&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DN5P6S4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FVZD9eMHpX7gIb1Qaac97sP0OtG5HEP0XDfwmdGN0%2FgIgGic3iJbeXgJ%2BX4cPbiByEmtu4dmyPFr92WA%2FHL40HUEqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGG0zc3fvVXqtvFZ3SrcAx3GXpO7CT0YUkDxI%2BeZXI%2F%2F0VKvZgC5%2FKd14jVxDMrD65svkHKvHA7armr97SaOtA8J01Jsx8mY%2FLhs6J52Q6txr917rTkNbT1O1yhbL4L%2Fr5p7GK1fY6GzcVfpCIpWfwm%2FFt6g4ZtzM%2F6upXrx9v97Qj7UwyaRqi7Y7dNIHFmyDLLxnAcn%2F%2BuwzjB%2BPK1LcJ%2FaM%2FaP1PEzHqBmHYbX1RDKJyDaZKtm2xC8s8mcbRJHIAv8a21mlaK%2F9OPRj3mWWMW96zb5cCO0xNrR8rp4yT9VsRwNeA8GB%2Boo%2Bp3jVXslUv%2FR0N%2BEjPSvKEY0%2FFoQJT%2Ft4sNZqI8SeB7gY8aTh7jWc%2BDrhInY4KcslaWyc4ueGoBjvB8Rxd3nUpgHksipIiIBZ5xtG2ZiKXe7zOfcz56K4ChEHSpttwt5q70IOVt3SKjvAoouqnyMtOKtErCCXqGCQYwwJAP%2FG228wa55v88h%2B20RiRqzQUDc%2FEer0%2FH9S7pXbsa3tNOrR7WsVcltm7kkeW73SU%2B8n%2FdoAsS7ixLRNpnWVHXWgkxtlR4z%2FacrouT54ttePQZnSTkZxH7kpHhHq5IF7a9PCv2RZ%2BcWzfcndS1uCtkg0mg7EUabbq7eSDyP4FK4kOaKcftCMIj77bwGOqUBwGQ6WRRpULHU1kj1tWf3OKjMuwevier7yDbv9nqc6kBnKWXD1Lt2x%2Fd%2F%2BgZ8h9oXOq%2BIw5lJ%2BHrWOspsNwtnKQGlflSZ%2FHZ05Ook9e4fsDFuwBJtCulfTi%2FaJKqhIkjg4I79U90JA%2B3uCh%2BCB7D45GGMISMjhFUfIG8tUm4kK9SIJa2NI8vseiul9D1JXGRqYvsYd7lhfFt7Plg%2BO67DIRNxmKKE&X-Amz-Signature=ab6e68163438ac358646fb1b81220ff15c8d0d2460c3bd71c794dfde4dbd7a5a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DN5P6S4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FVZD9eMHpX7gIb1Qaac97sP0OtG5HEP0XDfwmdGN0%2FgIgGic3iJbeXgJ%2BX4cPbiByEmtu4dmyPFr92WA%2FHL40HUEqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGG0zc3fvVXqtvFZ3SrcAx3GXpO7CT0YUkDxI%2BeZXI%2F%2F0VKvZgC5%2FKd14jVxDMrD65svkHKvHA7armr97SaOtA8J01Jsx8mY%2FLhs6J52Q6txr917rTkNbT1O1yhbL4L%2Fr5p7GK1fY6GzcVfpCIpWfwm%2FFt6g4ZtzM%2F6upXrx9v97Qj7UwyaRqi7Y7dNIHFmyDLLxnAcn%2F%2BuwzjB%2BPK1LcJ%2FaM%2FaP1PEzHqBmHYbX1RDKJyDaZKtm2xC8s8mcbRJHIAv8a21mlaK%2F9OPRj3mWWMW96zb5cCO0xNrR8rp4yT9VsRwNeA8GB%2Boo%2Bp3jVXslUv%2FR0N%2BEjPSvKEY0%2FFoQJT%2Ft4sNZqI8SeB7gY8aTh7jWc%2BDrhInY4KcslaWyc4ueGoBjvB8Rxd3nUpgHksipIiIBZ5xtG2ZiKXe7zOfcz56K4ChEHSpttwt5q70IOVt3SKjvAoouqnyMtOKtErCCXqGCQYwwJAP%2FG228wa55v88h%2B20RiRqzQUDc%2FEer0%2FH9S7pXbsa3tNOrR7WsVcltm7kkeW73SU%2B8n%2FdoAsS7ixLRNpnWVHXWgkxtlR4z%2FacrouT54ttePQZnSTkZxH7kpHhHq5IF7a9PCv2RZ%2BcWzfcndS1uCtkg0mg7EUabbq7eSDyP4FK4kOaKcftCMIj77bwGOqUBwGQ6WRRpULHU1kj1tWf3OKjMuwevier7yDbv9nqc6kBnKWXD1Lt2x%2Fd%2F%2BgZ8h9oXOq%2BIw5lJ%2BHrWOspsNwtnKQGlflSZ%2FHZ05Ook9e4fsDFuwBJtCulfTi%2FaJKqhIkjg4I79U90JA%2B3uCh%2BCB7D45GGMISMjhFUfIG8tUm4kK9SIJa2NI8vseiul9D1JXGRqYvsYd7lhfFt7Plg%2BO67DIRNxmKKE&X-Amz-Signature=e7cad9651cafe44546125cd21f951b75e888f4433108f612303efc5308fa4a27&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DN5P6S4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FVZD9eMHpX7gIb1Qaac97sP0OtG5HEP0XDfwmdGN0%2FgIgGic3iJbeXgJ%2BX4cPbiByEmtu4dmyPFr92WA%2FHL40HUEqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGG0zc3fvVXqtvFZ3SrcAx3GXpO7CT0YUkDxI%2BeZXI%2F%2F0VKvZgC5%2FKd14jVxDMrD65svkHKvHA7armr97SaOtA8J01Jsx8mY%2FLhs6J52Q6txr917rTkNbT1O1yhbL4L%2Fr5p7GK1fY6GzcVfpCIpWfwm%2FFt6g4ZtzM%2F6upXrx9v97Qj7UwyaRqi7Y7dNIHFmyDLLxnAcn%2F%2BuwzjB%2BPK1LcJ%2FaM%2FaP1PEzHqBmHYbX1RDKJyDaZKtm2xC8s8mcbRJHIAv8a21mlaK%2F9OPRj3mWWMW96zb5cCO0xNrR8rp4yT9VsRwNeA8GB%2Boo%2Bp3jVXslUv%2FR0N%2BEjPSvKEY0%2FFoQJT%2Ft4sNZqI8SeB7gY8aTh7jWc%2BDrhInY4KcslaWyc4ueGoBjvB8Rxd3nUpgHksipIiIBZ5xtG2ZiKXe7zOfcz56K4ChEHSpttwt5q70IOVt3SKjvAoouqnyMtOKtErCCXqGCQYwwJAP%2FG228wa55v88h%2B20RiRqzQUDc%2FEer0%2FH9S7pXbsa3tNOrR7WsVcltm7kkeW73SU%2B8n%2FdoAsS7ixLRNpnWVHXWgkxtlR4z%2FacrouT54ttePQZnSTkZxH7kpHhHq5IF7a9PCv2RZ%2BcWzfcndS1uCtkg0mg7EUabbq7eSDyP4FK4kOaKcftCMIj77bwGOqUBwGQ6WRRpULHU1kj1tWf3OKjMuwevier7yDbv9nqc6kBnKWXD1Lt2x%2Fd%2F%2BgZ8h9oXOq%2BIw5lJ%2BHrWOspsNwtnKQGlflSZ%2FHZ05Ook9e4fsDFuwBJtCulfTi%2FaJKqhIkjg4I79U90JA%2B3uCh%2BCB7D45GGMISMjhFUfIG8tUm4kK9SIJa2NI8vseiul9D1JXGRqYvsYd7lhfFt7Plg%2BO67DIRNxmKKE&X-Amz-Signature=e97377dff35a625e1b7171500e398efa4d40f09256b6339a3afa50a5b7fcc96e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DN5P6S4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FVZD9eMHpX7gIb1Qaac97sP0OtG5HEP0XDfwmdGN0%2FgIgGic3iJbeXgJ%2BX4cPbiByEmtu4dmyPFr92WA%2FHL40HUEqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGG0zc3fvVXqtvFZ3SrcAx3GXpO7CT0YUkDxI%2BeZXI%2F%2F0VKvZgC5%2FKd14jVxDMrD65svkHKvHA7armr97SaOtA8J01Jsx8mY%2FLhs6J52Q6txr917rTkNbT1O1yhbL4L%2Fr5p7GK1fY6GzcVfpCIpWfwm%2FFt6g4ZtzM%2F6upXrx9v97Qj7UwyaRqi7Y7dNIHFmyDLLxnAcn%2F%2BuwzjB%2BPK1LcJ%2FaM%2FaP1PEzHqBmHYbX1RDKJyDaZKtm2xC8s8mcbRJHIAv8a21mlaK%2F9OPRj3mWWMW96zb5cCO0xNrR8rp4yT9VsRwNeA8GB%2Boo%2Bp3jVXslUv%2FR0N%2BEjPSvKEY0%2FFoQJT%2Ft4sNZqI8SeB7gY8aTh7jWc%2BDrhInY4KcslaWyc4ueGoBjvB8Rxd3nUpgHksipIiIBZ5xtG2ZiKXe7zOfcz56K4ChEHSpttwt5q70IOVt3SKjvAoouqnyMtOKtErCCXqGCQYwwJAP%2FG228wa55v88h%2B20RiRqzQUDc%2FEer0%2FH9S7pXbsa3tNOrR7WsVcltm7kkeW73SU%2B8n%2FdoAsS7ixLRNpnWVHXWgkxtlR4z%2FacrouT54ttePQZnSTkZxH7kpHhHq5IF7a9PCv2RZ%2BcWzfcndS1uCtkg0mg7EUabbq7eSDyP4FK4kOaKcftCMIj77bwGOqUBwGQ6WRRpULHU1kj1tWf3OKjMuwevier7yDbv9nqc6kBnKWXD1Lt2x%2Fd%2F%2BgZ8h9oXOq%2BIw5lJ%2BHrWOspsNwtnKQGlflSZ%2FHZ05Ook9e4fsDFuwBJtCulfTi%2FaJKqhIkjg4I79U90JA%2B3uCh%2BCB7D45GGMISMjhFUfIG8tUm4kK9SIJa2NI8vseiul9D1JXGRqYvsYd7lhfFt7Plg%2BO67DIRNxmKKE&X-Amz-Signature=d23badc5e12eff9b13fbe9839669abf2e77c3702e273fdeeaf732db9b960f432&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DN5P6S4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FVZD9eMHpX7gIb1Qaac97sP0OtG5HEP0XDfwmdGN0%2FgIgGic3iJbeXgJ%2BX4cPbiByEmtu4dmyPFr92WA%2FHL40HUEqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGG0zc3fvVXqtvFZ3SrcAx3GXpO7CT0YUkDxI%2BeZXI%2F%2F0VKvZgC5%2FKd14jVxDMrD65svkHKvHA7armr97SaOtA8J01Jsx8mY%2FLhs6J52Q6txr917rTkNbT1O1yhbL4L%2Fr5p7GK1fY6GzcVfpCIpWfwm%2FFt6g4ZtzM%2F6upXrx9v97Qj7UwyaRqi7Y7dNIHFmyDLLxnAcn%2F%2BuwzjB%2BPK1LcJ%2FaM%2FaP1PEzHqBmHYbX1RDKJyDaZKtm2xC8s8mcbRJHIAv8a21mlaK%2F9OPRj3mWWMW96zb5cCO0xNrR8rp4yT9VsRwNeA8GB%2Boo%2Bp3jVXslUv%2FR0N%2BEjPSvKEY0%2FFoQJT%2Ft4sNZqI8SeB7gY8aTh7jWc%2BDrhInY4KcslaWyc4ueGoBjvB8Rxd3nUpgHksipIiIBZ5xtG2ZiKXe7zOfcz56K4ChEHSpttwt5q70IOVt3SKjvAoouqnyMtOKtErCCXqGCQYwwJAP%2FG228wa55v88h%2B20RiRqzQUDc%2FEer0%2FH9S7pXbsa3tNOrR7WsVcltm7kkeW73SU%2B8n%2FdoAsS7ixLRNpnWVHXWgkxtlR4z%2FacrouT54ttePQZnSTkZxH7kpHhHq5IF7a9PCv2RZ%2BcWzfcndS1uCtkg0mg7EUabbq7eSDyP4FK4kOaKcftCMIj77bwGOqUBwGQ6WRRpULHU1kj1tWf3OKjMuwevier7yDbv9nqc6kBnKWXD1Lt2x%2Fd%2F%2BgZ8h9oXOq%2BIw5lJ%2BHrWOspsNwtnKQGlflSZ%2FHZ05Ook9e4fsDFuwBJtCulfTi%2FaJKqhIkjg4I79U90JA%2B3uCh%2BCB7D45GGMISMjhFUfIG8tUm4kK9SIJa2NI8vseiul9D1JXGRqYvsYd7lhfFt7Plg%2BO67DIRNxmKKE&X-Amz-Signature=a91e319c8dcae2ee1457956bb6568f9d9f7d7714584515d8023ac901b6f5751c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DN5P6S4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FVZD9eMHpX7gIb1Qaac97sP0OtG5HEP0XDfwmdGN0%2FgIgGic3iJbeXgJ%2BX4cPbiByEmtu4dmyPFr92WA%2FHL40HUEqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGG0zc3fvVXqtvFZ3SrcAx3GXpO7CT0YUkDxI%2BeZXI%2F%2F0VKvZgC5%2FKd14jVxDMrD65svkHKvHA7armr97SaOtA8J01Jsx8mY%2FLhs6J52Q6txr917rTkNbT1O1yhbL4L%2Fr5p7GK1fY6GzcVfpCIpWfwm%2FFt6g4ZtzM%2F6upXrx9v97Qj7UwyaRqi7Y7dNIHFmyDLLxnAcn%2F%2BuwzjB%2BPK1LcJ%2FaM%2FaP1PEzHqBmHYbX1RDKJyDaZKtm2xC8s8mcbRJHIAv8a21mlaK%2F9OPRj3mWWMW96zb5cCO0xNrR8rp4yT9VsRwNeA8GB%2Boo%2Bp3jVXslUv%2FR0N%2BEjPSvKEY0%2FFoQJT%2Ft4sNZqI8SeB7gY8aTh7jWc%2BDrhInY4KcslaWyc4ueGoBjvB8Rxd3nUpgHksipIiIBZ5xtG2ZiKXe7zOfcz56K4ChEHSpttwt5q70IOVt3SKjvAoouqnyMtOKtErCCXqGCQYwwJAP%2FG228wa55v88h%2B20RiRqzQUDc%2FEer0%2FH9S7pXbsa3tNOrR7WsVcltm7kkeW73SU%2B8n%2FdoAsS7ixLRNpnWVHXWgkxtlR4z%2FacrouT54ttePQZnSTkZxH7kpHhHq5IF7a9PCv2RZ%2BcWzfcndS1uCtkg0mg7EUabbq7eSDyP4FK4kOaKcftCMIj77bwGOqUBwGQ6WRRpULHU1kj1tWf3OKjMuwevier7yDbv9nqc6kBnKWXD1Lt2x%2Fd%2F%2BgZ8h9oXOq%2BIw5lJ%2BHrWOspsNwtnKQGlflSZ%2FHZ05Ook9e4fsDFuwBJtCulfTi%2FaJKqhIkjg4I79U90JA%2B3uCh%2BCB7D45GGMISMjhFUfIG8tUm4kK9SIJa2NI8vseiul9D1JXGRqYvsYd7lhfFt7Plg%2BO67DIRNxmKKE&X-Amz-Signature=dee31850351258b520a8e57fef86f70b451379b72618f8fb760dd724f6e90d14&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DN5P6S4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FVZD9eMHpX7gIb1Qaac97sP0OtG5HEP0XDfwmdGN0%2FgIgGic3iJbeXgJ%2BX4cPbiByEmtu4dmyPFr92WA%2FHL40HUEqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGG0zc3fvVXqtvFZ3SrcAx3GXpO7CT0YUkDxI%2BeZXI%2F%2F0VKvZgC5%2FKd14jVxDMrD65svkHKvHA7armr97SaOtA8J01Jsx8mY%2FLhs6J52Q6txr917rTkNbT1O1yhbL4L%2Fr5p7GK1fY6GzcVfpCIpWfwm%2FFt6g4ZtzM%2F6upXrx9v97Qj7UwyaRqi7Y7dNIHFmyDLLxnAcn%2F%2BuwzjB%2BPK1LcJ%2FaM%2FaP1PEzHqBmHYbX1RDKJyDaZKtm2xC8s8mcbRJHIAv8a21mlaK%2F9OPRj3mWWMW96zb5cCO0xNrR8rp4yT9VsRwNeA8GB%2Boo%2Bp3jVXslUv%2FR0N%2BEjPSvKEY0%2FFoQJT%2Ft4sNZqI8SeB7gY8aTh7jWc%2BDrhInY4KcslaWyc4ueGoBjvB8Rxd3nUpgHksipIiIBZ5xtG2ZiKXe7zOfcz56K4ChEHSpttwt5q70IOVt3SKjvAoouqnyMtOKtErCCXqGCQYwwJAP%2FG228wa55v88h%2B20RiRqzQUDc%2FEer0%2FH9S7pXbsa3tNOrR7WsVcltm7kkeW73SU%2B8n%2FdoAsS7ixLRNpnWVHXWgkxtlR4z%2FacrouT54ttePQZnSTkZxH7kpHhHq5IF7a9PCv2RZ%2BcWzfcndS1uCtkg0mg7EUabbq7eSDyP4FK4kOaKcftCMIj77bwGOqUBwGQ6WRRpULHU1kj1tWf3OKjMuwevier7yDbv9nqc6kBnKWXD1Lt2x%2Fd%2F%2BgZ8h9oXOq%2BIw5lJ%2BHrWOspsNwtnKQGlflSZ%2FHZ05Ook9e4fsDFuwBJtCulfTi%2FaJKqhIkjg4I79U90JA%2B3uCh%2BCB7D45GGMISMjhFUfIG8tUm4kK9SIJa2NI8vseiul9D1JXGRqYvsYd7lhfFt7Plg%2BO67DIRNxmKKE&X-Amz-Signature=3db9f56ecea112edf6f4911635bc78469026e8554d2c3d9d38e5db8113848e70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DN5P6S4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FVZD9eMHpX7gIb1Qaac97sP0OtG5HEP0XDfwmdGN0%2FgIgGic3iJbeXgJ%2BX4cPbiByEmtu4dmyPFr92WA%2FHL40HUEqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGG0zc3fvVXqtvFZ3SrcAx3GXpO7CT0YUkDxI%2BeZXI%2F%2F0VKvZgC5%2FKd14jVxDMrD65svkHKvHA7armr97SaOtA8J01Jsx8mY%2FLhs6J52Q6txr917rTkNbT1O1yhbL4L%2Fr5p7GK1fY6GzcVfpCIpWfwm%2FFt6g4ZtzM%2F6upXrx9v97Qj7UwyaRqi7Y7dNIHFmyDLLxnAcn%2F%2BuwzjB%2BPK1LcJ%2FaM%2FaP1PEzHqBmHYbX1RDKJyDaZKtm2xC8s8mcbRJHIAv8a21mlaK%2F9OPRj3mWWMW96zb5cCO0xNrR8rp4yT9VsRwNeA8GB%2Boo%2Bp3jVXslUv%2FR0N%2BEjPSvKEY0%2FFoQJT%2Ft4sNZqI8SeB7gY8aTh7jWc%2BDrhInY4KcslaWyc4ueGoBjvB8Rxd3nUpgHksipIiIBZ5xtG2ZiKXe7zOfcz56K4ChEHSpttwt5q70IOVt3SKjvAoouqnyMtOKtErCCXqGCQYwwJAP%2FG228wa55v88h%2B20RiRqzQUDc%2FEer0%2FH9S7pXbsa3tNOrR7WsVcltm7kkeW73SU%2B8n%2FdoAsS7ixLRNpnWVHXWgkxtlR4z%2FacrouT54ttePQZnSTkZxH7kpHhHq5IF7a9PCv2RZ%2BcWzfcndS1uCtkg0mg7EUabbq7eSDyP4FK4kOaKcftCMIj77bwGOqUBwGQ6WRRpULHU1kj1tWf3OKjMuwevier7yDbv9nqc6kBnKWXD1Lt2x%2Fd%2F%2BgZ8h9oXOq%2BIw5lJ%2BHrWOspsNwtnKQGlflSZ%2FHZ05Ook9e4fsDFuwBJtCulfTi%2FaJKqhIkjg4I79U90JA%2B3uCh%2BCB7D45GGMISMjhFUfIG8tUm4kK9SIJa2NI8vseiul9D1JXGRqYvsYd7lhfFt7Plg%2BO67DIRNxmKKE&X-Amz-Signature=ae7b081edd16762011565a0722db1a5e6bce6eb14aa1ec19cd9d0d35687be8d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RX6I5RCO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BnDtBgPQm2Ce7UqZdppFdESvWUHAYZSHYf2BrSnwRYAIgbxSVja%2Bp8cZKbGU3jAs4u6AluIEkVrq5LZc2KFeEG6kqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBILsNGdqHCmVcQpIyrcA%2BERGR4L1pxcWltVMO8D49GayyOiV0T48wem6eetPMxtLMlMy3SUkTIrKOphmcwa7liaamVdbsrxuhrBN0Nvd%2FYpwaFnDm5wTtCkrB98IgIn3grNBbbD8vjUmX3q6WUG4ooM4bd9%2Bd7Q0nhwS069fxbA95tDZWm0jXkhvSLnD50HVNwHXn9TloAEbLq2GnZS3R1I77%2Bj%2BsZTn9X9R8mE2rOX%2BiGMoMFd1JZKjjK%2Ffu7gYj0I0NvaXSMLKG900YVHMHDcKlGvxH3%2FN7VgP%2BuABGs%2FPLmnq4XmG6HQDgE84f6RByOCyp7wGIagvu6bV9TXVjjXC807KMrxi%2FZg%2Bd0w33DEGkkqwXuIzZaC449etTpfMaSQtB0Ykp%2BHrINpqYVILxvofWfFNo7fFNbO4t6FuG%2FtsmS2dvrHDGQcsm9l5%2FRu%2Bw3Et4CpvuiBeBeEBpLNDVK%2FDfuDbQLTD5VeAifPDgO4azzer1ZrqLtwGQF%2FZVmAnXMfA4SbXglWCEcoZCwqICpKklsJFW0%2FvzeugHdGse%2FOCTT3ubOg2sh9StRBNvxrfTDhi0UC9TT9XD2O7VgEf0fhlWniBSGcu6wg2cSPhSvjmYa8QDuSIK05RZwnns89ZHlOUFgtgM74bwTcMNb67bwGOqUB%2BCPyC90XTcACJUT8Ygeg5w6xzBMzo4Z%2BFYHYL9n5w3p%2FpPIvW2E5ck2j10qky8zc%2Bm9uoMR13g42643SgSudCnEnhpVc%2FKxocA9plWQ1qqmtCMSH0zMsvGIuPo8CXIRzP%2BiUYK0f3wTPbskQISxyVLlwQ1f5%2FehPXipJEuwFE%2B4Z64PClCEOty6IPcvCReRQJT0YGVbO8Su4Gt%2F4UcjQwouUZGaW&X-Amz-Signature=9ed5357db27f8a18bb66b6fc4943236f780d29b5384942ea5c9488a1068c85e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RX6I5RCO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BnDtBgPQm2Ce7UqZdppFdESvWUHAYZSHYf2BrSnwRYAIgbxSVja%2Bp8cZKbGU3jAs4u6AluIEkVrq5LZc2KFeEG6kqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBILsNGdqHCmVcQpIyrcA%2BERGR4L1pxcWltVMO8D49GayyOiV0T48wem6eetPMxtLMlMy3SUkTIrKOphmcwa7liaamVdbsrxuhrBN0Nvd%2FYpwaFnDm5wTtCkrB98IgIn3grNBbbD8vjUmX3q6WUG4ooM4bd9%2Bd7Q0nhwS069fxbA95tDZWm0jXkhvSLnD50HVNwHXn9TloAEbLq2GnZS3R1I77%2Bj%2BsZTn9X9R8mE2rOX%2BiGMoMFd1JZKjjK%2Ffu7gYj0I0NvaXSMLKG900YVHMHDcKlGvxH3%2FN7VgP%2BuABGs%2FPLmnq4XmG6HQDgE84f6RByOCyp7wGIagvu6bV9TXVjjXC807KMrxi%2FZg%2Bd0w33DEGkkqwXuIzZaC449etTpfMaSQtB0Ykp%2BHrINpqYVILxvofWfFNo7fFNbO4t6FuG%2FtsmS2dvrHDGQcsm9l5%2FRu%2Bw3Et4CpvuiBeBeEBpLNDVK%2FDfuDbQLTD5VeAifPDgO4azzer1ZrqLtwGQF%2FZVmAnXMfA4SbXglWCEcoZCwqICpKklsJFW0%2FvzeugHdGse%2FOCTT3ubOg2sh9StRBNvxrfTDhi0UC9TT9XD2O7VgEf0fhlWniBSGcu6wg2cSPhSvjmYa8QDuSIK05RZwnns89ZHlOUFgtgM74bwTcMNb67bwGOqUB%2BCPyC90XTcACJUT8Ygeg5w6xzBMzo4Z%2BFYHYL9n5w3p%2FpPIvW2E5ck2j10qky8zc%2Bm9uoMR13g42643SgSudCnEnhpVc%2FKxocA9plWQ1qqmtCMSH0zMsvGIuPo8CXIRzP%2BiUYK0f3wTPbskQISxyVLlwQ1f5%2FehPXipJEuwFE%2B4Z64PClCEOty6IPcvCReRQJT0YGVbO8Su4Gt%2F4UcjQwouUZGaW&X-Amz-Signature=71f72075aa06a27e6740d517a3247d52a5aac3aeb1f4b3f4cbe9b102618cb0d4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
