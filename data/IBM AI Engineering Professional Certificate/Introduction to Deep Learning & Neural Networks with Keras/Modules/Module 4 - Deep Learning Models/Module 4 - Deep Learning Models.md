

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S6WSKW2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB784L85eBC359vfI82b2KoRcrRaSqNJOgpj5jWMQpD5AiBnWmMbNYdH%2BNYcK6TkkPtTLVPCVPegz1PZhsAUOmo%2B6iqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8kNjsc0PQQ%2FYyhfAKtwD7DFeHhXVpVGZmm2dMdDE0uEEPyw5hdBo0gYlJ5bgTtisuh35Hq7G6cNHZDTimGoHW6egC560PD1ZDsvXxWbm2yXwtaEwlPUfb2kp3pMhcpgby1l7F7uIQn9FZ8Dp85iUG1I9PYNtcwXvudujkEJGv1LaqDqFSrqrxDrlQOV22na6BoIX%2BEIjCSj81Qq8OHGG8Wx7mzdJKR%2BaOeH9%2BZePpYrLPuV8WY1qBG98zguOdDYliS%2FiyPIic%2FBPY%2F2mmuVroB2OVSiVnjxGr9csqyqkt4%2F2ZC3Beo%2BWcLNnql87y9RipPzQjIo%2BxvsFYbSyJsR0OjAQc6VmjI1ZTDasmySBlFqwJ55S33wB9TB1%2FaX0EB2KwahPgbAW4fLmruFQIsM5hPtoO0BX0KyE22YDsO5KQprGqyF7u0N4Tb7ZWiiNK79ALoJt5yMWR2QDzNpvBw5QgCKSUwPfmHCovRHUD9N6pQDCQ2rAjDEc86OChetqMCGJFMnDxvJxPyMm2pla2Ra3uqUkhcx4maWl%2BhVbaRQOLOEngeNiNs285WeUnX2Ks%2BphebZS1B4T9D8QFSINdMaqAVUF%2Fm9dqtZRE%2FllmdlpCy8%2FmkbPsl%2BINc097LXixVC7EaCMzfaTRj0ZNn8wkuX%2FvAY6pgEe2Ys2vqmmR4EMef2mY1zR%2BK2Va79BJiIFmaC%2BgDYh9nUJbQA3MrwX6H7Edh6%2FJ9BuYpRuKq1l57ExjGv6sp2FFMZfyjWiiUve0oa3IZRN5V209pLg0nsTQSny71nfwUjGRa%2BBtBEhfIzp8BWflLo47TvurcUQLlncuINfUZlC8Pml7SHUhXVguaNmUpeB446k6dIO2Q3iDBjtSP26TLBEUccRaezD&X-Amz-Signature=8e5ffc2f8d58a76199a6985be5f1f96e930e289e50ca11aace2c6cb3b1ba5b31&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S6WSKW2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB784L85eBC359vfI82b2KoRcrRaSqNJOgpj5jWMQpD5AiBnWmMbNYdH%2BNYcK6TkkPtTLVPCVPegz1PZhsAUOmo%2B6iqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8kNjsc0PQQ%2FYyhfAKtwD7DFeHhXVpVGZmm2dMdDE0uEEPyw5hdBo0gYlJ5bgTtisuh35Hq7G6cNHZDTimGoHW6egC560PD1ZDsvXxWbm2yXwtaEwlPUfb2kp3pMhcpgby1l7F7uIQn9FZ8Dp85iUG1I9PYNtcwXvudujkEJGv1LaqDqFSrqrxDrlQOV22na6BoIX%2BEIjCSj81Qq8OHGG8Wx7mzdJKR%2BaOeH9%2BZePpYrLPuV8WY1qBG98zguOdDYliS%2FiyPIic%2FBPY%2F2mmuVroB2OVSiVnjxGr9csqyqkt4%2F2ZC3Beo%2BWcLNnql87y9RipPzQjIo%2BxvsFYbSyJsR0OjAQc6VmjI1ZTDasmySBlFqwJ55S33wB9TB1%2FaX0EB2KwahPgbAW4fLmruFQIsM5hPtoO0BX0KyE22YDsO5KQprGqyF7u0N4Tb7ZWiiNK79ALoJt5yMWR2QDzNpvBw5QgCKSUwPfmHCovRHUD9N6pQDCQ2rAjDEc86OChetqMCGJFMnDxvJxPyMm2pla2Ra3uqUkhcx4maWl%2BhVbaRQOLOEngeNiNs285WeUnX2Ks%2BphebZS1B4T9D8QFSINdMaqAVUF%2Fm9dqtZRE%2FllmdlpCy8%2FmkbPsl%2BINc097LXixVC7EaCMzfaTRj0ZNn8wkuX%2FvAY6pgEe2Ys2vqmmR4EMef2mY1zR%2BK2Va79BJiIFmaC%2BgDYh9nUJbQA3MrwX6H7Edh6%2FJ9BuYpRuKq1l57ExjGv6sp2FFMZfyjWiiUve0oa3IZRN5V209pLg0nsTQSny71nfwUjGRa%2BBtBEhfIzp8BWflLo47TvurcUQLlncuINfUZlC8Pml7SHUhXVguaNmUpeB446k6dIO2Q3iDBjtSP26TLBEUccRaezD&X-Amz-Signature=a821d6012a24a484551a3d5f813cdab92fd4240d8b82af9207b5ace93d030ff6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S6WSKW2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB784L85eBC359vfI82b2KoRcrRaSqNJOgpj5jWMQpD5AiBnWmMbNYdH%2BNYcK6TkkPtTLVPCVPegz1PZhsAUOmo%2B6iqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8kNjsc0PQQ%2FYyhfAKtwD7DFeHhXVpVGZmm2dMdDE0uEEPyw5hdBo0gYlJ5bgTtisuh35Hq7G6cNHZDTimGoHW6egC560PD1ZDsvXxWbm2yXwtaEwlPUfb2kp3pMhcpgby1l7F7uIQn9FZ8Dp85iUG1I9PYNtcwXvudujkEJGv1LaqDqFSrqrxDrlQOV22na6BoIX%2BEIjCSj81Qq8OHGG8Wx7mzdJKR%2BaOeH9%2BZePpYrLPuV8WY1qBG98zguOdDYliS%2FiyPIic%2FBPY%2F2mmuVroB2OVSiVnjxGr9csqyqkt4%2F2ZC3Beo%2BWcLNnql87y9RipPzQjIo%2BxvsFYbSyJsR0OjAQc6VmjI1ZTDasmySBlFqwJ55S33wB9TB1%2FaX0EB2KwahPgbAW4fLmruFQIsM5hPtoO0BX0KyE22YDsO5KQprGqyF7u0N4Tb7ZWiiNK79ALoJt5yMWR2QDzNpvBw5QgCKSUwPfmHCovRHUD9N6pQDCQ2rAjDEc86OChetqMCGJFMnDxvJxPyMm2pla2Ra3uqUkhcx4maWl%2BhVbaRQOLOEngeNiNs285WeUnX2Ks%2BphebZS1B4T9D8QFSINdMaqAVUF%2Fm9dqtZRE%2FllmdlpCy8%2FmkbPsl%2BINc097LXixVC7EaCMzfaTRj0ZNn8wkuX%2FvAY6pgEe2Ys2vqmmR4EMef2mY1zR%2BK2Va79BJiIFmaC%2BgDYh9nUJbQA3MrwX6H7Edh6%2FJ9BuYpRuKq1l57ExjGv6sp2FFMZfyjWiiUve0oa3IZRN5V209pLg0nsTQSny71nfwUjGRa%2BBtBEhfIzp8BWflLo47TvurcUQLlncuINfUZlC8Pml7SHUhXVguaNmUpeB446k6dIO2Q3iDBjtSP26TLBEUccRaezD&X-Amz-Signature=4338bb3732f437a84d155c3bb6c161be2589416bbd4a27d6978eaad27eee5e0f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S6WSKW2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB784L85eBC359vfI82b2KoRcrRaSqNJOgpj5jWMQpD5AiBnWmMbNYdH%2BNYcK6TkkPtTLVPCVPegz1PZhsAUOmo%2B6iqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8kNjsc0PQQ%2FYyhfAKtwD7DFeHhXVpVGZmm2dMdDE0uEEPyw5hdBo0gYlJ5bgTtisuh35Hq7G6cNHZDTimGoHW6egC560PD1ZDsvXxWbm2yXwtaEwlPUfb2kp3pMhcpgby1l7F7uIQn9FZ8Dp85iUG1I9PYNtcwXvudujkEJGv1LaqDqFSrqrxDrlQOV22na6BoIX%2BEIjCSj81Qq8OHGG8Wx7mzdJKR%2BaOeH9%2BZePpYrLPuV8WY1qBG98zguOdDYliS%2FiyPIic%2FBPY%2F2mmuVroB2OVSiVnjxGr9csqyqkt4%2F2ZC3Beo%2BWcLNnql87y9RipPzQjIo%2BxvsFYbSyJsR0OjAQc6VmjI1ZTDasmySBlFqwJ55S33wB9TB1%2FaX0EB2KwahPgbAW4fLmruFQIsM5hPtoO0BX0KyE22YDsO5KQprGqyF7u0N4Tb7ZWiiNK79ALoJt5yMWR2QDzNpvBw5QgCKSUwPfmHCovRHUD9N6pQDCQ2rAjDEc86OChetqMCGJFMnDxvJxPyMm2pla2Ra3uqUkhcx4maWl%2BhVbaRQOLOEngeNiNs285WeUnX2Ks%2BphebZS1B4T9D8QFSINdMaqAVUF%2Fm9dqtZRE%2FllmdlpCy8%2FmkbPsl%2BINc097LXixVC7EaCMzfaTRj0ZNn8wkuX%2FvAY6pgEe2Ys2vqmmR4EMef2mY1zR%2BK2Va79BJiIFmaC%2BgDYh9nUJbQA3MrwX6H7Edh6%2FJ9BuYpRuKq1l57ExjGv6sp2FFMZfyjWiiUve0oa3IZRN5V209pLg0nsTQSny71nfwUjGRa%2BBtBEhfIzp8BWflLo47TvurcUQLlncuINfUZlC8Pml7SHUhXVguaNmUpeB446k6dIO2Q3iDBjtSP26TLBEUccRaezD&X-Amz-Signature=7892b84be8960cf141519f287482c35ec70d8c7fa9bd713da9bc14b0820f24c0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S6WSKW2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB784L85eBC359vfI82b2KoRcrRaSqNJOgpj5jWMQpD5AiBnWmMbNYdH%2BNYcK6TkkPtTLVPCVPegz1PZhsAUOmo%2B6iqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8kNjsc0PQQ%2FYyhfAKtwD7DFeHhXVpVGZmm2dMdDE0uEEPyw5hdBo0gYlJ5bgTtisuh35Hq7G6cNHZDTimGoHW6egC560PD1ZDsvXxWbm2yXwtaEwlPUfb2kp3pMhcpgby1l7F7uIQn9FZ8Dp85iUG1I9PYNtcwXvudujkEJGv1LaqDqFSrqrxDrlQOV22na6BoIX%2BEIjCSj81Qq8OHGG8Wx7mzdJKR%2BaOeH9%2BZePpYrLPuV8WY1qBG98zguOdDYliS%2FiyPIic%2FBPY%2F2mmuVroB2OVSiVnjxGr9csqyqkt4%2F2ZC3Beo%2BWcLNnql87y9RipPzQjIo%2BxvsFYbSyJsR0OjAQc6VmjI1ZTDasmySBlFqwJ55S33wB9TB1%2FaX0EB2KwahPgbAW4fLmruFQIsM5hPtoO0BX0KyE22YDsO5KQprGqyF7u0N4Tb7ZWiiNK79ALoJt5yMWR2QDzNpvBw5QgCKSUwPfmHCovRHUD9N6pQDCQ2rAjDEc86OChetqMCGJFMnDxvJxPyMm2pla2Ra3uqUkhcx4maWl%2BhVbaRQOLOEngeNiNs285WeUnX2Ks%2BphebZS1B4T9D8QFSINdMaqAVUF%2Fm9dqtZRE%2FllmdlpCy8%2FmkbPsl%2BINc097LXixVC7EaCMzfaTRj0ZNn8wkuX%2FvAY6pgEe2Ys2vqmmR4EMef2mY1zR%2BK2Va79BJiIFmaC%2BgDYh9nUJbQA3MrwX6H7Edh6%2FJ9BuYpRuKq1l57ExjGv6sp2FFMZfyjWiiUve0oa3IZRN5V209pLg0nsTQSny71nfwUjGRa%2BBtBEhfIzp8BWflLo47TvurcUQLlncuINfUZlC8Pml7SHUhXVguaNmUpeB446k6dIO2Q3iDBjtSP26TLBEUccRaezD&X-Amz-Signature=c2c3fe873b665b2236134a02133635e809d4ea98258551f71dd4e74e443e8405&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S6WSKW2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB784L85eBC359vfI82b2KoRcrRaSqNJOgpj5jWMQpD5AiBnWmMbNYdH%2BNYcK6TkkPtTLVPCVPegz1PZhsAUOmo%2B6iqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8kNjsc0PQQ%2FYyhfAKtwD7DFeHhXVpVGZmm2dMdDE0uEEPyw5hdBo0gYlJ5bgTtisuh35Hq7G6cNHZDTimGoHW6egC560PD1ZDsvXxWbm2yXwtaEwlPUfb2kp3pMhcpgby1l7F7uIQn9FZ8Dp85iUG1I9PYNtcwXvudujkEJGv1LaqDqFSrqrxDrlQOV22na6BoIX%2BEIjCSj81Qq8OHGG8Wx7mzdJKR%2BaOeH9%2BZePpYrLPuV8WY1qBG98zguOdDYliS%2FiyPIic%2FBPY%2F2mmuVroB2OVSiVnjxGr9csqyqkt4%2F2ZC3Beo%2BWcLNnql87y9RipPzQjIo%2BxvsFYbSyJsR0OjAQc6VmjI1ZTDasmySBlFqwJ55S33wB9TB1%2FaX0EB2KwahPgbAW4fLmruFQIsM5hPtoO0BX0KyE22YDsO5KQprGqyF7u0N4Tb7ZWiiNK79ALoJt5yMWR2QDzNpvBw5QgCKSUwPfmHCovRHUD9N6pQDCQ2rAjDEc86OChetqMCGJFMnDxvJxPyMm2pla2Ra3uqUkhcx4maWl%2BhVbaRQOLOEngeNiNs285WeUnX2Ks%2BphebZS1B4T9D8QFSINdMaqAVUF%2Fm9dqtZRE%2FllmdlpCy8%2FmkbPsl%2BINc097LXixVC7EaCMzfaTRj0ZNn8wkuX%2FvAY6pgEe2Ys2vqmmR4EMef2mY1zR%2BK2Va79BJiIFmaC%2BgDYh9nUJbQA3MrwX6H7Edh6%2FJ9BuYpRuKq1l57ExjGv6sp2FFMZfyjWiiUve0oa3IZRN5V209pLg0nsTQSny71nfwUjGRa%2BBtBEhfIzp8BWflLo47TvurcUQLlncuINfUZlC8Pml7SHUhXVguaNmUpeB446k6dIO2Q3iDBjtSP26TLBEUccRaezD&X-Amz-Signature=4ceb71c1443cbc0e12af8094fb156b22778ce251fbf51be50a56de9e62c06e5e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S6WSKW2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB784L85eBC359vfI82b2KoRcrRaSqNJOgpj5jWMQpD5AiBnWmMbNYdH%2BNYcK6TkkPtTLVPCVPegz1PZhsAUOmo%2B6iqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8kNjsc0PQQ%2FYyhfAKtwD7DFeHhXVpVGZmm2dMdDE0uEEPyw5hdBo0gYlJ5bgTtisuh35Hq7G6cNHZDTimGoHW6egC560PD1ZDsvXxWbm2yXwtaEwlPUfb2kp3pMhcpgby1l7F7uIQn9FZ8Dp85iUG1I9PYNtcwXvudujkEJGv1LaqDqFSrqrxDrlQOV22na6BoIX%2BEIjCSj81Qq8OHGG8Wx7mzdJKR%2BaOeH9%2BZePpYrLPuV8WY1qBG98zguOdDYliS%2FiyPIic%2FBPY%2F2mmuVroB2OVSiVnjxGr9csqyqkt4%2F2ZC3Beo%2BWcLNnql87y9RipPzQjIo%2BxvsFYbSyJsR0OjAQc6VmjI1ZTDasmySBlFqwJ55S33wB9TB1%2FaX0EB2KwahPgbAW4fLmruFQIsM5hPtoO0BX0KyE22YDsO5KQprGqyF7u0N4Tb7ZWiiNK79ALoJt5yMWR2QDzNpvBw5QgCKSUwPfmHCovRHUD9N6pQDCQ2rAjDEc86OChetqMCGJFMnDxvJxPyMm2pla2Ra3uqUkhcx4maWl%2BhVbaRQOLOEngeNiNs285WeUnX2Ks%2BphebZS1B4T9D8QFSINdMaqAVUF%2Fm9dqtZRE%2FllmdlpCy8%2FmkbPsl%2BINc097LXixVC7EaCMzfaTRj0ZNn8wkuX%2FvAY6pgEe2Ys2vqmmR4EMef2mY1zR%2BK2Va79BJiIFmaC%2BgDYh9nUJbQA3MrwX6H7Edh6%2FJ9BuYpRuKq1l57ExjGv6sp2FFMZfyjWiiUve0oa3IZRN5V209pLg0nsTQSny71nfwUjGRa%2BBtBEhfIzp8BWflLo47TvurcUQLlncuINfUZlC8Pml7SHUhXVguaNmUpeB446k6dIO2Q3iDBjtSP26TLBEUccRaezD&X-Amz-Signature=4f71f917eb2204e2a6ccecaa845f1ede38ecccd51cd8a643d1147fc1ff104465&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S6WSKW2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB784L85eBC359vfI82b2KoRcrRaSqNJOgpj5jWMQpD5AiBnWmMbNYdH%2BNYcK6TkkPtTLVPCVPegz1PZhsAUOmo%2B6iqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8kNjsc0PQQ%2FYyhfAKtwD7DFeHhXVpVGZmm2dMdDE0uEEPyw5hdBo0gYlJ5bgTtisuh35Hq7G6cNHZDTimGoHW6egC560PD1ZDsvXxWbm2yXwtaEwlPUfb2kp3pMhcpgby1l7F7uIQn9FZ8Dp85iUG1I9PYNtcwXvudujkEJGv1LaqDqFSrqrxDrlQOV22na6BoIX%2BEIjCSj81Qq8OHGG8Wx7mzdJKR%2BaOeH9%2BZePpYrLPuV8WY1qBG98zguOdDYliS%2FiyPIic%2FBPY%2F2mmuVroB2OVSiVnjxGr9csqyqkt4%2F2ZC3Beo%2BWcLNnql87y9RipPzQjIo%2BxvsFYbSyJsR0OjAQc6VmjI1ZTDasmySBlFqwJ55S33wB9TB1%2FaX0EB2KwahPgbAW4fLmruFQIsM5hPtoO0BX0KyE22YDsO5KQprGqyF7u0N4Tb7ZWiiNK79ALoJt5yMWR2QDzNpvBw5QgCKSUwPfmHCovRHUD9N6pQDCQ2rAjDEc86OChetqMCGJFMnDxvJxPyMm2pla2Ra3uqUkhcx4maWl%2BhVbaRQOLOEngeNiNs285WeUnX2Ks%2BphebZS1B4T9D8QFSINdMaqAVUF%2Fm9dqtZRE%2FllmdlpCy8%2FmkbPsl%2BINc097LXixVC7EaCMzfaTRj0ZNn8wkuX%2FvAY6pgEe2Ys2vqmmR4EMef2mY1zR%2BK2Va79BJiIFmaC%2BgDYh9nUJbQA3MrwX6H7Edh6%2FJ9BuYpRuKq1l57ExjGv6sp2FFMZfyjWiiUve0oa3IZRN5V209pLg0nsTQSny71nfwUjGRa%2BBtBEhfIzp8BWflLo47TvurcUQLlncuINfUZlC8Pml7SHUhXVguaNmUpeB446k6dIO2Q3iDBjtSP26TLBEUccRaezD&X-Amz-Signature=a682d5958c0aed86e8a8d8fbff24363e2014fc4820ac0740f534b65d62e27f3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S6WSKW2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB784L85eBC359vfI82b2KoRcrRaSqNJOgpj5jWMQpD5AiBnWmMbNYdH%2BNYcK6TkkPtTLVPCVPegz1PZhsAUOmo%2B6iqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8kNjsc0PQQ%2FYyhfAKtwD7DFeHhXVpVGZmm2dMdDE0uEEPyw5hdBo0gYlJ5bgTtisuh35Hq7G6cNHZDTimGoHW6egC560PD1ZDsvXxWbm2yXwtaEwlPUfb2kp3pMhcpgby1l7F7uIQn9FZ8Dp85iUG1I9PYNtcwXvudujkEJGv1LaqDqFSrqrxDrlQOV22na6BoIX%2BEIjCSj81Qq8OHGG8Wx7mzdJKR%2BaOeH9%2BZePpYrLPuV8WY1qBG98zguOdDYliS%2FiyPIic%2FBPY%2F2mmuVroB2OVSiVnjxGr9csqyqkt4%2F2ZC3Beo%2BWcLNnql87y9RipPzQjIo%2BxvsFYbSyJsR0OjAQc6VmjI1ZTDasmySBlFqwJ55S33wB9TB1%2FaX0EB2KwahPgbAW4fLmruFQIsM5hPtoO0BX0KyE22YDsO5KQprGqyF7u0N4Tb7ZWiiNK79ALoJt5yMWR2QDzNpvBw5QgCKSUwPfmHCovRHUD9N6pQDCQ2rAjDEc86OChetqMCGJFMnDxvJxPyMm2pla2Ra3uqUkhcx4maWl%2BhVbaRQOLOEngeNiNs285WeUnX2Ks%2BphebZS1B4T9D8QFSINdMaqAVUF%2Fm9dqtZRE%2FllmdlpCy8%2FmkbPsl%2BINc097LXixVC7EaCMzfaTRj0ZNn8wkuX%2FvAY6pgEe2Ys2vqmmR4EMef2mY1zR%2BK2Va79BJiIFmaC%2BgDYh9nUJbQA3MrwX6H7Edh6%2FJ9BuYpRuKq1l57ExjGv6sp2FFMZfyjWiiUve0oa3IZRN5V209pLg0nsTQSny71nfwUjGRa%2BBtBEhfIzp8BWflLo47TvurcUQLlncuINfUZlC8Pml7SHUhXVguaNmUpeB446k6dIO2Q3iDBjtSP26TLBEUccRaezD&X-Amz-Signature=5909d95d6121fd8cac73d57e4d03df03813417d5a00839535b55953632ed5bc5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LKV2MTV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEy2d5xSHhuhAkwJNPVr3KEJgkQ7MoYiVPXDoa1y6l4qAiEA%2BQp9DwEIdMUCdyP9t6vwg1yEKHpcf3fsjvnxt8DqzsgqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBFp0RZhJeuWt%2BMVpCrcA14HuuTUp5dFPv3FnPr1HqPeCvE%2BsdCm%2FCAvbIHWeoMx2vBNQ6r2jRfEygn58zrPN4WiAwJ%2B%2B0wFMSeDdus16iMVfcFj1MrpaZrw%2Bs8pcrZCrSEo9pOPP%2BaNuN5CBnEKSErjj9hT%2BM2c8w4qcuwX6xZaNB%2Fm6K7XxHv9tOYgZkOFq2o1qWzfdNZNLSOe1qm4p%2BMI8t2MlzDTJoZsZhE3K5AW3hGs8lS2unX0Zia2gAMctnbkn78IRQJmyPPVwnPdcVHrXKUPSXaYTNXTz%2BYzE79FollDBAkE14oqTugJ%2BYDkBd5F5BjbtgxBO8itoTKrrjHitCxkf5J0mmOzgy4RPvKfDyb2KGbce9C%2BlvSj1OCUuJtL%2FXMNlI2X050SFlFJvIWuvif2mgER6qGFkuuhvvlSOrY6GvOpKkUEsyGtglA8wIP0U63Y%2FBVI0XS6u1SL%2BsrbpFihBKLJkcTmxSpFb8dUlAjVdYuMd2aj4QRF03Jb5wSRiLMvFevAj0MmMac1XxwC4JYfn5ndLp9AxsLB91alpHeTlitE9VIZToNk%2B16F6XcqTmMURz6tGHiygWU%2FgPzwKIvAheAEA8HQOADfPcgs%2B8PgOYBeYVXWv4bqpWO%2B1v4mQqnAYaFhQs1TMLLl%2F7wGOqUBOiKDzSqIn4wzXivw82bNltwKAcGFbXdTJH4P1qI%2BG8lafCHLLJwvzZcY1IiXxdrXSB7%2F7PLqoU1CFQrGPIdbGP%2F%2B3zKgbT3RTIi74E0hA6ZIYvRgyHHR3J6Eo2u%2BmrALdUaoxvzvBdg4YVLNXtu0GlUyPDfKjH4zeXQo2DuqoVckFpqCgDXFtXdVuHcgAKwSHjinSnUJtbFJ64QeP8ZYGe%2Bp8cA0&X-Amz-Signature=d0c1d0faf6a103fc0e0ce4d5e9861050bf08bba3c65555c7958e13ad5cd9e021&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LKV2MTV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEy2d5xSHhuhAkwJNPVr3KEJgkQ7MoYiVPXDoa1y6l4qAiEA%2BQp9DwEIdMUCdyP9t6vwg1yEKHpcf3fsjvnxt8DqzsgqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBFp0RZhJeuWt%2BMVpCrcA14HuuTUp5dFPv3FnPr1HqPeCvE%2BsdCm%2FCAvbIHWeoMx2vBNQ6r2jRfEygn58zrPN4WiAwJ%2B%2B0wFMSeDdus16iMVfcFj1MrpaZrw%2Bs8pcrZCrSEo9pOPP%2BaNuN5CBnEKSErjj9hT%2BM2c8w4qcuwX6xZaNB%2Fm6K7XxHv9tOYgZkOFq2o1qWzfdNZNLSOe1qm4p%2BMI8t2MlzDTJoZsZhE3K5AW3hGs8lS2unX0Zia2gAMctnbkn78IRQJmyPPVwnPdcVHrXKUPSXaYTNXTz%2BYzE79FollDBAkE14oqTugJ%2BYDkBd5F5BjbtgxBO8itoTKrrjHitCxkf5J0mmOzgy4RPvKfDyb2KGbce9C%2BlvSj1OCUuJtL%2FXMNlI2X050SFlFJvIWuvif2mgER6qGFkuuhvvlSOrY6GvOpKkUEsyGtglA8wIP0U63Y%2FBVI0XS6u1SL%2BsrbpFihBKLJkcTmxSpFb8dUlAjVdYuMd2aj4QRF03Jb5wSRiLMvFevAj0MmMac1XxwC4JYfn5ndLp9AxsLB91alpHeTlitE9VIZToNk%2B16F6XcqTmMURz6tGHiygWU%2FgPzwKIvAheAEA8HQOADfPcgs%2B8PgOYBeYVXWv4bqpWO%2B1v4mQqnAYaFhQs1TMLLl%2F7wGOqUBOiKDzSqIn4wzXivw82bNltwKAcGFbXdTJH4P1qI%2BG8lafCHLLJwvzZcY1IiXxdrXSB7%2F7PLqoU1CFQrGPIdbGP%2F%2B3zKgbT3RTIi74E0hA6ZIYvRgyHHR3J6Eo2u%2BmrALdUaoxvzvBdg4YVLNXtu0GlUyPDfKjH4zeXQo2DuqoVckFpqCgDXFtXdVuHcgAKwSHjinSnUJtbFJ64QeP8ZYGe%2Bp8cA0&X-Amz-Signature=7cf25c2477bcee59e0b74d97ad19c80188dff7332e9fe1f76bcc7e7ed1363a57&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
