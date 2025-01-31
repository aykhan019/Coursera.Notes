

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CKFGZJN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHXfqNgWA0Fyf7NXTEMnGziHcEtYi2%2FFmN%2BeW4oQRhhfAiAL25QP1AHxZuFxfuVsA1n%2BxkuYi0SX9MugjihDbst8miqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8to5IWR1SnXn5oA%2BKtwDmt%2FJIZyTuDZNFqHhSrfOS7sUW89YCIdQWxsghHo5tHEmoj4osDaC63pwXD4UDMTUXy0PklAm%2BcpdTR8w9PTDOMs%2FnnQQy5j2M2TJKYjZq5dQje5pgPgAsx7at8HUImV%2Bgoc6nkohDMFOF0DlOnv6DzNKey%2FUy%2BbeIt73xzd3IoBpFZr0q2X55yYvIZr3MozK%2BAVdx6Wxc5DlBhJrY5SoHx0NmA9ORaTFNklIWnIQJnirqknJNZKhwTKgXdrEXYuB3FNTV7w8uur%2FaJNzffbHs03qi1mDl19mtsblGLha1u2Y0Bc75R7B9tKc%2B8B7wX%2BYKP2OSiJz3xzTonGLU74QLdyyR6txshCS8qtCqnxDQqX%2FYyza8gYSkH8A5Gzf4yt9SgxFRVb5i2KKbEkB%2BnXCh2UWtckcTK%2FO%2BeGcUxytXlXifWIQNxsBNxPqXjOL8QdSvg%2FoFmYbWYgAHH2sQiHD55%2B46TI7Wul1EAGox4EuTdq1PpgXCPyrfUBW%2BNowfEg%2FvtHCLSnkWR93OuS7O675ivTOEltMWY5VJ18cl49IX2TuIFenbJ7f9RTUuj7ynN9CTlK7%2Bv9YrPIB1UnRzMgz92tsGk8dSzhRXfCuDVSi6s5FCIMXQ5aXbwpBKqEwl%2BvzvAY6pgEXXYN4tEDfKtcFObqm78VMJRk96H4M3pjEVqsp4BVNs2bwVEdvSREIey3CQ8Z%2FWvo3GQC%2B1o5i5VxrqgMdlb0%2Be%2Bvilsc5Rf6qDpslFIhPl%2Fn1b9rHnqIOT3bvjeMiFnHp8RLGZuO%2B4UScPfx6IIkjTT%2BnLu4e187vUXnN4dBF%2FcpY09FLg9MwGKYpK%2BaEJbaxdmnPbIY6oRMI9WeNLT%2B50iL1dXau&X-Amz-Signature=362bc699190dff7a666850e6230d03e3517fd87a02201561c8054092ce06b238&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGR332ZM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCErBy8HWD55kBTdKXNvHxyH%2F3uwPAkzrTgBA6sX4khQgIga2Pf7llPYZ6FBBbGHO6wfWvGo69C1fw8FP5GWnl9m9YqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqVTYKkI0%2BlyawKzircAzxvspiso1%2FxiU95KR%2FYqq%2BLO9qD%2F3YSiG2sMolkDY0aHDZPbShlSQATJitzMeB3NVo86od4vv%2FVnz%2F7ngZ7F9Bu9NwSkPhsRJG6TysO4so%2BOrswbjpKEenRQhGbmxCXl5rHkwqwDr2IQAH7GDq0ZpCe8vm%2BZ%2BBDjRQzess4Kruw2KctYpegKYnF4slE92BzYV8Di0VzPf03HLFejGOIyvQRCorLX8GnR49s1jBR%2BlN0TF6N%2FJ9yV3o04%2Ft2xpC%2BPiUEuQjbogSVPfa1KV3aGRTAy%2B6IRrvXOjIDIBKemfH%2FQa9Kp9vO7RJbAG2Zmr2tgaJBfkaa5AXDUh0V47jNbswGwmccMB5iUisSEhFxNrgvjw6HsZ3REc5dDbKpK7OUuxLF9E5T6x2sZ2zuMo4mSXKoCrrVgREyWNf0AnWGbeNs4rn0XvtOLrev%2BDWBOOiDnFa7gnOUDR8JKwW0k%2FQf2cLH1i9apMM7GRuqe%2F7zOrLERWprQ1M74r1XNzfyNHZl0%2FI0lNxb8Q5vqi9p7E7OYK6wbpHRdXD0ixdkElKOnl6pcO48BfdmTc2fzN1kF1S4D0tcE8pp2WSu%2B6n0dUxpBdYn%2ByvIT9vPpAt6Q5HDrzzixuxtDzsDtXLc4li%2FMLXr87wGOqUBdTn1Zz8iQGnkTP0P%2BOnBs%2FOulbDU28SROE%2FiLlOX6RpfLNt0V7OI%2Bg2y%2FLO8J6TcJ8mcfGkgUbRKbh93DOnbbOii3sUsWfNXTMTeMr5awEd3opP7EwS3jB%2BxauNKZm1N9pezKDBA3MOPqOWTpYabZ9BVKtmkAAcwio1eI0yhsEu179rorlbfCEP3FlKX4DKFWElA7ZEEUNAusPjWOmlXhwJJ3W09&X-Amz-Signature=4f994b14680103caf61178bb599711d9342ed8a2e2c840061d9a32bd84b0d609&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGR332ZM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCErBy8HWD55kBTdKXNvHxyH%2F3uwPAkzrTgBA6sX4khQgIga2Pf7llPYZ6FBBbGHO6wfWvGo69C1fw8FP5GWnl9m9YqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqVTYKkI0%2BlyawKzircAzxvspiso1%2FxiU95KR%2FYqq%2BLO9qD%2F3YSiG2sMolkDY0aHDZPbShlSQATJitzMeB3NVo86od4vv%2FVnz%2F7ngZ7F9Bu9NwSkPhsRJG6TysO4so%2BOrswbjpKEenRQhGbmxCXl5rHkwqwDr2IQAH7GDq0ZpCe8vm%2BZ%2BBDjRQzess4Kruw2KctYpegKYnF4slE92BzYV8Di0VzPf03HLFejGOIyvQRCorLX8GnR49s1jBR%2BlN0TF6N%2FJ9yV3o04%2Ft2xpC%2BPiUEuQjbogSVPfa1KV3aGRTAy%2B6IRrvXOjIDIBKemfH%2FQa9Kp9vO7RJbAG2Zmr2tgaJBfkaa5AXDUh0V47jNbswGwmccMB5iUisSEhFxNrgvjw6HsZ3REc5dDbKpK7OUuxLF9E5T6x2sZ2zuMo4mSXKoCrrVgREyWNf0AnWGbeNs4rn0XvtOLrev%2BDWBOOiDnFa7gnOUDR8JKwW0k%2FQf2cLH1i9apMM7GRuqe%2F7zOrLERWprQ1M74r1XNzfyNHZl0%2FI0lNxb8Q5vqi9p7E7OYK6wbpHRdXD0ixdkElKOnl6pcO48BfdmTc2fzN1kF1S4D0tcE8pp2WSu%2B6n0dUxpBdYn%2ByvIT9vPpAt6Q5HDrzzixuxtDzsDtXLc4li%2FMLXr87wGOqUBdTn1Zz8iQGnkTP0P%2BOnBs%2FOulbDU28SROE%2FiLlOX6RpfLNt0V7OI%2Bg2y%2FLO8J6TcJ8mcfGkgUbRKbh93DOnbbOii3sUsWfNXTMTeMr5awEd3opP7EwS3jB%2BxauNKZm1N9pezKDBA3MOPqOWTpYabZ9BVKtmkAAcwio1eI0yhsEu179rorlbfCEP3FlKX4DKFWElA7ZEEUNAusPjWOmlXhwJJ3W09&X-Amz-Signature=e3a2bcbf379564d3ccf0d06c2c0db1464907d09bbafa4cc2c587a838f0b086a0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGR332ZM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCErBy8HWD55kBTdKXNvHxyH%2F3uwPAkzrTgBA6sX4khQgIga2Pf7llPYZ6FBBbGHO6wfWvGo69C1fw8FP5GWnl9m9YqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqVTYKkI0%2BlyawKzircAzxvspiso1%2FxiU95KR%2FYqq%2BLO9qD%2F3YSiG2sMolkDY0aHDZPbShlSQATJitzMeB3NVo86od4vv%2FVnz%2F7ngZ7F9Bu9NwSkPhsRJG6TysO4so%2BOrswbjpKEenRQhGbmxCXl5rHkwqwDr2IQAH7GDq0ZpCe8vm%2BZ%2BBDjRQzess4Kruw2KctYpegKYnF4slE92BzYV8Di0VzPf03HLFejGOIyvQRCorLX8GnR49s1jBR%2BlN0TF6N%2FJ9yV3o04%2Ft2xpC%2BPiUEuQjbogSVPfa1KV3aGRTAy%2B6IRrvXOjIDIBKemfH%2FQa9Kp9vO7RJbAG2Zmr2tgaJBfkaa5AXDUh0V47jNbswGwmccMB5iUisSEhFxNrgvjw6HsZ3REc5dDbKpK7OUuxLF9E5T6x2sZ2zuMo4mSXKoCrrVgREyWNf0AnWGbeNs4rn0XvtOLrev%2BDWBOOiDnFa7gnOUDR8JKwW0k%2FQf2cLH1i9apMM7GRuqe%2F7zOrLERWprQ1M74r1XNzfyNHZl0%2FI0lNxb8Q5vqi9p7E7OYK6wbpHRdXD0ixdkElKOnl6pcO48BfdmTc2fzN1kF1S4D0tcE8pp2WSu%2B6n0dUxpBdYn%2ByvIT9vPpAt6Q5HDrzzixuxtDzsDtXLc4li%2FMLXr87wGOqUBdTn1Zz8iQGnkTP0P%2BOnBs%2FOulbDU28SROE%2FiLlOX6RpfLNt0V7OI%2Bg2y%2FLO8J6TcJ8mcfGkgUbRKbh93DOnbbOii3sUsWfNXTMTeMr5awEd3opP7EwS3jB%2BxauNKZm1N9pezKDBA3MOPqOWTpYabZ9BVKtmkAAcwio1eI0yhsEu179rorlbfCEP3FlKX4DKFWElA7ZEEUNAusPjWOmlXhwJJ3W09&X-Amz-Signature=f90ae68bdb8fcf37ab7c2fa5936fdd24a41274d21e383e519d05b311bfec5015&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGR332ZM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCErBy8HWD55kBTdKXNvHxyH%2F3uwPAkzrTgBA6sX4khQgIga2Pf7llPYZ6FBBbGHO6wfWvGo69C1fw8FP5GWnl9m9YqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqVTYKkI0%2BlyawKzircAzxvspiso1%2FxiU95KR%2FYqq%2BLO9qD%2F3YSiG2sMolkDY0aHDZPbShlSQATJitzMeB3NVo86od4vv%2FVnz%2F7ngZ7F9Bu9NwSkPhsRJG6TysO4so%2BOrswbjpKEenRQhGbmxCXl5rHkwqwDr2IQAH7GDq0ZpCe8vm%2BZ%2BBDjRQzess4Kruw2KctYpegKYnF4slE92BzYV8Di0VzPf03HLFejGOIyvQRCorLX8GnR49s1jBR%2BlN0TF6N%2FJ9yV3o04%2Ft2xpC%2BPiUEuQjbogSVPfa1KV3aGRTAy%2B6IRrvXOjIDIBKemfH%2FQa9Kp9vO7RJbAG2Zmr2tgaJBfkaa5AXDUh0V47jNbswGwmccMB5iUisSEhFxNrgvjw6HsZ3REc5dDbKpK7OUuxLF9E5T6x2sZ2zuMo4mSXKoCrrVgREyWNf0AnWGbeNs4rn0XvtOLrev%2BDWBOOiDnFa7gnOUDR8JKwW0k%2FQf2cLH1i9apMM7GRuqe%2F7zOrLERWprQ1M74r1XNzfyNHZl0%2FI0lNxb8Q5vqi9p7E7OYK6wbpHRdXD0ixdkElKOnl6pcO48BfdmTc2fzN1kF1S4D0tcE8pp2WSu%2B6n0dUxpBdYn%2ByvIT9vPpAt6Q5HDrzzixuxtDzsDtXLc4li%2FMLXr87wGOqUBdTn1Zz8iQGnkTP0P%2BOnBs%2FOulbDU28SROE%2FiLlOX6RpfLNt0V7OI%2Bg2y%2FLO8J6TcJ8mcfGkgUbRKbh93DOnbbOii3sUsWfNXTMTeMr5awEd3opP7EwS3jB%2BxauNKZm1N9pezKDBA3MOPqOWTpYabZ9BVKtmkAAcwio1eI0yhsEu179rorlbfCEP3FlKX4DKFWElA7ZEEUNAusPjWOmlXhwJJ3W09&X-Amz-Signature=4cf003babd5b95e7c23282a073696b199bf3820872657ce17db2fb009d3bf3da&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGR332ZM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCErBy8HWD55kBTdKXNvHxyH%2F3uwPAkzrTgBA6sX4khQgIga2Pf7llPYZ6FBBbGHO6wfWvGo69C1fw8FP5GWnl9m9YqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqVTYKkI0%2BlyawKzircAzxvspiso1%2FxiU95KR%2FYqq%2BLO9qD%2F3YSiG2sMolkDY0aHDZPbShlSQATJitzMeB3NVo86od4vv%2FVnz%2F7ngZ7F9Bu9NwSkPhsRJG6TysO4so%2BOrswbjpKEenRQhGbmxCXl5rHkwqwDr2IQAH7GDq0ZpCe8vm%2BZ%2BBDjRQzess4Kruw2KctYpegKYnF4slE92BzYV8Di0VzPf03HLFejGOIyvQRCorLX8GnR49s1jBR%2BlN0TF6N%2FJ9yV3o04%2Ft2xpC%2BPiUEuQjbogSVPfa1KV3aGRTAy%2B6IRrvXOjIDIBKemfH%2FQa9Kp9vO7RJbAG2Zmr2tgaJBfkaa5AXDUh0V47jNbswGwmccMB5iUisSEhFxNrgvjw6HsZ3REc5dDbKpK7OUuxLF9E5T6x2sZ2zuMo4mSXKoCrrVgREyWNf0AnWGbeNs4rn0XvtOLrev%2BDWBOOiDnFa7gnOUDR8JKwW0k%2FQf2cLH1i9apMM7GRuqe%2F7zOrLERWprQ1M74r1XNzfyNHZl0%2FI0lNxb8Q5vqi9p7E7OYK6wbpHRdXD0ixdkElKOnl6pcO48BfdmTc2fzN1kF1S4D0tcE8pp2WSu%2B6n0dUxpBdYn%2ByvIT9vPpAt6Q5HDrzzixuxtDzsDtXLc4li%2FMLXr87wGOqUBdTn1Zz8iQGnkTP0P%2BOnBs%2FOulbDU28SROE%2FiLlOX6RpfLNt0V7OI%2Bg2y%2FLO8J6TcJ8mcfGkgUbRKbh93DOnbbOii3sUsWfNXTMTeMr5awEd3opP7EwS3jB%2BxauNKZm1N9pezKDBA3MOPqOWTpYabZ9BVKtmkAAcwio1eI0yhsEu179rorlbfCEP3FlKX4DKFWElA7ZEEUNAusPjWOmlXhwJJ3W09&X-Amz-Signature=5c5f974f536f64c033dd27c18c5b8145e540100458bfcc355d78dd26e0003a5c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CKFGZJN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHXfqNgWA0Fyf7NXTEMnGziHcEtYi2%2FFmN%2BeW4oQRhhfAiAL25QP1AHxZuFxfuVsA1n%2BxkuYi0SX9MugjihDbst8miqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8to5IWR1SnXn5oA%2BKtwDmt%2FJIZyTuDZNFqHhSrfOS7sUW89YCIdQWxsghHo5tHEmoj4osDaC63pwXD4UDMTUXy0PklAm%2BcpdTR8w9PTDOMs%2FnnQQy5j2M2TJKYjZq5dQje5pgPgAsx7at8HUImV%2Bgoc6nkohDMFOF0DlOnv6DzNKey%2FUy%2BbeIt73xzd3IoBpFZr0q2X55yYvIZr3MozK%2BAVdx6Wxc5DlBhJrY5SoHx0NmA9ORaTFNklIWnIQJnirqknJNZKhwTKgXdrEXYuB3FNTV7w8uur%2FaJNzffbHs03qi1mDl19mtsblGLha1u2Y0Bc75R7B9tKc%2B8B7wX%2BYKP2OSiJz3xzTonGLU74QLdyyR6txshCS8qtCqnxDQqX%2FYyza8gYSkH8A5Gzf4yt9SgxFRVb5i2KKbEkB%2BnXCh2UWtckcTK%2FO%2BeGcUxytXlXifWIQNxsBNxPqXjOL8QdSvg%2FoFmYbWYgAHH2sQiHD55%2B46TI7Wul1EAGox4EuTdq1PpgXCPyrfUBW%2BNowfEg%2FvtHCLSnkWR93OuS7O675ivTOEltMWY5VJ18cl49IX2TuIFenbJ7f9RTUuj7ynN9CTlK7%2Bv9YrPIB1UnRzMgz92tsGk8dSzhRXfCuDVSi6s5FCIMXQ5aXbwpBKqEwl%2BvzvAY6pgEXXYN4tEDfKtcFObqm78VMJRk96H4M3pjEVqsp4BVNs2bwVEdvSREIey3CQ8Z%2FWvo3GQC%2B1o5i5VxrqgMdlb0%2Be%2Bvilsc5Rf6qDpslFIhPl%2Fn1b9rHnqIOT3bvjeMiFnHp8RLGZuO%2B4UScPfx6IIkjTT%2BnLu4e187vUXnN4dBF%2FcpY09FLg9MwGKYpK%2BaEJbaxdmnPbIY6oRMI9WeNLT%2B50iL1dXau&X-Amz-Signature=1d2ec684bec53d0d2af4fe455fb64d3f0b6774da8bcfde2acabf0cbb32b3e8a3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CKFGZJN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHXfqNgWA0Fyf7NXTEMnGziHcEtYi2%2FFmN%2BeW4oQRhhfAiAL25QP1AHxZuFxfuVsA1n%2BxkuYi0SX9MugjihDbst8miqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8to5IWR1SnXn5oA%2BKtwDmt%2FJIZyTuDZNFqHhSrfOS7sUW89YCIdQWxsghHo5tHEmoj4osDaC63pwXD4UDMTUXy0PklAm%2BcpdTR8w9PTDOMs%2FnnQQy5j2M2TJKYjZq5dQje5pgPgAsx7at8HUImV%2Bgoc6nkohDMFOF0DlOnv6DzNKey%2FUy%2BbeIt73xzd3IoBpFZr0q2X55yYvIZr3MozK%2BAVdx6Wxc5DlBhJrY5SoHx0NmA9ORaTFNklIWnIQJnirqknJNZKhwTKgXdrEXYuB3FNTV7w8uur%2FaJNzffbHs03qi1mDl19mtsblGLha1u2Y0Bc75R7B9tKc%2B8B7wX%2BYKP2OSiJz3xzTonGLU74QLdyyR6txshCS8qtCqnxDQqX%2FYyza8gYSkH8A5Gzf4yt9SgxFRVb5i2KKbEkB%2BnXCh2UWtckcTK%2FO%2BeGcUxytXlXifWIQNxsBNxPqXjOL8QdSvg%2FoFmYbWYgAHH2sQiHD55%2B46TI7Wul1EAGox4EuTdq1PpgXCPyrfUBW%2BNowfEg%2FvtHCLSnkWR93OuS7O675ivTOEltMWY5VJ18cl49IX2TuIFenbJ7f9RTUuj7ynN9CTlK7%2Bv9YrPIB1UnRzMgz92tsGk8dSzhRXfCuDVSi6s5FCIMXQ5aXbwpBKqEwl%2BvzvAY6pgEXXYN4tEDfKtcFObqm78VMJRk96H4M3pjEVqsp4BVNs2bwVEdvSREIey3CQ8Z%2FWvo3GQC%2B1o5i5VxrqgMdlb0%2Be%2Bvilsc5Rf6qDpslFIhPl%2Fn1b9rHnqIOT3bvjeMiFnHp8RLGZuO%2B4UScPfx6IIkjTT%2BnLu4e187vUXnN4dBF%2FcpY09FLg9MwGKYpK%2BaEJbaxdmnPbIY6oRMI9WeNLT%2B50iL1dXau&X-Amz-Signature=9fffd741a78c56c2bc7690d90024eaa280ce7acda23d57a95f7536dd51a01898&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CKFGZJN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHXfqNgWA0Fyf7NXTEMnGziHcEtYi2%2FFmN%2BeW4oQRhhfAiAL25QP1AHxZuFxfuVsA1n%2BxkuYi0SX9MugjihDbst8miqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8to5IWR1SnXn5oA%2BKtwDmt%2FJIZyTuDZNFqHhSrfOS7sUW89YCIdQWxsghHo5tHEmoj4osDaC63pwXD4UDMTUXy0PklAm%2BcpdTR8w9PTDOMs%2FnnQQy5j2M2TJKYjZq5dQje5pgPgAsx7at8HUImV%2Bgoc6nkohDMFOF0DlOnv6DzNKey%2FUy%2BbeIt73xzd3IoBpFZr0q2X55yYvIZr3MozK%2BAVdx6Wxc5DlBhJrY5SoHx0NmA9ORaTFNklIWnIQJnirqknJNZKhwTKgXdrEXYuB3FNTV7w8uur%2FaJNzffbHs03qi1mDl19mtsblGLha1u2Y0Bc75R7B9tKc%2B8B7wX%2BYKP2OSiJz3xzTonGLU74QLdyyR6txshCS8qtCqnxDQqX%2FYyza8gYSkH8A5Gzf4yt9SgxFRVb5i2KKbEkB%2BnXCh2UWtckcTK%2FO%2BeGcUxytXlXifWIQNxsBNxPqXjOL8QdSvg%2FoFmYbWYgAHH2sQiHD55%2B46TI7Wul1EAGox4EuTdq1PpgXCPyrfUBW%2BNowfEg%2FvtHCLSnkWR93OuS7O675ivTOEltMWY5VJ18cl49IX2TuIFenbJ7f9RTUuj7ynN9CTlK7%2Bv9YrPIB1UnRzMgz92tsGk8dSzhRXfCuDVSi6s5FCIMXQ5aXbwpBKqEwl%2BvzvAY6pgEXXYN4tEDfKtcFObqm78VMJRk96H4M3pjEVqsp4BVNs2bwVEdvSREIey3CQ8Z%2FWvo3GQC%2B1o5i5VxrqgMdlb0%2Be%2Bvilsc5Rf6qDpslFIhPl%2Fn1b9rHnqIOT3bvjeMiFnHp8RLGZuO%2B4UScPfx6IIkjTT%2BnLu4e187vUXnN4dBF%2FcpY09FLg9MwGKYpK%2BaEJbaxdmnPbIY6oRMI9WeNLT%2B50iL1dXau&X-Amz-Signature=03b2b05c970a58caaaeb6379c3fbc5909bf58eb01e08b13fb46e84a3925f8b51&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CKFGZJN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHXfqNgWA0Fyf7NXTEMnGziHcEtYi2%2FFmN%2BeW4oQRhhfAiAL25QP1AHxZuFxfuVsA1n%2BxkuYi0SX9MugjihDbst8miqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8to5IWR1SnXn5oA%2BKtwDmt%2FJIZyTuDZNFqHhSrfOS7sUW89YCIdQWxsghHo5tHEmoj4osDaC63pwXD4UDMTUXy0PklAm%2BcpdTR8w9PTDOMs%2FnnQQy5j2M2TJKYjZq5dQje5pgPgAsx7at8HUImV%2Bgoc6nkohDMFOF0DlOnv6DzNKey%2FUy%2BbeIt73xzd3IoBpFZr0q2X55yYvIZr3MozK%2BAVdx6Wxc5DlBhJrY5SoHx0NmA9ORaTFNklIWnIQJnirqknJNZKhwTKgXdrEXYuB3FNTV7w8uur%2FaJNzffbHs03qi1mDl19mtsblGLha1u2Y0Bc75R7B9tKc%2B8B7wX%2BYKP2OSiJz3xzTonGLU74QLdyyR6txshCS8qtCqnxDQqX%2FYyza8gYSkH8A5Gzf4yt9SgxFRVb5i2KKbEkB%2BnXCh2UWtckcTK%2FO%2BeGcUxytXlXifWIQNxsBNxPqXjOL8QdSvg%2FoFmYbWYgAHH2sQiHD55%2B46TI7Wul1EAGox4EuTdq1PpgXCPyrfUBW%2BNowfEg%2FvtHCLSnkWR93OuS7O675ivTOEltMWY5VJ18cl49IX2TuIFenbJ7f9RTUuj7ynN9CTlK7%2Bv9YrPIB1UnRzMgz92tsGk8dSzhRXfCuDVSi6s5FCIMXQ5aXbwpBKqEwl%2BvzvAY6pgEXXYN4tEDfKtcFObqm78VMJRk96H4M3pjEVqsp4BVNs2bwVEdvSREIey3CQ8Z%2FWvo3GQC%2B1o5i5VxrqgMdlb0%2Be%2Bvilsc5Rf6qDpslFIhPl%2Fn1b9rHnqIOT3bvjeMiFnHp8RLGZuO%2B4UScPfx6IIkjTT%2BnLu4e187vUXnN4dBF%2FcpY09FLg9MwGKYpK%2BaEJbaxdmnPbIY6oRMI9WeNLT%2B50iL1dXau&X-Amz-Signature=795eb9f09b4e2444eb4cb82e174ede8ef7e4f4baaf93e9f063c021958fc4b154&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CKFGZJN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHXfqNgWA0Fyf7NXTEMnGziHcEtYi2%2FFmN%2BeW4oQRhhfAiAL25QP1AHxZuFxfuVsA1n%2BxkuYi0SX9MugjihDbst8miqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8to5IWR1SnXn5oA%2BKtwDmt%2FJIZyTuDZNFqHhSrfOS7sUW89YCIdQWxsghHo5tHEmoj4osDaC63pwXD4UDMTUXy0PklAm%2BcpdTR8w9PTDOMs%2FnnQQy5j2M2TJKYjZq5dQje5pgPgAsx7at8HUImV%2Bgoc6nkohDMFOF0DlOnv6DzNKey%2FUy%2BbeIt73xzd3IoBpFZr0q2X55yYvIZr3MozK%2BAVdx6Wxc5DlBhJrY5SoHx0NmA9ORaTFNklIWnIQJnirqknJNZKhwTKgXdrEXYuB3FNTV7w8uur%2FaJNzffbHs03qi1mDl19mtsblGLha1u2Y0Bc75R7B9tKc%2B8B7wX%2BYKP2OSiJz3xzTonGLU74QLdyyR6txshCS8qtCqnxDQqX%2FYyza8gYSkH8A5Gzf4yt9SgxFRVb5i2KKbEkB%2BnXCh2UWtckcTK%2FO%2BeGcUxytXlXifWIQNxsBNxPqXjOL8QdSvg%2FoFmYbWYgAHH2sQiHD55%2B46TI7Wul1EAGox4EuTdq1PpgXCPyrfUBW%2BNowfEg%2FvtHCLSnkWR93OuS7O675ivTOEltMWY5VJ18cl49IX2TuIFenbJ7f9RTUuj7ynN9CTlK7%2Bv9YrPIB1UnRzMgz92tsGk8dSzhRXfCuDVSi6s5FCIMXQ5aXbwpBKqEwl%2BvzvAY6pgEXXYN4tEDfKtcFObqm78VMJRk96H4M3pjEVqsp4BVNs2bwVEdvSREIey3CQ8Z%2FWvo3GQC%2B1o5i5VxrqgMdlb0%2Be%2Bvilsc5Rf6qDpslFIhPl%2Fn1b9rHnqIOT3bvjeMiFnHp8RLGZuO%2B4UScPfx6IIkjTT%2BnLu4e187vUXnN4dBF%2FcpY09FLg9MwGKYpK%2BaEJbaxdmnPbIY6oRMI9WeNLT%2B50iL1dXau&X-Amz-Signature=75575ca1cb685b418f4471cc58fee0ef0adafb36f9a03c6226cbe7710d474e42&X-Amz-SignedHeaders=host&x-id=GetObject)
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


