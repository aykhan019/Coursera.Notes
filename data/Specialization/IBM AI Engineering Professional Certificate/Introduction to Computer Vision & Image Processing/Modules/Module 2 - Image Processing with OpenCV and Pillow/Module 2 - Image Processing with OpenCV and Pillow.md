

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QJIQICF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3DcCnTz4XaHVuw88vPUazghsL1vbPjR6FDs2CsdS2fwIhAKUlq8it9xMvPk9N1r8i48%2B9USwiYtmfGYkL0xPtnXBXKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxdcwh2dnhwHI%2FDiW8q3ANPDuHeRDVQAjjpfL1SJQwfEK6EucmO9xrUlhwtvBnsVz5AVXnAHTbysNoGSEqsue18CSv4jVbKIbdxTyDIkeFu7y0Fzrtg7UxNIGOaNApNZGWaHSqejSNLnHseymDu9PBC4LjJV6MIALjprIHbK071AgUQukIxUKKTxWnWKFhueOKU8YLpsCVH3ajmIMcNzKoJzHuPN6OqpQzGHumnZPEfeQPF5Fned4fXsT9JOTw9K3jYn9%2BrfWZKL%2FkF2NAxbGy39zr%2B6RZ27FdE26iDh0EWiEVjNcpxgAfQsPmcL3N0Y%2FeBe%2BBkZio6CXUWN7z101fqokYXNwnWsNYwX3QGyAc3oLyYhP6PaKyA4o2946o8xewroj7Papx%2Fb2OhSSZq3nlA506h7fMevBfupQppnVvnOqvnPxodBoPNorhVgC182m9GzcaG8qqkvchCBy7aZtXA7WR28t3r5heWi278CA0Arq28DLOWFAWXMviCNT3mqpnHXMDEg58W7xkY4NTZ93%2BMAe7WNuWIeay%2BXf9qIhtuoHicfVP21EXj41HUnzYuKbeRtJ5ay9MXPOptv6LWV5jhGAf1P9q6VNJJjf%2FCSeXfYPZcUQhnvP9GiSw25yld97JoStoxLL6TpigvtDDmluu8BjqkAY367buWabNSzpxJ69SEPaxgq8po6AwGga%2FA04Hf96ywAom1eZR0CB5VMqkWlYzs5%2BSd9pn2JINo5bdf95HHWQg0HSqSIJWSnNnrmsTdn%2BunLBAG%2FngBwmS7blZtaj4nJ9lQzyQUge1P8ja1Gap09%2Bmxdy9QHGGwSYdwR3sM3nCovTdJnDV0tGOXqtTLw2xwalEC84Uk4PdqjNpWGhVeh7RjnLT6&X-Amz-Signature=1bf72b585029a72859f04160c9260c372ccb91dca857dd24d0ef08cc7b2ead56&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XGC3GKL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1KMArAlH7BdJ7euJxGT%2Bk9Gii0nwybgyxuN4uF87%2BWwIgU0YBoCjhNqM%2Bp0UNtFDwYBlfKkgCzKDWmlTXrLgroW8qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPgkX7G6i14%2BtFObkSrcA0LA6a9sSbWWS1t6pJTp8bx5Sp%2BTjBhxgWbGppDcg2fCmmKRpNHykFa8eG7ACCZL6CIzTpgJgUMuaYULZqYmeLMSVRa%2B9k57QKB4QPTo7%2BYyBj3mQVjq3b3NIympI6ZV6kE6BJPbpuYa9%2BJoKSdDPqCtbQoKgFivVAYBxmRXIprrDSnPziAkRuIBfyQnwvoitzw%2BZF8NxnzlS6UPJFIuhyzFQ%2BWXuBgVBvlcK0V%2BNgNCM7%2Fe4Jm%2FYrCSReW8FuW5539rTHgm6TrnHypJgJFuIREBTFYYjaupD%2F8HPjHW7uruT9x7OaRFSN%2Bc8xXmgwVtYuktz5GG1GrkULLKoeCQG7l%2BC6hHy0kee8QCV6qs2UymcKyQfq1%2FqcUUVQtqpS5GQ6vrx8vvGay4ylvQRxN%2FRFzq7vLltHIjmnb%2Fm0fBlQdJbfKI6AfkjNIiMWzOTw9jW8T6TLUTqF%2BYIDc0GssvLefwUxUxBlvl2W0nqb4djnao52xoFTNxqwgJEgVEKxXQZX3HdtUTrvbrYDwbgezhhKrkckuAGmPM6BQBqPPZqLylajkQaIa%2FfCKPGsk6wmHgW33MAWuxbsZoYB2wFPJ5Lep0srWAjufhwyrWCXbMTy%2F8Awm1Y%2FCaKadSKASPMPCW67wGOqUBzUiDD6L9SxZfzOTiwBY7pKQLR%2BpVg3CeHGOFdSCSIPsQ2IjnDK5yp7qwbp1ozutuuA3RtByv5uQQUO2lLxvKRX%2FVtL8YAOxotpvy5OgOGkbnWjdqKyJI4GvHZf2%2FBtDmVz76wEkvGa5Z%2Bud3ICk71qrIMd0zxznZ2F2gxH8c0vBoQCFOtk9TM%2FSheuFWYq67yNTFoI4QceK9vcMcCYh6wZoMgIOY&X-Amz-Signature=1ee2c2c72fe8ff6df6afd3705e7b68acbfe1a6a27cc9d1306ae7e5e89e1021fc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XGC3GKL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1KMArAlH7BdJ7euJxGT%2Bk9Gii0nwybgyxuN4uF87%2BWwIgU0YBoCjhNqM%2Bp0UNtFDwYBlfKkgCzKDWmlTXrLgroW8qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPgkX7G6i14%2BtFObkSrcA0LA6a9sSbWWS1t6pJTp8bx5Sp%2BTjBhxgWbGppDcg2fCmmKRpNHykFa8eG7ACCZL6CIzTpgJgUMuaYULZqYmeLMSVRa%2B9k57QKB4QPTo7%2BYyBj3mQVjq3b3NIympI6ZV6kE6BJPbpuYa9%2BJoKSdDPqCtbQoKgFivVAYBxmRXIprrDSnPziAkRuIBfyQnwvoitzw%2BZF8NxnzlS6UPJFIuhyzFQ%2BWXuBgVBvlcK0V%2BNgNCM7%2Fe4Jm%2FYrCSReW8FuW5539rTHgm6TrnHypJgJFuIREBTFYYjaupD%2F8HPjHW7uruT9x7OaRFSN%2Bc8xXmgwVtYuktz5GG1GrkULLKoeCQG7l%2BC6hHy0kee8QCV6qs2UymcKyQfq1%2FqcUUVQtqpS5GQ6vrx8vvGay4ylvQRxN%2FRFzq7vLltHIjmnb%2Fm0fBlQdJbfKI6AfkjNIiMWzOTw9jW8T6TLUTqF%2BYIDc0GssvLefwUxUxBlvl2W0nqb4djnao52xoFTNxqwgJEgVEKxXQZX3HdtUTrvbrYDwbgezhhKrkckuAGmPM6BQBqPPZqLylajkQaIa%2FfCKPGsk6wmHgW33MAWuxbsZoYB2wFPJ5Lep0srWAjufhwyrWCXbMTy%2F8Awm1Y%2FCaKadSKASPMPCW67wGOqUBzUiDD6L9SxZfzOTiwBY7pKQLR%2BpVg3CeHGOFdSCSIPsQ2IjnDK5yp7qwbp1ozutuuA3RtByv5uQQUO2lLxvKRX%2FVtL8YAOxotpvy5OgOGkbnWjdqKyJI4GvHZf2%2FBtDmVz76wEkvGa5Z%2Bud3ICk71qrIMd0zxznZ2F2gxH8c0vBoQCFOtk9TM%2FSheuFWYq67yNTFoI4QceK9vcMcCYh6wZoMgIOY&X-Amz-Signature=0fa61f1786a9e98b08c021107b404209257d79073eb81ac399d2ea914f87556c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XGC3GKL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1KMArAlH7BdJ7euJxGT%2Bk9Gii0nwybgyxuN4uF87%2BWwIgU0YBoCjhNqM%2Bp0UNtFDwYBlfKkgCzKDWmlTXrLgroW8qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPgkX7G6i14%2BtFObkSrcA0LA6a9sSbWWS1t6pJTp8bx5Sp%2BTjBhxgWbGppDcg2fCmmKRpNHykFa8eG7ACCZL6CIzTpgJgUMuaYULZqYmeLMSVRa%2B9k57QKB4QPTo7%2BYyBj3mQVjq3b3NIympI6ZV6kE6BJPbpuYa9%2BJoKSdDPqCtbQoKgFivVAYBxmRXIprrDSnPziAkRuIBfyQnwvoitzw%2BZF8NxnzlS6UPJFIuhyzFQ%2BWXuBgVBvlcK0V%2BNgNCM7%2Fe4Jm%2FYrCSReW8FuW5539rTHgm6TrnHypJgJFuIREBTFYYjaupD%2F8HPjHW7uruT9x7OaRFSN%2Bc8xXmgwVtYuktz5GG1GrkULLKoeCQG7l%2BC6hHy0kee8QCV6qs2UymcKyQfq1%2FqcUUVQtqpS5GQ6vrx8vvGay4ylvQRxN%2FRFzq7vLltHIjmnb%2Fm0fBlQdJbfKI6AfkjNIiMWzOTw9jW8T6TLUTqF%2BYIDc0GssvLefwUxUxBlvl2W0nqb4djnao52xoFTNxqwgJEgVEKxXQZX3HdtUTrvbrYDwbgezhhKrkckuAGmPM6BQBqPPZqLylajkQaIa%2FfCKPGsk6wmHgW33MAWuxbsZoYB2wFPJ5Lep0srWAjufhwyrWCXbMTy%2F8Awm1Y%2FCaKadSKASPMPCW67wGOqUBzUiDD6L9SxZfzOTiwBY7pKQLR%2BpVg3CeHGOFdSCSIPsQ2IjnDK5yp7qwbp1ozutuuA3RtByv5uQQUO2lLxvKRX%2FVtL8YAOxotpvy5OgOGkbnWjdqKyJI4GvHZf2%2FBtDmVz76wEkvGa5Z%2Bud3ICk71qrIMd0zxznZ2F2gxH8c0vBoQCFOtk9TM%2FSheuFWYq67yNTFoI4QceK9vcMcCYh6wZoMgIOY&X-Amz-Signature=665d1813d068a87da4adfff8e6b36c453d0d2f05f13cd0e3ab431af849974104&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XGC3GKL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1KMArAlH7BdJ7euJxGT%2Bk9Gii0nwybgyxuN4uF87%2BWwIgU0YBoCjhNqM%2Bp0UNtFDwYBlfKkgCzKDWmlTXrLgroW8qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPgkX7G6i14%2BtFObkSrcA0LA6a9sSbWWS1t6pJTp8bx5Sp%2BTjBhxgWbGppDcg2fCmmKRpNHykFa8eG7ACCZL6CIzTpgJgUMuaYULZqYmeLMSVRa%2B9k57QKB4QPTo7%2BYyBj3mQVjq3b3NIympI6ZV6kE6BJPbpuYa9%2BJoKSdDPqCtbQoKgFivVAYBxmRXIprrDSnPziAkRuIBfyQnwvoitzw%2BZF8NxnzlS6UPJFIuhyzFQ%2BWXuBgVBvlcK0V%2BNgNCM7%2Fe4Jm%2FYrCSReW8FuW5539rTHgm6TrnHypJgJFuIREBTFYYjaupD%2F8HPjHW7uruT9x7OaRFSN%2Bc8xXmgwVtYuktz5GG1GrkULLKoeCQG7l%2BC6hHy0kee8QCV6qs2UymcKyQfq1%2FqcUUVQtqpS5GQ6vrx8vvGay4ylvQRxN%2FRFzq7vLltHIjmnb%2Fm0fBlQdJbfKI6AfkjNIiMWzOTw9jW8T6TLUTqF%2BYIDc0GssvLefwUxUxBlvl2W0nqb4djnao52xoFTNxqwgJEgVEKxXQZX3HdtUTrvbrYDwbgezhhKrkckuAGmPM6BQBqPPZqLylajkQaIa%2FfCKPGsk6wmHgW33MAWuxbsZoYB2wFPJ5Lep0srWAjufhwyrWCXbMTy%2F8Awm1Y%2FCaKadSKASPMPCW67wGOqUBzUiDD6L9SxZfzOTiwBY7pKQLR%2BpVg3CeHGOFdSCSIPsQ2IjnDK5yp7qwbp1ozutuuA3RtByv5uQQUO2lLxvKRX%2FVtL8YAOxotpvy5OgOGkbnWjdqKyJI4GvHZf2%2FBtDmVz76wEkvGa5Z%2Bud3ICk71qrIMd0zxznZ2F2gxH8c0vBoQCFOtk9TM%2FSheuFWYq67yNTFoI4QceK9vcMcCYh6wZoMgIOY&X-Amz-Signature=b75eac2f6deec56f3bf59b3ec10f7b98960cd645d12dfb96a12a0c2fb918a660&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XGC3GKL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1KMArAlH7BdJ7euJxGT%2Bk9Gii0nwybgyxuN4uF87%2BWwIgU0YBoCjhNqM%2Bp0UNtFDwYBlfKkgCzKDWmlTXrLgroW8qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPgkX7G6i14%2BtFObkSrcA0LA6a9sSbWWS1t6pJTp8bx5Sp%2BTjBhxgWbGppDcg2fCmmKRpNHykFa8eG7ACCZL6CIzTpgJgUMuaYULZqYmeLMSVRa%2B9k57QKB4QPTo7%2BYyBj3mQVjq3b3NIympI6ZV6kE6BJPbpuYa9%2BJoKSdDPqCtbQoKgFivVAYBxmRXIprrDSnPziAkRuIBfyQnwvoitzw%2BZF8NxnzlS6UPJFIuhyzFQ%2BWXuBgVBvlcK0V%2BNgNCM7%2Fe4Jm%2FYrCSReW8FuW5539rTHgm6TrnHypJgJFuIREBTFYYjaupD%2F8HPjHW7uruT9x7OaRFSN%2Bc8xXmgwVtYuktz5GG1GrkULLKoeCQG7l%2BC6hHy0kee8QCV6qs2UymcKyQfq1%2FqcUUVQtqpS5GQ6vrx8vvGay4ylvQRxN%2FRFzq7vLltHIjmnb%2Fm0fBlQdJbfKI6AfkjNIiMWzOTw9jW8T6TLUTqF%2BYIDc0GssvLefwUxUxBlvl2W0nqb4djnao52xoFTNxqwgJEgVEKxXQZX3HdtUTrvbrYDwbgezhhKrkckuAGmPM6BQBqPPZqLylajkQaIa%2FfCKPGsk6wmHgW33MAWuxbsZoYB2wFPJ5Lep0srWAjufhwyrWCXbMTy%2F8Awm1Y%2FCaKadSKASPMPCW67wGOqUBzUiDD6L9SxZfzOTiwBY7pKQLR%2BpVg3CeHGOFdSCSIPsQ2IjnDK5yp7qwbp1ozutuuA3RtByv5uQQUO2lLxvKRX%2FVtL8YAOxotpvy5OgOGkbnWjdqKyJI4GvHZf2%2FBtDmVz76wEkvGa5Z%2Bud3ICk71qrIMd0zxznZ2F2gxH8c0vBoQCFOtk9TM%2FSheuFWYq67yNTFoI4QceK9vcMcCYh6wZoMgIOY&X-Amz-Signature=d337692f5b1534e905a801527fd5275a1cf3d2f8fba3db0ca442ed4a94cc9ef2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QJIQICF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3DcCnTz4XaHVuw88vPUazghsL1vbPjR6FDs2CsdS2fwIhAKUlq8it9xMvPk9N1r8i48%2B9USwiYtmfGYkL0xPtnXBXKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxdcwh2dnhwHI%2FDiW8q3ANPDuHeRDVQAjjpfL1SJQwfEK6EucmO9xrUlhwtvBnsVz5AVXnAHTbysNoGSEqsue18CSv4jVbKIbdxTyDIkeFu7y0Fzrtg7UxNIGOaNApNZGWaHSqejSNLnHseymDu9PBC4LjJV6MIALjprIHbK071AgUQukIxUKKTxWnWKFhueOKU8YLpsCVH3ajmIMcNzKoJzHuPN6OqpQzGHumnZPEfeQPF5Fned4fXsT9JOTw9K3jYn9%2BrfWZKL%2FkF2NAxbGy39zr%2B6RZ27FdE26iDh0EWiEVjNcpxgAfQsPmcL3N0Y%2FeBe%2BBkZio6CXUWN7z101fqokYXNwnWsNYwX3QGyAc3oLyYhP6PaKyA4o2946o8xewroj7Papx%2Fb2OhSSZq3nlA506h7fMevBfupQppnVvnOqvnPxodBoPNorhVgC182m9GzcaG8qqkvchCBy7aZtXA7WR28t3r5heWi278CA0Arq28DLOWFAWXMviCNT3mqpnHXMDEg58W7xkY4NTZ93%2BMAe7WNuWIeay%2BXf9qIhtuoHicfVP21EXj41HUnzYuKbeRtJ5ay9MXPOptv6LWV5jhGAf1P9q6VNJJjf%2FCSeXfYPZcUQhnvP9GiSw25yld97JoStoxLL6TpigvtDDmluu8BjqkAY367buWabNSzpxJ69SEPaxgq8po6AwGga%2FA04Hf96ywAom1eZR0CB5VMqkWlYzs5%2BSd9pn2JINo5bdf95HHWQg0HSqSIJWSnNnrmsTdn%2BunLBAG%2FngBwmS7blZtaj4nJ9lQzyQUge1P8ja1Gap09%2Bmxdy9QHGGwSYdwR3sM3nCovTdJnDV0tGOXqtTLw2xwalEC84Uk4PdqjNpWGhVeh7RjnLT6&X-Amz-Signature=400bca15753f3f7ec2763fe6c4da37860820ea0a747053d0d60d8584c7a84541&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QJIQICF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3DcCnTz4XaHVuw88vPUazghsL1vbPjR6FDs2CsdS2fwIhAKUlq8it9xMvPk9N1r8i48%2B9USwiYtmfGYkL0xPtnXBXKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxdcwh2dnhwHI%2FDiW8q3ANPDuHeRDVQAjjpfL1SJQwfEK6EucmO9xrUlhwtvBnsVz5AVXnAHTbysNoGSEqsue18CSv4jVbKIbdxTyDIkeFu7y0Fzrtg7UxNIGOaNApNZGWaHSqejSNLnHseymDu9PBC4LjJV6MIALjprIHbK071AgUQukIxUKKTxWnWKFhueOKU8YLpsCVH3ajmIMcNzKoJzHuPN6OqpQzGHumnZPEfeQPF5Fned4fXsT9JOTw9K3jYn9%2BrfWZKL%2FkF2NAxbGy39zr%2B6RZ27FdE26iDh0EWiEVjNcpxgAfQsPmcL3N0Y%2FeBe%2BBkZio6CXUWN7z101fqokYXNwnWsNYwX3QGyAc3oLyYhP6PaKyA4o2946o8xewroj7Papx%2Fb2OhSSZq3nlA506h7fMevBfupQppnVvnOqvnPxodBoPNorhVgC182m9GzcaG8qqkvchCBy7aZtXA7WR28t3r5heWi278CA0Arq28DLOWFAWXMviCNT3mqpnHXMDEg58W7xkY4NTZ93%2BMAe7WNuWIeay%2BXf9qIhtuoHicfVP21EXj41HUnzYuKbeRtJ5ay9MXPOptv6LWV5jhGAf1P9q6VNJJjf%2FCSeXfYPZcUQhnvP9GiSw25yld97JoStoxLL6TpigvtDDmluu8BjqkAY367buWabNSzpxJ69SEPaxgq8po6AwGga%2FA04Hf96ywAom1eZR0CB5VMqkWlYzs5%2BSd9pn2JINo5bdf95HHWQg0HSqSIJWSnNnrmsTdn%2BunLBAG%2FngBwmS7blZtaj4nJ9lQzyQUge1P8ja1Gap09%2Bmxdy9QHGGwSYdwR3sM3nCovTdJnDV0tGOXqtTLw2xwalEC84Uk4PdqjNpWGhVeh7RjnLT6&X-Amz-Signature=fd924c284adf7092a74e1a35e5091cf589569e2612d37c600a304c1f25e9abd0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QJIQICF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3DcCnTz4XaHVuw88vPUazghsL1vbPjR6FDs2CsdS2fwIhAKUlq8it9xMvPk9N1r8i48%2B9USwiYtmfGYkL0xPtnXBXKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxdcwh2dnhwHI%2FDiW8q3ANPDuHeRDVQAjjpfL1SJQwfEK6EucmO9xrUlhwtvBnsVz5AVXnAHTbysNoGSEqsue18CSv4jVbKIbdxTyDIkeFu7y0Fzrtg7UxNIGOaNApNZGWaHSqejSNLnHseymDu9PBC4LjJV6MIALjprIHbK071AgUQukIxUKKTxWnWKFhueOKU8YLpsCVH3ajmIMcNzKoJzHuPN6OqpQzGHumnZPEfeQPF5Fned4fXsT9JOTw9K3jYn9%2BrfWZKL%2FkF2NAxbGy39zr%2B6RZ27FdE26iDh0EWiEVjNcpxgAfQsPmcL3N0Y%2FeBe%2BBkZio6CXUWN7z101fqokYXNwnWsNYwX3QGyAc3oLyYhP6PaKyA4o2946o8xewroj7Papx%2Fb2OhSSZq3nlA506h7fMevBfupQppnVvnOqvnPxodBoPNorhVgC182m9GzcaG8qqkvchCBy7aZtXA7WR28t3r5heWi278CA0Arq28DLOWFAWXMviCNT3mqpnHXMDEg58W7xkY4NTZ93%2BMAe7WNuWIeay%2BXf9qIhtuoHicfVP21EXj41HUnzYuKbeRtJ5ay9MXPOptv6LWV5jhGAf1P9q6VNJJjf%2FCSeXfYPZcUQhnvP9GiSw25yld97JoStoxLL6TpigvtDDmluu8BjqkAY367buWabNSzpxJ69SEPaxgq8po6AwGga%2FA04Hf96ywAom1eZR0CB5VMqkWlYzs5%2BSd9pn2JINo5bdf95HHWQg0HSqSIJWSnNnrmsTdn%2BunLBAG%2FngBwmS7blZtaj4nJ9lQzyQUge1P8ja1Gap09%2Bmxdy9QHGGwSYdwR3sM3nCovTdJnDV0tGOXqtTLw2xwalEC84Uk4PdqjNpWGhVeh7RjnLT6&X-Amz-Signature=dd5351a1a4864031739f1b1e7d4111913032f748eb990e85cd993ab7d6f40719&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QJIQICF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3DcCnTz4XaHVuw88vPUazghsL1vbPjR6FDs2CsdS2fwIhAKUlq8it9xMvPk9N1r8i48%2B9USwiYtmfGYkL0xPtnXBXKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxdcwh2dnhwHI%2FDiW8q3ANPDuHeRDVQAjjpfL1SJQwfEK6EucmO9xrUlhwtvBnsVz5AVXnAHTbysNoGSEqsue18CSv4jVbKIbdxTyDIkeFu7y0Fzrtg7UxNIGOaNApNZGWaHSqejSNLnHseymDu9PBC4LjJV6MIALjprIHbK071AgUQukIxUKKTxWnWKFhueOKU8YLpsCVH3ajmIMcNzKoJzHuPN6OqpQzGHumnZPEfeQPF5Fned4fXsT9JOTw9K3jYn9%2BrfWZKL%2FkF2NAxbGy39zr%2B6RZ27FdE26iDh0EWiEVjNcpxgAfQsPmcL3N0Y%2FeBe%2BBkZio6CXUWN7z101fqokYXNwnWsNYwX3QGyAc3oLyYhP6PaKyA4o2946o8xewroj7Papx%2Fb2OhSSZq3nlA506h7fMevBfupQppnVvnOqvnPxodBoPNorhVgC182m9GzcaG8qqkvchCBy7aZtXA7WR28t3r5heWi278CA0Arq28DLOWFAWXMviCNT3mqpnHXMDEg58W7xkY4NTZ93%2BMAe7WNuWIeay%2BXf9qIhtuoHicfVP21EXj41HUnzYuKbeRtJ5ay9MXPOptv6LWV5jhGAf1P9q6VNJJjf%2FCSeXfYPZcUQhnvP9GiSw25yld97JoStoxLL6TpigvtDDmluu8BjqkAY367buWabNSzpxJ69SEPaxgq8po6AwGga%2FA04Hf96ywAom1eZR0CB5VMqkWlYzs5%2BSd9pn2JINo5bdf95HHWQg0HSqSIJWSnNnrmsTdn%2BunLBAG%2FngBwmS7blZtaj4nJ9lQzyQUge1P8ja1Gap09%2Bmxdy9QHGGwSYdwR3sM3nCovTdJnDV0tGOXqtTLw2xwalEC84Uk4PdqjNpWGhVeh7RjnLT6&X-Amz-Signature=7737470ea94695f4643cc5933a7eaeba07df31e535e2d992e2b7f8090ebcf457&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QJIQICF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3DcCnTz4XaHVuw88vPUazghsL1vbPjR6FDs2CsdS2fwIhAKUlq8it9xMvPk9N1r8i48%2B9USwiYtmfGYkL0xPtnXBXKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxdcwh2dnhwHI%2FDiW8q3ANPDuHeRDVQAjjpfL1SJQwfEK6EucmO9xrUlhwtvBnsVz5AVXnAHTbysNoGSEqsue18CSv4jVbKIbdxTyDIkeFu7y0Fzrtg7UxNIGOaNApNZGWaHSqejSNLnHseymDu9PBC4LjJV6MIALjprIHbK071AgUQukIxUKKTxWnWKFhueOKU8YLpsCVH3ajmIMcNzKoJzHuPN6OqpQzGHumnZPEfeQPF5Fned4fXsT9JOTw9K3jYn9%2BrfWZKL%2FkF2NAxbGy39zr%2B6RZ27FdE26iDh0EWiEVjNcpxgAfQsPmcL3N0Y%2FeBe%2BBkZio6CXUWN7z101fqokYXNwnWsNYwX3QGyAc3oLyYhP6PaKyA4o2946o8xewroj7Papx%2Fb2OhSSZq3nlA506h7fMevBfupQppnVvnOqvnPxodBoPNorhVgC182m9GzcaG8qqkvchCBy7aZtXA7WR28t3r5heWi278CA0Arq28DLOWFAWXMviCNT3mqpnHXMDEg58W7xkY4NTZ93%2BMAe7WNuWIeay%2BXf9qIhtuoHicfVP21EXj41HUnzYuKbeRtJ5ay9MXPOptv6LWV5jhGAf1P9q6VNJJjf%2FCSeXfYPZcUQhnvP9GiSw25yld97JoStoxLL6TpigvtDDmluu8BjqkAY367buWabNSzpxJ69SEPaxgq8po6AwGga%2FA04Hf96ywAom1eZR0CB5VMqkWlYzs5%2BSd9pn2JINo5bdf95HHWQg0HSqSIJWSnNnrmsTdn%2BunLBAG%2FngBwmS7blZtaj4nJ9lQzyQUge1P8ja1Gap09%2Bmxdy9QHGGwSYdwR3sM3nCovTdJnDV0tGOXqtTLw2xwalEC84Uk4PdqjNpWGhVeh7RjnLT6&X-Amz-Signature=cad7ac59110698a78ce8fc7b338c4753bd27211f509b405297bfa10b0340ae0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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


