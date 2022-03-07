import asyncclick as aclick
from flow.report import ReportFlow
from flow.reports import ReportsFlow

@aclick.group(name='report')
def report():
    pass


@report.command('report', short_help='Get reports or report related to scan or id')
@aclick.option('--flow', type=str, is_flag=False, default='', help='Flow id')
@aclick.option('--id', type=str, is_flag=False, default='', help='''
Report id: Must be given when flow option is absent, or will be ignored
''')
@aclick.option('--hash', type=str, is_flag=False, default='', help='''
File hash the report contains. Must be given when id is specified
''')
@aclick.option('-f', '--filters', type=str, is_flag=False, multiple=True, default=[], help='Filters that apply to the report')
@aclick.option('-s', '--sorts', type=str, is_flag=False, multiple=True, default=[], help='Sorting that apply to the report')
@aclick.option('-g', '--graph', type=bool, is_flag=True, default=False, help='Whether get emulation graph or not')
async def get_report(
    flow: str,
    id: str,
    hash: str,
    filters: list[str],
    sorts: list[str],
    graph: bool
):
    if flow:
        reports_flow = ReportsFlow()
        await reports_flow.get_scan_reports(flow, filters, sorts, graph)
    elif id and hash:
        report_flow = ReportFlow()
        await report_flow.get_report(id, hash, filters, sorts, graph)


@report.command('export', short_help='Export report in the given format')
@aclick.option('--id', type=str, required=True, help='Report id to be exported')
@aclick.option('--format', required=True, type=aclick.Choice(['misp', 'stix', 'html', 'pdf'], case_sensitive=True), default='misp', help='Export format')
@aclick.option('--output', '-o', type=str, is_flag=False, default='report.out', help='Output path where report is saved')
async def export_report(id: str, format: str, output: str):
    
    report_flow = ReportFlow()
    await report_flow.get_formatted_report(id, format, output)
