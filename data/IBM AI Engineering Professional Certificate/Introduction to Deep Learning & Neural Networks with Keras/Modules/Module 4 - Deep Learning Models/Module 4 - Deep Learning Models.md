

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQBDR4FA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDY2D2jMghcYGMj1RHyF8CxarZHB9GP8ihQNlePcV50uAiEA0sqKjb76Clkf5XRo0O3%2B8gcks4bffgVF%2BfDIfTIT22UqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJIvRnvmtdYcpLX5yrcA%2Bfqtep%2FXruHYRdsHg%2BdzJOGeDO1WZ5h8ZsDBFs6lahtRpEhxC0Nvn6tm4ez8dzjy9nxH9wm61iFyjrY%2FUIgiKoaoVwGOs9tb1VjdCUzEk2PjRtU1Ah1UxIVBm%2Bs%2BwN207f1F%2F0KwyT%2Fj7bIbvRGhJHeSUp8L4bLUY6uh5e0Id4jCanmIT3a8O4Hpdj9d43eOqrKzJjRZS6QB5LzQzfiKxQdHIy0%2B2jlvUW7dcKizNCpAfz2igNEV%2FZhdN%2FlXK7pQrFTpb0Nzo2RnM%2FILS8cIQgUtBSHlBRGiRZBw3z3sBXdCHAqNhVNk%2FFMoftoSoA7kYwwAoljcrgWCNc7QqLoZyO4jTNn6c2pgn6m10vKz218iVgQM3jikxd2pHHA3Qf4M0%2FcT3RjzyFR6RY3bfdNcXziKrNIBtc92rW7qV84Bt0r0F1jdW7vPK7bSf%2FZX80pK%2FOQFIMpdY8XtuXA7R1k%2FCPuwnTHnpGN8Epkr%2FnUy54vJT33PkYuxm%2FFwMK9ZFlJxuN1fLQqxmlxryfxyjIUiZeQIaoHjjxVEOZeNkrXLw%2FouT5ozKrWm5ZiskAszaocW9l2YZvRXhk2CF%2FXVtMzxCt4EvBDwRm2JLw9N5VA51RFSww4O4c9EbN5UoTTML2k97wGOqUB6Ogbc3Ksl%2BtURLwV73LqPe7KSeIf%2FPTHI0aWIa1rnGRhG8H4TMxlZNwaqnDIyXqZtld3N17WH5U4aLeay2i7jrU%2FSv%2B9qVEiX9PSK%2BD0zSTOa%2FIgkRD0cLJ1WE1ZznnXYvWX6x3RzQx6mq3oEo11pIjxGtzrErdek9NKwqwHIyDiIfOWwOe4kEzDHIywrH6pNW3p7eZ4OZvuIlCGQ755l1kAUUjq&X-Amz-Signature=f734646146bd1554b865460c1af6692cf4f69a687d553e948209dd9a0523ece6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQBDR4FA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDY2D2jMghcYGMj1RHyF8CxarZHB9GP8ihQNlePcV50uAiEA0sqKjb76Clkf5XRo0O3%2B8gcks4bffgVF%2BfDIfTIT22UqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJIvRnvmtdYcpLX5yrcA%2Bfqtep%2FXruHYRdsHg%2BdzJOGeDO1WZ5h8ZsDBFs6lahtRpEhxC0Nvn6tm4ez8dzjy9nxH9wm61iFyjrY%2FUIgiKoaoVwGOs9tb1VjdCUzEk2PjRtU1Ah1UxIVBm%2Bs%2BwN207f1F%2F0KwyT%2Fj7bIbvRGhJHeSUp8L4bLUY6uh5e0Id4jCanmIT3a8O4Hpdj9d43eOqrKzJjRZS6QB5LzQzfiKxQdHIy0%2B2jlvUW7dcKizNCpAfz2igNEV%2FZhdN%2FlXK7pQrFTpb0Nzo2RnM%2FILS8cIQgUtBSHlBRGiRZBw3z3sBXdCHAqNhVNk%2FFMoftoSoA7kYwwAoljcrgWCNc7QqLoZyO4jTNn6c2pgn6m10vKz218iVgQM3jikxd2pHHA3Qf4M0%2FcT3RjzyFR6RY3bfdNcXziKrNIBtc92rW7qV84Bt0r0F1jdW7vPK7bSf%2FZX80pK%2FOQFIMpdY8XtuXA7R1k%2FCPuwnTHnpGN8Epkr%2FnUy54vJT33PkYuxm%2FFwMK9ZFlJxuN1fLQqxmlxryfxyjIUiZeQIaoHjjxVEOZeNkrXLw%2FouT5ozKrWm5ZiskAszaocW9l2YZvRXhk2CF%2FXVtMzxCt4EvBDwRm2JLw9N5VA51RFSww4O4c9EbN5UoTTML2k97wGOqUB6Ogbc3Ksl%2BtURLwV73LqPe7KSeIf%2FPTHI0aWIa1rnGRhG8H4TMxlZNwaqnDIyXqZtld3N17WH5U4aLeay2i7jrU%2FSv%2B9qVEiX9PSK%2BD0zSTOa%2FIgkRD0cLJ1WE1ZznnXYvWX6x3RzQx6mq3oEo11pIjxGtzrErdek9NKwqwHIyDiIfOWwOe4kEzDHIywrH6pNW3p7eZ4OZvuIlCGQ755l1kAUUjq&X-Amz-Signature=a45598c2dbfac21cc864e833e5db11a617dcfe2d5391319f529aa282a6859745&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQBDR4FA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDY2D2jMghcYGMj1RHyF8CxarZHB9GP8ihQNlePcV50uAiEA0sqKjb76Clkf5XRo0O3%2B8gcks4bffgVF%2BfDIfTIT22UqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJIvRnvmtdYcpLX5yrcA%2Bfqtep%2FXruHYRdsHg%2BdzJOGeDO1WZ5h8ZsDBFs6lahtRpEhxC0Nvn6tm4ez8dzjy9nxH9wm61iFyjrY%2FUIgiKoaoVwGOs9tb1VjdCUzEk2PjRtU1Ah1UxIVBm%2Bs%2BwN207f1F%2F0KwyT%2Fj7bIbvRGhJHeSUp8L4bLUY6uh5e0Id4jCanmIT3a8O4Hpdj9d43eOqrKzJjRZS6QB5LzQzfiKxQdHIy0%2B2jlvUW7dcKizNCpAfz2igNEV%2FZhdN%2FlXK7pQrFTpb0Nzo2RnM%2FILS8cIQgUtBSHlBRGiRZBw3z3sBXdCHAqNhVNk%2FFMoftoSoA7kYwwAoljcrgWCNc7QqLoZyO4jTNn6c2pgn6m10vKz218iVgQM3jikxd2pHHA3Qf4M0%2FcT3RjzyFR6RY3bfdNcXziKrNIBtc92rW7qV84Bt0r0F1jdW7vPK7bSf%2FZX80pK%2FOQFIMpdY8XtuXA7R1k%2FCPuwnTHnpGN8Epkr%2FnUy54vJT33PkYuxm%2FFwMK9ZFlJxuN1fLQqxmlxryfxyjIUiZeQIaoHjjxVEOZeNkrXLw%2FouT5ozKrWm5ZiskAszaocW9l2YZvRXhk2CF%2FXVtMzxCt4EvBDwRm2JLw9N5VA51RFSww4O4c9EbN5UoTTML2k97wGOqUB6Ogbc3Ksl%2BtURLwV73LqPe7KSeIf%2FPTHI0aWIa1rnGRhG8H4TMxlZNwaqnDIyXqZtld3N17WH5U4aLeay2i7jrU%2FSv%2B9qVEiX9PSK%2BD0zSTOa%2FIgkRD0cLJ1WE1ZznnXYvWX6x3RzQx6mq3oEo11pIjxGtzrErdek9NKwqwHIyDiIfOWwOe4kEzDHIywrH6pNW3p7eZ4OZvuIlCGQ755l1kAUUjq&X-Amz-Signature=01238c84f4aa16c3f960f5331d4e01811d1648677ec753e00306cd2d7a90035d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQBDR4FA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDY2D2jMghcYGMj1RHyF8CxarZHB9GP8ihQNlePcV50uAiEA0sqKjb76Clkf5XRo0O3%2B8gcks4bffgVF%2BfDIfTIT22UqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJIvRnvmtdYcpLX5yrcA%2Bfqtep%2FXruHYRdsHg%2BdzJOGeDO1WZ5h8ZsDBFs6lahtRpEhxC0Nvn6tm4ez8dzjy9nxH9wm61iFyjrY%2FUIgiKoaoVwGOs9tb1VjdCUzEk2PjRtU1Ah1UxIVBm%2Bs%2BwN207f1F%2F0KwyT%2Fj7bIbvRGhJHeSUp8L4bLUY6uh5e0Id4jCanmIT3a8O4Hpdj9d43eOqrKzJjRZS6QB5LzQzfiKxQdHIy0%2B2jlvUW7dcKizNCpAfz2igNEV%2FZhdN%2FlXK7pQrFTpb0Nzo2RnM%2FILS8cIQgUtBSHlBRGiRZBw3z3sBXdCHAqNhVNk%2FFMoftoSoA7kYwwAoljcrgWCNc7QqLoZyO4jTNn6c2pgn6m10vKz218iVgQM3jikxd2pHHA3Qf4M0%2FcT3RjzyFR6RY3bfdNcXziKrNIBtc92rW7qV84Bt0r0F1jdW7vPK7bSf%2FZX80pK%2FOQFIMpdY8XtuXA7R1k%2FCPuwnTHnpGN8Epkr%2FnUy54vJT33PkYuxm%2FFwMK9ZFlJxuN1fLQqxmlxryfxyjIUiZeQIaoHjjxVEOZeNkrXLw%2FouT5ozKrWm5ZiskAszaocW9l2YZvRXhk2CF%2FXVtMzxCt4EvBDwRm2JLw9N5VA51RFSww4O4c9EbN5UoTTML2k97wGOqUB6Ogbc3Ksl%2BtURLwV73LqPe7KSeIf%2FPTHI0aWIa1rnGRhG8H4TMxlZNwaqnDIyXqZtld3N17WH5U4aLeay2i7jrU%2FSv%2B9qVEiX9PSK%2BD0zSTOa%2FIgkRD0cLJ1WE1ZznnXYvWX6x3RzQx6mq3oEo11pIjxGtzrErdek9NKwqwHIyDiIfOWwOe4kEzDHIywrH6pNW3p7eZ4OZvuIlCGQ755l1kAUUjq&X-Amz-Signature=93cb2dbcc50c5acf39a70515f08496936c86f6d16040309c58fc7285ab54bb42&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQBDR4FA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDY2D2jMghcYGMj1RHyF8CxarZHB9GP8ihQNlePcV50uAiEA0sqKjb76Clkf5XRo0O3%2B8gcks4bffgVF%2BfDIfTIT22UqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJIvRnvmtdYcpLX5yrcA%2Bfqtep%2FXruHYRdsHg%2BdzJOGeDO1WZ5h8ZsDBFs6lahtRpEhxC0Nvn6tm4ez8dzjy9nxH9wm61iFyjrY%2FUIgiKoaoVwGOs9tb1VjdCUzEk2PjRtU1Ah1UxIVBm%2Bs%2BwN207f1F%2F0KwyT%2Fj7bIbvRGhJHeSUp8L4bLUY6uh5e0Id4jCanmIT3a8O4Hpdj9d43eOqrKzJjRZS6QB5LzQzfiKxQdHIy0%2B2jlvUW7dcKizNCpAfz2igNEV%2FZhdN%2FlXK7pQrFTpb0Nzo2RnM%2FILS8cIQgUtBSHlBRGiRZBw3z3sBXdCHAqNhVNk%2FFMoftoSoA7kYwwAoljcrgWCNc7QqLoZyO4jTNn6c2pgn6m10vKz218iVgQM3jikxd2pHHA3Qf4M0%2FcT3RjzyFR6RY3bfdNcXziKrNIBtc92rW7qV84Bt0r0F1jdW7vPK7bSf%2FZX80pK%2FOQFIMpdY8XtuXA7R1k%2FCPuwnTHnpGN8Epkr%2FnUy54vJT33PkYuxm%2FFwMK9ZFlJxuN1fLQqxmlxryfxyjIUiZeQIaoHjjxVEOZeNkrXLw%2FouT5ozKrWm5ZiskAszaocW9l2YZvRXhk2CF%2FXVtMzxCt4EvBDwRm2JLw9N5VA51RFSww4O4c9EbN5UoTTML2k97wGOqUB6Ogbc3Ksl%2BtURLwV73LqPe7KSeIf%2FPTHI0aWIa1rnGRhG8H4TMxlZNwaqnDIyXqZtld3N17WH5U4aLeay2i7jrU%2FSv%2B9qVEiX9PSK%2BD0zSTOa%2FIgkRD0cLJ1WE1ZznnXYvWX6x3RzQx6mq3oEo11pIjxGtzrErdek9NKwqwHIyDiIfOWwOe4kEzDHIywrH6pNW3p7eZ4OZvuIlCGQ755l1kAUUjq&X-Amz-Signature=7600b526ab7e94b78257104d85713d71f8f1f13d70cecec8f618e7a172249375&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQBDR4FA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDY2D2jMghcYGMj1RHyF8CxarZHB9GP8ihQNlePcV50uAiEA0sqKjb76Clkf5XRo0O3%2B8gcks4bffgVF%2BfDIfTIT22UqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJIvRnvmtdYcpLX5yrcA%2Bfqtep%2FXruHYRdsHg%2BdzJOGeDO1WZ5h8ZsDBFs6lahtRpEhxC0Nvn6tm4ez8dzjy9nxH9wm61iFyjrY%2FUIgiKoaoVwGOs9tb1VjdCUzEk2PjRtU1Ah1UxIVBm%2Bs%2BwN207f1F%2F0KwyT%2Fj7bIbvRGhJHeSUp8L4bLUY6uh5e0Id4jCanmIT3a8O4Hpdj9d43eOqrKzJjRZS6QB5LzQzfiKxQdHIy0%2B2jlvUW7dcKizNCpAfz2igNEV%2FZhdN%2FlXK7pQrFTpb0Nzo2RnM%2FILS8cIQgUtBSHlBRGiRZBw3z3sBXdCHAqNhVNk%2FFMoftoSoA7kYwwAoljcrgWCNc7QqLoZyO4jTNn6c2pgn6m10vKz218iVgQM3jikxd2pHHA3Qf4M0%2FcT3RjzyFR6RY3bfdNcXziKrNIBtc92rW7qV84Bt0r0F1jdW7vPK7bSf%2FZX80pK%2FOQFIMpdY8XtuXA7R1k%2FCPuwnTHnpGN8Epkr%2FnUy54vJT33PkYuxm%2FFwMK9ZFlJxuN1fLQqxmlxryfxyjIUiZeQIaoHjjxVEOZeNkrXLw%2FouT5ozKrWm5ZiskAszaocW9l2YZvRXhk2CF%2FXVtMzxCt4EvBDwRm2JLw9N5VA51RFSww4O4c9EbN5UoTTML2k97wGOqUB6Ogbc3Ksl%2BtURLwV73LqPe7KSeIf%2FPTHI0aWIa1rnGRhG8H4TMxlZNwaqnDIyXqZtld3N17WH5U4aLeay2i7jrU%2FSv%2B9qVEiX9PSK%2BD0zSTOa%2FIgkRD0cLJ1WE1ZznnXYvWX6x3RzQx6mq3oEo11pIjxGtzrErdek9NKwqwHIyDiIfOWwOe4kEzDHIywrH6pNW3p7eZ4OZvuIlCGQ755l1kAUUjq&X-Amz-Signature=9af9b4565760d67bb6b871f16cfc85243a5c845f940d93928af973d3f983d502&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQBDR4FA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDY2D2jMghcYGMj1RHyF8CxarZHB9GP8ihQNlePcV50uAiEA0sqKjb76Clkf5XRo0O3%2B8gcks4bffgVF%2BfDIfTIT22UqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJIvRnvmtdYcpLX5yrcA%2Bfqtep%2FXruHYRdsHg%2BdzJOGeDO1WZ5h8ZsDBFs6lahtRpEhxC0Nvn6tm4ez8dzjy9nxH9wm61iFyjrY%2FUIgiKoaoVwGOs9tb1VjdCUzEk2PjRtU1Ah1UxIVBm%2Bs%2BwN207f1F%2F0KwyT%2Fj7bIbvRGhJHeSUp8L4bLUY6uh5e0Id4jCanmIT3a8O4Hpdj9d43eOqrKzJjRZS6QB5LzQzfiKxQdHIy0%2B2jlvUW7dcKizNCpAfz2igNEV%2FZhdN%2FlXK7pQrFTpb0Nzo2RnM%2FILS8cIQgUtBSHlBRGiRZBw3z3sBXdCHAqNhVNk%2FFMoftoSoA7kYwwAoljcrgWCNc7QqLoZyO4jTNn6c2pgn6m10vKz218iVgQM3jikxd2pHHA3Qf4M0%2FcT3RjzyFR6RY3bfdNcXziKrNIBtc92rW7qV84Bt0r0F1jdW7vPK7bSf%2FZX80pK%2FOQFIMpdY8XtuXA7R1k%2FCPuwnTHnpGN8Epkr%2FnUy54vJT33PkYuxm%2FFwMK9ZFlJxuN1fLQqxmlxryfxyjIUiZeQIaoHjjxVEOZeNkrXLw%2FouT5ozKrWm5ZiskAszaocW9l2YZvRXhk2CF%2FXVtMzxCt4EvBDwRm2JLw9N5VA51RFSww4O4c9EbN5UoTTML2k97wGOqUB6Ogbc3Ksl%2BtURLwV73LqPe7KSeIf%2FPTHI0aWIa1rnGRhG8H4TMxlZNwaqnDIyXqZtld3N17WH5U4aLeay2i7jrU%2FSv%2B9qVEiX9PSK%2BD0zSTOa%2FIgkRD0cLJ1WE1ZznnXYvWX6x3RzQx6mq3oEo11pIjxGtzrErdek9NKwqwHIyDiIfOWwOe4kEzDHIywrH6pNW3p7eZ4OZvuIlCGQ755l1kAUUjq&X-Amz-Signature=a4c5e09b701bd410de5ff3b193e2811b5d8415689e5e1a9e26e4b25fe65340e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQBDR4FA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDY2D2jMghcYGMj1RHyF8CxarZHB9GP8ihQNlePcV50uAiEA0sqKjb76Clkf5XRo0O3%2B8gcks4bffgVF%2BfDIfTIT22UqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJIvRnvmtdYcpLX5yrcA%2Bfqtep%2FXruHYRdsHg%2BdzJOGeDO1WZ5h8ZsDBFs6lahtRpEhxC0Nvn6tm4ez8dzjy9nxH9wm61iFyjrY%2FUIgiKoaoVwGOs9tb1VjdCUzEk2PjRtU1Ah1UxIVBm%2Bs%2BwN207f1F%2F0KwyT%2Fj7bIbvRGhJHeSUp8L4bLUY6uh5e0Id4jCanmIT3a8O4Hpdj9d43eOqrKzJjRZS6QB5LzQzfiKxQdHIy0%2B2jlvUW7dcKizNCpAfz2igNEV%2FZhdN%2FlXK7pQrFTpb0Nzo2RnM%2FILS8cIQgUtBSHlBRGiRZBw3z3sBXdCHAqNhVNk%2FFMoftoSoA7kYwwAoljcrgWCNc7QqLoZyO4jTNn6c2pgn6m10vKz218iVgQM3jikxd2pHHA3Qf4M0%2FcT3RjzyFR6RY3bfdNcXziKrNIBtc92rW7qV84Bt0r0F1jdW7vPK7bSf%2FZX80pK%2FOQFIMpdY8XtuXA7R1k%2FCPuwnTHnpGN8Epkr%2FnUy54vJT33PkYuxm%2FFwMK9ZFlJxuN1fLQqxmlxryfxyjIUiZeQIaoHjjxVEOZeNkrXLw%2FouT5ozKrWm5ZiskAszaocW9l2YZvRXhk2CF%2FXVtMzxCt4EvBDwRm2JLw9N5VA51RFSww4O4c9EbN5UoTTML2k97wGOqUB6Ogbc3Ksl%2BtURLwV73LqPe7KSeIf%2FPTHI0aWIa1rnGRhG8H4TMxlZNwaqnDIyXqZtld3N17WH5U4aLeay2i7jrU%2FSv%2B9qVEiX9PSK%2BD0zSTOa%2FIgkRD0cLJ1WE1ZznnXYvWX6x3RzQx6mq3oEo11pIjxGtzrErdek9NKwqwHIyDiIfOWwOe4kEzDHIywrH6pNW3p7eZ4OZvuIlCGQ755l1kAUUjq&X-Amz-Signature=b93cf35b8fcf75c3c01d3356b6f07b9762f62a08868dc8b1f68f88da40c44211&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQBDR4FA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDY2D2jMghcYGMj1RHyF8CxarZHB9GP8ihQNlePcV50uAiEA0sqKjb76Clkf5XRo0O3%2B8gcks4bffgVF%2BfDIfTIT22UqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJIvRnvmtdYcpLX5yrcA%2Bfqtep%2FXruHYRdsHg%2BdzJOGeDO1WZ5h8ZsDBFs6lahtRpEhxC0Nvn6tm4ez8dzjy9nxH9wm61iFyjrY%2FUIgiKoaoVwGOs9tb1VjdCUzEk2PjRtU1Ah1UxIVBm%2Bs%2BwN207f1F%2F0KwyT%2Fj7bIbvRGhJHeSUp8L4bLUY6uh5e0Id4jCanmIT3a8O4Hpdj9d43eOqrKzJjRZS6QB5LzQzfiKxQdHIy0%2B2jlvUW7dcKizNCpAfz2igNEV%2FZhdN%2FlXK7pQrFTpb0Nzo2RnM%2FILS8cIQgUtBSHlBRGiRZBw3z3sBXdCHAqNhVNk%2FFMoftoSoA7kYwwAoljcrgWCNc7QqLoZyO4jTNn6c2pgn6m10vKz218iVgQM3jikxd2pHHA3Qf4M0%2FcT3RjzyFR6RY3bfdNcXziKrNIBtc92rW7qV84Bt0r0F1jdW7vPK7bSf%2FZX80pK%2FOQFIMpdY8XtuXA7R1k%2FCPuwnTHnpGN8Epkr%2FnUy54vJT33PkYuxm%2FFwMK9ZFlJxuN1fLQqxmlxryfxyjIUiZeQIaoHjjxVEOZeNkrXLw%2FouT5ozKrWm5ZiskAszaocW9l2YZvRXhk2CF%2FXVtMzxCt4EvBDwRm2JLw9N5VA51RFSww4O4c9EbN5UoTTML2k97wGOqUB6Ogbc3Ksl%2BtURLwV73LqPe7KSeIf%2FPTHI0aWIa1rnGRhG8H4TMxlZNwaqnDIyXqZtld3N17WH5U4aLeay2i7jrU%2FSv%2B9qVEiX9PSK%2BD0zSTOa%2FIgkRD0cLJ1WE1ZznnXYvWX6x3RzQx6mq3oEo11pIjxGtzrErdek9NKwqwHIyDiIfOWwOe4kEzDHIywrH6pNW3p7eZ4OZvuIlCGQ755l1kAUUjq&X-Amz-Signature=809286d725aed65b421cf419f263797c3a19ade77268c9c2efb114549b40d450&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FNG4ZCW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICeXe1X8g0BmNXgxxGM638J3C9Nsypr%2FLnOXh1Mg%2B2irAiEAqEYjRGIyNV%2Boyv5Cn8JiP0pVoXHuLgl8L0NhI6E1yZUqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBZ7vk2Oe%2FQWNV%2FqCrcA6QybI1Yxp3ooaaFW%2FTnOgLImn%2BgbLWVJDDXlb76jYUdVXos6t1UAbeQGLWuliyxbx4LiDUnBq%2FmseNZ3yeXXrfyQsk81XevIglIqZ0CY7SMmlkYcyKgqGj7YimJHrDvk64%2F2y3KYxU9Yu2E0SRr%2FMAbMcFxONOtrNdfv7rkoONvHNMRW4rKUDMloyzmvoFPuEcVI%2FdCVTpMrbC3zV0kf5bNUHU4qBRvh6eduOn2kddgm8IuuUhfQFrjyftrd3PbBNg%2B6bd8hIuNblwnLoaeVEI5j5jcNXMyn9VX7UpMNONJjv3RZH3nxnbswxybnSMftTYn03Y2xxutkhAZ%2B1YRHUEoEOk%2Fv9xJl303%2BOFenfWf%2BzB5oxEE8%2FXNaF9D18au3JnGZuXuDLqgmdeu3ZVJ7ELWBonj0RR9kdCV5bU7nLiuSq4eqAgiqbV8KVQM2Iy43VB8qBZNYjCVwrFYEs20XfdBe8sQC1Z9wmqT0r8N%2FlMJtLYSzly5VKGY2tnOWpFxn8nu7qcGMs2afkIjqNSEGf%2FA%2BAFnVb4sRQgqG%2FFuONxUpZqEZWVV0lgXhzZkihchzL0O3Z3lmiyW1v6PoyeWkYsc5nXSp%2BfFrdwE1g30uLWLfe%2Fvwnwz%2BMq1heA7MN2k97wGOqUBTJlqVTrxOE8lTq5ctvgc7QsfVl0UXNYScaK8FD2v8GIzX7BufIFEx%2Fte8B8Kau%2F5X19JoF8fhY1Oo9z2nxtWnhoClGAKAkDglvFGyjWxUvRMrLzgwNr%2FcYx20LmnBQofVtUvzF3kjrPXFjBlviwqW2XX8Wno8wW658JvFNFbCeIouqtm5Jo%2BRJ1JBrQmRxm9TzdrHYZQnoiMHdTvl5dRO20as9FG&X-Amz-Signature=330143d014b6f4a5c77eb531a555067c5bd091739af2d904f10808c555f69d1f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FNG4ZCW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICeXe1X8g0BmNXgxxGM638J3C9Nsypr%2FLnOXh1Mg%2B2irAiEAqEYjRGIyNV%2Boyv5Cn8JiP0pVoXHuLgl8L0NhI6E1yZUqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBZ7vk2Oe%2FQWNV%2FqCrcA6QybI1Yxp3ooaaFW%2FTnOgLImn%2BgbLWVJDDXlb76jYUdVXos6t1UAbeQGLWuliyxbx4LiDUnBq%2FmseNZ3yeXXrfyQsk81XevIglIqZ0CY7SMmlkYcyKgqGj7YimJHrDvk64%2F2y3KYxU9Yu2E0SRr%2FMAbMcFxONOtrNdfv7rkoONvHNMRW4rKUDMloyzmvoFPuEcVI%2FdCVTpMrbC3zV0kf5bNUHU4qBRvh6eduOn2kddgm8IuuUhfQFrjyftrd3PbBNg%2B6bd8hIuNblwnLoaeVEI5j5jcNXMyn9VX7UpMNONJjv3RZH3nxnbswxybnSMftTYn03Y2xxutkhAZ%2B1YRHUEoEOk%2Fv9xJl303%2BOFenfWf%2BzB5oxEE8%2FXNaF9D18au3JnGZuXuDLqgmdeu3ZVJ7ELWBonj0RR9kdCV5bU7nLiuSq4eqAgiqbV8KVQM2Iy43VB8qBZNYjCVwrFYEs20XfdBe8sQC1Z9wmqT0r8N%2FlMJtLYSzly5VKGY2tnOWpFxn8nu7qcGMs2afkIjqNSEGf%2FA%2BAFnVb4sRQgqG%2FFuONxUpZqEZWVV0lgXhzZkihchzL0O3Z3lmiyW1v6PoyeWkYsc5nXSp%2BfFrdwE1g30uLWLfe%2Fvwnwz%2BMq1heA7MN2k97wGOqUBTJlqVTrxOE8lTq5ctvgc7QsfVl0UXNYScaK8FD2v8GIzX7BufIFEx%2Fte8B8Kau%2F5X19JoF8fhY1Oo9z2nxtWnhoClGAKAkDglvFGyjWxUvRMrLzgwNr%2FcYx20LmnBQofVtUvzF3kjrPXFjBlviwqW2XX8Wno8wW658JvFNFbCeIouqtm5Jo%2BRJ1JBrQmRxm9TzdrHYZQnoiMHdTvl5dRO20as9FG&X-Amz-Signature=582da75802116efe3dd281f5f6e7b7aa8a8de2cde8486b30f125770164c018fc&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
