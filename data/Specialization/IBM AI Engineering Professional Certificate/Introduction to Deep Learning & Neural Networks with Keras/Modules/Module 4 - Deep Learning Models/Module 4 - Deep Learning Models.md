

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBEHJOGV%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIGIMdKZBqpaAR6m1x3qILVX8wdOo7BemOmzMIXCP%2Fux9AiBBE%2BbIFy5RC24JsajCTqAhIHX40m7K28hj4Z1445Bwdir%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMK5uSU0lLd0DpuIIDKtwDkWBzL0x3rgdS1Yi%2FF%2B7zVcXrA7%2BSigLhVv4RmQj%2BO41pnkbeJtWZcNhDxHADOnhch8Jm46jAXoMO8AnAehMKqOmxnCvJOHjmi6kT5h5k%2F%2FFeUnC0rloHk56Hs%2F4VZFAm0oKtsHZcOY0zZY7U%2B2lAumkC29RvwgrnDQSKnc6NAxiH0mfCgyE%2FF44jdL4S8spenIeNOHUb3HT%2BkkX9hYuIYrUlP3zjsAJgDGV7%2FEdWr8rUJa%2FIKCV9HyTRpHoGPMfI9lwOx3QN9hJfMUUhyPkcikUsPyN9z6dBAZkpJu%2FTKJCgtWt4Goi7zbmXIaY0PquHBfl8XxaUJAUE5pZpaTWwbozq8a9O9niDUdqPWA56f3gz%2BhWZIycrAa6%2FtENIuDTncgSUHxiPDBr3FpAmofcRGoF0n9nJqkdp7Tu9vEaSvt3O2%2Bla7r9Hz9w7dUaRxZsx7uSiYEUHoUabr8j1gjdceK5dEHSK2NckHTl9CoQV%2F47kO0vE2kbaE0KAzFHqzPBDv2b9oLJCFkZLfimN%2FpZSIyorXBlot0e%2B9xSNIshHepMer1VCL9xzbyi0qKPMJSHRWT7SKRiw%2BHD4j38vtftsvVPG5yJdYsRPCVM34osP0ftsWZjJ%2Fp5CNlfpbJww%2BvnkvAY6pgGzWJpR9ezCYHWcbhLy0XiboT4VJLmYpiRX9W0GRNXuM%2BvGJ%2FIyQBLVwsfVhl9eU1f0zS0ORBumCQvWYWGhVrscWiLtIfnSadtCxr9iGRQ7zqt697%2BDvoG9zliBx8%2B8uRl96PUuPCaAwdFQlT%2Bh%2Bh8Y%2BZQE1I7VflgHQnUVKS32f9%2BJxpxJZZUdbUNNNQsaepJhjwUv7mXJWhaDwiVdrQVJ7WADD7KW&X-Amz-Signature=c7e784f630f66ce6f45791ffa5f723ef0b5718e6d6f2765e022d70daed19002a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBEHJOGV%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIGIMdKZBqpaAR6m1x3qILVX8wdOo7BemOmzMIXCP%2Fux9AiBBE%2BbIFy5RC24JsajCTqAhIHX40m7K28hj4Z1445Bwdir%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMK5uSU0lLd0DpuIIDKtwDkWBzL0x3rgdS1Yi%2FF%2B7zVcXrA7%2BSigLhVv4RmQj%2BO41pnkbeJtWZcNhDxHADOnhch8Jm46jAXoMO8AnAehMKqOmxnCvJOHjmi6kT5h5k%2F%2FFeUnC0rloHk56Hs%2F4VZFAm0oKtsHZcOY0zZY7U%2B2lAumkC29RvwgrnDQSKnc6NAxiH0mfCgyE%2FF44jdL4S8spenIeNOHUb3HT%2BkkX9hYuIYrUlP3zjsAJgDGV7%2FEdWr8rUJa%2FIKCV9HyTRpHoGPMfI9lwOx3QN9hJfMUUhyPkcikUsPyN9z6dBAZkpJu%2FTKJCgtWt4Goi7zbmXIaY0PquHBfl8XxaUJAUE5pZpaTWwbozq8a9O9niDUdqPWA56f3gz%2BhWZIycrAa6%2FtENIuDTncgSUHxiPDBr3FpAmofcRGoF0n9nJqkdp7Tu9vEaSvt3O2%2Bla7r9Hz9w7dUaRxZsx7uSiYEUHoUabr8j1gjdceK5dEHSK2NckHTl9CoQV%2F47kO0vE2kbaE0KAzFHqzPBDv2b9oLJCFkZLfimN%2FpZSIyorXBlot0e%2B9xSNIshHepMer1VCL9xzbyi0qKPMJSHRWT7SKRiw%2BHD4j38vtftsvVPG5yJdYsRPCVM34osP0ftsWZjJ%2Fp5CNlfpbJww%2BvnkvAY6pgGzWJpR9ezCYHWcbhLy0XiboT4VJLmYpiRX9W0GRNXuM%2BvGJ%2FIyQBLVwsfVhl9eU1f0zS0ORBumCQvWYWGhVrscWiLtIfnSadtCxr9iGRQ7zqt697%2BDvoG9zliBx8%2B8uRl96PUuPCaAwdFQlT%2Bh%2Bh8Y%2BZQE1I7VflgHQnUVKS32f9%2BJxpxJZZUdbUNNNQsaepJhjwUv7mXJWhaDwiVdrQVJ7WADD7KW&X-Amz-Signature=58d050061fb51a775988db50a8268b1886cc909b8f1b57d8eebf88dbe99b19da&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBEHJOGV%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIGIMdKZBqpaAR6m1x3qILVX8wdOo7BemOmzMIXCP%2Fux9AiBBE%2BbIFy5RC24JsajCTqAhIHX40m7K28hj4Z1445Bwdir%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMK5uSU0lLd0DpuIIDKtwDkWBzL0x3rgdS1Yi%2FF%2B7zVcXrA7%2BSigLhVv4RmQj%2BO41pnkbeJtWZcNhDxHADOnhch8Jm46jAXoMO8AnAehMKqOmxnCvJOHjmi6kT5h5k%2F%2FFeUnC0rloHk56Hs%2F4VZFAm0oKtsHZcOY0zZY7U%2B2lAumkC29RvwgrnDQSKnc6NAxiH0mfCgyE%2FF44jdL4S8spenIeNOHUb3HT%2BkkX9hYuIYrUlP3zjsAJgDGV7%2FEdWr8rUJa%2FIKCV9HyTRpHoGPMfI9lwOx3QN9hJfMUUhyPkcikUsPyN9z6dBAZkpJu%2FTKJCgtWt4Goi7zbmXIaY0PquHBfl8XxaUJAUE5pZpaTWwbozq8a9O9niDUdqPWA56f3gz%2BhWZIycrAa6%2FtENIuDTncgSUHxiPDBr3FpAmofcRGoF0n9nJqkdp7Tu9vEaSvt3O2%2Bla7r9Hz9w7dUaRxZsx7uSiYEUHoUabr8j1gjdceK5dEHSK2NckHTl9CoQV%2F47kO0vE2kbaE0KAzFHqzPBDv2b9oLJCFkZLfimN%2FpZSIyorXBlot0e%2B9xSNIshHepMer1VCL9xzbyi0qKPMJSHRWT7SKRiw%2BHD4j38vtftsvVPG5yJdYsRPCVM34osP0ftsWZjJ%2Fp5CNlfpbJww%2BvnkvAY6pgGzWJpR9ezCYHWcbhLy0XiboT4VJLmYpiRX9W0GRNXuM%2BvGJ%2FIyQBLVwsfVhl9eU1f0zS0ORBumCQvWYWGhVrscWiLtIfnSadtCxr9iGRQ7zqt697%2BDvoG9zliBx8%2B8uRl96PUuPCaAwdFQlT%2Bh%2Bh8Y%2BZQE1I7VflgHQnUVKS32f9%2BJxpxJZZUdbUNNNQsaepJhjwUv7mXJWhaDwiVdrQVJ7WADD7KW&X-Amz-Signature=242a46ea1f0d91c2761a717de60f43b04349076092794b29e416909d3ab8e5ad&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBEHJOGV%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIGIMdKZBqpaAR6m1x3qILVX8wdOo7BemOmzMIXCP%2Fux9AiBBE%2BbIFy5RC24JsajCTqAhIHX40m7K28hj4Z1445Bwdir%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMK5uSU0lLd0DpuIIDKtwDkWBzL0x3rgdS1Yi%2FF%2B7zVcXrA7%2BSigLhVv4RmQj%2BO41pnkbeJtWZcNhDxHADOnhch8Jm46jAXoMO8AnAehMKqOmxnCvJOHjmi6kT5h5k%2F%2FFeUnC0rloHk56Hs%2F4VZFAm0oKtsHZcOY0zZY7U%2B2lAumkC29RvwgrnDQSKnc6NAxiH0mfCgyE%2FF44jdL4S8spenIeNOHUb3HT%2BkkX9hYuIYrUlP3zjsAJgDGV7%2FEdWr8rUJa%2FIKCV9HyTRpHoGPMfI9lwOx3QN9hJfMUUhyPkcikUsPyN9z6dBAZkpJu%2FTKJCgtWt4Goi7zbmXIaY0PquHBfl8XxaUJAUE5pZpaTWwbozq8a9O9niDUdqPWA56f3gz%2BhWZIycrAa6%2FtENIuDTncgSUHxiPDBr3FpAmofcRGoF0n9nJqkdp7Tu9vEaSvt3O2%2Bla7r9Hz9w7dUaRxZsx7uSiYEUHoUabr8j1gjdceK5dEHSK2NckHTl9CoQV%2F47kO0vE2kbaE0KAzFHqzPBDv2b9oLJCFkZLfimN%2FpZSIyorXBlot0e%2B9xSNIshHepMer1VCL9xzbyi0qKPMJSHRWT7SKRiw%2BHD4j38vtftsvVPG5yJdYsRPCVM34osP0ftsWZjJ%2Fp5CNlfpbJww%2BvnkvAY6pgGzWJpR9ezCYHWcbhLy0XiboT4VJLmYpiRX9W0GRNXuM%2BvGJ%2FIyQBLVwsfVhl9eU1f0zS0ORBumCQvWYWGhVrscWiLtIfnSadtCxr9iGRQ7zqt697%2BDvoG9zliBx8%2B8uRl96PUuPCaAwdFQlT%2Bh%2Bh8Y%2BZQE1I7VflgHQnUVKS32f9%2BJxpxJZZUdbUNNNQsaepJhjwUv7mXJWhaDwiVdrQVJ7WADD7KW&X-Amz-Signature=73a5bb01d46b15f7acf8473081e11344eb34f54079f92251a3daaa8fe579981a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBEHJOGV%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIGIMdKZBqpaAR6m1x3qILVX8wdOo7BemOmzMIXCP%2Fux9AiBBE%2BbIFy5RC24JsajCTqAhIHX40m7K28hj4Z1445Bwdir%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMK5uSU0lLd0DpuIIDKtwDkWBzL0x3rgdS1Yi%2FF%2B7zVcXrA7%2BSigLhVv4RmQj%2BO41pnkbeJtWZcNhDxHADOnhch8Jm46jAXoMO8AnAehMKqOmxnCvJOHjmi6kT5h5k%2F%2FFeUnC0rloHk56Hs%2F4VZFAm0oKtsHZcOY0zZY7U%2B2lAumkC29RvwgrnDQSKnc6NAxiH0mfCgyE%2FF44jdL4S8spenIeNOHUb3HT%2BkkX9hYuIYrUlP3zjsAJgDGV7%2FEdWr8rUJa%2FIKCV9HyTRpHoGPMfI9lwOx3QN9hJfMUUhyPkcikUsPyN9z6dBAZkpJu%2FTKJCgtWt4Goi7zbmXIaY0PquHBfl8XxaUJAUE5pZpaTWwbozq8a9O9niDUdqPWA56f3gz%2BhWZIycrAa6%2FtENIuDTncgSUHxiPDBr3FpAmofcRGoF0n9nJqkdp7Tu9vEaSvt3O2%2Bla7r9Hz9w7dUaRxZsx7uSiYEUHoUabr8j1gjdceK5dEHSK2NckHTl9CoQV%2F47kO0vE2kbaE0KAzFHqzPBDv2b9oLJCFkZLfimN%2FpZSIyorXBlot0e%2B9xSNIshHepMer1VCL9xzbyi0qKPMJSHRWT7SKRiw%2BHD4j38vtftsvVPG5yJdYsRPCVM34osP0ftsWZjJ%2Fp5CNlfpbJww%2BvnkvAY6pgGzWJpR9ezCYHWcbhLy0XiboT4VJLmYpiRX9W0GRNXuM%2BvGJ%2FIyQBLVwsfVhl9eU1f0zS0ORBumCQvWYWGhVrscWiLtIfnSadtCxr9iGRQ7zqt697%2BDvoG9zliBx8%2B8uRl96PUuPCaAwdFQlT%2Bh%2Bh8Y%2BZQE1I7VflgHQnUVKS32f9%2BJxpxJZZUdbUNNNQsaepJhjwUv7mXJWhaDwiVdrQVJ7WADD7KW&X-Amz-Signature=7a7658a4ff8eb97d203adec0f0695b17b166671ef07bf72f00044355e2127b90&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBEHJOGV%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIGIMdKZBqpaAR6m1x3qILVX8wdOo7BemOmzMIXCP%2Fux9AiBBE%2BbIFy5RC24JsajCTqAhIHX40m7K28hj4Z1445Bwdir%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMK5uSU0lLd0DpuIIDKtwDkWBzL0x3rgdS1Yi%2FF%2B7zVcXrA7%2BSigLhVv4RmQj%2BO41pnkbeJtWZcNhDxHADOnhch8Jm46jAXoMO8AnAehMKqOmxnCvJOHjmi6kT5h5k%2F%2FFeUnC0rloHk56Hs%2F4VZFAm0oKtsHZcOY0zZY7U%2B2lAumkC29RvwgrnDQSKnc6NAxiH0mfCgyE%2FF44jdL4S8spenIeNOHUb3HT%2BkkX9hYuIYrUlP3zjsAJgDGV7%2FEdWr8rUJa%2FIKCV9HyTRpHoGPMfI9lwOx3QN9hJfMUUhyPkcikUsPyN9z6dBAZkpJu%2FTKJCgtWt4Goi7zbmXIaY0PquHBfl8XxaUJAUE5pZpaTWwbozq8a9O9niDUdqPWA56f3gz%2BhWZIycrAa6%2FtENIuDTncgSUHxiPDBr3FpAmofcRGoF0n9nJqkdp7Tu9vEaSvt3O2%2Bla7r9Hz9w7dUaRxZsx7uSiYEUHoUabr8j1gjdceK5dEHSK2NckHTl9CoQV%2F47kO0vE2kbaE0KAzFHqzPBDv2b9oLJCFkZLfimN%2FpZSIyorXBlot0e%2B9xSNIshHepMer1VCL9xzbyi0qKPMJSHRWT7SKRiw%2BHD4j38vtftsvVPG5yJdYsRPCVM34osP0ftsWZjJ%2Fp5CNlfpbJww%2BvnkvAY6pgGzWJpR9ezCYHWcbhLy0XiboT4VJLmYpiRX9W0GRNXuM%2BvGJ%2FIyQBLVwsfVhl9eU1f0zS0ORBumCQvWYWGhVrscWiLtIfnSadtCxr9iGRQ7zqt697%2BDvoG9zliBx8%2B8uRl96PUuPCaAwdFQlT%2Bh%2Bh8Y%2BZQE1I7VflgHQnUVKS32f9%2BJxpxJZZUdbUNNNQsaepJhjwUv7mXJWhaDwiVdrQVJ7WADD7KW&X-Amz-Signature=94798e282ecd679d83073b54f10ea20e3fa75488379373df458dfbd95ce07672&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBEHJOGV%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIGIMdKZBqpaAR6m1x3qILVX8wdOo7BemOmzMIXCP%2Fux9AiBBE%2BbIFy5RC24JsajCTqAhIHX40m7K28hj4Z1445Bwdir%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMK5uSU0lLd0DpuIIDKtwDkWBzL0x3rgdS1Yi%2FF%2B7zVcXrA7%2BSigLhVv4RmQj%2BO41pnkbeJtWZcNhDxHADOnhch8Jm46jAXoMO8AnAehMKqOmxnCvJOHjmi6kT5h5k%2F%2FFeUnC0rloHk56Hs%2F4VZFAm0oKtsHZcOY0zZY7U%2B2lAumkC29RvwgrnDQSKnc6NAxiH0mfCgyE%2FF44jdL4S8spenIeNOHUb3HT%2BkkX9hYuIYrUlP3zjsAJgDGV7%2FEdWr8rUJa%2FIKCV9HyTRpHoGPMfI9lwOx3QN9hJfMUUhyPkcikUsPyN9z6dBAZkpJu%2FTKJCgtWt4Goi7zbmXIaY0PquHBfl8XxaUJAUE5pZpaTWwbozq8a9O9niDUdqPWA56f3gz%2BhWZIycrAa6%2FtENIuDTncgSUHxiPDBr3FpAmofcRGoF0n9nJqkdp7Tu9vEaSvt3O2%2Bla7r9Hz9w7dUaRxZsx7uSiYEUHoUabr8j1gjdceK5dEHSK2NckHTl9CoQV%2F47kO0vE2kbaE0KAzFHqzPBDv2b9oLJCFkZLfimN%2FpZSIyorXBlot0e%2B9xSNIshHepMer1VCL9xzbyi0qKPMJSHRWT7SKRiw%2BHD4j38vtftsvVPG5yJdYsRPCVM34osP0ftsWZjJ%2Fp5CNlfpbJww%2BvnkvAY6pgGzWJpR9ezCYHWcbhLy0XiboT4VJLmYpiRX9W0GRNXuM%2BvGJ%2FIyQBLVwsfVhl9eU1f0zS0ORBumCQvWYWGhVrscWiLtIfnSadtCxr9iGRQ7zqt697%2BDvoG9zliBx8%2B8uRl96PUuPCaAwdFQlT%2Bh%2Bh8Y%2BZQE1I7VflgHQnUVKS32f9%2BJxpxJZZUdbUNNNQsaepJhjwUv7mXJWhaDwiVdrQVJ7WADD7KW&X-Amz-Signature=04ae43916d1e759da61c3617116a00db9fdfb9ba425513fe2ccb3fece417638d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBEHJOGV%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIGIMdKZBqpaAR6m1x3qILVX8wdOo7BemOmzMIXCP%2Fux9AiBBE%2BbIFy5RC24JsajCTqAhIHX40m7K28hj4Z1445Bwdir%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMK5uSU0lLd0DpuIIDKtwDkWBzL0x3rgdS1Yi%2FF%2B7zVcXrA7%2BSigLhVv4RmQj%2BO41pnkbeJtWZcNhDxHADOnhch8Jm46jAXoMO8AnAehMKqOmxnCvJOHjmi6kT5h5k%2F%2FFeUnC0rloHk56Hs%2F4VZFAm0oKtsHZcOY0zZY7U%2B2lAumkC29RvwgrnDQSKnc6NAxiH0mfCgyE%2FF44jdL4S8spenIeNOHUb3HT%2BkkX9hYuIYrUlP3zjsAJgDGV7%2FEdWr8rUJa%2FIKCV9HyTRpHoGPMfI9lwOx3QN9hJfMUUhyPkcikUsPyN9z6dBAZkpJu%2FTKJCgtWt4Goi7zbmXIaY0PquHBfl8XxaUJAUE5pZpaTWwbozq8a9O9niDUdqPWA56f3gz%2BhWZIycrAa6%2FtENIuDTncgSUHxiPDBr3FpAmofcRGoF0n9nJqkdp7Tu9vEaSvt3O2%2Bla7r9Hz9w7dUaRxZsx7uSiYEUHoUabr8j1gjdceK5dEHSK2NckHTl9CoQV%2F47kO0vE2kbaE0KAzFHqzPBDv2b9oLJCFkZLfimN%2FpZSIyorXBlot0e%2B9xSNIshHepMer1VCL9xzbyi0qKPMJSHRWT7SKRiw%2BHD4j38vtftsvVPG5yJdYsRPCVM34osP0ftsWZjJ%2Fp5CNlfpbJww%2BvnkvAY6pgGzWJpR9ezCYHWcbhLy0XiboT4VJLmYpiRX9W0GRNXuM%2BvGJ%2FIyQBLVwsfVhl9eU1f0zS0ORBumCQvWYWGhVrscWiLtIfnSadtCxr9iGRQ7zqt697%2BDvoG9zliBx8%2B8uRl96PUuPCaAwdFQlT%2Bh%2Bh8Y%2BZQE1I7VflgHQnUVKS32f9%2BJxpxJZZUdbUNNNQsaepJhjwUv7mXJWhaDwiVdrQVJ7WADD7KW&X-Amz-Signature=20a5cef9bccd14393fa03825991fc90143431349afb73dcb56e28f99d41940d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBEHJOGV%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIGIMdKZBqpaAR6m1x3qILVX8wdOo7BemOmzMIXCP%2Fux9AiBBE%2BbIFy5RC24JsajCTqAhIHX40m7K28hj4Z1445Bwdir%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMK5uSU0lLd0DpuIIDKtwDkWBzL0x3rgdS1Yi%2FF%2B7zVcXrA7%2BSigLhVv4RmQj%2BO41pnkbeJtWZcNhDxHADOnhch8Jm46jAXoMO8AnAehMKqOmxnCvJOHjmi6kT5h5k%2F%2FFeUnC0rloHk56Hs%2F4VZFAm0oKtsHZcOY0zZY7U%2B2lAumkC29RvwgrnDQSKnc6NAxiH0mfCgyE%2FF44jdL4S8spenIeNOHUb3HT%2BkkX9hYuIYrUlP3zjsAJgDGV7%2FEdWr8rUJa%2FIKCV9HyTRpHoGPMfI9lwOx3QN9hJfMUUhyPkcikUsPyN9z6dBAZkpJu%2FTKJCgtWt4Goi7zbmXIaY0PquHBfl8XxaUJAUE5pZpaTWwbozq8a9O9niDUdqPWA56f3gz%2BhWZIycrAa6%2FtENIuDTncgSUHxiPDBr3FpAmofcRGoF0n9nJqkdp7Tu9vEaSvt3O2%2Bla7r9Hz9w7dUaRxZsx7uSiYEUHoUabr8j1gjdceK5dEHSK2NckHTl9CoQV%2F47kO0vE2kbaE0KAzFHqzPBDv2b9oLJCFkZLfimN%2FpZSIyorXBlot0e%2B9xSNIshHepMer1VCL9xzbyi0qKPMJSHRWT7SKRiw%2BHD4j38vtftsvVPG5yJdYsRPCVM34osP0ftsWZjJ%2Fp5CNlfpbJww%2BvnkvAY6pgGzWJpR9ezCYHWcbhLy0XiboT4VJLmYpiRX9W0GRNXuM%2BvGJ%2FIyQBLVwsfVhl9eU1f0zS0ORBumCQvWYWGhVrscWiLtIfnSadtCxr9iGRQ7zqt697%2BDvoG9zliBx8%2B8uRl96PUuPCaAwdFQlT%2Bh%2Bh8Y%2BZQE1I7VflgHQnUVKS32f9%2BJxpxJZZUdbUNNNQsaepJhjwUv7mXJWhaDwiVdrQVJ7WADD7KW&X-Amz-Signature=e8f250a5f4b8e2256db9dc81e38237cbcb1360d021b5b056f415b33b9b7611d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGMRWX4Y%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQDCvzWMyRsNp%2BJFf6RxPiDMHsN%2FGzme%2B6WbsJMiUOHP%2BQIgJauU5KAxEH9Fs4vD9SXfgN933dX49vDLcf6C0s2x%2BiIq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEewEg8TimlGFF1JTircAzKwthrCoWCQu9A3d5ZvPeFAi%2BPGYfvmmp4cQFJQHAb8imDB1BcSwdFF3g9RIO5Qitst%2F7Z%2Fe%2BII0cwxlHAq8KTex5MDlF5FedD99l%2BbOYsXl3uy2sUNFar6OrzEMaLTglSPRHznbVwhwkDfHtKuUVqudKSSvoM9DMFqR05whdzl1weSXznw5aZ4SpAkRfg9i6K0WEa1LgUfdXZSCgUhhFeZqdgDJfhTHCwOHAOkvpMeW4zfTbadDekX%2Bua0jy0DX6gtslLlWxUJAayCfJKGcnsL4U03EecdDg8MKdbPyfu5sUQjLp%2FutuQETvILxqbhdKoyJwJyFyPzeZy%2BwCznDsuiaLth7n8%2ByP5PGhxMHBP33HR%2Bkj3lRnYFQNK32mdCO15cpR9vQdWbbZVF7qTgCqdPXRZS9joECxCd7fCs0flr0YcG63f%2BUxl22VizYKna0GKiXuJriZVFNmClBWJgf%2Bu8buMv%2BV3EnFU5aiwDOvEXPe0wbvtcBtGchkNivQAxR7Yn9vbkyNwU2fwYFJI9YfplF4VZfpAZubAnLwJCIzAxoSCbakKV0AyoXXJXrxidW5Khu4Ny%2BBH9F0Wg1PeTrQCjUr%2BxnFD6t%2Bnl7hbFccUrBWvbFXxIXd6cHH7NMND55LwGOqUBJT0MmWMeS23kXWoVrEABKNhHJ2387ew2OjOUZoiy73V5%2FQPIO3RXOYSiG5gDIprZLxH3ITIUqc1VDYd%2F3UgXSxDC6wzgmqD0up34hn74UZS6vWDbq0iQhyZukBpDhtUIjpHSG5r0Zjbz1Z6OKJTuKQJgBwPXjvZNOJM%2BiDwEadsyJqB%2FmPljTIWEj8dW%2FQ3zJHcNlcSd0ZD27Wj3yIVlH6v44Soy&X-Amz-Signature=a367a810d4437ed1fcae649522b472085b7991f5f2e31b7c69aa906e91febd3a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGMRWX4Y%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQDCvzWMyRsNp%2BJFf6RxPiDMHsN%2FGzme%2B6WbsJMiUOHP%2BQIgJauU5KAxEH9Fs4vD9SXfgN933dX49vDLcf6C0s2x%2BiIq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEewEg8TimlGFF1JTircAzKwthrCoWCQu9A3d5ZvPeFAi%2BPGYfvmmp4cQFJQHAb8imDB1BcSwdFF3g9RIO5Qitst%2F7Z%2Fe%2BII0cwxlHAq8KTex5MDlF5FedD99l%2BbOYsXl3uy2sUNFar6OrzEMaLTglSPRHznbVwhwkDfHtKuUVqudKSSvoM9DMFqR05whdzl1weSXznw5aZ4SpAkRfg9i6K0WEa1LgUfdXZSCgUhhFeZqdgDJfhTHCwOHAOkvpMeW4zfTbadDekX%2Bua0jy0DX6gtslLlWxUJAayCfJKGcnsL4U03EecdDg8MKdbPyfu5sUQjLp%2FutuQETvILxqbhdKoyJwJyFyPzeZy%2BwCznDsuiaLth7n8%2ByP5PGhxMHBP33HR%2Bkj3lRnYFQNK32mdCO15cpR9vQdWbbZVF7qTgCqdPXRZS9joECxCd7fCs0flr0YcG63f%2BUxl22VizYKna0GKiXuJriZVFNmClBWJgf%2Bu8buMv%2BV3EnFU5aiwDOvEXPe0wbvtcBtGchkNivQAxR7Yn9vbkyNwU2fwYFJI9YfplF4VZfpAZubAnLwJCIzAxoSCbakKV0AyoXXJXrxidW5Khu4Ny%2BBH9F0Wg1PeTrQCjUr%2BxnFD6t%2Bnl7hbFccUrBWvbFXxIXd6cHH7NMND55LwGOqUBJT0MmWMeS23kXWoVrEABKNhHJ2387ew2OjOUZoiy73V5%2FQPIO3RXOYSiG5gDIprZLxH3ITIUqc1VDYd%2F3UgXSxDC6wzgmqD0up34hn74UZS6vWDbq0iQhyZukBpDhtUIjpHSG5r0Zjbz1Z6OKJTuKQJgBwPXjvZNOJM%2BiDwEadsyJqB%2FmPljTIWEj8dW%2FQ3zJHcNlcSd0ZD27Wj3yIVlH6v44Soy&X-Amz-Signature=a10ad0ed2ffa9e31370028b084e1ca4ea7c756bcbff2e870f60a8064193afa37&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
