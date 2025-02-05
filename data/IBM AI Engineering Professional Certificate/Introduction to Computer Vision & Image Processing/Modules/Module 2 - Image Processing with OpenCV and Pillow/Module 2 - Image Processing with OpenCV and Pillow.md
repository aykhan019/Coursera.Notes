

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OMYBHXR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCqhcNjwZQKA0z2G0bZFvCQLOfuKNhYwSWPTdfBPUY%2FbAIhAI7fht9wDlO%2B8AyGzgPaQM7xunaPEnND71eA6%2B9Gw4GWKv8DCEQQABoMNjM3NDIzMTgzODA1IgwAO63cxxQarI%2FJuOMq3ANWsUc1A3u6l4xWtjsj70SsKajJ1KEprEm84E%2BtwEbMkq9mjZa2EsmlmqwfQRwXIH7dOu364zHFbR7tTsWNV30yomUH8kAYzkW2egZ2ifIl9jDDmwouc428Qj%2Br7wdc63GJB9TGjAUMeBY9z3jVSjVYJiIdrCtBXFEEmNh7zhRmxXJXlk65kFR%2BQb5%2F6%2BCGaFaT1IDVSSIvRbUtT4%2B7SZ7gVfCNC%2FBXj8MaZ8ksXWJTGrAVdT1zapIK7ZnIirnfaP6ZP%2FwZtjEFFxVXw91TLRRJT68OZPvKGLI1bri3bUyYmcYpGO3a9pICrN5jbORpXPai2ur6UlkkCUFZ2glwmeTEyvnh5L%2BFLe1AY0akZY%2FE%2Fc%2Fms1MmIi3Bp0KnJ4TGFd8ng6aH3cAYYYL04lRzfdJa1zleFUZUN5ZbUmY4dxX%2FSsEHVfkOoFGvPWIDf5jm529sO%2Fx3lPZHhRLV%2FsM36iY8CSK14OYLOXNeS%2BTOkRrwBox0XeKhTn2yf5NguS3FngX4Ej%2BfDeOANgtXnmwZMl%2FdDx9d3dfC9yD%2Fng09rxf5GQmbqpXCvM%2FHsAF2ZcPbYkykRDpEZ8fumB8u7SvKN6AvmFizNkjTsrUJi3QR7ErbrediVHeITBpn9qn5oTDxio29BjqkARjmwujmiWUtvV6jZ13cv9iVFDAeSeBCu%2B9wgvm7Bar5SH9k39zFdpJsVfPlSC9JC6UPvfIB2crQ7Kjk3QlIsnUkpyGXzXxNJ48iQqrEopp6tJRbOE7a3aVZ0x2ksznCEYKDN%2BUQO%2BuPCKO%2B%2FtdOrJVKXhtSaSAI71BzraUx0DGPbgEBQjf8N1v%2B3xnRBuAqaX5Bpw19s4xjsmilVH8oiqS4sUz2&X-Amz-Signature=648ec197aa54a95b458ce366c7db250d84f6067f7b62c642835aa49ea3097482&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667J5F3F3O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQC09Tjb4qKRW5poL6Kq%2FIuUKVKWa34x9cgYA0QszjdenAIgNiw1ISZUbixoAwgtK60QK3FftIsXC5cf1RKkeM0EpN0q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDBLz9Uyo%2BIKJrwH3ZSrcA2jO1n9Tljb%2BKLC2%2BuTOqUFLMKHxhy0rvNFD0GZ7y2qrn0GRt4Flys98MHhdZzeFE0HXClJ2XoGhHrX0fFD3Y7MXoR%2B%2Fj%2BD6yT%2Bq5sC8fSN0gWUSnxQmUigxfK0%2B2KrNOJd%2Bdb231pqZEuWYPTPl7qJyuskPkKzjtjM4yOUe%2Bu%2B3auU3J%2FnL9pS0x%2BU84c%2FUgZisxneYwnBFDFxQ6uZaGDSQbgy%2FBIVjPpUeFIRDabj6cRXR1CEHxwyIWojQUBS3pon8bFP99BLS3pnWvOlL%2FulmVwSjOCbgBzrlCbGWt%2BpFEiGDRtikNdi%2F2Qzp4Rid3dfIExZUPTLeesPFfFwEkXCmOWcRCDB04fA5hYmNHNE6nyzM8Aoy33L8CrLbjb4d0xX7shag8ijQrmRLDt6bxNlasj41aYotYYTDHbs5LAfRYpZAMyZIdWpX586W3Hv1dSkBVhsAnFh%2B0lZNHJYiEwk7NxZzIolRj4Of%2B1hdpubfyWVo3tN1EVyZglsd%2Fwb3MvYMTihJzzdZRmwCQyQ25aU%2BWbOcCocftG6v3XI8BROmA9L%2FjRubalbi%2BH6ItlmP9AgaEwGOZ%2F4tQgK%2B7IGqXBhhndNsUER7q3sWfi%2BEmnVkiywx9PgO%2Fe6A%2BmELMN2Kjb0GOqUB0aLMY%2Blkvyg3u9VkVGUKJBzsZVd8P5WHs1csXzF7G1o8BIUNbQVMhz7QoBEU0dgZYTLqYwuv5NHxgh1YZyGdgwLP9wS13CA4x2kG%2FCPRmK%2F%2F63lhPN5h3h8nYAJn%2FRVbBfZObOH36u8V33AtjTF6zAeSOJ8tK1JAXVp18SqYW3ftmOL1AoCwNTHPvxaywGJzP6mGv2p%2FGXcUN5rSIxiyagvsWuK%2B&X-Amz-Signature=ee658849584db5a4c14b8736bbcbbf90306e0b29c9173318ec053d2935e7852f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667J5F3F3O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQC09Tjb4qKRW5poL6Kq%2FIuUKVKWa34x9cgYA0QszjdenAIgNiw1ISZUbixoAwgtK60QK3FftIsXC5cf1RKkeM0EpN0q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDBLz9Uyo%2BIKJrwH3ZSrcA2jO1n9Tljb%2BKLC2%2BuTOqUFLMKHxhy0rvNFD0GZ7y2qrn0GRt4Flys98MHhdZzeFE0HXClJ2XoGhHrX0fFD3Y7MXoR%2B%2Fj%2BD6yT%2Bq5sC8fSN0gWUSnxQmUigxfK0%2B2KrNOJd%2Bdb231pqZEuWYPTPl7qJyuskPkKzjtjM4yOUe%2Bu%2B3auU3J%2FnL9pS0x%2BU84c%2FUgZisxneYwnBFDFxQ6uZaGDSQbgy%2FBIVjPpUeFIRDabj6cRXR1CEHxwyIWojQUBS3pon8bFP99BLS3pnWvOlL%2FulmVwSjOCbgBzrlCbGWt%2BpFEiGDRtikNdi%2F2Qzp4Rid3dfIExZUPTLeesPFfFwEkXCmOWcRCDB04fA5hYmNHNE6nyzM8Aoy33L8CrLbjb4d0xX7shag8ijQrmRLDt6bxNlasj41aYotYYTDHbs5LAfRYpZAMyZIdWpX586W3Hv1dSkBVhsAnFh%2B0lZNHJYiEwk7NxZzIolRj4Of%2B1hdpubfyWVo3tN1EVyZglsd%2Fwb3MvYMTihJzzdZRmwCQyQ25aU%2BWbOcCocftG6v3XI8BROmA9L%2FjRubalbi%2BH6ItlmP9AgaEwGOZ%2F4tQgK%2B7IGqXBhhndNsUER7q3sWfi%2BEmnVkiywx9PgO%2Fe6A%2BmELMN2Kjb0GOqUB0aLMY%2Blkvyg3u9VkVGUKJBzsZVd8P5WHs1csXzF7G1o8BIUNbQVMhz7QoBEU0dgZYTLqYwuv5NHxgh1YZyGdgwLP9wS13CA4x2kG%2FCPRmK%2F%2F63lhPN5h3h8nYAJn%2FRVbBfZObOH36u8V33AtjTF6zAeSOJ8tK1JAXVp18SqYW3ftmOL1AoCwNTHPvxaywGJzP6mGv2p%2FGXcUN5rSIxiyagvsWuK%2B&X-Amz-Signature=f679282d5e24f59387aa15fcc0c5ad6b095fb85dd4fa69778d44552608a3d93e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667J5F3F3O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQC09Tjb4qKRW5poL6Kq%2FIuUKVKWa34x9cgYA0QszjdenAIgNiw1ISZUbixoAwgtK60QK3FftIsXC5cf1RKkeM0EpN0q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDBLz9Uyo%2BIKJrwH3ZSrcA2jO1n9Tljb%2BKLC2%2BuTOqUFLMKHxhy0rvNFD0GZ7y2qrn0GRt4Flys98MHhdZzeFE0HXClJ2XoGhHrX0fFD3Y7MXoR%2B%2Fj%2BD6yT%2Bq5sC8fSN0gWUSnxQmUigxfK0%2B2KrNOJd%2Bdb231pqZEuWYPTPl7qJyuskPkKzjtjM4yOUe%2Bu%2B3auU3J%2FnL9pS0x%2BU84c%2FUgZisxneYwnBFDFxQ6uZaGDSQbgy%2FBIVjPpUeFIRDabj6cRXR1CEHxwyIWojQUBS3pon8bFP99BLS3pnWvOlL%2FulmVwSjOCbgBzrlCbGWt%2BpFEiGDRtikNdi%2F2Qzp4Rid3dfIExZUPTLeesPFfFwEkXCmOWcRCDB04fA5hYmNHNE6nyzM8Aoy33L8CrLbjb4d0xX7shag8ijQrmRLDt6bxNlasj41aYotYYTDHbs5LAfRYpZAMyZIdWpX586W3Hv1dSkBVhsAnFh%2B0lZNHJYiEwk7NxZzIolRj4Of%2B1hdpubfyWVo3tN1EVyZglsd%2Fwb3MvYMTihJzzdZRmwCQyQ25aU%2BWbOcCocftG6v3XI8BROmA9L%2FjRubalbi%2BH6ItlmP9AgaEwGOZ%2F4tQgK%2B7IGqXBhhndNsUER7q3sWfi%2BEmnVkiywx9PgO%2Fe6A%2BmELMN2Kjb0GOqUB0aLMY%2Blkvyg3u9VkVGUKJBzsZVd8P5WHs1csXzF7G1o8BIUNbQVMhz7QoBEU0dgZYTLqYwuv5NHxgh1YZyGdgwLP9wS13CA4x2kG%2FCPRmK%2F%2F63lhPN5h3h8nYAJn%2FRVbBfZObOH36u8V33AtjTF6zAeSOJ8tK1JAXVp18SqYW3ftmOL1AoCwNTHPvxaywGJzP6mGv2p%2FGXcUN5rSIxiyagvsWuK%2B&X-Amz-Signature=10676710d1213e8fe95e62bfa25bec13f22789e49cab1a28211150b99e397c51&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667J5F3F3O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQC09Tjb4qKRW5poL6Kq%2FIuUKVKWa34x9cgYA0QszjdenAIgNiw1ISZUbixoAwgtK60QK3FftIsXC5cf1RKkeM0EpN0q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDBLz9Uyo%2BIKJrwH3ZSrcA2jO1n9Tljb%2BKLC2%2BuTOqUFLMKHxhy0rvNFD0GZ7y2qrn0GRt4Flys98MHhdZzeFE0HXClJ2XoGhHrX0fFD3Y7MXoR%2B%2Fj%2BD6yT%2Bq5sC8fSN0gWUSnxQmUigxfK0%2B2KrNOJd%2Bdb231pqZEuWYPTPl7qJyuskPkKzjtjM4yOUe%2Bu%2B3auU3J%2FnL9pS0x%2BU84c%2FUgZisxneYwnBFDFxQ6uZaGDSQbgy%2FBIVjPpUeFIRDabj6cRXR1CEHxwyIWojQUBS3pon8bFP99BLS3pnWvOlL%2FulmVwSjOCbgBzrlCbGWt%2BpFEiGDRtikNdi%2F2Qzp4Rid3dfIExZUPTLeesPFfFwEkXCmOWcRCDB04fA5hYmNHNE6nyzM8Aoy33L8CrLbjb4d0xX7shag8ijQrmRLDt6bxNlasj41aYotYYTDHbs5LAfRYpZAMyZIdWpX586W3Hv1dSkBVhsAnFh%2B0lZNHJYiEwk7NxZzIolRj4Of%2B1hdpubfyWVo3tN1EVyZglsd%2Fwb3MvYMTihJzzdZRmwCQyQ25aU%2BWbOcCocftG6v3XI8BROmA9L%2FjRubalbi%2BH6ItlmP9AgaEwGOZ%2F4tQgK%2B7IGqXBhhndNsUER7q3sWfi%2BEmnVkiywx9PgO%2Fe6A%2BmELMN2Kjb0GOqUB0aLMY%2Blkvyg3u9VkVGUKJBzsZVd8P5WHs1csXzF7G1o8BIUNbQVMhz7QoBEU0dgZYTLqYwuv5NHxgh1YZyGdgwLP9wS13CA4x2kG%2FCPRmK%2F%2F63lhPN5h3h8nYAJn%2FRVbBfZObOH36u8V33AtjTF6zAeSOJ8tK1JAXVp18SqYW3ftmOL1AoCwNTHPvxaywGJzP6mGv2p%2FGXcUN5rSIxiyagvsWuK%2B&X-Amz-Signature=4c8eb47a37255b290af90d9a1fbe36dbf6cc706a5a2acad0a6b4459d891ca9bc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667J5F3F3O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQC09Tjb4qKRW5poL6Kq%2FIuUKVKWa34x9cgYA0QszjdenAIgNiw1ISZUbixoAwgtK60QK3FftIsXC5cf1RKkeM0EpN0q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDBLz9Uyo%2BIKJrwH3ZSrcA2jO1n9Tljb%2BKLC2%2BuTOqUFLMKHxhy0rvNFD0GZ7y2qrn0GRt4Flys98MHhdZzeFE0HXClJ2XoGhHrX0fFD3Y7MXoR%2B%2Fj%2BD6yT%2Bq5sC8fSN0gWUSnxQmUigxfK0%2B2KrNOJd%2Bdb231pqZEuWYPTPl7qJyuskPkKzjtjM4yOUe%2Bu%2B3auU3J%2FnL9pS0x%2BU84c%2FUgZisxneYwnBFDFxQ6uZaGDSQbgy%2FBIVjPpUeFIRDabj6cRXR1CEHxwyIWojQUBS3pon8bFP99BLS3pnWvOlL%2FulmVwSjOCbgBzrlCbGWt%2BpFEiGDRtikNdi%2F2Qzp4Rid3dfIExZUPTLeesPFfFwEkXCmOWcRCDB04fA5hYmNHNE6nyzM8Aoy33L8CrLbjb4d0xX7shag8ijQrmRLDt6bxNlasj41aYotYYTDHbs5LAfRYpZAMyZIdWpX586W3Hv1dSkBVhsAnFh%2B0lZNHJYiEwk7NxZzIolRj4Of%2B1hdpubfyWVo3tN1EVyZglsd%2Fwb3MvYMTihJzzdZRmwCQyQ25aU%2BWbOcCocftG6v3XI8BROmA9L%2FjRubalbi%2BH6ItlmP9AgaEwGOZ%2F4tQgK%2B7IGqXBhhndNsUER7q3sWfi%2BEmnVkiywx9PgO%2Fe6A%2BmELMN2Kjb0GOqUB0aLMY%2Blkvyg3u9VkVGUKJBzsZVd8P5WHs1csXzF7G1o8BIUNbQVMhz7QoBEU0dgZYTLqYwuv5NHxgh1YZyGdgwLP9wS13CA4x2kG%2FCPRmK%2F%2F63lhPN5h3h8nYAJn%2FRVbBfZObOH36u8V33AtjTF6zAeSOJ8tK1JAXVp18SqYW3ftmOL1AoCwNTHPvxaywGJzP6mGv2p%2FGXcUN5rSIxiyagvsWuK%2B&X-Amz-Signature=9f08488c9e6142e16b2e77c2973fbcac5b9b560fbb07ffa3bc74f7595ec0fa47&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OMYBHXR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCqhcNjwZQKA0z2G0bZFvCQLOfuKNhYwSWPTdfBPUY%2FbAIhAI7fht9wDlO%2B8AyGzgPaQM7xunaPEnND71eA6%2B9Gw4GWKv8DCEQQABoMNjM3NDIzMTgzODA1IgwAO63cxxQarI%2FJuOMq3ANWsUc1A3u6l4xWtjsj70SsKajJ1KEprEm84E%2BtwEbMkq9mjZa2EsmlmqwfQRwXIH7dOu364zHFbR7tTsWNV30yomUH8kAYzkW2egZ2ifIl9jDDmwouc428Qj%2Br7wdc63GJB9TGjAUMeBY9z3jVSjVYJiIdrCtBXFEEmNh7zhRmxXJXlk65kFR%2BQb5%2F6%2BCGaFaT1IDVSSIvRbUtT4%2B7SZ7gVfCNC%2FBXj8MaZ8ksXWJTGrAVdT1zapIK7ZnIirnfaP6ZP%2FwZtjEFFxVXw91TLRRJT68OZPvKGLI1bri3bUyYmcYpGO3a9pICrN5jbORpXPai2ur6UlkkCUFZ2glwmeTEyvnh5L%2BFLe1AY0akZY%2FE%2Fc%2Fms1MmIi3Bp0KnJ4TGFd8ng6aH3cAYYYL04lRzfdJa1zleFUZUN5ZbUmY4dxX%2FSsEHVfkOoFGvPWIDf5jm529sO%2Fx3lPZHhRLV%2FsM36iY8CSK14OYLOXNeS%2BTOkRrwBox0XeKhTn2yf5NguS3FngX4Ej%2BfDeOANgtXnmwZMl%2FdDx9d3dfC9yD%2Fng09rxf5GQmbqpXCvM%2FHsAF2ZcPbYkykRDpEZ8fumB8u7SvKN6AvmFizNkjTsrUJi3QR7ErbrediVHeITBpn9qn5oTDxio29BjqkARjmwujmiWUtvV6jZ13cv9iVFDAeSeBCu%2B9wgvm7Bar5SH9k39zFdpJsVfPlSC9JC6UPvfIB2crQ7Kjk3QlIsnUkpyGXzXxNJ48iQqrEopp6tJRbOE7a3aVZ0x2ksznCEYKDN%2BUQO%2BuPCKO%2B%2FtdOrJVKXhtSaSAI71BzraUx0DGPbgEBQjf8N1v%2B3xnRBuAqaX5Bpw19s4xjsmilVH8oiqS4sUz2&X-Amz-Signature=21c138684c9c82402cf976b0da7233f493ac38483b92390a088ba7304d8e40b9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OMYBHXR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCqhcNjwZQKA0z2G0bZFvCQLOfuKNhYwSWPTdfBPUY%2FbAIhAI7fht9wDlO%2B8AyGzgPaQM7xunaPEnND71eA6%2B9Gw4GWKv8DCEQQABoMNjM3NDIzMTgzODA1IgwAO63cxxQarI%2FJuOMq3ANWsUc1A3u6l4xWtjsj70SsKajJ1KEprEm84E%2BtwEbMkq9mjZa2EsmlmqwfQRwXIH7dOu364zHFbR7tTsWNV30yomUH8kAYzkW2egZ2ifIl9jDDmwouc428Qj%2Br7wdc63GJB9TGjAUMeBY9z3jVSjVYJiIdrCtBXFEEmNh7zhRmxXJXlk65kFR%2BQb5%2F6%2BCGaFaT1IDVSSIvRbUtT4%2B7SZ7gVfCNC%2FBXj8MaZ8ksXWJTGrAVdT1zapIK7ZnIirnfaP6ZP%2FwZtjEFFxVXw91TLRRJT68OZPvKGLI1bri3bUyYmcYpGO3a9pICrN5jbORpXPai2ur6UlkkCUFZ2glwmeTEyvnh5L%2BFLe1AY0akZY%2FE%2Fc%2Fms1MmIi3Bp0KnJ4TGFd8ng6aH3cAYYYL04lRzfdJa1zleFUZUN5ZbUmY4dxX%2FSsEHVfkOoFGvPWIDf5jm529sO%2Fx3lPZHhRLV%2FsM36iY8CSK14OYLOXNeS%2BTOkRrwBox0XeKhTn2yf5NguS3FngX4Ej%2BfDeOANgtXnmwZMl%2FdDx9d3dfC9yD%2Fng09rxf5GQmbqpXCvM%2FHsAF2ZcPbYkykRDpEZ8fumB8u7SvKN6AvmFizNkjTsrUJi3QR7ErbrediVHeITBpn9qn5oTDxio29BjqkARjmwujmiWUtvV6jZ13cv9iVFDAeSeBCu%2B9wgvm7Bar5SH9k39zFdpJsVfPlSC9JC6UPvfIB2crQ7Kjk3QlIsnUkpyGXzXxNJ48iQqrEopp6tJRbOE7a3aVZ0x2ksznCEYKDN%2BUQO%2BuPCKO%2B%2FtdOrJVKXhtSaSAI71BzraUx0DGPbgEBQjf8N1v%2B3xnRBuAqaX5Bpw19s4xjsmilVH8oiqS4sUz2&X-Amz-Signature=c113ff92c7b05da7fe2e75dc9cb6b13d08b820073089d9cc41041e0c1eeeaee7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OMYBHXR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCqhcNjwZQKA0z2G0bZFvCQLOfuKNhYwSWPTdfBPUY%2FbAIhAI7fht9wDlO%2B8AyGzgPaQM7xunaPEnND71eA6%2B9Gw4GWKv8DCEQQABoMNjM3NDIzMTgzODA1IgwAO63cxxQarI%2FJuOMq3ANWsUc1A3u6l4xWtjsj70SsKajJ1KEprEm84E%2BtwEbMkq9mjZa2EsmlmqwfQRwXIH7dOu364zHFbR7tTsWNV30yomUH8kAYzkW2egZ2ifIl9jDDmwouc428Qj%2Br7wdc63GJB9TGjAUMeBY9z3jVSjVYJiIdrCtBXFEEmNh7zhRmxXJXlk65kFR%2BQb5%2F6%2BCGaFaT1IDVSSIvRbUtT4%2B7SZ7gVfCNC%2FBXj8MaZ8ksXWJTGrAVdT1zapIK7ZnIirnfaP6ZP%2FwZtjEFFxVXw91TLRRJT68OZPvKGLI1bri3bUyYmcYpGO3a9pICrN5jbORpXPai2ur6UlkkCUFZ2glwmeTEyvnh5L%2BFLe1AY0akZY%2FE%2Fc%2Fms1MmIi3Bp0KnJ4TGFd8ng6aH3cAYYYL04lRzfdJa1zleFUZUN5ZbUmY4dxX%2FSsEHVfkOoFGvPWIDf5jm529sO%2Fx3lPZHhRLV%2FsM36iY8CSK14OYLOXNeS%2BTOkRrwBox0XeKhTn2yf5NguS3FngX4Ej%2BfDeOANgtXnmwZMl%2FdDx9d3dfC9yD%2Fng09rxf5GQmbqpXCvM%2FHsAF2ZcPbYkykRDpEZ8fumB8u7SvKN6AvmFizNkjTsrUJi3QR7ErbrediVHeITBpn9qn5oTDxio29BjqkARjmwujmiWUtvV6jZ13cv9iVFDAeSeBCu%2B9wgvm7Bar5SH9k39zFdpJsVfPlSC9JC6UPvfIB2crQ7Kjk3QlIsnUkpyGXzXxNJ48iQqrEopp6tJRbOE7a3aVZ0x2ksznCEYKDN%2BUQO%2BuPCKO%2B%2FtdOrJVKXhtSaSAI71BzraUx0DGPbgEBQjf8N1v%2B3xnRBuAqaX5Bpw19s4xjsmilVH8oiqS4sUz2&X-Amz-Signature=4f670bd2114f968238c91d905a95e85f9acb84b8a2e0ad060abd772f94c36f4d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OMYBHXR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCqhcNjwZQKA0z2G0bZFvCQLOfuKNhYwSWPTdfBPUY%2FbAIhAI7fht9wDlO%2B8AyGzgPaQM7xunaPEnND71eA6%2B9Gw4GWKv8DCEQQABoMNjM3NDIzMTgzODA1IgwAO63cxxQarI%2FJuOMq3ANWsUc1A3u6l4xWtjsj70SsKajJ1KEprEm84E%2BtwEbMkq9mjZa2EsmlmqwfQRwXIH7dOu364zHFbR7tTsWNV30yomUH8kAYzkW2egZ2ifIl9jDDmwouc428Qj%2Br7wdc63GJB9TGjAUMeBY9z3jVSjVYJiIdrCtBXFEEmNh7zhRmxXJXlk65kFR%2BQb5%2F6%2BCGaFaT1IDVSSIvRbUtT4%2B7SZ7gVfCNC%2FBXj8MaZ8ksXWJTGrAVdT1zapIK7ZnIirnfaP6ZP%2FwZtjEFFxVXw91TLRRJT68OZPvKGLI1bri3bUyYmcYpGO3a9pICrN5jbORpXPai2ur6UlkkCUFZ2glwmeTEyvnh5L%2BFLe1AY0akZY%2FE%2Fc%2Fms1MmIi3Bp0KnJ4TGFd8ng6aH3cAYYYL04lRzfdJa1zleFUZUN5ZbUmY4dxX%2FSsEHVfkOoFGvPWIDf5jm529sO%2Fx3lPZHhRLV%2FsM36iY8CSK14OYLOXNeS%2BTOkRrwBox0XeKhTn2yf5NguS3FngX4Ej%2BfDeOANgtXnmwZMl%2FdDx9d3dfC9yD%2Fng09rxf5GQmbqpXCvM%2FHsAF2ZcPbYkykRDpEZ8fumB8u7SvKN6AvmFizNkjTsrUJi3QR7ErbrediVHeITBpn9qn5oTDxio29BjqkARjmwujmiWUtvV6jZ13cv9iVFDAeSeBCu%2B9wgvm7Bar5SH9k39zFdpJsVfPlSC9JC6UPvfIB2crQ7Kjk3QlIsnUkpyGXzXxNJ48iQqrEopp6tJRbOE7a3aVZ0x2ksznCEYKDN%2BUQO%2BuPCKO%2B%2FtdOrJVKXhtSaSAI71BzraUx0DGPbgEBQjf8N1v%2B3xnRBuAqaX5Bpw19s4xjsmilVH8oiqS4sUz2&X-Amz-Signature=ea46a33d07fb6e0c6bb4dea0bc6f7ff5c56cc97ae686976fbf42e07e00c40961&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OMYBHXR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCqhcNjwZQKA0z2G0bZFvCQLOfuKNhYwSWPTdfBPUY%2FbAIhAI7fht9wDlO%2B8AyGzgPaQM7xunaPEnND71eA6%2B9Gw4GWKv8DCEQQABoMNjM3NDIzMTgzODA1IgwAO63cxxQarI%2FJuOMq3ANWsUc1A3u6l4xWtjsj70SsKajJ1KEprEm84E%2BtwEbMkq9mjZa2EsmlmqwfQRwXIH7dOu364zHFbR7tTsWNV30yomUH8kAYzkW2egZ2ifIl9jDDmwouc428Qj%2Br7wdc63GJB9TGjAUMeBY9z3jVSjVYJiIdrCtBXFEEmNh7zhRmxXJXlk65kFR%2BQb5%2F6%2BCGaFaT1IDVSSIvRbUtT4%2B7SZ7gVfCNC%2FBXj8MaZ8ksXWJTGrAVdT1zapIK7ZnIirnfaP6ZP%2FwZtjEFFxVXw91TLRRJT68OZPvKGLI1bri3bUyYmcYpGO3a9pICrN5jbORpXPai2ur6UlkkCUFZ2glwmeTEyvnh5L%2BFLe1AY0akZY%2FE%2Fc%2Fms1MmIi3Bp0KnJ4TGFd8ng6aH3cAYYYL04lRzfdJa1zleFUZUN5ZbUmY4dxX%2FSsEHVfkOoFGvPWIDf5jm529sO%2Fx3lPZHhRLV%2FsM36iY8CSK14OYLOXNeS%2BTOkRrwBox0XeKhTn2yf5NguS3FngX4Ej%2BfDeOANgtXnmwZMl%2FdDx9d3dfC9yD%2Fng09rxf5GQmbqpXCvM%2FHsAF2ZcPbYkykRDpEZ8fumB8u7SvKN6AvmFizNkjTsrUJi3QR7ErbrediVHeITBpn9qn5oTDxio29BjqkARjmwujmiWUtvV6jZ13cv9iVFDAeSeBCu%2B9wgvm7Bar5SH9k39zFdpJsVfPlSC9JC6UPvfIB2crQ7Kjk3QlIsnUkpyGXzXxNJ48iQqrEopp6tJRbOE7a3aVZ0x2ksznCEYKDN%2BUQO%2BuPCKO%2B%2FtdOrJVKXhtSaSAI71BzraUx0DGPbgEBQjf8N1v%2B3xnRBuAqaX5Bpw19s4xjsmilVH8oiqS4sUz2&X-Amz-Signature=c2a8480452c1ecaa7975666e92934db8944be7527fd2676eb44f4ebabf911cd2&X-Amz-SignedHeaders=host&x-id=GetObject)
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


