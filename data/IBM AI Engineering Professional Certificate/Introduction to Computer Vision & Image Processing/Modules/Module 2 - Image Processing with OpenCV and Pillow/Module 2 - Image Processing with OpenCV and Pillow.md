

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFCLMPMK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT%2F0sNiIY9QW5MvetKXC%2BDTDmr5p6cU5VTaWpc0xJcZAIhALhA04FPhi3PpG8OrFP6yQ8tCp0tL6GQ0U%2FTVphQm9NhKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzzpa3pPcddA8yWcpMq3AOeFSRinkcpinRDOC3tAZGXRYZlzCqknAw0i1%2BRHuPcHScppV%2FzgaEsF8oZUgSEMbpRIShAzcxTzJsnqwt0K580OX%2B2YVoN7kCiUhkCR2SsxjRf3OUUfxIR8ULfKkA5wH6UuzrVQ0XmC1Gl7hbOpLlLi0U1ztnet6XDToZWwdue%2BKloTWlrvypZ49XaRcWTBfSEIBag1X2vXYdY0WMlZH8kcX5JbCVwCZJ4re0m3XXaD7BgosBCfQvsTbOkGm98UfJnY0r0ZAYY4i1MkCKOCiFMLCFi9BbErYdeZ3i24lzycI9O2JNW7kn6y%2Bx6j3tjo%2BEYWLnVpHLPhR9K5UdEVNkyLYVM4NGnzB6NN050AQM7%2B%2BBhv%2BIfIKRlA8TPxTt876ctf8z8chr7BVfeMjiNFStsLdDAR9sARCPkKt4%2BD0%2FItaXv0o6EWy2AzBc5roD5LrDoxYHKaezkRzBYUc0w7fdApFYmLCvgAakj3ZPMVW7y9IkqdZUNAINcO9Ke7nBxzEOJm%2B9aHKpUXxSf739uXO3k3EnytvxWCwL1ig2IHBkOJXjWH3975wJN9GOdlSrADuL6Iy9QhAjokiZZkA%2BlAEro4V%2Ff6Oo4olkDPgHtynTugSWwqq%2BtZ6uE4PhM9DCFrfO8BjqkAep9KaBRV5WmjZidcpGIMWVOJqkoBXdmJ0I%2B2wRvwxF4VVmOjdl9r6ir6Qrr9oJ8YH5auy%2FmlNdWsCCHpsubR6Nt8wylqMct8A9GhcZJjlx5eCgj%2FT%2BjqUboh5CNyx5vU8YCv2Eizuk59%2ByuhUyAUJVOEccbJ75BEViiEWssxQSXYd46g1Q%2BuTBJyRG0nnSo88H2%2B2z%2Ff8JfYZYix%2BE%2FGSXPYxPQ&X-Amz-Signature=f9fc373f6f2d46cda6ea9797fc16b4c36fa235e81ac894bbcb8c27ae26d7172d&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZRMXAEX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvuBDfUauLiw6uP6Ws83Qqy%2F4P%2BnHFIhCn4a7OIvLgMwIgEXUsKP1ROcYOfA%2F1afM2HQlD4oVrFeReWKRUGxxPG80qiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP4yAaj3B%2FOQ2%2Fyo0SrcA4kcQQHmUL%2BK7WPKnxsqE5y8dVQW4IA7hoimReRUiCcHDGd8a3IMVIkxqsRko%2F39dcYh3IOBh7V9Hd%2BXxB6TgzUhKg6CsOvrbHN4iWehaQITSu0nECGcAXi4Sf3OLZ0eY9EqPrVLH6gbWDdw0tmVnVbhlz2QdN4xiIGxmmxE6IjB%2Fn5xSimEv%2B9JiADU0XTthPsDQr4BdfNzUWPB%2Fq4EyRKft%2BDx6ADRGfp5CM95wFqAtki%2FHcVEQTuxOl5NCXDr3111CQ6dT5qwjN%2BhH1v%2FIFIGmpawkxujPSp8QgaMcA6MuUV8oqrFIaazny56h%2BXsmR4Vj3C%2FHAaE6UYvk4Ocjz3nuPGY4lxbg2oKvdvkFC666fG32Fgc%2Bwjc7W7Ts%2BqZ01%2F69CUkvpQcxlxYziu4CXuOVfW384JowIkOEoFxA9lMcPHGuzAdZ%2FuYrRUHlH0iTBpSkwFGvHsz9IW%2Fay%2FdL6RL5GxdvZ5aWemS4raOa3DSMd4Uvo9JymWIGgaaYErrDYvk0aj%2FmD17cwoHbnBYf012CEsD35Mil83MAF5kA5ysPC5ETa%2Fev3NGV4qUfFtaiIkpW1BXR4HbYFtgeBka%2B%2BEKJSTFoZUtBh1x5PaErAYUq4zy1XNhqxcmZpuOMLKs87wGOqUBlZWnzLc%2FpPq4xGU2IFovdAWnc%2FXl%2Bj853rhmfU%2Br%2B7YE3YX0UNMsBHZYKp1tJcwUDLwedgXaM1wRg4N3qip1NqBV7xq02ZETl%2FDscK7H5jDBVDu0Q%2FNS7t73LZ4r6dhvJArhjGfvpo4gji0uCzac2kQp6pqEEWrMRicA6ECFL0aGq6S5OkST8%2BG10RwWoX1n76dkNLLIzWcN%2BTeABbYWJstmuRfV&X-Amz-Signature=0663718b68c66c3da0e6a20d0779e94b76e28c95dce865edff832c6bd31874b5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZRMXAEX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvuBDfUauLiw6uP6Ws83Qqy%2F4P%2BnHFIhCn4a7OIvLgMwIgEXUsKP1ROcYOfA%2F1afM2HQlD4oVrFeReWKRUGxxPG80qiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP4yAaj3B%2FOQ2%2Fyo0SrcA4kcQQHmUL%2BK7WPKnxsqE5y8dVQW4IA7hoimReRUiCcHDGd8a3IMVIkxqsRko%2F39dcYh3IOBh7V9Hd%2BXxB6TgzUhKg6CsOvrbHN4iWehaQITSu0nECGcAXi4Sf3OLZ0eY9EqPrVLH6gbWDdw0tmVnVbhlz2QdN4xiIGxmmxE6IjB%2Fn5xSimEv%2B9JiADU0XTthPsDQr4BdfNzUWPB%2Fq4EyRKft%2BDx6ADRGfp5CM95wFqAtki%2FHcVEQTuxOl5NCXDr3111CQ6dT5qwjN%2BhH1v%2FIFIGmpawkxujPSp8QgaMcA6MuUV8oqrFIaazny56h%2BXsmR4Vj3C%2FHAaE6UYvk4Ocjz3nuPGY4lxbg2oKvdvkFC666fG32Fgc%2Bwjc7W7Ts%2BqZ01%2F69CUkvpQcxlxYziu4CXuOVfW384JowIkOEoFxA9lMcPHGuzAdZ%2FuYrRUHlH0iTBpSkwFGvHsz9IW%2Fay%2FdL6RL5GxdvZ5aWemS4raOa3DSMd4Uvo9JymWIGgaaYErrDYvk0aj%2FmD17cwoHbnBYf012CEsD35Mil83MAF5kA5ysPC5ETa%2Fev3NGV4qUfFtaiIkpW1BXR4HbYFtgeBka%2B%2BEKJSTFoZUtBh1x5PaErAYUq4zy1XNhqxcmZpuOMLKs87wGOqUBlZWnzLc%2FpPq4xGU2IFovdAWnc%2FXl%2Bj853rhmfU%2Br%2B7YE3YX0UNMsBHZYKp1tJcwUDLwedgXaM1wRg4N3qip1NqBV7xq02ZETl%2FDscK7H5jDBVDu0Q%2FNS7t73LZ4r6dhvJArhjGfvpo4gji0uCzac2kQp6pqEEWrMRicA6ECFL0aGq6S5OkST8%2BG10RwWoX1n76dkNLLIzWcN%2BTeABbYWJstmuRfV&X-Amz-Signature=7ece709da5f33f9471dce50bd7408dde7cb3d715493518decb3c01ca97360d29&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZRMXAEX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvuBDfUauLiw6uP6Ws83Qqy%2F4P%2BnHFIhCn4a7OIvLgMwIgEXUsKP1ROcYOfA%2F1afM2HQlD4oVrFeReWKRUGxxPG80qiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP4yAaj3B%2FOQ2%2Fyo0SrcA4kcQQHmUL%2BK7WPKnxsqE5y8dVQW4IA7hoimReRUiCcHDGd8a3IMVIkxqsRko%2F39dcYh3IOBh7V9Hd%2BXxB6TgzUhKg6CsOvrbHN4iWehaQITSu0nECGcAXi4Sf3OLZ0eY9EqPrVLH6gbWDdw0tmVnVbhlz2QdN4xiIGxmmxE6IjB%2Fn5xSimEv%2B9JiADU0XTthPsDQr4BdfNzUWPB%2Fq4EyRKft%2BDx6ADRGfp5CM95wFqAtki%2FHcVEQTuxOl5NCXDr3111CQ6dT5qwjN%2BhH1v%2FIFIGmpawkxujPSp8QgaMcA6MuUV8oqrFIaazny56h%2BXsmR4Vj3C%2FHAaE6UYvk4Ocjz3nuPGY4lxbg2oKvdvkFC666fG32Fgc%2Bwjc7W7Ts%2BqZ01%2F69CUkvpQcxlxYziu4CXuOVfW384JowIkOEoFxA9lMcPHGuzAdZ%2FuYrRUHlH0iTBpSkwFGvHsz9IW%2Fay%2FdL6RL5GxdvZ5aWemS4raOa3DSMd4Uvo9JymWIGgaaYErrDYvk0aj%2FmD17cwoHbnBYf012CEsD35Mil83MAF5kA5ysPC5ETa%2Fev3NGV4qUfFtaiIkpW1BXR4HbYFtgeBka%2B%2BEKJSTFoZUtBh1x5PaErAYUq4zy1XNhqxcmZpuOMLKs87wGOqUBlZWnzLc%2FpPq4xGU2IFovdAWnc%2FXl%2Bj853rhmfU%2Br%2B7YE3YX0UNMsBHZYKp1tJcwUDLwedgXaM1wRg4N3qip1NqBV7xq02ZETl%2FDscK7H5jDBVDu0Q%2FNS7t73LZ4r6dhvJArhjGfvpo4gji0uCzac2kQp6pqEEWrMRicA6ECFL0aGq6S5OkST8%2BG10RwWoX1n76dkNLLIzWcN%2BTeABbYWJstmuRfV&X-Amz-Signature=8b07733764ce8ae02396e4d7b9c5170248ef1e1257001b49cac2d86f7e5dfaea&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZRMXAEX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvuBDfUauLiw6uP6Ws83Qqy%2F4P%2BnHFIhCn4a7OIvLgMwIgEXUsKP1ROcYOfA%2F1afM2HQlD4oVrFeReWKRUGxxPG80qiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP4yAaj3B%2FOQ2%2Fyo0SrcA4kcQQHmUL%2BK7WPKnxsqE5y8dVQW4IA7hoimReRUiCcHDGd8a3IMVIkxqsRko%2F39dcYh3IOBh7V9Hd%2BXxB6TgzUhKg6CsOvrbHN4iWehaQITSu0nECGcAXi4Sf3OLZ0eY9EqPrVLH6gbWDdw0tmVnVbhlz2QdN4xiIGxmmxE6IjB%2Fn5xSimEv%2B9JiADU0XTthPsDQr4BdfNzUWPB%2Fq4EyRKft%2BDx6ADRGfp5CM95wFqAtki%2FHcVEQTuxOl5NCXDr3111CQ6dT5qwjN%2BhH1v%2FIFIGmpawkxujPSp8QgaMcA6MuUV8oqrFIaazny56h%2BXsmR4Vj3C%2FHAaE6UYvk4Ocjz3nuPGY4lxbg2oKvdvkFC666fG32Fgc%2Bwjc7W7Ts%2BqZ01%2F69CUkvpQcxlxYziu4CXuOVfW384JowIkOEoFxA9lMcPHGuzAdZ%2FuYrRUHlH0iTBpSkwFGvHsz9IW%2Fay%2FdL6RL5GxdvZ5aWemS4raOa3DSMd4Uvo9JymWIGgaaYErrDYvk0aj%2FmD17cwoHbnBYf012CEsD35Mil83MAF5kA5ysPC5ETa%2Fev3NGV4qUfFtaiIkpW1BXR4HbYFtgeBka%2B%2BEKJSTFoZUtBh1x5PaErAYUq4zy1XNhqxcmZpuOMLKs87wGOqUBlZWnzLc%2FpPq4xGU2IFovdAWnc%2FXl%2Bj853rhmfU%2Br%2B7YE3YX0UNMsBHZYKp1tJcwUDLwedgXaM1wRg4N3qip1NqBV7xq02ZETl%2FDscK7H5jDBVDu0Q%2FNS7t73LZ4r6dhvJArhjGfvpo4gji0uCzac2kQp6pqEEWrMRicA6ECFL0aGq6S5OkST8%2BG10RwWoX1n76dkNLLIzWcN%2BTeABbYWJstmuRfV&X-Amz-Signature=c26759b053aaa13a599a3fa9b0f88fc4ea732eae7fa53e30f3ff1031072f9f58&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZRMXAEX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvuBDfUauLiw6uP6Ws83Qqy%2F4P%2BnHFIhCn4a7OIvLgMwIgEXUsKP1ROcYOfA%2F1afM2HQlD4oVrFeReWKRUGxxPG80qiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP4yAaj3B%2FOQ2%2Fyo0SrcA4kcQQHmUL%2BK7WPKnxsqE5y8dVQW4IA7hoimReRUiCcHDGd8a3IMVIkxqsRko%2F39dcYh3IOBh7V9Hd%2BXxB6TgzUhKg6CsOvrbHN4iWehaQITSu0nECGcAXi4Sf3OLZ0eY9EqPrVLH6gbWDdw0tmVnVbhlz2QdN4xiIGxmmxE6IjB%2Fn5xSimEv%2B9JiADU0XTthPsDQr4BdfNzUWPB%2Fq4EyRKft%2BDx6ADRGfp5CM95wFqAtki%2FHcVEQTuxOl5NCXDr3111CQ6dT5qwjN%2BhH1v%2FIFIGmpawkxujPSp8QgaMcA6MuUV8oqrFIaazny56h%2BXsmR4Vj3C%2FHAaE6UYvk4Ocjz3nuPGY4lxbg2oKvdvkFC666fG32Fgc%2Bwjc7W7Ts%2BqZ01%2F69CUkvpQcxlxYziu4CXuOVfW384JowIkOEoFxA9lMcPHGuzAdZ%2FuYrRUHlH0iTBpSkwFGvHsz9IW%2Fay%2FdL6RL5GxdvZ5aWemS4raOa3DSMd4Uvo9JymWIGgaaYErrDYvk0aj%2FmD17cwoHbnBYf012CEsD35Mil83MAF5kA5ysPC5ETa%2Fev3NGV4qUfFtaiIkpW1BXR4HbYFtgeBka%2B%2BEKJSTFoZUtBh1x5PaErAYUq4zy1XNhqxcmZpuOMLKs87wGOqUBlZWnzLc%2FpPq4xGU2IFovdAWnc%2FXl%2Bj853rhmfU%2Br%2B7YE3YX0UNMsBHZYKp1tJcwUDLwedgXaM1wRg4N3qip1NqBV7xq02ZETl%2FDscK7H5jDBVDu0Q%2FNS7t73LZ4r6dhvJArhjGfvpo4gji0uCzac2kQp6pqEEWrMRicA6ECFL0aGq6S5OkST8%2BG10RwWoX1n76dkNLLIzWcN%2BTeABbYWJstmuRfV&X-Amz-Signature=01d3c14a7a93b674538c127c7a9884ebffadbcf9fffa4a45a5369d34bd429b9e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFCLMPMK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT%2F0sNiIY9QW5MvetKXC%2BDTDmr5p6cU5VTaWpc0xJcZAIhALhA04FPhi3PpG8OrFP6yQ8tCp0tL6GQ0U%2FTVphQm9NhKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzzpa3pPcddA8yWcpMq3AOeFSRinkcpinRDOC3tAZGXRYZlzCqknAw0i1%2BRHuPcHScppV%2FzgaEsF8oZUgSEMbpRIShAzcxTzJsnqwt0K580OX%2B2YVoN7kCiUhkCR2SsxjRf3OUUfxIR8ULfKkA5wH6UuzrVQ0XmC1Gl7hbOpLlLi0U1ztnet6XDToZWwdue%2BKloTWlrvypZ49XaRcWTBfSEIBag1X2vXYdY0WMlZH8kcX5JbCVwCZJ4re0m3XXaD7BgosBCfQvsTbOkGm98UfJnY0r0ZAYY4i1MkCKOCiFMLCFi9BbErYdeZ3i24lzycI9O2JNW7kn6y%2Bx6j3tjo%2BEYWLnVpHLPhR9K5UdEVNkyLYVM4NGnzB6NN050AQM7%2B%2BBhv%2BIfIKRlA8TPxTt876ctf8z8chr7BVfeMjiNFStsLdDAR9sARCPkKt4%2BD0%2FItaXv0o6EWy2AzBc5roD5LrDoxYHKaezkRzBYUc0w7fdApFYmLCvgAakj3ZPMVW7y9IkqdZUNAINcO9Ke7nBxzEOJm%2B9aHKpUXxSf739uXO3k3EnytvxWCwL1ig2IHBkOJXjWH3975wJN9GOdlSrADuL6Iy9QhAjokiZZkA%2BlAEro4V%2Ff6Oo4olkDPgHtynTugSWwqq%2BtZ6uE4PhM9DCFrfO8BjqkAep9KaBRV5WmjZidcpGIMWVOJqkoBXdmJ0I%2B2wRvwxF4VVmOjdl9r6ir6Qrr9oJ8YH5auy%2FmlNdWsCCHpsubR6Nt8wylqMct8A9GhcZJjlx5eCgj%2FT%2BjqUboh5CNyx5vU8YCv2Eizuk59%2ByuhUyAUJVOEccbJ75BEViiEWssxQSXYd46g1Q%2BuTBJyRG0nnSo88H2%2B2z%2Ff8JfYZYix%2BE%2FGSXPYxPQ&X-Amz-Signature=e1b2c63d2257f8195a07595976bedcec4bf91a2bc0e81a8e75fd5298a9c26c7f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFCLMPMK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT%2F0sNiIY9QW5MvetKXC%2BDTDmr5p6cU5VTaWpc0xJcZAIhALhA04FPhi3PpG8OrFP6yQ8tCp0tL6GQ0U%2FTVphQm9NhKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzzpa3pPcddA8yWcpMq3AOeFSRinkcpinRDOC3tAZGXRYZlzCqknAw0i1%2BRHuPcHScppV%2FzgaEsF8oZUgSEMbpRIShAzcxTzJsnqwt0K580OX%2B2YVoN7kCiUhkCR2SsxjRf3OUUfxIR8ULfKkA5wH6UuzrVQ0XmC1Gl7hbOpLlLi0U1ztnet6XDToZWwdue%2BKloTWlrvypZ49XaRcWTBfSEIBag1X2vXYdY0WMlZH8kcX5JbCVwCZJ4re0m3XXaD7BgosBCfQvsTbOkGm98UfJnY0r0ZAYY4i1MkCKOCiFMLCFi9BbErYdeZ3i24lzycI9O2JNW7kn6y%2Bx6j3tjo%2BEYWLnVpHLPhR9K5UdEVNkyLYVM4NGnzB6NN050AQM7%2B%2BBhv%2BIfIKRlA8TPxTt876ctf8z8chr7BVfeMjiNFStsLdDAR9sARCPkKt4%2BD0%2FItaXv0o6EWy2AzBc5roD5LrDoxYHKaezkRzBYUc0w7fdApFYmLCvgAakj3ZPMVW7y9IkqdZUNAINcO9Ke7nBxzEOJm%2B9aHKpUXxSf739uXO3k3EnytvxWCwL1ig2IHBkOJXjWH3975wJN9GOdlSrADuL6Iy9QhAjokiZZkA%2BlAEro4V%2Ff6Oo4olkDPgHtynTugSWwqq%2BtZ6uE4PhM9DCFrfO8BjqkAep9KaBRV5WmjZidcpGIMWVOJqkoBXdmJ0I%2B2wRvwxF4VVmOjdl9r6ir6Qrr9oJ8YH5auy%2FmlNdWsCCHpsubR6Nt8wylqMct8A9GhcZJjlx5eCgj%2FT%2BjqUboh5CNyx5vU8YCv2Eizuk59%2ByuhUyAUJVOEccbJ75BEViiEWssxQSXYd46g1Q%2BuTBJyRG0nnSo88H2%2B2z%2Ff8JfYZYix%2BE%2FGSXPYxPQ&X-Amz-Signature=ad760fe52d666bcb23fbbb3a22108af1640fa47deec8f422e5123efe76ba32e8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFCLMPMK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT%2F0sNiIY9QW5MvetKXC%2BDTDmr5p6cU5VTaWpc0xJcZAIhALhA04FPhi3PpG8OrFP6yQ8tCp0tL6GQ0U%2FTVphQm9NhKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzzpa3pPcddA8yWcpMq3AOeFSRinkcpinRDOC3tAZGXRYZlzCqknAw0i1%2BRHuPcHScppV%2FzgaEsF8oZUgSEMbpRIShAzcxTzJsnqwt0K580OX%2B2YVoN7kCiUhkCR2SsxjRf3OUUfxIR8ULfKkA5wH6UuzrVQ0XmC1Gl7hbOpLlLi0U1ztnet6XDToZWwdue%2BKloTWlrvypZ49XaRcWTBfSEIBag1X2vXYdY0WMlZH8kcX5JbCVwCZJ4re0m3XXaD7BgosBCfQvsTbOkGm98UfJnY0r0ZAYY4i1MkCKOCiFMLCFi9BbErYdeZ3i24lzycI9O2JNW7kn6y%2Bx6j3tjo%2BEYWLnVpHLPhR9K5UdEVNkyLYVM4NGnzB6NN050AQM7%2B%2BBhv%2BIfIKRlA8TPxTt876ctf8z8chr7BVfeMjiNFStsLdDAR9sARCPkKt4%2BD0%2FItaXv0o6EWy2AzBc5roD5LrDoxYHKaezkRzBYUc0w7fdApFYmLCvgAakj3ZPMVW7y9IkqdZUNAINcO9Ke7nBxzEOJm%2B9aHKpUXxSf739uXO3k3EnytvxWCwL1ig2IHBkOJXjWH3975wJN9GOdlSrADuL6Iy9QhAjokiZZkA%2BlAEro4V%2Ff6Oo4olkDPgHtynTugSWwqq%2BtZ6uE4PhM9DCFrfO8BjqkAep9KaBRV5WmjZidcpGIMWVOJqkoBXdmJ0I%2B2wRvwxF4VVmOjdl9r6ir6Qrr9oJ8YH5auy%2FmlNdWsCCHpsubR6Nt8wylqMct8A9GhcZJjlx5eCgj%2FT%2BjqUboh5CNyx5vU8YCv2Eizuk59%2ByuhUyAUJVOEccbJ75BEViiEWssxQSXYd46g1Q%2BuTBJyRG0nnSo88H2%2B2z%2Ff8JfYZYix%2BE%2FGSXPYxPQ&X-Amz-Signature=a986488d58ef35dc4cfeca6f0663654ef31ab8049b2f2cabd22e1bc204d2a639&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFCLMPMK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT%2F0sNiIY9QW5MvetKXC%2BDTDmr5p6cU5VTaWpc0xJcZAIhALhA04FPhi3PpG8OrFP6yQ8tCp0tL6GQ0U%2FTVphQm9NhKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzzpa3pPcddA8yWcpMq3AOeFSRinkcpinRDOC3tAZGXRYZlzCqknAw0i1%2BRHuPcHScppV%2FzgaEsF8oZUgSEMbpRIShAzcxTzJsnqwt0K580OX%2B2YVoN7kCiUhkCR2SsxjRf3OUUfxIR8ULfKkA5wH6UuzrVQ0XmC1Gl7hbOpLlLi0U1ztnet6XDToZWwdue%2BKloTWlrvypZ49XaRcWTBfSEIBag1X2vXYdY0WMlZH8kcX5JbCVwCZJ4re0m3XXaD7BgosBCfQvsTbOkGm98UfJnY0r0ZAYY4i1MkCKOCiFMLCFi9BbErYdeZ3i24lzycI9O2JNW7kn6y%2Bx6j3tjo%2BEYWLnVpHLPhR9K5UdEVNkyLYVM4NGnzB6NN050AQM7%2B%2BBhv%2BIfIKRlA8TPxTt876ctf8z8chr7BVfeMjiNFStsLdDAR9sARCPkKt4%2BD0%2FItaXv0o6EWy2AzBc5roD5LrDoxYHKaezkRzBYUc0w7fdApFYmLCvgAakj3ZPMVW7y9IkqdZUNAINcO9Ke7nBxzEOJm%2B9aHKpUXxSf739uXO3k3EnytvxWCwL1ig2IHBkOJXjWH3975wJN9GOdlSrADuL6Iy9QhAjokiZZkA%2BlAEro4V%2Ff6Oo4olkDPgHtynTugSWwqq%2BtZ6uE4PhM9DCFrfO8BjqkAep9KaBRV5WmjZidcpGIMWVOJqkoBXdmJ0I%2B2wRvwxF4VVmOjdl9r6ir6Qrr9oJ8YH5auy%2FmlNdWsCCHpsubR6Nt8wylqMct8A9GhcZJjlx5eCgj%2FT%2BjqUboh5CNyx5vU8YCv2Eizuk59%2ByuhUyAUJVOEccbJ75BEViiEWssxQSXYd46g1Q%2BuTBJyRG0nnSo88H2%2B2z%2Ff8JfYZYix%2BE%2FGSXPYxPQ&X-Amz-Signature=fb26ad075b2539e0885d5c99f8e631b5af66f2859956b4add040336433a9f727&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFCLMPMK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT%2F0sNiIY9QW5MvetKXC%2BDTDmr5p6cU5VTaWpc0xJcZAIhALhA04FPhi3PpG8OrFP6yQ8tCp0tL6GQ0U%2FTVphQm9NhKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzzpa3pPcddA8yWcpMq3AOeFSRinkcpinRDOC3tAZGXRYZlzCqknAw0i1%2BRHuPcHScppV%2FzgaEsF8oZUgSEMbpRIShAzcxTzJsnqwt0K580OX%2B2YVoN7kCiUhkCR2SsxjRf3OUUfxIR8ULfKkA5wH6UuzrVQ0XmC1Gl7hbOpLlLi0U1ztnet6XDToZWwdue%2BKloTWlrvypZ49XaRcWTBfSEIBag1X2vXYdY0WMlZH8kcX5JbCVwCZJ4re0m3XXaD7BgosBCfQvsTbOkGm98UfJnY0r0ZAYY4i1MkCKOCiFMLCFi9BbErYdeZ3i24lzycI9O2JNW7kn6y%2Bx6j3tjo%2BEYWLnVpHLPhR9K5UdEVNkyLYVM4NGnzB6NN050AQM7%2B%2BBhv%2BIfIKRlA8TPxTt876ctf8z8chr7BVfeMjiNFStsLdDAR9sARCPkKt4%2BD0%2FItaXv0o6EWy2AzBc5roD5LrDoxYHKaezkRzBYUc0w7fdApFYmLCvgAakj3ZPMVW7y9IkqdZUNAINcO9Ke7nBxzEOJm%2B9aHKpUXxSf739uXO3k3EnytvxWCwL1ig2IHBkOJXjWH3975wJN9GOdlSrADuL6Iy9QhAjokiZZkA%2BlAEro4V%2Ff6Oo4olkDPgHtynTugSWwqq%2BtZ6uE4PhM9DCFrfO8BjqkAep9KaBRV5WmjZidcpGIMWVOJqkoBXdmJ0I%2B2wRvwxF4VVmOjdl9r6ir6Qrr9oJ8YH5auy%2FmlNdWsCCHpsubR6Nt8wylqMct8A9GhcZJjlx5eCgj%2FT%2BjqUboh5CNyx5vU8YCv2Eizuk59%2ByuhUyAUJVOEccbJ75BEViiEWssxQSXYd46g1Q%2BuTBJyRG0nnSo88H2%2B2z%2Ff8JfYZYix%2BE%2FGSXPYxPQ&X-Amz-Signature=31aff5c5e84e575e3cbd83f3902a0c27e6b3dcb709708874aec02cf8323ca02b&X-Amz-SignedHeaders=host&x-id=GetObject)
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


