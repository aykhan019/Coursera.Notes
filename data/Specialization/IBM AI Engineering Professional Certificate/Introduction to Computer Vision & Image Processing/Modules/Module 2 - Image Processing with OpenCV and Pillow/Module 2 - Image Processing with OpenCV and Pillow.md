

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROXN5V7G%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEMzvDESaq9KuLZx7OgSRwQ8Au5lUEr61o1iZwDYSsKAiAUQkbO%2FU%2F%2BP%2B%2BoiPn3Rz8nZcqF5yup0O4ATKuPEY6uFiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFuYmUTekOrg15kGoKtwDuK%2FnBJKvsBkNOdZ0z99vW0DKFlJUpV%2FJvLYPYjrUpv7hCAi86gTnq%2FvqXUfMgjT22C02K8iTDfLIT9Vle0FBsFn8Y6DrLtlWpqwaD6eplVF9Ptc2Vnmje%2BI3VWKCHG5DfrkQ9BZ%2FKulShG%2FeEm9daDzcMnYIXZnh5QCKJp91ti8t8GfBEhJy4ExnO7Xw2DSy0DsB8k34XRzcLM5PqGqXql%2FYJsusIxLfV327KofjH59jeINSyH607RbEKnX27YGaSlBxl8WDvVwLG82mLWOkc7tiVsIBiLEg2RfJCZ%2BlJEaP3CeTyTxpFkf9k1XXuJBIkrRdD2ceD9FjPw66gI3p3Xug62exF05VswcH1ZXLOhajV0l56nXsHkiKQB1M9pPLFkPJ6ZJkdbRB1z4hzeDSNmDoSb8zULPwFZolWL7a7MPOLTq%2FrOMqXlAmuhUgfhsJvKHxFSgAPH6TAL9X8J8STHTHUIBw1MpfK%2FOWhDYTelC%2FddzUw%2Feg8mjjBqIZw%2FdngyE8UDgYywK%2Fgr3JYOy077hzX0yrJryKpd7TbKa2kPD8zmfNZUfkKqhnS6tYo%2FG1IOZjuUsGAg%2BSQnfnxMCzMsbxWSX3gDaO2KiQ366y67tXcj3xksG7AOqoun8wmvXpvAY6pgHFoDmHPpFeZc6PcWApBiMCNgwikXxlV%2Ff8a36lfF9Dgn1f%2F82pae9cggKeMHlMpqxKZtDakpz7bIMRrTcqyhiDHxiopb106tXy8uPABpViboz95BM3S3AGpMyfD7Ph4XUlCdNxZbzLpFDOowj2iiMb9QMl9Qe8Y5C5YC7YpUn1AVjUeaHOvh2aChlW5IaTLZwC37msrkbuKJ2y9ze%2FIr0e94gD8D8d&X-Amz-Signature=84d58da4e313488fb5eaf52b2fd7abc0de273d8e98e63eb6e01bd0eed485b3d8&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HKYQT3Y%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqpF%2Bs0YpX%2BLVU0RpEHnscELNCZOZKql%2FDjpKjgK729AiAJ%2B0aO0PCyZrbgr49rt9GaJ7pKC8E0yvfzwhvtknAyTSqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAZN3BOGmSIT23BGjKtwDi5OnmbDP1Wp20xap7kqPf%2FykL565AY3HkwkbHRZTjLDUqmQWMrg0Yx%2FdVeUaxQ7TIyRvOGtBm650LfbHVRxghuzYTnlOWJc%2FF5uQ6aKCDHO%2B1NJbJydd5S7aGhiKBWtHgq%2BDMJyvyFN57WtiHCMirc%2BEMMSVOTbj879AACoWe%2BA%2FB%2F4aIE%2FWxE4DinK%2FwD%2F408nD90uaDofdYbA%2BsLRQFfDRobB1wo%2B46XA8qkia4rkNwW3oF6VEP9YQNDwLRs2vfQUDlRAOUGjXpH3B71IMYrRhH1eK5YjItcUS%2FBWpzMcRIwl%2BXt2tn924FhzKeItU7izA2p7XMzTtTx92%2BxnYkBsSsqNYmlbme%2F5gLinDsrrU1ZVQja6ZwFg4IcpXHILLQ6%2Bgxi00gwDSX%2BNPBLkxkOea8O2aoxwIR58SvXZV5HtyhW1Oo6MXjS3niF%2B%2Bz6CmTb%2FWBGh6salldmIrxnNwwfcqw8aGdRnW8d4zw%2FbLFmFP4pm71JG67IffZuCuPkheclGOosyTcaQCFsxvsPcqBAXWsqeXHlj%2F9W6wEmUiHwj6MzDWWNVY3DOkhpa7PKxx1RFA6z0tDcBjYlKMkTIJH2lvQGEEGuBoBLu59Q2NMCbrSq%2BYdmzcjNe1pasw1%2FTpvAY6pgGr24M2ALSpNxv3bAvh1sSUxrd8XobSJVJ2ZmwWBwMge3qa1FLWzbVBSrBD1w7gOVORJ4XGpvktntFKNyCGRR0DpF82HDvcBi%2F7cHBK6u9D%2BERuJIl3JHdFB%2B%2FqNCCbTgHSBWrh8Nx%2Fii%2B7Li5gqCuFnlALZ0wlCAF6Em0pE5ZJi%2FlQdv1OxrVH0gLdCuKb6FKX2BKk5762Zgff9png%2FveHdgo%2FXF13&X-Amz-Signature=a918b6c1727c245b21e653a1ce8c2e2c3cb9355d2b38b68e549acb174438bd2c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HKYQT3Y%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqpF%2Bs0YpX%2BLVU0RpEHnscELNCZOZKql%2FDjpKjgK729AiAJ%2B0aO0PCyZrbgr49rt9GaJ7pKC8E0yvfzwhvtknAyTSqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAZN3BOGmSIT23BGjKtwDi5OnmbDP1Wp20xap7kqPf%2FykL565AY3HkwkbHRZTjLDUqmQWMrg0Yx%2FdVeUaxQ7TIyRvOGtBm650LfbHVRxghuzYTnlOWJc%2FF5uQ6aKCDHO%2B1NJbJydd5S7aGhiKBWtHgq%2BDMJyvyFN57WtiHCMirc%2BEMMSVOTbj879AACoWe%2BA%2FB%2F4aIE%2FWxE4DinK%2FwD%2F408nD90uaDofdYbA%2BsLRQFfDRobB1wo%2B46XA8qkia4rkNwW3oF6VEP9YQNDwLRs2vfQUDlRAOUGjXpH3B71IMYrRhH1eK5YjItcUS%2FBWpzMcRIwl%2BXt2tn924FhzKeItU7izA2p7XMzTtTx92%2BxnYkBsSsqNYmlbme%2F5gLinDsrrU1ZVQja6ZwFg4IcpXHILLQ6%2Bgxi00gwDSX%2BNPBLkxkOea8O2aoxwIR58SvXZV5HtyhW1Oo6MXjS3niF%2B%2Bz6CmTb%2FWBGh6salldmIrxnNwwfcqw8aGdRnW8d4zw%2FbLFmFP4pm71JG67IffZuCuPkheclGOosyTcaQCFsxvsPcqBAXWsqeXHlj%2F9W6wEmUiHwj6MzDWWNVY3DOkhpa7PKxx1RFA6z0tDcBjYlKMkTIJH2lvQGEEGuBoBLu59Q2NMCbrSq%2BYdmzcjNe1pasw1%2FTpvAY6pgGr24M2ALSpNxv3bAvh1sSUxrd8XobSJVJ2ZmwWBwMge3qa1FLWzbVBSrBD1w7gOVORJ4XGpvktntFKNyCGRR0DpF82HDvcBi%2F7cHBK6u9D%2BERuJIl3JHdFB%2B%2FqNCCbTgHSBWrh8Nx%2Fii%2B7Li5gqCuFnlALZ0wlCAF6Em0pE5ZJi%2FlQdv1OxrVH0gLdCuKb6FKX2BKk5762Zgff9png%2FveHdgo%2FXF13&X-Amz-Signature=53f5c12db8e10ac0af623a9afd0a818a08abd18c1ca8f3effdc1037d3d08534f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HKYQT3Y%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqpF%2Bs0YpX%2BLVU0RpEHnscELNCZOZKql%2FDjpKjgK729AiAJ%2B0aO0PCyZrbgr49rt9GaJ7pKC8E0yvfzwhvtknAyTSqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAZN3BOGmSIT23BGjKtwDi5OnmbDP1Wp20xap7kqPf%2FykL565AY3HkwkbHRZTjLDUqmQWMrg0Yx%2FdVeUaxQ7TIyRvOGtBm650LfbHVRxghuzYTnlOWJc%2FF5uQ6aKCDHO%2B1NJbJydd5S7aGhiKBWtHgq%2BDMJyvyFN57WtiHCMirc%2BEMMSVOTbj879AACoWe%2BA%2FB%2F4aIE%2FWxE4DinK%2FwD%2F408nD90uaDofdYbA%2BsLRQFfDRobB1wo%2B46XA8qkia4rkNwW3oF6VEP9YQNDwLRs2vfQUDlRAOUGjXpH3B71IMYrRhH1eK5YjItcUS%2FBWpzMcRIwl%2BXt2tn924FhzKeItU7izA2p7XMzTtTx92%2BxnYkBsSsqNYmlbme%2F5gLinDsrrU1ZVQja6ZwFg4IcpXHILLQ6%2Bgxi00gwDSX%2BNPBLkxkOea8O2aoxwIR58SvXZV5HtyhW1Oo6MXjS3niF%2B%2Bz6CmTb%2FWBGh6salldmIrxnNwwfcqw8aGdRnW8d4zw%2FbLFmFP4pm71JG67IffZuCuPkheclGOosyTcaQCFsxvsPcqBAXWsqeXHlj%2F9W6wEmUiHwj6MzDWWNVY3DOkhpa7PKxx1RFA6z0tDcBjYlKMkTIJH2lvQGEEGuBoBLu59Q2NMCbrSq%2BYdmzcjNe1pasw1%2FTpvAY6pgGr24M2ALSpNxv3bAvh1sSUxrd8XobSJVJ2ZmwWBwMge3qa1FLWzbVBSrBD1w7gOVORJ4XGpvktntFKNyCGRR0DpF82HDvcBi%2F7cHBK6u9D%2BERuJIl3JHdFB%2B%2FqNCCbTgHSBWrh8Nx%2Fii%2B7Li5gqCuFnlALZ0wlCAF6Em0pE5ZJi%2FlQdv1OxrVH0gLdCuKb6FKX2BKk5762Zgff9png%2FveHdgo%2FXF13&X-Amz-Signature=5c5d37593500e7c43bbb5ebd230e8ca7fa20b1edcb3dbc795d97e919e98525c1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HKYQT3Y%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqpF%2Bs0YpX%2BLVU0RpEHnscELNCZOZKql%2FDjpKjgK729AiAJ%2B0aO0PCyZrbgr49rt9GaJ7pKC8E0yvfzwhvtknAyTSqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAZN3BOGmSIT23BGjKtwDi5OnmbDP1Wp20xap7kqPf%2FykL565AY3HkwkbHRZTjLDUqmQWMrg0Yx%2FdVeUaxQ7TIyRvOGtBm650LfbHVRxghuzYTnlOWJc%2FF5uQ6aKCDHO%2B1NJbJydd5S7aGhiKBWtHgq%2BDMJyvyFN57WtiHCMirc%2BEMMSVOTbj879AACoWe%2BA%2FB%2F4aIE%2FWxE4DinK%2FwD%2F408nD90uaDofdYbA%2BsLRQFfDRobB1wo%2B46XA8qkia4rkNwW3oF6VEP9YQNDwLRs2vfQUDlRAOUGjXpH3B71IMYrRhH1eK5YjItcUS%2FBWpzMcRIwl%2BXt2tn924FhzKeItU7izA2p7XMzTtTx92%2BxnYkBsSsqNYmlbme%2F5gLinDsrrU1ZVQja6ZwFg4IcpXHILLQ6%2Bgxi00gwDSX%2BNPBLkxkOea8O2aoxwIR58SvXZV5HtyhW1Oo6MXjS3niF%2B%2Bz6CmTb%2FWBGh6salldmIrxnNwwfcqw8aGdRnW8d4zw%2FbLFmFP4pm71JG67IffZuCuPkheclGOosyTcaQCFsxvsPcqBAXWsqeXHlj%2F9W6wEmUiHwj6MzDWWNVY3DOkhpa7PKxx1RFA6z0tDcBjYlKMkTIJH2lvQGEEGuBoBLu59Q2NMCbrSq%2BYdmzcjNe1pasw1%2FTpvAY6pgGr24M2ALSpNxv3bAvh1sSUxrd8XobSJVJ2ZmwWBwMge3qa1FLWzbVBSrBD1w7gOVORJ4XGpvktntFKNyCGRR0DpF82HDvcBi%2F7cHBK6u9D%2BERuJIl3JHdFB%2B%2FqNCCbTgHSBWrh8Nx%2Fii%2B7Li5gqCuFnlALZ0wlCAF6Em0pE5ZJi%2FlQdv1OxrVH0gLdCuKb6FKX2BKk5762Zgff9png%2FveHdgo%2FXF13&X-Amz-Signature=41da8bbe875249fe0d34694131c6084de9b86751b21f2b9165fb4056da248d6b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HKYQT3Y%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqpF%2Bs0YpX%2BLVU0RpEHnscELNCZOZKql%2FDjpKjgK729AiAJ%2B0aO0PCyZrbgr49rt9GaJ7pKC8E0yvfzwhvtknAyTSqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAZN3BOGmSIT23BGjKtwDi5OnmbDP1Wp20xap7kqPf%2FykL565AY3HkwkbHRZTjLDUqmQWMrg0Yx%2FdVeUaxQ7TIyRvOGtBm650LfbHVRxghuzYTnlOWJc%2FF5uQ6aKCDHO%2B1NJbJydd5S7aGhiKBWtHgq%2BDMJyvyFN57WtiHCMirc%2BEMMSVOTbj879AACoWe%2BA%2FB%2F4aIE%2FWxE4DinK%2FwD%2F408nD90uaDofdYbA%2BsLRQFfDRobB1wo%2B46XA8qkia4rkNwW3oF6VEP9YQNDwLRs2vfQUDlRAOUGjXpH3B71IMYrRhH1eK5YjItcUS%2FBWpzMcRIwl%2BXt2tn924FhzKeItU7izA2p7XMzTtTx92%2BxnYkBsSsqNYmlbme%2F5gLinDsrrU1ZVQja6ZwFg4IcpXHILLQ6%2Bgxi00gwDSX%2BNPBLkxkOea8O2aoxwIR58SvXZV5HtyhW1Oo6MXjS3niF%2B%2Bz6CmTb%2FWBGh6salldmIrxnNwwfcqw8aGdRnW8d4zw%2FbLFmFP4pm71JG67IffZuCuPkheclGOosyTcaQCFsxvsPcqBAXWsqeXHlj%2F9W6wEmUiHwj6MzDWWNVY3DOkhpa7PKxx1RFA6z0tDcBjYlKMkTIJH2lvQGEEGuBoBLu59Q2NMCbrSq%2BYdmzcjNe1pasw1%2FTpvAY6pgGr24M2ALSpNxv3bAvh1sSUxrd8XobSJVJ2ZmwWBwMge3qa1FLWzbVBSrBD1w7gOVORJ4XGpvktntFKNyCGRR0DpF82HDvcBi%2F7cHBK6u9D%2BERuJIl3JHdFB%2B%2FqNCCbTgHSBWrh8Nx%2Fii%2B7Li5gqCuFnlALZ0wlCAF6Em0pE5ZJi%2FlQdv1OxrVH0gLdCuKb6FKX2BKk5762Zgff9png%2FveHdgo%2FXF13&X-Amz-Signature=4371f97fe76f6ef027ef287a03aed2e23b7249230563735bf101a80fe79f2008&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROXN5V7G%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEMzvDESaq9KuLZx7OgSRwQ8Au5lUEr61o1iZwDYSsKAiAUQkbO%2FU%2F%2BP%2B%2BoiPn3Rz8nZcqF5yup0O4ATKuPEY6uFiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFuYmUTekOrg15kGoKtwDuK%2FnBJKvsBkNOdZ0z99vW0DKFlJUpV%2FJvLYPYjrUpv7hCAi86gTnq%2FvqXUfMgjT22C02K8iTDfLIT9Vle0FBsFn8Y6DrLtlWpqwaD6eplVF9Ptc2Vnmje%2BI3VWKCHG5DfrkQ9BZ%2FKulShG%2FeEm9daDzcMnYIXZnh5QCKJp91ti8t8GfBEhJy4ExnO7Xw2DSy0DsB8k34XRzcLM5PqGqXql%2FYJsusIxLfV327KofjH59jeINSyH607RbEKnX27YGaSlBxl8WDvVwLG82mLWOkc7tiVsIBiLEg2RfJCZ%2BlJEaP3CeTyTxpFkf9k1XXuJBIkrRdD2ceD9FjPw66gI3p3Xug62exF05VswcH1ZXLOhajV0l56nXsHkiKQB1M9pPLFkPJ6ZJkdbRB1z4hzeDSNmDoSb8zULPwFZolWL7a7MPOLTq%2FrOMqXlAmuhUgfhsJvKHxFSgAPH6TAL9X8J8STHTHUIBw1MpfK%2FOWhDYTelC%2FddzUw%2Feg8mjjBqIZw%2FdngyE8UDgYywK%2Fgr3JYOy077hzX0yrJryKpd7TbKa2kPD8zmfNZUfkKqhnS6tYo%2FG1IOZjuUsGAg%2BSQnfnxMCzMsbxWSX3gDaO2KiQ366y67tXcj3xksG7AOqoun8wmvXpvAY6pgHFoDmHPpFeZc6PcWApBiMCNgwikXxlV%2Ff8a36lfF9Dgn1f%2F82pae9cggKeMHlMpqxKZtDakpz7bIMRrTcqyhiDHxiopb106tXy8uPABpViboz95BM3S3AGpMyfD7Ph4XUlCdNxZbzLpFDOowj2iiMb9QMl9Qe8Y5C5YC7YpUn1AVjUeaHOvh2aChlW5IaTLZwC37msrkbuKJ2y9ze%2FIr0e94gD8D8d&X-Amz-Signature=776f8599b854df4dbead90b16725361e12083c111c9d556ebd3ac57f5d893b01&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROXN5V7G%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEMzvDESaq9KuLZx7OgSRwQ8Au5lUEr61o1iZwDYSsKAiAUQkbO%2FU%2F%2BP%2B%2BoiPn3Rz8nZcqF5yup0O4ATKuPEY6uFiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFuYmUTekOrg15kGoKtwDuK%2FnBJKvsBkNOdZ0z99vW0DKFlJUpV%2FJvLYPYjrUpv7hCAi86gTnq%2FvqXUfMgjT22C02K8iTDfLIT9Vle0FBsFn8Y6DrLtlWpqwaD6eplVF9Ptc2Vnmje%2BI3VWKCHG5DfrkQ9BZ%2FKulShG%2FeEm9daDzcMnYIXZnh5QCKJp91ti8t8GfBEhJy4ExnO7Xw2DSy0DsB8k34XRzcLM5PqGqXql%2FYJsusIxLfV327KofjH59jeINSyH607RbEKnX27YGaSlBxl8WDvVwLG82mLWOkc7tiVsIBiLEg2RfJCZ%2BlJEaP3CeTyTxpFkf9k1XXuJBIkrRdD2ceD9FjPw66gI3p3Xug62exF05VswcH1ZXLOhajV0l56nXsHkiKQB1M9pPLFkPJ6ZJkdbRB1z4hzeDSNmDoSb8zULPwFZolWL7a7MPOLTq%2FrOMqXlAmuhUgfhsJvKHxFSgAPH6TAL9X8J8STHTHUIBw1MpfK%2FOWhDYTelC%2FddzUw%2Feg8mjjBqIZw%2FdngyE8UDgYywK%2Fgr3JYOy077hzX0yrJryKpd7TbKa2kPD8zmfNZUfkKqhnS6tYo%2FG1IOZjuUsGAg%2BSQnfnxMCzMsbxWSX3gDaO2KiQ366y67tXcj3xksG7AOqoun8wmvXpvAY6pgHFoDmHPpFeZc6PcWApBiMCNgwikXxlV%2Ff8a36lfF9Dgn1f%2F82pae9cggKeMHlMpqxKZtDakpz7bIMRrTcqyhiDHxiopb106tXy8uPABpViboz95BM3S3AGpMyfD7Ph4XUlCdNxZbzLpFDOowj2iiMb9QMl9Qe8Y5C5YC7YpUn1AVjUeaHOvh2aChlW5IaTLZwC37msrkbuKJ2y9ze%2FIr0e94gD8D8d&X-Amz-Signature=95822f8b67501c10b3fe1bf8f8f207ffe2392d09e8e9e8ce85b57dfbfd54d895&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROXN5V7G%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEMzvDESaq9KuLZx7OgSRwQ8Au5lUEr61o1iZwDYSsKAiAUQkbO%2FU%2F%2BP%2B%2BoiPn3Rz8nZcqF5yup0O4ATKuPEY6uFiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFuYmUTekOrg15kGoKtwDuK%2FnBJKvsBkNOdZ0z99vW0DKFlJUpV%2FJvLYPYjrUpv7hCAi86gTnq%2FvqXUfMgjT22C02K8iTDfLIT9Vle0FBsFn8Y6DrLtlWpqwaD6eplVF9Ptc2Vnmje%2BI3VWKCHG5DfrkQ9BZ%2FKulShG%2FeEm9daDzcMnYIXZnh5QCKJp91ti8t8GfBEhJy4ExnO7Xw2DSy0DsB8k34XRzcLM5PqGqXql%2FYJsusIxLfV327KofjH59jeINSyH607RbEKnX27YGaSlBxl8WDvVwLG82mLWOkc7tiVsIBiLEg2RfJCZ%2BlJEaP3CeTyTxpFkf9k1XXuJBIkrRdD2ceD9FjPw66gI3p3Xug62exF05VswcH1ZXLOhajV0l56nXsHkiKQB1M9pPLFkPJ6ZJkdbRB1z4hzeDSNmDoSb8zULPwFZolWL7a7MPOLTq%2FrOMqXlAmuhUgfhsJvKHxFSgAPH6TAL9X8J8STHTHUIBw1MpfK%2FOWhDYTelC%2FddzUw%2Feg8mjjBqIZw%2FdngyE8UDgYywK%2Fgr3JYOy077hzX0yrJryKpd7TbKa2kPD8zmfNZUfkKqhnS6tYo%2FG1IOZjuUsGAg%2BSQnfnxMCzMsbxWSX3gDaO2KiQ366y67tXcj3xksG7AOqoun8wmvXpvAY6pgHFoDmHPpFeZc6PcWApBiMCNgwikXxlV%2Ff8a36lfF9Dgn1f%2F82pae9cggKeMHlMpqxKZtDakpz7bIMRrTcqyhiDHxiopb106tXy8uPABpViboz95BM3S3AGpMyfD7Ph4XUlCdNxZbzLpFDOowj2iiMb9QMl9Qe8Y5C5YC7YpUn1AVjUeaHOvh2aChlW5IaTLZwC37msrkbuKJ2y9ze%2FIr0e94gD8D8d&X-Amz-Signature=33cecf208f69ef83870132d420308449a5608f5952b0b078236ee5332f0c386b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROXN5V7G%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEMzvDESaq9KuLZx7OgSRwQ8Au5lUEr61o1iZwDYSsKAiAUQkbO%2FU%2F%2BP%2B%2BoiPn3Rz8nZcqF5yup0O4ATKuPEY6uFiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFuYmUTekOrg15kGoKtwDuK%2FnBJKvsBkNOdZ0z99vW0DKFlJUpV%2FJvLYPYjrUpv7hCAi86gTnq%2FvqXUfMgjT22C02K8iTDfLIT9Vle0FBsFn8Y6DrLtlWpqwaD6eplVF9Ptc2Vnmje%2BI3VWKCHG5DfrkQ9BZ%2FKulShG%2FeEm9daDzcMnYIXZnh5QCKJp91ti8t8GfBEhJy4ExnO7Xw2DSy0DsB8k34XRzcLM5PqGqXql%2FYJsusIxLfV327KofjH59jeINSyH607RbEKnX27YGaSlBxl8WDvVwLG82mLWOkc7tiVsIBiLEg2RfJCZ%2BlJEaP3CeTyTxpFkf9k1XXuJBIkrRdD2ceD9FjPw66gI3p3Xug62exF05VswcH1ZXLOhajV0l56nXsHkiKQB1M9pPLFkPJ6ZJkdbRB1z4hzeDSNmDoSb8zULPwFZolWL7a7MPOLTq%2FrOMqXlAmuhUgfhsJvKHxFSgAPH6TAL9X8J8STHTHUIBw1MpfK%2FOWhDYTelC%2FddzUw%2Feg8mjjBqIZw%2FdngyE8UDgYywK%2Fgr3JYOy077hzX0yrJryKpd7TbKa2kPD8zmfNZUfkKqhnS6tYo%2FG1IOZjuUsGAg%2BSQnfnxMCzMsbxWSX3gDaO2KiQ366y67tXcj3xksG7AOqoun8wmvXpvAY6pgHFoDmHPpFeZc6PcWApBiMCNgwikXxlV%2Ff8a36lfF9Dgn1f%2F82pae9cggKeMHlMpqxKZtDakpz7bIMRrTcqyhiDHxiopb106tXy8uPABpViboz95BM3S3AGpMyfD7Ph4XUlCdNxZbzLpFDOowj2iiMb9QMl9Qe8Y5C5YC7YpUn1AVjUeaHOvh2aChlW5IaTLZwC37msrkbuKJ2y9ze%2FIr0e94gD8D8d&X-Amz-Signature=dbf0ad80135cdccf3a3a08f3b99e533190ad40569865e65b847b3198dc8baebb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROXN5V7G%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEMzvDESaq9KuLZx7OgSRwQ8Au5lUEr61o1iZwDYSsKAiAUQkbO%2FU%2F%2BP%2B%2BoiPn3Rz8nZcqF5yup0O4ATKuPEY6uFiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFuYmUTekOrg15kGoKtwDuK%2FnBJKvsBkNOdZ0z99vW0DKFlJUpV%2FJvLYPYjrUpv7hCAi86gTnq%2FvqXUfMgjT22C02K8iTDfLIT9Vle0FBsFn8Y6DrLtlWpqwaD6eplVF9Ptc2Vnmje%2BI3VWKCHG5DfrkQ9BZ%2FKulShG%2FeEm9daDzcMnYIXZnh5QCKJp91ti8t8GfBEhJy4ExnO7Xw2DSy0DsB8k34XRzcLM5PqGqXql%2FYJsusIxLfV327KofjH59jeINSyH607RbEKnX27YGaSlBxl8WDvVwLG82mLWOkc7tiVsIBiLEg2RfJCZ%2BlJEaP3CeTyTxpFkf9k1XXuJBIkrRdD2ceD9FjPw66gI3p3Xug62exF05VswcH1ZXLOhajV0l56nXsHkiKQB1M9pPLFkPJ6ZJkdbRB1z4hzeDSNmDoSb8zULPwFZolWL7a7MPOLTq%2FrOMqXlAmuhUgfhsJvKHxFSgAPH6TAL9X8J8STHTHUIBw1MpfK%2FOWhDYTelC%2FddzUw%2Feg8mjjBqIZw%2FdngyE8UDgYywK%2Fgr3JYOy077hzX0yrJryKpd7TbKa2kPD8zmfNZUfkKqhnS6tYo%2FG1IOZjuUsGAg%2BSQnfnxMCzMsbxWSX3gDaO2KiQ366y67tXcj3xksG7AOqoun8wmvXpvAY6pgHFoDmHPpFeZc6PcWApBiMCNgwikXxlV%2Ff8a36lfF9Dgn1f%2F82pae9cggKeMHlMpqxKZtDakpz7bIMRrTcqyhiDHxiopb106tXy8uPABpViboz95BM3S3AGpMyfD7Ph4XUlCdNxZbzLpFDOowj2iiMb9QMl9Qe8Y5C5YC7YpUn1AVjUeaHOvh2aChlW5IaTLZwC37msrkbuKJ2y9ze%2FIr0e94gD8D8d&X-Amz-Signature=8f198077e188662ed610c3e01664a64c91e915fcce31f067aab2ca6cb6026d14&X-Amz-SignedHeaders=host&x-id=GetObject)
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


