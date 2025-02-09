

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IEHIAP6%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICahzYCLEy8iEZsl4YNBkuxKzGAzFJYpG6YQ9vR5heNMAiB3oPj3uwm%2B16FMWCqUBh34K%2FUsRv2aqvgTJ6hEpIRalSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJwe%2F0zXO8%2BnqKlVGKtwDtszvOC7yGHuhpC3reyiSB%2B35vXxZ0Nz5Yi4p9qcW45YqudR9yzNLutwkkr4spLYqOiV39vm72PhZiFSgn4gSzTFiSZpRzHuzPk3z3Rg5pFdz1rM7l0dXZCilCahDs1dgjJCaufnSSCB%2BaVddecEu99kUep8Yv8jeOrQzMsaF79utIsYX6bBt%2FLLN8LrJpfLe3ehpV3yBNFw5DmIJ4c%2FRuzHhGGw0Xm9939EU4E%2BvIvuRhyTp26IXIw6P%2FgWiM59cluUT3nXmg96XcnH7Y9wBBpHQ3WyLcPZn7ldaDzMVDrnj8RljKoJsYKqpfRBwl9SMyuSI1mJzK2Lq5xbDk%2Brfov7atxPNnmicb2KFvZJYt1zNxjwPQCZlHJeIn2A6W0v0lI6C6%2BEdDIGC4fXFrkld4%2Fk5fa%2Fv5vc9PemdsW85oU01DjeoHZLUdjB0FioWQ%2FUFkMII3wCURASrWpucdYV5VEJ14zfn1k5Uka78SSu6xiHsspuFofLjnC3Ea%2BsohVk3rFlPIZlHA9ADJRb1%2BwSOuEws0Vx57cnohxU7SHtv%2FoOBhaN5HAiiLeGlVLB9MrAgOCb2Tww7ZoVmTEJIhUWm4CEuroYqPPMxArjm92LpHSCneVYUXffmcbSRFEkwzNafvQY6pgEqSNcxmShvlUBuY%2BLzS2xjanuV7t1uZ9QDQ%2F92bJrRqqnD0O%2FPD7NTZwUXJ6GA68UpJHATkeAAHbnh6JZFUiDtoUUTgqPyhyYoErpxUSnM0EzdHiVIxEQF5qXBKU71FiMlZGAG4s1VMljyQVK8Z3t94iUgvrq1QKjsTRfnF8D7D7ClDXqqe1C7pF%2BhHnjOm0Rx7Qr%2FWugq%2BtqM%2FivWFeHG4a2tbAfm&X-Amz-Signature=bd0a00ba1e06fb96af17784af5348a83fc65051ea0153e9d33183ad80b94396b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IEHIAP6%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICahzYCLEy8iEZsl4YNBkuxKzGAzFJYpG6YQ9vR5heNMAiB3oPj3uwm%2B16FMWCqUBh34K%2FUsRv2aqvgTJ6hEpIRalSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJwe%2F0zXO8%2BnqKlVGKtwDtszvOC7yGHuhpC3reyiSB%2B35vXxZ0Nz5Yi4p9qcW45YqudR9yzNLutwkkr4spLYqOiV39vm72PhZiFSgn4gSzTFiSZpRzHuzPk3z3Rg5pFdz1rM7l0dXZCilCahDs1dgjJCaufnSSCB%2BaVddecEu99kUep8Yv8jeOrQzMsaF79utIsYX6bBt%2FLLN8LrJpfLe3ehpV3yBNFw5DmIJ4c%2FRuzHhGGw0Xm9939EU4E%2BvIvuRhyTp26IXIw6P%2FgWiM59cluUT3nXmg96XcnH7Y9wBBpHQ3WyLcPZn7ldaDzMVDrnj8RljKoJsYKqpfRBwl9SMyuSI1mJzK2Lq5xbDk%2Brfov7atxPNnmicb2KFvZJYt1zNxjwPQCZlHJeIn2A6W0v0lI6C6%2BEdDIGC4fXFrkld4%2Fk5fa%2Fv5vc9PemdsW85oU01DjeoHZLUdjB0FioWQ%2FUFkMII3wCURASrWpucdYV5VEJ14zfn1k5Uka78SSu6xiHsspuFofLjnC3Ea%2BsohVk3rFlPIZlHA9ADJRb1%2BwSOuEws0Vx57cnohxU7SHtv%2FoOBhaN5HAiiLeGlVLB9MrAgOCb2Tww7ZoVmTEJIhUWm4CEuroYqPPMxArjm92LpHSCneVYUXffmcbSRFEkwzNafvQY6pgEqSNcxmShvlUBuY%2BLzS2xjanuV7t1uZ9QDQ%2F92bJrRqqnD0O%2FPD7NTZwUXJ6GA68UpJHATkeAAHbnh6JZFUiDtoUUTgqPyhyYoErpxUSnM0EzdHiVIxEQF5qXBKU71FiMlZGAG4s1VMljyQVK8Z3t94iUgvrq1QKjsTRfnF8D7D7ClDXqqe1C7pF%2BhHnjOm0Rx7Qr%2FWugq%2BtqM%2FivWFeHG4a2tbAfm&X-Amz-Signature=b70b0adaad35b62c90f3f827dfd363d207c769d0f78772e1e2c8909decfae044&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IEHIAP6%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICahzYCLEy8iEZsl4YNBkuxKzGAzFJYpG6YQ9vR5heNMAiB3oPj3uwm%2B16FMWCqUBh34K%2FUsRv2aqvgTJ6hEpIRalSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJwe%2F0zXO8%2BnqKlVGKtwDtszvOC7yGHuhpC3reyiSB%2B35vXxZ0Nz5Yi4p9qcW45YqudR9yzNLutwkkr4spLYqOiV39vm72PhZiFSgn4gSzTFiSZpRzHuzPk3z3Rg5pFdz1rM7l0dXZCilCahDs1dgjJCaufnSSCB%2BaVddecEu99kUep8Yv8jeOrQzMsaF79utIsYX6bBt%2FLLN8LrJpfLe3ehpV3yBNFw5DmIJ4c%2FRuzHhGGw0Xm9939EU4E%2BvIvuRhyTp26IXIw6P%2FgWiM59cluUT3nXmg96XcnH7Y9wBBpHQ3WyLcPZn7ldaDzMVDrnj8RljKoJsYKqpfRBwl9SMyuSI1mJzK2Lq5xbDk%2Brfov7atxPNnmicb2KFvZJYt1zNxjwPQCZlHJeIn2A6W0v0lI6C6%2BEdDIGC4fXFrkld4%2Fk5fa%2Fv5vc9PemdsW85oU01DjeoHZLUdjB0FioWQ%2FUFkMII3wCURASrWpucdYV5VEJ14zfn1k5Uka78SSu6xiHsspuFofLjnC3Ea%2BsohVk3rFlPIZlHA9ADJRb1%2BwSOuEws0Vx57cnohxU7SHtv%2FoOBhaN5HAiiLeGlVLB9MrAgOCb2Tww7ZoVmTEJIhUWm4CEuroYqPPMxArjm92LpHSCneVYUXffmcbSRFEkwzNafvQY6pgEqSNcxmShvlUBuY%2BLzS2xjanuV7t1uZ9QDQ%2F92bJrRqqnD0O%2FPD7NTZwUXJ6GA68UpJHATkeAAHbnh6JZFUiDtoUUTgqPyhyYoErpxUSnM0EzdHiVIxEQF5qXBKU71FiMlZGAG4s1VMljyQVK8Z3t94iUgvrq1QKjsTRfnF8D7D7ClDXqqe1C7pF%2BhHnjOm0Rx7Qr%2FWugq%2BtqM%2FivWFeHG4a2tbAfm&X-Amz-Signature=e475928e70b28ab33c04b4a9d824bc2dede73162d36d8312e64e66ec1c155d63&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IEHIAP6%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICahzYCLEy8iEZsl4YNBkuxKzGAzFJYpG6YQ9vR5heNMAiB3oPj3uwm%2B16FMWCqUBh34K%2FUsRv2aqvgTJ6hEpIRalSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJwe%2F0zXO8%2BnqKlVGKtwDtszvOC7yGHuhpC3reyiSB%2B35vXxZ0Nz5Yi4p9qcW45YqudR9yzNLutwkkr4spLYqOiV39vm72PhZiFSgn4gSzTFiSZpRzHuzPk3z3Rg5pFdz1rM7l0dXZCilCahDs1dgjJCaufnSSCB%2BaVddecEu99kUep8Yv8jeOrQzMsaF79utIsYX6bBt%2FLLN8LrJpfLe3ehpV3yBNFw5DmIJ4c%2FRuzHhGGw0Xm9939EU4E%2BvIvuRhyTp26IXIw6P%2FgWiM59cluUT3nXmg96XcnH7Y9wBBpHQ3WyLcPZn7ldaDzMVDrnj8RljKoJsYKqpfRBwl9SMyuSI1mJzK2Lq5xbDk%2Brfov7atxPNnmicb2KFvZJYt1zNxjwPQCZlHJeIn2A6W0v0lI6C6%2BEdDIGC4fXFrkld4%2Fk5fa%2Fv5vc9PemdsW85oU01DjeoHZLUdjB0FioWQ%2FUFkMII3wCURASrWpucdYV5VEJ14zfn1k5Uka78SSu6xiHsspuFofLjnC3Ea%2BsohVk3rFlPIZlHA9ADJRb1%2BwSOuEws0Vx57cnohxU7SHtv%2FoOBhaN5HAiiLeGlVLB9MrAgOCb2Tww7ZoVmTEJIhUWm4CEuroYqPPMxArjm92LpHSCneVYUXffmcbSRFEkwzNafvQY6pgEqSNcxmShvlUBuY%2BLzS2xjanuV7t1uZ9QDQ%2F92bJrRqqnD0O%2FPD7NTZwUXJ6GA68UpJHATkeAAHbnh6JZFUiDtoUUTgqPyhyYoErpxUSnM0EzdHiVIxEQF5qXBKU71FiMlZGAG4s1VMljyQVK8Z3t94iUgvrq1QKjsTRfnF8D7D7ClDXqqe1C7pF%2BhHnjOm0Rx7Qr%2FWugq%2BtqM%2FivWFeHG4a2tbAfm&X-Amz-Signature=1e7348a05ae14d2f9913500d3554266ac4d4179cb9bf442e7266143000b423b2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IEHIAP6%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICahzYCLEy8iEZsl4YNBkuxKzGAzFJYpG6YQ9vR5heNMAiB3oPj3uwm%2B16FMWCqUBh34K%2FUsRv2aqvgTJ6hEpIRalSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJwe%2F0zXO8%2BnqKlVGKtwDtszvOC7yGHuhpC3reyiSB%2B35vXxZ0Nz5Yi4p9qcW45YqudR9yzNLutwkkr4spLYqOiV39vm72PhZiFSgn4gSzTFiSZpRzHuzPk3z3Rg5pFdz1rM7l0dXZCilCahDs1dgjJCaufnSSCB%2BaVddecEu99kUep8Yv8jeOrQzMsaF79utIsYX6bBt%2FLLN8LrJpfLe3ehpV3yBNFw5DmIJ4c%2FRuzHhGGw0Xm9939EU4E%2BvIvuRhyTp26IXIw6P%2FgWiM59cluUT3nXmg96XcnH7Y9wBBpHQ3WyLcPZn7ldaDzMVDrnj8RljKoJsYKqpfRBwl9SMyuSI1mJzK2Lq5xbDk%2Brfov7atxPNnmicb2KFvZJYt1zNxjwPQCZlHJeIn2A6W0v0lI6C6%2BEdDIGC4fXFrkld4%2Fk5fa%2Fv5vc9PemdsW85oU01DjeoHZLUdjB0FioWQ%2FUFkMII3wCURASrWpucdYV5VEJ14zfn1k5Uka78SSu6xiHsspuFofLjnC3Ea%2BsohVk3rFlPIZlHA9ADJRb1%2BwSOuEws0Vx57cnohxU7SHtv%2FoOBhaN5HAiiLeGlVLB9MrAgOCb2Tww7ZoVmTEJIhUWm4CEuroYqPPMxArjm92LpHSCneVYUXffmcbSRFEkwzNafvQY6pgEqSNcxmShvlUBuY%2BLzS2xjanuV7t1uZ9QDQ%2F92bJrRqqnD0O%2FPD7NTZwUXJ6GA68UpJHATkeAAHbnh6JZFUiDtoUUTgqPyhyYoErpxUSnM0EzdHiVIxEQF5qXBKU71FiMlZGAG4s1VMljyQVK8Z3t94iUgvrq1QKjsTRfnF8D7D7ClDXqqe1C7pF%2BhHnjOm0Rx7Qr%2FWugq%2BtqM%2FivWFeHG4a2tbAfm&X-Amz-Signature=a330abea2b46d9b36b017d5a87827f56bcb734760dee7dd4227a0c6ef40538d4&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IEHIAP6%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICahzYCLEy8iEZsl4YNBkuxKzGAzFJYpG6YQ9vR5heNMAiB3oPj3uwm%2B16FMWCqUBh34K%2FUsRv2aqvgTJ6hEpIRalSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJwe%2F0zXO8%2BnqKlVGKtwDtszvOC7yGHuhpC3reyiSB%2B35vXxZ0Nz5Yi4p9qcW45YqudR9yzNLutwkkr4spLYqOiV39vm72PhZiFSgn4gSzTFiSZpRzHuzPk3z3Rg5pFdz1rM7l0dXZCilCahDs1dgjJCaufnSSCB%2BaVddecEu99kUep8Yv8jeOrQzMsaF79utIsYX6bBt%2FLLN8LrJpfLe3ehpV3yBNFw5DmIJ4c%2FRuzHhGGw0Xm9939EU4E%2BvIvuRhyTp26IXIw6P%2FgWiM59cluUT3nXmg96XcnH7Y9wBBpHQ3WyLcPZn7ldaDzMVDrnj8RljKoJsYKqpfRBwl9SMyuSI1mJzK2Lq5xbDk%2Brfov7atxPNnmicb2KFvZJYt1zNxjwPQCZlHJeIn2A6W0v0lI6C6%2BEdDIGC4fXFrkld4%2Fk5fa%2Fv5vc9PemdsW85oU01DjeoHZLUdjB0FioWQ%2FUFkMII3wCURASrWpucdYV5VEJ14zfn1k5Uka78SSu6xiHsspuFofLjnC3Ea%2BsohVk3rFlPIZlHA9ADJRb1%2BwSOuEws0Vx57cnohxU7SHtv%2FoOBhaN5HAiiLeGlVLB9MrAgOCb2Tww7ZoVmTEJIhUWm4CEuroYqPPMxArjm92LpHSCneVYUXffmcbSRFEkwzNafvQY6pgEqSNcxmShvlUBuY%2BLzS2xjanuV7t1uZ9QDQ%2F92bJrRqqnD0O%2FPD7NTZwUXJ6GA68UpJHATkeAAHbnh6JZFUiDtoUUTgqPyhyYoErpxUSnM0EzdHiVIxEQF5qXBKU71FiMlZGAG4s1VMljyQVK8Z3t94iUgvrq1QKjsTRfnF8D7D7ClDXqqe1C7pF%2BhHnjOm0Rx7Qr%2FWugq%2BtqM%2FivWFeHG4a2tbAfm&X-Amz-Signature=ad366290027eed9e9a6d74e3779057c77853dfbf7e9ac25b378d9cd752e7e81e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IEHIAP6%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICahzYCLEy8iEZsl4YNBkuxKzGAzFJYpG6YQ9vR5heNMAiB3oPj3uwm%2B16FMWCqUBh34K%2FUsRv2aqvgTJ6hEpIRalSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJwe%2F0zXO8%2BnqKlVGKtwDtszvOC7yGHuhpC3reyiSB%2B35vXxZ0Nz5Yi4p9qcW45YqudR9yzNLutwkkr4spLYqOiV39vm72PhZiFSgn4gSzTFiSZpRzHuzPk3z3Rg5pFdz1rM7l0dXZCilCahDs1dgjJCaufnSSCB%2BaVddecEu99kUep8Yv8jeOrQzMsaF79utIsYX6bBt%2FLLN8LrJpfLe3ehpV3yBNFw5DmIJ4c%2FRuzHhGGw0Xm9939EU4E%2BvIvuRhyTp26IXIw6P%2FgWiM59cluUT3nXmg96XcnH7Y9wBBpHQ3WyLcPZn7ldaDzMVDrnj8RljKoJsYKqpfRBwl9SMyuSI1mJzK2Lq5xbDk%2Brfov7atxPNnmicb2KFvZJYt1zNxjwPQCZlHJeIn2A6W0v0lI6C6%2BEdDIGC4fXFrkld4%2Fk5fa%2Fv5vc9PemdsW85oU01DjeoHZLUdjB0FioWQ%2FUFkMII3wCURASrWpucdYV5VEJ14zfn1k5Uka78SSu6xiHsspuFofLjnC3Ea%2BsohVk3rFlPIZlHA9ADJRb1%2BwSOuEws0Vx57cnohxU7SHtv%2FoOBhaN5HAiiLeGlVLB9MrAgOCb2Tww7ZoVmTEJIhUWm4CEuroYqPPMxArjm92LpHSCneVYUXffmcbSRFEkwzNafvQY6pgEqSNcxmShvlUBuY%2BLzS2xjanuV7t1uZ9QDQ%2F92bJrRqqnD0O%2FPD7NTZwUXJ6GA68UpJHATkeAAHbnh6JZFUiDtoUUTgqPyhyYoErpxUSnM0EzdHiVIxEQF5qXBKU71FiMlZGAG4s1VMljyQVK8Z3t94iUgvrq1QKjsTRfnF8D7D7ClDXqqe1C7pF%2BhHnjOm0Rx7Qr%2FWugq%2BtqM%2FivWFeHG4a2tbAfm&X-Amz-Signature=8184427597ed4df191de3f4e78c386fa2f04e3c4ebb4694398ed3df8ab0abd6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IEHIAP6%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICahzYCLEy8iEZsl4YNBkuxKzGAzFJYpG6YQ9vR5heNMAiB3oPj3uwm%2B16FMWCqUBh34K%2FUsRv2aqvgTJ6hEpIRalSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJwe%2F0zXO8%2BnqKlVGKtwDtszvOC7yGHuhpC3reyiSB%2B35vXxZ0Nz5Yi4p9qcW45YqudR9yzNLutwkkr4spLYqOiV39vm72PhZiFSgn4gSzTFiSZpRzHuzPk3z3Rg5pFdz1rM7l0dXZCilCahDs1dgjJCaufnSSCB%2BaVddecEu99kUep8Yv8jeOrQzMsaF79utIsYX6bBt%2FLLN8LrJpfLe3ehpV3yBNFw5DmIJ4c%2FRuzHhGGw0Xm9939EU4E%2BvIvuRhyTp26IXIw6P%2FgWiM59cluUT3nXmg96XcnH7Y9wBBpHQ3WyLcPZn7ldaDzMVDrnj8RljKoJsYKqpfRBwl9SMyuSI1mJzK2Lq5xbDk%2Brfov7atxPNnmicb2KFvZJYt1zNxjwPQCZlHJeIn2A6W0v0lI6C6%2BEdDIGC4fXFrkld4%2Fk5fa%2Fv5vc9PemdsW85oU01DjeoHZLUdjB0FioWQ%2FUFkMII3wCURASrWpucdYV5VEJ14zfn1k5Uka78SSu6xiHsspuFofLjnC3Ea%2BsohVk3rFlPIZlHA9ADJRb1%2BwSOuEws0Vx57cnohxU7SHtv%2FoOBhaN5HAiiLeGlVLB9MrAgOCb2Tww7ZoVmTEJIhUWm4CEuroYqPPMxArjm92LpHSCneVYUXffmcbSRFEkwzNafvQY6pgEqSNcxmShvlUBuY%2BLzS2xjanuV7t1uZ9QDQ%2F92bJrRqqnD0O%2FPD7NTZwUXJ6GA68UpJHATkeAAHbnh6JZFUiDtoUUTgqPyhyYoErpxUSnM0EzdHiVIxEQF5qXBKU71FiMlZGAG4s1VMljyQVK8Z3t94iUgvrq1QKjsTRfnF8D7D7ClDXqqe1C7pF%2BhHnjOm0Rx7Qr%2FWugq%2BtqM%2FivWFeHG4a2tbAfm&X-Amz-Signature=f4d0745e85b14dcac4d6fc4abd2d32f84f98d40146fcf4540441f7f38dc326eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IEHIAP6%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICahzYCLEy8iEZsl4YNBkuxKzGAzFJYpG6YQ9vR5heNMAiB3oPj3uwm%2B16FMWCqUBh34K%2FUsRv2aqvgTJ6hEpIRalSqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJwe%2F0zXO8%2BnqKlVGKtwDtszvOC7yGHuhpC3reyiSB%2B35vXxZ0Nz5Yi4p9qcW45YqudR9yzNLutwkkr4spLYqOiV39vm72PhZiFSgn4gSzTFiSZpRzHuzPk3z3Rg5pFdz1rM7l0dXZCilCahDs1dgjJCaufnSSCB%2BaVddecEu99kUep8Yv8jeOrQzMsaF79utIsYX6bBt%2FLLN8LrJpfLe3ehpV3yBNFw5DmIJ4c%2FRuzHhGGw0Xm9939EU4E%2BvIvuRhyTp26IXIw6P%2FgWiM59cluUT3nXmg96XcnH7Y9wBBpHQ3WyLcPZn7ldaDzMVDrnj8RljKoJsYKqpfRBwl9SMyuSI1mJzK2Lq5xbDk%2Brfov7atxPNnmicb2KFvZJYt1zNxjwPQCZlHJeIn2A6W0v0lI6C6%2BEdDIGC4fXFrkld4%2Fk5fa%2Fv5vc9PemdsW85oU01DjeoHZLUdjB0FioWQ%2FUFkMII3wCURASrWpucdYV5VEJ14zfn1k5Uka78SSu6xiHsspuFofLjnC3Ea%2BsohVk3rFlPIZlHA9ADJRb1%2BwSOuEws0Vx57cnohxU7SHtv%2FoOBhaN5HAiiLeGlVLB9MrAgOCb2Tww7ZoVmTEJIhUWm4CEuroYqPPMxArjm92LpHSCneVYUXffmcbSRFEkwzNafvQY6pgEqSNcxmShvlUBuY%2BLzS2xjanuV7t1uZ9QDQ%2F92bJrRqqnD0O%2FPD7NTZwUXJ6GA68UpJHATkeAAHbnh6JZFUiDtoUUTgqPyhyYoErpxUSnM0EzdHiVIxEQF5qXBKU71FiMlZGAG4s1VMljyQVK8Z3t94iUgvrq1QKjsTRfnF8D7D7ClDXqqe1C7pF%2BhHnjOm0Rx7Qr%2FWugq%2BtqM%2FivWFeHG4a2tbAfm&X-Amz-Signature=f4dab002fa51209315b184635de980fbb674a74e6df76db284f9345b8b5877a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXUCBXOB%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCViKcBKULYeXIHk7Y7b4NPbn2cQNucrBtRBQ8zWwrU9gIhALSxK8qfH5ADmbOt9VbR0xQaS7JIAtK8HXyHwu3%2FWqcYKogECJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz8JCC%2B2N2ncGDxpUsq3AOfuGdobIulOgnYVhgEHS3aM9SVsLwsBgjvpn0FLVqJdc3TK9fXCchJKVsDoouTagb5DkDBhOJ2Jn6uDNiF4wCSpkqhzE2%2BDoiRAEauOiYH5FvHvLs5dc2vdwetEaUBfh2RxQ9ttUNTom5shvtOsV1qYkqNh4ucI11w3djPHjFMRRnLLRR65pi75vnaBeJ4qklsZ4YXTd443btPvuWaRD0y6UudOgpiXYRjRNVHf1Y%2FGbhxgsw%2FOSBnz2vBEjXDxA21leA%2FbK2w88AnvqXsQigoxvmew9d0PObAWwfpwpHYW1aQPzAHnyW5zoRKWN%2F3sr8MpBYYFUvHYctCkZdmYu6Hpiljkue%2BbUCI7c3ixYRkj56a7%2Bp7rbmbt2qJyGm2r2k1pkClD1vxim82145lnYvl3a068h74DugL7nNYkJzfee82BgXCW35zWMU9jOUgSA54m%2FIGdbJyL2hTphZhmUwQzEQTydHLCfHCPc%2BrZZWaLINZb%2BaYSmXC%2FColxpROZAmh0SLQejCTELuxGSbSk8mBcGhNDcSFYGDjzOFBvRCWM5kb2GcDmE1sle31FKBj7Dk0JmJ1tvcespg7C7fDtQ6go3ADcdYrBL0LrplkAYLhcAPt19zbj8fTsDCd5TCy1p%2B9BjqkAfpQpq6CG5b%2B7azQycKUHt%2Fm%2FQEqiq%2FqxhxjTTKrvwzYyKSAA6POR4bZtWvcYEoLmuVmhR0FjNd4R2c1kHL5pGKAnj%2FjzP9wI3v3GtfvaiECUhm28hSIglY87Euy3mPntZQU5N02XNri%2BXu22OJ6I1jEvTqFzHH7FbnXNTTad2lhSBI2b6WsVB0AghcKJE1f4seZ5EJ3jhEqDjkJ4nyuRrg%2FsLvw&X-Amz-Signature=34d2d62896135941ce717cfc338d7c5b2bb0bc728237ab90c8acc338ea054acf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXUCBXOB%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCViKcBKULYeXIHk7Y7b4NPbn2cQNucrBtRBQ8zWwrU9gIhALSxK8qfH5ADmbOt9VbR0xQaS7JIAtK8HXyHwu3%2FWqcYKogECJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz8JCC%2B2N2ncGDxpUsq3AOfuGdobIulOgnYVhgEHS3aM9SVsLwsBgjvpn0FLVqJdc3TK9fXCchJKVsDoouTagb5DkDBhOJ2Jn6uDNiF4wCSpkqhzE2%2BDoiRAEauOiYH5FvHvLs5dc2vdwetEaUBfh2RxQ9ttUNTom5shvtOsV1qYkqNh4ucI11w3djPHjFMRRnLLRR65pi75vnaBeJ4qklsZ4YXTd443btPvuWaRD0y6UudOgpiXYRjRNVHf1Y%2FGbhxgsw%2FOSBnz2vBEjXDxA21leA%2FbK2w88AnvqXsQigoxvmew9d0PObAWwfpwpHYW1aQPzAHnyW5zoRKWN%2F3sr8MpBYYFUvHYctCkZdmYu6Hpiljkue%2BbUCI7c3ixYRkj56a7%2Bp7rbmbt2qJyGm2r2k1pkClD1vxim82145lnYvl3a068h74DugL7nNYkJzfee82BgXCW35zWMU9jOUgSA54m%2FIGdbJyL2hTphZhmUwQzEQTydHLCfHCPc%2BrZZWaLINZb%2BaYSmXC%2FColxpROZAmh0SLQejCTELuxGSbSk8mBcGhNDcSFYGDjzOFBvRCWM5kb2GcDmE1sle31FKBj7Dk0JmJ1tvcespg7C7fDtQ6go3ADcdYrBL0LrplkAYLhcAPt19zbj8fTsDCd5TCy1p%2B9BjqkAfpQpq6CG5b%2B7azQycKUHt%2Fm%2FQEqiq%2FqxhxjTTKrvwzYyKSAA6POR4bZtWvcYEoLmuVmhR0FjNd4R2c1kHL5pGKAnj%2FjzP9wI3v3GtfvaiECUhm28hSIglY87Euy3mPntZQU5N02XNri%2BXu22OJ6I1jEvTqFzHH7FbnXNTTad2lhSBI2b6WsVB0AghcKJE1f4seZ5EJ3jhEqDjkJ4nyuRrg%2FsLvw&X-Amz-Signature=04b71c3eb8d1b7fa9850c4b2507319eb68da28258601490a0cf015ad8f9a28d2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
