

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IIELEJR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIE0AUABF%2FHZ%2Ft8sQMZgz8gIdlaKggGt4sSIkzv2g4eGzAiEApa17LKoQQ5nNRJUQ%2F7wjmOKuHbMvVIxpCfpBe95fUYEq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDMROhJ%2Fmn7wya%2FFAAircA8A%2BWDi2y0D2gtepWgkxfVjBZ%2F8thDhSYngQTCtVpwc0YTcalH6v2TdKxavYOGpCXoIGNGfRQGXMXbzHPzAAPGgZO%2BeRps8BVqRc19SVrUgKQLHmz2Ra9z6oxFEPI0%2F7e3%2FM%2FslzROzhWksKyW1ZrAnXmU9D7nXPIdHS%2BXD5MQWBnjf5qYEAKSLomjzLYcW%2B1p4fQyWNYwWiXPLkf%2FgOegWQNaV3ghmmCcWdBZgyenDb9q9YdPbteRfPypYdI3LNnGaufYyOxTpW0%2Bpztab%2FESKTniFZBgDD88WRedmOoPzqx2XiovzrPx2iC%2Fh0qcIxcgEclnvaFwVRKLOgJqHKo164aFnD5panYcHLQWkCemnux%2B9DRzs9MAfoMoO1bUpNd0FIniEWhHSYPXr1L8TgXHc8w2uCJLHiO%2Be%2FULvD8wr9DrpEd3%2FmZA%2F%2FPN7USwhPaeVcJM1vQxtw8vicPWTOIv1JFfXbgMXCDHQUfsX2dsSmK%2F%2FVwGtubmuxmHG4uTxBh2X1X%2BpaC%2BxWCNaWIv%2BmSufwhLVtSur6gFrk21C%2Fjz4n8oYfo%2FndA2osd1CHMeoSg7Tq3wmJMeZxvTVeoWKRNqtNOSqDhWfVSMUeT4p1gPEfPj6WHh36qf9YYB6ZMPWAjr0GOqUBA5nwaXz8sjATWzE9uYuRB0ZDQBXmM1oBgcj3ttOtrY%2FFndXaDousrTZTGM1j6FS2QWfoV6E4%2BQNmoM9S4tli7mRb38yh9XtH%2BWgyjx9xH4CnUU4yS3eU9VjKUOKVw6LpvNSTVzSOjijoIsaFH9z49dJZQIhBjJKMWbb14r71qMyN7HYMm2oz%2FHR1u79%2FM0yyVgtlLS5KCTKx06Sv7yPye63LQaDt&X-Amz-Signature=e37245b0bcc894c66a00553fe3f3af780e59d983761a28b76e68f653c6406514&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAS3TRUJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIBWyIGHyVzNDhDcKayJ8Ez1AaOudxKSux8IH5nx3%2FzgdAiBQHdgvDmQETq%2FFBaI5zm2JVjXXqtH9UNw4nMCmLfQlhyr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMJ%2Bf5GpnlhZ7FvctjKtwDOrvbg8ZU6psvgQDG0ps9K0wrOipgCtGyVuN4eQ5%2BINyrs5gLHfVGu2GWcgX5SXUd%2FHAB8civQLtPd4EnbOZvlwa%2BFb9E5y2sj4fAwDsfU%2BXjsyl9DFtcm1oIIhDmenDezeVWBMo1sS1oF7mX9NlKOPJNvkkBdFbAQ3cbcT9gjhOoioNAEMcDbn7ha4aMCov5pu4Ueff0TSuP9WkCzLiY7IidPBMABbR32Afi%2B4Z7iKf1%2FJSFx%2Bet5QFPBYfrwPw%2FW2qolFKdyXjDPWb2GEV0eZeczEast5vJ7Q%2Fr0PZx%2BA%2FOLaKIgmS5%2FJEF%2FozF909gqxgs7Q8d71QCzgU%2BnxRMmSnK4%2BWOuCY774DoUs7CT32uhk1SRsrFFpuT766byWpF4%2FJS7IsEunWurPm8dDRtJhJmALm%2FbvRM9SQfzNcOv9jE2CCExN9brfJfLsb0mBKa%2FwU34ZqgXu8AM72Kn70j5%2FygBgBaLn%2BQdlOWihnokbT80rcIEU4yS9CjsQvc5WAQNA8uIET%2FRi5YnLpPD5OyIY8oFWTd5bnk%2B%2FmW%2B%2FwkKbbjK5n%2BamSEKV%2FaXGEgnxH%2BKnN%2FCdKncdUZ0n%2BjUlwUHcJ645zIrgxztNWY6Fu5CSFfeKVp7stDdZLpilYwwZ2OvQY6pgHQoRFVuyJICnuadT%2BcDPfPxaBlIsqKQ7J7X%2Fl%2Fpyn5gvcMLQ9KsJ2eoANX%2BUn1FfmMqa0vvH3mHuvoqiDG6NySNtaH6olhyxy51lgDQoyTCNuMnUxcNFfCF%2F0KPGTyGMeE%2Fb2MiUGCG1UTQ1ogbW5hWTUQOmnzzwhvuW6Pt1WG4DArhGCUAA%2F6CzTiqNOfskGQ9NnhqyA1M4w7Hx%2Fq3vNKBr9AVDn%2B&X-Amz-Signature=0bc92311fdf8582f3fe43d4918b8f1cdd077e1d9a2027882d2962b7499d680e8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAS3TRUJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIBWyIGHyVzNDhDcKayJ8Ez1AaOudxKSux8IH5nx3%2FzgdAiBQHdgvDmQETq%2FFBaI5zm2JVjXXqtH9UNw4nMCmLfQlhyr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMJ%2Bf5GpnlhZ7FvctjKtwDOrvbg8ZU6psvgQDG0ps9K0wrOipgCtGyVuN4eQ5%2BINyrs5gLHfVGu2GWcgX5SXUd%2FHAB8civQLtPd4EnbOZvlwa%2BFb9E5y2sj4fAwDsfU%2BXjsyl9DFtcm1oIIhDmenDezeVWBMo1sS1oF7mX9NlKOPJNvkkBdFbAQ3cbcT9gjhOoioNAEMcDbn7ha4aMCov5pu4Ueff0TSuP9WkCzLiY7IidPBMABbR32Afi%2B4Z7iKf1%2FJSFx%2Bet5QFPBYfrwPw%2FW2qolFKdyXjDPWb2GEV0eZeczEast5vJ7Q%2Fr0PZx%2BA%2FOLaKIgmS5%2FJEF%2FozF909gqxgs7Q8d71QCzgU%2BnxRMmSnK4%2BWOuCY774DoUs7CT32uhk1SRsrFFpuT766byWpF4%2FJS7IsEunWurPm8dDRtJhJmALm%2FbvRM9SQfzNcOv9jE2CCExN9brfJfLsb0mBKa%2FwU34ZqgXu8AM72Kn70j5%2FygBgBaLn%2BQdlOWihnokbT80rcIEU4yS9CjsQvc5WAQNA8uIET%2FRi5YnLpPD5OyIY8oFWTd5bnk%2B%2FmW%2B%2FwkKbbjK5n%2BamSEKV%2FaXGEgnxH%2BKnN%2FCdKncdUZ0n%2BjUlwUHcJ645zIrgxztNWY6Fu5CSFfeKVp7stDdZLpilYwwZ2OvQY6pgHQoRFVuyJICnuadT%2BcDPfPxaBlIsqKQ7J7X%2Fl%2Fpyn5gvcMLQ9KsJ2eoANX%2BUn1FfmMqa0vvH3mHuvoqiDG6NySNtaH6olhyxy51lgDQoyTCNuMnUxcNFfCF%2F0KPGTyGMeE%2Fb2MiUGCG1UTQ1ogbW5hWTUQOmnzzwhvuW6Pt1WG4DArhGCUAA%2F6CzTiqNOfskGQ9NnhqyA1M4w7Hx%2Fq3vNKBr9AVDn%2B&X-Amz-Signature=225f9c2eb3bd7ce5e3f4baa28aa6b2f7e8d775d8d200f3708bf55a9cb1a3b2c1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAS3TRUJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIBWyIGHyVzNDhDcKayJ8Ez1AaOudxKSux8IH5nx3%2FzgdAiBQHdgvDmQETq%2FFBaI5zm2JVjXXqtH9UNw4nMCmLfQlhyr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMJ%2Bf5GpnlhZ7FvctjKtwDOrvbg8ZU6psvgQDG0ps9K0wrOipgCtGyVuN4eQ5%2BINyrs5gLHfVGu2GWcgX5SXUd%2FHAB8civQLtPd4EnbOZvlwa%2BFb9E5y2sj4fAwDsfU%2BXjsyl9DFtcm1oIIhDmenDezeVWBMo1sS1oF7mX9NlKOPJNvkkBdFbAQ3cbcT9gjhOoioNAEMcDbn7ha4aMCov5pu4Ueff0TSuP9WkCzLiY7IidPBMABbR32Afi%2B4Z7iKf1%2FJSFx%2Bet5QFPBYfrwPw%2FW2qolFKdyXjDPWb2GEV0eZeczEast5vJ7Q%2Fr0PZx%2BA%2FOLaKIgmS5%2FJEF%2FozF909gqxgs7Q8d71QCzgU%2BnxRMmSnK4%2BWOuCY774DoUs7CT32uhk1SRsrFFpuT766byWpF4%2FJS7IsEunWurPm8dDRtJhJmALm%2FbvRM9SQfzNcOv9jE2CCExN9brfJfLsb0mBKa%2FwU34ZqgXu8AM72Kn70j5%2FygBgBaLn%2BQdlOWihnokbT80rcIEU4yS9CjsQvc5WAQNA8uIET%2FRi5YnLpPD5OyIY8oFWTd5bnk%2B%2FmW%2B%2FwkKbbjK5n%2BamSEKV%2FaXGEgnxH%2BKnN%2FCdKncdUZ0n%2BjUlwUHcJ645zIrgxztNWY6Fu5CSFfeKVp7stDdZLpilYwwZ2OvQY6pgHQoRFVuyJICnuadT%2BcDPfPxaBlIsqKQ7J7X%2Fl%2Fpyn5gvcMLQ9KsJ2eoANX%2BUn1FfmMqa0vvH3mHuvoqiDG6NySNtaH6olhyxy51lgDQoyTCNuMnUxcNFfCF%2F0KPGTyGMeE%2Fb2MiUGCG1UTQ1ogbW5hWTUQOmnzzwhvuW6Pt1WG4DArhGCUAA%2F6CzTiqNOfskGQ9NnhqyA1M4w7Hx%2Fq3vNKBr9AVDn%2B&X-Amz-Signature=d967a091c91c55414709cc5a2985009b688d76b2068e5aa161ad4663d1091f06&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAS3TRUJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIBWyIGHyVzNDhDcKayJ8Ez1AaOudxKSux8IH5nx3%2FzgdAiBQHdgvDmQETq%2FFBaI5zm2JVjXXqtH9UNw4nMCmLfQlhyr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMJ%2Bf5GpnlhZ7FvctjKtwDOrvbg8ZU6psvgQDG0ps9K0wrOipgCtGyVuN4eQ5%2BINyrs5gLHfVGu2GWcgX5SXUd%2FHAB8civQLtPd4EnbOZvlwa%2BFb9E5y2sj4fAwDsfU%2BXjsyl9DFtcm1oIIhDmenDezeVWBMo1sS1oF7mX9NlKOPJNvkkBdFbAQ3cbcT9gjhOoioNAEMcDbn7ha4aMCov5pu4Ueff0TSuP9WkCzLiY7IidPBMABbR32Afi%2B4Z7iKf1%2FJSFx%2Bet5QFPBYfrwPw%2FW2qolFKdyXjDPWb2GEV0eZeczEast5vJ7Q%2Fr0PZx%2BA%2FOLaKIgmS5%2FJEF%2FozF909gqxgs7Q8d71QCzgU%2BnxRMmSnK4%2BWOuCY774DoUs7CT32uhk1SRsrFFpuT766byWpF4%2FJS7IsEunWurPm8dDRtJhJmALm%2FbvRM9SQfzNcOv9jE2CCExN9brfJfLsb0mBKa%2FwU34ZqgXu8AM72Kn70j5%2FygBgBaLn%2BQdlOWihnokbT80rcIEU4yS9CjsQvc5WAQNA8uIET%2FRi5YnLpPD5OyIY8oFWTd5bnk%2B%2FmW%2B%2FwkKbbjK5n%2BamSEKV%2FaXGEgnxH%2BKnN%2FCdKncdUZ0n%2BjUlwUHcJ645zIrgxztNWY6Fu5CSFfeKVp7stDdZLpilYwwZ2OvQY6pgHQoRFVuyJICnuadT%2BcDPfPxaBlIsqKQ7J7X%2Fl%2Fpyn5gvcMLQ9KsJ2eoANX%2BUn1FfmMqa0vvH3mHuvoqiDG6NySNtaH6olhyxy51lgDQoyTCNuMnUxcNFfCF%2F0KPGTyGMeE%2Fb2MiUGCG1UTQ1ogbW5hWTUQOmnzzwhvuW6Pt1WG4DArhGCUAA%2F6CzTiqNOfskGQ9NnhqyA1M4w7Hx%2Fq3vNKBr9AVDn%2B&X-Amz-Signature=b7f279e65180b8cb3915ab5449648f631964a15238295acaa2c883a95cc5ef78&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAS3TRUJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIBWyIGHyVzNDhDcKayJ8Ez1AaOudxKSux8IH5nx3%2FzgdAiBQHdgvDmQETq%2FFBaI5zm2JVjXXqtH9UNw4nMCmLfQlhyr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMJ%2Bf5GpnlhZ7FvctjKtwDOrvbg8ZU6psvgQDG0ps9K0wrOipgCtGyVuN4eQ5%2BINyrs5gLHfVGu2GWcgX5SXUd%2FHAB8civQLtPd4EnbOZvlwa%2BFb9E5y2sj4fAwDsfU%2BXjsyl9DFtcm1oIIhDmenDezeVWBMo1sS1oF7mX9NlKOPJNvkkBdFbAQ3cbcT9gjhOoioNAEMcDbn7ha4aMCov5pu4Ueff0TSuP9WkCzLiY7IidPBMABbR32Afi%2B4Z7iKf1%2FJSFx%2Bet5QFPBYfrwPw%2FW2qolFKdyXjDPWb2GEV0eZeczEast5vJ7Q%2Fr0PZx%2BA%2FOLaKIgmS5%2FJEF%2FozF909gqxgs7Q8d71QCzgU%2BnxRMmSnK4%2BWOuCY774DoUs7CT32uhk1SRsrFFpuT766byWpF4%2FJS7IsEunWurPm8dDRtJhJmALm%2FbvRM9SQfzNcOv9jE2CCExN9brfJfLsb0mBKa%2FwU34ZqgXu8AM72Kn70j5%2FygBgBaLn%2BQdlOWihnokbT80rcIEU4yS9CjsQvc5WAQNA8uIET%2FRi5YnLpPD5OyIY8oFWTd5bnk%2B%2FmW%2B%2FwkKbbjK5n%2BamSEKV%2FaXGEgnxH%2BKnN%2FCdKncdUZ0n%2BjUlwUHcJ645zIrgxztNWY6Fu5CSFfeKVp7stDdZLpilYwwZ2OvQY6pgHQoRFVuyJICnuadT%2BcDPfPxaBlIsqKQ7J7X%2Fl%2Fpyn5gvcMLQ9KsJ2eoANX%2BUn1FfmMqa0vvH3mHuvoqiDG6NySNtaH6olhyxy51lgDQoyTCNuMnUxcNFfCF%2F0KPGTyGMeE%2Fb2MiUGCG1UTQ1ogbW5hWTUQOmnzzwhvuW6Pt1WG4DArhGCUAA%2F6CzTiqNOfskGQ9NnhqyA1M4w7Hx%2Fq3vNKBr9AVDn%2B&X-Amz-Signature=c2d104a7aadcabe4b28050ddac933b612cf3fe6ebd9d7324d9561064904dfdc3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IIELEJR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIE0AUABF%2FHZ%2Ft8sQMZgz8gIdlaKggGt4sSIkzv2g4eGzAiEApa17LKoQQ5nNRJUQ%2F7wjmOKuHbMvVIxpCfpBe95fUYEq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDMROhJ%2Fmn7wya%2FFAAircA8A%2BWDi2y0D2gtepWgkxfVjBZ%2F8thDhSYngQTCtVpwc0YTcalH6v2TdKxavYOGpCXoIGNGfRQGXMXbzHPzAAPGgZO%2BeRps8BVqRc19SVrUgKQLHmz2Ra9z6oxFEPI0%2F7e3%2FM%2FslzROzhWksKyW1ZrAnXmU9D7nXPIdHS%2BXD5MQWBnjf5qYEAKSLomjzLYcW%2B1p4fQyWNYwWiXPLkf%2FgOegWQNaV3ghmmCcWdBZgyenDb9q9YdPbteRfPypYdI3LNnGaufYyOxTpW0%2Bpztab%2FESKTniFZBgDD88WRedmOoPzqx2XiovzrPx2iC%2Fh0qcIxcgEclnvaFwVRKLOgJqHKo164aFnD5panYcHLQWkCemnux%2B9DRzs9MAfoMoO1bUpNd0FIniEWhHSYPXr1L8TgXHc8w2uCJLHiO%2Be%2FULvD8wr9DrpEd3%2FmZA%2F%2FPN7USwhPaeVcJM1vQxtw8vicPWTOIv1JFfXbgMXCDHQUfsX2dsSmK%2F%2FVwGtubmuxmHG4uTxBh2X1X%2BpaC%2BxWCNaWIv%2BmSufwhLVtSur6gFrk21C%2Fjz4n8oYfo%2FndA2osd1CHMeoSg7Tq3wmJMeZxvTVeoWKRNqtNOSqDhWfVSMUeT4p1gPEfPj6WHh36qf9YYB6ZMPWAjr0GOqUBA5nwaXz8sjATWzE9uYuRB0ZDQBXmM1oBgcj3ttOtrY%2FFndXaDousrTZTGM1j6FS2QWfoV6E4%2BQNmoM9S4tli7mRb38yh9XtH%2BWgyjx9xH4CnUU4yS3eU9VjKUOKVw6LpvNSTVzSOjijoIsaFH9z49dJZQIhBjJKMWbb14r71qMyN7HYMm2oz%2FHR1u79%2FM0yyVgtlLS5KCTKx06Sv7yPye63LQaDt&X-Amz-Signature=3ee3c75ad8920df28e225eed287464a67aeca59104203fb50fa3195e7fa26517&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IIELEJR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIE0AUABF%2FHZ%2Ft8sQMZgz8gIdlaKggGt4sSIkzv2g4eGzAiEApa17LKoQQ5nNRJUQ%2F7wjmOKuHbMvVIxpCfpBe95fUYEq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDMROhJ%2Fmn7wya%2FFAAircA8A%2BWDi2y0D2gtepWgkxfVjBZ%2F8thDhSYngQTCtVpwc0YTcalH6v2TdKxavYOGpCXoIGNGfRQGXMXbzHPzAAPGgZO%2BeRps8BVqRc19SVrUgKQLHmz2Ra9z6oxFEPI0%2F7e3%2FM%2FslzROzhWksKyW1ZrAnXmU9D7nXPIdHS%2BXD5MQWBnjf5qYEAKSLomjzLYcW%2B1p4fQyWNYwWiXPLkf%2FgOegWQNaV3ghmmCcWdBZgyenDb9q9YdPbteRfPypYdI3LNnGaufYyOxTpW0%2Bpztab%2FESKTniFZBgDD88WRedmOoPzqx2XiovzrPx2iC%2Fh0qcIxcgEclnvaFwVRKLOgJqHKo164aFnD5panYcHLQWkCemnux%2B9DRzs9MAfoMoO1bUpNd0FIniEWhHSYPXr1L8TgXHc8w2uCJLHiO%2Be%2FULvD8wr9DrpEd3%2FmZA%2F%2FPN7USwhPaeVcJM1vQxtw8vicPWTOIv1JFfXbgMXCDHQUfsX2dsSmK%2F%2FVwGtubmuxmHG4uTxBh2X1X%2BpaC%2BxWCNaWIv%2BmSufwhLVtSur6gFrk21C%2Fjz4n8oYfo%2FndA2osd1CHMeoSg7Tq3wmJMeZxvTVeoWKRNqtNOSqDhWfVSMUeT4p1gPEfPj6WHh36qf9YYB6ZMPWAjr0GOqUBA5nwaXz8sjATWzE9uYuRB0ZDQBXmM1oBgcj3ttOtrY%2FFndXaDousrTZTGM1j6FS2QWfoV6E4%2BQNmoM9S4tli7mRb38yh9XtH%2BWgyjx9xH4CnUU4yS3eU9VjKUOKVw6LpvNSTVzSOjijoIsaFH9z49dJZQIhBjJKMWbb14r71qMyN7HYMm2oz%2FHR1u79%2FM0yyVgtlLS5KCTKx06Sv7yPye63LQaDt&X-Amz-Signature=434589b7d4a62595c0d09408ead37e03a20d4d8eb8917ea51f6fb3c1eefc81aa&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IIELEJR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIE0AUABF%2FHZ%2Ft8sQMZgz8gIdlaKggGt4sSIkzv2g4eGzAiEApa17LKoQQ5nNRJUQ%2F7wjmOKuHbMvVIxpCfpBe95fUYEq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDMROhJ%2Fmn7wya%2FFAAircA8A%2BWDi2y0D2gtepWgkxfVjBZ%2F8thDhSYngQTCtVpwc0YTcalH6v2TdKxavYOGpCXoIGNGfRQGXMXbzHPzAAPGgZO%2BeRps8BVqRc19SVrUgKQLHmz2Ra9z6oxFEPI0%2F7e3%2FM%2FslzROzhWksKyW1ZrAnXmU9D7nXPIdHS%2BXD5MQWBnjf5qYEAKSLomjzLYcW%2B1p4fQyWNYwWiXPLkf%2FgOegWQNaV3ghmmCcWdBZgyenDb9q9YdPbteRfPypYdI3LNnGaufYyOxTpW0%2Bpztab%2FESKTniFZBgDD88WRedmOoPzqx2XiovzrPx2iC%2Fh0qcIxcgEclnvaFwVRKLOgJqHKo164aFnD5panYcHLQWkCemnux%2B9DRzs9MAfoMoO1bUpNd0FIniEWhHSYPXr1L8TgXHc8w2uCJLHiO%2Be%2FULvD8wr9DrpEd3%2FmZA%2F%2FPN7USwhPaeVcJM1vQxtw8vicPWTOIv1JFfXbgMXCDHQUfsX2dsSmK%2F%2FVwGtubmuxmHG4uTxBh2X1X%2BpaC%2BxWCNaWIv%2BmSufwhLVtSur6gFrk21C%2Fjz4n8oYfo%2FndA2osd1CHMeoSg7Tq3wmJMeZxvTVeoWKRNqtNOSqDhWfVSMUeT4p1gPEfPj6WHh36qf9YYB6ZMPWAjr0GOqUBA5nwaXz8sjATWzE9uYuRB0ZDQBXmM1oBgcj3ttOtrY%2FFndXaDousrTZTGM1j6FS2QWfoV6E4%2BQNmoM9S4tli7mRb38yh9XtH%2BWgyjx9xH4CnUU4yS3eU9VjKUOKVw6LpvNSTVzSOjijoIsaFH9z49dJZQIhBjJKMWbb14r71qMyN7HYMm2oz%2FHR1u79%2FM0yyVgtlLS5KCTKx06Sv7yPye63LQaDt&X-Amz-Signature=94864f5e29862597cb81b358db35b0c8ebb83e9c2e75fc235d6b1928ce7e0670&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IIELEJR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIE0AUABF%2FHZ%2Ft8sQMZgz8gIdlaKggGt4sSIkzv2g4eGzAiEApa17LKoQQ5nNRJUQ%2F7wjmOKuHbMvVIxpCfpBe95fUYEq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDMROhJ%2Fmn7wya%2FFAAircA8A%2BWDi2y0D2gtepWgkxfVjBZ%2F8thDhSYngQTCtVpwc0YTcalH6v2TdKxavYOGpCXoIGNGfRQGXMXbzHPzAAPGgZO%2BeRps8BVqRc19SVrUgKQLHmz2Ra9z6oxFEPI0%2F7e3%2FM%2FslzROzhWksKyW1ZrAnXmU9D7nXPIdHS%2BXD5MQWBnjf5qYEAKSLomjzLYcW%2B1p4fQyWNYwWiXPLkf%2FgOegWQNaV3ghmmCcWdBZgyenDb9q9YdPbteRfPypYdI3LNnGaufYyOxTpW0%2Bpztab%2FESKTniFZBgDD88WRedmOoPzqx2XiovzrPx2iC%2Fh0qcIxcgEclnvaFwVRKLOgJqHKo164aFnD5panYcHLQWkCemnux%2B9DRzs9MAfoMoO1bUpNd0FIniEWhHSYPXr1L8TgXHc8w2uCJLHiO%2Be%2FULvD8wr9DrpEd3%2FmZA%2F%2FPN7USwhPaeVcJM1vQxtw8vicPWTOIv1JFfXbgMXCDHQUfsX2dsSmK%2F%2FVwGtubmuxmHG4uTxBh2X1X%2BpaC%2BxWCNaWIv%2BmSufwhLVtSur6gFrk21C%2Fjz4n8oYfo%2FndA2osd1CHMeoSg7Tq3wmJMeZxvTVeoWKRNqtNOSqDhWfVSMUeT4p1gPEfPj6WHh36qf9YYB6ZMPWAjr0GOqUBA5nwaXz8sjATWzE9uYuRB0ZDQBXmM1oBgcj3ttOtrY%2FFndXaDousrTZTGM1j6FS2QWfoV6E4%2BQNmoM9S4tli7mRb38yh9XtH%2BWgyjx9xH4CnUU4yS3eU9VjKUOKVw6LpvNSTVzSOjijoIsaFH9z49dJZQIhBjJKMWbb14r71qMyN7HYMm2oz%2FHR1u79%2FM0yyVgtlLS5KCTKx06Sv7yPye63LQaDt&X-Amz-Signature=78a96e2021214b70d74caebd3cf18e2ea7c70fe7a606d52509ad463effd51b03&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IIELEJR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIE0AUABF%2FHZ%2Ft8sQMZgz8gIdlaKggGt4sSIkzv2g4eGzAiEApa17LKoQQ5nNRJUQ%2F7wjmOKuHbMvVIxpCfpBe95fUYEq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDMROhJ%2Fmn7wya%2FFAAircA8A%2BWDi2y0D2gtepWgkxfVjBZ%2F8thDhSYngQTCtVpwc0YTcalH6v2TdKxavYOGpCXoIGNGfRQGXMXbzHPzAAPGgZO%2BeRps8BVqRc19SVrUgKQLHmz2Ra9z6oxFEPI0%2F7e3%2FM%2FslzROzhWksKyW1ZrAnXmU9D7nXPIdHS%2BXD5MQWBnjf5qYEAKSLomjzLYcW%2B1p4fQyWNYwWiXPLkf%2FgOegWQNaV3ghmmCcWdBZgyenDb9q9YdPbteRfPypYdI3LNnGaufYyOxTpW0%2Bpztab%2FESKTniFZBgDD88WRedmOoPzqx2XiovzrPx2iC%2Fh0qcIxcgEclnvaFwVRKLOgJqHKo164aFnD5panYcHLQWkCemnux%2B9DRzs9MAfoMoO1bUpNd0FIniEWhHSYPXr1L8TgXHc8w2uCJLHiO%2Be%2FULvD8wr9DrpEd3%2FmZA%2F%2FPN7USwhPaeVcJM1vQxtw8vicPWTOIv1JFfXbgMXCDHQUfsX2dsSmK%2F%2FVwGtubmuxmHG4uTxBh2X1X%2BpaC%2BxWCNaWIv%2BmSufwhLVtSur6gFrk21C%2Fjz4n8oYfo%2FndA2osd1CHMeoSg7Tq3wmJMeZxvTVeoWKRNqtNOSqDhWfVSMUeT4p1gPEfPj6WHh36qf9YYB6ZMPWAjr0GOqUBA5nwaXz8sjATWzE9uYuRB0ZDQBXmM1oBgcj3ttOtrY%2FFndXaDousrTZTGM1j6FS2QWfoV6E4%2BQNmoM9S4tli7mRb38yh9XtH%2BWgyjx9xH4CnUU4yS3eU9VjKUOKVw6LpvNSTVzSOjijoIsaFH9z49dJZQIhBjJKMWbb14r71qMyN7HYMm2oz%2FHR1u79%2FM0yyVgtlLS5KCTKx06Sv7yPye63LQaDt&X-Amz-Signature=f75e45c772021b2102c7f85163cda429184aceaff0ed48cd88b9f0c90a8029dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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


