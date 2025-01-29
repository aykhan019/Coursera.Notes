

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KGXMCFY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIDcaHDqYwon1NhizC0AFR%2F2PlHiEadkJpjPf%2FTD%2FYIkgAiEAlPKYy58huZSOwnM5hT1wyYASRgdGGwM0cWhGsqQ8Z5MqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6FQTlGAUmg3C8K6CrcA4LyGrmcMdUXWMubqnuWcSaaNn9bDbqcHeaPNd1YP3iI%2BA9Bln7Scrhfw0mkjtjGJ8MkcexmXhuKGzZkDBPdAURUw%2FMO1xufuJSseUJSz9m%2FsNw7F1VwHrRwdEXW4x2uJowb5x3LYqmXlKVOeC4Z5W82u%2FJAiW3H188xmCyuEBKju96XphZCSqTw0ntVzyDO0tRVShAe9fi6HJBLTzWIu9SMkayRK%2FZ2UntOKXJq%2B41RolHuzaO5R%2BOQ%2FMKKJoOEtBeTlCzIjha%2FZ6A8p4EHuP4OipJRpZrFfGB9wrBOKzZtSRLVpE9iMt5vxsdOdytbUdPjsm2F8gqTrkHt3nVEF7HL1M3RYvBs9isI6qh9VXLhIDQGJPs8iSD35abUGZa8BApQlPgt0txpQM877PIaw4leu6QTrdPTAgmkXF9tYcvpkvwqXHm4l52H%2Bzifc1qzEAcZGMMi96cvs9NLWZx%2BUNkgfkPVFKiY4Wvo0E4CMZOKPu3SYDrmi8eUZStIi%2FYSfbMBfmCUU52KWM4y7C9R8EUlVcaz5YEaOLxFVEYUn0Jc832HWG3GYEcnuRQZRE01BjG3JwqJWpxJwTCHP1pq0WMcS1H4i2s42KrtIhmjKmsyIBLUZ61KRGUaC1VwMIKg5rwGOqUBleOS90WoW092QnvNeyrufu8nzXvAqiGVova95iIJpVB%2BrevjVNZ4I4uVbL5j9wIdmrpIPC196kNsD0ERHD0n%2F0JEJZAINdiPhRnDW8712P%2FxZJtTwxLdPk8t3ylJVmtkqVqL3eR8O%2BXIkDh51zXZbksaUs1gCJlocFWmP53d0r%2FBiANWs57A%2B%2BjlnBU7BuvUr7EE3jmCSEsahMw9vaoxfE4cwH7a&X-Amz-Signature=43893b0a8d9252a0cf8fe501d4d2bcbf238195227f97c913633a55b1edc05ed8&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2RT5K3T%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDj7WwQreImpMBNRS1ehQxw41SVfdCst8zHml%2BtrOmrLwIgKhQkF%2BF%2FTHvTu5dieMHAN0LKi3kAHuRI8eukKriBNb4qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOo3juXukKIe2C7zGSrcA6oAF5%2BJCtoKqYi%2FcFHpxUM3VPn7a3%2FUqg%2FoVfilfj7GNvrYA9xpic91YnVHByPpRJLdfWcOcXY5C4DV1tAYFH0xI8oe53GY4Nvp%2BJMk75p3fVvkNcJgpqutbraZN8kcibOdVnVf%2BtMruUg4r2sxIRm4OhF%2FZMc53P6%2FhPe5GEY1WNAI1%2FNNP78W2URVAgQenXwF%2FNh20Tgk35YyrJbTRaclUBWfxfYCAcxUyWtvzGnkq3E42JXDR5HqZ3V1jMYXfKT6NFrzyJ3L1Raht72UjaKdapgxKMU%2BvEEfV0xvwdlkjldVc29X00cNHMTquCY4k%2FTrQY3liDTz00tk33xL3S2Apg1iIHuyVd4Sz6Xi8i1BiHJIdTJIFiPhPIQxhhmnq0GhP9yG26mFjXw2th3wN%2Fc7grU2jXXzO3jZ25S%2Fu%2BUaXi0mCAnoVvOVc1OjEtDc4MVfkMF2kCRiFUf2Le1zBX1FEex%2F58Gk4LGcB%2FrH98Pcdb6BDp6yFzn6JH3o9vGl7bvoH1rQtEzCzgd9xW%2FMepFYK19CcpA45OiDe4yHD%2BQVXrw6xg7C28bNkZC61sTaHf34u61W6WS9UMIR40RG6Vbwzl13iLlrrCLH0V6m5qcEAh2xS6nynANYyaSoMMCf5rwGOqUB0LH1ql0eEOUrFzhnaJ5wsRBqk0pC%2FAG6ifdc%2Fse5%2FxzdIUhNQovjYWIhtP%2B3osp0rVUXLCGBy8XJ5sHo2W5lZSUywS%2FEfvwPqvThu8KlyS%2BUWaZrDgxHI0qJ9kZycZlSDOG5M4eT4Wsyp7CJv6KC72M5mxKibQsjYi7J1OVAVX9%2Fa39IXPmrMm%2FfgmxA7BTXSGWAKaSS%2B7mjodUZjdfQKp0HreGk&X-Amz-Signature=5702e96c5afe664318602544c3fc983d1f06b48a10a40cbd5aa6938220ee10f1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2RT5K3T%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDj7WwQreImpMBNRS1ehQxw41SVfdCst8zHml%2BtrOmrLwIgKhQkF%2BF%2FTHvTu5dieMHAN0LKi3kAHuRI8eukKriBNb4qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOo3juXukKIe2C7zGSrcA6oAF5%2BJCtoKqYi%2FcFHpxUM3VPn7a3%2FUqg%2FoVfilfj7GNvrYA9xpic91YnVHByPpRJLdfWcOcXY5C4DV1tAYFH0xI8oe53GY4Nvp%2BJMk75p3fVvkNcJgpqutbraZN8kcibOdVnVf%2BtMruUg4r2sxIRm4OhF%2FZMc53P6%2FhPe5GEY1WNAI1%2FNNP78W2URVAgQenXwF%2FNh20Tgk35YyrJbTRaclUBWfxfYCAcxUyWtvzGnkq3E42JXDR5HqZ3V1jMYXfKT6NFrzyJ3L1Raht72UjaKdapgxKMU%2BvEEfV0xvwdlkjldVc29X00cNHMTquCY4k%2FTrQY3liDTz00tk33xL3S2Apg1iIHuyVd4Sz6Xi8i1BiHJIdTJIFiPhPIQxhhmnq0GhP9yG26mFjXw2th3wN%2Fc7grU2jXXzO3jZ25S%2Fu%2BUaXi0mCAnoVvOVc1OjEtDc4MVfkMF2kCRiFUf2Le1zBX1FEex%2F58Gk4LGcB%2FrH98Pcdb6BDp6yFzn6JH3o9vGl7bvoH1rQtEzCzgd9xW%2FMepFYK19CcpA45OiDe4yHD%2BQVXrw6xg7C28bNkZC61sTaHf34u61W6WS9UMIR40RG6Vbwzl13iLlrrCLH0V6m5qcEAh2xS6nynANYyaSoMMCf5rwGOqUB0LH1ql0eEOUrFzhnaJ5wsRBqk0pC%2FAG6ifdc%2Fse5%2FxzdIUhNQovjYWIhtP%2B3osp0rVUXLCGBy8XJ5sHo2W5lZSUywS%2FEfvwPqvThu8KlyS%2BUWaZrDgxHI0qJ9kZycZlSDOG5M4eT4Wsyp7CJv6KC72M5mxKibQsjYi7J1OVAVX9%2Fa39IXPmrMm%2FfgmxA7BTXSGWAKaSS%2B7mjodUZjdfQKp0HreGk&X-Amz-Signature=ee8edc2ce4bd4aeab6ead9aa4de0fff0a50ebe92b8831fc46922f7c98f7150d9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2RT5K3T%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDj7WwQreImpMBNRS1ehQxw41SVfdCst8zHml%2BtrOmrLwIgKhQkF%2BF%2FTHvTu5dieMHAN0LKi3kAHuRI8eukKriBNb4qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOo3juXukKIe2C7zGSrcA6oAF5%2BJCtoKqYi%2FcFHpxUM3VPn7a3%2FUqg%2FoVfilfj7GNvrYA9xpic91YnVHByPpRJLdfWcOcXY5C4DV1tAYFH0xI8oe53GY4Nvp%2BJMk75p3fVvkNcJgpqutbraZN8kcibOdVnVf%2BtMruUg4r2sxIRm4OhF%2FZMc53P6%2FhPe5GEY1WNAI1%2FNNP78W2URVAgQenXwF%2FNh20Tgk35YyrJbTRaclUBWfxfYCAcxUyWtvzGnkq3E42JXDR5HqZ3V1jMYXfKT6NFrzyJ3L1Raht72UjaKdapgxKMU%2BvEEfV0xvwdlkjldVc29X00cNHMTquCY4k%2FTrQY3liDTz00tk33xL3S2Apg1iIHuyVd4Sz6Xi8i1BiHJIdTJIFiPhPIQxhhmnq0GhP9yG26mFjXw2th3wN%2Fc7grU2jXXzO3jZ25S%2Fu%2BUaXi0mCAnoVvOVc1OjEtDc4MVfkMF2kCRiFUf2Le1zBX1FEex%2F58Gk4LGcB%2FrH98Pcdb6BDp6yFzn6JH3o9vGl7bvoH1rQtEzCzgd9xW%2FMepFYK19CcpA45OiDe4yHD%2BQVXrw6xg7C28bNkZC61sTaHf34u61W6WS9UMIR40RG6Vbwzl13iLlrrCLH0V6m5qcEAh2xS6nynANYyaSoMMCf5rwGOqUB0LH1ql0eEOUrFzhnaJ5wsRBqk0pC%2FAG6ifdc%2Fse5%2FxzdIUhNQovjYWIhtP%2B3osp0rVUXLCGBy8XJ5sHo2W5lZSUywS%2FEfvwPqvThu8KlyS%2BUWaZrDgxHI0qJ9kZycZlSDOG5M4eT4Wsyp7CJv6KC72M5mxKibQsjYi7J1OVAVX9%2Fa39IXPmrMm%2FfgmxA7BTXSGWAKaSS%2B7mjodUZjdfQKp0HreGk&X-Amz-Signature=c7ce0fafccfeeda8a01b4c01b7d664d4100b5406b1256910148b6fc4bc95cd35&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2RT5K3T%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDj7WwQreImpMBNRS1ehQxw41SVfdCst8zHml%2BtrOmrLwIgKhQkF%2BF%2FTHvTu5dieMHAN0LKi3kAHuRI8eukKriBNb4qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOo3juXukKIe2C7zGSrcA6oAF5%2BJCtoKqYi%2FcFHpxUM3VPn7a3%2FUqg%2FoVfilfj7GNvrYA9xpic91YnVHByPpRJLdfWcOcXY5C4DV1tAYFH0xI8oe53GY4Nvp%2BJMk75p3fVvkNcJgpqutbraZN8kcibOdVnVf%2BtMruUg4r2sxIRm4OhF%2FZMc53P6%2FhPe5GEY1WNAI1%2FNNP78W2URVAgQenXwF%2FNh20Tgk35YyrJbTRaclUBWfxfYCAcxUyWtvzGnkq3E42JXDR5HqZ3V1jMYXfKT6NFrzyJ3L1Raht72UjaKdapgxKMU%2BvEEfV0xvwdlkjldVc29X00cNHMTquCY4k%2FTrQY3liDTz00tk33xL3S2Apg1iIHuyVd4Sz6Xi8i1BiHJIdTJIFiPhPIQxhhmnq0GhP9yG26mFjXw2th3wN%2Fc7grU2jXXzO3jZ25S%2Fu%2BUaXi0mCAnoVvOVc1OjEtDc4MVfkMF2kCRiFUf2Le1zBX1FEex%2F58Gk4LGcB%2FrH98Pcdb6BDp6yFzn6JH3o9vGl7bvoH1rQtEzCzgd9xW%2FMepFYK19CcpA45OiDe4yHD%2BQVXrw6xg7C28bNkZC61sTaHf34u61W6WS9UMIR40RG6Vbwzl13iLlrrCLH0V6m5qcEAh2xS6nynANYyaSoMMCf5rwGOqUB0LH1ql0eEOUrFzhnaJ5wsRBqk0pC%2FAG6ifdc%2Fse5%2FxzdIUhNQovjYWIhtP%2B3osp0rVUXLCGBy8XJ5sHo2W5lZSUywS%2FEfvwPqvThu8KlyS%2BUWaZrDgxHI0qJ9kZycZlSDOG5M4eT4Wsyp7CJv6KC72M5mxKibQsjYi7J1OVAVX9%2Fa39IXPmrMm%2FfgmxA7BTXSGWAKaSS%2B7mjodUZjdfQKp0HreGk&X-Amz-Signature=da7693dedba834eff07afbc28faebe60b8b1f4a1c1fb5ba3b888d853fd716430&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2RT5K3T%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDj7WwQreImpMBNRS1ehQxw41SVfdCst8zHml%2BtrOmrLwIgKhQkF%2BF%2FTHvTu5dieMHAN0LKi3kAHuRI8eukKriBNb4qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOo3juXukKIe2C7zGSrcA6oAF5%2BJCtoKqYi%2FcFHpxUM3VPn7a3%2FUqg%2FoVfilfj7GNvrYA9xpic91YnVHByPpRJLdfWcOcXY5C4DV1tAYFH0xI8oe53GY4Nvp%2BJMk75p3fVvkNcJgpqutbraZN8kcibOdVnVf%2BtMruUg4r2sxIRm4OhF%2FZMc53P6%2FhPe5GEY1WNAI1%2FNNP78W2URVAgQenXwF%2FNh20Tgk35YyrJbTRaclUBWfxfYCAcxUyWtvzGnkq3E42JXDR5HqZ3V1jMYXfKT6NFrzyJ3L1Raht72UjaKdapgxKMU%2BvEEfV0xvwdlkjldVc29X00cNHMTquCY4k%2FTrQY3liDTz00tk33xL3S2Apg1iIHuyVd4Sz6Xi8i1BiHJIdTJIFiPhPIQxhhmnq0GhP9yG26mFjXw2th3wN%2Fc7grU2jXXzO3jZ25S%2Fu%2BUaXi0mCAnoVvOVc1OjEtDc4MVfkMF2kCRiFUf2Le1zBX1FEex%2F58Gk4LGcB%2FrH98Pcdb6BDp6yFzn6JH3o9vGl7bvoH1rQtEzCzgd9xW%2FMepFYK19CcpA45OiDe4yHD%2BQVXrw6xg7C28bNkZC61sTaHf34u61W6WS9UMIR40RG6Vbwzl13iLlrrCLH0V6m5qcEAh2xS6nynANYyaSoMMCf5rwGOqUB0LH1ql0eEOUrFzhnaJ5wsRBqk0pC%2FAG6ifdc%2Fse5%2FxzdIUhNQovjYWIhtP%2B3osp0rVUXLCGBy8XJ5sHo2W5lZSUywS%2FEfvwPqvThu8KlyS%2BUWaZrDgxHI0qJ9kZycZlSDOG5M4eT4Wsyp7CJv6KC72M5mxKibQsjYi7J1OVAVX9%2Fa39IXPmrMm%2FfgmxA7BTXSGWAKaSS%2B7mjodUZjdfQKp0HreGk&X-Amz-Signature=738e6d654b0bd835357a285fa3ef638f9e355f8d88852bc8936734e69a5b7078&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KGXMCFY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIDcaHDqYwon1NhizC0AFR%2F2PlHiEadkJpjPf%2FTD%2FYIkgAiEAlPKYy58huZSOwnM5hT1wyYASRgdGGwM0cWhGsqQ8Z5MqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6FQTlGAUmg3C8K6CrcA4LyGrmcMdUXWMubqnuWcSaaNn9bDbqcHeaPNd1YP3iI%2BA9Bln7Scrhfw0mkjtjGJ8MkcexmXhuKGzZkDBPdAURUw%2FMO1xufuJSseUJSz9m%2FsNw7F1VwHrRwdEXW4x2uJowb5x3LYqmXlKVOeC4Z5W82u%2FJAiW3H188xmCyuEBKju96XphZCSqTw0ntVzyDO0tRVShAe9fi6HJBLTzWIu9SMkayRK%2FZ2UntOKXJq%2B41RolHuzaO5R%2BOQ%2FMKKJoOEtBeTlCzIjha%2FZ6A8p4EHuP4OipJRpZrFfGB9wrBOKzZtSRLVpE9iMt5vxsdOdytbUdPjsm2F8gqTrkHt3nVEF7HL1M3RYvBs9isI6qh9VXLhIDQGJPs8iSD35abUGZa8BApQlPgt0txpQM877PIaw4leu6QTrdPTAgmkXF9tYcvpkvwqXHm4l52H%2Bzifc1qzEAcZGMMi96cvs9NLWZx%2BUNkgfkPVFKiY4Wvo0E4CMZOKPu3SYDrmi8eUZStIi%2FYSfbMBfmCUU52KWM4y7C9R8EUlVcaz5YEaOLxFVEYUn0Jc832HWG3GYEcnuRQZRE01BjG3JwqJWpxJwTCHP1pq0WMcS1H4i2s42KrtIhmjKmsyIBLUZ61KRGUaC1VwMIKg5rwGOqUBleOS90WoW092QnvNeyrufu8nzXvAqiGVova95iIJpVB%2BrevjVNZ4I4uVbL5j9wIdmrpIPC196kNsD0ERHD0n%2F0JEJZAINdiPhRnDW8712P%2FxZJtTwxLdPk8t3ylJVmtkqVqL3eR8O%2BXIkDh51zXZbksaUs1gCJlocFWmP53d0r%2FBiANWs57A%2B%2BjlnBU7BuvUr7EE3jmCSEsahMw9vaoxfE4cwH7a&X-Amz-Signature=b8ba172226467069749cc1a468a385d1b1f78e161c55a5875ffe1f17bb783456&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KGXMCFY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIDcaHDqYwon1NhizC0AFR%2F2PlHiEadkJpjPf%2FTD%2FYIkgAiEAlPKYy58huZSOwnM5hT1wyYASRgdGGwM0cWhGsqQ8Z5MqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6FQTlGAUmg3C8K6CrcA4LyGrmcMdUXWMubqnuWcSaaNn9bDbqcHeaPNd1YP3iI%2BA9Bln7Scrhfw0mkjtjGJ8MkcexmXhuKGzZkDBPdAURUw%2FMO1xufuJSseUJSz9m%2FsNw7F1VwHrRwdEXW4x2uJowb5x3LYqmXlKVOeC4Z5W82u%2FJAiW3H188xmCyuEBKju96XphZCSqTw0ntVzyDO0tRVShAe9fi6HJBLTzWIu9SMkayRK%2FZ2UntOKXJq%2B41RolHuzaO5R%2BOQ%2FMKKJoOEtBeTlCzIjha%2FZ6A8p4EHuP4OipJRpZrFfGB9wrBOKzZtSRLVpE9iMt5vxsdOdytbUdPjsm2F8gqTrkHt3nVEF7HL1M3RYvBs9isI6qh9VXLhIDQGJPs8iSD35abUGZa8BApQlPgt0txpQM877PIaw4leu6QTrdPTAgmkXF9tYcvpkvwqXHm4l52H%2Bzifc1qzEAcZGMMi96cvs9NLWZx%2BUNkgfkPVFKiY4Wvo0E4CMZOKPu3SYDrmi8eUZStIi%2FYSfbMBfmCUU52KWM4y7C9R8EUlVcaz5YEaOLxFVEYUn0Jc832HWG3GYEcnuRQZRE01BjG3JwqJWpxJwTCHP1pq0WMcS1H4i2s42KrtIhmjKmsyIBLUZ61KRGUaC1VwMIKg5rwGOqUBleOS90WoW092QnvNeyrufu8nzXvAqiGVova95iIJpVB%2BrevjVNZ4I4uVbL5j9wIdmrpIPC196kNsD0ERHD0n%2F0JEJZAINdiPhRnDW8712P%2FxZJtTwxLdPk8t3ylJVmtkqVqL3eR8O%2BXIkDh51zXZbksaUs1gCJlocFWmP53d0r%2FBiANWs57A%2B%2BjlnBU7BuvUr7EE3jmCSEsahMw9vaoxfE4cwH7a&X-Amz-Signature=c4933fe1b7f12f9a153dbbeb80c0f592f958f793f72f784e71629d27a33352c3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KGXMCFY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIDcaHDqYwon1NhizC0AFR%2F2PlHiEadkJpjPf%2FTD%2FYIkgAiEAlPKYy58huZSOwnM5hT1wyYASRgdGGwM0cWhGsqQ8Z5MqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6FQTlGAUmg3C8K6CrcA4LyGrmcMdUXWMubqnuWcSaaNn9bDbqcHeaPNd1YP3iI%2BA9Bln7Scrhfw0mkjtjGJ8MkcexmXhuKGzZkDBPdAURUw%2FMO1xufuJSseUJSz9m%2FsNw7F1VwHrRwdEXW4x2uJowb5x3LYqmXlKVOeC4Z5W82u%2FJAiW3H188xmCyuEBKju96XphZCSqTw0ntVzyDO0tRVShAe9fi6HJBLTzWIu9SMkayRK%2FZ2UntOKXJq%2B41RolHuzaO5R%2BOQ%2FMKKJoOEtBeTlCzIjha%2FZ6A8p4EHuP4OipJRpZrFfGB9wrBOKzZtSRLVpE9iMt5vxsdOdytbUdPjsm2F8gqTrkHt3nVEF7HL1M3RYvBs9isI6qh9VXLhIDQGJPs8iSD35abUGZa8BApQlPgt0txpQM877PIaw4leu6QTrdPTAgmkXF9tYcvpkvwqXHm4l52H%2Bzifc1qzEAcZGMMi96cvs9NLWZx%2BUNkgfkPVFKiY4Wvo0E4CMZOKPu3SYDrmi8eUZStIi%2FYSfbMBfmCUU52KWM4y7C9R8EUlVcaz5YEaOLxFVEYUn0Jc832HWG3GYEcnuRQZRE01BjG3JwqJWpxJwTCHP1pq0WMcS1H4i2s42KrtIhmjKmsyIBLUZ61KRGUaC1VwMIKg5rwGOqUBleOS90WoW092QnvNeyrufu8nzXvAqiGVova95iIJpVB%2BrevjVNZ4I4uVbL5j9wIdmrpIPC196kNsD0ERHD0n%2F0JEJZAINdiPhRnDW8712P%2FxZJtTwxLdPk8t3ylJVmtkqVqL3eR8O%2BXIkDh51zXZbksaUs1gCJlocFWmP53d0r%2FBiANWs57A%2B%2BjlnBU7BuvUr7EE3jmCSEsahMw9vaoxfE4cwH7a&X-Amz-Signature=89841f3d6841677f705397ecb3c9480f88ab3c27481486aaefcec25bfd2a32ce&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KGXMCFY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIDcaHDqYwon1NhizC0AFR%2F2PlHiEadkJpjPf%2FTD%2FYIkgAiEAlPKYy58huZSOwnM5hT1wyYASRgdGGwM0cWhGsqQ8Z5MqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6FQTlGAUmg3C8K6CrcA4LyGrmcMdUXWMubqnuWcSaaNn9bDbqcHeaPNd1YP3iI%2BA9Bln7Scrhfw0mkjtjGJ8MkcexmXhuKGzZkDBPdAURUw%2FMO1xufuJSseUJSz9m%2FsNw7F1VwHrRwdEXW4x2uJowb5x3LYqmXlKVOeC4Z5W82u%2FJAiW3H188xmCyuEBKju96XphZCSqTw0ntVzyDO0tRVShAe9fi6HJBLTzWIu9SMkayRK%2FZ2UntOKXJq%2B41RolHuzaO5R%2BOQ%2FMKKJoOEtBeTlCzIjha%2FZ6A8p4EHuP4OipJRpZrFfGB9wrBOKzZtSRLVpE9iMt5vxsdOdytbUdPjsm2F8gqTrkHt3nVEF7HL1M3RYvBs9isI6qh9VXLhIDQGJPs8iSD35abUGZa8BApQlPgt0txpQM877PIaw4leu6QTrdPTAgmkXF9tYcvpkvwqXHm4l52H%2Bzifc1qzEAcZGMMi96cvs9NLWZx%2BUNkgfkPVFKiY4Wvo0E4CMZOKPu3SYDrmi8eUZStIi%2FYSfbMBfmCUU52KWM4y7C9R8EUlVcaz5YEaOLxFVEYUn0Jc832HWG3GYEcnuRQZRE01BjG3JwqJWpxJwTCHP1pq0WMcS1H4i2s42KrtIhmjKmsyIBLUZ61KRGUaC1VwMIKg5rwGOqUBleOS90WoW092QnvNeyrufu8nzXvAqiGVova95iIJpVB%2BrevjVNZ4I4uVbL5j9wIdmrpIPC196kNsD0ERHD0n%2F0JEJZAINdiPhRnDW8712P%2FxZJtTwxLdPk8t3ylJVmtkqVqL3eR8O%2BXIkDh51zXZbksaUs1gCJlocFWmP53d0r%2FBiANWs57A%2B%2BjlnBU7BuvUr7EE3jmCSEsahMw9vaoxfE4cwH7a&X-Amz-Signature=0c9a34bec3773de19bb5bfc4378b7519d230fa4acc6e0c38781d0986c03b9d73&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KGXMCFY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIDcaHDqYwon1NhizC0AFR%2F2PlHiEadkJpjPf%2FTD%2FYIkgAiEAlPKYy58huZSOwnM5hT1wyYASRgdGGwM0cWhGsqQ8Z5MqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6FQTlGAUmg3C8K6CrcA4LyGrmcMdUXWMubqnuWcSaaNn9bDbqcHeaPNd1YP3iI%2BA9Bln7Scrhfw0mkjtjGJ8MkcexmXhuKGzZkDBPdAURUw%2FMO1xufuJSseUJSz9m%2FsNw7F1VwHrRwdEXW4x2uJowb5x3LYqmXlKVOeC4Z5W82u%2FJAiW3H188xmCyuEBKju96XphZCSqTw0ntVzyDO0tRVShAe9fi6HJBLTzWIu9SMkayRK%2FZ2UntOKXJq%2B41RolHuzaO5R%2BOQ%2FMKKJoOEtBeTlCzIjha%2FZ6A8p4EHuP4OipJRpZrFfGB9wrBOKzZtSRLVpE9iMt5vxsdOdytbUdPjsm2F8gqTrkHt3nVEF7HL1M3RYvBs9isI6qh9VXLhIDQGJPs8iSD35abUGZa8BApQlPgt0txpQM877PIaw4leu6QTrdPTAgmkXF9tYcvpkvwqXHm4l52H%2Bzifc1qzEAcZGMMi96cvs9NLWZx%2BUNkgfkPVFKiY4Wvo0E4CMZOKPu3SYDrmi8eUZStIi%2FYSfbMBfmCUU52KWM4y7C9R8EUlVcaz5YEaOLxFVEYUn0Jc832HWG3GYEcnuRQZRE01BjG3JwqJWpxJwTCHP1pq0WMcS1H4i2s42KrtIhmjKmsyIBLUZ61KRGUaC1VwMIKg5rwGOqUBleOS90WoW092QnvNeyrufu8nzXvAqiGVova95iIJpVB%2BrevjVNZ4I4uVbL5j9wIdmrpIPC196kNsD0ERHD0n%2F0JEJZAINdiPhRnDW8712P%2FxZJtTwxLdPk8t3ylJVmtkqVqL3eR8O%2BXIkDh51zXZbksaUs1gCJlocFWmP53d0r%2FBiANWs57A%2B%2BjlnBU7BuvUr7EE3jmCSEsahMw9vaoxfE4cwH7a&X-Amz-Signature=0140861fc6c562880b464502b492f4ffaba8627732c5eb111b73337c69cc1e29&X-Amz-SignedHeaders=host&x-id=GetObject)
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


