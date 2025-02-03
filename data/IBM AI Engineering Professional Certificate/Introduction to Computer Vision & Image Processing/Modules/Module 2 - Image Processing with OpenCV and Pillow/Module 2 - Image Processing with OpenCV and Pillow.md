

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM5VKWXH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEprjBLP0MWEJVFey6dsf3b0PJ7waMoLCqLubQmVC%2Fz7AiEAvORGxF0qPNiMDI57v1FQeVxzZq8tCkdLVUEWyv16%2B34qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgAQd2Mm6Zk6zJ8qircA9JHg0POVlo5lp433HFJqKSckvlbbr9d80W8QMzI5%2Bm4fdyek%2FML8jU%2FzJTspbFA2GK%2FDp7U5%2B9vgMz1EV4WQJYSJo4J%2FWZ%2FeNL%2BHooYaPagVDGMiM1Le6cdO1ca3%2FWJFj0qv1pCk7%2B61PlYhdyybQixOAkuXsAmCypUy8MVaCggrGpXTCZW11w6f1IgsQqqdRcdmGCu9JN%2FmXI1QamSVkHraN6l0WFmlouaQvBUOACznr6xgPpoVd%2Ff7uCCSXIxB0gx23RbQ4eyd9pkryfiFlGRaJq6aeGSJx%2Fk63IobGJ6YwtabjECE7OByh0jywrUBtJNOmCOGE35PhHfLwcYuQO4hUtaWPoik7TlaUht9rZ8X%2FsRMVzEPIYA2uN3J699KOc27MaFHSCehnw%2FjRgn0oYxu3rzB0X7YDSIIJLYJbUVQgCMT0Jr1loX%2FaxlDXF9HyCGQ9%2F76cUJ1ObELS%2FQJKG9J7L%2F4iSS2ZtHPjicisSeQR5o2Fs3wnp3SOf8jMMpmPtHOsl3R5xAxALtpd0uH%2FM7wx6FHOgurdDMGG7SGBavDp54gsUQSrwzAcRh2GnzvCR634QrqBXID54nEMaxodxtsEj64TdKTsi1dG2fEVRpj7J4l47D9VzmGoBxMN%2B5gb0GOqUBUGwx%2FJlLAq5iJN4OrG1Jl2uJSI18z%2FS4%2Fyk1XS4H45JeSmXfPpNkoLZZDXQsYX2dRyVD76%2F8JzZawNR1sNS988OUkounsi05haEcJPhhyCEm1Qt5AV54lsca1%2BOWvmpoLZ7vyNMwbpsUW06GH7mvg%2FQ3G8WM%2FQsBu705dvvVsyUel7Uwpds%2B58CevGWDMI7gtOIhCAC0bJxooXxIaxLhKH4YO5VQ&X-Amz-Signature=f332a3968737501cd9eb05390b7d6adf8517f408d525d805af9b257110527890&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REIUKAOB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFyirbG1dizSdZAPePIyP0C%2FT%2FceSBifRt%2FF1%2Bu5MRgwAiASAZ2JZSSQrejz3K2bjGIHWfO5wzRexJn%2B%2BvqYwcjlGSqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIcdA0de55flmRd58KtwDIBnLIkbTidAhuTZB2IQdNhkHr5wMifvXZA14y0s0LuOZJk0KDP0wl4mVQZRJ%2BFGyaSsU2v%2BdVDr7JRxH0P%2BPX3b4Rj3vkQRi3Z82I3zVo5e640SgdJL%2F5fp3LEEi5%2ByYqHKC2VhmMypW7ce3zgPa9k7gEemkeElIba5A64SBRBdQnwf%2FQ60%2Femm7SlZNFTrH8gFoXeeLSyGytKDNt9CnFSlNwSO5ytU7X1Q9MI8RVSkGbgMW2NBYnItneOpzuAV89uVKtkRE86TJouy%2BrdewLYnt901NE2991irapgrpJZnvpzQc1%2Bn%2F1nqB0pqJvIfTCubXFK70ySgih2xouY6Frai0H6%2BFCrChoz%2Bd6T3InoshwmOwjwawT9kZCTLOzFl25ZN96NFP6gC5XpiTMluUdwrTC8xdwCaZeBY8C1qz9LWxLNZfKpqGaJLGSSh47%2FVYMTMifdMHC6FPE95QxMNq8iH%2Br5GdTvyZMGmYHKoASRoNTAUapRpFZZBqI%2B0DxzWDDK3KLym9vh0jwEoxMvqot6AX8U1CgGXKigIOlmZ5uNqvTl9Wo9kjKgoUftuv5zKifuwEvK1xbAT3He3q5JBoplpRuXENfTuKWO%2F2e%2Fiq3YHgingXmkTZuKhWYTIwibqBvQY6pgHTJ7fqKx9BaOX1A5yXKe0VDh8E3Xa6ZPVRNqM2yjuhIwMLCZpIlsWcasxLk%2F%2Br0wM3p6Krt5mRfwloTxW1pGSJEKab8ZTPNMj7%2BDdFBEHbyRdxoic4sRYrkzc4USebTw0qfnqjAjfaWuysoLRx8GzWeGAqca0iDUEjkILQIUV%2FHyxys3kuDKUZHNOGtQT9MK3UtYsDvHKNFZE91QV3TYAYTeTOd0pm&X-Amz-Signature=d88f7972c81840f77c893c971f533c493bb38c6f4cfa1b4b237e118462077ed6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REIUKAOB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFyirbG1dizSdZAPePIyP0C%2FT%2FceSBifRt%2FF1%2Bu5MRgwAiASAZ2JZSSQrejz3K2bjGIHWfO5wzRexJn%2B%2BvqYwcjlGSqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIcdA0de55flmRd58KtwDIBnLIkbTidAhuTZB2IQdNhkHr5wMifvXZA14y0s0LuOZJk0KDP0wl4mVQZRJ%2BFGyaSsU2v%2BdVDr7JRxH0P%2BPX3b4Rj3vkQRi3Z82I3zVo5e640SgdJL%2F5fp3LEEi5%2ByYqHKC2VhmMypW7ce3zgPa9k7gEemkeElIba5A64SBRBdQnwf%2FQ60%2Femm7SlZNFTrH8gFoXeeLSyGytKDNt9CnFSlNwSO5ytU7X1Q9MI8RVSkGbgMW2NBYnItneOpzuAV89uVKtkRE86TJouy%2BrdewLYnt901NE2991irapgrpJZnvpzQc1%2Bn%2F1nqB0pqJvIfTCubXFK70ySgih2xouY6Frai0H6%2BFCrChoz%2Bd6T3InoshwmOwjwawT9kZCTLOzFl25ZN96NFP6gC5XpiTMluUdwrTC8xdwCaZeBY8C1qz9LWxLNZfKpqGaJLGSSh47%2FVYMTMifdMHC6FPE95QxMNq8iH%2Br5GdTvyZMGmYHKoASRoNTAUapRpFZZBqI%2B0DxzWDDK3KLym9vh0jwEoxMvqot6AX8U1CgGXKigIOlmZ5uNqvTl9Wo9kjKgoUftuv5zKifuwEvK1xbAT3He3q5JBoplpRuXENfTuKWO%2F2e%2Fiq3YHgingXmkTZuKhWYTIwibqBvQY6pgHTJ7fqKx9BaOX1A5yXKe0VDh8E3Xa6ZPVRNqM2yjuhIwMLCZpIlsWcasxLk%2F%2Br0wM3p6Krt5mRfwloTxW1pGSJEKab8ZTPNMj7%2BDdFBEHbyRdxoic4sRYrkzc4USebTw0qfnqjAjfaWuysoLRx8GzWeGAqca0iDUEjkILQIUV%2FHyxys3kuDKUZHNOGtQT9MK3UtYsDvHKNFZE91QV3TYAYTeTOd0pm&X-Amz-Signature=37f52fe67e5b12d7feb84ae93707106d63d0ff367eb85a282ce92fa4629c5aa0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REIUKAOB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFyirbG1dizSdZAPePIyP0C%2FT%2FceSBifRt%2FF1%2Bu5MRgwAiASAZ2JZSSQrejz3K2bjGIHWfO5wzRexJn%2B%2BvqYwcjlGSqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIcdA0de55flmRd58KtwDIBnLIkbTidAhuTZB2IQdNhkHr5wMifvXZA14y0s0LuOZJk0KDP0wl4mVQZRJ%2BFGyaSsU2v%2BdVDr7JRxH0P%2BPX3b4Rj3vkQRi3Z82I3zVo5e640SgdJL%2F5fp3LEEi5%2ByYqHKC2VhmMypW7ce3zgPa9k7gEemkeElIba5A64SBRBdQnwf%2FQ60%2Femm7SlZNFTrH8gFoXeeLSyGytKDNt9CnFSlNwSO5ytU7X1Q9MI8RVSkGbgMW2NBYnItneOpzuAV89uVKtkRE86TJouy%2BrdewLYnt901NE2991irapgrpJZnvpzQc1%2Bn%2F1nqB0pqJvIfTCubXFK70ySgih2xouY6Frai0H6%2BFCrChoz%2Bd6T3InoshwmOwjwawT9kZCTLOzFl25ZN96NFP6gC5XpiTMluUdwrTC8xdwCaZeBY8C1qz9LWxLNZfKpqGaJLGSSh47%2FVYMTMifdMHC6FPE95QxMNq8iH%2Br5GdTvyZMGmYHKoASRoNTAUapRpFZZBqI%2B0DxzWDDK3KLym9vh0jwEoxMvqot6AX8U1CgGXKigIOlmZ5uNqvTl9Wo9kjKgoUftuv5zKifuwEvK1xbAT3He3q5JBoplpRuXENfTuKWO%2F2e%2Fiq3YHgingXmkTZuKhWYTIwibqBvQY6pgHTJ7fqKx9BaOX1A5yXKe0VDh8E3Xa6ZPVRNqM2yjuhIwMLCZpIlsWcasxLk%2F%2Br0wM3p6Krt5mRfwloTxW1pGSJEKab8ZTPNMj7%2BDdFBEHbyRdxoic4sRYrkzc4USebTw0qfnqjAjfaWuysoLRx8GzWeGAqca0iDUEjkILQIUV%2FHyxys3kuDKUZHNOGtQT9MK3UtYsDvHKNFZE91QV3TYAYTeTOd0pm&X-Amz-Signature=129f714d424cb1f315554ae462c6a35bd7823fe4a9dd6d107ba6ee26cd1fecf9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REIUKAOB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFyirbG1dizSdZAPePIyP0C%2FT%2FceSBifRt%2FF1%2Bu5MRgwAiASAZ2JZSSQrejz3K2bjGIHWfO5wzRexJn%2B%2BvqYwcjlGSqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIcdA0de55flmRd58KtwDIBnLIkbTidAhuTZB2IQdNhkHr5wMifvXZA14y0s0LuOZJk0KDP0wl4mVQZRJ%2BFGyaSsU2v%2BdVDr7JRxH0P%2BPX3b4Rj3vkQRi3Z82I3zVo5e640SgdJL%2F5fp3LEEi5%2ByYqHKC2VhmMypW7ce3zgPa9k7gEemkeElIba5A64SBRBdQnwf%2FQ60%2Femm7SlZNFTrH8gFoXeeLSyGytKDNt9CnFSlNwSO5ytU7X1Q9MI8RVSkGbgMW2NBYnItneOpzuAV89uVKtkRE86TJouy%2BrdewLYnt901NE2991irapgrpJZnvpzQc1%2Bn%2F1nqB0pqJvIfTCubXFK70ySgih2xouY6Frai0H6%2BFCrChoz%2Bd6T3InoshwmOwjwawT9kZCTLOzFl25ZN96NFP6gC5XpiTMluUdwrTC8xdwCaZeBY8C1qz9LWxLNZfKpqGaJLGSSh47%2FVYMTMifdMHC6FPE95QxMNq8iH%2Br5GdTvyZMGmYHKoASRoNTAUapRpFZZBqI%2B0DxzWDDK3KLym9vh0jwEoxMvqot6AX8U1CgGXKigIOlmZ5uNqvTl9Wo9kjKgoUftuv5zKifuwEvK1xbAT3He3q5JBoplpRuXENfTuKWO%2F2e%2Fiq3YHgingXmkTZuKhWYTIwibqBvQY6pgHTJ7fqKx9BaOX1A5yXKe0VDh8E3Xa6ZPVRNqM2yjuhIwMLCZpIlsWcasxLk%2F%2Br0wM3p6Krt5mRfwloTxW1pGSJEKab8ZTPNMj7%2BDdFBEHbyRdxoic4sRYrkzc4USebTw0qfnqjAjfaWuysoLRx8GzWeGAqca0iDUEjkILQIUV%2FHyxys3kuDKUZHNOGtQT9MK3UtYsDvHKNFZE91QV3TYAYTeTOd0pm&X-Amz-Signature=1bd36efe984243e0e4588a6b527eb4bbb62e2f558fb35eb2cfde7a7d64222357&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REIUKAOB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFyirbG1dizSdZAPePIyP0C%2FT%2FceSBifRt%2FF1%2Bu5MRgwAiASAZ2JZSSQrejz3K2bjGIHWfO5wzRexJn%2B%2BvqYwcjlGSqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIcdA0de55flmRd58KtwDIBnLIkbTidAhuTZB2IQdNhkHr5wMifvXZA14y0s0LuOZJk0KDP0wl4mVQZRJ%2BFGyaSsU2v%2BdVDr7JRxH0P%2BPX3b4Rj3vkQRi3Z82I3zVo5e640SgdJL%2F5fp3LEEi5%2ByYqHKC2VhmMypW7ce3zgPa9k7gEemkeElIba5A64SBRBdQnwf%2FQ60%2Femm7SlZNFTrH8gFoXeeLSyGytKDNt9CnFSlNwSO5ytU7X1Q9MI8RVSkGbgMW2NBYnItneOpzuAV89uVKtkRE86TJouy%2BrdewLYnt901NE2991irapgrpJZnvpzQc1%2Bn%2F1nqB0pqJvIfTCubXFK70ySgih2xouY6Frai0H6%2BFCrChoz%2Bd6T3InoshwmOwjwawT9kZCTLOzFl25ZN96NFP6gC5XpiTMluUdwrTC8xdwCaZeBY8C1qz9LWxLNZfKpqGaJLGSSh47%2FVYMTMifdMHC6FPE95QxMNq8iH%2Br5GdTvyZMGmYHKoASRoNTAUapRpFZZBqI%2B0DxzWDDK3KLym9vh0jwEoxMvqot6AX8U1CgGXKigIOlmZ5uNqvTl9Wo9kjKgoUftuv5zKifuwEvK1xbAT3He3q5JBoplpRuXENfTuKWO%2F2e%2Fiq3YHgingXmkTZuKhWYTIwibqBvQY6pgHTJ7fqKx9BaOX1A5yXKe0VDh8E3Xa6ZPVRNqM2yjuhIwMLCZpIlsWcasxLk%2F%2Br0wM3p6Krt5mRfwloTxW1pGSJEKab8ZTPNMj7%2BDdFBEHbyRdxoic4sRYrkzc4USebTw0qfnqjAjfaWuysoLRx8GzWeGAqca0iDUEjkILQIUV%2FHyxys3kuDKUZHNOGtQT9MK3UtYsDvHKNFZE91QV3TYAYTeTOd0pm&X-Amz-Signature=02eb6726425f91754c6ff03b13c7b698ddf386ed2c4c4fae4777eb1aafb9bc24&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM5VKWXH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEprjBLP0MWEJVFey6dsf3b0PJ7waMoLCqLubQmVC%2Fz7AiEAvORGxF0qPNiMDI57v1FQeVxzZq8tCkdLVUEWyv16%2B34qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgAQd2Mm6Zk6zJ8qircA9JHg0POVlo5lp433HFJqKSckvlbbr9d80W8QMzI5%2Bm4fdyek%2FML8jU%2FzJTspbFA2GK%2FDp7U5%2B9vgMz1EV4WQJYSJo4J%2FWZ%2FeNL%2BHooYaPagVDGMiM1Le6cdO1ca3%2FWJFj0qv1pCk7%2B61PlYhdyybQixOAkuXsAmCypUy8MVaCggrGpXTCZW11w6f1IgsQqqdRcdmGCu9JN%2FmXI1QamSVkHraN6l0WFmlouaQvBUOACznr6xgPpoVd%2Ff7uCCSXIxB0gx23RbQ4eyd9pkryfiFlGRaJq6aeGSJx%2Fk63IobGJ6YwtabjECE7OByh0jywrUBtJNOmCOGE35PhHfLwcYuQO4hUtaWPoik7TlaUht9rZ8X%2FsRMVzEPIYA2uN3J699KOc27MaFHSCehnw%2FjRgn0oYxu3rzB0X7YDSIIJLYJbUVQgCMT0Jr1loX%2FaxlDXF9HyCGQ9%2F76cUJ1ObELS%2FQJKG9J7L%2F4iSS2ZtHPjicisSeQR5o2Fs3wnp3SOf8jMMpmPtHOsl3R5xAxALtpd0uH%2FM7wx6FHOgurdDMGG7SGBavDp54gsUQSrwzAcRh2GnzvCR634QrqBXID54nEMaxodxtsEj64TdKTsi1dG2fEVRpj7J4l47D9VzmGoBxMN%2B5gb0GOqUBUGwx%2FJlLAq5iJN4OrG1Jl2uJSI18z%2FS4%2Fyk1XS4H45JeSmXfPpNkoLZZDXQsYX2dRyVD76%2F8JzZawNR1sNS988OUkounsi05haEcJPhhyCEm1Qt5AV54lsca1%2BOWvmpoLZ7vyNMwbpsUW06GH7mvg%2FQ3G8WM%2FQsBu705dvvVsyUel7Uwpds%2B58CevGWDMI7gtOIhCAC0bJxooXxIaxLhKH4YO5VQ&X-Amz-Signature=a757d724e3c454488b972a3412f2a1bb04f9d296c1d9eca20fd92b3b668536ba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM5VKWXH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEprjBLP0MWEJVFey6dsf3b0PJ7waMoLCqLubQmVC%2Fz7AiEAvORGxF0qPNiMDI57v1FQeVxzZq8tCkdLVUEWyv16%2B34qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgAQd2Mm6Zk6zJ8qircA9JHg0POVlo5lp433HFJqKSckvlbbr9d80W8QMzI5%2Bm4fdyek%2FML8jU%2FzJTspbFA2GK%2FDp7U5%2B9vgMz1EV4WQJYSJo4J%2FWZ%2FeNL%2BHooYaPagVDGMiM1Le6cdO1ca3%2FWJFj0qv1pCk7%2B61PlYhdyybQixOAkuXsAmCypUy8MVaCggrGpXTCZW11w6f1IgsQqqdRcdmGCu9JN%2FmXI1QamSVkHraN6l0WFmlouaQvBUOACznr6xgPpoVd%2Ff7uCCSXIxB0gx23RbQ4eyd9pkryfiFlGRaJq6aeGSJx%2Fk63IobGJ6YwtabjECE7OByh0jywrUBtJNOmCOGE35PhHfLwcYuQO4hUtaWPoik7TlaUht9rZ8X%2FsRMVzEPIYA2uN3J699KOc27MaFHSCehnw%2FjRgn0oYxu3rzB0X7YDSIIJLYJbUVQgCMT0Jr1loX%2FaxlDXF9HyCGQ9%2F76cUJ1ObELS%2FQJKG9J7L%2F4iSS2ZtHPjicisSeQR5o2Fs3wnp3SOf8jMMpmPtHOsl3R5xAxALtpd0uH%2FM7wx6FHOgurdDMGG7SGBavDp54gsUQSrwzAcRh2GnzvCR634QrqBXID54nEMaxodxtsEj64TdKTsi1dG2fEVRpj7J4l47D9VzmGoBxMN%2B5gb0GOqUBUGwx%2FJlLAq5iJN4OrG1Jl2uJSI18z%2FS4%2Fyk1XS4H45JeSmXfPpNkoLZZDXQsYX2dRyVD76%2F8JzZawNR1sNS988OUkounsi05haEcJPhhyCEm1Qt5AV54lsca1%2BOWvmpoLZ7vyNMwbpsUW06GH7mvg%2FQ3G8WM%2FQsBu705dvvVsyUel7Uwpds%2B58CevGWDMI7gtOIhCAC0bJxooXxIaxLhKH4YO5VQ&X-Amz-Signature=1e979dcbbefc7738c9656d50dba98a6a1014b6e8a1696eccf39fb510d1ca571f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM5VKWXH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEprjBLP0MWEJVFey6dsf3b0PJ7waMoLCqLubQmVC%2Fz7AiEAvORGxF0qPNiMDI57v1FQeVxzZq8tCkdLVUEWyv16%2B34qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgAQd2Mm6Zk6zJ8qircA9JHg0POVlo5lp433HFJqKSckvlbbr9d80W8QMzI5%2Bm4fdyek%2FML8jU%2FzJTspbFA2GK%2FDp7U5%2B9vgMz1EV4WQJYSJo4J%2FWZ%2FeNL%2BHooYaPagVDGMiM1Le6cdO1ca3%2FWJFj0qv1pCk7%2B61PlYhdyybQixOAkuXsAmCypUy8MVaCggrGpXTCZW11w6f1IgsQqqdRcdmGCu9JN%2FmXI1QamSVkHraN6l0WFmlouaQvBUOACznr6xgPpoVd%2Ff7uCCSXIxB0gx23RbQ4eyd9pkryfiFlGRaJq6aeGSJx%2Fk63IobGJ6YwtabjECE7OByh0jywrUBtJNOmCOGE35PhHfLwcYuQO4hUtaWPoik7TlaUht9rZ8X%2FsRMVzEPIYA2uN3J699KOc27MaFHSCehnw%2FjRgn0oYxu3rzB0X7YDSIIJLYJbUVQgCMT0Jr1loX%2FaxlDXF9HyCGQ9%2F76cUJ1ObELS%2FQJKG9J7L%2F4iSS2ZtHPjicisSeQR5o2Fs3wnp3SOf8jMMpmPtHOsl3R5xAxALtpd0uH%2FM7wx6FHOgurdDMGG7SGBavDp54gsUQSrwzAcRh2GnzvCR634QrqBXID54nEMaxodxtsEj64TdKTsi1dG2fEVRpj7J4l47D9VzmGoBxMN%2B5gb0GOqUBUGwx%2FJlLAq5iJN4OrG1Jl2uJSI18z%2FS4%2Fyk1XS4H45JeSmXfPpNkoLZZDXQsYX2dRyVD76%2F8JzZawNR1sNS988OUkounsi05haEcJPhhyCEm1Qt5AV54lsca1%2BOWvmpoLZ7vyNMwbpsUW06GH7mvg%2FQ3G8WM%2FQsBu705dvvVsyUel7Uwpds%2B58CevGWDMI7gtOIhCAC0bJxooXxIaxLhKH4YO5VQ&X-Amz-Signature=440ae36771b577812161300b84dc94635c8c70f7de3b77b3f41649fe992e492a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM5VKWXH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEprjBLP0MWEJVFey6dsf3b0PJ7waMoLCqLubQmVC%2Fz7AiEAvORGxF0qPNiMDI57v1FQeVxzZq8tCkdLVUEWyv16%2B34qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgAQd2Mm6Zk6zJ8qircA9JHg0POVlo5lp433HFJqKSckvlbbr9d80W8QMzI5%2Bm4fdyek%2FML8jU%2FzJTspbFA2GK%2FDp7U5%2B9vgMz1EV4WQJYSJo4J%2FWZ%2FeNL%2BHooYaPagVDGMiM1Le6cdO1ca3%2FWJFj0qv1pCk7%2B61PlYhdyybQixOAkuXsAmCypUy8MVaCggrGpXTCZW11w6f1IgsQqqdRcdmGCu9JN%2FmXI1QamSVkHraN6l0WFmlouaQvBUOACznr6xgPpoVd%2Ff7uCCSXIxB0gx23RbQ4eyd9pkryfiFlGRaJq6aeGSJx%2Fk63IobGJ6YwtabjECE7OByh0jywrUBtJNOmCOGE35PhHfLwcYuQO4hUtaWPoik7TlaUht9rZ8X%2FsRMVzEPIYA2uN3J699KOc27MaFHSCehnw%2FjRgn0oYxu3rzB0X7YDSIIJLYJbUVQgCMT0Jr1loX%2FaxlDXF9HyCGQ9%2F76cUJ1ObELS%2FQJKG9J7L%2F4iSS2ZtHPjicisSeQR5o2Fs3wnp3SOf8jMMpmPtHOsl3R5xAxALtpd0uH%2FM7wx6FHOgurdDMGG7SGBavDp54gsUQSrwzAcRh2GnzvCR634QrqBXID54nEMaxodxtsEj64TdKTsi1dG2fEVRpj7J4l47D9VzmGoBxMN%2B5gb0GOqUBUGwx%2FJlLAq5iJN4OrG1Jl2uJSI18z%2FS4%2Fyk1XS4H45JeSmXfPpNkoLZZDXQsYX2dRyVD76%2F8JzZawNR1sNS988OUkounsi05haEcJPhhyCEm1Qt5AV54lsca1%2BOWvmpoLZ7vyNMwbpsUW06GH7mvg%2FQ3G8WM%2FQsBu705dvvVsyUel7Uwpds%2B58CevGWDMI7gtOIhCAC0bJxooXxIaxLhKH4YO5VQ&X-Amz-Signature=00c8453339f193e78172c4b9656e1dbdde20e335e81cdde032bf3dfd6e5a3714&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM5VKWXH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEprjBLP0MWEJVFey6dsf3b0PJ7waMoLCqLubQmVC%2Fz7AiEAvORGxF0qPNiMDI57v1FQeVxzZq8tCkdLVUEWyv16%2B34qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgAQd2Mm6Zk6zJ8qircA9JHg0POVlo5lp433HFJqKSckvlbbr9d80W8QMzI5%2Bm4fdyek%2FML8jU%2FzJTspbFA2GK%2FDp7U5%2B9vgMz1EV4WQJYSJo4J%2FWZ%2FeNL%2BHooYaPagVDGMiM1Le6cdO1ca3%2FWJFj0qv1pCk7%2B61PlYhdyybQixOAkuXsAmCypUy8MVaCggrGpXTCZW11w6f1IgsQqqdRcdmGCu9JN%2FmXI1QamSVkHraN6l0WFmlouaQvBUOACznr6xgPpoVd%2Ff7uCCSXIxB0gx23RbQ4eyd9pkryfiFlGRaJq6aeGSJx%2Fk63IobGJ6YwtabjECE7OByh0jywrUBtJNOmCOGE35PhHfLwcYuQO4hUtaWPoik7TlaUht9rZ8X%2FsRMVzEPIYA2uN3J699KOc27MaFHSCehnw%2FjRgn0oYxu3rzB0X7YDSIIJLYJbUVQgCMT0Jr1loX%2FaxlDXF9HyCGQ9%2F76cUJ1ObELS%2FQJKG9J7L%2F4iSS2ZtHPjicisSeQR5o2Fs3wnp3SOf8jMMpmPtHOsl3R5xAxALtpd0uH%2FM7wx6FHOgurdDMGG7SGBavDp54gsUQSrwzAcRh2GnzvCR634QrqBXID54nEMaxodxtsEj64TdKTsi1dG2fEVRpj7J4l47D9VzmGoBxMN%2B5gb0GOqUBUGwx%2FJlLAq5iJN4OrG1Jl2uJSI18z%2FS4%2Fyk1XS4H45JeSmXfPpNkoLZZDXQsYX2dRyVD76%2F8JzZawNR1sNS988OUkounsi05haEcJPhhyCEm1Qt5AV54lsca1%2BOWvmpoLZ7vyNMwbpsUW06GH7mvg%2FQ3G8WM%2FQsBu705dvvVsyUel7Uwpds%2B58CevGWDMI7gtOIhCAC0bJxooXxIaxLhKH4YO5VQ&X-Amz-Signature=b1319cac24bf68b01cee01367fe164f8ca7d6dc2117c45d45d18b8f825816e4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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


