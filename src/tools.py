from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from crewai.tools import tool

# 1. Hazır Araçlar
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()


@tool("Kaynak Doğrulayıcı")
def verify_source(url: str) -> str:
    """Verilen URL'in güvenilir bir kaynak (akademik, resmi) olup olmadığını kontrol eder."""
    print(f"  [Tool] Kaynak doğrulanıyor: {url}")

    trusted_domains = [
        'arxiv.org',
        'openai.com',
        'huggingface.co',
        'github.com',
        'wikipedia.org',
        'google.com',
        'microsoft.com'
    ]

    try:
        domain = url.split('/')[2].replace('www.', '')

        if any(trusted in domain for trusted in trusted_domains):
            return f"✓ Güvenilir kaynak: {domain}"

        return f" Dikkat: {domain} güvenilir kaynaklar listesinde değil. Kullanmadan önce dikkatli ol."

    except (IndexError, AttributeError):
        return "Geçersiz URL, doğrulanamadı."