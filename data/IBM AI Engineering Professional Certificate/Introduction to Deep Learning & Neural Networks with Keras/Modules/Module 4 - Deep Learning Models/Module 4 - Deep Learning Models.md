

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKZZWEU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL5I%2FTiw6kz63PCqMBB2DL4UMdhZhytJJfd7mWTtjxsQIhAM%2BUC%2BsjasP%2Fg8FHtoDqAvg23U269Sz%2FLU05aQH1lEihKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxA4anwQZ8PGWYRBisq3APRy2OjlVp7dZ7KqT8DAZ3m93SU7eM6MGduXW43b%2BAllwnsddLTfnkfq%2Fm%2FOmegu7X4qSQKz%2Fgrtto7VtsuT54JxoTd4%2Ba9rEyuN%2Fr1qzx%2FlrJWnx%2Fn3aknyjjTIUeWXbzTdNyitqx6XsgCQMrhwQajn1eBqwCtdjgB8%2B5VkQaoNPfZLQrTDRVeZ1hhvis%2FQZjVkylkfi0NIOIofmXREuTKxqLuYCSk%2FVFuo%2BaVUYrV%2FVgTEGfSPxbyhOuUz1G7uuv12uN%2FY9P6lfSkQpGkaOB%2BsTJtYEcJc%2FQp0r2Kbw9ERCPKFWcdBlZELN58Ii0ljfN1%2B%2Ba2i2KMChJwM5WG4eKidqfZHwtg2BHYl%2FWD6%2FTQXGgAvZbQNPBpGLiq6glBiwD%2FBAx2jr%2FG3tUoX5xwTKzr3BftIwm8zp56kKrMNdIHNsP%2FpJDnyeXf0kU8z%2BvPuMDVm%2BcT2fr9gZeAsXC1pqoS9bjuhhxyBWQEuvEYl%2BfegDw4%2BtNaxbpC6abFFjqdkrm2PxKqpkTAjm8YitnJMNqYzbdCxJ2MtUi76aOCVWQh5fZKRZGnt7ba6kxXf%2BmfCZUYgXyXpzTdjJkhd5GFzCfYsnBMhuzXQUgaTJa9pRWKvI3GaHU95lTeCqmgCjC26%2FO8BjqkAQHL9LuolU1w5%2Fx%2FtH2o0orG08EiUeXh76tGXucLr9leAMD1ca158eCumPVvFNxs24cZf3OhodHFjGJMyPX7UcHFZs%2FGXqVuEawujmnzTIpny4YJzJOEFFxf%2B29V3jbXq4uuHqGLviW7N0Of3GCd0dTOt0RzmLs3O6g64i%2FLdZs0zqrtjMA50WIQN6ffX7ZuqQnqw%2B670lHsS8XKkOMVKtyHRJaQ&X-Amz-Signature=991895d67965de33c23c2b9dbb3b624ca38ac227a7a6c7fea8cef65390bede12&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKZZWEU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL5I%2FTiw6kz63PCqMBB2DL4UMdhZhytJJfd7mWTtjxsQIhAM%2BUC%2BsjasP%2Fg8FHtoDqAvg23U269Sz%2FLU05aQH1lEihKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxA4anwQZ8PGWYRBisq3APRy2OjlVp7dZ7KqT8DAZ3m93SU7eM6MGduXW43b%2BAllwnsddLTfnkfq%2Fm%2FOmegu7X4qSQKz%2Fgrtto7VtsuT54JxoTd4%2Ba9rEyuN%2Fr1qzx%2FlrJWnx%2Fn3aknyjjTIUeWXbzTdNyitqx6XsgCQMrhwQajn1eBqwCtdjgB8%2B5VkQaoNPfZLQrTDRVeZ1hhvis%2FQZjVkylkfi0NIOIofmXREuTKxqLuYCSk%2FVFuo%2BaVUYrV%2FVgTEGfSPxbyhOuUz1G7uuv12uN%2FY9P6lfSkQpGkaOB%2BsTJtYEcJc%2FQp0r2Kbw9ERCPKFWcdBlZELN58Ii0ljfN1%2B%2Ba2i2KMChJwM5WG4eKidqfZHwtg2BHYl%2FWD6%2FTQXGgAvZbQNPBpGLiq6glBiwD%2FBAx2jr%2FG3tUoX5xwTKzr3BftIwm8zp56kKrMNdIHNsP%2FpJDnyeXf0kU8z%2BvPuMDVm%2BcT2fr9gZeAsXC1pqoS9bjuhhxyBWQEuvEYl%2BfegDw4%2BtNaxbpC6abFFjqdkrm2PxKqpkTAjm8YitnJMNqYzbdCxJ2MtUi76aOCVWQh5fZKRZGnt7ba6kxXf%2BmfCZUYgXyXpzTdjJkhd5GFzCfYsnBMhuzXQUgaTJa9pRWKvI3GaHU95lTeCqmgCjC26%2FO8BjqkAQHL9LuolU1w5%2Fx%2FtH2o0orG08EiUeXh76tGXucLr9leAMD1ca158eCumPVvFNxs24cZf3OhodHFjGJMyPX7UcHFZs%2FGXqVuEawujmnzTIpny4YJzJOEFFxf%2B29V3jbXq4uuHqGLviW7N0Of3GCd0dTOt0RzmLs3O6g64i%2FLdZs0zqrtjMA50WIQN6ffX7ZuqQnqw%2B670lHsS8XKkOMVKtyHRJaQ&X-Amz-Signature=abd9017bd7a9dcdf1782d8cc96e9a15fbf8e4ca26135c2b00c9fcbde0cf82ef9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKZZWEU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL5I%2FTiw6kz63PCqMBB2DL4UMdhZhytJJfd7mWTtjxsQIhAM%2BUC%2BsjasP%2Fg8FHtoDqAvg23U269Sz%2FLU05aQH1lEihKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxA4anwQZ8PGWYRBisq3APRy2OjlVp7dZ7KqT8DAZ3m93SU7eM6MGduXW43b%2BAllwnsddLTfnkfq%2Fm%2FOmegu7X4qSQKz%2Fgrtto7VtsuT54JxoTd4%2Ba9rEyuN%2Fr1qzx%2FlrJWnx%2Fn3aknyjjTIUeWXbzTdNyitqx6XsgCQMrhwQajn1eBqwCtdjgB8%2B5VkQaoNPfZLQrTDRVeZ1hhvis%2FQZjVkylkfi0NIOIofmXREuTKxqLuYCSk%2FVFuo%2BaVUYrV%2FVgTEGfSPxbyhOuUz1G7uuv12uN%2FY9P6lfSkQpGkaOB%2BsTJtYEcJc%2FQp0r2Kbw9ERCPKFWcdBlZELN58Ii0ljfN1%2B%2Ba2i2KMChJwM5WG4eKidqfZHwtg2BHYl%2FWD6%2FTQXGgAvZbQNPBpGLiq6glBiwD%2FBAx2jr%2FG3tUoX5xwTKzr3BftIwm8zp56kKrMNdIHNsP%2FpJDnyeXf0kU8z%2BvPuMDVm%2BcT2fr9gZeAsXC1pqoS9bjuhhxyBWQEuvEYl%2BfegDw4%2BtNaxbpC6abFFjqdkrm2PxKqpkTAjm8YitnJMNqYzbdCxJ2MtUi76aOCVWQh5fZKRZGnt7ba6kxXf%2BmfCZUYgXyXpzTdjJkhd5GFzCfYsnBMhuzXQUgaTJa9pRWKvI3GaHU95lTeCqmgCjC26%2FO8BjqkAQHL9LuolU1w5%2Fx%2FtH2o0orG08EiUeXh76tGXucLr9leAMD1ca158eCumPVvFNxs24cZf3OhodHFjGJMyPX7UcHFZs%2FGXqVuEawujmnzTIpny4YJzJOEFFxf%2B29V3jbXq4uuHqGLviW7N0Of3GCd0dTOt0RzmLs3O6g64i%2FLdZs0zqrtjMA50WIQN6ffX7ZuqQnqw%2B670lHsS8XKkOMVKtyHRJaQ&X-Amz-Signature=83e91e4113c61cbb85066079b0d62d7698fddaea53fdf865e6b162a6f7769dc0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKZZWEU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL5I%2FTiw6kz63PCqMBB2DL4UMdhZhytJJfd7mWTtjxsQIhAM%2BUC%2BsjasP%2Fg8FHtoDqAvg23U269Sz%2FLU05aQH1lEihKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxA4anwQZ8PGWYRBisq3APRy2OjlVp7dZ7KqT8DAZ3m93SU7eM6MGduXW43b%2BAllwnsddLTfnkfq%2Fm%2FOmegu7X4qSQKz%2Fgrtto7VtsuT54JxoTd4%2Ba9rEyuN%2Fr1qzx%2FlrJWnx%2Fn3aknyjjTIUeWXbzTdNyitqx6XsgCQMrhwQajn1eBqwCtdjgB8%2B5VkQaoNPfZLQrTDRVeZ1hhvis%2FQZjVkylkfi0NIOIofmXREuTKxqLuYCSk%2FVFuo%2BaVUYrV%2FVgTEGfSPxbyhOuUz1G7uuv12uN%2FY9P6lfSkQpGkaOB%2BsTJtYEcJc%2FQp0r2Kbw9ERCPKFWcdBlZELN58Ii0ljfN1%2B%2Ba2i2KMChJwM5WG4eKidqfZHwtg2BHYl%2FWD6%2FTQXGgAvZbQNPBpGLiq6glBiwD%2FBAx2jr%2FG3tUoX5xwTKzr3BftIwm8zp56kKrMNdIHNsP%2FpJDnyeXf0kU8z%2BvPuMDVm%2BcT2fr9gZeAsXC1pqoS9bjuhhxyBWQEuvEYl%2BfegDw4%2BtNaxbpC6abFFjqdkrm2PxKqpkTAjm8YitnJMNqYzbdCxJ2MtUi76aOCVWQh5fZKRZGnt7ba6kxXf%2BmfCZUYgXyXpzTdjJkhd5GFzCfYsnBMhuzXQUgaTJa9pRWKvI3GaHU95lTeCqmgCjC26%2FO8BjqkAQHL9LuolU1w5%2Fx%2FtH2o0orG08EiUeXh76tGXucLr9leAMD1ca158eCumPVvFNxs24cZf3OhodHFjGJMyPX7UcHFZs%2FGXqVuEawujmnzTIpny4YJzJOEFFxf%2B29V3jbXq4uuHqGLviW7N0Of3GCd0dTOt0RzmLs3O6g64i%2FLdZs0zqrtjMA50WIQN6ffX7ZuqQnqw%2B670lHsS8XKkOMVKtyHRJaQ&X-Amz-Signature=6620e33658cdf44fb6d235e12a0916d2343f9c5dbe523ca75ad258a6049bb6ab&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKZZWEU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL5I%2FTiw6kz63PCqMBB2DL4UMdhZhytJJfd7mWTtjxsQIhAM%2BUC%2BsjasP%2Fg8FHtoDqAvg23U269Sz%2FLU05aQH1lEihKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxA4anwQZ8PGWYRBisq3APRy2OjlVp7dZ7KqT8DAZ3m93SU7eM6MGduXW43b%2BAllwnsddLTfnkfq%2Fm%2FOmegu7X4qSQKz%2Fgrtto7VtsuT54JxoTd4%2Ba9rEyuN%2Fr1qzx%2FlrJWnx%2Fn3aknyjjTIUeWXbzTdNyitqx6XsgCQMrhwQajn1eBqwCtdjgB8%2B5VkQaoNPfZLQrTDRVeZ1hhvis%2FQZjVkylkfi0NIOIofmXREuTKxqLuYCSk%2FVFuo%2BaVUYrV%2FVgTEGfSPxbyhOuUz1G7uuv12uN%2FY9P6lfSkQpGkaOB%2BsTJtYEcJc%2FQp0r2Kbw9ERCPKFWcdBlZELN58Ii0ljfN1%2B%2Ba2i2KMChJwM5WG4eKidqfZHwtg2BHYl%2FWD6%2FTQXGgAvZbQNPBpGLiq6glBiwD%2FBAx2jr%2FG3tUoX5xwTKzr3BftIwm8zp56kKrMNdIHNsP%2FpJDnyeXf0kU8z%2BvPuMDVm%2BcT2fr9gZeAsXC1pqoS9bjuhhxyBWQEuvEYl%2BfegDw4%2BtNaxbpC6abFFjqdkrm2PxKqpkTAjm8YitnJMNqYzbdCxJ2MtUi76aOCVWQh5fZKRZGnt7ba6kxXf%2BmfCZUYgXyXpzTdjJkhd5GFzCfYsnBMhuzXQUgaTJa9pRWKvI3GaHU95lTeCqmgCjC26%2FO8BjqkAQHL9LuolU1w5%2Fx%2FtH2o0orG08EiUeXh76tGXucLr9leAMD1ca158eCumPVvFNxs24cZf3OhodHFjGJMyPX7UcHFZs%2FGXqVuEawujmnzTIpny4YJzJOEFFxf%2B29V3jbXq4uuHqGLviW7N0Of3GCd0dTOt0RzmLs3O6g64i%2FLdZs0zqrtjMA50WIQN6ffX7ZuqQnqw%2B670lHsS8XKkOMVKtyHRJaQ&X-Amz-Signature=8fd722606ba74ecdc51ead98b4413732ef59dacda912688588f77f09947bbdbd&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKZZWEU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL5I%2FTiw6kz63PCqMBB2DL4UMdhZhytJJfd7mWTtjxsQIhAM%2BUC%2BsjasP%2Fg8FHtoDqAvg23U269Sz%2FLU05aQH1lEihKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxA4anwQZ8PGWYRBisq3APRy2OjlVp7dZ7KqT8DAZ3m93SU7eM6MGduXW43b%2BAllwnsddLTfnkfq%2Fm%2FOmegu7X4qSQKz%2Fgrtto7VtsuT54JxoTd4%2Ba9rEyuN%2Fr1qzx%2FlrJWnx%2Fn3aknyjjTIUeWXbzTdNyitqx6XsgCQMrhwQajn1eBqwCtdjgB8%2B5VkQaoNPfZLQrTDRVeZ1hhvis%2FQZjVkylkfi0NIOIofmXREuTKxqLuYCSk%2FVFuo%2BaVUYrV%2FVgTEGfSPxbyhOuUz1G7uuv12uN%2FY9P6lfSkQpGkaOB%2BsTJtYEcJc%2FQp0r2Kbw9ERCPKFWcdBlZELN58Ii0ljfN1%2B%2Ba2i2KMChJwM5WG4eKidqfZHwtg2BHYl%2FWD6%2FTQXGgAvZbQNPBpGLiq6glBiwD%2FBAx2jr%2FG3tUoX5xwTKzr3BftIwm8zp56kKrMNdIHNsP%2FpJDnyeXf0kU8z%2BvPuMDVm%2BcT2fr9gZeAsXC1pqoS9bjuhhxyBWQEuvEYl%2BfegDw4%2BtNaxbpC6abFFjqdkrm2PxKqpkTAjm8YitnJMNqYzbdCxJ2MtUi76aOCVWQh5fZKRZGnt7ba6kxXf%2BmfCZUYgXyXpzTdjJkhd5GFzCfYsnBMhuzXQUgaTJa9pRWKvI3GaHU95lTeCqmgCjC26%2FO8BjqkAQHL9LuolU1w5%2Fx%2FtH2o0orG08EiUeXh76tGXucLr9leAMD1ca158eCumPVvFNxs24cZf3OhodHFjGJMyPX7UcHFZs%2FGXqVuEawujmnzTIpny4YJzJOEFFxf%2B29V3jbXq4uuHqGLviW7N0Of3GCd0dTOt0RzmLs3O6g64i%2FLdZs0zqrtjMA50WIQN6ffX7ZuqQnqw%2B670lHsS8XKkOMVKtyHRJaQ&X-Amz-Signature=2fef5a7a437f153f08f37dc3fe351f74102492c3d631a0820ef7515c0e810bc1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKZZWEU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL5I%2FTiw6kz63PCqMBB2DL4UMdhZhytJJfd7mWTtjxsQIhAM%2BUC%2BsjasP%2Fg8FHtoDqAvg23U269Sz%2FLU05aQH1lEihKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxA4anwQZ8PGWYRBisq3APRy2OjlVp7dZ7KqT8DAZ3m93SU7eM6MGduXW43b%2BAllwnsddLTfnkfq%2Fm%2FOmegu7X4qSQKz%2Fgrtto7VtsuT54JxoTd4%2Ba9rEyuN%2Fr1qzx%2FlrJWnx%2Fn3aknyjjTIUeWXbzTdNyitqx6XsgCQMrhwQajn1eBqwCtdjgB8%2B5VkQaoNPfZLQrTDRVeZ1hhvis%2FQZjVkylkfi0NIOIofmXREuTKxqLuYCSk%2FVFuo%2BaVUYrV%2FVgTEGfSPxbyhOuUz1G7uuv12uN%2FY9P6lfSkQpGkaOB%2BsTJtYEcJc%2FQp0r2Kbw9ERCPKFWcdBlZELN58Ii0ljfN1%2B%2Ba2i2KMChJwM5WG4eKidqfZHwtg2BHYl%2FWD6%2FTQXGgAvZbQNPBpGLiq6glBiwD%2FBAx2jr%2FG3tUoX5xwTKzr3BftIwm8zp56kKrMNdIHNsP%2FpJDnyeXf0kU8z%2BvPuMDVm%2BcT2fr9gZeAsXC1pqoS9bjuhhxyBWQEuvEYl%2BfegDw4%2BtNaxbpC6abFFjqdkrm2PxKqpkTAjm8YitnJMNqYzbdCxJ2MtUi76aOCVWQh5fZKRZGnt7ba6kxXf%2BmfCZUYgXyXpzTdjJkhd5GFzCfYsnBMhuzXQUgaTJa9pRWKvI3GaHU95lTeCqmgCjC26%2FO8BjqkAQHL9LuolU1w5%2Fx%2FtH2o0orG08EiUeXh76tGXucLr9leAMD1ca158eCumPVvFNxs24cZf3OhodHFjGJMyPX7UcHFZs%2FGXqVuEawujmnzTIpny4YJzJOEFFxf%2B29V3jbXq4uuHqGLviW7N0Of3GCd0dTOt0RzmLs3O6g64i%2FLdZs0zqrtjMA50WIQN6ffX7ZuqQnqw%2B670lHsS8XKkOMVKtyHRJaQ&X-Amz-Signature=451789791eb7c9151be7cebd197811cac2d0329a4fc905fbff7fef8344908414&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKZZWEU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL5I%2FTiw6kz63PCqMBB2DL4UMdhZhytJJfd7mWTtjxsQIhAM%2BUC%2BsjasP%2Fg8FHtoDqAvg23U269Sz%2FLU05aQH1lEihKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxA4anwQZ8PGWYRBisq3APRy2OjlVp7dZ7KqT8DAZ3m93SU7eM6MGduXW43b%2BAllwnsddLTfnkfq%2Fm%2FOmegu7X4qSQKz%2Fgrtto7VtsuT54JxoTd4%2Ba9rEyuN%2Fr1qzx%2FlrJWnx%2Fn3aknyjjTIUeWXbzTdNyitqx6XsgCQMrhwQajn1eBqwCtdjgB8%2B5VkQaoNPfZLQrTDRVeZ1hhvis%2FQZjVkylkfi0NIOIofmXREuTKxqLuYCSk%2FVFuo%2BaVUYrV%2FVgTEGfSPxbyhOuUz1G7uuv12uN%2FY9P6lfSkQpGkaOB%2BsTJtYEcJc%2FQp0r2Kbw9ERCPKFWcdBlZELN58Ii0ljfN1%2B%2Ba2i2KMChJwM5WG4eKidqfZHwtg2BHYl%2FWD6%2FTQXGgAvZbQNPBpGLiq6glBiwD%2FBAx2jr%2FG3tUoX5xwTKzr3BftIwm8zp56kKrMNdIHNsP%2FpJDnyeXf0kU8z%2BvPuMDVm%2BcT2fr9gZeAsXC1pqoS9bjuhhxyBWQEuvEYl%2BfegDw4%2BtNaxbpC6abFFjqdkrm2PxKqpkTAjm8YitnJMNqYzbdCxJ2MtUi76aOCVWQh5fZKRZGnt7ba6kxXf%2BmfCZUYgXyXpzTdjJkhd5GFzCfYsnBMhuzXQUgaTJa9pRWKvI3GaHU95lTeCqmgCjC26%2FO8BjqkAQHL9LuolU1w5%2Fx%2FtH2o0orG08EiUeXh76tGXucLr9leAMD1ca158eCumPVvFNxs24cZf3OhodHFjGJMyPX7UcHFZs%2FGXqVuEawujmnzTIpny4YJzJOEFFxf%2B29V3jbXq4uuHqGLviW7N0Of3GCd0dTOt0RzmLs3O6g64i%2FLdZs0zqrtjMA50WIQN6ffX7ZuqQnqw%2B670lHsS8XKkOMVKtyHRJaQ&X-Amz-Signature=b2b61844c0f936b34d382eaef315593b0552db0f34e0809af24a509ff45a5494&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLKZZWEU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL5I%2FTiw6kz63PCqMBB2DL4UMdhZhytJJfd7mWTtjxsQIhAM%2BUC%2BsjasP%2Fg8FHtoDqAvg23U269Sz%2FLU05aQH1lEihKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxA4anwQZ8PGWYRBisq3APRy2OjlVp7dZ7KqT8DAZ3m93SU7eM6MGduXW43b%2BAllwnsddLTfnkfq%2Fm%2FOmegu7X4qSQKz%2Fgrtto7VtsuT54JxoTd4%2Ba9rEyuN%2Fr1qzx%2FlrJWnx%2Fn3aknyjjTIUeWXbzTdNyitqx6XsgCQMrhwQajn1eBqwCtdjgB8%2B5VkQaoNPfZLQrTDRVeZ1hhvis%2FQZjVkylkfi0NIOIofmXREuTKxqLuYCSk%2FVFuo%2BaVUYrV%2FVgTEGfSPxbyhOuUz1G7uuv12uN%2FY9P6lfSkQpGkaOB%2BsTJtYEcJc%2FQp0r2Kbw9ERCPKFWcdBlZELN58Ii0ljfN1%2B%2Ba2i2KMChJwM5WG4eKidqfZHwtg2BHYl%2FWD6%2FTQXGgAvZbQNPBpGLiq6glBiwD%2FBAx2jr%2FG3tUoX5xwTKzr3BftIwm8zp56kKrMNdIHNsP%2FpJDnyeXf0kU8z%2BvPuMDVm%2BcT2fr9gZeAsXC1pqoS9bjuhhxyBWQEuvEYl%2BfegDw4%2BtNaxbpC6abFFjqdkrm2PxKqpkTAjm8YitnJMNqYzbdCxJ2MtUi76aOCVWQh5fZKRZGnt7ba6kxXf%2BmfCZUYgXyXpzTdjJkhd5GFzCfYsnBMhuzXQUgaTJa9pRWKvI3GaHU95lTeCqmgCjC26%2FO8BjqkAQHL9LuolU1w5%2Fx%2FtH2o0orG08EiUeXh76tGXucLr9leAMD1ca158eCumPVvFNxs24cZf3OhodHFjGJMyPX7UcHFZs%2FGXqVuEawujmnzTIpny4YJzJOEFFxf%2B29V3jbXq4uuHqGLviW7N0Of3GCd0dTOt0RzmLs3O6g64i%2FLdZs0zqrtjMA50WIQN6ffX7ZuqQnqw%2B670lHsS8XKkOMVKtyHRJaQ&X-Amz-Signature=7bba5949dc57b82a29353193e580b2a84b38865d2b18e0931fa3e59cd9e2d51d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6HG3HRH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs3kS8wPWsOWZHMRAh%2BSqTQF%2FBXG%2B5ZXYsGpsx1oJMhAIhAImhbxF7229IbjvDFJBTWOrNUmmXt%2ByspfoUm9Ns8AC8KogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfIPs%2BE%2FQK6wOxQBIq3ANNeEDMFM7MGC%2FUm7BQl0YNrXyLYQ5vlvri5JNdjU5ep4%2BJ3bY1XytHeOwuSJeD%2BqBg8Dh5KpqAK%2FiucPMBk7i5KS11%2B7fTFi5Rg4aYt5vwVIkrVaRqGbkoclGAuI%2FdV0vOqO9rGBw1Te2LBPHih5cHmH8yakETX%2Bx4qCvxV7qUUyVkbhe6dDH%2FwN95kzQkA9aqe3sdlvL%2FyWfxEi7Uk16BXZo0HlkC6oqYRjJuiCwgAf2ra8yRvL0Z5dte3tKAV8wMKLN3snNMwt6VdoAqxgCDFrba9FihwsR6bwByT5uFELdY2sDyvsHTeEWObyL9ZPm2HEWHKiDxjLsGjeH99N7KwaCaNJNskov%2Bqwl2%2FYO8%2B1b3ijRiI0Wpt8RNxDhKbzy7OwrxTGHaIQvVYzi%2BFaK5USVeT5Mp72w9XJMBvRq7Zhxc1I5OHdgDkbJrfY7McM47dJcSjI7S%2BEPEZrT7sKW7%2BxFZrMdLWnBYdVAz%2FGb4ToULTxq%2FZaCYRwGaokD6u6PD%2FoyWYpWZzzmAveaQ7zff4cMNs88bFDwVPuK2ieGlasLzbjiRc4nEIAb%2FQxT8FeuYeWnjPDQ8QdW%2Fxg3dqIau3F%2B%2BnpuFYmGFKpOU3npaikIIWFHOyGaXWgDMEjDkh%2FS8BjqkAenjRNzomTDRT%2FdFHgR6pRQoNWlteAx6hK%2BWkpJQSVziC%2BBrxnSpxY98GgerHrgXMuaecoG5BYIou%2BbyYezWzVCXudxUNqAbZYIaitb1%2Fhmn95pehcufBYGgiO7GJS981%2BPXWLJ1hjaIuBLFAgpwbqOv1PKGWsyUKoAP%2FHoSKY6UeMqgKJJ6AMWT8lQSE8%2Bw%2Frv0SeBwuFY7I39yOVmTFf70TPz4&X-Amz-Signature=2db62ecda7ca5b544b340a3965c68bf273268a4a9a7932743c296710cd73864c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6HG3HRH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs3kS8wPWsOWZHMRAh%2BSqTQF%2FBXG%2B5ZXYsGpsx1oJMhAIhAImhbxF7229IbjvDFJBTWOrNUmmXt%2ByspfoUm9Ns8AC8KogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfIPs%2BE%2FQK6wOxQBIq3ANNeEDMFM7MGC%2FUm7BQl0YNrXyLYQ5vlvri5JNdjU5ep4%2BJ3bY1XytHeOwuSJeD%2BqBg8Dh5KpqAK%2FiucPMBk7i5KS11%2B7fTFi5Rg4aYt5vwVIkrVaRqGbkoclGAuI%2FdV0vOqO9rGBw1Te2LBPHih5cHmH8yakETX%2Bx4qCvxV7qUUyVkbhe6dDH%2FwN95kzQkA9aqe3sdlvL%2FyWfxEi7Uk16BXZo0HlkC6oqYRjJuiCwgAf2ra8yRvL0Z5dte3tKAV8wMKLN3snNMwt6VdoAqxgCDFrba9FihwsR6bwByT5uFELdY2sDyvsHTeEWObyL9ZPm2HEWHKiDxjLsGjeH99N7KwaCaNJNskov%2Bqwl2%2FYO8%2B1b3ijRiI0Wpt8RNxDhKbzy7OwrxTGHaIQvVYzi%2BFaK5USVeT5Mp72w9XJMBvRq7Zhxc1I5OHdgDkbJrfY7McM47dJcSjI7S%2BEPEZrT7sKW7%2BxFZrMdLWnBYdVAz%2FGb4ToULTxq%2FZaCYRwGaokD6u6PD%2FoyWYpWZzzmAveaQ7zff4cMNs88bFDwVPuK2ieGlasLzbjiRc4nEIAb%2FQxT8FeuYeWnjPDQ8QdW%2Fxg3dqIau3F%2B%2BnpuFYmGFKpOU3npaikIIWFHOyGaXWgDMEjDkh%2FS8BjqkAenjRNzomTDRT%2FdFHgR6pRQoNWlteAx6hK%2BWkpJQSVziC%2BBrxnSpxY98GgerHrgXMuaecoG5BYIou%2BbyYezWzVCXudxUNqAbZYIaitb1%2Fhmn95pehcufBYGgiO7GJS981%2BPXWLJ1hjaIuBLFAgpwbqOv1PKGWsyUKoAP%2FHoSKY6UeMqgKJJ6AMWT8lQSE8%2Bw%2Frv0SeBwuFY7I39yOVmTFf70TPz4&X-Amz-Signature=dcd66567b3cb62b88c59164666e57b23fd9b73b6cb1aa2cde4ff4c941e43feac&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
