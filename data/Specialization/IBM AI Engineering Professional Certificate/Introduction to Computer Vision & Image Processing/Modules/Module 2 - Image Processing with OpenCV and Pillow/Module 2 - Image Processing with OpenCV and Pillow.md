

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZORQIEO5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnB%2FqoA%2FlXfuCqS4drPmA2RmcqhJ%2BdXqAHaBCqJbjj%2BwIhAOErRik9hSwJYv9kYAVbyM%2B5sLMROASbMF5kves3b5PGKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyowPMlgEek0VbIUMUq3APLg0%2FW5I973MMhXQ3s%2FSYMRC2vEeskbjYf%2BMWzUVvLDrgYR2HPeZnivptSUmFarbdHMxUpS0nZOalNcnOsNv40M0vbR8OguZOlSt3Bm50XLYpGo7M4vaiJiD6GvMpxxXsOKedk%2BfXCCQbR9gOpXGtdUJL0Tlpd1pxRaWBjT3Tp9ww31o2AYX6DSibqEjx%2BILvSgdX2IdkHOhQTV4vE9kVLoy30CjP4VCr9Wm94jLso%2BB484zE8ykYd3Z6vd%2FRSBROfOh5WCHA1QDzHzrHFh6Kn87ciO039OWPbx69DW6ni%2BaOfQaYsB28%2F99d%2B16gUlGOAM1SK6%2BHSLnyx3NZel2lAsZGvFEEFcBNM9wjFH5wx%2FyMegsyu4npHLAhEe0mD5lHzGSJPEL8P4%2F2qg23SjuUArvwJvGwAQf%2Fq7ti3A9ByROCytBrmqhPOsJQoYm6XlmdCHW1vFz8mGHIr4yzzqG93vjFMaHF1RAZ845uxm32fpdWha1f9vPtDx5db6OEFh3OjKTypfyfwcO5DQwT6wtAtMS2ZgCwUWtObiQkrDr2%2Bm8%2FhEUV%2Bk2hrU%2FXUGqPFgEWwRT3Ylk3%2BfcVzHpcR1ViA4obmaU8%2BDsd9seqXpE5x0csQnXuRlJ0j0NckfTCM%2F%2Be8BjqkAVd%2FzLxG3%2BnBSj675x7NngLzRwdioE45ZyWIODpY7GMxlQmyYQfHV6uE1PWYsBrXPQG3jA9cswgzbrWrYPUb7n330MNDIvMF40GhI6L0Abu31ymDrtQDbB5DvO%2BuHE2Dk4t9nbNw8ijIEJEWpqmvRgX5QhHCno2dnhOUZXvpXNDDIFjTKdIVzyGrLNJ8iAxCO73ZMgBkeVeRcRLnXR8CSMwD%2Bwkm&X-Amz-Signature=8f659f9123378b71620770254729e726178d3a83d2739b299378cc4afa1a8ad1&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ232RGN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICghd%2F4jKuiIV6z20fAPda2%2BhbJ%2BbSxXbV%2FAEM%2F7vTbkAiBQK5J2NpIBFHLpaKQ9UDtgGC9QVMryd4Y4JA%2BblGtJvCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWZzkHGlCqsmuGAFXKtwDJP6cMzflfz%2F9nBds86a27ZUUz3O9rX9cDwPWhQEtySmlwOASSWn140v3TJxEmoy%2FataUN4RGB4dUMJlZ8mGz2ATs4rTwq6VbLNusJLv35IZ8Lv7vobvFPWmcgB1fSrv7d96WAflgHz%2FQFe0GQ5KI%2BkvhiFFQhtEU3gEGwMy2RkOga3cY71bOzBvdAe1sLhzhz%2BNYw91SxAYFoYXiYld86ve8Y%2BsfJG3W94%2F351Y1A77STYIGQ%2F%2Fbg%2Br11OoS8DwIGZTFlYeSjis4rkZBvCfJp3%2F1K7dv7xE4WECj7f8oFb0wE5YFQM1uhQousuzWsWgYE8e%2Fg6TuvkdxjecR1ezpQ%2FP16k1nZulLuiOZ8J%2FQTHfboz%2Fl3txLBMe%2BJs%2F%2FfYnfnmIeD6%2BY2GUlYt1kZB9K%2F0ZL0GDKRyyxU8G4HuuvWpApPex2ApVEEiEUxNQS9z3HHU6zdNYwDnF%2BRDJLg9WxwqsIMsoHNhxOpPJZY4ljAK2edra1va7DxO0tvimO3hR%2BRBKHrJGJO%2BqU0ovAdTDTUcjGIIbLaqoZErebz0wX2WzBZZhpW2%2BouUB51SulFhfKPv0EEBSqt9pIVkzEBnpBskFdiBKKpzphZ9cNqoinV0v3lMMMuAh8Pl1FWEQwzIDovAY6pgFFIPoV3GZ36dYAkQTuVzxOxvojmryqHzzeDPUooj2najBEU3ValXbwTcDhynRd82aRadYIFALX3%2BKvQdST%2FSXiR3CqdFJoLUuivmHsUjGpJUHktGLCsQ5rupzsmE%2BgwNF5L8zNIofKh6GxNKpG3H9LLEtzZxVP%2Fd6c5aif0wkV8L%2BWG0u9JxwX3YaO9rSKDMCOosHB4%2BCpgGZYO3LjaU1m7l3VoOCL&X-Amz-Signature=ebb93f8fb9fcdbbbff02936163912e0a796e0456affdbc2df94ea3000c3ca95a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ232RGN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICghd%2F4jKuiIV6z20fAPda2%2BhbJ%2BbSxXbV%2FAEM%2F7vTbkAiBQK5J2NpIBFHLpaKQ9UDtgGC9QVMryd4Y4JA%2BblGtJvCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWZzkHGlCqsmuGAFXKtwDJP6cMzflfz%2F9nBds86a27ZUUz3O9rX9cDwPWhQEtySmlwOASSWn140v3TJxEmoy%2FataUN4RGB4dUMJlZ8mGz2ATs4rTwq6VbLNusJLv35IZ8Lv7vobvFPWmcgB1fSrv7d96WAflgHz%2FQFe0GQ5KI%2BkvhiFFQhtEU3gEGwMy2RkOga3cY71bOzBvdAe1sLhzhz%2BNYw91SxAYFoYXiYld86ve8Y%2BsfJG3W94%2F351Y1A77STYIGQ%2F%2Fbg%2Br11OoS8DwIGZTFlYeSjis4rkZBvCfJp3%2F1K7dv7xE4WECj7f8oFb0wE5YFQM1uhQousuzWsWgYE8e%2Fg6TuvkdxjecR1ezpQ%2FP16k1nZulLuiOZ8J%2FQTHfboz%2Fl3txLBMe%2BJs%2F%2FfYnfnmIeD6%2BY2GUlYt1kZB9K%2F0ZL0GDKRyyxU8G4HuuvWpApPex2ApVEEiEUxNQS9z3HHU6zdNYwDnF%2BRDJLg9WxwqsIMsoHNhxOpPJZY4ljAK2edra1va7DxO0tvimO3hR%2BRBKHrJGJO%2BqU0ovAdTDTUcjGIIbLaqoZErebz0wX2WzBZZhpW2%2BouUB51SulFhfKPv0EEBSqt9pIVkzEBnpBskFdiBKKpzphZ9cNqoinV0v3lMMMuAh8Pl1FWEQwzIDovAY6pgFFIPoV3GZ36dYAkQTuVzxOxvojmryqHzzeDPUooj2najBEU3ValXbwTcDhynRd82aRadYIFALX3%2BKvQdST%2FSXiR3CqdFJoLUuivmHsUjGpJUHktGLCsQ5rupzsmE%2BgwNF5L8zNIofKh6GxNKpG3H9LLEtzZxVP%2Fd6c5aif0wkV8L%2BWG0u9JxwX3YaO9rSKDMCOosHB4%2BCpgGZYO3LjaU1m7l3VoOCL&X-Amz-Signature=5154a508a646767fda10a0d89ff8cbf6feecb818534db368c8cd7432832d7c58&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ232RGN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICghd%2F4jKuiIV6z20fAPda2%2BhbJ%2BbSxXbV%2FAEM%2F7vTbkAiBQK5J2NpIBFHLpaKQ9UDtgGC9QVMryd4Y4JA%2BblGtJvCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWZzkHGlCqsmuGAFXKtwDJP6cMzflfz%2F9nBds86a27ZUUz3O9rX9cDwPWhQEtySmlwOASSWn140v3TJxEmoy%2FataUN4RGB4dUMJlZ8mGz2ATs4rTwq6VbLNusJLv35IZ8Lv7vobvFPWmcgB1fSrv7d96WAflgHz%2FQFe0GQ5KI%2BkvhiFFQhtEU3gEGwMy2RkOga3cY71bOzBvdAe1sLhzhz%2BNYw91SxAYFoYXiYld86ve8Y%2BsfJG3W94%2F351Y1A77STYIGQ%2F%2Fbg%2Br11OoS8DwIGZTFlYeSjis4rkZBvCfJp3%2F1K7dv7xE4WECj7f8oFb0wE5YFQM1uhQousuzWsWgYE8e%2Fg6TuvkdxjecR1ezpQ%2FP16k1nZulLuiOZ8J%2FQTHfboz%2Fl3txLBMe%2BJs%2F%2FfYnfnmIeD6%2BY2GUlYt1kZB9K%2F0ZL0GDKRyyxU8G4HuuvWpApPex2ApVEEiEUxNQS9z3HHU6zdNYwDnF%2BRDJLg9WxwqsIMsoHNhxOpPJZY4ljAK2edra1va7DxO0tvimO3hR%2BRBKHrJGJO%2BqU0ovAdTDTUcjGIIbLaqoZErebz0wX2WzBZZhpW2%2BouUB51SulFhfKPv0EEBSqt9pIVkzEBnpBskFdiBKKpzphZ9cNqoinV0v3lMMMuAh8Pl1FWEQwzIDovAY6pgFFIPoV3GZ36dYAkQTuVzxOxvojmryqHzzeDPUooj2najBEU3ValXbwTcDhynRd82aRadYIFALX3%2BKvQdST%2FSXiR3CqdFJoLUuivmHsUjGpJUHktGLCsQ5rupzsmE%2BgwNF5L8zNIofKh6GxNKpG3H9LLEtzZxVP%2Fd6c5aif0wkV8L%2BWG0u9JxwX3YaO9rSKDMCOosHB4%2BCpgGZYO3LjaU1m7l3VoOCL&X-Amz-Signature=692c544820f39e5656044b6f1a5bcda8f5bcb6d64ce2c1870dcb5afaf7a76c53&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ232RGN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICghd%2F4jKuiIV6z20fAPda2%2BhbJ%2BbSxXbV%2FAEM%2F7vTbkAiBQK5J2NpIBFHLpaKQ9UDtgGC9QVMryd4Y4JA%2BblGtJvCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWZzkHGlCqsmuGAFXKtwDJP6cMzflfz%2F9nBds86a27ZUUz3O9rX9cDwPWhQEtySmlwOASSWn140v3TJxEmoy%2FataUN4RGB4dUMJlZ8mGz2ATs4rTwq6VbLNusJLv35IZ8Lv7vobvFPWmcgB1fSrv7d96WAflgHz%2FQFe0GQ5KI%2BkvhiFFQhtEU3gEGwMy2RkOga3cY71bOzBvdAe1sLhzhz%2BNYw91SxAYFoYXiYld86ve8Y%2BsfJG3W94%2F351Y1A77STYIGQ%2F%2Fbg%2Br11OoS8DwIGZTFlYeSjis4rkZBvCfJp3%2F1K7dv7xE4WECj7f8oFb0wE5YFQM1uhQousuzWsWgYE8e%2Fg6TuvkdxjecR1ezpQ%2FP16k1nZulLuiOZ8J%2FQTHfboz%2Fl3txLBMe%2BJs%2F%2FfYnfnmIeD6%2BY2GUlYt1kZB9K%2F0ZL0GDKRyyxU8G4HuuvWpApPex2ApVEEiEUxNQS9z3HHU6zdNYwDnF%2BRDJLg9WxwqsIMsoHNhxOpPJZY4ljAK2edra1va7DxO0tvimO3hR%2BRBKHrJGJO%2BqU0ovAdTDTUcjGIIbLaqoZErebz0wX2WzBZZhpW2%2BouUB51SulFhfKPv0EEBSqt9pIVkzEBnpBskFdiBKKpzphZ9cNqoinV0v3lMMMuAh8Pl1FWEQwzIDovAY6pgFFIPoV3GZ36dYAkQTuVzxOxvojmryqHzzeDPUooj2najBEU3ValXbwTcDhynRd82aRadYIFALX3%2BKvQdST%2FSXiR3CqdFJoLUuivmHsUjGpJUHktGLCsQ5rupzsmE%2BgwNF5L8zNIofKh6GxNKpG3H9LLEtzZxVP%2Fd6c5aif0wkV8L%2BWG0u9JxwX3YaO9rSKDMCOosHB4%2BCpgGZYO3LjaU1m7l3VoOCL&X-Amz-Signature=8e9a6f8082bb274d76d6cea8b05f4e00e7892d586911064dc50de33294e1c8d4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ232RGN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICghd%2F4jKuiIV6z20fAPda2%2BhbJ%2BbSxXbV%2FAEM%2F7vTbkAiBQK5J2NpIBFHLpaKQ9UDtgGC9QVMryd4Y4JA%2BblGtJvCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWZzkHGlCqsmuGAFXKtwDJP6cMzflfz%2F9nBds86a27ZUUz3O9rX9cDwPWhQEtySmlwOASSWn140v3TJxEmoy%2FataUN4RGB4dUMJlZ8mGz2ATs4rTwq6VbLNusJLv35IZ8Lv7vobvFPWmcgB1fSrv7d96WAflgHz%2FQFe0GQ5KI%2BkvhiFFQhtEU3gEGwMy2RkOga3cY71bOzBvdAe1sLhzhz%2BNYw91SxAYFoYXiYld86ve8Y%2BsfJG3W94%2F351Y1A77STYIGQ%2F%2Fbg%2Br11OoS8DwIGZTFlYeSjis4rkZBvCfJp3%2F1K7dv7xE4WECj7f8oFb0wE5YFQM1uhQousuzWsWgYE8e%2Fg6TuvkdxjecR1ezpQ%2FP16k1nZulLuiOZ8J%2FQTHfboz%2Fl3txLBMe%2BJs%2F%2FfYnfnmIeD6%2BY2GUlYt1kZB9K%2F0ZL0GDKRyyxU8G4HuuvWpApPex2ApVEEiEUxNQS9z3HHU6zdNYwDnF%2BRDJLg9WxwqsIMsoHNhxOpPJZY4ljAK2edra1va7DxO0tvimO3hR%2BRBKHrJGJO%2BqU0ovAdTDTUcjGIIbLaqoZErebz0wX2WzBZZhpW2%2BouUB51SulFhfKPv0EEBSqt9pIVkzEBnpBskFdiBKKpzphZ9cNqoinV0v3lMMMuAh8Pl1FWEQwzIDovAY6pgFFIPoV3GZ36dYAkQTuVzxOxvojmryqHzzeDPUooj2najBEU3ValXbwTcDhynRd82aRadYIFALX3%2BKvQdST%2FSXiR3CqdFJoLUuivmHsUjGpJUHktGLCsQ5rupzsmE%2BgwNF5L8zNIofKh6GxNKpG3H9LLEtzZxVP%2Fd6c5aif0wkV8L%2BWG0u9JxwX3YaO9rSKDMCOosHB4%2BCpgGZYO3LjaU1m7l3VoOCL&X-Amz-Signature=238995407785e1c676790f1bc29e2937c322dafe346e1a1daa6ecf95cf228e8d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZORQIEO5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnB%2FqoA%2FlXfuCqS4drPmA2RmcqhJ%2BdXqAHaBCqJbjj%2BwIhAOErRik9hSwJYv9kYAVbyM%2B5sLMROASbMF5kves3b5PGKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyowPMlgEek0VbIUMUq3APLg0%2FW5I973MMhXQ3s%2FSYMRC2vEeskbjYf%2BMWzUVvLDrgYR2HPeZnivptSUmFarbdHMxUpS0nZOalNcnOsNv40M0vbR8OguZOlSt3Bm50XLYpGo7M4vaiJiD6GvMpxxXsOKedk%2BfXCCQbR9gOpXGtdUJL0Tlpd1pxRaWBjT3Tp9ww31o2AYX6DSibqEjx%2BILvSgdX2IdkHOhQTV4vE9kVLoy30CjP4VCr9Wm94jLso%2BB484zE8ykYd3Z6vd%2FRSBROfOh5WCHA1QDzHzrHFh6Kn87ciO039OWPbx69DW6ni%2BaOfQaYsB28%2F99d%2B16gUlGOAM1SK6%2BHSLnyx3NZel2lAsZGvFEEFcBNM9wjFH5wx%2FyMegsyu4npHLAhEe0mD5lHzGSJPEL8P4%2F2qg23SjuUArvwJvGwAQf%2Fq7ti3A9ByROCytBrmqhPOsJQoYm6XlmdCHW1vFz8mGHIr4yzzqG93vjFMaHF1RAZ845uxm32fpdWha1f9vPtDx5db6OEFh3OjKTypfyfwcO5DQwT6wtAtMS2ZgCwUWtObiQkrDr2%2Bm8%2FhEUV%2Bk2hrU%2FXUGqPFgEWwRT3Ylk3%2BfcVzHpcR1ViA4obmaU8%2BDsd9seqXpE5x0csQnXuRlJ0j0NckfTCM%2F%2Be8BjqkAVd%2FzLxG3%2BnBSj675x7NngLzRwdioE45ZyWIODpY7GMxlQmyYQfHV6uE1PWYsBrXPQG3jA9cswgzbrWrYPUb7n330MNDIvMF40GhI6L0Abu31ymDrtQDbB5DvO%2BuHE2Dk4t9nbNw8ijIEJEWpqmvRgX5QhHCno2dnhOUZXvpXNDDIFjTKdIVzyGrLNJ8iAxCO73ZMgBkeVeRcRLnXR8CSMwD%2Bwkm&X-Amz-Signature=dcd6059d6ca21c2a96cba1624234d5892b01e6a7706cae9983f70e62672b0db0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZORQIEO5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnB%2FqoA%2FlXfuCqS4drPmA2RmcqhJ%2BdXqAHaBCqJbjj%2BwIhAOErRik9hSwJYv9kYAVbyM%2B5sLMROASbMF5kves3b5PGKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyowPMlgEek0VbIUMUq3APLg0%2FW5I973MMhXQ3s%2FSYMRC2vEeskbjYf%2BMWzUVvLDrgYR2HPeZnivptSUmFarbdHMxUpS0nZOalNcnOsNv40M0vbR8OguZOlSt3Bm50XLYpGo7M4vaiJiD6GvMpxxXsOKedk%2BfXCCQbR9gOpXGtdUJL0Tlpd1pxRaWBjT3Tp9ww31o2AYX6DSibqEjx%2BILvSgdX2IdkHOhQTV4vE9kVLoy30CjP4VCr9Wm94jLso%2BB484zE8ykYd3Z6vd%2FRSBROfOh5WCHA1QDzHzrHFh6Kn87ciO039OWPbx69DW6ni%2BaOfQaYsB28%2F99d%2B16gUlGOAM1SK6%2BHSLnyx3NZel2lAsZGvFEEFcBNM9wjFH5wx%2FyMegsyu4npHLAhEe0mD5lHzGSJPEL8P4%2F2qg23SjuUArvwJvGwAQf%2Fq7ti3A9ByROCytBrmqhPOsJQoYm6XlmdCHW1vFz8mGHIr4yzzqG93vjFMaHF1RAZ845uxm32fpdWha1f9vPtDx5db6OEFh3OjKTypfyfwcO5DQwT6wtAtMS2ZgCwUWtObiQkrDr2%2Bm8%2FhEUV%2Bk2hrU%2FXUGqPFgEWwRT3Ylk3%2BfcVzHpcR1ViA4obmaU8%2BDsd9seqXpE5x0csQnXuRlJ0j0NckfTCM%2F%2Be8BjqkAVd%2FzLxG3%2BnBSj675x7NngLzRwdioE45ZyWIODpY7GMxlQmyYQfHV6uE1PWYsBrXPQG3jA9cswgzbrWrYPUb7n330MNDIvMF40GhI6L0Abu31ymDrtQDbB5DvO%2BuHE2Dk4t9nbNw8ijIEJEWpqmvRgX5QhHCno2dnhOUZXvpXNDDIFjTKdIVzyGrLNJ8iAxCO73ZMgBkeVeRcRLnXR8CSMwD%2Bwkm&X-Amz-Signature=250375842a704e5e61ce92e897fc479767714f4b717c9aae9c97bdd14ba2183e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZORQIEO5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnB%2FqoA%2FlXfuCqS4drPmA2RmcqhJ%2BdXqAHaBCqJbjj%2BwIhAOErRik9hSwJYv9kYAVbyM%2B5sLMROASbMF5kves3b5PGKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyowPMlgEek0VbIUMUq3APLg0%2FW5I973MMhXQ3s%2FSYMRC2vEeskbjYf%2BMWzUVvLDrgYR2HPeZnivptSUmFarbdHMxUpS0nZOalNcnOsNv40M0vbR8OguZOlSt3Bm50XLYpGo7M4vaiJiD6GvMpxxXsOKedk%2BfXCCQbR9gOpXGtdUJL0Tlpd1pxRaWBjT3Tp9ww31o2AYX6DSibqEjx%2BILvSgdX2IdkHOhQTV4vE9kVLoy30CjP4VCr9Wm94jLso%2BB484zE8ykYd3Z6vd%2FRSBROfOh5WCHA1QDzHzrHFh6Kn87ciO039OWPbx69DW6ni%2BaOfQaYsB28%2F99d%2B16gUlGOAM1SK6%2BHSLnyx3NZel2lAsZGvFEEFcBNM9wjFH5wx%2FyMegsyu4npHLAhEe0mD5lHzGSJPEL8P4%2F2qg23SjuUArvwJvGwAQf%2Fq7ti3A9ByROCytBrmqhPOsJQoYm6XlmdCHW1vFz8mGHIr4yzzqG93vjFMaHF1RAZ845uxm32fpdWha1f9vPtDx5db6OEFh3OjKTypfyfwcO5DQwT6wtAtMS2ZgCwUWtObiQkrDr2%2Bm8%2FhEUV%2Bk2hrU%2FXUGqPFgEWwRT3Ylk3%2BfcVzHpcR1ViA4obmaU8%2BDsd9seqXpE5x0csQnXuRlJ0j0NckfTCM%2F%2Be8BjqkAVd%2FzLxG3%2BnBSj675x7NngLzRwdioE45ZyWIODpY7GMxlQmyYQfHV6uE1PWYsBrXPQG3jA9cswgzbrWrYPUb7n330MNDIvMF40GhI6L0Abu31ymDrtQDbB5DvO%2BuHE2Dk4t9nbNw8ijIEJEWpqmvRgX5QhHCno2dnhOUZXvpXNDDIFjTKdIVzyGrLNJ8iAxCO73ZMgBkeVeRcRLnXR8CSMwD%2Bwkm&X-Amz-Signature=5ea07e2ae19b702263b0215f551c6c14366f997beecd2570b2678fe6634fc397&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZORQIEO5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnB%2FqoA%2FlXfuCqS4drPmA2RmcqhJ%2BdXqAHaBCqJbjj%2BwIhAOErRik9hSwJYv9kYAVbyM%2B5sLMROASbMF5kves3b5PGKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyowPMlgEek0VbIUMUq3APLg0%2FW5I973MMhXQ3s%2FSYMRC2vEeskbjYf%2BMWzUVvLDrgYR2HPeZnivptSUmFarbdHMxUpS0nZOalNcnOsNv40M0vbR8OguZOlSt3Bm50XLYpGo7M4vaiJiD6GvMpxxXsOKedk%2BfXCCQbR9gOpXGtdUJL0Tlpd1pxRaWBjT3Tp9ww31o2AYX6DSibqEjx%2BILvSgdX2IdkHOhQTV4vE9kVLoy30CjP4VCr9Wm94jLso%2BB484zE8ykYd3Z6vd%2FRSBROfOh5WCHA1QDzHzrHFh6Kn87ciO039OWPbx69DW6ni%2BaOfQaYsB28%2F99d%2B16gUlGOAM1SK6%2BHSLnyx3NZel2lAsZGvFEEFcBNM9wjFH5wx%2FyMegsyu4npHLAhEe0mD5lHzGSJPEL8P4%2F2qg23SjuUArvwJvGwAQf%2Fq7ti3A9ByROCytBrmqhPOsJQoYm6XlmdCHW1vFz8mGHIr4yzzqG93vjFMaHF1RAZ845uxm32fpdWha1f9vPtDx5db6OEFh3OjKTypfyfwcO5DQwT6wtAtMS2ZgCwUWtObiQkrDr2%2Bm8%2FhEUV%2Bk2hrU%2FXUGqPFgEWwRT3Ylk3%2BfcVzHpcR1ViA4obmaU8%2BDsd9seqXpE5x0csQnXuRlJ0j0NckfTCM%2F%2Be8BjqkAVd%2FzLxG3%2BnBSj675x7NngLzRwdioE45ZyWIODpY7GMxlQmyYQfHV6uE1PWYsBrXPQG3jA9cswgzbrWrYPUb7n330MNDIvMF40GhI6L0Abu31ymDrtQDbB5DvO%2BuHE2Dk4t9nbNw8ijIEJEWpqmvRgX5QhHCno2dnhOUZXvpXNDDIFjTKdIVzyGrLNJ8iAxCO73ZMgBkeVeRcRLnXR8CSMwD%2Bwkm&X-Amz-Signature=80a9d553089108605d9089c95e365d0a4fb2d110d3edb9c35dd6089caef316a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZORQIEO5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnB%2FqoA%2FlXfuCqS4drPmA2RmcqhJ%2BdXqAHaBCqJbjj%2BwIhAOErRik9hSwJYv9kYAVbyM%2B5sLMROASbMF5kves3b5PGKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyowPMlgEek0VbIUMUq3APLg0%2FW5I973MMhXQ3s%2FSYMRC2vEeskbjYf%2BMWzUVvLDrgYR2HPeZnivptSUmFarbdHMxUpS0nZOalNcnOsNv40M0vbR8OguZOlSt3Bm50XLYpGo7M4vaiJiD6GvMpxxXsOKedk%2BfXCCQbR9gOpXGtdUJL0Tlpd1pxRaWBjT3Tp9ww31o2AYX6DSibqEjx%2BILvSgdX2IdkHOhQTV4vE9kVLoy30CjP4VCr9Wm94jLso%2BB484zE8ykYd3Z6vd%2FRSBROfOh5WCHA1QDzHzrHFh6Kn87ciO039OWPbx69DW6ni%2BaOfQaYsB28%2F99d%2B16gUlGOAM1SK6%2BHSLnyx3NZel2lAsZGvFEEFcBNM9wjFH5wx%2FyMegsyu4npHLAhEe0mD5lHzGSJPEL8P4%2F2qg23SjuUArvwJvGwAQf%2Fq7ti3A9ByROCytBrmqhPOsJQoYm6XlmdCHW1vFz8mGHIr4yzzqG93vjFMaHF1RAZ845uxm32fpdWha1f9vPtDx5db6OEFh3OjKTypfyfwcO5DQwT6wtAtMS2ZgCwUWtObiQkrDr2%2Bm8%2FhEUV%2Bk2hrU%2FXUGqPFgEWwRT3Ylk3%2BfcVzHpcR1ViA4obmaU8%2BDsd9seqXpE5x0csQnXuRlJ0j0NckfTCM%2F%2Be8BjqkAVd%2FzLxG3%2BnBSj675x7NngLzRwdioE45ZyWIODpY7GMxlQmyYQfHV6uE1PWYsBrXPQG3jA9cswgzbrWrYPUb7n330MNDIvMF40GhI6L0Abu31ymDrtQDbB5DvO%2BuHE2Dk4t9nbNw8ijIEJEWpqmvRgX5QhHCno2dnhOUZXvpXNDDIFjTKdIVzyGrLNJ8iAxCO73ZMgBkeVeRcRLnXR8CSMwD%2Bwkm&X-Amz-Signature=edfc4683a4c904c8718c7abc07d56dba09c01d2b0fc8e46e1b41481e93cab150&X-Amz-SignedHeaders=host&x-id=GetObject)
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


