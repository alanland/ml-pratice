# coding: utf-8

import matplotlib.pyplot as plt


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2., 1.03 * height, '%s' % float(height))


# plt.bar(left=0, height=1)
# plt.show()

# plt.bar(left=(0, 1), height=(1, 0.5))
# plt.show()

# plt.bar(left=(0, 1), height=(1, 0.5), width=0.35)
# plt.show()

# plt.xlabel(u'性别')
# plt.ylabel(u'人数')
# plt.bar(left=(0, 1), height=(1, 0.5), width=0.35)
# plt.show()

plt.title(u"Gender and Person")
plt.xlabel(u'Gender')
plt.ylabel(u'Persons')
plt.xticks((0, 1), (u'M', u'F'))
rect = plt.bar(left=(0, 1), height=(1, 0.5), width=0.35, align="center", yerr=0.000001)
plt.legend((rect,), (u"Legend",))
autolabel(rect)
plt.show()
