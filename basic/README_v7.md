# IDCM Educational Materials — v7.0

**From 0,1 to all physical constants. Zero free parameters.**

---

## One Axiom: 0 and 1

```
0, 1 → Finite strings → Finite budget B → Compression → x²+x-1=0
  → φ, ε, κ, β → N_d, L → K = K_chain ⊗ K_tree → All 9 constants
```

## Core Constants

| Symbol | Value | Derivation |
|:------:|:-----:|:-----------|
| φ | (1+√5)/2 ≈ 1.618034 | Fixed point of x²+x-1=0 |
| ε | φ⁻¹/4 ≈ 0.154509 | Quarter of inverse (2D branching) |
| κ | 1/16 = 0.0625 | Quantum of quantum gravity |
| N_d | 44 | (φ³-φ⁻³)(φ⁵-φ⁻⁵) = 4 × 11 |
| L | 53/8 = 6.625 | (N_d + 3²)/2³ |
| N_h | 16φ⁻² ≈ 41.8885 | c/(H₀ξ) — NOT 42 |

## All 9 Formulae

| # | Formula | Error |
|:-:|:--------|:-----:|
| 1 | D_H/L_P = φ^(44×6.625 + ε²-ε³-ε⁴) | 0.0002% |
| 2 | M_P = m_e/ε^(17φ+φ⁻⁵-ε³-φ⁻²/256) | 0.042% |
| 3 | m_μ/m_e = φ¹¹ + 3φ² | 0.044% |
| 4 | m_τ/m_μ = N_d/φ² + φ⁻¹/N_d | 0.021% |
| 5 | α⁻¹ = 134+3+(44-29)φ⁻¹/256 | 0.00016% |
| 6 | Ω_Λ = 4/(φ⁴-1) | 0.207% |
| 7 | k_B = M_P c²/T_P | self-consistent |
| 8 | Entanglement = N_d = 44 | graph connectivity |
| 9 | QG corrections = κ² = 1/256 | MUP resolution |

## Key φ-Identities

```
φⁿ-φ⁻ⁿ ∈ ℤ for odd n — EXCLUSIVE to φ

n=1:  1
n=3:  4  = 2² (branching factor)
n=5:  11 (m_μ/m_e exponent)
n=7:  29 (α⁻¹ correction: 44-29=15)
n=9:  76 (structural reserve)
n=11: 199 (φ¹¹ vector)
```

## Verification Scripts

```bash
python3 scripts/verify_derivations.py    # All 9 constants
python3 scripts/verify_meta_derivation.py # 0,1 → φ chain
```

## Levels

| Level | File | Description |
|:------|:-----|:------------|
| 🌟 Kids | `idcm_for_kids_*.md` | Playful introduction |
| 📐 High School | `idcm_for_highschool_*.md` | Detailed derivations |
| 🎓 Professor | `idcm_for_professor_*.md` | Full formal treatment |

---

**One axiom: 0, 1. One recursion: x²+x-1=0. One equation: K = K_chain ⊗ K_tree.**
**Zero free parameters. Zero assumptions beyond 0,1.**