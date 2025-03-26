from .html_collector import HtmlCollector
from .mocks.http_requester_mock import mock_request_from_page


def test_collect_essentials():
    http_request_response = mock_request_from_page()

    html_collector = HtmlCollector()
    essentials_information = html_collector.collect_essentials(
        http_request_response["html"]
    )
    print()
    print(essentials_information)
