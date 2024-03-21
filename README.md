# Job-Matching
My project aims to match resumes in .pdf or .docx format with job postings for Vietnamese positions available on the internet, specifically targeting the role of AI Engineer

## TODO
- [x] Scrape jobs posted on Google Jobs
- [ ] Perform NLP processing on scraped jobs
- [ ] Utilize NLP techniques for skills extraction or summarization to facilitate matching
- [ ] Scale the scraping pipeline to gather all available jobs

## Setup
Installing [anaconda](https://www.anaconda.com/download) or [mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html) (mamba is prefered due to its lightness)

```
$ mamba create -n data python=3.11
$ conda activate data
$ pip install -r requirements.txt
```

## Scraping the jobs from [link](https://www.google.com/search?q=ai+engineer+tuy%E1%BB%83n+d%E1%BB%A5ng&oq=ai+en&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GIAEGIoFMg4IABBFGCcYOxiABBiKBTIGCAEQRRg5MgwIAhAjGCcYgAQYigUyDQgDEAAYgwEYsQMYgAQyBwgEEAAYgAQyBwgFEAAYgAQyBwgGEAAYgAQyBggHEEUYPNIBCDExNDZqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&ved=2ahUKEwiisMKI24SFAxULplYBHRCvB70QudcGKAF6BAgYECw&sxsrf=ACQVn0_8MFqhjalilrK3fV_l-TKkM6Gtdg:1711001977273#htivrt=jobs&htidocid=4Ptk3N01fWIzsD-wAAAAAA%3D%3D&fpstate=tldetail) using [Selenium](https://www.selenium.dev/)
```
$ python tuyendung_scraping.py
```
The output will be a CSV file like in the [sample file](job_vn_posted.csv)
