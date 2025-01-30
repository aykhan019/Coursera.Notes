

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y32RGQCG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHSTNUdwnn9yrS8FrZ2nRAPA3xX8h61kEfwYSSsyHGlFAiEAn5W%2BM%2BtJwsoJFHw7jUcQch0BA9igMojqqnxuRtdjMnUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPYtHHA3Px%2BxUZBWBircA6fQPyIndnH2KnKRZnKgt45qo%2FPJ0OiedKLbVoegRNEwwZTd%2FYaOIv7Ua%2BsNFaOZ8KsReENU7lLtaLJdT4Ac3DxmAfKUaLPrY8sjCkDXohZ6DMrO7%2B6GSsnLhD8CGPJ409y7nCk82vE9UOArDt07a32Qq4clPbi5xV7hwVERjtbSoODIbH5esDeYm7iR9MwS8vQlp%2FfEZ%2BC60XkDqab1Ls%2FcA2GC%2B9P9kwzQyP%2FK4bikNFlOeVrL5k0Aol3RhpRzzlZVqdmnHfSQjVK4zl45wdtkcfBnRgLadiezTKqUcZQ7RquePMlMJXwUfsACJw9plra57ObBZ7jTXYSkwRHPw0%2FgUVxI%2FtukspadObwwtFAkMIjPEIJs1MsofhwmgVEz%2B8DP400u8WivA6%2Fs%2BXKbtOzneBLTbFsT%2B%2FhMCZEhF2Y92hpUkkUNymrdLhm7cjwx8TMPS%2Fh%2FZpeJtlkOpoHE5SkyjB6Zj%2B0P%2B01F%2FoTdEC856dG2kKdcRhqPI4KH%2BdjJSYMbeJbLMFxZ23924geEPK3xjFweBN6AjLsaFoud89jnb8kzjrpb2tOWPLQiY7lG1Lg7sESn1Ote5Hr0XTcEmnR8GAYH0749z1S7qNd54A553JzbSDocSllclqReMIyo7bwGOqUB1PcowqOpA0ecuWtc8ldYPgNg9eFF1b1Nf8g3M22YIayq9WQ1JNnuH1bwHfXdRAir%2BBycT7d%2F1QT27SRAf%2BQLsSG1mMqy9qa%2BkiXZvTCpcQUJdMzJrlY1oiDZ%2FOcHiaiOguoFIy7p7LbKDQnhIHHQbeTY1YSbrV%2BDWwIZwg2qlmV%2BGYu4KOuGFqCxdmMK8f4AL6yeW0TzE%2FSuU004Xd85UlvXURxb&X-Amz-Signature=1401019a190599b86a539f12b58a79288c5d05e84a745dd6d14c910eeffdb202&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y32RGQCG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHSTNUdwnn9yrS8FrZ2nRAPA3xX8h61kEfwYSSsyHGlFAiEAn5W%2BM%2BtJwsoJFHw7jUcQch0BA9igMojqqnxuRtdjMnUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPYtHHA3Px%2BxUZBWBircA6fQPyIndnH2KnKRZnKgt45qo%2FPJ0OiedKLbVoegRNEwwZTd%2FYaOIv7Ua%2BsNFaOZ8KsReENU7lLtaLJdT4Ac3DxmAfKUaLPrY8sjCkDXohZ6DMrO7%2B6GSsnLhD8CGPJ409y7nCk82vE9UOArDt07a32Qq4clPbi5xV7hwVERjtbSoODIbH5esDeYm7iR9MwS8vQlp%2FfEZ%2BC60XkDqab1Ls%2FcA2GC%2B9P9kwzQyP%2FK4bikNFlOeVrL5k0Aol3RhpRzzlZVqdmnHfSQjVK4zl45wdtkcfBnRgLadiezTKqUcZQ7RquePMlMJXwUfsACJw9plra57ObBZ7jTXYSkwRHPw0%2FgUVxI%2FtukspadObwwtFAkMIjPEIJs1MsofhwmgVEz%2B8DP400u8WivA6%2Fs%2BXKbtOzneBLTbFsT%2B%2FhMCZEhF2Y92hpUkkUNymrdLhm7cjwx8TMPS%2Fh%2FZpeJtlkOpoHE5SkyjB6Zj%2B0P%2B01F%2FoTdEC856dG2kKdcRhqPI4KH%2BdjJSYMbeJbLMFxZ23924geEPK3xjFweBN6AjLsaFoud89jnb8kzjrpb2tOWPLQiY7lG1Lg7sESn1Ote5Hr0XTcEmnR8GAYH0749z1S7qNd54A553JzbSDocSllclqReMIyo7bwGOqUB1PcowqOpA0ecuWtc8ldYPgNg9eFF1b1Nf8g3M22YIayq9WQ1JNnuH1bwHfXdRAir%2BBycT7d%2F1QT27SRAf%2BQLsSG1mMqy9qa%2BkiXZvTCpcQUJdMzJrlY1oiDZ%2FOcHiaiOguoFIy7p7LbKDQnhIHHQbeTY1YSbrV%2BDWwIZwg2qlmV%2BGYu4KOuGFqCxdmMK8f4AL6yeW0TzE%2FSuU004Xd85UlvXURxb&X-Amz-Signature=0374bd0481f7901d2bbf19b7c0c2e293918b9a9e395b2f14535241e856210c93&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y32RGQCG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHSTNUdwnn9yrS8FrZ2nRAPA3xX8h61kEfwYSSsyHGlFAiEAn5W%2BM%2BtJwsoJFHw7jUcQch0BA9igMojqqnxuRtdjMnUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPYtHHA3Px%2BxUZBWBircA6fQPyIndnH2KnKRZnKgt45qo%2FPJ0OiedKLbVoegRNEwwZTd%2FYaOIv7Ua%2BsNFaOZ8KsReENU7lLtaLJdT4Ac3DxmAfKUaLPrY8sjCkDXohZ6DMrO7%2B6GSsnLhD8CGPJ409y7nCk82vE9UOArDt07a32Qq4clPbi5xV7hwVERjtbSoODIbH5esDeYm7iR9MwS8vQlp%2FfEZ%2BC60XkDqab1Ls%2FcA2GC%2B9P9kwzQyP%2FK4bikNFlOeVrL5k0Aol3RhpRzzlZVqdmnHfSQjVK4zl45wdtkcfBnRgLadiezTKqUcZQ7RquePMlMJXwUfsACJw9plra57ObBZ7jTXYSkwRHPw0%2FgUVxI%2FtukspadObwwtFAkMIjPEIJs1MsofhwmgVEz%2B8DP400u8WivA6%2Fs%2BXKbtOzneBLTbFsT%2B%2FhMCZEhF2Y92hpUkkUNymrdLhm7cjwx8TMPS%2Fh%2FZpeJtlkOpoHE5SkyjB6Zj%2B0P%2B01F%2FoTdEC856dG2kKdcRhqPI4KH%2BdjJSYMbeJbLMFxZ23924geEPK3xjFweBN6AjLsaFoud89jnb8kzjrpb2tOWPLQiY7lG1Lg7sESn1Ote5Hr0XTcEmnR8GAYH0749z1S7qNd54A553JzbSDocSllclqReMIyo7bwGOqUB1PcowqOpA0ecuWtc8ldYPgNg9eFF1b1Nf8g3M22YIayq9WQ1JNnuH1bwHfXdRAir%2BBycT7d%2F1QT27SRAf%2BQLsSG1mMqy9qa%2BkiXZvTCpcQUJdMzJrlY1oiDZ%2FOcHiaiOguoFIy7p7LbKDQnhIHHQbeTY1YSbrV%2BDWwIZwg2qlmV%2BGYu4KOuGFqCxdmMK8f4AL6yeW0TzE%2FSuU004Xd85UlvXURxb&X-Amz-Signature=8f190c66c82780546e686b1cb2da2864461bc6df158ec58360a3b99d7e065f07&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y32RGQCG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHSTNUdwnn9yrS8FrZ2nRAPA3xX8h61kEfwYSSsyHGlFAiEAn5W%2BM%2BtJwsoJFHw7jUcQch0BA9igMojqqnxuRtdjMnUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPYtHHA3Px%2BxUZBWBircA6fQPyIndnH2KnKRZnKgt45qo%2FPJ0OiedKLbVoegRNEwwZTd%2FYaOIv7Ua%2BsNFaOZ8KsReENU7lLtaLJdT4Ac3DxmAfKUaLPrY8sjCkDXohZ6DMrO7%2B6GSsnLhD8CGPJ409y7nCk82vE9UOArDt07a32Qq4clPbi5xV7hwVERjtbSoODIbH5esDeYm7iR9MwS8vQlp%2FfEZ%2BC60XkDqab1Ls%2FcA2GC%2B9P9kwzQyP%2FK4bikNFlOeVrL5k0Aol3RhpRzzlZVqdmnHfSQjVK4zl45wdtkcfBnRgLadiezTKqUcZQ7RquePMlMJXwUfsACJw9plra57ObBZ7jTXYSkwRHPw0%2FgUVxI%2FtukspadObwwtFAkMIjPEIJs1MsofhwmgVEz%2B8DP400u8WivA6%2Fs%2BXKbtOzneBLTbFsT%2B%2FhMCZEhF2Y92hpUkkUNymrdLhm7cjwx8TMPS%2Fh%2FZpeJtlkOpoHE5SkyjB6Zj%2B0P%2B01F%2FoTdEC856dG2kKdcRhqPI4KH%2BdjJSYMbeJbLMFxZ23924geEPK3xjFweBN6AjLsaFoud89jnb8kzjrpb2tOWPLQiY7lG1Lg7sESn1Ote5Hr0XTcEmnR8GAYH0749z1S7qNd54A553JzbSDocSllclqReMIyo7bwGOqUB1PcowqOpA0ecuWtc8ldYPgNg9eFF1b1Nf8g3M22YIayq9WQ1JNnuH1bwHfXdRAir%2BBycT7d%2F1QT27SRAf%2BQLsSG1mMqy9qa%2BkiXZvTCpcQUJdMzJrlY1oiDZ%2FOcHiaiOguoFIy7p7LbKDQnhIHHQbeTY1YSbrV%2BDWwIZwg2qlmV%2BGYu4KOuGFqCxdmMK8f4AL6yeW0TzE%2FSuU004Xd85UlvXURxb&X-Amz-Signature=fdd488c8233452bf4880266fde474424b526625d9c590d79e3adfa890b4d787e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y32RGQCG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHSTNUdwnn9yrS8FrZ2nRAPA3xX8h61kEfwYSSsyHGlFAiEAn5W%2BM%2BtJwsoJFHw7jUcQch0BA9igMojqqnxuRtdjMnUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPYtHHA3Px%2BxUZBWBircA6fQPyIndnH2KnKRZnKgt45qo%2FPJ0OiedKLbVoegRNEwwZTd%2FYaOIv7Ua%2BsNFaOZ8KsReENU7lLtaLJdT4Ac3DxmAfKUaLPrY8sjCkDXohZ6DMrO7%2B6GSsnLhD8CGPJ409y7nCk82vE9UOArDt07a32Qq4clPbi5xV7hwVERjtbSoODIbH5esDeYm7iR9MwS8vQlp%2FfEZ%2BC60XkDqab1Ls%2FcA2GC%2B9P9kwzQyP%2FK4bikNFlOeVrL5k0Aol3RhpRzzlZVqdmnHfSQjVK4zl45wdtkcfBnRgLadiezTKqUcZQ7RquePMlMJXwUfsACJw9plra57ObBZ7jTXYSkwRHPw0%2FgUVxI%2FtukspadObwwtFAkMIjPEIJs1MsofhwmgVEz%2B8DP400u8WivA6%2Fs%2BXKbtOzneBLTbFsT%2B%2FhMCZEhF2Y92hpUkkUNymrdLhm7cjwx8TMPS%2Fh%2FZpeJtlkOpoHE5SkyjB6Zj%2B0P%2B01F%2FoTdEC856dG2kKdcRhqPI4KH%2BdjJSYMbeJbLMFxZ23924geEPK3xjFweBN6AjLsaFoud89jnb8kzjrpb2tOWPLQiY7lG1Lg7sESn1Ote5Hr0XTcEmnR8GAYH0749z1S7qNd54A553JzbSDocSllclqReMIyo7bwGOqUB1PcowqOpA0ecuWtc8ldYPgNg9eFF1b1Nf8g3M22YIayq9WQ1JNnuH1bwHfXdRAir%2BBycT7d%2F1QT27SRAf%2BQLsSG1mMqy9qa%2BkiXZvTCpcQUJdMzJrlY1oiDZ%2FOcHiaiOguoFIy7p7LbKDQnhIHHQbeTY1YSbrV%2BDWwIZwg2qlmV%2BGYu4KOuGFqCxdmMK8f4AL6yeW0TzE%2FSuU004Xd85UlvXURxb&X-Amz-Signature=6baade5ec66131fea0790f4a9fe3c4ffcea98e0ca03778463eafc8986c7a7196&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y32RGQCG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHSTNUdwnn9yrS8FrZ2nRAPA3xX8h61kEfwYSSsyHGlFAiEAn5W%2BM%2BtJwsoJFHw7jUcQch0BA9igMojqqnxuRtdjMnUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPYtHHA3Px%2BxUZBWBircA6fQPyIndnH2KnKRZnKgt45qo%2FPJ0OiedKLbVoegRNEwwZTd%2FYaOIv7Ua%2BsNFaOZ8KsReENU7lLtaLJdT4Ac3DxmAfKUaLPrY8sjCkDXohZ6DMrO7%2B6GSsnLhD8CGPJ409y7nCk82vE9UOArDt07a32Qq4clPbi5xV7hwVERjtbSoODIbH5esDeYm7iR9MwS8vQlp%2FfEZ%2BC60XkDqab1Ls%2FcA2GC%2B9P9kwzQyP%2FK4bikNFlOeVrL5k0Aol3RhpRzzlZVqdmnHfSQjVK4zl45wdtkcfBnRgLadiezTKqUcZQ7RquePMlMJXwUfsACJw9plra57ObBZ7jTXYSkwRHPw0%2FgUVxI%2FtukspadObwwtFAkMIjPEIJs1MsofhwmgVEz%2B8DP400u8WivA6%2Fs%2BXKbtOzneBLTbFsT%2B%2FhMCZEhF2Y92hpUkkUNymrdLhm7cjwx8TMPS%2Fh%2FZpeJtlkOpoHE5SkyjB6Zj%2B0P%2B01F%2FoTdEC856dG2kKdcRhqPI4KH%2BdjJSYMbeJbLMFxZ23924geEPK3xjFweBN6AjLsaFoud89jnb8kzjrpb2tOWPLQiY7lG1Lg7sESn1Ote5Hr0XTcEmnR8GAYH0749z1S7qNd54A553JzbSDocSllclqReMIyo7bwGOqUB1PcowqOpA0ecuWtc8ldYPgNg9eFF1b1Nf8g3M22YIayq9WQ1JNnuH1bwHfXdRAir%2BBycT7d%2F1QT27SRAf%2BQLsSG1mMqy9qa%2BkiXZvTCpcQUJdMzJrlY1oiDZ%2FOcHiaiOguoFIy7p7LbKDQnhIHHQbeTY1YSbrV%2BDWwIZwg2qlmV%2BGYu4KOuGFqCxdmMK8f4AL6yeW0TzE%2FSuU004Xd85UlvXURxb&X-Amz-Signature=5aaf293d8bd882fae8a40d3407d539bee9db3882c239d7c9d540d0368fd8b31c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y32RGQCG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHSTNUdwnn9yrS8FrZ2nRAPA3xX8h61kEfwYSSsyHGlFAiEAn5W%2BM%2BtJwsoJFHw7jUcQch0BA9igMojqqnxuRtdjMnUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPYtHHA3Px%2BxUZBWBircA6fQPyIndnH2KnKRZnKgt45qo%2FPJ0OiedKLbVoegRNEwwZTd%2FYaOIv7Ua%2BsNFaOZ8KsReENU7lLtaLJdT4Ac3DxmAfKUaLPrY8sjCkDXohZ6DMrO7%2B6GSsnLhD8CGPJ409y7nCk82vE9UOArDt07a32Qq4clPbi5xV7hwVERjtbSoODIbH5esDeYm7iR9MwS8vQlp%2FfEZ%2BC60XkDqab1Ls%2FcA2GC%2B9P9kwzQyP%2FK4bikNFlOeVrL5k0Aol3RhpRzzlZVqdmnHfSQjVK4zl45wdtkcfBnRgLadiezTKqUcZQ7RquePMlMJXwUfsACJw9plra57ObBZ7jTXYSkwRHPw0%2FgUVxI%2FtukspadObwwtFAkMIjPEIJs1MsofhwmgVEz%2B8DP400u8WivA6%2Fs%2BXKbtOzneBLTbFsT%2B%2FhMCZEhF2Y92hpUkkUNymrdLhm7cjwx8TMPS%2Fh%2FZpeJtlkOpoHE5SkyjB6Zj%2B0P%2B01F%2FoTdEC856dG2kKdcRhqPI4KH%2BdjJSYMbeJbLMFxZ23924geEPK3xjFweBN6AjLsaFoud89jnb8kzjrpb2tOWPLQiY7lG1Lg7sESn1Ote5Hr0XTcEmnR8GAYH0749z1S7qNd54A553JzbSDocSllclqReMIyo7bwGOqUB1PcowqOpA0ecuWtc8ldYPgNg9eFF1b1Nf8g3M22YIayq9WQ1JNnuH1bwHfXdRAir%2BBycT7d%2F1QT27SRAf%2BQLsSG1mMqy9qa%2BkiXZvTCpcQUJdMzJrlY1oiDZ%2FOcHiaiOguoFIy7p7LbKDQnhIHHQbeTY1YSbrV%2BDWwIZwg2qlmV%2BGYu4KOuGFqCxdmMK8f4AL6yeW0TzE%2FSuU004Xd85UlvXURxb&X-Amz-Signature=7bf8d45b0188decdab632f699804cd8f872d71bd847f22b532711a2771815a33&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y32RGQCG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHSTNUdwnn9yrS8FrZ2nRAPA3xX8h61kEfwYSSsyHGlFAiEAn5W%2BM%2BtJwsoJFHw7jUcQch0BA9igMojqqnxuRtdjMnUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPYtHHA3Px%2BxUZBWBircA6fQPyIndnH2KnKRZnKgt45qo%2FPJ0OiedKLbVoegRNEwwZTd%2FYaOIv7Ua%2BsNFaOZ8KsReENU7lLtaLJdT4Ac3DxmAfKUaLPrY8sjCkDXohZ6DMrO7%2B6GSsnLhD8CGPJ409y7nCk82vE9UOArDt07a32Qq4clPbi5xV7hwVERjtbSoODIbH5esDeYm7iR9MwS8vQlp%2FfEZ%2BC60XkDqab1Ls%2FcA2GC%2B9P9kwzQyP%2FK4bikNFlOeVrL5k0Aol3RhpRzzlZVqdmnHfSQjVK4zl45wdtkcfBnRgLadiezTKqUcZQ7RquePMlMJXwUfsACJw9plra57ObBZ7jTXYSkwRHPw0%2FgUVxI%2FtukspadObwwtFAkMIjPEIJs1MsofhwmgVEz%2B8DP400u8WivA6%2Fs%2BXKbtOzneBLTbFsT%2B%2FhMCZEhF2Y92hpUkkUNymrdLhm7cjwx8TMPS%2Fh%2FZpeJtlkOpoHE5SkyjB6Zj%2B0P%2B01F%2FoTdEC856dG2kKdcRhqPI4KH%2BdjJSYMbeJbLMFxZ23924geEPK3xjFweBN6AjLsaFoud89jnb8kzjrpb2tOWPLQiY7lG1Lg7sESn1Ote5Hr0XTcEmnR8GAYH0749z1S7qNd54A553JzbSDocSllclqReMIyo7bwGOqUB1PcowqOpA0ecuWtc8ldYPgNg9eFF1b1Nf8g3M22YIayq9WQ1JNnuH1bwHfXdRAir%2BBycT7d%2F1QT27SRAf%2BQLsSG1mMqy9qa%2BkiXZvTCpcQUJdMzJrlY1oiDZ%2FOcHiaiOguoFIy7p7LbKDQnhIHHQbeTY1YSbrV%2BDWwIZwg2qlmV%2BGYu4KOuGFqCxdmMK8f4AL6yeW0TzE%2FSuU004Xd85UlvXURxb&X-Amz-Signature=cbb8d22b2a71ac56a811a07c1d1d2cb6375cbaa8bd3be449c66add950b77530b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y32RGQCG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHSTNUdwnn9yrS8FrZ2nRAPA3xX8h61kEfwYSSsyHGlFAiEAn5W%2BM%2BtJwsoJFHw7jUcQch0BA9igMojqqnxuRtdjMnUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPYtHHA3Px%2BxUZBWBircA6fQPyIndnH2KnKRZnKgt45qo%2FPJ0OiedKLbVoegRNEwwZTd%2FYaOIv7Ua%2BsNFaOZ8KsReENU7lLtaLJdT4Ac3DxmAfKUaLPrY8sjCkDXohZ6DMrO7%2B6GSsnLhD8CGPJ409y7nCk82vE9UOArDt07a32Qq4clPbi5xV7hwVERjtbSoODIbH5esDeYm7iR9MwS8vQlp%2FfEZ%2BC60XkDqab1Ls%2FcA2GC%2B9P9kwzQyP%2FK4bikNFlOeVrL5k0Aol3RhpRzzlZVqdmnHfSQjVK4zl45wdtkcfBnRgLadiezTKqUcZQ7RquePMlMJXwUfsACJw9plra57ObBZ7jTXYSkwRHPw0%2FgUVxI%2FtukspadObwwtFAkMIjPEIJs1MsofhwmgVEz%2B8DP400u8WivA6%2Fs%2BXKbtOzneBLTbFsT%2B%2FhMCZEhF2Y92hpUkkUNymrdLhm7cjwx8TMPS%2Fh%2FZpeJtlkOpoHE5SkyjB6Zj%2B0P%2B01F%2FoTdEC856dG2kKdcRhqPI4KH%2BdjJSYMbeJbLMFxZ23924geEPK3xjFweBN6AjLsaFoud89jnb8kzjrpb2tOWPLQiY7lG1Lg7sESn1Ote5Hr0XTcEmnR8GAYH0749z1S7qNd54A553JzbSDocSllclqReMIyo7bwGOqUB1PcowqOpA0ecuWtc8ldYPgNg9eFF1b1Nf8g3M22YIayq9WQ1JNnuH1bwHfXdRAir%2BBycT7d%2F1QT27SRAf%2BQLsSG1mMqy9qa%2BkiXZvTCpcQUJdMzJrlY1oiDZ%2FOcHiaiOguoFIy7p7LbKDQnhIHHQbeTY1YSbrV%2BDWwIZwg2qlmV%2BGYu4KOuGFqCxdmMK8f4AL6yeW0TzE%2FSuU004Xd85UlvXURxb&X-Amz-Signature=bea1815805468a02152421519bd227351bcfe28ec069b2597f2370225ba8c062&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMDFA5L5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBZMaHW%2FTIw1OaNtJZGsVie7TeKh94PSUbnOhD14HolnAiEA7nBsJ%2BDcLsHchjBJUTXtLMmkkC55SVQ%2B20%2BsrwcxR8wqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEE0V62Z8GqvqkaoSSrcA96kFY2n1TCBmEuZRLe18hAs6ibwm86VP2R7FYdyiWk9G0m1SU3LnKrcXZHXBrLjukPmoMjFSwfA%2FAORg73I2%2FpvltdVJNz8%2BNJ55ApU9YFxpt%2FFOWA1Ccl5hld%2B3VKpaVIpEHVrzISl4d1DDYf2Thpw8ma%2FZxgqv8737Mk68zhjJYBhg93bmesCOKb8BB9%2BZZCi0DegIqogSvXdV5VL0BCkhnHpvSpzT0KMA0zkjXzO6l%2FAavMGNuHkz9%2Fgskuwr3yJm56jWynkHoQ6tVg1jsDMLBtJCgnPEban04x%2BPg7EO1Z9SsXSorXv5hG63AkW5uDO9%2BAVhtfDtqhrsN3rLCjtwPgj0mGoFdVORY%2BmEis7xf%2Bfhm70DCoDEo49iT2GI1Rw5F1EvAbpxAai%2BEd7t6kEpDAMqJpnVDkjuGoDuJ4okk9OLpWn%2Bwqdjh82t3DItiGAJ0cSyf9iPls38%2BXVDZdLIvxXqbFMCQNOBcE%2F34tm6Bj5ZHLbPjQEcyikvBoVj2%2BiD%2BZ6%2FF54U5EEgLUEL5vsjXExgwROwRDwZlb%2BAgm6i8T%2FKdxuQTL%2FUwtD0pdcBwParpkU1RmlLthuicDRsKyI%2ByKL8WDmvsS9AmqpwFVgZCUjuWnN7Km6%2BtdbMLuo7bwGOqUBl2q0lW5vjeIL1fbC9gb9E5BlgAvQRC3hA%2F5ciWtUHlY4mjbAhmIWa%2FRUm6o7Z5FMlt8vzz8FWt6I8UPjJbHnoWbBQkB7k3Z6SSENnPV9r%2Bz%2BTZekKDdWYyXHYeyO9D31Pze38Ad2VdzpwyDQnqY1HL6c8r1vPs8%2FGbpv030cMwLb7iimxWDG0U7S2G88ZIJx6%2F7Q3tNjiNX9Ma6v2xGf72VGuv6d&X-Amz-Signature=d11f4a8d2f6bfb5da0ce86a1ffba4e9e64bddf09086a618712cef71eba12152e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMDFA5L5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBZMaHW%2FTIw1OaNtJZGsVie7TeKh94PSUbnOhD14HolnAiEA7nBsJ%2BDcLsHchjBJUTXtLMmkkC55SVQ%2B20%2BsrwcxR8wqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEE0V62Z8GqvqkaoSSrcA96kFY2n1TCBmEuZRLe18hAs6ibwm86VP2R7FYdyiWk9G0m1SU3LnKrcXZHXBrLjukPmoMjFSwfA%2FAORg73I2%2FpvltdVJNz8%2BNJ55ApU9YFxpt%2FFOWA1Ccl5hld%2B3VKpaVIpEHVrzISl4d1DDYf2Thpw8ma%2FZxgqv8737Mk68zhjJYBhg93bmesCOKb8BB9%2BZZCi0DegIqogSvXdV5VL0BCkhnHpvSpzT0KMA0zkjXzO6l%2FAavMGNuHkz9%2Fgskuwr3yJm56jWynkHoQ6tVg1jsDMLBtJCgnPEban04x%2BPg7EO1Z9SsXSorXv5hG63AkW5uDO9%2BAVhtfDtqhrsN3rLCjtwPgj0mGoFdVORY%2BmEis7xf%2Bfhm70DCoDEo49iT2GI1Rw5F1EvAbpxAai%2BEd7t6kEpDAMqJpnVDkjuGoDuJ4okk9OLpWn%2Bwqdjh82t3DItiGAJ0cSyf9iPls38%2BXVDZdLIvxXqbFMCQNOBcE%2F34tm6Bj5ZHLbPjQEcyikvBoVj2%2BiD%2BZ6%2FF54U5EEgLUEL5vsjXExgwROwRDwZlb%2BAgm6i8T%2FKdxuQTL%2FUwtD0pdcBwParpkU1RmlLthuicDRsKyI%2ByKL8WDmvsS9AmqpwFVgZCUjuWnN7Km6%2BtdbMLuo7bwGOqUBl2q0lW5vjeIL1fbC9gb9E5BlgAvQRC3hA%2F5ciWtUHlY4mjbAhmIWa%2FRUm6o7Z5FMlt8vzz8FWt6I8UPjJbHnoWbBQkB7k3Z6SSENnPV9r%2Bz%2BTZekKDdWYyXHYeyO9D31Pze38Ad2VdzpwyDQnqY1HL6c8r1vPs8%2FGbpv030cMwLb7iimxWDG0U7S2G88ZIJx6%2F7Q3tNjiNX9Ma6v2xGf72VGuv6d&X-Amz-Signature=7b9cc57aa1ac746bf20c89d98db4ccc6382db9b9b54adc8975cb94c39afa32fc&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
