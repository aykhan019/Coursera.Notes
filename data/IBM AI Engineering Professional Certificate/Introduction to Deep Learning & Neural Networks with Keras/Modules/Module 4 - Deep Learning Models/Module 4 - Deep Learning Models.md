

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=f3e5ece0c6896457b11f39a598b68818efd1d7295736caa196cce3be59684087&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=cada1b1b7b982edf1c1bd11a27175c4b8648fd2b73d5127421008cc4a41a79f7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=1d3c65b0dccff6114e3c8a99c414db75bcf1b09cdf3b236ab264abfe66b6c29d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=b724ca4d557f0f7c8344c3a3c1c5e34a079a352038d02673a0aca8c25826a842&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=6a1d67118f33c66640ab852719127f8e15a6bd8fdffd7d8e1ef4c6fa0a8c4f5f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=67ed64f7836982b0a2729bda9caba7296acc891592f581861d78934f95bbbb31&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=8e7cf11df7e7ba2668fc5d1536d2274f0f4049074a69ac2fee10b2eef162604a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=7f31d40b2f377b91ae37595d610a33ecc3401b3e4caf655d3d54a502b05ed4b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=66f2c45d1a816e63e280467b7f61352944ea37763d64663e104589a258c27bc9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QMLGXRE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHkq7hG1Pb8lgsfPCndpHG3xOBf%2BJklBRlN%2B9geglRVAIgbuhVDlmD7W1kVe6CGy%2Fh4C1x1OmIU1OX%2FSM9qLzvNDgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNs%2FB5vMXIwl3GCsaSrcA5%2FXWOzy9Ih9i7nk80KL%2FRmu93O4ghNsQ0YpHdK0eCUwONuByu2gjpn2Pc%2FTAkIBGIp6AlbCo5qywRcOXmz%2FNS%2F3kWIIQ0lPVQ99j4QNTMI%2F9usNWV5%2BUgPVSlLukk2f%2By0PL5DQdU8rS%2Bjq6BDjN4v7j1IvuRpk5IzCK%2BopevZbUgPQa3IpuNmpjvHmYAVerdKz0duml3VzlQvqOxeeDARsBeEOaMihf7FK5cQ2LI4BhrvxYYS%2BeCTQ5gb%2Biw9cc687leBm9o%2BxUxytPLdmX95IpDO0%2BMuO8aBJ5SBsFHy4BIlU50GndEwL0xz8tbjm0umSiF51AJ04NWEZ7lqd5lCFMbm9Y2RVT7sTawqx321oJ41Q2eIr8itfdoEhdXWdQg87pVY1sA4%2B2M1C8MkjggN2ulwi5ztLc9Wbz%2F866DYBxxgZqkGyrGwm1dItZnA4w6oD3kuPlmDixYdZE%2FhVXu6hMMeYj3erdw9%2Bt%2BoIhhim%2ByUIaBXKpkQ7Clmc9KNmNFDlsKGvr0wMfrHSmMnfqNXHDoRMY87viui8PdBqUlrWgR8gEMDEZoOhnVPFeQHjoSPXCkaLXYQCLkLGMpyDt%2B7zT%2Bx5h8AAGeVpwKwJpM33D8PoVF%2FZko8W%2FMl0MNje%2FrwGOqUBab8%2BXkIVRxw8aSBsUbczT94TBP52IWnaNEUIhyWiETJZ1vEEE03GHkEkChn7r6opuytOKY8%2BSmQlGqcfoufmQEVCqIwS0%2FiG4iJZSJ9j7ILLw3deBRfl7enNJlD2v6tu47lj1%2FztBH0hFyeSNRlzeBBFVyrJ8KpMqQYB%2B5RJwjLdmRZIBhz7Ln7mc2faR%2FIgHxNXXZwPDYFH5ikIKN2c6Wra1is%2F&X-Amz-Signature=db490258e56e033b3b5a20bf1ef2ecb9d1f166e1f618e371b8aedf3a0be70ae0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QMLGXRE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHkq7hG1Pb8lgsfPCndpHG3xOBf%2BJklBRlN%2B9geglRVAIgbuhVDlmD7W1kVe6CGy%2Fh4C1x1OmIU1OX%2FSM9qLzvNDgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNs%2FB5vMXIwl3GCsaSrcA5%2FXWOzy9Ih9i7nk80KL%2FRmu93O4ghNsQ0YpHdK0eCUwONuByu2gjpn2Pc%2FTAkIBGIp6AlbCo5qywRcOXmz%2FNS%2F3kWIIQ0lPVQ99j4QNTMI%2F9usNWV5%2BUgPVSlLukk2f%2By0PL5DQdU8rS%2Bjq6BDjN4v7j1IvuRpk5IzCK%2BopevZbUgPQa3IpuNmpjvHmYAVerdKz0duml3VzlQvqOxeeDARsBeEOaMihf7FK5cQ2LI4BhrvxYYS%2BeCTQ5gb%2Biw9cc687leBm9o%2BxUxytPLdmX95IpDO0%2BMuO8aBJ5SBsFHy4BIlU50GndEwL0xz8tbjm0umSiF51AJ04NWEZ7lqd5lCFMbm9Y2RVT7sTawqx321oJ41Q2eIr8itfdoEhdXWdQg87pVY1sA4%2B2M1C8MkjggN2ulwi5ztLc9Wbz%2F866DYBxxgZqkGyrGwm1dItZnA4w6oD3kuPlmDixYdZE%2FhVXu6hMMeYj3erdw9%2Bt%2BoIhhim%2ByUIaBXKpkQ7Clmc9KNmNFDlsKGvr0wMfrHSmMnfqNXHDoRMY87viui8PdBqUlrWgR8gEMDEZoOhnVPFeQHjoSPXCkaLXYQCLkLGMpyDt%2B7zT%2Bx5h8AAGeVpwKwJpM33D8PoVF%2FZko8W%2FMl0MNje%2FrwGOqUBab8%2BXkIVRxw8aSBsUbczT94TBP52IWnaNEUIhyWiETJZ1vEEE03GHkEkChn7r6opuytOKY8%2BSmQlGqcfoufmQEVCqIwS0%2FiG4iJZSJ9j7ILLw3deBRfl7enNJlD2v6tu47lj1%2FztBH0hFyeSNRlzeBBFVyrJ8KpMqQYB%2B5RJwjLdmRZIBhz7Ln7mc2faR%2FIgHxNXXZwPDYFH5ikIKN2c6Wra1is%2F&X-Amz-Signature=29a5644f3c771c437b9179a30f010ac965489aeb2c12ee33a972425d003b5035&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
