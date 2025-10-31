from crewai import Agent
from .config import llm
from .tools import search_tool, scrape_tool, verify_source

researcher = Agent(
    role="Teknik Araştırma Uzmanı",
    goal="Verilen konu hakkında güncel, doğru ve kapsamlı bilgi toplamak",
    backstory="""Sen deneyimli bir AI ve makine öğrenmesi araştırmacısısın.
    Akademik makaleler, teknik bloglar ve güncel gelişmeleri takip ederek
    en güvenilir kaynaklardan bilgi toplarsın. Bilimsel doğruluğa önem verirsin
    ve bulduğun her kaynağı 'verify_source' aracıyla kontrol edersin.""",
    tools=[search_tool, scrape_tool, verify_source], # Özel doğrulama aracını ekledik
    llm=llm,
    verbose=True,
    allow_delegation=False
)

writer = Agent(
    role="Teknik İçerik Yazarı",
    goal="Araştırma bulgularını anlaşılır ve ilgi çekici blog yazısına dönüştürmek",
    backstory="""Sen yetenekli bir teknik yazarsın. Karmaşık AI konularını
    hem teknik hem de geniş kitle için anlaşılır şekilde anlatabilirsin.
    SEO'ya uygun, akıcı ve bilgilendirici içerikler üretirsin.
    Başlıklar, alt başlıklar ve örneklerle zengin yazılar yazarsın.""",
    llm=llm,
    verbose=True,
    allow_delegation=False
)