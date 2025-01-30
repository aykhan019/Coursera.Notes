

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6LVECU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfMYNmDeEhnNtwSUNE3Zr3oatZOqttqWb%2BiROMItJl9AiA1AjUBI%2FsWBC2WF3%2BkntpvPGxOzeRn9ay3pnN4cmnDaiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzy5g1pX2ZleeDOy7KtwD1TVS%2F5bV7WSVPt1qE017Ahz7pAlsha6b5Jch9CICFmHhyYTLHYLxSd5vZHGNoBs%2F7V4Aakmu%2BqCqcAm9XP3apf73WyP1Kebig2jrRrTp999rrV9Cj3PN7RmWEAhu8FaoohV4RpMwmkeGwwhg%2Bm8bk%2FSRQOmFLaGaCfD8GROrIYujs%2FOPQer%2F11ae6C6tOBIqeug9e%2BwzO6jLuwaZ7trTd2KjsCPfGrfqZ%2BPGM3kZS6asPz9wXtcQLtVco%2FEr%2BNkwHOS3f3rcZJmC0bIAAU45vc7%2FR%2FKTuRwgQHBD%2BKkMJ2%2BlNsnBnuOZQ7i3TPsZkoadhvVnhf8mepJs7bBSUj0Vf%2Fy8tXEEwUfejlrglGF6US7WKD%2BvVbZF6ZN%2B%2FH668S32%2BLVB50u5feeAmnf9PcO7qamf44428vtPSi3%2BAcrSJh8NmoHjyeGqksSGtPmqAu9YFqIOz6eav%2FiZNStUrB6UbvtfkB%2BgCLgzsvnvkPGsuU1xauTpccdSwW2aJKK1cOdzo8z1lov3qXeU0dcFy6oLYLn6d%2FbQhvu5h2MeT9Rj1mF517HzBflLyNUuPSXQ6CstDlto0YGAAATeimuSQsarj%2B31UukS1QaRFUdXnDBSw3nU5fqSijlk5z6MZcUwksXvvAY6pgFXbfJVzn07PECdWGATxG6TVwz3JdfoZIB5FL6DrNaZZu6wZGrZbFTNL%2FELZIlAkkQPUknYt3ORE%2BXycZKUEHtV4K%2FPdcLwmLqUYshW3awCJ6kbKnQwNM7whFeZq1sO82exqFpyC2z0zIaYsTdx%2FBp8nHq4uSzfqiOAv8PsUevCM5RehhUNKLGZLJvmiuxQAKvaFOEXLx89LTyeuKo0UKVXpiUq%2Bwvr&X-Amz-Signature=33d612a53e239b9649ce0ff9da917a0e9c80b848016a8916629fe1144b85e331&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6LVECU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfMYNmDeEhnNtwSUNE3Zr3oatZOqttqWb%2BiROMItJl9AiA1AjUBI%2FsWBC2WF3%2BkntpvPGxOzeRn9ay3pnN4cmnDaiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzy5g1pX2ZleeDOy7KtwD1TVS%2F5bV7WSVPt1qE017Ahz7pAlsha6b5Jch9CICFmHhyYTLHYLxSd5vZHGNoBs%2F7V4Aakmu%2BqCqcAm9XP3apf73WyP1Kebig2jrRrTp999rrV9Cj3PN7RmWEAhu8FaoohV4RpMwmkeGwwhg%2Bm8bk%2FSRQOmFLaGaCfD8GROrIYujs%2FOPQer%2F11ae6C6tOBIqeug9e%2BwzO6jLuwaZ7trTd2KjsCPfGrfqZ%2BPGM3kZS6asPz9wXtcQLtVco%2FEr%2BNkwHOS3f3rcZJmC0bIAAU45vc7%2FR%2FKTuRwgQHBD%2BKkMJ2%2BlNsnBnuOZQ7i3TPsZkoadhvVnhf8mepJs7bBSUj0Vf%2Fy8tXEEwUfejlrglGF6US7WKD%2BvVbZF6ZN%2B%2FH668S32%2BLVB50u5feeAmnf9PcO7qamf44428vtPSi3%2BAcrSJh8NmoHjyeGqksSGtPmqAu9YFqIOz6eav%2FiZNStUrB6UbvtfkB%2BgCLgzsvnvkPGsuU1xauTpccdSwW2aJKK1cOdzo8z1lov3qXeU0dcFy6oLYLn6d%2FbQhvu5h2MeT9Rj1mF517HzBflLyNUuPSXQ6CstDlto0YGAAATeimuSQsarj%2B31UukS1QaRFUdXnDBSw3nU5fqSijlk5z6MZcUwksXvvAY6pgFXbfJVzn07PECdWGATxG6TVwz3JdfoZIB5FL6DrNaZZu6wZGrZbFTNL%2FELZIlAkkQPUknYt3ORE%2BXycZKUEHtV4K%2FPdcLwmLqUYshW3awCJ6kbKnQwNM7whFeZq1sO82exqFpyC2z0zIaYsTdx%2FBp8nHq4uSzfqiOAv8PsUevCM5RehhUNKLGZLJvmiuxQAKvaFOEXLx89LTyeuKo0UKVXpiUq%2Bwvr&X-Amz-Signature=a84aca1c2d2daaf29f12a9bfd78efdfe22f800657f771a0207a3ebb9c4cc56f1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6LVECU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfMYNmDeEhnNtwSUNE3Zr3oatZOqttqWb%2BiROMItJl9AiA1AjUBI%2FsWBC2WF3%2BkntpvPGxOzeRn9ay3pnN4cmnDaiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzy5g1pX2ZleeDOy7KtwD1TVS%2F5bV7WSVPt1qE017Ahz7pAlsha6b5Jch9CICFmHhyYTLHYLxSd5vZHGNoBs%2F7V4Aakmu%2BqCqcAm9XP3apf73WyP1Kebig2jrRrTp999rrV9Cj3PN7RmWEAhu8FaoohV4RpMwmkeGwwhg%2Bm8bk%2FSRQOmFLaGaCfD8GROrIYujs%2FOPQer%2F11ae6C6tOBIqeug9e%2BwzO6jLuwaZ7trTd2KjsCPfGrfqZ%2BPGM3kZS6asPz9wXtcQLtVco%2FEr%2BNkwHOS3f3rcZJmC0bIAAU45vc7%2FR%2FKTuRwgQHBD%2BKkMJ2%2BlNsnBnuOZQ7i3TPsZkoadhvVnhf8mepJs7bBSUj0Vf%2Fy8tXEEwUfejlrglGF6US7WKD%2BvVbZF6ZN%2B%2FH668S32%2BLVB50u5feeAmnf9PcO7qamf44428vtPSi3%2BAcrSJh8NmoHjyeGqksSGtPmqAu9YFqIOz6eav%2FiZNStUrB6UbvtfkB%2BgCLgzsvnvkPGsuU1xauTpccdSwW2aJKK1cOdzo8z1lov3qXeU0dcFy6oLYLn6d%2FbQhvu5h2MeT9Rj1mF517HzBflLyNUuPSXQ6CstDlto0YGAAATeimuSQsarj%2B31UukS1QaRFUdXnDBSw3nU5fqSijlk5z6MZcUwksXvvAY6pgFXbfJVzn07PECdWGATxG6TVwz3JdfoZIB5FL6DrNaZZu6wZGrZbFTNL%2FELZIlAkkQPUknYt3ORE%2BXycZKUEHtV4K%2FPdcLwmLqUYshW3awCJ6kbKnQwNM7whFeZq1sO82exqFpyC2z0zIaYsTdx%2FBp8nHq4uSzfqiOAv8PsUevCM5RehhUNKLGZLJvmiuxQAKvaFOEXLx89LTyeuKo0UKVXpiUq%2Bwvr&X-Amz-Signature=24c339ba2f5d255950749ccdcaf036af25874f15ed2e267e2e8cbf0b0a3aee2f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6LVECU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfMYNmDeEhnNtwSUNE3Zr3oatZOqttqWb%2BiROMItJl9AiA1AjUBI%2FsWBC2WF3%2BkntpvPGxOzeRn9ay3pnN4cmnDaiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzy5g1pX2ZleeDOy7KtwD1TVS%2F5bV7WSVPt1qE017Ahz7pAlsha6b5Jch9CICFmHhyYTLHYLxSd5vZHGNoBs%2F7V4Aakmu%2BqCqcAm9XP3apf73WyP1Kebig2jrRrTp999rrV9Cj3PN7RmWEAhu8FaoohV4RpMwmkeGwwhg%2Bm8bk%2FSRQOmFLaGaCfD8GROrIYujs%2FOPQer%2F11ae6C6tOBIqeug9e%2BwzO6jLuwaZ7trTd2KjsCPfGrfqZ%2BPGM3kZS6asPz9wXtcQLtVco%2FEr%2BNkwHOS3f3rcZJmC0bIAAU45vc7%2FR%2FKTuRwgQHBD%2BKkMJ2%2BlNsnBnuOZQ7i3TPsZkoadhvVnhf8mepJs7bBSUj0Vf%2Fy8tXEEwUfejlrglGF6US7WKD%2BvVbZF6ZN%2B%2FH668S32%2BLVB50u5feeAmnf9PcO7qamf44428vtPSi3%2BAcrSJh8NmoHjyeGqksSGtPmqAu9YFqIOz6eav%2FiZNStUrB6UbvtfkB%2BgCLgzsvnvkPGsuU1xauTpccdSwW2aJKK1cOdzo8z1lov3qXeU0dcFy6oLYLn6d%2FbQhvu5h2MeT9Rj1mF517HzBflLyNUuPSXQ6CstDlto0YGAAATeimuSQsarj%2B31UukS1QaRFUdXnDBSw3nU5fqSijlk5z6MZcUwksXvvAY6pgFXbfJVzn07PECdWGATxG6TVwz3JdfoZIB5FL6DrNaZZu6wZGrZbFTNL%2FELZIlAkkQPUknYt3ORE%2BXycZKUEHtV4K%2FPdcLwmLqUYshW3awCJ6kbKnQwNM7whFeZq1sO82exqFpyC2z0zIaYsTdx%2FBp8nHq4uSzfqiOAv8PsUevCM5RehhUNKLGZLJvmiuxQAKvaFOEXLx89LTyeuKo0UKVXpiUq%2Bwvr&X-Amz-Signature=d8a71775aca64015866e4f70076fc009dffa66bf90a5eebe600e3949d26af936&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6LVECU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfMYNmDeEhnNtwSUNE3Zr3oatZOqttqWb%2BiROMItJl9AiA1AjUBI%2FsWBC2WF3%2BkntpvPGxOzeRn9ay3pnN4cmnDaiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzy5g1pX2ZleeDOy7KtwD1TVS%2F5bV7WSVPt1qE017Ahz7pAlsha6b5Jch9CICFmHhyYTLHYLxSd5vZHGNoBs%2F7V4Aakmu%2BqCqcAm9XP3apf73WyP1Kebig2jrRrTp999rrV9Cj3PN7RmWEAhu8FaoohV4RpMwmkeGwwhg%2Bm8bk%2FSRQOmFLaGaCfD8GROrIYujs%2FOPQer%2F11ae6C6tOBIqeug9e%2BwzO6jLuwaZ7trTd2KjsCPfGrfqZ%2BPGM3kZS6asPz9wXtcQLtVco%2FEr%2BNkwHOS3f3rcZJmC0bIAAU45vc7%2FR%2FKTuRwgQHBD%2BKkMJ2%2BlNsnBnuOZQ7i3TPsZkoadhvVnhf8mepJs7bBSUj0Vf%2Fy8tXEEwUfejlrglGF6US7WKD%2BvVbZF6ZN%2B%2FH668S32%2BLVB50u5feeAmnf9PcO7qamf44428vtPSi3%2BAcrSJh8NmoHjyeGqksSGtPmqAu9YFqIOz6eav%2FiZNStUrB6UbvtfkB%2BgCLgzsvnvkPGsuU1xauTpccdSwW2aJKK1cOdzo8z1lov3qXeU0dcFy6oLYLn6d%2FbQhvu5h2MeT9Rj1mF517HzBflLyNUuPSXQ6CstDlto0YGAAATeimuSQsarj%2B31UukS1QaRFUdXnDBSw3nU5fqSijlk5z6MZcUwksXvvAY6pgFXbfJVzn07PECdWGATxG6TVwz3JdfoZIB5FL6DrNaZZu6wZGrZbFTNL%2FELZIlAkkQPUknYt3ORE%2BXycZKUEHtV4K%2FPdcLwmLqUYshW3awCJ6kbKnQwNM7whFeZq1sO82exqFpyC2z0zIaYsTdx%2FBp8nHq4uSzfqiOAv8PsUevCM5RehhUNKLGZLJvmiuxQAKvaFOEXLx89LTyeuKo0UKVXpiUq%2Bwvr&X-Amz-Signature=330b662fae03beb03a2ccc06fbfe19b5dcccae8881e80b095797f4cb045ea02d&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6LVECU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfMYNmDeEhnNtwSUNE3Zr3oatZOqttqWb%2BiROMItJl9AiA1AjUBI%2FsWBC2WF3%2BkntpvPGxOzeRn9ay3pnN4cmnDaiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzy5g1pX2ZleeDOy7KtwD1TVS%2F5bV7WSVPt1qE017Ahz7pAlsha6b5Jch9CICFmHhyYTLHYLxSd5vZHGNoBs%2F7V4Aakmu%2BqCqcAm9XP3apf73WyP1Kebig2jrRrTp999rrV9Cj3PN7RmWEAhu8FaoohV4RpMwmkeGwwhg%2Bm8bk%2FSRQOmFLaGaCfD8GROrIYujs%2FOPQer%2F11ae6C6tOBIqeug9e%2BwzO6jLuwaZ7trTd2KjsCPfGrfqZ%2BPGM3kZS6asPz9wXtcQLtVco%2FEr%2BNkwHOS3f3rcZJmC0bIAAU45vc7%2FR%2FKTuRwgQHBD%2BKkMJ2%2BlNsnBnuOZQ7i3TPsZkoadhvVnhf8mepJs7bBSUj0Vf%2Fy8tXEEwUfejlrglGF6US7WKD%2BvVbZF6ZN%2B%2FH668S32%2BLVB50u5feeAmnf9PcO7qamf44428vtPSi3%2BAcrSJh8NmoHjyeGqksSGtPmqAu9YFqIOz6eav%2FiZNStUrB6UbvtfkB%2BgCLgzsvnvkPGsuU1xauTpccdSwW2aJKK1cOdzo8z1lov3qXeU0dcFy6oLYLn6d%2FbQhvu5h2MeT9Rj1mF517HzBflLyNUuPSXQ6CstDlto0YGAAATeimuSQsarj%2B31UukS1QaRFUdXnDBSw3nU5fqSijlk5z6MZcUwksXvvAY6pgFXbfJVzn07PECdWGATxG6TVwz3JdfoZIB5FL6DrNaZZu6wZGrZbFTNL%2FELZIlAkkQPUknYt3ORE%2BXycZKUEHtV4K%2FPdcLwmLqUYshW3awCJ6kbKnQwNM7whFeZq1sO82exqFpyC2z0zIaYsTdx%2FBp8nHq4uSzfqiOAv8PsUevCM5RehhUNKLGZLJvmiuxQAKvaFOEXLx89LTyeuKo0UKVXpiUq%2Bwvr&X-Amz-Signature=efe54e5e4e307ce3d9487e5f79be65e004f68dac90a11991976587d25b07a49e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6LVECU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfMYNmDeEhnNtwSUNE3Zr3oatZOqttqWb%2BiROMItJl9AiA1AjUBI%2FsWBC2WF3%2BkntpvPGxOzeRn9ay3pnN4cmnDaiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzy5g1pX2ZleeDOy7KtwD1TVS%2F5bV7WSVPt1qE017Ahz7pAlsha6b5Jch9CICFmHhyYTLHYLxSd5vZHGNoBs%2F7V4Aakmu%2BqCqcAm9XP3apf73WyP1Kebig2jrRrTp999rrV9Cj3PN7RmWEAhu8FaoohV4RpMwmkeGwwhg%2Bm8bk%2FSRQOmFLaGaCfD8GROrIYujs%2FOPQer%2F11ae6C6tOBIqeug9e%2BwzO6jLuwaZ7trTd2KjsCPfGrfqZ%2BPGM3kZS6asPz9wXtcQLtVco%2FEr%2BNkwHOS3f3rcZJmC0bIAAU45vc7%2FR%2FKTuRwgQHBD%2BKkMJ2%2BlNsnBnuOZQ7i3TPsZkoadhvVnhf8mepJs7bBSUj0Vf%2Fy8tXEEwUfejlrglGF6US7WKD%2BvVbZF6ZN%2B%2FH668S32%2BLVB50u5feeAmnf9PcO7qamf44428vtPSi3%2BAcrSJh8NmoHjyeGqksSGtPmqAu9YFqIOz6eav%2FiZNStUrB6UbvtfkB%2BgCLgzsvnvkPGsuU1xauTpccdSwW2aJKK1cOdzo8z1lov3qXeU0dcFy6oLYLn6d%2FbQhvu5h2MeT9Rj1mF517HzBflLyNUuPSXQ6CstDlto0YGAAATeimuSQsarj%2B31UukS1QaRFUdXnDBSw3nU5fqSijlk5z6MZcUwksXvvAY6pgFXbfJVzn07PECdWGATxG6TVwz3JdfoZIB5FL6DrNaZZu6wZGrZbFTNL%2FELZIlAkkQPUknYt3ORE%2BXycZKUEHtV4K%2FPdcLwmLqUYshW3awCJ6kbKnQwNM7whFeZq1sO82exqFpyC2z0zIaYsTdx%2FBp8nHq4uSzfqiOAv8PsUevCM5RehhUNKLGZLJvmiuxQAKvaFOEXLx89LTyeuKo0UKVXpiUq%2Bwvr&X-Amz-Signature=718e67eb0fb6f2e71478da011257b470eca7437e996b0b7ad924cf56bd2654f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6LVECU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfMYNmDeEhnNtwSUNE3Zr3oatZOqttqWb%2BiROMItJl9AiA1AjUBI%2FsWBC2WF3%2BkntpvPGxOzeRn9ay3pnN4cmnDaiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzy5g1pX2ZleeDOy7KtwD1TVS%2F5bV7WSVPt1qE017Ahz7pAlsha6b5Jch9CICFmHhyYTLHYLxSd5vZHGNoBs%2F7V4Aakmu%2BqCqcAm9XP3apf73WyP1Kebig2jrRrTp999rrV9Cj3PN7RmWEAhu8FaoohV4RpMwmkeGwwhg%2Bm8bk%2FSRQOmFLaGaCfD8GROrIYujs%2FOPQer%2F11ae6C6tOBIqeug9e%2BwzO6jLuwaZ7trTd2KjsCPfGrfqZ%2BPGM3kZS6asPz9wXtcQLtVco%2FEr%2BNkwHOS3f3rcZJmC0bIAAU45vc7%2FR%2FKTuRwgQHBD%2BKkMJ2%2BlNsnBnuOZQ7i3TPsZkoadhvVnhf8mepJs7bBSUj0Vf%2Fy8tXEEwUfejlrglGF6US7WKD%2BvVbZF6ZN%2B%2FH668S32%2BLVB50u5feeAmnf9PcO7qamf44428vtPSi3%2BAcrSJh8NmoHjyeGqksSGtPmqAu9YFqIOz6eav%2FiZNStUrB6UbvtfkB%2BgCLgzsvnvkPGsuU1xauTpccdSwW2aJKK1cOdzo8z1lov3qXeU0dcFy6oLYLn6d%2FbQhvu5h2MeT9Rj1mF517HzBflLyNUuPSXQ6CstDlto0YGAAATeimuSQsarj%2B31UukS1QaRFUdXnDBSw3nU5fqSijlk5z6MZcUwksXvvAY6pgFXbfJVzn07PECdWGATxG6TVwz3JdfoZIB5FL6DrNaZZu6wZGrZbFTNL%2FELZIlAkkQPUknYt3ORE%2BXycZKUEHtV4K%2FPdcLwmLqUYshW3awCJ6kbKnQwNM7whFeZq1sO82exqFpyC2z0zIaYsTdx%2FBp8nHq4uSzfqiOAv8PsUevCM5RehhUNKLGZLJvmiuxQAKvaFOEXLx89LTyeuKo0UKVXpiUq%2Bwvr&X-Amz-Signature=48b0d307c0d7b463bae47069b637450f465b3af76a2508fee6409651b7281b85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6LVECU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfMYNmDeEhnNtwSUNE3Zr3oatZOqttqWb%2BiROMItJl9AiA1AjUBI%2FsWBC2WF3%2BkntpvPGxOzeRn9ay3pnN4cmnDaiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzy5g1pX2ZleeDOy7KtwD1TVS%2F5bV7WSVPt1qE017Ahz7pAlsha6b5Jch9CICFmHhyYTLHYLxSd5vZHGNoBs%2F7V4Aakmu%2BqCqcAm9XP3apf73WyP1Kebig2jrRrTp999rrV9Cj3PN7RmWEAhu8FaoohV4RpMwmkeGwwhg%2Bm8bk%2FSRQOmFLaGaCfD8GROrIYujs%2FOPQer%2F11ae6C6tOBIqeug9e%2BwzO6jLuwaZ7trTd2KjsCPfGrfqZ%2BPGM3kZS6asPz9wXtcQLtVco%2FEr%2BNkwHOS3f3rcZJmC0bIAAU45vc7%2FR%2FKTuRwgQHBD%2BKkMJ2%2BlNsnBnuOZQ7i3TPsZkoadhvVnhf8mepJs7bBSUj0Vf%2Fy8tXEEwUfejlrglGF6US7WKD%2BvVbZF6ZN%2B%2FH668S32%2BLVB50u5feeAmnf9PcO7qamf44428vtPSi3%2BAcrSJh8NmoHjyeGqksSGtPmqAu9YFqIOz6eav%2FiZNStUrB6UbvtfkB%2BgCLgzsvnvkPGsuU1xauTpccdSwW2aJKK1cOdzo8z1lov3qXeU0dcFy6oLYLn6d%2FbQhvu5h2MeT9Rj1mF517HzBflLyNUuPSXQ6CstDlto0YGAAATeimuSQsarj%2B31UukS1QaRFUdXnDBSw3nU5fqSijlk5z6MZcUwksXvvAY6pgFXbfJVzn07PECdWGATxG6TVwz3JdfoZIB5FL6DrNaZZu6wZGrZbFTNL%2FELZIlAkkQPUknYt3ORE%2BXycZKUEHtV4K%2FPdcLwmLqUYshW3awCJ6kbKnQwNM7whFeZq1sO82exqFpyC2z0zIaYsTdx%2FBp8nHq4uSzfqiOAv8PsUevCM5RehhUNKLGZLJvmiuxQAKvaFOEXLx89LTyeuKo0UKVXpiUq%2Bwvr&X-Amz-Signature=f8f1f5c11a9586da2e9519f06544f912e0ee265bc7490cced2bb3c12665afaae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DH5MFNM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH45f%2FRyD3b%2FuHhDQKqS8kKJVb5XUPxGNHJPT0pcoRgCAiEAovSLjnNjCpK1GpkZ5W9tu87a2Xl1Q%2F3mqrFWY2EXuDwqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMMzqr6iwzpvVjgc8yrcAwwD6%2BQ6k0%2FrGtz2oHYl%2FuxKZSByIptmajxIGgorBlNMicTjHo19DgAOhKCVpDaucaquET5GQ3jpZxEw2p7u%2FwBjS%2Frn3z2jazNBm1bW9VOa30S02qiZWyOcsh3oykVa4EsPN9bfoLUxvq7ai8l1%2Bo8fmrqQasoaXW43vYcp444Bl5lqHIw0wM7tiz13gMFZ1yQBbWyKrGzgqdPeqoG%2Fb4EtgC5hsF6ZSG9PUD7FTg8x%2FbIG4oSyILWyV7yXpq9yWYuQ9QF7LgG30lmf7xzPTtX5ICNer0JH37OWo1L%2F4HZ9BZi87sCqAMxf8MqYRC3M6WHqNhw2kiPYpZ82yZyK597h4jRUAgg84QohZRDBeiKf7RuySd4Jif%2BsmHNidI25kNmFElyV1kKgnVy9d57HICaelgjBOZJ0CqffcLDZXc%2FYwtnhzUQ%2FDcDcxojTFs1hoz887rDrhiBsTti6wC9jsnsfbV06sAiwt9F%2F14bhdmrlFAv%2B%2BcJ48ACwPPCp5POGjkfT5dKVWRhOUU%2FK0ons7jufc7FyL%2BZZnXbz8rUg%2FPFs3I1lsRwQf7H3ZWXWXtEOdpp38KgXL3mpj5rTooH9Gm19JBOebZT%2Bhx5wSLdtz9d%2Bci2wc3IyHaBWOL8IMKfF77wGOqUBtZvXZBYMyiWUu004Hn0mXJMqpkp1W0M%2FulTYmqkMzhXBcR08G2RxRug11FAsKqx0gnRsti7A1MDMjiVVRIV%2B7TfYPTjm2YAT6UTcMQ80INpgmjKsRF2LLSDEyXETG7SU2Y%2FOuY%2FN87Jy6k4hj7jVt52rk3JpqgPuSlhGCoM1x5WDUnqWmEB56VbKmDQtkTSQ7%2BO%2FEIj8gPNoQdgGdo06Cz3M1o9n&X-Amz-Signature=a8e623ec63117f8fad3a8d23d059d4fae9779809e5d69336e922462dd0388fb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DH5MFNM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH45f%2FRyD3b%2FuHhDQKqS8kKJVb5XUPxGNHJPT0pcoRgCAiEAovSLjnNjCpK1GpkZ5W9tu87a2Xl1Q%2F3mqrFWY2EXuDwqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMMzqr6iwzpvVjgc8yrcAwwD6%2BQ6k0%2FrGtz2oHYl%2FuxKZSByIptmajxIGgorBlNMicTjHo19DgAOhKCVpDaucaquET5GQ3jpZxEw2p7u%2FwBjS%2Frn3z2jazNBm1bW9VOa30S02qiZWyOcsh3oykVa4EsPN9bfoLUxvq7ai8l1%2Bo8fmrqQasoaXW43vYcp444Bl5lqHIw0wM7tiz13gMFZ1yQBbWyKrGzgqdPeqoG%2Fb4EtgC5hsF6ZSG9PUD7FTg8x%2FbIG4oSyILWyV7yXpq9yWYuQ9QF7LgG30lmf7xzPTtX5ICNer0JH37OWo1L%2F4HZ9BZi87sCqAMxf8MqYRC3M6WHqNhw2kiPYpZ82yZyK597h4jRUAgg84QohZRDBeiKf7RuySd4Jif%2BsmHNidI25kNmFElyV1kKgnVy9d57HICaelgjBOZJ0CqffcLDZXc%2FYwtnhzUQ%2FDcDcxojTFs1hoz887rDrhiBsTti6wC9jsnsfbV06sAiwt9F%2F14bhdmrlFAv%2B%2BcJ48ACwPPCp5POGjkfT5dKVWRhOUU%2FK0ons7jufc7FyL%2BZZnXbz8rUg%2FPFs3I1lsRwQf7H3ZWXWXtEOdpp38KgXL3mpj5rTooH9Gm19JBOebZT%2Bhx5wSLdtz9d%2Bci2wc3IyHaBWOL8IMKfF77wGOqUBtZvXZBYMyiWUu004Hn0mXJMqpkp1W0M%2FulTYmqkMzhXBcR08G2RxRug11FAsKqx0gnRsti7A1MDMjiVVRIV%2B7TfYPTjm2YAT6UTcMQ80INpgmjKsRF2LLSDEyXETG7SU2Y%2FOuY%2FN87Jy6k4hj7jVt52rk3JpqgPuSlhGCoM1x5WDUnqWmEB56VbKmDQtkTSQ7%2BO%2FEIj8gPNoQdgGdo06Cz3M1o9n&X-Amz-Signature=e073b2aa7f595634fd2fec0ecf253134cc0c399ff585b0ff6d5a3cc04949ac67&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
