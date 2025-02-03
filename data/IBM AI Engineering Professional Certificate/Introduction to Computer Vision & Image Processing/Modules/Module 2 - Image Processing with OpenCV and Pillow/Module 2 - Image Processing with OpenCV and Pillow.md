

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6FP6ZMP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFe%2Bpc6g9OOlOt0nFQBGJSqCjMoZIGLAq6xM5usRLLkpAiEAkWFkygj8h5DGGK9vrGvfFgIeJPN9lUvFjR6UmbxjoI4qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDnCkGCHvG2tCiW6wyrcA7hsMEplFJs%2B0HwXTVTqCtez1xfdSXYC2Isql6gfC2luV%2F9BX1y%2BH5X9RwkncoeNseMCw3jpavFzbublfBpfNTFyoaM%2BT7CjaCcw8pnPcjyMa59GUaS7J645bLfahJOtEh2%2FbciRRuFpgevlePWVcBRQkcMv8WDUBLzZ4PLcsTKVnFpFAuIF%2B59RrLreR5nZmkBA8E1TwNlz3uGXktoavDZ4LI8N1eIWWQcqvR8BA5ZOKgLpyjpOBHUxVwL4Yf%2FUrN07ln5EbAWTpn45gS2B6jRMdwpqVXhCNcS%2F5aCC%2FEBanBNf38WfDqqwxT4rpbnGuJfTVuXKSEYfMWJF3pOpO%2Fzmu0gG9vSSQuo8JsUT8g55eug6061q1HYVYtJcyvGMr9gpb3j6iH9r522TI98bUGwZognNOPBrYwNldVm7uWBCSRwaxWAWACbtadU62274JJFb2Pk0HSl83HIXx7nk6AIXCP7s%2ByTSAXqWH78iDMkO5RYLIcR5g8hKJNaxLqnPqCAcfQkrdTVlR2DAli0SPajdeugVFtJA%2F54N2%2FHZ0D0jBn7RyeK6iajZywZM662V%2BPBvQQ6qc4YCRvq%2B7Pn3esozihhYtrrw8vog7TaluPUajPMtSpFzDRvBuBMRMJLl%2F7wGOqUBB03k0fc4Q%2FoGqJfhILT%2FfQm2KQ4RFrG6k%2FwSDfoX0dwCRpBTXNNPwN19JsA7DQQX8J1QC%2FePzdCnAGegffaVGOUsal5NDmsb1%2BCct1gIEUvUA2wUq6LEzdV%2BypGhm8UmBNF03yyeu6ye%2FVa%2BxnoNe6SUL3gGv6uWnqAHBR9mFrXMSum0SiYQVQHii194jfDIdOPoM2Mieu3TWtvZdlb56FU5z9s2&X-Amz-Signature=4035dbb75143b098b79947e922ac35c3a631a37e471ae312102bed3dcc05e445&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWYAOT64%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FIFhnpi1e0%2B1%2FniNd%2FCSTGInQA7gbR7pl3rrc4rQKFAiA0BQdKxc3%2FHmaISv4U0u3pqLa4m9KYXU8PBh%2B%2Fd5w0kiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqYKMHiZX7w3R8wa2KtwDBjYlEFEBSsXhh9C9AINpNZNMZPoQ5EA3orohHrWbZraGy2V4lP8O8F18SDnCdpvhWtDnovNuJdX2lQ%2FW8VyFXFrIDHth%2BxPO26CD3u2nmIe%2BmKIxcz8alFCylaGgsY%2FhEkP9hRNxZCT5etVsQRyeS1UxQo9eBOai4fMZj14xj8KYt4Gzs%2BFh7gtuvLtfGURbBF43A58J8QldRnFinnvDMH6SxSLFCAuR8a%2Bqh86dMPJveX5CLVlzTxc6r3NvWgtnDqj6%2FFDG58g5XEYEtMIdgniXOBxkNLKFQbn9qIvY7zTXHGI%2Fk2Zsqjeyd2jmEzxmfDq8RQMAxYYbnoCaMLT23yX3%2B67n3IgCfwm8TFSjZMiASOSP4f8E91R1xKlMC3R7tiChFiLWqXumS8xWN%2FtSbimKP%2F26ouMwyChVhDAEvM1hsYUoWjzsuxxXoedQFRwk56TY0wHe%2FvkGHP%2Fk5B99q79nmsrkZgR8oM8LpmYN0Y8eQ5iNOPYOQWyDBORK8GyKwOGmshuivD622uljeZu7JF0Wt5MoD65rHrXRdjMr%2BsGFAqSQ4eJZnOcH8NAlK4yDpW6krkL7y6Troh60tScjUDTEreNXoz8ZMpkzMd24PNNOJZdQp2HDGt3jl8wwh%2BX%2FvAY6pgGpFEGRjRYMHGscvVn6CRnr%2Fd5Ny40s%2B7lJWDlK83N5GpTsitigE3wBtCOZMAT%2BEpSElyUQ6ztqDaJhdZvXJ%2BYBRbUi0ohaucKVQGZ6Huh05dlbE2LuJa51pbsmYr5xvN%2F%2BOfjcxVX9Kbxmmjta2dudbjMPF48rVYyoQOzx%2Fdt2JFOYdudITOb4BmmUBfQ3jqOwi6QW3F8zsXB19vXP3FErBCKJvYrp&X-Amz-Signature=333f740e30b3dc6508312ae7c2f9a1e0ad64dadef1c23f9a6b7e5fab9e5efb0d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWYAOT64%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FIFhnpi1e0%2B1%2FniNd%2FCSTGInQA7gbR7pl3rrc4rQKFAiA0BQdKxc3%2FHmaISv4U0u3pqLa4m9KYXU8PBh%2B%2Fd5w0kiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqYKMHiZX7w3R8wa2KtwDBjYlEFEBSsXhh9C9AINpNZNMZPoQ5EA3orohHrWbZraGy2V4lP8O8F18SDnCdpvhWtDnovNuJdX2lQ%2FW8VyFXFrIDHth%2BxPO26CD3u2nmIe%2BmKIxcz8alFCylaGgsY%2FhEkP9hRNxZCT5etVsQRyeS1UxQo9eBOai4fMZj14xj8KYt4Gzs%2BFh7gtuvLtfGURbBF43A58J8QldRnFinnvDMH6SxSLFCAuR8a%2Bqh86dMPJveX5CLVlzTxc6r3NvWgtnDqj6%2FFDG58g5XEYEtMIdgniXOBxkNLKFQbn9qIvY7zTXHGI%2Fk2Zsqjeyd2jmEzxmfDq8RQMAxYYbnoCaMLT23yX3%2B67n3IgCfwm8TFSjZMiASOSP4f8E91R1xKlMC3R7tiChFiLWqXumS8xWN%2FtSbimKP%2F26ouMwyChVhDAEvM1hsYUoWjzsuxxXoedQFRwk56TY0wHe%2FvkGHP%2Fk5B99q79nmsrkZgR8oM8LpmYN0Y8eQ5iNOPYOQWyDBORK8GyKwOGmshuivD622uljeZu7JF0Wt5MoD65rHrXRdjMr%2BsGFAqSQ4eJZnOcH8NAlK4yDpW6krkL7y6Troh60tScjUDTEreNXoz8ZMpkzMd24PNNOJZdQp2HDGt3jl8wwh%2BX%2FvAY6pgGpFEGRjRYMHGscvVn6CRnr%2Fd5Ny40s%2B7lJWDlK83N5GpTsitigE3wBtCOZMAT%2BEpSElyUQ6ztqDaJhdZvXJ%2BYBRbUi0ohaucKVQGZ6Huh05dlbE2LuJa51pbsmYr5xvN%2F%2BOfjcxVX9Kbxmmjta2dudbjMPF48rVYyoQOzx%2Fdt2JFOYdudITOb4BmmUBfQ3jqOwi6QW3F8zsXB19vXP3FErBCKJvYrp&X-Amz-Signature=7f63f4db962509cbe271e509c6373336925235fa3856f2a2b64396ba47d51589&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWYAOT64%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FIFhnpi1e0%2B1%2FniNd%2FCSTGInQA7gbR7pl3rrc4rQKFAiA0BQdKxc3%2FHmaISv4U0u3pqLa4m9KYXU8PBh%2B%2Fd5w0kiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqYKMHiZX7w3R8wa2KtwDBjYlEFEBSsXhh9C9AINpNZNMZPoQ5EA3orohHrWbZraGy2V4lP8O8F18SDnCdpvhWtDnovNuJdX2lQ%2FW8VyFXFrIDHth%2BxPO26CD3u2nmIe%2BmKIxcz8alFCylaGgsY%2FhEkP9hRNxZCT5etVsQRyeS1UxQo9eBOai4fMZj14xj8KYt4Gzs%2BFh7gtuvLtfGURbBF43A58J8QldRnFinnvDMH6SxSLFCAuR8a%2Bqh86dMPJveX5CLVlzTxc6r3NvWgtnDqj6%2FFDG58g5XEYEtMIdgniXOBxkNLKFQbn9qIvY7zTXHGI%2Fk2Zsqjeyd2jmEzxmfDq8RQMAxYYbnoCaMLT23yX3%2B67n3IgCfwm8TFSjZMiASOSP4f8E91R1xKlMC3R7tiChFiLWqXumS8xWN%2FtSbimKP%2F26ouMwyChVhDAEvM1hsYUoWjzsuxxXoedQFRwk56TY0wHe%2FvkGHP%2Fk5B99q79nmsrkZgR8oM8LpmYN0Y8eQ5iNOPYOQWyDBORK8GyKwOGmshuivD622uljeZu7JF0Wt5MoD65rHrXRdjMr%2BsGFAqSQ4eJZnOcH8NAlK4yDpW6krkL7y6Troh60tScjUDTEreNXoz8ZMpkzMd24PNNOJZdQp2HDGt3jl8wwh%2BX%2FvAY6pgGpFEGRjRYMHGscvVn6CRnr%2Fd5Ny40s%2B7lJWDlK83N5GpTsitigE3wBtCOZMAT%2BEpSElyUQ6ztqDaJhdZvXJ%2BYBRbUi0ohaucKVQGZ6Huh05dlbE2LuJa51pbsmYr5xvN%2F%2BOfjcxVX9Kbxmmjta2dudbjMPF48rVYyoQOzx%2Fdt2JFOYdudITOb4BmmUBfQ3jqOwi6QW3F8zsXB19vXP3FErBCKJvYrp&X-Amz-Signature=5791f608a5518833b8988bff3d50d3bd30d0e574c3b79dbf7e8f0b8ea3579ce6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWYAOT64%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FIFhnpi1e0%2B1%2FniNd%2FCSTGInQA7gbR7pl3rrc4rQKFAiA0BQdKxc3%2FHmaISv4U0u3pqLa4m9KYXU8PBh%2B%2Fd5w0kiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqYKMHiZX7w3R8wa2KtwDBjYlEFEBSsXhh9C9AINpNZNMZPoQ5EA3orohHrWbZraGy2V4lP8O8F18SDnCdpvhWtDnovNuJdX2lQ%2FW8VyFXFrIDHth%2BxPO26CD3u2nmIe%2BmKIxcz8alFCylaGgsY%2FhEkP9hRNxZCT5etVsQRyeS1UxQo9eBOai4fMZj14xj8KYt4Gzs%2BFh7gtuvLtfGURbBF43A58J8QldRnFinnvDMH6SxSLFCAuR8a%2Bqh86dMPJveX5CLVlzTxc6r3NvWgtnDqj6%2FFDG58g5XEYEtMIdgniXOBxkNLKFQbn9qIvY7zTXHGI%2Fk2Zsqjeyd2jmEzxmfDq8RQMAxYYbnoCaMLT23yX3%2B67n3IgCfwm8TFSjZMiASOSP4f8E91R1xKlMC3R7tiChFiLWqXumS8xWN%2FtSbimKP%2F26ouMwyChVhDAEvM1hsYUoWjzsuxxXoedQFRwk56TY0wHe%2FvkGHP%2Fk5B99q79nmsrkZgR8oM8LpmYN0Y8eQ5iNOPYOQWyDBORK8GyKwOGmshuivD622uljeZu7JF0Wt5MoD65rHrXRdjMr%2BsGFAqSQ4eJZnOcH8NAlK4yDpW6krkL7y6Troh60tScjUDTEreNXoz8ZMpkzMd24PNNOJZdQp2HDGt3jl8wwh%2BX%2FvAY6pgGpFEGRjRYMHGscvVn6CRnr%2Fd5Ny40s%2B7lJWDlK83N5GpTsitigE3wBtCOZMAT%2BEpSElyUQ6ztqDaJhdZvXJ%2BYBRbUi0ohaucKVQGZ6Huh05dlbE2LuJa51pbsmYr5xvN%2F%2BOfjcxVX9Kbxmmjta2dudbjMPF48rVYyoQOzx%2Fdt2JFOYdudITOb4BmmUBfQ3jqOwi6QW3F8zsXB19vXP3FErBCKJvYrp&X-Amz-Signature=4a4087c06f56100b49b252b18f4af28b3eac362f8659fe88af6a947645c36f9d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWYAOT64%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FIFhnpi1e0%2B1%2FniNd%2FCSTGInQA7gbR7pl3rrc4rQKFAiA0BQdKxc3%2FHmaISv4U0u3pqLa4m9KYXU8PBh%2B%2Fd5w0kiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqYKMHiZX7w3R8wa2KtwDBjYlEFEBSsXhh9C9AINpNZNMZPoQ5EA3orohHrWbZraGy2V4lP8O8F18SDnCdpvhWtDnovNuJdX2lQ%2FW8VyFXFrIDHth%2BxPO26CD3u2nmIe%2BmKIxcz8alFCylaGgsY%2FhEkP9hRNxZCT5etVsQRyeS1UxQo9eBOai4fMZj14xj8KYt4Gzs%2BFh7gtuvLtfGURbBF43A58J8QldRnFinnvDMH6SxSLFCAuR8a%2Bqh86dMPJveX5CLVlzTxc6r3NvWgtnDqj6%2FFDG58g5XEYEtMIdgniXOBxkNLKFQbn9qIvY7zTXHGI%2Fk2Zsqjeyd2jmEzxmfDq8RQMAxYYbnoCaMLT23yX3%2B67n3IgCfwm8TFSjZMiASOSP4f8E91R1xKlMC3R7tiChFiLWqXumS8xWN%2FtSbimKP%2F26ouMwyChVhDAEvM1hsYUoWjzsuxxXoedQFRwk56TY0wHe%2FvkGHP%2Fk5B99q79nmsrkZgR8oM8LpmYN0Y8eQ5iNOPYOQWyDBORK8GyKwOGmshuivD622uljeZu7JF0Wt5MoD65rHrXRdjMr%2BsGFAqSQ4eJZnOcH8NAlK4yDpW6krkL7y6Troh60tScjUDTEreNXoz8ZMpkzMd24PNNOJZdQp2HDGt3jl8wwh%2BX%2FvAY6pgGpFEGRjRYMHGscvVn6CRnr%2Fd5Ny40s%2B7lJWDlK83N5GpTsitigE3wBtCOZMAT%2BEpSElyUQ6ztqDaJhdZvXJ%2BYBRbUi0ohaucKVQGZ6Huh05dlbE2LuJa51pbsmYr5xvN%2F%2BOfjcxVX9Kbxmmjta2dudbjMPF48rVYyoQOzx%2Fdt2JFOYdudITOb4BmmUBfQ3jqOwi6QW3F8zsXB19vXP3FErBCKJvYrp&X-Amz-Signature=c3e7bcb10aa2778a2e4f88b77495f6eb16166f45bc44b5278889e49fe29a619e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6FP6ZMP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFe%2Bpc6g9OOlOt0nFQBGJSqCjMoZIGLAq6xM5usRLLkpAiEAkWFkygj8h5DGGK9vrGvfFgIeJPN9lUvFjR6UmbxjoI4qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDnCkGCHvG2tCiW6wyrcA7hsMEplFJs%2B0HwXTVTqCtez1xfdSXYC2Isql6gfC2luV%2F9BX1y%2BH5X9RwkncoeNseMCw3jpavFzbublfBpfNTFyoaM%2BT7CjaCcw8pnPcjyMa59GUaS7J645bLfahJOtEh2%2FbciRRuFpgevlePWVcBRQkcMv8WDUBLzZ4PLcsTKVnFpFAuIF%2B59RrLreR5nZmkBA8E1TwNlz3uGXktoavDZ4LI8N1eIWWQcqvR8BA5ZOKgLpyjpOBHUxVwL4Yf%2FUrN07ln5EbAWTpn45gS2B6jRMdwpqVXhCNcS%2F5aCC%2FEBanBNf38WfDqqwxT4rpbnGuJfTVuXKSEYfMWJF3pOpO%2Fzmu0gG9vSSQuo8JsUT8g55eug6061q1HYVYtJcyvGMr9gpb3j6iH9r522TI98bUGwZognNOPBrYwNldVm7uWBCSRwaxWAWACbtadU62274JJFb2Pk0HSl83HIXx7nk6AIXCP7s%2ByTSAXqWH78iDMkO5RYLIcR5g8hKJNaxLqnPqCAcfQkrdTVlR2DAli0SPajdeugVFtJA%2F54N2%2FHZ0D0jBn7RyeK6iajZywZM662V%2BPBvQQ6qc4YCRvq%2B7Pn3esozihhYtrrw8vog7TaluPUajPMtSpFzDRvBuBMRMJLl%2F7wGOqUBB03k0fc4Q%2FoGqJfhILT%2FfQm2KQ4RFrG6k%2FwSDfoX0dwCRpBTXNNPwN19JsA7DQQX8J1QC%2FePzdCnAGegffaVGOUsal5NDmsb1%2BCct1gIEUvUA2wUq6LEzdV%2BypGhm8UmBNF03yyeu6ye%2FVa%2BxnoNe6SUL3gGv6uWnqAHBR9mFrXMSum0SiYQVQHii194jfDIdOPoM2Mieu3TWtvZdlb56FU5z9s2&X-Amz-Signature=47288ee6994048fa18118368b998bc7116fe5b0b3fdc84f06a7007cd0b57f297&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6FP6ZMP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFe%2Bpc6g9OOlOt0nFQBGJSqCjMoZIGLAq6xM5usRLLkpAiEAkWFkygj8h5DGGK9vrGvfFgIeJPN9lUvFjR6UmbxjoI4qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDnCkGCHvG2tCiW6wyrcA7hsMEplFJs%2B0HwXTVTqCtez1xfdSXYC2Isql6gfC2luV%2F9BX1y%2BH5X9RwkncoeNseMCw3jpavFzbublfBpfNTFyoaM%2BT7CjaCcw8pnPcjyMa59GUaS7J645bLfahJOtEh2%2FbciRRuFpgevlePWVcBRQkcMv8WDUBLzZ4PLcsTKVnFpFAuIF%2B59RrLreR5nZmkBA8E1TwNlz3uGXktoavDZ4LI8N1eIWWQcqvR8BA5ZOKgLpyjpOBHUxVwL4Yf%2FUrN07ln5EbAWTpn45gS2B6jRMdwpqVXhCNcS%2F5aCC%2FEBanBNf38WfDqqwxT4rpbnGuJfTVuXKSEYfMWJF3pOpO%2Fzmu0gG9vSSQuo8JsUT8g55eug6061q1HYVYtJcyvGMr9gpb3j6iH9r522TI98bUGwZognNOPBrYwNldVm7uWBCSRwaxWAWACbtadU62274JJFb2Pk0HSl83HIXx7nk6AIXCP7s%2ByTSAXqWH78iDMkO5RYLIcR5g8hKJNaxLqnPqCAcfQkrdTVlR2DAli0SPajdeugVFtJA%2F54N2%2FHZ0D0jBn7RyeK6iajZywZM662V%2BPBvQQ6qc4YCRvq%2B7Pn3esozihhYtrrw8vog7TaluPUajPMtSpFzDRvBuBMRMJLl%2F7wGOqUBB03k0fc4Q%2FoGqJfhILT%2FfQm2KQ4RFrG6k%2FwSDfoX0dwCRpBTXNNPwN19JsA7DQQX8J1QC%2FePzdCnAGegffaVGOUsal5NDmsb1%2BCct1gIEUvUA2wUq6LEzdV%2BypGhm8UmBNF03yyeu6ye%2FVa%2BxnoNe6SUL3gGv6uWnqAHBR9mFrXMSum0SiYQVQHii194jfDIdOPoM2Mieu3TWtvZdlb56FU5z9s2&X-Amz-Signature=a39080be513804a49cb5771a488cde4e5914f6c79ea7c14d8f9a7f9edc319f84&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6FP6ZMP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFe%2Bpc6g9OOlOt0nFQBGJSqCjMoZIGLAq6xM5usRLLkpAiEAkWFkygj8h5DGGK9vrGvfFgIeJPN9lUvFjR6UmbxjoI4qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDnCkGCHvG2tCiW6wyrcA7hsMEplFJs%2B0HwXTVTqCtez1xfdSXYC2Isql6gfC2luV%2F9BX1y%2BH5X9RwkncoeNseMCw3jpavFzbublfBpfNTFyoaM%2BT7CjaCcw8pnPcjyMa59GUaS7J645bLfahJOtEh2%2FbciRRuFpgevlePWVcBRQkcMv8WDUBLzZ4PLcsTKVnFpFAuIF%2B59RrLreR5nZmkBA8E1TwNlz3uGXktoavDZ4LI8N1eIWWQcqvR8BA5ZOKgLpyjpOBHUxVwL4Yf%2FUrN07ln5EbAWTpn45gS2B6jRMdwpqVXhCNcS%2F5aCC%2FEBanBNf38WfDqqwxT4rpbnGuJfTVuXKSEYfMWJF3pOpO%2Fzmu0gG9vSSQuo8JsUT8g55eug6061q1HYVYtJcyvGMr9gpb3j6iH9r522TI98bUGwZognNOPBrYwNldVm7uWBCSRwaxWAWACbtadU62274JJFb2Pk0HSl83HIXx7nk6AIXCP7s%2ByTSAXqWH78iDMkO5RYLIcR5g8hKJNaxLqnPqCAcfQkrdTVlR2DAli0SPajdeugVFtJA%2F54N2%2FHZ0D0jBn7RyeK6iajZywZM662V%2BPBvQQ6qc4YCRvq%2B7Pn3esozihhYtrrw8vog7TaluPUajPMtSpFzDRvBuBMRMJLl%2F7wGOqUBB03k0fc4Q%2FoGqJfhILT%2FfQm2KQ4RFrG6k%2FwSDfoX0dwCRpBTXNNPwN19JsA7DQQX8J1QC%2FePzdCnAGegffaVGOUsal5NDmsb1%2BCct1gIEUvUA2wUq6LEzdV%2BypGhm8UmBNF03yyeu6ye%2FVa%2BxnoNe6SUL3gGv6uWnqAHBR9mFrXMSum0SiYQVQHii194jfDIdOPoM2Mieu3TWtvZdlb56FU5z9s2&X-Amz-Signature=77c0f049e76efb709d6bc2f42fb5be04dddfcff2f19cd5da8ae8d500ba4c20ea&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6FP6ZMP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFe%2Bpc6g9OOlOt0nFQBGJSqCjMoZIGLAq6xM5usRLLkpAiEAkWFkygj8h5DGGK9vrGvfFgIeJPN9lUvFjR6UmbxjoI4qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDnCkGCHvG2tCiW6wyrcA7hsMEplFJs%2B0HwXTVTqCtez1xfdSXYC2Isql6gfC2luV%2F9BX1y%2BH5X9RwkncoeNseMCw3jpavFzbublfBpfNTFyoaM%2BT7CjaCcw8pnPcjyMa59GUaS7J645bLfahJOtEh2%2FbciRRuFpgevlePWVcBRQkcMv8WDUBLzZ4PLcsTKVnFpFAuIF%2B59RrLreR5nZmkBA8E1TwNlz3uGXktoavDZ4LI8N1eIWWQcqvR8BA5ZOKgLpyjpOBHUxVwL4Yf%2FUrN07ln5EbAWTpn45gS2B6jRMdwpqVXhCNcS%2F5aCC%2FEBanBNf38WfDqqwxT4rpbnGuJfTVuXKSEYfMWJF3pOpO%2Fzmu0gG9vSSQuo8JsUT8g55eug6061q1HYVYtJcyvGMr9gpb3j6iH9r522TI98bUGwZognNOPBrYwNldVm7uWBCSRwaxWAWACbtadU62274JJFb2Pk0HSl83HIXx7nk6AIXCP7s%2ByTSAXqWH78iDMkO5RYLIcR5g8hKJNaxLqnPqCAcfQkrdTVlR2DAli0SPajdeugVFtJA%2F54N2%2FHZ0D0jBn7RyeK6iajZywZM662V%2BPBvQQ6qc4YCRvq%2B7Pn3esozihhYtrrw8vog7TaluPUajPMtSpFzDRvBuBMRMJLl%2F7wGOqUBB03k0fc4Q%2FoGqJfhILT%2FfQm2KQ4RFrG6k%2FwSDfoX0dwCRpBTXNNPwN19JsA7DQQX8J1QC%2FePzdCnAGegffaVGOUsal5NDmsb1%2BCct1gIEUvUA2wUq6LEzdV%2BypGhm8UmBNF03yyeu6ye%2FVa%2BxnoNe6SUL3gGv6uWnqAHBR9mFrXMSum0SiYQVQHii194jfDIdOPoM2Mieu3TWtvZdlb56FU5z9s2&X-Amz-Signature=8d9bc8f542460b67e8b16a1d3b7157c104648483c912bbcb36e6d2df549905ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6FP6ZMP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFe%2Bpc6g9OOlOt0nFQBGJSqCjMoZIGLAq6xM5usRLLkpAiEAkWFkygj8h5DGGK9vrGvfFgIeJPN9lUvFjR6UmbxjoI4qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDnCkGCHvG2tCiW6wyrcA7hsMEplFJs%2B0HwXTVTqCtez1xfdSXYC2Isql6gfC2luV%2F9BX1y%2BH5X9RwkncoeNseMCw3jpavFzbublfBpfNTFyoaM%2BT7CjaCcw8pnPcjyMa59GUaS7J645bLfahJOtEh2%2FbciRRuFpgevlePWVcBRQkcMv8WDUBLzZ4PLcsTKVnFpFAuIF%2B59RrLreR5nZmkBA8E1TwNlz3uGXktoavDZ4LI8N1eIWWQcqvR8BA5ZOKgLpyjpOBHUxVwL4Yf%2FUrN07ln5EbAWTpn45gS2B6jRMdwpqVXhCNcS%2F5aCC%2FEBanBNf38WfDqqwxT4rpbnGuJfTVuXKSEYfMWJF3pOpO%2Fzmu0gG9vSSQuo8JsUT8g55eug6061q1HYVYtJcyvGMr9gpb3j6iH9r522TI98bUGwZognNOPBrYwNldVm7uWBCSRwaxWAWACbtadU62274JJFb2Pk0HSl83HIXx7nk6AIXCP7s%2ByTSAXqWH78iDMkO5RYLIcR5g8hKJNaxLqnPqCAcfQkrdTVlR2DAli0SPajdeugVFtJA%2F54N2%2FHZ0D0jBn7RyeK6iajZywZM662V%2BPBvQQ6qc4YCRvq%2B7Pn3esozihhYtrrw8vog7TaluPUajPMtSpFzDRvBuBMRMJLl%2F7wGOqUBB03k0fc4Q%2FoGqJfhILT%2FfQm2KQ4RFrG6k%2FwSDfoX0dwCRpBTXNNPwN19JsA7DQQX8J1QC%2FePzdCnAGegffaVGOUsal5NDmsb1%2BCct1gIEUvUA2wUq6LEzdV%2BypGhm8UmBNF03yyeu6ye%2FVa%2BxnoNe6SUL3gGv6uWnqAHBR9mFrXMSum0SiYQVQHii194jfDIdOPoM2Mieu3TWtvZdlb56FU5z9s2&X-Amz-Signature=d0ae5732b05925a91d09d0686a4980c18a8ec58c321d2e49217dbba870f7fd82&X-Amz-SignedHeaders=host&x-id=GetObject)
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


