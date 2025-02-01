

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR4RCV6B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDctHtYdIceptsAhWrfQVLbnQOmzWNard0Xx4wJL7XWRQIgX61NNNbaiSQ8RrZtiVHG2HUM%2BP9uiyu7fm0K%2Bvlj0QAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMZKNxf1IQqVhB12NyrcA82%2B0PO5zIhmTdQslzgwxtMZjK3wShBfqr5naOqLFibBEC40OZ9m%2F3rT%2F2Kvcg7yjMWPisJCfwkLSg6RUPW2Tuhxk%2FcZ75rOq8A4%2F0BnBMcpYoDZzFS2jGkZ3UxtpS7nOKhCA%2FWJSKjCfVIIdzXXs1ur8qZOMOD3%2BMu2vDyrecNXv3xuutZeyeNfbCDVzOoRQKhASaDXWf2o032MqH208tfpQuFyCeS1tAd9COr%2F3YB%2FqAnu2qpx3wpLp3gYbBWN%2B4gey%2BYZrK8EZkfVJE09AWgSiH7RCyZqTBO2yi08%2FVmF8E%2BUL%2FAi2WjCetdg3mPIoLT0s14ygN9Khe2%2BNFqjkXqXDJk4RokURl8D1O1Ax325I3ICehe1jPPvV8GQwD1b7Gi%2FcKrN6%2BpRGYyci429HgDCmDHcduEDcPzj9BKX6sTDQmzwqNFuaHV2DGu3ExUFhgPaVGIojtcO8ybg%2BwbnAz0I8HSx%2FUwMA409P26J%2B320MhkhO4qElSub9Q%2FbBP9PmmhRMUiIs8zWzYAo83mqGjNsKHdr5royvJZcS7W4NgLHWuaDU%2BCk2gvgEYhn6bp4ZBX33lx7IRsebfNnhLofV6X2aVxS8ZaK7rNz%2BcXeLTWtGmNeWk15ce3sMOn1MKuk97wGOqUBKfkrtCW5Eb%2BvhE6qwbFtymF7EbsBZuvI1Uq6yifaOPL7YH0MT0XedcopKdyrM3nIWGN%2FoOHxfF8L6HwNv9Xgd1FpUJuO2XuYRNFyamMFPoGAejumvEXpssFxzWr%2Fjf29hEmpIzvd7quE5R7bj%2FtmktELyDadD0briUQAbA9ZNdQXp%2FPv6oKL%2BB6mkD%2B7BPyJLnRHGQRmMYmN8Ozl7Ry1r%2FhOIbgd&X-Amz-Signature=d4980dcf59433202a71347f74e77608281be54aa85871be811eb781ea99705e3&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3J2WIQF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDG987BM0WOy5dlkKfK8HHddEyxlQGqgHs%2FPVDKQe%2FOTAIhAJ7NOHns%2F06H%2BtCkBxPU9aNdlxMVsgHbqdl4lOPuXLbRKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzbmkFMZTN5UfrrHioq3APyYqbLe%2BNv0H9TsrSNmBdpb%2B8SLqr9Qnog8KnUqs2YuAKUH2c8m7pazXC5E1wY4%2BHBPg%2B6nO5Civ6u8XrPBqQRAXujp92P2s0EJXs0AsENSouBkg3foqyiMoZGCfn%2FqneCwq48Ij%2FpcP0D9vkB%2FybmwtLb1OOCY%2FHTS25idUGdIZZ%2BPClJmDQDPAFougmwjiq2Lkj%2B%2FTaEC9EyiW36J3HRY5vBvWIo6nafB1NnPaND1jHzBMigjuH1HNW%2FK5WdyrX3%2F1%2BDDWc%2FNii7l0J3G3YZ5iHr%2BawuG%2BziIGYk6ED5oHeHz2mc%2BqTniKv4YuhiTx5LPb1mZvFlQ%2FSNzUUOQFMQMO0wI0Dsj5R9v6q1qDxjxzEILcWabBUsL6yhqG9TfN%2BBXuubGjS0dhfs9oEPW7R%2FC2A4zBKhlbK%2FIhhKYCxirz5d4l3hPQnaopnjXdWbGZFzWqgH6GfFaGWJRDH4Ax9qiGfUrGEldL%2F2srE736jnT3Sc%2FbaRs97uGOXTB4Kc8%2FKh8qctLoeliBt0EtgAAqe%2F6IEsbiRtS8aZ5hs8WoSb4dpBhTIBDDOshuLLaVdvFIB2uP0tXbZivLBF4pfZUJnRaaCjQBAHf8jnNpixanXadxskxpbPrhs4bdC8cjC9pPe8BjqkAVI4n2MxsWdRtb%2FG2WnRE%2F5h8KemxQ%2Fkk0iioPACr09e0gPuWGiQAyH7vvIr137bnZ%2Fcy7Gt4Eq1pHUWju1ZPHIQtzTSe%2BQt48pnjwuXF4QriNO%2FZUZ8agYsXHOQZ2rtqHp2cEEqP%2BeraO%2B6YTUVWeIE6vWSN4miMe27anyIlb2pMX796X7QzhE0WyJBCkRk1zEHnxP1zP90Xnasv7FP7BB%2FsOd8&X-Amz-Signature=c87becaa7593551908d086fec4c12d9784ce088abe1d668e1336ac08fe7261ce&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3J2WIQF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDG987BM0WOy5dlkKfK8HHddEyxlQGqgHs%2FPVDKQe%2FOTAIhAJ7NOHns%2F06H%2BtCkBxPU9aNdlxMVsgHbqdl4lOPuXLbRKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzbmkFMZTN5UfrrHioq3APyYqbLe%2BNv0H9TsrSNmBdpb%2B8SLqr9Qnog8KnUqs2YuAKUH2c8m7pazXC5E1wY4%2BHBPg%2B6nO5Civ6u8XrPBqQRAXujp92P2s0EJXs0AsENSouBkg3foqyiMoZGCfn%2FqneCwq48Ij%2FpcP0D9vkB%2FybmwtLb1OOCY%2FHTS25idUGdIZZ%2BPClJmDQDPAFougmwjiq2Lkj%2B%2FTaEC9EyiW36J3HRY5vBvWIo6nafB1NnPaND1jHzBMigjuH1HNW%2FK5WdyrX3%2F1%2BDDWc%2FNii7l0J3G3YZ5iHr%2BawuG%2BziIGYk6ED5oHeHz2mc%2BqTniKv4YuhiTx5LPb1mZvFlQ%2FSNzUUOQFMQMO0wI0Dsj5R9v6q1qDxjxzEILcWabBUsL6yhqG9TfN%2BBXuubGjS0dhfs9oEPW7R%2FC2A4zBKhlbK%2FIhhKYCxirz5d4l3hPQnaopnjXdWbGZFzWqgH6GfFaGWJRDH4Ax9qiGfUrGEldL%2F2srE736jnT3Sc%2FbaRs97uGOXTB4Kc8%2FKh8qctLoeliBt0EtgAAqe%2F6IEsbiRtS8aZ5hs8WoSb4dpBhTIBDDOshuLLaVdvFIB2uP0tXbZivLBF4pfZUJnRaaCjQBAHf8jnNpixanXadxskxpbPrhs4bdC8cjC9pPe8BjqkAVI4n2MxsWdRtb%2FG2WnRE%2F5h8KemxQ%2Fkk0iioPACr09e0gPuWGiQAyH7vvIr137bnZ%2Fcy7Gt4Eq1pHUWju1ZPHIQtzTSe%2BQt48pnjwuXF4QriNO%2FZUZ8agYsXHOQZ2rtqHp2cEEqP%2BeraO%2B6YTUVWeIE6vWSN4miMe27anyIlb2pMX796X7QzhE0WyJBCkRk1zEHnxP1zP90Xnasv7FP7BB%2FsOd8&X-Amz-Signature=27ca58391c2f631c722d40dfef9ab3d0590c265efeeb0569ee2cd23112bca189&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3J2WIQF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDG987BM0WOy5dlkKfK8HHddEyxlQGqgHs%2FPVDKQe%2FOTAIhAJ7NOHns%2F06H%2BtCkBxPU9aNdlxMVsgHbqdl4lOPuXLbRKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzbmkFMZTN5UfrrHioq3APyYqbLe%2BNv0H9TsrSNmBdpb%2B8SLqr9Qnog8KnUqs2YuAKUH2c8m7pazXC5E1wY4%2BHBPg%2B6nO5Civ6u8XrPBqQRAXujp92P2s0EJXs0AsENSouBkg3foqyiMoZGCfn%2FqneCwq48Ij%2FpcP0D9vkB%2FybmwtLb1OOCY%2FHTS25idUGdIZZ%2BPClJmDQDPAFougmwjiq2Lkj%2B%2FTaEC9EyiW36J3HRY5vBvWIo6nafB1NnPaND1jHzBMigjuH1HNW%2FK5WdyrX3%2F1%2BDDWc%2FNii7l0J3G3YZ5iHr%2BawuG%2BziIGYk6ED5oHeHz2mc%2BqTniKv4YuhiTx5LPb1mZvFlQ%2FSNzUUOQFMQMO0wI0Dsj5R9v6q1qDxjxzEILcWabBUsL6yhqG9TfN%2BBXuubGjS0dhfs9oEPW7R%2FC2A4zBKhlbK%2FIhhKYCxirz5d4l3hPQnaopnjXdWbGZFzWqgH6GfFaGWJRDH4Ax9qiGfUrGEldL%2F2srE736jnT3Sc%2FbaRs97uGOXTB4Kc8%2FKh8qctLoeliBt0EtgAAqe%2F6IEsbiRtS8aZ5hs8WoSb4dpBhTIBDDOshuLLaVdvFIB2uP0tXbZivLBF4pfZUJnRaaCjQBAHf8jnNpixanXadxskxpbPrhs4bdC8cjC9pPe8BjqkAVI4n2MxsWdRtb%2FG2WnRE%2F5h8KemxQ%2Fkk0iioPACr09e0gPuWGiQAyH7vvIr137bnZ%2Fcy7Gt4Eq1pHUWju1ZPHIQtzTSe%2BQt48pnjwuXF4QriNO%2FZUZ8agYsXHOQZ2rtqHp2cEEqP%2BeraO%2B6YTUVWeIE6vWSN4miMe27anyIlb2pMX796X7QzhE0WyJBCkRk1zEHnxP1zP90Xnasv7FP7BB%2FsOd8&X-Amz-Signature=a808b944eeab1a499c33ab19cc15f1b4f9977b8492c30f9c363544998c6c75cf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3J2WIQF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDG987BM0WOy5dlkKfK8HHddEyxlQGqgHs%2FPVDKQe%2FOTAIhAJ7NOHns%2F06H%2BtCkBxPU9aNdlxMVsgHbqdl4lOPuXLbRKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzbmkFMZTN5UfrrHioq3APyYqbLe%2BNv0H9TsrSNmBdpb%2B8SLqr9Qnog8KnUqs2YuAKUH2c8m7pazXC5E1wY4%2BHBPg%2B6nO5Civ6u8XrPBqQRAXujp92P2s0EJXs0AsENSouBkg3foqyiMoZGCfn%2FqneCwq48Ij%2FpcP0D9vkB%2FybmwtLb1OOCY%2FHTS25idUGdIZZ%2BPClJmDQDPAFougmwjiq2Lkj%2B%2FTaEC9EyiW36J3HRY5vBvWIo6nafB1NnPaND1jHzBMigjuH1HNW%2FK5WdyrX3%2F1%2BDDWc%2FNii7l0J3G3YZ5iHr%2BawuG%2BziIGYk6ED5oHeHz2mc%2BqTniKv4YuhiTx5LPb1mZvFlQ%2FSNzUUOQFMQMO0wI0Dsj5R9v6q1qDxjxzEILcWabBUsL6yhqG9TfN%2BBXuubGjS0dhfs9oEPW7R%2FC2A4zBKhlbK%2FIhhKYCxirz5d4l3hPQnaopnjXdWbGZFzWqgH6GfFaGWJRDH4Ax9qiGfUrGEldL%2F2srE736jnT3Sc%2FbaRs97uGOXTB4Kc8%2FKh8qctLoeliBt0EtgAAqe%2F6IEsbiRtS8aZ5hs8WoSb4dpBhTIBDDOshuLLaVdvFIB2uP0tXbZivLBF4pfZUJnRaaCjQBAHf8jnNpixanXadxskxpbPrhs4bdC8cjC9pPe8BjqkAVI4n2MxsWdRtb%2FG2WnRE%2F5h8KemxQ%2Fkk0iioPACr09e0gPuWGiQAyH7vvIr137bnZ%2Fcy7Gt4Eq1pHUWju1ZPHIQtzTSe%2BQt48pnjwuXF4QriNO%2FZUZ8agYsXHOQZ2rtqHp2cEEqP%2BeraO%2B6YTUVWeIE6vWSN4miMe27anyIlb2pMX796X7QzhE0WyJBCkRk1zEHnxP1zP90Xnasv7FP7BB%2FsOd8&X-Amz-Signature=3fe4b8851ef86fc949f17dcfb880a2c62894dd7e20109ce4693f3a4b38efe3b9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3J2WIQF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDG987BM0WOy5dlkKfK8HHddEyxlQGqgHs%2FPVDKQe%2FOTAIhAJ7NOHns%2F06H%2BtCkBxPU9aNdlxMVsgHbqdl4lOPuXLbRKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzbmkFMZTN5UfrrHioq3APyYqbLe%2BNv0H9TsrSNmBdpb%2B8SLqr9Qnog8KnUqs2YuAKUH2c8m7pazXC5E1wY4%2BHBPg%2B6nO5Civ6u8XrPBqQRAXujp92P2s0EJXs0AsENSouBkg3foqyiMoZGCfn%2FqneCwq48Ij%2FpcP0D9vkB%2FybmwtLb1OOCY%2FHTS25idUGdIZZ%2BPClJmDQDPAFougmwjiq2Lkj%2B%2FTaEC9EyiW36J3HRY5vBvWIo6nafB1NnPaND1jHzBMigjuH1HNW%2FK5WdyrX3%2F1%2BDDWc%2FNii7l0J3G3YZ5iHr%2BawuG%2BziIGYk6ED5oHeHz2mc%2BqTniKv4YuhiTx5LPb1mZvFlQ%2FSNzUUOQFMQMO0wI0Dsj5R9v6q1qDxjxzEILcWabBUsL6yhqG9TfN%2BBXuubGjS0dhfs9oEPW7R%2FC2A4zBKhlbK%2FIhhKYCxirz5d4l3hPQnaopnjXdWbGZFzWqgH6GfFaGWJRDH4Ax9qiGfUrGEldL%2F2srE736jnT3Sc%2FbaRs97uGOXTB4Kc8%2FKh8qctLoeliBt0EtgAAqe%2F6IEsbiRtS8aZ5hs8WoSb4dpBhTIBDDOshuLLaVdvFIB2uP0tXbZivLBF4pfZUJnRaaCjQBAHf8jnNpixanXadxskxpbPrhs4bdC8cjC9pPe8BjqkAVI4n2MxsWdRtb%2FG2WnRE%2F5h8KemxQ%2Fkk0iioPACr09e0gPuWGiQAyH7vvIr137bnZ%2Fcy7Gt4Eq1pHUWju1ZPHIQtzTSe%2BQt48pnjwuXF4QriNO%2FZUZ8agYsXHOQZ2rtqHp2cEEqP%2BeraO%2B6YTUVWeIE6vWSN4miMe27anyIlb2pMX796X7QzhE0WyJBCkRk1zEHnxP1zP90Xnasv7FP7BB%2FsOd8&X-Amz-Signature=48e3d4c49554505743cf55cddf573fce93bf9c0e1f2bbe184b617826a4bc49ac&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR4RCV6B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDctHtYdIceptsAhWrfQVLbnQOmzWNard0Xx4wJL7XWRQIgX61NNNbaiSQ8RrZtiVHG2HUM%2BP9uiyu7fm0K%2Bvlj0QAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMZKNxf1IQqVhB12NyrcA82%2B0PO5zIhmTdQslzgwxtMZjK3wShBfqr5naOqLFibBEC40OZ9m%2F3rT%2F2Kvcg7yjMWPisJCfwkLSg6RUPW2Tuhxk%2FcZ75rOq8A4%2F0BnBMcpYoDZzFS2jGkZ3UxtpS7nOKhCA%2FWJSKjCfVIIdzXXs1ur8qZOMOD3%2BMu2vDyrecNXv3xuutZeyeNfbCDVzOoRQKhASaDXWf2o032MqH208tfpQuFyCeS1tAd9COr%2F3YB%2FqAnu2qpx3wpLp3gYbBWN%2B4gey%2BYZrK8EZkfVJE09AWgSiH7RCyZqTBO2yi08%2FVmF8E%2BUL%2FAi2WjCetdg3mPIoLT0s14ygN9Khe2%2BNFqjkXqXDJk4RokURl8D1O1Ax325I3ICehe1jPPvV8GQwD1b7Gi%2FcKrN6%2BpRGYyci429HgDCmDHcduEDcPzj9BKX6sTDQmzwqNFuaHV2DGu3ExUFhgPaVGIojtcO8ybg%2BwbnAz0I8HSx%2FUwMA409P26J%2B320MhkhO4qElSub9Q%2FbBP9PmmhRMUiIs8zWzYAo83mqGjNsKHdr5royvJZcS7W4NgLHWuaDU%2BCk2gvgEYhn6bp4ZBX33lx7IRsebfNnhLofV6X2aVxS8ZaK7rNz%2BcXeLTWtGmNeWk15ce3sMOn1MKuk97wGOqUBKfkrtCW5Eb%2BvhE6qwbFtymF7EbsBZuvI1Uq6yifaOPL7YH0MT0XedcopKdyrM3nIWGN%2FoOHxfF8L6HwNv9Xgd1FpUJuO2XuYRNFyamMFPoGAejumvEXpssFxzWr%2Fjf29hEmpIzvd7quE5R7bj%2FtmktELyDadD0briUQAbA9ZNdQXp%2FPv6oKL%2BB6mkD%2B7BPyJLnRHGQRmMYmN8Ozl7Ry1r%2FhOIbgd&X-Amz-Signature=74935d5582e4d81ab9f1726745ec9c7903285d47bed748d5c91c31a5b7ff2191&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR4RCV6B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDctHtYdIceptsAhWrfQVLbnQOmzWNard0Xx4wJL7XWRQIgX61NNNbaiSQ8RrZtiVHG2HUM%2BP9uiyu7fm0K%2Bvlj0QAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMZKNxf1IQqVhB12NyrcA82%2B0PO5zIhmTdQslzgwxtMZjK3wShBfqr5naOqLFibBEC40OZ9m%2F3rT%2F2Kvcg7yjMWPisJCfwkLSg6RUPW2Tuhxk%2FcZ75rOq8A4%2F0BnBMcpYoDZzFS2jGkZ3UxtpS7nOKhCA%2FWJSKjCfVIIdzXXs1ur8qZOMOD3%2BMu2vDyrecNXv3xuutZeyeNfbCDVzOoRQKhASaDXWf2o032MqH208tfpQuFyCeS1tAd9COr%2F3YB%2FqAnu2qpx3wpLp3gYbBWN%2B4gey%2BYZrK8EZkfVJE09AWgSiH7RCyZqTBO2yi08%2FVmF8E%2BUL%2FAi2WjCetdg3mPIoLT0s14ygN9Khe2%2BNFqjkXqXDJk4RokURl8D1O1Ax325I3ICehe1jPPvV8GQwD1b7Gi%2FcKrN6%2BpRGYyci429HgDCmDHcduEDcPzj9BKX6sTDQmzwqNFuaHV2DGu3ExUFhgPaVGIojtcO8ybg%2BwbnAz0I8HSx%2FUwMA409P26J%2B320MhkhO4qElSub9Q%2FbBP9PmmhRMUiIs8zWzYAo83mqGjNsKHdr5royvJZcS7W4NgLHWuaDU%2BCk2gvgEYhn6bp4ZBX33lx7IRsebfNnhLofV6X2aVxS8ZaK7rNz%2BcXeLTWtGmNeWk15ce3sMOn1MKuk97wGOqUBKfkrtCW5Eb%2BvhE6qwbFtymF7EbsBZuvI1Uq6yifaOPL7YH0MT0XedcopKdyrM3nIWGN%2FoOHxfF8L6HwNv9Xgd1FpUJuO2XuYRNFyamMFPoGAejumvEXpssFxzWr%2Fjf29hEmpIzvd7quE5R7bj%2FtmktELyDadD0briUQAbA9ZNdQXp%2FPv6oKL%2BB6mkD%2B7BPyJLnRHGQRmMYmN8Ozl7Ry1r%2FhOIbgd&X-Amz-Signature=6e9141bc0e3fd5222e060cdac076d27b5cc9024cb58a6de50de56d82205b180e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR4RCV6B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDctHtYdIceptsAhWrfQVLbnQOmzWNard0Xx4wJL7XWRQIgX61NNNbaiSQ8RrZtiVHG2HUM%2BP9uiyu7fm0K%2Bvlj0QAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMZKNxf1IQqVhB12NyrcA82%2B0PO5zIhmTdQslzgwxtMZjK3wShBfqr5naOqLFibBEC40OZ9m%2F3rT%2F2Kvcg7yjMWPisJCfwkLSg6RUPW2Tuhxk%2FcZ75rOq8A4%2F0BnBMcpYoDZzFS2jGkZ3UxtpS7nOKhCA%2FWJSKjCfVIIdzXXs1ur8qZOMOD3%2BMu2vDyrecNXv3xuutZeyeNfbCDVzOoRQKhASaDXWf2o032MqH208tfpQuFyCeS1tAd9COr%2F3YB%2FqAnu2qpx3wpLp3gYbBWN%2B4gey%2BYZrK8EZkfVJE09AWgSiH7RCyZqTBO2yi08%2FVmF8E%2BUL%2FAi2WjCetdg3mPIoLT0s14ygN9Khe2%2BNFqjkXqXDJk4RokURl8D1O1Ax325I3ICehe1jPPvV8GQwD1b7Gi%2FcKrN6%2BpRGYyci429HgDCmDHcduEDcPzj9BKX6sTDQmzwqNFuaHV2DGu3ExUFhgPaVGIojtcO8ybg%2BwbnAz0I8HSx%2FUwMA409P26J%2B320MhkhO4qElSub9Q%2FbBP9PmmhRMUiIs8zWzYAo83mqGjNsKHdr5royvJZcS7W4NgLHWuaDU%2BCk2gvgEYhn6bp4ZBX33lx7IRsebfNnhLofV6X2aVxS8ZaK7rNz%2BcXeLTWtGmNeWk15ce3sMOn1MKuk97wGOqUBKfkrtCW5Eb%2BvhE6qwbFtymF7EbsBZuvI1Uq6yifaOPL7YH0MT0XedcopKdyrM3nIWGN%2FoOHxfF8L6HwNv9Xgd1FpUJuO2XuYRNFyamMFPoGAejumvEXpssFxzWr%2Fjf29hEmpIzvd7quE5R7bj%2FtmktELyDadD0briUQAbA9ZNdQXp%2FPv6oKL%2BB6mkD%2B7BPyJLnRHGQRmMYmN8Ozl7Ry1r%2FhOIbgd&X-Amz-Signature=c0c4e88e88ed2269d30493bffcb96dc34fad2ab3d373cfb7c6eac191b3f0fa0a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR4RCV6B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDctHtYdIceptsAhWrfQVLbnQOmzWNard0Xx4wJL7XWRQIgX61NNNbaiSQ8RrZtiVHG2HUM%2BP9uiyu7fm0K%2Bvlj0QAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMZKNxf1IQqVhB12NyrcA82%2B0PO5zIhmTdQslzgwxtMZjK3wShBfqr5naOqLFibBEC40OZ9m%2F3rT%2F2Kvcg7yjMWPisJCfwkLSg6RUPW2Tuhxk%2FcZ75rOq8A4%2F0BnBMcpYoDZzFS2jGkZ3UxtpS7nOKhCA%2FWJSKjCfVIIdzXXs1ur8qZOMOD3%2BMu2vDyrecNXv3xuutZeyeNfbCDVzOoRQKhASaDXWf2o032MqH208tfpQuFyCeS1tAd9COr%2F3YB%2FqAnu2qpx3wpLp3gYbBWN%2B4gey%2BYZrK8EZkfVJE09AWgSiH7RCyZqTBO2yi08%2FVmF8E%2BUL%2FAi2WjCetdg3mPIoLT0s14ygN9Khe2%2BNFqjkXqXDJk4RokURl8D1O1Ax325I3ICehe1jPPvV8GQwD1b7Gi%2FcKrN6%2BpRGYyci429HgDCmDHcduEDcPzj9BKX6sTDQmzwqNFuaHV2DGu3ExUFhgPaVGIojtcO8ybg%2BwbnAz0I8HSx%2FUwMA409P26J%2B320MhkhO4qElSub9Q%2FbBP9PmmhRMUiIs8zWzYAo83mqGjNsKHdr5royvJZcS7W4NgLHWuaDU%2BCk2gvgEYhn6bp4ZBX33lx7IRsebfNnhLofV6X2aVxS8ZaK7rNz%2BcXeLTWtGmNeWk15ce3sMOn1MKuk97wGOqUBKfkrtCW5Eb%2BvhE6qwbFtymF7EbsBZuvI1Uq6yifaOPL7YH0MT0XedcopKdyrM3nIWGN%2FoOHxfF8L6HwNv9Xgd1FpUJuO2XuYRNFyamMFPoGAejumvEXpssFxzWr%2Fjf29hEmpIzvd7quE5R7bj%2FtmktELyDadD0briUQAbA9ZNdQXp%2FPv6oKL%2BB6mkD%2B7BPyJLnRHGQRmMYmN8Ozl7Ry1r%2FhOIbgd&X-Amz-Signature=64f426b397a94bf9f5a98605a5db8a69291b54be045d43f395b39473889bd62b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR4RCV6B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDctHtYdIceptsAhWrfQVLbnQOmzWNard0Xx4wJL7XWRQIgX61NNNbaiSQ8RrZtiVHG2HUM%2BP9uiyu7fm0K%2Bvlj0QAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMZKNxf1IQqVhB12NyrcA82%2B0PO5zIhmTdQslzgwxtMZjK3wShBfqr5naOqLFibBEC40OZ9m%2F3rT%2F2Kvcg7yjMWPisJCfwkLSg6RUPW2Tuhxk%2FcZ75rOq8A4%2F0BnBMcpYoDZzFS2jGkZ3UxtpS7nOKhCA%2FWJSKjCfVIIdzXXs1ur8qZOMOD3%2BMu2vDyrecNXv3xuutZeyeNfbCDVzOoRQKhASaDXWf2o032MqH208tfpQuFyCeS1tAd9COr%2F3YB%2FqAnu2qpx3wpLp3gYbBWN%2B4gey%2BYZrK8EZkfVJE09AWgSiH7RCyZqTBO2yi08%2FVmF8E%2BUL%2FAi2WjCetdg3mPIoLT0s14ygN9Khe2%2BNFqjkXqXDJk4RokURl8D1O1Ax325I3ICehe1jPPvV8GQwD1b7Gi%2FcKrN6%2BpRGYyci429HgDCmDHcduEDcPzj9BKX6sTDQmzwqNFuaHV2DGu3ExUFhgPaVGIojtcO8ybg%2BwbnAz0I8HSx%2FUwMA409P26J%2B320MhkhO4qElSub9Q%2FbBP9PmmhRMUiIs8zWzYAo83mqGjNsKHdr5royvJZcS7W4NgLHWuaDU%2BCk2gvgEYhn6bp4ZBX33lx7IRsebfNnhLofV6X2aVxS8ZaK7rNz%2BcXeLTWtGmNeWk15ce3sMOn1MKuk97wGOqUBKfkrtCW5Eb%2BvhE6qwbFtymF7EbsBZuvI1Uq6yifaOPL7YH0MT0XedcopKdyrM3nIWGN%2FoOHxfF8L6HwNv9Xgd1FpUJuO2XuYRNFyamMFPoGAejumvEXpssFxzWr%2Fjf29hEmpIzvd7quE5R7bj%2FtmktELyDadD0briUQAbA9ZNdQXp%2FPv6oKL%2BB6mkD%2B7BPyJLnRHGQRmMYmN8Ozl7Ry1r%2FhOIbgd&X-Amz-Signature=abf1ba6c5eebe4855a7656762fb158da54ebc010e33dc1f1513e2baea12db2ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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


