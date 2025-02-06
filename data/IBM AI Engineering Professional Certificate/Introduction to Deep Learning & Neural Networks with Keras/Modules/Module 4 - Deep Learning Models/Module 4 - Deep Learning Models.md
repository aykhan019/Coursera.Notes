

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3MXDBTS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCICrThxyuSkoblj15LAyXfB40CfU5cD610hnDDDczv9MoAiEAqWlMVhH1cNhkIhc%2Ba64PPAkla4V9ev6AbqsFK6FTp1Uq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDKPxKt0nvF5jSEB8VircAw%2Bl9158lOLw%2B%2BgDjOjUrfYokUkOsrV5IIRTgy96PQgwEsZVrX6WpJCFpBVmF75xhmQIZUsnz0elswoqb8upy5tSbyYpaDhXz8r4N%2F2u2xJwgQOur0gm4HpwGNX2Lj6QqsM%2B72%2F1SGW9VAVCmC8L2Pqj4GUfIm37SEKV5bRaKumppqJecO703H7cJlhTyrXqfORFg2MiCKzZ0hbGuUhbP7Df6qBTjpvTHoHtGdGju2MV9AhePwS3KaGUbbW1gBmQswfdfZXc6VwxWl5hI84ff4TZh3RXNLKo9ZKsCkMb2lO5iKsqlGYJOQ4qFrlIYAMmHgofZa%2F4%2BvUY876MY6if1%2Bbf5gtyi9BKwtxAs2pNtaDOBLgMLimBht4BEse8qH6oTraQAJGqDD0nkxjEL7l6JLXuwkbepb2U3LcLXUVN%2B1w64uBtIIOjRM2C3xdwjrjXgXPILpdinUqhmQtzwHtiGePFa%2FIr55dcJ%2FMfcw%2FmJL1KlhykMrv7xELQTMb7821DUzdWy9RNVafQ5i0hLm8Ob4%2FcyRe8VkP4SshGQm842gMOOKoxtY5TWhw%2B%2FXwtS5n4qsC3xncFwxSGfej1dkl6o8bDn64EHY1LZwJ%2BnP6Zt2vtWwSVBq%2BZ4CU8rzMAMPTRkb0GOqUBhMJO%2Fyhyzu4ceBgXtduSwEk5Ca9JUXsMOB0cU%2F8cD92p5aCmS4vVab7u%2BR0EZw8McF1VYCBBaxuIl3kuOB2zDffBvojEX2ysxnyEo00MYAdfNArLD22lwKSkfIySJwkPE70pbQPWvXzb3IJQKUmcRriYu63D2Rvxy%2BDUkEetAuR1qovZNiu%2FApd79hnL0K%2B97%2BtPt%2FB3xBUjhXwKPesI2b1RVCzH&X-Amz-Signature=1553a3a737388f87a707f124d56f06e0d2dcf039f5d5903e1cfc237521d1781d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3MXDBTS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCICrThxyuSkoblj15LAyXfB40CfU5cD610hnDDDczv9MoAiEAqWlMVhH1cNhkIhc%2Ba64PPAkla4V9ev6AbqsFK6FTp1Uq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDKPxKt0nvF5jSEB8VircAw%2Bl9158lOLw%2B%2BgDjOjUrfYokUkOsrV5IIRTgy96PQgwEsZVrX6WpJCFpBVmF75xhmQIZUsnz0elswoqb8upy5tSbyYpaDhXz8r4N%2F2u2xJwgQOur0gm4HpwGNX2Lj6QqsM%2B72%2F1SGW9VAVCmC8L2Pqj4GUfIm37SEKV5bRaKumppqJecO703H7cJlhTyrXqfORFg2MiCKzZ0hbGuUhbP7Df6qBTjpvTHoHtGdGju2MV9AhePwS3KaGUbbW1gBmQswfdfZXc6VwxWl5hI84ff4TZh3RXNLKo9ZKsCkMb2lO5iKsqlGYJOQ4qFrlIYAMmHgofZa%2F4%2BvUY876MY6if1%2Bbf5gtyi9BKwtxAs2pNtaDOBLgMLimBht4BEse8qH6oTraQAJGqDD0nkxjEL7l6JLXuwkbepb2U3LcLXUVN%2B1w64uBtIIOjRM2C3xdwjrjXgXPILpdinUqhmQtzwHtiGePFa%2FIr55dcJ%2FMfcw%2FmJL1KlhykMrv7xELQTMb7821DUzdWy9RNVafQ5i0hLm8Ob4%2FcyRe8VkP4SshGQm842gMOOKoxtY5TWhw%2B%2FXwtS5n4qsC3xncFwxSGfej1dkl6o8bDn64EHY1LZwJ%2BnP6Zt2vtWwSVBq%2BZ4CU8rzMAMPTRkb0GOqUBhMJO%2Fyhyzu4ceBgXtduSwEk5Ca9JUXsMOB0cU%2F8cD92p5aCmS4vVab7u%2BR0EZw8McF1VYCBBaxuIl3kuOB2zDffBvojEX2ysxnyEo00MYAdfNArLD22lwKSkfIySJwkPE70pbQPWvXzb3IJQKUmcRriYu63D2Rvxy%2BDUkEetAuR1qovZNiu%2FApd79hnL0K%2B97%2BtPt%2FB3xBUjhXwKPesI2b1RVCzH&X-Amz-Signature=80b9dc7479a0e41e11d0d3dffc4ecf147fbf0b2d9b28a2e6b8b7faeb3f9bb020&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3MXDBTS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCICrThxyuSkoblj15LAyXfB40CfU5cD610hnDDDczv9MoAiEAqWlMVhH1cNhkIhc%2Ba64PPAkla4V9ev6AbqsFK6FTp1Uq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDKPxKt0nvF5jSEB8VircAw%2Bl9158lOLw%2B%2BgDjOjUrfYokUkOsrV5IIRTgy96PQgwEsZVrX6WpJCFpBVmF75xhmQIZUsnz0elswoqb8upy5tSbyYpaDhXz8r4N%2F2u2xJwgQOur0gm4HpwGNX2Lj6QqsM%2B72%2F1SGW9VAVCmC8L2Pqj4GUfIm37SEKV5bRaKumppqJecO703H7cJlhTyrXqfORFg2MiCKzZ0hbGuUhbP7Df6qBTjpvTHoHtGdGju2MV9AhePwS3KaGUbbW1gBmQswfdfZXc6VwxWl5hI84ff4TZh3RXNLKo9ZKsCkMb2lO5iKsqlGYJOQ4qFrlIYAMmHgofZa%2F4%2BvUY876MY6if1%2Bbf5gtyi9BKwtxAs2pNtaDOBLgMLimBht4BEse8qH6oTraQAJGqDD0nkxjEL7l6JLXuwkbepb2U3LcLXUVN%2B1w64uBtIIOjRM2C3xdwjrjXgXPILpdinUqhmQtzwHtiGePFa%2FIr55dcJ%2FMfcw%2FmJL1KlhykMrv7xELQTMb7821DUzdWy9RNVafQ5i0hLm8Ob4%2FcyRe8VkP4SshGQm842gMOOKoxtY5TWhw%2B%2FXwtS5n4qsC3xncFwxSGfej1dkl6o8bDn64EHY1LZwJ%2BnP6Zt2vtWwSVBq%2BZ4CU8rzMAMPTRkb0GOqUBhMJO%2Fyhyzu4ceBgXtduSwEk5Ca9JUXsMOB0cU%2F8cD92p5aCmS4vVab7u%2BR0EZw8McF1VYCBBaxuIl3kuOB2zDffBvojEX2ysxnyEo00MYAdfNArLD22lwKSkfIySJwkPE70pbQPWvXzb3IJQKUmcRriYu63D2Rvxy%2BDUkEetAuR1qovZNiu%2FApd79hnL0K%2B97%2BtPt%2FB3xBUjhXwKPesI2b1RVCzH&X-Amz-Signature=4cdf0ca5749fe7c67908ea99663d96db4f4ed7ecf59b3200de80b579d4afe166&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3MXDBTS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCICrThxyuSkoblj15LAyXfB40CfU5cD610hnDDDczv9MoAiEAqWlMVhH1cNhkIhc%2Ba64PPAkla4V9ev6AbqsFK6FTp1Uq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDKPxKt0nvF5jSEB8VircAw%2Bl9158lOLw%2B%2BgDjOjUrfYokUkOsrV5IIRTgy96PQgwEsZVrX6WpJCFpBVmF75xhmQIZUsnz0elswoqb8upy5tSbyYpaDhXz8r4N%2F2u2xJwgQOur0gm4HpwGNX2Lj6QqsM%2B72%2F1SGW9VAVCmC8L2Pqj4GUfIm37SEKV5bRaKumppqJecO703H7cJlhTyrXqfORFg2MiCKzZ0hbGuUhbP7Df6qBTjpvTHoHtGdGju2MV9AhePwS3KaGUbbW1gBmQswfdfZXc6VwxWl5hI84ff4TZh3RXNLKo9ZKsCkMb2lO5iKsqlGYJOQ4qFrlIYAMmHgofZa%2F4%2BvUY876MY6if1%2Bbf5gtyi9BKwtxAs2pNtaDOBLgMLimBht4BEse8qH6oTraQAJGqDD0nkxjEL7l6JLXuwkbepb2U3LcLXUVN%2B1w64uBtIIOjRM2C3xdwjrjXgXPILpdinUqhmQtzwHtiGePFa%2FIr55dcJ%2FMfcw%2FmJL1KlhykMrv7xELQTMb7821DUzdWy9RNVafQ5i0hLm8Ob4%2FcyRe8VkP4SshGQm842gMOOKoxtY5TWhw%2B%2FXwtS5n4qsC3xncFwxSGfej1dkl6o8bDn64EHY1LZwJ%2BnP6Zt2vtWwSVBq%2BZ4CU8rzMAMPTRkb0GOqUBhMJO%2Fyhyzu4ceBgXtduSwEk5Ca9JUXsMOB0cU%2F8cD92p5aCmS4vVab7u%2BR0EZw8McF1VYCBBaxuIl3kuOB2zDffBvojEX2ysxnyEo00MYAdfNArLD22lwKSkfIySJwkPE70pbQPWvXzb3IJQKUmcRriYu63D2Rvxy%2BDUkEetAuR1qovZNiu%2FApd79hnL0K%2B97%2BtPt%2FB3xBUjhXwKPesI2b1RVCzH&X-Amz-Signature=6f7cb272da649925e52125518713cfa09e351506622026256e6c92f530e65c4d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3MXDBTS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCICrThxyuSkoblj15LAyXfB40CfU5cD610hnDDDczv9MoAiEAqWlMVhH1cNhkIhc%2Ba64PPAkla4V9ev6AbqsFK6FTp1Uq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDKPxKt0nvF5jSEB8VircAw%2Bl9158lOLw%2B%2BgDjOjUrfYokUkOsrV5IIRTgy96PQgwEsZVrX6WpJCFpBVmF75xhmQIZUsnz0elswoqb8upy5tSbyYpaDhXz8r4N%2F2u2xJwgQOur0gm4HpwGNX2Lj6QqsM%2B72%2F1SGW9VAVCmC8L2Pqj4GUfIm37SEKV5bRaKumppqJecO703H7cJlhTyrXqfORFg2MiCKzZ0hbGuUhbP7Df6qBTjpvTHoHtGdGju2MV9AhePwS3KaGUbbW1gBmQswfdfZXc6VwxWl5hI84ff4TZh3RXNLKo9ZKsCkMb2lO5iKsqlGYJOQ4qFrlIYAMmHgofZa%2F4%2BvUY876MY6if1%2Bbf5gtyi9BKwtxAs2pNtaDOBLgMLimBht4BEse8qH6oTraQAJGqDD0nkxjEL7l6JLXuwkbepb2U3LcLXUVN%2B1w64uBtIIOjRM2C3xdwjrjXgXPILpdinUqhmQtzwHtiGePFa%2FIr55dcJ%2FMfcw%2FmJL1KlhykMrv7xELQTMb7821DUzdWy9RNVafQ5i0hLm8Ob4%2FcyRe8VkP4SshGQm842gMOOKoxtY5TWhw%2B%2FXwtS5n4qsC3xncFwxSGfej1dkl6o8bDn64EHY1LZwJ%2BnP6Zt2vtWwSVBq%2BZ4CU8rzMAMPTRkb0GOqUBhMJO%2Fyhyzu4ceBgXtduSwEk5Ca9JUXsMOB0cU%2F8cD92p5aCmS4vVab7u%2BR0EZw8McF1VYCBBaxuIl3kuOB2zDffBvojEX2ysxnyEo00MYAdfNArLD22lwKSkfIySJwkPE70pbQPWvXzb3IJQKUmcRriYu63D2Rvxy%2BDUkEetAuR1qovZNiu%2FApd79hnL0K%2B97%2BtPt%2FB3xBUjhXwKPesI2b1RVCzH&X-Amz-Signature=443e6b0ec4fb4c159ae062f5652ee846d04a9e7996ca1d4d24f5120252fcb839&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3MXDBTS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCICrThxyuSkoblj15LAyXfB40CfU5cD610hnDDDczv9MoAiEAqWlMVhH1cNhkIhc%2Ba64PPAkla4V9ev6AbqsFK6FTp1Uq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDKPxKt0nvF5jSEB8VircAw%2Bl9158lOLw%2B%2BgDjOjUrfYokUkOsrV5IIRTgy96PQgwEsZVrX6WpJCFpBVmF75xhmQIZUsnz0elswoqb8upy5tSbyYpaDhXz8r4N%2F2u2xJwgQOur0gm4HpwGNX2Lj6QqsM%2B72%2F1SGW9VAVCmC8L2Pqj4GUfIm37SEKV5bRaKumppqJecO703H7cJlhTyrXqfORFg2MiCKzZ0hbGuUhbP7Df6qBTjpvTHoHtGdGju2MV9AhePwS3KaGUbbW1gBmQswfdfZXc6VwxWl5hI84ff4TZh3RXNLKo9ZKsCkMb2lO5iKsqlGYJOQ4qFrlIYAMmHgofZa%2F4%2BvUY876MY6if1%2Bbf5gtyi9BKwtxAs2pNtaDOBLgMLimBht4BEse8qH6oTraQAJGqDD0nkxjEL7l6JLXuwkbepb2U3LcLXUVN%2B1w64uBtIIOjRM2C3xdwjrjXgXPILpdinUqhmQtzwHtiGePFa%2FIr55dcJ%2FMfcw%2FmJL1KlhykMrv7xELQTMb7821DUzdWy9RNVafQ5i0hLm8Ob4%2FcyRe8VkP4SshGQm842gMOOKoxtY5TWhw%2B%2FXwtS5n4qsC3xncFwxSGfej1dkl6o8bDn64EHY1LZwJ%2BnP6Zt2vtWwSVBq%2BZ4CU8rzMAMPTRkb0GOqUBhMJO%2Fyhyzu4ceBgXtduSwEk5Ca9JUXsMOB0cU%2F8cD92p5aCmS4vVab7u%2BR0EZw8McF1VYCBBaxuIl3kuOB2zDffBvojEX2ysxnyEo00MYAdfNArLD22lwKSkfIySJwkPE70pbQPWvXzb3IJQKUmcRriYu63D2Rvxy%2BDUkEetAuR1qovZNiu%2FApd79hnL0K%2B97%2BtPt%2FB3xBUjhXwKPesI2b1RVCzH&X-Amz-Signature=546511b05d5e7c9f510070e4e3b9a5a1065339d0ec91c8d66b2b1c021a3508d6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3MXDBTS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCICrThxyuSkoblj15LAyXfB40CfU5cD610hnDDDczv9MoAiEAqWlMVhH1cNhkIhc%2Ba64PPAkla4V9ev6AbqsFK6FTp1Uq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDKPxKt0nvF5jSEB8VircAw%2Bl9158lOLw%2B%2BgDjOjUrfYokUkOsrV5IIRTgy96PQgwEsZVrX6WpJCFpBVmF75xhmQIZUsnz0elswoqb8upy5tSbyYpaDhXz8r4N%2F2u2xJwgQOur0gm4HpwGNX2Lj6QqsM%2B72%2F1SGW9VAVCmC8L2Pqj4GUfIm37SEKV5bRaKumppqJecO703H7cJlhTyrXqfORFg2MiCKzZ0hbGuUhbP7Df6qBTjpvTHoHtGdGju2MV9AhePwS3KaGUbbW1gBmQswfdfZXc6VwxWl5hI84ff4TZh3RXNLKo9ZKsCkMb2lO5iKsqlGYJOQ4qFrlIYAMmHgofZa%2F4%2BvUY876MY6if1%2Bbf5gtyi9BKwtxAs2pNtaDOBLgMLimBht4BEse8qH6oTraQAJGqDD0nkxjEL7l6JLXuwkbepb2U3LcLXUVN%2B1w64uBtIIOjRM2C3xdwjrjXgXPILpdinUqhmQtzwHtiGePFa%2FIr55dcJ%2FMfcw%2FmJL1KlhykMrv7xELQTMb7821DUzdWy9RNVafQ5i0hLm8Ob4%2FcyRe8VkP4SshGQm842gMOOKoxtY5TWhw%2B%2FXwtS5n4qsC3xncFwxSGfej1dkl6o8bDn64EHY1LZwJ%2BnP6Zt2vtWwSVBq%2BZ4CU8rzMAMPTRkb0GOqUBhMJO%2Fyhyzu4ceBgXtduSwEk5Ca9JUXsMOB0cU%2F8cD92p5aCmS4vVab7u%2BR0EZw8McF1VYCBBaxuIl3kuOB2zDffBvojEX2ysxnyEo00MYAdfNArLD22lwKSkfIySJwkPE70pbQPWvXzb3IJQKUmcRriYu63D2Rvxy%2BDUkEetAuR1qovZNiu%2FApd79hnL0K%2B97%2BtPt%2FB3xBUjhXwKPesI2b1RVCzH&X-Amz-Signature=772db418f1c4949a954b75a8fccb7eaf31d789f31c373a8121cb5c78c29499bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3MXDBTS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCICrThxyuSkoblj15LAyXfB40CfU5cD610hnDDDczv9MoAiEAqWlMVhH1cNhkIhc%2Ba64PPAkla4V9ev6AbqsFK6FTp1Uq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDKPxKt0nvF5jSEB8VircAw%2Bl9158lOLw%2B%2BgDjOjUrfYokUkOsrV5IIRTgy96PQgwEsZVrX6WpJCFpBVmF75xhmQIZUsnz0elswoqb8upy5tSbyYpaDhXz8r4N%2F2u2xJwgQOur0gm4HpwGNX2Lj6QqsM%2B72%2F1SGW9VAVCmC8L2Pqj4GUfIm37SEKV5bRaKumppqJecO703H7cJlhTyrXqfORFg2MiCKzZ0hbGuUhbP7Df6qBTjpvTHoHtGdGju2MV9AhePwS3KaGUbbW1gBmQswfdfZXc6VwxWl5hI84ff4TZh3RXNLKo9ZKsCkMb2lO5iKsqlGYJOQ4qFrlIYAMmHgofZa%2F4%2BvUY876MY6if1%2Bbf5gtyi9BKwtxAs2pNtaDOBLgMLimBht4BEse8qH6oTraQAJGqDD0nkxjEL7l6JLXuwkbepb2U3LcLXUVN%2B1w64uBtIIOjRM2C3xdwjrjXgXPILpdinUqhmQtzwHtiGePFa%2FIr55dcJ%2FMfcw%2FmJL1KlhykMrv7xELQTMb7821DUzdWy9RNVafQ5i0hLm8Ob4%2FcyRe8VkP4SshGQm842gMOOKoxtY5TWhw%2B%2FXwtS5n4qsC3xncFwxSGfej1dkl6o8bDn64EHY1LZwJ%2BnP6Zt2vtWwSVBq%2BZ4CU8rzMAMPTRkb0GOqUBhMJO%2Fyhyzu4ceBgXtduSwEk5Ca9JUXsMOB0cU%2F8cD92p5aCmS4vVab7u%2BR0EZw8McF1VYCBBaxuIl3kuOB2zDffBvojEX2ysxnyEo00MYAdfNArLD22lwKSkfIySJwkPE70pbQPWvXzb3IJQKUmcRriYu63D2Rvxy%2BDUkEetAuR1qovZNiu%2FApd79hnL0K%2B97%2BtPt%2FB3xBUjhXwKPesI2b1RVCzH&X-Amz-Signature=c0a7852e394f512404a609b87481518ce8c0d19f917e602cf3a07a3116dcb3bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3MXDBTS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCICrThxyuSkoblj15LAyXfB40CfU5cD610hnDDDczv9MoAiEAqWlMVhH1cNhkIhc%2Ba64PPAkla4V9ev6AbqsFK6FTp1Uq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDKPxKt0nvF5jSEB8VircAw%2Bl9158lOLw%2B%2BgDjOjUrfYokUkOsrV5IIRTgy96PQgwEsZVrX6WpJCFpBVmF75xhmQIZUsnz0elswoqb8upy5tSbyYpaDhXz8r4N%2F2u2xJwgQOur0gm4HpwGNX2Lj6QqsM%2B72%2F1SGW9VAVCmC8L2Pqj4GUfIm37SEKV5bRaKumppqJecO703H7cJlhTyrXqfORFg2MiCKzZ0hbGuUhbP7Df6qBTjpvTHoHtGdGju2MV9AhePwS3KaGUbbW1gBmQswfdfZXc6VwxWl5hI84ff4TZh3RXNLKo9ZKsCkMb2lO5iKsqlGYJOQ4qFrlIYAMmHgofZa%2F4%2BvUY876MY6if1%2Bbf5gtyi9BKwtxAs2pNtaDOBLgMLimBht4BEse8qH6oTraQAJGqDD0nkxjEL7l6JLXuwkbepb2U3LcLXUVN%2B1w64uBtIIOjRM2C3xdwjrjXgXPILpdinUqhmQtzwHtiGePFa%2FIr55dcJ%2FMfcw%2FmJL1KlhykMrv7xELQTMb7821DUzdWy9RNVafQ5i0hLm8Ob4%2FcyRe8VkP4SshGQm842gMOOKoxtY5TWhw%2B%2FXwtS5n4qsC3xncFwxSGfej1dkl6o8bDn64EHY1LZwJ%2BnP6Zt2vtWwSVBq%2BZ4CU8rzMAMPTRkb0GOqUBhMJO%2Fyhyzu4ceBgXtduSwEk5Ca9JUXsMOB0cU%2F8cD92p5aCmS4vVab7u%2BR0EZw8McF1VYCBBaxuIl3kuOB2zDffBvojEX2ysxnyEo00MYAdfNArLD22lwKSkfIySJwkPE70pbQPWvXzb3IJQKUmcRriYu63D2Rvxy%2BDUkEetAuR1qovZNiu%2FApd79hnL0K%2B97%2BtPt%2FB3xBUjhXwKPesI2b1RVCzH&X-Amz-Signature=b15cf94fa712eaeb2e573bda1e0f601129558a5b5aeeef2aecd41ce34c33d8d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTL4K6TX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIH%2BZ9yVS5nK3BEGNyUpD70XPkigduOdZXcykjrSHpwPmAiBxsnExze%2Fcie%2FQ1XrX%2BPLpce8y0L2VmrLOUENz8byq6ir%2FAwhZEAAaDDYzNzQyMzE4MzgwNSIMlE0fFKXEDn%2FL21RXKtwDjtcehdKwpVyYHGnjj%2F7m9GWSuvfjJSvbmjFyNiS8SCMQ6ukRTlZijdjZk0hR2Mnx2tnd1OGT1c%2FgDajnulVequK3Si3KCRrnTtr61Vo%2BFo3A5OLDtQHou095iqb5Nsw%2FraQGSvVzfQlf%2BM%2BXwCdt8U80tWHw1eMx3OK1X%2FtEGhySY8v8CDnsEkDb2CGC%2BFM5VDKD2EqVvP3o8r04xdb8tUJuZ6HZyjwmQv92tQploL0kCSiTmxfZSrvi0V2cizjv2mF1YFWksPBV5CuDNomzfcyFhOA0vULZdDjODHNrkjIc25TDryHQCvuEuMVad2%2B9mOanzC1qgFfIqiZNB1eyLrRBAnnINy7nanSiFQ%2FO8MevnL9EsCZsnyYSXHg%2BZXu4QzpS6f1ajCm0ANalbIjqBn6nb6%2B8%2Bj19L%2FfTJFRghZ4meMHbSfWbgTi73%2BIai%2Fk%2FPtN6%2Byf8r3HpuFoQ9ycctF%2BUVHA4tTW6GZAN9iLgOq58w7Rd%2BJCEdoEYzyhSbQERhAwXfzNB1SNrNedR3Vvj4lllJfUCxQlsIafAUQlkI7NF9MABRqg4mKL9xcSa6EiUO627Smf0Aw%2BbTqiMbbAJhVCwxOq2vS2r5ywhjNrn54WBRQE4E0UBVPYLNx8wudGRvQY6pgGtdfdV6MXGA5g7epZy8zUj5htcxzzFs1Jekzkmrstwv0e2sREuGUAml9xgdf%2BXK%2Br8X3P6NWCrLMlE%2B%2F%2B9Y0gBvV41bxyDzpUJeAz3P%2BjhbXnEwEdIF%2FGZ%2F51Cz9vPhMv%2BRyd3hub4qM19YGfr%2Fu5sCqMwnlVDxneTOUUGTcLNZ60O3n44KtmcLfPOIS2gTjOVQodBluPLWvTfuPt0ee%2FzDP3CW6wb&X-Amz-Signature=a69a4e577f48ac263a938421c38cf0c566b1e40558687945146a4008f88dfc70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTL4K6TX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIH%2BZ9yVS5nK3BEGNyUpD70XPkigduOdZXcykjrSHpwPmAiBxsnExze%2Fcie%2FQ1XrX%2BPLpce8y0L2VmrLOUENz8byq6ir%2FAwhZEAAaDDYzNzQyMzE4MzgwNSIMlE0fFKXEDn%2FL21RXKtwDjtcehdKwpVyYHGnjj%2F7m9GWSuvfjJSvbmjFyNiS8SCMQ6ukRTlZijdjZk0hR2Mnx2tnd1OGT1c%2FgDajnulVequK3Si3KCRrnTtr61Vo%2BFo3A5OLDtQHou095iqb5Nsw%2FraQGSvVzfQlf%2BM%2BXwCdt8U80tWHw1eMx3OK1X%2FtEGhySY8v8CDnsEkDb2CGC%2BFM5VDKD2EqVvP3o8r04xdb8tUJuZ6HZyjwmQv92tQploL0kCSiTmxfZSrvi0V2cizjv2mF1YFWksPBV5CuDNomzfcyFhOA0vULZdDjODHNrkjIc25TDryHQCvuEuMVad2%2B9mOanzC1qgFfIqiZNB1eyLrRBAnnINy7nanSiFQ%2FO8MevnL9EsCZsnyYSXHg%2BZXu4QzpS6f1ajCm0ANalbIjqBn6nb6%2B8%2Bj19L%2FfTJFRghZ4meMHbSfWbgTi73%2BIai%2Fk%2FPtN6%2Byf8r3HpuFoQ9ycctF%2BUVHA4tTW6GZAN9iLgOq58w7Rd%2BJCEdoEYzyhSbQERhAwXfzNB1SNrNedR3Vvj4lllJfUCxQlsIafAUQlkI7NF9MABRqg4mKL9xcSa6EiUO627Smf0Aw%2BbTqiMbbAJhVCwxOq2vS2r5ywhjNrn54WBRQE4E0UBVPYLNx8wudGRvQY6pgGtdfdV6MXGA5g7epZy8zUj5htcxzzFs1Jekzkmrstwv0e2sREuGUAml9xgdf%2BXK%2Br8X3P6NWCrLMlE%2B%2F%2B9Y0gBvV41bxyDzpUJeAz3P%2BjhbXnEwEdIF%2FGZ%2F51Cz9vPhMv%2BRyd3hub4qM19YGfr%2Fu5sCqMwnlVDxneTOUUGTcLNZ60O3n44KtmcLfPOIS2gTjOVQodBluPLWvTfuPt0ee%2FzDP3CW6wb&X-Amz-Signature=78e82ef7ed41b880f43ffc664f42aefada5bf1c65290a88173346c0e5a7dbc53&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
