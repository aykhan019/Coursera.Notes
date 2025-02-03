

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSNRVQHI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFRJnK0NuvngzU9g8h5N8K6dm3FJDxxEGsRga19ae%2FD5AiBzSRQeYP4O6QIBsIC8GX3qxVO8SzKQgRczPMWJARoCSyr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMc1ANH4LdMVxHA94KKtwDyPmzeE9sEGDJt64msWI9JAwfVxPnC3HsTvaTrQbqdN7RMGhvI40cfdqdOY1Z6OXj20WqKu%2BcNpaYN9cRHXa8d4TKNCd%2BmIYSeeLqOoe0GTBChnh3ung%2B9RI2iCugKbH5aa%2B%2FmyESfhjPJz7O85fM4BMhbGAoYIjUrxvqFtPMZ7zI4sYdsEqzYUwirDlsrBXF5gsq8UiISm4QF9fY7vEaXq2eT9NT5WYe59g2pVOTqBEpGPQfvlQeWs%2B7vGAbOyTb%2BSDSorL%2Bhb1lrB9rvxEKGMcnaZWLYwMnLeksXLtWH6oosYNfiDlibU6KtHBbPDucWyEOOGSuEuDU3nBtEd9OE2Rx7407BrjAJNrCROoYLidR9ajKtbzjh6CPTuWoGyaYKt%2FonOw2UDPfZVAdiBWWZKThodS1DgdeNe7BO5bjdR1QOV0QkdnY90MY4QwQNG0YzfHvm1eKD5uHvmHP5cY0InEHW1%2F37KbCvmfc2%2FbGgLEIKKidKKuhGDDFgO%2BSQJt8aL2JB2jptnZerD4QAkrwVwvOQSvye1A32W3tF921dEHuWo1F%2B5PXNh%2BgkT%2FNQghzdX%2BKbUB1qnBlJDv0RBBu70O7DuxMGKZ3AQ6I48%2FIGgltA2QqaC93DiELb%2FAw6%2FGCvQY6pgFd890jprS3fZ6KLK6fNo4J%2FkQnq1ZBHY8%2B3itTlZh3nZozqyafFqjWsWPBwBdevmLxSuLRuG38CqLYrs5PvxcRi%2FG0uMs3PjgtP%2Fih766vHgkqi0Av88WvGtpqgkw5XEI7NcLraO9e6wYi%2F%2F%2FYapVFm5JsiG6UhaWKJYX6Jqly1vtSh6b%2B%2Fq2XCGAJUE8y79fGSYIuEqijbbbal9xXqqSvQDyPJ468&X-Amz-Signature=ce4b8d0fc91ab72cc12550a9b9cc9e0dcf3437c83b4251b765444349d23627e9&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVS73UZY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL7Mch46%2BjPxhq8pifJi%2FsRhX3h9KL8JHJZ%2BvWy9QeYAIhAKANfLA7jbMkt9xzwLahfIy7rOkqGbcGluH1xwG%2B7kn6Kv8DCBYQABoMNjM3NDIzMTgzODA1IgzfXLFfymvyzpgpWDYq3APMfrDBKvC9MYCn1XTVd7BKGF7cRpF%2Ff6D%2FQB6tA0RX%2BMMe6Y7NFWT5QkIHG7zR7FuAM3DqZ1C2nggGv4q8Ug7xKkdCLzK2%2FkaExE74AGVRbuzZgZ2PROGATDlVJ%2FeyvyIRw%2Bm2UrmynML8iNCXuILyNjj7Qu2%2FRRA8iVJ6cPzrhg%2FstaNkW3Ex1Mucq7v6P5mnSpTsZgPg8GCfWG0Vqn2eAA2cLZIIfLZUlwbKQBsDT7pNyfPHnVQltYzB0EdV9Uvj8PXzaCkuGcpFY3ZWCh%2F%2BOZFbMCrX3hPeye7qiblsAcApSEzwlZT0NYE4ztdbInOPgOJ7skHPml1RCNlitYdeydoEt6U8aAzPML2UVfkpvOmrPCYJGKDGKspMDYlA8NcxUChte7m0MPyVsXgE30M72LmUNB0XM2So0Y7B64w2BMsEHoa6w4VBJ6kokVBWd3Y9BApasLrOZ3UB47%2BsqGUXExMcjuO%2FAEEsCFvsoBPhVF4uCD0naCT%2BAz%2FihCwvXc1zSii7Ya2e0AaJaUhjtu0%2BNMb3ZhWFLr%2FobsOwbhyXxcwCg7KP%2FIhoru361mhrKRUex2VJCQUsUJ1PUohzwoRolAxvibTs1E5vkB3O7qejDuqY3D0LbfLi%2FNdrwzCq8YK9BjqkASg0nafbZ1o%2B70BGOVYF%2Ff0uAu%2Fw34b2IbWtuQLqkQTenqwA9Sdm5Ja9K%2FpzC6G5P4sYFu6a7IZBDtnfP8Lr%2FmXWXCuYQ2yzfQG%2BFhyYFThRHluMLC%2BrOSkohqoMwCori5nHUklrEryeH1y3eltTW%2FEj%2B4Nefy%2B0x4%2BGm4ay02XoM1M5QgS%2FH897bCy20tPh%2FImQ3lq%2BQFatT0jlNJqN136%2F3hjY&X-Amz-Signature=bf1b69d0ecc2b46c5c5888d11941a3e86fb75fc5a4d6371a6fc7d074a54de265&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVS73UZY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL7Mch46%2BjPxhq8pifJi%2FsRhX3h9KL8JHJZ%2BvWy9QeYAIhAKANfLA7jbMkt9xzwLahfIy7rOkqGbcGluH1xwG%2B7kn6Kv8DCBYQABoMNjM3NDIzMTgzODA1IgzfXLFfymvyzpgpWDYq3APMfrDBKvC9MYCn1XTVd7BKGF7cRpF%2Ff6D%2FQB6tA0RX%2BMMe6Y7NFWT5QkIHG7zR7FuAM3DqZ1C2nggGv4q8Ug7xKkdCLzK2%2FkaExE74AGVRbuzZgZ2PROGATDlVJ%2FeyvyIRw%2Bm2UrmynML8iNCXuILyNjj7Qu2%2FRRA8iVJ6cPzrhg%2FstaNkW3Ex1Mucq7v6P5mnSpTsZgPg8GCfWG0Vqn2eAA2cLZIIfLZUlwbKQBsDT7pNyfPHnVQltYzB0EdV9Uvj8PXzaCkuGcpFY3ZWCh%2F%2BOZFbMCrX3hPeye7qiblsAcApSEzwlZT0NYE4ztdbInOPgOJ7skHPml1RCNlitYdeydoEt6U8aAzPML2UVfkpvOmrPCYJGKDGKspMDYlA8NcxUChte7m0MPyVsXgE30M72LmUNB0XM2So0Y7B64w2BMsEHoa6w4VBJ6kokVBWd3Y9BApasLrOZ3UB47%2BsqGUXExMcjuO%2FAEEsCFvsoBPhVF4uCD0naCT%2BAz%2FihCwvXc1zSii7Ya2e0AaJaUhjtu0%2BNMb3ZhWFLr%2FobsOwbhyXxcwCg7KP%2FIhoru361mhrKRUex2VJCQUsUJ1PUohzwoRolAxvibTs1E5vkB3O7qejDuqY3D0LbfLi%2FNdrwzCq8YK9BjqkASg0nafbZ1o%2B70BGOVYF%2Ff0uAu%2Fw34b2IbWtuQLqkQTenqwA9Sdm5Ja9K%2FpzC6G5P4sYFu6a7IZBDtnfP8Lr%2FmXWXCuYQ2yzfQG%2BFhyYFThRHluMLC%2BrOSkohqoMwCori5nHUklrEryeH1y3eltTW%2FEj%2B4Nefy%2B0x4%2BGm4ay02XoM1M5QgS%2FH897bCy20tPh%2FImQ3lq%2BQFatT0jlNJqN136%2F3hjY&X-Amz-Signature=5921dcd8d68608ee44b0a55a0f5f3c9fe192e31feac73ca8129aad6f617cf430&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVS73UZY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL7Mch46%2BjPxhq8pifJi%2FsRhX3h9KL8JHJZ%2BvWy9QeYAIhAKANfLA7jbMkt9xzwLahfIy7rOkqGbcGluH1xwG%2B7kn6Kv8DCBYQABoMNjM3NDIzMTgzODA1IgzfXLFfymvyzpgpWDYq3APMfrDBKvC9MYCn1XTVd7BKGF7cRpF%2Ff6D%2FQB6tA0RX%2BMMe6Y7NFWT5QkIHG7zR7FuAM3DqZ1C2nggGv4q8Ug7xKkdCLzK2%2FkaExE74AGVRbuzZgZ2PROGATDlVJ%2FeyvyIRw%2Bm2UrmynML8iNCXuILyNjj7Qu2%2FRRA8iVJ6cPzrhg%2FstaNkW3Ex1Mucq7v6P5mnSpTsZgPg8GCfWG0Vqn2eAA2cLZIIfLZUlwbKQBsDT7pNyfPHnVQltYzB0EdV9Uvj8PXzaCkuGcpFY3ZWCh%2F%2BOZFbMCrX3hPeye7qiblsAcApSEzwlZT0NYE4ztdbInOPgOJ7skHPml1RCNlitYdeydoEt6U8aAzPML2UVfkpvOmrPCYJGKDGKspMDYlA8NcxUChte7m0MPyVsXgE30M72LmUNB0XM2So0Y7B64w2BMsEHoa6w4VBJ6kokVBWd3Y9BApasLrOZ3UB47%2BsqGUXExMcjuO%2FAEEsCFvsoBPhVF4uCD0naCT%2BAz%2FihCwvXc1zSii7Ya2e0AaJaUhjtu0%2BNMb3ZhWFLr%2FobsOwbhyXxcwCg7KP%2FIhoru361mhrKRUex2VJCQUsUJ1PUohzwoRolAxvibTs1E5vkB3O7qejDuqY3D0LbfLi%2FNdrwzCq8YK9BjqkASg0nafbZ1o%2B70BGOVYF%2Ff0uAu%2Fw34b2IbWtuQLqkQTenqwA9Sdm5Ja9K%2FpzC6G5P4sYFu6a7IZBDtnfP8Lr%2FmXWXCuYQ2yzfQG%2BFhyYFThRHluMLC%2BrOSkohqoMwCori5nHUklrEryeH1y3eltTW%2FEj%2B4Nefy%2B0x4%2BGm4ay02XoM1M5QgS%2FH897bCy20tPh%2FImQ3lq%2BQFatT0jlNJqN136%2F3hjY&X-Amz-Signature=f71241cb975a0f256a81862c7f176e1fb89f64785b3449201102197468375abb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVS73UZY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL7Mch46%2BjPxhq8pifJi%2FsRhX3h9KL8JHJZ%2BvWy9QeYAIhAKANfLA7jbMkt9xzwLahfIy7rOkqGbcGluH1xwG%2B7kn6Kv8DCBYQABoMNjM3NDIzMTgzODA1IgzfXLFfymvyzpgpWDYq3APMfrDBKvC9MYCn1XTVd7BKGF7cRpF%2Ff6D%2FQB6tA0RX%2BMMe6Y7NFWT5QkIHG7zR7FuAM3DqZ1C2nggGv4q8Ug7xKkdCLzK2%2FkaExE74AGVRbuzZgZ2PROGATDlVJ%2FeyvyIRw%2Bm2UrmynML8iNCXuILyNjj7Qu2%2FRRA8iVJ6cPzrhg%2FstaNkW3Ex1Mucq7v6P5mnSpTsZgPg8GCfWG0Vqn2eAA2cLZIIfLZUlwbKQBsDT7pNyfPHnVQltYzB0EdV9Uvj8PXzaCkuGcpFY3ZWCh%2F%2BOZFbMCrX3hPeye7qiblsAcApSEzwlZT0NYE4ztdbInOPgOJ7skHPml1RCNlitYdeydoEt6U8aAzPML2UVfkpvOmrPCYJGKDGKspMDYlA8NcxUChte7m0MPyVsXgE30M72LmUNB0XM2So0Y7B64w2BMsEHoa6w4VBJ6kokVBWd3Y9BApasLrOZ3UB47%2BsqGUXExMcjuO%2FAEEsCFvsoBPhVF4uCD0naCT%2BAz%2FihCwvXc1zSii7Ya2e0AaJaUhjtu0%2BNMb3ZhWFLr%2FobsOwbhyXxcwCg7KP%2FIhoru361mhrKRUex2VJCQUsUJ1PUohzwoRolAxvibTs1E5vkB3O7qejDuqY3D0LbfLi%2FNdrwzCq8YK9BjqkASg0nafbZ1o%2B70BGOVYF%2Ff0uAu%2Fw34b2IbWtuQLqkQTenqwA9Sdm5Ja9K%2FpzC6G5P4sYFu6a7IZBDtnfP8Lr%2FmXWXCuYQ2yzfQG%2BFhyYFThRHluMLC%2BrOSkohqoMwCori5nHUklrEryeH1y3eltTW%2FEj%2B4Nefy%2B0x4%2BGm4ay02XoM1M5QgS%2FH897bCy20tPh%2FImQ3lq%2BQFatT0jlNJqN136%2F3hjY&X-Amz-Signature=ea58adbbcf850ea171f0c8881e2818cb3e185779750d8ca6c889af20a7babb32&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVS73UZY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL7Mch46%2BjPxhq8pifJi%2FsRhX3h9KL8JHJZ%2BvWy9QeYAIhAKANfLA7jbMkt9xzwLahfIy7rOkqGbcGluH1xwG%2B7kn6Kv8DCBYQABoMNjM3NDIzMTgzODA1IgzfXLFfymvyzpgpWDYq3APMfrDBKvC9MYCn1XTVd7BKGF7cRpF%2Ff6D%2FQB6tA0RX%2BMMe6Y7NFWT5QkIHG7zR7FuAM3DqZ1C2nggGv4q8Ug7xKkdCLzK2%2FkaExE74AGVRbuzZgZ2PROGATDlVJ%2FeyvyIRw%2Bm2UrmynML8iNCXuILyNjj7Qu2%2FRRA8iVJ6cPzrhg%2FstaNkW3Ex1Mucq7v6P5mnSpTsZgPg8GCfWG0Vqn2eAA2cLZIIfLZUlwbKQBsDT7pNyfPHnVQltYzB0EdV9Uvj8PXzaCkuGcpFY3ZWCh%2F%2BOZFbMCrX3hPeye7qiblsAcApSEzwlZT0NYE4ztdbInOPgOJ7skHPml1RCNlitYdeydoEt6U8aAzPML2UVfkpvOmrPCYJGKDGKspMDYlA8NcxUChte7m0MPyVsXgE30M72LmUNB0XM2So0Y7B64w2BMsEHoa6w4VBJ6kokVBWd3Y9BApasLrOZ3UB47%2BsqGUXExMcjuO%2FAEEsCFvsoBPhVF4uCD0naCT%2BAz%2FihCwvXc1zSii7Ya2e0AaJaUhjtu0%2BNMb3ZhWFLr%2FobsOwbhyXxcwCg7KP%2FIhoru361mhrKRUex2VJCQUsUJ1PUohzwoRolAxvibTs1E5vkB3O7qejDuqY3D0LbfLi%2FNdrwzCq8YK9BjqkASg0nafbZ1o%2B70BGOVYF%2Ff0uAu%2Fw34b2IbWtuQLqkQTenqwA9Sdm5Ja9K%2FpzC6G5P4sYFu6a7IZBDtnfP8Lr%2FmXWXCuYQ2yzfQG%2BFhyYFThRHluMLC%2BrOSkohqoMwCori5nHUklrEryeH1y3eltTW%2FEj%2B4Nefy%2B0x4%2BGm4ay02XoM1M5QgS%2FH897bCy20tPh%2FImQ3lq%2BQFatT0jlNJqN136%2F3hjY&X-Amz-Signature=3e7634c58e2f2d041cfd8b80f3a3168208aea285dcdc5355172f088c681132fd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSNRVQHI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFRJnK0NuvngzU9g8h5N8K6dm3FJDxxEGsRga19ae%2FD5AiBzSRQeYP4O6QIBsIC8GX3qxVO8SzKQgRczPMWJARoCSyr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMc1ANH4LdMVxHA94KKtwDyPmzeE9sEGDJt64msWI9JAwfVxPnC3HsTvaTrQbqdN7RMGhvI40cfdqdOY1Z6OXj20WqKu%2BcNpaYN9cRHXa8d4TKNCd%2BmIYSeeLqOoe0GTBChnh3ung%2B9RI2iCugKbH5aa%2B%2FmyESfhjPJz7O85fM4BMhbGAoYIjUrxvqFtPMZ7zI4sYdsEqzYUwirDlsrBXF5gsq8UiISm4QF9fY7vEaXq2eT9NT5WYe59g2pVOTqBEpGPQfvlQeWs%2B7vGAbOyTb%2BSDSorL%2Bhb1lrB9rvxEKGMcnaZWLYwMnLeksXLtWH6oosYNfiDlibU6KtHBbPDucWyEOOGSuEuDU3nBtEd9OE2Rx7407BrjAJNrCROoYLidR9ajKtbzjh6CPTuWoGyaYKt%2FonOw2UDPfZVAdiBWWZKThodS1DgdeNe7BO5bjdR1QOV0QkdnY90MY4QwQNG0YzfHvm1eKD5uHvmHP5cY0InEHW1%2F37KbCvmfc2%2FbGgLEIKKidKKuhGDDFgO%2BSQJt8aL2JB2jptnZerD4QAkrwVwvOQSvye1A32W3tF921dEHuWo1F%2B5PXNh%2BgkT%2FNQghzdX%2BKbUB1qnBlJDv0RBBu70O7DuxMGKZ3AQ6I48%2FIGgltA2QqaC93DiELb%2FAw6%2FGCvQY6pgFd890jprS3fZ6KLK6fNo4J%2FkQnq1ZBHY8%2B3itTlZh3nZozqyafFqjWsWPBwBdevmLxSuLRuG38CqLYrs5PvxcRi%2FG0uMs3PjgtP%2Fih766vHgkqi0Av88WvGtpqgkw5XEI7NcLraO9e6wYi%2F%2F%2FYapVFm5JsiG6UhaWKJYX6Jqly1vtSh6b%2B%2Fq2XCGAJUE8y79fGSYIuEqijbbbal9xXqqSvQDyPJ468&X-Amz-Signature=ec9a60d9cd08da0d593649475fcb27163555fd7a6e17026c57ac566fe366b0a1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSNRVQHI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFRJnK0NuvngzU9g8h5N8K6dm3FJDxxEGsRga19ae%2FD5AiBzSRQeYP4O6QIBsIC8GX3qxVO8SzKQgRczPMWJARoCSyr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMc1ANH4LdMVxHA94KKtwDyPmzeE9sEGDJt64msWI9JAwfVxPnC3HsTvaTrQbqdN7RMGhvI40cfdqdOY1Z6OXj20WqKu%2BcNpaYN9cRHXa8d4TKNCd%2BmIYSeeLqOoe0GTBChnh3ung%2B9RI2iCugKbH5aa%2B%2FmyESfhjPJz7O85fM4BMhbGAoYIjUrxvqFtPMZ7zI4sYdsEqzYUwirDlsrBXF5gsq8UiISm4QF9fY7vEaXq2eT9NT5WYe59g2pVOTqBEpGPQfvlQeWs%2B7vGAbOyTb%2BSDSorL%2Bhb1lrB9rvxEKGMcnaZWLYwMnLeksXLtWH6oosYNfiDlibU6KtHBbPDucWyEOOGSuEuDU3nBtEd9OE2Rx7407BrjAJNrCROoYLidR9ajKtbzjh6CPTuWoGyaYKt%2FonOw2UDPfZVAdiBWWZKThodS1DgdeNe7BO5bjdR1QOV0QkdnY90MY4QwQNG0YzfHvm1eKD5uHvmHP5cY0InEHW1%2F37KbCvmfc2%2FbGgLEIKKidKKuhGDDFgO%2BSQJt8aL2JB2jptnZerD4QAkrwVwvOQSvye1A32W3tF921dEHuWo1F%2B5PXNh%2BgkT%2FNQghzdX%2BKbUB1qnBlJDv0RBBu70O7DuxMGKZ3AQ6I48%2FIGgltA2QqaC93DiELb%2FAw6%2FGCvQY6pgFd890jprS3fZ6KLK6fNo4J%2FkQnq1ZBHY8%2B3itTlZh3nZozqyafFqjWsWPBwBdevmLxSuLRuG38CqLYrs5PvxcRi%2FG0uMs3PjgtP%2Fih766vHgkqi0Av88WvGtpqgkw5XEI7NcLraO9e6wYi%2F%2F%2FYapVFm5JsiG6UhaWKJYX6Jqly1vtSh6b%2B%2Fq2XCGAJUE8y79fGSYIuEqijbbbal9xXqqSvQDyPJ468&X-Amz-Signature=efcebc728e8c7add7e44cf68a363f03f54c24f46842d7709c4aeee3a1fb445cb&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSNRVQHI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFRJnK0NuvngzU9g8h5N8K6dm3FJDxxEGsRga19ae%2FD5AiBzSRQeYP4O6QIBsIC8GX3qxVO8SzKQgRczPMWJARoCSyr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMc1ANH4LdMVxHA94KKtwDyPmzeE9sEGDJt64msWI9JAwfVxPnC3HsTvaTrQbqdN7RMGhvI40cfdqdOY1Z6OXj20WqKu%2BcNpaYN9cRHXa8d4TKNCd%2BmIYSeeLqOoe0GTBChnh3ung%2B9RI2iCugKbH5aa%2B%2FmyESfhjPJz7O85fM4BMhbGAoYIjUrxvqFtPMZ7zI4sYdsEqzYUwirDlsrBXF5gsq8UiISm4QF9fY7vEaXq2eT9NT5WYe59g2pVOTqBEpGPQfvlQeWs%2B7vGAbOyTb%2BSDSorL%2Bhb1lrB9rvxEKGMcnaZWLYwMnLeksXLtWH6oosYNfiDlibU6KtHBbPDucWyEOOGSuEuDU3nBtEd9OE2Rx7407BrjAJNrCROoYLidR9ajKtbzjh6CPTuWoGyaYKt%2FonOw2UDPfZVAdiBWWZKThodS1DgdeNe7BO5bjdR1QOV0QkdnY90MY4QwQNG0YzfHvm1eKD5uHvmHP5cY0InEHW1%2F37KbCvmfc2%2FbGgLEIKKidKKuhGDDFgO%2BSQJt8aL2JB2jptnZerD4QAkrwVwvOQSvye1A32W3tF921dEHuWo1F%2B5PXNh%2BgkT%2FNQghzdX%2BKbUB1qnBlJDv0RBBu70O7DuxMGKZ3AQ6I48%2FIGgltA2QqaC93DiELb%2FAw6%2FGCvQY6pgFd890jprS3fZ6KLK6fNo4J%2FkQnq1ZBHY8%2B3itTlZh3nZozqyafFqjWsWPBwBdevmLxSuLRuG38CqLYrs5PvxcRi%2FG0uMs3PjgtP%2Fih766vHgkqi0Av88WvGtpqgkw5XEI7NcLraO9e6wYi%2F%2F%2FYapVFm5JsiG6UhaWKJYX6Jqly1vtSh6b%2B%2Fq2XCGAJUE8y79fGSYIuEqijbbbal9xXqqSvQDyPJ468&X-Amz-Signature=9876dc6e1a70e61d46336e1fa74b13e342565a75e9053c383dcb89a167188421&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSNRVQHI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFRJnK0NuvngzU9g8h5N8K6dm3FJDxxEGsRga19ae%2FD5AiBzSRQeYP4O6QIBsIC8GX3qxVO8SzKQgRczPMWJARoCSyr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMc1ANH4LdMVxHA94KKtwDyPmzeE9sEGDJt64msWI9JAwfVxPnC3HsTvaTrQbqdN7RMGhvI40cfdqdOY1Z6OXj20WqKu%2BcNpaYN9cRHXa8d4TKNCd%2BmIYSeeLqOoe0GTBChnh3ung%2B9RI2iCugKbH5aa%2B%2FmyESfhjPJz7O85fM4BMhbGAoYIjUrxvqFtPMZ7zI4sYdsEqzYUwirDlsrBXF5gsq8UiISm4QF9fY7vEaXq2eT9NT5WYe59g2pVOTqBEpGPQfvlQeWs%2B7vGAbOyTb%2BSDSorL%2Bhb1lrB9rvxEKGMcnaZWLYwMnLeksXLtWH6oosYNfiDlibU6KtHBbPDucWyEOOGSuEuDU3nBtEd9OE2Rx7407BrjAJNrCROoYLidR9ajKtbzjh6CPTuWoGyaYKt%2FonOw2UDPfZVAdiBWWZKThodS1DgdeNe7BO5bjdR1QOV0QkdnY90MY4QwQNG0YzfHvm1eKD5uHvmHP5cY0InEHW1%2F37KbCvmfc2%2FbGgLEIKKidKKuhGDDFgO%2BSQJt8aL2JB2jptnZerD4QAkrwVwvOQSvye1A32W3tF921dEHuWo1F%2B5PXNh%2BgkT%2FNQghzdX%2BKbUB1qnBlJDv0RBBu70O7DuxMGKZ3AQ6I48%2FIGgltA2QqaC93DiELb%2FAw6%2FGCvQY6pgFd890jprS3fZ6KLK6fNo4J%2FkQnq1ZBHY8%2B3itTlZh3nZozqyafFqjWsWPBwBdevmLxSuLRuG38CqLYrs5PvxcRi%2FG0uMs3PjgtP%2Fih766vHgkqi0Av88WvGtpqgkw5XEI7NcLraO9e6wYi%2F%2F%2FYapVFm5JsiG6UhaWKJYX6Jqly1vtSh6b%2B%2Fq2XCGAJUE8y79fGSYIuEqijbbbal9xXqqSvQDyPJ468&X-Amz-Signature=87fa71ed59703a2c928eb93e9d2ffaeba0d2d53484b4123d5e35a09038bfeeaa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSNRVQHI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFRJnK0NuvngzU9g8h5N8K6dm3FJDxxEGsRga19ae%2FD5AiBzSRQeYP4O6QIBsIC8GX3qxVO8SzKQgRczPMWJARoCSyr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMc1ANH4LdMVxHA94KKtwDyPmzeE9sEGDJt64msWI9JAwfVxPnC3HsTvaTrQbqdN7RMGhvI40cfdqdOY1Z6OXj20WqKu%2BcNpaYN9cRHXa8d4TKNCd%2BmIYSeeLqOoe0GTBChnh3ung%2B9RI2iCugKbH5aa%2B%2FmyESfhjPJz7O85fM4BMhbGAoYIjUrxvqFtPMZ7zI4sYdsEqzYUwirDlsrBXF5gsq8UiISm4QF9fY7vEaXq2eT9NT5WYe59g2pVOTqBEpGPQfvlQeWs%2B7vGAbOyTb%2BSDSorL%2Bhb1lrB9rvxEKGMcnaZWLYwMnLeksXLtWH6oosYNfiDlibU6KtHBbPDucWyEOOGSuEuDU3nBtEd9OE2Rx7407BrjAJNrCROoYLidR9ajKtbzjh6CPTuWoGyaYKt%2FonOw2UDPfZVAdiBWWZKThodS1DgdeNe7BO5bjdR1QOV0QkdnY90MY4QwQNG0YzfHvm1eKD5uHvmHP5cY0InEHW1%2F37KbCvmfc2%2FbGgLEIKKidKKuhGDDFgO%2BSQJt8aL2JB2jptnZerD4QAkrwVwvOQSvye1A32W3tF921dEHuWo1F%2B5PXNh%2BgkT%2FNQghzdX%2BKbUB1qnBlJDv0RBBu70O7DuxMGKZ3AQ6I48%2FIGgltA2QqaC93DiELb%2FAw6%2FGCvQY6pgFd890jprS3fZ6KLK6fNo4J%2FkQnq1ZBHY8%2B3itTlZh3nZozqyafFqjWsWPBwBdevmLxSuLRuG38CqLYrs5PvxcRi%2FG0uMs3PjgtP%2Fih766vHgkqi0Av88WvGtpqgkw5XEI7NcLraO9e6wYi%2F%2F%2FYapVFm5JsiG6UhaWKJYX6Jqly1vtSh6b%2B%2Fq2XCGAJUE8y79fGSYIuEqijbbbal9xXqqSvQDyPJ468&X-Amz-Signature=7516321c8c2dedb617543fe667272f19f423bc2d007a18a86950aeb0a001d7df&X-Amz-SignedHeaders=host&x-id=GetObject)
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


