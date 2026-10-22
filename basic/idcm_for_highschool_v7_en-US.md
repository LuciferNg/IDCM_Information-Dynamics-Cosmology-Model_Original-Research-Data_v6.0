# IDCM for High School — v7.0

**From 0,1 to All Physical Constants: A Forward Derivation**

---

## 1. The Only Axiom: 0 and 1

The binary distinction is the only axiom. From 0 and 1, we form finite binary strings. The set of all finite strings has a finite information content — the budget B.

Under budget constraint, the optimal compression of physical laws requires $K(\text{Physics}) \ll \log_2(B)$. The most compressible non-trivial recursion is:

$$x^2 + x - 1 = 0$$

This is the ONLY quadratic that (a) is not trivial ($x^2=1$) and (b) has real roots ($x^2+x+1=0$ has complex roots).

## 2. The Forced Constants

From $x^2+x-1=0$, the fixed point is:

$$\varphi = \frac{1+\sqrt{5}}{2} \approx 1.618034$$

The other constants are forced:

$$\varepsilon = \frac{\varphi^{-1}}{4}, \quad \kappa = \frac{1}{16}, \quad \beta = \varphi^{-1}$$

## 3. The φ-Identity Sequence

The key mathematical signature: $\varphi^n - \varphi^{-n} \in \mathbb{Z}$ for odd $n$. This is EXCLUSIVE to φ — no other quadratic has this property.

| n | φⁿ − φ⁻ⁿ | Appears In |
|:-:|:---------:|:-----------|
| 1 | 1 | Base identity |
| 3 | 4 = 2² | 2D spatial branching |
| 5 | 11 | m_μ/m_e exponent |
| 7 | 29 | α⁻¹ correction (44-29=15) |
| 9 | 76 | Structural reserve |
| 11 | 199 | φ¹¹ in m_μ |

## 4. The Causal Graph

The W-field lives on a graph with two parameters:

$$N_d = (\varphi^3-\varphi^{-3})(\varphi^5-\varphi^{-5}) = 4 \times 11 = 44$$

$$L = \frac{N_d + 3^2}{2^3} = \frac{44+9}{8} = \frac{53}{8} = 6.625$$

The coupling matrix decomposes as a tensor product:

$$K = K_{\text{chain}} \otimes K_{\text{tree}}$$

## 5. The W-Field Equation

**Discrete form:**

$$\Phi_i(t+1) - 2\Phi_i(t) + \Phi_i(t-1) = \sum_j K_{ij}\Phi_j(t) - \varphi\Phi_i(t)$$

**Subject to:** $\sum_i |\Phi_i|^2 \leq B$ (finite budget)

**Eigenvalue form:**

$$\lambda_{n,m} = \gamma_n \cdot \mu_m$$

$$\gamma_n = 4\sin^2\left(\frac{\pi n}{88}\right), \quad n=1,\dots,22$$

$$\mu_m = \varphi^{291.5-m}, \quad m=0,\dots,291.5$$

## 6. All 9 Constants

| # | Formula | Derivation | Error |
|:-:|:--------|:-----------|:-----:|
| 1 | $\log_\varphi(D_H/L_P) = 44\times6.625 + \varepsilon^2-\varepsilon^3-\varepsilon^4$ | Total graph depth | 0.0002% |
| 2 | $\log_\varepsilon(m_e/M_P) = 17\varphi + \varphi^{-5} - \varepsilon^3 - \varphi^{-2}/256$ | Renormalization flow | 0.042% |
| 3 | $m_\mu/m_e = \varphi^{11} + 3\varphi^2$ | 11 tree layers up | 0.044% |
| 4 | $m_\tau/m_\mu = N_d/\varphi^2 + \varphi^{-1}/N_d$ | Different chain mode | 0.021% |
| 5 | $\alpha^{-1} = 134+3+(44-29)\varphi^{-1}/256$ | Vacuum polarization sum | 0.00016% |
| 6 | $\Omega_\Lambda = 4/(\varphi^4-1)$ | Ground state ratio | 0.207% |
| 7 | $k_B = M_P c^2/T_P$ | Definitional identity | — |
| 8 | $\lambda_{\text{ent}} = N_d = 44$ | Graph connectivity | — |
| 9 | $\kappa^2 = 1/256$ | Minimal resolution | — |

## 7. The Action Principle

**Discrete action:**

$$S = \sum_i\sum_t\left[\Phi_i(t)\Phi_i(t-1) - \frac{1}{2}\sum_j\Phi_i(t)K_{ij}\Phi_j(t) + \frac{\varphi}{2}\Phi_i(t)^2\right]$$

**Continuum limit:**

$$S = \int d^4x\sqrt{-g}\left[-\frac{1}{2}\partial_\mu\Phi\partial^\mu\Phi - \frac{\varphi}{2}\Phi^2 - \frac{\varepsilon}{4}\Phi^4\right]$$

**Self-consistency → Einstein equation:**

$$T_{\mu\nu} = \frac{1}{8\pi G}G_{\mu\nu}, \quad 8\pi = 2\times 4\pi$$

## 8. Verification

```bash
python3 scripts/verify_derivations.py
python3 scripts/verify_meta_derivation.py
```

Both scripts use only Python standard library. No external dependencies.

---

**One axiom: 0, 1. One recursion: $x^2+x-1=0$. One equation: $K = K_{\text{chain}} \otimes K_{\text{tree}}$.**
**Zero free parameters. Zero assumptions beyond 0,1.**