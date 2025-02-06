

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U65FN3X3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDkPRcdttXm0FvgTBv48ZxmbWcHYrmMMqYtChoLpMmcngIhAJwXl%2F20Q4zABxRRxz%2Bu6lC5jWYzOTwKv6N51ZF8ymx8Kv8DCFEQABoMNjM3NDIzMTgzODA1IgzKry8yWddukI0f1E8q3ANxZrxpWdYIIsg7eYrfRA2doKmeJiEx0XwDRj5LSySajKMDKEN20fBjBGUkDX0JPCOvKO26fmwpSP%2B46H784feswsSZs6zqDecqq%2FwJuqIM66SKM1jvgyD4RXqHktW6kNvBRdQS8YrzQdYCAWwEpQtc3XEzLKCNBhg0PiTUBA1A9UqwjNT6Tm6%2B2vHJ6UN8%2BsEpPLyYr3ZEiE3OLmL%2BI%2Br6uthZTYmKOpybCrqdEBkJSwsy8fsWgvREIfD9Rgp9QMNdQObO%2BEB86l5XaNBbi7uAiExu2x9akk5O3odA0eef%2BaduUqNKN9P%2Bd8El4%2F2MInJ9ksm%2F%2BTaVBEkgw4X4wVgR7s%2FyWhc2o1UpDi1Wk95G64EJLn9zKj2zVnKQyL0qJK0CMRrHagsqaSw4yYbYVSrKGht0uOUbB1v7qKSQiULM6CHo2%2FxWTG67RyZupElCnxMuGLIiPG%2BZ%2FTxik6wAi29%2BgG9pLuwONP1Hp80U7ceD9Oox4%2F3ZaJRC%2Fp2ArNnOxZiErZ97FfIV9QbXGhxl%2BFiEsedSBV5Z%2FxLVQBKlE9hur%2BSPN8LdYPFByiK6KVYbnIf4s%2FkP52DPuzxpf2rzLCoe8nXBs7K0brD%2Fo0PIB9AylTkpcVQ09%2B250ISzSTC%2F6o%2B9BjqkAZ2MmcD38LYd%2Flnwm6xKLgrVOTSnwZROp%2BOlPtDt2uooNh1hz7m7XXxnL1ULtDPHWSQHvrjm8Xz%2FonjN2NhEZmIkB8%2BYq%2BApbZ37jwkSyUiuXUZp8uEMuGmYN%2FkEbkOKtxk5OAufKmg2JrTkgAeKbgiKZdOrZrz%2FMmxckgO3lKGB7uqsq%2F%2Bc2hiC9nk6o7kE3PTHTIuHhZrQUSfhnK0N39RB2bIm&X-Amz-Signature=35f572c0235b78910f89f1ab4cb973c07461e8fbdc0c52509145bc16d5be1ecf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U65FN3X3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDkPRcdttXm0FvgTBv48ZxmbWcHYrmMMqYtChoLpMmcngIhAJwXl%2F20Q4zABxRRxz%2Bu6lC5jWYzOTwKv6N51ZF8ymx8Kv8DCFEQABoMNjM3NDIzMTgzODA1IgzKry8yWddukI0f1E8q3ANxZrxpWdYIIsg7eYrfRA2doKmeJiEx0XwDRj5LSySajKMDKEN20fBjBGUkDX0JPCOvKO26fmwpSP%2B46H784feswsSZs6zqDecqq%2FwJuqIM66SKM1jvgyD4RXqHktW6kNvBRdQS8YrzQdYCAWwEpQtc3XEzLKCNBhg0PiTUBA1A9UqwjNT6Tm6%2B2vHJ6UN8%2BsEpPLyYr3ZEiE3OLmL%2BI%2Br6uthZTYmKOpybCrqdEBkJSwsy8fsWgvREIfD9Rgp9QMNdQObO%2BEB86l5XaNBbi7uAiExu2x9akk5O3odA0eef%2BaduUqNKN9P%2Bd8El4%2F2MInJ9ksm%2F%2BTaVBEkgw4X4wVgR7s%2FyWhc2o1UpDi1Wk95G64EJLn9zKj2zVnKQyL0qJK0CMRrHagsqaSw4yYbYVSrKGht0uOUbB1v7qKSQiULM6CHo2%2FxWTG67RyZupElCnxMuGLIiPG%2BZ%2FTxik6wAi29%2BgG9pLuwONP1Hp80U7ceD9Oox4%2F3ZaJRC%2Fp2ArNnOxZiErZ97FfIV9QbXGhxl%2BFiEsedSBV5Z%2FxLVQBKlE9hur%2BSPN8LdYPFByiK6KVYbnIf4s%2FkP52DPuzxpf2rzLCoe8nXBs7K0brD%2Fo0PIB9AylTkpcVQ09%2B250ISzSTC%2F6o%2B9BjqkAZ2MmcD38LYd%2Flnwm6xKLgrVOTSnwZROp%2BOlPtDt2uooNh1hz7m7XXxnL1ULtDPHWSQHvrjm8Xz%2FonjN2NhEZmIkB8%2BYq%2BApbZ37jwkSyUiuXUZp8uEMuGmYN%2FkEbkOKtxk5OAufKmg2JrTkgAeKbgiKZdOrZrz%2FMmxckgO3lKGB7uqsq%2F%2Bc2hiC9nk6o7kE3PTHTIuHhZrQUSfhnK0N39RB2bIm&X-Amz-Signature=6fb1852378a7396d72bfa2561af93148c55e8681f8a860edae1f010680211e97&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U65FN3X3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDkPRcdttXm0FvgTBv48ZxmbWcHYrmMMqYtChoLpMmcngIhAJwXl%2F20Q4zABxRRxz%2Bu6lC5jWYzOTwKv6N51ZF8ymx8Kv8DCFEQABoMNjM3NDIzMTgzODA1IgzKry8yWddukI0f1E8q3ANxZrxpWdYIIsg7eYrfRA2doKmeJiEx0XwDRj5LSySajKMDKEN20fBjBGUkDX0JPCOvKO26fmwpSP%2B46H784feswsSZs6zqDecqq%2FwJuqIM66SKM1jvgyD4RXqHktW6kNvBRdQS8YrzQdYCAWwEpQtc3XEzLKCNBhg0PiTUBA1A9UqwjNT6Tm6%2B2vHJ6UN8%2BsEpPLyYr3ZEiE3OLmL%2BI%2Br6uthZTYmKOpybCrqdEBkJSwsy8fsWgvREIfD9Rgp9QMNdQObO%2BEB86l5XaNBbi7uAiExu2x9akk5O3odA0eef%2BaduUqNKN9P%2Bd8El4%2F2MInJ9ksm%2F%2BTaVBEkgw4X4wVgR7s%2FyWhc2o1UpDi1Wk95G64EJLn9zKj2zVnKQyL0qJK0CMRrHagsqaSw4yYbYVSrKGht0uOUbB1v7qKSQiULM6CHo2%2FxWTG67RyZupElCnxMuGLIiPG%2BZ%2FTxik6wAi29%2BgG9pLuwONP1Hp80U7ceD9Oox4%2F3ZaJRC%2Fp2ArNnOxZiErZ97FfIV9QbXGhxl%2BFiEsedSBV5Z%2FxLVQBKlE9hur%2BSPN8LdYPFByiK6KVYbnIf4s%2FkP52DPuzxpf2rzLCoe8nXBs7K0brD%2Fo0PIB9AylTkpcVQ09%2B250ISzSTC%2F6o%2B9BjqkAZ2MmcD38LYd%2Flnwm6xKLgrVOTSnwZROp%2BOlPtDt2uooNh1hz7m7XXxnL1ULtDPHWSQHvrjm8Xz%2FonjN2NhEZmIkB8%2BYq%2BApbZ37jwkSyUiuXUZp8uEMuGmYN%2FkEbkOKtxk5OAufKmg2JrTkgAeKbgiKZdOrZrz%2FMmxckgO3lKGB7uqsq%2F%2Bc2hiC9nk6o7kE3PTHTIuHhZrQUSfhnK0N39RB2bIm&X-Amz-Signature=ec3cc9387ada27a47f600c2e8e79493baea9a78af7a1f0a4d17d2fda4af409ea&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U65FN3X3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDkPRcdttXm0FvgTBv48ZxmbWcHYrmMMqYtChoLpMmcngIhAJwXl%2F20Q4zABxRRxz%2Bu6lC5jWYzOTwKv6N51ZF8ymx8Kv8DCFEQABoMNjM3NDIzMTgzODA1IgzKry8yWddukI0f1E8q3ANxZrxpWdYIIsg7eYrfRA2doKmeJiEx0XwDRj5LSySajKMDKEN20fBjBGUkDX0JPCOvKO26fmwpSP%2B46H784feswsSZs6zqDecqq%2FwJuqIM66SKM1jvgyD4RXqHktW6kNvBRdQS8YrzQdYCAWwEpQtc3XEzLKCNBhg0PiTUBA1A9UqwjNT6Tm6%2B2vHJ6UN8%2BsEpPLyYr3ZEiE3OLmL%2BI%2Br6uthZTYmKOpybCrqdEBkJSwsy8fsWgvREIfD9Rgp9QMNdQObO%2BEB86l5XaNBbi7uAiExu2x9akk5O3odA0eef%2BaduUqNKN9P%2Bd8El4%2F2MInJ9ksm%2F%2BTaVBEkgw4X4wVgR7s%2FyWhc2o1UpDi1Wk95G64EJLn9zKj2zVnKQyL0qJK0CMRrHagsqaSw4yYbYVSrKGht0uOUbB1v7qKSQiULM6CHo2%2FxWTG67RyZupElCnxMuGLIiPG%2BZ%2FTxik6wAi29%2BgG9pLuwONP1Hp80U7ceD9Oox4%2F3ZaJRC%2Fp2ArNnOxZiErZ97FfIV9QbXGhxl%2BFiEsedSBV5Z%2FxLVQBKlE9hur%2BSPN8LdYPFByiK6KVYbnIf4s%2FkP52DPuzxpf2rzLCoe8nXBs7K0brD%2Fo0PIB9AylTkpcVQ09%2B250ISzSTC%2F6o%2B9BjqkAZ2MmcD38LYd%2Flnwm6xKLgrVOTSnwZROp%2BOlPtDt2uooNh1hz7m7XXxnL1ULtDPHWSQHvrjm8Xz%2FonjN2NhEZmIkB8%2BYq%2BApbZ37jwkSyUiuXUZp8uEMuGmYN%2FkEbkOKtxk5OAufKmg2JrTkgAeKbgiKZdOrZrz%2FMmxckgO3lKGB7uqsq%2F%2Bc2hiC9nk6o7kE3PTHTIuHhZrQUSfhnK0N39RB2bIm&X-Amz-Signature=f00c6b755e0adff6b3db14c366fb4f44806a1839aa8b8c7c765a6aa076d92d5f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U65FN3X3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDkPRcdttXm0FvgTBv48ZxmbWcHYrmMMqYtChoLpMmcngIhAJwXl%2F20Q4zABxRRxz%2Bu6lC5jWYzOTwKv6N51ZF8ymx8Kv8DCFEQABoMNjM3NDIzMTgzODA1IgzKry8yWddukI0f1E8q3ANxZrxpWdYIIsg7eYrfRA2doKmeJiEx0XwDRj5LSySajKMDKEN20fBjBGUkDX0JPCOvKO26fmwpSP%2B46H784feswsSZs6zqDecqq%2FwJuqIM66SKM1jvgyD4RXqHktW6kNvBRdQS8YrzQdYCAWwEpQtc3XEzLKCNBhg0PiTUBA1A9UqwjNT6Tm6%2B2vHJ6UN8%2BsEpPLyYr3ZEiE3OLmL%2BI%2Br6uthZTYmKOpybCrqdEBkJSwsy8fsWgvREIfD9Rgp9QMNdQObO%2BEB86l5XaNBbi7uAiExu2x9akk5O3odA0eef%2BaduUqNKN9P%2Bd8El4%2F2MInJ9ksm%2F%2BTaVBEkgw4X4wVgR7s%2FyWhc2o1UpDi1Wk95G64EJLn9zKj2zVnKQyL0qJK0CMRrHagsqaSw4yYbYVSrKGht0uOUbB1v7qKSQiULM6CHo2%2FxWTG67RyZupElCnxMuGLIiPG%2BZ%2FTxik6wAi29%2BgG9pLuwONP1Hp80U7ceD9Oox4%2F3ZaJRC%2Fp2ArNnOxZiErZ97FfIV9QbXGhxl%2BFiEsedSBV5Z%2FxLVQBKlE9hur%2BSPN8LdYPFByiK6KVYbnIf4s%2FkP52DPuzxpf2rzLCoe8nXBs7K0brD%2Fo0PIB9AylTkpcVQ09%2B250ISzSTC%2F6o%2B9BjqkAZ2MmcD38LYd%2Flnwm6xKLgrVOTSnwZROp%2BOlPtDt2uooNh1hz7m7XXxnL1ULtDPHWSQHvrjm8Xz%2FonjN2NhEZmIkB8%2BYq%2BApbZ37jwkSyUiuXUZp8uEMuGmYN%2FkEbkOKtxk5OAufKmg2JrTkgAeKbgiKZdOrZrz%2FMmxckgO3lKGB7uqsq%2F%2Bc2hiC9nk6o7kE3PTHTIuHhZrQUSfhnK0N39RB2bIm&X-Amz-Signature=52af34f39077d658e66ad4af18601ac7e07123328a671d735e619e6eabf7bde3&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U65FN3X3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDkPRcdttXm0FvgTBv48ZxmbWcHYrmMMqYtChoLpMmcngIhAJwXl%2F20Q4zABxRRxz%2Bu6lC5jWYzOTwKv6N51ZF8ymx8Kv8DCFEQABoMNjM3NDIzMTgzODA1IgzKry8yWddukI0f1E8q3ANxZrxpWdYIIsg7eYrfRA2doKmeJiEx0XwDRj5LSySajKMDKEN20fBjBGUkDX0JPCOvKO26fmwpSP%2B46H784feswsSZs6zqDecqq%2FwJuqIM66SKM1jvgyD4RXqHktW6kNvBRdQS8YrzQdYCAWwEpQtc3XEzLKCNBhg0PiTUBA1A9UqwjNT6Tm6%2B2vHJ6UN8%2BsEpPLyYr3ZEiE3OLmL%2BI%2Br6uthZTYmKOpybCrqdEBkJSwsy8fsWgvREIfD9Rgp9QMNdQObO%2BEB86l5XaNBbi7uAiExu2x9akk5O3odA0eef%2BaduUqNKN9P%2Bd8El4%2F2MInJ9ksm%2F%2BTaVBEkgw4X4wVgR7s%2FyWhc2o1UpDi1Wk95G64EJLn9zKj2zVnKQyL0qJK0CMRrHagsqaSw4yYbYVSrKGht0uOUbB1v7qKSQiULM6CHo2%2FxWTG67RyZupElCnxMuGLIiPG%2BZ%2FTxik6wAi29%2BgG9pLuwONP1Hp80U7ceD9Oox4%2F3ZaJRC%2Fp2ArNnOxZiErZ97FfIV9QbXGhxl%2BFiEsedSBV5Z%2FxLVQBKlE9hur%2BSPN8LdYPFByiK6KVYbnIf4s%2FkP52DPuzxpf2rzLCoe8nXBs7K0brD%2Fo0PIB9AylTkpcVQ09%2B250ISzSTC%2F6o%2B9BjqkAZ2MmcD38LYd%2Flnwm6xKLgrVOTSnwZROp%2BOlPtDt2uooNh1hz7m7XXxnL1ULtDPHWSQHvrjm8Xz%2FonjN2NhEZmIkB8%2BYq%2BApbZ37jwkSyUiuXUZp8uEMuGmYN%2FkEbkOKtxk5OAufKmg2JrTkgAeKbgiKZdOrZrz%2FMmxckgO3lKGB7uqsq%2F%2Bc2hiC9nk6o7kE3PTHTIuHhZrQUSfhnK0N39RB2bIm&X-Amz-Signature=3bae006b86c45280314a11ed6e71d22c6d6de7df73259da4f9125d7de7cfb706&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U65FN3X3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDkPRcdttXm0FvgTBv48ZxmbWcHYrmMMqYtChoLpMmcngIhAJwXl%2F20Q4zABxRRxz%2Bu6lC5jWYzOTwKv6N51ZF8ymx8Kv8DCFEQABoMNjM3NDIzMTgzODA1IgzKry8yWddukI0f1E8q3ANxZrxpWdYIIsg7eYrfRA2doKmeJiEx0XwDRj5LSySajKMDKEN20fBjBGUkDX0JPCOvKO26fmwpSP%2B46H784feswsSZs6zqDecqq%2FwJuqIM66SKM1jvgyD4RXqHktW6kNvBRdQS8YrzQdYCAWwEpQtc3XEzLKCNBhg0PiTUBA1A9UqwjNT6Tm6%2B2vHJ6UN8%2BsEpPLyYr3ZEiE3OLmL%2BI%2Br6uthZTYmKOpybCrqdEBkJSwsy8fsWgvREIfD9Rgp9QMNdQObO%2BEB86l5XaNBbi7uAiExu2x9akk5O3odA0eef%2BaduUqNKN9P%2Bd8El4%2F2MInJ9ksm%2F%2BTaVBEkgw4X4wVgR7s%2FyWhc2o1UpDi1Wk95G64EJLn9zKj2zVnKQyL0qJK0CMRrHagsqaSw4yYbYVSrKGht0uOUbB1v7qKSQiULM6CHo2%2FxWTG67RyZupElCnxMuGLIiPG%2BZ%2FTxik6wAi29%2BgG9pLuwONP1Hp80U7ceD9Oox4%2F3ZaJRC%2Fp2ArNnOxZiErZ97FfIV9QbXGhxl%2BFiEsedSBV5Z%2FxLVQBKlE9hur%2BSPN8LdYPFByiK6KVYbnIf4s%2FkP52DPuzxpf2rzLCoe8nXBs7K0brD%2Fo0PIB9AylTkpcVQ09%2B250ISzSTC%2F6o%2B9BjqkAZ2MmcD38LYd%2Flnwm6xKLgrVOTSnwZROp%2BOlPtDt2uooNh1hz7m7XXxnL1ULtDPHWSQHvrjm8Xz%2FonjN2NhEZmIkB8%2BYq%2BApbZ37jwkSyUiuXUZp8uEMuGmYN%2FkEbkOKtxk5OAufKmg2JrTkgAeKbgiKZdOrZrz%2FMmxckgO3lKGB7uqsq%2F%2Bc2hiC9nk6o7kE3PTHTIuHhZrQUSfhnK0N39RB2bIm&X-Amz-Signature=a7caea17c77a4d8fc3e0780afd18e10b2655b61e66851d843c314292334fd4ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U65FN3X3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDkPRcdttXm0FvgTBv48ZxmbWcHYrmMMqYtChoLpMmcngIhAJwXl%2F20Q4zABxRRxz%2Bu6lC5jWYzOTwKv6N51ZF8ymx8Kv8DCFEQABoMNjM3NDIzMTgzODA1IgzKry8yWddukI0f1E8q3ANxZrxpWdYIIsg7eYrfRA2doKmeJiEx0XwDRj5LSySajKMDKEN20fBjBGUkDX0JPCOvKO26fmwpSP%2B46H784feswsSZs6zqDecqq%2FwJuqIM66SKM1jvgyD4RXqHktW6kNvBRdQS8YrzQdYCAWwEpQtc3XEzLKCNBhg0PiTUBA1A9UqwjNT6Tm6%2B2vHJ6UN8%2BsEpPLyYr3ZEiE3OLmL%2BI%2Br6uthZTYmKOpybCrqdEBkJSwsy8fsWgvREIfD9Rgp9QMNdQObO%2BEB86l5XaNBbi7uAiExu2x9akk5O3odA0eef%2BaduUqNKN9P%2Bd8El4%2F2MInJ9ksm%2F%2BTaVBEkgw4X4wVgR7s%2FyWhc2o1UpDi1Wk95G64EJLn9zKj2zVnKQyL0qJK0CMRrHagsqaSw4yYbYVSrKGht0uOUbB1v7qKSQiULM6CHo2%2FxWTG67RyZupElCnxMuGLIiPG%2BZ%2FTxik6wAi29%2BgG9pLuwONP1Hp80U7ceD9Oox4%2F3ZaJRC%2Fp2ArNnOxZiErZ97FfIV9QbXGhxl%2BFiEsedSBV5Z%2FxLVQBKlE9hur%2BSPN8LdYPFByiK6KVYbnIf4s%2FkP52DPuzxpf2rzLCoe8nXBs7K0brD%2Fo0PIB9AylTkpcVQ09%2B250ISzSTC%2F6o%2B9BjqkAZ2MmcD38LYd%2Flnwm6xKLgrVOTSnwZROp%2BOlPtDt2uooNh1hz7m7XXxnL1ULtDPHWSQHvrjm8Xz%2FonjN2NhEZmIkB8%2BYq%2BApbZ37jwkSyUiuXUZp8uEMuGmYN%2FkEbkOKtxk5OAufKmg2JrTkgAeKbgiKZdOrZrz%2FMmxckgO3lKGB7uqsq%2F%2Bc2hiC9nk6o7kE3PTHTIuHhZrQUSfhnK0N39RB2bIm&X-Amz-Signature=213601407a3a965a602e70da597d1c2e0077f60fb60e65eb6e5e38d78b18f6c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U65FN3X3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDkPRcdttXm0FvgTBv48ZxmbWcHYrmMMqYtChoLpMmcngIhAJwXl%2F20Q4zABxRRxz%2Bu6lC5jWYzOTwKv6N51ZF8ymx8Kv8DCFEQABoMNjM3NDIzMTgzODA1IgzKry8yWddukI0f1E8q3ANxZrxpWdYIIsg7eYrfRA2doKmeJiEx0XwDRj5LSySajKMDKEN20fBjBGUkDX0JPCOvKO26fmwpSP%2B46H784feswsSZs6zqDecqq%2FwJuqIM66SKM1jvgyD4RXqHktW6kNvBRdQS8YrzQdYCAWwEpQtc3XEzLKCNBhg0PiTUBA1A9UqwjNT6Tm6%2B2vHJ6UN8%2BsEpPLyYr3ZEiE3OLmL%2BI%2Br6uthZTYmKOpybCrqdEBkJSwsy8fsWgvREIfD9Rgp9QMNdQObO%2BEB86l5XaNBbi7uAiExu2x9akk5O3odA0eef%2BaduUqNKN9P%2Bd8El4%2F2MInJ9ksm%2F%2BTaVBEkgw4X4wVgR7s%2FyWhc2o1UpDi1Wk95G64EJLn9zKj2zVnKQyL0qJK0CMRrHagsqaSw4yYbYVSrKGht0uOUbB1v7qKSQiULM6CHo2%2FxWTG67RyZupElCnxMuGLIiPG%2BZ%2FTxik6wAi29%2BgG9pLuwONP1Hp80U7ceD9Oox4%2F3ZaJRC%2Fp2ArNnOxZiErZ97FfIV9QbXGhxl%2BFiEsedSBV5Z%2FxLVQBKlE9hur%2BSPN8LdYPFByiK6KVYbnIf4s%2FkP52DPuzxpf2rzLCoe8nXBs7K0brD%2Fo0PIB9AylTkpcVQ09%2B250ISzSTC%2F6o%2B9BjqkAZ2MmcD38LYd%2Flnwm6xKLgrVOTSnwZROp%2BOlPtDt2uooNh1hz7m7XXxnL1ULtDPHWSQHvrjm8Xz%2FonjN2NhEZmIkB8%2BYq%2BApbZ37jwkSyUiuXUZp8uEMuGmYN%2FkEbkOKtxk5OAufKmg2JrTkgAeKbgiKZdOrZrz%2FMmxckgO3lKGB7uqsq%2F%2Bc2hiC9nk6o7kE3PTHTIuHhZrQUSfhnK0N39RB2bIm&X-Amz-Signature=6466831ac67762d1de5f416654618e9657acf484136dc896b262c5bd3b7e5af3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUISLFBN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDsXgcwmGFHHXxQ9KVZvtv3N9xzy76c3G6ZlnGceJyQIgIhAK5uFoi52PP7ckENnKalDWQauzqViwZPcWBukcJwr%2FctKv8DCFEQABoMNjM3NDIzMTgzODA1IgxvKXpZemyPPLimTbQq3AOpMVeH2GsqSu7SesASXEjuc20lAunVxrMJFuOUjAX%2F0%2BPrqTFo1bFUA%2BVypO%2BjkZclQqkV%2Bhvjt0FRwIIUHYAaKDQgLz1sgTtq5NHx8KxrVD7t1pY0LLV0XlIctiJpZzGrQ5bZOUx%2BXFTZy2Rd87kJR9GM1N%2BYxyCJNzDXDqDCEE0WszCDFG3F0CA6QoD%2BxqPZsB1AGmTXH1CKYBItN0Yz2H%2FXQ3EGQeGUioIW%2BFpsoby4%2FAQOjcgHNzFTQ13D49ip2s9j3hlJOvi8mMCd2lIXyYxKg8bSelCebHJjUl6nLFoPMH59w7uW6ZeNTuyaLy1cVQ3d1FBnO9gaRLATAgWoEeWsYFzH7C74NKoioy9KTRaOsndZ66p4Pod7xLQ79iSNmglry73EgqFfpvj%2BvgKCtpB9877by4ATRJdnOT%2FOvHeMg3AOqYaHq7gQOmsyNih0drOCQWxUIcBTr7kYNkIdLJXsXjEs3rRyD2jbE3gR%2Btf3SxjODe2vv13IxmpdviSL66p53b4jmyTtUoarRAlIWgSSR2y1taNVj%2B9FDwYIigcXfXdjC%2Fj37V%2FmeTdWROWc%2Bi5ezpffPM0%2BK%2BUnvGPPdRouP5mN9%2FizZa%2BGHq08Ld7taxNMvTfoSPoRHjD76o%2B9BjqkAT2rJY3tuCRHD%2FCXQkbr2uhKJz3JFHBVNBd1%2FyNlzWxv45RiQE1tem0qcqBPr2WARp%2FMvyyMNjIcxcclAWoHsmNbcHyHWOYFwtSzjeT2lGdLYm0KomvYwy82%2Fk%2FDHWTvPIEHSg3wb4IVl1d64QVtbmAsNicyGpNm1Lnlyp086svaHem%2B%2F7aYK9gsn6nFN8W1St73krhtGi5bLKEv5WPHpZcUyWZa&X-Amz-Signature=c0c93d3bad558188ab13cab2a0ac5e973d4e9a5056b2abf0228f829750a3588e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUISLFBN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDsXgcwmGFHHXxQ9KVZvtv3N9xzy76c3G6ZlnGceJyQIgIhAK5uFoi52PP7ckENnKalDWQauzqViwZPcWBukcJwr%2FctKv8DCFEQABoMNjM3NDIzMTgzODA1IgxvKXpZemyPPLimTbQq3AOpMVeH2GsqSu7SesASXEjuc20lAunVxrMJFuOUjAX%2F0%2BPrqTFo1bFUA%2BVypO%2BjkZclQqkV%2Bhvjt0FRwIIUHYAaKDQgLz1sgTtq5NHx8KxrVD7t1pY0LLV0XlIctiJpZzGrQ5bZOUx%2BXFTZy2Rd87kJR9GM1N%2BYxyCJNzDXDqDCEE0WszCDFG3F0CA6QoD%2BxqPZsB1AGmTXH1CKYBItN0Yz2H%2FXQ3EGQeGUioIW%2BFpsoby4%2FAQOjcgHNzFTQ13D49ip2s9j3hlJOvi8mMCd2lIXyYxKg8bSelCebHJjUl6nLFoPMH59w7uW6ZeNTuyaLy1cVQ3d1FBnO9gaRLATAgWoEeWsYFzH7C74NKoioy9KTRaOsndZ66p4Pod7xLQ79iSNmglry73EgqFfpvj%2BvgKCtpB9877by4ATRJdnOT%2FOvHeMg3AOqYaHq7gQOmsyNih0drOCQWxUIcBTr7kYNkIdLJXsXjEs3rRyD2jbE3gR%2Btf3SxjODe2vv13IxmpdviSL66p53b4jmyTtUoarRAlIWgSSR2y1taNVj%2B9FDwYIigcXfXdjC%2Fj37V%2FmeTdWROWc%2Bi5ezpffPM0%2BK%2BUnvGPPdRouP5mN9%2FizZa%2BGHq08Ld7taxNMvTfoSPoRHjD76o%2B9BjqkAT2rJY3tuCRHD%2FCXQkbr2uhKJz3JFHBVNBd1%2FyNlzWxv45RiQE1tem0qcqBPr2WARp%2FMvyyMNjIcxcclAWoHsmNbcHyHWOYFwtSzjeT2lGdLYm0KomvYwy82%2Fk%2FDHWTvPIEHSg3wb4IVl1d64QVtbmAsNicyGpNm1Lnlyp086svaHem%2B%2F7aYK9gsn6nFN8W1St73krhtGi5bLKEv5WPHpZcUyWZa&X-Amz-Signature=664a6f3ffe2862103be295d3076b207b46309414880d3ae828e06b1d67027e7a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
