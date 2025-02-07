

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWJ3RAIS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIQDDz3qyrr5KCUWotbtTVbVg2SU30CRw%2Bfr7dgVOte3L9wIffk9HAlJINA7wi%2BwwqNPXaSZR%2FX8xh%2BiggOKHW11sWCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM0kpZ%2Ft%2FImH7M%2BR0pKtwDiKNW173kl0w94I4BFgiJQQouiBeOMkjpP7d%2BEP4hyX84LVaVzX7hXB3M2toRyOrl95lqlGZdaKNktI%2Bf%2FO6wh6jY%2Bvzwctr4kQzyEvMu4oqu2Itocz%2BECELEs4QA5xgBYqyWczW1EtqDxMNqe71IO6qPfyBrRvotjvSa6%2FJso5O%2BhNYDlUaYcKxVnFjbTp4mPFwQNgRwE22EPHlc2nxAes78uTIh3wM1Wzrnam%2FY3AT%2BJQAZcrYu2ra4Hem5C2R1ZYy%2BlKG%2FcvituOhaXAOnfPHisMamZ1U9YEPZFI92jXDrxkv8iVv28w6brPKAIpBLgzDgNDim5zm1UHCbPugAnyublM6PaH8cYDU4jrR5%2FAdPhv%2BzM7U3ZMm7nKAKLI5BmoLaZlXXlIYLMX%2B4P1nas8XL4quxyJVfgRPivGZoP2IERSu746iLXWpBzOKYE7ioJs8jbMcTj3jOmZiyJBGLEUt1Ya6XYkNQU6ZAeOlrVVknJvA826mENXz1Ww4vLpNaQFybNmmZCSCX%2FxHTrUtg5eDPBXCNKl7zxbuBhKLbZwQKbYd2%2FWA6UPM%2BqYAO8vRg4IpGIT68CUb3JHYzRS5JYBUU5eSAkFOQBBBx23niPiX417t1Hcw8SG6NAaEwufmWvQY6pgHZABd8JA4tVqc7aHWPx6h6UaGMDsPvJhqlE7Hd2KERga7l9ngqW4rYl76yPm%2FZ6HBGmc6xpq34u3vLqqijIGsKHksy3bMrNm%2Fv%2BkcayybCR7XLbVE1am%2F0YZ8O6PX7%2BnuUwBwKURQkoAf8w0jcAuYeB7ZLwgrX6DEpgQrpZSjvcEor6uuWqoPljg921oGh1K7hJzPxYJ1UQsrXaC61yUYcN0StVFbH&X-Amz-Signature=ec2c20409b84c311e15e9227bd9e94edb2ca8e2289e28b93bfca4e726c93ae22&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJHQO3KZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQC%2FiPptDM4WrQJ%2FET0rD%2BsXUgMUn2%2Fanp%2FAn2Jm1PSRqgIhAIBzXc8MBbP17HceUKOTDP%2B0RRVnpfLv3u629OzSE1p8Kv8DCHEQABoMNjM3NDIzMTgzODA1IgxDgOygQFmyCXSzt%2Fsq3ANTeZXj7tu3GaKcl8LGndzi4HsSdvCd9ykmqvF0jSxVMFfjoI0ZLWoqaRZ40Y8YDSJ1MOJZgAXK%2B7SIe1FCcJAG8FPfZguJuYVy%2BWvYWnqhEpgce%2Fim2K2kUyK2doNzOtmhyo2iSITKKI6NY1xpc1KFVuSfgcx4bAoRz7zWnBG37kCaqrnMgOdLbNRtZqVTLguZFJJVf06NYcasAi8jDGHBEsJi2z640ZnX9wiPshckq%2FS%2F8Gm71PKqleZuI8MWQd8jguxgdEyC0it4ahu%2FQQiEbnwvj3S1GWxjv13AZ3cgqhxUO2fT3Qk5czxazakfrahQS7I8G9fKjew%2FgXbckTqQbJIAXpEX3%2FRRIffm2M42AW%2BtgtGcj1%2B9L8wqYM%2Bg4SzkRXtX3O2nd5qtyuiTRvq6fWaUrTKQdZbh1CduL2wH1Kf5PTOekKTkSxrmSgoGmb1tACazzO9MXAw4dne5MOGajTrTBfyvt8yi%2BnNnjVC0ooFNIv2Y570c5v3N2cyvJNOOZwYRS%2B5nBzJ2HCSWC29souEP5e2JoKlpQ6ZmisMvrPR3IfYKMNO12L%2BVvRzqza1Xu3fMiVJJTwcH6FuJRGjwxKtFVr0W9QBmh9uS%2Fux8KjSEkU6gc1K4YuodhjC8%2BZa9BjqkAYUVZKUb8R6zQbmk9XWyM0jUqyOr4fxJHwmGtugtvIAwQ3umEonPOpj25TdnyzmEPygBjnwqzs4d4RhPnQu4BQsaGCs8mt6KLtlOS6Wcj5337RpUEtDG0op%2FDXtiNXxlKF7rBZpXGJBBEqv2l9Fq6PIDD9XVCmpKHTGJf8f2l7iQ4cFB8%2BmLQsDxQf5Ru2SF517aA0304TFLdFgq1QpHUGZlJDIW&X-Amz-Signature=d0964538c4a55ca318354b677923aa44cfc1d645e6bda21adaeeb8cd561d7ffc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJHQO3KZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQC%2FiPptDM4WrQJ%2FET0rD%2BsXUgMUn2%2Fanp%2FAn2Jm1PSRqgIhAIBzXc8MBbP17HceUKOTDP%2B0RRVnpfLv3u629OzSE1p8Kv8DCHEQABoMNjM3NDIzMTgzODA1IgxDgOygQFmyCXSzt%2Fsq3ANTeZXj7tu3GaKcl8LGndzi4HsSdvCd9ykmqvF0jSxVMFfjoI0ZLWoqaRZ40Y8YDSJ1MOJZgAXK%2B7SIe1FCcJAG8FPfZguJuYVy%2BWvYWnqhEpgce%2Fim2K2kUyK2doNzOtmhyo2iSITKKI6NY1xpc1KFVuSfgcx4bAoRz7zWnBG37kCaqrnMgOdLbNRtZqVTLguZFJJVf06NYcasAi8jDGHBEsJi2z640ZnX9wiPshckq%2FS%2F8Gm71PKqleZuI8MWQd8jguxgdEyC0it4ahu%2FQQiEbnwvj3S1GWxjv13AZ3cgqhxUO2fT3Qk5czxazakfrahQS7I8G9fKjew%2FgXbckTqQbJIAXpEX3%2FRRIffm2M42AW%2BtgtGcj1%2B9L8wqYM%2Bg4SzkRXtX3O2nd5qtyuiTRvq6fWaUrTKQdZbh1CduL2wH1Kf5PTOekKTkSxrmSgoGmb1tACazzO9MXAw4dne5MOGajTrTBfyvt8yi%2BnNnjVC0ooFNIv2Y570c5v3N2cyvJNOOZwYRS%2B5nBzJ2HCSWC29souEP5e2JoKlpQ6ZmisMvrPR3IfYKMNO12L%2BVvRzqza1Xu3fMiVJJTwcH6FuJRGjwxKtFVr0W9QBmh9uS%2Fux8KjSEkU6gc1K4YuodhjC8%2BZa9BjqkAYUVZKUb8R6zQbmk9XWyM0jUqyOr4fxJHwmGtugtvIAwQ3umEonPOpj25TdnyzmEPygBjnwqzs4d4RhPnQu4BQsaGCs8mt6KLtlOS6Wcj5337RpUEtDG0op%2FDXtiNXxlKF7rBZpXGJBBEqv2l9Fq6PIDD9XVCmpKHTGJf8f2l7iQ4cFB8%2BmLQsDxQf5Ru2SF517aA0304TFLdFgq1QpHUGZlJDIW&X-Amz-Signature=64c5c3b5291b89ba0051f27a9ad4387de8061e188d9dc5072039280df09b276c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJHQO3KZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQC%2FiPptDM4WrQJ%2FET0rD%2BsXUgMUn2%2Fanp%2FAn2Jm1PSRqgIhAIBzXc8MBbP17HceUKOTDP%2B0RRVnpfLv3u629OzSE1p8Kv8DCHEQABoMNjM3NDIzMTgzODA1IgxDgOygQFmyCXSzt%2Fsq3ANTeZXj7tu3GaKcl8LGndzi4HsSdvCd9ykmqvF0jSxVMFfjoI0ZLWoqaRZ40Y8YDSJ1MOJZgAXK%2B7SIe1FCcJAG8FPfZguJuYVy%2BWvYWnqhEpgce%2Fim2K2kUyK2doNzOtmhyo2iSITKKI6NY1xpc1KFVuSfgcx4bAoRz7zWnBG37kCaqrnMgOdLbNRtZqVTLguZFJJVf06NYcasAi8jDGHBEsJi2z640ZnX9wiPshckq%2FS%2F8Gm71PKqleZuI8MWQd8jguxgdEyC0it4ahu%2FQQiEbnwvj3S1GWxjv13AZ3cgqhxUO2fT3Qk5czxazakfrahQS7I8G9fKjew%2FgXbckTqQbJIAXpEX3%2FRRIffm2M42AW%2BtgtGcj1%2B9L8wqYM%2Bg4SzkRXtX3O2nd5qtyuiTRvq6fWaUrTKQdZbh1CduL2wH1Kf5PTOekKTkSxrmSgoGmb1tACazzO9MXAw4dne5MOGajTrTBfyvt8yi%2BnNnjVC0ooFNIv2Y570c5v3N2cyvJNOOZwYRS%2B5nBzJ2HCSWC29souEP5e2JoKlpQ6ZmisMvrPR3IfYKMNO12L%2BVvRzqza1Xu3fMiVJJTwcH6FuJRGjwxKtFVr0W9QBmh9uS%2Fux8KjSEkU6gc1K4YuodhjC8%2BZa9BjqkAYUVZKUb8R6zQbmk9XWyM0jUqyOr4fxJHwmGtugtvIAwQ3umEonPOpj25TdnyzmEPygBjnwqzs4d4RhPnQu4BQsaGCs8mt6KLtlOS6Wcj5337RpUEtDG0op%2FDXtiNXxlKF7rBZpXGJBBEqv2l9Fq6PIDD9XVCmpKHTGJf8f2l7iQ4cFB8%2BmLQsDxQf5Ru2SF517aA0304TFLdFgq1QpHUGZlJDIW&X-Amz-Signature=2f616a722e35f1a94b85dc0a31a6cb58ad58c9f4840ff552b1734daf795b06ad&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJHQO3KZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQC%2FiPptDM4WrQJ%2FET0rD%2BsXUgMUn2%2Fanp%2FAn2Jm1PSRqgIhAIBzXc8MBbP17HceUKOTDP%2B0RRVnpfLv3u629OzSE1p8Kv8DCHEQABoMNjM3NDIzMTgzODA1IgxDgOygQFmyCXSzt%2Fsq3ANTeZXj7tu3GaKcl8LGndzi4HsSdvCd9ykmqvF0jSxVMFfjoI0ZLWoqaRZ40Y8YDSJ1MOJZgAXK%2B7SIe1FCcJAG8FPfZguJuYVy%2BWvYWnqhEpgce%2Fim2K2kUyK2doNzOtmhyo2iSITKKI6NY1xpc1KFVuSfgcx4bAoRz7zWnBG37kCaqrnMgOdLbNRtZqVTLguZFJJVf06NYcasAi8jDGHBEsJi2z640ZnX9wiPshckq%2FS%2F8Gm71PKqleZuI8MWQd8jguxgdEyC0it4ahu%2FQQiEbnwvj3S1GWxjv13AZ3cgqhxUO2fT3Qk5czxazakfrahQS7I8G9fKjew%2FgXbckTqQbJIAXpEX3%2FRRIffm2M42AW%2BtgtGcj1%2B9L8wqYM%2Bg4SzkRXtX3O2nd5qtyuiTRvq6fWaUrTKQdZbh1CduL2wH1Kf5PTOekKTkSxrmSgoGmb1tACazzO9MXAw4dne5MOGajTrTBfyvt8yi%2BnNnjVC0ooFNIv2Y570c5v3N2cyvJNOOZwYRS%2B5nBzJ2HCSWC29souEP5e2JoKlpQ6ZmisMvrPR3IfYKMNO12L%2BVvRzqza1Xu3fMiVJJTwcH6FuJRGjwxKtFVr0W9QBmh9uS%2Fux8KjSEkU6gc1K4YuodhjC8%2BZa9BjqkAYUVZKUb8R6zQbmk9XWyM0jUqyOr4fxJHwmGtugtvIAwQ3umEonPOpj25TdnyzmEPygBjnwqzs4d4RhPnQu4BQsaGCs8mt6KLtlOS6Wcj5337RpUEtDG0op%2FDXtiNXxlKF7rBZpXGJBBEqv2l9Fq6PIDD9XVCmpKHTGJf8f2l7iQ4cFB8%2BmLQsDxQf5Ru2SF517aA0304TFLdFgq1QpHUGZlJDIW&X-Amz-Signature=64ebd11b4a345d47eb46e28bfc341b6e72c0df02ac435915441b90c294442f69&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJHQO3KZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQC%2FiPptDM4WrQJ%2FET0rD%2BsXUgMUn2%2Fanp%2FAn2Jm1PSRqgIhAIBzXc8MBbP17HceUKOTDP%2B0RRVnpfLv3u629OzSE1p8Kv8DCHEQABoMNjM3NDIzMTgzODA1IgxDgOygQFmyCXSzt%2Fsq3ANTeZXj7tu3GaKcl8LGndzi4HsSdvCd9ykmqvF0jSxVMFfjoI0ZLWoqaRZ40Y8YDSJ1MOJZgAXK%2B7SIe1FCcJAG8FPfZguJuYVy%2BWvYWnqhEpgce%2Fim2K2kUyK2doNzOtmhyo2iSITKKI6NY1xpc1KFVuSfgcx4bAoRz7zWnBG37kCaqrnMgOdLbNRtZqVTLguZFJJVf06NYcasAi8jDGHBEsJi2z640ZnX9wiPshckq%2FS%2F8Gm71PKqleZuI8MWQd8jguxgdEyC0it4ahu%2FQQiEbnwvj3S1GWxjv13AZ3cgqhxUO2fT3Qk5czxazakfrahQS7I8G9fKjew%2FgXbckTqQbJIAXpEX3%2FRRIffm2M42AW%2BtgtGcj1%2B9L8wqYM%2Bg4SzkRXtX3O2nd5qtyuiTRvq6fWaUrTKQdZbh1CduL2wH1Kf5PTOekKTkSxrmSgoGmb1tACazzO9MXAw4dne5MOGajTrTBfyvt8yi%2BnNnjVC0ooFNIv2Y570c5v3N2cyvJNOOZwYRS%2B5nBzJ2HCSWC29souEP5e2JoKlpQ6ZmisMvrPR3IfYKMNO12L%2BVvRzqza1Xu3fMiVJJTwcH6FuJRGjwxKtFVr0W9QBmh9uS%2Fux8KjSEkU6gc1K4YuodhjC8%2BZa9BjqkAYUVZKUb8R6zQbmk9XWyM0jUqyOr4fxJHwmGtugtvIAwQ3umEonPOpj25TdnyzmEPygBjnwqzs4d4RhPnQu4BQsaGCs8mt6KLtlOS6Wcj5337RpUEtDG0op%2FDXtiNXxlKF7rBZpXGJBBEqv2l9Fq6PIDD9XVCmpKHTGJf8f2l7iQ4cFB8%2BmLQsDxQf5Ru2SF517aA0304TFLdFgq1QpHUGZlJDIW&X-Amz-Signature=3b180149c2d3a95cb2741f9728a5866f65c06f5929cd05b95b05c7e7cb66ca00&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWJ3RAIS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIQDDz3qyrr5KCUWotbtTVbVg2SU30CRw%2Bfr7dgVOte3L9wIffk9HAlJINA7wi%2BwwqNPXaSZR%2FX8xh%2BiggOKHW11sWCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM0kpZ%2Ft%2FImH7M%2BR0pKtwDiKNW173kl0w94I4BFgiJQQouiBeOMkjpP7d%2BEP4hyX84LVaVzX7hXB3M2toRyOrl95lqlGZdaKNktI%2Bf%2FO6wh6jY%2Bvzwctr4kQzyEvMu4oqu2Itocz%2BECELEs4QA5xgBYqyWczW1EtqDxMNqe71IO6qPfyBrRvotjvSa6%2FJso5O%2BhNYDlUaYcKxVnFjbTp4mPFwQNgRwE22EPHlc2nxAes78uTIh3wM1Wzrnam%2FY3AT%2BJQAZcrYu2ra4Hem5C2R1ZYy%2BlKG%2FcvituOhaXAOnfPHisMamZ1U9YEPZFI92jXDrxkv8iVv28w6brPKAIpBLgzDgNDim5zm1UHCbPugAnyublM6PaH8cYDU4jrR5%2FAdPhv%2BzM7U3ZMm7nKAKLI5BmoLaZlXXlIYLMX%2B4P1nas8XL4quxyJVfgRPivGZoP2IERSu746iLXWpBzOKYE7ioJs8jbMcTj3jOmZiyJBGLEUt1Ya6XYkNQU6ZAeOlrVVknJvA826mENXz1Ww4vLpNaQFybNmmZCSCX%2FxHTrUtg5eDPBXCNKl7zxbuBhKLbZwQKbYd2%2FWA6UPM%2BqYAO8vRg4IpGIT68CUb3JHYzRS5JYBUU5eSAkFOQBBBx23niPiX417t1Hcw8SG6NAaEwufmWvQY6pgHZABd8JA4tVqc7aHWPx6h6UaGMDsPvJhqlE7Hd2KERga7l9ngqW4rYl76yPm%2FZ6HBGmc6xpq34u3vLqqijIGsKHksy3bMrNm%2Fv%2BkcayybCR7XLbVE1am%2F0YZ8O6PX7%2BnuUwBwKURQkoAf8w0jcAuYeB7ZLwgrX6DEpgQrpZSjvcEor6uuWqoPljg921oGh1K7hJzPxYJ1UQsrXaC61yUYcN0StVFbH&X-Amz-Signature=4384019612b3485d2fcd09b9a9ae22f3a49a553702e2eddc5734cf2f0d3d41c9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWJ3RAIS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIQDDz3qyrr5KCUWotbtTVbVg2SU30CRw%2Bfr7dgVOte3L9wIffk9HAlJINA7wi%2BwwqNPXaSZR%2FX8xh%2BiggOKHW11sWCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM0kpZ%2Ft%2FImH7M%2BR0pKtwDiKNW173kl0w94I4BFgiJQQouiBeOMkjpP7d%2BEP4hyX84LVaVzX7hXB3M2toRyOrl95lqlGZdaKNktI%2Bf%2FO6wh6jY%2Bvzwctr4kQzyEvMu4oqu2Itocz%2BECELEs4QA5xgBYqyWczW1EtqDxMNqe71IO6qPfyBrRvotjvSa6%2FJso5O%2BhNYDlUaYcKxVnFjbTp4mPFwQNgRwE22EPHlc2nxAes78uTIh3wM1Wzrnam%2FY3AT%2BJQAZcrYu2ra4Hem5C2R1ZYy%2BlKG%2FcvituOhaXAOnfPHisMamZ1U9YEPZFI92jXDrxkv8iVv28w6brPKAIpBLgzDgNDim5zm1UHCbPugAnyublM6PaH8cYDU4jrR5%2FAdPhv%2BzM7U3ZMm7nKAKLI5BmoLaZlXXlIYLMX%2B4P1nas8XL4quxyJVfgRPivGZoP2IERSu746iLXWpBzOKYE7ioJs8jbMcTj3jOmZiyJBGLEUt1Ya6XYkNQU6ZAeOlrVVknJvA826mENXz1Ww4vLpNaQFybNmmZCSCX%2FxHTrUtg5eDPBXCNKl7zxbuBhKLbZwQKbYd2%2FWA6UPM%2BqYAO8vRg4IpGIT68CUb3JHYzRS5JYBUU5eSAkFOQBBBx23niPiX417t1Hcw8SG6NAaEwufmWvQY6pgHZABd8JA4tVqc7aHWPx6h6UaGMDsPvJhqlE7Hd2KERga7l9ngqW4rYl76yPm%2FZ6HBGmc6xpq34u3vLqqijIGsKHksy3bMrNm%2Fv%2BkcayybCR7XLbVE1am%2F0YZ8O6PX7%2BnuUwBwKURQkoAf8w0jcAuYeB7ZLwgrX6DEpgQrpZSjvcEor6uuWqoPljg921oGh1K7hJzPxYJ1UQsrXaC61yUYcN0StVFbH&X-Amz-Signature=dde629011b641d73b7b53d148c9c3263208e1aaca1e342d2b35931d1d7d1d719&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWJ3RAIS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIQDDz3qyrr5KCUWotbtTVbVg2SU30CRw%2Bfr7dgVOte3L9wIffk9HAlJINA7wi%2BwwqNPXaSZR%2FX8xh%2BiggOKHW11sWCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM0kpZ%2Ft%2FImH7M%2BR0pKtwDiKNW173kl0w94I4BFgiJQQouiBeOMkjpP7d%2BEP4hyX84LVaVzX7hXB3M2toRyOrl95lqlGZdaKNktI%2Bf%2FO6wh6jY%2Bvzwctr4kQzyEvMu4oqu2Itocz%2BECELEs4QA5xgBYqyWczW1EtqDxMNqe71IO6qPfyBrRvotjvSa6%2FJso5O%2BhNYDlUaYcKxVnFjbTp4mPFwQNgRwE22EPHlc2nxAes78uTIh3wM1Wzrnam%2FY3AT%2BJQAZcrYu2ra4Hem5C2R1ZYy%2BlKG%2FcvituOhaXAOnfPHisMamZ1U9YEPZFI92jXDrxkv8iVv28w6brPKAIpBLgzDgNDim5zm1UHCbPugAnyublM6PaH8cYDU4jrR5%2FAdPhv%2BzM7U3ZMm7nKAKLI5BmoLaZlXXlIYLMX%2B4P1nas8XL4quxyJVfgRPivGZoP2IERSu746iLXWpBzOKYE7ioJs8jbMcTj3jOmZiyJBGLEUt1Ya6XYkNQU6ZAeOlrVVknJvA826mENXz1Ww4vLpNaQFybNmmZCSCX%2FxHTrUtg5eDPBXCNKl7zxbuBhKLbZwQKbYd2%2FWA6UPM%2BqYAO8vRg4IpGIT68CUb3JHYzRS5JYBUU5eSAkFOQBBBx23niPiX417t1Hcw8SG6NAaEwufmWvQY6pgHZABd8JA4tVqc7aHWPx6h6UaGMDsPvJhqlE7Hd2KERga7l9ngqW4rYl76yPm%2FZ6HBGmc6xpq34u3vLqqijIGsKHksy3bMrNm%2Fv%2BkcayybCR7XLbVE1am%2F0YZ8O6PX7%2BnuUwBwKURQkoAf8w0jcAuYeB7ZLwgrX6DEpgQrpZSjvcEor6uuWqoPljg921oGh1K7hJzPxYJ1UQsrXaC61yUYcN0StVFbH&X-Amz-Signature=126b25f3e276dac38f55638a2f6443f2e7b4aff84af455575f38b0f4162f4be6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWJ3RAIS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIQDDz3qyrr5KCUWotbtTVbVg2SU30CRw%2Bfr7dgVOte3L9wIffk9HAlJINA7wi%2BwwqNPXaSZR%2FX8xh%2BiggOKHW11sWCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM0kpZ%2Ft%2FImH7M%2BR0pKtwDiKNW173kl0w94I4BFgiJQQouiBeOMkjpP7d%2BEP4hyX84LVaVzX7hXB3M2toRyOrl95lqlGZdaKNktI%2Bf%2FO6wh6jY%2Bvzwctr4kQzyEvMu4oqu2Itocz%2BECELEs4QA5xgBYqyWczW1EtqDxMNqe71IO6qPfyBrRvotjvSa6%2FJso5O%2BhNYDlUaYcKxVnFjbTp4mPFwQNgRwE22EPHlc2nxAes78uTIh3wM1Wzrnam%2FY3AT%2BJQAZcrYu2ra4Hem5C2R1ZYy%2BlKG%2FcvituOhaXAOnfPHisMamZ1U9YEPZFI92jXDrxkv8iVv28w6brPKAIpBLgzDgNDim5zm1UHCbPugAnyublM6PaH8cYDU4jrR5%2FAdPhv%2BzM7U3ZMm7nKAKLI5BmoLaZlXXlIYLMX%2B4P1nas8XL4quxyJVfgRPivGZoP2IERSu746iLXWpBzOKYE7ioJs8jbMcTj3jOmZiyJBGLEUt1Ya6XYkNQU6ZAeOlrVVknJvA826mENXz1Ww4vLpNaQFybNmmZCSCX%2FxHTrUtg5eDPBXCNKl7zxbuBhKLbZwQKbYd2%2FWA6UPM%2BqYAO8vRg4IpGIT68CUb3JHYzRS5JYBUU5eSAkFOQBBBx23niPiX417t1Hcw8SG6NAaEwufmWvQY6pgHZABd8JA4tVqc7aHWPx6h6UaGMDsPvJhqlE7Hd2KERga7l9ngqW4rYl76yPm%2FZ6HBGmc6xpq34u3vLqqijIGsKHksy3bMrNm%2Fv%2BkcayybCR7XLbVE1am%2F0YZ8O6PX7%2BnuUwBwKURQkoAf8w0jcAuYeB7ZLwgrX6DEpgQrpZSjvcEor6uuWqoPljg921oGh1K7hJzPxYJ1UQsrXaC61yUYcN0StVFbH&X-Amz-Signature=a05f0399bf771a63e253687249d33f7ca160a2d109ae49de638c1e8dbcee0097&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWJ3RAIS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIQDDz3qyrr5KCUWotbtTVbVg2SU30CRw%2Bfr7dgVOte3L9wIffk9HAlJINA7wi%2BwwqNPXaSZR%2FX8xh%2BiggOKHW11sWCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM0kpZ%2Ft%2FImH7M%2BR0pKtwDiKNW173kl0w94I4BFgiJQQouiBeOMkjpP7d%2BEP4hyX84LVaVzX7hXB3M2toRyOrl95lqlGZdaKNktI%2Bf%2FO6wh6jY%2Bvzwctr4kQzyEvMu4oqu2Itocz%2BECELEs4QA5xgBYqyWczW1EtqDxMNqe71IO6qPfyBrRvotjvSa6%2FJso5O%2BhNYDlUaYcKxVnFjbTp4mPFwQNgRwE22EPHlc2nxAes78uTIh3wM1Wzrnam%2FY3AT%2BJQAZcrYu2ra4Hem5C2R1ZYy%2BlKG%2FcvituOhaXAOnfPHisMamZ1U9YEPZFI92jXDrxkv8iVv28w6brPKAIpBLgzDgNDim5zm1UHCbPugAnyublM6PaH8cYDU4jrR5%2FAdPhv%2BzM7U3ZMm7nKAKLI5BmoLaZlXXlIYLMX%2B4P1nas8XL4quxyJVfgRPivGZoP2IERSu746iLXWpBzOKYE7ioJs8jbMcTj3jOmZiyJBGLEUt1Ya6XYkNQU6ZAeOlrVVknJvA826mENXz1Ww4vLpNaQFybNmmZCSCX%2FxHTrUtg5eDPBXCNKl7zxbuBhKLbZwQKbYd2%2FWA6UPM%2BqYAO8vRg4IpGIT68CUb3JHYzRS5JYBUU5eSAkFOQBBBx23niPiX417t1Hcw8SG6NAaEwufmWvQY6pgHZABd8JA4tVqc7aHWPx6h6UaGMDsPvJhqlE7Hd2KERga7l9ngqW4rYl76yPm%2FZ6HBGmc6xpq34u3vLqqijIGsKHksy3bMrNm%2Fv%2BkcayybCR7XLbVE1am%2F0YZ8O6PX7%2BnuUwBwKURQkoAf8w0jcAuYeB7ZLwgrX6DEpgQrpZSjvcEor6uuWqoPljg921oGh1K7hJzPxYJ1UQsrXaC61yUYcN0StVFbH&X-Amz-Signature=6582005101e12b64710823df3a2ce824143f4cf137436efecaf26fb57ef09be6&X-Amz-SignedHeaders=host&x-id=GetObject)
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


