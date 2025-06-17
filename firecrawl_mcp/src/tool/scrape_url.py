from src.infrastructure.firecrawl_client import FireCrawlClient
from src.infrastructure.mcp_instance import mcp
from src.type.url_param import UrlParam
from src.type.web_page_scraping_result import WebPageScrapingResult


@mcp.tool()
def scrape_url(url_param: UrlParam) -> WebPageScrapingResult:
    url = str(url_param.url)
    try:
        result = FireCrawlClient.get_client().scrape_url(url, formats=['markdown'])

        if result.success:
            return WebPageScrapingResult(
                markdown=result.markdown,
                url=url,
            )
        else:
            return WebPageScrapingResult(
                url=url,
                error=result.error,
                success=False
            )
    except Exception as e:
        return WebPageScrapingResult(
            url=url,
            error=str(e),
            success=False
        )