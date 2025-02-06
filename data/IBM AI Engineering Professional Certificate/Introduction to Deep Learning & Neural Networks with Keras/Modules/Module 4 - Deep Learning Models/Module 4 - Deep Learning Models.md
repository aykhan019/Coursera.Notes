

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675A6PGIB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHBP%2FLShF5KtsHhr28SYv1cxoWD205S3r3Tj387NxaGuAiEA0OFF44gyQSU8RBjNBWuKMx792Mtd96AcpVVEdS5hOwgq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDJs3BUNXifO3NwaY8yrcA1%2BgPrSxZbbACVUGNzCo0qH%2BAULEM%2FNCbPaiIWybUVAL1yCBwTbnNvYLQpcUVf8YFaihxwaeESU1dNztthUF8xzfYv9cYq%2FUw6wRA1gLut%2F5Tnqiw3e1WGME%2BmvzhQPwXb1BC11u1RBL6SbqcczYuTKT2naD3dl0HmGFM1z4oLH8fzbtilT5EK0zlIwRhe2FKNkh1fnrz0noSp97U1MKRfjs7JKRdC4wW%2BpCKLlLr2pnlGUEkzV1vZccIfZDG415qW7ZuoqaO9WC1VGLpuEpEYO%2BPnAt38X6v9wy27aj117R3e%2BpK0%2FO1uH7%2B4JiImeYBxt7WLZEs827Ni9LODa9xgWBQut5rPv6BrsWBFedmxCGj48paF31YTSJPACig%2FEGsEQYXhEPPaZGMquj7q3r2cpTkr7FISbnynrIH7Yh6DVgIJTAQPf4eDxXvSZ7k1Poixs%2BSBMHRBQQtazD10CrXf164Fo28e2uZjxaek2LzPEVd7jl2rYZDIT7Z1jpi62Y3j0LbM5qcRni%2FwtoIpA0Hta1hdvFBeSI9%2Bi96I2R0OX%2FesaLE%2BkbVMIb%2B0sWwQQN5UdgOkIBiaOn%2Fal210wVGWMbU188g%2B00E%2BvU7dSTyejdI0ZK6IAgMRtvMhI4MN%2FfkL0GOqUBzcaU6UUjRVdV%2Fa2lDqhJ3wc%2B4GsdXQky0xFD2Anik%2FhGr5ajKzw7OhjQgDNbRDLmkpQG2t42AaSRecX8Ff8plBvn0odoYais62LwPgcekZiOt9tWxoD4jaJHuz%2Fwtfesq5qq7EfyhkZXosMtgYtaidBJVTfo6%2Beq3YYJNx4FA9NSpyJ7eE8mu1crHvl0cqLmB674ZJAuWZJuo9fwi%2FM9bfB9Ey6o&X-Amz-Signature=2ebaa6c91f7b87b6aa40ff00fab17586e1dfa9617f8353e55856951123830837&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675A6PGIB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHBP%2FLShF5KtsHhr28SYv1cxoWD205S3r3Tj387NxaGuAiEA0OFF44gyQSU8RBjNBWuKMx792Mtd96AcpVVEdS5hOwgq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDJs3BUNXifO3NwaY8yrcA1%2BgPrSxZbbACVUGNzCo0qH%2BAULEM%2FNCbPaiIWybUVAL1yCBwTbnNvYLQpcUVf8YFaihxwaeESU1dNztthUF8xzfYv9cYq%2FUw6wRA1gLut%2F5Tnqiw3e1WGME%2BmvzhQPwXb1BC11u1RBL6SbqcczYuTKT2naD3dl0HmGFM1z4oLH8fzbtilT5EK0zlIwRhe2FKNkh1fnrz0noSp97U1MKRfjs7JKRdC4wW%2BpCKLlLr2pnlGUEkzV1vZccIfZDG415qW7ZuoqaO9WC1VGLpuEpEYO%2BPnAt38X6v9wy27aj117R3e%2BpK0%2FO1uH7%2B4JiImeYBxt7WLZEs827Ni9LODa9xgWBQut5rPv6BrsWBFedmxCGj48paF31YTSJPACig%2FEGsEQYXhEPPaZGMquj7q3r2cpTkr7FISbnynrIH7Yh6DVgIJTAQPf4eDxXvSZ7k1Poixs%2BSBMHRBQQtazD10CrXf164Fo28e2uZjxaek2LzPEVd7jl2rYZDIT7Z1jpi62Y3j0LbM5qcRni%2FwtoIpA0Hta1hdvFBeSI9%2Bi96I2R0OX%2FesaLE%2BkbVMIb%2B0sWwQQN5UdgOkIBiaOn%2Fal210wVGWMbU188g%2B00E%2BvU7dSTyejdI0ZK6IAgMRtvMhI4MN%2FfkL0GOqUBzcaU6UUjRVdV%2Fa2lDqhJ3wc%2B4GsdXQky0xFD2Anik%2FhGr5ajKzw7OhjQgDNbRDLmkpQG2t42AaSRecX8Ff8plBvn0odoYais62LwPgcekZiOt9tWxoD4jaJHuz%2Fwtfesq5qq7EfyhkZXosMtgYtaidBJVTfo6%2Beq3YYJNx4FA9NSpyJ7eE8mu1crHvl0cqLmB674ZJAuWZJuo9fwi%2FM9bfB9Ey6o&X-Amz-Signature=683cba5fc84abd5cbe3711449bc76ff3b1affb2321f201bb5f1c0f04111d5a0f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675A6PGIB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHBP%2FLShF5KtsHhr28SYv1cxoWD205S3r3Tj387NxaGuAiEA0OFF44gyQSU8RBjNBWuKMx792Mtd96AcpVVEdS5hOwgq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDJs3BUNXifO3NwaY8yrcA1%2BgPrSxZbbACVUGNzCo0qH%2BAULEM%2FNCbPaiIWybUVAL1yCBwTbnNvYLQpcUVf8YFaihxwaeESU1dNztthUF8xzfYv9cYq%2FUw6wRA1gLut%2F5Tnqiw3e1WGME%2BmvzhQPwXb1BC11u1RBL6SbqcczYuTKT2naD3dl0HmGFM1z4oLH8fzbtilT5EK0zlIwRhe2FKNkh1fnrz0noSp97U1MKRfjs7JKRdC4wW%2BpCKLlLr2pnlGUEkzV1vZccIfZDG415qW7ZuoqaO9WC1VGLpuEpEYO%2BPnAt38X6v9wy27aj117R3e%2BpK0%2FO1uH7%2B4JiImeYBxt7WLZEs827Ni9LODa9xgWBQut5rPv6BrsWBFedmxCGj48paF31YTSJPACig%2FEGsEQYXhEPPaZGMquj7q3r2cpTkr7FISbnynrIH7Yh6DVgIJTAQPf4eDxXvSZ7k1Poixs%2BSBMHRBQQtazD10CrXf164Fo28e2uZjxaek2LzPEVd7jl2rYZDIT7Z1jpi62Y3j0LbM5qcRni%2FwtoIpA0Hta1hdvFBeSI9%2Bi96I2R0OX%2FesaLE%2BkbVMIb%2B0sWwQQN5UdgOkIBiaOn%2Fal210wVGWMbU188g%2B00E%2BvU7dSTyejdI0ZK6IAgMRtvMhI4MN%2FfkL0GOqUBzcaU6UUjRVdV%2Fa2lDqhJ3wc%2B4GsdXQky0xFD2Anik%2FhGr5ajKzw7OhjQgDNbRDLmkpQG2t42AaSRecX8Ff8plBvn0odoYais62LwPgcekZiOt9tWxoD4jaJHuz%2Fwtfesq5qq7EfyhkZXosMtgYtaidBJVTfo6%2Beq3YYJNx4FA9NSpyJ7eE8mu1crHvl0cqLmB674ZJAuWZJuo9fwi%2FM9bfB9Ey6o&X-Amz-Signature=43deebccc3e18ce77e0d79dd625a695ccb2d76e512fb969c23afe29a59435a30&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675A6PGIB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHBP%2FLShF5KtsHhr28SYv1cxoWD205S3r3Tj387NxaGuAiEA0OFF44gyQSU8RBjNBWuKMx792Mtd96AcpVVEdS5hOwgq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDJs3BUNXifO3NwaY8yrcA1%2BgPrSxZbbACVUGNzCo0qH%2BAULEM%2FNCbPaiIWybUVAL1yCBwTbnNvYLQpcUVf8YFaihxwaeESU1dNztthUF8xzfYv9cYq%2FUw6wRA1gLut%2F5Tnqiw3e1WGME%2BmvzhQPwXb1BC11u1RBL6SbqcczYuTKT2naD3dl0HmGFM1z4oLH8fzbtilT5EK0zlIwRhe2FKNkh1fnrz0noSp97U1MKRfjs7JKRdC4wW%2BpCKLlLr2pnlGUEkzV1vZccIfZDG415qW7ZuoqaO9WC1VGLpuEpEYO%2BPnAt38X6v9wy27aj117R3e%2BpK0%2FO1uH7%2B4JiImeYBxt7WLZEs827Ni9LODa9xgWBQut5rPv6BrsWBFedmxCGj48paF31YTSJPACig%2FEGsEQYXhEPPaZGMquj7q3r2cpTkr7FISbnynrIH7Yh6DVgIJTAQPf4eDxXvSZ7k1Poixs%2BSBMHRBQQtazD10CrXf164Fo28e2uZjxaek2LzPEVd7jl2rYZDIT7Z1jpi62Y3j0LbM5qcRni%2FwtoIpA0Hta1hdvFBeSI9%2Bi96I2R0OX%2FesaLE%2BkbVMIb%2B0sWwQQN5UdgOkIBiaOn%2Fal210wVGWMbU188g%2B00E%2BvU7dSTyejdI0ZK6IAgMRtvMhI4MN%2FfkL0GOqUBzcaU6UUjRVdV%2Fa2lDqhJ3wc%2B4GsdXQky0xFD2Anik%2FhGr5ajKzw7OhjQgDNbRDLmkpQG2t42AaSRecX8Ff8plBvn0odoYais62LwPgcekZiOt9tWxoD4jaJHuz%2Fwtfesq5qq7EfyhkZXosMtgYtaidBJVTfo6%2Beq3YYJNx4FA9NSpyJ7eE8mu1crHvl0cqLmB674ZJAuWZJuo9fwi%2FM9bfB9Ey6o&X-Amz-Signature=68c17865dfb02836d7305867792366727941f84290cf861c27dd8499e5ab5acb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675A6PGIB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHBP%2FLShF5KtsHhr28SYv1cxoWD205S3r3Tj387NxaGuAiEA0OFF44gyQSU8RBjNBWuKMx792Mtd96AcpVVEdS5hOwgq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDJs3BUNXifO3NwaY8yrcA1%2BgPrSxZbbACVUGNzCo0qH%2BAULEM%2FNCbPaiIWybUVAL1yCBwTbnNvYLQpcUVf8YFaihxwaeESU1dNztthUF8xzfYv9cYq%2FUw6wRA1gLut%2F5Tnqiw3e1WGME%2BmvzhQPwXb1BC11u1RBL6SbqcczYuTKT2naD3dl0HmGFM1z4oLH8fzbtilT5EK0zlIwRhe2FKNkh1fnrz0noSp97U1MKRfjs7JKRdC4wW%2BpCKLlLr2pnlGUEkzV1vZccIfZDG415qW7ZuoqaO9WC1VGLpuEpEYO%2BPnAt38X6v9wy27aj117R3e%2BpK0%2FO1uH7%2B4JiImeYBxt7WLZEs827Ni9LODa9xgWBQut5rPv6BrsWBFedmxCGj48paF31YTSJPACig%2FEGsEQYXhEPPaZGMquj7q3r2cpTkr7FISbnynrIH7Yh6DVgIJTAQPf4eDxXvSZ7k1Poixs%2BSBMHRBQQtazD10CrXf164Fo28e2uZjxaek2LzPEVd7jl2rYZDIT7Z1jpi62Y3j0LbM5qcRni%2FwtoIpA0Hta1hdvFBeSI9%2Bi96I2R0OX%2FesaLE%2BkbVMIb%2B0sWwQQN5UdgOkIBiaOn%2Fal210wVGWMbU188g%2B00E%2BvU7dSTyejdI0ZK6IAgMRtvMhI4MN%2FfkL0GOqUBzcaU6UUjRVdV%2Fa2lDqhJ3wc%2B4GsdXQky0xFD2Anik%2FhGr5ajKzw7OhjQgDNbRDLmkpQG2t42AaSRecX8Ff8plBvn0odoYais62LwPgcekZiOt9tWxoD4jaJHuz%2Fwtfesq5qq7EfyhkZXosMtgYtaidBJVTfo6%2Beq3YYJNx4FA9NSpyJ7eE8mu1crHvl0cqLmB674ZJAuWZJuo9fwi%2FM9bfB9Ey6o&X-Amz-Signature=eea712aa3d4d7d2456ebf18fe84df24e66847de1ab1a0bf440610c9b60d9b51b&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675A6PGIB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHBP%2FLShF5KtsHhr28SYv1cxoWD205S3r3Tj387NxaGuAiEA0OFF44gyQSU8RBjNBWuKMx792Mtd96AcpVVEdS5hOwgq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDJs3BUNXifO3NwaY8yrcA1%2BgPrSxZbbACVUGNzCo0qH%2BAULEM%2FNCbPaiIWybUVAL1yCBwTbnNvYLQpcUVf8YFaihxwaeESU1dNztthUF8xzfYv9cYq%2FUw6wRA1gLut%2F5Tnqiw3e1WGME%2BmvzhQPwXb1BC11u1RBL6SbqcczYuTKT2naD3dl0HmGFM1z4oLH8fzbtilT5EK0zlIwRhe2FKNkh1fnrz0noSp97U1MKRfjs7JKRdC4wW%2BpCKLlLr2pnlGUEkzV1vZccIfZDG415qW7ZuoqaO9WC1VGLpuEpEYO%2BPnAt38X6v9wy27aj117R3e%2BpK0%2FO1uH7%2B4JiImeYBxt7WLZEs827Ni9LODa9xgWBQut5rPv6BrsWBFedmxCGj48paF31YTSJPACig%2FEGsEQYXhEPPaZGMquj7q3r2cpTkr7FISbnynrIH7Yh6DVgIJTAQPf4eDxXvSZ7k1Poixs%2BSBMHRBQQtazD10CrXf164Fo28e2uZjxaek2LzPEVd7jl2rYZDIT7Z1jpi62Y3j0LbM5qcRni%2FwtoIpA0Hta1hdvFBeSI9%2Bi96I2R0OX%2FesaLE%2BkbVMIb%2B0sWwQQN5UdgOkIBiaOn%2Fal210wVGWMbU188g%2B00E%2BvU7dSTyejdI0ZK6IAgMRtvMhI4MN%2FfkL0GOqUBzcaU6UUjRVdV%2Fa2lDqhJ3wc%2B4GsdXQky0xFD2Anik%2FhGr5ajKzw7OhjQgDNbRDLmkpQG2t42AaSRecX8Ff8plBvn0odoYais62LwPgcekZiOt9tWxoD4jaJHuz%2Fwtfesq5qq7EfyhkZXosMtgYtaidBJVTfo6%2Beq3YYJNx4FA9NSpyJ7eE8mu1crHvl0cqLmB674ZJAuWZJuo9fwi%2FM9bfB9Ey6o&X-Amz-Signature=b637a62095a95f64046f081dbbc1119c467da664d8b4313112e0eaf624540b06&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675A6PGIB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHBP%2FLShF5KtsHhr28SYv1cxoWD205S3r3Tj387NxaGuAiEA0OFF44gyQSU8RBjNBWuKMx792Mtd96AcpVVEdS5hOwgq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDJs3BUNXifO3NwaY8yrcA1%2BgPrSxZbbACVUGNzCo0qH%2BAULEM%2FNCbPaiIWybUVAL1yCBwTbnNvYLQpcUVf8YFaihxwaeESU1dNztthUF8xzfYv9cYq%2FUw6wRA1gLut%2F5Tnqiw3e1WGME%2BmvzhQPwXb1BC11u1RBL6SbqcczYuTKT2naD3dl0HmGFM1z4oLH8fzbtilT5EK0zlIwRhe2FKNkh1fnrz0noSp97U1MKRfjs7JKRdC4wW%2BpCKLlLr2pnlGUEkzV1vZccIfZDG415qW7ZuoqaO9WC1VGLpuEpEYO%2BPnAt38X6v9wy27aj117R3e%2BpK0%2FO1uH7%2B4JiImeYBxt7WLZEs827Ni9LODa9xgWBQut5rPv6BrsWBFedmxCGj48paF31YTSJPACig%2FEGsEQYXhEPPaZGMquj7q3r2cpTkr7FISbnynrIH7Yh6DVgIJTAQPf4eDxXvSZ7k1Poixs%2BSBMHRBQQtazD10CrXf164Fo28e2uZjxaek2LzPEVd7jl2rYZDIT7Z1jpi62Y3j0LbM5qcRni%2FwtoIpA0Hta1hdvFBeSI9%2Bi96I2R0OX%2FesaLE%2BkbVMIb%2B0sWwQQN5UdgOkIBiaOn%2Fal210wVGWMbU188g%2B00E%2BvU7dSTyejdI0ZK6IAgMRtvMhI4MN%2FfkL0GOqUBzcaU6UUjRVdV%2Fa2lDqhJ3wc%2B4GsdXQky0xFD2Anik%2FhGr5ajKzw7OhjQgDNbRDLmkpQG2t42AaSRecX8Ff8plBvn0odoYais62LwPgcekZiOt9tWxoD4jaJHuz%2Fwtfesq5qq7EfyhkZXosMtgYtaidBJVTfo6%2Beq3YYJNx4FA9NSpyJ7eE8mu1crHvl0cqLmB674ZJAuWZJuo9fwi%2FM9bfB9Ey6o&X-Amz-Signature=8d104045aef646891d5df8116fef015397ba429cb7bfe7bd74d241532e0af63d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675A6PGIB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHBP%2FLShF5KtsHhr28SYv1cxoWD205S3r3Tj387NxaGuAiEA0OFF44gyQSU8RBjNBWuKMx792Mtd96AcpVVEdS5hOwgq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDJs3BUNXifO3NwaY8yrcA1%2BgPrSxZbbACVUGNzCo0qH%2BAULEM%2FNCbPaiIWybUVAL1yCBwTbnNvYLQpcUVf8YFaihxwaeESU1dNztthUF8xzfYv9cYq%2FUw6wRA1gLut%2F5Tnqiw3e1WGME%2BmvzhQPwXb1BC11u1RBL6SbqcczYuTKT2naD3dl0HmGFM1z4oLH8fzbtilT5EK0zlIwRhe2FKNkh1fnrz0noSp97U1MKRfjs7JKRdC4wW%2BpCKLlLr2pnlGUEkzV1vZccIfZDG415qW7ZuoqaO9WC1VGLpuEpEYO%2BPnAt38X6v9wy27aj117R3e%2BpK0%2FO1uH7%2B4JiImeYBxt7WLZEs827Ni9LODa9xgWBQut5rPv6BrsWBFedmxCGj48paF31YTSJPACig%2FEGsEQYXhEPPaZGMquj7q3r2cpTkr7FISbnynrIH7Yh6DVgIJTAQPf4eDxXvSZ7k1Poixs%2BSBMHRBQQtazD10CrXf164Fo28e2uZjxaek2LzPEVd7jl2rYZDIT7Z1jpi62Y3j0LbM5qcRni%2FwtoIpA0Hta1hdvFBeSI9%2Bi96I2R0OX%2FesaLE%2BkbVMIb%2B0sWwQQN5UdgOkIBiaOn%2Fal210wVGWMbU188g%2B00E%2BvU7dSTyejdI0ZK6IAgMRtvMhI4MN%2FfkL0GOqUBzcaU6UUjRVdV%2Fa2lDqhJ3wc%2B4GsdXQky0xFD2Anik%2FhGr5ajKzw7OhjQgDNbRDLmkpQG2t42AaSRecX8Ff8plBvn0odoYais62LwPgcekZiOt9tWxoD4jaJHuz%2Fwtfesq5qq7EfyhkZXosMtgYtaidBJVTfo6%2Beq3YYJNx4FA9NSpyJ7eE8mu1crHvl0cqLmB674ZJAuWZJuo9fwi%2FM9bfB9Ey6o&X-Amz-Signature=2e2bebad54080fe63ae8fd8567c047dcfa5f487d47ee31ef3b37eb16f1238196&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675A6PGIB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHBP%2FLShF5KtsHhr28SYv1cxoWD205S3r3Tj387NxaGuAiEA0OFF44gyQSU8RBjNBWuKMx792Mtd96AcpVVEdS5hOwgq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDJs3BUNXifO3NwaY8yrcA1%2BgPrSxZbbACVUGNzCo0qH%2BAULEM%2FNCbPaiIWybUVAL1yCBwTbnNvYLQpcUVf8YFaihxwaeESU1dNztthUF8xzfYv9cYq%2FUw6wRA1gLut%2F5Tnqiw3e1WGME%2BmvzhQPwXb1BC11u1RBL6SbqcczYuTKT2naD3dl0HmGFM1z4oLH8fzbtilT5EK0zlIwRhe2FKNkh1fnrz0noSp97U1MKRfjs7JKRdC4wW%2BpCKLlLr2pnlGUEkzV1vZccIfZDG415qW7ZuoqaO9WC1VGLpuEpEYO%2BPnAt38X6v9wy27aj117R3e%2BpK0%2FO1uH7%2B4JiImeYBxt7WLZEs827Ni9LODa9xgWBQut5rPv6BrsWBFedmxCGj48paF31YTSJPACig%2FEGsEQYXhEPPaZGMquj7q3r2cpTkr7FISbnynrIH7Yh6DVgIJTAQPf4eDxXvSZ7k1Poixs%2BSBMHRBQQtazD10CrXf164Fo28e2uZjxaek2LzPEVd7jl2rYZDIT7Z1jpi62Y3j0LbM5qcRni%2FwtoIpA0Hta1hdvFBeSI9%2Bi96I2R0OX%2FesaLE%2BkbVMIb%2B0sWwQQN5UdgOkIBiaOn%2Fal210wVGWMbU188g%2B00E%2BvU7dSTyejdI0ZK6IAgMRtvMhI4MN%2FfkL0GOqUBzcaU6UUjRVdV%2Fa2lDqhJ3wc%2B4GsdXQky0xFD2Anik%2FhGr5ajKzw7OhjQgDNbRDLmkpQG2t42AaSRecX8Ff8plBvn0odoYais62LwPgcekZiOt9tWxoD4jaJHuz%2Fwtfesq5qq7EfyhkZXosMtgYtaidBJVTfo6%2Beq3YYJNx4FA9NSpyJ7eE8mu1crHvl0cqLmB674ZJAuWZJuo9fwi%2FM9bfB9Ey6o&X-Amz-Signature=84e8287055bd24c03169f243190cb7b2e982dbdcb230b35dfd2f2c0ed86a8f57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXC7JXDR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIGdVsLpQzEC3TJzHni63QGS97DzDrv4DZlXbGV471p0FAiEAxf9Z8YrZqwBK1JuEZ42ua7qWWa3iZ%2Bs7J9coqLBUrNkq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDEFKqLDiaHQUNI4CGCrcA3b2SK3%2BtW6lEvUT0RvMate%2BrddYanIagXthUhdIzPeT2MSpGy0arO5TKj4V2P6Z5XTM3c8TEDv6zz5gsrq0MduB8uKCf3JVsiB3KvqX5Nw%2BUVlFuMAi1EhD4Nmt8YguouC9%2BzXjRyd28OEcrd4LLx%2Fv5%2Be8XBvrMZ7Y971nh8e9rHkZXbXmzkn3fJ8NSi2FAnztcbovjlIGtmIRylJJnFmFrN7EFuvgQhzJTQQsjHLtF7r7%2B%2F%2FDNyNJxmyDBYT3O8mceSatwBJM0O3Kf%2BkNXbY%2FGOAKTl%2BCwqUekcfjlbuFGAXnOssTvvqicDruBZRLtdZ9TMV05XxtBd3ZWCjXifW94Yj3%2Bj8ehZVrfweSE8Gxwg0z4LGBvrLWiSWgiaVF%2FO8XPHTXdiG8qUEzACF3ENUpLTRdsO7bPlpubbkDEjh4jMAFoCexTm8k6cMclZsCpS6w7cTP7Rwo%2F2An3H41yuxOKCKtBB44J5gEzXN%2Bc6xqIxEGwZw%2FiA3YjEP11TEV%2F6nxGa%2FugvYVhPtOa%2FKvMG%2FiIfDmRhYFNXOYinenLnKak0E0wZwBjaJOEA7v3aEIzIcR6ok%2Fu%2BV9h1VUrKVmtQdcviiZhbmYOW%2Fv8qTaxSW69WM3n85TbQe0jJtKMMbgkL0GOqUBG0gplj1o4IWCrd0tGtWwXPbrxIkeV5mxW3F1E%2BTIvd1A7nMPeBJRpBhnGHwYlNFJwFYycsVY%2FrurxvE%2BFi%2BywyOZCExCFzdOIJeEg3vvCNYfs0KhTeAtIXFujzDAU0Wn%2FjOfLFOyZA9eQ8ytVqXEW0H9A7wEwAdC3%2FfkTSQkdLJzDfF6F0xa6Ti81gbF6j0WQjjKP8fvrsDHaElOlWiDGC5bT5yr&X-Amz-Signature=98966a3bd87565370bb1912b6c5e221e423e67d75896379cd5f3098ed2b292f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXC7JXDR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIGdVsLpQzEC3TJzHni63QGS97DzDrv4DZlXbGV471p0FAiEAxf9Z8YrZqwBK1JuEZ42ua7qWWa3iZ%2Bs7J9coqLBUrNkq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDEFKqLDiaHQUNI4CGCrcA3b2SK3%2BtW6lEvUT0RvMate%2BrddYanIagXthUhdIzPeT2MSpGy0arO5TKj4V2P6Z5XTM3c8TEDv6zz5gsrq0MduB8uKCf3JVsiB3KvqX5Nw%2BUVlFuMAi1EhD4Nmt8YguouC9%2BzXjRyd28OEcrd4LLx%2Fv5%2Be8XBvrMZ7Y971nh8e9rHkZXbXmzkn3fJ8NSi2FAnztcbovjlIGtmIRylJJnFmFrN7EFuvgQhzJTQQsjHLtF7r7%2B%2F%2FDNyNJxmyDBYT3O8mceSatwBJM0O3Kf%2BkNXbY%2FGOAKTl%2BCwqUekcfjlbuFGAXnOssTvvqicDruBZRLtdZ9TMV05XxtBd3ZWCjXifW94Yj3%2Bj8ehZVrfweSE8Gxwg0z4LGBvrLWiSWgiaVF%2FO8XPHTXdiG8qUEzACF3ENUpLTRdsO7bPlpubbkDEjh4jMAFoCexTm8k6cMclZsCpS6w7cTP7Rwo%2F2An3H41yuxOKCKtBB44J5gEzXN%2Bc6xqIxEGwZw%2FiA3YjEP11TEV%2F6nxGa%2FugvYVhPtOa%2FKvMG%2FiIfDmRhYFNXOYinenLnKak0E0wZwBjaJOEA7v3aEIzIcR6ok%2Fu%2BV9h1VUrKVmtQdcviiZhbmYOW%2Fv8qTaxSW69WM3n85TbQe0jJtKMMbgkL0GOqUBG0gplj1o4IWCrd0tGtWwXPbrxIkeV5mxW3F1E%2BTIvd1A7nMPeBJRpBhnGHwYlNFJwFYycsVY%2FrurxvE%2BFi%2BywyOZCExCFzdOIJeEg3vvCNYfs0KhTeAtIXFujzDAU0Wn%2FjOfLFOyZA9eQ8ytVqXEW0H9A7wEwAdC3%2FfkTSQkdLJzDfF6F0xa6Ti81gbF6j0WQjjKP8fvrsDHaElOlWiDGC5bT5yr&X-Amz-Signature=de3fd40c73de52bf693e8e3cfdbdbcbfd0c13d437d343e1452795bcfaafaa649&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
