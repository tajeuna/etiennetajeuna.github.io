---
layout: page
title: Curriculum Vitae
eyebrow: Academic Profile
lead: Professor of Computer Science at the Université du Québec en Outaouais, working in data science and machine learning.
permalink: /cv/
---

{% assign cv_pdf = site.static_files | where: "path", "/CV_Etienne.pdf" | first %}
{% if cv_pdf %}
<p><a class="btn-primary" href="{{ cv_pdf.path | relative_url }}">Download CV (PDF)</a></p>
{% endif %}

## Appointments

- **Director, Computer Science Program**, Université du Québec en Outaouais — since 2026
- **Professor of Computer Science**, Université du Québec en Outaouais — since 2024
- **Adjunct Professor**, Université du Québec à Montréal — since 2024
- **Postdoctoral Fellow in Machine Learning**, Université Laval — 2021–2023 (with Prof. Pascal Germain and Prof. Jacques Corbeil)
- **Research Assistant**, Université de Sherbrooke — 2024 (with Prof. Shengrui Wang and Prof. Djemel Ziou)

## Education

- **Ph.D. in Computer Science**, Université de Sherbrooke, 2020 — *Survival analysis model for predicting the evolution of dynamic graphs: applications to social networks and co-evolving time series*
- **M.Sc. in Computer Science**, Université de Sherbrooke, 2015 — *Tracking communities in dynamic social networks*
- **Master's in Computer Science (MIAGE)**, Université de Picardie Jules Verne, France, 2013
- **Licence in Computer Science**, University of Yaoundé I, Cameroon, 2011

## Industry experience

- **Applied Research Scientist**, Intact Insurance, Montreal — 2022–2023: spatio-temporal modeling of insured driver behavior
- **Senior Data Scientist**, TouchTunes, Montreal — 2022–2023
- **Data Scientist**, Ciena, Ottawa — 2020–2021: predicting early failure symptoms in a production line
- **Applied Research Scientist**, SAP, Montreal — 2016–2018: electricity consumption profiling and forecasting

## Service

- Associate Editor, *Neurocomputing* (Elsevier)
- Organizing Committee Member, ASONAM 2026
- Review Committee Member, Fonds de recherche du Québec (FRQ)
- Reviewer for international conferences and journals in machine learning and data mining

## Awards

- Mitacs Elevate Fellowship (CAD $60,000) — 2020
- Mitacs Accelerate Fellowship (CAD $30,000) — 2020
- BMO Financial Group Academic Excellence Scholarship — 2017

See also [Publications]({{ '/publications/' | relative_url }}), [Teaching]({{ '/teaching/' | relative_url }}), [Students]({{ '/students/' | relative_url }}), and [Funding]({{ '/projects/' | relative_url }}).

<style>
.btn-primary {
  display: inline-block;
  margin-top: .5rem;
  padding: .65em 1.75em;
  background: var(--accent);
  color: #000 !important;
  font-size: .82rem;
  font-weight: 500;
  letter-spacing: .08em;
  text-transform: uppercase;
  border-radius: 3px;
  border-bottom: none !important;
  transition: background .2s, transform .15s;
}
.btn-primary:hover {
  background: var(--accent2);
  transform: translateY(-1px);
}
</style>
