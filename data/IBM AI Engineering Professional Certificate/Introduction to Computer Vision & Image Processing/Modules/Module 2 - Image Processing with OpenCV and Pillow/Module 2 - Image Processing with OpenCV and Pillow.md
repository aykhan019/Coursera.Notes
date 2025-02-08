

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2E6UUHG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDETZTdNVPDFzPPz0Adv9mMTjXpkLHZ5faX6AE3lLcoXwIhAMciRQTZWZLdpDrMrkk%2FkiBxRkG5dkUF1ASu4ToxINngKogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzWbUJEsv2kjs0Poz4q3ANaQCWGxgFAch7QRMOWPXniHgNCRXkVB7yMlz2RlmVUicMxCr%2B0ylToEoKokH7ReUNd%2BBhzvIFSxjAlk3Nw%2Boq79RgU34aw7zLyJMvttZlnGbTR%2BIYX4LWodJhsfhX3n5BzQjDUcTzCvJcc3HVC77xsv81BwC1QgFbw%2F3iGVkWpuKpHhIhCw2xGwC3om%2FUsE8BIkvxr4B68YPrz8yPHkaoFThWhzEveq%2BMT3wPwoYHU%2BhPtBynM%2Bfuu%2BVmDGQpxDgqrW01fD3R7SWDaEpbUPG4J0jbxpceWaQ0GE05%2BZnpru150e4vZrDSlFWz0kaVaRS0SHJKKIIwNdF%2BGAA140Fql4PzUYbrgCCRzUrKbdutWtYUlcSc4hYntsi0lYkC2XGmy4A53cubplEWQE1NtQ%2B1gNvikONfYLixV5UyFmAU9dzYjVuyB2ijAeunEV%2BCRpe%2B9sIUvIqXDq4pczdVLQzgsq%2BeRiWnX%2FjjLOr1gwOEZBLj33yYBkaBSntzJXq0i8s4QcNJTEXKF6jny9Bh50%2FStUggNUeMrG6O%2BvuitP0HABupL1ZYCTOspVenhp%2FEXsu5h5egm1YugzPUA61o5HIr2agnBi4%2B9tEFSpo11m01jwjZO95zQ3up6X4rm3jC9jpy9BjqkARevEk4tzyc%2Bmg5UvEu%2BoLnLw%2B4sUoZeGkUg8%2Ft%2F%2FCssacLRJa5QQ68ZlwdYSdDhyfG6qmEoCZR1QHW%2BAwbv%2ByTy%2Fnf7gtVU9OnKWePeP0CrkIQPdvGfGWoni%2FOYv6PBvm4xM34RXbG3FB%2FkavjLr8P5e0dUBBUr0AzQOiyrCXtDDdJmUmAg0AmgyGYCzPHqW%2Fws0A9wDhWQoyeZ%2Bgw2dktSyTit&X-Amz-Signature=e2afbe160ed8c1897b1cf9dd034de06ef234d83249d2d3a9a0c3c19151e905dc&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466646B77RM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHJCjwI4K16gIM0ZTds%2FF%2FSJdAdfMk7cLBDXkqgYlEF%2BAiEAjAPx%2FwDuqfHSkIGXa8fQYr67vzqJm4FA5GSfM%2BM2wtwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDCU16Z%2F6Z%2FG%2F6WigCrcA%2FLG8%2B5E%2FT%2Fg7%2Fj5mjRajJWwnd%2BHuw3J%2BmYaSBVzXYI0HplIULA8FlpxcgFw2meytE4JDgwYuAKMH7lFs3wV5Z1uhi%2BsWpbU6vgOdvALhg8Fzi%2BbIu4f96d0XM7ljbEdqGY%2FWqtKYGVCstXHOoTEo5zN0ve9gFBTkCY4LgLIZy2I3bUJYXW0Je8Pmb63j8xgy7wOoTMz6YOTBUXzsk9VE95EhELaVkQ7k6vFX%2Fa9ZifTcJmy%2FqRKP%2FO6US4XbmddE5SS8ECNnZik%2BtqbGgH1Q5ihbxPW1SvQa%2F%2BJIpqiO618eivwuVCLTr3WQvbW%2FzBgOdOHAn1%2FsQ0s5T482uo4epmZiIaBDEgciClHFIYK2FGbWrvk6rIclIfHshpMjjrxmXCf4Y5Y7fJjkk3%2BfGLAIYW3PipBtxnKa%2F8Biosx4G7eun6KjeUnVF%2BYwpNSXfaFRVDeoNeZkLQGEUClnae0whYjpiYWxeS8RDofp7lJn1CZu5kaYOxOxfeyO0IDIfghMEd4rTlvEBc77hqDoSUb%2FvuHGZzFhuml8Cn0iQhHzykcZdFivaMjqRGhwJw7DWndyrvvXj2XSrayrE7%2FSodsWC3KtO6d0p2IgnvJgJwcf5W7MLA3UX%2FpmTcCBnIAMNuOnL0GOqUBbNAfy3C9kElWWRYl3q5B9Y48ZdYtQoVtmIW7YWiylnLXnfZoknJPBpkRSbQa6VaMnOn3rlF0Fc9Dk%2Bt9nsg90eOdJoxYmjajUqetYIVjbXn4F%2BraPQnktKmlWiE7UiSGe5628VmGpudS%2BdbgEQjzWV5DGiQefnmeG%2BRSIP4TKhKdZ3LvNVbMbl8KLhEPi5iuUF1h9KeMyWqnKfNE8JVkX8lKu3XS&X-Amz-Signature=8bc0f97ee55fec5e73ed5d43782dd37160acf45c6b6d497c55dc3fe29fd96800&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466646B77RM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHJCjwI4K16gIM0ZTds%2FF%2FSJdAdfMk7cLBDXkqgYlEF%2BAiEAjAPx%2FwDuqfHSkIGXa8fQYr67vzqJm4FA5GSfM%2BM2wtwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDCU16Z%2F6Z%2FG%2F6WigCrcA%2FLG8%2B5E%2FT%2Fg7%2Fj5mjRajJWwnd%2BHuw3J%2BmYaSBVzXYI0HplIULA8FlpxcgFw2meytE4JDgwYuAKMH7lFs3wV5Z1uhi%2BsWpbU6vgOdvALhg8Fzi%2BbIu4f96d0XM7ljbEdqGY%2FWqtKYGVCstXHOoTEo5zN0ve9gFBTkCY4LgLIZy2I3bUJYXW0Je8Pmb63j8xgy7wOoTMz6YOTBUXzsk9VE95EhELaVkQ7k6vFX%2Fa9ZifTcJmy%2FqRKP%2FO6US4XbmddE5SS8ECNnZik%2BtqbGgH1Q5ihbxPW1SvQa%2F%2BJIpqiO618eivwuVCLTr3WQvbW%2FzBgOdOHAn1%2FsQ0s5T482uo4epmZiIaBDEgciClHFIYK2FGbWrvk6rIclIfHshpMjjrxmXCf4Y5Y7fJjkk3%2BfGLAIYW3PipBtxnKa%2F8Biosx4G7eun6KjeUnVF%2BYwpNSXfaFRVDeoNeZkLQGEUClnae0whYjpiYWxeS8RDofp7lJn1CZu5kaYOxOxfeyO0IDIfghMEd4rTlvEBc77hqDoSUb%2FvuHGZzFhuml8Cn0iQhHzykcZdFivaMjqRGhwJw7DWndyrvvXj2XSrayrE7%2FSodsWC3KtO6d0p2IgnvJgJwcf5W7MLA3UX%2FpmTcCBnIAMNuOnL0GOqUBbNAfy3C9kElWWRYl3q5B9Y48ZdYtQoVtmIW7YWiylnLXnfZoknJPBpkRSbQa6VaMnOn3rlF0Fc9Dk%2Bt9nsg90eOdJoxYmjajUqetYIVjbXn4F%2BraPQnktKmlWiE7UiSGe5628VmGpudS%2BdbgEQjzWV5DGiQefnmeG%2BRSIP4TKhKdZ3LvNVbMbl8KLhEPi5iuUF1h9KeMyWqnKfNE8JVkX8lKu3XS&X-Amz-Signature=1f0819f4f2e8ed6aba44795182c2d029429f20b6d98f693782e8d1990c356a40&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466646B77RM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHJCjwI4K16gIM0ZTds%2FF%2FSJdAdfMk7cLBDXkqgYlEF%2BAiEAjAPx%2FwDuqfHSkIGXa8fQYr67vzqJm4FA5GSfM%2BM2wtwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDCU16Z%2F6Z%2FG%2F6WigCrcA%2FLG8%2B5E%2FT%2Fg7%2Fj5mjRajJWwnd%2BHuw3J%2BmYaSBVzXYI0HplIULA8FlpxcgFw2meytE4JDgwYuAKMH7lFs3wV5Z1uhi%2BsWpbU6vgOdvALhg8Fzi%2BbIu4f96d0XM7ljbEdqGY%2FWqtKYGVCstXHOoTEo5zN0ve9gFBTkCY4LgLIZy2I3bUJYXW0Je8Pmb63j8xgy7wOoTMz6YOTBUXzsk9VE95EhELaVkQ7k6vFX%2Fa9ZifTcJmy%2FqRKP%2FO6US4XbmddE5SS8ECNnZik%2BtqbGgH1Q5ihbxPW1SvQa%2F%2BJIpqiO618eivwuVCLTr3WQvbW%2FzBgOdOHAn1%2FsQ0s5T482uo4epmZiIaBDEgciClHFIYK2FGbWrvk6rIclIfHshpMjjrxmXCf4Y5Y7fJjkk3%2BfGLAIYW3PipBtxnKa%2F8Biosx4G7eun6KjeUnVF%2BYwpNSXfaFRVDeoNeZkLQGEUClnae0whYjpiYWxeS8RDofp7lJn1CZu5kaYOxOxfeyO0IDIfghMEd4rTlvEBc77hqDoSUb%2FvuHGZzFhuml8Cn0iQhHzykcZdFivaMjqRGhwJw7DWndyrvvXj2XSrayrE7%2FSodsWC3KtO6d0p2IgnvJgJwcf5W7MLA3UX%2FpmTcCBnIAMNuOnL0GOqUBbNAfy3C9kElWWRYl3q5B9Y48ZdYtQoVtmIW7YWiylnLXnfZoknJPBpkRSbQa6VaMnOn3rlF0Fc9Dk%2Bt9nsg90eOdJoxYmjajUqetYIVjbXn4F%2BraPQnktKmlWiE7UiSGe5628VmGpudS%2BdbgEQjzWV5DGiQefnmeG%2BRSIP4TKhKdZ3LvNVbMbl8KLhEPi5iuUF1h9KeMyWqnKfNE8JVkX8lKu3XS&X-Amz-Signature=f07baba17b4c9fa35357b6638adb8cb5dd5eee158324c27e0fc1b937037c1e4d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466646B77RM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHJCjwI4K16gIM0ZTds%2FF%2FSJdAdfMk7cLBDXkqgYlEF%2BAiEAjAPx%2FwDuqfHSkIGXa8fQYr67vzqJm4FA5GSfM%2BM2wtwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDCU16Z%2F6Z%2FG%2F6WigCrcA%2FLG8%2B5E%2FT%2Fg7%2Fj5mjRajJWwnd%2BHuw3J%2BmYaSBVzXYI0HplIULA8FlpxcgFw2meytE4JDgwYuAKMH7lFs3wV5Z1uhi%2BsWpbU6vgOdvALhg8Fzi%2BbIu4f96d0XM7ljbEdqGY%2FWqtKYGVCstXHOoTEo5zN0ve9gFBTkCY4LgLIZy2I3bUJYXW0Je8Pmb63j8xgy7wOoTMz6YOTBUXzsk9VE95EhELaVkQ7k6vFX%2Fa9ZifTcJmy%2FqRKP%2FO6US4XbmddE5SS8ECNnZik%2BtqbGgH1Q5ihbxPW1SvQa%2F%2BJIpqiO618eivwuVCLTr3WQvbW%2FzBgOdOHAn1%2FsQ0s5T482uo4epmZiIaBDEgciClHFIYK2FGbWrvk6rIclIfHshpMjjrxmXCf4Y5Y7fJjkk3%2BfGLAIYW3PipBtxnKa%2F8Biosx4G7eun6KjeUnVF%2BYwpNSXfaFRVDeoNeZkLQGEUClnae0whYjpiYWxeS8RDofp7lJn1CZu5kaYOxOxfeyO0IDIfghMEd4rTlvEBc77hqDoSUb%2FvuHGZzFhuml8Cn0iQhHzykcZdFivaMjqRGhwJw7DWndyrvvXj2XSrayrE7%2FSodsWC3KtO6d0p2IgnvJgJwcf5W7MLA3UX%2FpmTcCBnIAMNuOnL0GOqUBbNAfy3C9kElWWRYl3q5B9Y48ZdYtQoVtmIW7YWiylnLXnfZoknJPBpkRSbQa6VaMnOn3rlF0Fc9Dk%2Bt9nsg90eOdJoxYmjajUqetYIVjbXn4F%2BraPQnktKmlWiE7UiSGe5628VmGpudS%2BdbgEQjzWV5DGiQefnmeG%2BRSIP4TKhKdZ3LvNVbMbl8KLhEPi5iuUF1h9KeMyWqnKfNE8JVkX8lKu3XS&X-Amz-Signature=454790244de8f86ff0eb42b509b5f83d79b266f2298d36519c36f7c96e7850c2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466646B77RM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHJCjwI4K16gIM0ZTds%2FF%2FSJdAdfMk7cLBDXkqgYlEF%2BAiEAjAPx%2FwDuqfHSkIGXa8fQYr67vzqJm4FA5GSfM%2BM2wtwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDCU16Z%2F6Z%2FG%2F6WigCrcA%2FLG8%2B5E%2FT%2Fg7%2Fj5mjRajJWwnd%2BHuw3J%2BmYaSBVzXYI0HplIULA8FlpxcgFw2meytE4JDgwYuAKMH7lFs3wV5Z1uhi%2BsWpbU6vgOdvALhg8Fzi%2BbIu4f96d0XM7ljbEdqGY%2FWqtKYGVCstXHOoTEo5zN0ve9gFBTkCY4LgLIZy2I3bUJYXW0Je8Pmb63j8xgy7wOoTMz6YOTBUXzsk9VE95EhELaVkQ7k6vFX%2Fa9ZifTcJmy%2FqRKP%2FO6US4XbmddE5SS8ECNnZik%2BtqbGgH1Q5ihbxPW1SvQa%2F%2BJIpqiO618eivwuVCLTr3WQvbW%2FzBgOdOHAn1%2FsQ0s5T482uo4epmZiIaBDEgciClHFIYK2FGbWrvk6rIclIfHshpMjjrxmXCf4Y5Y7fJjkk3%2BfGLAIYW3PipBtxnKa%2F8Biosx4G7eun6KjeUnVF%2BYwpNSXfaFRVDeoNeZkLQGEUClnae0whYjpiYWxeS8RDofp7lJn1CZu5kaYOxOxfeyO0IDIfghMEd4rTlvEBc77hqDoSUb%2FvuHGZzFhuml8Cn0iQhHzykcZdFivaMjqRGhwJw7DWndyrvvXj2XSrayrE7%2FSodsWC3KtO6d0p2IgnvJgJwcf5W7MLA3UX%2FpmTcCBnIAMNuOnL0GOqUBbNAfy3C9kElWWRYl3q5B9Y48ZdYtQoVtmIW7YWiylnLXnfZoknJPBpkRSbQa6VaMnOn3rlF0Fc9Dk%2Bt9nsg90eOdJoxYmjajUqetYIVjbXn4F%2BraPQnktKmlWiE7UiSGe5628VmGpudS%2BdbgEQjzWV5DGiQefnmeG%2BRSIP4TKhKdZ3LvNVbMbl8KLhEPi5iuUF1h9KeMyWqnKfNE8JVkX8lKu3XS&X-Amz-Signature=865e842a61de4673ccc20ef90f80f9260d3c30d8fe7d20a628896bd7473cda30&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2E6UUHG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDETZTdNVPDFzPPz0Adv9mMTjXpkLHZ5faX6AE3lLcoXwIhAMciRQTZWZLdpDrMrkk%2FkiBxRkG5dkUF1ASu4ToxINngKogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzWbUJEsv2kjs0Poz4q3ANaQCWGxgFAch7QRMOWPXniHgNCRXkVB7yMlz2RlmVUicMxCr%2B0ylToEoKokH7ReUNd%2BBhzvIFSxjAlk3Nw%2Boq79RgU34aw7zLyJMvttZlnGbTR%2BIYX4LWodJhsfhX3n5BzQjDUcTzCvJcc3HVC77xsv81BwC1QgFbw%2F3iGVkWpuKpHhIhCw2xGwC3om%2FUsE8BIkvxr4B68YPrz8yPHkaoFThWhzEveq%2BMT3wPwoYHU%2BhPtBynM%2Bfuu%2BVmDGQpxDgqrW01fD3R7SWDaEpbUPG4J0jbxpceWaQ0GE05%2BZnpru150e4vZrDSlFWz0kaVaRS0SHJKKIIwNdF%2BGAA140Fql4PzUYbrgCCRzUrKbdutWtYUlcSc4hYntsi0lYkC2XGmy4A53cubplEWQE1NtQ%2B1gNvikONfYLixV5UyFmAU9dzYjVuyB2ijAeunEV%2BCRpe%2B9sIUvIqXDq4pczdVLQzgsq%2BeRiWnX%2FjjLOr1gwOEZBLj33yYBkaBSntzJXq0i8s4QcNJTEXKF6jny9Bh50%2FStUggNUeMrG6O%2BvuitP0HABupL1ZYCTOspVenhp%2FEXsu5h5egm1YugzPUA61o5HIr2agnBi4%2B9tEFSpo11m01jwjZO95zQ3up6X4rm3jC9jpy9BjqkARevEk4tzyc%2Bmg5UvEu%2BoLnLw%2B4sUoZeGkUg8%2Ft%2F%2FCssacLRJa5QQ68ZlwdYSdDhyfG6qmEoCZR1QHW%2BAwbv%2ByTy%2Fnf7gtVU9OnKWePeP0CrkIQPdvGfGWoni%2FOYv6PBvm4xM34RXbG3FB%2FkavjLr8P5e0dUBBUr0AzQOiyrCXtDDdJmUmAg0AmgyGYCzPHqW%2Fws0A9wDhWQoyeZ%2Bgw2dktSyTit&X-Amz-Signature=b706b35f88c9af9687fd8facb5c815e67dfe078aad473e50a3f12898cc09b3e2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2E6UUHG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDETZTdNVPDFzPPz0Adv9mMTjXpkLHZ5faX6AE3lLcoXwIhAMciRQTZWZLdpDrMrkk%2FkiBxRkG5dkUF1ASu4ToxINngKogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzWbUJEsv2kjs0Poz4q3ANaQCWGxgFAch7QRMOWPXniHgNCRXkVB7yMlz2RlmVUicMxCr%2B0ylToEoKokH7ReUNd%2BBhzvIFSxjAlk3Nw%2Boq79RgU34aw7zLyJMvttZlnGbTR%2BIYX4LWodJhsfhX3n5BzQjDUcTzCvJcc3HVC77xsv81BwC1QgFbw%2F3iGVkWpuKpHhIhCw2xGwC3om%2FUsE8BIkvxr4B68YPrz8yPHkaoFThWhzEveq%2BMT3wPwoYHU%2BhPtBynM%2Bfuu%2BVmDGQpxDgqrW01fD3R7SWDaEpbUPG4J0jbxpceWaQ0GE05%2BZnpru150e4vZrDSlFWz0kaVaRS0SHJKKIIwNdF%2BGAA140Fql4PzUYbrgCCRzUrKbdutWtYUlcSc4hYntsi0lYkC2XGmy4A53cubplEWQE1NtQ%2B1gNvikONfYLixV5UyFmAU9dzYjVuyB2ijAeunEV%2BCRpe%2B9sIUvIqXDq4pczdVLQzgsq%2BeRiWnX%2FjjLOr1gwOEZBLj33yYBkaBSntzJXq0i8s4QcNJTEXKF6jny9Bh50%2FStUggNUeMrG6O%2BvuitP0HABupL1ZYCTOspVenhp%2FEXsu5h5egm1YugzPUA61o5HIr2agnBi4%2B9tEFSpo11m01jwjZO95zQ3up6X4rm3jC9jpy9BjqkARevEk4tzyc%2Bmg5UvEu%2BoLnLw%2B4sUoZeGkUg8%2Ft%2F%2FCssacLRJa5QQ68ZlwdYSdDhyfG6qmEoCZR1QHW%2BAwbv%2ByTy%2Fnf7gtVU9OnKWePeP0CrkIQPdvGfGWoni%2FOYv6PBvm4xM34RXbG3FB%2FkavjLr8P5e0dUBBUr0AzQOiyrCXtDDdJmUmAg0AmgyGYCzPHqW%2Fws0A9wDhWQoyeZ%2Bgw2dktSyTit&X-Amz-Signature=1255600280eeaa6bc0babede2523c40b4640c0bf7ba73e15d18ffabd84bd7c38&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2E6UUHG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDETZTdNVPDFzPPz0Adv9mMTjXpkLHZ5faX6AE3lLcoXwIhAMciRQTZWZLdpDrMrkk%2FkiBxRkG5dkUF1ASu4ToxINngKogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzWbUJEsv2kjs0Poz4q3ANaQCWGxgFAch7QRMOWPXniHgNCRXkVB7yMlz2RlmVUicMxCr%2B0ylToEoKokH7ReUNd%2BBhzvIFSxjAlk3Nw%2Boq79RgU34aw7zLyJMvttZlnGbTR%2BIYX4LWodJhsfhX3n5BzQjDUcTzCvJcc3HVC77xsv81BwC1QgFbw%2F3iGVkWpuKpHhIhCw2xGwC3om%2FUsE8BIkvxr4B68YPrz8yPHkaoFThWhzEveq%2BMT3wPwoYHU%2BhPtBynM%2Bfuu%2BVmDGQpxDgqrW01fD3R7SWDaEpbUPG4J0jbxpceWaQ0GE05%2BZnpru150e4vZrDSlFWz0kaVaRS0SHJKKIIwNdF%2BGAA140Fql4PzUYbrgCCRzUrKbdutWtYUlcSc4hYntsi0lYkC2XGmy4A53cubplEWQE1NtQ%2B1gNvikONfYLixV5UyFmAU9dzYjVuyB2ijAeunEV%2BCRpe%2B9sIUvIqXDq4pczdVLQzgsq%2BeRiWnX%2FjjLOr1gwOEZBLj33yYBkaBSntzJXq0i8s4QcNJTEXKF6jny9Bh50%2FStUggNUeMrG6O%2BvuitP0HABupL1ZYCTOspVenhp%2FEXsu5h5egm1YugzPUA61o5HIr2agnBi4%2B9tEFSpo11m01jwjZO95zQ3up6X4rm3jC9jpy9BjqkARevEk4tzyc%2Bmg5UvEu%2BoLnLw%2B4sUoZeGkUg8%2Ft%2F%2FCssacLRJa5QQ68ZlwdYSdDhyfG6qmEoCZR1QHW%2BAwbv%2ByTy%2Fnf7gtVU9OnKWePeP0CrkIQPdvGfGWoni%2FOYv6PBvm4xM34RXbG3FB%2FkavjLr8P5e0dUBBUr0AzQOiyrCXtDDdJmUmAg0AmgyGYCzPHqW%2Fws0A9wDhWQoyeZ%2Bgw2dktSyTit&X-Amz-Signature=b2b0901347e2e973d94133a74de83d5258b260d7e30cc0ec4c41c0e79fa1a2db&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2E6UUHG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDETZTdNVPDFzPPz0Adv9mMTjXpkLHZ5faX6AE3lLcoXwIhAMciRQTZWZLdpDrMrkk%2FkiBxRkG5dkUF1ASu4ToxINngKogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzWbUJEsv2kjs0Poz4q3ANaQCWGxgFAch7QRMOWPXniHgNCRXkVB7yMlz2RlmVUicMxCr%2B0ylToEoKokH7ReUNd%2BBhzvIFSxjAlk3Nw%2Boq79RgU34aw7zLyJMvttZlnGbTR%2BIYX4LWodJhsfhX3n5BzQjDUcTzCvJcc3HVC77xsv81BwC1QgFbw%2F3iGVkWpuKpHhIhCw2xGwC3om%2FUsE8BIkvxr4B68YPrz8yPHkaoFThWhzEveq%2BMT3wPwoYHU%2BhPtBynM%2Bfuu%2BVmDGQpxDgqrW01fD3R7SWDaEpbUPG4J0jbxpceWaQ0GE05%2BZnpru150e4vZrDSlFWz0kaVaRS0SHJKKIIwNdF%2BGAA140Fql4PzUYbrgCCRzUrKbdutWtYUlcSc4hYntsi0lYkC2XGmy4A53cubplEWQE1NtQ%2B1gNvikONfYLixV5UyFmAU9dzYjVuyB2ijAeunEV%2BCRpe%2B9sIUvIqXDq4pczdVLQzgsq%2BeRiWnX%2FjjLOr1gwOEZBLj33yYBkaBSntzJXq0i8s4QcNJTEXKF6jny9Bh50%2FStUggNUeMrG6O%2BvuitP0HABupL1ZYCTOspVenhp%2FEXsu5h5egm1YugzPUA61o5HIr2agnBi4%2B9tEFSpo11m01jwjZO95zQ3up6X4rm3jC9jpy9BjqkARevEk4tzyc%2Bmg5UvEu%2BoLnLw%2B4sUoZeGkUg8%2Ft%2F%2FCssacLRJa5QQ68ZlwdYSdDhyfG6qmEoCZR1QHW%2BAwbv%2ByTy%2Fnf7gtVU9OnKWePeP0CrkIQPdvGfGWoni%2FOYv6PBvm4xM34RXbG3FB%2FkavjLr8P5e0dUBBUr0AzQOiyrCXtDDdJmUmAg0AmgyGYCzPHqW%2Fws0A9wDhWQoyeZ%2Bgw2dktSyTit&X-Amz-Signature=6969b87b114a9c6fdd871e39a90140ff011a76601eff29ad1f9669cf2496323a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2E6UUHG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDETZTdNVPDFzPPz0Adv9mMTjXpkLHZ5faX6AE3lLcoXwIhAMciRQTZWZLdpDrMrkk%2FkiBxRkG5dkUF1ASu4ToxINngKogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzWbUJEsv2kjs0Poz4q3ANaQCWGxgFAch7QRMOWPXniHgNCRXkVB7yMlz2RlmVUicMxCr%2B0ylToEoKokH7ReUNd%2BBhzvIFSxjAlk3Nw%2Boq79RgU34aw7zLyJMvttZlnGbTR%2BIYX4LWodJhsfhX3n5BzQjDUcTzCvJcc3HVC77xsv81BwC1QgFbw%2F3iGVkWpuKpHhIhCw2xGwC3om%2FUsE8BIkvxr4B68YPrz8yPHkaoFThWhzEveq%2BMT3wPwoYHU%2BhPtBynM%2Bfuu%2BVmDGQpxDgqrW01fD3R7SWDaEpbUPG4J0jbxpceWaQ0GE05%2BZnpru150e4vZrDSlFWz0kaVaRS0SHJKKIIwNdF%2BGAA140Fql4PzUYbrgCCRzUrKbdutWtYUlcSc4hYntsi0lYkC2XGmy4A53cubplEWQE1NtQ%2B1gNvikONfYLixV5UyFmAU9dzYjVuyB2ijAeunEV%2BCRpe%2B9sIUvIqXDq4pczdVLQzgsq%2BeRiWnX%2FjjLOr1gwOEZBLj33yYBkaBSntzJXq0i8s4QcNJTEXKF6jny9Bh50%2FStUggNUeMrG6O%2BvuitP0HABupL1ZYCTOspVenhp%2FEXsu5h5egm1YugzPUA61o5HIr2agnBi4%2B9tEFSpo11m01jwjZO95zQ3up6X4rm3jC9jpy9BjqkARevEk4tzyc%2Bmg5UvEu%2BoLnLw%2B4sUoZeGkUg8%2Ft%2F%2FCssacLRJa5QQ68ZlwdYSdDhyfG6qmEoCZR1QHW%2BAwbv%2ByTy%2Fnf7gtVU9OnKWePeP0CrkIQPdvGfGWoni%2FOYv6PBvm4xM34RXbG3FB%2FkavjLr8P5e0dUBBUr0AzQOiyrCXtDDdJmUmAg0AmgyGYCzPHqW%2Fws0A9wDhWQoyeZ%2Bgw2dktSyTit&X-Amz-Signature=3a766c8fc630b7e72d53196337beb5240895750b5c12256355107c0222039787&X-Amz-SignedHeaders=host&x-id=GetObject)
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


