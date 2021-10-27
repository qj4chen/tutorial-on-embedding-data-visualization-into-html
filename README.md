# tutorial-on-embedding-data-visualization-into-html
> for my beautiful and cute wife only.

this tutorial aims to finish THREE popular tasks concerning data analysis, data visualization and combining it into html file, a.k.a for the purpose of using the analysis elsewhere other than local computer

# Step 1: data analysis
## 1.1 fecth data
Since my wife is interested in financial area and curious about plotting beatiful and interactive k-lines, this tutorial will focus on build plot of such kind.

To fetch the data we want to plot with, we need to install a popular python package named [`tushare`](https://tushare.pro/register) and sign up for a particular token which will be passed into the code for data fetching.

Use your account to log into the [site](https://tushare.pro/) for further steps. Meanwhile, open a prompt / powershell window, and install `tushare` package simply by typing `pip install tushare`, and then downloading and installing process will automatically start.

```python
import tushare as ts

```

