from crewai import Task
from .agents import researcher, writer

research_task = Task(
    description="""Konu: {topic}

    Görevin:
    1. Bu konu hakkında en güncel bilgileri web'de ara ('search_tool' kullan).
    2. En az 3-5 güvenilir kaynak bul.
    3. Bulduğun her kaynağın URL'sini 'verify_source' aracıyla kontrol et.
    4. Sadece 'Güvenilir' olarak işaretlenen kaynakların içeriğini 'scrape_tool' ile tara.
    5. Şu başlıklar altında bulgularını özetle:
       - Teknolojinin tanımı ve temel özellikleri
       - Kullanım alanları ve avantajları
       - Teknik detaylar ve nasıl çalıştığı
       - Güncel trendler ve gelecek öngörüleri
    6. Tüm (güvenilir) kaynaklarının URL'lerini raporuna ekle.

    Çıktı formatı: Detaylı araştırma raporu (markdown formatında)
    """,
    agent=researcher,
    expected_output="Markdown formatında detaylı araştırma raporu, güvenilir kaynak linkleri ile birlikte"
)

writing_task = Task(
    description="""Araştırma raporunu kullanarak profesyonel bir blog yazısı yaz.

    Gereksinimleri:
    1. 800-1000 kelimelik, akıcı bir blog yazısı
    2. Yapı:
       - Dikkat çekici bir başlık
       - Giriş paragrafı (konunun önemi)
       - 3-4 ana bölüm (alt başlıklarla)
       - Pratik örnekler veya kullanım senaryoları
       - Sonuç ve gelecek öngörüsü
    3. Teknik terimleri açıkla
    4. SEO dostu olsun (anahtar kelimeleri doğal şekilde kullan)
    5. Türkçe dilbilgisi kurallarına uy
    6. Markdown formatında yaz

    Dikkat: Araştırma raporundaki bilgileri kullan ama birebir kopyalama.
    Kendi cümlelerini kur ve akıcı bir anlatım oluştur.
    """,
    agent=writer,
    expected_output="800-1000 kelimelik, profesyonel markdown blog yazısı",
    context=[research_task]
)