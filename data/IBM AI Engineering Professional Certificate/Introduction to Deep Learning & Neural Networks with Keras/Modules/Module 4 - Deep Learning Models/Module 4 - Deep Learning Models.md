

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGDJ36F7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCez57XQjsio0mofLZ46dSeVl9idJ9QJY8BleV48RxamQIgMK1z3Ey4sky5zDPWDatWZgB3HiOYeTCFEfV64vLYqAQqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKNKgBl9UI%2FUDidRiyrcA%2FtnFm3ZtCp3sFvecAf7IeloXrsNdQZWmwmjROAhLa9t17I7VRBPsdGfIK0ng3m4fUyuZRzs7IHcFWa6bdvdqt%2Fe2%2FX5vExvFMYSav%2Bu7vkUwuXwXVJrOTCS8ElSToFUjWhjG3WhSBkX8kvbv6ngQYwQYQcwMCeykMTqsJwmKtGbJJ1tWgfmp4wlJ%2F%2BS66HE6oxRucuslTK6dfAgsECiBFyqhfl6eWEl7ZOQneIeUZ0j%2Bfs5yKL43eA1xj%2FzGrVxWya1HtaR7g5HYYelZ4zNrFbq1Z%2BGZvqPt3hiy6vIxuT%2BCny3vJMlDI2GyVs%2BGPtk5%2F%2FXHyO6yI8zF%2BoM2chpnvMkOJ9c7lTJwjvUbvX6xnsLhZEj4eESdoJACwB%2BuG8ExEZFCLbkMXLn72FCEaqPQmazMOf0k0z%2FQkAJTQAKOL4OS5VesQxOJmyjE%2BO%2BeuRxGOyyQ7bVDyGa3EEHbb%2FLCtZsq7HPI%2Fg%2FaYORODgKY2vRHw8aqLdcf91dL56BW1eWFfZJv5USvC%2Bvw1IuR4HZOs3S7AlS5E49T4xo15IS%2BJZvY2sXUZkRZipMSLFh3seqDxCoacvu4fafqqAmY3EC%2FIIbCcGkjHUKZZHpAWc2RqNbRG%2FI7mmxEF6obI25MPaNnL0GOqUBHRUf9G%2Fs1Q96Yorp9hrvOw6M36XutuuDHTLUOQuAmbeRfc9Ek3Cui7MzCiQ7FiwagL7d%2FG0hGqwTAG%2BkIsyuMmfThgZ8f1KA4OlVwHQPlXEHjeVlTxb1uw1Bok%2Fof%2FkJIAiIH%2FYZzUnojjx%2BTcqxrsih8zEMOf9K9ib6tVljmKZ5Qvibr9LKTBqdtKFQG7YOIqnwRUrCQd1LIPPypLbJXL8hx1hq&X-Amz-Signature=8b0ccb687f3741d62c34dee0cbce5a2a9090aef9ee453be08a537d8f489b000c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGDJ36F7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCez57XQjsio0mofLZ46dSeVl9idJ9QJY8BleV48RxamQIgMK1z3Ey4sky5zDPWDatWZgB3HiOYeTCFEfV64vLYqAQqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKNKgBl9UI%2FUDidRiyrcA%2FtnFm3ZtCp3sFvecAf7IeloXrsNdQZWmwmjROAhLa9t17I7VRBPsdGfIK0ng3m4fUyuZRzs7IHcFWa6bdvdqt%2Fe2%2FX5vExvFMYSav%2Bu7vkUwuXwXVJrOTCS8ElSToFUjWhjG3WhSBkX8kvbv6ngQYwQYQcwMCeykMTqsJwmKtGbJJ1tWgfmp4wlJ%2F%2BS66HE6oxRucuslTK6dfAgsECiBFyqhfl6eWEl7ZOQneIeUZ0j%2Bfs5yKL43eA1xj%2FzGrVxWya1HtaR7g5HYYelZ4zNrFbq1Z%2BGZvqPt3hiy6vIxuT%2BCny3vJMlDI2GyVs%2BGPtk5%2F%2FXHyO6yI8zF%2BoM2chpnvMkOJ9c7lTJwjvUbvX6xnsLhZEj4eESdoJACwB%2BuG8ExEZFCLbkMXLn72FCEaqPQmazMOf0k0z%2FQkAJTQAKOL4OS5VesQxOJmyjE%2BO%2BeuRxGOyyQ7bVDyGa3EEHbb%2FLCtZsq7HPI%2Fg%2FaYORODgKY2vRHw8aqLdcf91dL56BW1eWFfZJv5USvC%2Bvw1IuR4HZOs3S7AlS5E49T4xo15IS%2BJZvY2sXUZkRZipMSLFh3seqDxCoacvu4fafqqAmY3EC%2FIIbCcGkjHUKZZHpAWc2RqNbRG%2FI7mmxEF6obI25MPaNnL0GOqUBHRUf9G%2Fs1Q96Yorp9hrvOw6M36XutuuDHTLUOQuAmbeRfc9Ek3Cui7MzCiQ7FiwagL7d%2FG0hGqwTAG%2BkIsyuMmfThgZ8f1KA4OlVwHQPlXEHjeVlTxb1uw1Bok%2Fof%2FkJIAiIH%2FYZzUnojjx%2BTcqxrsih8zEMOf9K9ib6tVljmKZ5Qvibr9LKTBqdtKFQG7YOIqnwRUrCQd1LIPPypLbJXL8hx1hq&X-Amz-Signature=5a5f65edd846787b0f0b87a36e8c3b9de0e8a85cdfac0a2a4ab1e0bc12bc2cad&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGDJ36F7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCez57XQjsio0mofLZ46dSeVl9idJ9QJY8BleV48RxamQIgMK1z3Ey4sky5zDPWDatWZgB3HiOYeTCFEfV64vLYqAQqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKNKgBl9UI%2FUDidRiyrcA%2FtnFm3ZtCp3sFvecAf7IeloXrsNdQZWmwmjROAhLa9t17I7VRBPsdGfIK0ng3m4fUyuZRzs7IHcFWa6bdvdqt%2Fe2%2FX5vExvFMYSav%2Bu7vkUwuXwXVJrOTCS8ElSToFUjWhjG3WhSBkX8kvbv6ngQYwQYQcwMCeykMTqsJwmKtGbJJ1tWgfmp4wlJ%2F%2BS66HE6oxRucuslTK6dfAgsECiBFyqhfl6eWEl7ZOQneIeUZ0j%2Bfs5yKL43eA1xj%2FzGrVxWya1HtaR7g5HYYelZ4zNrFbq1Z%2BGZvqPt3hiy6vIxuT%2BCny3vJMlDI2GyVs%2BGPtk5%2F%2FXHyO6yI8zF%2BoM2chpnvMkOJ9c7lTJwjvUbvX6xnsLhZEj4eESdoJACwB%2BuG8ExEZFCLbkMXLn72FCEaqPQmazMOf0k0z%2FQkAJTQAKOL4OS5VesQxOJmyjE%2BO%2BeuRxGOyyQ7bVDyGa3EEHbb%2FLCtZsq7HPI%2Fg%2FaYORODgKY2vRHw8aqLdcf91dL56BW1eWFfZJv5USvC%2Bvw1IuR4HZOs3S7AlS5E49T4xo15IS%2BJZvY2sXUZkRZipMSLFh3seqDxCoacvu4fafqqAmY3EC%2FIIbCcGkjHUKZZHpAWc2RqNbRG%2FI7mmxEF6obI25MPaNnL0GOqUBHRUf9G%2Fs1Q96Yorp9hrvOw6M36XutuuDHTLUOQuAmbeRfc9Ek3Cui7MzCiQ7FiwagL7d%2FG0hGqwTAG%2BkIsyuMmfThgZ8f1KA4OlVwHQPlXEHjeVlTxb1uw1Bok%2Fof%2FkJIAiIH%2FYZzUnojjx%2BTcqxrsih8zEMOf9K9ib6tVljmKZ5Qvibr9LKTBqdtKFQG7YOIqnwRUrCQd1LIPPypLbJXL8hx1hq&X-Amz-Signature=ed220a5cfb08c173c21f120973c86c6b4b43e8490c4c068fed3a5e7a04636056&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGDJ36F7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCez57XQjsio0mofLZ46dSeVl9idJ9QJY8BleV48RxamQIgMK1z3Ey4sky5zDPWDatWZgB3HiOYeTCFEfV64vLYqAQqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKNKgBl9UI%2FUDidRiyrcA%2FtnFm3ZtCp3sFvecAf7IeloXrsNdQZWmwmjROAhLa9t17I7VRBPsdGfIK0ng3m4fUyuZRzs7IHcFWa6bdvdqt%2Fe2%2FX5vExvFMYSav%2Bu7vkUwuXwXVJrOTCS8ElSToFUjWhjG3WhSBkX8kvbv6ngQYwQYQcwMCeykMTqsJwmKtGbJJ1tWgfmp4wlJ%2F%2BS66HE6oxRucuslTK6dfAgsECiBFyqhfl6eWEl7ZOQneIeUZ0j%2Bfs5yKL43eA1xj%2FzGrVxWya1HtaR7g5HYYelZ4zNrFbq1Z%2BGZvqPt3hiy6vIxuT%2BCny3vJMlDI2GyVs%2BGPtk5%2F%2FXHyO6yI8zF%2BoM2chpnvMkOJ9c7lTJwjvUbvX6xnsLhZEj4eESdoJACwB%2BuG8ExEZFCLbkMXLn72FCEaqPQmazMOf0k0z%2FQkAJTQAKOL4OS5VesQxOJmyjE%2BO%2BeuRxGOyyQ7bVDyGa3EEHbb%2FLCtZsq7HPI%2Fg%2FaYORODgKY2vRHw8aqLdcf91dL56BW1eWFfZJv5USvC%2Bvw1IuR4HZOs3S7AlS5E49T4xo15IS%2BJZvY2sXUZkRZipMSLFh3seqDxCoacvu4fafqqAmY3EC%2FIIbCcGkjHUKZZHpAWc2RqNbRG%2FI7mmxEF6obI25MPaNnL0GOqUBHRUf9G%2Fs1Q96Yorp9hrvOw6M36XutuuDHTLUOQuAmbeRfc9Ek3Cui7MzCiQ7FiwagL7d%2FG0hGqwTAG%2BkIsyuMmfThgZ8f1KA4OlVwHQPlXEHjeVlTxb1uw1Bok%2Fof%2FkJIAiIH%2FYZzUnojjx%2BTcqxrsih8zEMOf9K9ib6tVljmKZ5Qvibr9LKTBqdtKFQG7YOIqnwRUrCQd1LIPPypLbJXL8hx1hq&X-Amz-Signature=9742e7aa116ab0486e16e66eac6d5dc2f8372ccd4283db446bd709000545f6d1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGDJ36F7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCez57XQjsio0mofLZ46dSeVl9idJ9QJY8BleV48RxamQIgMK1z3Ey4sky5zDPWDatWZgB3HiOYeTCFEfV64vLYqAQqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKNKgBl9UI%2FUDidRiyrcA%2FtnFm3ZtCp3sFvecAf7IeloXrsNdQZWmwmjROAhLa9t17I7VRBPsdGfIK0ng3m4fUyuZRzs7IHcFWa6bdvdqt%2Fe2%2FX5vExvFMYSav%2Bu7vkUwuXwXVJrOTCS8ElSToFUjWhjG3WhSBkX8kvbv6ngQYwQYQcwMCeykMTqsJwmKtGbJJ1tWgfmp4wlJ%2F%2BS66HE6oxRucuslTK6dfAgsECiBFyqhfl6eWEl7ZOQneIeUZ0j%2Bfs5yKL43eA1xj%2FzGrVxWya1HtaR7g5HYYelZ4zNrFbq1Z%2BGZvqPt3hiy6vIxuT%2BCny3vJMlDI2GyVs%2BGPtk5%2F%2FXHyO6yI8zF%2BoM2chpnvMkOJ9c7lTJwjvUbvX6xnsLhZEj4eESdoJACwB%2BuG8ExEZFCLbkMXLn72FCEaqPQmazMOf0k0z%2FQkAJTQAKOL4OS5VesQxOJmyjE%2BO%2BeuRxGOyyQ7bVDyGa3EEHbb%2FLCtZsq7HPI%2Fg%2FaYORODgKY2vRHw8aqLdcf91dL56BW1eWFfZJv5USvC%2Bvw1IuR4HZOs3S7AlS5E49T4xo15IS%2BJZvY2sXUZkRZipMSLFh3seqDxCoacvu4fafqqAmY3EC%2FIIbCcGkjHUKZZHpAWc2RqNbRG%2FI7mmxEF6obI25MPaNnL0GOqUBHRUf9G%2Fs1Q96Yorp9hrvOw6M36XutuuDHTLUOQuAmbeRfc9Ek3Cui7MzCiQ7FiwagL7d%2FG0hGqwTAG%2BkIsyuMmfThgZ8f1KA4OlVwHQPlXEHjeVlTxb1uw1Bok%2Fof%2FkJIAiIH%2FYZzUnojjx%2BTcqxrsih8zEMOf9K9ib6tVljmKZ5Qvibr9LKTBqdtKFQG7YOIqnwRUrCQd1LIPPypLbJXL8hx1hq&X-Amz-Signature=ae869af6b83585d1649d34b4bd23a4e0b719d3abc6eedb728fdba9532629d829&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGDJ36F7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCez57XQjsio0mofLZ46dSeVl9idJ9QJY8BleV48RxamQIgMK1z3Ey4sky5zDPWDatWZgB3HiOYeTCFEfV64vLYqAQqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKNKgBl9UI%2FUDidRiyrcA%2FtnFm3ZtCp3sFvecAf7IeloXrsNdQZWmwmjROAhLa9t17I7VRBPsdGfIK0ng3m4fUyuZRzs7IHcFWa6bdvdqt%2Fe2%2FX5vExvFMYSav%2Bu7vkUwuXwXVJrOTCS8ElSToFUjWhjG3WhSBkX8kvbv6ngQYwQYQcwMCeykMTqsJwmKtGbJJ1tWgfmp4wlJ%2F%2BS66HE6oxRucuslTK6dfAgsECiBFyqhfl6eWEl7ZOQneIeUZ0j%2Bfs5yKL43eA1xj%2FzGrVxWya1HtaR7g5HYYelZ4zNrFbq1Z%2BGZvqPt3hiy6vIxuT%2BCny3vJMlDI2GyVs%2BGPtk5%2F%2FXHyO6yI8zF%2BoM2chpnvMkOJ9c7lTJwjvUbvX6xnsLhZEj4eESdoJACwB%2BuG8ExEZFCLbkMXLn72FCEaqPQmazMOf0k0z%2FQkAJTQAKOL4OS5VesQxOJmyjE%2BO%2BeuRxGOyyQ7bVDyGa3EEHbb%2FLCtZsq7HPI%2Fg%2FaYORODgKY2vRHw8aqLdcf91dL56BW1eWFfZJv5USvC%2Bvw1IuR4HZOs3S7AlS5E49T4xo15IS%2BJZvY2sXUZkRZipMSLFh3seqDxCoacvu4fafqqAmY3EC%2FIIbCcGkjHUKZZHpAWc2RqNbRG%2FI7mmxEF6obI25MPaNnL0GOqUBHRUf9G%2Fs1Q96Yorp9hrvOw6M36XutuuDHTLUOQuAmbeRfc9Ek3Cui7MzCiQ7FiwagL7d%2FG0hGqwTAG%2BkIsyuMmfThgZ8f1KA4OlVwHQPlXEHjeVlTxb1uw1Bok%2Fof%2FkJIAiIH%2FYZzUnojjx%2BTcqxrsih8zEMOf9K9ib6tVljmKZ5Qvibr9LKTBqdtKFQG7YOIqnwRUrCQd1LIPPypLbJXL8hx1hq&X-Amz-Signature=e19cc58a0bf5d2fa823f20f6553bc7c598f0691f8072176363765f31ac80eff1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGDJ36F7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCez57XQjsio0mofLZ46dSeVl9idJ9QJY8BleV48RxamQIgMK1z3Ey4sky5zDPWDatWZgB3HiOYeTCFEfV64vLYqAQqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKNKgBl9UI%2FUDidRiyrcA%2FtnFm3ZtCp3sFvecAf7IeloXrsNdQZWmwmjROAhLa9t17I7VRBPsdGfIK0ng3m4fUyuZRzs7IHcFWa6bdvdqt%2Fe2%2FX5vExvFMYSav%2Bu7vkUwuXwXVJrOTCS8ElSToFUjWhjG3WhSBkX8kvbv6ngQYwQYQcwMCeykMTqsJwmKtGbJJ1tWgfmp4wlJ%2F%2BS66HE6oxRucuslTK6dfAgsECiBFyqhfl6eWEl7ZOQneIeUZ0j%2Bfs5yKL43eA1xj%2FzGrVxWya1HtaR7g5HYYelZ4zNrFbq1Z%2BGZvqPt3hiy6vIxuT%2BCny3vJMlDI2GyVs%2BGPtk5%2F%2FXHyO6yI8zF%2BoM2chpnvMkOJ9c7lTJwjvUbvX6xnsLhZEj4eESdoJACwB%2BuG8ExEZFCLbkMXLn72FCEaqPQmazMOf0k0z%2FQkAJTQAKOL4OS5VesQxOJmyjE%2BO%2BeuRxGOyyQ7bVDyGa3EEHbb%2FLCtZsq7HPI%2Fg%2FaYORODgKY2vRHw8aqLdcf91dL56BW1eWFfZJv5USvC%2Bvw1IuR4HZOs3S7AlS5E49T4xo15IS%2BJZvY2sXUZkRZipMSLFh3seqDxCoacvu4fafqqAmY3EC%2FIIbCcGkjHUKZZHpAWc2RqNbRG%2FI7mmxEF6obI25MPaNnL0GOqUBHRUf9G%2Fs1Q96Yorp9hrvOw6M36XutuuDHTLUOQuAmbeRfc9Ek3Cui7MzCiQ7FiwagL7d%2FG0hGqwTAG%2BkIsyuMmfThgZ8f1KA4OlVwHQPlXEHjeVlTxb1uw1Bok%2Fof%2FkJIAiIH%2FYZzUnojjx%2BTcqxrsih8zEMOf9K9ib6tVljmKZ5Qvibr9LKTBqdtKFQG7YOIqnwRUrCQd1LIPPypLbJXL8hx1hq&X-Amz-Signature=a375a0498621b046909a26e5eb2e4113bb1c18d4ecb40bf70b90833eeb175705&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGDJ36F7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCez57XQjsio0mofLZ46dSeVl9idJ9QJY8BleV48RxamQIgMK1z3Ey4sky5zDPWDatWZgB3HiOYeTCFEfV64vLYqAQqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKNKgBl9UI%2FUDidRiyrcA%2FtnFm3ZtCp3sFvecAf7IeloXrsNdQZWmwmjROAhLa9t17I7VRBPsdGfIK0ng3m4fUyuZRzs7IHcFWa6bdvdqt%2Fe2%2FX5vExvFMYSav%2Bu7vkUwuXwXVJrOTCS8ElSToFUjWhjG3WhSBkX8kvbv6ngQYwQYQcwMCeykMTqsJwmKtGbJJ1tWgfmp4wlJ%2F%2BS66HE6oxRucuslTK6dfAgsECiBFyqhfl6eWEl7ZOQneIeUZ0j%2Bfs5yKL43eA1xj%2FzGrVxWya1HtaR7g5HYYelZ4zNrFbq1Z%2BGZvqPt3hiy6vIxuT%2BCny3vJMlDI2GyVs%2BGPtk5%2F%2FXHyO6yI8zF%2BoM2chpnvMkOJ9c7lTJwjvUbvX6xnsLhZEj4eESdoJACwB%2BuG8ExEZFCLbkMXLn72FCEaqPQmazMOf0k0z%2FQkAJTQAKOL4OS5VesQxOJmyjE%2BO%2BeuRxGOyyQ7bVDyGa3EEHbb%2FLCtZsq7HPI%2Fg%2FaYORODgKY2vRHw8aqLdcf91dL56BW1eWFfZJv5USvC%2Bvw1IuR4HZOs3S7AlS5E49T4xo15IS%2BJZvY2sXUZkRZipMSLFh3seqDxCoacvu4fafqqAmY3EC%2FIIbCcGkjHUKZZHpAWc2RqNbRG%2FI7mmxEF6obI25MPaNnL0GOqUBHRUf9G%2Fs1Q96Yorp9hrvOw6M36XutuuDHTLUOQuAmbeRfc9Ek3Cui7MzCiQ7FiwagL7d%2FG0hGqwTAG%2BkIsyuMmfThgZ8f1KA4OlVwHQPlXEHjeVlTxb1uw1Bok%2Fof%2FkJIAiIH%2FYZzUnojjx%2BTcqxrsih8zEMOf9K9ib6tVljmKZ5Qvibr9LKTBqdtKFQG7YOIqnwRUrCQd1LIPPypLbJXL8hx1hq&X-Amz-Signature=e1c7c84db82c60705a62a330607c0591cff9cc13c456abb9a19b896d41a3de2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGDJ36F7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCez57XQjsio0mofLZ46dSeVl9idJ9QJY8BleV48RxamQIgMK1z3Ey4sky5zDPWDatWZgB3HiOYeTCFEfV64vLYqAQqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKNKgBl9UI%2FUDidRiyrcA%2FtnFm3ZtCp3sFvecAf7IeloXrsNdQZWmwmjROAhLa9t17I7VRBPsdGfIK0ng3m4fUyuZRzs7IHcFWa6bdvdqt%2Fe2%2FX5vExvFMYSav%2Bu7vkUwuXwXVJrOTCS8ElSToFUjWhjG3WhSBkX8kvbv6ngQYwQYQcwMCeykMTqsJwmKtGbJJ1tWgfmp4wlJ%2F%2BS66HE6oxRucuslTK6dfAgsECiBFyqhfl6eWEl7ZOQneIeUZ0j%2Bfs5yKL43eA1xj%2FzGrVxWya1HtaR7g5HYYelZ4zNrFbq1Z%2BGZvqPt3hiy6vIxuT%2BCny3vJMlDI2GyVs%2BGPtk5%2F%2FXHyO6yI8zF%2BoM2chpnvMkOJ9c7lTJwjvUbvX6xnsLhZEj4eESdoJACwB%2BuG8ExEZFCLbkMXLn72FCEaqPQmazMOf0k0z%2FQkAJTQAKOL4OS5VesQxOJmyjE%2BO%2BeuRxGOyyQ7bVDyGa3EEHbb%2FLCtZsq7HPI%2Fg%2FaYORODgKY2vRHw8aqLdcf91dL56BW1eWFfZJv5USvC%2Bvw1IuR4HZOs3S7AlS5E49T4xo15IS%2BJZvY2sXUZkRZipMSLFh3seqDxCoacvu4fafqqAmY3EC%2FIIbCcGkjHUKZZHpAWc2RqNbRG%2FI7mmxEF6obI25MPaNnL0GOqUBHRUf9G%2Fs1Q96Yorp9hrvOw6M36XutuuDHTLUOQuAmbeRfc9Ek3Cui7MzCiQ7FiwagL7d%2FG0hGqwTAG%2BkIsyuMmfThgZ8f1KA4OlVwHQPlXEHjeVlTxb1uw1Bok%2Fof%2FkJIAiIH%2FYZzUnojjx%2BTcqxrsih8zEMOf9K9ib6tVljmKZ5Qvibr9LKTBqdtKFQG7YOIqnwRUrCQd1LIPPypLbJXL8hx1hq&X-Amz-Signature=12b1ac65715ce7ef9268fa40beaf406efb1d2099d2c58c7b2ab26f0eb2ebdbda&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BVLV23Z%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCnqqRa3pLqEuUEJrPmK%2BJIN17hwxZjjRKEekErc2DN1gIhANBmINUN8Kw%2Ffn7Y7e60q34rMaXWjlxGW53beqpajq8%2FKogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgythUdpS7a6FlN0xuoq3AP1NcWxf%2FrLC%2FmPWzbZoq06NKUZsd9KYneWk9zQhBVsQ0wMcbJbh7vtCG69e7Hse4L4IQGTuwoYW75u6D9GeK3vF48JUASSfGbA%2BPtnU5SVpzHfY1ld%2FEYHiFS8AFo5NTR5%2BFe04aRa2xMMx6b2DP7pQy4Ovdr9BTeyqc0IzLe7gPy6WP9nnmHwZ9gHUPznhczkrGfEqXwmObQ1nnHI5j0Apig1mlh%2BaWiAQBdRkP5lYxAwCLvUbuPi1%2Ftbw3nnawOuLmkidyY%2F9UZNjD%2BFtad6MtZWv1VhEZjxlxnw8SFDFJeXtGFNE4MrEwNPwS0YwvHf%2B54%2Fr6S0pf8w6AHIODIjZ1Wkkv02OBb2S%2B72JpXaeFf%2Fk0%2B9cfUsGkAI9SyQat%2BCRU8qpXH0V9KJQUXnNdxtERl8rJyPFDkNGWSRh8ta%2FEXXW2kCQ8P%2BBQOszBq%2Fud5ui6PJRrgyWkn%2FL5VP7N7t2ZC9N%2BXzKFpaey7MiSNNZxQIta4SXROU7yCsadCucAy9oizHdF4CV63VyA0mz6SHk2eT8ckZ3D33%2FJGDg%2BT%2BL3KfPrCGwQ2rP9El6SSqWBanZdWsq%2BCJPGRtANUdQLfV90C6rdUwR0rWZ5%2FP5IoAKbVQx0ixB9BrvuZBAjCQjpy9BjqkAT6c1DUPj11xqKSKt6xAltkWGx2lVhOiH94fnNNBqYjBGH97LAB6oYeMjh3D0R3PmMMBPF%2BtfJ4NK%2FJ%2Fyba7U4NJKjkTCYxG7HTc24SUFuhBK%2BHtNRSPZWX9QWZE6fJ6WNMFiNT%2Bt1DsBIoHHeMzHt389vAyVUpKZ%2FQiuYGz9Uhi3chp9wCdPFRi5c4HFfUZhmCfoCVF%2FiiVc4tpLxAnyrWFMlzV&X-Amz-Signature=71e8c018b4860aa1bc4e88f28368c43ca5c8e3660870070de8e05e042a8f6234&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BVLV23Z%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCnqqRa3pLqEuUEJrPmK%2BJIN17hwxZjjRKEekErc2DN1gIhANBmINUN8Kw%2Ffn7Y7e60q34rMaXWjlxGW53beqpajq8%2FKogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgythUdpS7a6FlN0xuoq3AP1NcWxf%2FrLC%2FmPWzbZoq06NKUZsd9KYneWk9zQhBVsQ0wMcbJbh7vtCG69e7Hse4L4IQGTuwoYW75u6D9GeK3vF48JUASSfGbA%2BPtnU5SVpzHfY1ld%2FEYHiFS8AFo5NTR5%2BFe04aRa2xMMx6b2DP7pQy4Ovdr9BTeyqc0IzLe7gPy6WP9nnmHwZ9gHUPznhczkrGfEqXwmObQ1nnHI5j0Apig1mlh%2BaWiAQBdRkP5lYxAwCLvUbuPi1%2Ftbw3nnawOuLmkidyY%2F9UZNjD%2BFtad6MtZWv1VhEZjxlxnw8SFDFJeXtGFNE4MrEwNPwS0YwvHf%2B54%2Fr6S0pf8w6AHIODIjZ1Wkkv02OBb2S%2B72JpXaeFf%2Fk0%2B9cfUsGkAI9SyQat%2BCRU8qpXH0V9KJQUXnNdxtERl8rJyPFDkNGWSRh8ta%2FEXXW2kCQ8P%2BBQOszBq%2Fud5ui6PJRrgyWkn%2FL5VP7N7t2ZC9N%2BXzKFpaey7MiSNNZxQIta4SXROU7yCsadCucAy9oizHdF4CV63VyA0mz6SHk2eT8ckZ3D33%2FJGDg%2BT%2BL3KfPrCGwQ2rP9El6SSqWBanZdWsq%2BCJPGRtANUdQLfV90C6rdUwR0rWZ5%2FP5IoAKbVQx0ixB9BrvuZBAjCQjpy9BjqkAT6c1DUPj11xqKSKt6xAltkWGx2lVhOiH94fnNNBqYjBGH97LAB6oYeMjh3D0R3PmMMBPF%2BtfJ4NK%2FJ%2Fyba7U4NJKjkTCYxG7HTc24SUFuhBK%2BHtNRSPZWX9QWZE6fJ6WNMFiNT%2Bt1DsBIoHHeMzHt389vAyVUpKZ%2FQiuYGz9Uhi3chp9wCdPFRi5c4HFfUZhmCfoCVF%2FiiVc4tpLxAnyrWFMlzV&X-Amz-Signature=1dabc1a9dd3a860c103997c0c268a01196d6eeb808f8b9e51a9a77e260f2382e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
