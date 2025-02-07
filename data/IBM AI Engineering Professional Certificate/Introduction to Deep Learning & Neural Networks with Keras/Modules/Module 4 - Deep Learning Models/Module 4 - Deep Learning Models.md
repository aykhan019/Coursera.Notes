

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAQSJZGQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQDNiGgTQsedYKv%2Bjs6xFRDc4%2Fz8lgKUd3LDyzQtNZcrEAIgE9wMv8D46pq0weF9XUUA2X6BIr%2Bn0c6UV9s%2BeT7efW0q%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDL%2Fwdke3UubWwuDimircA9n0IvK93FRwwDnRzzVRI%2ByNH3JvbxepInwFhlb9EEv7zkQ3TpjLAmKz7TBLe13oIYj%2BCU7NTnQA37H%2FUyjrn%2FcAzMlmCykQK0uv0m8CzV5CeUqGoUk8UQlNvZT7M7pviJox%2BJK%2B7HPy%2Fn1nI%2BI73Ekmd7I2L%2B29Pu4%2FWblVQK6%2BvDp%2Bpe8S9rnJpJLJ2QjLiEuMi6w%2FUjiAvQDrq%2BhDkuQExZFXwXJTuAtk3IvEw1a0GPlyVHLbwhOoppZaCH3D5oiT4XNw2fdFHhXRq0nMiHcqeVATV9z4DcM52eV5YCUjIdlPeOVOX5ckQZ5GQc%2BaB8uOcchQLEfYU6BbWu%2FbJG6KG%2BFHpfuEwTSXRSQ2h0RC6LjvyzFH1FZMckJQP949FrNvCevOG1rpyySi98aiFw%2B9M4z%2BDoLC20%2BLGPhpjIdvkBEtqiwMMk1sWhiJqGiyrHY2xnR5K9ukiCj%2FosjqJzgKH1PorBP4HgOdq4nuQRGQsxxtCmbhglxfXep1bRNl27bGTG8V15B%2Fw2kP%2FEMM0s8pA3sCMwyEMO65oKqK%2BHoVqyUzuv3GEuHW6lkyvF40WwqUX4xaSKVqjsnry3OK1CmlJupvtDR9YHsmMT%2FOpjfJRw%2BggkseR%2FXQH4MeMJ%2B%2Flr0GOqUB7X2Ld68XuiJm2EJ7OfQW4roXbm7jB4ZLzNENP3RhvldMGA3zqaY%2F56UXus%2F1uc7pllhGoek%2BqBbzfQUMGThIxyCqjB%2FrE69REwg7xlqr4282Jo1uOqqhwAM8Kq5SwmYn1wMDT%2F5i12BVC829H2NzUb4dHNkwX5iZhKBb2PR7R8MfIOSHApyw4VuvvzwAX3d36XiaVSY%2Fnz%2BgoGpHxq0KDAG63GHE&X-Amz-Signature=e0362735fd3cafe527be6ab849e265fb8be3033fe29ff1d36299217fc6ef8405&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAQSJZGQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQDNiGgTQsedYKv%2Bjs6xFRDc4%2Fz8lgKUd3LDyzQtNZcrEAIgE9wMv8D46pq0weF9XUUA2X6BIr%2Bn0c6UV9s%2BeT7efW0q%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDL%2Fwdke3UubWwuDimircA9n0IvK93FRwwDnRzzVRI%2ByNH3JvbxepInwFhlb9EEv7zkQ3TpjLAmKz7TBLe13oIYj%2BCU7NTnQA37H%2FUyjrn%2FcAzMlmCykQK0uv0m8CzV5CeUqGoUk8UQlNvZT7M7pviJox%2BJK%2B7HPy%2Fn1nI%2BI73Ekmd7I2L%2B29Pu4%2FWblVQK6%2BvDp%2Bpe8S9rnJpJLJ2QjLiEuMi6w%2FUjiAvQDrq%2BhDkuQExZFXwXJTuAtk3IvEw1a0GPlyVHLbwhOoppZaCH3D5oiT4XNw2fdFHhXRq0nMiHcqeVATV9z4DcM52eV5YCUjIdlPeOVOX5ckQZ5GQc%2BaB8uOcchQLEfYU6BbWu%2FbJG6KG%2BFHpfuEwTSXRSQ2h0RC6LjvyzFH1FZMckJQP949FrNvCevOG1rpyySi98aiFw%2B9M4z%2BDoLC20%2BLGPhpjIdvkBEtqiwMMk1sWhiJqGiyrHY2xnR5K9ukiCj%2FosjqJzgKH1PorBP4HgOdq4nuQRGQsxxtCmbhglxfXep1bRNl27bGTG8V15B%2Fw2kP%2FEMM0s8pA3sCMwyEMO65oKqK%2BHoVqyUzuv3GEuHW6lkyvF40WwqUX4xaSKVqjsnry3OK1CmlJupvtDR9YHsmMT%2FOpjfJRw%2BggkseR%2FXQH4MeMJ%2B%2Flr0GOqUB7X2Ld68XuiJm2EJ7OfQW4roXbm7jB4ZLzNENP3RhvldMGA3zqaY%2F56UXus%2F1uc7pllhGoek%2BqBbzfQUMGThIxyCqjB%2FrE69REwg7xlqr4282Jo1uOqqhwAM8Kq5SwmYn1wMDT%2F5i12BVC829H2NzUb4dHNkwX5iZhKBb2PR7R8MfIOSHApyw4VuvvzwAX3d36XiaVSY%2Fnz%2BgoGpHxq0KDAG63GHE&X-Amz-Signature=c25981c2fb4588b4aa952020e98e1296af696822c1d504c79b3a76a257f36ceb&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAQSJZGQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQDNiGgTQsedYKv%2Bjs6xFRDc4%2Fz8lgKUd3LDyzQtNZcrEAIgE9wMv8D46pq0weF9XUUA2X6BIr%2Bn0c6UV9s%2BeT7efW0q%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDL%2Fwdke3UubWwuDimircA9n0IvK93FRwwDnRzzVRI%2ByNH3JvbxepInwFhlb9EEv7zkQ3TpjLAmKz7TBLe13oIYj%2BCU7NTnQA37H%2FUyjrn%2FcAzMlmCykQK0uv0m8CzV5CeUqGoUk8UQlNvZT7M7pviJox%2BJK%2B7HPy%2Fn1nI%2BI73Ekmd7I2L%2B29Pu4%2FWblVQK6%2BvDp%2Bpe8S9rnJpJLJ2QjLiEuMi6w%2FUjiAvQDrq%2BhDkuQExZFXwXJTuAtk3IvEw1a0GPlyVHLbwhOoppZaCH3D5oiT4XNw2fdFHhXRq0nMiHcqeVATV9z4DcM52eV5YCUjIdlPeOVOX5ckQZ5GQc%2BaB8uOcchQLEfYU6BbWu%2FbJG6KG%2BFHpfuEwTSXRSQ2h0RC6LjvyzFH1FZMckJQP949FrNvCevOG1rpyySi98aiFw%2B9M4z%2BDoLC20%2BLGPhpjIdvkBEtqiwMMk1sWhiJqGiyrHY2xnR5K9ukiCj%2FosjqJzgKH1PorBP4HgOdq4nuQRGQsxxtCmbhglxfXep1bRNl27bGTG8V15B%2Fw2kP%2FEMM0s8pA3sCMwyEMO65oKqK%2BHoVqyUzuv3GEuHW6lkyvF40WwqUX4xaSKVqjsnry3OK1CmlJupvtDR9YHsmMT%2FOpjfJRw%2BggkseR%2FXQH4MeMJ%2B%2Flr0GOqUB7X2Ld68XuiJm2EJ7OfQW4roXbm7jB4ZLzNENP3RhvldMGA3zqaY%2F56UXus%2F1uc7pllhGoek%2BqBbzfQUMGThIxyCqjB%2FrE69REwg7xlqr4282Jo1uOqqhwAM8Kq5SwmYn1wMDT%2F5i12BVC829H2NzUb4dHNkwX5iZhKBb2PR7R8MfIOSHApyw4VuvvzwAX3d36XiaVSY%2Fnz%2BgoGpHxq0KDAG63GHE&X-Amz-Signature=ae3dcda3205064b6335387d4c7b54ac2ff1a6a1f21d9643d0f60ce26d0f89668&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAQSJZGQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQDNiGgTQsedYKv%2Bjs6xFRDc4%2Fz8lgKUd3LDyzQtNZcrEAIgE9wMv8D46pq0weF9XUUA2X6BIr%2Bn0c6UV9s%2BeT7efW0q%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDL%2Fwdke3UubWwuDimircA9n0IvK93FRwwDnRzzVRI%2ByNH3JvbxepInwFhlb9EEv7zkQ3TpjLAmKz7TBLe13oIYj%2BCU7NTnQA37H%2FUyjrn%2FcAzMlmCykQK0uv0m8CzV5CeUqGoUk8UQlNvZT7M7pviJox%2BJK%2B7HPy%2Fn1nI%2BI73Ekmd7I2L%2B29Pu4%2FWblVQK6%2BvDp%2Bpe8S9rnJpJLJ2QjLiEuMi6w%2FUjiAvQDrq%2BhDkuQExZFXwXJTuAtk3IvEw1a0GPlyVHLbwhOoppZaCH3D5oiT4XNw2fdFHhXRq0nMiHcqeVATV9z4DcM52eV5YCUjIdlPeOVOX5ckQZ5GQc%2BaB8uOcchQLEfYU6BbWu%2FbJG6KG%2BFHpfuEwTSXRSQ2h0RC6LjvyzFH1FZMckJQP949FrNvCevOG1rpyySi98aiFw%2B9M4z%2BDoLC20%2BLGPhpjIdvkBEtqiwMMk1sWhiJqGiyrHY2xnR5K9ukiCj%2FosjqJzgKH1PorBP4HgOdq4nuQRGQsxxtCmbhglxfXep1bRNl27bGTG8V15B%2Fw2kP%2FEMM0s8pA3sCMwyEMO65oKqK%2BHoVqyUzuv3GEuHW6lkyvF40WwqUX4xaSKVqjsnry3OK1CmlJupvtDR9YHsmMT%2FOpjfJRw%2BggkseR%2FXQH4MeMJ%2B%2Flr0GOqUB7X2Ld68XuiJm2EJ7OfQW4roXbm7jB4ZLzNENP3RhvldMGA3zqaY%2F56UXus%2F1uc7pllhGoek%2BqBbzfQUMGThIxyCqjB%2FrE69REwg7xlqr4282Jo1uOqqhwAM8Kq5SwmYn1wMDT%2F5i12BVC829H2NzUb4dHNkwX5iZhKBb2PR7R8MfIOSHApyw4VuvvzwAX3d36XiaVSY%2Fnz%2BgoGpHxq0KDAG63GHE&X-Amz-Signature=91ed191299ef8c7f7b596aab16c6cfaaddd31632695a33261a608c2ea579c466&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAQSJZGQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQDNiGgTQsedYKv%2Bjs6xFRDc4%2Fz8lgKUd3LDyzQtNZcrEAIgE9wMv8D46pq0weF9XUUA2X6BIr%2Bn0c6UV9s%2BeT7efW0q%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDL%2Fwdke3UubWwuDimircA9n0IvK93FRwwDnRzzVRI%2ByNH3JvbxepInwFhlb9EEv7zkQ3TpjLAmKz7TBLe13oIYj%2BCU7NTnQA37H%2FUyjrn%2FcAzMlmCykQK0uv0m8CzV5CeUqGoUk8UQlNvZT7M7pviJox%2BJK%2B7HPy%2Fn1nI%2BI73Ekmd7I2L%2B29Pu4%2FWblVQK6%2BvDp%2Bpe8S9rnJpJLJ2QjLiEuMi6w%2FUjiAvQDrq%2BhDkuQExZFXwXJTuAtk3IvEw1a0GPlyVHLbwhOoppZaCH3D5oiT4XNw2fdFHhXRq0nMiHcqeVATV9z4DcM52eV5YCUjIdlPeOVOX5ckQZ5GQc%2BaB8uOcchQLEfYU6BbWu%2FbJG6KG%2BFHpfuEwTSXRSQ2h0RC6LjvyzFH1FZMckJQP949FrNvCevOG1rpyySi98aiFw%2B9M4z%2BDoLC20%2BLGPhpjIdvkBEtqiwMMk1sWhiJqGiyrHY2xnR5K9ukiCj%2FosjqJzgKH1PorBP4HgOdq4nuQRGQsxxtCmbhglxfXep1bRNl27bGTG8V15B%2Fw2kP%2FEMM0s8pA3sCMwyEMO65oKqK%2BHoVqyUzuv3GEuHW6lkyvF40WwqUX4xaSKVqjsnry3OK1CmlJupvtDR9YHsmMT%2FOpjfJRw%2BggkseR%2FXQH4MeMJ%2B%2Flr0GOqUB7X2Ld68XuiJm2EJ7OfQW4roXbm7jB4ZLzNENP3RhvldMGA3zqaY%2F56UXus%2F1uc7pllhGoek%2BqBbzfQUMGThIxyCqjB%2FrE69REwg7xlqr4282Jo1uOqqhwAM8Kq5SwmYn1wMDT%2F5i12BVC829H2NzUb4dHNkwX5iZhKBb2PR7R8MfIOSHApyw4VuvvzwAX3d36XiaVSY%2Fnz%2BgoGpHxq0KDAG63GHE&X-Amz-Signature=12a8f5cb7098d5e30de5ed44c95631331933f15bb477c36eca3697aacb5fa15f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAQSJZGQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQDNiGgTQsedYKv%2Bjs6xFRDc4%2Fz8lgKUd3LDyzQtNZcrEAIgE9wMv8D46pq0weF9XUUA2X6BIr%2Bn0c6UV9s%2BeT7efW0q%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDL%2Fwdke3UubWwuDimircA9n0IvK93FRwwDnRzzVRI%2ByNH3JvbxepInwFhlb9EEv7zkQ3TpjLAmKz7TBLe13oIYj%2BCU7NTnQA37H%2FUyjrn%2FcAzMlmCykQK0uv0m8CzV5CeUqGoUk8UQlNvZT7M7pviJox%2BJK%2B7HPy%2Fn1nI%2BI73Ekmd7I2L%2B29Pu4%2FWblVQK6%2BvDp%2Bpe8S9rnJpJLJ2QjLiEuMi6w%2FUjiAvQDrq%2BhDkuQExZFXwXJTuAtk3IvEw1a0GPlyVHLbwhOoppZaCH3D5oiT4XNw2fdFHhXRq0nMiHcqeVATV9z4DcM52eV5YCUjIdlPeOVOX5ckQZ5GQc%2BaB8uOcchQLEfYU6BbWu%2FbJG6KG%2BFHpfuEwTSXRSQ2h0RC6LjvyzFH1FZMckJQP949FrNvCevOG1rpyySi98aiFw%2B9M4z%2BDoLC20%2BLGPhpjIdvkBEtqiwMMk1sWhiJqGiyrHY2xnR5K9ukiCj%2FosjqJzgKH1PorBP4HgOdq4nuQRGQsxxtCmbhglxfXep1bRNl27bGTG8V15B%2Fw2kP%2FEMM0s8pA3sCMwyEMO65oKqK%2BHoVqyUzuv3GEuHW6lkyvF40WwqUX4xaSKVqjsnry3OK1CmlJupvtDR9YHsmMT%2FOpjfJRw%2BggkseR%2FXQH4MeMJ%2B%2Flr0GOqUB7X2Ld68XuiJm2EJ7OfQW4roXbm7jB4ZLzNENP3RhvldMGA3zqaY%2F56UXus%2F1uc7pllhGoek%2BqBbzfQUMGThIxyCqjB%2FrE69REwg7xlqr4282Jo1uOqqhwAM8Kq5SwmYn1wMDT%2F5i12BVC829H2NzUb4dHNkwX5iZhKBb2PR7R8MfIOSHApyw4VuvvzwAX3d36XiaVSY%2Fnz%2BgoGpHxq0KDAG63GHE&X-Amz-Signature=8a0c6dc3e5be4afffd403eb80d6648054c2eb83532f6476a777466da93a78fed&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAQSJZGQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQDNiGgTQsedYKv%2Bjs6xFRDc4%2Fz8lgKUd3LDyzQtNZcrEAIgE9wMv8D46pq0weF9XUUA2X6BIr%2Bn0c6UV9s%2BeT7efW0q%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDL%2Fwdke3UubWwuDimircA9n0IvK93FRwwDnRzzVRI%2ByNH3JvbxepInwFhlb9EEv7zkQ3TpjLAmKz7TBLe13oIYj%2BCU7NTnQA37H%2FUyjrn%2FcAzMlmCykQK0uv0m8CzV5CeUqGoUk8UQlNvZT7M7pviJox%2BJK%2B7HPy%2Fn1nI%2BI73Ekmd7I2L%2B29Pu4%2FWblVQK6%2BvDp%2Bpe8S9rnJpJLJ2QjLiEuMi6w%2FUjiAvQDrq%2BhDkuQExZFXwXJTuAtk3IvEw1a0GPlyVHLbwhOoppZaCH3D5oiT4XNw2fdFHhXRq0nMiHcqeVATV9z4DcM52eV5YCUjIdlPeOVOX5ckQZ5GQc%2BaB8uOcchQLEfYU6BbWu%2FbJG6KG%2BFHpfuEwTSXRSQ2h0RC6LjvyzFH1FZMckJQP949FrNvCevOG1rpyySi98aiFw%2B9M4z%2BDoLC20%2BLGPhpjIdvkBEtqiwMMk1sWhiJqGiyrHY2xnR5K9ukiCj%2FosjqJzgKH1PorBP4HgOdq4nuQRGQsxxtCmbhglxfXep1bRNl27bGTG8V15B%2Fw2kP%2FEMM0s8pA3sCMwyEMO65oKqK%2BHoVqyUzuv3GEuHW6lkyvF40WwqUX4xaSKVqjsnry3OK1CmlJupvtDR9YHsmMT%2FOpjfJRw%2BggkseR%2FXQH4MeMJ%2B%2Flr0GOqUB7X2Ld68XuiJm2EJ7OfQW4roXbm7jB4ZLzNENP3RhvldMGA3zqaY%2F56UXus%2F1uc7pllhGoek%2BqBbzfQUMGThIxyCqjB%2FrE69REwg7xlqr4282Jo1uOqqhwAM8Kq5SwmYn1wMDT%2F5i12BVC829H2NzUb4dHNkwX5iZhKBb2PR7R8MfIOSHApyw4VuvvzwAX3d36XiaVSY%2Fnz%2BgoGpHxq0KDAG63GHE&X-Amz-Signature=5c109eb9e113db07e3f89005267d067a8917005180c355b08f03613f11c3a6c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAQSJZGQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQDNiGgTQsedYKv%2Bjs6xFRDc4%2Fz8lgKUd3LDyzQtNZcrEAIgE9wMv8D46pq0weF9XUUA2X6BIr%2Bn0c6UV9s%2BeT7efW0q%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDL%2Fwdke3UubWwuDimircA9n0IvK93FRwwDnRzzVRI%2ByNH3JvbxepInwFhlb9EEv7zkQ3TpjLAmKz7TBLe13oIYj%2BCU7NTnQA37H%2FUyjrn%2FcAzMlmCykQK0uv0m8CzV5CeUqGoUk8UQlNvZT7M7pviJox%2BJK%2B7HPy%2Fn1nI%2BI73Ekmd7I2L%2B29Pu4%2FWblVQK6%2BvDp%2Bpe8S9rnJpJLJ2QjLiEuMi6w%2FUjiAvQDrq%2BhDkuQExZFXwXJTuAtk3IvEw1a0GPlyVHLbwhOoppZaCH3D5oiT4XNw2fdFHhXRq0nMiHcqeVATV9z4DcM52eV5YCUjIdlPeOVOX5ckQZ5GQc%2BaB8uOcchQLEfYU6BbWu%2FbJG6KG%2BFHpfuEwTSXRSQ2h0RC6LjvyzFH1FZMckJQP949FrNvCevOG1rpyySi98aiFw%2B9M4z%2BDoLC20%2BLGPhpjIdvkBEtqiwMMk1sWhiJqGiyrHY2xnR5K9ukiCj%2FosjqJzgKH1PorBP4HgOdq4nuQRGQsxxtCmbhglxfXep1bRNl27bGTG8V15B%2Fw2kP%2FEMM0s8pA3sCMwyEMO65oKqK%2BHoVqyUzuv3GEuHW6lkyvF40WwqUX4xaSKVqjsnry3OK1CmlJupvtDR9YHsmMT%2FOpjfJRw%2BggkseR%2FXQH4MeMJ%2B%2Flr0GOqUB7X2Ld68XuiJm2EJ7OfQW4roXbm7jB4ZLzNENP3RhvldMGA3zqaY%2F56UXus%2F1uc7pllhGoek%2BqBbzfQUMGThIxyCqjB%2FrE69REwg7xlqr4282Jo1uOqqhwAM8Kq5SwmYn1wMDT%2F5i12BVC829H2NzUb4dHNkwX5iZhKBb2PR7R8MfIOSHApyw4VuvvzwAX3d36XiaVSY%2Fnz%2BgoGpHxq0KDAG63GHE&X-Amz-Signature=dc109e8c2dcb0a5922e6f46e844636a4faa919d1850aa98bca953be5046e39ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAQSJZGQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQDNiGgTQsedYKv%2Bjs6xFRDc4%2Fz8lgKUd3LDyzQtNZcrEAIgE9wMv8D46pq0weF9XUUA2X6BIr%2Bn0c6UV9s%2BeT7efW0q%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDL%2Fwdke3UubWwuDimircA9n0IvK93FRwwDnRzzVRI%2ByNH3JvbxepInwFhlb9EEv7zkQ3TpjLAmKz7TBLe13oIYj%2BCU7NTnQA37H%2FUyjrn%2FcAzMlmCykQK0uv0m8CzV5CeUqGoUk8UQlNvZT7M7pviJox%2BJK%2B7HPy%2Fn1nI%2BI73Ekmd7I2L%2B29Pu4%2FWblVQK6%2BvDp%2Bpe8S9rnJpJLJ2QjLiEuMi6w%2FUjiAvQDrq%2BhDkuQExZFXwXJTuAtk3IvEw1a0GPlyVHLbwhOoppZaCH3D5oiT4XNw2fdFHhXRq0nMiHcqeVATV9z4DcM52eV5YCUjIdlPeOVOX5ckQZ5GQc%2BaB8uOcchQLEfYU6BbWu%2FbJG6KG%2BFHpfuEwTSXRSQ2h0RC6LjvyzFH1FZMckJQP949FrNvCevOG1rpyySi98aiFw%2B9M4z%2BDoLC20%2BLGPhpjIdvkBEtqiwMMk1sWhiJqGiyrHY2xnR5K9ukiCj%2FosjqJzgKH1PorBP4HgOdq4nuQRGQsxxtCmbhglxfXep1bRNl27bGTG8V15B%2Fw2kP%2FEMM0s8pA3sCMwyEMO65oKqK%2BHoVqyUzuv3GEuHW6lkyvF40WwqUX4xaSKVqjsnry3OK1CmlJupvtDR9YHsmMT%2FOpjfJRw%2BggkseR%2FXQH4MeMJ%2B%2Flr0GOqUB7X2Ld68XuiJm2EJ7OfQW4roXbm7jB4ZLzNENP3RhvldMGA3zqaY%2F56UXus%2F1uc7pllhGoek%2BqBbzfQUMGThIxyCqjB%2FrE69REwg7xlqr4282Jo1uOqqhwAM8Kq5SwmYn1wMDT%2F5i12BVC829H2NzUb4dHNkwX5iZhKBb2PR7R8MfIOSHApyw4VuvvzwAX3d36XiaVSY%2Fnz%2BgoGpHxq0KDAG63GHE&X-Amz-Signature=22e190c939892ba78592be3cf1ece91ac27e840c4a2873e41fa69bf22778b8ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCOX3IXI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDP9ceT2IpCacqEuNKt8PG0m4cdN0X5n3lpxgLNWOaHIAIhAIY91srLQ%2FnmxY0Le6HmunJ8YPQPg3gs%2FCsc0PmWwuKXKv8DCG8QABoMNjM3NDIzMTgzODA1Igy%2BUfDT5yJTTbZXc4Uq3AMXWYgC%2F18osE9gZJrnO0FjmdWdd1vx2Mq1W2nkVLBRa9L3RlNSz5Br0OQ%2BpfYmuZzmP9%2F%2BOmNR2p4JiQfSP36t4lWeqRHMxmM%2FnzpM6dU%2Ff6%2FdxHTg5USnNMUsu9K63OJYJtNwQYbNHleO72FqVURr4%2FbizxATp1BhmieAN%2FI9%2BcFp%2BKhcl6uWvT2eJYYV0O6ZI2JGqlzMvEOrrUzrEYCxCUNNbH5N5eAZ%2F310upLzlBfBQBqd1b8FzbSUoKXgr3G8uNIp%2FIjp2zxzZW1kMrAzV%2BEIcrDzm5uwN8KmrJ4CZ6he%2FTA1bKFEO%2Frq2cxGRw50NPKnTESpTESlj%2FsfiEwI4lXU6RO8MPa8l3mtXFdAZzYL3ui7%2FjLE1RziiuKs9sk0S%2BovDHOu97Y7HmdbxwSEVRugoL%2BLxeC8y43h5jinyAghBNReLsC0b93giXRZNp1zhW89X2Fx7XRM6RACwQuNsTWMC7eQBRFqCDkqV%2BbHB3YVAIRvrA%2Fx1zMdXn7P0FVcea%2FaPqCGHg9CZdijJMdNTQQ3mhapjXcnGO0Mae3yxds0LQ9oVyc7lzAoJwdWp8%2FaqF%2BE1D4sp8qnr8Ym%2BdlVDvlkgm4lWHrY5A4czsQh26l%2B77mcEzK6NRBraTCiv5a9BjqkAbsq2RUmcp1hqkenSl1%2BLq%2B6BWJ55a4%2FfO5uVPVMNw27EV0hNR3UnKvKusr%2B0ywu5%2Fozb901uY%2F5IwdV8LlkgDcICwqQOwzB%2F2XhosHS8wkSO0sj0Ch1rnRJdNs2p8DnOPHSL5BIqY55RK2sF9ESW3P3nMaNmkJY6wWuV5jjtzLRAxgwG%2FgaUT8qpKYXxoejFxRQAQC6FdVol%2FgfE%2FGZ6%2FCj2uZ0&X-Amz-Signature=6696d2a1e7086f7670198f0d12d51cafa1715c86270af875ec9df03d8cab22cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCOX3IXI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDP9ceT2IpCacqEuNKt8PG0m4cdN0X5n3lpxgLNWOaHIAIhAIY91srLQ%2FnmxY0Le6HmunJ8YPQPg3gs%2FCsc0PmWwuKXKv8DCG8QABoMNjM3NDIzMTgzODA1Igy%2BUfDT5yJTTbZXc4Uq3AMXWYgC%2F18osE9gZJrnO0FjmdWdd1vx2Mq1W2nkVLBRa9L3RlNSz5Br0OQ%2BpfYmuZzmP9%2F%2BOmNR2p4JiQfSP36t4lWeqRHMxmM%2FnzpM6dU%2Ff6%2FdxHTg5USnNMUsu9K63OJYJtNwQYbNHleO72FqVURr4%2FbizxATp1BhmieAN%2FI9%2BcFp%2BKhcl6uWvT2eJYYV0O6ZI2JGqlzMvEOrrUzrEYCxCUNNbH5N5eAZ%2F310upLzlBfBQBqd1b8FzbSUoKXgr3G8uNIp%2FIjp2zxzZW1kMrAzV%2BEIcrDzm5uwN8KmrJ4CZ6he%2FTA1bKFEO%2Frq2cxGRw50NPKnTESpTESlj%2FsfiEwI4lXU6RO8MPa8l3mtXFdAZzYL3ui7%2FjLE1RziiuKs9sk0S%2BovDHOu97Y7HmdbxwSEVRugoL%2BLxeC8y43h5jinyAghBNReLsC0b93giXRZNp1zhW89X2Fx7XRM6RACwQuNsTWMC7eQBRFqCDkqV%2BbHB3YVAIRvrA%2Fx1zMdXn7P0FVcea%2FaPqCGHg9CZdijJMdNTQQ3mhapjXcnGO0Mae3yxds0LQ9oVyc7lzAoJwdWp8%2FaqF%2BE1D4sp8qnr8Ym%2BdlVDvlkgm4lWHrY5A4czsQh26l%2B77mcEzK6NRBraTCiv5a9BjqkAbsq2RUmcp1hqkenSl1%2BLq%2B6BWJ55a4%2FfO5uVPVMNw27EV0hNR3UnKvKusr%2B0ywu5%2Fozb901uY%2F5IwdV8LlkgDcICwqQOwzB%2F2XhosHS8wkSO0sj0Ch1rnRJdNs2p8DnOPHSL5BIqY55RK2sF9ESW3P3nMaNmkJY6wWuV5jjtzLRAxgwG%2FgaUT8qpKYXxoejFxRQAQC6FdVol%2FgfE%2FGZ6%2FCj2uZ0&X-Amz-Signature=97761d2a18bb8939fe4757e6d133c732262aa84015f88d4acf94b908249e7c28&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
