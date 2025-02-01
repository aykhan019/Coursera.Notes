

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JHCC2RR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqZtwti9mYLQkf4uCgL%2BlP6n0QSxHUDF9DVWWL%2FZztFwIhAMOIqcEimjkb4r5MeMvSGxybEato0fc5IuRRzvpvHbSXKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2E54XFtKDDIisnoAq3APKyHyXhHqrypBkZzLgbFVzTT8yB8K0zZA8ahgtFTqUbeDIlHuZ6amcxTATrB0BZVff0zknQlPPn89V3A4wnUkUh%2BBK9JLJ%2Fm4JBgMRMz0xfg3OVjXSeCinlBa8rmRWfV%2FFMaDpeNpXIE4GcbMnVWx4B4ejCECehUf1jZCrNqdmTNTZXhS4jrZg4AZWe5xx4d5CFWeHr%2BRwd9MhN523tqQytQoM7MEtozqTAHExAsXXvie5WzR0%2FMGHeVXMrILszud0vC5yguoPB5VDcAwVwb%2FuhfBNAQMRyMDnSqp1ckAT3Gq7UzA%2BddJyxsTUEWU6W7jMsBttFBNwkmwgyMiEOjgB9Zd1O1uZ1zax%2BIl6NDbFQ3BG9gnPKQRxqsBKnr7i6EHb1mbrHgzEsZhgs2QjIuPTJK1eLXSelxksgv2ugddsRNq%2BnaChpaYWrEmasCxCkG4cD6sM335UePpG6V4fT%2FM2Bjo2y8tPncbm2h%2Fst4AqMeAjLOvnkTpx7SSl0yNIrY15jO164TlDrTQzbM4deUPBSR0ZfHiQ9m8mzJy5tIPubxnNZftKjF%2F2%2BIfrjXZrjdbPFpG2RnGDrdDrlEgj4PW7YGNaSP6%2FXOBOxWM2dt4CXmvwe%2FWpDN0icD7pEDDHpPe8BjqkAW%2F%2BV3XxovcV%2Fj2vTavTI%2FEABXaC1PzG%2BgLZxdf9RDGEuBsF7jW7Q9HEiuqXxRKmwu6DFzyk5e9NdktumwKD0F5IHYkdx3JH0b4Fdu96NnV6UazMnsYUs0FpofRSTU3FWt%2Bt6mgvikivK6IjFl7SogiYMNsSOWc44zlJgYbQY%2BPDWckvNNU%2FgVdwnLrtW1iSdGTnpDHjwV0H%2B4fBsrdGFATVq2H6&X-Amz-Signature=7cf515e8373acbdeacbecb5ed7015f982412111dcd676e727684e75131b6f0c8&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EQVXF52%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPQWDKj4amh6lfjZRUFgBzCuxkCen94CGmOaeStxEpnwIhAOvypqmBeN7cIH8BjDoZ%2Bq271%2FbbXIiq8S9P6iYsjSz1KogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYVh%2B53LsmnYad2WUq3AObhEiKi591Yjyd0Y0%2BuGjufXIKlkWKd4rb%2FMldtwdc6JGWd2x7mGwbzb4UcRo565mfl2oGRI69KZkOFRdRfcO0IqZ7%2BLcC5L8fwtbAwjtW1Yiey4dzGXAixYBla%2BBzxNNW8Tqgd4iTVrilM3GrLet2Kux8Gcl4P7qiyJEgVzhHIflNmsKv5VzUujRJlWfa4PdYpUwYzIZOzvrmtlYKlQWoOYXxIb7XuCdFLFuklCIoHTvL7uKoTnxsedLNumxWMPwOmrGo3FoBhlepja2t0rhTsNYa08Umu%2BGLk%2FSUjh484at5GDJsaWKO1yFHKdkj5c7zFJHF8FrT2CZFHL4JjP%2Fv0VSeOftOWtR532aQ%2FjNiPRx8zyxNKr1mOS39gDU%2FRzlRKAF%2BoEC%2FsYN%2BxYFvsV5C%2Fx%2FFWpzeseF58z6YCdyHZIg3Cf0dXxEOBBSK6CM3unthzkgIGt78dYx1dQVt%2By5NW1%2ByNQ1ym8WKPYtUPZPWuBRZsfW9LsRQjTEwOUUX7aTve0klKv778IMKb1yHvvTqCZMDVrLh0cDxH63Qis3LH4digEyf0Y1WH4Zv%2Frz%2BhlFObqYMhUoHKHl4Fv9VOT%2Bdb89uQYtj48iKc9U5eBtHempNJJXtjoWWSp2aczDBpPe8BjqkAVBZEfTQ1LwGeCKI15V%2BqAI29ioc1gYelKKfUgMEnyO0FuVmLuxc338B%2FlA4c9Qigt7lMqDFiQdbqgRIAQxVfXIGhIaE2YadmZifZGTJRyAhIDWpos7n3ztbGRzZhWTQRgBNDUCYK4%2Bk50aD%2FiMItLp3MzkWpw0X%2FfXnGOrfC7KbeCLDdTNocf3aMFGJEO8VC%2B26HM9mh2vb7PaxhE9D2zDofbkH&X-Amz-Signature=3a350ff08b40b77ecd0450e044fc51392556448b920cf874c07e644444539e78&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EQVXF52%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPQWDKj4amh6lfjZRUFgBzCuxkCen94CGmOaeStxEpnwIhAOvypqmBeN7cIH8BjDoZ%2Bq271%2FbbXIiq8S9P6iYsjSz1KogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYVh%2B53LsmnYad2WUq3AObhEiKi591Yjyd0Y0%2BuGjufXIKlkWKd4rb%2FMldtwdc6JGWd2x7mGwbzb4UcRo565mfl2oGRI69KZkOFRdRfcO0IqZ7%2BLcC5L8fwtbAwjtW1Yiey4dzGXAixYBla%2BBzxNNW8Tqgd4iTVrilM3GrLet2Kux8Gcl4P7qiyJEgVzhHIflNmsKv5VzUujRJlWfa4PdYpUwYzIZOzvrmtlYKlQWoOYXxIb7XuCdFLFuklCIoHTvL7uKoTnxsedLNumxWMPwOmrGo3FoBhlepja2t0rhTsNYa08Umu%2BGLk%2FSUjh484at5GDJsaWKO1yFHKdkj5c7zFJHF8FrT2CZFHL4JjP%2Fv0VSeOftOWtR532aQ%2FjNiPRx8zyxNKr1mOS39gDU%2FRzlRKAF%2BoEC%2FsYN%2BxYFvsV5C%2Fx%2FFWpzeseF58z6YCdyHZIg3Cf0dXxEOBBSK6CM3unthzkgIGt78dYx1dQVt%2By5NW1%2ByNQ1ym8WKPYtUPZPWuBRZsfW9LsRQjTEwOUUX7aTve0klKv778IMKb1yHvvTqCZMDVrLh0cDxH63Qis3LH4digEyf0Y1WH4Zv%2Frz%2BhlFObqYMhUoHKHl4Fv9VOT%2Bdb89uQYtj48iKc9U5eBtHempNJJXtjoWWSp2aczDBpPe8BjqkAVBZEfTQ1LwGeCKI15V%2BqAI29ioc1gYelKKfUgMEnyO0FuVmLuxc338B%2FlA4c9Qigt7lMqDFiQdbqgRIAQxVfXIGhIaE2YadmZifZGTJRyAhIDWpos7n3ztbGRzZhWTQRgBNDUCYK4%2Bk50aD%2FiMItLp3MzkWpw0X%2FfXnGOrfC7KbeCLDdTNocf3aMFGJEO8VC%2B26HM9mh2vb7PaxhE9D2zDofbkH&X-Amz-Signature=bdecfa80dfcf01ffa8e14e5957381ed446c8e709860b173153f90d54a7abb4e5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EQVXF52%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPQWDKj4amh6lfjZRUFgBzCuxkCen94CGmOaeStxEpnwIhAOvypqmBeN7cIH8BjDoZ%2Bq271%2FbbXIiq8S9P6iYsjSz1KogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYVh%2B53LsmnYad2WUq3AObhEiKi591Yjyd0Y0%2BuGjufXIKlkWKd4rb%2FMldtwdc6JGWd2x7mGwbzb4UcRo565mfl2oGRI69KZkOFRdRfcO0IqZ7%2BLcC5L8fwtbAwjtW1Yiey4dzGXAixYBla%2BBzxNNW8Tqgd4iTVrilM3GrLet2Kux8Gcl4P7qiyJEgVzhHIflNmsKv5VzUujRJlWfa4PdYpUwYzIZOzvrmtlYKlQWoOYXxIb7XuCdFLFuklCIoHTvL7uKoTnxsedLNumxWMPwOmrGo3FoBhlepja2t0rhTsNYa08Umu%2BGLk%2FSUjh484at5GDJsaWKO1yFHKdkj5c7zFJHF8FrT2CZFHL4JjP%2Fv0VSeOftOWtR532aQ%2FjNiPRx8zyxNKr1mOS39gDU%2FRzlRKAF%2BoEC%2FsYN%2BxYFvsV5C%2Fx%2FFWpzeseF58z6YCdyHZIg3Cf0dXxEOBBSK6CM3unthzkgIGt78dYx1dQVt%2By5NW1%2ByNQ1ym8WKPYtUPZPWuBRZsfW9LsRQjTEwOUUX7aTve0klKv778IMKb1yHvvTqCZMDVrLh0cDxH63Qis3LH4digEyf0Y1WH4Zv%2Frz%2BhlFObqYMhUoHKHl4Fv9VOT%2Bdb89uQYtj48iKc9U5eBtHempNJJXtjoWWSp2aczDBpPe8BjqkAVBZEfTQ1LwGeCKI15V%2BqAI29ioc1gYelKKfUgMEnyO0FuVmLuxc338B%2FlA4c9Qigt7lMqDFiQdbqgRIAQxVfXIGhIaE2YadmZifZGTJRyAhIDWpos7n3ztbGRzZhWTQRgBNDUCYK4%2Bk50aD%2FiMItLp3MzkWpw0X%2FfXnGOrfC7KbeCLDdTNocf3aMFGJEO8VC%2B26HM9mh2vb7PaxhE9D2zDofbkH&X-Amz-Signature=ac1e71f4e2d2f71ec56d015f439ca1c73dab2f9e1e8e8a283ca567457d022e3f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EQVXF52%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPQWDKj4amh6lfjZRUFgBzCuxkCen94CGmOaeStxEpnwIhAOvypqmBeN7cIH8BjDoZ%2Bq271%2FbbXIiq8S9P6iYsjSz1KogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYVh%2B53LsmnYad2WUq3AObhEiKi591Yjyd0Y0%2BuGjufXIKlkWKd4rb%2FMldtwdc6JGWd2x7mGwbzb4UcRo565mfl2oGRI69KZkOFRdRfcO0IqZ7%2BLcC5L8fwtbAwjtW1Yiey4dzGXAixYBla%2BBzxNNW8Tqgd4iTVrilM3GrLet2Kux8Gcl4P7qiyJEgVzhHIflNmsKv5VzUujRJlWfa4PdYpUwYzIZOzvrmtlYKlQWoOYXxIb7XuCdFLFuklCIoHTvL7uKoTnxsedLNumxWMPwOmrGo3FoBhlepja2t0rhTsNYa08Umu%2BGLk%2FSUjh484at5GDJsaWKO1yFHKdkj5c7zFJHF8FrT2CZFHL4JjP%2Fv0VSeOftOWtR532aQ%2FjNiPRx8zyxNKr1mOS39gDU%2FRzlRKAF%2BoEC%2FsYN%2BxYFvsV5C%2Fx%2FFWpzeseF58z6YCdyHZIg3Cf0dXxEOBBSK6CM3unthzkgIGt78dYx1dQVt%2By5NW1%2ByNQ1ym8WKPYtUPZPWuBRZsfW9LsRQjTEwOUUX7aTve0klKv778IMKb1yHvvTqCZMDVrLh0cDxH63Qis3LH4digEyf0Y1WH4Zv%2Frz%2BhlFObqYMhUoHKHl4Fv9VOT%2Bdb89uQYtj48iKc9U5eBtHempNJJXtjoWWSp2aczDBpPe8BjqkAVBZEfTQ1LwGeCKI15V%2BqAI29ioc1gYelKKfUgMEnyO0FuVmLuxc338B%2FlA4c9Qigt7lMqDFiQdbqgRIAQxVfXIGhIaE2YadmZifZGTJRyAhIDWpos7n3ztbGRzZhWTQRgBNDUCYK4%2Bk50aD%2FiMItLp3MzkWpw0X%2FfXnGOrfC7KbeCLDdTNocf3aMFGJEO8VC%2B26HM9mh2vb7PaxhE9D2zDofbkH&X-Amz-Signature=a14eed9b9e33e1ea7e888fdf6be623abbb71431c54c3f469305db4d1c4acfc07&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EQVXF52%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPQWDKj4amh6lfjZRUFgBzCuxkCen94CGmOaeStxEpnwIhAOvypqmBeN7cIH8BjDoZ%2Bq271%2FbbXIiq8S9P6iYsjSz1KogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYVh%2B53LsmnYad2WUq3AObhEiKi591Yjyd0Y0%2BuGjufXIKlkWKd4rb%2FMldtwdc6JGWd2x7mGwbzb4UcRo565mfl2oGRI69KZkOFRdRfcO0IqZ7%2BLcC5L8fwtbAwjtW1Yiey4dzGXAixYBla%2BBzxNNW8Tqgd4iTVrilM3GrLet2Kux8Gcl4P7qiyJEgVzhHIflNmsKv5VzUujRJlWfa4PdYpUwYzIZOzvrmtlYKlQWoOYXxIb7XuCdFLFuklCIoHTvL7uKoTnxsedLNumxWMPwOmrGo3FoBhlepja2t0rhTsNYa08Umu%2BGLk%2FSUjh484at5GDJsaWKO1yFHKdkj5c7zFJHF8FrT2CZFHL4JjP%2Fv0VSeOftOWtR532aQ%2FjNiPRx8zyxNKr1mOS39gDU%2FRzlRKAF%2BoEC%2FsYN%2BxYFvsV5C%2Fx%2FFWpzeseF58z6YCdyHZIg3Cf0dXxEOBBSK6CM3unthzkgIGt78dYx1dQVt%2By5NW1%2ByNQ1ym8WKPYtUPZPWuBRZsfW9LsRQjTEwOUUX7aTve0klKv778IMKb1yHvvTqCZMDVrLh0cDxH63Qis3LH4digEyf0Y1WH4Zv%2Frz%2BhlFObqYMhUoHKHl4Fv9VOT%2Bdb89uQYtj48iKc9U5eBtHempNJJXtjoWWSp2aczDBpPe8BjqkAVBZEfTQ1LwGeCKI15V%2BqAI29ioc1gYelKKfUgMEnyO0FuVmLuxc338B%2FlA4c9Qigt7lMqDFiQdbqgRIAQxVfXIGhIaE2YadmZifZGTJRyAhIDWpos7n3ztbGRzZhWTQRgBNDUCYK4%2Bk50aD%2FiMItLp3MzkWpw0X%2FfXnGOrfC7KbeCLDdTNocf3aMFGJEO8VC%2B26HM9mh2vb7PaxhE9D2zDofbkH&X-Amz-Signature=5488ab4711a03bbe7872a38e4ca2f60062d8b87e8fa088aa865d3fb8c5bdf651&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JHCC2RR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqZtwti9mYLQkf4uCgL%2BlP6n0QSxHUDF9DVWWL%2FZztFwIhAMOIqcEimjkb4r5MeMvSGxybEato0fc5IuRRzvpvHbSXKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2E54XFtKDDIisnoAq3APKyHyXhHqrypBkZzLgbFVzTT8yB8K0zZA8ahgtFTqUbeDIlHuZ6amcxTATrB0BZVff0zknQlPPn89V3A4wnUkUh%2BBK9JLJ%2Fm4JBgMRMz0xfg3OVjXSeCinlBa8rmRWfV%2FFMaDpeNpXIE4GcbMnVWx4B4ejCECehUf1jZCrNqdmTNTZXhS4jrZg4AZWe5xx4d5CFWeHr%2BRwd9MhN523tqQytQoM7MEtozqTAHExAsXXvie5WzR0%2FMGHeVXMrILszud0vC5yguoPB5VDcAwVwb%2FuhfBNAQMRyMDnSqp1ckAT3Gq7UzA%2BddJyxsTUEWU6W7jMsBttFBNwkmwgyMiEOjgB9Zd1O1uZ1zax%2BIl6NDbFQ3BG9gnPKQRxqsBKnr7i6EHb1mbrHgzEsZhgs2QjIuPTJK1eLXSelxksgv2ugddsRNq%2BnaChpaYWrEmasCxCkG4cD6sM335UePpG6V4fT%2FM2Bjo2y8tPncbm2h%2Fst4AqMeAjLOvnkTpx7SSl0yNIrY15jO164TlDrTQzbM4deUPBSR0ZfHiQ9m8mzJy5tIPubxnNZftKjF%2F2%2BIfrjXZrjdbPFpG2RnGDrdDrlEgj4PW7YGNaSP6%2FXOBOxWM2dt4CXmvwe%2FWpDN0icD7pEDDHpPe8BjqkAW%2F%2BV3XxovcV%2Fj2vTavTI%2FEABXaC1PzG%2BgLZxdf9RDGEuBsF7jW7Q9HEiuqXxRKmwu6DFzyk5e9NdktumwKD0F5IHYkdx3JH0b4Fdu96NnV6UazMnsYUs0FpofRSTU3FWt%2Bt6mgvikivK6IjFl7SogiYMNsSOWc44zlJgYbQY%2BPDWckvNNU%2FgVdwnLrtW1iSdGTnpDHjwV0H%2B4fBsrdGFATVq2H6&X-Amz-Signature=feec6ac05dee8ebbc485140b092775bff6119a5a18520094593c7b9dffc2b1ce&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JHCC2RR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqZtwti9mYLQkf4uCgL%2BlP6n0QSxHUDF9DVWWL%2FZztFwIhAMOIqcEimjkb4r5MeMvSGxybEato0fc5IuRRzvpvHbSXKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2E54XFtKDDIisnoAq3APKyHyXhHqrypBkZzLgbFVzTT8yB8K0zZA8ahgtFTqUbeDIlHuZ6amcxTATrB0BZVff0zknQlPPn89V3A4wnUkUh%2BBK9JLJ%2Fm4JBgMRMz0xfg3OVjXSeCinlBa8rmRWfV%2FFMaDpeNpXIE4GcbMnVWx4B4ejCECehUf1jZCrNqdmTNTZXhS4jrZg4AZWe5xx4d5CFWeHr%2BRwd9MhN523tqQytQoM7MEtozqTAHExAsXXvie5WzR0%2FMGHeVXMrILszud0vC5yguoPB5VDcAwVwb%2FuhfBNAQMRyMDnSqp1ckAT3Gq7UzA%2BddJyxsTUEWU6W7jMsBttFBNwkmwgyMiEOjgB9Zd1O1uZ1zax%2BIl6NDbFQ3BG9gnPKQRxqsBKnr7i6EHb1mbrHgzEsZhgs2QjIuPTJK1eLXSelxksgv2ugddsRNq%2BnaChpaYWrEmasCxCkG4cD6sM335UePpG6V4fT%2FM2Bjo2y8tPncbm2h%2Fst4AqMeAjLOvnkTpx7SSl0yNIrY15jO164TlDrTQzbM4deUPBSR0ZfHiQ9m8mzJy5tIPubxnNZftKjF%2F2%2BIfrjXZrjdbPFpG2RnGDrdDrlEgj4PW7YGNaSP6%2FXOBOxWM2dt4CXmvwe%2FWpDN0icD7pEDDHpPe8BjqkAW%2F%2BV3XxovcV%2Fj2vTavTI%2FEABXaC1PzG%2BgLZxdf9RDGEuBsF7jW7Q9HEiuqXxRKmwu6DFzyk5e9NdktumwKD0F5IHYkdx3JH0b4Fdu96NnV6UazMnsYUs0FpofRSTU3FWt%2Bt6mgvikivK6IjFl7SogiYMNsSOWc44zlJgYbQY%2BPDWckvNNU%2FgVdwnLrtW1iSdGTnpDHjwV0H%2B4fBsrdGFATVq2H6&X-Amz-Signature=7215afefe5eddce5cd6b3f2b3589ba20cec2857a54437bc74713ea28abfb274f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JHCC2RR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqZtwti9mYLQkf4uCgL%2BlP6n0QSxHUDF9DVWWL%2FZztFwIhAMOIqcEimjkb4r5MeMvSGxybEato0fc5IuRRzvpvHbSXKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2E54XFtKDDIisnoAq3APKyHyXhHqrypBkZzLgbFVzTT8yB8K0zZA8ahgtFTqUbeDIlHuZ6amcxTATrB0BZVff0zknQlPPn89V3A4wnUkUh%2BBK9JLJ%2Fm4JBgMRMz0xfg3OVjXSeCinlBa8rmRWfV%2FFMaDpeNpXIE4GcbMnVWx4B4ejCECehUf1jZCrNqdmTNTZXhS4jrZg4AZWe5xx4d5CFWeHr%2BRwd9MhN523tqQytQoM7MEtozqTAHExAsXXvie5WzR0%2FMGHeVXMrILszud0vC5yguoPB5VDcAwVwb%2FuhfBNAQMRyMDnSqp1ckAT3Gq7UzA%2BddJyxsTUEWU6W7jMsBttFBNwkmwgyMiEOjgB9Zd1O1uZ1zax%2BIl6NDbFQ3BG9gnPKQRxqsBKnr7i6EHb1mbrHgzEsZhgs2QjIuPTJK1eLXSelxksgv2ugddsRNq%2BnaChpaYWrEmasCxCkG4cD6sM335UePpG6V4fT%2FM2Bjo2y8tPncbm2h%2Fst4AqMeAjLOvnkTpx7SSl0yNIrY15jO164TlDrTQzbM4deUPBSR0ZfHiQ9m8mzJy5tIPubxnNZftKjF%2F2%2BIfrjXZrjdbPFpG2RnGDrdDrlEgj4PW7YGNaSP6%2FXOBOxWM2dt4CXmvwe%2FWpDN0icD7pEDDHpPe8BjqkAW%2F%2BV3XxovcV%2Fj2vTavTI%2FEABXaC1PzG%2BgLZxdf9RDGEuBsF7jW7Q9HEiuqXxRKmwu6DFzyk5e9NdktumwKD0F5IHYkdx3JH0b4Fdu96NnV6UazMnsYUs0FpofRSTU3FWt%2Bt6mgvikivK6IjFl7SogiYMNsSOWc44zlJgYbQY%2BPDWckvNNU%2FgVdwnLrtW1iSdGTnpDHjwV0H%2B4fBsrdGFATVq2H6&X-Amz-Signature=fb5ab2636d447aaf088df8979824523b6394288f436ffdb65de777a74fbf8d95&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JHCC2RR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqZtwti9mYLQkf4uCgL%2BlP6n0QSxHUDF9DVWWL%2FZztFwIhAMOIqcEimjkb4r5MeMvSGxybEato0fc5IuRRzvpvHbSXKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2E54XFtKDDIisnoAq3APKyHyXhHqrypBkZzLgbFVzTT8yB8K0zZA8ahgtFTqUbeDIlHuZ6amcxTATrB0BZVff0zknQlPPn89V3A4wnUkUh%2BBK9JLJ%2Fm4JBgMRMz0xfg3OVjXSeCinlBa8rmRWfV%2FFMaDpeNpXIE4GcbMnVWx4B4ejCECehUf1jZCrNqdmTNTZXhS4jrZg4AZWe5xx4d5CFWeHr%2BRwd9MhN523tqQytQoM7MEtozqTAHExAsXXvie5WzR0%2FMGHeVXMrILszud0vC5yguoPB5VDcAwVwb%2FuhfBNAQMRyMDnSqp1ckAT3Gq7UzA%2BddJyxsTUEWU6W7jMsBttFBNwkmwgyMiEOjgB9Zd1O1uZ1zax%2BIl6NDbFQ3BG9gnPKQRxqsBKnr7i6EHb1mbrHgzEsZhgs2QjIuPTJK1eLXSelxksgv2ugddsRNq%2BnaChpaYWrEmasCxCkG4cD6sM335UePpG6V4fT%2FM2Bjo2y8tPncbm2h%2Fst4AqMeAjLOvnkTpx7SSl0yNIrY15jO164TlDrTQzbM4deUPBSR0ZfHiQ9m8mzJy5tIPubxnNZftKjF%2F2%2BIfrjXZrjdbPFpG2RnGDrdDrlEgj4PW7YGNaSP6%2FXOBOxWM2dt4CXmvwe%2FWpDN0icD7pEDDHpPe8BjqkAW%2F%2BV3XxovcV%2Fj2vTavTI%2FEABXaC1PzG%2BgLZxdf9RDGEuBsF7jW7Q9HEiuqXxRKmwu6DFzyk5e9NdktumwKD0F5IHYkdx3JH0b4Fdu96NnV6UazMnsYUs0FpofRSTU3FWt%2Bt6mgvikivK6IjFl7SogiYMNsSOWc44zlJgYbQY%2BPDWckvNNU%2FgVdwnLrtW1iSdGTnpDHjwV0H%2B4fBsrdGFATVq2H6&X-Amz-Signature=76e2c228120a761aec522a8b18af98d7b559cd68b40e6658471af363029d5ad2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JHCC2RR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqZtwti9mYLQkf4uCgL%2BlP6n0QSxHUDF9DVWWL%2FZztFwIhAMOIqcEimjkb4r5MeMvSGxybEato0fc5IuRRzvpvHbSXKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2E54XFtKDDIisnoAq3APKyHyXhHqrypBkZzLgbFVzTT8yB8K0zZA8ahgtFTqUbeDIlHuZ6amcxTATrB0BZVff0zknQlPPn89V3A4wnUkUh%2BBK9JLJ%2Fm4JBgMRMz0xfg3OVjXSeCinlBa8rmRWfV%2FFMaDpeNpXIE4GcbMnVWx4B4ejCECehUf1jZCrNqdmTNTZXhS4jrZg4AZWe5xx4d5CFWeHr%2BRwd9MhN523tqQytQoM7MEtozqTAHExAsXXvie5WzR0%2FMGHeVXMrILszud0vC5yguoPB5VDcAwVwb%2FuhfBNAQMRyMDnSqp1ckAT3Gq7UzA%2BddJyxsTUEWU6W7jMsBttFBNwkmwgyMiEOjgB9Zd1O1uZ1zax%2BIl6NDbFQ3BG9gnPKQRxqsBKnr7i6EHb1mbrHgzEsZhgs2QjIuPTJK1eLXSelxksgv2ugddsRNq%2BnaChpaYWrEmasCxCkG4cD6sM335UePpG6V4fT%2FM2Bjo2y8tPncbm2h%2Fst4AqMeAjLOvnkTpx7SSl0yNIrY15jO164TlDrTQzbM4deUPBSR0ZfHiQ9m8mzJy5tIPubxnNZftKjF%2F2%2BIfrjXZrjdbPFpG2RnGDrdDrlEgj4PW7YGNaSP6%2FXOBOxWM2dt4CXmvwe%2FWpDN0icD7pEDDHpPe8BjqkAW%2F%2BV3XxovcV%2Fj2vTavTI%2FEABXaC1PzG%2BgLZxdf9RDGEuBsF7jW7Q9HEiuqXxRKmwu6DFzyk5e9NdktumwKD0F5IHYkdx3JH0b4Fdu96NnV6UazMnsYUs0FpofRSTU3FWt%2Bt6mgvikivK6IjFl7SogiYMNsSOWc44zlJgYbQY%2BPDWckvNNU%2FgVdwnLrtW1iSdGTnpDHjwV0H%2B4fBsrdGFATVq2H6&X-Amz-Signature=5056fe4670e66bb2530225e865e159187ab4ad78a1f4193499578c3bd072f966&X-Amz-SignedHeaders=host&x-id=GetObject)
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


