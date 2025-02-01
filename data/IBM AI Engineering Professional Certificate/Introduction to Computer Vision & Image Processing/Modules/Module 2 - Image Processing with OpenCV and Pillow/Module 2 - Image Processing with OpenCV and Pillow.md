

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPL4QATW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCK8DFANv7mwF7e46QdXI25ny67jTsKgFD7ULz8k4qShAIgFiT%2BPeIjYAFB3FX1GuIvTARVHQV8H72tlkBIdS%2BaahcqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPwzq1nmGARnn%2FH54CrcA1Lewmh7F%2Bwic9G%2BRq%2F7mlCD7HM0UNTqA3GQrSvtehggY0aenQqoiVPsWwWNXozwddmtZNIvEqIdkNQI%2FuD6bYxSzvaYyVESm3sZLpGJPLzMkStsh9J8qrpakFbrlwl2fQZ2ARZYumO1X%2FA88v3zNq%2F1xH%2BWdiGb3hlyRx0KmskyqKRHuVGOcC5%2Fvw%2FaKDoih3chR6imez22b0AbEGovN2l8He81cm2w2I8bYlFpxXYVQpcHZLXiJX0Jyatfd1496k9a0idhrYlJfBW9kzACX2aY3roXY%2FSSqRDBtv2HLrKItYtFx5J44KlB6YEu1CQGZZtI94LUIslkNEEjbXWIszAv6fLI8lRqaxeHRiIhGN2MeCkuqnWsxtfSEUZ1BJcA9feDIr2k802iP55P6vtygGD9qieHov4w%2BvvoOeQes53ld%2BFwaWb%2FbWedagjc%2Ft2PQxFpaZ3zPX3dJ8ZspVb0kZI68RbT8zqDmfffEJlO%2BoZsqc99Rj%2BXOosVUa0PFfaWx1W5Rkchsp%2FaQkRMEwWoYv2%2B%2FbeQBN%2FK41onuK57Fh%2B2xfapoEaXAK7kw%2FvBF76dWvaKYP6iDZgFvut5Xhh%2BTV%2BhE%2FQbAEfjldnQNv9%2FAYjZzhRnBRfnFm4XnxpeMJjB9rwGOqUBSK5rtFeSZ%2FkCoFaL%2BlU7VLynDi8eLxzhwV6DYbi7TBaFleIhHU1bLfcIY0rBhp%2BHHymKJfrmlKH0OxzVlvTA9nMwaiBEMSh3Af6usMhueTIE26rOfbjKuoa888U4FH6aZDS60n%2BHMmoOqun%2FRL%2Bmk4pFOjCTCGEV9cAh0bZzjvf4qx5WVG0eDKz9wCjI88UqCInDBc2vjart5KAok1zNFC6cA3BX&X-Amz-Signature=131875d8a946fea0103635ab398197bdb29e99507c4d265448e57c0f4dd0c425&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPF33DXW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG49bbjpfLEttnpGzlL6hvRQjpop91%2F1WwUVWecs3gQCAiAWYKI1wpHGX%2BzyXT6QBt0s2j9wCFaNeXBNjpo0gpJjJyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcDkmOtKdywh%2FQhkIKtwDFzZU34Ati2iDF6cbYJaoj9xwzmP8%2FiSL3KS6x%2Biwdu3HyH0E%2BjBy%2Fefp8qafg3TESmfsQHQfdTtXwLlQp%2BFkN%2Bg6OBX0BdaZdC6le2vTMKvTXoCj8o7an7%2FWhJju6qAeBXuKjOLE6HA7AuY0gUj2S8%2BMA8LDxQdvfmptQwCDiukox44gu6vYyUHfbcC9QrwipbCVEs4sIuNSs4KZPI9cD%2ByxzwvziK3wXcZra1dbjlfEHip83acrGCHRLwyXJUg5P5q%2BIZMOIAFLaPouWeW%2BlP8MSznnQTWmcs6EnGhZXIzxKh0bwgTsjfzpcuzgej8d%2B0Y5fqncvKx4%2FOKFaz2KNMjnjhORPW%2Bo6GFnMyBfQUft8yP%2Bp5E%2FWbQXoc1pf14cKRthK%2FsCqpB%2F4S594b9U%2Bl7A911nUrXqKk21%2FkzmAc6k1dWp7%2B6OEi0jedNo6hzr2%2BTxQ%2BdeKsuIIPucDeiF9652bAERKUAUm9SfwlZRAgS0gsIa%2BX9iaTejlGvi6HFc8AmW3smvhQ3x7WJdmt4%2FZkuEIp5xjrPhwch9otjCEGxtpAXoYdek6KHdJQNeGaBvc2REwD8JJovyHr7rXviHMPAoTdEimQHbo0%2FiWicwIKdA7zb9tL7oBteFu%2Bgw4MH2vAY6pgGktgfXBddxMbV1%2BJZb%2B%2By2soBWMmJ5mt%2B0oKDI%2FSEL3iG7Hn30fmcS2kV2OF7%2BWPmKXyP9wuZ9HEAWmMbk%2B2FDi2%2BZTIqnLh%2ByzcRy4PG0GNKl27ryV8bMJp1maPSvnb8lKYADDBcdWDBBBsD6c90HyUbekeVhq949%2BWXldweWsFIzWQ%2F7wzbBze5hk6p8%2BMiRFcRgTgGLP%2FVsysCHySQqenW0SipD&X-Amz-Signature=3b238ca4391fd0acb5daec1747d6d68ee1e1b5afc65634db17dd3f2e94dc1746&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPF33DXW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG49bbjpfLEttnpGzlL6hvRQjpop91%2F1WwUVWecs3gQCAiAWYKI1wpHGX%2BzyXT6QBt0s2j9wCFaNeXBNjpo0gpJjJyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcDkmOtKdywh%2FQhkIKtwDFzZU34Ati2iDF6cbYJaoj9xwzmP8%2FiSL3KS6x%2Biwdu3HyH0E%2BjBy%2Fefp8qafg3TESmfsQHQfdTtXwLlQp%2BFkN%2Bg6OBX0BdaZdC6le2vTMKvTXoCj8o7an7%2FWhJju6qAeBXuKjOLE6HA7AuY0gUj2S8%2BMA8LDxQdvfmptQwCDiukox44gu6vYyUHfbcC9QrwipbCVEs4sIuNSs4KZPI9cD%2ByxzwvziK3wXcZra1dbjlfEHip83acrGCHRLwyXJUg5P5q%2BIZMOIAFLaPouWeW%2BlP8MSznnQTWmcs6EnGhZXIzxKh0bwgTsjfzpcuzgej8d%2B0Y5fqncvKx4%2FOKFaz2KNMjnjhORPW%2Bo6GFnMyBfQUft8yP%2Bp5E%2FWbQXoc1pf14cKRthK%2FsCqpB%2F4S594b9U%2Bl7A911nUrXqKk21%2FkzmAc6k1dWp7%2B6OEi0jedNo6hzr2%2BTxQ%2BdeKsuIIPucDeiF9652bAERKUAUm9SfwlZRAgS0gsIa%2BX9iaTejlGvi6HFc8AmW3smvhQ3x7WJdmt4%2FZkuEIp5xjrPhwch9otjCEGxtpAXoYdek6KHdJQNeGaBvc2REwD8JJovyHr7rXviHMPAoTdEimQHbo0%2FiWicwIKdA7zb9tL7oBteFu%2Bgw4MH2vAY6pgGktgfXBddxMbV1%2BJZb%2B%2By2soBWMmJ5mt%2B0oKDI%2FSEL3iG7Hn30fmcS2kV2OF7%2BWPmKXyP9wuZ9HEAWmMbk%2B2FDi2%2BZTIqnLh%2ByzcRy4PG0GNKl27ryV8bMJp1maPSvnb8lKYADDBcdWDBBBsD6c90HyUbekeVhq949%2BWXldweWsFIzWQ%2F7wzbBze5hk6p8%2BMiRFcRgTgGLP%2FVsysCHySQqenW0SipD&X-Amz-Signature=1905d7f0b5c42a13ff9b55ad04bd8264f1d6a2f0e125a33ba946cceb663a2963&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPF33DXW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG49bbjpfLEttnpGzlL6hvRQjpop91%2F1WwUVWecs3gQCAiAWYKI1wpHGX%2BzyXT6QBt0s2j9wCFaNeXBNjpo0gpJjJyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcDkmOtKdywh%2FQhkIKtwDFzZU34Ati2iDF6cbYJaoj9xwzmP8%2FiSL3KS6x%2Biwdu3HyH0E%2BjBy%2Fefp8qafg3TESmfsQHQfdTtXwLlQp%2BFkN%2Bg6OBX0BdaZdC6le2vTMKvTXoCj8o7an7%2FWhJju6qAeBXuKjOLE6HA7AuY0gUj2S8%2BMA8LDxQdvfmptQwCDiukox44gu6vYyUHfbcC9QrwipbCVEs4sIuNSs4KZPI9cD%2ByxzwvziK3wXcZra1dbjlfEHip83acrGCHRLwyXJUg5P5q%2BIZMOIAFLaPouWeW%2BlP8MSznnQTWmcs6EnGhZXIzxKh0bwgTsjfzpcuzgej8d%2B0Y5fqncvKx4%2FOKFaz2KNMjnjhORPW%2Bo6GFnMyBfQUft8yP%2Bp5E%2FWbQXoc1pf14cKRthK%2FsCqpB%2F4S594b9U%2Bl7A911nUrXqKk21%2FkzmAc6k1dWp7%2B6OEi0jedNo6hzr2%2BTxQ%2BdeKsuIIPucDeiF9652bAERKUAUm9SfwlZRAgS0gsIa%2BX9iaTejlGvi6HFc8AmW3smvhQ3x7WJdmt4%2FZkuEIp5xjrPhwch9otjCEGxtpAXoYdek6KHdJQNeGaBvc2REwD8JJovyHr7rXviHMPAoTdEimQHbo0%2FiWicwIKdA7zb9tL7oBteFu%2Bgw4MH2vAY6pgGktgfXBddxMbV1%2BJZb%2B%2By2soBWMmJ5mt%2B0oKDI%2FSEL3iG7Hn30fmcS2kV2OF7%2BWPmKXyP9wuZ9HEAWmMbk%2B2FDi2%2BZTIqnLh%2ByzcRy4PG0GNKl27ryV8bMJp1maPSvnb8lKYADDBcdWDBBBsD6c90HyUbekeVhq949%2BWXldweWsFIzWQ%2F7wzbBze5hk6p8%2BMiRFcRgTgGLP%2FVsysCHySQqenW0SipD&X-Amz-Signature=00aa6254b197ff206ae6befb7688f2414c38a30a80dfe97fd57c1a1b1b7d233e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPF33DXW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG49bbjpfLEttnpGzlL6hvRQjpop91%2F1WwUVWecs3gQCAiAWYKI1wpHGX%2BzyXT6QBt0s2j9wCFaNeXBNjpo0gpJjJyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcDkmOtKdywh%2FQhkIKtwDFzZU34Ati2iDF6cbYJaoj9xwzmP8%2FiSL3KS6x%2Biwdu3HyH0E%2BjBy%2Fefp8qafg3TESmfsQHQfdTtXwLlQp%2BFkN%2Bg6OBX0BdaZdC6le2vTMKvTXoCj8o7an7%2FWhJju6qAeBXuKjOLE6HA7AuY0gUj2S8%2BMA8LDxQdvfmptQwCDiukox44gu6vYyUHfbcC9QrwipbCVEs4sIuNSs4KZPI9cD%2ByxzwvziK3wXcZra1dbjlfEHip83acrGCHRLwyXJUg5P5q%2BIZMOIAFLaPouWeW%2BlP8MSznnQTWmcs6EnGhZXIzxKh0bwgTsjfzpcuzgej8d%2B0Y5fqncvKx4%2FOKFaz2KNMjnjhORPW%2Bo6GFnMyBfQUft8yP%2Bp5E%2FWbQXoc1pf14cKRthK%2FsCqpB%2F4S594b9U%2Bl7A911nUrXqKk21%2FkzmAc6k1dWp7%2B6OEi0jedNo6hzr2%2BTxQ%2BdeKsuIIPucDeiF9652bAERKUAUm9SfwlZRAgS0gsIa%2BX9iaTejlGvi6HFc8AmW3smvhQ3x7WJdmt4%2FZkuEIp5xjrPhwch9otjCEGxtpAXoYdek6KHdJQNeGaBvc2REwD8JJovyHr7rXviHMPAoTdEimQHbo0%2FiWicwIKdA7zb9tL7oBteFu%2Bgw4MH2vAY6pgGktgfXBddxMbV1%2BJZb%2B%2By2soBWMmJ5mt%2B0oKDI%2FSEL3iG7Hn30fmcS2kV2OF7%2BWPmKXyP9wuZ9HEAWmMbk%2B2FDi2%2BZTIqnLh%2ByzcRy4PG0GNKl27ryV8bMJp1maPSvnb8lKYADDBcdWDBBBsD6c90HyUbekeVhq949%2BWXldweWsFIzWQ%2F7wzbBze5hk6p8%2BMiRFcRgTgGLP%2FVsysCHySQqenW0SipD&X-Amz-Signature=2d990658597b7c8f94ab10c5460514415f84c3b52a478ef973a510b32e03a1bd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPF33DXW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG49bbjpfLEttnpGzlL6hvRQjpop91%2F1WwUVWecs3gQCAiAWYKI1wpHGX%2BzyXT6QBt0s2j9wCFaNeXBNjpo0gpJjJyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcDkmOtKdywh%2FQhkIKtwDFzZU34Ati2iDF6cbYJaoj9xwzmP8%2FiSL3KS6x%2Biwdu3HyH0E%2BjBy%2Fefp8qafg3TESmfsQHQfdTtXwLlQp%2BFkN%2Bg6OBX0BdaZdC6le2vTMKvTXoCj8o7an7%2FWhJju6qAeBXuKjOLE6HA7AuY0gUj2S8%2BMA8LDxQdvfmptQwCDiukox44gu6vYyUHfbcC9QrwipbCVEs4sIuNSs4KZPI9cD%2ByxzwvziK3wXcZra1dbjlfEHip83acrGCHRLwyXJUg5P5q%2BIZMOIAFLaPouWeW%2BlP8MSznnQTWmcs6EnGhZXIzxKh0bwgTsjfzpcuzgej8d%2B0Y5fqncvKx4%2FOKFaz2KNMjnjhORPW%2Bo6GFnMyBfQUft8yP%2Bp5E%2FWbQXoc1pf14cKRthK%2FsCqpB%2F4S594b9U%2Bl7A911nUrXqKk21%2FkzmAc6k1dWp7%2B6OEi0jedNo6hzr2%2BTxQ%2BdeKsuIIPucDeiF9652bAERKUAUm9SfwlZRAgS0gsIa%2BX9iaTejlGvi6HFc8AmW3smvhQ3x7WJdmt4%2FZkuEIp5xjrPhwch9otjCEGxtpAXoYdek6KHdJQNeGaBvc2REwD8JJovyHr7rXviHMPAoTdEimQHbo0%2FiWicwIKdA7zb9tL7oBteFu%2Bgw4MH2vAY6pgGktgfXBddxMbV1%2BJZb%2B%2By2soBWMmJ5mt%2B0oKDI%2FSEL3iG7Hn30fmcS2kV2OF7%2BWPmKXyP9wuZ9HEAWmMbk%2B2FDi2%2BZTIqnLh%2ByzcRy4PG0GNKl27ryV8bMJp1maPSvnb8lKYADDBcdWDBBBsD6c90HyUbekeVhq949%2BWXldweWsFIzWQ%2F7wzbBze5hk6p8%2BMiRFcRgTgGLP%2FVsysCHySQqenW0SipD&X-Amz-Signature=bb6d009b81f68aebc337b62c462539ec6556faa5ef413520012ab32c7a3ad07e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPL4QATW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCK8DFANv7mwF7e46QdXI25ny67jTsKgFD7ULz8k4qShAIgFiT%2BPeIjYAFB3FX1GuIvTARVHQV8H72tlkBIdS%2BaahcqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPwzq1nmGARnn%2FH54CrcA1Lewmh7F%2Bwic9G%2BRq%2F7mlCD7HM0UNTqA3GQrSvtehggY0aenQqoiVPsWwWNXozwddmtZNIvEqIdkNQI%2FuD6bYxSzvaYyVESm3sZLpGJPLzMkStsh9J8qrpakFbrlwl2fQZ2ARZYumO1X%2FA88v3zNq%2F1xH%2BWdiGb3hlyRx0KmskyqKRHuVGOcC5%2Fvw%2FaKDoih3chR6imez22b0AbEGovN2l8He81cm2w2I8bYlFpxXYVQpcHZLXiJX0Jyatfd1496k9a0idhrYlJfBW9kzACX2aY3roXY%2FSSqRDBtv2HLrKItYtFx5J44KlB6YEu1CQGZZtI94LUIslkNEEjbXWIszAv6fLI8lRqaxeHRiIhGN2MeCkuqnWsxtfSEUZ1BJcA9feDIr2k802iP55P6vtygGD9qieHov4w%2BvvoOeQes53ld%2BFwaWb%2FbWedagjc%2Ft2PQxFpaZ3zPX3dJ8ZspVb0kZI68RbT8zqDmfffEJlO%2BoZsqc99Rj%2BXOosVUa0PFfaWx1W5Rkchsp%2FaQkRMEwWoYv2%2B%2FbeQBN%2FK41onuK57Fh%2B2xfapoEaXAK7kw%2FvBF76dWvaKYP6iDZgFvut5Xhh%2BTV%2BhE%2FQbAEfjldnQNv9%2FAYjZzhRnBRfnFm4XnxpeMJjB9rwGOqUBSK5rtFeSZ%2FkCoFaL%2BlU7VLynDi8eLxzhwV6DYbi7TBaFleIhHU1bLfcIY0rBhp%2BHHymKJfrmlKH0OxzVlvTA9nMwaiBEMSh3Af6usMhueTIE26rOfbjKuoa888U4FH6aZDS60n%2BHMmoOqun%2FRL%2Bmk4pFOjCTCGEV9cAh0bZzjvf4qx5WVG0eDKz9wCjI88UqCInDBc2vjart5KAok1zNFC6cA3BX&X-Amz-Signature=afa31ab259cffcfbf0d7f8c8013810717f3f401a514dfc929fb272fd3aa96d0c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPL4QATW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCK8DFANv7mwF7e46QdXI25ny67jTsKgFD7ULz8k4qShAIgFiT%2BPeIjYAFB3FX1GuIvTARVHQV8H72tlkBIdS%2BaahcqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPwzq1nmGARnn%2FH54CrcA1Lewmh7F%2Bwic9G%2BRq%2F7mlCD7HM0UNTqA3GQrSvtehggY0aenQqoiVPsWwWNXozwddmtZNIvEqIdkNQI%2FuD6bYxSzvaYyVESm3sZLpGJPLzMkStsh9J8qrpakFbrlwl2fQZ2ARZYumO1X%2FA88v3zNq%2F1xH%2BWdiGb3hlyRx0KmskyqKRHuVGOcC5%2Fvw%2FaKDoih3chR6imez22b0AbEGovN2l8He81cm2w2I8bYlFpxXYVQpcHZLXiJX0Jyatfd1496k9a0idhrYlJfBW9kzACX2aY3roXY%2FSSqRDBtv2HLrKItYtFx5J44KlB6YEu1CQGZZtI94LUIslkNEEjbXWIszAv6fLI8lRqaxeHRiIhGN2MeCkuqnWsxtfSEUZ1BJcA9feDIr2k802iP55P6vtygGD9qieHov4w%2BvvoOeQes53ld%2BFwaWb%2FbWedagjc%2Ft2PQxFpaZ3zPX3dJ8ZspVb0kZI68RbT8zqDmfffEJlO%2BoZsqc99Rj%2BXOosVUa0PFfaWx1W5Rkchsp%2FaQkRMEwWoYv2%2B%2FbeQBN%2FK41onuK57Fh%2B2xfapoEaXAK7kw%2FvBF76dWvaKYP6iDZgFvut5Xhh%2BTV%2BhE%2FQbAEfjldnQNv9%2FAYjZzhRnBRfnFm4XnxpeMJjB9rwGOqUBSK5rtFeSZ%2FkCoFaL%2BlU7VLynDi8eLxzhwV6DYbi7TBaFleIhHU1bLfcIY0rBhp%2BHHymKJfrmlKH0OxzVlvTA9nMwaiBEMSh3Af6usMhueTIE26rOfbjKuoa888U4FH6aZDS60n%2BHMmoOqun%2FRL%2Bmk4pFOjCTCGEV9cAh0bZzjvf4qx5WVG0eDKz9wCjI88UqCInDBc2vjart5KAok1zNFC6cA3BX&X-Amz-Signature=76e178de4d10fdb6cee21b52e5f49344841930c9d4d03decc2e4c749250d8711&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPL4QATW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCK8DFANv7mwF7e46QdXI25ny67jTsKgFD7ULz8k4qShAIgFiT%2BPeIjYAFB3FX1GuIvTARVHQV8H72tlkBIdS%2BaahcqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPwzq1nmGARnn%2FH54CrcA1Lewmh7F%2Bwic9G%2BRq%2F7mlCD7HM0UNTqA3GQrSvtehggY0aenQqoiVPsWwWNXozwddmtZNIvEqIdkNQI%2FuD6bYxSzvaYyVESm3sZLpGJPLzMkStsh9J8qrpakFbrlwl2fQZ2ARZYumO1X%2FA88v3zNq%2F1xH%2BWdiGb3hlyRx0KmskyqKRHuVGOcC5%2Fvw%2FaKDoih3chR6imez22b0AbEGovN2l8He81cm2w2I8bYlFpxXYVQpcHZLXiJX0Jyatfd1496k9a0idhrYlJfBW9kzACX2aY3roXY%2FSSqRDBtv2HLrKItYtFx5J44KlB6YEu1CQGZZtI94LUIslkNEEjbXWIszAv6fLI8lRqaxeHRiIhGN2MeCkuqnWsxtfSEUZ1BJcA9feDIr2k802iP55P6vtygGD9qieHov4w%2BvvoOeQes53ld%2BFwaWb%2FbWedagjc%2Ft2PQxFpaZ3zPX3dJ8ZspVb0kZI68RbT8zqDmfffEJlO%2BoZsqc99Rj%2BXOosVUa0PFfaWx1W5Rkchsp%2FaQkRMEwWoYv2%2B%2FbeQBN%2FK41onuK57Fh%2B2xfapoEaXAK7kw%2FvBF76dWvaKYP6iDZgFvut5Xhh%2BTV%2BhE%2FQbAEfjldnQNv9%2FAYjZzhRnBRfnFm4XnxpeMJjB9rwGOqUBSK5rtFeSZ%2FkCoFaL%2BlU7VLynDi8eLxzhwV6DYbi7TBaFleIhHU1bLfcIY0rBhp%2BHHymKJfrmlKH0OxzVlvTA9nMwaiBEMSh3Af6usMhueTIE26rOfbjKuoa888U4FH6aZDS60n%2BHMmoOqun%2FRL%2Bmk4pFOjCTCGEV9cAh0bZzjvf4qx5WVG0eDKz9wCjI88UqCInDBc2vjart5KAok1zNFC6cA3BX&X-Amz-Signature=a1ee8bb917b9967904b64285c757ea2cbd08f3bc2282d76b4a34e6905007d9c5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPL4QATW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCK8DFANv7mwF7e46QdXI25ny67jTsKgFD7ULz8k4qShAIgFiT%2BPeIjYAFB3FX1GuIvTARVHQV8H72tlkBIdS%2BaahcqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPwzq1nmGARnn%2FH54CrcA1Lewmh7F%2Bwic9G%2BRq%2F7mlCD7HM0UNTqA3GQrSvtehggY0aenQqoiVPsWwWNXozwddmtZNIvEqIdkNQI%2FuD6bYxSzvaYyVESm3sZLpGJPLzMkStsh9J8qrpakFbrlwl2fQZ2ARZYumO1X%2FA88v3zNq%2F1xH%2BWdiGb3hlyRx0KmskyqKRHuVGOcC5%2Fvw%2FaKDoih3chR6imez22b0AbEGovN2l8He81cm2w2I8bYlFpxXYVQpcHZLXiJX0Jyatfd1496k9a0idhrYlJfBW9kzACX2aY3roXY%2FSSqRDBtv2HLrKItYtFx5J44KlB6YEu1CQGZZtI94LUIslkNEEjbXWIszAv6fLI8lRqaxeHRiIhGN2MeCkuqnWsxtfSEUZ1BJcA9feDIr2k802iP55P6vtygGD9qieHov4w%2BvvoOeQes53ld%2BFwaWb%2FbWedagjc%2Ft2PQxFpaZ3zPX3dJ8ZspVb0kZI68RbT8zqDmfffEJlO%2BoZsqc99Rj%2BXOosVUa0PFfaWx1W5Rkchsp%2FaQkRMEwWoYv2%2B%2FbeQBN%2FK41onuK57Fh%2B2xfapoEaXAK7kw%2FvBF76dWvaKYP6iDZgFvut5Xhh%2BTV%2BhE%2FQbAEfjldnQNv9%2FAYjZzhRnBRfnFm4XnxpeMJjB9rwGOqUBSK5rtFeSZ%2FkCoFaL%2BlU7VLynDi8eLxzhwV6DYbi7TBaFleIhHU1bLfcIY0rBhp%2BHHymKJfrmlKH0OxzVlvTA9nMwaiBEMSh3Af6usMhueTIE26rOfbjKuoa888U4FH6aZDS60n%2BHMmoOqun%2FRL%2Bmk4pFOjCTCGEV9cAh0bZzjvf4qx5WVG0eDKz9wCjI88UqCInDBc2vjart5KAok1zNFC6cA3BX&X-Amz-Signature=b5517819d24d46c886f02f1583913c1ac3f6cde50e791f08e1b9248d2eceb07f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPL4QATW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCK8DFANv7mwF7e46QdXI25ny67jTsKgFD7ULz8k4qShAIgFiT%2BPeIjYAFB3FX1GuIvTARVHQV8H72tlkBIdS%2BaahcqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPwzq1nmGARnn%2FH54CrcA1Lewmh7F%2Bwic9G%2BRq%2F7mlCD7HM0UNTqA3GQrSvtehggY0aenQqoiVPsWwWNXozwddmtZNIvEqIdkNQI%2FuD6bYxSzvaYyVESm3sZLpGJPLzMkStsh9J8qrpakFbrlwl2fQZ2ARZYumO1X%2FA88v3zNq%2F1xH%2BWdiGb3hlyRx0KmskyqKRHuVGOcC5%2Fvw%2FaKDoih3chR6imez22b0AbEGovN2l8He81cm2w2I8bYlFpxXYVQpcHZLXiJX0Jyatfd1496k9a0idhrYlJfBW9kzACX2aY3roXY%2FSSqRDBtv2HLrKItYtFx5J44KlB6YEu1CQGZZtI94LUIslkNEEjbXWIszAv6fLI8lRqaxeHRiIhGN2MeCkuqnWsxtfSEUZ1BJcA9feDIr2k802iP55P6vtygGD9qieHov4w%2BvvoOeQes53ld%2BFwaWb%2FbWedagjc%2Ft2PQxFpaZ3zPX3dJ8ZspVb0kZI68RbT8zqDmfffEJlO%2BoZsqc99Rj%2BXOosVUa0PFfaWx1W5Rkchsp%2FaQkRMEwWoYv2%2B%2FbeQBN%2FK41onuK57Fh%2B2xfapoEaXAK7kw%2FvBF76dWvaKYP6iDZgFvut5Xhh%2BTV%2BhE%2FQbAEfjldnQNv9%2FAYjZzhRnBRfnFm4XnxpeMJjB9rwGOqUBSK5rtFeSZ%2FkCoFaL%2BlU7VLynDi8eLxzhwV6DYbi7TBaFleIhHU1bLfcIY0rBhp%2BHHymKJfrmlKH0OxzVlvTA9nMwaiBEMSh3Af6usMhueTIE26rOfbjKuoa888U4FH6aZDS60n%2BHMmoOqun%2FRL%2Bmk4pFOjCTCGEV9cAh0bZzjvf4qx5WVG0eDKz9wCjI88UqCInDBc2vjart5KAok1zNFC6cA3BX&X-Amz-Signature=73a00ab67e899bd5134a4f5baeba8c50353b724f01a6aac45e63414e7641a9e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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


