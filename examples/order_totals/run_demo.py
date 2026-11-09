"""Run identical tests against the faulty fixture and the corrected example."""
import io
import json
import unittest
from unittest.mock import patch

import app
import before
import test_totals


def run(implementation):
    output = io.StringIO()
    with patch.object(test_totals, 'quote', implementation):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_totals.QuoteTests)
        result = unittest.TextTestRunner(stream=output, verbosity=2).run(suite)
    return result, output.getvalue()


def main():
    red, red_log = run(before.quote)
    green, green_log = run(app.quote)
    print('BEFORE: deliberate shipping-discount bug\n' + red_log)
    print('AFTER: merchandise-only discount\n' + green_log)
    expected_failures = {
        'test_totals.QuoteTests.test_discount_excludes_shipping',
        'test_totals.QuoteTests.test_full_discount_keeps_shipping',
    }
    verified = (
        red.testsRun == green.testsRun == 8
        and {case.id() for case, _ in red.failures} == expected_failures
        and not red.errors and not red.skipped
        and green.wasSuccessful() and not green.skipped
    )
    print(json.dumps({
        'synthetic_data_only': True,
        'model_invoked': False,
        'before': {'tests': red.testsRun, 'failures': len(red.failures)},
        'after': {'tests': green.testsRun, 'failures': len(green.failures)},
        'demonstration_verified': verified,
    }, indent=2))
    return 0 if verified else 1


if __name__ == '__main__':
    raise SystemExit(main())
