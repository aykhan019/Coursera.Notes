

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WK3IOG2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICGR88TQtlVBuINBaO9LAqBEQVR6Cx%2Bp0ohQ3LIxb4DMAiEAylAK6OBsH564eErhMWe%2Bb2Nkm%2B2btvM%2FqaHy%2FGDeD4gqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGmI%2FEeXSpO9SPEWfircA9KQdzMqpqsTLdMXX5%2FF4tiNvuXUK%2FxtGJhdFsielmiER%2FNftxveba8MIDwBRq6CXGwhqHhDXti9R8nV55qMIjw6205Ny%2FdxZ%2BQX7YKVFMka9rmD%2B2sQU271mxHAsICNlZaBQEXBJP0v%2BbjNv15AR2Uxhfjp0NRjEwl5AwRdU5oicw3NnF%2BZkaDVQBnxX8asjqcey0ZvXx24%2BKYq8XcAg8zozyZ3sxx3YY5OQXZ%2Brcy1CCNPh2SvjckxYYR6lMoBudsPOTc4Xt3agtMgSGKZsc9reenGbtBVKOEb7fI7aFCUxAYJ%2FTQRWFl5dglZRIUDDDQpsN8HJPILXJqZLGy0IVRY%2FoS3FxUDcsSYmD0AkiLDShdPw0D0NAAr5XydbayFGcnG1tZA87c%2BpVSM8b35IOtdM8bTO081Sc8VncNvh3IiFr50KnIbwVAPiXhvJufu8CaMW%2FKYVv7F2%2BP9E6E%2B14szlLaYptLSHS1oa8xMieTjesGuUoh7UG1eqXp1y82mZWeBoMgEqUMqw%2FqC8nBdF18IZKiHQf6swIUp3MqIJSbFl%2BpEArudaXOtwl6ZPAeoH8fAWCtRdMROvaK5BxSji9mTRKcl56IJhUmAgm7dOSwkxKFHj%2Ftu7U7WPP%2B4MPDc%2FrwGOqUB7Z%2B6uOQKkPrw2CI8VBakPNYZEDhMwJRkvrJe7BBbR%2FaRfY4dBRNix2iQgWFcBPlw7cyrr7mia9iMkmxC%2BmPsPziGcLHW99%2FHiQcLHzHTahz4kZAzatJy5v4Q%2B2ikKHf%2FT5zXUPRGifORdE4Vu%2BzY04XPaGl2f0Gq2Oi7CXafEg4a3OeC0sm0QsKU0jOSww93ejgG7aPhxfmAd09owA20dw4bI%2FZk&X-Amz-Signature=850f8f277395fe693109eed44f8c3b41aef859c8b3960e2473d4e72ec7b0efd1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WK3IOG2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICGR88TQtlVBuINBaO9LAqBEQVR6Cx%2Bp0ohQ3LIxb4DMAiEAylAK6OBsH564eErhMWe%2Bb2Nkm%2B2btvM%2FqaHy%2FGDeD4gqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGmI%2FEeXSpO9SPEWfircA9KQdzMqpqsTLdMXX5%2FF4tiNvuXUK%2FxtGJhdFsielmiER%2FNftxveba8MIDwBRq6CXGwhqHhDXti9R8nV55qMIjw6205Ny%2FdxZ%2BQX7YKVFMka9rmD%2B2sQU271mxHAsICNlZaBQEXBJP0v%2BbjNv15AR2Uxhfjp0NRjEwl5AwRdU5oicw3NnF%2BZkaDVQBnxX8asjqcey0ZvXx24%2BKYq8XcAg8zozyZ3sxx3YY5OQXZ%2Brcy1CCNPh2SvjckxYYR6lMoBudsPOTc4Xt3agtMgSGKZsc9reenGbtBVKOEb7fI7aFCUxAYJ%2FTQRWFl5dglZRIUDDDQpsN8HJPILXJqZLGy0IVRY%2FoS3FxUDcsSYmD0AkiLDShdPw0D0NAAr5XydbayFGcnG1tZA87c%2BpVSM8b35IOtdM8bTO081Sc8VncNvh3IiFr50KnIbwVAPiXhvJufu8CaMW%2FKYVv7F2%2BP9E6E%2B14szlLaYptLSHS1oa8xMieTjesGuUoh7UG1eqXp1y82mZWeBoMgEqUMqw%2FqC8nBdF18IZKiHQf6swIUp3MqIJSbFl%2BpEArudaXOtwl6ZPAeoH8fAWCtRdMROvaK5BxSji9mTRKcl56IJhUmAgm7dOSwkxKFHj%2Ftu7U7WPP%2B4MPDc%2FrwGOqUB7Z%2B6uOQKkPrw2CI8VBakPNYZEDhMwJRkvrJe7BBbR%2FaRfY4dBRNix2iQgWFcBPlw7cyrr7mia9iMkmxC%2BmPsPziGcLHW99%2FHiQcLHzHTahz4kZAzatJy5v4Q%2B2ikKHf%2FT5zXUPRGifORdE4Vu%2BzY04XPaGl2f0Gq2Oi7CXafEg4a3OeC0sm0QsKU0jOSww93ejgG7aPhxfmAd09owA20dw4bI%2FZk&X-Amz-Signature=4e768f7d827ebd4fbdc9623a43c56fa6ead2886088dce15c819b2d44c98d8a0b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WK3IOG2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICGR88TQtlVBuINBaO9LAqBEQVR6Cx%2Bp0ohQ3LIxb4DMAiEAylAK6OBsH564eErhMWe%2Bb2Nkm%2B2btvM%2FqaHy%2FGDeD4gqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGmI%2FEeXSpO9SPEWfircA9KQdzMqpqsTLdMXX5%2FF4tiNvuXUK%2FxtGJhdFsielmiER%2FNftxveba8MIDwBRq6CXGwhqHhDXti9R8nV55qMIjw6205Ny%2FdxZ%2BQX7YKVFMka9rmD%2B2sQU271mxHAsICNlZaBQEXBJP0v%2BbjNv15AR2Uxhfjp0NRjEwl5AwRdU5oicw3NnF%2BZkaDVQBnxX8asjqcey0ZvXx24%2BKYq8XcAg8zozyZ3sxx3YY5OQXZ%2Brcy1CCNPh2SvjckxYYR6lMoBudsPOTc4Xt3agtMgSGKZsc9reenGbtBVKOEb7fI7aFCUxAYJ%2FTQRWFl5dglZRIUDDDQpsN8HJPILXJqZLGy0IVRY%2FoS3FxUDcsSYmD0AkiLDShdPw0D0NAAr5XydbayFGcnG1tZA87c%2BpVSM8b35IOtdM8bTO081Sc8VncNvh3IiFr50KnIbwVAPiXhvJufu8CaMW%2FKYVv7F2%2BP9E6E%2B14szlLaYptLSHS1oa8xMieTjesGuUoh7UG1eqXp1y82mZWeBoMgEqUMqw%2FqC8nBdF18IZKiHQf6swIUp3MqIJSbFl%2BpEArudaXOtwl6ZPAeoH8fAWCtRdMROvaK5BxSji9mTRKcl56IJhUmAgm7dOSwkxKFHj%2Ftu7U7WPP%2B4MPDc%2FrwGOqUB7Z%2B6uOQKkPrw2CI8VBakPNYZEDhMwJRkvrJe7BBbR%2FaRfY4dBRNix2iQgWFcBPlw7cyrr7mia9iMkmxC%2BmPsPziGcLHW99%2FHiQcLHzHTahz4kZAzatJy5v4Q%2B2ikKHf%2FT5zXUPRGifORdE4Vu%2BzY04XPaGl2f0Gq2Oi7CXafEg4a3OeC0sm0QsKU0jOSww93ejgG7aPhxfmAd09owA20dw4bI%2FZk&X-Amz-Signature=dc6bc9adbebdec4db632a62b1a16a461fe00420ca873d8ebd2b09e941f3054f7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WK3IOG2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICGR88TQtlVBuINBaO9LAqBEQVR6Cx%2Bp0ohQ3LIxb4DMAiEAylAK6OBsH564eErhMWe%2Bb2Nkm%2B2btvM%2FqaHy%2FGDeD4gqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGmI%2FEeXSpO9SPEWfircA9KQdzMqpqsTLdMXX5%2FF4tiNvuXUK%2FxtGJhdFsielmiER%2FNftxveba8MIDwBRq6CXGwhqHhDXti9R8nV55qMIjw6205Ny%2FdxZ%2BQX7YKVFMka9rmD%2B2sQU271mxHAsICNlZaBQEXBJP0v%2BbjNv15AR2Uxhfjp0NRjEwl5AwRdU5oicw3NnF%2BZkaDVQBnxX8asjqcey0ZvXx24%2BKYq8XcAg8zozyZ3sxx3YY5OQXZ%2Brcy1CCNPh2SvjckxYYR6lMoBudsPOTc4Xt3agtMgSGKZsc9reenGbtBVKOEb7fI7aFCUxAYJ%2FTQRWFl5dglZRIUDDDQpsN8HJPILXJqZLGy0IVRY%2FoS3FxUDcsSYmD0AkiLDShdPw0D0NAAr5XydbayFGcnG1tZA87c%2BpVSM8b35IOtdM8bTO081Sc8VncNvh3IiFr50KnIbwVAPiXhvJufu8CaMW%2FKYVv7F2%2BP9E6E%2B14szlLaYptLSHS1oa8xMieTjesGuUoh7UG1eqXp1y82mZWeBoMgEqUMqw%2FqC8nBdF18IZKiHQf6swIUp3MqIJSbFl%2BpEArudaXOtwl6ZPAeoH8fAWCtRdMROvaK5BxSji9mTRKcl56IJhUmAgm7dOSwkxKFHj%2Ftu7U7WPP%2B4MPDc%2FrwGOqUB7Z%2B6uOQKkPrw2CI8VBakPNYZEDhMwJRkvrJe7BBbR%2FaRfY4dBRNix2iQgWFcBPlw7cyrr7mia9iMkmxC%2BmPsPziGcLHW99%2FHiQcLHzHTahz4kZAzatJy5v4Q%2B2ikKHf%2FT5zXUPRGifORdE4Vu%2BzY04XPaGl2f0Gq2Oi7CXafEg4a3OeC0sm0QsKU0jOSww93ejgG7aPhxfmAd09owA20dw4bI%2FZk&X-Amz-Signature=87b1a3d221b7ff5dcdb0a7e78bc11a15126761ac0b847495600f09e970e89bfb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WK3IOG2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICGR88TQtlVBuINBaO9LAqBEQVR6Cx%2Bp0ohQ3LIxb4DMAiEAylAK6OBsH564eErhMWe%2Bb2Nkm%2B2btvM%2FqaHy%2FGDeD4gqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGmI%2FEeXSpO9SPEWfircA9KQdzMqpqsTLdMXX5%2FF4tiNvuXUK%2FxtGJhdFsielmiER%2FNftxveba8MIDwBRq6CXGwhqHhDXti9R8nV55qMIjw6205Ny%2FdxZ%2BQX7YKVFMka9rmD%2B2sQU271mxHAsICNlZaBQEXBJP0v%2BbjNv15AR2Uxhfjp0NRjEwl5AwRdU5oicw3NnF%2BZkaDVQBnxX8asjqcey0ZvXx24%2BKYq8XcAg8zozyZ3sxx3YY5OQXZ%2Brcy1CCNPh2SvjckxYYR6lMoBudsPOTc4Xt3agtMgSGKZsc9reenGbtBVKOEb7fI7aFCUxAYJ%2FTQRWFl5dglZRIUDDDQpsN8HJPILXJqZLGy0IVRY%2FoS3FxUDcsSYmD0AkiLDShdPw0D0NAAr5XydbayFGcnG1tZA87c%2BpVSM8b35IOtdM8bTO081Sc8VncNvh3IiFr50KnIbwVAPiXhvJufu8CaMW%2FKYVv7F2%2BP9E6E%2B14szlLaYptLSHS1oa8xMieTjesGuUoh7UG1eqXp1y82mZWeBoMgEqUMqw%2FqC8nBdF18IZKiHQf6swIUp3MqIJSbFl%2BpEArudaXOtwl6ZPAeoH8fAWCtRdMROvaK5BxSji9mTRKcl56IJhUmAgm7dOSwkxKFHj%2Ftu7U7WPP%2B4MPDc%2FrwGOqUB7Z%2B6uOQKkPrw2CI8VBakPNYZEDhMwJRkvrJe7BBbR%2FaRfY4dBRNix2iQgWFcBPlw7cyrr7mia9iMkmxC%2BmPsPziGcLHW99%2FHiQcLHzHTahz4kZAzatJy5v4Q%2B2ikKHf%2FT5zXUPRGifORdE4Vu%2BzY04XPaGl2f0Gq2Oi7CXafEg4a3OeC0sm0QsKU0jOSww93ejgG7aPhxfmAd09owA20dw4bI%2FZk&X-Amz-Signature=7a18f4402e09228064ddb2764475a7a00ced79515ed5e28e3f8d4986766e47cf&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WK3IOG2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICGR88TQtlVBuINBaO9LAqBEQVR6Cx%2Bp0ohQ3LIxb4DMAiEAylAK6OBsH564eErhMWe%2Bb2Nkm%2B2btvM%2FqaHy%2FGDeD4gqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGmI%2FEeXSpO9SPEWfircA9KQdzMqpqsTLdMXX5%2FF4tiNvuXUK%2FxtGJhdFsielmiER%2FNftxveba8MIDwBRq6CXGwhqHhDXti9R8nV55qMIjw6205Ny%2FdxZ%2BQX7YKVFMka9rmD%2B2sQU271mxHAsICNlZaBQEXBJP0v%2BbjNv15AR2Uxhfjp0NRjEwl5AwRdU5oicw3NnF%2BZkaDVQBnxX8asjqcey0ZvXx24%2BKYq8XcAg8zozyZ3sxx3YY5OQXZ%2Brcy1CCNPh2SvjckxYYR6lMoBudsPOTc4Xt3agtMgSGKZsc9reenGbtBVKOEb7fI7aFCUxAYJ%2FTQRWFl5dglZRIUDDDQpsN8HJPILXJqZLGy0IVRY%2FoS3FxUDcsSYmD0AkiLDShdPw0D0NAAr5XydbayFGcnG1tZA87c%2BpVSM8b35IOtdM8bTO081Sc8VncNvh3IiFr50KnIbwVAPiXhvJufu8CaMW%2FKYVv7F2%2BP9E6E%2B14szlLaYptLSHS1oa8xMieTjesGuUoh7UG1eqXp1y82mZWeBoMgEqUMqw%2FqC8nBdF18IZKiHQf6swIUp3MqIJSbFl%2BpEArudaXOtwl6ZPAeoH8fAWCtRdMROvaK5BxSji9mTRKcl56IJhUmAgm7dOSwkxKFHj%2Ftu7U7WPP%2B4MPDc%2FrwGOqUB7Z%2B6uOQKkPrw2CI8VBakPNYZEDhMwJRkvrJe7BBbR%2FaRfY4dBRNix2iQgWFcBPlw7cyrr7mia9iMkmxC%2BmPsPziGcLHW99%2FHiQcLHzHTahz4kZAzatJy5v4Q%2B2ikKHf%2FT5zXUPRGifORdE4Vu%2BzY04XPaGl2f0Gq2Oi7CXafEg4a3OeC0sm0QsKU0jOSww93ejgG7aPhxfmAd09owA20dw4bI%2FZk&X-Amz-Signature=5d7f856b13f6fa1d285ecd7c54e043daad52919e2d5a8d5bf85c71d0506e9e75&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WK3IOG2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICGR88TQtlVBuINBaO9LAqBEQVR6Cx%2Bp0ohQ3LIxb4DMAiEAylAK6OBsH564eErhMWe%2Bb2Nkm%2B2btvM%2FqaHy%2FGDeD4gqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGmI%2FEeXSpO9SPEWfircA9KQdzMqpqsTLdMXX5%2FF4tiNvuXUK%2FxtGJhdFsielmiER%2FNftxveba8MIDwBRq6CXGwhqHhDXti9R8nV55qMIjw6205Ny%2FdxZ%2BQX7YKVFMka9rmD%2B2sQU271mxHAsICNlZaBQEXBJP0v%2BbjNv15AR2Uxhfjp0NRjEwl5AwRdU5oicw3NnF%2BZkaDVQBnxX8asjqcey0ZvXx24%2BKYq8XcAg8zozyZ3sxx3YY5OQXZ%2Brcy1CCNPh2SvjckxYYR6lMoBudsPOTc4Xt3agtMgSGKZsc9reenGbtBVKOEb7fI7aFCUxAYJ%2FTQRWFl5dglZRIUDDDQpsN8HJPILXJqZLGy0IVRY%2FoS3FxUDcsSYmD0AkiLDShdPw0D0NAAr5XydbayFGcnG1tZA87c%2BpVSM8b35IOtdM8bTO081Sc8VncNvh3IiFr50KnIbwVAPiXhvJufu8CaMW%2FKYVv7F2%2BP9E6E%2B14szlLaYptLSHS1oa8xMieTjesGuUoh7UG1eqXp1y82mZWeBoMgEqUMqw%2FqC8nBdF18IZKiHQf6swIUp3MqIJSbFl%2BpEArudaXOtwl6ZPAeoH8fAWCtRdMROvaK5BxSji9mTRKcl56IJhUmAgm7dOSwkxKFHj%2Ftu7U7WPP%2B4MPDc%2FrwGOqUB7Z%2B6uOQKkPrw2CI8VBakPNYZEDhMwJRkvrJe7BBbR%2FaRfY4dBRNix2iQgWFcBPlw7cyrr7mia9iMkmxC%2BmPsPziGcLHW99%2FHiQcLHzHTahz4kZAzatJy5v4Q%2B2ikKHf%2FT5zXUPRGifORdE4Vu%2BzY04XPaGl2f0Gq2Oi7CXafEg4a3OeC0sm0QsKU0jOSww93ejgG7aPhxfmAd09owA20dw4bI%2FZk&X-Amz-Signature=50341f7cdfbf0654a67aca459213d11b6cbbb5ecb620a54bf0af985dbabd03ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WK3IOG2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICGR88TQtlVBuINBaO9LAqBEQVR6Cx%2Bp0ohQ3LIxb4DMAiEAylAK6OBsH564eErhMWe%2Bb2Nkm%2B2btvM%2FqaHy%2FGDeD4gqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGmI%2FEeXSpO9SPEWfircA9KQdzMqpqsTLdMXX5%2FF4tiNvuXUK%2FxtGJhdFsielmiER%2FNftxveba8MIDwBRq6CXGwhqHhDXti9R8nV55qMIjw6205Ny%2FdxZ%2BQX7YKVFMka9rmD%2B2sQU271mxHAsICNlZaBQEXBJP0v%2BbjNv15AR2Uxhfjp0NRjEwl5AwRdU5oicw3NnF%2BZkaDVQBnxX8asjqcey0ZvXx24%2BKYq8XcAg8zozyZ3sxx3YY5OQXZ%2Brcy1CCNPh2SvjckxYYR6lMoBudsPOTc4Xt3agtMgSGKZsc9reenGbtBVKOEb7fI7aFCUxAYJ%2FTQRWFl5dglZRIUDDDQpsN8HJPILXJqZLGy0IVRY%2FoS3FxUDcsSYmD0AkiLDShdPw0D0NAAr5XydbayFGcnG1tZA87c%2BpVSM8b35IOtdM8bTO081Sc8VncNvh3IiFr50KnIbwVAPiXhvJufu8CaMW%2FKYVv7F2%2BP9E6E%2B14szlLaYptLSHS1oa8xMieTjesGuUoh7UG1eqXp1y82mZWeBoMgEqUMqw%2FqC8nBdF18IZKiHQf6swIUp3MqIJSbFl%2BpEArudaXOtwl6ZPAeoH8fAWCtRdMROvaK5BxSji9mTRKcl56IJhUmAgm7dOSwkxKFHj%2Ftu7U7WPP%2B4MPDc%2FrwGOqUB7Z%2B6uOQKkPrw2CI8VBakPNYZEDhMwJRkvrJe7BBbR%2FaRfY4dBRNix2iQgWFcBPlw7cyrr7mia9iMkmxC%2BmPsPziGcLHW99%2FHiQcLHzHTahz4kZAzatJy5v4Q%2B2ikKHf%2FT5zXUPRGifORdE4Vu%2BzY04XPaGl2f0Gq2Oi7CXafEg4a3OeC0sm0QsKU0jOSww93ejgG7aPhxfmAd09owA20dw4bI%2FZk&X-Amz-Signature=4266a82372b33278508f215733ed6923d1414cc7cd13f800b8596f9dddd274a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WK3IOG2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICGR88TQtlVBuINBaO9LAqBEQVR6Cx%2Bp0ohQ3LIxb4DMAiEAylAK6OBsH564eErhMWe%2Bb2Nkm%2B2btvM%2FqaHy%2FGDeD4gqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGmI%2FEeXSpO9SPEWfircA9KQdzMqpqsTLdMXX5%2FF4tiNvuXUK%2FxtGJhdFsielmiER%2FNftxveba8MIDwBRq6CXGwhqHhDXti9R8nV55qMIjw6205Ny%2FdxZ%2BQX7YKVFMka9rmD%2B2sQU271mxHAsICNlZaBQEXBJP0v%2BbjNv15AR2Uxhfjp0NRjEwl5AwRdU5oicw3NnF%2BZkaDVQBnxX8asjqcey0ZvXx24%2BKYq8XcAg8zozyZ3sxx3YY5OQXZ%2Brcy1CCNPh2SvjckxYYR6lMoBudsPOTc4Xt3agtMgSGKZsc9reenGbtBVKOEb7fI7aFCUxAYJ%2FTQRWFl5dglZRIUDDDQpsN8HJPILXJqZLGy0IVRY%2FoS3FxUDcsSYmD0AkiLDShdPw0D0NAAr5XydbayFGcnG1tZA87c%2BpVSM8b35IOtdM8bTO081Sc8VncNvh3IiFr50KnIbwVAPiXhvJufu8CaMW%2FKYVv7F2%2BP9E6E%2B14szlLaYptLSHS1oa8xMieTjesGuUoh7UG1eqXp1y82mZWeBoMgEqUMqw%2FqC8nBdF18IZKiHQf6swIUp3MqIJSbFl%2BpEArudaXOtwl6ZPAeoH8fAWCtRdMROvaK5BxSji9mTRKcl56IJhUmAgm7dOSwkxKFHj%2Ftu7U7WPP%2B4MPDc%2FrwGOqUB7Z%2B6uOQKkPrw2CI8VBakPNYZEDhMwJRkvrJe7BBbR%2FaRfY4dBRNix2iQgWFcBPlw7cyrr7mia9iMkmxC%2BmPsPziGcLHW99%2FHiQcLHzHTahz4kZAzatJy5v4Q%2B2ikKHf%2FT5zXUPRGifORdE4Vu%2BzY04XPaGl2f0Gq2Oi7CXafEg4a3OeC0sm0QsKU0jOSww93ejgG7aPhxfmAd09owA20dw4bI%2FZk&X-Amz-Signature=0164b124f79540f924dcf437d3a188ad475dbc3d85074e0a45167501c6969a5b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAQ4HNR4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAeWy8jaKrGME1r7IDeLk0XSUCtfFcWyDcZBUvk2saeJAiEA7W8%2B%2F5Ux%2FqoIQIpesxni4wWod%2BA3ecbfUi%2BrzMQqjaQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE5rP68BqHlQi8UGSSrcA5tE67xu2DJM0EaIJJ8EVxdq74j40lD92SZX1PBnFXLzTmsGGVnfetAVMJRp%2BzLGBqN%2F43%2F3iZFvx%2B4WheoRgKwa7ZCcKqCC5QgTgyHBUVVP86S%2FTa1p1%2BYMr7GEjJKFKKHLtg58PN2jTU9MBaJM4HNfS3tv8pVeKVlN9Ih1t2QRt1qGLQUypg%2Bo7Lqs8j95RCql3Zc%2F11foGwiEm2hRCdIh6Vj37Iqudi6a%2B4qzv6KMUctEIbEB9gusGwhj7M%2Fn38RgNIuxuCVCEO54w6y58X%2BUzXP5ULHihcZHkPMTw4XtTSPL2WLQu1pN8pMVUd0TbhlPt%2FCFPCN5GaEnIqZcfY0d8vZ9fklBrocswY9ZUf3%2B9vDWtAIiRlkvvp6WowHhISHP9VdvhhCZsgChBZY%2B94vD5WIuZ502pjBOb9hKSolPm6egokhP3%2Biu3raPIT4FHmzcFv1FUPgm%2FiPAQrKWacLdWKfRMdVxbbP1KoWAUNcvaprOVJHlRQsZREUQIkSV3EC7N7U2vHi05kYojuEq0BOwxs7euBB8Cx0isEYVM852hSJeS4oIpNc7ziWHh8bGQBktuOZgSLWS%2FPkWxR8gF3OBqmsxEq7Kx9Fxq%2F6hkaAIyynlFWu13k6KwSOUMLHY%2FrwGOqUBYdowLa60qArEaXPcDQSl7%2FqN5svau2Ng2yJryDhYDbfxdWFQKV%2BygujIeTkHznJzH%2F8j54JAqijaTRCg3vNwngOW69lFgw%2FrIEy4MkI5Z5loSRRV8jiPxRFU5kAroAKNtFVt1W6hpphuWd%2BFq5p480VpAJmvDqSP59MhTfZK7hlwwBnpFoo%2BMURApo9ttqnqIYTBT3aVDgfcXbvHTl8QforBWPW5&X-Amz-Signature=bc89bc9b0ed1c33646e8c3a49f15e1336bd82b87d12e4ca2a602a1c5cc47a16d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAQ4HNR4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAeWy8jaKrGME1r7IDeLk0XSUCtfFcWyDcZBUvk2saeJAiEA7W8%2B%2F5Ux%2FqoIQIpesxni4wWod%2BA3ecbfUi%2BrzMQqjaQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE5rP68BqHlQi8UGSSrcA5tE67xu2DJM0EaIJJ8EVxdq74j40lD92SZX1PBnFXLzTmsGGVnfetAVMJRp%2BzLGBqN%2F43%2F3iZFvx%2B4WheoRgKwa7ZCcKqCC5QgTgyHBUVVP86S%2FTa1p1%2BYMr7GEjJKFKKHLtg58PN2jTU9MBaJM4HNfS3tv8pVeKVlN9Ih1t2QRt1qGLQUypg%2Bo7Lqs8j95RCql3Zc%2F11foGwiEm2hRCdIh6Vj37Iqudi6a%2B4qzv6KMUctEIbEB9gusGwhj7M%2Fn38RgNIuxuCVCEO54w6y58X%2BUzXP5ULHihcZHkPMTw4XtTSPL2WLQu1pN8pMVUd0TbhlPt%2FCFPCN5GaEnIqZcfY0d8vZ9fklBrocswY9ZUf3%2B9vDWtAIiRlkvvp6WowHhISHP9VdvhhCZsgChBZY%2B94vD5WIuZ502pjBOb9hKSolPm6egokhP3%2Biu3raPIT4FHmzcFv1FUPgm%2FiPAQrKWacLdWKfRMdVxbbP1KoWAUNcvaprOVJHlRQsZREUQIkSV3EC7N7U2vHi05kYojuEq0BOwxs7euBB8Cx0isEYVM852hSJeS4oIpNc7ziWHh8bGQBktuOZgSLWS%2FPkWxR8gF3OBqmsxEq7Kx9Fxq%2F6hkaAIyynlFWu13k6KwSOUMLHY%2FrwGOqUBYdowLa60qArEaXPcDQSl7%2FqN5svau2Ng2yJryDhYDbfxdWFQKV%2BygujIeTkHznJzH%2F8j54JAqijaTRCg3vNwngOW69lFgw%2FrIEy4MkI5Z5loSRRV8jiPxRFU5kAroAKNtFVt1W6hpphuWd%2BFq5p480VpAJmvDqSP59MhTfZK7hlwwBnpFoo%2BMURApo9ttqnqIYTBT3aVDgfcXbvHTl8QforBWPW5&X-Amz-Signature=8c16c951d99fd05f9fcbad833360800b0b6ed6286678ad833be2d8e5f68b460f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
