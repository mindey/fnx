[![Travis status](https://img.shields.io/travis/mindey/fnx/master.svg?style=flat)](https://travis-ci.org/mindey/fnx)

# xirr
Irregular(x) internal return rate (irr) and net present value (npv) computation.

    pip install fnx

Then:

```{python}
from fnx.xirr import xirr
from datetime import date

dates = [date(2003,1,1), date(2003,12,31), date(2003,12,31)]

values = [-25000,5000,25000]

xirr(values,dates)
```

Result:

    0.20060121063298536

Compare with:

[google spreadsheets example](https://docs.google.com/spreadsheets/d/1EQ-qpeBcGFJasiq06WCT7I0tiugOmt7iPBY_ySjBgJ0/edit?usp=sharing).
