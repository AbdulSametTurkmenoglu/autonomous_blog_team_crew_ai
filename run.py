import src.config
from src.crew import create_blog_post
import sys


def main():
    """
    Ana çalıştırma fonksiyonu.
    Komut satırından bir konu alabilir veya varsayılan bir konuyu kullanır.
    """

    default_topics = [
        "Direct Preference Optimization (DPO) ile LLM Fine-Tuning",
        "Mixture of Experts (MoE) Mimarisi ve LLM'lerdeki Yeri",
        "RAG (Retrieval-Augmented Generation) Sistemlerinde İleri Seviye Teknikler"
    ]

    selected_topic = default_topics[0]


    if len(sys.argv) > 1:
        selected_topic = " ".join(sys.argv[1:])

    print(f"Seçilen Konu: {selected_topic}")

    try:
        blog_post = create_blog_post(selected_topic)
    except Exception as e:
        print(f"Hata: Blog oluşturma sürecinde bir sorun oluştu: {e}")
        return

    safe_filename = selected_topic.replace(' ', '_').replace('/', '_').lower()
    safe_filename = "".join(c for c in safe_filename if c.isalnum() or c == '_')[:50]
    output_file = f"blog_ciktisi_{safe_filename}.md"

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(blog_post)
        print(f"\n Blog yazısı '{output_file}' dosyasına başarıyla kaydedildi.")
    except IOError as e:
        print(f"Hata: Dosyaya yazılırken bir sorun oluştu: {e}")

    print("\n" + "=" * 60)
    print("BLOG YAZISI ÖNİZLEMESİ (İlk 500 karakter):")
    print("=" * 60)
    print(blog_post[:500] + "...")


if __name__ == "__main__":
    main()