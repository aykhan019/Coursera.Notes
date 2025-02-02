

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXZSLHJH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbyz2ZaSA9LzlEX6JRp8ribyUGHL1W40YvBfNE4%2BGTxAiBYYMisOecY6IejiJytI%2BsgE2zzf%2Be4m0%2BgGXVNLJChayqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2v76rxWLVzGSQm7fKtwDuoqhZU%2BEOCgFLiCN2Ue8xGeTtQ%2BZEsff23p%2Fg%2F4H0L3M5gK%2BXP%2BUXNXGuaXO0%2F5AWKmTG5UdSZHYcV0TO77esWdv9Ia2ijY%2BoGNFdqoNtMasK45IEodLrwpsQe5dI1UeHWwlLKj8L8LlJUsrhzf5ADZCkUoCS8PHyLduhtrd5AjwHoWnQCunFbm5w5XkHUDw5D4zaFWiID%2Fi5LO4HoIRUoRfSoemt8OE0lH93f4H6bbFUbWfhdRXSoFhUyjqQOtg%2FmYo8Q00%2Fdv8oIZQkUPRTqlx%2F8Nt9V1G6DWAXTpBxjVrV3ADJfZ%2BY212yzHaoRAMduy4HiuLqDiYhU3NfyFXwaQzYvDUQM5W2er%2BujgOhsEI1YWhbBfb7pHfNccB33Q4dFe4xVK4Wp6cqPoEF0FNR0Rj%2ByL2qQ6BLNSvx1KNictcZqkdhCs26hl1l200ec6%2BXeHreW%2FEYfxFYOfhuxPDEKFz2ivvQVPpmgBe1DCW%2BFtY4pC3svD2G%2FusuLLdCfxMHDTZOyWzABa%2FIfNU6lmptA9P7O6oL7Ix9m3pVGOdWn%2BbOj%2BHvGSZCNJ3%2F92IzeBBCTqE%2FsX8VhB5xq7WiekmSlTzpiDN61WqCeehjGwi10FRiCnNiAmNq8VJg4ww1%2BH7vAY6pgFORx%2BwGUxxAIK2tidQ8BW3N7gm0Cp1XEG9dyDCOG%2BwNib9d4nzPMjdleRQkcHcpwwIYXu1RDwrSEFMDNM8ndpehmLftvn60VQbq3H5LrmhHOdvmG%2FSlMwpQtlgiOCrhIrZi%2FrLZ9Er%2FoMG%2Fju4Cp9Ff4w3RHfPyg%2BEl3KZT%2B%2F7PUtx%2F9B9OFashJhxmBPZwk7Z8MOFout0DacvJ4IaPss3y7vsfyLi&X-Amz-Signature=d62a8b9c95ec1358277b602ff7293af763042bd6a6dbd783a6729ab266ec8e36&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664E4AVGMJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnuxPSmfxGlzD7JhL4vgqA1VlBNFjR1OoA5aRmPZTM2AIhAN5b%2FtY9lbpeF8l%2FWo8ikrw%2FB8GYjLxv8MQGnCz4IkenKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ4XonR2A4Q50F6jUq3AOyNoKsxoXOY0gH8nZultPwA6sBhwX5TUHrrSGsRfDMZ6t1gmwBYj1C4OR0wRbnBfK3CW5HzzIxOLQWPLFqsBtjWSAAIcL1muo1nXYanCb%2BnFhEpW%2FKJ6QoK%2BZKdfNOXwgjbNke%2FY%2BTALUCx99UOPv9tsmAQFkulDfMVrm%2Blu4nducVo0RNi%2FZQZWurYfdxCcTPEsPLJVswPnEUjA%2BbnBX1NDRnMj3zVM7CkEAp4BtZUu2n%2FyMhenvIwRpo5qbJtQhAxHFHR8Ntmf02XCKAiADISPD5OWGbV6zUfRhrONDKofaSUYI71dBCCSZ%2BmpOzlmThDHO4UQHMzFrZ87S%2F5ynaCtnDD8JNcVeiLHOteKIe0G%2FdvkEXfBjFrvdv7sv4LnuHs8rUuNRSQFMf5R4omRFEi1A03rSmu8Y8FRpwZRnXvIsR0nktG8aEd4dyIOA3iVvAPM%2BZm84ydMnc8Aiqty6cB6iSkI1fxgUUhK76G0%2B%2FkSm6ZLt%2FehUE8h3nWey%2FObBgNx%2BH0SuNWeWZ2%2FLG43FoY%2B0evpN2%2B1B6O0eXFduyV00YuJWfJcllWp%2FwuLtriz4uict0S6HI%2F%2BmfuuME2ZBlFpeiKO2DM4HXoNhsYXfW5ArZgrE4cbHlrz%2Bg9TCq4fu8BjqkAfPatA4KrY%2BmMdlzeuCHmPfD7EOYR%2Fr1N%2FoyDyAbVTISmFkzo1fpcpVpC2nlol7fsQut8hdsPXM1N6uTZpJ4QYMsSzQ8HGs1ZWNWVRIA0SlXSlIH3d74FJX7Ep%2BALEieIs%2BrXAuJl4F6vwM3a%2Fpw%2FAjjS6BWS%2Fv8cd%2F2pGCnrQSiGTsyOHPuQtKxDkdIFTdO0K0AUbdwdzRvZnTwUkQdhscf4%2B7I&X-Amz-Signature=dd434d9c26aa4f5f3e3557c5530e37d4d6f12c29030f12eaa63b705d3b1f0fc4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664E4AVGMJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnuxPSmfxGlzD7JhL4vgqA1VlBNFjR1OoA5aRmPZTM2AIhAN5b%2FtY9lbpeF8l%2FWo8ikrw%2FB8GYjLxv8MQGnCz4IkenKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ4XonR2A4Q50F6jUq3AOyNoKsxoXOY0gH8nZultPwA6sBhwX5TUHrrSGsRfDMZ6t1gmwBYj1C4OR0wRbnBfK3CW5HzzIxOLQWPLFqsBtjWSAAIcL1muo1nXYanCb%2BnFhEpW%2FKJ6QoK%2BZKdfNOXwgjbNke%2FY%2BTALUCx99UOPv9tsmAQFkulDfMVrm%2Blu4nducVo0RNi%2FZQZWurYfdxCcTPEsPLJVswPnEUjA%2BbnBX1NDRnMj3zVM7CkEAp4BtZUu2n%2FyMhenvIwRpo5qbJtQhAxHFHR8Ntmf02XCKAiADISPD5OWGbV6zUfRhrONDKofaSUYI71dBCCSZ%2BmpOzlmThDHO4UQHMzFrZ87S%2F5ynaCtnDD8JNcVeiLHOteKIe0G%2FdvkEXfBjFrvdv7sv4LnuHs8rUuNRSQFMf5R4omRFEi1A03rSmu8Y8FRpwZRnXvIsR0nktG8aEd4dyIOA3iVvAPM%2BZm84ydMnc8Aiqty6cB6iSkI1fxgUUhK76G0%2B%2FkSm6ZLt%2FehUE8h3nWey%2FObBgNx%2BH0SuNWeWZ2%2FLG43FoY%2B0evpN2%2B1B6O0eXFduyV00YuJWfJcllWp%2FwuLtriz4uict0S6HI%2F%2BmfuuME2ZBlFpeiKO2DM4HXoNhsYXfW5ArZgrE4cbHlrz%2Bg9TCq4fu8BjqkAfPatA4KrY%2BmMdlzeuCHmPfD7EOYR%2Fr1N%2FoyDyAbVTISmFkzo1fpcpVpC2nlol7fsQut8hdsPXM1N6uTZpJ4QYMsSzQ8HGs1ZWNWVRIA0SlXSlIH3d74FJX7Ep%2BALEieIs%2BrXAuJl4F6vwM3a%2Fpw%2FAjjS6BWS%2Fv8cd%2F2pGCnrQSiGTsyOHPuQtKxDkdIFTdO0K0AUbdwdzRvZnTwUkQdhscf4%2B7I&X-Amz-Signature=5769c88910dabf520ea67e8b752129ddbd53e2f980d91e8f0397a2cef19b42c5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664E4AVGMJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnuxPSmfxGlzD7JhL4vgqA1VlBNFjR1OoA5aRmPZTM2AIhAN5b%2FtY9lbpeF8l%2FWo8ikrw%2FB8GYjLxv8MQGnCz4IkenKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ4XonR2A4Q50F6jUq3AOyNoKsxoXOY0gH8nZultPwA6sBhwX5TUHrrSGsRfDMZ6t1gmwBYj1C4OR0wRbnBfK3CW5HzzIxOLQWPLFqsBtjWSAAIcL1muo1nXYanCb%2BnFhEpW%2FKJ6QoK%2BZKdfNOXwgjbNke%2FY%2BTALUCx99UOPv9tsmAQFkulDfMVrm%2Blu4nducVo0RNi%2FZQZWurYfdxCcTPEsPLJVswPnEUjA%2BbnBX1NDRnMj3zVM7CkEAp4BtZUu2n%2FyMhenvIwRpo5qbJtQhAxHFHR8Ntmf02XCKAiADISPD5OWGbV6zUfRhrONDKofaSUYI71dBCCSZ%2BmpOzlmThDHO4UQHMzFrZ87S%2F5ynaCtnDD8JNcVeiLHOteKIe0G%2FdvkEXfBjFrvdv7sv4LnuHs8rUuNRSQFMf5R4omRFEi1A03rSmu8Y8FRpwZRnXvIsR0nktG8aEd4dyIOA3iVvAPM%2BZm84ydMnc8Aiqty6cB6iSkI1fxgUUhK76G0%2B%2FkSm6ZLt%2FehUE8h3nWey%2FObBgNx%2BH0SuNWeWZ2%2FLG43FoY%2B0evpN2%2B1B6O0eXFduyV00YuJWfJcllWp%2FwuLtriz4uict0S6HI%2F%2BmfuuME2ZBlFpeiKO2DM4HXoNhsYXfW5ArZgrE4cbHlrz%2Bg9TCq4fu8BjqkAfPatA4KrY%2BmMdlzeuCHmPfD7EOYR%2Fr1N%2FoyDyAbVTISmFkzo1fpcpVpC2nlol7fsQut8hdsPXM1N6uTZpJ4QYMsSzQ8HGs1ZWNWVRIA0SlXSlIH3d74FJX7Ep%2BALEieIs%2BrXAuJl4F6vwM3a%2Fpw%2FAjjS6BWS%2Fv8cd%2F2pGCnrQSiGTsyOHPuQtKxDkdIFTdO0K0AUbdwdzRvZnTwUkQdhscf4%2B7I&X-Amz-Signature=91834d6588384bdaad962a6eeddc2ac11b3772de52a8aa28a3e06a4e441f4c68&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664E4AVGMJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnuxPSmfxGlzD7JhL4vgqA1VlBNFjR1OoA5aRmPZTM2AIhAN5b%2FtY9lbpeF8l%2FWo8ikrw%2FB8GYjLxv8MQGnCz4IkenKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ4XonR2A4Q50F6jUq3AOyNoKsxoXOY0gH8nZultPwA6sBhwX5TUHrrSGsRfDMZ6t1gmwBYj1C4OR0wRbnBfK3CW5HzzIxOLQWPLFqsBtjWSAAIcL1muo1nXYanCb%2BnFhEpW%2FKJ6QoK%2BZKdfNOXwgjbNke%2FY%2BTALUCx99UOPv9tsmAQFkulDfMVrm%2Blu4nducVo0RNi%2FZQZWurYfdxCcTPEsPLJVswPnEUjA%2BbnBX1NDRnMj3zVM7CkEAp4BtZUu2n%2FyMhenvIwRpo5qbJtQhAxHFHR8Ntmf02XCKAiADISPD5OWGbV6zUfRhrONDKofaSUYI71dBCCSZ%2BmpOzlmThDHO4UQHMzFrZ87S%2F5ynaCtnDD8JNcVeiLHOteKIe0G%2FdvkEXfBjFrvdv7sv4LnuHs8rUuNRSQFMf5R4omRFEi1A03rSmu8Y8FRpwZRnXvIsR0nktG8aEd4dyIOA3iVvAPM%2BZm84ydMnc8Aiqty6cB6iSkI1fxgUUhK76G0%2B%2FkSm6ZLt%2FehUE8h3nWey%2FObBgNx%2BH0SuNWeWZ2%2FLG43FoY%2B0evpN2%2B1B6O0eXFduyV00YuJWfJcllWp%2FwuLtriz4uict0S6HI%2F%2BmfuuME2ZBlFpeiKO2DM4HXoNhsYXfW5ArZgrE4cbHlrz%2Bg9TCq4fu8BjqkAfPatA4KrY%2BmMdlzeuCHmPfD7EOYR%2Fr1N%2FoyDyAbVTISmFkzo1fpcpVpC2nlol7fsQut8hdsPXM1N6uTZpJ4QYMsSzQ8HGs1ZWNWVRIA0SlXSlIH3d74FJX7Ep%2BALEieIs%2BrXAuJl4F6vwM3a%2Fpw%2FAjjS6BWS%2Fv8cd%2F2pGCnrQSiGTsyOHPuQtKxDkdIFTdO0K0AUbdwdzRvZnTwUkQdhscf4%2B7I&X-Amz-Signature=cfb55d3cd9e625391844268632a35c0c43319870f47c33966706a7fbaf9ff562&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664E4AVGMJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnuxPSmfxGlzD7JhL4vgqA1VlBNFjR1OoA5aRmPZTM2AIhAN5b%2FtY9lbpeF8l%2FWo8ikrw%2FB8GYjLxv8MQGnCz4IkenKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ4XonR2A4Q50F6jUq3AOyNoKsxoXOY0gH8nZultPwA6sBhwX5TUHrrSGsRfDMZ6t1gmwBYj1C4OR0wRbnBfK3CW5HzzIxOLQWPLFqsBtjWSAAIcL1muo1nXYanCb%2BnFhEpW%2FKJ6QoK%2BZKdfNOXwgjbNke%2FY%2BTALUCx99UOPv9tsmAQFkulDfMVrm%2Blu4nducVo0RNi%2FZQZWurYfdxCcTPEsPLJVswPnEUjA%2BbnBX1NDRnMj3zVM7CkEAp4BtZUu2n%2FyMhenvIwRpo5qbJtQhAxHFHR8Ntmf02XCKAiADISPD5OWGbV6zUfRhrONDKofaSUYI71dBCCSZ%2BmpOzlmThDHO4UQHMzFrZ87S%2F5ynaCtnDD8JNcVeiLHOteKIe0G%2FdvkEXfBjFrvdv7sv4LnuHs8rUuNRSQFMf5R4omRFEi1A03rSmu8Y8FRpwZRnXvIsR0nktG8aEd4dyIOA3iVvAPM%2BZm84ydMnc8Aiqty6cB6iSkI1fxgUUhK76G0%2B%2FkSm6ZLt%2FehUE8h3nWey%2FObBgNx%2BH0SuNWeWZ2%2FLG43FoY%2B0evpN2%2B1B6O0eXFduyV00YuJWfJcllWp%2FwuLtriz4uict0S6HI%2F%2BmfuuME2ZBlFpeiKO2DM4HXoNhsYXfW5ArZgrE4cbHlrz%2Bg9TCq4fu8BjqkAfPatA4KrY%2BmMdlzeuCHmPfD7EOYR%2Fr1N%2FoyDyAbVTISmFkzo1fpcpVpC2nlol7fsQut8hdsPXM1N6uTZpJ4QYMsSzQ8HGs1ZWNWVRIA0SlXSlIH3d74FJX7Ep%2BALEieIs%2BrXAuJl4F6vwM3a%2Fpw%2FAjjS6BWS%2Fv8cd%2F2pGCnrQSiGTsyOHPuQtKxDkdIFTdO0K0AUbdwdzRvZnTwUkQdhscf4%2B7I&X-Amz-Signature=eca458b4413cf1256ccc7ae3c57047a7af5381b81f0e1de486c706f536d249ad&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXZSLHJH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbyz2ZaSA9LzlEX6JRp8ribyUGHL1W40YvBfNE4%2BGTxAiBYYMisOecY6IejiJytI%2BsgE2zzf%2Be4m0%2BgGXVNLJChayqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2v76rxWLVzGSQm7fKtwDuoqhZU%2BEOCgFLiCN2Ue8xGeTtQ%2BZEsff23p%2Fg%2F4H0L3M5gK%2BXP%2BUXNXGuaXO0%2F5AWKmTG5UdSZHYcV0TO77esWdv9Ia2ijY%2BoGNFdqoNtMasK45IEodLrwpsQe5dI1UeHWwlLKj8L8LlJUsrhzf5ADZCkUoCS8PHyLduhtrd5AjwHoWnQCunFbm5w5XkHUDw5D4zaFWiID%2Fi5LO4HoIRUoRfSoemt8OE0lH93f4H6bbFUbWfhdRXSoFhUyjqQOtg%2FmYo8Q00%2Fdv8oIZQkUPRTqlx%2F8Nt9V1G6DWAXTpBxjVrV3ADJfZ%2BY212yzHaoRAMduy4HiuLqDiYhU3NfyFXwaQzYvDUQM5W2er%2BujgOhsEI1YWhbBfb7pHfNccB33Q4dFe4xVK4Wp6cqPoEF0FNR0Rj%2ByL2qQ6BLNSvx1KNictcZqkdhCs26hl1l200ec6%2BXeHreW%2FEYfxFYOfhuxPDEKFz2ivvQVPpmgBe1DCW%2BFtY4pC3svD2G%2FusuLLdCfxMHDTZOyWzABa%2FIfNU6lmptA9P7O6oL7Ix9m3pVGOdWn%2BbOj%2BHvGSZCNJ3%2F92IzeBBCTqE%2FsX8VhB5xq7WiekmSlTzpiDN61WqCeehjGwi10FRiCnNiAmNq8VJg4ww1%2BH7vAY6pgFORx%2BwGUxxAIK2tidQ8BW3N7gm0Cp1XEG9dyDCOG%2BwNib9d4nzPMjdleRQkcHcpwwIYXu1RDwrSEFMDNM8ndpehmLftvn60VQbq3H5LrmhHOdvmG%2FSlMwpQtlgiOCrhIrZi%2FrLZ9Er%2FoMG%2Fju4Cp9Ff4w3RHfPyg%2BEl3KZT%2B%2F7PUtx%2F9B9OFashJhxmBPZwk7Z8MOFout0DacvJ4IaPss3y7vsfyLi&X-Amz-Signature=a4f4479c5770c610a2c83fcdde196626d9cf29ae8aeff5af334279e451e02cb9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXZSLHJH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbyz2ZaSA9LzlEX6JRp8ribyUGHL1W40YvBfNE4%2BGTxAiBYYMisOecY6IejiJytI%2BsgE2zzf%2Be4m0%2BgGXVNLJChayqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2v76rxWLVzGSQm7fKtwDuoqhZU%2BEOCgFLiCN2Ue8xGeTtQ%2BZEsff23p%2Fg%2F4H0L3M5gK%2BXP%2BUXNXGuaXO0%2F5AWKmTG5UdSZHYcV0TO77esWdv9Ia2ijY%2BoGNFdqoNtMasK45IEodLrwpsQe5dI1UeHWwlLKj8L8LlJUsrhzf5ADZCkUoCS8PHyLduhtrd5AjwHoWnQCunFbm5w5XkHUDw5D4zaFWiID%2Fi5LO4HoIRUoRfSoemt8OE0lH93f4H6bbFUbWfhdRXSoFhUyjqQOtg%2FmYo8Q00%2Fdv8oIZQkUPRTqlx%2F8Nt9V1G6DWAXTpBxjVrV3ADJfZ%2BY212yzHaoRAMduy4HiuLqDiYhU3NfyFXwaQzYvDUQM5W2er%2BujgOhsEI1YWhbBfb7pHfNccB33Q4dFe4xVK4Wp6cqPoEF0FNR0Rj%2ByL2qQ6BLNSvx1KNictcZqkdhCs26hl1l200ec6%2BXeHreW%2FEYfxFYOfhuxPDEKFz2ivvQVPpmgBe1DCW%2BFtY4pC3svD2G%2FusuLLdCfxMHDTZOyWzABa%2FIfNU6lmptA9P7O6oL7Ix9m3pVGOdWn%2BbOj%2BHvGSZCNJ3%2F92IzeBBCTqE%2FsX8VhB5xq7WiekmSlTzpiDN61WqCeehjGwi10FRiCnNiAmNq8VJg4ww1%2BH7vAY6pgFORx%2BwGUxxAIK2tidQ8BW3N7gm0Cp1XEG9dyDCOG%2BwNib9d4nzPMjdleRQkcHcpwwIYXu1RDwrSEFMDNM8ndpehmLftvn60VQbq3H5LrmhHOdvmG%2FSlMwpQtlgiOCrhIrZi%2FrLZ9Er%2FoMG%2Fju4Cp9Ff4w3RHfPyg%2BEl3KZT%2B%2F7PUtx%2F9B9OFashJhxmBPZwk7Z8MOFout0DacvJ4IaPss3y7vsfyLi&X-Amz-Signature=dd6742b1746528681be0d1ac7e25ac638f87c416d59239d3cfa1ac4fcde7a7c8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXZSLHJH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbyz2ZaSA9LzlEX6JRp8ribyUGHL1W40YvBfNE4%2BGTxAiBYYMisOecY6IejiJytI%2BsgE2zzf%2Be4m0%2BgGXVNLJChayqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2v76rxWLVzGSQm7fKtwDuoqhZU%2BEOCgFLiCN2Ue8xGeTtQ%2BZEsff23p%2Fg%2F4H0L3M5gK%2BXP%2BUXNXGuaXO0%2F5AWKmTG5UdSZHYcV0TO77esWdv9Ia2ijY%2BoGNFdqoNtMasK45IEodLrwpsQe5dI1UeHWwlLKj8L8LlJUsrhzf5ADZCkUoCS8PHyLduhtrd5AjwHoWnQCunFbm5w5XkHUDw5D4zaFWiID%2Fi5LO4HoIRUoRfSoemt8OE0lH93f4H6bbFUbWfhdRXSoFhUyjqQOtg%2FmYo8Q00%2Fdv8oIZQkUPRTqlx%2F8Nt9V1G6DWAXTpBxjVrV3ADJfZ%2BY212yzHaoRAMduy4HiuLqDiYhU3NfyFXwaQzYvDUQM5W2er%2BujgOhsEI1YWhbBfb7pHfNccB33Q4dFe4xVK4Wp6cqPoEF0FNR0Rj%2ByL2qQ6BLNSvx1KNictcZqkdhCs26hl1l200ec6%2BXeHreW%2FEYfxFYOfhuxPDEKFz2ivvQVPpmgBe1DCW%2BFtY4pC3svD2G%2FusuLLdCfxMHDTZOyWzABa%2FIfNU6lmptA9P7O6oL7Ix9m3pVGOdWn%2BbOj%2BHvGSZCNJ3%2F92IzeBBCTqE%2FsX8VhB5xq7WiekmSlTzpiDN61WqCeehjGwi10FRiCnNiAmNq8VJg4ww1%2BH7vAY6pgFORx%2BwGUxxAIK2tidQ8BW3N7gm0Cp1XEG9dyDCOG%2BwNib9d4nzPMjdleRQkcHcpwwIYXu1RDwrSEFMDNM8ndpehmLftvn60VQbq3H5LrmhHOdvmG%2FSlMwpQtlgiOCrhIrZi%2FrLZ9Er%2FoMG%2Fju4Cp9Ff4w3RHfPyg%2BEl3KZT%2B%2F7PUtx%2F9B9OFashJhxmBPZwk7Z8MOFout0DacvJ4IaPss3y7vsfyLi&X-Amz-Signature=9438f14096b4d74f5144643d187f4f9222367cd8187dcf7de404b28a318827e6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXZSLHJH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbyz2ZaSA9LzlEX6JRp8ribyUGHL1W40YvBfNE4%2BGTxAiBYYMisOecY6IejiJytI%2BsgE2zzf%2Be4m0%2BgGXVNLJChayqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2v76rxWLVzGSQm7fKtwDuoqhZU%2BEOCgFLiCN2Ue8xGeTtQ%2BZEsff23p%2Fg%2F4H0L3M5gK%2BXP%2BUXNXGuaXO0%2F5AWKmTG5UdSZHYcV0TO77esWdv9Ia2ijY%2BoGNFdqoNtMasK45IEodLrwpsQe5dI1UeHWwlLKj8L8LlJUsrhzf5ADZCkUoCS8PHyLduhtrd5AjwHoWnQCunFbm5w5XkHUDw5D4zaFWiID%2Fi5LO4HoIRUoRfSoemt8OE0lH93f4H6bbFUbWfhdRXSoFhUyjqQOtg%2FmYo8Q00%2Fdv8oIZQkUPRTqlx%2F8Nt9V1G6DWAXTpBxjVrV3ADJfZ%2BY212yzHaoRAMduy4HiuLqDiYhU3NfyFXwaQzYvDUQM5W2er%2BujgOhsEI1YWhbBfb7pHfNccB33Q4dFe4xVK4Wp6cqPoEF0FNR0Rj%2ByL2qQ6BLNSvx1KNictcZqkdhCs26hl1l200ec6%2BXeHreW%2FEYfxFYOfhuxPDEKFz2ivvQVPpmgBe1DCW%2BFtY4pC3svD2G%2FusuLLdCfxMHDTZOyWzABa%2FIfNU6lmptA9P7O6oL7Ix9m3pVGOdWn%2BbOj%2BHvGSZCNJ3%2F92IzeBBCTqE%2FsX8VhB5xq7WiekmSlTzpiDN61WqCeehjGwi10FRiCnNiAmNq8VJg4ww1%2BH7vAY6pgFORx%2BwGUxxAIK2tidQ8BW3N7gm0Cp1XEG9dyDCOG%2BwNib9d4nzPMjdleRQkcHcpwwIYXu1RDwrSEFMDNM8ndpehmLftvn60VQbq3H5LrmhHOdvmG%2FSlMwpQtlgiOCrhIrZi%2FrLZ9Er%2FoMG%2Fju4Cp9Ff4w3RHfPyg%2BEl3KZT%2B%2F7PUtx%2F9B9OFashJhxmBPZwk7Z8MOFout0DacvJ4IaPss3y7vsfyLi&X-Amz-Signature=f84959caf39edef568a6348aa52fdd1f59ac2b8f84570f4d2322441df480adc0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXZSLHJH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbyz2ZaSA9LzlEX6JRp8ribyUGHL1W40YvBfNE4%2BGTxAiBYYMisOecY6IejiJytI%2BsgE2zzf%2Be4m0%2BgGXVNLJChayqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2v76rxWLVzGSQm7fKtwDuoqhZU%2BEOCgFLiCN2Ue8xGeTtQ%2BZEsff23p%2Fg%2F4H0L3M5gK%2BXP%2BUXNXGuaXO0%2F5AWKmTG5UdSZHYcV0TO77esWdv9Ia2ijY%2BoGNFdqoNtMasK45IEodLrwpsQe5dI1UeHWwlLKj8L8LlJUsrhzf5ADZCkUoCS8PHyLduhtrd5AjwHoWnQCunFbm5w5XkHUDw5D4zaFWiID%2Fi5LO4HoIRUoRfSoemt8OE0lH93f4H6bbFUbWfhdRXSoFhUyjqQOtg%2FmYo8Q00%2Fdv8oIZQkUPRTqlx%2F8Nt9V1G6DWAXTpBxjVrV3ADJfZ%2BY212yzHaoRAMduy4HiuLqDiYhU3NfyFXwaQzYvDUQM5W2er%2BujgOhsEI1YWhbBfb7pHfNccB33Q4dFe4xVK4Wp6cqPoEF0FNR0Rj%2ByL2qQ6BLNSvx1KNictcZqkdhCs26hl1l200ec6%2BXeHreW%2FEYfxFYOfhuxPDEKFz2ivvQVPpmgBe1DCW%2BFtY4pC3svD2G%2FusuLLdCfxMHDTZOyWzABa%2FIfNU6lmptA9P7O6oL7Ix9m3pVGOdWn%2BbOj%2BHvGSZCNJ3%2F92IzeBBCTqE%2FsX8VhB5xq7WiekmSlTzpiDN61WqCeehjGwi10FRiCnNiAmNq8VJg4ww1%2BH7vAY6pgFORx%2BwGUxxAIK2tidQ8BW3N7gm0Cp1XEG9dyDCOG%2BwNib9d4nzPMjdleRQkcHcpwwIYXu1RDwrSEFMDNM8ndpehmLftvn60VQbq3H5LrmhHOdvmG%2FSlMwpQtlgiOCrhIrZi%2FrLZ9Er%2FoMG%2Fju4Cp9Ff4w3RHfPyg%2BEl3KZT%2B%2F7PUtx%2F9B9OFashJhxmBPZwk7Z8MOFout0DacvJ4IaPss3y7vsfyLi&X-Amz-Signature=e9ade1489c6b500335f0ba2fec3f6a676f7a9e047fc4102ab8e87073447e89bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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


