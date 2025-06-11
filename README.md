# Health Prevalence & Distribution Modelling for Diagnostic Demand

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Project Status: Active Development](https://img.shields.io/badge/Project%20Status-Active%20Development-green)](https://github.com/RossTylr/health-prevalence-distribution-modelling)

This repository explores the use of probability density functions (PDFs) to model the prevalence of health conditions and forecast diagnostic service demand, with a focus on the NHS South West region.

## Project Status
- **Version**: 1.0.0
- **Status**: Active Development
- **Last Updated**: [Current Date]
- **Known Limitations**: 
  - Models in Part 1 use synthetic data for demonstration
  - Real-world validation requires NHS South West data
  - API rate limits may apply when fetching PHE Fingertips data

## Quick Start
```bash
# Clone and setup
git clone https://github.com/RossTylr/health-prevalence-distribution-modelling.git
cd health-prevalence-distribution-modelling
conda env create -f environment.yml
conda activate health_modelling
jupyter notebook
```

## Objectives

* To demonstrate how PDFs can capture the **full spectrum of disease severity** and population variance, moving beyond simple average prevalence rates.
* To simulate how demographic factors like **age, location, and deprivation** impact condition prevalence.
* To provide a framework for **estimating diagnostic demand** (e.g., for CT, MRI, ultrasound) based on population health distributions.
* To create a practical, code-based guide to accessing and analysing key public health datasets from the PHE Fingertips API.

## Requirements
- Python 3.9 or higher
- Conda package manager
- Key dependencies (see environment.yml for full list):
  - pandas >= 1.5.0
  - numpy >= 1.21.0
  - scipy >= 1.7.0
  - matplotlib >= 3.5.0
  - jupyter >= 1.0.0
  - requests >= 2.28.0

## Project Structure
```
health-prevalence-distribution-modelling/
├── notebooks/               # Jupyter notebooks (1-10)
├── data/                    # Data storage directory
│   ├── raw/                # Raw data from PHE Fingertips
│   └── processed/          # Processed datasets
├── src/                    # Source code modules
├── environment.yml         # Conda environment specification
└── README.md              # This file
```

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

### Troubleshooting
- If you encounter SSL certificate errors when accessing the PHE Fingertips API, ensure your Python environment has updated certificates
- For memory issues with large datasets, consider using pandas' chunking functionality
- If conda environment creation fails, try updating conda first: `conda update conda`

## Contributing
We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Public Health England (PHE) Fingertips API for providing the data
- NHS South West for regional context and validation
- Contributors and reviewers of this project

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