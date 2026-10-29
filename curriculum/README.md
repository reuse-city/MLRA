# MLRA Curriculum Architecture

The **Material Literacy and Resource Assessment (MLRA)** course is designed as an open, modular online learning programme for makers, repairers, community organizers, and circular economy practitioners. 

Building directly upon the outcomes of the [Circular Material Valuer Curriculum (CMVC)](https://github.com/reuse-city/CMVC), MLRA translates citizen science research into practical, competency-based learning paths.

---

## 🧭 Pedagogical Approach

* **Practice-Oriented & Heuristic:** Focuses on actionable diagnostic methods, sensory tests (touch, sound, flame tests, density), and accessible tools rather than requiring industrial laboratory equipment.
* **Low-Barrier & Multimodal:** Designed for diverse connectivity contexts—featuring concise text summaries, illustrated cheat-sheets, short instructional videos, and downloadable offline guides.
* **One Root, Many Branches:** Built from the ground up for modularity. Local makerspaces and repair cafés can adapt specific modules to reflect their regional material streams, regulations, and repair cultures.

---

## 📚 Core Learning Pathways

The curriculum is structured around three foundational pathways:

```mermaid
graph LR
    A[Pathway 1: Material Identification] --> B[Pathway 2: Diagnostics & Assessment]
    B --> C[Pathway 3: Valuation & Circular Decision-Making]
    C --> D[Community Action & Local Adaptation]
```

### Pathway 1: Material Identification & Sorting
* **Objective:** Enable practitioners to reliably differentiate and categorize materials commonly encountered in repair and waste streams.
* **Key Topics:**
  * Polymers & Plastics: Differentiating common thermoplastics (PET, HDPE, PVC, LDPE, PP, PS) and composites using non-destructive and low-cost tests (float tests, burn tests, tactile/auditory checks).
  * Metals & Alloys: Identifying ferrous vs. non-ferrous metals, surface coatings, oxidation characteristics, and alloy distinctions.
  * Woods, Fibres & Bio-based Materials: Recognizing treated vs. untreated wood, composite boards (MDF, particle board), and natural fibres.
  * Electronic Substrates & Components: Basic recognition of circuit board materials, solder types, and wiring.

### Pathway 2: Condition Diagnostics & Integrity Assessment
* **Objective:** Assess the physical integrity, wear, safety hazards, and residual utility of discarded or recovered goods.
* **Key Topics:**
  * Structural & Mechanical Integrity: Fatigue, stress fractures, corrosion, delamination, and mechanical wear.
  * Electrical & Electronic Safety: Visual inspection for blown capacitors, corrosion/water damage, basic multimeter testing, and electrical safety hazards.
  * Chemical & Contaminant Screening: Identifying hazardous materials (asbestos, leaded solders, heavy metals, toxic paints, hazardous refrigerants) and safe handling practices.
  * Triage Heuristics: Establishing rapid assessment workflows (repairable / harvestable for parts / direct reuse / safe disposal).

### Pathway 3: Valuation & Circular Decision-Making
* **Objective:** Move beyond purely monetary metrics to evaluate the holistic value (embedded energy, material rarity, repairability, social utility) of goods and resources.
* **Key Topics:**
  * Embedded Carbon & Energy: Understanding the ecological savings of extending component life versus raw recycling or replacement.
  * Component Harvesting & Spare Parts Inventory: Strategies for extracting, categorizing, and cataloguing functional parts.
  * Decision Matrices: Developing structured guidelines for choosing between repair, remanufacture, open-hardware retrofitting, or material recovery.
  * Communicating Value: Explaining material trade-offs and repair viability to community members and workshop visitors.

---

## 🛠️ Course Structure (Open edX / OLX Modules)

The online course is planned as 5 self-contained, sequential modules:

| Module | Title | Primary Pathway | Hands-on Project / Assessment |
| :--- | :--- | :--- | :--- |
| **01** | **Foundations of Inclusive Circularity** | Core Concepts | Mapping local material flows and waste streams |
| **02** | **Material Identification in Practice** | Pathway 1 | Building a DIY material sample testing kit |
| **03** | **Diagnostics & Safety Triage** | Pathway 2 | Conducting a complete teardown and condition audit |
| **04** | **Valuation & Circular Resource Strategy** | Pathway 3 | Applying the Circular Decision Matrix to a local product |
| **05** | **Community Workshop & Knowledge Transfer** | Integration | Facilitating a peer triage session or local adaptation |

---

## 🔄 Relationship to the Predecessor Project (CMVC)

The CMVC project laid the groundwork through extensive participatory fieldwork and citizen science with open workshops in 2025. MLRA takes the curriculum framework co-created during CMVC and:
1. Structures it into modular online learning units with formal learning outcomes.
2. Integrates interactive assessments, quizzes, and peer review mechanisms.
3. Prepares the package for deployment on the **Global Innovation Academy (GIA)** Open edX infrastructure.
