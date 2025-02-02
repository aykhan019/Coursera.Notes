

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROJ4V46H%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGhhQ%2Fu7Cp8r7U%2FvGQqKKE%2BUvO%2BbgzTOT9Cgl7t2tYS1AiAVBOQA4HjfNsI4mruzfK3fcDZ0iYV9T4%2F2n95Vw%2FSkEiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUgkDEOMAsDwSVXTNKtwD%2BViSVCQFvpcRGY2ADna8iJzMzqKN4kp8q0ZgE658eMapfIuxaxfYq7enh2SlnvZEqCVG%2F%2BxUbNi7y6VhKrN8z0C0R5vyklYGn3vPOjB%2B2zbjDhpGp%2B8RpVa7kq%2BHGydjr6ihGXJT%2Bvza8fIAjaZZFobf2nUyzqajm7J0hWaqVZtkg0ijuDl1K0uE3rf0PRbUzJwT7GU2uN5R8v4mqxBQ7oOtOwRd%2BPqMkhFMfnM5WyGPdofueLGNcUcuwQKzc9DnTpJ1FpYcuq07MyoKl55uLGHsApJQ1%2BaCOopb%2FqMfLJP0RdLoYJ8k2oEyh6MH5HYC0dX2Ap1dR5G%2BvFnRPQkmrxEivEg1c05i%2B6s5jAf355cbNJ3dczAXRQEBEjZrpK%2BX03R0MXtudTl6%2F4rToiRIlQCy6BGZjCoS5kwUfKzGS4Dy6lNq4CZf4UDqFmqIlyDPVAKZnovGnGycN8mIUrubQN85zgU0JtkEKbyK%2BJR3uOAsXaV%2Fy2ZyJ%2BrDN%2F2gjF9kYvEkxVxDIEKNEkQoW5hPkEL%2B0Xd0fOTYHoJqjLbFZR9dFbSTQ0OvsLezPzheHJw4XMhdocfxuS3P5l967aeAPqj5D%2BRSKSwnqPEH%2Bo%2F9Q7YQg1qRRapggcSblFUwiML9vAY6pgGxXXZnd13XTqpy5pAM6yvM81gZfkD9QuTnCQWh7qxCWQcxxM831FXZpfRNQOp84ANWyZPsQdKuR0x6xhy1D8tdUCXsK%2FE%2BS9dlj4krrtQ8FsPw8Z1k14hZLXyxwSPcevRk05fA%2B3H5oLIvtTUkrN1arUueFym3GyR9LIgIdShI4RYT9Cj6DadknDyXBpXvDzrJH7UXIUdoi3%2BQ%2BNkeCPOKlBupyjur&X-Amz-Signature=8ab6cefa81126bf519410d911bb88ec99f25dc276aea74f7e645f639e157dd0d&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KCRT5TT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHlwockQyLO92nTSzVYiuLEJh5sQEfljQYvaXVOUAqxwIgQNLUqzLxXQAjauorw8TliI5K%2BDllk1l8uEGkNGs3o%2FkqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDG8aMEJmKnQJlfw5ircA%2FJQxyzxKOxRiv0ELxgMH1b0svDqXyPS4PQNPuPxIwKkXr8CotmOCElO13DikET%2F3GOeGmDmVJLMOupx1VK%2BiUkaY4PX6ZHZa6hHg%2BdycwkqE2WxSEgXn0HeXC0%2FVZkZz%2B0hENRxGkqZO3y%2BbUUaotxT8sh248OUqIx43fxsgFLdg5fuYssKLkqoFumeMX5BiLVdwdUNygd30uZga1BVFcM%2BPG%2FYTWVyWLAHnz0EtMIi7%2FQG1pubxkOQSQbH0RYAtui%2BnM4Por%2FADKjBWcR7o34oDvqYGTtXWOHckU27zpjHEVvwVP%2BCtlWCRack4XdW2z3zRaNv5D4k9UMjDa%2BwH%2FFsdhjDT6QZxhwE77OnWWp4rmnbkjwysNjRYwzy1uqTx9BY86iBcpDNQFF%2B7fOv%2B3xnzSaCoFELQVniSUk%2Bv6y2CuIihyurWLSFZpaUnKdg2%2FiG2AEp35dotNTd3yzOLiw4ml6ixdB%2BuTt%2B73uAJ9tbScgrbn2nRJcLhWlHTOL2yuXafwnJ%2F8s2lgnw%2FXbWo08IoT5Pjr5uVaZICz83leCnSJDlQAwFEYdbOzLlRIBqGnHRB0YuAmN2uCkyGJw1iIUGRzDCZMGIb0FlDYKuHYvUigJxxaJmPs07p31FMOW%2F%2FbwGOqUBpOsOdz%2BmFy8ftFQITnXMuA6yk%2F5smuRuRMjgo6PdcMqYiCzbJM6zQMQX%2FQcVWnGPWBMxpYIvrHMzb3BlziLiOphziwNVx9F8AaA%2FxpjSvebqmd7R26ZGVpV2QzG5r7UZ9qPzR62rJBjd2JOcZ8WdtNb%2BlODoPqiOBd5po9d4RMPVmznRQNs41Lq%2Fi42vjP%2BjpeFmxiaQ3zDbTeLLazz5p0DYVWbz&X-Amz-Signature=90c60c1c2da26379a29f81c1b2bac5c4991dcadd3fe8d1b4f63351591f545256&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KCRT5TT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHlwockQyLO92nTSzVYiuLEJh5sQEfljQYvaXVOUAqxwIgQNLUqzLxXQAjauorw8TliI5K%2BDllk1l8uEGkNGs3o%2FkqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDG8aMEJmKnQJlfw5ircA%2FJQxyzxKOxRiv0ELxgMH1b0svDqXyPS4PQNPuPxIwKkXr8CotmOCElO13DikET%2F3GOeGmDmVJLMOupx1VK%2BiUkaY4PX6ZHZa6hHg%2BdycwkqE2WxSEgXn0HeXC0%2FVZkZz%2B0hENRxGkqZO3y%2BbUUaotxT8sh248OUqIx43fxsgFLdg5fuYssKLkqoFumeMX5BiLVdwdUNygd30uZga1BVFcM%2BPG%2FYTWVyWLAHnz0EtMIi7%2FQG1pubxkOQSQbH0RYAtui%2BnM4Por%2FADKjBWcR7o34oDvqYGTtXWOHckU27zpjHEVvwVP%2BCtlWCRack4XdW2z3zRaNv5D4k9UMjDa%2BwH%2FFsdhjDT6QZxhwE77OnWWp4rmnbkjwysNjRYwzy1uqTx9BY86iBcpDNQFF%2B7fOv%2B3xnzSaCoFELQVniSUk%2Bv6y2CuIihyurWLSFZpaUnKdg2%2FiG2AEp35dotNTd3yzOLiw4ml6ixdB%2BuTt%2B73uAJ9tbScgrbn2nRJcLhWlHTOL2yuXafwnJ%2F8s2lgnw%2FXbWo08IoT5Pjr5uVaZICz83leCnSJDlQAwFEYdbOzLlRIBqGnHRB0YuAmN2uCkyGJw1iIUGRzDCZMGIb0FlDYKuHYvUigJxxaJmPs07p31FMOW%2F%2FbwGOqUBpOsOdz%2BmFy8ftFQITnXMuA6yk%2F5smuRuRMjgo6PdcMqYiCzbJM6zQMQX%2FQcVWnGPWBMxpYIvrHMzb3BlziLiOphziwNVx9F8AaA%2FxpjSvebqmd7R26ZGVpV2QzG5r7UZ9qPzR62rJBjd2JOcZ8WdtNb%2BlODoPqiOBd5po9d4RMPVmznRQNs41Lq%2Fi42vjP%2BjpeFmxiaQ3zDbTeLLazz5p0DYVWbz&X-Amz-Signature=2f490a04fad4f5becaa79276f7c48716447c5352601ee687806e07cc57019d59&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KCRT5TT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHlwockQyLO92nTSzVYiuLEJh5sQEfljQYvaXVOUAqxwIgQNLUqzLxXQAjauorw8TliI5K%2BDllk1l8uEGkNGs3o%2FkqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDG8aMEJmKnQJlfw5ircA%2FJQxyzxKOxRiv0ELxgMH1b0svDqXyPS4PQNPuPxIwKkXr8CotmOCElO13DikET%2F3GOeGmDmVJLMOupx1VK%2BiUkaY4PX6ZHZa6hHg%2BdycwkqE2WxSEgXn0HeXC0%2FVZkZz%2B0hENRxGkqZO3y%2BbUUaotxT8sh248OUqIx43fxsgFLdg5fuYssKLkqoFumeMX5BiLVdwdUNygd30uZga1BVFcM%2BPG%2FYTWVyWLAHnz0EtMIi7%2FQG1pubxkOQSQbH0RYAtui%2BnM4Por%2FADKjBWcR7o34oDvqYGTtXWOHckU27zpjHEVvwVP%2BCtlWCRack4XdW2z3zRaNv5D4k9UMjDa%2BwH%2FFsdhjDT6QZxhwE77OnWWp4rmnbkjwysNjRYwzy1uqTx9BY86iBcpDNQFF%2B7fOv%2B3xnzSaCoFELQVniSUk%2Bv6y2CuIihyurWLSFZpaUnKdg2%2FiG2AEp35dotNTd3yzOLiw4ml6ixdB%2BuTt%2B73uAJ9tbScgrbn2nRJcLhWlHTOL2yuXafwnJ%2F8s2lgnw%2FXbWo08IoT5Pjr5uVaZICz83leCnSJDlQAwFEYdbOzLlRIBqGnHRB0YuAmN2uCkyGJw1iIUGRzDCZMGIb0FlDYKuHYvUigJxxaJmPs07p31FMOW%2F%2FbwGOqUBpOsOdz%2BmFy8ftFQITnXMuA6yk%2F5smuRuRMjgo6PdcMqYiCzbJM6zQMQX%2FQcVWnGPWBMxpYIvrHMzb3BlziLiOphziwNVx9F8AaA%2FxpjSvebqmd7R26ZGVpV2QzG5r7UZ9qPzR62rJBjd2JOcZ8WdtNb%2BlODoPqiOBd5po9d4RMPVmznRQNs41Lq%2Fi42vjP%2BjpeFmxiaQ3zDbTeLLazz5p0DYVWbz&X-Amz-Signature=d3a1ae8699c7312ff7dbb108a4a7c8ed26c73c81e2b8a52ee463091ea7c31ef1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KCRT5TT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHlwockQyLO92nTSzVYiuLEJh5sQEfljQYvaXVOUAqxwIgQNLUqzLxXQAjauorw8TliI5K%2BDllk1l8uEGkNGs3o%2FkqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDG8aMEJmKnQJlfw5ircA%2FJQxyzxKOxRiv0ELxgMH1b0svDqXyPS4PQNPuPxIwKkXr8CotmOCElO13DikET%2F3GOeGmDmVJLMOupx1VK%2BiUkaY4PX6ZHZa6hHg%2BdycwkqE2WxSEgXn0HeXC0%2FVZkZz%2B0hENRxGkqZO3y%2BbUUaotxT8sh248OUqIx43fxsgFLdg5fuYssKLkqoFumeMX5BiLVdwdUNygd30uZga1BVFcM%2BPG%2FYTWVyWLAHnz0EtMIi7%2FQG1pubxkOQSQbH0RYAtui%2BnM4Por%2FADKjBWcR7o34oDvqYGTtXWOHckU27zpjHEVvwVP%2BCtlWCRack4XdW2z3zRaNv5D4k9UMjDa%2BwH%2FFsdhjDT6QZxhwE77OnWWp4rmnbkjwysNjRYwzy1uqTx9BY86iBcpDNQFF%2B7fOv%2B3xnzSaCoFELQVniSUk%2Bv6y2CuIihyurWLSFZpaUnKdg2%2FiG2AEp35dotNTd3yzOLiw4ml6ixdB%2BuTt%2B73uAJ9tbScgrbn2nRJcLhWlHTOL2yuXafwnJ%2F8s2lgnw%2FXbWo08IoT5Pjr5uVaZICz83leCnSJDlQAwFEYdbOzLlRIBqGnHRB0YuAmN2uCkyGJw1iIUGRzDCZMGIb0FlDYKuHYvUigJxxaJmPs07p31FMOW%2F%2FbwGOqUBpOsOdz%2BmFy8ftFQITnXMuA6yk%2F5smuRuRMjgo6PdcMqYiCzbJM6zQMQX%2FQcVWnGPWBMxpYIvrHMzb3BlziLiOphziwNVx9F8AaA%2FxpjSvebqmd7R26ZGVpV2QzG5r7UZ9qPzR62rJBjd2JOcZ8WdtNb%2BlODoPqiOBd5po9d4RMPVmznRQNs41Lq%2Fi42vjP%2BjpeFmxiaQ3zDbTeLLazz5p0DYVWbz&X-Amz-Signature=523ae3a68c3b2d507bdcdca697e769d4d89c27410c38f623bb44d3b4643f52a2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KCRT5TT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHlwockQyLO92nTSzVYiuLEJh5sQEfljQYvaXVOUAqxwIgQNLUqzLxXQAjauorw8TliI5K%2BDllk1l8uEGkNGs3o%2FkqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDG8aMEJmKnQJlfw5ircA%2FJQxyzxKOxRiv0ELxgMH1b0svDqXyPS4PQNPuPxIwKkXr8CotmOCElO13DikET%2F3GOeGmDmVJLMOupx1VK%2BiUkaY4PX6ZHZa6hHg%2BdycwkqE2WxSEgXn0HeXC0%2FVZkZz%2B0hENRxGkqZO3y%2BbUUaotxT8sh248OUqIx43fxsgFLdg5fuYssKLkqoFumeMX5BiLVdwdUNygd30uZga1BVFcM%2BPG%2FYTWVyWLAHnz0EtMIi7%2FQG1pubxkOQSQbH0RYAtui%2BnM4Por%2FADKjBWcR7o34oDvqYGTtXWOHckU27zpjHEVvwVP%2BCtlWCRack4XdW2z3zRaNv5D4k9UMjDa%2BwH%2FFsdhjDT6QZxhwE77OnWWp4rmnbkjwysNjRYwzy1uqTx9BY86iBcpDNQFF%2B7fOv%2B3xnzSaCoFELQVniSUk%2Bv6y2CuIihyurWLSFZpaUnKdg2%2FiG2AEp35dotNTd3yzOLiw4ml6ixdB%2BuTt%2B73uAJ9tbScgrbn2nRJcLhWlHTOL2yuXafwnJ%2F8s2lgnw%2FXbWo08IoT5Pjr5uVaZICz83leCnSJDlQAwFEYdbOzLlRIBqGnHRB0YuAmN2uCkyGJw1iIUGRzDCZMGIb0FlDYKuHYvUigJxxaJmPs07p31FMOW%2F%2FbwGOqUBpOsOdz%2BmFy8ftFQITnXMuA6yk%2F5smuRuRMjgo6PdcMqYiCzbJM6zQMQX%2FQcVWnGPWBMxpYIvrHMzb3BlziLiOphziwNVx9F8AaA%2FxpjSvebqmd7R26ZGVpV2QzG5r7UZ9qPzR62rJBjd2JOcZ8WdtNb%2BlODoPqiOBd5po9d4RMPVmznRQNs41Lq%2Fi42vjP%2BjpeFmxiaQ3zDbTeLLazz5p0DYVWbz&X-Amz-Signature=5d843093eaf7b14e7b7b6fa3d9cb14bd756ed9bee208eecfd95b4ba807307d83&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROJ4V46H%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGhhQ%2Fu7Cp8r7U%2FvGQqKKE%2BUvO%2BbgzTOT9Cgl7t2tYS1AiAVBOQA4HjfNsI4mruzfK3fcDZ0iYV9T4%2F2n95Vw%2FSkEiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUgkDEOMAsDwSVXTNKtwD%2BViSVCQFvpcRGY2ADna8iJzMzqKN4kp8q0ZgE658eMapfIuxaxfYq7enh2SlnvZEqCVG%2F%2BxUbNi7y6VhKrN8z0C0R5vyklYGn3vPOjB%2B2zbjDhpGp%2B8RpVa7kq%2BHGydjr6ihGXJT%2Bvza8fIAjaZZFobf2nUyzqajm7J0hWaqVZtkg0ijuDl1K0uE3rf0PRbUzJwT7GU2uN5R8v4mqxBQ7oOtOwRd%2BPqMkhFMfnM5WyGPdofueLGNcUcuwQKzc9DnTpJ1FpYcuq07MyoKl55uLGHsApJQ1%2BaCOopb%2FqMfLJP0RdLoYJ8k2oEyh6MH5HYC0dX2Ap1dR5G%2BvFnRPQkmrxEivEg1c05i%2B6s5jAf355cbNJ3dczAXRQEBEjZrpK%2BX03R0MXtudTl6%2F4rToiRIlQCy6BGZjCoS5kwUfKzGS4Dy6lNq4CZf4UDqFmqIlyDPVAKZnovGnGycN8mIUrubQN85zgU0JtkEKbyK%2BJR3uOAsXaV%2Fy2ZyJ%2BrDN%2F2gjF9kYvEkxVxDIEKNEkQoW5hPkEL%2B0Xd0fOTYHoJqjLbFZR9dFbSTQ0OvsLezPzheHJw4XMhdocfxuS3P5l967aeAPqj5D%2BRSKSwnqPEH%2Bo%2F9Q7YQg1qRRapggcSblFUwiML9vAY6pgGxXXZnd13XTqpy5pAM6yvM81gZfkD9QuTnCQWh7qxCWQcxxM831FXZpfRNQOp84ANWyZPsQdKuR0x6xhy1D8tdUCXsK%2FE%2BS9dlj4krrtQ8FsPw8Z1k14hZLXyxwSPcevRk05fA%2B3H5oLIvtTUkrN1arUueFym3GyR9LIgIdShI4RYT9Cj6DadknDyXBpXvDzrJH7UXIUdoi3%2BQ%2BNkeCPOKlBupyjur&X-Amz-Signature=47dee91b207b5c5a9be8b213627ab3e4618bb9b5c9c6196f951d8e7419c53866&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROJ4V46H%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGhhQ%2Fu7Cp8r7U%2FvGQqKKE%2BUvO%2BbgzTOT9Cgl7t2tYS1AiAVBOQA4HjfNsI4mruzfK3fcDZ0iYV9T4%2F2n95Vw%2FSkEiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUgkDEOMAsDwSVXTNKtwD%2BViSVCQFvpcRGY2ADna8iJzMzqKN4kp8q0ZgE658eMapfIuxaxfYq7enh2SlnvZEqCVG%2F%2BxUbNi7y6VhKrN8z0C0R5vyklYGn3vPOjB%2B2zbjDhpGp%2B8RpVa7kq%2BHGydjr6ihGXJT%2Bvza8fIAjaZZFobf2nUyzqajm7J0hWaqVZtkg0ijuDl1K0uE3rf0PRbUzJwT7GU2uN5R8v4mqxBQ7oOtOwRd%2BPqMkhFMfnM5WyGPdofueLGNcUcuwQKzc9DnTpJ1FpYcuq07MyoKl55uLGHsApJQ1%2BaCOopb%2FqMfLJP0RdLoYJ8k2oEyh6MH5HYC0dX2Ap1dR5G%2BvFnRPQkmrxEivEg1c05i%2B6s5jAf355cbNJ3dczAXRQEBEjZrpK%2BX03R0MXtudTl6%2F4rToiRIlQCy6BGZjCoS5kwUfKzGS4Dy6lNq4CZf4UDqFmqIlyDPVAKZnovGnGycN8mIUrubQN85zgU0JtkEKbyK%2BJR3uOAsXaV%2Fy2ZyJ%2BrDN%2F2gjF9kYvEkxVxDIEKNEkQoW5hPkEL%2B0Xd0fOTYHoJqjLbFZR9dFbSTQ0OvsLezPzheHJw4XMhdocfxuS3P5l967aeAPqj5D%2BRSKSwnqPEH%2Bo%2F9Q7YQg1qRRapggcSblFUwiML9vAY6pgGxXXZnd13XTqpy5pAM6yvM81gZfkD9QuTnCQWh7qxCWQcxxM831FXZpfRNQOp84ANWyZPsQdKuR0x6xhy1D8tdUCXsK%2FE%2BS9dlj4krrtQ8FsPw8Z1k14hZLXyxwSPcevRk05fA%2B3H5oLIvtTUkrN1arUueFym3GyR9LIgIdShI4RYT9Cj6DadknDyXBpXvDzrJH7UXIUdoi3%2BQ%2BNkeCPOKlBupyjur&X-Amz-Signature=b82e63afdd4c15fdaebaa092ca484a9133133fcc6079fc1fb463272903ccaa7b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROJ4V46H%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGhhQ%2Fu7Cp8r7U%2FvGQqKKE%2BUvO%2BbgzTOT9Cgl7t2tYS1AiAVBOQA4HjfNsI4mruzfK3fcDZ0iYV9T4%2F2n95Vw%2FSkEiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUgkDEOMAsDwSVXTNKtwD%2BViSVCQFvpcRGY2ADna8iJzMzqKN4kp8q0ZgE658eMapfIuxaxfYq7enh2SlnvZEqCVG%2F%2BxUbNi7y6VhKrN8z0C0R5vyklYGn3vPOjB%2B2zbjDhpGp%2B8RpVa7kq%2BHGydjr6ihGXJT%2Bvza8fIAjaZZFobf2nUyzqajm7J0hWaqVZtkg0ijuDl1K0uE3rf0PRbUzJwT7GU2uN5R8v4mqxBQ7oOtOwRd%2BPqMkhFMfnM5WyGPdofueLGNcUcuwQKzc9DnTpJ1FpYcuq07MyoKl55uLGHsApJQ1%2BaCOopb%2FqMfLJP0RdLoYJ8k2oEyh6MH5HYC0dX2Ap1dR5G%2BvFnRPQkmrxEivEg1c05i%2B6s5jAf355cbNJ3dczAXRQEBEjZrpK%2BX03R0MXtudTl6%2F4rToiRIlQCy6BGZjCoS5kwUfKzGS4Dy6lNq4CZf4UDqFmqIlyDPVAKZnovGnGycN8mIUrubQN85zgU0JtkEKbyK%2BJR3uOAsXaV%2Fy2ZyJ%2BrDN%2F2gjF9kYvEkxVxDIEKNEkQoW5hPkEL%2B0Xd0fOTYHoJqjLbFZR9dFbSTQ0OvsLezPzheHJw4XMhdocfxuS3P5l967aeAPqj5D%2BRSKSwnqPEH%2Bo%2F9Q7YQg1qRRapggcSblFUwiML9vAY6pgGxXXZnd13XTqpy5pAM6yvM81gZfkD9QuTnCQWh7qxCWQcxxM831FXZpfRNQOp84ANWyZPsQdKuR0x6xhy1D8tdUCXsK%2FE%2BS9dlj4krrtQ8FsPw8Z1k14hZLXyxwSPcevRk05fA%2B3H5oLIvtTUkrN1arUueFym3GyR9LIgIdShI4RYT9Cj6DadknDyXBpXvDzrJH7UXIUdoi3%2BQ%2BNkeCPOKlBupyjur&X-Amz-Signature=b30f375e68d37dad97efb4f9fdf8711df3b076548836bf9937303ac66c78f999&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROJ4V46H%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGhhQ%2Fu7Cp8r7U%2FvGQqKKE%2BUvO%2BbgzTOT9Cgl7t2tYS1AiAVBOQA4HjfNsI4mruzfK3fcDZ0iYV9T4%2F2n95Vw%2FSkEiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUgkDEOMAsDwSVXTNKtwD%2BViSVCQFvpcRGY2ADna8iJzMzqKN4kp8q0ZgE658eMapfIuxaxfYq7enh2SlnvZEqCVG%2F%2BxUbNi7y6VhKrN8z0C0R5vyklYGn3vPOjB%2B2zbjDhpGp%2B8RpVa7kq%2BHGydjr6ihGXJT%2Bvza8fIAjaZZFobf2nUyzqajm7J0hWaqVZtkg0ijuDl1K0uE3rf0PRbUzJwT7GU2uN5R8v4mqxBQ7oOtOwRd%2BPqMkhFMfnM5WyGPdofueLGNcUcuwQKzc9DnTpJ1FpYcuq07MyoKl55uLGHsApJQ1%2BaCOopb%2FqMfLJP0RdLoYJ8k2oEyh6MH5HYC0dX2Ap1dR5G%2BvFnRPQkmrxEivEg1c05i%2B6s5jAf355cbNJ3dczAXRQEBEjZrpK%2BX03R0MXtudTl6%2F4rToiRIlQCy6BGZjCoS5kwUfKzGS4Dy6lNq4CZf4UDqFmqIlyDPVAKZnovGnGycN8mIUrubQN85zgU0JtkEKbyK%2BJR3uOAsXaV%2Fy2ZyJ%2BrDN%2F2gjF9kYvEkxVxDIEKNEkQoW5hPkEL%2B0Xd0fOTYHoJqjLbFZR9dFbSTQ0OvsLezPzheHJw4XMhdocfxuS3P5l967aeAPqj5D%2BRSKSwnqPEH%2Bo%2F9Q7YQg1qRRapggcSblFUwiML9vAY6pgGxXXZnd13XTqpy5pAM6yvM81gZfkD9QuTnCQWh7qxCWQcxxM831FXZpfRNQOp84ANWyZPsQdKuR0x6xhy1D8tdUCXsK%2FE%2BS9dlj4krrtQ8FsPw8Z1k14hZLXyxwSPcevRk05fA%2B3H5oLIvtTUkrN1arUueFym3GyR9LIgIdShI4RYT9Cj6DadknDyXBpXvDzrJH7UXIUdoi3%2BQ%2BNkeCPOKlBupyjur&X-Amz-Signature=df16022ae90a415c56cd93a793028c122f9a8d7b8ecd00b25e237507296e608d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROJ4V46H%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGhhQ%2Fu7Cp8r7U%2FvGQqKKE%2BUvO%2BbgzTOT9Cgl7t2tYS1AiAVBOQA4HjfNsI4mruzfK3fcDZ0iYV9T4%2F2n95Vw%2FSkEiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUgkDEOMAsDwSVXTNKtwD%2BViSVCQFvpcRGY2ADna8iJzMzqKN4kp8q0ZgE658eMapfIuxaxfYq7enh2SlnvZEqCVG%2F%2BxUbNi7y6VhKrN8z0C0R5vyklYGn3vPOjB%2B2zbjDhpGp%2B8RpVa7kq%2BHGydjr6ihGXJT%2Bvza8fIAjaZZFobf2nUyzqajm7J0hWaqVZtkg0ijuDl1K0uE3rf0PRbUzJwT7GU2uN5R8v4mqxBQ7oOtOwRd%2BPqMkhFMfnM5WyGPdofueLGNcUcuwQKzc9DnTpJ1FpYcuq07MyoKl55uLGHsApJQ1%2BaCOopb%2FqMfLJP0RdLoYJ8k2oEyh6MH5HYC0dX2Ap1dR5G%2BvFnRPQkmrxEivEg1c05i%2B6s5jAf355cbNJ3dczAXRQEBEjZrpK%2BX03R0MXtudTl6%2F4rToiRIlQCy6BGZjCoS5kwUfKzGS4Dy6lNq4CZf4UDqFmqIlyDPVAKZnovGnGycN8mIUrubQN85zgU0JtkEKbyK%2BJR3uOAsXaV%2Fy2ZyJ%2BrDN%2F2gjF9kYvEkxVxDIEKNEkQoW5hPkEL%2B0Xd0fOTYHoJqjLbFZR9dFbSTQ0OvsLezPzheHJw4XMhdocfxuS3P5l967aeAPqj5D%2BRSKSwnqPEH%2Bo%2F9Q7YQg1qRRapggcSblFUwiML9vAY6pgGxXXZnd13XTqpy5pAM6yvM81gZfkD9QuTnCQWh7qxCWQcxxM831FXZpfRNQOp84ANWyZPsQdKuR0x6xhy1D8tdUCXsK%2FE%2BS9dlj4krrtQ8FsPw8Z1k14hZLXyxwSPcevRk05fA%2B3H5oLIvtTUkrN1arUueFym3GyR9LIgIdShI4RYT9Cj6DadknDyXBpXvDzrJH7UXIUdoi3%2BQ%2BNkeCPOKlBupyjur&X-Amz-Signature=a6946c75fbac8712e54a18cfad69a58dec2cabb18b5f978a6b6ee4612d0d84e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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


