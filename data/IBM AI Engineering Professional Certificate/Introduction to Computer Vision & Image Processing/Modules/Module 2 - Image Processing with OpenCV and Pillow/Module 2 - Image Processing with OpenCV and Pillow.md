

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZOJCMAM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArxtY%2BZGNMQAd119ckdl7hBn9VzRN1cYVuqvwTy93Y2AiBaK6AMbPwaJKCeesqRYkwO9C7fGrdd5BF4b%2B67XWmbiSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF8sr8J4LlA55TXG1KtwDwyeuZ9lxPQ6%2F0gY4reaJ17afj1P93O9eK8le4ChhDTJddhZlX57%2BAK%2FgB51L5PJPYAheN6DhBc205RRDw21tWmBCTb6UM8rP0NjGt4crcXM3UJOGKZTTxCgkHZoNw2Nga%2BmLffUxWRfr4ZROzoGgVV1Wyn9GLuS8DTEPV31C3jpIR5MAv4NpbBU6bwHF2sr%2FO5abh5nYsoPqoypygOrqpA4SGjTqf0kQKcb5yU7GbguPPnkjtKNIEepmXi6VCF9026FUc4UP9%2Bh9nfHdmhNxygJHu9GIUTozGqWjhewRU2IdEzh%2FA6Uj0ekt3T%2FZab0Dqvs20TnJ14Ioi73yimjXCcyUjI66XZPGtiwIPzaOnw5LuhfZpT81TTBgjoP5qGeQm9XowYHG9J%2Fzbz6o8bKXoOgoiRLlkLW%2FdiGbSYiFBGF12QoQtyhzt%2BcLDNLILmABic%2B1%2F0CPOBXM0peNdunaiDloj%2FfjQ8IOHTN7gdZZf9amAP9Zhqs6D%2FMP9lWtk9UMkfM6SAI83Ln3iJo6YRVEJdsV68rebrwq2klSixa6DbcPQ6nztTW1OsLRNIQZWD27BnzfV2ag5m2y9xMHvXwGGLmCAsahd4NcFlI0HVWDC7jkbx2O4Lc0pSrtoL4wl6X3vAY6pgFhLqMLQi6tIYcrkDfydUhj5IYfYGkrJmqe%2BHZFNAbiN3ZyUuk9lIaRAkf9BUlWfK%2BE3%2BFnYkIKLjNEdUPF4SQDqK4UxEneQ8Iy1mr2PMJ6cT%2FTGOrnp8p7lVZ0iNU%2B3tvM26vm0S56ogzaS2jlmSlvytdNHX4kTDBr7%2BVdEUOVrXdPixTMUo6hEYjC8vANtB0rN4FXKBFcA94w%2BAskOgOFFtdAERzC&X-Amz-Signature=bdfa34fd6dd6fc8b10f54a961133db45ede225cf4db057951c21012dce2390de&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ECRPG35%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClRUzdCRCF5O%2BNoRpIDAkaacrvbUZvfxMwoEPh2WfvzAiEA8ErwuH%2BZvFvdwp84l7YOz5pcVlBSHcenbYTtI1P7fvkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXd2uADr75xNbwtiircAxUSvC0xao7A%2FiKzl7d9O70gq1IldUssj7P6nZn4BFIsb8Up1cdOyLlw22o5SdeFLVQZ0v8NFjM%2F4bDGT87ZMXM%2FKl6rui7251aX8PumWLT9%2B8vPy2qtCmHYkh9np3JZDa1P2Zt%2FNfowqcr4eOw6FVzLMoIzPcRGxtERKvh4VO07tIFCAOpcHJVbdoBHlVVR6va039HuNQf3cNdwpT7h2Zmxg0fm1lXLbzbwrVxOT8GV5HZOBcUXztIV7I0QWksPYZEAHmhmofl%2FT1Z22J9wPLO%2Bn0kOHggHP%2FQWDdjSNFKDUwuNvjxPkRou7L7isq8DcSlJie%2F2D2eHkkeqIjy77XE2afRqITlx05mEKU1srSp3Cxw5po7P21JZgIHzDxkNtzOucAaKpgolQiFmBYcMZNhzbjUanLeHEe4d4wDHdv98D1VwivAmUOhq%2Fo%2FTvWk6U1G5NtywEaxNuMdIu3eU8vP7ClJ4X2Ir8kriOmr08AbONN1VWfoV4N7hWwlatSsva%2BGSucLM9GHTEQ4ZHN9pO1lTuCx%2B%2FBD02IjXfslYeTssmuxvoWF5hKLrvKc4GflZhzO%2FI1J%2FjlStgyiKvM2%2Ff2zFreeEIfk%2BGw3pFRo%2FBy5dGIJzhDV%2FWX1YPJX5MKWk97wGOqUBy7c%2Bz8Jmvm4mAVQed1TSzxQadKnem5zxThQGor6c56OMnXxP1IvoEaga1vKFlE5zMW2Zr2hNumrpVYzwPRA9b4o8ry0QnPwmMRPDf5fFTUsDUFyF0E%2BSGgaiMrkYBhHNiG%2Bl8OOcgNOOotNxnFXEvjUjHjoXhNcRoo5FTqGOl7qVEwWV8O%2BOrMNBbyimA%2BFOStlVcWO8vKjjOdK3YtaiI7yXL52u&X-Amz-Signature=5300f51e6cc6954614b9f2575d3e9f2ecb1546b058314d9dd5a6fe59be291a18&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ECRPG35%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClRUzdCRCF5O%2BNoRpIDAkaacrvbUZvfxMwoEPh2WfvzAiEA8ErwuH%2BZvFvdwp84l7YOz5pcVlBSHcenbYTtI1P7fvkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXd2uADr75xNbwtiircAxUSvC0xao7A%2FiKzl7d9O70gq1IldUssj7P6nZn4BFIsb8Up1cdOyLlw22o5SdeFLVQZ0v8NFjM%2F4bDGT87ZMXM%2FKl6rui7251aX8PumWLT9%2B8vPy2qtCmHYkh9np3JZDa1P2Zt%2FNfowqcr4eOw6FVzLMoIzPcRGxtERKvh4VO07tIFCAOpcHJVbdoBHlVVR6va039HuNQf3cNdwpT7h2Zmxg0fm1lXLbzbwrVxOT8GV5HZOBcUXztIV7I0QWksPYZEAHmhmofl%2FT1Z22J9wPLO%2Bn0kOHggHP%2FQWDdjSNFKDUwuNvjxPkRou7L7isq8DcSlJie%2F2D2eHkkeqIjy77XE2afRqITlx05mEKU1srSp3Cxw5po7P21JZgIHzDxkNtzOucAaKpgolQiFmBYcMZNhzbjUanLeHEe4d4wDHdv98D1VwivAmUOhq%2Fo%2FTvWk6U1G5NtywEaxNuMdIu3eU8vP7ClJ4X2Ir8kriOmr08AbONN1VWfoV4N7hWwlatSsva%2BGSucLM9GHTEQ4ZHN9pO1lTuCx%2B%2FBD02IjXfslYeTssmuxvoWF5hKLrvKc4GflZhzO%2FI1J%2FjlStgyiKvM2%2Ff2zFreeEIfk%2BGw3pFRo%2FBy5dGIJzhDV%2FWX1YPJX5MKWk97wGOqUBy7c%2Bz8Jmvm4mAVQed1TSzxQadKnem5zxThQGor6c56OMnXxP1IvoEaga1vKFlE5zMW2Zr2hNumrpVYzwPRA9b4o8ry0QnPwmMRPDf5fFTUsDUFyF0E%2BSGgaiMrkYBhHNiG%2Bl8OOcgNOOotNxnFXEvjUjHjoXhNcRoo5FTqGOl7qVEwWV8O%2BOrMNBbyimA%2BFOStlVcWO8vKjjOdK3YtaiI7yXL52u&X-Amz-Signature=b64a474a9079601f3202a944ba7733af4884237b458fa89a3c8225e988b9cf24&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ECRPG35%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClRUzdCRCF5O%2BNoRpIDAkaacrvbUZvfxMwoEPh2WfvzAiEA8ErwuH%2BZvFvdwp84l7YOz5pcVlBSHcenbYTtI1P7fvkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXd2uADr75xNbwtiircAxUSvC0xao7A%2FiKzl7d9O70gq1IldUssj7P6nZn4BFIsb8Up1cdOyLlw22o5SdeFLVQZ0v8NFjM%2F4bDGT87ZMXM%2FKl6rui7251aX8PumWLT9%2B8vPy2qtCmHYkh9np3JZDa1P2Zt%2FNfowqcr4eOw6FVzLMoIzPcRGxtERKvh4VO07tIFCAOpcHJVbdoBHlVVR6va039HuNQf3cNdwpT7h2Zmxg0fm1lXLbzbwrVxOT8GV5HZOBcUXztIV7I0QWksPYZEAHmhmofl%2FT1Z22J9wPLO%2Bn0kOHggHP%2FQWDdjSNFKDUwuNvjxPkRou7L7isq8DcSlJie%2F2D2eHkkeqIjy77XE2afRqITlx05mEKU1srSp3Cxw5po7P21JZgIHzDxkNtzOucAaKpgolQiFmBYcMZNhzbjUanLeHEe4d4wDHdv98D1VwivAmUOhq%2Fo%2FTvWk6U1G5NtywEaxNuMdIu3eU8vP7ClJ4X2Ir8kriOmr08AbONN1VWfoV4N7hWwlatSsva%2BGSucLM9GHTEQ4ZHN9pO1lTuCx%2B%2FBD02IjXfslYeTssmuxvoWF5hKLrvKc4GflZhzO%2FI1J%2FjlStgyiKvM2%2Ff2zFreeEIfk%2BGw3pFRo%2FBy5dGIJzhDV%2FWX1YPJX5MKWk97wGOqUBy7c%2Bz8Jmvm4mAVQed1TSzxQadKnem5zxThQGor6c56OMnXxP1IvoEaga1vKFlE5zMW2Zr2hNumrpVYzwPRA9b4o8ry0QnPwmMRPDf5fFTUsDUFyF0E%2BSGgaiMrkYBhHNiG%2Bl8OOcgNOOotNxnFXEvjUjHjoXhNcRoo5FTqGOl7qVEwWV8O%2BOrMNBbyimA%2BFOStlVcWO8vKjjOdK3YtaiI7yXL52u&X-Amz-Signature=af8c6221fd205faea24dc68f9c8cfe3c5442db2cd52fbdfa0bc1b2950325eb81&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ECRPG35%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClRUzdCRCF5O%2BNoRpIDAkaacrvbUZvfxMwoEPh2WfvzAiEA8ErwuH%2BZvFvdwp84l7YOz5pcVlBSHcenbYTtI1P7fvkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXd2uADr75xNbwtiircAxUSvC0xao7A%2FiKzl7d9O70gq1IldUssj7P6nZn4BFIsb8Up1cdOyLlw22o5SdeFLVQZ0v8NFjM%2F4bDGT87ZMXM%2FKl6rui7251aX8PumWLT9%2B8vPy2qtCmHYkh9np3JZDa1P2Zt%2FNfowqcr4eOw6FVzLMoIzPcRGxtERKvh4VO07tIFCAOpcHJVbdoBHlVVR6va039HuNQf3cNdwpT7h2Zmxg0fm1lXLbzbwrVxOT8GV5HZOBcUXztIV7I0QWksPYZEAHmhmofl%2FT1Z22J9wPLO%2Bn0kOHggHP%2FQWDdjSNFKDUwuNvjxPkRou7L7isq8DcSlJie%2F2D2eHkkeqIjy77XE2afRqITlx05mEKU1srSp3Cxw5po7P21JZgIHzDxkNtzOucAaKpgolQiFmBYcMZNhzbjUanLeHEe4d4wDHdv98D1VwivAmUOhq%2Fo%2FTvWk6U1G5NtywEaxNuMdIu3eU8vP7ClJ4X2Ir8kriOmr08AbONN1VWfoV4N7hWwlatSsva%2BGSucLM9GHTEQ4ZHN9pO1lTuCx%2B%2FBD02IjXfslYeTssmuxvoWF5hKLrvKc4GflZhzO%2FI1J%2FjlStgyiKvM2%2Ff2zFreeEIfk%2BGw3pFRo%2FBy5dGIJzhDV%2FWX1YPJX5MKWk97wGOqUBy7c%2Bz8Jmvm4mAVQed1TSzxQadKnem5zxThQGor6c56OMnXxP1IvoEaga1vKFlE5zMW2Zr2hNumrpVYzwPRA9b4o8ry0QnPwmMRPDf5fFTUsDUFyF0E%2BSGgaiMrkYBhHNiG%2Bl8OOcgNOOotNxnFXEvjUjHjoXhNcRoo5FTqGOl7qVEwWV8O%2BOrMNBbyimA%2BFOStlVcWO8vKjjOdK3YtaiI7yXL52u&X-Amz-Signature=82a0d2db42d60cefca6f835f4b5d466c1351e780e4fbf242110821ad4ceccc7b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ECRPG35%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClRUzdCRCF5O%2BNoRpIDAkaacrvbUZvfxMwoEPh2WfvzAiEA8ErwuH%2BZvFvdwp84l7YOz5pcVlBSHcenbYTtI1P7fvkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXd2uADr75xNbwtiircAxUSvC0xao7A%2FiKzl7d9O70gq1IldUssj7P6nZn4BFIsb8Up1cdOyLlw22o5SdeFLVQZ0v8NFjM%2F4bDGT87ZMXM%2FKl6rui7251aX8PumWLT9%2B8vPy2qtCmHYkh9np3JZDa1P2Zt%2FNfowqcr4eOw6FVzLMoIzPcRGxtERKvh4VO07tIFCAOpcHJVbdoBHlVVR6va039HuNQf3cNdwpT7h2Zmxg0fm1lXLbzbwrVxOT8GV5HZOBcUXztIV7I0QWksPYZEAHmhmofl%2FT1Z22J9wPLO%2Bn0kOHggHP%2FQWDdjSNFKDUwuNvjxPkRou7L7isq8DcSlJie%2F2D2eHkkeqIjy77XE2afRqITlx05mEKU1srSp3Cxw5po7P21JZgIHzDxkNtzOucAaKpgolQiFmBYcMZNhzbjUanLeHEe4d4wDHdv98D1VwivAmUOhq%2Fo%2FTvWk6U1G5NtywEaxNuMdIu3eU8vP7ClJ4X2Ir8kriOmr08AbONN1VWfoV4N7hWwlatSsva%2BGSucLM9GHTEQ4ZHN9pO1lTuCx%2B%2FBD02IjXfslYeTssmuxvoWF5hKLrvKc4GflZhzO%2FI1J%2FjlStgyiKvM2%2Ff2zFreeEIfk%2BGw3pFRo%2FBy5dGIJzhDV%2FWX1YPJX5MKWk97wGOqUBy7c%2Bz8Jmvm4mAVQed1TSzxQadKnem5zxThQGor6c56OMnXxP1IvoEaga1vKFlE5zMW2Zr2hNumrpVYzwPRA9b4o8ry0QnPwmMRPDf5fFTUsDUFyF0E%2BSGgaiMrkYBhHNiG%2Bl8OOcgNOOotNxnFXEvjUjHjoXhNcRoo5FTqGOl7qVEwWV8O%2BOrMNBbyimA%2BFOStlVcWO8vKjjOdK3YtaiI7yXL52u&X-Amz-Signature=892a2ba4120eb3d1ac8d813ee127e4b38636e06d42e96e01baf94b13c88063b6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZOJCMAM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArxtY%2BZGNMQAd119ckdl7hBn9VzRN1cYVuqvwTy93Y2AiBaK6AMbPwaJKCeesqRYkwO9C7fGrdd5BF4b%2B67XWmbiSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF8sr8J4LlA55TXG1KtwDwyeuZ9lxPQ6%2F0gY4reaJ17afj1P93O9eK8le4ChhDTJddhZlX57%2BAK%2FgB51L5PJPYAheN6DhBc205RRDw21tWmBCTb6UM8rP0NjGt4crcXM3UJOGKZTTxCgkHZoNw2Nga%2BmLffUxWRfr4ZROzoGgVV1Wyn9GLuS8DTEPV31C3jpIR5MAv4NpbBU6bwHF2sr%2FO5abh5nYsoPqoypygOrqpA4SGjTqf0kQKcb5yU7GbguPPnkjtKNIEepmXi6VCF9026FUc4UP9%2Bh9nfHdmhNxygJHu9GIUTozGqWjhewRU2IdEzh%2FA6Uj0ekt3T%2FZab0Dqvs20TnJ14Ioi73yimjXCcyUjI66XZPGtiwIPzaOnw5LuhfZpT81TTBgjoP5qGeQm9XowYHG9J%2Fzbz6o8bKXoOgoiRLlkLW%2FdiGbSYiFBGF12QoQtyhzt%2BcLDNLILmABic%2B1%2F0CPOBXM0peNdunaiDloj%2FfjQ8IOHTN7gdZZf9amAP9Zhqs6D%2FMP9lWtk9UMkfM6SAI83Ln3iJo6YRVEJdsV68rebrwq2klSixa6DbcPQ6nztTW1OsLRNIQZWD27BnzfV2ag5m2y9xMHvXwGGLmCAsahd4NcFlI0HVWDC7jkbx2O4Lc0pSrtoL4wl6X3vAY6pgFhLqMLQi6tIYcrkDfydUhj5IYfYGkrJmqe%2BHZFNAbiN3ZyUuk9lIaRAkf9BUlWfK%2BE3%2BFnYkIKLjNEdUPF4SQDqK4UxEneQ8Iy1mr2PMJ6cT%2FTGOrnp8p7lVZ0iNU%2B3tvM26vm0S56ogzaS2jlmSlvytdNHX4kTDBr7%2BVdEUOVrXdPixTMUo6hEYjC8vANtB0rN4FXKBFcA94w%2BAskOgOFFtdAERzC&X-Amz-Signature=50c04fc6863e1801be6ce1db9381010e86e4d6ec9d27bdf687307961e8915a87&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZOJCMAM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArxtY%2BZGNMQAd119ckdl7hBn9VzRN1cYVuqvwTy93Y2AiBaK6AMbPwaJKCeesqRYkwO9C7fGrdd5BF4b%2B67XWmbiSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF8sr8J4LlA55TXG1KtwDwyeuZ9lxPQ6%2F0gY4reaJ17afj1P93O9eK8le4ChhDTJddhZlX57%2BAK%2FgB51L5PJPYAheN6DhBc205RRDw21tWmBCTb6UM8rP0NjGt4crcXM3UJOGKZTTxCgkHZoNw2Nga%2BmLffUxWRfr4ZROzoGgVV1Wyn9GLuS8DTEPV31C3jpIR5MAv4NpbBU6bwHF2sr%2FO5abh5nYsoPqoypygOrqpA4SGjTqf0kQKcb5yU7GbguPPnkjtKNIEepmXi6VCF9026FUc4UP9%2Bh9nfHdmhNxygJHu9GIUTozGqWjhewRU2IdEzh%2FA6Uj0ekt3T%2FZab0Dqvs20TnJ14Ioi73yimjXCcyUjI66XZPGtiwIPzaOnw5LuhfZpT81TTBgjoP5qGeQm9XowYHG9J%2Fzbz6o8bKXoOgoiRLlkLW%2FdiGbSYiFBGF12QoQtyhzt%2BcLDNLILmABic%2B1%2F0CPOBXM0peNdunaiDloj%2FfjQ8IOHTN7gdZZf9amAP9Zhqs6D%2FMP9lWtk9UMkfM6SAI83Ln3iJo6YRVEJdsV68rebrwq2klSixa6DbcPQ6nztTW1OsLRNIQZWD27BnzfV2ag5m2y9xMHvXwGGLmCAsahd4NcFlI0HVWDC7jkbx2O4Lc0pSrtoL4wl6X3vAY6pgFhLqMLQi6tIYcrkDfydUhj5IYfYGkrJmqe%2BHZFNAbiN3ZyUuk9lIaRAkf9BUlWfK%2BE3%2BFnYkIKLjNEdUPF4SQDqK4UxEneQ8Iy1mr2PMJ6cT%2FTGOrnp8p7lVZ0iNU%2B3tvM26vm0S56ogzaS2jlmSlvytdNHX4kTDBr7%2BVdEUOVrXdPixTMUo6hEYjC8vANtB0rN4FXKBFcA94w%2BAskOgOFFtdAERzC&X-Amz-Signature=f2d75842677da2f77715261ec5625ecbc5db57f326895cff6aed4e0aba3e38e4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZOJCMAM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArxtY%2BZGNMQAd119ckdl7hBn9VzRN1cYVuqvwTy93Y2AiBaK6AMbPwaJKCeesqRYkwO9C7fGrdd5BF4b%2B67XWmbiSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF8sr8J4LlA55TXG1KtwDwyeuZ9lxPQ6%2F0gY4reaJ17afj1P93O9eK8le4ChhDTJddhZlX57%2BAK%2FgB51L5PJPYAheN6DhBc205RRDw21tWmBCTb6UM8rP0NjGt4crcXM3UJOGKZTTxCgkHZoNw2Nga%2BmLffUxWRfr4ZROzoGgVV1Wyn9GLuS8DTEPV31C3jpIR5MAv4NpbBU6bwHF2sr%2FO5abh5nYsoPqoypygOrqpA4SGjTqf0kQKcb5yU7GbguPPnkjtKNIEepmXi6VCF9026FUc4UP9%2Bh9nfHdmhNxygJHu9GIUTozGqWjhewRU2IdEzh%2FA6Uj0ekt3T%2FZab0Dqvs20TnJ14Ioi73yimjXCcyUjI66XZPGtiwIPzaOnw5LuhfZpT81TTBgjoP5qGeQm9XowYHG9J%2Fzbz6o8bKXoOgoiRLlkLW%2FdiGbSYiFBGF12QoQtyhzt%2BcLDNLILmABic%2B1%2F0CPOBXM0peNdunaiDloj%2FfjQ8IOHTN7gdZZf9amAP9Zhqs6D%2FMP9lWtk9UMkfM6SAI83Ln3iJo6YRVEJdsV68rebrwq2klSixa6DbcPQ6nztTW1OsLRNIQZWD27BnzfV2ag5m2y9xMHvXwGGLmCAsahd4NcFlI0HVWDC7jkbx2O4Lc0pSrtoL4wl6X3vAY6pgFhLqMLQi6tIYcrkDfydUhj5IYfYGkrJmqe%2BHZFNAbiN3ZyUuk9lIaRAkf9BUlWfK%2BE3%2BFnYkIKLjNEdUPF4SQDqK4UxEneQ8Iy1mr2PMJ6cT%2FTGOrnp8p7lVZ0iNU%2B3tvM26vm0S56ogzaS2jlmSlvytdNHX4kTDBr7%2BVdEUOVrXdPixTMUo6hEYjC8vANtB0rN4FXKBFcA94w%2BAskOgOFFtdAERzC&X-Amz-Signature=21679f77da8ce82e31d11ae80bda70e7c1dffef5e0e9395c4e5a173eef6645ec&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZOJCMAM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArxtY%2BZGNMQAd119ckdl7hBn9VzRN1cYVuqvwTy93Y2AiBaK6AMbPwaJKCeesqRYkwO9C7fGrdd5BF4b%2B67XWmbiSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF8sr8J4LlA55TXG1KtwDwyeuZ9lxPQ6%2F0gY4reaJ17afj1P93O9eK8le4ChhDTJddhZlX57%2BAK%2FgB51L5PJPYAheN6DhBc205RRDw21tWmBCTb6UM8rP0NjGt4crcXM3UJOGKZTTxCgkHZoNw2Nga%2BmLffUxWRfr4ZROzoGgVV1Wyn9GLuS8DTEPV31C3jpIR5MAv4NpbBU6bwHF2sr%2FO5abh5nYsoPqoypygOrqpA4SGjTqf0kQKcb5yU7GbguPPnkjtKNIEepmXi6VCF9026FUc4UP9%2Bh9nfHdmhNxygJHu9GIUTozGqWjhewRU2IdEzh%2FA6Uj0ekt3T%2FZab0Dqvs20TnJ14Ioi73yimjXCcyUjI66XZPGtiwIPzaOnw5LuhfZpT81TTBgjoP5qGeQm9XowYHG9J%2Fzbz6o8bKXoOgoiRLlkLW%2FdiGbSYiFBGF12QoQtyhzt%2BcLDNLILmABic%2B1%2F0CPOBXM0peNdunaiDloj%2FfjQ8IOHTN7gdZZf9amAP9Zhqs6D%2FMP9lWtk9UMkfM6SAI83Ln3iJo6YRVEJdsV68rebrwq2klSixa6DbcPQ6nztTW1OsLRNIQZWD27BnzfV2ag5m2y9xMHvXwGGLmCAsahd4NcFlI0HVWDC7jkbx2O4Lc0pSrtoL4wl6X3vAY6pgFhLqMLQi6tIYcrkDfydUhj5IYfYGkrJmqe%2BHZFNAbiN3ZyUuk9lIaRAkf9BUlWfK%2BE3%2BFnYkIKLjNEdUPF4SQDqK4UxEneQ8Iy1mr2PMJ6cT%2FTGOrnp8p7lVZ0iNU%2B3tvM26vm0S56ogzaS2jlmSlvytdNHX4kTDBr7%2BVdEUOVrXdPixTMUo6hEYjC8vANtB0rN4FXKBFcA94w%2BAskOgOFFtdAERzC&X-Amz-Signature=e8ada902ffb53cc1b359a9b4ce804dd2d1ce965dac5cdf798c67857e1baf8950&X-Amz-SignedHeaders=host&x-id=GetObject)
### Video Sequences
A **video** can be viewed as a sequence of multiple **images** or **frames**.
### Image Formats
Common image file formats include:
- **JPEG** (Joint Photographic Expert Group)
- **PNG** (Portable Network Graphics)
These formats compress and reduce file sizes while maintaining image quality.
### Image Processing Libraries in Python
#### Pillow (PIL)
Pillow is a widely used Python library for image manipulation.
- To load an image:
```python
from PIL import Image
img = Image.open('image.png')
```
- **Attributes** of a Pillow image:
	- `format`: The file format (e.g., PNG, JPEG).
	- `size`: The dimensions of the image (width x height).
	- `mode`: The color space (e.g., RGB, L for grayscale).
#### Example: Converting to Gray-Scale
- Convert an image to **gray-scale**:
```python
gray_img = img.convert('L')
gray_img.show()
```
#### Example: Quantization
- **Quantize** an image to reduce the number of intensity levels:
```python
quantized_img = img.quantize(colors=16)
quantized_img.show()
```
#### OpenCV
**OpenCV** is a powerful library for **computer vision** with more functionality than PIL.
- Import OpenCV:
```python
import cv2
```
- Load an image:
```python
img = cv2.imread('image.png')
```
- **Attributes** of an OpenCV image:
	- OpenCV represents images as **NumPy arrays**.
	- The **color channels** are ordered as **BGR** (blue, green, red) instead of **RGB**.
#### Example: Color Space Conversion
- Convert from **BGR to RGB**:
```python
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```
- Convert to **gray-scale**:
```python
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
#### Example: Saving an Image
- Save an image using OpenCV:
```python
cv2.imwrite('output.png', img)
```
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZOJCMAM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArxtY%2BZGNMQAd119ckdl7hBn9VzRN1cYVuqvwTy93Y2AiBaK6AMbPwaJKCeesqRYkwO9C7fGrdd5BF4b%2B67XWmbiSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF8sr8J4LlA55TXG1KtwDwyeuZ9lxPQ6%2F0gY4reaJ17afj1P93O9eK8le4ChhDTJddhZlX57%2BAK%2FgB51L5PJPYAheN6DhBc205RRDw21tWmBCTb6UM8rP0NjGt4crcXM3UJOGKZTTxCgkHZoNw2Nga%2BmLffUxWRfr4ZROzoGgVV1Wyn9GLuS8DTEPV31C3jpIR5MAv4NpbBU6bwHF2sr%2FO5abh5nYsoPqoypygOrqpA4SGjTqf0kQKcb5yU7GbguPPnkjtKNIEepmXi6VCF9026FUc4UP9%2Bh9nfHdmhNxygJHu9GIUTozGqWjhewRU2IdEzh%2FA6Uj0ekt3T%2FZab0Dqvs20TnJ14Ioi73yimjXCcyUjI66XZPGtiwIPzaOnw5LuhfZpT81TTBgjoP5qGeQm9XowYHG9J%2Fzbz6o8bKXoOgoiRLlkLW%2FdiGbSYiFBGF12QoQtyhzt%2BcLDNLILmABic%2B1%2F0CPOBXM0peNdunaiDloj%2FfjQ8IOHTN7gdZZf9amAP9Zhqs6D%2FMP9lWtk9UMkfM6SAI83Ln3iJo6YRVEJdsV68rebrwq2klSixa6DbcPQ6nztTW1OsLRNIQZWD27BnzfV2ag5m2y9xMHvXwGGLmCAsahd4NcFlI0HVWDC7jkbx2O4Lc0pSrtoL4wl6X3vAY6pgFhLqMLQi6tIYcrkDfydUhj5IYfYGkrJmqe%2BHZFNAbiN3ZyUuk9lIaRAkf9BUlWfK%2BE3%2BFnYkIKLjNEdUPF4SQDqK4UxEneQ8Iy1mr2PMJ6cT%2FTGOrnp8p7lVZ0iNU%2B3tvM26vm0S56ogzaS2jlmSlvytdNHX4kTDBr7%2BVdEUOVrXdPixTMUo6hEYjC8vANtB0rN4FXKBFcA94w%2BAskOgOFFtdAERzC&X-Amz-Signature=aa6d6b2ae372cd62b566491f38c0ff8fcc27286b0cc1d941af563c18e803659e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Working with Color Channels
Using **slices**, individual color channels (e.g., **blue**, **green**, **red**) can be extracted:
```python
blue_channel = img[:, :, 0]
green_channel = img[:, :, 1]
red_channel = img[:, :, 2]
```
Each channel can then be processed or analyzed separately.
#### Conversion between PIL and NumPy Arrays
PIL images can be easily converted to **NumPy arrays** for further processing:
```python
import numpy as np
np_img = np.array(img)
```
This conversion is particularly useful when integrating with **OpenCV** and performing advanced operations.
### Conclusion
Both **PIL** and **OpenCV** are essential tools for handling and processing digital images in Python. Each has its strengths:
- **PIL** is simple and great for basic tasks.
- **OpenCV** offers more advanced capabilities for **computer vision** applications.
___


