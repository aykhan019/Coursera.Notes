

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GNX4AZQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtBcTJoybCPjc6rzW%2F9za%2FUofmJ31todaDn4Pftr7vnAiB0S2wnzzFKenENhOklm74gKIzs6zhx%2Ba7EUEvbh6NySyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9nBv8Us09VPxM%2F%2FuKtwDKafUIBrPBaQYgF7ouZLA9C3u0XUEUG%2Fh7lvSKoxK3%2F9eb3II17tp%2FYIdMpEkSxBbHEeGzZsDDnL9e9JsezRSIpAXf%2B2h%2F02WX3bnrPrxT7k6fRrNcU4%2F2F13Gibz9%2FJ3Ub8sKs9NaZOxcT6tSBUBXYAUVKLURWq8Dnj5jz06M2Tv%2FWeDtHx7mst%2FsZ8C73ErhV%2F0MPMY7xfp%2BmFtXfYk12DjuEQ3d2HwX8J7Dkb%2BlKKVm5pm2Qy6OffFq9h2z3ues3TGa9O3qqoIEvY6MVywbofKu1yHLHB%2Fy1ChS2KGCjZ8KB35uMFLm10HnmZRt%2FfpVBzH5j%2F7R0qMdD2Nw%2FtZ2auZ%2FMzjMOKKRT%2BBE5lQseeLQHM3q6sXDFx4fnU%2FnzPw4Mt%2BLYxntktsiWe44An%2BChX3xNusC0GtpQiFb%2FW6lxSD%2F27fuTeV5fTxFYxafr37bbbIILf9zFZcAG3xxKFFSonrZcV%2BHVKd49QHMaTfii3UZLrK3OL259nWjhDsM2ALDRUjZdU4%2BoFAk9qacS4t8F5X1OhuWy3u0RTDrLm6TbBj9eU1yXInTvdEez0kc1vyhIAQlO6zOOu2SfQIl%2Fv457nU8cTW0Pn%2FIuIw6Ac3wCtg9AjTYX7YEPFBlHkw8L39vAY6pgHPX7cbyXL82dOJI%2BVxBjR9G17yteBxeJq8liZjFQUZVLPw2ZUZZpavP7sOTgYV5C5uFTIm1ZkQ1n5ux1pWyQCTD4SHJU45IJrg6rfdG6o0hvxucyp0ZQ7p3NKqgjoVNlxBU4xdXHsPDRlMe5zWUGjbtNFdA%2BsN6eKRHJOo2xBbKj2oTbKBBXd9u997YzEtdhI1WAxKCO62a7wQxBDib2U7QJfrqxiP&X-Amz-Signature=76122f6674c36dfb539f91db5aa30bee70252299106f5f7e67d447a219fb48d1&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466233E5IWQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGIU6Ye4QZq%2FD0JNBGX9AnMAfeIYKejCoJjNeBDeeVcdAiAoP3NGdzvgMX9%2B6Z%2FLVQz5mS5OCDEgNOX0OVu5TmWMLyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcJko2EYuE26kVi6TKtwDlfrHCm5OWYaKwOZts%2FfqLkyDrJQpQGDlhjiSTGFHlPNGY01fI%2Fwxdw%2FiOUMajiRGHpwYP6ga1xlyUozISpmdLKMAg5UCbPQvP2uRAdU9dk7y3W43PieStAxrt1iGZ6gdrGAXlBOcW2s0tYON8rVtf%2BVm%2F6HaRROpL8rJu1vh%2B9F%2F2HJns%2Bhfp2Wz3JJCiNPjS%2BnDpWSmAB2l2eAWIyyeHhLgB2mZ9NS6Gu1fQj%2BCGKARFFNXXZ3mYE4HsedrhEctYKMHPiTszR6weF7oJnJgDMs3FyUoesICaf7bGCOBdCQxBoyG4e6Xv12PtEI%2Bbb%2Fi0T8qkTkW7MosPE3FDWvEVzyB42iHAqmJENP%2BYJn9yhUEMzXnq5nNxkWGuTb%2F4otvkrC%2FOGZRhIOFI0vRo4iggwF8nITs47WAMggoriShHOzttIE%2FMMEj2AyuUIbpHBNEQUEqMKLI%2FEzVAZOJWUMa2uN3BTJjNcXodMenN9S4uadYGYnCaQo19HNwLpJ3tcp7z9D0abCI3oZjBnChyBO9L57WGZvdRtRCoXqYqgCQkVoZexMSnu738xrYYidqP19kLsxYiIGo4Vq1DfGCpTMKLCUKzqKLEzqCNyKHNWdck6DEPz5F6hfqhcibpIkwqsH9vAY6pgHHm1sX7MM3KI4d%2B8%2BMpqEQp%2FK0Rkni3f38EU%2B%2Fn2KnUZoG2VqWx%2BScI8vTNik28QwpHj9dNLemFjb9D25lrQtJsD1%2BVTT%2Fxi01N44KuiRjAQophHmuRZ8wMZ%2BzBTq3rCDiCdIaw7KczdELVFzTk%2BSqgz1YDN%2B4E5H3%2Bcp5L9Arc6l9QMgVMk5zLBnjJycBGkqcuM5NxVXG1bFFIZnmM%2FvRj4FgCmpL&X-Amz-Signature=dcfd22947e395e18b8d53340ebbc42eaee9037c00650b9c5d16d2cdc0e31d80a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466233E5IWQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGIU6Ye4QZq%2FD0JNBGX9AnMAfeIYKejCoJjNeBDeeVcdAiAoP3NGdzvgMX9%2B6Z%2FLVQz5mS5OCDEgNOX0OVu5TmWMLyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcJko2EYuE26kVi6TKtwDlfrHCm5OWYaKwOZts%2FfqLkyDrJQpQGDlhjiSTGFHlPNGY01fI%2Fwxdw%2FiOUMajiRGHpwYP6ga1xlyUozISpmdLKMAg5UCbPQvP2uRAdU9dk7y3W43PieStAxrt1iGZ6gdrGAXlBOcW2s0tYON8rVtf%2BVm%2F6HaRROpL8rJu1vh%2B9F%2F2HJns%2Bhfp2Wz3JJCiNPjS%2BnDpWSmAB2l2eAWIyyeHhLgB2mZ9NS6Gu1fQj%2BCGKARFFNXXZ3mYE4HsedrhEctYKMHPiTszR6weF7oJnJgDMs3FyUoesICaf7bGCOBdCQxBoyG4e6Xv12PtEI%2Bbb%2Fi0T8qkTkW7MosPE3FDWvEVzyB42iHAqmJENP%2BYJn9yhUEMzXnq5nNxkWGuTb%2F4otvkrC%2FOGZRhIOFI0vRo4iggwF8nITs47WAMggoriShHOzttIE%2FMMEj2AyuUIbpHBNEQUEqMKLI%2FEzVAZOJWUMa2uN3BTJjNcXodMenN9S4uadYGYnCaQo19HNwLpJ3tcp7z9D0abCI3oZjBnChyBO9L57WGZvdRtRCoXqYqgCQkVoZexMSnu738xrYYidqP19kLsxYiIGo4Vq1DfGCpTMKLCUKzqKLEzqCNyKHNWdck6DEPz5F6hfqhcibpIkwqsH9vAY6pgHHm1sX7MM3KI4d%2B8%2BMpqEQp%2FK0Rkni3f38EU%2B%2Fn2KnUZoG2VqWx%2BScI8vTNik28QwpHj9dNLemFjb9D25lrQtJsD1%2BVTT%2Fxi01N44KuiRjAQophHmuRZ8wMZ%2BzBTq3rCDiCdIaw7KczdELVFzTk%2BSqgz1YDN%2B4E5H3%2Bcp5L9Arc6l9QMgVMk5zLBnjJycBGkqcuM5NxVXG1bFFIZnmM%2FvRj4FgCmpL&X-Amz-Signature=e77df36e7facb634b1691ea532bf3b2ea9471a10fbea767cc9ace02a0060e9f2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466233E5IWQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGIU6Ye4QZq%2FD0JNBGX9AnMAfeIYKejCoJjNeBDeeVcdAiAoP3NGdzvgMX9%2B6Z%2FLVQz5mS5OCDEgNOX0OVu5TmWMLyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcJko2EYuE26kVi6TKtwDlfrHCm5OWYaKwOZts%2FfqLkyDrJQpQGDlhjiSTGFHlPNGY01fI%2Fwxdw%2FiOUMajiRGHpwYP6ga1xlyUozISpmdLKMAg5UCbPQvP2uRAdU9dk7y3W43PieStAxrt1iGZ6gdrGAXlBOcW2s0tYON8rVtf%2BVm%2F6HaRROpL8rJu1vh%2B9F%2F2HJns%2Bhfp2Wz3JJCiNPjS%2BnDpWSmAB2l2eAWIyyeHhLgB2mZ9NS6Gu1fQj%2BCGKARFFNXXZ3mYE4HsedrhEctYKMHPiTszR6weF7oJnJgDMs3FyUoesICaf7bGCOBdCQxBoyG4e6Xv12PtEI%2Bbb%2Fi0T8qkTkW7MosPE3FDWvEVzyB42iHAqmJENP%2BYJn9yhUEMzXnq5nNxkWGuTb%2F4otvkrC%2FOGZRhIOFI0vRo4iggwF8nITs47WAMggoriShHOzttIE%2FMMEj2AyuUIbpHBNEQUEqMKLI%2FEzVAZOJWUMa2uN3BTJjNcXodMenN9S4uadYGYnCaQo19HNwLpJ3tcp7z9D0abCI3oZjBnChyBO9L57WGZvdRtRCoXqYqgCQkVoZexMSnu738xrYYidqP19kLsxYiIGo4Vq1DfGCpTMKLCUKzqKLEzqCNyKHNWdck6DEPz5F6hfqhcibpIkwqsH9vAY6pgHHm1sX7MM3KI4d%2B8%2BMpqEQp%2FK0Rkni3f38EU%2B%2Fn2KnUZoG2VqWx%2BScI8vTNik28QwpHj9dNLemFjb9D25lrQtJsD1%2BVTT%2Fxi01N44KuiRjAQophHmuRZ8wMZ%2BzBTq3rCDiCdIaw7KczdELVFzTk%2BSqgz1YDN%2B4E5H3%2Bcp5L9Arc6l9QMgVMk5zLBnjJycBGkqcuM5NxVXG1bFFIZnmM%2FvRj4FgCmpL&X-Amz-Signature=0cb3019189a45f0e0c3d9fffb6076c41e322a241f58a0d7d3d1f8448c2125307&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466233E5IWQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGIU6Ye4QZq%2FD0JNBGX9AnMAfeIYKejCoJjNeBDeeVcdAiAoP3NGdzvgMX9%2B6Z%2FLVQz5mS5OCDEgNOX0OVu5TmWMLyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcJko2EYuE26kVi6TKtwDlfrHCm5OWYaKwOZts%2FfqLkyDrJQpQGDlhjiSTGFHlPNGY01fI%2Fwxdw%2FiOUMajiRGHpwYP6ga1xlyUozISpmdLKMAg5UCbPQvP2uRAdU9dk7y3W43PieStAxrt1iGZ6gdrGAXlBOcW2s0tYON8rVtf%2BVm%2F6HaRROpL8rJu1vh%2B9F%2F2HJns%2Bhfp2Wz3JJCiNPjS%2BnDpWSmAB2l2eAWIyyeHhLgB2mZ9NS6Gu1fQj%2BCGKARFFNXXZ3mYE4HsedrhEctYKMHPiTszR6weF7oJnJgDMs3FyUoesICaf7bGCOBdCQxBoyG4e6Xv12PtEI%2Bbb%2Fi0T8qkTkW7MosPE3FDWvEVzyB42iHAqmJENP%2BYJn9yhUEMzXnq5nNxkWGuTb%2F4otvkrC%2FOGZRhIOFI0vRo4iggwF8nITs47WAMggoriShHOzttIE%2FMMEj2AyuUIbpHBNEQUEqMKLI%2FEzVAZOJWUMa2uN3BTJjNcXodMenN9S4uadYGYnCaQo19HNwLpJ3tcp7z9D0abCI3oZjBnChyBO9L57WGZvdRtRCoXqYqgCQkVoZexMSnu738xrYYidqP19kLsxYiIGo4Vq1DfGCpTMKLCUKzqKLEzqCNyKHNWdck6DEPz5F6hfqhcibpIkwqsH9vAY6pgHHm1sX7MM3KI4d%2B8%2BMpqEQp%2FK0Rkni3f38EU%2B%2Fn2KnUZoG2VqWx%2BScI8vTNik28QwpHj9dNLemFjb9D25lrQtJsD1%2BVTT%2Fxi01N44KuiRjAQophHmuRZ8wMZ%2BzBTq3rCDiCdIaw7KczdELVFzTk%2BSqgz1YDN%2B4E5H3%2Bcp5L9Arc6l9QMgVMk5zLBnjJycBGkqcuM5NxVXG1bFFIZnmM%2FvRj4FgCmpL&X-Amz-Signature=4b298fe658750c775f42f7da59b472e23162ab970991adfa55c752074c6ff257&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466233E5IWQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGIU6Ye4QZq%2FD0JNBGX9AnMAfeIYKejCoJjNeBDeeVcdAiAoP3NGdzvgMX9%2B6Z%2FLVQz5mS5OCDEgNOX0OVu5TmWMLyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcJko2EYuE26kVi6TKtwDlfrHCm5OWYaKwOZts%2FfqLkyDrJQpQGDlhjiSTGFHlPNGY01fI%2Fwxdw%2FiOUMajiRGHpwYP6ga1xlyUozISpmdLKMAg5UCbPQvP2uRAdU9dk7y3W43PieStAxrt1iGZ6gdrGAXlBOcW2s0tYON8rVtf%2BVm%2F6HaRROpL8rJu1vh%2B9F%2F2HJns%2Bhfp2Wz3JJCiNPjS%2BnDpWSmAB2l2eAWIyyeHhLgB2mZ9NS6Gu1fQj%2BCGKARFFNXXZ3mYE4HsedrhEctYKMHPiTszR6weF7oJnJgDMs3FyUoesICaf7bGCOBdCQxBoyG4e6Xv12PtEI%2Bbb%2Fi0T8qkTkW7MosPE3FDWvEVzyB42iHAqmJENP%2BYJn9yhUEMzXnq5nNxkWGuTb%2F4otvkrC%2FOGZRhIOFI0vRo4iggwF8nITs47WAMggoriShHOzttIE%2FMMEj2AyuUIbpHBNEQUEqMKLI%2FEzVAZOJWUMa2uN3BTJjNcXodMenN9S4uadYGYnCaQo19HNwLpJ3tcp7z9D0abCI3oZjBnChyBO9L57WGZvdRtRCoXqYqgCQkVoZexMSnu738xrYYidqP19kLsxYiIGo4Vq1DfGCpTMKLCUKzqKLEzqCNyKHNWdck6DEPz5F6hfqhcibpIkwqsH9vAY6pgHHm1sX7MM3KI4d%2B8%2BMpqEQp%2FK0Rkni3f38EU%2B%2Fn2KnUZoG2VqWx%2BScI8vTNik28QwpHj9dNLemFjb9D25lrQtJsD1%2BVTT%2Fxi01N44KuiRjAQophHmuRZ8wMZ%2BzBTq3rCDiCdIaw7KczdELVFzTk%2BSqgz1YDN%2B4E5H3%2Bcp5L9Arc6l9QMgVMk5zLBnjJycBGkqcuM5NxVXG1bFFIZnmM%2FvRj4FgCmpL&X-Amz-Signature=e082212c1ad31caaaf4ffb7775eb1856355b4f256838da2fedfc07740e00be0b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GNX4AZQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtBcTJoybCPjc6rzW%2F9za%2FUofmJ31todaDn4Pftr7vnAiB0S2wnzzFKenENhOklm74gKIzs6zhx%2Ba7EUEvbh6NySyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9nBv8Us09VPxM%2F%2FuKtwDKafUIBrPBaQYgF7ouZLA9C3u0XUEUG%2Fh7lvSKoxK3%2F9eb3II17tp%2FYIdMpEkSxBbHEeGzZsDDnL9e9JsezRSIpAXf%2B2h%2F02WX3bnrPrxT7k6fRrNcU4%2F2F13Gibz9%2FJ3Ub8sKs9NaZOxcT6tSBUBXYAUVKLURWq8Dnj5jz06M2Tv%2FWeDtHx7mst%2FsZ8C73ErhV%2F0MPMY7xfp%2BmFtXfYk12DjuEQ3d2HwX8J7Dkb%2BlKKVm5pm2Qy6OffFq9h2z3ues3TGa9O3qqoIEvY6MVywbofKu1yHLHB%2Fy1ChS2KGCjZ8KB35uMFLm10HnmZRt%2FfpVBzH5j%2F7R0qMdD2Nw%2FtZ2auZ%2FMzjMOKKRT%2BBE5lQseeLQHM3q6sXDFx4fnU%2FnzPw4Mt%2BLYxntktsiWe44An%2BChX3xNusC0GtpQiFb%2FW6lxSD%2F27fuTeV5fTxFYxafr37bbbIILf9zFZcAG3xxKFFSonrZcV%2BHVKd49QHMaTfii3UZLrK3OL259nWjhDsM2ALDRUjZdU4%2BoFAk9qacS4t8F5X1OhuWy3u0RTDrLm6TbBj9eU1yXInTvdEez0kc1vyhIAQlO6zOOu2SfQIl%2Fv457nU8cTW0Pn%2FIuIw6Ac3wCtg9AjTYX7YEPFBlHkw8L39vAY6pgHPX7cbyXL82dOJI%2BVxBjR9G17yteBxeJq8liZjFQUZVLPw2ZUZZpavP7sOTgYV5C5uFTIm1ZkQ1n5ux1pWyQCTD4SHJU45IJrg6rfdG6o0hvxucyp0ZQ7p3NKqgjoVNlxBU4xdXHsPDRlMe5zWUGjbtNFdA%2BsN6eKRHJOo2xBbKj2oTbKBBXd9u997YzEtdhI1WAxKCO62a7wQxBDib2U7QJfrqxiP&X-Amz-Signature=f634a4ee1f3063af9118749ade0b5299501592da88368c8c64896da82bdf4944&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GNX4AZQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtBcTJoybCPjc6rzW%2F9za%2FUofmJ31todaDn4Pftr7vnAiB0S2wnzzFKenENhOklm74gKIzs6zhx%2Ba7EUEvbh6NySyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9nBv8Us09VPxM%2F%2FuKtwDKafUIBrPBaQYgF7ouZLA9C3u0XUEUG%2Fh7lvSKoxK3%2F9eb3II17tp%2FYIdMpEkSxBbHEeGzZsDDnL9e9JsezRSIpAXf%2B2h%2F02WX3bnrPrxT7k6fRrNcU4%2F2F13Gibz9%2FJ3Ub8sKs9NaZOxcT6tSBUBXYAUVKLURWq8Dnj5jz06M2Tv%2FWeDtHx7mst%2FsZ8C73ErhV%2F0MPMY7xfp%2BmFtXfYk12DjuEQ3d2HwX8J7Dkb%2BlKKVm5pm2Qy6OffFq9h2z3ues3TGa9O3qqoIEvY6MVywbofKu1yHLHB%2Fy1ChS2KGCjZ8KB35uMFLm10HnmZRt%2FfpVBzH5j%2F7R0qMdD2Nw%2FtZ2auZ%2FMzjMOKKRT%2BBE5lQseeLQHM3q6sXDFx4fnU%2FnzPw4Mt%2BLYxntktsiWe44An%2BChX3xNusC0GtpQiFb%2FW6lxSD%2F27fuTeV5fTxFYxafr37bbbIILf9zFZcAG3xxKFFSonrZcV%2BHVKd49QHMaTfii3UZLrK3OL259nWjhDsM2ALDRUjZdU4%2BoFAk9qacS4t8F5X1OhuWy3u0RTDrLm6TbBj9eU1yXInTvdEez0kc1vyhIAQlO6zOOu2SfQIl%2Fv457nU8cTW0Pn%2FIuIw6Ac3wCtg9AjTYX7YEPFBlHkw8L39vAY6pgHPX7cbyXL82dOJI%2BVxBjR9G17yteBxeJq8liZjFQUZVLPw2ZUZZpavP7sOTgYV5C5uFTIm1ZkQ1n5ux1pWyQCTD4SHJU45IJrg6rfdG6o0hvxucyp0ZQ7p3NKqgjoVNlxBU4xdXHsPDRlMe5zWUGjbtNFdA%2BsN6eKRHJOo2xBbKj2oTbKBBXd9u997YzEtdhI1WAxKCO62a7wQxBDib2U7QJfrqxiP&X-Amz-Signature=1d5e4e87b6c34c660913bfe3facd7f8183a69f11ac6ce4e59fd95b91ca79b9ca&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GNX4AZQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtBcTJoybCPjc6rzW%2F9za%2FUofmJ31todaDn4Pftr7vnAiB0S2wnzzFKenENhOklm74gKIzs6zhx%2Ba7EUEvbh6NySyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9nBv8Us09VPxM%2F%2FuKtwDKafUIBrPBaQYgF7ouZLA9C3u0XUEUG%2Fh7lvSKoxK3%2F9eb3II17tp%2FYIdMpEkSxBbHEeGzZsDDnL9e9JsezRSIpAXf%2B2h%2F02WX3bnrPrxT7k6fRrNcU4%2F2F13Gibz9%2FJ3Ub8sKs9NaZOxcT6tSBUBXYAUVKLURWq8Dnj5jz06M2Tv%2FWeDtHx7mst%2FsZ8C73ErhV%2F0MPMY7xfp%2BmFtXfYk12DjuEQ3d2HwX8J7Dkb%2BlKKVm5pm2Qy6OffFq9h2z3ues3TGa9O3qqoIEvY6MVywbofKu1yHLHB%2Fy1ChS2KGCjZ8KB35uMFLm10HnmZRt%2FfpVBzH5j%2F7R0qMdD2Nw%2FtZ2auZ%2FMzjMOKKRT%2BBE5lQseeLQHM3q6sXDFx4fnU%2FnzPw4Mt%2BLYxntktsiWe44An%2BChX3xNusC0GtpQiFb%2FW6lxSD%2F27fuTeV5fTxFYxafr37bbbIILf9zFZcAG3xxKFFSonrZcV%2BHVKd49QHMaTfii3UZLrK3OL259nWjhDsM2ALDRUjZdU4%2BoFAk9qacS4t8F5X1OhuWy3u0RTDrLm6TbBj9eU1yXInTvdEez0kc1vyhIAQlO6zOOu2SfQIl%2Fv457nU8cTW0Pn%2FIuIw6Ac3wCtg9AjTYX7YEPFBlHkw8L39vAY6pgHPX7cbyXL82dOJI%2BVxBjR9G17yteBxeJq8liZjFQUZVLPw2ZUZZpavP7sOTgYV5C5uFTIm1ZkQ1n5ux1pWyQCTD4SHJU45IJrg6rfdG6o0hvxucyp0ZQ7p3NKqgjoVNlxBU4xdXHsPDRlMe5zWUGjbtNFdA%2BsN6eKRHJOo2xBbKj2oTbKBBXd9u997YzEtdhI1WAxKCO62a7wQxBDib2U7QJfrqxiP&X-Amz-Signature=9ecbea94756804b514d7b61fb10742f7f4fc6c93b3bfcb0d5668e267d50ebc9d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GNX4AZQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtBcTJoybCPjc6rzW%2F9za%2FUofmJ31todaDn4Pftr7vnAiB0S2wnzzFKenENhOklm74gKIzs6zhx%2Ba7EUEvbh6NySyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9nBv8Us09VPxM%2F%2FuKtwDKafUIBrPBaQYgF7ouZLA9C3u0XUEUG%2Fh7lvSKoxK3%2F9eb3II17tp%2FYIdMpEkSxBbHEeGzZsDDnL9e9JsezRSIpAXf%2B2h%2F02WX3bnrPrxT7k6fRrNcU4%2F2F13Gibz9%2FJ3Ub8sKs9NaZOxcT6tSBUBXYAUVKLURWq8Dnj5jz06M2Tv%2FWeDtHx7mst%2FsZ8C73ErhV%2F0MPMY7xfp%2BmFtXfYk12DjuEQ3d2HwX8J7Dkb%2BlKKVm5pm2Qy6OffFq9h2z3ues3TGa9O3qqoIEvY6MVywbofKu1yHLHB%2Fy1ChS2KGCjZ8KB35uMFLm10HnmZRt%2FfpVBzH5j%2F7R0qMdD2Nw%2FtZ2auZ%2FMzjMOKKRT%2BBE5lQseeLQHM3q6sXDFx4fnU%2FnzPw4Mt%2BLYxntktsiWe44An%2BChX3xNusC0GtpQiFb%2FW6lxSD%2F27fuTeV5fTxFYxafr37bbbIILf9zFZcAG3xxKFFSonrZcV%2BHVKd49QHMaTfii3UZLrK3OL259nWjhDsM2ALDRUjZdU4%2BoFAk9qacS4t8F5X1OhuWy3u0RTDrLm6TbBj9eU1yXInTvdEez0kc1vyhIAQlO6zOOu2SfQIl%2Fv457nU8cTW0Pn%2FIuIw6Ac3wCtg9AjTYX7YEPFBlHkw8L39vAY6pgHPX7cbyXL82dOJI%2BVxBjR9G17yteBxeJq8liZjFQUZVLPw2ZUZZpavP7sOTgYV5C5uFTIm1ZkQ1n5ux1pWyQCTD4SHJU45IJrg6rfdG6o0hvxucyp0ZQ7p3NKqgjoVNlxBU4xdXHsPDRlMe5zWUGjbtNFdA%2BsN6eKRHJOo2xBbKj2oTbKBBXd9u997YzEtdhI1WAxKCO62a7wQxBDib2U7QJfrqxiP&X-Amz-Signature=70fe4dccaafd43c5dee6ed9e92f8e5bb8cd96da0621fbb1c52c8604b3c3588d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GNX4AZQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtBcTJoybCPjc6rzW%2F9za%2FUofmJ31todaDn4Pftr7vnAiB0S2wnzzFKenENhOklm74gKIzs6zhx%2Ba7EUEvbh6NySyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9nBv8Us09VPxM%2F%2FuKtwDKafUIBrPBaQYgF7ouZLA9C3u0XUEUG%2Fh7lvSKoxK3%2F9eb3II17tp%2FYIdMpEkSxBbHEeGzZsDDnL9e9JsezRSIpAXf%2B2h%2F02WX3bnrPrxT7k6fRrNcU4%2F2F13Gibz9%2FJ3Ub8sKs9NaZOxcT6tSBUBXYAUVKLURWq8Dnj5jz06M2Tv%2FWeDtHx7mst%2FsZ8C73ErhV%2F0MPMY7xfp%2BmFtXfYk12DjuEQ3d2HwX8J7Dkb%2BlKKVm5pm2Qy6OffFq9h2z3ues3TGa9O3qqoIEvY6MVywbofKu1yHLHB%2Fy1ChS2KGCjZ8KB35uMFLm10HnmZRt%2FfpVBzH5j%2F7R0qMdD2Nw%2FtZ2auZ%2FMzjMOKKRT%2BBE5lQseeLQHM3q6sXDFx4fnU%2FnzPw4Mt%2BLYxntktsiWe44An%2BChX3xNusC0GtpQiFb%2FW6lxSD%2F27fuTeV5fTxFYxafr37bbbIILf9zFZcAG3xxKFFSonrZcV%2BHVKd49QHMaTfii3UZLrK3OL259nWjhDsM2ALDRUjZdU4%2BoFAk9qacS4t8F5X1OhuWy3u0RTDrLm6TbBj9eU1yXInTvdEez0kc1vyhIAQlO6zOOu2SfQIl%2Fv457nU8cTW0Pn%2FIuIw6Ac3wCtg9AjTYX7YEPFBlHkw8L39vAY6pgHPX7cbyXL82dOJI%2BVxBjR9G17yteBxeJq8liZjFQUZVLPw2ZUZZpavP7sOTgYV5C5uFTIm1ZkQ1n5ux1pWyQCTD4SHJU45IJrg6rfdG6o0hvxucyp0ZQ7p3NKqgjoVNlxBU4xdXHsPDRlMe5zWUGjbtNFdA%2BsN6eKRHJOo2xBbKj2oTbKBBXd9u997YzEtdhI1WAxKCO62a7wQxBDib2U7QJfrqxiP&X-Amz-Signature=a7e89c40e3e428674aca121f8c91726758ecf73970c9d4a0983c89254c52ce96&X-Amz-SignedHeaders=host&x-id=GetObject)
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


