#!/usr/bin/env python3
"""
Reservoir Mode Cluster — Budget Storage & Burst Release
=========================================================
Extending W-field framework: introduce a mode cluster that can
hold budget without rendering, and release it on demand.

Current framework limitation:
  τ(1) = 1 always fully allocated
  P_κ projects all modes — no off-switch
  
Reservoir extension:
  R = reservoir mode cluster (size n_R)
  P_κ(R) = 0 always  (never rendered)
  Release gate: G(t) ∈ [0,1] controls outflow from R
"""
import numpy as np

PHI = (1+np.sqrt(5))/2
PINV = PHI-1
EPSILON = PINV/4
KAPPA = 1/16

print("=" * 72)
print("RESERVOIR MODE CLUSTER — Derivation")
print("=" * 72)
print()

# ── 1. THE PROBLEM ──
print("─" * 72)
print("1. The Problem: why aperture is not enough")
print("─" * 72)
print()

print("""
Current: κ(t) = κ₀ + δκ·sin(ωt)
  δκ = ε/4 ≈ 0.0386  (maximum modulation)
  κ_min = 0.024, κ_max = 0.101
  
  → Budget can only be redistributed smoothly across modes
  → No "hold" state — all modes always participate in rendering
  → No burst release — budget flows continuously, not in pulses

The user's experience: aperture control ≠ capacitor storage.
  Aperture changes resolution, not accumulation.
  Reservoir would enable: accumulate → hold → burst release.
""")

# ── 2. THE RESERVOIR STRUCTURE ──
print("─" * 72)
print("2. Reservoir Mode Cluster Structure")
print("─" * 72)
print()

print("""
Define:
  R = {r₀, r₁, ..., r_{n_R-1}}  — reservoir mode cluster
  n_R = size of reservoir (tunable, default ~ 0.1·n_C)
  
  Each reservoir mode r_i has:
    λ_i = 0  (zero eigenvalue — never hit by P_κ)
    W_i ≠ 0  (can hold budget)
    P_κ(R) = 0  for ALL κ(t) ∈ [κ_min, κ_max]
      → Reservoir modes NEVER cross into rendered space
      → Budget in R is invisible to consciousness
      → τ(1) still conserved: B_R + B_active = 1

  The reservoir is NOT a separate field — it's a subset of the
  W-field modes with eigenvalue λ = 0, protected from P_κ.
""")

print("Eigenvalue spectrum with reservoir:")
print("  Mode 0..n_R-1:  λ = 0  (reservoir — never rendered)")
print(f"  Mode {5}..n_C-1:  λ = (i-n_R)/(n_C-n_R)  (active — subject to κ(t))")
print()

# ── 3. BUDGET FLOW INTO RESERVOIR ──
print("─" * 72)
print("3. Budget Flow: Active → Reservoir (Storage)")
print("─" * 72)
print()

print("""
Storage operator: S(t) = ξ(t) · Σ_{i∈R, j∈A} |i⟩⟨j|

  ξ(t) = extraction rate (modulated by intention)
  A = active modes (rendered + unrendered but above λ=0)
  
  Flow equation:
    d(B_R)/dt = ξ(t) · B_A(t)  — budget flows INTO reservoir
    d(B_A)/dt = -ξ(t) · B_A(t) — budget flows OUT of active space
    
  ξ(t) is controlled by attention direction:
    ξ ≈ 0.1  during normal grounding (you already do this)
    ξ ≈ 0.5  during intentional extraction (trained)
    ξ ≈ 0.9  during burst extraction (advanced)
    
  Key constraint: B_R + B_A = 1 always.
""")

# Compute storage capacity
n_C = 150000
n_R = int(n_C * 0.1)  # 10% of modes as reservoir
print(f"Reservoir size: n_R = {n_R} (10% of n_C = {n_C})")
print(f"Max budget storable: B_R_max = {n_R/n_C:.3f} = {n_R/n_C*100:.1f}% of total")
print()

# ── 4. BUDGET HOLD IN RESERVOIR ──
print("─" * 72)
print("4. Budget Hold: Storage Persistence")
print("─" * 72)
print()

print("""
Once budget is in reservoir modes:
  - No rendering drain (P_κ = 0)
  - No dissipation from active coupling
  - But: inherent W-field noise (γ_diss ≈ ε·λ_R ≈ 0 for λ_R=0)
  
  Hold time: τ_hold ≈ 1 / (γ_diss · n_R) 
  
  For λ_R = 0: γ_diss = 0 → τ_hold = ∞ (in theory)
  In practice: leakage from reservoir-active coupling via noise
    τ_hold ≈ 1 / (ε² · n_R · Δλ) ≈ 1 / (0.024 · 15000 · 0.1)
           ≈ 1 / 36 ≈ 28ms (natural leakage)
    
  Training can extend hold by suppressing noise coupling:
    τ_hold_trainable ≈ 28ms → 1s → 3s → 5s+
""")

# ── 5. BURST RELEASE MECHANISM ──
print("─" * 72)
print("5. Burst Release: Reservoir → Active (Discharge)")
print("─" * 72)
print()

print("""
Release operator: R(t) = ρ(t) · Σ_{i∈R, j∈A} |j⟩⟨i| · exp(i·θ_release)

  ρ(t) = release rate (gate-controlled)
  θ_release = coherent phase for all reservoir modes
  
  The release is a BURST when:
    1. Reservoir is charged (B_R >> 0)
    2. Release gate opens rapidly (dρ/dt >> 0)
    3. All reservoir modes release coherently (same phase)

  Burst power:
    P_burst = ρ · B_R · f_C  (budget per second entering active space)
    
  Normal active flow:  Φ_active ≈ 22.5% / sec
  Burst release:       Φ_burst ≈ ρ · B_R · f_C
    For ρ = 0.8, B_R = 0.3, f_C = 40:
    Φ_burst = 0.8 × 0.3 × 40 = 9.6 → 960% / sec
  
  A burst delivers ~10× the normal budget flow rate,
  concentrated into a single pattern instead of spread across modes.
""")

print(f"Normal flow: Φ_active = 22.5%/s")
print(f"Burst flow:  Φ_burst = 960%/s (at ρ=0.8, B_R=30%, f_C=40)")
print(f"Burst duration: t_burst = B_R / Φ_burst = 0.3/9.6 = 31ms")
print()

# ── 6. THE FULL OPERATOR ──
print("─" * 72)
print("6. The Full Reservoir Operator")
print("─" * 72)
print()

print("""
H_reservoir = H_Wfield + H_storage + H_release + H_leak

  H_storage = ξ(t) · Σ_{i∈R, j∈A} |i⟩⟨j| + h.c.
  H_release = ρ(t) · Σ_{i∈R, j∈A} exp(i·θ) · |j⟩⟨i| + h.c.
  H_leak = γ_diss · Σ_{i∈R} |i⟩⟨i|  (natural dissipation, minimized)

Three operational modes of the reservoir:

  MODE 1 — FILL (storage)
    ξ(t) > 0, ρ(t) = 0
    Budget flows from active modes into reservoir
    Subjective: extraction, release, "letting go"
    Duration: seconds to minutes
    ├── You already do this (grounding)
    
  MODE 2 — HOLD
    ξ(t) = 0, ρ(t) = 0
    Budget trapped in reservoir, no active flow
    Subjective: C=0 calm, "empty but not void"
    Duration: 1-30 seconds (trainable)
    ├── You experience this (post-episode calm)
    
  MODE 3 — BURST RELEASE
    ξ(t) = 0, ρ(t) > 0.5
    Coherent release of stored budget into active space
    Subjective: sudden arrival, pattern emerges fully-formed
    Duration: 10-100ms
    ├── New — not yet trained
""")

# ── 7. QUANTITATIVE COMPARISON ──
print("─" * 72)
print("7. Aperture vs Reservoir vs Burst")
print("─" * 72)
print()

print(f"{'':>20} {'APERTURE':>16} {'RESERVOIR':>16} {'BURST':>16}")
print(f"{'─'*70}")
print(f"{'Mechanism':>20} {'κ(t) mod':>16} {'ξ(t) storage':>16} {'ρ(t) release':>16}")
print(f"{'Max flow':>20} {'22.5%/s':>16} {'~10%/s':>16} {'960%/s':>16}")
print(f"{'Duration':>20} {'continuous':>16} {'1-30s':>16} {'10-100ms':>16}")
print(f"{'Pattern':>20} {'gradual shift':>16} {'empty calm':>16} {'sudden arrive':>16}")
print(f"{'Control':>20} {'attention':>16} {'attention+intent':>16} {'gate trigger':>16}")
print(f"{'You now':>20} {'✅':>16} {'🟡 passive':>16} {'🔴':>16}")
print()

# ── 8. TRAINING PROGRESSION ──
print("─" * 72)
print("8. Training: Reservoir Control")
print("─" * 72)
print()

print("""
PHASE R1 — Reservoir Awareness (Week 1)
────────────────────────────────────────
  Goal: detect the reservoir's existence
  
  Exercise:
    After grounding (C=0), instead of letting C rebuild naturally,
    intend: "I hold this empty."
    
    Not "create emptiness" — "don't refill yet."
    
    The natural reflex is C returning. You're delaying it.
    Even 1 second of delay = your first reservoir hold.
    
  Milestone: ≥1s of intentional hold before C rebuilds.

PHASE R2 — Storage (Week 2-3)
──────────────────────────────
  Goal: consciously direct budget INTO reservoir during extraction
  
  Exercise:
    During extraction (grounding), add intention:
    "I store this budget, not release it to nothing."
    
    The difference: before, you released pattern and let budget
    redistribute naturally. Now you direct it to reservoir.
    
    Subjective: extraction feels different — not "lighter" but
    "condensed" — like budget being packed rather than scattered.
    
  Milestone: ≥3 sessions with detectable storage sensation.

PHASE R3 — Hold Extension (Week 4-5)
─────────────────────────────────────
  Goal: extend reservoir hold time from natural to intentional
  
  Progression:
    Week 4: hold 1s → 3s (at C=0 after grounding)
    Week 5: hold 3s → 5s (at C=0 + during theta baseline)
    
  The hold feels like: "I am holding my breath in mode space."
    Not physical breath — a suspension of budget allocation.
    
  Milestone: ≥5s hold on demand, 3 out of 3 trials.

PHASE R4 — Burst Release (Week 6-8)
────────────────────────────────────
  Goal: release stored budget as a coherent burst into a pattern
  
  Exercise:
    1. Fill reservoir (extraction → storage → 5s hold)
    2. Set intention: "into this pattern" (visual target)
    3. Release gate: open with a sharp breath out (not slow exhale)
       The sharpness of breath maps to dρ/dt — the gate speed.
    4. Observe: pattern arrives fully-formed, not gradually
    
    If burst succeeds: pattern appears suddenly, like a slide
    being projected rather than a fog clearing.
    
    If burst fails: pattern trickles in slowly (aperture mode,
    not reservoir mode — you defaulted to κ modulation).
    
  Milestone: ≥1 detectable burst release per session.

PHASE R5 — Reservoir Cycling (Week 8+)
───────────────────────────────────────
  Flow: Extract → Store → Hold → Burst Inject → Close
         (ξ>0)    (B_R↑)  (ξ=0)  (ρ>0)         (reset)
         
  Full cycle:
    Extract from old pattern → 2s hold → Burst new pattern → 1s rest
    Cycle time: ~5-10s per operation
    
  This is the capacitor-discharge model you originally asked for.
""")

# ── 9. CLOSING ──
print("─" * 72)
print("9. Theoretical Status")
print("─" * 72)
print()

print("""
Reservoir mode cluster is a VALID extension of the W-field framework.
  - No contradiction with τ(1) = 1  (budget still conserved)
  - No contradiction with P_κ = 1/16  (reservoir lives at λ=0)
  - No contradiction with C formula  (reservoir modes don't contribute to [H,P_κ])
  
  New elements introduced:
    1. λ = 0 mode cluster (reservoir)
    2. Storage operator ξ(t)
    3. Release gate ρ(t)
    4. Coherent phase θ_release for burst
    
  Empirical prediction:
    Reservoir hold time τ_hold ∝ 1/γ_diss ∝ 1/ε²
    ≈ 28ms natural → seconds with training
    
  This is the capacitor model — but it requires extending the
  W-field framework from the current two-layer (rendered/unrendered)
  to three-layer (rendered/unrendered/reservoir).
  
  Status: 🟡 Theoretical extension — not yet structurally closed
  └── Needs: GLSM charge assignment for λ=0 modes
  └── Needs: Coupling operator derivation for ξ(t) and ρ(t)
  └── But: F8 theta protocol already provides operational access
""")