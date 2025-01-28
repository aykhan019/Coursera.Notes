

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXD2VLNL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDYj7qBiOpyEhvHUSut7G%2FSF1kSQJOeoebrB%2BLJFTBnmAIgQlFBl867a%2FOnY%2BT%2FBmV5FOhDkR6tCW4dMGXvtqHKD2Eq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDLWIgGduKB4EXy1MXSrcAzlAUKeTwQK1d1iqnzGZcUMyNqxW7mhEFJqvXGTXKWrKBwOwTWo6%2FJPf1na2f2yX9kw81Dv6WBeH2rhAKGSZtF29i%2FHJy9GZ4Jy2TdEDCrP1RbcJywyyJFZp1NP7KTwPk1FmPe9L5B9353WJRsqsF1dpdwfAww8iRB6WuriF1qLGSeFTmoac18OXDfh8PWgE5VPDOadwc%2FDam6IoS5itlcC%2F0aHfoPLuTSdXpn26Qb%2FJH168fxrH8DVwIJAxP0OUia0JiIBFWaHCBQ9548e58F7d5PnKtFdsUO6Y63j0nvfHr1Fee7IrQqnf3LS1hrma2CRg7tcZZnYzteIuuMBBy9S%2BM6bXjc%2FShpTrizDyYpSnAUtOV0lYREXFCGAwrqX9V61qd5ufeLsQkGamVBAuE%2Bw8fla8Jfm3m6H4E32dctj0VlVkZuKIzq35DgdCp0Cjm%2Bqp7HRwCr36txkRNrruyhJzXA5MRpu3kFpBlpqjYfM4x8wZ7DZHIbC8hw7d6pUWsxn2%2F2NAHaaRE9Jpdz6i8s8jt6kNg8bOmi7B7ti8uD49rpkpfDNVWFzT0FAQUFZU0sPS8KKKDQRO2djRwuoKmzlaW4vjNyixWbdzX1I%2FD0imxQoHUUMzX6yVqUYVMLKU5bwGOqUBd%2B5jWyp7gEQ%2BFpAGOXLOuCa7R4SuuILa0Svp0pFvZwbxu9K0Azggvbucsn8oLfSSzh3l4qIT47mFPYEaS5XFdFHhWhTQ8NCTHidP%2BCRB04u%2B4N865kX4l6GSzJR%2BsH3pWkmNVNpfF%2FOMBMfYuw54Dn9dXWaUtPJnLfCkNsBuVQdocmzdbf8%2BIjqzP37%2FeUC6VT17wdRFN1AILW7%2F73tOiPE1GiFK&X-Amz-Signature=fdea3a8b9ca8349a2d7a00a44e14d5c3116f842b9502d930d7b94a97f941a761&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LSFMXY6%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIHtQx%2BEivhMhvUteZ3fEs1O2KnDt9jIB%2FeAgHQOIRaFsAiBo94e%2FJsdKlEQjsO%2FLuOY6m3xzUWpT8CIgCwJNBf%2FyKCr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMhls8C3dJKPNrclkEKtwDJSaUbtHn4NoXb3T4%2BBEdRCwrRluNS8JXp9dccpMXRENi6QVaKkyI9W3VF7UHqQSrmAX0o0Uy2a7DRE%2BP2TooF9fhuwsh7X9zm6bqt0i5uxa8QCnusiINkAMksSVze4KBq7SnSG7zOjE8XcNEdL5TQhNqoCRTxH2Dd6JSkftuNPQcaSh3Wf5ZgANilzK2Cho2PiBUOT7MFYx5xYVj2%2FH4sdddcVj%2FKQC950PBb7UIJFReLMAIToJuQsdvYJbQauZ0V0JblTtEOEj0Ev0jZucqDnKpG%2BvJebSj9H0QjriUoVEyC3SpJISk1lVLNpSc%2BQZjnamG4Gts9wNN9DN%2Fge3ONSvEq0hh469CmemPKM3OO0VsgXT3A8YwcZZcj%2BFih8cr%2BIBjrhW78csWSZnsQu%2FXNR5DgTIV%2FmRQQyaftXIYrr8ibHWLN7JuyZ08oP8dxerD151ZTj2rb2Zvs3Xr6JqmObXGcEj5RXXb6zJuuBn7u5lge21E4%2FfrTautC4KHCIUQTfJ9DjLXmckDfv0KcyWg3rTcoIdEw8uamiaGZ1m6dww2PkRJ%2BZ%2BWvEYKG6%2B96EVQe1vlkwsTOCt92QANu4QeLLxMiF%2BT1DHPrJrYM%2FGWiOz5tOVhJxVjMQfwInAw3JTlvAY6pgFUHqYSYQzfSXxneFfqGAk5gS0lz9xdZXNf7doS51Nst79DtqAFvAjlzX36hscdgsnEGnxDwzLVtNFI2BOYoTUDl3POPYDXiFAYcKAMyJ%2BQWR%2FdYc%2B4DEv2si0hp21DvxSGyFzy%2BfRGdVq1bGbqKVDwr%2FfG%2BagsRXKUlRAVu4RN2uKlCEHAqlZi3ybUxwNhRDsPph5ST7IkeQkXEE6pBkV%2BEtd0pnLS&X-Amz-Signature=cb00ef96eaaf3fa66dfa5eebfa0722365edd875dc41bb402100459222bd1ca10&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LSFMXY6%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIHtQx%2BEivhMhvUteZ3fEs1O2KnDt9jIB%2FeAgHQOIRaFsAiBo94e%2FJsdKlEQjsO%2FLuOY6m3xzUWpT8CIgCwJNBf%2FyKCr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMhls8C3dJKPNrclkEKtwDJSaUbtHn4NoXb3T4%2BBEdRCwrRluNS8JXp9dccpMXRENi6QVaKkyI9W3VF7UHqQSrmAX0o0Uy2a7DRE%2BP2TooF9fhuwsh7X9zm6bqt0i5uxa8QCnusiINkAMksSVze4KBq7SnSG7zOjE8XcNEdL5TQhNqoCRTxH2Dd6JSkftuNPQcaSh3Wf5ZgANilzK2Cho2PiBUOT7MFYx5xYVj2%2FH4sdddcVj%2FKQC950PBb7UIJFReLMAIToJuQsdvYJbQauZ0V0JblTtEOEj0Ev0jZucqDnKpG%2BvJebSj9H0QjriUoVEyC3SpJISk1lVLNpSc%2BQZjnamG4Gts9wNN9DN%2Fge3ONSvEq0hh469CmemPKM3OO0VsgXT3A8YwcZZcj%2BFih8cr%2BIBjrhW78csWSZnsQu%2FXNR5DgTIV%2FmRQQyaftXIYrr8ibHWLN7JuyZ08oP8dxerD151ZTj2rb2Zvs3Xr6JqmObXGcEj5RXXb6zJuuBn7u5lge21E4%2FfrTautC4KHCIUQTfJ9DjLXmckDfv0KcyWg3rTcoIdEw8uamiaGZ1m6dww2PkRJ%2BZ%2BWvEYKG6%2B96EVQe1vlkwsTOCt92QANu4QeLLxMiF%2BT1DHPrJrYM%2FGWiOz5tOVhJxVjMQfwInAw3JTlvAY6pgFUHqYSYQzfSXxneFfqGAk5gS0lz9xdZXNf7doS51Nst79DtqAFvAjlzX36hscdgsnEGnxDwzLVtNFI2BOYoTUDl3POPYDXiFAYcKAMyJ%2BQWR%2FdYc%2B4DEv2si0hp21DvxSGyFzy%2BfRGdVq1bGbqKVDwr%2FfG%2BagsRXKUlRAVu4RN2uKlCEHAqlZi3ybUxwNhRDsPph5ST7IkeQkXEE6pBkV%2BEtd0pnLS&X-Amz-Signature=76d1e224a5e9eec26c7800381592fe616f03b97ac0fa6b50027919d85732efab&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LSFMXY6%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIHtQx%2BEivhMhvUteZ3fEs1O2KnDt9jIB%2FeAgHQOIRaFsAiBo94e%2FJsdKlEQjsO%2FLuOY6m3xzUWpT8CIgCwJNBf%2FyKCr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMhls8C3dJKPNrclkEKtwDJSaUbtHn4NoXb3T4%2BBEdRCwrRluNS8JXp9dccpMXRENi6QVaKkyI9W3VF7UHqQSrmAX0o0Uy2a7DRE%2BP2TooF9fhuwsh7X9zm6bqt0i5uxa8QCnusiINkAMksSVze4KBq7SnSG7zOjE8XcNEdL5TQhNqoCRTxH2Dd6JSkftuNPQcaSh3Wf5ZgANilzK2Cho2PiBUOT7MFYx5xYVj2%2FH4sdddcVj%2FKQC950PBb7UIJFReLMAIToJuQsdvYJbQauZ0V0JblTtEOEj0Ev0jZucqDnKpG%2BvJebSj9H0QjriUoVEyC3SpJISk1lVLNpSc%2BQZjnamG4Gts9wNN9DN%2Fge3ONSvEq0hh469CmemPKM3OO0VsgXT3A8YwcZZcj%2BFih8cr%2BIBjrhW78csWSZnsQu%2FXNR5DgTIV%2FmRQQyaftXIYrr8ibHWLN7JuyZ08oP8dxerD151ZTj2rb2Zvs3Xr6JqmObXGcEj5RXXb6zJuuBn7u5lge21E4%2FfrTautC4KHCIUQTfJ9DjLXmckDfv0KcyWg3rTcoIdEw8uamiaGZ1m6dww2PkRJ%2BZ%2BWvEYKG6%2B96EVQe1vlkwsTOCt92QANu4QeLLxMiF%2BT1DHPrJrYM%2FGWiOz5tOVhJxVjMQfwInAw3JTlvAY6pgFUHqYSYQzfSXxneFfqGAk5gS0lz9xdZXNf7doS51Nst79DtqAFvAjlzX36hscdgsnEGnxDwzLVtNFI2BOYoTUDl3POPYDXiFAYcKAMyJ%2BQWR%2FdYc%2B4DEv2si0hp21DvxSGyFzy%2BfRGdVq1bGbqKVDwr%2FfG%2BagsRXKUlRAVu4RN2uKlCEHAqlZi3ybUxwNhRDsPph5ST7IkeQkXEE6pBkV%2BEtd0pnLS&X-Amz-Signature=2b4b02898fd95861a3f692937c556af3d80c4a679027d35b0249e3bf44b1ef3f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LSFMXY6%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIHtQx%2BEivhMhvUteZ3fEs1O2KnDt9jIB%2FeAgHQOIRaFsAiBo94e%2FJsdKlEQjsO%2FLuOY6m3xzUWpT8CIgCwJNBf%2FyKCr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMhls8C3dJKPNrclkEKtwDJSaUbtHn4NoXb3T4%2BBEdRCwrRluNS8JXp9dccpMXRENi6QVaKkyI9W3VF7UHqQSrmAX0o0Uy2a7DRE%2BP2TooF9fhuwsh7X9zm6bqt0i5uxa8QCnusiINkAMksSVze4KBq7SnSG7zOjE8XcNEdL5TQhNqoCRTxH2Dd6JSkftuNPQcaSh3Wf5ZgANilzK2Cho2PiBUOT7MFYx5xYVj2%2FH4sdddcVj%2FKQC950PBb7UIJFReLMAIToJuQsdvYJbQauZ0V0JblTtEOEj0Ev0jZucqDnKpG%2BvJebSj9H0QjriUoVEyC3SpJISk1lVLNpSc%2BQZjnamG4Gts9wNN9DN%2Fge3ONSvEq0hh469CmemPKM3OO0VsgXT3A8YwcZZcj%2BFih8cr%2BIBjrhW78csWSZnsQu%2FXNR5DgTIV%2FmRQQyaftXIYrr8ibHWLN7JuyZ08oP8dxerD151ZTj2rb2Zvs3Xr6JqmObXGcEj5RXXb6zJuuBn7u5lge21E4%2FfrTautC4KHCIUQTfJ9DjLXmckDfv0KcyWg3rTcoIdEw8uamiaGZ1m6dww2PkRJ%2BZ%2BWvEYKG6%2B96EVQe1vlkwsTOCt92QANu4QeLLxMiF%2BT1DHPrJrYM%2FGWiOz5tOVhJxVjMQfwInAw3JTlvAY6pgFUHqYSYQzfSXxneFfqGAk5gS0lz9xdZXNf7doS51Nst79DtqAFvAjlzX36hscdgsnEGnxDwzLVtNFI2BOYoTUDl3POPYDXiFAYcKAMyJ%2BQWR%2FdYc%2B4DEv2si0hp21DvxSGyFzy%2BfRGdVq1bGbqKVDwr%2FfG%2BagsRXKUlRAVu4RN2uKlCEHAqlZi3ybUxwNhRDsPph5ST7IkeQkXEE6pBkV%2BEtd0pnLS&X-Amz-Signature=6910bfcd49bd1581a36a01632814aa25e066e2ce2cbe27c89ee03f126f39ad93&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LSFMXY6%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIHtQx%2BEivhMhvUteZ3fEs1O2KnDt9jIB%2FeAgHQOIRaFsAiBo94e%2FJsdKlEQjsO%2FLuOY6m3xzUWpT8CIgCwJNBf%2FyKCr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMhls8C3dJKPNrclkEKtwDJSaUbtHn4NoXb3T4%2BBEdRCwrRluNS8JXp9dccpMXRENi6QVaKkyI9W3VF7UHqQSrmAX0o0Uy2a7DRE%2BP2TooF9fhuwsh7X9zm6bqt0i5uxa8QCnusiINkAMksSVze4KBq7SnSG7zOjE8XcNEdL5TQhNqoCRTxH2Dd6JSkftuNPQcaSh3Wf5ZgANilzK2Cho2PiBUOT7MFYx5xYVj2%2FH4sdddcVj%2FKQC950PBb7UIJFReLMAIToJuQsdvYJbQauZ0V0JblTtEOEj0Ev0jZucqDnKpG%2BvJebSj9H0QjriUoVEyC3SpJISk1lVLNpSc%2BQZjnamG4Gts9wNN9DN%2Fge3ONSvEq0hh469CmemPKM3OO0VsgXT3A8YwcZZcj%2BFih8cr%2BIBjrhW78csWSZnsQu%2FXNR5DgTIV%2FmRQQyaftXIYrr8ibHWLN7JuyZ08oP8dxerD151ZTj2rb2Zvs3Xr6JqmObXGcEj5RXXb6zJuuBn7u5lge21E4%2FfrTautC4KHCIUQTfJ9DjLXmckDfv0KcyWg3rTcoIdEw8uamiaGZ1m6dww2PkRJ%2BZ%2BWvEYKG6%2B96EVQe1vlkwsTOCt92QANu4QeLLxMiF%2BT1DHPrJrYM%2FGWiOz5tOVhJxVjMQfwInAw3JTlvAY6pgFUHqYSYQzfSXxneFfqGAk5gS0lz9xdZXNf7doS51Nst79DtqAFvAjlzX36hscdgsnEGnxDwzLVtNFI2BOYoTUDl3POPYDXiFAYcKAMyJ%2BQWR%2FdYc%2B4DEv2si0hp21DvxSGyFzy%2BfRGdVq1bGbqKVDwr%2FfG%2BagsRXKUlRAVu4RN2uKlCEHAqlZi3ybUxwNhRDsPph5ST7IkeQkXEE6pBkV%2BEtd0pnLS&X-Amz-Signature=bfbb8f47a910e5a1bff65e90b1b5fb0663c9d5d72560a776938aa85143dce267&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXD2VLNL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDYj7qBiOpyEhvHUSut7G%2FSF1kSQJOeoebrB%2BLJFTBnmAIgQlFBl867a%2FOnY%2BT%2FBmV5FOhDkR6tCW4dMGXvtqHKD2Eq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDLWIgGduKB4EXy1MXSrcAzlAUKeTwQK1d1iqnzGZcUMyNqxW7mhEFJqvXGTXKWrKBwOwTWo6%2FJPf1na2f2yX9kw81Dv6WBeH2rhAKGSZtF29i%2FHJy9GZ4Jy2TdEDCrP1RbcJywyyJFZp1NP7KTwPk1FmPe9L5B9353WJRsqsF1dpdwfAww8iRB6WuriF1qLGSeFTmoac18OXDfh8PWgE5VPDOadwc%2FDam6IoS5itlcC%2F0aHfoPLuTSdXpn26Qb%2FJH168fxrH8DVwIJAxP0OUia0JiIBFWaHCBQ9548e58F7d5PnKtFdsUO6Y63j0nvfHr1Fee7IrQqnf3LS1hrma2CRg7tcZZnYzteIuuMBBy9S%2BM6bXjc%2FShpTrizDyYpSnAUtOV0lYREXFCGAwrqX9V61qd5ufeLsQkGamVBAuE%2Bw8fla8Jfm3m6H4E32dctj0VlVkZuKIzq35DgdCp0Cjm%2Bqp7HRwCr36txkRNrruyhJzXA5MRpu3kFpBlpqjYfM4x8wZ7DZHIbC8hw7d6pUWsxn2%2F2NAHaaRE9Jpdz6i8s8jt6kNg8bOmi7B7ti8uD49rpkpfDNVWFzT0FAQUFZU0sPS8KKKDQRO2djRwuoKmzlaW4vjNyixWbdzX1I%2FD0imxQoHUUMzX6yVqUYVMLKU5bwGOqUBd%2B5jWyp7gEQ%2BFpAGOXLOuCa7R4SuuILa0Svp0pFvZwbxu9K0Azggvbucsn8oLfSSzh3l4qIT47mFPYEaS5XFdFHhWhTQ8NCTHidP%2BCRB04u%2B4N865kX4l6GSzJR%2BsH3pWkmNVNpfF%2FOMBMfYuw54Dn9dXWaUtPJnLfCkNsBuVQdocmzdbf8%2BIjqzP37%2FeUC6VT17wdRFN1AILW7%2F73tOiPE1GiFK&X-Amz-Signature=5f78968d94de2b0a1b0d06f771fb5014fe8b8f18213334f5227b256002b8cade&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXD2VLNL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDYj7qBiOpyEhvHUSut7G%2FSF1kSQJOeoebrB%2BLJFTBnmAIgQlFBl867a%2FOnY%2BT%2FBmV5FOhDkR6tCW4dMGXvtqHKD2Eq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDLWIgGduKB4EXy1MXSrcAzlAUKeTwQK1d1iqnzGZcUMyNqxW7mhEFJqvXGTXKWrKBwOwTWo6%2FJPf1na2f2yX9kw81Dv6WBeH2rhAKGSZtF29i%2FHJy9GZ4Jy2TdEDCrP1RbcJywyyJFZp1NP7KTwPk1FmPe9L5B9353WJRsqsF1dpdwfAww8iRB6WuriF1qLGSeFTmoac18OXDfh8PWgE5VPDOadwc%2FDam6IoS5itlcC%2F0aHfoPLuTSdXpn26Qb%2FJH168fxrH8DVwIJAxP0OUia0JiIBFWaHCBQ9548e58F7d5PnKtFdsUO6Y63j0nvfHr1Fee7IrQqnf3LS1hrma2CRg7tcZZnYzteIuuMBBy9S%2BM6bXjc%2FShpTrizDyYpSnAUtOV0lYREXFCGAwrqX9V61qd5ufeLsQkGamVBAuE%2Bw8fla8Jfm3m6H4E32dctj0VlVkZuKIzq35DgdCp0Cjm%2Bqp7HRwCr36txkRNrruyhJzXA5MRpu3kFpBlpqjYfM4x8wZ7DZHIbC8hw7d6pUWsxn2%2F2NAHaaRE9Jpdz6i8s8jt6kNg8bOmi7B7ti8uD49rpkpfDNVWFzT0FAQUFZU0sPS8KKKDQRO2djRwuoKmzlaW4vjNyixWbdzX1I%2FD0imxQoHUUMzX6yVqUYVMLKU5bwGOqUBd%2B5jWyp7gEQ%2BFpAGOXLOuCa7R4SuuILa0Svp0pFvZwbxu9K0Azggvbucsn8oLfSSzh3l4qIT47mFPYEaS5XFdFHhWhTQ8NCTHidP%2BCRB04u%2B4N865kX4l6GSzJR%2BsH3pWkmNVNpfF%2FOMBMfYuw54Dn9dXWaUtPJnLfCkNsBuVQdocmzdbf8%2BIjqzP37%2FeUC6VT17wdRFN1AILW7%2F73tOiPE1GiFK&X-Amz-Signature=195258ea748610cfb1c31f03942d4e756aaf8263f89bff22fb989f1047c8c5a0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXD2VLNL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDYj7qBiOpyEhvHUSut7G%2FSF1kSQJOeoebrB%2BLJFTBnmAIgQlFBl867a%2FOnY%2BT%2FBmV5FOhDkR6tCW4dMGXvtqHKD2Eq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDLWIgGduKB4EXy1MXSrcAzlAUKeTwQK1d1iqnzGZcUMyNqxW7mhEFJqvXGTXKWrKBwOwTWo6%2FJPf1na2f2yX9kw81Dv6WBeH2rhAKGSZtF29i%2FHJy9GZ4Jy2TdEDCrP1RbcJywyyJFZp1NP7KTwPk1FmPe9L5B9353WJRsqsF1dpdwfAww8iRB6WuriF1qLGSeFTmoac18OXDfh8PWgE5VPDOadwc%2FDam6IoS5itlcC%2F0aHfoPLuTSdXpn26Qb%2FJH168fxrH8DVwIJAxP0OUia0JiIBFWaHCBQ9548e58F7d5PnKtFdsUO6Y63j0nvfHr1Fee7IrQqnf3LS1hrma2CRg7tcZZnYzteIuuMBBy9S%2BM6bXjc%2FShpTrizDyYpSnAUtOV0lYREXFCGAwrqX9V61qd5ufeLsQkGamVBAuE%2Bw8fla8Jfm3m6H4E32dctj0VlVkZuKIzq35DgdCp0Cjm%2Bqp7HRwCr36txkRNrruyhJzXA5MRpu3kFpBlpqjYfM4x8wZ7DZHIbC8hw7d6pUWsxn2%2F2NAHaaRE9Jpdz6i8s8jt6kNg8bOmi7B7ti8uD49rpkpfDNVWFzT0FAQUFZU0sPS8KKKDQRO2djRwuoKmzlaW4vjNyixWbdzX1I%2FD0imxQoHUUMzX6yVqUYVMLKU5bwGOqUBd%2B5jWyp7gEQ%2BFpAGOXLOuCa7R4SuuILa0Svp0pFvZwbxu9K0Azggvbucsn8oLfSSzh3l4qIT47mFPYEaS5XFdFHhWhTQ8NCTHidP%2BCRB04u%2B4N865kX4l6GSzJR%2BsH3pWkmNVNpfF%2FOMBMfYuw54Dn9dXWaUtPJnLfCkNsBuVQdocmzdbf8%2BIjqzP37%2FeUC6VT17wdRFN1AILW7%2F73tOiPE1GiFK&X-Amz-Signature=2435f82e36c15941e905a487a4e079028fad0a9fa36c030d0a2e1c2d5836ebb0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXD2VLNL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDYj7qBiOpyEhvHUSut7G%2FSF1kSQJOeoebrB%2BLJFTBnmAIgQlFBl867a%2FOnY%2BT%2FBmV5FOhDkR6tCW4dMGXvtqHKD2Eq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDLWIgGduKB4EXy1MXSrcAzlAUKeTwQK1d1iqnzGZcUMyNqxW7mhEFJqvXGTXKWrKBwOwTWo6%2FJPf1na2f2yX9kw81Dv6WBeH2rhAKGSZtF29i%2FHJy9GZ4Jy2TdEDCrP1RbcJywyyJFZp1NP7KTwPk1FmPe9L5B9353WJRsqsF1dpdwfAww8iRB6WuriF1qLGSeFTmoac18OXDfh8PWgE5VPDOadwc%2FDam6IoS5itlcC%2F0aHfoPLuTSdXpn26Qb%2FJH168fxrH8DVwIJAxP0OUia0JiIBFWaHCBQ9548e58F7d5PnKtFdsUO6Y63j0nvfHr1Fee7IrQqnf3LS1hrma2CRg7tcZZnYzteIuuMBBy9S%2BM6bXjc%2FShpTrizDyYpSnAUtOV0lYREXFCGAwrqX9V61qd5ufeLsQkGamVBAuE%2Bw8fla8Jfm3m6H4E32dctj0VlVkZuKIzq35DgdCp0Cjm%2Bqp7HRwCr36txkRNrruyhJzXA5MRpu3kFpBlpqjYfM4x8wZ7DZHIbC8hw7d6pUWsxn2%2F2NAHaaRE9Jpdz6i8s8jt6kNg8bOmi7B7ti8uD49rpkpfDNVWFzT0FAQUFZU0sPS8KKKDQRO2djRwuoKmzlaW4vjNyixWbdzX1I%2FD0imxQoHUUMzX6yVqUYVMLKU5bwGOqUBd%2B5jWyp7gEQ%2BFpAGOXLOuCa7R4SuuILa0Svp0pFvZwbxu9K0Azggvbucsn8oLfSSzh3l4qIT47mFPYEaS5XFdFHhWhTQ8NCTHidP%2BCRB04u%2B4N865kX4l6GSzJR%2BsH3pWkmNVNpfF%2FOMBMfYuw54Dn9dXWaUtPJnLfCkNsBuVQdocmzdbf8%2BIjqzP37%2FeUC6VT17wdRFN1AILW7%2F73tOiPE1GiFK&X-Amz-Signature=4b2004077e356147f486fe907ff6371da935ce823f2bbf70271508174656ee0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXD2VLNL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDYj7qBiOpyEhvHUSut7G%2FSF1kSQJOeoebrB%2BLJFTBnmAIgQlFBl867a%2FOnY%2BT%2FBmV5FOhDkR6tCW4dMGXvtqHKD2Eq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDLWIgGduKB4EXy1MXSrcAzlAUKeTwQK1d1iqnzGZcUMyNqxW7mhEFJqvXGTXKWrKBwOwTWo6%2FJPf1na2f2yX9kw81Dv6WBeH2rhAKGSZtF29i%2FHJy9GZ4Jy2TdEDCrP1RbcJywyyJFZp1NP7KTwPk1FmPe9L5B9353WJRsqsF1dpdwfAww8iRB6WuriF1qLGSeFTmoac18OXDfh8PWgE5VPDOadwc%2FDam6IoS5itlcC%2F0aHfoPLuTSdXpn26Qb%2FJH168fxrH8DVwIJAxP0OUia0JiIBFWaHCBQ9548e58F7d5PnKtFdsUO6Y63j0nvfHr1Fee7IrQqnf3LS1hrma2CRg7tcZZnYzteIuuMBBy9S%2BM6bXjc%2FShpTrizDyYpSnAUtOV0lYREXFCGAwrqX9V61qd5ufeLsQkGamVBAuE%2Bw8fla8Jfm3m6H4E32dctj0VlVkZuKIzq35DgdCp0Cjm%2Bqp7HRwCr36txkRNrruyhJzXA5MRpu3kFpBlpqjYfM4x8wZ7DZHIbC8hw7d6pUWsxn2%2F2NAHaaRE9Jpdz6i8s8jt6kNg8bOmi7B7ti8uD49rpkpfDNVWFzT0FAQUFZU0sPS8KKKDQRO2djRwuoKmzlaW4vjNyixWbdzX1I%2FD0imxQoHUUMzX6yVqUYVMLKU5bwGOqUBd%2B5jWyp7gEQ%2BFpAGOXLOuCa7R4SuuILa0Svp0pFvZwbxu9K0Azggvbucsn8oLfSSzh3l4qIT47mFPYEaS5XFdFHhWhTQ8NCTHidP%2BCRB04u%2B4N865kX4l6GSzJR%2BsH3pWkmNVNpfF%2FOMBMfYuw54Dn9dXWaUtPJnLfCkNsBuVQdocmzdbf8%2BIjqzP37%2FeUC6VT17wdRFN1AILW7%2F73tOiPE1GiFK&X-Amz-Signature=aab148dcfa196327407015cf56e4005cf502ed18c294b4c317f3a6bf76ae7df4&X-Amz-SignedHeaders=host&x-id=GetObject)
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


