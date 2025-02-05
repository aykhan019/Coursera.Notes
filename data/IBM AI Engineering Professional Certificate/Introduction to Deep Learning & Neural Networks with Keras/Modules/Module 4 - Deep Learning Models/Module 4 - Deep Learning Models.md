

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTZXGOI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCO7nme09Ntpkt2bR9FernoNuhrIELX9WSQPIGjh03t5QIgVO%2FMe71%2Bo0MetM54XTJX%2FLYH%2B2y3Wq46bwXwvcvZ28Iq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBirdWrHTJnXSE9ysyrcAy7sODWE4NSLeGVCtDd9Ri2MYaTstKkap3nTVphkmBC6nVQyaoFE5dJUReAp2tI9fcfLgA%2BPKmTzfyqUEBRXmX9DVrxq7fiuOJrrVviA37Ft3%2FQmEy%2FXmdIhrb%2BfyAeKbJTeQqTw7PTS8fzqb3Gl2R1qPCJyesmQQ4D3eioSkK58pgPQLUPl79VwhGQgC%2BEOpV12%2BswRRkE1bW92ExHi2%2FCtZ51SgmF95Ywurhq4x33zBDX9z27lHmfVscrClI8EgFxro30inOw3ikazBMz94iA5nHFew8ApmE1P5h63nsITQy4voyoQ1wTcFRRADYuJUAcrW3wKDKv18TnOorE41LQrIxhPaQtH3R5MxdwVq0uemLiopW6M9wLEw7yVS6ueLGiK%2FWsS%2BfNRT5Oh%2FUTn1n7FFZCGdpzIwi6c0MCUnJ0Mlxk%2B77mr9rgVBH2%2FLZAPcuJnCIoFt%2FBPsPnMin%2FjuRKRKHW%2Be3fylnmwtMPMSKeEv0kd0OAiWO3lEDrJr01P8yvjB9Basd7Fpgn2HHQS15qc2PboBSrUcLQyugWuUswaNrNvlu6jLXWEMQIHbaXjMvjXW33dt8k98gQOohD0PP9qDonqpw0C6Gdj7kbhmHh9oR6j5DRGbMjmNbnTMK26jr0GOqUBQz6jTv8K%2FBoVcYLWTQf2KkeceunjiTSmICfZEvMZ5UCGWOcviquWkPw7b%2BTnO2CHzavf%2BssvzdT4yo0a9jWXysxNg2BXBsh6Ir%2BjF%2B8x5iCExh%2BQfJnFhCnNUDtc9%2B10Yxs13ILSAmaBFPuhPUJn2KHwrQv06LtIi72UjE2bTuTY2ViJGkuIOcCv%2BsAcmm8NFAebvIruWJtfrKDMp%2Fyofphao71h&X-Amz-Signature=449eb52bc37de391a549c023649b5612d7a642233b5c9505e18b74f87d2967b4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTZXGOI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCO7nme09Ntpkt2bR9FernoNuhrIELX9WSQPIGjh03t5QIgVO%2FMe71%2Bo0MetM54XTJX%2FLYH%2B2y3Wq46bwXwvcvZ28Iq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBirdWrHTJnXSE9ysyrcAy7sODWE4NSLeGVCtDd9Ri2MYaTstKkap3nTVphkmBC6nVQyaoFE5dJUReAp2tI9fcfLgA%2BPKmTzfyqUEBRXmX9DVrxq7fiuOJrrVviA37Ft3%2FQmEy%2FXmdIhrb%2BfyAeKbJTeQqTw7PTS8fzqb3Gl2R1qPCJyesmQQ4D3eioSkK58pgPQLUPl79VwhGQgC%2BEOpV12%2BswRRkE1bW92ExHi2%2FCtZ51SgmF95Ywurhq4x33zBDX9z27lHmfVscrClI8EgFxro30inOw3ikazBMz94iA5nHFew8ApmE1P5h63nsITQy4voyoQ1wTcFRRADYuJUAcrW3wKDKv18TnOorE41LQrIxhPaQtH3R5MxdwVq0uemLiopW6M9wLEw7yVS6ueLGiK%2FWsS%2BfNRT5Oh%2FUTn1n7FFZCGdpzIwi6c0MCUnJ0Mlxk%2B77mr9rgVBH2%2FLZAPcuJnCIoFt%2FBPsPnMin%2FjuRKRKHW%2Be3fylnmwtMPMSKeEv0kd0OAiWO3lEDrJr01P8yvjB9Basd7Fpgn2HHQS15qc2PboBSrUcLQyugWuUswaNrNvlu6jLXWEMQIHbaXjMvjXW33dt8k98gQOohD0PP9qDonqpw0C6Gdj7kbhmHh9oR6j5DRGbMjmNbnTMK26jr0GOqUBQz6jTv8K%2FBoVcYLWTQf2KkeceunjiTSmICfZEvMZ5UCGWOcviquWkPw7b%2BTnO2CHzavf%2BssvzdT4yo0a9jWXysxNg2BXBsh6Ir%2BjF%2B8x5iCExh%2BQfJnFhCnNUDtc9%2B10Yxs13ILSAmaBFPuhPUJn2KHwrQv06LtIi72UjE2bTuTY2ViJGkuIOcCv%2BsAcmm8NFAebvIruWJtfrKDMp%2Fyofphao71h&X-Amz-Signature=be9f2a87b030c804837ce8e5b03cf2d1368b5e4e366ac8e49db9311a66a5bb5b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTZXGOI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCO7nme09Ntpkt2bR9FernoNuhrIELX9WSQPIGjh03t5QIgVO%2FMe71%2Bo0MetM54XTJX%2FLYH%2B2y3Wq46bwXwvcvZ28Iq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBirdWrHTJnXSE9ysyrcAy7sODWE4NSLeGVCtDd9Ri2MYaTstKkap3nTVphkmBC6nVQyaoFE5dJUReAp2tI9fcfLgA%2BPKmTzfyqUEBRXmX9DVrxq7fiuOJrrVviA37Ft3%2FQmEy%2FXmdIhrb%2BfyAeKbJTeQqTw7PTS8fzqb3Gl2R1qPCJyesmQQ4D3eioSkK58pgPQLUPl79VwhGQgC%2BEOpV12%2BswRRkE1bW92ExHi2%2FCtZ51SgmF95Ywurhq4x33zBDX9z27lHmfVscrClI8EgFxro30inOw3ikazBMz94iA5nHFew8ApmE1P5h63nsITQy4voyoQ1wTcFRRADYuJUAcrW3wKDKv18TnOorE41LQrIxhPaQtH3R5MxdwVq0uemLiopW6M9wLEw7yVS6ueLGiK%2FWsS%2BfNRT5Oh%2FUTn1n7FFZCGdpzIwi6c0MCUnJ0Mlxk%2B77mr9rgVBH2%2FLZAPcuJnCIoFt%2FBPsPnMin%2FjuRKRKHW%2Be3fylnmwtMPMSKeEv0kd0OAiWO3lEDrJr01P8yvjB9Basd7Fpgn2HHQS15qc2PboBSrUcLQyugWuUswaNrNvlu6jLXWEMQIHbaXjMvjXW33dt8k98gQOohD0PP9qDonqpw0C6Gdj7kbhmHh9oR6j5DRGbMjmNbnTMK26jr0GOqUBQz6jTv8K%2FBoVcYLWTQf2KkeceunjiTSmICfZEvMZ5UCGWOcviquWkPw7b%2BTnO2CHzavf%2BssvzdT4yo0a9jWXysxNg2BXBsh6Ir%2BjF%2B8x5iCExh%2BQfJnFhCnNUDtc9%2B10Yxs13ILSAmaBFPuhPUJn2KHwrQv06LtIi72UjE2bTuTY2ViJGkuIOcCv%2BsAcmm8NFAebvIruWJtfrKDMp%2Fyofphao71h&X-Amz-Signature=ee1ca3ce53cf2074910756fb139c68df20eb97746b3e308af8db34dda1452395&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTZXGOI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCO7nme09Ntpkt2bR9FernoNuhrIELX9WSQPIGjh03t5QIgVO%2FMe71%2Bo0MetM54XTJX%2FLYH%2B2y3Wq46bwXwvcvZ28Iq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBirdWrHTJnXSE9ysyrcAy7sODWE4NSLeGVCtDd9Ri2MYaTstKkap3nTVphkmBC6nVQyaoFE5dJUReAp2tI9fcfLgA%2BPKmTzfyqUEBRXmX9DVrxq7fiuOJrrVviA37Ft3%2FQmEy%2FXmdIhrb%2BfyAeKbJTeQqTw7PTS8fzqb3Gl2R1qPCJyesmQQ4D3eioSkK58pgPQLUPl79VwhGQgC%2BEOpV12%2BswRRkE1bW92ExHi2%2FCtZ51SgmF95Ywurhq4x33zBDX9z27lHmfVscrClI8EgFxro30inOw3ikazBMz94iA5nHFew8ApmE1P5h63nsITQy4voyoQ1wTcFRRADYuJUAcrW3wKDKv18TnOorE41LQrIxhPaQtH3R5MxdwVq0uemLiopW6M9wLEw7yVS6ueLGiK%2FWsS%2BfNRT5Oh%2FUTn1n7FFZCGdpzIwi6c0MCUnJ0Mlxk%2B77mr9rgVBH2%2FLZAPcuJnCIoFt%2FBPsPnMin%2FjuRKRKHW%2Be3fylnmwtMPMSKeEv0kd0OAiWO3lEDrJr01P8yvjB9Basd7Fpgn2HHQS15qc2PboBSrUcLQyugWuUswaNrNvlu6jLXWEMQIHbaXjMvjXW33dt8k98gQOohD0PP9qDonqpw0C6Gdj7kbhmHh9oR6j5DRGbMjmNbnTMK26jr0GOqUBQz6jTv8K%2FBoVcYLWTQf2KkeceunjiTSmICfZEvMZ5UCGWOcviquWkPw7b%2BTnO2CHzavf%2BssvzdT4yo0a9jWXysxNg2BXBsh6Ir%2BjF%2B8x5iCExh%2BQfJnFhCnNUDtc9%2B10Yxs13ILSAmaBFPuhPUJn2KHwrQv06LtIi72UjE2bTuTY2ViJGkuIOcCv%2BsAcmm8NFAebvIruWJtfrKDMp%2Fyofphao71h&X-Amz-Signature=4cc4f1d6d8f95a544fa6552c84729d0b6ddcfd901cfbd0333b393748cd3689ac&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTZXGOI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCO7nme09Ntpkt2bR9FernoNuhrIELX9WSQPIGjh03t5QIgVO%2FMe71%2Bo0MetM54XTJX%2FLYH%2B2y3Wq46bwXwvcvZ28Iq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBirdWrHTJnXSE9ysyrcAy7sODWE4NSLeGVCtDd9Ri2MYaTstKkap3nTVphkmBC6nVQyaoFE5dJUReAp2tI9fcfLgA%2BPKmTzfyqUEBRXmX9DVrxq7fiuOJrrVviA37Ft3%2FQmEy%2FXmdIhrb%2BfyAeKbJTeQqTw7PTS8fzqb3Gl2R1qPCJyesmQQ4D3eioSkK58pgPQLUPl79VwhGQgC%2BEOpV12%2BswRRkE1bW92ExHi2%2FCtZ51SgmF95Ywurhq4x33zBDX9z27lHmfVscrClI8EgFxro30inOw3ikazBMz94iA5nHFew8ApmE1P5h63nsITQy4voyoQ1wTcFRRADYuJUAcrW3wKDKv18TnOorE41LQrIxhPaQtH3R5MxdwVq0uemLiopW6M9wLEw7yVS6ueLGiK%2FWsS%2BfNRT5Oh%2FUTn1n7FFZCGdpzIwi6c0MCUnJ0Mlxk%2B77mr9rgVBH2%2FLZAPcuJnCIoFt%2FBPsPnMin%2FjuRKRKHW%2Be3fylnmwtMPMSKeEv0kd0OAiWO3lEDrJr01P8yvjB9Basd7Fpgn2HHQS15qc2PboBSrUcLQyugWuUswaNrNvlu6jLXWEMQIHbaXjMvjXW33dt8k98gQOohD0PP9qDonqpw0C6Gdj7kbhmHh9oR6j5DRGbMjmNbnTMK26jr0GOqUBQz6jTv8K%2FBoVcYLWTQf2KkeceunjiTSmICfZEvMZ5UCGWOcviquWkPw7b%2BTnO2CHzavf%2BssvzdT4yo0a9jWXysxNg2BXBsh6Ir%2BjF%2B8x5iCExh%2BQfJnFhCnNUDtc9%2B10Yxs13ILSAmaBFPuhPUJn2KHwrQv06LtIi72UjE2bTuTY2ViJGkuIOcCv%2BsAcmm8NFAebvIruWJtfrKDMp%2Fyofphao71h&X-Amz-Signature=00a0cc798c89b3b7d7db5f33b361e9204fff4a25dae2aa26a8aac396dfb6a82f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTZXGOI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCO7nme09Ntpkt2bR9FernoNuhrIELX9WSQPIGjh03t5QIgVO%2FMe71%2Bo0MetM54XTJX%2FLYH%2B2y3Wq46bwXwvcvZ28Iq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBirdWrHTJnXSE9ysyrcAy7sODWE4NSLeGVCtDd9Ri2MYaTstKkap3nTVphkmBC6nVQyaoFE5dJUReAp2tI9fcfLgA%2BPKmTzfyqUEBRXmX9DVrxq7fiuOJrrVviA37Ft3%2FQmEy%2FXmdIhrb%2BfyAeKbJTeQqTw7PTS8fzqb3Gl2R1qPCJyesmQQ4D3eioSkK58pgPQLUPl79VwhGQgC%2BEOpV12%2BswRRkE1bW92ExHi2%2FCtZ51SgmF95Ywurhq4x33zBDX9z27lHmfVscrClI8EgFxro30inOw3ikazBMz94iA5nHFew8ApmE1P5h63nsITQy4voyoQ1wTcFRRADYuJUAcrW3wKDKv18TnOorE41LQrIxhPaQtH3R5MxdwVq0uemLiopW6M9wLEw7yVS6ueLGiK%2FWsS%2BfNRT5Oh%2FUTn1n7FFZCGdpzIwi6c0MCUnJ0Mlxk%2B77mr9rgVBH2%2FLZAPcuJnCIoFt%2FBPsPnMin%2FjuRKRKHW%2Be3fylnmwtMPMSKeEv0kd0OAiWO3lEDrJr01P8yvjB9Basd7Fpgn2HHQS15qc2PboBSrUcLQyugWuUswaNrNvlu6jLXWEMQIHbaXjMvjXW33dt8k98gQOohD0PP9qDonqpw0C6Gdj7kbhmHh9oR6j5DRGbMjmNbnTMK26jr0GOqUBQz6jTv8K%2FBoVcYLWTQf2KkeceunjiTSmICfZEvMZ5UCGWOcviquWkPw7b%2BTnO2CHzavf%2BssvzdT4yo0a9jWXysxNg2BXBsh6Ir%2BjF%2B8x5iCExh%2BQfJnFhCnNUDtc9%2B10Yxs13ILSAmaBFPuhPUJn2KHwrQv06LtIi72UjE2bTuTY2ViJGkuIOcCv%2BsAcmm8NFAebvIruWJtfrKDMp%2Fyofphao71h&X-Amz-Signature=be88d01789611ca79f5eca083a47ebee4bd3fcdda6f491f9c3be6dd284bba65e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTZXGOI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCO7nme09Ntpkt2bR9FernoNuhrIELX9WSQPIGjh03t5QIgVO%2FMe71%2Bo0MetM54XTJX%2FLYH%2B2y3Wq46bwXwvcvZ28Iq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBirdWrHTJnXSE9ysyrcAy7sODWE4NSLeGVCtDd9Ri2MYaTstKkap3nTVphkmBC6nVQyaoFE5dJUReAp2tI9fcfLgA%2BPKmTzfyqUEBRXmX9DVrxq7fiuOJrrVviA37Ft3%2FQmEy%2FXmdIhrb%2BfyAeKbJTeQqTw7PTS8fzqb3Gl2R1qPCJyesmQQ4D3eioSkK58pgPQLUPl79VwhGQgC%2BEOpV12%2BswRRkE1bW92ExHi2%2FCtZ51SgmF95Ywurhq4x33zBDX9z27lHmfVscrClI8EgFxro30inOw3ikazBMz94iA5nHFew8ApmE1P5h63nsITQy4voyoQ1wTcFRRADYuJUAcrW3wKDKv18TnOorE41LQrIxhPaQtH3R5MxdwVq0uemLiopW6M9wLEw7yVS6ueLGiK%2FWsS%2BfNRT5Oh%2FUTn1n7FFZCGdpzIwi6c0MCUnJ0Mlxk%2B77mr9rgVBH2%2FLZAPcuJnCIoFt%2FBPsPnMin%2FjuRKRKHW%2Be3fylnmwtMPMSKeEv0kd0OAiWO3lEDrJr01P8yvjB9Basd7Fpgn2HHQS15qc2PboBSrUcLQyugWuUswaNrNvlu6jLXWEMQIHbaXjMvjXW33dt8k98gQOohD0PP9qDonqpw0C6Gdj7kbhmHh9oR6j5DRGbMjmNbnTMK26jr0GOqUBQz6jTv8K%2FBoVcYLWTQf2KkeceunjiTSmICfZEvMZ5UCGWOcviquWkPw7b%2BTnO2CHzavf%2BssvzdT4yo0a9jWXysxNg2BXBsh6Ir%2BjF%2B8x5iCExh%2BQfJnFhCnNUDtc9%2B10Yxs13ILSAmaBFPuhPUJn2KHwrQv06LtIi72UjE2bTuTY2ViJGkuIOcCv%2BsAcmm8NFAebvIruWJtfrKDMp%2Fyofphao71h&X-Amz-Signature=c5f43347afbdb8a3fb2e8514822661e29a94bd55abb39f86f6c3c4f5ca504114&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTZXGOI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCO7nme09Ntpkt2bR9FernoNuhrIELX9WSQPIGjh03t5QIgVO%2FMe71%2Bo0MetM54XTJX%2FLYH%2B2y3Wq46bwXwvcvZ28Iq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBirdWrHTJnXSE9ysyrcAy7sODWE4NSLeGVCtDd9Ri2MYaTstKkap3nTVphkmBC6nVQyaoFE5dJUReAp2tI9fcfLgA%2BPKmTzfyqUEBRXmX9DVrxq7fiuOJrrVviA37Ft3%2FQmEy%2FXmdIhrb%2BfyAeKbJTeQqTw7PTS8fzqb3Gl2R1qPCJyesmQQ4D3eioSkK58pgPQLUPl79VwhGQgC%2BEOpV12%2BswRRkE1bW92ExHi2%2FCtZ51SgmF95Ywurhq4x33zBDX9z27lHmfVscrClI8EgFxro30inOw3ikazBMz94iA5nHFew8ApmE1P5h63nsITQy4voyoQ1wTcFRRADYuJUAcrW3wKDKv18TnOorE41LQrIxhPaQtH3R5MxdwVq0uemLiopW6M9wLEw7yVS6ueLGiK%2FWsS%2BfNRT5Oh%2FUTn1n7FFZCGdpzIwi6c0MCUnJ0Mlxk%2B77mr9rgVBH2%2FLZAPcuJnCIoFt%2FBPsPnMin%2FjuRKRKHW%2Be3fylnmwtMPMSKeEv0kd0OAiWO3lEDrJr01P8yvjB9Basd7Fpgn2HHQS15qc2PboBSrUcLQyugWuUswaNrNvlu6jLXWEMQIHbaXjMvjXW33dt8k98gQOohD0PP9qDonqpw0C6Gdj7kbhmHh9oR6j5DRGbMjmNbnTMK26jr0GOqUBQz6jTv8K%2FBoVcYLWTQf2KkeceunjiTSmICfZEvMZ5UCGWOcviquWkPw7b%2BTnO2CHzavf%2BssvzdT4yo0a9jWXysxNg2BXBsh6Ir%2BjF%2B8x5iCExh%2BQfJnFhCnNUDtc9%2B10Yxs13ILSAmaBFPuhPUJn2KHwrQv06LtIi72UjE2bTuTY2ViJGkuIOcCv%2BsAcmm8NFAebvIruWJtfrKDMp%2Fyofphao71h&X-Amz-Signature=121657a1eea2168fb9ab93fd41a278fc81dd24b6f716f61a44b855e6039532b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTZXGOI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCO7nme09Ntpkt2bR9FernoNuhrIELX9WSQPIGjh03t5QIgVO%2FMe71%2Bo0MetM54XTJX%2FLYH%2B2y3Wq46bwXwvcvZ28Iq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBirdWrHTJnXSE9ysyrcAy7sODWE4NSLeGVCtDd9Ri2MYaTstKkap3nTVphkmBC6nVQyaoFE5dJUReAp2tI9fcfLgA%2BPKmTzfyqUEBRXmX9DVrxq7fiuOJrrVviA37Ft3%2FQmEy%2FXmdIhrb%2BfyAeKbJTeQqTw7PTS8fzqb3Gl2R1qPCJyesmQQ4D3eioSkK58pgPQLUPl79VwhGQgC%2BEOpV12%2BswRRkE1bW92ExHi2%2FCtZ51SgmF95Ywurhq4x33zBDX9z27lHmfVscrClI8EgFxro30inOw3ikazBMz94iA5nHFew8ApmE1P5h63nsITQy4voyoQ1wTcFRRADYuJUAcrW3wKDKv18TnOorE41LQrIxhPaQtH3R5MxdwVq0uemLiopW6M9wLEw7yVS6ueLGiK%2FWsS%2BfNRT5Oh%2FUTn1n7FFZCGdpzIwi6c0MCUnJ0Mlxk%2B77mr9rgVBH2%2FLZAPcuJnCIoFt%2FBPsPnMin%2FjuRKRKHW%2Be3fylnmwtMPMSKeEv0kd0OAiWO3lEDrJr01P8yvjB9Basd7Fpgn2HHQS15qc2PboBSrUcLQyugWuUswaNrNvlu6jLXWEMQIHbaXjMvjXW33dt8k98gQOohD0PP9qDonqpw0C6Gdj7kbhmHh9oR6j5DRGbMjmNbnTMK26jr0GOqUBQz6jTv8K%2FBoVcYLWTQf2KkeceunjiTSmICfZEvMZ5UCGWOcviquWkPw7b%2BTnO2CHzavf%2BssvzdT4yo0a9jWXysxNg2BXBsh6Ir%2BjF%2B8x5iCExh%2BQfJnFhCnNUDtc9%2B10Yxs13ILSAmaBFPuhPUJn2KHwrQv06LtIi72UjE2bTuTY2ViJGkuIOcCv%2BsAcmm8NFAebvIruWJtfrKDMp%2Fyofphao71h&X-Amz-Signature=6d82ff21f7e01c5e15b7c4af1526976d645735b8ed0b44632033542972b34233&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDEJWC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDwnVkoGB0nejZoeh%2B9UkvScHJCOA8FTvHkYKA1ggbiWwIgWImnhxUUopF60FslrJ4P4BgTzIRp0PxP5X75A63%2FNaAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBD%2BUd%2FD%2FyBfkbO4vyrcAzvF7%2F7c71vYQnkRmEdzZ7gAnd7VD564Xz7lQ7%2BCAc8GdKT%2B7sZALHoLC%2FBS0nGq56qG7YpF4IQou91NYbFd%2BvFpFskJrOKo8DYSwa7Lkud1lanbFqCSE8KQuB3KfR2KFI0wzjR8LUDgYBrQQmNnuvRgR8O6SXqrsh3GfCUU4qUierAbIXS8z22ZrWhyBgt%2BMnbmqlL1Wgc5kP8WWbmSJrcgU2%2BNtfW0XmBCoQam703%2FCnc%2BE3HahqzbodNOfXmieLcKqliNcP5WRuGogZHTt82REdCz9WdfBWjs%2Fredv75bmGEcX4yCxqsyWXakUucwFkc81qNJO0LRxqHDs%2ByKzO1qVOjWBJTcfCH2G%2F6toweiAGhba57kPJ4GHcXsK%2B%2BT11Sgv2cnZ%2BCc9nL351D4XhHQRRjO2hIJxwknDnae6%2BoXIEfnU1YVh8KuKrVk4I%2FH%2BNajOl1%2B0QIAr6%2BcviFgs5%2B2vTCYaRrdCCiwEdTGzbCJWJNAen3WgT92tpc2ZYugY7lc7O3jSPXKi2sV7cjnYazm96VVPZzZZs3bkSuIqOdcCumpGVqBOW6owUfRF9V1s1BdqcFKDC7%2FfiUUHS2YMQ3vYCtZur2q34lb3zpiMmX7Ril1gxotO4wrm8NxMI28jr0GOqUBMVOYo%2Bdn9En1k1rAB0SJDc6LtLY3baFeLeIHWesH%2Ft3f8MSgys6Hm6OBkj2PC3OmAwKtJEoy%2FDUuQeCcqhslv7tB1HJaUHjzazWa6TGIhi5ybqrau9tn%2BzZzr%2FPDt8RtaVo1oEoyhvAM1%2BtLkA2%2BqnJDyJ9BbN9nsN0jomotENzowYWOX9XVcukSfOlB%2BvafV3ZaYfSOsIYRm05HW9sQE9a57BQA&X-Amz-Signature=93ffdb045c129c7ef807a9614b123f823c0559678f61551bdfc832223ae958d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXDEJWC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDwnVkoGB0nejZoeh%2B9UkvScHJCOA8FTvHkYKA1ggbiWwIgWImnhxUUopF60FslrJ4P4BgTzIRp0PxP5X75A63%2FNaAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBD%2BUd%2FD%2FyBfkbO4vyrcAzvF7%2F7c71vYQnkRmEdzZ7gAnd7VD564Xz7lQ7%2BCAc8GdKT%2B7sZALHoLC%2FBS0nGq56qG7YpF4IQou91NYbFd%2BvFpFskJrOKo8DYSwa7Lkud1lanbFqCSE8KQuB3KfR2KFI0wzjR8LUDgYBrQQmNnuvRgR8O6SXqrsh3GfCUU4qUierAbIXS8z22ZrWhyBgt%2BMnbmqlL1Wgc5kP8WWbmSJrcgU2%2BNtfW0XmBCoQam703%2FCnc%2BE3HahqzbodNOfXmieLcKqliNcP5WRuGogZHTt82REdCz9WdfBWjs%2Fredv75bmGEcX4yCxqsyWXakUucwFkc81qNJO0LRxqHDs%2ByKzO1qVOjWBJTcfCH2G%2F6toweiAGhba57kPJ4GHcXsK%2B%2BT11Sgv2cnZ%2BCc9nL351D4XhHQRRjO2hIJxwknDnae6%2BoXIEfnU1YVh8KuKrVk4I%2FH%2BNajOl1%2B0QIAr6%2BcviFgs5%2B2vTCYaRrdCCiwEdTGzbCJWJNAen3WgT92tpc2ZYugY7lc7O3jSPXKi2sV7cjnYazm96VVPZzZZs3bkSuIqOdcCumpGVqBOW6owUfRF9V1s1BdqcFKDC7%2FfiUUHS2YMQ3vYCtZur2q34lb3zpiMmX7Ril1gxotO4wrm8NxMI28jr0GOqUBMVOYo%2Bdn9En1k1rAB0SJDc6LtLY3baFeLeIHWesH%2Ft3f8MSgys6Hm6OBkj2PC3OmAwKtJEoy%2FDUuQeCcqhslv7tB1HJaUHjzazWa6TGIhi5ybqrau9tn%2BzZzr%2FPDt8RtaVo1oEoyhvAM1%2BtLkA2%2BqnJDyJ9BbN9nsN0jomotENzowYWOX9XVcukSfOlB%2BvafV3ZaYfSOsIYRm05HW9sQE9a57BQA&X-Amz-Signature=1ba8eb235ed03f0db766340a62faf3bbebd1da29922ac034eb4d33e3a02bec83&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
