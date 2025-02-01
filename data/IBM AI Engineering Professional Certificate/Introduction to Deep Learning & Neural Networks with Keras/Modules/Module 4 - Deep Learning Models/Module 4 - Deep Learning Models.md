

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QHKU7VH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyArHCqduNDkc0YqhIs%2B47rujcZD9VdNm8jC%2B8paNiJAIhANGMCXRC3q18OU6bxbEjRyL6%2BHthywIYwqbs6ZRd1Ky%2FKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSK2p%2Fj6V35EvDK%2Bsq3ANCgn4qx2sTSL%2BnUoNxqenIJvp3ICbkAoL1t28Jn3SOdLpcMhT7hnMMtykbCf0Ha71ttknnuTz7AY9TsuU4IJfRGYljvzn7wiy%2FZhByjayAQiEhXecMV0QwqgeCGFSo%2Bx85nn1ZwfayHbYvCd1oL%2F7lcQtKyJVy7EBOfHGBizXGjFwZk%2FnGERlyCT5BrvlpSkBb5iUk1uIAajZBiHfkWGwB8su%2FFMllUX%2Bx9mrAa6G4S88NX2liS3bwPFIIxEEVJ2BtpCmEtNivJJVtweN%2F3Iy4otyOJqh%2FT%2FaEtFQ5ZKwQGtcPZ6cKb8cDEPBbiLy6HZmU2nKPliVqh4055X8HiOc4U2tkSKnQX5gX9rD6L8iRC6kMqkPrLv8%2B0Zn9mNLc0WIZMDSXdI5eTnPGZI9PThni%2B80Cr2Iez0SQ0mv4OEHLywga14TgYK8XrIcuvQi2wXxRU6eaQ2P7CbRrUecgsJP1Mx5kw5rAYzBXXvErEEAVIIrrd7TVsmmXh%2FaYp8NM4ojJ68Oo7GLKKjhLYaDQ2Fab%2BQpWZK9fmZ6s4zPHS%2Bb7WpQet5f%2FiOeJY7Xof1UV%2B8QIXUhmtgsmS8PKZt8RKAFT1HSxue97Dx6iFC4Lf0bNA42TAe%2FaLQ%2FQD3fDYTDI3fa8BjqkAbgKRYd%2FpdVOTVPXvm8T1i4jEu5S%2F4KRcRbJKj%2BegnlJedfKhj9g20Gximb2b8w1QQ24BPak%2FMA9E8QHIhLRpaHsCeLFR4yt%2F%2BiuxgSDeYA6EFpENAL5%2BiIKJkjrNMUQXiO%2BzlbB6%2BJQtlchUlOQEwyRh%2BrNfVU4uurAAkaYtOKOwqcoF8NQyopn1KYq2ggfk4yhzcmORZTCwlQioDBEtZ%2BWZng%2F&X-Amz-Signature=49e1af8ecad1438e6fd3ba8a574cecdf2c86da674e486bbd4f5b4f4541c0b070&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QHKU7VH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyArHCqduNDkc0YqhIs%2B47rujcZD9VdNm8jC%2B8paNiJAIhANGMCXRC3q18OU6bxbEjRyL6%2BHthywIYwqbs6ZRd1Ky%2FKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSK2p%2Fj6V35EvDK%2Bsq3ANCgn4qx2sTSL%2BnUoNxqenIJvp3ICbkAoL1t28Jn3SOdLpcMhT7hnMMtykbCf0Ha71ttknnuTz7AY9TsuU4IJfRGYljvzn7wiy%2FZhByjayAQiEhXecMV0QwqgeCGFSo%2Bx85nn1ZwfayHbYvCd1oL%2F7lcQtKyJVy7EBOfHGBizXGjFwZk%2FnGERlyCT5BrvlpSkBb5iUk1uIAajZBiHfkWGwB8su%2FFMllUX%2Bx9mrAa6G4S88NX2liS3bwPFIIxEEVJ2BtpCmEtNivJJVtweN%2F3Iy4otyOJqh%2FT%2FaEtFQ5ZKwQGtcPZ6cKb8cDEPBbiLy6HZmU2nKPliVqh4055X8HiOc4U2tkSKnQX5gX9rD6L8iRC6kMqkPrLv8%2B0Zn9mNLc0WIZMDSXdI5eTnPGZI9PThni%2B80Cr2Iez0SQ0mv4OEHLywga14TgYK8XrIcuvQi2wXxRU6eaQ2P7CbRrUecgsJP1Mx5kw5rAYzBXXvErEEAVIIrrd7TVsmmXh%2FaYp8NM4ojJ68Oo7GLKKjhLYaDQ2Fab%2BQpWZK9fmZ6s4zPHS%2Bb7WpQet5f%2FiOeJY7Xof1UV%2B8QIXUhmtgsmS8PKZt8RKAFT1HSxue97Dx6iFC4Lf0bNA42TAe%2FaLQ%2FQD3fDYTDI3fa8BjqkAbgKRYd%2FpdVOTVPXvm8T1i4jEu5S%2F4KRcRbJKj%2BegnlJedfKhj9g20Gximb2b8w1QQ24BPak%2FMA9E8QHIhLRpaHsCeLFR4yt%2F%2BiuxgSDeYA6EFpENAL5%2BiIKJkjrNMUQXiO%2BzlbB6%2BJQtlchUlOQEwyRh%2BrNfVU4uurAAkaYtOKOwqcoF8NQyopn1KYq2ggfk4yhzcmORZTCwlQioDBEtZ%2BWZng%2F&X-Amz-Signature=54422a852027d1712c31648db6ff29ff7c5d3450c430346e3d0e15763b0fbb56&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QHKU7VH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyArHCqduNDkc0YqhIs%2B47rujcZD9VdNm8jC%2B8paNiJAIhANGMCXRC3q18OU6bxbEjRyL6%2BHthywIYwqbs6ZRd1Ky%2FKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSK2p%2Fj6V35EvDK%2Bsq3ANCgn4qx2sTSL%2BnUoNxqenIJvp3ICbkAoL1t28Jn3SOdLpcMhT7hnMMtykbCf0Ha71ttknnuTz7AY9TsuU4IJfRGYljvzn7wiy%2FZhByjayAQiEhXecMV0QwqgeCGFSo%2Bx85nn1ZwfayHbYvCd1oL%2F7lcQtKyJVy7EBOfHGBizXGjFwZk%2FnGERlyCT5BrvlpSkBb5iUk1uIAajZBiHfkWGwB8su%2FFMllUX%2Bx9mrAa6G4S88NX2liS3bwPFIIxEEVJ2BtpCmEtNivJJVtweN%2F3Iy4otyOJqh%2FT%2FaEtFQ5ZKwQGtcPZ6cKb8cDEPBbiLy6HZmU2nKPliVqh4055X8HiOc4U2tkSKnQX5gX9rD6L8iRC6kMqkPrLv8%2B0Zn9mNLc0WIZMDSXdI5eTnPGZI9PThni%2B80Cr2Iez0SQ0mv4OEHLywga14TgYK8XrIcuvQi2wXxRU6eaQ2P7CbRrUecgsJP1Mx5kw5rAYzBXXvErEEAVIIrrd7TVsmmXh%2FaYp8NM4ojJ68Oo7GLKKjhLYaDQ2Fab%2BQpWZK9fmZ6s4zPHS%2Bb7WpQet5f%2FiOeJY7Xof1UV%2B8QIXUhmtgsmS8PKZt8RKAFT1HSxue97Dx6iFC4Lf0bNA42TAe%2FaLQ%2FQD3fDYTDI3fa8BjqkAbgKRYd%2FpdVOTVPXvm8T1i4jEu5S%2F4KRcRbJKj%2BegnlJedfKhj9g20Gximb2b8w1QQ24BPak%2FMA9E8QHIhLRpaHsCeLFR4yt%2F%2BiuxgSDeYA6EFpENAL5%2BiIKJkjrNMUQXiO%2BzlbB6%2BJQtlchUlOQEwyRh%2BrNfVU4uurAAkaYtOKOwqcoF8NQyopn1KYq2ggfk4yhzcmORZTCwlQioDBEtZ%2BWZng%2F&X-Amz-Signature=2cd70a082932e7e98e76ae8f2e3f12ec4d85c1d96a47410fdb88ee7f53e24df9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QHKU7VH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyArHCqduNDkc0YqhIs%2B47rujcZD9VdNm8jC%2B8paNiJAIhANGMCXRC3q18OU6bxbEjRyL6%2BHthywIYwqbs6ZRd1Ky%2FKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSK2p%2Fj6V35EvDK%2Bsq3ANCgn4qx2sTSL%2BnUoNxqenIJvp3ICbkAoL1t28Jn3SOdLpcMhT7hnMMtykbCf0Ha71ttknnuTz7AY9TsuU4IJfRGYljvzn7wiy%2FZhByjayAQiEhXecMV0QwqgeCGFSo%2Bx85nn1ZwfayHbYvCd1oL%2F7lcQtKyJVy7EBOfHGBizXGjFwZk%2FnGERlyCT5BrvlpSkBb5iUk1uIAajZBiHfkWGwB8su%2FFMllUX%2Bx9mrAa6G4S88NX2liS3bwPFIIxEEVJ2BtpCmEtNivJJVtweN%2F3Iy4otyOJqh%2FT%2FaEtFQ5ZKwQGtcPZ6cKb8cDEPBbiLy6HZmU2nKPliVqh4055X8HiOc4U2tkSKnQX5gX9rD6L8iRC6kMqkPrLv8%2B0Zn9mNLc0WIZMDSXdI5eTnPGZI9PThni%2B80Cr2Iez0SQ0mv4OEHLywga14TgYK8XrIcuvQi2wXxRU6eaQ2P7CbRrUecgsJP1Mx5kw5rAYzBXXvErEEAVIIrrd7TVsmmXh%2FaYp8NM4ojJ68Oo7GLKKjhLYaDQ2Fab%2BQpWZK9fmZ6s4zPHS%2Bb7WpQet5f%2FiOeJY7Xof1UV%2B8QIXUhmtgsmS8PKZt8RKAFT1HSxue97Dx6iFC4Lf0bNA42TAe%2FaLQ%2FQD3fDYTDI3fa8BjqkAbgKRYd%2FpdVOTVPXvm8T1i4jEu5S%2F4KRcRbJKj%2BegnlJedfKhj9g20Gximb2b8w1QQ24BPak%2FMA9E8QHIhLRpaHsCeLFR4yt%2F%2BiuxgSDeYA6EFpENAL5%2BiIKJkjrNMUQXiO%2BzlbB6%2BJQtlchUlOQEwyRh%2BrNfVU4uurAAkaYtOKOwqcoF8NQyopn1KYq2ggfk4yhzcmORZTCwlQioDBEtZ%2BWZng%2F&X-Amz-Signature=0b4caf26198cf99aa7f785db7a3ffb48eb3d4a3a93469869d2e95cf27505bacf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QHKU7VH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyArHCqduNDkc0YqhIs%2B47rujcZD9VdNm8jC%2B8paNiJAIhANGMCXRC3q18OU6bxbEjRyL6%2BHthywIYwqbs6ZRd1Ky%2FKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSK2p%2Fj6V35EvDK%2Bsq3ANCgn4qx2sTSL%2BnUoNxqenIJvp3ICbkAoL1t28Jn3SOdLpcMhT7hnMMtykbCf0Ha71ttknnuTz7AY9TsuU4IJfRGYljvzn7wiy%2FZhByjayAQiEhXecMV0QwqgeCGFSo%2Bx85nn1ZwfayHbYvCd1oL%2F7lcQtKyJVy7EBOfHGBizXGjFwZk%2FnGERlyCT5BrvlpSkBb5iUk1uIAajZBiHfkWGwB8su%2FFMllUX%2Bx9mrAa6G4S88NX2liS3bwPFIIxEEVJ2BtpCmEtNivJJVtweN%2F3Iy4otyOJqh%2FT%2FaEtFQ5ZKwQGtcPZ6cKb8cDEPBbiLy6HZmU2nKPliVqh4055X8HiOc4U2tkSKnQX5gX9rD6L8iRC6kMqkPrLv8%2B0Zn9mNLc0WIZMDSXdI5eTnPGZI9PThni%2B80Cr2Iez0SQ0mv4OEHLywga14TgYK8XrIcuvQi2wXxRU6eaQ2P7CbRrUecgsJP1Mx5kw5rAYzBXXvErEEAVIIrrd7TVsmmXh%2FaYp8NM4ojJ68Oo7GLKKjhLYaDQ2Fab%2BQpWZK9fmZ6s4zPHS%2Bb7WpQet5f%2FiOeJY7Xof1UV%2B8QIXUhmtgsmS8PKZt8RKAFT1HSxue97Dx6iFC4Lf0bNA42TAe%2FaLQ%2FQD3fDYTDI3fa8BjqkAbgKRYd%2FpdVOTVPXvm8T1i4jEu5S%2F4KRcRbJKj%2BegnlJedfKhj9g20Gximb2b8w1QQ24BPak%2FMA9E8QHIhLRpaHsCeLFR4yt%2F%2BiuxgSDeYA6EFpENAL5%2BiIKJkjrNMUQXiO%2BzlbB6%2BJQtlchUlOQEwyRh%2BrNfVU4uurAAkaYtOKOwqcoF8NQyopn1KYq2ggfk4yhzcmORZTCwlQioDBEtZ%2BWZng%2F&X-Amz-Signature=6e9d0c7ab4f761d96d338bf50d003742383168b8d083cbeafd52b3f6dfaff2f4&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QHKU7VH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyArHCqduNDkc0YqhIs%2B47rujcZD9VdNm8jC%2B8paNiJAIhANGMCXRC3q18OU6bxbEjRyL6%2BHthywIYwqbs6ZRd1Ky%2FKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSK2p%2Fj6V35EvDK%2Bsq3ANCgn4qx2sTSL%2BnUoNxqenIJvp3ICbkAoL1t28Jn3SOdLpcMhT7hnMMtykbCf0Ha71ttknnuTz7AY9TsuU4IJfRGYljvzn7wiy%2FZhByjayAQiEhXecMV0QwqgeCGFSo%2Bx85nn1ZwfayHbYvCd1oL%2F7lcQtKyJVy7EBOfHGBizXGjFwZk%2FnGERlyCT5BrvlpSkBb5iUk1uIAajZBiHfkWGwB8su%2FFMllUX%2Bx9mrAa6G4S88NX2liS3bwPFIIxEEVJ2BtpCmEtNivJJVtweN%2F3Iy4otyOJqh%2FT%2FaEtFQ5ZKwQGtcPZ6cKb8cDEPBbiLy6HZmU2nKPliVqh4055X8HiOc4U2tkSKnQX5gX9rD6L8iRC6kMqkPrLv8%2B0Zn9mNLc0WIZMDSXdI5eTnPGZI9PThni%2B80Cr2Iez0SQ0mv4OEHLywga14TgYK8XrIcuvQi2wXxRU6eaQ2P7CbRrUecgsJP1Mx5kw5rAYzBXXvErEEAVIIrrd7TVsmmXh%2FaYp8NM4ojJ68Oo7GLKKjhLYaDQ2Fab%2BQpWZK9fmZ6s4zPHS%2Bb7WpQet5f%2FiOeJY7Xof1UV%2B8QIXUhmtgsmS8PKZt8RKAFT1HSxue97Dx6iFC4Lf0bNA42TAe%2FaLQ%2FQD3fDYTDI3fa8BjqkAbgKRYd%2FpdVOTVPXvm8T1i4jEu5S%2F4KRcRbJKj%2BegnlJedfKhj9g20Gximb2b8w1QQ24BPak%2FMA9E8QHIhLRpaHsCeLFR4yt%2F%2BiuxgSDeYA6EFpENAL5%2BiIKJkjrNMUQXiO%2BzlbB6%2BJQtlchUlOQEwyRh%2BrNfVU4uurAAkaYtOKOwqcoF8NQyopn1KYq2ggfk4yhzcmORZTCwlQioDBEtZ%2BWZng%2F&X-Amz-Signature=ca7788c67f468807e89561f1d3467f88c1d580885f692ae69f8b550f822e9be5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QHKU7VH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyArHCqduNDkc0YqhIs%2B47rujcZD9VdNm8jC%2B8paNiJAIhANGMCXRC3q18OU6bxbEjRyL6%2BHthywIYwqbs6ZRd1Ky%2FKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSK2p%2Fj6V35EvDK%2Bsq3ANCgn4qx2sTSL%2BnUoNxqenIJvp3ICbkAoL1t28Jn3SOdLpcMhT7hnMMtykbCf0Ha71ttknnuTz7AY9TsuU4IJfRGYljvzn7wiy%2FZhByjayAQiEhXecMV0QwqgeCGFSo%2Bx85nn1ZwfayHbYvCd1oL%2F7lcQtKyJVy7EBOfHGBizXGjFwZk%2FnGERlyCT5BrvlpSkBb5iUk1uIAajZBiHfkWGwB8su%2FFMllUX%2Bx9mrAa6G4S88NX2liS3bwPFIIxEEVJ2BtpCmEtNivJJVtweN%2F3Iy4otyOJqh%2FT%2FaEtFQ5ZKwQGtcPZ6cKb8cDEPBbiLy6HZmU2nKPliVqh4055X8HiOc4U2tkSKnQX5gX9rD6L8iRC6kMqkPrLv8%2B0Zn9mNLc0WIZMDSXdI5eTnPGZI9PThni%2B80Cr2Iez0SQ0mv4OEHLywga14TgYK8XrIcuvQi2wXxRU6eaQ2P7CbRrUecgsJP1Mx5kw5rAYzBXXvErEEAVIIrrd7TVsmmXh%2FaYp8NM4ojJ68Oo7GLKKjhLYaDQ2Fab%2BQpWZK9fmZ6s4zPHS%2Bb7WpQet5f%2FiOeJY7Xof1UV%2B8QIXUhmtgsmS8PKZt8RKAFT1HSxue97Dx6iFC4Lf0bNA42TAe%2FaLQ%2FQD3fDYTDI3fa8BjqkAbgKRYd%2FpdVOTVPXvm8T1i4jEu5S%2F4KRcRbJKj%2BegnlJedfKhj9g20Gximb2b8w1QQ24BPak%2FMA9E8QHIhLRpaHsCeLFR4yt%2F%2BiuxgSDeYA6EFpENAL5%2BiIKJkjrNMUQXiO%2BzlbB6%2BJQtlchUlOQEwyRh%2BrNfVU4uurAAkaYtOKOwqcoF8NQyopn1KYq2ggfk4yhzcmORZTCwlQioDBEtZ%2BWZng%2F&X-Amz-Signature=bb4836b68efc0afffb9160429ce8e846fa6febf15c763c1ae092c9eb5a04142f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QHKU7VH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyArHCqduNDkc0YqhIs%2B47rujcZD9VdNm8jC%2B8paNiJAIhANGMCXRC3q18OU6bxbEjRyL6%2BHthywIYwqbs6ZRd1Ky%2FKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSK2p%2Fj6V35EvDK%2Bsq3ANCgn4qx2sTSL%2BnUoNxqenIJvp3ICbkAoL1t28Jn3SOdLpcMhT7hnMMtykbCf0Ha71ttknnuTz7AY9TsuU4IJfRGYljvzn7wiy%2FZhByjayAQiEhXecMV0QwqgeCGFSo%2Bx85nn1ZwfayHbYvCd1oL%2F7lcQtKyJVy7EBOfHGBizXGjFwZk%2FnGERlyCT5BrvlpSkBb5iUk1uIAajZBiHfkWGwB8su%2FFMllUX%2Bx9mrAa6G4S88NX2liS3bwPFIIxEEVJ2BtpCmEtNivJJVtweN%2F3Iy4otyOJqh%2FT%2FaEtFQ5ZKwQGtcPZ6cKb8cDEPBbiLy6HZmU2nKPliVqh4055X8HiOc4U2tkSKnQX5gX9rD6L8iRC6kMqkPrLv8%2B0Zn9mNLc0WIZMDSXdI5eTnPGZI9PThni%2B80Cr2Iez0SQ0mv4OEHLywga14TgYK8XrIcuvQi2wXxRU6eaQ2P7CbRrUecgsJP1Mx5kw5rAYzBXXvErEEAVIIrrd7TVsmmXh%2FaYp8NM4ojJ68Oo7GLKKjhLYaDQ2Fab%2BQpWZK9fmZ6s4zPHS%2Bb7WpQet5f%2FiOeJY7Xof1UV%2B8QIXUhmtgsmS8PKZt8RKAFT1HSxue97Dx6iFC4Lf0bNA42TAe%2FaLQ%2FQD3fDYTDI3fa8BjqkAbgKRYd%2FpdVOTVPXvm8T1i4jEu5S%2F4KRcRbJKj%2BegnlJedfKhj9g20Gximb2b8w1QQ24BPak%2FMA9E8QHIhLRpaHsCeLFR4yt%2F%2BiuxgSDeYA6EFpENAL5%2BiIKJkjrNMUQXiO%2BzlbB6%2BJQtlchUlOQEwyRh%2BrNfVU4uurAAkaYtOKOwqcoF8NQyopn1KYq2ggfk4yhzcmORZTCwlQioDBEtZ%2BWZng%2F&X-Amz-Signature=ba4ee9e1ed77ccfdb1f7fb798539ad5e3fe8219b97475a6cbb0f433a978f9131&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QHKU7VH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyArHCqduNDkc0YqhIs%2B47rujcZD9VdNm8jC%2B8paNiJAIhANGMCXRC3q18OU6bxbEjRyL6%2BHthywIYwqbs6ZRd1Ky%2FKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSK2p%2Fj6V35EvDK%2Bsq3ANCgn4qx2sTSL%2BnUoNxqenIJvp3ICbkAoL1t28Jn3SOdLpcMhT7hnMMtykbCf0Ha71ttknnuTz7AY9TsuU4IJfRGYljvzn7wiy%2FZhByjayAQiEhXecMV0QwqgeCGFSo%2Bx85nn1ZwfayHbYvCd1oL%2F7lcQtKyJVy7EBOfHGBizXGjFwZk%2FnGERlyCT5BrvlpSkBb5iUk1uIAajZBiHfkWGwB8su%2FFMllUX%2Bx9mrAa6G4S88NX2liS3bwPFIIxEEVJ2BtpCmEtNivJJVtweN%2F3Iy4otyOJqh%2FT%2FaEtFQ5ZKwQGtcPZ6cKb8cDEPBbiLy6HZmU2nKPliVqh4055X8HiOc4U2tkSKnQX5gX9rD6L8iRC6kMqkPrLv8%2B0Zn9mNLc0WIZMDSXdI5eTnPGZI9PThni%2B80Cr2Iez0SQ0mv4OEHLywga14TgYK8XrIcuvQi2wXxRU6eaQ2P7CbRrUecgsJP1Mx5kw5rAYzBXXvErEEAVIIrrd7TVsmmXh%2FaYp8NM4ojJ68Oo7GLKKjhLYaDQ2Fab%2BQpWZK9fmZ6s4zPHS%2Bb7WpQet5f%2FiOeJY7Xof1UV%2B8QIXUhmtgsmS8PKZt8RKAFT1HSxue97Dx6iFC4Lf0bNA42TAe%2FaLQ%2FQD3fDYTDI3fa8BjqkAbgKRYd%2FpdVOTVPXvm8T1i4jEu5S%2F4KRcRbJKj%2BegnlJedfKhj9g20Gximb2b8w1QQ24BPak%2FMA9E8QHIhLRpaHsCeLFR4yt%2F%2BiuxgSDeYA6EFpENAL5%2BiIKJkjrNMUQXiO%2BzlbB6%2BJQtlchUlOQEwyRh%2BrNfVU4uurAAkaYtOKOwqcoF8NQyopn1KYq2ggfk4yhzcmORZTCwlQioDBEtZ%2BWZng%2F&X-Amz-Signature=3b13a877001091eef00f5b66e48f92e3d78efc60917d64fbc991b2057b338050&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZA6VG4QV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCD0pGvAm6Ibeoj0QarWyvc5p5Nt91ZsLxGjIcMoM9z5AIhAORnkhZZ42AWNZCTMt8MWh0lUIXwJvGW6Ld6qUtqqyuYKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydHSBsri5yXrPjje0q3AMVxUaiLQyubBauah0kDJbk3LcWa6sEQTF15SNCZ6otSv44ur3ShmNwY4ZcTAP8nyH94fAejHyDApGYu%2B8d7oF1atLwt%2FOFiPsCWa%2FWDpWrDuFILMF3JNIS1LFHBBOnOVw7uwXBxAvI07u%2F3Mnfqvg2fN0tu2u%2F5Q9N85LwB84aKSvZ73YQa5%2F3LTM3x8th3GMT8xf9H8g2YqekvU3ZFaDHPOROLWhfqRJ6Dw4kZkcQgTwseKXcrJk%2Facvp8OPQpvpr%2BulefvA1YhovPd62OnhPsWbnJL0%2FHVAALU%2BKO701GbvweEhZguBSoD02obF42jAHk15NP7TUmitzANLAfh%2FRngXyOmKj9s4qUz2GwI3yGMS9DIU37Vgb%2FuG8LEbRg7iqWpEvVLQ50UAJLqakx%2B%2FipIhGgMPk3WQJS1GJoFVD%2FTfmLO%2FP0R5JUVdbDPioXk7J8jir14ltfqnI5AFy2ms7gqDcvDTy8PsSY1ZwREwGRf9m0%2FeT8xris2F7hvuiTS1XJMw2WFr6%2B1wO%2Bj1deYBgQSxXNipkkOt4fHRCuoJr7c8V7ASDPHMN2M0Dd%2FX4KrK1fGdH0Y%2BhkdAkpkbkLfE8HPEDQXGZO4tNxfYq%2BU1xaMEhEr%2FfqGS9%2BR45dDCf3fa8BjqkAfunNLC%2FvZY6JYf7aMsUQuI8BJYOq%2FEjYFzuVopw0alPOEnzVvXziMkX%2BpBqj4PU5A8JD6J8gvGHG2qJfhFlvIOkBBnBOhMCJaBhplyoFdS5%2FCFc7hlhOJ7mE9iXSrRSS9URtu%2Fb6iOtJsCEJ5O0azfrr%2Fi4GWt%2BrRn%2F6UbE5e0iPd4DjAwB2BUoDLVTOb7BP%2BZzucs6sGRZQzuGOqUeuiH%2FKI26&X-Amz-Signature=6616684648591668b2f8345861cc576741965df9e482ea2840d96096213d9d52&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZA6VG4QV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCD0pGvAm6Ibeoj0QarWyvc5p5Nt91ZsLxGjIcMoM9z5AIhAORnkhZZ42AWNZCTMt8MWh0lUIXwJvGW6Ld6qUtqqyuYKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydHSBsri5yXrPjje0q3AMVxUaiLQyubBauah0kDJbk3LcWa6sEQTF15SNCZ6otSv44ur3ShmNwY4ZcTAP8nyH94fAejHyDApGYu%2B8d7oF1atLwt%2FOFiPsCWa%2FWDpWrDuFILMF3JNIS1LFHBBOnOVw7uwXBxAvI07u%2F3Mnfqvg2fN0tu2u%2F5Q9N85LwB84aKSvZ73YQa5%2F3LTM3x8th3GMT8xf9H8g2YqekvU3ZFaDHPOROLWhfqRJ6Dw4kZkcQgTwseKXcrJk%2Facvp8OPQpvpr%2BulefvA1YhovPd62OnhPsWbnJL0%2FHVAALU%2BKO701GbvweEhZguBSoD02obF42jAHk15NP7TUmitzANLAfh%2FRngXyOmKj9s4qUz2GwI3yGMS9DIU37Vgb%2FuG8LEbRg7iqWpEvVLQ50UAJLqakx%2B%2FipIhGgMPk3WQJS1GJoFVD%2FTfmLO%2FP0R5JUVdbDPioXk7J8jir14ltfqnI5AFy2ms7gqDcvDTy8PsSY1ZwREwGRf9m0%2FeT8xris2F7hvuiTS1XJMw2WFr6%2B1wO%2Bj1deYBgQSxXNipkkOt4fHRCuoJr7c8V7ASDPHMN2M0Dd%2FX4KrK1fGdH0Y%2BhkdAkpkbkLfE8HPEDQXGZO4tNxfYq%2BU1xaMEhEr%2FfqGS9%2BR45dDCf3fa8BjqkAfunNLC%2FvZY6JYf7aMsUQuI8BJYOq%2FEjYFzuVopw0alPOEnzVvXziMkX%2BpBqj4PU5A8JD6J8gvGHG2qJfhFlvIOkBBnBOhMCJaBhplyoFdS5%2FCFc7hlhOJ7mE9iXSrRSS9URtu%2Fb6iOtJsCEJ5O0azfrr%2Fi4GWt%2BrRn%2F6UbE5e0iPd4DjAwB2BUoDLVTOb7BP%2BZzucs6sGRZQzuGOqUeuiH%2FKI26&X-Amz-Signature=528530261f0e20591dd3999fda10f4705c858a7e977875cb6915bf817c5b65ca&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
