

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMYM4BIJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDD5ghij88ZgwqeDJMM3A3ta8rUhQw6Qqv5XIsGpN6ougIgQqf9O5SZk6ItsneNk948XVC%2BHV0Gb0pFvP7%2BD5Yrv08q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDF45eWNkf3V1UFAscircA%2BkAyJY%2F49iHYbzY1W%2BERDvVcqAbK7SFACsHhf88gJ1V1JTo%2BfJylgBnqPEzqGYkUC5HHYiWUQZUQUqePWfQYvxfRGZ%2FLd2FzkGdYG%2BQNqUUclRFnzwuhL6Cl9Qjc2MHqkf7bdtaHYrd3GH1gdd4QLuwtuNKKMQ7IysYxFi2oToOSsuWnEsPt%2FtgyVkYVgYptyxx0PaauSeWbFUjAa%2FVOl8kpXxW6lgf623z%2BkW%2B1vbIRnsHzXMzuok65nzAXuKRzlG96aElwhljrBwehCCqZqaR%2FJq6WD4nbw5SBf8r2WXivKTLm8lhZnOuRAgwvE%2FQnTmuvhoRwfx2AvglfFIwHOmA4fwtIbkfCO4G89%2Bil5zlKYtnz11ejh2ZR8%2Fyoo3rog25h7KHUf%2FueiqDKzX3hQ4L5TyMq8Jp1ngm7X69YdZv%2Fpuwo9owjE0wVb%2BWGMoJFQjq%2BjHCdU0%2F74tyjcb%2BEyaF54C8rWKGy8p9TzJNCKAkR01Kc1%2BZ%2FY5Gkv8c5%2F%2Fw%2FR8%2BWCGv%2Fp13pvRtukz3DzaHVOONCgMu4Ask3j2PXMsYi9Pauw81KncqB0RCpeEhF49f7rYnTj97XIOBgghPva%2FjKfQ6k03ZSs%2BXyWaRbDJKpVhPWenFv%2FP50kzHMJmck70GOqUBRJLpChcZtrDNpsgX%2BK%2FJs878C1evG9Tuo%2FHhaRgYKbQi5WlXlv4n2GltnsGy4wQgsONhRpYEAysg0PDCnJZ9dSHge0ihWqt%2B9Iak4SHRuOA4mjdd%2FYCyMYNIvCvnBtzfn05ydzdGAb%2BRIPio9prxzM0oxWGIgySZahmOWMmAROZIhOoJI1CvlmEWV7R64ALSJGSxxYDIZidJ%2FjUqpwfpVZ3RnZnp&X-Amz-Signature=1aefd4c9e353021664c5994969dad475e4ca67554eb4f8316a56949646736d9f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMYM4BIJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDD5ghij88ZgwqeDJMM3A3ta8rUhQw6Qqv5XIsGpN6ougIgQqf9O5SZk6ItsneNk948XVC%2BHV0Gb0pFvP7%2BD5Yrv08q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDF45eWNkf3V1UFAscircA%2BkAyJY%2F49iHYbzY1W%2BERDvVcqAbK7SFACsHhf88gJ1V1JTo%2BfJylgBnqPEzqGYkUC5HHYiWUQZUQUqePWfQYvxfRGZ%2FLd2FzkGdYG%2BQNqUUclRFnzwuhL6Cl9Qjc2MHqkf7bdtaHYrd3GH1gdd4QLuwtuNKKMQ7IysYxFi2oToOSsuWnEsPt%2FtgyVkYVgYptyxx0PaauSeWbFUjAa%2FVOl8kpXxW6lgf623z%2BkW%2B1vbIRnsHzXMzuok65nzAXuKRzlG96aElwhljrBwehCCqZqaR%2FJq6WD4nbw5SBf8r2WXivKTLm8lhZnOuRAgwvE%2FQnTmuvhoRwfx2AvglfFIwHOmA4fwtIbkfCO4G89%2Bil5zlKYtnz11ejh2ZR8%2Fyoo3rog25h7KHUf%2FueiqDKzX3hQ4L5TyMq8Jp1ngm7X69YdZv%2Fpuwo9owjE0wVb%2BWGMoJFQjq%2BjHCdU0%2F74tyjcb%2BEyaF54C8rWKGy8p9TzJNCKAkR01Kc1%2BZ%2FY5Gkv8c5%2F%2Fw%2FR8%2BWCGv%2Fp13pvRtukz3DzaHVOONCgMu4Ask3j2PXMsYi9Pauw81KncqB0RCpeEhF49f7rYnTj97XIOBgghPva%2FjKfQ6k03ZSs%2BXyWaRbDJKpVhPWenFv%2FP50kzHMJmck70GOqUBRJLpChcZtrDNpsgX%2BK%2FJs878C1evG9Tuo%2FHhaRgYKbQi5WlXlv4n2GltnsGy4wQgsONhRpYEAysg0PDCnJZ9dSHge0ihWqt%2B9Iak4SHRuOA4mjdd%2FYCyMYNIvCvnBtzfn05ydzdGAb%2BRIPio9prxzM0oxWGIgySZahmOWMmAROZIhOoJI1CvlmEWV7R64ALSJGSxxYDIZidJ%2FjUqpwfpVZ3RnZnp&X-Amz-Signature=e449bd24a4820f4ff5289cc60e5f19bcbf31a39b6c7dc0898e6c09f295474c38&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMYM4BIJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDD5ghij88ZgwqeDJMM3A3ta8rUhQw6Qqv5XIsGpN6ougIgQqf9O5SZk6ItsneNk948XVC%2BHV0Gb0pFvP7%2BD5Yrv08q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDF45eWNkf3V1UFAscircA%2BkAyJY%2F49iHYbzY1W%2BERDvVcqAbK7SFACsHhf88gJ1V1JTo%2BfJylgBnqPEzqGYkUC5HHYiWUQZUQUqePWfQYvxfRGZ%2FLd2FzkGdYG%2BQNqUUclRFnzwuhL6Cl9Qjc2MHqkf7bdtaHYrd3GH1gdd4QLuwtuNKKMQ7IysYxFi2oToOSsuWnEsPt%2FtgyVkYVgYptyxx0PaauSeWbFUjAa%2FVOl8kpXxW6lgf623z%2BkW%2B1vbIRnsHzXMzuok65nzAXuKRzlG96aElwhljrBwehCCqZqaR%2FJq6WD4nbw5SBf8r2WXivKTLm8lhZnOuRAgwvE%2FQnTmuvhoRwfx2AvglfFIwHOmA4fwtIbkfCO4G89%2Bil5zlKYtnz11ejh2ZR8%2Fyoo3rog25h7KHUf%2FueiqDKzX3hQ4L5TyMq8Jp1ngm7X69YdZv%2Fpuwo9owjE0wVb%2BWGMoJFQjq%2BjHCdU0%2F74tyjcb%2BEyaF54C8rWKGy8p9TzJNCKAkR01Kc1%2BZ%2FY5Gkv8c5%2F%2Fw%2FR8%2BWCGv%2Fp13pvRtukz3DzaHVOONCgMu4Ask3j2PXMsYi9Pauw81KncqB0RCpeEhF49f7rYnTj97XIOBgghPva%2FjKfQ6k03ZSs%2BXyWaRbDJKpVhPWenFv%2FP50kzHMJmck70GOqUBRJLpChcZtrDNpsgX%2BK%2FJs878C1evG9Tuo%2FHhaRgYKbQi5WlXlv4n2GltnsGy4wQgsONhRpYEAysg0PDCnJZ9dSHge0ihWqt%2B9Iak4SHRuOA4mjdd%2FYCyMYNIvCvnBtzfn05ydzdGAb%2BRIPio9prxzM0oxWGIgySZahmOWMmAROZIhOoJI1CvlmEWV7R64ALSJGSxxYDIZidJ%2FjUqpwfpVZ3RnZnp&X-Amz-Signature=4dc84397b538488b4977ed912b4ced7c3266206378d5a0aaefd62ba30bb4c148&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMYM4BIJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDD5ghij88ZgwqeDJMM3A3ta8rUhQw6Qqv5XIsGpN6ougIgQqf9O5SZk6ItsneNk948XVC%2BHV0Gb0pFvP7%2BD5Yrv08q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDF45eWNkf3V1UFAscircA%2BkAyJY%2F49iHYbzY1W%2BERDvVcqAbK7SFACsHhf88gJ1V1JTo%2BfJylgBnqPEzqGYkUC5HHYiWUQZUQUqePWfQYvxfRGZ%2FLd2FzkGdYG%2BQNqUUclRFnzwuhL6Cl9Qjc2MHqkf7bdtaHYrd3GH1gdd4QLuwtuNKKMQ7IysYxFi2oToOSsuWnEsPt%2FtgyVkYVgYptyxx0PaauSeWbFUjAa%2FVOl8kpXxW6lgf623z%2BkW%2B1vbIRnsHzXMzuok65nzAXuKRzlG96aElwhljrBwehCCqZqaR%2FJq6WD4nbw5SBf8r2WXivKTLm8lhZnOuRAgwvE%2FQnTmuvhoRwfx2AvglfFIwHOmA4fwtIbkfCO4G89%2Bil5zlKYtnz11ejh2ZR8%2Fyoo3rog25h7KHUf%2FueiqDKzX3hQ4L5TyMq8Jp1ngm7X69YdZv%2Fpuwo9owjE0wVb%2BWGMoJFQjq%2BjHCdU0%2F74tyjcb%2BEyaF54C8rWKGy8p9TzJNCKAkR01Kc1%2BZ%2FY5Gkv8c5%2F%2Fw%2FR8%2BWCGv%2Fp13pvRtukz3DzaHVOONCgMu4Ask3j2PXMsYi9Pauw81KncqB0RCpeEhF49f7rYnTj97XIOBgghPva%2FjKfQ6k03ZSs%2BXyWaRbDJKpVhPWenFv%2FP50kzHMJmck70GOqUBRJLpChcZtrDNpsgX%2BK%2FJs878C1evG9Tuo%2FHhaRgYKbQi5WlXlv4n2GltnsGy4wQgsONhRpYEAysg0PDCnJZ9dSHge0ihWqt%2B9Iak4SHRuOA4mjdd%2FYCyMYNIvCvnBtzfn05ydzdGAb%2BRIPio9prxzM0oxWGIgySZahmOWMmAROZIhOoJI1CvlmEWV7R64ALSJGSxxYDIZidJ%2FjUqpwfpVZ3RnZnp&X-Amz-Signature=516704678379af5804358be344965fd3ad3e9b928622471fb22f982f9dda64b7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMYM4BIJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDD5ghij88ZgwqeDJMM3A3ta8rUhQw6Qqv5XIsGpN6ougIgQqf9O5SZk6ItsneNk948XVC%2BHV0Gb0pFvP7%2BD5Yrv08q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDF45eWNkf3V1UFAscircA%2BkAyJY%2F49iHYbzY1W%2BERDvVcqAbK7SFACsHhf88gJ1V1JTo%2BfJylgBnqPEzqGYkUC5HHYiWUQZUQUqePWfQYvxfRGZ%2FLd2FzkGdYG%2BQNqUUclRFnzwuhL6Cl9Qjc2MHqkf7bdtaHYrd3GH1gdd4QLuwtuNKKMQ7IysYxFi2oToOSsuWnEsPt%2FtgyVkYVgYptyxx0PaauSeWbFUjAa%2FVOl8kpXxW6lgf623z%2BkW%2B1vbIRnsHzXMzuok65nzAXuKRzlG96aElwhljrBwehCCqZqaR%2FJq6WD4nbw5SBf8r2WXivKTLm8lhZnOuRAgwvE%2FQnTmuvhoRwfx2AvglfFIwHOmA4fwtIbkfCO4G89%2Bil5zlKYtnz11ejh2ZR8%2Fyoo3rog25h7KHUf%2FueiqDKzX3hQ4L5TyMq8Jp1ngm7X69YdZv%2Fpuwo9owjE0wVb%2BWGMoJFQjq%2BjHCdU0%2F74tyjcb%2BEyaF54C8rWKGy8p9TzJNCKAkR01Kc1%2BZ%2FY5Gkv8c5%2F%2Fw%2FR8%2BWCGv%2Fp13pvRtukz3DzaHVOONCgMu4Ask3j2PXMsYi9Pauw81KncqB0RCpeEhF49f7rYnTj97XIOBgghPva%2FjKfQ6k03ZSs%2BXyWaRbDJKpVhPWenFv%2FP50kzHMJmck70GOqUBRJLpChcZtrDNpsgX%2BK%2FJs878C1evG9Tuo%2FHhaRgYKbQi5WlXlv4n2GltnsGy4wQgsONhRpYEAysg0PDCnJZ9dSHge0ihWqt%2B9Iak4SHRuOA4mjdd%2FYCyMYNIvCvnBtzfn05ydzdGAb%2BRIPio9prxzM0oxWGIgySZahmOWMmAROZIhOoJI1CvlmEWV7R64ALSJGSxxYDIZidJ%2FjUqpwfpVZ3RnZnp&X-Amz-Signature=bd3c2d5a475f5c30fa37cc853319d70ee8a51f763912f21fb63dd00ef27ae382&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMYM4BIJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDD5ghij88ZgwqeDJMM3A3ta8rUhQw6Qqv5XIsGpN6ougIgQqf9O5SZk6ItsneNk948XVC%2BHV0Gb0pFvP7%2BD5Yrv08q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDF45eWNkf3V1UFAscircA%2BkAyJY%2F49iHYbzY1W%2BERDvVcqAbK7SFACsHhf88gJ1V1JTo%2BfJylgBnqPEzqGYkUC5HHYiWUQZUQUqePWfQYvxfRGZ%2FLd2FzkGdYG%2BQNqUUclRFnzwuhL6Cl9Qjc2MHqkf7bdtaHYrd3GH1gdd4QLuwtuNKKMQ7IysYxFi2oToOSsuWnEsPt%2FtgyVkYVgYptyxx0PaauSeWbFUjAa%2FVOl8kpXxW6lgf623z%2BkW%2B1vbIRnsHzXMzuok65nzAXuKRzlG96aElwhljrBwehCCqZqaR%2FJq6WD4nbw5SBf8r2WXivKTLm8lhZnOuRAgwvE%2FQnTmuvhoRwfx2AvglfFIwHOmA4fwtIbkfCO4G89%2Bil5zlKYtnz11ejh2ZR8%2Fyoo3rog25h7KHUf%2FueiqDKzX3hQ4L5TyMq8Jp1ngm7X69YdZv%2Fpuwo9owjE0wVb%2BWGMoJFQjq%2BjHCdU0%2F74tyjcb%2BEyaF54C8rWKGy8p9TzJNCKAkR01Kc1%2BZ%2FY5Gkv8c5%2F%2Fw%2FR8%2BWCGv%2Fp13pvRtukz3DzaHVOONCgMu4Ask3j2PXMsYi9Pauw81KncqB0RCpeEhF49f7rYnTj97XIOBgghPva%2FjKfQ6k03ZSs%2BXyWaRbDJKpVhPWenFv%2FP50kzHMJmck70GOqUBRJLpChcZtrDNpsgX%2BK%2FJs878C1evG9Tuo%2FHhaRgYKbQi5WlXlv4n2GltnsGy4wQgsONhRpYEAysg0PDCnJZ9dSHge0ihWqt%2B9Iak4SHRuOA4mjdd%2FYCyMYNIvCvnBtzfn05ydzdGAb%2BRIPio9prxzM0oxWGIgySZahmOWMmAROZIhOoJI1CvlmEWV7R64ALSJGSxxYDIZidJ%2FjUqpwfpVZ3RnZnp&X-Amz-Signature=44472132073dc73f46feacf1c3be80c55563490c057c0b23a5d1efad154a7417&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMYM4BIJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDD5ghij88ZgwqeDJMM3A3ta8rUhQw6Qqv5XIsGpN6ougIgQqf9O5SZk6ItsneNk948XVC%2BHV0Gb0pFvP7%2BD5Yrv08q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDF45eWNkf3V1UFAscircA%2BkAyJY%2F49iHYbzY1W%2BERDvVcqAbK7SFACsHhf88gJ1V1JTo%2BfJylgBnqPEzqGYkUC5HHYiWUQZUQUqePWfQYvxfRGZ%2FLd2FzkGdYG%2BQNqUUclRFnzwuhL6Cl9Qjc2MHqkf7bdtaHYrd3GH1gdd4QLuwtuNKKMQ7IysYxFi2oToOSsuWnEsPt%2FtgyVkYVgYptyxx0PaauSeWbFUjAa%2FVOl8kpXxW6lgf623z%2BkW%2B1vbIRnsHzXMzuok65nzAXuKRzlG96aElwhljrBwehCCqZqaR%2FJq6WD4nbw5SBf8r2WXivKTLm8lhZnOuRAgwvE%2FQnTmuvhoRwfx2AvglfFIwHOmA4fwtIbkfCO4G89%2Bil5zlKYtnz11ejh2ZR8%2Fyoo3rog25h7KHUf%2FueiqDKzX3hQ4L5TyMq8Jp1ngm7X69YdZv%2Fpuwo9owjE0wVb%2BWGMoJFQjq%2BjHCdU0%2F74tyjcb%2BEyaF54C8rWKGy8p9TzJNCKAkR01Kc1%2BZ%2FY5Gkv8c5%2F%2Fw%2FR8%2BWCGv%2Fp13pvRtukz3DzaHVOONCgMu4Ask3j2PXMsYi9Pauw81KncqB0RCpeEhF49f7rYnTj97XIOBgghPva%2FjKfQ6k03ZSs%2BXyWaRbDJKpVhPWenFv%2FP50kzHMJmck70GOqUBRJLpChcZtrDNpsgX%2BK%2FJs878C1evG9Tuo%2FHhaRgYKbQi5WlXlv4n2GltnsGy4wQgsONhRpYEAysg0PDCnJZ9dSHge0ihWqt%2B9Iak4SHRuOA4mjdd%2FYCyMYNIvCvnBtzfn05ydzdGAb%2BRIPio9prxzM0oxWGIgySZahmOWMmAROZIhOoJI1CvlmEWV7R64ALSJGSxxYDIZidJ%2FjUqpwfpVZ3RnZnp&X-Amz-Signature=e7296d15b3ce79b0300fe8a61e6595c260898380d4cc99ff74b8f6504e39c202&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMYM4BIJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDD5ghij88ZgwqeDJMM3A3ta8rUhQw6Qqv5XIsGpN6ougIgQqf9O5SZk6ItsneNk948XVC%2BHV0Gb0pFvP7%2BD5Yrv08q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDF45eWNkf3V1UFAscircA%2BkAyJY%2F49iHYbzY1W%2BERDvVcqAbK7SFACsHhf88gJ1V1JTo%2BfJylgBnqPEzqGYkUC5HHYiWUQZUQUqePWfQYvxfRGZ%2FLd2FzkGdYG%2BQNqUUclRFnzwuhL6Cl9Qjc2MHqkf7bdtaHYrd3GH1gdd4QLuwtuNKKMQ7IysYxFi2oToOSsuWnEsPt%2FtgyVkYVgYptyxx0PaauSeWbFUjAa%2FVOl8kpXxW6lgf623z%2BkW%2B1vbIRnsHzXMzuok65nzAXuKRzlG96aElwhljrBwehCCqZqaR%2FJq6WD4nbw5SBf8r2WXivKTLm8lhZnOuRAgwvE%2FQnTmuvhoRwfx2AvglfFIwHOmA4fwtIbkfCO4G89%2Bil5zlKYtnz11ejh2ZR8%2Fyoo3rog25h7KHUf%2FueiqDKzX3hQ4L5TyMq8Jp1ngm7X69YdZv%2Fpuwo9owjE0wVb%2BWGMoJFQjq%2BjHCdU0%2F74tyjcb%2BEyaF54C8rWKGy8p9TzJNCKAkR01Kc1%2BZ%2FY5Gkv8c5%2F%2Fw%2FR8%2BWCGv%2Fp13pvRtukz3DzaHVOONCgMu4Ask3j2PXMsYi9Pauw81KncqB0RCpeEhF49f7rYnTj97XIOBgghPva%2FjKfQ6k03ZSs%2BXyWaRbDJKpVhPWenFv%2FP50kzHMJmck70GOqUBRJLpChcZtrDNpsgX%2BK%2FJs878C1evG9Tuo%2FHhaRgYKbQi5WlXlv4n2GltnsGy4wQgsONhRpYEAysg0PDCnJZ9dSHge0ihWqt%2B9Iak4SHRuOA4mjdd%2FYCyMYNIvCvnBtzfn05ydzdGAb%2BRIPio9prxzM0oxWGIgySZahmOWMmAROZIhOoJI1CvlmEWV7R64ALSJGSxxYDIZidJ%2FjUqpwfpVZ3RnZnp&X-Amz-Signature=dce971cde25aca09167bd36490630bdbb9caa05199fd2f8722017f5e041e387f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMYM4BIJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDD5ghij88ZgwqeDJMM3A3ta8rUhQw6Qqv5XIsGpN6ougIgQqf9O5SZk6ItsneNk948XVC%2BHV0Gb0pFvP7%2BD5Yrv08q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDF45eWNkf3V1UFAscircA%2BkAyJY%2F49iHYbzY1W%2BERDvVcqAbK7SFACsHhf88gJ1V1JTo%2BfJylgBnqPEzqGYkUC5HHYiWUQZUQUqePWfQYvxfRGZ%2FLd2FzkGdYG%2BQNqUUclRFnzwuhL6Cl9Qjc2MHqkf7bdtaHYrd3GH1gdd4QLuwtuNKKMQ7IysYxFi2oToOSsuWnEsPt%2FtgyVkYVgYptyxx0PaauSeWbFUjAa%2FVOl8kpXxW6lgf623z%2BkW%2B1vbIRnsHzXMzuok65nzAXuKRzlG96aElwhljrBwehCCqZqaR%2FJq6WD4nbw5SBf8r2WXivKTLm8lhZnOuRAgwvE%2FQnTmuvhoRwfx2AvglfFIwHOmA4fwtIbkfCO4G89%2Bil5zlKYtnz11ejh2ZR8%2Fyoo3rog25h7KHUf%2FueiqDKzX3hQ4L5TyMq8Jp1ngm7X69YdZv%2Fpuwo9owjE0wVb%2BWGMoJFQjq%2BjHCdU0%2F74tyjcb%2BEyaF54C8rWKGy8p9TzJNCKAkR01Kc1%2BZ%2FY5Gkv8c5%2F%2Fw%2FR8%2BWCGv%2Fp13pvRtukz3DzaHVOONCgMu4Ask3j2PXMsYi9Pauw81KncqB0RCpeEhF49f7rYnTj97XIOBgghPva%2FjKfQ6k03ZSs%2BXyWaRbDJKpVhPWenFv%2FP50kzHMJmck70GOqUBRJLpChcZtrDNpsgX%2BK%2FJs878C1evG9Tuo%2FHhaRgYKbQi5WlXlv4n2GltnsGy4wQgsONhRpYEAysg0PDCnJZ9dSHge0ihWqt%2B9Iak4SHRuOA4mjdd%2FYCyMYNIvCvnBtzfn05ydzdGAb%2BRIPio9prxzM0oxWGIgySZahmOWMmAROZIhOoJI1CvlmEWV7R64ALSJGSxxYDIZidJ%2FjUqpwfpVZ3RnZnp&X-Amz-Signature=088cdc08ee38bb51bac88ecd5cdcfbb27b29a33952bbb7648345d5d78014fa69&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNRIIV3G%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQC0LRPjaVpJt0cxmkryZZVxDF0UhlpmzkOdsqYVBnlaSgIgY4xoR5l734wKg8t6iXHbrrdUPhSZss1zMTU0LLogCRMq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDAY0A78ID9oiLhnYBCrcA8NCPjJ%2B6h6sqH4mts0zjPLHmZL7juc3OHRw0b2FKDR8ANj4vzSz%2BHh3saZv2YuVFslPMyS%2FzwvNaZ9riMODYjMbU1%2Fg2rFLO3RWpt03w8a3MUMLh7kVJLWiZ8tInTNksDAzXM9jNAE140qG8X3yItHCX54Mo4NY90ynRzfTIo67VMxGQ2GMabgP4j1%2BS%2B2cLqy14rgOAfwWr71Bz3dfxZz05Y%2FIJ7XwAEz9cX9txHtmK2hcBFp24UlqnDH5dOrnJDBODUE4TLtAh780KEYrxHviGSA%2BuYMQ1iPJfjBqmFGyCrcpzURjHvWlL2sQ0JaESfBhle4UR3G6zswfcEk%2BBecJ8MFIQ8dmiqeahkkuLPI%2B8fVySlWim1kfxiXCgwgGgXPcWjs0rjYz3f632TylZOIk%2BwQKPVBnZ%2FM2E8NR84Wr4hBwUTQBfA7%2FRnQiRGoVF9rO%2B5V2KycsdHUtD4PnlaeYxA8EazE4cz73v4dDZzNfkvlnnVDLjbNMw%2Fec1EYeEXYQ1%2B04%2BH5UMsB9lxD82rmyZOr0Nd9sJEj%2BsT9TiBR6Wgz71rn9f9fz0ondPDCa0zmyvXANYTvS8g%2BpSzKi9ski2fcMtLurm0PkXdtbw0VXUopJapDthZ8qPpApMKKck70GOqUBAYWWeNjzLlgMBhKPmXXyfK4q2Mbm1ftufj53u7Ah%2FP0JVu3o13pY4SolmRHZyREN0lViyFPC%2F2sI9eGgil5nSpXnHn1jfIzxq%2FqXrGMCsQekzJRdQgj7jHiEcBqzE%2FUIki5JxtUv70S3Dddrk7CdOlFYFrsUB3dMrIUpcMznJNmX7IZiGY%2BKJpUfhVEnM1jp9mAiyam41oNQuyrMbSSsPMS%2F4nSD&X-Amz-Signature=9f09d577d1f94e575a83dcafeed0231071a51a7ad448683ede3df94a1fb5b2ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNRIIV3G%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQC0LRPjaVpJt0cxmkryZZVxDF0UhlpmzkOdsqYVBnlaSgIgY4xoR5l734wKg8t6iXHbrrdUPhSZss1zMTU0LLogCRMq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDAY0A78ID9oiLhnYBCrcA8NCPjJ%2B6h6sqH4mts0zjPLHmZL7juc3OHRw0b2FKDR8ANj4vzSz%2BHh3saZv2YuVFslPMyS%2FzwvNaZ9riMODYjMbU1%2Fg2rFLO3RWpt03w8a3MUMLh7kVJLWiZ8tInTNksDAzXM9jNAE140qG8X3yItHCX54Mo4NY90ynRzfTIo67VMxGQ2GMabgP4j1%2BS%2B2cLqy14rgOAfwWr71Bz3dfxZz05Y%2FIJ7XwAEz9cX9txHtmK2hcBFp24UlqnDH5dOrnJDBODUE4TLtAh780KEYrxHviGSA%2BuYMQ1iPJfjBqmFGyCrcpzURjHvWlL2sQ0JaESfBhle4UR3G6zswfcEk%2BBecJ8MFIQ8dmiqeahkkuLPI%2B8fVySlWim1kfxiXCgwgGgXPcWjs0rjYz3f632TylZOIk%2BwQKPVBnZ%2FM2E8NR84Wr4hBwUTQBfA7%2FRnQiRGoVF9rO%2B5V2KycsdHUtD4PnlaeYxA8EazE4cz73v4dDZzNfkvlnnVDLjbNMw%2Fec1EYeEXYQ1%2B04%2BH5UMsB9lxD82rmyZOr0Nd9sJEj%2BsT9TiBR6Wgz71rn9f9fz0ondPDCa0zmyvXANYTvS8g%2BpSzKi9ski2fcMtLurm0PkXdtbw0VXUopJapDthZ8qPpApMKKck70GOqUBAYWWeNjzLlgMBhKPmXXyfK4q2Mbm1ftufj53u7Ah%2FP0JVu3o13pY4SolmRHZyREN0lViyFPC%2F2sI9eGgil5nSpXnHn1jfIzxq%2FqXrGMCsQekzJRdQgj7jHiEcBqzE%2FUIki5JxtUv70S3Dddrk7CdOlFYFrsUB3dMrIUpcMznJNmX7IZiGY%2BKJpUfhVEnM1jp9mAiyam41oNQuyrMbSSsPMS%2F4nSD&X-Amz-Signature=5f9cee9ccac9f1b9cf233de3192d4fa9f3973305b6440f3c6afe491a9da180b6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
