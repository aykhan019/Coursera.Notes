

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4OMAZW4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIDW8uNwy6xzFVSq1EU6mOhHHKBCxc%2B1grqnp%2F%2FrNXLcMAiAcJazGwsgdgJzlrFMvV1ZM40xIZBnCxJK70d5%2FdcgHDyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBm%2FS9p6MGCTuuzK0KtwD6l1U4FFvnxKaS2eM5Zu4l4y0puO2H9hAsNkPdd%2BuH6GOmLXblNNzZ%2FmOC0j6xqmVcC08reD6TasJnYb6Y8UewZOHOaQsCBBLC9f%2Fqjs4MnnoF549LzVe4i3zkqlrweixSUBKFt1k4r5W0RJW14wzkxI5GvrAaaFkT2708q8xoR%2FlfwkGC4alhrnsij%2FzoX7Yi%2BnLuqR%2Fe1kLP1o8Yx%2FjiXrfZWEwDKVof1zBwJtqN8rPjNstTs2tU%2B8tmjfGP7Z2dNy24jA2gIW7pllRAOUrsjT8IqH2yeiPgKceOLcsoZnOoJnq4DE%2FmFu%2BAvjENZaaZu5RviVkg6y8Ua67gylDZBkkp%2Bl5G1DTlYIJJ%2BpdyqooZSP%2BwE0CdCGTlTy%2FnrRKykfnNNJfO6t1z0VFZV%2B0PdcGwcsrgcxaAXBxWriMNMJ3bkw%2FZVDbFQZEhSY98THwsiBuRvEWXs8eyWXBdi6gfnbnxhbOYH4TamnoVQYZGlwofMCnNNFoNjX66YP%2FFFcPRfKIOdME7Myyn8oC8bQWWf2ITGIgCYL5W6ZBRkIZsX%2BCeioAQv6COPX3SmiZNTB6h3VzjgWWmfxYeA9%2FUy5Aj8ANH0emvyMsCHYLTSKQl0wNIW2VPL0B9u%2FsmDQwlLKbvQY6pgF0l%2Fzkr0ytR4bZ8jk3JC1MbbUXj0ghE%2B%2FhBM5en%2Fze9EjsOroD07%2BIMcPPMT7pS2K2NkPE%2FXxNPXw8j%2BqYn1k6ra3r3J5ng7RmgzBU%2FDSfQKWVG4p5yvibxvepUrqBHRdvvlNFKa9kxI5pyMdQ0gh4xZCIHMe6m52%2FpNoWOIQqyUSZqT1GeSoieu2CiYIQiRoZRGSWkITsBccTBlIDRDZw3cgq%2FIbE&X-Amz-Signature=6f147c9623ac2659880c512b8cb7e56879825892f24d3f4ac4704728e5750233&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEGTQXLI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIFivTuzmB2fHOCwiinjfwtiBe9GJN9NhOh4Bpv%2BBujJWAiAHlc8taL68Iwb1SyLOx553EghQcOQgmoU6afexmw3sjyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgx%2FaP%2BgA9gbSfXIoKtwD6bJwislDz16%2F%2BebN2rT3i%2BvJnwFTioCr40oSI2nl4mQTcznYed9u0jh4g8GfSXV4btdLiHrGGLFREeKy9FvViZ8R1%2FhTatBDAOHt3ByhkF7LQxLNLzx1KS%2FJ3LPdDD280w5QXv3qu0CKd3XAB0xYxPZ47DO2Kls%2BvxJTdqFGgCs27uRVpRzvaeAX32tg8DQLfPY%2F9tWOTu7P11uPVj8cjI05%2FtLv98CykECr9EDpkSbrN%2Fp40rv196jptjQne0I4sUbuXRKDfUSS9D8eGbmMHBzZGekAjAqPvpD6flGdE72dWJSHyTsr2W7u6XphGnV%2FFQgWycbuhPo8DKVToxkqomgQky2XexhQyxlFM1%2FCXo51UH695anamS0XFStLcYfQrOtJRavHw%2BweilTgDgWAI%2B14SF%2BWgLBB%2FFfICI9h6AbGUjgPRfrGh%2FgTEAwr%2FTDNQhcGVCHfcqnAk52ZS3xFxdikbuDVMe%2Fb6eCY8l2z1%2B5WXsvHbm2u6uQARvbrhXJIjSHf5IQUNsB18OnSuF7qbeHyQYUUm8CWXMUi%2Br6seIQFFHdWqhfg1B02bEGmRXQt%2F%2FEli5CcOf2RgGw4whqSWByu2L%2BQWQlpL6Tulzz5krbtMOp%2FWbJRiUsp5hcwsrKbvQY6pgGqTJ4YZr7XlDQvb5sfDyC6qeRcPgDQr0imS%2FjGuA2%2F5P748J2EZvkUjiv%2BikM2IpvHWNxeZsgBiGi2FkQuHMkteTvtP3QtYsO3PTAJVR5ItD2y5Ki3zQ8Yn5hxNIrucyY%2BXnsNW1fCZQRM3doGE3sWCFi2RSQ4cXAcD3Q1MPgHPU7rJYHsKgZTred3EAjn9oH8Dxg%2BDC7mjeX4s%2B7sYFBiQmlRTriY&X-Amz-Signature=9495d8b58c8d7598ce2099e8689cf799cac8cb18870095dcadbd251b5b7fba49&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEGTQXLI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIFivTuzmB2fHOCwiinjfwtiBe9GJN9NhOh4Bpv%2BBujJWAiAHlc8taL68Iwb1SyLOx553EghQcOQgmoU6afexmw3sjyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgx%2FaP%2BgA9gbSfXIoKtwD6bJwislDz16%2F%2BebN2rT3i%2BvJnwFTioCr40oSI2nl4mQTcznYed9u0jh4g8GfSXV4btdLiHrGGLFREeKy9FvViZ8R1%2FhTatBDAOHt3ByhkF7LQxLNLzx1KS%2FJ3LPdDD280w5QXv3qu0CKd3XAB0xYxPZ47DO2Kls%2BvxJTdqFGgCs27uRVpRzvaeAX32tg8DQLfPY%2F9tWOTu7P11uPVj8cjI05%2FtLv98CykECr9EDpkSbrN%2Fp40rv196jptjQne0I4sUbuXRKDfUSS9D8eGbmMHBzZGekAjAqPvpD6flGdE72dWJSHyTsr2W7u6XphGnV%2FFQgWycbuhPo8DKVToxkqomgQky2XexhQyxlFM1%2FCXo51UH695anamS0XFStLcYfQrOtJRavHw%2BweilTgDgWAI%2B14SF%2BWgLBB%2FFfICI9h6AbGUjgPRfrGh%2FgTEAwr%2FTDNQhcGVCHfcqnAk52ZS3xFxdikbuDVMe%2Fb6eCY8l2z1%2B5WXsvHbm2u6uQARvbrhXJIjSHf5IQUNsB18OnSuF7qbeHyQYUUm8CWXMUi%2Br6seIQFFHdWqhfg1B02bEGmRXQt%2F%2FEli5CcOf2RgGw4whqSWByu2L%2BQWQlpL6Tulzz5krbtMOp%2FWbJRiUsp5hcwsrKbvQY6pgGqTJ4YZr7XlDQvb5sfDyC6qeRcPgDQr0imS%2FjGuA2%2F5P748J2EZvkUjiv%2BikM2IpvHWNxeZsgBiGi2FkQuHMkteTvtP3QtYsO3PTAJVR5ItD2y5Ki3zQ8Yn5hxNIrucyY%2BXnsNW1fCZQRM3doGE3sWCFi2RSQ4cXAcD3Q1MPgHPU7rJYHsKgZTred3EAjn9oH8Dxg%2BDC7mjeX4s%2B7sYFBiQmlRTriY&X-Amz-Signature=eac4f07f89aceb540251460e47b395a45561053f54f92e05f533701bfcd8504e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEGTQXLI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIFivTuzmB2fHOCwiinjfwtiBe9GJN9NhOh4Bpv%2BBujJWAiAHlc8taL68Iwb1SyLOx553EghQcOQgmoU6afexmw3sjyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgx%2FaP%2BgA9gbSfXIoKtwD6bJwislDz16%2F%2BebN2rT3i%2BvJnwFTioCr40oSI2nl4mQTcznYed9u0jh4g8GfSXV4btdLiHrGGLFREeKy9FvViZ8R1%2FhTatBDAOHt3ByhkF7LQxLNLzx1KS%2FJ3LPdDD280w5QXv3qu0CKd3XAB0xYxPZ47DO2Kls%2BvxJTdqFGgCs27uRVpRzvaeAX32tg8DQLfPY%2F9tWOTu7P11uPVj8cjI05%2FtLv98CykECr9EDpkSbrN%2Fp40rv196jptjQne0I4sUbuXRKDfUSS9D8eGbmMHBzZGekAjAqPvpD6flGdE72dWJSHyTsr2W7u6XphGnV%2FFQgWycbuhPo8DKVToxkqomgQky2XexhQyxlFM1%2FCXo51UH695anamS0XFStLcYfQrOtJRavHw%2BweilTgDgWAI%2B14SF%2BWgLBB%2FFfICI9h6AbGUjgPRfrGh%2FgTEAwr%2FTDNQhcGVCHfcqnAk52ZS3xFxdikbuDVMe%2Fb6eCY8l2z1%2B5WXsvHbm2u6uQARvbrhXJIjSHf5IQUNsB18OnSuF7qbeHyQYUUm8CWXMUi%2Br6seIQFFHdWqhfg1B02bEGmRXQt%2F%2FEli5CcOf2RgGw4whqSWByu2L%2BQWQlpL6Tulzz5krbtMOp%2FWbJRiUsp5hcwsrKbvQY6pgGqTJ4YZr7XlDQvb5sfDyC6qeRcPgDQr0imS%2FjGuA2%2F5P748J2EZvkUjiv%2BikM2IpvHWNxeZsgBiGi2FkQuHMkteTvtP3QtYsO3PTAJVR5ItD2y5Ki3zQ8Yn5hxNIrucyY%2BXnsNW1fCZQRM3doGE3sWCFi2RSQ4cXAcD3Q1MPgHPU7rJYHsKgZTred3EAjn9oH8Dxg%2BDC7mjeX4s%2B7sYFBiQmlRTriY&X-Amz-Signature=6b336e6ea35b2fd41afd42b6d2da8969af0f4965bfb79cabf1502f50e34f177c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEGTQXLI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIFivTuzmB2fHOCwiinjfwtiBe9GJN9NhOh4Bpv%2BBujJWAiAHlc8taL68Iwb1SyLOx553EghQcOQgmoU6afexmw3sjyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgx%2FaP%2BgA9gbSfXIoKtwD6bJwislDz16%2F%2BebN2rT3i%2BvJnwFTioCr40oSI2nl4mQTcznYed9u0jh4g8GfSXV4btdLiHrGGLFREeKy9FvViZ8R1%2FhTatBDAOHt3ByhkF7LQxLNLzx1KS%2FJ3LPdDD280w5QXv3qu0CKd3XAB0xYxPZ47DO2Kls%2BvxJTdqFGgCs27uRVpRzvaeAX32tg8DQLfPY%2F9tWOTu7P11uPVj8cjI05%2FtLv98CykECr9EDpkSbrN%2Fp40rv196jptjQne0I4sUbuXRKDfUSS9D8eGbmMHBzZGekAjAqPvpD6flGdE72dWJSHyTsr2W7u6XphGnV%2FFQgWycbuhPo8DKVToxkqomgQky2XexhQyxlFM1%2FCXo51UH695anamS0XFStLcYfQrOtJRavHw%2BweilTgDgWAI%2B14SF%2BWgLBB%2FFfICI9h6AbGUjgPRfrGh%2FgTEAwr%2FTDNQhcGVCHfcqnAk52ZS3xFxdikbuDVMe%2Fb6eCY8l2z1%2B5WXsvHbm2u6uQARvbrhXJIjSHf5IQUNsB18OnSuF7qbeHyQYUUm8CWXMUi%2Br6seIQFFHdWqhfg1B02bEGmRXQt%2F%2FEli5CcOf2RgGw4whqSWByu2L%2BQWQlpL6Tulzz5krbtMOp%2FWbJRiUsp5hcwsrKbvQY6pgGqTJ4YZr7XlDQvb5sfDyC6qeRcPgDQr0imS%2FjGuA2%2F5P748J2EZvkUjiv%2BikM2IpvHWNxeZsgBiGi2FkQuHMkteTvtP3QtYsO3PTAJVR5ItD2y5Ki3zQ8Yn5hxNIrucyY%2BXnsNW1fCZQRM3doGE3sWCFi2RSQ4cXAcD3Q1MPgHPU7rJYHsKgZTred3EAjn9oH8Dxg%2BDC7mjeX4s%2B7sYFBiQmlRTriY&X-Amz-Signature=00ba485cc1a0cc8291a3eca4ce75386beea98b4f69c6a41e80df7093e31480ca&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEGTQXLI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIFivTuzmB2fHOCwiinjfwtiBe9GJN9NhOh4Bpv%2BBujJWAiAHlc8taL68Iwb1SyLOx553EghQcOQgmoU6afexmw3sjyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgx%2FaP%2BgA9gbSfXIoKtwD6bJwislDz16%2F%2BebN2rT3i%2BvJnwFTioCr40oSI2nl4mQTcznYed9u0jh4g8GfSXV4btdLiHrGGLFREeKy9FvViZ8R1%2FhTatBDAOHt3ByhkF7LQxLNLzx1KS%2FJ3LPdDD280w5QXv3qu0CKd3XAB0xYxPZ47DO2Kls%2BvxJTdqFGgCs27uRVpRzvaeAX32tg8DQLfPY%2F9tWOTu7P11uPVj8cjI05%2FtLv98CykECr9EDpkSbrN%2Fp40rv196jptjQne0I4sUbuXRKDfUSS9D8eGbmMHBzZGekAjAqPvpD6flGdE72dWJSHyTsr2W7u6XphGnV%2FFQgWycbuhPo8DKVToxkqomgQky2XexhQyxlFM1%2FCXo51UH695anamS0XFStLcYfQrOtJRavHw%2BweilTgDgWAI%2B14SF%2BWgLBB%2FFfICI9h6AbGUjgPRfrGh%2FgTEAwr%2FTDNQhcGVCHfcqnAk52ZS3xFxdikbuDVMe%2Fb6eCY8l2z1%2B5WXsvHbm2u6uQARvbrhXJIjSHf5IQUNsB18OnSuF7qbeHyQYUUm8CWXMUi%2Br6seIQFFHdWqhfg1B02bEGmRXQt%2F%2FEli5CcOf2RgGw4whqSWByu2L%2BQWQlpL6Tulzz5krbtMOp%2FWbJRiUsp5hcwsrKbvQY6pgGqTJ4YZr7XlDQvb5sfDyC6qeRcPgDQr0imS%2FjGuA2%2F5P748J2EZvkUjiv%2BikM2IpvHWNxeZsgBiGi2FkQuHMkteTvtP3QtYsO3PTAJVR5ItD2y5Ki3zQ8Yn5hxNIrucyY%2BXnsNW1fCZQRM3doGE3sWCFi2RSQ4cXAcD3Q1MPgHPU7rJYHsKgZTred3EAjn9oH8Dxg%2BDC7mjeX4s%2B7sYFBiQmlRTriY&X-Amz-Signature=83f23a512293ece1deee956e7cff37f4d874d567ef301d148185305fc5698792&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4OMAZW4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIDW8uNwy6xzFVSq1EU6mOhHHKBCxc%2B1grqnp%2F%2FrNXLcMAiAcJazGwsgdgJzlrFMvV1ZM40xIZBnCxJK70d5%2FdcgHDyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBm%2FS9p6MGCTuuzK0KtwD6l1U4FFvnxKaS2eM5Zu4l4y0puO2H9hAsNkPdd%2BuH6GOmLXblNNzZ%2FmOC0j6xqmVcC08reD6TasJnYb6Y8UewZOHOaQsCBBLC9f%2Fqjs4MnnoF549LzVe4i3zkqlrweixSUBKFt1k4r5W0RJW14wzkxI5GvrAaaFkT2708q8xoR%2FlfwkGC4alhrnsij%2FzoX7Yi%2BnLuqR%2Fe1kLP1o8Yx%2FjiXrfZWEwDKVof1zBwJtqN8rPjNstTs2tU%2B8tmjfGP7Z2dNy24jA2gIW7pllRAOUrsjT8IqH2yeiPgKceOLcsoZnOoJnq4DE%2FmFu%2BAvjENZaaZu5RviVkg6y8Ua67gylDZBkkp%2Bl5G1DTlYIJJ%2BpdyqooZSP%2BwE0CdCGTlTy%2FnrRKykfnNNJfO6t1z0VFZV%2B0PdcGwcsrgcxaAXBxWriMNMJ3bkw%2FZVDbFQZEhSY98THwsiBuRvEWXs8eyWXBdi6gfnbnxhbOYH4TamnoVQYZGlwofMCnNNFoNjX66YP%2FFFcPRfKIOdME7Myyn8oC8bQWWf2ITGIgCYL5W6ZBRkIZsX%2BCeioAQv6COPX3SmiZNTB6h3VzjgWWmfxYeA9%2FUy5Aj8ANH0emvyMsCHYLTSKQl0wNIW2VPL0B9u%2FsmDQwlLKbvQY6pgF0l%2Fzkr0ytR4bZ8jk3JC1MbbUXj0ghE%2B%2FhBM5en%2Fze9EjsOroD07%2BIMcPPMT7pS2K2NkPE%2FXxNPXw8j%2BqYn1k6ra3r3J5ng7RmgzBU%2FDSfQKWVG4p5yvibxvepUrqBHRdvvlNFKa9kxI5pyMdQ0gh4xZCIHMe6m52%2FpNoWOIQqyUSZqT1GeSoieu2CiYIQiRoZRGSWkITsBccTBlIDRDZw3cgq%2FIbE&X-Amz-Signature=5130429983bac6fca0d69d1f7d4075e0c094d4cd28b4b7ae324f0c6a7446dab2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4OMAZW4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIDW8uNwy6xzFVSq1EU6mOhHHKBCxc%2B1grqnp%2F%2FrNXLcMAiAcJazGwsgdgJzlrFMvV1ZM40xIZBnCxJK70d5%2FdcgHDyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBm%2FS9p6MGCTuuzK0KtwD6l1U4FFvnxKaS2eM5Zu4l4y0puO2H9hAsNkPdd%2BuH6GOmLXblNNzZ%2FmOC0j6xqmVcC08reD6TasJnYb6Y8UewZOHOaQsCBBLC9f%2Fqjs4MnnoF549LzVe4i3zkqlrweixSUBKFt1k4r5W0RJW14wzkxI5GvrAaaFkT2708q8xoR%2FlfwkGC4alhrnsij%2FzoX7Yi%2BnLuqR%2Fe1kLP1o8Yx%2FjiXrfZWEwDKVof1zBwJtqN8rPjNstTs2tU%2B8tmjfGP7Z2dNy24jA2gIW7pllRAOUrsjT8IqH2yeiPgKceOLcsoZnOoJnq4DE%2FmFu%2BAvjENZaaZu5RviVkg6y8Ua67gylDZBkkp%2Bl5G1DTlYIJJ%2BpdyqooZSP%2BwE0CdCGTlTy%2FnrRKykfnNNJfO6t1z0VFZV%2B0PdcGwcsrgcxaAXBxWriMNMJ3bkw%2FZVDbFQZEhSY98THwsiBuRvEWXs8eyWXBdi6gfnbnxhbOYH4TamnoVQYZGlwofMCnNNFoNjX66YP%2FFFcPRfKIOdME7Myyn8oC8bQWWf2ITGIgCYL5W6ZBRkIZsX%2BCeioAQv6COPX3SmiZNTB6h3VzjgWWmfxYeA9%2FUy5Aj8ANH0emvyMsCHYLTSKQl0wNIW2VPL0B9u%2FsmDQwlLKbvQY6pgF0l%2Fzkr0ytR4bZ8jk3JC1MbbUXj0ghE%2B%2FhBM5en%2Fze9EjsOroD07%2BIMcPPMT7pS2K2NkPE%2FXxNPXw8j%2BqYn1k6ra3r3J5ng7RmgzBU%2FDSfQKWVG4p5yvibxvepUrqBHRdvvlNFKa9kxI5pyMdQ0gh4xZCIHMe6m52%2FpNoWOIQqyUSZqT1GeSoieu2CiYIQiRoZRGSWkITsBccTBlIDRDZw3cgq%2FIbE&X-Amz-Signature=3d2dc5cfc3180feee1af5a45cd3aff085574248d4920ca25e1727722abf4eaa7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4OMAZW4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIDW8uNwy6xzFVSq1EU6mOhHHKBCxc%2B1grqnp%2F%2FrNXLcMAiAcJazGwsgdgJzlrFMvV1ZM40xIZBnCxJK70d5%2FdcgHDyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBm%2FS9p6MGCTuuzK0KtwD6l1U4FFvnxKaS2eM5Zu4l4y0puO2H9hAsNkPdd%2BuH6GOmLXblNNzZ%2FmOC0j6xqmVcC08reD6TasJnYb6Y8UewZOHOaQsCBBLC9f%2Fqjs4MnnoF549LzVe4i3zkqlrweixSUBKFt1k4r5W0RJW14wzkxI5GvrAaaFkT2708q8xoR%2FlfwkGC4alhrnsij%2FzoX7Yi%2BnLuqR%2Fe1kLP1o8Yx%2FjiXrfZWEwDKVof1zBwJtqN8rPjNstTs2tU%2B8tmjfGP7Z2dNy24jA2gIW7pllRAOUrsjT8IqH2yeiPgKceOLcsoZnOoJnq4DE%2FmFu%2BAvjENZaaZu5RviVkg6y8Ua67gylDZBkkp%2Bl5G1DTlYIJJ%2BpdyqooZSP%2BwE0CdCGTlTy%2FnrRKykfnNNJfO6t1z0VFZV%2B0PdcGwcsrgcxaAXBxWriMNMJ3bkw%2FZVDbFQZEhSY98THwsiBuRvEWXs8eyWXBdi6gfnbnxhbOYH4TamnoVQYZGlwofMCnNNFoNjX66YP%2FFFcPRfKIOdME7Myyn8oC8bQWWf2ITGIgCYL5W6ZBRkIZsX%2BCeioAQv6COPX3SmiZNTB6h3VzjgWWmfxYeA9%2FUy5Aj8ANH0emvyMsCHYLTSKQl0wNIW2VPL0B9u%2FsmDQwlLKbvQY6pgF0l%2Fzkr0ytR4bZ8jk3JC1MbbUXj0ghE%2B%2FhBM5en%2Fze9EjsOroD07%2BIMcPPMT7pS2K2NkPE%2FXxNPXw8j%2BqYn1k6ra3r3J5ng7RmgzBU%2FDSfQKWVG4p5yvibxvepUrqBHRdvvlNFKa9kxI5pyMdQ0gh4xZCIHMe6m52%2FpNoWOIQqyUSZqT1GeSoieu2CiYIQiRoZRGSWkITsBccTBlIDRDZw3cgq%2FIbE&X-Amz-Signature=598428111d8f738d8fa8e0bb3b5935e99cee493f16b703addfe3ed72ff5dfb93&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4OMAZW4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIDW8uNwy6xzFVSq1EU6mOhHHKBCxc%2B1grqnp%2F%2FrNXLcMAiAcJazGwsgdgJzlrFMvV1ZM40xIZBnCxJK70d5%2FdcgHDyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBm%2FS9p6MGCTuuzK0KtwD6l1U4FFvnxKaS2eM5Zu4l4y0puO2H9hAsNkPdd%2BuH6GOmLXblNNzZ%2FmOC0j6xqmVcC08reD6TasJnYb6Y8UewZOHOaQsCBBLC9f%2Fqjs4MnnoF549LzVe4i3zkqlrweixSUBKFt1k4r5W0RJW14wzkxI5GvrAaaFkT2708q8xoR%2FlfwkGC4alhrnsij%2FzoX7Yi%2BnLuqR%2Fe1kLP1o8Yx%2FjiXrfZWEwDKVof1zBwJtqN8rPjNstTs2tU%2B8tmjfGP7Z2dNy24jA2gIW7pllRAOUrsjT8IqH2yeiPgKceOLcsoZnOoJnq4DE%2FmFu%2BAvjENZaaZu5RviVkg6y8Ua67gylDZBkkp%2Bl5G1DTlYIJJ%2BpdyqooZSP%2BwE0CdCGTlTy%2FnrRKykfnNNJfO6t1z0VFZV%2B0PdcGwcsrgcxaAXBxWriMNMJ3bkw%2FZVDbFQZEhSY98THwsiBuRvEWXs8eyWXBdi6gfnbnxhbOYH4TamnoVQYZGlwofMCnNNFoNjX66YP%2FFFcPRfKIOdME7Myyn8oC8bQWWf2ITGIgCYL5W6ZBRkIZsX%2BCeioAQv6COPX3SmiZNTB6h3VzjgWWmfxYeA9%2FUy5Aj8ANH0emvyMsCHYLTSKQl0wNIW2VPL0B9u%2FsmDQwlLKbvQY6pgF0l%2Fzkr0ytR4bZ8jk3JC1MbbUXj0ghE%2B%2FhBM5en%2Fze9EjsOroD07%2BIMcPPMT7pS2K2NkPE%2FXxNPXw8j%2BqYn1k6ra3r3J5ng7RmgzBU%2FDSfQKWVG4p5yvibxvepUrqBHRdvvlNFKa9kxI5pyMdQ0gh4xZCIHMe6m52%2FpNoWOIQqyUSZqT1GeSoieu2CiYIQiRoZRGSWkITsBccTBlIDRDZw3cgq%2FIbE&X-Amz-Signature=6e4939b203eca7cafc5cef6c999512f0b06f9763682f38976d3c75c66a430c88&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4OMAZW4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIDW8uNwy6xzFVSq1EU6mOhHHKBCxc%2B1grqnp%2F%2FrNXLcMAiAcJazGwsgdgJzlrFMvV1ZM40xIZBnCxJK70d5%2FdcgHDyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBm%2FS9p6MGCTuuzK0KtwD6l1U4FFvnxKaS2eM5Zu4l4y0puO2H9hAsNkPdd%2BuH6GOmLXblNNzZ%2FmOC0j6xqmVcC08reD6TasJnYb6Y8UewZOHOaQsCBBLC9f%2Fqjs4MnnoF549LzVe4i3zkqlrweixSUBKFt1k4r5W0RJW14wzkxI5GvrAaaFkT2708q8xoR%2FlfwkGC4alhrnsij%2FzoX7Yi%2BnLuqR%2Fe1kLP1o8Yx%2FjiXrfZWEwDKVof1zBwJtqN8rPjNstTs2tU%2B8tmjfGP7Z2dNy24jA2gIW7pllRAOUrsjT8IqH2yeiPgKceOLcsoZnOoJnq4DE%2FmFu%2BAvjENZaaZu5RviVkg6y8Ua67gylDZBkkp%2Bl5G1DTlYIJJ%2BpdyqooZSP%2BwE0CdCGTlTy%2FnrRKykfnNNJfO6t1z0VFZV%2B0PdcGwcsrgcxaAXBxWriMNMJ3bkw%2FZVDbFQZEhSY98THwsiBuRvEWXs8eyWXBdi6gfnbnxhbOYH4TamnoVQYZGlwofMCnNNFoNjX66YP%2FFFcPRfKIOdME7Myyn8oC8bQWWf2ITGIgCYL5W6ZBRkIZsX%2BCeioAQv6COPX3SmiZNTB6h3VzjgWWmfxYeA9%2FUy5Aj8ANH0emvyMsCHYLTSKQl0wNIW2VPL0B9u%2FsmDQwlLKbvQY6pgF0l%2Fzkr0ytR4bZ8jk3JC1MbbUXj0ghE%2B%2FhBM5en%2Fze9EjsOroD07%2BIMcPPMT7pS2K2NkPE%2FXxNPXw8j%2BqYn1k6ra3r3J5ng7RmgzBU%2FDSfQKWVG4p5yvibxvepUrqBHRdvvlNFKa9kxI5pyMdQ0gh4xZCIHMe6m52%2FpNoWOIQqyUSZqT1GeSoieu2CiYIQiRoZRGSWkITsBccTBlIDRDZw3cgq%2FIbE&X-Amz-Signature=2a4de0a3c53c79a460ca4280cd897dccf991f212d20ea1640df9be31557a6e70&X-Amz-SignedHeaders=host&x-id=GetObject)
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


