

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNZZFGR6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyDRygBm%2BCSfd3oWGQdUeAwvPHqnlPzl%2BYW0Ag4FPfyAIgBciDHwG8poRoRuxEkHeJEUOaxqmHN0vCItoV9ded6%2FYqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvTDUnalvIYlL5SIircA8sjo%2Bj64pytUymd6zlitOrWqkZOPelTcHKOQcREnc4qjQLODeXyJfaxOJd2uMpjMDpZgFct70r55OO1b3ZBzPZih4BMVC18VlgttEMBjW8NXsEBuCy8OBoq20B1wFSXNNBMyNh13l70pPKRhp%2FNHdhDVYTeUjvwlzh2mbmfGGrDRV6cMB4UX%2BIdc7L8s0lM5%2BTTJQdOYxXq6fDd5vJTLnQpfio8XaSSwjzIkab0xchR0H7Vmhj5qFr6jv%2FltrMSY9NtIzFCTN4v8pvzz4FmkLYajgrC1C7iwyXsjORi5hxZT7pHHotZlVXENWvR%2B8SqqM892%2FdsWvaAY8xoiecozpxAV%2Be%2BBzx7k5ZJxaBMxpaS%2B3Y6PwmLVXyHFsUOCc%2FLoQ5WXMwQBVOMh7APh1ZVgpgUpiVlaLDSwAkJAzLjwiF3Z2awj5Zf36RidhHw2JvQt0UmlqJYbo7u20tWY3O9RhQV57y6eVcZDI1qBtCvLFErCMl0EmLH6KQJKnSQDUOI1L4Jtebhqv9LQhF%2F7ZFkHB4eOUrichzzTKKgtPhjjZdPZWdC2x5pKhtCAH7p%2FlhoQ5dP6ivTaeqflmkZqyG%2FsdH6uZmM0ywNAKK4L6KhH1igFv6WDpmce0SsRPwBMKKU9bwGOqUBAGTIwrg13F8brL%2BPotXCL11fvCjw5OtQ%2FfPENzG0xH55JupZInjeSAtBqGbpvGdx%2BCL%2Bo4rANeZqnsi2Ou%2F%2FGjQdSoPPZSmWsez%2Bl7Ecvw8EZ97J1ZNzRm7OzugxBSmqG2o3LER0nGSRYn2b9NuRDZXoe790BiBN4%2FzQJwG9DP3CoImxRBQ4kCINAjahxJNel%2F97x%2BjVhn2tBOb0ilQTYTxTmnnp&X-Amz-Signature=cdf06e55a7e926df9ba40f6c74d9c26228c485a2ab2c7714d0d232842fd7ae17&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNZZFGR6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyDRygBm%2BCSfd3oWGQdUeAwvPHqnlPzl%2BYW0Ag4FPfyAIgBciDHwG8poRoRuxEkHeJEUOaxqmHN0vCItoV9ded6%2FYqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvTDUnalvIYlL5SIircA8sjo%2Bj64pytUymd6zlitOrWqkZOPelTcHKOQcREnc4qjQLODeXyJfaxOJd2uMpjMDpZgFct70r55OO1b3ZBzPZih4BMVC18VlgttEMBjW8NXsEBuCy8OBoq20B1wFSXNNBMyNh13l70pPKRhp%2FNHdhDVYTeUjvwlzh2mbmfGGrDRV6cMB4UX%2BIdc7L8s0lM5%2BTTJQdOYxXq6fDd5vJTLnQpfio8XaSSwjzIkab0xchR0H7Vmhj5qFr6jv%2FltrMSY9NtIzFCTN4v8pvzz4FmkLYajgrC1C7iwyXsjORi5hxZT7pHHotZlVXENWvR%2B8SqqM892%2FdsWvaAY8xoiecozpxAV%2Be%2BBzx7k5ZJxaBMxpaS%2B3Y6PwmLVXyHFsUOCc%2FLoQ5WXMwQBVOMh7APh1ZVgpgUpiVlaLDSwAkJAzLjwiF3Z2awj5Zf36RidhHw2JvQt0UmlqJYbo7u20tWY3O9RhQV57y6eVcZDI1qBtCvLFErCMl0EmLH6KQJKnSQDUOI1L4Jtebhqv9LQhF%2F7ZFkHB4eOUrichzzTKKgtPhjjZdPZWdC2x5pKhtCAH7p%2FlhoQ5dP6ivTaeqflmkZqyG%2FsdH6uZmM0ywNAKK4L6KhH1igFv6WDpmce0SsRPwBMKKU9bwGOqUBAGTIwrg13F8brL%2BPotXCL11fvCjw5OtQ%2FfPENzG0xH55JupZInjeSAtBqGbpvGdx%2BCL%2Bo4rANeZqnsi2Ou%2F%2FGjQdSoPPZSmWsez%2Bl7Ecvw8EZ97J1ZNzRm7OzugxBSmqG2o3LER0nGSRYn2b9NuRDZXoe790BiBN4%2FzQJwG9DP3CoImxRBQ4kCINAjahxJNel%2F97x%2BjVhn2tBOb0ilQTYTxTmnnp&X-Amz-Signature=f4545f823d4c885fe0582b3b68eb361d560debfe3e83e561dcc53054ae4780a3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNZZFGR6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyDRygBm%2BCSfd3oWGQdUeAwvPHqnlPzl%2BYW0Ag4FPfyAIgBciDHwG8poRoRuxEkHeJEUOaxqmHN0vCItoV9ded6%2FYqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvTDUnalvIYlL5SIircA8sjo%2Bj64pytUymd6zlitOrWqkZOPelTcHKOQcREnc4qjQLODeXyJfaxOJd2uMpjMDpZgFct70r55OO1b3ZBzPZih4BMVC18VlgttEMBjW8NXsEBuCy8OBoq20B1wFSXNNBMyNh13l70pPKRhp%2FNHdhDVYTeUjvwlzh2mbmfGGrDRV6cMB4UX%2BIdc7L8s0lM5%2BTTJQdOYxXq6fDd5vJTLnQpfio8XaSSwjzIkab0xchR0H7Vmhj5qFr6jv%2FltrMSY9NtIzFCTN4v8pvzz4FmkLYajgrC1C7iwyXsjORi5hxZT7pHHotZlVXENWvR%2B8SqqM892%2FdsWvaAY8xoiecozpxAV%2Be%2BBzx7k5ZJxaBMxpaS%2B3Y6PwmLVXyHFsUOCc%2FLoQ5WXMwQBVOMh7APh1ZVgpgUpiVlaLDSwAkJAzLjwiF3Z2awj5Zf36RidhHw2JvQt0UmlqJYbo7u20tWY3O9RhQV57y6eVcZDI1qBtCvLFErCMl0EmLH6KQJKnSQDUOI1L4Jtebhqv9LQhF%2F7ZFkHB4eOUrichzzTKKgtPhjjZdPZWdC2x5pKhtCAH7p%2FlhoQ5dP6ivTaeqflmkZqyG%2FsdH6uZmM0ywNAKK4L6KhH1igFv6WDpmce0SsRPwBMKKU9bwGOqUBAGTIwrg13F8brL%2BPotXCL11fvCjw5OtQ%2FfPENzG0xH55JupZInjeSAtBqGbpvGdx%2BCL%2Bo4rANeZqnsi2Ou%2F%2FGjQdSoPPZSmWsez%2Bl7Ecvw8EZ97J1ZNzRm7OzugxBSmqG2o3LER0nGSRYn2b9NuRDZXoe790BiBN4%2FzQJwG9DP3CoImxRBQ4kCINAjahxJNel%2F97x%2BjVhn2tBOb0ilQTYTxTmnnp&X-Amz-Signature=72dab11f060fbc3887460cb7364ebf2bc11bc7dc214850475d77058769ae94da&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNZZFGR6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyDRygBm%2BCSfd3oWGQdUeAwvPHqnlPzl%2BYW0Ag4FPfyAIgBciDHwG8poRoRuxEkHeJEUOaxqmHN0vCItoV9ded6%2FYqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvTDUnalvIYlL5SIircA8sjo%2Bj64pytUymd6zlitOrWqkZOPelTcHKOQcREnc4qjQLODeXyJfaxOJd2uMpjMDpZgFct70r55OO1b3ZBzPZih4BMVC18VlgttEMBjW8NXsEBuCy8OBoq20B1wFSXNNBMyNh13l70pPKRhp%2FNHdhDVYTeUjvwlzh2mbmfGGrDRV6cMB4UX%2BIdc7L8s0lM5%2BTTJQdOYxXq6fDd5vJTLnQpfio8XaSSwjzIkab0xchR0H7Vmhj5qFr6jv%2FltrMSY9NtIzFCTN4v8pvzz4FmkLYajgrC1C7iwyXsjORi5hxZT7pHHotZlVXENWvR%2B8SqqM892%2FdsWvaAY8xoiecozpxAV%2Be%2BBzx7k5ZJxaBMxpaS%2B3Y6PwmLVXyHFsUOCc%2FLoQ5WXMwQBVOMh7APh1ZVgpgUpiVlaLDSwAkJAzLjwiF3Z2awj5Zf36RidhHw2JvQt0UmlqJYbo7u20tWY3O9RhQV57y6eVcZDI1qBtCvLFErCMl0EmLH6KQJKnSQDUOI1L4Jtebhqv9LQhF%2F7ZFkHB4eOUrichzzTKKgtPhjjZdPZWdC2x5pKhtCAH7p%2FlhoQ5dP6ivTaeqflmkZqyG%2FsdH6uZmM0ywNAKK4L6KhH1igFv6WDpmce0SsRPwBMKKU9bwGOqUBAGTIwrg13F8brL%2BPotXCL11fvCjw5OtQ%2FfPENzG0xH55JupZInjeSAtBqGbpvGdx%2BCL%2Bo4rANeZqnsi2Ou%2F%2FGjQdSoPPZSmWsez%2Bl7Ecvw8EZ97J1ZNzRm7OzugxBSmqG2o3LER0nGSRYn2b9NuRDZXoe790BiBN4%2FzQJwG9DP3CoImxRBQ4kCINAjahxJNel%2F97x%2BjVhn2tBOb0ilQTYTxTmnnp&X-Amz-Signature=aa877120f085095bf5dfa9141c66d422137a66e1fec30bf84965ad3f05f9aaae&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNZZFGR6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyDRygBm%2BCSfd3oWGQdUeAwvPHqnlPzl%2BYW0Ag4FPfyAIgBciDHwG8poRoRuxEkHeJEUOaxqmHN0vCItoV9ded6%2FYqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvTDUnalvIYlL5SIircA8sjo%2Bj64pytUymd6zlitOrWqkZOPelTcHKOQcREnc4qjQLODeXyJfaxOJd2uMpjMDpZgFct70r55OO1b3ZBzPZih4BMVC18VlgttEMBjW8NXsEBuCy8OBoq20B1wFSXNNBMyNh13l70pPKRhp%2FNHdhDVYTeUjvwlzh2mbmfGGrDRV6cMB4UX%2BIdc7L8s0lM5%2BTTJQdOYxXq6fDd5vJTLnQpfio8XaSSwjzIkab0xchR0H7Vmhj5qFr6jv%2FltrMSY9NtIzFCTN4v8pvzz4FmkLYajgrC1C7iwyXsjORi5hxZT7pHHotZlVXENWvR%2B8SqqM892%2FdsWvaAY8xoiecozpxAV%2Be%2BBzx7k5ZJxaBMxpaS%2B3Y6PwmLVXyHFsUOCc%2FLoQ5WXMwQBVOMh7APh1ZVgpgUpiVlaLDSwAkJAzLjwiF3Z2awj5Zf36RidhHw2JvQt0UmlqJYbo7u20tWY3O9RhQV57y6eVcZDI1qBtCvLFErCMl0EmLH6KQJKnSQDUOI1L4Jtebhqv9LQhF%2F7ZFkHB4eOUrichzzTKKgtPhjjZdPZWdC2x5pKhtCAH7p%2FlhoQ5dP6ivTaeqflmkZqyG%2FsdH6uZmM0ywNAKK4L6KhH1igFv6WDpmce0SsRPwBMKKU9bwGOqUBAGTIwrg13F8brL%2BPotXCL11fvCjw5OtQ%2FfPENzG0xH55JupZInjeSAtBqGbpvGdx%2BCL%2Bo4rANeZqnsi2Ou%2F%2FGjQdSoPPZSmWsez%2Bl7Ecvw8EZ97J1ZNzRm7OzugxBSmqG2o3LER0nGSRYn2b9NuRDZXoe790BiBN4%2FzQJwG9DP3CoImxRBQ4kCINAjahxJNel%2F97x%2BjVhn2tBOb0ilQTYTxTmnnp&X-Amz-Signature=becdb26653e2efc1e3f84d0b2846f40fa139befa4c1e97fe585e4522108e9285&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNZZFGR6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyDRygBm%2BCSfd3oWGQdUeAwvPHqnlPzl%2BYW0Ag4FPfyAIgBciDHwG8poRoRuxEkHeJEUOaxqmHN0vCItoV9ded6%2FYqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvTDUnalvIYlL5SIircA8sjo%2Bj64pytUymd6zlitOrWqkZOPelTcHKOQcREnc4qjQLODeXyJfaxOJd2uMpjMDpZgFct70r55OO1b3ZBzPZih4BMVC18VlgttEMBjW8NXsEBuCy8OBoq20B1wFSXNNBMyNh13l70pPKRhp%2FNHdhDVYTeUjvwlzh2mbmfGGrDRV6cMB4UX%2BIdc7L8s0lM5%2BTTJQdOYxXq6fDd5vJTLnQpfio8XaSSwjzIkab0xchR0H7Vmhj5qFr6jv%2FltrMSY9NtIzFCTN4v8pvzz4FmkLYajgrC1C7iwyXsjORi5hxZT7pHHotZlVXENWvR%2B8SqqM892%2FdsWvaAY8xoiecozpxAV%2Be%2BBzx7k5ZJxaBMxpaS%2B3Y6PwmLVXyHFsUOCc%2FLoQ5WXMwQBVOMh7APh1ZVgpgUpiVlaLDSwAkJAzLjwiF3Z2awj5Zf36RidhHw2JvQt0UmlqJYbo7u20tWY3O9RhQV57y6eVcZDI1qBtCvLFErCMl0EmLH6KQJKnSQDUOI1L4Jtebhqv9LQhF%2F7ZFkHB4eOUrichzzTKKgtPhjjZdPZWdC2x5pKhtCAH7p%2FlhoQ5dP6ivTaeqflmkZqyG%2FsdH6uZmM0ywNAKK4L6KhH1igFv6WDpmce0SsRPwBMKKU9bwGOqUBAGTIwrg13F8brL%2BPotXCL11fvCjw5OtQ%2FfPENzG0xH55JupZInjeSAtBqGbpvGdx%2BCL%2Bo4rANeZqnsi2Ou%2F%2FGjQdSoPPZSmWsez%2Bl7Ecvw8EZ97J1ZNzRm7OzugxBSmqG2o3LER0nGSRYn2b9NuRDZXoe790BiBN4%2FzQJwG9DP3CoImxRBQ4kCINAjahxJNel%2F97x%2BjVhn2tBOb0ilQTYTxTmnnp&X-Amz-Signature=d04bbe4e3f8a2df6f33320eae102211c044c4a3917c39a9366c98461591d9d16&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNZZFGR6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyDRygBm%2BCSfd3oWGQdUeAwvPHqnlPzl%2BYW0Ag4FPfyAIgBciDHwG8poRoRuxEkHeJEUOaxqmHN0vCItoV9ded6%2FYqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvTDUnalvIYlL5SIircA8sjo%2Bj64pytUymd6zlitOrWqkZOPelTcHKOQcREnc4qjQLODeXyJfaxOJd2uMpjMDpZgFct70r55OO1b3ZBzPZih4BMVC18VlgttEMBjW8NXsEBuCy8OBoq20B1wFSXNNBMyNh13l70pPKRhp%2FNHdhDVYTeUjvwlzh2mbmfGGrDRV6cMB4UX%2BIdc7L8s0lM5%2BTTJQdOYxXq6fDd5vJTLnQpfio8XaSSwjzIkab0xchR0H7Vmhj5qFr6jv%2FltrMSY9NtIzFCTN4v8pvzz4FmkLYajgrC1C7iwyXsjORi5hxZT7pHHotZlVXENWvR%2B8SqqM892%2FdsWvaAY8xoiecozpxAV%2Be%2BBzx7k5ZJxaBMxpaS%2B3Y6PwmLVXyHFsUOCc%2FLoQ5WXMwQBVOMh7APh1ZVgpgUpiVlaLDSwAkJAzLjwiF3Z2awj5Zf36RidhHw2JvQt0UmlqJYbo7u20tWY3O9RhQV57y6eVcZDI1qBtCvLFErCMl0EmLH6KQJKnSQDUOI1L4Jtebhqv9LQhF%2F7ZFkHB4eOUrichzzTKKgtPhjjZdPZWdC2x5pKhtCAH7p%2FlhoQ5dP6ivTaeqflmkZqyG%2FsdH6uZmM0ywNAKK4L6KhH1igFv6WDpmce0SsRPwBMKKU9bwGOqUBAGTIwrg13F8brL%2BPotXCL11fvCjw5OtQ%2FfPENzG0xH55JupZInjeSAtBqGbpvGdx%2BCL%2Bo4rANeZqnsi2Ou%2F%2FGjQdSoPPZSmWsez%2Bl7Ecvw8EZ97J1ZNzRm7OzugxBSmqG2o3LER0nGSRYn2b9NuRDZXoe790BiBN4%2FzQJwG9DP3CoImxRBQ4kCINAjahxJNel%2F97x%2BjVhn2tBOb0ilQTYTxTmnnp&X-Amz-Signature=2ce33726641d2aeeb754fdcc2c658a2adbb3aba180a19571f284fa45373e3b88&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNZZFGR6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyDRygBm%2BCSfd3oWGQdUeAwvPHqnlPzl%2BYW0Ag4FPfyAIgBciDHwG8poRoRuxEkHeJEUOaxqmHN0vCItoV9ded6%2FYqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvTDUnalvIYlL5SIircA8sjo%2Bj64pytUymd6zlitOrWqkZOPelTcHKOQcREnc4qjQLODeXyJfaxOJd2uMpjMDpZgFct70r55OO1b3ZBzPZih4BMVC18VlgttEMBjW8NXsEBuCy8OBoq20B1wFSXNNBMyNh13l70pPKRhp%2FNHdhDVYTeUjvwlzh2mbmfGGrDRV6cMB4UX%2BIdc7L8s0lM5%2BTTJQdOYxXq6fDd5vJTLnQpfio8XaSSwjzIkab0xchR0H7Vmhj5qFr6jv%2FltrMSY9NtIzFCTN4v8pvzz4FmkLYajgrC1C7iwyXsjORi5hxZT7pHHotZlVXENWvR%2B8SqqM892%2FdsWvaAY8xoiecozpxAV%2Be%2BBzx7k5ZJxaBMxpaS%2B3Y6PwmLVXyHFsUOCc%2FLoQ5WXMwQBVOMh7APh1ZVgpgUpiVlaLDSwAkJAzLjwiF3Z2awj5Zf36RidhHw2JvQt0UmlqJYbo7u20tWY3O9RhQV57y6eVcZDI1qBtCvLFErCMl0EmLH6KQJKnSQDUOI1L4Jtebhqv9LQhF%2F7ZFkHB4eOUrichzzTKKgtPhjjZdPZWdC2x5pKhtCAH7p%2FlhoQ5dP6ivTaeqflmkZqyG%2FsdH6uZmM0ywNAKK4L6KhH1igFv6WDpmce0SsRPwBMKKU9bwGOqUBAGTIwrg13F8brL%2BPotXCL11fvCjw5OtQ%2FfPENzG0xH55JupZInjeSAtBqGbpvGdx%2BCL%2Bo4rANeZqnsi2Ou%2F%2FGjQdSoPPZSmWsez%2Bl7Ecvw8EZ97J1ZNzRm7OzugxBSmqG2o3LER0nGSRYn2b9NuRDZXoe790BiBN4%2FzQJwG9DP3CoImxRBQ4kCINAjahxJNel%2F97x%2BjVhn2tBOb0ilQTYTxTmnnp&X-Amz-Signature=6e38ce2bdc7c11cbadb80850ca387a71f68e11f085cb1b255df7fc1e0cb93568&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNZZFGR6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyDRygBm%2BCSfd3oWGQdUeAwvPHqnlPzl%2BYW0Ag4FPfyAIgBciDHwG8poRoRuxEkHeJEUOaxqmHN0vCItoV9ded6%2FYqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvTDUnalvIYlL5SIircA8sjo%2Bj64pytUymd6zlitOrWqkZOPelTcHKOQcREnc4qjQLODeXyJfaxOJd2uMpjMDpZgFct70r55OO1b3ZBzPZih4BMVC18VlgttEMBjW8NXsEBuCy8OBoq20B1wFSXNNBMyNh13l70pPKRhp%2FNHdhDVYTeUjvwlzh2mbmfGGrDRV6cMB4UX%2BIdc7L8s0lM5%2BTTJQdOYxXq6fDd5vJTLnQpfio8XaSSwjzIkab0xchR0H7Vmhj5qFr6jv%2FltrMSY9NtIzFCTN4v8pvzz4FmkLYajgrC1C7iwyXsjORi5hxZT7pHHotZlVXENWvR%2B8SqqM892%2FdsWvaAY8xoiecozpxAV%2Be%2BBzx7k5ZJxaBMxpaS%2B3Y6PwmLVXyHFsUOCc%2FLoQ5WXMwQBVOMh7APh1ZVgpgUpiVlaLDSwAkJAzLjwiF3Z2awj5Zf36RidhHw2JvQt0UmlqJYbo7u20tWY3O9RhQV57y6eVcZDI1qBtCvLFErCMl0EmLH6KQJKnSQDUOI1L4Jtebhqv9LQhF%2F7ZFkHB4eOUrichzzTKKgtPhjjZdPZWdC2x5pKhtCAH7p%2FlhoQ5dP6ivTaeqflmkZqyG%2FsdH6uZmM0ywNAKK4L6KhH1igFv6WDpmce0SsRPwBMKKU9bwGOqUBAGTIwrg13F8brL%2BPotXCL11fvCjw5OtQ%2FfPENzG0xH55JupZInjeSAtBqGbpvGdx%2BCL%2Bo4rANeZqnsi2Ou%2F%2FGjQdSoPPZSmWsez%2Bl7Ecvw8EZ97J1ZNzRm7OzugxBSmqG2o3LER0nGSRYn2b9NuRDZXoe790BiBN4%2FzQJwG9DP3CoImxRBQ4kCINAjahxJNel%2F97x%2BjVhn2tBOb0ilQTYTxTmnnp&X-Amz-Signature=42c4ce0c57b28e1108db2f63cbd2f9a21c43d8a3d3e085ec720ddf5abbdeb386&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUNO5OL5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDNb3LWnUk8EK61GNloKYkDbud1%2Ftku1kk1sRAqfR1%2FEAiEAtVordhGOBfy4fJyA5FZh2AUnxJ0QEi6nIbMBN3pjZ0EqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOJScWUljTfhS%2F%2BKsyrcAyhdcThUrHayZkViLs88ijkXXHlGDrTt02vPfu7SjkbZ%2FBtIM1Ql0kZ%2FWOL1evcWiYcif4kJMQYEH9vkAFKWNcaEYy0jJ9qdR2BTst1XSoK5%2F4xchhGyQ3HpG5S4cMhtvnSeTHv99%2F5SkYdSwgEDjZg2GY8HjNeSptLgjm2dqnDQbSnXOIzrj5h50AvEwhxyV8e%2BbT3RweAKttf5ANfbmTWL6tSkQY%2BSppiOzdqSNDTyIrUv51MkvbTU5oMte4ZSTvq964LRRLjiJpGgIrFeWyz7ieqLDGkSm8ZcVrO%2FEJujgcV5YZxwxxOA5uz4bQkv2ocbMaZ0jNBuLOq%2F38HBNPJo2NrFjLm8GvUTksRL%2FZrbgSg028g4Q3fDp1%2FJkpgdK9CZtAPiVZpA9DLuW%2BkxabS%2BVUmjEOATHpLC0Hyt2KFm6OZrMGijY%2B3sMb2SmDyiikpUD%2FnSs%2FdF6ioCZVz2%2F3w6QvFco5uK1bH6UoygM%2B0a384%2FnH%2FXxeieF8zmv6kk3hwImQoD1Uq9wGGEBJg2csWFxecIqh7YFDDASAwoBWwebGjdAseveyXqydvqTxR4BOOtJagCboyaMzcC8W4cDqVRCBEkbtkArhZPP1YQOZgJQfgiz7bXTSZd2MlYMKyU9bwGOqUBf3nKkjI9V%2FDc1xN8k8zjFjQfMWFNdDqhsZIe26p4bz5i3PCZzX1aXYXyhKWJ6jnVqXH9fW9w8eEfgnujlmuFjGWxXw3%2FW7QcLcA0vdwyb6j6i4ote8yFlXv5598aYXtUm2%2Fo5hXFeyRLUOpo%2B4j4UVlv3dhnr4%2B3cDJBd19BexuMpPlllVk%2F0JWzsJGZQgz1gj6db7dpbRB3dR7e0FImpXxPWHZx&X-Amz-Signature=c3ef733dd73af30f54aca51b0e562716234895f68b1cf74c56f19884b799b787&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUNO5OL5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDNb3LWnUk8EK61GNloKYkDbud1%2Ftku1kk1sRAqfR1%2FEAiEAtVordhGOBfy4fJyA5FZh2AUnxJ0QEi6nIbMBN3pjZ0EqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOJScWUljTfhS%2F%2BKsyrcAyhdcThUrHayZkViLs88ijkXXHlGDrTt02vPfu7SjkbZ%2FBtIM1Ql0kZ%2FWOL1evcWiYcif4kJMQYEH9vkAFKWNcaEYy0jJ9qdR2BTst1XSoK5%2F4xchhGyQ3HpG5S4cMhtvnSeTHv99%2F5SkYdSwgEDjZg2GY8HjNeSptLgjm2dqnDQbSnXOIzrj5h50AvEwhxyV8e%2BbT3RweAKttf5ANfbmTWL6tSkQY%2BSppiOzdqSNDTyIrUv51MkvbTU5oMte4ZSTvq964LRRLjiJpGgIrFeWyz7ieqLDGkSm8ZcVrO%2FEJujgcV5YZxwxxOA5uz4bQkv2ocbMaZ0jNBuLOq%2F38HBNPJo2NrFjLm8GvUTksRL%2FZrbgSg028g4Q3fDp1%2FJkpgdK9CZtAPiVZpA9DLuW%2BkxabS%2BVUmjEOATHpLC0Hyt2KFm6OZrMGijY%2B3sMb2SmDyiikpUD%2FnSs%2FdF6ioCZVz2%2F3w6QvFco5uK1bH6UoygM%2B0a384%2FnH%2FXxeieF8zmv6kk3hwImQoD1Uq9wGGEBJg2csWFxecIqh7YFDDASAwoBWwebGjdAseveyXqydvqTxR4BOOtJagCboyaMzcC8W4cDqVRCBEkbtkArhZPP1YQOZgJQfgiz7bXTSZd2MlYMKyU9bwGOqUBf3nKkjI9V%2FDc1xN8k8zjFjQfMWFNdDqhsZIe26p4bz5i3PCZzX1aXYXyhKWJ6jnVqXH9fW9w8eEfgnujlmuFjGWxXw3%2FW7QcLcA0vdwyb6j6i4ote8yFlXv5598aYXtUm2%2Fo5hXFeyRLUOpo%2B4j4UVlv3dhnr4%2B3cDJBd19BexuMpPlllVk%2F0JWzsJGZQgz1gj6db7dpbRB3dR7e0FImpXxPWHZx&X-Amz-Signature=4d044006b663b84602106af8e8b64039c5028d60ea5b3b4be6c678c23b723a67&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
