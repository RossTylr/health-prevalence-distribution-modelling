# Health Prevalence & Distribution Modelling for Diagnostic Demand

This repository explores the use of probability density functions (PDFs) to model the prevalence of health conditions and forecast diagnostic service demand, with a focus on the NHS South West region.

The project is divided into two main parts:
1.  **Synthetic Data Exploration**: We begin by using synthetic data to understand how PDFs can represent the complex, variable nature of conditions like frailty, multimorbidity, and other long-term conditions (LTCs).
2.  **Real-World Data Acquisition**: We then use the Public Health England (PHE) Fingertips API to acquire real-world prevalence data and test the assumptions from our initial models.

## Objectives

* To demonstrate how PDFs can capture the **full spectrum of disease severity** and population variance, moving beyond simple average prevalence rates.
* To simulate how demographic factors like **age, location, and deprivation** impact condition prevalence.
* To provide a framework for **estimating diagnostic demand** (e.g., for CT, MRI, ultrasound) based on population health distributions.
* To create a practical, code-based guide to accessing and analysing key public health datasets from the PHE Fingertips API.

## Setup and Installation

To run the notebooks in this repository, you'll need Conda.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/RossTylr/health-prevalence-distribution-modelling.git](https://github.com/RossTylr/health-prevalence-distribution-modelling.git)
    cd health-prevalence-distribution-modelling
    ```

2.  **Create and activate the Conda environment:**
    ```bash
    conda env create -f environment.yml
    conda activate health_modelling
    ```

3.  **Launch Jupyter Notebook or JupyterLab:**
    ```bash
    jupyter notebook
    ```

## Notebook Guide

### Part 1: Synthetic Data & Probability Distributions (Notebooks 1-5)
* **01_introduction_to_prevalence_and_pdfs.ipynb**: Introduces the core concept of using PDFs to model health states over raw counts.
* **02_simulating_frailty_distribution.ipynb**: A deep dive into modelling frailty using a right-skewed Beta distribution to represent the spectrum from fit to severely frail.
* **03_modelling_long_term_conditions_and_multimorbidity.ipynb**: Uses Poisson-like distributions to model the number of LTCs per person and clusters of high-need patients.
* **04_disease_specific_prevalence_distributions.ipynb**: Explores appropriate PDFs for major conditions like CVD, COPD, and Dementia, linking them to specific diagnostic modalities.
* **05_impact_of_demographics_on_prevalence.ipynb**: Shows how to adjust PDF parameters to simulate the impact of age and deprivation on disease distribution.

### Part 2: PHE Fingertips API & Real-World Data (Notebooks 6-10)
* **06_api_exploration_phes_fingertips.ipynb**: A foundational notebook that explores the structure of the Fingertips API, listing available profiles and area types.
* **07_exploring_phof_and_gp_profiles.ipynb**: Fetches and analyses high-level data from the Public Health Outcomes Framework and GP Practice Profiles.
* **08_analysing_disease_specific_profiles_cvd_dementia_cancer.ipynb**: Focuses on priority clinical areas (CVD, Dementia, Cancer) to understand their prevalence across different geographies.
* **09_integrating_wider_determinants_and_vulnerable_groups.ipynb**: Explores data related to social determinants, learning disabilities, and severe mental illness to contextualise health needs.
* **10_testing_distributions_with_real_data.ipynb**: The capstone notebook where we fit the theoretical PDFs from Part 1 to the real-world data extracted from the Fingertips API.

---
**Disclaimer:** The initial models (Notebooks 1-5) use synthetically generated data for illustrative purposes. Real-world data for the NHS South West would be required to build production-level models.