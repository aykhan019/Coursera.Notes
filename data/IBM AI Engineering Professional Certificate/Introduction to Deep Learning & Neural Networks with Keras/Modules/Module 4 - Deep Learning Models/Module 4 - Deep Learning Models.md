

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRUYJWF2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCUfJJKi5hs%2FtcAHinbLmUIgnU8l78UgQy12MCiGadeWwIgQCT7uDpLzQ%2B%2BDxhfNfRxD0i8M8lgMgx9TMn71iz8Ifsq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDE8umWr9MaRp4GFk3CrcAwoUZduWz8Ls0XVV3X4Btugb7wflWdjq1MaxQiqV0juT%2F1Xs1G4OKQv%2FCvks4Cntu0wR%2BdWuXxDqfsBQ3FjqfOaiQkfDKYuNXEwPKqvmLCPxYtzKS%2BSXRxXdn7ex9lwTydAURu%2B%2FCWovl4rF4DZP%2FK7GilJR4DU3vid%2FWs%2FbJFN%2F%2FJc7OSn5jF4Hq8PJZpwo%2B5JSUdWAUK6mYvK8y4QGKvpb4DwlRZ9nDo%2FFuW2F%2Byo5%2BdQ30LE6kEnVxVt1Zu595Q8ZyVJ%2BRixLXfKJH5mLKDlMvKRjIYeL80m4JDARyg%2BKx2p7RmpMdUdc3rB%2ByFV5eyPOzOKgwmsvF2Sn877iQQbGyawl8HL19pikvtW8eyIGlfgZPQazqWAkk92AaXamhgPoxdPI8orApbhlgMUjSH6IhujUy9NNJvye87kVJu3mJNMOfe26OsE52uCfO4K585QQBGQno2iuCrAP7bnGaITziSYRbtZnOiBnhd0HJVfNwd2WjwXzJyAB9u%2BoiV2iy3ONBETFl7MOXMrdxwx7pNXNYk3MpfuZCSnb3oBHLXIuTaZaToQ3EnEtxrvHJc6Ujc1eGq7nMnfvkGuUZcuBTQ%2FPv5HwydTeymzkoycc4A6xCdpJ%2BWBTLrncgRDIMLK4lL0GOqUBIA2xMwO8t4ZWc7SSa1hXrYbAI5gQtK9Ts6RUjUmO%2Fk0qkEPO6iqcE1ZylPZXbQ0bFHFzC%2FGhX9ElZb3QxHXPS7PVli1IlsALSC4GPH3hFqW2h90cuigLttlOJINAqEb%2FDGiRIbLSydD949%2FSh5RzDCHMUUVPk8D5D%2FZ2Il0xeByzF5B49HmmwmgB%2F06NcRz537oMARdfOF%2BbPuSM0RnZCXjtRiN8&X-Amz-Signature=1c8306115b0737c5ef60e0cb505264834e85c6835e34dd8923cd04869b5a781c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRUYJWF2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCUfJJKi5hs%2FtcAHinbLmUIgnU8l78UgQy12MCiGadeWwIgQCT7uDpLzQ%2B%2BDxhfNfRxD0i8M8lgMgx9TMn71iz8Ifsq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDE8umWr9MaRp4GFk3CrcAwoUZduWz8Ls0XVV3X4Btugb7wflWdjq1MaxQiqV0juT%2F1Xs1G4OKQv%2FCvks4Cntu0wR%2BdWuXxDqfsBQ3FjqfOaiQkfDKYuNXEwPKqvmLCPxYtzKS%2BSXRxXdn7ex9lwTydAURu%2B%2FCWovl4rF4DZP%2FK7GilJR4DU3vid%2FWs%2FbJFN%2F%2FJc7OSn5jF4Hq8PJZpwo%2B5JSUdWAUK6mYvK8y4QGKvpb4DwlRZ9nDo%2FFuW2F%2Byo5%2BdQ30LE6kEnVxVt1Zu595Q8ZyVJ%2BRixLXfKJH5mLKDlMvKRjIYeL80m4JDARyg%2BKx2p7RmpMdUdc3rB%2ByFV5eyPOzOKgwmsvF2Sn877iQQbGyawl8HL19pikvtW8eyIGlfgZPQazqWAkk92AaXamhgPoxdPI8orApbhlgMUjSH6IhujUy9NNJvye87kVJu3mJNMOfe26OsE52uCfO4K585QQBGQno2iuCrAP7bnGaITziSYRbtZnOiBnhd0HJVfNwd2WjwXzJyAB9u%2BoiV2iy3ONBETFl7MOXMrdxwx7pNXNYk3MpfuZCSnb3oBHLXIuTaZaToQ3EnEtxrvHJc6Ujc1eGq7nMnfvkGuUZcuBTQ%2FPv5HwydTeymzkoycc4A6xCdpJ%2BWBTLrncgRDIMLK4lL0GOqUBIA2xMwO8t4ZWc7SSa1hXrYbAI5gQtK9Ts6RUjUmO%2Fk0qkEPO6iqcE1ZylPZXbQ0bFHFzC%2FGhX9ElZb3QxHXPS7PVli1IlsALSC4GPH3hFqW2h90cuigLttlOJINAqEb%2FDGiRIbLSydD949%2FSh5RzDCHMUUVPk8D5D%2FZ2Il0xeByzF5B49HmmwmgB%2F06NcRz537oMARdfOF%2BbPuSM0RnZCXjtRiN8&X-Amz-Signature=e47f8ed0c40c91506b59e6d99c0505cfceddc4dcf726f7831f30ef0b19e49b13&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRUYJWF2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCUfJJKi5hs%2FtcAHinbLmUIgnU8l78UgQy12MCiGadeWwIgQCT7uDpLzQ%2B%2BDxhfNfRxD0i8M8lgMgx9TMn71iz8Ifsq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDE8umWr9MaRp4GFk3CrcAwoUZduWz8Ls0XVV3X4Btugb7wflWdjq1MaxQiqV0juT%2F1Xs1G4OKQv%2FCvks4Cntu0wR%2BdWuXxDqfsBQ3FjqfOaiQkfDKYuNXEwPKqvmLCPxYtzKS%2BSXRxXdn7ex9lwTydAURu%2B%2FCWovl4rF4DZP%2FK7GilJR4DU3vid%2FWs%2FbJFN%2F%2FJc7OSn5jF4Hq8PJZpwo%2B5JSUdWAUK6mYvK8y4QGKvpb4DwlRZ9nDo%2FFuW2F%2Byo5%2BdQ30LE6kEnVxVt1Zu595Q8ZyVJ%2BRixLXfKJH5mLKDlMvKRjIYeL80m4JDARyg%2BKx2p7RmpMdUdc3rB%2ByFV5eyPOzOKgwmsvF2Sn877iQQbGyawl8HL19pikvtW8eyIGlfgZPQazqWAkk92AaXamhgPoxdPI8orApbhlgMUjSH6IhujUy9NNJvye87kVJu3mJNMOfe26OsE52uCfO4K585QQBGQno2iuCrAP7bnGaITziSYRbtZnOiBnhd0HJVfNwd2WjwXzJyAB9u%2BoiV2iy3ONBETFl7MOXMrdxwx7pNXNYk3MpfuZCSnb3oBHLXIuTaZaToQ3EnEtxrvHJc6Ujc1eGq7nMnfvkGuUZcuBTQ%2FPv5HwydTeymzkoycc4A6xCdpJ%2BWBTLrncgRDIMLK4lL0GOqUBIA2xMwO8t4ZWc7SSa1hXrYbAI5gQtK9Ts6RUjUmO%2Fk0qkEPO6iqcE1ZylPZXbQ0bFHFzC%2FGhX9ElZb3QxHXPS7PVli1IlsALSC4GPH3hFqW2h90cuigLttlOJINAqEb%2FDGiRIbLSydD949%2FSh5RzDCHMUUVPk8D5D%2FZ2Il0xeByzF5B49HmmwmgB%2F06NcRz537oMARdfOF%2BbPuSM0RnZCXjtRiN8&X-Amz-Signature=971d46792cb7ab01b9bc0dd2ca4275f5a7079146cc31454ae22d2cb76ba606ce&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRUYJWF2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCUfJJKi5hs%2FtcAHinbLmUIgnU8l78UgQy12MCiGadeWwIgQCT7uDpLzQ%2B%2BDxhfNfRxD0i8M8lgMgx9TMn71iz8Ifsq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDE8umWr9MaRp4GFk3CrcAwoUZduWz8Ls0XVV3X4Btugb7wflWdjq1MaxQiqV0juT%2F1Xs1G4OKQv%2FCvks4Cntu0wR%2BdWuXxDqfsBQ3FjqfOaiQkfDKYuNXEwPKqvmLCPxYtzKS%2BSXRxXdn7ex9lwTydAURu%2B%2FCWovl4rF4DZP%2FK7GilJR4DU3vid%2FWs%2FbJFN%2F%2FJc7OSn5jF4Hq8PJZpwo%2B5JSUdWAUK6mYvK8y4QGKvpb4DwlRZ9nDo%2FFuW2F%2Byo5%2BdQ30LE6kEnVxVt1Zu595Q8ZyVJ%2BRixLXfKJH5mLKDlMvKRjIYeL80m4JDARyg%2BKx2p7RmpMdUdc3rB%2ByFV5eyPOzOKgwmsvF2Sn877iQQbGyawl8HL19pikvtW8eyIGlfgZPQazqWAkk92AaXamhgPoxdPI8orApbhlgMUjSH6IhujUy9NNJvye87kVJu3mJNMOfe26OsE52uCfO4K585QQBGQno2iuCrAP7bnGaITziSYRbtZnOiBnhd0HJVfNwd2WjwXzJyAB9u%2BoiV2iy3ONBETFl7MOXMrdxwx7pNXNYk3MpfuZCSnb3oBHLXIuTaZaToQ3EnEtxrvHJc6Ujc1eGq7nMnfvkGuUZcuBTQ%2FPv5HwydTeymzkoycc4A6xCdpJ%2BWBTLrncgRDIMLK4lL0GOqUBIA2xMwO8t4ZWc7SSa1hXrYbAI5gQtK9Ts6RUjUmO%2Fk0qkEPO6iqcE1ZylPZXbQ0bFHFzC%2FGhX9ElZb3QxHXPS7PVli1IlsALSC4GPH3hFqW2h90cuigLttlOJINAqEb%2FDGiRIbLSydD949%2FSh5RzDCHMUUVPk8D5D%2FZ2Il0xeByzF5B49HmmwmgB%2F06NcRz537oMARdfOF%2BbPuSM0RnZCXjtRiN8&X-Amz-Signature=82cc9086a53cbd34612c9e1f02b80bba3bbc5b5f5111e0a9b6c6770376c270ca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRUYJWF2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCUfJJKi5hs%2FtcAHinbLmUIgnU8l78UgQy12MCiGadeWwIgQCT7uDpLzQ%2B%2BDxhfNfRxD0i8M8lgMgx9TMn71iz8Ifsq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDE8umWr9MaRp4GFk3CrcAwoUZduWz8Ls0XVV3X4Btugb7wflWdjq1MaxQiqV0juT%2F1Xs1G4OKQv%2FCvks4Cntu0wR%2BdWuXxDqfsBQ3FjqfOaiQkfDKYuNXEwPKqvmLCPxYtzKS%2BSXRxXdn7ex9lwTydAURu%2B%2FCWovl4rF4DZP%2FK7GilJR4DU3vid%2FWs%2FbJFN%2F%2FJc7OSn5jF4Hq8PJZpwo%2B5JSUdWAUK6mYvK8y4QGKvpb4DwlRZ9nDo%2FFuW2F%2Byo5%2BdQ30LE6kEnVxVt1Zu595Q8ZyVJ%2BRixLXfKJH5mLKDlMvKRjIYeL80m4JDARyg%2BKx2p7RmpMdUdc3rB%2ByFV5eyPOzOKgwmsvF2Sn877iQQbGyawl8HL19pikvtW8eyIGlfgZPQazqWAkk92AaXamhgPoxdPI8orApbhlgMUjSH6IhujUy9NNJvye87kVJu3mJNMOfe26OsE52uCfO4K585QQBGQno2iuCrAP7bnGaITziSYRbtZnOiBnhd0HJVfNwd2WjwXzJyAB9u%2BoiV2iy3ONBETFl7MOXMrdxwx7pNXNYk3MpfuZCSnb3oBHLXIuTaZaToQ3EnEtxrvHJc6Ujc1eGq7nMnfvkGuUZcuBTQ%2FPv5HwydTeymzkoycc4A6xCdpJ%2BWBTLrncgRDIMLK4lL0GOqUBIA2xMwO8t4ZWc7SSa1hXrYbAI5gQtK9Ts6RUjUmO%2Fk0qkEPO6iqcE1ZylPZXbQ0bFHFzC%2FGhX9ElZb3QxHXPS7PVli1IlsALSC4GPH3hFqW2h90cuigLttlOJINAqEb%2FDGiRIbLSydD949%2FSh5RzDCHMUUVPk8D5D%2FZ2Il0xeByzF5B49HmmwmgB%2F06NcRz537oMARdfOF%2BbPuSM0RnZCXjtRiN8&X-Amz-Signature=81542117e6caa9a5d86aa015f7204594994b6ee440e232e5c4d8bc97a4b6df12&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRUYJWF2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCUfJJKi5hs%2FtcAHinbLmUIgnU8l78UgQy12MCiGadeWwIgQCT7uDpLzQ%2B%2BDxhfNfRxD0i8M8lgMgx9TMn71iz8Ifsq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDE8umWr9MaRp4GFk3CrcAwoUZduWz8Ls0XVV3X4Btugb7wflWdjq1MaxQiqV0juT%2F1Xs1G4OKQv%2FCvks4Cntu0wR%2BdWuXxDqfsBQ3FjqfOaiQkfDKYuNXEwPKqvmLCPxYtzKS%2BSXRxXdn7ex9lwTydAURu%2B%2FCWovl4rF4DZP%2FK7GilJR4DU3vid%2FWs%2FbJFN%2F%2FJc7OSn5jF4Hq8PJZpwo%2B5JSUdWAUK6mYvK8y4QGKvpb4DwlRZ9nDo%2FFuW2F%2Byo5%2BdQ30LE6kEnVxVt1Zu595Q8ZyVJ%2BRixLXfKJH5mLKDlMvKRjIYeL80m4JDARyg%2BKx2p7RmpMdUdc3rB%2ByFV5eyPOzOKgwmsvF2Sn877iQQbGyawl8HL19pikvtW8eyIGlfgZPQazqWAkk92AaXamhgPoxdPI8orApbhlgMUjSH6IhujUy9NNJvye87kVJu3mJNMOfe26OsE52uCfO4K585QQBGQno2iuCrAP7bnGaITziSYRbtZnOiBnhd0HJVfNwd2WjwXzJyAB9u%2BoiV2iy3ONBETFl7MOXMrdxwx7pNXNYk3MpfuZCSnb3oBHLXIuTaZaToQ3EnEtxrvHJc6Ujc1eGq7nMnfvkGuUZcuBTQ%2FPv5HwydTeymzkoycc4A6xCdpJ%2BWBTLrncgRDIMLK4lL0GOqUBIA2xMwO8t4ZWc7SSa1hXrYbAI5gQtK9Ts6RUjUmO%2Fk0qkEPO6iqcE1ZylPZXbQ0bFHFzC%2FGhX9ElZb3QxHXPS7PVli1IlsALSC4GPH3hFqW2h90cuigLttlOJINAqEb%2FDGiRIbLSydD949%2FSh5RzDCHMUUVPk8D5D%2FZ2Il0xeByzF5B49HmmwmgB%2F06NcRz537oMARdfOF%2BbPuSM0RnZCXjtRiN8&X-Amz-Signature=685ebc168ba2ce1c416c0ea3fa9cd5e520586a3256d81097d693e8fb133d337d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRUYJWF2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCUfJJKi5hs%2FtcAHinbLmUIgnU8l78UgQy12MCiGadeWwIgQCT7uDpLzQ%2B%2BDxhfNfRxD0i8M8lgMgx9TMn71iz8Ifsq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDE8umWr9MaRp4GFk3CrcAwoUZduWz8Ls0XVV3X4Btugb7wflWdjq1MaxQiqV0juT%2F1Xs1G4OKQv%2FCvks4Cntu0wR%2BdWuXxDqfsBQ3FjqfOaiQkfDKYuNXEwPKqvmLCPxYtzKS%2BSXRxXdn7ex9lwTydAURu%2B%2FCWovl4rF4DZP%2FK7GilJR4DU3vid%2FWs%2FbJFN%2F%2FJc7OSn5jF4Hq8PJZpwo%2B5JSUdWAUK6mYvK8y4QGKvpb4DwlRZ9nDo%2FFuW2F%2Byo5%2BdQ30LE6kEnVxVt1Zu595Q8ZyVJ%2BRixLXfKJH5mLKDlMvKRjIYeL80m4JDARyg%2BKx2p7RmpMdUdc3rB%2ByFV5eyPOzOKgwmsvF2Sn877iQQbGyawl8HL19pikvtW8eyIGlfgZPQazqWAkk92AaXamhgPoxdPI8orApbhlgMUjSH6IhujUy9NNJvye87kVJu3mJNMOfe26OsE52uCfO4K585QQBGQno2iuCrAP7bnGaITziSYRbtZnOiBnhd0HJVfNwd2WjwXzJyAB9u%2BoiV2iy3ONBETFl7MOXMrdxwx7pNXNYk3MpfuZCSnb3oBHLXIuTaZaToQ3EnEtxrvHJc6Ujc1eGq7nMnfvkGuUZcuBTQ%2FPv5HwydTeymzkoycc4A6xCdpJ%2BWBTLrncgRDIMLK4lL0GOqUBIA2xMwO8t4ZWc7SSa1hXrYbAI5gQtK9Ts6RUjUmO%2Fk0qkEPO6iqcE1ZylPZXbQ0bFHFzC%2FGhX9ElZb3QxHXPS7PVli1IlsALSC4GPH3hFqW2h90cuigLttlOJINAqEb%2FDGiRIbLSydD949%2FSh5RzDCHMUUVPk8D5D%2FZ2Il0xeByzF5B49HmmwmgB%2F06NcRz537oMARdfOF%2BbPuSM0RnZCXjtRiN8&X-Amz-Signature=1db798108d0d68bd9a19124111a3c66c8b627a316b0520e51391473b01773924&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRUYJWF2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCUfJJKi5hs%2FtcAHinbLmUIgnU8l78UgQy12MCiGadeWwIgQCT7uDpLzQ%2B%2BDxhfNfRxD0i8M8lgMgx9TMn71iz8Ifsq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDE8umWr9MaRp4GFk3CrcAwoUZduWz8Ls0XVV3X4Btugb7wflWdjq1MaxQiqV0juT%2F1Xs1G4OKQv%2FCvks4Cntu0wR%2BdWuXxDqfsBQ3FjqfOaiQkfDKYuNXEwPKqvmLCPxYtzKS%2BSXRxXdn7ex9lwTydAURu%2B%2FCWovl4rF4DZP%2FK7GilJR4DU3vid%2FWs%2FbJFN%2F%2FJc7OSn5jF4Hq8PJZpwo%2B5JSUdWAUK6mYvK8y4QGKvpb4DwlRZ9nDo%2FFuW2F%2Byo5%2BdQ30LE6kEnVxVt1Zu595Q8ZyVJ%2BRixLXfKJH5mLKDlMvKRjIYeL80m4JDARyg%2BKx2p7RmpMdUdc3rB%2ByFV5eyPOzOKgwmsvF2Sn877iQQbGyawl8HL19pikvtW8eyIGlfgZPQazqWAkk92AaXamhgPoxdPI8orApbhlgMUjSH6IhujUy9NNJvye87kVJu3mJNMOfe26OsE52uCfO4K585QQBGQno2iuCrAP7bnGaITziSYRbtZnOiBnhd0HJVfNwd2WjwXzJyAB9u%2BoiV2iy3ONBETFl7MOXMrdxwx7pNXNYk3MpfuZCSnb3oBHLXIuTaZaToQ3EnEtxrvHJc6Ujc1eGq7nMnfvkGuUZcuBTQ%2FPv5HwydTeymzkoycc4A6xCdpJ%2BWBTLrncgRDIMLK4lL0GOqUBIA2xMwO8t4ZWc7SSa1hXrYbAI5gQtK9Ts6RUjUmO%2Fk0qkEPO6iqcE1ZylPZXbQ0bFHFzC%2FGhX9ElZb3QxHXPS7PVli1IlsALSC4GPH3hFqW2h90cuigLttlOJINAqEb%2FDGiRIbLSydD949%2FSh5RzDCHMUUVPk8D5D%2FZ2Il0xeByzF5B49HmmwmgB%2F06NcRz537oMARdfOF%2BbPuSM0RnZCXjtRiN8&X-Amz-Signature=2b74c97e633e41f28fbabf616f2cc78ea4ee112ccbbc398598562f982efb1657&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRUYJWF2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCUfJJKi5hs%2FtcAHinbLmUIgnU8l78UgQy12MCiGadeWwIgQCT7uDpLzQ%2B%2BDxhfNfRxD0i8M8lgMgx9TMn71iz8Ifsq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDE8umWr9MaRp4GFk3CrcAwoUZduWz8Ls0XVV3X4Btugb7wflWdjq1MaxQiqV0juT%2F1Xs1G4OKQv%2FCvks4Cntu0wR%2BdWuXxDqfsBQ3FjqfOaiQkfDKYuNXEwPKqvmLCPxYtzKS%2BSXRxXdn7ex9lwTydAURu%2B%2FCWovl4rF4DZP%2FK7GilJR4DU3vid%2FWs%2FbJFN%2F%2FJc7OSn5jF4Hq8PJZpwo%2B5JSUdWAUK6mYvK8y4QGKvpb4DwlRZ9nDo%2FFuW2F%2Byo5%2BdQ30LE6kEnVxVt1Zu595Q8ZyVJ%2BRixLXfKJH5mLKDlMvKRjIYeL80m4JDARyg%2BKx2p7RmpMdUdc3rB%2ByFV5eyPOzOKgwmsvF2Sn877iQQbGyawl8HL19pikvtW8eyIGlfgZPQazqWAkk92AaXamhgPoxdPI8orApbhlgMUjSH6IhujUy9NNJvye87kVJu3mJNMOfe26OsE52uCfO4K585QQBGQno2iuCrAP7bnGaITziSYRbtZnOiBnhd0HJVfNwd2WjwXzJyAB9u%2BoiV2iy3ONBETFl7MOXMrdxwx7pNXNYk3MpfuZCSnb3oBHLXIuTaZaToQ3EnEtxrvHJc6Ujc1eGq7nMnfvkGuUZcuBTQ%2FPv5HwydTeymzkoycc4A6xCdpJ%2BWBTLrncgRDIMLK4lL0GOqUBIA2xMwO8t4ZWc7SSa1hXrYbAI5gQtK9Ts6RUjUmO%2Fk0qkEPO6iqcE1ZylPZXbQ0bFHFzC%2FGhX9ElZb3QxHXPS7PVli1IlsALSC4GPH3hFqW2h90cuigLttlOJINAqEb%2FDGiRIbLSydD949%2FSh5RzDCHMUUVPk8D5D%2FZ2Il0xeByzF5B49HmmwmgB%2F06NcRz537oMARdfOF%2BbPuSM0RnZCXjtRiN8&X-Amz-Signature=61e1a0415e7d0ba4fecdcdf6d889a0d83d0ea4bc7fccaedc1311508a9a3b8b8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZDEHTAW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDiHlad0tnBRYsxDCCopmUSbes%2Fzn8Pk8n4qNFsdzZkogIhAKcsGvltq6RDrkxYYckb1VHKpmdp20RVgoTVqqN0ntHQKv8DCGYQABoMNjM3NDIzMTgzODA1IgzuupgH1R2IV77AH3Aq3AMv57pxNSFn2o1cPqDxmMo31xTRLV1qG9aQS3lu6ofYqTjjT4mzEpMQtbpTWIgHSGazfSiYlFggQhdNwaXWjIHpMm%2B1CyYgyHoVcXZoNvrDosTitX72xc62HH9edNa2Mt%2FafczSWFftFbKdSqJfcbOC4XcI0s3HVncup61ZKvaCWy7O385V%2BvtqvfDFGP012AfQQnoMMg0e4NvnW5jWzzvkG39AEhPFxkLuJ44K1KwuarQ4216N2Y%2Fl4KRXrl05MyDeFSAgPCjGxPXir828vJ0YCV%2Bu5c0uO8hW8CwCcqpiG32iwt5TPisYlj6lFvX4I0hO3TZmK4dMygF%2FLOo%2BMDO7I65JbpBDgseCISCv2RdhwHrF4GmUYOxAGgfFGf7FbQwIOOreKxLaVFey%2F6zn%2F0sGoqQ3GvNDys2QAWcAUGNDPG%2FbEGdTjo29EUwEyg31jrepikT2MpB%2F3kt%2BoN8PgxhKNguBH3gueVeIhIYPP1hM4TLD6vDT31CVgOHX%2FVdXrVrIWniJIhxNAOOX3zKSKjPzHHli9MCZ8b5ljwC22x2o8vAZB9NRfcgCbw4Rh%2FwfcNUTiy5hsJ2l8nETttW0XDR%2F3UbzNb6MTjk9B11rptFmbxfNz9LxX8onH%2Fli9jCyuJS9BjqkAa27tY9t9aC41GwYQzTu8SxY8826OtEmj%2F9X0QdnuK2rA0f7ed3m7qXYnU%2FEMbfA%2FqmFbfu9K723iedot72jU6QhFgn1ah51TRAa2BD0NYKJQyRdQCihKiR7QktxCFYraj7TLYVyShgv82JC%2FPQhM59vBUQG%2B%2FywQY7TXpts%2F6hW%2FiYovsMX00Vt%2FbMvtESKg3kkBEnouAVocCK9o8Bot7Hs7tLl&X-Amz-Signature=45b516a59c4739327e4d900d9ce46bc99a48892ae4b755abc007026c7dfdb752&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZDEHTAW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDiHlad0tnBRYsxDCCopmUSbes%2Fzn8Pk8n4qNFsdzZkogIhAKcsGvltq6RDrkxYYckb1VHKpmdp20RVgoTVqqN0ntHQKv8DCGYQABoMNjM3NDIzMTgzODA1IgzuupgH1R2IV77AH3Aq3AMv57pxNSFn2o1cPqDxmMo31xTRLV1qG9aQS3lu6ofYqTjjT4mzEpMQtbpTWIgHSGazfSiYlFggQhdNwaXWjIHpMm%2B1CyYgyHoVcXZoNvrDosTitX72xc62HH9edNa2Mt%2FafczSWFftFbKdSqJfcbOC4XcI0s3HVncup61ZKvaCWy7O385V%2BvtqvfDFGP012AfQQnoMMg0e4NvnW5jWzzvkG39AEhPFxkLuJ44K1KwuarQ4216N2Y%2Fl4KRXrl05MyDeFSAgPCjGxPXir828vJ0YCV%2Bu5c0uO8hW8CwCcqpiG32iwt5TPisYlj6lFvX4I0hO3TZmK4dMygF%2FLOo%2BMDO7I65JbpBDgseCISCv2RdhwHrF4GmUYOxAGgfFGf7FbQwIOOreKxLaVFey%2F6zn%2F0sGoqQ3GvNDys2QAWcAUGNDPG%2FbEGdTjo29EUwEyg31jrepikT2MpB%2F3kt%2BoN8PgxhKNguBH3gueVeIhIYPP1hM4TLD6vDT31CVgOHX%2FVdXrVrIWniJIhxNAOOX3zKSKjPzHHli9MCZ8b5ljwC22x2o8vAZB9NRfcgCbw4Rh%2FwfcNUTiy5hsJ2l8nETttW0XDR%2F3UbzNb6MTjk9B11rptFmbxfNz9LxX8onH%2Fli9jCyuJS9BjqkAa27tY9t9aC41GwYQzTu8SxY8826OtEmj%2F9X0QdnuK2rA0f7ed3m7qXYnU%2FEMbfA%2FqmFbfu9K723iedot72jU6QhFgn1ah51TRAa2BD0NYKJQyRdQCihKiR7QktxCFYraj7TLYVyShgv82JC%2FPQhM59vBUQG%2B%2FywQY7TXpts%2F6hW%2FiYovsMX00Vt%2FbMvtESKg3kkBEnouAVocCK9o8Bot7Hs7tLl&X-Amz-Signature=3a1fd703d47495070e4c5cde52b12e4c1610bb172ca92201aef5ea4b21872771&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
