# Demo: catch a discount applied to shipping

A small public example of the **test → fix → independent review** workflow. No customer code, names, accounts, credentials or services are used. Python 3.11+; standard library only. No network, model, plugin or account is needed to run the demonstration.

## Run it

From the repository root:

```sh
python3 examples/order_totals/run_demo.py
```

Expected result: the intentionally faulty implementation fails **2 of 8 tests**; the corrected implementation passes **8 of 8**. Exit code 0 means those exact before/after outcomes were verified, not that the faulty version passed.

For two items costing 10.00 each, shipping 5.00 and a 10% discount:

| Implementation | Total | Why |
| --- | --- | --- |
| Faulty fixture | 22.50 | Discounts both merchandise and shipping |
| Corrected example | 23.00 | Discounts merchandise only |

All arithmetic uses integer cents. The business rule is explicit: round the discounted merchandise total half-up to a cent, then add shipping. This is not a tax engine or production commerce library.

## What the files do

- `app.py`: corrected implementation and input validation.
- `before.py`: intentionally faulty calculation; it shares validation with `app.py` so the example isolates one defect.
- `test_totals.py`: eight synthetic acceptance tests, including full discount, rounding, free shipping and invalid inputs.
- `run_demo.py`: runs the same acceptance tests against both implementations and verifies the expected outcomes. It does **not** run agents or call an AI model.

Run only the corrected implementation's tests:

```sh
python3 -m unittest discover -s examples/order_totals -p 'test_*.py' -v
```

## Try the workflow with Codex agents

Install the plugin and project roles as described in the [main README](../../README.md). In a Codex session for this repository, ask:

> Use Codex Engineering Kit on examples/order_totals. Delegate to a test analyst and an independent code reviewer using the installed cek roles. Explain the failure in before.py, verify app.py against the acceptance tests, and report any untested assumptions. Use only synthetic local data. Do not publish, contact external services or modify the bundled skill catalog.

The host must support delegated agents, load the project role configuration and permit delegation. If it does not, Codex can perform a sequential review, but must report that no independent agent ran.

This is an inspectable teaching example with the answer included, **not** a blind model benchmark. The command's output proves the behavior of this example; it does not certify all catalog skills or demonstrate superiority over another model. See the [evaluation protocol](../../docs/EVALUATION.md) for a fair comparison.
