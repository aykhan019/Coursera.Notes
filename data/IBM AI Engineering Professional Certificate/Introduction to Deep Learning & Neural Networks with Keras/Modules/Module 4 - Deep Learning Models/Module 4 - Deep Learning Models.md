

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THP6F6CK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWVGOM0V5ER9iAlWaDMFdDvqS4P6ZLFEZQlZF%2BLbXtFQIhAIZT7bPOwShs%2FzJg3YHoIZGv%2BsJXBwi8i1lqQEvNGdkyKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igywh3AADi8%2B0LdfO7cq3AMWRXrzRsuKebZH8ny%2FrKAf9P1IkztVKW%2FkEINbTRgyRCA3Ky4k84Rjt7R9pHfUf%2BKhfHASYXPLR8UDMXYt%2BI3wgYsLyazmsnE%2FLhVUiuHUm3ylagCCo67WPJJdfV693U63ta54y7dNA%2FaUZ2D1ilkbPWKUt88uUKTfYYgkcS5jjmwlPPYXLEO4yswdJ9Os8ScXGHCcfOJH53s3xitxwMKhPPCYFkzd%2B%2FN9dHWB6ev%2FnhwpsNir8gfXNSshYsSFPdmEcCSZlM0sNyHA%2BqdgEPDOAC3k1l53n7D9RMVaWJnTn%2Bk57HU9jQ6tIqKk1bgzXfdPF6vXhnymLDbdEIyhlOO8udycI6qwCn0HSuYh8Web75Nq%2BWLoAGwturGYQ2qyWGkiS%2BsGh0%2BzTGVKbqI14r8hwEnSMCUWtzURB9wm2eY160T0Flou4leFJw4kXtTA%2B7zoefy64zdM8IdsUJZJLh77lAx8yeWIctNCdzlRSJ7L%2Bx43VknthylRYQdoPaWcp9zl2WyR3h0yRsSq4awBL9iVLN72CY%2BTtW5ScVGnZC2YXlVNYraP5Q7CYLhDWB4sRi5TBcw1QYiuw9lkmfA1vLD9L99wcXSC4aX0urGkhnVZv4zrmpDOpkZzX%2F%2B3pTDdpPe8BjqkAXIoJbHZ5Rx7gWHPDPJx%2Bx8jlPF9LWDqtsiLmW%2F6D2f6%2B2zIRfQCwvBcRehzkCD%2FIS%2Btt7bG%2BMik3OZRDyQX2ZoSrtTMKXTyE3xlGHorBk62zUdIiKJ7RliRJoBMBmmoGA3R9TxmVVs11SmowvtLxFPrl0ErmJcseD1H5LgMaoq1GuB9P3sTahy%2F9l7D2Nr7XAcyUOuVjWTGpAzTxwbpmRPH6Sk0&X-Amz-Signature=2f2c25a4d77b414debacc4fb5b3c8f5e7c6ce184cf70fb7faa3a39ba1fccda7c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THP6F6CK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWVGOM0V5ER9iAlWaDMFdDvqS4P6ZLFEZQlZF%2BLbXtFQIhAIZT7bPOwShs%2FzJg3YHoIZGv%2BsJXBwi8i1lqQEvNGdkyKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igywh3AADi8%2B0LdfO7cq3AMWRXrzRsuKebZH8ny%2FrKAf9P1IkztVKW%2FkEINbTRgyRCA3Ky4k84Rjt7R9pHfUf%2BKhfHASYXPLR8UDMXYt%2BI3wgYsLyazmsnE%2FLhVUiuHUm3ylagCCo67WPJJdfV693U63ta54y7dNA%2FaUZ2D1ilkbPWKUt88uUKTfYYgkcS5jjmwlPPYXLEO4yswdJ9Os8ScXGHCcfOJH53s3xitxwMKhPPCYFkzd%2B%2FN9dHWB6ev%2FnhwpsNir8gfXNSshYsSFPdmEcCSZlM0sNyHA%2BqdgEPDOAC3k1l53n7D9RMVaWJnTn%2Bk57HU9jQ6tIqKk1bgzXfdPF6vXhnymLDbdEIyhlOO8udycI6qwCn0HSuYh8Web75Nq%2BWLoAGwturGYQ2qyWGkiS%2BsGh0%2BzTGVKbqI14r8hwEnSMCUWtzURB9wm2eY160T0Flou4leFJw4kXtTA%2B7zoefy64zdM8IdsUJZJLh77lAx8yeWIctNCdzlRSJ7L%2Bx43VknthylRYQdoPaWcp9zl2WyR3h0yRsSq4awBL9iVLN72CY%2BTtW5ScVGnZC2YXlVNYraP5Q7CYLhDWB4sRi5TBcw1QYiuw9lkmfA1vLD9L99wcXSC4aX0urGkhnVZv4zrmpDOpkZzX%2F%2B3pTDdpPe8BjqkAXIoJbHZ5Rx7gWHPDPJx%2Bx8jlPF9LWDqtsiLmW%2F6D2f6%2B2zIRfQCwvBcRehzkCD%2FIS%2Btt7bG%2BMik3OZRDyQX2ZoSrtTMKXTyE3xlGHorBk62zUdIiKJ7RliRJoBMBmmoGA3R9TxmVVs11SmowvtLxFPrl0ErmJcseD1H5LgMaoq1GuB9P3sTahy%2F9l7D2Nr7XAcyUOuVjWTGpAzTxwbpmRPH6Sk0&X-Amz-Signature=a7181d975c03a86cdf476098cde5797df5579bba9b2465d0d78e0e2d1cce71b9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THP6F6CK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWVGOM0V5ER9iAlWaDMFdDvqS4P6ZLFEZQlZF%2BLbXtFQIhAIZT7bPOwShs%2FzJg3YHoIZGv%2BsJXBwi8i1lqQEvNGdkyKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igywh3AADi8%2B0LdfO7cq3AMWRXrzRsuKebZH8ny%2FrKAf9P1IkztVKW%2FkEINbTRgyRCA3Ky4k84Rjt7R9pHfUf%2BKhfHASYXPLR8UDMXYt%2BI3wgYsLyazmsnE%2FLhVUiuHUm3ylagCCo67WPJJdfV693U63ta54y7dNA%2FaUZ2D1ilkbPWKUt88uUKTfYYgkcS5jjmwlPPYXLEO4yswdJ9Os8ScXGHCcfOJH53s3xitxwMKhPPCYFkzd%2B%2FN9dHWB6ev%2FnhwpsNir8gfXNSshYsSFPdmEcCSZlM0sNyHA%2BqdgEPDOAC3k1l53n7D9RMVaWJnTn%2Bk57HU9jQ6tIqKk1bgzXfdPF6vXhnymLDbdEIyhlOO8udycI6qwCn0HSuYh8Web75Nq%2BWLoAGwturGYQ2qyWGkiS%2BsGh0%2BzTGVKbqI14r8hwEnSMCUWtzURB9wm2eY160T0Flou4leFJw4kXtTA%2B7zoefy64zdM8IdsUJZJLh77lAx8yeWIctNCdzlRSJ7L%2Bx43VknthylRYQdoPaWcp9zl2WyR3h0yRsSq4awBL9iVLN72CY%2BTtW5ScVGnZC2YXlVNYraP5Q7CYLhDWB4sRi5TBcw1QYiuw9lkmfA1vLD9L99wcXSC4aX0urGkhnVZv4zrmpDOpkZzX%2F%2B3pTDdpPe8BjqkAXIoJbHZ5Rx7gWHPDPJx%2Bx8jlPF9LWDqtsiLmW%2F6D2f6%2B2zIRfQCwvBcRehzkCD%2FIS%2Btt7bG%2BMik3OZRDyQX2ZoSrtTMKXTyE3xlGHorBk62zUdIiKJ7RliRJoBMBmmoGA3R9TxmVVs11SmowvtLxFPrl0ErmJcseD1H5LgMaoq1GuB9P3sTahy%2F9l7D2Nr7XAcyUOuVjWTGpAzTxwbpmRPH6Sk0&X-Amz-Signature=602ab48a2248c17bacecd8346a8b0d22a9cce49c78333701fb49b1f0b8704cd5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THP6F6CK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWVGOM0V5ER9iAlWaDMFdDvqS4P6ZLFEZQlZF%2BLbXtFQIhAIZT7bPOwShs%2FzJg3YHoIZGv%2BsJXBwi8i1lqQEvNGdkyKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igywh3AADi8%2B0LdfO7cq3AMWRXrzRsuKebZH8ny%2FrKAf9P1IkztVKW%2FkEINbTRgyRCA3Ky4k84Rjt7R9pHfUf%2BKhfHASYXPLR8UDMXYt%2BI3wgYsLyazmsnE%2FLhVUiuHUm3ylagCCo67WPJJdfV693U63ta54y7dNA%2FaUZ2D1ilkbPWKUt88uUKTfYYgkcS5jjmwlPPYXLEO4yswdJ9Os8ScXGHCcfOJH53s3xitxwMKhPPCYFkzd%2B%2FN9dHWB6ev%2FnhwpsNir8gfXNSshYsSFPdmEcCSZlM0sNyHA%2BqdgEPDOAC3k1l53n7D9RMVaWJnTn%2Bk57HU9jQ6tIqKk1bgzXfdPF6vXhnymLDbdEIyhlOO8udycI6qwCn0HSuYh8Web75Nq%2BWLoAGwturGYQ2qyWGkiS%2BsGh0%2BzTGVKbqI14r8hwEnSMCUWtzURB9wm2eY160T0Flou4leFJw4kXtTA%2B7zoefy64zdM8IdsUJZJLh77lAx8yeWIctNCdzlRSJ7L%2Bx43VknthylRYQdoPaWcp9zl2WyR3h0yRsSq4awBL9iVLN72CY%2BTtW5ScVGnZC2YXlVNYraP5Q7CYLhDWB4sRi5TBcw1QYiuw9lkmfA1vLD9L99wcXSC4aX0urGkhnVZv4zrmpDOpkZzX%2F%2B3pTDdpPe8BjqkAXIoJbHZ5Rx7gWHPDPJx%2Bx8jlPF9LWDqtsiLmW%2F6D2f6%2B2zIRfQCwvBcRehzkCD%2FIS%2Btt7bG%2BMik3OZRDyQX2ZoSrtTMKXTyE3xlGHorBk62zUdIiKJ7RliRJoBMBmmoGA3R9TxmVVs11SmowvtLxFPrl0ErmJcseD1H5LgMaoq1GuB9P3sTahy%2F9l7D2Nr7XAcyUOuVjWTGpAzTxwbpmRPH6Sk0&X-Amz-Signature=41e555ee80ec91871b341ef723cd6c53293256ca3cbce7bfd7063bd8c1636d60&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THP6F6CK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWVGOM0V5ER9iAlWaDMFdDvqS4P6ZLFEZQlZF%2BLbXtFQIhAIZT7bPOwShs%2FzJg3YHoIZGv%2BsJXBwi8i1lqQEvNGdkyKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igywh3AADi8%2B0LdfO7cq3AMWRXrzRsuKebZH8ny%2FrKAf9P1IkztVKW%2FkEINbTRgyRCA3Ky4k84Rjt7R9pHfUf%2BKhfHASYXPLR8UDMXYt%2BI3wgYsLyazmsnE%2FLhVUiuHUm3ylagCCo67WPJJdfV693U63ta54y7dNA%2FaUZ2D1ilkbPWKUt88uUKTfYYgkcS5jjmwlPPYXLEO4yswdJ9Os8ScXGHCcfOJH53s3xitxwMKhPPCYFkzd%2B%2FN9dHWB6ev%2FnhwpsNir8gfXNSshYsSFPdmEcCSZlM0sNyHA%2BqdgEPDOAC3k1l53n7D9RMVaWJnTn%2Bk57HU9jQ6tIqKk1bgzXfdPF6vXhnymLDbdEIyhlOO8udycI6qwCn0HSuYh8Web75Nq%2BWLoAGwturGYQ2qyWGkiS%2BsGh0%2BzTGVKbqI14r8hwEnSMCUWtzURB9wm2eY160T0Flou4leFJw4kXtTA%2B7zoefy64zdM8IdsUJZJLh77lAx8yeWIctNCdzlRSJ7L%2Bx43VknthylRYQdoPaWcp9zl2WyR3h0yRsSq4awBL9iVLN72CY%2BTtW5ScVGnZC2YXlVNYraP5Q7CYLhDWB4sRi5TBcw1QYiuw9lkmfA1vLD9L99wcXSC4aX0urGkhnVZv4zrmpDOpkZzX%2F%2B3pTDdpPe8BjqkAXIoJbHZ5Rx7gWHPDPJx%2Bx8jlPF9LWDqtsiLmW%2F6D2f6%2B2zIRfQCwvBcRehzkCD%2FIS%2Btt7bG%2BMik3OZRDyQX2ZoSrtTMKXTyE3xlGHorBk62zUdIiKJ7RliRJoBMBmmoGA3R9TxmVVs11SmowvtLxFPrl0ErmJcseD1H5LgMaoq1GuB9P3sTahy%2F9l7D2Nr7XAcyUOuVjWTGpAzTxwbpmRPH6Sk0&X-Amz-Signature=b91c9453a43ad46977765fc76b0a7f3efd66a69e614af02b2b795d96552636c0&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THP6F6CK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWVGOM0V5ER9iAlWaDMFdDvqS4P6ZLFEZQlZF%2BLbXtFQIhAIZT7bPOwShs%2FzJg3YHoIZGv%2BsJXBwi8i1lqQEvNGdkyKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igywh3AADi8%2B0LdfO7cq3AMWRXrzRsuKebZH8ny%2FrKAf9P1IkztVKW%2FkEINbTRgyRCA3Ky4k84Rjt7R9pHfUf%2BKhfHASYXPLR8UDMXYt%2BI3wgYsLyazmsnE%2FLhVUiuHUm3ylagCCo67WPJJdfV693U63ta54y7dNA%2FaUZ2D1ilkbPWKUt88uUKTfYYgkcS5jjmwlPPYXLEO4yswdJ9Os8ScXGHCcfOJH53s3xitxwMKhPPCYFkzd%2B%2FN9dHWB6ev%2FnhwpsNir8gfXNSshYsSFPdmEcCSZlM0sNyHA%2BqdgEPDOAC3k1l53n7D9RMVaWJnTn%2Bk57HU9jQ6tIqKk1bgzXfdPF6vXhnymLDbdEIyhlOO8udycI6qwCn0HSuYh8Web75Nq%2BWLoAGwturGYQ2qyWGkiS%2BsGh0%2BzTGVKbqI14r8hwEnSMCUWtzURB9wm2eY160T0Flou4leFJw4kXtTA%2B7zoefy64zdM8IdsUJZJLh77lAx8yeWIctNCdzlRSJ7L%2Bx43VknthylRYQdoPaWcp9zl2WyR3h0yRsSq4awBL9iVLN72CY%2BTtW5ScVGnZC2YXlVNYraP5Q7CYLhDWB4sRi5TBcw1QYiuw9lkmfA1vLD9L99wcXSC4aX0urGkhnVZv4zrmpDOpkZzX%2F%2B3pTDdpPe8BjqkAXIoJbHZ5Rx7gWHPDPJx%2Bx8jlPF9LWDqtsiLmW%2F6D2f6%2B2zIRfQCwvBcRehzkCD%2FIS%2Btt7bG%2BMik3OZRDyQX2ZoSrtTMKXTyE3xlGHorBk62zUdIiKJ7RliRJoBMBmmoGA3R9TxmVVs11SmowvtLxFPrl0ErmJcseD1H5LgMaoq1GuB9P3sTahy%2F9l7D2Nr7XAcyUOuVjWTGpAzTxwbpmRPH6Sk0&X-Amz-Signature=3a75ddb01a0e6c7131d03dbe20f356471e58123939d2e957bc8b29b0f6cec09e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THP6F6CK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWVGOM0V5ER9iAlWaDMFdDvqS4P6ZLFEZQlZF%2BLbXtFQIhAIZT7bPOwShs%2FzJg3YHoIZGv%2BsJXBwi8i1lqQEvNGdkyKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igywh3AADi8%2B0LdfO7cq3AMWRXrzRsuKebZH8ny%2FrKAf9P1IkztVKW%2FkEINbTRgyRCA3Ky4k84Rjt7R9pHfUf%2BKhfHASYXPLR8UDMXYt%2BI3wgYsLyazmsnE%2FLhVUiuHUm3ylagCCo67WPJJdfV693U63ta54y7dNA%2FaUZ2D1ilkbPWKUt88uUKTfYYgkcS5jjmwlPPYXLEO4yswdJ9Os8ScXGHCcfOJH53s3xitxwMKhPPCYFkzd%2B%2FN9dHWB6ev%2FnhwpsNir8gfXNSshYsSFPdmEcCSZlM0sNyHA%2BqdgEPDOAC3k1l53n7D9RMVaWJnTn%2Bk57HU9jQ6tIqKk1bgzXfdPF6vXhnymLDbdEIyhlOO8udycI6qwCn0HSuYh8Web75Nq%2BWLoAGwturGYQ2qyWGkiS%2BsGh0%2BzTGVKbqI14r8hwEnSMCUWtzURB9wm2eY160T0Flou4leFJw4kXtTA%2B7zoefy64zdM8IdsUJZJLh77lAx8yeWIctNCdzlRSJ7L%2Bx43VknthylRYQdoPaWcp9zl2WyR3h0yRsSq4awBL9iVLN72CY%2BTtW5ScVGnZC2YXlVNYraP5Q7CYLhDWB4sRi5TBcw1QYiuw9lkmfA1vLD9L99wcXSC4aX0urGkhnVZv4zrmpDOpkZzX%2F%2B3pTDdpPe8BjqkAXIoJbHZ5Rx7gWHPDPJx%2Bx8jlPF9LWDqtsiLmW%2F6D2f6%2B2zIRfQCwvBcRehzkCD%2FIS%2Btt7bG%2BMik3OZRDyQX2ZoSrtTMKXTyE3xlGHorBk62zUdIiKJ7RliRJoBMBmmoGA3R9TxmVVs11SmowvtLxFPrl0ErmJcseD1H5LgMaoq1GuB9P3sTahy%2F9l7D2Nr7XAcyUOuVjWTGpAzTxwbpmRPH6Sk0&X-Amz-Signature=b9ea0731ca08e795b2df16b799d9e20742742c48bf18deef74f560bf73278e2e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THP6F6CK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWVGOM0V5ER9iAlWaDMFdDvqS4P6ZLFEZQlZF%2BLbXtFQIhAIZT7bPOwShs%2FzJg3YHoIZGv%2BsJXBwi8i1lqQEvNGdkyKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igywh3AADi8%2B0LdfO7cq3AMWRXrzRsuKebZH8ny%2FrKAf9P1IkztVKW%2FkEINbTRgyRCA3Ky4k84Rjt7R9pHfUf%2BKhfHASYXPLR8UDMXYt%2BI3wgYsLyazmsnE%2FLhVUiuHUm3ylagCCo67WPJJdfV693U63ta54y7dNA%2FaUZ2D1ilkbPWKUt88uUKTfYYgkcS5jjmwlPPYXLEO4yswdJ9Os8ScXGHCcfOJH53s3xitxwMKhPPCYFkzd%2B%2FN9dHWB6ev%2FnhwpsNir8gfXNSshYsSFPdmEcCSZlM0sNyHA%2BqdgEPDOAC3k1l53n7D9RMVaWJnTn%2Bk57HU9jQ6tIqKk1bgzXfdPF6vXhnymLDbdEIyhlOO8udycI6qwCn0HSuYh8Web75Nq%2BWLoAGwturGYQ2qyWGkiS%2BsGh0%2BzTGVKbqI14r8hwEnSMCUWtzURB9wm2eY160T0Flou4leFJw4kXtTA%2B7zoefy64zdM8IdsUJZJLh77lAx8yeWIctNCdzlRSJ7L%2Bx43VknthylRYQdoPaWcp9zl2WyR3h0yRsSq4awBL9iVLN72CY%2BTtW5ScVGnZC2YXlVNYraP5Q7CYLhDWB4sRi5TBcw1QYiuw9lkmfA1vLD9L99wcXSC4aX0urGkhnVZv4zrmpDOpkZzX%2F%2B3pTDdpPe8BjqkAXIoJbHZ5Rx7gWHPDPJx%2Bx8jlPF9LWDqtsiLmW%2F6D2f6%2B2zIRfQCwvBcRehzkCD%2FIS%2Btt7bG%2BMik3OZRDyQX2ZoSrtTMKXTyE3xlGHorBk62zUdIiKJ7RliRJoBMBmmoGA3R9TxmVVs11SmowvtLxFPrl0ErmJcseD1H5LgMaoq1GuB9P3sTahy%2F9l7D2Nr7XAcyUOuVjWTGpAzTxwbpmRPH6Sk0&X-Amz-Signature=6669512b8a2d3723122788d8227f745fe0e65140d6da63b67a1226a5ea15c50e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THP6F6CK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWVGOM0V5ER9iAlWaDMFdDvqS4P6ZLFEZQlZF%2BLbXtFQIhAIZT7bPOwShs%2FzJg3YHoIZGv%2BsJXBwi8i1lqQEvNGdkyKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igywh3AADi8%2B0LdfO7cq3AMWRXrzRsuKebZH8ny%2FrKAf9P1IkztVKW%2FkEINbTRgyRCA3Ky4k84Rjt7R9pHfUf%2BKhfHASYXPLR8UDMXYt%2BI3wgYsLyazmsnE%2FLhVUiuHUm3ylagCCo67WPJJdfV693U63ta54y7dNA%2FaUZ2D1ilkbPWKUt88uUKTfYYgkcS5jjmwlPPYXLEO4yswdJ9Os8ScXGHCcfOJH53s3xitxwMKhPPCYFkzd%2B%2FN9dHWB6ev%2FnhwpsNir8gfXNSshYsSFPdmEcCSZlM0sNyHA%2BqdgEPDOAC3k1l53n7D9RMVaWJnTn%2Bk57HU9jQ6tIqKk1bgzXfdPF6vXhnymLDbdEIyhlOO8udycI6qwCn0HSuYh8Web75Nq%2BWLoAGwturGYQ2qyWGkiS%2BsGh0%2BzTGVKbqI14r8hwEnSMCUWtzURB9wm2eY160T0Flou4leFJw4kXtTA%2B7zoefy64zdM8IdsUJZJLh77lAx8yeWIctNCdzlRSJ7L%2Bx43VknthylRYQdoPaWcp9zl2WyR3h0yRsSq4awBL9iVLN72CY%2BTtW5ScVGnZC2YXlVNYraP5Q7CYLhDWB4sRi5TBcw1QYiuw9lkmfA1vLD9L99wcXSC4aX0urGkhnVZv4zrmpDOpkZzX%2F%2B3pTDdpPe8BjqkAXIoJbHZ5Rx7gWHPDPJx%2Bx8jlPF9LWDqtsiLmW%2F6D2f6%2B2zIRfQCwvBcRehzkCD%2FIS%2Btt7bG%2BMik3OZRDyQX2ZoSrtTMKXTyE3xlGHorBk62zUdIiKJ7RliRJoBMBmmoGA3R9TxmVVs11SmowvtLxFPrl0ErmJcseD1H5LgMaoq1GuB9P3sTahy%2F9l7D2Nr7XAcyUOuVjWTGpAzTxwbpmRPH6Sk0&X-Amz-Signature=cf94de7231ea3e02b2dfab9a46e110dfdd8f589e4504adb1d695e5077833235d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKROG7QJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICfytEgfbKRUr47zATZvR2MQdQJOlqkK5X2lpvzbseNnAiEA5JqyUqGfIH2M2fzub1ewbYWWGN5AnplOhn%2F9Q5%2Bv7nAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMtJkkpM1wKjjiqWpircA12EBWyWLKj9hU%2FPOd1MFEdmbSpfhhWMl8AeZdzsiHRJJ9nV6Br7ngoVA3sAsd1JSrnH5%2FAj1tJ6we3tLaYvWV1%2Fsm4io929u6ioIxxyUvi%2BpCDmrCLmujdoJ78yFRSNH1hkD0gjTnAkZ1pgFOEwLTkKuVJis122DVe%2F9lwDDFmKR26GVIt9mLWOTW7o08uKygEPq6YVlSD709%2BkoPSfAr0IoG7Px5MFF%2BusGopoRyKO58n10syvhkKFj3oUmKEchTcfAXa9CEEv5nXLSmHVkNkS6DDBjwUjBD4yxCsDG2iZgjIBKFswoKCl5FAk1CbS6Y9EOW1FIOJOpzi80%2F0wc0UnAZFfEv0hEVV64BPkoEiTR4yXOy7cN0tY1vyHaLsKk9P0YmIFbcQY8I1Ix1OQzhRBH%2B5973ZXW39PkJB9vvbSH7gIFgM3W69Q8vW7jQEj6QOEuVqMfX335GsR715WpcEt%2B8y7uzKEKqHfqdMECNptKSKIdIoOsirqbU%2B3sRtGn4Uz%2BQgwYtXVTtPEhwesnFVsHNLKt8mI3QjkIQBg9mEdS%2FWrD1HdY5TsoKIgbSZkVFzSYaY664dejq9DAbKm8ihJxvVCsiyYD6QEOTPtFotWTrK%2FNgrePzuXWs1VMOSk97wGOqUBt9III4VeTCTeJKu3uv41GguJpVPnynIpklQwec7vq9ZjpGfDK8XcyGe4jk5z3zicOrmi%2FyIofDMxHEmRSwLX75bkRRxQfN1AFWmHQ5H5C5xetD76TodO2nvjY8KQzB8T4DXcR9iiOBJx4%2FZHKBKZLNl52b%2BmND8uH1GVFTX9pplw8u3cKBO1FAGIvi4%2FArpw%2FQpRB%2FSTtUaA3m6c1rs%2FGqxsaT1%2F&X-Amz-Signature=0a76a7ead4a4290b9d84923e4472337f7bd0b9fc4e352bc5aa135026ac9c6892&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKROG7QJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICfytEgfbKRUr47zATZvR2MQdQJOlqkK5X2lpvzbseNnAiEA5JqyUqGfIH2M2fzub1ewbYWWGN5AnplOhn%2F9Q5%2Bv7nAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMtJkkpM1wKjjiqWpircA12EBWyWLKj9hU%2FPOd1MFEdmbSpfhhWMl8AeZdzsiHRJJ9nV6Br7ngoVA3sAsd1JSrnH5%2FAj1tJ6we3tLaYvWV1%2Fsm4io929u6ioIxxyUvi%2BpCDmrCLmujdoJ78yFRSNH1hkD0gjTnAkZ1pgFOEwLTkKuVJis122DVe%2F9lwDDFmKR26GVIt9mLWOTW7o08uKygEPq6YVlSD709%2BkoPSfAr0IoG7Px5MFF%2BusGopoRyKO58n10syvhkKFj3oUmKEchTcfAXa9CEEv5nXLSmHVkNkS6DDBjwUjBD4yxCsDG2iZgjIBKFswoKCl5FAk1CbS6Y9EOW1FIOJOpzi80%2F0wc0UnAZFfEv0hEVV64BPkoEiTR4yXOy7cN0tY1vyHaLsKk9P0YmIFbcQY8I1Ix1OQzhRBH%2B5973ZXW39PkJB9vvbSH7gIFgM3W69Q8vW7jQEj6QOEuVqMfX335GsR715WpcEt%2B8y7uzKEKqHfqdMECNptKSKIdIoOsirqbU%2B3sRtGn4Uz%2BQgwYtXVTtPEhwesnFVsHNLKt8mI3QjkIQBg9mEdS%2FWrD1HdY5TsoKIgbSZkVFzSYaY664dejq9DAbKm8ihJxvVCsiyYD6QEOTPtFotWTrK%2FNgrePzuXWs1VMOSk97wGOqUBt9III4VeTCTeJKu3uv41GguJpVPnynIpklQwec7vq9ZjpGfDK8XcyGe4jk5z3zicOrmi%2FyIofDMxHEmRSwLX75bkRRxQfN1AFWmHQ5H5C5xetD76TodO2nvjY8KQzB8T4DXcR9iiOBJx4%2FZHKBKZLNl52b%2BmND8uH1GVFTX9pplw8u3cKBO1FAGIvi4%2FArpw%2FQpRB%2FSTtUaA3m6c1rs%2FGqxsaT1%2F&X-Amz-Signature=837c57af239a35c75776d8ca6d679b117d840d049a4c7795efb7815c0f9561f0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
