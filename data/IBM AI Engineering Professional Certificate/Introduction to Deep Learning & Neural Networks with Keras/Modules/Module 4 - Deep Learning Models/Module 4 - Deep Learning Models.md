

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQVK4KB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQCoMOF8qLFfvHT9hrYvTFFOG2P0peC37YwgF5gK4EPNowIgUGu6jyQgCv4zL9EDWMq8oPIuWQKokxWzB0Y1KxlzCfwq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDPo051adCH8Ib%2B3nVCrcA1zRA02WpLmnsT2Y6o3TrOZWmUqUKBkLdV0g4JG9epREOhaH%2FjB23mScDKmlhttsAITMFSkdppLqPbUuy77jB3n2oYhZSFkgC%2B8grnWHyeeL2DoecfRlsyynOx%2FW8inaxYn7ctMvKayEo7JPHWbMvOU6Zqm%2BlxXscNaEe1voDeD9xYbKi0oe%2BdpsdBEGUYohC%2Fk%2BjJym5Mk%2BMHt4T%2FMFJeHtSUEckN3RTl%2Fle2zccBZRW6kqPGFTOUWjBqvqbXvcN0jU1gvopVjS7JPVuD7rQJikmWn6XPxbsQ%2B9%2FSfs%2By%2FWsl6ym11lxa4SY%2BfLIyFMCgAHKlaC%2B7OO0xP13lTk82Btn0yhk3pMAJlWQXThHI2CPQrrfIBbAXpL%2BcweyS2TSNBaT5AYrOaRZTaoID55B4NEh7aMd4PGl3JxDb9jWAwJkBnlGEcQhEKF5zrQKjE1tB77pAeDU7I42Mh%2BlxG7%2B5OqU45BRv6kefuoCxuNhKuVv1sX8yCeT2BYApj8OS73QaUD2BYN%2FoYSvAxW5%2FBaftHxrc6XsMSfy4LMhwh1SVj0UMWrg0PQHl%2BwHjhPTbZJ%2FnEzx%2Bk3DYhr5COnZAOQrsbUPu8D4terb%2F1V1qLCvktSvfKJSts6kZ7hVZxxMLCdjr0GOqUBK4dOk2y1WFb2IEOh3pdYb5WmIdkPgkb7qoRr%2Fncy5XTd2LO9ankVgWCO1R4QkVr2elGPS7T2N5QUjfxSEjfOCH82Zsqv0DOnZCa0FF4vEptgj8pMT2Vx7VV0u%2BoRi8Okkz4HYiVr9oLmicdHXZsBswX%2FYtP5RITXufoAB0S0bugrG0pI%2BNtuGNxbCDWvKpF1%2FukDSSJF5bpZltqfqeme0F0tJ6T7&X-Amz-Signature=606c034c32d540dfe290a152da421fd3650a8f82bbd797e2db2761026bbdd200&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQVK4KB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQCoMOF8qLFfvHT9hrYvTFFOG2P0peC37YwgF5gK4EPNowIgUGu6jyQgCv4zL9EDWMq8oPIuWQKokxWzB0Y1KxlzCfwq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDPo051adCH8Ib%2B3nVCrcA1zRA02WpLmnsT2Y6o3TrOZWmUqUKBkLdV0g4JG9epREOhaH%2FjB23mScDKmlhttsAITMFSkdppLqPbUuy77jB3n2oYhZSFkgC%2B8grnWHyeeL2DoecfRlsyynOx%2FW8inaxYn7ctMvKayEo7JPHWbMvOU6Zqm%2BlxXscNaEe1voDeD9xYbKi0oe%2BdpsdBEGUYohC%2Fk%2BjJym5Mk%2BMHt4T%2FMFJeHtSUEckN3RTl%2Fle2zccBZRW6kqPGFTOUWjBqvqbXvcN0jU1gvopVjS7JPVuD7rQJikmWn6XPxbsQ%2B9%2FSfs%2By%2FWsl6ym11lxa4SY%2BfLIyFMCgAHKlaC%2B7OO0xP13lTk82Btn0yhk3pMAJlWQXThHI2CPQrrfIBbAXpL%2BcweyS2TSNBaT5AYrOaRZTaoID55B4NEh7aMd4PGl3JxDb9jWAwJkBnlGEcQhEKF5zrQKjE1tB77pAeDU7I42Mh%2BlxG7%2B5OqU45BRv6kefuoCxuNhKuVv1sX8yCeT2BYApj8OS73QaUD2BYN%2FoYSvAxW5%2FBaftHxrc6XsMSfy4LMhwh1SVj0UMWrg0PQHl%2BwHjhPTbZJ%2FnEzx%2Bk3DYhr5COnZAOQrsbUPu8D4terb%2F1V1qLCvktSvfKJSts6kZ7hVZxxMLCdjr0GOqUBK4dOk2y1WFb2IEOh3pdYb5WmIdkPgkb7qoRr%2Fncy5XTd2LO9ankVgWCO1R4QkVr2elGPS7T2N5QUjfxSEjfOCH82Zsqv0DOnZCa0FF4vEptgj8pMT2Vx7VV0u%2BoRi8Okkz4HYiVr9oLmicdHXZsBswX%2FYtP5RITXufoAB0S0bugrG0pI%2BNtuGNxbCDWvKpF1%2FukDSSJF5bpZltqfqeme0F0tJ6T7&X-Amz-Signature=8da09d4fc918bc4e377ee76cbf2c884df5abfb02836eac2a9b3c9f4047d34a7e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQVK4KB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQCoMOF8qLFfvHT9hrYvTFFOG2P0peC37YwgF5gK4EPNowIgUGu6jyQgCv4zL9EDWMq8oPIuWQKokxWzB0Y1KxlzCfwq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDPo051adCH8Ib%2B3nVCrcA1zRA02WpLmnsT2Y6o3TrOZWmUqUKBkLdV0g4JG9epREOhaH%2FjB23mScDKmlhttsAITMFSkdppLqPbUuy77jB3n2oYhZSFkgC%2B8grnWHyeeL2DoecfRlsyynOx%2FW8inaxYn7ctMvKayEo7JPHWbMvOU6Zqm%2BlxXscNaEe1voDeD9xYbKi0oe%2BdpsdBEGUYohC%2Fk%2BjJym5Mk%2BMHt4T%2FMFJeHtSUEckN3RTl%2Fle2zccBZRW6kqPGFTOUWjBqvqbXvcN0jU1gvopVjS7JPVuD7rQJikmWn6XPxbsQ%2B9%2FSfs%2By%2FWsl6ym11lxa4SY%2BfLIyFMCgAHKlaC%2B7OO0xP13lTk82Btn0yhk3pMAJlWQXThHI2CPQrrfIBbAXpL%2BcweyS2TSNBaT5AYrOaRZTaoID55B4NEh7aMd4PGl3JxDb9jWAwJkBnlGEcQhEKF5zrQKjE1tB77pAeDU7I42Mh%2BlxG7%2B5OqU45BRv6kefuoCxuNhKuVv1sX8yCeT2BYApj8OS73QaUD2BYN%2FoYSvAxW5%2FBaftHxrc6XsMSfy4LMhwh1SVj0UMWrg0PQHl%2BwHjhPTbZJ%2FnEzx%2Bk3DYhr5COnZAOQrsbUPu8D4terb%2F1V1qLCvktSvfKJSts6kZ7hVZxxMLCdjr0GOqUBK4dOk2y1WFb2IEOh3pdYb5WmIdkPgkb7qoRr%2Fncy5XTd2LO9ankVgWCO1R4QkVr2elGPS7T2N5QUjfxSEjfOCH82Zsqv0DOnZCa0FF4vEptgj8pMT2Vx7VV0u%2BoRi8Okkz4HYiVr9oLmicdHXZsBswX%2FYtP5RITXufoAB0S0bugrG0pI%2BNtuGNxbCDWvKpF1%2FukDSSJF5bpZltqfqeme0F0tJ6T7&X-Amz-Signature=4f2fdacb72be2555e5ccb4b33f731a84a1046670ce80ebaa14225d5113cabcbd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQVK4KB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQCoMOF8qLFfvHT9hrYvTFFOG2P0peC37YwgF5gK4EPNowIgUGu6jyQgCv4zL9EDWMq8oPIuWQKokxWzB0Y1KxlzCfwq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDPo051adCH8Ib%2B3nVCrcA1zRA02WpLmnsT2Y6o3TrOZWmUqUKBkLdV0g4JG9epREOhaH%2FjB23mScDKmlhttsAITMFSkdppLqPbUuy77jB3n2oYhZSFkgC%2B8grnWHyeeL2DoecfRlsyynOx%2FW8inaxYn7ctMvKayEo7JPHWbMvOU6Zqm%2BlxXscNaEe1voDeD9xYbKi0oe%2BdpsdBEGUYohC%2Fk%2BjJym5Mk%2BMHt4T%2FMFJeHtSUEckN3RTl%2Fle2zccBZRW6kqPGFTOUWjBqvqbXvcN0jU1gvopVjS7JPVuD7rQJikmWn6XPxbsQ%2B9%2FSfs%2By%2FWsl6ym11lxa4SY%2BfLIyFMCgAHKlaC%2B7OO0xP13lTk82Btn0yhk3pMAJlWQXThHI2CPQrrfIBbAXpL%2BcweyS2TSNBaT5AYrOaRZTaoID55B4NEh7aMd4PGl3JxDb9jWAwJkBnlGEcQhEKF5zrQKjE1tB77pAeDU7I42Mh%2BlxG7%2B5OqU45BRv6kefuoCxuNhKuVv1sX8yCeT2BYApj8OS73QaUD2BYN%2FoYSvAxW5%2FBaftHxrc6XsMSfy4LMhwh1SVj0UMWrg0PQHl%2BwHjhPTbZJ%2FnEzx%2Bk3DYhr5COnZAOQrsbUPu8D4terb%2F1V1qLCvktSvfKJSts6kZ7hVZxxMLCdjr0GOqUBK4dOk2y1WFb2IEOh3pdYb5WmIdkPgkb7qoRr%2Fncy5XTd2LO9ankVgWCO1R4QkVr2elGPS7T2N5QUjfxSEjfOCH82Zsqv0DOnZCa0FF4vEptgj8pMT2Vx7VV0u%2BoRi8Okkz4HYiVr9oLmicdHXZsBswX%2FYtP5RITXufoAB0S0bugrG0pI%2BNtuGNxbCDWvKpF1%2FukDSSJF5bpZltqfqeme0F0tJ6T7&X-Amz-Signature=3840865aa6d81962c96ce055de093a46e0debe565fe58e8db59c69e245dfc178&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQVK4KB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQCoMOF8qLFfvHT9hrYvTFFOG2P0peC37YwgF5gK4EPNowIgUGu6jyQgCv4zL9EDWMq8oPIuWQKokxWzB0Y1KxlzCfwq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDPo051adCH8Ib%2B3nVCrcA1zRA02WpLmnsT2Y6o3TrOZWmUqUKBkLdV0g4JG9epREOhaH%2FjB23mScDKmlhttsAITMFSkdppLqPbUuy77jB3n2oYhZSFkgC%2B8grnWHyeeL2DoecfRlsyynOx%2FW8inaxYn7ctMvKayEo7JPHWbMvOU6Zqm%2BlxXscNaEe1voDeD9xYbKi0oe%2BdpsdBEGUYohC%2Fk%2BjJym5Mk%2BMHt4T%2FMFJeHtSUEckN3RTl%2Fle2zccBZRW6kqPGFTOUWjBqvqbXvcN0jU1gvopVjS7JPVuD7rQJikmWn6XPxbsQ%2B9%2FSfs%2By%2FWsl6ym11lxa4SY%2BfLIyFMCgAHKlaC%2B7OO0xP13lTk82Btn0yhk3pMAJlWQXThHI2CPQrrfIBbAXpL%2BcweyS2TSNBaT5AYrOaRZTaoID55B4NEh7aMd4PGl3JxDb9jWAwJkBnlGEcQhEKF5zrQKjE1tB77pAeDU7I42Mh%2BlxG7%2B5OqU45BRv6kefuoCxuNhKuVv1sX8yCeT2BYApj8OS73QaUD2BYN%2FoYSvAxW5%2FBaftHxrc6XsMSfy4LMhwh1SVj0UMWrg0PQHl%2BwHjhPTbZJ%2FnEzx%2Bk3DYhr5COnZAOQrsbUPu8D4terb%2F1V1qLCvktSvfKJSts6kZ7hVZxxMLCdjr0GOqUBK4dOk2y1WFb2IEOh3pdYb5WmIdkPgkb7qoRr%2Fncy5XTd2LO9ankVgWCO1R4QkVr2elGPS7T2N5QUjfxSEjfOCH82Zsqv0DOnZCa0FF4vEptgj8pMT2Vx7VV0u%2BoRi8Okkz4HYiVr9oLmicdHXZsBswX%2FYtP5RITXufoAB0S0bugrG0pI%2BNtuGNxbCDWvKpF1%2FukDSSJF5bpZltqfqeme0F0tJ6T7&X-Amz-Signature=96a7ca56a3bd7a28de49069f2fb052cf495d400f034032defe6009792b913056&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQVK4KB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQCoMOF8qLFfvHT9hrYvTFFOG2P0peC37YwgF5gK4EPNowIgUGu6jyQgCv4zL9EDWMq8oPIuWQKokxWzB0Y1KxlzCfwq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDPo051adCH8Ib%2B3nVCrcA1zRA02WpLmnsT2Y6o3TrOZWmUqUKBkLdV0g4JG9epREOhaH%2FjB23mScDKmlhttsAITMFSkdppLqPbUuy77jB3n2oYhZSFkgC%2B8grnWHyeeL2DoecfRlsyynOx%2FW8inaxYn7ctMvKayEo7JPHWbMvOU6Zqm%2BlxXscNaEe1voDeD9xYbKi0oe%2BdpsdBEGUYohC%2Fk%2BjJym5Mk%2BMHt4T%2FMFJeHtSUEckN3RTl%2Fle2zccBZRW6kqPGFTOUWjBqvqbXvcN0jU1gvopVjS7JPVuD7rQJikmWn6XPxbsQ%2B9%2FSfs%2By%2FWsl6ym11lxa4SY%2BfLIyFMCgAHKlaC%2B7OO0xP13lTk82Btn0yhk3pMAJlWQXThHI2CPQrrfIBbAXpL%2BcweyS2TSNBaT5AYrOaRZTaoID55B4NEh7aMd4PGl3JxDb9jWAwJkBnlGEcQhEKF5zrQKjE1tB77pAeDU7I42Mh%2BlxG7%2B5OqU45BRv6kefuoCxuNhKuVv1sX8yCeT2BYApj8OS73QaUD2BYN%2FoYSvAxW5%2FBaftHxrc6XsMSfy4LMhwh1SVj0UMWrg0PQHl%2BwHjhPTbZJ%2FnEzx%2Bk3DYhr5COnZAOQrsbUPu8D4terb%2F1V1qLCvktSvfKJSts6kZ7hVZxxMLCdjr0GOqUBK4dOk2y1WFb2IEOh3pdYb5WmIdkPgkb7qoRr%2Fncy5XTd2LO9ankVgWCO1R4QkVr2elGPS7T2N5QUjfxSEjfOCH82Zsqv0DOnZCa0FF4vEptgj8pMT2Vx7VV0u%2BoRi8Okkz4HYiVr9oLmicdHXZsBswX%2FYtP5RITXufoAB0S0bugrG0pI%2BNtuGNxbCDWvKpF1%2FukDSSJF5bpZltqfqeme0F0tJ6T7&X-Amz-Signature=16c61c0350947b48c678c12eb737e5606d821afed0f6d5411f652946c35e68a4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQVK4KB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQCoMOF8qLFfvHT9hrYvTFFOG2P0peC37YwgF5gK4EPNowIgUGu6jyQgCv4zL9EDWMq8oPIuWQKokxWzB0Y1KxlzCfwq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDPo051adCH8Ib%2B3nVCrcA1zRA02WpLmnsT2Y6o3TrOZWmUqUKBkLdV0g4JG9epREOhaH%2FjB23mScDKmlhttsAITMFSkdppLqPbUuy77jB3n2oYhZSFkgC%2B8grnWHyeeL2DoecfRlsyynOx%2FW8inaxYn7ctMvKayEo7JPHWbMvOU6Zqm%2BlxXscNaEe1voDeD9xYbKi0oe%2BdpsdBEGUYohC%2Fk%2BjJym5Mk%2BMHt4T%2FMFJeHtSUEckN3RTl%2Fle2zccBZRW6kqPGFTOUWjBqvqbXvcN0jU1gvopVjS7JPVuD7rQJikmWn6XPxbsQ%2B9%2FSfs%2By%2FWsl6ym11lxa4SY%2BfLIyFMCgAHKlaC%2B7OO0xP13lTk82Btn0yhk3pMAJlWQXThHI2CPQrrfIBbAXpL%2BcweyS2TSNBaT5AYrOaRZTaoID55B4NEh7aMd4PGl3JxDb9jWAwJkBnlGEcQhEKF5zrQKjE1tB77pAeDU7I42Mh%2BlxG7%2B5OqU45BRv6kefuoCxuNhKuVv1sX8yCeT2BYApj8OS73QaUD2BYN%2FoYSvAxW5%2FBaftHxrc6XsMSfy4LMhwh1SVj0UMWrg0PQHl%2BwHjhPTbZJ%2FnEzx%2Bk3DYhr5COnZAOQrsbUPu8D4terb%2F1V1qLCvktSvfKJSts6kZ7hVZxxMLCdjr0GOqUBK4dOk2y1WFb2IEOh3pdYb5WmIdkPgkb7qoRr%2Fncy5XTd2LO9ankVgWCO1R4QkVr2elGPS7T2N5QUjfxSEjfOCH82Zsqv0DOnZCa0FF4vEptgj8pMT2Vx7VV0u%2BoRi8Okkz4HYiVr9oLmicdHXZsBswX%2FYtP5RITXufoAB0S0bugrG0pI%2BNtuGNxbCDWvKpF1%2FukDSSJF5bpZltqfqeme0F0tJ6T7&X-Amz-Signature=5d5caa7d6962436584e2be39439a0cedd57e822f9b7a9e0f1eff3df55ea68534&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQVK4KB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQCoMOF8qLFfvHT9hrYvTFFOG2P0peC37YwgF5gK4EPNowIgUGu6jyQgCv4zL9EDWMq8oPIuWQKokxWzB0Y1KxlzCfwq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDPo051adCH8Ib%2B3nVCrcA1zRA02WpLmnsT2Y6o3TrOZWmUqUKBkLdV0g4JG9epREOhaH%2FjB23mScDKmlhttsAITMFSkdppLqPbUuy77jB3n2oYhZSFkgC%2B8grnWHyeeL2DoecfRlsyynOx%2FW8inaxYn7ctMvKayEo7JPHWbMvOU6Zqm%2BlxXscNaEe1voDeD9xYbKi0oe%2BdpsdBEGUYohC%2Fk%2BjJym5Mk%2BMHt4T%2FMFJeHtSUEckN3RTl%2Fle2zccBZRW6kqPGFTOUWjBqvqbXvcN0jU1gvopVjS7JPVuD7rQJikmWn6XPxbsQ%2B9%2FSfs%2By%2FWsl6ym11lxa4SY%2BfLIyFMCgAHKlaC%2B7OO0xP13lTk82Btn0yhk3pMAJlWQXThHI2CPQrrfIBbAXpL%2BcweyS2TSNBaT5AYrOaRZTaoID55B4NEh7aMd4PGl3JxDb9jWAwJkBnlGEcQhEKF5zrQKjE1tB77pAeDU7I42Mh%2BlxG7%2B5OqU45BRv6kefuoCxuNhKuVv1sX8yCeT2BYApj8OS73QaUD2BYN%2FoYSvAxW5%2FBaftHxrc6XsMSfy4LMhwh1SVj0UMWrg0PQHl%2BwHjhPTbZJ%2FnEzx%2Bk3DYhr5COnZAOQrsbUPu8D4terb%2F1V1qLCvktSvfKJSts6kZ7hVZxxMLCdjr0GOqUBK4dOk2y1WFb2IEOh3pdYb5WmIdkPgkb7qoRr%2Fncy5XTd2LO9ankVgWCO1R4QkVr2elGPS7T2N5QUjfxSEjfOCH82Zsqv0DOnZCa0FF4vEptgj8pMT2Vx7VV0u%2BoRi8Okkz4HYiVr9oLmicdHXZsBswX%2FYtP5RITXufoAB0S0bugrG0pI%2BNtuGNxbCDWvKpF1%2FukDSSJF5bpZltqfqeme0F0tJ6T7&X-Amz-Signature=a1d230a71e1ae08410d0c5ade16cc23d7361da5733937d5811236b598ac665bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQVK4KB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQCoMOF8qLFfvHT9hrYvTFFOG2P0peC37YwgF5gK4EPNowIgUGu6jyQgCv4zL9EDWMq8oPIuWQKokxWzB0Y1KxlzCfwq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDPo051adCH8Ib%2B3nVCrcA1zRA02WpLmnsT2Y6o3TrOZWmUqUKBkLdV0g4JG9epREOhaH%2FjB23mScDKmlhttsAITMFSkdppLqPbUuy77jB3n2oYhZSFkgC%2B8grnWHyeeL2DoecfRlsyynOx%2FW8inaxYn7ctMvKayEo7JPHWbMvOU6Zqm%2BlxXscNaEe1voDeD9xYbKi0oe%2BdpsdBEGUYohC%2Fk%2BjJym5Mk%2BMHt4T%2FMFJeHtSUEckN3RTl%2Fle2zccBZRW6kqPGFTOUWjBqvqbXvcN0jU1gvopVjS7JPVuD7rQJikmWn6XPxbsQ%2B9%2FSfs%2By%2FWsl6ym11lxa4SY%2BfLIyFMCgAHKlaC%2B7OO0xP13lTk82Btn0yhk3pMAJlWQXThHI2CPQrrfIBbAXpL%2BcweyS2TSNBaT5AYrOaRZTaoID55B4NEh7aMd4PGl3JxDb9jWAwJkBnlGEcQhEKF5zrQKjE1tB77pAeDU7I42Mh%2BlxG7%2B5OqU45BRv6kefuoCxuNhKuVv1sX8yCeT2BYApj8OS73QaUD2BYN%2FoYSvAxW5%2FBaftHxrc6XsMSfy4LMhwh1SVj0UMWrg0PQHl%2BwHjhPTbZJ%2FnEzx%2Bk3DYhr5COnZAOQrsbUPu8D4terb%2F1V1qLCvktSvfKJSts6kZ7hVZxxMLCdjr0GOqUBK4dOk2y1WFb2IEOh3pdYb5WmIdkPgkb7qoRr%2Fncy5XTd2LO9ankVgWCO1R4QkVr2elGPS7T2N5QUjfxSEjfOCH82Zsqv0DOnZCa0FF4vEptgj8pMT2Vx7VV0u%2BoRi8Okkz4HYiVr9oLmicdHXZsBswX%2FYtP5RITXufoAB0S0bugrG0pI%2BNtuGNxbCDWvKpF1%2FukDSSJF5bpZltqfqeme0F0tJ6T7&X-Amz-Signature=3f7ead09e6b19b8212591695ab5325e964b45aac42f3f1730e1821e80c947751&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662P3LWJJE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIDxeE5Sk17e2iLrRSQHKF5xBNe3ShY0B%2Bo%2F23cUtOlHhAiEAicTvjTZxTr3ZHCQViNsQMgjZOWeuL1Sth%2BToRRS5wZgq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDKg4VIb8TlERRqyJwCrcA7S%2Bdqyjj8XBtH6NmBqBzKgZurYZzuUFaN1cm0lG6CtrlOIHqfXSP6wPJ4Yx5nPNe%2FCFr3t9EMNbZjSxoSBP5TohNd7g73bEgOTNpM4erNHyYzeSOS3yqm0H5VLpaLBT2vmrTyR3MiAnONJ3UEKhrJgLT7oxls6hUOV0QqeaoZQIvUdUISt5rvSeqQUODhaznAAY%2FcGa%2FQSYuULYIhrS1CY6INp5nalcmqWXwUVoHHA0rtjHmONWJ868OpMfWL6yfp42LDOPsEr4CmoHbhH2iuo10uQg5h8VHdrnWcyvq%2F4PvcRbptlrai1gDxot4rsflbAqIjxaBFdmj2kMo6%2FBeDVTjw6gheKy%2F8itqY5r0cX%2B7xNYA%2F7%2BsZS34J0yZP9Q44sVBGeXGeb2fEJk589ChTzFZIAZ0EoNbExaAB7fxd%2FyxMieWtaOxoVQg%2Bb1%2BYlKuhPt3%2BidEzYkSEtFZYCv%2FxCtUBoqOxYz4lcGytH8jb%2BlLdZ0B8YMRLu2HUYAiuyItWGcZY6tip%2BkWOlyRcYHlloHnXwlgzQFOh%2BFMnFT%2Bzq%2FtWzgYP6mj3I5KbFxk%2Fks5QMMsnIK0osTEw4P7v2bzSWgNrTw2DxXpBIk4%2FuyQNrFdrZ%2FNUX07U6y%2FLfHMNSdjr0GOqUB4xBqVFl3aSi%2BA8OgkhOu2CQ1hUn6nSbOMoZQxwDTZKvNhwNcbPfKun0dkTM0d8Wc2dmqiefnePxOLC3n04%2F2X8aDzQV2HPF%2FWQWK0QqOjw34amiY6tGPnIevjpfse0pLJGv7z0cznLyvv4ZWYwyDY6g4PJXQxDGTTlIk%2BEBN4Uq2DSon8y59yGXXHeStw3pJpQxohyOODH1ZgSBbafDH8emIqfdj&X-Amz-Signature=30e44c0d54e330288961ae92d3837264d01cc0929faed4e21f71dbaf73665787&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662P3LWJJE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIDxeE5Sk17e2iLrRSQHKF5xBNe3ShY0B%2Bo%2F23cUtOlHhAiEAicTvjTZxTr3ZHCQViNsQMgjZOWeuL1Sth%2BToRRS5wZgq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDKg4VIb8TlERRqyJwCrcA7S%2Bdqyjj8XBtH6NmBqBzKgZurYZzuUFaN1cm0lG6CtrlOIHqfXSP6wPJ4Yx5nPNe%2FCFr3t9EMNbZjSxoSBP5TohNd7g73bEgOTNpM4erNHyYzeSOS3yqm0H5VLpaLBT2vmrTyR3MiAnONJ3UEKhrJgLT7oxls6hUOV0QqeaoZQIvUdUISt5rvSeqQUODhaznAAY%2FcGa%2FQSYuULYIhrS1CY6INp5nalcmqWXwUVoHHA0rtjHmONWJ868OpMfWL6yfp42LDOPsEr4CmoHbhH2iuo10uQg5h8VHdrnWcyvq%2F4PvcRbptlrai1gDxot4rsflbAqIjxaBFdmj2kMo6%2FBeDVTjw6gheKy%2F8itqY5r0cX%2B7xNYA%2F7%2BsZS34J0yZP9Q44sVBGeXGeb2fEJk589ChTzFZIAZ0EoNbExaAB7fxd%2FyxMieWtaOxoVQg%2Bb1%2BYlKuhPt3%2BidEzYkSEtFZYCv%2FxCtUBoqOxYz4lcGytH8jb%2BlLdZ0B8YMRLu2HUYAiuyItWGcZY6tip%2BkWOlyRcYHlloHnXwlgzQFOh%2BFMnFT%2Bzq%2FtWzgYP6mj3I5KbFxk%2Fks5QMMsnIK0osTEw4P7v2bzSWgNrTw2DxXpBIk4%2FuyQNrFdrZ%2FNUX07U6y%2FLfHMNSdjr0GOqUB4xBqVFl3aSi%2BA8OgkhOu2CQ1hUn6nSbOMoZQxwDTZKvNhwNcbPfKun0dkTM0d8Wc2dmqiefnePxOLC3n04%2F2X8aDzQV2HPF%2FWQWK0QqOjw34amiY6tGPnIevjpfse0pLJGv7z0cznLyvv4ZWYwyDY6g4PJXQxDGTTlIk%2BEBN4Uq2DSon8y59yGXXHeStw3pJpQxohyOODH1ZgSBbafDH8emIqfdj&X-Amz-Signature=daddf9ee738fc365f5a4afae954f30e14cbe8f237e7314665e72df6fbff625fb&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
