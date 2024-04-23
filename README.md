# Planet-based snow cover and SWE reconstruction scripts

### This repository contains python scripts used to perform 1) snow cover estimates from PlanetScope commercial satellite imagery, and 2) SWE reconstructions based on snow cover and snowmelt rates from snow pillows. These scripts correspond to Pflug et al., (2024) [insert link], and are listed in the order necessary to produce SWE reconstructions. Scripts include the following:
  - 0_PlanetDownload: PlanetScope downloading scripts using API tools. Users need to define their API download key, domain extents, and additional filters and data-specifications
  - 1_classify_train_model: Scripting that allows users to interactively and visually classify snow presence, snow absence, and image artifacts from PlanetScope imagery, and then train a Random-Forest model for snow classification
  - 2_process_SCA: This code allows users to process snow cover maps using the RF model from 1_classify_train_model, and compare snow cover estimates side-by-side with raw PlanetScope imagery
  - 3_process_DSD: This code compiles the snow cover output by 2_process_SCA to determine the date of snow disappearance (DSD), DSD uncertainty, and DSD anonaly (relative to the domain-average DSD)
  - 4_process_SnowClass: This code classifies four unique snow classes of equal area using the annual-average DSD from 3_process_DSD
  - 5_process_Reconstruction: This code combines the PlanetScope-observed DSD and fractional snow cover evolution, and melt rates observed from snow pillows, to reconstruct spring SWE. More information can be found in Pflug et al., (2024)

### Additional geojsons (geojson_<domainID>.py) show the extents used to query the domains analyzed by Pflug et al., (2024).
