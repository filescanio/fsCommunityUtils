from common.config import SERVICE_BASE_URL

FILE_SCAN = '/api/scan/file'

GET_SCAN_REPORTS = '/api/scan/{scan_id}/report'
GET_FORMATTED_REPORT = '/api/reports/{report_id}/download'
GET_SPECIFIC_REPORT = '/api/reports/{report_id}/{file_hash}'
GET_REPORTS = '/api/users/uploads'

GET_ALL_FILES = '/api/reports/{report_id}/files'
DOWNLOAD_FILE = '/api/files/{file_hash}'

SEARCH_REPORT = '/api/reports/search'

SYSTEM_INFO = '/api/system/info'
SYSTEM_CONFIG = '/api/system/config'


def get_endpoint(ep: str, **kwargs) -> str:

    result = ep
    for key in kwargs:
        result = result.replace(f'{{{key}}}', kwargs[key])

    return f'{SERVICE_BASE_URL}{result}'
