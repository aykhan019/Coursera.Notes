

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CBRNZJ3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCk1Mhfx9tS6Yd2eIciYyAzt%2BMf%2FwRXmkVVJOMG7Be%2BRgIgbMSydHYMzy%2BqFPgJSoN6B%2BDrj0zTna%2BR%2FPkgqbkszLgq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDFVUW5X31vAxck63BircA%2F4ASJm%2BnjKqhMpKTZMlgVVNPXOQO0jWdI4zCEwQmmGESQDfMz68IXpAZVG5R1DCpWTkQET2VwWR8B4lmmoLCGGHnWXZ1EgcecStvrbDLrAV53AJCBaBprJP%2BcevPactQo5mxrVJjJ%2BLwUdpF4Aoi5BtypRtrgI5OW1XwXZTq5sCARBUmWzEz53lBSNbsHDPQeAu1MPhE%2FLCT1zJ9BUoIScq8zsQh2JskZ%2FzjQLQnqB%2FJzCP6emjsjWbFhV%2BKYQ0n97lBs1pW8Tv38hgDQe4K3%2BVW3SC%2B3pPgp0UfGqIMAQ%2FZ5iMAevZ1v00TaMzbU6OJviRUm7X2GKCWIfUf5uYo%2BY4n99FUVRTRlQKPQt8kGea78Qn9JPSsQPYQT%2BrKx%2BxHd5nCiB203C25CGO0kgi4ivVWpgdfGih%2BKSUqfR9qhBUPH1MY20CDv7uzDrZwK%2BQDpz3IeeWayfYF%2FKIK%2FQBb5YXZezbTX4Hrj2MxFZX9bNgTwdN123fZdD2zRhJmUUXz0VPto6AygYI8qBoJ7%2B1oNVeMhoFRLpbIG%2Fr9VECSswiel3iPTUHjaO%2FvdrCgYn2q%2B0%2FSlksjsckbxecoV%2FXam06INTQvVMpdmcZ%2BMDtLXUAw2HDE0vaEVbYIHtxMLnDkr0GOqUBTx014omZu506W9GFMly%2B4%2BvEOKCMl54zY5tO2ZaBNy1yMcHSz67xZhKrvj7Hmnvkl0uVKsooc2UwHcgqH2oUANe%2BffHn2huXZPEc2UFdCPTMk%2FK5qN0U%2FFYG1ZsKth6XNrQVXElLwJPgdPJ2WIfGl8uJn2Defl0FEueTUuCqFx4GFtbT5%2FBVX7QusoED%2FGS3oFaYtvt0F6LOaZdHuttgjP2uWyIH&X-Amz-Signature=62e7e21ca033d7db2574a8d6ff172c9165b612598bda5a3996a0b4876ae2eb5d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CBRNZJ3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCk1Mhfx9tS6Yd2eIciYyAzt%2BMf%2FwRXmkVVJOMG7Be%2BRgIgbMSydHYMzy%2BqFPgJSoN6B%2BDrj0zTna%2BR%2FPkgqbkszLgq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDFVUW5X31vAxck63BircA%2F4ASJm%2BnjKqhMpKTZMlgVVNPXOQO0jWdI4zCEwQmmGESQDfMz68IXpAZVG5R1DCpWTkQET2VwWR8B4lmmoLCGGHnWXZ1EgcecStvrbDLrAV53AJCBaBprJP%2BcevPactQo5mxrVJjJ%2BLwUdpF4Aoi5BtypRtrgI5OW1XwXZTq5sCARBUmWzEz53lBSNbsHDPQeAu1MPhE%2FLCT1zJ9BUoIScq8zsQh2JskZ%2FzjQLQnqB%2FJzCP6emjsjWbFhV%2BKYQ0n97lBs1pW8Tv38hgDQe4K3%2BVW3SC%2B3pPgp0UfGqIMAQ%2FZ5iMAevZ1v00TaMzbU6OJviRUm7X2GKCWIfUf5uYo%2BY4n99FUVRTRlQKPQt8kGea78Qn9JPSsQPYQT%2BrKx%2BxHd5nCiB203C25CGO0kgi4ivVWpgdfGih%2BKSUqfR9qhBUPH1MY20CDv7uzDrZwK%2BQDpz3IeeWayfYF%2FKIK%2FQBb5YXZezbTX4Hrj2MxFZX9bNgTwdN123fZdD2zRhJmUUXz0VPto6AygYI8qBoJ7%2B1oNVeMhoFRLpbIG%2Fr9VECSswiel3iPTUHjaO%2FvdrCgYn2q%2B0%2FSlksjsckbxecoV%2FXam06INTQvVMpdmcZ%2BMDtLXUAw2HDE0vaEVbYIHtxMLnDkr0GOqUBTx014omZu506W9GFMly%2B4%2BvEOKCMl54zY5tO2ZaBNy1yMcHSz67xZhKrvj7Hmnvkl0uVKsooc2UwHcgqH2oUANe%2BffHn2huXZPEc2UFdCPTMk%2FK5qN0U%2FFYG1ZsKth6XNrQVXElLwJPgdPJ2WIfGl8uJn2Defl0FEueTUuCqFx4GFtbT5%2FBVX7QusoED%2FGS3oFaYtvt0F6LOaZdHuttgjP2uWyIH&X-Amz-Signature=2348ddf0c7c8838678e681a849bac708359568654d629bbafa5f97a08dcf919b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CBRNZJ3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCk1Mhfx9tS6Yd2eIciYyAzt%2BMf%2FwRXmkVVJOMG7Be%2BRgIgbMSydHYMzy%2BqFPgJSoN6B%2BDrj0zTna%2BR%2FPkgqbkszLgq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDFVUW5X31vAxck63BircA%2F4ASJm%2BnjKqhMpKTZMlgVVNPXOQO0jWdI4zCEwQmmGESQDfMz68IXpAZVG5R1DCpWTkQET2VwWR8B4lmmoLCGGHnWXZ1EgcecStvrbDLrAV53AJCBaBprJP%2BcevPactQo5mxrVJjJ%2BLwUdpF4Aoi5BtypRtrgI5OW1XwXZTq5sCARBUmWzEz53lBSNbsHDPQeAu1MPhE%2FLCT1zJ9BUoIScq8zsQh2JskZ%2FzjQLQnqB%2FJzCP6emjsjWbFhV%2BKYQ0n97lBs1pW8Tv38hgDQe4K3%2BVW3SC%2B3pPgp0UfGqIMAQ%2FZ5iMAevZ1v00TaMzbU6OJviRUm7X2GKCWIfUf5uYo%2BY4n99FUVRTRlQKPQt8kGea78Qn9JPSsQPYQT%2BrKx%2BxHd5nCiB203C25CGO0kgi4ivVWpgdfGih%2BKSUqfR9qhBUPH1MY20CDv7uzDrZwK%2BQDpz3IeeWayfYF%2FKIK%2FQBb5YXZezbTX4Hrj2MxFZX9bNgTwdN123fZdD2zRhJmUUXz0VPto6AygYI8qBoJ7%2B1oNVeMhoFRLpbIG%2Fr9VECSswiel3iPTUHjaO%2FvdrCgYn2q%2B0%2FSlksjsckbxecoV%2FXam06INTQvVMpdmcZ%2BMDtLXUAw2HDE0vaEVbYIHtxMLnDkr0GOqUBTx014omZu506W9GFMly%2B4%2BvEOKCMl54zY5tO2ZaBNy1yMcHSz67xZhKrvj7Hmnvkl0uVKsooc2UwHcgqH2oUANe%2BffHn2huXZPEc2UFdCPTMk%2FK5qN0U%2FFYG1ZsKth6XNrQVXElLwJPgdPJ2WIfGl8uJn2Defl0FEueTUuCqFx4GFtbT5%2FBVX7QusoED%2FGS3oFaYtvt0F6LOaZdHuttgjP2uWyIH&X-Amz-Signature=9a3525de4ff2f3cb7b09515850c20224e1329dc43a738aca4f36aca87ce86b29&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CBRNZJ3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCk1Mhfx9tS6Yd2eIciYyAzt%2BMf%2FwRXmkVVJOMG7Be%2BRgIgbMSydHYMzy%2BqFPgJSoN6B%2BDrj0zTna%2BR%2FPkgqbkszLgq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDFVUW5X31vAxck63BircA%2F4ASJm%2BnjKqhMpKTZMlgVVNPXOQO0jWdI4zCEwQmmGESQDfMz68IXpAZVG5R1DCpWTkQET2VwWR8B4lmmoLCGGHnWXZ1EgcecStvrbDLrAV53AJCBaBprJP%2BcevPactQo5mxrVJjJ%2BLwUdpF4Aoi5BtypRtrgI5OW1XwXZTq5sCARBUmWzEz53lBSNbsHDPQeAu1MPhE%2FLCT1zJ9BUoIScq8zsQh2JskZ%2FzjQLQnqB%2FJzCP6emjsjWbFhV%2BKYQ0n97lBs1pW8Tv38hgDQe4K3%2BVW3SC%2B3pPgp0UfGqIMAQ%2FZ5iMAevZ1v00TaMzbU6OJviRUm7X2GKCWIfUf5uYo%2BY4n99FUVRTRlQKPQt8kGea78Qn9JPSsQPYQT%2BrKx%2BxHd5nCiB203C25CGO0kgi4ivVWpgdfGih%2BKSUqfR9qhBUPH1MY20CDv7uzDrZwK%2BQDpz3IeeWayfYF%2FKIK%2FQBb5YXZezbTX4Hrj2MxFZX9bNgTwdN123fZdD2zRhJmUUXz0VPto6AygYI8qBoJ7%2B1oNVeMhoFRLpbIG%2Fr9VECSswiel3iPTUHjaO%2FvdrCgYn2q%2B0%2FSlksjsckbxecoV%2FXam06INTQvVMpdmcZ%2BMDtLXUAw2HDE0vaEVbYIHtxMLnDkr0GOqUBTx014omZu506W9GFMly%2B4%2BvEOKCMl54zY5tO2ZaBNy1yMcHSz67xZhKrvj7Hmnvkl0uVKsooc2UwHcgqH2oUANe%2BffHn2huXZPEc2UFdCPTMk%2FK5qN0U%2FFYG1ZsKth6XNrQVXElLwJPgdPJ2WIfGl8uJn2Defl0FEueTUuCqFx4GFtbT5%2FBVX7QusoED%2FGS3oFaYtvt0F6LOaZdHuttgjP2uWyIH&X-Amz-Signature=aa5014b8d1bf20be0bfec939da18bb304bc7f0480a8a8bbb451b0758b647fc04&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CBRNZJ3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCk1Mhfx9tS6Yd2eIciYyAzt%2BMf%2FwRXmkVVJOMG7Be%2BRgIgbMSydHYMzy%2BqFPgJSoN6B%2BDrj0zTna%2BR%2FPkgqbkszLgq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDFVUW5X31vAxck63BircA%2F4ASJm%2BnjKqhMpKTZMlgVVNPXOQO0jWdI4zCEwQmmGESQDfMz68IXpAZVG5R1DCpWTkQET2VwWR8B4lmmoLCGGHnWXZ1EgcecStvrbDLrAV53AJCBaBprJP%2BcevPactQo5mxrVJjJ%2BLwUdpF4Aoi5BtypRtrgI5OW1XwXZTq5sCARBUmWzEz53lBSNbsHDPQeAu1MPhE%2FLCT1zJ9BUoIScq8zsQh2JskZ%2FzjQLQnqB%2FJzCP6emjsjWbFhV%2BKYQ0n97lBs1pW8Tv38hgDQe4K3%2BVW3SC%2B3pPgp0UfGqIMAQ%2FZ5iMAevZ1v00TaMzbU6OJviRUm7X2GKCWIfUf5uYo%2BY4n99FUVRTRlQKPQt8kGea78Qn9JPSsQPYQT%2BrKx%2BxHd5nCiB203C25CGO0kgi4ivVWpgdfGih%2BKSUqfR9qhBUPH1MY20CDv7uzDrZwK%2BQDpz3IeeWayfYF%2FKIK%2FQBb5YXZezbTX4Hrj2MxFZX9bNgTwdN123fZdD2zRhJmUUXz0VPto6AygYI8qBoJ7%2B1oNVeMhoFRLpbIG%2Fr9VECSswiel3iPTUHjaO%2FvdrCgYn2q%2B0%2FSlksjsckbxecoV%2FXam06INTQvVMpdmcZ%2BMDtLXUAw2HDE0vaEVbYIHtxMLnDkr0GOqUBTx014omZu506W9GFMly%2B4%2BvEOKCMl54zY5tO2ZaBNy1yMcHSz67xZhKrvj7Hmnvkl0uVKsooc2UwHcgqH2oUANe%2BffHn2huXZPEc2UFdCPTMk%2FK5qN0U%2FFYG1ZsKth6XNrQVXElLwJPgdPJ2WIfGl8uJn2Defl0FEueTUuCqFx4GFtbT5%2FBVX7QusoED%2FGS3oFaYtvt0F6LOaZdHuttgjP2uWyIH&X-Amz-Signature=305c488bf71ed5c0c1e16df88ddffb7b5abd6c7102b71bf7d917f757b37f27e9&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CBRNZJ3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCk1Mhfx9tS6Yd2eIciYyAzt%2BMf%2FwRXmkVVJOMG7Be%2BRgIgbMSydHYMzy%2BqFPgJSoN6B%2BDrj0zTna%2BR%2FPkgqbkszLgq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDFVUW5X31vAxck63BircA%2F4ASJm%2BnjKqhMpKTZMlgVVNPXOQO0jWdI4zCEwQmmGESQDfMz68IXpAZVG5R1DCpWTkQET2VwWR8B4lmmoLCGGHnWXZ1EgcecStvrbDLrAV53AJCBaBprJP%2BcevPactQo5mxrVJjJ%2BLwUdpF4Aoi5BtypRtrgI5OW1XwXZTq5sCARBUmWzEz53lBSNbsHDPQeAu1MPhE%2FLCT1zJ9BUoIScq8zsQh2JskZ%2FzjQLQnqB%2FJzCP6emjsjWbFhV%2BKYQ0n97lBs1pW8Tv38hgDQe4K3%2BVW3SC%2B3pPgp0UfGqIMAQ%2FZ5iMAevZ1v00TaMzbU6OJviRUm7X2GKCWIfUf5uYo%2BY4n99FUVRTRlQKPQt8kGea78Qn9JPSsQPYQT%2BrKx%2BxHd5nCiB203C25CGO0kgi4ivVWpgdfGih%2BKSUqfR9qhBUPH1MY20CDv7uzDrZwK%2BQDpz3IeeWayfYF%2FKIK%2FQBb5YXZezbTX4Hrj2MxFZX9bNgTwdN123fZdD2zRhJmUUXz0VPto6AygYI8qBoJ7%2B1oNVeMhoFRLpbIG%2Fr9VECSswiel3iPTUHjaO%2FvdrCgYn2q%2B0%2FSlksjsckbxecoV%2FXam06INTQvVMpdmcZ%2BMDtLXUAw2HDE0vaEVbYIHtxMLnDkr0GOqUBTx014omZu506W9GFMly%2B4%2BvEOKCMl54zY5tO2ZaBNy1yMcHSz67xZhKrvj7Hmnvkl0uVKsooc2UwHcgqH2oUANe%2BffHn2huXZPEc2UFdCPTMk%2FK5qN0U%2FFYG1ZsKth6XNrQVXElLwJPgdPJ2WIfGl8uJn2Defl0FEueTUuCqFx4GFtbT5%2FBVX7QusoED%2FGS3oFaYtvt0F6LOaZdHuttgjP2uWyIH&X-Amz-Signature=19e81fdb1fedafd844eca79e586421911e4d50fcca1c9ad0fe95233de1a51ab3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CBRNZJ3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCk1Mhfx9tS6Yd2eIciYyAzt%2BMf%2FwRXmkVVJOMG7Be%2BRgIgbMSydHYMzy%2BqFPgJSoN6B%2BDrj0zTna%2BR%2FPkgqbkszLgq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDFVUW5X31vAxck63BircA%2F4ASJm%2BnjKqhMpKTZMlgVVNPXOQO0jWdI4zCEwQmmGESQDfMz68IXpAZVG5R1DCpWTkQET2VwWR8B4lmmoLCGGHnWXZ1EgcecStvrbDLrAV53AJCBaBprJP%2BcevPactQo5mxrVJjJ%2BLwUdpF4Aoi5BtypRtrgI5OW1XwXZTq5sCARBUmWzEz53lBSNbsHDPQeAu1MPhE%2FLCT1zJ9BUoIScq8zsQh2JskZ%2FzjQLQnqB%2FJzCP6emjsjWbFhV%2BKYQ0n97lBs1pW8Tv38hgDQe4K3%2BVW3SC%2B3pPgp0UfGqIMAQ%2FZ5iMAevZ1v00TaMzbU6OJviRUm7X2GKCWIfUf5uYo%2BY4n99FUVRTRlQKPQt8kGea78Qn9JPSsQPYQT%2BrKx%2BxHd5nCiB203C25CGO0kgi4ivVWpgdfGih%2BKSUqfR9qhBUPH1MY20CDv7uzDrZwK%2BQDpz3IeeWayfYF%2FKIK%2FQBb5YXZezbTX4Hrj2MxFZX9bNgTwdN123fZdD2zRhJmUUXz0VPto6AygYI8qBoJ7%2B1oNVeMhoFRLpbIG%2Fr9VECSswiel3iPTUHjaO%2FvdrCgYn2q%2B0%2FSlksjsckbxecoV%2FXam06INTQvVMpdmcZ%2BMDtLXUAw2HDE0vaEVbYIHtxMLnDkr0GOqUBTx014omZu506W9GFMly%2B4%2BvEOKCMl54zY5tO2ZaBNy1yMcHSz67xZhKrvj7Hmnvkl0uVKsooc2UwHcgqH2oUANe%2BffHn2huXZPEc2UFdCPTMk%2FK5qN0U%2FFYG1ZsKth6XNrQVXElLwJPgdPJ2WIfGl8uJn2Defl0FEueTUuCqFx4GFtbT5%2FBVX7QusoED%2FGS3oFaYtvt0F6LOaZdHuttgjP2uWyIH&X-Amz-Signature=6a1978d16dbed98bdbb2c46d776a94f09e8b49fe292c72b098cde555fc8c4d04&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CBRNZJ3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCk1Mhfx9tS6Yd2eIciYyAzt%2BMf%2FwRXmkVVJOMG7Be%2BRgIgbMSydHYMzy%2BqFPgJSoN6B%2BDrj0zTna%2BR%2FPkgqbkszLgq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDFVUW5X31vAxck63BircA%2F4ASJm%2BnjKqhMpKTZMlgVVNPXOQO0jWdI4zCEwQmmGESQDfMz68IXpAZVG5R1DCpWTkQET2VwWR8B4lmmoLCGGHnWXZ1EgcecStvrbDLrAV53AJCBaBprJP%2BcevPactQo5mxrVJjJ%2BLwUdpF4Aoi5BtypRtrgI5OW1XwXZTq5sCARBUmWzEz53lBSNbsHDPQeAu1MPhE%2FLCT1zJ9BUoIScq8zsQh2JskZ%2FzjQLQnqB%2FJzCP6emjsjWbFhV%2BKYQ0n97lBs1pW8Tv38hgDQe4K3%2BVW3SC%2B3pPgp0UfGqIMAQ%2FZ5iMAevZ1v00TaMzbU6OJviRUm7X2GKCWIfUf5uYo%2BY4n99FUVRTRlQKPQt8kGea78Qn9JPSsQPYQT%2BrKx%2BxHd5nCiB203C25CGO0kgi4ivVWpgdfGih%2BKSUqfR9qhBUPH1MY20CDv7uzDrZwK%2BQDpz3IeeWayfYF%2FKIK%2FQBb5YXZezbTX4Hrj2MxFZX9bNgTwdN123fZdD2zRhJmUUXz0VPto6AygYI8qBoJ7%2B1oNVeMhoFRLpbIG%2Fr9VECSswiel3iPTUHjaO%2FvdrCgYn2q%2B0%2FSlksjsckbxecoV%2FXam06INTQvVMpdmcZ%2BMDtLXUAw2HDE0vaEVbYIHtxMLnDkr0GOqUBTx014omZu506W9GFMly%2B4%2BvEOKCMl54zY5tO2ZaBNy1yMcHSz67xZhKrvj7Hmnvkl0uVKsooc2UwHcgqH2oUANe%2BffHn2huXZPEc2UFdCPTMk%2FK5qN0U%2FFYG1ZsKth6XNrQVXElLwJPgdPJ2WIfGl8uJn2Defl0FEueTUuCqFx4GFtbT5%2FBVX7QusoED%2FGS3oFaYtvt0F6LOaZdHuttgjP2uWyIH&X-Amz-Signature=2b3bfcd70a804aeb3edbfc789b29773ed98e6515a11e4c00fda838cbdaa762e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CBRNZJ3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCk1Mhfx9tS6Yd2eIciYyAzt%2BMf%2FwRXmkVVJOMG7Be%2BRgIgbMSydHYMzy%2BqFPgJSoN6B%2BDrj0zTna%2BR%2FPkgqbkszLgq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDFVUW5X31vAxck63BircA%2F4ASJm%2BnjKqhMpKTZMlgVVNPXOQO0jWdI4zCEwQmmGESQDfMz68IXpAZVG5R1DCpWTkQET2VwWR8B4lmmoLCGGHnWXZ1EgcecStvrbDLrAV53AJCBaBprJP%2BcevPactQo5mxrVJjJ%2BLwUdpF4Aoi5BtypRtrgI5OW1XwXZTq5sCARBUmWzEz53lBSNbsHDPQeAu1MPhE%2FLCT1zJ9BUoIScq8zsQh2JskZ%2FzjQLQnqB%2FJzCP6emjsjWbFhV%2BKYQ0n97lBs1pW8Tv38hgDQe4K3%2BVW3SC%2B3pPgp0UfGqIMAQ%2FZ5iMAevZ1v00TaMzbU6OJviRUm7X2GKCWIfUf5uYo%2BY4n99FUVRTRlQKPQt8kGea78Qn9JPSsQPYQT%2BrKx%2BxHd5nCiB203C25CGO0kgi4ivVWpgdfGih%2BKSUqfR9qhBUPH1MY20CDv7uzDrZwK%2BQDpz3IeeWayfYF%2FKIK%2FQBb5YXZezbTX4Hrj2MxFZX9bNgTwdN123fZdD2zRhJmUUXz0VPto6AygYI8qBoJ7%2B1oNVeMhoFRLpbIG%2Fr9VECSswiel3iPTUHjaO%2FvdrCgYn2q%2B0%2FSlksjsckbxecoV%2FXam06INTQvVMpdmcZ%2BMDtLXUAw2HDE0vaEVbYIHtxMLnDkr0GOqUBTx014omZu506W9GFMly%2B4%2BvEOKCMl54zY5tO2ZaBNy1yMcHSz67xZhKrvj7Hmnvkl0uVKsooc2UwHcgqH2oUANe%2BffHn2huXZPEc2UFdCPTMk%2FK5qN0U%2FFYG1ZsKth6XNrQVXElLwJPgdPJ2WIfGl8uJn2Defl0FEueTUuCqFx4GFtbT5%2FBVX7QusoED%2FGS3oFaYtvt0F6LOaZdHuttgjP2uWyIH&X-Amz-Signature=471eea767d624975f9a68f365d7571a2906704d19034ca01ec2de68705b4c775&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U45LELAU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIFUmevdn3QkoHDzGK%2B%2BCCviQI%2BZBsulLiDxWFHr2fa9cAiEA9gQ4mUUD5cCJYDyQdLyaAQAjxtjfotDaABAS5IHkguwq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDDo%2B1pI3eX%2FzwPN%2BJircA0zL5HOwyiEGjw6yAXIya9v2q2e8FKbP02Got87YdndMl%2Fc7Url5GnUtLIJSvaiM4mOWl%2BCpX%2ByvAQKqa4HyjKoqwWyC3jYWbNdBtv12omC0hN71pyD561MProOx4e2cpBiZawZLBhrMQ1IXsGOxvGi%2FgWnyjlPz7aYB8y82N%2FuJp8IWKJdcagoNOlFvX%2FQKi%2BmIkStAlusfYvKFzwVVVxZ0IWoDJzl7XCN4r9CAQQuD8Uh10XF4Q82OYMmyld%2BJbMKC6vtEXCR27wtVj7xYFkwB51gRV6qYzzKYtAav79F2%2FJ7YIT7tcaHfl%2Fle4N16N6imgB1KeyZfoRVHUHQQiYCSmjwI%2BN%2BqueMyW4mL7%2FBljvP0HplEyc1ToXNyNhPrUKC9NkPCZvz%2Fvi1gzuEWgZ5PtyZE6%2FC0pqs%2FFC5mq9%2FRtmOVr6kjNSoIoNvNic4PvIWahEKpPBrX9qQ16i%2B7RZdf2gLXxqXC2ChOItk2Q9yAoZbnCWsYyplEmlDopJtucuF6sFC3amw%2FTR5vzrE%2Fd2UT1uZekVXwQNVEXu2kUAgicH98VFjlic9zCh0RDSi0qfGkkBSNFdIJXqTTuNjVSD%2FmXo0hOsjHN6Wjwdo2WvQEOmvQ088dRztBbafzMMLDkr0GOqUBzzfnZ8MuesZwpOWkkgtwotDky9llXGCi1WkQQXk7M05AfWsNxH%2FIg0sK0Lf60oWNrSPZV%2FlLA2a8hnR5FOfROlBdYjhnr7Y7cL8EZmUwwghr5W7S3J36LX6n9NRkB7JJSI3ZVtRt30Ki7NW5LVVIdl%2FTMcCmXmprOmT1RKUGnVQKoBSliPe7t4ndpR%2Fgnjx3GBWEbH6CLyPPIQhLk%2BRzNRizWiug&X-Amz-Signature=898cd93d991163f22e4fed94a4707c210447768cfdb4fb786b77b94a1c4984e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U45LELAU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIFUmevdn3QkoHDzGK%2B%2BCCviQI%2BZBsulLiDxWFHr2fa9cAiEA9gQ4mUUD5cCJYDyQdLyaAQAjxtjfotDaABAS5IHkguwq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDDo%2B1pI3eX%2FzwPN%2BJircA0zL5HOwyiEGjw6yAXIya9v2q2e8FKbP02Got87YdndMl%2Fc7Url5GnUtLIJSvaiM4mOWl%2BCpX%2ByvAQKqa4HyjKoqwWyC3jYWbNdBtv12omC0hN71pyD561MProOx4e2cpBiZawZLBhrMQ1IXsGOxvGi%2FgWnyjlPz7aYB8y82N%2FuJp8IWKJdcagoNOlFvX%2FQKi%2BmIkStAlusfYvKFzwVVVxZ0IWoDJzl7XCN4r9CAQQuD8Uh10XF4Q82OYMmyld%2BJbMKC6vtEXCR27wtVj7xYFkwB51gRV6qYzzKYtAav79F2%2FJ7YIT7tcaHfl%2Fle4N16N6imgB1KeyZfoRVHUHQQiYCSmjwI%2BN%2BqueMyW4mL7%2FBljvP0HplEyc1ToXNyNhPrUKC9NkPCZvz%2Fvi1gzuEWgZ5PtyZE6%2FC0pqs%2FFC5mq9%2FRtmOVr6kjNSoIoNvNic4PvIWahEKpPBrX9qQ16i%2B7RZdf2gLXxqXC2ChOItk2Q9yAoZbnCWsYyplEmlDopJtucuF6sFC3amw%2FTR5vzrE%2Fd2UT1uZekVXwQNVEXu2kUAgicH98VFjlic9zCh0RDSi0qfGkkBSNFdIJXqTTuNjVSD%2FmXo0hOsjHN6Wjwdo2WvQEOmvQ088dRztBbafzMMLDkr0GOqUBzzfnZ8MuesZwpOWkkgtwotDky9llXGCi1WkQQXk7M05AfWsNxH%2FIg0sK0Lf60oWNrSPZV%2FlLA2a8hnR5FOfROlBdYjhnr7Y7cL8EZmUwwghr5W7S3J36LX6n9NRkB7JJSI3ZVtRt30Ki7NW5LVVIdl%2FTMcCmXmprOmT1RKUGnVQKoBSliPe7t4ndpR%2Fgnjx3GBWEbH6CLyPPIQhLk%2BRzNRizWiug&X-Amz-Signature=1a18a80b714a4d721e50d8799d45966a1816f44dfe860f432143b52a843079c7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
