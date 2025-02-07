

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWYCSSM2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCICinNvIF0vGxoRQTJ3%2FLVo0R%2ByEy2r8YiwnjZItMAFtoAiEA7rlNyeBc1k%2Fc3SwhmsR02cRtrgGEF40H%2BJaSGJArC%2Bwq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDC8rVRSRZ%2BwkOE%2BEQSrcAwyCGTaA7yZFzWKgyRoSUQILb8P5zPw1b1x4PMYOuoKm2YI%2FaMj6Rb7a1gkb13HcobYhPGb1s1J42eLOaQsEwCu5dY9m6r9qQq9eEpgMWsqbxtkWeY%2BYH9R26tyv0%2BqgDwxDBFD%2F%2B55RMCANct7NNTBf71kap53k63j7Cx5MXlynARpVwmc9np14LD6JCUBdrbblYy4BD0ITyYdEBdnjah8WlyZJIsYATjIwAXk7B%2FgmT0MZk9ldFc%2F%2B3685PRekz6chnMHpd3qzVsOl4N8%2B28VGCOscP%2BZdOfKe5Zfj7NiMzcMcZS1Z%2B8D1%2F2Zyrt4fmBTl%2Fqhsz1RoG9MvoqVd1Y1uPh435OH81EUL7JQs9Hgwq0JavBykuiUiHTIGdv0c%2FaPSFwVJnTngev7B7jFsSDaOrtRshJXcrDUb6%2FJq8hEf1%2B5jZlLdeZxYsCJvno77NA5vAtq5aXZInXRpNnB9R7pM5GIsCCX%2BAkA0Dfu%2F3m6Hz6i3jprZlmydXvSXYcfLaX1qZiJ9PtvqJul2DRZgpjI3uqiSSwty8fKzAQJLV%2FKUPdEfAUtMWeFaL91r8N4wPJzVFvt22pvh689uESiJV0gFAkETJB8wqsABvJR8DSVejLZW6r4mzdDkQ9dnMMCZmb0GOqUBUIbpsGK7hDRiVTl9pdEIgazsZnreccZZE%2F3sYZ0p2YIywGrSABVvqYyyZ%2FHmP3WkmSRL%2FpE4%2BSbIlfYee6eekU3YS4B0kuQY47NCPGnd5nboFya7Gb%2FweHpDErOTKX7Gq79ZhKpYHWeYkTWoKEgAv0tLfZRW3nmJUL72F0quwaL5USi1StunjYP0GwYmGdTnutzI4lZLjGP6aVaaRmbSokDFq5oS&X-Amz-Signature=b9e69c89c74f90b87c67f7c7a8010215014a501487ae999a69d8c11290825785&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWYCSSM2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCICinNvIF0vGxoRQTJ3%2FLVo0R%2ByEy2r8YiwnjZItMAFtoAiEA7rlNyeBc1k%2Fc3SwhmsR02cRtrgGEF40H%2BJaSGJArC%2Bwq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDC8rVRSRZ%2BwkOE%2BEQSrcAwyCGTaA7yZFzWKgyRoSUQILb8P5zPw1b1x4PMYOuoKm2YI%2FaMj6Rb7a1gkb13HcobYhPGb1s1J42eLOaQsEwCu5dY9m6r9qQq9eEpgMWsqbxtkWeY%2BYH9R26tyv0%2BqgDwxDBFD%2F%2B55RMCANct7NNTBf71kap53k63j7Cx5MXlynARpVwmc9np14LD6JCUBdrbblYy4BD0ITyYdEBdnjah8WlyZJIsYATjIwAXk7B%2FgmT0MZk9ldFc%2F%2B3685PRekz6chnMHpd3qzVsOl4N8%2B28VGCOscP%2BZdOfKe5Zfj7NiMzcMcZS1Z%2B8D1%2F2Zyrt4fmBTl%2Fqhsz1RoG9MvoqVd1Y1uPh435OH81EUL7JQs9Hgwq0JavBykuiUiHTIGdv0c%2FaPSFwVJnTngev7B7jFsSDaOrtRshJXcrDUb6%2FJq8hEf1%2B5jZlLdeZxYsCJvno77NA5vAtq5aXZInXRpNnB9R7pM5GIsCCX%2BAkA0Dfu%2F3m6Hz6i3jprZlmydXvSXYcfLaX1qZiJ9PtvqJul2DRZgpjI3uqiSSwty8fKzAQJLV%2FKUPdEfAUtMWeFaL91r8N4wPJzVFvt22pvh689uESiJV0gFAkETJB8wqsABvJR8DSVejLZW6r4mzdDkQ9dnMMCZmb0GOqUBUIbpsGK7hDRiVTl9pdEIgazsZnreccZZE%2F3sYZ0p2YIywGrSABVvqYyyZ%2FHmP3WkmSRL%2FpE4%2BSbIlfYee6eekU3YS4B0kuQY47NCPGnd5nboFya7Gb%2FweHpDErOTKX7Gq79ZhKpYHWeYkTWoKEgAv0tLfZRW3nmJUL72F0quwaL5USi1StunjYP0GwYmGdTnutzI4lZLjGP6aVaaRmbSokDFq5oS&X-Amz-Signature=ee4cf6cb8bbe29a15f6925f05a586e05175095640ca82a7d08aafc4431b56473&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWYCSSM2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCICinNvIF0vGxoRQTJ3%2FLVo0R%2ByEy2r8YiwnjZItMAFtoAiEA7rlNyeBc1k%2Fc3SwhmsR02cRtrgGEF40H%2BJaSGJArC%2Bwq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDC8rVRSRZ%2BwkOE%2BEQSrcAwyCGTaA7yZFzWKgyRoSUQILb8P5zPw1b1x4PMYOuoKm2YI%2FaMj6Rb7a1gkb13HcobYhPGb1s1J42eLOaQsEwCu5dY9m6r9qQq9eEpgMWsqbxtkWeY%2BYH9R26tyv0%2BqgDwxDBFD%2F%2B55RMCANct7NNTBf71kap53k63j7Cx5MXlynARpVwmc9np14LD6JCUBdrbblYy4BD0ITyYdEBdnjah8WlyZJIsYATjIwAXk7B%2FgmT0MZk9ldFc%2F%2B3685PRekz6chnMHpd3qzVsOl4N8%2B28VGCOscP%2BZdOfKe5Zfj7NiMzcMcZS1Z%2B8D1%2F2Zyrt4fmBTl%2Fqhsz1RoG9MvoqVd1Y1uPh435OH81EUL7JQs9Hgwq0JavBykuiUiHTIGdv0c%2FaPSFwVJnTngev7B7jFsSDaOrtRshJXcrDUb6%2FJq8hEf1%2B5jZlLdeZxYsCJvno77NA5vAtq5aXZInXRpNnB9R7pM5GIsCCX%2BAkA0Dfu%2F3m6Hz6i3jprZlmydXvSXYcfLaX1qZiJ9PtvqJul2DRZgpjI3uqiSSwty8fKzAQJLV%2FKUPdEfAUtMWeFaL91r8N4wPJzVFvt22pvh689uESiJV0gFAkETJB8wqsABvJR8DSVejLZW6r4mzdDkQ9dnMMCZmb0GOqUBUIbpsGK7hDRiVTl9pdEIgazsZnreccZZE%2F3sYZ0p2YIywGrSABVvqYyyZ%2FHmP3WkmSRL%2FpE4%2BSbIlfYee6eekU3YS4B0kuQY47NCPGnd5nboFya7Gb%2FweHpDErOTKX7Gq79ZhKpYHWeYkTWoKEgAv0tLfZRW3nmJUL72F0quwaL5USi1StunjYP0GwYmGdTnutzI4lZLjGP6aVaaRmbSokDFq5oS&X-Amz-Signature=cdcc90231a7e51626fa1b5a95122bbd14e4ae80309b18faaed2afd81db06543d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWYCSSM2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCICinNvIF0vGxoRQTJ3%2FLVo0R%2ByEy2r8YiwnjZItMAFtoAiEA7rlNyeBc1k%2Fc3SwhmsR02cRtrgGEF40H%2BJaSGJArC%2Bwq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDC8rVRSRZ%2BwkOE%2BEQSrcAwyCGTaA7yZFzWKgyRoSUQILb8P5zPw1b1x4PMYOuoKm2YI%2FaMj6Rb7a1gkb13HcobYhPGb1s1J42eLOaQsEwCu5dY9m6r9qQq9eEpgMWsqbxtkWeY%2BYH9R26tyv0%2BqgDwxDBFD%2F%2B55RMCANct7NNTBf71kap53k63j7Cx5MXlynARpVwmc9np14LD6JCUBdrbblYy4BD0ITyYdEBdnjah8WlyZJIsYATjIwAXk7B%2FgmT0MZk9ldFc%2F%2B3685PRekz6chnMHpd3qzVsOl4N8%2B28VGCOscP%2BZdOfKe5Zfj7NiMzcMcZS1Z%2B8D1%2F2Zyrt4fmBTl%2Fqhsz1RoG9MvoqVd1Y1uPh435OH81EUL7JQs9Hgwq0JavBykuiUiHTIGdv0c%2FaPSFwVJnTngev7B7jFsSDaOrtRshJXcrDUb6%2FJq8hEf1%2B5jZlLdeZxYsCJvno77NA5vAtq5aXZInXRpNnB9R7pM5GIsCCX%2BAkA0Dfu%2F3m6Hz6i3jprZlmydXvSXYcfLaX1qZiJ9PtvqJul2DRZgpjI3uqiSSwty8fKzAQJLV%2FKUPdEfAUtMWeFaL91r8N4wPJzVFvt22pvh689uESiJV0gFAkETJB8wqsABvJR8DSVejLZW6r4mzdDkQ9dnMMCZmb0GOqUBUIbpsGK7hDRiVTl9pdEIgazsZnreccZZE%2F3sYZ0p2YIywGrSABVvqYyyZ%2FHmP3WkmSRL%2FpE4%2BSbIlfYee6eekU3YS4B0kuQY47NCPGnd5nboFya7Gb%2FweHpDErOTKX7Gq79ZhKpYHWeYkTWoKEgAv0tLfZRW3nmJUL72F0quwaL5USi1StunjYP0GwYmGdTnutzI4lZLjGP6aVaaRmbSokDFq5oS&X-Amz-Signature=1a51a57e04ae29e87a3c74dc774a8ea17e2ff2ce17968d2d34861c272ea7e671&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWYCSSM2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCICinNvIF0vGxoRQTJ3%2FLVo0R%2ByEy2r8YiwnjZItMAFtoAiEA7rlNyeBc1k%2Fc3SwhmsR02cRtrgGEF40H%2BJaSGJArC%2Bwq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDC8rVRSRZ%2BwkOE%2BEQSrcAwyCGTaA7yZFzWKgyRoSUQILb8P5zPw1b1x4PMYOuoKm2YI%2FaMj6Rb7a1gkb13HcobYhPGb1s1J42eLOaQsEwCu5dY9m6r9qQq9eEpgMWsqbxtkWeY%2BYH9R26tyv0%2BqgDwxDBFD%2F%2B55RMCANct7NNTBf71kap53k63j7Cx5MXlynARpVwmc9np14LD6JCUBdrbblYy4BD0ITyYdEBdnjah8WlyZJIsYATjIwAXk7B%2FgmT0MZk9ldFc%2F%2B3685PRekz6chnMHpd3qzVsOl4N8%2B28VGCOscP%2BZdOfKe5Zfj7NiMzcMcZS1Z%2B8D1%2F2Zyrt4fmBTl%2Fqhsz1RoG9MvoqVd1Y1uPh435OH81EUL7JQs9Hgwq0JavBykuiUiHTIGdv0c%2FaPSFwVJnTngev7B7jFsSDaOrtRshJXcrDUb6%2FJq8hEf1%2B5jZlLdeZxYsCJvno77NA5vAtq5aXZInXRpNnB9R7pM5GIsCCX%2BAkA0Dfu%2F3m6Hz6i3jprZlmydXvSXYcfLaX1qZiJ9PtvqJul2DRZgpjI3uqiSSwty8fKzAQJLV%2FKUPdEfAUtMWeFaL91r8N4wPJzVFvt22pvh689uESiJV0gFAkETJB8wqsABvJR8DSVejLZW6r4mzdDkQ9dnMMCZmb0GOqUBUIbpsGK7hDRiVTl9pdEIgazsZnreccZZE%2F3sYZ0p2YIywGrSABVvqYyyZ%2FHmP3WkmSRL%2FpE4%2BSbIlfYee6eekU3YS4B0kuQY47NCPGnd5nboFya7Gb%2FweHpDErOTKX7Gq79ZhKpYHWeYkTWoKEgAv0tLfZRW3nmJUL72F0quwaL5USi1StunjYP0GwYmGdTnutzI4lZLjGP6aVaaRmbSokDFq5oS&X-Amz-Signature=7dcae28d5b048ae2334d58c25b0dbacd73ec1ead51ad356087c64ede04f560e1&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWYCSSM2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCICinNvIF0vGxoRQTJ3%2FLVo0R%2ByEy2r8YiwnjZItMAFtoAiEA7rlNyeBc1k%2Fc3SwhmsR02cRtrgGEF40H%2BJaSGJArC%2Bwq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDC8rVRSRZ%2BwkOE%2BEQSrcAwyCGTaA7yZFzWKgyRoSUQILb8P5zPw1b1x4PMYOuoKm2YI%2FaMj6Rb7a1gkb13HcobYhPGb1s1J42eLOaQsEwCu5dY9m6r9qQq9eEpgMWsqbxtkWeY%2BYH9R26tyv0%2BqgDwxDBFD%2F%2B55RMCANct7NNTBf71kap53k63j7Cx5MXlynARpVwmc9np14LD6JCUBdrbblYy4BD0ITyYdEBdnjah8WlyZJIsYATjIwAXk7B%2FgmT0MZk9ldFc%2F%2B3685PRekz6chnMHpd3qzVsOl4N8%2B28VGCOscP%2BZdOfKe5Zfj7NiMzcMcZS1Z%2B8D1%2F2Zyrt4fmBTl%2Fqhsz1RoG9MvoqVd1Y1uPh435OH81EUL7JQs9Hgwq0JavBykuiUiHTIGdv0c%2FaPSFwVJnTngev7B7jFsSDaOrtRshJXcrDUb6%2FJq8hEf1%2B5jZlLdeZxYsCJvno77NA5vAtq5aXZInXRpNnB9R7pM5GIsCCX%2BAkA0Dfu%2F3m6Hz6i3jprZlmydXvSXYcfLaX1qZiJ9PtvqJul2DRZgpjI3uqiSSwty8fKzAQJLV%2FKUPdEfAUtMWeFaL91r8N4wPJzVFvt22pvh689uESiJV0gFAkETJB8wqsABvJR8DSVejLZW6r4mzdDkQ9dnMMCZmb0GOqUBUIbpsGK7hDRiVTl9pdEIgazsZnreccZZE%2F3sYZ0p2YIywGrSABVvqYyyZ%2FHmP3WkmSRL%2FpE4%2BSbIlfYee6eekU3YS4B0kuQY47NCPGnd5nboFya7Gb%2FweHpDErOTKX7Gq79ZhKpYHWeYkTWoKEgAv0tLfZRW3nmJUL72F0quwaL5USi1StunjYP0GwYmGdTnutzI4lZLjGP6aVaaRmbSokDFq5oS&X-Amz-Signature=a9cd3acc0a3511c933f30a4ffbf7b903e33bdf76b998a32a5027d40adda82086&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWYCSSM2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCICinNvIF0vGxoRQTJ3%2FLVo0R%2ByEy2r8YiwnjZItMAFtoAiEA7rlNyeBc1k%2Fc3SwhmsR02cRtrgGEF40H%2BJaSGJArC%2Bwq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDC8rVRSRZ%2BwkOE%2BEQSrcAwyCGTaA7yZFzWKgyRoSUQILb8P5zPw1b1x4PMYOuoKm2YI%2FaMj6Rb7a1gkb13HcobYhPGb1s1J42eLOaQsEwCu5dY9m6r9qQq9eEpgMWsqbxtkWeY%2BYH9R26tyv0%2BqgDwxDBFD%2F%2B55RMCANct7NNTBf71kap53k63j7Cx5MXlynARpVwmc9np14LD6JCUBdrbblYy4BD0ITyYdEBdnjah8WlyZJIsYATjIwAXk7B%2FgmT0MZk9ldFc%2F%2B3685PRekz6chnMHpd3qzVsOl4N8%2B28VGCOscP%2BZdOfKe5Zfj7NiMzcMcZS1Z%2B8D1%2F2Zyrt4fmBTl%2Fqhsz1RoG9MvoqVd1Y1uPh435OH81EUL7JQs9Hgwq0JavBykuiUiHTIGdv0c%2FaPSFwVJnTngev7B7jFsSDaOrtRshJXcrDUb6%2FJq8hEf1%2B5jZlLdeZxYsCJvno77NA5vAtq5aXZInXRpNnB9R7pM5GIsCCX%2BAkA0Dfu%2F3m6Hz6i3jprZlmydXvSXYcfLaX1qZiJ9PtvqJul2DRZgpjI3uqiSSwty8fKzAQJLV%2FKUPdEfAUtMWeFaL91r8N4wPJzVFvt22pvh689uESiJV0gFAkETJB8wqsABvJR8DSVejLZW6r4mzdDkQ9dnMMCZmb0GOqUBUIbpsGK7hDRiVTl9pdEIgazsZnreccZZE%2F3sYZ0p2YIywGrSABVvqYyyZ%2FHmP3WkmSRL%2FpE4%2BSbIlfYee6eekU3YS4B0kuQY47NCPGnd5nboFya7Gb%2FweHpDErOTKX7Gq79ZhKpYHWeYkTWoKEgAv0tLfZRW3nmJUL72F0quwaL5USi1StunjYP0GwYmGdTnutzI4lZLjGP6aVaaRmbSokDFq5oS&X-Amz-Signature=e1204132aba34bec036e65a26743e0b8bc5667407ae646c8a71762b2bf3d43d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWYCSSM2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCICinNvIF0vGxoRQTJ3%2FLVo0R%2ByEy2r8YiwnjZItMAFtoAiEA7rlNyeBc1k%2Fc3SwhmsR02cRtrgGEF40H%2BJaSGJArC%2Bwq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDC8rVRSRZ%2BwkOE%2BEQSrcAwyCGTaA7yZFzWKgyRoSUQILb8P5zPw1b1x4PMYOuoKm2YI%2FaMj6Rb7a1gkb13HcobYhPGb1s1J42eLOaQsEwCu5dY9m6r9qQq9eEpgMWsqbxtkWeY%2BYH9R26tyv0%2BqgDwxDBFD%2F%2B55RMCANct7NNTBf71kap53k63j7Cx5MXlynARpVwmc9np14LD6JCUBdrbblYy4BD0ITyYdEBdnjah8WlyZJIsYATjIwAXk7B%2FgmT0MZk9ldFc%2F%2B3685PRekz6chnMHpd3qzVsOl4N8%2B28VGCOscP%2BZdOfKe5Zfj7NiMzcMcZS1Z%2B8D1%2F2Zyrt4fmBTl%2Fqhsz1RoG9MvoqVd1Y1uPh435OH81EUL7JQs9Hgwq0JavBykuiUiHTIGdv0c%2FaPSFwVJnTngev7B7jFsSDaOrtRshJXcrDUb6%2FJq8hEf1%2B5jZlLdeZxYsCJvno77NA5vAtq5aXZInXRpNnB9R7pM5GIsCCX%2BAkA0Dfu%2F3m6Hz6i3jprZlmydXvSXYcfLaX1qZiJ9PtvqJul2DRZgpjI3uqiSSwty8fKzAQJLV%2FKUPdEfAUtMWeFaL91r8N4wPJzVFvt22pvh689uESiJV0gFAkETJB8wqsABvJR8DSVejLZW6r4mzdDkQ9dnMMCZmb0GOqUBUIbpsGK7hDRiVTl9pdEIgazsZnreccZZE%2F3sYZ0p2YIywGrSABVvqYyyZ%2FHmP3WkmSRL%2FpE4%2BSbIlfYee6eekU3YS4B0kuQY47NCPGnd5nboFya7Gb%2FweHpDErOTKX7Gq79ZhKpYHWeYkTWoKEgAv0tLfZRW3nmJUL72F0quwaL5USi1StunjYP0GwYmGdTnutzI4lZLjGP6aVaaRmbSokDFq5oS&X-Amz-Signature=f9c2375569233ad39a9dfdaba110e42f960c33c6f5a2487151f60f51f2a841ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWYCSSM2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCICinNvIF0vGxoRQTJ3%2FLVo0R%2ByEy2r8YiwnjZItMAFtoAiEA7rlNyeBc1k%2Fc3SwhmsR02cRtrgGEF40H%2BJaSGJArC%2Bwq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDC8rVRSRZ%2BwkOE%2BEQSrcAwyCGTaA7yZFzWKgyRoSUQILb8P5zPw1b1x4PMYOuoKm2YI%2FaMj6Rb7a1gkb13HcobYhPGb1s1J42eLOaQsEwCu5dY9m6r9qQq9eEpgMWsqbxtkWeY%2BYH9R26tyv0%2BqgDwxDBFD%2F%2B55RMCANct7NNTBf71kap53k63j7Cx5MXlynARpVwmc9np14LD6JCUBdrbblYy4BD0ITyYdEBdnjah8WlyZJIsYATjIwAXk7B%2FgmT0MZk9ldFc%2F%2B3685PRekz6chnMHpd3qzVsOl4N8%2B28VGCOscP%2BZdOfKe5Zfj7NiMzcMcZS1Z%2B8D1%2F2Zyrt4fmBTl%2Fqhsz1RoG9MvoqVd1Y1uPh435OH81EUL7JQs9Hgwq0JavBykuiUiHTIGdv0c%2FaPSFwVJnTngev7B7jFsSDaOrtRshJXcrDUb6%2FJq8hEf1%2B5jZlLdeZxYsCJvno77NA5vAtq5aXZInXRpNnB9R7pM5GIsCCX%2BAkA0Dfu%2F3m6Hz6i3jprZlmydXvSXYcfLaX1qZiJ9PtvqJul2DRZgpjI3uqiSSwty8fKzAQJLV%2FKUPdEfAUtMWeFaL91r8N4wPJzVFvt22pvh689uESiJV0gFAkETJB8wqsABvJR8DSVejLZW6r4mzdDkQ9dnMMCZmb0GOqUBUIbpsGK7hDRiVTl9pdEIgazsZnreccZZE%2F3sYZ0p2YIywGrSABVvqYyyZ%2FHmP3WkmSRL%2FpE4%2BSbIlfYee6eekU3YS4B0kuQY47NCPGnd5nboFya7Gb%2FweHpDErOTKX7Gq79ZhKpYHWeYkTWoKEgAv0tLfZRW3nmJUL72F0quwaL5USi1StunjYP0GwYmGdTnutzI4lZLjGP6aVaaRmbSokDFq5oS&X-Amz-Signature=58fc94dcfa2b0a6a35f55fec1f54368e477e863adc276cd470602541a942ef9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TU4RS7FU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIDS04t2w2%2Bc4Pvsbk9F1SdzRCkP%2BW5YgFfLgn8TOR3LFAiArQUPm2%2Bk4rxZtE33f4HjvHTGtyPFRnaicAUknqrRpnir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMJ07GUoU8hdZFSGoxKtwDiVEyIoBBq3ZPoPym9EwOAwolz1NxWMtFSmluhNRcFJeGMtiCAQU4MdJkw%2BL4S4Jpa6cZy0y2ND2Q89CprVxyXrjXZ1X5REPyr4m8x1WZZbi5kztVmWeVlp5zABCMA7lOYrcok%2B2ptonV%2BhzqNIJLjeDOhOkW2GJzs3dodkEkDSqHOGTrE3LczZcljlowWoBT9YvpyWZP1ceBmFBDHOtCXopJf%2F3PbSOVnZfnJP4R6L%2FGXWwcMq6rY%2B3Bz%2FhkdYAYvqFw3rkCApXOBu5r8IscWCsp1OsRJVcKwEx49QsvGCn3fiBoZWHO%2FqFJfSe%2FJkO2oL06E0MBEuNa32faR7PcxU9hP%2Fe6jrZUp7rMe%2FXdals0sMQII2oBKU88fOkDrCtQI4%2FtKMhSpr4nzT5bn5t84r7i%2BgSlxWO96jenKeiVo3F0jiKnWry7eN81txgvJ3XV7nwWH3P0zvnN72y9HpnXHJb35KA1hdgTtoYN0iqMvE11hzuFKfDDJNGxPF3hth56AbyFF83jVT2NzC0lxrgCwKR73oRZWxg6G3ae9f5jjErsCSzv6mUvshSiiyhFi1WK0piDf4YCKcdEW7jgiH36eT9%2FTylJRQaWDV788fpvU%2BXRLdCpB3EBc0LDMugw5pmZvQY6pgF%2FUS099SpcZfHRKyV4JK%2BLKEMV79kK9M8%2B1ke3w3ahw41YoU3k70O3ISEj2x5ClXZLf%2BbFbktE2SOksaJ4eZ929sgKJ5AMgAqWllmVrqXoZXj8PfiYtNlX7orjPY4kW6BBt13Y6fcKmUwocLVYKVwe39MSq9rKxGQJ%2FECritTDgn3WpKMeofYD8YN4k%2B12ncoE7DdI1%2FHCyVIPb3pKlwiJMrNBYDbl&X-Amz-Signature=9babe4e844e3ff975e4eeb45a9d67aa3ce83b4ed74059751204d2eebcbe2d049&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TU4RS7FU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIDS04t2w2%2Bc4Pvsbk9F1SdzRCkP%2BW5YgFfLgn8TOR3LFAiArQUPm2%2Bk4rxZtE33f4HjvHTGtyPFRnaicAUknqrRpnir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMJ07GUoU8hdZFSGoxKtwDiVEyIoBBq3ZPoPym9EwOAwolz1NxWMtFSmluhNRcFJeGMtiCAQU4MdJkw%2BL4S4Jpa6cZy0y2ND2Q89CprVxyXrjXZ1X5REPyr4m8x1WZZbi5kztVmWeVlp5zABCMA7lOYrcok%2B2ptonV%2BhzqNIJLjeDOhOkW2GJzs3dodkEkDSqHOGTrE3LczZcljlowWoBT9YvpyWZP1ceBmFBDHOtCXopJf%2F3PbSOVnZfnJP4R6L%2FGXWwcMq6rY%2B3Bz%2FhkdYAYvqFw3rkCApXOBu5r8IscWCsp1OsRJVcKwEx49QsvGCn3fiBoZWHO%2FqFJfSe%2FJkO2oL06E0MBEuNa32faR7PcxU9hP%2Fe6jrZUp7rMe%2FXdals0sMQII2oBKU88fOkDrCtQI4%2FtKMhSpr4nzT5bn5t84r7i%2BgSlxWO96jenKeiVo3F0jiKnWry7eN81txgvJ3XV7nwWH3P0zvnN72y9HpnXHJb35KA1hdgTtoYN0iqMvE11hzuFKfDDJNGxPF3hth56AbyFF83jVT2NzC0lxrgCwKR73oRZWxg6G3ae9f5jjErsCSzv6mUvshSiiyhFi1WK0piDf4YCKcdEW7jgiH36eT9%2FTylJRQaWDV788fpvU%2BXRLdCpB3EBc0LDMugw5pmZvQY6pgF%2FUS099SpcZfHRKyV4JK%2BLKEMV79kK9M8%2B1ke3w3ahw41YoU3k70O3ISEj2x5ClXZLf%2BbFbktE2SOksaJ4eZ929sgKJ5AMgAqWllmVrqXoZXj8PfiYtNlX7orjPY4kW6BBt13Y6fcKmUwocLVYKVwe39MSq9rKxGQJ%2FECritTDgn3WpKMeofYD8YN4k%2B12ncoE7DdI1%2FHCyVIPb3pKlwiJMrNBYDbl&X-Amz-Signature=96b083e3608103f085423bf58338c38ba3cfb1ef93f721ecd9e04ae97edbacc3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
