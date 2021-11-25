# -*- coding: utf-8 -*-

"""
pytest module to report stats as a QR code
"""

import io

import pytest
import qrcode


def pytest_addoption(parser):
    """
    add option to pytest to enable QR code output
    """
    group = parser.getgroup('qr')
    group.addoption(
        '--qr',
        action='store_true',
        dest='qr',
        help='generate QR code with results'
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary(terminalreporter, exitstatus, config):  # pylint:disable=unused-argument
    """
    hook into terminal summary to produce output
    """
    yield
    # special check for pytest-xdist plugin, cause we do not want to send report for each worker.
    if hasattr(terminalreporter.config, 'workerinput'):
        return

    if not config.getoption('qr'):
        return

    failed = len(terminalreporter.stats.get('failed', []))
    passed = len(terminalreporter.stats.get('passed', []))
    skipped = len(terminalreporter.stats.get('skipped', []))
    error = len(terminalreporter.stats.get('error', []))

    results = f'Passed={passed} Failed={failed} Skipped={skipped} Error={error}'
    if failed or error:
        status = 'BAD'
    else:
        status = 'GOOD'

    qr_result = qrcode.QRCode()
    qr_result.add_data(f'{status} - {results}')
    file_result = io.StringIO()
    qr_result.print_ascii(out=file_result)
    file_result.seek(0)
    print(file_result.read())
