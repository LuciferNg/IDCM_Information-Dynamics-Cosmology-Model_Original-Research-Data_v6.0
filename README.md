# IDCM v6.0 — Information-Dynamics-Cosmology-Model

**Information Dynamics Cosmology Model（資訊動力學宇宙論模型）— 6th Generation**

> `Information-Dynamics-Cosmology-Model` 係版本代號，唔係理論名稱。理論名稱由 v1.0 到 v11.0 一直係 Information Dynamics Cosmology Model，從未改變；本版係 `IDCM` 縮寫首次用於 repo 名的一版。
>
> v6.0 的職責係擴張對象：v5.0 只解釋膨脹歷史，v6.0 要解釋 19 個 SM 參數、暗物質質量、量子引力與電磁，並把四個常數追到 `CY₃(36,98)` 的拓撲。

## 緣起

v5.0 交出一條遞迴、一個凸起、`Δχ² = −9.80`（1848 dof）與 5 個擬合參數。它能講「膨脹史點解有 bump」，唔能講「為何電子質量係 0.511 MeV」。

`README_en-US.md` 開頭有一段自述，是理解本版的入口：IDCM 係**逆向工程**，唔係由第一原理前向推導。

```
ΛCDM/SM data → N_h from DESI bump → 4-domain architecture →
formula normalization → CY₃(36,98) matching → geometric verification
```

`x² + x − 1 = 0` 唔係生成公理，係校準器站在 κ 上能夠挖到的最深一層。所有公式由已測數據反挖而出，再以 IDCM 內部結構（MERA、SYNC、CLT）正規化。遞迴提供一致性框架去驗證挖掘，唔提供前向證明。

「零自由參數」的意思因此要讀準：每個數字都係**恢復**（recovered）而非**擬合**（fitted），但恢復出的數字唔等於前向推導出的數字——它們是通過一致性檢查的數字（`README_en-US.md` §Read This First）。

v6.0 因此做四件事：

1. **量子化指數**：把 φ-指數寫成 `M = 33`（MERA 深度）與 `N_h = 42`（視界層數）的整數倍，令 19 個 SM 參數變成離散譜上的點
2. **給幾何身體**：`CY₃(36,98)`（`h^{1,1} = 36`、`h^{2,1} = 98`、`χ = −124`、`Ind(L) = 48`）在 Kreuzer–Skarke 庫中驗證，令質量指數有拓撲來源
3. **分三期攻堅**：Phase I 味物理 19/19、Phase II 量子引力 9 個 attack vector、Phase III 電磁與動力學 12 主題
4. **立可證偽預言**：1853 個數據點全協方差對照，`Δχ² = −9.8`（約 3.1σ）

驗收標準：任何常數必須能寫成 `{M, N_h, β, ε}` 的封閉式；寫不出就用「未記錄」，唔准以擬合窗補位。

## 版本演進：v5.0 → v6.0

IDCM 係**逆向工程**：由已觀測的常數與結構反推生成機制，唔預設公理、唔設「核心假設」。因此版本之間的分野唔係假設改變，而係**逆推對象改變**。

### v5.0 — Recursive-Structural-Cosmology

- 形態：單遞迴 `C_{n+1} = 1/(1+C_n)` 加弗里德曼凸起 `f(z) = 1 + ε(z/z_c)e^{−z/z_c}`
- 常數：`ε = φ⁻¹/4 = 0.1545085`、`κ = (εφ)² = 1/16`、`β = φ⁻¹/2 = 0.309`
- 觀測：`Δχ² = −9.80`（1848 dof）、`H₀ = 68.2 ± 0.4`、BAO 6 箱 `χ² = 9.22`
- 已拆：OAS（2026-07-16，`data/oas_dissolve/OAS_reference.en-US.md` 記「dismantled 2026-07-16」）
- 未答：19 個 SM 參數一個都未解釋

### 根因：兩個未解的自由度

1. **常數有數值，無身份**。`ε`、`κ`、`β`、`z_c` 在 v5.0 只是四個好數，冇講出「為何係呢四個、為何係 φ 的 -1、-2、-4 次方」。缺一個離散結構去承載整數指數 ⟹ 每個質量比都可以事後凑一個 φ 冪，而凑法不可數。
2. **「零參數」與「五參數擬合」並存而未記賬**。v5.0 的結構常數零參數，但 `Ω_m`、`h`、`Ω_b h²`、`σ₈`、`n_s` 五個宇宙學參數仍由 MCMC 定。模型整體並非零參數，而舊敘述把兩件事寫成一件。

兩者同源：遞迴只給一條標度（`φ`），唔給「標度的指數從哪來」。要解釋 19 個參數，必須先有可數的整數結構。

### v6.0 — Information-Dynamics-Cosmology-Model

- **四常數**：`M = 33`（MERA RG 深度）、`N_h = 42`（KK tower cutoff／視界層數）、`β = φ⁻¹/2`、`ε = φ⁻¹/4`
- **19 個 SM 參數**：9 個費米子質量、Higgs 質量、CKM 四參數、PMNS 四參數、溫伯格角（`README_en-US.md` §Achievement）
- **暗物質**：`M_DM = M_P·e⁻⁴⁸·φ^{−1/2} = 13.68 MeV`（0.88%），`e⁻⁴⁸` 之 48 來自 `Ind(L) = 48`
- **幾何**：`CY₃(36,98)` 於 KS 庫 100+ polytopes 命中；`M = N_h − 9 = 33`，`9 = N_h − M`；`c₂[0] = −288 = −(32 × 9)`
- **Phase I 味物理**：19/19 參數；`k_u = 33β`、`k_d = 26β − φ⁻⁴`、`k_l = 19β`
- **Phase II 量子引力**：9 個 attack vector 全閉——質子衰變、引力子為 W-field 模、黑洞熵 `S = A/4G`（`1/4 = εφ`）、暴脹 `r = 0.00149`、`n_s = 0.959 ± 0.006`、`f_NL = +0.06`、退相干、全息糾纏熵、moduli 穩定、10D→4D 約化
- **Phase III 電磁**：12 主題閉合，EM 為 W-field 集體模而非基本 U(1)
- **代價（2026-07-20 自審）**：`AUDIT_REPORT.md` 抓出 CKM 舊式 `φ^{Δk/2}` 三元素偏 2.6×／39×／742×；中微子 seesaw 與 κ 公式差 5×10⁸；宇宙學常數差約 10⁵⁶；dS vacuum 判未解

## 研究路線

八層，上層不得借用下層未記賬的自由度：

**L0 生成式層** — 一條二次方程

- `x² + x − 1 = 0`，正根 `φ⁻¹ = (√5 − 1)/2 = 0.6180339887`
- 遞迴 `C_{n+1} = 1/(1+C_n)`，`C₀ = 1`；`C_n = F_n/F_{n+1}`
- 收斂線性：`λ = φ⁻² = 0.381966`，八步後誤差 < 10⁻³
- 解釋地位：最深可達層，非生成公理（`README_en-US.md` §Read This First）

**L1 常數層** — 四常數閉合

- `ε = φ⁻¹/4 = 0.1545084972`；factor 4 來自最小非平凡對稱分裂 `2 × 2`
- `κ = (εφ)² = 1/16 = 0.0625` 為代數恆等：`εφ = 1/4`
- `β = φ⁻¹/2 = 0.3090169944`；以 Cepheid/TRGB 比驗證 `(1.77/0.05)^β = 3.01`（觀測 3.03）
- `z_c = 0.6 ± 0.05`；DESI DR2 獨立給 0.58 ± 0.08、DES-SN5YR 給 0.62 ± 0.10

**L2 幾何層** — 指數的拓撲來源

- `CY₃(36,98)`：`h^{1,1} = 36`、`h^{2,1} = 98`、`χ = −124`、`Ind(L) = 48`
- `M = N_h − 9 = 33` 為 MERA RG 深度，亦係 Kähler moduli 數
- monad 序列 `0 → V → B → C → 0`；`h¹(V) = 3`、`Ind(V) = −6`
- Koszul 複體給 Yukawa 張量係數；`J*` 為穩定化 Kähler 類

**L3 味物理層** — Phase I（19/19）

- 費米子 9 質量：`φ^{−Mβ}`、`φ^{−(M−7)β − φ^{−4}}`、`φ^{−(M−14)β}` 三條主式
- Higgs：`m_H = v·φ^{−9β/2} = 125.99 GeV`（0.71%）
- CKM：`V_us`、`V_cb = φ^{−M/5}`、`V_ub = φ^{−(M/5+M/11+2)}`、`δ_CP = π/2 − arctan β`
- PMNS：`θ₁₂ = arctan φ⁻¹ + 1/M`、`θ₂₃ = π/4`、`θ₁₃ = arcsin(ε(M−1)/M)`、`δ_CP = π + arctan φ⁻³`
- 溫伯格角：`sin²θ_W = (3/8)·φ⁻¹ = 0.23176`（0.23%）

**L4 量子引力層** — Phase II（9 個 attack vector）

- AV-1 質子衰變 `τ(p→e⁺π⁰) = 9.8×10³⁵ yr`（monad map 修正後），`M_GUT = 1.24×10¹⁶ GeV`
- AV-2 引力子 = W-field 模；`c/(H₀ξ) = 16φ² = 41.8885`
- AV-3 黑洞熵 `S = A/4G`，`1/4 = εφ`；AV-4 暴脹 `r = 0.00149`、`n_s = 0.959`、`f_NL = +0.06`
- AV-5 退相干 `Γ = ε²(E/ℏ)(L/ξ)²`；AV-6 全息糾纏熵修正 2.4% at ξ
- AV-7 moduli 全部 `m > 10¹⁸ GeV`、`τ < 10⁻⁴³ s`；AV-8 10D→4D 約化；AV-9 暗能量

**L5 電磁層** — Phase III（12 主題）

- 立場：`U(1)_em` 非基本對稱，光子係 W-field 集體模（引力子的對稱夥伴）
- 12 主題：W-field EM 基礎、電子動力學、Maxwell 湧現、EM Lagrangian、精細結構、極端 EM、光子波、動能理論、導電、`𝒩` 凝聚、宇宙弦排除、Phase III 閉合報告
- 自評矛盾：`01_WFIELD_EM_FOUNDATION_en-US.md` 內文標「Foundation PDE requires reformulation」，與入口頁「12 topics closed」並存

**L6 觀測層** — 1853 點全協方差

- BAO DESI DR2 6 箱 `χ² = 9.22`；SNe DES-SN5YR 1820 點 `χ² = 1639.8`
- CMB shift `R = 1.7425`；RSD 20 點 `χ² = 13.7`；弱透鏡 `S₈ = 0.786`
- 合計 `Δχ² = −9.8`（約 3.1σ）
- `H₀` 同步相位：Cepheid 73.05 對 73.04（+0.01σ）、TRGB 69.80 對 69.80（0.00σ）、Planck +1.56σ、JWST −1.85σ

**L7 開放層** — 明確未閉合

- 宇宙學常數：`ρ_Λ` 預估 `10⁴⁴ eV⁴` 對觀測 `10⁻¹² eV⁴`（差約 10⁵⁶）
- 規範耦合 `g`、`g'` 未由遞迴導出（`data/problems/gauge_couplings.en-US.md`）
- dS vacuum：`DS_VACUUM_DISCLAIMER` 標未解，並註明「shared by all string theory」
- 暗物質候選：`data/problems/dark_matter.en-US.md` 開篇仍寫「IDCM has no dark matter particle candidate」

## 項目結構

```
IDCM-v6.0--Information-Dynamics-Cosmology-Model/
├── README.md                        # 語言選擇器（8 語）
├── README_en-US.md                  # 英文完整版（325 行，本檔主要依據）
├── README_zh-TW / zh-CN / zh-HK / ja-JP / ko-KR / es-ES / fr-FR.md   # 其餘 7 語
├── ALL_IN_ONE_IDCM.md / .pdf        # 單檔全集
├── data/                            # 471 檔，22 個主題子目錄（本 repo 主體）
│   ├── cy_search/                   # 176 檔：CY₃(36,98) 搜尋（自述 48 組雙語文檔 + validation/）
│   │   ├── README.md                # 搜尋目標、11 項驗證、工具鏈
│   │   ├── AUDIT_REPORT.md          # 2026-07-20 文檔自審（12 項中 10 正、CKM 三錯）
│   │   ├── CKM_ACCURACY_STATUS_*    # V_us 5.4% → 1.7%（Δ-current κ-ratio）
│   │   ├── CKM_CLOSURE_*            # c₂[0] = −288 ⟹ M = 33
│   │   ├── FERMION_EXPONENTS_FIRST_PRINCIPLES_*  # 9 質量指數
│   │   ├── YUKAWA_COUPLINGS_* / KOSZUL_*         # Yukawa 張量與 Koszul 係數
│   │   ├── HIGGS_MASS_* / NEUTRINO_SECTOR_* / PMNS_CP_PHASE_*  # 味物理閉合
│   │   ├── DARK_MATTER_MASS_* / DARK_MATTER_MASS_ORIGIN_*      # 13.68 MeV 與 e⁻⁴⁸
│   │   ├── CY3_VERIFICATION_* / SU3_BUNDLE_FRAMEWORK_*         # 幾何驗證
│   │   ├── HOLOGRAPHIC_CODE_* / SPEED_OF_LIGHT_HOLOGRAPHY_*    # 全息碼與光速
│   │   ├── DS_VACUUM_*              # dS vacuum：未解，附 disclaimer
│   │   └── validation/              # 8 支驗證腳本 + run_all.sh（make validate-all）
│   ├── quantum_gravity/             # 49 檔：Phase II 九個 attack vector（01–26 為 Phase I 記錄）
│   ├── em_dynamics/                 # 62 檔：Phase III 12 主題（01–12，雙語）＋ RFQ 生物共振
│   ├── p_n_spectrum/                # 11 檔：P_n 譜 n = 0–6（P₀ = 2.182×10¹⁷ GeV）
│   ├── monad_map_search/            # 13 檔：monad map 多項式搜尋（自評需暴力搜尋）
│   ├── oas_dissolve/                # 4 檔：OAS 拆除記錄（2026-07-16）
│   ├── absolute_yukawa/             # 8 檔：9 個絕對質量與 2-loop RG 修正
│   ├── proton_decay/                # 3 檔：τ = 9.8×10³⁵ yr、M_GUT
│   ├── problems/                    # 8 檔：4 個經典難題（CC／DM／g,g'／三代）
│   ├── mass_hierarchy / muon_mass / delta_cp / delta_cp_structural  # 單點推導
│   ├── gut_breaking / true_dm / dark_matter_p4 / dark_energy_wfield / inflation_wfield / baryogenesis_wfield  # 分主題攻堅
│   ├── spacetime_modulation / curvature_radius / large_scale_structure / E_equals_mc2 / heat_death_restart  # 宏觀與結構
│   ├── information_dynamics_sociology/  # 16 檔：非物理延伸（社會學類比）
│   ├── MCMC/                        # 11 檔：DES-SN5YR 全後驗
│   ├── paper/                       # 16 檔：論文草稿（含「為何三代」）
│   ├── predictions/                 # 4 檔：同步波集體模預言
│   └── *.py                         # 頂層腳本：explore_alpha、higgs 驗證、視覺化
├── codes/                           # 6 支：DES-SN5YR 似然、綜合驗證、SH0ES MCMC（雙語各一）
├── scripts/                         # 111 檔：CYTools／SageMath／WolframScript／cohomCalg 攻堅腳本
├── basic/                           # 27 檔：小學／高中／教授三級 × 多語（含 6 個 v7 後版檔）
├── figures/                         # 19 張圖
├── papers/                          # 12 篇參考論文 PDF
├── animations/                      # 5 檔：宇宙循環、H(z) 凸起、H₀ 同步、遞迴 GIF
├── Makefile                         # validate / validate-all / setup / clean
└── requirements.txt                 # numpy、scipy、matplotlib
```

## 狀態快照（2026-11-03 重數；數字以實際檔案為準）

```
實際檔案
  總檔案                             667
  markdown                           375
  python                             163
  data/                              471（22 個主題子目錄）
  data/cy_search/                    176（自述 48 組雙語文檔 + validation 8 支腳本）
  data/quantum_gravity/              49
  data/em_dynamics/                  62
  scripts/                           111
  basic/                             27（含 v7 後版遺留 6 檔）
  codes/                             6
  papers/ ｜ figures/ ｜ animations   12 ｜ 19 ｜ 5

自述進度（README_en-US.md）
  Phase I 味物理                     19 / 19 參數
  Phase II 量子引力                  9 / 9 attack vector
  Phase III 電磁                     12 / 12 主題
  觀測                               1853 點，Δχ² = −9.8（約 3.1σ）
  結構常數                           4（M, N_h, β, ε），零自由參數

未解（data/problems/ 與 DS_VACUUM_*）
  宇宙學常數                         10⁴⁴ vs 10⁻¹² eV⁴，差約 10⁵⁶
  規範耦合 g、g'                     未導出
  dS vacuum                          未解（文檔註明與弦論共有）
  暗物質粒子候選                     兩處敘述相反（見下註）
```

> **同一量多組值（原文照錄，不代為調和）**：
> ① `V_us`：`README_en-US.md` 用 `√(ε/3) = 0.22694`（0.2%），`CKM_ACCURACY_STATUS` 用 `φ^{−M/11} = 0.2361`（1.7%，Δ-current）。兩式不同，值亦不同。
> ② `N_h = 42`：`README_en-US.md` §4 寫「`N_horizon = ⌊4/ε⌋ = 42`」，但 `4/ε = 25.88`，該式不成立；等值關係實為 `1/ε² = 16φ² = 41.8885`（Phase II AV-2 與 v5.0 JSON 一致）。
> ③ 暗物質質量：主線 `13.68 MeV`（`M_P e⁻⁴⁸ φ^{−1/2}`，0.88%），`p_n_spectrum` n = 4 給 dark photon `81.7 MeV`。
> ④ BAO 的 ΛCDM 對照：`README_en-US.md` 寫 `15.64`，而 `data/comprehensive_validation.json` 的總 χ² 隱含 BAO 增益與此不同；本 README 引用時一律標明來源檔。

## 已閉合關鍵結果（選錄）

- **2026-07-18（`data/cy_search/README.md`）**：`CY₃(36,98)` 在 Kreuzer–Skarke 庫命中——100+ polytopes、`χ = −124`、`Ind(L) = 48`、`Z₂` Wilson line 62 → 3 代；CYTools／PALP／SageMath／WolframScript 四工具鏈交叉驗證 11 項
- **2026-07-18（`data/mass_hierarchy.en-US.md` §5.1）**：9 條質量關係 9/9 通過，全部在 3.4% 內
- **2026-07-19（`data/cy_search/CKM_CLOSURE_en-US.md`）**：`c₂[0] = −288 = −(32 × 9)`，`9 = N_h − M` ⟹ `M = N_h − 9 = 33`；CKM 由 `c₂` 拓撲經 `M = 33` 至三元素
- **2026-07-20（`data/quantum_gravity/00_QUANTUM_GRAVITY_ENTRY_en-US.md`）**：Phase II 9 個 attack vector 全閉——`τ(p→e⁺π⁰) = 1.99×10³⁵ yr`、`S_BH = A/4G`（`1/4 = εφ`）、`r = 0.00149`、`n_s = 0.959 ± 0.006`、`f_NL = +0.06`、`N_e = 16φ² = 41.8885`
- **2026-07-20（`data/cy_search/AUDIT_REPORT.md`）**：文檔自審 12 項，10 項數值正確；CKM 舊式 `φ^{Δk/2}` 判錯——`V_us` 2.6×、`V_cb` 39×、`V_ub` 742×；中微子 seesaw 與 κ 公式差 5×10⁸。錯因寫明：需 6 個 flavor charges 的完整 FN 結構，非 2 個 sector charges 之差
- **2026-07-20（`data/cy_search/CKM_ACCURACY_STATUS_en-US.md`）**：改用 Δ-current `κ(D₉)/κ(D₂₈)` 投影，`V_us` 由 5.4% 收至 1.7%（`φ⁻³`），`V_cb` 0.6%（`φ^{−6.6}`），`V_ub` 5.9%、`δ_CP` 5.9% 仍開放
- **2026-07-21（`data/absolute_yukawa/docs/01_STATUS.md`）**：絕對 Yukawa 九質量——`t`／`b`／`τ` 為輸入，`c` 0.57%、`s` 0.41%、`μ` 0.30%、`e` 3.59%；`d` 夸克 39.6% 偏差由 2-loop RG 修至 2.2%
- **2026-07-21（`data/p_n_spectrum/07_FINAL_SUMMARY.md`）**：`P_n = 6κεβ·M_Pl·(κ²/16π²)^n`，`P₀ = 2.182×10¹⁷ GeV`（0.16%）；光譜 n = 0–6 對應邊界算子至 6-loop 微中子 0.05 eV

## 驗證紀律

本版嚴謹性分六層：入場券 → 結構審計 → 獨立性審計 → 數字紀律 → 記錄紀律 → 路徑與命名。任一層不過，結果只停留「數值候選」。

### 一、入場券：4 Hard Tests

| 測試 | 要求 | 本版對應 |
|------|------|----------|
| ① 零參數自由度 | dof = 0；每加一個可調參數扣一級 | 19 個 SM 參數只用 `{M, N_h, β, ε}` 四常數；但宇宙學擬合仍有 5 參數（`Ω_m`、`h`、`Ω_b h²`、`σ₈`、`n_s`），須與結構常數分賬 |
| ② 可證偽 | 預言須零寬度或可被更精確測量殺 | `θ₂₃ = π/4` 為零寬度；`z_c = 0.6 ± 0.05` 可被 DESI DR3 收窄至 ±0.02；`r = 0.00149` 待 LiteBIRD |
| ③ 樣本外 | 預言先寫死，數據後開 | `Δχ² = −9.8` 於 1853 點全協方差下計算，逐通道獨立偏好 IDCM；`H₀` 同步相位先給 73.05／69.80，後對 SH0ES／TRGB |
| ④ 結構剛性 | 擾動任一參數，結論必須崩 | `κ = (εφ)² = 1/16` 為代數恆等，改 `ε` 則 `κ` 崩；`t_cycle = τ₀e^{1/κ}` 只有 `κ = 1/16` 給出與可觀測宇宙相容的週期（`e¹⁶ = 8.886×10⁶`） |

### 二、結構審計：三鐵律

- **能證偽**：禁「約 X%」。所有質量比寫成 `φ^{-k}` 的封閉式，可被更精確測量直接殺
- **能預言**：至少一個獨立樣本外預言。`V_us` 的兩式（0.22694 與 0.2361）之差正是本層的壓力測試——同一元素兩個結構式只有一個能活
- **自由度能砸**：禁「枚舉 N 個候選揀中 1 個」。`M = 33` 若可由任意整數替換，19 參數的「零參數」即刻變隱藏 dof；本版以 `M = N_h − 9` 與 MERA 深度雙重釘死

### 三、獨立性審計：五反模式

1. **同義反覆** — 計放大因子 `δy/y ÷ δx/x`；若對所有候選同一常數，則 `y = f(x)` 為單調變換，唔算兩個判據。本版實例：`φ` 冪族極密，任何 0.3–6% 的質量比都能凑出一個指數，所以判準必須落在「指數是否為 `{M, N_h}` 的整數組合」，唔係「誤差是否 < 1%」
2. **循環** — 預言公式內含被解釋量。`README_en-US.md` 自承全部公式係 backward-excavated；因此**恢復值唔可以稱前向預言**，本版把它寫成方法論聲明而唔係免責條款
3. **範疇錯** — 樹級 vs RG running（`d` 夸克 39.6% 由 2-loop RG 修至 2.2%）、on-shell vs MS-bar、`M_Z` vs GUT 標度
4. **枚舉即隱藏 dof** — 掃 N 個組合揀中 1 個 ⟹ dof = N；48 份文檔中凡以「凑中」為結論者，一律要求補算子身份
5. **密度家族依賴** — 家族越小統計力越弱；φ 冪族的密度必須與掃描範圍一併報，唔可以只報命中誤差

### 四、數字紀律

- **多源並列**：`V_us` 兩式、`N_h` 兩種寫法、暗物質 13.68 MeV 與 81.7 MeV、BAO 對照值 15.64 與 JSON 值，一律並列並標來源
- **反硬編碼**：關鍵常數須二源以上（結構推導／獨立觀測／數值重算）；只有一源 ⟹ 標未驗
- **自審留痕**：`AUDIT_REPORT.md` 保留 2.6×／39×／742× 與 5×10⁸ 的 FAIL 原文，唔改寫、唔刪除
- **禁區**：見 target 後凑 φ 指數、事後選質量比、以「與 PDG 差 X%」代替結構推導

### 五、記錄紀律

- 每主題一個 `data/<topic>/`，內含 `00_ENTRY`（起手與判準）、`NN_*`（逐輪）、`*_FINAL`／`RESULT`（結論）
- 雙語成對：`_en-US` 與 `_zh-TW` 同名並存；數字兩邊必須一致，否則以計算腳本輸出為準
- 執行證據落 `data/cy_search/validation/`（8 支腳本 + `run_all.sh`）與 `Makefile` 的 `validate-all`
- 後版檔案隔離：`basic/*_v7_*.md` 與 `basic/README_v7.md` 屬 v7.0 遺留，保留原位但唔計入本版結論

### 六、路徑與命名

- 目錄用主題名（`cy_search`、`quantum_gravity`、`em_dynamics`），唔用編號
- 文檔用大寫語義名＋語言後綴（`CKM_CLOSURE_en-US.md`），階段入口固定 `00_*_ENTRY_*`
- 腳本分兩處：`data/cy_search/validation/` 為可重跑驗證，`scripts/` 為攻堅期一次性地挖掘工具（含 SageMath／WolframScript／cohomCalg）
- 版本邊界：本 repo 名用 `IDCM-v6.0--…`，與 v7.0 同名（`IDCM-v7.0--Information-Dynamics-Cosmology-Model`），靠目錄前綴分辨

## O/P/M 系列全列表

> 本 repo 無 O 系列，亦無 repo 原有的統一問題編號（`../problem_register/` 內無 v6.0 記錄）。下表 M1–M23 為本 README 為對照而編的**模組索引**（編號非 repo 原有），每行對應 `data/` 的實際子目錄或文檔。本 repo 亦無 `open_problems_fresh/`。

| 編號 | 標題 | 核心發現 | 狀態 |
|------|------|----------|------|
| M1 | 生成式與遞迴：x² + x − 1 = 0 | 正根 φ⁻¹；C_n = F_n/F_{n+1}；λ = φ⁻² = 0.381966，八步誤差 < 10⁻³；定位為最深可達層，非公理 | 全部閉合 |
| M2 | 四常數閉合：M = 33、N_h = 42、β、ε | ε = φ⁻¹/4 = 0.1545085；κ = (εφ)² = 1/16 為代數恆等；β = φ⁻¹/2；z_c = 0.6 ± 0.05 | 全部閉合 |
| M3 | MERA 深度 M = 33 與指數量子化 | c₂[0] = −288 = −(32 × 9)，9 = N_h − M ⟹ M = 33；k_u = 33β、k_d = 26β − φ⁻⁴、k_l = 19β | 全部閉合 |
| M4 | 視界層數 N_h = 42 與 z_c | 1/ε² = 16φ² = 41.8885，取整 42；z_c 由 DESI DR2 0.58 ± 0.08 與 DES-SN5YR 0.62 ± 0.10 交叉 | 部分閉合 |
| M5 | 費米子九質量：φ 冪譜 | 9 條關係 9/9 通過且在 3.4% 內；絕對值 c 0.57%、s 0.41%、μ 0.30%、e 3.59%；d 由 2-loop RG 修至 2.2% | 部分閉合 |
| M6 | Higgs 質量：m_H = v·φ^(−9β/2) | 125.99 GeV 對 PDG 125.10 GeV，誤差 0.71%；k_H = 9β/2 由 M 與 N_h 組合給出 | 全部閉合 |
| M7 | CKM 四元素：c₂ 拓撲至混合角 | V_us φ⁻³ 1.7%（Δ-current）、V_cb φ^(−6.6) 0.6%；V_ub 5.9%、δ_CP 5.9% 仍偏；舊式判錯 2.6×–742× | 部分閉合 |
| M8 | PMNS 四參數：θ₂₃ = π/4 極大混合 | θ₁₂ 1.08%；θ₁₃ = arcsin(ε(M−1)/M) 0.55%；δ_CP 193.3°（0.9%）；θ₂₃ = π/4 零寬度 | 全部閉合 |
| M9 | 溫伯格角：sin²θ_W = (3/8)φ⁻¹ | 0.23176 對 PDG 0.23122，誤差 0.23%；3/8 由 SU(5) 正規化與 φ⁻¹ 預算比給出 | 全部閉合 |
| M10 | 暗物質質量：M_P·e⁻⁴⁸·φ^(−1/2) | 13.68 MeV（0.88%）；48 = Ind(L) 由 CY₃ 給出；但 problems/dark_matter 仍寫「無暗物質粒子候選」 | 部分閉合 |
| M11 | CY₃(36,98)：KS 庫命中與拓撲驗證 | h¹¹ = 36、h²¹ = 98、χ = −124、Ind(L) = 48；100+ polytopes；四工具鏈 11 項驗證通過 | 全部閉合 |
| M12 | W-field 36D PDE 閉合 | 36 維 PDE 數值閉合，ξ = 10 已驗；對應 SU(3) monad bundle 的 h¹(V) = 3、Ind(V) = −6 | 全部閉合 |
| M13 | 量子引力 Phase II：九個 attack vector | 質子 τ = 1.99×10³⁵ yr；S = A/4G（1/4 = εφ）；r = 0.00149、n_s = 0.959、f_NL = +0.06；N_e = 16φ² | 全部閉合 |
| M14 | 電磁 Phase III：12 主題與 𝒩 凝聚 | EM 為 W-field 集體模而非基本 U(1)；12 主題閉合；但 01 號文檔內文自標 foundation PDE 需重新表述 | 部分閉合 |
| M15 | 全息碼與光速：MERA → C* → φ⁻¹ | v_LR = 8φ⁻¹ 由 Lieb-Robinson 界給出；SYNC 343 步；全息碼文檔在索引中標未完成 | 部分閉合 |
| M16 | 觀測對照：1853 點全協方差 | 合計 Δχ² = −9.8（約 3.1σ）；BAO 6 箱 χ² 9.22、SNe 1820 點 1639.8、RSD 20 點 13.7、S₈ 0.786 | 全部閉合 |
| M17 | H₀ 同步相位：距離階梯分層 | A(r) = ε(r/ξ)^β 令 H₀ 隨錨定尺度分層；Cepheid +0.01σ、TRGB 0.00σ、Planck +1.56σ、JWST −1.85σ | 部分閉合 |
| M18 | 熱死亡與重啟：t_cycle = τ₀e^(1/κ) | κ = 1/16 為唯一給出與可觀測宇宙相容週期的值；e¹⁶ = 8.886×10⁶；僅數量級，無獨立測量 | 部分閉合 |
| M19 | 重子生成：leptogenesis 路徑 | η_B ~ O(10⁻⁷)，對觀測 6.1×10⁻¹⁰ 偏約三個數量級；文檔自評為部分閉合 | 部分閉合 |
| M20 | 宇宙學常數問題 | V_min = −ε²/(4κ) = −0.0955 給 ρ_Λ ~ 10⁴⁴ eV⁴，對觀測 10⁻¹² eV⁴，差約 10⁵⁶ | 開放 |
| M21 | 規範耦合 g、g' 的遞迴來源 | M_W、M_Z 仍用 SM 公式；g 與 g' 未由遞迴常數導出，僅 θ_W 已閉合 | 開放 |
| M22 | dS vacuum 存在性 | 文檔標未解，並註明此困難與弦論共有；moduli 穩定（AV-7）已閉但真空性質未定 | 開放 |
| M23 | P_n 譜：n = 0–6 的物理對應 | P_n = 6κεβ·M_Pl·(κ²/16π²)^n，P₀ = 2.182×10¹⁷ GeV（0.16%）；n = 4 給 dark photon 81.7 MeV | 部分閉合 |

> M4 標部分閉合：`README_en-US.md` 寫 `⌊4/ε⌋ = 42`，數值不成立（4/ε = 25.88）；實際等值關係為 `1/ε² = 16φ²`。
> M7 標部分閉合：`CKM_ACCURACY_STATUS` 自列 `V_ub` 與 `δ_CP` 為待收項。
> M19 標部分閉合：`data/cy_search/BARYOGENESIS_*` 於索引標為部分成立（原文用彩色標記），η_B 與觀測差三個數量級。
> M20／M21／M22 標開放：分別出自 `data/problems/cosmological_constant.en-US.md`、`gauge_couplings.en-US.md`、`DS_VACUUM_DISCLAIMER_*`。