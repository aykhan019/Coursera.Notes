

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBEEVN7A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDxwvrcsB5elIwgk9erm2ZWCGyqBU1%2Bz0iHv6Kwgr06%2FwIhAPZLT0JfOs%2F48MfUrrzn7P6vehBJQs%2Bcw5kyiMwsKHh3KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwx6Ua7Yjczr%2BhC9%2B0q3AMTVzFF4uU%2Bj9gNSYWNO50dglzSTYpj0Kxx7UcBtQoDbTzAk6fDyd%2BIhhpUhskraE6FKioL%2FvqsjkbqaqhPCxlKofOfyHduTsTcueLpkOJbm2xiJiWd6eVP5CSUo86UsxJpzOsCwNNQEZq0Xx9Trl2%2FKEfVRpQRBWalU%2FUv83fv8XyVRrKUJ%2F5ZX3zkBoreciqw78ZsY69fVzaY9sFdF9F2r5UuZi9XmY3oX%2BCfJQU65QDWwgHE3j7PQyMXknA2xi8ouHos9yNsSq4xNVw6y7duLQmLaenHAIrSvlV5%2BoHpTQHJIKRkLsAUwPvez2Cr%2FtF7T94owodJ8eA2M79dAZ9%2FAO8HQCVpA5rGZ9ZlZIhOaazTEA1H4B1VJBbyAsEYByZopjyE4h%2B%2BuKhlr96KD62uWUPYtBpwt9qbyGkSHM5lGnP4S0m2FaL183pJ%2FOr5jJZApAAMV7Qy8VtS2zZsnzCOU%2FmqoTuU18ZMznfgWQTord6l%2Bw8Nlanqqkn2v9rpaKXpfx72A9BT4CgOZHrI20Gek70HMfdVnAYbzsJEMIF%2BmPrlM%2FJFN6CBVQGN6K%2ByQ%2FZ939lyFCQBVZKPofFGIrT8KRrSRRRP3nhjdujVWbIX1O4tOG2fXbr6E%2FGX2zD8uua8BjqkAcT1CwLJ9jR2c5znnHet%2Br0cicL8ja4d%2FPPgtbMLXzqQYYdIsn9rzqzgQDqvEPzH6%2FSEHb4Fre5sEynAYHF8R1%2FAk5J3%2Fck4oK2lHUMgOgo2FRDz6D3t7%2F5NtlTuClBLbn%2BLtvTwa43xbmgvWoKeto1ioZ7lVoatnFJef%2B3Ewo7Haxzn%2FFY7WbHmxBW3pVXQALgYnC605SL%2B5P95JCO2fYWb3UuJ&X-Amz-Signature=c3f3540093166770132e9b0bd1502733d546c675922fbfe50f80a730a96c00c5&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHNQVZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDHJ0L3gT1iP%2FQUfrd8cArQMWvM3MDw6t4JCM7j6SitEgIgO7UDwDLKZSsQy4ZOaJ313YzDJK%2BKCcT5TTm%2F8P5dHfAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqAP7XzKLFG646AcCrcA83zUSbfLAjW8bPk7aeam%2FmF16nTnK0OBrf1VojMfDUr21otigUxENZdgsowMoW7%2BtybF2FyA%2FF2itPpM6PFygdc%2BnLYbptjSuknODyuvc7mnE10jsvl4qcCShZcLaqMxb43PKgnXvMVn9Qb7WB0KFOXHs9J2Fwp5XUt19KkF5Vb6nvRR30sz9FrZX4pSBVv%2Bbcs59MhNRSxuNfcHmOxXuh6IBgyaGWv1q6SVwIRPj5rHCBYj6F5VrS1R3iZFLA02HsWdZ2W6jdrlHkDTApKXGGIKyZE48lyKk0AIsus3g4RBcSrG04sI0hZztkUJc%2FJxrhp0kIBBQEK%2F4CNHwqhllfIWQxIPXfCLALhhiZgx4s5lLtOhkMUI%2FxTCfehzVq%2BvwOZksRI49EPs8W7QSrY19WCRYdsORTy9fZ1GmyAClPZstRdicJUE2p%2FtxaeQmKIVBEeWnK%2BmgJ1mC49pyYPFqQ9t%2FYStQmQTyHsL3Iw0HOxbk6ZMSG4EjjU9oqW30Fh60kAFkLiz%2F%2BZm39KlcWgbQPHQpYtiEHnQKQLFhEoLESwiZiUOP6ScJwiTbfpSv3lXU2H%2F4EgFrdcuK%2B%2Bu%2FZS6pvbfgLzlxvZA8D85lDmPK6YtdPZUSy1KPVRs1xcMI275rwGOqUBi3%2Fui425U5rvkEIWSoQYmA3TwKN30tBCkcUglK7EsevXgjlSMnYzF4PrLFpAKivSqSM59awnDUQ%2BTRaOtuTi5gnl97QUqyeXusoXnJMHWmrVsSdKNbbycSd8ppH8vofrpFfebf0L3lTkIPNO9xfqyrVuHi6Pt82jEdLtAtzhNwu9OXG%2Fykub%2B1uHIIYYUEfx%2FJl8bFVYSj8ucqvFQ3zHJh4sCx%2BQ&X-Amz-Signature=c34b3073206dccbb116d617c84cbc45aa808079f36138ce15ea59106825cfc48&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHNQVZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDHJ0L3gT1iP%2FQUfrd8cArQMWvM3MDw6t4JCM7j6SitEgIgO7UDwDLKZSsQy4ZOaJ313YzDJK%2BKCcT5TTm%2F8P5dHfAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqAP7XzKLFG646AcCrcA83zUSbfLAjW8bPk7aeam%2FmF16nTnK0OBrf1VojMfDUr21otigUxENZdgsowMoW7%2BtybF2FyA%2FF2itPpM6PFygdc%2BnLYbptjSuknODyuvc7mnE10jsvl4qcCShZcLaqMxb43PKgnXvMVn9Qb7WB0KFOXHs9J2Fwp5XUt19KkF5Vb6nvRR30sz9FrZX4pSBVv%2Bbcs59MhNRSxuNfcHmOxXuh6IBgyaGWv1q6SVwIRPj5rHCBYj6F5VrS1R3iZFLA02HsWdZ2W6jdrlHkDTApKXGGIKyZE48lyKk0AIsus3g4RBcSrG04sI0hZztkUJc%2FJxrhp0kIBBQEK%2F4CNHwqhllfIWQxIPXfCLALhhiZgx4s5lLtOhkMUI%2FxTCfehzVq%2BvwOZksRI49EPs8W7QSrY19WCRYdsORTy9fZ1GmyAClPZstRdicJUE2p%2FtxaeQmKIVBEeWnK%2BmgJ1mC49pyYPFqQ9t%2FYStQmQTyHsL3Iw0HOxbk6ZMSG4EjjU9oqW30Fh60kAFkLiz%2F%2BZm39KlcWgbQPHQpYtiEHnQKQLFhEoLESwiZiUOP6ScJwiTbfpSv3lXU2H%2F4EgFrdcuK%2B%2Bu%2FZS6pvbfgLzlxvZA8D85lDmPK6YtdPZUSy1KPVRs1xcMI275rwGOqUBi3%2Fui425U5rvkEIWSoQYmA3TwKN30tBCkcUglK7EsevXgjlSMnYzF4PrLFpAKivSqSM59awnDUQ%2BTRaOtuTi5gnl97QUqyeXusoXnJMHWmrVsSdKNbbycSd8ppH8vofrpFfebf0L3lTkIPNO9xfqyrVuHi6Pt82jEdLtAtzhNwu9OXG%2Fykub%2B1uHIIYYUEfx%2FJl8bFVYSj8ucqvFQ3zHJh4sCx%2BQ&X-Amz-Signature=81100c360c3e732abea72244e1c31b3bd34a93a621996a3fea9590032a5a92dc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHNQVZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDHJ0L3gT1iP%2FQUfrd8cArQMWvM3MDw6t4JCM7j6SitEgIgO7UDwDLKZSsQy4ZOaJ313YzDJK%2BKCcT5TTm%2F8P5dHfAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqAP7XzKLFG646AcCrcA83zUSbfLAjW8bPk7aeam%2FmF16nTnK0OBrf1VojMfDUr21otigUxENZdgsowMoW7%2BtybF2FyA%2FF2itPpM6PFygdc%2BnLYbptjSuknODyuvc7mnE10jsvl4qcCShZcLaqMxb43PKgnXvMVn9Qb7WB0KFOXHs9J2Fwp5XUt19KkF5Vb6nvRR30sz9FrZX4pSBVv%2Bbcs59MhNRSxuNfcHmOxXuh6IBgyaGWv1q6SVwIRPj5rHCBYj6F5VrS1R3iZFLA02HsWdZ2W6jdrlHkDTApKXGGIKyZE48lyKk0AIsus3g4RBcSrG04sI0hZztkUJc%2FJxrhp0kIBBQEK%2F4CNHwqhllfIWQxIPXfCLALhhiZgx4s5lLtOhkMUI%2FxTCfehzVq%2BvwOZksRI49EPs8W7QSrY19WCRYdsORTy9fZ1GmyAClPZstRdicJUE2p%2FtxaeQmKIVBEeWnK%2BmgJ1mC49pyYPFqQ9t%2FYStQmQTyHsL3Iw0HOxbk6ZMSG4EjjU9oqW30Fh60kAFkLiz%2F%2BZm39KlcWgbQPHQpYtiEHnQKQLFhEoLESwiZiUOP6ScJwiTbfpSv3lXU2H%2F4EgFrdcuK%2B%2Bu%2FZS6pvbfgLzlxvZA8D85lDmPK6YtdPZUSy1KPVRs1xcMI275rwGOqUBi3%2Fui425U5rvkEIWSoQYmA3TwKN30tBCkcUglK7EsevXgjlSMnYzF4PrLFpAKivSqSM59awnDUQ%2BTRaOtuTi5gnl97QUqyeXusoXnJMHWmrVsSdKNbbycSd8ppH8vofrpFfebf0L3lTkIPNO9xfqyrVuHi6Pt82jEdLtAtzhNwu9OXG%2Fykub%2B1uHIIYYUEfx%2FJl8bFVYSj8ucqvFQ3zHJh4sCx%2BQ&X-Amz-Signature=6d5f8192ed1381831369b294fb0f4b5284611ae4ed8b563ac9829f279ebb35ca&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHNQVZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDHJ0L3gT1iP%2FQUfrd8cArQMWvM3MDw6t4JCM7j6SitEgIgO7UDwDLKZSsQy4ZOaJ313YzDJK%2BKCcT5TTm%2F8P5dHfAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqAP7XzKLFG646AcCrcA83zUSbfLAjW8bPk7aeam%2FmF16nTnK0OBrf1VojMfDUr21otigUxENZdgsowMoW7%2BtybF2FyA%2FF2itPpM6PFygdc%2BnLYbptjSuknODyuvc7mnE10jsvl4qcCShZcLaqMxb43PKgnXvMVn9Qb7WB0KFOXHs9J2Fwp5XUt19KkF5Vb6nvRR30sz9FrZX4pSBVv%2Bbcs59MhNRSxuNfcHmOxXuh6IBgyaGWv1q6SVwIRPj5rHCBYj6F5VrS1R3iZFLA02HsWdZ2W6jdrlHkDTApKXGGIKyZE48lyKk0AIsus3g4RBcSrG04sI0hZztkUJc%2FJxrhp0kIBBQEK%2F4CNHwqhllfIWQxIPXfCLALhhiZgx4s5lLtOhkMUI%2FxTCfehzVq%2BvwOZksRI49EPs8W7QSrY19WCRYdsORTy9fZ1GmyAClPZstRdicJUE2p%2FtxaeQmKIVBEeWnK%2BmgJ1mC49pyYPFqQ9t%2FYStQmQTyHsL3Iw0HOxbk6ZMSG4EjjU9oqW30Fh60kAFkLiz%2F%2BZm39KlcWgbQPHQpYtiEHnQKQLFhEoLESwiZiUOP6ScJwiTbfpSv3lXU2H%2F4EgFrdcuK%2B%2Bu%2FZS6pvbfgLzlxvZA8D85lDmPK6YtdPZUSy1KPVRs1xcMI275rwGOqUBi3%2Fui425U5rvkEIWSoQYmA3TwKN30tBCkcUglK7EsevXgjlSMnYzF4PrLFpAKivSqSM59awnDUQ%2BTRaOtuTi5gnl97QUqyeXusoXnJMHWmrVsSdKNbbycSd8ppH8vofrpFfebf0L3lTkIPNO9xfqyrVuHi6Pt82jEdLtAtzhNwu9OXG%2Fykub%2B1uHIIYYUEfx%2FJl8bFVYSj8ucqvFQ3zHJh4sCx%2BQ&X-Amz-Signature=5c6fc42fe0ed1054d0b85ba4466e0bd049e032a4cb0ca13d7cd4cfaad1541faf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHNQVZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDHJ0L3gT1iP%2FQUfrd8cArQMWvM3MDw6t4JCM7j6SitEgIgO7UDwDLKZSsQy4ZOaJ313YzDJK%2BKCcT5TTm%2F8P5dHfAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqAP7XzKLFG646AcCrcA83zUSbfLAjW8bPk7aeam%2FmF16nTnK0OBrf1VojMfDUr21otigUxENZdgsowMoW7%2BtybF2FyA%2FF2itPpM6PFygdc%2BnLYbptjSuknODyuvc7mnE10jsvl4qcCShZcLaqMxb43PKgnXvMVn9Qb7WB0KFOXHs9J2Fwp5XUt19KkF5Vb6nvRR30sz9FrZX4pSBVv%2Bbcs59MhNRSxuNfcHmOxXuh6IBgyaGWv1q6SVwIRPj5rHCBYj6F5VrS1R3iZFLA02HsWdZ2W6jdrlHkDTApKXGGIKyZE48lyKk0AIsus3g4RBcSrG04sI0hZztkUJc%2FJxrhp0kIBBQEK%2F4CNHwqhllfIWQxIPXfCLALhhiZgx4s5lLtOhkMUI%2FxTCfehzVq%2BvwOZksRI49EPs8W7QSrY19WCRYdsORTy9fZ1GmyAClPZstRdicJUE2p%2FtxaeQmKIVBEeWnK%2BmgJ1mC49pyYPFqQ9t%2FYStQmQTyHsL3Iw0HOxbk6ZMSG4EjjU9oqW30Fh60kAFkLiz%2F%2BZm39KlcWgbQPHQpYtiEHnQKQLFhEoLESwiZiUOP6ScJwiTbfpSv3lXU2H%2F4EgFrdcuK%2B%2Bu%2FZS6pvbfgLzlxvZA8D85lDmPK6YtdPZUSy1KPVRs1xcMI275rwGOqUBi3%2Fui425U5rvkEIWSoQYmA3TwKN30tBCkcUglK7EsevXgjlSMnYzF4PrLFpAKivSqSM59awnDUQ%2BTRaOtuTi5gnl97QUqyeXusoXnJMHWmrVsSdKNbbycSd8ppH8vofrpFfebf0L3lTkIPNO9xfqyrVuHi6Pt82jEdLtAtzhNwu9OXG%2Fykub%2B1uHIIYYUEfx%2FJl8bFVYSj8ucqvFQ3zHJh4sCx%2BQ&X-Amz-Signature=75af1238abb42f63031d32a6fe7965225256f04462f33563026abafb9a9193db&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBEEVN7A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDxwvrcsB5elIwgk9erm2ZWCGyqBU1%2Bz0iHv6Kwgr06%2FwIhAPZLT0JfOs%2F48MfUrrzn7P6vehBJQs%2Bcw5kyiMwsKHh3KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwx6Ua7Yjczr%2BhC9%2B0q3AMTVzFF4uU%2Bj9gNSYWNO50dglzSTYpj0Kxx7UcBtQoDbTzAk6fDyd%2BIhhpUhskraE6FKioL%2FvqsjkbqaqhPCxlKofOfyHduTsTcueLpkOJbm2xiJiWd6eVP5CSUo86UsxJpzOsCwNNQEZq0Xx9Trl2%2FKEfVRpQRBWalU%2FUv83fv8XyVRrKUJ%2F5ZX3zkBoreciqw78ZsY69fVzaY9sFdF9F2r5UuZi9XmY3oX%2BCfJQU65QDWwgHE3j7PQyMXknA2xi8ouHos9yNsSq4xNVw6y7duLQmLaenHAIrSvlV5%2BoHpTQHJIKRkLsAUwPvez2Cr%2FtF7T94owodJ8eA2M79dAZ9%2FAO8HQCVpA5rGZ9ZlZIhOaazTEA1H4B1VJBbyAsEYByZopjyE4h%2B%2BuKhlr96KD62uWUPYtBpwt9qbyGkSHM5lGnP4S0m2FaL183pJ%2FOr5jJZApAAMV7Qy8VtS2zZsnzCOU%2FmqoTuU18ZMznfgWQTord6l%2Bw8Nlanqqkn2v9rpaKXpfx72A9BT4CgOZHrI20Gek70HMfdVnAYbzsJEMIF%2BmPrlM%2FJFN6CBVQGN6K%2ByQ%2FZ939lyFCQBVZKPofFGIrT8KRrSRRRP3nhjdujVWbIX1O4tOG2fXbr6E%2FGX2zD8uua8BjqkAcT1CwLJ9jR2c5znnHet%2Br0cicL8ja4d%2FPPgtbMLXzqQYYdIsn9rzqzgQDqvEPzH6%2FSEHb4Fre5sEynAYHF8R1%2FAk5J3%2Fck4oK2lHUMgOgo2FRDz6D3t7%2F5NtlTuClBLbn%2BLtvTwa43xbmgvWoKeto1ioZ7lVoatnFJef%2B3Ewo7Haxzn%2FFY7WbHmxBW3pVXQALgYnC605SL%2B5P95JCO2fYWb3UuJ&X-Amz-Signature=cc5fc70fb414c8292f78493e6ea1f48e16e85891608e3b8c66a9751cf30f5320&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBEEVN7A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDxwvrcsB5elIwgk9erm2ZWCGyqBU1%2Bz0iHv6Kwgr06%2FwIhAPZLT0JfOs%2F48MfUrrzn7P6vehBJQs%2Bcw5kyiMwsKHh3KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwx6Ua7Yjczr%2BhC9%2B0q3AMTVzFF4uU%2Bj9gNSYWNO50dglzSTYpj0Kxx7UcBtQoDbTzAk6fDyd%2BIhhpUhskraE6FKioL%2FvqsjkbqaqhPCxlKofOfyHduTsTcueLpkOJbm2xiJiWd6eVP5CSUo86UsxJpzOsCwNNQEZq0Xx9Trl2%2FKEfVRpQRBWalU%2FUv83fv8XyVRrKUJ%2F5ZX3zkBoreciqw78ZsY69fVzaY9sFdF9F2r5UuZi9XmY3oX%2BCfJQU65QDWwgHE3j7PQyMXknA2xi8ouHos9yNsSq4xNVw6y7duLQmLaenHAIrSvlV5%2BoHpTQHJIKRkLsAUwPvez2Cr%2FtF7T94owodJ8eA2M79dAZ9%2FAO8HQCVpA5rGZ9ZlZIhOaazTEA1H4B1VJBbyAsEYByZopjyE4h%2B%2BuKhlr96KD62uWUPYtBpwt9qbyGkSHM5lGnP4S0m2FaL183pJ%2FOr5jJZApAAMV7Qy8VtS2zZsnzCOU%2FmqoTuU18ZMznfgWQTord6l%2Bw8Nlanqqkn2v9rpaKXpfx72A9BT4CgOZHrI20Gek70HMfdVnAYbzsJEMIF%2BmPrlM%2FJFN6CBVQGN6K%2ByQ%2FZ939lyFCQBVZKPofFGIrT8KRrSRRRP3nhjdujVWbIX1O4tOG2fXbr6E%2FGX2zD8uua8BjqkAcT1CwLJ9jR2c5znnHet%2Br0cicL8ja4d%2FPPgtbMLXzqQYYdIsn9rzqzgQDqvEPzH6%2FSEHb4Fre5sEynAYHF8R1%2FAk5J3%2Fck4oK2lHUMgOgo2FRDz6D3t7%2F5NtlTuClBLbn%2BLtvTwa43xbmgvWoKeto1ioZ7lVoatnFJef%2B3Ewo7Haxzn%2FFY7WbHmxBW3pVXQALgYnC605SL%2B5P95JCO2fYWb3UuJ&X-Amz-Signature=550faf83ba3365b992af8c1b4d5f4e3946c8e0ce3b0e931f7971e1f2c8ab6e6f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBEEVN7A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDxwvrcsB5elIwgk9erm2ZWCGyqBU1%2Bz0iHv6Kwgr06%2FwIhAPZLT0JfOs%2F48MfUrrzn7P6vehBJQs%2Bcw5kyiMwsKHh3KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwx6Ua7Yjczr%2BhC9%2B0q3AMTVzFF4uU%2Bj9gNSYWNO50dglzSTYpj0Kxx7UcBtQoDbTzAk6fDyd%2BIhhpUhskraE6FKioL%2FvqsjkbqaqhPCxlKofOfyHduTsTcueLpkOJbm2xiJiWd6eVP5CSUo86UsxJpzOsCwNNQEZq0Xx9Trl2%2FKEfVRpQRBWalU%2FUv83fv8XyVRrKUJ%2F5ZX3zkBoreciqw78ZsY69fVzaY9sFdF9F2r5UuZi9XmY3oX%2BCfJQU65QDWwgHE3j7PQyMXknA2xi8ouHos9yNsSq4xNVw6y7duLQmLaenHAIrSvlV5%2BoHpTQHJIKRkLsAUwPvez2Cr%2FtF7T94owodJ8eA2M79dAZ9%2FAO8HQCVpA5rGZ9ZlZIhOaazTEA1H4B1VJBbyAsEYByZopjyE4h%2B%2BuKhlr96KD62uWUPYtBpwt9qbyGkSHM5lGnP4S0m2FaL183pJ%2FOr5jJZApAAMV7Qy8VtS2zZsnzCOU%2FmqoTuU18ZMznfgWQTord6l%2Bw8Nlanqqkn2v9rpaKXpfx72A9BT4CgOZHrI20Gek70HMfdVnAYbzsJEMIF%2BmPrlM%2FJFN6CBVQGN6K%2ByQ%2FZ939lyFCQBVZKPofFGIrT8KRrSRRRP3nhjdujVWbIX1O4tOG2fXbr6E%2FGX2zD8uua8BjqkAcT1CwLJ9jR2c5znnHet%2Br0cicL8ja4d%2FPPgtbMLXzqQYYdIsn9rzqzgQDqvEPzH6%2FSEHb4Fre5sEynAYHF8R1%2FAk5J3%2Fck4oK2lHUMgOgo2FRDz6D3t7%2F5NtlTuClBLbn%2BLtvTwa43xbmgvWoKeto1ioZ7lVoatnFJef%2B3Ewo7Haxzn%2FFY7WbHmxBW3pVXQALgYnC605SL%2B5P95JCO2fYWb3UuJ&X-Amz-Signature=890940e8b2854ae16b8ebd2180f3e55dc3d1acce334f366d1cc8499d9f9190de&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBEEVN7A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDxwvrcsB5elIwgk9erm2ZWCGyqBU1%2Bz0iHv6Kwgr06%2FwIhAPZLT0JfOs%2F48MfUrrzn7P6vehBJQs%2Bcw5kyiMwsKHh3KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwx6Ua7Yjczr%2BhC9%2B0q3AMTVzFF4uU%2Bj9gNSYWNO50dglzSTYpj0Kxx7UcBtQoDbTzAk6fDyd%2BIhhpUhskraE6FKioL%2FvqsjkbqaqhPCxlKofOfyHduTsTcueLpkOJbm2xiJiWd6eVP5CSUo86UsxJpzOsCwNNQEZq0Xx9Trl2%2FKEfVRpQRBWalU%2FUv83fv8XyVRrKUJ%2F5ZX3zkBoreciqw78ZsY69fVzaY9sFdF9F2r5UuZi9XmY3oX%2BCfJQU65QDWwgHE3j7PQyMXknA2xi8ouHos9yNsSq4xNVw6y7duLQmLaenHAIrSvlV5%2BoHpTQHJIKRkLsAUwPvez2Cr%2FtF7T94owodJ8eA2M79dAZ9%2FAO8HQCVpA5rGZ9ZlZIhOaazTEA1H4B1VJBbyAsEYByZopjyE4h%2B%2BuKhlr96KD62uWUPYtBpwt9qbyGkSHM5lGnP4S0m2FaL183pJ%2FOr5jJZApAAMV7Qy8VtS2zZsnzCOU%2FmqoTuU18ZMznfgWQTord6l%2Bw8Nlanqqkn2v9rpaKXpfx72A9BT4CgOZHrI20Gek70HMfdVnAYbzsJEMIF%2BmPrlM%2FJFN6CBVQGN6K%2ByQ%2FZ939lyFCQBVZKPofFGIrT8KRrSRRRP3nhjdujVWbIX1O4tOG2fXbr6E%2FGX2zD8uua8BjqkAcT1CwLJ9jR2c5znnHet%2Br0cicL8ja4d%2FPPgtbMLXzqQYYdIsn9rzqzgQDqvEPzH6%2FSEHb4Fre5sEynAYHF8R1%2FAk5J3%2Fck4oK2lHUMgOgo2FRDz6D3t7%2F5NtlTuClBLbn%2BLtvTwa43xbmgvWoKeto1ioZ7lVoatnFJef%2B3Ewo7Haxzn%2FFY7WbHmxBW3pVXQALgYnC605SL%2B5P95JCO2fYWb3UuJ&X-Amz-Signature=bbfce8512906bab064f820919c0baab0750cf0e4649054da87d0d68fcd44f447&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBEEVN7A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDxwvrcsB5elIwgk9erm2ZWCGyqBU1%2Bz0iHv6Kwgr06%2FwIhAPZLT0JfOs%2F48MfUrrzn7P6vehBJQs%2Bcw5kyiMwsKHh3KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwx6Ua7Yjczr%2BhC9%2B0q3AMTVzFF4uU%2Bj9gNSYWNO50dglzSTYpj0Kxx7UcBtQoDbTzAk6fDyd%2BIhhpUhskraE6FKioL%2FvqsjkbqaqhPCxlKofOfyHduTsTcueLpkOJbm2xiJiWd6eVP5CSUo86UsxJpzOsCwNNQEZq0Xx9Trl2%2FKEfVRpQRBWalU%2FUv83fv8XyVRrKUJ%2F5ZX3zkBoreciqw78ZsY69fVzaY9sFdF9F2r5UuZi9XmY3oX%2BCfJQU65QDWwgHE3j7PQyMXknA2xi8ouHos9yNsSq4xNVw6y7duLQmLaenHAIrSvlV5%2BoHpTQHJIKRkLsAUwPvez2Cr%2FtF7T94owodJ8eA2M79dAZ9%2FAO8HQCVpA5rGZ9ZlZIhOaazTEA1H4B1VJBbyAsEYByZopjyE4h%2B%2BuKhlr96KD62uWUPYtBpwt9qbyGkSHM5lGnP4S0m2FaL183pJ%2FOr5jJZApAAMV7Qy8VtS2zZsnzCOU%2FmqoTuU18ZMznfgWQTord6l%2Bw8Nlanqqkn2v9rpaKXpfx72A9BT4CgOZHrI20Gek70HMfdVnAYbzsJEMIF%2BmPrlM%2FJFN6CBVQGN6K%2ByQ%2FZ939lyFCQBVZKPofFGIrT8KRrSRRRP3nhjdujVWbIX1O4tOG2fXbr6E%2FGX2zD8uua8BjqkAcT1CwLJ9jR2c5znnHet%2Br0cicL8ja4d%2FPPgtbMLXzqQYYdIsn9rzqzgQDqvEPzH6%2FSEHb4Fre5sEynAYHF8R1%2FAk5J3%2Fck4oK2lHUMgOgo2FRDz6D3t7%2F5NtlTuClBLbn%2BLtvTwa43xbmgvWoKeto1ioZ7lVoatnFJef%2B3Ewo7Haxzn%2FFY7WbHmxBW3pVXQALgYnC605SL%2B5P95JCO2fYWb3UuJ&X-Amz-Signature=d2dd1fd825726d6a34b3ddcd3dac4faa99025fdf19d94a51b665b24d15d5b937&X-Amz-SignedHeaders=host&x-id=GetObject)
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


