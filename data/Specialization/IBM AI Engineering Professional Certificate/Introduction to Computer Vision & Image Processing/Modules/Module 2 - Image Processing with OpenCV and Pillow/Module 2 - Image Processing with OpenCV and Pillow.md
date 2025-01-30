

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O2JN7UT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFAldUo3E6nV7h8EVmPpNTGzBdPt76rGOmBzDvMzKWswIhAOilx1vanPy7JzyQIgt%2BYGkiejEyzBONJ4r7cXJ%2FW5SSKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9cqewILvLFAsMrdoq3APomEdoHO%2FBpW%2BkVIox%2FtHFLye3oeb1LfJxdJiGLFsclhoTYib0MiMTqkNvzVyBc8%2B07yN0HuFJ8ZhkfwSpq3d%2FxcPZp69aO0XDumqj3zUbLSXmS7dmEYzIvpP4HYoOXw358M1rPDhaLF0fJlYZZXiUuE8U480xSk7tsUzD37%2FGWDUaJfCJQCD1w2Q%2BLnOYZMlIsklq%2BGq1FNjXGPje4Ntqp6vm9WQOk00HnwNO0YSPXan2d%2B7Qeliz14wm%2Bh2tSEEmkocNNqBqNayTWi0bIJQ5i8jgxZr73WVTCmYMafJvu9Xv14p8DQ4TWPzTpPmFPjSDGdh46pJmjjMcSoaxXgGJKEskFNKMYHkZ2QwoGq8q4BKrR1iqCdL9Om3wzyF%2BSMvFXypTIoZpmXdwwKx5Iu0PM5pf8RgjO6WIlo7KOf8LqtIPh23Xlj%2BkDPdvA0xg1%2BifgHH3MnuKNHZ3ipvLaaW3LjHLU0shnOiiYmsUOGwDWtzMadggx8reN7klFj0G4QtSFAT3mp2kDU%2F%2Fxade%2Bbzk%2BzSSM3gJlPpcqjhBjYHBQHSJlERsvGRJ2%2B63Cqc%2F0bNc8rc4P2Xs9V4kIVHLUfS7kb3wosF9tt9tmDF660Ma5Tl3KRuMkxsJS4EY6TDmouy8BjqkAeNX%2BELFw0HoUNhsNGuD4digiRQD3xew%2FQ9dKAre5ASJd%2FYxogcon82lae0GAxPzFoXzQCpHY5VsIuWQEtIY6W8fXzb0UM3QElj1X9u8CmNSYrAh8n%2BsVJULMXUVMb8LH7T9%2B7gSO0acrWFXTH7Sn7vhGHZMDDYhDQOFJhNgF9Sbmw0HTiTCbdtBo0mNnyvjVG1mRiEY9C4ZWKsN1LKKse5NWmXt&X-Amz-Signature=39c29d8fc923e227b759e24afe9e90c27a65e843c06932b5830fb45a20150075&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PGOMLFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAgzSqqEp3gQ8Mjb3pAffdGLyuypoGdCDS2S6g7tPESgAiBdP1L5jKREJ5dn%2FU%2BJDqbb%2BzRJ4DSN6oZbGY435wZrRyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjbsuKdWSIkHdzJ4fKtwD9UOEk87pD1FFan5oSD%2B4ZIsniDzU2iwHfijfMPqtiJwCcDMDre7IGxN6p49S8FinzL0lZ2yj9DXxTasIz7pll2iwsbng7lVS180nFMCZKD7BH6wf3V%2FHUCy6RgoF89HvpQ%2BistalnnsKBbvV9Tk15rSe%2FOHIVcCk4WG7v%2FgvayG5tVztGM%2BJBThuVtPxnItn8Z3Ii0JrY4UuLSUsZRFGdM5zwa%2Fde%2BW4iVV7mDBTZ5SVjaj%2BEyYxPjHlaBE8i8ZcXLeunW5E7xkCMYC%2BQyFTxO3m195DpstqYvlhtyC1oPtcpghsL9hd4rNPcw%2F1JXnCgDHJPTM6fKQGCCC0FYKK%2BQnmcRJptaKwJHBHqqvD0onSiVyMzXfw6TaljFp1RGYDAruvtY6aN82PRb4WzDnxc88l%2BPPQga3uWlReWRzBNOMZxCle6uAlKcRh3A5WzywCfmjpv%2Bda78ZDaArxWs2zli9q7uG61lkdZ53If9ZktyZGfzHOgxuLRUKYtv5Nsr5UvXznj9%2B36rw68ImMVSicGnBDF0EyQ4BInz1WOaH9sPy6f3ubUvIddr9WiN8F72HzpKmtoBdn21YZBUZ0Ld7IPJ6AZAxlwALMvGNvvEF5tXsH58Vl6Ki48zqxSL8wy6LsvAY6pgFvtckTnIg%2BJCdBGS5oYJfZT8KVeGpCXWXcXGb6ATm1IDii4NtYWv2%2F6OxU%2FDjx13FFnvFAIz1Kq1%2FMaJ1AAtLItaTLIdt%2BROa28THcVSSbEMmUTTz7%2B6TGVhtJPGmRYJRX69HKMNMgNCOrC4rIQ0zPkpCCL1mIGkBOqtiE2EKirOSaO8bVkVa1Vcw6nF7%2F67VyCwxHBOuO8o%2F18899RgsyGXpKIuy0&X-Amz-Signature=3530f62c57084ff72ab761933ad8e2aecf1389004e810bcdef61264fafa29243&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PGOMLFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAgzSqqEp3gQ8Mjb3pAffdGLyuypoGdCDS2S6g7tPESgAiBdP1L5jKREJ5dn%2FU%2BJDqbb%2BzRJ4DSN6oZbGY435wZrRyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjbsuKdWSIkHdzJ4fKtwD9UOEk87pD1FFan5oSD%2B4ZIsniDzU2iwHfijfMPqtiJwCcDMDre7IGxN6p49S8FinzL0lZ2yj9DXxTasIz7pll2iwsbng7lVS180nFMCZKD7BH6wf3V%2FHUCy6RgoF89HvpQ%2BistalnnsKBbvV9Tk15rSe%2FOHIVcCk4WG7v%2FgvayG5tVztGM%2BJBThuVtPxnItn8Z3Ii0JrY4UuLSUsZRFGdM5zwa%2Fde%2BW4iVV7mDBTZ5SVjaj%2BEyYxPjHlaBE8i8ZcXLeunW5E7xkCMYC%2BQyFTxO3m195DpstqYvlhtyC1oPtcpghsL9hd4rNPcw%2F1JXnCgDHJPTM6fKQGCCC0FYKK%2BQnmcRJptaKwJHBHqqvD0onSiVyMzXfw6TaljFp1RGYDAruvtY6aN82PRb4WzDnxc88l%2BPPQga3uWlReWRzBNOMZxCle6uAlKcRh3A5WzywCfmjpv%2Bda78ZDaArxWs2zli9q7uG61lkdZ53If9ZktyZGfzHOgxuLRUKYtv5Nsr5UvXznj9%2B36rw68ImMVSicGnBDF0EyQ4BInz1WOaH9sPy6f3ubUvIddr9WiN8F72HzpKmtoBdn21YZBUZ0Ld7IPJ6AZAxlwALMvGNvvEF5tXsH58Vl6Ki48zqxSL8wy6LsvAY6pgFvtckTnIg%2BJCdBGS5oYJfZT8KVeGpCXWXcXGb6ATm1IDii4NtYWv2%2F6OxU%2FDjx13FFnvFAIz1Kq1%2FMaJ1AAtLItaTLIdt%2BROa28THcVSSbEMmUTTz7%2B6TGVhtJPGmRYJRX69HKMNMgNCOrC4rIQ0zPkpCCL1mIGkBOqtiE2EKirOSaO8bVkVa1Vcw6nF7%2F67VyCwxHBOuO8o%2F18899RgsyGXpKIuy0&X-Amz-Signature=23d87d91dde179864c631b1ffa4ba85910a87c03c9bfa7a8ee59e606e6402eb9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PGOMLFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAgzSqqEp3gQ8Mjb3pAffdGLyuypoGdCDS2S6g7tPESgAiBdP1L5jKREJ5dn%2FU%2BJDqbb%2BzRJ4DSN6oZbGY435wZrRyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjbsuKdWSIkHdzJ4fKtwD9UOEk87pD1FFan5oSD%2B4ZIsniDzU2iwHfijfMPqtiJwCcDMDre7IGxN6p49S8FinzL0lZ2yj9DXxTasIz7pll2iwsbng7lVS180nFMCZKD7BH6wf3V%2FHUCy6RgoF89HvpQ%2BistalnnsKBbvV9Tk15rSe%2FOHIVcCk4WG7v%2FgvayG5tVztGM%2BJBThuVtPxnItn8Z3Ii0JrY4UuLSUsZRFGdM5zwa%2Fde%2BW4iVV7mDBTZ5SVjaj%2BEyYxPjHlaBE8i8ZcXLeunW5E7xkCMYC%2BQyFTxO3m195DpstqYvlhtyC1oPtcpghsL9hd4rNPcw%2F1JXnCgDHJPTM6fKQGCCC0FYKK%2BQnmcRJptaKwJHBHqqvD0onSiVyMzXfw6TaljFp1RGYDAruvtY6aN82PRb4WzDnxc88l%2BPPQga3uWlReWRzBNOMZxCle6uAlKcRh3A5WzywCfmjpv%2Bda78ZDaArxWs2zli9q7uG61lkdZ53If9ZktyZGfzHOgxuLRUKYtv5Nsr5UvXznj9%2B36rw68ImMVSicGnBDF0EyQ4BInz1WOaH9sPy6f3ubUvIddr9WiN8F72HzpKmtoBdn21YZBUZ0Ld7IPJ6AZAxlwALMvGNvvEF5tXsH58Vl6Ki48zqxSL8wy6LsvAY6pgFvtckTnIg%2BJCdBGS5oYJfZT8KVeGpCXWXcXGb6ATm1IDii4NtYWv2%2F6OxU%2FDjx13FFnvFAIz1Kq1%2FMaJ1AAtLItaTLIdt%2BROa28THcVSSbEMmUTTz7%2B6TGVhtJPGmRYJRX69HKMNMgNCOrC4rIQ0zPkpCCL1mIGkBOqtiE2EKirOSaO8bVkVa1Vcw6nF7%2F67VyCwxHBOuO8o%2F18899RgsyGXpKIuy0&X-Amz-Signature=ec95f098e156439b5e6620dd601745d6f10e30bb62ec3af28b02fc1fffa5932a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PGOMLFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAgzSqqEp3gQ8Mjb3pAffdGLyuypoGdCDS2S6g7tPESgAiBdP1L5jKREJ5dn%2FU%2BJDqbb%2BzRJ4DSN6oZbGY435wZrRyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjbsuKdWSIkHdzJ4fKtwD9UOEk87pD1FFan5oSD%2B4ZIsniDzU2iwHfijfMPqtiJwCcDMDre7IGxN6p49S8FinzL0lZ2yj9DXxTasIz7pll2iwsbng7lVS180nFMCZKD7BH6wf3V%2FHUCy6RgoF89HvpQ%2BistalnnsKBbvV9Tk15rSe%2FOHIVcCk4WG7v%2FgvayG5tVztGM%2BJBThuVtPxnItn8Z3Ii0JrY4UuLSUsZRFGdM5zwa%2Fde%2BW4iVV7mDBTZ5SVjaj%2BEyYxPjHlaBE8i8ZcXLeunW5E7xkCMYC%2BQyFTxO3m195DpstqYvlhtyC1oPtcpghsL9hd4rNPcw%2F1JXnCgDHJPTM6fKQGCCC0FYKK%2BQnmcRJptaKwJHBHqqvD0onSiVyMzXfw6TaljFp1RGYDAruvtY6aN82PRb4WzDnxc88l%2BPPQga3uWlReWRzBNOMZxCle6uAlKcRh3A5WzywCfmjpv%2Bda78ZDaArxWs2zli9q7uG61lkdZ53If9ZktyZGfzHOgxuLRUKYtv5Nsr5UvXznj9%2B36rw68ImMVSicGnBDF0EyQ4BInz1WOaH9sPy6f3ubUvIddr9WiN8F72HzpKmtoBdn21YZBUZ0Ld7IPJ6AZAxlwALMvGNvvEF5tXsH58Vl6Ki48zqxSL8wy6LsvAY6pgFvtckTnIg%2BJCdBGS5oYJfZT8KVeGpCXWXcXGb6ATm1IDii4NtYWv2%2F6OxU%2FDjx13FFnvFAIz1Kq1%2FMaJ1AAtLItaTLIdt%2BROa28THcVSSbEMmUTTz7%2B6TGVhtJPGmRYJRX69HKMNMgNCOrC4rIQ0zPkpCCL1mIGkBOqtiE2EKirOSaO8bVkVa1Vcw6nF7%2F67VyCwxHBOuO8o%2F18899RgsyGXpKIuy0&X-Amz-Signature=931311e1b4455c5a5141f24718cd5be98d53dd30f13b6a228e2f3e8310f91189&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PGOMLFQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAgzSqqEp3gQ8Mjb3pAffdGLyuypoGdCDS2S6g7tPESgAiBdP1L5jKREJ5dn%2FU%2BJDqbb%2BzRJ4DSN6oZbGY435wZrRyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjbsuKdWSIkHdzJ4fKtwD9UOEk87pD1FFan5oSD%2B4ZIsniDzU2iwHfijfMPqtiJwCcDMDre7IGxN6p49S8FinzL0lZ2yj9DXxTasIz7pll2iwsbng7lVS180nFMCZKD7BH6wf3V%2FHUCy6RgoF89HvpQ%2BistalnnsKBbvV9Tk15rSe%2FOHIVcCk4WG7v%2FgvayG5tVztGM%2BJBThuVtPxnItn8Z3Ii0JrY4UuLSUsZRFGdM5zwa%2Fde%2BW4iVV7mDBTZ5SVjaj%2BEyYxPjHlaBE8i8ZcXLeunW5E7xkCMYC%2BQyFTxO3m195DpstqYvlhtyC1oPtcpghsL9hd4rNPcw%2F1JXnCgDHJPTM6fKQGCCC0FYKK%2BQnmcRJptaKwJHBHqqvD0onSiVyMzXfw6TaljFp1RGYDAruvtY6aN82PRb4WzDnxc88l%2BPPQga3uWlReWRzBNOMZxCle6uAlKcRh3A5WzywCfmjpv%2Bda78ZDaArxWs2zli9q7uG61lkdZ53If9ZktyZGfzHOgxuLRUKYtv5Nsr5UvXznj9%2B36rw68ImMVSicGnBDF0EyQ4BInz1WOaH9sPy6f3ubUvIddr9WiN8F72HzpKmtoBdn21YZBUZ0Ld7IPJ6AZAxlwALMvGNvvEF5tXsH58Vl6Ki48zqxSL8wy6LsvAY6pgFvtckTnIg%2BJCdBGS5oYJfZT8KVeGpCXWXcXGb6ATm1IDii4NtYWv2%2F6OxU%2FDjx13FFnvFAIz1Kq1%2FMaJ1AAtLItaTLIdt%2BROa28THcVSSbEMmUTTz7%2B6TGVhtJPGmRYJRX69HKMNMgNCOrC4rIQ0zPkpCCL1mIGkBOqtiE2EKirOSaO8bVkVa1Vcw6nF7%2F67VyCwxHBOuO8o%2F18899RgsyGXpKIuy0&X-Amz-Signature=73759da16d1e46f0537261b876d59b4b31208d89e5bd3f551727190262549ec4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O2JN7UT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFAldUo3E6nV7h8EVmPpNTGzBdPt76rGOmBzDvMzKWswIhAOilx1vanPy7JzyQIgt%2BYGkiejEyzBONJ4r7cXJ%2FW5SSKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9cqewILvLFAsMrdoq3APomEdoHO%2FBpW%2BkVIox%2FtHFLye3oeb1LfJxdJiGLFsclhoTYib0MiMTqkNvzVyBc8%2B07yN0HuFJ8ZhkfwSpq3d%2FxcPZp69aO0XDumqj3zUbLSXmS7dmEYzIvpP4HYoOXw358M1rPDhaLF0fJlYZZXiUuE8U480xSk7tsUzD37%2FGWDUaJfCJQCD1w2Q%2BLnOYZMlIsklq%2BGq1FNjXGPje4Ntqp6vm9WQOk00HnwNO0YSPXan2d%2B7Qeliz14wm%2Bh2tSEEmkocNNqBqNayTWi0bIJQ5i8jgxZr73WVTCmYMafJvu9Xv14p8DQ4TWPzTpPmFPjSDGdh46pJmjjMcSoaxXgGJKEskFNKMYHkZ2QwoGq8q4BKrR1iqCdL9Om3wzyF%2BSMvFXypTIoZpmXdwwKx5Iu0PM5pf8RgjO6WIlo7KOf8LqtIPh23Xlj%2BkDPdvA0xg1%2BifgHH3MnuKNHZ3ipvLaaW3LjHLU0shnOiiYmsUOGwDWtzMadggx8reN7klFj0G4QtSFAT3mp2kDU%2F%2Fxade%2Bbzk%2BzSSM3gJlPpcqjhBjYHBQHSJlERsvGRJ2%2B63Cqc%2F0bNc8rc4P2Xs9V4kIVHLUfS7kb3wosF9tt9tmDF660Ma5Tl3KRuMkxsJS4EY6TDmouy8BjqkAeNX%2BELFw0HoUNhsNGuD4digiRQD3xew%2FQ9dKAre5ASJd%2FYxogcon82lae0GAxPzFoXzQCpHY5VsIuWQEtIY6W8fXzb0UM3QElj1X9u8CmNSYrAh8n%2BsVJULMXUVMb8LH7T9%2B7gSO0acrWFXTH7Sn7vhGHZMDDYhDQOFJhNgF9Sbmw0HTiTCbdtBo0mNnyvjVG1mRiEY9C4ZWKsN1LKKse5NWmXt&X-Amz-Signature=68076f7c6d29c1ca1b411013e09c348a4e78b03775a324fc5d68d6e20cc30435&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O2JN7UT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFAldUo3E6nV7h8EVmPpNTGzBdPt76rGOmBzDvMzKWswIhAOilx1vanPy7JzyQIgt%2BYGkiejEyzBONJ4r7cXJ%2FW5SSKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9cqewILvLFAsMrdoq3APomEdoHO%2FBpW%2BkVIox%2FtHFLye3oeb1LfJxdJiGLFsclhoTYib0MiMTqkNvzVyBc8%2B07yN0HuFJ8ZhkfwSpq3d%2FxcPZp69aO0XDumqj3zUbLSXmS7dmEYzIvpP4HYoOXw358M1rPDhaLF0fJlYZZXiUuE8U480xSk7tsUzD37%2FGWDUaJfCJQCD1w2Q%2BLnOYZMlIsklq%2BGq1FNjXGPje4Ntqp6vm9WQOk00HnwNO0YSPXan2d%2B7Qeliz14wm%2Bh2tSEEmkocNNqBqNayTWi0bIJQ5i8jgxZr73WVTCmYMafJvu9Xv14p8DQ4TWPzTpPmFPjSDGdh46pJmjjMcSoaxXgGJKEskFNKMYHkZ2QwoGq8q4BKrR1iqCdL9Om3wzyF%2BSMvFXypTIoZpmXdwwKx5Iu0PM5pf8RgjO6WIlo7KOf8LqtIPh23Xlj%2BkDPdvA0xg1%2BifgHH3MnuKNHZ3ipvLaaW3LjHLU0shnOiiYmsUOGwDWtzMadggx8reN7klFj0G4QtSFAT3mp2kDU%2F%2Fxade%2Bbzk%2BzSSM3gJlPpcqjhBjYHBQHSJlERsvGRJ2%2B63Cqc%2F0bNc8rc4P2Xs9V4kIVHLUfS7kb3wosF9tt9tmDF660Ma5Tl3KRuMkxsJS4EY6TDmouy8BjqkAeNX%2BELFw0HoUNhsNGuD4digiRQD3xew%2FQ9dKAre5ASJd%2FYxogcon82lae0GAxPzFoXzQCpHY5VsIuWQEtIY6W8fXzb0UM3QElj1X9u8CmNSYrAh8n%2BsVJULMXUVMb8LH7T9%2B7gSO0acrWFXTH7Sn7vhGHZMDDYhDQOFJhNgF9Sbmw0HTiTCbdtBo0mNnyvjVG1mRiEY9C4ZWKsN1LKKse5NWmXt&X-Amz-Signature=52e9f1f8ce38fd7ef55605f101329052f75c88c7de4b408469f3fac671a566db&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O2JN7UT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFAldUo3E6nV7h8EVmPpNTGzBdPt76rGOmBzDvMzKWswIhAOilx1vanPy7JzyQIgt%2BYGkiejEyzBONJ4r7cXJ%2FW5SSKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9cqewILvLFAsMrdoq3APomEdoHO%2FBpW%2BkVIox%2FtHFLye3oeb1LfJxdJiGLFsclhoTYib0MiMTqkNvzVyBc8%2B07yN0HuFJ8ZhkfwSpq3d%2FxcPZp69aO0XDumqj3zUbLSXmS7dmEYzIvpP4HYoOXw358M1rPDhaLF0fJlYZZXiUuE8U480xSk7tsUzD37%2FGWDUaJfCJQCD1w2Q%2BLnOYZMlIsklq%2BGq1FNjXGPje4Ntqp6vm9WQOk00HnwNO0YSPXan2d%2B7Qeliz14wm%2Bh2tSEEmkocNNqBqNayTWi0bIJQ5i8jgxZr73WVTCmYMafJvu9Xv14p8DQ4TWPzTpPmFPjSDGdh46pJmjjMcSoaxXgGJKEskFNKMYHkZ2QwoGq8q4BKrR1iqCdL9Om3wzyF%2BSMvFXypTIoZpmXdwwKx5Iu0PM5pf8RgjO6WIlo7KOf8LqtIPh23Xlj%2BkDPdvA0xg1%2BifgHH3MnuKNHZ3ipvLaaW3LjHLU0shnOiiYmsUOGwDWtzMadggx8reN7klFj0G4QtSFAT3mp2kDU%2F%2Fxade%2Bbzk%2BzSSM3gJlPpcqjhBjYHBQHSJlERsvGRJ2%2B63Cqc%2F0bNc8rc4P2Xs9V4kIVHLUfS7kb3wosF9tt9tmDF660Ma5Tl3KRuMkxsJS4EY6TDmouy8BjqkAeNX%2BELFw0HoUNhsNGuD4digiRQD3xew%2FQ9dKAre5ASJd%2FYxogcon82lae0GAxPzFoXzQCpHY5VsIuWQEtIY6W8fXzb0UM3QElj1X9u8CmNSYrAh8n%2BsVJULMXUVMb8LH7T9%2B7gSO0acrWFXTH7Sn7vhGHZMDDYhDQOFJhNgF9Sbmw0HTiTCbdtBo0mNnyvjVG1mRiEY9C4ZWKsN1LKKse5NWmXt&X-Amz-Signature=2827866ae23d77184ac9f1b3171023a3653c2ba715c3ff10d67008cc03ec9b19&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O2JN7UT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFAldUo3E6nV7h8EVmPpNTGzBdPt76rGOmBzDvMzKWswIhAOilx1vanPy7JzyQIgt%2BYGkiejEyzBONJ4r7cXJ%2FW5SSKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9cqewILvLFAsMrdoq3APomEdoHO%2FBpW%2BkVIox%2FtHFLye3oeb1LfJxdJiGLFsclhoTYib0MiMTqkNvzVyBc8%2B07yN0HuFJ8ZhkfwSpq3d%2FxcPZp69aO0XDumqj3zUbLSXmS7dmEYzIvpP4HYoOXw358M1rPDhaLF0fJlYZZXiUuE8U480xSk7tsUzD37%2FGWDUaJfCJQCD1w2Q%2BLnOYZMlIsklq%2BGq1FNjXGPje4Ntqp6vm9WQOk00HnwNO0YSPXan2d%2B7Qeliz14wm%2Bh2tSEEmkocNNqBqNayTWi0bIJQ5i8jgxZr73WVTCmYMafJvu9Xv14p8DQ4TWPzTpPmFPjSDGdh46pJmjjMcSoaxXgGJKEskFNKMYHkZ2QwoGq8q4BKrR1iqCdL9Om3wzyF%2BSMvFXypTIoZpmXdwwKx5Iu0PM5pf8RgjO6WIlo7KOf8LqtIPh23Xlj%2BkDPdvA0xg1%2BifgHH3MnuKNHZ3ipvLaaW3LjHLU0shnOiiYmsUOGwDWtzMadggx8reN7klFj0G4QtSFAT3mp2kDU%2F%2Fxade%2Bbzk%2BzSSM3gJlPpcqjhBjYHBQHSJlERsvGRJ2%2B63Cqc%2F0bNc8rc4P2Xs9V4kIVHLUfS7kb3wosF9tt9tmDF660Ma5Tl3KRuMkxsJS4EY6TDmouy8BjqkAeNX%2BELFw0HoUNhsNGuD4digiRQD3xew%2FQ9dKAre5ASJd%2FYxogcon82lae0GAxPzFoXzQCpHY5VsIuWQEtIY6W8fXzb0UM3QElj1X9u8CmNSYrAh8n%2BsVJULMXUVMb8LH7T9%2B7gSO0acrWFXTH7Sn7vhGHZMDDYhDQOFJhNgF9Sbmw0HTiTCbdtBo0mNnyvjVG1mRiEY9C4ZWKsN1LKKse5NWmXt&X-Amz-Signature=e1e8cba5a6debf481137794dc6de56d865ce4a30dd52fc697d4f47067facdc44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O2JN7UT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFAldUo3E6nV7h8EVmPpNTGzBdPt76rGOmBzDvMzKWswIhAOilx1vanPy7JzyQIgt%2BYGkiejEyzBONJ4r7cXJ%2FW5SSKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9cqewILvLFAsMrdoq3APomEdoHO%2FBpW%2BkVIox%2FtHFLye3oeb1LfJxdJiGLFsclhoTYib0MiMTqkNvzVyBc8%2B07yN0HuFJ8ZhkfwSpq3d%2FxcPZp69aO0XDumqj3zUbLSXmS7dmEYzIvpP4HYoOXw358M1rPDhaLF0fJlYZZXiUuE8U480xSk7tsUzD37%2FGWDUaJfCJQCD1w2Q%2BLnOYZMlIsklq%2BGq1FNjXGPje4Ntqp6vm9WQOk00HnwNO0YSPXan2d%2B7Qeliz14wm%2Bh2tSEEmkocNNqBqNayTWi0bIJQ5i8jgxZr73WVTCmYMafJvu9Xv14p8DQ4TWPzTpPmFPjSDGdh46pJmjjMcSoaxXgGJKEskFNKMYHkZ2QwoGq8q4BKrR1iqCdL9Om3wzyF%2BSMvFXypTIoZpmXdwwKx5Iu0PM5pf8RgjO6WIlo7KOf8LqtIPh23Xlj%2BkDPdvA0xg1%2BifgHH3MnuKNHZ3ipvLaaW3LjHLU0shnOiiYmsUOGwDWtzMadggx8reN7klFj0G4QtSFAT3mp2kDU%2F%2Fxade%2Bbzk%2BzSSM3gJlPpcqjhBjYHBQHSJlERsvGRJ2%2B63Cqc%2F0bNc8rc4P2Xs9V4kIVHLUfS7kb3wosF9tt9tmDF660Ma5Tl3KRuMkxsJS4EY6TDmouy8BjqkAeNX%2BELFw0HoUNhsNGuD4digiRQD3xew%2FQ9dKAre5ASJd%2FYxogcon82lae0GAxPzFoXzQCpHY5VsIuWQEtIY6W8fXzb0UM3QElj1X9u8CmNSYrAh8n%2BsVJULMXUVMb8LH7T9%2B7gSO0acrWFXTH7Sn7vhGHZMDDYhDQOFJhNgF9Sbmw0HTiTCbdtBo0mNnyvjVG1mRiEY9C4ZWKsN1LKKse5NWmXt&X-Amz-Signature=3d94e9457e2b3057399a11bad2a2fa61e7e45f61564df95698a8188c0e49ac41&X-Amz-SignedHeaders=host&x-id=GetObject)
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


