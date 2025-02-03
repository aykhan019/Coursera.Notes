

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWXUVDXY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCILMpfztdwk58S5k6Y80ZA%2FSmmHhS6kXkWt5ebI5OyKAIgI8hmlBPP%2FEvCVa7vO0cOGRpEuUH8W5p4xIU6UYAoUX4qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrsBOirnADZlHzhWCrcAxYn0gOq%2BD3K295GgdhTobPZ1z%2FR4lYW2jNNQ2KQF7kzghm%2FHdIs%2FMKH508KXeBL79FSpWlm0o48pnvJI509b34KkTEuFCZS2htExJjxUcG8ajQ7W7fF%2FyCPldjCtwkbpe6oEGL58jhDSfPrLWn3fSRxJs%2B5v9uNm0EMibBhU5uy7Grnrl2AZkXNbRilFLEyaKazK%2BZXG8vUDPp8I%2B91otSdvWD4bCHyJ1Q47T8fbil%2FRDSUMLKvaYkN%2FtvrDWhiXoVITg2cmmRpqcNqpzH6FPTW9x9zmb%2FYU2FJgW1kTxVjZOd4McTPNUU5xBH6w8KL%2BKf%2BwNNbAr4kRVyrHeMaCLEbrJo%2FE6%2FK1%2FVDAx50UiKlQWLQTCdsxQ8HAkanOvBGStmBpaLL1%2BlrSInaK5zDYKAiQ8kFEX24mUnGtaN5VG795knekjTgjhalstinMGytS5tqrfSxEgQUMtU37QE2ZOzQaNMtUuEqvHbsMQU2V%2F7jEvsWIkWoZtEOecXGn0YZ6HgrLoSoQFQ4dK7SbEmH%2BCpwlSqh42%2Bxk7RqNTcsIsf5XaQGx%2BCUOjfmbIX%2BbyCHzsa5np2YV3sVk2Th%2FkDZSB8GPz7dpc%2FmaM3lTecD3nZgxZ8E9iwr8C33l0pMMNC6gb0GOqUB676tTcKGlXi1EZok49XX9K%2B28ndo33Din2qzyExq2ClptIXr%2F1a22064r1coQ9Ob8p00P7gacJnRT%2FpMdcS9Vc2paQ%2Fw2KSnC55%2Fvg5WqTD%2Fg8HWvzocCrmcLHxo7x2chwnq77f%2FZrqDIvCCj6HfQNjpgE%2F6zu4lL0XqdzA7Sfqn%2BowMqzvyBHaA3w8wD6bICT65DwfxG1hFGvIrd93hHASlxiqC&X-Amz-Signature=7bdb7fb329a4009ee75a8a525105a72f980fbc883d4872a8b912d5c451d61d81&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWXUVDXY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCILMpfztdwk58S5k6Y80ZA%2FSmmHhS6kXkWt5ebI5OyKAIgI8hmlBPP%2FEvCVa7vO0cOGRpEuUH8W5p4xIU6UYAoUX4qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrsBOirnADZlHzhWCrcAxYn0gOq%2BD3K295GgdhTobPZ1z%2FR4lYW2jNNQ2KQF7kzghm%2FHdIs%2FMKH508KXeBL79FSpWlm0o48pnvJI509b34KkTEuFCZS2htExJjxUcG8ajQ7W7fF%2FyCPldjCtwkbpe6oEGL58jhDSfPrLWn3fSRxJs%2B5v9uNm0EMibBhU5uy7Grnrl2AZkXNbRilFLEyaKazK%2BZXG8vUDPp8I%2B91otSdvWD4bCHyJ1Q47T8fbil%2FRDSUMLKvaYkN%2FtvrDWhiXoVITg2cmmRpqcNqpzH6FPTW9x9zmb%2FYU2FJgW1kTxVjZOd4McTPNUU5xBH6w8KL%2BKf%2BwNNbAr4kRVyrHeMaCLEbrJo%2FE6%2FK1%2FVDAx50UiKlQWLQTCdsxQ8HAkanOvBGStmBpaLL1%2BlrSInaK5zDYKAiQ8kFEX24mUnGtaN5VG795knekjTgjhalstinMGytS5tqrfSxEgQUMtU37QE2ZOzQaNMtUuEqvHbsMQU2V%2F7jEvsWIkWoZtEOecXGn0YZ6HgrLoSoQFQ4dK7SbEmH%2BCpwlSqh42%2Bxk7RqNTcsIsf5XaQGx%2BCUOjfmbIX%2BbyCHzsa5np2YV3sVk2Th%2FkDZSB8GPz7dpc%2FmaM3lTecD3nZgxZ8E9iwr8C33l0pMMNC6gb0GOqUB676tTcKGlXi1EZok49XX9K%2B28ndo33Din2qzyExq2ClptIXr%2F1a22064r1coQ9Ob8p00P7gacJnRT%2FpMdcS9Vc2paQ%2Fw2KSnC55%2Fvg5WqTD%2Fg8HWvzocCrmcLHxo7x2chwnq77f%2FZrqDIvCCj6HfQNjpgE%2F6zu4lL0XqdzA7Sfqn%2BowMqzvyBHaA3w8wD6bICT65DwfxG1hFGvIrd93hHASlxiqC&X-Amz-Signature=fa041dd20b30d212d518bf80b1b6205151d9626f0ce9924bbdff0ca9f99b6012&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWXUVDXY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCILMpfztdwk58S5k6Y80ZA%2FSmmHhS6kXkWt5ebI5OyKAIgI8hmlBPP%2FEvCVa7vO0cOGRpEuUH8W5p4xIU6UYAoUX4qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrsBOirnADZlHzhWCrcAxYn0gOq%2BD3K295GgdhTobPZ1z%2FR4lYW2jNNQ2KQF7kzghm%2FHdIs%2FMKH508KXeBL79FSpWlm0o48pnvJI509b34KkTEuFCZS2htExJjxUcG8ajQ7W7fF%2FyCPldjCtwkbpe6oEGL58jhDSfPrLWn3fSRxJs%2B5v9uNm0EMibBhU5uy7Grnrl2AZkXNbRilFLEyaKazK%2BZXG8vUDPp8I%2B91otSdvWD4bCHyJ1Q47T8fbil%2FRDSUMLKvaYkN%2FtvrDWhiXoVITg2cmmRpqcNqpzH6FPTW9x9zmb%2FYU2FJgW1kTxVjZOd4McTPNUU5xBH6w8KL%2BKf%2BwNNbAr4kRVyrHeMaCLEbrJo%2FE6%2FK1%2FVDAx50UiKlQWLQTCdsxQ8HAkanOvBGStmBpaLL1%2BlrSInaK5zDYKAiQ8kFEX24mUnGtaN5VG795knekjTgjhalstinMGytS5tqrfSxEgQUMtU37QE2ZOzQaNMtUuEqvHbsMQU2V%2F7jEvsWIkWoZtEOecXGn0YZ6HgrLoSoQFQ4dK7SbEmH%2BCpwlSqh42%2Bxk7RqNTcsIsf5XaQGx%2BCUOjfmbIX%2BbyCHzsa5np2YV3sVk2Th%2FkDZSB8GPz7dpc%2FmaM3lTecD3nZgxZ8E9iwr8C33l0pMMNC6gb0GOqUB676tTcKGlXi1EZok49XX9K%2B28ndo33Din2qzyExq2ClptIXr%2F1a22064r1coQ9Ob8p00P7gacJnRT%2FpMdcS9Vc2paQ%2Fw2KSnC55%2Fvg5WqTD%2Fg8HWvzocCrmcLHxo7x2chwnq77f%2FZrqDIvCCj6HfQNjpgE%2F6zu4lL0XqdzA7Sfqn%2BowMqzvyBHaA3w8wD6bICT65DwfxG1hFGvIrd93hHASlxiqC&X-Amz-Signature=b8c82df9f4068c10d35b22dde15966d2297f9331509999689df714de2e9145d1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWXUVDXY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCILMpfztdwk58S5k6Y80ZA%2FSmmHhS6kXkWt5ebI5OyKAIgI8hmlBPP%2FEvCVa7vO0cOGRpEuUH8W5p4xIU6UYAoUX4qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrsBOirnADZlHzhWCrcAxYn0gOq%2BD3K295GgdhTobPZ1z%2FR4lYW2jNNQ2KQF7kzghm%2FHdIs%2FMKH508KXeBL79FSpWlm0o48pnvJI509b34KkTEuFCZS2htExJjxUcG8ajQ7W7fF%2FyCPldjCtwkbpe6oEGL58jhDSfPrLWn3fSRxJs%2B5v9uNm0EMibBhU5uy7Grnrl2AZkXNbRilFLEyaKazK%2BZXG8vUDPp8I%2B91otSdvWD4bCHyJ1Q47T8fbil%2FRDSUMLKvaYkN%2FtvrDWhiXoVITg2cmmRpqcNqpzH6FPTW9x9zmb%2FYU2FJgW1kTxVjZOd4McTPNUU5xBH6w8KL%2BKf%2BwNNbAr4kRVyrHeMaCLEbrJo%2FE6%2FK1%2FVDAx50UiKlQWLQTCdsxQ8HAkanOvBGStmBpaLL1%2BlrSInaK5zDYKAiQ8kFEX24mUnGtaN5VG795knekjTgjhalstinMGytS5tqrfSxEgQUMtU37QE2ZOzQaNMtUuEqvHbsMQU2V%2F7jEvsWIkWoZtEOecXGn0YZ6HgrLoSoQFQ4dK7SbEmH%2BCpwlSqh42%2Bxk7RqNTcsIsf5XaQGx%2BCUOjfmbIX%2BbyCHzsa5np2YV3sVk2Th%2FkDZSB8GPz7dpc%2FmaM3lTecD3nZgxZ8E9iwr8C33l0pMMNC6gb0GOqUB676tTcKGlXi1EZok49XX9K%2B28ndo33Din2qzyExq2ClptIXr%2F1a22064r1coQ9Ob8p00P7gacJnRT%2FpMdcS9Vc2paQ%2Fw2KSnC55%2Fvg5WqTD%2Fg8HWvzocCrmcLHxo7x2chwnq77f%2FZrqDIvCCj6HfQNjpgE%2F6zu4lL0XqdzA7Sfqn%2BowMqzvyBHaA3w8wD6bICT65DwfxG1hFGvIrd93hHASlxiqC&X-Amz-Signature=13cc8d753e2069cc9008185be5b09cb0844f60f0ec97954213f2b67871628b6f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWXUVDXY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCILMpfztdwk58S5k6Y80ZA%2FSmmHhS6kXkWt5ebI5OyKAIgI8hmlBPP%2FEvCVa7vO0cOGRpEuUH8W5p4xIU6UYAoUX4qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrsBOirnADZlHzhWCrcAxYn0gOq%2BD3K295GgdhTobPZ1z%2FR4lYW2jNNQ2KQF7kzghm%2FHdIs%2FMKH508KXeBL79FSpWlm0o48pnvJI509b34KkTEuFCZS2htExJjxUcG8ajQ7W7fF%2FyCPldjCtwkbpe6oEGL58jhDSfPrLWn3fSRxJs%2B5v9uNm0EMibBhU5uy7Grnrl2AZkXNbRilFLEyaKazK%2BZXG8vUDPp8I%2B91otSdvWD4bCHyJ1Q47T8fbil%2FRDSUMLKvaYkN%2FtvrDWhiXoVITg2cmmRpqcNqpzH6FPTW9x9zmb%2FYU2FJgW1kTxVjZOd4McTPNUU5xBH6w8KL%2BKf%2BwNNbAr4kRVyrHeMaCLEbrJo%2FE6%2FK1%2FVDAx50UiKlQWLQTCdsxQ8HAkanOvBGStmBpaLL1%2BlrSInaK5zDYKAiQ8kFEX24mUnGtaN5VG795knekjTgjhalstinMGytS5tqrfSxEgQUMtU37QE2ZOzQaNMtUuEqvHbsMQU2V%2F7jEvsWIkWoZtEOecXGn0YZ6HgrLoSoQFQ4dK7SbEmH%2BCpwlSqh42%2Bxk7RqNTcsIsf5XaQGx%2BCUOjfmbIX%2BbyCHzsa5np2YV3sVk2Th%2FkDZSB8GPz7dpc%2FmaM3lTecD3nZgxZ8E9iwr8C33l0pMMNC6gb0GOqUB676tTcKGlXi1EZok49XX9K%2B28ndo33Din2qzyExq2ClptIXr%2F1a22064r1coQ9Ob8p00P7gacJnRT%2FpMdcS9Vc2paQ%2Fw2KSnC55%2Fvg5WqTD%2Fg8HWvzocCrmcLHxo7x2chwnq77f%2FZrqDIvCCj6HfQNjpgE%2F6zu4lL0XqdzA7Sfqn%2BowMqzvyBHaA3w8wD6bICT65DwfxG1hFGvIrd93hHASlxiqC&X-Amz-Signature=91025dfe436d063c27737131889bb4f0a9ee9267a835194c83aadd2933e118ab&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWXUVDXY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCILMpfztdwk58S5k6Y80ZA%2FSmmHhS6kXkWt5ebI5OyKAIgI8hmlBPP%2FEvCVa7vO0cOGRpEuUH8W5p4xIU6UYAoUX4qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrsBOirnADZlHzhWCrcAxYn0gOq%2BD3K295GgdhTobPZ1z%2FR4lYW2jNNQ2KQF7kzghm%2FHdIs%2FMKH508KXeBL79FSpWlm0o48pnvJI509b34KkTEuFCZS2htExJjxUcG8ajQ7W7fF%2FyCPldjCtwkbpe6oEGL58jhDSfPrLWn3fSRxJs%2B5v9uNm0EMibBhU5uy7Grnrl2AZkXNbRilFLEyaKazK%2BZXG8vUDPp8I%2B91otSdvWD4bCHyJ1Q47T8fbil%2FRDSUMLKvaYkN%2FtvrDWhiXoVITg2cmmRpqcNqpzH6FPTW9x9zmb%2FYU2FJgW1kTxVjZOd4McTPNUU5xBH6w8KL%2BKf%2BwNNbAr4kRVyrHeMaCLEbrJo%2FE6%2FK1%2FVDAx50UiKlQWLQTCdsxQ8HAkanOvBGStmBpaLL1%2BlrSInaK5zDYKAiQ8kFEX24mUnGtaN5VG795knekjTgjhalstinMGytS5tqrfSxEgQUMtU37QE2ZOzQaNMtUuEqvHbsMQU2V%2F7jEvsWIkWoZtEOecXGn0YZ6HgrLoSoQFQ4dK7SbEmH%2BCpwlSqh42%2Bxk7RqNTcsIsf5XaQGx%2BCUOjfmbIX%2BbyCHzsa5np2YV3sVk2Th%2FkDZSB8GPz7dpc%2FmaM3lTecD3nZgxZ8E9iwr8C33l0pMMNC6gb0GOqUB676tTcKGlXi1EZok49XX9K%2B28ndo33Din2qzyExq2ClptIXr%2F1a22064r1coQ9Ob8p00P7gacJnRT%2FpMdcS9Vc2paQ%2Fw2KSnC55%2Fvg5WqTD%2Fg8HWvzocCrmcLHxo7x2chwnq77f%2FZrqDIvCCj6HfQNjpgE%2F6zu4lL0XqdzA7Sfqn%2BowMqzvyBHaA3w8wD6bICT65DwfxG1hFGvIrd93hHASlxiqC&X-Amz-Signature=1ed529b77618f05ff349334a1a942fda22394956bbbd1567eb3f3e319cd9b87c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWXUVDXY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCILMpfztdwk58S5k6Y80ZA%2FSmmHhS6kXkWt5ebI5OyKAIgI8hmlBPP%2FEvCVa7vO0cOGRpEuUH8W5p4xIU6UYAoUX4qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrsBOirnADZlHzhWCrcAxYn0gOq%2BD3K295GgdhTobPZ1z%2FR4lYW2jNNQ2KQF7kzghm%2FHdIs%2FMKH508KXeBL79FSpWlm0o48pnvJI509b34KkTEuFCZS2htExJjxUcG8ajQ7W7fF%2FyCPldjCtwkbpe6oEGL58jhDSfPrLWn3fSRxJs%2B5v9uNm0EMibBhU5uy7Grnrl2AZkXNbRilFLEyaKazK%2BZXG8vUDPp8I%2B91otSdvWD4bCHyJ1Q47T8fbil%2FRDSUMLKvaYkN%2FtvrDWhiXoVITg2cmmRpqcNqpzH6FPTW9x9zmb%2FYU2FJgW1kTxVjZOd4McTPNUU5xBH6w8KL%2BKf%2BwNNbAr4kRVyrHeMaCLEbrJo%2FE6%2FK1%2FVDAx50UiKlQWLQTCdsxQ8HAkanOvBGStmBpaLL1%2BlrSInaK5zDYKAiQ8kFEX24mUnGtaN5VG795knekjTgjhalstinMGytS5tqrfSxEgQUMtU37QE2ZOzQaNMtUuEqvHbsMQU2V%2F7jEvsWIkWoZtEOecXGn0YZ6HgrLoSoQFQ4dK7SbEmH%2BCpwlSqh42%2Bxk7RqNTcsIsf5XaQGx%2BCUOjfmbIX%2BbyCHzsa5np2YV3sVk2Th%2FkDZSB8GPz7dpc%2FmaM3lTecD3nZgxZ8E9iwr8C33l0pMMNC6gb0GOqUB676tTcKGlXi1EZok49XX9K%2B28ndo33Din2qzyExq2ClptIXr%2F1a22064r1coQ9Ob8p00P7gacJnRT%2FpMdcS9Vc2paQ%2Fw2KSnC55%2Fvg5WqTD%2Fg8HWvzocCrmcLHxo7x2chwnq77f%2FZrqDIvCCj6HfQNjpgE%2F6zu4lL0XqdzA7Sfqn%2BowMqzvyBHaA3w8wD6bICT65DwfxG1hFGvIrd93hHASlxiqC&X-Amz-Signature=0ed3dd110e365d3104b4a4313ec7d58bdf9e3aca3a1212e3b930f1c86ecbc594&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWXUVDXY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCILMpfztdwk58S5k6Y80ZA%2FSmmHhS6kXkWt5ebI5OyKAIgI8hmlBPP%2FEvCVa7vO0cOGRpEuUH8W5p4xIU6UYAoUX4qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrsBOirnADZlHzhWCrcAxYn0gOq%2BD3K295GgdhTobPZ1z%2FR4lYW2jNNQ2KQF7kzghm%2FHdIs%2FMKH508KXeBL79FSpWlm0o48pnvJI509b34KkTEuFCZS2htExJjxUcG8ajQ7W7fF%2FyCPldjCtwkbpe6oEGL58jhDSfPrLWn3fSRxJs%2B5v9uNm0EMibBhU5uy7Grnrl2AZkXNbRilFLEyaKazK%2BZXG8vUDPp8I%2B91otSdvWD4bCHyJ1Q47T8fbil%2FRDSUMLKvaYkN%2FtvrDWhiXoVITg2cmmRpqcNqpzH6FPTW9x9zmb%2FYU2FJgW1kTxVjZOd4McTPNUU5xBH6w8KL%2BKf%2BwNNbAr4kRVyrHeMaCLEbrJo%2FE6%2FK1%2FVDAx50UiKlQWLQTCdsxQ8HAkanOvBGStmBpaLL1%2BlrSInaK5zDYKAiQ8kFEX24mUnGtaN5VG795knekjTgjhalstinMGytS5tqrfSxEgQUMtU37QE2ZOzQaNMtUuEqvHbsMQU2V%2F7jEvsWIkWoZtEOecXGn0YZ6HgrLoSoQFQ4dK7SbEmH%2BCpwlSqh42%2Bxk7RqNTcsIsf5XaQGx%2BCUOjfmbIX%2BbyCHzsa5np2YV3sVk2Th%2FkDZSB8GPz7dpc%2FmaM3lTecD3nZgxZ8E9iwr8C33l0pMMNC6gb0GOqUB676tTcKGlXi1EZok49XX9K%2B28ndo33Din2qzyExq2ClptIXr%2F1a22064r1coQ9Ob8p00P7gacJnRT%2FpMdcS9Vc2paQ%2Fw2KSnC55%2Fvg5WqTD%2Fg8HWvzocCrmcLHxo7x2chwnq77f%2FZrqDIvCCj6HfQNjpgE%2F6zu4lL0XqdzA7Sfqn%2BowMqzvyBHaA3w8wD6bICT65DwfxG1hFGvIrd93hHASlxiqC&X-Amz-Signature=8df394e718822603303d795177651982dd42eb7261c2daf2aa7d8205fafaa222&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWXUVDXY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCILMpfztdwk58S5k6Y80ZA%2FSmmHhS6kXkWt5ebI5OyKAIgI8hmlBPP%2FEvCVa7vO0cOGRpEuUH8W5p4xIU6UYAoUX4qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrsBOirnADZlHzhWCrcAxYn0gOq%2BD3K295GgdhTobPZ1z%2FR4lYW2jNNQ2KQF7kzghm%2FHdIs%2FMKH508KXeBL79FSpWlm0o48pnvJI509b34KkTEuFCZS2htExJjxUcG8ajQ7W7fF%2FyCPldjCtwkbpe6oEGL58jhDSfPrLWn3fSRxJs%2B5v9uNm0EMibBhU5uy7Grnrl2AZkXNbRilFLEyaKazK%2BZXG8vUDPp8I%2B91otSdvWD4bCHyJ1Q47T8fbil%2FRDSUMLKvaYkN%2FtvrDWhiXoVITg2cmmRpqcNqpzH6FPTW9x9zmb%2FYU2FJgW1kTxVjZOd4McTPNUU5xBH6w8KL%2BKf%2BwNNbAr4kRVyrHeMaCLEbrJo%2FE6%2FK1%2FVDAx50UiKlQWLQTCdsxQ8HAkanOvBGStmBpaLL1%2BlrSInaK5zDYKAiQ8kFEX24mUnGtaN5VG795knekjTgjhalstinMGytS5tqrfSxEgQUMtU37QE2ZOzQaNMtUuEqvHbsMQU2V%2F7jEvsWIkWoZtEOecXGn0YZ6HgrLoSoQFQ4dK7SbEmH%2BCpwlSqh42%2Bxk7RqNTcsIsf5XaQGx%2BCUOjfmbIX%2BbyCHzsa5np2YV3sVk2Th%2FkDZSB8GPz7dpc%2FmaM3lTecD3nZgxZ8E9iwr8C33l0pMMNC6gb0GOqUB676tTcKGlXi1EZok49XX9K%2B28ndo33Din2qzyExq2ClptIXr%2F1a22064r1coQ9Ob8p00P7gacJnRT%2FpMdcS9Vc2paQ%2Fw2KSnC55%2Fvg5WqTD%2Fg8HWvzocCrmcLHxo7x2chwnq77f%2FZrqDIvCCj6HfQNjpgE%2F6zu4lL0XqdzA7Sfqn%2BowMqzvyBHaA3w8wD6bICT65DwfxG1hFGvIrd93hHASlxiqC&X-Amz-Signature=7b66f85b586d44d3e08d71bcb820eff6ad3ccf3b8b4bb387d271626b2aec3270&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CIT2S2A%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGzE2aRaQ7Jnt%2FpszuYXHocWLnIvmXgy6u2mTBUAXyRTAiAWNKTdbcivWjSauQlOkuFYZwF0ipWdF1U9%2BJw5%2BDnreiqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbgrUVRHRU7verIvIKtwDWxnj%2F68PQzooOwUItcyt8xfvVD2KNkfX415hNqTAdimi5lyZqg5%2B30Vx8YY8w%2Bp1rHZk%2B5saw%2BJ2kHxYPLVdvawAz%2Bnwx%2BPcFHf%2FZHBPS2jXrbAgjVrbsKALqJY73DDxh5cOyacuDRueSJuYDrsCd%2BOr0sTE3jXp6zP73FmSqcfxJj7MUa9%2FXN%2F5%2Fn2NZ3hdZnoyi5sRxdmUsC138HBczkdXZjfxsxnTJCPVLoGV3iC%2F0Q2LNsUUwoSTBkLcMf8DpwR36whrkPJakAycMnbqjAmM8hT%2BWlMkCQ13hJBTu%2F6ign3OBPv6W7DTyquBxtqQgaksTiZVLHGLwNdnGhjHHHCOJNjEKPQjJCLGCxmMyRJkWwMzE%2FRWtwOsWYxjU8LIOLYfRkdUNN%2B%2BNGixRbnZJWzInaNOrTdjdB7GuCmBkRlo24hV6nazZBC%2Bf5e6PmQ%2BRpABUUp7%2FOAbE9fEQkqG1fdIuo5Qoqi9qR9Y3KGuzhkETxj9vihPH9mp77AvO6PixYpdXCa%2BCsiaRPAdheixHfg%2FRQ1Tvsoy0SPwIyXoVUUg9Z6iIgfmCWgZLOkGlVcj%2BPYQPcK2%2FTxPyuwadzIvVKF9%2BsrpATtirwT%2FYA0Qt5yqHjhVozBVqpPq7rgw3bmBvQY6pgECbBxWjGJaOFIn9XeNUAKskPmiKzneDd41ABu2T5JnxsLerCPOAgwJnpXSlA0VdTRRbYBJrBOzT%2FE33yBVnRkcGPOVwiqSgZmoHI5Nz4kQwLOvcWfI66q1ABfZeGekz8UXxGEUjzyZRzb3API6N3QUFdjEb%2BvVwqCLgWUP1IvUfnalOdeJZDqnwxOXz8c7fONq%2F%2BeGNWdOjyYjZrZBq9Gl%2FYg0AsTd&X-Amz-Signature=7e56f11be9353fdd95cf27bf2b9b3c7e7f470c6de77b40da1a13db8657827c4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CIT2S2A%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGzE2aRaQ7Jnt%2FpszuYXHocWLnIvmXgy6u2mTBUAXyRTAiAWNKTdbcivWjSauQlOkuFYZwF0ipWdF1U9%2BJw5%2BDnreiqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbgrUVRHRU7verIvIKtwDWxnj%2F68PQzooOwUItcyt8xfvVD2KNkfX415hNqTAdimi5lyZqg5%2B30Vx8YY8w%2Bp1rHZk%2B5saw%2BJ2kHxYPLVdvawAz%2Bnwx%2BPcFHf%2FZHBPS2jXrbAgjVrbsKALqJY73DDxh5cOyacuDRueSJuYDrsCd%2BOr0sTE3jXp6zP73FmSqcfxJj7MUa9%2FXN%2F5%2Fn2NZ3hdZnoyi5sRxdmUsC138HBczkdXZjfxsxnTJCPVLoGV3iC%2F0Q2LNsUUwoSTBkLcMf8DpwR36whrkPJakAycMnbqjAmM8hT%2BWlMkCQ13hJBTu%2F6ign3OBPv6W7DTyquBxtqQgaksTiZVLHGLwNdnGhjHHHCOJNjEKPQjJCLGCxmMyRJkWwMzE%2FRWtwOsWYxjU8LIOLYfRkdUNN%2B%2BNGixRbnZJWzInaNOrTdjdB7GuCmBkRlo24hV6nazZBC%2Bf5e6PmQ%2BRpABUUp7%2FOAbE9fEQkqG1fdIuo5Qoqi9qR9Y3KGuzhkETxj9vihPH9mp77AvO6PixYpdXCa%2BCsiaRPAdheixHfg%2FRQ1Tvsoy0SPwIyXoVUUg9Z6iIgfmCWgZLOkGlVcj%2BPYQPcK2%2FTxPyuwadzIvVKF9%2BsrpATtirwT%2FYA0Qt5yqHjhVozBVqpPq7rgw3bmBvQY6pgECbBxWjGJaOFIn9XeNUAKskPmiKzneDd41ABu2T5JnxsLerCPOAgwJnpXSlA0VdTRRbYBJrBOzT%2FE33yBVnRkcGPOVwiqSgZmoHI5Nz4kQwLOvcWfI66q1ABfZeGekz8UXxGEUjzyZRzb3API6N3QUFdjEb%2BvVwqCLgWUP1IvUfnalOdeJZDqnwxOXz8c7fONq%2F%2BeGNWdOjyYjZrZBq9Gl%2FYg0AsTd&X-Amz-Signature=b50f4d57f353b6a79585dab7fb8b53bfb8387878dda6b07e274240a6935b2b7b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
