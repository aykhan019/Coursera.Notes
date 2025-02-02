

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXPSVYFX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDO9U%2BqBjxHC13RuPvLk4gBS0WY9IEQ2JUnWK6FG9Di9AIhAPeMZE7u7uDiGnms4q0lUutoDJd8Pc%2FYxzCrC1LMW5GXKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyeqza9gm0lKnqCoU8q3AM4uRJTt5urwyzcgTvmLX4MOw53iZESlSsO1hHxS%2BqiFgeXjqgxComvWd1q%2Bpy0BMx7uWdbrvK%2BDqmcYrcbzg1buz61OgfqyQbcZTifZ4xTjpM8P%2FyfNVDp9z%2B%2BGeLh8IcD3S9ynASEqA9efKLIkPQXPpVXeNcCwgBu3WfVjA%2FcTi21BO2OEHoCfVbOcmM%2B5c5u6wgNQj%2FO8pIasSmIUXhitwGn9dTkritcPeRof3yLi7dRpxNOn%2FB50zqnMYzNtWWX53aVDG3BE9Z28pmizbg0xYo6%2FaObbGOAb%2BnKEQl%2BvaE1J1Tgf64xk1XdJbZnkSf6VQKA9WVS30LhWGL%2FVGMKyj%2BYjirpl%2FeTYOBi2N8OCi7mVvUnMW%2FYtuFZxxCJyis2iW3YBqtjb8AE8l8v33jna9a%2BJxSPOK%2BxR3bTyMEttVfulgbrRRR3Kswcfutr%2Bqwp59ZbYlSDw6%2FNIl9u%2FPOSo%2FabCTZdCawkdQlSPV%2FcS6uy%2FFDgPRYPEirGrQ3MZKHA8hjzMzR03RRjMLUO8AFBqA5nl8LZloYvokBtG6zO8Hqr0yydcgV9f9mv9oz%2FOhGpUqrrCWZ0AE2jRXf4VB26h2bxnXuToNOd7%2FfPyTL40%2Fbic7ckRqXUJ1fkgTD4m%2Fy8BjqkAeUqGZDHWchteittM5Fp2yb8leayT8tuyM%2BDh0%2BcgPHulaHORNj%2BjmKPjxGrKAgL3N28IZBh82zx2AdqF8Cc8Lqj1e3ERx5LqhyyF0DZYWDz097M1klvogb9pY98uci0OYAb%2BLpZ%2B2h24Mo16m93Iul4jQD6q1QSp4oxv%2FbHCwqxrj%2F6SKHPu4iblCq9weNIhyIdQyhMy1lBiv%2Ba8CKicE%2Fk2G3n&X-Amz-Signature=7d045c5dd7d8a7ead707ed82e4b9588d2434136d5ed6e53b3b9d07bc76bfbd6c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXPSVYFX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDO9U%2BqBjxHC13RuPvLk4gBS0WY9IEQ2JUnWK6FG9Di9AIhAPeMZE7u7uDiGnms4q0lUutoDJd8Pc%2FYxzCrC1LMW5GXKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyeqza9gm0lKnqCoU8q3AM4uRJTt5urwyzcgTvmLX4MOw53iZESlSsO1hHxS%2BqiFgeXjqgxComvWd1q%2Bpy0BMx7uWdbrvK%2BDqmcYrcbzg1buz61OgfqyQbcZTifZ4xTjpM8P%2FyfNVDp9z%2B%2BGeLh8IcD3S9ynASEqA9efKLIkPQXPpVXeNcCwgBu3WfVjA%2FcTi21BO2OEHoCfVbOcmM%2B5c5u6wgNQj%2FO8pIasSmIUXhitwGn9dTkritcPeRof3yLi7dRpxNOn%2FB50zqnMYzNtWWX53aVDG3BE9Z28pmizbg0xYo6%2FaObbGOAb%2BnKEQl%2BvaE1J1Tgf64xk1XdJbZnkSf6VQKA9WVS30LhWGL%2FVGMKyj%2BYjirpl%2FeTYOBi2N8OCi7mVvUnMW%2FYtuFZxxCJyis2iW3YBqtjb8AE8l8v33jna9a%2BJxSPOK%2BxR3bTyMEttVfulgbrRRR3Kswcfutr%2Bqwp59ZbYlSDw6%2FNIl9u%2FPOSo%2FabCTZdCawkdQlSPV%2FcS6uy%2FFDgPRYPEirGrQ3MZKHA8hjzMzR03RRjMLUO8AFBqA5nl8LZloYvokBtG6zO8Hqr0yydcgV9f9mv9oz%2FOhGpUqrrCWZ0AE2jRXf4VB26h2bxnXuToNOd7%2FfPyTL40%2Fbic7ckRqXUJ1fkgTD4m%2Fy8BjqkAeUqGZDHWchteittM5Fp2yb8leayT8tuyM%2BDh0%2BcgPHulaHORNj%2BjmKPjxGrKAgL3N28IZBh82zx2AdqF8Cc8Lqj1e3ERx5LqhyyF0DZYWDz097M1klvogb9pY98uci0OYAb%2BLpZ%2B2h24Mo16m93Iul4jQD6q1QSp4oxv%2FbHCwqxrj%2F6SKHPu4iblCq9weNIhyIdQyhMy1lBiv%2Ba8CKicE%2Fk2G3n&X-Amz-Signature=4ae2ffb2d989e1fd9fd5af3b6cbd5fd8cc86ce8be99734f0e39566d9b59a5e84&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXPSVYFX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDO9U%2BqBjxHC13RuPvLk4gBS0WY9IEQ2JUnWK6FG9Di9AIhAPeMZE7u7uDiGnms4q0lUutoDJd8Pc%2FYxzCrC1LMW5GXKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyeqza9gm0lKnqCoU8q3AM4uRJTt5urwyzcgTvmLX4MOw53iZESlSsO1hHxS%2BqiFgeXjqgxComvWd1q%2Bpy0BMx7uWdbrvK%2BDqmcYrcbzg1buz61OgfqyQbcZTifZ4xTjpM8P%2FyfNVDp9z%2B%2BGeLh8IcD3S9ynASEqA9efKLIkPQXPpVXeNcCwgBu3WfVjA%2FcTi21BO2OEHoCfVbOcmM%2B5c5u6wgNQj%2FO8pIasSmIUXhitwGn9dTkritcPeRof3yLi7dRpxNOn%2FB50zqnMYzNtWWX53aVDG3BE9Z28pmizbg0xYo6%2FaObbGOAb%2BnKEQl%2BvaE1J1Tgf64xk1XdJbZnkSf6VQKA9WVS30LhWGL%2FVGMKyj%2BYjirpl%2FeTYOBi2N8OCi7mVvUnMW%2FYtuFZxxCJyis2iW3YBqtjb8AE8l8v33jna9a%2BJxSPOK%2BxR3bTyMEttVfulgbrRRR3Kswcfutr%2Bqwp59ZbYlSDw6%2FNIl9u%2FPOSo%2FabCTZdCawkdQlSPV%2FcS6uy%2FFDgPRYPEirGrQ3MZKHA8hjzMzR03RRjMLUO8AFBqA5nl8LZloYvokBtG6zO8Hqr0yydcgV9f9mv9oz%2FOhGpUqrrCWZ0AE2jRXf4VB26h2bxnXuToNOd7%2FfPyTL40%2Fbic7ckRqXUJ1fkgTD4m%2Fy8BjqkAeUqGZDHWchteittM5Fp2yb8leayT8tuyM%2BDh0%2BcgPHulaHORNj%2BjmKPjxGrKAgL3N28IZBh82zx2AdqF8Cc8Lqj1e3ERx5LqhyyF0DZYWDz097M1klvogb9pY98uci0OYAb%2BLpZ%2B2h24Mo16m93Iul4jQD6q1QSp4oxv%2FbHCwqxrj%2F6SKHPu4iblCq9weNIhyIdQyhMy1lBiv%2Ba8CKicE%2Fk2G3n&X-Amz-Signature=9360e73d466ccaab400524015ecab89a13b652accb6b0add914c2c570478e345&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXPSVYFX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDO9U%2BqBjxHC13RuPvLk4gBS0WY9IEQ2JUnWK6FG9Di9AIhAPeMZE7u7uDiGnms4q0lUutoDJd8Pc%2FYxzCrC1LMW5GXKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyeqza9gm0lKnqCoU8q3AM4uRJTt5urwyzcgTvmLX4MOw53iZESlSsO1hHxS%2BqiFgeXjqgxComvWd1q%2Bpy0BMx7uWdbrvK%2BDqmcYrcbzg1buz61OgfqyQbcZTifZ4xTjpM8P%2FyfNVDp9z%2B%2BGeLh8IcD3S9ynASEqA9efKLIkPQXPpVXeNcCwgBu3WfVjA%2FcTi21BO2OEHoCfVbOcmM%2B5c5u6wgNQj%2FO8pIasSmIUXhitwGn9dTkritcPeRof3yLi7dRpxNOn%2FB50zqnMYzNtWWX53aVDG3BE9Z28pmizbg0xYo6%2FaObbGOAb%2BnKEQl%2BvaE1J1Tgf64xk1XdJbZnkSf6VQKA9WVS30LhWGL%2FVGMKyj%2BYjirpl%2FeTYOBi2N8OCi7mVvUnMW%2FYtuFZxxCJyis2iW3YBqtjb8AE8l8v33jna9a%2BJxSPOK%2BxR3bTyMEttVfulgbrRRR3Kswcfutr%2Bqwp59ZbYlSDw6%2FNIl9u%2FPOSo%2FabCTZdCawkdQlSPV%2FcS6uy%2FFDgPRYPEirGrQ3MZKHA8hjzMzR03RRjMLUO8AFBqA5nl8LZloYvokBtG6zO8Hqr0yydcgV9f9mv9oz%2FOhGpUqrrCWZ0AE2jRXf4VB26h2bxnXuToNOd7%2FfPyTL40%2Fbic7ckRqXUJ1fkgTD4m%2Fy8BjqkAeUqGZDHWchteittM5Fp2yb8leayT8tuyM%2BDh0%2BcgPHulaHORNj%2BjmKPjxGrKAgL3N28IZBh82zx2AdqF8Cc8Lqj1e3ERx5LqhyyF0DZYWDz097M1klvogb9pY98uci0OYAb%2BLpZ%2B2h24Mo16m93Iul4jQD6q1QSp4oxv%2FbHCwqxrj%2F6SKHPu4iblCq9weNIhyIdQyhMy1lBiv%2Ba8CKicE%2Fk2G3n&X-Amz-Signature=4a557a3378e06b036f289438533492894b4768c64cce4a960ff39852d4af87c8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXPSVYFX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDO9U%2BqBjxHC13RuPvLk4gBS0WY9IEQ2JUnWK6FG9Di9AIhAPeMZE7u7uDiGnms4q0lUutoDJd8Pc%2FYxzCrC1LMW5GXKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyeqza9gm0lKnqCoU8q3AM4uRJTt5urwyzcgTvmLX4MOw53iZESlSsO1hHxS%2BqiFgeXjqgxComvWd1q%2Bpy0BMx7uWdbrvK%2BDqmcYrcbzg1buz61OgfqyQbcZTifZ4xTjpM8P%2FyfNVDp9z%2B%2BGeLh8IcD3S9ynASEqA9efKLIkPQXPpVXeNcCwgBu3WfVjA%2FcTi21BO2OEHoCfVbOcmM%2B5c5u6wgNQj%2FO8pIasSmIUXhitwGn9dTkritcPeRof3yLi7dRpxNOn%2FB50zqnMYzNtWWX53aVDG3BE9Z28pmizbg0xYo6%2FaObbGOAb%2BnKEQl%2BvaE1J1Tgf64xk1XdJbZnkSf6VQKA9WVS30LhWGL%2FVGMKyj%2BYjirpl%2FeTYOBi2N8OCi7mVvUnMW%2FYtuFZxxCJyis2iW3YBqtjb8AE8l8v33jna9a%2BJxSPOK%2BxR3bTyMEttVfulgbrRRR3Kswcfutr%2Bqwp59ZbYlSDw6%2FNIl9u%2FPOSo%2FabCTZdCawkdQlSPV%2FcS6uy%2FFDgPRYPEirGrQ3MZKHA8hjzMzR03RRjMLUO8AFBqA5nl8LZloYvokBtG6zO8Hqr0yydcgV9f9mv9oz%2FOhGpUqrrCWZ0AE2jRXf4VB26h2bxnXuToNOd7%2FfPyTL40%2Fbic7ckRqXUJ1fkgTD4m%2Fy8BjqkAeUqGZDHWchteittM5Fp2yb8leayT8tuyM%2BDh0%2BcgPHulaHORNj%2BjmKPjxGrKAgL3N28IZBh82zx2AdqF8Cc8Lqj1e3ERx5LqhyyF0DZYWDz097M1klvogb9pY98uci0OYAb%2BLpZ%2B2h24Mo16m93Iul4jQD6q1QSp4oxv%2FbHCwqxrj%2F6SKHPu4iblCq9weNIhyIdQyhMy1lBiv%2Ba8CKicE%2Fk2G3n&X-Amz-Signature=bc5320d83120ed3e98954f5aa61a8c748bd703fa4502ed00b5388623dbdccae2&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXPSVYFX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDO9U%2BqBjxHC13RuPvLk4gBS0WY9IEQ2JUnWK6FG9Di9AIhAPeMZE7u7uDiGnms4q0lUutoDJd8Pc%2FYxzCrC1LMW5GXKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyeqza9gm0lKnqCoU8q3AM4uRJTt5urwyzcgTvmLX4MOw53iZESlSsO1hHxS%2BqiFgeXjqgxComvWd1q%2Bpy0BMx7uWdbrvK%2BDqmcYrcbzg1buz61OgfqyQbcZTifZ4xTjpM8P%2FyfNVDp9z%2B%2BGeLh8IcD3S9ynASEqA9efKLIkPQXPpVXeNcCwgBu3WfVjA%2FcTi21BO2OEHoCfVbOcmM%2B5c5u6wgNQj%2FO8pIasSmIUXhitwGn9dTkritcPeRof3yLi7dRpxNOn%2FB50zqnMYzNtWWX53aVDG3BE9Z28pmizbg0xYo6%2FaObbGOAb%2BnKEQl%2BvaE1J1Tgf64xk1XdJbZnkSf6VQKA9WVS30LhWGL%2FVGMKyj%2BYjirpl%2FeTYOBi2N8OCi7mVvUnMW%2FYtuFZxxCJyis2iW3YBqtjb8AE8l8v33jna9a%2BJxSPOK%2BxR3bTyMEttVfulgbrRRR3Kswcfutr%2Bqwp59ZbYlSDw6%2FNIl9u%2FPOSo%2FabCTZdCawkdQlSPV%2FcS6uy%2FFDgPRYPEirGrQ3MZKHA8hjzMzR03RRjMLUO8AFBqA5nl8LZloYvokBtG6zO8Hqr0yydcgV9f9mv9oz%2FOhGpUqrrCWZ0AE2jRXf4VB26h2bxnXuToNOd7%2FfPyTL40%2Fbic7ckRqXUJ1fkgTD4m%2Fy8BjqkAeUqGZDHWchteittM5Fp2yb8leayT8tuyM%2BDh0%2BcgPHulaHORNj%2BjmKPjxGrKAgL3N28IZBh82zx2AdqF8Cc8Lqj1e3ERx5LqhyyF0DZYWDz097M1klvogb9pY98uci0OYAb%2BLpZ%2B2h24Mo16m93Iul4jQD6q1QSp4oxv%2FbHCwqxrj%2F6SKHPu4iblCq9weNIhyIdQyhMy1lBiv%2Ba8CKicE%2Fk2G3n&X-Amz-Signature=e345345bed975cfb95e6c54e0181df2c176a95b7db70d93c5d74c0f82f5cc2f9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXPSVYFX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDO9U%2BqBjxHC13RuPvLk4gBS0WY9IEQ2JUnWK6FG9Di9AIhAPeMZE7u7uDiGnms4q0lUutoDJd8Pc%2FYxzCrC1LMW5GXKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyeqza9gm0lKnqCoU8q3AM4uRJTt5urwyzcgTvmLX4MOw53iZESlSsO1hHxS%2BqiFgeXjqgxComvWd1q%2Bpy0BMx7uWdbrvK%2BDqmcYrcbzg1buz61OgfqyQbcZTifZ4xTjpM8P%2FyfNVDp9z%2B%2BGeLh8IcD3S9ynASEqA9efKLIkPQXPpVXeNcCwgBu3WfVjA%2FcTi21BO2OEHoCfVbOcmM%2B5c5u6wgNQj%2FO8pIasSmIUXhitwGn9dTkritcPeRof3yLi7dRpxNOn%2FB50zqnMYzNtWWX53aVDG3BE9Z28pmizbg0xYo6%2FaObbGOAb%2BnKEQl%2BvaE1J1Tgf64xk1XdJbZnkSf6VQKA9WVS30LhWGL%2FVGMKyj%2BYjirpl%2FeTYOBi2N8OCi7mVvUnMW%2FYtuFZxxCJyis2iW3YBqtjb8AE8l8v33jna9a%2BJxSPOK%2BxR3bTyMEttVfulgbrRRR3Kswcfutr%2Bqwp59ZbYlSDw6%2FNIl9u%2FPOSo%2FabCTZdCawkdQlSPV%2FcS6uy%2FFDgPRYPEirGrQ3MZKHA8hjzMzR03RRjMLUO8AFBqA5nl8LZloYvokBtG6zO8Hqr0yydcgV9f9mv9oz%2FOhGpUqrrCWZ0AE2jRXf4VB26h2bxnXuToNOd7%2FfPyTL40%2Fbic7ckRqXUJ1fkgTD4m%2Fy8BjqkAeUqGZDHWchteittM5Fp2yb8leayT8tuyM%2BDh0%2BcgPHulaHORNj%2BjmKPjxGrKAgL3N28IZBh82zx2AdqF8Cc8Lqj1e3ERx5LqhyyF0DZYWDz097M1klvogb9pY98uci0OYAb%2BLpZ%2B2h24Mo16m93Iul4jQD6q1QSp4oxv%2FbHCwqxrj%2F6SKHPu4iblCq9weNIhyIdQyhMy1lBiv%2Ba8CKicE%2Fk2G3n&X-Amz-Signature=c9883206603c942bcaf3da958942d2f5e321961df4fcd8f922a83ebb2e6bf988&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXPSVYFX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDO9U%2BqBjxHC13RuPvLk4gBS0WY9IEQ2JUnWK6FG9Di9AIhAPeMZE7u7uDiGnms4q0lUutoDJd8Pc%2FYxzCrC1LMW5GXKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyeqza9gm0lKnqCoU8q3AM4uRJTt5urwyzcgTvmLX4MOw53iZESlSsO1hHxS%2BqiFgeXjqgxComvWd1q%2Bpy0BMx7uWdbrvK%2BDqmcYrcbzg1buz61OgfqyQbcZTifZ4xTjpM8P%2FyfNVDp9z%2B%2BGeLh8IcD3S9ynASEqA9efKLIkPQXPpVXeNcCwgBu3WfVjA%2FcTi21BO2OEHoCfVbOcmM%2B5c5u6wgNQj%2FO8pIasSmIUXhitwGn9dTkritcPeRof3yLi7dRpxNOn%2FB50zqnMYzNtWWX53aVDG3BE9Z28pmizbg0xYo6%2FaObbGOAb%2BnKEQl%2BvaE1J1Tgf64xk1XdJbZnkSf6VQKA9WVS30LhWGL%2FVGMKyj%2BYjirpl%2FeTYOBi2N8OCi7mVvUnMW%2FYtuFZxxCJyis2iW3YBqtjb8AE8l8v33jna9a%2BJxSPOK%2BxR3bTyMEttVfulgbrRRR3Kswcfutr%2Bqwp59ZbYlSDw6%2FNIl9u%2FPOSo%2FabCTZdCawkdQlSPV%2FcS6uy%2FFDgPRYPEirGrQ3MZKHA8hjzMzR03RRjMLUO8AFBqA5nl8LZloYvokBtG6zO8Hqr0yydcgV9f9mv9oz%2FOhGpUqrrCWZ0AE2jRXf4VB26h2bxnXuToNOd7%2FfPyTL40%2Fbic7ckRqXUJ1fkgTD4m%2Fy8BjqkAeUqGZDHWchteittM5Fp2yb8leayT8tuyM%2BDh0%2BcgPHulaHORNj%2BjmKPjxGrKAgL3N28IZBh82zx2AdqF8Cc8Lqj1e3ERx5LqhyyF0DZYWDz097M1klvogb9pY98uci0OYAb%2BLpZ%2B2h24Mo16m93Iul4jQD6q1QSp4oxv%2FbHCwqxrj%2F6SKHPu4iblCq9weNIhyIdQyhMy1lBiv%2Ba8CKicE%2Fk2G3n&X-Amz-Signature=546b0b19f82a8cb2f2eaa42ae667a5636efda5b16ffc5addd465727cddf50868&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXPSVYFX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDO9U%2BqBjxHC13RuPvLk4gBS0WY9IEQ2JUnWK6FG9Di9AIhAPeMZE7u7uDiGnms4q0lUutoDJd8Pc%2FYxzCrC1LMW5GXKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyeqza9gm0lKnqCoU8q3AM4uRJTt5urwyzcgTvmLX4MOw53iZESlSsO1hHxS%2BqiFgeXjqgxComvWd1q%2Bpy0BMx7uWdbrvK%2BDqmcYrcbzg1buz61OgfqyQbcZTifZ4xTjpM8P%2FyfNVDp9z%2B%2BGeLh8IcD3S9ynASEqA9efKLIkPQXPpVXeNcCwgBu3WfVjA%2FcTi21BO2OEHoCfVbOcmM%2B5c5u6wgNQj%2FO8pIasSmIUXhitwGn9dTkritcPeRof3yLi7dRpxNOn%2FB50zqnMYzNtWWX53aVDG3BE9Z28pmizbg0xYo6%2FaObbGOAb%2BnKEQl%2BvaE1J1Tgf64xk1XdJbZnkSf6VQKA9WVS30LhWGL%2FVGMKyj%2BYjirpl%2FeTYOBi2N8OCi7mVvUnMW%2FYtuFZxxCJyis2iW3YBqtjb8AE8l8v33jna9a%2BJxSPOK%2BxR3bTyMEttVfulgbrRRR3Kswcfutr%2Bqwp59ZbYlSDw6%2FNIl9u%2FPOSo%2FabCTZdCawkdQlSPV%2FcS6uy%2FFDgPRYPEirGrQ3MZKHA8hjzMzR03RRjMLUO8AFBqA5nl8LZloYvokBtG6zO8Hqr0yydcgV9f9mv9oz%2FOhGpUqrrCWZ0AE2jRXf4VB26h2bxnXuToNOd7%2FfPyTL40%2Fbic7ckRqXUJ1fkgTD4m%2Fy8BjqkAeUqGZDHWchteittM5Fp2yb8leayT8tuyM%2BDh0%2BcgPHulaHORNj%2BjmKPjxGrKAgL3N28IZBh82zx2AdqF8Cc8Lqj1e3ERx5LqhyyF0DZYWDz097M1klvogb9pY98uci0OYAb%2BLpZ%2B2h24Mo16m93Iul4jQD6q1QSp4oxv%2FbHCwqxrj%2F6SKHPu4iblCq9weNIhyIdQyhMy1lBiv%2Ba8CKicE%2Fk2G3n&X-Amz-Signature=298529227f6af78a7f546c06219ce23182f7dcc409e403e8d7cf7ac6c8f6a42e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3KRGF77%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCja1R%2Fb%2FpP0EI%2FEunKHthgmEKpM0cRSCBAqhmxgqnhbQIhALXNERVFqFmKcEr1AkGMbFIt5nsMmNDwQSH0psCZrdsZKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHpbj%2Bt2cXbpSgGysq3AOqbKD983gEbt8CNJi%2B%2BkIdJ6T2mAjlqYAbt3sdofdvHl8SccfiA0i69VU9oPquqbDdkPsc6vFeL9lNRCXOZnPAJbqCQQeyVVA1F2H1uxJEz7hEqUa52p4wEshke%2BxtD4ssb5aA1qKV7pE9ShFzSiQjwUMiw%2Fx59hQtRz19pQo5kvzvsHb8pQloVKEO9RSfFVHknO1sQAobZ%2BMVV0yrUKcmD3%2Fap8E7DSPDR8yVo8xrkne37ycC8K6mpGDUJy%2FZyEPFUi1Hr0obVfhqcNgPPnc%2Bk%2FRgbSWh1JST1GMak2wxlRa8b5%2Fb3qabxw1OlTcJAdWh90vEmbQ1rikBR0yzkPdOTD%2BmhR6xkeyzQroyifGUuY9JwE%2BmYvbM0w8pPdi1AHBMbgirP5g8eazY6qbdH7RFaIbThaw5MpCc3%2FFoXOw0MS%2B36wpSdpynSFwRC4tmgSwklFEzauhzBKCP2Hgz%2BUwkTJmwPDrhahwGaOlga1UVsxdvG4r9b4tZKd5yyCyONuYjhJCuqG9fZhOiQY9g1zSxchZhvxSFWlBAJmEJ6dt%2BMIQi%2FHYD8vC%2FNFv6oE0D7nOieaVz%2B0qqYg%2BsnClp7RxkbMrNys3H0QLtDq7WKR93xLg8bchXwAoKB7XlrjCknPy8BjqkAemDrwkbyND9ZrGV9%2FatZn0Ey6V%2BMBbqrog3XUVvN29PwNIfeE6JohWhYY5wjfxbP%2FP%2FUGAUTLU63N9X%2F47hWpsBRBKz4GC4jukBaH9O8mzj%2Fs%2FRi%2FMh5beQ6oWLylzT1vSVs%2FxNTh2Hyj04v9h0Xb1NofGdRZjbJngeRHgPy4wvMoWkIVnRz7Ed6sWkKfD2OwIi7rjVI87Cg2GNx3VPR%2FJ6maW%2B&X-Amz-Signature=60f5b1be2d4c22d12146ae7a82487b95b1dda904b1e6d5db598460033b7abd27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3KRGF77%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCja1R%2Fb%2FpP0EI%2FEunKHthgmEKpM0cRSCBAqhmxgqnhbQIhALXNERVFqFmKcEr1AkGMbFIt5nsMmNDwQSH0psCZrdsZKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHpbj%2Bt2cXbpSgGysq3AOqbKD983gEbt8CNJi%2B%2BkIdJ6T2mAjlqYAbt3sdofdvHl8SccfiA0i69VU9oPquqbDdkPsc6vFeL9lNRCXOZnPAJbqCQQeyVVA1F2H1uxJEz7hEqUa52p4wEshke%2BxtD4ssb5aA1qKV7pE9ShFzSiQjwUMiw%2Fx59hQtRz19pQo5kvzvsHb8pQloVKEO9RSfFVHknO1sQAobZ%2BMVV0yrUKcmD3%2Fap8E7DSPDR8yVo8xrkne37ycC8K6mpGDUJy%2FZyEPFUi1Hr0obVfhqcNgPPnc%2Bk%2FRgbSWh1JST1GMak2wxlRa8b5%2Fb3qabxw1OlTcJAdWh90vEmbQ1rikBR0yzkPdOTD%2BmhR6xkeyzQroyifGUuY9JwE%2BmYvbM0w8pPdi1AHBMbgirP5g8eazY6qbdH7RFaIbThaw5MpCc3%2FFoXOw0MS%2B36wpSdpynSFwRC4tmgSwklFEzauhzBKCP2Hgz%2BUwkTJmwPDrhahwGaOlga1UVsxdvG4r9b4tZKd5yyCyONuYjhJCuqG9fZhOiQY9g1zSxchZhvxSFWlBAJmEJ6dt%2BMIQi%2FHYD8vC%2FNFv6oE0D7nOieaVz%2B0qqYg%2BsnClp7RxkbMrNys3H0QLtDq7WKR93xLg8bchXwAoKB7XlrjCknPy8BjqkAemDrwkbyND9ZrGV9%2FatZn0Ey6V%2BMBbqrog3XUVvN29PwNIfeE6JohWhYY5wjfxbP%2FP%2FUGAUTLU63N9X%2F47hWpsBRBKz4GC4jukBaH9O8mzj%2Fs%2FRi%2FMh5beQ6oWLylzT1vSVs%2FxNTh2Hyj04v9h0Xb1NofGdRZjbJngeRHgPy4wvMoWkIVnRz7Ed6sWkKfD2OwIi7rjVI87Cg2GNx3VPR%2FJ6maW%2B&X-Amz-Signature=e2ef3421c3230e1582a6b0b633f82a76eef4a64438d32132b14495d36314f546&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
