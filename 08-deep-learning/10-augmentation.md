## 8.10 Data augmentation

<a href="https://www.youtube.com/watch?v=aoPfVsS3BDE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-8-10.jpg"></a>

In this video, I had a typo/bug: instead of using `val_gen` for generating images for validation,
I used `train_gen`. That's why adding augmentations didn't help in the video.

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-8-neural-networks-and-deep-learning-250592316)


## Notes

* Possible image transformations
  * Flip
  * Rotation
  * Shift
  * Shear
  * Zoom In/Out
  * Brightness/Contrast
* Choosing augmentations
  * Use your own judgement
  * Look at the dataset, what kind of variations are there?
  * Are the objects always centered?
    * Rotate, Shift.
* Tune it as a hyperparameter
  * Train it for 10-20 epochs, is it better? Yes? (Use it) No? (Don't use it), Same (train for more epochs)
  * We don't change validation, we use original images because we can think this would be the images that ours users upload to our website.


<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>


## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 8: Neural Networks and Deep Learning](./)
* Previous: [Regularization and dropout](09-dropout.md)
* Next: [Training a larger model](11-large-model.md)