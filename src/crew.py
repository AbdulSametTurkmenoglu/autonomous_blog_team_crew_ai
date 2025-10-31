from crewai import Crew, Process
from .agents import researcher, writer
from .tasks import research_task, writing_task

blog_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    verbose=True
)


def create_blog_post(topic: str) -> str:
    """
    Verilen konu hakkında otonom olarak blog yazısı oluşturur.
    """
    print(f"\n{'=' * 60}")
    print(f" Blog Yazma Ekibi Başlatılıyor...")
    print(f" Konu: {topic}")
    print(f"{'=' * 60}\n")

    result = blog_crew.kickoff(inputs={"topic": topic})

    print(f"\n{'=' * 60}")
    print(f" Blog Yazısı Tamamlandı!")
    print(f"{'=' * 60}\n")

    return str(result)