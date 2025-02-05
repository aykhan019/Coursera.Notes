

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIDXXG5Z%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIHqk%2BTUsP6Z6yIcJoAEpfnwI%2BFA5xJrhbSWHG61Pxw1yAiEAj9ihoKM9r3583ThSi9l0qM5Pm3PnNL12HXcENe7phAoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDEu0HFDHAr%2FRURDgzircAzCdGxXT94tQf6Nj%2F%2Fc4vXeB42Q3ScceXtehBLWS0KtRSHCJ1IYJP9tQ7StSo5dN7vsTE2Eg9jNzxsez3adakr5m4pD05A0%2FcUa0mQwimRrvtfS07OETOn%2FJ0HP%2FzPhOWmqML5lfk0kPOuYJTJkqDuMPPx9es4R8FHEmNBgPR4540h20S5QEzYihOENXXoUoogo1vGDjTqoT7usZPpgY0OLeNHj5pW88Cp4gMbdQU83EM54yNLaIFlHwOoEzmJtn%2FUupjS0UYzQFEEWVCxnhKviDkx%2BhdQiYF4C7Jn1aruRv8mK8x0hrJvA%2BDseoNE6Uun8qLc0PGfR3yAocOI2xh%2BW0GUbUl8WeZkno64vYlJYoj1Groyx0e2HvBPmt6d0g0U9Ok16GfwnKkmA5vc8P%2FaLEQ9zHF9eBc9Ym0zpcTPLcJDVtqtWqxzXK7TsZEFTEhk2ucBCbXq4RgYlaGDKmssim9pG7cL%2BkiZnKcn59iebjWTirmaR145ehzIALIOnJR8moyrttBcUoGaOBkZN9LjOc6D2wdYSdbhHAEgAytObz0rywo6TseIDPDOwZJsNzMkARc%2BV05bWLqbQoe4v3vOhHV5mN%2Ba3CpLT0jk5OHmW1Ew3EMYOTfDtJNJhRMP3Mir0GOqUBreJrX%2BW6afgTHx4B2Ch2BbxNXvlIC3DLbU5w73iEWFT6s8BFKjESGG1zR92km%2B2MQnDdUmgLGCijpf3iEzD3d0%2FpXo6eBsqrxxoyo9BPi0iQ4xisWk6JYN4mjzsHpQRkhsoSzcVC%2F1wO4Bxl4B0ynf1VqxObrB4MCh7Lw%2Fhjgiuf6jQVPvYawwYho6KmTkvckkEEG2%2B2CUJWSPGDdQe%2FfnRoJDqE&X-Amz-Signature=d5035c1c9faebfe83dae02d32200ca80fc2e869df536122dcc0bd35500a99195&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5YALQQX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIFnTHgSLowDW8WizMz0fQ4YdmsW0K4C9hLwoPvQrP6KXAiBRjZSGT%2Fl8MXz8VDLQtuGS7ud2BcrwegqZy9rvDJwULir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMxZxzmRjXfVe4zYuOKtwDnHx0WLyeHAnl1pBgSRG01lxct%2Foi8XzP0uhFSv%2ByY%2B3elqeCz602hP1WhuhSSMgSNb3k1VTXVYeNE8cjrBOVDpw1mmRHxqCTOknjpVgo3iZNkkUvdUB0OwjSmGd9EtIvAxg8zt7bRf%2FJIFUH4vR5Rh4QBzQO%2FTwUwMieAEn0ndgG%2FR8hsjEQTKDV%2FVWzn1LpPx1KEe0KRHIj5PYR9KoYrneTq5r%2FHydgb4xDqqHhqByVf8seZ%2B9YMqITya4%2B90J57qrk6ds9oR0cYZk4%2BuU3GqDEiCQmMM7VLF4Xy6Q2E3bHoC1onO6GEATdbLEUGwjsW0yw%2FyMK3auR%2BIWbMkJ1BmGKB18Zpjrpm3S0QhkN%2BXH38%2Bl9s3A6ibqZ2ielG8bPYvnEnx42IZTc1T3CkY%2B8a4%2BmISw3exof5ZKPQnIvEDAPJL55jxSSUYfL7jZwRnqlj9XAW2ow%2BQB2d4YCa96W1AYQzOe8A3IrHUNFYIuMBtjlP%2FfRLMBoJJrK%2B3oRAJZ7bIrR1vNW7Y7Z6%2BvvGcUpJKdsMpJeZREgWRZMQsTFpXKVRxUpWuEuK2MzJEc%2FdFDx2d0AaBB0zOATZqmSGwoQnwUqAUIaZJF7NPgs%2Fb6W3cH3wny%2FtJVCi4JuMuYw8syKvQY6pgHnLzDVNB851dBJfKNN9l5c34%2Fu4KGRNbWZ7DcEeb18m5PDSQnLdgd9al17ft2tptCR7p3WHDMSjOjAicB11p4a9oGsv6M1suPJ4CXjOZ8srwqdwA7QvYHH93Ga%2FG4qmprA4onc6JGI4AQ8S6q7bvmU5DxTjy1IMRXKPu4cwqqm25g01gRmaAq9FFZdiE5Ni%2BzrIuz5aGG8W2fTM76yHxofNMD%2BY9OB&X-Amz-Signature=8baf83cc99a508c2beca86f8c0e859b5e5f5d62877a2b4fc6b79f9e8fb3a9543&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5YALQQX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIFnTHgSLowDW8WizMz0fQ4YdmsW0K4C9hLwoPvQrP6KXAiBRjZSGT%2Fl8MXz8VDLQtuGS7ud2BcrwegqZy9rvDJwULir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMxZxzmRjXfVe4zYuOKtwDnHx0WLyeHAnl1pBgSRG01lxct%2Foi8XzP0uhFSv%2ByY%2B3elqeCz602hP1WhuhSSMgSNb3k1VTXVYeNE8cjrBOVDpw1mmRHxqCTOknjpVgo3iZNkkUvdUB0OwjSmGd9EtIvAxg8zt7bRf%2FJIFUH4vR5Rh4QBzQO%2FTwUwMieAEn0ndgG%2FR8hsjEQTKDV%2FVWzn1LpPx1KEe0KRHIj5PYR9KoYrneTq5r%2FHydgb4xDqqHhqByVf8seZ%2B9YMqITya4%2B90J57qrk6ds9oR0cYZk4%2BuU3GqDEiCQmMM7VLF4Xy6Q2E3bHoC1onO6GEATdbLEUGwjsW0yw%2FyMK3auR%2BIWbMkJ1BmGKB18Zpjrpm3S0QhkN%2BXH38%2Bl9s3A6ibqZ2ielG8bPYvnEnx42IZTc1T3CkY%2B8a4%2BmISw3exof5ZKPQnIvEDAPJL55jxSSUYfL7jZwRnqlj9XAW2ow%2BQB2d4YCa96W1AYQzOe8A3IrHUNFYIuMBtjlP%2FfRLMBoJJrK%2B3oRAJZ7bIrR1vNW7Y7Z6%2BvvGcUpJKdsMpJeZREgWRZMQsTFpXKVRxUpWuEuK2MzJEc%2FdFDx2d0AaBB0zOATZqmSGwoQnwUqAUIaZJF7NPgs%2Fb6W3cH3wny%2FtJVCi4JuMuYw8syKvQY6pgHnLzDVNB851dBJfKNN9l5c34%2Fu4KGRNbWZ7DcEeb18m5PDSQnLdgd9al17ft2tptCR7p3WHDMSjOjAicB11p4a9oGsv6M1suPJ4CXjOZ8srwqdwA7QvYHH93Ga%2FG4qmprA4onc6JGI4AQ8S6q7bvmU5DxTjy1IMRXKPu4cwqqm25g01gRmaAq9FFZdiE5Ni%2BzrIuz5aGG8W2fTM76yHxofNMD%2BY9OB&X-Amz-Signature=3c0a173ecce7679e9de2faf06618fe87a62de13fb1d8466262a838a90245fee6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5YALQQX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIFnTHgSLowDW8WizMz0fQ4YdmsW0K4C9hLwoPvQrP6KXAiBRjZSGT%2Fl8MXz8VDLQtuGS7ud2BcrwegqZy9rvDJwULir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMxZxzmRjXfVe4zYuOKtwDnHx0WLyeHAnl1pBgSRG01lxct%2Foi8XzP0uhFSv%2ByY%2B3elqeCz602hP1WhuhSSMgSNb3k1VTXVYeNE8cjrBOVDpw1mmRHxqCTOknjpVgo3iZNkkUvdUB0OwjSmGd9EtIvAxg8zt7bRf%2FJIFUH4vR5Rh4QBzQO%2FTwUwMieAEn0ndgG%2FR8hsjEQTKDV%2FVWzn1LpPx1KEe0KRHIj5PYR9KoYrneTq5r%2FHydgb4xDqqHhqByVf8seZ%2B9YMqITya4%2B90J57qrk6ds9oR0cYZk4%2BuU3GqDEiCQmMM7VLF4Xy6Q2E3bHoC1onO6GEATdbLEUGwjsW0yw%2FyMK3auR%2BIWbMkJ1BmGKB18Zpjrpm3S0QhkN%2BXH38%2Bl9s3A6ibqZ2ielG8bPYvnEnx42IZTc1T3CkY%2B8a4%2BmISw3exof5ZKPQnIvEDAPJL55jxSSUYfL7jZwRnqlj9XAW2ow%2BQB2d4YCa96W1AYQzOe8A3IrHUNFYIuMBtjlP%2FfRLMBoJJrK%2B3oRAJZ7bIrR1vNW7Y7Z6%2BvvGcUpJKdsMpJeZREgWRZMQsTFpXKVRxUpWuEuK2MzJEc%2FdFDx2d0AaBB0zOATZqmSGwoQnwUqAUIaZJF7NPgs%2Fb6W3cH3wny%2FtJVCi4JuMuYw8syKvQY6pgHnLzDVNB851dBJfKNN9l5c34%2Fu4KGRNbWZ7DcEeb18m5PDSQnLdgd9al17ft2tptCR7p3WHDMSjOjAicB11p4a9oGsv6M1suPJ4CXjOZ8srwqdwA7QvYHH93Ga%2FG4qmprA4onc6JGI4AQ8S6q7bvmU5DxTjy1IMRXKPu4cwqqm25g01gRmaAq9FFZdiE5Ni%2BzrIuz5aGG8W2fTM76yHxofNMD%2BY9OB&X-Amz-Signature=c06b1977b0dbbab0208f755f052aa5203219a5a583645fdc0d68f5115941a55e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5YALQQX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIFnTHgSLowDW8WizMz0fQ4YdmsW0K4C9hLwoPvQrP6KXAiBRjZSGT%2Fl8MXz8VDLQtuGS7ud2BcrwegqZy9rvDJwULir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMxZxzmRjXfVe4zYuOKtwDnHx0WLyeHAnl1pBgSRG01lxct%2Foi8XzP0uhFSv%2ByY%2B3elqeCz602hP1WhuhSSMgSNb3k1VTXVYeNE8cjrBOVDpw1mmRHxqCTOknjpVgo3iZNkkUvdUB0OwjSmGd9EtIvAxg8zt7bRf%2FJIFUH4vR5Rh4QBzQO%2FTwUwMieAEn0ndgG%2FR8hsjEQTKDV%2FVWzn1LpPx1KEe0KRHIj5PYR9KoYrneTq5r%2FHydgb4xDqqHhqByVf8seZ%2B9YMqITya4%2B90J57qrk6ds9oR0cYZk4%2BuU3GqDEiCQmMM7VLF4Xy6Q2E3bHoC1onO6GEATdbLEUGwjsW0yw%2FyMK3auR%2BIWbMkJ1BmGKB18Zpjrpm3S0QhkN%2BXH38%2Bl9s3A6ibqZ2ielG8bPYvnEnx42IZTc1T3CkY%2B8a4%2BmISw3exof5ZKPQnIvEDAPJL55jxSSUYfL7jZwRnqlj9XAW2ow%2BQB2d4YCa96W1AYQzOe8A3IrHUNFYIuMBtjlP%2FfRLMBoJJrK%2B3oRAJZ7bIrR1vNW7Y7Z6%2BvvGcUpJKdsMpJeZREgWRZMQsTFpXKVRxUpWuEuK2MzJEc%2FdFDx2d0AaBB0zOATZqmSGwoQnwUqAUIaZJF7NPgs%2Fb6W3cH3wny%2FtJVCi4JuMuYw8syKvQY6pgHnLzDVNB851dBJfKNN9l5c34%2Fu4KGRNbWZ7DcEeb18m5PDSQnLdgd9al17ft2tptCR7p3WHDMSjOjAicB11p4a9oGsv6M1suPJ4CXjOZ8srwqdwA7QvYHH93Ga%2FG4qmprA4onc6JGI4AQ8S6q7bvmU5DxTjy1IMRXKPu4cwqqm25g01gRmaAq9FFZdiE5Ni%2BzrIuz5aGG8W2fTM76yHxofNMD%2BY9OB&X-Amz-Signature=fcef438119076f910427412590d1bfa8506e7dd97128c56d5487eff5ff9f0068&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5YALQQX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIFnTHgSLowDW8WizMz0fQ4YdmsW0K4C9hLwoPvQrP6KXAiBRjZSGT%2Fl8MXz8VDLQtuGS7ud2BcrwegqZy9rvDJwULir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMxZxzmRjXfVe4zYuOKtwDnHx0WLyeHAnl1pBgSRG01lxct%2Foi8XzP0uhFSv%2ByY%2B3elqeCz602hP1WhuhSSMgSNb3k1VTXVYeNE8cjrBOVDpw1mmRHxqCTOknjpVgo3iZNkkUvdUB0OwjSmGd9EtIvAxg8zt7bRf%2FJIFUH4vR5Rh4QBzQO%2FTwUwMieAEn0ndgG%2FR8hsjEQTKDV%2FVWzn1LpPx1KEe0KRHIj5PYR9KoYrneTq5r%2FHydgb4xDqqHhqByVf8seZ%2B9YMqITya4%2B90J57qrk6ds9oR0cYZk4%2BuU3GqDEiCQmMM7VLF4Xy6Q2E3bHoC1onO6GEATdbLEUGwjsW0yw%2FyMK3auR%2BIWbMkJ1BmGKB18Zpjrpm3S0QhkN%2BXH38%2Bl9s3A6ibqZ2ielG8bPYvnEnx42IZTc1T3CkY%2B8a4%2BmISw3exof5ZKPQnIvEDAPJL55jxSSUYfL7jZwRnqlj9XAW2ow%2BQB2d4YCa96W1AYQzOe8A3IrHUNFYIuMBtjlP%2FfRLMBoJJrK%2B3oRAJZ7bIrR1vNW7Y7Z6%2BvvGcUpJKdsMpJeZREgWRZMQsTFpXKVRxUpWuEuK2MzJEc%2FdFDx2d0AaBB0zOATZqmSGwoQnwUqAUIaZJF7NPgs%2Fb6W3cH3wny%2FtJVCi4JuMuYw8syKvQY6pgHnLzDVNB851dBJfKNN9l5c34%2Fu4KGRNbWZ7DcEeb18m5PDSQnLdgd9al17ft2tptCR7p3WHDMSjOjAicB11p4a9oGsv6M1suPJ4CXjOZ8srwqdwA7QvYHH93Ga%2FG4qmprA4onc6JGI4AQ8S6q7bvmU5DxTjy1IMRXKPu4cwqqm25g01gRmaAq9FFZdiE5Ni%2BzrIuz5aGG8W2fTM76yHxofNMD%2BY9OB&X-Amz-Signature=4f148c1711b8fc90e59332851158e2eca44ff5d0c39f25435ef80f67494098a0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIDXXG5Z%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIHqk%2BTUsP6Z6yIcJoAEpfnwI%2BFA5xJrhbSWHG61Pxw1yAiEAj9ihoKM9r3583ThSi9l0qM5Pm3PnNL12HXcENe7phAoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDEu0HFDHAr%2FRURDgzircAzCdGxXT94tQf6Nj%2F%2Fc4vXeB42Q3ScceXtehBLWS0KtRSHCJ1IYJP9tQ7StSo5dN7vsTE2Eg9jNzxsez3adakr5m4pD05A0%2FcUa0mQwimRrvtfS07OETOn%2FJ0HP%2FzPhOWmqML5lfk0kPOuYJTJkqDuMPPx9es4R8FHEmNBgPR4540h20S5QEzYihOENXXoUoogo1vGDjTqoT7usZPpgY0OLeNHj5pW88Cp4gMbdQU83EM54yNLaIFlHwOoEzmJtn%2FUupjS0UYzQFEEWVCxnhKviDkx%2BhdQiYF4C7Jn1aruRv8mK8x0hrJvA%2BDseoNE6Uun8qLc0PGfR3yAocOI2xh%2BW0GUbUl8WeZkno64vYlJYoj1Groyx0e2HvBPmt6d0g0U9Ok16GfwnKkmA5vc8P%2FaLEQ9zHF9eBc9Ym0zpcTPLcJDVtqtWqxzXK7TsZEFTEhk2ucBCbXq4RgYlaGDKmssim9pG7cL%2BkiZnKcn59iebjWTirmaR145ehzIALIOnJR8moyrttBcUoGaOBkZN9LjOc6D2wdYSdbhHAEgAytObz0rywo6TseIDPDOwZJsNzMkARc%2BV05bWLqbQoe4v3vOhHV5mN%2Ba3CpLT0jk5OHmW1Ew3EMYOTfDtJNJhRMP3Mir0GOqUBreJrX%2BW6afgTHx4B2Ch2BbxNXvlIC3DLbU5w73iEWFT6s8BFKjESGG1zR92km%2B2MQnDdUmgLGCijpf3iEzD3d0%2FpXo6eBsqrxxoyo9BPi0iQ4xisWk6JYN4mjzsHpQRkhsoSzcVC%2F1wO4Bxl4B0ynf1VqxObrB4MCh7Lw%2Fhjgiuf6jQVPvYawwYho6KmTkvckkEEG2%2B2CUJWSPGDdQe%2FfnRoJDqE&X-Amz-Signature=d5076a49ccad4ede29d904e242ad9723f9eb846cb0fa8922cb1210575f592d12&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIDXXG5Z%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIHqk%2BTUsP6Z6yIcJoAEpfnwI%2BFA5xJrhbSWHG61Pxw1yAiEAj9ihoKM9r3583ThSi9l0qM5Pm3PnNL12HXcENe7phAoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDEu0HFDHAr%2FRURDgzircAzCdGxXT94tQf6Nj%2F%2Fc4vXeB42Q3ScceXtehBLWS0KtRSHCJ1IYJP9tQ7StSo5dN7vsTE2Eg9jNzxsez3adakr5m4pD05A0%2FcUa0mQwimRrvtfS07OETOn%2FJ0HP%2FzPhOWmqML5lfk0kPOuYJTJkqDuMPPx9es4R8FHEmNBgPR4540h20S5QEzYihOENXXoUoogo1vGDjTqoT7usZPpgY0OLeNHj5pW88Cp4gMbdQU83EM54yNLaIFlHwOoEzmJtn%2FUupjS0UYzQFEEWVCxnhKviDkx%2BhdQiYF4C7Jn1aruRv8mK8x0hrJvA%2BDseoNE6Uun8qLc0PGfR3yAocOI2xh%2BW0GUbUl8WeZkno64vYlJYoj1Groyx0e2HvBPmt6d0g0U9Ok16GfwnKkmA5vc8P%2FaLEQ9zHF9eBc9Ym0zpcTPLcJDVtqtWqxzXK7TsZEFTEhk2ucBCbXq4RgYlaGDKmssim9pG7cL%2BkiZnKcn59iebjWTirmaR145ehzIALIOnJR8moyrttBcUoGaOBkZN9LjOc6D2wdYSdbhHAEgAytObz0rywo6TseIDPDOwZJsNzMkARc%2BV05bWLqbQoe4v3vOhHV5mN%2Ba3CpLT0jk5OHmW1Ew3EMYOTfDtJNJhRMP3Mir0GOqUBreJrX%2BW6afgTHx4B2Ch2BbxNXvlIC3DLbU5w73iEWFT6s8BFKjESGG1zR92km%2B2MQnDdUmgLGCijpf3iEzD3d0%2FpXo6eBsqrxxoyo9BPi0iQ4xisWk6JYN4mjzsHpQRkhsoSzcVC%2F1wO4Bxl4B0ynf1VqxObrB4MCh7Lw%2Fhjgiuf6jQVPvYawwYho6KmTkvckkEEG2%2B2CUJWSPGDdQe%2FfnRoJDqE&X-Amz-Signature=037f4ffddbc3b4ba5f96c0f8bac8cee34e708ead223229cda3e8a7590e5e714d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIDXXG5Z%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIHqk%2BTUsP6Z6yIcJoAEpfnwI%2BFA5xJrhbSWHG61Pxw1yAiEAj9ihoKM9r3583ThSi9l0qM5Pm3PnNL12HXcENe7phAoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDEu0HFDHAr%2FRURDgzircAzCdGxXT94tQf6Nj%2F%2Fc4vXeB42Q3ScceXtehBLWS0KtRSHCJ1IYJP9tQ7StSo5dN7vsTE2Eg9jNzxsez3adakr5m4pD05A0%2FcUa0mQwimRrvtfS07OETOn%2FJ0HP%2FzPhOWmqML5lfk0kPOuYJTJkqDuMPPx9es4R8FHEmNBgPR4540h20S5QEzYihOENXXoUoogo1vGDjTqoT7usZPpgY0OLeNHj5pW88Cp4gMbdQU83EM54yNLaIFlHwOoEzmJtn%2FUupjS0UYzQFEEWVCxnhKviDkx%2BhdQiYF4C7Jn1aruRv8mK8x0hrJvA%2BDseoNE6Uun8qLc0PGfR3yAocOI2xh%2BW0GUbUl8WeZkno64vYlJYoj1Groyx0e2HvBPmt6d0g0U9Ok16GfwnKkmA5vc8P%2FaLEQ9zHF9eBc9Ym0zpcTPLcJDVtqtWqxzXK7TsZEFTEhk2ucBCbXq4RgYlaGDKmssim9pG7cL%2BkiZnKcn59iebjWTirmaR145ehzIALIOnJR8moyrttBcUoGaOBkZN9LjOc6D2wdYSdbhHAEgAytObz0rywo6TseIDPDOwZJsNzMkARc%2BV05bWLqbQoe4v3vOhHV5mN%2Ba3CpLT0jk5OHmW1Ew3EMYOTfDtJNJhRMP3Mir0GOqUBreJrX%2BW6afgTHx4B2Ch2BbxNXvlIC3DLbU5w73iEWFT6s8BFKjESGG1zR92km%2B2MQnDdUmgLGCijpf3iEzD3d0%2FpXo6eBsqrxxoyo9BPi0iQ4xisWk6JYN4mjzsHpQRkhsoSzcVC%2F1wO4Bxl4B0ynf1VqxObrB4MCh7Lw%2Fhjgiuf6jQVPvYawwYho6KmTkvckkEEG2%2B2CUJWSPGDdQe%2FfnRoJDqE&X-Amz-Signature=3cff960c63b24d318ca7db9afdf23d03bfc8302810c8e1c62562f512dbf26b0f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIDXXG5Z%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIHqk%2BTUsP6Z6yIcJoAEpfnwI%2BFA5xJrhbSWHG61Pxw1yAiEAj9ihoKM9r3583ThSi9l0qM5Pm3PnNL12HXcENe7phAoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDEu0HFDHAr%2FRURDgzircAzCdGxXT94tQf6Nj%2F%2Fc4vXeB42Q3ScceXtehBLWS0KtRSHCJ1IYJP9tQ7StSo5dN7vsTE2Eg9jNzxsez3adakr5m4pD05A0%2FcUa0mQwimRrvtfS07OETOn%2FJ0HP%2FzPhOWmqML5lfk0kPOuYJTJkqDuMPPx9es4R8FHEmNBgPR4540h20S5QEzYihOENXXoUoogo1vGDjTqoT7usZPpgY0OLeNHj5pW88Cp4gMbdQU83EM54yNLaIFlHwOoEzmJtn%2FUupjS0UYzQFEEWVCxnhKviDkx%2BhdQiYF4C7Jn1aruRv8mK8x0hrJvA%2BDseoNE6Uun8qLc0PGfR3yAocOI2xh%2BW0GUbUl8WeZkno64vYlJYoj1Groyx0e2HvBPmt6d0g0U9Ok16GfwnKkmA5vc8P%2FaLEQ9zHF9eBc9Ym0zpcTPLcJDVtqtWqxzXK7TsZEFTEhk2ucBCbXq4RgYlaGDKmssim9pG7cL%2BkiZnKcn59iebjWTirmaR145ehzIALIOnJR8moyrttBcUoGaOBkZN9LjOc6D2wdYSdbhHAEgAytObz0rywo6TseIDPDOwZJsNzMkARc%2BV05bWLqbQoe4v3vOhHV5mN%2Ba3CpLT0jk5OHmW1Ew3EMYOTfDtJNJhRMP3Mir0GOqUBreJrX%2BW6afgTHx4B2Ch2BbxNXvlIC3DLbU5w73iEWFT6s8BFKjESGG1zR92km%2B2MQnDdUmgLGCijpf3iEzD3d0%2FpXo6eBsqrxxoyo9BPi0iQ4xisWk6JYN4mjzsHpQRkhsoSzcVC%2F1wO4Bxl4B0ynf1VqxObrB4MCh7Lw%2Fhjgiuf6jQVPvYawwYho6KmTkvckkEEG2%2B2CUJWSPGDdQe%2FfnRoJDqE&X-Amz-Signature=124d76b3373c2c1f3ffb797dab7d66f7c14cd5214b361ed2a0b4d933f9a3650e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIDXXG5Z%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIHqk%2BTUsP6Z6yIcJoAEpfnwI%2BFA5xJrhbSWHG61Pxw1yAiEAj9ihoKM9r3583ThSi9l0qM5Pm3PnNL12HXcENe7phAoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDEu0HFDHAr%2FRURDgzircAzCdGxXT94tQf6Nj%2F%2Fc4vXeB42Q3ScceXtehBLWS0KtRSHCJ1IYJP9tQ7StSo5dN7vsTE2Eg9jNzxsez3adakr5m4pD05A0%2FcUa0mQwimRrvtfS07OETOn%2FJ0HP%2FzPhOWmqML5lfk0kPOuYJTJkqDuMPPx9es4R8FHEmNBgPR4540h20S5QEzYihOENXXoUoogo1vGDjTqoT7usZPpgY0OLeNHj5pW88Cp4gMbdQU83EM54yNLaIFlHwOoEzmJtn%2FUupjS0UYzQFEEWVCxnhKviDkx%2BhdQiYF4C7Jn1aruRv8mK8x0hrJvA%2BDseoNE6Uun8qLc0PGfR3yAocOI2xh%2BW0GUbUl8WeZkno64vYlJYoj1Groyx0e2HvBPmt6d0g0U9Ok16GfwnKkmA5vc8P%2FaLEQ9zHF9eBc9Ym0zpcTPLcJDVtqtWqxzXK7TsZEFTEhk2ucBCbXq4RgYlaGDKmssim9pG7cL%2BkiZnKcn59iebjWTirmaR145ehzIALIOnJR8moyrttBcUoGaOBkZN9LjOc6D2wdYSdbhHAEgAytObz0rywo6TseIDPDOwZJsNzMkARc%2BV05bWLqbQoe4v3vOhHV5mN%2Ba3CpLT0jk5OHmW1Ew3EMYOTfDtJNJhRMP3Mir0GOqUBreJrX%2BW6afgTHx4B2Ch2BbxNXvlIC3DLbU5w73iEWFT6s8BFKjESGG1zR92km%2B2MQnDdUmgLGCijpf3iEzD3d0%2FpXo6eBsqrxxoyo9BPi0iQ4xisWk6JYN4mjzsHpQRkhsoSzcVC%2F1wO4Bxl4B0ynf1VqxObrB4MCh7Lw%2Fhjgiuf6jQVPvYawwYho6KmTkvckkEEG2%2B2CUJWSPGDdQe%2FfnRoJDqE&X-Amz-Signature=dcf681d8a0f3a24926cf401a4f57799832e7ee47bb76a71b307b306e8d311ed4&X-Amz-SignedHeaders=host&x-id=GetObject)
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


