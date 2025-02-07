

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QOSC54L%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQC7VMupRu2F1c%2FBc47ghJb87S7pXNXl652YwVaAXudQYgIhAOeZsZbCwWhh%2F0z0nwVsQp1ohE1TF5wQmEeyrNY77REHKv8DCHEQABoMNjM3NDIzMTgzODA1IgxiVSVmpOJeaf1Y%2BeEq3AMbb%2FDW1n06J749%2B6mYJ1dauykUyuAC0g4VlE8%2Fd%2Fi2zzI57%2BSMUCjFjgCHL3j16klwiux6U2nCDknFzaI4wvtnCoCXHNWwxMI5ya9vBL5vxo5571aydoEUvcVf4CHFWc%2Fx7UVscHI05qLJ5ges73W2hudv2PNGu7yruH21qi5wVLmaOqsc66WOb%2FVhY6Jz7ElzCWmu%2Fq6XWpRHuTJCEqP4h42IXsenyQF%2FuWRArfEUtoT4wxZzqGwMnKv5U7JNTSL13GN6NP1O5VHslpuUt446XtJwUHKVKmw5gk5TFuq%2B5gf7kpw42GbuXx15YpnwiPgCe67Zjt2zEedC0hCqX4T1LsJjIWqbXIBtaXSzB%2FkTOaFM1LrxbgFD2J7mrE3EgVsqF8tUlAQyfgx6y6DhoFFFAmwcxynZNMGxLglOfBi5tWctYOOFO9TwkQXbbzdMjb84%2FZ3GhcbFpTX0D%2ByRg%2F%2FgSzVeyQdFmmIk3oY2EZaKpfCgUeSeiEG2Ce67TPRkfgv06NSIjx7hLv2Om6VWl5OKEefse87LHDf%2Fv2DXu569zHWGqmannmwFIHzQ%2BkXxMsO3cFHbuhRWXPZpZ3AYiFeyGF4DZM%2FT56ngjRHDpgxXxNW%2FalwXSqhcsWqwYzCG%2Bpa9BjqkAXfAEuQVamA4G%2BP1zzM%2BqYiNZuNx6VyHCUF7uVkbEbtxJa6txuPDAEVKQTyFDEw%2FWKN4Bg6yXmOnTN4A5k%2BK6hOd%2BKyzhigYb%2BJB6pzrZpZLRbzLItDP8fMU2JN53Takgn6Q8IBZQRmJ%2FSj1WTrQ2xlT8hTcubCvVRHcwBx1AUSWqgFibNmTtFKdAzUaJae6PDLTwMVL6zSji6Flkuloh6jjZqmj&X-Amz-Signature=cecc0e99ef04698ef8f146ba4c69549a1c3e995a4e41555da3d85a103f29d730&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYGQBQKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIFXo5%2F2c9GPTxYBVc7703HP8CnKMhWBc8smv0Px77pFKAiBX0RZe1Fd3OPh0QOLwVf7eS23%2FMPoraejgsmM2ovh6%2FCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM6JWz%2F7GxdmQVZETsKtwDFJzEJh8bbca6cjWFdclPHSKCzlHDzhnqs8W9y36qdX%2BTwiUOyySRlf1LtJ3XRdfDTsPcEAu8Oxv%2FzORzoXDw0h%2BW3slwelMjTjECH8gdpkEwvi%2FYjz4BvYv71ci0VstmlMxicdlROL0lCivHgGFePw2m1JaNEnjqAsF6IdK8fW4sU54r31WvfXwP7CLDgof8ubu79sffO1WsuDpOu39naRZoDuY9oxpaIvyDgCKKFv2V69%2BwnuhfhWUJ3Preu%2BSZDglAIyKVDDrsyKx1w6oL6w5ctU2GTO7lFEVKtKUhWLnQkbUYaKN8F%2FvmEIIRBitgtkwAmAJqDrBjYStgI4BMtpacp51Ao%2FDVTlBWds%2FvwltZhnIQwtjOiuMq1%2BYr%2FAEucIMN1HkuK1K9sTwboLVyRn%2BC9x10O6PPYQvR2E92mhENmshlQ8beOrPgKTarff15dnobygYaEjucX9Chf9eHZp%2FcAnUqqPPsLGVg92CJHiMiglGTVtbe233TbdtfdgKyjqAcoE6YOhKAqryGr6K522GQxsTAUkfLpxeZz%2B9KzzVyo5%2F36KF8DEYiUSd2bwAlWVKtrYrJeHsnkZjSd9dbcye1bQT%2Fl17ryuxgiwtnE2PiNmvfdbtApQbEcIQwmvqWvQY6pgFz7MuPY88ghW8islmzBTm%2Blra42rlwTf17xIGHv%2FKeCfgmggUi%2BJ92lfmVxaP7Naah%2BAWLnF%2FgdnnWOjYwrkPBfjlB7XNyaSt2GkrJPBD754eTNHLMZFRG28xEB%2BlEdK7ezGyBbnxjuZHXFFfdq6JAQV6GutbtXrBeZrZXyHvgkpSak9XmqUCLo0UlvGUZUJsDJ9EE2%2FPRF8tw7cKJzZt%2FzmgAmTC8&X-Amz-Signature=602abd5754d299dc24bbe790b59577a9d104fa72b02001fdca957b64d44443c9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYGQBQKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIFXo5%2F2c9GPTxYBVc7703HP8CnKMhWBc8smv0Px77pFKAiBX0RZe1Fd3OPh0QOLwVf7eS23%2FMPoraejgsmM2ovh6%2FCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM6JWz%2F7GxdmQVZETsKtwDFJzEJh8bbca6cjWFdclPHSKCzlHDzhnqs8W9y36qdX%2BTwiUOyySRlf1LtJ3XRdfDTsPcEAu8Oxv%2FzORzoXDw0h%2BW3slwelMjTjECH8gdpkEwvi%2FYjz4BvYv71ci0VstmlMxicdlROL0lCivHgGFePw2m1JaNEnjqAsF6IdK8fW4sU54r31WvfXwP7CLDgof8ubu79sffO1WsuDpOu39naRZoDuY9oxpaIvyDgCKKFv2V69%2BwnuhfhWUJ3Preu%2BSZDglAIyKVDDrsyKx1w6oL6w5ctU2GTO7lFEVKtKUhWLnQkbUYaKN8F%2FvmEIIRBitgtkwAmAJqDrBjYStgI4BMtpacp51Ao%2FDVTlBWds%2FvwltZhnIQwtjOiuMq1%2BYr%2FAEucIMN1HkuK1K9sTwboLVyRn%2BC9x10O6PPYQvR2E92mhENmshlQ8beOrPgKTarff15dnobygYaEjucX9Chf9eHZp%2FcAnUqqPPsLGVg92CJHiMiglGTVtbe233TbdtfdgKyjqAcoE6YOhKAqryGr6K522GQxsTAUkfLpxeZz%2B9KzzVyo5%2F36KF8DEYiUSd2bwAlWVKtrYrJeHsnkZjSd9dbcye1bQT%2Fl17ryuxgiwtnE2PiNmvfdbtApQbEcIQwmvqWvQY6pgFz7MuPY88ghW8islmzBTm%2Blra42rlwTf17xIGHv%2FKeCfgmggUi%2BJ92lfmVxaP7Naah%2BAWLnF%2FgdnnWOjYwrkPBfjlB7XNyaSt2GkrJPBD754eTNHLMZFRG28xEB%2BlEdK7ezGyBbnxjuZHXFFfdq6JAQV6GutbtXrBeZrZXyHvgkpSak9XmqUCLo0UlvGUZUJsDJ9EE2%2FPRF8tw7cKJzZt%2FzmgAmTC8&X-Amz-Signature=b892670f45e0e0b7c0164bd8eee256ac058912943a657b842acd2d26644dbdc3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYGQBQKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIFXo5%2F2c9GPTxYBVc7703HP8CnKMhWBc8smv0Px77pFKAiBX0RZe1Fd3OPh0QOLwVf7eS23%2FMPoraejgsmM2ovh6%2FCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM6JWz%2F7GxdmQVZETsKtwDFJzEJh8bbca6cjWFdclPHSKCzlHDzhnqs8W9y36qdX%2BTwiUOyySRlf1LtJ3XRdfDTsPcEAu8Oxv%2FzORzoXDw0h%2BW3slwelMjTjECH8gdpkEwvi%2FYjz4BvYv71ci0VstmlMxicdlROL0lCivHgGFePw2m1JaNEnjqAsF6IdK8fW4sU54r31WvfXwP7CLDgof8ubu79sffO1WsuDpOu39naRZoDuY9oxpaIvyDgCKKFv2V69%2BwnuhfhWUJ3Preu%2BSZDglAIyKVDDrsyKx1w6oL6w5ctU2GTO7lFEVKtKUhWLnQkbUYaKN8F%2FvmEIIRBitgtkwAmAJqDrBjYStgI4BMtpacp51Ao%2FDVTlBWds%2FvwltZhnIQwtjOiuMq1%2BYr%2FAEucIMN1HkuK1K9sTwboLVyRn%2BC9x10O6PPYQvR2E92mhENmshlQ8beOrPgKTarff15dnobygYaEjucX9Chf9eHZp%2FcAnUqqPPsLGVg92CJHiMiglGTVtbe233TbdtfdgKyjqAcoE6YOhKAqryGr6K522GQxsTAUkfLpxeZz%2B9KzzVyo5%2F36KF8DEYiUSd2bwAlWVKtrYrJeHsnkZjSd9dbcye1bQT%2Fl17ryuxgiwtnE2PiNmvfdbtApQbEcIQwmvqWvQY6pgFz7MuPY88ghW8islmzBTm%2Blra42rlwTf17xIGHv%2FKeCfgmggUi%2BJ92lfmVxaP7Naah%2BAWLnF%2FgdnnWOjYwrkPBfjlB7XNyaSt2GkrJPBD754eTNHLMZFRG28xEB%2BlEdK7ezGyBbnxjuZHXFFfdq6JAQV6GutbtXrBeZrZXyHvgkpSak9XmqUCLo0UlvGUZUJsDJ9EE2%2FPRF8tw7cKJzZt%2FzmgAmTC8&X-Amz-Signature=ca4199bcd41ffb9e768f81b9e3bc9cd545a60d5c95e462f97038690f309489fb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYGQBQKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIFXo5%2F2c9GPTxYBVc7703HP8CnKMhWBc8smv0Px77pFKAiBX0RZe1Fd3OPh0QOLwVf7eS23%2FMPoraejgsmM2ovh6%2FCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM6JWz%2F7GxdmQVZETsKtwDFJzEJh8bbca6cjWFdclPHSKCzlHDzhnqs8W9y36qdX%2BTwiUOyySRlf1LtJ3XRdfDTsPcEAu8Oxv%2FzORzoXDw0h%2BW3slwelMjTjECH8gdpkEwvi%2FYjz4BvYv71ci0VstmlMxicdlROL0lCivHgGFePw2m1JaNEnjqAsF6IdK8fW4sU54r31WvfXwP7CLDgof8ubu79sffO1WsuDpOu39naRZoDuY9oxpaIvyDgCKKFv2V69%2BwnuhfhWUJ3Preu%2BSZDglAIyKVDDrsyKx1w6oL6w5ctU2GTO7lFEVKtKUhWLnQkbUYaKN8F%2FvmEIIRBitgtkwAmAJqDrBjYStgI4BMtpacp51Ao%2FDVTlBWds%2FvwltZhnIQwtjOiuMq1%2BYr%2FAEucIMN1HkuK1K9sTwboLVyRn%2BC9x10O6PPYQvR2E92mhENmshlQ8beOrPgKTarff15dnobygYaEjucX9Chf9eHZp%2FcAnUqqPPsLGVg92CJHiMiglGTVtbe233TbdtfdgKyjqAcoE6YOhKAqryGr6K522GQxsTAUkfLpxeZz%2B9KzzVyo5%2F36KF8DEYiUSd2bwAlWVKtrYrJeHsnkZjSd9dbcye1bQT%2Fl17ryuxgiwtnE2PiNmvfdbtApQbEcIQwmvqWvQY6pgFz7MuPY88ghW8islmzBTm%2Blra42rlwTf17xIGHv%2FKeCfgmggUi%2BJ92lfmVxaP7Naah%2BAWLnF%2FgdnnWOjYwrkPBfjlB7XNyaSt2GkrJPBD754eTNHLMZFRG28xEB%2BlEdK7ezGyBbnxjuZHXFFfdq6JAQV6GutbtXrBeZrZXyHvgkpSak9XmqUCLo0UlvGUZUJsDJ9EE2%2FPRF8tw7cKJzZt%2FzmgAmTC8&X-Amz-Signature=1b5e57324e9229f5c51736c83448cbd5c230dcf86b573323d0098ac010f5ef5c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYGQBQKX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIFXo5%2F2c9GPTxYBVc7703HP8CnKMhWBc8smv0Px77pFKAiBX0RZe1Fd3OPh0QOLwVf7eS23%2FMPoraejgsmM2ovh6%2FCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM6JWz%2F7GxdmQVZETsKtwDFJzEJh8bbca6cjWFdclPHSKCzlHDzhnqs8W9y36qdX%2BTwiUOyySRlf1LtJ3XRdfDTsPcEAu8Oxv%2FzORzoXDw0h%2BW3slwelMjTjECH8gdpkEwvi%2FYjz4BvYv71ci0VstmlMxicdlROL0lCivHgGFePw2m1JaNEnjqAsF6IdK8fW4sU54r31WvfXwP7CLDgof8ubu79sffO1WsuDpOu39naRZoDuY9oxpaIvyDgCKKFv2V69%2BwnuhfhWUJ3Preu%2BSZDglAIyKVDDrsyKx1w6oL6w5ctU2GTO7lFEVKtKUhWLnQkbUYaKN8F%2FvmEIIRBitgtkwAmAJqDrBjYStgI4BMtpacp51Ao%2FDVTlBWds%2FvwltZhnIQwtjOiuMq1%2BYr%2FAEucIMN1HkuK1K9sTwboLVyRn%2BC9x10O6PPYQvR2E92mhENmshlQ8beOrPgKTarff15dnobygYaEjucX9Chf9eHZp%2FcAnUqqPPsLGVg92CJHiMiglGTVtbe233TbdtfdgKyjqAcoE6YOhKAqryGr6K522GQxsTAUkfLpxeZz%2B9KzzVyo5%2F36KF8DEYiUSd2bwAlWVKtrYrJeHsnkZjSd9dbcye1bQT%2Fl17ryuxgiwtnE2PiNmvfdbtApQbEcIQwmvqWvQY6pgFz7MuPY88ghW8islmzBTm%2Blra42rlwTf17xIGHv%2FKeCfgmggUi%2BJ92lfmVxaP7Naah%2BAWLnF%2FgdnnWOjYwrkPBfjlB7XNyaSt2GkrJPBD754eTNHLMZFRG28xEB%2BlEdK7ezGyBbnxjuZHXFFfdq6JAQV6GutbtXrBeZrZXyHvgkpSak9XmqUCLo0UlvGUZUJsDJ9EE2%2FPRF8tw7cKJzZt%2FzmgAmTC8&X-Amz-Signature=c88a26970cd05d87f65cd7c7054bbb72a6ff8afb98b17a71e0a03c5183483983&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QOSC54L%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQC7VMupRu2F1c%2FBc47ghJb87S7pXNXl652YwVaAXudQYgIhAOeZsZbCwWhh%2F0z0nwVsQp1ohE1TF5wQmEeyrNY77REHKv8DCHEQABoMNjM3NDIzMTgzODA1IgxiVSVmpOJeaf1Y%2BeEq3AMbb%2FDW1n06J749%2B6mYJ1dauykUyuAC0g4VlE8%2Fd%2Fi2zzI57%2BSMUCjFjgCHL3j16klwiux6U2nCDknFzaI4wvtnCoCXHNWwxMI5ya9vBL5vxo5571aydoEUvcVf4CHFWc%2Fx7UVscHI05qLJ5ges73W2hudv2PNGu7yruH21qi5wVLmaOqsc66WOb%2FVhY6Jz7ElzCWmu%2Fq6XWpRHuTJCEqP4h42IXsenyQF%2FuWRArfEUtoT4wxZzqGwMnKv5U7JNTSL13GN6NP1O5VHslpuUt446XtJwUHKVKmw5gk5TFuq%2B5gf7kpw42GbuXx15YpnwiPgCe67Zjt2zEedC0hCqX4T1LsJjIWqbXIBtaXSzB%2FkTOaFM1LrxbgFD2J7mrE3EgVsqF8tUlAQyfgx6y6DhoFFFAmwcxynZNMGxLglOfBi5tWctYOOFO9TwkQXbbzdMjb84%2FZ3GhcbFpTX0D%2ByRg%2F%2FgSzVeyQdFmmIk3oY2EZaKpfCgUeSeiEG2Ce67TPRkfgv06NSIjx7hLv2Om6VWl5OKEefse87LHDf%2Fv2DXu569zHWGqmannmwFIHzQ%2BkXxMsO3cFHbuhRWXPZpZ3AYiFeyGF4DZM%2FT56ngjRHDpgxXxNW%2FalwXSqhcsWqwYzCG%2Bpa9BjqkAXfAEuQVamA4G%2BP1zzM%2BqYiNZuNx6VyHCUF7uVkbEbtxJa6txuPDAEVKQTyFDEw%2FWKN4Bg6yXmOnTN4A5k%2BK6hOd%2BKyzhigYb%2BJB6pzrZpZLRbzLItDP8fMU2JN53Takgn6Q8IBZQRmJ%2FSj1WTrQ2xlT8hTcubCvVRHcwBx1AUSWqgFibNmTtFKdAzUaJae6PDLTwMVL6zSji6Flkuloh6jjZqmj&X-Amz-Signature=bf26c2c64df91696bb3f771c9221c99aedba829bf185908ecceb47d364c24dff&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QOSC54L%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQC7VMupRu2F1c%2FBc47ghJb87S7pXNXl652YwVaAXudQYgIhAOeZsZbCwWhh%2F0z0nwVsQp1ohE1TF5wQmEeyrNY77REHKv8DCHEQABoMNjM3NDIzMTgzODA1IgxiVSVmpOJeaf1Y%2BeEq3AMbb%2FDW1n06J749%2B6mYJ1dauykUyuAC0g4VlE8%2Fd%2Fi2zzI57%2BSMUCjFjgCHL3j16klwiux6U2nCDknFzaI4wvtnCoCXHNWwxMI5ya9vBL5vxo5571aydoEUvcVf4CHFWc%2Fx7UVscHI05qLJ5ges73W2hudv2PNGu7yruH21qi5wVLmaOqsc66WOb%2FVhY6Jz7ElzCWmu%2Fq6XWpRHuTJCEqP4h42IXsenyQF%2FuWRArfEUtoT4wxZzqGwMnKv5U7JNTSL13GN6NP1O5VHslpuUt446XtJwUHKVKmw5gk5TFuq%2B5gf7kpw42GbuXx15YpnwiPgCe67Zjt2zEedC0hCqX4T1LsJjIWqbXIBtaXSzB%2FkTOaFM1LrxbgFD2J7mrE3EgVsqF8tUlAQyfgx6y6DhoFFFAmwcxynZNMGxLglOfBi5tWctYOOFO9TwkQXbbzdMjb84%2FZ3GhcbFpTX0D%2ByRg%2F%2FgSzVeyQdFmmIk3oY2EZaKpfCgUeSeiEG2Ce67TPRkfgv06NSIjx7hLv2Om6VWl5OKEefse87LHDf%2Fv2DXu569zHWGqmannmwFIHzQ%2BkXxMsO3cFHbuhRWXPZpZ3AYiFeyGF4DZM%2FT56ngjRHDpgxXxNW%2FalwXSqhcsWqwYzCG%2Bpa9BjqkAXfAEuQVamA4G%2BP1zzM%2BqYiNZuNx6VyHCUF7uVkbEbtxJa6txuPDAEVKQTyFDEw%2FWKN4Bg6yXmOnTN4A5k%2BK6hOd%2BKyzhigYb%2BJB6pzrZpZLRbzLItDP8fMU2JN53Takgn6Q8IBZQRmJ%2FSj1WTrQ2xlT8hTcubCvVRHcwBx1AUSWqgFibNmTtFKdAzUaJae6PDLTwMVL6zSji6Flkuloh6jjZqmj&X-Amz-Signature=bc0e7eb9fefe5a525d3ab01faef0f6fb79b40b8928edac9d052062dd22b1e6ad&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QOSC54L%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQC7VMupRu2F1c%2FBc47ghJb87S7pXNXl652YwVaAXudQYgIhAOeZsZbCwWhh%2F0z0nwVsQp1ohE1TF5wQmEeyrNY77REHKv8DCHEQABoMNjM3NDIzMTgzODA1IgxiVSVmpOJeaf1Y%2BeEq3AMbb%2FDW1n06J749%2B6mYJ1dauykUyuAC0g4VlE8%2Fd%2Fi2zzI57%2BSMUCjFjgCHL3j16klwiux6U2nCDknFzaI4wvtnCoCXHNWwxMI5ya9vBL5vxo5571aydoEUvcVf4CHFWc%2Fx7UVscHI05qLJ5ges73W2hudv2PNGu7yruH21qi5wVLmaOqsc66WOb%2FVhY6Jz7ElzCWmu%2Fq6XWpRHuTJCEqP4h42IXsenyQF%2FuWRArfEUtoT4wxZzqGwMnKv5U7JNTSL13GN6NP1O5VHslpuUt446XtJwUHKVKmw5gk5TFuq%2B5gf7kpw42GbuXx15YpnwiPgCe67Zjt2zEedC0hCqX4T1LsJjIWqbXIBtaXSzB%2FkTOaFM1LrxbgFD2J7mrE3EgVsqF8tUlAQyfgx6y6DhoFFFAmwcxynZNMGxLglOfBi5tWctYOOFO9TwkQXbbzdMjb84%2FZ3GhcbFpTX0D%2ByRg%2F%2FgSzVeyQdFmmIk3oY2EZaKpfCgUeSeiEG2Ce67TPRkfgv06NSIjx7hLv2Om6VWl5OKEefse87LHDf%2Fv2DXu569zHWGqmannmwFIHzQ%2BkXxMsO3cFHbuhRWXPZpZ3AYiFeyGF4DZM%2FT56ngjRHDpgxXxNW%2FalwXSqhcsWqwYzCG%2Bpa9BjqkAXfAEuQVamA4G%2BP1zzM%2BqYiNZuNx6VyHCUF7uVkbEbtxJa6txuPDAEVKQTyFDEw%2FWKN4Bg6yXmOnTN4A5k%2BK6hOd%2BKyzhigYb%2BJB6pzrZpZLRbzLItDP8fMU2JN53Takgn6Q8IBZQRmJ%2FSj1WTrQ2xlT8hTcubCvVRHcwBx1AUSWqgFibNmTtFKdAzUaJae6PDLTwMVL6zSji6Flkuloh6jjZqmj&X-Amz-Signature=15d74abedb6a6f951b6446c7fe8f490fec42e7e3bc329f9c9bde80cbaf411677&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QOSC54L%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQC7VMupRu2F1c%2FBc47ghJb87S7pXNXl652YwVaAXudQYgIhAOeZsZbCwWhh%2F0z0nwVsQp1ohE1TF5wQmEeyrNY77REHKv8DCHEQABoMNjM3NDIzMTgzODA1IgxiVSVmpOJeaf1Y%2BeEq3AMbb%2FDW1n06J749%2B6mYJ1dauykUyuAC0g4VlE8%2Fd%2Fi2zzI57%2BSMUCjFjgCHL3j16klwiux6U2nCDknFzaI4wvtnCoCXHNWwxMI5ya9vBL5vxo5571aydoEUvcVf4CHFWc%2Fx7UVscHI05qLJ5ges73W2hudv2PNGu7yruH21qi5wVLmaOqsc66WOb%2FVhY6Jz7ElzCWmu%2Fq6XWpRHuTJCEqP4h42IXsenyQF%2FuWRArfEUtoT4wxZzqGwMnKv5U7JNTSL13GN6NP1O5VHslpuUt446XtJwUHKVKmw5gk5TFuq%2B5gf7kpw42GbuXx15YpnwiPgCe67Zjt2zEedC0hCqX4T1LsJjIWqbXIBtaXSzB%2FkTOaFM1LrxbgFD2J7mrE3EgVsqF8tUlAQyfgx6y6DhoFFFAmwcxynZNMGxLglOfBi5tWctYOOFO9TwkQXbbzdMjb84%2FZ3GhcbFpTX0D%2ByRg%2F%2FgSzVeyQdFmmIk3oY2EZaKpfCgUeSeiEG2Ce67TPRkfgv06NSIjx7hLv2Om6VWl5OKEefse87LHDf%2Fv2DXu569zHWGqmannmwFIHzQ%2BkXxMsO3cFHbuhRWXPZpZ3AYiFeyGF4DZM%2FT56ngjRHDpgxXxNW%2FalwXSqhcsWqwYzCG%2Bpa9BjqkAXfAEuQVamA4G%2BP1zzM%2BqYiNZuNx6VyHCUF7uVkbEbtxJa6txuPDAEVKQTyFDEw%2FWKN4Bg6yXmOnTN4A5k%2BK6hOd%2BKyzhigYb%2BJB6pzrZpZLRbzLItDP8fMU2JN53Takgn6Q8IBZQRmJ%2FSj1WTrQ2xlT8hTcubCvVRHcwBx1AUSWqgFibNmTtFKdAzUaJae6PDLTwMVL6zSji6Flkuloh6jjZqmj&X-Amz-Signature=0ee44c93b123814bd102494e5f87c3508c580b77ec5e3c94c6089f25527f0d29&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QOSC54L%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQC7VMupRu2F1c%2FBc47ghJb87S7pXNXl652YwVaAXudQYgIhAOeZsZbCwWhh%2F0z0nwVsQp1ohE1TF5wQmEeyrNY77REHKv8DCHEQABoMNjM3NDIzMTgzODA1IgxiVSVmpOJeaf1Y%2BeEq3AMbb%2FDW1n06J749%2B6mYJ1dauykUyuAC0g4VlE8%2Fd%2Fi2zzI57%2BSMUCjFjgCHL3j16klwiux6U2nCDknFzaI4wvtnCoCXHNWwxMI5ya9vBL5vxo5571aydoEUvcVf4CHFWc%2Fx7UVscHI05qLJ5ges73W2hudv2PNGu7yruH21qi5wVLmaOqsc66WOb%2FVhY6Jz7ElzCWmu%2Fq6XWpRHuTJCEqP4h42IXsenyQF%2FuWRArfEUtoT4wxZzqGwMnKv5U7JNTSL13GN6NP1O5VHslpuUt446XtJwUHKVKmw5gk5TFuq%2B5gf7kpw42GbuXx15YpnwiPgCe67Zjt2zEedC0hCqX4T1LsJjIWqbXIBtaXSzB%2FkTOaFM1LrxbgFD2J7mrE3EgVsqF8tUlAQyfgx6y6DhoFFFAmwcxynZNMGxLglOfBi5tWctYOOFO9TwkQXbbzdMjb84%2FZ3GhcbFpTX0D%2ByRg%2F%2FgSzVeyQdFmmIk3oY2EZaKpfCgUeSeiEG2Ce67TPRkfgv06NSIjx7hLv2Om6VWl5OKEefse87LHDf%2Fv2DXu569zHWGqmannmwFIHzQ%2BkXxMsO3cFHbuhRWXPZpZ3AYiFeyGF4DZM%2FT56ngjRHDpgxXxNW%2FalwXSqhcsWqwYzCG%2Bpa9BjqkAXfAEuQVamA4G%2BP1zzM%2BqYiNZuNx6VyHCUF7uVkbEbtxJa6txuPDAEVKQTyFDEw%2FWKN4Bg6yXmOnTN4A5k%2BK6hOd%2BKyzhigYb%2BJB6pzrZpZLRbzLItDP8fMU2JN53Takgn6Q8IBZQRmJ%2FSj1WTrQ2xlT8hTcubCvVRHcwBx1AUSWqgFibNmTtFKdAzUaJae6PDLTwMVL6zSji6Flkuloh6jjZqmj&X-Amz-Signature=2d231d217484b1b1aecdd11fd3cdedea65ae8979d5bb25d4d3d95d694ad07956&X-Amz-SignedHeaders=host&x-id=GetObject)
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


