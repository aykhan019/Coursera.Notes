

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRI3OPXD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDV2OWWW6hG4VDjW4%2FChzA2iKc31rHT9J1Hm8ty4LC0AAiAmZ9%2BHjp6lAFwCgyivZ2y%2BT%2FH%2FmNWLcQZ4Nzq%2B5LU06CqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjfhVNPiqFS0za0fZKtwD2YSejTezWw2d1owhc%2BMDGDGNXIF%2Fz00GWO%2F4wDs3asu3YYxuYp%2Bq4gRIR%2FgFW8QoZBpopHUDbrrAzKk9ClYlWFu62y5r1H9jA0uJ5C6IhxQLmgr2wVtOlKOx2VBFK2XqnjHK6InZFTtDkR3UFQJpMOhUPT2swvD3EPRzDojx6E3p%2FPsug%2FziZLVUPXYQ1I%2BzqMOq%2F0WfwxglBggPoKgOh4k4U6WuIOgcpIO6gnVEdKNyJv%2BxixP3ou%2BG%2F2h3B1SDJ7hHSUK4qsckMNFoyQ4w6p6jK7F7nX%2BYyBl%2Bt0jIdmoHxYcJfuNwzbIxP6w7OKzH%2BdHc1zLaqPys%2F1QYXq9q7q%2FVhac9eYEHQdiEqYwR6WXA%2FgIJ1ZnCZ9F54iu9zGsNiULEs%2BwhzfKS%2FGzDeh0i1sv5Rx0KwCQ5%2Fg3WotAvBHdeG3%2BocFOHNnxpEdEgs34aTh4w2hX9VpKkfV8kd4kz%2BDUybKoakkt%2FXySC8Mh%2FPtn8DqxP5%2FgLx1HwEhW2o40bdF3D6uXqgeNajbRyXJR%2FR2%2BNr9X4DSjjEge0KZ0k5sTnRHcBfrmrbGQCI1kLAq4oap9U9vE3GbQxL8tIXoNqFIltQqWzsWfJ4n7FrQPXSuIB7cf8ksGC5%2B0co%2BYwytbuvAY6pgFa8Xj0udmrwYS8t799DdS74EwXY8kI1%2BnlCySzto5UtCQowRbAF%2BHrKVi%2FELKacfqfLdgB%2BSgClTergPn%2FTX5Kj%2Bun2MU6uVcXn5XdgdpFPFPVyJ%2BJc0RuaNJ9edsnd9qAPgbkOfuT4O2IQSuvh1LEeEQcTBsusk7hC8N516D6G72dZEtun5WXLM4OebgL59seDzcLOBkpzdeZaxkwftD2YayNgKKt&X-Amz-Signature=82fdfbe93ad6fa0ce0666102fdb870dd0507d43cf8ec309202865057c38b09df&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRI3OPXD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDV2OWWW6hG4VDjW4%2FChzA2iKc31rHT9J1Hm8ty4LC0AAiAmZ9%2BHjp6lAFwCgyivZ2y%2BT%2FH%2FmNWLcQZ4Nzq%2B5LU06CqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjfhVNPiqFS0za0fZKtwD2YSejTezWw2d1owhc%2BMDGDGNXIF%2Fz00GWO%2F4wDs3asu3YYxuYp%2Bq4gRIR%2FgFW8QoZBpopHUDbrrAzKk9ClYlWFu62y5r1H9jA0uJ5C6IhxQLmgr2wVtOlKOx2VBFK2XqnjHK6InZFTtDkR3UFQJpMOhUPT2swvD3EPRzDojx6E3p%2FPsug%2FziZLVUPXYQ1I%2BzqMOq%2F0WfwxglBggPoKgOh4k4U6WuIOgcpIO6gnVEdKNyJv%2BxixP3ou%2BG%2F2h3B1SDJ7hHSUK4qsckMNFoyQ4w6p6jK7F7nX%2BYyBl%2Bt0jIdmoHxYcJfuNwzbIxP6w7OKzH%2BdHc1zLaqPys%2F1QYXq9q7q%2FVhac9eYEHQdiEqYwR6WXA%2FgIJ1ZnCZ9F54iu9zGsNiULEs%2BwhzfKS%2FGzDeh0i1sv5Rx0KwCQ5%2Fg3WotAvBHdeG3%2BocFOHNnxpEdEgs34aTh4w2hX9VpKkfV8kd4kz%2BDUybKoakkt%2FXySC8Mh%2FPtn8DqxP5%2FgLx1HwEhW2o40bdF3D6uXqgeNajbRyXJR%2FR2%2BNr9X4DSjjEge0KZ0k5sTnRHcBfrmrbGQCI1kLAq4oap9U9vE3GbQxL8tIXoNqFIltQqWzsWfJ4n7FrQPXSuIB7cf8ksGC5%2B0co%2BYwytbuvAY6pgFa8Xj0udmrwYS8t799DdS74EwXY8kI1%2BnlCySzto5UtCQowRbAF%2BHrKVi%2FELKacfqfLdgB%2BSgClTergPn%2FTX5Kj%2Bun2MU6uVcXn5XdgdpFPFPVyJ%2BJc0RuaNJ9edsnd9qAPgbkOfuT4O2IQSuvh1LEeEQcTBsusk7hC8N516D6G72dZEtun5WXLM4OebgL59seDzcLOBkpzdeZaxkwftD2YayNgKKt&X-Amz-Signature=3919ff2218446dae13a8047d4fa299c92fb97d5bac076fb1cacf29bb0f4404bd&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRI3OPXD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDV2OWWW6hG4VDjW4%2FChzA2iKc31rHT9J1Hm8ty4LC0AAiAmZ9%2BHjp6lAFwCgyivZ2y%2BT%2FH%2FmNWLcQZ4Nzq%2B5LU06CqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjfhVNPiqFS0za0fZKtwD2YSejTezWw2d1owhc%2BMDGDGNXIF%2Fz00GWO%2F4wDs3asu3YYxuYp%2Bq4gRIR%2FgFW8QoZBpopHUDbrrAzKk9ClYlWFu62y5r1H9jA0uJ5C6IhxQLmgr2wVtOlKOx2VBFK2XqnjHK6InZFTtDkR3UFQJpMOhUPT2swvD3EPRzDojx6E3p%2FPsug%2FziZLVUPXYQ1I%2BzqMOq%2F0WfwxglBggPoKgOh4k4U6WuIOgcpIO6gnVEdKNyJv%2BxixP3ou%2BG%2F2h3B1SDJ7hHSUK4qsckMNFoyQ4w6p6jK7F7nX%2BYyBl%2Bt0jIdmoHxYcJfuNwzbIxP6w7OKzH%2BdHc1zLaqPys%2F1QYXq9q7q%2FVhac9eYEHQdiEqYwR6WXA%2FgIJ1ZnCZ9F54iu9zGsNiULEs%2BwhzfKS%2FGzDeh0i1sv5Rx0KwCQ5%2Fg3WotAvBHdeG3%2BocFOHNnxpEdEgs34aTh4w2hX9VpKkfV8kd4kz%2BDUybKoakkt%2FXySC8Mh%2FPtn8DqxP5%2FgLx1HwEhW2o40bdF3D6uXqgeNajbRyXJR%2FR2%2BNr9X4DSjjEge0KZ0k5sTnRHcBfrmrbGQCI1kLAq4oap9U9vE3GbQxL8tIXoNqFIltQqWzsWfJ4n7FrQPXSuIB7cf8ksGC5%2B0co%2BYwytbuvAY6pgFa8Xj0udmrwYS8t799DdS74EwXY8kI1%2BnlCySzto5UtCQowRbAF%2BHrKVi%2FELKacfqfLdgB%2BSgClTergPn%2FTX5Kj%2Bun2MU6uVcXn5XdgdpFPFPVyJ%2BJc0RuaNJ9edsnd9qAPgbkOfuT4O2IQSuvh1LEeEQcTBsusk7hC8N516D6G72dZEtun5WXLM4OebgL59seDzcLOBkpzdeZaxkwftD2YayNgKKt&X-Amz-Signature=5e6becd2d67839d4eb5fd02c9f44d466b11897e10a45cbaf16efa2994c20e011&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRI3OPXD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDV2OWWW6hG4VDjW4%2FChzA2iKc31rHT9J1Hm8ty4LC0AAiAmZ9%2BHjp6lAFwCgyivZ2y%2BT%2FH%2FmNWLcQZ4Nzq%2B5LU06CqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjfhVNPiqFS0za0fZKtwD2YSejTezWw2d1owhc%2BMDGDGNXIF%2Fz00GWO%2F4wDs3asu3YYxuYp%2Bq4gRIR%2FgFW8QoZBpopHUDbrrAzKk9ClYlWFu62y5r1H9jA0uJ5C6IhxQLmgr2wVtOlKOx2VBFK2XqnjHK6InZFTtDkR3UFQJpMOhUPT2swvD3EPRzDojx6E3p%2FPsug%2FziZLVUPXYQ1I%2BzqMOq%2F0WfwxglBggPoKgOh4k4U6WuIOgcpIO6gnVEdKNyJv%2BxixP3ou%2BG%2F2h3B1SDJ7hHSUK4qsckMNFoyQ4w6p6jK7F7nX%2BYyBl%2Bt0jIdmoHxYcJfuNwzbIxP6w7OKzH%2BdHc1zLaqPys%2F1QYXq9q7q%2FVhac9eYEHQdiEqYwR6WXA%2FgIJ1ZnCZ9F54iu9zGsNiULEs%2BwhzfKS%2FGzDeh0i1sv5Rx0KwCQ5%2Fg3WotAvBHdeG3%2BocFOHNnxpEdEgs34aTh4w2hX9VpKkfV8kd4kz%2BDUybKoakkt%2FXySC8Mh%2FPtn8DqxP5%2FgLx1HwEhW2o40bdF3D6uXqgeNajbRyXJR%2FR2%2BNr9X4DSjjEge0KZ0k5sTnRHcBfrmrbGQCI1kLAq4oap9U9vE3GbQxL8tIXoNqFIltQqWzsWfJ4n7FrQPXSuIB7cf8ksGC5%2B0co%2BYwytbuvAY6pgFa8Xj0udmrwYS8t799DdS74EwXY8kI1%2BnlCySzto5UtCQowRbAF%2BHrKVi%2FELKacfqfLdgB%2BSgClTergPn%2FTX5Kj%2Bun2MU6uVcXn5XdgdpFPFPVyJ%2BJc0RuaNJ9edsnd9qAPgbkOfuT4O2IQSuvh1LEeEQcTBsusk7hC8N516D6G72dZEtun5WXLM4OebgL59seDzcLOBkpzdeZaxkwftD2YayNgKKt&X-Amz-Signature=3095c5b170d968043d43bb575f50036225634bd3647d0112827746151515b944&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRI3OPXD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDV2OWWW6hG4VDjW4%2FChzA2iKc31rHT9J1Hm8ty4LC0AAiAmZ9%2BHjp6lAFwCgyivZ2y%2BT%2FH%2FmNWLcQZ4Nzq%2B5LU06CqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjfhVNPiqFS0za0fZKtwD2YSejTezWw2d1owhc%2BMDGDGNXIF%2Fz00GWO%2F4wDs3asu3YYxuYp%2Bq4gRIR%2FgFW8QoZBpopHUDbrrAzKk9ClYlWFu62y5r1H9jA0uJ5C6IhxQLmgr2wVtOlKOx2VBFK2XqnjHK6InZFTtDkR3UFQJpMOhUPT2swvD3EPRzDojx6E3p%2FPsug%2FziZLVUPXYQ1I%2BzqMOq%2F0WfwxglBggPoKgOh4k4U6WuIOgcpIO6gnVEdKNyJv%2BxixP3ou%2BG%2F2h3B1SDJ7hHSUK4qsckMNFoyQ4w6p6jK7F7nX%2BYyBl%2Bt0jIdmoHxYcJfuNwzbIxP6w7OKzH%2BdHc1zLaqPys%2F1QYXq9q7q%2FVhac9eYEHQdiEqYwR6WXA%2FgIJ1ZnCZ9F54iu9zGsNiULEs%2BwhzfKS%2FGzDeh0i1sv5Rx0KwCQ5%2Fg3WotAvBHdeG3%2BocFOHNnxpEdEgs34aTh4w2hX9VpKkfV8kd4kz%2BDUybKoakkt%2FXySC8Mh%2FPtn8DqxP5%2FgLx1HwEhW2o40bdF3D6uXqgeNajbRyXJR%2FR2%2BNr9X4DSjjEge0KZ0k5sTnRHcBfrmrbGQCI1kLAq4oap9U9vE3GbQxL8tIXoNqFIltQqWzsWfJ4n7FrQPXSuIB7cf8ksGC5%2B0co%2BYwytbuvAY6pgFa8Xj0udmrwYS8t799DdS74EwXY8kI1%2BnlCySzto5UtCQowRbAF%2BHrKVi%2FELKacfqfLdgB%2BSgClTergPn%2FTX5Kj%2Bun2MU6uVcXn5XdgdpFPFPVyJ%2BJc0RuaNJ9edsnd9qAPgbkOfuT4O2IQSuvh1LEeEQcTBsusk7hC8N516D6G72dZEtun5WXLM4OebgL59seDzcLOBkpzdeZaxkwftD2YayNgKKt&X-Amz-Signature=4d9e5596e647d0dc2aed98cfe2c3fa63c09ee993378c178560134dc2cbd22474&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRI3OPXD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDV2OWWW6hG4VDjW4%2FChzA2iKc31rHT9J1Hm8ty4LC0AAiAmZ9%2BHjp6lAFwCgyivZ2y%2BT%2FH%2FmNWLcQZ4Nzq%2B5LU06CqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjfhVNPiqFS0za0fZKtwD2YSejTezWw2d1owhc%2BMDGDGNXIF%2Fz00GWO%2F4wDs3asu3YYxuYp%2Bq4gRIR%2FgFW8QoZBpopHUDbrrAzKk9ClYlWFu62y5r1H9jA0uJ5C6IhxQLmgr2wVtOlKOx2VBFK2XqnjHK6InZFTtDkR3UFQJpMOhUPT2swvD3EPRzDojx6E3p%2FPsug%2FziZLVUPXYQ1I%2BzqMOq%2F0WfwxglBggPoKgOh4k4U6WuIOgcpIO6gnVEdKNyJv%2BxixP3ou%2BG%2F2h3B1SDJ7hHSUK4qsckMNFoyQ4w6p6jK7F7nX%2BYyBl%2Bt0jIdmoHxYcJfuNwzbIxP6w7OKzH%2BdHc1zLaqPys%2F1QYXq9q7q%2FVhac9eYEHQdiEqYwR6WXA%2FgIJ1ZnCZ9F54iu9zGsNiULEs%2BwhzfKS%2FGzDeh0i1sv5Rx0KwCQ5%2Fg3WotAvBHdeG3%2BocFOHNnxpEdEgs34aTh4w2hX9VpKkfV8kd4kz%2BDUybKoakkt%2FXySC8Mh%2FPtn8DqxP5%2FgLx1HwEhW2o40bdF3D6uXqgeNajbRyXJR%2FR2%2BNr9X4DSjjEge0KZ0k5sTnRHcBfrmrbGQCI1kLAq4oap9U9vE3GbQxL8tIXoNqFIltQqWzsWfJ4n7FrQPXSuIB7cf8ksGC5%2B0co%2BYwytbuvAY6pgFa8Xj0udmrwYS8t799DdS74EwXY8kI1%2BnlCySzto5UtCQowRbAF%2BHrKVi%2FELKacfqfLdgB%2BSgClTergPn%2FTX5Kj%2Bun2MU6uVcXn5XdgdpFPFPVyJ%2BJc0RuaNJ9edsnd9qAPgbkOfuT4O2IQSuvh1LEeEQcTBsusk7hC8N516D6G72dZEtun5WXLM4OebgL59seDzcLOBkpzdeZaxkwftD2YayNgKKt&X-Amz-Signature=7405f58855dc9b3d819cefc7efa78777abdef1a46b22165aeafe288301a7cf02&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRI3OPXD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDV2OWWW6hG4VDjW4%2FChzA2iKc31rHT9J1Hm8ty4LC0AAiAmZ9%2BHjp6lAFwCgyivZ2y%2BT%2FH%2FmNWLcQZ4Nzq%2B5LU06CqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjfhVNPiqFS0za0fZKtwD2YSejTezWw2d1owhc%2BMDGDGNXIF%2Fz00GWO%2F4wDs3asu3YYxuYp%2Bq4gRIR%2FgFW8QoZBpopHUDbrrAzKk9ClYlWFu62y5r1H9jA0uJ5C6IhxQLmgr2wVtOlKOx2VBFK2XqnjHK6InZFTtDkR3UFQJpMOhUPT2swvD3EPRzDojx6E3p%2FPsug%2FziZLVUPXYQ1I%2BzqMOq%2F0WfwxglBggPoKgOh4k4U6WuIOgcpIO6gnVEdKNyJv%2BxixP3ou%2BG%2F2h3B1SDJ7hHSUK4qsckMNFoyQ4w6p6jK7F7nX%2BYyBl%2Bt0jIdmoHxYcJfuNwzbIxP6w7OKzH%2BdHc1zLaqPys%2F1QYXq9q7q%2FVhac9eYEHQdiEqYwR6WXA%2FgIJ1ZnCZ9F54iu9zGsNiULEs%2BwhzfKS%2FGzDeh0i1sv5Rx0KwCQ5%2Fg3WotAvBHdeG3%2BocFOHNnxpEdEgs34aTh4w2hX9VpKkfV8kd4kz%2BDUybKoakkt%2FXySC8Mh%2FPtn8DqxP5%2FgLx1HwEhW2o40bdF3D6uXqgeNajbRyXJR%2FR2%2BNr9X4DSjjEge0KZ0k5sTnRHcBfrmrbGQCI1kLAq4oap9U9vE3GbQxL8tIXoNqFIltQqWzsWfJ4n7FrQPXSuIB7cf8ksGC5%2B0co%2BYwytbuvAY6pgFa8Xj0udmrwYS8t799DdS74EwXY8kI1%2BnlCySzto5UtCQowRbAF%2BHrKVi%2FELKacfqfLdgB%2BSgClTergPn%2FTX5Kj%2Bun2MU6uVcXn5XdgdpFPFPVyJ%2BJc0RuaNJ9edsnd9qAPgbkOfuT4O2IQSuvh1LEeEQcTBsusk7hC8N516D6G72dZEtun5WXLM4OebgL59seDzcLOBkpzdeZaxkwftD2YayNgKKt&X-Amz-Signature=d4629030056bb0d420c615ef25861388c8ce66d68ab4e287774871ad01e3e91f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRI3OPXD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDV2OWWW6hG4VDjW4%2FChzA2iKc31rHT9J1Hm8ty4LC0AAiAmZ9%2BHjp6lAFwCgyivZ2y%2BT%2FH%2FmNWLcQZ4Nzq%2B5LU06CqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjfhVNPiqFS0za0fZKtwD2YSejTezWw2d1owhc%2BMDGDGNXIF%2Fz00GWO%2F4wDs3asu3YYxuYp%2Bq4gRIR%2FgFW8QoZBpopHUDbrrAzKk9ClYlWFu62y5r1H9jA0uJ5C6IhxQLmgr2wVtOlKOx2VBFK2XqnjHK6InZFTtDkR3UFQJpMOhUPT2swvD3EPRzDojx6E3p%2FPsug%2FziZLVUPXYQ1I%2BzqMOq%2F0WfwxglBggPoKgOh4k4U6WuIOgcpIO6gnVEdKNyJv%2BxixP3ou%2BG%2F2h3B1SDJ7hHSUK4qsckMNFoyQ4w6p6jK7F7nX%2BYyBl%2Bt0jIdmoHxYcJfuNwzbIxP6w7OKzH%2BdHc1zLaqPys%2F1QYXq9q7q%2FVhac9eYEHQdiEqYwR6WXA%2FgIJ1ZnCZ9F54iu9zGsNiULEs%2BwhzfKS%2FGzDeh0i1sv5Rx0KwCQ5%2Fg3WotAvBHdeG3%2BocFOHNnxpEdEgs34aTh4w2hX9VpKkfV8kd4kz%2BDUybKoakkt%2FXySC8Mh%2FPtn8DqxP5%2FgLx1HwEhW2o40bdF3D6uXqgeNajbRyXJR%2FR2%2BNr9X4DSjjEge0KZ0k5sTnRHcBfrmrbGQCI1kLAq4oap9U9vE3GbQxL8tIXoNqFIltQqWzsWfJ4n7FrQPXSuIB7cf8ksGC5%2B0co%2BYwytbuvAY6pgFa8Xj0udmrwYS8t799DdS74EwXY8kI1%2BnlCySzto5UtCQowRbAF%2BHrKVi%2FELKacfqfLdgB%2BSgClTergPn%2FTX5Kj%2Bun2MU6uVcXn5XdgdpFPFPVyJ%2BJc0RuaNJ9edsnd9qAPgbkOfuT4O2IQSuvh1LEeEQcTBsusk7hC8N516D6G72dZEtun5WXLM4OebgL59seDzcLOBkpzdeZaxkwftD2YayNgKKt&X-Amz-Signature=5afbad73b642505944ef5cc7d1e3c9beb3aadbac97130fa3d0a196aed6069797&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRI3OPXD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDV2OWWW6hG4VDjW4%2FChzA2iKc31rHT9J1Hm8ty4LC0AAiAmZ9%2BHjp6lAFwCgyivZ2y%2BT%2FH%2FmNWLcQZ4Nzq%2B5LU06CqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjfhVNPiqFS0za0fZKtwD2YSejTezWw2d1owhc%2BMDGDGNXIF%2Fz00GWO%2F4wDs3asu3YYxuYp%2Bq4gRIR%2FgFW8QoZBpopHUDbrrAzKk9ClYlWFu62y5r1H9jA0uJ5C6IhxQLmgr2wVtOlKOx2VBFK2XqnjHK6InZFTtDkR3UFQJpMOhUPT2swvD3EPRzDojx6E3p%2FPsug%2FziZLVUPXYQ1I%2BzqMOq%2F0WfwxglBggPoKgOh4k4U6WuIOgcpIO6gnVEdKNyJv%2BxixP3ou%2BG%2F2h3B1SDJ7hHSUK4qsckMNFoyQ4w6p6jK7F7nX%2BYyBl%2Bt0jIdmoHxYcJfuNwzbIxP6w7OKzH%2BdHc1zLaqPys%2F1QYXq9q7q%2FVhac9eYEHQdiEqYwR6WXA%2FgIJ1ZnCZ9F54iu9zGsNiULEs%2BwhzfKS%2FGzDeh0i1sv5Rx0KwCQ5%2Fg3WotAvBHdeG3%2BocFOHNnxpEdEgs34aTh4w2hX9VpKkfV8kd4kz%2BDUybKoakkt%2FXySC8Mh%2FPtn8DqxP5%2FgLx1HwEhW2o40bdF3D6uXqgeNajbRyXJR%2FR2%2BNr9X4DSjjEge0KZ0k5sTnRHcBfrmrbGQCI1kLAq4oap9U9vE3GbQxL8tIXoNqFIltQqWzsWfJ4n7FrQPXSuIB7cf8ksGC5%2B0co%2BYwytbuvAY6pgFa8Xj0udmrwYS8t799DdS74EwXY8kI1%2BnlCySzto5UtCQowRbAF%2BHrKVi%2FELKacfqfLdgB%2BSgClTergPn%2FTX5Kj%2Bun2MU6uVcXn5XdgdpFPFPVyJ%2BJc0RuaNJ9edsnd9qAPgbkOfuT4O2IQSuvh1LEeEQcTBsusk7hC8N516D6G72dZEtun5WXLM4OebgL59seDzcLOBkpzdeZaxkwftD2YayNgKKt&X-Amz-Signature=272eabd3d15cdbb1af0d652e49e3fed11dd85ac5c25be2c868d5cae8473ee457&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665J7ZXVUU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDjXDB7MfuAqzKbfX2bpz%2FWBRC1fUDyI%2FGKA6IBN5tHqAiAOAUMBrFM4tpZH5a00G4NJmL%2Fyihj1hZ1HcH1vmfHTnSqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxL6B6GKAD18zJUtoKtwDZk129c2FEhANLRxUBBOAIqhXijsaXO3QyI0I7KoplO5Yz5g4yQFOWBAxqQzZo3X8AlNVctv4uo9RvD7MTzUhAfeXIdLFVBOGc8Mt16P%2BTslwmhO8KbvVzgBvDmUcfXlsHnkdGyB9ta%2BvDLPLVCcoE1m9ScV3qi2409ldLy2b3YZ2o1o1UXBDsY%2FHfdlGAyYpKI9SE45D6XNGYq1%2FZXd7ROMy%2F3pRxVbaKPeNkxZhG7Fo8Y8RJM%2FuccFnu%2F6wp17KjaQ06vs5zO3WVhgn8Xwzi5ZnKVynXhQXax1gz%2BSaVrF75SQ8W9JqUYrAxQ7JGYtfaQoWIflYzo104it%2FzwJvBcSuKllXi%2BQ3VweX9ygLE45EUE0icoX1Evm8TPGNmo3VNizUF2Zxp2ZhIPCN11gmwlMnQe63NhT49M1YCDj8bjATmAPLfbyc0ib3oOU%2BZIb8D74dRI14ImzbPNJDd156CrPUqwWV9QjWpuU%2FKlLls6JNwXQBSjq%2BgmuKkDGANrE7N1J1hjqwsoYvJx7cNKAw65m4sm%2BpdVT%2BcHsRJNFM5bfScgsyn0unZ8z%2BG%2FDgE7kIkRt%2BdvAfoZdHHHTMJVjCyla2aghDpR1QCEfU%2BXujct1kMrrG%2Be5CEjXR7vgwvdbuvAY6pgFdP1LMEavIWgtfQCp4j%2FnQSltBu6DW4tU%2FfL3eO7BoVHeGnyguN%2FmDrLvaAmCRiSyfn%2BJPNHONwtqv%2FuytlSIJGfB5UecRyQHtjU6S4kCb3q678LtkGgSS3VlTQj69yRHtewtNGILV%2FhssNNMvI7N9vsfX1m42rIGhRyBxEHY3B1LTQ7LJkb7Sc5Erzo6tb%2BjeZ48WBM%2BWKLXBeeVzMQRQ%2Fhz3pXmR&X-Amz-Signature=42d1347eeed28f8c9b9fcf126d436862298d4dbe4177a328fbb8cdf3d443fada&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665J7ZXVUU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDjXDB7MfuAqzKbfX2bpz%2FWBRC1fUDyI%2FGKA6IBN5tHqAiAOAUMBrFM4tpZH5a00G4NJmL%2Fyihj1hZ1HcH1vmfHTnSqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxL6B6GKAD18zJUtoKtwDZk129c2FEhANLRxUBBOAIqhXijsaXO3QyI0I7KoplO5Yz5g4yQFOWBAxqQzZo3X8AlNVctv4uo9RvD7MTzUhAfeXIdLFVBOGc8Mt16P%2BTslwmhO8KbvVzgBvDmUcfXlsHnkdGyB9ta%2BvDLPLVCcoE1m9ScV3qi2409ldLy2b3YZ2o1o1UXBDsY%2FHfdlGAyYpKI9SE45D6XNGYq1%2FZXd7ROMy%2F3pRxVbaKPeNkxZhG7Fo8Y8RJM%2FuccFnu%2F6wp17KjaQ06vs5zO3WVhgn8Xwzi5ZnKVynXhQXax1gz%2BSaVrF75SQ8W9JqUYrAxQ7JGYtfaQoWIflYzo104it%2FzwJvBcSuKllXi%2BQ3VweX9ygLE45EUE0icoX1Evm8TPGNmo3VNizUF2Zxp2ZhIPCN11gmwlMnQe63NhT49M1YCDj8bjATmAPLfbyc0ib3oOU%2BZIb8D74dRI14ImzbPNJDd156CrPUqwWV9QjWpuU%2FKlLls6JNwXQBSjq%2BgmuKkDGANrE7N1J1hjqwsoYvJx7cNKAw65m4sm%2BpdVT%2BcHsRJNFM5bfScgsyn0unZ8z%2BG%2FDgE7kIkRt%2BdvAfoZdHHHTMJVjCyla2aghDpR1QCEfU%2BXujct1kMrrG%2Be5CEjXR7vgwvdbuvAY6pgFdP1LMEavIWgtfQCp4j%2FnQSltBu6DW4tU%2FfL3eO7BoVHeGnyguN%2FmDrLvaAmCRiSyfn%2BJPNHONwtqv%2FuytlSIJGfB5UecRyQHtjU6S4kCb3q678LtkGgSS3VlTQj69yRHtewtNGILV%2FhssNNMvI7N9vsfX1m42rIGhRyBxEHY3B1LTQ7LJkb7Sc5Erzo6tb%2BjeZ48WBM%2BWKLXBeeVzMQRQ%2Fhz3pXmR&X-Amz-Signature=78308b25d04745bb66e74c84f58f7b5762c0e2c88d85d1580334ab52fa2557ec&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
