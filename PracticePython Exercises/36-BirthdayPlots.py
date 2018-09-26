#!/usr/bin/env python3

from bokeh.plotting import figure, show, output_file
import calendar

monthsData = BirthdayMonths()
output_file("plot.html")

x = [calendar.month_abbr[month] for month in range(1,13)]
y = [number for number in range(0,11)]
print(x)
print(y)
p = figure(x_range=x)
p.vbar(x=x, top=y, width=1)

show(p)