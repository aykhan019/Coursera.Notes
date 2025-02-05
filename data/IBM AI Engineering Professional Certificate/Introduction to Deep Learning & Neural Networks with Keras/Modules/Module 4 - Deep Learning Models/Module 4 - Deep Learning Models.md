

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MS7NSD3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIFw7dCnh1dnMQrJWJi4jsDzwkLWjlZKIk7xPab0qzvREAiEAzPaPeVnc3eLZzItMtemhBc%2BUGQQd4KuobUIM4WyZcF8q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBqyOv2V0Tnh1KkDLCrcA87HbbbOtifPZB3Ywjzul3sfFBOlNqSAKRQ3hGGvPsCrIS6MVL4jQWm%2Fe4onb7fxKKyNYNGxWasrx69ZJm4LmL5ER2%2FRMo5dS3KOEvqZCZ8eMeOT06UpmpL0GVexIjKF1kY8mkXDYTaXkLuWd5U8rQ%2FOpQKmwZvYZaPDR%2FdNGRoDMEaaqYHlKPS5SgHnnEoJQXn5OaFD6Ge2eACjezZwEZ5ZHtM0a9PxkQB81ppDjhd3Ag77IoKV%2FwugFYHafEJKsAtGUBccUDUZ%2FNZ41Jh6kKPb3X%2FiXkgW%2FzI%2BYMWWbyfdxUJFbYVst%2F%2BzY8sU0%2B9fvCPROOL5nj4%2BsC5wOZYNTZWisd2l77XKZN5gX%2FN%2FCGTRJgzCReG0xra4jFxCGr6m3A1QIGrEq1sTSGoNvYZI9awp21aIA4S4e1Vo1y9sEzgZvkP%2Fg%2BcC%2FcsPloR5JR5zUFoM0V2o4rOGt4EOMQF4qjk0yKST96CO%2FWyxH8AxtG7Agb2E4Xc9q1T7SdG5NADbaA1fAITZJLyTrRc%2BwsUsZQOmS8EHk22igb0uF%2B8FE7HtMH4ATMm%2F6tv0kRoNpCQpXGjzm2sH4Hqb41Xl4nKRMzYwGadVbfwmIPSb9vy3JlkVf08OOg9gTpkl8FSnMKrfj70GOqUBPZM64mxvPVYtCulPJ7LMQ608HCijIMJyz5lJR4iSPvF1XYjYu7AyXDhff1YQo96l8BOhsPws5UfjqKtWUok7RkKXmyQdiv8U1ntnSgF1%2BtJRQR%2BGubv95iuUrR7FVkT0zwYUEZmNvzmWTehGV6stwqc9xB5UyrrOTAIQ%2Fm4Fjh9AmZ%2BNr0HaJe08Gpeox8OoDCWtjptg2CAGbGaLUQfS7RPVhVM2&X-Amz-Signature=0ab4f88996197ca229855e9bebee0bd6bf89d96e22b6a30fb8911bc88e938bcc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MS7NSD3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIFw7dCnh1dnMQrJWJi4jsDzwkLWjlZKIk7xPab0qzvREAiEAzPaPeVnc3eLZzItMtemhBc%2BUGQQd4KuobUIM4WyZcF8q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBqyOv2V0Tnh1KkDLCrcA87HbbbOtifPZB3Ywjzul3sfFBOlNqSAKRQ3hGGvPsCrIS6MVL4jQWm%2Fe4onb7fxKKyNYNGxWasrx69ZJm4LmL5ER2%2FRMo5dS3KOEvqZCZ8eMeOT06UpmpL0GVexIjKF1kY8mkXDYTaXkLuWd5U8rQ%2FOpQKmwZvYZaPDR%2FdNGRoDMEaaqYHlKPS5SgHnnEoJQXn5OaFD6Ge2eACjezZwEZ5ZHtM0a9PxkQB81ppDjhd3Ag77IoKV%2FwugFYHafEJKsAtGUBccUDUZ%2FNZ41Jh6kKPb3X%2FiXkgW%2FzI%2BYMWWbyfdxUJFbYVst%2F%2BzY8sU0%2B9fvCPROOL5nj4%2BsC5wOZYNTZWisd2l77XKZN5gX%2FN%2FCGTRJgzCReG0xra4jFxCGr6m3A1QIGrEq1sTSGoNvYZI9awp21aIA4S4e1Vo1y9sEzgZvkP%2Fg%2BcC%2FcsPloR5JR5zUFoM0V2o4rOGt4EOMQF4qjk0yKST96CO%2FWyxH8AxtG7Agb2E4Xc9q1T7SdG5NADbaA1fAITZJLyTrRc%2BwsUsZQOmS8EHk22igb0uF%2B8FE7HtMH4ATMm%2F6tv0kRoNpCQpXGjzm2sH4Hqb41Xl4nKRMzYwGadVbfwmIPSb9vy3JlkVf08OOg9gTpkl8FSnMKrfj70GOqUBPZM64mxvPVYtCulPJ7LMQ608HCijIMJyz5lJR4iSPvF1XYjYu7AyXDhff1YQo96l8BOhsPws5UfjqKtWUok7RkKXmyQdiv8U1ntnSgF1%2BtJRQR%2BGubv95iuUrR7FVkT0zwYUEZmNvzmWTehGV6stwqc9xB5UyrrOTAIQ%2Fm4Fjh9AmZ%2BNr0HaJe08Gpeox8OoDCWtjptg2CAGbGaLUQfS7RPVhVM2&X-Amz-Signature=22a640494e4d21a2b1a21f308a6e6404d3f7444eabe5d43113d2a84f3a2c483b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MS7NSD3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIFw7dCnh1dnMQrJWJi4jsDzwkLWjlZKIk7xPab0qzvREAiEAzPaPeVnc3eLZzItMtemhBc%2BUGQQd4KuobUIM4WyZcF8q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBqyOv2V0Tnh1KkDLCrcA87HbbbOtifPZB3Ywjzul3sfFBOlNqSAKRQ3hGGvPsCrIS6MVL4jQWm%2Fe4onb7fxKKyNYNGxWasrx69ZJm4LmL5ER2%2FRMo5dS3KOEvqZCZ8eMeOT06UpmpL0GVexIjKF1kY8mkXDYTaXkLuWd5U8rQ%2FOpQKmwZvYZaPDR%2FdNGRoDMEaaqYHlKPS5SgHnnEoJQXn5OaFD6Ge2eACjezZwEZ5ZHtM0a9PxkQB81ppDjhd3Ag77IoKV%2FwugFYHafEJKsAtGUBccUDUZ%2FNZ41Jh6kKPb3X%2FiXkgW%2FzI%2BYMWWbyfdxUJFbYVst%2F%2BzY8sU0%2B9fvCPROOL5nj4%2BsC5wOZYNTZWisd2l77XKZN5gX%2FN%2FCGTRJgzCReG0xra4jFxCGr6m3A1QIGrEq1sTSGoNvYZI9awp21aIA4S4e1Vo1y9sEzgZvkP%2Fg%2BcC%2FcsPloR5JR5zUFoM0V2o4rOGt4EOMQF4qjk0yKST96CO%2FWyxH8AxtG7Agb2E4Xc9q1T7SdG5NADbaA1fAITZJLyTrRc%2BwsUsZQOmS8EHk22igb0uF%2B8FE7HtMH4ATMm%2F6tv0kRoNpCQpXGjzm2sH4Hqb41Xl4nKRMzYwGadVbfwmIPSb9vy3JlkVf08OOg9gTpkl8FSnMKrfj70GOqUBPZM64mxvPVYtCulPJ7LMQ608HCijIMJyz5lJR4iSPvF1XYjYu7AyXDhff1YQo96l8BOhsPws5UfjqKtWUok7RkKXmyQdiv8U1ntnSgF1%2BtJRQR%2BGubv95iuUrR7FVkT0zwYUEZmNvzmWTehGV6stwqc9xB5UyrrOTAIQ%2Fm4Fjh9AmZ%2BNr0HaJe08Gpeox8OoDCWtjptg2CAGbGaLUQfS7RPVhVM2&X-Amz-Signature=17ecc6d61cbebc7e4559eb4abb2216d16525f5965a14045e66fbeed7289b5a84&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MS7NSD3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIFw7dCnh1dnMQrJWJi4jsDzwkLWjlZKIk7xPab0qzvREAiEAzPaPeVnc3eLZzItMtemhBc%2BUGQQd4KuobUIM4WyZcF8q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBqyOv2V0Tnh1KkDLCrcA87HbbbOtifPZB3Ywjzul3sfFBOlNqSAKRQ3hGGvPsCrIS6MVL4jQWm%2Fe4onb7fxKKyNYNGxWasrx69ZJm4LmL5ER2%2FRMo5dS3KOEvqZCZ8eMeOT06UpmpL0GVexIjKF1kY8mkXDYTaXkLuWd5U8rQ%2FOpQKmwZvYZaPDR%2FdNGRoDMEaaqYHlKPS5SgHnnEoJQXn5OaFD6Ge2eACjezZwEZ5ZHtM0a9PxkQB81ppDjhd3Ag77IoKV%2FwugFYHafEJKsAtGUBccUDUZ%2FNZ41Jh6kKPb3X%2FiXkgW%2FzI%2BYMWWbyfdxUJFbYVst%2F%2BzY8sU0%2B9fvCPROOL5nj4%2BsC5wOZYNTZWisd2l77XKZN5gX%2FN%2FCGTRJgzCReG0xra4jFxCGr6m3A1QIGrEq1sTSGoNvYZI9awp21aIA4S4e1Vo1y9sEzgZvkP%2Fg%2BcC%2FcsPloR5JR5zUFoM0V2o4rOGt4EOMQF4qjk0yKST96CO%2FWyxH8AxtG7Agb2E4Xc9q1T7SdG5NADbaA1fAITZJLyTrRc%2BwsUsZQOmS8EHk22igb0uF%2B8FE7HtMH4ATMm%2F6tv0kRoNpCQpXGjzm2sH4Hqb41Xl4nKRMzYwGadVbfwmIPSb9vy3JlkVf08OOg9gTpkl8FSnMKrfj70GOqUBPZM64mxvPVYtCulPJ7LMQ608HCijIMJyz5lJR4iSPvF1XYjYu7AyXDhff1YQo96l8BOhsPws5UfjqKtWUok7RkKXmyQdiv8U1ntnSgF1%2BtJRQR%2BGubv95iuUrR7FVkT0zwYUEZmNvzmWTehGV6stwqc9xB5UyrrOTAIQ%2Fm4Fjh9AmZ%2BNr0HaJe08Gpeox8OoDCWtjptg2CAGbGaLUQfS7RPVhVM2&X-Amz-Signature=da18bddf3e9cc99db255c05dfbe538d6f0f9da86cce47418edc7aa5a8c0572f8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MS7NSD3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIFw7dCnh1dnMQrJWJi4jsDzwkLWjlZKIk7xPab0qzvREAiEAzPaPeVnc3eLZzItMtemhBc%2BUGQQd4KuobUIM4WyZcF8q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBqyOv2V0Tnh1KkDLCrcA87HbbbOtifPZB3Ywjzul3sfFBOlNqSAKRQ3hGGvPsCrIS6MVL4jQWm%2Fe4onb7fxKKyNYNGxWasrx69ZJm4LmL5ER2%2FRMo5dS3KOEvqZCZ8eMeOT06UpmpL0GVexIjKF1kY8mkXDYTaXkLuWd5U8rQ%2FOpQKmwZvYZaPDR%2FdNGRoDMEaaqYHlKPS5SgHnnEoJQXn5OaFD6Ge2eACjezZwEZ5ZHtM0a9PxkQB81ppDjhd3Ag77IoKV%2FwugFYHafEJKsAtGUBccUDUZ%2FNZ41Jh6kKPb3X%2FiXkgW%2FzI%2BYMWWbyfdxUJFbYVst%2F%2BzY8sU0%2B9fvCPROOL5nj4%2BsC5wOZYNTZWisd2l77XKZN5gX%2FN%2FCGTRJgzCReG0xra4jFxCGr6m3A1QIGrEq1sTSGoNvYZI9awp21aIA4S4e1Vo1y9sEzgZvkP%2Fg%2BcC%2FcsPloR5JR5zUFoM0V2o4rOGt4EOMQF4qjk0yKST96CO%2FWyxH8AxtG7Agb2E4Xc9q1T7SdG5NADbaA1fAITZJLyTrRc%2BwsUsZQOmS8EHk22igb0uF%2B8FE7HtMH4ATMm%2F6tv0kRoNpCQpXGjzm2sH4Hqb41Xl4nKRMzYwGadVbfwmIPSb9vy3JlkVf08OOg9gTpkl8FSnMKrfj70GOqUBPZM64mxvPVYtCulPJ7LMQ608HCijIMJyz5lJR4iSPvF1XYjYu7AyXDhff1YQo96l8BOhsPws5UfjqKtWUok7RkKXmyQdiv8U1ntnSgF1%2BtJRQR%2BGubv95iuUrR7FVkT0zwYUEZmNvzmWTehGV6stwqc9xB5UyrrOTAIQ%2Fm4Fjh9AmZ%2BNr0HaJe08Gpeox8OoDCWtjptg2CAGbGaLUQfS7RPVhVM2&X-Amz-Signature=fa6c2fbb2979ab2dd61f7c804bcdd2b6131920525f643faf3968432eedcfd168&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MS7NSD3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIFw7dCnh1dnMQrJWJi4jsDzwkLWjlZKIk7xPab0qzvREAiEAzPaPeVnc3eLZzItMtemhBc%2BUGQQd4KuobUIM4WyZcF8q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBqyOv2V0Tnh1KkDLCrcA87HbbbOtifPZB3Ywjzul3sfFBOlNqSAKRQ3hGGvPsCrIS6MVL4jQWm%2Fe4onb7fxKKyNYNGxWasrx69ZJm4LmL5ER2%2FRMo5dS3KOEvqZCZ8eMeOT06UpmpL0GVexIjKF1kY8mkXDYTaXkLuWd5U8rQ%2FOpQKmwZvYZaPDR%2FdNGRoDMEaaqYHlKPS5SgHnnEoJQXn5OaFD6Ge2eACjezZwEZ5ZHtM0a9PxkQB81ppDjhd3Ag77IoKV%2FwugFYHafEJKsAtGUBccUDUZ%2FNZ41Jh6kKPb3X%2FiXkgW%2FzI%2BYMWWbyfdxUJFbYVst%2F%2BzY8sU0%2B9fvCPROOL5nj4%2BsC5wOZYNTZWisd2l77XKZN5gX%2FN%2FCGTRJgzCReG0xra4jFxCGr6m3A1QIGrEq1sTSGoNvYZI9awp21aIA4S4e1Vo1y9sEzgZvkP%2Fg%2BcC%2FcsPloR5JR5zUFoM0V2o4rOGt4EOMQF4qjk0yKST96CO%2FWyxH8AxtG7Agb2E4Xc9q1T7SdG5NADbaA1fAITZJLyTrRc%2BwsUsZQOmS8EHk22igb0uF%2B8FE7HtMH4ATMm%2F6tv0kRoNpCQpXGjzm2sH4Hqb41Xl4nKRMzYwGadVbfwmIPSb9vy3JlkVf08OOg9gTpkl8FSnMKrfj70GOqUBPZM64mxvPVYtCulPJ7LMQ608HCijIMJyz5lJR4iSPvF1XYjYu7AyXDhff1YQo96l8BOhsPws5UfjqKtWUok7RkKXmyQdiv8U1ntnSgF1%2BtJRQR%2BGubv95iuUrR7FVkT0zwYUEZmNvzmWTehGV6stwqc9xB5UyrrOTAIQ%2Fm4Fjh9AmZ%2BNr0HaJe08Gpeox8OoDCWtjptg2CAGbGaLUQfS7RPVhVM2&X-Amz-Signature=88d83c41a8502e8c880ef26625c303a8f9c2f0aefb4540dd36bed2e0eb5cd8bb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MS7NSD3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIFw7dCnh1dnMQrJWJi4jsDzwkLWjlZKIk7xPab0qzvREAiEAzPaPeVnc3eLZzItMtemhBc%2BUGQQd4KuobUIM4WyZcF8q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBqyOv2V0Tnh1KkDLCrcA87HbbbOtifPZB3Ywjzul3sfFBOlNqSAKRQ3hGGvPsCrIS6MVL4jQWm%2Fe4onb7fxKKyNYNGxWasrx69ZJm4LmL5ER2%2FRMo5dS3KOEvqZCZ8eMeOT06UpmpL0GVexIjKF1kY8mkXDYTaXkLuWd5U8rQ%2FOpQKmwZvYZaPDR%2FdNGRoDMEaaqYHlKPS5SgHnnEoJQXn5OaFD6Ge2eACjezZwEZ5ZHtM0a9PxkQB81ppDjhd3Ag77IoKV%2FwugFYHafEJKsAtGUBccUDUZ%2FNZ41Jh6kKPb3X%2FiXkgW%2FzI%2BYMWWbyfdxUJFbYVst%2F%2BzY8sU0%2B9fvCPROOL5nj4%2BsC5wOZYNTZWisd2l77XKZN5gX%2FN%2FCGTRJgzCReG0xra4jFxCGr6m3A1QIGrEq1sTSGoNvYZI9awp21aIA4S4e1Vo1y9sEzgZvkP%2Fg%2BcC%2FcsPloR5JR5zUFoM0V2o4rOGt4EOMQF4qjk0yKST96CO%2FWyxH8AxtG7Agb2E4Xc9q1T7SdG5NADbaA1fAITZJLyTrRc%2BwsUsZQOmS8EHk22igb0uF%2B8FE7HtMH4ATMm%2F6tv0kRoNpCQpXGjzm2sH4Hqb41Xl4nKRMzYwGadVbfwmIPSb9vy3JlkVf08OOg9gTpkl8FSnMKrfj70GOqUBPZM64mxvPVYtCulPJ7LMQ608HCijIMJyz5lJR4iSPvF1XYjYu7AyXDhff1YQo96l8BOhsPws5UfjqKtWUok7RkKXmyQdiv8U1ntnSgF1%2BtJRQR%2BGubv95iuUrR7FVkT0zwYUEZmNvzmWTehGV6stwqc9xB5UyrrOTAIQ%2Fm4Fjh9AmZ%2BNr0HaJe08Gpeox8OoDCWtjptg2CAGbGaLUQfS7RPVhVM2&X-Amz-Signature=f33c657e3f9cf2a331f9e794605ce87ee1d1d69cfe0569888e242a202a2ae6bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MS7NSD3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIFw7dCnh1dnMQrJWJi4jsDzwkLWjlZKIk7xPab0qzvREAiEAzPaPeVnc3eLZzItMtemhBc%2BUGQQd4KuobUIM4WyZcF8q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBqyOv2V0Tnh1KkDLCrcA87HbbbOtifPZB3Ywjzul3sfFBOlNqSAKRQ3hGGvPsCrIS6MVL4jQWm%2Fe4onb7fxKKyNYNGxWasrx69ZJm4LmL5ER2%2FRMo5dS3KOEvqZCZ8eMeOT06UpmpL0GVexIjKF1kY8mkXDYTaXkLuWd5U8rQ%2FOpQKmwZvYZaPDR%2FdNGRoDMEaaqYHlKPS5SgHnnEoJQXn5OaFD6Ge2eACjezZwEZ5ZHtM0a9PxkQB81ppDjhd3Ag77IoKV%2FwugFYHafEJKsAtGUBccUDUZ%2FNZ41Jh6kKPb3X%2FiXkgW%2FzI%2BYMWWbyfdxUJFbYVst%2F%2BzY8sU0%2B9fvCPROOL5nj4%2BsC5wOZYNTZWisd2l77XKZN5gX%2FN%2FCGTRJgzCReG0xra4jFxCGr6m3A1QIGrEq1sTSGoNvYZI9awp21aIA4S4e1Vo1y9sEzgZvkP%2Fg%2BcC%2FcsPloR5JR5zUFoM0V2o4rOGt4EOMQF4qjk0yKST96CO%2FWyxH8AxtG7Agb2E4Xc9q1T7SdG5NADbaA1fAITZJLyTrRc%2BwsUsZQOmS8EHk22igb0uF%2B8FE7HtMH4ATMm%2F6tv0kRoNpCQpXGjzm2sH4Hqb41Xl4nKRMzYwGadVbfwmIPSb9vy3JlkVf08OOg9gTpkl8FSnMKrfj70GOqUBPZM64mxvPVYtCulPJ7LMQ608HCijIMJyz5lJR4iSPvF1XYjYu7AyXDhff1YQo96l8BOhsPws5UfjqKtWUok7RkKXmyQdiv8U1ntnSgF1%2BtJRQR%2BGubv95iuUrR7FVkT0zwYUEZmNvzmWTehGV6stwqc9xB5UyrrOTAIQ%2Fm4Fjh9AmZ%2BNr0HaJe08Gpeox8OoDCWtjptg2CAGbGaLUQfS7RPVhVM2&X-Amz-Signature=41e7dffc3304c76fb9edb816aff40bfe48653d2044a04512cc2aba0a88e6c133&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MS7NSD3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIFw7dCnh1dnMQrJWJi4jsDzwkLWjlZKIk7xPab0qzvREAiEAzPaPeVnc3eLZzItMtemhBc%2BUGQQd4KuobUIM4WyZcF8q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBqyOv2V0Tnh1KkDLCrcA87HbbbOtifPZB3Ywjzul3sfFBOlNqSAKRQ3hGGvPsCrIS6MVL4jQWm%2Fe4onb7fxKKyNYNGxWasrx69ZJm4LmL5ER2%2FRMo5dS3KOEvqZCZ8eMeOT06UpmpL0GVexIjKF1kY8mkXDYTaXkLuWd5U8rQ%2FOpQKmwZvYZaPDR%2FdNGRoDMEaaqYHlKPS5SgHnnEoJQXn5OaFD6Ge2eACjezZwEZ5ZHtM0a9PxkQB81ppDjhd3Ag77IoKV%2FwugFYHafEJKsAtGUBccUDUZ%2FNZ41Jh6kKPb3X%2FiXkgW%2FzI%2BYMWWbyfdxUJFbYVst%2F%2BzY8sU0%2B9fvCPROOL5nj4%2BsC5wOZYNTZWisd2l77XKZN5gX%2FN%2FCGTRJgzCReG0xra4jFxCGr6m3A1QIGrEq1sTSGoNvYZI9awp21aIA4S4e1Vo1y9sEzgZvkP%2Fg%2BcC%2FcsPloR5JR5zUFoM0V2o4rOGt4EOMQF4qjk0yKST96CO%2FWyxH8AxtG7Agb2E4Xc9q1T7SdG5NADbaA1fAITZJLyTrRc%2BwsUsZQOmS8EHk22igb0uF%2B8FE7HtMH4ATMm%2F6tv0kRoNpCQpXGjzm2sH4Hqb41Xl4nKRMzYwGadVbfwmIPSb9vy3JlkVf08OOg9gTpkl8FSnMKrfj70GOqUBPZM64mxvPVYtCulPJ7LMQ608HCijIMJyz5lJR4iSPvF1XYjYu7AyXDhff1YQo96l8BOhsPws5UfjqKtWUok7RkKXmyQdiv8U1ntnSgF1%2BtJRQR%2BGubv95iuUrR7FVkT0zwYUEZmNvzmWTehGV6stwqc9xB5UyrrOTAIQ%2Fm4Fjh9AmZ%2BNr0HaJe08Gpeox8OoDCWtjptg2CAGbGaLUQfS7RPVhVM2&X-Amz-Signature=0a489e839ac04b739437054b1a6d3d390acc4c9b12f7389d3bc949b845755aaa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLGNC6FF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQDmARibAcj5scabeU6Rq2VjykKA2nkSuvnUUOpKU%2BqvBgIhALdtMJhw6nvnOv31FwMq%2FhitCwje8c1lMN14eGVyilvXKv8DCFAQABoMNjM3NDIzMTgzODA1IgzS%2FXJEPcxGxKxy6ogq3AMKIeNE4UAD6hOauEsaCLTRiCXPgoGV04RG9%2FCuGSgjtMR%2BnpoyzK6aPOzQaPTcSifS5kQ5ozj1FBidSDm2raEEdEw%2FTB3JhqHf8ZwAHMnFfQu2ADzIwxpT%2FoozlayE6MQjLQZavwznfawvYmB1cwg0zbwsjiEMKpo0bSAuaDRdZ9Nhu0khr%2F99ZRt6PsBKYL6j9jVXioqe2QWyc%2FbVMxJb1LMWY%2BZiwZ2YQSGgD4Dgw%2B7SyhE0PfaCpOcJNGWgYuJNQp71pRHcMaKb%2BGoZcz7HlBex%2BVVPdXrx49B0AunY5Wgkg%2BeA87yw%2BOFlO1rTERRMPfLh32PpkLJ9OYrwPMjwNBqVgYhoSxa1fmnf31ZvC8DNbQjXpYm1RC%2FZDbZu%2BoiOHU18ATGF7UKUK8CqvMtTTuoTGVxgRjTWNuYnEmXaYW7Hpl0eLb2bss7TjRliLPxqdja%2Bt9YccyHhnpWHmAog9AtP8zUBE7azDigY10VLgy1ICuDj7FK%2B5Au956synm1hyeHjOKxpnltS1CswUW2SvomCabW70c6mPbyTKALswoa0EinT7HcqI%2FNXonnNmevWmXEbhRECZA8j4Rrj8I8XWrmQwJNoxeIPvhOLmU2b6nmSAl9CxF9HnbkZbTCz24%2B9BjqkAcFORNa4%2BZkkFqdwQPm2qZryhLc8t60moODhUD5xwOK3AjqiTcUoMW9IhaEhzcqDIlOEEMzYfMuUe%2FMlHn7QuO76L%2BvQPqeNI6vtGFRIgeEcKAExYcfevvjNEYaEPvv9HX20akMKt21aWyikrz4xsF8Vg06h5IicHImvLlsioeYXaRTW5hrSetYMByY31ZQYqOImr6TSfJD0mzsXXdscY3afTVg8&X-Amz-Signature=00817f2fb540f024a407c54a2f23347da61438e6b2c2fa036f511182a1a6aad4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLGNC6FF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQDmARibAcj5scabeU6Rq2VjykKA2nkSuvnUUOpKU%2BqvBgIhALdtMJhw6nvnOv31FwMq%2FhitCwje8c1lMN14eGVyilvXKv8DCFAQABoMNjM3NDIzMTgzODA1IgzS%2FXJEPcxGxKxy6ogq3AMKIeNE4UAD6hOauEsaCLTRiCXPgoGV04RG9%2FCuGSgjtMR%2BnpoyzK6aPOzQaPTcSifS5kQ5ozj1FBidSDm2raEEdEw%2FTB3JhqHf8ZwAHMnFfQu2ADzIwxpT%2FoozlayE6MQjLQZavwznfawvYmB1cwg0zbwsjiEMKpo0bSAuaDRdZ9Nhu0khr%2F99ZRt6PsBKYL6j9jVXioqe2QWyc%2FbVMxJb1LMWY%2BZiwZ2YQSGgD4Dgw%2B7SyhE0PfaCpOcJNGWgYuJNQp71pRHcMaKb%2BGoZcz7HlBex%2BVVPdXrx49B0AunY5Wgkg%2BeA87yw%2BOFlO1rTERRMPfLh32PpkLJ9OYrwPMjwNBqVgYhoSxa1fmnf31ZvC8DNbQjXpYm1RC%2FZDbZu%2BoiOHU18ATGF7UKUK8CqvMtTTuoTGVxgRjTWNuYnEmXaYW7Hpl0eLb2bss7TjRliLPxqdja%2Bt9YccyHhnpWHmAog9AtP8zUBE7azDigY10VLgy1ICuDj7FK%2B5Au956synm1hyeHjOKxpnltS1CswUW2SvomCabW70c6mPbyTKALswoa0EinT7HcqI%2FNXonnNmevWmXEbhRECZA8j4Rrj8I8XWrmQwJNoxeIPvhOLmU2b6nmSAl9CxF9HnbkZbTCz24%2B9BjqkAcFORNa4%2BZkkFqdwQPm2qZryhLc8t60moODhUD5xwOK3AjqiTcUoMW9IhaEhzcqDIlOEEMzYfMuUe%2FMlHn7QuO76L%2BvQPqeNI6vtGFRIgeEcKAExYcfevvjNEYaEPvv9HX20akMKt21aWyikrz4xsF8Vg06h5IicHImvLlsioeYXaRTW5hrSetYMByY31ZQYqOImr6TSfJD0mzsXXdscY3afTVg8&X-Amz-Signature=c6267a35ed749dc27425effaf6565068072f99d47f82430dad39d96c0cecb023&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
