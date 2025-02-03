

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SDYFAMB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAbByhzlrA9JRMng91FTYFKSWZhhqqbCvWI6Y35VHBEuAiEA409wZtdvXmaKPLXj5MBsDT37u0nXiCuudBtkuPdRiqwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDICHawlBd9JzbfUxvCrcAxbaUD%2FxkGD7gYhqPuX1PoPjX2HR7f%2B35aowqkAIjqaAggJXbizJz4zPac3B4OGCVDzpfhMsNSTqS3Cle%2FzYftQ757YpdSdsIr1lSB1V%2FkFJonfvX5v5%2FKJyJ4v%2Fiha6DO4ajyOyfqQXElmixoDYS2CdfooEilGnv%2B7qKxO%2B2Hf%2BeewuhH%2FYrsnHv1ImINywQT%2BTlFhOP%2FOOEr6%2BG2Z%2FjcwULhEcnZIOWYUd4k0IxMcl02811GtfDbnqY%2F2rhmhtcYHLcH%2FjbCU8miFq4%2BgvTyXwD3%2ByJBoqW3quB38vI61HjHBhCrzR%2FaPj1n5ZHqBXPEw8WRw%2BqgxaiU8C7J%2BAXnI%2BTHveIdn7y7t6p64H%2FBU%2FJJuCcbDTH3ac9L8i95YYlyiujhXeMtZjbECG%2FBNmBgpQwt37nULLDiQ%2FIPRtx359bZYYh55qQW8DC5QlsWfIrMKzPZHKPhUBRnR8WOF4M3MHcmYpWlZUHqkGhj5TyVP55nFsX9%2FXhJGNUTMKRy9CsIlmGewNkQVZuDpEJD91E3FTkH%2BO%2BzZpV%2B5q3Zvf%2FUq37Ao4lNLLJFrTszaPjp8ezGNaR6zbqQX%2FYzQSfNfX6Vss%2BjaLatQwoqu0s3hCBnmc5HJMCQWQh%2Fx7GuRRMNi%2FgL0GOqUBHtwq0Dv0Jkp8pZhuXawaFPbL%2FujP9LAMqhZCczv7qrVNUTVRMNhDXEmyFK5u8R8GToqBe0Ymnoj7xsTK8vJhipMmoUttKhAqiZrvp8%2BeEI2rRu4sjw9k74qw9mfIebMpb%2BaxMBAUVvHS3bKO6zDBwRu7Sc%2BJ3ZQ3WF15Krhl3Ya%2Bqy7KlRzNFzq9dHiE0yQJ6LvpdgNFE%2B3TG5Q9fhk65x3CG0%2FI&X-Amz-Signature=b275396e23300fa8d67063370fafa10d8d50c8af4e11fd5ed89467d3b268eb2b&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3PTP2U4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlonyh7pnx5qfWFZwU7iYViWp823juejRzQ4Kfb14i8AIgLEIkUBFYg1BSuAuEQUAooQWrfqBLyJh0dcNPwRxRyEkqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAaY%2BM3ZvTjCS7%2BXCyrcAxXD%2Bjevz%2FzJI8tftA8khxxMfqg47atfDGzIknPASJ%2Be88nthDV4ffAYfTYG2lPNs1wUI7w4LRYJLAjmXUEqUvyATbxjgFEPxiEB2fF3jTAOmECO%2B8h9KIf%2BtL2NF%2FCGEfnnDCHEmD3cLRcnk%2BKSS5VUa%2Fc2Aafy%2FToxORWlvvXfq26CYnfmM4%2BQSpL6WiYsbvUHs%2FqJhe66GvPwv%2FPox%2BliEAtKTPfkPb1kfDdMvo887BGeVs1VeUzeHhO7oV8u4W6P%2FNu2GRYWTOIBKS5XJTTOW%2FriDQ0zL%2FjLRsFeJBrz%2FFT%2FQySUKxBLgkwjequL8%2By%2BQN6F1Oe30fY8xl1iNShKj7Qu7OHEnda2xGTw75UXG4oWwpQbnXZmipqyelt%2FB7VGrxw0qLqJR3KELE8z1gYXp3naWaRheObToqaPKSLrycwpU6PXVbYFH%2FChyTvLSHGm%2BCb70k4m7oF1GF7xAIIBQSihv23gFACmCeQ53T7p2K618QTfdbLfZeYH97vcnmU8N0DUIthwr5x30WyfvSidayxn8oYAFBN2%2FgvagvYnugk1tsJGpbYZsHmEjxFzwAvZSBiWwwdmM8E220sj83b%2FOk%2FfosXcFUvOagl320L%2BpnBJYkLzJ%2Fsp3ZPVMNC%2FgL0GOqUBrFWiL5fyWRMifnHLBgs0VzDh3LGJbGM%2FlLoRvXhGbbN2htMJzF%2FJxHDNmSr8YhS5AihSRq4OTBjV53hIADJoEoQDcxkrEW2dJHjS2AqMYCJ4afQdxTnJFWFkVBU7Ja63u7YEc9yfMLBdaxQK9%2Fi54HytN7IRtuwju4sm5h4aueDBgzc%2B1rMVYD31rZDcNh7rsKVdazJXIJgaWho%2BjNem4HqcKIBA&X-Amz-Signature=0803832f20b942838e109a1306124283c138a9c0f8a1c136ed166b60346063d3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3PTP2U4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlonyh7pnx5qfWFZwU7iYViWp823juejRzQ4Kfb14i8AIgLEIkUBFYg1BSuAuEQUAooQWrfqBLyJh0dcNPwRxRyEkqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAaY%2BM3ZvTjCS7%2BXCyrcAxXD%2Bjevz%2FzJI8tftA8khxxMfqg47atfDGzIknPASJ%2Be88nthDV4ffAYfTYG2lPNs1wUI7w4LRYJLAjmXUEqUvyATbxjgFEPxiEB2fF3jTAOmECO%2B8h9KIf%2BtL2NF%2FCGEfnnDCHEmD3cLRcnk%2BKSS5VUa%2Fc2Aafy%2FToxORWlvvXfq26CYnfmM4%2BQSpL6WiYsbvUHs%2FqJhe66GvPwv%2FPox%2BliEAtKTPfkPb1kfDdMvo887BGeVs1VeUzeHhO7oV8u4W6P%2FNu2GRYWTOIBKS5XJTTOW%2FriDQ0zL%2FjLRsFeJBrz%2FFT%2FQySUKxBLgkwjequL8%2By%2BQN6F1Oe30fY8xl1iNShKj7Qu7OHEnda2xGTw75UXG4oWwpQbnXZmipqyelt%2FB7VGrxw0qLqJR3KELE8z1gYXp3naWaRheObToqaPKSLrycwpU6PXVbYFH%2FChyTvLSHGm%2BCb70k4m7oF1GF7xAIIBQSihv23gFACmCeQ53T7p2K618QTfdbLfZeYH97vcnmU8N0DUIthwr5x30WyfvSidayxn8oYAFBN2%2FgvagvYnugk1tsJGpbYZsHmEjxFzwAvZSBiWwwdmM8E220sj83b%2FOk%2FfosXcFUvOagl320L%2BpnBJYkLzJ%2Fsp3ZPVMNC%2FgL0GOqUBrFWiL5fyWRMifnHLBgs0VzDh3LGJbGM%2FlLoRvXhGbbN2htMJzF%2FJxHDNmSr8YhS5AihSRq4OTBjV53hIADJoEoQDcxkrEW2dJHjS2AqMYCJ4afQdxTnJFWFkVBU7Ja63u7YEc9yfMLBdaxQK9%2Fi54HytN7IRtuwju4sm5h4aueDBgzc%2B1rMVYD31rZDcNh7rsKVdazJXIJgaWho%2BjNem4HqcKIBA&X-Amz-Signature=3f7a518e861f8d49d4ecea0d388febe83a13c387d9f89ae68b323f705ee16f08&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3PTP2U4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlonyh7pnx5qfWFZwU7iYViWp823juejRzQ4Kfb14i8AIgLEIkUBFYg1BSuAuEQUAooQWrfqBLyJh0dcNPwRxRyEkqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAaY%2BM3ZvTjCS7%2BXCyrcAxXD%2Bjevz%2FzJI8tftA8khxxMfqg47atfDGzIknPASJ%2Be88nthDV4ffAYfTYG2lPNs1wUI7w4LRYJLAjmXUEqUvyATbxjgFEPxiEB2fF3jTAOmECO%2B8h9KIf%2BtL2NF%2FCGEfnnDCHEmD3cLRcnk%2BKSS5VUa%2Fc2Aafy%2FToxORWlvvXfq26CYnfmM4%2BQSpL6WiYsbvUHs%2FqJhe66GvPwv%2FPox%2BliEAtKTPfkPb1kfDdMvo887BGeVs1VeUzeHhO7oV8u4W6P%2FNu2GRYWTOIBKS5XJTTOW%2FriDQ0zL%2FjLRsFeJBrz%2FFT%2FQySUKxBLgkwjequL8%2By%2BQN6F1Oe30fY8xl1iNShKj7Qu7OHEnda2xGTw75UXG4oWwpQbnXZmipqyelt%2FB7VGrxw0qLqJR3KELE8z1gYXp3naWaRheObToqaPKSLrycwpU6PXVbYFH%2FChyTvLSHGm%2BCb70k4m7oF1GF7xAIIBQSihv23gFACmCeQ53T7p2K618QTfdbLfZeYH97vcnmU8N0DUIthwr5x30WyfvSidayxn8oYAFBN2%2FgvagvYnugk1tsJGpbYZsHmEjxFzwAvZSBiWwwdmM8E220sj83b%2FOk%2FfosXcFUvOagl320L%2BpnBJYkLzJ%2Fsp3ZPVMNC%2FgL0GOqUBrFWiL5fyWRMifnHLBgs0VzDh3LGJbGM%2FlLoRvXhGbbN2htMJzF%2FJxHDNmSr8YhS5AihSRq4OTBjV53hIADJoEoQDcxkrEW2dJHjS2AqMYCJ4afQdxTnJFWFkVBU7Ja63u7YEc9yfMLBdaxQK9%2Fi54HytN7IRtuwju4sm5h4aueDBgzc%2B1rMVYD31rZDcNh7rsKVdazJXIJgaWho%2BjNem4HqcKIBA&X-Amz-Signature=5f1e0e46479c98859c4e2a64d091beb222e6de59614cd73f49a6bd042b5e470a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3PTP2U4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlonyh7pnx5qfWFZwU7iYViWp823juejRzQ4Kfb14i8AIgLEIkUBFYg1BSuAuEQUAooQWrfqBLyJh0dcNPwRxRyEkqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAaY%2BM3ZvTjCS7%2BXCyrcAxXD%2Bjevz%2FzJI8tftA8khxxMfqg47atfDGzIknPASJ%2Be88nthDV4ffAYfTYG2lPNs1wUI7w4LRYJLAjmXUEqUvyATbxjgFEPxiEB2fF3jTAOmECO%2B8h9KIf%2BtL2NF%2FCGEfnnDCHEmD3cLRcnk%2BKSS5VUa%2Fc2Aafy%2FToxORWlvvXfq26CYnfmM4%2BQSpL6WiYsbvUHs%2FqJhe66GvPwv%2FPox%2BliEAtKTPfkPb1kfDdMvo887BGeVs1VeUzeHhO7oV8u4W6P%2FNu2GRYWTOIBKS5XJTTOW%2FriDQ0zL%2FjLRsFeJBrz%2FFT%2FQySUKxBLgkwjequL8%2By%2BQN6F1Oe30fY8xl1iNShKj7Qu7OHEnda2xGTw75UXG4oWwpQbnXZmipqyelt%2FB7VGrxw0qLqJR3KELE8z1gYXp3naWaRheObToqaPKSLrycwpU6PXVbYFH%2FChyTvLSHGm%2BCb70k4m7oF1GF7xAIIBQSihv23gFACmCeQ53T7p2K618QTfdbLfZeYH97vcnmU8N0DUIthwr5x30WyfvSidayxn8oYAFBN2%2FgvagvYnugk1tsJGpbYZsHmEjxFzwAvZSBiWwwdmM8E220sj83b%2FOk%2FfosXcFUvOagl320L%2BpnBJYkLzJ%2Fsp3ZPVMNC%2FgL0GOqUBrFWiL5fyWRMifnHLBgs0VzDh3LGJbGM%2FlLoRvXhGbbN2htMJzF%2FJxHDNmSr8YhS5AihSRq4OTBjV53hIADJoEoQDcxkrEW2dJHjS2AqMYCJ4afQdxTnJFWFkVBU7Ja63u7YEc9yfMLBdaxQK9%2Fi54HytN7IRtuwju4sm5h4aueDBgzc%2B1rMVYD31rZDcNh7rsKVdazJXIJgaWho%2BjNem4HqcKIBA&X-Amz-Signature=d788502a0f373e2e553c29009adcabdd65cbf3a06d996aaaf686862243486601&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3PTP2U4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlonyh7pnx5qfWFZwU7iYViWp823juejRzQ4Kfb14i8AIgLEIkUBFYg1BSuAuEQUAooQWrfqBLyJh0dcNPwRxRyEkqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAaY%2BM3ZvTjCS7%2BXCyrcAxXD%2Bjevz%2FzJI8tftA8khxxMfqg47atfDGzIknPASJ%2Be88nthDV4ffAYfTYG2lPNs1wUI7w4LRYJLAjmXUEqUvyATbxjgFEPxiEB2fF3jTAOmECO%2B8h9KIf%2BtL2NF%2FCGEfnnDCHEmD3cLRcnk%2BKSS5VUa%2Fc2Aafy%2FToxORWlvvXfq26CYnfmM4%2BQSpL6WiYsbvUHs%2FqJhe66GvPwv%2FPox%2BliEAtKTPfkPb1kfDdMvo887BGeVs1VeUzeHhO7oV8u4W6P%2FNu2GRYWTOIBKS5XJTTOW%2FriDQ0zL%2FjLRsFeJBrz%2FFT%2FQySUKxBLgkwjequL8%2By%2BQN6F1Oe30fY8xl1iNShKj7Qu7OHEnda2xGTw75UXG4oWwpQbnXZmipqyelt%2FB7VGrxw0qLqJR3KELE8z1gYXp3naWaRheObToqaPKSLrycwpU6PXVbYFH%2FChyTvLSHGm%2BCb70k4m7oF1GF7xAIIBQSihv23gFACmCeQ53T7p2K618QTfdbLfZeYH97vcnmU8N0DUIthwr5x30WyfvSidayxn8oYAFBN2%2FgvagvYnugk1tsJGpbYZsHmEjxFzwAvZSBiWwwdmM8E220sj83b%2FOk%2FfosXcFUvOagl320L%2BpnBJYkLzJ%2Fsp3ZPVMNC%2FgL0GOqUBrFWiL5fyWRMifnHLBgs0VzDh3LGJbGM%2FlLoRvXhGbbN2htMJzF%2FJxHDNmSr8YhS5AihSRq4OTBjV53hIADJoEoQDcxkrEW2dJHjS2AqMYCJ4afQdxTnJFWFkVBU7Ja63u7YEc9yfMLBdaxQK9%2Fi54HytN7IRtuwju4sm5h4aueDBgzc%2B1rMVYD31rZDcNh7rsKVdazJXIJgaWho%2BjNem4HqcKIBA&X-Amz-Signature=2fa2987059744a12b08661780f08928b5133fe972a852ba2a9f8632b6b695c2b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SDYFAMB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAbByhzlrA9JRMng91FTYFKSWZhhqqbCvWI6Y35VHBEuAiEA409wZtdvXmaKPLXj5MBsDT37u0nXiCuudBtkuPdRiqwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDICHawlBd9JzbfUxvCrcAxbaUD%2FxkGD7gYhqPuX1PoPjX2HR7f%2B35aowqkAIjqaAggJXbizJz4zPac3B4OGCVDzpfhMsNSTqS3Cle%2FzYftQ757YpdSdsIr1lSB1V%2FkFJonfvX5v5%2FKJyJ4v%2Fiha6DO4ajyOyfqQXElmixoDYS2CdfooEilGnv%2B7qKxO%2B2Hf%2BeewuhH%2FYrsnHv1ImINywQT%2BTlFhOP%2FOOEr6%2BG2Z%2FjcwULhEcnZIOWYUd4k0IxMcl02811GtfDbnqY%2F2rhmhtcYHLcH%2FjbCU8miFq4%2BgvTyXwD3%2ByJBoqW3quB38vI61HjHBhCrzR%2FaPj1n5ZHqBXPEw8WRw%2BqgxaiU8C7J%2BAXnI%2BTHveIdn7y7t6p64H%2FBU%2FJJuCcbDTH3ac9L8i95YYlyiujhXeMtZjbECG%2FBNmBgpQwt37nULLDiQ%2FIPRtx359bZYYh55qQW8DC5QlsWfIrMKzPZHKPhUBRnR8WOF4M3MHcmYpWlZUHqkGhj5TyVP55nFsX9%2FXhJGNUTMKRy9CsIlmGewNkQVZuDpEJD91E3FTkH%2BO%2BzZpV%2B5q3Zvf%2FUq37Ao4lNLLJFrTszaPjp8ezGNaR6zbqQX%2FYzQSfNfX6Vss%2BjaLatQwoqu0s3hCBnmc5HJMCQWQh%2Fx7GuRRMNi%2FgL0GOqUBHtwq0Dv0Jkp8pZhuXawaFPbL%2FujP9LAMqhZCczv7qrVNUTVRMNhDXEmyFK5u8R8GToqBe0Ymnoj7xsTK8vJhipMmoUttKhAqiZrvp8%2BeEI2rRu4sjw9k74qw9mfIebMpb%2BaxMBAUVvHS3bKO6zDBwRu7Sc%2BJ3ZQ3WF15Krhl3Ya%2Bqy7KlRzNFzq9dHiE0yQJ6LvpdgNFE%2B3TG5Q9fhk65x3CG0%2FI&X-Amz-Signature=c2842915c4c43294d6b88da953e34360d24719a778be4316727543cee92dd5e5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SDYFAMB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAbByhzlrA9JRMng91FTYFKSWZhhqqbCvWI6Y35VHBEuAiEA409wZtdvXmaKPLXj5MBsDT37u0nXiCuudBtkuPdRiqwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDICHawlBd9JzbfUxvCrcAxbaUD%2FxkGD7gYhqPuX1PoPjX2HR7f%2B35aowqkAIjqaAggJXbizJz4zPac3B4OGCVDzpfhMsNSTqS3Cle%2FzYftQ757YpdSdsIr1lSB1V%2FkFJonfvX5v5%2FKJyJ4v%2Fiha6DO4ajyOyfqQXElmixoDYS2CdfooEilGnv%2B7qKxO%2B2Hf%2BeewuhH%2FYrsnHv1ImINywQT%2BTlFhOP%2FOOEr6%2BG2Z%2FjcwULhEcnZIOWYUd4k0IxMcl02811GtfDbnqY%2F2rhmhtcYHLcH%2FjbCU8miFq4%2BgvTyXwD3%2ByJBoqW3quB38vI61HjHBhCrzR%2FaPj1n5ZHqBXPEw8WRw%2BqgxaiU8C7J%2BAXnI%2BTHveIdn7y7t6p64H%2FBU%2FJJuCcbDTH3ac9L8i95YYlyiujhXeMtZjbECG%2FBNmBgpQwt37nULLDiQ%2FIPRtx359bZYYh55qQW8DC5QlsWfIrMKzPZHKPhUBRnR8WOF4M3MHcmYpWlZUHqkGhj5TyVP55nFsX9%2FXhJGNUTMKRy9CsIlmGewNkQVZuDpEJD91E3FTkH%2BO%2BzZpV%2B5q3Zvf%2FUq37Ao4lNLLJFrTszaPjp8ezGNaR6zbqQX%2FYzQSfNfX6Vss%2BjaLatQwoqu0s3hCBnmc5HJMCQWQh%2Fx7GuRRMNi%2FgL0GOqUBHtwq0Dv0Jkp8pZhuXawaFPbL%2FujP9LAMqhZCczv7qrVNUTVRMNhDXEmyFK5u8R8GToqBe0Ymnoj7xsTK8vJhipMmoUttKhAqiZrvp8%2BeEI2rRu4sjw9k74qw9mfIebMpb%2BaxMBAUVvHS3bKO6zDBwRu7Sc%2BJ3ZQ3WF15Krhl3Ya%2Bqy7KlRzNFzq9dHiE0yQJ6LvpdgNFE%2B3TG5Q9fhk65x3CG0%2FI&X-Amz-Signature=abea259e323ea135f78f14503b0ab78c35a049cfce2ab52bbf664b4a3248bdcf&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SDYFAMB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAbByhzlrA9JRMng91FTYFKSWZhhqqbCvWI6Y35VHBEuAiEA409wZtdvXmaKPLXj5MBsDT37u0nXiCuudBtkuPdRiqwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDICHawlBd9JzbfUxvCrcAxbaUD%2FxkGD7gYhqPuX1PoPjX2HR7f%2B35aowqkAIjqaAggJXbizJz4zPac3B4OGCVDzpfhMsNSTqS3Cle%2FzYftQ757YpdSdsIr1lSB1V%2FkFJonfvX5v5%2FKJyJ4v%2Fiha6DO4ajyOyfqQXElmixoDYS2CdfooEilGnv%2B7qKxO%2B2Hf%2BeewuhH%2FYrsnHv1ImINywQT%2BTlFhOP%2FOOEr6%2BG2Z%2FjcwULhEcnZIOWYUd4k0IxMcl02811GtfDbnqY%2F2rhmhtcYHLcH%2FjbCU8miFq4%2BgvTyXwD3%2ByJBoqW3quB38vI61HjHBhCrzR%2FaPj1n5ZHqBXPEw8WRw%2BqgxaiU8C7J%2BAXnI%2BTHveIdn7y7t6p64H%2FBU%2FJJuCcbDTH3ac9L8i95YYlyiujhXeMtZjbECG%2FBNmBgpQwt37nULLDiQ%2FIPRtx359bZYYh55qQW8DC5QlsWfIrMKzPZHKPhUBRnR8WOF4M3MHcmYpWlZUHqkGhj5TyVP55nFsX9%2FXhJGNUTMKRy9CsIlmGewNkQVZuDpEJD91E3FTkH%2BO%2BzZpV%2B5q3Zvf%2FUq37Ao4lNLLJFrTszaPjp8ezGNaR6zbqQX%2FYzQSfNfX6Vss%2BjaLatQwoqu0s3hCBnmc5HJMCQWQh%2Fx7GuRRMNi%2FgL0GOqUBHtwq0Dv0Jkp8pZhuXawaFPbL%2FujP9LAMqhZCczv7qrVNUTVRMNhDXEmyFK5u8R8GToqBe0Ymnoj7xsTK8vJhipMmoUttKhAqiZrvp8%2BeEI2rRu4sjw9k74qw9mfIebMpb%2BaxMBAUVvHS3bKO6zDBwRu7Sc%2BJ3ZQ3WF15Krhl3Ya%2Bqy7KlRzNFzq9dHiE0yQJ6LvpdgNFE%2B3TG5Q9fhk65x3CG0%2FI&X-Amz-Signature=13158ae0d5616c9ac9f341f813b91318eb61a8027283a6a9d12251fa23c7ce36&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SDYFAMB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAbByhzlrA9JRMng91FTYFKSWZhhqqbCvWI6Y35VHBEuAiEA409wZtdvXmaKPLXj5MBsDT37u0nXiCuudBtkuPdRiqwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDICHawlBd9JzbfUxvCrcAxbaUD%2FxkGD7gYhqPuX1PoPjX2HR7f%2B35aowqkAIjqaAggJXbizJz4zPac3B4OGCVDzpfhMsNSTqS3Cle%2FzYftQ757YpdSdsIr1lSB1V%2FkFJonfvX5v5%2FKJyJ4v%2Fiha6DO4ajyOyfqQXElmixoDYS2CdfooEilGnv%2B7qKxO%2B2Hf%2BeewuhH%2FYrsnHv1ImINywQT%2BTlFhOP%2FOOEr6%2BG2Z%2FjcwULhEcnZIOWYUd4k0IxMcl02811GtfDbnqY%2F2rhmhtcYHLcH%2FjbCU8miFq4%2BgvTyXwD3%2ByJBoqW3quB38vI61HjHBhCrzR%2FaPj1n5ZHqBXPEw8WRw%2BqgxaiU8C7J%2BAXnI%2BTHveIdn7y7t6p64H%2FBU%2FJJuCcbDTH3ac9L8i95YYlyiujhXeMtZjbECG%2FBNmBgpQwt37nULLDiQ%2FIPRtx359bZYYh55qQW8DC5QlsWfIrMKzPZHKPhUBRnR8WOF4M3MHcmYpWlZUHqkGhj5TyVP55nFsX9%2FXhJGNUTMKRy9CsIlmGewNkQVZuDpEJD91E3FTkH%2BO%2BzZpV%2B5q3Zvf%2FUq37Ao4lNLLJFrTszaPjp8ezGNaR6zbqQX%2FYzQSfNfX6Vss%2BjaLatQwoqu0s3hCBnmc5HJMCQWQh%2Fx7GuRRMNi%2FgL0GOqUBHtwq0Dv0Jkp8pZhuXawaFPbL%2FujP9LAMqhZCczv7qrVNUTVRMNhDXEmyFK5u8R8GToqBe0Ymnoj7xsTK8vJhipMmoUttKhAqiZrvp8%2BeEI2rRu4sjw9k74qw9mfIebMpb%2BaxMBAUVvHS3bKO6zDBwRu7Sc%2BJ3ZQ3WF15Krhl3Ya%2Bqy7KlRzNFzq9dHiE0yQJ6LvpdgNFE%2B3TG5Q9fhk65x3CG0%2FI&X-Amz-Signature=35001fa46cf664bb26ad020881b517394f73e3ccf69ff8289c265b866dc1565a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SDYFAMB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAbByhzlrA9JRMng91FTYFKSWZhhqqbCvWI6Y35VHBEuAiEA409wZtdvXmaKPLXj5MBsDT37u0nXiCuudBtkuPdRiqwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDICHawlBd9JzbfUxvCrcAxbaUD%2FxkGD7gYhqPuX1PoPjX2HR7f%2B35aowqkAIjqaAggJXbizJz4zPac3B4OGCVDzpfhMsNSTqS3Cle%2FzYftQ757YpdSdsIr1lSB1V%2FkFJonfvX5v5%2FKJyJ4v%2Fiha6DO4ajyOyfqQXElmixoDYS2CdfooEilGnv%2B7qKxO%2B2Hf%2BeewuhH%2FYrsnHv1ImINywQT%2BTlFhOP%2FOOEr6%2BG2Z%2FjcwULhEcnZIOWYUd4k0IxMcl02811GtfDbnqY%2F2rhmhtcYHLcH%2FjbCU8miFq4%2BgvTyXwD3%2ByJBoqW3quB38vI61HjHBhCrzR%2FaPj1n5ZHqBXPEw8WRw%2BqgxaiU8C7J%2BAXnI%2BTHveIdn7y7t6p64H%2FBU%2FJJuCcbDTH3ac9L8i95YYlyiujhXeMtZjbECG%2FBNmBgpQwt37nULLDiQ%2FIPRtx359bZYYh55qQW8DC5QlsWfIrMKzPZHKPhUBRnR8WOF4M3MHcmYpWlZUHqkGhj5TyVP55nFsX9%2FXhJGNUTMKRy9CsIlmGewNkQVZuDpEJD91E3FTkH%2BO%2BzZpV%2B5q3Zvf%2FUq37Ao4lNLLJFrTszaPjp8ezGNaR6zbqQX%2FYzQSfNfX6Vss%2BjaLatQwoqu0s3hCBnmc5HJMCQWQh%2Fx7GuRRMNi%2FgL0GOqUBHtwq0Dv0Jkp8pZhuXawaFPbL%2FujP9LAMqhZCczv7qrVNUTVRMNhDXEmyFK5u8R8GToqBe0Ymnoj7xsTK8vJhipMmoUttKhAqiZrvp8%2BeEI2rRu4sjw9k74qw9mfIebMpb%2BaxMBAUVvHS3bKO6zDBwRu7Sc%2BJ3ZQ3WF15Krhl3Ya%2Bqy7KlRzNFzq9dHiE0yQJ6LvpdgNFE%2B3TG5Q9fhk65x3CG0%2FI&X-Amz-Signature=360f29ba2c5b60ff55d726e5f41572dcaefdee8f7826d68baff1a828a077676c&X-Amz-SignedHeaders=host&x-id=GetObject)
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


