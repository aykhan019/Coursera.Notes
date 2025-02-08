

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6O2K4OP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQCrjynoUuOaI4DU%2B0lb8j9KO2o4vNZaFHXpXa%2BZz7idIAIgdo4D9qoVG1EjyXHNx5E%2Bsi8Bto7S3ZkEt1fA9Se93DAqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKhSNM7ctIYKwfXgnSrcA90JIqjT4A1aIqOuZxfeZ58l6VfLiZkleKbB1wvDMs08kylqT9o%2FqYxSBbEKjEVKamKb4ynRyCFdJxxwp0ik3mN3n%2BWCLtzsJXpSdLgOoOkFkebLtucWH2k%2FUdfOFxYdNfxII9rSxjlbNHva%2BEf2Ydu3WoyBS40JhedF6SZoNZ1L50izA4wHfVMYf%2FVN8qy1LjBIEhwZSNftgOIrrxz%2BvZLLBu9Oc%2FWPHKKejUJ7kX0vmZEWxJoePdD%2FtqlhVOhrZ9rtpamAi91Rv60p8XXYsXisQ9WP8uCn6P9Aefk0UutudZ1XeKUaSI5silAvINceRoTd6hjGer21YtngqSpYqzlsMrjPfF7hf3E6jSkPptVEgFuhW%2FMHUYD7iPLZLWsObDudlyVEWEhX4z3%2FAD6J7TYxzvH5FZoh90EuO1Ba3qcZ86BW%2BkJALn2OtpDg8XrCDMyT6%2FVFqoCLIiekb4NueWLkn3GLOv00sdIxY0rsFihs20vjv0witnemzLxwCAFJmoFfS%2BxulBcAAiIjqb4%2B%2BrF2kuDsfPItMXmHG%2FWtlnNlgb67GEhDfxG2VpFC2mxqwd3fdTQ3KpaXq2SuhSnWXBgCcMeID%2FkVxu5I3ftr83yEAHlo%2BA26u%2Bm9ACGXMPLUm70GOqUBG9thd9eI9DI4%2BQvSgajUerWnKnvyEmljsP47wriuXCddyp0vaU45V%2F4%2BzGNAW4mnc%2Byp4V8Toek34tZ14JyV1tva3Y7UXk9U%2B1rJjHkKcEoZojwDfytuhdEFS8zsq78EnYFswh1GdCet0oL%2Bf83srqAh4JQJ0w3xc1HHacYY5GunL015XgFJIMj%2FEy32ietK%2BP4tNaD8Aq1OSq3hU%2FMXl5h%2BV5S%2B&X-Amz-Signature=2cab1d8e9ec0854307053472b17667ce2c78d10eb251cd795ea10237b2fe3243&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CTYD6BN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIARZXQU43c5Wgxjx8TwDYVCJVTstbvbsFXrE7M7xSRReAiB8KRdhDHnXh0e2DMlK%2BCaUwv6L30XFOTEvBm6mXggIkiqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMm5%2FHJEVcjlO8hDomKtwDC9bX7Wujo6T4wFUF8x5lFYbuxCFf92DQ1ZYwxLVMeYQQs47ZW7sGXecmjmL8oh6wzDQA%2FUKK9MafHllgY7p7ZJREvGeJm0gISpE0NSyB%2BIXJUluEnzQyvDQwSG6zBGpAm8pDxWWOpzOaOdJtRCsejbV7IXWwxKQwkaOKG1Rc6Xe2EbHhsFDqGFlFOgbBGqPZGExQ%2BSpOOMZw9Q%2Fq4SIXeh0hxCtLh3gwVerd2n02fkitukughQmonTN54otDBy5LWMuQeyOVB1CNOT0G5HhjShJO1bQSq4SGzgWm6PBcYs2MDkCiJP1Uyppfbx5P6suAQAgMulPPkQoc1eFmuYwjf8Jvo8x%2Bn1dI%2FR0qbytKmD4Ninw883D4lHbYVSPmf7jktF3hVb0c0nmR08LVk2s6A0HAwZxf4UKlNiOHN8iSZa5o%2BI%2FH45MH3QRTADqGEk2PF0DGA%2FAud5NfpallVjKGmKAIB8SJjqZRYJ0evVH1Pb0Q%2BOR5aEJSHsOy7A%2BP6oGAbObnwlt5%2BbrXFySjPhGtQ3HLWKIseRaRoMkW3sWUQKvDCxvNSHF0stuYU9saYFgAiIUnylIFzNtXmG4jKNrxu%2BwQpUCQtd6a8lZ2nnD2eMIPRzHViihfpxIq6eEwmtSbvQY6pgH9MethzklSrrQZ4wRKaiObXZQKpeESCI9JJvpDFQv984zMd5bW8Feq%2BHAz1i0Eu0SItbgMujTtRYGP4ebPOhpQsjHV1Mr9EwpzeKqcTJh0Ul7hDNuXNaArOAqfvX8gIQuA9c2jlHPf2IMNQz4Ms%2BEZt9VRNXcpbd9x4y2kbAkUnIyc9NmkoPTypgpWFamhNmZh2w4M3dVMsW68r93w62v32lHbpXzf&X-Amz-Signature=088d372413d341c4c5de32e7f141bb6a8f7ee9702c00aecd1bae2599b82a6076&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CTYD6BN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIARZXQU43c5Wgxjx8TwDYVCJVTstbvbsFXrE7M7xSRReAiB8KRdhDHnXh0e2DMlK%2BCaUwv6L30XFOTEvBm6mXggIkiqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMm5%2FHJEVcjlO8hDomKtwDC9bX7Wujo6T4wFUF8x5lFYbuxCFf92DQ1ZYwxLVMeYQQs47ZW7sGXecmjmL8oh6wzDQA%2FUKK9MafHllgY7p7ZJREvGeJm0gISpE0NSyB%2BIXJUluEnzQyvDQwSG6zBGpAm8pDxWWOpzOaOdJtRCsejbV7IXWwxKQwkaOKG1Rc6Xe2EbHhsFDqGFlFOgbBGqPZGExQ%2BSpOOMZw9Q%2Fq4SIXeh0hxCtLh3gwVerd2n02fkitukughQmonTN54otDBy5LWMuQeyOVB1CNOT0G5HhjShJO1bQSq4SGzgWm6PBcYs2MDkCiJP1Uyppfbx5P6suAQAgMulPPkQoc1eFmuYwjf8Jvo8x%2Bn1dI%2FR0qbytKmD4Ninw883D4lHbYVSPmf7jktF3hVb0c0nmR08LVk2s6A0HAwZxf4UKlNiOHN8iSZa5o%2BI%2FH45MH3QRTADqGEk2PF0DGA%2FAud5NfpallVjKGmKAIB8SJjqZRYJ0evVH1Pb0Q%2BOR5aEJSHsOy7A%2BP6oGAbObnwlt5%2BbrXFySjPhGtQ3HLWKIseRaRoMkW3sWUQKvDCxvNSHF0stuYU9saYFgAiIUnylIFzNtXmG4jKNrxu%2BwQpUCQtd6a8lZ2nnD2eMIPRzHViihfpxIq6eEwmtSbvQY6pgH9MethzklSrrQZ4wRKaiObXZQKpeESCI9JJvpDFQv984zMd5bW8Feq%2BHAz1i0Eu0SItbgMujTtRYGP4ebPOhpQsjHV1Mr9EwpzeKqcTJh0Ul7hDNuXNaArOAqfvX8gIQuA9c2jlHPf2IMNQz4Ms%2BEZt9VRNXcpbd9x4y2kbAkUnIyc9NmkoPTypgpWFamhNmZh2w4M3dVMsW68r93w62v32lHbpXzf&X-Amz-Signature=58d2903ab2417bb7b5468e9fc01b426f8beb32bc2286cac22b4ebe452d95d21b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CTYD6BN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIARZXQU43c5Wgxjx8TwDYVCJVTstbvbsFXrE7M7xSRReAiB8KRdhDHnXh0e2DMlK%2BCaUwv6L30XFOTEvBm6mXggIkiqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMm5%2FHJEVcjlO8hDomKtwDC9bX7Wujo6T4wFUF8x5lFYbuxCFf92DQ1ZYwxLVMeYQQs47ZW7sGXecmjmL8oh6wzDQA%2FUKK9MafHllgY7p7ZJREvGeJm0gISpE0NSyB%2BIXJUluEnzQyvDQwSG6zBGpAm8pDxWWOpzOaOdJtRCsejbV7IXWwxKQwkaOKG1Rc6Xe2EbHhsFDqGFlFOgbBGqPZGExQ%2BSpOOMZw9Q%2Fq4SIXeh0hxCtLh3gwVerd2n02fkitukughQmonTN54otDBy5LWMuQeyOVB1CNOT0G5HhjShJO1bQSq4SGzgWm6PBcYs2MDkCiJP1Uyppfbx5P6suAQAgMulPPkQoc1eFmuYwjf8Jvo8x%2Bn1dI%2FR0qbytKmD4Ninw883D4lHbYVSPmf7jktF3hVb0c0nmR08LVk2s6A0HAwZxf4UKlNiOHN8iSZa5o%2BI%2FH45MH3QRTADqGEk2PF0DGA%2FAud5NfpallVjKGmKAIB8SJjqZRYJ0evVH1Pb0Q%2BOR5aEJSHsOy7A%2BP6oGAbObnwlt5%2BbrXFySjPhGtQ3HLWKIseRaRoMkW3sWUQKvDCxvNSHF0stuYU9saYFgAiIUnylIFzNtXmG4jKNrxu%2BwQpUCQtd6a8lZ2nnD2eMIPRzHViihfpxIq6eEwmtSbvQY6pgH9MethzklSrrQZ4wRKaiObXZQKpeESCI9JJvpDFQv984zMd5bW8Feq%2BHAz1i0Eu0SItbgMujTtRYGP4ebPOhpQsjHV1Mr9EwpzeKqcTJh0Ul7hDNuXNaArOAqfvX8gIQuA9c2jlHPf2IMNQz4Ms%2BEZt9VRNXcpbd9x4y2kbAkUnIyc9NmkoPTypgpWFamhNmZh2w4M3dVMsW68r93w62v32lHbpXzf&X-Amz-Signature=68478caf887f6c196ebf6f28f89e0b2fe65ab567eed92062d6d32978461154b7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CTYD6BN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIARZXQU43c5Wgxjx8TwDYVCJVTstbvbsFXrE7M7xSRReAiB8KRdhDHnXh0e2DMlK%2BCaUwv6L30XFOTEvBm6mXggIkiqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMm5%2FHJEVcjlO8hDomKtwDC9bX7Wujo6T4wFUF8x5lFYbuxCFf92DQ1ZYwxLVMeYQQs47ZW7sGXecmjmL8oh6wzDQA%2FUKK9MafHllgY7p7ZJREvGeJm0gISpE0NSyB%2BIXJUluEnzQyvDQwSG6zBGpAm8pDxWWOpzOaOdJtRCsejbV7IXWwxKQwkaOKG1Rc6Xe2EbHhsFDqGFlFOgbBGqPZGExQ%2BSpOOMZw9Q%2Fq4SIXeh0hxCtLh3gwVerd2n02fkitukughQmonTN54otDBy5LWMuQeyOVB1CNOT0G5HhjShJO1bQSq4SGzgWm6PBcYs2MDkCiJP1Uyppfbx5P6suAQAgMulPPkQoc1eFmuYwjf8Jvo8x%2Bn1dI%2FR0qbytKmD4Ninw883D4lHbYVSPmf7jktF3hVb0c0nmR08LVk2s6A0HAwZxf4UKlNiOHN8iSZa5o%2BI%2FH45MH3QRTADqGEk2PF0DGA%2FAud5NfpallVjKGmKAIB8SJjqZRYJ0evVH1Pb0Q%2BOR5aEJSHsOy7A%2BP6oGAbObnwlt5%2BbrXFySjPhGtQ3HLWKIseRaRoMkW3sWUQKvDCxvNSHF0stuYU9saYFgAiIUnylIFzNtXmG4jKNrxu%2BwQpUCQtd6a8lZ2nnD2eMIPRzHViihfpxIq6eEwmtSbvQY6pgH9MethzklSrrQZ4wRKaiObXZQKpeESCI9JJvpDFQv984zMd5bW8Feq%2BHAz1i0Eu0SItbgMujTtRYGP4ebPOhpQsjHV1Mr9EwpzeKqcTJh0Ul7hDNuXNaArOAqfvX8gIQuA9c2jlHPf2IMNQz4Ms%2BEZt9VRNXcpbd9x4y2kbAkUnIyc9NmkoPTypgpWFamhNmZh2w4M3dVMsW68r93w62v32lHbpXzf&X-Amz-Signature=bc7687b1bf4635cff46a8c1ac9958c10841d4f13b7cc353b0ed0ce41f341b079&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CTYD6BN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIARZXQU43c5Wgxjx8TwDYVCJVTstbvbsFXrE7M7xSRReAiB8KRdhDHnXh0e2DMlK%2BCaUwv6L30XFOTEvBm6mXggIkiqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMm5%2FHJEVcjlO8hDomKtwDC9bX7Wujo6T4wFUF8x5lFYbuxCFf92DQ1ZYwxLVMeYQQs47ZW7sGXecmjmL8oh6wzDQA%2FUKK9MafHllgY7p7ZJREvGeJm0gISpE0NSyB%2BIXJUluEnzQyvDQwSG6zBGpAm8pDxWWOpzOaOdJtRCsejbV7IXWwxKQwkaOKG1Rc6Xe2EbHhsFDqGFlFOgbBGqPZGExQ%2BSpOOMZw9Q%2Fq4SIXeh0hxCtLh3gwVerd2n02fkitukughQmonTN54otDBy5LWMuQeyOVB1CNOT0G5HhjShJO1bQSq4SGzgWm6PBcYs2MDkCiJP1Uyppfbx5P6suAQAgMulPPkQoc1eFmuYwjf8Jvo8x%2Bn1dI%2FR0qbytKmD4Ninw883D4lHbYVSPmf7jktF3hVb0c0nmR08LVk2s6A0HAwZxf4UKlNiOHN8iSZa5o%2BI%2FH45MH3QRTADqGEk2PF0DGA%2FAud5NfpallVjKGmKAIB8SJjqZRYJ0evVH1Pb0Q%2BOR5aEJSHsOy7A%2BP6oGAbObnwlt5%2BbrXFySjPhGtQ3HLWKIseRaRoMkW3sWUQKvDCxvNSHF0stuYU9saYFgAiIUnylIFzNtXmG4jKNrxu%2BwQpUCQtd6a8lZ2nnD2eMIPRzHViihfpxIq6eEwmtSbvQY6pgH9MethzklSrrQZ4wRKaiObXZQKpeESCI9JJvpDFQv984zMd5bW8Feq%2BHAz1i0Eu0SItbgMujTtRYGP4ebPOhpQsjHV1Mr9EwpzeKqcTJh0Ul7hDNuXNaArOAqfvX8gIQuA9c2jlHPf2IMNQz4Ms%2BEZt9VRNXcpbd9x4y2kbAkUnIyc9NmkoPTypgpWFamhNmZh2w4M3dVMsW68r93w62v32lHbpXzf&X-Amz-Signature=5215b897e5f68b9f5c2c9aa9f4fc02db17d31f8d799ae50061e8a183e88855fa&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6O2K4OP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQCrjynoUuOaI4DU%2B0lb8j9KO2o4vNZaFHXpXa%2BZz7idIAIgdo4D9qoVG1EjyXHNx5E%2Bsi8Bto7S3ZkEt1fA9Se93DAqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKhSNM7ctIYKwfXgnSrcA90JIqjT4A1aIqOuZxfeZ58l6VfLiZkleKbB1wvDMs08kylqT9o%2FqYxSBbEKjEVKamKb4ynRyCFdJxxwp0ik3mN3n%2BWCLtzsJXpSdLgOoOkFkebLtucWH2k%2FUdfOFxYdNfxII9rSxjlbNHva%2BEf2Ydu3WoyBS40JhedF6SZoNZ1L50izA4wHfVMYf%2FVN8qy1LjBIEhwZSNftgOIrrxz%2BvZLLBu9Oc%2FWPHKKejUJ7kX0vmZEWxJoePdD%2FtqlhVOhrZ9rtpamAi91Rv60p8XXYsXisQ9WP8uCn6P9Aefk0UutudZ1XeKUaSI5silAvINceRoTd6hjGer21YtngqSpYqzlsMrjPfF7hf3E6jSkPptVEgFuhW%2FMHUYD7iPLZLWsObDudlyVEWEhX4z3%2FAD6J7TYxzvH5FZoh90EuO1Ba3qcZ86BW%2BkJALn2OtpDg8XrCDMyT6%2FVFqoCLIiekb4NueWLkn3GLOv00sdIxY0rsFihs20vjv0witnemzLxwCAFJmoFfS%2BxulBcAAiIjqb4%2B%2BrF2kuDsfPItMXmHG%2FWtlnNlgb67GEhDfxG2VpFC2mxqwd3fdTQ3KpaXq2SuhSnWXBgCcMeID%2FkVxu5I3ftr83yEAHlo%2BA26u%2Bm9ACGXMPLUm70GOqUBG9thd9eI9DI4%2BQvSgajUerWnKnvyEmljsP47wriuXCddyp0vaU45V%2F4%2BzGNAW4mnc%2Byp4V8Toek34tZ14JyV1tva3Y7UXk9U%2B1rJjHkKcEoZojwDfytuhdEFS8zsq78EnYFswh1GdCet0oL%2Bf83srqAh4JQJ0w3xc1HHacYY5GunL015XgFJIMj%2FEy32ietK%2BP4tNaD8Aq1OSq3hU%2FMXl5h%2BV5S%2B&X-Amz-Signature=1826c5728c52efb29b7f76c709be6e78de750fba4484326e530acfa5333b7827&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6O2K4OP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQCrjynoUuOaI4DU%2B0lb8j9KO2o4vNZaFHXpXa%2BZz7idIAIgdo4D9qoVG1EjyXHNx5E%2Bsi8Bto7S3ZkEt1fA9Se93DAqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKhSNM7ctIYKwfXgnSrcA90JIqjT4A1aIqOuZxfeZ58l6VfLiZkleKbB1wvDMs08kylqT9o%2FqYxSBbEKjEVKamKb4ynRyCFdJxxwp0ik3mN3n%2BWCLtzsJXpSdLgOoOkFkebLtucWH2k%2FUdfOFxYdNfxII9rSxjlbNHva%2BEf2Ydu3WoyBS40JhedF6SZoNZ1L50izA4wHfVMYf%2FVN8qy1LjBIEhwZSNftgOIrrxz%2BvZLLBu9Oc%2FWPHKKejUJ7kX0vmZEWxJoePdD%2FtqlhVOhrZ9rtpamAi91Rv60p8XXYsXisQ9WP8uCn6P9Aefk0UutudZ1XeKUaSI5silAvINceRoTd6hjGer21YtngqSpYqzlsMrjPfF7hf3E6jSkPptVEgFuhW%2FMHUYD7iPLZLWsObDudlyVEWEhX4z3%2FAD6J7TYxzvH5FZoh90EuO1Ba3qcZ86BW%2BkJALn2OtpDg8XrCDMyT6%2FVFqoCLIiekb4NueWLkn3GLOv00sdIxY0rsFihs20vjv0witnemzLxwCAFJmoFfS%2BxulBcAAiIjqb4%2B%2BrF2kuDsfPItMXmHG%2FWtlnNlgb67GEhDfxG2VpFC2mxqwd3fdTQ3KpaXq2SuhSnWXBgCcMeID%2FkVxu5I3ftr83yEAHlo%2BA26u%2Bm9ACGXMPLUm70GOqUBG9thd9eI9DI4%2BQvSgajUerWnKnvyEmljsP47wriuXCddyp0vaU45V%2F4%2BzGNAW4mnc%2Byp4V8Toek34tZ14JyV1tva3Y7UXk9U%2B1rJjHkKcEoZojwDfytuhdEFS8zsq78EnYFswh1GdCet0oL%2Bf83srqAh4JQJ0w3xc1HHacYY5GunL015XgFJIMj%2FEy32ietK%2BP4tNaD8Aq1OSq3hU%2FMXl5h%2BV5S%2B&X-Amz-Signature=19bfba3485cf49adef8a5b9c973dc4574f96b4097110e9a8d555fb5ab911caa7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6O2K4OP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQCrjynoUuOaI4DU%2B0lb8j9KO2o4vNZaFHXpXa%2BZz7idIAIgdo4D9qoVG1EjyXHNx5E%2Bsi8Bto7S3ZkEt1fA9Se93DAqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKhSNM7ctIYKwfXgnSrcA90JIqjT4A1aIqOuZxfeZ58l6VfLiZkleKbB1wvDMs08kylqT9o%2FqYxSBbEKjEVKamKb4ynRyCFdJxxwp0ik3mN3n%2BWCLtzsJXpSdLgOoOkFkebLtucWH2k%2FUdfOFxYdNfxII9rSxjlbNHva%2BEf2Ydu3WoyBS40JhedF6SZoNZ1L50izA4wHfVMYf%2FVN8qy1LjBIEhwZSNftgOIrrxz%2BvZLLBu9Oc%2FWPHKKejUJ7kX0vmZEWxJoePdD%2FtqlhVOhrZ9rtpamAi91Rv60p8XXYsXisQ9WP8uCn6P9Aefk0UutudZ1XeKUaSI5silAvINceRoTd6hjGer21YtngqSpYqzlsMrjPfF7hf3E6jSkPptVEgFuhW%2FMHUYD7iPLZLWsObDudlyVEWEhX4z3%2FAD6J7TYxzvH5FZoh90EuO1Ba3qcZ86BW%2BkJALn2OtpDg8XrCDMyT6%2FVFqoCLIiekb4NueWLkn3GLOv00sdIxY0rsFihs20vjv0witnemzLxwCAFJmoFfS%2BxulBcAAiIjqb4%2B%2BrF2kuDsfPItMXmHG%2FWtlnNlgb67GEhDfxG2VpFC2mxqwd3fdTQ3KpaXq2SuhSnWXBgCcMeID%2FkVxu5I3ftr83yEAHlo%2BA26u%2Bm9ACGXMPLUm70GOqUBG9thd9eI9DI4%2BQvSgajUerWnKnvyEmljsP47wriuXCddyp0vaU45V%2F4%2BzGNAW4mnc%2Byp4V8Toek34tZ14JyV1tva3Y7UXk9U%2B1rJjHkKcEoZojwDfytuhdEFS8zsq78EnYFswh1GdCet0oL%2Bf83srqAh4JQJ0w3xc1HHacYY5GunL015XgFJIMj%2FEy32ietK%2BP4tNaD8Aq1OSq3hU%2FMXl5h%2BV5S%2B&X-Amz-Signature=f11c477e76242550cd239423237249eb86728697c15f17abf83dc401cdcf279d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6O2K4OP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQCrjynoUuOaI4DU%2B0lb8j9KO2o4vNZaFHXpXa%2BZz7idIAIgdo4D9qoVG1EjyXHNx5E%2Bsi8Bto7S3ZkEt1fA9Se93DAqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKhSNM7ctIYKwfXgnSrcA90JIqjT4A1aIqOuZxfeZ58l6VfLiZkleKbB1wvDMs08kylqT9o%2FqYxSBbEKjEVKamKb4ynRyCFdJxxwp0ik3mN3n%2BWCLtzsJXpSdLgOoOkFkebLtucWH2k%2FUdfOFxYdNfxII9rSxjlbNHva%2BEf2Ydu3WoyBS40JhedF6SZoNZ1L50izA4wHfVMYf%2FVN8qy1LjBIEhwZSNftgOIrrxz%2BvZLLBu9Oc%2FWPHKKejUJ7kX0vmZEWxJoePdD%2FtqlhVOhrZ9rtpamAi91Rv60p8XXYsXisQ9WP8uCn6P9Aefk0UutudZ1XeKUaSI5silAvINceRoTd6hjGer21YtngqSpYqzlsMrjPfF7hf3E6jSkPptVEgFuhW%2FMHUYD7iPLZLWsObDudlyVEWEhX4z3%2FAD6J7TYxzvH5FZoh90EuO1Ba3qcZ86BW%2BkJALn2OtpDg8XrCDMyT6%2FVFqoCLIiekb4NueWLkn3GLOv00sdIxY0rsFihs20vjv0witnemzLxwCAFJmoFfS%2BxulBcAAiIjqb4%2B%2BrF2kuDsfPItMXmHG%2FWtlnNlgb67GEhDfxG2VpFC2mxqwd3fdTQ3KpaXq2SuhSnWXBgCcMeID%2FkVxu5I3ftr83yEAHlo%2BA26u%2Bm9ACGXMPLUm70GOqUBG9thd9eI9DI4%2BQvSgajUerWnKnvyEmljsP47wriuXCddyp0vaU45V%2F4%2BzGNAW4mnc%2Byp4V8Toek34tZ14JyV1tva3Y7UXk9U%2B1rJjHkKcEoZojwDfytuhdEFS8zsq78EnYFswh1GdCet0oL%2Bf83srqAh4JQJ0w3xc1HHacYY5GunL015XgFJIMj%2FEy32ietK%2BP4tNaD8Aq1OSq3hU%2FMXl5h%2BV5S%2B&X-Amz-Signature=79857dab070c18c677c67fbbd605d4e4541a8eacad349507b632f0de799a8e55&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6O2K4OP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQCrjynoUuOaI4DU%2B0lb8j9KO2o4vNZaFHXpXa%2BZz7idIAIgdo4D9qoVG1EjyXHNx5E%2Bsi8Bto7S3ZkEt1fA9Se93DAqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKhSNM7ctIYKwfXgnSrcA90JIqjT4A1aIqOuZxfeZ58l6VfLiZkleKbB1wvDMs08kylqT9o%2FqYxSBbEKjEVKamKb4ynRyCFdJxxwp0ik3mN3n%2BWCLtzsJXpSdLgOoOkFkebLtucWH2k%2FUdfOFxYdNfxII9rSxjlbNHva%2BEf2Ydu3WoyBS40JhedF6SZoNZ1L50izA4wHfVMYf%2FVN8qy1LjBIEhwZSNftgOIrrxz%2BvZLLBu9Oc%2FWPHKKejUJ7kX0vmZEWxJoePdD%2FtqlhVOhrZ9rtpamAi91Rv60p8XXYsXisQ9WP8uCn6P9Aefk0UutudZ1XeKUaSI5silAvINceRoTd6hjGer21YtngqSpYqzlsMrjPfF7hf3E6jSkPptVEgFuhW%2FMHUYD7iPLZLWsObDudlyVEWEhX4z3%2FAD6J7TYxzvH5FZoh90EuO1Ba3qcZ86BW%2BkJALn2OtpDg8XrCDMyT6%2FVFqoCLIiekb4NueWLkn3GLOv00sdIxY0rsFihs20vjv0witnemzLxwCAFJmoFfS%2BxulBcAAiIjqb4%2B%2BrF2kuDsfPItMXmHG%2FWtlnNlgb67GEhDfxG2VpFC2mxqwd3fdTQ3KpaXq2SuhSnWXBgCcMeID%2FkVxu5I3ftr83yEAHlo%2BA26u%2Bm9ACGXMPLUm70GOqUBG9thd9eI9DI4%2BQvSgajUerWnKnvyEmljsP47wriuXCddyp0vaU45V%2F4%2BzGNAW4mnc%2Byp4V8Toek34tZ14JyV1tva3Y7UXk9U%2B1rJjHkKcEoZojwDfytuhdEFS8zsq78EnYFswh1GdCet0oL%2Bf83srqAh4JQJ0w3xc1HHacYY5GunL015XgFJIMj%2FEy32ietK%2BP4tNaD8Aq1OSq3hU%2FMXl5h%2BV5S%2B&X-Amz-Signature=971a68a50350984c70de92240b8b35aa9fb77d667407a405688dc0cb84be5a6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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


