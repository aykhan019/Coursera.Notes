

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FGN6ICA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfEBVF%2BwwJnhh5GLOx3G29iZqFbv5QOZsuDvKXCvySpAiBDIUkTBjc%2BKsYOGanATGxPigeqg7sEDmcFO1s%2FrfbaUSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMqWtVmbAjg1PSkfKmKtwD04adIDjqOH0P%2FMeeHMcsjEshsKEex5Aag%2BfsqNF8ibR%2F9et6a0BPMByJ6nBX52Qq1xeInMxjIuLyWFD0AIZxlJHnTTfNLSFVueZLL05NgvRIC1UWpD6aiLQWjwFA%2BQOgmggBhroMCVHwTaRfqZshjQ80ZkdxLLgEB9mJAGaXlUFHHQ7VJ7%2FqsiHNL9zLbvMlFBKCM0FUHpVGHmOZYp8LdLgUEfRJidarDw9ING3Lw9XFuljG8gMnllakYR16l77AwjjOk8s7eZ5ApMAigzsuwQdpCriu1Vt5Xc60aDVbk%2FNo0mQw2UYbtD6QtCpnqy4uVoOXPM1oRpHcQTR1UBPOaoIWHYL0MNAPlADdTd652TWotD6Ve1iOY6oIFeK51gzZrJ0KMqPDOyBl1s6ZMDxJnyC%2FfXNTtw711BUN0VOpUpelMObAEWRhaBAEKQqkV0IK8XStxjB5sqI9tHP5jXMOBf96gvOzuav0eUZZ1x%2FkXLRDWlEWjMBug3YPDf4FN9lszYjDgcJS07E77HMfpQI%2BT9OWqZBV9A4DDWMXRZcJA4mafBxxQ8LpNgskvz69%2BSrQgjWgQ63Uh%2BiMk%2FJitOSaxXJRHPx0xh3YJYhW1Cs%2BbJdxkF0HmBPl4%2Fb5Eg0wrfOBvQY6pgFdmjM7kRrfekvLaotzgNTyxrnJ0VMBSikFICc0%2BRZ9uNbpaBYQk%2BJsPtK2oqB%2FRXelt42y9hvmIODOTFQo8MGUY%2FN4cr7N0X%2FyHqvsP7vZYBxucFsKi4UH9IhuE9QOdcQXcOJiURnOsbcRT7xcxp3fPUyCK6Z%2BrdcyImAtF%2FjIba3j0TbQ2gRtWECVMgtscWC8wmSnQO9i12GDpPn3tU7WY4VzlNjg&X-Amz-Signature=8d755ada54c505df0dc6342ab77c4122eeffa239fbc3f363f34d6705a025a4ef&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FGN6ICA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfEBVF%2BwwJnhh5GLOx3G29iZqFbv5QOZsuDvKXCvySpAiBDIUkTBjc%2BKsYOGanATGxPigeqg7sEDmcFO1s%2FrfbaUSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMqWtVmbAjg1PSkfKmKtwD04adIDjqOH0P%2FMeeHMcsjEshsKEex5Aag%2BfsqNF8ibR%2F9et6a0BPMByJ6nBX52Qq1xeInMxjIuLyWFD0AIZxlJHnTTfNLSFVueZLL05NgvRIC1UWpD6aiLQWjwFA%2BQOgmggBhroMCVHwTaRfqZshjQ80ZkdxLLgEB9mJAGaXlUFHHQ7VJ7%2FqsiHNL9zLbvMlFBKCM0FUHpVGHmOZYp8LdLgUEfRJidarDw9ING3Lw9XFuljG8gMnllakYR16l77AwjjOk8s7eZ5ApMAigzsuwQdpCriu1Vt5Xc60aDVbk%2FNo0mQw2UYbtD6QtCpnqy4uVoOXPM1oRpHcQTR1UBPOaoIWHYL0MNAPlADdTd652TWotD6Ve1iOY6oIFeK51gzZrJ0KMqPDOyBl1s6ZMDxJnyC%2FfXNTtw711BUN0VOpUpelMObAEWRhaBAEKQqkV0IK8XStxjB5sqI9tHP5jXMOBf96gvOzuav0eUZZ1x%2FkXLRDWlEWjMBug3YPDf4FN9lszYjDgcJS07E77HMfpQI%2BT9OWqZBV9A4DDWMXRZcJA4mafBxxQ8LpNgskvz69%2BSrQgjWgQ63Uh%2BiMk%2FJitOSaxXJRHPx0xh3YJYhW1Cs%2BbJdxkF0HmBPl4%2Fb5Eg0wrfOBvQY6pgFdmjM7kRrfekvLaotzgNTyxrnJ0VMBSikFICc0%2BRZ9uNbpaBYQk%2BJsPtK2oqB%2FRXelt42y9hvmIODOTFQo8MGUY%2FN4cr7N0X%2FyHqvsP7vZYBxucFsKi4UH9IhuE9QOdcQXcOJiURnOsbcRT7xcxp3fPUyCK6Z%2BrdcyImAtF%2FjIba3j0TbQ2gRtWECVMgtscWC8wmSnQO9i12GDpPn3tU7WY4VzlNjg&X-Amz-Signature=9802d084f068c96376368b9f9ba284223c9476ba34eef4f349ebade89936912b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FGN6ICA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfEBVF%2BwwJnhh5GLOx3G29iZqFbv5QOZsuDvKXCvySpAiBDIUkTBjc%2BKsYOGanATGxPigeqg7sEDmcFO1s%2FrfbaUSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMqWtVmbAjg1PSkfKmKtwD04adIDjqOH0P%2FMeeHMcsjEshsKEex5Aag%2BfsqNF8ibR%2F9et6a0BPMByJ6nBX52Qq1xeInMxjIuLyWFD0AIZxlJHnTTfNLSFVueZLL05NgvRIC1UWpD6aiLQWjwFA%2BQOgmggBhroMCVHwTaRfqZshjQ80ZkdxLLgEB9mJAGaXlUFHHQ7VJ7%2FqsiHNL9zLbvMlFBKCM0FUHpVGHmOZYp8LdLgUEfRJidarDw9ING3Lw9XFuljG8gMnllakYR16l77AwjjOk8s7eZ5ApMAigzsuwQdpCriu1Vt5Xc60aDVbk%2FNo0mQw2UYbtD6QtCpnqy4uVoOXPM1oRpHcQTR1UBPOaoIWHYL0MNAPlADdTd652TWotD6Ve1iOY6oIFeK51gzZrJ0KMqPDOyBl1s6ZMDxJnyC%2FfXNTtw711BUN0VOpUpelMObAEWRhaBAEKQqkV0IK8XStxjB5sqI9tHP5jXMOBf96gvOzuav0eUZZ1x%2FkXLRDWlEWjMBug3YPDf4FN9lszYjDgcJS07E77HMfpQI%2BT9OWqZBV9A4DDWMXRZcJA4mafBxxQ8LpNgskvz69%2BSrQgjWgQ63Uh%2BiMk%2FJitOSaxXJRHPx0xh3YJYhW1Cs%2BbJdxkF0HmBPl4%2Fb5Eg0wrfOBvQY6pgFdmjM7kRrfekvLaotzgNTyxrnJ0VMBSikFICc0%2BRZ9uNbpaBYQk%2BJsPtK2oqB%2FRXelt42y9hvmIODOTFQo8MGUY%2FN4cr7N0X%2FyHqvsP7vZYBxucFsKi4UH9IhuE9QOdcQXcOJiURnOsbcRT7xcxp3fPUyCK6Z%2BrdcyImAtF%2FjIba3j0TbQ2gRtWECVMgtscWC8wmSnQO9i12GDpPn3tU7WY4VzlNjg&X-Amz-Signature=0ed7c8d18b5311a6c1b4bf678b8c4305224ddf0acda1e388afcfe8b33270ba2d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FGN6ICA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfEBVF%2BwwJnhh5GLOx3G29iZqFbv5QOZsuDvKXCvySpAiBDIUkTBjc%2BKsYOGanATGxPigeqg7sEDmcFO1s%2FrfbaUSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMqWtVmbAjg1PSkfKmKtwD04adIDjqOH0P%2FMeeHMcsjEshsKEex5Aag%2BfsqNF8ibR%2F9et6a0BPMByJ6nBX52Qq1xeInMxjIuLyWFD0AIZxlJHnTTfNLSFVueZLL05NgvRIC1UWpD6aiLQWjwFA%2BQOgmggBhroMCVHwTaRfqZshjQ80ZkdxLLgEB9mJAGaXlUFHHQ7VJ7%2FqsiHNL9zLbvMlFBKCM0FUHpVGHmOZYp8LdLgUEfRJidarDw9ING3Lw9XFuljG8gMnllakYR16l77AwjjOk8s7eZ5ApMAigzsuwQdpCriu1Vt5Xc60aDVbk%2FNo0mQw2UYbtD6QtCpnqy4uVoOXPM1oRpHcQTR1UBPOaoIWHYL0MNAPlADdTd652TWotD6Ve1iOY6oIFeK51gzZrJ0KMqPDOyBl1s6ZMDxJnyC%2FfXNTtw711BUN0VOpUpelMObAEWRhaBAEKQqkV0IK8XStxjB5sqI9tHP5jXMOBf96gvOzuav0eUZZ1x%2FkXLRDWlEWjMBug3YPDf4FN9lszYjDgcJS07E77HMfpQI%2BT9OWqZBV9A4DDWMXRZcJA4mafBxxQ8LpNgskvz69%2BSrQgjWgQ63Uh%2BiMk%2FJitOSaxXJRHPx0xh3YJYhW1Cs%2BbJdxkF0HmBPl4%2Fb5Eg0wrfOBvQY6pgFdmjM7kRrfekvLaotzgNTyxrnJ0VMBSikFICc0%2BRZ9uNbpaBYQk%2BJsPtK2oqB%2FRXelt42y9hvmIODOTFQo8MGUY%2FN4cr7N0X%2FyHqvsP7vZYBxucFsKi4UH9IhuE9QOdcQXcOJiURnOsbcRT7xcxp3fPUyCK6Z%2BrdcyImAtF%2FjIba3j0TbQ2gRtWECVMgtscWC8wmSnQO9i12GDpPn3tU7WY4VzlNjg&X-Amz-Signature=26a841f4f23fc1881231b3216913186312d157715e6f980e7c984e32fdd963b4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FGN6ICA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfEBVF%2BwwJnhh5GLOx3G29iZqFbv5QOZsuDvKXCvySpAiBDIUkTBjc%2BKsYOGanATGxPigeqg7sEDmcFO1s%2FrfbaUSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMqWtVmbAjg1PSkfKmKtwD04adIDjqOH0P%2FMeeHMcsjEshsKEex5Aag%2BfsqNF8ibR%2F9et6a0BPMByJ6nBX52Qq1xeInMxjIuLyWFD0AIZxlJHnTTfNLSFVueZLL05NgvRIC1UWpD6aiLQWjwFA%2BQOgmggBhroMCVHwTaRfqZshjQ80ZkdxLLgEB9mJAGaXlUFHHQ7VJ7%2FqsiHNL9zLbvMlFBKCM0FUHpVGHmOZYp8LdLgUEfRJidarDw9ING3Lw9XFuljG8gMnllakYR16l77AwjjOk8s7eZ5ApMAigzsuwQdpCriu1Vt5Xc60aDVbk%2FNo0mQw2UYbtD6QtCpnqy4uVoOXPM1oRpHcQTR1UBPOaoIWHYL0MNAPlADdTd652TWotD6Ve1iOY6oIFeK51gzZrJ0KMqPDOyBl1s6ZMDxJnyC%2FfXNTtw711BUN0VOpUpelMObAEWRhaBAEKQqkV0IK8XStxjB5sqI9tHP5jXMOBf96gvOzuav0eUZZ1x%2FkXLRDWlEWjMBug3YPDf4FN9lszYjDgcJS07E77HMfpQI%2BT9OWqZBV9A4DDWMXRZcJA4mafBxxQ8LpNgskvz69%2BSrQgjWgQ63Uh%2BiMk%2FJitOSaxXJRHPx0xh3YJYhW1Cs%2BbJdxkF0HmBPl4%2Fb5Eg0wrfOBvQY6pgFdmjM7kRrfekvLaotzgNTyxrnJ0VMBSikFICc0%2BRZ9uNbpaBYQk%2BJsPtK2oqB%2FRXelt42y9hvmIODOTFQo8MGUY%2FN4cr7N0X%2FyHqvsP7vZYBxucFsKi4UH9IhuE9QOdcQXcOJiURnOsbcRT7xcxp3fPUyCK6Z%2BrdcyImAtF%2FjIba3j0TbQ2gRtWECVMgtscWC8wmSnQO9i12GDpPn3tU7WY4VzlNjg&X-Amz-Signature=2ad92819e620d5c095ee86435fc120b2085959932a0ee197c689dd92582448a7&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FGN6ICA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfEBVF%2BwwJnhh5GLOx3G29iZqFbv5QOZsuDvKXCvySpAiBDIUkTBjc%2BKsYOGanATGxPigeqg7sEDmcFO1s%2FrfbaUSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMqWtVmbAjg1PSkfKmKtwD04adIDjqOH0P%2FMeeHMcsjEshsKEex5Aag%2BfsqNF8ibR%2F9et6a0BPMByJ6nBX52Qq1xeInMxjIuLyWFD0AIZxlJHnTTfNLSFVueZLL05NgvRIC1UWpD6aiLQWjwFA%2BQOgmggBhroMCVHwTaRfqZshjQ80ZkdxLLgEB9mJAGaXlUFHHQ7VJ7%2FqsiHNL9zLbvMlFBKCM0FUHpVGHmOZYp8LdLgUEfRJidarDw9ING3Lw9XFuljG8gMnllakYR16l77AwjjOk8s7eZ5ApMAigzsuwQdpCriu1Vt5Xc60aDVbk%2FNo0mQw2UYbtD6QtCpnqy4uVoOXPM1oRpHcQTR1UBPOaoIWHYL0MNAPlADdTd652TWotD6Ve1iOY6oIFeK51gzZrJ0KMqPDOyBl1s6ZMDxJnyC%2FfXNTtw711BUN0VOpUpelMObAEWRhaBAEKQqkV0IK8XStxjB5sqI9tHP5jXMOBf96gvOzuav0eUZZ1x%2FkXLRDWlEWjMBug3YPDf4FN9lszYjDgcJS07E77HMfpQI%2BT9OWqZBV9A4DDWMXRZcJA4mafBxxQ8LpNgskvz69%2BSrQgjWgQ63Uh%2BiMk%2FJitOSaxXJRHPx0xh3YJYhW1Cs%2BbJdxkF0HmBPl4%2Fb5Eg0wrfOBvQY6pgFdmjM7kRrfekvLaotzgNTyxrnJ0VMBSikFICc0%2BRZ9uNbpaBYQk%2BJsPtK2oqB%2FRXelt42y9hvmIODOTFQo8MGUY%2FN4cr7N0X%2FyHqvsP7vZYBxucFsKi4UH9IhuE9QOdcQXcOJiURnOsbcRT7xcxp3fPUyCK6Z%2BrdcyImAtF%2FjIba3j0TbQ2gRtWECVMgtscWC8wmSnQO9i12GDpPn3tU7WY4VzlNjg&X-Amz-Signature=f18e63088ed872ce9272ee4d2527dd6e06691dec909548ce33812770ceb01c9e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FGN6ICA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfEBVF%2BwwJnhh5GLOx3G29iZqFbv5QOZsuDvKXCvySpAiBDIUkTBjc%2BKsYOGanATGxPigeqg7sEDmcFO1s%2FrfbaUSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMqWtVmbAjg1PSkfKmKtwD04adIDjqOH0P%2FMeeHMcsjEshsKEex5Aag%2BfsqNF8ibR%2F9et6a0BPMByJ6nBX52Qq1xeInMxjIuLyWFD0AIZxlJHnTTfNLSFVueZLL05NgvRIC1UWpD6aiLQWjwFA%2BQOgmggBhroMCVHwTaRfqZshjQ80ZkdxLLgEB9mJAGaXlUFHHQ7VJ7%2FqsiHNL9zLbvMlFBKCM0FUHpVGHmOZYp8LdLgUEfRJidarDw9ING3Lw9XFuljG8gMnllakYR16l77AwjjOk8s7eZ5ApMAigzsuwQdpCriu1Vt5Xc60aDVbk%2FNo0mQw2UYbtD6QtCpnqy4uVoOXPM1oRpHcQTR1UBPOaoIWHYL0MNAPlADdTd652TWotD6Ve1iOY6oIFeK51gzZrJ0KMqPDOyBl1s6ZMDxJnyC%2FfXNTtw711BUN0VOpUpelMObAEWRhaBAEKQqkV0IK8XStxjB5sqI9tHP5jXMOBf96gvOzuav0eUZZ1x%2FkXLRDWlEWjMBug3YPDf4FN9lszYjDgcJS07E77HMfpQI%2BT9OWqZBV9A4DDWMXRZcJA4mafBxxQ8LpNgskvz69%2BSrQgjWgQ63Uh%2BiMk%2FJitOSaxXJRHPx0xh3YJYhW1Cs%2BbJdxkF0HmBPl4%2Fb5Eg0wrfOBvQY6pgFdmjM7kRrfekvLaotzgNTyxrnJ0VMBSikFICc0%2BRZ9uNbpaBYQk%2BJsPtK2oqB%2FRXelt42y9hvmIODOTFQo8MGUY%2FN4cr7N0X%2FyHqvsP7vZYBxucFsKi4UH9IhuE9QOdcQXcOJiURnOsbcRT7xcxp3fPUyCK6Z%2BrdcyImAtF%2FjIba3j0TbQ2gRtWECVMgtscWC8wmSnQO9i12GDpPn3tU7WY4VzlNjg&X-Amz-Signature=d0e07fc2f6a4c55133eabeb75530eb116b2039f7949908fac1a65555199c9f95&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FGN6ICA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfEBVF%2BwwJnhh5GLOx3G29iZqFbv5QOZsuDvKXCvySpAiBDIUkTBjc%2BKsYOGanATGxPigeqg7sEDmcFO1s%2FrfbaUSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMqWtVmbAjg1PSkfKmKtwD04adIDjqOH0P%2FMeeHMcsjEshsKEex5Aag%2BfsqNF8ibR%2F9et6a0BPMByJ6nBX52Qq1xeInMxjIuLyWFD0AIZxlJHnTTfNLSFVueZLL05NgvRIC1UWpD6aiLQWjwFA%2BQOgmggBhroMCVHwTaRfqZshjQ80ZkdxLLgEB9mJAGaXlUFHHQ7VJ7%2FqsiHNL9zLbvMlFBKCM0FUHpVGHmOZYp8LdLgUEfRJidarDw9ING3Lw9XFuljG8gMnllakYR16l77AwjjOk8s7eZ5ApMAigzsuwQdpCriu1Vt5Xc60aDVbk%2FNo0mQw2UYbtD6QtCpnqy4uVoOXPM1oRpHcQTR1UBPOaoIWHYL0MNAPlADdTd652TWotD6Ve1iOY6oIFeK51gzZrJ0KMqPDOyBl1s6ZMDxJnyC%2FfXNTtw711BUN0VOpUpelMObAEWRhaBAEKQqkV0IK8XStxjB5sqI9tHP5jXMOBf96gvOzuav0eUZZ1x%2FkXLRDWlEWjMBug3YPDf4FN9lszYjDgcJS07E77HMfpQI%2BT9OWqZBV9A4DDWMXRZcJA4mafBxxQ8LpNgskvz69%2BSrQgjWgQ63Uh%2BiMk%2FJitOSaxXJRHPx0xh3YJYhW1Cs%2BbJdxkF0HmBPl4%2Fb5Eg0wrfOBvQY6pgFdmjM7kRrfekvLaotzgNTyxrnJ0VMBSikFICc0%2BRZ9uNbpaBYQk%2BJsPtK2oqB%2FRXelt42y9hvmIODOTFQo8MGUY%2FN4cr7N0X%2FyHqvsP7vZYBxucFsKi4UH9IhuE9QOdcQXcOJiURnOsbcRT7xcxp3fPUyCK6Z%2BrdcyImAtF%2FjIba3j0TbQ2gRtWECVMgtscWC8wmSnQO9i12GDpPn3tU7WY4VzlNjg&X-Amz-Signature=2a99664dd2474dbfc6ae3fa98a6dbbe03152bb5b7adb55dd461e9e8276593f3d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FGN6ICA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfEBVF%2BwwJnhh5GLOx3G29iZqFbv5QOZsuDvKXCvySpAiBDIUkTBjc%2BKsYOGanATGxPigeqg7sEDmcFO1s%2FrfbaUSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMqWtVmbAjg1PSkfKmKtwD04adIDjqOH0P%2FMeeHMcsjEshsKEex5Aag%2BfsqNF8ibR%2F9et6a0BPMByJ6nBX52Qq1xeInMxjIuLyWFD0AIZxlJHnTTfNLSFVueZLL05NgvRIC1UWpD6aiLQWjwFA%2BQOgmggBhroMCVHwTaRfqZshjQ80ZkdxLLgEB9mJAGaXlUFHHQ7VJ7%2FqsiHNL9zLbvMlFBKCM0FUHpVGHmOZYp8LdLgUEfRJidarDw9ING3Lw9XFuljG8gMnllakYR16l77AwjjOk8s7eZ5ApMAigzsuwQdpCriu1Vt5Xc60aDVbk%2FNo0mQw2UYbtD6QtCpnqy4uVoOXPM1oRpHcQTR1UBPOaoIWHYL0MNAPlADdTd652TWotD6Ve1iOY6oIFeK51gzZrJ0KMqPDOyBl1s6ZMDxJnyC%2FfXNTtw711BUN0VOpUpelMObAEWRhaBAEKQqkV0IK8XStxjB5sqI9tHP5jXMOBf96gvOzuav0eUZZ1x%2FkXLRDWlEWjMBug3YPDf4FN9lszYjDgcJS07E77HMfpQI%2BT9OWqZBV9A4DDWMXRZcJA4mafBxxQ8LpNgskvz69%2BSrQgjWgQ63Uh%2BiMk%2FJitOSaxXJRHPx0xh3YJYhW1Cs%2BbJdxkF0HmBPl4%2Fb5Eg0wrfOBvQY6pgFdmjM7kRrfekvLaotzgNTyxrnJ0VMBSikFICc0%2BRZ9uNbpaBYQk%2BJsPtK2oqB%2FRXelt42y9hvmIODOTFQo8MGUY%2FN4cr7N0X%2FyHqvsP7vZYBxucFsKi4UH9IhuE9QOdcQXcOJiURnOsbcRT7xcxp3fPUyCK6Z%2BrdcyImAtF%2FjIba3j0TbQ2gRtWECVMgtscWC8wmSnQO9i12GDpPn3tU7WY4VzlNjg&X-Amz-Signature=e262092d52f4fbe78ec6c97350611b2ee105463295e11cdd963c430cef4ca05e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVEHMAZT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpwfqHoS%2FttjV1Rd2dwDzlz4jViiZxVofnywyy4y4ZuAIhANdGKc9S1v3S8MSpWiViwEXItUv2TmhJJlFNIuqfSzIZKv8DCBEQABoMNjM3NDIzMTgzODA1IgxVvWeVgHgrEpt0FI4q3AMSJzsLseVo4RerMqFc0B1XuI0CIjr1XL%2FMITcqHlDMvBmezl5rY42hAvzSKdXzRMGIt0zFfT%2FP65hvlT%2F%2Fa0KN4ySYpg%2FXtHkuWD4zvDp7B68ZhGJJBSfaE0tErTni6lEPUWHZj8wr5AlYo0Crpd%2Fzxh49HwAcmX1B8HF7MvBnYQZI4neX3y4q57sQ6bwfjZX6cXf234inm8Dcx%2FS3%2BVgfsIHZQVnUu9rewuCByN1w82YakKUQe%2FhhxRMPrww8Pd3nbbn9GYsLu2Ocip2Wcsc9BRW0abBRoDXRA9z8eKOGHYcYCFWf22ShchnVceg0I%2Fa4CfFA6OzTv1ldMdW1tkwqzzN6qGNV2EbjWI9J4fcpgpIdlQY5sh8xPDSIIHhgc6mzLDH76k3DiVxzctF7hnZapxIFWPL3JDBepU3R3jRprfSaZETBPJA9Ey7a8WPOkccFU8ovgwo9cNa%2B03ivNuOovH1jU2e%2F3A6Gyzv7ZMjTiN8zxoIzO%2FRaaM1cNLhGRZO9RiEvg%2BF5kMTiZX0uBEHALXvx9FKgZjTENf022Gtqz%2Fq0EDe3DVLhiem3ZihpIcYOpiJpLs%2FmEoLj5gTAJE6AO3jFGVFz7nS%2Bi07cbuliyqx45qSjlLWqOTX7ODCg84G9BjqkAS3iVTbd5W28sW7d4XLs%2FTadRLGDV53uEOBbbwRWQAyJaytCjOYI9T68yMGyd37DZ4MSMduHQcsu%2FBmhKiQ5Pvtodc4r2SJ%2BicfgeKEwa4VRJuvUWUGsD0S56DMEc3nStTjRO2K5EOb963TS2gswSngvWIfwBk5ppsppl%2FRzTlbZXDWpw3XfbLjTo2NPOeQqqxQ0WpnSdoZwB5ceIngFfReRFaLe&X-Amz-Signature=a5b1c1baf5ce4f2b319353ef8cf48c8e35181a741bf7175a3caf53c7273b9ea7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVEHMAZT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpwfqHoS%2FttjV1Rd2dwDzlz4jViiZxVofnywyy4y4ZuAIhANdGKc9S1v3S8MSpWiViwEXItUv2TmhJJlFNIuqfSzIZKv8DCBEQABoMNjM3NDIzMTgzODA1IgxVvWeVgHgrEpt0FI4q3AMSJzsLseVo4RerMqFc0B1XuI0CIjr1XL%2FMITcqHlDMvBmezl5rY42hAvzSKdXzRMGIt0zFfT%2FP65hvlT%2F%2Fa0KN4ySYpg%2FXtHkuWD4zvDp7B68ZhGJJBSfaE0tErTni6lEPUWHZj8wr5AlYo0Crpd%2Fzxh49HwAcmX1B8HF7MvBnYQZI4neX3y4q57sQ6bwfjZX6cXf234inm8Dcx%2FS3%2BVgfsIHZQVnUu9rewuCByN1w82YakKUQe%2FhhxRMPrww8Pd3nbbn9GYsLu2Ocip2Wcsc9BRW0abBRoDXRA9z8eKOGHYcYCFWf22ShchnVceg0I%2Fa4CfFA6OzTv1ldMdW1tkwqzzN6qGNV2EbjWI9J4fcpgpIdlQY5sh8xPDSIIHhgc6mzLDH76k3DiVxzctF7hnZapxIFWPL3JDBepU3R3jRprfSaZETBPJA9Ey7a8WPOkccFU8ovgwo9cNa%2B03ivNuOovH1jU2e%2F3A6Gyzv7ZMjTiN8zxoIzO%2FRaaM1cNLhGRZO9RiEvg%2BF5kMTiZX0uBEHALXvx9FKgZjTENf022Gtqz%2Fq0EDe3DVLhiem3ZihpIcYOpiJpLs%2FmEoLj5gTAJE6AO3jFGVFz7nS%2Bi07cbuliyqx45qSjlLWqOTX7ODCg84G9BjqkAS3iVTbd5W28sW7d4XLs%2FTadRLGDV53uEOBbbwRWQAyJaytCjOYI9T68yMGyd37DZ4MSMduHQcsu%2FBmhKiQ5Pvtodc4r2SJ%2BicfgeKEwa4VRJuvUWUGsD0S56DMEc3nStTjRO2K5EOb963TS2gswSngvWIfwBk5ppsppl%2FRzTlbZXDWpw3XfbLjTo2NPOeQqqxQ0WpnSdoZwB5ceIngFfReRFaLe&X-Amz-Signature=02d8b9b1909e04f864903e841bc0db79ec8a88afdbb51f7f7d4a9177f943e8d0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
