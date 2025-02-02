

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGATX7VR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfULNb%2Fb7UW%2FRfrIIlz97BCWWqdnS2IjUDeRa8fjXqDAiB6Y%2BWMat7%2BkTaZJs2jWv8bj2vAGbXn2wZObdLY2o%2BLlyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUQ2yfDxs%2BkQ2zzzTKtwDxePki479tuLoS7bYQ5S6Wqvzof0HhDAatUf3Vvlce69KXOL4ff58KMHrtYoLQhd1J%2BGwQGOZ3znCeykxygw0KOhyXyxjc%2B8tilXvG8tcYeciKZvLl7QYBt93ynFLJhkp8mFPcpehTLIZ1Zxz4py5iEB7kwWHRnw1hqUZssI8nUYRRrp1ZjBbbQvnZaPVSv%2Bc8iqOlQlBXvYbeyx%2Brt8XOmaOvXwyWbKgJe6R8AeeA9dweu6aZQ7Qw9Y1AzXyAchrHDPIukM%2FaKigpaLi7J8rTERcINYKADbOuRUCVpSIR12gkKt03J39XOFtktN0mJhIRXNwCRde0JwKeQPkVjHAjMlV%2BdQVImZmi2WlZHwmo%2FRrUeoaxl7rb92wekky0YRaDfhi%2BO3pxzgWrApkoWkTkRR9OjUfiG6%2B8Lgl7kyKBwKTwE1XrGCgNOAA024xvp8cWfE3EaF40SSNSGQNyfKJxOklCqkfrlDVSjesmcuT9DTcqISpImlPWjrKzIDERtZTWtrm%2B0gG%2F1KgPya3QexRXDNXeJifzcbTe%2FFlWUlVWctJGftlNXpW32XGmrG3Fow6fUvszMfV5Xg3Mu3lGUXpfNDXke3igz2emaOzS2OlXIXFN%2BwDHVDB6bWnOXwwuOT%2FvAY6pgEmjcm6o9BIL7ZJeOZyaHKLJliMc0GAa5ogRO2lO57eSon3uk%2FTsso4atAeqK8iQPLlvyfpzQpw53UG%2BaUrDKxmjeY2V9zNCs4FJogwmyuKr1xQgpfeRrBEaqOugs1AA1FcurWMiEUKRLMrvzNo9Ff4w7%2BEAwl5rQynRl9AaeJoYbkz288mhmARDwyexVVd2gDjmt7%2B1ubsFKBr6ILYrszoal1iSimC&X-Amz-Signature=6835df9f81749c80d75d47306174ee69e9d4fb7535bbc56b21c3b60d656643b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGATX7VR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfULNb%2Fb7UW%2FRfrIIlz97BCWWqdnS2IjUDeRa8fjXqDAiB6Y%2BWMat7%2BkTaZJs2jWv8bj2vAGbXn2wZObdLY2o%2BLlyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUQ2yfDxs%2BkQ2zzzTKtwDxePki479tuLoS7bYQ5S6Wqvzof0HhDAatUf3Vvlce69KXOL4ff58KMHrtYoLQhd1J%2BGwQGOZ3znCeykxygw0KOhyXyxjc%2B8tilXvG8tcYeciKZvLl7QYBt93ynFLJhkp8mFPcpehTLIZ1Zxz4py5iEB7kwWHRnw1hqUZssI8nUYRRrp1ZjBbbQvnZaPVSv%2Bc8iqOlQlBXvYbeyx%2Brt8XOmaOvXwyWbKgJe6R8AeeA9dweu6aZQ7Qw9Y1AzXyAchrHDPIukM%2FaKigpaLi7J8rTERcINYKADbOuRUCVpSIR12gkKt03J39XOFtktN0mJhIRXNwCRde0JwKeQPkVjHAjMlV%2BdQVImZmi2WlZHwmo%2FRrUeoaxl7rb92wekky0YRaDfhi%2BO3pxzgWrApkoWkTkRR9OjUfiG6%2B8Lgl7kyKBwKTwE1XrGCgNOAA024xvp8cWfE3EaF40SSNSGQNyfKJxOklCqkfrlDVSjesmcuT9DTcqISpImlPWjrKzIDERtZTWtrm%2B0gG%2F1KgPya3QexRXDNXeJifzcbTe%2FFlWUlVWctJGftlNXpW32XGmrG3Fow6fUvszMfV5Xg3Mu3lGUXpfNDXke3igz2emaOzS2OlXIXFN%2BwDHVDB6bWnOXwwuOT%2FvAY6pgEmjcm6o9BIL7ZJeOZyaHKLJliMc0GAa5ogRO2lO57eSon3uk%2FTsso4atAeqK8iQPLlvyfpzQpw53UG%2BaUrDKxmjeY2V9zNCs4FJogwmyuKr1xQgpfeRrBEaqOugs1AA1FcurWMiEUKRLMrvzNo9Ff4w7%2BEAwl5rQynRl9AaeJoYbkz288mhmARDwyexVVd2gDjmt7%2B1ubsFKBr6ILYrszoal1iSimC&X-Amz-Signature=25756a2364b0118466734cf24d10733a7bc7c5813df135af6c8f85dbe42b431e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGATX7VR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfULNb%2Fb7UW%2FRfrIIlz97BCWWqdnS2IjUDeRa8fjXqDAiB6Y%2BWMat7%2BkTaZJs2jWv8bj2vAGbXn2wZObdLY2o%2BLlyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUQ2yfDxs%2BkQ2zzzTKtwDxePki479tuLoS7bYQ5S6Wqvzof0HhDAatUf3Vvlce69KXOL4ff58KMHrtYoLQhd1J%2BGwQGOZ3znCeykxygw0KOhyXyxjc%2B8tilXvG8tcYeciKZvLl7QYBt93ynFLJhkp8mFPcpehTLIZ1Zxz4py5iEB7kwWHRnw1hqUZssI8nUYRRrp1ZjBbbQvnZaPVSv%2Bc8iqOlQlBXvYbeyx%2Brt8XOmaOvXwyWbKgJe6R8AeeA9dweu6aZQ7Qw9Y1AzXyAchrHDPIukM%2FaKigpaLi7J8rTERcINYKADbOuRUCVpSIR12gkKt03J39XOFtktN0mJhIRXNwCRde0JwKeQPkVjHAjMlV%2BdQVImZmi2WlZHwmo%2FRrUeoaxl7rb92wekky0YRaDfhi%2BO3pxzgWrApkoWkTkRR9OjUfiG6%2B8Lgl7kyKBwKTwE1XrGCgNOAA024xvp8cWfE3EaF40SSNSGQNyfKJxOklCqkfrlDVSjesmcuT9DTcqISpImlPWjrKzIDERtZTWtrm%2B0gG%2F1KgPya3QexRXDNXeJifzcbTe%2FFlWUlVWctJGftlNXpW32XGmrG3Fow6fUvszMfV5Xg3Mu3lGUXpfNDXke3igz2emaOzS2OlXIXFN%2BwDHVDB6bWnOXwwuOT%2FvAY6pgEmjcm6o9BIL7ZJeOZyaHKLJliMc0GAa5ogRO2lO57eSon3uk%2FTsso4atAeqK8iQPLlvyfpzQpw53UG%2BaUrDKxmjeY2V9zNCs4FJogwmyuKr1xQgpfeRrBEaqOugs1AA1FcurWMiEUKRLMrvzNo9Ff4w7%2BEAwl5rQynRl9AaeJoYbkz288mhmARDwyexVVd2gDjmt7%2B1ubsFKBr6ILYrszoal1iSimC&X-Amz-Signature=aa492a8f15eca1f3dc78dd3506a01ade3d6bf24667c5ac9929df5c7b5662a48b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGATX7VR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfULNb%2Fb7UW%2FRfrIIlz97BCWWqdnS2IjUDeRa8fjXqDAiB6Y%2BWMat7%2BkTaZJs2jWv8bj2vAGbXn2wZObdLY2o%2BLlyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUQ2yfDxs%2BkQ2zzzTKtwDxePki479tuLoS7bYQ5S6Wqvzof0HhDAatUf3Vvlce69KXOL4ff58KMHrtYoLQhd1J%2BGwQGOZ3znCeykxygw0KOhyXyxjc%2B8tilXvG8tcYeciKZvLl7QYBt93ynFLJhkp8mFPcpehTLIZ1Zxz4py5iEB7kwWHRnw1hqUZssI8nUYRRrp1ZjBbbQvnZaPVSv%2Bc8iqOlQlBXvYbeyx%2Brt8XOmaOvXwyWbKgJe6R8AeeA9dweu6aZQ7Qw9Y1AzXyAchrHDPIukM%2FaKigpaLi7J8rTERcINYKADbOuRUCVpSIR12gkKt03J39XOFtktN0mJhIRXNwCRde0JwKeQPkVjHAjMlV%2BdQVImZmi2WlZHwmo%2FRrUeoaxl7rb92wekky0YRaDfhi%2BO3pxzgWrApkoWkTkRR9OjUfiG6%2B8Lgl7kyKBwKTwE1XrGCgNOAA024xvp8cWfE3EaF40SSNSGQNyfKJxOklCqkfrlDVSjesmcuT9DTcqISpImlPWjrKzIDERtZTWtrm%2B0gG%2F1KgPya3QexRXDNXeJifzcbTe%2FFlWUlVWctJGftlNXpW32XGmrG3Fow6fUvszMfV5Xg3Mu3lGUXpfNDXke3igz2emaOzS2OlXIXFN%2BwDHVDB6bWnOXwwuOT%2FvAY6pgEmjcm6o9BIL7ZJeOZyaHKLJliMc0GAa5ogRO2lO57eSon3uk%2FTsso4atAeqK8iQPLlvyfpzQpw53UG%2BaUrDKxmjeY2V9zNCs4FJogwmyuKr1xQgpfeRrBEaqOugs1AA1FcurWMiEUKRLMrvzNo9Ff4w7%2BEAwl5rQynRl9AaeJoYbkz288mhmARDwyexVVd2gDjmt7%2B1ubsFKBr6ILYrszoal1iSimC&X-Amz-Signature=f83a3818e3dc5f212a84fd303f58849e5105cb846bafe5f2bb28cbd1a3552799&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGATX7VR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfULNb%2Fb7UW%2FRfrIIlz97BCWWqdnS2IjUDeRa8fjXqDAiB6Y%2BWMat7%2BkTaZJs2jWv8bj2vAGbXn2wZObdLY2o%2BLlyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUQ2yfDxs%2BkQ2zzzTKtwDxePki479tuLoS7bYQ5S6Wqvzof0HhDAatUf3Vvlce69KXOL4ff58KMHrtYoLQhd1J%2BGwQGOZ3znCeykxygw0KOhyXyxjc%2B8tilXvG8tcYeciKZvLl7QYBt93ynFLJhkp8mFPcpehTLIZ1Zxz4py5iEB7kwWHRnw1hqUZssI8nUYRRrp1ZjBbbQvnZaPVSv%2Bc8iqOlQlBXvYbeyx%2Brt8XOmaOvXwyWbKgJe6R8AeeA9dweu6aZQ7Qw9Y1AzXyAchrHDPIukM%2FaKigpaLi7J8rTERcINYKADbOuRUCVpSIR12gkKt03J39XOFtktN0mJhIRXNwCRde0JwKeQPkVjHAjMlV%2BdQVImZmi2WlZHwmo%2FRrUeoaxl7rb92wekky0YRaDfhi%2BO3pxzgWrApkoWkTkRR9OjUfiG6%2B8Lgl7kyKBwKTwE1XrGCgNOAA024xvp8cWfE3EaF40SSNSGQNyfKJxOklCqkfrlDVSjesmcuT9DTcqISpImlPWjrKzIDERtZTWtrm%2B0gG%2F1KgPya3QexRXDNXeJifzcbTe%2FFlWUlVWctJGftlNXpW32XGmrG3Fow6fUvszMfV5Xg3Mu3lGUXpfNDXke3igz2emaOzS2OlXIXFN%2BwDHVDB6bWnOXwwuOT%2FvAY6pgEmjcm6o9BIL7ZJeOZyaHKLJliMc0GAa5ogRO2lO57eSon3uk%2FTsso4atAeqK8iQPLlvyfpzQpw53UG%2BaUrDKxmjeY2V9zNCs4FJogwmyuKr1xQgpfeRrBEaqOugs1AA1FcurWMiEUKRLMrvzNo9Ff4w7%2BEAwl5rQynRl9AaeJoYbkz288mhmARDwyexVVd2gDjmt7%2B1ubsFKBr6ILYrszoal1iSimC&X-Amz-Signature=ccbc9ad5ead3f99e40b72088930bb7e361b04d0fa78c8d1fe5472b78fd5b733f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGATX7VR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfULNb%2Fb7UW%2FRfrIIlz97BCWWqdnS2IjUDeRa8fjXqDAiB6Y%2BWMat7%2BkTaZJs2jWv8bj2vAGbXn2wZObdLY2o%2BLlyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUQ2yfDxs%2BkQ2zzzTKtwDxePki479tuLoS7bYQ5S6Wqvzof0HhDAatUf3Vvlce69KXOL4ff58KMHrtYoLQhd1J%2BGwQGOZ3znCeykxygw0KOhyXyxjc%2B8tilXvG8tcYeciKZvLl7QYBt93ynFLJhkp8mFPcpehTLIZ1Zxz4py5iEB7kwWHRnw1hqUZssI8nUYRRrp1ZjBbbQvnZaPVSv%2Bc8iqOlQlBXvYbeyx%2Brt8XOmaOvXwyWbKgJe6R8AeeA9dweu6aZQ7Qw9Y1AzXyAchrHDPIukM%2FaKigpaLi7J8rTERcINYKADbOuRUCVpSIR12gkKt03J39XOFtktN0mJhIRXNwCRde0JwKeQPkVjHAjMlV%2BdQVImZmi2WlZHwmo%2FRrUeoaxl7rb92wekky0YRaDfhi%2BO3pxzgWrApkoWkTkRR9OjUfiG6%2B8Lgl7kyKBwKTwE1XrGCgNOAA024xvp8cWfE3EaF40SSNSGQNyfKJxOklCqkfrlDVSjesmcuT9DTcqISpImlPWjrKzIDERtZTWtrm%2B0gG%2F1KgPya3QexRXDNXeJifzcbTe%2FFlWUlVWctJGftlNXpW32XGmrG3Fow6fUvszMfV5Xg3Mu3lGUXpfNDXke3igz2emaOzS2OlXIXFN%2BwDHVDB6bWnOXwwuOT%2FvAY6pgEmjcm6o9BIL7ZJeOZyaHKLJliMc0GAa5ogRO2lO57eSon3uk%2FTsso4atAeqK8iQPLlvyfpzQpw53UG%2BaUrDKxmjeY2V9zNCs4FJogwmyuKr1xQgpfeRrBEaqOugs1AA1FcurWMiEUKRLMrvzNo9Ff4w7%2BEAwl5rQynRl9AaeJoYbkz288mhmARDwyexVVd2gDjmt7%2B1ubsFKBr6ILYrszoal1iSimC&X-Amz-Signature=d171e12b8eeeb9dafcee52fa54437d320ca578e6e60b54a4e895747cb40005e9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGATX7VR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfULNb%2Fb7UW%2FRfrIIlz97BCWWqdnS2IjUDeRa8fjXqDAiB6Y%2BWMat7%2BkTaZJs2jWv8bj2vAGbXn2wZObdLY2o%2BLlyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUQ2yfDxs%2BkQ2zzzTKtwDxePki479tuLoS7bYQ5S6Wqvzof0HhDAatUf3Vvlce69KXOL4ff58KMHrtYoLQhd1J%2BGwQGOZ3znCeykxygw0KOhyXyxjc%2B8tilXvG8tcYeciKZvLl7QYBt93ynFLJhkp8mFPcpehTLIZ1Zxz4py5iEB7kwWHRnw1hqUZssI8nUYRRrp1ZjBbbQvnZaPVSv%2Bc8iqOlQlBXvYbeyx%2Brt8XOmaOvXwyWbKgJe6R8AeeA9dweu6aZQ7Qw9Y1AzXyAchrHDPIukM%2FaKigpaLi7J8rTERcINYKADbOuRUCVpSIR12gkKt03J39XOFtktN0mJhIRXNwCRde0JwKeQPkVjHAjMlV%2BdQVImZmi2WlZHwmo%2FRrUeoaxl7rb92wekky0YRaDfhi%2BO3pxzgWrApkoWkTkRR9OjUfiG6%2B8Lgl7kyKBwKTwE1XrGCgNOAA024xvp8cWfE3EaF40SSNSGQNyfKJxOklCqkfrlDVSjesmcuT9DTcqISpImlPWjrKzIDERtZTWtrm%2B0gG%2F1KgPya3QexRXDNXeJifzcbTe%2FFlWUlVWctJGftlNXpW32XGmrG3Fow6fUvszMfV5Xg3Mu3lGUXpfNDXke3igz2emaOzS2OlXIXFN%2BwDHVDB6bWnOXwwuOT%2FvAY6pgEmjcm6o9BIL7ZJeOZyaHKLJliMc0GAa5ogRO2lO57eSon3uk%2FTsso4atAeqK8iQPLlvyfpzQpw53UG%2BaUrDKxmjeY2V9zNCs4FJogwmyuKr1xQgpfeRrBEaqOugs1AA1FcurWMiEUKRLMrvzNo9Ff4w7%2BEAwl5rQynRl9AaeJoYbkz288mhmARDwyexVVd2gDjmt7%2B1ubsFKBr6ILYrszoal1iSimC&X-Amz-Signature=b4333b1c2c776e0a63bc3a786cca28ce78567de08f33d3d200a50a63131d2b0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGATX7VR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfULNb%2Fb7UW%2FRfrIIlz97BCWWqdnS2IjUDeRa8fjXqDAiB6Y%2BWMat7%2BkTaZJs2jWv8bj2vAGbXn2wZObdLY2o%2BLlyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUQ2yfDxs%2BkQ2zzzTKtwDxePki479tuLoS7bYQ5S6Wqvzof0HhDAatUf3Vvlce69KXOL4ff58KMHrtYoLQhd1J%2BGwQGOZ3znCeykxygw0KOhyXyxjc%2B8tilXvG8tcYeciKZvLl7QYBt93ynFLJhkp8mFPcpehTLIZ1Zxz4py5iEB7kwWHRnw1hqUZssI8nUYRRrp1ZjBbbQvnZaPVSv%2Bc8iqOlQlBXvYbeyx%2Brt8XOmaOvXwyWbKgJe6R8AeeA9dweu6aZQ7Qw9Y1AzXyAchrHDPIukM%2FaKigpaLi7J8rTERcINYKADbOuRUCVpSIR12gkKt03J39XOFtktN0mJhIRXNwCRde0JwKeQPkVjHAjMlV%2BdQVImZmi2WlZHwmo%2FRrUeoaxl7rb92wekky0YRaDfhi%2BO3pxzgWrApkoWkTkRR9OjUfiG6%2B8Lgl7kyKBwKTwE1XrGCgNOAA024xvp8cWfE3EaF40SSNSGQNyfKJxOklCqkfrlDVSjesmcuT9DTcqISpImlPWjrKzIDERtZTWtrm%2B0gG%2F1KgPya3QexRXDNXeJifzcbTe%2FFlWUlVWctJGftlNXpW32XGmrG3Fow6fUvszMfV5Xg3Mu3lGUXpfNDXke3igz2emaOzS2OlXIXFN%2BwDHVDB6bWnOXwwuOT%2FvAY6pgEmjcm6o9BIL7ZJeOZyaHKLJliMc0GAa5ogRO2lO57eSon3uk%2FTsso4atAeqK8iQPLlvyfpzQpw53UG%2BaUrDKxmjeY2V9zNCs4FJogwmyuKr1xQgpfeRrBEaqOugs1AA1FcurWMiEUKRLMrvzNo9Ff4w7%2BEAwl5rQynRl9AaeJoYbkz288mhmARDwyexVVd2gDjmt7%2B1ubsFKBr6ILYrszoal1iSimC&X-Amz-Signature=570d8b849a2524f39188cdd788bb7c2a05a32258c74d20afd108aef1d09bd0ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGATX7VR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfULNb%2Fb7UW%2FRfrIIlz97BCWWqdnS2IjUDeRa8fjXqDAiB6Y%2BWMat7%2BkTaZJs2jWv8bj2vAGbXn2wZObdLY2o%2BLlyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUQ2yfDxs%2BkQ2zzzTKtwDxePki479tuLoS7bYQ5S6Wqvzof0HhDAatUf3Vvlce69KXOL4ff58KMHrtYoLQhd1J%2BGwQGOZ3znCeykxygw0KOhyXyxjc%2B8tilXvG8tcYeciKZvLl7QYBt93ynFLJhkp8mFPcpehTLIZ1Zxz4py5iEB7kwWHRnw1hqUZssI8nUYRRrp1ZjBbbQvnZaPVSv%2Bc8iqOlQlBXvYbeyx%2Brt8XOmaOvXwyWbKgJe6R8AeeA9dweu6aZQ7Qw9Y1AzXyAchrHDPIukM%2FaKigpaLi7J8rTERcINYKADbOuRUCVpSIR12gkKt03J39XOFtktN0mJhIRXNwCRde0JwKeQPkVjHAjMlV%2BdQVImZmi2WlZHwmo%2FRrUeoaxl7rb92wekky0YRaDfhi%2BO3pxzgWrApkoWkTkRR9OjUfiG6%2B8Lgl7kyKBwKTwE1XrGCgNOAA024xvp8cWfE3EaF40SSNSGQNyfKJxOklCqkfrlDVSjesmcuT9DTcqISpImlPWjrKzIDERtZTWtrm%2B0gG%2F1KgPya3QexRXDNXeJifzcbTe%2FFlWUlVWctJGftlNXpW32XGmrG3Fow6fUvszMfV5Xg3Mu3lGUXpfNDXke3igz2emaOzS2OlXIXFN%2BwDHVDB6bWnOXwwuOT%2FvAY6pgEmjcm6o9BIL7ZJeOZyaHKLJliMc0GAa5ogRO2lO57eSon3uk%2FTsso4atAeqK8iQPLlvyfpzQpw53UG%2BaUrDKxmjeY2V9zNCs4FJogwmyuKr1xQgpfeRrBEaqOugs1AA1FcurWMiEUKRLMrvzNo9Ff4w7%2BEAwl5rQynRl9AaeJoYbkz288mhmARDwyexVVd2gDjmt7%2B1ubsFKBr6ILYrszoal1iSimC&X-Amz-Signature=f03b6d1cb062a082e83f098ce93fe21cb42f46e759f3120597e3c12bbd5b8584&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6SF5JMR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG8TjJAUfH088fg%2BC8kYa2MPYyg5DBZaVbFfgvVpyL7UAiByvMYgp6QOqoudMqypuWk0HU%2FS3t1A2fEz%2Bx%2BLt33Q0SqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJhpd5cH0J6hiZ2muKtwD%2Fr27WX2%2FvdKo4fVoaXHbee9g93D7%2Fdo%2BIWpK0Zy19ZS7kmSI%2FFo7vTOIXhZ3dJmEMrYPeox%2BHnI6LweJ0B9qzAmzs5DyoY%2BpgIfZjzf1ixS5UoZzVcxM9tPrh64G5afxClCS%2BsG7r6Geof5l1l6NHKAvYCaicyoMvaVNdxaPbj9Pk%2BXahi%2B3XFVimG3BujPAtobjDXMPIAzjx6lRPomzqKy%2BzQFNL5DLlJhtg2IC8HUqQxSsR81MBIqEaxXEfcr4eyFx%2B1qYC0z%2BxkN5%2FMdnhJbsioFBgueVh8W0SmPuHA%2BSxIAeCEY0p9rDsUpMJlj2e8hzG0p02fmlVKgtqppIN5R6WTOwSUsS5vi6NbvxS0EpXBqofTqG3tEjrd%2BDK06gZnva%2F0Gq378qpgFQ%2B4r33tE7WZqpm88w2qB%2BwLYeLKSiFGKW0IPuWBbRO5ZNbycg42Ql9t4VqWo3Hg44Cy2NUdYo1VUdchNWmqjF%2FSyQUxGJbmMhfRWAVC9SwfcyotKCPqqqJN3onsUEMaz1lzPVOGxdpSFW8RIr%2BPQKx1Bz%2FQ%2FkW0YgGpspm2EocHLzBmea7srxZA5PK52WeF2XZzoYEqSD%2FzvB5DkSo2F5x756yVWjkiHNl1OCiY0QATYwuuT%2FvAY6pgGjmZmQLjkVirgp2DtWAHv6r1VFS6X9nMd%2F3FpHDYrPuJevqFQKZpGGv5%2Bp61o3N%2F6xa4CDpdbaUaz6zU9%2FUfj7rsVuXRaXEsOaTO%2BJuv5frVb%2BWiZd8o6Kl6RtngL894SNmN2lLrZDeQFPu8ulupzFIsfjRrEMISA%2F243h8IFTG4DP6f2KzrM0zQ9egUUdFhR2lB7rp2vSrLmAY7JJgkzhDvjQErEX&X-Amz-Signature=4d0ba4bbe9ca790293449f49596d5fa96a18a6eca42f111c2cefcdd09d991003&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6SF5JMR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG8TjJAUfH088fg%2BC8kYa2MPYyg5DBZaVbFfgvVpyL7UAiByvMYgp6QOqoudMqypuWk0HU%2FS3t1A2fEz%2Bx%2BLt33Q0SqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJhpd5cH0J6hiZ2muKtwD%2Fr27WX2%2FvdKo4fVoaXHbee9g93D7%2Fdo%2BIWpK0Zy19ZS7kmSI%2FFo7vTOIXhZ3dJmEMrYPeox%2BHnI6LweJ0B9qzAmzs5DyoY%2BpgIfZjzf1ixS5UoZzVcxM9tPrh64G5afxClCS%2BsG7r6Geof5l1l6NHKAvYCaicyoMvaVNdxaPbj9Pk%2BXahi%2B3XFVimG3BujPAtobjDXMPIAzjx6lRPomzqKy%2BzQFNL5DLlJhtg2IC8HUqQxSsR81MBIqEaxXEfcr4eyFx%2B1qYC0z%2BxkN5%2FMdnhJbsioFBgueVh8W0SmPuHA%2BSxIAeCEY0p9rDsUpMJlj2e8hzG0p02fmlVKgtqppIN5R6WTOwSUsS5vi6NbvxS0EpXBqofTqG3tEjrd%2BDK06gZnva%2F0Gq378qpgFQ%2B4r33tE7WZqpm88w2qB%2BwLYeLKSiFGKW0IPuWBbRO5ZNbycg42Ql9t4VqWo3Hg44Cy2NUdYo1VUdchNWmqjF%2FSyQUxGJbmMhfRWAVC9SwfcyotKCPqqqJN3onsUEMaz1lzPVOGxdpSFW8RIr%2BPQKx1Bz%2FQ%2FkW0YgGpspm2EocHLzBmea7srxZA5PK52WeF2XZzoYEqSD%2FzvB5DkSo2F5x756yVWjkiHNl1OCiY0QATYwuuT%2FvAY6pgGjmZmQLjkVirgp2DtWAHv6r1VFS6X9nMd%2F3FpHDYrPuJevqFQKZpGGv5%2Bp61o3N%2F6xa4CDpdbaUaz6zU9%2FUfj7rsVuXRaXEsOaTO%2BJuv5frVb%2BWiZd8o6Kl6RtngL894SNmN2lLrZDeQFPu8ulupzFIsfjRrEMISA%2F243h8IFTG4DP6f2KzrM0zQ9egUUdFhR2lB7rp2vSrLmAY7JJgkzhDvjQErEX&X-Amz-Signature=018e14cc0fd7e8fc5751e6b54fc66f6d1d78d6eeb4f7cbbb585a05a875d147e2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
