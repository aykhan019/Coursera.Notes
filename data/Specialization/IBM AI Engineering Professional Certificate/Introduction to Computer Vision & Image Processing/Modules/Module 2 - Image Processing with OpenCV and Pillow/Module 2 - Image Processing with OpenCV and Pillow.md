

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NDPV5FX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGYkPCVtygJc0m1eMyR5EjlQnk5%2Bi0nySop821Ks7w8PAiEAuQ%2Fg0eLtu1bn8IAsVng5jdCjOjmSVJMxvFOdutqUYsgqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL0ignNErtIAUk%2FKDCrcA3uzINxQcBA5O1k6xs3woj7S0Sf8yKYJfgt8Adx5Ea56pK3gknEStdKCllElwMpOZXvf5xKnDGd15gumDTe7d2%2B05UlNLvCGAAW%2BxNiKJys5NJdkC7r2FhPcxMg1xa4pP%2BCn6JRxFVryq446YjtH2kJyNh4rab0%2B%2BIX%2FYwANEUqqg2xi1ZXkk9EaMVBe9eVJlkF2vXn8DFiTk5FjR3%2B%2BfbnPxQmHg%2B6CbeUVIdEx68I6D95NRY9hCXAsOqYieij77dM3GzziWeQrNtO2YgnblYX413L3luuzQ3tsK9VSfiKpPV76TFCmTcEuIgfFC4hyIlpVqObS8Od6sTrwRg1ws%2FS6%2FmX1EWydcCMBfIWBYIKaEBiHMn7SM8ZA0WnNiSgyntpQb52aDfY8DBgKxlDtfx7R9w6vb9Q9iXOLJz5xiUQKiLBgYZgK1VZCS4lKQHjPSoEZQfUIjV%2B6%2BNTLS%2BfLtrk4%2FSK4ZfjFG2WN3qZtGI0DKipdUexvNXu9SWhMjTJ0CaN%2FSJcAKLO0OjJhm%2FnyBsQRcHM%2Fhqb5EH9zCkILmANiKR%2FYAKJohiEkjL4z9ntA6slL6XxZ8eFAB04t1AcyzxE4GB3vJ1KAScxti4LlVdlnI5qj%2FVm8h6YRGRZIMJ3f7bwGOqUBUL7Ih7b5mSZVxX1wTWoP0RdV6PPFX2%2FncTy94LTWqzkZ29k8Ob%2FAmxSzf1nBl3O13fdUYxrE3x%2FxkNCGqT7AYhOiegiqOr758C6H3bASlFHYEURH33OcQFZV3ObQu3gftfkHp%2BuoidXCtMwsrR3NaTNEgLeREqvNcP2DE1dC7uDs2xyOjzH4zf0JU4lgdwMWCZ5k1DHGtoaDUZsJ6k6J10OOaPv%2B&X-Amz-Signature=553928eeb7e7c97ba8497b42106248382b40f6e7fc017a8eedcfd73e86e210e7&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3ABOOFI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBqgr687%2F3eRITjmx9GfLuAS%2FKv9uWhZmgR%2FJUl24eTCAiEAl1NaiLTfEU%2F2ERHcp0c1X5y7sb%2B2kq8RAGGWRdOFcGwqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDBmPKlq0PbOdbOKHSrcA3HRLS1Hmo%2BK6eeTJP4mD1jevYo2VZTVW9Dsw2YvGZH4DV%2BgCRjKrQ8xz6sG0tog9o8%2Fwdqp19%2Fab%2B6MwYUezYddrc1SXdIPJwvTUggbUtjtbz2vNIJgzJ4RgXCA9BWiBeUH7u3HSGMnNwVCMQhzlpK4MdBHnizZG4UyO%2BpHwimOQVbbPedH4Ih%2FtdQ4%2FkDNaB10wkys1D3iYBcBrEwJzYyGV2bUxxaU5kzJmrET4N8WOKHyrOe9OzwhQoI%2Bcz8RPy%2FmkJp41EtFyyuAfLQLvWG5MgR%2BZ7ZmPTCp5uLy2LI1Z%2BXeHRfYMZzBIVRLhra3LPGGrwb29l3CYuItJH6TO9JESvdbQySqR36jdMnBtWYTlMWsTFKn8nuDv3HJht9FJBpBmqwMNxCHKUA%2BRu271jBVEJzoQadSW7TlbtSoYwYwsQmauN6zVfk7Sgh%2Fv5Zl6YFvs7a9hXrDpwz%2F3NM8u79S6efcPCZBvD9%2FaFHt4J5Kli6ZGW1T5eEThCCJdgzLVK3p%2B4zkQ%2BwGC4v%2BCzEdnLIxLutoItp4dQA0W%2FDb8u9ZKPtmUFrMPJqBcAcswmColKNnTbWyDut53lJ6Sv8UG%2FK0NTP4cWgwn1BF9QZ%2FeNybjKGaH00atDEr0x9tMJjf7bwGOqUBL%2Fl0GLlXv6xPnzkIIn25tAjivAW09ns1wvbt9DbGq%2Fw6wb1xtAe9heuxYAzvhBmzZL%2BS3QyulVRBo29v46ZZaVL2dM3XBn4%2BXfzT1y5zt3rgq56QmDJb%2FB4c4eYPFesEJJwcBkcuABtV4dcSOkW5c0qQ9q%2B33e4dsQoCqx6dP7gLWVc4MvGwQrAzkEVKflmmeArfPHyjoOauTpBHQW2vyh2uQXqF&X-Amz-Signature=bdae0a6e1915fa0160e1cb37b9a3ca390dc70cd05f57e05c199642f053f2b548&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3ABOOFI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBqgr687%2F3eRITjmx9GfLuAS%2FKv9uWhZmgR%2FJUl24eTCAiEAl1NaiLTfEU%2F2ERHcp0c1X5y7sb%2B2kq8RAGGWRdOFcGwqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDBmPKlq0PbOdbOKHSrcA3HRLS1Hmo%2BK6eeTJP4mD1jevYo2VZTVW9Dsw2YvGZH4DV%2BgCRjKrQ8xz6sG0tog9o8%2Fwdqp19%2Fab%2B6MwYUezYddrc1SXdIPJwvTUggbUtjtbz2vNIJgzJ4RgXCA9BWiBeUH7u3HSGMnNwVCMQhzlpK4MdBHnizZG4UyO%2BpHwimOQVbbPedH4Ih%2FtdQ4%2FkDNaB10wkys1D3iYBcBrEwJzYyGV2bUxxaU5kzJmrET4N8WOKHyrOe9OzwhQoI%2Bcz8RPy%2FmkJp41EtFyyuAfLQLvWG5MgR%2BZ7ZmPTCp5uLy2LI1Z%2BXeHRfYMZzBIVRLhra3LPGGrwb29l3CYuItJH6TO9JESvdbQySqR36jdMnBtWYTlMWsTFKn8nuDv3HJht9FJBpBmqwMNxCHKUA%2BRu271jBVEJzoQadSW7TlbtSoYwYwsQmauN6zVfk7Sgh%2Fv5Zl6YFvs7a9hXrDpwz%2F3NM8u79S6efcPCZBvD9%2FaFHt4J5Kli6ZGW1T5eEThCCJdgzLVK3p%2B4zkQ%2BwGC4v%2BCzEdnLIxLutoItp4dQA0W%2FDb8u9ZKPtmUFrMPJqBcAcswmColKNnTbWyDut53lJ6Sv8UG%2FK0NTP4cWgwn1BF9QZ%2FeNybjKGaH00atDEr0x9tMJjf7bwGOqUBL%2Fl0GLlXv6xPnzkIIn25tAjivAW09ns1wvbt9DbGq%2Fw6wb1xtAe9heuxYAzvhBmzZL%2BS3QyulVRBo29v46ZZaVL2dM3XBn4%2BXfzT1y5zt3rgq56QmDJb%2FB4c4eYPFesEJJwcBkcuABtV4dcSOkW5c0qQ9q%2B33e4dsQoCqx6dP7gLWVc4MvGwQrAzkEVKflmmeArfPHyjoOauTpBHQW2vyh2uQXqF&X-Amz-Signature=7a3a583a0e812155bccceacdbabf06a17b1d75958b1532f0f3583c8ceb4ad191&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3ABOOFI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBqgr687%2F3eRITjmx9GfLuAS%2FKv9uWhZmgR%2FJUl24eTCAiEAl1NaiLTfEU%2F2ERHcp0c1X5y7sb%2B2kq8RAGGWRdOFcGwqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDBmPKlq0PbOdbOKHSrcA3HRLS1Hmo%2BK6eeTJP4mD1jevYo2VZTVW9Dsw2YvGZH4DV%2BgCRjKrQ8xz6sG0tog9o8%2Fwdqp19%2Fab%2B6MwYUezYddrc1SXdIPJwvTUggbUtjtbz2vNIJgzJ4RgXCA9BWiBeUH7u3HSGMnNwVCMQhzlpK4MdBHnizZG4UyO%2BpHwimOQVbbPedH4Ih%2FtdQ4%2FkDNaB10wkys1D3iYBcBrEwJzYyGV2bUxxaU5kzJmrET4N8WOKHyrOe9OzwhQoI%2Bcz8RPy%2FmkJp41EtFyyuAfLQLvWG5MgR%2BZ7ZmPTCp5uLy2LI1Z%2BXeHRfYMZzBIVRLhra3LPGGrwb29l3CYuItJH6TO9JESvdbQySqR36jdMnBtWYTlMWsTFKn8nuDv3HJht9FJBpBmqwMNxCHKUA%2BRu271jBVEJzoQadSW7TlbtSoYwYwsQmauN6zVfk7Sgh%2Fv5Zl6YFvs7a9hXrDpwz%2F3NM8u79S6efcPCZBvD9%2FaFHt4J5Kli6ZGW1T5eEThCCJdgzLVK3p%2B4zkQ%2BwGC4v%2BCzEdnLIxLutoItp4dQA0W%2FDb8u9ZKPtmUFrMPJqBcAcswmColKNnTbWyDut53lJ6Sv8UG%2FK0NTP4cWgwn1BF9QZ%2FeNybjKGaH00atDEr0x9tMJjf7bwGOqUBL%2Fl0GLlXv6xPnzkIIn25tAjivAW09ns1wvbt9DbGq%2Fw6wb1xtAe9heuxYAzvhBmzZL%2BS3QyulVRBo29v46ZZaVL2dM3XBn4%2BXfzT1y5zt3rgq56QmDJb%2FB4c4eYPFesEJJwcBkcuABtV4dcSOkW5c0qQ9q%2B33e4dsQoCqx6dP7gLWVc4MvGwQrAzkEVKflmmeArfPHyjoOauTpBHQW2vyh2uQXqF&X-Amz-Signature=6f7e2f6f8491739e39e1d6e15de3db0939a14869a5cd20bd8cfaf5efbe15c775&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3ABOOFI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBqgr687%2F3eRITjmx9GfLuAS%2FKv9uWhZmgR%2FJUl24eTCAiEAl1NaiLTfEU%2F2ERHcp0c1X5y7sb%2B2kq8RAGGWRdOFcGwqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDBmPKlq0PbOdbOKHSrcA3HRLS1Hmo%2BK6eeTJP4mD1jevYo2VZTVW9Dsw2YvGZH4DV%2BgCRjKrQ8xz6sG0tog9o8%2Fwdqp19%2Fab%2B6MwYUezYddrc1SXdIPJwvTUggbUtjtbz2vNIJgzJ4RgXCA9BWiBeUH7u3HSGMnNwVCMQhzlpK4MdBHnizZG4UyO%2BpHwimOQVbbPedH4Ih%2FtdQ4%2FkDNaB10wkys1D3iYBcBrEwJzYyGV2bUxxaU5kzJmrET4N8WOKHyrOe9OzwhQoI%2Bcz8RPy%2FmkJp41EtFyyuAfLQLvWG5MgR%2BZ7ZmPTCp5uLy2LI1Z%2BXeHRfYMZzBIVRLhra3LPGGrwb29l3CYuItJH6TO9JESvdbQySqR36jdMnBtWYTlMWsTFKn8nuDv3HJht9FJBpBmqwMNxCHKUA%2BRu271jBVEJzoQadSW7TlbtSoYwYwsQmauN6zVfk7Sgh%2Fv5Zl6YFvs7a9hXrDpwz%2F3NM8u79S6efcPCZBvD9%2FaFHt4J5Kli6ZGW1T5eEThCCJdgzLVK3p%2B4zkQ%2BwGC4v%2BCzEdnLIxLutoItp4dQA0W%2FDb8u9ZKPtmUFrMPJqBcAcswmColKNnTbWyDut53lJ6Sv8UG%2FK0NTP4cWgwn1BF9QZ%2FeNybjKGaH00atDEr0x9tMJjf7bwGOqUBL%2Fl0GLlXv6xPnzkIIn25tAjivAW09ns1wvbt9DbGq%2Fw6wb1xtAe9heuxYAzvhBmzZL%2BS3QyulVRBo29v46ZZaVL2dM3XBn4%2BXfzT1y5zt3rgq56QmDJb%2FB4c4eYPFesEJJwcBkcuABtV4dcSOkW5c0qQ9q%2B33e4dsQoCqx6dP7gLWVc4MvGwQrAzkEVKflmmeArfPHyjoOauTpBHQW2vyh2uQXqF&X-Amz-Signature=e03ce2ba9a932d740ef5a1279c66a97f2cf50c97dcb242197a3de3864806d22a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3ABOOFI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBqgr687%2F3eRITjmx9GfLuAS%2FKv9uWhZmgR%2FJUl24eTCAiEAl1NaiLTfEU%2F2ERHcp0c1X5y7sb%2B2kq8RAGGWRdOFcGwqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDBmPKlq0PbOdbOKHSrcA3HRLS1Hmo%2BK6eeTJP4mD1jevYo2VZTVW9Dsw2YvGZH4DV%2BgCRjKrQ8xz6sG0tog9o8%2Fwdqp19%2Fab%2B6MwYUezYddrc1SXdIPJwvTUggbUtjtbz2vNIJgzJ4RgXCA9BWiBeUH7u3HSGMnNwVCMQhzlpK4MdBHnizZG4UyO%2BpHwimOQVbbPedH4Ih%2FtdQ4%2FkDNaB10wkys1D3iYBcBrEwJzYyGV2bUxxaU5kzJmrET4N8WOKHyrOe9OzwhQoI%2Bcz8RPy%2FmkJp41EtFyyuAfLQLvWG5MgR%2BZ7ZmPTCp5uLy2LI1Z%2BXeHRfYMZzBIVRLhra3LPGGrwb29l3CYuItJH6TO9JESvdbQySqR36jdMnBtWYTlMWsTFKn8nuDv3HJht9FJBpBmqwMNxCHKUA%2BRu271jBVEJzoQadSW7TlbtSoYwYwsQmauN6zVfk7Sgh%2Fv5Zl6YFvs7a9hXrDpwz%2F3NM8u79S6efcPCZBvD9%2FaFHt4J5Kli6ZGW1T5eEThCCJdgzLVK3p%2B4zkQ%2BwGC4v%2BCzEdnLIxLutoItp4dQA0W%2FDb8u9ZKPtmUFrMPJqBcAcswmColKNnTbWyDut53lJ6Sv8UG%2FK0NTP4cWgwn1BF9QZ%2FeNybjKGaH00atDEr0x9tMJjf7bwGOqUBL%2Fl0GLlXv6xPnzkIIn25tAjivAW09ns1wvbt9DbGq%2Fw6wb1xtAe9heuxYAzvhBmzZL%2BS3QyulVRBo29v46ZZaVL2dM3XBn4%2BXfzT1y5zt3rgq56QmDJb%2FB4c4eYPFesEJJwcBkcuABtV4dcSOkW5c0qQ9q%2B33e4dsQoCqx6dP7gLWVc4MvGwQrAzkEVKflmmeArfPHyjoOauTpBHQW2vyh2uQXqF&X-Amz-Signature=3607622edd4479290f11864a220868de9680e517bb639ea980929de098ec1b91&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NDPV5FX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGYkPCVtygJc0m1eMyR5EjlQnk5%2Bi0nySop821Ks7w8PAiEAuQ%2Fg0eLtu1bn8IAsVng5jdCjOjmSVJMxvFOdutqUYsgqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL0ignNErtIAUk%2FKDCrcA3uzINxQcBA5O1k6xs3woj7S0Sf8yKYJfgt8Adx5Ea56pK3gknEStdKCllElwMpOZXvf5xKnDGd15gumDTe7d2%2B05UlNLvCGAAW%2BxNiKJys5NJdkC7r2FhPcxMg1xa4pP%2BCn6JRxFVryq446YjtH2kJyNh4rab0%2B%2BIX%2FYwANEUqqg2xi1ZXkk9EaMVBe9eVJlkF2vXn8DFiTk5FjR3%2B%2BfbnPxQmHg%2B6CbeUVIdEx68I6D95NRY9hCXAsOqYieij77dM3GzziWeQrNtO2YgnblYX413L3luuzQ3tsK9VSfiKpPV76TFCmTcEuIgfFC4hyIlpVqObS8Od6sTrwRg1ws%2FS6%2FmX1EWydcCMBfIWBYIKaEBiHMn7SM8ZA0WnNiSgyntpQb52aDfY8DBgKxlDtfx7R9w6vb9Q9iXOLJz5xiUQKiLBgYZgK1VZCS4lKQHjPSoEZQfUIjV%2B6%2BNTLS%2BfLtrk4%2FSK4ZfjFG2WN3qZtGI0DKipdUexvNXu9SWhMjTJ0CaN%2FSJcAKLO0OjJhm%2FnyBsQRcHM%2Fhqb5EH9zCkILmANiKR%2FYAKJohiEkjL4z9ntA6slL6XxZ8eFAB04t1AcyzxE4GB3vJ1KAScxti4LlVdlnI5qj%2FVm8h6YRGRZIMJ3f7bwGOqUBUL7Ih7b5mSZVxX1wTWoP0RdV6PPFX2%2FncTy94LTWqzkZ29k8Ob%2FAmxSzf1nBl3O13fdUYxrE3x%2FxkNCGqT7AYhOiegiqOr758C6H3bASlFHYEURH33OcQFZV3ObQu3gftfkHp%2BuoidXCtMwsrR3NaTNEgLeREqvNcP2DE1dC7uDs2xyOjzH4zf0JU4lgdwMWCZ5k1DHGtoaDUZsJ6k6J10OOaPv%2B&X-Amz-Signature=3e157ed1ce241ceb6d4f44f22bc0660457742f1aa37a784612c5f7f5cd9b77df&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NDPV5FX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGYkPCVtygJc0m1eMyR5EjlQnk5%2Bi0nySop821Ks7w8PAiEAuQ%2Fg0eLtu1bn8IAsVng5jdCjOjmSVJMxvFOdutqUYsgqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL0ignNErtIAUk%2FKDCrcA3uzINxQcBA5O1k6xs3woj7S0Sf8yKYJfgt8Adx5Ea56pK3gknEStdKCllElwMpOZXvf5xKnDGd15gumDTe7d2%2B05UlNLvCGAAW%2BxNiKJys5NJdkC7r2FhPcxMg1xa4pP%2BCn6JRxFVryq446YjtH2kJyNh4rab0%2B%2BIX%2FYwANEUqqg2xi1ZXkk9EaMVBe9eVJlkF2vXn8DFiTk5FjR3%2B%2BfbnPxQmHg%2B6CbeUVIdEx68I6D95NRY9hCXAsOqYieij77dM3GzziWeQrNtO2YgnblYX413L3luuzQ3tsK9VSfiKpPV76TFCmTcEuIgfFC4hyIlpVqObS8Od6sTrwRg1ws%2FS6%2FmX1EWydcCMBfIWBYIKaEBiHMn7SM8ZA0WnNiSgyntpQb52aDfY8DBgKxlDtfx7R9w6vb9Q9iXOLJz5xiUQKiLBgYZgK1VZCS4lKQHjPSoEZQfUIjV%2B6%2BNTLS%2BfLtrk4%2FSK4ZfjFG2WN3qZtGI0DKipdUexvNXu9SWhMjTJ0CaN%2FSJcAKLO0OjJhm%2FnyBsQRcHM%2Fhqb5EH9zCkILmANiKR%2FYAKJohiEkjL4z9ntA6slL6XxZ8eFAB04t1AcyzxE4GB3vJ1KAScxti4LlVdlnI5qj%2FVm8h6YRGRZIMJ3f7bwGOqUBUL7Ih7b5mSZVxX1wTWoP0RdV6PPFX2%2FncTy94LTWqzkZ29k8Ob%2FAmxSzf1nBl3O13fdUYxrE3x%2FxkNCGqT7AYhOiegiqOr758C6H3bASlFHYEURH33OcQFZV3ObQu3gftfkHp%2BuoidXCtMwsrR3NaTNEgLeREqvNcP2DE1dC7uDs2xyOjzH4zf0JU4lgdwMWCZ5k1DHGtoaDUZsJ6k6J10OOaPv%2B&X-Amz-Signature=5985d88d72dcc037ac5204b97a61c6b12b508a3a777d5a58f208fa82aa973ac5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NDPV5FX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGYkPCVtygJc0m1eMyR5EjlQnk5%2Bi0nySop821Ks7w8PAiEAuQ%2Fg0eLtu1bn8IAsVng5jdCjOjmSVJMxvFOdutqUYsgqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL0ignNErtIAUk%2FKDCrcA3uzINxQcBA5O1k6xs3woj7S0Sf8yKYJfgt8Adx5Ea56pK3gknEStdKCllElwMpOZXvf5xKnDGd15gumDTe7d2%2B05UlNLvCGAAW%2BxNiKJys5NJdkC7r2FhPcxMg1xa4pP%2BCn6JRxFVryq446YjtH2kJyNh4rab0%2B%2BIX%2FYwANEUqqg2xi1ZXkk9EaMVBe9eVJlkF2vXn8DFiTk5FjR3%2B%2BfbnPxQmHg%2B6CbeUVIdEx68I6D95NRY9hCXAsOqYieij77dM3GzziWeQrNtO2YgnblYX413L3luuzQ3tsK9VSfiKpPV76TFCmTcEuIgfFC4hyIlpVqObS8Od6sTrwRg1ws%2FS6%2FmX1EWydcCMBfIWBYIKaEBiHMn7SM8ZA0WnNiSgyntpQb52aDfY8DBgKxlDtfx7R9w6vb9Q9iXOLJz5xiUQKiLBgYZgK1VZCS4lKQHjPSoEZQfUIjV%2B6%2BNTLS%2BfLtrk4%2FSK4ZfjFG2WN3qZtGI0DKipdUexvNXu9SWhMjTJ0CaN%2FSJcAKLO0OjJhm%2FnyBsQRcHM%2Fhqb5EH9zCkILmANiKR%2FYAKJohiEkjL4z9ntA6slL6XxZ8eFAB04t1AcyzxE4GB3vJ1KAScxti4LlVdlnI5qj%2FVm8h6YRGRZIMJ3f7bwGOqUBUL7Ih7b5mSZVxX1wTWoP0RdV6PPFX2%2FncTy94LTWqzkZ29k8Ob%2FAmxSzf1nBl3O13fdUYxrE3x%2FxkNCGqT7AYhOiegiqOr758C6H3bASlFHYEURH33OcQFZV3ObQu3gftfkHp%2BuoidXCtMwsrR3NaTNEgLeREqvNcP2DE1dC7uDs2xyOjzH4zf0JU4lgdwMWCZ5k1DHGtoaDUZsJ6k6J10OOaPv%2B&X-Amz-Signature=7e264e8a30ed321422c24a5a8ddf97dfa8e6571eb4773df2335e5bcf729f9426&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NDPV5FX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGYkPCVtygJc0m1eMyR5EjlQnk5%2Bi0nySop821Ks7w8PAiEAuQ%2Fg0eLtu1bn8IAsVng5jdCjOjmSVJMxvFOdutqUYsgqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL0ignNErtIAUk%2FKDCrcA3uzINxQcBA5O1k6xs3woj7S0Sf8yKYJfgt8Adx5Ea56pK3gknEStdKCllElwMpOZXvf5xKnDGd15gumDTe7d2%2B05UlNLvCGAAW%2BxNiKJys5NJdkC7r2FhPcxMg1xa4pP%2BCn6JRxFVryq446YjtH2kJyNh4rab0%2B%2BIX%2FYwANEUqqg2xi1ZXkk9EaMVBe9eVJlkF2vXn8DFiTk5FjR3%2B%2BfbnPxQmHg%2B6CbeUVIdEx68I6D95NRY9hCXAsOqYieij77dM3GzziWeQrNtO2YgnblYX413L3luuzQ3tsK9VSfiKpPV76TFCmTcEuIgfFC4hyIlpVqObS8Od6sTrwRg1ws%2FS6%2FmX1EWydcCMBfIWBYIKaEBiHMn7SM8ZA0WnNiSgyntpQb52aDfY8DBgKxlDtfx7R9w6vb9Q9iXOLJz5xiUQKiLBgYZgK1VZCS4lKQHjPSoEZQfUIjV%2B6%2BNTLS%2BfLtrk4%2FSK4ZfjFG2WN3qZtGI0DKipdUexvNXu9SWhMjTJ0CaN%2FSJcAKLO0OjJhm%2FnyBsQRcHM%2Fhqb5EH9zCkILmANiKR%2FYAKJohiEkjL4z9ntA6slL6XxZ8eFAB04t1AcyzxE4GB3vJ1KAScxti4LlVdlnI5qj%2FVm8h6YRGRZIMJ3f7bwGOqUBUL7Ih7b5mSZVxX1wTWoP0RdV6PPFX2%2FncTy94LTWqzkZ29k8Ob%2FAmxSzf1nBl3O13fdUYxrE3x%2FxkNCGqT7AYhOiegiqOr758C6H3bASlFHYEURH33OcQFZV3ObQu3gftfkHp%2BuoidXCtMwsrR3NaTNEgLeREqvNcP2DE1dC7uDs2xyOjzH4zf0JU4lgdwMWCZ5k1DHGtoaDUZsJ6k6J10OOaPv%2B&X-Amz-Signature=869cc27d768f42e21e39ce1e9a4fb128e499730c608185880e92b06331c73d7f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NDPV5FX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGYkPCVtygJc0m1eMyR5EjlQnk5%2Bi0nySop821Ks7w8PAiEAuQ%2Fg0eLtu1bn8IAsVng5jdCjOjmSVJMxvFOdutqUYsgqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL0ignNErtIAUk%2FKDCrcA3uzINxQcBA5O1k6xs3woj7S0Sf8yKYJfgt8Adx5Ea56pK3gknEStdKCllElwMpOZXvf5xKnDGd15gumDTe7d2%2B05UlNLvCGAAW%2BxNiKJys5NJdkC7r2FhPcxMg1xa4pP%2BCn6JRxFVryq446YjtH2kJyNh4rab0%2B%2BIX%2FYwANEUqqg2xi1ZXkk9EaMVBe9eVJlkF2vXn8DFiTk5FjR3%2B%2BfbnPxQmHg%2B6CbeUVIdEx68I6D95NRY9hCXAsOqYieij77dM3GzziWeQrNtO2YgnblYX413L3luuzQ3tsK9VSfiKpPV76TFCmTcEuIgfFC4hyIlpVqObS8Od6sTrwRg1ws%2FS6%2FmX1EWydcCMBfIWBYIKaEBiHMn7SM8ZA0WnNiSgyntpQb52aDfY8DBgKxlDtfx7R9w6vb9Q9iXOLJz5xiUQKiLBgYZgK1VZCS4lKQHjPSoEZQfUIjV%2B6%2BNTLS%2BfLtrk4%2FSK4ZfjFG2WN3qZtGI0DKipdUexvNXu9SWhMjTJ0CaN%2FSJcAKLO0OjJhm%2FnyBsQRcHM%2Fhqb5EH9zCkILmANiKR%2FYAKJohiEkjL4z9ntA6slL6XxZ8eFAB04t1AcyzxE4GB3vJ1KAScxti4LlVdlnI5qj%2FVm8h6YRGRZIMJ3f7bwGOqUBUL7Ih7b5mSZVxX1wTWoP0RdV6PPFX2%2FncTy94LTWqzkZ29k8Ob%2FAmxSzf1nBl3O13fdUYxrE3x%2FxkNCGqT7AYhOiegiqOr758C6H3bASlFHYEURH33OcQFZV3ObQu3gftfkHp%2BuoidXCtMwsrR3NaTNEgLeREqvNcP2DE1dC7uDs2xyOjzH4zf0JU4lgdwMWCZ5k1DHGtoaDUZsJ6k6J10OOaPv%2B&X-Amz-Signature=4f25b26c0bfad5ec599e4d14bb1ddb897ec275a7a35a9b7bca44a10bb5411218&X-Amz-SignedHeaders=host&x-id=GetObject)
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


