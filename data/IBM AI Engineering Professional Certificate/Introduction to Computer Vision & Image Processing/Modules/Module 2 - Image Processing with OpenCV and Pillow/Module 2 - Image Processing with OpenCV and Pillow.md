

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YLMLP6M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIANuge%2By0FYScGCkmJVV7fOwTozMhYG0%2BfP2xq0e77s3AiEA0byRdmCAHu3VwBd3c31odeOWZfFPzmCAIO%2BcsCKZogAq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDCV0iMHO5YQBxybiGyrcA8PAl%2FapnEMm%2B1ecTPFHFPhy0FaT5QS660y8CzSh%2Bnn%2FymcVS5Qj2WXepS3Qvy6lgVLtU2ypEynwMhwg7Uq%2FBOUiOFptf3OmGLka7hSGt436zGm12a2YN4EDQwIDIHntsRpjojz9%2BamDKrYLlCk%2BJ4xMoP99ddWubbYfnayeFxNmWTdJS6QNVc2sv2LbO2uTmeBkIQb90nTvBxvSLh5cU8ZzM1p29kYLDuh5jTxdJvhnZOFaQO%2BU%2BHSdzt0AvyyCMiX8HB9cRGhXijyjCXkmqQXA0VXQ3%2FWK2CfvWQUwniJGelUaWuMMNa5Zy78Rg7L74J5nwuhO8n18kkCRD2ZuQku%2BdHXXbom5oyt6zWpFRRLxHTLYv6T7Jh4O%2FVorq29OhPLIKm4ZU86lGx5vQ1dX427mXNiYLKaBhJHrG1C1y41qPprhVbp4uQ%2FvnxS2ECRsLIy4ekbQ8OzFKfqBht%2FNc7ISky7xkRWmSOF4aUiYmu2OH7WY05sDf4a2KXPHxmKUsilFJGQT%2BL6LcElo%2Fx8fbVou7pJKU0UCcZ6X7PuSzMfa6dROti%2Fk0kNRwJl%2FlvkkAsoM2Rle8gVPx0jtOmnV6I0KAZf1QjWj9eBvKHM4FNBQZZVf898PO5sXQgtsMPHMir0GOqUBFTOBgNJGKawAlwXCDEoToisVh9yDTC23ylZDn0d1Cx9%2FOxrt7oQqpkWkNyHDSw3H94wfTjHrheOyOOUls4LCyIFmmjcwxMpvS%2Fwuhnso3FlnZSiLuiN5fvp11oX9E2aLoamHKyoePh06EThz9wo67AUoi6oXIaTR4bN09uApWN9LSP3a%2BwNnU8NRThCmu5FYKARz0SNIcz8HeEISn0eXYVabDvlF&X-Amz-Signature=7e5f0790922e1964ea5a839ca368d01967168ac38c22eb4dc3a0236a23d3e49b&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDCZP2S6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIFMj6EKopCl74TXPLU5A97Y4XQUjj5vCQ%2BjA0bNwjOgwAiA1gghHERy3nHA0WIcArt3mZqC0xHtBWbpSX7e9lNlPcCr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMZF%2FZuGaT4s1NsxJWKtwDoiYp8mUyoN5zqAMaEKA8BoeJOe5aae7gd6h0IRBVt14xRbdswSZVeF6xlDHLWZj4dSxQ%2BMdgXQxlnc6R6LI%2BjWkNLAy7GlTx%2BSXELZWZRZMEm3aFVDJfOmrk%2F5eADkjmKkgbbC8DpM5vOwweWTjg178uT7oqfPQ5xDSAYHG8UGQg2tVTpOtAqqXpguLmBLv%2B2UdVIj2wiWZNTmmzknxkCsZlrd%2B8vryPzBk9REag9NXpilsnbO91UnmiMIzTg0TnvCsBqC32j54VsH35r1mty%2BBOXgXl9%2BsASv%2BkAlEzC9YOKbzxg0peuqgl8ylK27XXWkCS2qgX%2F1U1wlSMsVtO5DXskgAW%2FY5VyHtftbwdgebQBjYohEwylidpY1BYR%2FhC3j6sIM%2FXaOGlMjAHfLyns%2FGqOiiCUa87zvHUzUMW46tDjS4VyplWB5FWzRGSc%2FaQxzzwlchTT4HelxJB44aYxLFkavL2Tx1iDTruy3jz9I10wEU21Wi%2FhhmGV73T94HmJfp7Ybxxx0JZfFy%2B3wj%2BSDxNe7pUyREYt%2F1K5jJaY0JCZ%2BaMAs9Indgpv%2Bc%2BE5Ch7yogy4%2BIV4UIGt57%2BPs3o%2BVKi4oWGo4n8d9Ts%2FwDuYA5%2F%2FJ9PUsrN5Qgy2Yw2c2KvQY6pgEm7p8FoFp6MIeNS3%2Fqqmo762tRkv8al3AdYb%2FSUv6iBA8NqYDh1sZI2ZQ0bUsP6sFtK1zKkv%2FKPcrSuKt1fwWQg%2F3Ebb6Kyv2wXXl4W6aKbbP9tm22DoWnYyPrmkoIXPN3XxkRgfVxzmTf4G3WVaLVkxVCRg%2FhvxZokIhFYf07YZi589CFAdvAy0yrVzsXMGqsWZaZysNQnXgJbtb2eoje7VQ1XiLO&X-Amz-Signature=2392002592abc3abafaa330fbcc1b9836c7f92aa51df7bb63e9677cf051497ff&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDCZP2S6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIFMj6EKopCl74TXPLU5A97Y4XQUjj5vCQ%2BjA0bNwjOgwAiA1gghHERy3nHA0WIcArt3mZqC0xHtBWbpSX7e9lNlPcCr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMZF%2FZuGaT4s1NsxJWKtwDoiYp8mUyoN5zqAMaEKA8BoeJOe5aae7gd6h0IRBVt14xRbdswSZVeF6xlDHLWZj4dSxQ%2BMdgXQxlnc6R6LI%2BjWkNLAy7GlTx%2BSXELZWZRZMEm3aFVDJfOmrk%2F5eADkjmKkgbbC8DpM5vOwweWTjg178uT7oqfPQ5xDSAYHG8UGQg2tVTpOtAqqXpguLmBLv%2B2UdVIj2wiWZNTmmzknxkCsZlrd%2B8vryPzBk9REag9NXpilsnbO91UnmiMIzTg0TnvCsBqC32j54VsH35r1mty%2BBOXgXl9%2BsASv%2BkAlEzC9YOKbzxg0peuqgl8ylK27XXWkCS2qgX%2F1U1wlSMsVtO5DXskgAW%2FY5VyHtftbwdgebQBjYohEwylidpY1BYR%2FhC3j6sIM%2FXaOGlMjAHfLyns%2FGqOiiCUa87zvHUzUMW46tDjS4VyplWB5FWzRGSc%2FaQxzzwlchTT4HelxJB44aYxLFkavL2Tx1iDTruy3jz9I10wEU21Wi%2FhhmGV73T94HmJfp7Ybxxx0JZfFy%2B3wj%2BSDxNe7pUyREYt%2F1K5jJaY0JCZ%2BaMAs9Indgpv%2Bc%2BE5Ch7yogy4%2BIV4UIGt57%2BPs3o%2BVKi4oWGo4n8d9Ts%2FwDuYA5%2F%2FJ9PUsrN5Qgy2Yw2c2KvQY6pgEm7p8FoFp6MIeNS3%2Fqqmo762tRkv8al3AdYb%2FSUv6iBA8NqYDh1sZI2ZQ0bUsP6sFtK1zKkv%2FKPcrSuKt1fwWQg%2F3Ebb6Kyv2wXXl4W6aKbbP9tm22DoWnYyPrmkoIXPN3XxkRgfVxzmTf4G3WVaLVkxVCRg%2FhvxZokIhFYf07YZi589CFAdvAy0yrVzsXMGqsWZaZysNQnXgJbtb2eoje7VQ1XiLO&X-Amz-Signature=e17caefa6628c3d9be3faac02504341c212ca656476f9a3374181d519430d4f8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDCZP2S6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIFMj6EKopCl74TXPLU5A97Y4XQUjj5vCQ%2BjA0bNwjOgwAiA1gghHERy3nHA0WIcArt3mZqC0xHtBWbpSX7e9lNlPcCr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMZF%2FZuGaT4s1NsxJWKtwDoiYp8mUyoN5zqAMaEKA8BoeJOe5aae7gd6h0IRBVt14xRbdswSZVeF6xlDHLWZj4dSxQ%2BMdgXQxlnc6R6LI%2BjWkNLAy7GlTx%2BSXELZWZRZMEm3aFVDJfOmrk%2F5eADkjmKkgbbC8DpM5vOwweWTjg178uT7oqfPQ5xDSAYHG8UGQg2tVTpOtAqqXpguLmBLv%2B2UdVIj2wiWZNTmmzknxkCsZlrd%2B8vryPzBk9REag9NXpilsnbO91UnmiMIzTg0TnvCsBqC32j54VsH35r1mty%2BBOXgXl9%2BsASv%2BkAlEzC9YOKbzxg0peuqgl8ylK27XXWkCS2qgX%2F1U1wlSMsVtO5DXskgAW%2FY5VyHtftbwdgebQBjYohEwylidpY1BYR%2FhC3j6sIM%2FXaOGlMjAHfLyns%2FGqOiiCUa87zvHUzUMW46tDjS4VyplWB5FWzRGSc%2FaQxzzwlchTT4HelxJB44aYxLFkavL2Tx1iDTruy3jz9I10wEU21Wi%2FhhmGV73T94HmJfp7Ybxxx0JZfFy%2B3wj%2BSDxNe7pUyREYt%2F1K5jJaY0JCZ%2BaMAs9Indgpv%2Bc%2BE5Ch7yogy4%2BIV4UIGt57%2BPs3o%2BVKi4oWGo4n8d9Ts%2FwDuYA5%2F%2FJ9PUsrN5Qgy2Yw2c2KvQY6pgEm7p8FoFp6MIeNS3%2Fqqmo762tRkv8al3AdYb%2FSUv6iBA8NqYDh1sZI2ZQ0bUsP6sFtK1zKkv%2FKPcrSuKt1fwWQg%2F3Ebb6Kyv2wXXl4W6aKbbP9tm22DoWnYyPrmkoIXPN3XxkRgfVxzmTf4G3WVaLVkxVCRg%2FhvxZokIhFYf07YZi589CFAdvAy0yrVzsXMGqsWZaZysNQnXgJbtb2eoje7VQ1XiLO&X-Amz-Signature=7eaf0f418e84aeca69201e5bda72d35d4a12351d17b48f4dfb038367f6e7e4bf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDCZP2S6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIFMj6EKopCl74TXPLU5A97Y4XQUjj5vCQ%2BjA0bNwjOgwAiA1gghHERy3nHA0WIcArt3mZqC0xHtBWbpSX7e9lNlPcCr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMZF%2FZuGaT4s1NsxJWKtwDoiYp8mUyoN5zqAMaEKA8BoeJOe5aae7gd6h0IRBVt14xRbdswSZVeF6xlDHLWZj4dSxQ%2BMdgXQxlnc6R6LI%2BjWkNLAy7GlTx%2BSXELZWZRZMEm3aFVDJfOmrk%2F5eADkjmKkgbbC8DpM5vOwweWTjg178uT7oqfPQ5xDSAYHG8UGQg2tVTpOtAqqXpguLmBLv%2B2UdVIj2wiWZNTmmzknxkCsZlrd%2B8vryPzBk9REag9NXpilsnbO91UnmiMIzTg0TnvCsBqC32j54VsH35r1mty%2BBOXgXl9%2BsASv%2BkAlEzC9YOKbzxg0peuqgl8ylK27XXWkCS2qgX%2F1U1wlSMsVtO5DXskgAW%2FY5VyHtftbwdgebQBjYohEwylidpY1BYR%2FhC3j6sIM%2FXaOGlMjAHfLyns%2FGqOiiCUa87zvHUzUMW46tDjS4VyplWB5FWzRGSc%2FaQxzzwlchTT4HelxJB44aYxLFkavL2Tx1iDTruy3jz9I10wEU21Wi%2FhhmGV73T94HmJfp7Ybxxx0JZfFy%2B3wj%2BSDxNe7pUyREYt%2F1K5jJaY0JCZ%2BaMAs9Indgpv%2Bc%2BE5Ch7yogy4%2BIV4UIGt57%2BPs3o%2BVKi4oWGo4n8d9Ts%2FwDuYA5%2F%2FJ9PUsrN5Qgy2Yw2c2KvQY6pgEm7p8FoFp6MIeNS3%2Fqqmo762tRkv8al3AdYb%2FSUv6iBA8NqYDh1sZI2ZQ0bUsP6sFtK1zKkv%2FKPcrSuKt1fwWQg%2F3Ebb6Kyv2wXXl4W6aKbbP9tm22DoWnYyPrmkoIXPN3XxkRgfVxzmTf4G3WVaLVkxVCRg%2FhvxZokIhFYf07YZi589CFAdvAy0yrVzsXMGqsWZaZysNQnXgJbtb2eoje7VQ1XiLO&X-Amz-Signature=5513c6b7695384eb00cf2a986c1ce141bcba5f8158ca12544a8163cc36cb4f82&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDCZP2S6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIFMj6EKopCl74TXPLU5A97Y4XQUjj5vCQ%2BjA0bNwjOgwAiA1gghHERy3nHA0WIcArt3mZqC0xHtBWbpSX7e9lNlPcCr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMZF%2FZuGaT4s1NsxJWKtwDoiYp8mUyoN5zqAMaEKA8BoeJOe5aae7gd6h0IRBVt14xRbdswSZVeF6xlDHLWZj4dSxQ%2BMdgXQxlnc6R6LI%2BjWkNLAy7GlTx%2BSXELZWZRZMEm3aFVDJfOmrk%2F5eADkjmKkgbbC8DpM5vOwweWTjg178uT7oqfPQ5xDSAYHG8UGQg2tVTpOtAqqXpguLmBLv%2B2UdVIj2wiWZNTmmzknxkCsZlrd%2B8vryPzBk9REag9NXpilsnbO91UnmiMIzTg0TnvCsBqC32j54VsH35r1mty%2BBOXgXl9%2BsASv%2BkAlEzC9YOKbzxg0peuqgl8ylK27XXWkCS2qgX%2F1U1wlSMsVtO5DXskgAW%2FY5VyHtftbwdgebQBjYohEwylidpY1BYR%2FhC3j6sIM%2FXaOGlMjAHfLyns%2FGqOiiCUa87zvHUzUMW46tDjS4VyplWB5FWzRGSc%2FaQxzzwlchTT4HelxJB44aYxLFkavL2Tx1iDTruy3jz9I10wEU21Wi%2FhhmGV73T94HmJfp7Ybxxx0JZfFy%2B3wj%2BSDxNe7pUyREYt%2F1K5jJaY0JCZ%2BaMAs9Indgpv%2Bc%2BE5Ch7yogy4%2BIV4UIGt57%2BPs3o%2BVKi4oWGo4n8d9Ts%2FwDuYA5%2F%2FJ9PUsrN5Qgy2Yw2c2KvQY6pgEm7p8FoFp6MIeNS3%2Fqqmo762tRkv8al3AdYb%2FSUv6iBA8NqYDh1sZI2ZQ0bUsP6sFtK1zKkv%2FKPcrSuKt1fwWQg%2F3Ebb6Kyv2wXXl4W6aKbbP9tm22DoWnYyPrmkoIXPN3XxkRgfVxzmTf4G3WVaLVkxVCRg%2FhvxZokIhFYf07YZi589CFAdvAy0yrVzsXMGqsWZaZysNQnXgJbtb2eoje7VQ1XiLO&X-Amz-Signature=42664ebea673cf3740adeec9b1e481d3ef1c258df86c7dcc1ece4cc19738f43d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YLMLP6M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIANuge%2By0FYScGCkmJVV7fOwTozMhYG0%2BfP2xq0e77s3AiEA0byRdmCAHu3VwBd3c31odeOWZfFPzmCAIO%2BcsCKZogAq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDCV0iMHO5YQBxybiGyrcA8PAl%2FapnEMm%2B1ecTPFHFPhy0FaT5QS660y8CzSh%2Bnn%2FymcVS5Qj2WXepS3Qvy6lgVLtU2ypEynwMhwg7Uq%2FBOUiOFptf3OmGLka7hSGt436zGm12a2YN4EDQwIDIHntsRpjojz9%2BamDKrYLlCk%2BJ4xMoP99ddWubbYfnayeFxNmWTdJS6QNVc2sv2LbO2uTmeBkIQb90nTvBxvSLh5cU8ZzM1p29kYLDuh5jTxdJvhnZOFaQO%2BU%2BHSdzt0AvyyCMiX8HB9cRGhXijyjCXkmqQXA0VXQ3%2FWK2CfvWQUwniJGelUaWuMMNa5Zy78Rg7L74J5nwuhO8n18kkCRD2ZuQku%2BdHXXbom5oyt6zWpFRRLxHTLYv6T7Jh4O%2FVorq29OhPLIKm4ZU86lGx5vQ1dX427mXNiYLKaBhJHrG1C1y41qPprhVbp4uQ%2FvnxS2ECRsLIy4ekbQ8OzFKfqBht%2FNc7ISky7xkRWmSOF4aUiYmu2OH7WY05sDf4a2KXPHxmKUsilFJGQT%2BL6LcElo%2Fx8fbVou7pJKU0UCcZ6X7PuSzMfa6dROti%2Fk0kNRwJl%2FlvkkAsoM2Rle8gVPx0jtOmnV6I0KAZf1QjWj9eBvKHM4FNBQZZVf898PO5sXQgtsMPHMir0GOqUBFTOBgNJGKawAlwXCDEoToisVh9yDTC23ylZDn0d1Cx9%2FOxrt7oQqpkWkNyHDSw3H94wfTjHrheOyOOUls4LCyIFmmjcwxMpvS%2Fwuhnso3FlnZSiLuiN5fvp11oX9E2aLoamHKyoePh06EThz9wo67AUoi6oXIaTR4bN09uApWN9LSP3a%2BwNnU8NRThCmu5FYKARz0SNIcz8HeEISn0eXYVabDvlF&X-Amz-Signature=4e85a2c53ad98e6ad38a40133e8441bab02fc78859e95e951e783d4ee52852ca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YLMLP6M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIANuge%2By0FYScGCkmJVV7fOwTozMhYG0%2BfP2xq0e77s3AiEA0byRdmCAHu3VwBd3c31odeOWZfFPzmCAIO%2BcsCKZogAq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDCV0iMHO5YQBxybiGyrcA8PAl%2FapnEMm%2B1ecTPFHFPhy0FaT5QS660y8CzSh%2Bnn%2FymcVS5Qj2WXepS3Qvy6lgVLtU2ypEynwMhwg7Uq%2FBOUiOFptf3OmGLka7hSGt436zGm12a2YN4EDQwIDIHntsRpjojz9%2BamDKrYLlCk%2BJ4xMoP99ddWubbYfnayeFxNmWTdJS6QNVc2sv2LbO2uTmeBkIQb90nTvBxvSLh5cU8ZzM1p29kYLDuh5jTxdJvhnZOFaQO%2BU%2BHSdzt0AvyyCMiX8HB9cRGhXijyjCXkmqQXA0VXQ3%2FWK2CfvWQUwniJGelUaWuMMNa5Zy78Rg7L74J5nwuhO8n18kkCRD2ZuQku%2BdHXXbom5oyt6zWpFRRLxHTLYv6T7Jh4O%2FVorq29OhPLIKm4ZU86lGx5vQ1dX427mXNiYLKaBhJHrG1C1y41qPprhVbp4uQ%2FvnxS2ECRsLIy4ekbQ8OzFKfqBht%2FNc7ISky7xkRWmSOF4aUiYmu2OH7WY05sDf4a2KXPHxmKUsilFJGQT%2BL6LcElo%2Fx8fbVou7pJKU0UCcZ6X7PuSzMfa6dROti%2Fk0kNRwJl%2FlvkkAsoM2Rle8gVPx0jtOmnV6I0KAZf1QjWj9eBvKHM4FNBQZZVf898PO5sXQgtsMPHMir0GOqUBFTOBgNJGKawAlwXCDEoToisVh9yDTC23ylZDn0d1Cx9%2FOxrt7oQqpkWkNyHDSw3H94wfTjHrheOyOOUls4LCyIFmmjcwxMpvS%2Fwuhnso3FlnZSiLuiN5fvp11oX9E2aLoamHKyoePh06EThz9wo67AUoi6oXIaTR4bN09uApWN9LSP3a%2BwNnU8NRThCmu5FYKARz0SNIcz8HeEISn0eXYVabDvlF&X-Amz-Signature=b20a737c60b9d488f7566bcb58d2a5d6e1137dcaf82d8c54fd4e35660e13cac9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YLMLP6M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIANuge%2By0FYScGCkmJVV7fOwTozMhYG0%2BfP2xq0e77s3AiEA0byRdmCAHu3VwBd3c31odeOWZfFPzmCAIO%2BcsCKZogAq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDCV0iMHO5YQBxybiGyrcA8PAl%2FapnEMm%2B1ecTPFHFPhy0FaT5QS660y8CzSh%2Bnn%2FymcVS5Qj2WXepS3Qvy6lgVLtU2ypEynwMhwg7Uq%2FBOUiOFptf3OmGLka7hSGt436zGm12a2YN4EDQwIDIHntsRpjojz9%2BamDKrYLlCk%2BJ4xMoP99ddWubbYfnayeFxNmWTdJS6QNVc2sv2LbO2uTmeBkIQb90nTvBxvSLh5cU8ZzM1p29kYLDuh5jTxdJvhnZOFaQO%2BU%2BHSdzt0AvyyCMiX8HB9cRGhXijyjCXkmqQXA0VXQ3%2FWK2CfvWQUwniJGelUaWuMMNa5Zy78Rg7L74J5nwuhO8n18kkCRD2ZuQku%2BdHXXbom5oyt6zWpFRRLxHTLYv6T7Jh4O%2FVorq29OhPLIKm4ZU86lGx5vQ1dX427mXNiYLKaBhJHrG1C1y41qPprhVbp4uQ%2FvnxS2ECRsLIy4ekbQ8OzFKfqBht%2FNc7ISky7xkRWmSOF4aUiYmu2OH7WY05sDf4a2KXPHxmKUsilFJGQT%2BL6LcElo%2Fx8fbVou7pJKU0UCcZ6X7PuSzMfa6dROti%2Fk0kNRwJl%2FlvkkAsoM2Rle8gVPx0jtOmnV6I0KAZf1QjWj9eBvKHM4FNBQZZVf898PO5sXQgtsMPHMir0GOqUBFTOBgNJGKawAlwXCDEoToisVh9yDTC23ylZDn0d1Cx9%2FOxrt7oQqpkWkNyHDSw3H94wfTjHrheOyOOUls4LCyIFmmjcwxMpvS%2Fwuhnso3FlnZSiLuiN5fvp11oX9E2aLoamHKyoePh06EThz9wo67AUoi6oXIaTR4bN09uApWN9LSP3a%2BwNnU8NRThCmu5FYKARz0SNIcz8HeEISn0eXYVabDvlF&X-Amz-Signature=dbf31aed380779b06544622b69d6da542560293e7d3180272b8a63f699cc9917&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YLMLP6M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIANuge%2By0FYScGCkmJVV7fOwTozMhYG0%2BfP2xq0e77s3AiEA0byRdmCAHu3VwBd3c31odeOWZfFPzmCAIO%2BcsCKZogAq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDCV0iMHO5YQBxybiGyrcA8PAl%2FapnEMm%2B1ecTPFHFPhy0FaT5QS660y8CzSh%2Bnn%2FymcVS5Qj2WXepS3Qvy6lgVLtU2ypEynwMhwg7Uq%2FBOUiOFptf3OmGLka7hSGt436zGm12a2YN4EDQwIDIHntsRpjojz9%2BamDKrYLlCk%2BJ4xMoP99ddWubbYfnayeFxNmWTdJS6QNVc2sv2LbO2uTmeBkIQb90nTvBxvSLh5cU8ZzM1p29kYLDuh5jTxdJvhnZOFaQO%2BU%2BHSdzt0AvyyCMiX8HB9cRGhXijyjCXkmqQXA0VXQ3%2FWK2CfvWQUwniJGelUaWuMMNa5Zy78Rg7L74J5nwuhO8n18kkCRD2ZuQku%2BdHXXbom5oyt6zWpFRRLxHTLYv6T7Jh4O%2FVorq29OhPLIKm4ZU86lGx5vQ1dX427mXNiYLKaBhJHrG1C1y41qPprhVbp4uQ%2FvnxS2ECRsLIy4ekbQ8OzFKfqBht%2FNc7ISky7xkRWmSOF4aUiYmu2OH7WY05sDf4a2KXPHxmKUsilFJGQT%2BL6LcElo%2Fx8fbVou7pJKU0UCcZ6X7PuSzMfa6dROti%2Fk0kNRwJl%2FlvkkAsoM2Rle8gVPx0jtOmnV6I0KAZf1QjWj9eBvKHM4FNBQZZVf898PO5sXQgtsMPHMir0GOqUBFTOBgNJGKawAlwXCDEoToisVh9yDTC23ylZDn0d1Cx9%2FOxrt7oQqpkWkNyHDSw3H94wfTjHrheOyOOUls4LCyIFmmjcwxMpvS%2Fwuhnso3FlnZSiLuiN5fvp11oX9E2aLoamHKyoePh06EThz9wo67AUoi6oXIaTR4bN09uApWN9LSP3a%2BwNnU8NRThCmu5FYKARz0SNIcz8HeEISn0eXYVabDvlF&X-Amz-Signature=0abecedf7afefb50046903f17d5cce6d9772da95e7b84a8019d55b5f1d7e465c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YLMLP6M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIANuge%2By0FYScGCkmJVV7fOwTozMhYG0%2BfP2xq0e77s3AiEA0byRdmCAHu3VwBd3c31odeOWZfFPzmCAIO%2BcsCKZogAq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDCV0iMHO5YQBxybiGyrcA8PAl%2FapnEMm%2B1ecTPFHFPhy0FaT5QS660y8CzSh%2Bnn%2FymcVS5Qj2WXepS3Qvy6lgVLtU2ypEynwMhwg7Uq%2FBOUiOFptf3OmGLka7hSGt436zGm12a2YN4EDQwIDIHntsRpjojz9%2BamDKrYLlCk%2BJ4xMoP99ddWubbYfnayeFxNmWTdJS6QNVc2sv2LbO2uTmeBkIQb90nTvBxvSLh5cU8ZzM1p29kYLDuh5jTxdJvhnZOFaQO%2BU%2BHSdzt0AvyyCMiX8HB9cRGhXijyjCXkmqQXA0VXQ3%2FWK2CfvWQUwniJGelUaWuMMNa5Zy78Rg7L74J5nwuhO8n18kkCRD2ZuQku%2BdHXXbom5oyt6zWpFRRLxHTLYv6T7Jh4O%2FVorq29OhPLIKm4ZU86lGx5vQ1dX427mXNiYLKaBhJHrG1C1y41qPprhVbp4uQ%2FvnxS2ECRsLIy4ekbQ8OzFKfqBht%2FNc7ISky7xkRWmSOF4aUiYmu2OH7WY05sDf4a2KXPHxmKUsilFJGQT%2BL6LcElo%2Fx8fbVou7pJKU0UCcZ6X7PuSzMfa6dROti%2Fk0kNRwJl%2FlvkkAsoM2Rle8gVPx0jtOmnV6I0KAZf1QjWj9eBvKHM4FNBQZZVf898PO5sXQgtsMPHMir0GOqUBFTOBgNJGKawAlwXCDEoToisVh9yDTC23ylZDn0d1Cx9%2FOxrt7oQqpkWkNyHDSw3H94wfTjHrheOyOOUls4LCyIFmmjcwxMpvS%2Fwuhnso3FlnZSiLuiN5fvp11oX9E2aLoamHKyoePh06EThz9wo67AUoi6oXIaTR4bN09uApWN9LSP3a%2BwNnU8NRThCmu5FYKARz0SNIcz8HeEISn0eXYVabDvlF&X-Amz-Signature=a5373a1f7f6f45b5beecdbb4f98a55723faeafcfbe32c96d79c6f1728a09aeef&X-Amz-SignedHeaders=host&x-id=GetObject)
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


