
## 7.1 Intro/Session Overview

<a href="https://www.youtube.com/watch?v=2viqmJ_NpgE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-7-01.jpg"></a>
 
## Links
[Slides](https://www.slideshare.net/TimLiu72/71-ml-zoom-camp-intro-publicpptx)

## Notes

Add notes from the video (PRs are welcome)

1. Install BentoML: `pip install bentoml`
2. Try on [train.ipynb](code/train.ipynb)
3. Add `svc.api(input = JSON(), output = JSON(=))` for use the model with curl and rest
4. Call the service with the following command: `bentoml serve service.py:svc`
5. Add `--reload` to reload the service when the code changes
6. Try the following example:
```
{
  "seniority": 3,
  "home": "owner",
  "time": 36,
  "age": 26,
  "marital": "single",
  "records": "no",
  "job": "freelance",
  "expenses": 35,
  "income": 0.0,
  "assets": 60000.0,
  "debt": 3000.0,
  "amount": 800,
  "price": 1000
}
```
7. List of your bento models: `bentoml models list`
8. Get details of your bento model: `bentoml models get credit_risk_model:sqoxub2pw2iygcep`
9. Create your [bentofile.yaml](code/bentofile.yaml)
10. Build your bento (using a bentofile.yaml) with `bentoml build `
11. Results on ![bentoml build](images/bento-model.PNG)
12. Containerize your bento model with `bentoml containerize credit_risk_model:latest`
13. Working with pydantic on `code/service.py`
14. Install pydanctic with `pip install pydantic`
15. Serving with locust, install locust with `pip install locust`
16. Start a local server with `locust -H http://localhost:3000`
where 3000 is the port where the service is running (bentoml).
17. Open the locust web interface on http://localhost:8089
18. Async-away optimizations with `async` (every request needs to be serviced one by one)
<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

## Additional Issue Support
* Thanks for watching! Depending on your local setup, we do find issues from time to time. If you run into anything strange
we have a big community of BentoML users who would be happy to receive issue feedback: 
[BentoML slack community](https://l.bentoml.com/join-slack-mlzoomcamp). And if you're around shoot me a direct
message and say hi! 😃 

~Tim


## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 7: Production-Ready Machine Learning (Bento ML)](./)
* Next: [Building Your Prediction Service with BentoML](02-build-bento-service.md)