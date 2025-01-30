

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663HHANNB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBn9SwAknTCBXXZrznZAYtPeyQTyum3zgazHbd9aLaJIAiEAhcrbNMqJ%2Bqqn3ZOoyRP0C2xlULYyv85spwFKekcxVnwqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHUk%2BcGqP67lfxocbircA5sRCir%2BZWzuPTnkmlncbVdg%2BKuWo9Yh5XYtkahhr%2BrVWZK9KvdYDerRBdM7SO5qFPxCj%2BgI99Tn%2BrGZoTDeOu7Wt%2BtILSqU2Vqhh%2FjNuDXROtlE9OoUjg3r8vtx2hSZ%2B44zImq%2BafNs25QhzK97hjCCV1egs2KI9CJhnV7voAzSk4ytFfI5h22BrMIU55ATa1OUR7IEpmsMHHc3AC00V2hdpMDmKNkgF6PjAo2eRBV%2B%2BxL677I5mxnPKwcTmQchEMhkdHcW6aDJEaosYGnY8SmmFSygPCgsanQpNEYyHoRrajKlkN6mzJFnaHW8fywcAV8ySx4nhneutv6OV%2BzwS3aMfwwrBJWOEXd3948retn69Fj%2BZELjg6QF%2F72HrAvQDd2zYL4oiOgWIx43OpXZ7ApZgvy7vdxcNioz7zIpR3jKVU%2BQq%2FqG5Aey2pwR%2BJf%2F8cL%2BkMPN5UD%2BR1cu3ECyocn4cxLmA9kdrQj2YGqw1fMPgB7YmKijRX8j20War8b2OZN8xXTLqtvQnykE790E0eu9hhQzteMieDT0DxOih3aBTJlsFXlju8RGrD8RyQy%2B6h1XsHdkf5Zv4BVkswSx5WmFVSM1Mr897eANs%2BnzBJD3lM5ZTsiW6Dw8ssACMKeq77wGOqUBEOlmfnJuYdgL2UEjg20%2B0VgKu%2BIr5ED%2F6KnTyVx9W6NyQWOy%2FHJlehoj9LM1zEJSIGT7oRNRDXRdtJ%2FVDCXTAj3dMq39bgxJ06dpRC5tOIFxZM7HywP0T7a9ppW0xDVPbD87HnpdU7m9HApc1UZJy64VTcVPW%2BDcb9taLnwbmG%2F%2B3MvaGr5fmKW98w405mIjfV6PKdwWF9tcMkj%2F6Ucpi4i%2BOz4L&X-Amz-Signature=6d2d4b2ee4f8a6d3da7b13ab4692050d1a282971d72d532b84d92a46f75052b5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663HHANNB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBn9SwAknTCBXXZrznZAYtPeyQTyum3zgazHbd9aLaJIAiEAhcrbNMqJ%2Bqqn3ZOoyRP0C2xlULYyv85spwFKekcxVnwqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHUk%2BcGqP67lfxocbircA5sRCir%2BZWzuPTnkmlncbVdg%2BKuWo9Yh5XYtkahhr%2BrVWZK9KvdYDerRBdM7SO5qFPxCj%2BgI99Tn%2BrGZoTDeOu7Wt%2BtILSqU2Vqhh%2FjNuDXROtlE9OoUjg3r8vtx2hSZ%2B44zImq%2BafNs25QhzK97hjCCV1egs2KI9CJhnV7voAzSk4ytFfI5h22BrMIU55ATa1OUR7IEpmsMHHc3AC00V2hdpMDmKNkgF6PjAo2eRBV%2B%2BxL677I5mxnPKwcTmQchEMhkdHcW6aDJEaosYGnY8SmmFSygPCgsanQpNEYyHoRrajKlkN6mzJFnaHW8fywcAV8ySx4nhneutv6OV%2BzwS3aMfwwrBJWOEXd3948retn69Fj%2BZELjg6QF%2F72HrAvQDd2zYL4oiOgWIx43OpXZ7ApZgvy7vdxcNioz7zIpR3jKVU%2BQq%2FqG5Aey2pwR%2BJf%2F8cL%2BkMPN5UD%2BR1cu3ECyocn4cxLmA9kdrQj2YGqw1fMPgB7YmKijRX8j20War8b2OZN8xXTLqtvQnykE790E0eu9hhQzteMieDT0DxOih3aBTJlsFXlju8RGrD8RyQy%2B6h1XsHdkf5Zv4BVkswSx5WmFVSM1Mr897eANs%2BnzBJD3lM5ZTsiW6Dw8ssACMKeq77wGOqUBEOlmfnJuYdgL2UEjg20%2B0VgKu%2BIr5ED%2F6KnTyVx9W6NyQWOy%2FHJlehoj9LM1zEJSIGT7oRNRDXRdtJ%2FVDCXTAj3dMq39bgxJ06dpRC5tOIFxZM7HywP0T7a9ppW0xDVPbD87HnpdU7m9HApc1UZJy64VTcVPW%2BDcb9taLnwbmG%2F%2B3MvaGr5fmKW98w405mIjfV6PKdwWF9tcMkj%2F6Ucpi4i%2BOz4L&X-Amz-Signature=6a2d3e14749187561d2780f6fd342c5784a37ccbdc048812a526c68146c18169&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663HHANNB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBn9SwAknTCBXXZrznZAYtPeyQTyum3zgazHbd9aLaJIAiEAhcrbNMqJ%2Bqqn3ZOoyRP0C2xlULYyv85spwFKekcxVnwqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHUk%2BcGqP67lfxocbircA5sRCir%2BZWzuPTnkmlncbVdg%2BKuWo9Yh5XYtkahhr%2BrVWZK9KvdYDerRBdM7SO5qFPxCj%2BgI99Tn%2BrGZoTDeOu7Wt%2BtILSqU2Vqhh%2FjNuDXROtlE9OoUjg3r8vtx2hSZ%2B44zImq%2BafNs25QhzK97hjCCV1egs2KI9CJhnV7voAzSk4ytFfI5h22BrMIU55ATa1OUR7IEpmsMHHc3AC00V2hdpMDmKNkgF6PjAo2eRBV%2B%2BxL677I5mxnPKwcTmQchEMhkdHcW6aDJEaosYGnY8SmmFSygPCgsanQpNEYyHoRrajKlkN6mzJFnaHW8fywcAV8ySx4nhneutv6OV%2BzwS3aMfwwrBJWOEXd3948retn69Fj%2BZELjg6QF%2F72HrAvQDd2zYL4oiOgWIx43OpXZ7ApZgvy7vdxcNioz7zIpR3jKVU%2BQq%2FqG5Aey2pwR%2BJf%2F8cL%2BkMPN5UD%2BR1cu3ECyocn4cxLmA9kdrQj2YGqw1fMPgB7YmKijRX8j20War8b2OZN8xXTLqtvQnykE790E0eu9hhQzteMieDT0DxOih3aBTJlsFXlju8RGrD8RyQy%2B6h1XsHdkf5Zv4BVkswSx5WmFVSM1Mr897eANs%2BnzBJD3lM5ZTsiW6Dw8ssACMKeq77wGOqUBEOlmfnJuYdgL2UEjg20%2B0VgKu%2BIr5ED%2F6KnTyVx9W6NyQWOy%2FHJlehoj9LM1zEJSIGT7oRNRDXRdtJ%2FVDCXTAj3dMq39bgxJ06dpRC5tOIFxZM7HywP0T7a9ppW0xDVPbD87HnpdU7m9HApc1UZJy64VTcVPW%2BDcb9taLnwbmG%2F%2B3MvaGr5fmKW98w405mIjfV6PKdwWF9tcMkj%2F6Ucpi4i%2BOz4L&X-Amz-Signature=b163d93b1350b4cdda71ab3f248b91208b0faa711722a7100656e9b8d0937b98&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663HHANNB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBn9SwAknTCBXXZrznZAYtPeyQTyum3zgazHbd9aLaJIAiEAhcrbNMqJ%2Bqqn3ZOoyRP0C2xlULYyv85spwFKekcxVnwqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHUk%2BcGqP67lfxocbircA5sRCir%2BZWzuPTnkmlncbVdg%2BKuWo9Yh5XYtkahhr%2BrVWZK9KvdYDerRBdM7SO5qFPxCj%2BgI99Tn%2BrGZoTDeOu7Wt%2BtILSqU2Vqhh%2FjNuDXROtlE9OoUjg3r8vtx2hSZ%2B44zImq%2BafNs25QhzK97hjCCV1egs2KI9CJhnV7voAzSk4ytFfI5h22BrMIU55ATa1OUR7IEpmsMHHc3AC00V2hdpMDmKNkgF6PjAo2eRBV%2B%2BxL677I5mxnPKwcTmQchEMhkdHcW6aDJEaosYGnY8SmmFSygPCgsanQpNEYyHoRrajKlkN6mzJFnaHW8fywcAV8ySx4nhneutv6OV%2BzwS3aMfwwrBJWOEXd3948retn69Fj%2BZELjg6QF%2F72HrAvQDd2zYL4oiOgWIx43OpXZ7ApZgvy7vdxcNioz7zIpR3jKVU%2BQq%2FqG5Aey2pwR%2BJf%2F8cL%2BkMPN5UD%2BR1cu3ECyocn4cxLmA9kdrQj2YGqw1fMPgB7YmKijRX8j20War8b2OZN8xXTLqtvQnykE790E0eu9hhQzteMieDT0DxOih3aBTJlsFXlju8RGrD8RyQy%2B6h1XsHdkf5Zv4BVkswSx5WmFVSM1Mr897eANs%2BnzBJD3lM5ZTsiW6Dw8ssACMKeq77wGOqUBEOlmfnJuYdgL2UEjg20%2B0VgKu%2BIr5ED%2F6KnTyVx9W6NyQWOy%2FHJlehoj9LM1zEJSIGT7oRNRDXRdtJ%2FVDCXTAj3dMq39bgxJ06dpRC5tOIFxZM7HywP0T7a9ppW0xDVPbD87HnpdU7m9HApc1UZJy64VTcVPW%2BDcb9taLnwbmG%2F%2B3MvaGr5fmKW98w405mIjfV6PKdwWF9tcMkj%2F6Ucpi4i%2BOz4L&X-Amz-Signature=14a6baf57c345787183b39b1dbb722f658aecedaa89517d4ca711080e5b581b2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663HHANNB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBn9SwAknTCBXXZrznZAYtPeyQTyum3zgazHbd9aLaJIAiEAhcrbNMqJ%2Bqqn3ZOoyRP0C2xlULYyv85spwFKekcxVnwqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHUk%2BcGqP67lfxocbircA5sRCir%2BZWzuPTnkmlncbVdg%2BKuWo9Yh5XYtkahhr%2BrVWZK9KvdYDerRBdM7SO5qFPxCj%2BgI99Tn%2BrGZoTDeOu7Wt%2BtILSqU2Vqhh%2FjNuDXROtlE9OoUjg3r8vtx2hSZ%2B44zImq%2BafNs25QhzK97hjCCV1egs2KI9CJhnV7voAzSk4ytFfI5h22BrMIU55ATa1OUR7IEpmsMHHc3AC00V2hdpMDmKNkgF6PjAo2eRBV%2B%2BxL677I5mxnPKwcTmQchEMhkdHcW6aDJEaosYGnY8SmmFSygPCgsanQpNEYyHoRrajKlkN6mzJFnaHW8fywcAV8ySx4nhneutv6OV%2BzwS3aMfwwrBJWOEXd3948retn69Fj%2BZELjg6QF%2F72HrAvQDd2zYL4oiOgWIx43OpXZ7ApZgvy7vdxcNioz7zIpR3jKVU%2BQq%2FqG5Aey2pwR%2BJf%2F8cL%2BkMPN5UD%2BR1cu3ECyocn4cxLmA9kdrQj2YGqw1fMPgB7YmKijRX8j20War8b2OZN8xXTLqtvQnykE790E0eu9hhQzteMieDT0DxOih3aBTJlsFXlju8RGrD8RyQy%2B6h1XsHdkf5Zv4BVkswSx5WmFVSM1Mr897eANs%2BnzBJD3lM5ZTsiW6Dw8ssACMKeq77wGOqUBEOlmfnJuYdgL2UEjg20%2B0VgKu%2BIr5ED%2F6KnTyVx9W6NyQWOy%2FHJlehoj9LM1zEJSIGT7oRNRDXRdtJ%2FVDCXTAj3dMq39bgxJ06dpRC5tOIFxZM7HywP0T7a9ppW0xDVPbD87HnpdU7m9HApc1UZJy64VTcVPW%2BDcb9taLnwbmG%2F%2B3MvaGr5fmKW98w405mIjfV6PKdwWF9tcMkj%2F6Ucpi4i%2BOz4L&X-Amz-Signature=f35f41bb9d8f9d57ec7fed7a770748fc12d355d310c0bc6759231a52f873b4a9&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663HHANNB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBn9SwAknTCBXXZrznZAYtPeyQTyum3zgazHbd9aLaJIAiEAhcrbNMqJ%2Bqqn3ZOoyRP0C2xlULYyv85spwFKekcxVnwqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHUk%2BcGqP67lfxocbircA5sRCir%2BZWzuPTnkmlncbVdg%2BKuWo9Yh5XYtkahhr%2BrVWZK9KvdYDerRBdM7SO5qFPxCj%2BgI99Tn%2BrGZoTDeOu7Wt%2BtILSqU2Vqhh%2FjNuDXROtlE9OoUjg3r8vtx2hSZ%2B44zImq%2BafNs25QhzK97hjCCV1egs2KI9CJhnV7voAzSk4ytFfI5h22BrMIU55ATa1OUR7IEpmsMHHc3AC00V2hdpMDmKNkgF6PjAo2eRBV%2B%2BxL677I5mxnPKwcTmQchEMhkdHcW6aDJEaosYGnY8SmmFSygPCgsanQpNEYyHoRrajKlkN6mzJFnaHW8fywcAV8ySx4nhneutv6OV%2BzwS3aMfwwrBJWOEXd3948retn69Fj%2BZELjg6QF%2F72HrAvQDd2zYL4oiOgWIx43OpXZ7ApZgvy7vdxcNioz7zIpR3jKVU%2BQq%2FqG5Aey2pwR%2BJf%2F8cL%2BkMPN5UD%2BR1cu3ECyocn4cxLmA9kdrQj2YGqw1fMPgB7YmKijRX8j20War8b2OZN8xXTLqtvQnykE790E0eu9hhQzteMieDT0DxOih3aBTJlsFXlju8RGrD8RyQy%2B6h1XsHdkf5Zv4BVkswSx5WmFVSM1Mr897eANs%2BnzBJD3lM5ZTsiW6Dw8ssACMKeq77wGOqUBEOlmfnJuYdgL2UEjg20%2B0VgKu%2BIr5ED%2F6KnTyVx9W6NyQWOy%2FHJlehoj9LM1zEJSIGT7oRNRDXRdtJ%2FVDCXTAj3dMq39bgxJ06dpRC5tOIFxZM7HywP0T7a9ppW0xDVPbD87HnpdU7m9HApc1UZJy64VTcVPW%2BDcb9taLnwbmG%2F%2B3MvaGr5fmKW98w405mIjfV6PKdwWF9tcMkj%2F6Ucpi4i%2BOz4L&X-Amz-Signature=c4b7ff543b698653e27d08d980a7ba6871a658ca85b32201d62c2bd0e2fba4fb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663HHANNB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBn9SwAknTCBXXZrznZAYtPeyQTyum3zgazHbd9aLaJIAiEAhcrbNMqJ%2Bqqn3ZOoyRP0C2xlULYyv85spwFKekcxVnwqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHUk%2BcGqP67lfxocbircA5sRCir%2BZWzuPTnkmlncbVdg%2BKuWo9Yh5XYtkahhr%2BrVWZK9KvdYDerRBdM7SO5qFPxCj%2BgI99Tn%2BrGZoTDeOu7Wt%2BtILSqU2Vqhh%2FjNuDXROtlE9OoUjg3r8vtx2hSZ%2B44zImq%2BafNs25QhzK97hjCCV1egs2KI9CJhnV7voAzSk4ytFfI5h22BrMIU55ATa1OUR7IEpmsMHHc3AC00V2hdpMDmKNkgF6PjAo2eRBV%2B%2BxL677I5mxnPKwcTmQchEMhkdHcW6aDJEaosYGnY8SmmFSygPCgsanQpNEYyHoRrajKlkN6mzJFnaHW8fywcAV8ySx4nhneutv6OV%2BzwS3aMfwwrBJWOEXd3948retn69Fj%2BZELjg6QF%2F72HrAvQDd2zYL4oiOgWIx43OpXZ7ApZgvy7vdxcNioz7zIpR3jKVU%2BQq%2FqG5Aey2pwR%2BJf%2F8cL%2BkMPN5UD%2BR1cu3ECyocn4cxLmA9kdrQj2YGqw1fMPgB7YmKijRX8j20War8b2OZN8xXTLqtvQnykE790E0eu9hhQzteMieDT0DxOih3aBTJlsFXlju8RGrD8RyQy%2B6h1XsHdkf5Zv4BVkswSx5WmFVSM1Mr897eANs%2BnzBJD3lM5ZTsiW6Dw8ssACMKeq77wGOqUBEOlmfnJuYdgL2UEjg20%2B0VgKu%2BIr5ED%2F6KnTyVx9W6NyQWOy%2FHJlehoj9LM1zEJSIGT7oRNRDXRdtJ%2FVDCXTAj3dMq39bgxJ06dpRC5tOIFxZM7HywP0T7a9ppW0xDVPbD87HnpdU7m9HApc1UZJy64VTcVPW%2BDcb9taLnwbmG%2F%2B3MvaGr5fmKW98w405mIjfV6PKdwWF9tcMkj%2F6Ucpi4i%2BOz4L&X-Amz-Signature=f66ffe3a48f3c61d9f35fb404254ed2276bba7c5b82f2498ba098bf6e31c129b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663HHANNB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBn9SwAknTCBXXZrznZAYtPeyQTyum3zgazHbd9aLaJIAiEAhcrbNMqJ%2Bqqn3ZOoyRP0C2xlULYyv85spwFKekcxVnwqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHUk%2BcGqP67lfxocbircA5sRCir%2BZWzuPTnkmlncbVdg%2BKuWo9Yh5XYtkahhr%2BrVWZK9KvdYDerRBdM7SO5qFPxCj%2BgI99Tn%2BrGZoTDeOu7Wt%2BtILSqU2Vqhh%2FjNuDXROtlE9OoUjg3r8vtx2hSZ%2B44zImq%2BafNs25QhzK97hjCCV1egs2KI9CJhnV7voAzSk4ytFfI5h22BrMIU55ATa1OUR7IEpmsMHHc3AC00V2hdpMDmKNkgF6PjAo2eRBV%2B%2BxL677I5mxnPKwcTmQchEMhkdHcW6aDJEaosYGnY8SmmFSygPCgsanQpNEYyHoRrajKlkN6mzJFnaHW8fywcAV8ySx4nhneutv6OV%2BzwS3aMfwwrBJWOEXd3948retn69Fj%2BZELjg6QF%2F72HrAvQDd2zYL4oiOgWIx43OpXZ7ApZgvy7vdxcNioz7zIpR3jKVU%2BQq%2FqG5Aey2pwR%2BJf%2F8cL%2BkMPN5UD%2BR1cu3ECyocn4cxLmA9kdrQj2YGqw1fMPgB7YmKijRX8j20War8b2OZN8xXTLqtvQnykE790E0eu9hhQzteMieDT0DxOih3aBTJlsFXlju8RGrD8RyQy%2B6h1XsHdkf5Zv4BVkswSx5WmFVSM1Mr897eANs%2BnzBJD3lM5ZTsiW6Dw8ssACMKeq77wGOqUBEOlmfnJuYdgL2UEjg20%2B0VgKu%2BIr5ED%2F6KnTyVx9W6NyQWOy%2FHJlehoj9LM1zEJSIGT7oRNRDXRdtJ%2FVDCXTAj3dMq39bgxJ06dpRC5tOIFxZM7HywP0T7a9ppW0xDVPbD87HnpdU7m9HApc1UZJy64VTcVPW%2BDcb9taLnwbmG%2F%2B3MvaGr5fmKW98w405mIjfV6PKdwWF9tcMkj%2F6Ucpi4i%2BOz4L&X-Amz-Signature=05823e65a5bbc636e53ba0c2ddeb58fdcdfb02e5ccbcf7855aa9128d17a4a67a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663HHANNB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBn9SwAknTCBXXZrznZAYtPeyQTyum3zgazHbd9aLaJIAiEAhcrbNMqJ%2Bqqn3ZOoyRP0C2xlULYyv85spwFKekcxVnwqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHUk%2BcGqP67lfxocbircA5sRCir%2BZWzuPTnkmlncbVdg%2BKuWo9Yh5XYtkahhr%2BrVWZK9KvdYDerRBdM7SO5qFPxCj%2BgI99Tn%2BrGZoTDeOu7Wt%2BtILSqU2Vqhh%2FjNuDXROtlE9OoUjg3r8vtx2hSZ%2B44zImq%2BafNs25QhzK97hjCCV1egs2KI9CJhnV7voAzSk4ytFfI5h22BrMIU55ATa1OUR7IEpmsMHHc3AC00V2hdpMDmKNkgF6PjAo2eRBV%2B%2BxL677I5mxnPKwcTmQchEMhkdHcW6aDJEaosYGnY8SmmFSygPCgsanQpNEYyHoRrajKlkN6mzJFnaHW8fywcAV8ySx4nhneutv6OV%2BzwS3aMfwwrBJWOEXd3948retn69Fj%2BZELjg6QF%2F72HrAvQDd2zYL4oiOgWIx43OpXZ7ApZgvy7vdxcNioz7zIpR3jKVU%2BQq%2FqG5Aey2pwR%2BJf%2F8cL%2BkMPN5UD%2BR1cu3ECyocn4cxLmA9kdrQj2YGqw1fMPgB7YmKijRX8j20War8b2OZN8xXTLqtvQnykE790E0eu9hhQzteMieDT0DxOih3aBTJlsFXlju8RGrD8RyQy%2B6h1XsHdkf5Zv4BVkswSx5WmFVSM1Mr897eANs%2BnzBJD3lM5ZTsiW6Dw8ssACMKeq77wGOqUBEOlmfnJuYdgL2UEjg20%2B0VgKu%2BIr5ED%2F6KnTyVx9W6NyQWOy%2FHJlehoj9LM1zEJSIGT7oRNRDXRdtJ%2FVDCXTAj3dMq39bgxJ06dpRC5tOIFxZM7HywP0T7a9ppW0xDVPbD87HnpdU7m9HApc1UZJy64VTcVPW%2BDcb9taLnwbmG%2F%2B3MvaGr5fmKW98w405mIjfV6PKdwWF9tcMkj%2F6Ucpi4i%2BOz4L&X-Amz-Signature=10acd697e23ddd33447b70f341886c18708d0ce4191aff47035100345c94d95e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DVUYP2P%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFM5DjctC7jpRdqhGZlWD6jMNvXU9uMCSe5QGyrM%2BXLiAiAX%2FaYQuYXH8RiAcAy3PVy2R80l5oJE1WXebazvrd5fwCqIBAit%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQjTn%2B1qhVJuiNivPKtwDsp5BKxfCUFFwouXirI%2BWJ9FwZP5GGtYahiSpqnhLieTPJsc4kDG82YTnFEfeBc6RjhlaBuPa5YPx0I9k4cEyu6biABxZkBys%2B%2Ftxy0EUYHVOAWKptlUUwPa7b0tV7sdAoi66Xw%2FGRdCk9hfJiP%2BJ1nk5KIMliEOTaptLYZiSQ2VLiQVgVOjqx0tIA9%2FWwN01ZaxEXIacYoB%2Bv4jJVdGvFSjdytMNVHxfzJvGKKQO8BMp%2FvBOGcUErZBOBquBxSBDaYDzc0YGoRDiO3f86QmhyqO4znq46bF1aMN8mhNMEDcP1naiMNgheDSD9qn0vCjY2vOsVUQsPrMBwjST1RcQcBQxGz%2BKS%2FCW3R7BizEYhLhl%2F7c9hDBwAlQbY%2BtLqdR6%2BaTKJHn8W%2B2u2Q6%2F3kjcdgn6jHHQogVZtnneb0wWm%2FMW9IYcnnKwSObklFSw1%2FI0ieByoKxF5NoHU0Ull2SewlqXO5lFxgX2AG4RTA8%2Ff%2FPPB3M0UoSV1frTBYCH4N6SEDn7Ybh0TojXXTlkMT%2FqboMOhQRXchH3YyKdicKTur1UtHOfEsoDsDhuB8bu9JdIrv6qTwXrWPojISICQTitM6GQTFIQzYUsUoD4Tt88ophUkrQjQV1jx4HYdSsw4anvvAY6pgF6%2BYJWPlIifm4HZs5ptAEScXk7mjMDbM7OGDidGEZgYz%2BDXak6wMpF88B3YyE%2FNeE00WCH%2BDrzLO6AkUFz%2Fd%2FHpbskNvwk2qIZgrxE8pmUzmo62X62d8K1dOAh1CXEb9n68%2BhIrIxWYEHjglLLcy4N%2BKmAS2E38r2a2HtIrdfCLbsy6xZeSMINebfvpPQK1Sz1YoflYX9JiZPsHBMBFges8JFnsQ%2Fj&X-Amz-Signature=790aa018de69ee7f55b8ae7843bed5076b36e043b1de268cab6b348c3a01a81d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DVUYP2P%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFM5DjctC7jpRdqhGZlWD6jMNvXU9uMCSe5QGyrM%2BXLiAiAX%2FaYQuYXH8RiAcAy3PVy2R80l5oJE1WXebazvrd5fwCqIBAit%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQjTn%2B1qhVJuiNivPKtwDsp5BKxfCUFFwouXirI%2BWJ9FwZP5GGtYahiSpqnhLieTPJsc4kDG82YTnFEfeBc6RjhlaBuPa5YPx0I9k4cEyu6biABxZkBys%2B%2Ftxy0EUYHVOAWKptlUUwPa7b0tV7sdAoi66Xw%2FGRdCk9hfJiP%2BJ1nk5KIMliEOTaptLYZiSQ2VLiQVgVOjqx0tIA9%2FWwN01ZaxEXIacYoB%2Bv4jJVdGvFSjdytMNVHxfzJvGKKQO8BMp%2FvBOGcUErZBOBquBxSBDaYDzc0YGoRDiO3f86QmhyqO4znq46bF1aMN8mhNMEDcP1naiMNgheDSD9qn0vCjY2vOsVUQsPrMBwjST1RcQcBQxGz%2BKS%2FCW3R7BizEYhLhl%2F7c9hDBwAlQbY%2BtLqdR6%2BaTKJHn8W%2B2u2Q6%2F3kjcdgn6jHHQogVZtnneb0wWm%2FMW9IYcnnKwSObklFSw1%2FI0ieByoKxF5NoHU0Ull2SewlqXO5lFxgX2AG4RTA8%2Ff%2FPPB3M0UoSV1frTBYCH4N6SEDn7Ybh0TojXXTlkMT%2FqboMOhQRXchH3YyKdicKTur1UtHOfEsoDsDhuB8bu9JdIrv6qTwXrWPojISICQTitM6GQTFIQzYUsUoD4Tt88ophUkrQjQV1jx4HYdSsw4anvvAY6pgF6%2BYJWPlIifm4HZs5ptAEScXk7mjMDbM7OGDidGEZgYz%2BDXak6wMpF88B3YyE%2FNeE00WCH%2BDrzLO6AkUFz%2Fd%2FHpbskNvwk2qIZgrxE8pmUzmo62X62d8K1dOAh1CXEb9n68%2BhIrIxWYEHjglLLcy4N%2BKmAS2E38r2a2HtIrdfCLbsy6xZeSMINebfvpPQK1Sz1YoflYX9JiZPsHBMBFges8JFnsQ%2Fj&X-Amz-Signature=a7709484bcd2ce9f329c7d7fc803eafd1fab2f2f0a05f9322a6c661ba4d0b894&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
