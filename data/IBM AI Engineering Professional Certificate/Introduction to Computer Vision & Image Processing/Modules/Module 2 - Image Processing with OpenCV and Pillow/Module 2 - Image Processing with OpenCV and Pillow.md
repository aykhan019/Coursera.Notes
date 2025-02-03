

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3HTV7OR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBgciTVNy8WbHZc5eCiXwPU0CMUUGcXQEJyMCde%2FdDSQAiB8TLS5NLZFafURWqWuxfqQzJaLy%2Fw9%2B%2Fph%2FPeOvtq9Eyr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM5JT3UuQfVOBa6jZlKtwDneUsTQbNgSGIt6XPSkHktVRVsbD2%2Fj0tisWnyBxXh8bJ0KcgBW4c%2F6slFpsTHxWQahHBipn%2BPCw8k22J4a7m94sXXE9U2MWphP33Be4vvDb%2FAVf2LoygPWXRwVfsmLO5vH6A1WreHmHvR15mjJQsR51pFoV%2FoELqZxWXELbFEfDt8EsUvlpDMd67UTtpC%2BajAYM5ReJqS5rSF4NAxRuBjKEHcuzJYRDGeudPrMq8qMo6cBJGg%2Fs%2BjKDP0DL6ws%2FFZI54P6bEi0%2BzOdun9CJ5h8uqyYiX%2FLmybWs86e6hrqAe%2FJTXGnThtCPrUPErOo0NLZFi8pRkIT7uGJ9CVvwyc0gp2Y4UHYpl0e7g4ajxvZHM4LPpCnc%2FbmPevaxNT%2F%2BHyFHNb7ylLMelyzWUHSJ0%2F8C3BdIUXFqeKRiywHqUMwSf0v%2Bj%2FuSgdiZgRBf8JzOxJ0O5tebMDcuTX27jN8hyfIIHYOubK7jGF9%2F%2B0aG%2BzpxVux7G66Yc22d2qDtX%2FiKXWYbjzRIupBq6qKWYrpGjFF1iDX7YVpp%2BA7Ap%2F6yAuiV39RvK5VHQXyZapcv1pipbGWxOl6B02A5iYjciADfok5VcHfYeh2ZCPt3Ck39rk2yUZ7kEoLrx06fDaGwwtvOBvQY6pgGTbAunRhHtGTRE%2FVW%2BZcL17x4bNVeIiqlz%2BQNhE5aoptwUlsRmx3fFhYCrjr7%2FyIFrv025Bl2yvj0KxEvmuo1nQ8Wwy3ACk0IhZlRlIujLkWpJC3zksig%2FvKOvR4ukG4A%2BXi70SXqPnoKG%2BwKfT3crBPdrHe8H3A3Ol2Lurdeovo6YGwjNap40AN0rZxo52aMod8rHwZCHNs6HLT4o6XoZZxF4zYTM&X-Amz-Signature=96158335985955f361bd5f29ae51ca0817fb394f4af0b61ee9d14e64165530d4&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYRX47BD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FghZB9WkA2GmpHR8wz0vfMhb2MntlhJkDFTaq5r%2FB1AiBTNeDaalaq2UYpNM6k0d%2B5Ip%2BSXj1hlYIMAOnoNY1tNir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMylu23z8JSdVzzMpaKtwDwu07%2FakSk6bi6eHFKLlGxfYZcrNoPYE5d3lkuguG%2Ffi%2BlPupRxNVUyeUtUQ5u73%2BF4056WRgiKg0SGFlK4eaDeOlBEFCN6gUDB3RcKcEwqc3El%2BHaVVDtoLuZZgMFMUZz%2FRQGnuBBTk4wJ7qqUTFgA7eCKdXTa6i58KdNFUheXTl%2FweFJvMWMv4uxZNV7GoKzMJcigzrFyFo%2FJ3nBxR2EKOKAXqBLmI7PRp6a85UQmd75Sg781z%2FBit5mxegHZqDwOkvM%2FpClVEQUpCi0SplnS%2FAObGQFPuduNZMhsGUJal1MzE2kC15FTQoa8cWZeOoC0Oq6bR5EHJW1zu105lkGiM%2B48sONnyDPBzgrW7gY5sOi%2B9G3f55fw1b%2FyrCB9XBkdrTA8sbKKDuOCS85P7U6j%2BzPHQ8YV9RCbdZqkOYafz6Ev6hy6KQUjmhjN46WcsCy7K1pMAOP79%2FmFeun8SYHIRMOQ3mAow%2B%2B1CFYQgCq2GI7%2FJ5B9FZfzT5sZdze%2BAi8Vh%2FjZ1bSlU2Y64bhn5LJcylZQC1ub99VpOdLeoPpCMk8AusTfOkwQFHaOB4Qyes1GKlmZM2fsry3aVbhDt1rWhVPYv935wXpbAqR%2FL9enC33qP5Js1j2gUJMKowtfOBvQY6pgG8ldSxANEXNASGYRjTm7orNT1QayOSys9dawCbDvCmI56Xo8JhhbKKD96aMnOA86I88Aw3zosqXm8XeguQItR%2FVEbcDXE6YuPbGlE6EBzA1rZwNXtdq01e%2FYqvaUrxYQhacptNV0iNBtR7zvnQQc4GoLsBOh26ofhJwFkB22Ek6XVUrNlMr27TBEu5UZLz9zCHbhhPPM4yA3Uo9n5mXvGmjzV9i6Fp&X-Amz-Signature=75f9f45b77da1daf62f8198cd009280da14e8cfa068a509cfd1142e3a8c19faf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYRX47BD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FghZB9WkA2GmpHR8wz0vfMhb2MntlhJkDFTaq5r%2FB1AiBTNeDaalaq2UYpNM6k0d%2B5Ip%2BSXj1hlYIMAOnoNY1tNir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMylu23z8JSdVzzMpaKtwDwu07%2FakSk6bi6eHFKLlGxfYZcrNoPYE5d3lkuguG%2Ffi%2BlPupRxNVUyeUtUQ5u73%2BF4056WRgiKg0SGFlK4eaDeOlBEFCN6gUDB3RcKcEwqc3El%2BHaVVDtoLuZZgMFMUZz%2FRQGnuBBTk4wJ7qqUTFgA7eCKdXTa6i58KdNFUheXTl%2FweFJvMWMv4uxZNV7GoKzMJcigzrFyFo%2FJ3nBxR2EKOKAXqBLmI7PRp6a85UQmd75Sg781z%2FBit5mxegHZqDwOkvM%2FpClVEQUpCi0SplnS%2FAObGQFPuduNZMhsGUJal1MzE2kC15FTQoa8cWZeOoC0Oq6bR5EHJW1zu105lkGiM%2B48sONnyDPBzgrW7gY5sOi%2B9G3f55fw1b%2FyrCB9XBkdrTA8sbKKDuOCS85P7U6j%2BzPHQ8YV9RCbdZqkOYafz6Ev6hy6KQUjmhjN46WcsCy7K1pMAOP79%2FmFeun8SYHIRMOQ3mAow%2B%2B1CFYQgCq2GI7%2FJ5B9FZfzT5sZdze%2BAi8Vh%2FjZ1bSlU2Y64bhn5LJcylZQC1ub99VpOdLeoPpCMk8AusTfOkwQFHaOB4Qyes1GKlmZM2fsry3aVbhDt1rWhVPYv935wXpbAqR%2FL9enC33qP5Js1j2gUJMKowtfOBvQY6pgG8ldSxANEXNASGYRjTm7orNT1QayOSys9dawCbDvCmI56Xo8JhhbKKD96aMnOA86I88Aw3zosqXm8XeguQItR%2FVEbcDXE6YuPbGlE6EBzA1rZwNXtdq01e%2FYqvaUrxYQhacptNV0iNBtR7zvnQQc4GoLsBOh26ofhJwFkB22Ek6XVUrNlMr27TBEu5UZLz9zCHbhhPPM4yA3Uo9n5mXvGmjzV9i6Fp&X-Amz-Signature=74258d5acc657777beb600c797f9adc5c05018f5a4f52aec4bf36de50010015c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYRX47BD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FghZB9WkA2GmpHR8wz0vfMhb2MntlhJkDFTaq5r%2FB1AiBTNeDaalaq2UYpNM6k0d%2B5Ip%2BSXj1hlYIMAOnoNY1tNir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMylu23z8JSdVzzMpaKtwDwu07%2FakSk6bi6eHFKLlGxfYZcrNoPYE5d3lkuguG%2Ffi%2BlPupRxNVUyeUtUQ5u73%2BF4056WRgiKg0SGFlK4eaDeOlBEFCN6gUDB3RcKcEwqc3El%2BHaVVDtoLuZZgMFMUZz%2FRQGnuBBTk4wJ7qqUTFgA7eCKdXTa6i58KdNFUheXTl%2FweFJvMWMv4uxZNV7GoKzMJcigzrFyFo%2FJ3nBxR2EKOKAXqBLmI7PRp6a85UQmd75Sg781z%2FBit5mxegHZqDwOkvM%2FpClVEQUpCi0SplnS%2FAObGQFPuduNZMhsGUJal1MzE2kC15FTQoa8cWZeOoC0Oq6bR5EHJW1zu105lkGiM%2B48sONnyDPBzgrW7gY5sOi%2B9G3f55fw1b%2FyrCB9XBkdrTA8sbKKDuOCS85P7U6j%2BzPHQ8YV9RCbdZqkOYafz6Ev6hy6KQUjmhjN46WcsCy7K1pMAOP79%2FmFeun8SYHIRMOQ3mAow%2B%2B1CFYQgCq2GI7%2FJ5B9FZfzT5sZdze%2BAi8Vh%2FjZ1bSlU2Y64bhn5LJcylZQC1ub99VpOdLeoPpCMk8AusTfOkwQFHaOB4Qyes1GKlmZM2fsry3aVbhDt1rWhVPYv935wXpbAqR%2FL9enC33qP5Js1j2gUJMKowtfOBvQY6pgG8ldSxANEXNASGYRjTm7orNT1QayOSys9dawCbDvCmI56Xo8JhhbKKD96aMnOA86I88Aw3zosqXm8XeguQItR%2FVEbcDXE6YuPbGlE6EBzA1rZwNXtdq01e%2FYqvaUrxYQhacptNV0iNBtR7zvnQQc4GoLsBOh26ofhJwFkB22Ek6XVUrNlMr27TBEu5UZLz9zCHbhhPPM4yA3Uo9n5mXvGmjzV9i6Fp&X-Amz-Signature=55b877084e365d9e99789eea39dd7f3f222cb6390d6bee6db87ef80bf14177dd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYRX47BD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FghZB9WkA2GmpHR8wz0vfMhb2MntlhJkDFTaq5r%2FB1AiBTNeDaalaq2UYpNM6k0d%2B5Ip%2BSXj1hlYIMAOnoNY1tNir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMylu23z8JSdVzzMpaKtwDwu07%2FakSk6bi6eHFKLlGxfYZcrNoPYE5d3lkuguG%2Ffi%2BlPupRxNVUyeUtUQ5u73%2BF4056WRgiKg0SGFlK4eaDeOlBEFCN6gUDB3RcKcEwqc3El%2BHaVVDtoLuZZgMFMUZz%2FRQGnuBBTk4wJ7qqUTFgA7eCKdXTa6i58KdNFUheXTl%2FweFJvMWMv4uxZNV7GoKzMJcigzrFyFo%2FJ3nBxR2EKOKAXqBLmI7PRp6a85UQmd75Sg781z%2FBit5mxegHZqDwOkvM%2FpClVEQUpCi0SplnS%2FAObGQFPuduNZMhsGUJal1MzE2kC15FTQoa8cWZeOoC0Oq6bR5EHJW1zu105lkGiM%2B48sONnyDPBzgrW7gY5sOi%2B9G3f55fw1b%2FyrCB9XBkdrTA8sbKKDuOCS85P7U6j%2BzPHQ8YV9RCbdZqkOYafz6Ev6hy6KQUjmhjN46WcsCy7K1pMAOP79%2FmFeun8SYHIRMOQ3mAow%2B%2B1CFYQgCq2GI7%2FJ5B9FZfzT5sZdze%2BAi8Vh%2FjZ1bSlU2Y64bhn5LJcylZQC1ub99VpOdLeoPpCMk8AusTfOkwQFHaOB4Qyes1GKlmZM2fsry3aVbhDt1rWhVPYv935wXpbAqR%2FL9enC33qP5Js1j2gUJMKowtfOBvQY6pgG8ldSxANEXNASGYRjTm7orNT1QayOSys9dawCbDvCmI56Xo8JhhbKKD96aMnOA86I88Aw3zosqXm8XeguQItR%2FVEbcDXE6YuPbGlE6EBzA1rZwNXtdq01e%2FYqvaUrxYQhacptNV0iNBtR7zvnQQc4GoLsBOh26ofhJwFkB22Ek6XVUrNlMr27TBEu5UZLz9zCHbhhPPM4yA3Uo9n5mXvGmjzV9i6Fp&X-Amz-Signature=789a863cacef931dba2f7faee002cc46663f2bd901155e749efa7b4df6892078&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYRX47BD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FghZB9WkA2GmpHR8wz0vfMhb2MntlhJkDFTaq5r%2FB1AiBTNeDaalaq2UYpNM6k0d%2B5Ip%2BSXj1hlYIMAOnoNY1tNir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMylu23z8JSdVzzMpaKtwDwu07%2FakSk6bi6eHFKLlGxfYZcrNoPYE5d3lkuguG%2Ffi%2BlPupRxNVUyeUtUQ5u73%2BF4056WRgiKg0SGFlK4eaDeOlBEFCN6gUDB3RcKcEwqc3El%2BHaVVDtoLuZZgMFMUZz%2FRQGnuBBTk4wJ7qqUTFgA7eCKdXTa6i58KdNFUheXTl%2FweFJvMWMv4uxZNV7GoKzMJcigzrFyFo%2FJ3nBxR2EKOKAXqBLmI7PRp6a85UQmd75Sg781z%2FBit5mxegHZqDwOkvM%2FpClVEQUpCi0SplnS%2FAObGQFPuduNZMhsGUJal1MzE2kC15FTQoa8cWZeOoC0Oq6bR5EHJW1zu105lkGiM%2B48sONnyDPBzgrW7gY5sOi%2B9G3f55fw1b%2FyrCB9XBkdrTA8sbKKDuOCS85P7U6j%2BzPHQ8YV9RCbdZqkOYafz6Ev6hy6KQUjmhjN46WcsCy7K1pMAOP79%2FmFeun8SYHIRMOQ3mAow%2B%2B1CFYQgCq2GI7%2FJ5B9FZfzT5sZdze%2BAi8Vh%2FjZ1bSlU2Y64bhn5LJcylZQC1ub99VpOdLeoPpCMk8AusTfOkwQFHaOB4Qyes1GKlmZM2fsry3aVbhDt1rWhVPYv935wXpbAqR%2FL9enC33qP5Js1j2gUJMKowtfOBvQY6pgG8ldSxANEXNASGYRjTm7orNT1QayOSys9dawCbDvCmI56Xo8JhhbKKD96aMnOA86I88Aw3zosqXm8XeguQItR%2FVEbcDXE6YuPbGlE6EBzA1rZwNXtdq01e%2FYqvaUrxYQhacptNV0iNBtR7zvnQQc4GoLsBOh26ofhJwFkB22Ek6XVUrNlMr27TBEu5UZLz9zCHbhhPPM4yA3Uo9n5mXvGmjzV9i6Fp&X-Amz-Signature=74d126a01ebb9928f0ca90cc5f67a1e4ec964c67e0e8b1cc88d12f4434c8bd73&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3HTV7OR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBgciTVNy8WbHZc5eCiXwPU0CMUUGcXQEJyMCde%2FdDSQAiB8TLS5NLZFafURWqWuxfqQzJaLy%2Fw9%2B%2Fph%2FPeOvtq9Eyr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM5JT3UuQfVOBa6jZlKtwDneUsTQbNgSGIt6XPSkHktVRVsbD2%2Fj0tisWnyBxXh8bJ0KcgBW4c%2F6slFpsTHxWQahHBipn%2BPCw8k22J4a7m94sXXE9U2MWphP33Be4vvDb%2FAVf2LoygPWXRwVfsmLO5vH6A1WreHmHvR15mjJQsR51pFoV%2FoELqZxWXELbFEfDt8EsUvlpDMd67UTtpC%2BajAYM5ReJqS5rSF4NAxRuBjKEHcuzJYRDGeudPrMq8qMo6cBJGg%2Fs%2BjKDP0DL6ws%2FFZI54P6bEi0%2BzOdun9CJ5h8uqyYiX%2FLmybWs86e6hrqAe%2FJTXGnThtCPrUPErOo0NLZFi8pRkIT7uGJ9CVvwyc0gp2Y4UHYpl0e7g4ajxvZHM4LPpCnc%2FbmPevaxNT%2F%2BHyFHNb7ylLMelyzWUHSJ0%2F8C3BdIUXFqeKRiywHqUMwSf0v%2Bj%2FuSgdiZgRBf8JzOxJ0O5tebMDcuTX27jN8hyfIIHYOubK7jGF9%2F%2B0aG%2BzpxVux7G66Yc22d2qDtX%2FiKXWYbjzRIupBq6qKWYrpGjFF1iDX7YVpp%2BA7Ap%2F6yAuiV39RvK5VHQXyZapcv1pipbGWxOl6B02A5iYjciADfok5VcHfYeh2ZCPt3Ck39rk2yUZ7kEoLrx06fDaGwwtvOBvQY6pgGTbAunRhHtGTRE%2FVW%2BZcL17x4bNVeIiqlz%2BQNhE5aoptwUlsRmx3fFhYCrjr7%2FyIFrv025Bl2yvj0KxEvmuo1nQ8Wwy3ACk0IhZlRlIujLkWpJC3zksig%2FvKOvR4ukG4A%2BXi70SXqPnoKG%2BwKfT3crBPdrHe8H3A3Ol2Lurdeovo6YGwjNap40AN0rZxo52aMod8rHwZCHNs6HLT4o6XoZZxF4zYTM&X-Amz-Signature=34489a8ad368b12563f2856ac27b5eef89be68ae22efa7a2e9ecced6bee11f34&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3HTV7OR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBgciTVNy8WbHZc5eCiXwPU0CMUUGcXQEJyMCde%2FdDSQAiB8TLS5NLZFafURWqWuxfqQzJaLy%2Fw9%2B%2Fph%2FPeOvtq9Eyr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM5JT3UuQfVOBa6jZlKtwDneUsTQbNgSGIt6XPSkHktVRVsbD2%2Fj0tisWnyBxXh8bJ0KcgBW4c%2F6slFpsTHxWQahHBipn%2BPCw8k22J4a7m94sXXE9U2MWphP33Be4vvDb%2FAVf2LoygPWXRwVfsmLO5vH6A1WreHmHvR15mjJQsR51pFoV%2FoELqZxWXELbFEfDt8EsUvlpDMd67UTtpC%2BajAYM5ReJqS5rSF4NAxRuBjKEHcuzJYRDGeudPrMq8qMo6cBJGg%2Fs%2BjKDP0DL6ws%2FFZI54P6bEi0%2BzOdun9CJ5h8uqyYiX%2FLmybWs86e6hrqAe%2FJTXGnThtCPrUPErOo0NLZFi8pRkIT7uGJ9CVvwyc0gp2Y4UHYpl0e7g4ajxvZHM4LPpCnc%2FbmPevaxNT%2F%2BHyFHNb7ylLMelyzWUHSJ0%2F8C3BdIUXFqeKRiywHqUMwSf0v%2Bj%2FuSgdiZgRBf8JzOxJ0O5tebMDcuTX27jN8hyfIIHYOubK7jGF9%2F%2B0aG%2BzpxVux7G66Yc22d2qDtX%2FiKXWYbjzRIupBq6qKWYrpGjFF1iDX7YVpp%2BA7Ap%2F6yAuiV39RvK5VHQXyZapcv1pipbGWxOl6B02A5iYjciADfok5VcHfYeh2ZCPt3Ck39rk2yUZ7kEoLrx06fDaGwwtvOBvQY6pgGTbAunRhHtGTRE%2FVW%2BZcL17x4bNVeIiqlz%2BQNhE5aoptwUlsRmx3fFhYCrjr7%2FyIFrv025Bl2yvj0KxEvmuo1nQ8Wwy3ACk0IhZlRlIujLkWpJC3zksig%2FvKOvR4ukG4A%2BXi70SXqPnoKG%2BwKfT3crBPdrHe8H3A3Ol2Lurdeovo6YGwjNap40AN0rZxo52aMod8rHwZCHNs6HLT4o6XoZZxF4zYTM&X-Amz-Signature=c331fafa846dd631b21c987f5f7b089e7d24dfe35c88691aa767ae0008a7d739&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3HTV7OR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBgciTVNy8WbHZc5eCiXwPU0CMUUGcXQEJyMCde%2FdDSQAiB8TLS5NLZFafURWqWuxfqQzJaLy%2Fw9%2B%2Fph%2FPeOvtq9Eyr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM5JT3UuQfVOBa6jZlKtwDneUsTQbNgSGIt6XPSkHktVRVsbD2%2Fj0tisWnyBxXh8bJ0KcgBW4c%2F6slFpsTHxWQahHBipn%2BPCw8k22J4a7m94sXXE9U2MWphP33Be4vvDb%2FAVf2LoygPWXRwVfsmLO5vH6A1WreHmHvR15mjJQsR51pFoV%2FoELqZxWXELbFEfDt8EsUvlpDMd67UTtpC%2BajAYM5ReJqS5rSF4NAxRuBjKEHcuzJYRDGeudPrMq8qMo6cBJGg%2Fs%2BjKDP0DL6ws%2FFZI54P6bEi0%2BzOdun9CJ5h8uqyYiX%2FLmybWs86e6hrqAe%2FJTXGnThtCPrUPErOo0NLZFi8pRkIT7uGJ9CVvwyc0gp2Y4UHYpl0e7g4ajxvZHM4LPpCnc%2FbmPevaxNT%2F%2BHyFHNb7ylLMelyzWUHSJ0%2F8C3BdIUXFqeKRiywHqUMwSf0v%2Bj%2FuSgdiZgRBf8JzOxJ0O5tebMDcuTX27jN8hyfIIHYOubK7jGF9%2F%2B0aG%2BzpxVux7G66Yc22d2qDtX%2FiKXWYbjzRIupBq6qKWYrpGjFF1iDX7YVpp%2BA7Ap%2F6yAuiV39RvK5VHQXyZapcv1pipbGWxOl6B02A5iYjciADfok5VcHfYeh2ZCPt3Ck39rk2yUZ7kEoLrx06fDaGwwtvOBvQY6pgGTbAunRhHtGTRE%2FVW%2BZcL17x4bNVeIiqlz%2BQNhE5aoptwUlsRmx3fFhYCrjr7%2FyIFrv025Bl2yvj0KxEvmuo1nQ8Wwy3ACk0IhZlRlIujLkWpJC3zksig%2FvKOvR4ukG4A%2BXi70SXqPnoKG%2BwKfT3crBPdrHe8H3A3Ol2Lurdeovo6YGwjNap40AN0rZxo52aMod8rHwZCHNs6HLT4o6XoZZxF4zYTM&X-Amz-Signature=d67892050439aef9890580bbe125490b13f5a8f57a4c4029cdbf5c3ee03c9640&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3HTV7OR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBgciTVNy8WbHZc5eCiXwPU0CMUUGcXQEJyMCde%2FdDSQAiB8TLS5NLZFafURWqWuxfqQzJaLy%2Fw9%2B%2Fph%2FPeOvtq9Eyr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM5JT3UuQfVOBa6jZlKtwDneUsTQbNgSGIt6XPSkHktVRVsbD2%2Fj0tisWnyBxXh8bJ0KcgBW4c%2F6slFpsTHxWQahHBipn%2BPCw8k22J4a7m94sXXE9U2MWphP33Be4vvDb%2FAVf2LoygPWXRwVfsmLO5vH6A1WreHmHvR15mjJQsR51pFoV%2FoELqZxWXELbFEfDt8EsUvlpDMd67UTtpC%2BajAYM5ReJqS5rSF4NAxRuBjKEHcuzJYRDGeudPrMq8qMo6cBJGg%2Fs%2BjKDP0DL6ws%2FFZI54P6bEi0%2BzOdun9CJ5h8uqyYiX%2FLmybWs86e6hrqAe%2FJTXGnThtCPrUPErOo0NLZFi8pRkIT7uGJ9CVvwyc0gp2Y4UHYpl0e7g4ajxvZHM4LPpCnc%2FbmPevaxNT%2F%2BHyFHNb7ylLMelyzWUHSJ0%2F8C3BdIUXFqeKRiywHqUMwSf0v%2Bj%2FuSgdiZgRBf8JzOxJ0O5tebMDcuTX27jN8hyfIIHYOubK7jGF9%2F%2B0aG%2BzpxVux7G66Yc22d2qDtX%2FiKXWYbjzRIupBq6qKWYrpGjFF1iDX7YVpp%2BA7Ap%2F6yAuiV39RvK5VHQXyZapcv1pipbGWxOl6B02A5iYjciADfok5VcHfYeh2ZCPt3Ck39rk2yUZ7kEoLrx06fDaGwwtvOBvQY6pgGTbAunRhHtGTRE%2FVW%2BZcL17x4bNVeIiqlz%2BQNhE5aoptwUlsRmx3fFhYCrjr7%2FyIFrv025Bl2yvj0KxEvmuo1nQ8Wwy3ACk0IhZlRlIujLkWpJC3zksig%2FvKOvR4ukG4A%2BXi70SXqPnoKG%2BwKfT3crBPdrHe8H3A3Ol2Lurdeovo6YGwjNap40AN0rZxo52aMod8rHwZCHNs6HLT4o6XoZZxF4zYTM&X-Amz-Signature=7a76ff5c247d0a3a7b6715f278ef3ea25e454a9ad3f6cb74def8fc03c761ad20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3HTV7OR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBgciTVNy8WbHZc5eCiXwPU0CMUUGcXQEJyMCde%2FdDSQAiB8TLS5NLZFafURWqWuxfqQzJaLy%2Fw9%2B%2Fph%2FPeOvtq9Eyr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM5JT3UuQfVOBa6jZlKtwDneUsTQbNgSGIt6XPSkHktVRVsbD2%2Fj0tisWnyBxXh8bJ0KcgBW4c%2F6slFpsTHxWQahHBipn%2BPCw8k22J4a7m94sXXE9U2MWphP33Be4vvDb%2FAVf2LoygPWXRwVfsmLO5vH6A1WreHmHvR15mjJQsR51pFoV%2FoELqZxWXELbFEfDt8EsUvlpDMd67UTtpC%2BajAYM5ReJqS5rSF4NAxRuBjKEHcuzJYRDGeudPrMq8qMo6cBJGg%2Fs%2BjKDP0DL6ws%2FFZI54P6bEi0%2BzOdun9CJ5h8uqyYiX%2FLmybWs86e6hrqAe%2FJTXGnThtCPrUPErOo0NLZFi8pRkIT7uGJ9CVvwyc0gp2Y4UHYpl0e7g4ajxvZHM4LPpCnc%2FbmPevaxNT%2F%2BHyFHNb7ylLMelyzWUHSJ0%2F8C3BdIUXFqeKRiywHqUMwSf0v%2Bj%2FuSgdiZgRBf8JzOxJ0O5tebMDcuTX27jN8hyfIIHYOubK7jGF9%2F%2B0aG%2BzpxVux7G66Yc22d2qDtX%2FiKXWYbjzRIupBq6qKWYrpGjFF1iDX7YVpp%2BA7Ap%2F6yAuiV39RvK5VHQXyZapcv1pipbGWxOl6B02A5iYjciADfok5VcHfYeh2ZCPt3Ck39rk2yUZ7kEoLrx06fDaGwwtvOBvQY6pgGTbAunRhHtGTRE%2FVW%2BZcL17x4bNVeIiqlz%2BQNhE5aoptwUlsRmx3fFhYCrjr7%2FyIFrv025Bl2yvj0KxEvmuo1nQ8Wwy3ACk0IhZlRlIujLkWpJC3zksig%2FvKOvR4ukG4A%2BXi70SXqPnoKG%2BwKfT3crBPdrHe8H3A3Ol2Lurdeovo6YGwjNap40AN0rZxo52aMod8rHwZCHNs6HLT4o6XoZZxF4zYTM&X-Amz-Signature=f8065118e314851c33d2807f8b7cb6683d6794e3a00e550af4d34ea8e20924c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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


