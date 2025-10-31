# Autonomous Blog Team (CrewAI Project)

An autonomous agent team built with the `crewai` library that researches any given technical topic on the web and creates a professional blog post based on that research.

##  Team & Process

The project uses two agents working in a sequential process (`Process.sequential`):

1. **Technical Research Specialist (Researcher)**
   - **Tools**: `SerperDevTool` (Web Search), `ScrapeWebsiteTool` (Website Scraper), `verify_source` (Custom Source Validator)
   - **Task**: Finds 3-5 reliable sources, validates them, reads their content, and prepares a technical research report

2. **Technical Content Writer (Writer)**
   - **Task**: Takes the researcher's report as `context` and transforms it into an 800-1000 word, SEO-friendly, fluent blog post

##  Prerequisites

- Python 3.8+
- OpenAI API Key
- Serper API Key (for web search via serper.dev)

##  Installation
```bash
# Clone the repository
git clone https://github.com/AbdulSametTurkmenoglu/autonomous_blog_team_crew_ai.git
cd autonomous_blog_team_crew_ai


# Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env  # Windows: copy .env.example .env
# Edit .env and add your API keys
```

**.env file contents:**
```
OPENAI_API_KEY="sk-..."
SERPER_API_KEY="..."
```

*Note: Get your `SERPER_API_KEY` from serper.dev*

##  Usage

The project runs via the `run.py` script.

**Run with default topic:**
```bash
python run.py
```
The script will process the default topic: `Direct Preference Optimization (DPO)`

**Run with custom topic:**
```bash
python run.py "What is LangGraph and how does it work?"
```

When the team starts working, you'll see detailed logs in the terminal (enabled by `verbose=True`). Once completed, a markdown file named `blog_ciktisi_...md` will be created.


##  How It Works

1. **Research Phase**: 
   - Researcher agent searches the web for relevant sources
   - Validates source credibility
   - Scrapes and analyzes content
   - Compiles a comprehensive research report

2. **Writing Phase**:
   - Writer agent receives the research report
   - Transforms technical information into engaging content
   - Ensures SEO optimization
   - Produces a polished 800-1000 word blog post

##  Features

- **Autonomous Research**: Agents independently find and verify sources
- **Source Validation**: Custom tool ensures information credibility
- **SEO Optimization**: Generated content is search-engine friendly
- **Sequential Process**: Clear workflow from research to final output
- **Detailed Logging**: Verbose mode shows the entire decision-making process
- **Markdown Output**: Ready-to-publish blog posts in markdown format

