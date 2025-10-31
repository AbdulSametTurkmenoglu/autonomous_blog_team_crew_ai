# Otonom Blog Ekibi (CrewAI Projesi)

Bu proje, `crewai` kütüphanesini kullanarak otonom bir ajan ekibi oluşturur. Ekibin amacı, verilen herhangi bir teknik konu hakkında web'de araştırma yapmak ve bu araştırmaya dayanarak profesyonel bir blog yazısı oluşturmaktır.

##  Ekip ve Süreç

Proje, sıralı (`Process.sequential`) bir süreçte çalışan iki ajandan oluşur:

1.  **Teknik Araştırma Uzmanı (Researcher):**
    * **Araçlar:** `SerperDevTool` (Web Arama), `ScrapeWebsiteTool` (Web Sitesi Okuma), `verify_source` (Özel Kaynak Doğrulayıcı).
    * **Görevi:** Konuyla ilgili 3-5 güvenilir kaynak bulur, bu kaynakları doğrular, içeriklerini okur ve teknik bir araştırma raporu hazırlar.

2.  **Teknik İçerik Yazarı (Writer):**
    * **Görevi:** Araştırmacının hazırladığı raporu (`context` olarak alır) ve bu bilgileri kullanarak 800-1000 kelimelik, SEO dostu, akıcı bir blog yazısına dönüştürür.



##  Kurulum

1.  **Depoyu Klonlama:**
    ```bash
    git clone [https://github.com/AbdulSametTurkmenoglu/otonom_blog_ekibi.git](https://github.com/AbdulSametTurkmenoglu/otonom_blog_ekibi.git)
    cd otonom_blog_ekibi
    ```

2.  **Sanal Ortam (Önerilir):**
    ```bash
    python -m venv .venv
    # Windows: .\.venv\Scripts\activate
    # macOS/Linux: source .venv/bin/activate
    ```

3.  **Gerekli Kütüphaneleri Yükleme:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **.env Dosyasını Oluşturma:**
    `.env.example` dosyasını kopyalayıp `.env` olarak adlandırın ve içini kendi API anahtarlarınızla doldurun:
    ```bash
    # Windows
    copy .env.example .env
    
    # macOS / Linux
    cp .env.example .env
    ```
    `.env` dosyasının içeriği:
    ```
    OPENAI_API_KEY="sk-..."
    SERPER_API_KEY="..." 
    ```
    *Not: `SERPER_API_KEY`, web araması için `serper.dev` sitesinden alınmalıdır.*

##  Kullanım

Proje, `run.py` script'i üzerinden çalıştırılır.

**1. Varsayılan Konu ile Çalıştırma:**
Script, varsayılan olarak `Direct Preference Optimization (DPO)` konusunu işleyecektir.

```bash
python run.py
```

**2. Özel Konu ile Çalıştırma:**
Konunuzu komut satırından argüman olarak girebilirsiniz:

```bash
python run.py "LangGraph nedir ve nasıl çalışır?"
```

Ekip çalışmaya başladığında terminalde detaylı logları (`verbose=True` sayesinde) göreceksiniz. Süreç tamamlandığında, `blog_ciktisi_...md` adında bir markdown dosyası oluşturulacaktır.