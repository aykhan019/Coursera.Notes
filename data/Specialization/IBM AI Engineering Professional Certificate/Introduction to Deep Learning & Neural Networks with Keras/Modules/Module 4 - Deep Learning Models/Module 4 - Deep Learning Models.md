

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YC7RW5X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDgYAplYiqZHkqxTlVTym4QtKtIbma1O2oqf2bq63S%2FYAiAY%2B0GxCXNKA%2BlIqKEztqnSHp88LCvdNgx3QS4KimBZ5yqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZOD1sujyKurQ%2FOXtKtwDAjImccW7a22PpUCdhSF5NRcXrMOQCVqZ5c%2B32j8XXW7KbzNjKlWBo17jwkTq8lxww1Om6U%2BTnNa2xS9ox1%2FY%2F%2FuoIF2NTJRoZ2atnM5ZhA7cN1PbKCbcTqlLtwtoXmzU92ob%2BzB%2FLGBdRus6ovu6qRPh8BLVrWIfYUXjCFMT8t4VeOfqzP3PLPgwtUakzgwtTWr0fl9q3CNsjfSyXor3lswU1u3ZPj8asJGtnfmFL2N3t4BfpjwRVx%2Fe9yGUggwPjyvJBa5tBQ5ItMHO0XwP%2F81sRargr5yrOV5tPDS%2FkwlQSFqD3aWJNTbmCdKYJgqB7fGNboil%2FYMzOF3NmhE10Ei4sJXfUjhHybE5qwYhu7qeM8qgWs49pz2J53SMsMoVC8HpJi90tvsXxkMwRSgUK7i2mi8VzGJ%2BNG%2B1g%2BarR901H7rZytwowyCQ8btf1RGndEMSGCHZRTdWl2FAkC69U4IXKtQGbjdlr2T4gnO%2Bk4zcguToe1bz6vbU7MGH3AfsQes2n0of5v1hGk%2B8GozPAlEbl%2BWS7eFSD68SiWp8VdAlURx5cC214n3D83xZFyTh%2B4DUf6l%2FvVZjeO%2B1a1KLJnbyWyenHwhBDb%2Bd%2F4d43B6FHBxO2n7QqueoBHwwjd%2FtvAY6pgFDa8AwT5hQ1p5rWeehb07%2BZOFmhF0N8z2enQjqeEr9ALq0fUnVo4uUSiweBcb%2BF1vSJCDf%2FaDUYnkvrGh6jG7VT59gj1Ov2ygSViNEeKXVHu1fJ6qUn8lYaDVjHF%2FqlqH8c3qQm4G8Dq5TvTJmPZJUpRMlcTEsYUAlEqDCy6VPwzJsd8gr4EG2Fho5FZl5yL7IwO1hQ%2Fq%2BncaMhIUlgZSqZpaxL1QX&X-Amz-Signature=7b26cb66e1221d451dca4a4fc4e0f0e2a06eff5a38c906c89f8aa9d55f74368a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YC7RW5X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDgYAplYiqZHkqxTlVTym4QtKtIbma1O2oqf2bq63S%2FYAiAY%2B0GxCXNKA%2BlIqKEztqnSHp88LCvdNgx3QS4KimBZ5yqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZOD1sujyKurQ%2FOXtKtwDAjImccW7a22PpUCdhSF5NRcXrMOQCVqZ5c%2B32j8XXW7KbzNjKlWBo17jwkTq8lxww1Om6U%2BTnNa2xS9ox1%2FY%2F%2FuoIF2NTJRoZ2atnM5ZhA7cN1PbKCbcTqlLtwtoXmzU92ob%2BzB%2FLGBdRus6ovu6qRPh8BLVrWIfYUXjCFMT8t4VeOfqzP3PLPgwtUakzgwtTWr0fl9q3CNsjfSyXor3lswU1u3ZPj8asJGtnfmFL2N3t4BfpjwRVx%2Fe9yGUggwPjyvJBa5tBQ5ItMHO0XwP%2F81sRargr5yrOV5tPDS%2FkwlQSFqD3aWJNTbmCdKYJgqB7fGNboil%2FYMzOF3NmhE10Ei4sJXfUjhHybE5qwYhu7qeM8qgWs49pz2J53SMsMoVC8HpJi90tvsXxkMwRSgUK7i2mi8VzGJ%2BNG%2B1g%2BarR901H7rZytwowyCQ8btf1RGndEMSGCHZRTdWl2FAkC69U4IXKtQGbjdlr2T4gnO%2Bk4zcguToe1bz6vbU7MGH3AfsQes2n0of5v1hGk%2B8GozPAlEbl%2BWS7eFSD68SiWp8VdAlURx5cC214n3D83xZFyTh%2B4DUf6l%2FvVZjeO%2B1a1KLJnbyWyenHwhBDb%2Bd%2F4d43B6FHBxO2n7QqueoBHwwjd%2FtvAY6pgFDa8AwT5hQ1p5rWeehb07%2BZOFmhF0N8z2enQjqeEr9ALq0fUnVo4uUSiweBcb%2BF1vSJCDf%2FaDUYnkvrGh6jG7VT59gj1Ov2ygSViNEeKXVHu1fJ6qUn8lYaDVjHF%2FqlqH8c3qQm4G8Dq5TvTJmPZJUpRMlcTEsYUAlEqDCy6VPwzJsd8gr4EG2Fho5FZl5yL7IwO1hQ%2Fq%2BncaMhIUlgZSqZpaxL1QX&X-Amz-Signature=f6e44e4eae1f1b525150f074b2ae868085ccba9574861d8b4c203c94f7843660&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YC7RW5X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDgYAplYiqZHkqxTlVTym4QtKtIbma1O2oqf2bq63S%2FYAiAY%2B0GxCXNKA%2BlIqKEztqnSHp88LCvdNgx3QS4KimBZ5yqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZOD1sujyKurQ%2FOXtKtwDAjImccW7a22PpUCdhSF5NRcXrMOQCVqZ5c%2B32j8XXW7KbzNjKlWBo17jwkTq8lxww1Om6U%2BTnNa2xS9ox1%2FY%2F%2FuoIF2NTJRoZ2atnM5ZhA7cN1PbKCbcTqlLtwtoXmzU92ob%2BzB%2FLGBdRus6ovu6qRPh8BLVrWIfYUXjCFMT8t4VeOfqzP3PLPgwtUakzgwtTWr0fl9q3CNsjfSyXor3lswU1u3ZPj8asJGtnfmFL2N3t4BfpjwRVx%2Fe9yGUggwPjyvJBa5tBQ5ItMHO0XwP%2F81sRargr5yrOV5tPDS%2FkwlQSFqD3aWJNTbmCdKYJgqB7fGNboil%2FYMzOF3NmhE10Ei4sJXfUjhHybE5qwYhu7qeM8qgWs49pz2J53SMsMoVC8HpJi90tvsXxkMwRSgUK7i2mi8VzGJ%2BNG%2B1g%2BarR901H7rZytwowyCQ8btf1RGndEMSGCHZRTdWl2FAkC69U4IXKtQGbjdlr2T4gnO%2Bk4zcguToe1bz6vbU7MGH3AfsQes2n0of5v1hGk%2B8GozPAlEbl%2BWS7eFSD68SiWp8VdAlURx5cC214n3D83xZFyTh%2B4DUf6l%2FvVZjeO%2B1a1KLJnbyWyenHwhBDb%2Bd%2F4d43B6FHBxO2n7QqueoBHwwjd%2FtvAY6pgFDa8AwT5hQ1p5rWeehb07%2BZOFmhF0N8z2enQjqeEr9ALq0fUnVo4uUSiweBcb%2BF1vSJCDf%2FaDUYnkvrGh6jG7VT59gj1Ov2ygSViNEeKXVHu1fJ6qUn8lYaDVjHF%2FqlqH8c3qQm4G8Dq5TvTJmPZJUpRMlcTEsYUAlEqDCy6VPwzJsd8gr4EG2Fho5FZl5yL7IwO1hQ%2Fq%2BncaMhIUlgZSqZpaxL1QX&X-Amz-Signature=ab1c222e98ea30b83e51c120ca5c774f858653c50da4958ad6e492cf27b0e2ef&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YC7RW5X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDgYAplYiqZHkqxTlVTym4QtKtIbma1O2oqf2bq63S%2FYAiAY%2B0GxCXNKA%2BlIqKEztqnSHp88LCvdNgx3QS4KimBZ5yqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZOD1sujyKurQ%2FOXtKtwDAjImccW7a22PpUCdhSF5NRcXrMOQCVqZ5c%2B32j8XXW7KbzNjKlWBo17jwkTq8lxww1Om6U%2BTnNa2xS9ox1%2FY%2F%2FuoIF2NTJRoZ2atnM5ZhA7cN1PbKCbcTqlLtwtoXmzU92ob%2BzB%2FLGBdRus6ovu6qRPh8BLVrWIfYUXjCFMT8t4VeOfqzP3PLPgwtUakzgwtTWr0fl9q3CNsjfSyXor3lswU1u3ZPj8asJGtnfmFL2N3t4BfpjwRVx%2Fe9yGUggwPjyvJBa5tBQ5ItMHO0XwP%2F81sRargr5yrOV5tPDS%2FkwlQSFqD3aWJNTbmCdKYJgqB7fGNboil%2FYMzOF3NmhE10Ei4sJXfUjhHybE5qwYhu7qeM8qgWs49pz2J53SMsMoVC8HpJi90tvsXxkMwRSgUK7i2mi8VzGJ%2BNG%2B1g%2BarR901H7rZytwowyCQ8btf1RGndEMSGCHZRTdWl2FAkC69U4IXKtQGbjdlr2T4gnO%2Bk4zcguToe1bz6vbU7MGH3AfsQes2n0of5v1hGk%2B8GozPAlEbl%2BWS7eFSD68SiWp8VdAlURx5cC214n3D83xZFyTh%2B4DUf6l%2FvVZjeO%2B1a1KLJnbyWyenHwhBDb%2Bd%2F4d43B6FHBxO2n7QqueoBHwwjd%2FtvAY6pgFDa8AwT5hQ1p5rWeehb07%2BZOFmhF0N8z2enQjqeEr9ALq0fUnVo4uUSiweBcb%2BF1vSJCDf%2FaDUYnkvrGh6jG7VT59gj1Ov2ygSViNEeKXVHu1fJ6qUn8lYaDVjHF%2FqlqH8c3qQm4G8Dq5TvTJmPZJUpRMlcTEsYUAlEqDCy6VPwzJsd8gr4EG2Fho5FZl5yL7IwO1hQ%2Fq%2BncaMhIUlgZSqZpaxL1QX&X-Amz-Signature=ae15846f1e9107f9d5e1176553beadf24410eef2e164bfd2b9ba836f5a777153&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YC7RW5X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDgYAplYiqZHkqxTlVTym4QtKtIbma1O2oqf2bq63S%2FYAiAY%2B0GxCXNKA%2BlIqKEztqnSHp88LCvdNgx3QS4KimBZ5yqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZOD1sujyKurQ%2FOXtKtwDAjImccW7a22PpUCdhSF5NRcXrMOQCVqZ5c%2B32j8XXW7KbzNjKlWBo17jwkTq8lxww1Om6U%2BTnNa2xS9ox1%2FY%2F%2FuoIF2NTJRoZ2atnM5ZhA7cN1PbKCbcTqlLtwtoXmzU92ob%2BzB%2FLGBdRus6ovu6qRPh8BLVrWIfYUXjCFMT8t4VeOfqzP3PLPgwtUakzgwtTWr0fl9q3CNsjfSyXor3lswU1u3ZPj8asJGtnfmFL2N3t4BfpjwRVx%2Fe9yGUggwPjyvJBa5tBQ5ItMHO0XwP%2F81sRargr5yrOV5tPDS%2FkwlQSFqD3aWJNTbmCdKYJgqB7fGNboil%2FYMzOF3NmhE10Ei4sJXfUjhHybE5qwYhu7qeM8qgWs49pz2J53SMsMoVC8HpJi90tvsXxkMwRSgUK7i2mi8VzGJ%2BNG%2B1g%2BarR901H7rZytwowyCQ8btf1RGndEMSGCHZRTdWl2FAkC69U4IXKtQGbjdlr2T4gnO%2Bk4zcguToe1bz6vbU7MGH3AfsQes2n0of5v1hGk%2B8GozPAlEbl%2BWS7eFSD68SiWp8VdAlURx5cC214n3D83xZFyTh%2B4DUf6l%2FvVZjeO%2B1a1KLJnbyWyenHwhBDb%2Bd%2F4d43B6FHBxO2n7QqueoBHwwjd%2FtvAY6pgFDa8AwT5hQ1p5rWeehb07%2BZOFmhF0N8z2enQjqeEr9ALq0fUnVo4uUSiweBcb%2BF1vSJCDf%2FaDUYnkvrGh6jG7VT59gj1Ov2ygSViNEeKXVHu1fJ6qUn8lYaDVjHF%2FqlqH8c3qQm4G8Dq5TvTJmPZJUpRMlcTEsYUAlEqDCy6VPwzJsd8gr4EG2Fho5FZl5yL7IwO1hQ%2Fq%2BncaMhIUlgZSqZpaxL1QX&X-Amz-Signature=9e1cfd2d7bdf6d20000873b303cb5bdfad451b65d986c1edb2b9363517c624c1&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YC7RW5X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDgYAplYiqZHkqxTlVTym4QtKtIbma1O2oqf2bq63S%2FYAiAY%2B0GxCXNKA%2BlIqKEztqnSHp88LCvdNgx3QS4KimBZ5yqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZOD1sujyKurQ%2FOXtKtwDAjImccW7a22PpUCdhSF5NRcXrMOQCVqZ5c%2B32j8XXW7KbzNjKlWBo17jwkTq8lxww1Om6U%2BTnNa2xS9ox1%2FY%2F%2FuoIF2NTJRoZ2atnM5ZhA7cN1PbKCbcTqlLtwtoXmzU92ob%2BzB%2FLGBdRus6ovu6qRPh8BLVrWIfYUXjCFMT8t4VeOfqzP3PLPgwtUakzgwtTWr0fl9q3CNsjfSyXor3lswU1u3ZPj8asJGtnfmFL2N3t4BfpjwRVx%2Fe9yGUggwPjyvJBa5tBQ5ItMHO0XwP%2F81sRargr5yrOV5tPDS%2FkwlQSFqD3aWJNTbmCdKYJgqB7fGNboil%2FYMzOF3NmhE10Ei4sJXfUjhHybE5qwYhu7qeM8qgWs49pz2J53SMsMoVC8HpJi90tvsXxkMwRSgUK7i2mi8VzGJ%2BNG%2B1g%2BarR901H7rZytwowyCQ8btf1RGndEMSGCHZRTdWl2FAkC69U4IXKtQGbjdlr2T4gnO%2Bk4zcguToe1bz6vbU7MGH3AfsQes2n0of5v1hGk%2B8GozPAlEbl%2BWS7eFSD68SiWp8VdAlURx5cC214n3D83xZFyTh%2B4DUf6l%2FvVZjeO%2B1a1KLJnbyWyenHwhBDb%2Bd%2F4d43B6FHBxO2n7QqueoBHwwjd%2FtvAY6pgFDa8AwT5hQ1p5rWeehb07%2BZOFmhF0N8z2enQjqeEr9ALq0fUnVo4uUSiweBcb%2BF1vSJCDf%2FaDUYnkvrGh6jG7VT59gj1Ov2ygSViNEeKXVHu1fJ6qUn8lYaDVjHF%2FqlqH8c3qQm4G8Dq5TvTJmPZJUpRMlcTEsYUAlEqDCy6VPwzJsd8gr4EG2Fho5FZl5yL7IwO1hQ%2Fq%2BncaMhIUlgZSqZpaxL1QX&X-Amz-Signature=40c7b3effc02e968393066c941a1898d8e47949148424006f04ed0131c8c3ce4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YC7RW5X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDgYAplYiqZHkqxTlVTym4QtKtIbma1O2oqf2bq63S%2FYAiAY%2B0GxCXNKA%2BlIqKEztqnSHp88LCvdNgx3QS4KimBZ5yqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZOD1sujyKurQ%2FOXtKtwDAjImccW7a22PpUCdhSF5NRcXrMOQCVqZ5c%2B32j8XXW7KbzNjKlWBo17jwkTq8lxww1Om6U%2BTnNa2xS9ox1%2FY%2F%2FuoIF2NTJRoZ2atnM5ZhA7cN1PbKCbcTqlLtwtoXmzU92ob%2BzB%2FLGBdRus6ovu6qRPh8BLVrWIfYUXjCFMT8t4VeOfqzP3PLPgwtUakzgwtTWr0fl9q3CNsjfSyXor3lswU1u3ZPj8asJGtnfmFL2N3t4BfpjwRVx%2Fe9yGUggwPjyvJBa5tBQ5ItMHO0XwP%2F81sRargr5yrOV5tPDS%2FkwlQSFqD3aWJNTbmCdKYJgqB7fGNboil%2FYMzOF3NmhE10Ei4sJXfUjhHybE5qwYhu7qeM8qgWs49pz2J53SMsMoVC8HpJi90tvsXxkMwRSgUK7i2mi8VzGJ%2BNG%2B1g%2BarR901H7rZytwowyCQ8btf1RGndEMSGCHZRTdWl2FAkC69U4IXKtQGbjdlr2T4gnO%2Bk4zcguToe1bz6vbU7MGH3AfsQes2n0of5v1hGk%2B8GozPAlEbl%2BWS7eFSD68SiWp8VdAlURx5cC214n3D83xZFyTh%2B4DUf6l%2FvVZjeO%2B1a1KLJnbyWyenHwhBDb%2Bd%2F4d43B6FHBxO2n7QqueoBHwwjd%2FtvAY6pgFDa8AwT5hQ1p5rWeehb07%2BZOFmhF0N8z2enQjqeEr9ALq0fUnVo4uUSiweBcb%2BF1vSJCDf%2FaDUYnkvrGh6jG7VT59gj1Ov2ygSViNEeKXVHu1fJ6qUn8lYaDVjHF%2FqlqH8c3qQm4G8Dq5TvTJmPZJUpRMlcTEsYUAlEqDCy6VPwzJsd8gr4EG2Fho5FZl5yL7IwO1hQ%2Fq%2BncaMhIUlgZSqZpaxL1QX&X-Amz-Signature=e960e406588093400702d3f79e47a11f1451922be54c4306a01bd6e545f3989c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YC7RW5X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDgYAplYiqZHkqxTlVTym4QtKtIbma1O2oqf2bq63S%2FYAiAY%2B0GxCXNKA%2BlIqKEztqnSHp88LCvdNgx3QS4KimBZ5yqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZOD1sujyKurQ%2FOXtKtwDAjImccW7a22PpUCdhSF5NRcXrMOQCVqZ5c%2B32j8XXW7KbzNjKlWBo17jwkTq8lxww1Om6U%2BTnNa2xS9ox1%2FY%2F%2FuoIF2NTJRoZ2atnM5ZhA7cN1PbKCbcTqlLtwtoXmzU92ob%2BzB%2FLGBdRus6ovu6qRPh8BLVrWIfYUXjCFMT8t4VeOfqzP3PLPgwtUakzgwtTWr0fl9q3CNsjfSyXor3lswU1u3ZPj8asJGtnfmFL2N3t4BfpjwRVx%2Fe9yGUggwPjyvJBa5tBQ5ItMHO0XwP%2F81sRargr5yrOV5tPDS%2FkwlQSFqD3aWJNTbmCdKYJgqB7fGNboil%2FYMzOF3NmhE10Ei4sJXfUjhHybE5qwYhu7qeM8qgWs49pz2J53SMsMoVC8HpJi90tvsXxkMwRSgUK7i2mi8VzGJ%2BNG%2B1g%2BarR901H7rZytwowyCQ8btf1RGndEMSGCHZRTdWl2FAkC69U4IXKtQGbjdlr2T4gnO%2Bk4zcguToe1bz6vbU7MGH3AfsQes2n0of5v1hGk%2B8GozPAlEbl%2BWS7eFSD68SiWp8VdAlURx5cC214n3D83xZFyTh%2B4DUf6l%2FvVZjeO%2B1a1KLJnbyWyenHwhBDb%2Bd%2F4d43B6FHBxO2n7QqueoBHwwjd%2FtvAY6pgFDa8AwT5hQ1p5rWeehb07%2BZOFmhF0N8z2enQjqeEr9ALq0fUnVo4uUSiweBcb%2BF1vSJCDf%2FaDUYnkvrGh6jG7VT59gj1Ov2ygSViNEeKXVHu1fJ6qUn8lYaDVjHF%2FqlqH8c3qQm4G8Dq5TvTJmPZJUpRMlcTEsYUAlEqDCy6VPwzJsd8gr4EG2Fho5FZl5yL7IwO1hQ%2Fq%2BncaMhIUlgZSqZpaxL1QX&X-Amz-Signature=adb518037506dec3dfd4944091b3f85bef05c50b738232428f5936d5a0fe02d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YC7RW5X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDgYAplYiqZHkqxTlVTym4QtKtIbma1O2oqf2bq63S%2FYAiAY%2B0GxCXNKA%2BlIqKEztqnSHp88LCvdNgx3QS4KimBZ5yqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZOD1sujyKurQ%2FOXtKtwDAjImccW7a22PpUCdhSF5NRcXrMOQCVqZ5c%2B32j8XXW7KbzNjKlWBo17jwkTq8lxww1Om6U%2BTnNa2xS9ox1%2FY%2F%2FuoIF2NTJRoZ2atnM5ZhA7cN1PbKCbcTqlLtwtoXmzU92ob%2BzB%2FLGBdRus6ovu6qRPh8BLVrWIfYUXjCFMT8t4VeOfqzP3PLPgwtUakzgwtTWr0fl9q3CNsjfSyXor3lswU1u3ZPj8asJGtnfmFL2N3t4BfpjwRVx%2Fe9yGUggwPjyvJBa5tBQ5ItMHO0XwP%2F81sRargr5yrOV5tPDS%2FkwlQSFqD3aWJNTbmCdKYJgqB7fGNboil%2FYMzOF3NmhE10Ei4sJXfUjhHybE5qwYhu7qeM8qgWs49pz2J53SMsMoVC8HpJi90tvsXxkMwRSgUK7i2mi8VzGJ%2BNG%2B1g%2BarR901H7rZytwowyCQ8btf1RGndEMSGCHZRTdWl2FAkC69U4IXKtQGbjdlr2T4gnO%2Bk4zcguToe1bz6vbU7MGH3AfsQes2n0of5v1hGk%2B8GozPAlEbl%2BWS7eFSD68SiWp8VdAlURx5cC214n3D83xZFyTh%2B4DUf6l%2FvVZjeO%2B1a1KLJnbyWyenHwhBDb%2Bd%2F4d43B6FHBxO2n7QqueoBHwwjd%2FtvAY6pgFDa8AwT5hQ1p5rWeehb07%2BZOFmhF0N8z2enQjqeEr9ALq0fUnVo4uUSiweBcb%2BF1vSJCDf%2FaDUYnkvrGh6jG7VT59gj1Ov2ygSViNEeKXVHu1fJ6qUn8lYaDVjHF%2FqlqH8c3qQm4G8Dq5TvTJmPZJUpRMlcTEsYUAlEqDCy6VPwzJsd8gr4EG2Fho5FZl5yL7IwO1hQ%2Fq%2BncaMhIUlgZSqZpaxL1QX&X-Amz-Signature=a91195dcd7fcce6ec0907e6ee29e3ac1bc6a5f7f691cd1368fa51ae39039c2ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PBDN2O3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBiIVOXYhDQAqbUeq3t4MJaJG6kSS71zck%2BV8YhCRZaPAiAbPzGYhVejUfZFFa2B606MOHfA9AzT9IYSKjI9Mo1LdSqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKRK2sAxxxZ9WyL5gKtwDfz2wbAbRsi64YvzEoFa2IVfzPL5iK0Ggmm5vRvMoe%2BHq37YoHvedO89iaEQ%2BLyjKoXVY0h20dqb1GLf16b56OQdryl%2FApAjlgy4a0ZqsApGb0O7qSfAuY65jHdJTS5VAg7wEP8LUVMq39J9q7uWoBWdIWZr75AdjOFPduvriIPDqc08%2B%2FvdQ%2Bzq8lu0XrMHhSWYHACRTLXDzVd0EZeZo6IklXrjf6jLGhgaTGgu%2BnCEUYi7uEB%2FKuh8fiGL0ZBBpIh%2B8tNsORAOfXZ0QAYI3VJkXcp7ypnwb2E%2FaZrlLeCxBQJEe%2FrUw6lT%2BwqZaycZqANGLK%2FqXMkfHdExy9nrMWIqhLnVN7OFmlJlgMtKmoa2H2fcgSSpx8uRZ6BXoQS63MdG2WejQ6wJT2MrEpnD3nbkmm94qqNaMta6PRA6uonTeVzpP%2FRd6hoI46G6NpaMyS7r2jl%2BSsvRIfqR5dEBrZeLfRQlMRNrluqAUmXVaSbGXiFGKcJmyXF%2BGbISgByEISOGy2SJx9n5FJE31FlJYgudo6kbDdTMppmpZhvP8OSfiKHXpRA5f6gMUqG46xXZhkFDN%2FKsda0opD8ohyI592xhJh6cxvPoubEyxlSaMZBWvMjZXoIYSYmXOCIIwgN%2FtvAY6pgEKgo9%2FB40ehDQcLBgotcNR4oRJ4eGAyHs%2BSeb0S92ZyMf7AO0UcX7zTbWnGIEBpPGzC%2FEdOBWh5UorRIX41qerzSalN0kGqItYbWjTN5YpCyDYHy9a%2Bl%2Bi2dstyhx0xuvoGoj25Bxj5uQQx7t0DR3idZRB4HtgSXj4Myy%2BmXyOdj%2FmAd%2BrTLFQ8Aqmp0wxFrKBrj1CYDQFaL2FF7mrMv12w3oLAmAj&X-Amz-Signature=73477e44227e12d62e8992ab4ba8dacaeed3dbbc1c19a196ed952fd300c4abd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PBDN2O3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBiIVOXYhDQAqbUeq3t4MJaJG6kSS71zck%2BV8YhCRZaPAiAbPzGYhVejUfZFFa2B606MOHfA9AzT9IYSKjI9Mo1LdSqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKRK2sAxxxZ9WyL5gKtwDfz2wbAbRsi64YvzEoFa2IVfzPL5iK0Ggmm5vRvMoe%2BHq37YoHvedO89iaEQ%2BLyjKoXVY0h20dqb1GLf16b56OQdryl%2FApAjlgy4a0ZqsApGb0O7qSfAuY65jHdJTS5VAg7wEP8LUVMq39J9q7uWoBWdIWZr75AdjOFPduvriIPDqc08%2B%2FvdQ%2Bzq8lu0XrMHhSWYHACRTLXDzVd0EZeZo6IklXrjf6jLGhgaTGgu%2BnCEUYi7uEB%2FKuh8fiGL0ZBBpIh%2B8tNsORAOfXZ0QAYI3VJkXcp7ypnwb2E%2FaZrlLeCxBQJEe%2FrUw6lT%2BwqZaycZqANGLK%2FqXMkfHdExy9nrMWIqhLnVN7OFmlJlgMtKmoa2H2fcgSSpx8uRZ6BXoQS63MdG2WejQ6wJT2MrEpnD3nbkmm94qqNaMta6PRA6uonTeVzpP%2FRd6hoI46G6NpaMyS7r2jl%2BSsvRIfqR5dEBrZeLfRQlMRNrluqAUmXVaSbGXiFGKcJmyXF%2BGbISgByEISOGy2SJx9n5FJE31FlJYgudo6kbDdTMppmpZhvP8OSfiKHXpRA5f6gMUqG46xXZhkFDN%2FKsda0opD8ohyI592xhJh6cxvPoubEyxlSaMZBWvMjZXoIYSYmXOCIIwgN%2FtvAY6pgEKgo9%2FB40ehDQcLBgotcNR4oRJ4eGAyHs%2BSeb0S92ZyMf7AO0UcX7zTbWnGIEBpPGzC%2FEdOBWh5UorRIX41qerzSalN0kGqItYbWjTN5YpCyDYHy9a%2Bl%2Bi2dstyhx0xuvoGoj25Bxj5uQQx7t0DR3idZRB4HtgSXj4Myy%2BmXyOdj%2FmAd%2BrTLFQ8Aqmp0wxFrKBrj1CYDQFaL2FF7mrMv12w3oLAmAj&X-Amz-Signature=3ef2b1bdae9e1cfedb47282834dc0e5045c10f0183f5230c0519a084840c0390&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
