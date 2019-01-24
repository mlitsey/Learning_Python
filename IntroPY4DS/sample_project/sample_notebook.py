import matplotlib.pyplot as plt
#import matplotlib as mpl
import numpy as np

nums = np.random.randint(0,10,100)
fig,plot = plt.subplots()
plot.hist(nums,range=(0,10), align='left', rwidth=0.25)
plot.set_title('freq')
plot.set_xlabel('number')
#plot.set_xticks(range(10))
plot.set_ylabel('freq')
#plot.set_yticks(range(20))
plot.get_yaxis().grid()

plt.show