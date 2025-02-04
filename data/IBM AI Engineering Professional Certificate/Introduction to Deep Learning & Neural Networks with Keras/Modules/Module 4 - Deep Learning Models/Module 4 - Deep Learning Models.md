

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVMR7Q4I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIHHNtJZiXq65keVCq%2FAGA65iLjpHNmOXVn0bGC8DalSeAiEA1NgxtVu6vwAsdVe9JRgA5UUkKzGfR%2FNv8umat9dc01Eq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDKseRt3PIbmCUiQ9KyrcA3Dp9K%2FbAREJRxXyfqFCZikapab%2FI9KgBFI3gcg2Yh%2BWE88hzL2BoTHgq0jiUp%2FdhkAZzO1fNlJYoR2T2wgxQeX8MDxBgcJsV%2BhLQRJrD6hM3P7xeSrzoC9m2p%2Fyt2Dm42fRKNSWuxyAnTvKoMgdhfU50B2cgYU7tssnw%2BrX9WThZ7XSllNm7Rf1IzuC%2Fheuzm29%2FXelhVWZPqDO%2FGrbUAzuAGWT8GffvU2nR4IOZYwN4nS5I4SR5E%2BShDl2nYHqfaWu3afq4v5g%2Bx6C%2FE2UBLAcnMxnPScLz%2BkILMkYuRK%2FnOt9R%2BDzp3bxtoQJgX8JiReK0eYcJ00COGzO5l6baealDagDnNENfctL2zpPLs30ImtkG0epHJaXcvz%2Brd2039stgKK6aabaM6TNXqxJ49Aq3jQUp8TK8ogJL2sT9CyOqZjEZGA5yv%2BnPaIq7nob86bQqMXBQz4Pe2iOy919lbl8jVnynEIJgpowSNIBLHzwrSjqsH9ZYHWdCvEoGH0IenQf7xEWLwLG4pz7ZCKSON4NJ11OmOycI4eWr8DER%2BgHFvywJczqvtuGhDtMZKAHymZzkllsiS2MHmB3iClnA3Zftq9xAS1sRBpXGtuvA6MURwOdhUToH5A4f2fmMN28iL0GOqUBhjYS8oljEjCbqe7XLVTNMakjrNmJmmx3oNWIuR0jR%2FtV0ZcHKWuUJwG1HoeMqCA1WwPqBCZTak0PHfPBCiG0Ap61zdb7c1ClArrK%2BTaNG6Oy1wWnJXd57XXQSpR3k5uA1lg0BjgapYunPGLe7i78rbkoZw82RPnh53i4ECLc3EMTiudmEVhT4MkYj7uP4%2BoHhpaJHqH1TwVq4SCxLdGuGjhFzyJl&X-Amz-Signature=85ef54b3908e77f290b4ccb729b1eac9e734de53ffb1e1407917558e97b208b0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVMR7Q4I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIHHNtJZiXq65keVCq%2FAGA65iLjpHNmOXVn0bGC8DalSeAiEA1NgxtVu6vwAsdVe9JRgA5UUkKzGfR%2FNv8umat9dc01Eq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDKseRt3PIbmCUiQ9KyrcA3Dp9K%2FbAREJRxXyfqFCZikapab%2FI9KgBFI3gcg2Yh%2BWE88hzL2BoTHgq0jiUp%2FdhkAZzO1fNlJYoR2T2wgxQeX8MDxBgcJsV%2BhLQRJrD6hM3P7xeSrzoC9m2p%2Fyt2Dm42fRKNSWuxyAnTvKoMgdhfU50B2cgYU7tssnw%2BrX9WThZ7XSllNm7Rf1IzuC%2Fheuzm29%2FXelhVWZPqDO%2FGrbUAzuAGWT8GffvU2nR4IOZYwN4nS5I4SR5E%2BShDl2nYHqfaWu3afq4v5g%2Bx6C%2FE2UBLAcnMxnPScLz%2BkILMkYuRK%2FnOt9R%2BDzp3bxtoQJgX8JiReK0eYcJ00COGzO5l6baealDagDnNENfctL2zpPLs30ImtkG0epHJaXcvz%2Brd2039stgKK6aabaM6TNXqxJ49Aq3jQUp8TK8ogJL2sT9CyOqZjEZGA5yv%2BnPaIq7nob86bQqMXBQz4Pe2iOy919lbl8jVnynEIJgpowSNIBLHzwrSjqsH9ZYHWdCvEoGH0IenQf7xEWLwLG4pz7ZCKSON4NJ11OmOycI4eWr8DER%2BgHFvywJczqvtuGhDtMZKAHymZzkllsiS2MHmB3iClnA3Zftq9xAS1sRBpXGtuvA6MURwOdhUToH5A4f2fmMN28iL0GOqUBhjYS8oljEjCbqe7XLVTNMakjrNmJmmx3oNWIuR0jR%2FtV0ZcHKWuUJwG1HoeMqCA1WwPqBCZTak0PHfPBCiG0Ap61zdb7c1ClArrK%2BTaNG6Oy1wWnJXd57XXQSpR3k5uA1lg0BjgapYunPGLe7i78rbkoZw82RPnh53i4ECLc3EMTiudmEVhT4MkYj7uP4%2BoHhpaJHqH1TwVq4SCxLdGuGjhFzyJl&X-Amz-Signature=18369445dbe520b1ca784ea4eb4695db5726f77c5d923a981bf4243176b0e670&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVMR7Q4I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIHHNtJZiXq65keVCq%2FAGA65iLjpHNmOXVn0bGC8DalSeAiEA1NgxtVu6vwAsdVe9JRgA5UUkKzGfR%2FNv8umat9dc01Eq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDKseRt3PIbmCUiQ9KyrcA3Dp9K%2FbAREJRxXyfqFCZikapab%2FI9KgBFI3gcg2Yh%2BWE88hzL2BoTHgq0jiUp%2FdhkAZzO1fNlJYoR2T2wgxQeX8MDxBgcJsV%2BhLQRJrD6hM3P7xeSrzoC9m2p%2Fyt2Dm42fRKNSWuxyAnTvKoMgdhfU50B2cgYU7tssnw%2BrX9WThZ7XSllNm7Rf1IzuC%2Fheuzm29%2FXelhVWZPqDO%2FGrbUAzuAGWT8GffvU2nR4IOZYwN4nS5I4SR5E%2BShDl2nYHqfaWu3afq4v5g%2Bx6C%2FE2UBLAcnMxnPScLz%2BkILMkYuRK%2FnOt9R%2BDzp3bxtoQJgX8JiReK0eYcJ00COGzO5l6baealDagDnNENfctL2zpPLs30ImtkG0epHJaXcvz%2Brd2039stgKK6aabaM6TNXqxJ49Aq3jQUp8TK8ogJL2sT9CyOqZjEZGA5yv%2BnPaIq7nob86bQqMXBQz4Pe2iOy919lbl8jVnynEIJgpowSNIBLHzwrSjqsH9ZYHWdCvEoGH0IenQf7xEWLwLG4pz7ZCKSON4NJ11OmOycI4eWr8DER%2BgHFvywJczqvtuGhDtMZKAHymZzkllsiS2MHmB3iClnA3Zftq9xAS1sRBpXGtuvA6MURwOdhUToH5A4f2fmMN28iL0GOqUBhjYS8oljEjCbqe7XLVTNMakjrNmJmmx3oNWIuR0jR%2FtV0ZcHKWuUJwG1HoeMqCA1WwPqBCZTak0PHfPBCiG0Ap61zdb7c1ClArrK%2BTaNG6Oy1wWnJXd57XXQSpR3k5uA1lg0BjgapYunPGLe7i78rbkoZw82RPnh53i4ECLc3EMTiudmEVhT4MkYj7uP4%2BoHhpaJHqH1TwVq4SCxLdGuGjhFzyJl&X-Amz-Signature=467891eddb43e6a62ac738e2b8b410a344c22a78f7495999e9b6dbdde8b1b861&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVMR7Q4I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIHHNtJZiXq65keVCq%2FAGA65iLjpHNmOXVn0bGC8DalSeAiEA1NgxtVu6vwAsdVe9JRgA5UUkKzGfR%2FNv8umat9dc01Eq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDKseRt3PIbmCUiQ9KyrcA3Dp9K%2FbAREJRxXyfqFCZikapab%2FI9KgBFI3gcg2Yh%2BWE88hzL2BoTHgq0jiUp%2FdhkAZzO1fNlJYoR2T2wgxQeX8MDxBgcJsV%2BhLQRJrD6hM3P7xeSrzoC9m2p%2Fyt2Dm42fRKNSWuxyAnTvKoMgdhfU50B2cgYU7tssnw%2BrX9WThZ7XSllNm7Rf1IzuC%2Fheuzm29%2FXelhVWZPqDO%2FGrbUAzuAGWT8GffvU2nR4IOZYwN4nS5I4SR5E%2BShDl2nYHqfaWu3afq4v5g%2Bx6C%2FE2UBLAcnMxnPScLz%2BkILMkYuRK%2FnOt9R%2BDzp3bxtoQJgX8JiReK0eYcJ00COGzO5l6baealDagDnNENfctL2zpPLs30ImtkG0epHJaXcvz%2Brd2039stgKK6aabaM6TNXqxJ49Aq3jQUp8TK8ogJL2sT9CyOqZjEZGA5yv%2BnPaIq7nob86bQqMXBQz4Pe2iOy919lbl8jVnynEIJgpowSNIBLHzwrSjqsH9ZYHWdCvEoGH0IenQf7xEWLwLG4pz7ZCKSON4NJ11OmOycI4eWr8DER%2BgHFvywJczqvtuGhDtMZKAHymZzkllsiS2MHmB3iClnA3Zftq9xAS1sRBpXGtuvA6MURwOdhUToH5A4f2fmMN28iL0GOqUBhjYS8oljEjCbqe7XLVTNMakjrNmJmmx3oNWIuR0jR%2FtV0ZcHKWuUJwG1HoeMqCA1WwPqBCZTak0PHfPBCiG0Ap61zdb7c1ClArrK%2BTaNG6Oy1wWnJXd57XXQSpR3k5uA1lg0BjgapYunPGLe7i78rbkoZw82RPnh53i4ECLc3EMTiudmEVhT4MkYj7uP4%2BoHhpaJHqH1TwVq4SCxLdGuGjhFzyJl&X-Amz-Signature=0948a2f22859965f6844929f5ba584da1aba977df9baad263b6df3015571fa97&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVMR7Q4I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIHHNtJZiXq65keVCq%2FAGA65iLjpHNmOXVn0bGC8DalSeAiEA1NgxtVu6vwAsdVe9JRgA5UUkKzGfR%2FNv8umat9dc01Eq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDKseRt3PIbmCUiQ9KyrcA3Dp9K%2FbAREJRxXyfqFCZikapab%2FI9KgBFI3gcg2Yh%2BWE88hzL2BoTHgq0jiUp%2FdhkAZzO1fNlJYoR2T2wgxQeX8MDxBgcJsV%2BhLQRJrD6hM3P7xeSrzoC9m2p%2Fyt2Dm42fRKNSWuxyAnTvKoMgdhfU50B2cgYU7tssnw%2BrX9WThZ7XSllNm7Rf1IzuC%2Fheuzm29%2FXelhVWZPqDO%2FGrbUAzuAGWT8GffvU2nR4IOZYwN4nS5I4SR5E%2BShDl2nYHqfaWu3afq4v5g%2Bx6C%2FE2UBLAcnMxnPScLz%2BkILMkYuRK%2FnOt9R%2BDzp3bxtoQJgX8JiReK0eYcJ00COGzO5l6baealDagDnNENfctL2zpPLs30ImtkG0epHJaXcvz%2Brd2039stgKK6aabaM6TNXqxJ49Aq3jQUp8TK8ogJL2sT9CyOqZjEZGA5yv%2BnPaIq7nob86bQqMXBQz4Pe2iOy919lbl8jVnynEIJgpowSNIBLHzwrSjqsH9ZYHWdCvEoGH0IenQf7xEWLwLG4pz7ZCKSON4NJ11OmOycI4eWr8DER%2BgHFvywJczqvtuGhDtMZKAHymZzkllsiS2MHmB3iClnA3Zftq9xAS1sRBpXGtuvA6MURwOdhUToH5A4f2fmMN28iL0GOqUBhjYS8oljEjCbqe7XLVTNMakjrNmJmmx3oNWIuR0jR%2FtV0ZcHKWuUJwG1HoeMqCA1WwPqBCZTak0PHfPBCiG0Ap61zdb7c1ClArrK%2BTaNG6Oy1wWnJXd57XXQSpR3k5uA1lg0BjgapYunPGLe7i78rbkoZw82RPnh53i4ECLc3EMTiudmEVhT4MkYj7uP4%2BoHhpaJHqH1TwVq4SCxLdGuGjhFzyJl&X-Amz-Signature=321f555e1a922d7a4735f34f428a9a3010da75dda47fe2e69c3282f24ce6a905&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVMR7Q4I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIHHNtJZiXq65keVCq%2FAGA65iLjpHNmOXVn0bGC8DalSeAiEA1NgxtVu6vwAsdVe9JRgA5UUkKzGfR%2FNv8umat9dc01Eq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDKseRt3PIbmCUiQ9KyrcA3Dp9K%2FbAREJRxXyfqFCZikapab%2FI9KgBFI3gcg2Yh%2BWE88hzL2BoTHgq0jiUp%2FdhkAZzO1fNlJYoR2T2wgxQeX8MDxBgcJsV%2BhLQRJrD6hM3P7xeSrzoC9m2p%2Fyt2Dm42fRKNSWuxyAnTvKoMgdhfU50B2cgYU7tssnw%2BrX9WThZ7XSllNm7Rf1IzuC%2Fheuzm29%2FXelhVWZPqDO%2FGrbUAzuAGWT8GffvU2nR4IOZYwN4nS5I4SR5E%2BShDl2nYHqfaWu3afq4v5g%2Bx6C%2FE2UBLAcnMxnPScLz%2BkILMkYuRK%2FnOt9R%2BDzp3bxtoQJgX8JiReK0eYcJ00COGzO5l6baealDagDnNENfctL2zpPLs30ImtkG0epHJaXcvz%2Brd2039stgKK6aabaM6TNXqxJ49Aq3jQUp8TK8ogJL2sT9CyOqZjEZGA5yv%2BnPaIq7nob86bQqMXBQz4Pe2iOy919lbl8jVnynEIJgpowSNIBLHzwrSjqsH9ZYHWdCvEoGH0IenQf7xEWLwLG4pz7ZCKSON4NJ11OmOycI4eWr8DER%2BgHFvywJczqvtuGhDtMZKAHymZzkllsiS2MHmB3iClnA3Zftq9xAS1sRBpXGtuvA6MURwOdhUToH5A4f2fmMN28iL0GOqUBhjYS8oljEjCbqe7XLVTNMakjrNmJmmx3oNWIuR0jR%2FtV0ZcHKWuUJwG1HoeMqCA1WwPqBCZTak0PHfPBCiG0Ap61zdb7c1ClArrK%2BTaNG6Oy1wWnJXd57XXQSpR3k5uA1lg0BjgapYunPGLe7i78rbkoZw82RPnh53i4ECLc3EMTiudmEVhT4MkYj7uP4%2BoHhpaJHqH1TwVq4SCxLdGuGjhFzyJl&X-Amz-Signature=8c01b4148783ee51ae0422a935061b217a81bafd3222d25e297bc103785434ce&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVMR7Q4I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIHHNtJZiXq65keVCq%2FAGA65iLjpHNmOXVn0bGC8DalSeAiEA1NgxtVu6vwAsdVe9JRgA5UUkKzGfR%2FNv8umat9dc01Eq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDKseRt3PIbmCUiQ9KyrcA3Dp9K%2FbAREJRxXyfqFCZikapab%2FI9KgBFI3gcg2Yh%2BWE88hzL2BoTHgq0jiUp%2FdhkAZzO1fNlJYoR2T2wgxQeX8MDxBgcJsV%2BhLQRJrD6hM3P7xeSrzoC9m2p%2Fyt2Dm42fRKNSWuxyAnTvKoMgdhfU50B2cgYU7tssnw%2BrX9WThZ7XSllNm7Rf1IzuC%2Fheuzm29%2FXelhVWZPqDO%2FGrbUAzuAGWT8GffvU2nR4IOZYwN4nS5I4SR5E%2BShDl2nYHqfaWu3afq4v5g%2Bx6C%2FE2UBLAcnMxnPScLz%2BkILMkYuRK%2FnOt9R%2BDzp3bxtoQJgX8JiReK0eYcJ00COGzO5l6baealDagDnNENfctL2zpPLs30ImtkG0epHJaXcvz%2Brd2039stgKK6aabaM6TNXqxJ49Aq3jQUp8TK8ogJL2sT9CyOqZjEZGA5yv%2BnPaIq7nob86bQqMXBQz4Pe2iOy919lbl8jVnynEIJgpowSNIBLHzwrSjqsH9ZYHWdCvEoGH0IenQf7xEWLwLG4pz7ZCKSON4NJ11OmOycI4eWr8DER%2BgHFvywJczqvtuGhDtMZKAHymZzkllsiS2MHmB3iClnA3Zftq9xAS1sRBpXGtuvA6MURwOdhUToH5A4f2fmMN28iL0GOqUBhjYS8oljEjCbqe7XLVTNMakjrNmJmmx3oNWIuR0jR%2FtV0ZcHKWuUJwG1HoeMqCA1WwPqBCZTak0PHfPBCiG0Ap61zdb7c1ClArrK%2BTaNG6Oy1wWnJXd57XXQSpR3k5uA1lg0BjgapYunPGLe7i78rbkoZw82RPnh53i4ECLc3EMTiudmEVhT4MkYj7uP4%2BoHhpaJHqH1TwVq4SCxLdGuGjhFzyJl&X-Amz-Signature=aef4bea98ddcdb1cd3c9865a28a5549e1a99134003a2da0d6a4ce80f3b9dae74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVMR7Q4I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIHHNtJZiXq65keVCq%2FAGA65iLjpHNmOXVn0bGC8DalSeAiEA1NgxtVu6vwAsdVe9JRgA5UUkKzGfR%2FNv8umat9dc01Eq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDKseRt3PIbmCUiQ9KyrcA3Dp9K%2FbAREJRxXyfqFCZikapab%2FI9KgBFI3gcg2Yh%2BWE88hzL2BoTHgq0jiUp%2FdhkAZzO1fNlJYoR2T2wgxQeX8MDxBgcJsV%2BhLQRJrD6hM3P7xeSrzoC9m2p%2Fyt2Dm42fRKNSWuxyAnTvKoMgdhfU50B2cgYU7tssnw%2BrX9WThZ7XSllNm7Rf1IzuC%2Fheuzm29%2FXelhVWZPqDO%2FGrbUAzuAGWT8GffvU2nR4IOZYwN4nS5I4SR5E%2BShDl2nYHqfaWu3afq4v5g%2Bx6C%2FE2UBLAcnMxnPScLz%2BkILMkYuRK%2FnOt9R%2BDzp3bxtoQJgX8JiReK0eYcJ00COGzO5l6baealDagDnNENfctL2zpPLs30ImtkG0epHJaXcvz%2Brd2039stgKK6aabaM6TNXqxJ49Aq3jQUp8TK8ogJL2sT9CyOqZjEZGA5yv%2BnPaIq7nob86bQqMXBQz4Pe2iOy919lbl8jVnynEIJgpowSNIBLHzwrSjqsH9ZYHWdCvEoGH0IenQf7xEWLwLG4pz7ZCKSON4NJ11OmOycI4eWr8DER%2BgHFvywJczqvtuGhDtMZKAHymZzkllsiS2MHmB3iClnA3Zftq9xAS1sRBpXGtuvA6MURwOdhUToH5A4f2fmMN28iL0GOqUBhjYS8oljEjCbqe7XLVTNMakjrNmJmmx3oNWIuR0jR%2FtV0ZcHKWuUJwG1HoeMqCA1WwPqBCZTak0PHfPBCiG0Ap61zdb7c1ClArrK%2BTaNG6Oy1wWnJXd57XXQSpR3k5uA1lg0BjgapYunPGLe7i78rbkoZw82RPnh53i4ECLc3EMTiudmEVhT4MkYj7uP4%2BoHhpaJHqH1TwVq4SCxLdGuGjhFzyJl&X-Amz-Signature=c99c05debd9a4e4787dbd9a237b251728055518a52e7e400c41cdb0bae97c1e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVMR7Q4I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIHHNtJZiXq65keVCq%2FAGA65iLjpHNmOXVn0bGC8DalSeAiEA1NgxtVu6vwAsdVe9JRgA5UUkKzGfR%2FNv8umat9dc01Eq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDKseRt3PIbmCUiQ9KyrcA3Dp9K%2FbAREJRxXyfqFCZikapab%2FI9KgBFI3gcg2Yh%2BWE88hzL2BoTHgq0jiUp%2FdhkAZzO1fNlJYoR2T2wgxQeX8MDxBgcJsV%2BhLQRJrD6hM3P7xeSrzoC9m2p%2Fyt2Dm42fRKNSWuxyAnTvKoMgdhfU50B2cgYU7tssnw%2BrX9WThZ7XSllNm7Rf1IzuC%2Fheuzm29%2FXelhVWZPqDO%2FGrbUAzuAGWT8GffvU2nR4IOZYwN4nS5I4SR5E%2BShDl2nYHqfaWu3afq4v5g%2Bx6C%2FE2UBLAcnMxnPScLz%2BkILMkYuRK%2FnOt9R%2BDzp3bxtoQJgX8JiReK0eYcJ00COGzO5l6baealDagDnNENfctL2zpPLs30ImtkG0epHJaXcvz%2Brd2039stgKK6aabaM6TNXqxJ49Aq3jQUp8TK8ogJL2sT9CyOqZjEZGA5yv%2BnPaIq7nob86bQqMXBQz4Pe2iOy919lbl8jVnynEIJgpowSNIBLHzwrSjqsH9ZYHWdCvEoGH0IenQf7xEWLwLG4pz7ZCKSON4NJ11OmOycI4eWr8DER%2BgHFvywJczqvtuGhDtMZKAHymZzkllsiS2MHmB3iClnA3Zftq9xAS1sRBpXGtuvA6MURwOdhUToH5A4f2fmMN28iL0GOqUBhjYS8oljEjCbqe7XLVTNMakjrNmJmmx3oNWIuR0jR%2FtV0ZcHKWuUJwG1HoeMqCA1WwPqBCZTak0PHfPBCiG0Ap61zdb7c1ClArrK%2BTaNG6Oy1wWnJXd57XXQSpR3k5uA1lg0BjgapYunPGLe7i78rbkoZw82RPnh53i4ECLc3EMTiudmEVhT4MkYj7uP4%2BoHhpaJHqH1TwVq4SCxLdGuGjhFzyJl&X-Amz-Signature=ad76a4f2e8d57f78f946507fa005560a0284a91061c702c249a35f5bf6f25ba5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX7QDMI5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQD1mAlmInRaGKHa8s3ywhno60kDHaNLyLfcXJ2bACp0%2BAIhAOUKW7BuPKKa%2FXI1Orwz62%2BveqmAjTERkqSlcFjS9df9Kv8DCC8QABoMNjM3NDIzMTgzODA1Igw0INvBVHuc7Mjhb8sq3AP2jSdVDVOTszxxQ2Qv%2F8guNDYCp56uu1QMFt3sr28khHgJttlP9C8L7LnT0SUVpVJmOscjKTkmYQ%2F6n%2BevwOrlU8RKEGXRdYMTgemyjD%2BTk4hkq%2B4NyTC196%2FnZm%2Bb%2Bv%2BowkvovaV3dem%2BAlOV78SmJRlKEMuWxajqSPMgmViCaNC4YmDWhT9nlRmcJzxr%2BJpie%2B8oH7qfojQx2G1fc3qobfDW16mPs%2BWWc2D3w1vWyTABGJ8uVJwAbLp98zC%2FdOzfNMkjBqxcvF3HUApsGWz7944KS9TGHY48bVLA1pgCiVwTCW4eo%2BJl9Djbdm5ZIGWT5YlMB1MyBKoXdDSD9auvJdEGfXLfDgh5vyxLL8paImTnx6%2FXMhSTIw1DSsUTFWZnpZWyTcWAb7o79G7kRrmvMi2RZU6%2FCl6smRn%2F5NjKyn6vYTQmdGeH6hMMLwyYEB%2B7WLzzUuSrqaslPHoUrepIaHEb6%2FZdA3Ce3OpORxMkOZED9J2lKLDS8DM3K%2FEGTtgZkOE3k5d0T7IMZQjf6nJ1AVGqxGitF33778uPXNkxrAVlZonaYyxkoI7fHK5%2BepWbgsQdWf8VJofXXiauKmdpG7BF0Vc2mVoThcWB1ZHI2o3yX0rFreyH3JxB1TCZvYi9BjqkAQoLiNfHDK105Wvm6lDHA8rDv9JDhE7JUIFoTTbr%2FnNP7bb%2FbA6JGOX%2FU10Y5yJIsczr%2Fb8KRF%2B5%2BUI03cKUbkBVeYbxPh%2F2br4SFCsaZcTRppONbtvH6sBSKv7ze8AtNkGJ8gwgf%2Be9Qvu2ElpFjp53zEcDDs7MFqGqHfUdf8gDZ5qGha%2FNjL1wqA67geuQPQDfTSf7likD%2BPzoUeAR8rAo6grN&X-Amz-Signature=ad3b34d16843bfce6136010ae55510a56619e2239304fb8b4438fd280c33a044&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX7QDMI5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQD1mAlmInRaGKHa8s3ywhno60kDHaNLyLfcXJ2bACp0%2BAIhAOUKW7BuPKKa%2FXI1Orwz62%2BveqmAjTERkqSlcFjS9df9Kv8DCC8QABoMNjM3NDIzMTgzODA1Igw0INvBVHuc7Mjhb8sq3AP2jSdVDVOTszxxQ2Qv%2F8guNDYCp56uu1QMFt3sr28khHgJttlP9C8L7LnT0SUVpVJmOscjKTkmYQ%2F6n%2BevwOrlU8RKEGXRdYMTgemyjD%2BTk4hkq%2B4NyTC196%2FnZm%2Bb%2Bv%2BowkvovaV3dem%2BAlOV78SmJRlKEMuWxajqSPMgmViCaNC4YmDWhT9nlRmcJzxr%2BJpie%2B8oH7qfojQx2G1fc3qobfDW16mPs%2BWWc2D3w1vWyTABGJ8uVJwAbLp98zC%2FdOzfNMkjBqxcvF3HUApsGWz7944KS9TGHY48bVLA1pgCiVwTCW4eo%2BJl9Djbdm5ZIGWT5YlMB1MyBKoXdDSD9auvJdEGfXLfDgh5vyxLL8paImTnx6%2FXMhSTIw1DSsUTFWZnpZWyTcWAb7o79G7kRrmvMi2RZU6%2FCl6smRn%2F5NjKyn6vYTQmdGeH6hMMLwyYEB%2B7WLzzUuSrqaslPHoUrepIaHEb6%2FZdA3Ce3OpORxMkOZED9J2lKLDS8DM3K%2FEGTtgZkOE3k5d0T7IMZQjf6nJ1AVGqxGitF33778uPXNkxrAVlZonaYyxkoI7fHK5%2BepWbgsQdWf8VJofXXiauKmdpG7BF0Vc2mVoThcWB1ZHI2o3yX0rFreyH3JxB1TCZvYi9BjqkAQoLiNfHDK105Wvm6lDHA8rDv9JDhE7JUIFoTTbr%2FnNP7bb%2FbA6JGOX%2FU10Y5yJIsczr%2Fb8KRF%2B5%2BUI03cKUbkBVeYbxPh%2F2br4SFCsaZcTRppONbtvH6sBSKv7ze8AtNkGJ8gwgf%2Be9Qvu2ElpFjp53zEcDDs7MFqGqHfUdf8gDZ5qGha%2FNjL1wqA67geuQPQDfTSf7likD%2BPzoUeAR8rAo6grN&X-Amz-Signature=e03c56b1a239bcf5be8e9fe59a4ad015859f88f4a6fc6da8160abb547cff5eeb&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
