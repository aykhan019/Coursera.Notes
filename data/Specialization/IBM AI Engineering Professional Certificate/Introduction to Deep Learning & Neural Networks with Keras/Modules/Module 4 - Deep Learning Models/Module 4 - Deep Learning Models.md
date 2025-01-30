

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4NASAYX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrWv%2F%2BO7%2FMpDvTzYKhmSFee%2BAx726TMhRMN5t%2BUB06OAiBtaeXpaMI%2BiNJGa%2FkU6usQsYi16GCzOPXSaKzBvG4tSSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtd%2BZTOmJzzmaeXRtKtwDIEffFYa2OWZ%2FQlZ3mArctc8wuKAG4T7iwliYq%2Fz2SZ%2BEWJ%2Fwcbctrczshb5fihjRkehx%2FK%2BnvyVidMuDqTMctVwzr4JVTu353ff9Oyp%2B8nBjMqnoaxu9CMyqOuHSFlO2NjLFVBgfF%2BFXRXYUOf0NAsxp7oa5JrnsAwheB9mZYX4AMfPBC14ok36s7ZbIIICWlX7CiuKlI9oQgx9Ch0I7ObJYVUvAjGnWobFG3e%2FsViALpYfJTzR4sO%2B7sGFOD9%2FEWys0%2FIfgLrtn5tMzllyCig6pd7e0EuCFAC1ExptzN8NAx43lJO8VMO%2FHV7QYUb4HuhkNX%2BslkF8m52vEtvG8JyEB8hGu5Yg2%2FjO1OguGq5b4ias5FIk526RC%2FK680Wxlug5H%2B%2FzIAcmnQgenVgZ4eM%2BrrLsEO7MpRRZ0BawUONT1WQs9yB7xYh%2Fk4YZEznqvpJll6t%2FeOFd1tmgBdEN4BmmMXf2FT92vXChR8IgvZtyAkmC%2BuvnCw%2BHt9iF0zHXkbDo%2Bf0apUQM7aleTmilbxRE27%2FxG%2Fb7Um%2By3%2Bc8%2Ff808nf3HX9d9DjFXdGRNSHaEEvnjiKlM7kqyIJ5HuZgcnr6dHRh0rHlGMd1FO02yjedqXe0ElrEvo2ly1Msw55brvAY6pgHpP5P0TcQs7yv9nMNkH2H7fDJcS4seomXa7S7VeJe1T%2BgJuPz5rO6pK1S09sJCg%2FGOEyA4yBYS5O9l%2Bw%2F8u5tXZPEUaQXSOjDZHEPF9NNeyn2MydtcKWhMZbnIldXJ1fXmsd74I8cN%2FFq3arPgWp7uoddpoZZE12M4roz2t80%2BMeswpUPMG3r78opRIGUvSvjUvTMQkg%2BaMQJGLQe67FN67dKR04M4&X-Amz-Signature=aa73483abdb1ec4269402fe16d0f60f72b3216e35b9ba12f729fd011d5007769&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4NASAYX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrWv%2F%2BO7%2FMpDvTzYKhmSFee%2BAx726TMhRMN5t%2BUB06OAiBtaeXpaMI%2BiNJGa%2FkU6usQsYi16GCzOPXSaKzBvG4tSSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtd%2BZTOmJzzmaeXRtKtwDIEffFYa2OWZ%2FQlZ3mArctc8wuKAG4T7iwliYq%2Fz2SZ%2BEWJ%2Fwcbctrczshb5fihjRkehx%2FK%2BnvyVidMuDqTMctVwzr4JVTu353ff9Oyp%2B8nBjMqnoaxu9CMyqOuHSFlO2NjLFVBgfF%2BFXRXYUOf0NAsxp7oa5JrnsAwheB9mZYX4AMfPBC14ok36s7ZbIIICWlX7CiuKlI9oQgx9Ch0I7ObJYVUvAjGnWobFG3e%2FsViALpYfJTzR4sO%2B7sGFOD9%2FEWys0%2FIfgLrtn5tMzllyCig6pd7e0EuCFAC1ExptzN8NAx43lJO8VMO%2FHV7QYUb4HuhkNX%2BslkF8m52vEtvG8JyEB8hGu5Yg2%2FjO1OguGq5b4ias5FIk526RC%2FK680Wxlug5H%2B%2FzIAcmnQgenVgZ4eM%2BrrLsEO7MpRRZ0BawUONT1WQs9yB7xYh%2Fk4YZEznqvpJll6t%2FeOFd1tmgBdEN4BmmMXf2FT92vXChR8IgvZtyAkmC%2BuvnCw%2BHt9iF0zHXkbDo%2Bf0apUQM7aleTmilbxRE27%2FxG%2Fb7Um%2By3%2Bc8%2Ff808nf3HX9d9DjFXdGRNSHaEEvnjiKlM7kqyIJ5HuZgcnr6dHRh0rHlGMd1FO02yjedqXe0ElrEvo2ly1Msw55brvAY6pgHpP5P0TcQs7yv9nMNkH2H7fDJcS4seomXa7S7VeJe1T%2BgJuPz5rO6pK1S09sJCg%2FGOEyA4yBYS5O9l%2Bw%2F8u5tXZPEUaQXSOjDZHEPF9NNeyn2MydtcKWhMZbnIldXJ1fXmsd74I8cN%2FFq3arPgWp7uoddpoZZE12M4roz2t80%2BMeswpUPMG3r78opRIGUvSvjUvTMQkg%2BaMQJGLQe67FN67dKR04M4&X-Amz-Signature=443badce4df3b1d8560cd558252083a793b6fdb1c3c25440d6e0ecc39e37d344&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4NASAYX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrWv%2F%2BO7%2FMpDvTzYKhmSFee%2BAx726TMhRMN5t%2BUB06OAiBtaeXpaMI%2BiNJGa%2FkU6usQsYi16GCzOPXSaKzBvG4tSSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtd%2BZTOmJzzmaeXRtKtwDIEffFYa2OWZ%2FQlZ3mArctc8wuKAG4T7iwliYq%2Fz2SZ%2BEWJ%2Fwcbctrczshb5fihjRkehx%2FK%2BnvyVidMuDqTMctVwzr4JVTu353ff9Oyp%2B8nBjMqnoaxu9CMyqOuHSFlO2NjLFVBgfF%2BFXRXYUOf0NAsxp7oa5JrnsAwheB9mZYX4AMfPBC14ok36s7ZbIIICWlX7CiuKlI9oQgx9Ch0I7ObJYVUvAjGnWobFG3e%2FsViALpYfJTzR4sO%2B7sGFOD9%2FEWys0%2FIfgLrtn5tMzllyCig6pd7e0EuCFAC1ExptzN8NAx43lJO8VMO%2FHV7QYUb4HuhkNX%2BslkF8m52vEtvG8JyEB8hGu5Yg2%2FjO1OguGq5b4ias5FIk526RC%2FK680Wxlug5H%2B%2FzIAcmnQgenVgZ4eM%2BrrLsEO7MpRRZ0BawUONT1WQs9yB7xYh%2Fk4YZEznqvpJll6t%2FeOFd1tmgBdEN4BmmMXf2FT92vXChR8IgvZtyAkmC%2BuvnCw%2BHt9iF0zHXkbDo%2Bf0apUQM7aleTmilbxRE27%2FxG%2Fb7Um%2By3%2Bc8%2Ff808nf3HX9d9DjFXdGRNSHaEEvnjiKlM7kqyIJ5HuZgcnr6dHRh0rHlGMd1FO02yjedqXe0ElrEvo2ly1Msw55brvAY6pgHpP5P0TcQs7yv9nMNkH2H7fDJcS4seomXa7S7VeJe1T%2BgJuPz5rO6pK1S09sJCg%2FGOEyA4yBYS5O9l%2Bw%2F8u5tXZPEUaQXSOjDZHEPF9NNeyn2MydtcKWhMZbnIldXJ1fXmsd74I8cN%2FFq3arPgWp7uoddpoZZE12M4roz2t80%2BMeswpUPMG3r78opRIGUvSvjUvTMQkg%2BaMQJGLQe67FN67dKR04M4&X-Amz-Signature=a64c9e5d33b2bf5d50d04cd04cad338e90856a6512921cafe09171778c835aea&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4NASAYX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrWv%2F%2BO7%2FMpDvTzYKhmSFee%2BAx726TMhRMN5t%2BUB06OAiBtaeXpaMI%2BiNJGa%2FkU6usQsYi16GCzOPXSaKzBvG4tSSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtd%2BZTOmJzzmaeXRtKtwDIEffFYa2OWZ%2FQlZ3mArctc8wuKAG4T7iwliYq%2Fz2SZ%2BEWJ%2Fwcbctrczshb5fihjRkehx%2FK%2BnvyVidMuDqTMctVwzr4JVTu353ff9Oyp%2B8nBjMqnoaxu9CMyqOuHSFlO2NjLFVBgfF%2BFXRXYUOf0NAsxp7oa5JrnsAwheB9mZYX4AMfPBC14ok36s7ZbIIICWlX7CiuKlI9oQgx9Ch0I7ObJYVUvAjGnWobFG3e%2FsViALpYfJTzR4sO%2B7sGFOD9%2FEWys0%2FIfgLrtn5tMzllyCig6pd7e0EuCFAC1ExptzN8NAx43lJO8VMO%2FHV7QYUb4HuhkNX%2BslkF8m52vEtvG8JyEB8hGu5Yg2%2FjO1OguGq5b4ias5FIk526RC%2FK680Wxlug5H%2B%2FzIAcmnQgenVgZ4eM%2BrrLsEO7MpRRZ0BawUONT1WQs9yB7xYh%2Fk4YZEznqvpJll6t%2FeOFd1tmgBdEN4BmmMXf2FT92vXChR8IgvZtyAkmC%2BuvnCw%2BHt9iF0zHXkbDo%2Bf0apUQM7aleTmilbxRE27%2FxG%2Fb7Um%2By3%2Bc8%2Ff808nf3HX9d9DjFXdGRNSHaEEvnjiKlM7kqyIJ5HuZgcnr6dHRh0rHlGMd1FO02yjedqXe0ElrEvo2ly1Msw55brvAY6pgHpP5P0TcQs7yv9nMNkH2H7fDJcS4seomXa7S7VeJe1T%2BgJuPz5rO6pK1S09sJCg%2FGOEyA4yBYS5O9l%2Bw%2F8u5tXZPEUaQXSOjDZHEPF9NNeyn2MydtcKWhMZbnIldXJ1fXmsd74I8cN%2FFq3arPgWp7uoddpoZZE12M4roz2t80%2BMeswpUPMG3r78opRIGUvSvjUvTMQkg%2BaMQJGLQe67FN67dKR04M4&X-Amz-Signature=0c7defad8d16134d081b44d119dda924d889b2d55ab67773b5b5f0262e64e8cf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4NASAYX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrWv%2F%2BO7%2FMpDvTzYKhmSFee%2BAx726TMhRMN5t%2BUB06OAiBtaeXpaMI%2BiNJGa%2FkU6usQsYi16GCzOPXSaKzBvG4tSSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtd%2BZTOmJzzmaeXRtKtwDIEffFYa2OWZ%2FQlZ3mArctc8wuKAG4T7iwliYq%2Fz2SZ%2BEWJ%2Fwcbctrczshb5fihjRkehx%2FK%2BnvyVidMuDqTMctVwzr4JVTu353ff9Oyp%2B8nBjMqnoaxu9CMyqOuHSFlO2NjLFVBgfF%2BFXRXYUOf0NAsxp7oa5JrnsAwheB9mZYX4AMfPBC14ok36s7ZbIIICWlX7CiuKlI9oQgx9Ch0I7ObJYVUvAjGnWobFG3e%2FsViALpYfJTzR4sO%2B7sGFOD9%2FEWys0%2FIfgLrtn5tMzllyCig6pd7e0EuCFAC1ExptzN8NAx43lJO8VMO%2FHV7QYUb4HuhkNX%2BslkF8m52vEtvG8JyEB8hGu5Yg2%2FjO1OguGq5b4ias5FIk526RC%2FK680Wxlug5H%2B%2FzIAcmnQgenVgZ4eM%2BrrLsEO7MpRRZ0BawUONT1WQs9yB7xYh%2Fk4YZEznqvpJll6t%2FeOFd1tmgBdEN4BmmMXf2FT92vXChR8IgvZtyAkmC%2BuvnCw%2BHt9iF0zHXkbDo%2Bf0apUQM7aleTmilbxRE27%2FxG%2Fb7Um%2By3%2Bc8%2Ff808nf3HX9d9DjFXdGRNSHaEEvnjiKlM7kqyIJ5HuZgcnr6dHRh0rHlGMd1FO02yjedqXe0ElrEvo2ly1Msw55brvAY6pgHpP5P0TcQs7yv9nMNkH2H7fDJcS4seomXa7S7VeJe1T%2BgJuPz5rO6pK1S09sJCg%2FGOEyA4yBYS5O9l%2Bw%2F8u5tXZPEUaQXSOjDZHEPF9NNeyn2MydtcKWhMZbnIldXJ1fXmsd74I8cN%2FFq3arPgWp7uoddpoZZE12M4roz2t80%2BMeswpUPMG3r78opRIGUvSvjUvTMQkg%2BaMQJGLQe67FN67dKR04M4&X-Amz-Signature=c2d53154214a6d28190d0af04fab3dfbf4b54854d8c8915a258709fba58019c9&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4NASAYX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrWv%2F%2BO7%2FMpDvTzYKhmSFee%2BAx726TMhRMN5t%2BUB06OAiBtaeXpaMI%2BiNJGa%2FkU6usQsYi16GCzOPXSaKzBvG4tSSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtd%2BZTOmJzzmaeXRtKtwDIEffFYa2OWZ%2FQlZ3mArctc8wuKAG4T7iwliYq%2Fz2SZ%2BEWJ%2Fwcbctrczshb5fihjRkehx%2FK%2BnvyVidMuDqTMctVwzr4JVTu353ff9Oyp%2B8nBjMqnoaxu9CMyqOuHSFlO2NjLFVBgfF%2BFXRXYUOf0NAsxp7oa5JrnsAwheB9mZYX4AMfPBC14ok36s7ZbIIICWlX7CiuKlI9oQgx9Ch0I7ObJYVUvAjGnWobFG3e%2FsViALpYfJTzR4sO%2B7sGFOD9%2FEWys0%2FIfgLrtn5tMzllyCig6pd7e0EuCFAC1ExptzN8NAx43lJO8VMO%2FHV7QYUb4HuhkNX%2BslkF8m52vEtvG8JyEB8hGu5Yg2%2FjO1OguGq5b4ias5FIk526RC%2FK680Wxlug5H%2B%2FzIAcmnQgenVgZ4eM%2BrrLsEO7MpRRZ0BawUONT1WQs9yB7xYh%2Fk4YZEznqvpJll6t%2FeOFd1tmgBdEN4BmmMXf2FT92vXChR8IgvZtyAkmC%2BuvnCw%2BHt9iF0zHXkbDo%2Bf0apUQM7aleTmilbxRE27%2FxG%2Fb7Um%2By3%2Bc8%2Ff808nf3HX9d9DjFXdGRNSHaEEvnjiKlM7kqyIJ5HuZgcnr6dHRh0rHlGMd1FO02yjedqXe0ElrEvo2ly1Msw55brvAY6pgHpP5P0TcQs7yv9nMNkH2H7fDJcS4seomXa7S7VeJe1T%2BgJuPz5rO6pK1S09sJCg%2FGOEyA4yBYS5O9l%2Bw%2F8u5tXZPEUaQXSOjDZHEPF9NNeyn2MydtcKWhMZbnIldXJ1fXmsd74I8cN%2FFq3arPgWp7uoddpoZZE12M4roz2t80%2BMeswpUPMG3r78opRIGUvSvjUvTMQkg%2BaMQJGLQe67FN67dKR04M4&X-Amz-Signature=0f81b6252ccc538cd93e75fdde57713c917bff8228ef509bf8e5225bd0923e50&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4NASAYX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrWv%2F%2BO7%2FMpDvTzYKhmSFee%2BAx726TMhRMN5t%2BUB06OAiBtaeXpaMI%2BiNJGa%2FkU6usQsYi16GCzOPXSaKzBvG4tSSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtd%2BZTOmJzzmaeXRtKtwDIEffFYa2OWZ%2FQlZ3mArctc8wuKAG4T7iwliYq%2Fz2SZ%2BEWJ%2Fwcbctrczshb5fihjRkehx%2FK%2BnvyVidMuDqTMctVwzr4JVTu353ff9Oyp%2B8nBjMqnoaxu9CMyqOuHSFlO2NjLFVBgfF%2BFXRXYUOf0NAsxp7oa5JrnsAwheB9mZYX4AMfPBC14ok36s7ZbIIICWlX7CiuKlI9oQgx9Ch0I7ObJYVUvAjGnWobFG3e%2FsViALpYfJTzR4sO%2B7sGFOD9%2FEWys0%2FIfgLrtn5tMzllyCig6pd7e0EuCFAC1ExptzN8NAx43lJO8VMO%2FHV7QYUb4HuhkNX%2BslkF8m52vEtvG8JyEB8hGu5Yg2%2FjO1OguGq5b4ias5FIk526RC%2FK680Wxlug5H%2B%2FzIAcmnQgenVgZ4eM%2BrrLsEO7MpRRZ0BawUONT1WQs9yB7xYh%2Fk4YZEznqvpJll6t%2FeOFd1tmgBdEN4BmmMXf2FT92vXChR8IgvZtyAkmC%2BuvnCw%2BHt9iF0zHXkbDo%2Bf0apUQM7aleTmilbxRE27%2FxG%2Fb7Um%2By3%2Bc8%2Ff808nf3HX9d9DjFXdGRNSHaEEvnjiKlM7kqyIJ5HuZgcnr6dHRh0rHlGMd1FO02yjedqXe0ElrEvo2ly1Msw55brvAY6pgHpP5P0TcQs7yv9nMNkH2H7fDJcS4seomXa7S7VeJe1T%2BgJuPz5rO6pK1S09sJCg%2FGOEyA4yBYS5O9l%2Bw%2F8u5tXZPEUaQXSOjDZHEPF9NNeyn2MydtcKWhMZbnIldXJ1fXmsd74I8cN%2FFq3arPgWp7uoddpoZZE12M4roz2t80%2BMeswpUPMG3r78opRIGUvSvjUvTMQkg%2BaMQJGLQe67FN67dKR04M4&X-Amz-Signature=1778507bcd8390a734ef78ae421dde2e5489382e40132f1d1c2fb04d073fb5e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4NASAYX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrWv%2F%2BO7%2FMpDvTzYKhmSFee%2BAx726TMhRMN5t%2BUB06OAiBtaeXpaMI%2BiNJGa%2FkU6usQsYi16GCzOPXSaKzBvG4tSSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtd%2BZTOmJzzmaeXRtKtwDIEffFYa2OWZ%2FQlZ3mArctc8wuKAG4T7iwliYq%2Fz2SZ%2BEWJ%2Fwcbctrczshb5fihjRkehx%2FK%2BnvyVidMuDqTMctVwzr4JVTu353ff9Oyp%2B8nBjMqnoaxu9CMyqOuHSFlO2NjLFVBgfF%2BFXRXYUOf0NAsxp7oa5JrnsAwheB9mZYX4AMfPBC14ok36s7ZbIIICWlX7CiuKlI9oQgx9Ch0I7ObJYVUvAjGnWobFG3e%2FsViALpYfJTzR4sO%2B7sGFOD9%2FEWys0%2FIfgLrtn5tMzllyCig6pd7e0EuCFAC1ExptzN8NAx43lJO8VMO%2FHV7QYUb4HuhkNX%2BslkF8m52vEtvG8JyEB8hGu5Yg2%2FjO1OguGq5b4ias5FIk526RC%2FK680Wxlug5H%2B%2FzIAcmnQgenVgZ4eM%2BrrLsEO7MpRRZ0BawUONT1WQs9yB7xYh%2Fk4YZEznqvpJll6t%2FeOFd1tmgBdEN4BmmMXf2FT92vXChR8IgvZtyAkmC%2BuvnCw%2BHt9iF0zHXkbDo%2Bf0apUQM7aleTmilbxRE27%2FxG%2Fb7Um%2By3%2Bc8%2Ff808nf3HX9d9DjFXdGRNSHaEEvnjiKlM7kqyIJ5HuZgcnr6dHRh0rHlGMd1FO02yjedqXe0ElrEvo2ly1Msw55brvAY6pgHpP5P0TcQs7yv9nMNkH2H7fDJcS4seomXa7S7VeJe1T%2BgJuPz5rO6pK1S09sJCg%2FGOEyA4yBYS5O9l%2Bw%2F8u5tXZPEUaQXSOjDZHEPF9NNeyn2MydtcKWhMZbnIldXJ1fXmsd74I8cN%2FFq3arPgWp7uoddpoZZE12M4roz2t80%2BMeswpUPMG3r78opRIGUvSvjUvTMQkg%2BaMQJGLQe67FN67dKR04M4&X-Amz-Signature=be73aec47f1a1ac17b2d60e42c679cef28aaac3899db3a7f264e873011864e35&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4NASAYX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrWv%2F%2BO7%2FMpDvTzYKhmSFee%2BAx726TMhRMN5t%2BUB06OAiBtaeXpaMI%2BiNJGa%2FkU6usQsYi16GCzOPXSaKzBvG4tSSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtd%2BZTOmJzzmaeXRtKtwDIEffFYa2OWZ%2FQlZ3mArctc8wuKAG4T7iwliYq%2Fz2SZ%2BEWJ%2Fwcbctrczshb5fihjRkehx%2FK%2BnvyVidMuDqTMctVwzr4JVTu353ff9Oyp%2B8nBjMqnoaxu9CMyqOuHSFlO2NjLFVBgfF%2BFXRXYUOf0NAsxp7oa5JrnsAwheB9mZYX4AMfPBC14ok36s7ZbIIICWlX7CiuKlI9oQgx9Ch0I7ObJYVUvAjGnWobFG3e%2FsViALpYfJTzR4sO%2B7sGFOD9%2FEWys0%2FIfgLrtn5tMzllyCig6pd7e0EuCFAC1ExptzN8NAx43lJO8VMO%2FHV7QYUb4HuhkNX%2BslkF8m52vEtvG8JyEB8hGu5Yg2%2FjO1OguGq5b4ias5FIk526RC%2FK680Wxlug5H%2B%2FzIAcmnQgenVgZ4eM%2BrrLsEO7MpRRZ0BawUONT1WQs9yB7xYh%2Fk4YZEznqvpJll6t%2FeOFd1tmgBdEN4BmmMXf2FT92vXChR8IgvZtyAkmC%2BuvnCw%2BHt9iF0zHXkbDo%2Bf0apUQM7aleTmilbxRE27%2FxG%2Fb7Um%2By3%2Bc8%2Ff808nf3HX9d9DjFXdGRNSHaEEvnjiKlM7kqyIJ5HuZgcnr6dHRh0rHlGMd1FO02yjedqXe0ElrEvo2ly1Msw55brvAY6pgHpP5P0TcQs7yv9nMNkH2H7fDJcS4seomXa7S7VeJe1T%2BgJuPz5rO6pK1S09sJCg%2FGOEyA4yBYS5O9l%2Bw%2F8u5tXZPEUaQXSOjDZHEPF9NNeyn2MydtcKWhMZbnIldXJ1fXmsd74I8cN%2FFq3arPgWp7uoddpoZZE12M4roz2t80%2BMeswpUPMG3r78opRIGUvSvjUvTMQkg%2BaMQJGLQe67FN67dKR04M4&X-Amz-Signature=b94c09ed098a626b01aaaf64375b16d7e7d680ecdf639967fff5b2c5e9dab4b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHGVXR3K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2MpLgnhcEUPVsuorRi8QfEPa65gTZjPxiOcUZwSajKAiEAu%2FP%2F9OmLYMiG3zVr3w10%2FXhCcp3q6cVtigy%2BkcrFIwgqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOY9jmqjDnH97PIpayrcAyGx1uhfdAHFypFjZ92bG%2BH6TplgUK1vqBNRtFR6WbUzkqemYCB7wXYJ8YRIfF385YjMxXkSCNsAFLaIueVDfUul9CkNjOaFYqWrXe90ilU62qbmIasAfVnhP0AhbCkBwt4ESFQ0dNdJU2kTFBK%2BKDN0bwhl5mvyNKkau08RMjKPPuTULBe%2BtKHT3CtsAhnhaJfKimwddfvr64HvKq1e%2FmHGJWnMCYpuFMEP%2BG3kSVA6iDEhwwl5zuOyn7rG4M%2F6gZA%2FxFQXM6QxrtlCBA%2BDdOOVn5kd5p8kJyItliVJHMwtnCRd8VaxUmKiUt6NsyFWJbfWWnDkSVhbrZGwtfYeiT6cbkApd7pUvZXXW5t0kKoDUr4vWHga8IfrtBQB50Lynm2EcokDgvAX3u93zjQRO%2BiTIlGwkghnW%2B1FVZhbMaJDqUh%2FNsKwbWkP0PoftXCSgCOrbH%2F8XwAOExBgsMmrMVA7623ZYdnnL7FhR4Tn58vN5mmh%2FmZCKpI5kYArnEK%2FWuhgiFH1c2NcJu7r01hyxarDcUACpFKcu%2BEuIXkLyRpjjjlf7gI1jSChSxgOT%2FXUMZmQ88XGDFbWYCHV%2Fj%2BhMW38Sy19TmgaVP%2BXMdWkpnP6S48bJy%2FQPM69AbdtMJaX67wGOqUBHH2ZaodMcuSwjMtjBD6mVW8gxd2oSg4OCOrObuW%2BMZHjBlOC9BLnxedKzeuFu3VhXaskXV68M3UJR%2BOaQDkG406E3Ry%2FFvcrdEouRhh%2BV7b0w9rIcWY7fpPRfaPvr9soObBUUXhpTVBq7iELIVvpxXrmziRRKcnjDOrnzca9TlMjO%2FkBx%2FQ5xe8e%2FsT7kFOdOmkvInieHvDsF3hQeIchRCT8LSzW&X-Amz-Signature=84a8428e1402b3fe3c79cf95bcf602d476062c05020d78a1a954806222728ec8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHGVXR3K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2MpLgnhcEUPVsuorRi8QfEPa65gTZjPxiOcUZwSajKAiEAu%2FP%2F9OmLYMiG3zVr3w10%2FXhCcp3q6cVtigy%2BkcrFIwgqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOY9jmqjDnH97PIpayrcAyGx1uhfdAHFypFjZ92bG%2BH6TplgUK1vqBNRtFR6WbUzkqemYCB7wXYJ8YRIfF385YjMxXkSCNsAFLaIueVDfUul9CkNjOaFYqWrXe90ilU62qbmIasAfVnhP0AhbCkBwt4ESFQ0dNdJU2kTFBK%2BKDN0bwhl5mvyNKkau08RMjKPPuTULBe%2BtKHT3CtsAhnhaJfKimwddfvr64HvKq1e%2FmHGJWnMCYpuFMEP%2BG3kSVA6iDEhwwl5zuOyn7rG4M%2F6gZA%2FxFQXM6QxrtlCBA%2BDdOOVn5kd5p8kJyItliVJHMwtnCRd8VaxUmKiUt6NsyFWJbfWWnDkSVhbrZGwtfYeiT6cbkApd7pUvZXXW5t0kKoDUr4vWHga8IfrtBQB50Lynm2EcokDgvAX3u93zjQRO%2BiTIlGwkghnW%2B1FVZhbMaJDqUh%2FNsKwbWkP0PoftXCSgCOrbH%2F8XwAOExBgsMmrMVA7623ZYdnnL7FhR4Tn58vN5mmh%2FmZCKpI5kYArnEK%2FWuhgiFH1c2NcJu7r01hyxarDcUACpFKcu%2BEuIXkLyRpjjjlf7gI1jSChSxgOT%2FXUMZmQ88XGDFbWYCHV%2Fj%2BhMW38Sy19TmgaVP%2BXMdWkpnP6S48bJy%2FQPM69AbdtMJaX67wGOqUBHH2ZaodMcuSwjMtjBD6mVW8gxd2oSg4OCOrObuW%2BMZHjBlOC9BLnxedKzeuFu3VhXaskXV68M3UJR%2BOaQDkG406E3Ry%2FFvcrdEouRhh%2BV7b0w9rIcWY7fpPRfaPvr9soObBUUXhpTVBq7iELIVvpxXrmziRRKcnjDOrnzca9TlMjO%2FkBx%2FQ5xe8e%2FsT7kFOdOmkvInieHvDsF3hQeIchRCT8LSzW&X-Amz-Signature=3b783ee7799d4aa870dcdd0837c365ee7f4a79f7aa3009b4b1571d2a0f756aee&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
