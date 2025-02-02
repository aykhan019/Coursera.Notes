

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BHMJEUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvZrQqJYG7OZ6tuKhWtHGkx2saWCAzEMXVnyKocq9YEQIhAIHF8J5chsNqQY568WuR8lqC%2BBaRlWQhc03KJX5eHlU1KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGacSFoDGNkBdMTx0q3ANz7ESRp2AFteVZ3Xx3XzJDSLi0%2FNakeBu%2Bx8jEfMjgiTkwxuMeY7Y9CWf%2Fx%2FHn9OnEykpypxwes4rXv67a5cKhPgHrG9Rpmdc1tRuC5D9yr4wkgRWDrlveXF7w3bNmWp%2BZWaDdaf0%2BEcmDAYN%2FLrN9%2BVInL62wEP98Jwu94%2BlNiZMCo4ux8ykepcEUwpkcbhWA7MWOD%2Fwa%2BewJcVgTEfgQzmRTbbWP3xg8aLhG0oM%2BVzdWYbG5iBhS9gPtLlhdLKgPaoYDp%2Fr09%2BdC261Wg6I08ASjJDMSKXnuc9tnqI56EpPit4wb0gtmtXUUzCg7JIsScpbgskiR9gJJ9FscA842rnd23k5RSZOYGLkXaunM2imHWMif8j%2B0UgU5V%2BU4pI7q3h2jqq8k5rjfKcwbCauRWvdBqVacAfcDbYpjK31OQXCpjUvlR%2BgO51IRHiRHZO5ZSDjul8wzVLU57mtYx2vcVwx7h9nMEbwfs19L3rSMh6%2F5hRd%2F3FDCluccyb9TtNI%2BgfeU%2FYXnPY8kZ9S1GA9BVHjVpQGEgDrawkBPeRKueKi7QRHoubUf3cUA77mcwOM%2FG6m%2F2QsCqcraOfnWWynitHWuqEkRMBG6DAFTu3tXEqVyplAENLZpWR6BHTDam%2Fy8BjqkAeFFqtDTEgeKVUwtGZA3D%2B8KEOEsfFh7yW8LhX0FxTO%2BmV3Ewewoxr0CF%2FWnFhifszENQuuBhFTFyY%2FFA8UHnXE6a35c6eWp%2Bh1Ttln1M9DgwP%2BN3Vm%2BLkdPB0ZlWAb53J48s0h35JLq6Jfo0HuXI6uMjfCsMB1qBMwW%2BlXq5T77cm8R5lBM79RoiWFma5XJy3ui%2F3aHhPFKaZcfE3Q520iBAOzZ&X-Amz-Signature=62fe4843c2338b4f18f271b66f57e52cc06d18274bf243f3defa2aa7add376ce&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BHMJEUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvZrQqJYG7OZ6tuKhWtHGkx2saWCAzEMXVnyKocq9YEQIhAIHF8J5chsNqQY568WuR8lqC%2BBaRlWQhc03KJX5eHlU1KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGacSFoDGNkBdMTx0q3ANz7ESRp2AFteVZ3Xx3XzJDSLi0%2FNakeBu%2Bx8jEfMjgiTkwxuMeY7Y9CWf%2Fx%2FHn9OnEykpypxwes4rXv67a5cKhPgHrG9Rpmdc1tRuC5D9yr4wkgRWDrlveXF7w3bNmWp%2BZWaDdaf0%2BEcmDAYN%2FLrN9%2BVInL62wEP98Jwu94%2BlNiZMCo4ux8ykepcEUwpkcbhWA7MWOD%2Fwa%2BewJcVgTEfgQzmRTbbWP3xg8aLhG0oM%2BVzdWYbG5iBhS9gPtLlhdLKgPaoYDp%2Fr09%2BdC261Wg6I08ASjJDMSKXnuc9tnqI56EpPit4wb0gtmtXUUzCg7JIsScpbgskiR9gJJ9FscA842rnd23k5RSZOYGLkXaunM2imHWMif8j%2B0UgU5V%2BU4pI7q3h2jqq8k5rjfKcwbCauRWvdBqVacAfcDbYpjK31OQXCpjUvlR%2BgO51IRHiRHZO5ZSDjul8wzVLU57mtYx2vcVwx7h9nMEbwfs19L3rSMh6%2F5hRd%2F3FDCluccyb9TtNI%2BgfeU%2FYXnPY8kZ9S1GA9BVHjVpQGEgDrawkBPeRKueKi7QRHoubUf3cUA77mcwOM%2FG6m%2F2QsCqcraOfnWWynitHWuqEkRMBG6DAFTu3tXEqVyplAENLZpWR6BHTDam%2Fy8BjqkAeFFqtDTEgeKVUwtGZA3D%2B8KEOEsfFh7yW8LhX0FxTO%2BmV3Ewewoxr0CF%2FWnFhifszENQuuBhFTFyY%2FFA8UHnXE6a35c6eWp%2Bh1Ttln1M9DgwP%2BN3Vm%2BLkdPB0ZlWAb53J48s0h35JLq6Jfo0HuXI6uMjfCsMB1qBMwW%2BlXq5T77cm8R5lBM79RoiWFma5XJy3ui%2F3aHhPFKaZcfE3Q520iBAOzZ&X-Amz-Signature=7445cac299e3882ff1fa4c73e938aad30133ce6573facd5730510405ac76d039&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BHMJEUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvZrQqJYG7OZ6tuKhWtHGkx2saWCAzEMXVnyKocq9YEQIhAIHF8J5chsNqQY568WuR8lqC%2BBaRlWQhc03KJX5eHlU1KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGacSFoDGNkBdMTx0q3ANz7ESRp2AFteVZ3Xx3XzJDSLi0%2FNakeBu%2Bx8jEfMjgiTkwxuMeY7Y9CWf%2Fx%2FHn9OnEykpypxwes4rXv67a5cKhPgHrG9Rpmdc1tRuC5D9yr4wkgRWDrlveXF7w3bNmWp%2BZWaDdaf0%2BEcmDAYN%2FLrN9%2BVInL62wEP98Jwu94%2BlNiZMCo4ux8ykepcEUwpkcbhWA7MWOD%2Fwa%2BewJcVgTEfgQzmRTbbWP3xg8aLhG0oM%2BVzdWYbG5iBhS9gPtLlhdLKgPaoYDp%2Fr09%2BdC261Wg6I08ASjJDMSKXnuc9tnqI56EpPit4wb0gtmtXUUzCg7JIsScpbgskiR9gJJ9FscA842rnd23k5RSZOYGLkXaunM2imHWMif8j%2B0UgU5V%2BU4pI7q3h2jqq8k5rjfKcwbCauRWvdBqVacAfcDbYpjK31OQXCpjUvlR%2BgO51IRHiRHZO5ZSDjul8wzVLU57mtYx2vcVwx7h9nMEbwfs19L3rSMh6%2F5hRd%2F3FDCluccyb9TtNI%2BgfeU%2FYXnPY8kZ9S1GA9BVHjVpQGEgDrawkBPeRKueKi7QRHoubUf3cUA77mcwOM%2FG6m%2F2QsCqcraOfnWWynitHWuqEkRMBG6DAFTu3tXEqVyplAENLZpWR6BHTDam%2Fy8BjqkAeFFqtDTEgeKVUwtGZA3D%2B8KEOEsfFh7yW8LhX0FxTO%2BmV3Ewewoxr0CF%2FWnFhifszENQuuBhFTFyY%2FFA8UHnXE6a35c6eWp%2Bh1Ttln1M9DgwP%2BN3Vm%2BLkdPB0ZlWAb53J48s0h35JLq6Jfo0HuXI6uMjfCsMB1qBMwW%2BlXq5T77cm8R5lBM79RoiWFma5XJy3ui%2F3aHhPFKaZcfE3Q520iBAOzZ&X-Amz-Signature=d2f83ccd9db15c0a6fbb62e5b1e6150c36a769553d10158f3b49bbb9cbd1d57f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BHMJEUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvZrQqJYG7OZ6tuKhWtHGkx2saWCAzEMXVnyKocq9YEQIhAIHF8J5chsNqQY568WuR8lqC%2BBaRlWQhc03KJX5eHlU1KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGacSFoDGNkBdMTx0q3ANz7ESRp2AFteVZ3Xx3XzJDSLi0%2FNakeBu%2Bx8jEfMjgiTkwxuMeY7Y9CWf%2Fx%2FHn9OnEykpypxwes4rXv67a5cKhPgHrG9Rpmdc1tRuC5D9yr4wkgRWDrlveXF7w3bNmWp%2BZWaDdaf0%2BEcmDAYN%2FLrN9%2BVInL62wEP98Jwu94%2BlNiZMCo4ux8ykepcEUwpkcbhWA7MWOD%2Fwa%2BewJcVgTEfgQzmRTbbWP3xg8aLhG0oM%2BVzdWYbG5iBhS9gPtLlhdLKgPaoYDp%2Fr09%2BdC261Wg6I08ASjJDMSKXnuc9tnqI56EpPit4wb0gtmtXUUzCg7JIsScpbgskiR9gJJ9FscA842rnd23k5RSZOYGLkXaunM2imHWMif8j%2B0UgU5V%2BU4pI7q3h2jqq8k5rjfKcwbCauRWvdBqVacAfcDbYpjK31OQXCpjUvlR%2BgO51IRHiRHZO5ZSDjul8wzVLU57mtYx2vcVwx7h9nMEbwfs19L3rSMh6%2F5hRd%2F3FDCluccyb9TtNI%2BgfeU%2FYXnPY8kZ9S1GA9BVHjVpQGEgDrawkBPeRKueKi7QRHoubUf3cUA77mcwOM%2FG6m%2F2QsCqcraOfnWWynitHWuqEkRMBG6DAFTu3tXEqVyplAENLZpWR6BHTDam%2Fy8BjqkAeFFqtDTEgeKVUwtGZA3D%2B8KEOEsfFh7yW8LhX0FxTO%2BmV3Ewewoxr0CF%2FWnFhifszENQuuBhFTFyY%2FFA8UHnXE6a35c6eWp%2Bh1Ttln1M9DgwP%2BN3Vm%2BLkdPB0ZlWAb53J48s0h35JLq6Jfo0HuXI6uMjfCsMB1qBMwW%2BlXq5T77cm8R5lBM79RoiWFma5XJy3ui%2F3aHhPFKaZcfE3Q520iBAOzZ&X-Amz-Signature=221ffa11b68492d4bdcb85da9f0e786a4ed9ac210bc528cd586f32882aa03258&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BHMJEUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvZrQqJYG7OZ6tuKhWtHGkx2saWCAzEMXVnyKocq9YEQIhAIHF8J5chsNqQY568WuR8lqC%2BBaRlWQhc03KJX5eHlU1KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGacSFoDGNkBdMTx0q3ANz7ESRp2AFteVZ3Xx3XzJDSLi0%2FNakeBu%2Bx8jEfMjgiTkwxuMeY7Y9CWf%2Fx%2FHn9OnEykpypxwes4rXv67a5cKhPgHrG9Rpmdc1tRuC5D9yr4wkgRWDrlveXF7w3bNmWp%2BZWaDdaf0%2BEcmDAYN%2FLrN9%2BVInL62wEP98Jwu94%2BlNiZMCo4ux8ykepcEUwpkcbhWA7MWOD%2Fwa%2BewJcVgTEfgQzmRTbbWP3xg8aLhG0oM%2BVzdWYbG5iBhS9gPtLlhdLKgPaoYDp%2Fr09%2BdC261Wg6I08ASjJDMSKXnuc9tnqI56EpPit4wb0gtmtXUUzCg7JIsScpbgskiR9gJJ9FscA842rnd23k5RSZOYGLkXaunM2imHWMif8j%2B0UgU5V%2BU4pI7q3h2jqq8k5rjfKcwbCauRWvdBqVacAfcDbYpjK31OQXCpjUvlR%2BgO51IRHiRHZO5ZSDjul8wzVLU57mtYx2vcVwx7h9nMEbwfs19L3rSMh6%2F5hRd%2F3FDCluccyb9TtNI%2BgfeU%2FYXnPY8kZ9S1GA9BVHjVpQGEgDrawkBPeRKueKi7QRHoubUf3cUA77mcwOM%2FG6m%2F2QsCqcraOfnWWynitHWuqEkRMBG6DAFTu3tXEqVyplAENLZpWR6BHTDam%2Fy8BjqkAeFFqtDTEgeKVUwtGZA3D%2B8KEOEsfFh7yW8LhX0FxTO%2BmV3Ewewoxr0CF%2FWnFhifszENQuuBhFTFyY%2FFA8UHnXE6a35c6eWp%2Bh1Ttln1M9DgwP%2BN3Vm%2BLkdPB0ZlWAb53J48s0h35JLq6Jfo0HuXI6uMjfCsMB1qBMwW%2BlXq5T77cm8R5lBM79RoiWFma5XJy3ui%2F3aHhPFKaZcfE3Q520iBAOzZ&X-Amz-Signature=c5758c6fbf9ad91af4d7ae20d0d0f3aaf85d97f6de2ce6e418e2b7bca88a878f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BHMJEUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvZrQqJYG7OZ6tuKhWtHGkx2saWCAzEMXVnyKocq9YEQIhAIHF8J5chsNqQY568WuR8lqC%2BBaRlWQhc03KJX5eHlU1KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGacSFoDGNkBdMTx0q3ANz7ESRp2AFteVZ3Xx3XzJDSLi0%2FNakeBu%2Bx8jEfMjgiTkwxuMeY7Y9CWf%2Fx%2FHn9OnEykpypxwes4rXv67a5cKhPgHrG9Rpmdc1tRuC5D9yr4wkgRWDrlveXF7w3bNmWp%2BZWaDdaf0%2BEcmDAYN%2FLrN9%2BVInL62wEP98Jwu94%2BlNiZMCo4ux8ykepcEUwpkcbhWA7MWOD%2Fwa%2BewJcVgTEfgQzmRTbbWP3xg8aLhG0oM%2BVzdWYbG5iBhS9gPtLlhdLKgPaoYDp%2Fr09%2BdC261Wg6I08ASjJDMSKXnuc9tnqI56EpPit4wb0gtmtXUUzCg7JIsScpbgskiR9gJJ9FscA842rnd23k5RSZOYGLkXaunM2imHWMif8j%2B0UgU5V%2BU4pI7q3h2jqq8k5rjfKcwbCauRWvdBqVacAfcDbYpjK31OQXCpjUvlR%2BgO51IRHiRHZO5ZSDjul8wzVLU57mtYx2vcVwx7h9nMEbwfs19L3rSMh6%2F5hRd%2F3FDCluccyb9TtNI%2BgfeU%2FYXnPY8kZ9S1GA9BVHjVpQGEgDrawkBPeRKueKi7QRHoubUf3cUA77mcwOM%2FG6m%2F2QsCqcraOfnWWynitHWuqEkRMBG6DAFTu3tXEqVyplAENLZpWR6BHTDam%2Fy8BjqkAeFFqtDTEgeKVUwtGZA3D%2B8KEOEsfFh7yW8LhX0FxTO%2BmV3Ewewoxr0CF%2FWnFhifszENQuuBhFTFyY%2FFA8UHnXE6a35c6eWp%2Bh1Ttln1M9DgwP%2BN3Vm%2BLkdPB0ZlWAb53J48s0h35JLq6Jfo0HuXI6uMjfCsMB1qBMwW%2BlXq5T77cm8R5lBM79RoiWFma5XJy3ui%2F3aHhPFKaZcfE3Q520iBAOzZ&X-Amz-Signature=c80e931a037bb49e57fcbc809e8d180149aeedeb4d8e92ef60472b05013d6134&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BHMJEUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvZrQqJYG7OZ6tuKhWtHGkx2saWCAzEMXVnyKocq9YEQIhAIHF8J5chsNqQY568WuR8lqC%2BBaRlWQhc03KJX5eHlU1KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGacSFoDGNkBdMTx0q3ANz7ESRp2AFteVZ3Xx3XzJDSLi0%2FNakeBu%2Bx8jEfMjgiTkwxuMeY7Y9CWf%2Fx%2FHn9OnEykpypxwes4rXv67a5cKhPgHrG9Rpmdc1tRuC5D9yr4wkgRWDrlveXF7w3bNmWp%2BZWaDdaf0%2BEcmDAYN%2FLrN9%2BVInL62wEP98Jwu94%2BlNiZMCo4ux8ykepcEUwpkcbhWA7MWOD%2Fwa%2BewJcVgTEfgQzmRTbbWP3xg8aLhG0oM%2BVzdWYbG5iBhS9gPtLlhdLKgPaoYDp%2Fr09%2BdC261Wg6I08ASjJDMSKXnuc9tnqI56EpPit4wb0gtmtXUUzCg7JIsScpbgskiR9gJJ9FscA842rnd23k5RSZOYGLkXaunM2imHWMif8j%2B0UgU5V%2BU4pI7q3h2jqq8k5rjfKcwbCauRWvdBqVacAfcDbYpjK31OQXCpjUvlR%2BgO51IRHiRHZO5ZSDjul8wzVLU57mtYx2vcVwx7h9nMEbwfs19L3rSMh6%2F5hRd%2F3FDCluccyb9TtNI%2BgfeU%2FYXnPY8kZ9S1GA9BVHjVpQGEgDrawkBPeRKueKi7QRHoubUf3cUA77mcwOM%2FG6m%2F2QsCqcraOfnWWynitHWuqEkRMBG6DAFTu3tXEqVyplAENLZpWR6BHTDam%2Fy8BjqkAeFFqtDTEgeKVUwtGZA3D%2B8KEOEsfFh7yW8LhX0FxTO%2BmV3Ewewoxr0CF%2FWnFhifszENQuuBhFTFyY%2FFA8UHnXE6a35c6eWp%2Bh1Ttln1M9DgwP%2BN3Vm%2BLkdPB0ZlWAb53J48s0h35JLq6Jfo0HuXI6uMjfCsMB1qBMwW%2BlXq5T77cm8R5lBM79RoiWFma5XJy3ui%2F3aHhPFKaZcfE3Q520iBAOzZ&X-Amz-Signature=73a3a4b0d0435ede5afda28e3551eaa0b8ea6d8f94d376d5f793fd4225def38b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BHMJEUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvZrQqJYG7OZ6tuKhWtHGkx2saWCAzEMXVnyKocq9YEQIhAIHF8J5chsNqQY568WuR8lqC%2BBaRlWQhc03KJX5eHlU1KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGacSFoDGNkBdMTx0q3ANz7ESRp2AFteVZ3Xx3XzJDSLi0%2FNakeBu%2Bx8jEfMjgiTkwxuMeY7Y9CWf%2Fx%2FHn9OnEykpypxwes4rXv67a5cKhPgHrG9Rpmdc1tRuC5D9yr4wkgRWDrlveXF7w3bNmWp%2BZWaDdaf0%2BEcmDAYN%2FLrN9%2BVInL62wEP98Jwu94%2BlNiZMCo4ux8ykepcEUwpkcbhWA7MWOD%2Fwa%2BewJcVgTEfgQzmRTbbWP3xg8aLhG0oM%2BVzdWYbG5iBhS9gPtLlhdLKgPaoYDp%2Fr09%2BdC261Wg6I08ASjJDMSKXnuc9tnqI56EpPit4wb0gtmtXUUzCg7JIsScpbgskiR9gJJ9FscA842rnd23k5RSZOYGLkXaunM2imHWMif8j%2B0UgU5V%2BU4pI7q3h2jqq8k5rjfKcwbCauRWvdBqVacAfcDbYpjK31OQXCpjUvlR%2BgO51IRHiRHZO5ZSDjul8wzVLU57mtYx2vcVwx7h9nMEbwfs19L3rSMh6%2F5hRd%2F3FDCluccyb9TtNI%2BgfeU%2FYXnPY8kZ9S1GA9BVHjVpQGEgDrawkBPeRKueKi7QRHoubUf3cUA77mcwOM%2FG6m%2F2QsCqcraOfnWWynitHWuqEkRMBG6DAFTu3tXEqVyplAENLZpWR6BHTDam%2Fy8BjqkAeFFqtDTEgeKVUwtGZA3D%2B8KEOEsfFh7yW8LhX0FxTO%2BmV3Ewewoxr0CF%2FWnFhifszENQuuBhFTFyY%2FFA8UHnXE6a35c6eWp%2Bh1Ttln1M9DgwP%2BN3Vm%2BLkdPB0ZlWAb53J48s0h35JLq6Jfo0HuXI6uMjfCsMB1qBMwW%2BlXq5T77cm8R5lBM79RoiWFma5XJy3ui%2F3aHhPFKaZcfE3Q520iBAOzZ&X-Amz-Signature=9f6fe8928d1ca1ee0bdc7a896793ad5e747d0d05fa0aa002378b66a88a6c259f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BHMJEUJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvZrQqJYG7OZ6tuKhWtHGkx2saWCAzEMXVnyKocq9YEQIhAIHF8J5chsNqQY568WuR8lqC%2BBaRlWQhc03KJX5eHlU1KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGacSFoDGNkBdMTx0q3ANz7ESRp2AFteVZ3Xx3XzJDSLi0%2FNakeBu%2Bx8jEfMjgiTkwxuMeY7Y9CWf%2Fx%2FHn9OnEykpypxwes4rXv67a5cKhPgHrG9Rpmdc1tRuC5D9yr4wkgRWDrlveXF7w3bNmWp%2BZWaDdaf0%2BEcmDAYN%2FLrN9%2BVInL62wEP98Jwu94%2BlNiZMCo4ux8ykepcEUwpkcbhWA7MWOD%2Fwa%2BewJcVgTEfgQzmRTbbWP3xg8aLhG0oM%2BVzdWYbG5iBhS9gPtLlhdLKgPaoYDp%2Fr09%2BdC261Wg6I08ASjJDMSKXnuc9tnqI56EpPit4wb0gtmtXUUzCg7JIsScpbgskiR9gJJ9FscA842rnd23k5RSZOYGLkXaunM2imHWMif8j%2B0UgU5V%2BU4pI7q3h2jqq8k5rjfKcwbCauRWvdBqVacAfcDbYpjK31OQXCpjUvlR%2BgO51IRHiRHZO5ZSDjul8wzVLU57mtYx2vcVwx7h9nMEbwfs19L3rSMh6%2F5hRd%2F3FDCluccyb9TtNI%2BgfeU%2FYXnPY8kZ9S1GA9BVHjVpQGEgDrawkBPeRKueKi7QRHoubUf3cUA77mcwOM%2FG6m%2F2QsCqcraOfnWWynitHWuqEkRMBG6DAFTu3tXEqVyplAENLZpWR6BHTDam%2Fy8BjqkAeFFqtDTEgeKVUwtGZA3D%2B8KEOEsfFh7yW8LhX0FxTO%2BmV3Ewewoxr0CF%2FWnFhifszENQuuBhFTFyY%2FFA8UHnXE6a35c6eWp%2Bh1Ttln1M9DgwP%2BN3Vm%2BLkdPB0ZlWAb53J48s0h35JLq6Jfo0HuXI6uMjfCsMB1qBMwW%2BlXq5T77cm8R5lBM79RoiWFma5XJy3ui%2F3aHhPFKaZcfE3Q520iBAOzZ&X-Amz-Signature=a2ddad0c371c15d26179313b0110f06106d7f53bdfcc982dea08f82d1ffbd2ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXYIP7HW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3MIS4NqY5iJwf7YiD%2FtrCMZh8PnPyxIPPbw0tOvtjNAIgRyWAd%2FAtft%2F1sPe4tc1v8YJZg%2BPu2K4fhBt4roZIF3kqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELKi0OCHJKI5boWdCrcA1fo2RHW8UMM55bBz5NxFA5ip%2BFcCQLcUOvZr2%2BIqQPotLorOaquST5J3JdYZqtt2aHoIIbZIV3VUEkKw5wL3gzBnEl2kOlZdOefewiw%2BC0PHTc1kfFlhxOvLukd84SsXpokxeMOQUJwSVSZM6FGd%2BiC5xCj0k%2BKDH7TKVvwP%2BpO5zfIHqVDLhUNO7z%2BUAaTLiNTor830%2F1ZHIC50Sv458hCDgDln9mMGuEnnevZLzqr%2Fn7Ga71yrXJq%2F0zjYNnri5v2UYZJDJJeTapO7diCBkzyCPIKd0zbt%2FykHJHj%2B5ImWzELQB5f7Xbbey0O8tyMNMRmvoXXQsV5hN0MAF3%2FgnX%2BvLnhy94WIoMHnd642VSlp2yJEdshd5ZVKM1uN4Pj6OBRs1fCwHIC278IYzvdA34NX88QPyKcmzTLNNM%2BZN8JbFcL1YWSJQdTR1%2BasTvePOYH1JuiRjjQ%2FYfqXSF3U58Nwzmn%2FKOD6R3abW3ywxelwJUtmu9gh5wm7e4nHsdr23B2fG0fydlrIX%2Fvh1wGWNyS284MLlmEbep%2BD%2ByybrD4MXn3CFzivyREA6EC0UbRZa%2Fplmct8lhKi3lGRjfesSzSOTrs6JocbxgJ98UoPENLPEXy5PKWNRyUARaWMJac%2FLwGOqUBafQnDKI5lrKKe68tB%2FfAP8wakOmByVUZ9YCYdoGhKEneYNdecdtO1l%2FQ81fkXvnnVER2mTevW764RRgFKI3SmQcueh5SGGlSrsIhT6RNnEqQwKGmJKsN3Kl0ONvNMDO5Hi8Mt5izYJLaL%2BE%2FMXxy2RYNeW0zMrnL1sB4CGTfG3gLFKWHKb%2Fw4qa%2FxC34iEgUsY5rc9B1tCsH8ouQH6Sceiy4yaUQ&X-Amz-Signature=477cd9c1dbf35d80a81068d75f01d8398379e4b1b3279f5750a52c8b01748349&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXYIP7HW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3MIS4NqY5iJwf7YiD%2FtrCMZh8PnPyxIPPbw0tOvtjNAIgRyWAd%2FAtft%2F1sPe4tc1v8YJZg%2BPu2K4fhBt4roZIF3kqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELKi0OCHJKI5boWdCrcA1fo2RHW8UMM55bBz5NxFA5ip%2BFcCQLcUOvZr2%2BIqQPotLorOaquST5J3JdYZqtt2aHoIIbZIV3VUEkKw5wL3gzBnEl2kOlZdOefewiw%2BC0PHTc1kfFlhxOvLukd84SsXpokxeMOQUJwSVSZM6FGd%2BiC5xCj0k%2BKDH7TKVvwP%2BpO5zfIHqVDLhUNO7z%2BUAaTLiNTor830%2F1ZHIC50Sv458hCDgDln9mMGuEnnevZLzqr%2Fn7Ga71yrXJq%2F0zjYNnri5v2UYZJDJJeTapO7diCBkzyCPIKd0zbt%2FykHJHj%2B5ImWzELQB5f7Xbbey0O8tyMNMRmvoXXQsV5hN0MAF3%2FgnX%2BvLnhy94WIoMHnd642VSlp2yJEdshd5ZVKM1uN4Pj6OBRs1fCwHIC278IYzvdA34NX88QPyKcmzTLNNM%2BZN8JbFcL1YWSJQdTR1%2BasTvePOYH1JuiRjjQ%2FYfqXSF3U58Nwzmn%2FKOD6R3abW3ywxelwJUtmu9gh5wm7e4nHsdr23B2fG0fydlrIX%2Fvh1wGWNyS284MLlmEbep%2BD%2ByybrD4MXn3CFzivyREA6EC0UbRZa%2Fplmct8lhKi3lGRjfesSzSOTrs6JocbxgJ98UoPENLPEXy5PKWNRyUARaWMJac%2FLwGOqUBafQnDKI5lrKKe68tB%2FfAP8wakOmByVUZ9YCYdoGhKEneYNdecdtO1l%2FQ81fkXvnnVER2mTevW764RRgFKI3SmQcueh5SGGlSrsIhT6RNnEqQwKGmJKsN3Kl0ONvNMDO5Hi8Mt5izYJLaL%2BE%2FMXxy2RYNeW0zMrnL1sB4CGTfG3gLFKWHKb%2Fw4qa%2FxC34iEgUsY5rc9B1tCsH8ouQH6Sceiy4yaUQ&X-Amz-Signature=b1f20d16829a09fa7ee57a146536ab2644f1dc1afa0d4c68df1c1aac7b441d43&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
