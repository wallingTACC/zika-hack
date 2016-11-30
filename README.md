# zika-hack

## Background

This project began as a from scratch effort to develop a portal where users could submit geolocated genomic data which could be analyzed by TACC supercomputers for the presence of mosquito signitures.  It was originally developed as part of the Cloudera Cares+TACC Zika Hackathon #2 on Sep 9th, 2016.  The initial work focused on getting a simple portal up and running that could handle data submissions.  Further work is needed to complete and end-to-end solution.

## Software Stack

The primary software involved is Django for building the portal interface and Agave () for submitting jobs to TACC supercomputers.  In particular, the Agave's python API is utilized for submitting jobs.  Please see the README files in the agave_job and gene_analyze_web sub-folders for more details.

## Future Directions

This was the product of a hackathon, and where it goes from here is completely up to the communities imagination.  Possibilities include:

* Complete the AGACE integration to run gene analysis code on TACC systems.
* Expand the portal to handle additional data submission types, perhaps photos which sould trigger a species detection algorithm, etc..
* Build hooks for other non-AGAVE based job submission platforms.
* Incorporate additional datasets to explore mosquito or disease related data visually.


