

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TA2OGKP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIF4L9w3ZM%2Bj7gYmBVrVw77motKuDYrbxg7SRNoO3B0%2FrAiApq1kb2LNrqNKxZp5VTJRYnpO1rbnAifwVZAOk1eVfKSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIM%2FeMEkjV2692cqkCWKtwDsvGqoOcS%2B4V3HPsT0wzOt%2BKTTzQzpiKM2xblyG2mgz3KYOfmY%2FOcs%2Bb%2B%2BhReFTB%2BvvjvATyixsym3bvips2DIcMmK85DdpMAmyO9hAhJaVxzNZ4DmjTJEXvjF5fX%2BvwHrkLdgmGNOIFyJcjgCbfzYxJc50V6kR1vUlEH%2FBTDImCgphihCLYVTGKwgPaHX5NJ6AvcblRw1rKhA%2FYbHpaPwLNsY5Qvv0NwEaRG6QvCJSMTo1QInCaenvg4lpyzzoFUGwcVDZjVZ2L%2B9pQLP47PTMXizmkd1C14A2IxvbJTY%2BbYUdbGJH6T3LR6rqVXJGpjenxfeeCebSWlvdv65ZBB07mg88P8mZnXzr3vdBntO%2Fteq6bofo%2BaLIQi8MfZW9dj8rQZJhbk5PwOvURCPq%2BPeW5BPob70eTbNEC5yLojU2gjpp2UwMTvZRAZzP47JZRSn8vCRazQfA8TJHnlzDm7UvD9T7nnW1%2F5lVjcEjAomXG3aG1wonSWSj3I2BvK%2Fq3I%2FwcLAkjMXevKYEXBYLZI5AKrRfbatp5x4WoeTTsD4ClBoJEvHALqaTb89mW%2F0vNWJ%2FX3PhXgd2QmJPlAIoO1vUD394OFU7Byzp1MHt05x9Z3rfMnlUDCYZCMsKwwkc2KvQY6pgEs21m8pDXWZGnkvRO1DSMb7RkX2bxm2DemQZ1RCe8W0%2Bwkk%2FfXdCH2Nrtogqb4%2FdHwQQcHrH55rcFBwSUMPHlkvMEzuB1VfQCNPEobwkhJgL%2Bsu6WHptv%2FKjQmtAHidEn%2Fhb5gqfyGaMxYiUoxWqWj%2F0yMbrcVHlh9ROk4UANmNHL5Jx0DR3JgaH7wyXaOkGWWPyRDCXeVrU5zT79bDmiFbCY%2FTujs&X-Amz-Signature=eef11f7e677c3ae283c2398fa53035efd04af42e961c69a93a98f50004fc63e3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TA2OGKP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIF4L9w3ZM%2Bj7gYmBVrVw77motKuDYrbxg7SRNoO3B0%2FrAiApq1kb2LNrqNKxZp5VTJRYnpO1rbnAifwVZAOk1eVfKSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIM%2FeMEkjV2692cqkCWKtwDsvGqoOcS%2B4V3HPsT0wzOt%2BKTTzQzpiKM2xblyG2mgz3KYOfmY%2FOcs%2Bb%2B%2BhReFTB%2BvvjvATyixsym3bvips2DIcMmK85DdpMAmyO9hAhJaVxzNZ4DmjTJEXvjF5fX%2BvwHrkLdgmGNOIFyJcjgCbfzYxJc50V6kR1vUlEH%2FBTDImCgphihCLYVTGKwgPaHX5NJ6AvcblRw1rKhA%2FYbHpaPwLNsY5Qvv0NwEaRG6QvCJSMTo1QInCaenvg4lpyzzoFUGwcVDZjVZ2L%2B9pQLP47PTMXizmkd1C14A2IxvbJTY%2BbYUdbGJH6T3LR6rqVXJGpjenxfeeCebSWlvdv65ZBB07mg88P8mZnXzr3vdBntO%2Fteq6bofo%2BaLIQi8MfZW9dj8rQZJhbk5PwOvURCPq%2BPeW5BPob70eTbNEC5yLojU2gjpp2UwMTvZRAZzP47JZRSn8vCRazQfA8TJHnlzDm7UvD9T7nnW1%2F5lVjcEjAomXG3aG1wonSWSj3I2BvK%2Fq3I%2FwcLAkjMXevKYEXBYLZI5AKrRfbatp5x4WoeTTsD4ClBoJEvHALqaTb89mW%2F0vNWJ%2FX3PhXgd2QmJPlAIoO1vUD394OFU7Byzp1MHt05x9Z3rfMnlUDCYZCMsKwwkc2KvQY6pgEs21m8pDXWZGnkvRO1DSMb7RkX2bxm2DemQZ1RCe8W0%2Bwkk%2FfXdCH2Nrtogqb4%2FdHwQQcHrH55rcFBwSUMPHlkvMEzuB1VfQCNPEobwkhJgL%2Bsu6WHptv%2FKjQmtAHidEn%2Fhb5gqfyGaMxYiUoxWqWj%2F0yMbrcVHlh9ROk4UANmNHL5Jx0DR3JgaH7wyXaOkGWWPyRDCXeVrU5zT79bDmiFbCY%2FTujs&X-Amz-Signature=bf721debf5c391e8eadc0f1fb34675f0e50a8c6a0fa96e9163f50742d32479e6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TA2OGKP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIF4L9w3ZM%2Bj7gYmBVrVw77motKuDYrbxg7SRNoO3B0%2FrAiApq1kb2LNrqNKxZp5VTJRYnpO1rbnAifwVZAOk1eVfKSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIM%2FeMEkjV2692cqkCWKtwDsvGqoOcS%2B4V3HPsT0wzOt%2BKTTzQzpiKM2xblyG2mgz3KYOfmY%2FOcs%2Bb%2B%2BhReFTB%2BvvjvATyixsym3bvips2DIcMmK85DdpMAmyO9hAhJaVxzNZ4DmjTJEXvjF5fX%2BvwHrkLdgmGNOIFyJcjgCbfzYxJc50V6kR1vUlEH%2FBTDImCgphihCLYVTGKwgPaHX5NJ6AvcblRw1rKhA%2FYbHpaPwLNsY5Qvv0NwEaRG6QvCJSMTo1QInCaenvg4lpyzzoFUGwcVDZjVZ2L%2B9pQLP47PTMXizmkd1C14A2IxvbJTY%2BbYUdbGJH6T3LR6rqVXJGpjenxfeeCebSWlvdv65ZBB07mg88P8mZnXzr3vdBntO%2Fteq6bofo%2BaLIQi8MfZW9dj8rQZJhbk5PwOvURCPq%2BPeW5BPob70eTbNEC5yLojU2gjpp2UwMTvZRAZzP47JZRSn8vCRazQfA8TJHnlzDm7UvD9T7nnW1%2F5lVjcEjAomXG3aG1wonSWSj3I2BvK%2Fq3I%2FwcLAkjMXevKYEXBYLZI5AKrRfbatp5x4WoeTTsD4ClBoJEvHALqaTb89mW%2F0vNWJ%2FX3PhXgd2QmJPlAIoO1vUD394OFU7Byzp1MHt05x9Z3rfMnlUDCYZCMsKwwkc2KvQY6pgEs21m8pDXWZGnkvRO1DSMb7RkX2bxm2DemQZ1RCe8W0%2Bwkk%2FfXdCH2Nrtogqb4%2FdHwQQcHrH55rcFBwSUMPHlkvMEzuB1VfQCNPEobwkhJgL%2Bsu6WHptv%2FKjQmtAHidEn%2Fhb5gqfyGaMxYiUoxWqWj%2F0yMbrcVHlh9ROk4UANmNHL5Jx0DR3JgaH7wyXaOkGWWPyRDCXeVrU5zT79bDmiFbCY%2FTujs&X-Amz-Signature=4fd77c1005c40192e12b3b1f5e33eac3c0ba8e49145b729becb234902a80a0b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TA2OGKP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIF4L9w3ZM%2Bj7gYmBVrVw77motKuDYrbxg7SRNoO3B0%2FrAiApq1kb2LNrqNKxZp5VTJRYnpO1rbnAifwVZAOk1eVfKSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIM%2FeMEkjV2692cqkCWKtwDsvGqoOcS%2B4V3HPsT0wzOt%2BKTTzQzpiKM2xblyG2mgz3KYOfmY%2FOcs%2Bb%2B%2BhReFTB%2BvvjvATyixsym3bvips2DIcMmK85DdpMAmyO9hAhJaVxzNZ4DmjTJEXvjF5fX%2BvwHrkLdgmGNOIFyJcjgCbfzYxJc50V6kR1vUlEH%2FBTDImCgphihCLYVTGKwgPaHX5NJ6AvcblRw1rKhA%2FYbHpaPwLNsY5Qvv0NwEaRG6QvCJSMTo1QInCaenvg4lpyzzoFUGwcVDZjVZ2L%2B9pQLP47PTMXizmkd1C14A2IxvbJTY%2BbYUdbGJH6T3LR6rqVXJGpjenxfeeCebSWlvdv65ZBB07mg88P8mZnXzr3vdBntO%2Fteq6bofo%2BaLIQi8MfZW9dj8rQZJhbk5PwOvURCPq%2BPeW5BPob70eTbNEC5yLojU2gjpp2UwMTvZRAZzP47JZRSn8vCRazQfA8TJHnlzDm7UvD9T7nnW1%2F5lVjcEjAomXG3aG1wonSWSj3I2BvK%2Fq3I%2FwcLAkjMXevKYEXBYLZI5AKrRfbatp5x4WoeTTsD4ClBoJEvHALqaTb89mW%2F0vNWJ%2FX3PhXgd2QmJPlAIoO1vUD394OFU7Byzp1MHt05x9Z3rfMnlUDCYZCMsKwwkc2KvQY6pgEs21m8pDXWZGnkvRO1DSMb7RkX2bxm2DemQZ1RCe8W0%2Bwkk%2FfXdCH2Nrtogqb4%2FdHwQQcHrH55rcFBwSUMPHlkvMEzuB1VfQCNPEobwkhJgL%2Bsu6WHptv%2FKjQmtAHidEn%2Fhb5gqfyGaMxYiUoxWqWj%2F0yMbrcVHlh9ROk4UANmNHL5Jx0DR3JgaH7wyXaOkGWWPyRDCXeVrU5zT79bDmiFbCY%2FTujs&X-Amz-Signature=a006b8044d6a219d8f9e09d72a5a5e794b1205857c4c23a4875248fe38687845&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TA2OGKP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIF4L9w3ZM%2Bj7gYmBVrVw77motKuDYrbxg7SRNoO3B0%2FrAiApq1kb2LNrqNKxZp5VTJRYnpO1rbnAifwVZAOk1eVfKSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIM%2FeMEkjV2692cqkCWKtwDsvGqoOcS%2B4V3HPsT0wzOt%2BKTTzQzpiKM2xblyG2mgz3KYOfmY%2FOcs%2Bb%2B%2BhReFTB%2BvvjvATyixsym3bvips2DIcMmK85DdpMAmyO9hAhJaVxzNZ4DmjTJEXvjF5fX%2BvwHrkLdgmGNOIFyJcjgCbfzYxJc50V6kR1vUlEH%2FBTDImCgphihCLYVTGKwgPaHX5NJ6AvcblRw1rKhA%2FYbHpaPwLNsY5Qvv0NwEaRG6QvCJSMTo1QInCaenvg4lpyzzoFUGwcVDZjVZ2L%2B9pQLP47PTMXizmkd1C14A2IxvbJTY%2BbYUdbGJH6T3LR6rqVXJGpjenxfeeCebSWlvdv65ZBB07mg88P8mZnXzr3vdBntO%2Fteq6bofo%2BaLIQi8MfZW9dj8rQZJhbk5PwOvURCPq%2BPeW5BPob70eTbNEC5yLojU2gjpp2UwMTvZRAZzP47JZRSn8vCRazQfA8TJHnlzDm7UvD9T7nnW1%2F5lVjcEjAomXG3aG1wonSWSj3I2BvK%2Fq3I%2FwcLAkjMXevKYEXBYLZI5AKrRfbatp5x4WoeTTsD4ClBoJEvHALqaTb89mW%2F0vNWJ%2FX3PhXgd2QmJPlAIoO1vUD394OFU7Byzp1MHt05x9Z3rfMnlUDCYZCMsKwwkc2KvQY6pgEs21m8pDXWZGnkvRO1DSMb7RkX2bxm2DemQZ1RCe8W0%2Bwkk%2FfXdCH2Nrtogqb4%2FdHwQQcHrH55rcFBwSUMPHlkvMEzuB1VfQCNPEobwkhJgL%2Bsu6WHptv%2FKjQmtAHidEn%2Fhb5gqfyGaMxYiUoxWqWj%2F0yMbrcVHlh9ROk4UANmNHL5Jx0DR3JgaH7wyXaOkGWWPyRDCXeVrU5zT79bDmiFbCY%2FTujs&X-Amz-Signature=53238e85f75de0021afdd77b328d169939a69939abb64b02f3001bed64f3630f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TA2OGKP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIF4L9w3ZM%2Bj7gYmBVrVw77motKuDYrbxg7SRNoO3B0%2FrAiApq1kb2LNrqNKxZp5VTJRYnpO1rbnAifwVZAOk1eVfKSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIM%2FeMEkjV2692cqkCWKtwDsvGqoOcS%2B4V3HPsT0wzOt%2BKTTzQzpiKM2xblyG2mgz3KYOfmY%2FOcs%2Bb%2B%2BhReFTB%2BvvjvATyixsym3bvips2DIcMmK85DdpMAmyO9hAhJaVxzNZ4DmjTJEXvjF5fX%2BvwHrkLdgmGNOIFyJcjgCbfzYxJc50V6kR1vUlEH%2FBTDImCgphihCLYVTGKwgPaHX5NJ6AvcblRw1rKhA%2FYbHpaPwLNsY5Qvv0NwEaRG6QvCJSMTo1QInCaenvg4lpyzzoFUGwcVDZjVZ2L%2B9pQLP47PTMXizmkd1C14A2IxvbJTY%2BbYUdbGJH6T3LR6rqVXJGpjenxfeeCebSWlvdv65ZBB07mg88P8mZnXzr3vdBntO%2Fteq6bofo%2BaLIQi8MfZW9dj8rQZJhbk5PwOvURCPq%2BPeW5BPob70eTbNEC5yLojU2gjpp2UwMTvZRAZzP47JZRSn8vCRazQfA8TJHnlzDm7UvD9T7nnW1%2F5lVjcEjAomXG3aG1wonSWSj3I2BvK%2Fq3I%2FwcLAkjMXevKYEXBYLZI5AKrRfbatp5x4WoeTTsD4ClBoJEvHALqaTb89mW%2F0vNWJ%2FX3PhXgd2QmJPlAIoO1vUD394OFU7Byzp1MHt05x9Z3rfMnlUDCYZCMsKwwkc2KvQY6pgEs21m8pDXWZGnkvRO1DSMb7RkX2bxm2DemQZ1RCe8W0%2Bwkk%2FfXdCH2Nrtogqb4%2FdHwQQcHrH55rcFBwSUMPHlkvMEzuB1VfQCNPEobwkhJgL%2Bsu6WHptv%2FKjQmtAHidEn%2Fhb5gqfyGaMxYiUoxWqWj%2F0yMbrcVHlh9ROk4UANmNHL5Jx0DR3JgaH7wyXaOkGWWPyRDCXeVrU5zT79bDmiFbCY%2FTujs&X-Amz-Signature=fde425de17fc669e103edfefc611b5568632a0aa7a364be5e74f51b5684fc35e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TA2OGKP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIF4L9w3ZM%2Bj7gYmBVrVw77motKuDYrbxg7SRNoO3B0%2FrAiApq1kb2LNrqNKxZp5VTJRYnpO1rbnAifwVZAOk1eVfKSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIM%2FeMEkjV2692cqkCWKtwDsvGqoOcS%2B4V3HPsT0wzOt%2BKTTzQzpiKM2xblyG2mgz3KYOfmY%2FOcs%2Bb%2B%2BhReFTB%2BvvjvATyixsym3bvips2DIcMmK85DdpMAmyO9hAhJaVxzNZ4DmjTJEXvjF5fX%2BvwHrkLdgmGNOIFyJcjgCbfzYxJc50V6kR1vUlEH%2FBTDImCgphihCLYVTGKwgPaHX5NJ6AvcblRw1rKhA%2FYbHpaPwLNsY5Qvv0NwEaRG6QvCJSMTo1QInCaenvg4lpyzzoFUGwcVDZjVZ2L%2B9pQLP47PTMXizmkd1C14A2IxvbJTY%2BbYUdbGJH6T3LR6rqVXJGpjenxfeeCebSWlvdv65ZBB07mg88P8mZnXzr3vdBntO%2Fteq6bofo%2BaLIQi8MfZW9dj8rQZJhbk5PwOvURCPq%2BPeW5BPob70eTbNEC5yLojU2gjpp2UwMTvZRAZzP47JZRSn8vCRazQfA8TJHnlzDm7UvD9T7nnW1%2F5lVjcEjAomXG3aG1wonSWSj3I2BvK%2Fq3I%2FwcLAkjMXevKYEXBYLZI5AKrRfbatp5x4WoeTTsD4ClBoJEvHALqaTb89mW%2F0vNWJ%2FX3PhXgd2QmJPlAIoO1vUD394OFU7Byzp1MHt05x9Z3rfMnlUDCYZCMsKwwkc2KvQY6pgEs21m8pDXWZGnkvRO1DSMb7RkX2bxm2DemQZ1RCe8W0%2Bwkk%2FfXdCH2Nrtogqb4%2FdHwQQcHrH55rcFBwSUMPHlkvMEzuB1VfQCNPEobwkhJgL%2Bsu6WHptv%2FKjQmtAHidEn%2Fhb5gqfyGaMxYiUoxWqWj%2F0yMbrcVHlh9ROk4UANmNHL5Jx0DR3JgaH7wyXaOkGWWPyRDCXeVrU5zT79bDmiFbCY%2FTujs&X-Amz-Signature=18865df210ae523b04a84a909cbf6df68623da6c481ae24cc0990bd658a5cdf0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TA2OGKP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIF4L9w3ZM%2Bj7gYmBVrVw77motKuDYrbxg7SRNoO3B0%2FrAiApq1kb2LNrqNKxZp5VTJRYnpO1rbnAifwVZAOk1eVfKSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIM%2FeMEkjV2692cqkCWKtwDsvGqoOcS%2B4V3HPsT0wzOt%2BKTTzQzpiKM2xblyG2mgz3KYOfmY%2FOcs%2Bb%2B%2BhReFTB%2BvvjvATyixsym3bvips2DIcMmK85DdpMAmyO9hAhJaVxzNZ4DmjTJEXvjF5fX%2BvwHrkLdgmGNOIFyJcjgCbfzYxJc50V6kR1vUlEH%2FBTDImCgphihCLYVTGKwgPaHX5NJ6AvcblRw1rKhA%2FYbHpaPwLNsY5Qvv0NwEaRG6QvCJSMTo1QInCaenvg4lpyzzoFUGwcVDZjVZ2L%2B9pQLP47PTMXizmkd1C14A2IxvbJTY%2BbYUdbGJH6T3LR6rqVXJGpjenxfeeCebSWlvdv65ZBB07mg88P8mZnXzr3vdBntO%2Fteq6bofo%2BaLIQi8MfZW9dj8rQZJhbk5PwOvURCPq%2BPeW5BPob70eTbNEC5yLojU2gjpp2UwMTvZRAZzP47JZRSn8vCRazQfA8TJHnlzDm7UvD9T7nnW1%2F5lVjcEjAomXG3aG1wonSWSj3I2BvK%2Fq3I%2FwcLAkjMXevKYEXBYLZI5AKrRfbatp5x4WoeTTsD4ClBoJEvHALqaTb89mW%2F0vNWJ%2FX3PhXgd2QmJPlAIoO1vUD394OFU7Byzp1MHt05x9Z3rfMnlUDCYZCMsKwwkc2KvQY6pgEs21m8pDXWZGnkvRO1DSMb7RkX2bxm2DemQZ1RCe8W0%2Bwkk%2FfXdCH2Nrtogqb4%2FdHwQQcHrH55rcFBwSUMPHlkvMEzuB1VfQCNPEobwkhJgL%2Bsu6WHptv%2FKjQmtAHidEn%2Fhb5gqfyGaMxYiUoxWqWj%2F0yMbrcVHlh9ROk4UANmNHL5Jx0DR3JgaH7wyXaOkGWWPyRDCXeVrU5zT79bDmiFbCY%2FTujs&X-Amz-Signature=309869f61f254e20f38db23463d193d825034d7c5a6e8e47cb019b06e9c8280c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TA2OGKP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIF4L9w3ZM%2Bj7gYmBVrVw77motKuDYrbxg7SRNoO3B0%2FrAiApq1kb2LNrqNKxZp5VTJRYnpO1rbnAifwVZAOk1eVfKSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIM%2FeMEkjV2692cqkCWKtwDsvGqoOcS%2B4V3HPsT0wzOt%2BKTTzQzpiKM2xblyG2mgz3KYOfmY%2FOcs%2Bb%2B%2BhReFTB%2BvvjvATyixsym3bvips2DIcMmK85DdpMAmyO9hAhJaVxzNZ4DmjTJEXvjF5fX%2BvwHrkLdgmGNOIFyJcjgCbfzYxJc50V6kR1vUlEH%2FBTDImCgphihCLYVTGKwgPaHX5NJ6AvcblRw1rKhA%2FYbHpaPwLNsY5Qvv0NwEaRG6QvCJSMTo1QInCaenvg4lpyzzoFUGwcVDZjVZ2L%2B9pQLP47PTMXizmkd1C14A2IxvbJTY%2BbYUdbGJH6T3LR6rqVXJGpjenxfeeCebSWlvdv65ZBB07mg88P8mZnXzr3vdBntO%2Fteq6bofo%2BaLIQi8MfZW9dj8rQZJhbk5PwOvURCPq%2BPeW5BPob70eTbNEC5yLojU2gjpp2UwMTvZRAZzP47JZRSn8vCRazQfA8TJHnlzDm7UvD9T7nnW1%2F5lVjcEjAomXG3aG1wonSWSj3I2BvK%2Fq3I%2FwcLAkjMXevKYEXBYLZI5AKrRfbatp5x4WoeTTsD4ClBoJEvHALqaTb89mW%2F0vNWJ%2FX3PhXgd2QmJPlAIoO1vUD394OFU7Byzp1MHt05x9Z3rfMnlUDCYZCMsKwwkc2KvQY6pgEs21m8pDXWZGnkvRO1DSMb7RkX2bxm2DemQZ1RCe8W0%2Bwkk%2FfXdCH2Nrtogqb4%2FdHwQQcHrH55rcFBwSUMPHlkvMEzuB1VfQCNPEobwkhJgL%2Bsu6WHptv%2FKjQmtAHidEn%2Fhb5gqfyGaMxYiUoxWqWj%2F0yMbrcVHlh9ROk4UANmNHL5Jx0DR3JgaH7wyXaOkGWWPyRDCXeVrU5zT79bDmiFbCY%2FTujs&X-Amz-Signature=0d71a42b1bd74861ac7c7bf5ed5462a70bead7d1a9445a37cef979b1042e4dbf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Z6K32HQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIGYWgvgT8gbwoe5HOC0cWjzZkKiTj4EANaEqUje0zHBlAiEAiC8S6TjLwmof5QGI3FyJB8CwP4C3QZupeh3G5W9DT1Yq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDDpNabM%2Bf0w1G2Ov0yrcA%2FmTkVTeUE5C20ASflKXSGHrEC5D2QMKXQXMAfDpZw0Ixaj1HW7BLIFKarlQAxhIhzb1ukulRot98oli5drGR7tslfJhyiq%2Bje3X3Tdfm4gP%2FTU9U0nNh0DNMvZvJRx2hAyBMx4%2FlfRjyG5X8zo%2FnmfXzm5N6E6NMEyE5ropKT8Q3wVO0kBCJmCu0sU%2BKSZhvNRhzlfxjkQRAQyI%2Fp%2BnPlZo8LdH74EbiDL3vhqDozrrNYYLZyjDv8dmkd%2BRZYjitBxLzPxI0J%2F%2Fo1G6QYXNrpIuOSs5wu6y7AJrzXG3c8r%2FlPzAIOHNwCjtbZ5npwieBXFIiGGw0DWvZfb6naNko7%2FmtlDw%2FS87IvOGn4bZzXJ5nUyTEYUjmRf8igQeDyCAluRIodvmIoi6DWMLNMSO7VvqrYCf0YmqR%2FmVvW5yK%2FzL4qIQ3%2Fy4yTcuogsZuXA7GHCnatnRkMcflnCegCSarsOsqxcdxef5WLkZG8VTf%2BLSUCbpkYVd8RwpARognXqN%2FgfLK76S2SLFKrR9MP4V6RdLx5kN1EfghuYOodY6j9x%2B%2Blslm1XOBGNjjqyUTqV0XnCKTMLqz2qQPc4VDFKNx8BitbrIm9Un%2FgRgEPTwaGCAj3ZDDw%2Fmwf%2BywrACMJvNir0GOqUB0gWhYB4z05nPaex4mykZ0oypC33KyMRWQYVbMv9%2BPAn36SrVVm1joxtA%2FMEeiUjjV0bQBPb6nWeJfOb9sBfpIkyIgV%2F1TgYn3Unb3Nbb0i1Z09fXHsxqj92cf5UqSyyTiuUAqOLsqL3jL50XiNRQXtT9xJZJV3ikY2AVzZrUTMO07sHtuIJ2o95OmGtKHdhnpUG64WvA2ONMIk5NWOoIW2C9dBQI&X-Amz-Signature=2d9729d7845558998b5f9a8c253259a6c66d7b9aa44b6765a6b75233ddce55b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Z6K32HQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIGYWgvgT8gbwoe5HOC0cWjzZkKiTj4EANaEqUje0zHBlAiEAiC8S6TjLwmof5QGI3FyJB8CwP4C3QZupeh3G5W9DT1Yq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDDpNabM%2Bf0w1G2Ov0yrcA%2FmTkVTeUE5C20ASflKXSGHrEC5D2QMKXQXMAfDpZw0Ixaj1HW7BLIFKarlQAxhIhzb1ukulRot98oli5drGR7tslfJhyiq%2Bje3X3Tdfm4gP%2FTU9U0nNh0DNMvZvJRx2hAyBMx4%2FlfRjyG5X8zo%2FnmfXzm5N6E6NMEyE5ropKT8Q3wVO0kBCJmCu0sU%2BKSZhvNRhzlfxjkQRAQyI%2Fp%2BnPlZo8LdH74EbiDL3vhqDozrrNYYLZyjDv8dmkd%2BRZYjitBxLzPxI0J%2F%2Fo1G6QYXNrpIuOSs5wu6y7AJrzXG3c8r%2FlPzAIOHNwCjtbZ5npwieBXFIiGGw0DWvZfb6naNko7%2FmtlDw%2FS87IvOGn4bZzXJ5nUyTEYUjmRf8igQeDyCAluRIodvmIoi6DWMLNMSO7VvqrYCf0YmqR%2FmVvW5yK%2FzL4qIQ3%2Fy4yTcuogsZuXA7GHCnatnRkMcflnCegCSarsOsqxcdxef5WLkZG8VTf%2BLSUCbpkYVd8RwpARognXqN%2FgfLK76S2SLFKrR9MP4V6RdLx5kN1EfghuYOodY6j9x%2B%2Blslm1XOBGNjjqyUTqV0XnCKTMLqz2qQPc4VDFKNx8BitbrIm9Un%2FgRgEPTwaGCAj3ZDDw%2Fmwf%2BywrACMJvNir0GOqUB0gWhYB4z05nPaex4mykZ0oypC33KyMRWQYVbMv9%2BPAn36SrVVm1joxtA%2FMEeiUjjV0bQBPb6nWeJfOb9sBfpIkyIgV%2F1TgYn3Unb3Nbb0i1Z09fXHsxqj92cf5UqSyyTiuUAqOLsqL3jL50XiNRQXtT9xJZJV3ikY2AVzZrUTMO07sHtuIJ2o95OmGtKHdhnpUG64WvA2ONMIk5NWOoIW2C9dBQI&X-Amz-Signature=bdba92b71daca3dd3d568ad99c074f54cd42b1900e28381532080a1bba0b882f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
