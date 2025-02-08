

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW5BXSFY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDTroFAG%2FQOOQkCWaA5A4oZAKYU6s5QsMnhq8P%2BqgObawIgE%2F%2FSZ%2BXPQ5KuMTFHnLZauB%2Bu7wu%2BnqMTTsszzU%2FTbxUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPtpgER1BspY5KwqwSrcA3IzqcIjAllxit%2BZPGIueEaKkFYmlf25pCm7dlZDqglFwQZriOF7HsP%2FHNYmisvmuJ8GeEWZeh71HBFPrOLPsJ4qShc%2BJr%2FRrTVJoZfhr7UvYnVeUC8HoywqErtFG9U6D75ym32gDWB7Vu1hTU21vSHWqktFjI%2FiX2UuEJReVnEVduHaBkG1qnpv2m1VPT8fPB1BSxeBlY1vFqRBv004BKrye6l6L3UsdaeIhQPX7HHgBSNc%2FUFP5NLKbjibSiToe0OpdVf6TeTuMNSrNtQbwDGHmdTF9bTLNgmTZLCwfBszeiNNZv9Ev5F1XjBxqIrLclRNWMSyUJeNLxrh3zakWTDIS0em40EUToz7yPZ1bCso9LTC%2FTihunbWvREXQ5zavSS0rn2If0lBK0s0x95Oyy2wUlfvnonZLmTeMRsg6XUrbdN0Egz2CWG2kkUDZs1CCJJg4NVRIlWRAIL%2FNWKzZCeu1pDBAk6u6M2sIKvY6vhReNl8b3uwu8CCbTmVrr9O2ewZhYzReFFpLTFi6JhMmk4B00nVaB9M%2FDqHTccMC%2BBPP8KpWmxnjmRoSWAG5jhEcbMpKSY6wWA8h5BnUb67jceu3991dVgyUosKMGHxA2F0Bocsq%2F4%2BUCP%2FuIIlMM6OnL0GOqUBFi6edlNQ8cIak1l%2BVOB2IL7jfOoL2HlFqPwTK7zeSDuq%2B5uF13wW2QojNdKo2uAWxxLAMCVqj2jLO4PpI1nZZsSU4RoDbNvWfp79QnsKKuVg8PB4zTFecniDPpPk8fZ5dZuds4zdCQKbYsmY8CLhEFqDwyDSsVUW5IB1MbQy2j0vO5s6FosQuP2so03JrYahrhvfSotV9CNCdw6dOHgKFAJKaqP7&X-Amz-Signature=35c9a76955976b3937010d3736bbee1c36704ac42f780e4d8b80a8f80b58e99d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW5BXSFY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDTroFAG%2FQOOQkCWaA5A4oZAKYU6s5QsMnhq8P%2BqgObawIgE%2F%2FSZ%2BXPQ5KuMTFHnLZauB%2Bu7wu%2BnqMTTsszzU%2FTbxUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPtpgER1BspY5KwqwSrcA3IzqcIjAllxit%2BZPGIueEaKkFYmlf25pCm7dlZDqglFwQZriOF7HsP%2FHNYmisvmuJ8GeEWZeh71HBFPrOLPsJ4qShc%2BJr%2FRrTVJoZfhr7UvYnVeUC8HoywqErtFG9U6D75ym32gDWB7Vu1hTU21vSHWqktFjI%2FiX2UuEJReVnEVduHaBkG1qnpv2m1VPT8fPB1BSxeBlY1vFqRBv004BKrye6l6L3UsdaeIhQPX7HHgBSNc%2FUFP5NLKbjibSiToe0OpdVf6TeTuMNSrNtQbwDGHmdTF9bTLNgmTZLCwfBszeiNNZv9Ev5F1XjBxqIrLclRNWMSyUJeNLxrh3zakWTDIS0em40EUToz7yPZ1bCso9LTC%2FTihunbWvREXQ5zavSS0rn2If0lBK0s0x95Oyy2wUlfvnonZLmTeMRsg6XUrbdN0Egz2CWG2kkUDZs1CCJJg4NVRIlWRAIL%2FNWKzZCeu1pDBAk6u6M2sIKvY6vhReNl8b3uwu8CCbTmVrr9O2ewZhYzReFFpLTFi6JhMmk4B00nVaB9M%2FDqHTccMC%2BBPP8KpWmxnjmRoSWAG5jhEcbMpKSY6wWA8h5BnUb67jceu3991dVgyUosKMGHxA2F0Bocsq%2F4%2BUCP%2FuIIlMM6OnL0GOqUBFi6edlNQ8cIak1l%2BVOB2IL7jfOoL2HlFqPwTK7zeSDuq%2B5uF13wW2QojNdKo2uAWxxLAMCVqj2jLO4PpI1nZZsSU4RoDbNvWfp79QnsKKuVg8PB4zTFecniDPpPk8fZ5dZuds4zdCQKbYsmY8CLhEFqDwyDSsVUW5IB1MbQy2j0vO5s6FosQuP2so03JrYahrhvfSotV9CNCdw6dOHgKFAJKaqP7&X-Amz-Signature=a8f78a79475d170aaba23c79ca8d6a45240bab5715f60684a47f9077650a2924&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW5BXSFY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDTroFAG%2FQOOQkCWaA5A4oZAKYU6s5QsMnhq8P%2BqgObawIgE%2F%2FSZ%2BXPQ5KuMTFHnLZauB%2Bu7wu%2BnqMTTsszzU%2FTbxUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPtpgER1BspY5KwqwSrcA3IzqcIjAllxit%2BZPGIueEaKkFYmlf25pCm7dlZDqglFwQZriOF7HsP%2FHNYmisvmuJ8GeEWZeh71HBFPrOLPsJ4qShc%2BJr%2FRrTVJoZfhr7UvYnVeUC8HoywqErtFG9U6D75ym32gDWB7Vu1hTU21vSHWqktFjI%2FiX2UuEJReVnEVduHaBkG1qnpv2m1VPT8fPB1BSxeBlY1vFqRBv004BKrye6l6L3UsdaeIhQPX7HHgBSNc%2FUFP5NLKbjibSiToe0OpdVf6TeTuMNSrNtQbwDGHmdTF9bTLNgmTZLCwfBszeiNNZv9Ev5F1XjBxqIrLclRNWMSyUJeNLxrh3zakWTDIS0em40EUToz7yPZ1bCso9LTC%2FTihunbWvREXQ5zavSS0rn2If0lBK0s0x95Oyy2wUlfvnonZLmTeMRsg6XUrbdN0Egz2CWG2kkUDZs1CCJJg4NVRIlWRAIL%2FNWKzZCeu1pDBAk6u6M2sIKvY6vhReNl8b3uwu8CCbTmVrr9O2ewZhYzReFFpLTFi6JhMmk4B00nVaB9M%2FDqHTccMC%2BBPP8KpWmxnjmRoSWAG5jhEcbMpKSY6wWA8h5BnUb67jceu3991dVgyUosKMGHxA2F0Bocsq%2F4%2BUCP%2FuIIlMM6OnL0GOqUBFi6edlNQ8cIak1l%2BVOB2IL7jfOoL2HlFqPwTK7zeSDuq%2B5uF13wW2QojNdKo2uAWxxLAMCVqj2jLO4PpI1nZZsSU4RoDbNvWfp79QnsKKuVg8PB4zTFecniDPpPk8fZ5dZuds4zdCQKbYsmY8CLhEFqDwyDSsVUW5IB1MbQy2j0vO5s6FosQuP2so03JrYahrhvfSotV9CNCdw6dOHgKFAJKaqP7&X-Amz-Signature=c5774cb436a4288fc65710f0e2462aca8e4f14f9debbacc187a82e227a940fa1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW5BXSFY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDTroFAG%2FQOOQkCWaA5A4oZAKYU6s5QsMnhq8P%2BqgObawIgE%2F%2FSZ%2BXPQ5KuMTFHnLZauB%2Bu7wu%2BnqMTTsszzU%2FTbxUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPtpgER1BspY5KwqwSrcA3IzqcIjAllxit%2BZPGIueEaKkFYmlf25pCm7dlZDqglFwQZriOF7HsP%2FHNYmisvmuJ8GeEWZeh71HBFPrOLPsJ4qShc%2BJr%2FRrTVJoZfhr7UvYnVeUC8HoywqErtFG9U6D75ym32gDWB7Vu1hTU21vSHWqktFjI%2FiX2UuEJReVnEVduHaBkG1qnpv2m1VPT8fPB1BSxeBlY1vFqRBv004BKrye6l6L3UsdaeIhQPX7HHgBSNc%2FUFP5NLKbjibSiToe0OpdVf6TeTuMNSrNtQbwDGHmdTF9bTLNgmTZLCwfBszeiNNZv9Ev5F1XjBxqIrLclRNWMSyUJeNLxrh3zakWTDIS0em40EUToz7yPZ1bCso9LTC%2FTihunbWvREXQ5zavSS0rn2If0lBK0s0x95Oyy2wUlfvnonZLmTeMRsg6XUrbdN0Egz2CWG2kkUDZs1CCJJg4NVRIlWRAIL%2FNWKzZCeu1pDBAk6u6M2sIKvY6vhReNl8b3uwu8CCbTmVrr9O2ewZhYzReFFpLTFi6JhMmk4B00nVaB9M%2FDqHTccMC%2BBPP8KpWmxnjmRoSWAG5jhEcbMpKSY6wWA8h5BnUb67jceu3991dVgyUosKMGHxA2F0Bocsq%2F4%2BUCP%2FuIIlMM6OnL0GOqUBFi6edlNQ8cIak1l%2BVOB2IL7jfOoL2HlFqPwTK7zeSDuq%2B5uF13wW2QojNdKo2uAWxxLAMCVqj2jLO4PpI1nZZsSU4RoDbNvWfp79QnsKKuVg8PB4zTFecniDPpPk8fZ5dZuds4zdCQKbYsmY8CLhEFqDwyDSsVUW5IB1MbQy2j0vO5s6FosQuP2so03JrYahrhvfSotV9CNCdw6dOHgKFAJKaqP7&X-Amz-Signature=37f0a5b6984a28d62f0c759307e26e386023837b906b91bb7eadaf6686fa57c8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW5BXSFY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDTroFAG%2FQOOQkCWaA5A4oZAKYU6s5QsMnhq8P%2BqgObawIgE%2F%2FSZ%2BXPQ5KuMTFHnLZauB%2Bu7wu%2BnqMTTsszzU%2FTbxUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPtpgER1BspY5KwqwSrcA3IzqcIjAllxit%2BZPGIueEaKkFYmlf25pCm7dlZDqglFwQZriOF7HsP%2FHNYmisvmuJ8GeEWZeh71HBFPrOLPsJ4qShc%2BJr%2FRrTVJoZfhr7UvYnVeUC8HoywqErtFG9U6D75ym32gDWB7Vu1hTU21vSHWqktFjI%2FiX2UuEJReVnEVduHaBkG1qnpv2m1VPT8fPB1BSxeBlY1vFqRBv004BKrye6l6L3UsdaeIhQPX7HHgBSNc%2FUFP5NLKbjibSiToe0OpdVf6TeTuMNSrNtQbwDGHmdTF9bTLNgmTZLCwfBszeiNNZv9Ev5F1XjBxqIrLclRNWMSyUJeNLxrh3zakWTDIS0em40EUToz7yPZ1bCso9LTC%2FTihunbWvREXQ5zavSS0rn2If0lBK0s0x95Oyy2wUlfvnonZLmTeMRsg6XUrbdN0Egz2CWG2kkUDZs1CCJJg4NVRIlWRAIL%2FNWKzZCeu1pDBAk6u6M2sIKvY6vhReNl8b3uwu8CCbTmVrr9O2ewZhYzReFFpLTFi6JhMmk4B00nVaB9M%2FDqHTccMC%2BBPP8KpWmxnjmRoSWAG5jhEcbMpKSY6wWA8h5BnUb67jceu3991dVgyUosKMGHxA2F0Bocsq%2F4%2BUCP%2FuIIlMM6OnL0GOqUBFi6edlNQ8cIak1l%2BVOB2IL7jfOoL2HlFqPwTK7zeSDuq%2B5uF13wW2QojNdKo2uAWxxLAMCVqj2jLO4PpI1nZZsSU4RoDbNvWfp79QnsKKuVg8PB4zTFecniDPpPk8fZ5dZuds4zdCQKbYsmY8CLhEFqDwyDSsVUW5IB1MbQy2j0vO5s6FosQuP2so03JrYahrhvfSotV9CNCdw6dOHgKFAJKaqP7&X-Amz-Signature=c632eb3512e3c71aaefc52a6332500cc73658ad21f71217ee83c020c553b20ab&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW5BXSFY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDTroFAG%2FQOOQkCWaA5A4oZAKYU6s5QsMnhq8P%2BqgObawIgE%2F%2FSZ%2BXPQ5KuMTFHnLZauB%2Bu7wu%2BnqMTTsszzU%2FTbxUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPtpgER1BspY5KwqwSrcA3IzqcIjAllxit%2BZPGIueEaKkFYmlf25pCm7dlZDqglFwQZriOF7HsP%2FHNYmisvmuJ8GeEWZeh71HBFPrOLPsJ4qShc%2BJr%2FRrTVJoZfhr7UvYnVeUC8HoywqErtFG9U6D75ym32gDWB7Vu1hTU21vSHWqktFjI%2FiX2UuEJReVnEVduHaBkG1qnpv2m1VPT8fPB1BSxeBlY1vFqRBv004BKrye6l6L3UsdaeIhQPX7HHgBSNc%2FUFP5NLKbjibSiToe0OpdVf6TeTuMNSrNtQbwDGHmdTF9bTLNgmTZLCwfBszeiNNZv9Ev5F1XjBxqIrLclRNWMSyUJeNLxrh3zakWTDIS0em40EUToz7yPZ1bCso9LTC%2FTihunbWvREXQ5zavSS0rn2If0lBK0s0x95Oyy2wUlfvnonZLmTeMRsg6XUrbdN0Egz2CWG2kkUDZs1CCJJg4NVRIlWRAIL%2FNWKzZCeu1pDBAk6u6M2sIKvY6vhReNl8b3uwu8CCbTmVrr9O2ewZhYzReFFpLTFi6JhMmk4B00nVaB9M%2FDqHTccMC%2BBPP8KpWmxnjmRoSWAG5jhEcbMpKSY6wWA8h5BnUb67jceu3991dVgyUosKMGHxA2F0Bocsq%2F4%2BUCP%2FuIIlMM6OnL0GOqUBFi6edlNQ8cIak1l%2BVOB2IL7jfOoL2HlFqPwTK7zeSDuq%2B5uF13wW2QojNdKo2uAWxxLAMCVqj2jLO4PpI1nZZsSU4RoDbNvWfp79QnsKKuVg8PB4zTFecniDPpPk8fZ5dZuds4zdCQKbYsmY8CLhEFqDwyDSsVUW5IB1MbQy2j0vO5s6FosQuP2so03JrYahrhvfSotV9CNCdw6dOHgKFAJKaqP7&X-Amz-Signature=9d0038dc566f732f03a0562e10e97f025d4a0cd52148dbbe14aeb0b54392abf0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW5BXSFY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDTroFAG%2FQOOQkCWaA5A4oZAKYU6s5QsMnhq8P%2BqgObawIgE%2F%2FSZ%2BXPQ5KuMTFHnLZauB%2Bu7wu%2BnqMTTsszzU%2FTbxUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPtpgER1BspY5KwqwSrcA3IzqcIjAllxit%2BZPGIueEaKkFYmlf25pCm7dlZDqglFwQZriOF7HsP%2FHNYmisvmuJ8GeEWZeh71HBFPrOLPsJ4qShc%2BJr%2FRrTVJoZfhr7UvYnVeUC8HoywqErtFG9U6D75ym32gDWB7Vu1hTU21vSHWqktFjI%2FiX2UuEJReVnEVduHaBkG1qnpv2m1VPT8fPB1BSxeBlY1vFqRBv004BKrye6l6L3UsdaeIhQPX7HHgBSNc%2FUFP5NLKbjibSiToe0OpdVf6TeTuMNSrNtQbwDGHmdTF9bTLNgmTZLCwfBszeiNNZv9Ev5F1XjBxqIrLclRNWMSyUJeNLxrh3zakWTDIS0em40EUToz7yPZ1bCso9LTC%2FTihunbWvREXQ5zavSS0rn2If0lBK0s0x95Oyy2wUlfvnonZLmTeMRsg6XUrbdN0Egz2CWG2kkUDZs1CCJJg4NVRIlWRAIL%2FNWKzZCeu1pDBAk6u6M2sIKvY6vhReNl8b3uwu8CCbTmVrr9O2ewZhYzReFFpLTFi6JhMmk4B00nVaB9M%2FDqHTccMC%2BBPP8KpWmxnjmRoSWAG5jhEcbMpKSY6wWA8h5BnUb67jceu3991dVgyUosKMGHxA2F0Bocsq%2F4%2BUCP%2FuIIlMM6OnL0GOqUBFi6edlNQ8cIak1l%2BVOB2IL7jfOoL2HlFqPwTK7zeSDuq%2B5uF13wW2QojNdKo2uAWxxLAMCVqj2jLO4PpI1nZZsSU4RoDbNvWfp79QnsKKuVg8PB4zTFecniDPpPk8fZ5dZuds4zdCQKbYsmY8CLhEFqDwyDSsVUW5IB1MbQy2j0vO5s6FosQuP2so03JrYahrhvfSotV9CNCdw6dOHgKFAJKaqP7&X-Amz-Signature=a5c88e7649526cb18c529951962a7b9636fdf9e6ef8aafe368c6584bbd166e22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW5BXSFY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDTroFAG%2FQOOQkCWaA5A4oZAKYU6s5QsMnhq8P%2BqgObawIgE%2F%2FSZ%2BXPQ5KuMTFHnLZauB%2Bu7wu%2BnqMTTsszzU%2FTbxUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPtpgER1BspY5KwqwSrcA3IzqcIjAllxit%2BZPGIueEaKkFYmlf25pCm7dlZDqglFwQZriOF7HsP%2FHNYmisvmuJ8GeEWZeh71HBFPrOLPsJ4qShc%2BJr%2FRrTVJoZfhr7UvYnVeUC8HoywqErtFG9U6D75ym32gDWB7Vu1hTU21vSHWqktFjI%2FiX2UuEJReVnEVduHaBkG1qnpv2m1VPT8fPB1BSxeBlY1vFqRBv004BKrye6l6L3UsdaeIhQPX7HHgBSNc%2FUFP5NLKbjibSiToe0OpdVf6TeTuMNSrNtQbwDGHmdTF9bTLNgmTZLCwfBszeiNNZv9Ev5F1XjBxqIrLclRNWMSyUJeNLxrh3zakWTDIS0em40EUToz7yPZ1bCso9LTC%2FTihunbWvREXQ5zavSS0rn2If0lBK0s0x95Oyy2wUlfvnonZLmTeMRsg6XUrbdN0Egz2CWG2kkUDZs1CCJJg4NVRIlWRAIL%2FNWKzZCeu1pDBAk6u6M2sIKvY6vhReNl8b3uwu8CCbTmVrr9O2ewZhYzReFFpLTFi6JhMmk4B00nVaB9M%2FDqHTccMC%2BBPP8KpWmxnjmRoSWAG5jhEcbMpKSY6wWA8h5BnUb67jceu3991dVgyUosKMGHxA2F0Bocsq%2F4%2BUCP%2FuIIlMM6OnL0GOqUBFi6edlNQ8cIak1l%2BVOB2IL7jfOoL2HlFqPwTK7zeSDuq%2B5uF13wW2QojNdKo2uAWxxLAMCVqj2jLO4PpI1nZZsSU4RoDbNvWfp79QnsKKuVg8PB4zTFecniDPpPk8fZ5dZuds4zdCQKbYsmY8CLhEFqDwyDSsVUW5IB1MbQy2j0vO5s6FosQuP2so03JrYahrhvfSotV9CNCdw6dOHgKFAJKaqP7&X-Amz-Signature=b25b7c6c9a1f3e4df64db7d72478ba9e7a90aef4f9d253cd56d3edc59b4f2b08&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW5BXSFY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDTroFAG%2FQOOQkCWaA5A4oZAKYU6s5QsMnhq8P%2BqgObawIgE%2F%2FSZ%2BXPQ5KuMTFHnLZauB%2Bu7wu%2BnqMTTsszzU%2FTbxUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPtpgER1BspY5KwqwSrcA3IzqcIjAllxit%2BZPGIueEaKkFYmlf25pCm7dlZDqglFwQZriOF7HsP%2FHNYmisvmuJ8GeEWZeh71HBFPrOLPsJ4qShc%2BJr%2FRrTVJoZfhr7UvYnVeUC8HoywqErtFG9U6D75ym32gDWB7Vu1hTU21vSHWqktFjI%2FiX2UuEJReVnEVduHaBkG1qnpv2m1VPT8fPB1BSxeBlY1vFqRBv004BKrye6l6L3UsdaeIhQPX7HHgBSNc%2FUFP5NLKbjibSiToe0OpdVf6TeTuMNSrNtQbwDGHmdTF9bTLNgmTZLCwfBszeiNNZv9Ev5F1XjBxqIrLclRNWMSyUJeNLxrh3zakWTDIS0em40EUToz7yPZ1bCso9LTC%2FTihunbWvREXQ5zavSS0rn2If0lBK0s0x95Oyy2wUlfvnonZLmTeMRsg6XUrbdN0Egz2CWG2kkUDZs1CCJJg4NVRIlWRAIL%2FNWKzZCeu1pDBAk6u6M2sIKvY6vhReNl8b3uwu8CCbTmVrr9O2ewZhYzReFFpLTFi6JhMmk4B00nVaB9M%2FDqHTccMC%2BBPP8KpWmxnjmRoSWAG5jhEcbMpKSY6wWA8h5BnUb67jceu3991dVgyUosKMGHxA2F0Bocsq%2F4%2BUCP%2FuIIlMM6OnL0GOqUBFi6edlNQ8cIak1l%2BVOB2IL7jfOoL2HlFqPwTK7zeSDuq%2B5uF13wW2QojNdKo2uAWxxLAMCVqj2jLO4PpI1nZZsSU4RoDbNvWfp79QnsKKuVg8PB4zTFecniDPpPk8fZ5dZuds4zdCQKbYsmY8CLhEFqDwyDSsVUW5IB1MbQy2j0vO5s6FosQuP2so03JrYahrhvfSotV9CNCdw6dOHgKFAJKaqP7&X-Amz-Signature=b5be8113c9a08b2d00eadeb5fc287a9429fdc0b30797af7864f05319a6a095bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZQZLHG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIFJ5nfRqx1T92EWraIDPiX7Sm9sL8kRHtn3As61D7rRqAiATc5yTX8DMyZhakyoj4DPu1eMC3zWyAPw2gomr2P%2F%2F0SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BTyAH3zLLNlaC1siKtwDJK9J5xG5vG49OB2K9I%2BWGfI9QRDgNfa1b3IC9VRQ%2Fl%2F0%2BZFk8m4r8GMgzI%2FAm2hsqjR9dlk%2BU%2BTWJE8%2FrIrvuVze%2BQ9%2FWV3hWwRgQP8cl1R7qpQcMGi0dROoXbkuVG4Ac3pQ%2BlEm0UpSm6BFZUbLEDdtVl2ctD45CsaeOjFF9cQ07c4KB8wyaFQMV9gN3Bz1xG4BMxQeYaisNtiT8uEEZCG6HfVTwMwLk8%2FstpP%2B5hQugVoYzLo4cRcYM7B6ZlUXcfeK9kruRCJ1ZF8VksYdVeDoD43dofvXFby7ikxL4hqSjf0kg3h%2B4JWWEkTxoIK%2FPYSLr8UF9dMWtpTPOV3ixedU4bGYh%2FEKkTm7DoEYaNakIB1KhNAj4myOUsflE5vl87pptcztd3TmPUwmolMiIMrn2AtICE%2Fwf2XuN4xbS8rsruATKm3%2FEo0nfp08KF0HYSKecHVBy7ay%2FzKV5fdoq4tkBLKnoqeRZtXKGblO7vz8ApZNL6SLSc5p9J28AjeQeBp3KuvQw6OBtq9hOoR%2BeOX7PrfbKWwoO35XE4pMFGGR6WNNDXVX0yYS4yzFnmpfYp4aNvntn1o2avn%2BUDDt0%2Feg2ZPLRHs3KeDave0CyTzFFO5erzFZd1UmjrQw1Y6cvQY6pgH4sH6enPBr1r3ilEuJP0DtfGVjZhCevPLN%2BbNAK25bi8b0mLhPElv2lKFgMdW4fK%2BxbdV%2B%2BPDTG9rKRqhwhJg3kRzSacscAKE3MBGi%2FSUMTM4PpX1k%2B0CdvbkvEc3VFX%2F1UDZjKvYdMomjPG9jhgiVm4b3ZzuKMNR2XUoDqyjw1Px11TjF%2BbjrgdDX1XuXLvU2kSeGhH%2BniXoSdI0%2BXI2p5gjL6Wl3&X-Amz-Signature=7ee49e91932a35dea042bc6b0524e93f75cf970c730766da8d1e80d18cb14a9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZQZLHG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIFJ5nfRqx1T92EWraIDPiX7Sm9sL8kRHtn3As61D7rRqAiATc5yTX8DMyZhakyoj4DPu1eMC3zWyAPw2gomr2P%2F%2F0SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BTyAH3zLLNlaC1siKtwDJK9J5xG5vG49OB2K9I%2BWGfI9QRDgNfa1b3IC9VRQ%2Fl%2F0%2BZFk8m4r8GMgzI%2FAm2hsqjR9dlk%2BU%2BTWJE8%2FrIrvuVze%2BQ9%2FWV3hWwRgQP8cl1R7qpQcMGi0dROoXbkuVG4Ac3pQ%2BlEm0UpSm6BFZUbLEDdtVl2ctD45CsaeOjFF9cQ07c4KB8wyaFQMV9gN3Bz1xG4BMxQeYaisNtiT8uEEZCG6HfVTwMwLk8%2FstpP%2B5hQugVoYzLo4cRcYM7B6ZlUXcfeK9kruRCJ1ZF8VksYdVeDoD43dofvXFby7ikxL4hqSjf0kg3h%2B4JWWEkTxoIK%2FPYSLr8UF9dMWtpTPOV3ixedU4bGYh%2FEKkTm7DoEYaNakIB1KhNAj4myOUsflE5vl87pptcztd3TmPUwmolMiIMrn2AtICE%2Fwf2XuN4xbS8rsruATKm3%2FEo0nfp08KF0HYSKecHVBy7ay%2FzKV5fdoq4tkBLKnoqeRZtXKGblO7vz8ApZNL6SLSc5p9J28AjeQeBp3KuvQw6OBtq9hOoR%2BeOX7PrfbKWwoO35XE4pMFGGR6WNNDXVX0yYS4yzFnmpfYp4aNvntn1o2avn%2BUDDt0%2Feg2ZPLRHs3KeDave0CyTzFFO5erzFZd1UmjrQw1Y6cvQY6pgH4sH6enPBr1r3ilEuJP0DtfGVjZhCevPLN%2BbNAK25bi8b0mLhPElv2lKFgMdW4fK%2BxbdV%2B%2BPDTG9rKRqhwhJg3kRzSacscAKE3MBGi%2FSUMTM4PpX1k%2B0CdvbkvEc3VFX%2F1UDZjKvYdMomjPG9jhgiVm4b3ZzuKMNR2XUoDqyjw1Px11TjF%2BbjrgdDX1XuXLvU2kSeGhH%2BniXoSdI0%2BXI2p5gjL6Wl3&X-Amz-Signature=e2a4700e7aa4aead27e2b78a097793e1120008baad2cf0233b1e6dfe9234f500&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
