# Speech-to-text pipeline
## <small>Speech recognition in multiple languages</small>

I worked at a provider of automatic speech recognition (ASR), automating the building of ASR systems in multiple languages.

**Skills employed:** Software design, specification gathering, data pipelines, web scraping, databases, PostgreSQL, Python (scrapy, numpy, scipy), Luigi, project design, Linux

<div class='embed-responsive embed-responsive-16by9'><iframe class='embed-responsive-item' frameborder='0' scrolling='no' src='https://plot.ly/~cjdavie/0.embed'></iframe></div>

*Global language coverage, as of July 2016.*

## Speech recognition in many languages

Speechmatics provides cloud-based speech recognition in multiple languages, with a per-hour pricing, and also provides on-premises solutions.

### Challenge

Previously, there was a largely manual process for building ASR systems, using state-of-the-art deep neural net technologies. This manual process worked in English and German, with ambitions for automatically building ASR systems for many world languages. While the process for building these new languages had been proven with German, the process needed to be automated, and made robust, reproducible and scalable to 10s of languages.

### Solution

Building speech recognition systems has two parts - the language model and acoustic model. I gathered the specifications for the acoustic model pipeline, I then designed and my team built this pipeline. We went on to redesign and reimplement the underlying machine learning libraries. This design combined the machine learning technology, some reworking of the software design methods, unit and integration testing and open-source pipeline frameworks.

I also designed the data handling system, including the databases and data ingestion. This allowed rapid storing and processing of many thousands of hours of audio data, in many languages from a range of sources - both internal and external.

The design principles and technologies allowed a robust, maintainable and scalable framework for automatically building a full ASR system, from the initial data to a fully tested model, ready for deployment in the cloud.

### Results

This pipeline successfully built ASR systems for over 20 languages in a year, where the goal was 10. These included French, Spanish and Japanese. The previous manual language building process took many weeks of work, spread over months. This automated pipeline typically takes less than a day of work in total, with the build itself taking a few weeks.

