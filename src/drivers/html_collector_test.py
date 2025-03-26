from .html_collector import HtmlCollector
from .mocks.http_requester_mock import mock_request_from_page


def test_collect_essentials():
    http_request_response = mock_request_from_page()

    html_collector = HtmlCollector()
    essentials_information = html_collector.collect_essentials(
        http_request_response["html"]
    )

    assert isinstance(essentials_information, list)
    assert isinstance(essentials_information[0], dict)
    assert "name" in essentials_information[0]
    assert "link" in essentials_information[0]
