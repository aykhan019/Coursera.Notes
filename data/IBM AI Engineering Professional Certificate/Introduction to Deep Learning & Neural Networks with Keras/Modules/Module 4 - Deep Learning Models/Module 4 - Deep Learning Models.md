

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVYGRTXC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICz1NpapgtjJp1iQuY%2BHZwO4xtrHemJE4rGp1iMJbLaLAiAlKdnLxcnfv9azG9Q%2FUtqGfMGu4bjp45N9l%2FSy1MsMKir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMUghPa24M5G9arpRJKtwDMViKcoPWhmbUQ7LGl9rJWU5xDjgPphJydO2PA4A2Q%2BVCYyR7ws8SVeEbIuOhw2yLrnMnX9CsHm6knOApNm1Powv8fszJPnDy1Tv42giWB0ffpAH2a7jTv1B6jbdR7FayzjNzoQA3ST135%2FidcUaLsBH%2FoGaba%2BeTShFtLU05Au%2F7EAN6mCmOADDtmPgLcj4lm6bid0XaVitNNSWeEbWtuApfhI26NSL%2BrYJtVZIhp0dSybRHEw2VB7u4lOAVwHls3R6rOz4gfX6v9xtIMpBMyxJZCwUCIaiKs%2BE%2BbY29%2F296PS7J86AM%2F08VsNN8Xt0FFtTt2Glm%2B85dWzt0iccY2moOL3iqwNUB3%2BysflKfo4zzuOqKyqGVZNIFbN2HrffC1l1FcximhHhImwK8weLeBBBu3hi8n9M%2BJge1VQoj%2F5wV%2BIK1dnYwqScY8w0%2F9MHtp4AsXQSlkxnVQzDSF3ajRTq0o8W21Eis6g7xTlpeZhQd5%2FDw65OWKq2HGMLSeALCxtweD9BeRyfz7Kj74gixGS2X1jQal6y9Z7jwOmKbx47ruGItQDXzx5KTtJK7l89VCqgFm8bt%2FZ4F7Q70HiC7RS8nojn2%2FblQ6s0gUc3%2BLdyOvCMbDMdsIuCxepYw7b6GvQY6pgFQkfh59hpRMNTihiwBtHApa%2BxS0ccn3nfpijRH4C1Pu%2FSCDcRZNjQb6OD%2B2%2Bu%2F9%2Bv0vq7JjKl5NjEWAw3EN9gKVPXUl4evlttWMmQl0hu3Ho6ur7vT822NhficL65buJaNB7lYYILZCa3okcE1WNZtDgZaUkxYLblnDZjuLQxvtTM8pJA%2BfOz24mSBLgcIRGmUDyjj6XlU3zEYbLEaExyskFsgIoV%2B&X-Amz-Signature=263181961e27db348f525c0db7617a59655fdb3c1ac88f3a4cbb83257d55dcb6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVYGRTXC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICz1NpapgtjJp1iQuY%2BHZwO4xtrHemJE4rGp1iMJbLaLAiAlKdnLxcnfv9azG9Q%2FUtqGfMGu4bjp45N9l%2FSy1MsMKir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMUghPa24M5G9arpRJKtwDMViKcoPWhmbUQ7LGl9rJWU5xDjgPphJydO2PA4A2Q%2BVCYyR7ws8SVeEbIuOhw2yLrnMnX9CsHm6knOApNm1Powv8fszJPnDy1Tv42giWB0ffpAH2a7jTv1B6jbdR7FayzjNzoQA3ST135%2FidcUaLsBH%2FoGaba%2BeTShFtLU05Au%2F7EAN6mCmOADDtmPgLcj4lm6bid0XaVitNNSWeEbWtuApfhI26NSL%2BrYJtVZIhp0dSybRHEw2VB7u4lOAVwHls3R6rOz4gfX6v9xtIMpBMyxJZCwUCIaiKs%2BE%2BbY29%2F296PS7J86AM%2F08VsNN8Xt0FFtTt2Glm%2B85dWzt0iccY2moOL3iqwNUB3%2BysflKfo4zzuOqKyqGVZNIFbN2HrffC1l1FcximhHhImwK8weLeBBBu3hi8n9M%2BJge1VQoj%2F5wV%2BIK1dnYwqScY8w0%2F9MHtp4AsXQSlkxnVQzDSF3ajRTq0o8W21Eis6g7xTlpeZhQd5%2FDw65OWKq2HGMLSeALCxtweD9BeRyfz7Kj74gixGS2X1jQal6y9Z7jwOmKbx47ruGItQDXzx5KTtJK7l89VCqgFm8bt%2FZ4F7Q70HiC7RS8nojn2%2FblQ6s0gUc3%2BLdyOvCMbDMdsIuCxepYw7b6GvQY6pgFQkfh59hpRMNTihiwBtHApa%2BxS0ccn3nfpijRH4C1Pu%2FSCDcRZNjQb6OD%2B2%2Bu%2F9%2Bv0vq7JjKl5NjEWAw3EN9gKVPXUl4evlttWMmQl0hu3Ho6ur7vT822NhficL65buJaNB7lYYILZCa3okcE1WNZtDgZaUkxYLblnDZjuLQxvtTM8pJA%2BfOz24mSBLgcIRGmUDyjj6XlU3zEYbLEaExyskFsgIoV%2B&X-Amz-Signature=15eef0344c7e171f89f6d961d563d7dc420f9b657d9d71056eb672b867163c3a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVYGRTXC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICz1NpapgtjJp1iQuY%2BHZwO4xtrHemJE4rGp1iMJbLaLAiAlKdnLxcnfv9azG9Q%2FUtqGfMGu4bjp45N9l%2FSy1MsMKir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMUghPa24M5G9arpRJKtwDMViKcoPWhmbUQ7LGl9rJWU5xDjgPphJydO2PA4A2Q%2BVCYyR7ws8SVeEbIuOhw2yLrnMnX9CsHm6knOApNm1Powv8fszJPnDy1Tv42giWB0ffpAH2a7jTv1B6jbdR7FayzjNzoQA3ST135%2FidcUaLsBH%2FoGaba%2BeTShFtLU05Au%2F7EAN6mCmOADDtmPgLcj4lm6bid0XaVitNNSWeEbWtuApfhI26NSL%2BrYJtVZIhp0dSybRHEw2VB7u4lOAVwHls3R6rOz4gfX6v9xtIMpBMyxJZCwUCIaiKs%2BE%2BbY29%2F296PS7J86AM%2F08VsNN8Xt0FFtTt2Glm%2B85dWzt0iccY2moOL3iqwNUB3%2BysflKfo4zzuOqKyqGVZNIFbN2HrffC1l1FcximhHhImwK8weLeBBBu3hi8n9M%2BJge1VQoj%2F5wV%2BIK1dnYwqScY8w0%2F9MHtp4AsXQSlkxnVQzDSF3ajRTq0o8W21Eis6g7xTlpeZhQd5%2FDw65OWKq2HGMLSeALCxtweD9BeRyfz7Kj74gixGS2X1jQal6y9Z7jwOmKbx47ruGItQDXzx5KTtJK7l89VCqgFm8bt%2FZ4F7Q70HiC7RS8nojn2%2FblQ6s0gUc3%2BLdyOvCMbDMdsIuCxepYw7b6GvQY6pgFQkfh59hpRMNTihiwBtHApa%2BxS0ccn3nfpijRH4C1Pu%2FSCDcRZNjQb6OD%2B2%2Bu%2F9%2Bv0vq7JjKl5NjEWAw3EN9gKVPXUl4evlttWMmQl0hu3Ho6ur7vT822NhficL65buJaNB7lYYILZCa3okcE1WNZtDgZaUkxYLblnDZjuLQxvtTM8pJA%2BfOz24mSBLgcIRGmUDyjj6XlU3zEYbLEaExyskFsgIoV%2B&X-Amz-Signature=bb4a7bfb204a8670e33a4365a0ce14b498de3884b58b63731d6c3cd85e23e4a1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVYGRTXC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICz1NpapgtjJp1iQuY%2BHZwO4xtrHemJE4rGp1iMJbLaLAiAlKdnLxcnfv9azG9Q%2FUtqGfMGu4bjp45N9l%2FSy1MsMKir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMUghPa24M5G9arpRJKtwDMViKcoPWhmbUQ7LGl9rJWU5xDjgPphJydO2PA4A2Q%2BVCYyR7ws8SVeEbIuOhw2yLrnMnX9CsHm6knOApNm1Powv8fszJPnDy1Tv42giWB0ffpAH2a7jTv1B6jbdR7FayzjNzoQA3ST135%2FidcUaLsBH%2FoGaba%2BeTShFtLU05Au%2F7EAN6mCmOADDtmPgLcj4lm6bid0XaVitNNSWeEbWtuApfhI26NSL%2BrYJtVZIhp0dSybRHEw2VB7u4lOAVwHls3R6rOz4gfX6v9xtIMpBMyxJZCwUCIaiKs%2BE%2BbY29%2F296PS7J86AM%2F08VsNN8Xt0FFtTt2Glm%2B85dWzt0iccY2moOL3iqwNUB3%2BysflKfo4zzuOqKyqGVZNIFbN2HrffC1l1FcximhHhImwK8weLeBBBu3hi8n9M%2BJge1VQoj%2F5wV%2BIK1dnYwqScY8w0%2F9MHtp4AsXQSlkxnVQzDSF3ajRTq0o8W21Eis6g7xTlpeZhQd5%2FDw65OWKq2HGMLSeALCxtweD9BeRyfz7Kj74gixGS2X1jQal6y9Z7jwOmKbx47ruGItQDXzx5KTtJK7l89VCqgFm8bt%2FZ4F7Q70HiC7RS8nojn2%2FblQ6s0gUc3%2BLdyOvCMbDMdsIuCxepYw7b6GvQY6pgFQkfh59hpRMNTihiwBtHApa%2BxS0ccn3nfpijRH4C1Pu%2FSCDcRZNjQb6OD%2B2%2Bu%2F9%2Bv0vq7JjKl5NjEWAw3EN9gKVPXUl4evlttWMmQl0hu3Ho6ur7vT822NhficL65buJaNB7lYYILZCa3okcE1WNZtDgZaUkxYLblnDZjuLQxvtTM8pJA%2BfOz24mSBLgcIRGmUDyjj6XlU3zEYbLEaExyskFsgIoV%2B&X-Amz-Signature=9998d423a9c9f00dbb4927855c84d13d80271c4b4d0532b20efac1ab0cdfef6f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVYGRTXC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICz1NpapgtjJp1iQuY%2BHZwO4xtrHemJE4rGp1iMJbLaLAiAlKdnLxcnfv9azG9Q%2FUtqGfMGu4bjp45N9l%2FSy1MsMKir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMUghPa24M5G9arpRJKtwDMViKcoPWhmbUQ7LGl9rJWU5xDjgPphJydO2PA4A2Q%2BVCYyR7ws8SVeEbIuOhw2yLrnMnX9CsHm6knOApNm1Powv8fszJPnDy1Tv42giWB0ffpAH2a7jTv1B6jbdR7FayzjNzoQA3ST135%2FidcUaLsBH%2FoGaba%2BeTShFtLU05Au%2F7EAN6mCmOADDtmPgLcj4lm6bid0XaVitNNSWeEbWtuApfhI26NSL%2BrYJtVZIhp0dSybRHEw2VB7u4lOAVwHls3R6rOz4gfX6v9xtIMpBMyxJZCwUCIaiKs%2BE%2BbY29%2F296PS7J86AM%2F08VsNN8Xt0FFtTt2Glm%2B85dWzt0iccY2moOL3iqwNUB3%2BysflKfo4zzuOqKyqGVZNIFbN2HrffC1l1FcximhHhImwK8weLeBBBu3hi8n9M%2BJge1VQoj%2F5wV%2BIK1dnYwqScY8w0%2F9MHtp4AsXQSlkxnVQzDSF3ajRTq0o8W21Eis6g7xTlpeZhQd5%2FDw65OWKq2HGMLSeALCxtweD9BeRyfz7Kj74gixGS2X1jQal6y9Z7jwOmKbx47ruGItQDXzx5KTtJK7l89VCqgFm8bt%2FZ4F7Q70HiC7RS8nojn2%2FblQ6s0gUc3%2BLdyOvCMbDMdsIuCxepYw7b6GvQY6pgFQkfh59hpRMNTihiwBtHApa%2BxS0ccn3nfpijRH4C1Pu%2FSCDcRZNjQb6OD%2B2%2Bu%2F9%2Bv0vq7JjKl5NjEWAw3EN9gKVPXUl4evlttWMmQl0hu3Ho6ur7vT822NhficL65buJaNB7lYYILZCa3okcE1WNZtDgZaUkxYLblnDZjuLQxvtTM8pJA%2BfOz24mSBLgcIRGmUDyjj6XlU3zEYbLEaExyskFsgIoV%2B&X-Amz-Signature=3ccd62c862fc138f480820f10ea14c9542a3fbd92f6ea23ec9e79c8ab54c1ae4&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVYGRTXC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICz1NpapgtjJp1iQuY%2BHZwO4xtrHemJE4rGp1iMJbLaLAiAlKdnLxcnfv9azG9Q%2FUtqGfMGu4bjp45N9l%2FSy1MsMKir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMUghPa24M5G9arpRJKtwDMViKcoPWhmbUQ7LGl9rJWU5xDjgPphJydO2PA4A2Q%2BVCYyR7ws8SVeEbIuOhw2yLrnMnX9CsHm6knOApNm1Powv8fszJPnDy1Tv42giWB0ffpAH2a7jTv1B6jbdR7FayzjNzoQA3ST135%2FidcUaLsBH%2FoGaba%2BeTShFtLU05Au%2F7EAN6mCmOADDtmPgLcj4lm6bid0XaVitNNSWeEbWtuApfhI26NSL%2BrYJtVZIhp0dSybRHEw2VB7u4lOAVwHls3R6rOz4gfX6v9xtIMpBMyxJZCwUCIaiKs%2BE%2BbY29%2F296PS7J86AM%2F08VsNN8Xt0FFtTt2Glm%2B85dWzt0iccY2moOL3iqwNUB3%2BysflKfo4zzuOqKyqGVZNIFbN2HrffC1l1FcximhHhImwK8weLeBBBu3hi8n9M%2BJge1VQoj%2F5wV%2BIK1dnYwqScY8w0%2F9MHtp4AsXQSlkxnVQzDSF3ajRTq0o8W21Eis6g7xTlpeZhQd5%2FDw65OWKq2HGMLSeALCxtweD9BeRyfz7Kj74gixGS2X1jQal6y9Z7jwOmKbx47ruGItQDXzx5KTtJK7l89VCqgFm8bt%2FZ4F7Q70HiC7RS8nojn2%2FblQ6s0gUc3%2BLdyOvCMbDMdsIuCxepYw7b6GvQY6pgFQkfh59hpRMNTihiwBtHApa%2BxS0ccn3nfpijRH4C1Pu%2FSCDcRZNjQb6OD%2B2%2Bu%2F9%2Bv0vq7JjKl5NjEWAw3EN9gKVPXUl4evlttWMmQl0hu3Ho6ur7vT822NhficL65buJaNB7lYYILZCa3okcE1WNZtDgZaUkxYLblnDZjuLQxvtTM8pJA%2BfOz24mSBLgcIRGmUDyjj6XlU3zEYbLEaExyskFsgIoV%2B&X-Amz-Signature=05e69a5a2bc9cfa1c70dad9085a5ed6e4283b1454e7a32caaa165bfb2aa44ccd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVYGRTXC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICz1NpapgtjJp1iQuY%2BHZwO4xtrHemJE4rGp1iMJbLaLAiAlKdnLxcnfv9azG9Q%2FUtqGfMGu4bjp45N9l%2FSy1MsMKir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMUghPa24M5G9arpRJKtwDMViKcoPWhmbUQ7LGl9rJWU5xDjgPphJydO2PA4A2Q%2BVCYyR7ws8SVeEbIuOhw2yLrnMnX9CsHm6knOApNm1Powv8fszJPnDy1Tv42giWB0ffpAH2a7jTv1B6jbdR7FayzjNzoQA3ST135%2FidcUaLsBH%2FoGaba%2BeTShFtLU05Au%2F7EAN6mCmOADDtmPgLcj4lm6bid0XaVitNNSWeEbWtuApfhI26NSL%2BrYJtVZIhp0dSybRHEw2VB7u4lOAVwHls3R6rOz4gfX6v9xtIMpBMyxJZCwUCIaiKs%2BE%2BbY29%2F296PS7J86AM%2F08VsNN8Xt0FFtTt2Glm%2B85dWzt0iccY2moOL3iqwNUB3%2BysflKfo4zzuOqKyqGVZNIFbN2HrffC1l1FcximhHhImwK8weLeBBBu3hi8n9M%2BJge1VQoj%2F5wV%2BIK1dnYwqScY8w0%2F9MHtp4AsXQSlkxnVQzDSF3ajRTq0o8W21Eis6g7xTlpeZhQd5%2FDw65OWKq2HGMLSeALCxtweD9BeRyfz7Kj74gixGS2X1jQal6y9Z7jwOmKbx47ruGItQDXzx5KTtJK7l89VCqgFm8bt%2FZ4F7Q70HiC7RS8nojn2%2FblQ6s0gUc3%2BLdyOvCMbDMdsIuCxepYw7b6GvQY6pgFQkfh59hpRMNTihiwBtHApa%2BxS0ccn3nfpijRH4C1Pu%2FSCDcRZNjQb6OD%2B2%2Bu%2F9%2Bv0vq7JjKl5NjEWAw3EN9gKVPXUl4evlttWMmQl0hu3Ho6ur7vT822NhficL65buJaNB7lYYILZCa3okcE1WNZtDgZaUkxYLblnDZjuLQxvtTM8pJA%2BfOz24mSBLgcIRGmUDyjj6XlU3zEYbLEaExyskFsgIoV%2B&X-Amz-Signature=cd5cf2e0c36e406c3d3a92a2d88ebc01e102d648e65aecd0a5d9132ba73c5c20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVYGRTXC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICz1NpapgtjJp1iQuY%2BHZwO4xtrHemJE4rGp1iMJbLaLAiAlKdnLxcnfv9azG9Q%2FUtqGfMGu4bjp45N9l%2FSy1MsMKir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMUghPa24M5G9arpRJKtwDMViKcoPWhmbUQ7LGl9rJWU5xDjgPphJydO2PA4A2Q%2BVCYyR7ws8SVeEbIuOhw2yLrnMnX9CsHm6knOApNm1Powv8fszJPnDy1Tv42giWB0ffpAH2a7jTv1B6jbdR7FayzjNzoQA3ST135%2FidcUaLsBH%2FoGaba%2BeTShFtLU05Au%2F7EAN6mCmOADDtmPgLcj4lm6bid0XaVitNNSWeEbWtuApfhI26NSL%2BrYJtVZIhp0dSybRHEw2VB7u4lOAVwHls3R6rOz4gfX6v9xtIMpBMyxJZCwUCIaiKs%2BE%2BbY29%2F296PS7J86AM%2F08VsNN8Xt0FFtTt2Glm%2B85dWzt0iccY2moOL3iqwNUB3%2BysflKfo4zzuOqKyqGVZNIFbN2HrffC1l1FcximhHhImwK8weLeBBBu3hi8n9M%2BJge1VQoj%2F5wV%2BIK1dnYwqScY8w0%2F9MHtp4AsXQSlkxnVQzDSF3ajRTq0o8W21Eis6g7xTlpeZhQd5%2FDw65OWKq2HGMLSeALCxtweD9BeRyfz7Kj74gixGS2X1jQal6y9Z7jwOmKbx47ruGItQDXzx5KTtJK7l89VCqgFm8bt%2FZ4F7Q70HiC7RS8nojn2%2FblQ6s0gUc3%2BLdyOvCMbDMdsIuCxepYw7b6GvQY6pgFQkfh59hpRMNTihiwBtHApa%2BxS0ccn3nfpijRH4C1Pu%2FSCDcRZNjQb6OD%2B2%2Bu%2F9%2Bv0vq7JjKl5NjEWAw3EN9gKVPXUl4evlttWMmQl0hu3Ho6ur7vT822NhficL65buJaNB7lYYILZCa3okcE1WNZtDgZaUkxYLblnDZjuLQxvtTM8pJA%2BfOz24mSBLgcIRGmUDyjj6XlU3zEYbLEaExyskFsgIoV%2B&X-Amz-Signature=c98e5dbb143e7fcf9ed039f7649e617c940156a3e8ef391565a5b1b105d105d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVYGRTXC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICz1NpapgtjJp1iQuY%2BHZwO4xtrHemJE4rGp1iMJbLaLAiAlKdnLxcnfv9azG9Q%2FUtqGfMGu4bjp45N9l%2FSy1MsMKir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMUghPa24M5G9arpRJKtwDMViKcoPWhmbUQ7LGl9rJWU5xDjgPphJydO2PA4A2Q%2BVCYyR7ws8SVeEbIuOhw2yLrnMnX9CsHm6knOApNm1Powv8fszJPnDy1Tv42giWB0ffpAH2a7jTv1B6jbdR7FayzjNzoQA3ST135%2FidcUaLsBH%2FoGaba%2BeTShFtLU05Au%2F7EAN6mCmOADDtmPgLcj4lm6bid0XaVitNNSWeEbWtuApfhI26NSL%2BrYJtVZIhp0dSybRHEw2VB7u4lOAVwHls3R6rOz4gfX6v9xtIMpBMyxJZCwUCIaiKs%2BE%2BbY29%2F296PS7J86AM%2F08VsNN8Xt0FFtTt2Glm%2B85dWzt0iccY2moOL3iqwNUB3%2BysflKfo4zzuOqKyqGVZNIFbN2HrffC1l1FcximhHhImwK8weLeBBBu3hi8n9M%2BJge1VQoj%2F5wV%2BIK1dnYwqScY8w0%2F9MHtp4AsXQSlkxnVQzDSF3ajRTq0o8W21Eis6g7xTlpeZhQd5%2FDw65OWKq2HGMLSeALCxtweD9BeRyfz7Kj74gixGS2X1jQal6y9Z7jwOmKbx47ruGItQDXzx5KTtJK7l89VCqgFm8bt%2FZ4F7Q70HiC7RS8nojn2%2FblQ6s0gUc3%2BLdyOvCMbDMdsIuCxepYw7b6GvQY6pgFQkfh59hpRMNTihiwBtHApa%2BxS0ccn3nfpijRH4C1Pu%2FSCDcRZNjQb6OD%2B2%2Bu%2F9%2Bv0vq7JjKl5NjEWAw3EN9gKVPXUl4evlttWMmQl0hu3Ho6ur7vT822NhficL65buJaNB7lYYILZCa3okcE1WNZtDgZaUkxYLblnDZjuLQxvtTM8pJA%2BfOz24mSBLgcIRGmUDyjj6XlU3zEYbLEaExyskFsgIoV%2B&X-Amz-Signature=3619402c894f971997daf19c4554dcebadf29b64db4f1b85b868d37b5b2a5939&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YGNGP54%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDaGqX5QzxrY6eMA2hKw0g2bNKfWZu%2FuG1L%2B5KX25e5sgIhAOY55kPhaHWSu6XDSTZb5jHlpLiHouM8EZlGTDFNW5Y4Kv8DCCYQABoMNjM3NDIzMTgzODA1Igxoz7p0x%2BTyt4xN3lUq3AMqaQC4sSzzf4bh6%2BbiDgYksaeamnlZd0Uei2WuN4ahktFRymsBbv0iN4EPJUMw6KUxpbmLH%2FpTPA5wQE1OSTTJTvJeD0YzG15vvRArOgHWEbceirLZfOrBKY03BEV3b1c3RRwa2j9P1UbFUIsp%2BxxBw9aGJWlZWGb6OG8wYup9semXh8JMhYhL9OAyhT1pDXbqoMXGZgsOjRBoXQa1X27TSWTh1u%2FgM3n79%2F9P3orrAZbPkFjH%2BuYDb829%2B6wuiaFlY7JlRhAicdZF3wGPHUBiajag0iXpyLWaw26steO9uUuDOnQN2MluJgsXbghUYRm6I3zYLv9htHNkRSgM6%2BrNVDiZuhuoaMLPWL7gIvarVHNS8oan0TJykjFxTLqnPgfEiIc5mzQ0vdfDb7Ky9bwqKRcTjzDyH1V3Y6cEjzfjy3RrGJ%2FmvzlvYUo60eARrb%2FT1JnRo5Yh7r2V1fVbF3Q5rpch6%2Frvsvtxjur7h1iVHvWFEz1YmrHpvWk7KXgi9xtWb%2BMCXtIbl4ctsIdIAAB%2F9k1oHHJihJe%2FfqhlIzY3sK5pChYFSPV8wftkE7Y7ntkZ8WSHK6KanUyEOXToZ%2BGwiL%2BXu50wdd4IBb5QIcpHx6ImHd%2FQOam8arQuyjDmvoa9BjqkAd3%2FT%2BXghvasjmfuaCt22QhK5I0dJ9OiZ06AUXLOnw%2F8rahBbuAzq9dhbiQ941ocGz014ZpwE%2BMr5d95vpEAEMql7hVqRBJanmjIXTwiqSxNd9KzRzz5Pevz7XejSmKnLvyxetL0%2B1UXiNuY6ze2uYLcDpMPIz7jit4b9B47vJigQ95jsjrE22fwVn0CpMyFAlHvKonHDMOj0aqM3znIkVEyBIUA&X-Amz-Signature=043cc6503016861aca130b614e3123fdcddac6dd3dd57fd3f638bb10f0db782e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YGNGP54%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDaGqX5QzxrY6eMA2hKw0g2bNKfWZu%2FuG1L%2B5KX25e5sgIhAOY55kPhaHWSu6XDSTZb5jHlpLiHouM8EZlGTDFNW5Y4Kv8DCCYQABoMNjM3NDIzMTgzODA1Igxoz7p0x%2BTyt4xN3lUq3AMqaQC4sSzzf4bh6%2BbiDgYksaeamnlZd0Uei2WuN4ahktFRymsBbv0iN4EPJUMw6KUxpbmLH%2FpTPA5wQE1OSTTJTvJeD0YzG15vvRArOgHWEbceirLZfOrBKY03BEV3b1c3RRwa2j9P1UbFUIsp%2BxxBw9aGJWlZWGb6OG8wYup9semXh8JMhYhL9OAyhT1pDXbqoMXGZgsOjRBoXQa1X27TSWTh1u%2FgM3n79%2F9P3orrAZbPkFjH%2BuYDb829%2B6wuiaFlY7JlRhAicdZF3wGPHUBiajag0iXpyLWaw26steO9uUuDOnQN2MluJgsXbghUYRm6I3zYLv9htHNkRSgM6%2BrNVDiZuhuoaMLPWL7gIvarVHNS8oan0TJykjFxTLqnPgfEiIc5mzQ0vdfDb7Ky9bwqKRcTjzDyH1V3Y6cEjzfjy3RrGJ%2FmvzlvYUo60eARrb%2FT1JnRo5Yh7r2V1fVbF3Q5rpch6%2Frvsvtxjur7h1iVHvWFEz1YmrHpvWk7KXgi9xtWb%2BMCXtIbl4ctsIdIAAB%2F9k1oHHJihJe%2FfqhlIzY3sK5pChYFSPV8wftkE7Y7ntkZ8WSHK6KanUyEOXToZ%2BGwiL%2BXu50wdd4IBb5QIcpHx6ImHd%2FQOam8arQuyjDmvoa9BjqkAd3%2FT%2BXghvasjmfuaCt22QhK5I0dJ9OiZ06AUXLOnw%2F8rahBbuAzq9dhbiQ941ocGz014ZpwE%2BMr5d95vpEAEMql7hVqRBJanmjIXTwiqSxNd9KzRzz5Pevz7XejSmKnLvyxetL0%2B1UXiNuY6ze2uYLcDpMPIz7jit4b9B47vJigQ95jsjrE22fwVn0CpMyFAlHvKonHDMOj0aqM3znIkVEyBIUA&X-Amz-Signature=9cda3fb91c7710574e4e7ef91c79d7fc613df761acd69ef1d2dd611fd7448618&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
