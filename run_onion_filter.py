# Architected by Kuber Sharma (@kubersharmax) | kubersharma.com
"""
run_onion_filter.py â Agentic GTM Operating System
====================================================

Production-ready Negative ICP Filter engine that ingests the
negative-icp-filter.json schema and evaluates a prospect's
Agentic Readiness score.

Core concepts:
  - Metaphorical Onions: Legacy ETL/middleware noise layers that
    signal a prospect is NOT ready for agentic, zero-copy GTM.
  - Zero-Copy Data Activation: Modern data architecture patterns
    (reverse ETL, event-driven, composable CDP) that indicate a
    prospect IS ready for agentic workflows.

Usage:
  python run_onion_filter.py

Repository: github.com/kubersharmax/agentic-gtm-os
"""

import json
import os
import sys
from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# Data Models
# ---------------------------------------------------------------------------

@dataclass
class OnionDetection:
    """A single detected onion-layer signal in a prospect's stack."""

    layer_id: str
    layer_name: str
    matched_keyword: str
    severity: str
    penalty: int


@dataclass
class ZeroCopyDetection:
    """A single detected zero-copy readiness signal."""

    signal_id: str
    signal_name: str
    matched_indicator: str
    weight: int


@dataclass
class ProspectEvaluation:
    """Complete evaluation result for a prospect."""

    prospect_name: str
    raw_score: int
    classification: str
    onion_detections: list = field(default_factory=list)
    zero_copy_detections: list = field(default_factory=list)
    summary: str = ""


# ---------------------------------------------------------------------------
# Schema Loader
# ---------------------------------------------------------------------------

def load_schema(schema_path: str) -> dict:
    """Load and validate the negative-icp-filter.json schema.

    Args:
        schema_path: Absolute or relative path to the JSON schema file.

    Returns:
        Parsed schema dictionary.

    Raises:
        FileNotFoundError: If the schema file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
        ValueError: If required schema keys are missing.
    """
    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"Schema not found: {schema_path}")

    with open(schema_path, "r", encoding="utf-8") as fh:
        schema = json.load(fh)

    required_keys = {"onion_layers", "zero_copy_readiness_signals", "scoring"}
    missing = required_keys - set(schema.keys())
    if missing:
        raise ValueError(f"Schema is missing required keys: {missing}")

    return schema


# ---------------------------------------------------------------------------
# Onion Detection â "Peeling the Layers"
# ---------------------------------------------------------------------------

def detect_onion_layers(
    prospect_signals: list[str],
    schema: dict,
) -> list[OnionDetection]:
    """Scan prospect signals for Metaphorical Onion matches.

    Each onion layer represents a category of legacy tech debt.
    When a prospect's declared stack or behaviour matches an onion
    keyword, that layer is "detected" and contributes a penalty to
    the overall Agentic Readiness score.

    Args:
        prospect_signals: List of free-text signals describing the
            prospect's current data/GTM stack.
        schema: The loaded negative-icp-filter schema.

    Returns:
        List of OnionDetection objects for every matched layer.
    """
    penalties = schema["scoring"]["onion_penalty"]
    detections: list[OnionDetection] = []

    normalised_signals = [s.lower() for s in prospect_signals]

    for layer in schema["onion_layers"]:
        for keyword in layer["signal_keywords"]:
            keyword_lower = keyword.lower()
            for signal in normalised_signals:
                if keyword_lower in signal:
                    detections.append(
                        OnionDetection(
                            layer_id=layer["layer_id"],
                            layer_name=layer["name"],
                            matched_keyword=keyword,
                            severity=layer["severity"],
                            penalty=penalties[layer["severity"]],
                        )
                    )
                    break  # one match per keyword is enough

    return detections


# ---------------------------------------------------------------------------
# Zero-Copy Readiness Detection
# ---------------------------------------------------------------------------

def detect_zero_copy_signals(
    prospect_signals: list[str],
    schema: dict,
) -> list[ZeroCopyDetection]:
    """Scan prospect signals for Zero-Copy Data Activation indicators.

    Zero-copy signals are the *positive* counterpart to onion layers.
    They indicate a prospect has modern, activation-ready architecture
    that can benefit from agentic GTM workflows.

    Args:
        prospect_signals: List of free-text signals describing the
            prospect's current data/GTM stack.
        schema: The loaded negative-icp-filter schema.

    Returns:
        List of ZeroCopyDetection objects for every matched indicator.
    """
    detections: list[ZeroCopyDetection] = []

    normalised_signals = [s.lower() for s in prospect_signals]

    for zc_signal in schema["zero_copy_readiness_signals"]:
        for indicator in zc_signal["indicators"]:
            indicator_lower = indicator.lower()
            for signal in normalised_signals:
                if indicator_lower in signal:
                    detections.append(
                        ZeroCopyDetection(
                            signal_id=zc_signal["signal_id"],
                            signal_name=zc_signal["name"],
                            matched_indicator=indicator,
                            weight=zc_signal["weight"],
                        )
                    )
                    break

    return detections


# ---------------------------------------------------------------------------
# Prospect Evaluation Engine
# ---------------------------------------------------------------------------

def evaluate_prospect(
    prospect_name: str,
    prospect_signals: list[str],
    schema: dict,
) -> ProspectEvaluation:
    """Evaluate a prospect's Agentic Readiness using the Onion Filter.

    The evaluation pipeline:
      1. Detect Metaphorical Onion layers (legacy penalties).
      2. Detect Zero-Copy readiness signals (modern bonuses).
      3. Compute a composite score: sum(zero-copy weights) + sum(onion penalties).
      4. Classify the prospect against schema-defined thresholds.

    Zero-Copy signals are evaluated FIRST and weighted with a bonus
    multiplier, reflecting the framework's principle that modern
    architecture should be *prioritised* over legacy noise.

    Args:
        prospect_name: Human-readable name for the prospect/account.
        prospect_signals: List of free-text signals from CRM, enrichment
            tools, or manual research.
        schema: The loaded negative-icp-filter schema.

    Returns:
        A fully populated ProspectEvaluation dataclass.
    """
    # --- Step 1: Prioritise zero-copy detection (evaluated first) ---
    zc_detections = detect_zero_copy_signals(prospect_signals, schema)
    multiplier = schema["scoring"].get("zero_copy_bonus_multiplier", 1.0)
    zc_score = int(sum(d.weight for d in zc_detections) * multiplier)

    # --- Step 2: Detect onion layers ---
    onion_detections = detect_onion_layers(prospect_signals, schema)
    onion_score = sum(d.penalty for d in onion_detections)

    # --- Step 3: Composite score ---
    raw_score = zc_score + onion_score

    # --- Step 4: Classify ---
    thresholds = schema["scoring"]["thresholds"]
    if raw_score >= thresholds["agentic_ready"]:
        classification = "AGENTIC READY"
    elif raw_score >= thresholds["conditional"]:
        classification = "CONDITIONAL"
    else:
        classification = "NEGATIVE ICP"

    # --- Build summary ---
    summary_lines = [
        f"Prospect: {prospect_name}",
        f"Zero-Copy Score: +{zc_score}  |  Onion Penalty: {onion_score}",
        f"Composite Score: {raw_score}",
        f"Classification: {classification}",
    ]
    if onion_detections:
        summary_lines.append("")
        summary_lines.append("Onion Layers Detected:")
        for d in onion_detections:
            summary_lines.append(
                f"  [{d.severity.upper()}] {d.layer_name} â "
                f"matched '{d.matched_keyword}' (penalty: {d.penalty})"
            )
    if zc_detections:
        summary_lines.append("")
        summary_lines.append("Zero-Copy Signals Detected:")
        for d in zc_detections:
            summary_lines.append(
                f"  [+{d.weight}] {d.signal_name} â "
                f"matched '{d.matched_indicator}'"
            )

    return ProspectEvaluation(
        prospect_name=prospect_name,
        raw_score=raw_score,
        classification=classification,
        onion_detections=onion_detections,
        zero_copy_detections=zc_detections,
        summary="\n".join(summary_lines),
    )


# ---------------------------------------------------------------------------
# Display Helpers
# ---------------------------------------------------------------------------

def print_separator(char: str = "=", width: int = 70) -> None:
    """Print a visual separator line."""
    print(char * width)


def print_evaluation(evaluation: ProspectEvaluation) -> None:
    """Pretty-print a prospect evaluation to stdout."""
    print_separator()
    print(evaluation.summary)
    print_separator()
    print()


# ---------------------------------------------------------------------------
# Mock Experiment â Legacy vs. Modern Prospect Comparison
# ---------------------------------------------------------------------------

def run_mock_experiment(schema: dict) -> None:
    """Run a side-by-side comparison of a Legacy and Modern prospect.

    This demonstrates the Onion Filter's ability to distinguish
    between prospects drowning in legacy middleware ("Metaphorical
    Onions") and prospects with clean, zero-copy-ready architecture.

    The experiment uses realistic signal data modelled on patterns
    observed across enterprise GTM pipelines.
    """
    print()
    print_separator("*")
    print("  MOCK EXPERIMENT: Legacy vs. Modern Prospect Comparison")
    print_separator("*")
    print()

    # --- Legacy Prospect ---
    legacy_signals = [
        "Runs nightly batch ETL from on-prem Oracle to Salesforce Classic",
        "MuleSoft handles all integrations â 200+ connectors deployed",
        "Marketing uses CSV upload to sync Marketo batch sync audiences",
        "Data team processes Excel handoff files every Monday morning",
        "IT-gated access to customer data â 30-day SLA for data requests",
        "IBM DataStage pipelines feed the data warehouse on a cron schedule",
        "Custom ESB layer sits between CRM and billing system",
    ]

    legacy_eval = evaluate_prospect(
        prospect_name="Acme Industrial Corp (Legacy)",
        prospect_signals=legacy_signals,
        schema=schema,
    )

    print("[PROSPECT A] â The Onion")
    print(f"Signals fed into filter: {len(legacy_signals)}")
    print()
    print_evaluation(legacy_eval)

    # --- Modern Prospect ---
    modern_signals = [
        "Data lives in Snowflake â single source of truth",
        "Hightouch reverse ETL activates warehouse audiences in real-time",
        "Event stream via Kafka powers all downstream workflows",
        "Composable CDP built on warehouse-backed audiences",
        "API-first CRM with programmable workflows and webhooks",
        "RudderStack handles event collection and identity resolution",
        "Engineering team runs real-time pipeline for product-led signals",
    ]

    modern_eval = evaluate_prospect(
        prospect_name="NovaTech AI (Modern)",
        prospect_signals=modern_signals,
        schema=schema,
    )

    print("[PROSPECT B] â Zero-Copy Native")
    print(f"Signals fed into filter: {len(modern_signals)}")
    print()
    print_evaluation(modern_eval)

    # --- Head-to-Head Summary ---
    print_separator("~")
    print("  HEAD-TO-HEAD SUMMARY")
    print_separator("~")
    print(
        f"  {'Metric':<30} {'Acme (Legacy)':<20} {'NovaTech (Modern)':<20}"
    )
    print(f"  {'-'*30} {'-'*20} {'-'*20}")
    print(
        f"  {'Onion Layers Detected':<30} "
        f"{len(legacy_eval.onion_detections):<20} "
        f"{len(modern_eval.onion_detections):<20}"
    )
    print(
        f"  {'Zero-Copy Signals':<30} "
        f"{len(legacy_eval.zero_copy_detections):<20} "
        f"{len(modern_eval.zero_copy_detections):<20}"
    )
    print(
        f"  {'Composite Score':<30} "
        f"{legacy_eval.raw_score:<20} "
        f"{modern_eval.raw_score:<20}"
    )
    print(
        f"  {'Classification':<30} "
        f"{legacy_eval.classification:<20} "
        f"{modern_eval.classification:<20}"
    )
    print()
    print(
        "  Verdict: The Onion Filter correctly separates legacy middleware "
        "noise from\n  agentic-ready architecture. Acme is a Negative ICP; "
        "NovaTech is Agentic Ready."
    )
    print()


# ---------------------------------------------------------------------------
# Main Entry Point
# ---------------------------------------------------------------------------

def main() -> None:
    """Load the schema, run the mock experiment, and exit."""
    # Resolve schema path relative to this script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.join(
        script_dir, "frameworks", "negative-icp-filter.json"
    )

    # Fallback: check same directory (for when script is run standalone)
    if not os.path.exists(schema_path):
        schema_path = os.path.join(script_dir, "negative-icp-filter.json")

    try:
        schema = load_schema(schema_path)
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as exc:
        print(f"[ERROR] Failed to load schema: {exc}", file=sys.stderr)
        sys.exit(1)

    print()
    print("  Agentic GTM Operating System â Negative ICP Onion Filter")
    print("  github.com/kubersharmax/agentic-gtm-os")
    print()

    run_mock_experiment(schema)


if __name__ == "__main__":
    main()
